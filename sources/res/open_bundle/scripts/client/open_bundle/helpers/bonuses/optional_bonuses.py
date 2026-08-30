from __future__ import absolute_import
from future.utils import viewitems
from gui.server_events.bonuses import getNonQuestBonuses

def parseBonusData(data):
    groups = data.get(b'groups')
    if groups is None or not groups:
        return {}
    oneOfSection = groups[0].get(b'oneof')
    if oneOfSection is None:
        return {}
    result = {}
    if len(oneOfSection) == 2:
        _, items = oneOfSection
        for item in items:
            if item and len(item) == 4:
                probability, _, _, rawData = item
                if rawData:
                    name = (rawData.get(b'properties') or {}).get(b'name') or b''
                    if name:
                        cell = result.setdefault(name, {})
                        cell[b'probability'] = probability[0]
                        cell[b'bonuses'] = []
                        for k, v in viewitems(rawData):
                            cell[b'bonuses'].extend(getNonQuestBonuses(k, v))

    return result
