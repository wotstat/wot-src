from __future__ import absolute_import
import resource_helper
from future.utils import iteritems
_SIMPLIFIED_COEFFICIENTS_PATH = b'gui/params_coefficients.xml'

def _getBonusTypesGenerator(bonusTypes):
    for bonusType, items in iteritems(bonusTypes):
        for itemName in items:
            yield (itemName, bonusType)

    return


def read():
    params = {}
    for item in resource_helper.root_iterator(_SIMPLIFIED_COEFFICIENTS_PATH):
        params[item.name] = item.value

    coefficients = params.pop(b'coefficients')
    bonuses = params.pop(b'bonuses')
    for paramName, bonusTypes in iteritems(bonuses):
        bonuses[paramName] = tuple(_getBonusTypesGenerator(bonusTypes))

    return (coefficients, bonuses)
