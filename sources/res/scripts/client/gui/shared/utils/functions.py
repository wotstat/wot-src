from __future__ import absolute_import
import random, re, typing
from builtins import map, range
import ArenaType, wg_async as future_async
from adisp import adisp_async
from gui import GUI_SETTINGS, SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets
from gui.shared.money import Currency
from helpers.i18n import makeString
from ids_generators import SequenceIDGenerator
from items import ITEM_TYPE_INDICES, vehicles as vehs_core
from items.components.shell_components import ShellType, HollowChargeType, HighExplosiveType
from post_progression_common import TankSetupGroupsId
if typing.TYPE_CHECKING:
    from typing import Tuple
    from gui.impl.gen_utils import DynAccessor

def rnd_choice(*args):
    args = list(args)
    for _ in range(len(args)):
        c = random.choice(args)
        yield c
        args.remove(c)

    return


def rnd_choice_loop(*args):
    args = list(args)
    while True:
        for value in rnd_choice(*args):
            yield value

    return


def clamp(value, minRange, maxRange):
    if value < minRange:
        return minRange
    if value > maxRange:
        return maxRange
    return value


def roundToMinOrZero(value, minValue):
    if value == 0:
        return value
    return max(minValue, value)


def getShortDescr(descr):
    res = re.findall(b'<shortDesc>(.*?)</shortDesc>', descr)
    if res:
        res_str = res[0]
    else:
        res_str = descr
    return res_str


def stripShortDescrTags(descr):
    return re.sub(b'<shortDesc>|</shortDesc>', b'', descr)


def stripColorTagDescrTags(descr):
    return re.sub(b'{colorTagOpen}|{colorTagClose}', b'', descr)


def stripExpAmountTags(descr):
    return re.sub(b'{expTagOpen}|{expTagClose}', b'', descr)


def stripShortDescr(descr):
    return re.sub(b'<shortDesc>(.*?)</shortDesc>', b'', descr)


def stripAllTags(descr):
    return re.sub(b'{\\w+Open}|{\\w+Close}', b'', descr)


def stripHTMLTags(descr):
    return re.sub(b'<(.*?)>', b'', descr)


def makeTooltip(header=None, body=None, note=None, attention=None):
    res_str = b''
    if header is not None:
        res_str += b'{HEADER}%s{/HEADER}' % makeString(header)
    if body is not None:
        res_str += b'{BODY}%s{/BODY}' % makeString(body)
    if note is not None:
        res_str += b'{NOTE}%s{/NOTE}' % makeString(note)
    if attention is not None:
        res_str += b'{ATTENTION}%s{/ATTENTION}' % makeString(attention)
    return res_str


@adisp_async
@future_async.wg_async
def checkAmmoLevel(vehicles, callback):
    showAmmoWarning = False
    ammoWarningMessage = b'lowAmmoAutoLoad'
    alternativeAmmoWarningMessage = b'lowAlternativeAmmoAutoLoad'
    for vehicle in vehicles:
        if vehicle.isAmmoCanSwitch:
            isNotFull, _ = vehicle.isAmmoNotFullInSetups
            isPrebattleSwitchDisabled = vehicle.postProgression.isPrebattleSwitchDisabled(TankSetupGroupsId.EQUIPMENT_AND_SHELLS)
            isNotFull = isNotFull and (not isPrebattleSwitchDisabled or not vehicle.isAmmoFullInSetups(vehicle.shells.setupLayouts.layoutIndex))
        else:
            isNotFull = not vehicle.isAmmoFull
        showAmmoWarning = showAmmoWarning or isNotFull
        if showAmmoWarning:
            from gui.impl.dialogs import dialogs
            from gui.impl.dialogs.builders import ResSimpleDialogBuilder
            builder = ResSimpleDialogBuilder()
            msg = alternativeAmmoWarningMessage if vehicle.isAmmoFull else ammoWarningMessage
            builder.setMessagesAndButtons(R.strings.dialogs.dyn(msg), R.strings.dialogs.dyn(ammoWarningMessage))
            builder.setIcon(R.images.gui.maps.icons.tanksetup.warning.ammunition())
            builder.setPreset(DialogPresets.TROPHY_DEVICE_UPGRADE)
            success = yield future_async.wg_await(dialogs.showSimple(builder.buildInLobby()))
            callback(success)
        else:
            callback(True)

    return


def getModuleGoldStatus(price, money):
    currency = Currency.GOLD
    availableForCredits = 1
    availableForGold = 2
    couldBeBought = 0
    if price.credits and price.credits > money.credits:
        currency = Currency.CREDITS
    else:
        couldBeBought |= availableForCredits
    if price.gold and price.gold < money.gold:
        couldBeBought |= availableForGold
    if not couldBeBought:
        return (False, b'#menu:moduleFits/%s_error' % currency, b'#tooltips:moduleFits/%s_error' % currency)
    return (True, b'', b'')


def findConflictedEquipments(itemCompactDescr, itemTypeID, vehicle):
    conflictEqs = []
    if itemTypeID != ITEM_TYPE_INDICES[b'vehicleEngine']:
        return conflictEqs
    oldModule, = vehicle.descriptor.installComponent(itemCompactDescr)
    for equipmentDescr in vehicle.equipments:
        if equipmentDescr:
            equipment = vehs_core.getItemByCompactDescr(equipmentDescr)
            installPossible, _ = equipment.checkCompatibilityWithVehicle(vehicle.descriptor)
            if not installPossible:
                conflictEqs.append(equipment)

    vehicle.descriptor.installComponent(oldModule)
    return conflictEqs


def findConflictedEquipmentForModule(module, vehicle):
    return findConflictedEquipments(module.compactDescr, ITEM_TYPE_INDICES[module.itemTypeName], vehicle)


def getArenaSubTypeID(arenaTypeID):
    return arenaTypeID >> 16


def getArenaSubTypeName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].gameplayName


def getArenaGeometryName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].geometryName


def getArenaShortName(arenaTypeID):
    return ArenaType.g_cache[arenaTypeID].name


def getArenaFullName(arenaTypeID):
    arenaType = ArenaType.g_cache[arenaTypeID]
    arenaName = arenaType.name
    if arenaType.gameplayName != b'ctf':
        arenaName = b'%s - %s' % (arenaName,
         backport.text(R.strings.arenas.type.dyn(arenaType.gameplayName).dyn(b'name')()))
    return arenaName


def getArenaImage(geometryName, subdir=b''):
    dynAccessor = R.images.gui.maps.icons.map
    if subdir:
        dynAccessor = dynAccessor.dyn(subdir)
    imgDynAccessor = dynAccessor.num(geometryName)
    if imgDynAccessor.isValid():
        return backport.image(imgDynAccessor())
    return b''


def getBattleSubTypeWinText(arenaTypeID, teamID):
    root = R.strings.arenas.type.dyn(ArenaType.g_cache[arenaTypeID].gameplayName)
    description = root.dyn(b'description')
    if not description:
        description = root.dyn((b'description{}').format(teamID))
    return backport.text(description())


def getBattleSubTypeBaseNumber(arenaTypeID, team, baseID):
    teamBasePositions = ArenaType.g_cache[arenaTypeID].teamBasePositions
    if len(teamBasePositions) >= team:
        points = teamBasePositions[team - 1]
        if len(points) > 1:
            return b' %d' % (sorted(points.keys()).index(baseID) + 1)
    points = ArenaType.g_cache[arenaTypeID].controlPoints
    if points:
        if len(points) > 1:
            return b' %d' % baseID
    return b''


def isBaseExists(arenaTypeID, team):
    teamBasePositions = ArenaType.g_cache[arenaTypeID].teamBasePositions
    if len(teamBasePositions) >= team:
        points = teamBasePositions[team - 1]
        if points:
            return True
    return False


def isControlPointExists(arenaTypeID):
    controlPoint = ArenaType.g_cache[arenaTypeID].controlPoints
    if controlPoint:
        return True
    return False


def getAbsoluteUrl(url):
    return url.replace(b'../', b'img://gui/')


def getRelativeUrl(url):
    return url.replace(b'img://gui', b'..')


_viewIdsGen = None

def getViewName(viewAlias, *args):
    l = list(args)
    if viewAlias:
        l.insert(0, viewAlias)
    return (b'_').join(map(str, l))


def getUniqueViewName(viewAlias):
    global _viewIdsGen
    if _viewIdsGen is None:
        _viewIdsGen = SequenceIDGenerator()
    return getViewName(viewAlias, _viewIdsGen.nextSequenceID)


def getPostBattleUniqueSubUrl(svrPackedData, clientPackedData):
    return b'%s/%s/%s ' % (
     GUI_SETTINGS.postBattleExchange.url, svrPackedData, clientPackedData)


def parsePostBattleUniqueSubUrl(uniqueSubUrl):
    return uniqueSubUrl.split(b'/')[1:]


def showSentInviteMessage(user=None):
    if user is not None:
        if user is not None:
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.PREBATTLE_INVITES_SENDINVITE_NAME, type=SystemMessages.SM_TYPE.Information, name=user.getFullName())
        else:
            SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.PREBATTLE_INVITES_SENDINVITE, type=SystemMessages.SM_TYPE.Information)
    return


def replaceHyphenToUnderscore(text):
    return text.replace(b'-', b'_')


def getVehTypeIconName(vType, isElite=False):
    vType = replaceHyphenToUnderscore(vType)
    if isElite:
        return (b'{}_elite').format(vType)
    return vType


def getImageResourceFromPath(path):
    path = path.replace(b'../', b'gui/')
    path = path.rsplit(b'.', 1)[0]
    resource = R.images
    for pathItem in path.split(b'/'):
        resource = resource.dyn(pathItem)

    return resource


def capitalizeText(text):
    t = text.decode()
    return t[0].upper() + t[1:]


def getShellImpactParams(shellType):
    shieldPenetration = False
    shellTypeMaxDamage = 0
    if isinstance(shellType, HollowChargeType):
        ricochetAngleCos = shellType.ricochetAngleCos
        normalizationAngle = 0.0
    elif isinstance(shellType, HighExplosiveType):
        ricochetAngleCos = 0.0
        normalizationAngle = 0.0
        if shellType.shieldPenetration is not None:
            shieldPenetration = shellType.shieldPenetration
        if shellType.maxDamage is not None:
            shellTypeMaxDamage = shellType.maxDamage
    else:
        ricochetAngleCos = shellType.ricochetAngleCos
        normalizationAngle = shellType.normalizationAngle
    return (ricochetAngleCos, normalizationAngle, shieldPenetration, shellTypeMaxDamage)


def deepMergeDicts(destination, source):
    for key in source:
        if key in destination and isinstance(destination[key], dict) and isinstance(source[key], dict):
            if not source[key]:
                destination[key] = {}
            else:
                deepMergeDicts(destination[key], source[key])
        else:
            destination[key] = source[key]

    return
