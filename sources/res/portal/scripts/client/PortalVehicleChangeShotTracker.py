import BigWorld

class PortalVehicleChangeShotTracker(object):

    def __init__(self):
        self.__vehiclesUnderControl = set()
        return

    def subscribe(self):
        if self.vehicleChangeComponent is not None:
            self.vehicleChangeComponent.onStartVehicleControl += self.__onStartVehicleControl
            self.vehicleChangeComponent.onStopVehicleControl += self.__onStopVehicleControl
        return

    def unsubscribe(self):
        if self.vehicleChangeComponent is not None:
            self.vehicleChangeComponent.onStartVehicleControl -= self.__onStartVehicleControl
            self.vehicleChangeComponent.onStopVehicleControl -= self.__onStopVehicleControl
            self.__vehiclesUnderControl.clear()
        return

    def isVehicleUnderControl(self, vehicleID):
        return vehicleID in self.__vehiclesUnderControl

    @property
    def vehicleChangeComponent(self):
        return getattr(BigWorld.player(), b'DynamicVehicleChangeComponent', None)

    def __onStartVehicleControl(self, newVehicleID):
        self.__vehiclesUnderControl.add(newVehicleID)
        return

    def __onStopVehicleControl(self, prevVehicleID):
        self.__vehiclesUnderControl.discard(prevVehicleID)
        return
