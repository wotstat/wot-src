import math
from typing import List, Optional, Dict
import nations
from gui import makeHtmlString
from gui.game_control.restore_contoller import getTankmenRestoreInfo
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.tooltips.common import BlocksTooltipData
from gui.shared.tooltips import ToolTipDataField, ToolTipAttrField, ToolTipData, TOOLTIP_TYPE, formatters
from gui.shared.formatters import text_styles, moneyWithIcon
from gui.shared.gui_items.Tankman import Tankman
from gui.shared.gui_items.Vehicle import Vehicle
from helpers import dependency
from helpers import i18n
from helpers import time_utils
from helpers.i18n import makeString
from items.components.component_constants import EMPTY_STRING
from items.tankmen import SKILLS_BY_ROLES, getSkillsConfig
from shared_utils import findFirst
from skeletons.gui.shared import IItemsCache
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.game_control import IBattleRoyaleController
TANKMAN_DISMISSED = b'dismissed'
_TIME_FORMAT_UNITS = [
 (
  b'days', time_utils.ONE_DAY),
 (
  b'hours', time_utils.ONE_HOUR),
 (
  b'minutes', time_utils.ONE_MINUTE)]

class TankmanRoleLevelField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        if tankman:
            return tankman.realRoleLevel.lvl
        return 0


class TankmanRoleBonusesField(ToolTipDataField):

    class BONUSES(object):
        COMMANDER = 0
        BROTHERHOOD = 1
        EQUIPMENTS = 2
        DEVICES = 3
        PENALTY = 4

    def __init__(self, context, name, ids):
        super(TankmanRoleBonusesField, self).__init__(context, name)
        self.__ids = ids
        return

    def _getValue(self):
        tankman = self._tooltip.item
        result = 0
        if tankman:
            bonuses = tankman.realRoleLevel.bonuses
            for idx in self.__ids:
                result += int(math.ceil(float(bonuses[idx])))

        return result


class TankmanCurrentVehicleAttrField(ToolTipAttrField):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getItem(self):
        tankman = self._tooltip.item
        if tankman and tankman.isInTank:
            return self.itemsCache.items.getVehicle(tankman.vehicleInvID)
        else:
            return


class TankmanNativeVehicleAttrField(ToolTipAttrField):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getItem(self):
        tankman = self._tooltip.item
        return self.itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)


class TankmanSkillListField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        skillsList = self._getBaseSkills(tankman)
        self._addNewSkills(tankman, skillsList)
        return skillsList

    @staticmethod
    def _getBaseSkills(tankman):
        skillsList = []
        for idx, skill in enumerate(tankman.skills):
            skillsList.append({b'id': (str(idx)), 
               b'label': (skill.userName), 
               b'level': (skill.level), 
               b'enabled': (tankman.isInTank or skill.isEnable)})

        return skillsList

    def _addNewSkills(self, tankman, skillsList):
        newSkillsCount, newSkillLevel = tankman.newSkillCount
        if newSkillsCount > 0:
            if newSkillsCount > 2:
                newSkills = [
                 str(newSkillsCount - 1) + b'x100']
            elif newSkillsCount == 2:
                newSkills = [
                 100]
            else:
                newSkills = []
            if newSkillLevel > 0:
                newSkills.append(newSkillLevel)
            newSkillStr = makeString(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_NEWSKILL)
            for idx, skillLevel in enumerate(newSkills, start=len(skillsList)):
                skillsList.append({b'id': (str(idx)), 
                   b'label': newSkillStr, 
                   b'level': skillLevel, 
                   b'enabled': False})

        return


class BattleRoyaleTankmanSkillListField(TankmanSkillListField):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def _getValue(self):
        skills = self.__battleRoyaleController.getBrCommanderSkills()
        skillsList = []
        for idx, skill in enumerate(skills):
            skillsList.append({b'id': (str(idx)), 
               b'label': (skill.userName), 
               b'level': (skill.level), 
               b'enabled': (skill.isEnable), 
               b'typeName': (skill.typeName)})

        return skillsList

    def _addNewSkills(self, tankman, skillsList):
        return


class TankmanNewFreeSkillCountField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        if not tankman.isDismissed:
            return tankman.newFreeSkillsCount
        return 0


class TankmanNewSkillCountField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        if not tankman.isDismissed:
            return tankman.newSkillCount[0]
        return 0


def formatRecoveryLeftValue(secondsLeft):
    closestUnit = findFirst((lambda (k, v): v < secondsLeft), _TIME_FORMAT_UNITS)
    if closestUnit is not None:
        name, factor = closestUnit
        timeLeft = int(math.ceil(float(secondsLeft) / factor))
        return makeString(TOOLTIPS.template_all_short(name), value=timeLeft)
    else:
        return makeString(TOOLTIPS.TEMPLATE_TIME_LESSTHENMINUTE)


def getRecoveryStatusText(restoreInfo):
    price, timeLeft = restoreInfo
    if not price:
        itemsCache = dependency.instance(IItemsCache)
        restoreConfig = itemsCache.items.shop.tankmenRestoreConfig
        duration = restoreConfig.billableDuration - restoreConfig.freeDuration
        text = makeString(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_FREE_BODY, totalLeftValue=formatRecoveryLeftValue(timeLeft), freeLeftValue=formatRecoveryLeftValue(timeLeft - duration), price=moneyWithIcon(restoreConfig.cost), withMoneyLeftValue=formatRecoveryLeftValue(duration))
    else:
        text = makeString(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_GOLD_BODY, totalLeftValue=formatRecoveryLeftValue(timeLeft), price=moneyWithIcon(price))
    return text_styles.main(text)


class TankmanStatusField(ToolTipDataField):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getValue(self):
        header = b''
        text = b''
        statusTemplate = b'#tooltips:tankman/status/%s'
        tankman = self._tooltip.item
        vehicle = None
        if tankman.isInTank:
            vehicle = self.itemsCache.items.getVehicle(tankman.vehicleInvID)
        nativeVehicle = self.itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)
        if tankman.isDismissed:
            return {b'header': (text_styles.warning(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_HEADER)), 
               b'text': (getRecoveryStatusText(getTankmenRestoreInfo(tankman))), 
               b'level': TANKMAN_DISMISSED}
        else:
            inactiveRoles = []
            if tankman.isInTank:
                for skill in tankman.skills:
                    if not skill.isEnable:
                        role = self.__getRoleBySkill(skill)
                        if role not in inactiveRoles:
                            inactiveRoles.append(role)

            if vehicle is not None and nativeVehicle.innationID != vehicle.innationID:
                if (vehicle.isPremium or vehicle.isPremiumIGR) and vehicle.type in nativeVehicle.tags:
                    header = makeString(statusTemplate % b'wrongPremiumVehicle/header')
                    text = makeString(statusTemplate % b'wrongPremiumVehicle/text') % {b'vehicle': (vehicle.shortUserName)}
                else:
                    header = makeString(statusTemplate % b'wrongVehicle/header') % {b'vehicle': (vehicle.shortUserName)}
                    text = makeString(statusTemplate % b'wrongVehicle/text')
            elif inactiveRoles:

                def roleFormat(role):
                    return makeString(statusTemplate % b'inactiveSkillsRoleFormat') % makeString(getSkillsConfig().getSkill(role).userString)

                header = makeString(statusTemplate % b'inactiveSkills/header')
                text = makeString(statusTemplate % b'inactiveSkills/text') % {b'skills': ((b', ').join([roleFormat(role) for role in inactiveRoles]))}
            return {b'header': header, 
               b'text': text, 
               b'level': (Vehicle.VEHICLE_STATE_LEVEL.WARNING)}
            return

    def __getRoleBySkill(self, skill):
        for role, skills in SKILLS_BY_ROLES.iteritems():
            if skill.name in skills:
                return role

        return


class NotRecruitedTooltipData(BlocksTooltipData):

    def __init__(self, ctx):
        super(NotRecruitedTooltipData, self).__init__(ctx, TOOLTIP_TYPE.NOT_RECRUITED_TANKMAN)
        self._setWidth(350)
        self.item = None
        return

    def _packBlocks(self, *args, **kwargs):
        items = super(NotRecruitedTooltipData, self)._packBlocks()
        item = self.context.buildItem(*args)
        self.item = item
        blocks = list()
        blocks.append(formatters.packImageTextBlockData(title=text_styles.highTitle(item.getFullUserName()), desc=text_styles.main(item.getLabel())))
        specialIcon = item.getSpecialIcon()
        blocks.append(formatters.packImageBlockData(img=specialIcon if specialIcon is not None else item.getBigIcon(), align=BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER, width=350 if specialIcon is not None else -1, height=238 if specialIcon is not None else -1))
        blocks.append(formatters.packSeparatorBlockData(paddings=formatters.packPadding(top=-40)))
        descrStr = i18n.makeString(item.getDescription())
        hasDescr = descrStr != EMPTY_STRING
        if hasDescr:
            blocks.append(formatters.packTextBlockData(text_styles.main(descrStr), useHtml=True, padding=formatters.packPadding(top=18)))
        howToGetStr = i18n.makeString(item.getHowToGetInfo())
        hasHowToGetStr = howToGetStr != EMPTY_STRING
        if hasHowToGetStr:
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(backport.text(R.strings.tooltips.notrecruitedtankman.howToGet())), useHtml=True, padding=formatters.packPadding(top=17 if hasDescr else 18, bottom=5)))
            blocks.append(formatters.packTextBlockData(text_styles.main(howToGetStr), useHtml=True, padding=formatters.packPadding()))
        freeSkills = item.getFreeSkills()
        if freeSkills:
            tankmanSkill = item.getTankmanSkill()
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.NOTRECRUITEDTANKMAN_FREESKILLSTITLE), useHtml=True, padding=formatters.packPadding(top=17 if hasDescr else 18, bottom=10)))
            blocks.append(formatters.packImageListParameterBlockData(listIconSrc=[formatters.packImageListIconData(tankmanSkill(skillName=skillName).bigIconPath) for skillName in freeSkills], columnWidth=52, rowHeight=52, verticalGap=10, horizontalGap=10))
        skills = item.getEarnedSkills(multiplyNew=True)
        if skills:
            tankmanSkill = item.getTankmanSkill()
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.NOTRECRUITEDTANKMAN_SKILLSTITLE), useHtml=True, padding=formatters.packPadding(top=17 if hasDescr else 18, bottom=10)))
            blocks.append(formatters.packImageListParameterBlockData(listIconSrc=[formatters.packImageListIconData(tankmanSkill(skillName=skillName).bigIconPath) for skillName in skills], columnWidth=52, rowHeight=52, verticalGap=10, horizontalGap=10))
        expiryTime = item.getExpiryTime()
        if expiryTime:
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.NOTRECRUITEDTANKMAN_EXPIRETITLE), useHtml=True, padding=formatters.packPadding(top=20 if skills else 17 if hasDescr else 16, bottom=2)))
            expireDateStr = makeString(TOOLTIPS.NOTRECRUITEDTANKMAN_USEBEFORE, date=expiryTime)
            blocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.premiumVehicleName(expireDateStr), value=b'', icon=ICON_TEXT_FRAMES.RENTALS, padding=formatters.packPadding(left=-60, bottom=-18), iconYOffset=3))
        items.append(formatters.packBuildUpBlockData(blocks, padding=formatters.packPadding(bottom=-5)))
        return items


class BattleRoyaleTankmanTooltipDataBlock(BlocksTooltipData):
    _itemsCache = dependency.descriptor(IItemsCache)
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _skillIconNamePadding = {b'padding': (formatters.packPadding(left=65)), 
       b'titlePadding': (formatters.packPadding(left=6)), 
       b'iconPadding': (formatters.packPadding(top=-1))}

    def __init__(self, context):
        super(BattleRoyaleTankmanTooltipDataBlock, self).__init__(context, TOOLTIP_TYPE.SKILL)
        self._setWidth(320)
        self.item = None
        return

    def _packBlocks(self, *args, **kwargs):
        items = super(BattleRoyaleTankmanTooltipDataBlock, self)._packBlocks()
        item = self.context.buildItem(*args, **kwargs)
        if item is None:
            return items
        else:
            self.item = item
            vehicle = None
            if item.isInTank:
                vehicle = self._itemsCache.items.getVehicle(item.vehicleInvID)
            fullUserName = self._getFullUserName(item)
            titleBlock = [
             formatters.packTitleDescBlock(title=text_styles.highTitle(fullUserName), desc=text_styles.main(self._getTankmanDescription(item)))]
            items.append(formatters.packBuildUpBlockData(titleBlock))
            innerBlock = []
            if vehicle:
                self._createLabel(innerBlock)
                self._createVehicleBlock(innerBlock, vehicle)
            if innerBlock:
                items.append(formatters.packBuildUpBlockData(innerBlock, padding=formatters.packPadding(left=0, right=50, top=-5, bottom=0), linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE))
            commonStatsBlock = []
            self._createCommanderFeatureSkillsBlock(commonStatsBlock)
            self._createFreeSkillsBlock(commonStatsBlock)
            self._createEarnedSkillsBlock(commonStatsBlock)
            if commonStatsBlock:
                items.append(formatters.packBuildUpBlockData(commonStatsBlock, gap=5))
            return items

    @staticmethod
    def _makeXpToTankmanCaption():
        return formatters.packImageTextBlockData(img=backport.image(R.images.gui.maps.icons.library.tman_acc_training_24x24()), padding=formatters.packPadding(bottom=0, top=16, left=0), imgPadding=formatters.packPadding(top=-2, right=6), desc=text_styles.main(backport.text(R.strings.tooltips.hangar.crew.xpToTmen())))

    @staticmethod
    def _getSign(val):
        if val < 0:
            return b''
        return b'+'

    @staticmethod
    def _getBonusValue(tankman, ids):
        result = 0
        if tankman:
            bonuses = tankman.realRoleLevel.bonuses
            for idx in ids:
                result += bonuses[idx]

        return int(result)

    @staticmethod
    def _getVehicleName(vehicle=None, nativeVehicle=None):
        if not vehicle or nativeVehicle.shortUserName == vehicle.shortUserName:
            return text_styles.main(nativeVehicle.shortUserName)
        return text_styles.critical(nativeVehicle.shortUserName)

    @staticmethod
    def _createLabel(innerBlock):
        innerBlock.append(formatters.packTextBlockData(text=makeHtmlString(b'html_templates:lobby/textStyle', b'grayTitle', {b'message': (backport.text(R.strings.tooltips.hangar.crew.assignedTo()))})))
        return

    def _createFreeSkillsBlock(self, commonStatsBlock):
        return

    def _createCommanderFeatureSkillsBlock(self, commonStatsBlock):
        commanderFeatures = self._getCommanderFeatureList()
        if not commanderFeatures:
            return
        commonStatsBlock.append(formatters.packTextBlockData(text=makeHtmlString(b'html_templates:lobby/textStyle', b'grayTitle', {b'message': (makeString(TOOLTIPS.HANGAR_CREW_COMMANDERFEATURE))})))
        maxPopUpBlocks = 2
        for skill in commanderFeatures[:maxPopUpBlocks]:
            commonStatsBlock.append(formatters.packTextParameterBlockData(text_styles.main(skill[b'label']), text_styles.stats(str(skill[b'level']) + b'%'), valueWidth=90))

        return

    def _createEarnedSkillsBlock(self, commonStatsBlock):
        skills = self._getSkillList()
        if not skills:
            return
        commonStatsBlock.append(formatters.packTextBlockData(text=makeHtmlString(b'html_templates:lobby/textStyle', b'grayTitle', {b'message': (makeString(TOOLTIPS.HANGAR_CREW_SPECIALTY_SKILLS))})))
        maxPopUpBlocks = 14
        for skill in skills[:maxPopUpBlocks]:
            commonStatsBlock.append(formatters.packTextParameterBlockData(text_styles.main(skill[b'label']), text_styles.stats(str(skill[b'level']) + b'%'), valueWidth=90))

        if len(skills) > maxPopUpBlocks:
            diff = str(len(skills) - maxPopUpBlocks)
            commonStatsBlock.append(formatters.packAlignedTextBlockData(text=text_styles.middleTitle(makeString(TOOLTIPS.HANGAR_CREW_MORESKILLS, skill_cnt=diff)), align=BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER))
        return

    @classmethod
    def _getNewSkillsBlock(cls, isFree):
        if isFree:
            titleR = R.strings.tooltips.hangar.crew.new_free_skill_available.header()
        else:
            titleR = R.strings.tooltips.hangar.crew.new_skill_available.header()
        return formatters.packImageTextBlockData(img=b'../maps/icons/tankmen/skills/small/new_skill.png', txtOffset=20, padding=formatters.packPadding(bottom=0, top=5, left=0), imgPadding=formatters.packPadding(left=0, top=3), title=makeHtmlString(b'html_templates:lobby/textStyle', b'goldTextTitle', {b'message': (backport.text(titleR))}), desc=makeHtmlString(b'html_templates:lobby/textStyle', b'goldTextField', {b'message': (backport.text(R.strings.tooltips.hangar.crew.new_skill_available.text()))}))

    @staticmethod
    def _getFullUserName(item):
        nationName = nations.NAMES[item.nationID]
        nationResId = R.strings.battle_royale.commanderInfo.fullName.dyn(nationName)()
        result = backport.text(nationResId)
        return result

    @staticmethod
    def _getTankmanDescription(_):
        return backport.text(R.strings.battle_royale.commanderInfo.commonRank())

    def _getSkillList(self):
        skillListField = BattleRoyaleTankmanSkillListField(self, b'skills')
        _, value = skillListField.buildData()
        if value is None:
            return []
        else:
            return [skill for skill in value if skill[b'typeName'] != b'commanderSpecial']

    def _getCommanderFeatureList(self):
        skillListField = BattleRoyaleTankmanSkillListField(self, b'skills')
        _, value = skillListField.buildData()
        if value is None:
            return []
        else:
            return [skill for skill in value if skill[b'typeName'] == b'commanderSpecial']

    @staticmethod
    def _createVehicleBlock(innerBlock, vehicle):
        vehName = vehicle.shortUserName
        innerBlock.append(formatters.packTextBlockData(text=text_styles.stats(backport.text(R.strings.battle_royale.commanderTooltip.vehicleDescription(), vehicle=vehName)), padding=formatters.packPadding(top=10, right=-50)))
        return


class TankmanTooltipData(ToolTipData):

    def __init__(self, context):
        super(TankmanTooltipData, self).__init__(context, TOOLTIP_TYPE.TANKMAN)
        self.fields = (
         ToolTipAttrField(self, b'name', b'fullUserName'),
         ToolTipAttrField(self, b'rank', b'rankUserName'),
         ToolTipAttrField(self, b'role', b'roleUserName'),
         ToolTipAttrField(self, b'roleLevel'),
         ToolTipAttrField(self, b'isInTank'),
         ToolTipAttrField(self, b'iconRole'),
         ToolTipAttrField(self, b'nation', b'nationID'),
         TankmanRoleLevelField(self, b'efficiencyRoleLevel'),
         TankmanRoleBonusesField(self, b'addition', [
          TankmanRoleBonusesField.BONUSES.COMMANDER,
          TankmanRoleBonusesField.BONUSES.EQUIPMENTS,
          TankmanRoleBonusesField.BONUSES.DEVICES,
          TankmanRoleBonusesField.BONUSES.BROTHERHOOD]),
         TankmanRoleBonusesField(self, b'penalty', [TankmanRoleBonusesField.BONUSES.PENALTY]),
         TankmanNativeVehicleAttrField(self, b'vehicleType', b'type'),
         TankmanNativeVehicleAttrField(self, b'vehicleName', b'shortUserName'),
         TankmanCurrentVehicleAttrField(self, b'currentVehicleType', b'type'),
         TankmanCurrentVehicleAttrField(self, b'currentVehicleName', b'shortUserName'),
         TankmanSkillListField(self, b'skills'),
         TankmanNewSkillCountField(self, b'newSkillsCount'),
         TankmanCurrentVehicleAttrField(self, b'vehicleContour', b'iconContour'),
         TankmanCurrentVehicleAttrField(self, b'isCurrentVehiclePremium', b'isPremium'),
         TankmanStatusField(self, b'status'))
        return
