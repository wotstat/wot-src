from collections import namedtuple
from gui.impl.gen.view_models.views.lobby.customization_resource.customization_resource_main_view_model import ExchangeCaptchaState
ConfirmationTab = namedtuple(b'ConfirmationTab', (b'tabId', b'selectedCount'))
ConfirmationSummary = namedtuple(b'ConfirmationSummary', (b'tabs', b'itemsCount', b'reward'))

def buildConfirmationSummary(dataProvider, selection):
    tabs = []
    itemsCount = 0
    reward = 0
    for tabId in dataProvider.getTabs():
        tabItems = dataProvider.getItems(tabId)
        selectedCount = selection.getSelectedCountForTab(tabItems)
        if selectedCount <= 0:
            continue
        tabs.append(ConfirmationTab(tabId, selectedCount))
        itemsCount += selectedCount
        reward += sum(selection.getSelectedCount(item) * item.exchangePrice for item in tabItems)

    return ConfirmationSummary(tuple(tabs), itemsCount, reward)


def getCaptchaState(value, expectedValue):
    if value is None:
        return ExchangeCaptchaState.EMPTY
    else:
        value = unicode(value).strip()
        if not value:
            return ExchangeCaptchaState.EMPTY
        try:
            isValid = int(value) == expectedValue
        except (TypeError, ValueError):
            isValid = False

        if isValid:
            return ExchangeCaptchaState.VALID
        return ExchangeCaptchaState.INVALID
