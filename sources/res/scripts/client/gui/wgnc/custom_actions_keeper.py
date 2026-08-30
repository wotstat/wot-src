class CustomActionsKeeper(object):
    __actions = {}

    @classmethod
    def registerAction(cls, actionId, actionHandler):
        cls.__actions[actionId] = actionHandler
        return

    @classmethod
    def getAction(cls, actionId):
        return cls.__actions.get(actionId, None)

    @classmethod
    def invoke(cls, actor, **kwargs):
        if actor is None:
            return
        else:
            if hasattr(actor, b'invoke'):
                actor.invoke(**kwargs)
            else:
                actor(**kwargs)
            return
