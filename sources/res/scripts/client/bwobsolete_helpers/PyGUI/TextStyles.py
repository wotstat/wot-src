import BigWorld, GUI, Math, ResMgr
from bwdebug import ERROR_MSG
styles = {b'Heading': (
              b'Heading.font', (255, 255, 255, 255)), 
   b'Label': (
            b'Label.font', (255, 255, 255, 255)), 
   b'ButtonNormal': (
                   b'Heading.font', (255, 255, 255, 200)), 
   b'ButtonHover': (
                  b'Heading.font', (255, 255, 255, 255)), 
   b'ButtonPressed': (
                    b'Heading.font', (255, 255, 255, 255)), 
   b'ButtonActive': (
                   b'Heading.font', (0, 0, 0, 255)), 
   b'ButtonDisabled': (
                     b'Heading.font', (128, 128, 128, 255))}
fontAliases = {}

def setStyle(component, styleName):
    if styles.has_key(styleName):
        style = styles[styleName]
        component.font = fontAliases.get(style[0], style[0])
        component.colour = style[1]
    else:
        ERROR_MSG(b"No style named '%s'." % (styleName,))
    return
