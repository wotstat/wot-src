from __future__ import absolute_import
from gui.battle_results.components import base
from fort_rush.gui.battle_results import components as ex
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
EXAMPLE_TOTAL_VO_META = base.DictMeta({b'eventPoints': 0, 
   b'vehicleCommanderID': 0, 
   b'doubleTotalDamage': 0})
HB_TOTAL_RESULTS_BLOCK = base.StatsBlock(EXAMPLE_TOTAL_VO_META, b'victoryData')
HB_TOTAL_RESULTS_BLOCK.addNextComponent(ex.EventPointsItem(b'eventPoints', _RECORD.PERSONAL))
HB_TOTAL_RESULTS_BLOCK.addNextComponent(ex.VehicleCommanderIDItem(b'vehicleCommanderID', _RECORD.PERSONAL))
HB_TOTAL_RESULTS_BLOCK.addNextComponent(ex.VehicleDoubleDamage(b'doubleTotalDamage', _RECORD.PERSONAL))
