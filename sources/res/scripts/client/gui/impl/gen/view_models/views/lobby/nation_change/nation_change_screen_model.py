from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_tank_slot_model import NationChangeTankSlotModel

class NationChangeScreenModel(ViewModel):
    __slots__ = (b'onCloseBtnClick', b'onSwitchBtnClick', b'onCancelBtnClick', b'onHangarBtnClick', b'onDogClick')

    def __init__(self, properties=15, commands=5):
        super(NationChangeScreenModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentNation(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentNationType():
        return NationChangeTankSlotModel

    @property
    def targetNation(self):
        return self._getViewModel(1)

    @staticmethod
    def getTargetNationType():
        return NationChangeTankSlotModel

    def getCurrentTankLvl(self):
        return self._getString(2)

    def setCurrentTankLvl(self, value):
        self._setString(2, value)
        return

    def getTargetTankLvl(self):
        return self._getString(3)

    def setTargetTankLvl(self, value):
        self._setString(3, value)
        return

    def getCurrentTankType(self):
        return self._getString(4)

    def setCurrentTankType(self, value):
        self._setString(4, value)
        return

    def getTargetTankType(self):
        return self._getString(5)

    def setTargetTankType(self, value):
        self._setString(5, value)
        return

    def getCurrenTankName(self):
        return self._getString(6)

    def setCurrenTankName(self, value):
        self._setString(6, value)
        return

    def getTargetTankName(self):
        return self._getString(7)

    def setTargetTankName(self, value):
        self._setString(7, value)
        return

    def getCurrentTankSetupsNumber(self):
        return self._getNumber(8)

    def setCurrentTankSetupsNumber(self, value):
        self._setNumber(8, value)
        return

    def getTargetTankSetupsNumber(self):
        return self._getNumber(9)

    def setTargetTankSetupsNumber(self, value):
        self._setNumber(9, value)
        return

    def getCurrentNation(self):
        return self._getString(10)

    def setCurrentNation(self, value):
        self._setString(10, value)
        return

    def getTargetNation(self):
        return self._getString(11)

    def setTargetNation(self, value):
        self._setString(11, value)
        return

    def getCurrentTankTooltipHeader(self):
        return self._getString(12)

    def setCurrentTankTooltipHeader(self, value):
        self._setString(12, value)
        return

    def getCurrentTankTooltipBody(self):
        return self._getString(13)

    def setCurrentTankTooltipBody(self, value):
        self._setString(13, value)
        return

    def getIsSlotAnimPlaying(self):
        return self._getBool(14)

    def setIsSlotAnimPlaying(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(NationChangeScreenModel, self)._initialize()
        self._addViewModelProperty(b'currentNation', NationChangeTankSlotModel())
        self._addViewModelProperty(b'targetNation', NationChangeTankSlotModel())
        self._addStringProperty(b'currentTankLvl', b'')
        self._addStringProperty(b'targetTankLvl', b'')
        self._addStringProperty(b'currentTankType', b'')
        self._addStringProperty(b'targetTankType', b'')
        self._addStringProperty(b'currenTankName', b'')
        self._addStringProperty(b'targetTankName', b'')
        self._addNumberProperty(b'currentTankSetupsNumber', 0)
        self._addNumberProperty(b'targetTankSetupsNumber', 0)
        self._addStringProperty(b'currentNation', b'')
        self._addStringProperty(b'targetNation', b'')
        self._addStringProperty(b'currentTankTooltipHeader', b'')
        self._addStringProperty(b'currentTankTooltipBody', b'')
        self._addBoolProperty(b'isSlotAnimPlaying', False)
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        self.onSwitchBtnClick = self._addCommand(b'onSwitchBtnClick')
        self.onCancelBtnClick = self._addCommand(b'onCancelBtnClick')
        self.onHangarBtnClick = self._addCommand(b'onHangarBtnClick')
        self.onDogClick = self._addCommand(b'onDogClick')
        return
