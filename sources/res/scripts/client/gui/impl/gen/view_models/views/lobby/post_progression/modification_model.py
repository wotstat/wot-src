from enum import Enum
from gui.impl.gen.view_models.common.price_model import PriceModel
from gui.impl.gen.view_models.views.lobby.post_progression.base_modification_model import BaseModificationModel

class RoleCategory(Enum):
    FIREPOWER = b'firepower'
    SURVIVABILITY = b'survivability'
    MOBILITY = b'mobility'
    STEALTH = b'stealth'
    NONE = b'none'


class ModificationModel(BaseModificationModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ModificationModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(4)

    @staticmethod
    def getPriceType():
        return PriceModel

    def getRoleCategory(self):
        return RoleCategory(self._getString(5))

    def setRoleCategory(self, value):
        self._setString(5, value.value)
        return

    def _initialize(self):
        super(ModificationModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceModel())
        self._addStringProperty(b'roleCategory')
        return
