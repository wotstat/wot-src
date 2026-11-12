from gui.shared.events import HasCtxEvent

class NewYearEvent(HasCtxEvent):
    ON_BREAK_TOYS_FILTER_APPLIED = b'newYear/onBreakToysFilterApplied'
    ON_BREAK_TOYS_ANIMATION_COMPLETED = b'newYear/onBreakToysAnimationCompleted'
    ON_PRE_SWITCH_VIEW = b'newYear/onPreSwitchView'
    ON_SWITCH_VIEW = b'newYear/onSwitchView'
    ON_SIDEBAR_SELECTED = b'newYear/onSidebarSelected'
    SELECT_SIDEBAR_TAB_OUTSIDE = b'newYear/selectSidebarTabOutside'
    UPDATE_BACK_BUTTON = b'newYear/updateBackButton'
    ON_TOY_INSTALLED = b'newYear/onToyInstalled'
