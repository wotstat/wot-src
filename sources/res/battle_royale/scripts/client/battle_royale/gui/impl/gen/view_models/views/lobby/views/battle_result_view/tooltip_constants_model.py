from frameworks.wulf import ViewModel

class TooltipConstantsModel(ViewModel):
    __slots__ = ()
    ACHIEVEMENT_TOOLTIP = b'battleStatsAchievementData'
    QUEST_COMPLETE_TOOLTIP = b'QuestCompletedTooltip'
    BONUS_TOOLTIP = b'bonusTooltip'

    def __init__(self, properties=0, commands=0):
        super(TooltipConstantsModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TooltipConstantsModel, self)._initialize()
        return
