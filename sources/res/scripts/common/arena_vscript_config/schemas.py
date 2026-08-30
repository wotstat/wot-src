from __future__ import absolute_import
import typing
from constants import IS_CLIENT
from dict2model import fields, models, validate
from dict2model.extensions.battle_type import BattleTypesModel, BattleTypesSchema
from dict2model.schemas import Schema
from visual_script.misc import ASPECT
if typing.TYPE_CHECKING:
    from dict2model.extensions.battle_type import BattleTypeModel

def _getCurrentAspect():
    if IS_CLIENT:
        return ASPECT.CLIENT
    return ASPECT.SERVER


class VScriptParamModel(models.Model):
    __slots__ = (b'name', b'value')

    def __init__(self, name, value):
        super(VScriptParamModel, self).__init__()
        self.name = name
        self.value = value
        return

    def _reprArgs(self):
        return (b'name={}, value={}').format(self.name, self.value)


_vscriptParamSchema = Schema[VScriptParamModel](fields={b'name': (fields.NonEmptyString(required=True)), 
   b'value': (fields.UniCapList(fields.NonEmptyString(), required=True))}, modelClass=VScriptParamModel, checkUnknown=True)

class VScriptModel(models.Model):
    __slots__ = (b'name', b'planId', b'param')

    def __init__(self, name, planId, param):
        super(VScriptModel, self).__init__()
        self.name = name
        self.planId = planId
        self.param = param
        return

    def _reprArgs(self):
        return (b'name={}, param={}, planId={}').format(self.name, self.param, self.planId)


_vscriptSchema = Schema[VScriptModel](fields={b'name': (fields.NonEmptyString(required=True)), 
   b'planId': (fields.String(required=False, default=b'')), 
   b'param': (fields.UniCapList(_vscriptParamSchema, required=False, default=list))}, modelClass=VScriptModel, checkUnknown=True)

class AspectVScriptsModel(models.Model):
    __slots__ = (b'plan',)

    def __init__(self, plan):
        super(AspectVScriptsModel, self).__init__()
        self.plan = plan
        return

    def _reprArgs(self):
        return (b'plan={}').format(self.plan)


_aspectVScriptSchema = Schema[AspectVScriptsModel](fields={b'plan': (fields.UniCapList(_vscriptSchema, required=True))}, modelClass=AspectVScriptsModel, checkUnknown=True)

class ArenaVScriptsModel(BattleTypesModel):
    __slots__ = (b'client', b'server', b'_plans')

    def __init__(self, client, server, battleTypes):
        super(ArenaVScriptsModel, self).__init__(battleTypes)
        self.client = client
        self.server = server
        self._plans = {}
        self._preparePlansForLoader()
        return

    def getPlansForLoader(self, aspect):
        return self._plans.get(aspect, [])

    def _preparePlansForLoader(self):
        aspect = _getCurrentAspect()
        self._plans[aspect] = [{b'name': (vscript.name), b'params': {param.name: param.value[0] if len(param.value) == 1 else list(param.value) for param in vscript.param}, 
           b'plan_id': (vscript.planId)} for vscript in (self.client if aspect == ASPECT.CLIENT else self.server).plan]
        return

    def _reprArgs(self):
        return (b'{}, client={}, server={}').format(super(ArenaVScriptsModel, self)._reprArgs(), self.client, self.server)


def _validateAnyPlanGiven(model):
    if not model.server.plan and not model.client.plan:
        raise validate.ValidationError(b'At least one plan(client or server) must be defined.')
    return


def _defaultAspectVScriptModel():
    return AspectVScriptsModel([])


_arenaVScriptSchema = BattleTypesSchema[ArenaVScriptsModel](fields={b'client': (fields.Nested(_aspectVScriptSchema, required=False, default=_defaultAspectVScriptModel)), 
   b'server': (fields.Nested(_aspectVScriptSchema, required=False, default=_defaultAspectVScriptModel))}, modelClass=ArenaVScriptsModel, checkUnknown=True, deserializedValidators=_validateAnyPlanGiven)

class ConfigModel(models.Model):
    __slots__ = (b'visualScript',)

    def __init__(self, visualScript):
        super(ConfigModel, self).__init__()
        self.visualScript = visualScript
        return

    def getPlansForLoader(self, aspect, arenaBonusType, gameplayName):
        plans = []
        for vscript in self.visualScript:
            if vscript.isSuitableForBattleType(arenaBonusType, gameplayName):
                plans.extend(vscript.getPlansForLoader(aspect))

        return plans


configSchema = Schema[ConfigModel](fields={b'visualScript': (fields.UniCapList(_arenaVScriptSchema, required=False, default=list))}, modelClass=ConfigModel, checkUnknown=True)
