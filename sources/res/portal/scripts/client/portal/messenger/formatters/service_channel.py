from gui.impl import backport
from gui.impl.gen import R
from messenger import g_settings
from messenger.formatters.service_channel import BattleResultsFormatter, ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData

class ExtendedBattleResultsFormatter(BattleResultsFormatter):
    _battleResultKeys = {(-1): b'portalBattleDefeatResult', 
       0: b'portalBattleDrawGameResult', 
       1: b'portalBattleVictoryResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(ExtendedBattleResultsFormatter, self)._prepareFormatData(message)
        ctx[b'progressionTokens'] = self.__formatProgressionPoints(message)
        ctx[b'vehicleUpgradePoints'] = self.__formatVehicleUpgradePoints(message)
        ctx[b'difficulty'] = self.__getDifficultyDescr(message)
        return (templateName, ctx)

    @staticmethod
    def __formatProgressionPoints(message):
        progressionTokens = message.data.get(b'progressionTokens', 0)
        return g_settings.htmlTemplates.format(b'portalBattleResultProgressionPoints', ctx={b'progressionTokens': progressionTokens})

    @staticmethod
    def __formatVehicleUpgradePoints(message):
        vehicleUpgradePoints = message.data.get(b'vehicleUpgradePoints', 0)
        return g_settings.htmlTemplates.format(b'portalBattleResultVehicleUpgradePoints', ctx={b'vehicleUpgradePoints': vehicleUpgradePoints})

    def __getDifficultyDescr(self, message):
        level = message.data.get(b'portalBattleLevel', 1)
        return backport.text(R.strings.portal_lobby.complexity.level.dyn((b'c_{}').format(level))())


class PortalSystemMessageFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'PortalSystemMessage'

    def format(self, message, *args):
        formatted = g_settings.msgTemplates.format(self.__TEMPLATE)
        return [MessageData(formatted, self._getGuiSettings(message, self.__TEMPLATE))]
