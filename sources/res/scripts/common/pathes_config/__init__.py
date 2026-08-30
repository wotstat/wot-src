from __future__ import absolute_import
import os, sys, site
from soft_exception import SoftException

def setupPaths():
    root = b'../../../../..'

    def expandPath(item):
        if not os.path.isabs(item):
            if item[0] == b'~':
                item = os.path.expanduser(item)
            else:
                item = os.path.join(os.path.split(os.path.abspath(__file__))[0], item)
        return os.path.normpath(item)

    platformSuffix = None
    try:
        from pycommon import platform_info
    except:
        platformSuffix = None

    platformSuffix = platform_info.getPlatformSuffix()
    if not platformSuffix:
        raise SoftException(b'Unable to determine platform suffix')
    addPath = [
     root + b'/tools/bigworld/server',
     root + b'/res/bigworld/scripts/common',
     root + b'/res/bigworld/scripts/common/Lib',
     root + b'/res/bigworld/scripts/common/site-packages',
     root + b'/res/bigworld/scripts/server_common',
     root + b'/res/bigworld/scripts/server_common/lib-dynload-el7',
     root + b'/res/wot/scripts',
     root + b'/res/wot/scripts/base',
     root + b'/res/wot/scripts/base/account_helpers',
     root + b'/res/wot/scripts/server_common',
     root + b'/res/wot/scripts/server_common/virtual_machine',
     root + b'/res/wot/scripts/server_common/site-packages/' + platformSuffix,
     root + b'/res/wot/scripts/common',
     root + b'/res/wot/scripts/development/libs',
     root + b'/tools/wot/server/bw_lib/bigworld/fake']
    for path in addPath:
        norm_path = expandPath(path)
        if norm_path.endswith(b'site-packages'):
            site.addsitedir(norm_path)
        else:
            sys.path.append(norm_path)

    bw_xml = expandPath(root + b'/res/wot/server/bw.xml')
    if not os.path.exists(bw_xml):
        from shutil import copyfile
        copyfile(expandPath(root + b'/res/wot/server/bw.xml.dist'), bw_xml)
    return
