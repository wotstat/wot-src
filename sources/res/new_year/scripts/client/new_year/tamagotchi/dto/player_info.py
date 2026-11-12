import typing
from collections import deque
from new_year.tamagotchi.dto.base import BaseDto

class PlayerInfo(BaseDto):

    class Dto(BaseDto):
        __slots__ = (b'leaderboardPoint', b'cumulativePoint', b'lastUpdateTime', b'state', b'indicators', b'debHistory')

        def __init__(self):
            super(PlayerInfo.Dto, self).__init__()
            self.leaderboardPoint = 0.0
            self.cumulativePoint = 0.0
            self.lastUpdateTime = 0.0
            self.state = b''
            self.indicators = dict()
            self.debHistory = deque()
            return

    class DebHistory(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'value', b'expirationTime')

            def __init__(self):
                super(PlayerInfo.DebHistory.Dto, self).__init__()
                self.value = 0
                self.expirationTime = 0.0
                return
