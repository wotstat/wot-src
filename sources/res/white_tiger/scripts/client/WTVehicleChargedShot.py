from WTPrefabActivator import WTPrefabActivator

class WTVehicleChargedShot(WTPrefabActivator):

    def set_isChargedShotActive(self, prev):
        self._updatePrefab()
        return

    def _isAbilityActive(self):
        return self.isChargedShotActive
