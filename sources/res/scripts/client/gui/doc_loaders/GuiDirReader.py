from __future__ import absolute_import
from constants import CURRENT_REALM
import ResMgr

class GuiDirReader(object):
    SCALEFORM_STARTUP_VIDEO_PATH = b'gui/flash/videos/startup'
    SCALEFORM_STARTUP_VIDEO_MASK = b'videos/startup{realm}/%s'
    VIDEO_EXTENSION = b'usm'

    @staticmethod
    def computeVideoParams():
        realm = b'_' + CURRENT_REALM.lower()
        path = GuiDirReader.SCALEFORM_STARTUP_VIDEO_PATH
        mask = GuiDirReader.SCALEFORM_STARTUP_VIDEO_MASK
        custom_path = path + realm
        ds = ResMgr.openSection(custom_path)
        if ds is not None:
            custom_mask = mask.format(realm=realm)
            return (
             custom_path, custom_mask)
        else:
            default_mask = mask.format(realm=b'')
            return (path, default_mask)

    @staticmethod
    def getAvailableIntroVideoFiles():
        path, mask = GuiDirReader.computeVideoParams()
        ds = ResMgr.openSection(path)
        movieFiles = []
        for filename in ds.keys():
            try:
                _, extension = filename.split(b'.')
            except ValueError:
                continue

            _, extension = filename.split(b'.')
            if extension == GuiDirReader.VIDEO_EXTENSION:
                movieFiles.append(mask % filename)

        ResMgr.purge(path, True)
        return movieFiles
