import BigWorld
from gui.DialogsInterface import showDialog
from gui.Scaleform.daapi.view.dialogs import SimpleDialogMeta
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogButtons, DIALOG_BUTTON_ID
from gui.shared.formatters import icons
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import aop
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache

class OnTechTreePopulate(aop.Aspect):

    def atReturn(self, cd):
        cd.self.as_showMiniClientInfoS(_ms(b'#miniclient:tech_tree/description'), _ms(b'#miniclient:tech_tree/continue_download'))
        return


class OnBuyVehicle(aop.Aspect):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, config):
        self.__vehicle_is_available = config[b'vehicle_is_available']
        self._localKey = b'#miniclient:buy_vehicle/%s'
        aop.Aspect.__init__(self)
        return

    def atCall(self, cd):
        vehicleItem = self.itemsCache.items.getItem(GUI_ITEM_TYPE.VEHICLE, cd.self.nationID, cd.self.inNationID)
        if self.__vehicle_is_available(vehicleItem):
            return
        else:
            cd.avoid()

            def dialogButtonClickHandler(confirm):
                if confirm:
                    BigWorld.callback(0.1, (lambda : cd.self._VehicleBuyWindow__requestForMoneyObtain(cd.args[0])))
                else:
                    cd.self.as_setEnabledSubmitBtnS(True)
                return

            showDialog(SimpleDialogMeta(title=_ms(self._localKey % b'title'), message=icons.alert() + _ms(self._localKey % b'message'), buttons=I18nConfirmDialogButtons(i18nKey=b'questsConfirmDialog', focusedIndex=DIALOG_BUTTON_ID.SUBMIT)), dialogButtonClickHandler)
            return


class OnRestoreVehicle(OnBuyVehicle):

    def __init__(self, config):
        super(OnRestoreVehicle, self).__init__(config)
        self._localKey = b'#miniclient:restore_vehicle/%s'
        return
