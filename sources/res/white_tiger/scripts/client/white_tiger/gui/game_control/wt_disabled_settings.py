import resource_helper
_CONFIG_PATH = b'gui/event_blocked_settings.xml'

class WhiteTigerDisabledSettings(object):

    def __init__(self):
        self.__disabledSettings = []
        self.__readSettingsTemplate()
        return

    @property
    def disabledSetting(self):
        for item in self.__disabledSettings:
            yield item

        return

    def __readSettingsTemplate(self):
        ctx, section = resource_helper.getRoot(_CONFIG_PATH)
        self.__disabledSettings = []
        for ctx, subSection in resource_helper.getIterator(ctx, section):
            item = resource_helper.readItem(ctx, subSection).value
            if b'controlPath' in item:
                path = item[b'controlPath'].split(b'/')
                self.__disabledSettings.append(path)

        resource_helper.purgeResource(_CONFIG_PATH)
        return
