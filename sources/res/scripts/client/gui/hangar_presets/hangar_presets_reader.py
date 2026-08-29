import ResMgr
from gui.hangar_presets.hangar_gui_config import HangarGuiPreset, HangarGuiSettings, PresetSettings
from soft_exception import SoftException
_ERR_TEMPLATE = b"[HangarGUI] {} in the preset '{}'"

class IPresetReader(object):

    @classmethod
    def readConfig(cls, fullConfig):
        raise NotImplementedError
        return

    @staticmethod
    def isDefault():
        raise NotImplementedError
        return


class DefaultPresetReader(IPresetReader):
    _CONFIG_PATH = b'gui/hangar_gui_presets.xml'

    @classmethod
    def readConfig(cls, fullConfig):
        return cls.__readGuiHangarConfig(cls._CONFIG_PATH, fullConfig)

    @staticmethod
    def isDefault():
        return True

    @classmethod
    def _getPreset(cls, presetName, config):
        return presetName

    @classmethod
    def _updateItems(cls, items, queueType, preset):
        items[queueType] = preset
        return

    @classmethod
    def __readComponents(cls, config, presetName):
        shownComponents = {}
        hiddenComponents = {}
        for name, section in config.items():
            if name != b'component':
                raise SoftException(_ERR_TEMPLATE.format(b'Wrong section', presetName))
            if not section.has_key(b'name'):
                raise SoftException(_ERR_TEMPLATE.format(b'Missing component name', presetName))
            name = section[b'name'].asString
            if not section.has_key(b'name'):
                raise SoftException(_ERR_TEMPLATE.format(b'Missing component visibility', presetName))
            isVisible = section[b'visible'].asBool
            isChangeable = section.readBool(b'isChangeable')
            componentType = section[b'type'].asString if section.has_key(b'type') else None
            layout = section[b'layout'].asString if section.has_key(b'layout') else None
            targetComponents = shownComponents if isVisible else hiddenComponents
            targetComponents[name] = PresetSettings(componentType, layout, isChangeable)

        return HangarGuiPreset(shownComponents, hiddenComponents)

    @classmethod
    def __readGuiHangarConfig(cls, configPath, fullConfig):
        config = ResMgr.openSection(configPath)
        if config is None:
            raise SoftException((b'[HangarGUI] Cannot open or read config {}').format(configPath))
        presets = {}
        if config.has_key(b'presets'):
            presets = cls.__readPresets(config[b'presets'], fullConfig)
        if not config.has_key(b'queueTypePresets'):
            raise SoftException((b'[HangarGUI] Missing queueTypePresets section in the config').format(configPath))
        queueTypePresets = cls.__readPresetsForQueueTypes(config[b'queueTypePresets'])
        return HangarGuiSettings(presets, queueTypePresets)

    @classmethod
    def __readPresets(cls, config, fullConfig):
        presets = {}
        for name, subSection in config.items():
            if name != b'preset':
                raise SoftException(b'[HangarGUI] Invalid preset section')
            if not subSection.has_key(b'name'):
                raise SoftException(b'[HangarGUI] Missing preset name')
            presetName = subSection[b'name'].asString
            if not subSection.has_key(b'components'):
                raise SoftException(_ERR_TEMPLATE.format(b'Missing components section', presetName))
            components = cls.__readComponents(subSection[b'components'], presetName)
            if subSection.has_key(b'basePreset'):
                basePresetName = subSection[b'basePreset'].asString
                basePreset = presets.get(basePresetName) or fullConfig.presets.get(basePresetName)
                if basePreset is None:
                    raise SoftException(_ERR_TEMPLATE.format(b'Invalid base preset', presetName))
                components = cls.__updateComponents(basePreset, components)
            presets[presetName] = components

        return presets

    @classmethod
    def __readPresetsForQueueTypes(cls, config):
        items = {}
        for name, subSection in config.items():
            if name != b'item':
                raise SoftException(b'[HangarGUI] Invalid item section in queueTypePresets section')
            if not subSection.has_key(b'queueType'):
                raise SoftException(b'[HangarGUI] Missing queueType in queueTypePresets section')
            queueType = subSection[b'queueType'].asInt
            if not subSection.has_key(b'presetName'):
                raise SoftException(b'[HangarGUI] Missing preset name in queueTypePresets section')
            presetName = subSection[b'presetName'].asString
            preset = cls._getPreset(presetName, subSection)
            cls._updateItems(items, queueType, preset)

        return items

    @staticmethod
    def __updateComponents(baseComponents, override):
        baseVisibleComponents = baseComponents.visibleComponents.copy()
        baseHiddenComponents = baseComponents.hiddenComponents.copy()
        for compName, compSettings in override.visibleComponents.items():
            if compName in baseHiddenComponents:
                del baseHiddenComponents[compName]
            baseVisibleComponents[compName] = compSettings

        for compName, compSettings in override.hiddenComponents.items():
            if compName in baseVisibleComponents:
                del baseVisibleComponents[compName]
            baseHiddenComponents[compName] = compSettings

        return HangarGuiPreset(baseVisibleComponents, baseHiddenComponents)


class DefaultSubPresetReader(DefaultPresetReader):
    _SUB_TYPES_KEY = b'subTypes'

    @staticmethod
    def isDefault():
        return False

    @classmethod
    def _getPreset(cls, presetName, config):
        if not config.has_key(cls._SUB_TYPES_KEY):
            raise SoftException((b'Missing {} section for {}').format(cls._SUB_TYPES_KEY, cls._CONFIG_PATH))
        return {subType: presetName for subType in map(int, config[cls._SUB_TYPES_KEY].asString.split())}

    @classmethod
    def _updateItems(cls, items, queueType, preset):
        presets = items.get(queueType, {})
        if not presets:
            items[queueType] = preset
        else:
            items[queueType].update(preset)
        return


class SpecBattlePresetReader(DefaultSubPresetReader):
    _CONFIG_PATH = b'gui/hangar_gui_spec_presets.xml'
    _SUB_TYPES_KEY = b'guiTypes'
