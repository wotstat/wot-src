from gui.Scaleform.daapi.view.meta.SecondaryEntryPointMeta import SecondaryEntryPointMeta
from gui.impl.gen import R
from gui.impl import backport
from gui.shared.utils.functions import makeComplexTooltipByResource
from helpers import dependency
from shared_utils import first
from skeletons.gui.game_control import IBattlePassController
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.lobby.battle_pass.battle_pass_entry_point_view import BaseBattlePassEntryPointView
from gui.battle_pass.battle_pass_helpers import getIsBpPointsShopEntryPointActive
_R_TOOLTIPS = R.views.lobby.battle_pass.tooltips
_R_IMAGES = R.images.gui.maps.icons.library.hangarEntryPoints.battlePass
_TOOLTIPS = {(_R_TOOLTIPS.BattlePassNotStartedTooltipView()): (TOOLTIPS_CONSTANTS.BATTLE_PASS_NOT_STARTED), 
   (_R_TOOLTIPS.BattlePassCompletedTooltipView()): (TOOLTIPS_CONSTANTS.BATTLE_PASS_COMPLETED), 
   (_R_TOOLTIPS.BattlePassInProgressTooltipView()): (TOOLTIPS_CONSTANTS.BATTLE_PASS_IN_PROGRESS), 
   (_R_TOOLTIPS.BattlePassNoChapterTooltipView()): (TOOLTIPS_CONSTANTS.BATTLE_PASS_NO_CHAPTER)}

class BattlePassSecondaryEntryPointWidget(SecondaryEntryPointMeta, BaseBattlePassEntryPointView):
    __battlePass = dependency.descriptor(IBattlePassController)
    __slots__ = (b'__arenaBonusType',)

    def __init__(self):
        super(BattlePassSecondaryEntryPointWidget, self).__init__()
        self.__arenaBonusType = None
        return

    def onClick(self):
        self._onClick()
        return

    def update(self, currentArenaBonusType):
        self.__arenaBonusType = currentArenaBonusType
        self._updateData()
        return

    def _populate(self):
        super(BattlePassSecondaryEntryPointWidget, self)._populate()
        super(BattlePassSecondaryEntryPointWidget, self)._subscribe()
        self._start()
        return

    def _dispose(self):
        self._stop()
        super(BattlePassSecondaryEntryPointWidget, self)._unsubscribe()
        super(BattlePassSecondaryEntryPointWidget, self)._dispose()
        return

    def _updateData(self, *_):
        super(BattlePassSecondaryEntryPointWidget, self)._updateData()
        if self.__arenaBonusType is None:
            return
        else:
            flagIcon = backport.image(_R_IMAGES.dyn((b'flag_chapter_{}').format(self.chapterID), default=_R_IMAGES.flag_default)()) if self.chapterID > 0 else None
            gameModeIsEnabled = self.__battlePass.isGameModeEnabled(self.__arenaBonusType)
            isEnabled = gameModeIsEnabled and self.__battlePass.isActive() and self.__battlePass.isEnabled()
            isPointsVisible = self.isCompleted and getIsBpPointsShopEntryPointActive()
            data = {b'flagIcon': flagIcon, 
               b'icon': (self.__getIcon()), 
               b'altIcon': (self.__getAltIcon(isEnabled)), 
               b'extraIcon': (self.__getExtraIcon()), 
               b'text': (str(self.level + 1)), 
               b'isEnabled': isEnabled, 
               b'isBought': (self.isBought), 
               b'isPaused': (self.isPaused), 
               b'chapterID': (self.chapterID), 
               b'points': (self.freePoints if isPointsVisible else 0)}
            self.__updateTooltipData(data, self.__arenaBonusType, gameModeIsEnabled)
            self.as_setDataS(data)
            if not self.__battlePass.isDisabled():
                self.as_setCountS(self._getNotChosenRewardCount())
            return

    def _getCurrentArenaBonusType(self):
        return self.__arenaBonusType

    def __getChapterID(self):
        availableChapter = first(self.__battlePass.getChapterIDs())
        if self.__battlePass.isSingleChapter():
            return availableChapter
        return self.chapterID

    def __getIcon(self):
        isCompleted = self.isCompleted
        isBought = self.isBought
        isMarathonChapter = self.__battlePass.isMarathonChapter(self.chapterID)
        chapterID = self.__getChapterID()
        shieldTemplate = b'shield{}{}{}'
        customShieldTemplate = b'c_{}_shield{}{}{}'
        plateColor = b'_normal'
        borderColor = b'_gold' if isBought else b'_silver'
        postfix = b'' if self.__battlePass.hasActiveChapter() or isCompleted and self.freePoints > 0 else b'_closed'
        if isMarathonChapter:
            plateColor = b'_marathon'
        elif isBought or isCompleted:
            plateColor = b'_blue'
        customIcon = _R_IMAGES.dyn(customShieldTemplate.format(chapterID, plateColor, borderColor, postfix), default=_R_IMAGES.dyn(shieldTemplate.format(plateColor, borderColor, postfix)))()
        return backport.image(customIcon)

    def __getAltIcon(self, isEnabled):
        progressionType = b'gold' if self.isBought else b'silver'
        customIcon = None
        if self.chapterID > 0:
            iconTemplate = b'icon_{}_chapter_{}'
            icon = _R_IMAGES.dyn(iconTemplate.format(progressionType, self.chapterID), default=_R_IMAGES.icon_default)()
        elif self.isCompleted:
            chapterID = self.__getChapterID()
            customIconTemplate = b'c_{}_icon_completed_{}'
            iconTemplate = b'icon_completed_{}'
            icon = _R_IMAGES.dyn(iconTemplate.format(progressionType))()
            customIcon = _R_IMAGES.dyn(customIconTemplate.format(chapterID, progressionType), default=_R_IMAGES.dyn(iconTemplate.format(progressionType)))()
        else:
            icon = _R_IMAGES.icon_chapter_empty()
        if customIcon:
            return backport.image(customIcon)
        else:
            return backport.image(icon)

    def __getExtraIcon(self):
        if self.hasMarathon:
            return backport.image(_R_IMAGES.extra_flags_mini())
        else:
            if self.isResourceAvailable:
                return backport.image(_R_IMAGES.resource_decor())
            return

    def __updateTooltipData(self, data, currentArenaBonusType, gameModeIsEnabled):
        if gameModeIsEnabled and self.__battlePass.isEnabled():
            tooltip = _TOOLTIPS.get(self._getTooltip(), b'')
            tooltipType = TOOLTIPS_CONSTANTS.WULF
        elif not self.__battlePass.isEnabled():
            tooltip = makeComplexTooltipByResource(R.strings.battle_pass.tooltips.entryPoint.disabled)
            tooltipType = TOOLTIPS_CONSTANTS.COMPLEX
        else:
            tooltip = backport.text(R.strings.battle_pass.tooltips.secondaryEntryPoint.disabled.num(currentArenaBonusType)())
            if tooltip:
                tooltipType = TOOLTIPS_CONSTANTS.SIMPLE
            else:
                tooltip = makeComplexTooltipByResource(R.strings.battle_pass.tooltips.entryPoint.disabled)
                tooltipType = TOOLTIPS_CONSTANTS.COMPLEX
        data[b'tooltip'] = tooltip
        data[b'tooltipType'] = tooltipType
        return
