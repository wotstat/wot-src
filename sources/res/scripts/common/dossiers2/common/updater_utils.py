from __future__ import absolute_import
import struct
from future.utils import viewitems, viewvalues
from past.builtins import xrange

def buildBlocksLayout(buildersLayout):
    return [builder.name for builder in buildersLayout]


def buildAllRecordsFormat(block, recordsInfo):
    return {recordInfo[1]: recordInfo[3] for recordInfo in recordsInfo if recordInfo[0] == block and recordInfo[2] == b'p'}


def buildRecordsPacking(records, layout, formats):
    offset = 0
    packing = {}
    for record in layout:
        format = formats[record]
        if record in records:
            packing[record] = (
             offset, format)
        offset += struct.calcsize(b'<' + format)

    return packing


def buildLayoutWithFormat(block, layout, recordsInfo):
    indices = dict((rec[:2], idx) for idx, rec in enumerate(recordsInfo))
    return [(record, recordsInfo[indices[block, record]][3]) for record in layout]


def getHeader(updateCtx):
    updateCtx[b'headerFormat'] = headerFormat = b'<%s%d%s' % (
     updateCtx[b'versionFormat'], len(updateCtx[b'blocksLayout']),
     updateCtx[b'blockSizeFormat'])
    updateCtx[b'headerLength'] = struct.calcsize(headerFormat)
    updateCtx[b'header'] = list(struct.unpack_from(headerFormat, updateCtx[b'dossierCompDescr']))
    return


def getStaticSizeBlockRecordValues(updateCtx, block, recordsPacking):
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    if updateCtx[b'header'][blockIndex + 1] == 0:
        return {}
    blockOffset = updateCtx[b'headerLength'] + sum(updateCtx[b'header'][1:blockIndex + 1])
    res = {}
    for record, (offset, format) in viewitems(recordsPacking):
        res[record] = struct.unpack_from(b'<' + format, updateCtx[b'dossierCompDescr'], blockOffset + offset)[0]

    return res


def getDictBlockRecordValues(updateCtx, block, keyFormat, valueFormat):
    compDescr = getBlockCompDescr(updateCtx, block)
    itemFormat = keyFormat + valueFormat
    itemSize = struct.calcsize(b'<' + itemFormat)
    length = len(compDescr) // itemSize
    keyLength = len(keyFormat)
    valueLength = len(valueFormat)
    if length == 0:
        return {}
    data = {}
    fmt = b'<' + itemFormat * length
    values = struct.unpack(fmt, compDescr)
    itemLength = len(itemFormat)
    for i in xrange(0, len(values), itemLength):
        key = values[i:i + keyLength]
        value = values[i + keyLength:i + valueLength + keyLength]
        data[key] = value

    return data


def updateDictRecords(updateCtx, block, keyFormat, valueFormat, values):
    header = updateCtx[b'header']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    blockSize = header[blockIndex + 1]
    headerLength = updateCtx[b'headerLength']
    blockOffset = headerLength + sum(header[1:blockIndex + 1])
    fmt = b'<' + (keyFormat + valueFormat) * len(values)
    writeValues = []
    for key, value in viewitems(values):
        writeValues += key + value

    blockCompDescr = struct.pack(fmt, *writeValues)
    dossierCompDescr = updateCtx[b'dossierCompDescr']
    dossierCompDescr = dossierCompDescr[:blockOffset] + blockCompDescr + dossierCompDescr[blockOffset + blockSize:]
    header[blockIndex + 1] = len(blockCompDescr)
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + dossierCompDescr[updateCtx[b'headerLength']:]
    return


def setStaticSizeBlockRecordValues(updateCtx, block, recordsPacking, recordsValues):
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    if updateCtx[b'header'][blockIndex + 1] == 0:
        return {}
    blockOffset = updateCtx[b'headerLength'] + sum(updateCtx[b'header'][1:blockIndex + 1])
    for key, value in viewitems(recordsValues):
        offset, format = recordsPacking[key]
        data = struct.pack(b'<' + format, value)
        updateCtx[b'dossierCompDescr'] = updateCtx[b'dossierCompDescr'][:blockOffset + offset] + data + updateCtx[b'dossierCompDescr'][blockOffset + offset + len(data):]

    return


def getBinarySetValue(updateCtx, block, byteNum, bitNum):
    compDescr = getBlockCompDescr(updateCtx, block)
    arraySize = len(compDescr)
    if byteNum >= arraySize:
        return False
    unpackedByte = struct.unpack_from(b'<B', compDescr, byteNum)[0]
    return bool(unpackedByte & 1 << bitNum)


def getNewStaticSizeBlockValues(layoutWithFormat, defaults):
    blockFormat = b'<' + (b'').join([format for record, format in layoutWithFormat])
    blockValues = [defaults.get(record, 0) for record, format in layoutWithFormat]
    return (blockFormat, blockValues)


def getNewBinarySetBlockValues(layout, values):
    blockValues = []
    bit = 0
    byte = 0
    for name in layout:
        bit += 1
        byte >>= 1
        byte |= 128 if bool(values.get(name, 0)) else 0
        if bit == 8:
            blockValues.append(byte)
            bit = 0
            byte = 0

    if bit > 0:
        byte >>= 8 - bit
        blockValues.append(byte)
    while len(blockValues) > 0 and blockValues[-1] == 0:
        blockValues.pop()

    blockFormat = b'<%dB' % len(blockValues)
    return (blockFormat, blockValues)


def setVersion(updateCtx, version):
    versionFormat = b'<' + updateCtx[b'versionFormat']
    versionLength = struct.calcsize(versionFormat)
    updateCtx[b'dossierCompDescr'] = struct.pack(versionFormat, version) + updateCtx[b'dossierCompDescr'][versionLength:]
    return


def addBlock(updateCtx, block, blockFormat=b'', blockValues=None):
    blockSize = struct.calcsize(blockFormat) if bool(blockFormat) else 0
    header = updateCtx[b'header']
    header.append(blockSize)
    updateCtx[b'headerFormat'] += updateCtx[b'blockSizeFormat']
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + updateCtx[b'dossierCompDescr'][updateCtx[b'headerLength']:]
    updateCtx[b'blocksLayout'].append(block)
    updateCtx[b'headerLength'] += struct.calcsize(b'<' + updateCtx[b'blockSizeFormat'])
    if blockSize != 0:
        updateCtx[b'dossierCompDescr'] += struct.pack(blockFormat, *blockValues)
    return


def removeBlock(updateCtx, block):
    header = updateCtx[b'header']
    compDescr = updateCtx[b'dossierCompDescr']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    updateCtx[b'blocksLayout'].pop(blockIndex)
    prevHeaderLength = updateCtx[b'headerLength']
    blockSize = header.pop(blockIndex + 1)
    blockOffset = prevHeaderLength + sum(header[1:blockIndex + 1])
    updateCtx[b'headerFormat'] = headerFormat = b'<%s%d%s' % (
     updateCtx[b'versionFormat'], len(updateCtx[b'blocksLayout']),
     updateCtx[b'blockSizeFormat'])
    updateCtx[b'headerLength'] = struct.calcsize(headerFormat)
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + compDescr[prevHeaderLength:blockOffset] + compDescr[blockOffset + blockSize:]
    return


def addRecords(updateCtx, block, recordFormats, defaults):
    header = updateCtx[b'header']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    blockSize = header[blockIndex + 1]
    if blockSize == 0:
        return
    blockOffset = updateCtx[b'headerLength'] + sum(header[1:blockIndex + 1])
    subBlockFormat = b'<' + (b'').join([format for record, format in recordFormats])
    subBlockValues = [defaults.get(record, 0) for record, format in recordFormats]
    dossierCompDescr = updateCtx[b'dossierCompDescr']
    dossierCompDescr = dossierCompDescr[:blockOffset + blockSize] + struct.pack(subBlockFormat, *subBlockValues) + dossierCompDescr[blockOffset + blockSize:]
    header[blockIndex + 1] += struct.calcsize(subBlockFormat)
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + dossierCompDescr[updateCtx[b'headerLength']:]
    return


def updateStaticSizeBlockRecords(updateCtx, block, records):
    header = updateCtx[b'header']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    blockSize = header[blockIndex + 1]
    if blockSize == 0 and not any(True for _, _, value in records if value != 0):
        return
    dossierCompDescr = updateCtx[b'dossierCompDescr']
    blockOffset = updateCtx[b'headerLength'] + sum(header[1:blockIndex + 1])
    blockDescr = dossierCompDescr[blockOffset:blockOffset + blockSize]
    for offset, format, value in records:
        itemSize = struct.calcsize(b'<' + format)
        if offset + itemSize > len(blockDescr):
            toExpand = offset + itemSize - len(blockDescr)
            blockDescr += b'\x00' * toExpand
        newValue = struct.pack(b'<' + format, value)
        blockDescr = blockDescr[:offset] + newValue + blockDescr[offset + itemSize:]

    dossierCompDescr = dossierCompDescr[:blockOffset] + blockDescr + dossierCompDescr[blockOffset + blockSize:]
    header[blockIndex + 1] = len(blockDescr)
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + dossierCompDescr[updateCtx[b'headerLength']:]
    return


def updateBinaryBlockRecords(updateCtx, block, records):
    header = updateCtx[b'header']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    blockSize = header[blockIndex + 1]
    dossierCompDescr = updateCtx[b'dossierCompDescr']
    blockOffset = updateCtx[b'headerLength'] + sum(header[1:blockIndex + 1])
    blockDescr = dossierCompDescr[blockOffset:blockOffset + blockSize]
    for byteNum, bitNum, value in records:
        if byteNum >= len(blockDescr):
            blockDescr += b'\x00' * (byteNum - len(blockDescr) + 1)
        unpackedByte = struct.unpack_from(b'<B', blockDescr, byteNum)[0]
        unpackedByte &= ~(1 << bitNum)
        unpackedByte |= bool(value) << bitNum
        newValue = struct.pack(b'<B', unpackedByte)
        blockDescr = blockDescr[:byteNum] + newValue + blockDescr[byteNum + 1:]

    dossierCompDescr = dossierCompDescr[:blockOffset] + blockDescr + dossierCompDescr[blockOffset + blockSize:]
    header[blockIndex + 1] = len(blockDescr)
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + dossierCompDescr[updateCtx[b'headerLength']:]
    return


def removeRecords(updateCtx, block, recordsPacking):
    header = updateCtx[b'header']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    if header[blockIndex + 1] == 0:
        return
    blockOffset = updateCtx[b'headerLength'] + sum(header[1:blockIndex + 1])
    l = [(offset, struct.calcsize(b'<' + format)) for offset, format in viewvalues(recordsPacking)]
    l.sort()
    totalSizeDec = 0
    dossierCompDescr = updateCtx[b'dossierCompDescr']
    for offset, size in l:
        dossierCompDescr = dossierCompDescr[:blockOffset + offset - totalSizeDec] + dossierCompDescr[blockOffset + offset - totalSizeDec + size:]
        totalSizeDec += size

    header[blockIndex + 1] -= totalSizeDec
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + dossierCompDescr[updateCtx[b'headerLength']:]
    return


def getBlockSize(updateCtx, block):
    header = updateCtx[b'header']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    blockSize = header[blockIndex + 1]
    return blockSize


def getBlockCompDescr(updateCtx, block):
    header = updateCtx[b'header']
    compDescr = updateCtx[b'dossierCompDescr']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    blockSize = header[blockIndex + 1]
    if blockSize == 0:
        return []
    headerLength = updateCtx[b'headerLength']
    blockOffset = headerLength + sum(header[1:blockIndex + 1])
    return compDescr[blockOffset:blockOffset + blockSize]


def setBlockCompDescr(updateCtx, block, blockCompDescr):
    header = updateCtx[b'header']
    compDescr = updateCtx[b'dossierCompDescr']
    blockIndex = updateCtx[b'blocksLayout'].index(block)
    blockSize = header[blockIndex + 1]
    headerLength = updateCtx[b'headerLength']
    blockOffset = headerLength + sum(header[1:blockIndex + 1])
    header[blockIndex + 1] = len(blockCompDescr)
    updateCtx[b'dossierCompDescr'] = struct.pack(updateCtx[b'headerFormat'], *header) + compDescr[headerLength:blockOffset] + blockCompDescr + compDescr[blockOffset + blockSize:]
    return
