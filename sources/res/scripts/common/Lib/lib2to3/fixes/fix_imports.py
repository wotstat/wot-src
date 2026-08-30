from .. import fixer_base
from ..fixer_util import Name, attr_chain
MAPPING = {b'StringIO': b'io', b'cStringIO': b'io', 
   b'cPickle': b'pickle', 
   b'__builtin__': b'builtins', 
   b'copy_reg': b'copyreg', 
   b'Queue': b'queue', 
   b'SocketServer': b'socketserver', 
   b'ConfigParser': b'configparser', 
   b'repr': b'reprlib', 
   b'FileDialog': b'tkinter.filedialog', 
   b'tkFileDialog': b'tkinter.filedialog', 
   b'SimpleDialog': b'tkinter.simpledialog', 
   b'tkSimpleDialog': b'tkinter.simpledialog', 
   b'tkColorChooser': b'tkinter.colorchooser', 
   b'tkCommonDialog': b'tkinter.commondialog', 
   b'Dialog': b'tkinter.dialog', 
   b'Tkdnd': b'tkinter.dnd', 
   b'tkFont': b'tkinter.font', 
   b'tkMessageBox': b'tkinter.messagebox', 
   b'ScrolledText': b'tkinter.scrolledtext', 
   b'Tkconstants': b'tkinter.constants', 
   b'Tix': b'tkinter.tix', 
   b'ttk': b'tkinter.ttk', 
   b'Tkinter': b'tkinter', 
   b'markupbase': b'_markupbase', 
   b'_winreg': b'winreg', 
   b'thread': b'_thread', 
   b'dummy_thread': b'_dummy_thread', 
   b'dbhash': b'dbm.bsd', 
   b'dumbdbm': b'dbm.dumb', 
   b'dbm': b'dbm.ndbm', 
   b'gdbm': b'dbm.gnu', 
   b'xmlrpclib': b'xmlrpc.client', 
   b'DocXMLRPCServer': b'xmlrpc.server', 
   b'SimpleXMLRPCServer': b'xmlrpc.server', 
   b'httplib': b'http.client', 
   b'htmlentitydefs': b'html.entities', 
   b'HTMLParser': b'html.parser', 
   b'Cookie': b'http.cookies', 
   b'cookielib': b'http.cookiejar', 
   b'BaseHTTPServer': b'http.server', 
   b'SimpleHTTPServer': b'http.server', 
   b'CGIHTTPServer': b'http.server', 
   b'commands': b'subprocess', 
   b'UserString': b'collections', 
   b'UserList': b'collections', 
   b'urlparse': b'urllib.parse', 
   b'robotparser': b'urllib.robotparser'}

def alternates(members):
    return b'(' + (b'|').join(map(repr, members)) + b')'


def build_pattern(mapping=MAPPING):
    mod_list = (b' | ').join([b"module_name='%s'" % key for key in mapping])
    bare_names = alternates(mapping.keys())
    yield b"name_import=import_name< 'import' ((%s) |\n               multiple_imports=dotted_as_names< any* (%s) any* >) >\n          " % (mod_list, mod_list)
    yield b"import_from< 'from' (%s) 'import' ['(']\n              ( any | import_as_name< any 'as' any > |\n                import_as_names< any* >)  [')'] >\n          " % mod_list
    yield b"import_name< 'import' (dotted_as_name< (%s) 'as' any > |\n               multiple_imports=dotted_as_names<\n                 any* dotted_as_name< (%s) 'as' any > any* >) >\n          " % (mod_list, mod_list)
    yield b"power< bare_with_attr=(%s) trailer<'.' any > any* >" % bare_names
    return


class FixImports(fixer_base.BaseFix):
    BM_compatible = True
    keep_line_order = True
    mapping = MAPPING
    run_order = 6

    def build_pattern(self):
        return (b'|').join(build_pattern(self.mapping))

    def compile_pattern(self):
        self.PATTERN = self.build_pattern()
        super(FixImports, self).compile_pattern()
        return

    def match(self, node):
        match = super(FixImports, self).match
        results = match(node)
        if results:
            if b'bare_with_attr' not in results and any(match(obj) for obj in attr_chain(node, b'parent')):
                return False
            return results
        return False

    def start_tree(self, tree, filename):
        super(FixImports, self).start_tree(tree, filename)
        self.replace = {}
        return

    def transform(self, node, results):
        import_mod = results.get(b'module_name')
        if import_mod:
            mod_name = import_mod.value
            new_name = unicode(self.mapping[mod_name])
            import_mod.replace(Name(new_name, prefix=import_mod.prefix))
            if b'name_import' in results:
                self.replace[mod_name] = new_name
            if b'multiple_imports' in results:
                results = self.match(node)
                if results:
                    self.transform(node, results)
        else:
            bare_name = results[b'bare_with_attr'][0]
            new_name = self.replace.get(bare_name.value)
            if new_name:
                bare_name.replace(Name(new_name, prefix=bare_name.prefix))
        return
