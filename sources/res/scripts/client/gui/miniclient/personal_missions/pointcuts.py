import aspects
from helpers import aop

class IsPersonalMissionsEnabled(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'helpers.server_settings', b'ServerSettings', b'isPersonalMissionsEnabled', aspects=(
         aspects.IsPersonalMissionsEnabled,))
        return
