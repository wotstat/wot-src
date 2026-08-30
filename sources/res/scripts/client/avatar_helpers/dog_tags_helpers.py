import random, BigWorld
from dog_tags_common.components_config import componentConfigAdapter
from dog_tags_common.components_packer import unpack_component
from dog_tags_common.config.common import ComponentViewType
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from soft_exception import SoftException

class DogTagsHelpers(object):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    @classmethod
    def showRandomVictimDogTag(cls):
        dogTag = cls._getRandomDogTagForVehicle(cls._selectRandomEnemyVehicleInfo())
        cls._getDogTagController().setVictimsDogTags([dogTag])
        return

    @classmethod
    def showRandomKillerDogTag(cls):
        dogTag = cls._getRandomDogTagForVehicle(cls._selectRandomEnemyVehicleInfo())
        cls.guiSessionProvider.switchToPostmortem(True, False)
        cls._getDogTagController().onKillerDogTagCheat(cls._getDeadReasonInfo())
        cls._getDogTagController().setKillerDogTag(dogTag)
        return

    @classmethod
    def _randomDogTag(cls):
        usedDogTagsComponents = BigWorld.player().arena.arenaInfo.dogTagsInfo.usedDogTagsComponents
        possibleDTs = []
        for componentPacked in usedDogTagsComponents:
            compId, grade, teamId = unpack_component(componentPacked)
            if teamId == BigWorld.player().team:
                continue
            possibleDTs.append((compId, grade))

        if not possibleDTs:
            raise SoftException(b'Could not generate random Dog Tag. No enemies in battle.')
        random.shuffle(possibleDTs)
        result = []
        allComponents = componentConfigAdapter.getAllComponents()
        for viewType in ComponentViewType.__members__.values():
            compID, grade = next(k for k in possibleDTs if allComponents[k[0]].viewType == viewType)
            progress = 0
            result.append({b'id': compID, b'progress': progress, b'grade': grade})

        return result

    @classmethod
    def _getDeadReasonInfo(cls):
        return [
         b'Cheat', True, b'X', b'', b'', b'Cheat',
         {b'userName': b'Cheat', 
            b'clanAbbrev': b'', 
            b'tags': (set([])), 
            b'region': None, b'fakeName': b'', b'igrType': 0}]

    @classmethod
    def _selectRandomEnemyVehicleInfo(cls):
        arenaDP = cls.guiSessionProvider.getArenaDP()
        infoIterator = arenaDP.getVehiclesInfoIterator()
        enemyVehicles = [vInfo for vInfo in infoIterator if arenaDP.isEnemyTeam(vInfo.team)]
        if not enemyVehicles:
            raise SoftException(b'Could not generate random Dog Tag. No enemies in battle.')
        return random.choice(enemyVehicles)

    @classmethod
    def _getRandomDogTagForVehicle(cls, vInfo):
        dogTag = {b'vehicleId': (vInfo.vehicleID), 
           b'dogTag': {b'components': (cls._randomDogTag())}}
        return dogTag

    @classmethod
    def _getDogTagController(cls):
        dogTagsCtrl = cls.guiSessionProvider.dynamic.dogTags
        if not dogTagsCtrl:
            raise SoftException(b'DogTagsController has not been found.')
        return dogTagsCtrl
