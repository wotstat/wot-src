class FilterSetupContext(object):

    def __init__(self, ctx=None, asset=None):
        self.ctx = ctx or {}
        self.asset = asset or b''
        self.asset = self.asset.format(**self.ctx)
        return


def getFilterSetupContexts(xpRateMultiplier):
    return {b'favorite': (FilterSetupContext(asset=b'favorite')), 
       b'elite': (FilterSetupContext(asset=b'elite_small_icon')), 
       b'premium': (FilterSetupContext(asset=b'prem_small_icon')), 
       b'igr': (FilterSetupContext(asset=b'premium_small')), 
       b'bonus': (FilterSetupContext(ctx={b'multiplier': xpRateMultiplier}, asset=b'bonus_x{multiplier}')), 
       b'battleRoyale': (FilterSetupContext(asset=b'battle_royale_toggle')), 
       b'rented': (FilterSetupContext(asset=b'marathon/time_icon')), 
       b'debut_boxes': (FilterSetupContext(asset=b'debut_boxes_filter'))}


def getFilterPopoverSetupContexts(xpRateMultiplier):
    return {b'favorite': (FilterSetupContext(asset=b'favorite_medium')), 
       b'elite': (FilterSetupContext(asset=b'elite_small_icon')), 
       b'premium': (FilterSetupContext(asset=b'prem_small_icon')), 
       b'igr': (FilterSetupContext(asset=b'premium_igr_small')), 
       b'bonus': (FilterSetupContext(ctx={b'multiplier': xpRateMultiplier}, asset=b'bonus_x')), 
       b'rented': (FilterSetupContext(asset=b'marathon/time_icon')), 
       b'event': (FilterSetupContext(asset=b'event_small_icon')), 
       b'isCommonProgression': (FilterSetupContext(asset=b'common_progression')), 
       b'crystals': (FilterSetupContext(asset=b'bons_small')), 
       b'clanRented': (FilterSetupContext(asset=b'clan_wars')), 
       b'ranked': (FilterSetupContext(asset=b'ranked')), 
       b'debut_boxes': (FilterSetupContext(asset=b'debut_boxes_small')), 
       b'paragons': (FilterSetupContext(asset=b'paragons_filter_btn')), 
       b'early_access': (FilterSetupContext(asset=b'early_access'))}
