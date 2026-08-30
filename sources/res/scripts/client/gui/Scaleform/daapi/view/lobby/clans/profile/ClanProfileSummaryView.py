from adisp import adisp_process
from constants import IS_CHINA
from gui.impl import backport
from helpers import i18n, dependency
from gui.clans.settings import CLIENT_CLAN_RESTRICTIONS as _RES
from gui.clans.items import formatField, isValueAvailable, StrongholdStatisticsData
from gui.clans.clan_helpers import isStrongholdsEnabled
from gui.clans.formatters import DUMMY_UNAVAILABLE_DATA
from gui.shared.formatters import icons, text_styles
from gui.shared.utils.functions import makeTooltip
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper
from gui.shared.events import OpenLinkEvent
from gui.Scaleform.genConsts.TEXT_MANAGER_STYLES import TEXT_MANAGER_STYLES as _STYLE
from gui.Scaleform.locale.CLANS import CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.daapi.view.meta.ClanProfileSummaryViewMeta import ClanProfileSummaryViewMeta
from gui.shared.image_helper import ImagesFetchCoordinator
from skeletons.gui.lobby_context import ILobbyContext
_DIVISIONS = (6, 8, 10)

def _stateVO(showRequestBtn, mainStatus=None, tooltip=b'', enabledRequestBtn=False, addStatus=None, showPersonalBtn=False):
    return {b'isShowRequestBtn': showRequestBtn, 
       b'isEnabledRequestBtn': enabledRequestBtn, 
       b'isShowPersonnelBtn': showPersonalBtn, 
       b'mainStatus': (mainStatus or b''), 
       b'additionalStatus': (addStatus or b''), 
       b'tooltip': tooltip}


def _status(i18nKey, style, icon=None):
    message = CLANS.clanprofile_summaryview_statusmsg(i18nKey)
    if icon is not None:
        message = i18n.makeString(message, icon=icons.makeImageTag(icon, 16, 16, -4, 0))
    else:
        message = i18n.makeString(message)
    return style(message)


_STATES = {(_RES.NO_RESTRICTIONS): (_stateVO(True, enabledRequestBtn=True)), 
   (_RES.OWN_CLAN): (_stateVO(False, showPersonalBtn=True)), 
   (_RES.ALREADY_IN_CLAN): (_stateVO(False, addStatus=_status(b'inAnotherClan', text_styles.success))), 
   (_RES.FORBIDDEN_ACCOUNT_TYPE): (_stateVO(False, addStatus=_status(b'banned', text_styles.error))), 
   (_RES.CLAN_IS_FULL): (_stateVO(False, addStatus=_status(b'banned', text_styles.error))), 
   (_RES.CLAN_APPLICATION_ALREADY_SENT): (_stateVO(False, addStatus=_status(b'requestSubmitted', text_styles.success))), 
   (_RES.CLAN_INVITE_ALREADY_RECEIVED): (_stateVO(False, addStatus=_status(b'invitationSubmitted', text_styles.success))), 
   (_RES.SENT_INVITES_LIMIT_REACHED): (_stateVO(True, mainStatus=_status(b'inviteLimit', text_styles.alert, RES_ICONS.MAPS_ICONS_LIBRARY_ALERTICON), tooltip=CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_JOINUNAVAILABLE_INVITESHASBEENREACHED)), 
   (_RES.CLAN_CONSCRIPTION_CLOSED): (_stateVO(True, mainStatus=_status(b'requestNotBeConsidered', text_styles.main, RES_ICONS.MAPS_ICONS_LIBRARY_INFORMATIONICON), tooltip=CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_JOINUNAVAILABLE_RECEIVINGREQUESTSCLOSED)), 
   (_RES.RESYNCHRONIZE): (_stateVO(False, addStatus=_status(b'resynchronize', text_styles.main))), 
   (_RES.CLAN_ENTER_COOLDOWN): (_stateVO(True, enabledRequestBtn=False)), 
   (_RES.DEFAULT): (_stateVO(False))}

class StrongholdDataReceiver(object):

    def __init__(self, clanDossier, updateStrongholdCallback):
        self.__disposed = False
        self.__clanDossier = clanDossier
        self.__updateStrongholdCallback = updateStrongholdCallback
        self.__strongholdStats = StrongholdStatisticsData()
        self.__imagesFetchCoordinator = ImagesFetchCoordinator()
        return

    def getStatsVO(self):
        stats = self.__strongholdStats
        isActual = stats.hasSorties() or stats.hasFortBattles()
        rows = (
         (
          b'rageLevel10', stats.getElo10(), isActual,
          CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_FORT_ELO_RAGE_10_BODY),
         (
          b'rageLevel8', stats.getElo8(), isActual,
          CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_FORT_ELO_RAGE_8_BODY),
         (
          b'rageLevel6', stats.getElo6(), isActual,
          CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_FORT_ELO_RAGE_6_BODY),
         (
          b'sortiesPerDay', stats.getSortiesIn28Days(), True,
          CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_FORT_SORTIE_COUNT_28_BODY),
         (
          b'battlesPerDay', stats.getFortBattlesIn28Days(), True,
          CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_FORT_BATTLES_COUNT_28_BODY),
         (
          b'fortLevel', stats.getStrongholdLevel(), True,
          CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_FORT_LEVEL_BODY))
        if stats.getLeagues():
            excludes = (b'rageLevel6', b'rageLevel8', b'rageLevel10')
        else:
            excludes = (b'rageLevel6', b'rageLevel8') if IS_CHINA else ()
        return [{b'local': key, b'value': (DUMMY_UNAVAILABLE_DATA if elo is None or not isStrongholdsEnabled() else elo), b'timeExpired': (True if elo is None else not actual), b'tooltip': tooltip, b'isHidden': False} for key, elo, actual, tooltip in rows if key not in excludes]

    def getLeaguesVO(self):
        return self.__strongholdStats.getLeagues()

    def dispose(self):
        self.__disposed = True
        self.__clanDossier = None
        self.__updateStrongholdCallback = None
        self.__strongholdStats = None
        self.__imagesFetchCoordinator.fini()
        return

    @adisp_process
    def updateStrongholdStatistics(self):
        self.__strongholdStats = yield self.__clanDossier.requestStrongholdStatistics()
        if self.__disposed:
            return
        leagues = self.__strongholdStats.getLeagues()
        for league in leagues:
            emblem = league.get(b'emblem')
            league[b'emblemImage'] = yield self.__imagesFetchCoordinator.fetchImageByUrl(emblem, oneUse=False)
            if self.__disposed:
                return

        self.__updateStrongholdStatistics()
        return

    def __updateStrongholdStatistics(self):
        if self.__updateStrongholdCallback:
            self.__updateStrongholdCallback(self.getStatsVO(), self.getLeaguesVO())
        return


class ClanProfileSummaryView(ClanProfileSummaryViewMeta, UsersInfoHelper):
    _lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        ClanProfileSummaryViewMeta.__init__(self)
        UsersInfoHelper.__init__(self)
        self.__stateMask = 0
        self.__strongholdStatsVOReceiver = None
        self._isGlobalMapEnabled = self._lobbyContext.getServerSettings().isGlobalMapEnabled()
        self._lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        return

    @adisp_process
    def setClanDossier(self, clanDossier):
        super(ClanProfileSummaryView, self).setClanDossier(clanDossier)
        self._showWaiting()
        clanInfo = yield clanDossier.requestClanInfo()
        if not clanInfo.isValid():
            self._dummyMustBeShown = True
            self._updateDummy()
            self._hideWaiting()
            return
        ratings = yield clanDossier.requestClanRatings()
        globalMapStats = yield clanDossier.requestGlobalMapStats()
        if self.isDisposed():
            return
        self._updateClanInfo(clanInfo)
        ratingStrBuilder = text_styles.builder(delimiter=b'\n')
        ratingStrBuilder.addStyledText(text_styles.promoTitle, formatField(getter=ratings.getEfficiency, formatter=backport.getIntegralFormat))
        ratingStrBuilder.addStyledText(text_styles.stats, CLANS.CLANPROFILE_SUMMARYVIEW_TOTALRAGE)
        motto = clanInfo.getMotto()
        if motto:
            description = text_styles.main(motto)
        else:
            description = text_styles.standard(CLANS.CLANPROFILE_SUMMARYVIEW_DEFAULTCLANDESCR)
        hasGlobalMap = globalMapStats.hasGlobalMap() and self._isGlobalMapEnabled
        self.as_setDataS({b'totalRating': (ratingStrBuilder.render()), 
           b'totalRatingTooltip': (CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_TOTALRATING), 
           b'clanDescription': description, 
           b'isShowFortBtn': True, 
           b'isShowClanNavBtn': hasGlobalMap, 
           b'isShowUrlString': (not hasGlobalMap), 
           b'isDetailLinkEnabled': (self._isGlobalMapEnabled)})
        self.as_updateGeneralBlockS(self.__makeGeneralBlock(clanInfo, syncUserInfo=True))
        self.as_updateGlobalMapBlockS(self.__makeGlobalMapBlock(globalMapStats, ratings))
        self.__updateStatus()
        self.__strongholdStatsVOReceiver = StrongholdDataReceiver(clanDossier, self.__updateStrongholdBlock)
        self.__strongholdStatsVOReceiver.updateStrongholdStatistics()
        return

    def onAccountWebVitalInfoChanged(self, fieldName, value):
        self.__updateStatus()
        return

    def onClanWebVitalInfoChanged(self, clanDbID, fieldName, value):
        if clanDbID == self._clanDossier.getDbID():
            self.__updateStatus()
        return

    @adisp_process
    def onAccountClanProfileChanged(self, profile):
        clanInfo = yield self._clanDossier.requestClanInfo()
        if not self.isDisposed():
            self.as_updateGeneralBlockS(self.__makeGeneralBlock(clanInfo))
        return

    def onClanEmblem128x128Received(self, clanDbID, emblem):
        return

    def onClanEmblem256x256Received(self, clanDbID, emblem):
        if emblem:
            self.as_setClanEmblemS(self.getMemoryTexturePath(emblem))
        return

    @adisp_process
    def onUserNamesReceived(self, names):
        clanInfo = yield self._clanDossier.requestClanInfo()
        if not self.isDisposed():
            self.as_updateGeneralBlockS(self.__makeGeneralBlock(clanInfo))
        return

    def hyperLinkGotoDetailsMap(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_PROMO_SUMMARY))
        return

    def hyperLinkGotoMap(self):
        self.fireEvent(OpenLinkEvent(OpenLinkEvent.GLOBAL_MAP_SUMMARY))
        return

    def sendRequestHandler(self):
        self._sendApplication()
        return

    def _onAppSuccessfullySent(self):
        self.__updateStatus()
        return

    def _updateClanEmblem(self, clanDbID):
        self.requestClanEmblem256x256(clanDbID)
        return

    def _updateHeaderState(self):
        return

    def _dispose(self):
        if self.__strongholdStatsVOReceiver:
            self.__strongholdStatsVOReceiver.dispose()
            self.__strongholdStatsVOReceiver = None
        self._lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        super(ClanProfileSummaryView, self)._dispose()
        return

    def __onServerSettingChanged(self, diff):
        ratings = yield self._clanDossier.requestClanRatings()
        globalMapStats = yield self._clanDossier.requestGlobalMapStats()
        if b'isGlobalMapEnabled' in diff or (b'isGlobalMapEnabled', b'_r') in diff:
            self._isGlobalMapEnabled = self._lobbyContext.getServerSettings().isGlobalMapEnabled()
            self.as_updateGlobalMapBlockS(self.__makeGlobalMapBlock(globalMapStats, ratings))
        return

    def __updateStrongholdBlock(self, stats, leagues=None):
        if leagues:
            self.as_updateLeaguesBlockS({b'leagues': (self.__makeLeaguesBlock(leagues))})
        self.as_updateFortBlockS({b'isShowHeader': True, 
           b'header': (text_styles.highTitle(CLANS.CLANPROFILE_MAINWINDOWTAB_FORTIFICATION)), 
           b'statBlocks': (self.__makeStatsBlock(stats)), 
           b'emptyLbl': b'', 
           b'isActivated': True})
        self._hideWaiting()
        return

    def __makeGeneralBlock(self, clanInfo, syncUserInfo=False):
        stats = [
         {b'local': b'commander', 
            b'value': (formatField(getter=clanInfo.getLeaderDbID, formatter=self.getGuiUserName)), 
            b'textStyle': (_STYLE.STATS_TEXT)},
         {b'local': b'totalPlayers', 
            b'value': (formatField(getter=clanInfo.getMembersCount, formatter=backport.getIntegralFormat))}]
        canSeeTreasury = self.webCtrl.getLimits().canSeeTreasury(self._clanDossier)
        if canSeeTreasury.success:
            stats.append({b'local': b'gold', 
               b'value': (formatField(getter=clanInfo.getTreasuryValue, formatter=backport.getIntegralFormat)), 
               b'icon': (RES_ICONS.MAPS_ICONS_LIBRARY_GOLDICON_2)})
        if syncUserInfo:
            self.syncUsersInfo()
        return {b'isShowHeader': False, 
           b'header': b'', 
           b'statBlocks': (self.__makeStatsBlock(stats)), 
           b'isActivated': True}

    def __makeGlobalMapBlock(self, globalMapStats, ratings):
        hasGlobalMap = globalMapStats.hasGlobalMap()
        if hasGlobalMap and self._isGlobalMapEnabled:
            notActual = ratings.getGlobalMapBattlesFor28Days() <= 0
            stats = [
             {b'local': b'rageLevel10', 
                b'value': (formatField(getter=ratings.getGlobalMapEloRating10, formatter=backport.getIntegralFormat)), 
                b'timeExpired': notActual, 
                b'tooltip': (CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_GMAP_ELO_RAGE_10_BODY)},
             {b'local': b'rageLevel8', 
                b'value': (formatField(getter=ratings.getGlobalMapEloRating8, formatter=backport.getIntegralFormat)), 
                b'timeExpired': notActual, 
                b'tooltip': (CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_GMAP_ELO_RAGE_8_BODY)},
             {b'local': b'rageLevel6', 
                b'value': (formatField(getter=ratings.getGlobalMapEloRating6, formatter=backport.getIntegralFormat)), 
                b'timeExpired': notActual, 
                b'tooltip': (CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_GMAP_ELO_RAGE_6_BODY)},
             {b'local': b'battlesCount', 
                b'value': (formatField(getter=ratings.getGlobalMapBattlesFor28Days, formatter=backport.getIntegralFormat)), 
                b'tooltip': (CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_GMAP_BATTLES_COUNT_BODY)},
             {b'local': b'provinces', 
                b'value': (formatField(getter=globalMapStats.getCurrentProvincesCount, formatter=backport.getIntegralFormat)), 
                b'tooltip': (CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_GMAP_PROVINCE_BODY)}]
            statsBlock = self.__makeStatsBlock(stats)
            emptyLbl = b''
        else:
            statsBlock = ()
            if self._isGlobalMapEnabled:
                if isValueAvailable(globalMapStats.hasGlobalMap):
                    emptyLbl = text_styles.standard(CLANS.CLANPROFILE_SUMMARYVIEW_BLOCKLBL_EMPTYGLOBALMAP)
                else:
                    emptyLbl = b'%s %s' % (icons.alert(), text_styles.standard(CLANS.CLANPROFILE_SUMMARYVIEW_NODATA))
            else:
                hasGlobalMap = False
                emptyLbl = emptyLbl = b'%s %s' % (icons.alert(), text_styles.standard(CLANS.GLOBALMAP_DISABLED))
        return {b'isShowHeader': True, b'header': (text_styles.highTitle(CLANS.CLANPROFILE_MAINWINDOWTAB_GLOBALMAP)), 
           b'statBlocks': statsBlock, 
           b'emptyLbl': emptyLbl, 
           b'isActivated': hasGlobalMap}

    def __makeStatsBlock(self, listValues):
        lst = []
        for item in listValues:
            flag = item.get(b'flag', None)
            if flag is not None and not bool(self.__stateMask & flag):
                continue
            localKey = item.get(b'local', None)
            value = item.get(b'value', None)
            isTimeExpired = item.get(b'timeExpired', False)
            tooltipBody = item.get(b'tooltip', None)
            textStyle = item.get(b'textStyle', None)
            isHidden = item.get(b'isHidden', None)
            isUseTextStylePattern = textStyle is not None
            valueStyle = text_styles.stats
            localKey = i18n.makeString(CLANS.clanprofile_summaryview_blocklbl(localKey))
            tooltipHeader = localKey
            if isTimeExpired:
                valueStyle = text_styles.standard
                tooltipBody = CLANS.CLANPROFILE_SUMMARYVIEW_TOOLTIP_RATINGOUTDATED_BODY
            elif tooltipBody is None:
                tooltipBody = None
                tooltipHeader = None
            if not isinstance(value, (str, unicode)):
                value = backport.getIntegralFormat(value)
            icon = item.get(b'icon', None)
            if icon is not None:
                icon = icons.makeImageTag(icon, 16, 16, -4, 0)
                value = icon + b' ' + value
            if isUseTextStylePattern:
                truncateVo = {b'isUseTruncate': isUseTextStylePattern, b'textStyle': textStyle, 
                   b'maxWidthTF': 140}
            else:
                truncateVo = None
            lst.append({b'label': (text_styles.main(localKey)), 
               b'value': ((isUseTextStylePattern or valueStyle)(str(value)) if 1 else value), 
               b'tooltipHeader': tooltipHeader, 
               b'tooltipBody': (i18n.makeString(tooltipBody) if tooltipBody is not None else b''), 
               b'isUseTextStyle': isUseTextStylePattern, 
               b'truncateVo': truncateVo, 
               b'isHidden': isHidden})

        return lst

    def __makeLeaguesBlock(self, leagues):
        leaguesVO = []
        for league in leagues[:len(_DIVISIONS)]:
            division = league.get(b'max_vehicle_level')
            level = division if division in _DIVISIONS else _DIVISIONS[0]
            imgSource = league.get(b'emblemImage') or RES_ICONS.getDefaultLeagueIcon(level)
            elo = league.get(b'elo')
            if elo:
                elo = backport.getNiceNumberFormat(elo)
                label = text_styles.stats(elo) if league.get(b'position') else text_styles.main(elo)
            else:
                label = text_styles.main(DUMMY_UNAVAILABLE_DATA)
            tooltip = league.get(b'tooltip')
            if tooltip:
                tooltip = makeTooltip(tooltip.get(b'header'), tooltip.get(b'body'))
            leaguesVO.append({b'imgSource': imgSource, 
               b'label': label, 
               b'tooltip': tooltip})

        return leaguesVO

    def __updateStatus(self):
        reason = self.webCtrl.getLimits().canSendApplication(self._clanDossier).reason
        self.as_updateStatusS(_STATES[reason])
        return
