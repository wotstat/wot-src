from frameworks.wulf import ViewModel

class LootRendererTypes(ViewModel):
    __slots__ = ()
    DEF = b'LootDefRenderer'
    VIDEO = b'LootVideoRenderer'
    VEHICLE = b'LootVehicleRenderer'
    VEHICLE_VIDEO = b'LootVehicleVideoRenderer'
    ANIMATED = b'LootAnimatedRenderer'
    CONVERSION = b'LootConversionRenderer'
    COMPENSATION = b'LootCompensationRenderer'
    CREWSKINS_COMPENSATION = b'CrewSkinsCompensationRenderer'
    VEHICLE_COMPENSATION = b'VehicleCompensationRenderer'
    VEHICLE_COMPENSATION_WITHOUT_ANIMATION = b'VehicleCompensationWithoutAnimationRenderer'
    BLUEPRINT_FINAL_FRAGMENT = b'BlueprintFinalFragmentRenderer'
    CREW_BOOK = b'CrewBookRenderer'

    def __init__(self, properties=0, commands=0):
        super(LootRendererTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(LootRendererTypes, self)._initialize()
        return
