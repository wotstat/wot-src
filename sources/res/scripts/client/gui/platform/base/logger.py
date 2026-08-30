from helpers.log import adapters
DEFAULT_NAME = b'PRC'

def getWithContext(loggerName=DEFAULT_NAME, instance=None, **context):
    return adapters.getWithContext(loggerName, instance, **context)
