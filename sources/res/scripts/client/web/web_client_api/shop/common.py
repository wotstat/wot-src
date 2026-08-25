from account_helpers import AccountSettings
from account_helpers.AccountSettings import CUSTOM_SHOP_SETTINGS
from web.web_client_api import Field, W2CSchema, w2c

class _KeySchema(W2CSchema):
    key = Field(required=True, type=basestring)


class _KeyValueSchema(_KeySchema):
    key = Field(required=True, type=basestring)
    value = Field(required=True, type=(bool, int, float, basestring))


class SettingsWebApiMixin(object):

    @w2c(_KeySchema, b'get_setting')
    def getSetting(self, cmd):
        return AccountSettings.getSettings(CUSTOM_SHOP_SETTINGS).get(cmd.key)

    @w2c(_KeyValueSchema, b'set_setting')
    def setSetting(self, cmd):
        settings = AccountSettings.getSettings(CUSTOM_SHOP_SETTINGS)
        settings[cmd.key] = cmd.value
        AccountSettings.setSettings(CUSTOM_SHOP_SETTINGS, settings)
        return

    @w2c(_KeySchema, b'remove_setting')
    def remove(self, cmd):
        settings = AccountSettings.getSettings(CUSTOM_SHOP_SETTINGS)
        settings.pop(cmd.key)
        AccountSettings.setSettings(CUSTOM_SHOP_SETTINGS, settings)
        return

    @w2c(W2CSchema, b'get_settings')
    def getSettings(self, _):
        return AccountSettings.getSettings(CUSTOM_SHOP_SETTINGS)

    @w2c(W2CSchema, b'clear_settings')
    def clear(self, _):
        AccountSettings.setSettings(CUSTOM_SHOP_SETTINGS, {})
        return
