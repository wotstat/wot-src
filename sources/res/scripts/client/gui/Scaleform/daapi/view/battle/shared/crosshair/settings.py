import aih_constants
from gui.Scaleform.genConsts.ROOT_SWF_CONSTANTS import ROOT_SWF_CONSTANTS
CROSSHAIR_CONTAINER_SWF = b'battleCrosshairsApp.swf'
CROSSHAIR_ROOT_PATH = b'root.main'
CROSSHAIR_INIT_CALLBACK = ROOT_SWF_CONSTANTS.BATTLE_CROSSHAIRS_REGISTER_CALLBACK
CROSSHAIR_ITEM_PATH_FORMAT = b'_level0.' + CROSSHAIR_ROOT_PATH + b'.{}'
CROSSHAIR_RADIUS_MC_NAME = b'radiusMC'
SPG_GUN_MARKER_ELEMENTS_COUNT = aih_constants.SPG_GUN_MARKER_ELEMENTS_COUNT
SHOT_RESULT_TO_DEFAULT_COLOR = {(aih_constants.SHOT_RESULT.UNDEFINED): b'normal', 
   (aih_constants.SHOT_RESULT.NOT_PIERCED): b'red', 
   (aih_constants.SHOT_RESULT.LITTLE_PIERCED): b'orange', 
   (aih_constants.SHOT_RESULT.GREAT_PIERCED): b'green'}
SHOT_RESULT_TO_ALT_COLOR = {(aih_constants.SHOT_RESULT.UNDEFINED): b'normal', 
   (aih_constants.SHOT_RESULT.NOT_PIERCED): b'purple', 
   (aih_constants.SHOT_RESULT.LITTLE_PIERCED): b'yellow', 
   (aih_constants.SHOT_RESULT.GREAT_PIERCED): b'green'}
