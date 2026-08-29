from gui.Scaleform.daapi.view.lobby.user_cm_handlers import USER
from helpers import aop

class UserCmClanUnavailableAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        for item in original_return_options:
            if item[b'id'] == USER.CLAN_INFO:
                if not item[b'initData']:
                    item[b'initData'] = {}
                item[b'initData'][b'enabled'] = False
                break

        return original_return_options


class UserCmInviteClanUnavailableAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        for item in original_return_options:
            if item[b'id'] == USER.SEND_CLAN_INVITE:
                if not item[b'initData']:
                    item[b'initData'] = {}
                item[b'initData'][b'enabled'] = False
                break

        return original_return_options


class UserCmClanUnavailablePointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.user_cm_handlers', b'BaseUserCMHandler', b'_addClanProfileInfo', aspects=(
         UserCmClanUnavailableAspect,))
        return


class UserCmInviteClanUnavailablePointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.user_cm_handlers', b'BaseUserCMHandler', b'_addInviteClanInfo', aspects=(
         UserCmInviteClanUnavailableAspect,))
        return
