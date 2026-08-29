import datetime
from debug_utils import LOG_CURRENT_EXCEPTION
CMD_BATTLE_ROYALE_TRN_JOIN = 20000
CMD_BATTLE_ROYALE_TRN_LEAVE = 20001
CMD_BATTLE_ROYALE_TRN_READY = 20002
CMD_BATTLE_ROYALE_TRN_NOT_READY = 20003
CMD_BATTLE_ROYALE_TRN_START_BATTLE = 20004
CMD_DEV_BATTLE_ROYALE_TRN_ADD_TOKEN = 20005
CMD_DEV_BATTLE_ROYALE_TRN_REM_TOKEN = 20006

class RESULT(object):
    OK = 0
    SOME_ERROR = -1
    ALWAYS_JOINED = 1
    NEVER_JOINED = 2
    INVALID_TOKEN = 3
    WRONG_ROLE = 4
    NO_PLACES = 5
    WRONG_PERIPHERY = 6
    DIFFERENT_ROSTER = 7
    WRONG_VEHICLE = 8
    ACCOUNT_LOCKED = 9


RESULT_NAMES = dict([(v, k) for k, v in RESULT.__dict__.iteritems() if isinstance(v, int)])

class ROLE(object):
    OBSERVER = 1
    PLAYER = 2
    PLAYER_COMMANDER = 3


class TYPE(object):
    SOLO = 1
    SQUAD = 2
    ANY = 3


MAX_PLAYERS_IN_SQUAD = 2

class BattleRoyaleTourmanentToken(object):

    def __init__(self, token):
        self.isValid = False
        self.whatWrong = None
        self.data = token
        try:
            tokenParts = token.split(b':')
            if tokenParts[0] != b'br_trn':
                return
            id = tokenParts[1].split(b'-')
            self.startTime = datetime.datetime.strptime(id[0] + id[1], b'%Y%m%d%H%M')
            self.tournamentID = int(id[2])
            self.peripheryID = int(tokenParts[2])
            if tokenParts[3] not in (b'solo', b'squad'):
                return
            tp = tokenParts[3]
            if tp == b'solo':
                self.type = TYPE.SOLO
            elif tp == b'squad':
                self.type = TYPE.SQUAD
            elif tp == b'any':
                self.type = TYPE.ANY
            else:
                self.whatWrong = (b'Wrong type {}').format(tp)
                return
            self.fullTournamentID = tokenParts[1] + tp
            role = tokenParts[4]
            self.teamID = int(tokenParts[5])
            if self.teamID != 0:
                if self.type == TYPE.SOLO and (self.teamID < 1 or self.teamID > 20) or self.type == TYPE.SQUAD and (self.teamID < 1 or self.teamID > 10):
                    self.whatWrong = (b'Wrong teamID {} for type {}').format(self.teamID, self.type)
                    return
            if role == b'observer':
                self.role = ROLE.OBSERVER
            elif role == b'player':
                self.role = ROLE.PLAYER
            elif role == b'playerc':
                self.role = ROLE.PLAYER_COMMANDER
            else:
                self.whatWrong = (b'Wrong role {}').format(role)
                return
            self.isValid = True
        except:
            self.whatWrong = b'Something wrong'
            LOG_CURRENT_EXCEPTION()

        return

    @property
    def isObserver(self):
        return self.isValid and self.role == ROLE.OBSERVER

    @property
    def isSolo(self):
        return self.isValid and self.type == TYPE.SOLO

    @property
    def isCommander(self):
        return self.isValid and self.role == ROLE.PLAYER_COMMANDER

    @property
    def participantShortDescr(self):
        if self.role == ROLE.OBSERVER:
            return b'O'
        return (b'P' if self.role == ROLE.PLAYER else b'C') + str(self.teamID)

    def __repr__(self):
        return (b'{} {}').format(self.data, self.isValid)


def participantsHash(dbIds):
    return str(sum(dbIds))
