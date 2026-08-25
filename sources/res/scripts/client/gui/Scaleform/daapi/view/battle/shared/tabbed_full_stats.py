from __future__ import absolute_import
import logging, BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from gui.Scaleform.daapi.view.meta.TabbedFullStatsMeta import TabbedFullStatsMeta
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from gui.battle_control.battle_constants import TabsAliases
_logger = logging.getLogger(__name__)

class TabbedFullStatsComponent(TabbedFullStatsMeta):

    def __init__(self):
        super(TabbedFullStatsComponent, self).__init__()
        self.__tabsMap = {}
        return

    @property
    def hasTabs(self):
        return True

    def hasTab(self, alias):
        return alias in self.__tabsMap

    def setActiveTab(self, tabAlias):
        if tabAlias is None:
            self.as_resetActiveTabS()
        else:
            index = self.__tabsMap.get(tabAlias)
            if index is None:
                _logger.error(b"FullStatsComponent doesn't have %s tab", tabAlias)
            else:
                self.as_setActiveTabS(index)
        return

    def _populate(self):
        super(TabbedFullStatsComponent, self)._populate()
        tabs = self._buildTabs(_TabsBuilder())
        for idx, tabData in enumerate(tabs):
            self.__tabsMap[tabData[b'alias']] = idx
            tabData[b'alias'] = tabData[b'alias'].value

        self.as_updateTabsS(tabs)
        return

    def _destroy(self):
        self.__tabsMap = {}
        super(TabbedFullStatsComponent, self)._destroy()
        return

    @staticmethod
    def _buildTabs(builder):
        builder.addStatisticsTab()
        builder.addPersonalQuestsTab()
        builder.addBoostersTab()
        return builder.getTabs()


class _TabsBuilder(object):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        self.__tabs = []
        return

    def addStatisticsTab(self):
        self.__tabs.append({b'label': (backport.text(R.strings.ingame_gui.statistics.tab.line_up.header())), 
           b'alias': (TabsAliases.STATS)})
        return

    def addPersonalQuestsTab(self):
        if self.__lobbyContext.getServerSettings().isPersonalMissionsEnabled():
            self.__tabs.append({b'label': (backport.text(R.strings.ingame_gui.statistics.tab.quests.header())), 
               b'alias': (TabsAliases.QUESTS_PROGRESS)})
        return

    def addBoostersTab(self):
        if self.__isBoosterProcessingAvailable():
            self.__tabs.append({b'label': (backport.text(R.strings.ingame_gui.statistics.tab.personalReserves.header())), 
               b'alias': (TabsAliases.BOOSTERS)})
        return

    def getTabs(self):
        return self.__tabs

    def __isBoosterProcessingAvailable(self):
        return self.__lobbyContext.getServerSettings().personalReservesConfig.isReservesInBattleActivationEnabled and BigWorld.player().hasBonusCap(ARENA_BONUS_TYPE_CAPS.BOOSTERS)
