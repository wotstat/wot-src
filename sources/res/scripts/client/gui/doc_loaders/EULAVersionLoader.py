from __future__ import absolute_import
import ResMgr
from helpers import VERSION_FILE_PATH
from soft_exception import SoftException
__author__ = b'd_savitski'
VERSION_TAG = b'showLicense'

class EULAVersionLoader(object):

    def __init__(self):
        super(EULAVersionLoader, self).__init__()
        self.__xmlVersion = 0
        self.loadXMLVersion()
        return

    @property
    def xmlVersion(self):
        return self.__xmlVersion

    def loadXMLVersion(self):
        xmlFile = ResMgr.openSection(VERSION_FILE_PATH)
        if not xmlFile:
            raise SoftException(b'EULAVersionLoader.loadXMLVersion %s file is missing' % VERSION_FILE_PATH)
        xmlVersion = xmlFile.readString(VERSION_TAG)
        if not xmlVersion:
            raise SoftException(b'Subsection EULAVersionLoader.loadXMLVersion EULAVersion tag <%(ver)s> is missing or empty in %(path)s' % {b'ver': VERSION_TAG, b'path': VERSION_FILE_PATH})
        self.__xmlVersion = int(xmlVersion)
        return
