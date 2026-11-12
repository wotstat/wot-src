CUSTOMIZATION_RESOURCE_CURRENCY_CODE = b'paintcoin'

def getCustomizationResourceExchangePrice(priceGroups, priceGroupTags):
    priceGroupTags = frozenset(priceGroupTags)
    tagMatches = [group for group in priceGroups if frozenset(group[b'tags']) and frozenset(group[b'tags']).issubset(priceGroupTags)]
    if len(tagMatches) == 1:
        return tagMatches[0][b'price']
    return 0
