from __future__ import absolute_import
from enum import IntEnum
from pve_battle_hud import WidgetType

class BaseWidgetSettingsModel(object):
    __slots__ = (b'id', b'type', b'state')

    def __init__(self, id, type, state):
        super(BaseWidgetSettingsModel, self).__init__()
        self.id = id
        self.type = WidgetType(type)
        self.state = state
        return

    def setState(self, state):
        self.state = state
        return
