from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.buttons_bar_model import ButtonsBarModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_slot_model import CrewWidgetSlotModel

class SlotSizeMode(IntEnum):
    DEFAULT = 0
    COMPACT = 1


class CrewWidgetModel(ViewModel):
    __slots__ = (b'onSlotClick', b'onChangeCrewClick', b'onDogMoreInfoClick')

    def __init__(self, properties=12, commands=3):
        super(CrewWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def buttonsBar(self):
        return self._getViewModel(0)

    @staticmethod
    def getButtonsBarType():
        return ButtonsBarModel

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getNation(self):
        return self._getString(3)

    def setNation(self, value):
        self._setString(3, value)
        return

    def getSelectedSlotIdx(self):
        return self._getNumber(4)

    def setSelectedSlotIdx(self, value):
        self._setNumber(4, value)
        return

    def getSlots(self):
        return self._getArray(5)

    def setSlots(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getSlotsType():
        return CrewWidgetSlotModel

    def getIsDisabled(self):
        return self._getBool(6)

    def setIsDisabled(self, value):
        self._setBool(6, value)
        return

    def getHasDog(self):
        return self._getBool(7)

    def setHasDog(self, value):
        self._setBool(7, value)
        return

    def getCurrentLayoutID(self):
        return self._getNumber(8)

    def setCurrentLayoutID(self, value):
        self._setNumber(8, value)
        return

    def getPreviousLayoutID(self):
        return self._getNumber(9)

    def setPreviousLayoutID(self, value):
        self._setNumber(9, value)
        return

    def getIsCrewLocked(self):
        return self._getBool(10)

    def setIsCrewLocked(self, value):
        self._setBool(10, value)
        return

    def getSlotSizeMode(self):
        return SlotSizeMode(self._getNumber(11))

    def setSlotSizeMode(self, value):
        self._setNumber(11, value.value)
        return

    def _initialize(self):
        super(CrewWidgetModel, self)._initialize()
        self._addViewModelProperty(b'buttonsBar', ButtonsBarModel())
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'nation', b'')
        self._addNumberProperty(b'selectedSlotIdx', 0)
        self._addArrayProperty(b'slots', Array())
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'hasDog', False)
        self._addNumberProperty(b'currentLayoutID', 0)
        self._addNumberProperty(b'previousLayoutID', 0)
        self._addBoolProperty(b'isCrewLocked', False)
        self._addNumberProperty(b'slotSizeMode')
        self.onSlotClick = self._addCommand(b'onSlotClick')
        self.onChangeCrewClick = self._addCommand(b'onChangeCrewClick')
        self.onDogMoreInfoClick = self._addCommand(b'onDogMoreInfoClick')
        return
