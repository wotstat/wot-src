from __future__ import absolute_import
from builtins import round
from helpers.time_utils import ONE_MINUTE
from messenger.formatters.service_channel import BattleResultsFormatter

def formatTimeWithMs(allSeconds, prec=100):
    minutes, seconds = divmod(round(prec * allSeconds), prec * ONE_MINUTE)
    seconds, ms = divmod(seconds, prec)
    return b'%02d:%02d.%02d' % (minutes, seconds, ms)


class FallTanksBattleResultsSubFormatter(BattleResultsFormatter):
    _battleResultKeys = {0: b'fallTanksBattleNotFinishedResult', 
       1: b'fallTanksBattleFinishedResult'}

    def _getBattleResultsKey(self, battleResults):
        return int(battleResults.get(b'fallTanksFinishTime', 0) > 0)

    def _prepareFormatData(self, message):
        templateName, ctx = super(FallTanksBattleResultsSubFormatter, self)._prepareFormatData(message)
        battleResults = message.data
        ctx[b'finishTime'] = formatTimeWithMs(battleResults.get(b'fallTanksFinishTime', 0))
        ctx[b'playerPlace'] = battleResults.get(b'fallTanksPosition', 0)
        return (templateName, ctx)
