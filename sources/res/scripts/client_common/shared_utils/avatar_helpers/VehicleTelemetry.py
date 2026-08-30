import cPickle, zlib, math, os.path, datetime, ResMgr
from debug_utils import LOG_WARNING, LOG_ERROR, LOG_CODEPOINT_WARNING
from constants import ENABLE_DEBUG_DYNAMICS_INFO
from physics_shared import G

class VehicleTelemetry(object):

    def __init__(self, avatar):
        self.avatar = avatar
        self.logName = None
        self.saveTextLog = False
        self.dynamicsLog = None
        self.dynamicsData = {}
        self.scenarioName = None
        self.recordStarted = False
        self.__physicsDebugInfoEnabled = ENABLE_DEBUG_DYNAMICS_INFO
        self.__physicsDebugInfo = None
        self.__completionFlag = None
        return

    physicsDebugInfo = property((lambda self: self.__physicsDebugInfo))

    def enableVehiclePhysicsTelemetry(self, enabled=None):
        if not self.avatar.inWorld:
            return
        else:
            shouldEnable = enabled if enabled is not None else not self.__physicsDebugInfoEnabled
            flag = 1 if shouldEnable else 0
            self.avatar.base.setDevelopmentFeature(0, b'toggle_vehicle_debug_info', flag, b'')
            self.__physicsDebugInfoEnabled = shouldEnable
            return

    try:
        DYNAMICS_LOG_DIR = ResMgr.appDirectory() + b'dynamics_log'
    except AttributeError:
        DYNAMICS_LOG_DIR = b'dynamics_log'

    def __checkDynLogDir(self):
        if not os.path.exists(VehicleTelemetry.DYNAMICS_LOG_DIR):
            LOG_WARNING(b'DYNAMICS_LOG_DIR not found, creating ...', VehicleTelemetry.DYNAMICS_LOG_DIR)
            os.mkdir(VehicleTelemetry.DYNAMICS_LOG_DIR)
        return

    NAME_DELIMITER = b'$'

    def __generateDynamicsLogName(self):
        vehicleName = self.avatar.getVehicleAttached().typeDescriptor.name
        vehicleName = vehicleName.replace(b':', VehicleTelemetry.NAME_DELIMITER)
        timestamp = datetime.datetime.now().strftime(b'%y%m%d%H%M%S')
        logName = VehicleTelemetry.NAME_DELIMITER.join((vehicleName, self.scenarioName, timestamp))
        return logName

    def recordVehicleDynamics(self, scenarioName, cmd, rapidModeSpeedup=1, saveTextLog=False):
        if not self.avatar.inWorld:
            LOG_WARNING(b'Avatar.base is not available yet on Avatar client')
            LOG_CODEPOINT_WARNING()
            return
        self.scenarioName = scenarioName
        self.saveTextLog = saveTextLog
        self.logName = self.__generateDynamicsLogName()
        cmd = cmd.strip()
        zippedArg = zlib.compress(cPickle.dumps((rapidModeSpeedup, cmd)), 9)
        self.__completionFlag = False
        self.avatar.base.setDevelopmentFeature(0, b'record_vehicle_dynamics', 0, zippedArg)
        return

    def isSimulationComplete(self):
        return self.__completionFlag

    def __openDynamicsLog(self, refTime, refDist):
        self.__checkDynLogDir()
        if self.dynamicsLog:
            self.__closeDynamicsLog()
        self.logPath = os.path.join(VehicleTelemetry.DYNAMICS_LOG_DIR, self.logName)
        self.refTime = refTime
        self.refDist = refDist
        if self.saveTextLog:
            self.dynamicsLog = open(self.logPath, b'w')
            self.__writeHeader()
        return

    HEADER_TEMPLATE = b'# vehicle : {}\n# engine  : {}\n# chassis : {}\n# scenario: {}\n#  time    distance    Vz      Vx        Az       Ax      X        Y       Z         w        wcc     yaw      pitch     roll     r   health\n'

    def __writeHeader(self):
        descr = self.avatar.getVehicleAttached().typeDescriptor
        header = VehicleTelemetry.HEADER_TEMPLATE.format(descr.name, descr.engine.name, descr.chassis.name, self.scenarioName)
        self.dynamicsLog.write(header)
        return

    def __closeDynamicsLog(self):
        if self.dynamicsLog:
            self.dynamicsLog.close()
            self.dynamicsLog = None
            os.rename(self.logPath, self.logPath + b'.log')
        if self.dynamicsData:
            dataFileName = (b'{}.pkl').format(self.logName)
            with open(os.path.join(VehicleTelemetry.DYNAMICS_LOG_DIR, dataFileName), b'wb') as dataFile:
                cPickle.dump(self.dynamicsData, dataFile, protocol=2)
        self.dynamicsData = {}
        self.refTime = None
        self.refDist = None
        self.recordStarted = False
        return

    def __onStop(self):
        self.__closeDynamicsLog()
        self.__completionFlag = True
        return

    LOG_LINE_TEMPLATE = (b' ').join((b'{t:8.3f} {dist:8.3f}', b'{Vz:8.3f} {Vx:8.3f}', b'{Az:8.3f} {Ax:8.3f}', b'{X:8.3f} {Y:8.3f} {Z:8.3f}', b'{w:8.3f} {wcc:8.3f}', b'{yaw:8.3f} {pitch:8.3f} {roll:8.3f}', b'{r:8.3f} {health:4d}', b'{ltr:8.3f} {rtr:8.3f}', b'{ltp:8.3f} {rtp:8.3f}', b'{lte:8.3f} {rte:8.3f}', b'{hle:8.3f}', b'{dhh:8.3f} {dlt:8.3f} {drt:8.3f}', b'{hdm:8.3f} {hrc:8.3f}', b'{lthp:8.3f} {rthp:8.3f}', b'{Vy:8.3f} {Ay:8.3f}', b'{ltslp:8.3f} {rtslp:8.3f}', b'{ltbf:8.3f} {rtbf:8.3f}', b'\n'))

    def __logDynamics(self, paramNamesMap, snapshots):
        namesMap = paramNamesMap

        def getSnapshotValue(snapshot, parameterName, default=0.0):
            if namesMap.has_key(parameterName):
                return snapshot[namesMap[parameterName]]
            return default

        snapshot = None
        for snapshot in snapshots:
            time = snapshot[namesMap[b'time']] - self.refTime
            if time < 0:
                print b'Nt:', snapshot[namesMap[b'time']], self.refTime
            dist = snapshot[namesMap[b'path']] - self.refDist
            velocity = snapshot[namesMap[b'vel']]
            acceleration = snapshot[namesMap[b'acc']]
            position = snapshot[namesMap[b'pos']]
            pitch = -math.degrees(snapshot[namesMap[b'dir']][1])
            roll = math.degrees(snapshot[namesMap[b'dir']][2])
            yaw = math.degrees(snapshot[namesMap[b'dir']][0])
            angularVelocity = math.degrees(snapshot[namesMap[b'wel']].y)
            angularAcceleration = math.degrees(snapshot[namesMap[b'wac']].y)
            binormal = (acceleration * velocity).length
            r = abs(velocity.length ** 3 / binormal) if abs(binormal) > 0 else 0
            r = min(500, r)
            velocity *= 3.6
            acceleration *= 1 / G
            data = {b't': time, 
               b'dist': dist, 
               b'Vz': (velocity.z), 
               b'Vx': (velocity.x), 
               b'Az': (acceleration.z), 
               b'Ax': (acceleration.x), 
               b'X': (position.x), 
               b'Y': (position.y), 
               b'Z': (position.z), 
               b'w': angularVelocity, 
               b'wcc': angularAcceleration, 
               b'yaw': yaw, 
               b'pitch': pitch, 
               b'roll': roll, 
               b'r': r, 
               b'health': (int(self.avatar.getVehicleAttached().health)), 
               b'ltr': (getSnapshotValue(snapshot, b'lTrackReaction')), 
               b'rtr': (getSnapshotValue(snapshot, b'rTrackReaction')), 
               b'ltp': (getSnapshotValue(snapshot, b'lTrackPressure')), 
               b'rtp': (getSnapshotValue(snapshot, b'rTrackPressure')), 
               b'lte': (getSnapshotValue(snapshot, b'lTrackEnergy')), 
               b'rte': (getSnapshotValue(snapshot, b'rTrackEnergy')), 
               b'hle': (getSnapshotValue(snapshot, b'hullEnergy')), 
               b'dhh': (getSnapshotValue(snapshot, b'dmg_hh')), 
               b'dlt': (getSnapshotValue(snapshot, b'dmg_lt')), 
               b'drt': (getSnapshotValue(snapshot, b'dmg_rt')), 
               b'lthp': (getSnapshotValue(snapshot, b'lthp')), 
               b'rthp': (getSnapshotValue(snapshot, b'rthp')), 
               b'hdm': (getSnapshotValue(snapshot, b'hull_dmgmp')), 
               b'hrc': (getSnapshotValue(snapshot, b'hull_react')), 
               b'Vy': (velocity.y), 
               b'Ay': (acceleration.y), 
               b'ltslp': (getSnapshotValue(snapshot, b'lTrackScrolling', default=-20.0)), 
               b'rtslp': (getSnapshotValue(snapshot, b'rTrackScrolling', default=-30.0)), 
               b'ltbf': (getSnapshotValue(snapshot, b'ltbf')), 
               b'rtbf': (getSnapshotValue(snapshot, b'rtbf'))}
            for key, value in data.iteritems():
                self.dynamicsData.setdefault(key, []).append(value)

            line = VehicleTelemetry.LOG_LINE_TEMPLATE.format(**data)
            if self.saveTextLog:
                self.dynamicsLog.write(line)
                self.dynamicsLog.flush()

        return

    def receivePhysicsDebugInfo(self, info, modifDict):
        infoDict = cPickle.loads(zlib.decompress(info))
        cmd = infoDict[b'cmd']
        if cmd == b'telemetry':
            nDict = {}
            for key, value in modifDict.iteritems():
                try:
                    index = infoDict[b'paramNamesMap'][key]
                    nDict[index] = value
                except Exception:
                    pass

            temp = []
            ind = 0
            for inValue in infoDict[b'snapshots'][0]:
                mValue = nDict.get(ind, None)
                if mValue is not None:
                    temp.append(mValue)
                else:
                    temp.append(inValue)
                ind += 1

            infoDict[b'snapshots'][0] = temp
            if self.recordStarted:
                self.__logDynamics(infoDict[b'paramNamesMap'], infoDict[b'snapshots'])
            self.__physicsDebugInfo = infoDict
        elif cmd == b'comment':
            if self.dynamicsLog:
                line = b'#%(text)s\n' % infoDict
                self.dynamicsLog.write(line)
        elif cmd == b'openLog':
            self.recordStarted = True
            self.__openDynamicsLog(infoDict[b'time'], infoDict[b'path'])
        elif cmd == b'closeLog':
            self.__closeDynamicsLog()
        elif cmd == b'stop':
            self.__onStop()
        else:
            LOG_ERROR(b'Invalid PhysicsDebugInfo has been received:', infoDict)
        return
