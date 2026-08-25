from __future__ import absolute_import, division
from dossiers2.ui.achievements import ACHIEVEMENT_SECTION, ACHIEVEMENT_TYPE
from dossiers2.custom.config import RECORD_CONFIGS
from gui.shared.gui_items.dossier.achievements.abstract import isRareAchievement
from gui.shared.gui_items.dossier.achievements import MarkOnGunAchievement
from gui.Scaleform.genConsts.ACHIEVEMENTS_ALIASES import ACHIEVEMENTS_ALIASES

class AchievementsUtils(object):

    @staticmethod
    def packAchievementList(target, dossierType, dossierCompactDescriptor, isDossierForCurrentUser, defaultShowProgress=True, defaultSeriesCounter=None):
        return [AchievementsUtils.packAchievement(achievement, dossierType, dossierCompactDescriptor, isDossierForCurrentUser, defaultShowProgress, defaultSeriesCounter) for achievement in target if achievement.canDisplayAchievement()]

    @staticmethod
    def packAchievement(achievement, dossierType, dossierCompDescr, isDossierForCurrentUser, defaultShowProgress=True, defaultSeriesCounter=None):
        atype = achievement.getType()
        total = achievement.getLevelUpTotalValue() or 0
        lvlUpValue = achievement.getLevelUpValue() or 0
        current = total - lvlUpValue
        progress = None
        section = achievement.getSection()
        if atype == ACHIEVEMENT_TYPE.REPEATABLE:
            if section in (ACHIEVEMENT_SECTION.SPECIAL, ACHIEVEMENT_SECTION.BATTLE):
                if total > 0:
                    progress = (
                     0, current, total)
        elif atype == ACHIEVEMENT_TYPE.SERIES:
            if section == ACHIEVEMENT_SECTION.SPECIAL:
                minRecordValue = -1
                if atype == ACHIEVEMENT_TYPE.SERIES and section == ACHIEVEMENT_SECTION.SPECIAL:
                    minRecordValue = RECORD_CONFIGS.get(achievement.getName())
                MIN_PROGRESS_PERCENT = 0.9
                divisionVal = 0
                if total != 0:
                    divisionVal = current / total
                if divisionVal >= MIN_PROGRESS_PERCENT or current != 0 and lvlUpValue < minRecordValue:
                    progress = (
                     0, current, total)
        elif atype == ACHIEVEMENT_TYPE.CUSTOM:
            if section == ACHIEVEMENT_SECTION.SPECIAL:
                if current != total:
                    progress = (
                     0, current, total)
            else:
                progress = (
                 0, current, total)
        elif atype == ACHIEVEMENT_TYPE.CLASS:
            if current != total:
                progress = (
                 0, current, total)
        elif atype == ACHIEVEMENT_TYPE.SINGLE:
            if current != total and not achievement.getValue():
                progress = (
                 0, current, total)
        isRare = isRareAchievement(achievement)
        if isRare:
            rareIconID = achievement.requestImageID()
        else:
            rareIconID = None
        if not defaultShowProgress or not isDossierForCurrentUser:
            progress = None
        commonData = AchievementsUtils.getCommonAchievementData(achievement, dossierType, dossierCompDescr, 1 if achievement.isInDossier() else 0.2)
        commonData.update({b'isRare': isRare, 
           b'rareIconId': rareIconID, 
           b'counterType': (AchievementsUtils.getCounterType(achievement, defaultSeriesCounter)), 
           b'progress': progress, 
           b'isDossierForCurrentUser': isDossierForCurrentUser})
        return commonData

    @staticmethod
    def getCommonAchievementData(achievement, dossierType, dossierCompDescr, iconAlpha=1):
        icons = achievement.getIcons()
        return {b'name': (achievement.getName()), 
           b'block': (achievement.getBlock()), 
           b'type': (achievement.getType()), 
           b'section': (achievement.getSection()), 
           b'value': (achievement.getValue()), 
           b'localizedValue': (achievement.getI18nValue()), 
           b'isInDossier': (achievement.isInDossier()), 
           b'icon': {b'big': (icons[b'180x180']), 
                     b'small': (icons[b'67x71'])}, 
           b'dossierType': dossierType, 
           b'dossierCompDescr': dossierCompDescr, 
           b'iconAlpha': iconAlpha}

    @staticmethod
    def getBattleResultAchievementData(achievement, aType, customData, isUnique=False):
        rank, i18nValue = (None, None)
        if achievement.getType() != ACHIEVEMENT_TYPE.SERIES:
            rank, i18nValue = achievement.getValue(), achievement.getI18nValue()
        icons = achievement.getIcons()
        specialIcon = icons.get(MarkOnGunAchievement.IT_95X85, None)
        return {b'type': aType, 
           b'block': (achievement.getBlock()), 
           b'inactive': False, 
           b'icon': {b'big': b'', 
                     b'small': (achievement.getSmallIcon() if specialIcon is None else b'')}, 
           b'rank': rank, 
           b'localizedValue': i18nValue, 
           b'unic': isUnique, 
           b'isRare': False, 
           b'title': (achievement.getUserName()), 
           b'description': (achievement.getUserDescription()), 
           b'rareIconId': None, 
           b'isEpic': (achievement.hasRibbon()), 
           b'specialIcon': specialIcon, 
           b'customData': customData}

    @staticmethod
    def getCounterType(achievement, defaultSeriesCounter=None):
        counterType = None
        section = achievement.getSection()
        atype = achievement.getType()
        in_dossier = achievement.isInDossier()
        if atype == ACHIEVEMENT_TYPE.REPEATABLE:
            if section in (ACHIEVEMENT_SECTION.SPECIAL, ACHIEVEMENT_SECTION.BATTLE):
                if in_dossier:
                    counterType = ACHIEVEMENTS_ALIASES.RED_COUNTER
            elif section == ACHIEVEMENT_SECTION.ACTION:
                if achievement.hasCounter():
                    counterType = ACHIEVEMENTS_ALIASES.RED_COUNTER
            elif in_dossier:
                counterType = ACHIEVEMENTS_ALIASES.RED_COUNTER
        elif atype == ACHIEVEMENT_TYPE.SERIES:
            if in_dossier:
                counterType = defaultSeriesCounter or ACHIEVEMENTS_ALIASES.YELLOW_COUNTER
        elif atype == ACHIEVEMENT_TYPE.CUSTOM:
            if section == ACHIEVEMENT_SECTION.SPECIAL:
                counterType = None
        elif atype == ACHIEVEMENT_TYPE.CLASS:
            counterType = ACHIEVEMENTS_ALIASES.BEIGE_COUNTER
        return counterType
