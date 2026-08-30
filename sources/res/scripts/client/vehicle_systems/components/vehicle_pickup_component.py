class VehiclePickupComponent(object):
    MAX_ANGLE_DEVIATION = 5.0
    MAX_LIFETIME = 1.0

    def __init__(self, appearance):
        self.__appearance = appearance
        self.time = 0.0
        return

    @property
    def appearance(self):
        return self.__appearance
