import BigWorld, GUI, Keys
from PyGUIBase import PyGUIBase

class Grid(PyGUIBase):
    factoryString = b'PyGUI.Grid'

    def __init__(self, component):
        PyGUIBase.__init__(self, component)
        component.script = self
        self.component.focus = True
        self.component.moveFocus = True
        self.component.crossFocus = True
        self.horizontalFirst = True
        self.gridWidth = 1
        self.gridHeight = 1
        self.borderTop = 0
        self.borderBottom = 0
        self.borderLeft = 0
        self.borderRight = 0
        self.horizontalGap = 0
        self.verticalGap = 0
        return

    def onSave(self, dataSection):
        dataSection.writeBool(b'horizontalFirst', self.horizontalFirst)
        dataSection.writeFloat(b'gridWidth', self.gridWidth)
        dataSection.writeFloat(b'gridHeight', self.gridHeight)
        dataSection.writeFloat(b'borderTop', self.borderTop)
        dataSection.writeFloat(b'borderBottom', self.borderBottom)
        dataSection.writeFloat(b'borderLeft', self.borderLeft)
        dataSection.writeFloat(b'borderRight', self.borderRight)
        dataSection.writeFloat(b'horizontalGap', self.horizontalGap)
        dataSection.writeFloat(b'verticalGap', self.verticalGap)
        return

    def onLoad(self, dataSection):
        self.horizontalFirst = dataSection.readBool(b'horizontalFirst', self.horizontalFirst)
        self.gridWidth = dataSection.readFloat(b'gridWidth', self.gridWidth)
        self.gridHeight = dataSection.readFloat(b'gridHeight', self.gridHeight)
        self.borderTop = dataSection.readFloat(b'borderTop', self.borderTop)
        self.borderBottom = dataSection.readFloat(b'borderBottom', self.borderBottom)
        self.borderLeft = dataSection.readFloat(b'borderLeft', self.borderLeft)
        self.borderRight = dataSection.readFloat(b'borderRight', self.borderRight)
        self.horizontalGap = dataSection.readFloat(b'horizontalGap', self.horizontalGap)
        self.verticalGap = dataSection.readFloat(b'verticalGap', self.verticalGap)
        return

    def doLayout(self):
        widthMode = self.component.widthMode
        heightMode = self.component.heightMode
        if widthMode == GUI.Simple.eSizeMode.PIXEL:
            horizSize = (self.component.width - self.borderLeft - self.borderRight - self.horizontalGap * (self.gridWidth - 1)) / self.gridWidth
            horizOffset = horizSize + self.horizontalGap
            horizStart = self.borderLeft
        if widthMode == GUI.Simple.eSizeMode.CLIP:
            horizSize = (2.0 - self.borderLeft - self.borderRight - self.horizontalGap * (self.gridWidth - 1)) / self.gridWidth
            horizOffset = horizSize + self.horizontalGap
            horizStart = -1.0 + self.borderLeft
        if heightMode == GUI.Simple.eSizeMode.PIXEL:
            vertSize = (self.component.height - self.borderTop - self.borderBottom - self.verticalGap * (self.gridHeight - 1)) / self.gridHeight
            vertOffset = vertSize + self.verticalGap
            vertStart = self.borderTop
        if heightMode == GUI.Simple.eSizeMode.CLIP:
            vertSize = (2.0 - self.borderTop - self.borderBottom - self.verticalGap * (self.gridHeight - 1)) / self.gridHeight
            vertOffset = -(vertSize + self.verticalGap)
            vertStart = 1.0 - self.borderTop
        horizPos = horizStart
        vertPos = vertStart
        count = 1
        for discard, i in self.component.children:
            i.widthMode = widthMode
            i.width = horizSize
            i.heightMode = heightMode
            i.height = vertSize
            i.horizontalPositionMode = widthMode
            i.verticalPositionMode = heightMode
            i.horizontalAnchor = b'LEFT'
            i.verticalAnchor = b'TOP'
            i.position = (horizPos, vertPos, i.position[2])
            if self.horizontalFirst:
                if count == self.gridWidth:
                    count = 1
                    horizPos = horizStart
                    vertPos += vertOffset
                else:
                    count += 1
                    horizPos += horizOffset
            elif count == self.gridHeight:
                count = 1
                vertPos = vertStart
                horizPos += horizOffset
            else:
                count += 1
                vertPos += vertOffset

        return

    @staticmethod
    def create(texture, gridSize=(1, 1), horizontalFirst=True, **kwargs):
        c = GUI.Window(texture)
        c.materialFX = GUI.Simple.eMaterialFX.BLEND
        c.widthMode = GUI.Simple.eSizeMode.CLIP
        c.heightMode = GUI.Simple.eSizeMode.CLIP
        c.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP
        c.verticalPositionMode = GUI.Simple.ePositionMode.CLIP
        g = Grid(c, **kwargs)
        if len(gridSize) == 2:
            g.gridWidth = gridSize[0]
            g.gridHeight = gridSize[1]
        else:
            g.gridWidth = 1
            g.gridHeight = 1
        g.horizontalFirst = horizontalFirst
        return g.component
