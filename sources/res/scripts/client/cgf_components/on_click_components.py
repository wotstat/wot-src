import logging, CGF
from GenericComponents import VSEComponent
from adisp import adisp_process
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
from cgf_script.managers_registrator import autoregister, onAddedQuery, onRemovedQuery
from constants import MarathonConfig, IS_CLIENT
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared.utils import IHangarSpace
from skeletons.gui.game_control import IExternalLinksController
from hover_component import IsHoveredComponent, SelectionComponent, IsExternalHoveredComponent
if IS_CLIENT:
    from gui.impl import backport
    from gui.impl.gen import R
    from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
    from gui.game_control.links import URLMacros
    from gui.shared.event_dispatcher import showBrowserOverlayView, showCollectionWindow
_logger = logging.getLogger(__name__)

@registerComponent
class OpenBrowserOnClickComponent(object):
    domain = CGF.DomainOption.DomainClient
    urlProvider = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'url provider', value=b'MARATHON_VIDEO_URL_PROVIDER')

    def __init__(self):
        super(OpenBrowserOnClickComponent, self).__init__()
        self.__urlParser = URLMacros()
        return

    def doAction(self):
        self.__openBrowser()
        return

    @adisp_process
    def __openBrowser(self):
        getterFunc = URL_PROVIDERS[self.urlProvider]
        unparsedUrl = getterFunc()
        url = yield self.__urlParser.parse(unparsedUrl)
        showBrowserOverlayView(url, alias=VIEW_ALIAS.BROWSER_OVERLAY)
        return


@registerComponent
class OpenExternalBrowserOnClickComponent(object):
    domain = CGF.DomainOption.DomainClient
    url = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'url', value=b'')

    def doAction(self):
        self.__openBrowser()
        return

    def __openBrowser(self):
        linkCtrl = dependency.instance(IExternalLinksController)
        linkCtrl.open(self.url)
        return


def getMarathonVideoUrl():
    lobbyContext = dependency.instance(ILobbyContext)
    return lobbyContext.getServerSettings().getMarathonConfig()[MarathonConfig.VIDEO_CONTENT_URL]


URL_PROVIDERS = {b'MARATHON_VIDEO_URL_PROVIDER': getMarathonVideoUrl}

@registerComponent
class OpenCollectionOnClickComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = b'Open collections on Click'
    collectionID = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'collection Id')

    def doAction(self):
        if self.collectionID:
            backText = backport.text(R.strings.menu.viewHeader.backBtn.descrLabel.hangar())
            showCollectionWindow(self.collectionID, backBtnText=backText)
        return


@autoregister(presentInAllWorlds=False, category=b'lobby')
class ClientSelectableComponentsManager(CGF.ComponentManager):

    @onAddedQuery(OpenBrowserOnClickComponent, SelectionComponent)
    def handleOpenBrowserOnClickAdded(self, openBrowserOnClickComponent, selectionComponent):
        selectionComponent.onClickAction += openBrowserOnClickComponent.doAction
        return

    @onRemovedQuery(OpenBrowserOnClickComponent, SelectionComponent)
    def handleOpenBrowserOnClickRemoved(self, openBrowserOnClickComponent, selectionComponent):
        selectionComponent.onClickAction -= openBrowserOnClickComponent.doAction
        return

    @onAddedQuery(OpenExternalBrowserOnClickComponent, SelectionComponent)
    def handleOpenExternalBrowserOnClickAdded(self, openExtBrowserOnClickComp, selectionComponent):
        selectionComponent.onClickAction += openExtBrowserOnClickComp.doAction
        return

    @onRemovedQuery(OpenExternalBrowserOnClickComponent, SelectionComponent)
    def handleOpenExternalBrowserOnClickRemoved(self, openExtBrowserOnClickComp, selectionComponent):
        selectionComponent.onClickAction -= openExtBrowserOnClickComp.doAction
        return

    @onAddedQuery(OpenCollectionOnClickComponent, SelectionComponent)
    def handleOpenCollectionOnClickAdded(self, openCollectionOnClickComponent, selectionComponent):
        selectionComponent.onClickAction += openCollectionOnClickComponent.doAction
        return

    @onRemovedQuery(OpenCollectionOnClickComponent, SelectionComponent)
    def handleOpenCollectionOnClickRemoved(self, openCollectionOnClickComponent, selectionComponent):
        selectionComponent.onClickAction -= openCollectionOnClickComponent.doAction
        return


@autoregister(presentInAllWorlds=True, category=b'lobby')
class ClickVSEComponentsManager(CGF.ComponentManager):

    @onAddedQuery(SelectionComponent, VSEComponent)
    def handleComponentAdded(self, selectionComponent, vseComponent):
        selectionComponent.onClickAction += vseComponent.context.onGameObjectClick
        return

    @onRemovedQuery(SelectionComponent, VSEComponent)
    def handleComponentRemoved(self, selectionComponent, vseComponent):
        selectionComponent.onClickAction -= vseComponent.context.onGameObjectClick
        return


class ClickManager(CGF.ComponentManager):
    _hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, *args):
        super(ClickManager, self).__init__(*args)
        self._selectedGO = None
        return

    def activate(self):
        self._hangarSpace.onMouseDown += self._onMouseDown
        self._hangarSpace.onMouseUp += self._onMouseUp
        return

    def deactivate(self):
        self._hangarSpace.onMouseDown -= self._onMouseDown
        self._hangarSpace.onMouseUp -= self._onMouseUp
        return

    def _onMouseDown(self):
        clickQuery = CGF.Query(self.spaceID, (CGF.GameObject, IsHoveredComponent, SelectionComponent, CGF.No(IsExternalHoveredComponent)))
        for go, _, __ in clickQuery:
            self._selectedGO = go

        return

    def _onMouseUp(self):
        if self._hangarSpace.space is None:
            return
        else:
            clickQuery = CGF.Query(self.spaceID, (CGF.GameObject, IsHoveredComponent, SelectionComponent, CGF.No(IsExternalHoveredComponent)))
            for go, _, selectionComponent in clickQuery:
                if self._selectedGO == go:
                    _logger.info(b'ClickManager::Clicked')
                    selectionComponent.onClickAction()

            return
