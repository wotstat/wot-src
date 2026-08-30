from __future__ import absolute_import
import typing
from past.builtins import basestring
from frameworks.wulf import WindowFlags, View, ViewSettings, PositionAnchor
from gui.impl.gen import R
from gui.impl.gen.view_models.windows.advanced_animated_tooltip_content_model import AdvancedAnimatedTooltipContentModel
from gui.impl.gen.view_models.windows.advanced_tooltip_content_model import AdvancedTooltipContentModel
from gui.impl.gen.view_models.windows.simple_tooltip_content_model import SimpleTooltipContentModel
from gui.impl.pub.window_impl import WindowImpl
from gui.impl.pub.window_view import WindowView
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.impl import IGuiLoader
if typing.TYPE_CHECKING:
    from typing import Optional
    from frameworks.wulf import ViewEvent, Window

class ToolTipWindow(WindowImpl):
    __slots__ = (b'_posX', b'_posY')

    def __init__(self, event, content, parent):
        if event is not None and event.decoratorID:
            decorator = WindowView(layoutID=event.decoratorID)
        else:
            decorator = None
        if event is not None:
            self._posX, self._posY = event.mouse.positionX, event.mouse.positionY
        else:
            self._posX, self._posY = (0, 0)
        super(ToolTipWindow, self).__init__(wndFlags=WindowFlags.TOOLTIP, decorator=decorator, content=content, parent=parent, areaID=R.areas.specific(), ownerViewID=event.targetViewID if event is not None else 0)
        return

    def move(self, x, y, xAnchor=PositionAnchor.LEFT, yAnchor=PositionAnchor.TOP):
        self._posX = x
        self._posY = y
        return super(ToolTipWindow, self).move(x, y, xAnchor, yAnchor)

    def _onReady(self):
        self.move(self._posX, self._posY)
        super(ToolTipWindow, self)._onReady()
        return


class SimpleToolTipWindow(ToolTipWindow):
    __slots__ = ()
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self, event, parent):
        header = self.makeString(event.getArgument(b'header', b''))
        body = self.makeString(event.getArgument(b'body', b''))
        note = self.makeString(event.getArgument(b'note', b''))
        alert = self.makeString(event.getArgument(b'alert', b''))
        super(SimpleToolTipWindow, self).__init__(event, SimpleTooltipContent(event.contentID, header, body, note, alert), parent)
        return

    @classmethod
    def makeString(cls, value):
        if not isinstance(value, basestring):
            value = cls.__gui.resourceManager.getTranslatedText(int(value))
        return value


class SimpleTooltipContent(View):
    __slots__ = ()

    def __init__(self, contentID, header=b'', body=b'', note=b'', alert=b''):
        settings = ViewSettings(contentID)
        settings.model = SimpleTooltipContentModel()
        settings.args = (header, body, note, alert)
        super(SimpleTooltipContent, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(SimpleTooltipContent, self).getViewModel()

    def _onLoading(self, header, body, note, alert):
        with self.viewModel.transaction() as tx:
            tx.setHeader(header)
            tx.setBody(body)
            tx.setNote(note)
            tx.setAlert(alert)
        return


class AdvancedToolTipWindow(ToolTipWindow):
    __slots__ = ()

    def __init__(self, event, parent, normalContent, advancedContent):
        super(AdvancedToolTipWindow, self).__init__(event, AdvancedTooltipContent(normalContent, advancedContent), parent)
        return


class AdvancedTooltipContent(View):
    __settingsCore = dependency.descriptor(ISettingsCore)
    __slots__ = ()

    def __init__(self, normalContent, advancedContent):
        settings = ViewSettings(R.views.common.tooltip_window.advanced_tooltip_content.AdvandcedTooltipContent())
        settings.model = AdvancedTooltipContentModel()
        settings.args = (normalContent, advancedContent)
        super(AdvancedTooltipContent, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(AdvancedTooltipContent, self).getViewModel()

    def _onLoading(self, normalContent, advancedContent):
        super(AdvancedTooltipContent, self)._initialize()
        disableAnim = self._getDisableAnimFlag()
        self.viewModel.setShowAnim(not disableAnim)
        self.setChildView(R.dynamic_ids.tooltip.normal_content(), normalContent)
        self.setChildView(R.dynamic_ids.tooltip.advanced_content(), advancedContent)
        if not disableAnim:
            self._setDisableAnimFlag()
        return

    def _getDisableAnimFlag(self):
        return self.__settingsCore.serverSettings.getDisableAnimTooltipFlag()

    def _setDisableAnimFlag(self):
        self.__settingsCore.serverSettings.setDisableAnimTooltipFlag()
        return


class AdvancedAnimatedTooltipContent(View):
    __slots__ = ()

    def __init__(self, header=b'', body=b'', animation=b''):
        settings = ViewSettings(R.views.common.tooltip_window.advanced_tooltip_content.AdvandcedAnimatedTooltipContent())
        settings.model = AdvancedAnimatedTooltipContentModel()
        settings.args = (header, body, animation)
        super(AdvancedAnimatedTooltipContent, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(AdvancedAnimatedTooltipContent, self).getViewModel()

    def _onLoading(self, header, body, animation):
        super(AdvancedAnimatedTooltipContent, self)._initialize()
        with self.viewModel.transaction() as tx:
            tx.setBody(body)
            tx.setHeader(header)
            tx.setAnimation(animation)
        return
