from __future__ import absolute_import
from game_params_common.base_manager import GameParamsSchema
from dict2model import models, fields, schemas
from halloween_common.halloween_constants import HALLOWEEN_LOOT_PARAMS_KEY

class LootModel(models.Model):
    __slots__ = (b'lootId', b'bonus')

    def __init__(self, lootId, bonus):
        super(LootModel, self).__init__()
        self.lootId = lootId
        self.bonus = bonus
        return


class LootConfigModel(models.Model):
    __slots__ = (b'loot',)

    def __init__(self, loot):
        super(LootConfigModel, self).__init__()
        self.loot = loot
        return

    def getBonus(self, lootId):
        for lootItem in self.loot:
            if lootItem.lootId == lootId:
                return lootItem.bonus

        return {}

    def getBonusItemsAmount(self, lootId):
        return sum([1 if isinstance(bonus, int) else len(bonus) for bonus in self.getBonus(lootId).values()])


def _getBonusReaders(*args, **kwargs):
    import bonus_readers
    return bonus_readers.readBonusSection(bonus_readers.getSupportedBonuses(), *args, **kwargs)


lootSchema = schemas.Schema(fields={b'lootId': (fields.String(required=True)), 
   b'bonus': (fields.Field(required=True))}, modelClass=LootModel, checkUnknown=True)
lootConfigSchema = GameParamsSchema[LootConfigModel](gameParamsKey=HALLOWEEN_LOOT_PARAMS_KEY, fields={b'loot': (fields.List(fieldOrSchema=lootSchema, required=True))}, modelClass=LootConfigModel, checkUnknown=True, usedInReplay=True, readers={b'bonus': _getBonusReaders})
