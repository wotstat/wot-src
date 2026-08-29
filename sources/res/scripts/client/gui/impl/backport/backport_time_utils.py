import time
from gui.impl.backport import text
from helpers import time_utils

def getTillTimeStringByRClass(timeValue, stringRClass, isRoundUp=False, removeLeadingZeros=True):
    gmtime = time.gmtime(timeValue)
    if isRoundUp and gmtime.tm_sec > 0:
        timeValue += time_utils.ONE_MINUTE
        gmtime = time.gmtime(timeValue)
    if timeValue >= time_utils.ONE_DAY:
        fmtKey = b'days'
        gmtime = time.gmtime(timeValue - time_utils.ONE_DAY)
    elif timeValue >= time_utils.ONE_HOUR:
        fmtKey = b'hours'
    elif timeValue >= time_utils.ONE_MINUTE:
        fmtKey = b'min'
    else:
        fmtKey = b'lessMin'
    tm = time.struct_time(gmtime)
    fmtValues = {b'day': (str(tm.tm_yday)), 
       b'hour': ((removeLeadingZeros or time.strftime)(b'%H', gmtime) if 1 else str(tm.tm_hour)), 
       b'min': ((removeLeadingZeros or time.strftime)(b'%M', gmtime) if 1 else str(tm.tm_min)), 
       b'sec': (time.strftime(b'%S', gmtime))}
    return text(stringRClass.dyn(fmtKey)(), **fmtValues)
