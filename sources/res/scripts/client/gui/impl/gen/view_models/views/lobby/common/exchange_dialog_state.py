from frameworks.wulf import ViewModel

class ExchangeDialogState(ViewModel):
    __slots__ = ()
    DEFAULT = b'default'
    NOT_POSSIBLE = b'notPossible'
    NOT_REQUIRED = b'notRequired'

    def __init__(self, properties=0, commands=0):
        super(ExchangeDialogState, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ExchangeDialogState, self)._initialize()
        return
