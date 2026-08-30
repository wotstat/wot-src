from constants import IS_VS_EDITOR
from visual_script import ASPECT
from visual_script.block import Block, Meta, InitParam, buildStrKeysValue
from visual_script.dictionary_blocks import Dictionary
from visual_script.misc import errorVScript, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE, arrayOf
from visual_script.tunable_event_block import TunableEventBlock
if not IS_VS_EDITOR:
    import Windowing
    from helpers import dependency
    from skeletons.account_helpers.settings_core import ISettingsCore

class GameSettingsMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 32767

    @classmethod
    def blockCategory(cls):
        return b'Game Settings'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/automation'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR]


class GetGameSetting(Block, GameSettingsMeta):
    _settingTypes = {b'bool': (
               SLOT_TYPE.BOOL, bool, None), 
       b'int': (
              SLOT_TYPE.INT, int, None), 
       b'str': (
              SLOT_TYPE.STR, str, None), 
       b'dict': (
               SLOT_TYPE.DICTIONARY, dict, Dictionary)}

    def __init__(self, *args, **kwargs):
        super(GetGameSetting, self).__init__(*args, **kwargs)
        self._name = self._makeDataInputSlot(b'settingName', SLOT_TYPE.STR)
        _settingType, = self._getInitParams()
        self._slotType, self._class, self._convertor = self._settingTypes[_settingType]
        self._value = self._makeDataOutputSlot(b'value', self._slotType, self._getValue)
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Game Setting Type', SLOT_TYPE.STR, buildStrKeysValue(*cls._settingTypes.keys()), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def _getValue(self):
        settings = dependency.instance(ISettingsCore)
        value = settings.getSetting(self._name.getValue())
        if isinstance(value, self._class):
            self._value.setValue(self._convertor(value) if self._convertor else value)
        else:
            errorVScript(self, (b'Incorrect type of the game setting value, {} expected ').format(self._class))
        return


class OnGameSettingsChanged(TunableEventBlock, GameSettingsMeta):
    _EVENT_SLOT_NAMES = [
     b'onChanged']
    settingsCore = (IS_VS_EDITOR or dependency.descriptor)(ISettingsCore) if 1 else None

    def __init__(self, *args, **kwargs):
        super(OnGameSettingsChanged, self).__init__(*args, **kwargs)
        self._settings = self._makeDataOutputSlot(b'settings', arrayOf(SLOT_TYPE.STR), None)
        self._lastSettings = {}
        return

    def onStartScript(self):
        self.settingsCore.onSettingsChanged += self._onSettingsChanged
        return

    def onFinishScript(self):
        self.settingsCore.onSettingsChanged -= self._onSettingsChanged
        return

    def _onSettingsChanged(self, diff):
        res = [name for name, value in diff.iteritems() if name not in self._lastSettings or value != self._lastSettings[name]]
        self._lastSettings.update(diff)
        if res:
            self._callOutput(res)
        return

    @TunableEventBlock.eventProcessor
    def _callOutput(self, res):
        self._settings.setValue(res)
        return


class OnWindowAccessibilityChanged(Block, GameSettingsMeta):

    def __init__(self, *args, **kwargs):
        super(OnWindowAccessibilityChanged, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._isAccessible = self._makeDataOutputSlot(b'isAccessible', SLOT_TYPE.BOOL, None)
        return

    def onStartScript(self):
        Windowing.addWindowAccessibilitynHandler(self._onWindowAccessibilityChanged)
        return

    def onFinishScript(self):
        Windowing.removeWindowAccessibilityHandler(self._onWindowAccessibilityChanged)
        return

    def _onWindowAccessibilityChanged(self, isWindowAccessible):
        self._isAccessible.setValue(isWindowAccessible)
        self._out.call()
        return
