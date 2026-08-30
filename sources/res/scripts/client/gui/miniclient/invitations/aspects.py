from gui import makeHtmlString
from helpers import aop
from helpers.i18n import makeString as _ms
from constants import PREBATTLE_TYPE_NAMES
from notification.settings import NOTIFICATION_BUTTON_STATE

class DisableAccept(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InvitationNote(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        battle_type = PREBATTLE_TYPE_NAMES[cd.args[0].type]
        return makeHtmlString(b'html_templates:lobby/prebattle', b'inviteNote', {b'note': (_ms((b'#miniclient:invitation/note/{0}').format(battle_type)))})


class DisableAcceptButton(aop.Aspect):

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_buttons = original_return_value[b'message'][b'buttonsStates']
        original_buttons[b'submit'] = original_buttons[b'submit'] & ~NOTIFICATION_BUTTON_STATE.ENABLED
        return original_return_value
