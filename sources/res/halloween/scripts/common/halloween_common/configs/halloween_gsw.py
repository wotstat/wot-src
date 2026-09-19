from __future__ import absolute_import
import typing
from game_params_common.base_manager import GameParamsSchema
from dict2model import models, fields, schemas
from halloween_common.halloween_constants import HALLOWEEN_GSW_PARAMS_KEY
if typing.TYPE_CHECKING:
    from typing import List, Optional

class CardModel(models.Model):
    __slots__ = (b'quests', b'visibleByToken')

    def __init__(self, visibleByToken, quests):
        super(CardModel, self).__init__()
        self.visibleByToken = visibleByToken
        self.quests = quests or []
        return


class CardsModel(models.Model):
    __slots__ = (b'card',)

    def __init__(self, card):
        super(CardsModel, self).__init__()
        self.card = card
        return


class GSWModel(models.Model):
    __slots__ = (b'cards',)

    def __init__(self, cards):
        super(GSWModel, self).__init__()
        self.cards = cards
        return


cardSchema = schemas.Schema(fields={b'visibleByToken': (fields.String(required=False, default=b'')), 
   b'quests': (fields.ListFromString(field=fields.String(), required=False))}, modelClass=CardModel, checkUnknown=True)
cardsSchema = schemas.Schema(fields={b'card': (fields.List(fieldOrSchema=cardSchema, required=True))}, modelClass=CardsModel, checkUnknown=True)
GSWSchema = GameParamsSchema[GSWModel](gameParamsKey=HALLOWEEN_GSW_PARAMS_KEY, fields={b'cards': (fields.Nested(schema=cardsSchema, required=True))}, modelClass=GSWModel, checkUnknown=True, usedInReplay=True)
