import aspects
from helpers import aop

class ShowBGWallpaper(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.login.login_modes.view_background', b'ViewBackground', b'show$', aspects=(
         aspects.ShowBGWallpaper,))
        return
