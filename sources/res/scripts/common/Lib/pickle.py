__version__ = b'$Revision: 72223 $'
from types import *
from copy_reg import dispatch_table
from copy_reg import _extension_registry, _inverted_registry, _extension_cache
import marshal, sys, struct, re
__all__ = [
 6, 7, 8, 9, 
 10, 11, 12, 13, 14]
format_version = b'2.0'
compatible_formats = [16, 
 17, 
 18, 
 19, 
 15]
HIGHEST_PROTOCOL = 2
mloads = marshal.loads

class PickleError(Exception):
    pass


class PicklingError(PickleError):
    pass


class UnpicklingError(PickleError):
    pass


class _Stop(Exception):

    def __init__(self, value):
        self.value = value
        return


try:
    from org.python.core import PyStringMap
except ImportError:
    PyStringMap = None

try:
    UnicodeType
except NameError:
    UnicodeType = None

MARK = b'('
STOP = b'.'
POP = b'0'
POP_MARK = b'1'
DUP = b'2'
FLOAT = b'F'
INT = b'I'
BININT = b'J'
BININT1 = b'K'
LONG = b'L'
BININT2 = b'M'
NONE = b'N'
PERSID = b'P'
BINPERSID = b'Q'
REDUCE = b'R'
STRING = b'S'
BINSTRING = b'T'
SHORT_BINSTRING = b'U'
UNICODE = b'V'
BINUNICODE = b'X'
APPEND = b'a'
BUILD = b'b'
GLOBAL = b'c'
DICT = b'd'
EMPTY_DICT = b'}'
APPENDS = b'e'
GET = b'g'
BINGET = b'h'
INST = b'i'
LONG_BINGET = b'j'
LIST = b'l'
EMPTY_LIST = b']'
OBJ = b'o'
PUT = b'p'
BINPUT = b'q'
LONG_BINPUT = b'r'
SETITEM = b's'
TUPLE = b't'
EMPTY_TUPLE = b')'
SETITEMS = b'u'
BINFLOAT = b'G'
TRUE = b'I01\n'
FALSE = b'I00\n'
PROTO = b'\x80'
NEWOBJ = b'\x81'
EXT1 = b'\x82'
EXT2 = b'\x83'
EXT4 = b'\x84'
TUPLE1 = b'\x85'
TUPLE2 = b'\x86'
TUPLE3 = b'\x87'
NEWTRUE = b'\x88'
NEWFALSE = b'\x89'
LONG1 = b'\x8a'
LONG4 = b'\x8b'
_tuplesize2code = [
 EMPTY_TUPLE, TUPLE1, TUPLE2, TUPLE3]
__all__.extend([x for x in dir() if re.match(b'[A-Z][A-Z0-9_]+$', x)])
del x

class Pickler():

    def __init__(self, file, protocol=None):
        if protocol is None:
            protocol = 0
        if protocol < 0:
            protocol = HIGHEST_PROTOCOL
        elif not 0 <= protocol <= HIGHEST_PROTOCOL:
            raise ValueError(b'pickle protocol must be <= %d' % HIGHEST_PROTOCOL)
        self.write = file.write
        self.memo = {}
        self.proto = int(protocol)
        self.bin = protocol >= 1
        self.fast = 0
        return

    def clear_memo(self):
        self.memo.clear()
        return

    def dump(self, obj):
        if self.proto >= 2:
            self.write(PROTO + chr(self.proto))
        self.save(obj)
        self.write(STOP)
        return

    def memoize(self, obj):
        if self.fast:
            return
        memo_len = len(self.memo)
        self.write(self.put(memo_len))
        self.memo[id(obj)] = (memo_len, obj)
        return

    def put(self, i, pack=struct.pack):
        if self.bin:
            if i < 256:
                return BINPUT + chr(i)
            else:
                return LONG_BINPUT + pack(b'<i', i)

        return PUT + repr(i) + b'\n'

    def get(self, i, pack=struct.pack):
        if self.bin:
            if i < 256:
                return BINGET + chr(i)
            else:
                return LONG_BINGET + pack(b'<i', i)

        return GET + repr(i) + b'\n'

    def save(self, obj):
        pid = self.persistent_id(obj)
        if pid is not None:
            self.save_pers(pid)
            return
        else:
            x = self.memo.get(id(obj))
            if x:
                self.write(self.get(x[0]))
                return
            t = type(obj)
            f = self.dispatch.get(t)
            if f:
                f(self, obj)
                return
            reduce = dispatch_table.get(t)
            if reduce:
                rv = reduce(obj)
            else:
                try:
                    issc = issubclass(t, TypeType)
                except TypeError:
                    issc = 0

                if issc:
                    self.save_global(obj)
                    return
                reduce = getattr(obj, b'__reduce_ex__', None)
                if reduce:
                    rv = reduce(self.proto)
                else:
                    reduce = getattr(obj, b'__reduce__', None)
                    if reduce:
                        rv = reduce()
                    else:
                        raise PicklingError(b"Can't pickle %r object: %r" % (
                         t.__name__, obj))
            if type(rv) is StringType:
                self.save_global(obj, rv)
                return
            if type(rv) is not TupleType:
                raise PicklingError(b'%s must return string or tuple' % reduce)
            l = len(rv)
            if not 2 <= l <= 5:
                raise PicklingError(b'Tuple returned by %s must have two to five elements' % reduce)
            self.save_reduce(obj=obj, *rv)
            return

    def persistent_id(self, obj):
        return

    def save_pers(self, pid):
        if self.bin:
            self.save(pid)
            self.write(BINPERSID)
        else:
            self.write(PERSID + str(pid) + b'\n')
        return

    def save_reduce(self, func, args, state=None, listitems=None, dictitems=None, obj=None):
        if not isinstance(args, TupleType):
            raise PicklingError(b'args from reduce() should be a tuple')
        if not hasattr(func, b'__call__'):
            raise PicklingError(b'func from reduce should be callable')
        save = self.save
        write = self.write
        if self.proto >= 2 and getattr(func, b'__name__', b'') == b'__newobj__':
            cls = args[0]
            if not hasattr(cls, b'__new__'):
                raise PicklingError(b'args[0] from __newobj__ args has no __new__')
            if obj is not None and cls is not obj.__class__:
                raise PicklingError(b'args[0] from __newobj__ args has the wrong class')
            args = args[1:]
            save(cls)
            save(args)
            write(NEWOBJ)
        else:
            save(func)
            save(args)
            write(REDUCE)
        if obj is not None:
            if id(obj) in self.memo:
                write(POP + self.get(self.memo[id(obj)][0]))
            else:
                self.memoize(obj)
        if listitems is not None:
            self._batch_appends(listitems)
        if dictitems is not None:
            self._batch_setitems(dictitems)
        if state is not None:
            save(state)
            write(BUILD)
        return

    dispatch = {}

    def save_none(self, obj):
        self.write(NONE)
        return

    dispatch[NoneType] = save_none

    def save_bool(self, obj):
        if self.proto >= 2:
            self.write(obj and NEWTRUE or NEWFALSE)
        else:
            self.write(obj and TRUE or FALSE)
        return

    dispatch[bool] = save_bool

    def save_int(self, obj, pack=struct.pack):
        if self.bin:
            if obj >= 0:
                if obj <= 255:
                    self.write(BININT1 + chr(obj))
                    return
                if obj <= 65535:
                    self.write(b'%c%c%c' % (BININT2, obj & 255, obj >> 8))
                    return
            high_bits = obj >> 31
            if high_bits == 0 or high_bits == -1:
                self.write(BININT + pack(b'<i', obj))
                return
        self.write(INT + repr(obj) + b'\n')
        return

    dispatch[IntType] = save_int

    def save_long(self, obj, pack=struct.pack):
        if self.proto >= 2:
            bytes = encode_long(obj)
            n = len(bytes)
            if n < 256:
                self.write(LONG1 + chr(n) + bytes)
            else:
                self.write(LONG4 + pack(b'<i', n) + bytes)
            return
        self.write(LONG + repr(obj) + b'\n')
        return

    dispatch[LongType] = save_long

    def save_float(self, obj, pack=struct.pack):
        if self.bin:
            self.write(BINFLOAT + pack(b'>d', obj))
        else:
            self.write(FLOAT + repr(obj) + b'\n')
        return

    dispatch[FloatType] = save_float

    def save_string(self, obj, pack=struct.pack):
        if self.bin:
            n = len(obj)
            if n < 256:
                self.write(SHORT_BINSTRING + chr(n) + obj)
            else:
                self.write(BINSTRING + pack(b'<i', n) + obj)
        else:
            self.write(STRING + repr(obj) + b'\n')
        self.memoize(obj)
        return

    dispatch[StringType] = save_string

    def save_unicode(self, obj, pack=struct.pack):
        if self.bin:
            encoding = obj.encode(b'utf-8')
            n = len(encoding)
            self.write(BINUNICODE + pack(b'<i', n) + encoding)
        else:
            obj = obj.replace(b'\\', b'\\u005c')
            obj = obj.replace(b'\n', b'\\u000a')
            self.write(UNICODE + obj.encode(b'raw-unicode-escape') + b'\n')
        self.memoize(obj)
        return

    dispatch[UnicodeType] = save_unicode
    if StringType is UnicodeType:

        def save_string(self, obj, pack=struct.pack):
            unicode = obj.isunicode()
            if self.bin:
                if unicode:
                    obj = obj.encode(b'utf-8')
                l = len(obj)
                if l < 256 and not unicode:
                    self.write(SHORT_BINSTRING + chr(l) + obj)
                else:
                    s = pack(b'<i', l)
                    if unicode:
                        self.write(BINUNICODE + s + obj)
                    else:
                        self.write(BINSTRING + s + obj)
            elif unicode:
                obj = obj.replace(b'\\', b'\\u005c')
                obj = obj.replace(b'\n', b'\\u000a')
                obj = obj.encode(b'raw-unicode-escape')
                self.write(UNICODE + obj + b'\n')
            else:
                self.write(STRING + repr(obj) + b'\n')
            self.memoize(obj)
            return

        dispatch[StringType] = save_string

    def save_tuple(self, obj):
        write = self.write
        proto = self.proto
        n = len(obj)
        if n == 0:
            if proto:
                write(EMPTY_TUPLE)
            else:
                write(MARK + TUPLE)
            return
        save = self.save
        memo = self.memo
        if n <= 3 and proto >= 2:
            for element in obj:
                save(element)

            if id(obj) in memo:
                get = self.get(memo[id(obj)][0])
                write(POP * n + get)
            else:
                write(_tuplesize2code[n])
                self.memoize(obj)
            return
        write(MARK)
        for element in obj:
            save(element)

        if id(obj) in memo:
            get = self.get(memo[id(obj)][0])
            if proto:
                write(POP_MARK + get)
            else:
                write(POP * (n + 1) + get)
            return
        self.write(TUPLE)
        self.memoize(obj)
        return

    dispatch[TupleType] = save_tuple

    def save_empty_tuple(self, obj):
        self.write(EMPTY_TUPLE)
        return

    def save_list(self, obj):
        write = self.write
        if self.bin:
            write(EMPTY_LIST)
        else:
            write(MARK + LIST)
        self.memoize(obj)
        self._batch_appends(iter(obj))
        return

    dispatch[ListType] = save_list
    _BATCHSIZE = 1000

    def _batch_appends(self, items):
        save = self.save
        write = self.write
        if not self.bin:
            for x in items:
                save(x)
                write(APPEND)

            return
        r = xrange(self._BATCHSIZE)
        while items is not None:
            tmp = []
            for i in r:
                try:
                    x = items.next()
                    tmp.append(x)
                except StopIteration:
                    items = None
                    break

            n = len(tmp)
            if n > 1:
                write(MARK)
                for x in tmp:
                    save(x)

                write(APPENDS)
            elif n:
                save(tmp[0])
                write(APPEND)

        return

    def save_dict(self, obj):
        write = self.write
        if self.bin:
            write(EMPTY_DICT)
        else:
            write(MARK + DICT)
        self.memoize(obj)
        self._batch_setitems(obj.iteritems())
        return

    dispatch[DictionaryType] = save_dict
    if PyStringMap is not None:
        dispatch[PyStringMap] = save_dict

    def _batch_setitems(self, items):
        save = self.save
        write = self.write
        if not self.bin:
            for k, v in items:
                save(k)
                save(v)
                write(SETITEM)

            return
        r = xrange(self._BATCHSIZE)
        while items is not None:
            tmp = []
            for i in r:
                try:
                    tmp.append(items.next())
                except StopIteration:
                    items = None
                    break

            n = len(tmp)
            if n > 1:
                write(MARK)
                for k, v in tmp:
                    save(k)
                    save(v)

                write(SETITEMS)
            elif n:
                k, v = tmp[0]
                save(k)
                save(v)
                write(SETITEM)

        return

    def save_inst(self, obj):
        cls = obj.__class__
        memo = self.memo
        write = self.write
        save = self.save
        if hasattr(obj, b'__getinitargs__'):
            args = obj.__getinitargs__()
            len(args)
            _keep_alive(args, memo)
        else:
            args = ()
        write(MARK)
        if self.bin:
            save(cls)
            for arg in args:
                save(arg)

            write(OBJ)
        else:
            for arg in args:
                save(arg)

            write(INST + cls.__module__ + b'\n' + cls.__name__ + b'\n')
        self.memoize(obj)
        try:
            getstate = obj.__getstate__
        except AttributeError:
            stuff = obj.__dict__
        else:
            stuff = getstate()
            _keep_alive(stuff, memo)

        save(stuff)
        write(BUILD)
        return

    dispatch[InstanceType] = save_inst

    def save_global(self, obj, name=None, pack=struct.pack):
        write = self.write
        memo = self.memo
        if name is None:
            name = obj.__name__
        module = getattr(obj, b'__module__', None)
        if module is None:
            module = whichmodule(obj, name)
        try:
            __import__(module)
            mod = sys.modules[module]
            klass = getattr(mod, name)
        except (ImportError, KeyError, AttributeError):
            raise PicklingError(b"Can't pickle %r: it's not found as %s.%s" % (
             obj, module, name))

        if klass is not obj:
            raise PicklingError(b"Can't pickle %r: it's not the same object as %s.%s" % (
             obj, module, name))
        if self.proto >= 2:
            code = _extension_registry.get((module, name))
            if code:
                if code <= 255:
                    write(EXT1 + chr(code))
                elif code <= 65535:
                    write(b'%c%c%c' % (EXT2, code & 255, code >> 8))
                else:
                    write(EXT4 + pack(b'<i', code))
                return
        write(GLOBAL + module + b'\n' + name + b'\n')
        self.memoize(obj)
        return

    dispatch[ClassType] = save_global
    dispatch[FunctionType] = save_global
    dispatch[BuiltinFunctionType] = save_global
    dispatch[TypeType] = save_global


def _keep_alive(x, memo):
    try:
        memo[id(memo)].append(x)
    except KeyError:
        memo[id(memo)] = [
         x]

    return


classmap = {}

def whichmodule(func, funcname):
    mod = getattr(func, b'__module__', None)
    if mod is not None:
        return mod
    else:
        if func in classmap:
            return classmap[func]
        for name, module in sys.modules.items():
            if module is None:
                continue
            if name != b'__main__' and getattr(module, funcname, None) is func:
                break
        else:
            name = b'__main__'

        classmap[func] = name
        return name


class Unpickler():

    def __init__(self, file):
        self.readline = file.readline
        self.read = file.read
        self.memo = {}
        return

    def load(self):
        self.mark = object()
        self.stack = []
        self.append = self.stack.append
        read = self.read
        dispatch = self.dispatch
        try:
            while 1:
                key = read(1)
                dispatch[key](self)

        except _Stop as stopinst:
            return stopinst.value

        return

    def marker(self):
        stack = self.stack
        mark = self.mark
        k = len(stack) - 1
        while stack[k] is not mark:
            k = k - 1

        return k

    dispatch = {}

    def load_eof(self):
        raise EOFError
        return

    dispatch[b''] = load_eof

    def load_proto(self):
        proto = ord(self.read(1))
        if not 0 <= proto <= 2:
            raise ValueError, b'unsupported pickle protocol: %d' % proto
        return

    dispatch[PROTO] = load_proto

    def load_persid(self):
        pid = self.readline()[:-1]
        self.append(self.persistent_load(pid))
        return

    dispatch[PERSID] = load_persid

    def load_binpersid(self):
        pid = self.stack.pop()
        self.append(self.persistent_load(pid))
        return

    dispatch[BINPERSID] = load_binpersid

    def load_none(self):
        self.append(None)
        return

    dispatch[NONE] = load_none

    def load_false(self):
        self.append(False)
        return

    dispatch[NEWFALSE] = load_false

    def load_true(self):
        self.append(True)
        return

    dispatch[NEWTRUE] = load_true

    def load_int(self):
        data = self.readline()
        if data == FALSE[1:]:
            val = False
        elif data == TRUE[1:]:
            val = True
        else:
            try:
                val = int(data)
            except ValueError:
                val = long(data)

        self.append(val)
        return

    dispatch[INT] = load_int

    def load_binint(self):
        self.append(mloads(b'i' + self.read(4)))
        return

    dispatch[BININT] = load_binint

    def load_binint1(self):
        self.append(ord(self.read(1)))
        return

    dispatch[BININT1] = load_binint1

    def load_binint2(self):
        self.append(mloads(b'i' + self.read(2) + b'\x00\x00'))
        return

    dispatch[BININT2] = load_binint2

    def load_long(self):
        self.append(long(self.readline()[:-1], 0))
        return

    dispatch[LONG] = load_long

    def load_long1(self):
        n = ord(self.read(1))
        bytes = self.read(n)
        self.append(decode_long(bytes))
        return

    dispatch[LONG1] = load_long1

    def load_long4(self):
        n = mloads(b'i' + self.read(4))
        bytes = self.read(n)
        self.append(decode_long(bytes))
        return

    dispatch[LONG4] = load_long4

    def load_float(self):
        self.append(float(self.readline()[:-1]))
        return

    dispatch[FLOAT] = load_float

    def load_binfloat(self, unpack=struct.unpack):
        self.append(unpack(b'>d', self.read(8))[0])
        return

    dispatch[BINFLOAT] = load_binfloat

    def load_string(self):
        rep = self.readline()[:-1]
        for q in b'"\'':
            if rep.startswith(q):
                if len(rep) < 2 or not rep.endswith(q):
                    raise ValueError, b'insecure string pickle'
                rep = rep[len(q):-len(q)]
                break
        else:
            raise ValueError, b'insecure string pickle'

        self.append(rep.decode(b'string-escape'))
        return

    dispatch[STRING] = load_string

    def load_binstring(self):
        len = mloads(b'i' + self.read(4))
        self.append(self.read(len))
        return

    dispatch[BINSTRING] = load_binstring

    def load_unicode(self):
        self.append(unicode(self.readline()[:-1], b'raw-unicode-escape'))
        return

    dispatch[UNICODE] = load_unicode

    def load_binunicode(self):
        len = mloads(b'i' + self.read(4))
        self.append(unicode(self.read(len), b'utf-8'))
        return

    dispatch[BINUNICODE] = load_binunicode

    def load_short_binstring(self):
        len = ord(self.read(1))
        self.append(self.read(len))
        return

    dispatch[SHORT_BINSTRING] = load_short_binstring

    def load_tuple(self):
        k = self.marker()
        self.stack[k:] = [tuple(self.stack[k + 1:])]
        return

    dispatch[TUPLE] = load_tuple

    def load_empty_tuple(self):
        self.stack.append(())
        return

    dispatch[EMPTY_TUPLE] = load_empty_tuple

    def load_tuple1(self):
        self.stack[-1] = (
         self.stack[-1],)
        return

    dispatch[TUPLE1] = load_tuple1

    def load_tuple2(self):
        self.stack[(-2):] = [
         (
          self.stack[-2], self.stack[-1])]
        return

    dispatch[TUPLE2] = load_tuple2

    def load_tuple3(self):
        self.stack[(-3):] = [
         (
          self.stack[-3], self.stack[-2], self.stack[-1])]
        return

    dispatch[TUPLE3] = load_tuple3

    def load_empty_list(self):
        self.stack.append([])
        return

    dispatch[EMPTY_LIST] = load_empty_list

    def load_empty_dictionary(self):
        self.stack.append({})
        return

    dispatch[EMPTY_DICT] = load_empty_dictionary

    def load_list(self):
        k = self.marker()
        self.stack[k:] = [self.stack[k + 1:]]
        return

    dispatch[LIST] = load_list

    def load_dict(self):
        k = self.marker()
        d = {}
        items = self.stack[k + 1:]
        for i in range(0, len(items), 2):
            key = items[i]
            value = items[i + 1]
            d[key] = value

        self.stack[k:] = [
         d]
        return

    dispatch[DICT] = load_dict

    def _instantiate(self, klass, k):
        args = tuple(self.stack[k + 1:])
        del self.stack[k:]
        instantiated = 0
        if not args and type(klass) is ClassType and not hasattr(klass, b'__getinitargs__'):
            try:
                value = _EmptyClass()
                value.__class__ = klass
                instantiated = 1
            except RuntimeError:
                pass

        if not instantiated:
            try:
                value = klass(*args)
            except TypeError as err:
                raise TypeError, b'in constructor for %s: %s' % (
                 klass.__name__, str(err)), sys.exc_info()[2]

        self.append(value)
        return

    def load_inst(self):
        module = self.readline()[:-1]
        name = self.readline()[:-1]
        klass = self.find_class(module, name)
        self._instantiate(klass, self.marker())
        return

    dispatch[INST] = load_inst

    def load_obj(self):
        k = self.marker()
        klass = self.stack.pop(k + 1)
        self._instantiate(klass, k)
        return

    dispatch[OBJ] = load_obj

    def load_newobj(self):
        args = self.stack.pop()
        cls = self.stack[-1]
        obj = cls.__new__(cls, *args)
        self.stack[-1] = obj
        return

    dispatch[NEWOBJ] = load_newobj

    def load_global(self):
        module = self.readline()[:-1]
        name = self.readline()[:-1]
        klass = self.find_class(module, name)
        self.append(klass)
        return

    dispatch[GLOBAL] = load_global

    def load_ext1(self):
        code = ord(self.read(1))
        self.get_extension(code)
        return

    dispatch[EXT1] = load_ext1

    def load_ext2(self):
        code = mloads(b'i' + self.read(2) + b'\x00\x00')
        self.get_extension(code)
        return

    dispatch[EXT2] = load_ext2

    def load_ext4(self):
        code = mloads(b'i' + self.read(4))
        self.get_extension(code)
        return

    dispatch[EXT4] = load_ext4

    def get_extension(self, code):
        nil = []
        obj = _extension_cache.get(code, nil)
        if obj is not nil:
            self.append(obj)
            return
        key = _inverted_registry.get(code)
        if not key:
            raise ValueError(b'unregistered extension code %d' % code)
        obj = self.find_class(*key)
        _extension_cache[code] = obj
        self.append(obj)
        return

    def find_class(self, module, name):
        __import__(module)
        mod = sys.modules[module]
        klass = getattr(mod, name)
        return klass

    def load_reduce(self):
        stack = self.stack
        args = stack.pop()
        func = stack[-1]
        value = func(*args)
        stack[-1] = value
        return

    dispatch[REDUCE] = load_reduce

    def load_pop(self):
        del self.stack[-1]
        return

    dispatch[POP] = load_pop

    def load_pop_mark(self):
        k = self.marker()
        del self.stack[k:]
        return

    dispatch[POP_MARK] = load_pop_mark

    def load_dup(self):
        self.append(self.stack[-1])
        return

    dispatch[DUP] = load_dup

    def load_get(self):
        self.append(self.memo[self.readline()[:-1]])
        return

    dispatch[GET] = load_get

    def load_binget(self):
        i = ord(self.read(1))
        self.append(self.memo[repr(i)])
        return

    dispatch[BINGET] = load_binget

    def load_long_binget(self):
        i = mloads(b'i' + self.read(4))
        self.append(self.memo[repr(i)])
        return

    dispatch[LONG_BINGET] = load_long_binget

    def load_put(self):
        self.memo[self.readline()[:-1]] = self.stack[-1]
        return

    dispatch[PUT] = load_put

    def load_binput(self):
        i = ord(self.read(1))
        self.memo[repr(i)] = self.stack[-1]
        return

    dispatch[BINPUT] = load_binput

    def load_long_binput(self):
        i = mloads(b'i' + self.read(4))
        self.memo[repr(i)] = self.stack[-1]
        return

    dispatch[LONG_BINPUT] = load_long_binput

    def load_append(self):
        stack = self.stack
        value = stack.pop()
        list = stack[-1]
        list.append(value)
        return

    dispatch[APPEND] = load_append

    def load_appends(self):
        stack = self.stack
        mark = self.marker()
        list = stack[mark - 1]
        list.extend(stack[mark + 1:])
        del stack[mark:]
        return

    dispatch[APPENDS] = load_appends

    def load_setitem(self):
        stack = self.stack
        value = stack.pop()
        key = stack.pop()
        dict = stack[-1]
        dict[key] = value
        return

    dispatch[SETITEM] = load_setitem

    def load_setitems(self):
        stack = self.stack
        mark = self.marker()
        dict = stack[mark - 1]
        for i in range(mark + 1, len(stack), 2):
            dict[stack[i]] = stack[i + 1]

        del stack[mark:]
        return

    dispatch[SETITEMS] = load_setitems

    def load_build(self):
        stack = self.stack
        state = stack.pop()
        inst = stack[-1]
        setstate = getattr(inst, b'__setstate__', None)
        if setstate:
            setstate(state)
            return
        else:
            slotstate = None
            if isinstance(state, tuple) and len(state) == 2:
                state, slotstate = state
            if state:
                try:
                    d = inst.__dict__
                    try:
                        for k, v in state.iteritems():
                            d[intern(k)] = v

                    except TypeError:
                        d.update(state)

                except RuntimeError:
                    for k, v in state.items():
                        setattr(inst, k, v)

            if slotstate:
                for k, v in slotstate.items():
                    setattr(inst, k, v)

            return

    dispatch[BUILD] = load_build

    def load_mark(self):
        self.append(self.mark)
        return

    dispatch[MARK] = load_mark

    def load_stop(self):
        value = self.stack.pop()
        raise _Stop(value)
        return

    dispatch[STOP] = load_stop


class _EmptyClass():
    pass


import binascii as _binascii

def encode_long(x):
    if x == 0:
        return b''
    if x > 0:
        ashex = hex(x)
        njunkchars = 2 + ashex.endswith(b'L')
        nibbles = len(ashex) - njunkchars
        if nibbles & 1:
            ashex = b'0x0' + ashex[2:]
        elif int(ashex[2], 16) >= 8:
            ashex = b'0x00' + ashex[2:]
    else:
        ashex = hex(-x)
        njunkchars = 2 + ashex.endswith(b'L')
        nibbles = len(ashex) - njunkchars
        if nibbles & 1:
            nibbles += 1
        nbits = nibbles * 4
        x += 1L << nbits
        ashex = hex(x)
        njunkchars = 2 + ashex.endswith(b'L')
        newnibbles = len(ashex) - njunkchars
        if newnibbles < nibbles:
            ashex = b'0x' + b'0' * (nibbles - newnibbles) + ashex[2:]
        if int(ashex[2], 16) < 8:
            ashex = b'0xff' + ashex[2:]
    if ashex.endswith(b'L'):
        ashex = ashex[2:-1]
    else:
        ashex = ashex[2:]
    binary = _binascii.unhexlify(ashex)
    return binary[::-1]


def decode_long(data):
    nbytes = len(data)
    if nbytes == 0:
        return 0L
    ashex = _binascii.hexlify(data[::-1])
    n = long(ashex, 16)
    if data[-1] >= b'\x80':
        n -= 1L << nbytes * 8
    return n


try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

def dump(obj, file, protocol=None):
    Pickler(file, protocol).dump(obj)
    return


def dumps(obj, protocol=None):
    file = StringIO()
    Pickler(file, protocol).dump(obj)
    return file.getvalue()


def load(file):
    return Unpickler(file).load()


def loads(str):
    file = StringIO(str)
    return Unpickler(file).load()


def _test():
    import doctest
    return doctest.testmod()


if __name__ == b'__main__':
    _test()
