from __future__ import absolute_import
import pkgutil
from ExtensionsManager import g_extensionsManager
from battle_modifiers_common.battle_modifiers import BattleParams, ModifiersContext, ConstantsSet, ModifierScope, EXT_DATA_MODIFIERS_KEY, BATTLE_MODIFIERS_TYPE
if b'battle_modifiers' in [ext.name for ext in g_extensionsManager.activeExtensions] and pkgutil.find_loader(b'battle_modifiers_ext'):
    from battle_modifiers_ext.battle_modifiers import BattleModifiers, getDevGlobalModifiers
else:
    from battle_modifiers_common.battle_modifiers import BattleModifiers, getDevGlobalModifiers
__all__ = (b'EXT_DATA_MODIFIERS_KEY', b'BATTLE_MODIFIERS_TYPE', b'BattleParams', b'ModifierScope', b'BattleModifiers', b'ModifiersContext', b'getDevGlobalModifiers')
