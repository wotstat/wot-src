import ResMgr

def gatherChunks(spaceDir):
    if spaceDir[-1] != b'/':
        spaceDir = spaceDir + b'/'
    result = []
    entries = ResMgr.openSection(spaceDir)
    if entries:
        for entry in entries.keys():
            if entry[0] == b'.':
                continue
            if ResMgr.isDir(spaceDir + entry):
                children = gatherChunks(spaceDir + entry)
                result.extend(children)
            else:
                entry = entry.lower()
                if len(entry) == 15 and entry[-6:] == b'.chunk':
                    result.append(spaceDir + entry)

    return result


def validateShells(spaceDir):
    if spaceDir[-1] != b'/':
        spaceDir = spaceDir + b'/'
    chunks = gatherChunks(spaceDir)
    shells = [x for x in chunks if x[-7] == b'i']
    outsides = [x for x in chunks if x[-7] == b'o']
    for chunk in outsides:
        section = ResMgr.openSection(chunk)
        overlappers = section.readStrings(b'overlapper')
        for overlapper in overlappers:
            shell = spaceDir + overlapper + b'.chunk'
            if shell in shells:
                shells.remove(shell)

    print shells
    return
