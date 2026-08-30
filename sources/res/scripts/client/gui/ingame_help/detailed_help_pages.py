import logging, typing, CommandMapping
from constants import ARENA_GUI_TYPE, ARENA_BONUS_TYPE, ROLE_TYPE, ACTION_TYPE_TO_LABEL, ROLE_TYPE_TO_LABEL
from gui import makeHtmlString
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HelpHintContext
from gui.comp7.comp7_helpers import getComp7DetailedHelpPages
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.shared.system_factory import registerIngameHelpPagesBuilders, collectIngameHelpPagesBuilders
from gui.shared.utils.functions import replaceHyphenToUnderscore
from gui.shared.utils.key_mapping import getReadableKey, getVirtualKey
from items.vehicles import getRolesActions
from nations import NAMES as NATIONS_NAMES
from shared_utils import findFirst
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from skeletons.gui.battle_session import IClientArenaVisitor
    from Vehicle import Vehicle
_logger = logging.getLogger(__name__)

class HelpPagePriority(object):
    DEFAULT = 0
    MAPS = 1
    TRACK_WITHIN_TRACK = 2
    MULTI_TRACK = 2
    ROCKET_ACCELERATION = 3
    TURBOSHAFT_ENGINE = 4
    BATTLE_ROYALE = 6
    DUAL_GUN = 7
    WHEELED = 8
    DUAL_ACCURACY = 8
    BURNOUT = 9
    SIEGE_MODE = 10
    ROLE_TYPE = 11
    COMP7 = 12
    FLAMETHROWER = 11
    ASSAULT_SPG = 11
    TANK_WITH_ABILITY = 11
    AUTOSHOOT_FLAMETHROWER = 11
    THERMAL_VISION = 11
    DISTANCE_DAMAGE_SHELL = 11
    AUTOSHOOT_GUN = 11
    DUAL_GUN_WITH_AUTORELOAD_CLIP = 12
    DUAL_GUN_WITH_CLIP = 12


def addPage(datailedList, headerTitle, title, descr, vKeys, buttons, image, roleImage=None, roleActions=None, hintCtx=None):
    data = {b'headerTitle': headerTitle, 
       b'title': title, 
       b'descr': descr, 
       b'vKeys': vKeys, 
       b'buttons': buttons, 
       b'image': image, 
       b'roleImage': roleImage, 
       b'roleActions': roleActions, 
       b'hintCtx': hintCtx}
    datailedList.append(data)
    return


def buildTitle(ctx):
    title = backport.text(R.strings.ingame_help.detailsHelp.default.title())
    return ctx.get(b'vehName') or title


def buildPagesData(ctx):
    detailedList = []
    builders = collectIngameHelpPagesBuilders()
    for builder in sorted(builders, key=(lambda item: item.priority()), reverse=True):
        if builder.hasPagesForCtx(ctx):
            detailedList.extend(builder.buildPages(ctx))

    selectedIdx = 0
    currentHintCtx = ctx.get(b'currentHintCtx')
    hintContexts = [pageData.pop(b'hintCtx') for pageData in detailedList]
    if currentHintCtx:
        selected = findFirst((lambda p: p == currentHintCtx), hintContexts)
        if selected is not None:
            selectedIdx = hintContexts.index(selected)
    return (
     detailedList, selectedIdx)


class DetailedHelpPagesBuilder(object):
    _SUITABLE_CTX_KEYS = ()

    @classmethod
    def hasPagesForCtx(cls, ctx):
        return all(ctx.get(key, False) for key in cls._SUITABLE_CTX_KEYS)

    @classmethod
    def priority(cls):
        return HelpPagePriority.DEFAULT

    @classmethod
    def buildPages(cls, ctx):
        return []

    @classmethod
    def collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        cls._collectHelpCtx(ctx, arenaVisitor, vehicle)
        return cls.hasPagesForCtx(ctx)

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        raise NotImplementedError
        return


class SiegeModePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isWheeledVehicle', b'hasSiegeMode')

    @classmethod
    def priority(cls):
        return HelpPagePriority.SIEGE_MODE

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        siegeKey = getVirtualKey(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION)
        siegeKeyName = getReadableKey(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION)
        keyName = siegeKeyName if siegeKeyName else backport.text(R.strings.ingame_help.detailsHelp.noKey())
        addPage(pages, buildTitle(ctx), backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.twoModes.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.twoModes(), key1=keyName)), [
         siegeKey], [
         siegeKeyName], backport.image(R.images.gui.maps.icons.battleHelp.wheeledHelp.wheel_two_mode()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'hasSiegeMode'] = vehicle is not None and vehicle.typeDescriptor.hasSiegeMode
        ctx[b'isWheeledVehicle'] = vehicle is not None and vehicle.typeDescriptor.isWheeledVehicle
        return


class BurnOutPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'hasBurnout',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.BURNOUT

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        breakeKeyName = getReadableKey(CommandMapping.CMD_BLOCK_TRACKS)
        forwardKeyName = getReadableKey(CommandMapping.CMD_MOVE_FORWARD)
        breakeKey = getVirtualKey(CommandMapping.CMD_BLOCK_TRACKS)
        forwardKey = getVirtualKey(CommandMapping.CMD_MOVE_FORWARD)
        keyName1 = breakeKeyName if breakeKeyName else backport.text(R.strings.ingame_help.detailsHelp.noKey())
        keyName2 = forwardKeyName if forwardKeyName else backport.text(R.strings.ingame_help.detailsHelp.noKey())
        addPage(pages, buildTitle(ctx), backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.burnout.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.burnout(), key1=keyName1, key2=keyName2)), [
         forwardKey, breakeKey], [
         forwardKeyName, breakeKeyName], backport.image(R.images.gui.maps.icons.battleHelp.wheeledHelp.wheel_burnout()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'hasBurnout'] = vehicle is not None and vehicle.typeDescriptor.hasBurnout
        return


class WheeledPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isFrenchWheeledVehicle',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.WHEELED

    @classmethod
    def buildPages(cls, ctx):
        headerTitle = buildTitle(ctx)
        pages = []
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.stableChassis.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.stableChassis())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.wheeledHelp.wheel_chassis()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.aboutTechnique.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.wheeledVeh.aboutTechnique())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.wheeledHelp.wheel_details()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        isRoleLtWheeled = vehicle is not None and vehicle.typeDescriptor.role == ROLE_TYPE.LT_WHEELED
        isFrenchWheeledVehicle = isRoleLtWheeled and NATIONS_NAMES[vehicle.typeDescriptor.type.id[0]] == b'france'
        ctx[b'isFrenchWheeledVehicle'] = isFrenchWheeledVehicle
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isFrenchWheeledVehicle
        return


class FlameTankPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isFlamethrower',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.FLAMETHROWER

    @classmethod
    def buildPages(cls, ctx):
        headerTitle = buildTitle(ctx)
        pages = []
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.flameTank.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.flameTank())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.flamethrowerHelp.flame_tank()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.flameTank.prosCons.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.flameTank.prosCons())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.flamethrowerHelp.flame_tank_pros_cons()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isFlamethrower'] = isFlamethrower = vehicle is not None and vehicle.typeDescriptor.isFlamethrower and vehicle.typeDescriptor.role == ROLE_TYPE.SPG_FLAME
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isFlamethrower
        return


class TankWithAbilityPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isTankWithAbility',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.TANK_WITH_ABILITY

    @classmethod
    def buildPages(cls, ctx):
        vehName = buildTitle(ctx)
        pages = []
        addPage(pages, backport.text(R.strings.ingame_help.detailsHelp.tankWithAbility.header(), vehName=vehName), backport.text(R.strings.ingame_help.detailsHelp.tankWithAbility.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.tankWithAbility.modifications())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.tankWithAbility.modifications()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        isTankWithAbility = vehicle.typeDescriptor.isTankWithAbility
        ctx[b'isTankWithAbility'] = isTankWithAbility
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isTankWithAbility
        return


class AutoshootFlameTankPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isAutoShootFlamethrower',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.AUTOSHOOT_FLAMETHROWER

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, backport.text(R.strings.ingame_help.detailsHelp.autoShootFlameTank.headerTitle()), backport.text(R.strings.ingame_help.detailsHelp.autoShootFlameTank.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.autoShootFlameTank.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.autoShootFlamethrowerHelp.autoshoot_flame_tank()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, backport.text(R.strings.ingame_help.detailsHelp.autoShootFlameTank.headerTitle()), backport.text(R.strings.ingame_help.detailsHelp.autoShootFlameTank.prosCons.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.autoShootFlameTank.prosCons())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.autoShootFlamethrowerHelp.autoshoot_flame_tank_pros_cons()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isAutoShootFlamethrower'] = isAutoShootFlamethrower = vehicle is not None and vehicle.typeDescriptor.isAutoShootFlamethrower
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isAutoShootFlamethrower
        return


class DistanceDamagePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isDistanceDamageShell',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.DISTANCE_DAMAGE_SHELL

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, backport.text(R.strings.ingame_help.detailsHelp.distanceDamage.headerTitle()), backport.text(R.strings.ingame_help.detailsHelp.distanceDamage.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.distanceDamage.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.unguidedMissile.distanceDamage()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        if vehicle is None:
            ctx[b'hasUniqueVehicleHelpScreen'] = False
            return
        else:
            shot = vehicle.typeDescriptor.shot
            ctx[b'isDistanceDamageShell'] = bool(shot.shell.distanceFactor)
            ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or ctx[b'isDistanceDamageShell']
            return


class AssaultTankPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isAssaultSPG',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.ASSAULT_SPG

    @classmethod
    def buildPages(cls, ctx):
        headerTitle = buildTitle(ctx)
        pages = []
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.assaultTank.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.assaultTank())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.assaultSPGHelp.assault_tank()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.assaultTank.prosCons.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.assaultTank.prosCons())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.assaultSPGHelp.assault_tank_pros_cons()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.assaultTank.aiming.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.assaultTank.aiming())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.assaultSPGHelp.assault_tank_aiming()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isAssaultSPG'] = isAssaultSPG = vehicle is not None and vehicle.typeDescriptor.isAssaultSPG
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isAssaultSPG
        return


class TrackWithinTrackPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isTrackWithinTrack',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.TRACK_WITHIN_TRACK

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, buildTitle(ctx), backport.text(R.strings.ingame_help.detailsHelp.trackWithinTrack.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.trackWithinTrack.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.trackWithinTrack.roll_away()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isTrackWithinTrack'] = isTrack = vehicle is not None and vehicle.typeDescriptor.isTrackWithinTrack
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isTrack
        return


class DualGunPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isDualGun',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.DUAL_GUN

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        headerTitle = buildTitle(ctx)
        shootKeyName = getReadableKey(CommandMapping.CMD_CM_SHOOT)
        shootKey = getVirtualKey(CommandMapping.CMD_CM_SHOOT)
        chargeKeyName = getReadableKey(CommandMapping.CMD_CM_CHARGE_SHOT)
        chargeKey = getVirtualKey(CommandMapping.CMD_CM_CHARGE_SHOT)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.dualGun.volley_fire.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.dualGun.volley_fire())), [
         chargeKey], [
         chargeKeyName], backport.image(R.images.gui.maps.icons.battleHelp.dualGunHelp.volley_fire()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.dualGun.quick_fire.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.dualGun.quick_fire())), [
         shootKey], [
         shootKeyName], backport.image(R.images.gui.maps.icons.battleHelp.dualGunHelp.quick_fire()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isDualGun'] = isDualGun = vehicle is not None and vehicle.typeDescriptor.isDualgunVehicle
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isDualGun
        return


class BattleRoyalePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isBattleRoyale', b'mapGeometryName')

    @classmethod
    def priority(cls):
        return HelpPagePriority.BATTLE_ROYALE

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        headerTitle = backport.text(R.strings.ingame_help.detailsHelp.default.title())
        mapGeometryName = ctx[b'mapGeometryName']
        isConeVisibility = ctx[b'isConeVisibility']
        mapResourceName = b'c_' + replaceHyphenToUnderscore(mapGeometryName)
        imagePath = R.images.gui.maps.icons.battleHelp.battleRoyale.dyn(mapResourceName)
        if not imagePath.isValid():
            raise SoftException((b'No icons found for map {}').format(mapGeometryName))
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.radar.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.radar.description())), [], [], backport.image(imagePath.br_radar()), hintCtx=HelpHintContext.BATTLE_ROYALE)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.zone.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.zone.description())), [], [], backport.image(imagePath.br_zone()), hintCtx=HelpHintContext.BATTLE_ROYALE)
        if isConeVisibility:
            addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.coneVisibility.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.coneVisibility.description())), [], [], backport.image(imagePath.br_sector()), hintCtx=HelpHintContext.BATTLE_ROYALE)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.airDrop.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.airDrop.description())), [], [], backport.image(imagePath.br_airdrop()), hintCtx=HelpHintContext.BATTLE_ROYALE)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.upgrade.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.upgrade.description())), [], [], backport.image(imagePath.br_tree()), hintCtx=HelpHintContext.BATTLE_ROYALE)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.uniqueAbilities.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.battleRoyale.uniqueAbilities.description())), [], [], backport.image(imagePath.br_unique_abilities()), hintCtx=HelpHintContext.BATTLE_ROYALE)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isBattleRoyale'] = isRoyale = arenaVisitor.getArenaBonusType() in ARENA_BONUS_TYPE.BATTLE_ROYALE_RANGE
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isRoyale
        ctx[b'mapGeometryName'] = arenaVisitor.type.getGeometryName()
        ctx[b'isConeVisibility'] = vehicle is not None and hasattr(vehicle, b'coneVisibility')
        return


class TurboshaftEnginePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'hasTurboshaftEngine',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.TURBOSHAFT_ENGINE

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        headerTitle = buildTitle(ctx)
        siegeKeyName = getReadableKey(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION)
        siegeKey = getVirtualKey(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.engineMode.engineModePage1.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.engineMode.engineModePage1())), [
         siegeKey], [
         siegeKeyName], backport.image(R.images.gui.maps.icons.battleHelp.turboshaftEngineHelp.engine_mode_page_1()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.engineMode.engineModePage2.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.engineMode.engineModePage2())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.turboshaftEngineHelp.engine_mode_page_2()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'hasTurboshaftEngine'] = hasTurboshaft = vehicle is not None and vehicle.typeDescriptor.hasTurboshaftEngine
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or hasTurboshaft
        return


class RocketAccelerationPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'hasRocketAcceleration',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.ROCKET_ACCELERATION

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        headerTitle = buildTitle(ctx)
        siegeKeyName = getReadableKey(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION)
        siegeKey = getVirtualKey(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.rocketAcceleration.page1.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.rocketAcceleration.page1())), [
         siegeKey], [
         siegeKeyName], backport.image(R.images.gui.maps.icons.battleHelp.rocketAcceleration.page_1()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.rocketAcceleration.page2.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.rocketAcceleration.page2())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.rocketAcceleration.page_2()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        hasRocketAcceleration = vehicle is not None and vehicle.typeDescriptor.hasRocketAcceleration
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or hasRocketAcceleration
        ctx[b'hasRocketAcceleration'] = hasRocketAcceleration
        return


class DualAccuracyPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'hasDualAccuracy',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.DUAL_ACCURACY

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, buildTitle(ctx), backport.text(R.strings.ingame_help.detailsHelp.dualAccuracy.mechanics.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.dualAccuracy.mechanics())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.dualAccuracy.mechanics()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        hasDualAccuracy = vehicle is not None and vehicle.typeDescriptor.hasDualAccuracy
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or hasDualAccuracy
        ctx[b'hasDualAccuracy'] = hasDualAccuracy
        return


class RoleTypePagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'roleType',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.ROLE_TYPE

    @classmethod
    def buildPages(cls, ctx):
        roleType = ctx.get(b'roleType')
        roleActions = []
        rolesToActions = getRolesActions()
        for action in rolesToActions[roleType]:
            actionLabel = ACTION_TYPE_TO_LABEL[action]
            roleActions.append({b'image': (backport.image(R.images.gui.maps.icons.roleExp.actions.c_128x128.dyn(actionLabel)())), 
               b'description': (backport.text(R.strings.menu.roleExp.action.dyn(actionLabel)()))})

        roleTypeLabel = ROLE_TYPE_TO_LABEL[roleType]
        pages = []
        addPage(pages, backport.text(R.strings.ingame_help.detailsHelp.role.title()), text_styles.superPromoTitle(backport.text(R.strings.menu.roleExp.roleName.dyn(roleTypeLabel)(), groupName=makeHtmlString(b'html_templates:vehicleRoles', b'roleTitle', {b'message': (backport.text(R.strings.menu.roleExp.roleGroupName.dyn(roleTypeLabel)()))}))), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.role.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.rolesHelp.dyn(roleTypeLabel)()), roleImage=backport.image(R.images.gui.maps.icons.roleExp.roles.c_100x100.dyn(roleTypeLabel)()), roleActions=roleActions, hintCtx=HelpHintContext.ROLE_HELP)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        isRanked = arenaVisitor.getArenaGuiType() == ARENA_GUI_TYPE.RANKED
        hasRoleType = isRanked and vehicle is not None and vehicle.typeDescriptor.role != ROLE_TYPE.NOT_DEFINED
        ctx[b'roleType'] = vehicle.typeDescriptor.role if hasRoleType else ROLE_TYPE.NOT_DEFINED
        return


class Comp7PagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isComp7',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.COMP7

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        comp7Header = backport.text(R.strings.comp7.detailsHelp.mainTitle())
        for pageName in getComp7DetailedHelpPages():
            addPage(datailedList=pages, headerTitle=comp7Header, title=backport.text(R.strings.comp7.detailsHelp.dyn(pageName).title()), descr=text_styles.mainBig(backport.text(R.strings.comp7.detailsHelp.dyn(pageName)())), vKeys=[], buttons=[], image=backport.image(R.images.comp7.gui.maps.icons.comp7.battleHelp.dyn(pageName)()))

        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isComp7'] = arenaVisitor.getArenaGuiType() in ARENA_GUI_TYPE.COMP7_RANGE
        return


class MapboxPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isMapbox',)
    _STR_PATH = R.strings.ingame_help.detailsHelp.mapbox

    @classmethod
    def priority(cls):
        return HelpPagePriority.MAPS

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        header = backport.text(cls._STR_PATH.headerTitle())
        hintCtx = HelpHintContext.MAPBOX
        addPage(pages, header, backport.text(cls._STR_PATH.markers.title()), text_styles.mainBig(backport.text(cls._STR_PATH.markers.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.mapbox.markers()), hintCtx=hintCtx)
        addPage(pages, header, backport.text(cls._STR_PATH.environment.title()), text_styles.mainBig(backport.text(cls._STR_PATH.environment.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.mapbox.environment()), hintCtx=hintCtx)
        addPage(pages, header, backport.text(cls._STR_PATH.artefacts.title()), text_styles.mainBig(backport.text(cls._STR_PATH.artefacts.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.mapbox.artefacts()), hintCtx=hintCtx)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isMapbox'] = arenaVisitor.getArenaGuiType() == ARENA_GUI_TYPE.MAPBOX
        return


class DevMapsPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isDevMaps',)
    _STR_PATH = R.strings.ingame_help.detailsHelp.devMaps

    @classmethod
    def priority(cls):
        return HelpPagePriority.MAPS

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        header = backport.text(cls._STR_PATH.headerTitle())
        hintCtx = HelpHintContext.DEV_MAPS
        addPage(pages, header, backport.text(cls._STR_PATH.title()), text_styles.mainBig(backport.text(cls._STR_PATH.markers.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.devMaps.markers()), hintCtx=hintCtx)
        addPage(pages, header, backport.text(cls._STR_PATH.title()), text_styles.mainBig(backport.text(cls._STR_PATH.zone.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.devMaps.zone()), hintCtx=hintCtx)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isDevMaps'] = arenaVisitor.extra.isMapsInDevelopmentEnabled()
        return


class MultiTrackPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isMultiTrack',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.MULTI_TRACK

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, backport.text(R.strings.ingame_help.detailsHelp.multiTrack.headerTitle()), backport.text(R.strings.ingame_help.detailsHelp.multiTrack.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.multiTrack.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.multiTrack.multitrack_tank()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isMultiTrack'] = isMultiTrack = vehicle is not None and vehicle.typeDescriptor.isMultiTrack
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isMultiTrack
        return


class ThermalVisionPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'hasThermalVision',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.THERMAL_VISION

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        headerTitle = buildTitle(ctx)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.thermalVision.page1.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.thermalVision.page1())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.thermalVisionHelp.page_1()), hintCtx=HelpHintContext.MECHANICS)
        addPage(pages, headerTitle, backport.text(R.strings.ingame_help.detailsHelp.thermalVision.page2.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.thermalVision.page2())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.thermalVisionHelp.page_2()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'hasThermalVision'] = hasThermalVision = vehicle is not None and vehicle.typeDescriptor.hasThermalVision
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or hasThermalVision
        return


class DualgunWithAutoreloadClip(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'hasDualgunWithAutoreloadClip',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.DUAL_GUN_WITH_AUTORELOAD_CLIP

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, buildTitle(ctx), backport.text(R.strings.ingame_help.detailsHelp.dualgunWithAutoreloadClip.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.dualgunWithAutoreloadClip.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.clipDualGunHelp.dualgun_with_autoreload_clip()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'hasDualgunWithAutoreloadClip'] = hasDualgunWithAutoreloadClip = vehicle is not None and vehicle.typeDescriptor.isDualgunVehicle and vehicle.typeDescriptor.isClipGun and vehicle.typeDescriptor.isAutoReloadGun
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or hasDualgunWithAutoreloadClip
        return


class DualgunWithClip(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'hasDualgunWithClip',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.DUAL_GUN_WITH_CLIP

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, buildTitle(ctx), backport.text(R.strings.ingame_help.detailsHelp.dualgunWithClip.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.dualgunWithClip.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.clipDualGunHelp.dualgun_with_clip()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'hasDualgunWithClip'] = hasDualgunWithClip = vehicle is not None and vehicle.typeDescriptor.isDualgunVehicle and vehicle.typeDescriptor.isClipGun and not vehicle.typeDescriptor.isAutoReloadGun
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or hasDualgunWithClip
        return


class AutoshootTankPagesBuilder(DetailedHelpPagesBuilder):
    _SUITABLE_CTX_KEYS = (b'isAutoShoot',)

    @classmethod
    def priority(cls):
        return HelpPagePriority.AUTOSHOOT_GUN

    @classmethod
    def buildPages(cls, ctx):
        pages = []
        addPage(pages, backport.text(R.strings.ingame_help.detailsHelp.autoShoot.headerTitle()), backport.text(R.strings.ingame_help.detailsHelp.autoShoot.title()), text_styles.mainBig(backport.text(R.strings.ingame_help.detailsHelp.autoShoot.description())), [], [], backport.image(R.images.gui.maps.icons.battleHelp.autoShootHelp.autoshoot_tank()), hintCtx=HelpHintContext.MECHANICS)
        return pages

    @classmethod
    def _collectHelpCtx(cls, ctx, arenaVisitor, vehicle):
        ctx[b'isAutoShoot'] = isAutoShoot = vehicle is not None and vehicle.typeDescriptor.isAutoShootGunVehicle and not vehicle.typeDescriptor.isAutoShootFlamethrower
        ctx[b'hasUniqueVehicleHelpScreen'] = ctx.get(b'hasUniqueVehicleHelpScreen') or isAutoShoot
        return


registerIngameHelpPagesBuilders((
 SiegeModePagesBuilder, BurnOutPagesBuilder, WheeledPagesBuilder, TrackWithinTrackPagesBuilder,
 DualGunPagesBuilder, BattleRoyalePagesBuilder, TurboshaftEnginePagesBuilder, RoleTypePagesBuilder,
 RocketAccelerationPagesBuilder, Comp7PagesBuilder, MapboxPagesBuilder,
 DualAccuracyPagesBuilder, DevMapsPagesBuilder, FlameTankPagesBuilder, AssaultTankPagesBuilder,
 MultiTrackPagesBuilder, TankWithAbilityPagesBuilder, AutoshootFlameTankPagesBuilder, ThermalVisionPagesBuilder,
 DualgunWithAutoreloadClip, DualgunWithClip, DistanceDamagePagesBuilder, AutoshootTankPagesBuilder))
