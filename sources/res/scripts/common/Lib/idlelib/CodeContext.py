import Tkinter
from Tkconstants import TOP, LEFT, X, W, SUNKEN
import re
from sys import maxint as INFINITY
from idlelib.configHandler import idleConf
BLOCKOPENERS = {
 5, 6, 7, 8, 9, 10, 11, 
 12, 13, 14, 15}
UPDATEINTERVAL = 100
FONTUPDATEINTERVAL = 1000
getspacesfirstword = lambda s, c=re.compile(b'^(\\s*)(\\w*)'): c.match(s).groups()

class CodeContext:
    menudefs = [
     (
      b'options', [(b'!Code Conte_xt', b'<<toggle-code-context>>')])]
    context_depth = idleConf.GetOption(b'extensions', b'CodeContext', b'numlines', type=b'int', default=3)
    bgcolor = idleConf.GetOption(b'extensions', b'CodeContext', b'bgcolor', type=b'str', default=b'LightGray')
    fgcolor = idleConf.GetOption(b'extensions', b'CodeContext', b'fgcolor', type=b'str', default=b'Black')

    def __init__(self, editwin):
        self.editwin = editwin
        self.text = editwin.text
        self.textfont = self.text[b'font']
        self.label = None
        self.info = [
         (
          0, -1, b'', False)]
        self.topvisible = 1
        visible = idleConf.GetOption(b'extensions', b'CodeContext', b'visible', type=b'bool', default=False)
        if visible:
            self.toggle_code_context_event()
            self.editwin.setvar(b'<<toggle-code-context>>', True)
        self.text.after(UPDATEINTERVAL, self.timer_event)
        self.text.after(FONTUPDATEINTERVAL, self.font_timer_event)
        return

    def toggle_code_context_event(self, event=None):
        if not self.label:
            widgets = (
             self.editwin.text, self.editwin.text_frame)
            padx = 0
            for widget in widgets:
                padx += int(str(widget.pack_info()[b'padx']))
                padx += int(str(widget.cget(b'padx')))

            border = 0
            for widget in widgets:
                border += int(str(widget.cget(b'border')))

            self.label = Tkinter.Label(self.editwin.top, text=b'\n' * (self.context_depth - 1), anchor=W, justify=LEFT, font=self.textfont, bg=self.bgcolor, fg=self.fgcolor, width=1, padx=padx, border=border, relief=SUNKEN)
            self.label.pack(side=TOP, fill=X, expand=False, before=self.editwin.text_frame)
        else:
            self.label.destroy()
            self.label = None
        idleConf.SetOption(b'extensions', b'CodeContext', b'visible', str(self.label is not None))
        idleConf.SaveUserCfgFiles()
        return

    def get_line_info(self, linenum):
        text = self.text.get(b'%d.0' % linenum, b'%d.end' % linenum)
        spaces, firstword = getspacesfirstword(text)
        opener = firstword in BLOCKOPENERS and firstword
        if len(text) == len(spaces) or text[len(spaces)] == b'#':
            indent = INFINITY
        else:
            indent = len(spaces)
        return (
         indent, text, opener)

    def get_context(self, new_topvisible, stopline=1, stopindent=0):
        lines = []
        lastindent = INFINITY
        for linenum in xrange(new_topvisible, stopline - 1, -1):
            indent, text, opener = self.get_line_info(linenum)
            if indent < lastindent:
                lastindent = indent
                if opener in (b'else', b'elif'):
                    lastindent += 1
                if opener and linenum < new_topvisible and indent >= stopindent:
                    lines.append((linenum, indent, text, opener))
                if lastindent <= stopindent:
                    break

        lines.reverse()
        return (lines, lastindent)

    def update_code_context(self):
        new_topvisible = int(self.text.index(b'@0,0').split(b'.')[0])
        if self.topvisible == new_topvisible:
            return
        if self.topvisible < new_topvisible:
            lines, lastindent = self.get_context(new_topvisible, self.topvisible)
            while self.info[-1][1] >= lastindent:
                del self.info[-1]

        elif self.topvisible > new_topvisible:
            stopindent = self.info[-1][1] + 1
            while self.info[-1][0] >= new_topvisible:
                stopindent = self.info[-1][1]
                del self.info[-1]

            lines, lastindent = self.get_context(new_topvisible, self.info[-1][0] + 1, stopindent)
        self.info.extend(lines)
        self.topvisible = new_topvisible
        context_strings = [
         b''] * max(0, self.context_depth - len(self.info))
        context_strings += [x[2] for x in self.info[-self.context_depth:]]
        self.label[b'text'] = (b'\n').join(context_strings)
        return

    def timer_event(self):
        if self.label:
            self.update_code_context()
        self.text.after(UPDATEINTERVAL, self.timer_event)
        return

    def font_timer_event(self):
        newtextfont = self.text[b'font']
        if self.label and newtextfont != self.textfont:
            self.textfont = newtextfont
            self.label[b'font'] = self.textfont
        self.text.after(FONTUPDATEINTERVAL, self.font_timer_event)
        return
