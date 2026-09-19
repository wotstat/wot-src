from __future__ import absolute_import
from HWArenaPhasesComponent import HWArenaPhasesComponent
from halloween.gui.scaleform.daapi.view.battle.fullscreen_watcher_mixin import FullscreenWatcherMixin
from halloween.gui.scaleform.daapi.view.meta.PhaseModifierMeta import PhaseModifierMeta
from typing import Optional
from gui.impl import backport
from gui.impl.gen import R

class HWModifierWidget(FullscreenWatcherMixin, PhaseModifierMeta):
    ICONS_PATH = R.images.halloween.gui.maps.icons.battleHints
    BATTLE_HINT = R.strings.halloween_battle.battleHint

    def _populate(self):
        super(HWModifierWidget, self)._populate()
        HWArenaPhasesComponent.onPhaseModifierChanged += self._update
        return

    def _dispose(self):
        HWArenaPhasesComponent.onPhaseModifierChanged -= self._update
        super(HWModifierWidget, self)._dispose()
        return

    def _update(self, arenaPhases):
        if not arenaPhases:
            return
        hasModifierName = bool(arenaPhases.modifierName)
        self.needToShow = hasModifierName
        self.updateVisibility()
        if hasModifierName:
            self.as_updateHintS({b'phaseName': (backport.text(self.BATTLE_HINT.phase.dyn(str(arenaPhases.activePhase))())), 
               b'modifierName': (backport.text(self.BATTLE_HINT.modifierName.dyn(arenaPhases.modifierName)())), 
               b'modifierRule': (backport.text(self.BATTLE_HINT.modifierRule.dyn(arenaPhases.modifierName)())), 
               b'modifierColor': (arenaPhases.modifierColor), 
               b'iconSource': (backport.image(self.ICONS_PATH.dyn(arenaPhases.modifierName)()))})
        return

    def _modifierChanged(self, modifierName):
        self.__modifierName = modifierName
        return
