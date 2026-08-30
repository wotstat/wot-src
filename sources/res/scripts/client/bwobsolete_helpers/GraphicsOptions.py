import ResMgr, sys, BigWorld
tex_detail_levels = ResMgr.openSection(b'system/data/texture_detail_levels.xml')

def normalMapsCompressed():
    ns = tex_detail_levels.values()[0]
    if ns.readString(b'format') == b'A8R8G8B8':
        return False
    return True


def compressNormalMaps(state):
    ns = tex_detail_levels.values()[0]
    ns.writeString(b'format', b'A8R8G8B8')
    BigWorld.reloadTextures()
    return


def optIncludeOptionEnabled(value):
    filename = b'../../bigworld/res/shaders/std_effects/optinclude.fxh'
    try:
        f = open(filename, b'r')
    except IOError:
        print b'Failed to open %s' % (filename,)
        return

    output = []
    lines = f.readlines()
    changed = False
    found = False
    for line in lines:
        if value in line:
            found = True
            if b'//' in line:
                return False
            return True

    return False


def enableOptincludeOption(value, enable):
    filename = b'../../bigworld/res/shaders/std_effects/optinclude.fxh'
    try:
        f = open(filename, b'r')
    except IOError:
        print b'Failed to open %s' % (filename,)
        return

    output = []
    lines = f.readlines()
    changed = False
    found = False
    for line in lines:
        if value in line:
            found = True
            if b'//' in line:
                if enable:
                    line = b'#define ' + value + b' 1\n'
                    changed = True
            elif not enable:
                line = b'//#define ' + value + b' 1\n'
                changed = True
        output.append(line)

    if enable and not found:
        output.append(b'#define ' + value + b' 1')
        changed = True
    f.close()
    if changed and len(output) > 0:
        f = open(filename, b'w+')
        if f == None:
            print b'Could not open %s for writing' % (filename,)
            return
        f.writelines(output)
        f.close()
    return
