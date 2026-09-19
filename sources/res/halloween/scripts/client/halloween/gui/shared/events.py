from __future__ import absolute_import
from gui.shared.event_bus import SharedEvent
from gui.shared.events import HasCtxEvent

class HWHangarEvent(SharedEvent):
    REFRESH = b'hwHangarEvent/refresh'


class HWBattleLootEvent(HasCtxEvent):
    VEH_CAPTURING_START = b'HWBattleLootEvent/VEH_CAPTURING_START'
    VEH_CAPTURING_CANCEL = b'HWBattleLootEvent/VEH_CAPTURING_CANCEL'
    APPEAR = b'HWBattleLootEvent/APPEAR'
    CAPTURED = b'HWBattleLootEvent/CAPTURED'
