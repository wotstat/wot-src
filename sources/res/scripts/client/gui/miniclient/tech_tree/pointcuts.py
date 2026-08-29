import aspects
from helpers import aop

class OnTechTreePopulate(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.techtree.techtree_page', b'TechTree', b'_populate', aspects=(
         aspects.OnTechTreePopulate,))
        return


class OnBuyVehicle(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows', b'VehicleBuyWindow', b'submit', aspects=(
         aspects.OnBuyVehicle(config),))
        return


class OnRestoreVehicle(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.vehicle_obtain_windows', b'VehicleRestoreWindow', b'submit', aspects=(
         aspects.OnRestoreVehicle(config),))
        return
