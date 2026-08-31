from helpers import dependency
from messenger import g_settings
from messenger.ext.player_helpers import isCurrentPlayer
from messenger.formatters import TimeFormatter
from messenger.m_constants import USER_GUI_TYPE
from messenger.storage import MessengerStorageDescriptor, UsersStorage
from skeletons.gui.battle_session import IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext

class _BattleMessageBuilder(object):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(_BattleMessageBuilder, self).__init__()
        self._ctx = {b'playerColor': b'', 
           b'playerName': b'', 
           b'messageColor': b'', 
           b'messageText': b''}
        return

    def setColors(self, avatarSessionID):
        getter = g_settings.getColorScheme
        self._ctx[b'playerColor'] = getter(b'battle/player').getHexStr(b'unknown')
        self._ctx[b'messageColor'] = getter(b'battle/message').getHexStr(b'unknown')
        return self

    def setName(self, avatarSessionID, pName=None, suffix=b'', vehID=None):
        name = self.sessionProvider.getCtx().getPlayerFullName(avatarSessionID=avatarSessionID, pName=pName, vID=vehID)
        name = name + suffix
        if isinstance(name, str):
            name = unicode(name, b'utf-8')
        self._ctx[b'playerName'] = name
        return self

    def setText(self, text):
        self._ctx[b'messageText'] = text
        return self

    def build(self):
        return g_settings.battle.messageFormat % self._ctx


class TeamMessageBuilder(_BattleMessageBuilder):

    def setColors(self, avatarSessionID):
        pColorScheme = g_settings.getColorScheme(b'battle/player')
        pColor = pColorScheme.getHexStr(b'teammate')
        ctx = self.sessionProvider.getCtx()
        if isCurrentPlayer(avatarSessionID):
            pColor = pColorScheme.getHexStr(b'himself')
        elif ctx.isTeamKiller(avatarSessionID=avatarSessionID):
            pColor = pColorScheme.getHexStr(b'teamkiller')
        elif ctx.isSquadMan(avatarSessionID=avatarSessionID):
            pColor = pColorScheme.getHexStr(b'squadman')
        elif ctx.isEnemy(avatarSessionID=avatarSessionID):
            pColor = pColorScheme.getHexStr(b'enemy')
        self._ctx[b'playerColor'] = pColor
        self._ctx[b'messageColor'] = g_settings.getColorScheme(b'battle/message').getHexStr(b'team')
        return self


class CommonMessageBuilder(_BattleMessageBuilder):

    def setColors(self, avatarSessionID):
        pColorScheme = g_settings.getColorScheme(b'battle/player')
        pColor = pColorScheme.getHexStr(b'unknown')
        if isCurrentPlayer(avatarSessionID):
            pColor = pColorScheme.getHexStr(b'himself')
        else:
            ctx = self.sessionProvider.getCtx()
            if ctx.isAlly(avatarSessionID=avatarSessionID):
                if ctx.isTeamKiller(avatarSessionID=avatarSessionID):
                    pColor = pColorScheme.getHexStr(b'teamkiller')
                elif ctx.isSquadMan(avatarSessionID=avatarSessionID):
                    pColor = pColorScheme.getHexStr(b'squadman')
                else:
                    pColor = pColorScheme.getHexStr(b'teammate')
            elif ctx.isEnemy(avatarSessionID=avatarSessionID):
                pColor = pColorScheme.getHexStr(b'enemy')
        self._ctx[b'playerColor'] = pColor
        self._ctx[b'messageColor'] = g_settings.getColorScheme(b'battle/message').getHexStr(b'common')
        return self


class SquadMessageBuilder(_BattleMessageBuilder):

    def setColors(self, avatarSessionID):
        pColorScheme = g_settings.getColorScheme(b'battle/player')
        pColor = pColorScheme.getHexStr(b'squadman')
        if isCurrentPlayer(avatarSessionID):
            pColor = pColorScheme.getHexStr(b'himself')
        elif self.sessionProvider.getCtx().isTeamKiller(avatarSessionID=avatarSessionID):
            pColor = pColorScheme.getHexStr(b'teamkiller')
        self._ctx[b'playerColor'] = pColor
        self._ctx[b'messageColor'] = g_settings.getColorScheme(b'battle/message').getHexStr(b'squad')
        return self


class LobbyMessageBuilder(object):
    lobbyContext = dependency.descriptor(ILobbyContext)
    usersStorage = MessengerStorageDescriptor(UsersStorage)

    def __init__(self):
        super(LobbyMessageBuilder, self).__init__()
        self.__templateKey = b''
        self.__guiType = USER_GUI_TYPE.OTHER
        self.__name = b''
        self.__time = 0.0
        self.__text = b''
        return

    def setTime(self, time_):
        self.__time = TimeFormatter.getMessageTimeFormat(time_)
        return self

    def getGroup(self):
        return self.__templateKey

    def setGroup(self, group):
        self.__templateKey = group
        return self

    def getGuiType(self):
        return self.__guiType

    def setGuiType(self, dbID):
        self.__guiType = self.__templateKey = self.usersStorage.getUserGuiType(dbID)
        return self

    def setName(self, dbID, nickName, clanAbbrev=None):
        self.__name = self.lobbyContext.getPlayerFullName(nickName, pDBID=dbID, clanAbbrev=clanAbbrev)
        return self

    def setText(self, text):
        self.__text = text
        return self

    def build(self):
        return g_settings.lobby.getMessageFormat(self.__templateKey).format(self.__name, self.__time, self.__text)
