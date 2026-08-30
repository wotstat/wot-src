from enum import Enum

class BanState(Enum):
    PREPICK = b'prepick'
    VOTING = b'voting'
    FINISHED = b'finished'
    NONE = b'none'


class CandidateState(Enum):
    NOSELECTED = b'noSelected'
    DONTBANSELECTED = b'dontBanSelected'
    SINGLECANDIDATE = b'singleCandidate'
    MULTIPLECANDIDATES = b'multipleCandidates'
