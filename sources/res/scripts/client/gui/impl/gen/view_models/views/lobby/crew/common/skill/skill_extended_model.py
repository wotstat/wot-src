from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_model import SkillModel

class SkillExtendedModel(SkillModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(SkillExtendedModel, self).__init__(properties=properties, commands=commands)
        return

    def getUserName(self):
        return self._getString(7)

    def setUserName(self, value):
        self._setString(7, value)
        return

    def getDescription(self):
        return self._getString(8)

    def setDescription(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(SkillExtendedModel, self)._initialize()
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'description', b'')
        return
