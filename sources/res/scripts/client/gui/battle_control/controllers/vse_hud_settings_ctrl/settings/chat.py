from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import BaseClientModel

class ChatModel(BaseClientModel):
    __slots__ = (b'hide',)

    def __init__(self, hide):
        super(ChatModel, self).__init__()
        self.hide = hide
        return

    def __repr__(self):
        return b'<ChatModel>: hide=%s' % self.hide
