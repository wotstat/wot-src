from __future__ import absolute_import
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional

class ISkill(object):

    @property
    def name(self):
        raise NotImplementedError
        return

    @property
    def customName(self):
        raise NotImplementedError
        return

    @property
    def crewCustomName(self):
        raise NotImplementedError
        return


class ISkillPresenter(ISkill):

    @property
    def userName(self):
        raise NotImplementedError
        return

    @property
    def description(self):
        raise NotImplementedError
        return

    @property
    def shortDescription(self):
        raise NotImplementedError
        return

    @property
    def maxLvlDescription(self):
        raise NotImplementedError
        return

    @property
    def currentLvlDescription(self):
        raise NotImplementedError
        return

    @property
    def altDescription(self):
        raise NotImplementedError
        return

    @property
    def altInfo(self):
        raise NotImplementedError
        return

    @property
    def icon(self):
        raise NotImplementedError
        return

    @property
    def extensionLessIconName(self):
        raise NotImplementedError
        return

    @property
    def bigIconPath(self):
        raise NotImplementedError
        return


class ISkillData(ISkill):

    @property
    def level(self):
        raise NotImplementedError
        return

    @property
    def roleType(self):
        raise NotImplementedError
        return

    @property
    def typeName(self):
        raise NotImplementedError
        return

    @property
    def isEnable(self):
        raise NotImplementedError
        return

    @property
    def isZero(self):
        raise NotImplementedError
        return

    @property
    def isSituational(self):
        raise NotImplementedError
        return

    @property
    def isLearned(self):
        raise NotImplementedError
        return

    @property
    def isLearnedAsMajor(self):
        raise NotImplementedError
        return

    @property
    def isLearnedAsBonus(self):
        raise NotImplementedError
        return

    @property
    def isMaxLevel(self):
        raise NotImplementedError
        return

    @property
    def isSkillActive(self):
        raise NotImplementedError
        return

    @property
    def isRelevant(self):
        raise NotImplementedError
        return

    @property
    def learnState(self):
        raise NotImplementedError
        return

    @property
    def skillRole(self):
        raise NotImplementedError
        return

    @property
    def tankmanRole(self):
        raise NotImplementedError
        return

    def setIsSkillActive(self, isSkillActive):
        raise NotImplementedError
        return
