from gui.Scaleform.locale.MINICLIENT import MINICLIENT
from gui.shared.utils.functions import makeTooltip
from helpers import aop

class MakeClanBtnUnavailable(aop.Aspect):

    def __init__(self, config=None):
        self.__config = config or {}
        aop.Aspect.__init__(self)
        return

    def atReturn(self, cd):
        original_return_value = cd.returned
        original_return_value[b'btnEnabled'] = False
        original_return_value[b'btnTooltip'] = makeTooltip(None, None, None, self.__config.get(b'sandbox_platform_message', MINICLIENT.ACCOUNTPOPOVER_WARNING))
        return original_return_value


class MakeClubProfileButtonUnavailable(aop.Aspect):

    def atCall(self, cd):
        cd.change()
        return (
         [
          False], {})
