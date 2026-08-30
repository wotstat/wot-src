from __future__ import absolute_import
import typing
from gui.Scaleform.daapi.view.battle.pve_base.base.settings_model import BaseWidgetSettingsModel
from pve_battle_hud import SecondaryObjectiveState

class SecondaryObjectiveServerModel(BaseWidgetSettingsModel):
    __slots__ = (b'timer', b'finishTime', b'progress', b'params')

    def __init__(self, id, type, state, timer, finishTime, progress, params):
        super(SecondaryObjectiveServerModel, self).__init__(id, type, SecondaryObjectiveState(state))
        self.timer = timer
        self.finishTime = finishTime
        self.progress = progress
        self.params = params
        return

    def __repr__(self):
        return b'<SecondaryObjectiveServerModel>: id=%s, type=%s, state=%s, timer=%s, finishTime=%s, progress=%s, params=%s' % (
         self.id, self.type, self.state, self.timer, self.finishTime, self.progress, self.params)
