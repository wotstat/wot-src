import aspects
from helpers import aop

class ShowMiniclientInfo(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.hangar.Hangar', b'Hangar', b'_populate', aspects=(
         aspects.ShowMiniclientInfo,))
        return


class DisableTankServiceButtons(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.hangar.Hangar', b'Hangar', b'as_setupAmmunitionPanelS', aspects=(
         aspects.DisableTankServiceButtons(config),))
        return


class TankModelHangarVisibility(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'CurrentVehicle', b'_CurrentVehicle', b'isInHangar', aspects=(
         aspects.TankModelHangarVisibility(config),))
        return


class TankHangarStatus(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'CurrentVehicle', b'_CurrentVehicle', b'getHangarMessage', aspects=(
         aspects.TankHangarStatus(config),))
        return


class EnableCrew(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.hangar.Hangar', b'Hangar', b'as_setCrewEnabledS', aspects=(
         aspects.EnableCrew(config),))
        return


class ChangeLobbyMenuTooltip(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby', b'LobbyMenu', b'_getVersionMessage', aspects=(
         aspects.ChangeLobbyMenuTooltip,))
        return
