from __future__ import absolute_import
import typing
from visual_script.block import Block, Meta, InitParam
from visual_script.misc import errorVScript, ASPECT, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE
if typing.TYPE_CHECKING:
    from score_reasons_common.manager import ScoreReasonsModelsManager
_BLOCK_ALL_SCOPE_FILTER = b'[all]'

def _getScoreReasonsChoices(modelsMgr):
    if not modelsMgr:
        return []
    choices = {scopeKey: [name.split(b'.')[-1] for name in sorted(uniqueNames)] for scopeKey, uniqueNames in modelsMgr.reasonsByScope.items()}
    allScope = [
     (
      _BLOCK_ALL_SCOPE_FILTER, sorted(modelsMgr.getAllUniqueNames()))]
    return allScope + [(scope, choices[scope]) for scope in sorted(choices)]


class ScoreReasonsMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16758465

    @classmethod
    def blockCategory(cls):
        return b'Score reasons'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/score_reason'


class BaseSelectScoreReason(Block, ScoreReasonsMeta):

    def __init__(self, *args, **kwargs):
        super(BaseSelectScoreReason, self).__init__(*args, **kwargs)
        selected, = self._getInitParams()
        if selected.startswith(_BLOCK_ALL_SCOPE_FILTER + b'.'):
            self._uniqueReason = selected[len(_BLOCK_ALL_SCOPE_FILTER) + 1:]
        else:
            self._uniqueReason = selected
        if not self._uniqueReason:
            errorVScript(self, b'No score reasons to select.')
            return
        else:
            self._name = self._makeDataOutputSlot(b'uniqueName', SLOT_TYPE.STR, None)
            self._name.setValue(self._uniqueReason)
            return

    def validate(self):
        modelsManager = self._getModelsManager(initialize=False)
        if not modelsManager:
            return b'No score reasons models manager initialized.'
        if not modelsManager.getScoreReasonModel(self._uniqueReason):
            return (b'Score reason [{}] does not exist.').format(self._uniqueReason)
        return super(BaseSelectScoreReason, self).validate()

    @classmethod
    def initParams(cls):
        return [
         InitParam(name=b'scope, reasonName', slotType=SLOT_TYPE.STR, defaultValue=b'', editorType=EDITOR_TYPE.COMPLEX_KEY_SELECTOR, editorData=_getScoreReasonsChoices(cls._getModelsManager(initialize=True)))]

    def captionText(self):
        return (b'Score reason: {}').format(self._uniqueReason)

    @classmethod
    def blockAspects(cls):
        return [
         ASPECT.CLIENT, ASPECT.SERVER]

    @classmethod
    def _getModelsManager(cls, initialize=False):
        raise NotImplementedError
        return
