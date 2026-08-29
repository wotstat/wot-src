from collections import namedtuple
import typing
if typing.TYPE_CHECKING:
    from gui.hangar_presets.hangar_presets_reader import IPresetReader
_HANGAR_GUI_CONFIG = None
HangarGuiSettings = namedtuple(b'HangarGuiSettings', (b'presets', b'modes'))
HangarGuiPreset = namedtuple(b'HangarGuiPreset', (b'visibleComponents', b'hiddenComponents'))
PresetSettings = namedtuple(b'PresetSettings', (b'type', b'layout', b'isChangeable'))

def _updateConfig(fullConfig, config):
    presets = {}
    presetsForQueueTypes = {}
    for c in [fullConfig, config]:
        presets.update(c.presets)
        presetsForQueueTypes.update(c.modes)

    return HangarGuiSettings(presets, presetsForQueueTypes)


def getHangarGuiConfig(readers):
    global _HANGAR_GUI_CONFIG
    if _HANGAR_GUI_CONFIG is None:
        fullConfig = HangarGuiSettings({}, {})
        for reader in readers:
            config = reader.readConfig(fullConfig)
            fullConfig = _updateConfig(fullConfig, config)

        _HANGAR_GUI_CONFIG = fullConfig
    return _HANGAR_GUI_CONFIG
