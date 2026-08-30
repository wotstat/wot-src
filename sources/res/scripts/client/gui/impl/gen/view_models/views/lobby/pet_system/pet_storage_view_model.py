from enum import Enum, IntEnum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.pet_system.pet_bonus_model import PetBonusModel
from gui.impl.gen.view_models.views.lobby.pet_system.pet_card_model import PetCardModel
from gui.impl.gen.view_models.views.lobby.pet_system.pet_name_model import PetNameModel
from gui.impl.gen.view_models.views.lobby.pet_system.promotion_model import PromotionModel

class SynergyStateEnum(Enum):
    INCOMPLETE = b'incomplete'
    UPDATEDRECENTLY = b'updatedRecently'
    COMPLETE = b'complete'


class VisibilityStateEnum(IntEnum):
    ALWAYS = 0
    DISABLEANIMATION = 1
    ONLYINTOPETPLACE = 2


class PetStorageViewModel(ViewModel):
    __slots__ = (b'onClose', b'onBonusSelect', b'onPetSelect', b'onCardSelect', b'onInfoPageOpen', b'onSaveVisibility', b'onSaveName', b'onCloseNameSelection')

    def __init__(self, properties=18, commands=8):
        super(PetStorageViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def promotionModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getPromotionModelType():
        return PromotionModel

    def getPetID(self):
        return self._getNumber(1)

    def setPetID(self, value):
        self._setNumber(1, value)
        return

    def getActivePetID(self):
        return self._getNumber(2)

    def setActivePetID(self, value):
        self._setNumber(2, value)
        return

    def getPetNameID(self):
        return self._getNumber(3)

    def setPetNameID(self, value):
        self._setNumber(3, value)
        return

    def getPetType(self):
        return self._getString(4)

    def setPetType(self, value):
        self._setString(4, value)
        return

    def getBreedName(self):
        return self._getString(5)

    def setBreedName(self, value):
        self._setString(5, value)
        return

    def getSynergyState(self):
        return SynergyStateEnum(self._getString(6))

    def setSynergyState(self, value):
        self._setString(6, value.value)
        return

    def getTotalCount(self):
        return self._getNumber(7)

    def setTotalCount(self, value):
        self._setNumber(7, value)
        return

    def getCurrentCount(self):
        return self._getNumber(8)

    def setCurrentCount(self, value):
        self._setNumber(8, value)
        return

    def getBonuses(self):
        return self._getArray(9)

    def setBonuses(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getBonusesType():
        return PetBonusModel

    def getSelectedBonus(self):
        return self._getNumber(10)

    def setSelectedBonus(self, value):
        self._setNumber(10, value)
        return

    def getIsPetSelected(self):
        return self._getBool(11)

    def setIsPetSelected(self, value):
        self._setBool(11, value)
        return

    def getCards(self):
        return self._getArray(12)

    def setCards(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getCardsType():
        return PetCardModel

    def getPetNames(self):
        return self._getArray(13)

    def setPetNames(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getPetNamesType():
        return PetNameModel

    def getVisibilityState(self):
        return VisibilityStateEnum(self._getNumber(14))

    def setVisibilityState(self, value):
        self._setNumber(14, value.value)
        return

    def getHasUniqueName(self):
        return self._getBool(15)

    def setHasUniqueName(self, value):
        self._setBool(15, value)
        return

    def getHasNewNames(self):
        return self._getBool(16)

    def setHasNewNames(self, value):
        self._setBool(16, value)
        return

    def getIsUnsuitableMode(self):
        return self._getBool(17)

    def setIsUnsuitableMode(self, value):
        self._setBool(17, value)
        return

    def _initialize(self):
        super(PetStorageViewModel, self)._initialize()
        self._addViewModelProperty(b'promotionModel', PromotionModel())
        self._addNumberProperty(b'petID', 0)
        self._addNumberProperty(b'activePetID', 0)
        self._addNumberProperty(b'petNameID', 0)
        self._addStringProperty(b'petType', b'')
        self._addStringProperty(b'breedName', b'')
        self._addStringProperty(b'SynergyState')
        self._addNumberProperty(b'totalCount', 0)
        self._addNumberProperty(b'currentCount', 0)
        self._addArrayProperty(b'bonuses', Array())
        self._addNumberProperty(b'selectedBonus', 0)
        self._addBoolProperty(b'isPetSelected', False)
        self._addArrayProperty(b'cards', Array())
        self._addArrayProperty(b'petNames', Array())
        self._addNumberProperty(b'visibilityState')
        self._addBoolProperty(b'hasUniqueName', False)
        self._addBoolProperty(b'hasNewNames', False)
        self._addBoolProperty(b'isUnsuitableMode', False)
        self.onClose = self._addCommand(b'onClose')
        self.onBonusSelect = self._addCommand(b'onBonusSelect')
        self.onPetSelect = self._addCommand(b'onPetSelect')
        self.onCardSelect = self._addCommand(b'onCardSelect')
        self.onInfoPageOpen = self._addCommand(b'onInfoPageOpen')
        self.onSaveVisibility = self._addCommand(b'onSaveVisibility')
        self.onSaveName = self._addCommand(b'onSaveName')
        self.onCloseNameSelection = self._addCommand(b'onCloseNameSelection')
        return
