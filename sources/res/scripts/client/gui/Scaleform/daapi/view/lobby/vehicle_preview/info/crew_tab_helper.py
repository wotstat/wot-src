from __future__ import absolute_import
from collections import namedtuple
import typing
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.crew_constants import CrewConstants
from gui.shared.gui_items.Tankman import Tankman, getBigIconPath, NO_TANKMAN
from helpers.i18n import makeString
from items.tankmen import TankmanDescr, makeTmanDescrByTmanData
from shared_utils import first
from web.web_client_api.common import ItemPackType
from items.tankmen import MAX_SKILL_LEVEL
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.tankman_skill import TankmanSkill
    from gui.shared.gui_items.Vehicle import Vehicle
GIRL_EMPTY = b'girl-empty'

class PreviewTankman(Tankman):
    __slots__ = (b'_previewData',)

    def __init__(self, slotIdx, tmanData=None, tankman=None, vehicle=None):
        if tankman is not None:
            strCD = tankman.descriptor.makeCompactDescr()
            self._previewData = {}
        else:
            gid = tmanData.get(b'gId', -1)
            if b'fnGroupID' not in tmanData:
                tmanData[b'fnGroupID'] = gid
            if b'lnGroupID' not in tmanData:
                tmanData[b'lnGroupID'] = gid
            if b'iGroupID' not in tmanData:
                tmanData[b'iGroupID'] = gid
            self._previewData = tmanData
            strCD = TankmanDescr(compactDescr=makeTmanDescrByTmanData(tmanData)).makeCompactDescr()
        super(PreviewTankman, self).__init__(strCD, vehicleSlotIdx=slotIdx, vehicle=vehicle)
        return

    @property
    def fullUserName(self):
        if self._previewData.get(b'firstNameID', None) and self._previewData.get(b'lastNameID', None):
            return super(PreviewTankman, self).fullUserName
        else:
            if self.isFemale:
                return backport.text(R.strings.tooltips.awardItem.tankwomen.header())
            return b''

    @property
    def extensionLessIcon(self):
        if self._previewData.get(b'iconID', None):
            return super(PreviewTankman, self).extensionLessIcon
        else:
            if self.isFemale:
                return GIRL_EMPTY
            return b''

    @property
    def bigIconPath(self):
        iconID = self._previewData.get(b'iconID', None)
        if self._previewData.get(b'iconID', None):
            return getBigIconPath(self.nationID, iconID)
        else:
            if self.isFemale:
                return backport.image(R.images.gui.maps.icons.tankmen.icons.big.girl_empty())
            return backport.image(R.images.gui.maps.icons.tankmen.icons.big.empty())

    @property
    def backportSkillList(self):
        result = [(skill.bigIconPath, skill.userName, skill.level) for skill in self.skills]
        if self.descriptor.freeXP > 0:
            newSkills, lastNewSkillLevel = self.newSkillsCount
            if newSkills:
                img = backport.image(R.images.gui.maps.icons.tankmen.skills.big.preview_new_skill_trained())
                result.extend([
                 (
                  img, TOOLTIPS.VEHICLEPREVIEW_TANKMAN_NEWPERK_HEADER, MAX_SKILL_LEVEL)] * (newSkills - 1))
                result.extend([(img, TOOLTIPS.VEHICLEPREVIEW_TANKMAN_NEWPERK_HEADER, lastNewSkillLevel)])
        return result

    @property
    def previewVehicleName(self):
        return self.vehicleNativeDescr.type.userString


def isValidCrewForVehicle(tankmenItems, roles):
    tmenItemsLen = len(tankmenItems)
    if tmenItemsLen == 0 and tmenItemsLen != len(roles):
        return False
    cleanRoles = [first(role) for role in roles]
    for tItem in tankmenItems:
        if tItem[b'role'] not in cleanRoles:
            return False

    tankmenItems.sort(key=(lambda i: cleanRoles.index(i[b'role'])))
    for slot, tmanData in enumerate(tankmenItems):
        if cleanRoles[slot] != tmanData[b'role']:
            return False

    return True


def getCrewPreviewTitle(title, itemCrew):
    if itemCrew and itemCrew.type in (ItemPackType.CREW_50, ItemPackType.CREW_75, ItemPackType.CREW_100,
     ItemPackType.CUSTOM_CREW_100):
        return makeString(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_WITHCREW)
    else:
        if title is not None:
            return title
        return makeString(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_NOCREW)


def getCustomTitle(skill, role, forOne):
    if skill.name == CrewConstants.NEW_SKILL:
        if forOne:
            tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_NEWSKILL_FORONE
        else:
            tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_NEWSKILL_FORALL
    elif forOne:
        tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_ONESKILL_FORONE
    else:
        tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_ONESKILL_FORALL
    return makeString(key=tKey, role=makeString(TOOLTIPS.crewRole(role)) if role != b'' else None, skillName=skill.userName)


NEW_SKILL_ICON = b'preview_new_skill_trained'
_SimpleSkill = namedtuple(b'_SimpleSkill', (b'name', b'crewCustomName', b'userName', b'extensionLessIconName'))
_SIMPLE_SKILL = _SimpleSkill(CrewConstants.NEW_SKILL, b'', CrewConstants.NEW_SKILL, NEW_SKILL_ICON)

def getCustomHeader(customCrew):
    crew = [tMan for _, tMan in sorted(customCrew)]
    skills = [tMan.skills[:] + [_SIMPLE_SKILL] if tMan.descriptor.freeXP > 0 else tMan.skills[:] for tMan in crew]
    notEmptySkills = [s for s in skills if s]
    if not notEmptySkills:
        return (makeString(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_WITHCREW), b'', b'', b'')
    if all(len(s) <= 1 for s in skills):
        firstSkill = first(notEmptySkills)[0]
        icon = firstSkill.extensionLessIconName
        skillName = firstSkill.name
        customName = firstSkill.crewCustomName
        notEmptySkillsLen = len(notEmptySkills)
        if notEmptySkillsLen == 1:
            role = first(tMan.role for tMan in crew if tMan.hasNewSkill) if firstSkill.name == CrewConstants.NEW_SKILL else first(tMan.role for tMan in crew if tMan.skills)
            return (
             getCustomTitle(firstSkill, role, True), icon, skillName, customName)
        if notEmptySkillsLen == len(skills) and all(firstSkill.name == s[0].name for s in notEmptySkills):
            return (getCustomTitle(firstSkill, b'', False), icon, skillName, customName)
    return (
     makeString(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_ANYSKILLS), b'', b'', b'')


def getPreviewCrewMemberArgs(isCustom, slotIdx, tankman):
    args = [
     tankman.role, NO_TANKMAN, slotIdx]
    if isCustom:
        args.extend([
         tankman.fullUserName,
         tankman.previewVehicleName,
         tankman.bigIconPath,
         b'',
         tankman.backportSkillList])
    else:
        args.extend([0, 0, 0, 0, 0])
    return args
