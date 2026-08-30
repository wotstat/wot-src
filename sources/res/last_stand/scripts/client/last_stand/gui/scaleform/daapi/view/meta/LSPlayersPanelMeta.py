from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class LSPlayersPanelMeta(PlayersPanel):

    def onVoiceChatClick(self):
        self._printOverrideError(b'onVoiceChatClick')
        return

    def onTalkDown(self):
        self._printOverrideError(b'onTalkDown')
        return

    def onTalkUp(self):
        self._printOverrideError(b'onTalkUp')
        return

    def as_setPlayerPanelInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelInfo(data)
        return

    def as_setPlayerPanelHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelHp(vehID, hpMax, hpCurrent)
        return

    def as_setVoiceChatBindingsS(self, chatBind, talkBind):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatBindings(chatBind, talkBind)
        return

    def as_setVoiceChatActivatedS(self, isActivated):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatActivated(isActivated)
        return

    def as_setVoiceChatAvailableS(self, isAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatAvailable(isAvailable)
        return

    def as_setVoiceChatEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatEnabled(isEnabled)
        return

    def as_setIsTalkS(self, isTalk):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsTalk(isTalk)
        return

    def as_setPlayerDeadS(self, vehID):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerDead(vehID)
        return

    def as_setPostmortemS(self, isPostmortem):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostmortem(isPostmortem)
        return
