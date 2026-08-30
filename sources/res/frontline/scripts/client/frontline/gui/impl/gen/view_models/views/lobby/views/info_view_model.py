from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.rank_item_model import RankItemModel
from frontline.gui.impl.gen.view_models.views.lobby.views.skill_category_base_model import SkillCategoryBaseModel

class InfoViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=21, commands=1):
        super(InfoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getValidVehicleLevels(self):
        return self._getArray(0)

    def setValidVehicleLevels(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getValidVehicleLevelsType():
        return int

    def getUnlockableInBattleVehicleLevel(self):
        return self._getNumber(1)

    def setUnlockableInBattleVehicleLevel(self, value):
        self._setNumber(1, value)
        return

    def getIsBattlePassAvailable(self):
        return self._getBool(2)

    def setIsBattlePassAvailable(self, value):
        self._setBool(2, value)
        return

    def getIsFullScreen(self):
        return self._getBool(3)

    def setIsFullScreen(self, value):
        self._setBool(3, value)
        return

    def getStartTimestamp(self):
        return self._getNumber(4)

    def setStartTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(5)

    def setEndTimestamp(self, value):
        self._setNumber(5, value)
        return

    def getSideDestructiblesArmor(self):
        return self._getNumber(6)

    def setSideDestructiblesArmor(self, value):
        self._setNumber(6, value)
        return

    def getBackDestructiblesArmor(self):
        return self._getNumber(7)

    def setBackDestructiblesArmor(self, value):
        self._setNumber(7, value)
        return

    def getDoorDestructiblesArmor(self):
        return self._getNumber(8)

    def setDoorDestructiblesArmor(self, value):
        self._setNumber(8, value)
        return

    def getVentilationDestructiblesArmor(self):
        return self._getNumber(9)

    def setVentilationDestructiblesArmor(self, value):
        self._setNumber(9, value)
        return

    def getMortarRespawnTime(self):
        return self._getNumber(10)

    def setMortarRespawnTime(self, value):
        self._setNumber(10, value)
        return

    def getAirshipRespawnTime(self):
        return self._getNumber(11)

    def setAirshipRespawnTime(self, value):
        self._setNumber(11, value)
        return

    def getPillboxRespawnTime(self):
        return self._getNumber(12)

    def setPillboxRespawnTime(self, value):
        self._setNumber(12, value)
        return

    def getFlamerRespawnTime(self):
        return self._getNumber(13)

    def setFlamerRespawnTime(self, value):
        self._setNumber(13, value)
        return

    def getAirshipCaptureDuration(self):
        return self._getNumber(14)

    def setAirshipCaptureDuration(self, value):
        self._setNumber(14, value)
        return

    def getAirshipHullDamageFactor(self):
        return self._getReal(15)

    def setAirshipHullDamageFactor(self, value):
        self._setReal(15, value)
        return

    def getAirshipTurretDamageFactor(self):
        return self._getReal(16)

    def setAirshipTurretDamageFactor(self, value):
        self._setReal(16, value)
        return

    def getSkillsCategories(self):
        return self._getArray(17)

    def setSkillsCategories(self, value):
        self._setArray(17, value)
        return

    @staticmethod
    def getSkillsCategoriesType():
        return SkillCategoryBaseModel

    def getRanksWithPoints(self):
        return self._getArray(18)

    def setRanksWithPoints(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getRanksWithPointsType():
        return RankItemModel

    def getWinTablePoints(self):
        return self._getArray(19)

    def setWinTablePoints(self, value):
        self._setArray(19, value)
        return

    @staticmethod
    def getWinTablePointsType():
        return int

    def getLoseTablePoints(self):
        return self._getArray(20)

    def setLoseTablePoints(self, value):
        self._setArray(20, value)
        return

    @staticmethod
    def getLoseTablePointsType():
        return int

    def _initialize(self):
        super(InfoViewModel, self)._initialize()
        self._addArrayProperty(b'validVehicleLevels', Array())
        self._addNumberProperty(b'unlockableInBattleVehicleLevel', 0)
        self._addBoolProperty(b'isBattlePassAvailable', False)
        self._addBoolProperty(b'isFullScreen', False)
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addNumberProperty(b'sideDestructiblesArmor', 0)
        self._addNumberProperty(b'backDestructiblesArmor', 0)
        self._addNumberProperty(b'doorDestructiblesArmor', 0)
        self._addNumberProperty(b'ventilationDestructiblesArmor', 0)
        self._addNumberProperty(b'mortarRespawnTime', 0)
        self._addNumberProperty(b'airshipRespawnTime', 0)
        self._addNumberProperty(b'pillboxRespawnTime', 0)
        self._addNumberProperty(b'flamerRespawnTime', 0)
        self._addNumberProperty(b'airshipCaptureDuration', 0)
        self._addRealProperty(b'airshipHullDamageFactor', 0.0)
        self._addRealProperty(b'airshipTurretDamageFactor', 0.0)
        self._addArrayProperty(b'skillsCategories', Array())
        self._addArrayProperty(b'ranksWithPoints', Array())
        self._addArrayProperty(b'winTablePoints', Array())
        self._addArrayProperty(b'loseTablePoints', Array())
        self.onClose = self._addCommand(b'onClose')
        return
