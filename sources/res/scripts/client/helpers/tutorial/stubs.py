from skeletons.tutorial import ITutorialLoader, IGuiController

class StubGuiController(IGuiController):

    @property
    def lastHangarMenuButtonsOverride(self):
        return

    @property
    def lastHeaderMenuButtonsOverride(self):
        return

    @property
    def hangarHeaderEnabled(self):
        return False

    @property
    def lastBattleSelectorHintOverride(self):
        return

    def getViewTutorialID(self, _):
        return

    def init(self, guiProviders):
        return

    def setup(self, isEnabled=False, path=b''):
        return

    def fini(self):
        return

    def setHintsWithClientTriggers(self, clientTriggers):
        return

    def getFoundComponentsIDs(self):
        return []

    def setCriteria(self, name, value):
        return

    def setViewCriteria(self, componentID, viewUniqueName):
        return

    def setTriggers(self, componentID, triggers):
        return

    def clearTriggers(self, componentID):
        return

    def showInteractiveHint(self, componentID, content, triggers=None, silent=False):
        return

    def closeInteractiveHint(self, componentID):
        return

    def setComponentProps(self, componentID, props):
        return

    def playComponentAnimation(self, componentID, animType):
        return

    def stopComponentAnimation(self, componentID, animType):
        return

    def showBootcampHint(self, componentID):
        return

    def hideBootcampHint(self, componentID):
        return

    def setupViewContextHints(self, viewTutorialID, hintsData, hintsArgs=None):
        return

    def overrideHangarMenuButtons(self, buttonsList=None):
        return

    def overrideHeaderMenuButtons(self, buttonsList=None):
        return

    def setHangarHeaderEnabled(self, enabled):
        return

    def overrideBattleSelectorHint(self, overrideType=None):
        return

    def clear(self):
        return


class StubTutorialLoader(ITutorialLoader):

    def __init__(self):
        super(StubTutorialLoader, self).__init__()
        self.__gui = StubGuiController()
        return

    @property
    def gui(self):
        return self.__gui

    @property
    def tutorial(self):
        return

    @property
    def tutorialID(self):
        return b''

    @property
    def isRunning(self):
        return False

    def isTutorialStopped(self):
        return False

    def init(self):
        return

    def fini(self):
        return

    def run(self, settingsID, state=None):
        return

    def stop(self, restore=True):
        return

    def stopTutorial(self):
        return

    def refuse(self):
        return
