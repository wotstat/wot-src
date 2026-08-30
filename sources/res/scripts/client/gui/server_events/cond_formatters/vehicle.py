from gui.server_events.cond_formatters.formatters import MissionsBattleConditionsFormatter, EmptyMissionsFormatter

class MissionsVehicleConditionsFormatter(MissionsBattleConditionsFormatter):

    def __init__(self):
        super(MissionsVehicleConditionsFormatter, self).__init__({b'customization': (_CustomizationFormatter())})
        return


class _CustomizationFormatter(EmptyMissionsFormatter):
    pass
