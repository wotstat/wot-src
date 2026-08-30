import logging, typing
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles import ranked_formatters
from gui.ranked_battles.ranked_helpers import getShieldSizeByRankSize, makeStatTooltip
from gui.shared.formatters import text_styles, icons
if typing.TYPE_CHECKING:
    from gui.ranked_battles.ranked_models import Division, Rank
_logger = logging.getLogger(__name__)
__ANIMATION_DATA_FIELDS = [b'top', b'bottom', b'left', b'right']

def buildRankVO(rank, isEnabled=False, hasTooltip=False, shieldStatus=None, shieldAnimated=False, showUnburnable=False, imageSize=RANKEDBATTLES_ALIASES.WIDGET_MEDIUM):
    shieldVO = None
    if shieldStatus:
        shieldVO = _getShieldVO(imageSize, shieldStatus, shieldAnimated)
    elif rank.isVisualUnburnable():
        shieldVO = _getUnburnableVO(imageSize)
    return {b'imageSrc': (rank.getIcon(imageSize)), b'smallImageSrc': (rank.getIcon(RANKEDBATTLES_ALIASES.WIDGET_SMALL)), 
       b'isEnabled': isEnabled, 
       b'rankID': (str(rank.getID())), 
       b'hasTooltip': hasTooltip, 
       b'shield': shieldVO}


def buildRankTooltipVO(rank, imageSize):
    shieldImage = plateImage = None
    shieldStatus = rank.getShieldStatus()
    if shieldStatus is not None:
        _, shieldHP, _, _, _ = shieldStatus
        if shieldHP > 0:
            shieldImage = backport.image(R.images.gui.maps.icons.rankedBattles.ranks.shields.dyn(imageSize)())
            plateImage = backport.image(R.images.gui.maps.icons.rankedBattles.ranks.shields.plate.dyn(imageSize).num(shieldHP)())
    return {b'rankImage': (rank.getIcon(imageSize)), 
       b'shieldImage': (shieldImage or _getUnburnableIcon(rank, imageSize)), 
       b'plateImage': plateImage, 
       b'isEnabled': True}


def getDivisionVO(division):
    return {b'id': (division.getUserID()), 
       b'name': (division.getUserName()), 
       b'isCompleted': (division.isCompleted()), 
       b'isLocked': (not division.isUnlocked()), 
       b'isCurrent': (division.isCurrent()), 
       b'isQualification': (division.isQualification())}


def getEfficiencyVO(currentSeasonEfficiency, currentSeasonEfficiencyDiff):
    delta = b''
    if currentSeasonEfficiencyDiff is not None:
        if currentSeasonEfficiencyDiff > 0:
            delta = text_styles.concatStylesToSingleLine(icons.makeImageTag(backport.image(R.images.gui.maps.icons.rankedBattles.league.delta_plus()), 11, 16, -3), text_styles.bonusAppliedText(ranked_formatters.getFloatPercentStrStat(currentSeasonEfficiencyDiff)))
        if currentSeasonEfficiencyDiff < 0:
            delta = text_styles.concatStylesToSingleLine(icons.makeImageTag(backport.image(R.images.gui.maps.icons.rankedBattles.league.delta_minus()), 11, 16, -3), text_styles.error(ranked_formatters.getFloatPercentStrStat(currentSeasonEfficiencyDiff)))
    return {b'icon': b'efficiency', 
       b'label': b'', 
       b'value': (ranked_formatters.getFloatPercentStrStat(currentSeasonEfficiency)), 
       b'delta': delta}


def getRatingVO(rating):
    return {b'icon': b'position', 
       b'label': b'', 
       b'value': (ranked_formatters.getIntegerStrStat(rating))}


def getStatVO(value, statKey, iconKey, tooltipKey):
    return {b'icon': iconKey, 
       b'label': (text_styles.alignText(text_styles.main(backport.text(R.strings.ranked_battles.rankedBattleMainView.stats.dyn(statKey)())), b'center')), 
       b'value': value, 
       b'tooltip': (makeStatTooltip(tooltipKey))}


def _getShieldVO(imageSize, shieldStatus, shieldAnimated):
    shield = None
    prevShieldHP, shieldHP, _, shieldState, newShieldState = shieldStatus
    if shieldState != newShieldState or shieldHP > 0:
        shieldSize = getShieldSizeByRankSize(imageSize)
        shortcut = R.images.gui.maps.icons.rankedBattles.ranks.shields
        shield = {b'state': shieldState, 
           b'newState': newShieldState, 
           b'size': shieldSize, 
           b'img': (backport.image(shortcut.dyn(attr=(b'{}').format(shieldSize))())), 
           b'plateImg': (backport.image(shortcut.plate.empty.dyn(attr=(b'{}').format(shieldSize))())), 
           b'prevLabel': (str(prevShieldHP)), 
           b'label': (str(shieldHP))}
        if shieldAnimated:
            shield[b'animationData'] = {b'topImg': (backport.image(shortcut.dyn(attr=(b'{}_{}').format(shieldSize, RANKEDBATTLES_ALIASES.SHIELD_PART_TOP))())), 
               b'bottomImg': (backport.image(shortcut.dyn(attr=(b'{}_{}').format(shieldSize, RANKEDBATTLES_ALIASES.SHIELD_PART_BOTTOM))())), 
               b'rightImg': (backport.image(shortcut.dyn(attr=(b'{}_{}').format(shieldSize, RANKEDBATTLES_ALIASES.SHIELD_PART_RIGHT))())), 
               b'leftImg': (backport.image(shortcut.dyn(attr=(b'{}_{}').format(shieldSize, RANKEDBATTLES_ALIASES.SHIELD_PART_LEFT))()))}
    return shield


def _getUnburnableVO(imageSize):
    shieldSize = getShieldSizeByRankSize(imageSize)
    shortcut = R.images.gui.maps.icons.rankedBattles.ranks.unburnable
    return {b'state': (RANKEDBATTLES_ALIASES.SHIELD_ENABLED), 
       b'newState': (RANKEDBATTLES_ALIASES.SHIELD_ENABLED), 
       b'size': shieldSize, 
       b'img': (backport.image(shortcut.dyn(attr=(b'{}').format(shieldSize))()))}


def _getUnburnableIcon(rank, imageSize):
    if rank.isVisualUnburnable():
        return backport.image(R.images.gui.maps.icons.rankedBattles.ranks.unburnable.dyn(imageSize)())
    return b''
