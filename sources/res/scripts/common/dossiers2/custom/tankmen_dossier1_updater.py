from __future__ import absolute_import
import dossiers2, struct
__TANKMAN_LAYOUT_10 = [
 3, 
 4, 5, 6, 
 7, 8, 9, 10, 11, 12, 13, 
 14, 15, 16, 17, 18, 
 19, 20, 
 21, 22, 23, 24, 25, 
 26, 27, 28, 29, 
 30, 31, 32, 
 33, 
 34, 35, 
 36, 37, 38, 39, 40, 41, 42, 
 43, 44, 45, 46, 
 47, 48, 
 49, 50, 51, 52, 53, 54, 
 55, 56, 57, 58, 
 59, 60, 
 61, 62, 63, 
 64, 65, 66, 67]
__TANKMAN_LAYOUT_11 = [
 3, 
 9, 
 36, 37, 38, 39, 40, 41, 42, 68, 
 51, 52, 53, 54, 
 55, 
 56, 57, 58, 
 69, 70, 71, 
 72, 73, 74]
__TANKMAN_LAYOUT_12 = [
 3, 
 9, 
 36, 37, 38, 39, 40, 41, 42, 68, 
 51, 52, 53, 54, 
 55, 
 56, 57, 58, 75, 
 76, 77, 78, 79, 80, 
 81, 82]
__TANKMAN_LAYOUT_13 = [
 3, 
 9, 
 36, 37, 38, 39, 40, 41, 42, 68, 
 51, 52, 53, 54, 
 55, 
 56, 57, 58, 75, 
 76, 77, 78, 79, 80, 
 81, 82, 83]
__TANKMAN_LAYOUT_14 = [
 3, 
 9, 
 36, 37, 38, 39, 40, 41, 42, 68, 
 51, 52, 53, 54, 
 55, 
 56, 57, 58, 75, 
 76, 77, 78, 79, 80, 
 81, 82, 83, 84, 
 71]
__RECORD_PACKING_10 = {b'spotted': (b'I', 4, 4000000001L), 
   b'medalCarius': (b'B', 1, 4), 
   b'medalHalonen': (b'B', 1, 201), 
   b'invader': (b'H', 2, 60001), 
   b'medalFadin': (b'B', 1, 201), 
   b'armorPiercer': (b'B', 1, 1), 
   b'damageReceived': (b'I', 4, 4000000001L), 
   b'sniperSeries': (b'H', 2, 60001), 
   b'battleLifeTime': (b'I', 4, 4000000001L), 
   b'battleHeroes': (b'H', 2, 60001), 
   b'medalOskin': (b'B', 1, 201), 
   b'droppedCapturePoints': (b'I', 4, 4000000001L), 
   b'defender': (b'H', 2, 60001), 
   b'xp': (b'I', 4, 4000000001L), 
   b'medalLeClerc': (b'B', 1, 4), 
   b'invincibleSeries': (b'B', 1, 201), 
   b'supporter': (b'H', 2, 60001), 
   b'maxInvincibleSeries': (b'B', 1, 201), 
   b'steelwall': (b'H', 2, 60001), 
   b'medalAbrams': (b'B', 1, 4), 
   b'maxFrags': (b'B', 1, 201), 
   b'fragsBeast': (b'I', 4, 4000000001L), 
   b'maxDiehardSeries': (b'B', 1, 201), 
   b'winAndSurvived': (b'I', 4, 4000000001L), 
   b'killingSeries': (b'B', 1, 201), 
   b'lastBattleTime': (b'I', 4, 4000000001L), 
   b'piercingSeries': (b'B', 1, 201), 
   b'diehard': (b'B', 1, 1), 
   b'maxSniperSeries': (b'H', 2, 60001), 
   b'medalKay': (b'B', 1, 4), 
   b'medalEkins': (b'B', 1, 4), 
   b'handOfDeath': (b'B', 1, 1), 
   b'frags': (b'I', 4, 4000000001L), 
   b'sniper': (b'H', 2, 60001), 
   b'medalPoppel': (b'B', 1, 4), 
   b'warrior': (b'H', 2, 60001), 
   b'titleSniper': (b'B', 1, 1), 
   b'treesCut': (b'H', 2, 60001), 
   b'maxXP': (b'H', 2, 60001), 
   b'medalWittmann': (b'B', 1, 201), 
   b'survivedBattles': (b'I', 4, 4000000001L), 
   b'medalBurda': (b'B', 1, 201), 
   b'maxPiercingSeries': (b'B', 1, 201), 
   b'battlesCount': (b'I', 4, 4000000001L), 
   b'scout': (b'H', 2, 60001), 
   b'beasthunter': (b'B', 1, 1), 
   b'kamikaze': (b'B', 1, 201), 
   b'raider': (b'B', 1, 201), 
   b'diehardSeries': (b'B', 1, 201), 
   b'medalBillotte': (b'B', 1, 201), 
   b'medalLavrinenko': (b'B', 1, 4), 
   b'medalKolobanov': (b'B', 1, 201), 
   b'wins': (b'I', 4, 4000000001L), 
   b'lumberjack': (b'B', 1, 1), 
   b'losses': (b'I', 4, 4000000001L), 
   b'damageDealt': (b'I', 4, 4000000001L), 
   b'_version': (b'H', 2, 32767), 
   b'medalKnispel': (b'B', 1, 4), 
   b'medalOrlik': (b'B', 1, 201), 
   b'maxKillingSeries': (b'B', 1, 201), 
   b'shots': (b'I', 4, 4000000001L), 
   b'invincible': (b'B', 1, 1), 
   b'frags8p': (b'I', 4, 4000000001L), 
   b'capturePoints': (b'I', 4, 4000000001L), 
   b'directHits': (b'I', 4, 4000000001L)}
__RECORD_PACKING_11 = {b'medalFadin': (b'H', 2, 60001), 
   b'defender': (b'H', 2, 60001), 
   b'supporter': (b'H', 2, 60001), 
   b'sniper': (b'H', 2, 60001), 
   b'medalHoroshilov': (b'H', 2, 60001), 
   b'scout': (b'H', 2, 60001), 
   b'medalKolobanov': (b'H', 2, 60001), 
   b'invader': (b'H', 2, 60001), 
   b'warrior': (b'H', 2, 60001), 
   b'medalWittmann': (b'H', 2, 60001), 
   b'medalBillotte': (b'H', 2, 60001), 
   b'_version': (b'H', 2, 32767), 
   b'evileye': (b'H', 2, 60001), 
   b'medalHalonen': (b'H', 2, 60001), 
   b'steelwall': (b'H', 2, 60001), 
   b'medalDeLaglanda': (b'H', 2, 60001), 
   b'battlesCount': (b'I', 4, 4000000001L), 
   b'medalOskin': (b'H', 2, 60001), 
   b'medalTamadaYoshio': (b'H', 2, 60001), 
   b'medalErohin': (b'H', 2, 60001), 
   b'medalOrlik': (b'H', 2, 60001), 
   b'medalBurda': (b'H', 2, 60001), 
   b'medalLister': (b'H', 2, 60001), 
   b'medalHeroesOfRassenai': (b'H', 2, 60001)}
__RECORD_PACKING_12 = {b'medalFadin': (b'H', 2, 60001), 
   b'defender': (b'H', 2, 60001), 
   b'supporter': (b'H', 2, 60001), 
   b'medalLehvaslaiho': (b'H', 2, 60001), 
   b'medalPascucci': (b'H', 2, 60001), 
   b'sniper': (b'H', 2, 60001), 
   b'scout': (b'H', 2, 60001), 
   b'medalKolobanov': (b'H', 2, 60001), 
   b'medalLafayettePool': (b'H', 2, 60001), 
   b'invader': (b'H', 2, 60001), 
   b'warrior': (b'H', 2, 60001), 
   b'medalWittmann': (b'H', 2, 60001), 
   b'medalRadleyWalters': (b'H', 2, 60001), 
   b'medalBillotte': (b'H', 2, 60001), 
   b'_version': (b'H', 2, 32767), 
   b'evileye': (b'H', 2, 60001), 
   b'medalHalonen': (b'H', 2, 60001), 
   b'steelwall': (b'H', 2, 60001), 
   b'medalTarczay': (b'H', 2, 60001), 
   b'battlesCount': (b'I', 4, 4000000001L), 
   b'medalOskin': (b'H', 2, 60001), 
   b'medalDumitru': (b'H', 2, 60001), 
   b'medalBrunoPietro': (b'H', 2, 60001), 
   b'medalOrlik': (b'H', 2, 60001), 
   b'medalBurda': (b'H', 2, 60001), 
   b'medalNikolas': (b'H', 2, 60001)}
__RECORD_PACKING_13 = {b'medalFadin': (b'H', 2, 60001), 
   b'heroesOfRassenay': (b'H', 2, 60001), 
   b'defender': (b'H', 2, 60001), 
   b'supporter': (b'H', 2, 60001), 
   b'medalLehvaslaiho': (b'H', 2, 60001), 
   b'medalPascucci': (b'H', 2, 60001), 
   b'sniper': (b'H', 2, 60001), 
   b'scout': (b'H', 2, 60001), 
   b'medalKolobanov': (b'H', 2, 60001), 
   b'medalLafayettePool': (b'H', 2, 60001), 
   b'invader': (b'H', 2, 60001), 
   b'warrior': (b'H', 2, 60001), 
   b'medalWittmann': (b'H', 2, 60001), 
   b'medalRadleyWalters': (b'H', 2, 60001), 
   b'medalBillotte': (b'H', 2, 60001), 
   b'_version': (b'H', 2, 32767), 
   b'evileye': (b'H', 2, 60001), 
   b'medalHalonen': (b'H', 2, 60001), 
   b'steelwall': (b'H', 2, 60001), 
   b'medalTarczay': (b'H', 2, 60001), 
   b'battlesCount': (b'I', 4, 4000000001L), 
   b'medalOskin': (b'H', 2, 60001), 
   b'medalDumitru': (b'H', 2, 60001), 
   b'medalBrunoPietro': (b'H', 2, 60001), 
   b'medalOrlik': (b'H', 2, 60001), 
   b'medalBurda': (b'H', 2, 60001), 
   b'medalNikolas': (b'H', 2, 60001)}
__RECORD_PACKING_14 = {b'medalHalonen': (b'H', 2, 60001), 
   b'medalFadin': (b'H', 2, 60001), 
   b'heroesOfRassenay': (b'H', 2, 60001), 
   b'defender': (b'H', 2, 60001), 
   b'supporter': (b'H', 2, 60001), 
   b'steelwall': (b'H', 2, 60001), 
   b'medalLehvaslaiho': (b'H', 2, 60001), 
   b'medalPascucci': (b'H', 2, 60001), 
   b'medalTarczay': (b'H', 2, 60001), 
   b'sniper': (b'H', 2, 60001), 
   b'battlesCount': (b'I', 4, 4000000001L), 
   b'scout': (b'H', 2, 60001), 
   b'medalOskin': (b'H', 2, 60001), 
   b'medalKolobanov': (b'H', 2, 60001), 
   b'medalLafayettePool': (b'H', 2, 60001), 
   b'medalOrlik': (b'H', 2, 60001), 
   b'medalDumitru': (b'H', 2, 60001), 
   b'invader': (b'H', 2, 60001), 
   b'medalBrunoPietro': (b'H', 2, 60001), 
   b'medalRadleyWalters': (b'H', 2, 60001), 
   b'medalDeLanglade': (b'H', 2, 60001), 
   b'medalTamadaYoshio': (b'H', 2, 60001), 
   b'warrior': (b'H', 2, 60001), 
   b'medalWittmann': (b'H', 2, 60001), 
   b'medalBurda': (b'H', 2, 60001), 
   b'medalNikolas': (b'H', 2, 60001), 
   b'medalBillotte': (b'H', 2, 60001), 
   b'_version': (b'H', 2, 32767), 
   b'evileye': (b'H', 2, 60001)}

def __getVersion(compDescr):
    return struct.unpack(b'<H', compDescr[0:2])[0]


def __buildRecordsFmt(recordsLayout, recordPackings):
    fmt = b'<'
    for record in recordsLayout:
        packing = recordPackings[record]
        fmt += packing[0]

    return fmt


def updateDossierCompDescr(compDescr):
    data = {}
    verDescr = __getVersion(compDescr)
    recordsLayout = __TANKMAN_LAYOUT_14
    record_packing = __RECORD_PACKING_14
    if verDescr == 10:
        recordsLayout = __TANKMAN_LAYOUT_10
        record_packing = __RECORD_PACKING_10
    elif verDescr == 11:
        recordsLayout = __TANKMAN_LAYOUT_11
        record_packing = __RECORD_PACKING_11
    elif verDescr == 12:
        recordsLayout = __TANKMAN_LAYOUT_12
        record_packing = __RECORD_PACKING_12
    elif verDescr == 13:
        recordsLayout = __TANKMAN_LAYOUT_13
        record_packing = __RECORD_PACKING_13
    fmt = __buildRecordsFmt(recordsLayout, record_packing)
    values = struct.unpack(fmt, compDescr)
    for index, record in enumerate(recordsLayout):
        data[record] = values[index]

    d2 = dossiers2.getTankmanDossierDescr()
    total = d2.expand(b'total')
    total.eventsEnabled = False
    total[b'battlesCount'] = data[b'battlesCount']
    achievements = d2.expand(b'achievements')
    achievements.eventsEnabled = False
    for record in [8, 9, 10, 11, 12, 13, 14, 
     15, 16, 17, 18, 19, 20, 
     21, 
     22, 23, 24, 
     25, 26, 27, 28, 29, 
     30, 31, 
     32, 33, 
     34]:
        achievements[record] = data.get(record, 0)

    return d2.makeCompDescr()
