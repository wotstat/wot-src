from frameworks.wulf import ViewModel

class ModeSelectorTooltipsConstants(ViewModel):
    __slots__ = ()
    DISABLED_TOOLTIP = b'disabledTooltip'
    RANDOM_BP_PAUSED_TOOLTIP = b'randomBPPausedTooltip'
    RANKED_CALENDAR_DAY_INFO_TOOLTIP = b'rankedCalendarDayInfoExtended'
    RANKED_STEP_TOOLTIP = b'rankedStep'
    RANKED_BATTLES_RANK_TOOLTIP = b'rankedBattlesRank'
    RANKED_BATTLES_BONUS_TOOLTIP = b'rankedBattlesBonus'
    RANKED_BATTLES_LEAGUE_TOOLTIP = b'rankedBattlesLeague'
    RANKED_BATTLES_EFFICIENCY_TOOLTIP = b'rankedBattlesEfficiency'
    RANKED_BATTLES_POSITION_TOOLTIP = b'rankedBattlesPosition'
    CALENDAR_TOOLTIP = b'calendarTooltip'
    MAPBOX_CALENDAR_TOOLTIP = b'mapboxCalendar'
    EPIC_BATTLE_CALENDAR_TOOLTIP = b'epicBattleCalendarTooltip'
    EPIC_BATTLE_WIDGET_INFO = b'epicBattleWidgetInfo'
    FUN_RANDOM_CALENDAR_TOOLTIP = b'funRandomModeSelectorCalendarDay'
    FUN_RANDOM_REWARDS = b'funRandomRewards'
    NOT_SUITABLE_VEHICLES_TOOLTIP = b'notSuitableVehiclesTooltip'
    COMP7_CALENDAR_DAY_EXTENDED_INFO = b'comp7CalendarDayExtendedInfo'

    def __init__(self, properties=0, commands=0):
        super(ModeSelectorTooltipsConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ModeSelectorTooltipsConstants, self)._initialize()
        return
