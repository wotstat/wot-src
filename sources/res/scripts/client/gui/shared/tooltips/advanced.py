import typing
from constants import SHELL_TYPES, QUEUE_TYPE
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.goodies.goodie_items import DemountKit
from gui.impl import backport
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.gen import R
from gui.prb_control.settings import PREBATTLE_ACTION_NAME
from gui.prb_control.dispatcher import g_prbLoader
from gui.shared.formatters import text_styles
from gui.shared.gui_items.artefacts import OptionalDevice, Equipment
from gui.shared.tooltips import formatters, ToolTipBaseData
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency
from helpers import i18n
from skeletons.account_helpers.settings_core import ISettingsCore
from fun_random.gui.fun_gui_constants import DISABLED_ADVANCED_TOOLTIPS_ITEMS_CD
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.vehicle_modules import Shell
DISABLED_ITEMS_ID = 12793
CHASSIS_TRACK_WITHIN_TRACK = b'vehicleTrackWithinTrackChassis'
MULTI_TRACK_CHASSIS = b'vehicleMultiTrackChassis'
AUTO_SHOOT_FLAME_GUN = b'vehicleAutoShootFlameGun'
AUTO_SHOOT_GUN = b'vehicleAutoShootGun'
THERMAL_VISION = b'vehicleThermalVision'

def getPreparedShellItemType(item):
    itemType = item.kind
    if item.isModernMechanics:
        itemType += _MODERN_POSTFIX
    elif item.hasStun:
        itemType += _STUN_POSTFIX
    return itemType


class ComplexTooltip(BlocksTooltipData):
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, context, disableAnim):
        super(ComplexTooltip, self).__init__(context, None)
        self._setMargins(11, 14)
        self._setWidth(520)
        self._disableAnim = disableAnim
        return

    def _packBlocks(self, *args, **kwargs):
        items = super(ComplexTooltip, self)._packBlocks(*args, **kwargs)
        strs = args[0].split(b'<br/>')
        items.append(formatters.packImageTextBlockData(title=strs[0], desc=strs[1]))
        block = formatters.packImageTextBlockData(img=RES_ICONS.MAPS_ICONS_LOBBY_ICONBTNALT, txtOffset=40, padding=formatters.packPadding(bottom=-7, top=-5, left=20 - self._getContentMargin()[b'left']), desc=text_styles.main(TOOLTIPS.ADVANCED_INFO), linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_ADVANCED_KEY_BLOCK_LINKAGE)
        block[b'data'][b'animated'] = not self._disableAnim
        items.append(block)
        return items


class BaseAdvancedTooltip(BlocksTooltipData):

    def __init__(self, context):
        super(BaseAdvancedTooltip, self).__init__(context, None)
        self._setContentMargin(top=2, left=3, bottom=3, right=3)
        self._setMargins(afterBlock=0)
        self._setWidth(415)
        self._item = None
        return

    @staticmethod
    def getMovieAnimationPath(moviename):
        return b'animations/advancedHints/%s.swf' % moviename

    def _packBlocks(self, *args, **kwargs):
        from debug_utils import LOG_DEBUG
        LOG_DEBUG(b'packBlocks::', args, kwargs, self.context)
        self._item = self.context.buildItem(*args, **kwargs)
        items = super(BaseAdvancedTooltip, self)._packBlocks()
        entity = g_prbLoader.getDispatcher().getEntity()
        disableForWheeled = isinstance(self._item, OptionalDevice) and self._item.intCD == DISABLED_ITEMS_ID
        disableAdvAnim = isinstance(self._item, Equipment) and entity.getEntityType() == QUEUE_TYPE.FUN_RANDOM and self._item.intCD in DISABLED_ADVANCED_TOOLTIPS_ITEMS_CD
        if disableForWheeled or disableAdvAnim:
            return []
        items.extend(self._getBlocksList(*args, **kwargs))
        return items

    def _getBlocksList(self, *args, **kwargs):
        return

    def _packAdvancedBlocks(self, movie, header, description, descReady=False):
        if not descReady:
            descrTextR = R.strings.tooltips.advanced.dyn(description)
            if descrTextR and descrTextR.isValid():
                descrText = backport.text(descrTextR())
            else:
                descrText = b'#tooltips:advanced/' + description
        else:
            descrText = description
        if movie is None:
            items = [
             formatters.packTextBlockData(text=text_styles.highTitle(header), padding=formatters.packPadding(left=20, top=20)),
             formatters.packTextBlockData(text=text_styles.main(descrText), padding=formatters.packPadding(left=20, top=10, bottom=20))]
        else:
            items = [
             formatters.packTextBlockData(text=text_styles.highTitle(header), padding=formatters.packPadding(left=20, top=20)),
             formatters.packImageBlockData(BaseAdvancedTooltip.getMovieAnimationPath(movie), BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT, padding=5, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_ADVANCED_CLIP_BLOCK_LINKAGE),
             formatters.packTextBlockData(text=text_styles.main(descrText), padding=formatters.packPadding(left=20, top=10, bottom=20))]
        return items


class FakeAdvancedTooltip(BaseAdvancedTooltip):

    def _getBlocksList(self, *args, **kwargs):
        return []


class ComplexAdvanced(BaseAdvancedTooltip):

    def _getBlocksList(self, item, *args, **kwargs):
        text, linkage = item
        headerKey = (b'#tooltips:advanced/{}/header').format(text)
        if headerKey in TOOLTIPS.ADVANCED_ENUM:
            header = headerKey
        else:
            header = linkage + b'/header'
        return self._packAdvancedBlocks(text, header, text)


class HangarShellAdvanced(BaseAdvancedTooltip):

    def _getBlocksList(self, *args, **kwargs):
        item = self._item
        header = backport.text(R.strings.tooltips.advanced.header.shellType.dyn(item.kind, default=R.invalid)())
        preparedItemType = getPreparedShellItemType(item)
        movie = SHELL_MOVIES.get(preparedItemType, None)
        return self._packAdvancedBlocks(movie=movie, header=header, description=preparedItemType)


class HangarBoosterAdvanced(BaseAdvancedTooltip):

    def _getBlocksList(self, *args, **kwargs):
        item = self._item
        itemId = descr = item.getGUIEmblemID()
        movie = MODULE_MOVIES.get(itemId, None)
        header = item.userName
        descReady = False
        if item.isCrewBooster():
            movie = SKILL_MOVIES[itemId]
            affectedSkillName = item.getAffectedSkillName()
            skillLocales = R.strings.crew_perks.dyn(affectedSkillName)
            descr = backport.text(skillLocales.shortDescription()) if skillLocales.isValid() else affectedSkillName
            descReady = True
        elif item.isEconomicBooster():
            descr = item.descriptor.shortDescriptionSpecial
            descReady = True
        return self._packAdvancedBlocks(movie, header, descr, descReady)


class HangarModuleAdvanced(BaseAdvancedTooltip):

    def _getBlocksList(self, *args, **kwargs):
        item = self._item
        itemId = item.getGUIEmblemID()
        movieKey = itemId
        descrKey = itemId
        isEquipment = item.itemTypeName == STORE_CONSTANTS.EQUIPMENT
        isOptionalDevice = item.itemTypeName == STORE_CONSTANTS.OPTIONAL_DEVICE
        if isEquipment or isOptionalDevice:
            header = self._item.shortUserName
        else:
            header = self._item.userType
        if itemId == FITTING_TYPES.VEHICLE_CHASSIS and item.isTrackWithinTrack():
            movieKey = CHASSIS_TRACK_WITHIN_TRACK
            descrKey = CHASSIS_TRACK_WITHIN_TRACK
        if isEquipment:
            if itemId in (b'lendLeaseOil', b'qualityOil'):
                descrKey = b'enhancedOil'
            elif item.isStimulator:
                descrKey = b'ration'
        if itemId == FITTING_TYPES.VEHICLE_CHASSIS and item.isMultiTrack():
            movieKey = MULTI_TRACK_CHASSIS
            descrKey = MULTI_TRACK_CHASSIS
        if itemId == FITTING_TYPES.VEHICLE_GUN and item.isAutoShootFlameGun():
            movieKey = AUTO_SHOOT_FLAME_GUN
            descrKey = AUTO_SHOOT_FLAME_GUN
        if itemId == FITTING_TYPES.VEHICLE_GUN and item.isAutoShootGun():
            movieKey = AUTO_SHOOT_GUN
            descrKey = AUTO_SHOOT_GUN
        if itemId == FITTING_TYPES.VEHICLE_TURRET and item.hasThermalVision():
            movieKey = THERMAL_VISION
            descrKey = THERMAL_VISION
        if movieKey not in MODULE_MOVIES:
            movieModule = None
        else:
            movieModule = MODULE_MOVIES[movieKey]
        return self._packAdvancedBlocks(movieModule, header, descrKey)


class TankmanPreviewTooltipAdvanced(BaseAdvancedTooltip):

    def _packBlocks(self, role, *args, **kwargs):
        return self._packAdvancedBlocks(TANKMAN_MOVIES[role], ITEM_TYPES.tankman_roles(role), role)


class VehicleParametersAdvanced(ToolTipBaseData):
    _movies = {b'relativePower': b'statFirepower', 
       b'relativeArmor': b'statSurvivability', 
       b'relativeMobility': b'statMobility', 
       b'relativeCamouflage': b'statConcealment', 
       b'relativeVisibility': b'statSpotting', 
       b'relativeAbility': b'abilityPreview'}

    def __init__(self, context):
        super(VehicleParametersAdvanced, self).__init__(context, None)
        return

    def getDisplayableData(self, paramName, *args, **kwargs):
        from gui.impl.lobby.crew.tooltips.advanced_tooltip_view import AdvancedTooltipView
        return DecoratedTooltipWindow(AdvancedTooltipView(self._movies[paramName], backport.text(R.strings.menu.tank_params.dyn(paramName)()), backport.text(R.strings.tooltips.advanced.dyn(paramName)())), useDecorator=False)


class MoneyAndXpAdvanced(BaseAdvancedTooltip):
    _moviesOrDescriptions = {b'crystal': b'economyBonds', 
       b'credits': b'economyCredits', 
       b'gold': b'economyGold', 
       b'freeXP': b'economyConvertExp'}

    def _getBlocksList(self, *args, **kwargs):
        _type = args[0]
        movie = self._moviesOrDescriptions[_type]
        header = TOOLTIPS.getHeaderBtnTitle(_type)
        description = self._moviesOrDescriptions[_type]
        return self._packAdvancedBlocks(movie, header, description)


class RankedAdvanced(BaseAdvancedTooltip):

    def _getBlocksList(self, *args, **kwargs):
        return self._packAdvancedBlocks(b'gamemodeRanked', i18n.makeString(TOOLTIPS.BATTLETYPES_RANKED + b'/header'), PREBATTLE_ACTION_NAME.RANKED)


class DemountKitTooltipAdvanced(BaseAdvancedTooltip):

    def _packBlocks(self, *args, **kwargs):
        demountKit = self.context.buildItem(*args, **kwargs)
        dkType = demountKit.demountKitGuiType
        return self._packAdvancedBlocks(b'demountKit', demountKit.userName, (b'demountKit/{}').format(dkType))


SKILL_MOVIES = {b'repair': b'skillRepairs', 
   b'camouflage': b'skillConcealment', 
   b'naturalCover': b'skillConcealment', 
   b'fireFighting': b'skillFirefighting', 
   b'brotherhood': b'skillBrothersInArms', 
   b'commander_tutor': b'skillMentor', 
   b'commander_eagleEye': b'skillEagleEye', 
   b'commander_universalist': b'skillJackOfAllTrades', 
   b'commander_expert': b'skillExpert', 
   b'commander_sixthSense': b'skillSixthSense', 
   b'gunner_rancorous': b'skillDesignatedTarget', 
   b'gunner_gunsmith': b'skillArmorer', 
   b'gunner_sniper': b'skillDeadEye', 
   b'gunner_smoothTurret': b'skillSnapShot', 
   b'driver_rammingMaster': b'skillControlledImpact', 
   b'driver_badRoadsKing': b'skillOffRoadDriving', 
   b'driver_tidyPerson': b'skillPreventativeMaintenance', 
   b'driver_virtuoso': b'skillClutchBraking', 
   b'driver_smoothDriving': b'skillSmoothRide', 
   b'radioman_finder': b'skillSituationalAwareness', 
   b'radioman_lastEffort': b'skillCallForVengeance', 
   b'radioman_inventor': b'skillSignalBoosting', 
   b'radioman_retransmitter': b'skillRelaying', 
   b'loader_desperado': b'skillAdrenalineRush', 
   b'loader_pedant': b'skillSafeStowage', 
   b'loader_intuition': b'skillIntuition', 
   b'commander_enemyShotPredictor': b'skillArtLamp'}
MODULE_MOVIES = {b'largeRepairkit': b'consumablesRepairKitBig', 
   b'smallRepairkit': b'consumablesRepairKitSmall', 
   b'largeMedkit': b'consumablesFirstAidBig', 
   b'smallMedkit': b'consumablesFirstAidSmall', 
   b'autoExtinguishers': b'consumablesExtinguisherBig', 
   b'handExtinguishers': b'consumablesExtinguisherSmall', 
   b'lendLeaseOil': b'consumablesOilLendLease', 
   b'qualityOil': b'consumablesOilQuality', 
   b'removedRpmLimiter': b'consumablesSpeedGovernorRemoved', 
   b'gasoline105': b'consumablesGasoline105', 
   b'gasoline100': b'consumablesGasoline100', 
   b'aimingStabilizer': b'equipmentVerticalStabilizer', 
   b'enhancedAimDrives': b'equipmentGunLayingDrive', 
   b'coatedOptics': b'equipmentCoatedOptics', 
   b'stereoscope': b'equipmentBinocularTelescope', 
   b'camouflageNet': b'equipmentCamouflageNet', 
   b'antifragmentationLining': b'equipmentLightSpallLiner', 
   b'improvedVentilation': b'equipmentImprovedVentilation', 
   b'rammer': b'equipmentMediumCaliberTankGunRammer', 
   b'vehicleGun': b'moduleGun', 
   b'vehicleDualGun': b'moduleDualGun', 
   b'dualGunCooling': b'dualgunCooling', 
   b'gunCooling': b'gunCooling', 
   AUTO_SHOOT_FLAME_GUN: b'moduleTemperatureGun', 
   AUTO_SHOOT_GUN: b'moduleAutogun', 
   b'vehicleRadio': b'moduleRadio', 
   b'vehicleEngine': b'moduleEngine', 
   b'vehicleChassis': b'moduleSuspension', 
   b'vehicleWheeledChassis': b'moduleWheel', 
   b'vehicleTrackWithinTrackChassis': b'moduleTrackWithinTrack', 
   b'vehicleMultiTrackChassis': b'moduleTrackWithinTrack', 
   b'vehicleTurret': b'moduleTurret', 
   b'cocacola': b'consumablesCola', 
   b'chocolate': b'consumablesChocolate', 
   b'ration': b'consumablesExtraCombatRations', 
   b'hotCoffee': b'consumablesStrongCoffee', 
   b'ration_china': b'consumablesImprovedCombatRations', 
   b'ration_uk': b'consumablesPuddingAndTea', 
   b'ration_japan': b'consumablesOnigiri', 
   b'ration_czech': b'consumablesBuchty', 
   b'ration_sweden': b'consumablesCoffeeWithCinnamonBuns', 
   b'ration_poland': b'consumablesBreadWithSchmaltz', 
   b'ration_italy': b'consumablesSpaghetti', 
   b'ration_intunion': b'consumables_intunion', 
   b'grousers': b'equipmentAdditionalGrousers', 
   b'artillery': b'artillery', 
   b'bomber': b'bomber', 
   b'inspire': b'inspire', 
   b'arcade_minefield': b'minefield', 
   b'stealthRadar': b'patrol', 
   b'recon': b'recon', 
   b'regenerationKit': b'resuply', 
   b'passive_engineering': b'sabotageSquad', 
   b'smoke': b'smokeCloud', 
   b'commandersView': b'equipmentCommandersVisionSystem', 
   b'modernizedAimDrivesAimingStabilizer': b'equipmentExperimentalAiming', 
   b'modernizedExtraHealthReserveAntifragmentationLining': b'equipmentExperimentalHardening', 
   b'modernizedTurbochargerRotationMechanism': b'equipmentExperimentalTurbocharger', 
   b'improvedSights': b'equipmentImprovedAiming', 
   b'extraHealthReserve': b'equipmentImprovedHardening', 
   b'improvedRadioCommunication': b'equipmentImprovedRadioSet', 
   b'improvedRotationMechanism': b'equipmentImprovedRotationMechanism', 
   b'additionalInvisibilityDevice': b'equipmentLowNoiseExhaustSystem', 
   b'improvedConfiguration': b'equipmentModifiedConfiguration', 
   b'turbocharger': b'equipmentTurbocharger', 
   THERMAL_VISION: b'thermalVision', 
   b'modernizedDamageVentilation': b'equipmentExperimentalDamageVentilation', 
   b'modernizedTankRammerSights': b'equipmentExperimentalTankRammerSights', 
   b'wt_largeMedkit': b'consumablesFirstAidWt', 
   b'wt_largeRepairkit': b'consumablesRepairKitBig', 
   b'xpDirectivesBattleBooster1': b'xpDirectivesBattleBooster', 
   b'xpDirectivesBattleBooster2': b'xpDirectivesBattleBooster', 
   b'xpDirectivesBattleBooster3': b'xpDirectivesBattleBooster', 
   b'creditsDirectivesBattleBooster1': b'creditsDirectivesBattleBooster', 
   b'creditsDirectivesBattleBooster2': b'creditsDirectivesBattleBooster', 
   b'creditsDirectivesBattleBooster3': b'creditsDirectivesBattleBooster', 
   b'comboXpDirectivesBattleBooster1': b'comboXpDirectivesBattleBooster', 
   b'comboXpDirectivesBattleBooster2': b'comboXpDirectivesBattleBooster', 
   b'comboXpDirectivesBattleBooster3': b'comboXpDirectivesBattleBooster'}
TANKMAN_MOVIES = {b'commander': b'crewCommander', 
   b'driver': b'crewDriver', 
   b'gunner': b'crewGunner', 
   b'loader': b'crewLoader', 
   b'radioman': b'crewRadioOperator'}
_MODERN_POSTFIX = b'_MODERN'
_STUN_POSTFIX = b'_STUN'
_DISTANCE_FACTOR_POSTFIX = b'_DF'
SHELL_MOVIES = {(SHELL_TYPES.ARMOR_PIERCING): b'bulletAP', 
   (SHELL_TYPES.HOLLOW_CHARGE): b'bulletHEAT', 
   (SHELL_TYPES.HIGH_EXPLOSIVE): b'bulletHE', 
   (SHELL_TYPES.ARMOR_PIERCING_CR): b'bulletAPCR', 
   (SHELL_TYPES.ARMOR_PIERCING_FSDS): b'bulletAPFSDS', 
   (SHELL_TYPES.HIGH_EXPLOSIVE + _MODERN_POSTFIX): b'bulletHEModern', 
   (SHELL_TYPES.HIGH_EXPLOSIVE + _STUN_POSTFIX): b'bulletHE', 
   (SHELL_TYPES.FLAME): b'bulletFlame', 
   (SHELL_TYPES.FLAME + _STUN_POSTFIX): b'bulletFlameStun', 
   (SHELL_TYPES.ARMOR_PIERCING + _DISTANCE_FACTOR_POSTFIX): b'bulletAP_DF', 
   (SHELL_TYPES.HIGH_EXPLOSIVE + _DISTANCE_FACTOR_POSTFIX + _MODERN_POSTFIX): b'bulletHEModern_DF', 
   (SHELL_TYPES.HIGH_EXPLOSIVE + _DISTANCE_FACTOR_POSTFIX): b'bulletHEModern_DF', 
   (SHELL_TYPES.HOLLOW_CHARGE + _DISTANCE_FACTOR_POSTFIX): b'bulletHEAT_DF'}
