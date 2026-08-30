from __future__ import absolute_import
import typing
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel

class ProgressCounterClientModel(TextClientModel):
    __slots__ = (b'id', b'header', b'icon')

    def __init__(self, id, header, icon):
        super(ProgressCounterClientModel, self).__init__()
        self.id = id
        self.header = header
        self.icon = icon
        return

    def getHeader(self, params):
        return self._getPluralText(self.header, params)

    def __repr__(self):
        return b'<ProgressCounterClientModel>: id=%s, header=%s, icon=%s' % (
         self.id, self.header, self.icon)
