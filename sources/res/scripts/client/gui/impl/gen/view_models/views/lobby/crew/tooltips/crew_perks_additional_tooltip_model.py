from frameworks.wulf import ViewModel

class CrewPerksAdditionalTooltipModel(ViewModel):
    __slots__ = (b'onError',)

    def __init__(self, properties=6, commands=1):
        super(CrewPerksAdditionalTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getSkillType(self):
        return self._getString(2)

    def setSkillType(self, value):
        self._setString(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getInfo(self):
        return self._getString(4)

    def setInfo(self, value):
        self._setString(4, value)
        return

    def getAnimationName(self):
        return self._getString(5)

    def setAnimationName(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(CrewPerksAdditionalTooltipModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'skillType', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'info', b'')
        self._addStringProperty(b'animationName', b'')
        self.onError = self._addCommand(b'onError')
        return
