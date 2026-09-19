from __future__ import absolute_import
import ArenaType
from fort_rush_common.fort_rush_constants import EventStates
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.money import Currency
from messenger import g_settings
from messenger.formatters.service_channel import BattleResultsFormatter, ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData

class FortRushBattleResultsFormatter(BattleResultsFormatter):
    _battleResultKeys = {(-1): b'FortRushBattleDefeatResult', 
       0: b'FortRushBattleDrawResult', 
       1: b'FortRushBattleVictoryResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(FortRushBattleResultsFormatter, self)._prepareFormatData(message)
        battleResults = message.data
        accessor = R.strings.arenas.num(ArenaType.g_cache[battleResults.get(b'arenaTypeID', 0)].geometryName)
        ctx[b'mapName'] = backport.text(accessor.name())
        ctx[b'vehicles'] = ctx.get(b'vehicleNames', b'')
        ctx[Currency.CREDITS] = text_styles.credits(backport.getIntegralFormat(battleResults.get(Currency.CREDITS, 0)))
        progressionPoints = sum(data.get(b'count', 0) for data in battleResults.get(b'tokens', {}).values() if isinstance(data, dict))
        ctx[b'progressionPoints'] = backport.getIntegralFormat(progressionPoints) if progressionPoints else b''
        return (
         templateName, ctx)


class FortRushEventStatesFormatter(ServiceChannelFormatter):
    __TEMPLATES = {(EventStates.START): b'FortRushEventStateStart', 
       (EventStates.PAUSE): b'FortRushEventStatePause', 
       (EventStates.RESUME): b'FortRushEventStateResume', 
       (EventStates.ENDED): b'FortRushEventStateEnded'}

    def format(self, message, *args):
        template = self.__TEMPLATES.get(message.get(b'state'))
        formatted = g_settings.msgTemplates.format(template)
        return [MessageData(formatted, self._getGuiSettings(message, template))]
