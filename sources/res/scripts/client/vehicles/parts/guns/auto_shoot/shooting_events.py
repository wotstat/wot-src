from __future__ import absolute_import
import typing, BigWorld, math_utils
from cgf_events import gun_events
from constants import SERVER_TICK_LENGTH
from events_handler import eventHandler
from helpers.CallbackDelayer import CallbackDelayer
from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootingEventsLogic, IAutoShootingListenerLogic
from vehicles.parts.guns.common import GunShootingEvents, GunShootingCoreIntegration, GunShootingEventsDebugger
if typing.TYPE_CHECKING:
    from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootGunComponent, IAutoShootGunComponentState
CONTINUOUS_ACTIVATION_DELTA = 0.0

class AutoShootingEvents(GunShootingEvents, IAutoShootingEventsLogic):

    def __init__(self, component):
        super(AutoShootingEvents, self).__init__(component)
        self.__componentState = None
        self.__lastDiscreteShotTime = 0.0
        self.__callbackDelayer = CallbackDelayer()
        self.onBurstActivation = self._createLateEvent(self.__lateBurstActivation)
        self.onContinuousBurstActivation = self._createLateEvent(self.__lateContinuousBurstActivation)
        self.onShotRateUpdate = self._createLateEvent(self.__lateShotRateUpdate)
        self.onBurstDeactivation = self._createEvent()
        self.onContinuousBurstDeactivation = self._createEvent()
        self.onContinuousBurstUpdate = self._createEvent()
        return

    def destroy(self):
        self.__destroyBurst()
        self.__callbackDelayer.destroy()
        self.__lastDiscreteShotTime = 0.0
        super(AutoShootingEvents, self).destroy()
        return

    def processAppearanceReady(self):
        super(AutoShootingEvents, self).processAppearanceReady()
        self.__componentState = self._getComponent().getComponentState()
        self.onShotRateUpdate(self.__componentState.getShotRatePerSecond())
        return

    def processDiscreteShot(self, gunIndex):
        self.__lastDiscreteShotTime = BigWorld.time()
        super(AutoShootingEvents, self).processDiscreteShot(gunIndex)
        return

    def updateAutoShootingState(self, componentState):
        newShotRatePerSecond = componentState.getShotRatePerSecond()
        prevComponentState, self.__componentState = self.__componentState, componentState
        if not math_utils.almostEqual(newShotRatePerSecond, prevComponentState.getShotRatePerSecond()):
            self.onShotRateUpdate(newShotRatePerSecond)
        isContinuousInProgress = self.__callbackDelayer.hasDelayedCallback(self.__updateContinuousBurst)
        if prevComponentState.isShooting() and not componentState.isShooting():
            self.__deactivateBurst(isContinuousInProgress)
            return
        isContinuousBurst = componentState.isContinuousShooting()
        if not prevComponentState.isShooting() and componentState.isShooting():
            self.__activateBurst(isContinuousBurst)
            return
        if isContinuousInProgress != isContinuousBurst:
            self.__switchBurstPhase(isContinuousBurst)
        return

    def _createCoreIntegration(self):
        return AutoShootingCoreIntegration(self, self._getComponent())

    def _createEventsDebugger(self):
        return AutoShootingEventsDebugger(self, self._getComponent())

    def _lateSubscribe(self, listener):
        super(AutoShootingEvents, self)._lateSubscribe(listener)
        self.__lateShotRateUpdate(listener.onShotRateUpdate)
        self.__lateContinuousBurstActivation(listener.onContinuousBurstActivation)
        self.__lateBurstActivation(listener.onBurstActivation)
        return

    def __activateBurst(self, isContinuousBurst):
        if isContinuousBurst:
            self.__activateContinuousBurst()
        self.onBurstActivation()
        return

    def __activateContinuousBurst(self):
        self.__lastDiscreteShotTime = BigWorld.time()
        self.__callbackDelayer.stopCallback(self.__tryActivateContinuousBurst)
        self.__callbackDelayer.delayCallback(SERVER_TICK_LENGTH, self.__updateContinuousBurst)
        self.onContinuousBurstActivation()
        return

    def __deactivateBurst(self, isContinuousInProgress):
        self.__callbackDelayer.stopCallback(self.__tryActivateContinuousBurst)
        if isContinuousInProgress:
            self.__deactivateContinuousBurst()
        self.onBurstDeactivation()
        return

    def __deactivateContinuousBurst(self):
        self.__lastDiscreteShotTime = BigWorld.time()
        self.__callbackDelayer.stopCallback(self.__updateContinuousBurst)
        self.onContinuousBurstDeactivation()
        return

    def __destroyBurst(self):
        if self.__componentState is not None and self.__componentState.isShooting():
            self.__deactivateBurst(self.__callbackDelayer.hasDelayedCallback(self.__updateContinuousBurst))
        return

    def __switchBurstPhase(self, isContinuousBurst):
        if isContinuousBurst:
            if self.__needDelayContinuousBurst():
                self.__callbackDelayer.delayCallback(CONTINUOUS_ACTIVATION_DELTA, self.__tryActivateContinuousBurst)
            else:
                self.__activateContinuousBurst()
        else:
            self.__deactivateContinuousBurst()
        return

    def __updateContinuousBurst(self):
        self.onContinuousBurstUpdate()
        return SERVER_TICK_LENGTH

    def __needDelayContinuousBurst(self):
        return self.__lastDiscreteShotTime + self.__componentState.getGroupShotInterval() > BigWorld.time()

    def __tryActivateContinuousBurst(self):
        if self.__needDelayContinuousBurst():
            return CONTINUOUS_ACTIVATION_DELTA
        return self.__activateContinuousBurst()

    def __lateBurstActivation(self, handler):
        if self.__componentState is not None and self.__componentState.isShooting():
            handler()
        return

    def __lateContinuousBurstActivation(self, handler):
        if self.__callbackDelayer.hasDelayedCallback(self.__updateContinuousBurst):
            handler()
        return

    def __lateShotRateUpdate(self, handler):
        if self.__componentState is not None:
            handler(self.__componentState.getShotRatePerSecond())
        return


class AutoShootingCoreIntegration(GunShootingCoreIntegration, IAutoShootingListenerLogic):

    @eventHandler
    def onContinuousBurstActivation(self):
        gun_events.postVehicularContinuousBurstEvent(self._spaceID, self._vehicleID, self._slotName, True)
        return

    @eventHandler
    def onContinuousBurstDeactivation(self):
        gun_events.postVehicularContinuousBurstEvent(self._spaceID, self._vehicleID, self._slotName, False)
        return

    @eventHandler
    def onShotRateUpdate(self, rate):
        gun_events.postVehicularFireRateChangedEvent(self._spaceID, self._vehicleID, self._slotName, rate)
        return


class AutoShootingEventsDebugger(GunShootingEventsDebugger):
    IGNORED_EVENTS = GunShootingEventsDebugger.IGNORED_EVENTS + (b'onContinuousBurstUpdate',)
    _EVENTS_DEBUG_PREFIX = b'AUTO_GUN'
