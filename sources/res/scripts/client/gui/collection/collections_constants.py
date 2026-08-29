from collections_common import COLLECTIONS_PREFIX
COLLECTION_ITEM_BONUS_NAME = b'collectionItem'
COLLECTION_ITEM_PREFIX_NAME = COLLECTIONS_PREFIX + b'_item'
COLLECTION_ITEM_TOKEN_PREFIX_NAME = b'cllc:item:'
COLLECTION_ITEM_RES_KEY_TEMPLATE = b'{}_{}_{}'
COLLECTION_RES_PREFIX = b'collection_'
COLLECTION_START_EVENT_TYPE = b'collectionStart'
COLLECTIONS_UPDATED_ENTRY_EVENT_TYPE = b'collectionsUpdatedEntry'
COLLECTIONS_RENEW_EVENT_TYPE = b'collectionsRenew'
COLLECTION_START_SEEN = b'collectionStartNotification'
COLLECTIONS_UPDATED_ENTRY_SEEN = b'collectionsUpdatedEntryNotification'
COLLECTION_RENEW_SEEN = b'collectionRenewNotification'

def cllcTokenToEntitlement(tokenID):
    try:
        _, _, collectionId, itemId = tokenID.split(b':')
        return COLLECTION_ITEM_PREFIX_NAME + (b'_{}_{}').format(collectionId, itemId)
    except ValueError:
        return

    return
