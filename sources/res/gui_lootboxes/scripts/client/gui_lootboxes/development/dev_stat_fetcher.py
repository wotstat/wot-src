import ResMgr
from bonus_readers import readBonusSection, SUPPORTED_BONUSES, timeDataToUTC
from gui_lootboxes.gui.statistic_helpers.statistic_data_provider import LootBoxStatFetcher
from gui_lootboxes.skeletons.statistic_lootbox_controller import IStatisticLootBoxController
from helpers import dependency
from optional_bonuses import BONUS_MERGERS
FILE_PATH = b'gui_lootboxes/scripts/client/gui_lootboxes/development/devStat.xml'

class LBDevFetcher(LootBoxStatFetcher):

    def onAccountBecomePlayer(self):
        return

    def onAccountBecomeNonPlayer(self):
        return

    def onServerSettingsChanged(self, diff):
        return

    def requestData(self, callback=None):
        data = {}
        sections = ResMgr.openSection(FILE_PATH)
        for _, lb in sections[b'lootBoxes'].items():
            data[lb.readInt(b'id')] = stat = []
            stat.append(timeDataToUTC(lb.readString(b'expires'), default=0))
            stat.append(lb.readInt(b'ver'))
            bonusStat = {}
            for bonus in lb[b'bonuses'].values():
                for key, value in readBonusSection(SUPPORTED_BONUSES, bonus).iteritems():
                    if key in BONUS_MERGERS:
                        BONUS_MERGERS[key](bonusStat, key, value, False, 1, None)

            stat.append(bonusStat)

        callback(data)
        return

    def processResult(self, data):
        self._storage.fillCache(data)
        return


@dependency.replace_none_kwargs(statLootBoxCtrl=IStatisticLootBoxController)
def devStat(statLootBoxCtrl=None):
    statLootBoxCtrl._statLocalCache.registerProvider(b'dev', LBDevFetcher)
    statLootBoxCtrl._statLocalCache.requestBaseStat()
    return
