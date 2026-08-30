from enum import Enum

class CameraMover(object):

    def moveCamera(self, cameraManager, cameraName):
        cameraManager.switchByCameraName(cameraName)
        return

    def moveCameraFailed(self):
        return


class SmoothCameraMover(CameraMover):

    def moveCamera(self, cameraManager, cameraName):
        cameraManager.switchByCameraName(cameraName, False)
        return


class SubhangarStateGroupConfig(object):

    def __init__(self, stateGroups=(), cameraMover=CameraMover(), environmentName=None):
        self.stateGroups = stateGroups
        self.cameraMover = cameraMover
        self.environmentName = environmentName
        return


class SubhangarStateGroupConfigProvider(object):

    def getSubhangarStateGroupConfig(self):
        raise NotImplementedError
        return


class SubhangarStateGroups(Enum):
    Customization = b'CustomizationStates'
    PersonalMissions = b'PersonalMissionsStates'
    VehicleHub = b'VehicleHubStates'
    PetDenStorage = b'PetDenStorage'
    VehicleHubOverviewLargeTank = b'VehicleHubOverviewLargeTankStates'
    VehicleHubModulesLargeTank = b'VehicleHubModulesLargeTankStates'
    VehicleHubUpgradesLargeTank = b'VehicleHubUpgradesLargeTankStates'
    VehicleHubArmorLargeTank = b'VehicleHubArmorLargeTankStates'
    VehicleHubStatsLargeTank = b'VehicleHubStatsLargeTankStates'
    VehicleHubOverviewMediumTank = b'VehicleHubOverviewMediumTankStates'
    VehicleHubModulesMediumTank = b'VehicleHubModulesMediumTankStates'
    VehicleHubUpgradesMediumTank = b'VehicleHubUpgradesMediumTankStates'
    VehicleHubStatsMediumTank = b'VehicleHubStatsMediumTankStates'
    VehicleHubArmorMediumTank = b'VehicleHubArmorMediumTankStates'
    VehicleHubOverviewSmallTank = b'VehicleHubOverviewSmallTankStates'
    VehicleHubModulesSmallTank = b'VehicleHubModulesSmallTankStates'
    VehicleHubUpgradesSmallTank = b'VehicleHubUpgradesSmallTankStates'
    VehicleHubStatsSmallTank = b'VehicleHubStatsSmallTankStates'
    VehicleHubArmorSmallTank = b'VehicleHubArmorSmallTankStates'
    PostBattleSmall = b'PostBattleSmallStates'
    PostBattleMedium = b'PostBattleMediumStates'
    PostBattleLarge = b'PostBattleLargeStates'
    PostBattleVictory = b'PostBattleVictoryStates'
    PostBattleDefeat = b'PostBattleDefeatStates'
    PostBattleCommon = b'PostBattleCommonStates'
    Comp7PostBattleSmall = b'Comp7PostBattleSmallStates'
    Comp7PostBattleMedium = b'Comp7PostBattleMediumStates'
    Comp7PostBattleLarge = b'Comp7PostBattleLargeStates'
    Comp7PostBattleVictory = b'Comp7PostBattleVictoryStates'
    Comp7PostBattleDefeat = b'Comp7PostBattleDefeatStates'
    Comp7PostBattleCommon = b'Comp7PostBattleCommonStates'
