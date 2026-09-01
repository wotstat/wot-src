from __future__ import absolute_import
import logging, BigWorld
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleTournamentController
import BattleRoyaleTournament
_logger = logging.getLogger(__name__)

class AccountBattleRoyaleTournamentComponent(BigWorld.StaticScriptComponent):
    __battleRoyaleTournamentController = dependency.descriptor(IBattleRoyaleTournamentController)

    def setParticipants(self, participants):
        _logger.debug(b"got tournament participants: '%r'", participants)
        self.__battleRoyaleTournamentController.updateParticipants(participants)
        return

    def setTournamentToken(self, token):
        _logger.debug(b"got joined tournament token: '%r'", token)
        self.__battleRoyaleTournamentController.selectBattleRoyaleTournament(token)
        return

    def tournamentJoin(self, tournamentID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_JOIN, 0, tournamentID, callback)
        return

    def tournamentLeave(self, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_LEAVE, 0, b'', callback)
        return

    def tournamentReady(self, vehInvID, tournamentID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_READY, vehInvID, tournamentID, callback)
        return

    def tournamentNotReady(self, tournamentID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_NOT_READY, 0, tournamentID, callback)
        return

    def tournamentForceStart(self, mapID, callback=None):
        self.entity._doCmdIntStr(BattleRoyaleTournament.CMD_BATTLE_ROYALE_TRN_START_BATTLE, mapID, b'', callback)
        return
