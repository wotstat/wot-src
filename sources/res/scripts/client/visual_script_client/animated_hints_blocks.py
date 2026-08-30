import BigWorld, aih_constants
from animated_hints.constants import HintType
from visual_script.block import Block, Meta
from visual_script.slot_types import SLOT_TYPE
from visual_script.misc import ASPECT, EDITOR_TYPE, errorVScript
from constants import IS_VS_EDITOR
if not IS_VS_EDITOR:
    from animated_hints.manager import HintManager

class AnimatedHintMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 6750207

    @classmethod
    def blockCategory(cls):
        return b'Hint'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/hint'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class InitAnimatedHint(Block, AnimatedHintMeta):

    def __init__(self, *args, **kwargs):
        super(InitAnimatedHint, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._onInit)
        self._typeId = self._makeDataInputSlot(b'typeId', SLOT_TYPE.STR, EDITOR_TYPE.ENUM_SELECTOR)
        self._typeId.setEditorData([t.name for t in HintType])
        self._text = self._makeDataInputSlot(b'text', SLOT_TYPE.STR)
        self._text.setDefaultValue(b'')
        self._voiceover = self._makeDataInputSlot(b'voiceover', SLOT_TYPE.STR)
        self._timeCooldownAfter = self._makeDataInputSlot(b'cooldownAfter', SLOT_TYPE.FLOAT)
        self._timeCompleteDuration = self._makeDataInputSlot(b'completeDuration', SLOT_TYPE.FLOAT)
        self._out = self._makeEventOutputSlot(b'out')
        self._id = self._makeDataOutputSlot(b'id', SLOT_TYPE.ID, None)
        return

    def _onInit(self):
        avatar = BigWorld.player()
        hintTypeId = HintType[self._typeId.getValue()]
        timeCompleted = self._timeCompleteDuration.getValue() if self._timeCompleteDuration.hasValue() else 1.0
        cooldownAfter = self._timeCooldownAfter.getValue() if self._timeCooldownAfter.hasValue() else 0.0
        message = self._text.getValue()
        voiceover = self._voiceover.getValue() if self._voiceover.hasValue() else None
        hintParam = (
         avatar, hintTypeId, timeCompleted, cooldownAfter,
         message, voiceover)
        hint = HintManager.instance().addHint(hintParam)
        hint.start()
        self._id.setValue(hint.id)
        self._out.call()
        return

    def validate(self):
        if not self._typeId.hasValue():
            return b'TypeId is required'
        return super(InitAnimatedHint, self).validate()


class ProcessAnimatedHint(Block, AnimatedHintMeta):

    def __init__(self, *args, **kwargs):
        super(ProcessAnimatedHint, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self.__execute)
        self._id = self._makeDataInputSlot(b'id', SLOT_TYPE.ID)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def validate(self):
        if not self._id.hasValue():
            return b'id value is required'
        return super(ProcessAnimatedHint, self).validate()

    def _processHint(self, hint):
        return

    def __execute(self):
        if not IS_VS_EDITOR:
            hintId = self._id.getValue()
            hint = HintManager.instance().getHint(hintId)
            if hint is not None:
                self._processHint(hint)
            else:
                errorVScript(self, b'Unknown hint id')
        self._out.call()
        return


class ShowAnimatedHint(ProcessAnimatedHint):

    def _processHint(self, hint):
        if not hint.isActive():
            hint.show()
        return


class HideAnimatedHint(ProcessAnimatedHint):

    def _processHint(self, hint):
        if hint.isActive():
            hint.hide()
        return


class CompleteAnimatedHint(ProcessAnimatedHint):

    def _processHint(self, hint):
        if not hint.isComplete():
            hint.complete()
        return


class IsAnimatedHintVisible(Block, AnimatedHintMeta):

    def __init__(self, *args, **kwargs):
        super(IsAnimatedHintVisible, self).__init__(*args, **kwargs)
        self._id = self._makeDataInputSlot(b'id', SLOT_TYPE.ID)
        self._visible = self._makeDataOutputSlot(b'visible', SLOT_TYPE.BOOL, self._isVisible)
        return

    def _isVisible(self):
        hintId = self._id.getValue()
        hint = HintManager.instance().getHint(hintId)
        if hint is not None:
            visible = hint.isActive()
            self._visible.setValue(visible)
        else:
            errorVScript(self, b'Unknown hint id')
        return


class HideAllAnimatedHints(Block, AnimatedHintMeta):

    def __init__(self, *args, **kwargs):
        super(HideAllAnimatedHints, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self.__onHide)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def __onHide(self):
        for hint in HintManager.instance().getHints().itervalues():
            if hint.isActive():
                hint.hide()

        self._out.call()
        return


class SetAnimatedHintPenetrationString(Block, AnimatedHintMeta):
    _SHOT_RESULT_TO_PIERCING_CHANCE_HINT = {(aih_constants.SHOT_RESULT.UNDEFINED): b'', 
       (aih_constants.SHOT_RESULT.NOT_PIERCED): b'low', 
       (aih_constants.SHOT_RESULT.LITTLE_PIERCED): b'medium', 
       (aih_constants.SHOT_RESULT.GREAT_PIERCED): b'high'}

    def __init__(self, *args, **kwargs):
        super(SetAnimatedHintPenetrationString, self).__init__(*args, **kwargs)
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
        return super(SetAnimatedHintPenetrationString, self).validate()

    def _execute(self):
        penetrationType = self._SHOT_RESULT_TO_PIERCING_CHANCE_HINT.get(self._penetration.getValue())
        if penetrationType is not None:
            HintManager.instance().setPenetration(penetrationType, self._isColorBlind.getValue())
        else:
            errorVScript(self, b'Unexpected crosshairPenetration given')
        self._out.call()
        return


def regBlocks(blockRegistrar):
    blockRegistrar.regBlock(InitAnimatedHint)
    blockRegistrar.regBlock(ShowAnimatedHint)
    blockRegistrar.regBlock(HideAnimatedHint)
    blockRegistrar.regBlock(CompleteAnimatedHint)
    blockRegistrar.regBlock(IsAnimatedHintVisible)
    blockRegistrar.regBlock(HideAllAnimatedHints)
    blockRegistrar.regBlock(SetAnimatedHintPenetrationString)
    return
