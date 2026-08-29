from gui.impl.gen import R
from gui.collection.collections_helpers import getCollectionRes
from gui.impl import backport
from gui.server_events.awards_formatters import AWARDS_SIZES
from web.web_client_api.common import ItemPackType, sanitizeResPath

class BonusAggregateWrapper(object):

    @classmethod
    def getWrappedBonus(cls, bonuses):
        return {}


class RandomCrewBooksWrapper(BonusAggregateWrapper):
    _R_IMAGE = R.images.gui.maps.icons.crewBooks.books

    @classmethod
    def getWrappedBonus(cls, bonuses):
        bonus = bonuses[0]
        return {b'id': (bonus.get(b'id', 0)), 
           b'type': (ItemPackType.CREW_BOOK_RANDOM), 
           b'value': (bonus.get(b'value', 0)), 
           b'icon': {(AWARDS_SIZES.SMALL): (sanitizeResPath(backport.image(cls._R_IMAGE.small.brochure_universal()))), (AWARDS_SIZES.BIG): (sanitizeResPath(backport.image(cls._R_IMAGE.big.brochure_universal())))}, 
           b'name': b'', 
           b'description': b''}


class RandomGuideWrapper(BonusAggregateWrapper):
    _R_IMAGE = R.images.gui.maps.icons.crewBooks.books

    @classmethod
    def getWrappedBonus(cls, bonuses):
        bonus = bonuses[0]
        return {b'id': (bonus.get(b'id', 0)), 
           b'type': (ItemPackType.CREW_BOOK_RANDOM), 
           b'value': (bonus.get(b'value', 0)), 
           b'icon': {(AWARDS_SIZES.SMALL): (sanitizeResPath(backport.image(cls._R_IMAGE.small.guide_universal()))), (AWARDS_SIZES.BIG): (sanitizeResPath(backport.image(cls._R_IMAGE.big.guide_universal())))}, 
           b'name': b'', 
           b'description': b''}


class RandomNationalBlueprintWrapper(BonusAggregateWrapper):
    _R_IMAGE = R.images.gui.maps.icons.blueprints.fragment

    @classmethod
    def getWrappedBonus(cls, bonuses):
        bonus = bonuses[0]
        return {b'id': 0, 
           b'type': (ItemPackType.BLUEPRINT_NATIONAL_ANY), 
           b'value': (bonus.get(b'value', 0)), 
           b'icon': {(AWARDS_SIZES.SMALL): (sanitizeResPath(backport.image(cls._R_IMAGE.small.randomNational()))), (AWARDS_SIZES.BIG): (sanitizeResPath(backport.image(cls._R_IMAGE.big.randomNational())))}, 
           b'name': b'', 
           b'description': b''}


class CollectionItemWrapper(BonusAggregateWrapper):

    @classmethod
    def getWrappedBonus(cls, bonuses):
        bonus = bonuses[0]
        collectionID = int(bonus[b'id'].split(b'_')[2])
        return {b'id': collectionID, 
           b'type': (ItemPackType.CUSTOM_ANY_COLLECTION_ITEM), 
           b'value': 1, 
           b'icon': {(AWARDS_SIZES.SMALL): (sanitizeResPath(backport.image(R.images.gui.maps.icons.collectionItems.c_48x48.dyn((b'any_{}').format(collectionID))()))), 
                     (AWARDS_SIZES.BIG): (sanitizeResPath(backport.image(R.images.gui.maps.icons.collectionItems.c_80x80.dyn((b'any_{}').format(collectionID))())))}, 
           b'name': (backport.text(getCollectionRes(collectionID).anyCollectionItem.tooltip.header())), 
           b'description': (backport.text(getCollectionRes(collectionID).anyCollectionItem.tooltip.body()))}
