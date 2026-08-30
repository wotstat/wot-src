import sys, Tkinter
from os import path
import warnings

def runningAsOSXApp():
    warnings.warn(b'runningAsOSXApp() is deprecated, use isAquaTk()', DeprecationWarning, stacklevel=2)
    return isAquaTk()


def isCarbonAquaTk(root):
    warnings.warn(b'isCarbonAquaTk(root) is deprecated, use isCarbonTk()', DeprecationWarning, stacklevel=2)
    return isCarbonTk()


_tk_type = None

def _initializeTkVariantTests(root):
    global _tk_type
    if sys.platform == b'darwin':
        ws = root.tk.call(b'tk', b'windowingsystem')
        if b'x11' in ws:
            _tk_type = b'xquartz'
        elif b'aqua' not in ws:
            _tk_type = b'other'
        elif b'AppKit' in root.tk.call(b'winfo', b'server', b'.'):
            _tk_type = b'cocoa'
        else:
            _tk_type = b'carbon'
    else:
        _tk_type = b'other'
    return


def isAquaTk():
    return _tk_type == b'cocoa' or _tk_type == b'carbon'


def isCarbonTk():
    return _tk_type == b'carbon'


def isCocoaTk():
    return _tk_type == b'cocoa'


def isXQuartz():
    return _tk_type == b'xquartz'


def tkVersionWarning(root):
    if isCocoaTk():
        patchlevel = root.tk.call(b'info', b'patchlevel')
        if patchlevel not in (b'8.5.7', b'8.5.9'):
            return False
        return (b'WARNING: The version of Tcl/Tk ({0}) in use may be unstable.\\nVisit http://www.python.org/download/mac/tcltk/ for current information.').format(patchlevel)
    else:
        return False

    return


def addOpenEventSupport(root, flist):

    def doOpenFile(*args):
        for fn in args:
            flist.open(fn)

        return

    root.createcommand(b'::tk::mac::OpenDocument', doOpenFile)
    return


def hideTkConsole(root):
    try:
        root.tk.call(b'console', b'hide')
    except Tkinter.TclError:
        pass

    return


def overrideRootMenu(root, flist):
    from Tkinter import Menu
    from idlelib import Bindings
    from idlelib import WindowList
    closeItem = Bindings.menudefs[0][1][-2]
    del Bindings.menudefs[0][1][-3:]
    Bindings.menudefs[0][1].insert(6, closeItem)
    del Bindings.menudefs[-1][1][0:2]
    del Bindings.menudefs[-2][1][0]
    menubar = Menu(root)
    root.configure(menu=menubar)
    menudict = {}
    menudict[b'windows'] = menu = Menu(menubar, name=b'windows', tearoff=0)
    menubar.add_cascade(label=b'Window', menu=menu, underline=0)

    def postwindowsmenu(menu=menu):
        end = menu.index(b'end')
        if end is None:
            end = -1
        if end > 0:
            menu.delete(0, end)
        WindowList.add_windows_to_menu(menu)
        return

    WindowList.register_callback(postwindowsmenu)

    def about_dialog(event=None):
        from idlelib import aboutDialog
        aboutDialog.AboutDialog(root, b'About IDLE')
        return

    def config_dialog(event=None):
        from idlelib import configDialog
        root.instance_dict = flist.inversedict
        configDialog.ConfigDialog(root, b'Settings')
        return

    def help_dialog(event=None):
        from idlelib import help
        help.show_idlehelp(root)
        return

    root.bind(b'<<about-idle>>', about_dialog)
    root.bind(b'<<open-config-dialog>>', config_dialog)
    root.createcommand(b'::tk::mac::ShowPreferences', config_dialog)
    if flist:
        root.bind(b'<<close-all-windows>>', flist.close_all_callback)
        root.createcommand(b'exit', flist.close_all_callback)
    if isCarbonTk():
        menudict[b'application'] = menu = Menu(menubar, name=b'apple', tearoff=0)
        menubar.add_cascade(label=b'IDLE', menu=menu)
        Bindings.menudefs.insert(0, (
         b'application',
         [
          (b'About IDLE', b'<<about-idle>>'),
          None]))
        tkversion = root.tk.eval(b'info patchlevel')
        if tuple(map(int, tkversion.split(b'.'))) < (8, 4, 14):
            Bindings.menudefs[0][1].append((b'_Preferences....', b'<<open-config-dialog>>'))
    if isCocoaTk():
        root.createcommand(b'tkAboutDialog', about_dialog)
        root.createcommand(b'::tk::mac::ShowHelp', help_dialog)
        del Bindings.menudefs[-1][1][0]
    return


def setupApp(root, flist):
    _initializeTkVariantTests(root)
    if isAquaTk():
        hideTkConsole(root)
        overrideRootMenu(root, flist)
        addOpenEventSupport(root, flist)
    return
