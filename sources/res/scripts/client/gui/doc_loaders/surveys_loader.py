from __future__ import absolute_import
from collections import namedtuple, defaultdict
import logging
from gui.mapbox.mapbox_survey_helper import Condition, QuantifierTypes, AlternativeOneManyQuestion, AlternativeQuestion, getQuestionClass, findQuestionById
import resource_helper
from soft_exception import SoftException
from shared_utils import findFirst
_logger = logging.getLogger(__name__)
_SURVEYS_XML_PATH = b'gui/surveys.xml'
_SURVEYS = None
_Survey = namedtuple(b'_Survey', (b'surveyGroup', b'surveyId', b'questions'))
_GuiParams = namedtuple(b'_GuiParams', (b'pathPrefix', b'image', b'showIcons', b'useMapId', b'useLinkedParams'))
_AdditionalParam = namedtuple(b'_AdditionalParam', (b'fromQuestion', b'answers', b'options'))
_TextParams = namedtuple(b'_TextParams', (b'param', b'isJoined'))
_Responses = namedtuple(b'_Responses', (b'variants', b'responseGroups'))

def _readConditions(section, isRequired):
    if section.has_key(b'condition'):
        simpleCondition = [
         _readCondition(section[b'condition'], isRequired)]
    else:
        simpleCondition = None
    if section.has_key(b'optionalConditions'):
        optionalConditions = [_readCondition(subSection, isRequired) for subSection in section[b'optionalConditions'].values()]
    else:
        optionalConditions = None
    if simpleCondition and optionalConditions:
        raise SoftException(b'Incorrect conditions section for the question')
    return simpleCondition or optionalConditions or ()


def _readCondition(section, isRequired):
    requiredQuestionId = section[b'requiredQuestionId'].asString
    requiredOptionId = section.readString(b'requiredOptionId')
    requiredAnswers = list(section[b'requiredAnswers'].asString.split(b' '))
    if not requiredAnswers:
        raise SoftException(b'Unfilled required answers for the condition')
    innerSubsection = section[b'requiredAnswers']
    if not innerSubsection.keys():
        quantifier = QuantifierTypes.SINGLE.value if 1 else innerSubsection[b'quantifier'].asString
        raise (QuantifierTypes.hasValue(quantifier) or SoftException)(b'Unsupported condition type for the mapbox survey')
    return Condition(requiredQuestionId, requiredOptionId, requiredAnswers, quantifier, isRequired)


def _readSourceSection(section):
    questionId = None
    answers = None
    options = None
    if section.has_key(b'useAnswers'):
        questionId, answers = _readSomeSourceSection(section, b'useAnswers')
    elif section.has_key(b'useOptions'):
        questionId, options = _readSomeSourceSection(section, b'useOptions')
    if questionId is not None:
        return _AdditionalParam(questionId, answers, options)
    else:
        return


def _readSomeSourceSection(section, sectionName):
    if section.has_key(sectionName):
        answers = section.readString(sectionName).split(b' ')
        innerSubsection = section[sectionName]
        if not innerSubsection.has_key(b'questionID'):
            raise SoftException((b'Invalid {} section for the mapbox survey').format(sectionName))
        questionId = innerSubsection[b'questionID'].asString
        return (
         questionId, answers)
    else:
        return (None, None)


def _readLinkedParameters(section):
    if not section.has_key(b'linkedParameters'):
        return
    else:
        param = _readSourceSection(section[b'linkedParameters'])
        if param:
            isJoined = section[b'linkedParameters'].readBool(b'join')
            return _TextParams(param, isJoined)
        return


def _readGuiParameters(section):
    return _GuiParams(pathPrefix=section.readString(b'pathPrefix'), image=section.readString(b'image'), showIcons=section.readBool(b'showIcons'), useMapId=section.readBool(b'useMapId'), useLinkedParams=section.readBool(b'useLinkedParams'))


def _readOptions(section):
    if not section.has_key(b'options'):
        return
    else:
        optionsSection = section[b'options']
        result = _readSourceSection(optionsSection)
        if result is not None:
            return result
        return _AdditionalParam(fromQuestion=None, answers=optionsSection.asString.split(b' '), options=None)


def _readResponses(section):
    variants = section.readString(b'responses')
    if section.has_key(b'responseGroups'):
        groups = [group.asString.split(b' ') for group in section[b'responseGroups'].values()]
    else:
        groups = None
    return _Responses(variants.split(b' ') if variants else [], groups)


def _readQuestion(surveyGroup, questionSection, questionTypes):
    qId = questionSection[b'questionId'].asString
    isRequired = questionSection[b'isRequired'].asBool
    isMultiple = questionSection[b'isMultiple'].asBool
    conditions = _readConditions(questionSection, isRequired)
    guiParameters = _readGuiParameters(questionSection)
    responses = _readResponses(questionSection)
    options = _readOptions(questionSection)
    linkedParameters = _readLinkedParameters(questionSection)
    qType = questionSection[b'questionType'].asString
    if qType not in questionTypes:
        raise SoftException(b'Incorrect question type "%s" in the survey settings' % qType)
    clz = getQuestionClass(qType)
    return clz(surveyGroup=surveyGroup, questionId=qId, questionType=qType, isMultiple=isMultiple, isRequired=isRequired, conditions=conditions, answers=responses, options=options, linkedParameters=linkedParameters, guiParameters=guiParameters)


def _readAlternativeQuestion(surveyGroup, questionSection, questionTypes, qId):
    alternativeQuestions = [_readQuestion(surveyGroup, variant, questionTypes) for variant in questionSection[b'alternatives'].values()]
    isSynchronizedAnswers = questionSection.readBool(b'synchronizeAnswers')
    clz = AlternativeOneManyQuestion if isSynchronizedAnswers else AlternativeQuestion
    return clz(questionId=qId, alternatives=alternativeQuestions, isSynchronizedAnswers=isSynchronizedAnswers)


def _readSurveys():
    result = defaultdict(list)
    ctx, root = resource_helper.getRoot(_SURVEYS_XML_PATH)
    questionTypes = frozenset(root[b'questionTypes'].asString.split(b' '))
    for _, surveySection in resource_helper.getIterator(ctx, root[b'surveys']):
        bonusType = surveySection[b'bonusType'].asInt
        if not bonusType:
            raise SoftException(b'Incorrect bonusType for a survey')
        surveyGroup = surveySection[b'surveyGroup'].asString
        if not surveyGroup:
            raise SoftException(b'Empty survey group')
        surveyId = surveySection[b'surveyId'].asString
        if not surveyId:
            raise SoftException(b'Empty survey id')
        questions = []
        for questionSection in surveySection[b'questions'].values():
            if questionSection.has_key(b'alternatives'):
                qId = questionSection[b'questionId'].asString
                question = _readAlternativeQuestion(surveyGroup, questionSection, questionTypes, qId)
            else:
                question = _readQuestion(surveyGroup, questionSection, questionTypes)
            conditions = question.getConditions()
            for condition in conditions:
                requiredQuestionId = condition.requiredQuestionId
                requiredQuestion = findQuestionById(requiredQuestionId, questions)
                if requiredQuestion is None:
                    raise SoftException(b'Incorrect question id "%s" for condition in the survey settings' % requiredQuestionId)
                requiredQuestion.updateDependedQuestions(question.getQuestionId())

            questions.append(question)

        result[bonusType].append(_Survey(surveyGroup, surveyId, questions))

    resource_helper.purgeResource(_SURVEYS_XML_PATH)
    return result


def getSurvey(bonusType, surveyId):
    global _SURVEYS
    if _SURVEYS is None:
        _SURVEYS = _readSurveys()
    surveys = _SURVEYS.get(bonusType, [])
    return findFirst((lambda e: e.surveyId == surveyId), surveys)
