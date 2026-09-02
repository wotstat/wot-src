from gui.server_events.bonuses import getNonQuestBonuses

def parseAllOfSection(data):
    slots = {}
    if data:
        for idx, slotsData in enumerate(data):
            probability, bonuses, name = parseSlotSection(slotsData)
            slot = slots.setdefault(idx, {})
            slot.setdefault(b'probability', probability)
            slot.setdefault(b'name', name)
            slot.setdefault(b'bonuses', bonuses)

    return slots


def parseSlotSection(data):
    if isinstance(data, tuple) and len(data) == 4:
        probability, _, _, rawData = data
        name = (rawData.get(b'properties') or {}).get(b'name') or b''
        return (
         probability, parseGroupsSection(rawData), name)
    return (
     0, [], b'')


def parseGroupsSection(data):
    groups = data.get(b'groups', [])
    bonuses = []
    for groupData in groups:
        bonuses.extend(parseOneOfSection(groupData))

    return bonuses


def parseOneOfSection(data):
    oneOf = data.get(b'oneof', ())
    bonuses = []
    if oneOf and len(oneOf) == 2:
        _, items = oneOf
        for item in items:
            if item and len(item) == 4:
                _, _, _, rawData = item
                if rawData:
                    for k, v in rawData.iteritems():
                        if k == b'groups':
                            bonuses.extend(parseGroupsSection(rawData))
                        else:
                            bonuses.extend(getNonQuestBonuses(k, v))

    return bonuses
