from __future__ import absolute_import
from gui.shared.tooltips.advanced import MODULE_MOVIES
from gui.Scaleform.daapi.settings.config import ADVANCED_COMPLEX_TOOLTIPS
from halloween.gui.impl.lobby.tank_setup.backports.tooltips import HW_CONSUMABLE_EMPTY_TOOLTIP

def registerHWEquipmentTooltipMovies():
    MODULE_MOVIES.update({b'hw_hpRepairAndCrewHeal': b'halloween|hw_hpRepairAndCrewHeal', 
       b'hw_teamRepairKit': b'halloween|hw_teamRepairKit', 
       b'hw_damageShield': b'halloween|hw_damageShield', 
       b'hw_fastReload': b'halloween|hw_fastReload', 
       b'hw_invisibility': b'halloween|hw_invisibility', 
       b'hw_aoeDamageInstantShot': b'halloween|hw_aoeDamageInstantShot', 
       b'hw_aoeStunInstantShot': b'halloween|hw_aoeStunInstantShot', 
       b'hw_aoeDrainEnemyHpInstantShot': b'halloween|hw_aoeDrainEnemyHpInstantShot'})
    ADVANCED_COMPLEX_TOOLTIPS.update({HW_CONSUMABLE_EMPTY_TOOLTIP: b'halloween|hw_equipment'})
    return
