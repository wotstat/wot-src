from __future__ import absolute_import
from functools import partial
import typing
from future.utils import viewitems
from battle_pass_common import BattlePassRewardReason, get3DStyleProgressToken
from frameworks.state_machine import ConditionTransition, State, StateEvent, StateFlags
from gui.battle_pass.battle_pass_helpers import asBPVideoName, getStyleForChapter, getStyleInfoForChapter, makeChapterMediaName, makeProgressionStyleMediaName, showBPFullscreenVideo
from gui.battle_pass.state_machine import lockNotificationManager
from gui.battle_pass.state_machine.state_machine_helpers import isProgressionComplete, packToken, processRewardsToChoose
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE, g_eventBus
from gui.shared.event_dispatcher import showBattlePass, showBattlePassAwardsWindow, showBattlePassRewardsSelectionWindow
from gui.shared.events import LobbySimpleEvent
from helpers import dependency
from shared_utils import CONST_CONTAINER
from skeletons.gui.game_control import IBattlePassController
from skeletons.gui.impl import IGuiLoader, INotificationWindowController
if typing.TYPE_CHECKING:
    from gui.battle_pass.state_machine.machine import BattlePassStateMachine
    from typing import Dict, List, Optional

class BattlePassRewardStateID(CONST_CONTAINER):
    LOBBY = b'lobby'
    LOBBY_START = b'lobby.start'
    LOBBY_WAIT = b'lobby.wait'
    LOBBY_FINAL = b'lobby.final'
    VIDEO = b'video'
    CHOICE = b'choice'
    CHOICE_ITEM = b'choice.item'
    CHOICE_STYLE = b'choice.style'
    CHOICE_PREVIEW = b'choice.preview'
    REWARD = b'reward'
    REWARD_STYLE = b'reward.style'
    REWARD_ANY = b'reward.any'


class StateMachineEventID(object):
    OPEN_PREVIEW = b'choice.event.open_preview'
    CLOSE_PREVIEW = b'choice.event.close_preview'


class LobbyState(State):
    __slots__ = ()
    __notificationManager = dependency.descriptor(INotificationWindowController)
    __battlePass = dependency.descriptor(IBattlePassController)

    def __init__(self):
        super(LobbyState, self).__init__(stateID=BattlePassRewardStateID.LOBBY, flags=StateFlags.SINGULAR | StateFlags.INITIAL)
        return

    @property
    def lobbyStart(self):
        return self.getChildByIndex(0)

    @property
    def lobbyWait(self):
        return self.getChildByIndex(1)

    @property
    def lobbyFinal(self):
        return self.getChildByIndex(2)

    def configure(self):
        lobbyStart = State(stateID=BattlePassRewardStateID.LOBBY_START, flags=StateFlags.INITIAL)
        lobbyWait = State(stateID=BattlePassRewardStateID.LOBBY_WAIT)
        lobbyFinal = State(stateID=BattlePassRewardStateID.LOBBY_FINAL, flags=StateFlags.FINAL)
        lobbyStart.addTransition(ConditionTransition(isProgressionComplete, priority=1), target=lobbyFinal)
        lobbyStart.addTransition(ConditionTransition((lambda _: True), priority=0), target=lobbyWait)
        self.addChildState(lobbyStart)
        self.addChildState(lobbyWait)
        self.addChildState(lobbyFinal)
        return

    def _onEntered(self, event):
        lockNotificationManager(False, notificationManager=self.__notificationManager)
        self.__battlePass.onRewardSelectChange()
        return

    def _onExited(self):
        lockNotificationManager(True, notificationManager=self.__notificationManager)
        return


class ChoiceState(State):
    __slots__ = ()

    def __init__(self):
        super(ChoiceState, self).__init__(stateID=BattlePassRewardStateID.CHOICE, flags=StateFlags.SINGULAR)
        return

    @property
    def choiceItem(self):
        return self.getChildByIndex(0)

    def configure(self):
        choiceItem = ChoiceItemState()
        self.addChildState(choiceItem)
        return


class ChoiceItemState(State):
    __slots__ = ()

    def __init__(self):
        super(ChoiceItemState, self).__init__(stateID=BattlePassRewardStateID.CHOICE_ITEM, flags=StateFlags.INITIAL)
        return

    def _onEntered(self, event):
        machine = self.getMachine()
        if machine is not None:
            _, data, _, _ = machine.getRewardsData()
            if machine.hasRewardToChoose():

                def onCloseCallback():
                    for token, isTaken in viewitems(processRewardsToChoose(machine.getRewardsToChoose())):
                        machine.removeRewardToChoose(token, isTaken)

                    machine.post(StateEvent())
                    return

                showBattlePassRewardsSelectionWindow(chapterID=data.get(b'chapter', 0), level=data.get(b'level', 0), onRewardsReceivedCallback=machine.extendRewards, onCloseCallback=onCloseCallback)
            else:
                machine.post(StateEvent())
        return


class PreviewState(State):
    __slots__ = ()

    def __init__(self):
        super(PreviewState, self).__init__(stateID=BattlePassRewardStateID.CHOICE_PREVIEW)
        return

    def _onEntered(self, event):
        g_eventBus.addListener(LobbySimpleEvent.VEHICLE_PREVIEW_HIDDEN, self.__onHidePreview, EVENT_BUS_SCOPE.LOBBY)
        return

    def _onExited(self):
        g_eventBus.removeListener(LobbySimpleEvent.VEHICLE_PREVIEW_HIDDEN, self.__onHidePreview, EVENT_BUS_SCOPE.LOBBY)
        return

    def __onHidePreview(self, _):
        machine = self.getMachine()
        if machine:
            machine.post(StateEvent())
        return


class VideoState(State):
    __battlePass = dependency.descriptor(IBattlePassController)
    __slots__ = ()

    def __init__(self):
        super(VideoState, self).__init__(stateID=BattlePassRewardStateID.VIDEO)
        return

    def _onEntered(self, event):
        machine = self.getMachine()
        if machine is not None:
            chapter = machine.getChosenStyleChapter()
            if chapter is not None:
                _, level = getStyleInfoForChapter(chapter)
                mediaName = makeProgressionStyleMediaName(chapter, level)
                showBPFullscreenVideo(asBPVideoName(mediaName), mediaName, partial(machine.post, StateEvent()))
            else:
                _, data, _, _ = machine.getRewardsData()
                chapterID = data.get(b'chapter')
                if self.__battlePass.isExtraChapter(chapterID) or self.__battlePass.isHoliday():
                    mediaName = makeChapterMediaName(chapterID)
                    showBPFullscreenVideo(asBPVideoName(mediaName), mediaName, partial(machine.post, StateEvent()))
        return


class RewardState(State):
    __slots__ = ()

    def __init__(self):
        super(RewardState, self).__init__(stateID=BattlePassRewardStateID.REWARD, flags=StateFlags.SINGULAR)
        return

    @property
    def rewardStyle(self):
        return self.getChildByIndex(0)

    @property
    def rewardAny(self):
        return self.getChildByIndex(1)

    def configure(self):
        rewardStyle = RewardStyleState()
        rewardAny = RewardAnyState()
        rewardStyle.addTransition(ConditionTransition((lambda _: True), priority=0), target=rewardAny)
        self.addChildState(rewardStyle)
        self.addChildState(rewardAny)
        return


class RewardStyleState(State):
    __slots__ = ()
    __battlePass = dependency.descriptor(IBattlePassController)

    def __init__(self):
        super(RewardStyleState, self).__init__(stateID=BattlePassRewardStateID.REWARD_STYLE, flags=StateFlags.INITIAL)
        return

    def _onEntered(self, event):
        machine = self.getMachine()
        if machine is None:
            return
        else:
            chapterID = machine.getChosenStyleChapter()
            _, level = getStyleInfoForChapter(chapterID)
            style = getStyleForChapter(chapterID)
            additionalRewards, _, _, _ = machine.getRewardsData()
            needNotifyClosing = not additionalRewards
            if style is not None and style.getProgressionLevel() == style.getMaxProgressionLevel():
                machine.post(StateEvent())
                return
            prevLevel, _ = self.__battlePass.getChapterLevelInterval(chapterID)
            data = {b'reason': (BattlePassRewardReason.STYLE_UPGRADE), 
               b'chapter': chapterID, 
               b'prevLevel': prevLevel, 
               b'exitCallback': (partial(machine.post, StateEvent()))}
            styleToken = get3DStyleProgressToken(self.__battlePass.getSeasonID(), chapterID, level)
            rewards = packToken(styleToken)
            machine.clearChapterStyle()
            showBattlePassAwardsWindow([rewards], data, needNotifyClosing=needNotifyClosing)
            return


class RewardAnyState(State):
    __slots__ = (b'__needShowBuy',)
    __guiLoader = dependency.descriptor(IGuiLoader)
    __battlePass = dependency.descriptor(IBattlePassController)

    def __init__(self):
        self.__needShowBuy = False
        super(RewardAnyState, self).__init__(stateID=BattlePassRewardStateID.REWARD_ANY)
        return

    def _onEntered(self, event):
        machine = self.getMachine()
        if machine is None:
            return
        else:
            rewards, data, packageRewards, starterPack = machine.getRewardsData()
            if rewards is None and packageRewards is None:
                machine.clearSelf()
                machine.post(StateEvent())
                return
            if data is None:
                data = {b'reason': (BattlePassRewardReason.PURCHASE_BATTLE_PASS_LEVELS)}
            data[b'callback'] = partial(self.__onAwardClose, data.get(b'chapter'), data.get(b'newLevel'), data.get(b'reason'))
            data[b'exitCallback'] = partial(self.__onAwardExit, data.get(b'chapter'), data.get(b'newLevel'))
            data[b'showBuyCallback'] = partial(self.__onShowBuy, data.get(b'chapter'))
            chapter = machine.getChosenStyleChapter()
            if chapter is not None:
                _, level = getStyleInfoForChapter(chapter)
                styleToken = get3DStyleProgressToken(self.__battlePass.getSeasonID(), chapter, level)
                rewards.append(packToken(styleToken))
                machine.clearChapterStyle()
            if not rewards and not packageRewards:
                machine.clearSelf()
                machine.post(StateEvent())
                return
            showBattlePassAwardsWindow(rewards, data, packageRewards=packageRewards, starterPack=starterPack)
            return

    def _onExited(self):
        machine = self.getMachine()
        if machine is None:
            return
        else:
            machine.clearManualFlow()
            self.__needShowBuy = False
            return

    def __onAwardClose(self, chapterID, newLevel, reason):
        if self.__battlePass.isDisabled():
            return
        else:
            viewID = None
            if reason == BattlePassRewardReason.PURCHASE_BATTLE_PASS:
                if self.__battlePass.isHoliday() and self.__battlePass.isCompleted():
                    viewID = R.aliases.battle_pass.HolidayFinal()
                else:
                    viewID = R.aliases.battle_pass.Progression()
            elif self.__battlePass.isFinalLevel(chapterID, newLevel) and not self.__needShowBuy:
                if self.__battlePass.isHoliday():
                    viewID = R.aliases.battle_pass.HolidayFinal()
                else:
                    viewID = R.aliases.battle_pass.ChapterChoice()
            if viewID is not None:
                showBattlePass(viewID, chapterID)
            return

    def __onAwardExit(self, chapterID, newLevel):
        machine = self.getMachine()
        if machine is not None:
            machine.post(StateEvent())
            if self.__battlePass.isFinalLevel(chapterID, newLevel):
                machine.clearSelf()
        return

    def __onShowBuy(self, chapterID):
        self.__needShowBuy = True
        machine = self.getMachine()
        if machine is not None:
            machine.clearSelf()
            machine.post(StateEvent())
        showBattlePass(R.aliases.battle_pass.BuyPass(), chapterID)
        return
