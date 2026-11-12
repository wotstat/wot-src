import typing
from new_year.tamagotchi.dto.base import BaseDto

class PlayerStats(BaseDto):

    class Dto(BaseDto):
        __slots__ = (b'leaderboardPoint', b'weekStats', b'cumulativeStats')

        def __init__(self):
            super(PlayerStats.Dto, self).__init__()
            self.leaderboardPoint = 0.0
            self.weekStats = list()
            self.cumulativeStats = list()
            return

    class WeekStat(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'week', b'position', b'point', b'isRewarded', b'rewardedDate', b'rewards')

            def __init__(self):
                super(PlayerStats.WeekStat.Dto, self).__init__()
                self.week = 0
                self.position = 0
                self.point = 0.0
                self.isRewarded = False
                self.rewardedDate = 0.0
                self.rewards = dict()
                return
