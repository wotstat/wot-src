from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from tutorial.data.client_triggers import ClientTriggers
    from tutorial.gui import IGuiImpl
    from tutorial.core import Tutorial
    from typing import Optional, Dict
    ComponentID = str

class IGuiController(object):

    def init(self, guiProviders):
        raise NotImplementedError
        return

    def setup(self, isEnabled=False, path=b''):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    @property
    def lastHangarMenuButtonsOverride(self):
        raise NotImplementedError
        return

    @property
    def lastHeaderMenuButtonsOverride(self):
        raise NotImplementedError
        return

    @property
    def hangarHeaderEnabled(self):
        raise NotImplementedError
        return

    @property
    def lastBattleSelectorHintOverride(self):
        raise NotImplementedError
        return

    def setHintsWithClientTriggers(self, clientTriggers):
        raise NotImplementedError
        return

    def getViewTutorialID(self, name):
        raise NotImplementedError
        return

    def getFoundComponentsIDs(self):
        raise NotImplementedError
        return

    def setCriteria(self, name, value):
        raise NotImplementedError
        return

    def setViewCriteria(self, componentID, viewUniqueName):
        raise NotImplementedError
        return

    def setTriggers(self, componentID, triggers):
        raise NotImplementedError
        return

    def clearTriggers(self, componentID):
        raise NotImplementedError
        return

    def showInteractiveHint(self, componentID, content, triggers=None, silent=False):
        raise NotImplementedError
        return

    def closeInteractiveHint(self, componentID):
        raise NotImplementedError
        return

    def setComponentProps(self, componentID, props):
        raise NotImplementedError
        return

    def playComponentAnimation(self, componentID, animType):
        raise NotImplementedError
        return

    def stopComponentAnimation(self, componentID, animType):
        raise NotImplementedError
        return

    def showBootcampHint(self, componentID):
        raise NotImplementedError
        return

    def hideBootcampHint(self, componentID):
        raise NotImplementedError
        return

    def setupViewContextHints(self, viewTutorialID, hintsData, hintsArgs=None):
        raise NotImplementedError
        return

    def overrideHangarMenuButtons(self, buttonsList=None):
        raise NotImplementedError
        return

    def overrideHeaderMenuButtons(self, buttonsList=None):
        raise NotImplementedError
        return

    def setHangarHeaderEnabled(self, enabled):
        raise NotImplementedError
        return

    def overrideBattleSelectorHint(self, overrideType=None):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return


class ITutorialLoader(object):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    @property
    def tutorial(self):
        raise NotImplementedError
        return

    @property
    def tutorialID(self):
        raise NotImplementedError
        return

    @property
    def isRunning(self):
        raise NotImplementedError
        return

    @property
    def gui(self):
        raise NotImplementedError
        return

    def isTutorialStopped(self):
        raise NotImplementedError
        return

    def run(self, settingsID, state=None):
        raise NotImplementedError
        return

    def stop(self, restore=True):
        raise NotImplementedError
        return

    def stopTutorial(self):
        raise NotImplementedError
        return

    def refuse(self):
        raise NotImplementedError
        return
