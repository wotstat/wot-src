from bootcamp.Bootcamp import g_bootcamp
from gui import DialogsInterface
from gui.Scaleform.daapi.view import dialogs
from gui.techtree.unlock import UnlockItemConfirmator
from gui.impl import backport
from gui.impl.gen import R

class BCUnlockItemConfirmator(UnlockItemConfirmator):
    _dialogsInterfaceMethod = staticmethod(DialogsInterface.showBCConfirmationDialog)
    _BOOTCAM_LABELS_PATH = b'../maps/icons/bootcamp/lines'
    _VEHICLE_COMPONENTS_LABLES = {b'vehicleChassis': b'bcChassis.png', 
       b'vehicleTurret': b'bcTurret.png', b'vehicleGun': b'bcGun.png', 
       b'vehicleRadio': b'bcRadio.png', b'vehicleWheels': b'bcWheels.png', 
       b'vehicleEngine': b'bcEngine.png'}

    @staticmethod
    def getPath(itemTypeName):
        dataStr = b''
        if itemTypeName in BCUnlockItemConfirmator._VEHICLE_COMPONENTS_LABLES:
            dataStr = (b'/').join((BCUnlockItemConfirmator._BOOTCAM_LABELS_PATH,
             BCUnlockItemConfirmator._VEHICLE_COMPONENTS_LABLES[itemTypeName]))
        return dataStr

    def __getVehicleData(self, bcNationData, item):
        if item.intCD == bcNationData[b'vehicle_second']:
            userName = backport.text(R.strings.bootcamp.award.options.tankTitle()).format(title=item.userName)
            return {b'label': (backport.text(R.strings.bootcamp.message.unlock.vehicle.title()).format(userName)), 
               b'labelExecute': (backport.text(R.strings.bootcamp.message.unlock.vehicle.buttonLabel())), 
               b'icon': (bcNationData[b'vehicle_second_icon']), 
               b'costValue': (self._costCtx[b'xpCost']), 
               b'isBuy': False}
        return

    def __getVehicleComponentData(self, item):
        return {b'label': (backport.text(R.strings.bootcamp.message.unlock.module.title()).format(item.longUserName)), 
           b'labelExecute': (backport.text(R.strings.bootcamp.message.unlock.module.buttonLabel())), 
           b'icon': (BCUnlockItemConfirmator.getPath(item.itemTypeName)), 
           b'costValue': (self._costCtx[b'xpCost']), 
           b'isBuy': False}

    def _makeMeta(self):
        item = self.itemsCache.items.getItemByCD(self._unlockCtx.itemCD)
        bcNationData = g_bootcamp.getNationData()
        if item.intCD == bcNationData[b'vehicle_second']:
            dialogData = self.__getVehicleData(bcNationData, item)
        else:
            dialogData = self.__getVehicleComponentData(item)
        return dialogs.BCConfirmDialogMeta(dialogData)
