from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from helpers import aop
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS

class MakeStrongholdsUnavailable(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        tooltip = TOOLTIPS.HEADER_BUTTONS_FORTS_SANDBOX_TURNEDOFF
        return {b'label': (MENU.HEADERBUTTONS_CLAN), 
           b'value': (VIEW_ALIAS.LOBBY_STRONGHOLD), 
           b'tooltip': tooltip, 
           b'enabled': False}
