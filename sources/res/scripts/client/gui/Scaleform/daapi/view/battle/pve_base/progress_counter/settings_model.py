from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.battle.pve_base.base.settings_model import BaseWidgetSettingsModel
from pve_battle_hud import ProgressCounterState

class ProgressCounterServerModel(BaseWidgetSettingsModel):
    __slots__ = (b'params',)

    def __init__(self, id, type, state, params):
        super(ProgressCounterServerModel, self).__init__(id, type, ProgressCounterState(state))
        self.params = params
        return

    def __repr__(self):
        return b'<ProgressCounterServerModel>: id=%s, type=%s, state=%s, params=%s' % (
         self.id, self.type, self.state, self.params)
