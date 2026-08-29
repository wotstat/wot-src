from visual_script.block import Block
from visual_script.slot_types import SLOT_TYPE
from visual_script_client.sound_blocks import SoundMeta

class PlayVoiceover(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(PlayVoiceover, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._voiceover = self._makeDataInputSlot(b'voiceover', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot(b'out')
        self._finished = self._makeEventOutputSlot(b'finished')
        return

    def validate(self):
        if not self._voiceover.hasValue():
            return b'Voiceover value is required'
        return super(PlayVoiceover, self).validate()

    def _execute(self):
        if self._voiceover.hasValue():
            from helpers import dependency
            from story_mode.skeletons.voiceover_controller import IVoiceoverManager
            manager = dependency.instance(IVoiceoverManager)
            ctx = {b'onEnd': (self._finished.call)}
            if self._vehicle.hasValue():
                ctx[b'vehicleId'] = self._vehicle.getValue().id
            manager.playVoiceover(voiceoverId=self._voiceover.getValue(), ctx=ctx)
        self._out.call()
        return


class StopVoiceover(Block, SoundMeta):

    def __init__(self, *args, **kwargs):
        super(StopVoiceover, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        from helpers import dependency
        from story_mode.skeletons.voiceover_controller import IVoiceoverManager
        manager = dependency.instance(IVoiceoverManager)
        manager.stopVoiceover()
        self._out.call()
        return
