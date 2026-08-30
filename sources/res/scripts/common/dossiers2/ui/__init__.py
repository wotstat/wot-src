from dossiers2.ui.layouts import init as ui_layouts_init
from dossiers2.ui.achievements import init as achieves_init

def init():
    achieves_init(b'scripts/item_defs/achievements.xml')
    ui_layouts_init()
    return
