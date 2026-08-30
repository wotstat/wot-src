from debug_utils import LOG_DEBUG
from gui.shared.utils import graphics
from web.web_client_api import w2c, W2CSchema

class GraphicsSettingsWebApiMixin(object):

    @w2c(W2CSchema, b'graphics_settings')
    def graphicsSettings(self, cmd):
        settings = {}
        settingNames = (b'TEXTURE_QUALITY', b'LIGHTING_QUALITY', b'SHADOWS_QUALITY', b'SNIPER_MODE_GRASS_ENABLED', b'EFFECTS_QUALITY', b'SNIPER_MODE_EFFECTS_QUALITY', b'FLORA_QUALITY', b'POST_PROCESSING_QUALITY', b'VEHICLE_DUST_ENABLED', b'CUSTOM_AA_MODE', b'MSAA_QUALITY', b'RENDER_PIPELINE')
        for settingName in settingNames:
            setting = graphics.getGraphicsSetting(settingName)
            if setting is not None:
                settings[settingName] = setting.value
            else:
                LOG_DEBUG(b'Settings "%s" not found!' % settingName)

        return {b'request_id': b'graphics_settings', b'settings': settings}
