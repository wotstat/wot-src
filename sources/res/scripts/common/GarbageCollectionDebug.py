import re, sys, itertools
from bwdebug import DEBUG_MSG
from bwdebug import ERROR_MSG
import __builtin__ as builtins, BigWorld, StringIO, objgraph
LIMIT_LEN = False
MAX_LEN = 5
MAX_DEPTH = 1
TEST_SIMPLE_LEAK = False
TEST_COMPLEX_LEAK = False
EXCLUDED = dir(builtins) + [b'frame']
MAX_REFS_PER_GARBAGE = 10
MAX_DISPLAYABLE_GARBAGE_PER_ITERATION = 30
displayed_garbage = []
try:
    import gc
    GC_DEBUG_FLAGS = gc.DEBUG_SAVEALL
except ImportError:
    GC_DEBUG_FLAGS = 0

def gcEnable():
    try:
        import gc
        gc.enable()
    except ImportError:
        raise RuntimeError(b'Garbage collection is not supported')

    return


def gcDisable():
    try:
        import gc
        gc.disable()
    except ImportError:
        return

    return


def gcDebugEnable():
    try:
        import gc
        gc.set_debug(GC_DEBUG_FLAGS)
    except ImportError:
        ERROR_MSG(b'Could not import gc module; ' + b'garbage collection support is not compiled in')

    return


def gcIsLeakDetect():
    try:
        import gc
        if (gc.isenabled() and gc.get_debug() & gc.DEBUG_LEAK) > 0:
            return True
    except ImportError:
        ERROR_MSG(b'Could not import gc module; garbage collection support is not compiled in')

    return False


def gcWriteLog(file, s, isError=False):
    if isError:
        ERROR_MSG(s)
    else:
        DEBUG_MSG(s)
    if file is not None:
        file.write(s + b'\n')
        file.flush()
    return


def get_all_unique_loops(edges):
    leafs = True
    while leafs:
        srcs = set()
        trgts = set()
        for src, tgt in edges:
            srcs.add(src)
            trgts.add(tgt)

        leafs = trgts - srcs
        new_edges = []
        for src, tgt in edges:
            if tgt not in leafs:
                new_edges.append((src, tgt))

        edges = new_edges

    return edges


def get_loops_graph(content):
    lines = content.split(b';')
    g = re.compile(b'o\\d+')
    objs = [g.findall(i) for i in lines]
    edges = [i for i in objs if len(i) == 2]
    unique_loops = get_all_unique_loops(edges)
    nodes = set(j for i in unique_loops for j in i)
    result = []
    for line in lines:
        line_nodes = g.findall(line)
        if not line_nodes or all(i in nodes for i in line_nodes):
            result.append(line)

    return (b';').join(result)


def gcDump():
    try:
        import gc
    except ImportError:
        ERROR_MSG(b'Could not import gc module; ' + b'garbage collection support is not compiled in')
        return

    gcDebugEnable()
    DEBUG_MSG(b'Forcing a garbage collection...')
    leakCount = gc.collect()
    s = b'Total garbage: %u' % (leakCount,)
    gcWriteLog(None, s, isError=leakCount > 0)
    if leakCount:
        gc_dump = gc.garbage[:]
        garbageLen = len(gc_dump)
        if garbageLen > 0:
            garbage_data = get_garbage_data_with_extended_info(gc_dump)
            for data in garbage_data:
                logStr = (b'Source: {}. ').format(data[b'source'])
                if data[b'referents']:
                    logStr += (b'Referents: {}. ').format((b', ').join(data[b'referents']))
                if data[b'referrers']:
                    logStr += (b'Referrers: {}. ').format((b', ').join(data[b'referrers']))
                gcWriteLog(None, logStr)

            del gc_dump[:]
        if garbageLen > MAX_DISPLAYABLE_GARBAGE_PER_ITERATION:
            gcWriteLog(None, (b'{} elements omitted for performance purposes...').format(garbageLen - MAX_DISPLAYABLE_GARBAGE_PER_ITERATION))
    del gc.garbage[:]
    return leakCount


def get_garbage_data_with_extended_info(gc_dump):
    result = []

    def getName(obj, default=b'-'):
        gName = b''
        try:
            gName = obj.__class__.__name__
        except Exception:
            pass

        if gName:
            return gName
        return default

    def getRepr(obj, default=b'-'):
        gRepr = b''
        try:
            gRepr = repr(obj)
        except Exception:
            pass

        if gRepr:
            return gRepr[:100]
        return default

    def analyze_refs(refs):
        matchRefs = []
        refCounter = 0
        for ref in refs:
            name = getName(ref)
            if name and name not in EXCLUDED:
                matchRefs.append(name)
            refCounter += 1
            if refCounter >= MAX_REFS_PER_GARBAGE:
                break

        return matchRefs

    garbageCounter = 0
    for garbage in gc_dump:
        garbageID = id(garbage)
        if garbageID in displayed_garbage:
            continue
        result.append({b'source': (
                     id(garbage), type(garbage), getName(garbage, b'<indefinable>'),
                     getRepr(garbage, b'<cannot extract>')), 
           b'referents': (analyze_refs(gc.get_referents(garbage))), 
           b'referrers': (analyze_refs(gc.get_referrers(garbage)))})
        displayed_garbage.append(id(garbage))
        garbageCounter += 1
        if garbageCounter >= MAX_DISPLAYABLE_GARBAGE_PER_ITERATION:
            break

    return result


def get_refs(obj, source_list, known_ids, get_unknown_referents=False):
    if id(obj) in source_list:
        return ([], [])
    source_list.append(id(obj))
    res = []
    unknown_referents = []
    for i in gc.get_referents(obj):
        if id(i) in known_ids:
            res.append({b'target': (id(i)), b'source': (id(obj))})
        elif get_unknown_referents:
            unknown_referents.append(i)
            res.append({b'target': (id(i)), b'source': (id(obj))})

    return (
     res, unknown_referents)


def get_graph_text_repr(graph, garbage_ids, extra_info=False, refcounts=False, shortnames=True):
    node_names = {}
    for edge_data in graph:
        if edge_data[b'target'] not in garbage_ids or edge_data[b'source'] not in garbage_ids:
            continue
        obj_id = edge_data[b'source']
        target = garbage_ids[obj_id]
        for obj_id in (edge_data[b'source'], edge_data[b'target']):
            obj = garbage_ids[obj_id]
            node_names[obj_id] = {b'id': obj_id, 
               b'label': (objgraph._obj_label(obj, extra_info, refcounts, shortnames))}

        source = garbage_ids[edge_data[b'target']]
        edge_data[b'label'] = objgraph._edge_label(target, source)

    return {b'nodes': node_names, b'edges': graph}


def getGarbageGraph(depth=0):
    try:
        import gc
    except ImportError:
        message = b'Could not import gc module; garbage collection support is not compiled in'
        return message

    leakCount = 0
    gcDebugEnable()
    leakCount = gc.collect()
    gc_dump = gc.garbage[:]
    del gc.garbage[:]
    if len(gc_dump) > 0:
        garbage_ids = {id(x): x for x in gc_dump}
        garbage_list = []
        gc_refs = []
        new_objects = gc_dump
        for d in range(depth + 1):
            added_objects = []
            for obj in new_objects:
                graph_part, new_objects = get_refs(obj, garbage_list, garbage_ids, get_unknown_referents=d < depth)
                gc_refs.extend(graph_part)
                garbage_ids.update({id(obj): obj for obj in new_objects})
                added_objects.extend(new_objects)

            new_objects = added_objects

        del garbage_list[:]
        graph_info = get_graph_text_repr(gc_refs, garbage_ids, shortnames=False)
        result = b'digraph ObjectGraph { node[shape=box, style=filled, fillcolor=white];  %s }'
        node_items = [b'o%s[label="%s"]' % (i[b'id'], i[b'label']) for i in graph_info[b'nodes'].values()]
        edge_items = [b'o%s -> o%s %s' % (i[b'source'], i[b'target'], i.get(b'label', b'')) for i in graph_info[b'edges']]
        garbage_ids.clear()
        graph_info[b'nodes'].clear()
        del graph_info[b'edges'][:]
        del gc_refs[:]
        del gc_dump[:]
        return result % (b'; ').join(itertools.chain(node_items, edge_items))
    return


class TestLeak:
    pass


def createTestLeaks():
    if TEST_SIMPLE_LEAK:
        createBasicLeak()
    if TEST_COMPLEX_LEAK:
        createComplexLeak()
    return


def createBasicLeak():
    DEBUG_MSG(b'Creating a simple test leak..')
    ref = TestLeak()
    ref.selfRef = ref
    ref = None
    return


def createComplexLeak():
    DEBUG_MSG(b'Creating a complex test leak..')
    refChain = TestLeak()
    refLink1 = TestLeak()
    refLink2 = TestLeak()
    saltLink = TestLeak()
    refChain.badRefStart = refLink1
    refLink1.badRefMiddle = refLink2
    refLink2.saltValue = saltLink
    refLink2.badRefEnd = refChain
    refChain = None
    refLink1 = None
    refLink2 = None
    return


def getObjectData(obj, indent=b''):
    result = b''
    result += b'%sObject id %u\n' % (indent, id(obj))
    try:
        result += b'%s name: %s\n' % (indent, obj.__class__.__name__)
    except AttributeError:
        result += b'%s name: no name\n' % (indent,)

    result += b'%s type: %s\n' % (indent, type(obj))
    try:
        result += b'%s len : %u\n' % (indent, len(obj))
    except AttributeError:
        result += b'%s len : no length\n' % (indent,)
    except TypeError:
        result += b'%s len : no length\n' % (indent,)

    result += getContents(obj, indent)
    try:
        result += b'%s bytes: %u\n' % (indent, sys.getsizeof(obj))
    except ImportError:
        result += b'%s bytes: could not get size\n' % (indent,)

    return result


def getContents(obj, indent=b''):
    result = b''
    try:
        import pprint
        pp = pprint.PrettyPrinter(depth=MAX_DEPTH)
        if LIMIT_LEN:
            if len(obj) <= MAX_LEN:
                result += b'%s contents: %s\n' % (indent, pp.pformat(obj))
            else:
                short = obj[:MAX_LEN]
                result += b'%s partial contents (first %u): %s ...\n' % (indent, MAX_LEN, pp.pformat(short))
        else:
            result += b'%s contents: %s\n' % (indent, pp.pformat(obj))
    except ImportError as e:
        ERROR_MSG(b'Error: could not import pprint: %s' % (e,))
        raise
    except AttributeError:
        result += b'%s str : %s\n' % (indent, pp.pformat(obj))
    except TypeError:
        result += b'%s str : %s\n' % (indent, pp.pformat(obj))

    return result


def getObjectReferrers(obj, ignore):
    result = b''
    try:
        refCount = sys.getrefcount(obj)
        result += b' sys.getrefcount: %u\n' % (refCount,)
    except:
        pass

    referrers = None
    try:
        try:
            referrers = gc.get_referrers(obj)
            result += b' gc.get_referrers (%u):\n' % (len(referrers),)
            i = 0
            for r in referrers:
                try:
                    result += b' ->(referrer %u)\n' % (i,)
                    if r not in ignore:
                        result += getObjectData(r, b' -> ')
                    else:
                        result += b' -> reference from gc.garbage list (ignore)\n'
                except:
                    print b'Error getting referrer'

                i += 1

        except:
            result += b'Error getting referrers'

    finally:
        del referrers

    return result


def saveOptimizedGarbage(path):
    import gc, sys, inspect
    delimiter = b'=-=' * 100 + b'\n'
    logPattern = b'{}Representation str(garbageObject):\n{}\nObject type: {}\nRef count: {}\nModule of object: {}\n'
    gc.collect()
    gcGarbageCopy = gc.garbage[:]
    del gc.garbage[:]
    with open(path, b'w') as f:
        for garbageObject in gcGarbageCopy:
            try:
                f.write(logPattern.format(delimiter, str(garbageObject), type(garbageObject), sys.getrefcount(garbageObject), inspect.getmodule(garbageObject)))
            except:
                continue

    del gcGarbageCopy[:]
    return
