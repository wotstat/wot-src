from frameworks.wulf import ViewModel

class HelpNavigateFrom(ViewModel):
    __slots__ = ()
    QUICKTRAINING = b'QuickTraining'
    PERSONALFILE = b'PersonalFile'
    PERSONALDATA = b'PersonalData'

    def __init__(self, properties=0, commands=0):
        super(HelpNavigateFrom, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(HelpNavigateFrom, self)._initialize()
        return
