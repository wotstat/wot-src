from collections import namedtuple
import typing
RoleEquipmentState = namedtuple(b'RoleEquipmentState', (b'level', b'progress'))
StatusWithTimeInterval = namedtuple(b'StatusWithTimeInterval', (b'statusID', b'startTime', b'endTime'))
TimeInterval = namedtuple(b'TimeInterval', (b'startTime', b'endTime'))
StateWithTimeInterval = namedtuple(b'TimeInterval', (b'stateID', b'timeInterval', b'isSourceVehicle'))
VisualScriptEquipmentState = namedtuple(b'VisualScriptEquipmentState', (b'quantity', b'endTime', b'totalTime', b'prevStage', b'stage', b'locked'))
VisualScriptEquipmentPublicState = namedtuple(b'VisualScriptEquipmentPublicState', (b'stage',))
if typing.TYPE_CHECKING:
    from enum import Enum

def getRoleEquipmentState(fixedDict):
    state = RoleEquipmentState(level=fixedDict[b'level'], progress=fixedDict[b'progress'])
    return state


def getStatusWithTimeInterval(fixedDict, statusEnum=None):
    status = StatusWithTimeInterval(statusID=statusEnum(fixedDict[b'statusID']) if statusEnum is not None else fixedDict[b'statusID'], startTime=fixedDict[b'startTime'], endTime=fixedDict[b'endTime'])
    return status


def getTimeInterval(fixedDict):
    interval = TimeInterval(startTime=fixedDict[b'startTime'], endTime=fixedDict[b'endTime'])
    return interval


def getStateWithTimeInterval(fixedDict):
    state = StateWithTimeInterval(stateID=fixedDict[b'stateID'], timeInterval=getTimeInterval(fixedDict[b'timeInterval']), isSourceVehicle=fixedDict[b'isSourceVehicle'])
    return state


def getVisualScriptEquipmentState(fixedDict):
    state = VisualScriptEquipmentState(quantity=fixedDict[b'quantity'], endTime=fixedDict[b'endTime'], totalTime=fixedDict[b'totalTime'], prevStage=fixedDict[b'prevStage'], stage=fixedDict[b'stage'], locked=fixedDict[b'locked'])
    return state


def getVisualScriptEquipmentPublicState(fixedDict):
    state = VisualScriptEquipmentPublicState(stage=fixedDict[b'stage'])
    return state
