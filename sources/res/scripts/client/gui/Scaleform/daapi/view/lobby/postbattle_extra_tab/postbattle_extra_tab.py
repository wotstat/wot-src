from frameworks.wulf import ViewFlags
from debug_utils import LOG_ERROR, LOG_WARNING
from gui.impl.pub import ViewImpl
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.daapi.view.meta.PostbattleExtraTabMeta import PostbattleExtraTabMeta

class PostbattleExtraTab(InjectComponentAdaptor, PostbattleExtraTabMeta):
    __injectionView = None

    @classmethod
    def overrideInjectionView(cls, view):
        if not issubclass(view, PostbattleExtraTabView):
            LOG_ERROR(b'Parameter is not a subclass of ViewImpl', view)
            return
        cls.__injectionView = view
        return

    @classmethod
    def deleteInjectionView(cls):
        cls.__injectionView = None
        return

    def _makeInjectView(self):
        if self.__injectionView:
            return self.__injectionView(flags=ViewFlags.VIEW)
        LOG_WARNING(b'Nothing to inject to PostbattleExtraTab.')
        return

    def updateQuestsInfo(self, arenaUniqueID):
        view = self.getInjectView()
        if view:
            view.onArenaInfoUpdated(arenaUniqueID)
        return

    @classmethod
    def isInjectionView(cls, view):
        return cls.__injectionView == view

    @classmethod
    def hasInjectionView(cls):
        return bool(cls.__injectionView)


class PostbattleExtraTabView(ViewImpl):

    def onArenaInfoUpdated(self, arenaUniqueID):
        raise NotImplementedError
        return
