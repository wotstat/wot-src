from __future__ import absolute_import
import re, ResMgr
from soft_exception import SoftException
EXTENSION_RULES_FILE = b'scripts/extension_rules.xml'
g_cache = None

class READ_METHOD(object):
    MERGE = b'merge'
    INCLUDE = b'include'
    INCLUDE_BY_PATH = b'includeByPath'


def prepareRuleParams(params):
    if params:
        params = params.replace(b'\r\n', b' ')
        params = params.replace(b'\n', b' ')
    return params


def init():
    global g_cache
    if g_cache is not None:
        return
    else:
        g_cache = {}
        sec = ResMgr.openSection(EXTENSION_RULES_FILE)
        if not sec:
            raise SoftException(b"Fail to read '%s'" % EXTENSION_RULES_FILE)
        whitelist = sec[b'xml_whitelist']

        def getParams(rule):
            params = None if rule[b'params'] is None else rule[b'params'].asString
            return prepareRuleParams(params)

        g_cache[b'merge_whitelist'] = [(re.compile(rule[b'pattern'].asString), rule[b'type'].asString, getParams(rule)) for rule in whitelist.values()]
        ResMgr.purge(EXTENSION_RULES_FILE, True)
        return


def isExtXML(path):
    path = path.replace(b'\\', b'/')
    if g_cache is None:
        return (False, None, None)
    else:
        for pattern, method, params in g_cache.get(b'merge_whitelist', {}):
            if bool(pattern.match(path)):
                return (True, method, params)

        return (
         False, None, None)
