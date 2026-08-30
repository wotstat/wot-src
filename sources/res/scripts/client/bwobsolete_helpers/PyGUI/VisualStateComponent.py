import sys
from bwdebug import ERROR_MSG
import ResMgr

class VisualState(object):

    def onSave(self, dataSection):
        return

    def onLoad(self, dataSection):
        return

    def apply(self, componentScript):
        return

    def _readMappingSection(self, dataSection):
        mappingName = dataSection.asString.strip()
        mappingType = mappingName if mappingName else b'UV'
        mapping = [
         None, None, None, None]
        mapping[0] = dataSection.readVector2(b'coords0')
        mapping[1] = dataSection.readVector2(b'coords1')
        mapping[2] = dataSection.readVector2(b'coords2')
        mapping[3] = dataSection.readVector2(b'coords3')
        mapping = tuple(mapping)
        return (
         mappingType, mapping)

    def _writeMappingSection(self, dataSection, mappingType, mapping):
        dataSection.asString = mappingType
        dataSection.writeVector2(b'coords0', mapping[0])
        dataSection.writeVector2(b'coords1', mapping[1])
        dataSection.writeVector2(b'coords2', mapping[2])
        dataSection.writeVector2(b'coords3', mapping[3])
        return


class VisualStateComponent(object):

    def __init__(self, component, visualStateClassName):
        self.visualStateClassName = visualStateClassName
        self._visualStates = {}
        return

    def onSave(self, dataSection):
        dataSection.writeString(b'visualStates', self.visualStateClassName)
        visualStatesSection = dataSection._visualStates
        for stateName, state in self._visualStates.items():
            stateSection = visualStatesSection.createSection(stateName)
            state.onSave(stateSection)

        return

    def onLoad(self, dataSection):
        if dataSection.has_key(b'visualStates'):
            visualStatesSection = dataSection._visualStates
            if visualStatesSection.has_key(b'external'):
                extName = visualStatesSection._external.asString
                ext = ResMgr.openSection(extName)
                if ext is not None:
                    visualStatesSection = ext
                else:
                    ERROR_MSG(b"Failed to open external visual state '%s'." % extName)
            self.visualStateClassName = visualStatesSection.asString
            components = self.visualStateClassName.strip(b'"').split(b'.')
            module = __import__(b'__main__')
            for comp in components[:-1]:
                module = getattr(module, comp)

            visualStateClass = getattr(module, components[-1])
            for stateName, stateSection in visualStatesSection.items():
                visualState = visualStateClass()
                visualState.onLoad(stateSection)
                self._visualStates[stateName] = visualState

        return

    def setVisualState(self, stateName):
        state = self._visualStates.get(stateName, None)
        if state:
            state.apply(self)
        else:
            ERROR_MSG(b"No Visual State '%s' on %s" % (stateName, self))
        return
