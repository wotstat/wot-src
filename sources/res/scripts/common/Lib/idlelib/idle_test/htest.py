from importlib import import_module
from idlelib.macosxSupport import _initializeTkVariantTests
import Tkinter as tk
AboutDialog_spec = {b'file': b'aboutDialog', 
   b'kwds': {b'title': b'aboutDialog test', b'_htest': True}, 
   b'msg': b'Test every button. Ensure Python, TK and IDLE versions are correctly displayed.\n [Close] to exit.'}
_calltip_window_spec = {b'file': b'CallTipWindow', 
   b'kwds': {}, b'msg': b"Typing '(' should display a calltip.\nTyping ') should hide the calltip.\n"}
_class_browser_spec = {b'file': b'ClassBrowser', 
   b'kwds': {}, b'msg': b'Inspect names of module, class(with superclass if applicable), methods and functions.\nToggle nested items.\nDouble clicking on items prints a traceback for an exception that is ignored.'}
_color_delegator_spec = {b'file': b'ColorDelegator', 
   b'kwds': {}, b'msg': b'The text is sample Python code.\nEnsure components like comments, keywords, builtins,\nstring, definitions, and break are correctly colored.\nThe default color scheme is in idlelib/config-highlight.def'}
ConfigDialog_spec = {b'file': b'configDialog', 
   b'kwds': {b'title': b'ConfigDialogTest', b'_htest': True}, 
   b'msg': b"IDLE preferences dialog.\nIn the 'Fonts/Tabs' tab, changing font face, should update the font face of the text in the area below it.\nIn the 'Highlighting' tab, try different color schemes. Clicking items in the sample program should update the choices above it.\nIn the 'Keys', 'General' and 'Extensions' tabs, test settings of interest.\n[Ok] to close the dialog.[Apply] to apply the settings and and [Cancel] to revert all changes.\nRe-run the test to ensure changes made have persisted."}
_dyn_option_menu_spec = {b'file': b'dynOptionMenuWidget', 
   b'kwds': {}, b'msg': b"Select one of the many options in the 'old option set'.\nClick the button to change the option set.\nSelect one of the many options in the 'new option set'."}
_editor_window_spec = {b'file': b'EditorWindow', 
   b'kwds': {}, b'msg': b'Test editor functions of interest.\nBest to close editor first.'}
GetCfgSectionNameDialog_spec = {b'file': b'configSectionNameDialog', 
   b'kwds': {b'title': b'Get Name', b'message': b'Enter something', 
             b'used_names': {
                           b'abc'}, 
             b'_htest': True}, 
   b'msg': b"After the text entered with [Ok] is stripped, <nothing>, 'abc', or more that 30 chars are errors.\nClose 'Get Name' with a valid entry (printed to Shell), [Cancel], or [X]"}
GetHelpSourceDialog_spec = {b'file': b'configHelpSourceEdit', 
   b'kwds': {b'title': b'Get helpsource', b'_htest': True}, 
   b'msg': b'Enter menu item name and help file path\n <nothing> and more than 30 chars are invalid menu item names.\n<nothing>, file does not exist are invalid path items.\nTest for incomplete web address for help file path.\nA valid entry will be printed to shell with [0k].\n[Cancel] will print None to shell'}
GetKeysDialog_spec = {b'file': b'keybindingDialog', 
   b'kwds': {b'title': b'Test keybindings', b'action': b'find-again', 
             b'currentKeySequences': [
                                    b''], 
             b'_htest': True}, 
   b'msg': b'Test for different key modifier sequences.\n<nothing> is invalid.\nNo modifier key is invalid.\nShift key with [a-z],[0-9], function key, move key, tab, space is invalid.\nNo validitity checking if advanced key binding entry is used.'}
_grep_dialog_spec = {b'file': b'GrepDialog', 
   b'kwds': {}, b'msg': b"Click the 'Show GrepDialog' button.\nTest the various 'Find-in-files' functions.\nThe results should be displayed in a new '*Output*' window.\n'Right-click'->'Goto file/line' anywhere in the search results should open that file \nin a new EditorWindow."}
_io_binding_spec = {b'file': b'IOBinding', 
   b'kwds': {}, b'msg': b'Test the following bindings.\n<Control-o> to open file from dialog.\nEdit the file.\n<Control-p> to print the file.\n<Control-s> to save the file.\n<Alt-s> to save-as another file.\n<Control-c> to save-copy-as another file.\nCheck that changes were saved by opening the file elsewhere.'}
_multi_call_spec = {b'file': b'MultiCall', 
   b'kwds': {}, b'msg': b'The following actions should trigger a print to console or IDLE Shell.\nEntering and leaving the text area, key entry, <Control-Key>,\n<Alt-Key-a>, <Control-Key-a>, <Alt-Control-Key-a>, \n<Control-Button-1>, <Alt-Button-1> and focusing out of the window\nare sequences to be tested.'}
_multistatus_bar_spec = {b'file': b'MultiStatusBar', 
   b'kwds': {}, b'msg': b"Ensure presence of multi-status bar below text area.\nClick 'Update Status' to change the multi-status text"}
_object_browser_spec = {b'file': b'ObjectBrowser', 
   b'kwds': {}, b'msg': b'Double click on items upto the lowest level.\nAttributes of the objects and related information will be displayed side-by-side at each level.'}
_path_browser_spec = {b'file': b'PathBrowser', 
   b'kwds': {}, b'msg': b'Test for correct display of all paths in sys.path.\nToggle nested items upto the lowest level.\nDouble clicking on an item prints a traceback\nfor an exception that is ignored.'}
_percolator_spec = {b'file': b'Percolator', 
   b'kwds': {}, b'msg': b"There are two tracers which can be toggled using a checkbox.\nToggling a tracer 'on' by checking it should print tracer output to the console or to the IDLE shell.\nIf both the tracers are 'on', the output from the tracer which was switched 'on' later, should be printed first\nTest for actions like text entry, and removal."}
_replace_dialog_spec = {b'file': b'ReplaceDialog', 
   b'kwds': {}, b'msg': b"Click the 'Replace' button.\nTest various replace options in the 'Replace dialog'.\nClick [Close] or [X] to close the 'Replace Dialog'."}
_search_dialog_spec = {b'file': b'SearchDialog', 
   b'kwds': {}, b'msg': b"Click the 'Search' button.\nTest various search options in the 'Search dialog'.\nClick [Close] or [X] to close the 'Search Dialog'."}
_scrolled_list_spec = {b'file': b'ScrolledList', 
   b'kwds': {}, b'msg': b'You should see a scrollable list of items\nSelecting (clicking) or double clicking an item prints the name to the console or Idle shell.\nRight clicking an item will display a popup.'}
show_idlehelp_spec = {b'file': b'help', 
   b'kwds': {}, b'msg': b'If the help text displays, this works.\nText is selectable. Window is scrollable.'}
_stack_viewer_spec = {b'file': b'StackViewer', 
   b'kwds': {}, b'msg': b"A stacktrace for a NameError exception.\nExpand 'idlelib ...' and '<locals>'.\nCheck that exc_value, exc_tb, and exc_type are correct.\n"}
_tabbed_pages_spec = {b'file': b'tabbedpages', 
   b'kwds': {}, b'msg': b"Toggle between the two tabs 'foo' and 'bar'\nAdd a tab by entering a suitable name for it.\nRemove an existing tab by entering its name.\nRemove all existing tabs.\n<nothing> is an invalid add page and remove page name.\n"}
TextViewer_spec = {b'file': b'textView', 
   b'kwds': {b'title': b'Test textView', b'text': (b'The quick brown fox jumps over the lazy dog.\n' * 35), 
             b'_htest': True}, 
   b'msg': b'Test for read-only property of text.\nText is selectable. Window is scrollable.'}
_tooltip_spec = {b'file': b'ToolTip', 
   b'kwds': {}, b'msg': b'Place mouse cursor over both the buttons\nA tooltip should appear with some text.'}
_tree_widget_spec = {b'file': b'TreeWidget', 
   b'kwds': {}, b'msg': b'The canvas is scrollable.\nClick on folders upto to the lowest level.'}
_undo_delegator_spec = {b'file': b'UndoDelegator', 
   b'kwds': {}, b'msg': b'Click [Undo] to undo any action.\nClick [Redo] to redo any action.\nClick [Dump] to dump the current state by printing to the console or the IDLE shell.\n'}
_widget_redirector_spec = {b'file': b'WidgetRedirector', 
   b'kwds': {}, b'msg': b'Every text insert should be printed to the console or the IDLE shell.'}

def run(*tests):
    root = tk.Tk()
    root.title(b'IDLE htest')
    root.resizable(0, 0)
    _initializeTkVariantTests(root)
    frameLabel = tk.Frame(root, padx=10)
    frameLabel.pack()
    text = tk.Text(frameLabel, wrap=b'word')
    text.configure(bg=root.cget(b'bg'), relief=b'flat', height=4, width=70)
    scrollbar = tk.Scrollbar(frameLabel, command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=b'right', fill=b'y', expand=False)
    text.pack(side=b'left', fill=b'both', expand=True)
    test_list = []
    if tests:
        for test in tests:
            test_spec = globals()[test.__name__ + b'_spec']
            test_spec[b'name'] = test.__name__
            test_list.append((test_spec, test))

    else:
        for k, d in globals().items():
            if k.endswith(b'_spec'):
                test_name = k[:-5]
                test_spec = d
                test_spec[b'name'] = test_name
                mod = import_module(b'idlelib.' + test_spec[b'file'])
                test = getattr(mod, test_name)
                test_list.append((test_spec, test))

    test_name = [
     tk.StringVar(b'')]
    callable_object = [None]
    test_kwds = [None]

    def next():
        if len(test_list) == 1:
            next_button.pack_forget()
        test_spec, callable_object[0] = test_list.pop()
        test_kwds[0] = test_spec[b'kwds']
        test_kwds[0][b'parent'] = root
        test_name[0].set(b'Test ' + test_spec[b'name'])
        text.configure(state=b'normal')
        text.delete(b'1.0', b'end')
        text.insert(b'1.0', test_spec[b'msg'])
        text.configure(state=b'disabled')
        return

    def run_test():
        widget = callable_object[0](**test_kwds[0])
        try:
            print widget.result
        except AttributeError:
            pass

        return

    button = tk.Button(root, textvariable=test_name[0], command=run_test)
    button.pack()
    next_button = tk.Button(root, text=b'Next', command=next)
    next_button.pack()
    next()
    root.mainloop()
    return


if __name__ == b'__main__':
    run()
