from __future__ import absolute_import
import logging, typing
from constants import IS_DEVELOPMENT, IS_VS_EDITOR
from dict2model import exceptions
from dict2model import fields
from dict2model import models
from dict2model import schemas
from dict2model import validate
from gui import makeHtmlString, g_htmlTemplates
from helpers import i18n, dependency
from hints.battle.schemas.const import HTML_TEMPLATE_PATH, MIN_SHOW_TIME_LOWER_LIMIT, MIN_SHOW_TIME_UPPER_LIMIT, DEFAULT_MIN_SHOW_TIME, DEFAULT_WAIT_TIME, DEFAULT_SHOW_TIME, DEFAULT_COOLDOWN_TIME
from hints_common.battle.schemas.base import CommonHintSchema, CommonHintModel, HMCPropsType, HMCContextType
from py2to3 import patched_typing
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from typing import Optional
    from dict2model.types import ValidatorsType
    from hints_common.battle.schemas.base import CommonHintPropsSchema
    from gui.battle_control.controllers.battle_hints.history import BattleHintsHistory
_logger = logging.getLogger(__name__)
_DEFAULT_DISPLAY_COUNT = 0

class ClientHintTextModel(models.Model):
    __slots__ = (b'raw', b'key', b'template', b'highlight', b'_message')

    def __init__(self, raw, key, template, highlight):
        super(ClientHintTextModel, self).__init__()
        self.raw = raw
        self.key = key
        self.template = template
        self.highlight = highlight
        self._message = self._createMessage(self.raw, self.key, self.template)
        return

    @property
    def message(self):
        return self._message

    @staticmethod
    def _createMessage(raw=b'', key=b'', template=b''):
        return raw or ((i18n.makeString(key) if key else b'') or (makeHtmlString(HTML_TEMPLATE_PATH, template) if template else b''))

    def _reprArgs(self):
        return (b'raw={}, key={}, template={}, highlight={}, msg={}').format(self.raw, self.key, self.template, self.highlight, self._message)


class ClientHintVisualModel(models.Model):
    __slots__ = (b'image',)

    def __init__(self, image):
        super(ClientHintVisualModel, self).__init__()
        self.image = image
        return

    def _reprArgs(self):
        return (b'image={}').format(self.image)


class ClientHintSoundModel(models.Model):
    __slots__ = (b'fx', b'notify', b'aliveOnly')

    def __init__(self, fx, notify, aliveOnly):
        super(ClientHintSoundModel, self).__init__()
        self.fx = fx
        self.notify = notify
        self.aliveOnly = aliveOnly
        return

    def createFx(self):
        try:
            return self._createFx()
        except Exception as error:
            _logger.error(b'Sound fx creation error: %s.', error)
            return b''

        return

    def createNotify(self):
        try:
            return self._createNotify()
        except Exception as error:
            _logger.error(b'Sound notify creation error: %s.', error)
            return b''

        return

    def createAliveOnly(self):
        try:
            return self._createAliveOnly()
        except Exception as error:
            _logger.error(b'Sound aliveOnly creation error: %s.', error)
            return False

        return

    def _createFx(self):
        return self.fx

    def _createNotify(self):
        return self.notify

    def _createAliveOnly(self):
        return self.aliveOnly

    def _reprArgs(self):
        return (b'fx={}, notify={}').format(self.fx, self.notify)


class ClientHintLifecycleModel(models.Model):
    __slots__ = (b'showTime', b'minShowTime', b'waitTime')

    def __init__(self, showTime, minShowTime, waitTime):
        super(ClientHintLifecycleModel, self).__init__()
        self.showTime = showTime
        self.minShowTime = minShowTime
        self.waitTime = waitTime
        return

    def _reprArgs(self):
        return (b'showTime={}, minShowTime={}, waitTime={}').format(self.showTime, self.minShowTime, self.waitTime)


class ClientHintHistoryModel(models.Model):
    __slots__ = (b'modifyPriority', b'cooldown', b'totalDisplayCount', b'perBattleCount')

    def __init__(self, modifyPriority, cooldown, totalDisplayCount, perBattleCount):
        super(ClientHintHistoryModel, self).__init__()
        self.modifyPriority = modifyPriority
        self.cooldown = cooldown
        self.totalDisplayCount = totalDisplayCount
        self.perBattleCount = perBattleCount
        return

    def _reprArgs(self):
        return (b'modifyPriority={}, cooldown={}, totalDisplayCount={}, perBattleCount={}').format(self.modifyPriority, self.cooldown, self.totalDisplayCount, self.perBattleCount)


CHMTextType = typing.TypeVar(b'CHMTextType', bound=ClientHintTextModel)
CHMVisualType = typing.TypeVar(b'CHMVisualType', bound=ClientHintVisualModel)
CHMSoundType = typing.TypeVar(b'CHMSoundType', bound=ClientHintSoundModel)
CHMLifecycleType = typing.TypeVar(b'CHMLifecycleType', bound=ClientHintLifecycleModel)
CHMHistoryType = typing.TypeVar(b'CHMHistoryType', bound=ClientHintHistoryModel)

class ClientHintModel(CommonHintModel[HMCPropsType, HMCContextType], patched_typing.Generic[HMCPropsType, HMCContextType, CHMTextType, CHMVisualType, CHMSoundType, CHMLifecycleType, CHMHistoryType]):
    __slots__ = (b'text', b'visual', b'sound', b'lifecycle', b'history')
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, props, context, text, visual, sound, lifecycle, history):
        super(ClientHintModel, self).__init__(props=props, context=context)
        self.text = text
        self.visual = visual
        self.sound = sound
        self.lifecycle = lifecycle
        self.history = history
        return

    def validate(self, *args, **kwargs):
        visitor = self._sessionProvider.arenaVisitor
        return super(ClientHintModel, self).validate(visitor.getArenaBonusType(), visitor.type.getGamePlayName(), *args, **kwargs)

    def canBeShown(self, historyStorage=None):
        if historyStorage is not None and self.history is not None:
            if self.history.totalDisplayCount:
                totalDisplayCount = historyStorage.getTotalDisplayCount(self.uniqueName)
                if totalDisplayCount >= self.history.totalDisplayCount:
                    _logger.debug(b'Can not show <%s>. Hint reached display limit.', self.uniqueName)
                    return False
            if self.history.perBattleCount:
                perBattleCount = historyStorage.getPerBattleCount(self.uniqueName)
                if perBattleCount >= self.history.perBattleCount:
                    _logger.debug(b'Can not show <%s>. Hint reached per battle count limit.', self.uniqueName)
                    return False
        return True

    def createVO(self, data=None):
        data = data or {}
        try:
            return self._createVO(data)
        except Exception as error:
            _logger.error(b'[%s] value object creation error: %s.', self.uniqueName, error)
            return {}

        return

    def _createVO(self, data):
        message = self._formatMessage(self.text.message, data) if self.text and self.text.message else b''
        messageHighlight = self.text.highlight if self.text else b''
        iconSource = self.visual.image if self.visual and self.visual.image else b''
        if not message and not iconSource:
            _logger.debug(b'[%s] missing visual.', self.uniqueName)
            return {}
        context = self.context.create(data) if self.context else {}
        return {b'message': message, 
           b'messageHighlight': messageHighlight, 
           b'iconSource': iconSource, 
           b'context': context}

    def _formatMessage(self, message, data):
        try:
            return message.format(**data)
        except KeyError:
            _logger.error(b'[%s]. Incorrect message format for: %s', self.uniqueName, str(data))

        return b''

    def _reprArgs(self):
        return (b'{}, {}').format(super(ClientHintModel, self)._reprArgs(), (b'text={}, visual={}, sound={}, lifecycle={}, history={}').format(self.text, self.visual, self.sound, self.lifecycle, self.history))


CHMType = typing.TypeVar(b'CHMType', bound=ClientHintModel)

def validateHintTextKey(key):
    if not i18n.isValidKey(key):
        raise exceptions.ValidationError(b'Wrong localization key format. Example: #feature:hints/fire.')
    return


def validateHintTextTemplate(key):
    templates = g_htmlTemplates[HTML_TEMPLATE_PATH]
    if not templates:
        raise exceptions.ValidationError((b'No templates by path: {}.').format(HTML_TEMPLATE_PATH))
    return


def validateHintTextModel(model):
    if not (IS_DEVELOPMENT or IS_VS_EDITOR) and model.raw:
        raise exceptions.ValidationError(b'Raw text disabled for production mode.')
    count = sum([1 for text in (model.raw, model.key, model.template) if text])
    if count <= 0:
        raise exceptions.ValidationError(b'Text not provided.')
    if count != 1:
        raise exceptions.ValidationError(b'More than one text source provided.')
    return


def validateLifecycleModel(model):
    if model.showTime and model.showTime < model.minShowTime:
        raise exceptions.ValidationError(b'ShowTime less than minShowTime.')
    return


def validateHintModel(model):
    if not model.text and not model.visual and not model.sound:
        raise exceptions.ValidationError(b'Provide text or visual or sound filed.')
    return


class ClientHintTextSchema(schemas.Schema[CHMTextType]):
    __slots__ = ()

    def __init__(self, modelClass=ClientHintTextModel, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        super(ClientHintTextSchema, self).__init__(fields={b'raw': (fields.String(required=False, default=b'', deserializedValidators=validate.Length(minValue=1, maxValue=500))), 
           b'key': (fields.String(required=False, default=b'', deserializedValidators=[
                  validate.Length(minValue=1, maxValue=100), validateHintTextKey])), 
           b'template': (fields.String(required=False, default=b'', deserializedValidators=[
                       validate.Length(minValue=1, maxValue=100), validateHintTextTemplate])), 
           b'highlight': (fields.String(required=False, default=b'', deserializedValidators=validate.Length(minValue=1, maxValue=100)))}, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=[
         validateHintTextModel] + validate.prepareValidators(deserializedValidators), modelClass=modelClass)
        return


class ClientHintVisualSchema(schemas.Schema[CHMVisualType]):
    __slots__ = ()

    def __init__(self, modelClass=ClientHintVisualModel, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        super(ClientHintVisualSchema, self).__init__(fields={b'image': (fields.String(required=False, default=b'', deserializedValidators=validate.Length(minValue=1, maxValue=100)))}, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators, modelClass=modelClass)
        return


class ClientHintSoundSchema(schemas.Schema[CHMSoundType]):
    __slots__ = ()

    def __init__(self, modelClass=ClientHintSoundModel, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        super(ClientHintSoundSchema, self).__init__(fields={b'fx': (fields.String(required=False, default=b'', deserializedValidators=validate.Length(minValue=1, maxValue=100))), 
           b'notify': (fields.String(required=False, default=b'', deserializedValidators=validate.Length(minValue=1, maxValue=100))), 
           b'aliveOnly': (fields.Boolean(default=False, required=False))}, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators, modelClass=modelClass)
        return


class ClientHintHistorySchema(schemas.Schema[CHMHistoryType]):
    __slots__ = ()

    def __init__(self, modelClass=ClientHintHistoryModel, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        super(ClientHintHistorySchema, self).__init__(fields={b'modifyPriority': (fields.Boolean(required=False, default=False)), 
           b'cooldown': (fields.Float(required=False, default=DEFAULT_COOLDOWN_TIME, deserializedValidators=validate.Range(minValue=0))), 
           b'totalDisplayCount': (fields.Integer(required=False, default=_DEFAULT_DISPLAY_COUNT, deserializedValidators=validate.Range(minValue=1))), 
           b'perBattleCount': (fields.Integer(required=False, default=_DEFAULT_DISPLAY_COUNT, deserializedValidators=validate.Range(minValue=1)))}, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators, modelClass=modelClass)
        return


clientHintTextSchema = ClientHintTextSchema()
clientHintVisualSchema = ClientHintVisualSchema()
clientHintSoundSchema = ClientHintSoundSchema()
clientHintHistorySchema = ClientHintHistorySchema()
clientHintLifecycleSchema = schemas.Schema[ClientHintLifecycleModel](fields={b'showTime': (fields.Float(required=False, default=DEFAULT_SHOW_TIME, deserializedValidators=validate.Range(minValue=0))), 
   b'minShowTime': (fields.Float(required=False, default=DEFAULT_MIN_SHOW_TIME, deserializedValidators=validate.Range(minValue=MIN_SHOW_TIME_LOWER_LIMIT, maxValue=MIN_SHOW_TIME_UPPER_LIMIT))), 
   b'waitTime': (fields.Float(required=False, default=DEFAULT_WAIT_TIME, deserializedValidators=validate.Range(minValue=0)))}, checkUnknown=True, deserializedValidators=validateLifecycleModel, modelClass=ClientHintLifecycleModel)

class ClientHintSchema(CommonHintSchema[CHMType]):
    __slots__ = (b'textSchema', b'visualSchema', b'soundSchema', b'historySchema')

    def __init__(self, modelClass=ClientHintModel, propsSchema=None, contextSchema=None, textSchema=None, visualSchema=None, soundSchema=None, historySchema=None, serializedValidators=None, deserializedValidators=None):
        super(ClientHintSchema, self).__init__(propsSchema=propsSchema, contextSchema=contextSchema, serializedValidators=serializedValidators, deserializedValidators=[
         validateHintModel] + validate.prepareValidators(deserializedValidators), modelClass=modelClass)
        self.textSchema = textSchema or clientHintTextSchema
        self.visualSchema = visualSchema or clientHintVisualSchema
        self.soundSchema = soundSchema or clientHintSoundSchema
        self.historySchema = historySchema or clientHintHistorySchema
        self._fields[b'text'] = fields.Nested(required=False, schema=self.textSchema, default=None)
        self._fields[b'visual'] = fields.Nested(required=False, schema=self.visualSchema, default=None)
        self._fields[b'sound'] = fields.Nested(required=False, schema=self.soundSchema, default=None)
        self._fields[b'lifecycle'] = fields.Nested(required=False, schema=clientHintLifecycleSchema, default=ClientHintLifecycleModel(showTime=DEFAULT_SHOW_TIME, minShowTime=DEFAULT_MIN_SHOW_TIME, waitTime=DEFAULT_WAIT_TIME))
        self._fields[b'history'] = fields.Nested(required=False, schema=self.historySchema, default=None)
        return


clientHintSchema = ClientHintSchema()
