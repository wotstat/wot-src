import time, BigWorld
from chat_shared import SYS_MESSAGE_TYPE
from gui.shared.gui_items.processors import Processor, makeSuccess
from gui.shared.gui_items.processors.plugins import StallPurchaseParamsValidator, StallStateValidator
from helpers import dependency, time_utils
from messenger import MessengerEntry
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from skeletons.gui.system_messages import ISystemMessages

class PurchaseStallProductProcessor(Processor):
    __systemMessages = dependency.descriptor(ISystemMessages)

    def __init__(self, productCode, count=1):
        super(PurchaseStallProductProcessor, self).__init__()
        self.__productCode = productCode
        self.__count = count
        self.addPlugins((
         StallStateValidator(),
         StallPurchaseParamsValidator(self.__productCode, self.__count)))
        return

    def _request(self, callback):
        BigWorld.player().stall.purchaseProduct(self.__productCode, self.__count, (lambda _, code, errStr, ext: self._response(code, callback, errStr, ctx=ext)))
        return

    def _successHandler(self, code, ctx=None):
        ctx = ctx or {}
        self.__sendCurrencyUpdate(ctx)
        self.__systemMessages.proto.serviceChannel.pushClientMessage(ctx, SCH_CLIENT_MSG_TYPE.STALL_RECEIPT)
        return makeSuccess(auxData=ctx)

    def __sendCurrencyUpdate(self, ctx):
        for currency, countDict in ctx.get(b'currencies', {}).iteritems():
            sysMsgData = {b'currency_name': currency, 
               b'amount_delta': (int(countDict.get(b'count'))), 
               b'date': (int(time_utils.getServerUTCTime())), 
               b'emitterID': None}
            action = {b'sentTime': (time.time()), 
               b'data': {b'type': (SYS_MESSAGE_TYPE.currencyUpdate.index()), 
                         b'data': sysMsgData}}
            MessengerEntry.g_instance.protos.BW.serviceChannel.onReceivePersonalSysMessage(action)

        return
