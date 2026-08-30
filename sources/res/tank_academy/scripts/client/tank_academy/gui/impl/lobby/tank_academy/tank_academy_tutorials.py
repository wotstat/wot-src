TANK_ACADEMY_MULTIPLIED_XP_CHAPTER_ID = b'tankAcademyMultipliedXP'
TANK_ACADEMY_RESEARCH_MODULE_CHAPTER_ID = b'tankAcademyResearchModule'
TANK_ACADEMY_RESEARCH_VEHICLE_4_CHAPTER_ID = b'tankAcademyResearchVehicle_4'
TANK_ACADEMY_RESEARCH_VEHICLE_5_CHAPTER_ID = b'tankAcademyResearchVehicle_5'
TANK_ACADEMY_ALL_EQUIPMENT_CHAPTER_ID = b'tankAcademyAllEquipment'
TANK_ACADEMY_OPTIONAL_DEVICES_CHAPTER_ID = b'tankAcademyOptionalDevices'
TANK_ACADEMY_ALL_AMMUNITION_CHAPTER_ID = b'tankAcademyAllAmmunition'
TANK_ACADEMY_CUSTOMIZATION_CHAPTER_ID = b'tankAcademyCustomization'
TANK_ACADEMY_PERSONAL_RESERVES_CHAPTER_ID = b'tankAcademyPersonalReserves'
QUEST_TUTORIAL_CHAPTER_BY_ID = {b'tank_academy_2': TANK_ACADEMY_MULTIPLIED_XP_CHAPTER_ID, 
   b'tank_academy_3': TANK_ACADEMY_RESEARCH_MODULE_CHAPTER_ID, 
   b'tank_academy_5': TANK_ACADEMY_RESEARCH_VEHICLE_4_CHAPTER_ID, 
   b'tank_academy_6': TANK_ACADEMY_ALL_EQUIPMENT_CHAPTER_ID, 
   b'tank_academy_7': TANK_ACADEMY_OPTIONAL_DEVICES_CHAPTER_ID, 
   b'tank_academy_8': TANK_ACADEMY_ALL_AMMUNITION_CHAPTER_ID, 
   b'tank_academy_10': TANK_ACADEMY_RESEARCH_VEHICLE_5_CHAPTER_ID, 
   b'tank_academy_11': TANK_ACADEMY_CUSTOMIZATION_CHAPTER_ID, 
   b'tank_academy_26': TANK_ACADEMY_PERSONAL_RESERVES_CHAPTER_ID}

def getQuestTutorialChapterID(quest):
    if quest is None:
        return
    else:
        return QUEST_TUTORIAL_CHAPTER_BY_ID.get(quest.getID())


def hasQuestTutorial(quest):
    return getQuestTutorialChapterID(quest) is not None
