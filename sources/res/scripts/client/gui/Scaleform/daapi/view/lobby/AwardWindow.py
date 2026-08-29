from gui.Scaleform.daapi.view.meta.MissionAwardWindowMeta import MissionAwardWindowMeta
from gui.Scaleform.daapi.view.meta.AwardWindowMeta import AwardWindowMeta
from gui.server_events.pm_constants import PERSONAL_MISSIONS_SILENT_SOUND_SPACE

class AwardWindow(AwardWindowMeta):

    def onOKClick(self):
        self._award.handleOkButton()
        self.onWindowClose()
        return

    def onCloseClick(self):
        self._award.handleCloseButton()
        self.onWindowClose()
        return

    def onTakeNextClick(self):
        self._award.handleBodyButton()
        self.onWindowClose()
        return

    def _getTypeSpecificFields(self):
        okBtn, closeBtn, bodyBtn = self._award.getButtonStates()
        result = {b'useBackAnimation': (self._award.useBackgroundAnimation()), 
           b'backAnimationData': (self._award.getBackgroundAnimationData()), 
           b'awardImage': (self._award.getAwardImage()), 
           b'additionalText': (self._award.getAdditionalText()), 
           b'isDashLineEnabled': (self._award.getHasDashedLine()), 
           b'buttonText': (self._award.getOkButtonText()), 
           b'closeBtnLabel': (self._award.getCloseButtonText()), 
           b'takeNextBtnLabel': (self._award.getBodyButtonText()), 
           b'textAreaIconPath': (self._award.getTextAreaIconPath()), 
           b'textAreaIconIsShow': (self._award.getTextAreaIconIsShow()), 
           b'isOKBtnEnabled': okBtn, 
           b'isCloseBtnEnabled': closeBtn, 
           b'isTakeNextBtnEnabled': bodyBtn, 
           b'bodyBtnLinkage': (self._award.getBodyButtonLinkage())}
        result.update(self._award.getExtraFields())
        ribbonInfo = self._award.getRibbonInfo()
        if ribbonInfo is not None:
            result.update({b'awardsBlock': (ribbonInfo._asdict())})
        return result


class MissionAwardWindow(MissionAwardWindowMeta):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_SILENT_SOUND_SPACE

    def onCurrentQuestClick(self):
        if self._award.handleNextButton():
            self.onWindowClose()
        return

    def onNextQuestClick(self):
        self._award.handleCurrentButton()
        self.onWindowClose()
        return

    def _getTypeSpecificFields(self):
        return {b'ribbonImage': (self._award.getRibbonImage()), 
           b'currentQuestHeader': (self._award.getCurrentQuestHeader()), 
           b'currentQuestConditions': (self._award.getCurrentQuestConditions()), 
           b'nextQuestHeader': (self._award.getNextQuestHeader()), 
           b'nextQuestConditionsHeader': (self._award.getNextQuestConditionsHeader()), 
           b'nextQuestConditions': (self._award.getNextQuestConditions()), 
           b'additionalStatusText': (self._award.getAdditionalStatusText()), 
           b'mainStatusText': (self._award.getMainStatusText()), 
           b'availableText': (self._award.getAvailableText()), 
           b'additionalStatusIcon': (self._award.getAdditionalStatusIcon()), 
           b'mainStatusIcon': (self._award.getMainStatusIcon()), 
           b'nextButtonText': (self._award.getNextButtonText()), 
           b'nextButtonTooltip': (self._award.getNextButtonTooltip()), 
           b'awards': (self._award.getAwards()), 
           b'conditions': None, 
           b'isPersonalQuest': (self._award.isPersonal()), 
           b'availableNextQuest': (self._award.isNextAvailable()), 
           b'isLastQuest': (self._award.isLast())}
