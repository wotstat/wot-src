from frameworks.wulf import ViewModel

class EventTypes(ViewModel):
    __slots__ = ()
    BATTLE_QUEST = b'battleQuest'
    RESEARCH_VEHICLE = b'researchVehicle'
    RESEARCH_MODULE = b'researchModule'
    CREW_MEMBER_NEW_SKILL = b'crewMemberNewSkill'
    PERSONAL_MISSION = b'personalQuest'
    DAILY_QUEST = b'dailyQuest'
    RANKED_BATTLES = b'rankedBattles'
    BATTLE_PASS = b'battlePass'

    def __init__(self, properties=0, commands=0):
        super(EventTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EventTypes, self)._initialize()
        return
