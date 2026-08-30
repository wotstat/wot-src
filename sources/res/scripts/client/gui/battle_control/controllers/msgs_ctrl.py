from __future__ import absolute_import
import weakref, BigWorld
from helpers import dependency
import BattleReplay, Event
from ReplayEvents import g_replayEvents
from constants import ATTACK_REASON_INDICES as _AR_INDICES
from gui.battle_control.arena_info.arena_vos import EPIC_BATTLE_KEYS
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController
from items.battle_royale import isSpawnedBot, isHunterBot
from skeletons.gui.battle_session import IBattleSessionProvider

class _ENTITY_TYPE(object):
    UNKNOWN = b'unknown'
    SELF = b'self'
    ALLY = b'ally'
    ENEMY = b'enemy'
    SUICIDE = b'suicide'


_ATTACK_REASON_CODE = {(_AR_INDICES[b'shot']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'fire']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'ramming']): b'DEATH_FROM_RAMMING', 
   (_AR_INDICES[b'world_collision']): b'DEATH_FROM_WORLD_COLLISION', 
   (_AR_INDICES[b'cgf_world']): b'DEATH_FROM_WORLD_COLLISION', 
   (_AR_INDICES[b'death_zone']): b'DEATH_FROM_DEATH_ZONE', 
   (_AR_INDICES[b'static_deathzone']): b'DEATH_FROM_STATIC_DEATH_ZONE', 
   (_AR_INDICES[b'minefield_zone']): b'DEATH_FROM_MINEFIELD_ZONE', 
   (_AR_INDICES[b'drowning']): b'DEATH_FROM_DROWNING', 
   (_AR_INDICES[b'overturn']): b'DEATH_FROM_OVERTURN', 
   (_AR_INDICES[b'artillery_protection']): b'DEATH_FROM_ARTILLERY_PROTECTION', 
   (_AR_INDICES[b'artillery_sector']): b'DEATH_FROM_SECTOR_PROTECTION', 
   (_AR_INDICES[b'bombers']): b'DEATH_FROM_SECTOR_BOMBERS', 
   (_AR_INDICES[b'recovery']): b'DEATH_FROM_RECOVERY', 
   (_AR_INDICES[b'artillery_eq']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'bomber_eq']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'minefield_eq']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'spawned_bot_explosion']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'fort_artillery_eq']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'thunderStrike']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'corrodingShot']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'fireCircle']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'clingBrander']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'battleship']): b'DEATH_FROM_SHOT', 
   (_AR_INDICES[b'destroyer']): b'DEATH_FROM_SHOT'}
_PLAYER_KILL_ENEMY_SOUND = b'enemy_killed_by_player'
_PLAYER_KILL_ALLY_SOUND = b'ally_killed_by_player'
_ALLY_KILLED_SOUND = b'ally_killed_by_enemy'
_ENEMY_KILLED_SOUND = b'enemy_killed_by_ally'

class BattleMessagesController(IBattleController):
    __slots__ = (b'_battleCtx', b'_arenaDP', b'_arenaVisitor', b'_eManager', b'_buffer', b'_isUIPopulated', b'onShowVehicleMessageByCode', b'onShowVehicleMessageByKey', b'onShowVehicleErrorByKey', b'onShowPlayerMessageByCode', b'onShowPlayerMessageByKey', b'onShowDestructibleEntityMessageByCode', b'__weakref__', b'__specEntityStringByCode', b'_attackReasonCodes')

    def __init__(self, setup):
        self._battleCtx = weakref.proxy(setup.battleCtx)
        self._arenaDP = weakref.proxy(setup.arenaDP)
        self._arenaVisitor = weakref.proxy(setup.arenaVisitor)
        self._eManager = Event.EventManager()
        self.onShowVehicleMessageByCode = Event.Event(self._eManager)
        self.onShowVehicleMessageByKey = Event.Event(self._eManager)
        self.onShowVehicleErrorByKey = Event.Event(self._eManager)
        self.onShowPlayerMessageByCode = Event.Event(self._eManager)
        self.onShowPlayerMessageByKey = Event.Event(self._eManager)
        self.onShowDestructibleEntityMessageByCode = Event.Event(self._eManager)
        self._attackReasonCodes = _ATTACK_REASON_CODE
        self._buffer = []
        self._isUIPopulated = False
        self.__specEntityStringByCode = {}
        self.__initSpecEntityStringFuncsByCode()
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.MESSAGES

    def startControl(self):
        return

    def stopControl(self):
        self._eManager.clear()
        self._battleCtx = None
        self._arenaDP = None
        self._arenaVisitor = None
        self.__specEntityStringByCode = {}
        return

    def showDestructibleEntityDestroyedMessage(self, avatar, destructibleID, attackerID):
        try:
            playerVehicleID = avatar.playerVehicleID
        except AttributeError:
            return

        if attackerID == playerVehicleID:
            code = b'DESTRUCTIBLE_DESTROYED_SELF'
        elif BigWorld.player().team == 1:
            code = b'DESTRUCTIBLE_DESTROYED_ALLY'
        else:
            code = b'DESTRUCTIBLE_DESTROYED_ENEMY'
        self.onShowDestructibleEntityMessageByCode(code, destructibleID, attackerID)
        return

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        try:
            playerVehicleID = avatar.playerVehicleID
        except AttributeError:
            return

        isMyVehicle = targetID == playerVehicleID
        if isMyVehicle:
            return
        else:
            if targetID == attackerID and self._battleCtx.isObserver(targetID):
                return
            if not avatar.isVehicleAlive:
                if avatar.isObserver() and targetID == avatar.observedVehicleID:
                    return
                if targetID == avatar.inputHandler.ctrl.curVehicleID:
                    return
            code, postfix, sound, soundExt = self.__getKillInfo(avatar, targetID, attackerID, reason)
            if sound is not None:
                avatar.soundNotifications.play(sound)
            if soundExt is not None:
                avatar.soundNotifications.play(soundExt)
            self.onShowPlayerMessageByCode(code, postfix, targetID, attackerID, equipmentID, False)
            return

    def showVehicleDamageInfo(self, avatar, code, targetID, entityID, extra, equipmentID, ignoreMessages=False):
        code, postfix = self.__getDamageInfo(avatar, code, entityID, targetID)
        self.onShowPlayerMessageByCode(code, postfix, targetID, entityID, equipmentID, ignoreMessages)
        self.onShowVehicleMessageByCode(code, postfix, entityID, extra, equipmentID, ignoreMessages)
        return

    def showVehicleMessage(self, key, args=None):
        self.onShowVehicleMessageByKey(key, args, None)
        return

    def showVehicleError(self, key, args=None):
        self.onShowVehicleErrorByKey(key, args, None)
        return

    def showAllyHitMessage(self, vehicleID=None):
        self.onShowPlayerMessageByKey(b'ALLY_HIT', {b'entity': (self._battleCtx.getPlayerFullName(vID=vehicleID))}, (
         (
          b'entity', vehicleID),))
        return

    def _getAttackReasonCodes(self, reason):
        return self._attackReasonCodes.get(reason)

    def _getEntityType(self, avatar, entityID):
        if entityID == avatar.playerVehicleID:
            return _ENTITY_TYPE.SELF
        if self._battleCtx.isAlly(entityID):
            return _ENTITY_TYPE.ALLY
        if self._battleCtx.isEnemy(entityID):
            return _ENTITY_TYPE.ENEMY
        return _ENTITY_TYPE.UNKNOWN

    def __getEntityString(self, avatar, entityID, code):
        func = self.__specEntityStringByCode.get(code)
        res = func(avatar, entityID, code) if func is not None else None
        if res:
            return res
        else:
            return self._getEntityType(avatar, entityID)

    def __getEntityStringDeathZone(self, avatar, entityID, code):
        observedVehicleID = BigWorld.player().getObservedVehicleID()
        if observedVehicleID and BigWorld.player().isObserver() and observedVehicleID != avatar.playerVehicleID:
            ownTeam = self._arenaDP.getVehicleInfo(avatar.playerVehicleID).team
            entityTeam = self._arenaDP.getVehicleInfo(entityID).team
            isAlly = ownTeam == entityTeam
            if isAlly:
                return _ENTITY_TYPE.ALLY
            return _ENTITY_TYPE.ENEMY
        else:
            return

    def __getDamageInfo(self, avatar, code, entityID, targetID):
        target = self.__getEntityString(avatar, targetID, code)
        if not entityID or entityID == targetID:
            postfix = b'%s_%s' % (target.upper(), _ENTITY_TYPE.SUICIDE.upper())
        else:
            entity = self.__getEntityString(avatar, entityID, code)
            postfix = b'%s_%s' % (entity.upper(), target.upper())
        return (code, postfix)

    def __getKillInfo(self, avatar, targetID, attackerID, reason):
        attacker = self.__getEntityString(avatar, attackerID, reason)
        target = _ENTITY_TYPE.SUICIDE
        if targetID != attackerID:
            target = self.__getEntityString(avatar, targetID, reason)
        code = self._getAttackReasonCodes(reason)
        sound = None
        soundExt = None
        if attackerID == BigWorld.player().playerVehicleID:
            if target == _ENTITY_TYPE.ENEMY:
                sound = _PLAYER_KILL_ENEMY_SOUND
            elif target == _ENTITY_TYPE.ALLY:
                sound = _PLAYER_KILL_ALLY_SOUND
                soundExt = _ALLY_KILLED_SOUND
        elif target == _ENTITY_TYPE.ALLY or target == _ENTITY_TYPE.SUICIDE and attacker == _ENTITY_TYPE.ALLY:
            soundExt = _ALLY_KILLED_SOUND
        elif target == _ENTITY_TYPE.ENEMY or target == _ENTITY_TYPE.SUICIDE and attacker == _ENTITY_TYPE.ENEMY:
            soundExt = _ENEMY_KILLED_SOUND
        return (code, b'%s_%s' % (attacker.upper(), target.upper()), sound, soundExt)

    def __initSpecEntityStringFuncsByCode(self):
        self.__specEntityStringByCode[b'DEATH_FROM_DEATH_ZONE'] = self.__getEntityStringDeathZone
        return

    def onUIPopulated(self):
        self._isUIPopulated = True
        for args in self._buffer:
            self.onShowVehicleMessageByKey(*args)

        return


class BattleMessagesPlayer(BattleMessagesController):

    def startControl(self):
        super(BattleMessagesPlayer, self).startControl()
        g_replayEvents.onWatcherNotify += self.__onWatcherNotify
        return

    def stopControl(self):
        g_replayEvents.onWatcherNotify -= self.__onWatcherNotify
        super(BattleMessagesPlayer, self).stopControl()
        return

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleKilledMessage(avatar, targetID, attackerID, equipmentID, reason)
        return

    def showDestructibleEntityDestroyedMessage(self, avatar, destructibleID, attackerID):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showDestructibleEntityDestroyedMessage(avatar, destructibleID, attackerID)
        return

    def showVehicleDamageInfo(self, avatar, code, targetID, entityID, extra, equipmentID, ignoreMessages=False):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleDamageInfo(avatar, code, targetID, entityID, extra, equipmentID, ignoreMessages)
        return

    def showVehicleMessage(self, key, args=None):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleMessage(key, args)
        return

    def showVehicleError(self, key, args=None):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showVehicleError(key, args)
        return

    def showAllyHitMessage(self, vehicleID=None):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        super(BattleMessagesPlayer, self).showAllyHitMessage(vehicleID)
        return

    def showInfoMessage(self, key, withBuffer=False, args=None):
        if withBuffer and not self._isUIPopulated:
            self._buffer.append((key, args))
        else:
            super(BattleMessagesPlayer, self).showVehicleMessage(key, args)
        return

    def __onWatcherNotify(self, message, args):
        self.showInfoMessage(message, withBuffer=True, args=args)
        return


class EpicBattleMessagesPlayer(BattleMessagesPlayer):

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        if not self._messageIsAllowedInEpicBattle(targetID, attackerID):
            return
        super(EpicBattleMessagesPlayer, self).showVehicleKilledMessage(avatar, targetID, attackerID, equipmentID, reason)
        return

    def _messageIsAllowedInEpicBattle(self, targetID, attackerID):
        componentSystem = self._arenaVisitor.getComponentSystem()
        if componentSystem is not None:
            playerDataComp = getattr(componentSystem, b'playerDataComponent', None)
            if playerDataComp is not None:
                voTarget = self._arenaDP.getVehicleStats(targetID)
                voAttacker = self._arenaDP.getVehicleStats(attackerID)
                targetLane = voTarget.gameModeSpecific.getValue(EPIC_BATTLE_KEYS.PLAYER_GROUP)
                attackerLane = voAttacker.gameModeSpecific.getValue(EPIC_BATTLE_KEYS.PLAYER_GROUP)
                playerLane = playerDataComp.physicalLane
                if playerLane not in (targetLane, attackerLane):
                    return False
        return True


class EpicBattleMessagesController(BattleMessagesController):

    def __init__(self, setup):
        super(EpicBattleMessagesController, self).__init__(setup)
        self._attackReasonCodes[_AR_INDICES[b'minefield_eq']] = b'DEATH_FROM_MINE_EXPLOSION'
        return

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        if not self._messageIsAllowedInEpicBattle(targetID, attackerID):
            return
        super(EpicBattleMessagesController, self).showVehicleKilledMessage(avatar, targetID, attackerID, equipmentID, reason)
        return

    def _messageIsAllowedInEpicBattle(self, targetID, attackerID):
        componentSystem = self._arenaVisitor.getComponentSystem()
        if componentSystem is not None:
            playerDataComp = getattr(componentSystem, b'playerDataComponent', None)
            if playerDataComp is not None:
                voTarget = self._arenaDP.getVehicleStats(targetID)
                voAttacker = self._arenaDP.getVehicleStats(attackerID)
                targetLane = voTarget.gameModeSpecific.getValue(EPIC_BATTLE_KEYS.PLAYER_GROUP)
                attackerLane = voAttacker.gameModeSpecific.getValue(EPIC_BATTLE_KEYS.PLAYER_GROUP)
                playerLane = playerDataComp.physicalLane
                if playerLane not in (targetLane, attackerLane):
                    return False
        return True


@dependency.replace_none_kwargs(battleSessionProvider=IBattleSessionProvider)
def _isHideVehicleKilledMsg(vehicleID, battleSessionProvider=None):
    ctx = battleSessionProvider.getCtx()
    vTypeInfoVO = ctx.getArenaDP().getVehicleInfo(vehicleID).vehicleType
    return isSpawnedBot(vTypeInfoVO.tags) or isHunterBot(vTypeInfoVO.tags)


@dependency.replace_none_kwargs(battleSessionProvider=IBattleSessionProvider)
def _getSpawnedBotMsgData(vehicleID, battleSessionProvider=None):
    ctx = battleSessionProvider.getCtx()
    vTypeInfoVO = ctx.getArenaDP().getVehicleInfo(vehicleID).vehicleType
    if isSpawnedBot(vTypeInfoVO.tags):
        botMasterPlayer = ctx.getPlayerFullName(vehicleID, showVehShortName=False)
        playerInfo = b'%s (%s)' % (botMasterPlayer, vTypeInfoVO.shortNameWithPrefix)
        return (
         b'ALLY_HIT', {b'entity': playerInfo}, ((b'entity', vehicleID),))
    else:
        return


class _BRBattleMessagesMixin(object):
    _battleCtx = None

    def _getEntityType(self, avatar, entityID):
        if entityID == avatar.playerVehicleID:
            return _ENTITY_TYPE.SELF
        if self._battleCtx.isEnemy(entityID) or self._battleCtx.isAlly(entityID) and self._playerChangedTeam():
            return _ENTITY_TYPE.ENEMY
        if self._battleCtx.isAlly(entityID):
            return _ENTITY_TYPE.ALLY
        return _ENTITY_TYPE.UNKNOWN

    def _playerChangedTeam(self):
        if b'observer' in BigWorld.player().vehicleTypeDescriptor.type.tags:
            return False
        arenaDP = self._battleCtx.getArenaDP()
        if not arenaDP:
            return False
        allyTeam = arenaDP.getAllyTeams()[0]
        currentTeam = BigWorld.player().team
        return allyTeam != currentTeam


class BattleRoyaleBattleMessagesController(_BRBattleMessagesMixin, BattleMessagesController):

    def showAllyHitMessage(self, vehicleID=None):
        spawnBotData = _getSpawnedBotMsgData(vehicleID)
        if spawnBotData:
            self.onShowPlayerMessageByKey(*spawnBotData)
            return
        super(BattleRoyaleBattleMessagesController, self).showAllyHitMessage(vehicleID)
        return

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        if _isHideVehicleKilledMsg(targetID):
            return
        equipmentID = 0
        super(BattleRoyaleBattleMessagesController, self).showVehicleKilledMessage(avatar, targetID, attackerID, equipmentID, reason)
        return


class BattleRoyaleBattleMessagesPlayer(_BRBattleMessagesMixin, BattleMessagesPlayer):

    def showAllyHitMessage(self, vehicleID=None):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        spawnBotData = _getSpawnedBotMsgData(vehicleID)
        if spawnBotData:
            self.onShowPlayerMessageByKey(*spawnBotData)
            return
        super(BattleRoyaleBattleMessagesPlayer, self).showAllyHitMessage(vehicleID)
        return

    def showVehicleKilledMessage(self, avatar, targetID, attackerID, equipmentID, reason):
        if BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        if _isHideVehicleKilledMsg(targetID):
            return
        equipmentID = 0
        super(BattleRoyaleBattleMessagesPlayer, self).showVehicleKilledMessage(avatar, targetID, attackerID, equipmentID, reason)
        return


def createBattleMessagesCtrl(setup):
    sessionProvider = dependency.instance(IBattleSessionProvider)
    arenaVisitor = sessionProvider.arenaVisitor
    gui = arenaVisitor.gui
    if gui.isInEpicRange():
        if setup.isReplayPlaying:
            ctrl = EpicBattleMessagesPlayer(setup)
        else:
            ctrl = EpicBattleMessagesController(setup)
    elif gui.isBattleRoyale():
        if setup.isReplayPlaying:
            ctrl = BattleRoyaleBattleMessagesPlayer(setup)
        else:
            ctrl = BattleRoyaleBattleMessagesController(setup)
    elif setup.isReplayPlaying:
        ctrl = BattleMessagesPlayer(setup)
    else:
        ctrl = BattleMessagesController(setup)
    return ctrl
