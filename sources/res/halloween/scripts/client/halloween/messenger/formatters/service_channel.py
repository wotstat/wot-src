from __future__ import absolute_import
from constants import AUTO_MAINTENANCE_RESULT, AUTO_MAINTENANCE_TYPE
from gui.shared.notifications import NotificationPriorityLevel
from halloween_common.halloween_constants import ArtefactsSettings
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from messenger import g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter, BattleResultsFormatter, _getRaresAchievementsStrings, AutoMaintenanceFormatter, InvoiceReceivedFormatter
from messenger.formatters.service_channel_helpers import MessageData
from gui.shared.gui_items.Vehicle import getUserName
from items import vehicles as vehicles_core
from dossiers2.custom.records import DB_ID_TO_RECORD
from dossiers2.ui.layouts import IGNORED_BY_BATTLE_RESULTS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK, BADGES_BLOCK
from gui.shared.gui_items.dossier.factories import getAchievementFactory
from gui.shared.money import Currency
from gui.shared.formatters import getBWFormatter

class HWVehicleRentFormatter(ServiceChannelFormatter):
    _MSG_KEY = b'HWVehicleRentMessage'

    def format(self, message, *args):
        data = message.data
        intCD = data.get(b'intCD')
        if intCD is not None:
            return [
             MessageData(self._getMessage(intCD), self._getGuiSettings(message, self._MSG_KEY))]
        else:
            return []

    def _getMessage(self, intCD):
        vehicleName = getUserName(vehicles_core.getVehicleType(intCD))
        ctx = {b'description': (backport.text(R.strings.halloween_system_messages.serviceChannelMessages.halloweenHangar.vehicleAcquired(), vehicle=vehicleName))}
        return g_settings.msgTemplates.format(self._MSG_KEY, ctx=ctx)


class HWArtefactKeysFormatter(ServiceChannelFormatter):
    _MSG_KEY = b'hwArtefactKeysMessage'

    def format(self, message, *args):
        data = message.data
        delta = data.get(b'delta')
        isAdded = data.get(b'isAdded', False)
        priority = NotificationPriorityLevel.MEDIUM if isAdded else None
        if delta is not None:
            return [
             MessageData(self._getMessage(isAdded, delta), self._getGuiSettings(message, self._MSG_KEY, priority))]
        else:
            return []

    def _getMessage(self, isAdded, delta):
        if isAdded:
            title = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.add.title())
            description = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.add.description(), key=text_styles.stats(delta))
        else:
            title = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.draw.title())
            description = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.draw.description(), key=text_styles.stats(delta))
        ctx = {b'title': title, b'description': description}
        return g_settings.msgTemplates.format(self._MSG_KEY, ctx=ctx)


class HWDifficultyLevelFormatter(ServiceChannelFormatter):
    _MSG_KEY = b'hwDifficultyRewardCongrats'

    def format(self, message, *args):
        data = message.data
        delta = data.get(b'delta')
        isAdded = data.get(b'isAdded', False)
        if delta is not None:
            return [
             MessageData(self._getMessage(isAdded, delta), self._getGuiSettings(message, self._MSG_KEY))]
        else:
            return []

    def _getMessage(self, isAdded, delta):
        if isAdded:
            title = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.add.title())
            description = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.add.description(), key=text_styles.credits(delta))
        else:
            title = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.draw.title())
            description = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.artefactKeys.draw.description(), key=text_styles.credits(delta))
        ctx = {b'title': title, b'description': description}
        return g_settings.msgTemplates.format(self._MSG_KEY, ctx=ctx)


class HalloweenBattleResultsFormatter(BattleResultsFormatter):
    R_SERVICE_CHANNEL_MESSAGES = R.strings.halloween_system_messages.serviceChannelMessages
    _battleResultKeys = {(-1): b'HWbattleDefeatResult', 
       0: b'HWbattleDefeatResult', 
       1: b'HWBattleVictoryResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(HalloweenBattleResultsFormatter, self)._prepareFormatData(message)
        battleResults = message.data
        halloweenPhase = battleResults.get(b'halloween_phase', 0)
        halloweenPhasesCount = battleResults.get(b'halloween_phases_count', 0)
        isWinner = battleResults.get(b'isWinner') == 1
        bonusType = battleResults.get(b'bonusType')
        ctx[b'difficultyLevel'] = self._getDifficultyLevel(bonusType)
        ctx[b'finalResult'] = self.__makeBattleResultString(halloweenPhase, halloweenPhasesCount, isWinner)
        accCredits = battleResults.get(Currency.CREDITS, 0) - battleResults.get(b'creditsToDraw', 0)
        ctx[Currency.CREDITS] = b'<br/>' + backport.text(R.strings.messenger.serviceChannelMessages.battleResults.credits(), text_styles.credits(getBWFormatter(Currency.CREDITS)(accCredits)))
        dailyQuestArtefactKeys = battleResults.get(b'tokens', {}).get(ArtefactsSettings.KEY_TOKEN, {}).get(b'count', 0)
        ctx[b'artefactKeys'] = dailyQuestArtefactKeys + battleResults.get(b'artefactKeys', 0)
        artefacts = sum(data.get(b'count', 0) for token, data in battleResults.get(b'tokens', {}).items() if ArtefactsSettings.QUEST_PREFIX in token and token != ArtefactsSettings.KEY_TOKEN)
        ctx[b'artefacts'] = self.__makeArtefactString(artefacts)
        ctx[b'achieves'], ctx[b'badges'] = self.__makeAchievementsAndBadgesStrings(battleResults)
        return (
         templateName, ctx)

    @staticmethod
    def _getBattleTypeDescr(data):
        bonusType = data.get(b'bonusType')
        description = backport.text(R.strings.halloween_system_messages.serviceChannelMessages.battleResults.battleTypeName.num(bonusType)())
        return description

    @staticmethod
    def _getDifficultyLevel(bonusType):
        return backport.text(R.strings.halloween_system_messages.serviceChannelMessages.battleResults.difficulty.num(bonusType)())

    def __makeBattleResultString(self, halloweenPhase, halloweenPhasesCount, isWinner):
        if isWinner:
            return g_settings.htmlTemplates.format(b'battleResultBossDefeated')
        return g_settings.htmlTemplates.format(b'battleResultPhases', ctx={b'curPhase': (text_styles.credits(max(0, halloweenPhase - 1))), b'maxPhases': (text_styles.credits(halloweenPhasesCount))})

    def __makeArtefactString(self, artefacts):
        if not artefacts:
            return b''
        if artefacts > 1:
            return g_settings.htmlTemplates.format(b'battleResultQuests', ctx={b'artefacts': artefacts})
        return g_settings.htmlTemplates.format(b'battleResultQuest', ctx={b'artefacts': artefacts})

    def __makeAchievementsAndBadgesStrings(self, battleResults):
        popUpRecords = []
        badges = []
        for _, vehBattleResults in battleResults.get(b'playerVehicles', {}).items():
            for recordIdx, value in vehBattleResults.get(b'popUpRecords', []):
                recordName = DB_ID_TO_RECORD[recordIdx]
                if recordName in IGNORED_BY_BATTLE_RESULTS:
                    continue
                block, name = recordName
                if block == BADGES_BLOCK:
                    badges.append(name)
                else:
                    achieve = getAchievementFactory(recordName).create(value=value)
                    if achieve is not None and achieve not in popUpRecords:
                        popUpRecords.append(achieve)

            if b'markOfMastery' in vehBattleResults and vehBattleResults[b'markOfMastery'] > 0:
                popUpRecords.append(getAchievementFactory((ACHIEVEMENT_BLOCK.TOTAL, b'markOfMastery')).create(value=vehBattleResults[b'markOfMastery']))

        dossierResults = battleResults.get(b'dossier', {})
        for records in dossierResults.values():
            for recordName in records:
                block, id_ = recordName
                if block == BADGES_BLOCK:
                    badges.append(id_)

        achievementsStrings = [a.getUserName() for a in sorted(popUpRecords)]
        raresStrings = _getRaresAchievementsStrings(battleResults)
        if raresStrings:
            achievementsStrings.extend(raresStrings)
        achievementsBlock = b''
        if achievementsStrings:
            achievementsBlock = g_settings.htmlTemplates.format(b'battleResultAchieves', {b'achieves': ((b', ').join(achievementsStrings))})
        badgesBlock = b''
        if badges:
            badgesStr = (b', ').join([backport.text(R.strings.badge.dyn((b'badge_{}').format(badgeID))()) for badgeID in badges])
            badgesBlock = b'<br/>' + g_settings.htmlTemplates.format(b'badgeAchievement', {b'badges': badgesStr})
        return (achievementsBlock, badgesBlock)


class HWAutoMaintenanceFormatter(AutoMaintenanceFormatter):
    _overriddenMessages = {(AUTO_MAINTENANCE_RESULT.NOT_ENOUGH_ASSETS): {(AUTO_MAINTENANCE_TYPE.EQUIP): (R.strings.halloween_system_messages.serviceChannelMessages.autoEquipError())}, 
       (AUTO_MAINTENANCE_RESULT.OK): {(AUTO_MAINTENANCE_TYPE.EQUIP): (R.strings.halloween_system_messages.serviceChannelMessages.autoEquipSuccess())}, 
       (AUTO_MAINTENANCE_RESULT.DISABLED_OPTION): {(AUTO_MAINTENANCE_TYPE.EQUIP): (R.strings.halloween_system_messages.serviceChannelMessages.autoEquipDisabledOption())}}


class HWInvoiceReceivedLowPriorityFormatter(InvoiceReceivedFormatter):

    def _getGuiSettings(self, data, key=None, priorityLevel=None, messageType=None, messageSubtype=None, decorator=None):
        if priorityLevel is None:
            priorityLevel = NotificationPriorityLevel.LOW
        return super(HWInvoiceReceivedLowPriorityFormatter, self)._getGuiSettings(data, key, priorityLevel, messageType, messageSubtype, decorator)
