from helpers import aop
from helpers.i18n import makeString as _ms
from gui.shared.gui_items import GUI_ITEM_TYPE

class _OnShopItemWrapAspect(aop.Aspect):

    def __init__(self, config):
        self.__config = config
        aop.Aspect.__init__(self)
        return

    def atReturn(self, cd):
        original_wrapping = cd.returned
        packedItem = cd.args[0]
        module = packedItem[0]
        warnMessage = b''
        if module.itemTypeID == GUI_ITEM_TYPE.VEHICLE and not self.__config[b'vehicle_is_available'](module):
            warnMessage = _ms(b'#miniclient:shop_vehicle_item_renderer/warn_message')
        original_wrapping[b'warnMessage'] = warnMessage
        return original_wrapping


class OnShopItemWrapPointcut(aop.Pointcut):

    def __init__(self, config):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.store.tabs.shop', b'ShopVehicleTab', b'itemWrapper', aspects=(
         _OnShopItemWrapAspect(config),))
        return
