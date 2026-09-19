from __future__ import absolute_import
from py2to3.patched_future import with_metaclass
from components_base.auto_properties import AutoPropertyInitMetaclass

class Component(with_metaclass(AutoPropertyInitMetaclass, object)):

    def activate(self):
        return

    def deactivate(self):
        return

    def destroy(self):
        return
