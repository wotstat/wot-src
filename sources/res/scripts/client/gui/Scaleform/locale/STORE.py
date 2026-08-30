from debug_utils import LOG_WARNING

class STORE(object):
    BUYVEHICLEWINDOW_TITLE = b'#store:buyVehicleWindow/title'
    BUYVEHICLEWINDOW_TITLE_RESTORE = b'#store:buyVehicleWindow/title_restore'
    BUYVEHICLEWINDOW_RENT_TITLE = b'#store:buyVehicleWindow/rent/title'
    BUYVEHICLEWINDOW_SLOT_0 = b'#store:buyVehicleWindow/slot/0'
    BUYVEHICLEWINDOW_FREESLOT = b'#store:buyVehicleWindow/freeSlot'
    BUYVEHICLEWINDOW_BOOTCAMP_TOPCOMMANDERFREE = b'#store:buyVehicleWindow/bootcamp/topCommanderFree'
    BUYVEHICLEWINDOW_SLOT_1 = b'#store:buyVehicleWindow/slot/1'
    BUYVEHICLEWINDOW_SLOT_2 = b'#store:buyVehicleWindow/slot/2'
    BUYVEHICLEWINDOW_CHECKBOX_BUY_WITHOUTCREW = b'#store:buyVehicleWindow/checkBox/buy/withoutCrew'
    BUYVEHICLEWINDOW_CHECKBOX_RESTORE_WITHOUTCREW = b'#store:buyVehicleWindow/checkBox/restore/withoutCrew'
    BUYVEHICLEWINDOW_COUNTCREWLBL = b'#store:buyVehicleWindow/countCrewLbl'
    BUYVEHICLEWINDOW_EQUIPMENT_AMMO = b'#store:buyVehicleWindow/equipment/ammo'
    BUYVEHICLEWINDOW_EQUIPMENT_SLOT = b'#store:buyVehicleWindow/equipment/slot'
    BUYVEHICLEWINDOW_BUYBTN = b'#store:buyVehicleWindow/buyBtn'
    BUYVEHICLEWINDOW_RENTBTN = b'#store:buyVehicleWindow/rentBtn'
    BUYVEHICLEWINDOW_EXCHANGE = b'#store:buyVehicleWindow/exchange'
    BUYVEHICLEWINDOW_RESTORE = b'#store:buyVehicleWindow/restore'
    BUYVEHICLEWINDOW_TRADEINBTNLABEL = b'#store:buyVehicleWindow/tradeInBtnLabel'
    BUYVEHICLEWINDOW_RENTBTNLABELSEASON_EPICSEASON = b'#store:buyVehicleWindow/rentBtnLabelSeason/epicSeason'
    BUYVEHICLEWINDOW_RENTBTNLABELSEASON_EPICCYCLE = b'#store:buyVehicleWindow/rentBtnLabelSeason/epicCycle'
    BUYVEHICLEWINDOW_RENTBTNLABELSEASON_RANKEDSEASON = b'#store:buyVehicleWindow/rentBtnLabelSeason/rankedSeason'
    BUYVEHICLEWINDOW_RENTBTNLABELSEASON_RANKEDCYCLE = b'#store:buyVehicleWindow/rentBtnLabelSeason/rankedCycle'
    BUYVEHICLEWINDOW_RENTBTNLABEL3DAYS = b'#store:buyVehicleWindow/rentBtnLabel3Days'
    BUYVEHICLEWINDOW_RENTBTNLABEL7DAYS = b'#store:buyVehicleWindow/rentBtnLabel7Days'
    BUYVEHICLEWINDOW_RENTBTNLABEL30DAYS = b'#store:buyVehicleWindow/rentBtnLabel30Days'
    BUYVEHICLEWINDOW_TERMSLOTUNLIM = b'#store:buyVehicleWindow/termSlotUnlim'
    BUYVEHICLEWINDOW_RENTBTNLABELANY = b'#store:buyVehicleWindow/rentBtnLabelAny'
    BUYVEHICLEWINDOW_TOGGLEBTN_RENT = b'#store:buyVehicleWindow/toggleBtn/rent'
    BUYVEHICLEWINDOW_TOGGLEBTN_BUY = b'#store:buyVehicleWindow/toggleBtn/buy'
    BUYVEHICLEWINDOW_CREWINVEHICLE = b'#store:buyVehicleWindow/crewInVehicle'
    SELLCONFIRMATIONPOPOVER_TITLELABEL = b'#store:sellConfirmationPopover/titleLabel'
    SELLCONFIRMATIONPOPOVER_PRICELABEL = b'#store:sellConfirmationPopover/priceLabel'
    RENTALTERMSELECTIONPOPOVER_TITLELABEL = b'#store:rentalTermSelectionPopover/titleLabel'
    RENTALTERMSELECTIONPOPOVER_TERMSLOT3DAYS = b'#store:rentalTermSelectionPopover/termSlot3Days'
    RENTALTERMSELECTIONPOPOVER_TERMSLOT7DAYS = b'#store:rentalTermSelectionPopover/termSlot7Days'
    RENTALTERMSELECTIONPOPOVER_TERMSLOT30DAYS = b'#store:rentalTermSelectionPopover/termSlot30Days'
    RENTALTERMSELECTIONPOPOVER_TERMSLOTANY = b'#store:rentalTermSelectionPopover/termSlotAny'
    RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_EPICSEASON = b'#store:rentalTermSelectionPopover/termSlotSeason/epicSeason'
    RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_EPICCYCLE = b'#store:rentalTermSelectionPopover/termSlotSeason/epicCycle'
    RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_RANKEDSEASON = b'#store:rentalTermSelectionPopover/termSlotSeason/rankedSeason'
    RENTALTERMSELECTIONPOPOVER_TERMSLOTSEASON_RANKEDCYCLE = b'#store:rentalTermSelectionPopover/termSlotSeason/rankedCycle'
    RENTALTERMSELECTIONPOPOVER_TERMSLOTUNLIM = b'#store:rentalTermSelectionPopover/termSlotUnlim'
    CONGRATULATIONANIM_BUYINGLABEL = b'#store:congratulationAnim/buyingLabel'
    CONGRATULATIONANIM_DESCRIPTIONLABEL_STYLE = b'#store:congratulationAnim/descriptionLabel/style'
    CONGRATULATIONANIM_CONFIRMLABEL = b'#store:congratulationAnim/confirmLabel'
    CONGRATULATIONANIM_BACKLABEL = b'#store:congratulationAnim/backLabel'
    CONGRATULATIONANIM_COLLECTIBLELABEL = b'#store:congratulationAnim/collectibleLabel'
    CONGRATULATIONANIM_RESTORELABEL = b'#store:congratulationAnim/restoreLabel'
    CONGRATULATIONANIM_SHOWPREVIEWBTNLABEL = b'#store:congratulationAnim/showPreviewBtnLabel'
    BUYVEHICLEWINDOW_SLOT_ENUM = (
     BUYVEHICLEWINDOW_SLOT_0,
     BUYVEHICLEWINDOW_SLOT_1,
     BUYVEHICLEWINDOW_SLOT_2)
    RENTALTERMSELECTIONPOPOVER_TERMSLOTALLDAYS_ENUM = (
     RENTALTERMSELECTIONPOPOVER_TERMSLOT3DAYS,
     RENTALTERMSELECTIONPOPOVER_TERMSLOT7DAYS,
     RENTALTERMSELECTIONPOPOVER_TERMSLOT30DAYS)

    @classmethod
    def getBuyVehicleSlotTitle(cls, key0):
        outcome = (b'#store:buyVehicleWindow/slot/{}').format(key0)
        if outcome not in cls.BUYVEHICLEWINDOW_SLOT_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getRentTermDays(cls, days):
        outcome = (b'#store:rentalTermSelectionPopover/termSlot{}Days').format(days)
        if outcome not in cls.RENTALTERMSELECTIONPOPOVER_TERMSLOTALLDAYS_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
