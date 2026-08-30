import logging
from gui.Scaleform.daapi.view.battle.shared import SharedPage
from gui.Scaleform.daapi.view.battle.shared.page import ComponentsConfig
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
_logger = logging.getLogger(__name__)
_COSMIC_COMPONENTS_CONFIG = ComponentsConfig(config=(
 (
  BATTLE_CTRL_ID.ARENA_PERIOD,
  (
   BATTLE_VIEW_ALIASES.COSMIC_HUD,)),
 (
  BATTLE_CTRL_ID.DEBUG, (BATTLE_VIEW_ALIASES.DEBUG_PANEL,)),
 (
  BATTLE_CTRL_ID.BATTLE_HINTS, (BATTLE_VIEW_ALIASES.COSMIC_HUD,))))

class CosmicPage(SharedPage):

    def __init__(self):
        _logger.debug(b'CosmicPage.__init__')
        super(CosmicPage, self).__init__(components=_COSMIC_COMPONENTS_CONFIG, external=())
        return

    def _onBattleLoadingStart(self):
        _logger.debug(b'CosmicPage._onBattleLoadingStart')
        self._blToggling = set(self.as_getComponentsVisibilityS())
        self._blToggling.difference_update([BATTLE_VIEW_ALIASES.BATTLE_LOADING])
        self._setComponentsVisibility(visible={BATTLE_VIEW_ALIASES.BATTLE_LOADING}, hidden=self._blToggling)
        return

    def _addDefaultHitDirectionController(self, controllers):
        return controllers

    def _handleToggleFullStats(self, event):
        return

    def _handleToggleFullStatsQuestProgress(self, event):
        return

    def _handleToggleFullStatsPersonalReserves(self, event):
        return

    def _handleGUIToggled(self, event):
        return

    def _handleRadialMenuCmd(self, event):
        return

    def _changeCtrlMode(self, ctrlMode):
        _logger.info(b'CosmicPage._changeCtrlMode: %s', str(ctrlMode))
        return

    def _canShowPostmortemTips(self):
        return False

    def _switchToPostmortem(self):
        return

    def as_setPostmortemTipsVisibleS(self, value):
        return
