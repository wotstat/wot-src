import logging
from cosmic_event.settings import HINTS
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.view_components import ViewComponentsController
_logger = logging.getLogger(__name__)

class CosmicBattleHintsController(ViewComponentsController):

    def getControllerID(self):
        return BATTLE_CTRL_ID.BATTLE_HINTS

    def startControl(self, *args):
        return

    def stopControl(self):
        return

    def showHint(self, hintName, data=None):
        hint = self.__getHint(hintName)
        if hint:
            _logger.debug(b'Request battle hint hintName=%s', hintName)
            for component in self._viewComponents:
                component.showHint(hint, data)

        else:
            _logger.error(b'Failed to show hint name=%s', hintName)
        return

    def hideHint(self, hintName):
        hint = self.__getHint(hintName)
        if hint:
            for component in self._viewComponents:
                component.hideHint(hint)

        else:
            _logger.error(b'Failed to hide hint name=%s', hintName)
        return

    def setScanningVehicles(self, scanningVehicles):
        for component in self._viewComponents:
            component.setScanningVehicles(scanningVehicles)

        return

    def __getHint(self, hintName):
        hint = HINTS.get(hintName)
        if not hint:
            _logger.error(b'Unknown hint name=%s', hintName)
        return hint
