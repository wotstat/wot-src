from debug_utils import LOG_WARNING

class STORE(object):
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
    RENTALTERMSELECTIONPOPOVER_TERMSLOTALLDAYS_ENUM = (
     RENTALTERMSELECTIONPOPOVER_TERMSLOT3DAYS,
     RENTALTERMSELECTIONPOPOVER_TERMSLOT7DAYS,
     RENTALTERMSELECTIONPOPOVER_TERMSLOT30DAYS)

    @classmethod
    def getRentTermDays(cls, days):
        outcome = (b'#store:rentalTermSelectionPopover/termSlot{}Days').format(days)
        if outcome not in cls.RENTALTERMSELECTIONPOPOVER_TERMSLOTALLDAYS_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
