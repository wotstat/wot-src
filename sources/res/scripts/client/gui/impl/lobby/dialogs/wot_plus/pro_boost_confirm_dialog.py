import json
from collections import namedtuple
import WWISE
from typing import Dict
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import ButtonType
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_view_model import MonoDialogTemplateViewModel
from gui.impl.lobby.dialogs.wot_plus.base_dialog import BaseDialog
_ProBoostConfirmDialogParams = namedtuple(b'confirmDialogParams', [
 b'vehicleName',
 b'cooldown',
 b'bonusPercentage'])

class ProBoostConfirmDialog(BaseDialog):

    def __init__(self, contentParams, *args, **kwargs):
        contentParams = self._buildContentParams(contentParams)
        resourcesParams = self._buildResourcesParams()
        super(ProBoostConfirmDialog, self).__init__(contentParams, resourcesParams, *args, **kwargs)
        return

    def _buildContentParams(self, contentParams):
        return {b'titleStringParams': (json.dumps({b'vehicle': (contentParams.vehicleName)})), 
           b'descriptionStringParams': (json.dumps({b'boostInterval': (str(contentParams.cooldown))})), 
           b'footerStringParams': (json.dumps({b'bonusPercent': (str(contentParams.bonusPercentage) + b'%')})), 
           b'footerHighlightColor': b'#FFEEA9'}

    def _buildResourcesParams(self):
        return {b'titleString': (backport.text(R.strings.dialogs.wotPlusProBoostActivationDialog.title())), 
           b'iconImage': (backport.image(R.images.gui.maps.icons.subscription.pro_boost_activation_dialog.pro_boost_activation_icon())), 
           b'descriptionString': (backport.text(R.strings.dialogs.wotPlusProBoostActivationDialog.description())), 
           b'footerString': (backport.text(R.strings.dialogs.wotPlusProBoostActivationDialog.footer())), 
           b'footerImage': (backport.image(R.images.gui.maps.icons.subscription.pro_boost_activation_dialog.pro_boost_footer_icon()))}

    def _setButtons(self):
        with self.viewModel.transaction() as vm:
            buttonsArray = vm.getButtons()
            buttonsArray.clear()
            self._addButton(self._buildButton(MonoDialogTemplateViewModel.ACTION_CONFIRM, R.strings.dialogs.wotPlusProBoostActivationDialog.confirm(), ButtonType.PRIMARY, False))
            self._addButton(self._buildButton(MonoDialogTemplateViewModel.ACTION_CANCEL, R.strings.dialogs.common.cancel(), ButtonType.SECONDARY, False))
        return

    def _onAction(self, event):
        super(ProBoostConfirmDialog, self)._onAction(event)
        actionType = event.get(b'action')
        if actionType == MonoDialogTemplateViewModel.ACTION_CONFIRM:
            WWISE.WW_eventGlobal(backport.sound(R.sounds.gui_wotp_proboost_activate()))
        return
