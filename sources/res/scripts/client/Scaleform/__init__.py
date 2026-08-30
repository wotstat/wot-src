from __future__ import absolute_import, print_function
AVAILABLE = False
try:
    from _Scaleform import *
    AVAILABLE = True
except ImportError:
    print(b'There is no module named _Scaleform.  The most likely cause of this     is the client was built without Scaleform support.  Please check the     documentation for further details on enabling Scaleform support.')

def showCursor():
    import GUI, BigWorld
    c = GUI.mcursor()
    c.visible = 1
    BigWorld.setCursor(c)
    return


def exampleFSCommandHandler(cmd, s2):
    print(b'FSCommand - ', cmd, s2)
    return


def exampleExternalInterfaceHandler(cmd, *args):
    print(b'External Interface command - ', cmd, args)
    return


def createMovieInstance(file=b'scaleform/d3d9guide.swf'):
    mv = None
    mvDef = MovieDef(file)
    mv = mvDef.createInstance()
    mv.backgroundAlpha = 0.0
    mv.setFSCommandCallback(exampleFSCommandHandler)
    mv.setExternalInterfaceCallback(exampleExternalInterfaceHandler)
    mv.setFocussed()
    return (mv, mvDef)


def create3DDemo():
    file = b'scaleform/dogfight.swf'
    return createMovieInstance(file)


def createMovieGUI(file=b'scaleform/d3d9guide.swf'):
    m, _ = createMovieInstance(file)
    import GUI
    for i in GUI.roots():
        i.position[2] = max(i.position[2], 0.1)

    f = GUI.Flash(m)
    f.position = (0, 0, 0)
    f.focus = True
    f.moveFocus = True
    GUI.addRoot(f)
    showCursor()
    return f


def createIMEFontsMovie():
    print(b'Fonts loading from Python is not supported anymore.')
    return


def createIME():
    print(b'Fonts mapping from Python is not supported anymore.')
    showCursor()
    return


def createIMEMovie():
    file = b'scaleform/IMESample.swf'
    return createMovieInstance(file)


def createFontMovie(file=b'scaleform/drawtext_fonts.swf'):
    print(b'Fonts loading from Python is not supported anymore.')
    return


def createAllFontsMovie():
    print(b'Fonts loading from Python is not supported anymore.')
    return


def createFlashText(fontName=b'Slate Mobile'):
    import GUI
    g = GUI.FlashText(u'some label', fontName)
    g.size = (2, 2)
    g.position = (0, 0, 0)
    return g
