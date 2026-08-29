from helpers import aop
from helpers.i18n import makeString as _ms
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.formatters import text_styles

class VehicleTooltipStatus(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config[b'vehicle_is_available']
        aop.Aspect.__init__(self)
        return

    def atCall(self, cd):
        if not self.__vehicle_is_available(cd.args[2]):
            cd.avoid()
            return {b'header': (_ms(b'#menu:tankCarousel/vehicleStates/%s' % Vehicle.VEHICLE_STATE.UNAVAILABLE)), 
               b'text': b'', 
               b'level': (Vehicle.VEHICLE_STATE_LEVEL.CRITICAL)}
        return


class MakeTankUnavailableInCarousel(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config[b'vehicle_is_available']
        aop.Aspect.__init__(self)
        return

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_args = cd.args
        if not self.__vehicle_is_available(original_args[0]):
            state = _ms((b'#menu:tankCarousel/vehicleStates/{}').format(Vehicle.VEHICLE_STATE.UNAVAILABLE))
            original_return_value[b'infoText'] = text_styles.vehicleStatusCriticalText(state)
            original_return_value[b'smallInfoText'] = text_styles.critical(state)
        return original_return_value
