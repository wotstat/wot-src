from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.shared.tooltips.advanced import BaseAdvancedTooltip
from gui.shared.tooltips.advanced.data.default_alt_key_data import AltKeyData

class MoneyAndXpAdvanced(BaseAdvancedTooltip):
    _moviesOrDescriptions = {b'crystal': b'economyBonds', 
       b'credits': b'economyCredits', 
       b'gold': b'economyGold', 
       b'freeXP': b'economyConvertExp'}

    def _getTooltipData(self, *args, **kwargs):
        _type = args[0]
        swfName = self._moviesOrDescriptions[_type]
        header = TOOLTIPS.getHeaderBtnTitle(_type)
        description = self._moviesOrDescriptions[_type]
        return (AltKeyData(swfName=swfName, header=header, description=description),)
