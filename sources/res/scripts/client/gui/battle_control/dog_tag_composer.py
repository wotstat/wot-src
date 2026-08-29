from dog_tags_common.config.common import ComponentViewType
from dog_tags_common.number_formatter import formatComponentValue
from dog_tags_common.player_dog_tag import DisplayableDogTag
from gui.dog_tag_composer import DogTagComposerClient
from helpers import getLanguageCode
STARTING_GRADE_OFFSET = 1

class DogTagComposerInBattle(DogTagComposerClient):

    def getModel(self, dt):
        engraving = dt.getComponentByType(ComponentViewType.ENGRAVING)
        background = dt.getComponentByType(ComponentViewType.BACKGROUND)
        isMaxLevel = engraving.grade + STARTING_GRADE_OFFSET == len(engraving.componentDefinition.grades)
        return {b'background': {b'componentID': (background.compId), 
                           b'imageStr': (self.getComponentImage(background.compId, 0))}, 
           b'engraving': {b'componentID': (engraving.compId), 
                          b'imageStr': (self.getComponentImage(engraving.compId, engraving.grade)), 
                          b'name': (self.getComponentTitle(engraving.compId)), 
                          b'value': (formatComponentValue(getLanguageCode(), engraving.value, engraving.componentDefinition.numberType))}, 
           b'playerName': (dt.getNickName()), 
           b'clanTag': (dt.getClanTag()), 
           b'isEngravingMaxLevel': isMaxLevel}

    def getModelFromDict(self, dogTag):
        return self.getModel(DisplayableDogTag.fromDict(dogTag))


layoutComposer = DogTagComposerInBattle()
