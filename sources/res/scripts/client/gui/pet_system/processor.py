import logging, BigWorld
from gui.impl import backport
from gui import SystemMessages
from gui.impl.gen import R
from gui.shared.gui_items.processors import Processor
_logger = logging.getLogger(__name__)

class PetSystemProcessor(Processor):

    def _errorHandler(self, code, errStr=b'', ctx=None):
        res = super(PetSystemProcessor, self)._errorHandler(code, errStr, ctx)
        SystemMessages.pushMessage(backport.text(R.strings.pet_system.message.server_error()), type=SystemMessages.SM_TYPE.Error)
        return res


class PetEventOpenProcessor(PetSystemProcessor):

    def _request(self, callback):
        _logger.debug(b'Make server request to open event')
        BigWorld.player().petSystem.interactWithEvent((lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class SelectActivePetProcessor(PetSystemProcessor):

    def __init__(self, petID):
        super(SelectActivePetProcessor, self).__init__()
        self.__petID = petID
        return

    def _request(self, callback):
        _logger.debug(b'Make server request to select active pet')
        BigWorld.player().petSystem.selectActivePet(self.__petID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class SelectPetNameProcessor(PetSystemProcessor):

    def __init__(self, petID, petNameID):
        super(SelectPetNameProcessor, self).__init__()
        self.__petID = petID
        self.__petNameID = petNameID
        return

    def _request(self, callback):
        _logger.debug(b'Make server request to save pet name')
        BigWorld.player().petSystem.selectPetName(self.__petID, self.__petNameID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class SelectPetStateProcessor(PetSystemProcessor):

    def __init__(self, visibilityState):
        super(SelectPetStateProcessor, self).__init__()
        self.__visibilityState = visibilityState
        return

    def _request(self, callback):
        _logger.debug(b'Make server request to change pet state')
        BigWorld.player().petSystem.selectPetStateBehavior(self.__visibilityState, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class SelectPetActiveBonusProcessor(PetSystemProcessor):

    def __init__(self, bonusID):
        super(SelectPetActiveBonusProcessor, self).__init__()
        self.__bonusID = bonusID
        return

    def _request(self, callback):
        _logger.debug(b'Make server request to change pet active bonus')
        BigWorld.player().petSystem.selectActiveBonus(self.__bonusID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class FirstClickSynergyProcessor(PetSystemProcessor):

    def __init__(self, petID):
        super(FirstClickSynergyProcessor, self).__init__()
        self.__petID = petID
        return

    def _request(self, callback):
        _logger.debug(b'Make server request to add first click synergy points')
        BigWorld.player().petSystem.addFirstClickSynergy(self.__petID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return


class PetPurchaseProcessor(PetSystemProcessor):

    def __init__(self, petID):
        super(PetPurchaseProcessor, self).__init__()
        self.__petID = petID
        return

    def _request(self, callback):
        _logger.debug(b'Make server request to buy pet')
        BigWorld.player().petSystem.buyPet(self.__petID, (lambda code, errStr, ext: self._response(code, callback, ctx=ext, errStr=errStr)))
        return
