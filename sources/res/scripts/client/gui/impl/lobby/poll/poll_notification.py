from debug_utils import LOG_WARNING, LOG_ERROR
from gui import SystemMessages
from gui.SystemMessages import SM_TYPE
from gui.impl.gen.view_models.views.lobby.poll.poll_view_model import PollViewType
from gui.shared.notifications import NotificationPriorityLevel

class PollNotification(object):

    @classmethod
    def invoke(cls, **kwargs):
        value = kwargs.get(b'value', None)
        if isinstance(value, dict):
            header = value.get(b'header', b'')
            text = value.get(b'text', b'')
            priority = value.get(b'priority', b'')
            target = value.get(b'target', b'')
            url = value.get(b'url', b'')
            notID = kwargs.get(b'notID', b'')
        else:
            LOG_ERROR((b'{}: "value" should be dict').format(cls.__name__))
            return
        if not all([bool(x) for x in [header, text, priority, target, url, notID]]):
            LOG_ERROR((b'{}: some items are not correct').format(cls.__name__))
            return
        else:
            if priority not in NotificationPriorityLevel.RANGE:
                LOG_WARNING((b'Notification priority is not allowed, priority={}').format(priority))
            notType = None
            if target == PollViewType.SURVEY.value:
                notType = SM_TYPE.SurveyNotification
            elif target == PollViewType.APPLICATION_FORM.value:
                notType = SM_TYPE.ApplicationFormNotification
            else:
                LOG_WARNING((b'Notification target is not allowed, target={}').format(target))
            if notType:
                SystemMessages.pushMessage(b'', priority=priority, type=notType, messageData={b'text': text, 
                   b'header': header, 
                   b'target': target}, savedData={b'value': {b'url': url, 
                              b'target': target}, 
                   b'notID': notID})
            return
