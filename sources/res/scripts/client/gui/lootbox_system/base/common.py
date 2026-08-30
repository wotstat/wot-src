import logging
from enum import Enum
from typing import TYPE_CHECKING
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import ILootBoxSystemController
if TYPE_CHECKING:
    from typing import Callable, Dict, Optional, Tuple
_logger = logging.getLogger(__name__)
LOOTBOX_RANDOM_NATIONAL_BLUEPRINT = b'randomNationalBlueprint'
LOOTBOX_RANDOM_NATIONAL_BROCHURE = b'randomNationalBrochure'
LOOTBOX_RANDOM_NATIONAL_GUIDE = b'randomNationalGuide'
LOOTBOX_RANDOM_NATIONAL_CREW_BOOK = b'randomNationalCrewBook'
TEXT_RESOURCE_PREFIX = b'lootbox_'
COUNTRY_CODES_FOR_EXTERNAL_LOOT_LIST = (b'KR',)
DEFAULT_EVENT_NAME = b'lootbox_system'
LOOTBOX_COMPENSATION_TOKEN_PREFIX = b'lbs_compensation'
LOOTBOX_COMPENSATION_BONUS = b'lootboxCompensation'

class NotificationPathPart(str, Enum):
    MAIN = b'serviceChannelMessages'
    AUTOOPEN = b'lootBoxesAutoOpen'
    HEADER = b'header'
    TEXT = b'text'
    COUNT = b'count'


class BonusTypeForPreview(str, Enum):
    VEHICLE = b'vehicles'
    CUSTOMIZATION = b'customizations'


class BonusesLayoutAttrs(object):
    PRIORITY = b'priority'
    RARITY = b'rarity'
    VISIBILITY = b'isVisible'
    OVERRIDE = b'override'
    ID = b'id'
    MAIN = (PRIORITY, RARITY, VISIBILITY)


class ViewID(str, Enum):
    INTRO = b'intro'
    MAIN = b'main'
    INFO = b'info'
    AUTOOPEN = b'autoopen'
    SHOP = b'shop'


class _ViewsResolver(object):

    def __init__(self):
        self.__loaders = {}
        return

    def load(self, viewID, *args, **kwargs):
        loadView = self.__loaders.get(viewID)
        if callable(loadView):
            loadView(*args, **kwargs)
        else:
            _logger.warning(b'View "%s" does not exists', viewID.name)
        return

    def getLoader(self, viewID):
        return self.__loaders.get(viewID)

    def setLoader(self, viewID, func):
        self.__loaders[viewID] = func
        return

    def setLoaders(self, loaders):
        self.__loaders.update(loaders)
        return

    def clear(self):
        self.__loaders.clear()
        return


Views = _ViewsResolver()

@dependency.replace_none_kwargs(lootBoxes=ILootBoxSystemController)
def getTextResource(path, eventName, lootBoxes=None):

    def getResourceFromPath(resource):
        for part in path:
            resource = resource.dyn(part)

        return resource

    customResource = getResourceFromPath(R.strings.dyn(TEXT_RESOURCE_PREFIX + eventName))
    if customResource.isValid():
        return customResource
    return getResourceFromPath(R.strings.lootbox_system)
