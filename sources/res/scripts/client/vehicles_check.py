from __future__ import absolute_import, print_function
from items import vehicles
import Math, ResMgr
EPSILON = 0.001

def check(*vehicleNames):
    if not vehicleNames:
        for nationID in (0, 1):
            for vID in vehicles.g_list.getList(nationID).keys():
                _vehicleCheck(vehicles.g_cache.vehicle(nationID, vID))

    else:
        for name in vehicleNames:
            _vehicleCheck(vehicles.g_cache.vehicle(*vehicles.g_list.getIDsByName(name)))

    print(b'Test finished!')
    return


def _vehicleCheck(vehType):
    tank = vehType.name
    for state in (b'undamaged', b'destroyed', b'exploded'):
        for chassis in vehType.chassis:
            _parameterCheck(chassis.hullPosition, chassis.models[state], (b'Scene Root', b'Tank', b'V'), b'hullPosition', tank, chassis.name)

        for hull in vehType.hulls:
            _parameterCheck(hull.turretPositions[0], hull.models[state], (
             b'Scene Root', hull.turretHardPoints[0]), b'turretPosition', tank, b'hull')

        for turret in vehType.turrets[0]:
            _parameterCheck(turret.gunPosition, turret.models[state], (b'Scene Root', b'HP_gunJoint'), b'gunPosition', tank, turret.name)

    return


def _parameterCheck(pos, modelPath, nodes, parameter, tank, comp):
    modelSec = ResMgr.openSection(modelPath)
    if modelSec is None:
        print(b'Error loading ', modelPath)
        return
    else:
        visualFile = modelSec.readString(b'nodefullVisual') + b'.visual'
        sec = ResMgr.openSection(visualFile)
        if sec is None:
            print(b"Error: can't find visual %s" % visualFile)
            return
        translation = Math.Vector3()
        for node in nodes:
            sec = _findNodeSec(sec, node)
            if sec is None:
                print(b"Error: cant't find node %s in visual %s" % (node, visualFile))
                return
            translation += sec.readVector3(b'transform/row3')

        if (translation - pos).length > EPSILON:
            print(b'Error: %s parameter is incorrect\n   Model:\t %s\n   Tank:\t  %s\n   Component: %s\n   Note: it must be <%s>' % (
             parameter, modelPath, tank, comp, translation))
        return


def _findNodeSec(sec, nodeName):
    for nodeSec in sec.values():
        if nodeSec.readString(b'identifier') == nodeName:
            return nodeSec

    return
