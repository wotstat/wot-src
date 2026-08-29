from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.view.meta.BaseContactViewMeta import BaseContactViewMeta

class BaseContactView(BaseContactViewMeta):

    def onCancel(self):
        return

    def _populate(self):
        super(BaseContactView, self)._populate()
        self.as_setInitDataS(self._getInitDataObject())
        return

    def _getInitDataObject(self):
        LOG_ERROR(b'this method have to be overridden!')
        return self._getDefaultInitData(b'', b'', b'', b'', b'')

    def _getDefaultInitData(self, mainLbl, btOkLbl, btnCancelLbl, btOkTooltip, btnCancelTooltip):
        return {b'btOkLbl': btOkLbl, 
           b'btnCancelLbl': btnCancelLbl, 
           b'mainLbl': mainLbl, 
           b'btOkTooltip': btOkTooltip, 
           b'btnCancelTooltip': btnCancelTooltip}
