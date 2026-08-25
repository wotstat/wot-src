MAGIC = 20031017
try:
    from _sre import MAXREPEAT
except ImportError:
    import _sre
    MAXREPEAT = _sre.MAXREPEAT = 65535

class error(Exception):
    pass


FAILURE = b'failure'
SUCCESS = b'success'
ANY = b'any'
ANY_ALL = b'any_all'
ASSERT = b'assert'
ASSERT_NOT = b'assert_not'
AT = b'at'
BIGCHARSET = b'bigcharset'
BRANCH = b'branch'
CALL = b'call'
CATEGORY = b'category'
CHARSET = b'charset'
GROUPREF = b'groupref'
GROUPREF_IGNORE = b'groupref_ignore'
GROUPREF_EXISTS = b'groupref_exists'
IN = b'in'
IN_IGNORE = b'in_ignore'
INFO = b'info'
JUMP = b'jump'
LITERAL = b'literal'
LITERAL_IGNORE = b'literal_ignore'
MARK = b'mark'
MAX_REPEAT = b'max_repeat'
MAX_UNTIL = b'max_until'
MIN_REPEAT = b'min_repeat'
MIN_UNTIL = b'min_until'
NEGATE = b'negate'
NOT_LITERAL = b'not_literal'
NOT_LITERAL_IGNORE = b'not_literal_ignore'
RANGE = b'range'
REPEAT = b'repeat'
REPEAT_ONE = b'repeat_one'
SUBPATTERN = b'subpattern'
MIN_REPEAT_ONE = b'min_repeat_one'
AT_BEGINNING = b'at_beginning'
AT_BEGINNING_LINE = b'at_beginning_line'
AT_BEGINNING_STRING = b'at_beginning_string'
AT_BOUNDARY = b'at_boundary'
AT_NON_BOUNDARY = b'at_non_boundary'
AT_END = b'at_end'
AT_END_LINE = b'at_end_line'
AT_END_STRING = b'at_end_string'
AT_LOC_BOUNDARY = b'at_loc_boundary'
AT_LOC_NON_BOUNDARY = b'at_loc_non_boundary'
AT_UNI_BOUNDARY = b'at_uni_boundary'
AT_UNI_NON_BOUNDARY = b'at_uni_non_boundary'
CATEGORY_DIGIT = b'category_digit'
CATEGORY_NOT_DIGIT = b'category_not_digit'
CATEGORY_SPACE = b'category_space'
CATEGORY_NOT_SPACE = b'category_not_space'
CATEGORY_WORD = b'category_word'
CATEGORY_NOT_WORD = b'category_not_word'
CATEGORY_LINEBREAK = b'category_linebreak'
CATEGORY_NOT_LINEBREAK = b'category_not_linebreak'
CATEGORY_LOC_WORD = b'category_loc_word'
CATEGORY_LOC_NOT_WORD = b'category_loc_not_word'
CATEGORY_UNI_DIGIT = b'category_uni_digit'
CATEGORY_UNI_NOT_DIGIT = b'category_uni_not_digit'
CATEGORY_UNI_SPACE = b'category_uni_space'
CATEGORY_UNI_NOT_SPACE = b'category_uni_not_space'
CATEGORY_UNI_WORD = b'category_uni_word'
CATEGORY_UNI_NOT_WORD = b'category_uni_not_word'
CATEGORY_UNI_LINEBREAK = b'category_uni_linebreak'
CATEGORY_UNI_NOT_LINEBREAK = b'category_uni_not_linebreak'
OPCODES = [
 FAILURE, SUCCESS, 
 ANY, ANY_ALL, 
 ASSERT, ASSERT_NOT, 
 AT, 
 BRANCH, 
 CALL, 
 CATEGORY, 
 CHARSET, 
 BIGCHARSET, 
 GROUPREF, GROUPREF_EXISTS, GROUPREF_IGNORE, 
 IN, IN_IGNORE, 
 INFO, 
 JUMP, 
 LITERAL, 
 LITERAL_IGNORE, 
 MARK, 
 MAX_UNTIL, 
 MIN_UNTIL, 
 NOT_LITERAL, NOT_LITERAL_IGNORE, 
 NEGATE, 
 RANGE, 
 REPEAT, 
 REPEAT_ONE, 
 SUBPATTERN, 
 MIN_REPEAT_ONE]
ATCODES = [
 AT_BEGINNING, AT_BEGINNING_LINE, AT_BEGINNING_STRING, AT_BOUNDARY, 
 AT_NON_BOUNDARY, 
 AT_END, AT_END_LINE, AT_END_STRING, 
 AT_LOC_BOUNDARY, AT_LOC_NON_BOUNDARY, 
 AT_UNI_BOUNDARY, 
 AT_UNI_NON_BOUNDARY]
CHCODES = [
 CATEGORY_DIGIT, CATEGORY_NOT_DIGIT, CATEGORY_SPACE, 
 CATEGORY_NOT_SPACE, 
 CATEGORY_WORD, CATEGORY_NOT_WORD, 
 CATEGORY_LINEBREAK, CATEGORY_NOT_LINEBREAK, 
 CATEGORY_LOC_WORD, 
 CATEGORY_LOC_NOT_WORD, CATEGORY_UNI_DIGIT, CATEGORY_UNI_NOT_DIGIT, 
 CATEGORY_UNI_SPACE, 
 CATEGORY_UNI_NOT_SPACE, CATEGORY_UNI_WORD, 
 CATEGORY_UNI_NOT_WORD, CATEGORY_UNI_LINEBREAK, 
 CATEGORY_UNI_NOT_LINEBREAK]

def makedict(list):
    d = {}
    i = 0
    for item in list:
        d[item] = i
        i = i + 1

    return d


OPCODES = makedict(OPCODES)
ATCODES = makedict(ATCODES)
CHCODES = makedict(CHCODES)
OP_IGNORE = {GROUPREF: GROUPREF_IGNORE, 
   IN: IN_IGNORE, 
   LITERAL: LITERAL_IGNORE, 
   NOT_LITERAL: NOT_LITERAL_IGNORE}
AT_MULTILINE = {AT_BEGINNING: AT_BEGINNING_LINE, 
   AT_END: AT_END_LINE}
AT_LOCALE = {AT_BOUNDARY: AT_LOC_BOUNDARY, 
   AT_NON_BOUNDARY: AT_LOC_NON_BOUNDARY}
AT_UNICODE = {AT_BOUNDARY: AT_UNI_BOUNDARY, 
   AT_NON_BOUNDARY: AT_UNI_NON_BOUNDARY}
CH_LOCALE = {CATEGORY_DIGIT: CATEGORY_DIGIT, 
   CATEGORY_NOT_DIGIT: CATEGORY_NOT_DIGIT, 
   CATEGORY_SPACE: CATEGORY_SPACE, 
   CATEGORY_NOT_SPACE: CATEGORY_NOT_SPACE, 
   CATEGORY_WORD: CATEGORY_LOC_WORD, 
   CATEGORY_NOT_WORD: CATEGORY_LOC_NOT_WORD, 
   CATEGORY_LINEBREAK: CATEGORY_LINEBREAK, 
   CATEGORY_NOT_LINEBREAK: CATEGORY_NOT_LINEBREAK}
CH_UNICODE = {CATEGORY_DIGIT: CATEGORY_UNI_DIGIT, 
   CATEGORY_NOT_DIGIT: CATEGORY_UNI_NOT_DIGIT, 
   CATEGORY_SPACE: CATEGORY_UNI_SPACE, 
   CATEGORY_NOT_SPACE: CATEGORY_UNI_NOT_SPACE, 
   CATEGORY_WORD: CATEGORY_UNI_WORD, 
   CATEGORY_NOT_WORD: CATEGORY_UNI_NOT_WORD, 
   CATEGORY_LINEBREAK: CATEGORY_UNI_LINEBREAK, 
   CATEGORY_NOT_LINEBREAK: CATEGORY_UNI_NOT_LINEBREAK}
SRE_FLAG_TEMPLATE = 1
SRE_FLAG_IGNORECASE = 2
SRE_FLAG_LOCALE = 4
SRE_FLAG_MULTILINE = 8
SRE_FLAG_DOTALL = 16
SRE_FLAG_UNICODE = 32
SRE_FLAG_VERBOSE = 64
SRE_FLAG_DEBUG = 128
SRE_INFO_PREFIX = 1
SRE_INFO_LITERAL = 2
SRE_INFO_CHARSET = 4
if __name__ == b'__main__':

    def dump(f, d, prefix):
        items = d.items()
        items.sort(key=(lambda a: a[1]))
        for k, v in items:
            f.write(b'#define %s_%s %s\n' % (prefix, k.upper(), v))

        return


    f = open(b'sre_constants.h', b'w')
    f.write(b"/*\n * Secret Labs' Regular Expression Engine\n *\n * regular expression matching engine\n *\n * NOTE: This file is generated by sre_constants.py.  If you need\n * to change anything in here, edit sre_constants.py and run it.\n *\n * Copyright (c) 1997-2001 by Secret Labs AB.  All rights reserved.\n *\n * See the _sre.c file for information on usage and redistribution.\n */\n\n")
    f.write(b'#define SRE_MAGIC %d\n' % MAGIC)
    dump(f, OPCODES, b'SRE_OP')
    dump(f, ATCODES, b'SRE')
    dump(f, CHCODES, b'SRE')
    f.write(b'#define SRE_FLAG_TEMPLATE %d\n' % SRE_FLAG_TEMPLATE)
    f.write(b'#define SRE_FLAG_IGNORECASE %d\n' % SRE_FLAG_IGNORECASE)
    f.write(b'#define SRE_FLAG_LOCALE %d\n' % SRE_FLAG_LOCALE)
    f.write(b'#define SRE_FLAG_MULTILINE %d\n' % SRE_FLAG_MULTILINE)
    f.write(b'#define SRE_FLAG_DOTALL %d\n' % SRE_FLAG_DOTALL)
    f.write(b'#define SRE_FLAG_UNICODE %d\n' % SRE_FLAG_UNICODE)
    f.write(b'#define SRE_FLAG_VERBOSE %d\n' % SRE_FLAG_VERBOSE)
    f.write(b'#define SRE_INFO_PREFIX %d\n' % SRE_INFO_PREFIX)
    f.write(b'#define SRE_INFO_LITERAL %d\n' % SRE_INFO_LITERAL)
    f.write(b'#define SRE_INFO_CHARSET %d\n' % SRE_INFO_CHARSET)
    f.close()
    print b'done'
