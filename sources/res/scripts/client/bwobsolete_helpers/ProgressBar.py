from PyGUI import PyGUIBase
import BigWorld, GUI, ResMgr, FantasyDemo, Bloom
from functools import partial

class IProgressBar(PyGUIBase):
    factoryString = b'PyGUI.IProgressBar'

    def __init__(self, component):
        PyGUIBase.__init__(self, component)
        return

    def setMinMax(self, min, max):
        return

    def setProgress(self, value):
        return

    def reset(self, value):
        return

    def addMessage(self, str):
        return

    def appendMessage(self, str):
        return


class ProgressBar(IProgressBar):
    factoryString = b'PyGUI.ProgressBar'

    def __init__(self, component):
        self.min = 0.0
        self.max = 1.0
        self.msgs = []
        IProgressBar.__init__(self, component)
        return

    def setMinMax(self, min, max):
        self.min = min
        self.max = max
        return

    def setProgress(self, value):
        range = self.max - self.min
        value = self.min + value * range
        try:
            self.component.bar.clipper.value = value
        except ReferenceError:
            pass

        return

    def reset(self, value):
        self.component.bar.clipper.reset()
        return

    def addMessage(self, str):
        FantasyDemo.rds.console.script.addMsg(str, 0)
        return

    def appendMessage(self, str):
        FantasyDemo.rds.console.script.appendMsg(str, 0)
        return

    def onLoad(self, section):
        PyGUIBase.onLoad(self, section)
        FantasyDemo.initConsole()
        return

    def onBound(self):
        IProgressBar.onBound(self)
        return


class ChunkLoadingProgressBar(ProgressBar):
    factoryString = b'PyGUI.ChunkLoadingProgressBar'

    def __init__(self, component):
        ProgressBar.__init__(self, component)
        self.phase1Ratio = 1.0
        self.checkRate = 0.05
        self.timeout = 180
        self.last = 0.0
        self.started = False
        self.inPhase1 = True
        self.cancelled = False
        return

    def start(self, distance, callbackFn):
        if self.started:
            return
        self.started = True
        self.distance = distance
        self.last = 0.0
        self.callbackFn = callbackFn
        self.cancelled = False
        self.setProgress(0.0)
        self.component.bar.clipper.reset()
        self.progressCheck(BigWorld.time() + self.timeout)
        return

    def finish(self, timedOut=False):
        self.started = False
        if self.callbackFn and not self.cancelled:
            if timedOut:
                self.callbackFn(True)
            else:
                BigWorld.callback(self.component.bar.clipper.speed, partial(self.callbackFn, timedOut))
            self.callbackFn = None
        return

    def cancel(self):
        self.cancelled = True
        self.started = False
        return

    def progressCheck(self, endTime):
        timedOut = endTime < BigWorld.time()
        finished = timedOut
        if not finished:
            status = BigWorld.spaceLoadStatus(self.distance)
            finished = status > 0.95
        if finished:
            self.setProgress(1.0)
            self.finish(timedOut)
        elif status > self.last:
            self.setProgress(status)
            self.last = status
        BigWorld.callback(self.checkRate, (lambda : self.progressCheck(endTime)))
        return

    def onLoad(self, section):
        ProgressBar.onLoad(self, section)
        self.phase1Ratio = section.readFloat(b'phase1Ratio', self.phase1Ratio)
        self.checkRate = section.readFloat(b'checkRate', self.checkRate)
        self.timeout = section.readInt(b'timeout', self.timeout)
        if section.readBool(b'useDefaultLoadingScreen', True):
            self.replaceLoadingScreen(section)
        self.startPhase(1)
        self.active(True)
        return

    def replaceLoadingScreen(self, section):
        sect = ResMgr.openSection(b'resources.xml/system')
        self.component.textureName = sect.readString(b'loadingScreen')
        return

    def startPhase(self, num):
        if num == 1:
            self.setMinMax(0.0, self.phase1Ratio)
        else:
            self.setMinMax(self.phase1Ratio, 1.0)
        return


class TeleportProgressBar(ChunkLoadingProgressBar):
    factoryString = b'PyGUI.TeleportProgressBar'

    def __init__(self, component):
        ChunkLoadingProgressBar.__init__(self, component)
        return

    def replaceLoadingScreen(self, section):
        return

    def preTeleport(self, callbackFn):
        import PostProcessing
        effect = PostProcessing.blur()
        effect.name = b'Teleport Progress Bar'
        effect.phases[-1].renderTarget = BigWorld.RenderTarget(b'teleportGobo', -3, -3)
        effect.phases[-1].material.additionalAlpha = 1.0
        c = list(PostProcessing.chain())
        c.append(effect)
        PostProcessing.chain(c)
        self.component.secondaryTexture = effect.phases[-1].renderTarget.texture
        self.component.freeze = None
        self.component.fader.value = 1.0
        BigWorld.callback(self.component.fader.speed, (lambda : self.onBlurred(callbackFn)))
        return

    def postTeleport(self):
        self.component.freeze = None
        return

    def onBlurred(self, callbackFn):
        import PostProcessing
        c = list(PostProcessing.chain())
        ch = []
        for e in c:
            if e.name != b'Teleport Progress Bar':
                ch.append(e)

        PostProcessing.chain(ch)
        if callbackFn:
            callbackFn()
        return
