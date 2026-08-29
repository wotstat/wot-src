import struct
from typing import Callable, Tuple
from DossierDescr import DossierDescr
from dossiers2.common.DossierBlockBuilders import TYPE_BLOCK_BUILDER
from dossiers2.custom.updaters import DossierVersionUpdaterBase

class DossierBuilder(object):

    def __init__(self, blockBuilders, versionFormat, blockSizeFormat, version, updater, initializer):
        self.__blockBuilders = blockBuilders
        self.__versionFormat = versionFormat
        self.__headerFormat = b'<' + versionFormat + blockSizeFormat * len(blockBuilders)
        self.__latestVersion = version
        self.__updater = updater
        self.__initializer = initializer
        self.__emptyCompDescr = struct.pack(self.__headerFormat, version, *([0] * len(blockBuilders)))
        return

    def build(self, compDescr=b''):
        if compDescr == b'':
            dossier = DossierDescr(self.__emptyCompDescr, self.__blockBuilders, self.__headerFormat)
            self.__initializer(dossier)
        else:
            version = struct.unpack_from(self.__versionFormat, compDescr)[0]
            compDescr = self.__updater.updateVersion(version, compDescr)
            dossier = DossierDescr(compDescr, self.__blockBuilders, self.__headerFormat)
        return dossier
