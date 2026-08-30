import stringprep, types, unicodedata
from soft_exception import SoftException

class XmppStringPrepError(SoftException):
    pass


def doMappingToNothing(char):
    if stringprep.in_table_b1(char):
        return u''
    return char


def doMappingSpaceChars(char):
    if stringprep.in_table_c12(char):
        return u' '
    return char


def normalizeToNFKC(data):
    return unicodedata.normalize(b'NFKC', data)


def normalizeToNFC(data):
    return unicodedata.normalize(b'NFC', data)


_NODE_PREP_PROHIBITED = {
 9, 10, 11, 12, 13, 14, 15, 16}

def inNodeProhibitedChars(char):
    return char in _NODE_PREP_PROHIBITED


def _isCharProhibited(table, char):
    if table(char):
        raise XmppStringPrepError((b'There is prohibited character: {0!r}').format(char))
    return


def _isCharUnassigned(table, char):
    if table(char):
        raise XmppStringPrepError((b'There is unassigned character: {0!r}').format(char))
    return


class _StringPrepProfile(object):
    __slots__ = (b'_unassigned', b'_mapping', b'_normalization', b'_prohibited', b'_bidi')

    def __init__(self, mapping=None, unassigned=None, normalization=None, prohibited=None, bidi=True):
        self._unassigned = unassigned or []
        self._mapping = mapping or []
        self._normalization = normalization
        self._prohibited = prohibited or []
        self._bidi = bidi
        return

    def prepare(self, data):
        if not isinstance(data, types.UnicodeType):
            data = unicode(data, b'utf8')
        result = self._doMapping(data)
        result = self._doNormalization(result)
        result = self._checkProhibited(result)
        result = self._checkUnassigned(result)
        return result

    def _doMapping(self, data):
        result = data
        for table in self._mapping:
            result = map(table, data)

        return (u'').join(result)

    def _doNormalization(self, data):
        result = data
        if self._normalization and callable(self._normalization):
            result = self._normalization(result)
        return result

    def _checkProhibited(self, data):
        for item in self._prohibited:
            map((lambda char, table=item: _isCharProhibited(table, char)), data)

        return data

    def _checkUnassigned(self, data):
        for item in self._unassigned:
            map((lambda char, table=item: _isCharUnassigned(table, char)), data)

        return data

    def _checkBidi(self, data):
        hasL = False
        hasRorAL = False
        for char in data:
            if stringprep.in_table_d1(char):
                hasRorAL = True
            elif stringprep.in_table_d2(char):
                hasL = True

        if hasL and hasRorAL:
            raise XmppStringPrepError(b'String contains RandALCat characters and LCat characters')
        if hasRorAL and (not stringprep.in_table_d1(data[0]) or not stringprep.in_table_d1(data[-1])):
            raise XmppStringPrepError(b'RandALCat character MUST be the first character of the string, and a RandALCat character MUST be the last character of the string')
        return data


NodePrep = _StringPrepProfile(unassigned=(
 stringprep.in_table_a1,), mapping=(
 doMappingToNothing, stringprep.map_table_b2), normalization=normalizeToNFKC, prohibited=(
 stringprep.in_table_c11, stringprep.in_table_c12,
 stringprep.in_table_c21, stringprep.in_table_c22,
 stringprep.in_table_c3, stringprep.in_table_c4,
 stringprep.in_table_c5, stringprep.in_table_c6,
 stringprep.in_table_c7, stringprep.in_table_c8,
 stringprep.in_table_c9, inNodeProhibitedChars), bidi=True)
ResourcePrep = _StringPrepProfile(unassigned=(
 stringprep.in_table_a1,), mapping=(
 doMappingToNothing,), normalization=normalizeToNFC, prohibited=(
 stringprep.in_table_c12, stringprep.in_table_c21,
 stringprep.in_table_c22, stringprep.in_table_c3,
 stringprep.in_table_c4, stringprep.in_table_c5,
 stringprep.in_table_c6, stringprep.in_table_c7,
 stringprep.in_table_c8, stringprep.in_table_c9), bidi=True)
