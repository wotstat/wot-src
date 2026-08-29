from survey.gui.game_control.SurveyChannelHandler import SurveyChannelHandler
from gui.shared.system_factory import registerAwardControllerHandler

def preInit():
    registerAwardControllerHandler(SurveyChannelHandler)
    return


def init():
    return


def start():
    return


def fini():
    return
