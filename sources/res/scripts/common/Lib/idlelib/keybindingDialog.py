from Tkinter import *
import tkMessageBox, string, sys

class GetKeysDialog(Toplevel):

    def __init__(self, parent, title, action, currentKeySequences, _htest=False):
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        self.resizable(height=FALSE, width=FALSE)
        self.title(title)
        self.transient(parent)
        self.grab_set()
        self.protocol(b'WM_DELETE_WINDOW', self.Cancel)
        self.parent = parent
        self.action = action
        self.currentKeySequences = currentKeySequences
        self.result = b''
        self.keyString = StringVar(self)
        self.keyString.set(b'')
        self.SetModifiersForPlatform()
        self.modifier_vars = []
        for modifier in self.modifiers:
            variable = StringVar(self)
            variable.set(b'')
            self.modifier_vars.append(variable)

        self.advanced = False
        self.CreateWidgets()
        self.LoadFinalKeyList()
        self.withdraw()
        self.update_idletasks()
        self.geometry(b'+%d+%d' % (
         parent.winfo_rootx() + (parent.winfo_width() / 2 - self.winfo_reqwidth() / 2),
         parent.winfo_rooty() + ((_htest or parent.winfo_height() / 2) - self.winfo_reqheight() / 2 if 1 else 150)))
        self.deiconify()
        self.wait_window()
        return

    def CreateWidgets(self):
        frameMain = Frame(self, borderwidth=2, relief=SUNKEN)
        frameMain.pack(side=TOP, expand=TRUE, fill=BOTH)
        frameButtons = Frame(self)
        frameButtons.pack(side=BOTTOM, fill=X)
        self.buttonOK = Button(frameButtons, text=b'OK', width=8, command=self.OK)
        self.buttonOK.grid(row=0, column=0, padx=5, pady=5)
        self.buttonCancel = Button(frameButtons, text=b'Cancel', width=8, command=self.Cancel)
        self.buttonCancel.grid(row=0, column=1, padx=5, pady=5)
        self.frameKeySeqBasic = Frame(frameMain)
        self.frameKeySeqAdvanced = Frame(frameMain)
        self.frameControlsBasic = Frame(frameMain)
        self.frameHelpAdvanced = Frame(frameMain)
        self.frameKeySeqAdvanced.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)
        self.frameKeySeqBasic.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)
        self.frameKeySeqBasic.lift()
        self.frameHelpAdvanced.grid(row=1, column=0, sticky=NSEW, padx=5)
        self.frameControlsBasic.grid(row=1, column=0, sticky=NSEW, padx=5)
        self.frameControlsBasic.lift()
        self.buttonLevel = Button(frameMain, command=self.ToggleLevel, text=b'Advanced Key Binding Entry >>')
        self.buttonLevel.grid(row=2, column=0, stick=EW, padx=5, pady=5)
        labelTitleBasic = Label(self.frameKeySeqBasic, text=b"New keys for  '" + self.action + b"' :")
        labelTitleBasic.pack(anchor=W)
        labelKeysBasic = Label(self.frameKeySeqBasic, justify=LEFT, textvariable=self.keyString, relief=GROOVE, borderwidth=2)
        labelKeysBasic.pack(ipadx=5, ipady=5, fill=X)
        self.modifier_checkbuttons = {}
        column = 0
        for modifier, variable in zip(self.modifiers, self.modifier_vars):
            label = self.modifier_label.get(modifier, modifier)
            check = Checkbutton(self.frameControlsBasic, command=self.BuildKeyString, text=label, variable=variable, onvalue=modifier, offvalue=b'')
            check.grid(row=0, column=column, padx=2, sticky=W)
            self.modifier_checkbuttons[modifier] = check
            column += 1

        labelFnAdvice = Label(self.frameControlsBasic, justify=LEFT, text=b'Select the desired modifier keys\n' + b'above, and the final key from the\n' + b'list on the right.\n\n' + b'Use upper case Symbols when using\n' + b'the Shift modifier.  (Letters will be\n' + b'converted automatically.)')
        labelFnAdvice.grid(row=1, column=0, columnspan=4, padx=2, sticky=W)
        self.listKeysFinal = Listbox(self.frameControlsBasic, width=15, height=10, selectmode=SINGLE)
        self.listKeysFinal.bind(b'<ButtonRelease-1>', self.FinalKeySelected)
        self.listKeysFinal.grid(row=0, column=4, rowspan=4, sticky=NS)
        scrollKeysFinal = Scrollbar(self.frameControlsBasic, orient=VERTICAL, command=self.listKeysFinal.yview)
        self.listKeysFinal.config(yscrollcommand=scrollKeysFinal.set)
        scrollKeysFinal.grid(row=0, column=5, rowspan=4, sticky=NS)
        self.buttonClear = Button(self.frameControlsBasic, text=b'Clear Keys', command=self.ClearKeySeq)
        self.buttonClear.grid(row=2, column=0, columnspan=4)
        labelTitleAdvanced = Label(self.frameKeySeqAdvanced, justify=LEFT, text=b"Enter new binding(s) for  '" + self.action + b"' :\n" + b'(These bindings will not be checked for validity!)')
        labelTitleAdvanced.pack(anchor=W)
        self.entryKeysAdvanced = Entry(self.frameKeySeqAdvanced, textvariable=self.keyString)
        self.entryKeysAdvanced.pack(fill=X)
        labelHelpAdvanced = Label(self.frameHelpAdvanced, justify=LEFT, text=b'Key bindings are specified using Tkinter keysyms as\n' + b'in these samples: <Control-f>, <Shift-F2>, <F12>,\n<Control-space>, <Meta-less>, <Control-Alt-Shift-X>.\nUpper case is used when the Shift modifier is present!\n\n' + b"'Emacs style' multi-keystroke bindings are specified as\n" + b'follows: <Control-x><Control-y>, where the first key\n' + b"is the 'do-nothing' keybinding.\n\n" + b'Multiple separate bindings for one action should be\n' + b'separated by a space, eg., <Alt-v> <Meta-v>.')
        labelHelpAdvanced.grid(row=0, column=0, sticky=NSEW)
        return

    def SetModifiersForPlatform(self):
        if sys.platform == b'darwin':
            self.modifiers = [
             b'Shift', b'Control', b'Option', b'Command']
        else:
            self.modifiers = [
             b'Control', b'Alt', b'Shift']
        self.modifier_label = {b'Control': b'Ctrl'}
        return

    def ToggleLevel(self):
        if self.buttonLevel.cget(b'text')[:8] == b'Advanced':
            self.ClearKeySeq()
            self.buttonLevel.config(text=b'<< Basic Key Binding Entry')
            self.frameKeySeqAdvanced.lift()
            self.frameHelpAdvanced.lift()
            self.entryKeysAdvanced.focus_set()
            self.advanced = True
        else:
            self.ClearKeySeq()
            self.buttonLevel.config(text=b'Advanced Key Binding Entry >>')
            self.frameKeySeqBasic.lift()
            self.frameControlsBasic.lift()
            self.advanced = False
        return

    def FinalKeySelected(self, event):
        self.BuildKeyString()
        return

    def BuildKeyString(self):
        keyList = modifiers = self.GetModifiers()
        finalKey = self.listKeysFinal.get(ANCHOR)
        if finalKey:
            finalKey = self.TranslateKey(finalKey, modifiers)
            keyList.append(finalKey)
        self.keyString.set(b'<' + string.join(keyList, b'-') + b'>')
        return

    def GetModifiers(self):
        modList = [variable.get() for variable in self.modifier_vars]
        return [mod for mod in modList if mod]

    def ClearKeySeq(self):
        self.listKeysFinal.select_clear(0, END)
        self.listKeysFinal.yview(MOVETO, b'0.0')
        for variable in self.modifier_vars:
            variable.set(b'')

        self.keyString.set(b'')
        return

    def LoadFinalKeyList(self):
        self.functionKeys = (b'F1', b'F2', b'F3', b'F4', b'F5', b'F6', b'F7', b'F8', b'F9', b'F10', b'F11', b'F12')
        self.alphanumKeys = tuple(string.ascii_lowercase + string.digits)
        self.punctuationKeys = tuple(b'~!@#%^&*()_-+={}[]|;:,.<>/?')
        self.whitespaceKeys = (b'Tab', b'Space', b'Return')
        self.editKeys = (b'BackSpace', b'Delete', b'Insert')
        self.moveKeys = (b'Home', b'End', b'Page Up', b'Page Down', b'Left Arrow', b'Right Arrow', b'Up Arrow', b'Down Arrow')
        keys = self.alphanumKeys + self.punctuationKeys + self.functionKeys + self.whitespaceKeys + self.editKeys + self.moveKeys
        self.listKeysFinal.insert(END, *keys)
        return

    def TranslateKey(self, key, modifiers):
        translateDict = {b'Space': b'space', b'~': b'asciitilde', 
           b'!': b'exclam', b'@': b'at', b'#': b'numbersign', b'%': b'percent', 
           b'^': b'asciicircum', b'&': b'ampersand', b'*': b'asterisk', b'(': b'parenleft', 
           b')': b'parenright', b'_': b'underscore', b'-': b'minus', b'+': b'plus', 
           b'=': b'equal', b'{': b'braceleft', b'}': b'braceright', b'[': b'bracketleft', 
           b']': b'bracketright', b'|': b'bar', b';': b'semicolon', b':': b'colon', 
           b',': b'comma', b'.': b'period', b'<': b'less', b'>': b'greater', b'/': b'slash', 
           b'?': b'question', b'Page Up': b'Prior', b'Page Down': b'Next', b'Left Arrow': b'Left', 
           b'Right Arrow': b'Right', b'Up Arrow': b'Up', b'Down Arrow': b'Down', 
           b'Tab': b'Tab'}
        if key in translateDict.keys():
            key = translateDict[key]
        if b'Shift' in modifiers and key in string.ascii_lowercase:
            key = key.upper()
        key = b'Key-' + key
        return key

    def OK(self, event=None):
        if self.advanced or self.KeysOK():
            self.result = self.keyString.get()
            self.grab_release()
            self.destroy()
        return

    def Cancel(self, event=None):
        self.result = b''
        self.grab_release()
        self.destroy()
        return

    def KeysOK(self):
        keys = self.keyString.get()
        keys.strip()
        finalKey = self.listKeysFinal.get(ANCHOR)
        modifiers = self.GetModifiers()
        keySequence = keys.split()
        keysOK = False
        title = b'Key Sequence Error'
        if not keys:
            tkMessageBox.showerror(title=title, parent=self, message=b'No keys specified.')
        elif not keys.endswith(b'>'):
            tkMessageBox.showerror(title=title, parent=self, message=b'Missing the final Key')
        elif not modifiers and finalKey not in self.functionKeys + self.moveKeys:
            tkMessageBox.showerror(title=title, parent=self, message=b'No modifier key(s) specified.')
        elif modifiers == [b'Shift'] and finalKey not in self.functionKeys + self.moveKeys + (b'Tab', b'Space'):
            msg = b'The shift modifier by itself may not be used with this key symbol.'
            tkMessageBox.showerror(title=title, parent=self, message=msg)
        elif keySequence in self.currentKeySequences:
            msg = b'This key combination is already in use.'
            tkMessageBox.showerror(title=title, parent=self, message=msg)
        else:
            keysOK = True
        return keysOK


if __name__ == b'__main__':
    from idlelib.idle_test.htest import run
    run(GetKeysDialog)
