from adisp import adisp_async, adisp_process
from gui.impl import backport
from gui.impl.gen import R
from helpers import time_utils, dependency
from messenger import g_settings
from messenger.formatters import TimeFormatter
from messenger.formatters.service_channel import BattleResultsFormatter, ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData
from story_mode_common.story_mode_constants import FIRST_MISSION_ID
from story_mode.skeletons.story_mode_controller import IStoryModeController

class StoryModeResultsFormatter(BattleResultsFormatter):
    _storyModeController = dependency.descriptor(IStoryModeController)
    _battleResultKeys = {(-1): b'storyModeBattleDefeatResult', 
       0: b'storyModeBattleDefeatResult', 
       1: b'storyModeBattleVictoryResult'}

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        if self._storyModeController.wasOnboardingSkipped:
            callback(MessageData(None, None))
        messages = yield super(StoryModeResultsFormatter, self).format(message)
        callback(messages)
        return

    def _prepareFormatData(self, message):
        templateName, ctx = super(StoryModeResultsFormatter, self)._prepareFormatData(message)
        missionId = message.data.get(b'missionId', FIRST_MISSION_ID)
        ctx[b'scenarioName'] = backport.text(R.strings.sm_battle.prebattle.mission.title.num(missionId)())
        return (templateName, ctx)


class StoryModeAwardFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'storyModeAwardMessage'

    def format(self, message, *args):
        medal = message.data[b'medal']
        formatted = g_settings.msgTemplates.format(self.__TEMPLATE, {b'at': (TimeFormatter.getLongDatetimeFormat(time_utils.makeLocalServerTime(message.sentTime))), 
           b'medal_name': (backport.text(R.strings.achievements.dyn(medal)()))})
        return [
         MessageData(formatted, self._getGuiSettings(message, self.__TEMPLATE))]
