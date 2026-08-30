from enum import Enum
from frameworks.wulf import ViewModel

class Type(Enum):
    LOOTBOX = b'lootBox'
    VEHICLES = b'vehicles'
    STYLE = b'style'
    STYLE3D = b'style_3d'
    CREWMEMBER = b'tmanToken'
    PREMIUMPLUS = b'premium_plus'
    CREDITS = b'credits'
    GOLD = b'gold'
    CRYSTAL = b'crystal'
    FREEXP = b'freeXP'
    CUSTOMIZATIONS = b'customizations'
    ATTACHMENT = b'attachment'
    EXPERIMENTALEQUIPMENT = b'experimental_equipment'
    COMPONENTS = b'equipCoin'
    IMPROVEDEQUIPMENT = b'improved_equipment'
    BOUNTYEQUIPMENT = b'trophy_equipment'
    STANDARDEQUIPMENT = b'standard_equipment'
    DIRECTIVES = b'battleBooster_gift'
    MENTORINGLICENSE = b'mentoringLicense'
    CREWBOOK = b'crewBook'
    GUIDE = b'guide'
    BROCHURE = b'brochure'
    RECERTIFICATIONFORM = b'recertificationForm'
    BLUEPRINTS = b'blueprints'
    BATTLEBONUSX5 = b'battle_bonus_x5'
    CREWBONUSX3 = b'crew_bonus_x3'
    PERSONALRESERVES = b'personal_reserves'
    CONSUMABLES = b'consumables'
    RATIONS = b'rations'


class RewardsCategoriesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RewardsCategoriesModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(RewardsCategoriesModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'count', 0)
        return
