from Tkinter import *
import tkMessageBox, tkColorChooser, tkFont
from idlelib.configHandler import idleConf
from idlelib.dynOptionMenuWidget import DynOptionMenu
from idlelib.keybindingDialog import GetKeysDialog
from idlelib.configSectionNameDialog import GetCfgSectionNameDialog
from idlelib.configHelpSourceEdit import GetHelpSourceDialog
from idlelib.tabbedpages import TabbedPageSet
from idlelib.textView import view_text
from idlelib import macosxSupport

class ConfigDialog(Toplevel):

    def __init__(self, parent, title=b'', _htest=False, _utest=False):
        Toplevel.__init__(self, parent)
        self.parent = parent
        if _htest:
            parent.instance_dict = {}
        self.wm_withdraw()
        self.configure(borderwidth=5)
        self.title(title or b'IDLE Preferences')
        self.geometry(b'+%d+%d' % (parent.winfo_rootx() + 20,
         parent.winfo_rooty() + (30 if not _htest else 150)))
        self.themeElements = {b'Normal Text': (b'normal', b'00'), 
           b'Python Keywords': (b'keyword', b'01'), 
           b'Python Definitions': (b'definition', b'02'), 
           b'Python Builtins': (b'builtin', b'03'), 
           b'Python Comments': (b'comment', b'04'), 
           b'Python Strings': (b'string', b'05'), 
           b'Selected Text': (b'hilite', b'06'), 
           b'Found Text': (b'hit', b'07'), 
           b'Cursor': (b'cursor', b'08'), 
           b'Editor Breakpoint': (b'break', b'09'), 
           b'Shell Normal Text': (b'console', b'10'), 
           b'Shell Error Text': (b'error', b'11'), 
           b'Shell Stdout Text': (b'stdout', b'12'), 
           b'Shell Stderr Text': (b'stderr', b'13')}
        self.ResetChangedItems()
        self.CreateWidgets()
        self.resizable(height=FALSE, width=FALSE)
        self.transient(parent)
        self.grab_set()
        self.protocol(b'WM_DELETE_WINDOW', self.Cancel)
        self.tabPages.focus_set()
        self.LoadConfigs()
        self.AttachVarCallbacks()
        if not _utest:
            self.wm_deiconify()
            self.wait_window()
        return

    def CreateWidgets(self):
        self.tabPages = TabbedPageSet(self, page_names=[
         2, 3, 4, 5, 
         6])
        self.tabPages.pack(side=TOP, expand=TRUE, fill=BOTH)
        self.CreatePageFontTab()
        self.CreatePageHighlight()
        self.CreatePageKeys()
        self.CreatePageGeneral()
        self.CreatePageExtensions()
        self.create_action_buttons().pack(side=BOTTOM)
        return

    def create_action_buttons(self):
        if macosxSupport.isAquaTk():
            paddingArgs = {}
        else:
            paddingArgs = {b'padx': 6, b'pady': 3}
        outer = Frame(self, pady=2)
        buttons = Frame(outer, pady=2)
        for txt, cmd in (
         (
          b'Ok', self.Ok),
         (
          b'Apply', self.Apply),
         (
          b'Cancel', self.Cancel),
         (
          b'Help', self.Help)):
            Button(buttons, text=txt, command=cmd, takefocus=FALSE, **paddingArgs).pack(side=LEFT, padx=5)

        Frame(outer, height=2, borderwidth=0).pack(side=TOP)
        buttons.pack(side=BOTTOM)
        return outer

    def CreatePageFontTab(self):
        parent = self.parent
        self.fontSize = StringVar(parent)
        self.fontBold = BooleanVar(parent)
        self.fontName = StringVar(parent)
        self.spaceNum = IntVar(parent)
        self.editFont = tkFont.Font(parent, (b'courier', 10, b'normal'))
        frame = self.tabPages.pages[b'Fonts/Tabs'].frame
        frameFont = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Base Editor Font ')
        frameIndent = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Indentation Width ')
        frameFontName = Frame(frameFont)
        frameFontParam = Frame(frameFont)
        labelFontNameTitle = Label(frameFontName, justify=LEFT, text=b'Font Face :')
        self.listFontName = Listbox(frameFontName, height=5, takefocus=FALSE, exportselection=FALSE)
        self.listFontName.bind(b'<ButtonRelease-1>', self.OnListFontButtonRelease)
        scrollFont = Scrollbar(frameFontName)
        scrollFont.config(command=self.listFontName.yview)
        self.listFontName.config(yscrollcommand=scrollFont.set)
        labelFontSizeTitle = Label(frameFontParam, text=b'Size :')
        self.optMenuFontSize = DynOptionMenu(frameFontParam, self.fontSize, None, command=self.SetFontSample)
        checkFontBold = Checkbutton(frameFontParam, variable=self.fontBold, onvalue=1, offvalue=0, text=b'Bold', command=self.SetFontSample)
        frameFontSample = Frame(frameFont, relief=SOLID, borderwidth=1)
        self.labelFontSample = Label(frameFontSample, justify=LEFT, font=self.editFont, text=b'AaBbCcDdEe\nFfGgHhIiJjK\n1234567890\n#:+=(){}[]')
        frameIndentSize = Frame(frameIndent)
        labelSpaceNumTitle = Label(frameIndentSize, justify=LEFT, text=b'Python Standard: 4 Spaces!')
        self.scaleSpaceNum = Scale(frameIndentSize, variable=self.spaceNum, orient=b'horizontal', tickinterval=2, from_=2, to=16)
        frameFont.pack(side=LEFT, padx=5, pady=5, expand=TRUE, fill=BOTH)
        frameIndent.pack(side=LEFT, padx=5, pady=5, fill=Y)
        frameFontName.pack(side=TOP, padx=5, pady=5, fill=X)
        frameFontParam.pack(side=TOP, padx=5, pady=5, fill=X)
        labelFontNameTitle.pack(side=TOP, anchor=W)
        self.listFontName.pack(side=LEFT, expand=TRUE, fill=X)
        scrollFont.pack(side=LEFT, fill=Y)
        labelFontSizeTitle.pack(side=LEFT, anchor=W)
        self.optMenuFontSize.pack(side=LEFT, anchor=W)
        checkFontBold.pack(side=LEFT, anchor=W, padx=20)
        frameFontSample.pack(side=TOP, padx=5, pady=5, expand=TRUE, fill=BOTH)
        self.labelFontSample.pack(expand=TRUE, fill=BOTH)
        frameIndentSize.pack(side=TOP, fill=X)
        labelSpaceNumTitle.pack(side=TOP, anchor=W, padx=5)
        self.scaleSpaceNum.pack(side=TOP, padx=5, fill=X)
        return frame

    def CreatePageHighlight(self):
        parent = self.parent
        self.builtinTheme = StringVar(parent)
        self.customTheme = StringVar(parent)
        self.fgHilite = BooleanVar(parent)
        self.colour = StringVar(parent)
        self.fontName = StringVar(parent)
        self.themeIsBuiltin = BooleanVar(parent)
        self.highlightTarget = StringVar(parent)
        frame = self.tabPages.pages[b'Highlighting'].frame
        frameCustom = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Custom Highlighting ')
        frameTheme = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Highlighting Theme ')
        self.textHighlightSample = Text(frameCustom, relief=SOLID, borderwidth=1, font=(b'courier', 12, b''), cursor=b'hand2', width=21, height=11, takefocus=FALSE, highlightthickness=0, wrap=NONE)
        text = self.textHighlightSample
        text.bind(b'<Double-Button-1>', (lambda e: b'break'))
        text.bind(b'<B1-Motion>', (lambda e: b'break'))
        textAndTags = (
         (b'#you can click here', b'comment'), (b'\n', b'normal'),
         (b'#to choose items', b'comment'), (b'\n', b'normal'),
         (b'def', b'keyword'), (b' ', b'normal'),
         (b'func', b'definition'), (b'(param):\n  ', b'normal'),
         (b'"""string"""', b'string'), (b'\n  var0 = ', b'normal'),
         (b"'string'", b'string'), (b'\n  var1 = ', b'normal'),
         (b"'selected'", b'hilite'), (b'\n  var2 = ', b'normal'),
         (b"'found'", b'hit'), (b'\n  var3 = ', b'normal'),
         (b'list', b'builtin'), (b'(', b'normal'),
         (b'None', b'builtin'), (b')\n', b'normal'),
         (b'  breakpoint("line")', b'break'), (b'\n\n', b'normal'),
         (b' error ', b'error'), (b' ', b'normal'),
         (b'cursor |', b'cursor'), (b'\n ', b'normal'),
         (b'shell', b'console'), (b' ', b'normal'),
         (b'stdout', b'stdout'), (b' ', b'normal'),
         (b'stderr', b'stderr'), (b'\n', b'normal'))
        for txTa in textAndTags:
            text.insert(END, txTa[0], txTa[1])

        for element in self.themeElements:

            def tem(event, elem=element):
                event.widget.winfo_toplevel().highlightTarget.set(elem)
                return

            text.tag_bind(self.themeElements[element][0], b'<ButtonPress-1>', tem)

        text.config(state=DISABLED)
        self.frameColourSet = Frame(frameCustom, relief=SOLID, borderwidth=1)
        frameFgBg = Frame(frameCustom)
        buttonSetColour = Button(self.frameColourSet, text=b'Choose Colour for :', command=self.GetColour, highlightthickness=0)
        self.optMenuHighlightTarget = DynOptionMenu(self.frameColourSet, self.highlightTarget, None, highlightthickness=0)
        self.radioFg = Radiobutton(frameFgBg, variable=self.fgHilite, value=1, text=b'Foreground', command=self.SetColourSampleBinding)
        self.radioBg = Radiobutton(frameFgBg, variable=self.fgHilite, value=0, text=b'Background', command=self.SetColourSampleBinding)
        self.fgHilite.set(1)
        buttonSaveCustomTheme = Button(frameCustom, text=b'Save as New Custom Theme', command=self.SaveAsNewTheme)
        labelTypeTitle = Label(frameTheme, text=b'Select : ')
        self.radioThemeBuiltin = Radiobutton(frameTheme, variable=self.themeIsBuiltin, value=1, command=self.SetThemeType, text=b'a Built-in Theme')
        self.radioThemeCustom = Radiobutton(frameTheme, variable=self.themeIsBuiltin, value=0, command=self.SetThemeType, text=b'a Custom Theme')
        self.optMenuThemeBuiltin = DynOptionMenu(frameTheme, self.builtinTheme, None, command=None)
        self.optMenuThemeCustom = DynOptionMenu(frameTheme, self.customTheme, None, command=None)
        self.buttonDeleteCustomTheme = Button(frameTheme, text=b'Delete Custom Theme', command=self.DeleteCustomTheme)
        self.new_custom_theme = Label(frameTheme, bd=2)
        frameCustom.pack(side=LEFT, padx=5, pady=5, expand=TRUE, fill=BOTH)
        frameTheme.pack(side=LEFT, padx=5, pady=5, fill=Y)
        self.frameColourSet.pack(side=TOP, padx=5, pady=5, expand=TRUE, fill=X)
        frameFgBg.pack(side=TOP, padx=5, pady=0)
        self.textHighlightSample.pack(side=TOP, padx=5, pady=5, expand=TRUE, fill=BOTH)
        buttonSetColour.pack(side=TOP, expand=TRUE, fill=X, padx=8, pady=4)
        self.optMenuHighlightTarget.pack(side=TOP, expand=TRUE, fill=X, padx=8, pady=3)
        self.radioFg.pack(side=LEFT, anchor=E)
        self.radioBg.pack(side=RIGHT, anchor=W)
        buttonSaveCustomTheme.pack(side=BOTTOM, fill=X, padx=5, pady=5)
        labelTypeTitle.pack(side=TOP, anchor=W, padx=5, pady=5)
        self.radioThemeBuiltin.pack(side=TOP, anchor=W, padx=5)
        self.radioThemeCustom.pack(side=TOP, anchor=W, padx=5, pady=2)
        self.optMenuThemeBuiltin.pack(side=TOP, fill=X, padx=5, pady=5)
        self.optMenuThemeCustom.pack(side=TOP, fill=X, anchor=W, padx=5, pady=5)
        self.buttonDeleteCustomTheme.pack(side=TOP, fill=X, padx=5, pady=5)
        self.new_custom_theme.pack(side=TOP, fill=X, pady=5)
        return frame

    def CreatePageKeys(self):
        parent = self.parent
        self.bindingTarget = StringVar(parent)
        self.builtinKeys = StringVar(parent)
        self.customKeys = StringVar(parent)
        self.keysAreBuiltin = BooleanVar(parent)
        self.keyBinding = StringVar(parent)
        frame = self.tabPages.pages[b'Keys'].frame
        frameCustom = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Custom Key Bindings ')
        frameKeySets = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Key Set ')
        frameTarget = Frame(frameCustom)
        labelTargetTitle = Label(frameTarget, text=b'Action - Key(s)')
        scrollTargetY = Scrollbar(frameTarget)
        scrollTargetX = Scrollbar(frameTarget, orient=HORIZONTAL)
        self.listBindings = Listbox(frameTarget, takefocus=FALSE, exportselection=FALSE)
        self.listBindings.bind(b'<ButtonRelease-1>', self.KeyBindingSelected)
        scrollTargetY.config(command=self.listBindings.yview)
        scrollTargetX.config(command=self.listBindings.xview)
        self.listBindings.config(yscrollcommand=scrollTargetY.set)
        self.listBindings.config(xscrollcommand=scrollTargetX.set)
        self.buttonNewKeys = Button(frameCustom, text=b'Get New Keys for Selection', command=self.GetNewKeys, state=DISABLED)
        frames = [Frame(frameKeySets, padx=2, pady=2, borderwidth=0) for i in range(2)]
        self.radioKeysBuiltin = Radiobutton(frames[0], variable=self.keysAreBuiltin, value=1, command=self.SetKeysType, text=b'Use a Built-in Key Set')
        self.radioKeysCustom = Radiobutton(frames[0], variable=self.keysAreBuiltin, value=0, command=self.SetKeysType, text=b'Use a Custom Key Set')
        self.optMenuKeysBuiltin = DynOptionMenu(frames[0], self.builtinKeys, None, command=None)
        self.optMenuKeysCustom = DynOptionMenu(frames[0], self.customKeys, None, command=None)
        self.buttonDeleteCustomKeys = Button(frames[1], text=b'Delete Custom Key Set', command=self.DeleteCustomKeys)
        buttonSaveCustomKeys = Button(frames[1], text=b'Save as New Custom Key Set', command=self.SaveAsNewKeySet)
        frameCustom.pack(side=BOTTOM, padx=5, pady=5, expand=TRUE, fill=BOTH)
        frameKeySets.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH)
        self.buttonNewKeys.pack(side=BOTTOM, fill=X, padx=5, pady=5)
        frameTarget.pack(side=LEFT, padx=5, pady=5, expand=TRUE, fill=BOTH)
        frameTarget.columnconfigure(0, weight=1)
        frameTarget.rowconfigure(1, weight=1)
        labelTargetTitle.grid(row=0, column=0, columnspan=2, sticky=W)
        self.listBindings.grid(row=1, column=0, sticky=NSEW)
        scrollTargetY.grid(row=1, column=1, sticky=NS)
        scrollTargetX.grid(row=2, column=0, sticky=EW)
        self.radioKeysBuiltin.grid(row=0, column=0, sticky=W + NS)
        self.radioKeysCustom.grid(row=1, column=0, sticky=W + NS)
        self.optMenuKeysBuiltin.grid(row=0, column=1, sticky=NSEW)
        self.optMenuKeysCustom.grid(row=1, column=1, sticky=NSEW)
        self.buttonDeleteCustomKeys.pack(side=LEFT, fill=X, expand=True, padx=2)
        buttonSaveCustomKeys.pack(side=LEFT, fill=X, expand=True, padx=2)
        frames[0].pack(side=TOP, fill=BOTH, expand=True)
        frames[1].pack(side=TOP, fill=X, expand=True, pady=2)
        return frame

    def CreatePageGeneral(self):
        parent = self.parent
        self.winWidth = StringVar(parent)
        self.winHeight = StringVar(parent)
        self.startupEdit = IntVar(parent)
        self.autoSave = IntVar(parent)
        self.encoding = StringVar(parent)
        self.userHelpBrowser = BooleanVar(parent)
        self.helpBrowser = StringVar(parent)
        frame = self.tabPages.pages[b'General'].frame
        frameRun = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Startup Preferences ')
        frameSave = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Autosave Preferences ')
        frameWinSize = Frame(frame, borderwidth=2, relief=GROOVE)
        frameEncoding = Frame(frame, borderwidth=2, relief=GROOVE)
        frameHelp = LabelFrame(frame, borderwidth=2, relief=GROOVE, text=b' Additional Help Sources ')
        labelRunChoiceTitle = Label(frameRun, text=b'At Startup')
        radioStartupEdit = Radiobutton(frameRun, variable=self.startupEdit, value=1, command=self.SetKeysType, text=b'Open Edit Window')
        radioStartupShell = Radiobutton(frameRun, variable=self.startupEdit, value=0, command=self.SetKeysType, text=b'Open Shell Window')
        labelRunSaveTitle = Label(frameSave, text=b'At Start of Run (F5)  ')
        radioSaveAsk = Radiobutton(frameSave, variable=self.autoSave, value=0, command=self.SetKeysType, text=b'Prompt to Save')
        radioSaveAuto = Radiobutton(frameSave, variable=self.autoSave, value=1, command=self.SetKeysType, text=b'No Prompt')
        labelWinSizeTitle = Label(frameWinSize, text=b'Initial Window Size  (in characters)')
        labelWinWidthTitle = Label(frameWinSize, text=b'Width')
        entryWinWidth = Entry(frameWinSize, textvariable=self.winWidth, width=3)
        labelWinHeightTitle = Label(frameWinSize, text=b'Height')
        entryWinHeight = Entry(frameWinSize, textvariable=self.winHeight, width=3)
        labelEncodingTitle = Label(frameEncoding, text=b'Default Source Encoding')
        radioEncLocale = Radiobutton(frameEncoding, variable=self.encoding, value=b'locale', text=b'Locale-defined')
        radioEncUTF8 = Radiobutton(frameEncoding, variable=self.encoding, value=b'utf-8', text=b'UTF-8')
        radioEncNone = Radiobutton(frameEncoding, variable=self.encoding, value=b'none', text=b'None')
        frameHelpList = Frame(frameHelp)
        frameHelpListButtons = Frame(frameHelpList)
        scrollHelpList = Scrollbar(frameHelpList)
        self.listHelp = Listbox(frameHelpList, height=5, takefocus=FALSE, exportselection=FALSE)
        scrollHelpList.config(command=self.listHelp.yview)
        self.listHelp.config(yscrollcommand=scrollHelpList.set)
        self.listHelp.bind(b'<ButtonRelease-1>', self.HelpSourceSelected)
        self.buttonHelpListEdit = Button(frameHelpListButtons, text=b'Edit', state=DISABLED, width=8, command=self.HelpListItemEdit)
        self.buttonHelpListAdd = Button(frameHelpListButtons, text=b'Add', width=8, command=self.HelpListItemAdd)
        self.buttonHelpListRemove = Button(frameHelpListButtons, text=b'Remove', state=DISABLED, width=8, command=self.HelpListItemRemove)
        frameRun.pack(side=TOP, padx=5, pady=5, fill=X)
        frameSave.pack(side=TOP, padx=5, pady=5, fill=X)
        frameWinSize.pack(side=TOP, padx=5, pady=5, fill=X)
        frameEncoding.pack(side=TOP, padx=5, pady=5, fill=X)
        frameHelp.pack(side=TOP, padx=5, pady=5, expand=TRUE, fill=BOTH)
        labelRunChoiceTitle.pack(side=LEFT, anchor=W, padx=5, pady=5)
        radioStartupShell.pack(side=RIGHT, anchor=W, padx=5, pady=5)
        radioStartupEdit.pack(side=RIGHT, anchor=W, padx=5, pady=5)
        labelRunSaveTitle.pack(side=LEFT, anchor=W, padx=5, pady=5)
        radioSaveAuto.pack(side=RIGHT, anchor=W, padx=5, pady=5)
        radioSaveAsk.pack(side=RIGHT, anchor=W, padx=5, pady=5)
        labelWinSizeTitle.pack(side=LEFT, anchor=W, padx=5, pady=5)
        entryWinHeight.pack(side=RIGHT, anchor=E, padx=10, pady=5)
        labelWinHeightTitle.pack(side=RIGHT, anchor=E, pady=5)
        entryWinWidth.pack(side=RIGHT, anchor=E, padx=10, pady=5)
        labelWinWidthTitle.pack(side=RIGHT, anchor=E, pady=5)
        labelEncodingTitle.pack(side=LEFT, anchor=W, padx=5, pady=5)
        radioEncNone.pack(side=RIGHT, anchor=E, pady=5)
        radioEncUTF8.pack(side=RIGHT, anchor=E, pady=5)
        radioEncLocale.pack(side=RIGHT, anchor=E, pady=5)
        frameHelpListButtons.pack(side=RIGHT, padx=5, pady=5, fill=Y)
        frameHelpList.pack(side=TOP, padx=5, pady=5, expand=TRUE, fill=BOTH)
        scrollHelpList.pack(side=RIGHT, anchor=W, fill=Y)
        self.listHelp.pack(side=LEFT, anchor=E, expand=TRUE, fill=BOTH)
        self.buttonHelpListEdit.pack(side=TOP, anchor=W, pady=5)
        self.buttonHelpListAdd.pack(side=TOP, anchor=W)
        self.buttonHelpListRemove.pack(side=TOP, anchor=W, pady=5)
        return frame

    def AttachVarCallbacks(self):
        self.fontSize.trace_variable(b'w', self.VarChanged_font)
        self.fontName.trace_variable(b'w', self.VarChanged_font)
        self.fontBold.trace_variable(b'w', self.VarChanged_font)
        self.spaceNum.trace_variable(b'w', self.VarChanged_spaceNum)
        self.colour.trace_variable(b'w', self.VarChanged_colour)
        self.builtinTheme.trace_variable(b'w', self.VarChanged_builtinTheme)
        self.customTheme.trace_variable(b'w', self.VarChanged_customTheme)
        self.themeIsBuiltin.trace_variable(b'w', self.VarChanged_themeIsBuiltin)
        self.highlightTarget.trace_variable(b'w', self.VarChanged_highlightTarget)
        self.keyBinding.trace_variable(b'w', self.VarChanged_keyBinding)
        self.builtinKeys.trace_variable(b'w', self.VarChanged_builtinKeys)
        self.customKeys.trace_variable(b'w', self.VarChanged_customKeys)
        self.keysAreBuiltin.trace_variable(b'w', self.VarChanged_keysAreBuiltin)
        self.winWidth.trace_variable(b'w', self.VarChanged_winWidth)
        self.winHeight.trace_variable(b'w', self.VarChanged_winHeight)
        self.startupEdit.trace_variable(b'w', self.VarChanged_startupEdit)
        self.autoSave.trace_variable(b'w', self.VarChanged_autoSave)
        self.encoding.trace_variable(b'w', self.VarChanged_encoding)
        return

    def remove_var_callbacks(self):
        for var in (
         self.fontSize, self.fontName, self.fontBold,
         self.spaceNum, self.colour, self.builtinTheme,
         self.customTheme, self.themeIsBuiltin, self.highlightTarget,
         self.keyBinding, self.builtinKeys, self.customKeys,
         self.keysAreBuiltin, self.winWidth, self.winHeight,
         self.startupEdit, self.autoSave, self.encoding):
            var.trace_vdelete(b'w', var.trace_vinfo()[0][1])

        return

    def VarChanged_font(self, *params):
        value = self.fontName.get()
        self.AddChangedItem(b'main', b'EditorWindow', b'font', value)
        value = self.fontSize.get()
        self.AddChangedItem(b'main', b'EditorWindow', b'font-size', value)
        value = self.fontBold.get()
        self.AddChangedItem(b'main', b'EditorWindow', b'font-bold', value)
        return

    def VarChanged_spaceNum(self, *params):
        value = self.spaceNum.get()
        self.AddChangedItem(b'main', b'Indent', b'num-spaces', value)
        return

    def VarChanged_colour(self, *params):
        self.OnNewColourSet()
        return

    def VarChanged_builtinTheme(self, *params):
        value = self.builtinTheme.get()
        if value == b'IDLE Dark':
            if idleConf.GetOption(b'main', b'Theme', b'name') != b'IDLE New':
                self.AddChangedItem(b'main', b'Theme', b'name', b'IDLE Classic')
            self.AddChangedItem(b'main', b'Theme', b'name2', value)
            self.new_custom_theme.config(text=b'New theme, see Help', fg=b'#500000')
        else:
            self.AddChangedItem(b'main', b'Theme', b'name', value)
            self.AddChangedItem(b'main', b'Theme', b'name2', b'')
            self.new_custom_theme.config(text=b'', fg=b'black')
        self.PaintThemeSample()
        return

    def VarChanged_customTheme(self, *params):
        value = self.customTheme.get()
        if value != b'- no custom themes -':
            self.AddChangedItem(b'main', b'Theme', b'name', value)
            self.PaintThemeSample()
        return

    def VarChanged_themeIsBuiltin(self, *params):
        value = self.themeIsBuiltin.get()
        self.AddChangedItem(b'main', b'Theme', b'default', value)
        if value:
            self.VarChanged_builtinTheme()
        else:
            self.VarChanged_customTheme()
        return

    def VarChanged_highlightTarget(self, *params):
        self.SetHighlightTarget()
        return

    def VarChanged_keyBinding(self, *params):
        value = self.keyBinding.get()
        keySet = self.customKeys.get()
        event = self.listBindings.get(ANCHOR).split()[0]
        if idleConf.IsCoreBinding(event):
            self.AddChangedItem(b'keys', keySet, event, value)
        else:
            extName = idleConf.GetExtnNameForEvent(event)
            extKeybindSection = extName + b'_cfgBindings'
            self.AddChangedItem(b'extensions', extKeybindSection, event, value)
        return

    def VarChanged_builtinKeys(self, *params):
        value = self.builtinKeys.get()
        self.AddChangedItem(b'main', b'Keys', b'name', value)
        self.LoadKeysList(value)
        return

    def VarChanged_customKeys(self, *params):
        value = self.customKeys.get()
        if value != b'- no custom keys -':
            self.AddChangedItem(b'main', b'Keys', b'name', value)
            self.LoadKeysList(value)
        return

    def VarChanged_keysAreBuiltin(self, *params):
        value = self.keysAreBuiltin.get()
        self.AddChangedItem(b'main', b'Keys', b'default', value)
        if value:
            self.VarChanged_builtinKeys()
        else:
            self.VarChanged_customKeys()
        return

    def VarChanged_winWidth(self, *params):
        value = self.winWidth.get()
        self.AddChangedItem(b'main', b'EditorWindow', b'width', value)
        return

    def VarChanged_winHeight(self, *params):
        value = self.winHeight.get()
        self.AddChangedItem(b'main', b'EditorWindow', b'height', value)
        return

    def VarChanged_startupEdit(self, *params):
        value = self.startupEdit.get()
        self.AddChangedItem(b'main', b'General', b'editor-on-startup', value)
        return

    def VarChanged_autoSave(self, *params):
        value = self.autoSave.get()
        self.AddChangedItem(b'main', b'General', b'autosave', value)
        return

    def VarChanged_encoding(self, *params):
        value = self.encoding.get()
        self.AddChangedItem(b'main', b'EditorWindow', b'encoding', value)
        return

    def ResetChangedItems(self):
        self.changedItems = {b'main': {}, b'highlight': {}, b'keys': {}, b'extensions': {}}
        return

    def AddChangedItem(self, typ, section, item, value):
        value = str(value)
        if section not in self.changedItems[typ]:
            self.changedItems[typ][section] = {}
        self.changedItems[typ][section][item] = value
        return

    def GetDefaultItems(self):
        dItems = {b'main': {}, b'highlight': {}, b'keys': {}, b'extensions': {}}
        for configType in dItems:
            sections = idleConf.GetSectionList(b'default', configType)
            for section in sections:
                dItems[configType][section] = {}
                options = idleConf.defaultCfg[configType].GetOptionList(section)
                for option in options:
                    dItems[configType][section][option] = idleConf.defaultCfg[configType].Get(section, option)

        return dItems

    def SetThemeType(self):
        if self.themeIsBuiltin.get():
            self.optMenuThemeBuiltin.config(state=NORMAL)
            self.optMenuThemeCustom.config(state=DISABLED)
            self.buttonDeleteCustomTheme.config(state=DISABLED)
        else:
            self.optMenuThemeBuiltin.config(state=DISABLED)
            self.radioThemeCustom.config(state=NORMAL)
            self.optMenuThemeCustom.config(state=NORMAL)
            self.buttonDeleteCustomTheme.config(state=NORMAL)
        return

    def SetKeysType(self):
        if self.keysAreBuiltin.get():
            self.optMenuKeysBuiltin.config(state=NORMAL)
            self.optMenuKeysCustom.config(state=DISABLED)
            self.buttonDeleteCustomKeys.config(state=DISABLED)
        else:
            self.optMenuKeysBuiltin.config(state=DISABLED)
            self.radioKeysCustom.config(state=NORMAL)
            self.optMenuKeysCustom.config(state=NORMAL)
            self.buttonDeleteCustomKeys.config(state=NORMAL)
        return

    def GetNewKeys(self):
        listIndex = self.listBindings.index(ANCHOR)
        binding = self.listBindings.get(listIndex)
        bindName = binding.split()[0]
        if self.keysAreBuiltin.get():
            currentKeySetName = self.builtinKeys.get()
        else:
            currentKeySetName = self.customKeys.get()
        currentBindings = idleConf.GetCurrentKeySet()
        if currentKeySetName in self.changedItems[b'keys']:
            keySetChanges = self.changedItems[b'keys'][currentKeySetName]
            for event in keySetChanges:
                currentBindings[event] = keySetChanges[event].split()

        currentKeySequences = currentBindings.values()
        newKeys = GetKeysDialog(self, b'Get New Keys', bindName, currentKeySequences).result
        if newKeys:
            if self.keysAreBuiltin.get():
                message = b'Your changes will be saved as a new Custom Key Set. Enter a name for your new Custom Key Set below.'
                newKeySet = self.GetNewKeysName(message)
                if not newKeySet:
                    self.listBindings.select_set(listIndex)
                    self.listBindings.select_anchor(listIndex)
                    return
                self.CreateNewKeySet(newKeySet)
            self.listBindings.delete(listIndex)
            self.listBindings.insert(listIndex, bindName + b' - ' + newKeys)
            self.listBindings.select_set(listIndex)
            self.listBindings.select_anchor(listIndex)
            self.keyBinding.set(newKeys)
        else:
            self.listBindings.select_set(listIndex)
            self.listBindings.select_anchor(listIndex)
        return

    def GetNewKeysName(self, message):
        usedNames = idleConf.GetSectionList(b'user', b'keys') + idleConf.GetSectionList(b'default', b'keys')
        newKeySet = GetCfgSectionNameDialog(self, b'New Custom Key Set', message, usedNames).result
        return newKeySet

    def SaveAsNewKeySet(self):
        newKeysName = self.GetNewKeysName(b'New Key Set Name:')
        if newKeysName:
            self.CreateNewKeySet(newKeysName)
        return

    def KeyBindingSelected(self, event):
        self.buttonNewKeys.config(state=NORMAL)
        return

    def CreateNewKeySet(self, newKeySetName):
        if self.keysAreBuiltin.get():
            prevKeySetName = self.builtinKeys.get()
        else:
            prevKeySetName = self.customKeys.get()
        prevKeys = idleConf.GetCoreKeys(prevKeySetName)
        newKeys = {}
        for event in prevKeys:
            eventName = event[2:-2]
            binding = (b' ').join(prevKeys[event])
            newKeys[eventName] = binding

        if prevKeySetName in self.changedItems[b'keys']:
            keySetChanges = self.changedItems[b'keys'][prevKeySetName]
            for event in keySetChanges:
                newKeys[event] = keySetChanges[event]

        self.SaveNewKeySet(newKeySetName, newKeys)
        customKeyList = idleConf.GetSectionList(b'user', b'keys')
        customKeyList.sort()
        self.optMenuKeysCustom.SetMenu(customKeyList, newKeySetName)
        self.keysAreBuiltin.set(0)
        self.SetKeysType()
        return

    def LoadKeysList(self, keySetName):
        reselect = 0
        newKeySet = 0
        if self.listBindings.curselection():
            reselect = 1
            listIndex = self.listBindings.index(ANCHOR)
        keySet = idleConf.GetKeySet(keySetName)
        bindNames = keySet.keys()
        bindNames.sort()
        self.listBindings.delete(0, END)
        for bindName in bindNames:
            key = (b' ').join(keySet[bindName])
            bindName = bindName[2:-2]
            if keySetName in self.changedItems[b'keys']:
                if bindName in self.changedItems[b'keys'][keySetName]:
                    key = self.changedItems[b'keys'][keySetName][bindName]
            self.listBindings.insert(END, bindName + b' - ' + key)

        if reselect:
            self.listBindings.see(listIndex)
            self.listBindings.select_set(listIndex)
            self.listBindings.select_anchor(listIndex)
        return

    def DeleteCustomKeys(self):
        keySetName = self.customKeys.get()
        delmsg = b'Are you sure you wish to delete the key set %r ?'
        if not tkMessageBox.askyesno(b'Delete Key Set', delmsg % keySetName, parent=self):
            return
        self.DeactivateCurrentConfig()
        idleConf.userCfg[b'keys'].remove_section(keySetName)
        if keySetName in self.changedItems[b'keys']:
            del self.changedItems[b'keys'][keySetName]
        idleConf.userCfg[b'keys'].Save()
        itemList = idleConf.GetSectionList(b'user', b'keys')
        itemList.sort()
        if not itemList:
            self.radioKeysCustom.config(state=DISABLED)
            self.optMenuKeysCustom.SetMenu(itemList, b'- no custom keys -')
        else:
            self.optMenuKeysCustom.SetMenu(itemList, itemList[0])
        self.keysAreBuiltin.set(idleConf.defaultCfg[b'main'].Get(b'Keys', b'default'))
        self.builtinKeys.set(idleConf.defaultCfg[b'main'].Get(b'Keys', b'name'))
        self.SaveAllChangedConfigs()
        self.ActivateConfigChanges()
        self.SetKeysType()
        return

    def DeleteCustomTheme(self):
        themeName = self.customTheme.get()
        delmsg = b'Are you sure you wish to delete the theme %r ?'
        if not tkMessageBox.askyesno(b'Delete Theme', delmsg % themeName, parent=self):
            return
        self.DeactivateCurrentConfig()
        idleConf.userCfg[b'highlight'].remove_section(themeName)
        if themeName in self.changedItems[b'highlight']:
            del self.changedItems[b'highlight'][themeName]
        idleConf.userCfg[b'highlight'].Save()
        itemList = idleConf.GetSectionList(b'user', b'highlight')
        itemList.sort()
        if not itemList:
            self.radioThemeCustom.config(state=DISABLED)
            self.optMenuThemeCustom.SetMenu(itemList, b'- no custom themes -')
        else:
            self.optMenuThemeCustom.SetMenu(itemList, itemList[0])
        self.themeIsBuiltin.set(idleConf.defaultCfg[b'main'].Get(b'Theme', b'default'))
        self.builtinTheme.set(idleConf.defaultCfg[b'main'].Get(b'Theme', b'name'))
        self.SaveAllChangedConfigs()
        self.ActivateConfigChanges()
        self.SetThemeType()
        return

    def GetColour(self):
        target = self.highlightTarget.get()
        prevColour = self.frameColourSet.cget(b'bg')
        rgbTuplet, colourString = tkColorChooser.askcolor(parent=self, title=b'Pick new colour for : ' + target, initialcolor=prevColour)
        if colourString and colourString != prevColour:
            if self.themeIsBuiltin.get():
                message = b'Your changes will be saved as a new Custom Theme. Enter a name for your new Custom Theme below.'
                newTheme = self.GetNewThemeName(message)
                if not newTheme:
                    return
                self.CreateNewTheme(newTheme)
                self.colour.set(colourString)
            else:
                self.colour.set(colourString)
        return

    def OnNewColourSet(self):
        newColour = self.colour.get()
        self.frameColourSet.config(bg=newColour)
        plane = b'foreground' if self.fgHilite.get() else b'background'
        sampleElement = self.themeElements[self.highlightTarget.get()][0]
        self.textHighlightSample.tag_config(sampleElement, **{plane: newColour})
        theme = self.customTheme.get()
        themeElement = sampleElement + b'-' + plane
        self.AddChangedItem(b'highlight', theme, themeElement, newColour)
        return

    def GetNewThemeName(self, message):
        usedNames = idleConf.GetSectionList(b'user', b'highlight') + idleConf.GetSectionList(b'default', b'highlight')
        newTheme = GetCfgSectionNameDialog(self, b'New Custom Theme', message, usedNames).result
        return newTheme

    def SaveAsNewTheme(self):
        newThemeName = self.GetNewThemeName(b'New Theme Name:')
        if newThemeName:
            self.CreateNewTheme(newThemeName)
        return

    def CreateNewTheme(self, newThemeName):
        if self.themeIsBuiltin.get():
            themeType = b'default'
            themeName = self.builtinTheme.get()
        else:
            themeType = b'user'
            themeName = self.customTheme.get()
        newTheme = idleConf.GetThemeDict(themeType, themeName)
        if themeName in self.changedItems[b'highlight']:
            themeChanges = self.changedItems[b'highlight'][themeName]
            for element in themeChanges:
                newTheme[element] = themeChanges[element]

        self.SaveNewTheme(newThemeName, newTheme)
        customThemeList = idleConf.GetSectionList(b'user', b'highlight')
        customThemeList.sort()
        self.optMenuThemeCustom.SetMenu(customThemeList, newThemeName)
        self.themeIsBuiltin.set(0)
        self.SetThemeType()
        return

    def OnListFontButtonRelease(self, event):
        font = self.listFontName.get(ANCHOR)
        self.fontName.set(font.lower())
        self.SetFontSample()
        return

    def SetFontSample(self, event=None):
        fontName = self.fontName.get()
        fontWeight = tkFont.BOLD if self.fontBold.get() else tkFont.NORMAL
        newFont = (fontName, self.fontSize.get(), fontWeight)
        self.labelFontSample.config(font=newFont)
        self.textHighlightSample.configure(font=newFont)
        return

    def SetHighlightTarget(self):
        if self.highlightTarget.get() == b'Cursor':
            self.radioFg.config(state=DISABLED)
            self.radioBg.config(state=DISABLED)
            self.fgHilite.set(1)
        else:
            self.radioFg.config(state=NORMAL)
            self.radioBg.config(state=NORMAL)
            self.fgHilite.set(1)
        self.SetColourSample()
        return

    def SetColourSampleBinding(self, *args):
        self.SetColourSample()
        return

    def SetColourSample(self):
        tag = self.themeElements[self.highlightTarget.get()][0]
        plane = b'foreground' if self.fgHilite.get() else b'background'
        colour = self.textHighlightSample.tag_cget(tag, plane)
        self.frameColourSet.config(bg=colour)
        return

    def PaintThemeSample(self):
        if self.themeIsBuiltin.get():
            theme = self.builtinTheme.get()
        else:
            theme = self.customTheme.get()
        for elementTitle in self.themeElements:
            element = self.themeElements[elementTitle][0]
            colours = idleConf.GetHighlight(theme, element)
            if element == b'cursor':
                colours[b'background'] = idleConf.GetHighlight(theme, b'normal', fgBg=b'bg')
            if theme in self.changedItems[b'highlight']:
                themeDict = self.changedItems[b'highlight'][theme]
                if element + b'-foreground' in themeDict:
                    colours[b'foreground'] = themeDict[element + b'-foreground']
                if element + b'-background' in themeDict:
                    colours[b'background'] = themeDict[element + b'-background']
            self.textHighlightSample.tag_config(element, **colours)

        self.SetColourSample()
        return

    def HelpSourceSelected(self, event):
        self.SetHelpListButtonStates()
        return

    def SetHelpListButtonStates(self):
        if self.listHelp.size() < 1:
            self.buttonHelpListEdit.config(state=DISABLED)
            self.buttonHelpListRemove.config(state=DISABLED)
        elif self.listHelp.curselection():
            self.buttonHelpListEdit.config(state=NORMAL)
            self.buttonHelpListRemove.config(state=NORMAL)
        else:
            self.buttonHelpListEdit.config(state=DISABLED)
            self.buttonHelpListRemove.config(state=DISABLED)
        return

    def HelpListItemAdd(self):
        helpSource = GetHelpSourceDialog(self, b'New Help Source').result
        if helpSource:
            self.userHelpList.append((helpSource[0], helpSource[1]))
            self.listHelp.insert(END, helpSource[0])
            self.UpdateUserHelpChangedItems()
        self.SetHelpListButtonStates()
        return

    def HelpListItemEdit(self):
        itemIndex = self.listHelp.index(ANCHOR)
        helpSource = self.userHelpList[itemIndex]
        newHelpSource = GetHelpSourceDialog(self, b'Edit Help Source', menuItem=helpSource[0], filePath=helpSource[1]).result
        if not newHelpSource or newHelpSource == helpSource:
            return
        self.userHelpList[itemIndex] = newHelpSource
        self.listHelp.delete(itemIndex)
        self.listHelp.insert(itemIndex, newHelpSource[0])
        self.UpdateUserHelpChangedItems()
        self.SetHelpListButtonStates()
        return

    def HelpListItemRemove(self):
        itemIndex = self.listHelp.index(ANCHOR)
        del self.userHelpList[itemIndex]
        self.listHelp.delete(itemIndex)
        self.UpdateUserHelpChangedItems()
        self.SetHelpListButtonStates()
        return

    def UpdateUserHelpChangedItems(self):
        self.changedItems[b'main'][b'HelpFiles'] = {}
        for num in range(1, len(self.userHelpList) + 1):
            self.AddChangedItem(b'main', b'HelpFiles', str(num), (b';').join(self.userHelpList[num - 1][:2]))

        return

    def LoadFontCfg(self):
        fonts = list(tkFont.families(self))
        fonts.sort()
        for font in fonts:
            self.listFontName.insert(END, font)

        configuredFont = idleConf.GetFont(self, b'main', b'EditorWindow')
        fontName = configuredFont[0].lower()
        fontSize = configuredFont[1]
        fontBold = configuredFont[2] == b'bold'
        self.fontName.set(fontName)
        lc_fonts = [s.lower() for s in fonts]
        try:
            currentFontIndex = lc_fonts.index(fontName)
            self.listFontName.see(currentFontIndex)
            self.listFontName.select_set(currentFontIndex)
            self.listFontName.select_anchor(currentFontIndex)
        except ValueError:
            pass

        self.optMenuFontSize.SetMenu((b'7', b'8', b'9', b'10', b'11', b'12', b'13', b'14', b'16', b'18', b'20', b'22', b'25', b'29', b'34', b'40'), fontSize)
        self.fontBold.set(fontBold)
        self.SetFontSample()
        return

    def LoadTabCfg(self):
        spaceNum = idleConf.GetOption(b'main', b'Indent', b'num-spaces', default=4, type=b'int')
        self.spaceNum.set(spaceNum)
        return

    def LoadThemeCfg(self):
        self.themeIsBuiltin.set(idleConf.GetOption(b'main', b'Theme', b'default', type=b'bool', default=1))
        currentOption = idleConf.CurrentTheme()
        if self.themeIsBuiltin.get():
            itemList = idleConf.GetSectionList(b'default', b'highlight')
            itemList.sort()
            self.optMenuThemeBuiltin.SetMenu(itemList, currentOption)
            itemList = idleConf.GetSectionList(b'user', b'highlight')
            itemList.sort()
            if not itemList:
                self.radioThemeCustom.config(state=DISABLED)
                self.customTheme.set(b'- no custom themes -')
            else:
                self.optMenuThemeCustom.SetMenu(itemList, itemList[0])
        else:
            itemList = idleConf.GetSectionList(b'user', b'highlight')
            itemList.sort()
            self.optMenuThemeCustom.SetMenu(itemList, currentOption)
            itemList = idleConf.GetSectionList(b'default', b'highlight')
            itemList.sort()
            self.optMenuThemeBuiltin.SetMenu(itemList, itemList[0])
        self.SetThemeType()
        themeNames = self.themeElements.keys()
        themeNames.sort(key=(lambda x: self.themeElements[x][1]))
        self.optMenuHighlightTarget.SetMenu(themeNames, themeNames[0])
        self.PaintThemeSample()
        self.SetHighlightTarget()
        return

    def LoadKeyCfg(self):
        self.keysAreBuiltin.set(idleConf.GetOption(b'main', b'Keys', b'default', type=b'bool', default=1))
        currentOption = idleConf.CurrentKeys()
        if self.keysAreBuiltin.get():
            itemList = idleConf.GetSectionList(b'default', b'keys')
            itemList.sort()
            self.optMenuKeysBuiltin.SetMenu(itemList, currentOption)
            itemList = idleConf.GetSectionList(b'user', b'keys')
            itemList.sort()
            if not itemList:
                self.radioKeysCustom.config(state=DISABLED)
                self.customKeys.set(b'- no custom keys -')
            else:
                self.optMenuKeysCustom.SetMenu(itemList, itemList[0])
        else:
            itemList = idleConf.GetSectionList(b'user', b'keys')
            itemList.sort()
            self.optMenuKeysCustom.SetMenu(itemList, currentOption)
            itemList = idleConf.GetSectionList(b'default', b'keys')
            itemList.sort()
            self.optMenuKeysBuiltin.SetMenu(itemList, itemList[0])
        self.SetKeysType()
        keySetName = idleConf.CurrentKeys()
        self.LoadKeysList(keySetName)
        return

    def LoadGeneralCfg(self):
        self.startupEdit.set(idleConf.GetOption(b'main', b'General', b'editor-on-startup', default=1, type=b'bool'))
        self.autoSave.set(idleConf.GetOption(b'main', b'General', b'autosave', default=0, type=b'bool'))
        self.winWidth.set(idleConf.GetOption(b'main', b'EditorWindow', b'width', type=b'int'))
        self.winHeight.set(idleConf.GetOption(b'main', b'EditorWindow', b'height', type=b'int'))
        self.encoding.set(idleConf.GetOption(b'main', b'EditorWindow', b'encoding', default=b'none'))
        self.userHelpList = idleConf.GetAllExtraHelpSourcesList()
        for helpItem in self.userHelpList:
            self.listHelp.insert(END, helpItem[0])

        self.SetHelpListButtonStates()
        return

    def LoadConfigs(self):
        self.LoadFontCfg()
        self.LoadTabCfg()
        self.LoadThemeCfg()
        self.LoadKeyCfg()
        self.LoadGeneralCfg()
        return

    def SaveNewKeySet(self, keySetName, keySet):
        if not idleConf.userCfg[b'keys'].has_section(keySetName):
            idleConf.userCfg[b'keys'].add_section(keySetName)
        for event in keySet:
            value = keySet[event]
            idleConf.userCfg[b'keys'].SetOption(keySetName, event, value)

        return

    def SaveNewTheme(self, themeName, theme):
        if not idleConf.userCfg[b'highlight'].has_section(themeName):
            idleConf.userCfg[b'highlight'].add_section(themeName)
        for element in theme:
            value = theme[element]
            idleConf.userCfg[b'highlight'].SetOption(themeName, element, value)

        return

    def SetUserValue(self, configType, section, item, value):
        if idleConf.defaultCfg[configType].has_option(section, item):
            if idleConf.defaultCfg[configType].Get(section, item) == value:
                return idleConf.userCfg[configType].RemoveOption(section, item)
        return idleConf.userCfg[configType].SetOption(section, item, value)

    def SaveAllChangedConfigs(self):
        idleConf.userCfg[b'main'].Save()
        for configType in self.changedItems:
            cfgTypeHasChanges = False
            for section in self.changedItems[configType]:
                if section == b'HelpFiles':
                    idleConf.userCfg[b'main'].remove_section(b'HelpFiles')
                    cfgTypeHasChanges = True
                for item in self.changedItems[configType][section]:
                    value = self.changedItems[configType][section][item]
                    if self.SetUserValue(configType, section, item, value):
                        cfgTypeHasChanges = True

            if cfgTypeHasChanges:
                idleConf.userCfg[configType].Save()

        for configType in [b'keys', b'highlight']:
            idleConf.userCfg[configType].Save()

        self.ResetChangedItems()
        self.save_all_changed_extensions()
        return

    def DeactivateCurrentConfig(self):
        winInstances = self.parent.instance_dict
        for instance in winInstances:
            instance.RemoveKeybindings()

        return

    def ActivateConfigChanges(self):
        winInstances = self.parent.instance_dict.keys()
        for instance in winInstances:
            instance.ResetColorizer()
            instance.ResetFont()
            instance.set_notabs_indentwidth()
            instance.ApplyKeybindings()
            instance.reset_help_menu_entries()

        return

    def Cancel(self):
        self.grab_release()
        self.destroy()
        return

    def Ok(self):
        self.Apply()
        self.grab_release()
        self.destroy()
        return

    def Apply(self):
        self.DeactivateCurrentConfig()
        self.SaveAllChangedConfigs()
        self.ActivateConfigChanges()
        return

    def Help(self):
        page = self.tabPages._current_page
        view_text(self, title=b'Help for IDLE preferences', text=help_common + help_pages.get(page, b''))
        return

    def CreatePageExtensions(self):
        parent = self.parent
        frame = self.tabPages.pages[b'Extensions'].frame
        self.ext_defaultCfg = idleConf.defaultCfg[b'extensions']
        self.ext_userCfg = idleConf.userCfg[b'extensions']
        self.is_int = self.register(is_int)
        self.load_extensions()
        self.extension_names = StringVar(self)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(2, weight=1)
        self.extension_list = Listbox(frame, listvariable=self.extension_names, selectmode=b'browse')
        self.extension_list.bind(b'<<ListboxSelect>>', self.extension_selected)
        scroll = Scrollbar(frame, command=self.extension_list.yview)
        self.extension_list.yscrollcommand = scroll.set
        self.details_frame = LabelFrame(frame, width=250, height=250)
        self.extension_list.grid(column=0, row=0, sticky=b'nws')
        scroll.grid(column=1, row=0, sticky=b'ns')
        self.details_frame.grid(column=2, row=0, sticky=b'nsew', padx=[10, 0])
        frame.configure(padx=10, pady=10)
        self.config_frame = {}
        self.current_extension = None
        self.outerframe = self
        self.tabbed_page_set = self.extension_list
        ext_names = b''
        for ext_name in sorted(self.extensions):
            self.create_extension_frame(ext_name)
            ext_names = ext_names + b'{' + ext_name + b'} '

        self.extension_names.set(ext_names)
        self.extension_list.selection_set(0)
        self.extension_selected(None)
        return

    def load_extensions(self):
        self.extensions = {}
        for ext_name in idleConf.GetExtensions(active_only=False):
            self.extensions[ext_name] = []

        for ext_name in self.extensions:
            opt_list = sorted(self.ext_defaultCfg.GetOptionList(ext_name))
            enables = [opt_name for opt_name in opt_list if opt_name.startswith(b'enable')]
            for opt_name in enables:
                opt_list.remove(opt_name)

            opt_list = enables + opt_list
            for opt_name in opt_list:
                def_str = self.ext_defaultCfg.Get(ext_name, opt_name, raw=True)
                try:
                    def_obj = {b'True': True, b'False': False}[def_str]
                    opt_type = b'bool'
                except KeyError:
                    try:
                        def_obj = int(def_str)
                        opt_type = b'int'
                    except ValueError:
                        def_obj = def_str
                        opt_type = None

                try:
                    value = self.ext_userCfg.Get(ext_name, opt_name, type=opt_type, raw=True, default=def_obj)
                except ValueError:
                    value = def_obj

                var = StringVar(self)
                var.set(str(value))
                self.extensions[ext_name].append({b'name': opt_name, b'type': opt_type, 
                   b'default': def_str, 
                   b'value': value, 
                   b'var': var})

        return

    def extension_selected(self, event):
        newsel = self.extension_list.curselection()
        if newsel:
            newsel = self.extension_list.get(newsel)
        if newsel is None or newsel != self.current_extension:
            if self.current_extension:
                self.details_frame.config(text=b'')
                self.config_frame[self.current_extension].grid_forget()
                self.current_extension = None
        if newsel:
            self.details_frame.config(text=newsel)
            self.config_frame[newsel].grid(column=0, row=0, sticky=b'nsew')
            self.current_extension = newsel
        return

    def create_extension_frame(self, ext_name):
        f = VerticalScrolledFrame(self.details_frame, height=250, width=250)
        self.config_frame[ext_name] = f
        entry_area = f.interior
        for row, opt in enumerate(self.extensions[ext_name]):
            label = Label(entry_area, text=opt[b'name'])
            label.grid(row=row, column=0, sticky=NW)
            var = opt[b'var']
            if opt[b'type'] == b'bool':
                Checkbutton(entry_area, textvariable=var, variable=var, onvalue=b'True', offvalue=b'False', indicatoron=FALSE, selectcolor=b'', width=8).grid(row=row, column=1, sticky=W, padx=7)
            elif opt[b'type'] == b'int':
                Entry(entry_area, textvariable=var, validate=b'key', validatecommand=(
                 self.is_int, b'%P')).grid(row=row, column=1, sticky=NSEW, padx=7)
            else:
                Entry(entry_area, textvariable=var).grid(row=row, column=1, sticky=NSEW, padx=7)

        return

    def set_extension_value(self, section, opt):
        name = opt[b'name']
        default = opt[b'default']
        value = opt[b'var'].get().strip() or default
        opt[b'var'].set(value)
        if value == default:
            return self.ext_userCfg.RemoveOption(section, name)
        return self.ext_userCfg.SetOption(section, name, value)

    def save_all_changed_extensions(self):
        has_changes = False
        for ext_name in self.extensions:
            options = self.extensions[ext_name]
            for opt in options:
                if self.set_extension_value(ext_name, opt):
                    has_changes = True

        if has_changes:
            self.ext_userCfg.Save()
        return


help_common = b"When you click either the Apply or Ok buttons, settings in this\ndialog that are different from IDLE's default are saved in\na .idlerc directory in your home directory. Except as noted,\nthese changes apply to all versions of IDLE installed on this\nmachine. Some do not take affect until IDLE is restarted.\n[Cancel] only cancels changes made since the last save.\n"
help_pages = {b'Highlighting': b'\nHighlighting:\nThe IDLE Dark color theme is new in October 2015.  It can only\nbe used with older IDLE releases if it is saved as a custom\ntheme, with a different name.\n'}

def is_int(s):
    if not s:
        return True
    try:
        int(s)
        return True
    except ValueError:
        return False

    return


class VerticalScrolledFrame(Frame):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        vscrollbar = Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set, width=240)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        self.interior = interior = Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=NW)

        def _configure_interior(event):
            size = (
             interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion=b'0 0 %s %s' % size)
            return

        interior.bind(b'<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
            return

        canvas.bind(b'<Configure>', _configure_canvas)
        return


if __name__ == b'__main__':
    import unittest
    unittest.main(b'idlelib.idle_test.test_configdialog', verbosity=2, exit=False)
    from idlelib.idle_test.htest import run
    run(ConfigDialog)
