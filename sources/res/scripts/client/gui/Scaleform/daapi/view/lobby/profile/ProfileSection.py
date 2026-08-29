from collections import namedtuple
from helpers import dependency, i18n
from gui.Scaleform.daapi.view.meta.ProfileSectionMeta import ProfileSectionMeta
from gui.Scaleform.locale.PROFILE import PROFILE
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
from gui.Scaleform.daapi.view.lobby.comp7.comp7_profile_helper import COMP7_ARCHIVE_NAMES, COMP7_SEASON_NUMBERS, getDropdownKeyByArchiveName, getDropdownKeyBySeason
_DropdownData = namedtuple(b'_DropdownData', (b'useSelf', b'funcName', b'params'))

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
        self.__needUpdate = False
        self.__battleTypeHandlers = {}
        self.__initHandlers()
        return

    def __initHandlers(self):
        self.__battleTypeHandlers = {(PROFILE_DROPDOWN_KEYS.ALL): (_DropdownData(True, b'_getTotalStatsBlock', {})), 
           (PROFILE_DROPDOWN_KEYS.TEAM): (_DropdownData(False, b'getTeam7x7Stats', {})), 
           (PROFILE_DROPDOWN_KEYS.STATICTEAM): (_DropdownData(False, b'getRated7x7Stats', {})), 
           (PROFILE_DROPDOWN_KEYS.HISTORICAL): (_DropdownData(False, b'getHistoricalStats', {})), 
           (PROFILE_DROPDOWN_KEYS.FORTIFICATIONS): (_DropdownData(True, b'_receiveFortDossier', {})), 
           (PROFILE_DROPDOWN_KEYS.FORTIFICATIONS_SORTIES): (_DropdownData(False, b'getFortSortiesStats', {})), 
           (PROFILE_DROPDOWN_KEYS.FORTIFICATIONS_BATTLES): (_DropdownData(False, b'getFortBattlesStats', {})), 
           (PROFILE_DROPDOWN_KEYS.COMPANY): (_DropdownData(False, b'getCompanyStats', {})), 
           (PROFILE_DROPDOWN_KEYS.CLAN): (_DropdownData(False, b'getGlobalMapStats', {})), 
           (PROFILE_DROPDOWN_KEYS.FALLOUT): (_DropdownData(False, b'getFalloutStats', {})), 
           (PROFILE_DROPDOWN_KEYS.RANKED): (_DropdownData(False, b'getRankedStats', {})), 
           (PROFILE_DROPDOWN_KEYS.RANKED_10X10): (_DropdownData(False, b'getRanked10x10Stats', {})), 
           (PROFILE_DROPDOWN_KEYS.EPIC_RANDOM): (_DropdownData(False, b'getEpicRandomStats', {})), 
           (PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SOLO): (_DropdownData(False, b'getBattleRoyaleSoloStats', {})), 
           (PROFILE_DROPDOWN_KEYS.BATTLE_ROYALE_SQUAD): (_DropdownData(False, b'getBattleRoyaleSquadStats', {})), 
           (PROFILE_DROPDOWN_KEYS.VERSUS_AI): (_DropdownData(False, b'getVersusAIStats', {}))}
        for archiveName in COMP7_ARCHIVE_NAMES:
            dropdownKey = getDropdownKeyByArchiveName(archiveName)
            self.__battleTypeHandlers[dropdownKey] = _DropdownData(False, b'getComp7Stats', {b'archive': archiveName})

        for season in COMP7_SEASON_NUMBERS:
            dropdownKey = getDropdownKeyBySeason(season)
            self.__battleTypeHandlers[dropdownKey] = _DropdownData(False, b'getComp7Stats', {b'season': season})

        return

    def __getData(self, battleType, obj):
        data = self.__battleTypeHandlers.get(battleType)
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

    def _dataProviderEntryAutoTranslate(self, key):
        return self._dataProviderEntry(key, i18n.makeString(PROFILE.profile_dropdown_labels(key)))

    @classmethod
    def _dataProviderEntry(cls, key, label):
        return {b'key': key, 
           b'label': label}

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
