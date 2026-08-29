from gui.shared.event_bus import SharedEvent

class WinbackViewEvent(SharedEvent):
    WINBACK_REWARD_VIEW_LOADED = b'onWinbackRewardViewLoad'
    WINBACK_REWARD_VIEW_CLOSED = b'onWinbackRewardViewClosed'
