from __future__ import absolute_import
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS
FLAG_BY_QUEST_TYPE = {(HANGAR_HEADER_QUESTS.QUEST_TYPE_PERSONAL_REGULAR): (RES_ICONS.MAPS_ICONS_LIBRARY_HANGARFLAG_FLAG_VINOUS), 
   (HANGAR_HEADER_QUESTS.QUEST_TYPE_PERSONAL_PM2): (RES_ICONS.MAPS_ICONS_LIBRARY_HANGARFLAG_FLAG_RED), 
   (HANGAR_HEADER_QUESTS.QUEST_TYPE_COMMON): (RES_ICONS.MAPS_ICONS_LIBRARY_HANGARFLAG_FLAG_BLUE), 
   (HANGAR_HEADER_QUESTS.QUEST_TYPE_EVENT): (RES_ICONS.MAPS_ICONS_LIBRARY_HANGARFLAG_FLAG_KHACKI), 
   (HANGAR_HEADER_QUESTS.QUEST_TYPE_BATTLE_ROYALE): (RES_ICONS.MAPS_ICONS_LIBRARY_HANGARFLAG_FLAG_EPIC_STEELHUNTER)}

class LabelState(object):
    ACTIVE = b'active'
    EMPTY = b'empty'
    INACTIVE = b'inactive'
    ALL_DONE = b'all_done'


def getActiveQuestLabel(total, completed):
    return backport.text(R.strings.menu.hangar_header.battle_quests_label.dyn(LabelState.ACTIVE)(), total=total - completed)


def headerQuestFormatterVo(enable, icon, label, questType, flag=None, flagDisabled=None, stateIcon=None, questID=None, isReward=False, tooltip=b'', isTooltipSpecial=False, isTooltipWulf=False):
    return {b'enable': enable, 
       b'flag': (flag or FLAG_BY_QUEST_TYPE[questType]), 
       b'flagDisabled': (flagDisabled or RES_ICONS.MAPS_ICONS_LIBRARY_HANGARFLAG_FLAG_GRAY), 
       b'icon': icon, 
       b'stateIcon': stateIcon, 
       b'label': label, 
       b'questType': questType, 
       b'questID': (str(questID)), 
       b'isReward': isReward, 
       b'tooltip': tooltip, 
       b'isTooltipSpecial': isTooltipSpecial, 
       b'isTooltipWulf': isTooltipWulf}


def wrapQuestGroup(groupID, icon, quests, isRightSide=False):
    return {b'groupID': groupID, 
       b'groupIcon': icon, 
       b'quests': quests, 
       b'isRightSide': isRightSide}
