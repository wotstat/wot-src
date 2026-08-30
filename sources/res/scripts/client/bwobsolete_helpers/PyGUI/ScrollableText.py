import BigWorld, GUI, re
from PyGUIBase import PyGUIBase
from Helpers.PyGUI.Utils import getHPixelScalar, WHITESPACE
from Helpers.PyGUI.Listeners import registerDeviceListener
import Utils, StringIO, string
_colourTagLen = len(b'\\cABCDEFGH;')
_colourTagRE = re.compile(b'\\\\[cC][0-9a-fA-F]{8};')

def _packColourTag(colour):
    return b'\\c%.2x%.2x%.2x%.2x;' % (int(colour[0]), int(colour[1]), int(colour[2]), int(colour[3]))


def _findStartOfWord(s, offset):
    i = offset
    while i >= 0:
        if i >= _colourTagLen and _colourTagRE.match(s, i - _colourTagLen) != None:
            i -= _colourTagLen + 1
            continue
        if s[i] in WHITESPACE:
            return i + 1
        i -= 1

    return -1


def _wrapLine(s, desiredWidth, textComponent):
    ret = []
    i = 0
    while i < len(s):
        while _colourTagRE.match(s, i) != None and i < len(s):
            i += _colourTagLen

        if i >= len(s):
            break
        subStr = s[:i]
        subStrWidth = textComponent.stringWidth(subStr)
        if subStrWidth > desiredWidth:
            wordStart = _findStartOfWord(s, i)
            if wordStart >= 0:
                subStr = s[:wordStart]
            else:
                while subStrWidth > desiredWidth and i > 0:
                    i -= 1
                    subStr = s[:i]
                    subStrWidth = textComponent.stringWidth(subStr)

                if i == 0:
                    i = 1
                subStr = s[:i]
            ret.append(subStr)
            s = s[len(subStr):]
            i = 0
        else:
            i += 1

    ret.append(s)
    return ret


class ScrollableText(PyGUIBase):
    factoryString = b'PyGUI.ScrollableText'

    def __init__(self, component=None):
        PyGUIBase.__init__(self, component)
        if component == None:
            self.component = GUI.Window(b'system/maps/col_white.bmp')
            self.component.colour = (128, 128, 128, 255)
            self.component.widthMode = GUI.Simple.eSizeMode.CLIP
            self.component.heightMode = GUI.Simple.eSizeMode.CLIP
            self.component.addChild(GUI.Text(b''), b'text')
            self.component.text.horizontalAnchor = GUI.Simple.eHAnchor.LEFT
            self.component.text.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP
            self.component.text.verticalAnchor = GUI.Simple.eVAnchor.BOTTOM
            self.component.text.verticalPositionMode = GUI.Simple.ePositionMode.CLIP
            self.component.text.position = (-1.0, -1.0, 0.5)
            self.component.text.multiline = True
            self.component.text.richFormatting = True
            self.component.text.colour = (255, 255, 255, 255)
            self.onBound()
        self.component.script = self
        self.maxLines = 255
        self.wordWrap = True
        self.minVisibleLines = 4
        self.autoSelectionFonts = [b'default_medium.font']
        self.idealCharactersPerLine = 80
        self.lines = []
        self.scrollIndex = 0
        self._displayedLineCount = 0
        registerDeviceListener(self)
        return

    def clear(self):
        self.lines = []
        self.scrollIndex = 0
        self._refillBuffer()
        return

    def getMaxLines(self):
        return self.maxLines

    def setMaxLines(self, maxLines):
        self.maxLines = maxLines
        self.scrollIndex = min(self.scrollIndex, self.maxLines)
        self.scrollIndex = min(self.scrollIndex, self._displayedLineCount - self.minVisibleLines)
        self._updateScroll()
        return

    def scrollUp(self, amt=4):
        self.scrollIndex = min(self.scrollIndex + amt, self.maxLines)
        self.scrollIndex = min(self.scrollIndex, self._displayedLineCount - self.minVisibleLines)
        self._updateScroll()
        return

    def scrollDown(self, amt=4):
        self.scrollIndex = max(self.scrollIndex - amt, 0)
        self._updateScroll()
        return

    def setScrollIndex(self, idx):
        self.scrollIndex = min(idx, self.maxLines)
        self.scrollIndex = max(self.scrollIndex, 0)
        self.scrollIndex = min(self.scrollIndex, self._displayedLineCount - self.minVisibleLines)
        self._updateScroll()
        return

    def onBound(self):
        if len(self.autoSelectionFonts) == 0:
            self.autoSelectionFonts = [
             self.component.text.font]
        self._recalcFontMetrics()
        self._selectFontBestMatch()
        return

    def onSave(self, dataSection):
        PyGUIBase.onSave(self, dataSection)
        dataSection.writeInt(b'maxLines', self.maxLines)
        dataSection.writeBool(b'wordWrap', self.wordWrap)
        return

    def onLoad(self, dataSection):
        PyGUIBase.onLoad(self, dataSection)
        self.maxLines = dataSection.readInt(b'maxLines', self.maxLines)
        self.wordWrap = dataSection.readBool(b'wordWrap', self.wordWrap)
        self.idealCharactersPerLine = dataSection.readInt(b'idealCharactersPerLine', self.idealCharactersPerLine)
        fonts = dataSection.readStrings(b'autoFont')
        if len(fonts) > 0:
            self.autoSelectionFonts = fonts
        return

    def appendLine(self, str, colour=(255, 255, 255, 255)):
        io = StringIO.StringIO(_packColourTag(colour) + unicode(str))
        newLines = [unicode(x).rstrip() for x in io.readlines()]
        if len(newLines) + len(self.lines) >= self.maxLines:
            diff = self.maxLines - len(self.lines)
            self.lines = self.lines[diff:]
        self.lines.extend(newLines)
        self._refillBuffer()
        if self.scrollIndex > 0:
            self.setScrollIndex(self.scrollIndex + len(newLines))
        return

    def onRecreateDevice(self):
        self._selectFontBestMatch()
        return

    def _refillBuffer(self):
        widthInPixels = self._widthInPixels()
        wrappedLines = []
        for x in self.lines:
            wrappedLines.extend(_wrapLine(x, widthInPixels, self.component.text))

        buffer = b'\n' + (b'\n').join(wrappedLines)
        self.component.text.text = buffer
        self._displayedLineCount = len(wrappedLines)
        self._recalcMaxScroll()
        self._updateScroll()
        return

    def _recalcMaxScroll(self):
        totalPixelHeight = self._lineHeight * self._displayedLineCount
        self.component.minScroll.y = -totalPixelHeight / (BigWorld.screenHeight() * 0.5)
        return

    def _recalcFontMetrics(self):
        _, self._lineHeight = self.component.text.stringDimensions(b'W')
        return

    def _widthInPixels(self):
        widthMode = self.component.widthMode
        self.component.widthMode = GUI.Simple.eSizeMode.PIXEL
        w = self.component.width
        self.component.widthMode = widthMode
        return w / getHPixelScalar()

    def _updateScroll(self):
        self.component.scroll.y = -self.scrollIndex * (self._lineHeight / (BigWorld.screenHeight() * 0.5))
        return

    def _selectFontBestMatch(self):
        selectedFont = Utils.autoSelectFont(self.autoSelectionFonts, self.idealCharactersPerLine, self._widthInPixels(), self.component.text)
        self.component.text.font = selectedFont
        self._recalcFontMetrics()
        self._recalcMaxScroll()
        self._refillBuffer()
        return

    @staticmethod
    def test():
        global testUI
        for x in GUI.roots():
            GUI.delRoot(x)

        testUI = ScrollableText().component
        GUI.addRoot(testUI)
        testUI.script.appendLine(b'AAAA\nBBBB\\CCCC\nDDDD')
        testUI.script.appendLine(b'XYZ')
        testUI.script.appendLine(b'ABCD')
        testUI.script.appendLine(b'EFG')
        testUI.script.appendLine(b'HIJKL')
        testUI.script.appendLine(b'VRRRRFRF')
        testUI.script.appendLine(b'\\cFF0000FF;test one two three four')
        testUI.script.appendLine(b'\\c00FF00FF;the fat cat sat on the MAT')
        testUI.script.appendLine(b'\\c0000FFFF;The quick brown fox jumped over the lazy dog')
        return
