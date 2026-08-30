from __future__ import absolute_import
from typing import TYPE_CHECKING
from collections import namedtuple
from items.artefacts import DynComponentsGroupEquipment
from items import _xml
from last_stand_common.ls_utils import formatVehicleInfoString
if TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor
LSEquipmentVariant = namedtuple(b'LSEquipmentVariant', (b'id', b'cooldownSeconds', b'durationSeconds', b'usageCost', b'equipmentItem', b'dynComponentsGroups'))

class LSEquipment(DynComponentsGroupEquipment):
    __slots__ = (b'equipmentItem', b'usageCost', b'variantIdFormat', b'variants', b'_fallbackVariant')

    def _readConfig(self, xmlCtx, scriptSection):
        super(LSEquipment, self)._readConfig(xmlCtx, scriptSection)
        section = scriptSection
        self.equipmentItem = _xml.readString(xmlCtx, section, b'equipmentItem') if section.has_key(b'equipmentItem') else None
        self.usageCost = _xml.readFloat(xmlCtx, section, b'usageCost')
        self.variantIdFormat = section.readString(b'variantIdFormat') if section.has_key(b'variantIdFormat') else None
        variants = _xml.getChildren(xmlCtx, section, b'variants', throwIfMissing=False)
        self.variants = {_xml.readString(xmlCtx, variant, b'id'): self._readVariant(xmlCtx, variant) for _, variant in variants}
        self._fallbackVariant = LSEquipmentVariant(id=b'', cooldownSeconds=self.cooldownSeconds, durationSeconds=self.durationSeconds, usageCost=self.usageCost, equipmentItem=self.equipmentItem, dynComponentsGroups=self.dynComponentsGroups)
        return

    @property
    def fallbackVariant(self):
        return self._fallbackVariant

    def getVariant(self, vehTypeDescr):
        if not self.variants or self.variantIdFormat is None:
            return self._fallbackVariant
        else:
            return self.variants.get(formatVehicleInfoString(self.variantIdFormat, vehTypeDescr), self._fallbackVariant)

    @staticmethod
    def _readVariant(xmlCtx, section):
        return LSEquipmentVariant(id=_xml.readString(xmlCtx, section, b'id'), cooldownSeconds=_xml.readFloat(xmlCtx, section, b'cooldownSeconds'), durationSeconds=_xml.readFloat(xmlCtx, section, b'durationSeconds'), usageCost=_xml.readFloat(xmlCtx, section, b'usageCost'), equipmentItem=_xml.readString(xmlCtx, section, b'equipmentItem') if section.has_key(b'equipmentItem') else None, dynComponentsGroups=frozenset(_xml.readString(xmlCtx, section, b'dynComponentsGroups').split()))
