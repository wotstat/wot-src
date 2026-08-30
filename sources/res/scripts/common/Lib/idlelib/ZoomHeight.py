import re, sys
from idlelib import macosxSupport

class ZoomHeight:
    menudefs = [
     (
      b'windows',
      [
       (b'_Zoom Height', b'<<zoom-height>>')])]

    def __init__(self, editwin):
        self.editwin = editwin
        return

    def zoom_height_event(self, event):
        top = self.editwin.top
        zoom_height(top)
        return


def zoom_height(top):
    geom = top.wm_geometry()
    m = re.match(b'(\\d+)x(\\d+)\\+(-?\\d+)\\+(-?\\d+)', geom)
    if not m:
        top.bell()
        return
    width, height, x, y = map(int, m.groups())
    newheight = top.winfo_screenheight()
    if sys.platform == b'win32':
        newy = 0
        newheight = newheight - 72
    elif macosxSupport.isAquaTk():
        newy = 22
        newheight = newheight - newy - 88
    else:
        newy = 0
        newheight = newheight - 88
    if height >= newheight:
        newgeom = b''
    else:
        newgeom = b'%dx%d+%d+%d' % (width, newheight, x, newy)
    top.wm_geometry(newgeom)
    return
