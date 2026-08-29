from . import fix_imports
MAPPING = {b'whichdb': b'dbm', 
   b'anydbm': b'dbm'}

class FixImports2(fix_imports.FixImports):
    run_order = 7
    mapping = MAPPING
