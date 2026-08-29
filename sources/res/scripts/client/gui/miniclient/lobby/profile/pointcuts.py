from helpers import aop
import aspects

class MakeClanBtnUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryWindow', b'ProfileSummaryWindow', b'_getClanBtnParams', aspects=(
         aspects.MakeClanBtnUnavailable(),))
        return


class MakeClubProfileButtonUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryWindow', b'ProfileSummaryWindow', b'_getClubProfileButtonParams', aspects=(
         aspects.MakeClubProfileButtonUnavailable(),))
        return
