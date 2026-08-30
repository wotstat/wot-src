from __future__ import absolute_import
import typing
from vehicles.parts.guns.common import IGunComponent, IGunShootingEvents, IGunShootingListener

class ITwinShootGunComponent(IGunComponent):

    def isDoubleBarrelMode(self):
        raise NotImplementedError
        return

    def getActiveGunIndexes(self):
        raise NotImplementedError
        return

    def getAfterShotDelay(self):
        raise NotImplementedError
        return

    def getNextGunIndexes(self):
        raise NotImplementedError
        return


class ITwinShootingEventsLogic(object):
    onActiveGunsUpdate = None
    onAnimatedGunsUpdate = None

    def processNextGunsUpdate(self, nextGunIndexes):
        raise NotImplementedError
        return


class ITwinShootingEvents(IGunShootingEvents, ITwinShootingEventsLogic):
    pass


class ITwinShootingListenerLogic(object):

    def onActiveGunsUpdate(self, gunIndexes):
        return

    def onAnimatedGunsUpdate(self, gunIndexes):
        return


class ITwinShootingListener(IGunShootingListener, ITwinShootingListenerLogic):
    pass
