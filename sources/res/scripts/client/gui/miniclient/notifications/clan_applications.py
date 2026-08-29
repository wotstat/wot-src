from gui import makeHtmlString
from helpers import aop
from notification.settings import NOTIFICATION_BUTTON_STATE

class _ClanMultiNotifAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        original_return_options[b'submit'] = NOTIFICATION_BUTTON_STATE.VISIBLE
        return original_return_options


class _BaseClanSingleNotifAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_options = cd.returned
        original_return_options[b'submit'] = NOTIFICATION_BUTTON_STATE.VISIBLE
        original_return_options[b'cancel'] = NOTIFICATION_BUTTON_STATE.VISIBLE
        return original_return_options


class _ClanSingleNotifHtmlTextFormatterAspect(aop.Aspect):

    def atReturn(self, cd):
        returned = cd.returned
        returned = makeHtmlString(b'html_templates:lobby/clans', b'appCommentMiniclient')
        cd.change()
        return returned


class ClanMultiNotifPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'notification.decorators', b'_ClanMultiDecorator', b'_getButtonsStates', aspects=(
         _ClanMultiNotifAspect,))
        return


class ClanSingleInviteNotifPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'notification.decorators', b'ClanSingleInviteDecorator', b'_getButtonsStates', aspects=(
         _BaseClanSingleNotifAspect,))
        return


class ClanSingleAppNotifPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'notification.decorators', b'ClanSingleAppDecorator', b'_getButtonsStates', aspects=(
         _BaseClanSingleNotifAspect,))
        return


class ClanSingleNotificationHtmlTextFormatterPointCut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.clans.formatters', b'ClanSingleNotificationHtmlTextFormatter', b'getComment', aspects=(
         _ClanSingleNotifHtmlTextFormatterAspect,))
        return
