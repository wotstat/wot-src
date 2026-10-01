import typing
from gui.shared.tooltips.advanced.data.default_alt_key_data import DefaultAltKeyData
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.artefacts import Equipment

class EquipmentAltKeyData(DefaultAltKeyData):
    LEND_LEASE_OIL_EQUIPMENT = b'lendLeaseOil'
    QUALITY_OIL_EQUIPMENT = b'qualityOil'
    ENHANCED_OIL_KEY = b'enhancedOil'
    RATION_KEY = b'ration'

    @classmethod
    def _getDescriptionKey(cls, item, mechanicName):
        if mechanicName in (cls.LEND_LEASE_OIL_EQUIPMENT, cls.QUALITY_OIL_EQUIPMENT):
            return cls.ENHANCED_OIL_KEY
        if item.isStimulator:
            return cls.RATION_KEY
        return mechanicName

    @staticmethod
    def _getHeader(item, mechanicName):
        return item.shortUserName
