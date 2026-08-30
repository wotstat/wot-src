from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.transitions import ToStateTransition
from pve_battle_hud import SecondaryObjectiveState

class ToAppearanceTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToAppearanceTransition, self).__init__(SecondaryObjectiveState.APPEARANCE, priority=2)
        return


class ToRestoredTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToRestoredTransition, self).__init__(SecondaryObjectiveState.RESTORED, priority=2)
        return


class ToRegularTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToRegularTransition, self).__init__(SecondaryObjectiveState.REGULAR, priority=2)
        return


class ToCountdownTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToCountdownTransition, self).__init__(SecondaryObjectiveState.COUNTDOWN, priority=2)
        return


class ToSuccessTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToSuccessTransition, self).__init__(SecondaryObjectiveState.SUCCESS, priority=1)
        return


class ToFailureTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToFailureTransition, self).__init__(SecondaryObjectiveState.FAILURE, priority=1)
        return


class ToDisappearanceTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToDisappearanceTransition, self).__init__(SecondaryObjectiveState.DISAPPEARANCE, priority=1)
        return


class ToHiddenTransition(ToStateTransition):
    __slots__ = ()

    def __init__(self):
        super(ToHiddenTransition, self).__init__(SecondaryObjectiveState.HIDDEN, priority=0)
        return
