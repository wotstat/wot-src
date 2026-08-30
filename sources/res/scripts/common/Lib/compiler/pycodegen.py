import imp, os, marshal, struct, sys
from cStringIO import StringIO
from compiler import ast, parse, walk, syntax
from compiler import pyassem, misc, future, symbols
from compiler.consts import SC_LOCAL, SC_GLOBAL_IMPLICIT, SC_GLOBAL_EXPLICIT, SC_FREE, SC_CELL
from compiler.consts import CO_VARARGS, CO_VARKEYWORDS, CO_NEWLOCALS, CO_NESTED, CO_GENERATOR, CO_FUTURE_DIVISION, CO_FUTURE_ABSIMPORT, CO_FUTURE_WITH_STATEMENT, CO_FUTURE_PRINT_FUNCTION
from compiler.pyassem import TupleArg
try:
    VERSION = sys.version_info[0]
except AttributeError:
    VERSION = 1

callfunc_opcode_info = {(0, 0): b'CALL_FUNCTION', 
   (1, 0): b'CALL_FUNCTION_VAR', 
   (0, 1): b'CALL_FUNCTION_KW', 
   (1, 1): b'CALL_FUNCTION_VAR_KW'}
LOOP = 1
EXCEPT = 2
TRY_FINALLY = 3
END_FINALLY = 4

def compileFile(filename, display=0):
    f = open(filename, b'U')
    buf = f.read()
    f.close()
    mod = Module(buf, filename)
    try:
        mod.compile(display)
    except SyntaxError:
        raise
    else:
        f = open(filename + b'c', b'wb')
        mod.dump(f)
        f.close()

    return


def compile(source, filename, mode, flags=None, dont_inherit=None):
    if flags is not None or dont_inherit is not None:
        raise RuntimeError, b'not implemented yet'
    if mode == b'single':
        gen = Interactive(source, filename)
    elif mode == b'exec':
        gen = Module(source, filename)
    elif mode == b'eval':
        gen = Expression(source, filename)
    else:
        raise ValueError(b"compile() 3rd arg must be 'exec' or 'eval' or 'single'")
    gen.compile()
    return gen.code


class AbstractCompileMode():
    mode = None

    def __init__(self, source, filename):
        self.source = source
        self.filename = filename
        self.code = None
        return

    def _get_tree(self):
        tree = parse(self.source, self.mode)
        misc.set_filename(self.filename, tree)
        syntax.check(tree)
        return tree

    def compile(self):
        return

    def getCode(self):
        return self.code


class Expression(AbstractCompileMode):
    mode = b'eval'

    def compile(self):
        tree = self._get_tree()
        gen = ExpressionCodeGenerator(tree)
        self.code = gen.getCode()
        return


class Interactive(AbstractCompileMode):
    mode = b'single'

    def compile(self):
        tree = self._get_tree()
        gen = InteractiveCodeGenerator(tree)
        self.code = gen.getCode()
        return


class Module(AbstractCompileMode):
    mode = b'exec'

    def compile(self, display=0):
        tree = self._get_tree()
        gen = ModuleCodeGenerator(tree)
        if display:
            import pprint
            print pprint.pprint(tree)
        self.code = gen.getCode()
        return

    def dump(self, f):
        f.write(self.getPycHeader())
        marshal.dump(self.code, f)
        return

    MAGIC = imp.get_magic()

    def getPycHeader(self):
        mtime = os.path.getmtime(self.filename)
        mtime = struct.pack(b'<i', mtime)
        return self.MAGIC + mtime


class LocalNameFinder():

    def __init__(self, names=()):
        self.names = misc.Set()
        self.globals = misc.Set()
        for name in names:
            self.names.add(name)

        return

    def getLocals(self):
        for elt in self.globals.elements():
            if self.names.has_elt(elt):
                self.names.remove(elt)

        return self.names

    def visitDict(self, node):
        return

    def visitGlobal(self, node):
        for name in node.names:
            self.globals.add(name)

        return

    def visitFunction(self, node):
        self.names.add(node.name)
        return

    def visitLambda(self, node):
        return

    def visitImport(self, node):
        for name, alias in node.names:
            self.names.add(alias or name)

        return

    def visitFrom(self, node):
        for name, alias in node.names:
            self.names.add(alias or name)

        return

    def visitClass(self, node):
        self.names.add(node.name)
        return

    def visitAssName(self, node):
        self.names.add(node.name)
        return


def is_constant_false(node):
    if isinstance(node, ast.Const):
        if not node.value:
            return 1
    return 0


class CodeGenerator():
    optimized = 0
    __initialized = None
    class_name = None

    def __init__(self):
        if self.__initialized is None:
            self.initClass()
            self.__class__.__initialized = 1
        self.checkClass()
        self.locals = misc.Stack()
        self.setups = misc.Stack()
        self.last_lineno = None
        self._setupGraphDelegation()
        self._div_op = b'BINARY_DIVIDE'
        futures = self.get_module().futures
        for feature in futures:
            if feature == b'division':
                self.graph.setFlag(CO_FUTURE_DIVISION)
                self._div_op = b'BINARY_TRUE_DIVIDE'
            elif feature == b'absolute_import':
                self.graph.setFlag(CO_FUTURE_ABSIMPORT)
            elif feature == b'with_statement':
                self.graph.setFlag(CO_FUTURE_WITH_STATEMENT)
            elif feature == b'print_function':
                self.graph.setFlag(CO_FUTURE_PRINT_FUNCTION)

        return

    def initClass(self):
        return

    def checkClass(self):
        try:
            pass
        except AssertionError as msg:
            intro = b'Bad class construction for %s' % self.__class__.__name__
            raise AssertionError, intro

        return

    def _setupGraphDelegation(self):
        self.emit = self.graph.emit
        self.newBlock = self.graph.newBlock
        self.startBlock = self.graph.startBlock
        self.nextBlock = self.graph.nextBlock
        self.setDocstring = self.graph.setDocstring
        return

    def getCode(self):
        return self.graph.getCode()

    def mangle(self, name):
        if self.class_name is not None:
            return misc.mangle(name, self.class_name)
        else:
            return name
            return

    def parseSymbols(self, tree):
        s = symbols.SymbolVisitor()
        walk(tree, s)
        return s.scopes

    def get_module(self):
        raise RuntimeError, b'should be implemented by subclasses'
        return

    def isLocalName(self, name):
        return self.locals.top().has_elt(name)

    def storeName(self, name):
        self._nameOp(b'STORE', name)
        return

    def loadName(self, name):
        self._nameOp(b'LOAD', name)
        return

    def delName(self, name):
        self._nameOp(b'DELETE', name)
        return

    def _nameOp(self, prefix, name):
        name = self.mangle(name)
        scope = self.scope.check_name(name)
        if scope == SC_LOCAL:
            if not self.optimized:
                self.emit(prefix + b'_NAME', name)
            else:
                self.emit(prefix + b'_FAST', name)
        elif scope == SC_GLOBAL_EXPLICIT:
            self.emit(prefix + b'_GLOBAL', name)
        elif scope == SC_GLOBAL_IMPLICIT:
            if not self.optimized:
                self.emit(prefix + b'_NAME', name)
            else:
                self.emit(prefix + b'_GLOBAL', name)
        elif scope == SC_FREE or scope == SC_CELL:
            self.emit(prefix + b'_DEREF', name)
        else:
            raise RuntimeError, b'unsupported scope for var %s: %d' % (
             name, scope)
        return

    def _implicitNameOp(self, prefix, name):
        if self.optimized:
            self.emit(prefix + b'_FAST', name)
        else:
            self.emit(prefix + b'_NAME', name)
        return

    def set_lineno(self, node, force=False):
        lineno = getattr(node, b'lineno', None)
        if lineno is not None and (lineno != self.last_lineno or force):
            self.emit(b'SET_LINENO', lineno)
            self.last_lineno = lineno
            return True
        else:
            return False

    NameFinder = LocalNameFinder
    FunctionGen = None
    ClassGen = None

    def visitModule(self, node):
        self.scopes = self.parseSymbols(node)
        self.scope = self.scopes[node]
        self.emit(b'SET_LINENO', 0)
        if node.doc:
            self.emit(b'LOAD_CONST', node.doc)
            self.storeName(b'__doc__')
        lnf = walk(node.node, self.NameFinder(), verbose=0)
        self.locals.push(lnf.getLocals())
        self.visit(node.node)
        self.emit(b'LOAD_CONST', None)
        self.emit(b'RETURN_VALUE')
        return

    def visitExpression(self, node):
        self.set_lineno(node)
        self.scopes = self.parseSymbols(node)
        self.scope = self.scopes[node]
        self.visit(node.node)
        self.emit(b'RETURN_VALUE')
        return

    def visitFunction(self, node):
        self._visitFuncOrLambda(node, isLambda=0)
        if node.doc:
            self.setDocstring(node.doc)
        self.storeName(node.name)
        return

    def visitLambda(self, node):
        self._visitFuncOrLambda(node, isLambda=1)
        return

    def _visitFuncOrLambda(self, node, isLambda=0):
        if not isLambda and node.decorators:
            for decorator in node.decorators.nodes:
                self.visit(decorator)

            ndecorators = len(node.decorators.nodes)
        else:
            ndecorators = 0
        gen = self.FunctionGen(node, self.scopes, isLambda, self.class_name, self.get_module())
        walk(node.code, gen)
        gen.finish()
        self.set_lineno(node)
        for default in node.defaults:
            self.visit(default)

        self._makeClosure(gen, len(node.defaults))
        for i in range(ndecorators):
            self.emit(b'CALL_FUNCTION', 1)

        return

    def visitClass(self, node):
        gen = self.ClassGen(node, self.scopes, self.get_module())
        walk(node.code, gen)
        gen.finish()
        self.set_lineno(node)
        self.emit(b'LOAD_CONST', node.name)
        for base in node.bases:
            self.visit(base)

        self.emit(b'BUILD_TUPLE', len(node.bases))
        self._makeClosure(gen, 0)
        self.emit(b'CALL_FUNCTION', 0)
        self.emit(b'BUILD_CLASS')
        self.storeName(node.name)
        return

    def visitIf(self, node):
        end = self.newBlock()
        numtests = len(node.tests)
        for i in range(numtests):
            test, suite = node.tests[i]
            if is_constant_false(test):
                continue
            self.set_lineno(test)
            self.visit(test)
            nextTest = self.newBlock()
            self.emit(b'POP_JUMP_IF_FALSE', nextTest)
            self.nextBlock()
            self.visit(suite)
            self.emit(b'JUMP_FORWARD', end)
            self.startBlock(nextTest)

        if node.else_:
            self.visit(node.else_)
        self.nextBlock(end)
        return

    def visitWhile(self, node):
        self.set_lineno(node)
        loop = self.newBlock()
        else_ = self.newBlock()
        after = self.newBlock()
        self.emit(b'SETUP_LOOP', after)
        self.nextBlock(loop)
        self.setups.push((LOOP, loop))
        self.set_lineno(node, force=True)
        self.visit(node.test)
        self.emit(b'POP_JUMP_IF_FALSE', else_ or after)
        self.nextBlock()
        self.visit(node.body)
        self.emit(b'JUMP_ABSOLUTE', loop)
        self.startBlock(else_)
        self.emit(b'POP_BLOCK')
        self.setups.pop()
        if node.else_:
            self.visit(node.else_)
        self.nextBlock(after)
        return

    def visitFor(self, node):
        start = self.newBlock()
        anchor = self.newBlock()
        after = self.newBlock()
        self.setups.push((LOOP, start))
        self.set_lineno(node)
        self.emit(b'SETUP_LOOP', after)
        self.visit(node.list)
        self.emit(b'GET_ITER')
        self.nextBlock(start)
        self.set_lineno(node, force=1)
        self.emit(b'FOR_ITER', anchor)
        self.visit(node.assign)
        self.visit(node.body)
        self.emit(b'JUMP_ABSOLUTE', start)
        self.nextBlock(anchor)
        self.emit(b'POP_BLOCK')
        self.setups.pop()
        if node.else_:
            self.visit(node.else_)
        self.nextBlock(after)
        return

    def visitBreak(self, node):
        if not self.setups:
            raise SyntaxError, b"'break' outside loop (%s, %d)" % (
             node.filename, node.lineno)
        self.set_lineno(node)
        self.emit(b'BREAK_LOOP')
        return

    def visitContinue(self, node):
        if not self.setups:
            raise SyntaxError, b"'continue' outside loop (%s, %d)" % (
             node.filename, node.lineno)
        kind, block = self.setups.top()
        if kind == LOOP:
            self.set_lineno(node)
            self.emit(b'JUMP_ABSOLUTE', block)
            self.nextBlock()
        elif kind == EXCEPT or kind == TRY_FINALLY:
            self.set_lineno(node)
            top = len(self.setups)
            while top > 0:
                top = top - 1
                kind, loop_block = self.setups[top]
                if kind == LOOP:
                    break

            if kind != LOOP:
                raise SyntaxError, b"'continue' outside loop (%s, %d)" % (
                 node.filename, node.lineno)
            self.emit(b'CONTINUE_LOOP', loop_block)
            self.nextBlock()
        elif kind == END_FINALLY:
            msg = b"'continue' not allowed inside 'finally' clause (%s, %d)"
            raise SyntaxError, msg % (node.filename, node.lineno)
        return

    def visitTest(self, node, jump):
        end = self.newBlock()
        for child in node.nodes[:-1]:
            self.visit(child)
            self.emit(jump, end)
            self.nextBlock()

        self.visit(node.nodes[-1])
        self.nextBlock(end)
        return

    def visitAnd(self, node):
        self.visitTest(node, b'JUMP_IF_FALSE_OR_POP')
        return

    def visitOr(self, node):
        self.visitTest(node, b'JUMP_IF_TRUE_OR_POP')
        return

    def visitIfExp(self, node):
        endblock = self.newBlock()
        elseblock = self.newBlock()
        self.visit(node.test)
        self.emit(b'POP_JUMP_IF_FALSE', elseblock)
        self.visit(node.then)
        self.emit(b'JUMP_FORWARD', endblock)
        self.nextBlock(elseblock)
        self.visit(node.else_)
        self.nextBlock(endblock)
        return

    def visitCompare(self, node):
        self.visit(node.expr)
        cleanup = self.newBlock()
        for op, code in node.ops[:-1]:
            self.visit(code)
            self.emit(b'DUP_TOP')
            self.emit(b'ROT_THREE')
            self.emit(b'COMPARE_OP', op)
            self.emit(b'JUMP_IF_FALSE_OR_POP', cleanup)
            self.nextBlock()

        if node.ops:
            op, code = node.ops[-1]
            self.visit(code)
            self.emit(b'COMPARE_OP', op)
        if len(node.ops) > 1:
            end = self.newBlock()
            self.emit(b'JUMP_FORWARD', end)
            self.startBlock(cleanup)
            self.emit(b'ROT_TWO')
            self.emit(b'POP_TOP')
            self.nextBlock(end)
        return

    def visitListComp(self, node):
        self.set_lineno(node)
        self.emit(b'BUILD_LIST', 0)
        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)

            stack.insert(0, (start, cont, anchor))

        self.visit(node.expr)
        self.emit(b'LIST_APPEND', len(node.quals) + 1)
        for start, cont, anchor in stack:
            if cont:
                self.nextBlock(cont)
            self.emit(b'JUMP_ABSOLUTE', start)
            self.startBlock(anchor)

        return

    def visitSetComp(self, node):
        self.set_lineno(node)
        self.emit(b'BUILD_SET', 0)
        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)

            stack.insert(0, (start, cont, anchor))

        self.visit(node.expr)
        self.emit(b'SET_ADD', len(node.quals) + 1)
        for start, cont, anchor in stack:
            if cont:
                self.nextBlock(cont)
            self.emit(b'JUMP_ABSOLUTE', start)
            self.startBlock(anchor)

        return

    def visitDictComp(self, node):
        self.set_lineno(node)
        self.emit(b'BUILD_MAP', 0)
        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)

            stack.insert(0, (start, cont, anchor))

        self.visit(node.value)
        self.visit(node.key)
        self.emit(b'MAP_ADD', len(node.quals) + 1)
        for start, cont, anchor in stack:
            if cont:
                self.nextBlock(cont)
            self.emit(b'JUMP_ABSOLUTE', start)
            self.startBlock(anchor)

        return

    def visitListCompFor(self, node):
        start = self.newBlock()
        anchor = self.newBlock()
        self.visit(node.list)
        self.emit(b'GET_ITER')
        self.nextBlock(start)
        self.set_lineno(node, force=True)
        self.emit(b'FOR_ITER', anchor)
        self.nextBlock()
        self.visit(node.assign)
        return (start, anchor)

    def visitListCompIf(self, node, branch):
        self.set_lineno(node, force=True)
        self.visit(node.test)
        self.emit(b'POP_JUMP_IF_FALSE', branch)
        self.newBlock()
        return

    def _makeClosure(self, gen, args):
        frees = gen.scope.get_free_vars()
        if frees:
            for name in frees:
                self.emit(b'LOAD_CLOSURE', name)

            self.emit(b'BUILD_TUPLE', len(frees))
            self.emit(b'LOAD_CONST', gen)
            self.emit(b'MAKE_CLOSURE', args)
        else:
            self.emit(b'LOAD_CONST', gen)
            self.emit(b'MAKE_FUNCTION', args)
        return

    def visitGenExpr(self, node):
        gen = GenExprCodeGenerator(node, self.scopes, self.class_name, self.get_module())
        walk(node.code, gen)
        gen.finish()
        self.set_lineno(node)
        self._makeClosure(gen, 0)
        self.visit(node.code.quals[0].iter)
        self.emit(b'GET_ITER')
        self.emit(b'CALL_FUNCTION', 1)
        return

    def visitGenExprInner(self, node):
        self.set_lineno(node)
        stack = []
        for i, for_ in zip(range(len(node.quals)), node.quals):
            start, anchor, end = self.visit(for_)
            cont = None
            for if_ in for_.ifs:
                if cont is None:
                    cont = self.newBlock()
                self.visit(if_, cont)

            stack.insert(0, (start, cont, anchor, end))

        self.visit(node.expr)
        self.emit(b'YIELD_VALUE')
        self.emit(b'POP_TOP')
        for start, cont, anchor, end in stack:
            if cont:
                self.nextBlock(cont)
            self.emit(b'JUMP_ABSOLUTE', start)
            self.startBlock(anchor)
            self.emit(b'POP_BLOCK')
            self.setups.pop()
            self.nextBlock(end)

        self.emit(b'LOAD_CONST', None)
        return

    def visitGenExprFor(self, node):
        start = self.newBlock()
        anchor = self.newBlock()
        end = self.newBlock()
        self.setups.push((LOOP, start))
        self.emit(b'SETUP_LOOP', end)
        if node.is_outmost:
            self.loadName(b'.0')
        else:
            self.visit(node.iter)
            self.emit(b'GET_ITER')
        self.nextBlock(start)
        self.set_lineno(node, force=True)
        self.emit(b'FOR_ITER', anchor)
        self.nextBlock()
        self.visit(node.assign)
        return (start, anchor, end)

    def visitGenExprIf(self, node, branch):
        self.set_lineno(node, force=True)
        self.visit(node.test)
        self.emit(b'POP_JUMP_IF_FALSE', branch)
        self.newBlock()
        return

    def visitAssert(self, node):
        return

    def visitRaise(self, node):
        self.set_lineno(node)
        n = 0
        if node.expr1:
            self.visit(node.expr1)
            n = n + 1
        if node.expr2:
            self.visit(node.expr2)
            n = n + 1
        if node.expr3:
            self.visit(node.expr3)
            n = n + 1
        self.emit(b'RAISE_VARARGS', n)
        return

    def visitTryExcept(self, node):
        body = self.newBlock()
        handlers = self.newBlock()
        end = self.newBlock()
        if node.else_:
            lElse = self.newBlock()
        else:
            lElse = end
        self.set_lineno(node)
        self.emit(b'SETUP_EXCEPT', handlers)
        self.nextBlock(body)
        self.setups.push((EXCEPT, body))
        self.visit(node.body)
        self.emit(b'POP_BLOCK')
        self.setups.pop()
        self.emit(b'JUMP_FORWARD', lElse)
        self.startBlock(handlers)
        last = len(node.handlers) - 1
        for i in range(len(node.handlers)):
            expr, target, body = node.handlers[i]
            self.set_lineno(expr)
            if expr:
                self.emit(b'DUP_TOP')
                self.visit(expr)
                self.emit(b'COMPARE_OP', b'exception match')
                next = self.newBlock()
                self.emit(b'POP_JUMP_IF_FALSE', next)
                self.nextBlock()
            self.emit(b'POP_TOP')
            if target:
                self.visit(target)
            else:
                self.emit(b'POP_TOP')
            self.emit(b'POP_TOP')
            self.visit(body)
            self.emit(b'JUMP_FORWARD', end)
            if expr:
                self.nextBlock(next)
            else:
                self.nextBlock()

        self.emit(b'END_FINALLY')
        if node.else_:
            self.nextBlock(lElse)
            self.visit(node.else_)
        self.nextBlock(end)
        return

    def visitTryFinally(self, node):
        body = self.newBlock()
        final = self.newBlock()
        self.set_lineno(node)
        self.emit(b'SETUP_FINALLY', final)
        self.nextBlock(body)
        self.setups.push((TRY_FINALLY, body))
        self.visit(node.body)
        self.emit(b'POP_BLOCK')
        self.setups.pop()
        self.emit(b'LOAD_CONST', None)
        self.nextBlock(final)
        self.setups.push((END_FINALLY, final))
        self.visit(node.final)
        self.emit(b'END_FINALLY')
        self.setups.pop()
        return

    __with_count = 0

    def visitWith(self, node):
        body = self.newBlock()
        final = self.newBlock()
        self.__with_count += 1
        valuevar = b'_[%d]' % self.__with_count
        self.set_lineno(node)
        self.visit(node.expr)
        self.emit(b'DUP_TOP')
        self.emit(b'LOAD_ATTR', b'__exit__')
        self.emit(b'ROT_TWO')
        self.emit(b'LOAD_ATTR', b'__enter__')
        self.emit(b'CALL_FUNCTION', 0)
        if node.vars is None:
            self.emit(b'POP_TOP')
        else:
            self._implicitNameOp(b'STORE', valuevar)
        self.emit(b'SETUP_FINALLY', final)
        self.nextBlock(body)
        self.setups.push((TRY_FINALLY, body))
        if node.vars is not None:
            self._implicitNameOp(b'LOAD', valuevar)
            self._implicitNameOp(b'DELETE', valuevar)
            self.visit(node.vars)
        self.visit(node.body)
        self.emit(b'POP_BLOCK')
        self.setups.pop()
        self.emit(b'LOAD_CONST', None)
        self.nextBlock(final)
        self.setups.push((END_FINALLY, final))
        self.emit(b'WITH_CLEANUP')
        self.emit(b'END_FINALLY')
        self.setups.pop()
        self.__with_count -= 1
        return

    def visitDiscard(self, node):
        self.set_lineno(node)
        self.visit(node.expr)
        self.emit(b'POP_TOP')
        return

    def visitConst(self, node):
        self.emit(b'LOAD_CONST', node.value)
        return

    def visitKeyword(self, node):
        self.emit(b'LOAD_CONST', node.name)
        self.visit(node.expr)
        return

    def visitGlobal(self, node):
        return

    def visitName(self, node):
        self.set_lineno(node)
        self.loadName(node.name)
        return

    def visitPass(self, node):
        self.set_lineno(node)
        return

    def visitImport(self, node):
        self.set_lineno(node)
        level = 0 if self.graph.checkFlag(CO_FUTURE_ABSIMPORT) else -1
        for name, alias in node.names:
            if VERSION > 1:
                self.emit(b'LOAD_CONST', level)
                self.emit(b'LOAD_CONST', None)
            self.emit(b'IMPORT_NAME', name)
            mod = name.split(b'.')[0]
            if alias:
                self._resolveDots(name)
                self.storeName(alias)
            else:
                self.storeName(mod)

        return

    def visitFrom(self, node):
        self.set_lineno(node)
        level = node.level
        if level == 0 and not self.graph.checkFlag(CO_FUTURE_ABSIMPORT):
            level = -1
        fromlist = tuple(name for name, alias in node.names)
        if VERSION > 1:
            self.emit(b'LOAD_CONST', level)
            self.emit(b'LOAD_CONST', fromlist)
        self.emit(b'IMPORT_NAME', node.modname)
        for name, alias in node.names:
            if VERSION > 1:
                if name == b'*':
                    self.namespace = 0
                    self.emit(b'IMPORT_STAR')
                    return
                self.emit(b'IMPORT_FROM', name)
                self._resolveDots(name)
                self.storeName(alias or name)
            else:
                self.emit(b'IMPORT_FROM', name)

        self.emit(b'POP_TOP')
        return

    def _resolveDots(self, name):
        elts = name.split(b'.')
        if len(elts) == 1:
            return
        for elt in elts[1:]:
            self.emit(b'LOAD_ATTR', elt)

        return

    def visitGetattr(self, node):
        self.visit(node.expr)
        self.emit(b'LOAD_ATTR', self.mangle(node.attrname))
        return

    def visitAssign(self, node):
        self.set_lineno(node)
        self.visit(node.expr)
        dups = len(node.nodes) - 1
        for i in range(len(node.nodes)):
            elt = node.nodes[i]
            if i < dups:
                self.emit(b'DUP_TOP')
            if isinstance(elt, ast.Node):
                self.visit(elt)

        return

    def visitAssName(self, node):
        if node.flags == b'OP_ASSIGN':
            self.storeName(node.name)
        elif node.flags == b'OP_DELETE':
            self.set_lineno(node)
            self.delName(node.name)
        else:
            print b'oops', node.flags
        return

    def visitAssAttr(self, node):
        self.visit(node.expr)
        if node.flags == b'OP_ASSIGN':
            self.emit(b'STORE_ATTR', self.mangle(node.attrname))
        elif node.flags == b'OP_DELETE':
            self.emit(b'DELETE_ATTR', self.mangle(node.attrname))
        else:
            print b'warning: unexpected flags:', node.flags
            print node
        return

    def _visitAssSequence(self, node, op=b'UNPACK_SEQUENCE'):
        if findOp(node) != b'OP_DELETE':
            self.emit(op, len(node.nodes))
        for child in node.nodes:
            self.visit(child)

        return

    if VERSION > 1:
        visitAssTuple = _visitAssSequence
        visitAssList = _visitAssSequence
    else:

        def visitAssTuple(self, node):
            self._visitAssSequence(node, b'UNPACK_TUPLE')
            return

        def visitAssList(self, node):
            self._visitAssSequence(node, b'UNPACK_LIST')
            return

    def visitAugAssign(self, node):
        self.set_lineno(node)
        aug_node = wrap_aug(node.node)
        self.visit(aug_node, b'load')
        self.visit(node.expr)
        self.emit(self._augmented_opcode[node.op])
        self.visit(aug_node, b'store')
        return

    _augmented_opcode = {b'+=': b'INPLACE_ADD', 
       b'-=': b'INPLACE_SUBTRACT', 
       b'*=': b'INPLACE_MULTIPLY', 
       b'/=': b'INPLACE_DIVIDE', 
       b'//=': b'INPLACE_FLOOR_DIVIDE', 
       b'%=': b'INPLACE_MODULO', 
       b'**=': b'INPLACE_POWER', 
       b'>>=': b'INPLACE_RSHIFT', 
       b'<<=': b'INPLACE_LSHIFT', 
       b'&=': b'INPLACE_AND', 
       b'^=': b'INPLACE_XOR', 
       b'|=': b'INPLACE_OR'}

    def visitAugName(self, node, mode):
        if mode == b'load':
            self.loadName(node.name)
        elif mode == b'store':
            self.storeName(node.name)
        return

    def visitAugGetattr(self, node, mode):
        if mode == b'load':
            self.visit(node.expr)
            self.emit(b'DUP_TOP')
            self.emit(b'LOAD_ATTR', self.mangle(node.attrname))
        elif mode == b'store':
            self.emit(b'ROT_TWO')
            self.emit(b'STORE_ATTR', self.mangle(node.attrname))
        return

    def visitAugSlice(self, node, mode):
        if mode == b'load':
            self.visitSlice(node, 1)
        elif mode == b'store':
            slice = 0
            if node.lower:
                slice = slice | 1
            if node.upper:
                slice = slice | 2
            if slice == 0:
                self.emit(b'ROT_TWO')
            elif slice == 3:
                self.emit(b'ROT_FOUR')
            else:
                self.emit(b'ROT_THREE')
            self.emit(b'STORE_SLICE+%d' % slice)
        return

    def visitAugSubscript(self, node, mode):
        if mode == b'load':
            self.visitSubscript(node, 1)
        elif mode == b'store':
            self.emit(b'ROT_THREE')
            self.emit(b'STORE_SUBSCR')
        return

    def visitExec(self, node):
        self.visit(node.expr)
        if node.locals is None:
            self.emit(b'LOAD_CONST', None)
        else:
            self.visit(node.locals)
        if node.globals is None:
            self.emit(b'DUP_TOP')
        else:
            self.visit(node.globals)
        self.emit(b'EXEC_STMT')
        return

    def visitCallFunc(self, node):
        pos = 0
        kw = 0
        self.set_lineno(node)
        self.visit(node.node)
        for arg in node.args:
            self.visit(arg)
            if isinstance(arg, ast.Keyword):
                kw = kw + 1
            else:
                pos = pos + 1

        if node.star_args is not None:
            self.visit(node.star_args)
        if node.dstar_args is not None:
            self.visit(node.dstar_args)
        have_star = node.star_args is not None
        have_dstar = node.dstar_args is not None
        opcode = callfunc_opcode_info[have_star, have_dstar]
        self.emit(opcode, kw << 8 | pos)
        return

    def visitPrint(self, node, newline=0):
        self.set_lineno(node)
        if node.dest:
            self.visit(node.dest)
        for child in node.nodes:
            if node.dest:
                self.emit(b'DUP_TOP')
            self.visit(child)
            if node.dest:
                self.emit(b'ROT_TWO')
                self.emit(b'PRINT_ITEM_TO')
            else:
                self.emit(b'PRINT_ITEM')

        if node.dest and not newline:
            self.emit(b'POP_TOP')
        return

    def visitPrintnl(self, node):
        self.visitPrint(node, newline=1)
        if node.dest:
            self.emit(b'PRINT_NEWLINE_TO')
        else:
            self.emit(b'PRINT_NEWLINE')
        return

    def visitReturn(self, node):
        self.set_lineno(node)
        self.visit(node.value)
        self.emit(b'RETURN_VALUE')
        return

    def visitYield(self, node):
        self.set_lineno(node)
        self.visit(node.value)
        self.emit(b'YIELD_VALUE')
        return

    def visitSlice(self, node, aug_flag=None):
        self.visit(node.expr)
        slice = 0
        if node.lower:
            self.visit(node.lower)
            slice = slice | 1
        if node.upper:
            self.visit(node.upper)
            slice = slice | 2
        if aug_flag:
            if slice == 0:
                self.emit(b'DUP_TOP')
            elif slice == 3:
                self.emit(b'DUP_TOPX', 3)
            else:
                self.emit(b'DUP_TOPX', 2)
        if node.flags == b'OP_APPLY':
            self.emit(b'SLICE+%d' % slice)
        elif node.flags == b'OP_ASSIGN':
            self.emit(b'STORE_SLICE+%d' % slice)
        elif node.flags == b'OP_DELETE':
            self.emit(b'DELETE_SLICE+%d' % slice)
        else:
            print b'weird slice', node.flags
            raise
        return

    def visitSubscript(self, node, aug_flag=None):
        self.visit(node.expr)
        for sub in node.subs:
            self.visit(sub)

        if len(node.subs) > 1:
            self.emit(b'BUILD_TUPLE', len(node.subs))
        if aug_flag:
            self.emit(b'DUP_TOPX', 2)
        if node.flags == b'OP_APPLY':
            self.emit(b'BINARY_SUBSCR')
        elif node.flags == b'OP_ASSIGN':
            self.emit(b'STORE_SUBSCR')
        elif node.flags == b'OP_DELETE':
            self.emit(b'DELETE_SUBSCR')
        return

    def binaryOp(self, node, op):
        self.visit(node.left)
        self.visit(node.right)
        self.emit(op)
        return

    def visitAdd(self, node):
        return self.binaryOp(node, b'BINARY_ADD')

    def visitSub(self, node):
        return self.binaryOp(node, b'BINARY_SUBTRACT')

    def visitMul(self, node):
        return self.binaryOp(node, b'BINARY_MULTIPLY')

    def visitDiv(self, node):
        return self.binaryOp(node, self._div_op)

    def visitFloorDiv(self, node):
        return self.binaryOp(node, b'BINARY_FLOOR_DIVIDE')

    def visitMod(self, node):
        return self.binaryOp(node, b'BINARY_MODULO')

    def visitPower(self, node):
        return self.binaryOp(node, b'BINARY_POWER')

    def visitLeftShift(self, node):
        return self.binaryOp(node, b'BINARY_LSHIFT')

    def visitRightShift(self, node):
        return self.binaryOp(node, b'BINARY_RSHIFT')

    def unaryOp(self, node, op):
        self.visit(node.expr)
        self.emit(op)
        return

    def visitInvert(self, node):
        return self.unaryOp(node, b'UNARY_INVERT')

    def visitUnarySub(self, node):
        return self.unaryOp(node, b'UNARY_NEGATIVE')

    def visitUnaryAdd(self, node):
        return self.unaryOp(node, b'UNARY_POSITIVE')

    def visitUnaryInvert(self, node):
        return self.unaryOp(node, b'UNARY_INVERT')

    def visitNot(self, node):
        return self.unaryOp(node, b'UNARY_NOT')

    def visitBackquote(self, node):
        return self.unaryOp(node, b'UNARY_CONVERT')

    def bitOp(self, nodes, op):
        self.visit(nodes[0])
        for node in nodes[1:]:
            self.visit(node)
            self.emit(op)

        return

    def visitBitand(self, node):
        return self.bitOp(node.nodes, b'BINARY_AND')

    def visitBitor(self, node):
        return self.bitOp(node.nodes, b'BINARY_OR')

    def visitBitxor(self, node):
        return self.bitOp(node.nodes, b'BINARY_XOR')

    def visitEllipsis(self, node):
        self.emit(b'LOAD_CONST', Ellipsis)
        return

    def visitTuple(self, node):
        self.set_lineno(node)
        for elt in node.nodes:
            self.visit(elt)

        self.emit(b'BUILD_TUPLE', len(node.nodes))
        return

    def visitList(self, node):
        self.set_lineno(node)
        for elt in node.nodes:
            self.visit(elt)

        self.emit(b'BUILD_LIST', len(node.nodes))
        return

    def visitSet(self, node):
        self.set_lineno(node)
        for elt in node.nodes:
            self.visit(elt)

        self.emit(b'BUILD_SET', len(node.nodes))
        return

    def visitSliceobj(self, node):
        for child in node.nodes:
            self.visit(child)

        self.emit(b'BUILD_SLICE', len(node.nodes))
        return

    def visitDict(self, node):
        self.set_lineno(node)
        self.emit(b'BUILD_MAP', 0)
        for k, v in node.items:
            self.emit(b'DUP_TOP')
            self.visit(k)
            self.visit(v)
            self.emit(b'ROT_THREE')
            self.emit(b'STORE_SUBSCR')

        return


class NestedScopeMixin():

    def initClass(self):
        self.__class__.NameFinder = LocalNameFinder
        self.__class__.FunctionGen = FunctionCodeGenerator
        self.__class__.ClassGen = ClassCodeGenerator
        return


class ModuleCodeGenerator(NestedScopeMixin, CodeGenerator):
    __super_init = CodeGenerator.__init__
    scopes = None

    def __init__(self, tree):
        self.graph = pyassem.PyFlowGraph(b'<module>', tree.filename)
        self.futures = future.find_futures(tree)
        self.__super_init()
        walk(tree, self)
        return

    def get_module(self):
        return self


class ExpressionCodeGenerator(NestedScopeMixin, CodeGenerator):
    __super_init = CodeGenerator.__init__
    scopes = None
    futures = ()

    def __init__(self, tree):
        self.graph = pyassem.PyFlowGraph(b'<expression>', tree.filename)
        self.__super_init()
        walk(tree, self)
        return

    def get_module(self):
        return self


class InteractiveCodeGenerator(NestedScopeMixin, CodeGenerator):
    __super_init = CodeGenerator.__init__
    scopes = None
    futures = ()

    def __init__(self, tree):
        self.graph = pyassem.PyFlowGraph(b'<interactive>', tree.filename)
        self.__super_init()
        self.set_lineno(tree)
        walk(tree, self)
        self.emit(b'RETURN_VALUE')
        return

    def get_module(self):
        return self

    def visitDiscard(self, node):
        self.visit(node.expr)
        self.emit(b'PRINT_EXPR')
        return


class AbstractFunctionCode():
    optimized = 1
    lambdaCount = 0

    def __init__(self, func, scopes, isLambda, class_name, mod):
        self.class_name = class_name
        self.module = mod
        if isLambda:
            klass = FunctionCodeGenerator
            name = b'<lambda.%d>' % klass.lambdaCount
            klass.lambdaCount = klass.lambdaCount + 1
        else:
            name = func.name
        args, hasTupleArg = generateArgList(func.argnames)
        self.graph = pyassem.PyFlowGraph(name, func.filename, args, optimized=1)
        self.isLambda = isLambda
        self.super_init()
        if not isLambda and func.doc:
            self.setDocstring(func.doc)
        lnf = walk(func.code, self.NameFinder(args), verbose=0)
        self.locals.push(lnf.getLocals())
        if func.varargs:
            self.graph.setFlag(CO_VARARGS)
        if func.kwargs:
            self.graph.setFlag(CO_VARKEYWORDS)
        self.set_lineno(func)
        if hasTupleArg:
            self.generateArgUnpack(func.argnames)
        return

    def get_module(self):
        return self.module

    def finish(self):
        self.graph.startExitBlock()
        if not self.isLambda:
            self.emit(b'LOAD_CONST', None)
        self.emit(b'RETURN_VALUE')
        return

    def generateArgUnpack(self, args):
        for i in range(len(args)):
            arg = args[i]
            if isinstance(arg, tuple):
                self.emit(b'LOAD_FAST', b'.%d' % (i * 2))
                self.unpackSequence(arg)

        return

    def unpackSequence(self, tup):
        if VERSION > 1:
            self.emit(b'UNPACK_SEQUENCE', len(tup))
        else:
            self.emit(b'UNPACK_TUPLE', len(tup))
        for elt in tup:
            if isinstance(elt, tuple):
                self.unpackSequence(elt)
            else:
                self._nameOp(b'STORE', elt)

        return

    unpackTuple = unpackSequence


class FunctionCodeGenerator(NestedScopeMixin, AbstractFunctionCode, CodeGenerator):
    super_init = CodeGenerator.__init__
    scopes = None
    __super_init = AbstractFunctionCode.__init__

    def __init__(self, func, scopes, isLambda, class_name, mod):
        self.scopes = scopes
        self.scope = scopes[func]
        self.__super_init(func, scopes, isLambda, class_name, mod)
        self.graph.setFreeVars(self.scope.get_free_vars())
        self.graph.setCellVars(self.scope.get_cell_vars())
        if self.scope.generator is not None:
            self.graph.setFlag(CO_GENERATOR)
        return


class GenExprCodeGenerator(NestedScopeMixin, AbstractFunctionCode, CodeGenerator):
    super_init = CodeGenerator.__init__
    scopes = None
    __super_init = AbstractFunctionCode.__init__

    def __init__(self, gexp, scopes, class_name, mod):
        self.scopes = scopes
        self.scope = scopes[gexp]
        self.__super_init(gexp, scopes, 1, class_name, mod)
        self.graph.setFreeVars(self.scope.get_free_vars())
        self.graph.setCellVars(self.scope.get_cell_vars())
        self.graph.setFlag(CO_GENERATOR)
        return


class AbstractClassCode():

    def __init__(self, klass, scopes, module):
        self.class_name = klass.name
        self.module = module
        self.graph = pyassem.PyFlowGraph(klass.name, klass.filename, optimized=0, klass=1)
        self.super_init()
        lnf = walk(klass.code, self.NameFinder(), verbose=0)
        self.locals.push(lnf.getLocals())
        self.graph.setFlag(CO_NEWLOCALS)
        if klass.doc:
            self.setDocstring(klass.doc)
        return

    def get_module(self):
        return self.module

    def finish(self):
        self.graph.startExitBlock()
        self.emit(b'LOAD_LOCALS')
        self.emit(b'RETURN_VALUE')
        return


class ClassCodeGenerator(NestedScopeMixin, AbstractClassCode, CodeGenerator):
    super_init = CodeGenerator.__init__
    scopes = None
    __super_init = AbstractClassCode.__init__

    def __init__(self, klass, scopes, module):
        self.scopes = scopes
        self.scope = scopes[klass]
        self.__super_init(klass, scopes, module)
        self.graph.setFreeVars(self.scope.get_free_vars())
        self.graph.setCellVars(self.scope.get_cell_vars())
        self.set_lineno(klass)
        self.emit(b'LOAD_GLOBAL', b'__name__')
        self.storeName(b'__module__')
        if klass.doc:
            self.emit(b'LOAD_CONST', klass.doc)
            self.storeName(b'__doc__')
        return


def generateArgList(arglist):
    args = []
    extra = []
    count = 0
    for i in range(len(arglist)):
        elt = arglist[i]
        if isinstance(elt, str):
            args.append(elt)
        elif isinstance(elt, tuple):
            args.append(TupleArg(i * 2, elt))
            extra.extend(misc.flatten(elt))
            count = count + 1
        else:
            raise ValueError, b'unexpect argument type:', elt

    return (
     args + extra, count)


def findOp(node):
    v = OpFinder()
    walk(node, v, verbose=0)
    return v.op


class OpFinder():

    def __init__(self):
        self.op = None
        return

    def visitAssName(self, node):
        if self.op is None:
            self.op = node.flags
        elif self.op != node.flags:
            raise ValueError, b'mixed ops in stmt'
        return

    visitAssAttr = visitAssName
    visitSubscript = visitAssName


class Delegator():

    def __init__(self, obj):
        self.obj = obj
        return

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


class AugGetattr(Delegator):
    pass


class AugName(Delegator):
    pass


class AugSlice(Delegator):
    pass


class AugSubscript(Delegator):
    pass


wrapper = {(ast.Getattr): AugGetattr, 
   (ast.Name): AugName, 
   (ast.Slice): AugSlice, 
   (ast.Subscript): AugSubscript}

def wrap_aug(node):
    return wrapper[node.__class__](node)


if __name__ == b'__main__':
    for file in sys.argv[1:]:
        compileFile(file)
