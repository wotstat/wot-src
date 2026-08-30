from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import BaseClientModel

class EnemyListClientModel(BaseClientModel):
    __slots__ = (b'showSpottedIcon', b'highlightElite')

    def __init__(self, showSpottedIcon, highlightElite):
        super(EnemyListClientModel, self).__init__()
        self.showSpottedIcon = showSpottedIcon
        self.highlightElite = highlightElite
        return

    def __repr__(self):
        return b'<EnemyListClientModel>: showSpottedIcon=%s, highlightElite=%s' % (
         self.showSpottedIcon, self.highlightElite)
