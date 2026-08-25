from enum import Enum

class IngameTournamentType(Enum):
    WCI = b'wci'
    OLS = b'ols'


class IngameTournamentState(Enum):
    INTRO = b'tournament_intro'
    IN_PROGRESS = b'tournament_in_live'
    BETWEEN_SHOWMATCHES = b'tournament_between_showmatch_days'
    FINISHED = b'tournament_finished'


class IngameTournamentBracketType(Enum):
    RR = b'RR'
    DE = b'DE'


class IngameTournamentMatchState(Enum):
    UPCOMING = b'upcoming'
    IN_LIVE = b'in_live'
    COMPLETED = b'completed'


class IngameTournamentUrlType(Enum):
    YOUTUBE = b'youtube'
    TWITCH = b'twitch'
    DOUYIN = b'douyin'
    HUYA = b'huya'


class IngameTournamentLogoSize(Enum):
    SMALL = b'48x48'
    MEDIUM = b'86x86'
    LARGE = b'260x260'
    EXTRA_LARGE = b'522x522'
