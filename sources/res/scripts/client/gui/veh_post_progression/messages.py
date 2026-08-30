from gui import SystemMessages
from gui.SystemMessages import SM_TYPE
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items.processors import makeSuccess, makeError
from gui.shared.notifications import NotificationPriorityLevel
from gui.veh_post_progression.formatters.ext_currency import formatExtendedCurrencyValue
from gui.shared.ext_money import ExtendedCurrency
from post_progression_common import ACTION_TYPES
_SPENT_MESSAGES = {(ExtendedCurrency.VEH_XP): (R.strings.system_messages.vehiclePostProgression.experienceSpent()), 
   (ExtendedCurrency.XP): (R.strings.system_messages.vehiclePostProgression.experienceSpent()), 
   (ExtendedCurrency.FREE_XP): (R.strings.system_messages.vehiclePostProgression.freeExperienceSpent()), 
   (ExtendedCurrency.CREDITS): (R.strings.system_messages.vehiclePostProgression.creditsSpent())}

def makeSpentString(price, ignoreCurrencies=()):
    result = []
    for currency, value in price.iteritems():
        if value and currency not in ignoreCurrencies:
            currencyR = _SPENT_MESSAGES.get(currency, R.invalid())
            if currencyR:
                result.append(backport.text(currencyR, value=formatExtendedCurrencyValue(currency, value)))

    return (b' ').join(result)


def makeUnlockFeatureMessage(featureName, vehicleUserName):
    msgKey = R.strings.system_messages.vehiclePostProgression.unlockFeature.dyn(featureName)
    if msgKey:
        return makeSuccess(backport.text(msgKey.body(), vehicle=vehicleUserName), msgType=SM_TYPE.InformationHeader, msgData={b'header': (backport.text(msgKey.title()))}, msgPriority=NotificationPriorityLevel.HIGH)
    else:
        return


def makeModificationErrorMsg():
    msgKey = R.strings.system_messages.vehiclePostProgression.modificationProcessorError
    return makeError(backport.text(msgKey.body()), msgType=SM_TYPE.ErrorHeader, msgData={b'header': (backport.text(msgKey.title()))}, msgPriority=NotificationPriorityLevel.HIGH)


def makeDiscardPairsMsg(vehicle, modifications):
    ctx = {b'vehicle': (vehicle.userName)}
    msgKey = R.strings.system_messages.vehiclePostProgression.discardPairModification
    modificationNames = [backport.text(mod.getLocNameRes()()) for mod in modifications]
    if len(modificationNames) > 1:
        msgBody = R.strings.system_messages.vehiclePostProgression.discardPairsModification.body()
        separator = backport.text(R.strings.system_messages.vehiclePostProgression.discardPairsModification.modifications.separator())
        ctx[b'modifications'] = separator.join(modificationNames)
    else:
        msgBody = msgKey.body()
        ctx[b'modification'] = modificationNames[0] if modificationNames else b''
    return makeSuccess(backport.text(msgBody, **ctx), msgType=SM_TYPE.InformationHeader, msgData={b'header': (backport.text(msgKey.title()))}, msgPriority=NotificationPriorityLevel.HIGH)


def makeAllPairsDiscardMsg(vehicleName):
    msgBody = R.strings.system_messages.vehiclePostProgression.discardAllPairsModification.body()
    msgTitle = R.strings.system_messages.vehiclePostProgression.discardPairModification.title()
    return makeSuccess(backport.text(msgBody, vehicle=vehicleName), msgType=SM_TYPE.InformationHeader, msgData={b'header': (backport.text(msgTitle))}, msgPriority=NotificationPriorityLevel.MEDIUM)


def makeBuyPairMsg(vehicle, stepID, modID):
    msgKey = R.strings.system_messages.vehiclePostProgression.buyPairModification
    mod = vehicle.postProgression.getStep(stepID).action.getModificationByID(modID)
    userMsg = backport.text(msgKey.body(), vehicle=vehicle.userName, modification=backport.text(mod.getLocNameRes()()))
    spentString = makeSpentString(mod.getPrice())
    return makeSuccess((b' ').join((userMsg, spentString)), SM_TYPE.BuyPostProgressionModForCredits)


def makePurchaseStepsMsg(vehicle, stepIDs, price):
    ctx = {b'vehicle': (vehicle.userName)}
    featureUnlockMsgs = []
    levels = []
    for stepID in stepIDs:
        step = vehicle.postProgression.getStep(stepID)
        if step.action.actionType != ACTION_TYPES.PAIR_MODIFICATION:
            levels.append(step.getLevel())
        if step.action.actionType == ACTION_TYPES.FEATURE:
            unlockMsg = makeUnlockFeatureMessage(step.action.getTechName(), vehicle.userName)
            if unlockMsg is not None:
                featureUnlockMsgs.append(unlockMsg)

    levels.sort()
    if len(levels) > 1:
        msgKey = R.strings.system_messages.vehiclePostProgression.researchSteps.body
        separator = backport.text(R.strings.system_messages.vehiclePostProgression.researchSteps.levels.separator())
        ctx[b'levels'] = separator.join(str(level) for level in levels)
    else:
        msgKey = R.strings.system_messages.vehiclePostProgression.researchStep.body
        ctx[b'level'] = str(levels[0]) if levels else b''
    userMsg = backport.text(msgKey(), **ctx)
    spentString = makeSpentString(price, ignoreCurrencies=(ExtendedCurrency.XP,))
    return makeSuccess((b' ').join((userMsg, spentString)), SM_TYPE.ResearchVehiclePostProgressionSteps, featureUnlockMsgs)


def _getSlotCategoryName(slot):
    categoryR = R.strings.tank_setup.categories.dyn(next(iter(slot.categories))) if slot.categories else R.invalid
    if categoryR:
        return backport.text(categoryR())
    return b''


def makeSetSlotCategoryMsg(vehicle, slot):
    msgKey = R.strings.system_messages.vehiclePostProgression.setSlotCategory
    if slot is not None:
        return makeSuccess(backport.text(msgKey.body(), vehicle=vehicle.userName, category=_getSlotCategoryName(slot)), msgType=SM_TYPE.InformationHeader, msgData={b'header': (backport.text(msgKey.title()))}, msgPriority=NotificationPriorityLevel.HIGH)
    else:
        return makeSuccess()


def makeChangeSlotCategoryMsg(vehicle, slot, price):
    msgKey = R.strings.system_messages.vehiclePostProgression.changeSlotCategory
    if slot is not None:
        userMsg = backport.text(msgKey.body(), vehicle=vehicle.userName, category=_getSlotCategoryName(slot))
        spentString = makeSpentString(price)
        return makeSuccess((b' ').join((userMsg, spentString)), msgType=SM_TYPE.ChangeSlotCategory)
    else:
        return makeSuccess()


def makeVehiclePostProgressionUnlockMsg(vehicle):
    msgKey = R.strings.system_messages.vehiclePostProgression.vehiclesUnlockPostProgression
    if vehicle.postProgressionAvailability(unlockOnly=True):
        return makeSuccess(backport.text(msgKey.single.body(), vehicle=vehicle.userName), msgType=SM_TYPE.InformationHeader, msgPriority=NotificationPriorityLevel.HIGH, msgData={b'header': (backport.text(msgKey.title()))})
    return makeSuccess()


def showWelcomeUnlockMsg():
    msgKey = R.strings.system_messages.vehiclePostProgression.vehiclesUnlockPostProgression
    SystemMessages.pushMessage(text=backport.text(msgKey.welcomeUnlock.body()), type=SM_TYPE.InformationHeader, priority=NotificationPriorityLevel.HIGH, messageData={b'header': (backport.text(msgKey.title()))})
    return
