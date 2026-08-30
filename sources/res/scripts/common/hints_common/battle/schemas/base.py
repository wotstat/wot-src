from __future__ import absolute_import
import logging, typing
from dict2model import exceptions, fields, models, schemas, validate
from dict2model.extensions.battle_type import BattleTypesModel, BattleTypesSchema
from hints_common.battle.schemas.const import DEFAULT_PRIORITY, DEFAULT_COMPONENT, DEFAULT_SCOPE, RESERVED_SCOPES, MAX_PRIORITY
from py2to3 import patched_typing
if typing.TYPE_CHECKING:
    from dict2model.extensions.battle_type import BattleTypeModel
    from dict2model.types import ValidatorsType
_logger = logging.getLogger(__name__)

class SchemaDependentModel(models.Model):
    __slots__ = ()

    def prepare(self, schema, **kwargs):
        try:
            return self._prepare(schema, **kwargs)
        except exceptions.ValidationError:
            raise
        except Exception as error:
            raise exceptions.ValidationError((b'Model preparation error: {}').format(error))

        return

    def _prepare(self, schema, **kwargs):
        return


class CommonHintPropsModel(BattleTypesModel):
    __slots__ = (b'name', b'scope', b'component', b'unique', b'priority', b'_uniqueName')

    def __init__(self, name, scope, component, unique, priority, battleTypes):
        super(CommonHintPropsModel, self).__init__(battleTypes)
        self.name = name
        self.scope = scope
        self.component = component
        self.unique = unique
        self.priority = priority
        self._uniqueName = (b'{}.{}').format(scope, name) if scope else name
        return

    @property
    def uniqueName(self):
        return self._uniqueName

    def _reprArgs(self):
        return (b'{}, name={}, component={}, unique={}, priority={}').format(super(CommonHintPropsModel, self)._reprArgs(), self.uniqueName, self.component, self.unique, self.priority)


class CommonHintContextModel(SchemaDependentModel):
    __slots__ = (b'_ctx',)

    def __init__(self, *args, **kwargs):
        super(CommonHintContextModel, self).__init__(*args, **kwargs)
        self._ctx = {}
        return

    def create(self, data):
        return dict(self._ctx)

    def _prepare(self, schema, **kwargs):
        self._ctx = schema.serialize(self, silent=False)
        return

    def _reprArgs(self):
        return (b'ctx={}').format(self._ctx)


HMCPropsType = typing.TypeVar(b'HMCPropsType', bound=CommonHintPropsModel)
HMCContextType = typing.TypeVar(b'HMCContextType', bound=CommonHintContextModel)

class CommonHintModel(SchemaDependentModel, patched_typing.Generic[HMCPropsType, HMCContextType]):
    __slots__ = (b'props', b'context')

    def __init__(self, props, context):
        super(CommonHintModel, self).__init__()
        self.props = props
        self.context = context
        return

    @property
    def uniqueName(self):
        return self.props.uniqueName

    def validate(self, arenaBonusType, gameplayName, *args, **kwargs):
        return self.props.isSuitableForBattleType(arenaBonusType, gameplayName)

    def _prepare(self, schema, **kwargs):
        if self.context:
            self.context.prepare(schema.contextSchema, **kwargs)
        return

    def _reprArgs(self):
        return (b'props={}, ctx={}').format(self.props, self.context)


HMCType = typing.TypeVar(b'HMCType', bound=CommonHintModel)

def validateCommonHintPropsModel(model):
    validate.ValidateIterable([validate.IterableOfUnique(b'arenaBonusType')])(model.battleTypes)
    return


class CommonHintPropsSchema(BattleTypesSchema[HMCPropsType]):
    __slots__ = ()

    def __init__(self, modelClass=CommonHintPropsModel, serializedValidators=None, deserializedValidators=None):
        super(CommonHintPropsSchema, self).__init__(fields={b'name': (fields.String(required=True, deserializedValidators=validate.Length(minValue=1, maxValue=50))), 
           b'scope': (fields.String(required=False, default=DEFAULT_SCOPE, deserializedValidators=[
                    validate.Length(minValue=1, maxValue=50),
                    validate.NoneOf(RESERVED_SCOPES)])), 
           b'priority': (fields.Integer(required=False, default=DEFAULT_PRIORITY, deserializedValidators=validate.Range(minValue=0, maxValue=MAX_PRIORITY))), 
           b'component': (fields.String(required=False, default=DEFAULT_COMPONENT, deserializedValidators=validate.Length(minValue=1, maxValue=50))), 
           b'unique': (fields.Boolean(required=False, default=False))}, checkUnknown=False, serializedValidators=serializedValidators, deserializedValidators=[
         validateCommonHintPropsModel] + validate.prepareValidators(deserializedValidators), modelClass=modelClass)
        return


commonHintPropsSchema = CommonHintPropsSchema()
commonHintContextSchema = schemas.Schema[CommonHintContextModel](fields={}, checkUnknown=False, modelClass=CommonHintContextModel)

class CommonHintSchema(schemas.Schema[HMCType]):
    __slots__ = (b'propsSchema', b'contextSchema')

    def __init__(self, modelClass=CommonHintModel, propsSchema=None, contextSchema=None, serializedValidators=None, deserializedValidators=None):
        self.propsSchema = propsSchema or commonHintPropsSchema
        self.contextSchema = contextSchema or commonHintContextSchema
        super(CommonHintSchema, self).__init__(fields={b'props': (fields.Nested(required=True, schema=self.propsSchema)), 
           b'context': (fields.Nested(required=False, schema=self.contextSchema, default=None))}, checkUnknown=False, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators, modelClass=modelClass)
        return
