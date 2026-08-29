import typing
from frameworks.wulf import WindowLayer
from gui.impl.dialogs.dialog_template import DialogTemplateView, DEFAULT_DIMMER_ALPHA
from gui.impl.dialogs.sub_views.common.simple_text import ImageSubstitution
from gui.impl.dialogs.sub_views.content.text_warning_content import TextWithWarning
from gui.impl.dialogs.dialog_template_button import ButtonPresenter, CancelButton, ConfirmButton
from gui.impl.dialogs.dialog_template_utils import toString
from gui.impl.dialogs.sub_views.content.simple_text_content import SimpleTextContent
from gui.impl.dialogs.sub_views.icon.icon_set import IconSet
from gui.impl.dialogs.sub_views.title.simple_text_title import SimpleTextTitle
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_set_view_model import IconPositionLogicEnum
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType
from gui.impl.gen_utils import DynAccessor
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogWindowWrapper
from gui.impl.pub.dialog_window import DialogButtons
if typing.TYPE_CHECKING:
    from typing import Optional, List, Union
    String = Union[str, unicode]

class BuilderDialogTemplateView(DialogTemplateView):
    __slots__ = ()

    def _closeClickHandler(self, args=None):
        reason = (args or {}).get(b'reason')
        self._setResult(reason or DialogButtons.CANCEL)
        return


class BaseDialogBuilder(object):
    __slots__ = (b'__title', b'__description', b'__icon', b'__buttons', b'__uniqueID', b'__backgroundID', b'__dimmerAlpha', b'__layoutID', b'__selectedButtonID', b'__doBlur', b'__layer', b'__displayFlags')

    def __init__(self, uniqueID=None, layoutID=None):
        super(BaseDialogBuilder, self).__init__()
        self.__title = None
        self.__description = None
        self.__icon = None
        self.__buttons = []
        self.__uniqueID = uniqueID
        self.__backgroundID = None
        self.__dimmerAlpha = DEFAULT_DIMMER_ALPHA
        self.__layoutID = layoutID
        self.__selectedButtonID = None
        self.__doBlur = True
        self.__layer = WindowLayer.UNDEFINED
        self.__displayFlags = []
        return

    def buildView(self):
        template = BuilderDialogTemplateView(layoutID=self.__layoutID, uniqueID=self.__uniqueID)
        if self.__title:
            template.setSubView(DefaultDialogPlaceHolders.TITLE, SimpleTextTitle(self.__title))
        if self.__description:
            template.setSubView(DefaultDialogPlaceHolders.CONTENT, SimpleTextContent(self.__description))
        if self.__icon:
            template.setSubView(DefaultDialogPlaceHolders.ICON, IconSet(**self.__icon))
        if self.__buttons:
            focusedButtonIndex = -1
            for index, buttonData in enumerate(self.__buttons):
                template.addButton(buttonData)
                if buttonData.buttonID == self.__selectedButtonID:
                    focusedButtonIndex = index

            template.setFocusedIndex(focusedButtonIndex)
        if self.__backgroundID:
            template.setBackgroundImagePath(self.__backgroundID)
        template.setBackgroundDimmerAlpha(self.__dimmerAlpha)
        if self.__displayFlags:
            template.setDisplayFlags(*self.__displayFlags)
        self._extendTemplate(template)
        return template

    def build(self):
        return FullScreenDialogWindowWrapper(self.buildView(), doBlur=self.__doBlur, layer=self.__layer)

    def setTitle(self, text):
        self.__title = toString(text)
        return

    def setDescription(self, text):
        self.__description = toString(text)
        return

    def setIcon(self, mainIcon, backgrounds=None, overlays=None, layoutID=None, iconPositionLogic=IconPositionLogicEnum.CENTREDANDTHROUGHCONTENT.value):
        self.__icon = {b'iconResID': mainIcon, 
           b'backgroundResIDList': backgrounds, 
           b'overlayResIDList': overlays, 
           b'layoutID': layoutID, 
           b'iconPositionLogic': iconPositionLogic}
        return

    def addButton(self, buttonSettings):
        self.__buttons.append(buttonSettings)
        return

    def getButton(self, buttonID):
        return next(data for data in self.__buttons if data.buttonID == buttonID)

    def setBackground(self, resourceID):
        self.__backgroundID = resourceID
        return

    def setDimmerAlpha(self, value):
        self.__dimmerAlpha = value
        return

    def setLayoutID(self, layoutID):
        self.__layoutID = layoutID
        return

    def setFocusedButtonID(self, buttonID):
        self.__selectedButtonID = buttonID
        return

    def setBlur(self, value=True):
        self.__doBlur = value
        return

    def setLayer(self, layerID):
        self.__layer = layerID
        return

    def setDisplayFlags(self, *displayFlags):
        self.__displayFlags = displayFlags
        return

    def _extendTemplate(self, template):
        return


class ResDialogBuilder(BaseDialogBuilder):
    __slots__ = (b'__showBalance',)

    def __init__(self, uniqueID=None):
        super(ResDialogBuilder, self).__init__(uniqueID)
        self.__showBalance = False
        return

    def setShowBalance(self, value):
        self.__showBalance = value
        return

    def setMessagesAndButtons(self, message, buttons=R.strings.dialogs.common, focusedButtonID=DialogButtons.SUBMIT):
        self.setDescription(message.dyn(b'message')())
        self.setTitle(message.dyn(b'title')())
        for _id in DialogButtons.ALL:
            button = message.dyn(_id) or buttons.dyn(_id)
            if button.exists():
                self.addButton(ButtonPresenter(button(), _id, ButtonType.PRIMARY if _id == focusedButtonID else ButtonType.SECONDARY))

        self.setFocusedButtonID(focusedButtonID)
        return

    def _extendTemplate(self, template):
        super(ResDialogBuilder, self)._extendTemplate(template)
        if self.__showBalance:
            template.setSubView(DefaultDialogPlaceHolders.TOP_RIGHT, MoneyBalance())
        return


class ConfirmCancelDialogBuilder(BaseDialogBuilder):
    __slots__ = ()

    def __init__(self, uniqueID=None, layoutID=None):
        super(ConfirmCancelDialogBuilder, self).__init__(uniqueID, layoutID)
        self.addButton(ConfirmButton())
        self.setFocusedButtonID(DialogButtons.SUBMIT)
        self.addButton(CancelButton())
        return

    def setConfirmButtonLabel(self, text):
        self.getButton(DialogButtons.SUBMIT).label = text
        return

    def setCancelButtonLabel(self, text):
        self.getButton(DialogButtons.CANCEL).label = text
        return


class ConfirmCancelWarningDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__ = (b'__descriptionMsg', b'__warningMsg')

    def __init__(self, uniqueID=None):
        super(ConfirmCancelWarningDialogBuilder, self).__init__(uniqueID)
        self.__descriptionMsg = None
        self.__warningMsg = None
        return

    def setDescription(self, text):
        return

    def setDescriptionMsg(self, text):
        self.__descriptionMsg = toString(text)
        return

    def setWarningMsg(self, text):
        self.__warningMsg = toString(text)
        return

    def _extendTemplate(self, template):
        super(ConfirmCancelWarningDialogBuilder, self)._extendTemplate(template)
        if self.__descriptionMsg and self.__warningMsg:
            template.setSubView(DefaultDialogPlaceHolders.CONTENT, TextWithWarning(self.__descriptionMsg, self.__warningMsg))
        return


class ConfirmCancelDescriptionDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__ = (b'__descriptionMsg',)

    def __init__(self, uniqueID=None):
        super(ConfirmCancelDescriptionDialogBuilder, self).__init__(uniqueID)
        self.__descriptionMsg = None
        return

    def setDescriptionMsg(self, text):
        self.__descriptionMsg = toString(text)
        return

    def _extendTemplate(self, template):
        if self.__descriptionMsg:
            template.setSubView(DefaultDialogPlaceHolders.CONTENT, TextWithWarning(self.__descriptionMsg, b''))
        return


class AlertBuilder(BaseDialogBuilder):
    __slots__ = ()

    def __init__(self, uniqueID=None):
        super(AlertBuilder, self).__init__(uniqueID)
        self.addButton(ButtonPresenter(R.strings.dialogs.dialogTemplates.ok(), DialogButtons.CANCEL))
        self.setFocusedButtonID(DialogButtons.CANCEL)
        return

    def setButtonLabel(self, text):
        self.getButton(DialogButtons.CANCEL).label = text
        return


class InfoDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__ = ()

    def __init__(self, uniqueID=None):
        super(InfoDialogBuilder, self).__init__(uniqueID)
        rDialogs = R.images.gui.maps.uiKit.dialogs
        self.setIcon(rDialogs.icons.info(), [rDialogs.highlights.blue()])
        return


class AcceleratedCrewTrainingDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__ = ()

    def __init__(self, uniqueID=None):
        super(AcceleratedCrewTrainingDialogBuilder, self).__init__(uniqueID)
        self.setIcon(R.images.gui.maps.uiKit.dialogs.icons.accelerated_crew())
        return


class PassiveXPDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__ = (b'__descriptionMsg', b'__icon')

    def __init__(self, uniqueID=None):
        super(PassiveXPDialogBuilder, self).__init__(uniqueID)
        self.setIcon(R.images.gui.maps.uiKit.dialogs.icons.intensive_crew())
        self.__descriptionMsg = None
        self.__icon = None
        return

    def setDescriptionMsg(self, text):
        self.__descriptionMsg = text
        return

    def setMessageIcon(self, icon):
        self.__icon = icon
        return

    def _extendTemplate(self, template):
        super(PassiveXPDialogBuilder, self)._extendTemplate(template)
        if self.__descriptionMsg and self.__icon:
            image = ImageSubstitution(self.__icon(), b'typeIcon', 3, -5, -5, -5)
            template.setSubView(DefaultDialogPlaceHolders.CONTENT, SimpleTextContent(self.__descriptionMsg, imageSubstitutions=[image]))
        return


class WarningDialogBuilder(ConfirmCancelDialogBuilder):
    __slots__ = (b'__warningMsg',)

    def __init__(self, uniqueID=None):
        super(WarningDialogBuilder, self).__init__(uniqueID)
        rDialogs = R.images.gui.maps.uiKit.dialogs
        self.setIcon(rDialogs.icons.alert(), [rDialogs.highlights.yellow_1()])
        self.__warningMsg = None
        return

    def setWarningMsg(self, text):
        self.__warningMsg = toString(text)
        return

    def _extendTemplate(self, template):
        super(WarningDialogBuilder, self)._extendTemplate(template)
        if self.__warningMsg:
            template.setSubView(DefaultDialogPlaceHolders.CONTENT, TextWithWarning(b'', self.__warningMsg))
        return


class ErrorAlertBuilder(AlertBuilder):
    __slots__ = ()

    def __init__(self, uniqueID=None):
        super(ErrorAlertBuilder, self).__init__(uniqueID)
        rDialogs = R.images.gui.maps.uiKit.dialogs
        self.setIcon(rDialogs.icons.error(), [rDialogs.highlights.red_1()])
        return
