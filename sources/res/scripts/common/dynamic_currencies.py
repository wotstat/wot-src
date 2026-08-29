from hashlib import md5
from typing import Dict

class DynamicCurrenciesData:

    def __init__(self):
        self.__currencies = {}
        self.__loaded = False
        return

    def getData(self):
        return self.__currencies

    def setData(self, data):
        self.__currencies = data
        self.__loaded = True
        return

    def replaceData(self, data):
        self.__currencies.update(data)
        return

    @property
    def loaded(self):
        return self.__loaded

    def isCurrencyCodeCorrect(self, currencyCode):
        return not self.__loaded or currencyCode in self.__currencies


def getCurrencyCD(currencyCode):
    cd_hex = md5(currencyCode).hexdigest()[:7]
    return int(cd_hex, 16)


g_dynamicCurrenciesData = DynamicCurrenciesData()
