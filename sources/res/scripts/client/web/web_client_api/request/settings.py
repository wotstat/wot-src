import helpers
from gui.limited_ui.lui_rules_storage import LuiRules
from helpers import dependency
from skeletons.gui.game_control import ILimitedUIController
from web.web_client_api import W2CSchema, w2c

class SettingsWebApiMixin(object):
    __limitedUIController = dependency.descriptor(ILimitedUIController)
    _MODE_HIDE_COUNTERS = b'hide_counters'

    @w2c(W2CSchema, b'settings')
    def getSettings(self, _):
        return {b'client_version': (helpers.getClientVersion()), 
           b'ui_spam_mode': (b'' if self.__limitedUIController.isRuleCompleted(LuiRules.LOBBY_HEADER_COUNTERS_STORE) else self._MODE_HIDE_COUNTERS), 
           b'is_frontline_content_available': (self.__limitedUIController.isRuleCompleted(LuiRules.FRONTLINE_CONTENT))}
