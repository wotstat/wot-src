from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel
from gui.impl.gen.view_models.views.buy_vehicle_view.equipment_block_model import EquipmentBlockModel
from gui.impl.gen.view_models.views.buy_vehicle_view.vehicle_congratulation_model import VehicleCongratulationModel

class BuyVehicleViewModel(ViewModel):
    __slots__ = (b'onCloseBtnClick', b'onBuyBtnClick', b'onInHangarClick', b'onBackClick', b'onCommanderLvlChange', b'onCheckboxWithoutCrewChanged', b'onDisclaimerClick')

    def __init__(self, properties=23, commands=7):
        super(BuyVehicleViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def commanderLvlCards(self):
        return self._getViewModel(0)

    @staticmethod
    def getCommanderLvlCardsType():
        return ListModel

    @property
    def equipmentBlock(self):
        return self._getViewModel(1)

    @staticmethod
    def getEquipmentBlockType():
        return EquipmentBlockModel

    @property
    def congratulationAnim(self):
        return self._getViewModel(2)

    @staticmethod
    def getCongratulationAnimType():
        return VehicleCongratulationModel

    def getNation(self):
        return self._getString(3)

    def setNation(self, value):
        self._setString(3, value)
        return

    def getTankLvl(self):
        return self._getString(4)

    def setTankLvl(self, value):
        self._setString(4, value)
        return

    def getTankName(self):
        return self._getString(5)

    def setTankName(self, value):
        self._setString(5, value)
        return

    def getTankType(self):
        return self._getString(6)

    def setTankType(self, value):
        self._setString(6, value)
        return

    def getIsWithoutCommander(self):
        return self._getBool(7)

    def setIsWithoutCommander(self, value):
        self._setBool(7, value)
        return

    def getHasCommanderCheckbox(self):
        return self._getBool(8)

    def setHasCommanderCheckbox(self, value):
        self._setBool(8, value)
        return

    def getCountCrew(self):
        return self._getNumber(9)

    def setCountCrew(self, value):
        self._setNumber(9, value)
        return

    def getVehicleNameTooltip(self):
        return self._getString(10)

    def setVehicleNameTooltip(self, value):
        self._setString(10, value)
        return

    def getTradeOffVehicleIntCD(self):
        return self._getNumber(11)

    def setTradeOffVehicleIntCD(self, value):
        self._setNumber(11, value)
        return

    def getBuyVehicleIntCD(self):
        return self._getNumber(12)

    def setBuyVehicleIntCD(self, value):
        self._setNumber(12, value)
        return

    def getIsToggleBtnVisible(self):
        return self._getBool(13)

    def setIsToggleBtnVisible(self, value):
        self._setBool(13, value)
        return

    def getIsElite(self):
        return self._getBool(14)

    def setIsElite(self, value):
        self._setBool(14, value)
        return

    def getIsRentSelected(self):
        return self._getBool(15)

    def setIsRentSelected(self, value):
        self._setBool(15, value)
        return

    def getIsRestore(self):
        return self._getBool(16)

    def setIsRestore(self, value):
        self._setBool(16, value)
        return

    def getWithoutCommanderAltText(self):
        return self._getResource(17)

    def setWithoutCommanderAltText(self, value):
        self._setResource(17, value)
        return

    def getPriceDescription(self):
        return self._getResource(18)

    def setPriceDescription(self, value):
        self._setResource(18, value)
        return

    def getNoCrewCheckboxLabel(self):
        return self._getResource(19)

    def setNoCrewCheckboxLabel(self, value):
        self._setResource(19, value)
        return

    def getIsContentHidden(self):
        return self._getBool(20)

    def setIsContentHidden(self, value):
        self._setBool(20, value)
        return

    def getBgSource(self):
        return self._getResource(21)

    def setBgSource(self, value):
        self._setResource(21, value)
        return

    def getNeedDisclaimer(self):
        return self._getBool(22)

    def setNeedDisclaimer(self, value):
        self._setBool(22, value)
        return

    def _initialize(self):
        super(BuyVehicleViewModel, self)._initialize()
        self._addViewModelProperty(b'commanderLvlCards', ListModel())
        self._addViewModelProperty(b'equipmentBlock', EquipmentBlockModel())
        self._addViewModelProperty(b'congratulationAnim', VehicleCongratulationModel())
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'tankLvl', b'')
        self._addStringProperty(b'tankName', b'')
        self._addStringProperty(b'tankType', b'')
        self._addBoolProperty(b'isWithoutCommander', False)
        self._addBoolProperty(b'hasCommanderCheckbox', False)
        self._addNumberProperty(b'countCrew', 0)
        self._addStringProperty(b'vehicleNameTooltip', b'')
        self._addNumberProperty(b'tradeOffVehicleIntCD', -1)
        self._addNumberProperty(b'buyVehicleIntCD', 0)
        self._addBoolProperty(b'isToggleBtnVisible', False)
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isRentSelected', False)
        self._addBoolProperty(b'isRestore', False)
        self._addResourceProperty(b'withoutCommanderAltText', R.invalid())
        self._addResourceProperty(b'priceDescription', R.invalid())
        self._addResourceProperty(b'noCrewCheckboxLabel', R.invalid())
        self._addBoolProperty(b'isContentHidden', False)
        self._addResourceProperty(b'bgSource', R.invalid())
        self._addBoolProperty(b'needDisclaimer', False)
        self.onCloseBtnClick = self._addCommand(b'onCloseBtnClick')
        self.onBuyBtnClick = self._addCommand(b'onBuyBtnClick')
        self.onInHangarClick = self._addCommand(b'onInHangarClick')
        self.onBackClick = self._addCommand(b'onBackClick')
        self.onCommanderLvlChange = self._addCommand(b'onCommanderLvlChange')
        self.onCheckboxWithoutCrewChanged = self._addCommand(b'onCheckboxWithoutCrewChanged')
        self.onDisclaimerClick = self._addCommand(b'onDisclaimerClick')
        return
