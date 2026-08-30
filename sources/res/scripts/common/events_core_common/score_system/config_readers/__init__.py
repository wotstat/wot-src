from soft_exception import SoftException

def readRuleSection(ruleSection):
    ruleConfig = {}
    for paramSection in ruleSection.values():
        ruleConfig[paramSection.name] = paramSection.asInt

    return ruleConfig


def readScoreSystemSection(scoreSystemSection):
    if b'actions' not in scoreSystemSection.keys():
        raise SoftException(b'Score system section missing actions')
    actionsDict = {}
    for actionSection in scoreSystemSection[b'actions'].values():
        actionID = actionSection.name
        rulesDict = {}
        for ruleSection in actionSection.values():
            rulesDict[ruleSection.name] = readRuleSection(ruleSection)

        actionsDict[actionID] = rulesDict

    return actionsDict
