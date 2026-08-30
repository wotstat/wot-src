from gui.prb_control.entities.base.listener import IPrbListener

class ILegacyIntroListener(IPrbListener):

    def onLegacyListReceived(self, prebattles):
        return

    def onLegacyRosterReceived(self, prebattleID, iterator):
        return


class ILegacyListener(ILegacyIntroListener):

    def onSettingUpdated(self, entity, settingName, settingValue):
        return

    def onPropertyUpdated(self, entity, propertyName, propertyValue):
        return

    def onTeamStatesReceived(self, entity, team1State, team2State):
        return

    def onPlayerAdded(self, entity, playerInfo):
        return

    def onPlayerRemoved(self, entity, playerInfo):
        return

    def onRostersChanged(self, entity, rosters, full):
        return

    def onPlayerTeamNumberChanged(self, entity, team):
        return

    def onPlayerRosterChanged(self, entity, actorInfo, playerInfo):
        return

    def onPlayerStateChanged(self, entity, roster, accountInfo):
        return
