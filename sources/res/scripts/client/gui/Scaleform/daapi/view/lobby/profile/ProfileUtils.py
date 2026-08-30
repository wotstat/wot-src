from __future__ import absolute_import, division
from debug_utils import LOG_ERROR
from gui.Scaleform.locale.PROFILE import PROFILE
from gui.battle_results.components import style
from gui.impl import backport
from gui.shared.formatters import text_styles
from gui.shared.gui_items.dossier.stats import _MaxVehicleStatsBlock, _FalloutStatsBlock
from gui.shared.gui_items.dossier.stats import _VehiclesStatsBlock
from helpers import dependency
from helpers import i18n
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

def _emptyField(targetData, isCurrentUser):
    return


class _AbstractField(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, label, tooltip):
        super(_AbstractField, self).__init__()
        self._label = label
        self._tooltip = tooltip
        return

    def __call__(self, targetData, isCurrentUser):
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), self._tooltip, self._buildTooltipData(targetData, isCurrentUser))

    def isVisible(self, targetData, isCurrentUser):
        return True

    def _buildData(self, targetData, isCurrentUser):
        return

    def _buildTooltipData(self, targetData, isCurrentUser):
        return


class _OnlyAccountField(_AbstractField):

    def isVisible(self, targetData, isCurrentUser):
        return isinstance(targetData, _VehiclesStatsBlock)


class _OnlyTechniqueField(_AbstractField):

    def isVisible(self, targetData, isCurrentUser):
        return not isinstance(targetData, _VehiclesStatsBlock)


class _BattlesCountField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getBattlesCount())

    def _buildTooltipData(self, targetData, isCurrentUser):
        lossesCount = targetData.getLossesCount()
        winsCount = targetData.getWinsCount()
        drawsCount = targetData.getDrawsCount()
        drawsStr = backport.getIntegralFormat(drawsCount) if drawsCount >= 0 else ProfileUtils.UNAVAILABLE_SYMBOL
        return ProfileUtils.createToolTipData((
         backport.getIntegralFormat(winsCount),
         backport.getIntegralFormat(lossesCount),
         drawsStr))


class _WinsEfficiencyField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return ProfileUtils.formatFloatPercent(ProfileUtils.getValueOrUnavailable(targetData.getWinsEfficiency()))


class _WinsField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getWinsCount())


class _SurvivalField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return ProfileUtils.formatFloatPercent(ProfileUtils.getValueOrUnavailable(targetData.getSurvivalEfficiency()))


class _HitsField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return ProfileUtils.formatFloatPercent(ProfileUtils.getValueOrUnavailable(targetData.getHitsEfficiency()))


class _DamageCoefficientField(_AbstractField):

    def __call__(self, targetData, isCurrentUser):
        tooltip = self._tooltip
        if isinstance(targetData, _FalloutStatsBlock):
            if not isinstance(targetData, _VehiclesStatsBlock):
                tooltip += b'/vehicle'
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), tooltip, self._buildTooltipData(targetData, isCurrentUser))

    def _buildData(self, targetData, isCurrentUser):
        return ProfileUtils.formatEfficiency(targetData.getDamageReceived(), targetData.getDamageEfficiency)

    def _buildTooltipData(self, targetData, isCurrentUser):
        damageToolTipData = [
         backport.getIntegralFormat(targetData.getDamageDealt()),
         backport.getIntegralFormat(targetData.getDamageReceived())]
        if isinstance(targetData, _FalloutStatsBlock):
            if isinstance(targetData, _VehiclesStatsBlock):
                damageToolTipData.append(backport.getIntegralFormat(targetData.getConsumablesDamageDealt()))
        return ProfileUtils.createToolTipData(damageToolTipData)


class _DestructionCoefficientField(_AbstractField):

    def __call__(self, targetData, isCurrentUser):
        tooltip = self._tooltip
        if isinstance(targetData, _FalloutStatsBlock):
            if not isinstance(targetData, _VehiclesStatsBlock):
                tooltip += b'/vehicle'
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), tooltip, self._buildTooltipData(targetData, isCurrentUser))

    def _buildData(self, targetData, isCurrentUser):
        return ProfileUtils.formatEfficiency(targetData.getDeathsCount(), targetData.getFragsEfficiency)

    def _buildTooltipData(self, targetData, isCurrentUser):
        destructionToolTipData = [
         backport.getIntegralFormat(targetData.getFragsCount()),
         backport.getIntegralFormat(targetData.getDeathsCount())]
        if isinstance(targetData, _FalloutStatsBlock):
            if isinstance(targetData, _VehiclesStatsBlock):
                destructionToolTipData.append(backport.getIntegralFormat(targetData.getConsumablesFragsCount()))
        return ProfileUtils.createToolTipData(destructionToolTipData)


class _ArmorusingField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        damageBlockedByArmor = targetData.getDamageBlockedByArmor()
        potentialDamageReceived = targetData.getPotentialDamageReceived()
        pResDmg = potentialDamageReceived - damageBlockedByArmor
        return ProfileUtils.formatEfficiency(pResDmg, targetData.getArmorUsingEfficiency)

    def _buildTooltipData(self, targetData, isCurrentUser):
        return ProfileUtils.createToolTipData((
         ProfileUtils.getAvgDamageBlockedValue(targetData),))


def _avgExpField(targetData, isCurrentUser):
    formatedExp = backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgXP()))
    return DetailedStatisticsUtils.getDetailedDataObject(PROFILE.SECTION_STATISTICS_SCORES_AVGEXPERIENCE_SHORT, formatedExp, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGEX_SHORT)


class _AvgDmgField(_AbstractField):

    def __call__(self, targetData, isCurrentUser):
        tooltip = self._tooltip
        if isinstance(targetData, _FalloutStatsBlock):
            if not isinstance(targetData, _VehiclesStatsBlock):
                tooltip += b'/vehicle'
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), tooltip, None)

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgDamage()))


class _AvgReceivedDmgField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgDamageReceived()))


def _avgAssignedDmgField(targetData, isCurrentUser):
    formatedAssignedDmg = ProfileUtils.formatEfficiency(targetData.getBattlesCountVer2(), targetData.getDamageAssistedEfficiency)
    return DetailedStatisticsUtils.getDetailedDataObject(PROFILE.SECTION_STATISTICS_SCORES_AVGASSISTEDDAMAGE_SHORTSELF if isCurrentUser else PROFILE.SECTION_STATISTICS_SCORES_AVGASSISTEDDAMAGE_SHORTOTHER, formatedAssignedDmg, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGASSISTEDDAMAGE_SHORTSELF if isCurrentUser else PROFILE.PROFILE_PARAMS_TOOLTIP_AVGASSISTEDDAMAGE_SHORTOTHER)


class _AvgHealthRepairField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        avgValue = targetData.getAvgHealthRepair() or ProfileUtils.UNAVAILABLE_VALUE
        return backport.getIntegralFormat(avgValue)


class _AvgEnemiesSpottedField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgEnemiesSpotted()))


class _StunFieldMixin(object):
    lobbyContext = dependency.descriptor(ILobbyContext)

    def isVisible(self, targetData, isCurrentUser):
        return super(_StunFieldMixin, self).isVisible(targetData, isCurrentUser) and self.lobbyContext.getServerSettings().spgRedesignFeatures.isStunEnabled()


class _StunNumberField(_StunFieldMixin, _OnlyTechniqueField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getStunNumber()))


class _AvgStunNumberField(_StunFieldMixin, _AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgStunNumber()))


class _AssistedStunDmgField(_StunFieldMixin, _OnlyTechniqueField):

    def __init__(self):
        super(_AssistedStunDmgField, self).__init__(label=b'', tooltip=b'')
        return

    def __call__(self, targetData, isCurrentUser):
        label, tooltip = self._getSelfStrings() if isCurrentUser else self._getOtherStrings()
        return DetailedStatisticsUtils.getDetailedDataObject(label, self._buildData(targetData, isCurrentUser), tooltip, self._buildTooltipData(targetData, isCurrentUser))

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getDamageAssistedStun()))

    @staticmethod
    def _getSelfStrings():
        label = PROFILE.SECTION_TECHNIQUE_STATISTICS_ASSISTEDSTUNDAMAGE_SHORTSELF
        tooltip = PROFILE.PROFILE_PARAMS_TOOLTIP_ASSISTEDSTUNDAMAGE_SHORTSELF
        return (label, tooltip)

    @staticmethod
    def _getOtherStrings():
        label = PROFILE.SECTION_TECHNIQUE_STATISTICS_ASSISTEDSTUNDAMAGE_SHORTOTHER
        tooltip = PROFILE.PROFILE_PARAMS_TOOLTIP_ASSISTEDSTUNDAMAGE_SHORTOTHER
        return (label, tooltip)


class _AvgAssistedStunDmgField(_StunFieldMixin, _AbstractField):

    def __init__(self):
        super(_AvgAssistedStunDmgField, self).__init__(label=b'', tooltip=b'')
        return

    def __call__(self, targetData, isCurrentUser):
        label, tooltip = self._getSelfStrings() if isCurrentUser else self._getOtherStrings()
        return DetailedStatisticsUtils.getDetailedDataObject(label, self._buildData(targetData, isCurrentUser), tooltip, self._buildTooltipData(targetData, isCurrentUser))

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgDamageAssistedStun()))

    @staticmethod
    def _getSelfStrings():
        label = PROFILE.SECTION_STATISTICS_DETAILED_AVGASSISTEDSTUNDAMAGE_SHORTSELF
        tooltip = PROFILE.PROFILE_PARAMS_TOOLTIP_AVGASSISTEDSTUNDAMAGE_SHORTSELF
        return (label, tooltip)

    @staticmethod
    def _getOtherStrings():
        label = PROFILE.SECTION_STATISTICS_DETAILED_AVGASSISTEDSTUNDAMAGE_SHORTOTHER
        tooltip = PROFILE.PROFILE_PARAMS_TOOLTIP_AVGASSISTEDSTUNDAMAGE_SHORTOTHER
        return (label, tooltip)


def _avgDetectedField(targetData, isCurrentUser):
    formatedDetected = backport.getNiceNumberFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgEnemiesSpotted()))
    return DetailedStatisticsUtils.getDetailedDataObject(PROFILE.SECTION_STATISTICS_DETAILED_AVGDETECTEDENEMIES, formatedDetected, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGDETECTEDENEMIES)


class _AvgDestroyedField(_AbstractField):

    def __call__(self, targetData, isCurrentUser):
        tooltip = self._tooltip
        if isinstance(targetData, _FalloutStatsBlock):
            if not isinstance(targetData, _VehiclesStatsBlock):
                tooltip += b'/vehicle'
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), tooltip, None)

    def _buildData(self, targetData, isCurrentUser):
        return backport.getNiceNumberFormat(ProfileUtils.getValueOrUnavailable(targetData.getAvgFrags()))


class _MaxXPField(_AbstractField):

    def __call__(self, targetData, isCurrentUser):
        tooltip = self._tooltip
        tooltipData = None
        if isinstance(targetData, _MaxVehicleStatsBlock):
            tooltipData = self._buildTooltipData(targetData, isCurrentUser)
        else:
            tooltip = self._tooltip + b'/vehicle'
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), tooltip, tooltipData)

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getMaxXp())

    def _buildTooltipData(self, targetData, isCurrentUser):
        maxXpVehicle = self.itemsCache.items.getItemByCD(targetData.getMaxXpVehicle())
        return ProfileUtils.getRecordTooltipDataByVehicle(maxXpVehicle)


class _MaxDamageField(_AbstractField):

    def __init__(self, label, tooltip, unavailableTooltip):
        super(_MaxDamageField, self).__init__(label, tooltip)
        self._unavailableTooltip = unavailableTooltip
        return

    def __call__(self, targetData, isCurrentUser):
        tooltip = self._unavailableTooltip
        tooltipData = None
        if targetData.getBattlesCountVer3() > 0:
            tooltip = self._tooltip
            if isinstance(targetData, _MaxVehicleStatsBlock):
                tooltipData = self._buildTooltipData(targetData, isCurrentUser)
            else:
                tooltip = self._tooltip + b'/vehicle'
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), tooltip, tooltipData)

    def _buildData(self, targetData, isCurrentUser):
        if targetData.getBattlesCountVer3() > 0:
            return backport.getIntegralFormat(targetData.getMaxDamage())
        return ProfileUtils.UNAVAILABLE_VALUE

    def _buildTooltipData(self, targetData, isCurrentUser):
        maxDamageVehicle = self.itemsCache.items.getItemByCD(targetData.getMaxDamageVehicle())
        return ProfileUtils.getRecordTooltipDataByVehicle(maxDamageVehicle)


class _MaxDestroyedField(_AbstractField):

    def __call__(self, targetData, isCurrentUser):
        tooltip = self._tooltip
        tooltipData = None
        if isinstance(targetData, _MaxVehicleStatsBlock):
            tooltipData = self._buildTooltipData(targetData, isCurrentUser)
        else:
            tooltip = self._tooltip + b'/vehicle'
        return DetailedStatisticsUtils.getDetailedDataObject(self._label, self._buildData(targetData, isCurrentUser), tooltip, tooltipData)

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getMaxFrags())

    def _buildTooltipData(self, targetData, isCurrentUser):
        maxFragsVehicle = self.itemsCache.items.getItemByCD(targetData.getMaxFragsVehicle())
        return ProfileUtils.getRecordTooltipDataByVehicle(maxFragsVehicle)


class _CapturePointsField(_OnlyAccountField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getCapturePoints())


class _DroppedPointsField(_OnlyAccountField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getDroppedCapturePoints())


class _TotalVehiclesField(_OnlyAccountField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getTotalVehicles())


class _BattleRoyaleBattlesCountField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getBattlesCount())


class _BattleRoyaleWinsEfficiencyField(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getWinsCount()))


class _AveragePositionBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getNiceNumberFormat(ProfileUtils.getValueOrUnavailable(targetData.getAveragePosition()))


class _AverageVehicleLevelBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getNiceNumberFormat(ProfileUtils.getValueOrUnavailable(targetData.getAverageLevel()))


class _MaxBattleXPBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getMaxXp()))

    def _buildTooltipData(self, targetData, isCurrentUser):
        maxXpVehicle = self.itemsCache.items.getItemByCD(targetData.getMaxXpVehicle())
        return ProfileUtils.getRecordTooltipDataByVehicle(maxXpVehicle)


class _MaxBattleDamageBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getMaxDamage()))

    def _buildTooltipData(self, targetData, isCurrentUser):
        maxXpVehicle = self.itemsCache.items.getItemByCD(targetData.getMaxDamageVehicle())
        return ProfileUtils.getRecordTooltipDataByVehicle(maxXpVehicle)


class _MaxBattleFragsBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(ProfileUtils.getValueOrUnavailable(targetData.getMaxFrags()))

    def _buildTooltipData(self, targetData, isCurrentUser):
        maxXpVehicle = self.itemsCache.items.getItemByCD(targetData.getMaxFragsVehicle())
        return ProfileUtils.getRecordTooltipDataByVehicle(maxXpVehicle)


class _MaxBattleXPVehicleBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getMaxXp())


class _MaxBattleDamageVehicleBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getMaxDamage())


class _MaxBattleFragsVehicleBR(_AbstractField):

    def _buildData(self, targetData, isCurrentUser):
        return backport.getIntegralFormat(targetData.getMaxFrags())


def _totalVehiclesField(targetData, isCurrentUser):
    formattedVehicles = backport.getIntegralFormat(targetData.getTotalVehicles())
    return DetailedStatisticsUtils.getDetailedDataObject(PROFILE.SECTION_STATISTICS_SCORES_TOTALVEHS, formattedVehicles, PROFILE.PROFILE_PARAMS_TOOLTIP_TOTALVEHS)


def _flagsDeliveredField(targetData, isCurrentUser):
    formattedDelivered = backport.getIntegralFormat(targetData.getFlagsDelivered())
    return DetailedStatisticsUtils.getDetailedDataObject(PROFILE.SECTION_STATISTICS_SCORES_FLAGSDELIVERED, formattedDelivered, PROFILE.PROFILE_PARAMS_TOOLTIP_FLAGSDELIVERED)


def _flagsAbsorbedField(targetData, isCurrentUser):
    formattedAbsorbed = backport.getIntegralFormat(targetData.getFlagsAbsorbed())
    return DetailedStatisticsUtils.getDetailedDataObject(PROFILE.SECTION_STATISTICS_SCORES_FLAGSABSORBED, formattedAbsorbed, PROFILE.PROFILE_PARAMS_TOOLTIP_FLAGSABSORBED)


def _maxWinPointsField(targetData, isCurrentUser):
    formatedMaxWP = backport.getIntegralFormat(targetData.getMaxVictoryPoints())
    return DetailedStatisticsUtils.getDetailedDataObject(PROFILE.SECTION_STATISTICS_SCORES_MAXVICTORYPOINTS, formatedMaxWP, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXVICTORYPOINTS)


COMMON_SECTION_FIELDS = (
 _BattlesCountField(PROFILE.SECTION_STATISTICS_SCORES_TOTALBATTLES, PROFILE.PROFILE_PARAMS_TOOLTIP_BATTLESCOUNT),
 _WinsEfficiencyField(PROFILE.SECTION_STATISTICS_SCORES_TOTALWINS, PROFILE.PROFILE_PARAMS_TOOLTIP_WINS),
 _SurvivalField(PROFILE.SECTION_STATISTICS_SCORES_SURVIVAL, PROFILE.PROFILE_PARAMS_TOOLTIP_SURVIVAL),
 _HitsField(PROFILE.SECTION_STATISTICS_SCORES_HITS, PROFILE.PROFILE_PARAMS_TOOLTIP_HITS),
 _emptyField,
 _DamageCoefficientField(PROFILE.SECTION_STATISTICS_DETAILED_DAMAGECOEFFICIENT, PROFILE.PROFILE_PARAMS_TOOLTIP_DAMAGECOEFF),
 _DestructionCoefficientField(PROFILE.SECTION_STATISTICS_DETAILED_DESTRUCTIONCOEFFICIENT, PROFILE.PROFILE_PARAMS_TOOLTIP_DESTROYCOEFF),
 _ArmorusingField(PROFILE.SECTION_STATISTICS_SCORES_ARMORUSING, PROFILE.PROFILE_PARAMS_TOOLTIP_ARMORUSING),
 _CapturePointsField(PROFILE.SECTION_STATISTICS_SCORES_CAPTUREPOINTS, PROFILE.PROFILE_PARAMS_TOOLTIP_CAPTUREPOINTS),
 _DroppedPointsField(PROFILE.SECTION_STATISTICS_SCORES_DROPPEDCAPTUREPOINTS, PROFILE.PROFILE_PARAMS_TOOLTIP_DROPPEDCAPTUREPOINTS),
 _StunNumberField(PROFILE.SECTION_TECHNIQUE_STATISTICS_STUNNUMBER, PROFILE.PROFILE_PARAMS_TOOLTIP_STUNNUMBER),
 _AssistedStunDmgField())
COMMON_SECTION_FALLOUT_FIELDS = (
 _BattlesCountField(PROFILE.SECTION_STATISTICS_SCORES_TOTALBATTLES, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_BATTLESCOUNT),
 _WinsField(PROFILE.SECTION_STATISTICS_SCORES_TOTALWINS, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_WINS),
 _HitsField(PROFILE.SECTION_STATISTICS_SCORES_HITS, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_HITS),
 _DamageCoefficientField(PROFILE.SECTION_STATISTICS_DETAILED_DAMAGECOEFFICIENT, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_DAMAGECOEFF),
 _DestructionCoefficientField(PROFILE.SECTION_STATISTICS_DETAILED_DESTRUCTIONCOEFFICIENT, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_DESTROYCOEFF),
 _ArmorusingField(PROFILE.SECTION_STATISTICS_SCORES_ARMORUSING, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_ARMORUSING),
 _TotalVehiclesField(PROFILE.SECTION_STATISTICS_SCORES_TOTALVEHS, PROFILE.PROFILE_PARAMS_TOOLTIP_TOTALVEHS),
 _emptyField,
 _flagsDeliveredField,
 _flagsAbsorbedField)
AVERAGE_SECTION_FIELDS = (
 _avgExpField,
 _emptyField,
 _AvgDmgField(PROFILE.SECTION_STATISTICS_DETAILED_AVGDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGDMG_SHORT),
 _AvgReceivedDmgField(PROFILE.SECTION_STATISTICS_DETAILED_AVGRECEIVEDDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGRECEIVEDDAMAGE),
 _AvgStunNumberField(PROFILE.SECTION_TECHNIQUE_STATISTICS_AVGSTUNNUMBER, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGSTUNNUMBER),
 _avgAssignedDmgField,
 _AvgAssistedStunDmgField(),
 _emptyField,
 _avgDetectedField,
 _AvgDestroyedField(PROFILE.SECTION_STATISTICS_DETAILED_AVGDESTROYEDVEHICLES, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGDESTROYEDVEHICLES))
AVERAGE_SECTION_FALLOUT_FIELDS = (
 _avgExpField,
 _emptyField,
 _AvgDmgField(PROFILE.SECTION_STATISTICS_DETAILED_AVGDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_AVGDMG_SHORT),
 _AvgReceivedDmgField(PROFILE.SECTION_STATISTICS_DETAILED_AVGRECEIVEDDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_AVGRECEIVEDDAMAGE),
 _emptyField,
 _AvgDestroyedField(PROFILE.SECTION_STATISTICS_DETAILED_AVGDESTROYEDVEHICLES, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_AVGDESTROYEDVEHICLES))
RECORD_SECTION_FIELDS = (
 _MaxXPField(PROFILE.SECTION_STATISTICS_SCORES_MAXEXPERIENCE, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXEXP),
 _MaxDamageField(PROFILE.SECTION_STATISTICS_SCORES_MAXDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_UNAVAILABLEMAXDAMAGE),
 _MaxDestroyedField(PROFILE.SECTION_STATISTICS_DETAILED_MAXDESTROYEDVEHICLES, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXDESTROYED))
RECORD_SECTION_FALLOUT_FIELDS = (
 _MaxXPField(PROFILE.SECTION_STATISTICS_SCORES_MAXEXPERIENCE, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXEXP),
 _MaxDamageField(PROFILE.SECTION_STATISTICS_SCORES_MAXDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_MAXDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_UNAVAILABLEMAXDAMAGE),
 _MaxDestroyedField(PROFILE.SECTION_STATISTICS_DETAILED_MAXDESTROYEDVEHICLES, PROFILE.PROFILE_PARAMS_TOOLTIP_DIF_FALLOUT_MAXDESTROYED),
 _maxWinPointsField)
STATISTICS_LAYOUT = (
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_COMMON,
  COMMON_SECTION_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_AVERAGE,
  AVERAGE_SECTION_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_RECORD,
  RECORD_SECTION_FIELDS))
FALLOUT_STATISTICS_LAYOUT = (
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_COMMON,
  COMMON_SECTION_FALLOUT_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_AVERAGE,
  AVERAGE_SECTION_FALLOUT_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_RECORD,
  RECORD_SECTION_FALLOUT_FIELDS))
BATTLE_ROYALE_SECTION_FIELDS = (
 _BattleRoyaleBattlesCountField(PROFILE.SECTION_STATISTICS_SCORES_TOTALBATTLES, PROFILE.PROFILE_PARAMS_TOOLTIP_BRBATTLESCOUNT),
 _BattleRoyaleWinsEfficiencyField(PROFILE.SECTION_STATISTICS_SCORES_TOTALWINS, PROFILE.PROFILE_PARAMS_TOOLTIP_BRWINS),
 _AveragePositionBR(PROFILE.SECTION_SUMMARY_SCORES_AVERAGERANK, PROFILE.PROFILE_PARAMS_TOOLTIP_BRAVERAGERANK),
 _AverageVehicleLevelBR(PROFILE.SECTION_SUMMARY_SCORES_AVERAGELEVEL, PROFILE.PROFILE_PARAMS_TOOLTIP_BRAVERAGELEVEL),
 _HitsField(PROFILE.SECTION_STATISTICS_SCORES_HITS, PROFILE.PROFILE_PARAMS_TOOLTIP_HITS),
 _emptyField,
 _DamageCoefficientField(PROFILE.SECTION_STATISTICS_DETAILED_DAMAGECOEFFICIENT, PROFILE.PROFILE_PARAMS_TOOLTIP_DAMAGECOEFF),
 _DestructionCoefficientField(PROFILE.SECTION_STATISTICS_DETAILED_DESTRUCTIONCOEFFICIENT, PROFILE.PROFILE_PARAMS_TOOLTIP_DESTROYCOEFF))
BR_AVERAGE_SECTION_FIELDS = (
 _avgExpField,
 _emptyField,
 _AvgDmgField(PROFILE.SECTION_STATISTICS_DETAILED_AVGDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGDMG_SHORT),
 _AvgReceivedDmgField(PROFILE.SECTION_STATISTICS_DETAILED_AVGRECEIVEDDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGRECEIVEDDAMAGE),
 _emptyField,
 _AvgDestroyedField(PROFILE.SECTION_STATISTICS_DETAILED_AVGDESTROYEDVEHICLES, PROFILE.PROFILE_PARAMS_TOOLTIP_AVGDESTROYEDVEHICLES))
BR_RECORD_SECTION_FIELDS = (
 _MaxBattleXPBR(PROFILE.SECTION_STATISTICS_SCORES_MAXEXPERIENCE, PROFILE.PROFILE_PARAMS_TOOLTIP_BRMAXEXP),
 _MaxBattleDamageBR(PROFILE.SECTION_STATISTICS_SCORES_MAXDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_BRMAXDAMAGE),
 _MaxBattleFragsBR(PROFILE.SECTION_STATISTICS_DETAILED_MAXDESTROYEDVEHICLES, PROFILE.PROFILE_PARAMS_TOOLTIP_BRMAXFRAGS))
BR_VEHICLE_RECORD_SECTION_FIELDS = (
 _MaxBattleXPVehicleBR(PROFILE.SECTION_STATISTICS_SCORES_MAXEXPERIENCE, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXEXP_VEHICLE),
 _MaxBattleDamageVehicleBR(PROFILE.SECTION_STATISTICS_SCORES_MAXDAMAGE, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXDAMAGE_VEHICLE),
 _MaxBattleFragsVehicleBR(PROFILE.SECTION_STATISTICS_DETAILED_MAXDESTROYEDVEHICLES, PROFILE.PROFILE_PARAMS_TOOLTIP_MAXDESTROYED_VEHICLE))
BATTLE_ROYALE_STATISTICS_LAYOUT = (
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_COMMON,
  BATTLE_ROYALE_SECTION_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_AVERAGE,
  BR_AVERAGE_SECTION_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_RECORD,
  BR_RECORD_SECTION_FIELDS))
BATTLE_ROYALE_VEHICLE_STATISTICS_LAYOUT = (
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_COMMON,
  BATTLE_ROYALE_SECTION_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_AVERAGE,
  BR_AVERAGE_SECTION_FIELDS),
 (
  PROFILE.SECTION_STATISTICS_BODYPARAMS_LABEL_RECORD,
  BR_VEHICLE_RECORD_SECTION_FIELDS))

class HeaderItemsTypes(object):
    VALUE_PREFIX = b'value_'
    COMMON = b'common'
    RATIO = b'ratio'
    VALUES = b'values'


class ProfileUtils(object):
    UNAVAILABLE_VALUE = -1
    UNAVAILABLE_SYMBOL = b'--'
    PERCENT_SYMBOL = b'%'
    VIEW_TYPE_TABLES = 0
    VIEW_TYPE_CHARTS = 1
    VIEW_TYPE_TABLE = 2
    itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def packProfileDossierInfo(cls, targetData, accountDossier):
        outcome = ProfileUtils.packProfileCommonInfo(targetData)
        epicRandomVehicles = set(accountDossier.getEpicRandomStats().getVehicles().keys())
        totalVehiclesCount = len(epicRandomVehicles.union(set(accountDossier.getRandomStats().getVehicles().keys())))
        vehicle = cls.itemsCache.items.getItemByCD(targetData.getMaxXpVehicle())
        outcome[b'maxXPByVehicle'] = vehicle.shortUserName if vehicle is not None else b''
        outcome[b'marksOfMasteryText'] = style.makeMarksOfMasteryText(backport.getIntegralFormat(targetData.getMarksOfMastery()[3]), totalVehiclesCount)
        return outcome

    @staticmethod
    def packProfileCommonInfo(targetData):
        outcome = {}
        outcome[b'battlesCount'] = targetData.getBattlesCount()
        outcome[b'lossesCount'] = targetData.getLossesCount()
        outcome[b'winsCount'] = targetData.getWinsCount()
        outcome[b'hitsEfficiency'] = ProfileUtils.getValueOrUnavailable(targetData.getHitsEfficiency())
        outcome[b'maxXP'] = targetData.getMaxXp()
        outcome[b'avgXP'] = ProfileUtils.getValueOrUnavailable(targetData.getAvgXP())
        return outcome

    @staticmethod
    def getIconPath(icon):
        return b'../maps/icons/library/dossier/' + icon

    @staticmethod
    def formatFloatPercent(value):
        if value != ProfileUtils.UNAVAILABLE_VALUE:
            value = value * 100
            value = text_styles.concatStylesWithSpace(backport.getNiceNumberFormat(value), ProfileUtils.PERCENT_SYMBOL)
        return str(value)

    @staticmethod
    def getFormattedWinsEfficiency(targetData):
        winsEfficiency = targetData.getWinsEfficiency()
        formattedWinsEfficiency = ProfileUtils.formatFloatPercent(ProfileUtils.getValueOrUnavailable(winsEfficiency))
        return formattedWinsEfficiency

    @staticmethod
    def formatEfficiency(coeff2, valueReceiveFunction):
        if coeff2 > 0:
            return backport.getNiceNumberFormat(valueReceiveFunction())
        return ProfileUtils.UNAVAILABLE_VALUE

    @staticmethod
    def getEfficiencyPercent(dividend, delimiter, unavailableValue=UNAVAILABLE_VALUE):
        if delimiter != 0:
            return backport.getNiceNumberFormat(float(dividend) / delimiter * 100) + ProfileUtils.PERCENT_SYMBOL
        return unavailableValue

    @staticmethod
    def packLditItemData(text, description, tooltip, icon, tooltipData=None):
        finalText = text
        enabled = True
        if text in (-1, b'-1'):
            enabled = False
            finalText = ProfileUtils.UNAVAILABLE_SYMBOL
        return {b'text': finalText, 
           b'description': (i18n.makeString(description)), 
           b'iconPath': (ProfileUtils.getIconPath(icon)), 
           b'tooltip': tooltip, 
           b'tooltipData': tooltipData, 
           b'enabled': enabled}

    @staticmethod
    def getValueOrUnavailable(targetValue):
        if targetValue is not None:
            return targetValue
        else:
            return ProfileUtils.UNAVAILABLE_VALUE

    @staticmethod
    def getLabelDataObject(label, data):
        return {b'label': (i18n.makeString(label)), 
           b'data': data}

    @staticmethod
    def getLabelViewTypeDataObject(label, data, viewType):
        if viewType not in (
         ProfileUtils.VIEW_TYPE_TABLES,
         ProfileUtils.VIEW_TYPE_CHARTS,
         ProfileUtils.VIEW_TYPE_TABLE):
            LOG_ERROR(b'Unknown view type', viewType)
            return None
        else:
            result = ProfileUtils.getLabelDataObject(label, data)
            result[b'viewType'] = viewType
            if viewType == ProfileUtils.VIEW_TYPE_TABLES:
                result[b'linkage'] = b'DetailedStatisticsView_UI'
            elif viewType == ProfileUtils.VIEW_TYPE_CHARTS:
                result[b'linkage'] = b'ChartsStatisticsView_UI'
            elif viewType == ProfileUtils.VIEW_TYPE_TABLE:
                result[b'linkage'] = b'ClanProfileTableStatisticsViewUI'
            return result

    @staticmethod
    def createToolTipData(bodyParamsList):
        result = {}
        bodyData = None
        if bodyParamsList is not None:
            bodyData = {}
            for i, param in enumerate(bodyParamsList):
                bodyData[HeaderItemsTypes.VALUE_PREFIX + str(i)] = text_styles.titleFont(str(param))

        result[b'body'] = bodyData
        result[b'header'] = {}
        result[b'note'] = None
        return result

    @staticmethod
    def getTotalBattlesHeaderParam(targetData, description, tooltip):
        battlesCount = targetData.getBattlesCount()
        lossesCount = targetData.getLossesCount()
        winsCount = targetData.getWinsCount()
        drawsCount = targetData.getDrawsCount()
        drawsStr = backport.getIntegralFormat(drawsCount) if drawsCount >= 0 else ProfileUtils.UNAVAILABLE_SYMBOL
        battlesToolTipData = (
         backport.getIntegralFormat(winsCount),
         backport.getIntegralFormat(lossesCount),
         drawsStr)
        return ProfileUtils.packLditItemData(backport.getIntegralFormat(battlesCount), description, tooltip, b'battles40x32.png', ProfileUtils.createToolTipData(battlesToolTipData))

    @classmethod
    def getVehicleRecordTooltipData(cls, getValueMethod):
        return ProfileUtils.getRecordTooltipDataByVehicle(cls.itemsCache.items.getItemByCD(getValueMethod()))

    @staticmethod
    def getRecordTooltipDataByVehicle(vehicle):
        if vehicle is not None:
            return ProfileUtils.createToolTipData([vehicle.shortUserName])
        else:
            return ProfileUtils.createToolTipData(None)

    @staticmethod
    def getAvailableValueStr(value):
        if value != -1:
            return value
        return ProfileUtils.UNAVAILABLE_SYMBOL

    @staticmethod
    def getAvgDamageBlockedValue(targetData):
        value = ProfileUtils.formatEfficiency(targetData.getBattlesCountVer3(), targetData.getAvgDamageBlocked)
        return ProfileUtils.getAvailableValueStr(value)


class DetailedStatisticsUtils(object):

    @staticmethod
    def getDetailedDataObject(label, value, tooltip, tooltipData=None):
        dataObject = ProfileUtils.getLabelDataObject(label, value)
        dataObject[b'tooltip'] = tooltip
        dataObject[b'tooltipData'] = tooltipData
        return dataObject

    @staticmethod
    def getStatistics(targetData, isCurrentUser, layout):
        result = []
        for section, fields in layout:
            sectionFields = []
            for field in fields:
                if not isinstance(field, _AbstractField) or field.isVisible(targetData, isCurrentUser):
                    sectionFields.append(field(targetData, isCurrentUser))

            result.append(ProfileUtils.getLabelDataObject(section, sectionFields))

        return result


def getProfileCommonInfo(userName, dossier):
    lastBattleTimeUserString = None
    if dossier[b'total'][b'lastBattleTime']:
        lbt = dossier[b'total'][b'lastBattleTime']
        lastBattleTimeUserString = b'%s %s' % (
         backport.getLongDateFormat(lbt),
         backport.getShortTimeFormat(lbt))
    return {b'name': userName, 
       b'registrationDate': (b'%s' % backport.getLongDateFormat(dossier[b'total'][b'creationTime'])), 
       b'lastBattleDate': lastBattleTimeUserString}
