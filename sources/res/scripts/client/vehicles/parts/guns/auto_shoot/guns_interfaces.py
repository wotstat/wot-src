from __future__ import absolute_import
from vehicles.parts.guns.common import IGunComponent, IGunShootingEvents, IGunShootingListener

class IAutoShootDispersionState(object):

    def getCurrentDispersionFactor(self):
        raise NotImplementedError
        return


class IAutoShootGunComponentState(object):

    def isShooting(self):
        raise NotImplementedError
        return

    def isContinuousShooting(self):
        raise NotImplementedError
        return

    def getDefaultShotRatePerSecond(self):
        raise NotImplementedError
        return

    def getGroupShotInterval(self):
        raise NotImplementedError
        return

    def getShotRatePerSecond(self):
        raise NotImplementedError
        return


class IAutoShootGunComponent(IGunComponent):

    def getComponentState(self):
        raise NotImplementedError
        return

    def getDispersionState(self):
        raise NotImplementedError
        return


class IAutoShootingEventsLogic(object):
    onBurstActivation = None
    onBurstDeactivation = None
    onContinuousBurstActivation = None
    onContinuousBurstDeactivation = None
    onContinuousBurstUpdate = None
    onShotRateUpdate = None

    def updateAutoShootingState(self, componentState):
        raise NotImplementedError
        return


class IAutoShootingEvents(IGunShootingEvents, IAutoShootingEventsLogic):
    pass


class IAutoShootingListenerLogic(object):

    def onBurstActivation(self):
        return

    def onBurstDeactivation(self):
        return

    def onContinuousBurstActivation(self):
        return

    def onContinuousBurstDeactivation(self):
        return

    def onContinuousBurstUpdate(self):
        return

    def onShotRateUpdate(self, rate):
        return


class IAutoShootingListener(IGunShootingListener, IAutoShootingListenerLogic):
    pass
