from enum import Enum
FEATURE = b'chat_hotkey'

class ChatHotkeyLogActions(Enum):
    HOTKEY_CLICKED = b'hotkey_clicked'
    COMMAND_SELECTED = b'command_selected'
