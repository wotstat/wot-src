import logging
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
_logger = logging.getLogger(__name__)

class HintInjectComponent(InjectComponentAdaptor):

    def _populate(self):
        super(HintInjectComponent, self)._populate()
        self.hideHint()
        return

    def _onPopulate(self):
        raise NotImplementedError
        return

    def setInjectView(self, viewClass):
        if not isinstance(self.getInjectView(), viewClass):
            self._destroyInjected()
            self._createInjectView(viewClass)
        return

    def showHint(self, *args):
        raise NotImplementedError
        return

    def hideHint(self):
        raise NotImplementedError
        return

    def _makeInjectView(self, viewClass):
        _logger.debug(b'[BATTLE_CONTEXT_INTS] HintInjectComponent._makeInjectView componentClass=%s', viewClass)
        return viewClass()
