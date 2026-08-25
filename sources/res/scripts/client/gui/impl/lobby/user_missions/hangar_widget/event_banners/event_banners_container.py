import typing, Event
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Dict, Type
    from base_event_banner import BaseEventBanner

class _Singleton(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance


class EventBannersContainer(object):
    __metaclass__ = _Singleton
    __slots__ = (b'__eventsMap', b'onBannerUpdate')

    def __init__(self):
        self.onBannerUpdate = Event.Event()
        self.__eventsMap = {}
        return

    @property
    def events(self):
        return self.__eventsMap

    def registerEventBanner(self, eventBannerCls):
        if self.__eventsMap.has_key(eventBannerCls.NAME):
            raise SoftException((b'Banner for key {0} is already registered').format(eventBannerCls.NAME))
        self.__eventsMap[eventBannerCls.NAME] = eventBannerCls()
        return

    def getEventBanner(self, key):
        return self.__eventsMap.get(key)

    def unregisterEventBanner(self, eventBannerCls):
        banner = self.__eventsMap.pop(eventBannerCls.NAME)
        if banner is not None:
            banner.onDisappear()
        return
