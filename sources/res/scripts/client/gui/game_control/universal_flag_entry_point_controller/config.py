import logging, operator, typing
from skeletons.gui.game_control import IUniversalFlagEntryPointController
from dict2model import fields, schemas
from dict2model.models import Model
from dict2model.exceptions import ValidationError
_logger = logging.getLogger(__name__)

class MissionsMarathonTarget(object):
    __slots__ = (b'marathonPrefix',)

    def __init__(self, marathonPrefix):
        self.marathonPrefix = marathonPrefix
        return


class FullScreenBrowserTarget(object):
    __slots__ = (b'url',)

    def __init__(self, url):
        self.url = url
        return


class ShopPageTarget(object):
    __slots__ = (b'relativeUrl',)

    def __init__(self, relativeUrl):
        self.relativeUrl = relativeUrl
        return


class TopSubBrowserTarget(object):
    __slots__ = (b'url',)

    def __init__(self, url):
        self.url = url
        return


class NopeTarget(object):
    __slots__ = tuple()


class TokenOperation(object):
    __slots__ = (b'_operationType', b'_expectedAmount')
    TOKEN_OPERATION_MAPPING = {b'less': (operator.lt), 
       b'greater': (operator.gt), 
       b'equal': (operator.eq), 
       b'lessOrEqual': (operator.le), 
       b'greaterOrEqual': (operator.ge)}

    def __init__(self, operationType, expectedAmount):
        self._operationType = operationType
        self._expectedAmount = expectedAmount
        return


class BaseProgressStateToken(TokenOperation):
    __slots__ = (b'_tokenName', b'_amount')

    def __init__(self, tokenName, operationType, expectedAmount):
        self._tokenName = tokenName
        self._amount = None
        super(BaseProgressStateToken, self).__init__(operationType=operationType, expectedAmount=expectedAmount)
        return

    def getAmount(self):
        return self._amount

    def update(self, tokens):
        raise NotImplementedError(b'BaseProgressStateToken.update() not implemented')
        return

    def checkCompareAmountWithExpected(self):
        return self.TOKEN_OPERATION_MAPPING[self._operationType](self._amount, self._expectedAmount)


class ProgressStateToken(BaseProgressStateToken):

    def __init__(self, tokenName, operationType, expectedAmount):
        super(ProgressStateToken, self).__init__(tokenName=tokenName, operationType=operationType, expectedAmount=expectedAmount)
        return

    def update(self, tokens):
        newAmount = 0
        token = tokens.getToken(self._tokenName)
        if token:
            newAmount = token[1]
        if self._amount == newAmount:
            return False
        self._amount = newAmount
        return True


class ProgressStateExpirationToken(BaseProgressStateToken):
    _slots__ = (b'__expiration',)

    def __init__(self, tokenName, operationType, expectedAmount):
        self.__expiration = None
        super(ProgressStateExpirationToken, self).__init__(tokenName=tokenName, operationType=operationType, expected_amount=expectedAmount)
        return

    def getExpiration(self):
        return self.__expiration

    def update(self, tokens):
        newAmount = 0
        newExpiration = None
        token = tokens.getToken(self._tokenName)
        if token:
            newExpiration = token[0]
            newAmount = token[1]
        if self._amount == newAmount and self.__expiration == newExpiration:
            return False
        else:
            self._amount = newAmount
            self.__expiration = newExpiration
            return True


class UniversalFlagTimer(Model):
    __slots__ = (b'time', b'iconType', b'text')

    def __init__(self, time=0, iconType=IUniversalFlagEntryPointController.TimerIconType.NONE, text=b''):
        super(UniversalFlagTimer, self).__init__()
        self.time = time
        self.iconType = iconType
        self.text = text
        return


class UniversalFlagState(Model):
    __slots__ = (b'startTime', b'finishTime', b'caption', b'description', b'background', b'timer', b'tooltipBackground', b'target', b'token')

    def __init__(self, startTime=0, finishTime=0, caption=b'', description=b'', background=None, tooltipBackground=b'', timer=None, target=None, token=None):
        super(UniversalFlagState, self).__init__()
        self.startTime = startTime
        self.finishTime = finishTime
        self.caption = caption
        self.description = description
        self.background = background if background else IUniversalFlagEntryPointController.FlagBackground()
        self.timer = timer if timer else UniversalFlagTimer()
        self.tooltipBackground = tooltipBackground
        self.target = target
        self.token = token
        return


class UniversalFlagConfig(Model):

    def __init__(self, isEnabled=False, isPaused=False, target=None, states=None, showTime=0, hideTime=0):
        super(UniversalFlagConfig, self).__init__()
        self.isEnabled = isEnabled
        self.isPaused = isPaused
        self.target = target
        self.states = states if states else []
        self.showTime = showTime
        self.hideTime = hideTime
        return


class _BackgroundField(fields.Field):

    def _deserialize(self, incoming, **kwargs):
        result = IUniversalFlagEntryPointController.FlagBackground()
        result.active = incoming[b'active']
        result.activeHover = incoming[b'activeHover']
        result.disabled = incoming[b'disabled']
        result.disabledHover = incoming[b'disabledHover']
        return result

    def _serialize(self, incoming, **kwargs):
        return {b'active': (incoming.active), 
           b'activeHover': (incoming.activeHover), 
           b'disabled': (incoming.disabled), 
           b'disabledHover': (incoming.disabledHover)}


class _TargetField(fields.Field):

    def _deserialize(self, incoming, **kwargs):
        if b'missionsMarathon' in incoming:
            return MissionsMarathonTarget(incoming[b'missionsMarathon'])
        if b'fullScreenBrowser' in incoming:
            return FullScreenBrowserTarget(incoming[b'fullScreenBrowser'])
        if b'shopPage' in incoming:
            return ShopPageTarget(incoming[b'shopPage'])
        if b'topSubBrowser' in incoming:
            return TopSubBrowserTarget(incoming[b'topSubBrowser'])
        if b'nope' in incoming:
            return NopeTarget()
        raise fields.ValidationError(b'Invalid flag entry point target config')
        return

    def _serialize(self, incoming, **kwargs):
        if isinstance(incoming, MissionsMarathonTarget):
            return {b'missionsMarathon': (incoming.marathonPrefix)}
        else:
            if isinstance(incoming, FullScreenBrowserTarget):
                return {b'fullScreenBrowser': (incoming.url)}
            if isinstance(incoming, ShopPageTarget):
                return {b'shopPage': (incoming.relativeUrl)}
            if isinstance(incoming, TopSubBrowserTarget):
                return {b'topSubBrowser': (incoming.url)}
            if isinstance(incoming, NopeTarget):
                return {b'nope': None}
            raise ValidationError(b'Wrong target type.')
            return


class _TokenField(fields.Field):

    def _deserialize(self, incoming, **kwargs):
        if b'progressStateToken' in incoming and b'operationType' in incoming:
            return ProgressStateToken(tokenName=incoming[b'progressStateToken'], operationType=incoming[b'operationType'], expectedAmount=incoming[b'expectedAmount'])
        if b'progressStateExpirationToken' in incoming and b'operationType' in incoming:
            return ProgressStateExpirationToken(tokenName=incoming[b'progressStateExpirationToken'], operationType=incoming[b'operationType'], expectedAmount=incoming[b'expectedAmount'])
        raise fields.ValidationError(b'Invalid flag entry point token config')
        return

    def _serialize(self, incoming, **kwargs):
        if isinstance(incoming, ProgressStateToken):
            return {b'progressStateTokenAmount': (incoming.getAmount())}
        if isinstance(incoming, ProgressStateExpirationToken):
            return {b'progressStateExpirationTokenAmount': (incoming.getAmount()), 
               b'progressStateExpirationTokenExpiration': (incoming.getExpiration())}
        raise ValidationError(b'Wrong token type.')
        return


universalFlagTimerSchema = schemas.Schema(fields={b'time': (fields.Integer(required=True)), 
   b'iconType': (fields.Enum(IUniversalFlagEntryPointController.TimerIconType, required=True)), 
   b'text': (fields.String(required=True))}, modelClass=UniversalFlagTimer, checkUnknown=True)
universalFlagStateSchema = schemas.Schema(fields={b'startTime': (fields.Integer(required=True)), 
   b'finishTime': (fields.Integer(required=True)), 
   b'background': (_BackgroundField(required=True)), 
   b'caption': (fields.String(required=True)), 
   b'description': (fields.String(required=True)), 
   b'tooltipBackground': (fields.String(required=True)), 
   b'timer': (fields.Nested(schema=universalFlagTimerSchema, required=True)), 
   b'target': (_TargetField(required=False)), 
   b'token': (_TokenField(required=False))}, modelClass=UniversalFlagState, checkUnknown=True)
universalFlagConfigSchema = schemas.Schema(fields={b'isEnabled': (fields.Boolean(required=True)), 
   b'isPaused': (fields.Boolean(required=True)), 
   b'target': (_TargetField(required=True)), 
   b'states': (fields.List(universalFlagStateSchema, required=True))}, modelClass=UniversalFlagConfig, checkUnknown=True)
