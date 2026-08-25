from __future__ import absolute_import
from future.moves import pickle
import Event
from constants import PREBATTLE_UPDATE, PREBATTLE_TEAM_STATE
from debug_utils import LOG_DEBUG_DEV

class ClientPrebattle(object):
    __onUpdate = {(PREBATTLE_UPDATE.ROSTER): b'_ClientPrebattle__onRosterReceived', 
       (PREBATTLE_UPDATE.PLAYER_ADDED): b'_ClientPrebattle__onPlayerAdded', 
       (PREBATTLE_UPDATE.PLAYER_REMOVED): b'_ClientPrebattle__onPlayerRemoved', 
       (PREBATTLE_UPDATE.PLAYER_STATE): b'_ClientPrebattle__onPlayerStateChanged', 
       (PREBATTLE_UPDATE.PLAYER_ROSTER): b'_ClientPrebattle__onPlayerRosterChanged', 
       (PREBATTLE_UPDATE.PLAYER_GROUP): b'_ClientPrebattle__onPlayerGroupChanged', 
       (PREBATTLE_UPDATE.TEAM_STATES): b'_ClientPrebattle__onTeamStatesReceived', 
       (PREBATTLE_UPDATE.SETTINGS): b'_ClientPrebattle__onSettingsReceived', 
       (PREBATTLE_UPDATE.SETTING): b'_ClientPrebattle__onSettingUpdated', 
       (PREBATTLE_UPDATE.KICKED_FROM_QUEUE): b'_ClientPrebattle__onKickedFromQueue', 
       (PREBATTLE_UPDATE.PROPERTIES): b'_ClientPrebattle__onPropertiesReceived', 
       (PREBATTLE_UPDATE.PROPERTY): b'_ClientPrebattle__onPropertyUpdated'}

    def __init__(self, prebattleID):
        self.id = prebattleID
        self.settings = None
        self.properties = None
        self.rosters = {}
        self.teamStates = [
         None, PREBATTLE_TEAM_STATE.NOT_READY, PREBATTLE_TEAM_STATE.NOT_READY]
        self.__eventManager = Event.EventManager()
        em = self.__eventManager
        self.onRosterReceived = Event.Event(em)
        self.onPlayerAdded = Event.Event(em)
        self.onPlayerRemoved = Event.Event(em)
        self.onPlayerStateChanged = Event.Event(em)
        self.onPlayerGroupChanged = Event.Event(em)
        self.onPlayerRosterChanged = Event.Event(em)
        self.onTeamStatesReceived = Event.Event(em)
        self.onSettingsReceived = Event.Event(em)
        self.onSettingUpdated = Event.Event(em)
        self.onKickedFromQueue = Event.Event(em)
        self.onPropertiesReceived = Event.Event(em)
        self.onPropertyUpdated = Event.Event(em)
        return

    def destroy(self):
        self.__eventManager.clear()
        return

    def update(self, updateType, argStr):
        delegateName = self.__onUpdate.get(updateType, None)
        if delegateName is not None:
            getattr(self, delegateName)(argStr)
        return

    def __accInfoAsDict(self, accInfoAsTuple):
        pID, name, dbID, badges, roster, state, time, vehCompDescr, igrType, clanDBID, clanAbbrev, group, vehEnhancements, role = accInfoAsTuple
        return (roster, pID,
         {b'name': name, 
            b'dbID': dbID, 
            b'badges': badges, 
            b'state': state, 
            b'time': time, 
            b'vehCompDescr': vehCompDescr, 
            b'clanDBID': clanDBID, 
            b'clanAbbrev': clanAbbrev, 
            b'igrType': igrType, 
            b'group': group, 
            b'vehEnhancements': vehEnhancements, 
            b'role': role})

    def __onRosterReceived(self, argStr):
        rostersAsList = pickle.loads(argStr)
        self.rosters.clear()
        for accInfoAsTuple in rostersAsList:
            roster, pID, accInfo = self.__accInfoAsDict(accInfoAsTuple)
            self.rosters.setdefault(roster, {})[pID] = accInfo

        self.onRosterReceived()
        return

    def __onPlayerAdded(self, argStr):
        accInfoAsTuple = pickle.loads(argStr)
        roster, pID, accInfo = self.__accInfoAsDict(accInfoAsTuple)
        self.rosters.setdefault(roster, {})[pID] = accInfo
        self.onPlayerAdded(pID, roster)
        return

    def __onPlayerRemoved(self, argStr):
        pID, roster = pickle.loads(argStr)
        name = self.rosters.get(roster, {}).pop(pID, {}).get(b'name', b'')
        self.onPlayerRemoved(pID, roster, name)
        return

    def __onPlayerStateChanged(self, argStr):
        pID, roster, state, vehCompDescr, igrType, badges, clanDBID, clanAbbrev, vehEnhancements, role = pickle.loads(argStr)
        LOG_DEBUG_DEV(b'__onPlayerStateChanged', pID, roster, state, vehCompDescr, igrType, clanDBID, clanAbbrev, vehEnhancements, role)
        accInfo = self.rosters.get(roster, {}).get(pID, None)
        if accInfo is None:
            return
        else:
            accInfo[b'state'] = state
            accInfo[b'vehCompDescr'] = vehCompDescr
            accInfo[b'igrType'] = igrType
            accInfo[b'badges'] = badges
            accInfo[b'clanDBID'] = clanDBID
            accInfo[b'clanAbbrev'] = clanAbbrev
            accInfo[b'vehEnhancements'] = vehEnhancements
            accInfo[b'role'] = role
            self.onPlayerStateChanged(pID, roster)
            return

    def __onPlayerRosterChanged(self, argStr):
        pID, prevRoster, roster, actorID = pickle.loads(argStr)
        accInfo = self.rosters.get(prevRoster, {}).pop(pID, None)
        self.rosters.setdefault(roster, {})[pID] = accInfo
        self.onPlayerRosterChanged(pID, prevRoster, roster, actorID)
        return

    def __onPlayerGroupChanged(self, argStr):
        groupId, prevRoster, roster, group, actorID = pickle.loads(argStr)
        accInfo = self.rosters.get(prevRoster, {}).pop(groupId, None)
        self.rosters.setdefault(roster, {})[groupId] = accInfo
        self.rosters.setdefault(roster, {}).setdefault(groupId, {})[b'group'] = group
        self.onPlayerGroupChanged(groupId, prevRoster, roster, group, actorID)
        return

    def __onTeamStatesReceived(self, argStr):
        team1, team2 = pickle.loads(argStr)
        self.teamStates = [None, team1, team2]
        self.onTeamStatesReceived()
        return

    def __onSettingsReceived(self, argStr):
        self.settings = pickle.loads(argStr)
        self.onSettingsReceived()
        return

    def __onSettingUpdated(self, argStr):
        name, value = pickle.loads(argStr)
        self.settings[name] = value
        self.onSettingUpdated(name)
        return

    def __onPropertiesReceived(self, argStr):
        self.properties = pickle.loads(argStr)
        self.onPropertiesReceived()
        return

    def __onPropertyUpdated(self, argStr):
        if self.properties is None:
            return
        else:
            name, value = pickle.loads(argStr)
            self.properties[name] = value
            self.onPropertyUpdated(name)
            return

    def __onKickedFromQueue(self, argStr):
        self.onKickedFromQueue()
        return
