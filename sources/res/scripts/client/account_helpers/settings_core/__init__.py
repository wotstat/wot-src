from skeletons.account_helpers.settings_core import ISettingsCache, ISettingsCore

def getSettingsCoreConfig(manager):
    from account_helpers.settings_core.SettingsCache import SettingsCache
    from account_helpers.settings_core.SettingsCore import SettingsCore
    cache = SettingsCache()
    manager.addInstance(ISettingsCache, cache, finalizer=b'fini')
    core = SettingsCore()
    manager.addInstance(ISettingsCore, core, finalizer=b'fini')
    cache.init()
    core.init()
    return


def longToInt32(value):
    if 2147483648L <= value <= 4294967295L:
        value &= 2147483647
        value = int(value)
        value = ~value
        value ^= 2147483647
    return value
