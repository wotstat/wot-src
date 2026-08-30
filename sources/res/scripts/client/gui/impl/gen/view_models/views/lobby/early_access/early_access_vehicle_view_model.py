from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.early_access.early_access_vehicle_model import EarlyAccessVehicleModel

class EarlyAccessVehicleViewModel(ViewModel):
    __slots__ = (b'onSelectVehicle', b'onCompare', b'onShowVehiclePreview', b'onShowInHangar', b'onBuyVehicle', b'onAboutEvent', b'onBackToHangar', b'onBackToPrevScreen', b'onBuyTokens', b'onGoToQuests', b'onMoveSpace', b'onStartMoving', b'onAnimationFinished')
    ARG_VEHICLE_CD = b'vehicleCD'

    def __init__(self, properties=10, commands=13):
        super(EarlyAccessVehicleViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentDate(self):
        return self._getNumber(0)

    def setCurrentDate(self, value):
        self._setNumber(0, value)
        return

    def getStartDate(self):
        return self._getNumber(1)

    def setStartDate(self, value):
        self._setNumber(1, value)
        return

    def getEndDate(self):
        return self._getNumber(2)

    def setEndDate(self, value):
        self._setNumber(2, value)
        return

    def getEndProgressionDate(self):
        return self._getNumber(3)

    def setEndProgressionDate(self, value):
        self._setNumber(3, value)
        return

    def getFeatureState(self):
        return self._getString(4)

    def setFeatureState(self, value):
        self._setString(4, value)
        return

    def getCurrentVehicleCD(self):
        return self._getNumber(5)

    def setCurrentVehicleCD(self, value):
        self._setNumber(5, value)
        return

    def getTokensBalance(self):
        return self._getNumber(6)

    def setTokensBalance(self, value):
        self._setNumber(6, value)
        return

    def getVehicles(self):
        return self._getArray(7)

    def setVehicles(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getVehiclesType():
        return EarlyAccessVehicleModel

    def getIsFromTechTree(self):
        return self._getBool(8)

    def setIsFromTechTree(self, value):
        self._setBool(8, value)
        return

    def getIsQuestWidgetEnabled(self):
        return self._getBool(9)

    def setIsQuestWidgetEnabled(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(EarlyAccessVehicleViewModel, self)._initialize()
        self._addNumberProperty(b'currentDate', 0)
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addNumberProperty(b'endProgressionDate', 0)
        self._addStringProperty(b'featureState', b'')
        self._addNumberProperty(b'currentVehicleCD', 0)
        self._addNumberProperty(b'tokensBalance', 0)
        self._addArrayProperty(b'vehicles', Array())
        self._addBoolProperty(b'isFromTechTree', False)
        self._addBoolProperty(b'isQuestWidgetEnabled', False)
        self.onSelectVehicle = self._addCommand(b'onSelectVehicle')
        self.onCompare = self._addCommand(b'onCompare')
        self.onShowVehiclePreview = self._addCommand(b'onShowVehiclePreview')
        self.onShowInHangar = self._addCommand(b'onShowInHangar')
        self.onBuyVehicle = self._addCommand(b'onBuyVehicle')
        self.onAboutEvent = self._addCommand(b'onAboutEvent')
        self.onBackToHangar = self._addCommand(b'onBackToHangar')
        self.onBackToPrevScreen = self._addCommand(b'onBackToPrevScreen')
        self.onBuyTokens = self._addCommand(b'onBuyTokens')
        self.onGoToQuests = self._addCommand(b'onGoToQuests')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onStartMoving = self._addCommand(b'onStartMoving')
        self.onAnimationFinished = self._addCommand(b'onAnimationFinished')
        return
