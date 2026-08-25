from __future__ import absolute_import
import typing
from frameworks.wulf import ViewModel
from py2to3 import patched_typing
TViewModel = typing.TypeVar(b'TViewModel', bound=ViewModel)

class BaseSubModelView(patched_typing.Generic[TViewModel], object):
    __slots__ = (b'_viewModel', b'_isLoaded')

    def __init__(self, viewModel):
        self._viewModel = viewModel
        self._isLoaded = False
        return

    def isLoaded(self):
        return self._isLoaded

    def onLoading(self, *args, **kwargs):
        self._isLoaded = True
        return

    def initialize(self, *args, **kwargs):
        self._addListeners()
        return

    def update(self, *args, **kwargs):
        return

    def finalize(self):
        self._removeListeners()
        self._viewModel = None
        return

    def _addListeners(self):
        return

    def _removeListeners(self):
        return
