import operator
from soft_exception import SoftException
from account_helpers.settings_core.settings_constants import GRAPHICS
from debug_utils import LOG_DEBUG, LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.meta.BattleMessageListMeta import BattleMessageListMeta
from gui.Scaleform.genConsts.BATTLE_MESSAGES_CONSTS import BATTLE_MESSAGES_CONSTS
from gui.app_loader import sf_battle
from gui.doc_loaders import messages_panel_reader
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
_MESSAGES_SETTINGS_PATH = b'gui/{}'
_EXTRA_COLOR_FORMAT = b'<font color="#{0:02X}{1:02X}{2:02X}">{3:>s}</font>'
_COLOR_TO_METHOD = {(BATTLE_MESSAGES_CONSTS.COLOR_YELLOW): b'as_showYellowMessageS', 
   (BATTLE_MESSAGES_CONSTS.COLOR_RED): b'as_showRedMessageS', 
   (BATTLE_MESSAGES_CONSTS.COLOR_PURPLE): b'as_showPurpleMessageS', 
   (BATTLE_MESSAGES_CONSTS.COLOR_GREEN): b'as_showGreenMessageS', 
   (BATTLE_MESSAGES_CONSTS.COLOR_GOLD): b'as_showGoldMessageS', 
   (BATTLE_MESSAGES_CONSTS.COLOR_SELF): b'as_showSelfMessageS'}

class FadingMessages(BattleMessageListMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, name, mFile):
        super(BattleMessageListMeta, self).__init__()
        self.__name = name
        self.__settingsFilePath = _MESSAGES_SETTINGS_PATH.format(mFile)
        self.__isColorBlind = self.settingsCore.getSetting(GRAPHICS.COLOR_BLIND)
        self._messages = {}
        self.__styles = None
        return

    def __del__(self):
        LOG_DEBUG((b'{0} is deleted').format(self.__name))
        return

    def setSettingFile(self, mFile):
        self.__settingsFilePath = _MESSAGES_SETTINGS_PATH.format(mFile)
        return

    @sf_battle
    def app(self):
        return

    def clear(self):
        self.as_clearS()
        return

    def showMessage(self, key, args=None, extra=None, postfix=b''):
        if postfix:
            extKey = (u'{0}_{1}').format(key, postfix)
            if extKey in self._messages:
                self.__doShowMessage(extKey, args, extra)
                return
        if key in self._messages:
            self.__doShowMessage(key, args, extra)
        return

    def getStyles(self):
        return self.__styles

    def _populate(self):
        super(FadingMessages, self)._populate()
        settings, self.__styles, self._messages = messages_panel_reader.readXML(self.__settingsFilePath)
        self.as_setupListS(settings)
        self._addGameListeners()
        return

    def _dispose(self):
        self._messages = None
        self.__styles = None
        self.clear()
        self._removeGameListeners()
        super(FadingMessages, self)._dispose()
        return

    def _addGameListeners(self):
        self.settingsCore.onSettingsChanged += self.__onSettingsChanged
        return

    def _removeGameListeners(self):
        self.settingsCore.onSettingsChanged -= self.__onSettingsChanged
        return

    def __formatEntitiesEx(self, args, extra=None):
        if extra is None:
            extra = ()
        manager = self.app.colorManager
        battleCtx = self.sessionProvider.getCtx()
        isTeamKiller = battleCtx.isTeamKiller
        isSquadMan = battleCtx.isSquadMan
        for argName, vID in extra:
            arg = args.get(argName)
            rgba = None
            if isTeamKiller(vID=vID):
                rgba = manager.getRGBA(b'teamkiller')
            elif isSquadMan(vID=vID):
                rgba = manager.getRGBA(b'squad')
            if arg and rgba:
                args[argName] = _EXTRA_COLOR_FORMAT.format(int(rgba[0]), int(rgba[1]), int(rgba[2]), arg)

        return

    def __doShowMessage(self, key, args=None, extra=None):
        msgText, colors = self._messages[key]
        if args is not None:
            self.__formatEntitiesEx(args, extra=extra)
            try:
                msgText = msgText % args
            except TypeError:
                LOG_CURRENT_EXCEPTION()

        if self.__isColorBlind:
            color = colors[1]
        else:
            color = colors[0]
        if color in _COLOR_TO_METHOD:
            method = _COLOR_TO_METHOD[color]
        else:
            raise SoftException((b'Can not recognize color for message "{}". List "{}"').format(key, self.__name))
        LOG_DEBUG(b'Show message in a battle', self.__name, key)
        operator.methodcaller(method, key, msgText)(self)
        return

    def __onSettingsChanged(self, diff):
        if b'isColorBlind' in diff:
            self.__isColorBlind = diff[b'isColorBlind']
        return
