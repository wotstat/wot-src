from soft_exception import SoftException
from items.components.ny_constants import YEARS_INFO

class NYSoftException(SoftException):

    def __init__(self, msg, *args):
        super(NYSoftException, self).__init__()
        self.msg = msg
        self.args = args
        return

    def __str__(self):
        return (b'NY{}: {} {}').format(YEARS_INFO.CURRENT_YEAR, self.msg, self.args)
