from constants import ARENA_BONUS_TYPE

class ArenaBonusTypeLabel(object):
    LABELS = {(ARENA_BONUS_TYPE.UNKNOWN): b'special', 
       (ARENA_BONUS_TYPE.REGULAR): b'random', 
       (ARENA_BONUS_TYPE.TRAINING): b'training', 
       (ARENA_BONUS_TYPE.BOOTCAMP): b'bootcamp', 
       (ARENA_BONUS_TYPE.RANKED): b'ranked', 
       (ARENA_BONUS_TYPE.EPIC_RANDOM): b'epicRandom', 
       (ARENA_BONUS_TYPE.EPIC_BATTLE): b'epicQueue', 
       (ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD): b'battleRoyaleQueue', 
       (ARENA_BONUS_TYPE.BATTLE_ROYALE_SOLO): b'battleRoyaleQueue', 
       (ARENA_BONUS_TYPE.MAPBOX): b'mapbox', 
       (ARENA_BONUS_TYPE.MAPS_TRAINING): b'mapsTraining', 
       (ARENA_BONUS_TYPE.COMP7): b'comp7', 
       (ARENA_BONUS_TYPE.VERSUS_AI): b'versusAI'}
