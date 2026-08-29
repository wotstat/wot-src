from typing import Optional, Union, TYPE_CHECKING
from gui.game_loading.resources.consts import InfoStyles
if TYPE_CHECKING:
    from gui.game_loading.resources.consts import ImageVfxs

class BaseResourceModel(object):
    __slots__ = (b'minShowTimeSec',)

    def __init__(self, minShowTimeSec):
        self.minShowTimeSec = max(minShowTimeSec, 0)
        return


class LocalImageModel(BaseResourceModel):
    __slots__ = (b'imageRelativePath', b'vfx', b'localizationText', b'descriptionText', b'transition', b'additionalImage', b'sound')

    def __init__(self, imageRelativePath, vfx=None, localizationText=None, descriptionText=None, minShowTimeSec=0, transition=0):
        super(LocalImageModel, self).__init__(minShowTimeSec=minShowTimeSec)
        self.imageRelativePath = imageRelativePath
        self.vfx = vfx
        self.localizationText = localizationText
        self.descriptionText = descriptionText
        self.transition = transition
        self.additionalImage = None
        self.sound = None
        return

    def __repr__(self):
        string = b'<{}(image={}, vfx={}, localizationExist={}, descriptionExist={}, minShowTimeSec={}, transition={})>'
        return string.format(self.__class__.__name__, self.imageRelativePath, self.vfx, bool(self.localizationText), bool(self.descriptionText), self.minShowTimeSec, self.transition)


class LogoModel(BaseResourceModel):
    __slots__ = (b'type', b'showCopyright', b'showVersion', b'transition', b'info', b'infoStyle')

    def __init__(self, logoType, minShowTimeSec=0, showCopyright=True, showVersion=True, transition=0, info=b'', infoStyle=InfoStyles.DEFAULT):
        super(LogoModel, self).__init__(minShowTimeSec=minShowTimeSec)
        self.type = logoType
        self.showCopyright = showCopyright
        self.showVersion = showVersion
        self.transition = transition
        self.info = info
        self.infoStyle = infoStyle
        return

    def __repr__(self):
        return (b'<LogoModel(type={}, minShowTimeSec={}, copyright={}, version={}, transition={}, info={}, infoStyle={})>').format(self.type, self.minShowTimeSec, self.showCopyright, self.showVersion, self.transition, self.info, self.infoStyle)


class StatusTextModel(BaseResourceModel):
    __slots__ = (b'text',)

    def __init__(self, text, minShowTimeSec=0):
        super(StatusTextModel, self).__init__(minShowTimeSec=minShowTimeSec)
        self.text = text
        return

    def __repr__(self):
        return (b'<StatusTextModel(text={}, minShowTimeSec={})>').format(self.text, self.minShowTimeSec)
