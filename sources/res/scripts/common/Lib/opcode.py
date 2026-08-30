__all__ = [
 0, 1, 2, 3, 4, 
 5, 6, 7, 8, 9, 
 10, 11]
cmp_op = (b'<', b'<=', b'==', b'!=', b'>', b'>=', b'in', b'not in', b'is', b'is not', b'exception match', b'BAD')
hasconst = []
hasname = []
hasjrel = []
hasjabs = []
haslocal = []
hascompare = []
hasfree = []
opmap = {}
opname = [
 b''] * 256
for op in range(256):
    opname[op] = b'<%r>' % (op,)

del op

def def_op(name, op):
    opname[op] = name
    opmap[name] = op
    return


def name_op(name, op):
    def_op(name, op)
    hasname.append(op)
    return


def jrel_op(name, op):
    def_op(name, op)
    hasjrel.append(op)
    return


def jabs_op(name, op):
    def_op(name, op)
    hasjabs.append(op)
    return


def_op(b'STOP_CODE', 0)
def_op(b'POP_TOP', 1)
def_op(b'ROT_TWO', 2)
def_op(b'ROT_THREE', 3)
def_op(b'DUP_TOP', 4)
def_op(b'ROT_FOUR', 5)
def_op(b'NOP', 9)
def_op(b'UNARY_POSITIVE', 10)
def_op(b'UNARY_NEGATIVE', 11)
def_op(b'UNARY_NOT', 12)
def_op(b'UNARY_CONVERT', 13)
def_op(b'UNARY_INVERT', 15)
def_op(b'BINARY_POWER', 19)
def_op(b'BINARY_MULTIPLY', 20)
def_op(b'BINARY_DIVIDE', 21)
def_op(b'BINARY_MODULO', 22)
def_op(b'BINARY_ADD', 23)
def_op(b'BINARY_SUBTRACT', 24)
def_op(b'BINARY_SUBSCR', 25)
def_op(b'BINARY_FLOOR_DIVIDE', 26)
def_op(b'BINARY_TRUE_DIVIDE', 27)
def_op(b'INPLACE_FLOOR_DIVIDE', 28)
def_op(b'INPLACE_TRUE_DIVIDE', 29)
def_op(b'SLICE+0', 30)
def_op(b'SLICE+1', 31)
def_op(b'SLICE+2', 32)
def_op(b'SLICE+3', 33)
def_op(b'STORE_SLICE+0', 40)
def_op(b'STORE_SLICE+1', 41)
def_op(b'STORE_SLICE+2', 42)
def_op(b'STORE_SLICE+3', 43)
def_op(b'DELETE_SLICE+0', 50)
def_op(b'DELETE_SLICE+1', 51)
def_op(b'DELETE_SLICE+2', 52)
def_op(b'DELETE_SLICE+3', 53)
def_op(b'STORE_MAP', 54)
def_op(b'INPLACE_ADD', 55)
def_op(b'INPLACE_SUBTRACT', 56)
def_op(b'INPLACE_MULTIPLY', 57)
def_op(b'INPLACE_DIVIDE', 58)
def_op(b'INPLACE_MODULO', 59)
def_op(b'STORE_SUBSCR', 60)
def_op(b'DELETE_SUBSCR', 61)
def_op(b'BINARY_LSHIFT', 62)
def_op(b'BINARY_RSHIFT', 63)
def_op(b'BINARY_AND', 64)
def_op(b'BINARY_XOR', 65)
def_op(b'BINARY_OR', 66)
def_op(b'INPLACE_POWER', 67)
def_op(b'GET_ITER', 68)
def_op(b'PRINT_EXPR', 70)
def_op(b'PRINT_ITEM', 71)
def_op(b'PRINT_NEWLINE', 72)
def_op(b'PRINT_ITEM_TO', 73)
def_op(b'PRINT_NEWLINE_TO', 74)
def_op(b'INPLACE_LSHIFT', 75)
def_op(b'INPLACE_RSHIFT', 76)
def_op(b'INPLACE_AND', 77)
def_op(b'INPLACE_XOR', 78)
def_op(b'INPLACE_OR', 79)
def_op(b'BREAK_LOOP', 80)
def_op(b'WITH_CLEANUP', 81)
def_op(b'LOAD_LOCALS', 82)
def_op(b'RETURN_VALUE', 83)
def_op(b'IMPORT_STAR', 84)
def_op(b'EXEC_STMT', 85)
def_op(b'YIELD_VALUE', 86)
def_op(b'POP_BLOCK', 87)
def_op(b'END_FINALLY', 88)
def_op(b'BUILD_CLASS', 89)
HAVE_ARGUMENT = 90
name_op(b'STORE_NAME', 90)
name_op(b'DELETE_NAME', 91)
def_op(b'UNPACK_SEQUENCE', 92)
jrel_op(b'FOR_ITER', 93)
def_op(b'LIST_APPEND', 94)
name_op(b'STORE_ATTR', 95)
name_op(b'DELETE_ATTR', 96)
name_op(b'STORE_GLOBAL', 97)
name_op(b'DELETE_GLOBAL', 98)
def_op(b'DUP_TOPX', 99)
def_op(b'LOAD_CONST', 100)
hasconst.append(100)
name_op(b'LOAD_NAME', 101)
def_op(b'BUILD_TUPLE', 102)
def_op(b'BUILD_LIST', 103)
def_op(b'BUILD_SET', 104)
def_op(b'BUILD_MAP', 105)
name_op(b'LOAD_ATTR', 106)
def_op(b'COMPARE_OP', 107)
hascompare.append(107)
name_op(b'IMPORT_NAME', 108)
name_op(b'IMPORT_FROM', 109)
jrel_op(b'JUMP_FORWARD', 110)
jabs_op(b'JUMP_IF_FALSE_OR_POP', 111)
jabs_op(b'JUMP_IF_TRUE_OR_POP', 112)
jabs_op(b'JUMP_ABSOLUTE', 113)
jabs_op(b'POP_JUMP_IF_FALSE', 114)
jabs_op(b'POP_JUMP_IF_TRUE', 115)
name_op(b'LOAD_GLOBAL', 116)
jabs_op(b'CONTINUE_LOOP', 119)
jrel_op(b'SETUP_LOOP', 120)
jrel_op(b'SETUP_EXCEPT', 121)
jrel_op(b'SETUP_FINALLY', 122)
def_op(b'LOAD_FAST', 124)
haslocal.append(124)
def_op(b'STORE_FAST', 125)
haslocal.append(125)
def_op(b'DELETE_FAST', 126)
haslocal.append(126)
def_op(b'RAISE_VARARGS', 130)
def_op(b'CALL_FUNCTION', 131)
def_op(b'MAKE_FUNCTION', 132)
def_op(b'BUILD_SLICE', 133)
def_op(b'MAKE_CLOSURE', 134)
def_op(b'LOAD_CLOSURE', 135)
hasfree.append(135)
def_op(b'LOAD_DEREF', 136)
hasfree.append(136)
def_op(b'STORE_DEREF', 137)
hasfree.append(137)
def_op(b'CALL_FUNCTION_VAR', 140)
def_op(b'CALL_FUNCTION_KW', 141)
def_op(b'CALL_FUNCTION_VAR_KW', 142)
jrel_op(b'SETUP_WITH', 143)
def_op(b'EXTENDED_ARG', 145)
EXTENDED_ARG = 145
def_op(b'SET_ADD', 146)
def_op(b'MAP_ADD', 147)
del def_op
del name_op
del jrel_op
del jabs_op
