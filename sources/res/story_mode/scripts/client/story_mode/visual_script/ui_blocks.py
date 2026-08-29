from visual_script.block import Block
from visual_script.dependency import dependencyImporter
from visual_script.slot_types import SLOT_TYPE
from visual_script_client.battle_hud_block import BattleHUDEventMeta
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
