import dis, types, sys
from compiler import misc
from compiler.consts import CO_OPTIMIZED, CO_NEWLOCALS, CO_VARARGS, CO_VARKEYWORDS

class FlowGraph():

    def __init__(self):
        self.current = self.entry = Block()
        self.exit = Block(b'exit')
        self.blocks = misc.Set()
        self.blocks.add(self.entry)
        self.blocks.add(self.exit)
        return

    def startBlock(self, block):
        if self._debug:
            if self.current:
                print b'end', repr(self.current)
                print b'    next', self.current.next
                print b'    prev', self.current.prev
                print b'   ', self.current.get_children()
            print repr(block)
        self.current = block
        return

    def nextBlock(self, block=None):
        if block is None:
            block = self.newBlock()
        self.current.addNext(block)
        self.startBlock(block)
        return

    def newBlock(self):
        b = Block()
        self.blocks.add(b)
        return b

    def startExitBlock(self):
        self.startBlock(self.exit)
        return

    _debug = 0

    def _enable_debug(self):
        self._debug = 1
        return

    def _disable_debug(self):
        self._debug = 0
        return

    def emit(self, *inst):
        if self._debug:
            print b'\t', inst
        if len(inst) == 2 and isinstance(inst[1], Block):
            self.current.addOutEdge(inst[1])
        self.current.emit(inst)
        return

    def getBlocksInOrder(self):
        order = order_blocks(self.entry, self.exit)
        return order

    def getBlocks(self):
        return self.blocks.elements()

    def getRoot(self):
        return self.entry

    def getContainedGraphs(self):
        l = []
        for b in self.getBlocks():
            l.extend(b.getContainedGraphs())

        return l


def order_blocks(start_block, exit_block):
    order = []
    remaining = set()
    todo = [start_block]
    while todo:
        b = todo.pop()
        if b in remaining:
            continue
        remaining.add(b)
        for c in b.get_children():
            if c not in remaining:
                todo.append(c)

    dominators = {}
    for b in remaining:
        if __debug__ and b.next:
            pass
        dominators.setdefault(b, set())
        for c in b.get_followers():
            while 1:
                dominators.setdefault(c, set()).add(b)
                if c.prev and c.prev[0] is not b:
                    c = c.prev[0]
                else:
                    break

    def find_next():
        for b in remaining:
            for c in dominators[b]:
                if c in remaining:
                    break
            else:
                return b

        return

    b = start_block
    while 1:
        order.append(b)
        remaining.discard(b)
        if b.next:
            b = b.next[0]
            continue
        elif b is not exit_block and not b.has_unconditional_transfer():
            order.append(exit_block)
        if not remaining:
            break
        b = find_next()

    return order


class Block():
    _count = 0

    def __init__(self, label=b''):
        self.insts = []
        self.outEdges = set()
        self.label = label
        self.bid = Block._count
        self.next = []
        self.prev = []
        Block._count = Block._count + 1
        return

    def __repr__(self):
        if self.label:
            return b'<block %s id=%d>' % (self.label, self.bid)
        else:
            return b'<block id=%d>' % self.bid

        return

    def __str__(self):
        insts = map(str, self.insts)
        return b'<block %s %d:\n%s>' % (self.label, self.bid,
         (b'\n').join(insts))

    def emit(self, inst):
        op = inst[0]
        self.insts.append(inst)
        return

    def getInstructions(self):
        return self.insts

    def addOutEdge(self, block):
        self.outEdges.add(block)
        return

    def addNext(self, block):
        self.next.append(block)
        block.prev.append(self)
        return

    _uncond_transfer = (b'RETURN_VALUE', b'RAISE_VARARGS', b'JUMP_ABSOLUTE', b'JUMP_FORWARD', b'CONTINUE_LOOP')

    def has_unconditional_transfer(self):
        try:
            op, arg = self.insts[-1]
        except (IndexError, ValueError):
            return

        return op in self._uncond_transfer

    def get_children(self):
        return list(self.outEdges) + self.next

    def get_followers(self):
        followers = set(self.next)
        for inst in self.insts:
            if inst[0] in PyFlowGraph.hasjrel:
                followers.add(inst[1])

        return followers

    def getContainedGraphs(self):
        contained = []
        for inst in self.insts:
            if len(inst) == 1:
                continue
            op = inst[1]
            if hasattr(op, b'graph'):
                contained.append(op.graph)

        return contained


RAW = b'RAW'
FLAT = b'FLAT'
CONV = b'CONV'
DONE = b'DONE'

class PyFlowGraph(FlowGraph):
    super_init = FlowGraph.__init__

    def __init__(self, name, filename, args=(), optimized=0, klass=None):
        self.super_init()
        self.name = name
        self.filename = filename
        self.docstring = None
        self.args = args
        self.argcount = getArgCount(args)
        self.klass = klass
        if optimized:
            self.flags = CO_OPTIMIZED | CO_NEWLOCALS
        else:
            self.flags = 0
        self.consts = []
        self.names = []
        self.freevars = []
        self.cellvars = []
        self.closure = []
        self.varnames = list(args) or []
        for i in range(len(self.varnames)):
            var = self.varnames[i]
            if isinstance(var, TupleArg):
                self.varnames[i] = var.getName()

        self.stage = RAW
        return

    def setDocstring(self, doc):
        self.docstring = doc
        return

    def setFlag(self, flag):
        self.flags = self.flags | flag
        if flag == CO_VARARGS:
            self.argcount = self.argcount - 1
        return

    def checkFlag(self, flag):
        if self.flags & flag:
            return 1
        return

    def setFreeVars(self, names):
        self.freevars = list(names)
        return

    def setCellVars(self, names):
        self.cellvars = names
        return

    def getCode(self):
        self.computeStackDepth()
        self.flattenGraph()
        self.convertArgs()
        self.makeByteCode()
        return self.newCodeObject()

    def dump(self, io=None):
        if io:
            save = sys.stdout
            sys.stdout = io
        pc = 0
        for t in self.insts:
            opname = t[0]
            if opname == b'SET_LINENO':
                print
            if len(t) == 1:
                print b'\t', b'%3d' % pc, opname
                pc = pc + 1
            else:
                print b'\t', b'%3d' % pc, opname, t[1]
                pc = pc + 3

        if io:
            sys.stdout = save
        return

    def computeStackDepth(self):
        depth = {}
        exit = None
        for b in self.getBlocks():
            depth[b] = findDepth(b.getInstructions())

        seen = {}

        def max_depth(b, d):
            if b in seen:
                return d
            else:
                seen[b] = 1
                d = d + depth[b]
                children = b.get_children()
                if children:
                    return max([max_depth(c, d) for c in children])
                if not b.label == b'exit':
                    return max_depth(self.exit, d)
                return d

            return

        self.stacksize = max_depth(self.entry, 0)
        return

    def flattenGraph(self):
        self.insts = insts = []
        pc = 0
        begin = {}
        end = {}
        for b in self.getBlocksInOrder():
            begin[b] = pc
            for inst in b.getInstructions():
                insts.append(inst)
                if len(inst) == 1:
                    pc = pc + 1
                elif inst[0] != b'SET_LINENO':
                    pc = pc + 3

            end[b] = pc

        pc = 0
        for i in range(len(insts)):
            inst = insts[i]
            if len(inst) == 1:
                pc = pc + 1
            elif inst[0] != b'SET_LINENO':
                pc = pc + 3
            opname = inst[0]
            if opname in self.hasjrel:
                oparg = inst[1]
                offset = begin[oparg] - pc
                insts[i] = (opname, offset)
            elif opname in self.hasjabs:
                insts[i] = (
                 opname, begin[inst[1]])

        self.stage = FLAT
        return

    hasjrel = set()
    for i in dis.hasjrel:
        hasjrel.add(dis.opname[i])

    hasjabs = set()
    for i in dis.hasjabs:
        hasjabs.add(dis.opname[i])

    def convertArgs(self):
        self.consts.insert(0, self.docstring)
        self.sort_cellvars()
        for i in range(len(self.insts)):
            t = self.insts[i]
            if len(t) == 2:
                opname, oparg = t
                conv = self._converters.get(opname, None)
                if conv:
                    self.insts[i] = (
                     opname, conv(self, oparg))

        self.stage = CONV
        return

    def sort_cellvars(self):
        cells = {}
        for name in self.cellvars:
            cells[name] = 1

        self.cellvars = [name for name in self.varnames if name in cells]
        for name in self.cellvars:
            del cells[name]

        self.cellvars = self.cellvars + cells.keys()
        self.closure = self.cellvars + self.freevars
        return

    def _lookupName(self, name, list):
        t = type(name)
        for i in range(len(list)):
            if t == type(list[i]) and list[i] == name:
                return i

        end = len(list)
        list.append(name)
        return end

    _converters = {}

    def _convert_LOAD_CONST(self, arg):
        if hasattr(arg, b'getCode'):
            arg = arg.getCode()
        return self._lookupName(arg, self.consts)

    def _convert_LOAD_FAST(self, arg):
        self._lookupName(arg, self.names)
        return self._lookupName(arg, self.varnames)

    _convert_STORE_FAST = _convert_LOAD_FAST
    _convert_DELETE_FAST = _convert_LOAD_FAST

    def _convert_LOAD_NAME(self, arg):
        if self.klass is None:
            self._lookupName(arg, self.varnames)
        return self._lookupName(arg, self.names)

    def _convert_NAME(self, arg):
        if self.klass is None:
            self._lookupName(arg, self.varnames)
        return self._lookupName(arg, self.names)

    _convert_STORE_NAME = _convert_NAME
    _convert_DELETE_NAME = _convert_NAME
    _convert_IMPORT_NAME = _convert_NAME
    _convert_IMPORT_FROM = _convert_NAME
    _convert_STORE_ATTR = _convert_NAME
    _convert_LOAD_ATTR = _convert_NAME
    _convert_DELETE_ATTR = _convert_NAME
    _convert_LOAD_GLOBAL = _convert_NAME
    _convert_STORE_GLOBAL = _convert_NAME
    _convert_DELETE_GLOBAL = _convert_NAME

    def _convert_DEREF(self, arg):
        self._lookupName(arg, self.names)
        self._lookupName(arg, self.varnames)
        return self._lookupName(arg, self.closure)

    _convert_LOAD_DEREF = _convert_DEREF
    _convert_STORE_DEREF = _convert_DEREF

    def _convert_LOAD_CLOSURE(self, arg):
        self._lookupName(arg, self.varnames)
        return self._lookupName(arg, self.closure)

    _cmp = list(dis.cmp_op)

    def _convert_COMPARE_OP(self, arg):
        return self._cmp.index(arg)

    for name, obj in locals().items():
        if name[:9] == b'_convert_':
            opname = name[9:]
            _converters[opname] = obj

    del name
    del obj
    del opname

    def makeByteCode(self):
        self.lnotab = lnotab = LineAddrTable()
        for t in self.insts:
            opname = t[0]
            if len(t) == 1:
                lnotab.addCode(self.opnum[opname])
            else:
                oparg = t[1]
                if opname == b'SET_LINENO':
                    lnotab.nextLine(oparg)
                    continue
                hi, lo = twobyte(oparg)
                try:
                    lnotab.addCode(self.opnum[opname], lo, hi)
                except ValueError:
                    print opname, oparg
                    print self.opnum[opname], lo, hi
                    raise

        self.stage = DONE
        return

    opnum = {}
    for num in range(len(dis.opname)):
        opnum[dis.opname[num]] = num

    del num

    def newCodeObject(self):
        if self.flags & CO_NEWLOCALS == 0:
            nlocals = 0
        else:
            nlocals = len(self.varnames)
        argcount = self.argcount
        if self.flags & CO_VARKEYWORDS:
            argcount = argcount - 1
        return types.CodeType(argcount, nlocals, self.stacksize, self.flags, self.lnotab.getCode(), self.getConsts(), tuple(self.names), tuple(self.varnames), self.filename, self.name, self.lnotab.firstline, self.lnotab.getTable(), tuple(self.freevars), tuple(self.cellvars))

    def getConsts(self):
        l = []
        for elt in self.consts:
            if isinstance(elt, PyFlowGraph):
                elt = elt.getCode()
            l.append(elt)

        return tuple(l)


def isJump(opname):
    if opname[:4] == b'JUMP':
        return 1
    return


class TupleArg():

    def __init__(self, count, names):
        self.count = count
        self.names = names
        return

    def __repr__(self):
        return b'TupleArg(%s, %s)' % (self.count, self.names)

    def getName(self):
        return b'.%d' % self.count


def getArgCount(args):
    argcount = len(args)
    if args:
        for arg in args:
            if isinstance(arg, TupleArg):
                numNames = len(misc.flatten(arg.names))
                argcount = argcount - numNames

    return argcount


def twobyte(val):
    return divmod(val, 256)


class LineAddrTable():

    def __init__(self):
        self.code = []
        self.codeOffset = 0
        self.firstline = 0
        self.lastline = 0
        self.lastoff = 0
        self.lnotab = []
        return

    def addCode(self, *args):
        for arg in args:
            self.code.append(chr(arg))

        self.codeOffset = self.codeOffset + len(args)
        return

    def nextLine(self, lineno):
        if self.firstline == 0:
            self.firstline = lineno
            self.lastline = lineno
        else:
            addr = self.codeOffset - self.lastoff
            line = lineno - self.lastline
            if line >= 0:
                push = self.lnotab.append
                while addr > 255:
                    push(255)
                    push(0)
                    addr -= 255

                while line > 255:
                    push(addr)
                    push(255)
                    line -= 255
                    addr = 0

                if addr > 0 or line > 0:
                    push(addr)
                    push(line)
                self.lastline = lineno
                self.lastoff = self.codeOffset
        return

    def getCode(self):
        return (b'').join(self.code)

    def getTable(self):
        return (b'').join(map(chr, self.lnotab))


class StackDepthTracker():

    def findDepth(self, insts, debug=0):
        depth = 0
        maxDepth = 0
        for i in insts:
            opname = i[0]
            if debug:
                print i,
            delta = self.effect.get(opname, None)
            if delta is not None:
                depth = depth + delta
            else:
                for pat, pat_delta in self.patterns:
                    if opname[:len(pat)] == pat:
                        delta = pat_delta
                        depth = depth + delta
                        break

                if delta is None:
                    meth = getattr(self, opname, None)
                    if meth is not None:
                        depth = depth + meth(i[1])
            if depth > maxDepth:
                maxDepth = depth
            if debug:
                print depth, maxDepth

        return maxDepth

    effect = {b'POP_TOP': (-1), 
       b'DUP_TOP': 1, 
       b'LIST_APPEND': (-1), 
       b'SET_ADD': (-1), 
       b'MAP_ADD': (-2), 
       b'SLICE+1': (-1), 
       b'SLICE+2': (-1), 
       b'SLICE+3': (-2), 
       b'STORE_SLICE+0': (-1), 
       b'STORE_SLICE+1': (-2), 
       b'STORE_SLICE+2': (-2), 
       b'STORE_SLICE+3': (-3), 
       b'DELETE_SLICE+0': (-1), 
       b'DELETE_SLICE+1': (-2), 
       b'DELETE_SLICE+2': (-2), 
       b'DELETE_SLICE+3': (-3), 
       b'STORE_SUBSCR': (-3), 
       b'DELETE_SUBSCR': (-2), 
       b'PRINT_ITEM': (-1), 
       b'RETURN_VALUE': (-1), 
       b'YIELD_VALUE': (-1), 
       b'EXEC_STMT': (-3), 
       b'BUILD_CLASS': (-2), 
       b'STORE_NAME': (-1), 
       b'STORE_ATTR': (-2), 
       b'DELETE_ATTR': (-1), 
       b'STORE_GLOBAL': (-1), 
       b'BUILD_MAP': 1, 
       b'COMPARE_OP': (-1), 
       b'STORE_FAST': (-1), 
       b'IMPORT_STAR': (-1), 
       b'IMPORT_NAME': (-1), 
       b'IMPORT_FROM': 1, 
       b'LOAD_ATTR': 0, 
       b'SETUP_EXCEPT': 3, 
       b'SETUP_FINALLY': 3, 
       b'FOR_ITER': 1, 
       b'WITH_CLEANUP': (-1)}
    patterns = [
     (b'BINARY_', -1),
     (b'LOAD_', 1)]

    def UNPACK_SEQUENCE(self, count):
        return count - 1

    def BUILD_TUPLE(self, count):
        return -count + 1

    def BUILD_LIST(self, count):
        return -count + 1

    def BUILD_SET(self, count):
        return -count + 1

    def CALL_FUNCTION(self, argc):
        hi, lo = divmod(argc, 256)
        return -(lo + hi * 2)

    def CALL_FUNCTION_VAR(self, argc):
        return self.CALL_FUNCTION(argc) - 1

    def CALL_FUNCTION_KW(self, argc):
        return self.CALL_FUNCTION(argc) - 1

    def CALL_FUNCTION_VAR_KW(self, argc):
        return self.CALL_FUNCTION(argc) - 2

    def MAKE_FUNCTION(self, argc):
        return -argc

    def MAKE_CLOSURE(self, argc):
        return -argc

    def BUILD_SLICE(self, argc):
        if argc == 2:
            return -1
        if argc == 3:
            return -2
        return

    def DUP_TOPX(self, argc):
        return argc


findDepth = StackDepthTracker().findDepth
