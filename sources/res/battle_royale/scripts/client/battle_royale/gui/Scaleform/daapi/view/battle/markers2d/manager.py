import plugins, BattleReplay
from gui.Scaleform.daapi.view.battle.shared.markers2d.manager import MarkersManager

class BattleRoyaleMarkersManager(MarkersManager):

    def _setupPlugins(self, arenaVisitor):
        setup = super(BattleRoyaleMarkersManager, self)._setupPlugins(arenaVisitor)
        setup[b'vehicles'] = plugins.BattleRoyaleVehicleMarkerPlugin
        setup[b'vehiclesTargets'] = plugins.BRVehicleMarkerTargetPlugin
        if BattleReplay.g_replayCtrl.isPlaying:
            setup[b'vehiclesTargets'] = plugins.BRVehicleMarkerTargetPluginReplayPlaying
        if BattleReplay.g_replayCtrl.isRecording:
            setup[b'vehiclesTargets'] = plugins.BRVehicleMarkerTargetPluginReplayRecording
        return setup
