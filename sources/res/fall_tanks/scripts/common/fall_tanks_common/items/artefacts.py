from __future__ import absolute_import
import importlib
artefacts = importlib.import_module(b'items.artefacts')

class FallTanksAbilityDashEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'duration', b'cooldownSeconds')

    def _readConfig(self, xmlCtx, section):
        super(FallTanksAbilityDashEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return


class FallTanksAbilityShieldEquipment(artefacts.VisualScriptEquipment, object):
    __slots__ = (b'duration', b'cooldownSeconds')

    def _readConfig(self, xmlCtx, section):
        super(FallTanksAbilityShieldEquipment, self)._readConfig(xmlCtx, section)
        self.duration = section.readFloat(b'duration')
        self.cooldownSeconds = section.readFloat(b'cooldownSeconds')
        self._exportSlotsToVSE()
        return
