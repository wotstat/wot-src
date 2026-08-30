import logging, typing
from frameworks.wulf import ViewSettings
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.platoon.chat_message_model import ChatMessageModel
from gui.impl.pub.view_impl import ViewImpl
from helpers import dependency
from messenger import g_settings
from messenger.formatters import TimeFormatter
from messenger.formatters.chat_message import LobbyMessageBuilder
from messenger.gui.gameface.view.gf_channel_view_interface import GFChannelViewInterface
from skeletons.gui.game_control import IPlatoonController, IAnonymizerController
from gui.impl.gen.view_models.views.lobby.platoon.chat_model import ChatModel
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from messenger.proto.bw_chat2.wrappers import UnitMessageVO
    from messenger.gui.gameface.channels import GFChannelController
_R_SQUAD = R.strings.messenger.dialogs.squadChannel

class ChatSubview(ViewImpl, GFChannelViewInterface):
    __platoonCtrl = dependency.descriptor(IPlatoonController)
    __anonymizerController = dependency.descriptor(IAnonymizerController)

    def __init__(self):
        settings = ViewSettings(layoutID=R.views.lobby.platoon.subViews.Chat(), model=ChatModel())
        super(ChatSubview, self).__init__(settings)
        self.__messageCount = 0
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def onChannelControllerInited(self, channelCtrl):
        if channelCtrl is not None and not self.__platoonCtrl.isPlayerRoleAutoSearch():
            self.__clearMessages()
            messagesCache = channelCtrl.getHistory()
            for msg in messagesCache:
                self.__addMessage(msg)

        return

    def addMessageToView(self, message, isHistoryMessage=False):
        if not isHistoryMessage or not self.__platoonCtrl.isPlayerRoleAutoSearch():
            self.__addMessage(message)
        return not self.getParentWindow().isHidden()

    def _initialize(self, *args, **kwargs):
        self.__updateHeaderText()
        self.__addListeners()
        self.viewModel.setCanClearInput(False)
        return

    def _onLoading(self, *args, **kwargs):
        channelCtrl = self.__platoonCtrl.getChannelController()
        if channelCtrl is not None:
            channelCtrl.addToSubscribedList(self)
        else:
            _logger.warning(b'no controller available at the end of initialize')
        return

    def _finalize(self):
        self.__removeListeners()
        channelCtrl = self.__platoonCtrl.getChannelController()
        if channelCtrl is not None:
            channelCtrl.removeFromSubscribedList(self)
        return

    def __clearMessages(self):
        with self.viewModel.transaction() as model:
            messagesArray = model.getMessages()
            messagesArray.clear()
            self.__messageCount = 0
        return

    def __addMessage(self, message):
        with self.viewModel.transaction() as model:
            messagesArray = model.getMessages()
            guiType = LobbyMessageBuilder().setGuiType(message.accountDBID).getGuiType()
            colorScheme = g_settings.getColorScheme(b'rosters')
            msgModel = ChatMessageModel()
            msgModel.text.setText(message.text)
            msgModel.text.setColor(colorScheme.getHexStr(b'squad_message'))
            msgModel.playerName.setText(message.accountName)
            msgModel.playerName.setColor(colorScheme.getHexStr(guiType))
            if message.sentAt:
                msgModel.timeStamp.setText(TimeFormatter.getMessageTimeFormat(message.sentAt))
            msgModel.timeStamp.setColor(colorScheme.getHexStr(guiType))
            msgModel.setKey(self.__messageCount)
            self.__messageCount += 1
            messagesArray.addViewModel(msgModel)
            messagesArray.invalidate()
        return

    def __addListeners(self):
        self.viewModel.onSend += self.__onSend
        self.viewModel.onInputCleared += self.__onInputCleared
        self.__platoonCtrl.onChannelControllerChanged += self.__onChannelControllerChanged
        self.__anonymizerController.onStateChanged += self.__onAnonymizerStateChanged
        return

    def __removeListeners(self):
        self.viewModel.onSend -= self.__onSend
        self.viewModel.onInputCleared -= self.__onInputCleared
        self.__platoonCtrl.onChannelControllerChanged -= self.__onChannelControllerChanged
        self.__anonymizerController.onStateChanged -= self.__onAnonymizerStateChanged
        return

    def __onChannelControllerChanged(self, channelController):
        channelController.addToSubscribedList(self)
        return

    def __onSend(self, *args, **kwargs):
        channelCtrl = self.__platoonCtrl.getChannelController()
        if channelCtrl is not None and args[0][b'message'] is not None:
            if channelCtrl.sendMessage(args[0][b'message']):
                with self.viewModel.transaction() as model:
                    model.setCanClearInput(True)
        return

    def __onInputCleared(self):
        with self.viewModel.transaction() as model:
            model.setCanClearInput(False)
        return

    def __updateHeaderText(self):
        colorScheme = g_settings.getColorScheme(b'battle/message')
        userAnonymized = self.__anonymizerController.isAnonymized
        anonymizerInfoText = backport.text(_R_SQUAD.simpleChatAlert.anonymizer()) if userAnonymized else b''
        self.viewModel.headerExtraInfo.setText(anonymizerInfoText)
        self.viewModel.headerExtraInfo.setColor(colorScheme.getHexStr(b'alert'))
        return

    def __onAnonymizerStateChanged(self, **_):
        self.__updateHeaderText()
        return
