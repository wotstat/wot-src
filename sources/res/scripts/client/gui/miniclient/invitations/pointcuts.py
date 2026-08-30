from helpers import aop
import aspects

class PrbDisableAcceptButton(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.prb_control.invites', b'InvitesManager', b'canAcceptInvite', aspects=(
         aspects.DisableAccept,))
        return


class PrbInvitationText(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.prb_control.formatters.invites', b'PrbInviteHtmlTextFormatter', b'getNote', aspects=(
         aspects.InvitationNote,))
        return
