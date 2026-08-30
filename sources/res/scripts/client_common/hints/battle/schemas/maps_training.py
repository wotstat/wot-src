from __future__ import absolute_import
import enum, typing
from dict2model import fields
from dict2model import validate
from hints_common.battle.schemas.base import HMCContextType, CommonHintPropsModel, CommonHintPropsSchema
from hints.battle.schemas.base import ClientHintSchema, ClientHintTextModel, ClientHintSoundModel, ClientHintTextSchema, ClientHintSoundSchema, ClientHintModel, validateHintTextKey, CHMVisualType, CHMLifecycleType, CHMHistoryType
from helpers import dependency, time_utils
from skeletons.account_helpers.settings_core import ISettingsCore
from account_helpers.settings_core.settings_constants import OnceOnlyHints
if typing.TYPE_CHECKING:
    from dict2model.extensions.battle_type import BattleTypeModel

@enum.unique
class HintType(str, enum.Enum):
    HINT = b'hint'
    GOAL = b'goal'
    TIMER_GREEN = b'timerGreen'
    TIMER_RED = b'timerRed'


class MTClientHintPropsModel(CommonHintPropsModel):
    __slots__ = (b'hintType',)

    def __init__(self, name, scope, component, unique, priority, battleTypes, hintType):
        super(MTClientHintPropsModel, self).__init__(name=name, scope=scope, component=component, unique=unique, priority=priority, battleTypes=battleTypes)
        self.hintType = hintType
        return

    def _reprArgs(self):
        return (b'{}, {}').format(super(MTClientHintPropsModel, self)._reprArgs(), (b'hintType={}').format(self.hintType))


class MTClientHintTextModel(ClientHintTextModel):
    __slots__ = (b'key2', b'_message2')

    def __init__(self, raw, key, template, highlight, key2):
        super(MTClientHintTextModel, self).__init__(raw=raw, key=key, template=template, highlight=highlight)
        self.key2 = key2
        self._message2 = self._createMessage(key=self.key2)
        return

    @property
    def message2(self):
        return self._message2

    def _reprArgs(self):
        return (b'{}, {}').format(super(MTClientHintTextModel, self)._reprArgs(), (b'key2={}, msg2={}').format(self.key2, self._message2))


class MTClientHintSoundModel(ClientHintSoundModel):
    __slots__ = (b'notifyNewbie',)

    def __init__(self, fx, notify, aliveOnly, notifyNewbie):
        super(MTClientHintSoundModel, self).__init__(fx=fx, notify=notify, aliveOnly=aliveOnly)
        self.notifyNewbie = notifyNewbie
        return

    def _createNotify(self):
        settingsCore = dependency.instance(ISettingsCore)
        if self.notifyNewbie and not settingsCore.serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.MAPS_TRAINING_NEWBIE_HINT, default=False):
            return self.notifyNewbie
        return self.notify

    def _reprArgs(self):
        return (b'{}, {}').format(super(MTClientHintSoundModel, self)._reprArgs(), (b'notifyNewbie={}').format(self.notifyNewbie))


class MTClientHintPropsSchema(CommonHintPropsSchema[MTClientHintPropsModel]):
    __slots__ = ()

    def __init__(self):
        super(MTClientHintPropsSchema, self).__init__(modelClass=MTClientHintPropsModel)
        self._fields[b'hintType'] = fields.StrEnum(enumClass=HintType, required=True)
        return


class MTClientHintTextSchema(ClientHintTextSchema[MTClientHintTextModel]):
    __slots__ = ()

    def __init__(self):
        super(MTClientHintTextSchema, self).__init__(checkUnknown=True, modelClass=MTClientHintTextModel)
        self._fields[b'key2'] = fields.String(required=False, default=b'', deserializedValidators=[
         validate.Length(minValue=1, maxValue=100), validateHintTextKey])
        return


class MTClientHintSoundSchema(ClientHintSoundSchema[MTClientHintSoundModel]):
    __slots__ = ()

    def __init__(self):
        super(MTClientHintSoundSchema, self).__init__(checkUnknown=True, modelClass=MTClientHintSoundModel)
        self._fields[b'notifyNewbie'] = fields.String(required=False, default=b'', deserializedValidators=validate.Length(minValue=1, maxValue=50))
        return


class MTClientHintModel(ClientHintModel[MTClientHintPropsModel, HMCContextType, MTClientHintTextModel, CHMVisualType, MTClientHintSoundModel, CHMLifecycleType, CHMHistoryType]):
    __slots__ = ()

    def _createVO(self, data):
        vo, param1, param2 = {}, data.get(b'param1'), data.get(b'param2')
        if self.text:
            if self.text.message:
                if self.props.hintType is HintType.GOAL and param1 and param2:
                    vo[b'message'] = self.text.message.format(count=param1, total=param2)
                elif self.props.hintType in (HintType.TIMER_RED, HintType.TIMER_GREEN) and param1:
                    minutes, seconds = divmod(int(param1), time_utils.ONE_MINUTE)
                    minutesStr, secondsStr = (b'{}').format(minutes), (b'{:02d}').format(seconds)
                    vo[b'message'] = self.text.message.format(minutes=minutesStr, seconds=secondsStr)
                else:
                    vo[b'message'] = self.text.message
            if self.text.message2:
                vo[b'message2'] = self.text.message2
        return vo


mtHintPropsSchema = MTClientHintPropsSchema()
mtHintTextSchema = MTClientHintTextSchema()
mtHintSoundSchema = MTClientHintSoundSchema()
hintSchema = ClientHintSchema[MTClientHintModel](propsSchema=mtHintPropsSchema, textSchema=mtHintTextSchema, soundSchema=mtHintSoundSchema, modelClass=MTClientHintModel)
