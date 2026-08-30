import sys, encodings, encodings.aliases, re, operator, functools
_str = str
try:
    _unicode = unicode
except NameError:

    class _unicode(object):
        pass


__all__ = [
 4, 5, 6, 7, 
 8, 9, 10, 11, 12, 
 13, 14, 15, 16, 17, 18, 
 19, 
 20, 21, 22, 23, 
 24, 25, 26]
try:
    from _locale import *
except ImportError:
    CHAR_MAX = 127
    LC_ALL = 6
    LC_COLLATE = 3
    LC_CTYPE = 0
    LC_MESSAGES = 5
    LC_MONETARY = 4
    LC_NUMERIC = 1
    LC_TIME = 2
    Error = ValueError

    def localeconv():
        return {b'grouping': [127], b'currency_symbol': b'', 
           b'n_sign_posn': 127, 
           b'p_cs_precedes': 127, 
           b'n_cs_precedes': 127, 
           b'mon_grouping': [], b'n_sep_by_space': 127, 
           b'decimal_point': b'.', 
           b'negative_sign': b'', 
           b'positive_sign': b'', 
           b'p_sep_by_space': 127, 
           b'int_curr_symbol': b'', 
           b'p_sign_posn': 127, 
           b'thousands_sep': b'', 
           b'mon_thousands_sep': b'', 
           b'frac_digits': 127, 
           b'mon_decimal_point': b'', 
           b'int_frac_digits': 127}


    def setlocale(category, value=None):
        if value not in (None, b'', b'C'):
            raise Error, b'_locale emulation only supports "C" locale'
        return b'C'


    def strcoll(a, b):
        return cmp(a, b)


    def strxfrm(s):
        return s


_localeconv = localeconv
_override_localeconv = {}

@functools.wraps(_localeconv)
def localeconv():
    d = _localeconv()
    if _override_localeconv:
        d.update(_override_localeconv)
    return d


def _grouping_intervals(grouping):
    last_interval = None
    for interval in grouping:
        if interval == CHAR_MAX:
            return
        if interval == 0:
            if last_interval is None:
                raise ValueError(b'invalid grouping')
            while True:
                yield last_interval

        yield interval
        last_interval = interval

    return


def _group(s, monetary=False):
    conv = localeconv()
    thousands_sep = conv[monetary and b'mon_thousands_sep' or b'thousands_sep']
    grouping = conv[monetary and b'mon_grouping' or b'grouping']
    if not grouping:
        return (s, 0)
    if s[-1] == b' ':
        stripped = s.rstrip()
        right_spaces = s[len(stripped):]
        s = stripped
    else:
        right_spaces = b''
    left_spaces = b''
    groups = []
    for interval in _grouping_intervals(grouping):
        if not s or s[-1] not in b'0123456789':
            left_spaces = s
            s = b''
            break
        groups.append(s[-interval:])
        s = s[:-interval]

    if s:
        groups.append(s)
    groups.reverse()
    return (
     left_spaces + thousands_sep.join(groups) + right_spaces,
     len(thousands_sep) * (len(groups) - 1))


def _strip_padding(s, amount):
    lpos = 0
    while amount and s[lpos] == b' ':
        lpos += 1
        amount -= 1

    rpos = len(s) - 1
    while amount and s[rpos] == b' ':
        rpos -= 1
        amount -= 1

    return s[lpos:rpos + 1]


_percent_re = re.compile(b'%(?:\\((?P<key>.*?)\\))?(?P<modifiers>[-#0-9 +*.hlL]*?)[eEfFgGdiouxXcrs%]')

def format(percent, value, grouping=False, monetary=False, *additional):
    match = _percent_re.match(percent)
    if not match or len(match.group()) != len(percent):
        raise ValueError(b'format() must be given exactly one %%char format specifier, %s not valid' % repr(percent))
    return _format(percent, value, grouping, monetary, *additional)


def _format(percent, value, grouping=False, monetary=False, *additional):
    if additional:
        formatted = percent % ((value,) + additional)
    else:
        formatted = percent % value
    if percent[-1] in b'eEfFgG':
        seps = 0
        parts = formatted.split(b'.')
        if grouping:
            parts[0], seps = _group(parts[0], monetary=monetary)
        decimal_point = localeconv()[monetary and b'mon_decimal_point' or b'decimal_point']
        formatted = decimal_point.join(parts)
        if seps:
            formatted = _strip_padding(formatted, seps)
    elif percent[-1] in b'diu':
        seps = 0
        if grouping:
            formatted, seps = _group(formatted, monetary=monetary)
        if seps:
            formatted = _strip_padding(formatted, seps)
    return formatted


def format_string(f, val, grouping=False):
    percents = list(_percent_re.finditer(f))
    new_f = _percent_re.sub(b'%s', f)
    if operator.isMappingType(val):
        new_val = []
        for perc in percents:
            if perc.group()[-1] == b'%':
                new_val.append(b'%')
            else:
                new_val.append(format(perc.group(), val, grouping))

    elif not isinstance(val, tuple):
        val = (
         val,)
    new_val = []
    i = 0
    for perc in percents:
        if perc.group()[-1] == b'%':
            new_val.append(b'%')
        else:
            starcount = perc.group(b'modifiers').count(b'*')
            new_val.append(_format(perc.group(), val[i], grouping, False, *val[i + 1:i + 1 + starcount]))
            i += 1 + starcount

    val = tuple(new_val)
    return new_f % val


def currency(val, symbol=True, grouping=False, international=False):
    conv = localeconv()
    digits = conv[international and b'int_frac_digits' or b'frac_digits']
    if digits == 127:
        raise ValueError(b"Currency formatting is not possible using the 'C' locale.")
    s = format(b'%%.%if' % digits, abs(val), grouping, monetary=True)
    s = b'<' + s + b'>'
    if symbol:
        smb = conv[international and b'int_curr_symbol' or b'currency_symbol']
        precedes = conv[val < 0 and b'n_cs_precedes' or b'p_cs_precedes']
        separated = conv[val < 0 and b'n_sep_by_space' or b'p_sep_by_space']
        if precedes:
            s = smb + (separated and b' ' or b'') + s
        else:
            s = s + (separated and b' ' or b'') + smb
    sign_pos = conv[val < 0 and b'n_sign_posn' or b'p_sign_posn']
    sign = conv[val < 0 and b'negative_sign' or b'positive_sign']
    if sign_pos == 0:
        s = b'(' + s + b')'
    elif sign_pos == 1:
        s = sign + s
    elif sign_pos == 2:
        s = s + sign
    elif sign_pos == 3:
        s = s.replace(b'<', sign)
    elif sign_pos == 4:
        s = s.replace(b'>', sign)
    else:
        s = sign + s
    return s.replace(b'<', b'').replace(b'>', b'')


def str(val):
    return format(b'%.12g', val)


def atof(string, func=float):
    ts = localeconv()[b'thousands_sep']
    if ts:
        string = string.replace(ts, b'')
    dd = localeconv()[b'decimal_point']
    if dd:
        string = string.replace(dd, b'.')
    return func(string)


def atoi(str):
    return atof(str, int)


def _test():
    setlocale(LC_ALL, b'')
    s1 = format(b'%d', 123456789, 1)
    print s1, b'is', atoi(s1)
    s1 = str(3.14)
    print s1, b'is', atof(s1)
    return


_setlocale = setlocale
_ascii_lower_map = (b'').join(chr(x + 32 if x >= ord(b'A') and x <= ord(b'Z') else x) for x in range(256))

def _replace_encoding(code, encoding):
    if b'.' in code:
        langname = code[:code.index(b'.')]
    else:
        langname = code
    norm_encoding = encodings.normalize_encoding(encoding)
    norm_encoding = encodings.aliases.aliases.get(norm_encoding, norm_encoding)
    encoding = locale_encoding_alias.get(norm_encoding, norm_encoding)
    return langname + b'.' + encoding


def normalize(localename):
    if isinstance(localename, _unicode):
        localename = localename.encode(b'ascii')
    code = localename.translate(_ascii_lower_map)
    if b':' in code:
        code = code.replace(b':', b'.')
    if b'@' in code:
        code, modifier = code.split(b'@', 1)
    else:
        modifier = b''
    if b'.' in code:
        langname, encoding = code.split(b'.')[:2]
    else:
        langname = code
        encoding = b''
    lang_enc = langname
    if encoding:
        norm_encoding = encoding.replace(b'-', b'')
        norm_encoding = norm_encoding.replace(b'_', b'')
        lang_enc += b'.' + norm_encoding
    lookup_name = lang_enc
    if modifier:
        lookup_name += b'@' + modifier
    code = locale_alias.get(lookup_name, None)
    if code is not None:
        return code
    else:
        if modifier:
            code = locale_alias.get(lang_enc, None)
            if code is not None:
                if b'@' not in code:
                    return code + b'@' + modifier
                if code.split(b'@', 1)[1].translate(_ascii_lower_map) == modifier:
                    return code
        if encoding:
            lookup_name = langname
            if modifier:
                lookup_name += b'@' + modifier
            code = locale_alias.get(lookup_name, None)
            if code is not None:
                if b'@' not in code:
                    return _replace_encoding(code, encoding)
                code, modifier = code.split(b'@', 1)
                return _replace_encoding(code, encoding) + b'@' + modifier
            if modifier:
                code = locale_alias.get(langname, None)
                if code is not None:
                    if b'@' not in code:
                        return _replace_encoding(code, encoding) + b'@' + modifier
                    code, defmod = code.split(b'@', 1)
                    if defmod.translate(_ascii_lower_map) == modifier:
                        return _replace_encoding(code, encoding) + b'@' + defmod
        return localename


def _parse_localename(localename):
    code = normalize(localename)
    if b'@' in code:
        code, modifier = code.split(b'@', 1)
        if modifier == b'euro' and b'.' not in code:
            return (
             code, b'iso-8859-15')
    if b'.' in code:
        return tuple(code.split(b'.')[:2])
    else:
        if code == b'C':
            return (None, None)
        raise ValueError, b'unknown locale: %s' % localename
        return


def _build_localename(localetuple):
    language, encoding = localetuple
    if language is None:
        language = b'C'
    if encoding is None:
        return language
    else:
        return language + b'.' + encoding
        return


def getdefaultlocale(envvars=(b'LC_ALL', b'LC_CTYPE', b'LANG', b'LANGUAGE')):
    try:
        import _locale
        code, encoding = _locale._getdefaultlocale()
    except (ImportError, AttributeError):
        pass
    else:
        if sys.platform == b'win32' and code and code[:2] == b'0x':
            code = windows_locale.get(int(code, 0))
        return (
         code, encoding)

    import os
    lookup = os.environ.get
    for variable in envvars:
        localename = lookup(variable, None)
        if localename:
            if variable == b'LANGUAGE':
                localename = localename.split(b':')[0]
            break
    else:
        localename = b'C'

    return _parse_localename(localename)


def getlocale(category=LC_CTYPE):
    localename = _setlocale(category)
    if category == LC_ALL and b';' in localename:
        raise TypeError, b'category LC_ALL is not supported'
    return _parse_localename(localename)


def setlocale(category, locale=None):
    if locale and not isinstance(locale, (_str, _unicode)):
        locale = normalize(_build_localename(locale))
    return _setlocale(category, locale)


def resetlocale(category=LC_ALL):
    _setlocale(category, _build_localename(getdefaultlocale()))
    return


if sys.platform.startswith(b'win'):

    def getpreferredencoding(do_setlocale=True):
        import _locale
        return _locale._getdefaultlocale()[1]


else:
    try:
        CODESET
    except NameError:

        def getpreferredencoding(do_setlocale=True):
            return getdefaultlocale()[1]


    else:

        def getpreferredencoding(do_setlocale=True):
            if do_setlocale:
                oldloc = setlocale(LC_CTYPE)
                try:
                    setlocale(LC_CTYPE, b'')
                except Error:
                    pass

                result = nl_langinfo(CODESET)
                setlocale(LC_CTYPE, oldloc)
            else:
                result = nl_langinfo(CODESET)
            if not result and sys.platform == b'darwin':
                result = b'UTF-8'
            return result


locale_encoding_alias = {b'437': b'C', 
   b'c': b'C', 
   b'en': b'ISO8859-1', 
   b'jis': b'JIS7', 
   b'jis7': b'JIS7', 
   b'ajec': b'eucJP', 
   b'ascii': b'ISO8859-1', 
   b'latin_1': b'ISO8859-1', 
   b'iso8859_1': b'ISO8859-1', 
   b'iso8859_10': b'ISO8859-10', 
   b'iso8859_11': b'ISO8859-11', 
   b'iso8859_13': b'ISO8859-13', 
   b'iso8859_14': b'ISO8859-14', 
   b'iso8859_15': b'ISO8859-15', 
   b'iso8859_16': b'ISO8859-16', 
   b'iso8859_2': b'ISO8859-2', 
   b'iso8859_3': b'ISO8859-3', 
   b'iso8859_4': b'ISO8859-4', 
   b'iso8859_5': b'ISO8859-5', 
   b'iso8859_6': b'ISO8859-6', 
   b'iso8859_7': b'ISO8859-7', 
   b'iso8859_8': b'ISO8859-8', 
   b'iso8859_9': b'ISO8859-9', 
   b'iso2022_jp': b'JIS7', 
   b'shift_jis': b'SJIS', 
   b'tactis': b'TACTIS', 
   b'euc_jp': b'eucJP', 
   b'euc_kr': b'eucKR', 
   b'utf_8': b'UTF-8', 
   b'koi8_r': b'KOI8-R', 
   b'koi8_u': b'KOI8-U'}
locale_alias = {b'a3': b'az_AZ.KOI8-C', 
   b'a3_az': b'az_AZ.KOI8-C', 
   b'a3_az.koi8c': b'az_AZ.KOI8-C', 
   b'a3_az.koic': b'az_AZ.KOI8-C', 
   b'aa_dj': b'aa_DJ.ISO8859-1', 
   b'aa_er': b'aa_ER.UTF-8', 
   b'aa_et': b'aa_ET.UTF-8', 
   b'af': b'af_ZA.ISO8859-1', 
   b'af_za': b'af_ZA.ISO8859-1', 
   b'af_za.iso88591': b'af_ZA.ISO8859-1', 
   b'agr_pe': b'agr_PE.UTF-8', 
   b'ak_gh': b'ak_GH.UTF-8', 
   b'am': b'am_ET.UTF-8', 
   b'am_et': b'am_ET.UTF-8', 
   b'american': b'en_US.ISO8859-1', 
   b'american.iso88591': b'en_US.ISO8859-1', 
   b'an_es': b'an_ES.ISO8859-15', 
   b'anp_in': b'anp_IN.UTF-8', 
   b'ar': b'ar_AA.ISO8859-6', 
   b'ar_aa': b'ar_AA.ISO8859-6', 
   b'ar_aa.iso88596': b'ar_AA.ISO8859-6', 
   b'ar_ae': b'ar_AE.ISO8859-6', 
   b'ar_ae.iso88596': b'ar_AE.ISO8859-6', 
   b'ar_bh': b'ar_BH.ISO8859-6', 
   b'ar_bh.iso88596': b'ar_BH.ISO8859-6', 
   b'ar_dz': b'ar_DZ.ISO8859-6', 
   b'ar_dz.iso88596': b'ar_DZ.ISO8859-6', 
   b'ar_eg': b'ar_EG.ISO8859-6', 
   b'ar_eg.iso88596': b'ar_EG.ISO8859-6', 
   b'ar_in': b'ar_IN.UTF-8', 
   b'ar_iq': b'ar_IQ.ISO8859-6', 
   b'ar_iq.iso88596': b'ar_IQ.ISO8859-6', 
   b'ar_jo': b'ar_JO.ISO8859-6', 
   b'ar_jo.iso88596': b'ar_JO.ISO8859-6', 
   b'ar_kw': b'ar_KW.ISO8859-6', 
   b'ar_kw.iso88596': b'ar_KW.ISO8859-6', 
   b'ar_lb': b'ar_LB.ISO8859-6', 
   b'ar_lb.iso88596': b'ar_LB.ISO8859-6', 
   b'ar_ly': b'ar_LY.ISO8859-6', 
   b'ar_ly.iso88596': b'ar_LY.ISO8859-6', 
   b'ar_ma': b'ar_MA.ISO8859-6', 
   b'ar_ma.iso88596': b'ar_MA.ISO8859-6', 
   b'ar_om': b'ar_OM.ISO8859-6', 
   b'ar_om.iso88596': b'ar_OM.ISO8859-6', 
   b'ar_qa': b'ar_QA.ISO8859-6', 
   b'ar_qa.iso88596': b'ar_QA.ISO8859-6', 
   b'ar_sa': b'ar_SA.ISO8859-6', 
   b'ar_sa.iso88596': b'ar_SA.ISO8859-6', 
   b'ar_sd': b'ar_SD.ISO8859-6', 
   b'ar_sd.iso88596': b'ar_SD.ISO8859-6', 
   b'ar_ss': b'ar_SS.UTF-8', 
   b'ar_sy': b'ar_SY.ISO8859-6', 
   b'ar_sy.iso88596': b'ar_SY.ISO8859-6', 
   b'ar_tn': b'ar_TN.ISO8859-6', 
   b'ar_tn.iso88596': b'ar_TN.ISO8859-6', 
   b'ar_ye': b'ar_YE.ISO8859-6', 
   b'ar_ye.iso88596': b'ar_YE.ISO8859-6', 
   b'arabic': b'ar_AA.ISO8859-6', 
   b'arabic.iso88596': b'ar_AA.ISO8859-6', 
   b'as': b'as_IN.UTF-8', 
   b'as_in': b'as_IN.UTF-8', 
   b'ast_es': b'ast_ES.ISO8859-15', 
   b'ayc_pe': b'ayc_PE.UTF-8', 
   b'az': b'az_AZ.ISO8859-9E', 
   b'az_az': b'az_AZ.ISO8859-9E', 
   b'az_az.iso88599e': b'az_AZ.ISO8859-9E', 
   b'az_ir': b'az_IR.UTF-8', 
   b'be': b'be_BY.CP1251', 
   b'be@latin': b'be_BY.UTF-8@latin', 
   b'be_bg.utf8': b'bg_BG.UTF-8', 
   b'be_by': b'be_BY.CP1251', 
   b'be_by.cp1251': b'be_BY.CP1251', 
   b'be_by.microsoftcp1251': b'be_BY.CP1251', 
   b'be_by.utf8@latin': b'be_BY.UTF-8@latin', 
   b'be_by@latin': b'be_BY.UTF-8@latin', 
   b'bem_zm': b'bem_ZM.UTF-8', 
   b'ber_dz': b'ber_DZ.UTF-8', 
   b'ber_ma': b'ber_MA.UTF-8', 
   b'bg': b'bg_BG.CP1251', 
   b'bg_bg': b'bg_BG.CP1251', 
   b'bg_bg.cp1251': b'bg_BG.CP1251', 
   b'bg_bg.iso88595': b'bg_BG.ISO8859-5', 
   b'bg_bg.koi8r': b'bg_BG.KOI8-R', 
   b'bg_bg.microsoftcp1251': b'bg_BG.CP1251', 
   b'bhb_in.utf8': b'bhb_IN.UTF-8', 
   b'bho_in': b'bho_IN.UTF-8', 
   b'bho_np': b'bho_NP.UTF-8', 
   b'bi_vu': b'bi_VU.UTF-8', 
   b'bn_bd': b'bn_BD.UTF-8', 
   b'bn_in': b'bn_IN.UTF-8', 
   b'bo_cn': b'bo_CN.UTF-8', 
   b'bo_in': b'bo_IN.UTF-8', 
   b'bokmal': b'nb_NO.ISO8859-1', 
   b'bokm\xe5l': b'nb_NO.ISO8859-1', 
   b'br': b'br_FR.ISO8859-1', 
   b'br_fr': b'br_FR.ISO8859-1', 
   b'br_fr.iso88591': b'br_FR.ISO8859-1', 
   b'br_fr.iso885914': b'br_FR.ISO8859-14', 
   b'br_fr.iso885915': b'br_FR.ISO8859-15', 
   b'br_fr.iso885915@euro': b'br_FR.ISO8859-15', 
   b'br_fr.utf8@euro': b'br_FR.UTF-8', 
   b'br_fr@euro': b'br_FR.ISO8859-15', 
   b'brx_in': b'brx_IN.UTF-8', 
   b'bs': b'bs_BA.ISO8859-2', 
   b'bs_ba': b'bs_BA.ISO8859-2', 
   b'bs_ba.iso88592': b'bs_BA.ISO8859-2', 
   b'bulgarian': b'bg_BG.CP1251', 
   b'byn_er': b'byn_ER.UTF-8', 
   b'c': b'C', 
   b'c-french': b'fr_CA.ISO8859-1', 
   b'c-french.iso88591': b'fr_CA.ISO8859-1', 
   b'c.ascii': b'C', 
   b'c.en': b'C', 
   b'c.iso88591': b'en_US.ISO8859-1', 
   b'c.utf8': b'en_US.UTF-8', 
   b'c_c': b'C', 
   b'c_c.c': b'C', 
   b'ca': b'ca_ES.ISO8859-1', 
   b'ca_ad': b'ca_AD.ISO8859-1', 
   b'ca_ad.iso88591': b'ca_AD.ISO8859-1', 
   b'ca_ad.iso885915': b'ca_AD.ISO8859-15', 
   b'ca_ad.iso885915@euro': b'ca_AD.ISO8859-15', 
   b'ca_ad.utf8@euro': b'ca_AD.UTF-8', 
   b'ca_ad@euro': b'ca_AD.ISO8859-15', 
   b'ca_es': b'ca_ES.ISO8859-1', 
   b'ca_es.iso88591': b'ca_ES.ISO8859-1', 
   b'ca_es.iso885915': b'ca_ES.ISO8859-15', 
   b'ca_es.iso885915@euro': b'ca_ES.ISO8859-15', 
   b'ca_es.utf8@euro': b'ca_ES.UTF-8', 
   b'ca_es@euro': b'ca_ES.ISO8859-15', 
   b'ca_es@valencia': b'ca_ES.UTF-8@valencia', 
   b'ca_fr': b'ca_FR.ISO8859-1', 
   b'ca_fr.iso88591': b'ca_FR.ISO8859-1', 
   b'ca_fr.iso885915': b'ca_FR.ISO8859-15', 
   b'ca_fr.iso885915@euro': b'ca_FR.ISO8859-15', 
   b'ca_fr.utf8@euro': b'ca_FR.UTF-8', 
   b'ca_fr@euro': b'ca_FR.ISO8859-15', 
   b'ca_it': b'ca_IT.ISO8859-1', 
   b'ca_it.iso88591': b'ca_IT.ISO8859-1', 
   b'ca_it.iso885915': b'ca_IT.ISO8859-15', 
   b'ca_it.iso885915@euro': b'ca_IT.ISO8859-15', 
   b'ca_it.utf8@euro': b'ca_IT.UTF-8', 
   b'ca_it@euro': b'ca_IT.ISO8859-15', 
   b'catalan': b'ca_ES.ISO8859-1', 
   b'ce_ru': b'ce_RU.UTF-8', 
   b'cextend': b'en_US.ISO8859-1', 
   b'cextend.en': b'en_US.ISO8859-1', 
   b'chinese-s': b'zh_CN.eucCN', 
   b'chinese-t': b'zh_TW.eucTW', 
   b'chr_us': b'chr_US.UTF-8', 
   b'ckb_iq': b'ckb_IQ.UTF-8', 
   b'cmn_tw': b'cmn_TW.UTF-8', 
   b'crh_ua': b'crh_UA.UTF-8', 
   b'croatian': b'hr_HR.ISO8859-2', 
   b'cs': b'cs_CZ.ISO8859-2', 
   b'cs_cs': b'cs_CZ.ISO8859-2', 
   b'cs_cs.iso88592': b'cs_CZ.ISO8859-2', 
   b'cs_cz': b'cs_CZ.ISO8859-2', 
   b'cs_cz.iso88592': b'cs_CZ.ISO8859-2', 
   b'csb_pl': b'csb_PL.UTF-8', 
   b'cv_ru': b'cv_RU.UTF-8', 
   b'cy': b'cy_GB.ISO8859-1', 
   b'cy_gb': b'cy_GB.ISO8859-1', 
   b'cy_gb.iso88591': b'cy_GB.ISO8859-1', 
   b'cy_gb.iso885914': b'cy_GB.ISO8859-14', 
   b'cy_gb.iso885915': b'cy_GB.ISO8859-15', 
   b'cy_gb@euro': b'cy_GB.ISO8859-15', 
   b'cz': b'cs_CZ.ISO8859-2', 
   b'cz_cz': b'cs_CZ.ISO8859-2', 
   b'czech': b'cs_CZ.ISO8859-2', 
   b'da': b'da_DK.ISO8859-1', 
   b'da.iso885915': b'da_DK.ISO8859-15', 
   b'da_dk': b'da_DK.ISO8859-1', 
   b'da_dk.88591': b'da_DK.ISO8859-1', 
   b'da_dk.885915': b'da_DK.ISO8859-15', 
   b'da_dk.iso88591': b'da_DK.ISO8859-1', 
   b'da_dk.iso885915': b'da_DK.ISO8859-15', 
   b'da_dk@euro': b'da_DK.ISO8859-15', 
   b'danish': b'da_DK.ISO8859-1', 
   b'danish.iso88591': b'da_DK.ISO8859-1', 
   b'dansk': b'da_DK.ISO8859-1', 
   b'de': b'de_DE.ISO8859-1', 
   b'de.iso885915': b'de_DE.ISO8859-15', 
   b'de_at': b'de_AT.ISO8859-1', 
   b'de_at.iso88591': b'de_AT.ISO8859-1', 
   b'de_at.iso885915': b'de_AT.ISO8859-15', 
   b'de_at.iso885915@euro': b'de_AT.ISO8859-15', 
   b'de_at.utf8@euro': b'de_AT.UTF-8', 
   b'de_at@euro': b'de_AT.ISO8859-15', 
   b'de_be': b'de_BE.ISO8859-1', 
   b'de_be.iso88591': b'de_BE.ISO8859-1', 
   b'de_be.iso885915': b'de_BE.ISO8859-15', 
   b'de_be.iso885915@euro': b'de_BE.ISO8859-15', 
   b'de_be.utf8@euro': b'de_BE.UTF-8', 
   b'de_be@euro': b'de_BE.ISO8859-15', 
   b'de_ch': b'de_CH.ISO8859-1', 
   b'de_ch.iso88591': b'de_CH.ISO8859-1', 
   b'de_ch.iso885915': b'de_CH.ISO8859-15', 
   b'de_ch@euro': b'de_CH.ISO8859-15', 
   b'de_de': b'de_DE.ISO8859-1', 
   b'de_de.88591': b'de_DE.ISO8859-1', 
   b'de_de.885915': b'de_DE.ISO8859-15', 
   b'de_de.885915@euro': b'de_DE.ISO8859-15', 
   b'de_de.iso88591': b'de_DE.ISO8859-1', 
   b'de_de.iso885915': b'de_DE.ISO8859-15', 
   b'de_de.iso885915@euro': b'de_DE.ISO8859-15', 
   b'de_de.utf8@euro': b'de_DE.UTF-8', 
   b'de_de@euro': b'de_DE.ISO8859-15', 
   b'de_it': b'de_IT.ISO8859-1', 
   b'de_li.utf8': b'de_LI.UTF-8', 
   b'de_lu': b'de_LU.ISO8859-1', 
   b'de_lu.iso88591': b'de_LU.ISO8859-1', 
   b'de_lu.iso885915': b'de_LU.ISO8859-15', 
   b'de_lu.iso885915@euro': b'de_LU.ISO8859-15', 
   b'de_lu.utf8@euro': b'de_LU.UTF-8', 
   b'de_lu@euro': b'de_LU.ISO8859-15', 
   b'deutsch': b'de_DE.ISO8859-1', 
   b'doi_in': b'doi_IN.UTF-8', 
   b'dutch': b'nl_NL.ISO8859-1', 
   b'dutch.iso88591': b'nl_BE.ISO8859-1', 
   b'dv_mv': b'dv_MV.UTF-8', 
   b'dz_bt': b'dz_BT.UTF-8', 
   b'ee': b'ee_EE.ISO8859-4', 
   b'ee_ee': b'ee_EE.ISO8859-4', 
   b'ee_ee.iso88594': b'ee_EE.ISO8859-4', 
   b'eesti': b'et_EE.ISO8859-1', 
   b'el': b'el_GR.ISO8859-7', 
   b'el_cy': b'el_CY.ISO8859-7', 
   b'el_gr': b'el_GR.ISO8859-7', 
   b'el_gr.iso88597': b'el_GR.ISO8859-7', 
   b'el_gr@euro': b'el_GR.ISO8859-15', 
   b'en': b'en_US.ISO8859-1', 
   b'en.iso88591': b'en_US.ISO8859-1', 
   b'en_ag': b'en_AG.UTF-8', 
   b'en_au': b'en_AU.ISO8859-1', 
   b'en_au.iso88591': b'en_AU.ISO8859-1', 
   b'en_be': b'en_BE.ISO8859-1', 
   b'en_be@euro': b'en_BE.ISO8859-15', 
   b'en_bw': b'en_BW.ISO8859-1', 
   b'en_bw.iso88591': b'en_BW.ISO8859-1', 
   b'en_ca': b'en_CA.ISO8859-1', 
   b'en_ca.iso88591': b'en_CA.ISO8859-1', 
   b'en_dk': b'en_DK.ISO8859-1', 
   b'en_dk.iso88591': b'en_DK.ISO8859-1', 
   b'en_dk.iso885915': b'en_DK.ISO8859-15', 
   b'en_dl.utf8': b'en_DL.UTF-8', 
   b'en_gb': b'en_GB.ISO8859-1', 
   b'en_gb.88591': b'en_GB.ISO8859-1', 
   b'en_gb.iso88591': b'en_GB.ISO8859-1', 
   b'en_gb.iso885915': b'en_GB.ISO8859-15', 
   b'en_gb@euro': b'en_GB.ISO8859-15', 
   b'en_hk': b'en_HK.ISO8859-1', 
   b'en_hk.iso88591': b'en_HK.ISO8859-1', 
   b'en_ie': b'en_IE.ISO8859-1', 
   b'en_ie.iso88591': b'en_IE.ISO8859-1', 
   b'en_ie.iso885915': b'en_IE.ISO8859-15', 
   b'en_ie.iso885915@euro': b'en_IE.ISO8859-15', 
   b'en_ie.utf8@euro': b'en_IE.UTF-8', 
   b'en_ie@euro': b'en_IE.ISO8859-15', 
   b'en_il': b'en_IL.UTF-8', 
   b'en_in': b'en_IN.ISO8859-1', 
   b'en_ng': b'en_NG.UTF-8', 
   b'en_nz': b'en_NZ.ISO8859-1', 
   b'en_nz.iso88591': b'en_NZ.ISO8859-1', 
   b'en_ph': b'en_PH.ISO8859-1', 
   b'en_ph.iso88591': b'en_PH.ISO8859-1', 
   b'en_sc.utf8': b'en_SC.UTF-8', 
   b'en_sg': b'en_SG.ISO8859-1', 
   b'en_sg.iso88591': b'en_SG.ISO8859-1', 
   b'en_uk': b'en_GB.ISO8859-1', 
   b'en_us': b'en_US.ISO8859-1', 
   b'en_us.88591': b'en_US.ISO8859-1', 
   b'en_us.885915': b'en_US.ISO8859-15', 
   b'en_us.iso88591': b'en_US.ISO8859-1', 
   b'en_us.iso885915': b'en_US.ISO8859-15', 
   b'en_us.iso885915@euro': b'en_US.ISO8859-15', 
   b'en_us@euro': b'en_US.ISO8859-15', 
   b'en_us@euro@euro': b'en_US.ISO8859-15', 
   b'en_za': b'en_ZA.ISO8859-1', 
   b'en_za.88591': b'en_ZA.ISO8859-1', 
   b'en_za.iso88591': b'en_ZA.ISO8859-1', 
   b'en_za.iso885915': b'en_ZA.ISO8859-15', 
   b'en_za@euro': b'en_ZA.ISO8859-15', 
   b'en_zm': b'en_ZM.UTF-8', 
   b'en_zw': b'en_ZW.ISO8859-1', 
   b'en_zw.iso88591': b'en_ZW.ISO8859-1', 
   b'en_zw.utf8': b'en_ZS.UTF-8', 
   b'eng_gb': b'en_GB.ISO8859-1', 
   b'eng_gb.8859': b'en_GB.ISO8859-1', 
   b'english': b'en_EN.ISO8859-1', 
   b'english.iso88591': b'en_US.ISO8859-1', 
   b'english_uk': b'en_GB.ISO8859-1', 
   b'english_uk.8859': b'en_GB.ISO8859-1', 
   b'english_united-states': b'en_US.ISO8859-1', 
   b'english_united-states.437': b'C', 
   b'english_us': b'en_US.ISO8859-1', 
   b'english_us.8859': b'en_US.ISO8859-1', 
   b'english_us.ascii': b'en_US.ISO8859-1', 
   b'eo': b'eo_XX.ISO8859-3', 
   b'eo.utf8': b'eo.UTF-8', 
   b'eo_eo': b'eo_EO.ISO8859-3', 
   b'eo_eo.iso88593': b'eo_EO.ISO8859-3', 
   b'eo_us.utf8': b'eo_US.UTF-8', 
   b'eo_xx': b'eo_XX.ISO8859-3', 
   b'eo_xx.iso88593': b'eo_XX.ISO8859-3', 
   b'es': b'es_ES.ISO8859-1', 
   b'es_ar': b'es_AR.ISO8859-1', 
   b'es_ar.iso88591': b'es_AR.ISO8859-1', 
   b'es_bo': b'es_BO.ISO8859-1', 
   b'es_bo.iso88591': b'es_BO.ISO8859-1', 
   b'es_cl': b'es_CL.ISO8859-1', 
   b'es_cl.iso88591': b'es_CL.ISO8859-1', 
   b'es_co': b'es_CO.ISO8859-1', 
   b'es_co.iso88591': b'es_CO.ISO8859-1', 
   b'es_cr': b'es_CR.ISO8859-1', 
   b'es_cr.iso88591': b'es_CR.ISO8859-1', 
   b'es_cu': b'es_CU.UTF-8', 
   b'es_do': b'es_DO.ISO8859-1', 
   b'es_do.iso88591': b'es_DO.ISO8859-1', 
   b'es_ec': b'es_EC.ISO8859-1', 
   b'es_ec.iso88591': b'es_EC.ISO8859-1', 
   b'es_es': b'es_ES.ISO8859-1', 
   b'es_es.88591': b'es_ES.ISO8859-1', 
   b'es_es.iso88591': b'es_ES.ISO8859-1', 
   b'es_es.iso885915': b'es_ES.ISO8859-15', 
   b'es_es.iso885915@euro': b'es_ES.ISO8859-15', 
   b'es_es.utf8@euro': b'es_ES.UTF-8', 
   b'es_es@euro': b'es_ES.ISO8859-15', 
   b'es_gt': b'es_GT.ISO8859-1', 
   b'es_gt.iso88591': b'es_GT.ISO8859-1', 
   b'es_hn': b'es_HN.ISO8859-1', 
   b'es_hn.iso88591': b'es_HN.ISO8859-1', 
   b'es_mx': b'es_MX.ISO8859-1', 
   b'es_mx.iso88591': b'es_MX.ISO8859-1', 
   b'es_ni': b'es_NI.ISO8859-1', 
   b'es_ni.iso88591': b'es_NI.ISO8859-1', 
   b'es_pa': b'es_PA.ISO8859-1', 
   b'es_pa.iso88591': b'es_PA.ISO8859-1', 
   b'es_pa.iso885915': b'es_PA.ISO8859-15', 
   b'es_pa@euro': b'es_PA.ISO8859-15', 
   b'es_pe': b'es_PE.ISO8859-1', 
   b'es_pe.iso88591': b'es_PE.ISO8859-1', 
   b'es_pe.iso885915': b'es_PE.ISO8859-15', 
   b'es_pe@euro': b'es_PE.ISO8859-15', 
   b'es_pr': b'es_PR.ISO8859-1', 
   b'es_pr.iso88591': b'es_PR.ISO8859-1', 
   b'es_py': b'es_PY.ISO8859-1', 
   b'es_py.iso88591': b'es_PY.ISO8859-1', 
   b'es_py.iso885915': b'es_PY.ISO8859-15', 
   b'es_py@euro': b'es_PY.ISO8859-15', 
   b'es_sv': b'es_SV.ISO8859-1', 
   b'es_sv.iso88591': b'es_SV.ISO8859-1', 
   b'es_sv.iso885915': b'es_SV.ISO8859-15', 
   b'es_sv@euro': b'es_SV.ISO8859-15', 
   b'es_us': b'es_US.ISO8859-1', 
   b'es_us.iso88591': b'es_US.ISO8859-1', 
   b'es_uy': b'es_UY.ISO8859-1', 
   b'es_uy.iso88591': b'es_UY.ISO8859-1', 
   b'es_uy.iso885915': b'es_UY.ISO8859-15', 
   b'es_uy@euro': b'es_UY.ISO8859-15', 
   b'es_ve': b'es_VE.ISO8859-1', 
   b'es_ve.iso88591': b'es_VE.ISO8859-1', 
   b'es_ve.iso885915': b'es_VE.ISO8859-15', 
   b'es_ve@euro': b'es_VE.ISO8859-15', 
   b'estonian': b'et_EE.ISO8859-1', 
   b'et': b'et_EE.ISO8859-15', 
   b'et_ee': b'et_EE.ISO8859-15', 
   b'et_ee.iso88591': b'et_EE.ISO8859-1', 
   b'et_ee.iso885913': b'et_EE.ISO8859-13', 
   b'et_ee.iso885915': b'et_EE.ISO8859-15', 
   b'et_ee.iso88594': b'et_EE.ISO8859-4', 
   b'et_ee@euro': b'et_EE.ISO8859-15', 
   b'eu': b'eu_ES.ISO8859-1', 
   b'eu_es': b'eu_ES.ISO8859-1', 
   b'eu_es.iso88591': b'eu_ES.ISO8859-1', 
   b'eu_es.iso885915': b'eu_ES.ISO8859-15', 
   b'eu_es.iso885915@euro': b'eu_ES.ISO8859-15', 
   b'eu_es.utf8@euro': b'eu_ES.UTF-8', 
   b'eu_es@euro': b'eu_ES.ISO8859-15', 
   b'eu_fr': b'eu_FR.ISO8859-1', 
   b'fa': b'fa_IR.UTF-8', 
   b'fa_ir': b'fa_IR.UTF-8', 
   b'fa_ir.isiri3342': b'fa_IR.ISIRI-3342', 
   b'ff_sn': b'ff_SN.UTF-8', 
   b'fi': b'fi_FI.ISO8859-15', 
   b'fi.iso885915': b'fi_FI.ISO8859-15', 
   b'fi_fi': b'fi_FI.ISO8859-15', 
   b'fi_fi.88591': b'fi_FI.ISO8859-1', 
   b'fi_fi.iso88591': b'fi_FI.ISO8859-1', 
   b'fi_fi.iso885915': b'fi_FI.ISO8859-15', 
   b'fi_fi.iso885915@euro': b'fi_FI.ISO8859-15', 
   b'fi_fi.utf8@euro': b'fi_FI.UTF-8', 
   b'fi_fi@euro': b'fi_FI.ISO8859-15', 
   b'fil_ph': b'fil_PH.UTF-8', 
   b'finnish': b'fi_FI.ISO8859-1', 
   b'finnish.iso88591': b'fi_FI.ISO8859-1', 
   b'fo': b'fo_FO.ISO8859-1', 
   b'fo_fo': b'fo_FO.ISO8859-1', 
   b'fo_fo.iso88591': b'fo_FO.ISO8859-1', 
   b'fo_fo.iso885915': b'fo_FO.ISO8859-15', 
   b'fo_fo@euro': b'fo_FO.ISO8859-15', 
   b'fr': b'fr_FR.ISO8859-1', 
   b'fr.iso885915': b'fr_FR.ISO8859-15', 
   b'fr_be': b'fr_BE.ISO8859-1', 
   b'fr_be.88591': b'fr_BE.ISO8859-1', 
   b'fr_be.iso88591': b'fr_BE.ISO8859-1', 
   b'fr_be.iso885915': b'fr_BE.ISO8859-15', 
   b'fr_be.iso885915@euro': b'fr_BE.ISO8859-15', 
   b'fr_be.utf8@euro': b'fr_BE.UTF-8', 
   b'fr_be@euro': b'fr_BE.ISO8859-15', 
   b'fr_ca': b'fr_CA.ISO8859-1', 
   b'fr_ca.88591': b'fr_CA.ISO8859-1', 
   b'fr_ca.iso88591': b'fr_CA.ISO8859-1', 
   b'fr_ca.iso885915': b'fr_CA.ISO8859-15', 
   b'fr_ca@euro': b'fr_CA.ISO8859-15', 
   b'fr_ch': b'fr_CH.ISO8859-1', 
   b'fr_ch.88591': b'fr_CH.ISO8859-1', 
   b'fr_ch.iso88591': b'fr_CH.ISO8859-1', 
   b'fr_ch.iso885915': b'fr_CH.ISO8859-15', 
   b'fr_ch@euro': b'fr_CH.ISO8859-15', 
   b'fr_fr': b'fr_FR.ISO8859-1', 
   b'fr_fr.88591': b'fr_FR.ISO8859-1', 
   b'fr_fr.iso88591': b'fr_FR.ISO8859-1', 
   b'fr_fr.iso885915': b'fr_FR.ISO8859-15', 
   b'fr_fr.iso885915@euro': b'fr_FR.ISO8859-15', 
   b'fr_fr.utf8@euro': b'fr_FR.UTF-8', 
   b'fr_fr@euro': b'fr_FR.ISO8859-15', 
   b'fr_lu': b'fr_LU.ISO8859-1', 
   b'fr_lu.88591': b'fr_LU.ISO8859-1', 
   b'fr_lu.iso88591': b'fr_LU.ISO8859-1', 
   b'fr_lu.iso885915': b'fr_LU.ISO8859-15', 
   b'fr_lu.iso885915@euro': b'fr_LU.ISO8859-15', 
   b'fr_lu.utf8@euro': b'fr_LU.UTF-8', 
   b'fr_lu@euro': b'fr_LU.ISO8859-15', 
   b'fran\xe7ais': b'fr_FR.ISO8859-1', 
   b'fre_fr': b'fr_FR.ISO8859-1', 
   b'fre_fr.8859': b'fr_FR.ISO8859-1', 
   b'french': b'fr_FR.ISO8859-1', 
   b'french.iso88591': b'fr_CH.ISO8859-1', 
   b'french_france': b'fr_FR.ISO8859-1', 
   b'french_france.8859': b'fr_FR.ISO8859-1', 
   b'fur_it': b'fur_IT.UTF-8', 
   b'fy_de': b'fy_DE.UTF-8', 
   b'fy_nl': b'fy_NL.UTF-8', 
   b'ga': b'ga_IE.ISO8859-1', 
   b'ga_ie': b'ga_IE.ISO8859-1', 
   b'ga_ie.iso88591': b'ga_IE.ISO8859-1', 
   b'ga_ie.iso885914': b'ga_IE.ISO8859-14', 
   b'ga_ie.iso885915': b'ga_IE.ISO8859-15', 
   b'ga_ie.iso885915@euro': b'ga_IE.ISO8859-15', 
   b'ga_ie.utf8@euro': b'ga_IE.UTF-8', 
   b'ga_ie@euro': b'ga_IE.ISO8859-15', 
   b'galego': b'gl_ES.ISO8859-1', 
   b'galician': b'gl_ES.ISO8859-1', 
   b'gd': b'gd_GB.ISO8859-1', 
   b'gd_gb': b'gd_GB.ISO8859-1', 
   b'gd_gb.iso88591': b'gd_GB.ISO8859-1', 
   b'gd_gb.iso885914': b'gd_GB.ISO8859-14', 
   b'gd_gb.iso885915': b'gd_GB.ISO8859-15', 
   b'gd_gb@euro': b'gd_GB.ISO8859-15', 
   b'ger_de': b'de_DE.ISO8859-1', 
   b'ger_de.8859': b'de_DE.ISO8859-1', 
   b'german': b'de_DE.ISO8859-1', 
   b'german.iso88591': b'de_CH.ISO8859-1', 
   b'german_germany': b'de_DE.ISO8859-1', 
   b'german_germany.8859': b'de_DE.ISO8859-1', 
   b'gez_er': b'gez_ER.UTF-8', 
   b'gez_et': b'gez_ET.UTF-8', 
   b'gl': b'gl_ES.ISO8859-1', 
   b'gl_es': b'gl_ES.ISO8859-1', 
   b'gl_es.iso88591': b'gl_ES.ISO8859-1', 
   b'gl_es.iso885915': b'gl_ES.ISO8859-15', 
   b'gl_es.iso885915@euro': b'gl_ES.ISO8859-15', 
   b'gl_es.utf8@euro': b'gl_ES.UTF-8', 
   b'gl_es@euro': b'gl_ES.ISO8859-15', 
   b'greek': b'el_GR.ISO8859-7', 
   b'greek.iso88597': b'el_GR.ISO8859-7', 
   b'gu_in': b'gu_IN.UTF-8', 
   b'gv': b'gv_GB.ISO8859-1', 
   b'gv_gb': b'gv_GB.ISO8859-1', 
   b'gv_gb.iso88591': b'gv_GB.ISO8859-1', 
   b'gv_gb.iso885914': b'gv_GB.ISO8859-14', 
   b'gv_gb.iso885915': b'gv_GB.ISO8859-15', 
   b'gv_gb@euro': b'gv_GB.ISO8859-15', 
   b'ha_ng': b'ha_NG.UTF-8', 
   b'hak_tw': b'hak_TW.UTF-8', 
   b'he': b'he_IL.ISO8859-8', 
   b'he_il': b'he_IL.ISO8859-8', 
   b'he_il.cp1255': b'he_IL.CP1255', 
   b'he_il.iso88598': b'he_IL.ISO8859-8', 
   b'he_il.microsoftcp1255': b'he_IL.CP1255', 
   b'hebrew': b'he_IL.ISO8859-8', 
   b'hebrew.iso88598': b'he_IL.ISO8859-8', 
   b'hi': b'hi_IN.ISCII-DEV', 
   b'hi_in': b'hi_IN.ISCII-DEV', 
   b'hi_in.isciidev': b'hi_IN.ISCII-DEV', 
   b'hif_fj': b'hif_FJ.UTF-8', 
   b'hne': b'hne_IN.UTF-8', 
   b'hne_in': b'hne_IN.UTF-8', 
   b'hr': b'hr_HR.ISO8859-2', 
   b'hr_hr': b'hr_HR.ISO8859-2', 
   b'hr_hr.iso88592': b'hr_HR.ISO8859-2', 
   b'hrvatski': b'hr_HR.ISO8859-2', 
   b'hsb_de': b'hsb_DE.ISO8859-2', 
   b'ht_ht': b'ht_HT.UTF-8', 
   b'hu': b'hu_HU.ISO8859-2', 
   b'hu_hu': b'hu_HU.ISO8859-2', 
   b'hu_hu.iso88592': b'hu_HU.ISO8859-2', 
   b'hungarian': b'hu_HU.ISO8859-2', 
   b'hy_am': b'hy_AM.UTF-8', 
   b'hy_am.armscii8': b'hy_AM.ARMSCII_8', 
   b'ia': b'ia.UTF-8', 
   b'ia_fr': b'ia_FR.UTF-8', 
   b'icelandic': b'is_IS.ISO8859-1', 
   b'icelandic.iso88591': b'is_IS.ISO8859-1', 
   b'id': b'id_ID.ISO8859-1', 
   b'id_id': b'id_ID.ISO8859-1', 
   b'ig_ng': b'ig_NG.UTF-8', 
   b'ik_ca': b'ik_CA.UTF-8', 
   b'in': b'id_ID.ISO8859-1', 
   b'in_id': b'id_ID.ISO8859-1', 
   b'is': b'is_IS.ISO8859-1', 
   b'is_is': b'is_IS.ISO8859-1', 
   b'is_is.iso88591': b'is_IS.ISO8859-1', 
   b'is_is.iso885915': b'is_IS.ISO8859-15', 
   b'is_is@euro': b'is_IS.ISO8859-15', 
   b'iso-8859-1': b'en_US.ISO8859-1', 
   b'iso-8859-15': b'en_US.ISO8859-15', 
   b'iso8859-1': b'en_US.ISO8859-1', 
   b'iso8859-15': b'en_US.ISO8859-15', 
   b'iso_8859_1': b'en_US.ISO8859-1', 
   b'iso_8859_15': b'en_US.ISO8859-15', 
   b'it': b'it_IT.ISO8859-1', 
   b'it.iso885915': b'it_IT.ISO8859-15', 
   b'it_ch': b'it_CH.ISO8859-1', 
   b'it_ch.iso88591': b'it_CH.ISO8859-1', 
   b'it_ch.iso885915': b'it_CH.ISO8859-15', 
   b'it_ch@euro': b'it_CH.ISO8859-15', 
   b'it_it': b'it_IT.ISO8859-1', 
   b'it_it.88591': b'it_IT.ISO8859-1', 
   b'it_it.iso88591': b'it_IT.ISO8859-1', 
   b'it_it.iso885915': b'it_IT.ISO8859-15', 
   b'it_it.iso885915@euro': b'it_IT.ISO8859-15', 
   b'it_it.utf8@euro': b'it_IT.UTF-8', 
   b'it_it@euro': b'it_IT.ISO8859-15', 
   b'italian': b'it_IT.ISO8859-1', 
   b'italian.iso88591': b'it_IT.ISO8859-1', 
   b'iu': b'iu_CA.NUNACOM-8', 
   b'iu_ca': b'iu_CA.NUNACOM-8', 
   b'iu_ca.nunacom8': b'iu_CA.NUNACOM-8', 
   b'iw': b'he_IL.ISO8859-8', 
   b'iw_il': b'he_IL.ISO8859-8', 
   b'iw_il.iso88598': b'he_IL.ISO8859-8', 
   b'iw_il.utf8': b'iw_IL.UTF-8', 
   b'ja': b'ja_JP.eucJP', 
   b'ja.jis': b'ja_JP.JIS7', 
   b'ja.sjis': b'ja_JP.SJIS', 
   b'ja_jp': b'ja_JP.eucJP', 
   b'ja_jp.ajec': b'ja_JP.eucJP', 
   b'ja_jp.euc': b'ja_JP.eucJP', 
   b'ja_jp.eucjp': b'ja_JP.eucJP', 
   b'ja_jp.iso-2022-jp': b'ja_JP.JIS7', 
   b'ja_jp.iso2022jp': b'ja_JP.JIS7', 
   b'ja_jp.jis': b'ja_JP.JIS7', 
   b'ja_jp.jis7': b'ja_JP.JIS7', 
   b'ja_jp.mscode': b'ja_JP.SJIS', 
   b'ja_jp.pck': b'ja_JP.SJIS', 
   b'ja_jp.sjis': b'ja_JP.SJIS', 
   b'ja_jp.ujis': b'ja_JP.eucJP', 
   b'japan': b'ja_JP.eucJP', 
   b'japanese': b'ja_JP.eucJP', 
   b'japanese-euc': b'ja_JP.eucJP', 
   b'japanese.euc': b'ja_JP.eucJP', 
   b'japanese.sjis': b'ja_JP.SJIS', 
   b'jp_jp': b'ja_JP.eucJP', 
   b'ka': b'ka_GE.GEORGIAN-ACADEMY', 
   b'ka_ge': b'ka_GE.GEORGIAN-ACADEMY', 
   b'ka_ge.georgianacademy': b'ka_GE.GEORGIAN-ACADEMY', 
   b'ka_ge.georgianps': b'ka_GE.GEORGIAN-PS', 
   b'ka_ge.georgianrs': b'ka_GE.GEORGIAN-ACADEMY', 
   b'kab_dz': b'kab_DZ.UTF-8', 
   b'kk_kz': b'kk_KZ.ptcp154', 
   b'kl': b'kl_GL.ISO8859-1', 
   b'kl_gl': b'kl_GL.ISO8859-1', 
   b'kl_gl.iso88591': b'kl_GL.ISO8859-1', 
   b'kl_gl.iso885915': b'kl_GL.ISO8859-15', 
   b'kl_gl@euro': b'kl_GL.ISO8859-15', 
   b'km_kh': b'km_KH.UTF-8', 
   b'kn': b'kn_IN.UTF-8', 
   b'kn_in': b'kn_IN.UTF-8', 
   b'ko': b'ko_KR.eucKR', 
   b'ko_kr': b'ko_KR.eucKR', 
   b'ko_kr.euc': b'ko_KR.eucKR', 
   b'ko_kr.euckr': b'ko_KR.eucKR', 
   b'kok_in': b'kok_IN.UTF-8', 
   b'korean': b'ko_KR.eucKR', 
   b'korean.euc': b'ko_KR.eucKR', 
   b'ks': b'ks_IN.UTF-8', 
   b'ks_in': b'ks_IN.UTF-8', 
   b'ks_in.utf8@devanagari': b'ks_IN.UTF-8@devanagari', 
   b'ks_in@devanagari': b'ks_IN.UTF-8@devanagari', 
   b'ks_in@devanagari.utf8': b'ks_IN.UTF-8@devanagari', 
   b'ku_tr': b'ku_TR.ISO8859-9', 
   b'kw': b'kw_GB.ISO8859-1', 
   b'kw_gb': b'kw_GB.ISO8859-1', 
   b'kw_gb.iso88591': b'kw_GB.ISO8859-1', 
   b'kw_gb.iso885914': b'kw_GB.ISO8859-14', 
   b'kw_gb.iso885915': b'kw_GB.ISO8859-15', 
   b'kw_gb@euro': b'kw_GB.ISO8859-15', 
   b'ky': b'ky_KG.UTF-8', 
   b'ky_kg': b'ky_KG.UTF-8', 
   b'lb_lu': b'lb_LU.UTF-8', 
   b'lg_ug': b'lg_UG.ISO8859-10', 
   b'li_be': b'li_BE.UTF-8', 
   b'li_nl': b'li_NL.UTF-8', 
   b'lij_it': b'lij_IT.UTF-8', 
   b'lithuanian': b'lt_LT.ISO8859-13', 
   b'ln_cd': b'ln_CD.UTF-8', 
   b'lo': b'lo_LA.MULELAO-1', 
   b'lo_la': b'lo_LA.MULELAO-1', 
   b'lo_la.cp1133': b'lo_LA.IBM-CP1133', 
   b'lo_la.ibmcp1133': b'lo_LA.IBM-CP1133', 
   b'lo_la.mulelao1': b'lo_LA.MULELAO-1', 
   b'lt': b'lt_LT.ISO8859-13', 
   b'lt_lt': b'lt_LT.ISO8859-13', 
   b'lt_lt.iso885913': b'lt_LT.ISO8859-13', 
   b'lt_lt.iso88594': b'lt_LT.ISO8859-4', 
   b'lv': b'lv_LV.ISO8859-13', 
   b'lv_lv': b'lv_LV.ISO8859-13', 
   b'lv_lv.iso885913': b'lv_LV.ISO8859-13', 
   b'lv_lv.iso88594': b'lv_LV.ISO8859-4', 
   b'lzh_tw': b'lzh_TW.UTF-8', 
   b'mag_in': b'mag_IN.UTF-8', 
   b'mai': b'mai_IN.UTF-8', 
   b'mai_in': b'mai_IN.UTF-8', 
   b'mai_np': b'mai_NP.UTF-8', 
   b'mfe_mu': b'mfe_MU.UTF-8', 
   b'mg_mg': b'mg_MG.ISO8859-15', 
   b'mhr_ru': b'mhr_RU.UTF-8', 
   b'mi': b'mi_NZ.ISO8859-1', 
   b'mi_nz': b'mi_NZ.ISO8859-1', 
   b'mi_nz.iso88591': b'mi_NZ.ISO8859-1', 
   b'miq_ni': b'miq_NI.UTF-8', 
   b'mjw_in': b'mjw_IN.UTF-8', 
   b'mk': b'mk_MK.ISO8859-5', 
   b'mk_mk': b'mk_MK.ISO8859-5', 
   b'mk_mk.cp1251': b'mk_MK.CP1251', 
   b'mk_mk.iso88595': b'mk_MK.ISO8859-5', 
   b'mk_mk.microsoftcp1251': b'mk_MK.CP1251', 
   b'ml': b'ml_IN.UTF-8', 
   b'ml_in': b'ml_IN.UTF-8', 
   b'mn_mn': b'mn_MN.UTF-8', 
   b'mni_in': b'mni_IN.UTF-8', 
   b'mr': b'mr_IN.UTF-8', 
   b'mr_in': b'mr_IN.UTF-8', 
   b'ms': b'ms_MY.ISO8859-1', 
   b'ms_my': b'ms_MY.ISO8859-1', 
   b'ms_my.iso88591': b'ms_MY.ISO8859-1', 
   b'mt': b'mt_MT.ISO8859-3', 
   b'mt_mt': b'mt_MT.ISO8859-3', 
   b'mt_mt.iso88593': b'mt_MT.ISO8859-3', 
   b'my_mm': b'my_MM.UTF-8', 
   b'nan_tw': b'nan_TW.UTF-8', 
   b'nb': b'nb_NO.ISO8859-1', 
   b'nb_no': b'nb_NO.ISO8859-1', 
   b'nb_no.88591': b'nb_NO.ISO8859-1', 
   b'nb_no.iso88591': b'nb_NO.ISO8859-1', 
   b'nb_no.iso885915': b'nb_NO.ISO8859-15', 
   b'nb_no@euro': b'nb_NO.ISO8859-15', 
   b'nds_de': b'nds_DE.UTF-8', 
   b'nds_nl': b'nds_NL.UTF-8', 
   b'ne_np': b'ne_NP.UTF-8', 
   b'nhn_mx': b'nhn_MX.UTF-8', 
   b'niu_nu': b'niu_NU.UTF-8', 
   b'niu_nz': b'niu_NZ.UTF-8', 
   b'nl': b'nl_NL.ISO8859-1', 
   b'nl.iso885915': b'nl_NL.ISO8859-15', 
   b'nl_aw': b'nl_AW.UTF-8', 
   b'nl_be': b'nl_BE.ISO8859-1', 
   b'nl_be.88591': b'nl_BE.ISO8859-1', 
   b'nl_be.iso88591': b'nl_BE.ISO8859-1', 
   b'nl_be.iso885915': b'nl_BE.ISO8859-15', 
   b'nl_be.iso885915@euro': b'nl_BE.ISO8859-15', 
   b'nl_be.utf8@euro': b'nl_BE.UTF-8', 
   b'nl_be@euro': b'nl_BE.ISO8859-15', 
   b'nl_nl': b'nl_NL.ISO8859-1', 
   b'nl_nl.88591': b'nl_NL.ISO8859-1', 
   b'nl_nl.iso88591': b'nl_NL.ISO8859-1', 
   b'nl_nl.iso885915': b'nl_NL.ISO8859-15', 
   b'nl_nl.iso885915@euro': b'nl_NL.ISO8859-15', 
   b'nl_nl.utf8@euro': b'nl_NL.UTF-8', 
   b'nl_nl@euro': b'nl_NL.ISO8859-15', 
   b'nn': b'nn_NO.ISO8859-1', 
   b'nn_no': b'nn_NO.ISO8859-1', 
   b'nn_no.88591': b'nn_NO.ISO8859-1', 
   b'nn_no.iso88591': b'nn_NO.ISO8859-1', 
   b'nn_no.iso885915': b'nn_NO.ISO8859-15', 
   b'nn_no@euro': b'nn_NO.ISO8859-15', 
   b'no': b'no_NO.ISO8859-1', 
   b'no@nynorsk': b'ny_NO.ISO8859-1', 
   b'no_no': b'no_NO.ISO8859-1', 
   b'no_no.88591': b'no_NO.ISO8859-1', 
   b'no_no.iso88591': b'no_NO.ISO8859-1', 
   b'no_no.iso885915': b'no_NO.ISO8859-15', 
   b'no_no.iso88591@bokmal': b'no_NO.ISO8859-1', 
   b'no_no.iso88591@nynorsk': b'no_NO.ISO8859-1', 
   b'no_no@euro': b'no_NO.ISO8859-15', 
   b'norwegian': b'no_NO.ISO8859-1', 
   b'norwegian.iso88591': b'no_NO.ISO8859-1', 
   b'nr': b'nr_ZA.ISO8859-1', 
   b'nr_za': b'nr_ZA.ISO8859-1', 
   b'nr_za.iso88591': b'nr_ZA.ISO8859-1', 
   b'nso': b'nso_ZA.ISO8859-15', 
   b'nso_za': b'nso_ZA.ISO8859-15', 
   b'nso_za.iso885915': b'nso_ZA.ISO8859-15', 
   b'ny': b'ny_NO.ISO8859-1', 
   b'ny_no': b'ny_NO.ISO8859-1', 
   b'ny_no.88591': b'ny_NO.ISO8859-1', 
   b'ny_no.iso88591': b'ny_NO.ISO8859-1', 
   b'ny_no.iso885915': b'ny_NO.ISO8859-15', 
   b'ny_no@euro': b'ny_NO.ISO8859-15', 
   b'nynorsk': b'nn_NO.ISO8859-1', 
   b'oc': b'oc_FR.ISO8859-1', 
   b'oc_fr': b'oc_FR.ISO8859-1', 
   b'oc_fr.iso88591': b'oc_FR.ISO8859-1', 
   b'oc_fr.iso885915': b'oc_FR.ISO8859-15', 
   b'oc_fr@euro': b'oc_FR.ISO8859-15', 
   b'om_et': b'om_ET.UTF-8', 
   b'om_ke': b'om_KE.ISO8859-1', 
   b'or': b'or_IN.UTF-8', 
   b'or_in': b'or_IN.UTF-8', 
   b'os_ru': b'os_RU.UTF-8', 
   b'pa': b'pa_IN.UTF-8', 
   b'pa_in': b'pa_IN.UTF-8', 
   b'pa_pk': b'pa_PK.UTF-8', 
   b'pap_an': b'pap_AN.UTF-8', 
   b'pap_aw': b'pap_AW.UTF-8', 
   b'pap_cw': b'pap_CW.UTF-8', 
   b'pd': b'pd_US.ISO8859-1', 
   b'pd_de': b'pd_DE.ISO8859-1', 
   b'pd_de.iso88591': b'pd_DE.ISO8859-1', 
   b'pd_de.iso885915': b'pd_DE.ISO8859-15', 
   b'pd_de@euro': b'pd_DE.ISO8859-15', 
   b'pd_us': b'pd_US.ISO8859-1', 
   b'pd_us.iso88591': b'pd_US.ISO8859-1', 
   b'pd_us.iso885915': b'pd_US.ISO8859-15', 
   b'pd_us@euro': b'pd_US.ISO8859-15', 
   b'ph': b'ph_PH.ISO8859-1', 
   b'ph_ph': b'ph_PH.ISO8859-1', 
   b'ph_ph.iso88591': b'ph_PH.ISO8859-1', 
   b'pl': b'pl_PL.ISO8859-2', 
   b'pl_pl': b'pl_PL.ISO8859-2', 
   b'pl_pl.iso88592': b'pl_PL.ISO8859-2', 
   b'polish': b'pl_PL.ISO8859-2', 
   b'portuguese': b'pt_PT.ISO8859-1', 
   b'portuguese.iso88591': b'pt_PT.ISO8859-1', 
   b'portuguese_brazil': b'pt_BR.ISO8859-1', 
   b'portuguese_brazil.8859': b'pt_BR.ISO8859-1', 
   b'posix': b'C', 
   b'posix-utf2': b'C', 
   b'pp': b'pp_AN.ISO8859-1', 
   b'pp_an': b'pp_AN.ISO8859-1', 
   b'pp_an.iso88591': b'pp_AN.ISO8859-1', 
   b'ps_af': b'ps_AF.UTF-8', 
   b'pt': b'pt_PT.ISO8859-1', 
   b'pt.iso885915': b'pt_PT.ISO8859-15', 
   b'pt_br': b'pt_BR.ISO8859-1', 
   b'pt_br.88591': b'pt_BR.ISO8859-1', 
   b'pt_br.iso88591': b'pt_BR.ISO8859-1', 
   b'pt_br.iso885915': b'pt_BR.ISO8859-15', 
   b'pt_br@euro': b'pt_BR.ISO8859-15', 
   b'pt_pt': b'pt_PT.ISO8859-1', 
   b'pt_pt.88591': b'pt_PT.ISO8859-1', 
   b'pt_pt.iso88591': b'pt_PT.ISO8859-1', 
   b'pt_pt.iso885915': b'pt_PT.ISO8859-15', 
   b'pt_pt.iso885915@euro': b'pt_PT.ISO8859-15', 
   b'pt_pt.utf8@euro': b'pt_PT.UTF-8', 
   b'pt_pt@euro': b'pt_PT.ISO8859-15', 
   b'quz_pe': b'quz_PE.UTF-8', 
   b'raj_in': b'raj_IN.UTF-8', 
   b'ro': b'ro_RO.ISO8859-2', 
   b'ro_ro': b'ro_RO.ISO8859-2', 
   b'ro_ro.iso88592': b'ro_RO.ISO8859-2', 
   b'romanian': b'ro_RO.ISO8859-2', 
   b'ru': b'ru_RU.UTF-8', 
   b'ru.koi8r': b'ru_RU.KOI8-R', 
   b'ru_ru': b'ru_RU.UTF-8', 
   b'ru_ru.cp1251': b'ru_RU.CP1251', 
   b'ru_ru.iso88595': b'ru_RU.ISO8859-5', 
   b'ru_ru.koi8r': b'ru_RU.KOI8-R', 
   b'ru_ru.microsoftcp1251': b'ru_RU.CP1251', 
   b'ru_ua': b'ru_UA.KOI8-U', 
   b'ru_ua.cp1251': b'ru_UA.CP1251', 
   b'ru_ua.koi8u': b'ru_UA.KOI8-U', 
   b'ru_ua.microsoftcp1251': b'ru_UA.CP1251', 
   b'rumanian': b'ro_RO.ISO8859-2', 
   b'russian': b'ru_RU.KOI8-R', 
   b'rw': b'rw_RW.ISO8859-1', 
   b'rw_rw': b'rw_RW.ISO8859-1', 
   b'rw_rw.iso88591': b'rw_RW.ISO8859-1', 
   b'sa_in': b'sa_IN.UTF-8', 
   b'sat_in': b'sat_IN.UTF-8', 
   b'sc_it': b'sc_IT.UTF-8', 
   b'sd': b'sd_IN.UTF-8', 
   b'sd@devanagari': b'sd_IN.UTF-8@devanagari', 
   b'sd_in': b'sd_IN.UTF-8', 
   b'sd_in.utf8@devanagari': b'sd_IN.UTF-8@devanagari', 
   b'sd_in@devanagari': b'sd_IN.UTF-8@devanagari', 
   b'sd_in@devanagari.utf8': b'sd_IN.UTF-8@devanagari', 
   b'sd_pk': b'sd_PK.UTF-8', 
   b'se_no': b'se_NO.UTF-8', 
   b'serbocroatian': b'sr_RS.UTF-8@latin', 
   b'sgs_lt': b'sgs_LT.UTF-8', 
   b'sh': b'sr_RS.UTF-8@latin', 
   b'sh_ba.iso88592@bosnia': b'sr_CS.ISO8859-2', 
   b'sh_hr': b'sh_HR.ISO8859-2', 
   b'sh_hr.iso88592': b'hr_HR.ISO8859-2', 
   b'sh_sp': b'sr_CS.ISO8859-2', 
   b'sh_yu': b'sr_RS.UTF-8@latin', 
   b'shn_mm': b'shn_MM.UTF-8', 
   b'shs_ca': b'shs_CA.UTF-8', 
   b'si': b'si_LK.UTF-8', 
   b'si_lk': b'si_LK.UTF-8', 
   b'sid_et': b'sid_ET.UTF-8', 
   b'sinhala': b'si_LK.UTF-8', 
   b'sk': b'sk_SK.ISO8859-2', 
   b'sk_sk': b'sk_SK.ISO8859-2', 
   b'sk_sk.iso88592': b'sk_SK.ISO8859-2', 
   b'sl': b'sl_SI.ISO8859-2', 
   b'sl_cs': b'sl_CS.ISO8859-2', 
   b'sl_si': b'sl_SI.ISO8859-2', 
   b'sl_si.iso88592': b'sl_SI.ISO8859-2', 
   b'slovak': b'sk_SK.ISO8859-2', 
   b'slovene': b'sl_SI.ISO8859-2', 
   b'slovenian': b'sl_SI.ISO8859-2', 
   b'sm_ws': b'sm_WS.UTF-8', 
   b'so_dj': b'so_DJ.ISO8859-1', 
   b'so_et': b'so_ET.UTF-8', 
   b'so_ke': b'so_KE.ISO8859-1', 
   b'so_so': b'so_SO.ISO8859-1', 
   b'sp': b'sr_CS.ISO8859-5', 
   b'sp_yu': b'sr_CS.ISO8859-5', 
   b'spanish': b'es_ES.ISO8859-1', 
   b'spanish.iso88591': b'es_ES.ISO8859-1', 
   b'spanish_spain': b'es_ES.ISO8859-1', 
   b'spanish_spain.8859': b'es_ES.ISO8859-1', 
   b'sq': b'sq_AL.ISO8859-2', 
   b'sq_al': b'sq_AL.ISO8859-2', 
   b'sq_al.iso88592': b'sq_AL.ISO8859-2', 
   b'sq_mk': b'sq_MK.UTF-8', 
   b'sr': b'sr_RS.UTF-8', 
   b'sr@cyrillic': b'sr_RS.UTF-8', 
   b'sr@latin': b'sr_RS.UTF-8@latin', 
   b'sr@latn': b'sr_CS.UTF-8@latin', 
   b'sr_cs': b'sr_CS.UTF-8', 
   b'sr_cs.iso88592': b'sr_CS.ISO8859-2', 
   b'sr_cs.iso88592@latn': b'sr_CS.ISO8859-2', 
   b'sr_cs.iso88595': b'sr_CS.ISO8859-5', 
   b'sr_cs.utf8@latn': b'sr_CS.UTF-8@latin', 
   b'sr_cs@latn': b'sr_CS.UTF-8@latin', 
   b'sr_me': b'sr_ME.UTF-8', 
   b'sr_rs': b'sr_RS.UTF-8', 
   b'sr_rs.utf8@latn': b'sr_RS.UTF-8@latin', 
   b'sr_rs@latin': b'sr_RS.UTF-8@latin', 
   b'sr_rs@latn': b'sr_RS.UTF-8@latin', 
   b'sr_sp': b'sr_CS.ISO8859-2', 
   b'sr_yu': b'sr_RS.UTF-8@latin', 
   b'sr_yu.cp1251@cyrillic': b'sr_CS.CP1251', 
   b'sr_yu.iso88592': b'sr_CS.ISO8859-2', 
   b'sr_yu.iso88595': b'sr_CS.ISO8859-5', 
   b'sr_yu.iso88595@cyrillic': b'sr_CS.ISO8859-5', 
   b'sr_yu.microsoftcp1251@cyrillic': b'sr_CS.CP1251', 
   b'sr_yu.utf8': b'sr_RS.UTF-8', 
   b'sr_yu.utf8@cyrillic': b'sr_RS.UTF-8', 
   b'sr_yu@cyrillic': b'sr_RS.UTF-8', 
   b'ss': b'ss_ZA.ISO8859-1', 
   b'ss_za': b'ss_ZA.ISO8859-1', 
   b'ss_za.iso88591': b'ss_ZA.ISO8859-1', 
   b'st': b'st_ZA.ISO8859-1', 
   b'st_za': b'st_ZA.ISO8859-1', 
   b'st_za.iso88591': b'st_ZA.ISO8859-1', 
   b'sv': b'sv_SE.ISO8859-1', 
   b'sv.iso885915': b'sv_SE.ISO8859-15', 
   b'sv_fi': b'sv_FI.ISO8859-1', 
   b'sv_fi.iso88591': b'sv_FI.ISO8859-1', 
   b'sv_fi.iso885915': b'sv_FI.ISO8859-15', 
   b'sv_fi.iso885915@euro': b'sv_FI.ISO8859-15', 
   b'sv_fi.utf8@euro': b'sv_FI.UTF-8', 
   b'sv_fi@euro': b'sv_FI.ISO8859-15', 
   b'sv_se': b'sv_SE.ISO8859-1', 
   b'sv_se.88591': b'sv_SE.ISO8859-1', 
   b'sv_se.iso88591': b'sv_SE.ISO8859-1', 
   b'sv_se.iso885915': b'sv_SE.ISO8859-15', 
   b'sv_se@euro': b'sv_SE.ISO8859-15', 
   b'sw_ke': b'sw_KE.UTF-8', 
   b'sw_tz': b'sw_TZ.UTF-8', 
   b'swedish': b'sv_SE.ISO8859-1', 
   b'swedish.iso88591': b'sv_SE.ISO8859-1', 
   b'szl_pl': b'szl_PL.UTF-8', 
   b'ta': b'ta_IN.TSCII-0', 
   b'ta_in': b'ta_IN.TSCII-0', 
   b'ta_in.tscii': b'ta_IN.TSCII-0', 
   b'ta_in.tscii0': b'ta_IN.TSCII-0', 
   b'ta_lk': b'ta_LK.UTF-8', 
   b'tcy_in.utf8': b'tcy_IN.UTF-8', 
   b'te': b'te_IN.UTF-8', 
   b'te_in': b'te_IN.UTF-8', 
   b'tg': b'tg_TJ.KOI8-C', 
   b'tg_tj': b'tg_TJ.KOI8-C', 
   b'tg_tj.koi8c': b'tg_TJ.KOI8-C', 
   b'th': b'th_TH.ISO8859-11', 
   b'th_th': b'th_TH.ISO8859-11', 
   b'th_th.iso885911': b'th_TH.ISO8859-11', 
   b'th_th.tactis': b'th_TH.TIS620', 
   b'th_th.tis620': b'th_TH.TIS620', 
   b'thai': b'th_TH.ISO8859-11', 
   b'the_np': b'the_NP.UTF-8', 
   b'ti_er': b'ti_ER.UTF-8', 
   b'ti_et': b'ti_ET.UTF-8', 
   b'tig_er': b'tig_ER.UTF-8', 
   b'tk_tm': b'tk_TM.UTF-8', 
   b'tl': b'tl_PH.ISO8859-1', 
   b'tl_ph': b'tl_PH.ISO8859-1', 
   b'tl_ph.iso88591': b'tl_PH.ISO8859-1', 
   b'tn': b'tn_ZA.ISO8859-15', 
   b'tn_za': b'tn_ZA.ISO8859-15', 
   b'tn_za.iso885915': b'tn_ZA.ISO8859-15', 
   b'to_to': b'to_TO.UTF-8', 
   b'tpi_pg': b'tpi_PG.UTF-8', 
   b'tr': b'tr_TR.ISO8859-9', 
   b'tr_cy': b'tr_CY.ISO8859-9', 
   b'tr_tr': b'tr_TR.ISO8859-9', 
   b'tr_tr.iso88599': b'tr_TR.ISO8859-9', 
   b'ts': b'ts_ZA.ISO8859-1', 
   b'ts_za': b'ts_ZA.ISO8859-1', 
   b'ts_za.iso88591': b'ts_ZA.ISO8859-1', 
   b'tt': b'tt_RU.TATAR-CYR', 
   b'tt_ru': b'tt_RU.TATAR-CYR', 
   b'tt_ru.koi8c': b'tt_RU.KOI8-C', 
   b'tt_ru.tatarcyr': b'tt_RU.TATAR-CYR', 
   b'tt_ru@iqtelif': b'tt_RU.UTF-8@iqtelif', 
   b'turkish': b'tr_TR.ISO8859-9', 
   b'turkish.iso88599': b'tr_TR.ISO8859-9', 
   b'ug_cn': b'ug_CN.UTF-8', 
   b'uk': b'uk_UA.KOI8-U', 
   b'uk_ua': b'uk_UA.KOI8-U', 
   b'uk_ua.cp1251': b'uk_UA.CP1251', 
   b'uk_ua.iso88595': b'uk_UA.ISO8859-5', 
   b'uk_ua.koi8u': b'uk_UA.KOI8-U', 
   b'uk_ua.microsoftcp1251': b'uk_UA.CP1251', 
   b'univ': b'en_US.utf', 
   b'universal': b'en_US.utf', 
   b'universal.utf8@ucs4': b'en_US.UTF-8', 
   b'unm_us': b'unm_US.UTF-8', 
   b'ur': b'ur_PK.CP1256', 
   b'ur_in': b'ur_IN.UTF-8', 
   b'ur_pk': b'ur_PK.CP1256', 
   b'ur_pk.cp1256': b'ur_PK.CP1256', 
   b'ur_pk.microsoftcp1256': b'ur_PK.CP1256', 
   b'uz': b'uz_UZ.UTF-8', 
   b'uz_uz': b'uz_UZ.UTF-8', 
   b'uz_uz.iso88591': b'uz_UZ.ISO8859-1', 
   b'uz_uz.utf8@cyrillic': b'uz_UZ.UTF-8', 
   b'uz_uz@cyrillic': b'uz_UZ.UTF-8', 
   b've': b've_ZA.UTF-8', 
   b've_za': b've_ZA.UTF-8', 
   b'vi': b'vi_VN.TCVN', 
   b'vi_vn': b'vi_VN.TCVN', 
   b'vi_vn.tcvn': b'vi_VN.TCVN', 
   b'vi_vn.tcvn5712': b'vi_VN.TCVN', 
   b'vi_vn.viscii': b'vi_VN.VISCII', 
   b'vi_vn.viscii111': b'vi_VN.VISCII', 
   b'wa': b'wa_BE.ISO8859-1', 
   b'wa_be': b'wa_BE.ISO8859-1', 
   b'wa_be.iso88591': b'wa_BE.ISO8859-1', 
   b'wa_be.iso885915': b'wa_BE.ISO8859-15', 
   b'wa_be.iso885915@euro': b'wa_BE.ISO8859-15', 
   b'wa_be@euro': b'wa_BE.ISO8859-15', 
   b'wae_ch': b'wae_CH.UTF-8', 
   b'wal_et': b'wal_ET.UTF-8', 
   b'wo_sn': b'wo_SN.UTF-8', 
   b'xh': b'xh_ZA.ISO8859-1', 
   b'xh_za': b'xh_ZA.ISO8859-1', 
   b'xh_za.iso88591': b'xh_ZA.ISO8859-1', 
   b'yi': b'yi_US.CP1255', 
   b'yi_us': b'yi_US.CP1255', 
   b'yi_us.cp1255': b'yi_US.CP1255', 
   b'yi_us.microsoftcp1255': b'yi_US.CP1255', 
   b'yo_ng': b'yo_NG.UTF-8', 
   b'yue_hk': b'yue_HK.UTF-8', 
   b'yuw_pg': b'yuw_PG.UTF-8', 
   b'zh': b'zh_CN.eucCN', 
   b'zh_cn': b'zh_CN.gb2312', 
   b'zh_cn.big5': b'zh_TW.big5', 
   b'zh_cn.euc': b'zh_CN.eucCN', 
   b'zh_cn.gb18030': b'zh_CN.gb18030', 
   b'zh_cn.gb2312': b'zh_CN.gb2312', 
   b'zh_cn.gbk': b'zh_CN.gbk', 
   b'zh_hk': b'zh_HK.big5hkscs', 
   b'zh_hk.big5': b'zh_HK.big5', 
   b'zh_hk.big5hk': b'zh_HK.big5hkscs', 
   b'zh_hk.big5hkscs': b'zh_HK.big5hkscs', 
   b'zh_sg': b'zh_SG.GB2312', 
   b'zh_sg.gbk': b'zh_SG.GBK', 
   b'zh_tw': b'zh_TW.big5', 
   b'zh_tw.big5': b'zh_TW.big5', 
   b'zh_tw.euc': b'zh_TW.eucTW', 
   b'zh_tw.euctw': b'zh_TW.eucTW', 
   b'zu': b'zu_ZA.ISO8859-1', 
   b'zu_za': b'zu_ZA.ISO8859-1', 
   b'zu_za.iso88591': b'zu_ZA.ISO8859-1'}
windows_locale = {1078: b'af_ZA', 
   1052: b'sq_AL', 
   1156: b'gsw_FR', 
   1118: b'am_ET', 
   1025: b'ar_SA', 
   2049: b'ar_IQ', 
   3073: b'ar_EG', 
   4097: b'ar_LY', 
   5121: b'ar_DZ', 
   6145: b'ar_MA', 
   7169: b'ar_TN', 
   8193: b'ar_OM', 
   9217: b'ar_YE', 
   10241: b'ar_SY', 
   11265: b'ar_JO', 
   12289: b'ar_LB', 
   13313: b'ar_KW', 
   14337: b'ar_AE', 
   15361: b'ar_BH', 
   16385: b'ar_QA', 
   1067: b'hy_AM', 
   1101: b'as_IN', 
   1068: b'az_AZ', 
   2092: b'az_AZ', 
   1133: b'ba_RU', 
   1069: b'eu_ES', 
   1059: b'be_BY', 
   1093: b'bn_IN', 
   8218: b'bs_BA', 
   5146: b'bs_BA', 
   1150: b'br_FR', 
   1026: b'bg_BG', 
   1027: b'ca_ES', 
   4: b'zh_CHS', 
   1028: b'zh_TW', 
   2052: b'zh_CN', 
   3076: b'zh_HK', 
   4100: b'zh_SG', 
   5124: b'zh_MO', 
   31748: b'zh_CHT', 
   1155: b'co_FR', 
   1050: b'hr_HR', 
   4122: b'hr_BA', 
   1029: b'cs_CZ', 
   1030: b'da_DK', 
   1164: b'gbz_AF', 
   1125: b'div_MV', 
   1043: b'nl_NL', 
   2067: b'nl_BE', 
   1033: b'en_US', 
   2057: b'en_GB', 
   3081: b'en_AU', 
   4105: b'en_CA', 
   5129: b'en_NZ', 
   6153: b'en_IE', 
   7177: b'en_ZA', 
   8201: b'en_JA', 
   9225: b'en_CB', 
   10249: b'en_BZ', 
   11273: b'en_TT', 
   12297: b'en_ZW', 
   13321: b'en_PH', 
   16393: b'en_IN', 
   17417: b'en_MY', 
   18441: b'en_IN', 
   1061: b'et_EE', 
   1080: b'fo_FO', 
   1124: b'fil_PH', 
   1035: b'fi_FI', 
   1036: b'fr_FR', 
   2060: b'fr_BE', 
   3084: b'fr_CA', 
   4108: b'fr_CH', 
   5132: b'fr_LU', 
   6156: b'fr_MC', 
   1122: b'fy_NL', 
   1110: b'gl_ES', 
   1079: b'ka_GE', 
   1031: b'de_DE', 
   2055: b'de_CH', 
   3079: b'de_AT', 
   4103: b'de_LU', 
   5127: b'de_LI', 
   1032: b'el_GR', 
   1135: b'kl_GL', 
   1095: b'gu_IN', 
   1128: b'ha_NG', 
   1037: b'he_IL', 
   1081: b'hi_IN', 
   1038: b'hu_HU', 
   1039: b'is_IS', 
   1057: b'id_ID', 
   1117: b'iu_CA', 
   2141: b'iu_CA', 
   2108: b'ga_IE', 
   1040: b'it_IT', 
   2064: b'it_CH', 
   1041: b'ja_JP', 
   1099: b'kn_IN', 
   1087: b'kk_KZ', 
   1107: b'kh_KH', 
   1158: b'qut_GT', 
   1159: b'rw_RW', 
   1111: b'kok_IN', 
   1042: b'ko_KR', 
   1088: b'ky_KG', 
   1108: b'lo_LA', 
   1062: b'lv_LV', 
   1063: b'lt_LT', 
   2094: b'dsb_DE', 
   1134: b'lb_LU', 
   1071: b'mk_MK', 
   1086: b'ms_MY', 
   2110: b'ms_BN', 
   1100: b'ml_IN', 
   1082: b'mt_MT', 
   1153: b'mi_NZ', 
   1146: b'arn_CL', 
   1102: b'mr_IN', 
   1148: b'moh_CA', 
   1104: b'mn_MN', 
   2128: b'mn_CN', 
   1121: b'ne_NP', 
   1044: b'nb_NO', 
   2068: b'nn_NO', 
   1154: b'oc_FR', 
   1096: b'or_IN', 
   1123: b'ps_AF', 
   1065: b'fa_IR', 
   1045: b'pl_PL', 
   1046: b'pt_BR', 
   2070: b'pt_PT', 
   1094: b'pa_IN', 
   1131: b'quz_BO', 
   2155: b'quz_EC', 
   3179: b'quz_PE', 
   1048: b'ro_RO', 
   1047: b'rm_CH', 
   1049: b'ru_RU', 
   9275: b'smn_FI', 
   4155: b'smj_NO', 
   5179: b'smj_SE', 
   1083: b'se_NO', 
   2107: b'se_SE', 
   3131: b'se_FI', 
   8251: b'sms_FI', 
   6203: b'sma_NO', 
   7227: b'sma_SE', 
   1103: b'sa_IN', 
   3098: b'sr_SP', 
   7194: b'sr_BA', 
   2074: b'sr_SP', 
   6170: b'sr_BA', 
   1115: b'si_LK', 
   1132: b'ns_ZA', 
   1074: b'tn_ZA', 
   1051: b'sk_SK', 
   1060: b'sl_SI', 
   1034: b'es_ES', 
   2058: b'es_MX', 
   3082: b'es_ES', 
   4106: b'es_GT', 
   5130: b'es_CR', 
   6154: b'es_PA', 
   7178: b'es_DO', 
   8202: b'es_VE', 
   9226: b'es_CO', 
   10250: b'es_PE', 
   11274: b'es_AR', 
   12298: b'es_EC', 
   13322: b'es_CL', 
   14346: b'es_UR', 
   15370: b'es_PY', 
   16394: b'es_BO', 
   17418: b'es_SV', 
   18442: b'es_HN', 
   19466: b'es_NI', 
   20490: b'es_PR', 
   21514: b'es_US', 
   1089: b'sw_KE', 
   1053: b'sv_SE', 
   2077: b'sv_FI', 
   1114: b'syr_SY', 
   1064: b'tg_TJ', 
   2143: b'tmz_DZ', 
   1097: b'ta_IN', 
   1092: b'tt_RU', 
   1098: b'te_IN', 
   1054: b'th_TH', 
   2129: b'bo_BT', 
   1105: b'bo_CN', 
   1055: b'tr_TR', 
   1090: b'tk_TM', 
   1152: b'ug_CN', 
   1058: b'uk_UA', 
   1070: b'wen_DE', 
   1056: b'ur_PK', 
   2080: b'ur_IN', 
   1091: b'uz_UZ', 
   2115: b'uz_UZ', 
   1066: b'vi_VN', 
   1106: b'cy_GB', 
   1160: b'wo_SN', 
   1076: b'xh_ZA', 
   1157: b'sah_RU', 
   1144: b'ii_CN', 
   1130: b'yo_NG', 
   1077: b'zu_ZA'}

def _print_locale():
    categories = {}

    def _init_categories(categories=categories):
        for k, v in globals().items():
            if k[:3] == b'LC_':
                categories[k] = v

        return

    _init_categories()
    del categories[b'LC_ALL']
    print b'Locale defaults as determined by getdefaultlocale():'
    print b'-' * 72
    lang, enc = getdefaultlocale()
    print b'Language: ', lang or b'(undefined)'
    print b'Encoding: ', enc or b'(undefined)'
    print
    print b'Locale settings on startup:'
    print b'-' * 72
    for name, category in categories.items():
        print name, b'...'
        lang, enc = getlocale(category)
        print b'   Language: ', lang or b'(undefined)'
        print b'   Encoding: ', enc or b'(undefined)'
        print

    print
    print b'Locale settings after calling resetlocale():'
    print b'-' * 72
    resetlocale()
    for name, category in categories.items():
        print name, b'...'
        lang, enc = getlocale(category)
        print b'   Language: ', lang or b'(undefined)'
        print b'   Encoding: ', enc or b'(undefined)'
        print

    try:
        setlocale(LC_ALL, b'')
    except:
        print b'NOTE:'
        print b'setlocale(LC_ALL, "") does not support the default locale'
        print b'given in the OS environment variables.'

    print
    print b'Locale settings after calling setlocale(LC_ALL, ""):'
    print b'-' * 72
    for name, category in categories.items():
        print name, b'...'
        lang, enc = getlocale(category)
        print b'   Language: ', lang or b'(undefined)'
        print b'   Encoding: ', enc or b'(undefined)'
        print

    return


try:
    LC_MESSAGES
except NameError:
    pass
else:
    __all__.append(b'LC_MESSAGES')

if __name__ == b'__main__':
    print b'Locale aliasing:'
    print
    _print_locale()
    print
    print b'Number formatting:'
    print
    _test()
