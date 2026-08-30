from __future__ import absolute_import
from MemoryCriticalController import g_critMemHandler
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.battle.shared.messages import fading_messages
from gui.shared.events import GameEvent
from items import vehicles
_VEHICLE_STYLE_FORMATTER = b'<font size="%(fontSize)s" face="%(fontFace)s" color="%(fontColor)s">{0}</font>'

class VehicleMessages(fading_messages.FadingMessages):

    def __init__(self):
        super(VehicleMessages, self).__init__(b'VehicleMessagesPanel', b'vehicle_messages_panel.xml')
        self.__styleFormatter = None
        return

    def __del__(self):
        LOG_DEBUG(b'VehicleMessages panel is deleted')
        return

    def _populate(self):
        super(VehicleMessages, self)._populate()
        styles = self.getStyles()
        self.__styleFormatter = _VEHICLE_STYLE_FORMATTER % styles[b'entityStyle']
        return

    def _dispose(self):
        self.__styleFormatter = None
        super(VehicleMessages, self)._dispose()
        return

    def _addGameListeners(self):
        super(VehicleMessages, self)._addGameListeners()
        self.addListener(GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade)
        for message in g_critMemHandler.messages:
            self.__handleMemoryCriticalMessage(message)

        g_critMemHandler.onMemCrit += self.__handleMemoryCriticalMessage
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleMessageByCode += self.__onShowVehicleMessageByCode
            ctrl.onShowVehicleMessageByKey += self.__onShowVehicleMessageByKey
            ctrl.onUIPopulated()
        return

    def _removeGameListeners(self):
        self.removeListener(GameEvent.SCREEN_SHOT_MADE, self.__handleScreenShotMade)
        if g_critMemHandler.onMemCrit:
            g_critMemHandler.onMemCrit -= self.__handleMemoryCriticalMessage
        ctrl = self.sessionProvider.shared.messages
        if ctrl is not None:
            ctrl.onShowVehicleMessageByCode -= self.__onShowVehicleMessageByCode
            ctrl.onShowVehicleMessageByKey -= self.__onShowVehicleMessageByKey
        super(VehicleMessages, self)._removeGameListeners()
        return

    def _getPlayerInfo(self, entityID):
        ctx = self.sessionProvider.getCtx()
        vInfoVO = ctx.getArenaDP().getVehicleInfo(entityID)
        playerName = ctx.getPlayerFullName(entityID, showVehShortName=False)
        playerInfo = b'%s | %s' % (playerName, vInfoVO.getDisplayedName())
        return playerInfo

    def __handleMemoryCriticalMessage(self, message):
        self.showMessage(message[1])
        return

    def __handleScreenShotMade(self, event):
        if b'path' not in event.ctx:
            return
        self.showMessage(b'SCREENSHOT_CREATED', {b'path': (event.ctx[b'path'])})
        return

    def __onShowVehicleMessageByCode(self, code, postfix, entityID, extra, equipmentID, ignoreMessages):
        LOG_DEBUG(b'onShowVehicleMessage', code, postfix, entityID, extra, equipmentID, ignoreMessages)
        if ignoreMessages:
            return
        else:
            names = {b'device': b'', b'entity': b'', b'target': b''}
            if extra is not None:
                names[b'device'] = extra.deviceUserString
            if entityID:
                names[b'entity'] = self.__formatEntity(entityID)
            if equipmentID:
                equipment = vehicles.g_cache.equipments().get(equipmentID)
                if equipment is not None:
                    postfix = (b'_').join((postfix, equipment.messagePostfix))
            self.showMessage(code, names, postfix=postfix)
            return

    def __onShowVehicleMessageByKey(self, key, args=None, extra=None):
        self.showMessage(key, args, extra)
        return

    def __formatEntity(self, entityID):
        playerInfo = self._getPlayerInfo(entityID)
        entityInfo = self.__styleFormatter.format(playerInfo)
        return entityInfo
