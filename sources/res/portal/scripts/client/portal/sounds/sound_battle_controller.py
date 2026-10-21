import BattleReplay, typing, WWISE
from gui.battle_control.controllers.sound_ctrls.common import SoundPlayersBattleController
from portal.sounds.sound_players import PortalGameFlowStateSoundPlayer, PortalVehicleStateSoundPlayer
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers import BattleSessionSetup
    from gui.battle_control.controllers.sound_ctrls.common import SoundPlayer

class PortalBattleSoundCtrl(SoundPlayersBattleController):

    def __init__(self, setup):
        super(PortalBattleSoundCtrl, self).__init__()
        return

    def startControl(self, *args):
        WWISE.activateRemapping(b'portal25')
        super(PortalBattleSoundCtrl, self).startControl()
        return

    def stopControl(self):
        WWISE.deactivateRemapping(b'portal25')
        super(PortalBattleSoundCtrl, self).stopControl()
        return

    def _initializeSoundPlayers(self):
        return (
         PortalGameFlowStateSoundPlayer(),
         PortalVehicleStateSoundPlayer())


class ReplayPortalBattleSoundCtrl(PortalBattleSoundCtrl):
    pass


def createPortalBattleSoundsController(setup):
    if BattleReplay.g_replayCtrl.isPlaying:
        return ReplayPortalBattleSoundCtrl(setup)
    return PortalBattleSoundCtrl(setup)
