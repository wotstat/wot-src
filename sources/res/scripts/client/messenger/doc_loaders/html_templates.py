import types
from debug_utils import LOG_WARNING
from gui.shared.notifications import NotificationPriorityLevel, NotificationGroup
from helpers.html import translation as html_translation, templates

class _MessageTemplate(templates.Template):

    def __init__(self, source, data, priority, groupID):
        super(_MessageTemplate, self).__init__({b'message': source})
        self.data = data
        self.priority = priority
        self.groupID = groupID
        return

    @property
    def lifeTime(self):
        return self.data.get(b'lifeTime', 0)

    def format(self, ctx=None, data=None):
        vo = self.data.copy()
        if isinstance(data, types.DictionaryType):
            for key, value in data.iteritems():
                if key in vo:
                    vo[key] = value

            if b'buttonsStates' in data:
                vo[b'buttonsStates'] = data[b'buttonsStates']
            else:
                vo[b'buttonsStates'] = {}
            if b'bgIconHeight' in data:
                vo[b'bgIconHeight'] = data[b'bgIconHeight']
            if b'linkageData' in data:
                vo[b'linkageData'] = data[b'linkageData']
        vo[b'message'] = super(_MessageTemplate, self).format(ctx=ctx, sourceKey=b'message')
        return vo


class MessageTemplates(templates.XMLCollection):

    def format(self, key, ctx=None, **kwargs):
        bgIconSource = kwargs.pop(b'bgIconSource', None)
        formatted = super(MessageTemplates, self).format(key, ctx, **kwargs)
        if b'bgIcon' in formatted:
            source = formatted[b'bgIcon']
        else:
            source = {}
        if bgIconSource in source:
            formatted[b'bgIcon'] = source[bgIconSource]
        else:
            formatted[b'bgIcon'] = source.get(None, b'')
        return formatted

    def priority(self, key):
        return self[key].priority

    def groupID(self, key):
        return self[key].groupID

    def lifeTime(self, key):
        return self[key].lifeTime

    def __missing__(self, key):
        self[key] = value = _MessageTemplate(key, {}, NotificationPriorityLevel.MEDIUM, NotificationGroup.INFO)
        return value

    def _make(self, source):
        sourceID = source.name
        data = {b'type': (source.readString(b'type')), 
           b'linkage': (source.readString(b'linkage')), 
           b'gfViewName': (source.readString(b'gfViewName')), 
           b'timestamp': (-1), 
           b'savedData': None, 
           b'bgIcon': (self._makeBgIconsData(source[b'bgIcon'])), 
           b'bgIconSizeAuto': (source.readBool(b'bgIconSizeAuto')), 
           b'icon': (source.readString(b'icon')), 
           b'defaultIcon': (source.readString(b'defaultIcon')), 
           b'filters': [], b'buttonsLayout': [], b'buttonsAlign': (source.readString(b'buttonsAlign', b'left')), 
           b'lifeTime': (source.readInt(b'lifeTime'))}
        if data.get(b'gfViewName'):
            data[b'gfViewHeight'] = int(source.readString(b'gfViewHeight'))
            data[b'gfViewWidth'] = int(source.readString(b'gfViewWidth'))
            data[b'gfViewPopUpWidth'] = int(source.readString(b'gfViewPopUpWidth'))
            data[b'gfViewPopUpHeight'] = int(source.readString(b'gfViewPopUpHeight'))
        priority = source.readString(b'priority', NotificationPriorityLevel.MEDIUM)
        if priority not in NotificationPriorityLevel.RANGE:
            LOG_WARNING(b'Priority is invalid', sourceID, priority)
            priority = NotificationPriorityLevel.MEDIUM
        groupID = source.readString(b'groupID', NotificationGroup.INFO)
        if groupID not in NotificationGroup.ALL:
            LOG_WARNING(b'GroupID is invalid', sourceID, groupID)
            groupID = NotificationGroup.INFO
        message = html_translation(source.readString(b'message'))
        section = source[b'filters']
        if section is None:
            section = {}
        for _, subSec in section.items():
            data[b'filters'].append({b'name': (subSec.readString(b'name')), 
               b'color': (subSec.readString(b'color'))})

        section = source[b'buttonsLayout']
        if section is not None:
            layout = data[b'buttonsLayout']
            buttonTypes = set([])
            for _, subSec in section.items():
                button = self._makeButtonData(sourceID, subSec)
                if button is None:
                    continue
                buttonType = button[b'type']
                if buttonType in buttonTypes:
                    LOG_WARNING(b'Duplicated type of button', sourceID, buttonType)
                    continue
                buttonTypes.add(buttonType)
                layout.append(button)

        return _MessageTemplate(message, data, priority, groupID)

    def _makeButtonData(self, sourceID, section):
        action = section.readString(b'action')
        if not action:
            LOG_WARNING(b'button/action is not defined', sourceID)
            return None
        else:
            label = html_translation(section.readString(b'label'))
            if not label:
                LOG_WARNING(b'button/label is not defined', sourceID)
                return None
            buttonType = section.readString(b'type')
            if not buttonType and buttonType not in (b'submit', b'cancel'):
                LOG_WARNING(b'button/type is not defined or invalid', sourceID, buttonType)
                return None
            result = {b'label': label, 
               b'type': buttonType, 
               b'action': action}
            assertMsg = b'You cannot use "width" and "dynamicSizeByText" at the same time for button in msgs {}'
            dynamicSizeByText = section.readBool(b'dynamicSizeByText')
            width = section.readInt(b'width')
            if dynamicSizeByText:
                result[b'dynamicSizeByText'] = dynamicSizeByText
            elif width > 0:
                result[b'width'] = width
            return result

    def _makeBgIconsData(self, section):
        result = {}
        if section is not None:
            result[None] = section.readString(b'')
            if section.items():
                for secName, subSec in section.items():
                    result[secName] = subSec.readString(b'')

        return result


def loadForMessage(_, section, settings):
    settings.msgTemplates.load(section=section)
    return


def loadForOthers(_, section, settings):
    settings.htmlTemplates.load(section=section)
    return
