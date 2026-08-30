from frameworks.wulf import Map, ViewModel
from gui.impl.gen.view_models.views.lobby.page.footer.message_model import MessageModel

class ChatModel(ViewModel):
    __slots__ = (b'onViewMessageAction', b'onDeleteMessageAction', b'onWindowAnchorPositionUpdated', b'onChatsAction')

    def __init__(self, properties=1, commands=4):
        super(ChatModel, self).__init__(properties=properties, commands=commands)
        return

    def getMessages(self):
        return self._getMap(0)

    def setMessages(self, value):
        self._setMap(0, value)
        return

    @staticmethod
    def getMessagesType():
        return (unicode, MessageModel)

    def _initialize(self):
        super(ChatModel, self)._initialize()
        self._addMapProperty(b'messages', Map(unicode, MessageModel))
        self.onViewMessageAction = self._addCommand(b'onViewMessageAction')
        self.onDeleteMessageAction = self._addCommand(b'onDeleteMessageAction')
        self.onWindowAnchorPositionUpdated = self._addCommand(b'onWindowAnchorPositionUpdated')
        self.onChatsAction = self._addCommand(b'onChatsAction')
        return
