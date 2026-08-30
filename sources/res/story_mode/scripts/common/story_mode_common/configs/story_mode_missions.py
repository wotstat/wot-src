import typing
from base_schema_manager import GameParamsSchema
from dict2model import models, schemas, fields, validate, exceptions
from story_mode_common.story_mode_constants import FIRST_MISSION_ID

class VehicleModel(models.Model):
    __slots__ = (b'name', b'styleId')

    def __init__(self, name, styleId):
        super(VehicleModel, self).__init__()
        self.name = name
        self.styleId = styleId
        return

    def __repr__(self):
        return (b'<VehicleModel(name={}, styleId={})>').format(self.name, self.styleId)


class MissionModel(models.Model):
    __slots__ = (b'missionId', b'vehicle', b'geometry')

    def __init__(self, missionId, vehicle, geometry):
        super(MissionModel, self).__init__()
        self.missionId = missionId
        self.vehicle = vehicle
        self.geometry = geometry
        return

    def __repr__(self):
        return (b'<MissionModel(id={}, vehicle={}, geometry={})>').format(self.missionId, self.vehicle, self.geometry)


class MissionsModel(models.Model):
    __slots__ = (b'missions', b'onboardingLastMissionId')

    def __init__(self, missions, onboardingLastMissionId):
        super(MissionsModel, self).__init__()
        self.missions = missions
        self.onboardingLastMissionId = onboardingLastMissionId
        return

    def __repr__(self):
        return (b'<MissionsModel(missions={}, onboardingLastMissionId={})>').format(self.missions, self.onboardingLastMissionId)


def validateMissionIds(model):
    sequencesIds, idDuplicates = set(), set()
    nextMissionId = FIRST_MISSION_ID
    for mission in model.missions:
        if mission.missionId != nextMissionId:
            raise exceptions.ValidationError((b'Mission id={} has wrong order').format(mission.missionId))
        nextMissionId += 1
        if mission.missionId not in sequencesIds:
            sequencesIds.add(mission.missionId)
        else:
            idDuplicates.add(mission.missionId)

    if idDuplicates:
        raise exceptions.ValidationError((b'Mission id duplicates: {}').format(idDuplicates))
    return


def validateOnboardingLastMissionId(model):
    lastMissionId = model.missions[-1].missionId
    if lastMissionId < model.onboardingLastMissionId:
        raise exceptions.ValidationError((b'onboardingLastMissionId={} is grater than last mission id={}').format(model.onboardingLastMissionId, lastMissionId))
    return


vehicleSchema = schemas.Schema(fields={b'name': (fields.String(required=True, public=False, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   b'styleId': (fields.Integer(required=False, public=False, serializedValidators=validate.Range(minValue=0), deserializedValidators=validate.Range(minValue=0), default=0))}, modelClass=VehicleModel, checkUnknown=True)
missionSchema = schemas.Schema(fields={b'missionId': (fields.Integer(required=True, serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1))), 
   b'vehicle': (fields.Nested(schema=vehicleSchema, required=True, public=False)), 
   b'geometry': (fields.String(required=True, public=False, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1)))}, modelClass=MissionModel, checkUnknown=True)
missionsSchema = GameParamsSchema(gameParamsKey=b'story_mode_missions', fields={b'missions': (fields.UniCapList(fieldOrSchema=missionSchema, required=True, deserializedValidators=validate.Length(minValue=1))), 
   b'onboardingLastMissionId': (fields.Integer(required=True, serializedValidators=validate.Range(minValue=1), deserializedValidators=validate.Range(minValue=1)))}, modelClass=MissionsModel, checkUnknown=True, deserializedValidators=[
 validateMissionIds, validateOnboardingLastMissionId])
