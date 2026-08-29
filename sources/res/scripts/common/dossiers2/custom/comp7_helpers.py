import collections, operator
from dossiers2.common.updater_utils import getStaticSizeBlockRecordValues, getDictBlockRecordValues, updateDictRecords, addRecords, removeRecords, updateStaticSizeBlockRecords
SEASON_KEY = b'comp7Season'
MAX_SEASON_KEY = b'maxComp7Season'
CUT_SEASON_KEY = b'comp7CutSeason'

def getSeasonsRecords(seasonKey, seasonsNumber, ctx, packing):
    seasonsRecords = []
    for seasonNumber in range(seasonsNumber):
        key = (b'{}{}').format(seasonKey, seasonNumber + 1)
        seasonsRecords.append(getStaticSizeBlockRecordValues(ctx, key, packing))

    return seasonsRecords


def getSeasonsRecordsWithGriffin(seasonKey, seasonsNumber, ctx, packing, archiveName):
    seasonsRecords = []
    for seasonNumber in range(seasonsNumber):
        key = (b'{}{}').format(seasonKey, seasonNumber + 1)
        seasonsRecords.append(getStaticSizeBlockRecordValues(ctx, key, packing))

    seasonsRecords.append(getStaticSizeBlockRecordValues(ctx, archiveName, packing))
    return seasonsRecords


def getCutSeasonsRecords(seasonKey, seasonsNumber, ctx):
    cutRecords = []
    for seasonNumber in range(seasonsNumber):
        key = (b'{}{}').format(seasonKey, seasonNumber + 1)
        cutRecords.append(getDictBlockRecordValues(ctx, key, b'I', b'IIII'))

    return cutRecords


def getCutSeasonsRecordsWithGriffin(seasonKey, seasonsNumber, ctx, archiveName):
    cutRecords = []
    for seasonNumber in range(seasonsNumber):
        key = (b'{}{}').format(seasonKey, seasonNumber + 1)
        cutRecords.append(getDictBlockRecordValues(ctx, key, b'I', b'IIII'))

    cutRecords.append(getDictBlockRecordValues(ctx, archiveName, b'I', b'IIII'))
    return cutRecords


def getSumSeasonsValues(seasonsValues):
    return dict(reduce(operator.add, map(collections.Counter, seasonsValues)))


def getMaxSeasonsValues(seasonsValues):
    maxValues = seasonsValues[0]
    for seasonValues in seasonsValues[1:]:
        for key, value in seasonValues.iteritems():
            if key.endswith(b'Vehicle'):
                continue
            if value >= maxValues.get(key):
                maxValues[key] = value
                vehicleKey = (b'{}Vehicle').format(key)
                if vehicleKey in seasonValues:
                    maxValues[vehicleKey] = seasonValues[vehicleKey]

    return maxValues


def prepareArchiveSeasonsRecords(values, packing):
    archiveRecords = []
    for key, packingFormat in packing.iteritems():
        archiveRecords.append((packingFormat[0], packingFormat[1], values.get(key, 0)))

    return archiveRecords


def prepareArchiveCutSeasonsRecords(cutSeasonsValues):
    cutArchiveRecords = cutSeasonsValues[0]
    for seasonValue in cutSeasonsValues[1:]:
        for key, value in seasonValue.iteritems():
            archiveValue = cutArchiveRecords.setdefault(key, (0, 0, 0, 0))
            cutArchiveRecords[key] = tuple(map(sum, tuple(zip(archiveValue, value))))

    return cutArchiveRecords


def clearSeasonsRecords(seasonsNumber, seasonsKey, ctx, packing):
    for seasonNumber in range(seasonsNumber):
        removeRecords(ctx, (b'{}{}').format(seasonsKey, seasonNumber + 1), packing)

    return


def clearCutSeasonsRecords(seasonsNumber, ctx):
    for seasonNumber in range(seasonsNumber):
        updateDictRecords(ctx, (b'{}{}').format(CUT_SEASON_KEY, seasonNumber + 1), b'I', b'IIII', {})

    return


def addSeasonRecord(updateCtx, seasonKey, fields, values):
    addRecords(updateCtx, seasonKey, fields, values)
    return


def archiveSeasonsGriffin(seasonsNumber, ctx, seasonsPacking, seasonsNewPacking):
    archiveName = b'comp7ArchiveGriffin'
    seasonsValues = getSeasonsRecords(SEASON_KEY, seasonsNumber, ctx, seasonsPacking)
    sumSeasonsValues = getSumSeasonsValues(seasonsValues)
    valuesToArchive = prepareArchiveSeasonsRecords(sumSeasonsValues, seasonsNewPacking)
    updateStaticSizeBlockRecords(ctx, archiveName, valuesToArchive)
    clearSeasonsRecords(seasonsNumber, SEASON_KEY, ctx, seasonsPacking)
    return


def archiveMaxSeasonsGriffin(seasonsNumber, ctx, maxSeasonsPacking):
    archiveName = b'maxComp7ArchiveGriffin'
    maxSeasonsValues = getSeasonsRecords(MAX_SEASON_KEY, seasonsNumber, ctx, maxSeasonsPacking)
    maxValues = getMaxSeasonsValues(maxSeasonsValues)
    valuesToArchive = prepareArchiveSeasonsRecords(maxValues, maxSeasonsPacking)
    updateStaticSizeBlockRecords(ctx, archiveName, valuesToArchive)
    clearSeasonsRecords(seasonsNumber, MAX_SEASON_KEY, ctx, maxSeasonsPacking)
    return


def archiveCutSeasonsGriffin(seasonsNumber, ctx):
    archiveName = b'comp7CutArchiveGriffin'
    cutSeasonsValues = getCutSeasonsRecords(CUT_SEASON_KEY, seasonsNumber, ctx)
    valuesToArchive = prepareArchiveCutSeasonsRecords(cutSeasonsValues)
    updateDictRecords(ctx, archiveName, b'I', b'IIII', valuesToArchive)
    clearCutSeasonsRecords(seasonsNumber, ctx)
    return


def archiveSeasonsWolf(seasonsNumber, ctx, seasonsPacking):
    archiveName = b'comp7ArchiveGriffin'
    seasonsValues = getSeasonsRecordsWithGriffin(SEASON_KEY, seasonsNumber, ctx, seasonsPacking, archiveName)
    sumSeasonsValues = getSumSeasonsValues(seasonsValues)
    valuesToArchive = prepareArchiveSeasonsRecords(sumSeasonsValues, seasonsPacking)
    updateStaticSizeBlockRecords(ctx, archiveName, valuesToArchive)
    clearSeasonsRecords(seasonsNumber, SEASON_KEY, ctx, seasonsPacking)
    return


def archiveMaxSeasonsWolf(seasonsNumber, ctx, maxSeasonsPacking):
    archiveName = b'maxComp7ArchiveGriffin'
    maxSeasonsValues = getSeasonsRecordsWithGriffin(MAX_SEASON_KEY, seasonsNumber, ctx, maxSeasonsPacking, archiveName)
    maxValues = getMaxSeasonsValues(maxSeasonsValues)
    valuesToArchive = prepareArchiveSeasonsRecords(maxValues, maxSeasonsPacking)
    updateStaticSizeBlockRecords(ctx, archiveName, valuesToArchive)
    clearSeasonsRecords(seasonsNumber, MAX_SEASON_KEY, ctx, maxSeasonsPacking)
    return


def archiveCutSeasonsWolf(seasonsNumber, ctx):
    archiveName = b'comp7CutArchiveGriffin'
    cutSeasonsValues = getCutSeasonsRecordsWithGriffin(CUT_SEASON_KEY, seasonsNumber, ctx, archiveName)
    valuesToArchive = prepareArchiveCutSeasonsRecords(cutSeasonsValues)
    updateDictRecords(ctx, archiveName, b'I', b'IIII', valuesToArchive)
    clearCutSeasonsRecords(seasonsNumber, ctx)
    return
