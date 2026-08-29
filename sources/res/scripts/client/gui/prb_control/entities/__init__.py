from constants import IS_DEVELOPMENT
__all__ = (b'initDevFunctional', b'finiDevFunctional')

def initDevFunctional():
    if IS_DEVELOPMENT:
        try:
            from gui.development.dev_prebattle import init
        except ImportError:

            def init():
                return

        init()
    return


def finiDevFunctional():
    if IS_DEVELOPMENT:
        try:
            from gui.development.dev_prebattle import fini
        except ImportError:

            def fini():
                return

        fini()
    return
