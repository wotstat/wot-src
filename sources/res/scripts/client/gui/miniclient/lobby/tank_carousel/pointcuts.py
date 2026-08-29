from helpers import aop
import aspects

class MakeTankUnavailableInCarousel(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.common.vehicle_carousel', b'carousel_data_provider', b'getVehicleDataVO', aspects=(
         aspects.MakeTankUnavailableInCarousel(config),))
        return


class VehicleTooltipStatus(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.shared.tooltips.vehicle', b'StatusBlockConstructor', b'_StatusBlockConstructor__getVehicleStatus', aspects=(
         aspects.VehicleTooltipStatus(config),))
        return
