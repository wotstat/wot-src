import typing
from epic_missions_config import getQuestConfig
from gui.impl import backport
from gui.impl.gen import R

def getQuestUiData(questName):
    config = getQuestConfig(questName)
    for itemData in config.itervalues():
        return (
         getQuestItemIcon(itemData), getQuestItemDescr(itemData), getQuestItemGoal(itemData))

    return


def getQuestItemDescr(itemData):
    itemDescription = itemData[b'description']
    descrDyn = R.strings.fl_quests.dyn(itemDescription)()
    configs = itemData.get(b'config', {})
    paramsObj = configs.get(b'params', {}).copy()
    paramsObj.update(configs)
    for key, value in paramsObj.iteritems():
        if isinstance(value, int):
            paramsObj[key] = backport.getNiceNumberFormat(value)

    if descrDyn <= 0:
        return b''
    if itemDescription.endswith(b'plural'):
        return backport.ntext(descrDyn, configs.get(b'goal', 0), **paramsObj)
    return backport.text(descrDyn, **paramsObj)


def getQuestItemGoal(itemData):
    configs = itemData.get(b'config', {})
    return configs.get(b'goal', configs.get(b'uniqueGoal', 1))


def getQuestItemIcon(itemData):
    return itemData[b'icon']
