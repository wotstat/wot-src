import BigWorld, logging, struct
NewAPINotice = b'\nInstead of old SpaceData API, please use space properties:\nBigWorld.spaces[ spaceID ].property_name.\nUser level space properties must be defined in space .def file.\n'
WarningFlag = True

def ShowWarningOnce():
    global WarningFlag
    if WarningFlag:
        WarningFlag = False
        import inspect
        func_name = inspect.stack()[1][3]
        logging.warning(func_name + b': This API will be deprecated soon, please use the new API.' + b' All deprecated functions: delSpaceDataForKey,' + b' getSpaceDataFirstForKey, setSpaceData, setSpaceTimeOfDay,' + b' timeOfDay, setSpaceArtificialMinLoad')
    return


def getPropertyNameForKey(key):
    supportedKeys = {0: b'timeOfDay', 
       1: b'mappingKeyClientServer', 
       2: b'mappingKeyClientOnly', 
       32768: b'isRecording', 
       32769: b'artificialMinLoad', 
       32770: b'serverLoadBounds', 
       300: b'itemsVisibilityMask', 
       17408: b'recorderFragment', 
       16384: b'geometryLoaded', 
       16385: b'spaceLoader'}
    try:
        return supportedKeys[key]
    except KeyError:
        raise ValueError(b'SpaceData key ', key, b' is unsupported', NewAPINotice)

    return


def addSpaceData(spaceID, key, value):
    raise ValueError(b'addSpaceData is unsupported', NewAPINotice)
    return


def delSpaceData(spaceID, entryID):
    raise ValueError(b'delSpaceData is unsupported', NewAPINotice)
    return


def delSpaceDataForKey(spaceID, key):
    ShowWarningOnce()
    setSpaceData(spaceID, key, b'')
    return


def getSpaceData(spaceID, entryID, key):
    raise ValueError(b'getSpaceData is unsupported', NewAPINotice)
    return


def getSpaceDataFirstForKey(spaceID, key):
    try:
        ShowWarningOnce()
        if key == 0:
            tod = BigWorld.spaces[spaceID].timeOfDay
            return struct.pack(b'ff', tod.initialTimeOfDay, tod.gameSecondsPerSecond)
        return getattr(BigWorld.spaces[spaceID], getPropertyNameForKey(key))
    except AttributeError:
        raise AttributeError(b'SpaceDataObject has no property: ' + getPropertyNameForKey(key) + b'. User level space property must be defined' + b' in the space .def file.', NewAPINotice)

    return


def getSpaceDataForKey(spaceID, key):
    raise ValueError(b'getSpaceDataForKey is unsupported', NewAPINotice)
    return


def setSpaceData(spaceID, key, value):
    try:
        ShowWarningOnce()
        setattr(BigWorld.spaces[spaceID], getPropertyNameForKey(key), value)
        return key
    except AttributeError:
        raise AttributeError(b'SpaceDataObject has no property: ' + getPropertyNameForKey(key) + b'. User level space property must be defined' + b' in the space .def file.', NewAPINotice)

    return


def timeOfDay(spaceID):
    ShowWarningOnce()
    try:
        tod = BigWorld.spaces[spaceID].timeOfDay
        return BigWorld.time() * tod.gameSecondsPerSecond + tod.initialTimeOfDay
    except KeyError:
        logging.warning(b'BigWorld.timeOfDay( spaceID ): Space is not found, spaceID=' + str(spaceID))
        return -1.0

    return


def setSpaceTimeOfDay(spaceID, initialTimeOfDay, gameSecondsPerSecond):
    ShowWarningOnce()
    BigWorld.spaces[spaceID].timeOfDay = {b'initialTimeOfDay': initialTimeOfDay, 
       b'gameSecondsPerSecond': gameSecondsPerSecond}
    return 0


def addSpaceGeometryMapping(spaceID, mapper, path, shouldLoadOnServer=True):
    ShowWarningOnce()
    return BigWorld.spaces[spaceID].geometryMappings.add(path, mapper, shouldLoadOnServer)


def setSpaceArtificialMinLoad(spaceID, artificialMinLoad):
    ShowWarningOnce()
    BigWorld.spaces[spaceID].artificialMinLoad = artificialMinLoad
    return


def getSpaceGeometryMappings(spaceID):
    ShowWarningOnce()
    return BigWorld.spaces[spaceID].geometryMappings.values()


BigWorld.addSpaceData = addSpaceData
BigWorld.delSpaceData = delSpaceData
BigWorld.delSpaceDataForKey = delSpaceDataForKey
BigWorld.getSpaceData = getSpaceData
BigWorld.getSpaceDataFirstForKey = getSpaceDataFirstForKey
BigWorld.getSpaceDataForKey = getSpaceDataForKey
BigWorld.setSpaceData = setSpaceData
BigWorld.timeOfDay = timeOfDay
BigWorld.setSpaceTimeOfDay = setSpaceTimeOfDay
BigWorld.addSpaceGeometryMapping = addSpaceGeometryMapping
BigWorld.getSpaceGeometryMappings = getSpaceGeometryMappings
BigWorld.setSpaceArtificialMinLoad = setSpaceArtificialMinLoad
