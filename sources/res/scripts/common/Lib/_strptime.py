import time, locale, calendar
from re import compile as re_compile
from re import IGNORECASE
from re import escape as re_escape
from datetime import date as datetime_date
try:
    from thread import allocate_lock as _thread_allocate_lock
except:
    from dummy_thread import allocate_lock as _thread_allocate_lock

__all__ = []

def _getlang():
    return locale.getlocale(locale.LC_TIME)


class LocaleTime(object):

    def __init__(self):
        self.lang = _getlang()
        self.__calc_weekday()
        self.__calc_month()
        self.__calc_am_pm()
        self.__calc_timezone()
        self.__calc_date_time()
        if _getlang() != self.lang:
            raise ValueError(b'locale changed during initialization')
        if time.tzname != self.tzname or time.daylight != self.daylight:
            raise ValueError(b'timezone changed during initialization')
        return

    def __pad(self, seq, front):
        seq = list(seq)
        if front:
            seq.insert(0, b'')
        else:
            seq.append(b'')
        return seq

    def __calc_weekday(self):
        a_weekday = [calendar.day_abbr[i].lower() for i in range(7)]
        f_weekday = [calendar.day_name[i].lower() for i in range(7)]
        self.a_weekday = a_weekday
        self.f_weekday = f_weekday
        return

    def __calc_month(self):
        a_month = [calendar.month_abbr[i].lower() for i in range(13)]
        f_month = [calendar.month_name[i].lower() for i in range(13)]
        self.a_month = a_month
        self.f_month = f_month
        return

    def __calc_am_pm(self):
        am_pm = []
        for hour in (1, 22):
            time_tuple = time.struct_time((1999, 3, 17, hour, 44, 55, 2, 76, 0))
            am_pm.append(time.strftime(b'%p', time_tuple).lower())

        self.am_pm = am_pm
        return

    def __calc_date_time(self):
        time_tuple = time.struct_time((1999, 3, 17, 22, 44, 55, 2, 76, 0))
        date_time = [None, None, None]
        date_time[0] = time.strftime(b'%c', time_tuple).lower()
        date_time[1] = time.strftime(b'%x', time_tuple).lower()
        date_time[2] = time.strftime(b'%X', time_tuple).lower()
        replacement_pairs = [(b'%', b'%%'), (self.f_weekday[2], b'%A'),
         (
          self.f_month[3], b'%B'), (self.a_weekday[2], b'%a'),
         (
          self.a_month[3], b'%b'), (self.am_pm[1], b'%p'),
         (b'1999', b'%Y'), (b'99', b'%y'), (b'22', b'%H'),
         (b'44', b'%M'), (b'55', b'%S'), (b'76', b'%j'),
         (b'17', b'%d'), (b'03', b'%m'), (b'3', b'%m'),
         (b'2', b'%w'), (b'10', b'%I')]
        replacement_pairs.extend([(tz, b'%Z') for tz_values in self.timezone for tz in tz_values])
        for offset, directive in ((0, b'%c'), (1, b'%x'), (2, b'%X')):
            current_format = date_time[offset]
            for old, new in replacement_pairs:
                if old:
                    current_format = current_format.replace(old, new)

            time_tuple = time.struct_time((1999, 1, 3, 1, 1, 1, 6, 3, 0))
            if b'00' in time.strftime(directive, time_tuple):
                U_W = b'%W'
            else:
                U_W = b'%U'
            date_time[offset] = current_format.replace(b'11', U_W)

        self.LC_date_time = date_time[0]
        self.LC_date = date_time[1]
        self.LC_time = date_time[2]
        return

    def __calc_timezone(self):
        try:
            time.tzset()
        except AttributeError:
            pass

        self.tzname = time.tzname
        self.daylight = time.daylight
        no_saving = frozenset([b'utc', b'gmt', self.tzname[0].lower()])
        if self.daylight:
            has_saving = frozenset([self.tzname[1].lower()])
        else:
            has_saving = frozenset()
        self.timezone = (
         no_saving, has_saving)
        return


class TimeRE(dict):

    def __init__(self, locale_time=None):
        if locale_time:
            self.locale_time = locale_time
        else:
            self.locale_time = LocaleTime()
        base = super(TimeRE, self)
        base.__init__({b'd': b'(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])', 
           b'f': b'(?P<f>[0-9]{1,6})', 
           b'H': b'(?P<H>2[0-3]|[0-1]\\d|\\d)', 
           b'I': b'(?P<I>1[0-2]|0[1-9]|[1-9])', 
           b'j': b'(?P<j>36[0-6]|3[0-5]\\d|[1-2]\\d\\d|0[1-9]\\d|00[1-9]|[1-9]\\d|0[1-9]|[1-9])', 
           b'm': b'(?P<m>1[0-2]|0[1-9]|[1-9])', 
           b'M': b'(?P<M>[0-5]\\d|\\d)', 
           b'S': b'(?P<S>6[0-1]|[0-5]\\d|\\d)', 
           b'U': b'(?P<U>5[0-3]|[0-4]\\d|\\d)', 
           b'w': b'(?P<w>[0-6])', 
           b'y': b'(?P<y>\\d\\d)', 
           b'Y': b'(?P<Y>\\d\\d\\d\\d)', 
           b'A': (self.__seqToRE(self.locale_time.f_weekday, b'A')), 
           b'a': (self.__seqToRE(self.locale_time.a_weekday, b'a')), 
           b'B': (self.__seqToRE(self.locale_time.f_month[1:], b'B')), 
           b'b': (self.__seqToRE(self.locale_time.a_month[1:], b'b')), 
           b'p': (self.__seqToRE(self.locale_time.am_pm, b'p')), 
           b'Z': (self.__seqToRE((tz for tz_names in self.locale_time.timezone for tz in tz_names), b'Z')), 
           b'%': b'%'})
        base.__setitem__(b'W', base.__getitem__(b'U').replace(b'U', b'W'))
        base.__setitem__(b'c', self.pattern(self.locale_time.LC_date_time))
        base.__setitem__(b'x', self.pattern(self.locale_time.LC_date))
        base.__setitem__(b'X', self.pattern(self.locale_time.LC_time))
        return

    def __seqToRE(self, to_convert, directive):
        to_convert = sorted(to_convert, key=len, reverse=True)
        for value in to_convert:
            if value != b'':
                break
        else:
            return b''

        regex = (b'|').join(re_escape(stuff) for stuff in to_convert)
        regex = b'(?P<%s>%s' % (directive, regex)
        return b'%s)' % regex

    def pattern(self, format):
        processed_format = b''
        regex_chars = re_compile(b'([\\\\.^$*+?\\(\\){}\\[\\]|])')
        format = regex_chars.sub(b'\\\\\\1', format)
        whitespace_replacement = re_compile(b'\\s+')
        format = whitespace_replacement.sub(b'\\\\s+', format)
        while b'%' in format:
            directive_index = format.index(b'%') + 1
            processed_format = b'%s%s%s' % (processed_format,
             format[:directive_index - 1],
             self[format[directive_index]])
            format = format[directive_index + 1:]

        return b'%s%s' % (processed_format, format)

    def compile(self, format):
        return re_compile(self.pattern(format), IGNORECASE)


_cache_lock = _thread_allocate_lock()
_TimeRE_cache = TimeRE()
_CACHE_MAX_SIZE = 5
_regex_cache = {}

def _calc_julian_from_U_or_W(year, week_of_year, day_of_week, week_starts_Mon):
    first_weekday = datetime_date(year, 1, 1).weekday()
    if not week_starts_Mon:
        first_weekday = (first_weekday + 1) % 7
        day_of_week = (day_of_week + 1) % 7
    week_0_length = (7 - first_weekday) % 7
    if week_of_year == 0:
        return 1 + day_of_week - first_weekday
    else:
        days_to_week = week_0_length + 7 * (week_of_year - 1)
        return 1 + days_to_week + day_of_week

    return


def _strptime(data_string, format=b'%a %b %d %H:%M:%S %Y'):
    global _TimeRE_cache
    global _regex_cache
    with _cache_lock:
        locale_time = _TimeRE_cache.locale_time
        if _getlang() != locale_time.lang or time.tzname != locale_time.tzname or time.daylight != locale_time.daylight:
            _TimeRE_cache = TimeRE()
            _regex_cache.clear()
            locale_time = _TimeRE_cache.locale_time
        if len(_regex_cache) > _CACHE_MAX_SIZE:
            _regex_cache.clear()
        format_regex = _regex_cache.get(format)
        if not format_regex:
            try:
                format_regex = _TimeRE_cache.compile(format)
            except KeyError as err:
                bad_directive = err.args[0]
                if bad_directive == b'\\':
                    bad_directive = b'%'
                del err
                raise ValueError(b"'%s' is a bad directive in format '%s'" % (
                 bad_directive, format))
            except IndexError:
                raise ValueError(b"stray %% in format '%s'" % format)

            _regex_cache[format] = format_regex
    found = format_regex.match(data_string)
    if not found:
        raise ValueError(b'time data %r does not match format %r' % (
         data_string, format))
    if len(data_string) != found.end():
        raise ValueError(b'unconverted data remains: %s' % data_string[found.end():])
    year = None
    month = day = 1
    hour = minute = second = fraction = 0
    tz = -1
    week_of_year = -1
    week_of_year_start = -1
    weekday = julian = None
    found_dict = found.groupdict()
    for group_key in found_dict.iterkeys():
        if group_key == b'y':
            year = int(found_dict[b'y'])
            if year <= 68:
                year += 2000
            else:
                year += 1900
        elif group_key == b'Y':
            year = int(found_dict[b'Y'])
        elif group_key == b'm':
            month = int(found_dict[b'm'])
        elif group_key == b'B':
            month = locale_time.f_month.index(found_dict[b'B'].lower())
        elif group_key == b'b':
            month = locale_time.a_month.index(found_dict[b'b'].lower())
        elif group_key == b'd':
            day = int(found_dict[b'd'])
        elif group_key == b'H':
            hour = int(found_dict[b'H'])
        elif group_key == b'I':
            hour = int(found_dict[b'I'])
            ampm = found_dict.get(b'p', b'').lower()
            if ampm in (b'', locale_time.am_pm[0]):
                if hour == 12:
                    hour = 0
            elif ampm == locale_time.am_pm[1]:
                if hour != 12:
                    hour += 12
        elif group_key == b'M':
            minute = int(found_dict[b'M'])
        elif group_key == b'S':
            second = int(found_dict[b'S'])
        elif group_key == b'f':
            s = found_dict[b'f']
            s += b'0' * (6 - len(s))
            fraction = int(s)
        elif group_key == b'A':
            weekday = locale_time.f_weekday.index(found_dict[b'A'].lower())
        elif group_key == b'a':
            weekday = locale_time.a_weekday.index(found_dict[b'a'].lower())
        elif group_key == b'w':
            weekday = int(found_dict[b'w'])
            if weekday == 0:
                weekday = 6
            else:
                weekday -= 1
        elif group_key == b'j':
            julian = int(found_dict[b'j'])
        elif group_key in (b'U', b'W'):
            week_of_year = int(found_dict[group_key])
            if group_key == b'U':
                week_of_year_start = 6
            else:
                week_of_year_start = 0
        elif group_key == b'Z':
            found_zone = found_dict[b'Z'].lower()
            for value, tz_values in enumerate(locale_time.timezone):
                if found_zone in tz_values:
                    if time.tzname[0] == time.tzname[1] and time.daylight and found_zone not in (b'utc', b'gmt'):
                        break
                    else:
                        tz = value
                        break

    leap_year_fix = False
    if year is None and month == 2 and day == 29:
        year = 1904
        leap_year_fix = True
    elif year is None:
        year = 1900
    if julian is None and week_of_year != -1 and weekday is not None:
        week_starts_Mon = True if week_of_year_start == 0 else False
        julian = _calc_julian_from_U_or_W(year, week_of_year, weekday, week_starts_Mon)
        if julian <= 0:
            year -= 1
            yday = 366 if calendar.isleap(year) else 365
            julian += yday
    if julian is None:
        julian = datetime_date(year, month, day).toordinal() - datetime_date(year, 1, 1).toordinal() + 1
    else:
        datetime_result = datetime_date.fromordinal(julian - 1 + datetime_date(year, 1, 1).toordinal())
        year = datetime_result.year
        month = datetime_result.month
        day = datetime_result.day
    if weekday is None:
        weekday = datetime_date(year, month, day).weekday()
    if leap_year_fix:
        year = 1900
    return (
     time.struct_time((year, month, day,
      hour, minute, second,
      weekday, julian, tz)), fraction)


def _strptime_time(data_string, format=b'%a %b %d %H:%M:%S %Y'):
    return _strptime(data_string, format)[0]
