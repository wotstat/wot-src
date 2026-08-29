import cPickle
from typing import Dict
from helpers import dependency, i18n
from items.components import skills_constants
from items.components.crew_skins_constants import NO_CREW_SKIN_ID
from gui.shared.gui_items.crew_skin import localizedFullName
from gui.shared.gui_items.fitting_item import ICONS_MASK
from gui.shared.gui_items import Tankman, Vehicle
from skeletons.gui.shared import IItemsCache
from skeletons.gui.lobby_context import ILobbyContext

def packTankmanSkill(skill, isPermanent=False):
    if skill.roleType in skills_constants.ACTIVE_SKILLS or skill.roleType in skills_constants.ROLES:
        roleIconPath = Tankman.getRoleSmallIconPath(skill.roleType)
    else:
        roleIconPath = b''
    return {b'name': (skill.name), 
       b'level': (skill.level), 
       b'userName': (skill.userName), 
       b'description': (skill.description), 
       b'shortDescription': (skill.shortDescription), 
       b'icon': {b'big': (skill.bigIconPath), 
                 b'small': (skill.smallIconPath), 
                 b'role': roleIconPath}, 
       b'isActive': True, 
       b'isEnable': (skill.isEnable), 
       b'roleType': (skill.roleType), 
       b'isPermanent': isPermanent}


def packTankman(tankman, isCountPermanentSkills=True, splitFreeAndEarnedSkills=False):

    def vehicleIcon(vDescr, subtype=b''):
        return ICONS_MASK % {b'type': b'vehicle', 
           b'subtype': subtype, 
           b'unicName': (vDescr.name.replace(b':', b'-'))}

    nativeVehicleData = {b'typeCompDescr': (tankman.vehicleNativeDescr.type.compactDescr), 
       b'userName': (Vehicle.getShortUserName(tankman.vehicleNativeDescr.type)), 
       b'icon': (vehicleIcon(tankman.vehicleNativeDescr)), 
       b'iconContour': (vehicleIcon(tankman.vehicleNativeDescr, b'contour/'))}
    currentVehicleData = None
    if tankman.isInTank:
        currentVehicleData = {b'inventoryID': (tankman.vehicleInvID), b'typeCompDescr': (tankman.vehicleDescr.type.compactDescr), 
           b'userName': (Vehicle.getShortUserName(tankman.vehicleDescr.type)), 
           b'icon': (vehicleIcon(tankman.vehicleDescr)), 
           b'iconContour': (vehicleIcon(tankman.vehicleDescr, b'contour/'))}
    freeSkills = []
    skills = []
    if splitFreeAndEarnedSkills:
        for tankmanSkill in tankman.freeSkills:
            freeSkills.append(packTankmanSkill(tankmanSkill, isPermanent=True))

        for tankmanSkill in tankman.earnedSkills:
            skills.append(packTankmanSkill(tankmanSkill, isPermanent=False))

    else:
        tManChosenFreeSkillsNum = tankman.chosenFreeSkillsCount
        startSkillNumber = 0 if isCountPermanentSkills else tManChosenFreeSkillsNum
        tManSkills = tankman.skills
        for i in xrange(startSkillNumber, len(tManSkills)):
            skills.append(packTankmanSkill(tManSkills[i], isPermanent=i < tManChosenFreeSkillsNum))

    rrl = tankman.realRoleLevel
    realRoleLevel = (rrl.lvl, tuple(rrl.bonuses))
    return {b'strCD': (cPickle.dumps(tankman.strCD)), 
       b'inventoryID': (tankman.invID), 
       b'nationID': (tankman.nationID), 
       b'firstUserName': (tankman.firstUserName), 
       b'lastUserName': (tankman.lastUserName), 
       b'roleName': (tankman.descriptor.role), 
       b'rankUserName': (tankman.rankUserName), 
       b'roleUserName': (tankman.roleUserName), 
       b'freeSkills': freeSkills, 
       b'newFreeSkillsCount': (tankman.newFreeSkillsCount), 
       b'skills': skills, 
       b'efficiencyRoleLevel': (tankman.efficiencyRoleLevel), 
       b'realRoleLevel': realRoleLevel, 
       b'roleLevel': (tankman.roleLevel), 
       b'icon': {b'big': (Tankman.getBigIconPath(tankman.nationID, tankman.descriptor.iconID)), 
                 b'small': (Tankman.getSmallIconPath(tankman.nationID, tankman.descriptor.iconID)), 
                 b'barracks': (Tankman.getBarracksIconPath(tankman.nationID, tankman.descriptor.iconID))}, 
       b'iconRole': {b'big': (Tankman.getRoleBigIconPath(tankman.descriptor.role)), 
                     b'medium': (Tankman.getRoleMediumIconPath(tankman.descriptor.role)), 
                     b'small': (Tankman.getRoleSmallIconPath(tankman.descriptor.role))}, 
       b'iconRank': {b'big': (Tankman.getRankBigIconPath(tankman.nationID, tankman.descriptor.rankID)), 
                     b'small': (Tankman.getRankSmallIconPath(tankman.nationID, tankman.descriptor.rankID))}, 
       b'isInTank': (tankman.isInTank), 
       b'newSkillsCount': (tankman.newSkillCount), 
       b'nativeVehicle': nativeVehicleData, 
       b'currentVehicle': currentVehicleData}


@dependency.replace_none_kwargs(itemsCache=IItemsCache, lobbyContext=ILobbyContext)
def repackTankmanWithSkinData(item, data, itemsCache=None, lobbyContext=None):
    if item.skinID != NO_CREW_SKIN_ID:
        skinItem = itemsCache.items.getCrewSkin(item.skinID)
        data[b'icon'][b'big'] = Tankman.getCrewSkinIconBig(skinItem.getIconID())
        data[b'firstUserName'] = i18n.makeString(skinItem.getFirstName())
        data[b'lastUserName'] = i18n.makeString(skinItem.getLastName())
        data[b'fullName'] = localizedFullName(skinItem)
    else:
        data[b'fullName'] = item.fullUserName
    return
