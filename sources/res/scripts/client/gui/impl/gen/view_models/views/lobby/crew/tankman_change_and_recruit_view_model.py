from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.recruit_window.vehicle_item_view_model import VehicleItemViewModel
from gui.impl.gen.view_models.views.lobby.crew.drop_down_item_view_model import DropDownItemViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_change_model import TankmanChangeModel

class TankmanChangeAndRecruitViewModel(ViewModel):
    __slots__ = (b'onNameChange', b'onSurnameChange', b'onNationChange', b'onVehChange', b'onVehTypeChange', b'onRetrainingChange', b'onSpecialtyChange', b'onViewClose', b'onTankmanPhotoChange', b'onTankmanUpdate', b'onSetInVehChange', b'onRecruit')

    def __init__(self, properties=22, commands=12):
        super(TankmanChangeAndRecruitViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentTankman(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentTankmanType():
        return TankmanChangeModel

    @property
    def futureTankman(self):
        return self._getViewModel(1)

    @staticmethod
    def getFutureTankmanType():
        return TankmanChangeModel

    def getIsRecruit(self):
        return self._getBool(2)

    def setIsRecruit(self, value):
        self._setBool(2, value)
        return

    def getIsNameCanBeChanged(self):
        return self._getBool(3)

    def setIsNameCanBeChanged(self, value):
        self._setBool(3, value)
        return

    def getIsPhotoLocked(self):
        return self._getBool(4)

    def setIsPhotoLocked(self, value):
        self._setBool(4, value)
        return

    def getInitialIcon(self):
        return self._getResource(5)

    def setInitialIcon(self, value):
        self._setResource(5, value)
        return

    def getRetraining(self):
        return self._getString(6)

    def setRetraining(self, value):
        self._setString(6, value)
        return

    def getCredits(self):
        return self._getNumber(7)

    def setCredits(self, value):
        self._setNumber(7, value)
        return

    def getSpecialtyGold(self):
        return self._getNumber(8)

    def setSpecialtyGold(self, value):
        self._setNumber(8, value)
        return

    def getRetrainingGold(self):
        return self._getNumber(9)

    def setRetrainingGold(self, value):
        self._setNumber(9, value)
        return

    def getIsEnoughCredits(self):
        return self._getBool(10)

    def setIsEnoughCredits(self, value):
        self._setBool(10, value)
        return

    def getIsEnoughGold(self):
        return self._getBool(11)

    def setIsEnoughGold(self, value):
        self._setBool(11, value)
        return

    def getIsShowCheckBox(self):
        return self._getBool(12)

    def setIsShowCheckBox(self, value):
        self._setBool(12, value)
        return

    def getIsCheckBoxSelected(self):
        return self._getBool(13)

    def setIsCheckBoxSelected(self, value):
        self._setBool(13, value)
        return

    def getCanChangeRetraining(self):
        return self._getBool(14)

    def setCanChangeRetraining(self, value):
        self._setBool(14, value)
        return

    def getNations(self):
        return self._getArray(15)

    def setNations(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getNationsType():
        return DropDownItemViewModel

    def getVehTypes(self):
        return self._getArray(16)

    def setVehTypes(self, value):
        self._setArray(16, value)
        return

    @staticmethod
    def getVehTypesType():
        return DropDownItemViewModel

    def getNames(self):
        return self._getArray(17)

    def setNames(self, value):
        self._setArray(17, value)
        return

    @staticmethod
    def getNamesType():
        return DropDownItemViewModel

    def getSurnames(self):
        return self._getArray(18)

    def setSurnames(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getSurnamesType():
        return DropDownItemViewModel

    def getVehicles(self):
        return self._getArray(19)

    def setVehicles(self, value):
        self._setArray(19, value)
        return

    @staticmethod
    def getVehiclesType():
        return VehicleItemViewModel

    def getRetrainings(self):
        return self._getArray(20)

    def setRetrainings(self, value):
        self._setArray(20, value)
        return

    @staticmethod
    def getRetrainingsType():
        return DropDownItemViewModel

    def getSpecialties(self):
        return self._getArray(21)

    def setSpecialties(self, value):
        self._setArray(21, value)
        return

    @staticmethod
    def getSpecialtiesType():
        return DropDownItemViewModel

    def _initialize(self):
        super(TankmanChangeAndRecruitViewModel, self)._initialize()
        self._addViewModelProperty(b'currentTankman', TankmanChangeModel())
        self._addViewModelProperty(b'futureTankman', TankmanChangeModel())
        self._addBoolProperty(b'isRecruit', False)
        self._addBoolProperty(b'isNameCanBeChanged', True)
        self._addBoolProperty(b'isPhotoLocked', False)
        self._addResourceProperty(b'initialIcon', R.invalid())
        self._addStringProperty(b'retraining', b'')
        self._addNumberProperty(b'credits', 0)
        self._addNumberProperty(b'specialtyGold', 0)
        self._addNumberProperty(b'retrainingGold', 0)
        self._addBoolProperty(b'isEnoughCredits', True)
        self._addBoolProperty(b'isEnoughGold', True)
        self._addBoolProperty(b'isShowCheckBox', False)
        self._addBoolProperty(b'isCheckBoxSelected', False)
        self._addBoolProperty(b'canChangeRetraining', False)
        self._addArrayProperty(b'nations', Array())
        self._addArrayProperty(b'vehTypes', Array())
        self._addArrayProperty(b'names', Array())
        self._addArrayProperty(b'surnames', Array())
        self._addArrayProperty(b'vehicles', Array())
        self._addArrayProperty(b'retrainings', Array())
        self._addArrayProperty(b'specialties', Array())
        self.onNameChange = self._addCommand(b'onNameChange')
        self.onSurnameChange = self._addCommand(b'onSurnameChange')
        self.onNationChange = self._addCommand(b'onNationChange')
        self.onVehChange = self._addCommand(b'onVehChange')
        self.onVehTypeChange = self._addCommand(b'onVehTypeChange')
        self.onRetrainingChange = self._addCommand(b'onRetrainingChange')
        self.onSpecialtyChange = self._addCommand(b'onSpecialtyChange')
        self.onViewClose = self._addCommand(b'onViewClose')
        self.onTankmanPhotoChange = self._addCommand(b'onTankmanPhotoChange')
        self.onTankmanUpdate = self._addCommand(b'onTankmanUpdate')
        self.onSetInVehChange = self._addCommand(b'onSetInVehChange')
        self.onRecruit = self._addCommand(b'onRecruit')
        return
