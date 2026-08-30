from __future__ import absolute_import
from collections import namedtuple
from helpers import dependency, i18n
from gui.Scaleform.daapi.view.meta.ProfileSectionMeta import ProfileSectionMeta
from gui.Scaleform.locale.PROFILE import PROFILE
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
from stats_params import BATTLE_ROYALE_STATS_ENABLED
DropdownData = namedtuple(b'DropdownData', (b'useSelf', b'funcName', b'params'))

class ProfileSection(ProfileSectionMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, *args):
        super(ProfileSection, self).__init__()
        self.__isActive = False
        self._battlesType = PROFILE_DROPDOWN_KEYS.ALL
        self._userName = args[0]
        self._userID = args[1]
        self._databaseID = args[2]
        self._selectedData = args[3]
        self._data = None
        self._dossier = None
        self._battleTypeHandlers = {}
        self.__needUpdate = False
        self.__initHandlers()
        return

    def __initHandlers(self):
        self._battleTypeHandlers = {(PROFILE_DROPDOWN_KEYS.ALL): (DropdownData(True, b'_getTotalStatsBlock', {})), 
           (PROFILE_DROPDOWN_KEYS.TEAM): (DropdownData(False, b'getTeam7x7Stats', {})), 
           (PROFILE_DROPDOWN_KEYS.STATICTEAM): (DropdownData(False, b'getRated7x7Stats', {})), 
           (PROFILE_DROPDOWN_KEYS.HISTORICAL): (DropdownData(False, b'getHistoricalStats', {})), 
           (PROFILE_DROPDOWN_KEYS.FORTIFICATIONS): (DropdownData(True, b'_receiveFortDossier', {})), 
           (PROFILE_DROPDOWN_KEYS.FORTIFICATIONS_SORTIES): (DropdownData(False, b'getFortSortiesStats', {})), 
           (PROFILE_DROPDOWN_KEYS.FORTIFICATIONS_BATTLES): (DropdownData(False, b'getFortBattlesStats', {})), 
           (PROFILE_DROPDOWN_KEYS.COMPANY): (DropdownData(False, b'getCompanyStats', {})), 
           (PROFILE_DROPDOWN_KEYS.CLAN): (DropdownData(False, b'getGlobalMapStats', {})), 
           (PROFILE_DROPDOWN_KEYS.FALLOUT): (DropdownData(False, b'getFalloutStats', {})), 
           (PROFILE_DROPDOWN_KEYS.RANKED): (DropdownData(False, b'getRankedStats', {})), 
           (PROFILE_DROPDOWN_KEYS.RANKED_10X10): (DropdownData(False, b'getRanked10x10Stats', {})), 
           (PROFILE_DROPDOWN_KEYS.EPIC_RANDOM): (DropdownData(False, b'getEpicRandomStats', {})), 
           (PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SOLO): (DropdownData(False, b'getBattleRoyaleSoloStats', {})), 
           (PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SQUAD): (DropdownData(False, b'getBattleRoyaleSquadStats', {}))}
        return

    def __getData(self, battleType, obj):
        data = self._battleTypeHandlers.get(battleType)
        if data is None:
            raise SoftException(b'ProfileSection: Unknown battle type: ' + self._battlesType)
        if data.useSelf:
            return getattr(self, data.funcName)(obj, **data.params)
        else:
            return getattr(obj, data.funcName)(**data.params)

    def _populate(self):
        super(ProfileSection, self)._populate()
        self.requestDossier(self._battlesType)
        return

    def _dispose(self):
        self._data = None
        self._dossier = None
        super(ProfileSection, self)._dispose()
        return

    def requestDossier(self, bType):
        self._battlesType = bType
        self.invokeUpdate()
        return

    def onSectionActivated(self):
        return

    def onSectionDeactivated(self):
        return

    @classmethod
    def _getTotalStatsBlock(cls, dossier):
        return dossier.getRandomStats()

    def __receiveDossier(self):
        if self.__isActive and self.__needUpdate:
            self.__needUpdate = False
            accountDossier = self.itemsCache.items.getAccountDossier(self._userID)
            self._sendAccountData(self._getNecessaryStats(accountDossier), accountDossier)
        return

    def _getNecessaryStats(self, accountDossier=None):
        if accountDossier is None:
            accountDossier = self.itemsCache.items.getAccountDossier(self._userID)
        data = self.__getData(self._battlesType, accountDossier)
        return data

    def _receiveFortDossier(self, accountDossier):
        return

    def _sendAccountData(self, targetData, accountDossier):
        self._data = targetData
        self._dossier = accountDossier
        return

    def setActive(self, value):
        self.__isActive = value
        self.__receiveDossier()
        return

    def invokeUpdate(self):
        self._data = None
        self._dossier = None
        self.__needUpdate = True
        self.__receiveDossier()
        return

    @property
    def isActive(self):
        return self.__isActive

    def _formIconLabelInitObject(self, i18key, icon):
        return {b'description': (i18n.makeString(i18key)), b'icon': icon}

    @classmethod
    def _makeBattleTypesDropDown(cls, accountDossier, forVehiclesPage=False):
        dropDownProvider = BattleTypesDropDownItems()
        dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.ALL)
        dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.EPIC_RANDOM)
        if BATTLE_ROYALE_STATS_ENABLED:
            dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SOLO)
            dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SQUAD)
        dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.RANKED)
        dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.RANKED_10X10)
        dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.FALLOUT)
        if accountDossier is not None and accountDossier.getHistoricalStats().getVehicles():
            dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.HISTORICAL)
        dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.TEAM)
        if accountDossier is not None and accountDossier.getRated7x7Stats().getVehicles():
            dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.STATICTEAM)
        dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.CLAN)
        if dependency.instance(ILobbyContext).getServerSettings().isStrongholdsEnabled():
            if forVehiclesPage:
                dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.FORTIFICATIONS_SORTIES)
                dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.FORTIFICATIONS_BATTLES)
            else:
                dropDownProvider.addByKey(PROFILE_DROPDOWN_KEYS.FORTIFICATIONS)
        return dropDownProvider


class BattleTypesDropDownItems(list):

    def addByKey(self, key):
        self.addWithKeyAndLabel(key, i18n.makeString(PROFILE.profile_dropdown_labels(key)))
        return

    def addWithKeyAndLabel(self, key, label):
        self.__addEntry(key, label)
        return

    def __addEntry(self, key, label):
        self.append({b'key': key, b'label': label})
        return
