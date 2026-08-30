from __future__ import absolute_import
from gui.Scaleform.daapi import LobbySubView
from hangar_selectable_objects import ISelectableLogicCallback, HangarSelectableLogic

class LobbySelectableView(LobbySubView, ISelectableLogicCallback):

    def __init__(self, ctx=None):
        super(LobbySelectableView, self).__init__(ctx)
        self.__selectableLogic = None
        return

    def onHighlight3DEntity(self, entity):
        self._highlight3DEntityAndShowTT(entity)
        return

    def onFade3DEntity(self, entity):
        self._fade3DEntityAndHideTT(entity)
        return

    def _populate(self):
        super(LobbySelectableView, self)._populate()
        self._activateSelectableLogic()
        return

    def _dispose(self):
        self._deactivateSelectableLogic()
        super(LobbySelectableView, self)._dispose()
        return

    def _highlight3DEntityAndShowTT(self, entity):
        return

    def _fade3DEntityAndHideTT(self, entity):
        return

    def _activateSelectableLogic(self):
        if self.__selectableLogic is not None:
            return
        else:
            self.__selectableLogic = self._createSelectableLogic()
            self.__selectableLogic.init(self)
            return

    def _deactivateSelectableLogic(self):
        if self.__selectableLogic is not None:
            self.__selectableLogic.fini()
            self.__selectableLogic = None
        return

    def _createSelectableLogic(self):
        return HangarSelectableLogic()
