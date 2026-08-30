from __future__ import absolute_import, division
import typing
from gui.battle_control import avatar_getter
from gui.battle_control.arena_info.interfaces import IAimingSoundsCtrl
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
_AIMING_SOUND = b'sight_convergence'
_DUAL_ACC_SOUND = b'dual_aiming'
_EMPTY_SOUND = b''

class AimingSoundsCtrl(IAimingSoundsCtrl):

    def __init__(self):
        self.__isAimingEnded = False
        self.__isDualAimingEnded = False
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.AIMING_SOUNDS_CTRL

    def updateDispersion(self, shotFactor, multFactor, aimingFactor, idealFactor, dualAccMultFactor, dualAccFactor, idealDualAccFactor, hasDualAcc):
        isGunInUse = shotFactor > 0
        self.__updateDispersion(multFactor, aimingFactor, idealFactor, self.__setAimingEnded, _DUAL_ACC_SOUND if hasDualAcc else _AIMING_SOUND, self.__isAimingEnded or isGunInUse)
        self.__updateDispersion(dualAccMultFactor, dualAccFactor, idealDualAccFactor, self.__setDualAimingEnded, _AIMING_SOUND if hasDualAcc else _EMPTY_SOUND, self.__isDualAimingEnded or isGunInUse)
        return

    def __setAimingEnded(self, value):
        self.__isAimingEnded = value
        return

    def __setDualAimingEnded(self, value):
        self.__isDualAimingEnded = value
        return

    def __playSoundNotification(self, notification):
        soundNotifications = avatar_getter.getSoundNotifications()
        if soundNotifications is not None and notification:
            soundNotifications.play(notification)
        return

    def __updateDispersion(self, multFactor, aimingFactor, idealFactor, aimingSetter, notification, skipNotification):
        if aimingFactor < idealFactor:
            if abs(idealFactor - multFactor) < 0.001:
                if not skipNotification:
                    self.__playSoundNotification(notification)
                aimingSetter(True)
            elif idealFactor / multFactor > 1.1:
                aimingSetter(False)
        elif aimingFactor / multFactor > 1.1:
            aimingSetter(False)
        return
