import BigWorld, constants
from debug_utils import LOG_ERROR
from helpers import dependency
from helpers import i18n
from gui import SystemMessages
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from messenger import MessengerEntry, g_settings
from messenger.storage import storage_getter
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.shared import IItemsCache

class DENUNCIATIONS(object):
    APPEAL = b'appeal'
    INCORRECT_BEHAVIOR = b'incorrectBehavior'
    NOT_FAIR_PLAY = b'notFairPlay'
    FORBIDDEN_NICK = b'forbiddenNick'
    BOT = b'bot'
    ORDER = (
     INCORRECT_BEHAVIOR, NOT_FAIR_PLAY, FORBIDDEN_NICK, BOT)
    ENEMY_ORDER = (
     INCORRECT_BEHAVIOR, NOT_FAIR_PLAY, FORBIDDEN_NICK, BOT)


DENUNCIATIONS_MAP = {(DENUNCIATIONS.INCORRECT_BEHAVIOR): (constants.DENUNCIATION.INCORRECT_BEHAVIOR), 
   (DENUNCIATIONS.NOT_FAIR_PLAY): (constants.DENUNCIATION.NOT_FAIR_PLAY), 
   (DENUNCIATIONS.FORBIDDEN_NICK): (constants.DENUNCIATION.FORBIDDEN_NICK), 
   (DENUNCIATIONS.BOT): (constants.DENUNCIATION.BOT)}

class Denunciator(object):

    @storage_getter(b'playerCtx')
    def playerCtx(self):
        return

    def makeAppeal(self, violatorID, userName, topic, arenaUniqueID, ctx=None):
        topicID = DENUNCIATIONS_MAP.get(topic)
        player = BigWorld.player()
        violatorKind = self._getViolatorKind(player, violatorID, ctx)
        denunciationsLeft = self.getDenunciationsLeft()
        try:
            player.makeDenunciation(violatorID, topicID, violatorKind, arenaUniqueID)
            if self._shouldSaveInLocalStorage():
                self.playerCtx.addDenunciationFor(violatorID, topicID, arenaUniqueID)
        except (AttributeError, TypeError):
            LOG_ERROR(b'Cannot make a denunciation')
            return

        message = self._formSystemMessage(userName, topicID, denunciationsLeft)
        self._makeNotification(message)
        return

    def isAppealsEnabled(self):
        return self.getDenunciationsLeft() > 0

    def isAppealsForTopicEnabled(self, violatorID, topicID, arenaUniqueID):
        return self.isAppealsEnabled() and not self.playerCtx.hasDenunciationFor(violatorID, topicID, arenaUniqueID)

    def getDenunciationsLeft(self):
        raise NotImplementedError()
        return

    def getDenunciationsPerDay(self):
        return constants.BATTLE_DENUNCIATIONS_PER_DAY

    def _shouldSaveInLocalStorage(self):
        return True

    def _getViolatorKind(self, player, violatorID, ctx=None):
        raise NotImplementedError()
        return

    def _formSystemMessage(self, userName, topicID, _):
        topicStr = i18n.makeString(MENU.denunciation(topicID))
        message = i18n.makeString(SYSTEM_MESSAGES.DENUNCIATION_SUCCESS)
        message = message % {b'name': userName, b'topic': topicStr}
        return message

    def _makeNotification(self, message):
        raise NotImplementedError()
        return


class LobbyDenunciator(Denunciator):
    itemsCache = dependency.descriptor(IItemsCache)

    def getDenunciationsLeft(self):
        return self.itemsCache.items.stats.battleDenunciationsLeft

    def _getViolatorKind(self, player, violatorID, ctx=None):
        if ctx is None:
            return constants.VIOLATOR_KIND.UNKNOWN
        else:
            if ctx.children.get(b'isAlly'):
                return constants.VIOLATOR_KIND.ALLY
            return constants.VIOLATOR_KIND.ENEMY

    def _makeNotification(self, message):
        SystemMessages.pushMessage(message, type=SystemMessages.SM_TYPE.Information)
        return


class BattleDenunciator(Denunciator):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def getDenunciationsLeft(self):
        return getattr(BigWorld.player(), b'denunciationsLeft', 0)

    @classmethod
    def getArenaUniqueID(cls):
        return BigWorld.player().arenaUniqueID

    def _getViolatorKind(self, player, violatorID, ctx=None):
        arenaDP = self.sessionProvider.getArenaDP()
        vehicleID = arenaDP.getVehIDBySessionID(str(violatorID))
        violator = arenaDP.getVehicleInfo(vehicleID)
        if player.team == violator.team:
            return constants.VIOLATOR_KIND.ALLY
        return constants.VIOLATOR_KIND.ENEMY

    def _makeNotification(self, message):
        MessengerEntry.g_instance.gui.addClientMessage(g_settings.htmlTemplates.format(b'battleErrorMessage', ctx={b'error': message}))
        return


class LobbyChatDenunciator(LobbyDenunciator):
    itemsCache = dependency.descriptor(IItemsCache)

    def getDenunciationsLeft(self):
        return self.itemsCache.items.stats.hangarDenunciationsLeft

    def getDenunciationsPerDay(self):
        return constants.HANGAR_DENUNCIATIONS_PER_DAY

    def isAppealsForTopicEnabled(self, violatorID, topicID, arenaUniqueID):
        if not self.isAppealsEnabled():
            return False
        hangarDenunciations = self.itemsCache.items.stats.hangarDenunciations
        violatorTopicIDs = hangarDenunciations.get(violatorID, set())
        return topicID not in violatorTopicIDs

    def _getViolatorKind(self, player, violatorID, ctx=None):
        return constants.VIOLATOR_KIND.HANGAR_CHAT_MEMBER

    def _shouldSaveInLocalStorage(self):
        return False

    def _formSystemMessage(self, userName, _, denunciationsLeft):
        message = i18n.makeString(SYSTEM_MESSAGES.DENUNCIATION_HANGARCHATSUCCESS_BODY)
        message = message % {b'name': userName, b'countLeft': (denunciationsLeft - 1), 
           b'countPerDay': (self.getDenunciationsPerDay())}
        return message

    def _makeNotification(self, message):
        header = i18n.makeString(SYSTEM_MESSAGES.DENUNCIATION_HANGARCHATSUCCESS_TITLE)
        SystemMessages.pushMessage(text=message, messageData={b'header': header}, type=SystemMessages.SM_TYPE.InformationHeader)
        return
