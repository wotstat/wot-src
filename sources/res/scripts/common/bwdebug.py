from __future__ import absolute_import, print_function
import BigWorld, sys
printPath = False

def getClassName(f):
    try:
        selfClass = f.f_locals[b'self'].__class__
        try:
            mro = selfClass.__mro__
        except AttributeError:
            stack = [
             selfClass]
            mro = []
            while stack:
                curr = stack.pop(0)
                mro.append(curr)
                stack += curr.__bases__

        funcName = f.f_code.co_name
        for c in mro:
            try:
                if funcName.startswith(b'__'):
                    method = c.__dict__[b'_' + c.__name__ + funcName]
                else:
                    method = c.__dict__[funcName]
                if method.func_code == f.f_code:
                    return c.__name__ + b'.'
            except KeyError:
                pass

    except:
        pass

    return b''


def defaultOutputMethod(category, message, metaData):
    if category == b'':
        print(message)
    else:
        print((b'[{category}] {message}').format(category=category, message=message))
    return


def _printMessage(outputMethod, args, printPathArg):
    f = sys._getframe(2)
    output = b''
    if printPathArg:
        output += f.f_code.co_filename + b'(' + str(f.f_lineno) + b') : '
    output += getClassName(f) + f.f_code.co_name + b': '
    output += (b' ').join([str(m) for m in args])
    outputMethod(b'', output, b'')
    return


def getOutputMethod(method):
    if not hasattr(BigWorld, method):
        return defaultOutputMethod
    return getattr(BigWorld, method)


def TRACE_MSG(*args):
    _printMessage(getOutputMethod(b'logTrace'), args, printPath)
    return


def DEBUG_MSG(*args):
    _printMessage(getOutputMethod(b'logDebug'), args, printPath)
    return


def INFO_MSG(*args):
    _printMessage(getOutputMethod(b'logInfo'), args, printPath)
    return


def NOTICE_MSG(*args):
    _printMessage(getOutputMethod(b'logNotice'), args, printPath)
    return


def WARNING_MSG(*args):
    _printMessage(getOutputMethod(b'logWarning'), args, True)
    return


def ERROR_MSG(*args):
    _printMessage(getOutputMethod(b'logError'), args, True)
    return


def CRITICAL_MSG(*args):
    _printMessage(getOutputMethod(b'logCritical'), args, True)
    return


def HACK_MSG(*args):
    _printMessage(getOutputMethod(b'logHack'), args, True)
    return


__all__ = [
 15, 
 16, 
 17, 
 18, 
 19, 
 20, 
 21, 
 22]
