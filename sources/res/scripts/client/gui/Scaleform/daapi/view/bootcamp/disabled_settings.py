import resource_helper
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP

class BCDisabledSettings(object):

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
        LOG_DEBUG_DEV_BOOTCAMP(b'Reading BootCamp template settings')
        ctx, section = resource_helper.getRoot(b'gui/bootcamp_blocked_settings.xml')
        self.__disabledSettings = []
        for ctx, subSection in resource_helper.getIterator(ctx, section):
            item = resource_helper.readItem(ctx, subSection).value
            if b'controlPath' in item:
                path = item[b'controlPath'].split(b'/')
                self.__disabledSettings.append(path)

        return
