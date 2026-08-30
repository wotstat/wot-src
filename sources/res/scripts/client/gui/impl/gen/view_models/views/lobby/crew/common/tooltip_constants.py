from frameworks.wulf import ViewModel

class TooltipConstants(ViewModel):
    __slots__ = ()
    SKILL = b'crewPerkGf'
    SKILL_ALT = b'crewPerkAltGf'
    COMMANDER_BONUS = b'commanderBonus'
    ACHIEVEMENT = b'achievement'
    SKIN = b'crewSkin'
    DIRECTIVE = b'directive'
    TANKMAN = b'tankman'
    TANKMAN_NOT_RECRUITED = b'tankmanNotRecruited'
    SKILLS_EFFICIENCY = b'skillsEfficiency'
    CREW_SKILL_UNTRAINED = b'crewSkillUntrained'
    VEHICLE_PREVIEW_CREW_MEMBER = b'vehiclePreviewCrewMember'
    VEHICLE_CREW_MEMBER_IN_HANGAR = b'vehicleCrewMemberInHangar'
    UNIQUE_VOICEOVER_WITCHES = b'witches'
    MENTOR_ASSIGNMENT = b'MentorAssignment'
    MENTOR_FULLY_TRAINED = b'fullyTrainedMentor'

    def __init__(self, properties=0, commands=0):
        super(TooltipConstants, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TooltipConstants, self)._initialize()
        return
