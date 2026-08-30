import logging, typing
from collections import namedtuple
import BigWorld, Math, ResMgr
from items import vehicles, parseIntCompactDescr, ITEM_TYPES
from vehicle_systems import model_assembler as ma
from vehicle_systems.stricted_loading import makeCallbackWeak
from vehicle_systems.tankStructure import ModelsSetParams
_logger = logging.getLogger(__name__)
_BLUEPRINT_BG_TEXTURE = b'gui/maps/blueprint_bg.png'
_BLUEPRINT_TEXTURE_PATH = b'img://customTexture:blueprint'
_BLUEPRINT_LAYOUTS_PATH = b'gui/blueprint_layouts.xml'
_BpProjections = namedtuple(b'BpProjections', (b'front', b'left', b'top', b'isometric'))
_BpLayout = namedtuple(b'BpLayout', (b'projections', b'lodIdx'))
_BLUEPRINT_DEFAULT_LAYOUT = _BpLayout(_BpProjections(front=Math.Vector4(220, 140, 0.25, 0.94), left=Math.Vector4(560, 140, 0.25, 0.94), top=Math.Vector4(220, 350, 0.25, 0.94), isometric=Math.Vector4(644, 433, 0.5, 0.94)), lodIdx=3)

class BlueprintGenerator(object):

    def __init__(self):
        self.__cachedCompound = {}
        self.__pendingCompound = set()
        self.__layouts = None
        self.__inProgress = None
        return

    def init(self):
        self.__layouts = self.__readConfig()
        BigWorld.enableBlueprintBuilding(True)
        return

    def fini(self):
        self.__cachedCompound.clear()
        self.__pendingCompound.clear()
        self.__layouts = None
        self.__inProgress = None
        BigWorld.enableBlueprintBuilding(False)
        return

    def generate(self, vehicleCD=None, vehicleName=None, clear=False):
        vehicleDescriptor = self.__getVehicleDescr(vehicleCD, vehicleName)
        if vehicleDescriptor is None:
            return
        else:
            if self.__inProgress != vehicleDescriptor.name:
                if clear:
                    BigWorld.clearBlueprint()
                self.__inProgress = vehicleDescriptor.name
                self.__loadVehicleCompound(vehicleDescriptor)
            return self.__getTexturePath()

    def cancel(self, vehicleCD=None, vehicleName=None):
        if self.__inProgress is None:
            return
        else:
            if vehicleName is None:
                vehicleDescriptor = self.__getVehicleDescr(vehicleCD, vehicleName)
                vehicleName = vehicleDescriptor.name if vehicleDescriptor is not None else None
            if vehicleName is not None and self.__inProgress == vehicleName:
                self.__inProgress = None
            return

    @classmethod
    def __getTexturePath(cls):
        return _BLUEPRINT_TEXTURE_PATH

    def __loadVehicleCompound(self, vehicleDescr):
        vehicleName = vehicleDescr.name
        layout = self.__layouts.get(vehicleName, self.__layouts[b'default'])
        if vehicleName in self.__cachedCompound:
            _logger.debug(b'Loaded vehicle compound of "%s" from cache', vehicleName)
            BigWorld.buildBlueprint(self.__cachedCompound[vehicleName], _BLUEPRINT_BG_TEXTURE, layout.projections)
            self.__inProgress = None
            return
        else:
            if vehicleName in self.__pendingCompound:
                _logger.debug(b'Vehicle compound of "%s" is loading at the moment.', vehicleName)
                return
            _logger.debug(b'Loading vehicle compound of "%s".', vehicleName)
            self.__pendingCompound.add(vehicleName)
            resources = (
             ma.prepareCompoundAssembler(vehicleDescr, ModelsSetParams(b'', b'undamaged', []), BigWorld.camera().spaceID, lodIdx=layout.lodIdx, skipMaterials=True),)
            BigWorld.loadResourceListBG(resources, makeCallbackWeak(self.__onResourcesLoaded, vehicleName))
            return

    def __onResourcesLoaded(self, vehicleName, resourceRefs):
        failedIDs = resourceRefs.failedIDs
        if failedIDs and vehicleName in failedIDs:
            _logger.error(b'Failed to load compound model for "%s"', vehicleName)
            return
        else:
            _logger.debug(b'Loaded compound model for "%s"', vehicleName)
            compound = resourceRefs[vehicleName]
            self.__cachedCompound[vehicleName] = compound
            self.__pendingCompound.remove(vehicleName)
            if vehicleName != self.__inProgress:
                return
            layout = self.__layouts.get(vehicleName, self.__layouts[b'default'])
            BigWorld.buildBlueprint(compound, _BLUEPRINT_BG_TEXTURE, layout.projections)
            self.__inProgress = None
            return

    def __readConfig(self):
        layouts = {b'default': _BLUEPRINT_DEFAULT_LAYOUT}
        try:
            try:
                layoutsSection = ResMgr.openSection(_BLUEPRINT_LAYOUTS_PATH)
                if layoutsSection is None:
                    return layouts
                for layout in layoutsSection.values():
                    bpLayout = _BpLayout(_BpProjections(front=layout[b'front'].asVector4, left=layout[b'left'].asVector4, top=layout[b'top'].asVector4, isometric=layout[b'isometric'].asVector4), lodIdx=layout[b'lodIdx'].asInt)
                    if layout.name == b'default':
                        layouts[b'default'] = bpLayout
                        continue
                    for vehicleName in layout[b'vehicles'].asString.split():
                        layouts[vehicleName] = bpLayout

            except Exception:
                _logger.exception(b"Can't read blueprint layouts config")

        finally:
            ResMgr.purge(_BLUEPRINT_LAYOUTS_PATH)

        return layouts

    def __getVehicleDescr(self, vehicleCD=None, vehicleName=None):
        if vehicleCD is not None:
            itemTypeId, nationId, innationId = parseIntCompactDescr(vehicleCD)
        elif vehicleName is not None:
            nationId, innationId = vehicles.g_list.getIDsByName(vehicleName)
        else:
            _logger.error(b'Do not specified correct vehicle int cd or vehicle name!')
            return
        return vehicles.VehicleDescr(typeID=(nationId, innationId))


g_blueprintGenerator = BlueprintGenerator()
