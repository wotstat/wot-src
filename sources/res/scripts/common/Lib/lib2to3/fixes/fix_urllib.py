from lib2to3.fixes.fix_imports import alternates, FixImports
from lib2to3 import fixer_base
from lib2to3.fixer_util import Name, Comma, FromImport, Newline, find_indentation, Node, syms
MAPPING = {b'urllib': [
             (
              b'urllib.request',
              [
               5, 6, 7, 
               8, 
               9, 10, 
               11, 12]),
             (
              b'urllib.parse',
              [
               14, 15, 16, 17, 
               18, 
               19, 20, 21, 
               22, 
               23, 24, 25, 
               26, 
               27, 28]),
             (
              b'urllib.error',
              [
               b'ContentTooShortError'])], 
   b'urllib2': [
              (
               b'urllib.request',
               [
                9, 32, 33, 
                34, 
                35, 36, 
                37, 
                38, 
                39, 40, 
                41, 
                42, 
                43, 
                44, 
                45, 
                46, 
                47, 
                48, 
                49, 50, 
                51, 
                52, 53, 
                54]),
              (
               b'urllib.error',
               [
                b'URLError', b'HTTPError'])]}
MAPPING[b'urllib2'].append(MAPPING[b'urllib'][1])

def build_pattern():
    bare = set()
    for old_module, changes in MAPPING.items():
        for change in changes:
            new_module, members = change
            members = alternates(members)
            yield b"import_name< 'import' (module=%r\n                                  | dotted_as_names< any* module=%r any* >) >\n                  " % (old_module, old_module)
            yield b"import_from< 'from' mod_member=%r 'import'\n                       ( member=%s | import_as_name< member=%s 'as' any > |\n                         import_as_names< members=any*  >) >\n                  " % (old_module, members, members)
            yield b"import_from< 'from' module_star=%r 'import' star='*' >\n                  " % old_module
            yield b"import_name< 'import'\n                                  dotted_as_name< module_as=%r 'as' any > >\n                  " % old_module
            yield b"power< bare_with_attr=%r trailer< '.' member=%s > any* >\n                  " % (old_module, members)

    return


class FixUrllib(FixImports):

    def build_pattern(self):
        return (b'|').join(build_pattern())

    def transform_import(self, node, results):
        import_mod = results.get(b'module')
        pref = import_mod.prefix
        names = []
        for name in MAPPING[import_mod.value][:-1]:
            names.extend([Name(name[0], prefix=pref), Comma()])

        names.append(Name(MAPPING[import_mod.value][-1][0], prefix=pref))
        import_mod.replace(names)
        return

    def transform_member(self, node, results):
        mod_member = results.get(b'mod_member')
        pref = mod_member.prefix
        member = results.get(b'member')
        if member:
            if isinstance(member, list):
                member = member[0]
            new_name = None
            for change in MAPPING[mod_member.value]:
                if member.value in change[1]:
                    new_name = change[0]
                    break

            if new_name:
                mod_member.replace(Name(new_name, prefix=pref))
            else:
                self.cannot_convert(node, b'This is an invalid module element')
        else:
            modules = []
            mod_dict = {}
            members = results[b'members']
            for member in members:
                if member.type == syms.import_as_name:
                    as_name = member.children[2].value
                    member_name = member.children[0].value
                else:
                    member_name = member.value
                    as_name = None
                if member_name != u',':
                    for change in MAPPING[mod_member.value]:
                        if member_name in change[1]:
                            if change[0] not in mod_dict:
                                modules.append(change[0])
                            mod_dict.setdefault(change[0], []).append(member)

            new_nodes = []
            indentation = find_indentation(node)
            first = True

            def handle_name(name, prefix):
                if name.type == syms.import_as_name:
                    kids = [
                     Name(name.children[0].value, prefix=prefix),
                     name.children[1].clone(),
                     name.children[2].clone()]
                    return [
                     Node(syms.import_as_name, kids)]
                return [
                 Name(name.value, prefix=prefix)]

            for module in modules:
                elts = mod_dict[module]
                names = []
                for elt in elts[:-1]:
                    names.extend(handle_name(elt, pref))
                    names.append(Comma())

                names.extend(handle_name(elts[-1], pref))
                new = FromImport(module, names)
                if not first or node.parent.prefix.endswith(indentation):
                    new.prefix = indentation
                new_nodes.append(new)
                first = False

            if new_nodes:
                nodes = []
                for new_node in new_nodes[:-1]:
                    nodes.extend([new_node, Newline()])

                nodes.append(new_nodes[-1])
                node.replace(nodes)
            else:
                self.cannot_convert(node, b'All module elements are invalid')
        return

    def transform_dot(self, node, results):
        module_dot = results.get(b'bare_with_attr')
        member = results.get(b'member')
        new_name = None
        if isinstance(member, list):
            member = member[0]
        for change in MAPPING[module_dot.value]:
            if member.value in change[1]:
                new_name = change[0]
                break

        if new_name:
            module_dot.replace(Name(new_name, prefix=module_dot.prefix))
        else:
            self.cannot_convert(node, b'This is an invalid module element')
        return

    def transform(self, node, results):
        if results.get(b'module'):
            self.transform_import(node, results)
        elif results.get(b'mod_member'):
            self.transform_member(node, results)
        elif results.get(b'bare_with_attr'):
            self.transform_dot(node, results)
        elif results.get(b'module_star'):
            self.cannot_convert(node, b'Cannot handle star imports.')
        elif results.get(b'module_as'):
            self.cannot_convert(node, b'This module is now multiple modules')
        return
