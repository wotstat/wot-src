from __future__ import absolute_import
import personal_missions
from adisp import adisp_async
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
from gui import SystemMessages
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getDetailedMissionData, getHtmlAwardSheetIcon
from gui.Scaleform.daapi.view.meta.PersonalMissionsQuestAwardScreenMeta import PersonalMissionsQuestAwardScreenMeta
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as _PM
from gui.Scaleform.locale.QUESTS import QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.server_events.events_dispatcher import showTankwomanAward
from gui.server_events.events_helpers import MISSIONS_STATES
from gui.server_events.pm_constants import SOUNDS
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import PersonalMissionsEvent
from gui.shared.formatters import text_styles
from gui.shared.gui_items.Vehicle import getTypeShortUserName
from gui.shared.gui_items.processors import quests as quests_proc
from gui.shared.utils import toUpper
from gui.shared.utils.decorators import adisp_process
from helpers import dependency
from helpers.i18n import makeString as _ms
from shared_utils import first
from skeletons.gui.server_events import IEventsCache
_OPERATION_ID_TO_UI_BACKGROUND = {1: (RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_QUESTAWARD_BG_STUG4), 
   2: (RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_QUESTAWARD_BG_HTC), 
   3: (RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_QUESTAWARD_BG_T55A), 
   4: (RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_QUESTAWARD_BG_OBJECT260), 
   5: (RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_QUESTAWARD_BG_EXCALIBUR), 
   6: (RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_QUESTAWARD_BG_CHIMERA), 
   7: (RES_ICONS.MAPS_ICONS_PERSONALMISSIONS_QUESTAWARD_BG_OBJECT279)}

def _getNextMissionInOperationByID(questID):
    eventsCache = dependency.instance(IEventsCache)
    for branch in personal_missions.PM_BRANCH.V1_BRANCHES:
        quests = eventsCache.getPersonalMissions().getQuestsForBranch(branch)
        if questID in quests:
            questsInOperation = sorted(personal_missions.g_cache.questListByOperationIDChainID(quests[questID].getOperationID(), quests[questID].getChainID()))
            try:
                questInd = questsInOperation.index(questID)
                for nextID in questsInOperation[questInd + 1:]:
                    if quests[nextID].isAvailableToPerform():
                        return nextID

                for nextID in questsInOperation[:questInd + 1]:
                    if quests[nextID].isAvailableToPerform():
                        return nextID

            except ValueError:
                LOG_ERROR((b'Cannot find quest ID {questID} in quests from tile {quests}').format(questID=questID, quests=questsInOperation))
                LOG_CURRENT_EXCEPTION()

    return


class PersonalMissionsQuestAwardScreen(PersonalMissionsQuestAwardScreenMeta):
    _eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, ctx):
        super(PersonalMissionsQuestAwardScreen, self).__init__(ctx)
        self._quest = ctx.get(b'quest')
        self._ctx = ctx.get(b'ctxData')
        self._proxyEvent = ctx.get(b'proxyEvent')
        self._awardListReturned = self._ctx.get(b'awardListReturned', False)
        nextQuestID = _getNextMissionInOperationByID(int(self._quest.getID()))
        branch = self._quest.getPMType().branch
        pmCache = self._eventsCache.getPersonalMissions()
        if nextQuestID is not None and not self._quest.isFinal():
            self._nextQuest = pmCache.getQuestsForBranch(branch)[nextQuestID]
        else:
            self._nextQuest = None
        self._operation = pmCache.getOperationsForBranch(branch)[self._quest.getOperationID()]
        self._mainReward = self._ctx.get(b'isMainReward', False)
        self._addReward = self._ctx.get(b'isAddReward', False)
        self._isAwardListUsed = self._ctx.get(b'isAwardListUsed', False)
        return

    def closeView(self):
        if not self.isDisposed():
            self.destroy()
        return

    def onContinueBtnClick(self):
        if not self.isDisposed():
            self.destroy()
        return

    def onNextQuestLinkClick(self):
        if not self.isDisposed():
            if self._addReward and self._nextQuest:
                self._proxyEvent(missionID=self._nextQuest.getID())
            elif self._addReward and not self._nextQuest:
                self.__tryGetAward()
            else:
                self._proxyEvent(missionID=self._quest.getID())
            self.destroy()
        return

    def onOkBtnClick(self):
        if not self.isDisposed():
            self.destroy()
        return

    def onRecruitBtnClick(self):
        if not self.isDisposed():
            self.__tryGetAward()
            self.destroy()
        return

    def onNextQuestBtnClick(self):
        if not self.isDisposed():
            self._processMission(self._nextQuest)
            self.destroy()
        return

    def _populate(self):
        super(PersonalMissionsQuestAwardScreen, self)._populate()
        self.__setData()
        tmBonus = self._quest.getTankmanBonus()
        haveTmBonus = tmBonus.tankman and (self._addReward and not tmBonus.isMain or self._mainReward and tmBonus.isMain)
        if haveTmBonus:
            self.soundManager.playSound(SOUNDS.WOMAN_AWARD_WINDOW)
        else:
            self.soundManager.playSound(SOUNDS.AWARD_WINDOW)
        return

    def _dispose(self):
        self.__fireOnClose()
        self._quest = None
        self._ctx = None
        self._proxyEvent = None
        self._operation = None
        super(PersonalMissionsQuestAwardScreen, self)._dispose()
        return

    def __fireOnClose(self):
        if self._quest.isFinal():
            self.fireEvent(PersonalMissionsEvent(PersonalMissionsEvent.ON_AWARD_SCEEN_CLOSE, ctx={b'operationID': (self._quest.getOperationID()), 
               b'eventID': (self._quest.getID())}), EVENT_BUS_SCOPE.LOBBY)
        return

    @adisp_process(b'updating')
    def _processMission(self, quest):
        result = yield quests_proc.PMQuestSelect(quest.getQuestBranch(), personalMission=quest).request()
        if result and result.userMsg:
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType)
        return

    def __setData(self):
        detailedData = getDetailedMissionData(self._quest)
        status = MISSIONS_STATES.COMPLETED
        isFinal = self._quest.isFinal()
        if self._isAwardListUsed:
            count = text_styles.stats(str(self._quest.getPawnCost()) + getHtmlAwardSheetIcon(self._quest.getQuestBranch()))
            statusLabel = text_styles.bonusAppliedText(_ms(QUESTS.PERSONALMISSION_STATUS_DONEWITHPAWN, count=count))
        elif self._mainReward and self._addReward:
            statusLabel = text_styles.bonusAppliedText(QUESTS.PERSONALMISSION_STATUS_FULLDONE)
            status = MISSIONS_STATES.FULL_COMPLETED
        elif self._addReward:
            statusLabel = text_styles.bonusAppliedText(QUESTS.PERSONALMISSION_STATUS_ONLYADDDONE)
            status = MISSIONS_STATES.FULL_COMPLETED
        else:
            statusLabel = text_styles.bonusAppliedText(QUESTS.PERSONALMISSION_STATUS_ONLYMAINDONE)
        questText = _ms(_PM.QUESTAWARDSCREEN_QUEST, quest=self._quest.getShortUserName())
        dataVO = {b'bgImage': (_OPERATION_ID_TO_UI_BACKGROUND.get(self._quest.getOperationID(), b'')), 
           b'operationText': (text_styles.promoTitle(_ms(_PM.QUESTAWARDSCREEN_OPERATION, operation=self._operation.getUserName()))), 
           b'questText': (toUpper(questText)), 
           b'statusLabel': statusLabel, 
           b'status': status, 
           b'ribbonData': {b'ribbonType': b'ribbon1', 
                           b'rendererLinkage': b'RibbonAwardAnimUI', 
                           b'gap': 20, 
                           b'rendererWidth': 80, 
                           b'rendererHeight': 80, 
                           b'awards': (self.__packAwards(detailedData))}}
        dataVO.update(self.__packQuestConditions(detailedData))
        dataVO.update(self.__packNextQuestTitleSection(isFinal))
        dataVO.update(self.__packButtonsSection(isFinal))
        self.as_setDataS(dataVO)
        return

    def __packNextQuestTitleSection(self, isFinal):
        dataVO = {}
        if self._addReward:
            if self._nextQuest:
                nextQuestTitle = _PM.QUESTAWARDSCREEN_NEXTQUEST_TITLE_QUESTACCEPT
                nextQuestText = self._nextQuest.getUserName()
                dataVO.update({b'nextQuestText': (text_styles.promoTitle(nextQuestText)), b'nextQuestTitle': (text_styles.highlightText(nextQuestTitle))})
            else:
                chainName = getTypeShortUserName(self._quest.getQuestClassifier().classificationAttr)
                nextQuestTitle = _ms(_PM.STATUSPANEL_STATUS_ALLDONE, vehicleClass=chainName)
                dataVO.update({b'nextQuestTitle': (text_styles.highlightText(nextQuestTitle))})
        elif self._isAwardListUsed:
            if isFinal:
                dataVO.update({b'nextQuestTitle': (text_styles.highlightText(QUESTS.PERSONALMISSION_STATUS_LASTDONEWITHPAWN))})
            elif self._quest.isInProgress():
                dataVO.update({b'nextQuestText': (text_styles.promoTitle(self._quest.getUserName())), 
                   b'nextQuestTitle': (text_styles.highlightText(_PM.QUESTAWARDSCREEN_NEXTQUEST_TITLE_QUESTIMPROVE))})
        else:
            dataVO.update({b'nextQuestText': (text_styles.promoTitle(self._quest.getUserName())), 
               b'nextQuestTitle': (text_styles.highlightText(_PM.QUESTAWARDSCREEN_NEXTQUEST_TITLE_QUESTIMPROVE))})
        return dataVO

    def __packButtonsSection(self, isFinal):
        dataVO = {}
        if self._addReward:
            mainLbl = _PM.QUESTAWARDSCREEN_RECRUITBTN_LABEL if isFinal and self._mainReward else _PM.QUESTAWARDSCREEN_OKBTN_LABEL
            dataVO.update({b'mainBtnLabel': mainLbl})
        elif not self._nextQuest and not isFinal or self._isAwardListUsed and not self._quest.isInProgress():
            mainLbl = _PM.QUESTAWARDSCREEN_RECRUITBTN_LABEL if isFinal else _PM.QUESTAWARDSCREEN_OKBTN_LABEL
            dataVO.update({b'mainBtnLabel': mainLbl})
        else:
            extraLbl = _PM.QUESTAWARDSCREEN_RECRUITBTN_LABEL if isFinal else _PM.QUESTAWARDSCREEN_NEXTQUESTBTN_LABEL
            dataVO.update({b'mainBtnLabel': (_PM.QUESTAWARDSCREEN_CONTINUEBTN_LABEL), b'extraBtnLabel': extraLbl})
        return dataVO

    def __packQuestConditions(self, detailedData):
        formatter = detailedData.getAwardScreenConditionsFormatter()
        return formatter.getConditionsData(self._mainReward, self._addReward)

    def __packAwards(self, detailedData):
        awards = detailedData.getAwards(extended=self._awardListReturned)
        result = []
        keys = []
        if self._mainReward:
            keys.append(b'awards')
        if self._addReward or self._awardListReturned:
            keys.append(b'awardsFullyCompleted')
        for key in keys:
            for item in awards.get(key, []):
                label = item[b'label'] if item[b'label'] is not None else b''
                result.append({b'imgSource': (item[b'imgSource']), 
                   b'label': (text_styles.hightlight(label)), 
                   b'align': (item[b'align']), 
                   b'tooltip': (item[b'tooltip']), 
                   b'overlayType': (item[b'overlayType']), 
                   b'isSpecial': (item[b'isSpecial']), 
                   b'specialAlias': (item[b'specialAlias']), 
                   b'specialArgs': (item[b'specialArgs']), 
                   b'isWulfTooltip': (item[b'isWulfTooltip'])})

        return result

    @adisp_process(b'updating')
    def __tryGetAward(self):
        result = yield self.__getPersonalMissionAward()
        if result and result.userMsg:
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType)
        return

    @adisp_async
    @adisp_process(b'updating')
    def __getPersonalMissionAward(self, callback):
        bonus = self._quest.getTankmanBonus()
        needToGetTankman = self._quest.needToGetAddReward() and not bonus.isMain or self._quest.needToGetMainReward() and bonus.isMain
        if needToGetTankman and bonus.tankman is not None:
            showTankwomanAward(self._quest.getID(), first(bonus.tankman.getTankmenData()))
            result = None
        else:
            result = yield quests_proc.PMGetReward(self._quest).request()
        callback(result)
        return
