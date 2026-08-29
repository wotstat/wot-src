import aspects
from helpers import aop

class MakeVehicleCompareUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.game_control.veh_comparison_basket', b'VehComparisonBasket', b'isAvailable', aspects=(
         aspects.MakeVehicleCompareUnavailable,))
        return
