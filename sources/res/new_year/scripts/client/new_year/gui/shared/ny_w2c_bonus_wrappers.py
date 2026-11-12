from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.awards_formatters import AWARDS_SIZES
from new_year_common.items.components.ny_constants import CurrentNYConstants
from new_year.gui.shared.ny_toy_info import NewYearCurrentToyInfo
from shared_utils import findFirst
from web.web_client_api.common import sanitizeResPath
from web.web_client_api.loot_boxes import BonusAggregateWrapper

class ToyWrapper(BonusAggregateWrapper):

    @classmethod
    def getWrappedBonus(cls, wrappedToys):
        return {b'id': 0, 
           b'type': (CurrentNYConstants.IP_TYPE_CUSTOM_TOYS), 
           b'value': 1, 
           b'rank': (cls._getToysRank(wrappedToys)), 
           b'icon': {(AWARDS_SIZES.SMALL): (sanitizeResPath(backport.image(R.images.new_year.gui.maps.icons.newYear.loot_box.rewards.box())))}, 
           b'name': b'', 
           b'description': b''}

    @classmethod
    def _getToysRank(cls, wrappedToys):
        toysRanks = set()
        for toy in wrappedToys:
            if toy[b'type'] == CurrentNYConstants.IP_TYPE_CUSTOM_ANYOF_TOYS:
                _, _, rank = toy[b'value'][0]
                toysRanks.add(rank)
            else:
                toysRanks.add(NewYearCurrentToyInfo(toy[b'value'].keys()[0]).getRank())

        if len(toysRanks) == 1:
            return findFirst((lambda x: x is not None), toysRanks)
        return -1
