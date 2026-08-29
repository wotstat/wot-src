from account_helpers.settings_core.settings_constants import GAME
from gui.battle_control.arena_info.settings import PERSONAL_STATUS
from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class ParametrizeInitPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.battle_control.battle_ctx', b'BattleContext', b'isInvitationEnabled', aspects=(
         _ParametrizeInitAspect,))
        return


class _RemoveShowInvitesFlagAspect(aop.Aspect):

    def atCall(self, cd):
        status = cd.findArg(0, b'bitmask')
        if status & PERSONAL_STATUS.SHOW_ALLY_INVITES > 0:
            status ^= PERSONAL_STATUS.SHOW_ALLY_INVITES
            return cd.changeArgs((0, b'bitmask', status))
        else:
            return


class RemoveShowInvitesFlagPointcut(aop.Pointcut):

    def __init__(self):
        super(RemoveShowInvitesFlagPointcut, self).__init__(b'gui.Scaleform.daapi.view.battle.shared.stats_exchange', b'BattleStatisticsDataController', b'as_setPersonalStatusS', aspects=(
         _RemoveShowInvitesFlagAspect(),))
        return


class _DisableGameSettingAspect(aop.Aspect):

    def atCall(self, cd):
        if cd.self.settingName == GAME.RECEIVE_INVITES_IN_BATTLE:
            cd.avoid()
        return


class DisableGameSettingPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'account_helpers.settings_core.options', b'MessengerSetting', b'_get', aspects=(
         _DisableGameSettingAspect,))
        return


class InviteReceivedMessagePointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.battle_control.controllers.dyn_squad_functional', b'DynSquadMessagesController', b'_inviteReceived', aspects=(
         aop.DummyAspect,))
        return
