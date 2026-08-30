import json
from collections import namedtuple
import WWISE
from typing import Dict
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import ButtonType
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_view_model import MonoDialogTemplateViewModel
from gui.impl.lobby.dialogs.wot_plus.base_dialog import BaseDialog
_ProBoostSwitchDialogVehicleParams = namedtuple(b'_ProBoostSwitchDialogVehicleParams', [
 b'vehicleItemImagePath',
 b'vehicleName',
 b'vehicleTier',
 b'vehicleIcon'])
_ProBoostSwitchDialogParams = namedtuple(b'_ProBoostSwitchDialogParams', [
 b'vehicleFrom',
 b'vehicleTo',
 b'cooldown',
 b'bonusPercentage'])

class ProBoostSwitchDialog(BaseDialog):
    LAYOUT_ID = R.views.mono.dialogs.pro_boost_switch_dialog()

    def __init__(self, params, *args, **kwargs):
        contentParams = self._buildContentParams(params)
        resourcesParams = self._buildResourcesParams(params)
        super(ProBoostSwitchDialog, self).__init__(contentParams, resourcesParams, *args, **kwargs)
        return

    def _buildContentParams(self, contentParams):
        return {b'fromItemLabelParams': (json.dumps({b'tier': (contentParams.vehicleFrom.vehicleTier), 
                                    b'type_image': (backport.image(contentParams.vehicleFrom.vehicleIcon())), 
                                    b'name': (contentParams.vehicleFrom.vehicleName)})), 
           b'toItemLabelParams': (json.dumps({b'tier': (contentParams.vehicleTo.vehicleTier), 
                                  b'type_image': (backport.image(contentParams.vehicleTo.vehicleIcon())), 
                                  b'name': (contentParams.vehicleTo.vehicleName)})), 
           b'titleStringParams': (json.dumps({b'vehicle': (contentParams.vehicleTo.vehicleName)})), 
           b'descriptionStringParams': (json.dumps({b'boostInterval': (str(contentParams.cooldown))})), 
           b'footerStringParams': (json.dumps({b'bonusPercent': (str(contentParams.bonusPercentage) + b'%')})), 
           b'footerHighlightColor': b'#FFEEA9'}

    def _buildResourcesParams(self, contentParams):
        return {b'fromItemImage': (backport.image(contentParams.vehicleFrom.vehicleItemImagePath)), 
           b'fromItemLabel': (backport.text(R.strings.dialogs.wotPlusProBoostSwitchDialog.vehicle())), 
           b'toItemImage': (backport.image(contentParams.vehicleTo.vehicleItemImagePath)), 
           b'toItemLabel': (backport.text(R.strings.dialogs.wotPlusProBoostSwitchDialog.vehicle())), 
           b'titleString': (backport.text(R.strings.dialogs.wotPlusProBoostSwitchDialog.title())), 
           b'descriptionString': (backport.text(R.strings.dialogs.wotPlusProBoostSwitchDialog.description())), 
           b'footerString': (backport.text(R.strings.dialogs.wotPlusProBoostSwitchDialog.footer())), 
           b'footerImage': (backport.image(R.images.gui.maps.icons.subscription.pro_boost_activation_dialog.pro_boost_footer_icon()))}

    def _setButtons(self):
        with self.viewModel.transaction() as model:
            buttonsArray = model.getButtons()
            buttonsArray.clear()
            self._addButton(self._buildButton(MonoDialogTemplateViewModel.ACTION_CONFIRM, R.strings.dialogs.wotPlusProBoostSwitchDialog.confirm(), ButtonType.PRIMARY, False))
            self._addButton(self._buildButton(MonoDialogTemplateViewModel.ACTION_CANCEL, R.strings.dialogs.common.cancel(), ButtonType.SECONDARY, False))
        return

    def _onAction(self, event):
        super(ProBoostSwitchDialog, self)._onAction(event)
        actionType = event.get(b'action')
        if actionType == MonoDialogTemplateViewModel.ACTION_CONFIRM:
            WWISE.WW_eventGlobal(backport.sound(R.sounds.gui_wotp_proboost_activate()))
        return
