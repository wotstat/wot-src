from gui.impl.gen.view_models.views.lobby.dog_tags.dt_dog_tag import DtDogTag

class DogTagMarkerViewModel(DtDogTag):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DogTagMarkerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getAnimation(self):
        return self._getString(4)

    def setAnimation(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(DogTagMarkerViewModel, self)._initialize()
        self._addStringProperty(b'animation', b'')
        return
