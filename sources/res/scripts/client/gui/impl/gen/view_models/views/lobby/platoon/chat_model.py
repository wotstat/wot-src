from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.chat_message_model import ChatMessageModel
from gui.impl.gen.view_models.views.lobby.platoon.chat_message_part_model import ChatMessagePartModel

class ChatModel(ViewModel):
    __slots__ = (b'onSend', b'onInputCleared')

    def __init__(self, properties=3, commands=2):
        super(ChatModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def headerExtraInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getHeaderExtraInfoType():
        return ChatMessagePartModel

    def getMessages(self):
        return self._getArray(1)

    def setMessages(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getMessagesType():
        return ChatMessageModel

    def getCanClearInput(self):
        return self._getBool(2)

    def setCanClearInput(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(ChatModel, self)._initialize()
        self._addViewModelProperty(b'headerExtraInfo', ChatMessagePartModel())
        self._addArrayProperty(b'messages', Array())
        self._addBoolProperty(b'canClearInput', False)
        self.onSend = self._addCommand(b'onSend')
        self.onInputCleared = self._addCommand(b'onInputCleared')
        return
