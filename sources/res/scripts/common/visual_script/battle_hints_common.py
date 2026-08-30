from __future__ import absolute_import
import typing
from hints_common.battle.schemas.const import BLOCK_ALL_HINTS_SCOPE_FILTER
from visual_script.block import Block, Meta, InitParam
from visual_script.misc import errorVScript, ASPECT, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE
if typing.TYPE_CHECKING:
    from hints_common.battle.manager import CommonBattleHintsModelsManager

def _getHintsChoices(modelsMgr):
    if not modelsMgr:
        return []
    choices, allHintIds = {}, set()
    for hint in modelsMgr.getAll():
        choices.setdefault(hint.props.scope, []).append(hint.uniqueName)
        allHintIds.add(hint.uniqueName)

    allHintsScope = [(BLOCK_ALL_HINTS_SCOPE_FILTER, sorted(allHintIds))]
    return allHintsScope + [(scope, sorted(choices[scope])) for scope in sorted(choices)]


class HintsMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 4259648

    @classmethod
    def blockCategory(cls):
        return b'Battle hints'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/hint'


class BaseSelectHint(Block, HintsMeta):

    def __init__(self, *args, **kwargs):
        super(BaseSelectHint, self).__init__(*args, **kwargs)
        selected, = self._getInitParams()
        _, self._hintId = selected.split(b'.', 1)
        if not self._hintId:
            errorVScript(self, b'No hints to select.')
            return
        else:
            self._id = self._makeDataOutputSlot(b'id', SLOT_TYPE.STR, None)
            self._id.setValue(self._hintId)
            return

    def validate(self):
        modelsMgr = self._getModelsManager(initialize=False)
        if not modelsMgr:
            return b'No hints models manager initialized.'
        if not modelsMgr.get(self._hintId):
            return (b'Hint [{}] does not exist.').format(self._hintId)
        return super(BaseSelectHint, self).validate()

    @classmethod
    def initParams(cls):
        return [
         InitParam(name=b'scope, hintId', slotType=SLOT_TYPE.STR, defaultValue=b'', editorType=EDITOR_TYPE.COMPLEX_KEY_SELECTOR, editorData=_getHintsChoices(cls._getModelsManager(initialize=True)))]

    def captionText(self):
        return (b'Hint: {}').format(self._hintId)

    @classmethod
    def blockAspects(cls):
        return [
         ASPECT.CLIENT, ASPECT.SERVER]

    @classmethod
    def _getModelsManager(cls, initialize=False):
        raise NotImplementedError
        return


class BaseHintAction(Block, HintsMeta):

    def __init__(self, *args, **kwargs):
        super(BaseHintAction, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._hintId = self._makeDataInputSlot(b'hintId', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        hintId = self._hintId.getValue()
        for receiver in self._getReceivers():
            self._doAction(receiver, hintId)

        self._out.call()
        return

    def _getReceivers(self):
        raise NotImplementedError
        return

    def _doAction(self, receiver, hintId):
        raise NotImplementedError
        return


class HintActionParamsMixin(object):
    RESERVED = (b'hintId',)

    def __init__(self, *args, **kwargs):
        super(HintActionParamsMixin, self).__init__(*args, **kwargs)
        paramsString, = self._getInitParams()[-1:]
        params = self._prepareParams(paramsString)
        self._params = [(name, self._makeDataInputSlot(name, SLOT_TYPE.STR)) for name in params]
        return

    @classmethod
    def initParams(cls):
        param = InitParam(b'Parameters names separated by " ". Example: magic test', SLOT_TYPE.STR, b'')
        return super(HintActionParamsMixin, cls).initParams() + [param]

    def _prepareParams(self, paramsString):
        params = []
        for name in paramsString.split():
            if name in params:
                errorVScript(self, (b'Name <{}> already in use.').format(name))
                continue
            if name in self.RESERVED:
                errorVScript(self, (b'Name <{}> reserved and can be used in params.').format(name))
                continue
            params.append(name)

        return params

    def _getParams(self):
        return {name: slot.getValue() for name, slot in self._params}
