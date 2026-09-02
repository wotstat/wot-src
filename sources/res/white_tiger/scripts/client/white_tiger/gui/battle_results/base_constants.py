from __future__ import absolute_import
from enum import Enum

class PresenterUpdateTypes(object):
    XP_BONUS = b'updateXpBonus'


class CommonTooltipType(Enum):
    EFFICIENCY_PARAMETER = b'efficiencyParameter'
    CRITICAL_DAMAGE_EFFICIENCY_PARAMETER = b'criticalDamageEfficiencyParameter'
