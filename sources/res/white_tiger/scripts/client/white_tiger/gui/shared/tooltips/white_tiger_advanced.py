from __future__ import absolute_import
from gui.shared.tooltips.advanced import MODULE_MOVIES

def registerWTEquipmentTooltipMovies():
    MODULE_MOVIES.update({b'wt_largeMedkit': b'white_tiger|wt_consumablesFirstAid', 
       b'wt_largeRepairkit': b'white_tiger|wt_consumablesRepairKitBig'})
    return
