from __future__ import absolute_import
from advent_calendar.gui.Scaleform import registerAdventCalendarScaleform
from advent_calendar.messenger import registerAdventCalendarTokenQuestsSubFormatters
from advent_calendar.notification import registerAdventNotifications
from advent_calendar.skeletons import registerAdventCalendarController

def preInit():
    registerAdventCalendarController()
    registerAdventCalendarScaleform()
    registerAdventCalendarTokenQuestsSubFormatters()
    registerAdventNotifications()
    return


def init():
    return


def start():
    return


def fini():
    return
