import typing
from dyn_objects_cache import DynObjectsBase, createTerrainCircleSettings
from story_mode_common.story_mode_constants import RECON_ABILITY, DISTRACTION_ABILITY, SCC_AIRSTRIKE_ABILITY, SCC_AIRSTRIKE_ABILITY_HARD
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
DEFAULT = b'default'
EQUIPMENT_VISUALS = {SCC_AIRSTRIKE_ABILITY: b'SMSccAirstrikeAimingCircleVisual', 
   SCC_AIRSTRIKE_ABILITY_HARD: b'SMSccAirstrikeAimingCircleVisual', 
   RECON_ABILITY: b'ReconAimingCircleVisual', 
   DISTRACTION_ABILITY: b'DistractionAimingCircleVisual', 
   DEFAULT: b'AimingCircleRestrictionVisual'}

class StoryModeDynObjects(DynObjectsBase):

    def __init__(self):
        super(StoryModeDynObjects, self).__init__()
        self._circleSettings = {}
        return

    def init(self, dataSection):
        if not self._initialized:
            for name, visual in EQUIPMENT_VISUALS.iteritems():
                if dataSection.has_key(visual):
                    self._circleSettings[name] = createTerrainCircleSettings(dataSection[visual])

            super(StoryModeDynObjects, self).init(dataSection)
        return

    def destroy(self):
        self._circleSettings.clear()
        super(StoryModeDynObjects, self).destroy()
        return

    def getAimingCircleRestrictionEffect(self, equipment):
        settings = self._circleSettings.get(equipment.name)
        if settings:
            return settings
        return self._circleSettings.get(DEFAULT)
