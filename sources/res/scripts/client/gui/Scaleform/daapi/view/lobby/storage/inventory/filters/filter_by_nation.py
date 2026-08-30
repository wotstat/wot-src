import nations
from gui import GUI_NATIONS
from gui.Scaleform.daapi.view.meta.ItemsWithTypeAndNationFilterTabViewMeta import ItemsWithTypeAndNationFilterTabViewMeta
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA

class FiltrableInventoryCategoryByNationTabView(ItemsWithTypeAndNationFilterTabViewMeta):

    def __init__(self):
        super(FiltrableInventoryCategoryByNationTabView, self).__init__()
        self.__selectedNationID = nations.NONE_INDEX
        return

    def selectNation(self, id):
        self.__selectedNationID = id
        self._buildItems()
        return

    def resetFilter(self):
        self.__selectedNationID = nations.NONE_INDEX
        super(FiltrableInventoryCategoryByNationTabView, self).resetFilter()
        return

    def _parseLoadedFilters(self, filterDict):
        self.__selectedNationID = filterDict[b'nationID']
        super(FiltrableInventoryCategoryByNationTabView, self)._parseLoadedFilters(filterDict)
        return

    def _prepareDataForFilterSaving(self):
        data = super(FiltrableInventoryCategoryByNationTabView, self)._prepareDataForFilterSaving()
        data[b'nationID'] = self.__selectedNationID
        return data

    def _initFilter(self):
        super(FiltrableInventoryCategoryByNationTabView, self)._initFilter()
        nationsIds = [{b'id': (nations.NONE_INDEX), b'label': (backport.text(R.strings.storage.crewBooks.filters.nation.all()))}]
        for name in GUI_NATIONS:
            if name in nations.AVAILABLE_NAMES:
                nationsIds.append({b'id': (nations.INDICES[name]), b'label': (backport.text(R.strings.menu.nations.dyn(name)()))})

        self.as_initNationFilterS({b'enabled': True, b'selectedIndex': 0, b'data': nationsIds})
        return

    def _shouldShowCounter(self):
        return super(FiltrableInventoryCategoryByNationTabView, self)._shouldShowCounter() or self.__selectedNationID != nations.NONE_INDEX

    def _getFilteredCriteria(self):
        criteria = super(FiltrableInventoryCategoryByNationTabView, self)._getFilteredCriteria()
        if self.__selectedNationID != nations.NONE_INDEX:
            criteria |= REQ_CRITERIA.CREW_ITEM.NATIONS([self.__selectedNationID])
        return criteria
