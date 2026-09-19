from __future__ import absolute_import
from dict2model import fields
from dict2model import schemas
from dict2model import validate
from hints_common.battle.schemas.base import CommonHintContextModel
from hints.battle.schemas.base import validateHintTextTemplate, ClientHintModel, ClientHintSchema, ClientHintTextModel, ClientHintTextSchema, CHMVisualType, CHMLifecycleType, HMCPropsType, CHMSoundType, CHMHistoryType

class HalloweenHintContextModel(CommonHintContextModel):
    __slots__ = (b'extraPadding', b'offsetY', b'isAdaptive')

    def __init__(self, extraPadding, offsetY, isAdaptive):
        super(HalloweenHintContextModel, self).__init__()
        self.extraPadding = extraPadding
        self.offsetY = offsetY
        self.isAdaptive = isAdaptive
        return


hintContextSchema = schemas.Schema[HalloweenHintContextModel](fields={b'extraPadding': (fields.Integer(default=0, required=False)), 
   b'offsetY': (fields.Integer(default=0, required=False)), 
   b'isAdaptive': (fields.Boolean(default=False, required=False))}, checkUnknown=True, modelClass=HalloweenHintContextModel)

class HalloweenHintTextModel(ClientHintTextModel):
    __slots__ = (b'templatePinnable', b'_messagePinnable')

    def __init__(self, raw, key, template, highlight, templatePinnable):
        super(HalloweenHintTextModel, self).__init__(raw=raw, key=key, template=template, highlight=highlight)
        self.templatePinnable = templatePinnable
        self._messagePinnable = self._createMessage(template=self.templatePinnable)
        return

    @property
    def messagePinnable(self):
        return self._messagePinnable

    def _reprArgs(self):
        return (b'{}, {}').format(super(HalloweenHintTextModel, self)._reprArgs(), (b'templatePinnable={}, messagePinnable={}').format(self.templatePinnable, self._messagePinnable))


class HalloweenHintTextSchema(ClientHintTextSchema[HalloweenHintTextModel]):
    __slots__ = ()

    def __init__(self):
        super(HalloweenHintTextSchema, self).__init__(checkUnknown=True, modelClass=HalloweenHintTextModel)
        self._fields[b'templatePinnable'] = fields.String(required=False, default=b'', deserializedValidators=[
         validate.Length(minValue=1, maxValue=100), validateHintTextTemplate])
        return


class HalloweenHintModel(ClientHintModel[HMCPropsType, HalloweenHintContextModel, HalloweenHintTextModel, CHMVisualType, CHMSoundType, CHMLifecycleType, CHMHistoryType]):
    __slots__ = ()

    def _createVO(self, data):
        vo = super(HalloweenHintModel, self)._createVO(data)
        if self.text and self.text.messagePinnable:
            vo[b'messagePinnable'] = self.text.messagePinnable
        return vo


hintTextSchema = HalloweenHintTextSchema()
hintSchema = ClientHintSchema[HalloweenHintModel](textSchema=hintTextSchema, contextSchema=hintContextSchema, modelClass=HalloweenHintModel)
