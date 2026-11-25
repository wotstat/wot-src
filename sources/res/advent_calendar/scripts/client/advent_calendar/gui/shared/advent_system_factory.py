from __future__ import absolute_import
from gui.shared.system_factory import CollectEventsManager
DOORS_AVAILABLE_LISTENER = 0
REWARD_WINDOW = 1
CALENDAR_WINDOW = 2
PURCHASE_DIALOG_VIEW = 3
QUEST_CALENDAR_FORMATTER = 4
__collectAdventEM = CollectEventsManager()

def registerDoorsAvailableListener(listener):

    def onCollect(ctx):
        ctx[b'doorsAvailableListener'] = listener
        return

    __collectAdventEM.addListener(DOORS_AVAILABLE_LISTENER, onCollect)
    return


def collectDoorsAvailableListener():
    return __collectAdventEM.handleEvent(DOORS_AVAILABLE_LISTENER, {}).get(b'doorsAvailableListener')


def registerRewardWindow(validator, viewType):

    def onCollect(ctx):
        ctx[b'rewardWindow'].extend([(validator, viewType)])
        return

    __collectAdventEM.addListener(REWARD_WINDOW, onCollect)
    return


def collectRewardWindow():
    return __collectAdventEM.handleEvent(REWARD_WINDOW, {b'rewardWindow': []})[b'rewardWindow']


def registerCalendarWindow(validator, windowCls):

    def onCollect(ctx):
        ctx[b'calendarWindow'].extend([(validator, windowCls)])
        return

    __collectAdventEM.addListener(CALENDAR_WINDOW, onCollect)
    return


def collectCalendarWindow():
    return __collectAdventEM.handleEvent(CALENDAR_WINDOW, {b'calendarWindow': []})[b'calendarWindow']


def registerPurchaseDialogView(validator, viewCls):

    def onCollect(ctx):
        ctx[b'purchaseDialogView'].extend([(validator, viewCls)])
        return

    __collectAdventEM.addListener(PURCHASE_DIALOG_VIEW, onCollect)
    return


def collectPurchaseDialogView():
    return __collectAdventEM.handleEvent(PURCHASE_DIALOG_VIEW, {b'purchaseDialogView': []})[b'purchaseDialogView']


def registerQuestRewardFormatter(formatter):

    def onCollect(ctx):
        ctx[b'formatter'] = formatter
        return

    __collectAdventEM.addListener(QUEST_CALENDAR_FORMATTER, onCollect)
    return


def collectQuestRewardFormatter():
    return __collectAdventEM.handleEvent(QUEST_CALENDAR_FORMATTER, ctx={}).get(b'formatter')
