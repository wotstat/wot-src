from __future__ import absolute_import
import typing, BigWorld
from constants import IS_DEVELOPMENT
from debug_utils import LOG_DEBUG_DEV
from frameworks.wulf import WindowLayer, WindowStatus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.pub import WindowImpl
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.limited_ui.lui_rules_storage import LUI_RULES
from gui.shared.event_dispatcher import showAdvancedAchievementsRewardView
from helpers import dependency
from functools import partial
from advanced_achievements_client.getters import getAchievementsEarnedBeforeTime, getBonusTuples
from helpers.dependency import replace_none_kwargs
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from skeletons.gui.game_control import IAchievements20EarningController, IAchievementsController, ILimitedUIController
from skeletons.gui.impl import IGuiLoader
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from skeletons.gui.system_messages import ISystemMessages
if typing.TYPE_CHECKING:
    from typing import Optional, Generator, List, Tuple
    from advanced_achievements_client.items import _BaseGuiAchievement

class Achievements20EarningController(IAchievements20EarningController):
    __slots__ = (b'__commandQueueManager', b'__commandBuilder')
    __settingsCore = dependency.descriptor(ISettingsCore)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __advAchmntCtrl = dependency.descriptor(IAchievementsController)
    __guiLoader = dependency.descriptor(IGuiLoader)
    __RESTRICTED_LAYERS = {
     WindowLayer.FULLSCREEN_WINDOW,
     WindowLayer.OVERLAY,
     WindowLayer.TOP_WINDOW}
    __ACTIVE_WINDOW_STATUSES = (
     WindowStatus.LOADING, WindowStatus.LOADED)
    __HIGH_PRIORITY_WINDOWS = (
     VIEW_ALIAS.LOBBY_STORE, VIEW_ALIAS.BATTLE_QUEUE)
    __HIGH_PRIORITY_WULF_WINDOWS = ()

    def __init__(self):
        super(Achievements20EarningController, self).__init__()
        self.__commandQueueManager = CommandQueueManager()
        self.__commandBuilder = CommandBuilder()
        return

    def onLobbyInited(self, event):
        self.__addControllerListeners()
        self.__addFlowListeners()
        self.__diffToCommands()
        return

    def onAccountBecomeNonPlayer(self):
        self.__stop()
        return

    def onDisconnected(self):
        self.__stop()
        return

    def __stop(self):
        self.__removeFlowListeners()
        self.__clearQueue()
        return

    def __clearQueue(self):
        if self.__commandQueueManager is not None:
            self.__commandQueueManager.stop()
        return

    def __addFlowListeners(self):
        self.__advAchmntCtrl.onNewAchievementsEarned += self.__onAchievementsEarned
        return

    def __addControllerListeners(self):
        self.__guiLoader.windowsManager.onWindowStatusChanged += self.__onWindowStatusChanged
        return

    def __removeFlowListeners(self):
        self.__advAchmntCtrl.onNewAchievementsEarned -= self.__onAchievementsEarned
        return

    def __removeControllerListeners(self):
        if self.__guiLoader.windowsManager is not None:
            self.__guiLoader.windowsManager.onWindowStatusChanged -= self.__onWindowStatusChanged
        return

    def __onWindowStatusChanged(self, _, newStatus):
        if newStatus in (WindowStatus.LOADING, WindowStatus.LOADED, WindowStatus.DESTROYING):
            isEarningLockedByLayer = self.__isEarningLockedByLayer()
            isEarningLockedByView = self.__isEarningLockedByViews()
            if isEarningLockedByLayer or isEarningLockedByView:
                self.pause()
            else:
                self.resume()
        return

    def __isEarningLockedByLayer(self):
        windowsManager = self.__guiLoader.windowsManager
        windows = windowsManager.findWindows((lambda w: w.layer in self.__RESTRICTED_LAYERS and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES))
        return len(windows) > 0

    def __isEarningLockedByViews(self):
        windowsManager = self.__guiLoader.windowsManager
        scaleformView = len(windowsManager.findWindows((lambda w: isinstance(w, SFWindow) and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES and w.loadParams.viewKey.alias in self.__HIGH_PRIORITY_WINDOWS))) > 0
        gamefaceView = len(windowsManager.findWindows((lambda w: isinstance(w, WindowImpl) and w.windowStatus in self.__ACTIVE_WINDOW_STATUSES and w.content.layoutID in self.__HIGH_PRIORITY_WULF_WINDOWS))) > 0
        return scaleformView or gamefaceView

    @replace_none_kwargs(itemsCache=IItemsCache)
    def __getDossierDescr(self, userId=None, itemsCache=None):
        return itemsCache.items.getAccountDossier(userId).getDossierDescr()

    def __diffToCommands(self):
        self.__clearQueue()
        timestamp = self.__settingsCore.serverSettings.getAdvancedAchievementsEarningTimestamp()
        dossierDescr = self.__getDossierDescr()
        achievementsData = getAchievementsEarnedBeforeTime(dossierDescr, timestamp)
        if achievementsData:
            self.__advAchmntCtrl.initUnseenAdvancedAchievements(achievementsData)
            self.__achievementsEarned(achievementsData)
        return

    def __onAchievementsEarned(self, achievementsData):
        self.__achievementsEarned(achievementsData)
        return

    def __achievementsEarned(self, achievementsData):
        self.__commandQueueManager.pushChain(self.__commandBuilder.createEarnAchievementChain(self.__commandQueueManager, achievementsData))
        self.__commandQueueManager.executeNextCommand()
        return

    def fini(self):
        self.__stop()
        self.__removeControllerListeners()
        self.__commandBuilder = None
        self.__commandQueueManager = None
        return

    def pause(self):
        self.__commandQueueManager.pause()
        return

    def resume(self):
        self.__commandQueueManager.resume()
        return


class CommandQueueManager(object):
    __slots__ = (b'__commandQueue', b'__commandChains', b'__currentCommand', b'__isPaused')

    def __init__(self):
        super(CommandQueueManager, self).__init__()
        self.__commandQueue = []
        self.__commandChains = []
        self.__currentCommand = None
        self.__isPaused = False
        return

    def pushChain(self, command):
        self.__commandChains.append(command)
        return

    def executeNextCommand(self):
        if self.__isPaused:
            return
        else:
            if self.__currentCommand and self.__currentCommand.isReleased():
                self.__currentCommand.stop()
                self.__currentCommand = None
            if not self.__commandQueue and self.__commandChains:
                self.__commandQueue = self.__commandChains.pop(0)
            if self.__commandQueue:
                if not self.__currentCommand:
                    self.__currentCommand = self.__commandQueue.pop(0)
                    self.__currentCommand.execute()
            return

    def stop(self):
        if self.__currentCommand:
            self.__currentCommand.stop()
            self.__currentCommand = None
        for command in self.__commandQueue:
            command.stop()

        for transactions in self.__commandChains:
            for command in transactions:
                command.stop()

        self.__commandQueue = []
        self.__commandChains = []
        return

    def pause(self):
        if not self.__isPaused:
            self.__isPaused = True
        return

    def resume(self):
        if self.__isPaused:
            self.__isPaused = False
            self.executeNextCommand()
        return


class CommandBuilder(object):
    __settingsCore = dependency.descriptor(ISettingsCore)
    __advAchmntCtrl = dependency.descriptor(IAchievementsController)
    __limitedUICtrl = dependency.descriptor(ILimitedUIController)

    def _isTrophy(self, achievementsData):
        return not any(not self.__advAchmntCtrl.getAchievementByID(idx, category).isDeprecated for idx, category, _, _ in achievementsData)

    def _isMultiple(self, achievementsData):
        return len(achievementsData) > 1

    def _getMultipleText(self, isMultiple):
        if isMultiple:
            return b'multiple'
        return b'single'

    def _getTrophyText(self, isTrophy):
        if isTrophy:
            return b'trophy'
        return b'common'

    def _getNewAchievementIterator(self, achievementsData):
        for id, category, stage, _ in achievementsData:
            yield self.__advAchmntCtrl.getAchievementByID(id, category).getFakeAchievementForStage(stage)

        return

    def _createAchievementDataDebugCommand(self, receiver, achievementData):
        message = b''
        for id, category, stage, _ in achievementData:
            message += (b' \n ------  Achievement: {} Category: {} Stage: {}').format(id, category, stage)

        args = {b'receiver': receiver, 
           b'message': message}
        return PrintCommand(args)

    def _createDebugMessageCommand(self, receiver, message):
        args = {b'receiver': receiver, 
           b'message': message}
        return PrintCommand(args)

    def _createTimeStampUpdateCommand(self, receiver, achievementsData):
        maxTimestamp = max(timestamp for _, _, _, timestamp in achievementsData)
        args = {b'receiver': receiver, 
           b'timestamp': maxTimestamp}
        return TimeStampUpdateCommand(args)

    def _createNotificationCommand(self, receiver, achievementsData):
        isMultiple = self._isMultiple(achievementsData)
        isTrophy = self._isTrophy(achievementsData)
        targetData = None
        if isMultiple:
            value = len(achievementsData)
        else:
            id, category, _, _ = achievementsData[0]
            key = self.__advAchmntCtrl.getAchievementByID(id, category).getStringKey()
            value = backport.text(R.strings.advanced_achievements.name.dyn(key)())
            targetData = (id, category)
        trophyText = self._getTrophyText(isTrophy)
        multipleText = self._getMultipleText(isMultiple)
        args = {b'receiver': receiver, 
           b'header': (backport.text(R.strings.system_messages.earning.title())), 
           b'body': (backport.text(R.strings.system_messages.earning.dyn(trophyText).dyn(multipleText)(), value=value)), 
           b'isTrophy': isTrophy, 
           b'isMultiple': isMultiple, 
           b'targetData': targetData}
        return NotificationCommand(args)

    def _createEarningAnimationCommand(self, receiver, achievementsData):
        isMultiple = self._isMultiple(achievementsData)
        isTrophy = self._isTrophy(achievementsData)
        args = {b'receiver': receiver, 
           b'data': (self._getNewAchievementIterator(achievementsData)), 
           b'isTrophy': isTrophy, 
           b'isMultiple': isMultiple}
        return EarningAnimationCommand(args)

    def _createRewardScreenCommand(self, receiver, achievementsData):
        bonusTuples = getBonusTuples(self._getNewAchievementIterator(achievementsData))
        if bonusTuples:
            args = {b'receiver': receiver, b'bonusTuples': bonusTuples}
            return RewardScreenCommand(args)
        else:
            return

    def createEarnAchievementChain(self, receiver, achievementsData):
        root = []
        if IS_DEVELOPMENT:
            root.append(self._createDebugMessageCommand(receiver, b'--- Achievements earned ---'))
            root.append(self._createAchievementDataDebugCommand(receiver, achievementsData))
        if self.__limitedUICtrl.isRuleCompleted(LUI_RULES.AdvancedAchievements):
            root.append(self._createEarningAnimationCommand(receiver, achievementsData))
        root.append(self._createTimeStampUpdateCommand(receiver, achievementsData))
        root.append(self._createNotificationCommand(receiver, achievementsData))
        if self.__limitedUICtrl.isRuleCompleted(LUI_RULES.AdvancedAchievements):
            rewardScreenCommand = self._createRewardScreenCommand(receiver, achievementsData)
            if rewardScreenCommand:
                root.append(rewardScreenCommand)
        return root


class Command(object):
    __slots__ = (b'__receiver', b'__isReleased')

    def __init__(self, args):
        self.__receiver = args[b'receiver']
        self.__isReleased = False
        return

    def execute(self):
        return

    def release(self, *args, **kwargs):
        self.__isReleased = True
        if self.__receiver:
            self.__receiver.executeNextCommand()
        return

    def isReleased(self):
        return self.__isReleased

    def stop(self):
        self.__receiver = None
        return


class TimeStampUpdateCommand(Command):
    __slots__ = (b'__timestamp',)
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, args):
        super(TimeStampUpdateCommand, self).__init__(args)
        self.__timestamp = args[b'timestamp']
        return

    def execute(self):
        self.__settingsCore.serverSettings.setAdvancedAchievementsEarningTimestamp(self.__timestamp)
        super(TimeStampUpdateCommand, self).execute()
        self.release()
        return


class PrintCommand(Command):
    __slots__ = (b'__message',)

    def __init__(self, args):
        super(PrintCommand, self).__init__(args)
        self.__message = args[b'message']
        return

    def execute(self):
        LOG_DEBUG_DEV(self.__message)
        super(PrintCommand, self).execute()
        self.release()
        return


class NotificationCommand(Command):
    __systemMessages = dependency.descriptor(ISystemMessages)
    __slots__ = (b'__header', b'__body', b'__isTrophy', b'__isMultiple', b'__targetData')

    def __init__(self, args):
        super(NotificationCommand, self).__init__(args)
        self.__header = args[b'header']
        self.__body = args[b'body']
        self.__isMultiple = args[b'isMultiple']
        self.__targetData = args[b'targetData']
        self.__isTrophy = args[b'isTrophy']
        return

    def execute(self):
        self.__systemMessages.proto.serviceChannel.pushClientMessage({b'header': (self.__header), 
           b'body': (self.__body), 
           b'isTrophy': (self.__isTrophy), 
           b'isMultiple': (self.__isMultiple), 
           b'targetData': (self.__targetData)}, SCH_CLIENT_MSG_TYPE.ACHIEVEMENTS20_EARNING_SM_TYPE)
        super(NotificationCommand, self).execute()
        self.release()
        return


class EarningAnimationCommand(Command):
    __slots__ = (b'__isTrophy', b'__isMultiple', b'__data')

    def __init__(self, args):
        super(EarningAnimationCommand, self).__init__(args)
        self.__isTrophy = args[b'isTrophy']
        self.__isMultiple = args[b'isMultiple']
        self.__data = args[b'data']
        return

    def execute(self):
        g_eventBus.addListener(events.Achievements20Event.ACHIEVEMENT_EARNED_SHOWNED, self.release, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.handleEvent(events.Achievements20Event(events.Achievements20Event.ACHIEVEMENT_EARNED, ctx={b'isTrophy': (self.__isTrophy), 
           b'isMultiple': (self.__isMultiple), 
           b'data': (self.__data)}), scope=EVENT_BUS_SCOPE.LOBBY)
        super(EarningAnimationCommand, self).execute()
        return

    def stop(self):
        g_eventBus.removeListener(events.Achievements20Event.ACHIEVEMENT_EARNED_SHOWNED, self.release, EVENT_BUS_SCOPE.LOBBY)
        super(EarningAnimationCommand, self).stop()
        return


class RewardScreenCommand(Command):
    __slots__ = (b'__bonusTuples',)

    def __init__(self, args):
        super(RewardScreenCommand, self).__init__(args)
        self.__bonusTuples = args[b'bonusTuples']
        return

    def execute(self):
        BigWorld.callback(0, partial(showAdvancedAchievementsRewardView, self.__bonusTuples))
        super(RewardScreenCommand, self).execute()
        self.release()
        return
