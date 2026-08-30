from tkCommonDialog import Dialog
ERROR = b'error'
INFO = b'info'
QUESTION = b'question'
WARNING = b'warning'
ABORTRETRYIGNORE = b'abortretryignore'
OK = b'ok'
OKCANCEL = b'okcancel'
RETRYCANCEL = b'retrycancel'
YESNO = b'yesno'
YESNOCANCEL = b'yesnocancel'
ABORT = b'abort'
RETRY = b'retry'
IGNORE = b'ignore'
OK = b'ok'
CANCEL = b'cancel'
YES = b'yes'
NO = b'no'

class Message(Dialog):
    command = b'tk_messageBox'


def _show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and b'icon' not in options:
        options[b'icon'] = _icon
    if _type and b'type' not in options:
        options[b'type'] = _type
    if title:
        options[b'title'] = title
    if message:
        options[b'message'] = message
    res = Message(**options).show()
    if isinstance(res, bool):
        if res:
            return YES
        return NO
    return str(res)


def showinfo(title=None, message=None, **options):
    return _show(title, message, INFO, OK, **options)


def showwarning(title=None, message=None, **options):
    return _show(title, message, WARNING, OK, **options)


def showerror(title=None, message=None, **options):
    return _show(title, message, ERROR, OK, **options)


def askquestion(title=None, message=None, **options):
    return _show(title, message, QUESTION, YESNO, **options)


def askokcancel(title=None, message=None, **options):
    s = _show(title, message, QUESTION, OKCANCEL, **options)
    return s == OK


def askyesno(title=None, message=None, **options):
    s = _show(title, message, QUESTION, YESNO, **options)
    return s == YES


def askyesnocancel(title=None, message=None, **options):
    s = _show(title, message, QUESTION, YESNOCANCEL, **options)
    s = str(s)
    if s == CANCEL:
        return None
    else:
        return s == YES


def askretrycancel(title=None, message=None, **options):
    s = _show(title, message, WARNING, RETRYCANCEL, **options)
    return s == RETRY


if __name__ == b'__main__':
    print b'info', showinfo(b'Spam', b'Egg Information')
    print b'warning', showwarning(b'Spam', b'Egg Warning')
    print b'error', showerror(b'Spam', b'Egg Alert')
    print b'question', askquestion(b'Spam', b'Question?')
    print b'proceed', askokcancel(b'Spam', b'Proceed?')
    print b'yes/no', askyesno(b'Spam', b'Got it?')
    print b'yes/no/cancel', askyesnocancel(b'Spam', b'Want it?')
    print b'try again', askretrycancel(b'Spam', b'Try again?')
