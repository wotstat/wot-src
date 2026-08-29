import sys, math, BigWorld, GUI, Keys, Math, ResMgr
from debug_utils import LOG_DEBUG, LOG_ERROR
import game_mode_emulator
g_lightGenModeEnabled = False
g_currentMoveRate = 0.5
g_gui = None
g_enableCameraInput = False
MOVE_SPEED_MAX = 200.0
MOVE_SPEED_POW = 2.0
MOVE_SPEED_ADJUST = 0.1
FOV_ADJUST = math.radians(10)
FOV_MIN = math.radians(10)
FOV_MAX = math.radians(160)
SCRIPT_ARG_NAME = b'lightingGen'
MOUSE_TOGGLE_KEYS = [
 Keys.KEY_ESCAPE, Keys.KEY_LEFTMOUSE]

class CameraTransform:
    matrix = Math.Matrix()

    def __init__(self, matrix):
        self.matrix = matrix
        return

    def apply(self):
        BigWorld.camera().set(self.matrix)
        return


PROFILE_CAMERA_TRANSFORMS_XML_NAME = b'scripts/profile_camera_transforms.xml'
g_cameraTransforms = list()
g_curCameraTransform = 0

def _clampCameraTransformIdx(val):
    global g_cameraTransforms
    val = max(0, val)
    val = min(len(g_cameraTransforms) - 1, val)
    return val


def _loadCameraTransforms():
    rootDS = ResMgr.openSection(PROFILE_CAMERA_TRANSFORMS_XML_NAME)
    if rootDS is not None and rootDS[b'cameras'] is not None:
        for c in rootDS[b'cameras'].values():
            c = CameraTransform(c.readMatrix(b'transform'))
            g_cameraTransforms.append(c)

    else:
        m = Math.Matrix()
        m.lookAt((41, 14, -337), (-0.2, -0.05, 0.97), (0, 1, 0))
        g_cameraTransforms.append(CameraTransform(m))
    return


def _setCameraTransform(idx):
    global g_curCameraTransform
    idx = _clampCameraTransformIdx(idx)
    g_cameraTransforms[idx].apply()
    g_curCameraTransform = idx
    return


def enabled():
    global g_lightGenModeEnabled
    return g_lightGenModeEnabled


def onStartup():
    try:
        LOG_DEBUG(str(sys.argv))
        idx = sys.argv.index(SCRIPT_ARG_NAME)
        manifestFilename = sys.argv[idx + 1]
        LOG_DEBUG(str(manifestFilename))
        spacePath = BigWorld.lightingGenLoadManifest(manifestFilename)
        LOG_DEBUG(str(spacePath))
        if not spacePath:
            LOG_ERROR(b'error reading manifest: %s' % manifestFilename)
            raise ValueError
        launch(spacePath)
        return True
    except ValueError:
        return False
    except IndexError:
        LOG_ERROR(b'lightGen mode: Expected lighting manifest file argument ' + b"after '%s' command line argument" % SCRIPT_ARG_NAME)
        return False

    return


def _clearGUI():
    global g_gui
    if g_gui is not None:
        GUI.delRoot(g_gui)
        g_gui = None
    return


def _displayGUI(text):
    global g_gui
    _clearGUI()
    g_gui = GUI.Text(text)
    g_gui.multiline = True
    g_gui.horizontalAnchor = GUI.Simple.eHAnchor.CENTER
    GUI.addRoot(g_gui)
    return


def _close():
    LOG_DEBUG(b'exiting client')
    BigWorld.quit()
    return


def _tick():
    workLeft = BigWorld.isLightingGenRunning()
    if workLeft:
        BigWorld.callback(0.2, _tick)
    else:
        LOG_DEBUG(b'finished lighting gen work!')
        LOG_DEBUG(b'shutting down lighting gen systems')
        BigWorld.lightingGenShutdown()
        BigWorld.callback(2.0, _close)
    return


def _startLightingGeneration():
    LOG_DEBUG(b'triggering lighting gen....')
    BigWorld.lightingGenStart()
    BigWorld.callback(5.0, _tick)
    return


def _offlineLoadCheck():
    if BigWorld.spaceLoadStatus() >= 1.0:
        BigWorld.worldDrawEnabled(True)
        BigWorld.uniprofSceneStart()
        _clearGUI()
        BigWorld.callback(1.0, _startLightingGeneration)
    else:
        BigWorld.callback(1.0, _offlineLoadCheck)
    return


def launch(spaceName):
    global g_lightGenModeEnabled
    print b'Entering offline space', spaceName
    BigWorld.clearAllSpaces()
    BigWorld.worldDrawEnabled(False)
    guitext = b'Client Lighting Generation Mode\n  entering: %s' % spaceName
    _displayGUI(guitext)
    spaceID = BigWorld.createSpace()
    visibilityMask = game_mode_emulator.gameModeVisibilityMask(spaceName)
    BigWorld.addSpaceGeometryMapping(spaceID, None, spaceName, visibilityMask)
    _loadCameraTransforms()
    camera = BigWorld.FreeCamera()
    camera.spaceID = spaceID
    BigWorld.camera(camera)
    _setCameraTransform(g_curCameraTransform)
    BigWorld.camera().fixed = False
    BigWorld.projection().fov = math.radians(75.0)
    BigWorld.setWatcher(b'Client Settings/Strafe Rate', 175.0)
    BigWorld.setWatcher(b'Client Settings/Camera Mass', 5.0)
    BigWorld.setCursor(GUI.mcursor())
    GUI.mcursor().visible = True
    GUI.mcursor().clipped = False
    g_lightGenModeEnabled = True
    BigWorld.callback(1.0, _offlineLoadCheck)
    game_mode_emulator.createFakeAvatar()
    return


def adjustSpeed(diff):
    global g_currentMoveRate
    g_currentMoveRate = max(0.1, g_currentMoveRate + diff)
    strafeRate = float(BigWorld.getWatcher(b'Client Settings/Strafe Rate'))
    strafeRate = 1.0 + math.pow(g_currentMoveRate, MOVE_SPEED_POW) * MOVE_SPEED_MAX
    BigWorld.setWatcher(b'Client Settings/Strafe Rate', strafeRate)
    return


def adjustFOV(diff):
    newFov = BigWorld.projection().fov + diff
    newFov = min(max(newFov, FOV_MIN), FOV_MAX)
    BigWorld.projection().rampFov(newFov, 0.1)
    return


def handleKeyEvent(event):
    if not g_lightGenModeEnabled or not BigWorld.camera():
        return False
    if g_enableCameraInput:
        BigWorld.camera().handleKeyEvent(event)
    if not event.isKeyDown():
        return False
    if event.key in MOUSE_TOGGLE_KEYS:
        GUI.mcursor().visible = not GUI.mcursor().visible
    elif event.key == Keys.KEY_ADD:
        adjustFOV(+FOV_ADJUST)
    elif event.key == Keys.KEY_NUMPADMINUS:
        adjustFOV(-FOV_ADJUST)
    elif event.key == Keys.KEY_F:
        newFixed = not BigWorld.camera().fixed
        BigWorld.camera().fixed = newFixed
        GUI.mcursor().visible = newFixed
        GUI.mcursor().clipped = not newFixed
    return True


def handleMouseEvent(event):
    if not g_lightGenModeEnabled or not BigWorld.camera():
        return False
    if GUI.mcursor().visible:
        return False
    if g_enableCameraInput:
        if event.dz > 0:
            adjustSpeed(+MOVE_SPEED_ADJUST)
        elif event.dz < 0:
            adjustSpeed(-MOVE_SPEED_ADJUST)
        return BigWorld.camera().handleMouseEvent(event)
    return False
