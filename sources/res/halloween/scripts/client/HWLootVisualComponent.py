from __future__ import absolute_import
from HWBuffSequencesComponent import HWBuffSequencesComponent
from dyn_components_groups import groupComponent
from xml_config_specs import StrParam

@groupComponent(stateParam=StrParam(default=b'state'))
class HWLootVisualComponent(HWBuffSequencesComponent):

    def __init__(self, stateParam=b'state'):
        super(HWLootVisualComponent, self).__init__()
        self._stateParam = stateParam
        return

    def set_lootState(self, prev):
        self._onChangeLootState()
        return

    def _onAvatarReady(self):
        super(HWLootVisualComponent, self)._onAvatarReady()
        self._onChangeLootState()
        return

    def _onChangeLootState(self):
        for animator in self._animators:
            animator.setFloatParam(self._stateParam, self.lootState)

        return
