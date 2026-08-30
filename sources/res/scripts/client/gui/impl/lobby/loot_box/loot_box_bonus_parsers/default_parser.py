from gui.impl.lobby.loot_box.loot_box_helper import BonusInfo, OneOfBonusInfo
from gui.server_events.bonuses import getNonQuestBonuses

def parseAllOfBonusInfoSection(data):
    slots = dict()
    if data:
        for idx, slotsData in enumerate(data):
            slotBonusInfo = BonusInfo(*slotsData)
            probability, bonuses, limitIDsMap = __parseSlotBonusInfoSection(slotBonusInfo)
            slots.setdefault(idx, {}).setdefault(b'probability', probability)
            slots.setdefault(idx, {}).setdefault(b'bonuses', bonuses)
            slots.setdefault(idx, {}).setdefault(b'limitIDsMap', limitIDsMap)

    return slots


def parseLimitBoxInfoSection(data):
    return data.get(b'limits', {}).get(b'guaranteedBonusLimit', {}).get(b'guaranteedFrequency', 30)


def __parseSlotBonusInfoSection(slotBonusInfo):
    if slotBonusInfo is not None:
        sectionLimitIDsMap, sectionBonuses = {}, []
        for key, data in slotBonusInfo.subBonusRawData.iteritems():
            if key == b'groups':
                groupsSectionLimitIDsmap, groupsSectionBonuses = parseGroupsBonusInfoSection(data, slotBonusInfo)
                sectionLimitIDsMap = groupsSectionLimitIDsmap
                sectionBonuses.extend(groupsSectionBonuses)
            else:
                sectionBonuses.extend(getNonQuestBonuses(key, data))

        return (slotBonusInfo.probabilitiesList, sectionBonuses, sectionLimitIDsMap)
    else:
        return (
         0, [], {})


def parseGroupsBonusInfoSection(groups, slotBonusInfo):
    limitIDsMap = dict()
    bonuses = []
    for groupData in groups:
        oneOfBonusInfo = OneOfBonusInfo(*groupData.get(b'oneof', ([], {})))
        sectionLimitIDsMap, sectionBonuses = parseOneOfBonusInfoSection(oneOfBonusInfo)
        updateLimitIDsMap(limitIDsMap, slotBonusInfo, sectionLimitIDsMap, sectionBonuses)
        bonuses.extend(sectionBonuses)

    return (limitIDsMap, bonuses)


def parseOneOfBonusInfoSection(oneOfBonusInfo):
    limitIDsMap = dict()
    bonuses = []
    if oneOfBonusInfo is None:
        return (limitIDsMap, bonuses)
    else:
        for item in oneOfBonusInfo.subBonusRawData:
            bonusInfo = BonusInfo(*item)
            if bonusInfo and bonusInfo.subBonusRawData:
                for k, v in bonusInfo.subBonusRawData.iteritems():
                    if k == b'groups':
                        sectionLimitIDsMap, sectionBonuses = parseGroupsBonusInfoSection(v, bonusInfo)
                        updateLimitIDsMap(limitIDsMap, bonusInfo, sectionLimitIDsMap, sectionBonuses)
                        bonuses.extend(sectionBonuses)
                    else:
                        sectionBonuses = getNonQuestBonuses(k, v)
                        updateLimitIDsMap(limitIDsMap, bonusInfo, {}, sectionBonuses)
                        bonuses.extend(sectionBonuses)

        return (
         limitIDsMap, bonuses)


def updateLimitIDsMap(resultLimitIDsMap, parentNodeBonusInfo, childLimitIDsMap, childBonuses):
    for childLimitID, childLimitBonuses in childLimitIDsMap.iteritems():
        resultLimitIDsMap.setdefault(childLimitID, []).extend(childLimitBonuses)

    if parentNodeBonusInfo.limitIDs:
        for limitID in parentNodeBonusInfo.limitIDs:
            if limitID not in childLimitIDsMap:
                resultLimitIDsMap.setdefault(limitID, []).extend(childBonuses)

    return
