import logging, typing
from .py_object_binder import PyObjectEntity
if typing.TYPE_CHECKING:
    from frameworks.wulf import ViewModel
    import Math
_logger = logging.getLogger(__name__)

class MarkersManager(PyObjectEntity):
    __slots__ = ()

    @classmethod
    def create(cls, proxy):
        manager = MarkersManager()
        manager.bind(proxy)
        return manager

    def addMarkerStatic(self, viewModel, worldPos):
        self.proxy.addMarkerStatic(viewModel, worldPos)
        return

    def addMarkerDynamic(self, viewModel, dataProvider):
        self.proxy.addMarkerDynamic(viewModel, dataProvider)
        return

    def removeMarker(self, viewModel):
        self.proxy.removeMarker(viewModel)
        return

    def clear(self):
        self.proxy.clear()
        return

    def destroy(self):
        if self.proxy is not None:
            self.proxy.clear()
        self.unbind()
        return
