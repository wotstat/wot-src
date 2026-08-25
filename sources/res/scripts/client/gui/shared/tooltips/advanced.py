from __future__ import absolute_import
from constants import SHELL_TYPES
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
from gui.shared.formatters import text_styles
from gui.shared.gui_items.artefacts import OptionalDevice
from gui.shared.tooltips import formatters, ToolTipBaseData
from gui.shared.tooltips.common import BlocksTooltipData
from helpers import dependency
from helpers import i18n
from skeletons.account_helpers.settings_core import ISettingsCore
from vehicles.mechanics.mechanic_constants import VehicleMechanic
DISABLED_ITEMS_ID = 12793
CHASSIS_TRACK_WITHIN_TRACK = b'vehicleTrackWithinTrackChassis'

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
        disabledForWheeled = False
        if self._item is not None:
            if isinstance(self._item, OptionalDevice):
                disabledForWheeled = self._item.intCD == DISABLED_ITEMS_ID
        if disabledForWheeled:
            return []
        else:
            items.extend(self._getBlocksList(*args, **kwargs))
            return items

    def _getBlocksList(self, *args, **kwargs):
        return

    def _getDescrText(self, description, descReady=False):
        tokens = description.split(b'|')
        if len(tokens) == 2:
            description = tokens[1]
        if not descReady:
            descrTextR = R.strings.tooltips.advanced.dyn(description)
            if descrTextR and descrTextR.isValid():
                descrText = backport.text(descrTextR())
            else:
                descrText = b'#tooltips:advanced/' + description
        else:
            descrText = description
        return descrText

    def _packAdvancedBlocks(self, movie, header, description, descReady=False):
        descrText = self._getDescrText(description, descReady)
        items = [
         formatters.packTextBlockData(text=text_styles.highTitle(header), padding=formatters.packPadding(left=20, top=20))]
        if movie is not None:
            items.append(formatters.packImageBlockData(BaseAdvancedTooltip.getMovieAnimationPath(movie), BLOCKS_TOOLTIP_TYPES.ALIGN_LEFT, padding=5, linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_ADVANCED_CLIP_BLOCK_LINKAGE))
        items.append(formatters.packTextBlockData(text=text_styles.main(descrText), padding=formatters.packPadding(left=20, top=10, bottom=20)))
        return items


class AdvancedTooltipWithMechanics(BaseAdvancedTooltip):

    def _hasMechanic(self, vehicle, mechanicName):
        return mechanicName in vehicle.getMechanics()

    def _getDescrText(self, description, descReady=False):
        descrText = super(AdvancedTooltipWithMechanics, self)._getDescrText(description, descReady)
        statsConfig = self.context.getStatsConfiguration(self._item)
        vehicle = statsConfig.vehicle
        if vehicle is not None and self._hasMechanic(vehicle, VehicleMechanic.LOW_CHARGE_SHOT):
            descrText = text_styles.concatStylesToMultiLine(text_styles.concatStylesToMultiLine(descrText, b''), i18n.makeString(TOOLTIPS.ADVANCED_LOW_CHARGE_SHOT_FOOTER, fireMode=text_styles.stats(TOOLTIPS.ADVANCED_LOW_CHARGE_SHOT_FIREMODE), fireRate=text_styles.stats(TOOLTIPS.ADVANCED_LOW_CHARGE_SHOT_FIRERATE)))
        return descrText


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


class HangarShellAdvanced(AdvancedTooltipWithMechanics):
    _MODERN_SUFFIX = b'_MODERN'
    _NOT_PIERCING_DAMAGE = b'_NOT_PIERCING_DAMAGE'
    _TRAY = b'_TRAY'

    def _getBlocksList(self, *args, **kwargs):
        movie = SHELL_MOVIES.get(self._item.getAdvancedTooltipKey(), None)
        header = backport.text(R.strings.tooltips.advanced.header.shellType.dyn(self._item.type, default=R.invalid)())
        description = self._item.type + self._getDescriptionSuffix()
        return self._packAdvancedBlocks(movie, header, description)

    def _getDescriptionSuffix(self):
        suffix = b''
        if self._item.isModernMechanics:
            suffix = self._MODERN_SUFFIX
        elif self._item.isNonPiercingDamageMechanics:
            suffix = self._NOT_PIERCING_DAMAGE
        elif self._item.isDamageMutable():
            suffix = self._TRAY
        return suffix


class HangarBoosterAdvanced(BaseAdvancedTooltip):

    def _getBlocksList(self, *args, **kwargs):
        item = self._item
        itemId = item.getGUIEmblemID()
        header = self._item.userName
        descReady = False
        if b'crewSkillBattleBooster' in item.tags:
            movie = SKILL_MOVIES[itemId]
            affectedSkillName = item.getAffectedSkillName()
            skillLocales = R.strings.crew_perks.dyn(affectedSkillName)
            itemId = backport.text(skillLocales.shortDescription()) if skillLocales.isValid() else affectedSkillName
            descReady = True
        else:
            movie = MODULE_MOVIES[itemId]
        return self._packAdvancedBlocks(movie, header, itemId, descReady)


class HangarModuleAdvanced(AdvancedTooltipWithMechanics):

    def _hasMechanic(self, vehicle, mechanicName):
        mechanics = self._item.getMechanics(vehicle.descriptor) or ()
        return mechanicName in mechanics

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
        elif isEquipment and item.isStimulator:
            descrKey = b'ration'
        statsConfig = self.context.getStatsConfiguration(self._item)
        vehicle = statsConfig.vehicle
        mechanics = item.getMechanics(vehicle.descriptor) if vehicle is not None else ()
        movieModule = None
        for mechanicName in mechanics:
            movieModule = MODULE_MOVIES.get(b'%s_%s' % (movieKey, mechanicName.value))
            if movieModule:
                break

        if not movieModule:
            movieModule = MODULE_MOVIES.get(movieKey)
        return self._packAdvancedBlocks(movieModule, header, descrKey)


class TankmanPreviewTooltipAdvanced(BaseAdvancedTooltip):

    def _packBlocks(self, role, *args, **kwargs):
        return self._packAdvancedBlocks(TANKMAN_MOVIES[role], ITEM_TYPES.tankman_roles(role), role)


class VehicleParametersAdvanced(ToolTipBaseData):
    _movies = {b'relativePower': b'statFirepower', 
       b'relativeArmor': b'statSurvivability', 
       b'relativeMobility': b'statMobility', 
       b'relativeCamouflage': b'statConcealment', 
       b'relativeVisibility': b'statSpotting'}

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
   b'armorPatching': b'skillArmorPatching', 
   b'commander_tutor': b'skillCommanderTutor', 
   b'commander_eagleEye': b'skillEagleEye', 
   b'commander_universalist': b'skillJackOfAllTrades', 
   b'commander_coordination': b'skillCommanderCoordination', 
   b'commander_sixthSense': b'skillSixthSense', 
   b'commander_enemyShotPredictor': b'skillCommanderEnemyShotPredictor', 
   b'commander_practical': b'skillCommanderPractical', 
   b'commander_emergency': b'skillCommanderEmergency', 
   b'commander_holdLine': b'skillHoldLine', 
   b'commander_staySharp': b'skillStaySharp', 
   b'gunner_rancorous': b'skillDesignatedTarget', 
   b'gunner_armorer': b'skillGunnerArmorer', 
   b'gunner_sniper': b'skillSniper', 
   b'gunner_smoothTurret': b'skillSnapShot', 
   b'gunner_focus': b'skillGunnerFocus', 
   b'gunner_quickAiming': b'skillGunnerQuickAiming', 
   b'gunner_pointBlast': b'skillPointBlast', 
   b'gunner_loneWolf': b'skillGunnerLoneWolf', 
   b'driver_rammingMaster': b'skillDriverRammingMaster', 
   b'driver_badRoadsKing': b'skillOffRoadDriving', 
   b'driver_tidyPerson': b'skillPreventativeMaintenance', 
   b'driver_virtuoso': b'skillClutchBraking', 
   b'driver_smoothDriving': b'skillSmoothRide', 
   b'driver_motorExpert': b'skillDriverMotorExpert', 
   b'driver_reliablePlacement': b'skillDriverReliablePlacement', 
   b'driver_suspensionRepair': b'skillSuspensionRepair', 
   b'driver_bulletproof': b'skillBulletproof', 
   b'radioman_finder': b'skillSituationalAwareness', 
   b'radioman_expert': b'skillRadiomanExpert', 
   b'radioman_sideBySide': b'skillRadiomanSideBySide', 
   b'radioman_interference': b'skillRadiomanInterference', 
   b'radioman_signalInterception': b'skillRadiomanSignalInterception', 
   b'radioman_battleTempered': b'skillBattleTempered', 
   b'radioman_threatSearch': b'skillThreatSearch', 
   b'loader_desperado': b'skillAdrenalineRush', 
   b'loader_pedant': b'skillSafeStowage', 
   b'loader_intuition': b'skillIntuition', 
   b'loader_ambushMaster': b'skillAmbushMaster', 
   b'loader_ammunitionImprove': b'skillLoaderAmmunitionImprove', 
   b'loader_melee': b'skillLoaderMelee', 
   b'loader_magMastery': b'skillMagMastery', 
   b'loader_perfectCharge': b'skillLoaderPerfectCharge', 
   b'loader_secondChance': b'skillSecondChance'}
MODULE_MOVIES = {b'largeRepairkit': b'consumablesRepairKitBig', 
   b'smallRepairkit': b'consumablesRepairKitSmall', 
   b'largeMedkit': b'consumablesFirstAidBig', 
   b'smallMedkit': b'consumablesFirstAidSmall', 
   b'autoExtinguishers': b'consumablesExtinguisherBig', 
   b'handExtinguishers': b'consumablesExtinguisherSmall', 
   b'qualityFuel': b'consumablesQualityFuel', 
   b'excellentFuel': b'consumablesExcellentFuel', 
   b'removedRpmLimiter': b'consumablesSpeedGovernorRemoved', 
   b'aimingStabilizer': b'equipmentVerticalStabilizer', 
   b'enhancedAimDrives': b'equipmentGunLayingDrive', 
   b'coatedOptics': b'equipmentCoatedOptics', 
   b'stereoscope': b'equipmentBinocularTelescope', 
   b'camouflageNet': b'equipmentCamouflageNet', 
   b'antifragmentationLining': b'equipmentLightSpallLiner', 
   b'improvedVentilation': b'equipmentImprovedVentilation', 
   b'rammer': b'equipmentMediumCaliberTankGunRammer', 
   b'vehicleGun': b'moduleGun', 
   b'vehicleGun_lowChargeShot': b'moduleGun_lowChargeShot', 
   b'vehicleDualGun': b'moduleDualGun', 
   b'vehicleRadio': b'moduleRadio', 
   b'vehicleEngine': b'moduleEngine', 
   b'vehicleChassis': b'moduleSuspension', 
   b'vehicleWheeledChassis': b'moduleWheel', 
   b'vehicleTrackWithinTrackChassis': b'moduleTrackWithinTrack', 
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
   b'modernizedImprovedSightsEnhancedAimDrives': b'equipmentExperimentalAccuracy', 
   b'modernizedAimDrivesAimingStabilizer': b'equipmentExperimentalAiming', 
   b'modernizedExtraHealthReserveAntifragmentationLining': b'equipmentExperimentalHardening', 
   b'modernizedTurbochargerRotationMechanism': b'equipmentExperimentalTurbocharger', 
   b'improvedSights': b'equipmentImprovedAiming', 
   b'extraHealthReserve': b'equipmentImprovedHardening', 
   b'improvedRadioCommunication': b'equipmentImprovedRadioSet', 
   b'improvedRotationMechanism': b'equipmentImprovedRotationMechanism', 
   b'additionalInvisibilityDevice': b'equipmentLowNoiseExhaustSystem', 
   b'improvedConfiguration': b'equipmentModifiedConfiguration', 
   b'turbocharger': b'equipmentTurbocharger'}
TANKMAN_MOVIES = {b'commander': b'crewCommander', 
   b'driver': b'crewDriver', 
   b'gunner': b'crewGunner', 
   b'loader': b'crewLoader', 
   b'radioman': b'crewRadioOperator'}
SHELL_MOVIES = {(SHELL_TYPES.ARMOR_PIERCING, False, False, False): b'bulletAP', 
   (SHELL_TYPES.HOLLOW_CHARGE, False, False, False): b'bulletHEAT', 
   (SHELL_TYPES.HIGH_EXPLOSIVE, False, False, False): b'bulletHE', 
   (SHELL_TYPES.ARMOR_PIERCING_CR, False, False, False): b'bulletAPCR', 
   (SHELL_TYPES.HIGH_EXPLOSIVE, True, False, False): b'bulletHEModern', 
   (SHELL_TYPES.ARMOR_PIERCING, False, True, False): b'bulletAP', 
   (SHELL_TYPES.ARMOR_PIERCING_CR, False, True, False): b'bulletAPCR', 
   (SHELL_TYPES.ARMOR_PIERCING, False, False, True): b'bulletAPMutable', 
   (SHELL_TYPES.ARMOR_PIERCING_CR, False, False, True): b'bulletAPCRMutable'}
