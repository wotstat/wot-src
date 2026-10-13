from __future__ import absolute_import
from game_params_common.base_manager import GameParamsSchema
from dict2model import models, fields, schemas
from halloween_common.halloween_constants import HALLOWEEN_BESTIARY_PARAMS_KEY

class SoundsModel(models.Model):
    __slots__ = (b'select',)

    def __init__(self, select):
        super(SoundsModel, self).__init__()
        self.select = select
        return


class ShopModel(models.Model):
    __slots__ = (b'vehicle', b'bundles')

    def __init__(self, vehicle, bundles):
        super(ShopModel, self).__init__()
        self.vehicle = vehicle
        self.bundles = bundles or []
        if self.bundles and not self.vehicle:
            raise ValueError(b'The vehicle must not be empty.')
        return


class EnemyModel(models.Model):
    __slots__ = (b'name', b'unlockedByToken', b'style', b'ability', b'shop', b'needShowInHangar', b'sounds')

    def __init__(self, name, unlockedByToken, style, ability, shop, needShowInHangar, sounds):
        super(EnemyModel, self).__init__()
        self.name = name
        self.unlockedByToken = unlockedByToken
        self.style = style
        self.ability = ability
        self.shop = shop
        self.needShowInHangar = needShowInHangar
        self.sounds = sounds
        return


class EnemiesModel(models.Model):
    __slots__ = (b'enemy',)

    def __init__(self, enemy):
        super(EnemiesModel, self).__init__()
        self.enemy = enemy
        return


class BestiaryModel(models.Model):
    __slots__ = (b'enemies',)

    def __init__(self, enemies):
        super(BestiaryModel, self).__init__()
        self.enemies = enemies
        return


shopSchema = schemas.Schema(fields={b'vehicle': (fields.String(required=False)), 
   b'bundles': (fields.ListFromString(field=fields.String(), required=False))}, modelClass=ShopModel, checkUnknown=True)
soundsSchema = schemas.Schema(fields={b'select': (fields.String(required=False))}, modelClass=SoundsModel, checkUnknown=True)
enemySchema = schemas.Schema(fields={b'name': (fields.String(required=True)), 
   b'unlockedByToken': (fields.String(required=True)), 
   b'style': (fields.Integer(required=False)), 
   b'ability': (fields.String(required=False)), 
   b'shop': (fields.Nested(schema=shopSchema, required=False)), 
   b'needShowInHangar': (fields.Boolean(required=True)), 
   b'sounds': (fields.Nested(schema=soundsSchema))}, modelClass=EnemyModel, checkUnknown=True)
enemiesSchema = schemas.Schema(fields={b'enemy': (fields.List(fieldOrSchema=enemySchema, required=True))}, modelClass=EnemiesModel, checkUnknown=True)
bestiarySchema = GameParamsSchema[BestiaryModel](gameParamsKey=HALLOWEEN_BESTIARY_PARAMS_KEY, fields={b'enemies': (fields.Nested(schema=enemiesSchema, required=True))}, modelClass=BestiaryModel, checkUnknown=True, usedInReplay=True)
