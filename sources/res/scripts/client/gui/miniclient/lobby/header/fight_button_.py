from helpers import aop
from CurrentVehicle import g_currentVehicle

class _DisableFightButtonAspect(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config[b'vehicle_is_available']
        aop.Aspect.__init__(self)
        return

    def atCall(self, cd):
        if g_currentVehicle.isPresent() and not self.__vehicle_is_available(g_currentVehicle.item):
            cd.change()
            original_args = list(cd.args)
            original_args[0] = True
            return (
             original_args, cd.kwargs)
        return


class DisableFightButtonPointcut(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.header.LobbyHeader', b'LobbyHeader', b'as_disableFightButtonS', aspects=(
         _DisableFightButtonAspect(config),))
        return


class DisableTrainingFightButtonPointcut(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.trainings.TrainingRoomBase', b'TrainingRoomBase', b'as_disableStartButtonS', aspects=(
         _DisableFightButtonAspect(config),))
        return


class _DisableBattlesForHiddenVehiclesAspect(aop.Aspect):

    def __init__(self, config):
        self.__vehicle_is_available = config[b'vehicle_is_available']
        aop.Aspect.__init__(self)
        return

    def atReturn(self, cd):
        if not self.__vehicle_is_available(cd.self):
            cd.change()
            return False
        return


class DisableBattlesForHiddenVehicles(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.shared.gui_items.Vehicle', b'Vehicle', b'isReadyToPrebattle', aspects=(
         _DisableBattlesForHiddenVehiclesAspect(config),))
        return
