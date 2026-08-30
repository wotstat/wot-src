from __future__ import absolute_import
import typing
from collections import namedtuple
from itertools import chain
from gui.Scaleform.daapi.view.meta.BaseVehicleMechanicsWidgetMeta import BaseVehicleMechanicsWidgetMeta
from gui.shared.utils.key_mapping import getScaleformKey
from gui.veh_mechanics.battle.updaters.hotkey_updaters import IHotKeysView
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import IMechanicPassengerView
if typing.TYPE_CHECKING:
    from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeyCommand
HotKeyData = namedtuple(b'HotKeyData', [b'command', b'isLong'])

class VehicleMechanicWidget(BaseVehicleMechanicsWidgetMeta, IHotKeysView, IMechanicPassengerView):
    _HOT_KEY_MAP = {}

    def setCrosshairType(self, crosshairType):
        self.as_setCrosshairTypeS(crosshairType)
        return

    def setHotkeys(self, hotKeyCommands):
        self.as_setHotKeysS(tuple(chain.from_iterable([[{b'keyCode': (getScaleformKey(hotKeyCommand.key)), b'command': (data.command), b'isLong': (data.isLong)} for data in self._HOT_KEY_MAP.get(hotKeyCommand.command, ())] for hotKeyCommand in hotKeyCommands])))
        return

    def setVisibleForPassenger(self, visibleForPassenger):
        self.as_setVisibleS(visibleForPassenger)
        return
