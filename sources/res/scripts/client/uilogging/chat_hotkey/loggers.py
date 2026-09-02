from uilogging.base.logger import MetricsLogger
from uilogging.chat_hotkey.constants import FEATURE, ChatHotkeyLogActions

class ChatHotkeyLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(ChatHotkeyLogger, self).__init__(FEATURE)
        return

    def logHotkeyClicked(self, action, info):
        self.log(action=action, item=ChatHotkeyLogActions.HOTKEY_CLICKED, info=info)
        return

    def logCommandSelected(self, action, info):
        self.log(action=action, item=ChatHotkeyLogActions.COMMAND_SELECTED, info=info)
        return
