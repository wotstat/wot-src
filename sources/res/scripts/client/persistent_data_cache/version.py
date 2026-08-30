import typing, constants
from helpers import version
from persistent_data_cache_common.common import getLogger
_logger = getLogger(b'Version')

def getClientPDCVersion():
    clientVersion = version.getClientVersion()
    locVersion = version.getLocalizationVersion()
    result = (
     clientVersion.version,
     clientVersion.meta.overrides,
     clientVersion.meta.client,
     clientVersion.meta.realm,
     locVersion.version,
     locVersion.revision,
     locVersion.language)
    if not constants.IS_DEVELOPMENT and b'' in result:
        _logger.error(b'Invalid client version: %s', result)
        return None
    else:
        return result
