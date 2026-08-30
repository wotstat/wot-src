from __future__ import absolute_import
import importlib, logging, typing, CGF, Event, GenericComponents, Math, math_utils
from cgf_script.registration import ComponentProperty, registerComponent
from constants import IS_CLIENT, IS_CGF_DUMP
from helpers import dependency
from UIComponents import GamefaceMarkerComponent
if IS_CLIENT:
    from skeletons.gui.battle_session import IBattleSessionProvider
    from CurrentVehicle import g_currentPreviewVehicle
    from skeletons.gui.app_loader import IAppLoader
    from skeletons.gui.impl import IGuiLoader
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    from gui.Scaleform.framework.entities.View import ViewKey
    from gui.app_loader.settings import APP_NAME_SPACE
    from gui.Scaleform.daapi.view.battle.shared.component_marker.markers import AreaMarker
    from gui.Scaleform.daapi.view.battle.shared.component_marker.markers_components import ComponentBitMask
    from gui.impl.pub import WindowImpl
    from frameworks.wulf import WindowFlags, WindowLayer
else:

    class IBattleSessionProvider(object):
        pass


    class IAppLoader(object):
        pass


    class IGuiLoader(object):
        pass


if typing.TYPE_CHECKING:
    import BigWorld
_logger = logging.getLogger(__name__)

@registerComponent
class LobbyFlashMarker(object):
    domain = CGF.Domain.Client
    editorTitle = b'Lobby Flash Marker'
    icon = ComponentProperty(type=CGF.PropertyType.String, editorName=b'marker icon', value=b'gui/maps/icons/marathon/marker/video.png', annotations={b'path': b'*.png'})
    textKey = ComponentProperty(type=CGF.PropertyType.String, editorName=b'marker text key', value=b'#marathon:3dObject/showVideo')


@registerComponent
class LobbyFlashMarkerVisibility(object):
    domain = CGF.Domain.Client
    editorTitle = b'Lobby Flash Marker Visibility'
    mainTankMarkerGO = ComponentProperty(type=CGF.PropertyType.Link, value=CGF.GameObject, editorName=b'non-hero tank marker GO')
    heroTankMarkerGO = ComponentProperty(type=CGF.PropertyType.Link, value=CGF.GameObject, editorName=b'hero tank marker GO')


@registerComponent
class CombatMarker(object):
    group = b'UI'
    editorTitle = b'Combat Marker'
    domain = CGF.Domain.Client
    shape = ComponentProperty(type=CGF.PropertyType.String, value=b'', editorName=b'Shape')
    offset = ComponentProperty(type=CGF.PropertyType.Vector3, value=Math.Vector3(0, 0, 0), editorName=b'offset')
    areaRadius = ComponentProperty(type=CGF.PropertyType.Float, value=0.0, editorName=b'areaRadius')
    disappearanceRadius = ComponentProperty(type=CGF.PropertyType.Float, value=1.0, editorName=b'Disappearance Radius')
    reverseDisappearing = ComponentProperty(type=CGF.PropertyType.Bool, value=False, editorName=b'Reverse disappearing')
    distanceFieldColor = ComponentProperty(type=CGF.PropertyType.String, value=b'white', editorName=b'Distance Field Color')

    def __init__(self):
        super(CombatMarker, self).__init__()
        self.marker = None
        self.markerID = None
        return


class LobbyMarkersSystem(CGF.System):
    if not IS_CGF_DUMP:
        __appLoader = dependency.descriptor(IAppLoader)
    MarkerActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRo(LobbyFlashMarker), CGF.Ro(CGF.TransformComponent))
    MarkerDeactivated = CGF.DeactivateReaction(CGF.GameObject, CGF.ReactRo(LobbyFlashMarker), CGF.Has(CGF.TransformComponent))
    EntitySyncAccess = CGF.AccessReaction(CGF.Ro(GenericComponents.EntityGOSync))
    Reactions = CGF.Reactions(MarkerActivated, MarkerDeactivated, EntitySyncAccess)

    def __init__(self, *args):
        super(LobbyMarkersSystem, self).__init__(*args)
        self.onMarkerComponentAdded = Event.Event()
        self.onMarkerComponentRemoved = Event.Event()
        return

    def update(self):
        entitySyncAccess = self.reaction(self.EntitySyncAccess)
        for gameObject, _ in self.reaction(self.MarkerDeactivated):
            self.handleMarkerRemoved(gameObject, entitySyncAccess)

        for gameObject, flashMarkerComponent, transformComponent in self.reaction(self.MarkerActivated):
            self.handleMarkerAdded(gameObject, flashMarkerComponent, transformComponent, entitySyncAccess)

        return

    def handleMarkerAdded(self, gameObject, flashMarkerComponent, transformComponent, entitySyncAccess):
        entity = self.__getRootEntity(gameObject, entitySyncAccess)
        matrix = transformComponent.worldTransform
        view = self.__getMarkerView()
        if entity is not None and view is not None:
            view.addCgfMarker(entity.id, flashMarkerComponent, matrix)
        return

    def handleMarkerRemoved(self, gameObject, entitySyncAccess):
        entity = self.__getRootEntity(gameObject, entitySyncAccess)
        view = self.__getMarkerView()
        if entity is not None and view is not None:
            view.removeCgfMarker(entity.id)
        return

    def __getRootEntity(self, gameObject, entitySyncAccess):
        rootGameObject = self.hierarchy.getTopMostParent(gameObject)
        goSyncComponent = entitySyncAccess.find(rootGameObject)
        if goSyncComponent is None:
            _logger.error(b'gameObject id=%d, name=%s has no root bigworld entity to show marker', gameObject.id, gameObject.name)
            return
        else:
            return goSyncComponent.entity

    def __getMarkerView(self):
        app = self.__appLoader.getApp(APP_NAME_SPACE.SF_LOBBY)
        return app.containerManager.getViewByKey(ViewKey(VIEW_ALIAS.LOBBY_VEHICLE_MARKER_VIEW))


class LobbyMarkersVisibilitySystem(CGF.System):
    VisibilityActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRo(LobbyFlashMarkerVisibility))
    VisibilityDeactivated = CGF.DeactivateReaction(CGF.GameObject, CGF.ReactRo(LobbyFlashMarkerVisibility))
    VisibilityAccess = CGF.AccessReaction(CGF.Ro(LobbyFlashMarkerVisibility))
    Reactions = CGF.Reactions(VisibilityActivated, VisibilityDeactivated, VisibilityAccess)

    def update(self):
        for gameObject, _ in self.reaction(self.VisibilityDeactivated):
            self.handleVisibilityRemoved(gameObject)

        for gameObject, lobbyFlashMarkerVisibility in self.reaction(self.VisibilityActivated):
            self.handleVisibilityAdded(gameObject, lobbyFlashMarkerVisibility)

        return

    def handleVisibilityAdded(self, gameObject, lobbyFlashMarkerVisibility):
        self.__onHeroTankAction(gameObject, lobbyFlashMarkerVisibility)
        g_currentPreviewVehicle.onSelected += (lambda : self.__onHeroTankAction(gameObject))
        return

    def handleVisibilityRemoved(self, gameObject):
        g_currentPreviewVehicle.onSelected -= (lambda : self.__onHeroTankAction(gameObject))
        return

    def __onHeroTankAction(self, gameObject, visibilityComponent=None):
        component = visibilityComponent
        if component is None:
            visibilityAccess = self.reaction(self.VisibilityAccess)
            component = visibilityAccess.find(gameObject)
        if g_currentPreviewVehicle.isHeroTank and g_currentPreviewVehicle.item:
            self.__activateMarkerFromHeroTank(component, self.gom)
        else:
            self.__activateMarkerFromNonHeroTank(component, self.gom)
        return

    @staticmethod
    def __activateMarkerFromNonHeroTank(component, gameObjectManager):
        if component.heroTankMarkerGO:
            heroMarkerObj = gameObjectManager.gameObject(component.heroTankMarkerGO)
            if heroMarkerObj.valid:
                heroMarkerObj.deactivate()
        if component.mainTankMarkerGO:
            mainMarkerObj = gameObjectManager.gameObject(component.mainTankMarkerGO)
            if mainMarkerObj.valid:
                mainMarkerObj.activate()
        return

    @staticmethod
    def __activateMarkerFromHeroTank(component, gameObjectManager):
        if component.mainTankMarkerGO:
            mainMarkerObj = gameObjectManager.gameObject(component.mainTankMarkerGO)
            if mainMarkerObj.valid:
                mainMarkerObj.deactivate()
        if component.heroTankMarkerGO:
            heroMarkerObj = gameObjectManager.gameObject(component.heroTankMarkerGO)
            if heroMarkerObj.valid:
                heroMarkerObj.activate()
        return


class CombatMarkerSystem(CGF.System):
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    MarkerActivated = CGF.ActivateReaction(CGF.ReactRw(CombatMarker), CGF.Ro(CGF.TransformComponent))
    MarkerDeactivated = CGF.DeactivateReaction(CGF.ReactRo(CombatMarker))
    Reactions = CGF.Reactions(MarkerActivated, MarkerDeactivated)

    def update(self):
        for combatMarker in self.reaction(self.MarkerDeactivated):
            self.onRemovedMarker(combatMarker)

        for combatMarker, transform in self.reaction(self.MarkerActivated):
            self.onAddedMarker(combatMarker, transform)

        return

    def onAddedMarker(self, combatMarker, transform):
        transform = transform.worldTransform
        matrixProduct = math_utils.MatrixProviders.product(transform, math_utils.createTranslationMatrix(combatMarker.offset))
        data = {b'visible': True, 
           b'areaRadius': (combatMarker.areaRadius), 
           b'disappearingRadius': (combatMarker.disappearanceRadius), 
           b'reverseDisappearing': (combatMarker.reverseDisappearing), 
           (ComponentBitMask.MARKER_2D): [
                                        {b'shape': (combatMarker.shape), 
                                           b'min-distance': 0.0, 
                                           b'max-distance': 0.0, 
                                           b'distance': 0.0, 
                                           b'distanceFieldColor': (combatMarker.distanceFieldColor), 
                                           b'displayDistance': False}], 
           b'matrixProduct': matrixProduct, 
           b'bitMask': (ComponentBitMask.MARKER_2D)}
        combatMarker.marker = AreaMarker(data)
        combatMarker.markerID = self.__guiSessionProvider.shared.areaMarker.addMarker(combatMarker.marker)
        return

    def onRemovedMarker(self, combatMarker):
        self.__guiSessionProvider.shared.areaMarker.removeMarker(combatMarker.markerID)
        return


class GFMarkersCreatorSystem(CGF.System):
    __gui = dependency.descriptor(IGuiLoader)
    MarkerActivated = CGF.ActivateReaction(CGF.ReactRw(GamefaceMarkerComponent))
    MarkerDeactivated = CGF.DeactivateReaction(CGF.ReactRo(GamefaceMarkerComponent))
    Reactions = CGF.Reactions(MarkerActivated, MarkerDeactivated)

    def update(self):
        for markerComponent in self.reaction(self.MarkerDeactivated):
            self.onMarkerRemoved(markerComponent)

        for markerComponent in self.reaction(self.MarkerActivated):
            self.onMarkerAdded(markerComponent)

        return

    def onMarkerAdded(self, markerComponent):
        module = importlib.import_module(markerComponent.viewPath)
        if not module or not hasattr(module, markerComponent.viewName):
            _logger.error(b'Cant find view. Module: %s, Name: %s', markerComponent.viewPath, markerComponent.viewName)
            return
        view = getattr(module, markerComponent.viewName)(markerComponent.viewKey)
        window = WindowImpl(WindowFlags.WINDOW, content=view, layer=WindowLayer.MARKER)
        window.load()
        markerComponent.windowID = window.uniqueID
        return

    def onMarkerRemoved(self, markerComponent):
        window = self.__gui.windowsManager.getWindow(markerComponent.windowID)
        if window:
            window.destroy()
        return
