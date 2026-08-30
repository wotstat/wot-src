class GameplayStateID(object):
    OFFLINE = b'game.offline'
    ONLINE = b'game.online'
    BATTLE_REPLAY = b'game.replay'
    ACCOUNT = b'online.account'
    AVATAR = b'online.avatar'
    WAITING_MAIN_LOOP = b'offline.waiting.main.loop'
    SYNCHRONIZATION = b'offline.synchronization'
    LOGIN = b'offline.login'
    ACCOUNT_ENTERING = b'account.entering'
    ACCOUNT_SHOW_GUI = b'account.show_gui'
    ACCOUNT_EXITING = b'account.exiting'
    AVATAR_ENTERING = b'avatar.entering'
    AVATAR_SHOW_GUI = b'avatar.show_gui'
    AVATAR_ARENA_INFO = b'avatar.arena.info'
    AVATAR_ARENA_LOADED = b'avatar.arena.loaded'
    AVATAR_EXITING = b'avatar.exiting'
    PREBATTLE_LOADING = b'avatar.arena.loaded.prebattle_loading'
    PREBATTLE_HIGHLIGHTS = b'avatar.arena.loaded.prebattle_highlights'
    PREBATTLE = b'avatar.arena.loaded.prebattle'
    BATTLE = b'avatar.arena.loaded.battle'
    SERVER_REPLAY_ENTERING = b'replay.server.entering'
    SERVER_REPLAY_EXITING = b'replay.server.exiting'
    BATTLE_REPLAY_LOADING = b'replay.loading'
    BATTLE_REPLAY_VERSION_DIFFERS = b'replay.version.differs'
    BATTLE_REPLAY_STARTING = b'replay.starting'
    BATTLE_REPLAY_PLAYING = b'replay.playing'
    BATTLE_REPLAY_REWIND = b'replay.rewind'
    BATTLE_REPLAY_FINISHED = b'replay.finished'
    BATTLE_REPLAY_NEXT = b'replay.next'


class OfflineEventID(object):
    MAIN_LOOP_INITIALIZED = b'game.offline.main.loop.initialized'
    SYNCHRONIZED = b'game.offline.synchronized'


class PlayerEventID(object):
    ACCOUNT_BECOME_PLAYER = b'player.account.entering'
    ACCOUNT_SHOW_GUI = b'player.account.show_gui'
    ACCOUNT_BECOME_NON_PLAYER = b'player.account.exiting'
    AVATAR_BECOME_PLAYER = b'player.avatar.entering'
    AVATAR_ARENA_INFO = b'player.avatar.arena.info'
    AVATAR_SHOW_GUI = b'player.avatar.show_gui'
    AVATAR_ARENA_LOADING = b'player.avatar.arena.loading'
    AVATAR_ARENA_LOADED = b'player.avatar.arena.loaded'
    AVATAR_BECOME_NON_PLAYER = b'player.avatar.exiting'
    PREBATTLE_HIGHLIGHTS_START = b'prebattle_highlights.start'
    PREBATTLE_START = b'prebattle.start'
    BATTLE_START = b'player.avatar.arena.loaded.battle'
    NON_PLAYER_BECOME_PLAYER = b'player.non_player'


class ReplayEventID(object):
    SERVER_REPLAY_ENTERING = b'replay.server.entering'
    SERVER_REPLAY_EXITING = b'replay.server.exiting'
    REPLAY_VERSION_CONFIRMATION = b'replay.version.confirmation'
    REPLAY_VERSION_CONFIRMED = b'replay.version.confirmed'
    REPLAY_REWIND = b'replay.rewind'
    REPLAY_FINISHED = b'replay.finished'
    REPLAY_NEXT = b'replay.next'


class IGameplayLogic(object):
    __slots__ = ()

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def postStateEvent(self, eventID, **kwargs):
        raise NotImplementedError
        return

    def addStateObserver(self, observer):
        raise NotImplementedError
        return

    def removeStateObserver(self, observer):
        raise NotImplementedError
        return

    def addOneshotObserver(self, gameplayStateIDs, observerLifetimeObj, enterFn=None, exitFn=None):
        raise NotImplementedError
        return

    def addStateEnterBlocker(self, stateID, event):
        raise NotImplementedError
        return

    def addStateExitBlocker(self, stateID, event):
        raise NotImplementedError
        return

    def goToLoginByRQ(self):
        raise NotImplementedError
        return

    def goToLoginByDisconnectRQ(self):
        raise NotImplementedError
        return

    def goToLoginByEvent(self):
        raise NotImplementedError
        return

    def goToLoginByKick(self, reason, kickReasonType, expiryTime):
        raise NotImplementedError
        return

    def goToLoginByError(self, reason):
        raise NotImplementedError
        return

    @staticmethod
    def quitFromGame():
        raise NotImplementedError
        return

    def tick(self):
        raise NotImplementedError
        return
