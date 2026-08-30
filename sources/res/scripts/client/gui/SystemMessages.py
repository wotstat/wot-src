from __future__ import absolute_import
from collections import namedtuple
from enumerations import Enumeration
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages
ResultMsg = namedtuple(b'ResultMsg', b'success userMsg sysMsgType msgPriority msgData auxData')
SM_TYPE = Enumeration(b'System message type', [
 10, 
 11, 
 12, 
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22, 
 23, 
 24, 
 25, 
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32, 
 33, 
 34, 
 35, 
 36, 
 37, 
 38, 
 39, 
 40, 
 41, 
 42, 
 43, 
 44, 
 45, 
 46, 
 47, 
 48, 
 49, 
 50, 
 51, 
 52, 
 53, 
 54, 
 55, 
 56, 
 57, 
 58, 
 59, 
 60, 
 61, 
 62, 
 63, 
 64, 
 65, 
 66, 
 67, 
 68, 
 69, 
 70, 
 71, 
 72, 
 73, 
 74, 
 75, 
 76, 
 77, 
 78, 
 79, 
 80, 
 81, 
 82, 
 83, 
 84, 
 85, 
 86, 
 87, 
 88, 
 89, 
 90, 
 91, 
 92, 
 93, 
 94, 
 95, 
 96, 
 97, 
 98, 
 99, 
 100, 
 101, 
 102, 
 103, 
 104, 
 105, 
 106])
CURRENCY_TO_SM_TYPE = {(Currency.CREDITS): (SM_TYPE.PurchaseForCredits), 
   (Currency.GOLD): (SM_TYPE.PurchaseForGold), 
   (Currency.CRYSTAL): (SM_TYPE.PurchaseForCrystal), 
   (Currency.EVENT_COIN): (SM_TYPE.PurchaseForEventCoin), 
   (Currency.BPCOIN): (SM_TYPE.PurchaseForBpcoin), 
   (Currency.EQUIP_COIN): (SM_TYPE.PurchaseForEquipCoin)}
CURRENCY_TO_SM_TYPE_DISMANTLING = {(Currency.CREDITS): (SM_TYPE.DismantlingForCredits), 
   (Currency.GOLD): (SM_TYPE.DismantlingForGold), 
   (Currency.CRYSTAL): (SM_TYPE.DismantlingForCrystal), 
   (Currency.EVENT_COIN): (SM_TYPE.DismantlingForEventCoin), 
   (Currency.BPCOIN): (SM_TYPE.DismantlingForBpcoin), 
   (Currency.EQUIP_COIN): (SM_TYPE.DismantlingForEquipCoin)}

def _getSystemMessages():
    return dependency.instance(ISystemMessages)


def pushMessage(text, type=SM_TYPE.Information, priority=None, messageData=None, savedData=None):
    _getSystemMessages().pushMessage(text, type, priority, messageData=messageData, savedData=savedData)
    return


def pushMessagesFromResult(resultMsg):
    if resultMsg and resultMsg.userMsg:
        pushMessage(resultMsg.userMsg, type=resultMsg.sysMsgType, priority=resultMsg.msgPriority, messageData=resultMsg.msgData)
    if resultMsg and hasattr(resultMsg, b'auxData') and not isinstance(resultMsg.auxData, dict) and resultMsg.auxData:
        for m in resultMsg.auxData:
            pushMessage(m.userMsg, type=m.sysMsgType, priority=m.msgPriority, messageData=m.msgData)

    return


def pushI18nMessage(key, *args, **kwargs):
    _getSystemMessages().pushI18nMessage(key, *args, **kwargs)
    return
