class CONDITION_ICON:
    ASSIST = b'assist'
    ASSIST_RADIO = b'assist_radio'
    ASSIST_TRACK = b'assist_track'
    ASSIST_STUN = b'assist_stun'
    ASSIST_STUN_DURATION = b'assist_stun_time'
    ASSIST_STUN_MULTY = b'assist_stun_multy'
    AWARD = b'award'
    BASE_CAPTURE = b'base_capture'
    BASE_DEF = b'base_def'
    BATTLES = b'battles'
    CREDITS = b'credits'
    DAMAGE = b'damage'
    DAMAGE_BLOCK = b'damage_block'
    DISCOVER = b'discover'
    EXPERIENCE = b'experience'
    FIRE = b'fire'
    GET_DAMAGE = b'get_damage'
    GET_HIT = b'get_hit'
    HIT = b'hit'
    HURT_1SHOT = b'hurt_1shot'
    HURT_VEHICLES = b'hurt_vehicles'
    KILL_1SHOT = b'kill_1shot'
    KILL_VEHICLES = b'kill_vehicles'
    MASTER = b'master'
    METERS = b'meters'
    MODULE_CRIT = b'module_crit'
    PREPARATION = b'preparation'
    SAVE_HP = b'save_hp'
    SEC_ALIVE = b'sec_alive'
    SURVIVE = b'survive'
    TIMES_GET_DAMAGE = b'times_get_damage'
    TOP = b'top'
    WIN = b'win'
    FOLDER = b'folder'
    BARREL_MARK = b'barrel_mark'
    RAM = b'ram'
    MAIN_REPEAT = b'main_repeat'
    IMPROVE = b'improve'
    RANK_UP = b'rank_up'
    PRESTIGE_POINTS = b'prestige_points'


class PROGRESS_TEMPLATE:
    BINARY = b'binaryProgress'
    VALUE = b'valueProgress'
    COUNTER = b'counterProgress'
    BIATHLON = b'biathlonProgress'


class MISSION_TYPES:
    KILL = 0
    WIN = 1
    ASSIST = 2
    AUTO = 3
    DAMAGE = 4


class VISIBLE_SCOPE:
    BATTLE = b'battle'
    HANGAR = b'hangar'


class TARGET_NATIONS:
    SAME_ALLIANCE = b'sameAlliance'
    ANOTHER_ALLIANCE = b'anotherAlliance'


class CRIT_TYPES(object):
    INNER_MODULES_AND_TANKMEN = 0
    DESTROYED_TRACKS = 1
    ALL_MODULES = 2
    DESTROYED_INNER_MODULES_AND_TANKMAN = 3


class CONTAINER:
    HEADER = b'header'
    BODY = b'body'


class DISPLAY_TYPE:
    BIATHLON = b'biathlon'
    LIMITED = b'limited'
    SERIES = b'series'
    COUNTER = b'counter'
    SIMPLE = b'simple'
    NONE = b'none'


class MULTIPLIER_TYPE:
    ATTEMPTS = b'attempts'
    PROGRESS = b'progress'


class MULTIPLIER_SCOPE:
    POST_BATTLE = b'postBattle'
    CARD = b'card'


class IClientDescription(object):

    @classmethod
    def getContainerType(cls):
        raise NotImplementedError
        return

    def __repr__(self):
        return self.__class__.__name__


class RegularDescription(IClientDescription):
    __slots__ = (b'iconID', b'limiterID', b'isInOrGroup', b'priority')

    def __init__(self, iconID, limiterID=None, isInOrGroup=False, priority=0):
        self.iconID = iconID
        self.limiterID = limiterID
        self.isInOrGroup = isInOrGroup
        self.priority = priority
        return

    @classmethod
    def getContainerType(cls):
        return CONTAINER.BODY

    def __repr__(self):
        return self.__class__.__name__ + b': ' + str(self.iconID) + b' ' + str(self.limiterID) + b' ' + str(self.isInOrGroup) + b' ' + str(self.priority)


class AverageDescription(RegularDescription):
    __slots__ = RegularDescription.__slots__ + (b'counterID',)

    def __init__(self, iconID, counterID, limiterID=None, isInOrGroup=False, priority=0):
        super(AverageDescription, self).__init__(iconID, limiterID, isInOrGroup, priority)
        self.counterID = counterID
        return

    def __repr__(self):
        return self.__class__.__name__ + b': ' + str(self.iconID) + b' ' + str(self.counterID) + b' ' + str(self.limiterID) + b' ' + str(self.isInOrGroup)


class HeaderDescription(IClientDescription):
    __slots__ = (b'displayType', b'isInOrGroup')

    def __init__(self, displayType):
        self.displayType = displayType
        self.isInOrGroup = False
        return

    @classmethod
    def getContainerType(cls):
        return CONTAINER.HEADER

    def __repr__(self):
        return self.__class__.__name__ + b': ' + str(self.displayType) + b' ' + str(self.isInOrGroup)


class DESCRIPTIONS(object):
    REGULAR = RegularDescription
    AVERAGE = AverageDescription
    HEADER = HeaderDescription


class PROCESSOR_PARAMETERS:
    ATTACK_REASONS = b'attackReasons'
    UNIQUE_TARGET = b'uniqueTarget'
    UNIQUE_ATTACKER = b'uniqueAttacker'
    TARGET_NATIONS = b'targetNations'
    TARGET_ALLIANCE = b'targetAlliance'
    TARGET_CLASSES = b'targetClasses'
    TARGET_IMMOBILIZED = b'targetImmobilized'
    TARGET_LEVEL_GREATER_OR_EQUAL = b'targetLevelGreaterOrEqual'
    TARGET_LEVEL_DIFF = b'targetLevelDiff'
    STUN_SEVERAL_TARGETS = b'stunSeveralTargets'
    DISTANCE_GREATER_OR_EQUAL = b'distanceGreatOrEqual'
    DISTANCE_SHORTER_OR_EQUAL = b'distanceShortOrEqual'
    ATTACKER_UNHARMED = b'attackerUnharmed'
    DISTANCE_IN_VISION_RADIUS = b'distanceInVisionRadius'
    ATTACKER_STAY_ALIVE = b'attackerStayAlive'
    ATTACKER_WAS_INVISIBLE = b'attackerWasInvisible'
    ATTACKER_DEALT_MORE_DAMAGE = b'attackerDealtMoreDamage'
    DIRECT_HITS_RECEIVED = b'directHitsReceived'
    ATTACKER_CLASSES = b'attackerClasses'
    ATTACKER_MOVING_SPEED_GREATER_OR_EQUAL = b'attackerMovingSpeedGreaterOrEqual'
    TARGET_IS_STATIONARY = b'targetIsStationary'
    DAMAGE_DEALT = b'damageDealt'
    TARGET_IS_NOT_SPOTTED = b'targetIsNotSpotted'
    DESIRED_POSITION = b'desiredPosition'
    MEDAL = b'medal'
    VEHICLE_HEALTH_FACTOR = b'vehicleHealthFactor'
    ASSIST_TYPES = b'assistTypes'
    SHOULD_BE_UNSPOTTED = b'shouldBeUnspotted'
    SHOULD_BE_INVISIBLE = b'shouldBeInvisible'
    MARK_OF_MASTERY = b'markOfMastery'
    CRIT_TYPES = b'critTypes'
    HITS = b'hits'
    TARGET_IS_MOVING = b'targetIsMoving'


class CONFIG_KEYS:
    PARAMS = b'params'
    UNIQUE_VEHICLE = b'uniqueVehicle'
    GOAL = b'goal'
    IS_MAIN = b'isMain'
    IS_AWARD = b'isAward'
    VISIBLE_SCOPE = b'visibleScope'
    BATTLES_UNIQUE_VEHICLES = b'battlesUniqueVehicles'
    UNIQUE_BATTLES_COUNT = b'uniqueBattlesCount'


VEHICLE_RESTRICTION_MIN_LEVEL = 1
VEHICLE_RESTRICTION_MAX_LEVEL = 11
