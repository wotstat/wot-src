import aih_constants
from visual_script.misc import errorVScript
from visual_script.block import Block
from visual_script.dependency import dependencyImporter
from visual_script.slot_types import SLOT_TYPE
from visual_script_client.battle_hud_block import BattleHUDEventMeta
from constants import IS_EDITOR
if not IS_EDITOR:
    from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
observers, = dependencyImporter(b'story_mode.gui.app_loader.observers')

class ShowWinMessage(Block, BattleHUDEventMeta):

    def __init__(self, *args, **kwargs):
        super(ShowWinMessage, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._teamSlot = self._makeDataInputSlot(b'team', SLOT_TYPE.INT)
        self._reasonSlot = self._makeDataInputSlot(b'reason', SLOT_TYPE.E_FINISH_REASON)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        battlePage = observers.getStoryModeBattle()
        if battlePage is not None:
            battlePage.showWinMessage(self._teamSlot.getValue(), self._reasonSlot.getValue())
        self._out.call()
        return


class SetAnimatedHintPenetrationMessage(Block, BattleHUDEventMeta):
    _SHOT_RESULT_TO_PIERCING_CHANCE_HINT = {(aih_constants.SHOT_RESULT.EMPTY): b'', 
       (aih_constants.SHOT_RESULT.UNDEFINED): b'', 
       (aih_constants.SHOT_RESULT.NOT_PIERCED): b'low', 
       (aih_constants.SHOT_RESULT.LITTLE_PIERCED): b'medium', 
       (aih_constants.SHOT_RESULT.GREAT_PIERCED): b'high'}

    def __init__(self, *args, **kwargs):
        super(SetAnimatedHintPenetrationMessage, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._penetration = self._makeDataInputSlot(b'crosshairPenetration', SLOT_TYPE.INT)
        self._penetration.setEditorData([aih_constants.SHOT_RESULT.UNDEFINED, aih_constants.SHOT_RESULT.GREAT_PIERCED])
        self._isColorBlind = self._makeDataInputSlot(b'isColorBlind', SLOT_TYPE.BOOL)
        self._isColorBlind.setDefaultValue(False)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def validate(self):
        if not self._penetration.hasValue():
            return b'crosshairPenetration value is required'
        return super(SetAnimatedHintPenetrationMessage, self).validate()

    def _execute(self):
        penetrationType = self._SHOT_RESULT_TO_PIERCING_CHANCE_HINT.get(self._penetration.getValue())
        if penetrationType is not None:
            battlePage = observers.getStoryModeBattle()
            if battlePage:
                penetrationPanel = battlePage.getComponent(BATTLE_VIEW_ALIASES.PENETRATION_PANEL)
                if penetrationPanel:
                    penetrationPanel.setPenetration(penetrationType, self._isColorBlind.getValue())
        else:
            errorVScript(self, b'Unexpected crosshairPenetration given')
        self._out.call()
        return
