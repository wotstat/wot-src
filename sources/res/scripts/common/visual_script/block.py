from __future__ import absolute_import
from builtins import map
from typing import List, Any, Sequence
from visual_script.misc import ASPECT, BLOCK_MODE

def buildStrKeysValue(*args):
    return (b';').join(args)


def makeResEditorData(path, *extensions):
    return [
     path, (b';;').join(map((lambda ext: b'*.%s' % ext), extensions))]


class InitParam(object):

    def __init__(self, name, slotType, defaultValue, editorType=None, editorData=None):
        self.name = name
        self.slotType = slotType
        self.defaultValue = defaultValue
        self.editorType = editorType
        self.editorData = editorData
        return


class DataInputSlot(object):

    @staticmethod
    def getValue():
        return

    @staticmethod
    def hasValue():
        return False

    @staticmethod
    def isConstValue():
        return False

    @staticmethod
    def setDefaultValue(value):
        return

    @staticmethod
    def setEditorData(editorData):
        return


class DataOutputSlot(object):

    @staticmethod
    def setValue(value):
        return


class EventInputSlot(object):
    pass


class EventOutputSlot(object):

    @staticmethod
    def call():
        return


class Meta(object):

    @classmethod
    def blockName(cls):
        return cls.__name__

    @classmethod
    def blockModule(cls):
        return cls.__module__

    @classmethod
    def blockAspects(cls):
        return ASPECT.ALL

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/python'

    @classmethod
    def blockColor(cls):
        return 7189746

    @classmethod
    def blockCategory(cls):
        return b'General'

    @classmethod
    def initParams(cls):
        return []

    @classmethod
    def mode(cls):
        return BLOCK_MODE.NONE


class Block(Meta):

    def __init__(self, agent):
        self.__agent = agent
        super(Block, self).__init__()
        return

    def captionText(self):
        return b''

    def validate(self):
        return b''

    def validateAllRequired(self):
        for item in self._getSlots():
            if hasattr(item, b'hasValue') and not item.hasValue():
                return item.name() + b' value is required'

        return b''

    @classmethod
    def isOnFinishScriptCallRequired(cls):
        return cls.onFinishScript != Block.onFinishScript

    def onFinishScript(self):
        return

    @classmethod
    def isOnStartScriptCallRequired(cls):
        return cls.onStartScript != Block.onStartScript

    def onStartScript(self):
        return

    def _getInitParams(self):
        return self.__agent.getInitParams()

    def _getSlots(self):
        return self.__agent.getSlots()

    def _makeDataInputSlot(self, name, slotType, editorType=-1):
        return self.__agent.makeDataInputSlot(name, slotType, editorType)

    def planName(self):
        return self.__agent.planName()

    def blockId(self):
        id = self.__agent.blockId()
        if id:
            return id
        return self.blockName()

    def _makeDataOutputSlot(self, name, slotType, fun):
        return self.__agent.makeDataOutputSlot(name, slotType, fun)

    def _makeEventInputSlot(self, name, fun):
        return self.__agent.makeEventInputSlot(name, fun)

    def _makeEventOutputSlot(self, name):
        return self.__agent.makeEventOutputSlot(name)

    def _writeLog(self, msg):
        self.__agent.writeLog(msg)
        return
