from __future__ import absolute_import
from future.utils import viewitems, viewvalues
from constants import AUTO_MAINTENANCE_RESULT, AUTO_MAINTENANCE_TYPE
from last_stand_common.last_stand_constants import ArtefactsSettings, ProgressPointsSettings
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from messenger import g_settings
from messenger.formatters.service_channel import ServiceChannelFormatter, BattleResultsFormatter, _getRaresAchievementsStrings, AutoMaintenanceFormatter
from messenger.formatters.service_channel_helpers import MessageData
from dossiers2.custom.records import DB_ID_TO_RECORD
from dossiers2.ui.layouts import IGNORED_BY_BATTLE_RESULTS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK, BADGES_BLOCK
from gui.shared.gui_items.dossier.factories import getAchievementFactory
from gui.shared.money import Currency
from gui.shared.formatters import getBWFormatter

class LSProgressPointsFormatter(ServiceChannelFormatter):
    _MSG_KEY = b'lsProgressPointsMessage'

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
            title = backport.text(R.strings.last_stand_system_messages.serviceChannelMessages.progressPoints.add.title())
            description = backport.text(R.strings.last_stand_system_messages.serviceChannelMessages.progressPoints.add.description(), key=text_styles.stats(delta))
        else:
            title = backport.text(R.strings.last_stand_system_messages.serviceChannelMessages.progressPoints.draw.title())
            description = backport.text(R.strings.last_stand_system_messages.serviceChannelMessages.progressPoints.draw.description(), key=text_styles.stats(delta))
        ctx = {b'title': title, b'description': description}
        return g_settings.msgTemplates.format(self._MSG_KEY, ctx=ctx)


class LSBattleResultsFormatter(BattleResultsFormatter):
    R_SERVICE_CHANNEL_MESSAGES = R.strings.last_stand_system_messages.serviceChannelMessages
    _battleResultKeys = {(-1): b'LSBattleDefeatResult', 
       0: b'LSBattleDefeatResult', 
       1: b'LSBattleVictoryResult'}

    def _prepareFormatData(self, message):
        _, ctx = super(LSBattleResultsFormatter, self)._prepareFormatData(message)
        battleResults = message.data
        templateName = self._getTemplateName(battleResults)
        lsPhase = battleResults.get(b'phase', 0)
        lsPhasesCount = battleResults.get(b'phasesCount', 0)
        isWinner = battleResults.get(b'isWinner') == 1
        bonusType = battleResults.get(b'bonusType')
        ctx[b'difficultyLevel'] = self._getDifficultyLevel(bonusType)
        ctx[b'finalResult'] = self.__makeBattleResultString(lsPhase, lsPhasesCount, isWinner, bonusType)
        accCredits = battleResults.get(Currency.CREDITS, 0) - battleResults.get(b'creditsToDraw', 0)
        ctx[Currency.CREDITS] = b'<br/>' + backport.text(R.strings.messenger.serviceChannelMessages.battleResults.credits(), text_styles.credits(getBWFormatter(Currency.CREDITS)(accCredits)))
        dailyQuestProgressPoints = battleResults.get(b'tokens', {}).get(ProgressPointsSettings.TOKEN, {}).get(b'count', 0)
        ctx[b'progressPoints'] = dailyQuestProgressPoints + battleResults.get(b'progressPoints', 0)
        artefacts = sum(data.get(b'count', 0) for token, data in viewitems(battleResults.get(b'tokens', {})) if ArtefactsSettings.QUEST_PREFIX in token and token != ProgressPointsSettings.TOKEN)
        ctx[b'artefacts'] = self.__makeArtefactString(artefacts)
        ctx[b'achieves'], ctx[b'badges'] = self.__makeAchievementsAndBadgesStrings(battleResults)
        return (
         templateName, ctx)

    @staticmethod
    def _getBattleTypeDescr(data):
        bonusType = data.get(b'bonusType')
        description = backport.text(R.strings.last_stand_system_messages.serviceChannelMessages.battleResults.battleTypeName.num(bonusType)())
        return description

    @staticmethod
    def _getDifficultyLevel(bonusType):
        return backport.text(R.strings.last_stand_system_messages.serviceChannelMessages.battleResults.difficulty.num(bonusType)())

    def _getTemplateName(self, data):
        battleResKey = data.get(b'isWinner', 0)
        return self._battleResultKeys[battleResKey]

    def __makeBattleResultString(self, lsPhase, lsPhasesCount, isWinner, bonusType):
        lsPhase = lsPhasesCount if isWinner else max(0, lsPhase - 1)
        return g_settings.htmlTemplates.format(b'LSBattleResultWaves', ctx={b'curPhase': (text_styles.credits(lsPhase)), b'maxPhases': (text_styles.credits(lsPhasesCount))})

    def __makeArtefactString(self, artefacts):
        if not artefacts:
            return b''
        if artefacts > 1:
            return g_settings.htmlTemplates.format(b'LSBattleResultQuests', ctx={b'artefacts': artefacts})
        return g_settings.htmlTemplates.format(b'LSBattleResultQuest', ctx={b'artefacts': artefacts})

    def __makeAchievementsAndBadgesStrings(self, battleResults):
        popUpRecords = []
        badges = []
        for vehBattleResults in viewvalues(battleResults.get(b'playerVehicles', {})):
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
        for records in viewvalues(dossierResults):
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


class LSAutoMaintenanceFormatter(AutoMaintenanceFormatter):
    _overriddenMessages = {(AUTO_MAINTENANCE_RESULT.NOT_ENOUGH_ASSETS): {(AUTO_MAINTENANCE_TYPE.EQUIP): (R.strings.last_stand_system_messages.serviceChannelMessages.autoEquipError())}, 
       (AUTO_MAINTENANCE_RESULT.OK): {(AUTO_MAINTENANCE_TYPE.EQUIP): (R.strings.last_stand_system_messages.serviceChannelMessages.autoEquipSuccess())}, 
       (AUTO_MAINTENANCE_RESULT.DISABLED_OPTION): {(AUTO_MAINTENANCE_TYPE.EQUIP): (R.strings.last_stand_system_messages.serviceChannelMessages.autoEquipDisabledOption())}}
