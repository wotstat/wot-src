import os, shutil
from itertools import chain
g_staticComponents = [
 b'BattleRoyaleComponent']
g_dynamicComponents = [
 4, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13]
g_entities = [
 14, 
 15, 
 16, 
 17, 
 18]
g_misc = [
 b'vehicle_extras_battle_royale',
 b'vehicles/common/vehicle_battle_royale',
 b'vehicles/common/equipments/battle_royale_equipments']
g_all = g_staticComponents + g_dynamicComponents + g_entities + g_misc
ROOT_PATH = b'./'
EXT_PATH = b'../wot_ext/battle_royale/'
g_folders = [
 24, 
 25, 
 26, 
 27, 
 28, 
 29, 
 30, 
 31, 
 32]
g_exts = [
 b'.py',
 b'.def',
 b'.xml']
MODE = b'svn'
extensionXMLpattern = b"\n<root>\n    <!-- Arbitrary and unique feature name. It can match <extension_dir> but doesn't have to -->\n    <FeatureName>\n        BattleRoyale\n    </FeatureName>\n    <Components>\n        <StaticComponents>\n            {staticComponents}\n        </StaticComponents>\n        <DynamicComponents>\n            {dynamicComponents}\n        </DynamicComponents>\n    </Components>\n\n    <IsEnabled>\n        True\n    </IsEnabled>\n\n    <Entities>\n        <!-- The list of client-server entities in this feature extension -->\n        <ClientServerEntities>\n            {entities}\n        </ClientServerEntities>\n        <!-- The list of server-only entities in this feature extension -->\n        <ServerOnlyEntities>\n        </ServerOnlyEntities>\n    </Entities>\n\n    <ExternalComponents>\n        <!-- The list of components defined externally -->\n    </ExternalComponents>\n</root>\n"

def mkdir(path):
    try:
        result = os.makedirs(path)
        os.system((b'svn add {}').format(path))
        return result
    except OSError:
        if not os.path.isdir(path):
            raise

    return


def makedirsRecursive(name, mode=511):
    head, tail = os.path.split(name)
    if not tail:
        head, tail = os.path.split(head)
    if head and tail and not os.path.exists(head):
        try:
            makedirsRecursive(head, mode)
        except OSError as e:
            if e.errno != os.errno.EEXIST:
                raise

        if tail == os.curdir:
            return
    try:
        os.mkdir(name, mode)
        os.system((b'svn add {}').format(name))
    except OSError as e:
        if e.errno != os.errno.EEXIST:
            raise

    return


mkdir = makedirsRecursive

def copyFile(file, ext, folders):
    filename = file + ext
    for folder in folders:
        fullPathFrom = (b'{}scripts/{}/{}').format(ROOT_PATH, folder, filename)
        fullPathTo = (b'{}scripts/{}/{}').format(EXT_PATH, folder, filename)
        if os.path.exists(fullPathFrom):
            mkdir(os.path.dirname(fullPathTo))
            if MODE == b'move':
                os.rename(fullPathFrom, fullPathTo)
            elif MODE == b'svn':
                os.system((b'svn move {} {}').format(fullPathFrom, os.path.dirname(fullPathTo)))
            else:
                shutil.copyfile(fullPathFrom, fullPathTo)

    for xmlFile in (b'entities.xml', b'components.xml', b'user_data_objects.xml'):
        with open((b'{}scripts/{}').format(ROOT_PATH, xmlFile), b'r+') as f:
            old = f.read()
            f.seek(0)
            f.truncate()
            f.write(old.replace((b'<{}/>\n').format(file), b''))

    return


def copyExt(items, exts, folders):
    for file in items:
        for ext in exts:
            copyFile(file, ext, folders)

    return


def generateXML(staticComponents, dynamicComponents, entities):
    magic = b'\n\t\t\t'
    result = extensionXMLpattern.replace(b'{staticComponents}', magic.join([(b'<{}/>').format(name) for name in staticComponents])).replace(b'{dynamicComponents}', magic.join([(b'<{}/>').format(name) for name in dynamicComponents])).replace(b'{entities}', magic.join([(b'<{}/>').format(name) for name in entities]))
    with open(EXT_PATH + b'extension.xml', b'w') as f:
        f.write(result)
    return


mkdir(EXT_PATH + b'scripts')
copyExt(g_all, g_exts, g_folders)
generateXML(g_staticComponents, g_dynamicComponents, g_entities)
