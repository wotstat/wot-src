from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.postbattle.details_group_model import DetailsGroupModel
from gui.impl.gen.view_models.views.lobby.postbattle.premium_bonuses_model import PremiumBonusesModel

class DetailsStatsModel(ViewModel):
    __slots__ = ()
    RECORD_TYPE = b'record'
    EARNINGS_SUBGROUP_TYPE = b'earningsSubgroup'
    EXPENSES_SUBGROUP_TYPE = b'expensesSubgroup'
    CREDITS_GROUP_TYPE = b'creditsGroup'
    XP_GROUP_TYPE = b'xpGroup'
    CRYSTALS_GROUP_TYPE = b'crystalsGroup'
    PREMIUM_EARNINGS_GROUP_TYPE = b'premiumBenefits'

    def __init__(self, properties=2, commands=0):
        super(DetailsStatsModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def premiumBonuses(self):
        return self._getViewModel(0)

    @staticmethod
    def getPremiumBonusesType():
        return PremiumBonusesModel

    def getGroups(self):
        return self._getArray(1)

    def setGroups(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getGroupsType():
        return DetailsGroupModel

    def _initialize(self):
        super(DetailsStatsModel, self)._initialize()
        self._addViewModelProperty(b'premiumBonuses', PremiumBonusesModel())
        self._addArrayProperty(b'groups', Array())
        return
