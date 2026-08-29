from collections import namedtuple
from CurrentVehicle import g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import OFFER_CHANGED_EVENT
from gui.Scaleform.daapi.view.meta.VehiclePreviewCrewTabMeta import VehiclePreviewCrewTabMeta
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.RES_COMMON import RES_COMMON
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.MENU import MENU
from gui.shared import g_eventBus
from gui.impl.gen import R
from gui.impl import backport
from gui.shared.formatters import text_styles
from gui.shared.gui_items.Tankman import SabatonTankmanSkill, TankmanSkill, OffspringTankmanSkill, YhaTankmanSkill, BROTHERHOOD_SKILL_NAME, WitchesTankmanSkill
from gui.shared.gui_items.Tankman import getFullUserName, getSmallIconPath, getBigIconPath
from gui.shared.gui_items.Vehicle import sortCrew
from helpers.i18n import makeString as _ms
from items import tankmen, vehicles
from items import special_crew
from items.tankmen import SKILL_INDICES, SKILL_NAMES
from shared_utils import first
from soft_exception import SoftException
from web.web_client_api.common import ItemPackType, ItemPackTypeGroup
NEW_SKILL_ICON = b'../maps/icons/tankmen/skills/big/preview_new_skill.png'
_SimpleSkill = namedtuple(b'_SimpleSkill', (b'name', b'userName', b'bigIconPath', b'isPerk'))
_SimpleSkill.__new__.__defaults__ = (b'new', b'new', NEW_SKILL_ICON, False)

def _createPrewiewTankman(tmanData=None):
    if tmanData:
        tankman = PreviewTankman(tmanData)
        return tankman
    else:
        return


def getTankmanSkill(skillName, tankman=None):
    if tankman is not None:
        if special_crew.isSabatonCrew(tankman):
            return SabatonTankmanSkill(skillName)
        if special_crew.isOffspringCrew(tankman):
            return OffspringTankmanSkill(skillName)
        if special_crew.isYhaCrew(tankman):
            return YhaTankmanSkill(skillName)
        if special_crew.isWitchesCrew(tankman):
            return WitchesTankmanSkill(skillName)
    return TankmanSkill(skillName, proxy=(0,))


class PreviewTankman(object):
    _TANKWOMAN_ICON_FORMAT_STRING = b'../maps/icons/tankmen/icons/{}/girl-empty.png'

    def __init__(self, tmanData):
        self.firstNameID = tmanData.get(b'firstNameID', None)
        self.lastNameID = tmanData.get(b'lastNameID', None)
        self.iconID = tmanData.get(b'iconID', None)
        self.isPremium = tmanData.get(b'isPremium', False)
        self.role = tmanData.get(b'role', b'')
        self.nationID = tmanData.get(b'nationID', None)
        self.roleLevel = tmanData.get(b'roleLevel', 100)
        self.freeXP = tmanData.get(b'freeXP', None)
        self.isFemale = tmanData.get(b'isFemale', False)
        self.vehicleTypeID = tmanData.get(b'vehicleTypeID', None)
        self.gid = tmanData.get(b'gId', -1)
        skills = tmanData.get(b'skills', []) + tmanData.get(b'freeSkills', [])
        self.skills = self._buildSkills(skills)
        return

    @property
    def fullUserName(self):
        if self.firstNameID and self.lastNameID:
            return getFullUserName(self.nationID, self.firstNameID, self.lastNameID)
        if self.isFemale:
            return TOOLTIPS.AWARDITEM_TANKWOMEN_HEADER
        return ITEM_TYPES.tankman_roles(self.role)

    @property
    def vehicleName(self):
        if self.vehicleTypeID:
            return vehicles.g_cache.vehicle(self.nationID, self.vehicleTypeID).userString
        return b''

    @property
    def icon(self):
        if self.iconID:
            return getSmallIconPath(self.nationID, self.iconID)
        if self.isFemale:
            return self._TANKWOMAN_ICON_FORMAT_STRING.format(b'small')
        return RES_ICONS.getItemBonus42x42(self.role)

    @property
    def bigIcon(self):
        if self.iconID:
            return getBigIconPath(self.nationID, self.iconID)
        if self.isFemale:
            return self._TANKWOMAN_ICON_FORMAT_STRING.format(b'big')
        return b''

    @property
    def tooltip(self):
        return TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_CREW_MEMBER

    @property
    def hasNewSkill(self):
        return self.freeXP > 0

    def getVO(self, showTankmanSkills=True):
        skillsList = [{b'tankmanID': 1, b'id': (str(self.skills.index(skill))), b'name': (skill.userName), b'desc': (skill.description), b'icon': (skill.icon), b'level': (tankmen.MAX_SKILL_LEVEL), b'active': True} for skill in self.skills]
        if self.hasNewSkill:
            skillsList.append({b'buy': True, 
               b'buyCount': 0, 
               b'tankmanID': 1, 
               b'level': (tankmen.MAX_SKILL_LEVEL)})
        tankmanVO = {b'icon': (self.icon), 
           b'name': (self.fullUserName), 
           b'tooltip': (self.tooltip), 
           b'role': (self.role)}
        if showTankmanSkills and skillsList:
            tankmanVO.update({b'tankman': {b'skills': skillsList, 
                            b'lastSkillLevel': (tankmen.MAX_SKILL_LEVEL)}})
        return tankmanVO

    def getTooltipVO(self):
        skillsItems = [(skill.bigIconPath, skill.userName, False) for skill in self.skills]
        if self.hasNewSkill:
            skillsItems.append((
             NEW_SKILL_ICON,
             TOOLTIPS.VEHICLEPREVIEW_TANKMAN_NEWPERK_HEADER,
             True))
        return (
         self.role,
         self.fullUserName,
         self.vehicleName,
         self.bigIcon,
         b'',
         skillsItems)

    def _buildSkills(self, skills):
        return [getTankmanSkill(skill, self) for skill in skills]


class VehiclePreviewCrewTab(VehiclePreviewCrewTabMeta):

    def __init__(self):
        super(VehiclePreviewCrewTab, self).__init__()
        self.__crewItems = ()
        self.__vehicleItems = ()
        self.__customCrew = None
        return

    def setActiveState(self, isActive):
        return

    def setVehicleCrews(self, vehicleItems, crewItems):
        self.__vehicleItems = vehicleItems
        self.__crewItems = crewItems
        self._update()
        return

    def getTooltipData(self, crewId):
        if self.__customCrew:
            for idx, tman in self.__customCrew:
                if idx == crewId:
                    return tman.getTooltipVO()

        return [
         SKILL_NAMES[crewId],
         None,
         None,
         None,
         None,
         None]

    def update(self, *args):
        if g_currentPreviewVehicle.isPresent():
            self._update()
        return

    def _populate(self):
        super(VehiclePreviewCrewTab, self)._populate()
        g_currentPreviewVehicle.onComponentInstalled += self.update
        g_currentPreviewVehicle.onChanged += self.update
        g_eventBus.addListener(OFFER_CHANGED_EVENT, self.__onOfferChanged)
        self.update()
        return

    def _dispose(self):
        g_eventBus.removeListener(OFFER_CHANGED_EVENT, self.__onOfferChanged)
        g_currentPreviewVehicle.onChanged -= self.update
        g_currentPreviewVehicle.onComponentInstalled -= self.update
        super(VehiclePreviewCrewTab, self)._dispose()
        return

    def _update(self):
        currentVehicle = g_currentPreviewVehicle.item
        vehicleCrewComment = _ms(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_NOCREW)
        skillIcon = b''
        skillName = b''
        gID = None
        regularCrewList = []
        uniqueCrewList = []
        isLockedCrew = False
        if self.__vehicleItems is not None and self.__crewItems is not None:
            for item in self.__vehicleItems:
                if item.id == currentVehicle.intCD:
                    gID = item.groupID
                    break

            if gID is not None:
                crewItems = sorted([item for item in self.__crewItems if item.groupID == gID], key=(lambda i: ItemPackTypeGroup.CREW.index(i.type)), reverse=True)
                topCrewItem = crewItems[0] if crewItems else None
                if topCrewItem and topCrewItem.type == ItemPackType.CREW_CUSTOM:
                    isLockedCrew = (topCrewItem.extra or False) and topCrewItem.extra.get(b'isLockedCrew', False)
                self.__setCustomCrew(topCrewItem, currentVehicle)
                vehicleCrewComment, skillIcon, skillName = self.__getCrewCommentAndIcon(topCrewItem)
                regularCrewList, uniqueCrewList = self.__getCrewData(currentVehicle, not bool(skillIcon))
        self.as_setDataS({b'vehicleCrewComment': (text_styles.middleTitle(vehicleCrewComment)), 
           b'regularCrewList': regularCrewList, 
           b'uniqueCrewList': uniqueCrewList, 
           b'skillIcon': skillIcon, 
           b'skillName': skillName, 
           b'lockedCrew': isLockedCrew})
        return

    def _getCustomCrewComment(self):
        crew = [tMan for _, tMan in sorted(self.__customCrew)]
        crewLevel = first(crew).roleLevel
        skills = [tMan.skills[:] + [_SimpleSkill()] if tMan.hasNewSkill else tMan.skills[:] for tMan in crew]
        notEmptySkills = [s for s in skills if s]
        if not notEmptySkills:
            return (_ms(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_WITHCREW, crewLevel), b'', b'')
        if all(len(s) <= 1 for s in skills):
            firstSkill = first(notEmptySkills)[0]
            icon = firstSkill.bigIconPath
            skillName = b''
            if _isSabatonBrotherhood(firstSkill):
                skillName = b'sabaton_brotherhood'
            elif _isOffspringBrotherhood(firstSkill):
                skillName = b'offspring_brotherhood'
            elif _isYhaBrotherhood(firstSkill):
                skillName = b'yha_brotherhood'
            elif _isWitchesBrotherhood(firstSkill):
                skillName = b'witches_brotherhood'
            elif not firstSkill.name == b'new':
                skillName = firstSkill.name
            notEmptySkillsLen = len(notEmptySkills)
            if notEmptySkillsLen == 1:
                role = first(tMan.role for tMan in crew if tMan.hasNewSkill) if firstSkill.name == b'new' else first(tMan.role for tMan in crew if tMan.skills)
                return (
                 getCrewComment(firstSkill, crewLevel, role, True), icon, skillName)
            if notEmptySkillsLen == len(skills) and all(firstSkill.name == s[0].name for s in notEmptySkills):
                return (getCrewComment(firstSkill, crewLevel, b'', False), icon, skillName)
        return (
         _ms(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_ANYSKILLS, crewLevel), b'', b'')

    def __onOfferChanged(self, event):
        ctx = event.ctx
        self.setVehicleCrews(ctx.get(b'vehicleItems'), ctx.get(b'crewItems'))
        return

    def __setCustomCrew(self, topCrewItem, vehicle):
        if topCrewItem and topCrewItem.extra and topCrewItem.type == ItemPackType.CREW_CUSTOM:
            roles = vehicle.descriptor.type.crewRoles
            tmenItems = topCrewItem.extra.get(b'tankmen', [])
            if not isValidCrewForVehicle(tmenItems, roles):
                raise SoftException(b'Invalid crew preset for this vehicle')
            crew = [(idx, _createPrewiewTankman(tmanData)) for idx, tmanData in enumerate(tmenItems)]
            self.__customCrew = sortCrew(crew, roles)
        else:
            self.__customCrew = None
        return

    def __getCrewData(self, currentVehicle, showTankmanSkills):
        regularCrewList, uniqueCrewList = [], []
        if currentVehicle:
            uniqueCrewList.extend(getUniqueMembers(currentVehicle))
        if self.__customCrew:
            for idx, tankman in self.__customCrew:
                tankmanData = tankman.getVO(showTankmanSkills)
                tankmanData.update({b'crewId': idx})
                if tankman.iconID or tankman.isFemale:
                    uniqueCrewList.append(tankmanData)
                else:
                    regularCrewList.append(tankmanData)

        else:
            for idx, tankman in currentVehicle.crew:
                role = tankman.descriptor.role
                roleIdx = SKILL_INDICES[role]
                regularCrewList.append({b'crewId': roleIdx, 
                   b'icon': (RES_ICONS.getItemBonus42x42(role)), 
                   b'name': (ITEM_TYPES.tankman_roles(role)), 
                   b'tooltip': (TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_CREW_MEMBER), 
                   b'role': role})

        return (
         regularCrewList, uniqueCrewList)

    def __getCrewCommentAndIcon(self, itemCrew):
        if self.__customCrew:
            return self._getCustomCrewComment()
        if itemCrew and itemCrew.type in (ItemPackType.CREW_50, ItemPackType.CREW_75, ItemPackType.CREW_100,
         ItemPackType.CUSTOM_CREW_100):
            pctValue = {(ItemPackType.CREW_50): 50, (ItemPackType.CREW_75): 75, 
               (ItemPackType.CREW_100): 100, 
               (ItemPackType.CUSTOM_CREW_100): 100}.get(itemCrew.type)
            return (
             _ms(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_WITHCREW, pctValue),
             b'', b'')
        return (_ms(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_NOCREW), b'', b'')


def getCrewComment(skill, crewLevel, role, forOne):
    if skill.name == b'new':
        if forOne:
            tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_NEWSKILL_FORONE
        else:
            tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_NEWSKILL_FORALL
    elif forOne:
        tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_ONESKILL_FORONE
    else:
        tKey = TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_ONESKILL_FORALL
    return _ms(key=tKey, level=crewLevel, role=_ms(TOOLTIPS.crewRole(role)) if role != b'' else None, skillType=_ms(TOOLTIPS.VEHICLEPREVIEW_VEHICLEPANEL_INFO_HEADER_CREW_ISABILLITY), skillName=text_styles.statusAttention(_ms(MENU.QUOTE, string=skill.userName)))


def _isSabatonBrotherhood(skill):
    return isinstance(skill, SabatonTankmanSkill) and skill.name == BROTHERHOOD_SKILL_NAME


def _isOffspringBrotherhood(skill):
    return isinstance(skill, OffspringTankmanSkill) and skill.name == BROTHERHOOD_SKILL_NAME


def _isYhaBrotherhood(skill):
    return isinstance(skill, YhaTankmanSkill) and skill.name == BROTHERHOOD_SKILL_NAME


def _isWitchesBrotherhood(skill):
    return isinstance(skill, WitchesTankmanSkill) and skill.name == BROTHERHOOD_SKILL_NAME


def getUniqueMembers(vehicle):
    uniqueMembers = []
    if b'dog' in vehicle.tags:
        uniqueMembers.append({b'crewId': (-1), 
           b'icon': (RES_COMMON.MAPS_ICONS_TANKMEN_ICONS_SMALL_USSR_DOG_1), 
           b'name': (backport.text(R.strings.menu.hangar.crew.rody.dog.dyn(vehicle.nationName).name())), 
           b'tooltip': (TOOLTIPS.HANGAR_CREW_RUDY_DOG + vehicle.nationName), 
           b'role': b''})
    return uniqueMembers


def isValidCrewForVehicle(tmenItems, roles):
    tmenItemsLen = len(tmenItems)
    if tmenItemsLen <= 0 and tmenItemsLen != len(roles):
        return False
    cleanRoles = [first(role) for role in roles]
    for tItem in tmenItems:
        if tItem[b'role'] not in cleanRoles:
            return False

    tmenItems.sort(key=(lambda i: cleanRoles.index(i[b'role'])))
    firstRoleLvl = first(tmenItems).get(b'roleLevel', [])
    for slot, tmanData in enumerate(tmenItems):
        if cleanRoles[slot] != tmanData[b'role'] or firstRoleLvl != tmanData.get(b'roleLevel', []):
            return False

    return True
