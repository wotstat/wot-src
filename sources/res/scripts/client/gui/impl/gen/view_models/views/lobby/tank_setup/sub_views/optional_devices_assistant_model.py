from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset import OptionalDevicesAssistantPreset
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset_model_type import OptionalDevicesAssistantPresetModelType

class OptionalDevicesAssistantItemType(Enum):
    STEREOSCOPE = b'stereoscope'
    TURBOCHARGER = b'turbocharger'
    ENHANCEDAIMDRIVES = b'enhancedAimDrives'
    COMMANDERSVIEW = b'commandersView'
    GROUSERS = b'grousers'
    ADDITINVISIBILITYDEVICE = b'additionalInvisibilityDevice'
    RADIOCOMMUNICATION = b'improvedRadioCommunication'
    ANTIFRAGMENTATIONLINING = b'antifragmentationLining'
    CAMOUFLAGENET = b'camouflageNet'
    ROTATIONMECHANISM = b'improvedRotationMechanism'
    VENTILATION = b'improvedVentilation'
    HEALTHRESERVE = b'extraHealthReserve'
    IMPROVEDSIGHTS = b'improvedSights'
    RAMMER = b'tankRammer'
    COATEDOPTICS = b'coatedOptics'
    AIMINGSTABILIZER = b'aimingStabilizer'
    IMPROVEDCONFIGURATION = b'improvedConfiguration'
    MODERNIZEDEXTRAHEALTHRESERVEANTIFRAGMENTATIONLINING = b'modernizedExtraHealthReserveAntifragmentationLining'
    MODERNIZEDTURBOCHARGERROTATIONMECHANISM = b'modernizedTurbochargerRotationMechanism'
    MODERNIZEDAIMDRIVESAIMINGSTABILIZER = b'modernizedAimDrivesAimingStabilizer'
    MODERNIZEDIMPROVEDSIGHTSENHANCEDAIMDRIVES = b'modernizedImprovedSightsEnhancedAimDrives'
    EMPTY = b''


class OptionalDevicesAssistantStateEnum(Enum):
    VISIBLE = b'visible'
    HIDDEN = b'hidden'
    NOTSUITABLEVEHICLE = b'notSuitableVehicle'
    NODATAATALL = b'noDataAtAll'


class OptionalDevicesAssistantModel(ViewModel):
    __slots__ = (b'onPresetSelected',)

    def __init__(self, properties=3, commands=1):
        super(OptionalDevicesAssistantModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def selectedPreset(self):
        return self._getViewModel(0)

    @staticmethod
    def getSelectedPresetType():
        return OptionalDevicesAssistantPresetModelType

    def getOptionalDevicesAssistantPresets(self):
        return self._getArray(1)

    def setOptionalDevicesAssistantPresets(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getOptionalDevicesAssistantPresetsType():
        return OptionalDevicesAssistantPreset

    def getState(self):
        return OptionalDevicesAssistantStateEnum(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(OptionalDevicesAssistantModel, self)._initialize()
        self._addViewModelProperty(b'selectedPreset', OptionalDevicesAssistantPresetModelType())
        self._addArrayProperty(b'optionalDevicesAssistantPresets', Array())
        self._addStringProperty(b'state', OptionalDevicesAssistantStateEnum.HIDDEN.value)
        self.onPresetSelected = self._addCommand(b'onPresetSelected')
        return
