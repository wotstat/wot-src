from debug_utils import LOG_WARNING

class QUESTSPROGRESS(object):
    QP_DOT = b'qp_dot'
    C_183X63_OPERATION_1 = b'183x63_operation_1'
    C_183X63_OPERATION_10 = b'183x63_operation_10'
    C_183X63_OPERATION_11 = b'183x63_operation_11'
    C_183X63_OPERATION_2 = b'183x63_operation_2'
    C_183X63_OPERATION_3 = b'183x63_operation_3'
    C_183X63_OPERATION_4 = b'183x63_operation_4'
    C_183X63_OPERATION_5 = b'183x63_operation_5'
    C_183X63_OPERATION_6 = b'183x63_operation_6'
    C_183X63_OPERATION_7 = b'183x63_operation_7'
    C_183X63_OPERATION_8 = b'183x63_operation_8'
    C_183X63_OPERATION_9 = b'183x63_operation_9'
    DONE = b'done'
    FAILED = b'failed'
    IN_PROGRESS = b'in_progress'
    LOCKED = b'locked'
    QUEST_DONE = b'quest_done'
    QUEST_DONE_PERFECTLY = b'quest_done_perfectly'
    QUEST_IN_PROGRESS = b'quest_in_progress'
    QUEST_NOT_AVAILABLE = b'quest_not_available'
    QUEST_ON_PAUSE = b'quest_on_pause'
    WARNING = b'warning'
    ORANGE_AT_SPG = b'orange_AT-SPG'
    ORANGE_HEAVY_TANK = b'orange_heavyTank'
    ORANGE_LIGHT_TANK = b'orange_lightTank'
    ORANGE_MEDIUM_TANK = b'orange_mediumTank'
    ORANGE_SPG = b'orange_SPG'
    SILVER_AT_SPG = b'silver_AT-SPG'
    SILVER_HEAVY_TANK = b'silver_heavyTank'
    SILVER_LIGHT_TANK = b'silver_lightTank'
    SILVER_MEDIUM_TANK = b'silver_mediumTank'
    SILVER_SPG = b'silver_SPG'
    SILVER_ENUM = (
     SILVER_AT_SPG,
     SILVER_HEAVY_TANK,
     SILVER_LIGHT_TANK,
     SILVER_MEDIUM_TANK,
     SILVER_SPG)
    ORANGE_ENUM = (
     ORANGE_AT_SPG,
     ORANGE_HEAVY_TANK,
     ORANGE_LIGHT_TANK,
     ORANGE_MEDIUM_TANK,
     ORANGE_SPG)
    C_183X63_OPERATION_ENUM = (
     C_183X63_OPERATION_1,
     C_183X63_OPERATION_10,
     C_183X63_OPERATION_11,
     C_183X63_OPERATION_2,
     C_183X63_OPERATION_3,
     C_183X63_OPERATION_4,
     C_183X63_OPERATION_5,
     C_183X63_OPERATION_6,
     C_183X63_OPERATION_7,
     C_183X63_OPERATION_8,
     C_183X63_OPERATION_9)

    @classmethod
    def getQPSilverVehicleType(cls, vType):
        outcome = (b'silver_{}').format(vType)
        if outcome not in cls.SILVER_ENUM:
            LOG_WARNING((b'Class constant "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getQPOrangeVehicleType(cls, vType):
        outcome = (b'orange_{}').format(vType)
        if outcome not in cls.ORANGE_ENUM:
            LOG_WARNING((b'Class constant "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getOperationTrackingIcon(cls, operationID):
        outcome = (b'183x63_operation_{}').format(operationID)
        if outcome not in cls.C_183X63_OPERATION_ENUM:
            LOG_WARNING((b'Class constant "{}" not found').format(outcome))
            return None
        else:
            return outcome
