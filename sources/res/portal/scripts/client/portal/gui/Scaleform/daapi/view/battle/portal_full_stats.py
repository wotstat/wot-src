from battle_royale.gui.Scaleform.daapi.view.battle.full_stats import FullStatsComponent
import BigWorld
from gui.impl import backport
from gui.impl.gen import R
from PortalBattleStateComponent import PortalBattleStateComponent

class PortalFullStatsComponent(FullStatsComponent):

    def _populate(self):
        super(PortalFullStatsComponent, self)._populate()
        PortalBattleStateComponent.onCampInfoUpdated += self.__onCampInfoUpdated
        return

    def _dispose(self):
        super(PortalFullStatsComponent, self)._dispose()
        PortalBattleStateComponent.onCampInfoUpdated -= self.__onCampInfoUpdated
        return

    def _initPanel(self):
        campsCount = 4
        capturedCamps = 0
        data = {b'header': {b'title': (backport.text(R.strings.portal_event.battle.tab.title())), 
                       b'subTitle': (backport.text(R.strings.portal_event.battle.tab.subTitle())), 
                       b'description': (backport.text(R.strings.portal_event.battle.tab.description()))}, 
           b'campsCount': campsCount, 
           b'capturedCamps': capturedCamps, 
           b'minimapItems': (self.__getMinimapItems())}
        self.as_setDataS(data)
        return

    def __onCampInfoUpdated(self, *args, **kwargs):
        campsCount = self.__battleState.getCampsCount()
        capturedCamps = self.__battleState.getCapturedCampsCount()
        self.as_updateScoreS(campsCount, capturedCamps, b'')
        return

    def __getMinimapItems(self):
        return [
         self.__getMinimapItem(b'portal_lgd', backport.text(R.strings.portal_event.battle.tab.minimapItemText.portal()), b'add'),
         self.__getMinimapItem(b'guard_lgd', backport.text(R.strings.portal_event.battle.tab.minimapItemText.guard()), b'add'),
         self.__getMinimapItem(b'camp_lgd', backport.text(R.strings.portal_event.battle.tab.minimapItemText.camp()), b'add'),
         self.__getMinimapItem(b'lane_lgd', backport.text(R.strings.portal_event.battle.tab.minimapItemText.lane()), b'add'),
         self.__getMinimapItem(b'teleport_lgd', backport.text(R.strings.portal_event.battle.tab.minimapItemText.teleport())),
         self.__getMinimapItem(b'tp_hub_lgd', backport.text(R.strings.portal_event.battle.tab.minimapItemText.tp_hub())),
         self.__getMinimapItem(b'base_lgd', backport.text(R.strings.portal_event.battle.tab.minimapItemText.base()))]

    def __getMinimapItem(self, icon, description, blendMode=b'normal'):
        return {b'icon': icon, 
           b'description': description, 
           b'blendMode': blendMode}

    def __getScoreBlock(self, icon, count, descr, squads=b''):
        return {b'icon': icon, 
           b'count': count, 
           b'description': descr, 
           b'squads': squads}

    @property
    def __battleState(self):
        return BigWorld.player().arena.arenaInfo.portalBattleStateComponent
