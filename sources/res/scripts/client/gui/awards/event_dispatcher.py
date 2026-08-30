import gui.awards.special_achievement_awards as specialAwards
from gui.shared.event_dispatcher import showAwardWindow
from gui.impl.lobby.reward_window import DynamicRewardWindow

def showBoosterAward(booster):
    showAwardWindow(specialAwards.BoosterAward(booster))
    return


def showClanJoinAward(clanAbbrev, clanName, clanDbID):
    showAwardWindow(specialAwards.ClanJoinAward(clanAbbrev, clanName, clanDbID))
    return


def showTelecomAward(vehicleDesrs, bundleID, hasCrew, hasBrotherhood):
    showAwardWindow(specialAwards.TelecomAward(vehicleDesrs, bundleID, hasCrew, hasBrotherhood))
    return


def showRecruiterAward():
    showAwardWindow(specialAwards.RecruiterAward())
    return


def showDynamicAward(eventName, bonuses):
    window = DynamicRewardWindow({b'eventName': eventName, b'bonuses': bonuses})
    window.load()
    return


def showVehicleCollectorAward(nationID):
    showAwardWindow(specialAwards.VehicleCollectorAward(nationID))
    return


def showVehicleCollectorOfEverythingAward(*args):
    showAwardWindow(specialAwards.VehicleCollectorOfEverythingAward())
    return
