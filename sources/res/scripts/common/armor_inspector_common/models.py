from __future__ import absolute_import
import typing
from dict2model import models

class ArmorInspectorConfigModel(models.Model):
    __slots__ = (b'enabled', b'linkButtonURL', b'disabledVehicle')

    def __init__(self, enabled, linkButtonURL, disabledVehicle):
        super(ArmorInspectorConfigModel, self).__init__()
        self.enabled = enabled
        self.linkButtonURL = linkButtonURL
        self.disabledVehicle = disabledVehicle
        return

    def _reprArgs(self):
        return (b'enabled={} linkButtonURL={} disabledVehicle={}').format(self.enabled, self.linkButtonURL, self.disabledVehicle)

    def isDisabledForVehicle(self, vehicleName):
        return vehicleName in self.disabledVehicle
