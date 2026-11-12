import typing
from new_year.tamagotchi.dto.base import BaseDto

class Config(BaseDto):

    class Dto(BaseDto):
        __slots__ = (b'startTime', b'endTime', b'raidScalePoint', b'currentSeason', b'seasons', b'cumulative', b'states', b'indicators')

        def __init__(self):
            super(Config.Dto, self).__init__()
            self.startTime = 0.0
            self.endTime = 0.0
            self.raidScalePoint = 0
            self.currentSeason = None
            self.seasons = list()
            self.cumulative = None
            self.states = dict()
            self.indicators = dict()
            return

    class Season(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'id', b'startTime', b'endTime', b'rewardTime', b'topConfig', b'drawReward', b'cumulative', b'resetPoints', b'positionReward')

            def __init__(self):
                super(Config.Season.Dto, self).__init__()
                self.id = 0
                self.startTime = 0.0
                self.endTime = 0.0
                self.rewardTime = 0.0
                self.cumulative = False
                self.resetPoints = True
                self.positionReward = b''
                self.topConfig = list()
                self.drawReward = Config.Season.DrawReward.Dto()
                return

        class TopConfig(BaseDto):

            class Dto(BaseDto):
                __slots__ = (b'startPos', b'endPos', b'rewards')

                def __init__(self):
                    super(Config.Season.TopConfig.Dto, self).__init__()
                    self.startPos = 0
                    self.endPos = 0
                    self.rewards = dict()
                    return

        class DrawReward(BaseDto):

            class Dto(BaseDto):
                __slots__ = (b'count', b'rewards')

                def __init__(self):
                    super(Config.Season.DrawReward.Dto, self).__init__()
                    self.count = 0
                    self.rewards = dict()
                    return

    class Cumulative(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'startTime', b'endTime', b'rewardTime', b'topConfig', b'drawReward', b'positionReward')

            def __init__(self):
                super(Config.Cumulative.Dto, self).__init__()
                self.startTime = 0.0
                self.endTime = 0.0
                self.rewardTime = 0.0
                self.positionReward = b''
                self.topConfig = list()
                self.drawReward = Config.Season.DrawReward.Dto()
                return

    class States(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'min', b'max')

            def __init__(self):
                super(Config.States.Dto, self).__init__()
                self.min = 0
                self.max = 0
                return

    class Indicators(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'maxPoints', b'levels', b'item')

            def __init__(self):
                super(Config.Indicators.Dto, self).__init__()
                self.maxPoints = 0
                self.levels = list()
                self.item = Config.Items.Dto()
                return

        class Level(BaseDto):

            class Dto(BaseDto):
                __slots__ = (b'debPercent', b'degradation', b'loyalty', b'points', b'state')

                def __init__(self):
                    super(Config.Indicators.Level.Dto, self).__init__()
                    self.debPercent = 0.0
                    self.degradation = 0
                    self.loyalty = 0
                    self.points = 0
                    self.state = 0
                    return

    class Items(BaseDto):

        class Dto(BaseDto):
            __slots__ = (b'id', b'leaderboardPoint', b'dynCurrencyCode', b'currency', b'price', b'scalePoint')

            def __init__(self):
                super(Config.Items.Dto, self).__init__()
                self.id = 0
                self.leaderboardPoint = 0
                self.dynCurrencyCode = b''
                self.currency = b''
                self.price = 0
                self.scalePoint = 0
                return
