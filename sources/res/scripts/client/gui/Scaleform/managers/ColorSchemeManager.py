import BigWorld
from gui.Scaleform.framework.entities.abstract.ColorSchemeManagerMeta import ColorSchemeManagerMeta
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.doc_loaders import GuiColorsLoader
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider

class ColorSchemeManager(ColorSchemeManagerMeta):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(ColorSchemeManager, self).__init__()
        self.colors = GuiColorsLoader.load()
        return

    def getColorGroup(self):
        if self.settingsCore.getSetting(b'isColorBlind'):
            return b'color_blind'
        return b'default'

    def getRGBA(self, schemeName):
        return self.colors.getSubScheme(schemeName, self.getColorGroup())[b'rgba']

    def getColorScheme(self, schemeName):
        scheme = self.colors.getSubScheme(schemeName, self.getColorGroup())
        transform = scheme[b'transform']
        return {b'aliasColor': (scheme[b'alias_color']), 
           b'rgb': (self._packRGB(scheme[b'rgba'])), 
           b'adjust': {b'offset': (scheme[b'adjust'][b'offset'].tuple())}, 
           b'transform': {b'mult': (transform[b'mult'].tuple()), 
                          b'offset': (transform[b'offset'].tuple())}}

    def getIsColorBlind(self):
        return self.settingsCore.getSetting(b'isColorBlind')

    def update(self):
        self.as_updateS()
        return

    def _populate(self):
        super(ColorSchemeManager, self)._populate()
        self.settingsCore.onSettingsChanged += self.__onAccountSettingsChange
        return

    def _dispose(self):
        self.settingsCore.onSettingsChanged -= self.__onAccountSettingsChange
        super(ColorSchemeManager, self)._dispose()
        return

    @classmethod
    def _packRGB(cls, rgba):
        return (int(rgba[0]) << 16) + (int(rgba[1]) << 8) + (int(rgba[2]) << 0)

    @classmethod
    def _makeRGB(cls, subScheme):
        return cls._packRGB(subScheme.get(b'rgb', (0, 0, 0, 0)))

    @classmethod
    def _makeAdjustTuple(cls, subScheme):
        return subScheme[b'adjust'][b'offset']

    def __onAccountSettingsChange(self, diff):
        if b'isColorBlind' in diff:
            self.update()
        return


class BattleColorSchemeManager(ColorSchemeManager, IArenaVehiclesController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def update(self):
        super(BattleColorSchemeManager, self).update()
        self.__set3DFlagsColors()
        return

    def invalidateArenaInfo(self):
        self.__set3DFlagsColors()
        return

    def _populate(self):
        super(BattleColorSchemeManager, self)._populate()
        from PlayerEvents import g_playerEvents
        g_playerEvents.onTeamChanged += self.__onTeamChanged
        self.sessionProvider.addArenaCtrl(self)
        return

    def _dispose(self):
        self.sessionProvider.removeArenaCtrl(self)
        from PlayerEvents import g_playerEvents
        g_playerEvents.onTeamChanged -= self.__onTeamChanged
        super(BattleColorSchemeManager, self)._dispose()
        return

    def __set3DFlagsColors(self):
        arenaDP = self.sessionProvider.getArenaDP()
        if arenaDP is None:
            return
        else:
            teamsOnArena = arenaDP.getTeamsOnArena()
            group = self.getColorGroup()
            allyColor = self.colors.getSubScheme(b'flag_team_green', group)[b'rgba']
            enemyColor = self.colors.getSubScheme(b'flag_team_red', group)[b'rgba']
            for teamIdx in teamsOnArena:
                color = allyColor if arenaDP.isAllyTeam(teamIdx) else enemyColor
                BigWorld.setFlagColor(teamIdx, color / 255)

            return

    def __onTeamChanged(self, teamID):
        self.__set3DFlagsColors()
        return
