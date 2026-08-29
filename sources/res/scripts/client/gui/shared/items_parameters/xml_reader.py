import resource_helper
SIMPLIFIED_COEFFICIENTS_PATH = b'gui/params_coefficients.xml'

def _getBonusTypesGenerator(bonusTypes):
    for bonusType, items in bonusTypes.items():
        for itemName in items:
            yield (itemName, bonusType)

    return


def read():
    params = {}
    for item in resource_helper.root_iterator(SIMPLIFIED_COEFFICIENTS_PATH):
        params[item.name] = item.value

    coefficients = params.pop(b'coefficients')
    bonuses = params.pop(b'bonuses')
    for paramName, bonusTypes in bonuses.iteritems():
        bonuses[paramName] = tuple(_getBonusTypesGenerator(bonusTypes))

    return (coefficients, bonuses)
