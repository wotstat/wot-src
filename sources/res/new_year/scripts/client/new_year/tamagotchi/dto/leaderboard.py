import typing
from new_year.tamagotchi.dto.base import BaseDto

class Leaderboard(BaseDto):

    class Dto(BaseDto):
        __slots__ = (b'updateTime', b'nextUpdateTime', b'isRecalcTime', b'cumulative', b'user', b'page')

        def __init__(self):
            super(Leaderboard.Dto, self).__init__()
            self.updateTime = 0.0
            self.nextUpdateTime = 0.0
            self.isRecalcTime = False
            self.cumulative = False
            self.user = Leaderboard.User.Dto()
            self.page = Leaderboard.Page.Dto()
            return

    class User(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'position', b'points', b'pointsByNextPlayer', b'pointsByNextTop', b'rewardsPlaces', b'rewards', b'upDown')

            def __init__(self):
                super(Leaderboard.User.Dto, self).__init__()
                self.position = 0
                self.points = 0
                self.pointsByNextPlayer = 0
                self.pointsByNextTop = 0
                self.rewardsPlaces = 0
                self.rewards = dict()
                self.upDown = 0
                return

    class Page(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'totalPage', b'currentPage', b'leaderboard')

            def __init__(self):
                super(Leaderboard.Page.Dto, self).__init__()
                self.totalPage = 0
                self.currentPage = 0
                self.leaderboard = list()
                return

        class Row(BaseDto):

            class Dto(BaseDto):
                __slots__ = (b'spaId', b'position', b'point', b'nickname', b'upDown')

                def __init__(self):
                    super(Leaderboard.Page.Row.Dto, self).__init__()
                    self.spaId = 0
                    self.position = 0
                    self.point = 0
                    self.nickname = b''
                    self.upDown = 0
                    return
