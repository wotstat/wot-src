import typing
from gui.impl.lobby.container_views.base.components import ComponentBase
if typing.TYPE_CHECKING:
    from typing import Any, Callable, Tuple
    from frameworks.wulf import ViewModel, ViewStatus
    from frameworks.wulf.gui_constants import ShowingStatus

class ExampleComponent(ComponentBase):

    def _getViewModel(self, vm):
        return vm.exampleComponent

    def _getEvents(self):
        return super(ExampleComponent, self)._getEvents() + (
         (
          self.viewModel.onMouseEnter, self._onMouseEnter),
         (
          self.viewModel.onMouseLeave, self._onMouseLeave))

    def _fillViewModel(self, vm):
        return

    def _onLoading(self, *args, **kwargs):
        return

    def _onLoaded(self, *args, **kwargs):
        return

    def _initialize(self, *args, **kwargs):
        return

    def _finalize(self):
        return

    def _onReady(self):
        return

    def _onShown(self):
        return

    def _onHidden(self):
        return

    def _onFocus(self, focused):
        return

    def _swapStates(self, oldStatus, newStatus):
        return

    def _swapShowingStates(self, oldStatus, newStatus):
        return

    def _subscribe(self):
        return

    def _unsubscribe(self):
        return

    def _onMouseEnter(self):
        self.events.onMouseEnter(self)
        return

    def _onMouseLeave(self):
        self.events.onMouseLeave(self)
        return
