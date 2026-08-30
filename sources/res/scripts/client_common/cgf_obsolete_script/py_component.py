from cgf_obsolete_script.auto_properties import AutoPropertyInitMetaclass

class Component(object):
    __metaclass__ = AutoPropertyInitMetaclass

    def activate(self):
        return

    def deactivate(self):
        return

    def destroy(self):
        return
