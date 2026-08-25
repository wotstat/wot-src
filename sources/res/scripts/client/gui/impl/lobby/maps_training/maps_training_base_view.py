from gui.impl.pub import ViewImpl
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from frameworks.wulf import ViewSettings, ViewFlags
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader

class MapsTrainingBaseView(ViewImpl):
    appLoader = dependency.descriptor(IAppLoader)
    _BACKGROUND_ALPHA = 0

    def __init__(self, viewResource, viewModel, *args, **kwargs):
        settings = ViewSettings(viewResource)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = viewModel
        settings.args = args
        settings.kwargs = kwargs
        super(MapsTrainingBaseView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(MapsTrainingBaseView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(MapsTrainingBaseView, self)._initialize(*args, **kwargs)
        app = self.appLoader.getApp()
        app.setBackgroundAlpha(self._BACKGROUND_ALPHA)
        return

    def _onLoading(self, *args, **kwargs):
        super(MapsTrainingBaseView, self)._onLoading(*args, **kwargs)
        self._addListeners()
        return

    def _finalize(self):
        self._removeListeners()
        super(MapsTrainingBaseView, self)._finalize()
        return

    def _addListeners(self):
        self.viewModel.onMoveSpace += self._onMoveSpace
        self.viewModel.onMouseOver3dScene += self._onMouseOver3dScene
        return

    def _removeListeners(self):
        self.viewModel.onMoveSpace -= self._onMoveSpace
        self.viewModel.onMouseOver3dScene -= self._onMouseOver3dScene
        return

    def _onMoveSpace(self, args=None):
        if args is None:
            return
        else:
            ctx = {b'dx': (args.get(b'dx')), b'dy': (args.get(b'dy')), b'dz': (args.get(b'dz'))}
            g_eventBus.handleEvent(CameraRelatedEvents(CameraRelatedEvents.LOBBY_VIEW_MOUSE_MOVE, ctx=ctx), EVENT_BUS_SCOPE.GLOBAL)
            g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_SPACE_MOVED, ctx=ctx), EVENT_BUS_SCOPE.GLOBAL)
            return

    def _onMouseOver3dScene(self, args):
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_OVER_3DSCENE, ctx={b'isOver3dScene': (bool(args.get(b'isOver3dScene')))}))
        return
