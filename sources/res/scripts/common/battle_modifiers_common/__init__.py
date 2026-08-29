import pkgutil
from ExtensionsManager import g_extensionsManager
from battle_modifiers import BattleParams, ModifiersContext, EXT_DATA_MODIFIERS_KEY
if b'battle_modifiers' in [ext.name for ext in g_extensionsManager.activeExtensions] and pkgutil.find_loader(b'battle_modifiers_ext'):
    from battle_modifiers_ext.battle_modifiers import BattleModifiers, getGlobalModifiers
else:
    from battle_modifiers import BattleModifiers, getGlobalModifiers
__all__ = (b'EXT_DATA_MODIFIERS_KEY', b'BattleParams', b'BattleModifiers', b'ModifiersContext', b'getGlobalModifiers')
