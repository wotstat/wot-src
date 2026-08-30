from __future__ import absolute_import
import typing
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.tooltips.simple_icon_tooltip_model import HeaderType
from gui.impl.lobby.common.tooltips.simple_icon_tooltip_view import SimpleIconTooltipView
from gui.impl.pub.tooltip_window import SimpleTooltipContent
if typing.TYPE_CHECKING:
    from frameworks.wulf import View, ViewEvent

def createSimpleTooltip(parent, event, header=b'', body=b''):
    window = DecoratedTooltipWindow(parent=parent, content=SimpleTooltipContent(R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent(), body=body, header=header))
    window.load()
    window.move(event.mouse.positionX, event.mouse.positionY)
    return window


def createSimpleIconTooltip(event):
    return SimpleIconTooltipView(event.getArgument(b'header', b''), event.getArgument(b'body', b''), event.getArgument(b'icon', b''), event.getArgument(b'headerType', HeaderType.NORMAL))
