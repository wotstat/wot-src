from __future__ import absolute_import
from debug_utils import LOG_DEBUG
from server_side_replay.gui.Scaleform import registerMainMenuEntries

def preInit():
    registerMainMenuEntries()
    return


def init():
    LOG_DEBUG(b'init', __name__)
    return


def start():
    return


def fini():
    return
