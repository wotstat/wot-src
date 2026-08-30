from __future__ import absolute_import
from gui.battle_control.controllers.vse_hud_settings_ctrl.settings.base_models import TextClientModel

class CountdownClientModel(TextClientModel):
    __slots__ = (b'header', b'subheader', b'battleStartMessage')

    def __init__(self, header, subheader, battleStartMessage):
        super(CountdownClientModel, self).__init__()
        self.header = header
        self.subheader = subheader
        self.battleStartMessage = battleStartMessage
        return

    def getHeader(self):
        return self._getText(self.header)

    def getSubheader(self):
        return self._getText(self.subheader)

    def getBattleStartMessage(self):
        return self._getText(self.battleStartMessage)

    def __repr__(self):
        return b'<CountdownClientModel>: header=%s, subheader=%s, battleStartMessage=%s' % (
         self.header, self.subheader, self.battleStartMessage)
