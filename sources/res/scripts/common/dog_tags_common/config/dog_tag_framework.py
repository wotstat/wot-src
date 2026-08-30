import inspect, sys
from functools import partial
import typing
from common import ParameterType, Visibility, ParseException, ComponentPurpose, ComponentViewType, ComponentNumberType
from validators import validateTriumphMedal, validateTriumph, validateSkill, validateDedication, validateDedicationUnlock, validateBase, validateRankedSkill, validateViewType, validateCommon, validateStartingComponent, validateStatic
if typing.TYPE_CHECKING:
    from typing import List

class XMLObjBuilder(object):

    def __init__(self, componentCls):
        self.__componentCls = componentCls
        self._component = componentCls()
        return

    def reset(self):
        self._component = self.__componentCls()
        return

    def validate(self):
        return

    def build(self):
        self.validate()
        componentObject = self._component
        self.reset()
        return componentObject


class ComponentBuilder(XMLObjBuilder):
    TAG = b'component'
    PARAMS = {b'componentId': (
                      ParameterType.INT, Visibility.ALL), 
       b'resourceRoot': (
                       ParameterType.STR, Visibility.ALL), 
       b'viewType': (
                   ParameterType.VIEW_TYPE, Visibility.ALL), 
       b'purpose': (
                  ParameterType.TYPE, Visibility.ALL), 
       b'unlockKey': (
                    ParameterType.STR_LIST, Visibility.ALL), 
       b'progressKey': (
                      ParameterType.STR_LIST, Visibility.ALL), 
       b'isHidden': (
                   ParameterType.BOOL, Visibility.ALL), 
       b'isSecret': (
                   ParameterType.BOOL, Visibility.ALL), 
       b'isDefault': (
                    ParameterType.BOOL, Visibility.ALL), 
       b'isExternalUnlockOnly': (
                               ParameterType.BOOL, Visibility.ALL), 
       b'grades': (
                 ParameterType.FLOAT_LIST, Visibility.ALL), 
       b'isDeprecated': (
                       ParameterType.BOOL, Visibility.ALL), 
       b'numberType': (
                     ParameterType.NUMBER_TYPE, Visibility.ALL), 
       b'src': (
              ParameterType.STR, Visibility.CLIENT), 
       b'minLevel': (
                   ParameterType.INT, Visibility.ALL), 
       b'battleTypes': (
                      ParameterType.INT_LIST, Visibility.ALL), 
       b'glossaryName': (
                       ParameterType.STR, Visibility.ALL), 
       b'lightingUpTo': (
                       ParameterType.FLOAT, Visibility.ALL), 
       b'skipProgressInDescr': (
                              ParameterType.BOOL, Visibility.CLIENT)}
    DEFAULTS = {b'isSecret': False, 
       b'isHidden': False, 
       b'isDefault': False, 
       b'isDeprecated': False, 
       b'isExternalUnlockOnly': False, 
       b'numberType': (ComponentNumberType.NUMBER), 
       b'glossaryName': b'', 
       b'skipProgressInDescr': False}
    VALIDATORS = {(ComponentPurpose.TRIUMPH_MEDAL): [
                                        validateCommon,
                                        partial(validateViewType, viewType=ComponentViewType.BACKGROUND, purpose=ComponentPurpose.TRIUMPH_MEDAL),
                                        validateTriumphMedal], 
       (ComponentPurpose.TRIUMPH): [
                                  validateCommon,
                                  partial(validateViewType, viewType=ComponentViewType.ENGRAVING, purpose=ComponentPurpose.TRIUMPH),
                                  validateTriumph], 
       (ComponentPurpose.SKILL): [
                                validateCommon,
                                partial(validateViewType, viewType=ComponentViewType.ENGRAVING, purpose=ComponentPurpose.SKILL),
                                validateSkill], 
       (ComponentPurpose.DEDICATION): [
                                     validateCommon,
                                     partial(validateViewType, viewType=ComponentViewType.ENGRAVING, purpose=ComponentPurpose.DEDICATION),
                                     validateDedication,
                                     validateDedicationUnlock], 
       (ComponentPurpose.RANKED_SKILL): [
                                       validateCommon,
                                       partial(validateViewType, viewType=ComponentViewType.ENGRAVING, purpose=ComponentPurpose.RANKED_SKILL),
                                       validateRankedSkill], 
       (ComponentPurpose.BASE): [
                               validateCommon,
                               partial(validateViewType, viewType=ComponentViewType.BACKGROUND, purpose=ComponentPurpose.BASE),
                               validateBase], 
       (ComponentPurpose.STATIC): [
                                 validateCommon,
                                 partial(validateViewType, viewType=ComponentViewType.ENGRAVING, purpose=ComponentPurpose.STATIC),
                                 validateStatic]}

    def __init__(self):
        super(ComponentBuilder, self).__init__(ComponentDefinition)
        return

    def componentId(self, value):
        self._component.componentId = value
        return

    def resourceRoot(self, value):
        self._component.resourceRoot = value
        return

    def viewType(self, value):
        self._component.viewType = value
        return

    def purpose(self, value):
        self._component.purpose = value
        return

    def unlockKey(self, value):
        self._component.unlockKey = value
        return

    def progressKey(self, value):
        self._component.progressKey = value
        return

    def isHidden(self, value):
        self._component.isHidden = value
        return

    def isSecret(self, value):
        self._component.isSecret = value
        return

    def isDefault(self, value):
        self._component.isDefault = value
        return

    def isExternalUnlockOnly(self, value):
        self._component.isExternalUnlockOnly = value
        return

    def grades(self, value):
        self._component.grades = value
        return

    def isDeprecated(self, value):
        self._component.isDeprecated = value
        return

    def numberType(self, value):
        self._component.numberType = value
        return

    def src(self, value):
        self._component.src = value
        return

    def minLevel(self, value):
        self._component.minLevel = value
        return

    def battleTypes(self, value):
        self._component.battleTypes = value
        return

    def glossaryName(self, value):
        self._component.glossaryName = value
        return

    def lightingUpTo(self, value):
        self._component.lightingUpTo = value
        return

    def skipProgressInDescr(self, value):
        self._component.skipProgressInDescr = value
        return

    def validate(self):
        for validator in self.VALIDATORS.get(self._component.purpose, []):
            validator(self._component)

        return


class StartingComponentsBuilder(XMLObjBuilder):
    TAG = b'startingComponents'
    PARAMS = {b'components': (
                     ParameterType.INT_LIST, Visibility.ALL)}
    VALIDATORS = [
     validateStartingComponent]

    def __init__(self, componentDefs=None):
        super(StartingComponentsBuilder, self).__init__(StartingComponents)
        self.__componentDefs = componentDefs
        self._compsID = []
        return

    def components(self, value):
        self._compsID = value
        return

    def validate(self):
        for validator in self.VALIDATORS:
            validator(self._component)

        return

    def build(self):
        if len(self._compsID) != len(set(self._compsID)):
            raise ParseException(ParseException.STARTING_COMPONENT_DUPLICITY)
        for c in self._compsID:
            for cd in self.__componentDefs:
                if cd.componentId == c:
                    self._component.components.append(cd)
                    break
            else:
                raise ParseException(ParseException.STARTING_COMPONENT_INVALID_ID, c)

        return super(StartingComponentsBuilder, self).build()


class ComponentDefinition(object):

    def __init__(self):
        self.componentId = 0
        self.resourceRoot = b''
        self.viewType = None
        self.purpose = None
        self.unlockKey = None
        self.progressKey = None
        self.isHidden = False
        self.isSecret = False
        self.isDefault = False
        self.isExternalUnlockOnly = False
        self.grades = None
        self.isDeprecated = False
        self.src = None
        self.numberType = ComponentNumberType.NUMBER
        self.minLevel = None
        self.battleTypes = None
        self.glossaryName = b''
        self.lightingUpTo = None
        self.skipProgressInDescr = False
        return

    def __str__(self):
        return (b"[id: {componentId}, {purpose}, {viewType}, unlock keys: {unlockKey}, progress keys: {progressKey}, hidden: {isHidden}, default: {isDefault}, deprecated: {isDeprecated}, grades: {grades}, secret: {isSecret}, only external unlock: {isExternalUnlockOnly}, src: '{src}', skipProgressInDescr: {skipProgressInDescr}]").format(componentId=self.componentId, purpose=b'None' if self.purpose is None else self.purpose.value, viewType=b'None' if self.viewType is None else self.viewType.value, unlockKey=self.unlockKey, progressKey=self.progressKey, isHidden=self.isHidden, isDefault=self.isDefault, isDeprecated=self.isDeprecated, grades=self.grades, isSecret=self.isSecret, isExternalUnlockOnly=self.isExternalUnlockOnly, src=self.src, skipProgressInDescr=self.skipProgressInDescr)

    def __repr__(self):
        return self.__str__()


class StartingComponents(object):

    def __init__(self):
        self.components = []
        return

    def __str__(self):
        return self.components.__str__()

    def __repr__(self):
        return self.__str__()


def buildParserInfo():
    res = {}
    clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    for name, cls in clsmembers:
        tag = getattr(cls, b'TAG', None)
        if tag:
            if tag in res:
                raise ParseException(ParseException.TAG_DUPLICITY, tag)
            paramNames = set(cls.PARAMS.iterkeys())
            paramsInfo = {}
            for paramName, paramType in cls.PARAMS.iteritems():
                if paramName in paramsInfo:
                    raise ParseException(ParseException.PARAM_DUPLICITY, paramName)
                paramsInfo[paramName] = paramType

            defaults = getattr(cls, b'DEFAULTS', {})
            res[tag] = (name, cls, paramNames, paramsInfo, defaults)

    return res


parserInfo = buildParserInfo()
