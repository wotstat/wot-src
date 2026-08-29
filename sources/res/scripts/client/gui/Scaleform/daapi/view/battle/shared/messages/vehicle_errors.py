import typing
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor

class VehicleErrorMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(VehicleErrorMessages, self).__init__(b'VehicleErrorsPanel', b'vehicle_errors_panel.xml')
        self.__ignoreKeys = ()
        self._keyReplacers = {b'cantShootNoAmmo': (self.__noAmmoReplacer)}
        return

    @property
    def ignoreKeys(self):
        return self.__ignoreKeys

    @ignoreKeys.setter
    def ignoreKeys(self, keys):
        self.__ignoreKeys = keys
        return

    def __del__(self):
        LOG_DEBUG(b'VehicleErrorMessages panel is deleted')
        return

    def _addGameListeners(self):
        super(VehicleErrorMessages, self)._addGameListeners()
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey += self.__onShowVehicleErrorByKey
        return

    def _removeGameListeners(self):
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleErrorByKey -= self.__onShowVehicleErrorByKey
        super(VehicleErrorMessages, self)._removeGameListeners()
        return

    def __onShowVehicleErrorByKey(self, key, args=None, extra=None):
        if key not in self.__ignoreKeys:
            if key in self._keyReplacers:
                key = self._keyReplacers[key](key, args)
            self.showMessage(key, args, extra)
        return

    @staticmethod
    def __noAmmoReplacer(key, args):
        typeDescriptor = args[b'typeDescriptor']
        if typeDescriptor.isFlamethrower:
            key = b'cantShootNoFlameAmmo'
        return key
