import sys
if sys.argv[0].endswith(b'__main__.py'):
    sys.argv[0] = b'python -m unittest'
__unittest = True
from .main import main, TestProgram, USAGE_AS_MAIN
TestProgram.USAGE = USAGE_AS_MAIN
main(module=None)
