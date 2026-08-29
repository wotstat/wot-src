from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class HintApplyingTrigger(object):

    def __init__(self, hintId, logger, applyingCallback, *args, **kwargs):
        self._hintId = hintId
        self._logger = logger
        self._applyingCallback = applyingCallback
        self._args = args
        self._kwargs = kwargs
        return

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return


class RepairKitApplyingTrigger(HintApplyingTrigger):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def start(self):
        eqCtrl = self.__sessionProvider.shared.equipments
        if eqCtrl is not None:
            eqCtrl.onEquipmentUpdated += self.__onEquipmentUpdated
        return

    def stop(self):
        eqCtrl = self.__sessionProvider.shared.equipments
        if eqCtrl is not None:
            eqCtrl.onEquipmentUpdated -= self.__onEquipmentUpdated
        return

    def __onEquipmentUpdated(self, intCD, item):
        if b'repairkit' in item.getTags():
            self._applyingCallback(self._hintId, self._logger)
        return


class MedKitApplyingTrigger(HintApplyingTrigger):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def start(self):
        eqCtrl = self.__sessionProvider.shared.equipments
        if eqCtrl is not None:
            eqCtrl.onEquipmentUpdated += self.__onEquipmentUpdated
        return

    def stop(self):
        eqCtrl = self.__sessionProvider.shared.equipments
        if eqCtrl is not None:
            eqCtrl.onEquipmentUpdated -= self.__onEquipmentUpdated
        return

    def __onEquipmentUpdated(self, intCD, item):
        if b'medkit' in item.getTags():
            self._applyingCallback(self._hintId, self._logger)
        return
