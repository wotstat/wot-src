from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import BaseClientModel

class AllyListClientModel(BaseClientModel):
    __slots__ = (b'showFrags', b'showVehicleTypeIcon', b'highlightElite')

    def __init__(self, showFrags, showVehicleTypeIcon, highlightElite):
        super(AllyListClientModel, self).__init__()
        self.showFrags = showFrags
        self.showVehicleTypeIcon = showVehicleTypeIcon
        self.highlightElite = highlightElite
        return

    def __repr__(self):
        return b'<AllyListClientModel>: showFrags=%s, showVehicleTypeIcon=%s, highlightElite=%s' % (
         self.showFrags, self.showVehicleTypeIcon, self.highlightElite)
