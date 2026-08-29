from typing import Optional, Type, NamedTuple
from gui.impl.battle.battle_page.battle_context_hints.battle_context_hint_view import BattleContextHintsView
from gui.impl.battle.battle_page.battle_context_hints.battle_context_hints_presenters import BattleContextHintsViewPresenter
from gui.battle_control.battle_context_hints.activation_triggers import HintActivationTrigger
from gui.battle_control.battle_context_hints.applying_triggers import HintApplyingTrigger
from gui.battle_control.battle_context_hints.hint_lifecycle_managers import HintLifecycleMgr
from gui.battle_control.battle_context_hints.settings_data_block import HintDataBlock
HintDescriptor = NamedTuple(b'HintDescriptor', [
 (
  b'priority', int),
 (
  b'hintId', str),
 (
  b'injectComponentAlias', Optional[str]),
 (
  b'hintView', Optional[Type[BattleContextHintsView]]),
 (
  b'hintPresenter', Optional[Type[BattleContextHintsViewPresenter]]),
 (
  b'activationTrigger', Optional[Type[HintActivationTrigger]]),
 (
  b'applyingTrigger', Optional[Type[HintApplyingTrigger]]),
 (
  b'hintLifecycleMgr', Optional[Type[HintLifecycleMgr]]),
 (
  b'dataBlock', HintDataBlock),
 (
  b'soundEvent', Optional[str]),
 (
  b'delay', float),
 (
  b'duration', float),
 (
  b'maxWatchingQty', int),
 (
  b'maxWatchingQtyPerBattle', int),
 (
  b'battlesCooldown', int)])
