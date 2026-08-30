from enum import Enum
from frameworks.wulf import ViewModel

class DateTimeFormatsEnum(Enum):
    DAYMONTHNUMERIC = b'dayMonthNumeric'
    DAYMONTHFULL = b'dayMonthFull'
    DAYMONTHFULLTIME = b'dayMonthFullTime'
    DAYMONTHABBREVIATED = b'dayMonthAbbreviated'
    DAYMONTHABBREVIATEDTIME = b'dayMonthAbbreviatedTime'
    SHORTDATE = b'shortDate'
    SHORTTIME = b'ShortTime'
    SHORTDATETIME = b'ShortDateTime'
    FULLDATE = b'fullDate'
    FULLTIME = b'fullTime'
    FULLDATETIME = b'fullDateTime'


class DateTimeFormats(ViewModel):
    __slots__ = ()

    def __init__(self, properties=0, commands=0):
        super(DateTimeFormats, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(DateTimeFormats, self)._initialize()
        return
