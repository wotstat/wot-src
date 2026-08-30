import BigWorld, GUI, Keys, math
from PyGUIBase import PyGUIBase
from DraggableComponent import DraggableComponent
from Utils import clipPosition, clipSize, applyMapping
from VisualStateComponent import VisualState, VisualStateComponent

class SliderVisualState(VisualState):

    def __init__(self):
        VisualState.__init__(self)
        self.backgroundTextureName = b''
        self.backgroundTextureMapping = None
        self.backgroundColour = (255, 255, 255, 255)
        self.thumbTextureName = b''
        self.thumbTextureMapping = None
        self.thumbColour = (255, 255, 255, 255)
        return

    def onSave(self, dataSection):
        VisualState.onSave(self, dataSection)
        backgroundSection = dataSection.createSection(b'background')
        backgroundSection.writeString(b'textureName', self.backgroundTextureName)
        if self.backgroundTextureMapping:
            mappingSection = backgroundSection.createSection(b'mapping')
            self._writeMappingSection(mappingSection, self.backgroundTextureMappingType, self.backgroundTextureMapping)
        backgroundSection.writeVector4(b'colour', self.backgroundColour)
        thumbSection = dataSection.createSection(b'thumb')
        thumbSection.writeString(b'textureName', self.thumbTextureName)
        if self.thumbTextureMapping:
            mappingSection = thumbSection.createSection(b'mapping')
            self._writeMappingSection(mappingSection, self.thumbTextureMappingType, self.thumbTextureMapping)
        thumbSection.writeVector4(b'colour', self.thumbColour)
        return

    def onLoad(self, dataSection):
        VisualState.onLoad(self, dataSection)
        if dataSection.has_key(b'background'):
            backgroundSection = dataSection._background
            self.backgroundTextureName = backgroundSection.readString(b'textureName', b'')
            if backgroundSection.has_key(b'mapping'):
                mappingSection = backgroundSection._mapping
                mappingType, mapping = self._readMappingSection(mappingSection)
                self.backgroundTextureMappingType = mappingType
                self.backgroundTextureMapping = mapping
            else:
                self.backgroundTextureMapping = None
            self.backgroundColour = backgroundSection.readVector4(b'colour', (255, 255, 255, 255))
        if dataSection.has_key(b'thumb'):
            thumbSection = dataSection._thumb
            self.thumbTextureName = thumbSection.readString(b'textureName', b'')
            if thumbSection.has_key(b'mapping'):
                mappingSection = thumbSection._mapping
                mappingType, mapping = self._readMappingSection(mappingSection)
                self.thumbTextureMappingType = mappingType
                self.thumbTextureMapping = mapping
            else:
                self.thumbTextureMapping = None
            self.thumbColour = thumbSection.readVector4(b'colour', (255, 255, 255, 255))
        return

    def apply(self, componentScript):
        VisualState.apply(self, componentScript)
        if hasattr(componentScript, b'sliderBackground'):
            componentScript.sliderBackground.textureName = self.backgroundTextureName
            if self.thumbTextureMapping:
                applyMapping(componentScript.sliderBackground, self.backgroundTextureMappingType, self.backgroundTextureMapping)
            componentScript.sliderBackground.colour = self.backgroundColour
        if hasattr(componentScript, b'sliderThumb'):
            componentScript.sliderThumb.textureName = self.thumbTextureName
            if self.thumbTextureMapping:
                applyMapping(componentScript.sliderThumb, self.thumbTextureMappingType, self.thumbTextureMapping)
            componentScript.sliderThumb.colour = self.thumbColour
        return


class SliderThumb(PyGUIBase, DraggableComponent):
    factoryString = b'PyGUI.SliderThumb'

    def __init__(self, component, isHorizontal=True):
        PyGUIBase.__init__(self, component)
        DraggableComponent.__init__(self, isHorizontal, not isHorizontal, True)
        self.component.focus = True
        self.component.mouseButtonFocus = True
        self.component.moveFocus = True
        self.component.crossFocus = True
        self.onDragging = self._onDragging
        return

    def _setValue(self, value):
        sliderWidth, sliderHeight = clipSize(self.component)
        slider = self.component.parent.script
        thumbPos = (value - slider.minValue) / (slider.maxValue - slider.minValue)
        if slider.isHorizontal:
            thumbPos = (2.0 - sliderWidth) * thumbPos - 1.0 + sliderWidth / 2
        else:
            thumbPos = (2.0 - sliderHeight) * thumbPos - 1.0 + sliderHeight / 2
        self.component.position = (thumbPos, 0, 1) if slider.isHorizontal else (0, thumbPos, 1)
        return

    def _setValueFromMouse(self, pos):
        slider = self.component.parent.script
        parent = self.component.parent
        position = parent.screenToLocal(pos)
        self.component.position = (2 * position[0] / parent.width - 1.0, 0, 1) if slider.isHorizontal else (0, 2 * position[1] / parent.height - 1.0, 1)
        self._onDragging()
        return

    def _onDragging(self):
        position = clipPosition(self.component)
        sliderWidth, sliderHeight = clipSize(self.component)
        slider = self.component.parent.script
        if slider.isHorizontal:
            thumbPos = (position[0] + 1.0 - sliderWidth / 2) / (2.0 - sliderWidth)
        else:
            thumbPos = (position[1] + 1.0 - sliderHeight / 2) / (2.0 - sliderHeight)
        thumbPos = min(max(0.0, thumbPos), 1.0)
        newValue = thumbPos * (slider.maxValue - slider.minValue) + slider.minValue
        newValue += slider.stepSize / 2.0
        newValue -= math.fmod(newValue, slider.stepSize)
        self._setValue(newValue)
        slider.value = newValue
        slider.onValueChanged()
        return

    def handleMouseButtonEvent(self, comp, event):
        PyGUIBase.handleMouseButtonEvent(self, comp, event)
        slider = self.component.parent.script
        if event.key == Keys.KEY_LEFTMOUSE:
            if event.isKeyDown() and not slider.thumbPressed:
                slider.thumbPressed = True
            elif not event.isKeyDown() and slider.thumbPressed:
                slider.thumbPressed = False
        slider._updateVisualState(hover=True)
        return DraggableComponent.handleMouseButtonEvent(self, comp, event)

    def handleMouseEnterEvent(self, comp):
        PyGUIBase.handleMouseEnterEvent(self, comp)
        slider = self.component.parent.script
        slider.handleMouseEnterEvent(comp)
        slider.thumbPressed = slider.thumbPressed and BigWorld.isKeyDown(Keys.KEY_LEFTMOUSE)
        slider._updateVisualState(hover=True)
        return True

    def handleMouseLeaveEvent(self, comp):
        slider = self.component.parent.script
        slider._updateVisualState(hover=False)
        return True

    @staticmethod
    def create(slider, thumbTexture=b'', isHorizontal=True):
        c = GUI.Window(thumbTexture)
        c.materialFX = GUI.Simple.eMaterialFX.BLEND
        c.widthMode = slider.component.widthMode
        c.heightMode = slider.component.heightMode
        c.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP
        c.verticalPositionMode = GUI.Simple.ePositionMode.CLIP
        c.position = (0, 0, 1)
        slider.component.addChild(c, b'thumb')
        return SliderThumb(c, isHorizontal)


class Slider(PyGUIBase, VisualStateComponent):
    NORMAL_STATE = b'normal'
    HOVER_STATE = b'hover'
    PRESSED_STATE = b'pressed'
    DISABLED_STATE = b'disabled'
    factoryString = b'PyGUI.Slider'
    visualStateString = b'PyGUI.SliderVisualState'

    def __init__(self, component):
        PyGUIBase.__init__(self, component)
        VisualStateComponent.__init__(self, component, Slider.visualStateString)
        component.script = self
        self.isHorizontal = True
        self.minValue = 0.0
        self.maxValue = 1.0
        self.stepSize = 0.1
        self._value = 0.0
        self.thumbPressed = False
        self.sliderDisabled = False
        self.component.focus = True
        self.component.mouseButtonFocus = True
        self.component.crossFocus = True
        self.component.moveFocus = True
        self.onValueChanged = lambda : None
        return

    def _updateVisualState(self, hover):
        if self.sliderDisabled:
            visualStateName = Slider.DISABLED_STATE
        elif self.thumbPressed:
            visualStateName = Slider.PRESSED_STATE
        elif hover:
            visualStateName = Slider.HOVER_STATE
        else:
            visualStateName = Slider.NORMAL_STATE
        self.setVisualState(visualStateName)
        return

    def _onValueChanged(self):
        self.onValueChanged()
        return

    def _getValue(self):
        return self._value

    def _setValue(self, value):
        self._value = value
        self.component.thumb.script._setValue(value)
        return

    value = property(_getValue, _setValue)

    def handleMouseButtonEvent(self, comp, event):
        if event.key == Keys.KEY_LEFTMOUSE and event.isKeyDown():
            self.component.thumb.script._setValueFromMouse(GUI.mcursor().position)
            self.component.thumb.script.handleMouseButtonEvent(self.component.thumb, event)
        return True

    def onSave(self, dataSection):
        PyGUIBase.onSave(self, dataSection)
        dataSection.writeBool(b'isHorizontal', self.isHorizontal)
        dataSection.writeFloat(b'minValue', self.minValue)
        dataSection.writeFloat(b'maxValue', self.maxValue)
        dataSection.writeFloat(b'stepSize', self.stepSize)
        VisualStateComponent.onSave(self, dataSection)
        return

    def onLoad(self, dataSection):
        PyGUIBase.onLoad(self, dataSection)
        self.isHorizontal = dataSection.readBool(b'isHorizontal', self.isHorizontal)
        self.minValue = dataSection.readFloat(b'minValue', self.minValue)
        self.maxValue = dataSection.readFloat(b'maxValue', self.maxValue)
        self.stepSize = dataSection.readFloat(b'stepSize', self.stepSize)
        VisualStateComponent.onLoad(self, dataSection)
        return

    def onBound(self):
        self.value = self.minValue
        self.sliderBackground = self.component
        self.sliderThumb = self.component.thumb
        self._updateVisualState(hover=False)
        return

    @staticmethod
    def create(texture, thumbTexture=b'', isHorizontal=True, **kwargs):
        c = GUI.Window(texture)
        c.materialFX = GUI.Simple.eMaterialFX.BLEND
        c.widthMode = GUI.Simple.eSizeMode.CLIP
        c.heightMode = GUI.Simple.eSizeMode.CLIP
        c.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP
        c.verticalPositionMode = GUI.Simple.ePositionMode.CLIP
        s = Slider(c, **kwargs)
        s.isHorizontal = isHorizontal
        thumb = SliderThumb.create(s, thumbTexture, isHorizontal)
        thumb.width = 0.2 if isHorizontal else 2.0
        thumb.height = 2.0 if isHorizontal else 0.2
        return s.component
