import BigWorld
from debug_utils import LOG_DEBUG, LOG_WARNING
import BattleReplay
from items import vehicles, ITEM_TYPES

class InBattleUpgradesAvatar(BigWorld.DynamicScriptComponent):

    def onEnterWorld(self, *args):
        return

    def onLeaveWorld(self, *args):
        return

    def vehicleUpgradeResponse(self, intCDs, reasons):
        player = self.entity

        def __vehicleUpgradeLogger(isSuccess, intCD, reason, moduleTxt):
            if isSuccess:
                LOG_DEBUG((b'{} intCD = {} successfully installed').format(moduleTxt, intCD))
            else:
                LOG_WARNING((b'Could not install {} intCD = {}. Reason - {}!').format(moduleTxt, intCD, reason))
            return

        for intCD, reason in zip(intCDs, reasons):
            __vehicleUpgradeLogger(reason == b'', intCD, reason, b'Main' if intCD is intCDs[0] else b'Additional')

        mainIntCDs = intCDs[0]
        mainSuccess = not reasons[0]
        if mainSuccess and ITEM_TYPES.vehicleGun in [vehicles.parseIntCompactDescr(intCD)[0] for intCD in intCDs]:
            self.__upgradeVehicleGun()
        if player.guiSessionProvider.dynamic.progression:
            if BattleReplay.g_replayCtrl.isPlaying:
                player.guiSessionProvider.dynamic.progression.vehicleUpgradeRequest(mainIntCDs)
            player.guiSessionProvider.dynamic.progression.vehicleUpgradeResponse(mainIntCDs, mainSuccess)
        return

    def __upgradeVehicleGun(self):
        player = self.entity
        if player.guiSessionProvider.shared.ammo:
            player.guiSessionProvider.shared.ammo.clear(leave=False)
        return

    def testAvatarMethod(self):
        LOG_DEBUG(b'testAvatarMethod')
        return
