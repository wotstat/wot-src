import WWISE
from gui.Scaleform.daapi.view.AchievementsUtils import AchievementsUtils
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import ProfileUtils, getProfileCommonInfo
from gui.Scaleform.daapi.view.meta.ProfileSummaryMeta import ProfileSummaryMeta
from gui.Scaleform.locale.PROFILE import PROFILE
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from PlayerEvents import g_playerEvents
from helpers.i18n import makeString
from gui.Scaleform.locale.MENU import MENU
from gui.shared.gui_items.dossier import dumpDossier
from skeletons.gui.shared import IItemsCache
from gui.battle_control.dog_tag_composer import layoutComposer as dogTagComposer
from skeletons.gui.web import IWebController

class ProfileSummary(ProfileSummaryMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    _webCtrl = dependency.descriptor(IWebController)

    def __init__(self, *args):
        super(ProfileSummary, self).__init__(*args)
        self._isDTFlameEnabled = False
        return

    def setActive(self, value):
        super(ProfileSummary, self).setActive(value)
        self._triggerDogTagFlameSound(value)
        return

    def _sendAccountData(self, targetData, accountDossier):
        super(ProfileSummary, self)._sendAccountData(targetData, accountDossier)
        outcome = ProfileUtils.packProfileDossierInfo(targetData, accountDossier)
        outcome[b'avgDamage'] = ProfileUtils.getValueOrUnavailable(targetData.getAvgDamage())
        outcome[b'maxDestroyed'] = targetData.getMaxFrags()
        vehicle = self.itemsCache.items.getItemByCD(targetData.getMaxFragsVehicle())
        outcome[b'maxDestroyedByVehicle'] = vehicle.shortUserName if vehicle is not None else b''
        outcome[b'globalRating'] = self.getGlobalRating(self._databaseID)
        totalStats = accountDossier.getTotalStats()
        outcome[b'significantAchievements'] = AchievementsUtils.packAchievementList(totalStats.getSignificantAchievements(), accountDossier.getDossierType(), dumpDossier(accountDossier), self._userID is None, False)
        outcome[b'nearestAchievements'] = AchievementsUtils.packAchievementList(totalStats.getNearestAchievements(), accountDossier.getDossierType(), dumpDossier(accountDossier), self._userID is None, True)
        self.as_responseDossierS(self._battlesType, outcome, b'', b'')
        return

    def _populate(self):
        super(ProfileSummary, self)._populate()
        g_playerEvents.onDossiersResync += self.__dossierResyncHandler
        self.__updateUserInfo()
        self.as_setInitDataS(self._getInitData())
        return

    def __dossierResyncHandler(self, *args):
        self.__updateUserInfo()
        return

    def __updateUserInfo(self):
        dossier = self.itemsCache.items.getAccountDossier(self._userID)
        if dossier is not None:
            info = getProfileCommonInfo(self._userName, dossier.getDossierDescr())
            info[b'name'] = makeString(PROFILE.PROFILE_TITLE, info[b'name'])
            info[b'userID'] = str(self._userID)
            registrationDate = makeString(MENU.PROFILE_HEADER_REGISTRATIONDATETITLE) + b' ' + info[b'registrationDate']
            info[b'registrationDate'] = registrationDate
            if info[b'lastBattleDate'] is not None:
                info[b'lastBattleDate'] = makeString(MENU.PROFILE_HEADER_LASTBATTLEDATETITLE) + b' ' + info[b'lastBattleDate']
            else:
                info[b'lastBattleDate'] = b''
            dogTag = self.itemsCache.items.getDogTag(self._userID)
            clanProfile = self._webCtrl.getAccountProfile()
            self._addDogTagInfo(info, dogTag, self._userName, clanProfile)
            self.as_setUserDataS(info)
        return

    def _getInitData(self):
        return {b'commonScores': {b'battles': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_TOTALBATTLES, ProfileUtils.getIconPath(b'battles40x32.png'))), 
                             b'wins': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_TOTALWINS, ProfileUtils.getIconPath(b'wins40x32.png'))), 
                             b'coolSigns': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_COOLSIGNS, ProfileUtils.getIconPath(b'markOfMastery40x32.png'))), 
                             b'maxDestroyed': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_MAXDESTROYED, ProfileUtils.getIconPath(b'maxDestroyed40x32.png'))), 
                             b'maxExperience': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_MAXEXPERIENCE, ProfileUtils.getIconPath(b'maxExp40x32.png'))), 
                             b'avgExperience': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_AVGEXPERIENCE, ProfileUtils.getIconPath(b'avgExp40x32.png'))), 
                             b'hits': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_HITS, ProfileUtils.getIconPath(b'hits40x32.png'))), 
                             b'avgDamage': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_AVGDAMAGE, ProfileUtils.getIconPath(b'avgDamage40x32.png'))), 
                             b'personalScore': (self._formIconLabelInitObject(PROFILE.SECTION_SUMMARY_SCORES_PERSONALSCORE, ProfileUtils.getIconPath(b'battles40x32.png')))}, 
           b'significantAwardsLabel': (PROFILE.SECTION_SUMMARY_LABELS_SIGNIFICANTAWARDS), 
           b'significantAwardsErrorText': (PROFILE.SECTION_SUMMARY_ERRORTEXT_SIGNIFICANTAWARDS)}

    def _dispose(self):
        g_playerEvents.onDossiersResync -= self.__dossierResyncHandler
        self._triggerDogTagFlameSound(False)
        self._disposeRequester()
        super(ProfileSummary, self)._dispose()
        return

    def _addDogTagInfo(self, info, dogTag, playerName, clanProfile):
        if not dogTag:
            return
        dogTag[b'playerName'] = playerName
        dogTag[b'clanTag'] = clanProfile.getClanAbbrev()
        info[b'dogTag'] = dogTagComposer.getModelFromDict(dogTag)
        if info[b'dogTag'][b'isEngravingMaxLevel']:
            self._isDTFlameEnabled = True
            self._triggerDogTagFlameSound(True)
        return

    def _triggerDogTagFlameSound(self, active):
        if not self._isDTFlameEnabled:
            return
        if active:
            WWISE.WW_eventGlobal(backport.sound(R.sounds.dt_flame_start()))
        else:
            WWISE.WW_eventGlobal(backport.sound(R.sounds.dt_flame_stop()))
        return
