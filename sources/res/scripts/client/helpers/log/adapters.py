import logging

class LoggerAdapter(logging.LoggerAdapter):

    def debug(self, msg, *args, **kwargs):
        self.log(logging.DEBUG, msg, *args, **kwargs)
        return

    def info(self, msg, *args, **kwargs):
        self.log(logging.INFO, msg, *args, **kwargs)
        return

    def warning(self, msg, *args, **kwargs):
        self.log(logging.WARNING, msg, *args, **kwargs)
        return

    def error(self, msg, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs)
        return

    def critical(self, msg, *args, **kwargs):
        self.log(logging.CRITICAL, msg, *args, **kwargs)
        return

    def log(self, level, msg, *args, **kwargs):
        if self.isEnabledFor(level):
            super(LoggerAdapter, self).log(level, msg, *args, **kwargs)
        return


class InstanceContextLoggerAdapter(LoggerAdapter):

    def __init__(self, logger, instance=None, **context):
        if instance is not None:
            context[b'cls'] = instance.__class__.__name__
            context[b'iid'] = id(instance)
        super(InstanceContextLoggerAdapter, self).__init__(logger, context)
        return

    def process(self, msg, kwargs):
        if self.extra:
            msg = (b'{} {}').format(self.extra, msg)
        return (
         msg, kwargs)


def getWithContext(loggerName, instance=None, **context):
    return InstanceContextLoggerAdapter(logging.getLogger(loggerName), instance=instance, **context)
