all_feature_names = [
 0, 
 1, 
 2, 
 3, 
 4, 
 5, 
 6]
__all__ = [
 b'all_feature_names'] + all_feature_names
CO_NESTED = 16
CO_GENERATOR_ALLOWED = 0
CO_FUTURE_DIVISION = 8192
CO_FUTURE_ABSOLUTE_IMPORT = 16384
CO_FUTURE_WITH_STATEMENT = 32768
CO_FUTURE_PRINT_FUNCTION = 65536
CO_FUTURE_UNICODE_LITERALS = 131072

class _Feature:

    def __init__(self, optionalRelease, mandatoryRelease, compiler_flag):
        self.optional = optionalRelease
        self.mandatory = mandatoryRelease
        self.compiler_flag = compiler_flag
        return

    def getOptionalRelease(self):
        return self.optional

    def getMandatoryRelease(self):
        return self.mandatory

    def __repr__(self):
        return b'_Feature' + repr((self.optional,
         self.mandatory,
         self.compiler_flag))


nested_scopes = _Feature((2, 1, 0, b'beta', 1), (2, 2, 0, b'alpha', 0), CO_NESTED)
generators = _Feature((2, 2, 0, b'alpha', 1), (2, 3, 0, b'final', 0), CO_GENERATOR_ALLOWED)
division = _Feature((2, 2, 0, b'alpha', 2), (3, 0, 0, b'alpha', 0), CO_FUTURE_DIVISION)
absolute_import = _Feature((2, 5, 0, b'alpha', 1), (3, 0, 0, b'alpha', 0), CO_FUTURE_ABSOLUTE_IMPORT)
with_statement = _Feature((2, 5, 0, b'alpha', 1), (2, 6, 0, b'alpha', 0), CO_FUTURE_WITH_STATEMENT)
print_function = _Feature((2, 6, 0, b'alpha', 2), (3, 0, 0, b'alpha', 0), CO_FUTURE_PRINT_FUNCTION)
unicode_literals = _Feature((2, 6, 0, b'alpha', 2), (3, 0, 0, b'alpha', 0), CO_FUTURE_UNICODE_LITERALS)
