from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.personal_mission_flags import PersonalMissionsFlag
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags import RankedQuestsFlag, ElenQuestsFlag, BattleQuestsFlag, MarathonQuestsFlag, MapboxQuestsFlag
from gui.shared.system_factory import registerQuestFlag

class QuestFlagTypes(object):
    PERSONAL_MISSIONS = b'personalMissions'
    BATTLE = b'battleQuests'
    MAPBOX = b'mapboxQuests'
    MARATHON = b'marathonQuests'
    ELEN = b'elenQuests'
    RANKED = b'rankedQuests'


registerQuestFlag(QuestFlagTypes.PERSONAL_MISSIONS, PersonalMissionsFlag)
registerQuestFlag(QuestFlagTypes.MARATHON, MarathonQuestsFlag)
registerQuestFlag(QuestFlagTypes.ELEN, ElenQuestsFlag)
registerQuestFlag(QuestFlagTypes.BATTLE, BattleQuestsFlag)
registerQuestFlag(QuestFlagTypes.RANKED, RankedQuestsFlag)
registerQuestFlag(QuestFlagTypes.MAPBOX, MapboxQuestsFlag)
