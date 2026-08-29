from constants import Configs
from gui.impl.lobby.tank_setup.dialogs.main_content.main_contents import NeedRepairMainContent
from gui.impl.lobby.tank_setup.dialogs.need_repair import NeedRepair
from helpers import dependency, server_settings
from skeletons.gui.lobby_context import ILobbyContext

class NeedRepairMainContentBattleRoyale(NeedRepairMainContent):

    def onLoading(self, *args, **kwargs):
        super(NeedRepairMainContentBattleRoyale, self).onLoading(*args, **kwargs)
        with self._viewModel.transaction() as model:
            model.setRepairPercentage(self._repairPercentage)
            model.setFreeAutoRepair(False)
        return


class NeedRepairBattleRoyale(NeedRepair):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def _initialize(self, *args, **kwargs):
        super(NeedRepairBattleRoyale, self)._initialize(*args, **kwargs)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged
        return

    def _finalize(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        super(NeedRepairBattleRoyale, self)._finalize()
        return

    @server_settings.serverSettingsChangeListener(Configs.BATTLE_ROYALE_CONFIG.value)
    def __onServerSettingsChanged(self, diff):
        if not diff[Configs.BATTLE_ROYALE_CONFIG.value].get(b'isEnabled', True):
            self._onCancel()
        return
