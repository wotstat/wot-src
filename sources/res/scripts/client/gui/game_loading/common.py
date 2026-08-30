import os, json, typing, logging
_logger = logging.getLogger(__name__)

def loadDictFromJsonFile(filePath):
    loaded = None
    try:
        _logger.debug(b'Loading data from json file: [%s].', filePath)
        if os.path.isfile(filePath):
            with open(filePath, b'rb') as jsonFile:
                _loaded = json.load(jsonFile)
            if not isinstance(_loaded, dict):
                _logger.error(b'Json: [%s] data type mismatch. %s != %s.', filePath, type(_loaded), dict)
            else:
                loaded = _loaded
        else:
            _logger.debug(b'[%s] does not exist or is not a file.', filePath)
    except Exception:
        _logger.exception(b'Load json file: [%s] error.', filePath)

    return loaded


def saveDictToJsonFile(filePath, data):
    try:
        _logger.debug(b'Saving data to json file: [%s].', filePath)
        with open(filePath, b'wb') as jsonFile:
            json.dump(data, jsonFile)
    except Exception:
        _logger.exception(b'Save json file: [%s] error.', filePath)

    return


def deleteFile(filePath):
    try:
        if not os.path.isfile(filePath):
            _logger.debug(b'File: [%s] already deleted.', filePath)
            return True
        else:
            os.remove(filePath)
            return True

    except Exception:
        _logger.exception(b'Deleting file: [%s] error.', filePath)
        return False

    return
