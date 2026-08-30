from frameworks.wulf import Map, ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_stats_efficiency_param_model import FunStatsEfficiencyParamModel

class FunStatsEfficiencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(FunStatsEfficiencyModel, self).__init__(properties=properties, commands=commands)
        return

    def getParameters(self):
        return self._getMap(0)

    def setParameters(self, value):
        self._setMap(0, value)
        return

    @staticmethod
    def getParametersType():
        return (unicode, FunStatsEfficiencyParamModel)

    def _initialize(self):
        super(FunStatsEfficiencyModel, self)._initialize()
        self._addMapProperty(b'parameters', Map(unicode, FunStatsEfficiencyParamModel))
        return
