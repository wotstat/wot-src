import itertools, logging
from gui.impl import backport
from gui.impl.gen import R
from helpers.html import translation
import resource_helper
from gui.Scaleform.genConsts.MANUAL_TEMPLATES import MANUAL_TEMPLATES
from gui.shared.utils.functions import makeTooltip
_logger = logging.getLogger(__name__)
_CHAPTERS_DATA_PATH = b'gui/manual/'
_CHAPTERS_LIST_XML = b'chapters_list.xml'

class ManualPageTypes(object):
    HINTS_PAGE = b'hints_page'
    BOOTCAMP_PAGE = b'bootcamp_page'
    MAPS_TRAINING_PAGE = b'maps_training_page'
    VIDEO_PAGE = b'video_page'


_MANUAL_LESSON_TEMPLATES = {(ManualPageTypes.HINTS_PAGE): (MANUAL_TEMPLATES.HINTS), 
   (ManualPageTypes.BOOTCAMP_PAGE): (MANUAL_TEMPLATES.BOOTCAMP), 
   (ManualPageTypes.MAPS_TRAINING_PAGE): (MANUAL_TEMPLATES.MAPS_TRAINING), 
   (ManualPageTypes.VIDEO_PAGE): (MANUAL_TEMPLATES.VIDEO)}

def getChapters(filterFunction):
    chaptersListPath = _CHAPTERS_DATA_PATH + _CHAPTERS_LIST_XML
    with resource_helper.root_generator(chaptersListPath) as ctx, root:
        chapters = __readChapters(ctx, root, filterFunction)
    return chapters


def getPagesIndexesList(filterFunction):
    chaptersData = getChapters(filterFunction)
    return itertools.chain.from_iterable([chapter[b'pageIDs'] for chapter in chaptersData])


def getChaptersIndexesList(filterFunction):
    chaptersData = getChapters(filterFunction)
    return [chapter[b'uiData'][b'index'] for chapter in chaptersData]


def getChapterData(chapterFileName, filterFunction, bootcampRunCount, chapterTitle=b''):
    _logger.debug(b'ManualXMLDataReader: requested chapter data: %s', chapterFileName)
    chapterPath = _CHAPTERS_DATA_PATH + chapterFileName
    with resource_helper.root_generator(chapterPath) as ctx, root:
        chapter = __readChapter(ctx, root, filterFunction, bootcampRunCount, chapterTitle)
    return chapter


def __isNew(lessonCtx, lessonSection):
    return bool(__getCustomSectionValue(lessonCtx, lessonSection, b'new', safe=True))


def __readChapter(ctx, root, filterFunction, bootcampRunCount, chapterTitle=b''):
    pages = []
    details = []
    index = 0
    ctx, section = resource_helper.getSubSection(ctx, root, b'lessons')
    for lessonCtx, lessonSection in resource_helper.getIterator(ctx, section):
        template = __getCustomSectionValue(lessonCtx, lessonSection, b'template')
        if not filterFunction(template):
            continue
        title = translation(__getCustomSectionValue(lessonCtx, lessonSection, b'title'))
        background = __getCustomSectionValue(lessonCtx, lessonSection, b'background')
        description = __getCustomSectionValue(lessonCtx, lessonSection, b'description', safe=True)
        pageId = __getCustomSectionValue(lessonCtx, lessonSection, b'id')
        if description is None:
            description = b''
        else:
            description = translation(description)
        contentRendererLinkage = b''
        if template == ManualPageTypes.MAPS_TRAINING_PAGE:
            contentRendererData = {b'text': (backport.text(R.strings.maps_training.manualPage.button()))}
            contentRendererLinkage = _MANUAL_LESSON_TEMPLATES.get(template)
        elif template == ManualPageTypes.BOOTCAMP_PAGE:
            contentRendererData = __getBootcampRendererData(bootcampRunCount)
            contentRendererLinkage = _MANUAL_LESSON_TEMPLATES.get(template)
        elif template == ManualPageTypes.VIDEO_PAGE:
            contentRendererData = __getVideoRendererData(lessonCtx, lessonSection)
            contentRendererLinkage = _MANUAL_LESSON_TEMPLATES.get(template)
        else:
            contentRendererData, hintsCount = __getHintsRendererData(lessonCtx, lessonSection)
            if hintsCount > 0:
                contentRendererLinkage = _MANUAL_LESSON_TEMPLATES.get(template)
        pages.append({b'buttonsGroup': b'ManualChapterGroup', 
           b'pageIndex': (int(index)), 
           b'selected': False, 
           b'hasNewContent': (__isNew(lessonCtx, lessonSection)), 
           b'label': (str(int(index) + 1)), 
           b'tooltip': {b'tooltip': (makeTooltip(title))}})
        details.append({b'title': title, 
           b'chapterTitle': chapterTitle, 
           b'description': description, 
           b'background': background, 
           b'contentRendererLinkage': contentRendererLinkage, 
           b'contentRendererData': contentRendererData, 
           b'id': pageId, 
           b'pageType': template})
        index += 1

    chapterData = {b'pages': pages, 
       b'details': details}
    _logger.debug(b'ManualXMLDataReader:  Read chapter: %s', chapterData)
    return chapterData


def __readChapters(ctx, root, filterFunction):
    ctx, section = resource_helper.getSubSection(ctx, root, b'chapters')
    chapters = []
    index = 0
    for chapterCtx, chapterSection in resource_helper.getIterator(ctx, section):
        filePath = __getCustomSectionValue(chapterCtx, chapterSection, b'file-path')
        title = __getCustomSectionValue(chapterCtx, chapterSection, b'title')
        background = __getCustomSectionValue(chapterCtx, chapterSection, b'background')
        attributes = __getChapterAttributes(filePath, filterFunction)
        ids = attributes.get(b'ids', [])
        if len(ids) != len(set(ids)):
            _logger.warning(b'chapter %s has duplicate page ids', title)
        chapter = {b'filePath': filePath, 
           b'pageIDs': ids, 
           b'newPageIDs': (attributes.get(b'newIds', [])), 
           b'uiData': {b'index': (int(index)), 
                       b'label': (translation(title)), 
                       b'image': background, 
                       b'tooltip': (makeTooltip(translation(title), (b'\n').join(attributes.get(b'chaptersTitles', []))))}}
        if any(ids in chapter[b'pageIDs'] for chapter in chapters):
            _logger.warning(b'chapter %s has duplicate page ids from another chapters', title)
        _logger.debug(b'ManualXMLDataReader: Read chapters. Chapter: %s', chapter)
        chapters.append(chapter)
        index += 1

    return chapters


def __getChapterAttributes(chapterFileName, filterFunction):
    chaptersTitles = []
    ids = []
    newIds = []
    chapterPath = _CHAPTERS_DATA_PATH + chapterFileName
    with resource_helper.root_generator(chapterPath) as ctx, root:
        ctx, section = resource_helper.getSubSection(ctx, root, b'lessons')
        for lessonCtx, lessonSection in resource_helper.getIterator(ctx, section):
            template = __getCustomSectionValue(lessonCtx, lessonSection, b'template')
            if not filterFunction(template):
                continue
            lessonId = int(__getCustomSectionValue(lessonCtx, lessonSection, b'id'))
            ids.append(lessonId)
            if __getCustomSectionValue(lessonCtx, lessonSection, b'new', safe=True):
                newIds.append(lessonId)
            chaptersTitles.append(translation(__getCustomSectionValue(lessonCtx, lessonSection, b'title')))

    return {b'ids': ids, b'newIds': newIds, b'chaptersTitles': chaptersTitles}


def __getCustomSectionValue(ctx, section, name, safe=False):
    valueCtx, valueSection = resource_helper.getSubSection(ctx, section, name, safe)
    result = None
    if valueSection is not None:
        item = resource_helper.readItem(valueCtx, valueSection, name)
        result = item.value
    return result


def __getVideoRendererData(lessonCtx, lessonSection):
    video = __getCustomSectionValue(lessonCtx, lessonSection, b'video', safe=True)
    if video is None:
        video = b''
    preview = __getCustomSectionValue(lessonCtx, lessonSection, b'preview', safe=True)
    if preview is None:
        preview = b''
    return {b'previewImage': preview, b'videoUrl': video}


def __getBootcampRendererData(bootcampRunCount):
    if bootcampRunCount == 0:
        bootcampText = translation(b'#bootcamp:request/bootcamp/start')
    else:
        bootcampText = translation(b'#bootcamp:request/bootcamp/return')
    return {b'text': bootcampText}


def __getHintsRendererData(lessonCtx, lessonSection):
    hints = []
    contentRendererData = None
    hintsCtx, hintsSection = resource_helper.getSubSection(lessonCtx, lessonSection, b'hints', safe=True)
    if hintsSection is not None:
        for hintCtx, hintSection in resource_helper.getIterator(hintsCtx, hintsSection):
            hintText = translation(__getCustomSectionValue(hintCtx, hintSection, b'text'))
            hintIcon = __getCustomSectionValue(hintCtx, hintSection, b'icon')
            hints.append({b'text': hintText, 
               b'icon': hintIcon})

        contentRendererData = {b'hints': hints}
    return (contentRendererData, len(hints))
