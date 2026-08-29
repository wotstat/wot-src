import sys
from . import styles_overrider
from . import report_generator
g_stylesOverrider = styles_overrider.StylesOverrider()
g_reportGenerator = report_generator.ReportGenerator()

def setup():
    applyStylesFlag = b'--applyStyles'
    if applyStylesFlag in sys.argv:
        path = sys.argv[sys.argv.index(applyStylesFlag) + 1]
        g_stylesOverrider.loadStylesConfig(path)
    generateReportFlag = b'--generateReport'
    if generateReportFlag in sys.argv:
        location = sys.argv[sys.argv.index(generateReportFlag) + 1]
        g_reportGenerator.setLocation(location)
    return


__all__ = (b'styles_overrider', b'report_generator', b'g_stylesOverrider', b'g_reportGenerator', b'setup')
