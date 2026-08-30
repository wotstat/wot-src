from visual_script.block import Block, Meta
from visual_script.slot_types import SLOT_TYPE
from visual_script.misc import ASPECT
from visual_script.dependency import dependencyImporter
events, dependency, guiShared, views, browserView, skeletons, WWISE = dependencyImporter(b'gui.shared.events', b'helpers.dependency', b'gui.shared', b'gui.Scaleform.daapi.settings.views', b'gui.Scaleform.daapi.view.lobby.hangar.BrowserView', b'skeletons.gui.game_control', b'WWISE')

class WebMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 8388607

    @classmethod
    def blockCategory(cls):
        return b'Web'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR]


class OpenWebLinkFullScreen(Block, WebMeta):
    __HANGAR_SOUND_FILTERED_STATE_NAME = b'STATE_hangar_filtered'
    __HANGAR_SOUND_FILTERED_STATE_ON = b'STATE_hangar_filtered_on'
    __HANGAR_SOUND_FILTERED_STATE_OFF = b'STATE_hangar_filtered_off'
    __browserCtrl = dependency.descriptor(skeletons.IBrowserController)

    def __init__(self, *args, **kwargs):
        super(OpenWebLinkFullScreen, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._exec)
        self._url = self._makeDataInputSlot(b'url', SLOT_TYPE.STR)
        self._filterSounds = self._makeDataInputSlot(b'filterSounds', SLOT_TYPE.BOOL)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def filterSoundsOn(self, browserId):
        if browserId == views.VIEW_ALIAS.BROWSER_OVERLAY:
            if self._filterSounds.getValue():
                WWISE.WW_setState(self.__HANGAR_SOUND_FILTERED_STATE_NAME, self.__HANGAR_SOUND_FILTERED_STATE_ON)
            self.__browserCtrl.onBrowserAdded -= self.filterSoundsOn
        return

    def filterSoundsOff(self, browserId):
        if browserId == views.VIEW_ALIAS.BROWSER_OVERLAY:
            if self._filterSounds.getValue():
                WWISE.WW_setState(self.__HANGAR_SOUND_FILTERED_STATE_NAME, self.__HANGAR_SOUND_FILTERED_STATE_OFF)
            self.__browserCtrl.onBrowserDeleted -= self.filterSoundsOff
        return

    def onFinishScript(self):
        self.__browserCtrl.onBrowserAdded -= self.filterSoundsOn
        self.__browserCtrl.onBrowserDeleted -= self.filterSoundsOff
        return

    def _exec(self):
        self.__browserCtrl.onBrowserAdded += self.filterSoundsOn
        self.__browserCtrl.onBrowserDeleted += self.filterSoundsOff
        guiShared.event_dispatcher.showBrowserOverlayView(self._url.getValue(), alias=views.VIEW_ALIAS.BROWSER_OVERLAY)
        self._out.call()
        return
