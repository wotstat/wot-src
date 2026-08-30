import BigWorld, LGC
from account_shared import getFairPlayViolationName
from adisp import adisp_process
from constants import ACCOUNT_KICK_REASONS
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.dialogs import I18nInfoDialogMeta, I18nConfirmDialogMeta, DisconnectMeta, CheckBoxDialogMeta, DemoAccountBootcampFailureMeta, DIALOG_BUTTON_ID
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.Scaleform.locale.EVENT import EVENT
from gui.impl.gen import R
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles
from gui.shared.formatters.time_formatters import getTillTimeByResource
from gui.shared.utils import decorators
from helpers import i18n
from messenger.formatters import TimeFormatter

class _DialogCallbackWrapper(object):

    def __init__(self, cb):
        Waiting.suspend(lockerID=id(self))
        self.__cb = cb
        return

    def __call__(self, result):
        Waiting.resume(lockerID=id(self))
        if self.__cb is not None:
            self.__cb(result)
        return


@decorators.adisp_async
def showDialog(meta, callback, parent=None):
    g_eventBus.handleEvent(events.ShowDialogEvent(meta, _DialogCallbackWrapper(callback), parent=parent))
    return


@decorators.adisp_async
def showBCConfirmationDialog(meta, callback):
    effectData = {b'messages': [
                   {b'messagePreset': b'BCMessageGreenUI', 
                      b'label': (meta.getLabel()), 
                      b'iconPath': (meta.getIcon()), 
                      b'labelExecute': (meta.getLabelExecute()), 
                      b'costValue': (meta.getCostValue()), 
                      b'isBuy': (meta.getIsBuy()), 
                      b'isTraining': (meta.getIsTraining()), 
                      b'message': (meta.getMessage())}], 
       b'voiceovers': [], b'callback': (_DialogCallbackWrapper(callback)), 
       b'submitID': b''}
    g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BOOTCAMP_MESSAGE_WINDOW), ctx=effectData), EVENT_BUS_SCOPE.LOBBY)
    return


@decorators.adisp_async
def showI18nInfoDialog(i18nKey, callback, meta=None):
    showDialog(I18nInfoDialogMeta(i18nKey, meta=meta), callback)
    return


@decorators.adisp_async
@adisp_process
def showDemoAccountBootcampFailureDialog(i18nKey, meta=None):
    result = yield showDialog(DemoAccountBootcampFailureMeta(i18nKey, meta=meta))
    if result == DIALOG_BUTTON_ID.HYPERLINK:
        LGC.requestCompleteAccount()
    BigWorld.quit()
    return


@decorators.adisp_async
def showI18nConfirmDialog(i18nKey, callback, ctx=None, meta=None, focusedID=None):
    showDialog(I18nConfirmDialogMeta(i18nKey, messageCtx=ctx, meta=meta, focusedID=focusedID), callback)
    return


@decorators.adisp_async
def showI18nCheckBoxDialog(i18nKey, callback, meta=None, focusedID=None):
    showDialog(CheckBoxDialogMeta(i18nKey, meta=meta, focusedID=focusedID), callback)
    return


__ifDisconnectDialogShown = False

def showDisconnect(reason=None, kickReasonType=ACCOUNT_KICK_REASONS.UNKNOWN, expiryTime=None):
    global __ifDisconnectDialogShown
    if __ifDisconnectDialogShown:
        return
    Waiting.close()

    def callback(_):
        global __ifDisconnectDialogShown
        __ifDisconnectDialogShown = False
        return

    if kickReasonType == ACCOUNT_KICK_REASONS.DEMO_ACCOUNT_BOOTCAMP_FAILURE:
        showDemoAccountBootcampFailureDialog(reason)
    else:
        __ifDisconnectDialogShown = True
        showDialog(DisconnectMeta(reason, kickReasonType, expiryTime), callback)
    return


def showPunishmentDialog(arenaType, arenaCreateTime, fairplayViolations, banDuration):
    from gui.Scaleform.daapi.view.dialogs import I18PunishmentDialogMeta
    from gui.Scaleform.daapi.view.lobby.comp7.dialogs.comp7_punishment_dialog_meta import Comp7PunishmentDialogMeta
    if arenaType.gameplayName == b'comp7':
        durationStr = getTillTimeByResource(banDuration, R.strings.comp7.alertMessage.timeLeft, removeLeadingZeros=True)
        styledDurationStr = text_styles.hightlight(durationStr)
        metaClass = Comp7PunishmentDialogMeta
        key = b'comp7/punishmentWindow'
        messageCtx = {b'banDuration': styledDurationStr}
    else:
        penaltyType = None
        violation = None
        if fairplayViolations[1] != 0:
            penaltyType = b'penalty'
            violation = fairplayViolations[1]
        elif fairplayViolations[0] != 0:
            penaltyType = b'warning'
            violation = fairplayViolations[0]
        violationName = getFairPlayViolationName(violation)
        msgID = (b'punishmentWindow/reason/{}').format(violationName)
        metaClass = I18PunishmentDialogMeta
        key = b'punishmentWindow'
        messageCtx = {b'penaltyType': penaltyType, 
           b'arenaName': (i18n.makeString(arenaType.name)), 
           b'time': (TimeFormatter.getActualMsgTimeStr(arenaCreateTime)), 
           b'reason': (i18n.makeString(_getLocalizationPunishmentString(msgID, violationName)))}
    showDialog(metaClass(key, None, messageCtx), (lambda *args: None))
    return


def _getLocalizationPunishmentString(msgID, violationName):
    if b'event' in violationName:
        res = EVENT.all(msgID)
    else:
        res = DIALOGS.all(msgID)
    return res
