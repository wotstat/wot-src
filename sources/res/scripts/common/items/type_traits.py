import Math
from typing import *

def allowEqualNone(eq):

    def wrap(lhs, rhs, *args):
        if lhs is None or rhs is None:
            return lhs == rhs
        else:
            return eq(lhs, rhs, *args)

    return wrap


def equal(lhs, rhs):
    return lhs == rhs


@allowEqualNone
def equalFloat(lhs, rhs):
    return abs(lhs - rhs) < 1e-05


@allowEqualNone
def equalString(lhs, rhs):
    return lhs.lower() == rhs.lower()


@allowEqualNone
def equalVector2(lhs, rhs):
    for i in range(2):
        if not equalFloat(lhs[i], rhs[i]):
            return False

    return True


@allowEqualNone
def equalVector3(lhs, rhs):
    for i in range(3):
        if not equalFloat(lhs[i], rhs[i]):
            return False

    return True


@allowEqualNone
def equalVector4(lhs, rhs):
    for i in range(4):
        if not equalFloat(lhs[i], rhs[i]):
            return False

    return True


@allowEqualNone
def equalMatrix(lhs, rhs):
    for x in range(4):
        for y in range(4):
            if not equalFloat(lhs.get(x, y), rhs.get(x, y)):
                return False

    return True


@allowEqualNone
def equalSeq(lhs, rhs, eq=equal):
    if len(lhs) != len(rhs):
        return False
    for l, r in zip(lhs, rhs):
        if not eq(l, r):
            return False

    return True


EQUAL_COMPARATORS = {b'Float': equalFloat, 
   b'String': equalString, 
   b'Vector2': equalVector2, 
   b'Vector3': equalVector3, 
   b'Vector4': equalVector4, 
   b'Matrix': equalMatrix, 
   b'Strings': (lambda lhs, rhs: equalSeq(lhs, rhs)), 
   b'WideStrings': (lambda lhs, rhs: equalSeq(lhs, rhs)), 
   b'Floats': (lambda lhs, rhs: equalSeq(lhs, rhs, equalFloat)), 
   b'Ints': (lambda lhs, rhs: equalSeq(lhs, rhs)), 
   b'Vector2s': (lambda lhs, rhs: equalSeq(lhs, rhs, equalVector2)), 
   b'Vector3s': (lambda lhs, rhs: equalSeq(lhs, rhs, equalVector3)), 
   b'Vector4s': (lambda lhs, rhs: equalSeq(lhs, rhs, equalVector4))}

def equalComparator(tp):
    try:
        return EQUAL_COMPARATORS[tp]
    except KeyError:
        return equal

    return


DEFAULT_GETTERS = {b'String': (lambda : str()), 
   b'WideString': (lambda : unicode()), 
   b'Float': (lambda : 0.0), 
   b'Int': (lambda : 0), 
   b'Int64': (lambda : 0), 
   b'Vector2': (lambda : Math.Vector2()), 
   b'Vector3': (lambda : Math.Vector3()), 
   b'Vector4': (lambda : Math.Vector4()), 
   b'Matrix': (lambda : Math.Matrix()), 
   b'Bool': (lambda : False), 
   b'Strings': (lambda : ()), 
   b'WideStrings': (lambda : ()), 
   b'Floats': (lambda : ()), 
   b'Ints': (lambda : ()), 
   b'Vector2s': (lambda : ()), 
   b'Vector3s': (lambda : ()), 
   b'Vector4s': (lambda : ())}

def defaultGetter(tp):
    try:
        return DEFAULT_GETTERS[tp]
    except KeyError:
        return (lambda : None)

    return


def default(tp):
    try:
        return DEFAULT_GETTERS[tp]()
    except KeyError:
        return

    return
