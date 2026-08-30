from __future__ import absolute_import

class CollectorVehicleConsts(object):
    CONFIG_NAME = b'collector_vehicle_config'
    COLLECTOR_VEHICLES_TAG = b'collectorVehicle'
    COLLECTOR_MEDAL_PREFIX = b'collectorVehicle'
    IS_ENABLED = b'enabled'


class CollectorVehicleConfig(object):
    __slots__ = (b'__config',)

    def __init__(self, config):
        self.__config = config
        return

    @property
    def isEnabled(self):
        return self.__config.get(CollectorVehicleConsts.IS_ENABLED, False)
