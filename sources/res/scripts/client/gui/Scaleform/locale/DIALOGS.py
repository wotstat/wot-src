from debug_utils import LOG_WARNING

class DIALOGS(object):
    GATHERINGXPFORM_SORTBY_VEHICLE = b'#dialogs:gatheringXPForm/sortBy/vehicle'
    GATHERINGXPFORM_SORTBY_XP = b'#dialogs:gatheringXPForm/sortBy/xp'
    GRAPHICSPRESETNOTINSTALLED = b'#dialogs:graphicsPresetNotInstalled'
    GATHERINGXPFORM_SORTBY_SELECTION = b'#dialogs:gatheringXPForm/sortBy/selection'
    TRADEINPOPOVER_SORTING_NATION = b'#dialogs:tradeInPopover/sorting/nation'
    TRADEINPOPOVER_SORTING_VEHTYPE = b'#dialogs:tradeInPopover/sorting/vehType'
    TRADEINPOPOVER_SORTING_VEHLVL = b'#dialogs:tradeInPopover/sorting/vehLvl'
    TRADEINPOPOVER_SORTING_VEHNAME = b'#dialogs:tradeInPopover/sorting/vehName'
    TRADEINPOPOVER_SORTING_SAVING = b'#dialogs:tradeInPopover/sorting/saving'
    MINIMAPALPHANOTIFICATION = b'#dialogs:minimapAlphaNotification'
    SOUNDMODEINVALID = b'#dialogs:soundModeInvalid'
    CONTROLSWRONGNOTIFICATION = b'#dialogs:controlsWrongNotification'
    HOF_EXCLUDERATING = b'#dialogs:hof/excludeRating'
    INTERVIEWQUIT_TITLE = b'#dialogs:interviewQuit/title'
    INTERVIEWQUIT_MESSAGE = b'#dialogs:interviewQuit/message'
    INTERVIEWQUIT_SUBMIT = b'#dialogs:interviewQuit/submit'
    INTERVIEWQUIT_CANCEL = b'#dialogs:interviewQuit/cancel'
    SURVEYQUIT_TITLE = b'#dialogs:surveyQuit/title'
    SURVEYQUIT_MESSAGE = b'#dialogs:surveyQuit/message'
    SURVEYQUIT_SUBMIT = b'#dialogs:surveyQuit/submit'
    SURVEYQUIT_CANCEL = b'#dialogs:surveyQuit/cancel'
    APPLICATIONQUIT_TITLE = b'#dialogs:applicationQuit/title'
    APPLICATIONQUIT_MESSAGE = b'#dialogs:applicationQuit/message'
    APPLICATIONQUIT_SUBMIT = b'#dialogs:applicationQuit/submit'
    APPLICATIONQUIT_CANCEL = b'#dialogs:applicationQuit/cancel'
    LEGALINFOWINDOW_TITLE = b'#dialogs:legalInfoWindow/title'
    COMMON_SUBMIT = b'#dialogs:common/submit'
    COMMON_CANCEL = b'#dialogs:common/cancel'
    COMMON_CONFIRM_SUBMIT = b'#dialogs:common/confirm/submit'
    COMMON_CONFIRM_CANCEL = b'#dialogs:common/confirm/cancel'
    COMMON_ERROR_CANCEL = b'#dialogs:common/error/cancel'
    COMMON_COST = b'#dialogs:common/cost'
    DISCONNECT_TITLE = b'#dialogs:disconnect/title'
    DISCONNECT_MESSAGE = b'#dialogs:disconnect/message'
    DISCONNECT_SUBMIT = b'#dialogs:disconnect/submit'
    DISCONNECT_CANCEL = b'#dialogs:disconnect/cancel'
    QUIT_TITLE = b'#dialogs:quit/title'
    QUIT_SUBMIT = b'#dialogs:quit/submit'
    QUIT_CANCEL = b'#dialogs:quit/cancel'
    QUITBATTLE_TITLE = b'#dialogs:quitBattle/title'
    QUITBATTLE_SUBMIT = b'#dialogs:quitBattle/submit'
    QUITBATTLE_CANCEL = b'#dialogs:quitBattle/cancel'
    QUITBATTLE_LEAVER_TITLE = b'#dialogs:quitBattle/leaver/title'
    QUITBATTLE_LEAVER_SUBMIT = b'#dialogs:quitBattle/leaver/submit'
    QUITBATTLE_LEAVER_CANCEL = b'#dialogs:quitBattle/leaver/cancel'
    QUITBATTLE_LEAVER_DESCRIPTIONALIVE = b'#dialogs:quitBattle/leaver/descriptionAlive'
    QUITBATTLE_IGR_LEAVER_TITLE = b'#dialogs:quitBattle/IGR/leaver/title'
    QUITBATTLE_IGR_LEAVER_SUBMIT = b'#dialogs:quitBattle/IGR/leaver/submit'
    QUITBATTLE_IGR_LEAVER_CANCEL = b'#dialogs:quitBattle/IGR/leaver/cancel'
    QUITBATTLE_IGR_LEAVER_DESCRIPTIONALIVE = b'#dialogs:quitBattle/IGR/leaver/descriptionAlive'
    QUITBATTLE_REPLAY_TITLE = b'#dialogs:quitBattle/replay/title'
    QUITBATTLE_REPLAY_SUBMIT = b'#dialogs:quitBattle/replay/submit'
    QUITBATTLE_REPLAY_CANCEL = b'#dialogs:quitBattle/replay/cancel'
    QUITPREBATTLE_TITLE = b'#dialogs:quitPreBattle/title'
    QUITPREBATTLE_MESSAGE = b'#dialogs:quitPreBattle/message'
    QUITPREBATTLE_SUBMIT = b'#dialogs:quitPreBattle/submit'
    QUITPREBATTLE_CANCEL = b'#dialogs:quitPreBattle/cancel'
    GRAPHICSPRESETRESTARTCONFIRMATION_TITLE = b'#dialogs:graphicsPresetRestartConfirmation/title'
    GRAPHICSPRESETRESTARTCONFIRMATION_MESSAGE = b'#dialogs:graphicsPresetRestartConfirmation/message'
    GRAPHICSPRESETRESTARTCONFIRMATION_SUBMIT = b'#dialogs:graphicsPresetRestartConfirmation/submit'
    GRAPHICSPRESETRESTARTCONFIRMATION_DELAY = b'#dialogs:graphicsPresetRestartConfirmation/delay'
    GRAPHICSPRESETRESTARTCONFIRMATION_CANCEL = b'#dialogs:graphicsPresetRestartConfirmation/cancel'
    GRAPHICSPRESETNOTINSTALLED_TITLE = b'#dialogs:graphicsPresetNotInstalled/title'
    GRAPHICSPRESETNOTINSTALLED_MESSAGE = b'#dialogs:graphicsPresetNotInstalled/message'
    GRAPHICSPRESETNOTINSTALLED_CANCEL = b'#dialogs:graphicsPresetNotInstalled/cancel'
    GRAPHICSPRESETDELAYEDCONFIRMATION_TITLE = b'#dialogs:graphicsPresetDelayedConfirmation/title'
    GRAPHICSPRESETDELAYEDCONFIRMATION_MESSAGE = b'#dialogs:graphicsPresetDelayedConfirmation/message'
    GRAPHICSPRESETDELAYEDCONFIRMATION_SUBMIT = b'#dialogs:graphicsPresetDelayedConfirmation/submit'
    GRAPHICSPRESETDELAYEDCONFIRMATION_CANCEL = b'#dialogs:graphicsPresetDelayedConfirmation/cancel'
    NEXTBATTLEOPTIONCONFIRMATION_TITLE = b'#dialogs:nextBattleOptionConfirmation/title'
    NEXTBATTLEOPTIONCONFIRMATION_MESSAGE = b'#dialogs:nextBattleOptionConfirmation/message'
    NEXTBATTLEOPTIONCONFIRMATION_SUBMIT = b'#dialogs:nextBattleOptionConfirmation/submit'
    NEXTBATTLEOPTIONCONFIRMATION_CANCEL = b'#dialogs:nextBattleOptionConfirmation/cancel'
    GRAPHICSPRESETAUTODETECTCONFIRMATION_TITLE = b'#dialogs:graphicsPresetAutodetectConfirmation/title'
    GRAPHICSPRESETAUTODETECTCONFIRMATION_MESSAGE = b'#dialogs:graphicsPresetAutodetectConfirmation/message'
    GRAPHICSPRESETAUTODETECTCONFIRMATION_SUBMIT = b'#dialogs:graphicsPresetAutodetectConfirmation/submit'
    GRAPHICSPRESETAUTODETECTCONFIRMATION_CANCEL = b'#dialogs:graphicsPresetAutodetectConfirmation/cancel'
    GRAPHICSPRESETNOTPOSSIBLE_TITLE = b'#dialogs:graphicsPresetNotPossible/title'
    GRAPHICSPRESETNOTPOSSIBLE_MESSAGE = b'#dialogs:graphicsPresetNotPossible/message'
    GRAPHICSPRESETNOTPOSSIBLE_CANCEL = b'#dialogs:graphicsPresetNotPossible/cancel'
    GRAPHICSCHANGECONFIRMATION_TITLE = b'#dialogs:graphicsChangeConfirmation/title'
    GRAPHICSCHANGECONFIRMATION_MESSAGE = b'#dialogs:graphicsChangeConfirmation/message'
    GRAPHICSCHANGECONFIRMATION_SUBMIT = b'#dialogs:graphicsChangeConfirmation/submit'
    GRAPHICSCHANGECONFIRMATION_CANCEL = b'#dialogs:graphicsChangeConfirmation/cancel'
    WATERQUALITYNOTPOSSIBLE_TITLE = b'#dialogs:waterQualityNotPossible/title'
    WATERQUALITYNOTPOSSIBLE_MESSAGE = b'#dialogs:waterQualityNotPossible/message'
    WATERQUALITYNOTPOSSIBLE_CANCEL = b'#dialogs:waterQualityNotPossible/cancel'
    PREMIUMBUYCONFIRMATION_TITLE = b'#dialogs:premiumBuyConfirmation/title'
    PREMIUMBUYCONFIRMATION_MESSAGE = b'#dialogs:premiumBuyConfirmation/message'
    PREMIUMBUYCONFIRMATION_SUBMIT = b'#dialogs:premiumBuyConfirmation/submit'
    PREMIUMBUYCONFIRMATION_CANCEL = b'#dialogs:premiumBuyConfirmation/cancel'
    PREMIUMCONTINUECONFIRMATION_TITLE = b'#dialogs:premiumContinueConfirmation/title'
    PREMIUMCONTINUECONFIRMATION_MESSAGE = b'#dialogs:premiumContinueConfirmation/message'
    PREMIUMCONTINUECONFIRMATION_SUBMIT = b'#dialogs:premiumContinueConfirmation/submit'
    PREMIUMCONTINUECONFIRMATION_CANCEL = b'#dialogs:premiumContinueConfirmation/cancel'
    BUYPREMWITHOUTBENEFITSCONFIRMATION_TITLE = b'#dialogs:buyPremWithoutBenefitsConfirmation/title'
    BUYPREMWITHOUTBENEFITSCONFIRMATION_MESSAGE = b'#dialogs:buyPremWithoutBenefitsConfirmation/message'
    BUYPREMWITHOUTBENEFITSCONFIRMATION_SUBMIT = b'#dialogs:buyPremWithoutBenefitsConfirmation/submit'
    BUYPREMWITHOUTBENEFITSCONFIRMATION_CANCEL = b'#dialogs:buyPremWithoutBenefitsConfirmation/cancel'
    BUYINSTALLCONFIRMATION_TITLE = b'#dialogs:buyInstallConfirmation/title'
    BUYINSTALLCONFIRMATION_MESSAGECOMBINE = b'#dialogs:buyInstallConfirmation/messageCombine'
    BUYINSTALLCONFIRMATION_MESSAGE = b'#dialogs:buyInstallConfirmation/message'
    BUYINSTALLCONFIRMATION_CONFLICTEDMESSAGE_PREFIX = b'#dialogs:buyInstallConfirmation/conflictedMessage/prefix'
    BUYINSTALLCONFIRMATION_CONFLICTEDMESSAGE_HIGHLIGHTENTEXT = b'#dialogs:buyInstallConfirmation/conflictedMessage/highlightenText'
    BUYINSTALLCONFIRMATION_CONFLICTEDMESSAGE_POSTFIX = b'#dialogs:buyInstallConfirmation/conflictedMessage/postfix'
    BUYINSTALLCONFIRMATION_SUBMIT = b'#dialogs:buyInstallConfirmation/submit'
    BUYINSTALLCONFIRMATION_CANCEL = b'#dialogs:buyInstallConfirmation/cancel'
    REMOVECONFIRMATIONNOTREMOVABLE_SUBMIT = b'#dialogs:removeConfirmationNotRemovable/submit'
    SELLCONFIRMATION_SUBMIT = b'#dialogs:sellConfirmation/submit'
    SELLCONFIRMATION_CANCEL = b'#dialogs:sellConfirmation/cancel'
    SELLMODULECONFIRMATION_TITLE = b'#dialogs:sellModuleConfirmation/title'
    SELLMODULECONFIRMATION_SUBMIT = b'#dialogs:sellModuleConfirmation/submit'
    SELLMODULECONFIRMATION_CANCEL = b'#dialogs:sellModuleConfirmation/cancel'
    CONFIRMMODULEDIALOG_PRICELABEL = b'#dialogs:confirmModuleDialog/priceLabel'
    CONFIRMMODULEDIALOG_COUNTLABEL = b'#dialogs:confirmModuleDialog/countLabel'
    CONFIRMMODULEDIALOG_TOTALLABEL = b'#dialogs:confirmModuleDialog/totalLabel'
    CONFIRMMODULEDIALOG_COUNTLABEL1 = b'#dialogs:confirmModuleDialog/countLabel1'
    CONFIRMMODULEDIALOG_PRICELABEL1 = b'#dialogs:confirmModuleDialog/priceLabel1'
    CONFIRMMODULEDIALOG_SHOP_TOTALLABEL1 = b'#dialogs:confirmModuleDialog/shop/totalLabel1'
    CONFIRMMODULEDIALOG_INVENTORY_TOTALLABEL1 = b'#dialogs:confirmModuleDialog/inventory/totalLabel1'
    CONFIRMMODULEDIALOG_REZULTLABEL1 = b'#dialogs:confirmModuleDialog/rezultLabel1'
    RENTCONFIRMATION_TITLE = b'#dialogs:rentConfirmation/title'
    RENTCONFIRMATION_MESSAGE = b'#dialogs:rentConfirmation/message'
    RENTCONFIRMATION_SUBMIT = b'#dialogs:rentConfirmation/submit'
    RENTCONFIRMATION_CANCEL = b'#dialogs:rentConfirmation/cancel'
    RENTCONFIRMATION_EVENT = b'#dialogs:rentConfirmation/event'
    RENTCONFIRMATIONRENEW_TITLE = b'#dialogs:rentConfirmationRenew/title'
    RENTCONFIRMATIONRENEW_MESSAGE = b'#dialogs:rentConfirmationRenew/message'
    RENTCONFIRMATIONRENEW_SUBMIT = b'#dialogs:rentConfirmationRenew/submit'
    RENTCONFIRMATIONRENEW_CANCEL = b'#dialogs:rentConfirmationRenew/cancel'
    BUYCONFIRMATION_TITLE = b'#dialogs:buyConfirmation/title'
    BUYCONFIRMATION_MESSAGECOMBINE = b'#dialogs:buyConfirmation/messageCombine'
    BUYCONFIRMATION_MESSAGE = b'#dialogs:buyConfirmation/message'
    BUYCONFIRMATION_SUBMIT = b'#dialogs:buyConfirmation/submit'
    BUYCONFIRMATION_CANCEL = b'#dialogs:buyConfirmation/cancel'
    IDLECREWBONUS_TITLE = b'#dialogs:idleCrewBonus/title'
    IDLECREWBONUS_MESSAGE_REMOVETYPE = b'#dialogs:idleCrewBonus/message/removeType'
    IDLECREWBONUS_MESSAGE_REMOVENAME = b'#dialogs:idleCrewBonus/message/removeName'
    IDLECREWBONUS_MESSAGE_CREWWARNING = b'#dialogs:idleCrewBonus/message/crewWarning'
    IDLECREWBONUS_MESSAGE_CREWINCOMPLETE = b'#dialogs:idleCrewBonus/message/crewIncomplete'
    IDLECREWBONUS_MESSAGE_CREWUNSUITABLE = b'#dialogs:idleCrewBonus/message/crewUnsuitable'
    IDLECREWBONUS_SUBMIT = b'#dialogs:idleCrewBonus/submit'
    IDLECREWBONUS_CANCEL = b'#dialogs:idleCrewBonus/cancel'
    WOTPLUSRENTAL_TITLE = b'#dialogs:wotPlusRental/title'
    WOTPLUSRENTAL_DESCRIPTION = b'#dialogs:wotPlusRental/description'
    WOTPLUSRENTAL_SUBMIT = b'#dialogs:wotPlusRental/submit'
    WOTPLUSRENTAL_CANCEL = b'#dialogs:wotPlusRental/cancel'
    DISCONNECTED_TITLE = b'#dialogs:disconnected/title'
    DISCONNECTED_MESSAGE = b'#dialogs:disconnected/message'
    DISCONNECTED_MESSAGEKICK = b'#dialogs:disconnected/messageKick'
    DISCONNECTED_MESSAGEBAN = b'#dialogs:disconnected/messageBan'
    DISCONNECTED_MESSAGEBANPERIOD = b'#dialogs:disconnected/messageBanPeriod'
    DISCONNECTED_REASON = b'#dialogs:disconnected/reason'
    DISCONNECTED_CANCEL = b'#dialogs:disconnected/cancel'
    LOWAMMO_TITLE = b'#dialogs:lowAmmo/title'
    LOWAMMO_MESSAGE = b'#dialogs:lowAmmo/message'
    LOWAMMO_SUBMIT = b'#dialogs:lowAmmo/submit'
    LOWAMMO_CANCEL = b'#dialogs:lowAmmo/cancel'
    LOWAMMOAUTOLOAD_TITLE = b'#dialogs:lowAmmoAutoLoad/title'
    LOWAMMOAUTOLOAD_MESSAGE = b'#dialogs:lowAmmoAutoLoad/message'
    LOWALTERNATIVEAMMOAUTOLOAD_TITLE = b'#dialogs:lowAlternativeAmmoAutoLoad/title'
    LOWALTERNATIVEAMMOAUTOLOAD_MESSAGE = b'#dialogs:lowAlternativeAmmoAutoLoad/message'
    LOWAMMOAUTOLOAD_SUBMIT = b'#dialogs:lowAmmoAutoLoad/submit'
    LOWAMMOAUTOLOAD_CANCEL = b'#dialogs:lowAmmoAutoLoad/cancel'
    BUYSLOTCONFIRMATION_TITLE = b'#dialogs:buySlotConfirmation/title'
    BUYSLOTCONFIRMATION_MESSAGE = b'#dialogs:buySlotConfirmation/message'
    BUYSLOTCONFIRMATION_SUBMIT = b'#dialogs:buySlotConfirmation/submit'
    BUYSLOTCONFIRMATION_CANCEL = b'#dialogs:buySlotConfirmation/cancel'
    FREESLOTCONFIRMATION_TITLE = b'#dialogs:freeSlotConfirmation/title'
    FREESLOTCONFIRMATION_MESSAGE = b'#dialogs:freeSlotConfirmation/message'
    FREESLOTCONFIRMATION_SUBMIT = b'#dialogs:freeSlotConfirmation/submit'
    FREESLOTCONFIRMATION_CANCEL = b'#dialogs:freeSlotConfirmation/cancel'
    REPLACEPASSPORT_UNIQUE_TITLE = b'#dialogs:replacePassport/unique/title'
    REPLACEPASSPORT_UNIQUE_MESSAGE = b'#dialogs:replacePassport/unique/message'
    REPLACEPASSPORT_UNIQUE_SUBMIT = b'#dialogs:replacePassport/unique/submit'
    REPLACEPASSPORT_UNIQUE_CANCEL = b'#dialogs:replacePassport/unique/cancel'
    REPLACEPASSPORTCONFIRMATION_TITLE = b'#dialogs:replacePassportConfirmation/title'
    REPLACEPASSPORTCONFIRMATION_MESSAGE = b'#dialogs:replacePassportConfirmation/message'
    REPLACEPASSPORTCONFIRMATION_SUBMIT = b'#dialogs:replacePassportConfirmation/submit'
    REPLACEPASSPORTCONFIRMATION_CANCEL = b'#dialogs:replacePassportConfirmation/cancel'
    BUYSLOT_HANGARSLOT_HEADER = b'#dialogs:buySlot/hangarSlot/header'
    BUYSLOTSHOPCONFIRMATION_TITLE = b'#dialogs:buySlotShopConfirmation/title'
    BUYSLOTSHOPCONFIRMATION_MESSAGECOMBINE = b'#dialogs:buySlotShopConfirmation/messageCombine'
    BUYSLOTSHOPCONFIRMATION_SUBMIT = b'#dialogs:buySlotShopConfirmation/submit'
    BUYSLOTSHOPCONFIRMATION_CANCEL = b'#dialogs:buySlotShopConfirmation/cancel'
    UPGRADETANKMANSCOOLCONFIRMATION_TITLE = b'#dialogs:upgradeTankmanScoolConfirmation/title'
    UPGRADETANKMANSCOOLCONFIRMATION_MESSAGECOMBINE = b'#dialogs:upgradeTankmanScoolConfirmation/messageCombine'
    UPGRADETANKMANSCOOLCONFIRMATION_SUBMIT = b'#dialogs:upgradeTankmanScoolConfirmation/submit'
    UPGRADETANKMANSCOOLCONFIRMATION_CANCEL = b'#dialogs:upgradeTankmanScoolConfirmation/cancel'
    UPGRADETANKMANACADEMYCONFIRMATION_TITLE = b'#dialogs:upgradeTankmanAcademyConfirmation/title'
    UPGRADETANKMANACADEMYCONFIRMATION_MESSAGECOMBINE = b'#dialogs:upgradeTankmanAcademyConfirmation/messageCombine'
    UPGRADETANKMANACADEMYCONFIRMATION_SUBMIT = b'#dialogs:upgradeTankmanAcademyConfirmation/submit'
    UPGRADETANKMANACADEMYCONFIRMATION_CANCEL = b'#dialogs:upgradeTankmanAcademyConfirmation/cancel'
    UPGRADETANKMANSCOOLNOTENOUGHMONEY_TITLE = b'#dialogs:upgradeTankmanScoolNotEnoughMoney/title'
    UPGRADETANKMANSCOOLNOTENOUGHMONEY_MESSAGE = b'#dialogs:upgradeTankmanScoolNotEnoughMoney/message'
    UPGRADETANKMANSCOOLNOTENOUGHMONEY_SUBMIT = b'#dialogs:upgradeTankmanScoolNotEnoughMoney/submit'
    UPGRADETANKMANSCOOLNOTENOUGHMONEY_CANCEL = b'#dialogs:upgradeTankmanScoolNotEnoughMoney/cancel'
    UPGRADETANKMANACADEMYNOTENOUGHMONEY_TITLE = b'#dialogs:upgradeTankmanAcademyNotEnoughMoney/title'
    UPGRADETANKMANACADEMYNOTENOUGHMONEY_MESSAGE = b'#dialogs:upgradeTankmanAcademyNotEnoughMoney/message'
    UPGRADETANKMANACADEMYNOTENOUGHMONEY_SUBMIT = b'#dialogs:upgradeTankmanAcademyNotEnoughMoney/submit'
    UPGRADETANKMANACADEMYNOTENOUGHMONEY_CANCEL = b'#dialogs:upgradeTankmanAcademyNotEnoughMoney/cancel'
    RECRUITDIALOG_TITLE = b'#dialogs:recruitDialog/title'
    RECRUITDIALOG_NAME_TITLE = b'#dialogs:recruitDialog/name/title'
    RECRUITWINDOW_NATION = b'#dialogs:recruitWindow/nation'
    RECRUITWINDOW_SPECIALIZATION = b'#dialogs:recruitWindow/specialization'
    RECRUITWINDOW_VEHICLECLASS = b'#dialogs:recruitWindow/vehicleClass'
    RECRUITWINDOW_VEHICLETYPE = b'#dialogs:recruitWindow/vehicleType'
    RECRUITWINDOW_MENUEMPTYROW = b'#dialogs:recruitWindow/menuEmptyRow'
    RECRUITWINDOW_SUBMIT = b'#dialogs:recruitWindow/submit'
    RECRUITWINDOW_CANCEL = b'#dialogs:recruitWindow/cancel'
    BUYSLOTNOTENOUGH_CREDITS_TITLE = b'#dialogs:buySlotNotEnough/credits/title'
    BUYSLOTNOTENOUGH_CREDITS_MESSAGE = b'#dialogs:buySlotNotEnough/credits/message'
    BUYSLOTNOTENOUGH_CREDITS_SUBMIT = b'#dialogs:buySlotNotEnough/credits/submit'
    BUYSLOTNOTENOUGH_CREDITS_CANCEL = b'#dialogs:buySlotNotEnough/credits/cancel'
    BUYSLOTNOTENOUGH_GOLD_TITLE = b'#dialogs:buySlotNotEnough/gold/title'
    BUYSLOTNOTENOUGH_GOLD_MESSAGE = b'#dialogs:buySlotNotEnough/gold/message'
    BUYSLOTNOTENOUGH_GOLD_SUBMIT = b'#dialogs:buySlotNotEnough/gold/submit'
    BUYSLOTNOTENOUGH_GOLD_CANCEL = b'#dialogs:buySlotNotEnough/gold/cancel'
    BUYVEHICLEWINDOW_TITLE = b'#dialogs:buyVehicleWindow/title'
    BUYVEHICLEWINDOW_TRADEIN_TITLE = b'#dialogs:buyVehicleWindow/tradein/title'
    BUYVEHICLEWINDOW_TRADEIN_PRICELABEL = b'#dialogs:buyVehicleWindow/tradein/priceLabel'
    BUYVEHICLEWINDOW_PRICELABEL = b'#dialogs:buyVehicleWindow/priceLabel'
    BUYVEHICLEWINDOW_SUBMITBTN = b'#dialogs:buyVehicleWindow/submitBtn'
    BUYVEHICLEWINDOW_TRADEIN_SUBMITBTN = b'#dialogs:buyVehicleWindow/tradein/submitBtn'
    BUYVEHICLEWINDOW_CANCELBTN = b'#dialogs:buyVehicleWindow/cancelBtn'
    BUYVEHICLEWINDOW_TRADEIN_CANCELBTN = b'#dialogs:buyVehicleWindow/tradein/cancelBtn'
    BUYVEHICLEWINDOW_WARNING = b'#dialogs:buyVehicleWindow/warning'
    BUYVEHICLEWINDOW_TRADEIN_WARNING = b'#dialogs:buyVehicleWindow/tradein/warning'
    BUYVEHICLEWINDOW_FREERENTSLOT = b'#dialogs:buyVehicleWindow/freeRentSlot'
    BUYVEHICLEWINDOW_FULLAMMO = b'#dialogs:buyVehicleWindow/fullAmmo'
    BUYVEHICLEWINDOW_TANKMENCHECKBOX = b'#dialogs:buyVehicleWindow/tankmenCheckbox'
    BUYVEHICLEWINDOW_TRADEIN_TANKMENCHECKBOX = b'#dialogs:buyVehicleWindow/tradein/tankmenCheckbox'
    BUYVEHICLEWINDOW_TANKMENLABEL = b'#dialogs:buyVehicleWindow/tankmenLabel'
    BUYVEHICLEWINDOW_TANKMENTOTALLABEL = b'#dialogs:buyVehicleWindow/tankmenTotalLabel'
    BUYVEHICLEWINDOW_SLOTCHECKBOX = b'#dialogs:buyVehicleWindow/slotCheckbox'
    BUYVEHICLEWINDOW_AMMOCHECKBOX = b'#dialogs:buyVehicleWindow/ammoCheckbox'
    BUYVEHICLEWINDOW_CREWINVEHICLE = b'#dialogs:buyVehicleWindow/crewInVehicle'
    BUYVEHICLEWINDOW_TOTALLABEL = b'#dialogs:buyVehicleWindow/totalLabel'
    BUYVEHICLEWINDOW_TABS_BUY = b'#dialogs:buyVehicleWindow/tabs/buy'
    BUYVEHICLEWINDOW_TABS_TRADE = b'#dialogs:buyVehicleWindow/tabs/trade'
    BUYVEHICLEWINDOW_TRADEIN_STUDYLABEL = b'#dialogs:buyVehicleWindow/tradeIn/studyLabel'
    BUYVEHICLEWINDOW_TRADEIN_TOTALLABEL = b'#dialogs:buyVehicleWindow/tradeIn/totalLabel'
    BUYVEHICLEWINDOW_TRADEIN_CONFIRMATION_TITLE = b'#dialogs:buyVehicleWindow/tradeIn/confirmation/title'
    BUYVEHICLEWINDOW_TRADEIN_CONFIRMATION_QUESTION = b'#dialogs:buyVehicleWindow/tradeIn/confirmation/question'
    BUYVEHICLEWINDOW_TRADEIN_CONFIRMATION_ERRORMESSAGE = b'#dialogs:buyVehicleWindow/tradeIn/confirmation/errorMessage'
    BUYVEHICLEWINDOW_TRADEIN_INFO_NOVEHICLES = b'#dialogs:buyVehicleWindow/tradeIn/info/noVehicles'
    BUYVEHICLEWINDOW_TRADEIN_WARNING_CHOOSE = b'#dialogs:buyVehicleWindow/tradeIn/warning/choose'
    BUYVEHICLEWINDOW_TRADEIN_INFO_SAVING = b'#dialogs:buyVehicleWindow/tradeIn/info/saving'
    BUYVEHICLEWINDOW_TRADEIN_VEHICLE_CHOOSE = b'#dialogs:buyVehicleWindow/tradeIn/vehicle/choose'
    TRADEINPOPOVER_DESCR = b'#dialogs:tradeInPopover/descr'
    TRADEINPOPOVER_TITLE = b'#dialogs:tradeInPopover/title'
    TRADEINPOPOVER_SORTING_NATION_HEADER = b'#dialogs:tradeInPopover/sorting/nation/header'
    TRADEINPOPOVER_SORTING_NATION_BODY = b'#dialogs:tradeInPopover/sorting/nation/body'
    TRADEINPOPOVER_SORTING_VEHTYPE_HEADER = b'#dialogs:tradeInPopover/sorting/vehType/header'
    TRADEINPOPOVER_SORTING_VEHTYPE_BODY = b'#dialogs:tradeInPopover/sorting/vehType/body'
    TRADEINPOPOVER_SORTING_VEHLVL_HEADER = b'#dialogs:tradeInPopover/sorting/vehLvl/header'
    TRADEINPOPOVER_SORTING_VEHLVL_BODY = b'#dialogs:tradeInPopover/sorting/vehLvl/body'
    TRADEINPOPOVER_SORTING_VEHNAME_HEADER = b'#dialogs:tradeInPopover/sorting/vehName/header'
    TRADEINPOPOVER_SORTING_VEHNAME_BODY = b'#dialogs:tradeInPopover/sorting/vehName/body'
    TRADEINPOPOVER_SORTING_SAVING_FORMATTED = b'#dialogs:tradeInPopover/sorting/saving/formatted'
    TRADEINPOPOVER_SORTING_SAVING_HEADER = b'#dialogs:tradeInPopover/sorting/saving/header'
    TRADEINPOPOVER_SORTING_SAVING_BODY = b'#dialogs:tradeInPopover/sorting/saving/body'
    TRADEOFFWIDGET_SELECTVEHICLE = b'#dialogs:tradeOffWidget/selectVehicle'
    RESTOREEQUIPMENT_HEADER = b'#dialogs:restoreEquipment/header'
    RESTOREEQUIPMENT_TEXT = b'#dialogs:restoreEquipment/text'
    RESTOREEQUIPMENT_BUTTON_RESTORE = b'#dialogs:restoreEquipment/button/restore'
    RESTOREEQUIPMENT_BUTTON_CANCEL = b'#dialogs:restoreEquipment/button/cancel'
    RESTOREVEHICLEDIALOG_TITLE = b'#dialogs:restoreVehicleDialog/title'
    RESTOREVEHICLEDIALOG_PRICELABEL = b'#dialogs:restoreVehicleDialog/priceLabel'
    RESTOREVEHICLEDIALOG_TANKMENCHECKBOX = b'#dialogs:restoreVehicleDialog/tankmenCheckbox'
    RESTOREVEHICLEDIALOG_SUBMITBTN = b'#dialogs:restoreVehicleDialog/submitBtn'
    RESTOREVEHICLEDIALOG_CANCELBTN = b'#dialogs:restoreVehicleDialog/cancelBtn'
    RESTOREVEHICLEDIALOG_WARNING = b'#dialogs:restoreVehicleDialog/warning'
    BARRACKSEXPAND_TITLE = b'#dialogs:barracksExpand/title'
    BARRACKSEXPAND_MESSAGE = b'#dialogs:barracksExpand/message'
    BARRACKSEXPAND_SUBMIT = b'#dialogs:barracksExpand/submit'
    BARRACKSEXPAND_CANCEL = b'#dialogs:barracksExpand/cancel'
    BARRACKSEXPANDNOTENOUGHMONEY_TITLE = b'#dialogs:barracksExpandNotEnoughMoney/title'
    BARRACKSEXPANDNOTENOUGHMONEY_MESSAGE = b'#dialogs:barracksExpandNotEnoughMoney/message'
    BARRACKSEXPANDNOTENOUGHMONEY_SUBMIT = b'#dialogs:barracksExpandNotEnoughMoney/submit'
    BARRACKSEXPANDNOTENOUGHMONEY_CANCEL = b'#dialogs:barracksExpandNotEnoughMoney/cancel'
    EULA_P1 = b'#dialogs:eula/p1'
    EULA_P2 = b'#dialogs:eula/p2'
    CONFIRMUNLOCK_TITLE = b'#dialogs:confirmUnlock/title'
    CONFIRMUNLOCK_ITEM_MESSAGE = b'#dialogs:confirmUnlock/item/message'
    CONFIRMUNLOCK_VEHICLE_MESSAGE = b'#dialogs:confirmUnlock/vehicle/message'
    CONFIRMUNLOCK_SUBMIT = b'#dialogs:confirmUnlock/submit'
    CONFIRMUNLOCK_CANCEL = b'#dialogs:confirmUnlock/cancel'
    CONFIRMBUY_TITLE = b'#dialogs:confirmBuy/title'
    CONFIRMBUYANDINSTALL_TITLE = b'#dialogs:confirmBuyAndInstall/title'
    CONFIRMBUYANDINSTALL_MESSAGE = b'#dialogs:confirmBuyAndInstall/message'
    CONFIRMBUYANDINSTALL_SELLMESSAGE = b'#dialogs:confirmBuyAndInstall/sellMessage'
    CONFIRMBUYANDINSTALL_DEPOTMESSAGE = b'#dialogs:confirmBuyAndInstall/depotMessage'
    CONFIRMBUYANDINSTALL_SOLDMODULEINFO_DESCRIPTION = b'#dialogs:confirmBuyAndInstall/soldModuleInfo/description'
    CONFIRMBUYANDINSTALL_SOLDMODULEINFO_COMPATIBLETANKS = b'#dialogs:confirmBuyAndInstall/soldModuleInfo/compatibleTanks'
    CONFIRMBUYANDINSTALL_INSUFFICIENTFUNDSTOOLTIP_HEADER = b'#dialogs:confirmBuyAndInstall/insufficientFundsTooltip/header'
    CONFIRMBUYANDINSTALL_INSUFFICIENTFUNDSTOOLTIP_BODY = b'#dialogs:confirmBuyAndInstall/insufficientFundsTooltip/body'
    CONFIRMBUYANDINSTALL_INSUFFICIENTFUNDSTOOLTIP_AMOUNT = b'#dialogs:confirmBuyAndInstall/insufficientFundsTooltip/amount'
    CONFIRMBUYANDINSTALL_SUBMIT = b'#dialogs:confirmBuyAndInstall/submit'
    CONFIRMBUYANDINSTALL_CANCEL = b'#dialogs:confirmBuyAndInstall/cancel'
    POSTMORTEM_TITLE = b'#dialogs:postmortem/title'
    POSTMORTEM_MESSAGE = b'#dialogs:postmortem/message'
    POSTMORTEM_SUBMIT = b'#dialogs:postmortem/submit'
    POSTMORTEM_CANCEL = b'#dialogs:postmortem/cancel'
    DISMISSEDBUFFEROVERFLAW_TITLE = b'#dialogs:dismissedBufferOverFlaw/title'
    DISMISSEDBUFFEROVERFLAW_MESSAGE = b'#dialogs:dismissedBufferOverFlaw/message'
    DISMISSEDBUFFEROVERFLAW_SUBMIT = b'#dialogs:dismissedBufferOverFlaw/submit'
    DISMISSEDBUFFEROVERFLAW_CANCEL = b'#dialogs:dismissedBufferOverFlaw/cancel'
    DISMISSEDBUFFEROVERFLAWMULTIPLE_TITLE = b'#dialogs:dismissedBufferOverFlawMultiple/title'
    DISMISSEDBUFFEROVERFLAWMULTIPLE_MESSAGE = b'#dialogs:dismissedBufferOverFlawMultiple/message'
    DISMISSEDBUFFEROVERFLAWMULTIPLE_SUBMIT = b'#dialogs:dismissedBufferOverFlawMultiple/submit'
    DISMISSEDBUFFEROVERFLAWMULTIPLE_CANCEL = b'#dialogs:dismissedBufferOverFlawMultiple/cancel'
    DROPSKILL_TITLE = b'#dialogs:dropSkill/title'
    DROPSKILL_MESSAGE = b'#dialogs:dropSkill/message'
    DROPSKILL_SUBMIT = b'#dialogs:dropSkill/submit'
    DROPSKILL_CANCEL = b'#dialogs:dropSkill/cancel'
    SQUADPREMIUMNEEDED_TITLE = b'#dialogs:squadPremiumNeeded/title'
    SQUADPREMIUMNEEDED_MESSAGE = b'#dialogs:squadPremiumNeeded/message'
    SQUADPREMIUMNEEDED_CANCEL = b'#dialogs:squadPremiumNeeded/cancel'
    SQUADHAVENOTREADYPLAYERS_TITLE = b'#dialogs:squadHaveNotReadyPlayers/title'
    SQUADHAVENOTREADYPLAYERS_MESSAGE = b'#dialogs:squadHaveNotReadyPlayers/message'
    SQUADHAVENOTREADYPLAYERS_SUBMIT = b'#dialogs:squadHaveNotReadyPlayers/submit'
    SQUADHAVENOTREADYPLAYERS_CANCEL = b'#dialogs:squadHaveNotReadyPlayers/cancel'
    SQUADHAVENOTREADYPLAYERSAUTO_TITLE = b'#dialogs:squadHaveNotReadyPlayersAuto/title'
    SQUADHAVENOTREADYPLAYERSAUTO_MESSAGE = b'#dialogs:squadHaveNotReadyPlayersAuto/message'
    SQUADHAVENOTREADYPLAYERSAUTO_SUBMIT = b'#dialogs:squadHaveNotReadyPlayersAuto/submit'
    SQUADHAVENOTREADYPLAYERSAUTO_CANCEL = b'#dialogs:squadHaveNotReadyPlayersAuto/cancel'
    SQUADHAVENOTREADYPLAYERAUTO_TITLE = b'#dialogs:squadHaveNotReadyPlayerAuto/title'
    SQUADHAVENOTREADYPLAYERAUTO_MESSAGE = b'#dialogs:squadHaveNotReadyPlayerAuto/message'
    SQUADHAVENOTREADYPLAYERAUTO_SUBMIT = b'#dialogs:squadHaveNotReadyPlayerAuto/submit'
    SQUADHAVENOTREADYPLAYERAUTO_CANCEL = b'#dialogs:squadHaveNotReadyPlayerAuto/cancel'
    SQUADHAVENOTREADYPLAYER_TITLE = b'#dialogs:squadHaveNotReadyPlayer/title'
    SQUADHAVENOTREADYPLAYER_MESSAGE = b'#dialogs:squadHaveNotReadyPlayer/message'
    SQUADHAVENOTREADYPLAYER_SUBMIT = b'#dialogs:squadHaveNotReadyPlayer/submit'
    SQUADHAVENOTREADYPLAYER_CANCEL = b'#dialogs:squadHaveNotReadyPlayer/cancel'
    SQUADHAVENOPLAYERS_TITLE = b'#dialogs:squadHaveNoPlayers/title'
    SQUADHAVENOPLAYERS_MESSAGE = b'#dialogs:squadHaveNoPlayers/message'
    SQUADHAVENOPLAYERS_SUBMIT = b'#dialogs:squadHaveNoPlayers/submit'
    SQUADHAVENOPLAYERS_CANCEL = b'#dialogs:squadHaveNoPlayers/cancel'
    SQUADHAVENOPLAYERSAUTO_TITLE = b'#dialogs:squadHaveNoPlayersAuto/title'
    SQUADHAVENOPLAYERSAUTO_MESSAGE = b'#dialogs:squadHaveNoPlayersAuto/message'
    SQUADHAVENOPLAYERSAUTO_SUBMIT = b'#dialogs:squadHaveNoPlayersAuto/submit'
    SQUADHAVENOPLAYERSAUTO_CANCEL = b'#dialogs:squadHaveNoPlayersAuto/cancel'
    SQUADHAVENOPLAYERAUTO_TITLE = b'#dialogs:squadHaveNoPlayerAuto/title'
    SQUADHAVENOPLAYERAUTO_MESSAGE = b'#dialogs:squadHaveNoPlayerAuto/message'
    SQUADHAVENOPLAYERAUTO_SUBMIT = b'#dialogs:squadHaveNoPlayerAuto/submit'
    SQUADHAVENOPLAYERAUTO_CANCEL = b'#dialogs:squadHaveNoPlayerAuto/cancel'
    SQUADHAVEPLAYERSINBATTLE_TITLE = b'#dialogs:squadHavePlayersInBattle/title'
    SQUADHAVEPLAYERSINBATTLE_MESSAGE = b'#dialogs:squadHavePlayersInBattle/message'
    SQUADHAVEPLAYERSINBATTLE_SUBMIT = b'#dialogs:squadHavePlayersInBattle/submit'
    LEFTPREBATTLEANDACCEPTINVITE_TITLE = b'#dialogs:leftPrebattleAndAcceptInvite/title'
    LEFTPREBATTLEANDACCEPTINVITE_MESSAGE = b'#dialogs:leftPrebattleAndAcceptInvite/message'
    LEFTPREBATTLEANDACCEPTINVITE_SUBMIT = b'#dialogs:leftPrebattleAndAcceptInvite/submit'
    LEFTPREBATTLEANDACCEPTINVITE_CANCEL = b'#dialogs:leftPrebattleAndAcceptInvite/cancel'
    LEFTTRAININGANDACCEPTINVITE_TITLE = b'#dialogs:leftTrainingAndAcceptInvite/title'
    LEFTTRAININGANDACCEPTINVITE_MESSAGE = b'#dialogs:leftTrainingAndAcceptInvite/message'
    LEFTTRAININGANDACCEPTINVITE_SUBMIT = b'#dialogs:leftTrainingAndAcceptInvite/submit'
    LEFTTRAININGANDACCEPTINVITE_CANCEL = b'#dialogs:leftTrainingAndAcceptInvite/cancel'
    LEFTSQUADANDACCEPTINVITE_TITLE = b'#dialogs:leftSquadAndAcceptInvite/title'
    LEFTSQUADANDACCEPTINVITE_MESSAGE = b'#dialogs:leftSquadAndAcceptInvite/message'
    LEFTSQUADANDACCEPTINVITE_SUBMIT = b'#dialogs:leftSquadAndAcceptInvite/submit'
    LEFTSQUADANDACCEPTINVITE_CANCEL = b'#dialogs:leftSquadAndAcceptInvite/cancel'
    GATHERINGXPFORM_TITLE = b'#dialogs:gatheringXPForm/title'
    GATHERINGXPFORM_BEFOREOPERATION = b'#dialogs:gatheringXPForm/beforeOperation'
    GATHERINGXPFORM_CURRENTAMOUNT = b'#dialogs:gatheringXPForm/currentAmount'
    GATHERINGXPFORM_AFTEROPERATION = b'#dialogs:gatheringXPForm/afterOperation'
    GATHERINGXPFORM_HEADERBUTTONS_VEHICLE = b'#dialogs:gatheringXPForm/headerButtons/vehicle'
    GATHERINGXPFORM_HEADERBUTTONS_XP = b'#dialogs:gatheringXPForm/headerButtons/xp'
    GATHERINGXPFORM_HEADERBUTTONS_CREW = b'#dialogs:gatheringXPForm/headerButtons/crew'
    GATHERINGXPFORM_TOCHANGELABEL = b'#dialogs:gatheringXPForm/toChangeLabel'
    GATHERINGXPFORM_TOTALLABEL = b'#dialogs:gatheringXPForm/totalLabel'
    GATHERINGXPFORM_SELECTALLLABEL = b'#dialogs:gatheringXPForm/selectAllLabel'
    GATHERINGXPFORM_TOTALXP = b'#dialogs:gatheringXPForm/totalXP'
    GATHERINGXPFORM_SORTBY_SELECTION_HEADER = b'#dialogs:gatheringXPForm/sortBy/selection/header'
    GATHERINGXPFORM_SORTBY_SELECTION_BODY = b'#dialogs:gatheringXPForm/sortBy/selection/body'
    GATHERINGXPFORM_SORTBY_VEHICLE_HEADER = b'#dialogs:gatheringXPForm/sortBy/vehicle/header'
    GATHERINGXPFORM_SORTBY_VEHICLE_BODY = b'#dialogs:gatheringXPForm/sortBy/vehicle/body'
    GATHERINGXPFORM_SORTBY_XP_HEADER = b'#dialogs:gatheringXPForm/sortBy/xp/header'
    GATHERINGXPFORM_SORTBY_XP_BODY = b'#dialogs:gatheringXPForm/sortBy/xp/body'
    EXCHANGEXPWINDOW_ERROR_NOELITEVEHICLEINHANGAR = b'#dialogs:exchangeXpWindow/error/noEliteVehicleInHangar'
    EXCHANGEXPWINDOW_ERROR_NOVEHICLESWITHXP = b'#dialogs:exchangeXpWindow/error/noVehiclesWithXp'
    GATHERINGXPFORM_TOOLTIPS_CHECKBOXCREWSELECTED = b'#dialogs:gatheringXPForm/tooltips/checkboxCrewSelected'
    GATHERINGXPFORM_TOOLTIPS_CHECKBOXCREWUNSELECTED = b'#dialogs:gatheringXPForm/tooltips/checkboxCrewUnselected'
    GATHERINGXPFORM_BTNSUBMIT = b'#dialogs:gatheringXPForm/btnSubmit'
    GATHERINGXPFORM_BTNCANCEL = b'#dialogs:gatheringXPForm/btnCancel'
    EXCHANGEXPCONFIRMATION_TITLE = b'#dialogs:exchangeXPConfirmation/title'
    EXCHANGEXPCONFIRMATION_MESSAGE = b'#dialogs:exchangeXPConfirmation/message'
    EXCHANGEXPCONFIRMATION_AVAILABLE_FORFREE_MESSAGE = b'#dialogs:exchangeXPConfirmation/available/forFree/message'
    EXCHANGEXPCONFIRMATION_SUBMIT = b'#dialogs:exchangeXPConfirmation/submit'
    EXCHANGEXPCONFIRMATION_CANCEL = b'#dialogs:exchangeXPConfirmation/cancel'
    EXCHANGEGOLDCONFIRMATION_TITLE = b'#dialogs:exchangeGoldConfirmation/title'
    EXCHANGEGOLDCONFIRMATION_MESSAGE = b'#dialogs:exchangeGoldConfirmation/message'
    EXCHANGEGOLDCONFIRMATION_SUBMIT = b'#dialogs:exchangeGoldConfirmation/submit'
    EXCHANGEGOLDCONFIRMATION_CANCEL = b'#dialogs:exchangeGoldConfirmation/cancel'
    CONTROLSWRONGNOTIFICATION_TITLE = b'#dialogs:controlsWrongNotification/title'
    CONTROLSWRONGNOTIFICATION_MESSAGE = b'#dialogs:controlsWrongNotification/message'
    CONTROLSWRONGNOTIFICATION_SUBMIT = b'#dialogs:controlsWrongNotification/submit'
    CONTROLSWRONGNOTIFICATION_CANCEL = b'#dialogs:controlsWrongNotification/cancel'
    MINIMAPALPHANOTIFICATION_TITLE = b'#dialogs:minimapAlphaNotification/title'
    MINIMAPALPHANOTIFICATION_MESSAGE = b'#dialogs:minimapAlphaNotification/message'
    MINIMAPALPHANOTIFICATION_MESSAGE_ALERT = b'#dialogs:minimapAlphaNotification/message/alert'
    MINIMAPALPHANOTIFICATION_SUBMIT = b'#dialogs:minimapAlphaNotification/submit'
    MINIMAPALPHANOTIFICATION_CANCEL = b'#dialogs:minimapAlphaNotification/cancel'
    LIMITEDUIOFFNOTIFICATION_TITLE = b'#dialogs:limitedUIOffNotification/title'
    LIMITEDUIOFFNOTIFICATION_MESSAGE = b'#dialogs:limitedUIOffNotification/message'
    LIMITEDUIOFFNOTIFICATION_MESSAGE_ALERT = b'#dialogs:limitedUIOffNotification/message/alert'
    LIMITEDUIOFFNOTIFICATION_SUBMIT = b'#dialogs:limitedUIOffNotification/submit'
    LIMITEDUIOFFNOTIFICATION_CANCEL = b'#dialogs:limitedUIOffNotification/cancel'
    SOUNDMODEINVALID_TITLE = b'#dialogs:soundModeInvalid/title'
    SOUNDMODEINVALID_MESSAGE = b'#dialogs:soundModeInvalid/message'
    SOUNDMODEINVALID_SUBMIT = b'#dialogs:soundModeInvalid/submit'
    SOUNDMODEINVALID_CANCEL = b'#dialogs:soundModeInvalid/cancel'
    CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_TITLE = b'#dialogs:controlsWrongNotificationsoundModeInvalid/title'
    CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_MESSAGE = b'#dialogs:controlsWrongNotificationsoundModeInvalid/message'
    CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_SUBMIT = b'#dialogs:controlsWrongNotificationsoundModeInvalid/submit'
    CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_CANCEL = b'#dialogs:controlsWrongNotificationsoundModeInvalid/cancel'
    EULA_TITLE = b'#dialogs:EULA/title'
    EULA_LABELS_AGREE = b'#dialogs:EULA/labels/agree'
    EULA_BUTTONS_APPLY = b'#dialogs:EULA/buttons/apply'
    HAVENOEMPTYSLOTS_TITLE = b'#dialogs:haveNoEmptySlots/title'
    HAVENOEMPTYSLOTS_MESSAGE = b'#dialogs:haveNoEmptySlots/message'
    HAVENOEMPTYSLOTS_SUBMIT = b'#dialogs:haveNoEmptySlots/submit'
    HAVENOEMPTYSLOTS_CANCEL = b'#dialogs:haveNoEmptySlots/cancel'
    MONEYTRANSFER_TITLE = b'#dialogs:moneyTransfer/title'
    MONEYTRANSFER_LABELTOTALPRICE = b'#dialogs:moneyTransfer/labelTotalPrice'
    MONEYTRANSFER_LABELTO = b'#dialogs:moneyTransfer/labelTo'
    MONEYTRANSFER_LABELGOLD = b'#dialogs:moneyTransfer/labelGold'
    MONEYTRANSFER_NOT_A_CLAN = b'#dialogs:moneyTransfer/not_a_clan'
    MONEYTRANSFER_LABELFEEPRICE = b'#dialogs:moneyTransfer/labelFeePrice'
    MONEYTRANSFER_LABELNORMAL = b'#dialogs:moneyTransfer/labelNormal'
    MONEYTRANSFER_LABELNORMALCREDITS = b'#dialogs:moneyTransfer/labelNormalCredits'
    MONEYTRANSFER_LABELNORMALGOLD = b'#dialogs:moneyTransfer/labelNormalGold'
    MONEYTRANSFER_LABELCLAN = b'#dialogs:moneyTransfer/labelClan'
    MONEYTRANSFER_LABELCLANCREDITS = b'#dialogs:moneyTransfer/labelClanCredits'
    MONEYTRANSFER_LABELCLANGOLD = b'#dialogs:moneyTransfer/labelClanGold'
    MONEYTRANSFER_SUBMITBTN = b'#dialogs:moneyTransfer/submitBtn'
    MONEYTRANSFER_CANCELBTN = b'#dialogs:moneyTransfer/cancelBtn'
    MONEYTRANSFERCONFIRMATION_TITLE = b'#dialogs:moneyTransferConfirmation/title'
    MONEYTRANSFERCONFIRMATION_MESSAGE = b'#dialogs:moneyTransferConfirmation/message'
    MONEYTRANSFERCONFIRMATION_SUBMIT = b'#dialogs:moneyTransferConfirmation/submit'
    MONEYTRANSFERCONFIRMATION_CANCEL = b'#dialogs:moneyTransferConfirmation/cancel'
    MONEYTRANSFERRESTRICTION_TITLE = b'#dialogs:moneyTransferRestriction/title'
    MONEYTRANSFERRESTRICTION_MESSAGE = b'#dialogs:moneyTransferRestriction/message'
    MONEYTRANSFERRESTRICTION_MESSAGE_EXPIRY = b'#dialogs:moneyTransferRestriction/message_expiry'
    MONEYTRANSFERRESTRICTION_SUBMIT = b'#dialogs:moneyTransferRestriction/submit'
    MONEYTRANSFERRESTRICTION_CANCEL = b'#dialogs:moneyTransferRestriction/cancel'
    MONEYTRANSFERLINK_SET_PASSWORD = b'#dialogs:moneyTransferLink/set_password'
    FINANCE_DIALOG_HEADER = b'#dialogs:finance_dialog/header'
    FINANCE_DIALOG_SUBMITBTN = b'#dialogs:finance_dialog/submitBtn'
    FINANCE_DIALOG_CANCELBTN = b'#dialogs:finance_dialog/cancelBtn'
    FINANCE_DIALOG_RESULTS_DEFAULTMESSAGE = b'#dialogs:finance_dialog/results/defaultMessage'
    FINANCE_DIALOG_RESULTS_VALID = b'#dialogs:finance_dialog/results/valid'
    FINANCE_DIALOG_RESULTS_INVALID = b'#dialogs:finance_dialog/results/invalid'
    FINANCE_DIALOG_RESULTS_LIMIT = b'#dialogs:finance_dialog/results/limit'
    FINANCE_DIALOG_RESULTS_WRONG = b'#dialogs:finance_dialog/results/wrong'
    FREEVEHICLELEFTLIMIT_TITLE = b'#dialogs:freeVehicleLeftLimit/title'
    FREEVEHICLELEFTLIMIT_MESSAGE = b'#dialogs:freeVehicleLeftLimit/message'
    FREEVEHICLELEFTLIMIT_CANCEL = b'#dialogs:freeVehicleLeftLimit/cancel'
    FREEVEHICLELEFTLIMIT_SUBMIT = b'#dialogs:freeVehicleLeftLimit/submit'
    VOICECHATINITFAILED_TITLE = b'#dialogs:voiceChatInitFailed/title'
    VOICECHATINITFAILED_MESSAGE = b'#dialogs:voiceChatInitFailed/message'
    VOICECHATINITFAILED_CANCEL = b'#dialogs:voiceChatInitFailed/cancel'
    VOICECHATINITSUCCEDED_TITLE = b'#dialogs:voiceChatInitSucceded/title'
    VOICECHATINITSUCCEDED_MESSAGE = b'#dialogs:voiceChatInitSucceded/message'
    VOICECHATINITSUCCEDED_CANCEL = b'#dialogs:voiceChatInitSucceded/cancel'
    INGAMEBROWSER_TEXTURELOADINGFAILED_TITLE = b'#dialogs:inGameBrowser/textureLoadingFailed/title'
    INGAMEBROWSER_TEXTURELOADINGFAILED_MESSAGE = b'#dialogs:inGameBrowser/textureLoadingFailed/message'
    MESSENGER_USERINFOHIDDEN_TITLE = b'#dialogs:messenger/userInfoHidden/title'
    MESSENGER_USERINFOHIDDEN_MESSAGE = b'#dialogs:messenger/userInfoHidden/message'
    MESSENGER_USERINFOHIDDEN_SUBMIT = b'#dialogs:messenger/userInfoHidden/submit'
    MESSENGER_USERINFOHIDDEN_CANCEL = b'#dialogs:messenger/userInfoHidden/cancel'
    MESSENGER_USERINFONOTAVAILABLE_TITLE = b'#dialogs:messenger/userInfoNotAvailable/title'
    MESSENGER_USERINFONOTAVAILABLE_MESSAGE = b'#dialogs:messenger/userInfoNotAvailable/message'
    MESSENGER_USERINFONOTAVAILABLE_SUBMIT = b'#dialogs:messenger/userInfoNotAvailable/submit'
    MESSENGER_USERINFONOTAVAILABLE_CANCEL = b'#dialogs:messenger/userInfoNotAvailable/cancel'
    VEHICLEREMOVEDIALOG_TITLE = b'#dialogs:vehicleRemoveDialog/title'
    VEHICLESELLDIALOG_EXPANDBTNLABEL = b'#dialogs:vehicleSellDialog/expandBtnLabel'
    VEHICLESELLDIALOG_TITLE = b'#dialogs:vehicleSellDialog/title'
    VEHICLESELLDIALOG_MESSAGE = b'#dialogs:vehicleSellDialog/message'
    VEHICLESELLDIALOG_MESSAGE_MULTINATIONAL = b'#dialogs:vehicleSellDialog/message/multinational'
    VEHICLESELLDIALOG_VEHICLETYPE_LIGHTTANK = b'#dialogs:vehicleSellDialog/vehicleType/lightTank'
    VEHICLESELLDIALOG_VEHICLETYPE_MEDIUMTANK = b'#dialogs:vehicleSellDialog/vehicleType/mediumTank'
    VEHICLESELLDIALOG_VEHICLETYPE_HEAVYTANK = b'#dialogs:vehicleSellDialog/vehicleType/heavyTank'
    VEHICLESELLDIALOG_VEHICLETYPE_SPG = b'#dialogs:vehicleSellDialog/vehicleType/SPG'
    VEHICLESELLDIALOG_VEHICLETYPE_AT_SPG = b'#dialogs:vehicleSellDialog/vehicleType/AT-SPG'
    VEHICLESELLDIALOG_VEHICLE_LEVEL = b'#dialogs:vehicleSellDialog/vehicle/level'
    VEHICLESELLDIALOG_VEHICLE_ROLE = b'#dialogs:vehicleSellDialog/vehicle/role'
    VEHICLESELLDIALOG_VEHICLE_EMPTYSELLPRICE = b'#dialogs:vehicleSellDialog/vehicle/emptySellPrice'
    VEHICLESELLDIALOG_PROFFIT = b'#dialogs:vehicleSellDialog/proffit'
    VEHICLESELLDIALOG_LOSS = b'#dialogs:vehicleSellDialog/loss'
    VEHICLESELLDIALOG_CREW_LABEL = b'#dialogs:vehicleSellDialog/crew/label'
    VEHICLESELLDIALOG_OPTIONALDEVICE = b'#dialogs:vehicleSellDialog/optionalDevice'
    VEHICLESELLDIALOG_EQUIPMENT = b'#dialogs:vehicleSellDialog/equipment'
    VEHICLESELLDIALOG_BATTLEBOSTER = b'#dialogs:vehicleSellDialog/battleBoster'
    VEHICLESELLDIALOG_CUSTOMIZATION = b'#dialogs:vehicleSellDialog/customization'
    VEHICLESELLDIALOG_AMMO_LABEL = b'#dialogs:vehicleSellDialog/ammo/label'
    VEHICLESELLDIALOG_COMMONRESULT = b'#dialogs:vehicleSellDialog/commonResult'
    VEHICLESELLDIALOG_INVENTORY = b'#dialogs:vehicleSellDialog/inventory'
    VEHICLESELLDIALOG_UNLOAD = b'#dialogs:vehicleSellDialog/unload'
    VEHICLESELLDIALOG_DECONSTRUCT = b'#dialogs:vehicleSellDialog/deconstruct'
    VEHICLESELLDIALOG_NOTINSTALLED_MODULES = b'#dialogs:vehicleSellDialog/notInstalled/modules'
    VEHICLESELLDIALOG_COUNT = b'#dialogs:vehicleSellDialog/count'
    VEHICLESELLDIALOG_REMOVE = b'#dialogs:vehicleSellDialog/remove'
    VEHICLESELLDIALOG_SUBMIT = b'#dialogs:vehicleSellDialog/submit'
    VEHICLESELLDIALOG_CANCEL = b'#dialogs:vehicleSellDialog/cancel'
    VEHICLESELLDIALOG_VEHICLE_ELITE = b'#dialogs:vehicleSellDialog/vehicle/elite'
    VEHICLESELLDIALOG_CREW_UNLOAD = b'#dialogs:vehicleSellDialog/crew/Unload'
    VEHICLESELLDIALOG_CREW_DISSMISS = b'#dialogs:vehicleSellDialog/crew/Dissmiss'
    VEHICLESELLDIALOG_CTRLQUESTION_HEADER = b'#dialogs:vehicleSellDialog/CtrlQuestion/Header'
    VEHICLESELLDIALOG_CTRLQUESTION_QUESTION = b'#dialogs:vehicleSellDialog/CtrlQuestion/Question'
    VEHICLESELLDIALOG_CTRLQUESTION_ERRORMESSAGE = b'#dialogs:vehicleSellDialog/CtrlQuestion/errorMessage'
    VEHICLESELLDIALOG_PRICE_SIGN_ADD = b'#dialogs:vehicleSellDialog/price/sign/add'
    VEHICLESELLDIALOG_POSTPROGRESSIONINFO = b'#dialogs:vehicleSellDialog/postProgressionInfo'
    VEHICLESELLDIALOG_POSTPROGRESSIONINFO_SUBSCRIPTION = b'#dialogs:vehicleSellDialog/postProgressionInfo_subscription'
    VEHICLESELL_UNIQUE_TITLE = b'#dialogs:vehicleSell/unique/title'
    VEHICLESELL_UNIQUE_MESSAGE = b'#dialogs:vehicleSell/unique/message'
    VEHICLESELL_UNIQUE_SUBMIT = b'#dialogs:vehicleSell/unique/submit'
    VEHICLESELL_UNIQUE_CANCEL = b'#dialogs:vehicleSell/unique/cancel'
    VEHICLESELL_UNIQUE_CREWLOCKED_TITLE = b'#dialogs:vehicleSell/unique/crewLocked/title'
    VEHICLESELL_UNIQUE_CREWLOCKED_MESSAGE = b'#dialogs:vehicleSell/unique/crewLocked/message'
    VEHICLESELL_UNIQUE_CREWLOCKED_SUBMIT = b'#dialogs:vehicleSell/unique/crewLocked/submit'
    VEHICLESELL_UNIQUE_CREWLOCKED_CANCEL = b'#dialogs:vehicleSell/unique/crewLocked/cancel'
    VEHICLESELL_RESTORECOOLDOWN_TITLE = b'#dialogs:vehicleSell/restoreCooldown/title'
    VEHICLESELL_RESTORECOOLDOWN_MESSAGE = b'#dialogs:vehicleSell/restoreCooldown/message'
    VEHICLESELL_RESTORECOOLDOWN_SUBMIT = b'#dialogs:vehicleSell/restoreCooldown/submit'
    VEHICLESELL_RESTORECOOLDOWN_CANCEL = b'#dialogs:vehicleSell/restoreCooldown/cancel'
    VEHICLESELL_RESTOREUNLIMITED_TITLE = b'#dialogs:vehicleSell/restoreUnlimited/title'
    VEHICLESELL_RESTOREUNLIMITED_MESSAGE = b'#dialogs:vehicleSell/restoreUnlimited/message'
    VEHICLESELL_RESTOREUNLIMITED_SUBMIT = b'#dialogs:vehicleSell/restoreUnlimited/submit'
    VEHICLESELL_RESTOREUNLIMITED_CANCEL = b'#dialogs:vehicleSell/restoreUnlimited/cancel'
    UPDATENEEDED_TITLE = b'#dialogs:updateNeeded/title'
    UPDATENEEDED_MESSAGE = b'#dialogs:updateNeeded/message'
    UPDATENEEDED_SUBMIT = b'#dialogs:updateNeeded/submit'
    UPDATENEEDED_CANCEL = b'#dialogs:updateNeeded/cancel'
    DEMOACCOUNTBOOTCAMPFAILURE_TITLE = b'#dialogs:demoAccountBootcampFailure/title'
    DEMOACCOUNTBOOTCAMPFAILURE_MESSAGE = b'#dialogs:demoAccountBootcampFailure/message'
    DEMOACCOUNTBOOTCAMPFAILURE_CANCEL = b'#dialogs:demoAccountBootcampFailure/cancel'
    STEAMSTARTNEEDED_TITLE = b'#dialogs:steamStartNeeded/title'
    STEAMSTARTNEEDED_MESSAGE = b'#dialogs:steamStartNeeded/message'
    STEAMSTARTNEEDED_CANCEL = b'#dialogs:steamStartNeeded/cancel'
    REPLAYNOTIFICATION_TITLE = b'#dialogs:replayNotification/title'
    REPLAYNOTIFICATION_MESSAGE = b'#dialogs:replayNotification/message'
    REPLAYNOTIFICATION_SUBMIT = b'#dialogs:replayNotification/submit'
    REPLAYNOTIFICATION_CANCEL = b'#dialogs:replayNotification/cancel'
    REPLAYSTOPPED_TITLE = b'#dialogs:replayStopped/title'
    REPLAYSTOPPED_MESSAGE = b'#dialogs:replayStopped/message'
    REPLAYSTOPPED_SUBMIT = b'#dialogs:replayStopped/submit'
    REPLAYSTOPPED_CANCEL = b'#dialogs:replayStopped/cancel'
    PUNISHMENTWINDOW_TITLE = b'#dialogs:punishmentWindow/title'
    PUNISHMENTWINDOW_MSGTITLE_WARNING = b'#dialogs:punishmentWindow/msgTitle/warning'
    PUNISHMENTWINDOW_MSGTITLE_PENALTY = b'#dialogs:punishmentWindow/msgTitle/penalty'
    PUNISHMENTWINDOW_MESSAGE_WARNING = b'#dialogs:punishmentWindow/message/warning'
    PUNISHMENTWINDOW_MESSAGE_PENALTY = b'#dialogs:punishmentWindow/message/penalty'
    PUNISHMENTWINDOW_MESSAGE_EXTRA_PENALTY = b'#dialogs:punishmentWindow/message/extra/penalty'
    PUNISHMENTWINDOW_CANCEL = b'#dialogs:punishmentWindow/cancel'
    PUNISHMENTWINDOW_REASON_DESERTER = b'#dialogs:punishmentWindow/reason/deserter'
    PUNISHMENTWINDOW_REASON_EPIC_DESERTER = b'#dialogs:punishmentWindow/reason/epic_deserter'
    PUNISHMENTWINDOW_REASON_SUICIDE = b'#dialogs:punishmentWindow/reason/suicide'
    PUNISHMENTWINDOW_REASON_AFK = b'#dialogs:punishmentWindow/reason/afk'
    PUNISHMENTWINDOW_REASON_BATTLEROYALE_DESERTER = b'#dialogs:punishmentWindow/reason/battleroyale_deserter'
    PUNISHMENTWINDOW_REASON_BATTLEROYALE_AFK = b'#dialogs:punishmentWindow/reason/battleroyale_afk'
    REMOVEINCOMPATIBLEEQS_TITLE = b'#dialogs:removeIncompatibleEqs/title'
    REMOVEINCOMPATIBLEEQS_MESSAGE = b'#dialogs:removeIncompatibleEqs/message'
    REMOVEINCOMPATIBLEEQS_MESSAGE_REASON = b'#dialogs:removeIncompatibleEqs/message/reason'
    REMOVEINCOMPATIBLEEQS_SUBMIT = b'#dialogs:removeIncompatibleEqs/submit'
    REMOVEINCOMPATIBLEEQS_CANCEL = b'#dialogs:removeIncompatibleEqs/cancel'
    REFUSETRAINING_TITLE = b'#dialogs:refuseTraining/title'
    REFUSETRAINING_MESSAGE = b'#dialogs:refuseTraining/message'
    REFUSETRAINING_SUBMIT = b'#dialogs:refuseTraining/submit'
    REFUSETRAINING_CANCEL = b'#dialogs:refuseTraining/cancel'
    SHOPSYNCERROR_TITLE = b'#dialogs:shopSyncError/title'
    SHOPSYNCERROR_MESSAGE = b'#dialogs:shopSyncError/message'
    SHOPSYNCERROR_CANCEL = b'#dialogs:shopSyncError/cancel'
    RESETGRAPHICS_TITLE = b'#dialogs:resetGraphics/title'
    RESETGRAPHICS_MESSAGE = b'#dialogs:resetGraphics/message'
    RESETGRAPHICS_SUBMIT = b'#dialogs:resetGraphics/submit'
    RESETGRAPHICS_CANCEL = b'#dialogs:resetGraphics/cancel'
    CHANGEGRAPHICS_TITLE = b'#dialogs:changeGraphics/title'
    CHANGEGRAPHICS_MESSAGE = b'#dialogs:changeGraphics/message'
    CHANGEGRAPHICS_SUBMIT = b'#dialogs:changeGraphics/submit'
    CHANGEGRAPHICS_CANCEL = b'#dialogs:changeGraphics/cancel'
    GRAPHICS_MESSAGE_ALERT = b'#dialogs:graphics/message/alert'
    LOWFPSWARNING_TITLE = b'#dialogs:lowFpsWarning/title'
    LOWFPSWARNING_MESSAGE = b'#dialogs:lowFpsWarning/message'
    LOWFPSWARNING_SUBMIT = b'#dialogs:lowFpsWarning/submit'
    LOWFPSWARNING_CANCEL = b'#dialogs:lowFpsWarning/cancel'
    KOREAPARENTNOTIFICATION_TITLE = b'#dialogs:koreaParentNotification/title'
    KOREAPARENTNOTIFICATION_MESSAGE = b'#dialogs:koreaParentNotification/message'
    KOREAPARENTNOTIFICATION_SUBMIT = b'#dialogs:koreaParentNotification/submit'
    KOREAPARENTNOTIFICATION_CANCEL = b'#dialogs:koreaParentNotification/cancel'
    KOREAPLAYTIMENOTIFICATION_TITLE = b'#dialogs:koreaPlayTimeNotification/title'
    KOREAPLAYTIMENOTIFICATION_MESSAGE = b'#dialogs:koreaPlayTimeNotification/message'
    KOREAPLAYTIMENOTIFICATION_SUBMIT = b'#dialogs:koreaPlayTimeNotification/submit'
    KOREAPLAYTIMENOTIFICATION_CANCEL = b'#dialogs:koreaPlayTimeNotification/cancel'
    SENDINVITES_COMMON_TITLE = b'#dialogs:sendInvites/common/title'
    RALLY_AUTOSEARCH_TITLE = b'#dialogs:rally/autoSearch/title'
    RALLY_AUTOSEARCH_MESSAGE = b'#dialogs:rally/autoSearch/message'
    RALLY_AUTOSEARCH_SUBMIT = b'#dialogs:rally/autoSearch/submit'
    RALLY_AUTOSEARCH_CANCEL = b'#dialogs:rally/autoSearch/cancel'
    RALLY_STARTBATTLE_TITLE = b'#dialogs:rally/startBattle/title'
    RALLY_STARTBATTLE_MESSAGE = b'#dialogs:rally/startBattle/message'
    RALLY_STARTBATTLE_SUBMIT = b'#dialogs:rally/startBattle/submit'
    RALLY_STARTBATTLE_CANCEL = b'#dialogs:rally/startBattle/cancel'
    RALLY_CHANGEPERIPHERY_TITLE = b'#dialogs:rally/changePeriphery/title'
    RALLY_CHANGEPERIPHERY_MESSAGE = b'#dialogs:rally/changePeriphery/message'
    RALLY_CHANGEPERIPHERY_SUBMIT = b'#dialogs:rally/changePeriphery/submit'
    RALLY_CHANGEPERIPHERY_CANCEL = b'#dialogs:rally/changePeriphery/cancel'
    RALLY_GOTOANOTHER_TITLE = b'#dialogs:rally/goToAnother/title'
    RALLY_GOTOANOTHER_MESSAGE = b'#dialogs:rally/goToAnother/message'
    RALLY_GOTOANOTHER_SUBMIT = b'#dialogs:rally/goToAnother/submit'
    RALLY_GOTOANOTHER_CANCEL = b'#dialogs:rally/goToAnother/cancel'
    RALLY_GOTOSQUAD_TITLE = b'#dialogs:rally/goToSquad/title'
    RALLY_GOTOSQUAD_MESSAGE = b'#dialogs:rally/goToSquad/message'
    RALLY_GOTOSQUAD_SUBMIT = b'#dialogs:rally/goToSquad/submit'
    RALLY_GOTOSQUAD_CANCEL = b'#dialogs:rally/goToSquad/cancel'
    SQUAD_GOTOSQUAD_TITLE = b'#dialogs:squad/goToSquad/title'
    SQUAD_GOTOSQUAD_MESSAGE = b'#dialogs:squad/goToSquad/message'
    SQUAD_GOTOSQUAD_SUBMIT = b'#dialogs:squad/goToSquad/submit'
    SQUAD_GOTOSQUAD_CANCEL = b'#dialogs:squad/goToSquad/cancel'
    SQUAD_GOTOANOTHER_TITLE = b'#dialogs:squad/goToAnother/title'
    SQUAD_GOTOANOTHER_MESSAGE = b'#dialogs:squad/goToAnother/message'
    SQUAD_GOTOANOTHER_SUBMIT = b'#dialogs:squad/goToAnother/submit'
    SQUAD_GOTOANOTHER_CANCEL = b'#dialogs:squad/goToAnother/cancel'
    RALLY_LEAVE_TITLE = b'#dialogs:rally/leave/title'
    RALLY_LEAVE_MESSAGE = b'#dialogs:rally/leave/message'
    RALLY_LEAVE_SUBMIT = b'#dialogs:rally/leave/submit'
    RALLY_LEAVE_CANCEL = b'#dialogs:rally/leave/cancel'
    RALLY_GOTOINTRO_TITLE = b'#dialogs:rally/goToIntro/title'
    RALLY_GOTOINTRO_MESSAGE = b'#dialogs:rally/goToIntro/message'
    RALLY_GOTOINTRO_SUBMIT = b'#dialogs:rally/goToIntro/submit'
    RALLY_GOTOINTRO_CANCEL = b'#dialogs:rally/goToIntro/cancel'
    SQUAD_LEAVE_TITLE = b'#dialogs:squad/leave/title'
    SQUAD_LEAVE_MESSAGE = b'#dialogs:squad/leave/message'
    SQUAD_LEAVE_SUBMIT = b'#dialogs:squad/leave/submit'
    SQUAD_LEAVE_CANCEL = b'#dialogs:squad/leave/cancel'
    RALLY_LEAVEDISABLED_TITLE = b'#dialogs:rally/leaveDisabled/title'
    RALLY_LEAVEDISABLED_MESSAGE = b'#dialogs:rally/leaveDisabled/message'
    RALLY_LEAVEDISABLED_CANCEL = b'#dialogs:rally/leaveDisabled/cancel'
    SQUAD_LEAVEDISABLED_TITLE = b'#dialogs:squad/leaveDisabled/title'
    SQUAD_LEAVEDISABLED_MESSAGE = b'#dialogs:squad/leaveDisabled/message'
    SQUAD_LEAVEDISABLED_CANCEL = b'#dialogs:squad/leaveDisabled/cancel'
    CHANGEPERIPHERY_TITLE = b'#dialogs:changePeriphery/title'
    CHANGEPERIPHERY_MESSAGE = b'#dialogs:changePeriphery/message'
    CHANGEPERIPHERY_SUBMIT = b'#dialogs:changePeriphery/submit'
    CHANGEPERIPHERY_CANCEL = b'#dialogs:changePeriphery/cancel'
    CHANGEROAMINGPERIPHERY_TITLE = b'#dialogs:changeRoamingPeriphery/title'
    CHANGEROAMINGPERIPHERY_MESSAGE = b'#dialogs:changeRoamingPeriphery/message'
    CHANGEROAMINGPERIPHERY_SUBMIT = b'#dialogs:changeRoamingPeriphery/submit'
    CHANGEROAMINGPERIPHERY_CANCEL = b'#dialogs:changeRoamingPeriphery/cancel'
    CHANGEPERIPHERYANDREMEMBER_TITLE = b'#dialogs:changePeripheryAndRemember/title'
    CHANGEPERIPHERYANDREMEMBER_MESSAGE = b'#dialogs:changePeripheryAndRemember/message'
    CHANGEPERIPHERYANDREMEMBER_SUBMIT = b'#dialogs:changePeripheryAndRemember/submit'
    CHANGEPERIPHERYANDREMEMBER_CANCEL = b'#dialogs:changePeripheryAndRemember/cancel'
    CHANGEROAMINGPERIPHERYANDREMEMBER_TITLE = b'#dialogs:changeRoamingPeripheryAndRemember/title'
    CHANGEROAMINGPERIPHERYANDREMEMBER_MESSAGE = b'#dialogs:changeRoamingPeripheryAndRemember/message'
    CHANGEROAMINGPERIPHERYANDREMEMBER_SUBMIT = b'#dialogs:changeRoamingPeripheryAndRemember/submit'
    CHANGEROAMINGPERIPHERYANDREMEMBER_CANCEL = b'#dialogs:changeRoamingPeripheryAndRemember/cancel'
    LOGINTOPERIPHERYANDREMEMBER_TITLE = b'#dialogs:loginToPeripheryAndRemember/title'
    LOGINTOPERIPHERYANDREMEMBER_MESSAGE = b'#dialogs:loginToPeripheryAndRemember/message'
    LOGINTOPERIPHERYANDREMEMBER_SUBMIT = b'#dialogs:loginToPeripheryAndRemember/submit'
    LOGINTOPERIPHERYANDREMEMBER_CANCEL = b'#dialogs:loginToPeripheryAndRemember/cancel'
    FREEXPINFO_TITLE = b'#dialogs:freeXPInfo/title'
    FREEXPINFO_MESSAGE = b'#dialogs:freeXPInfo/message'
    FREEXPINFO_SUBMITBTNLBL = b'#dialogs:freeXPInfo/submitBtnLbl'
    SWITCHPERIPHERYWINDOW_WINDOWTITLE = b'#dialogs:switchPeripheryWindow/windowTitle'
    SWITCHPERIPHERYWINDOW_BTNSWITCH = b'#dialogs:switchPeripheryWindow/btnSwitch'
    SWITCHPERIPHERYWINDOW_BTNCANCEL = b'#dialogs:switchPeripheryWindow/btnCancel'
    CREATEORDERCONFIRMATION_TITLE = b'#dialogs:createOrderConfirmation/title'
    CREATEORDERCONFIRMATION_SUBMIT = b'#dialogs:createOrderConfirmation/submit'
    CREATEORDERCONFIRMATION_CANCEL = b'#dialogs:createOrderConfirmation/cancel'
    FORTIFICATIONFIXEDPLAYERS_TITLE = b'#dialogs:fortificationFixedPlayers/title'
    FORTIFICATIONFIXEDPLAYERS_MESSAGE = b'#dialogs:fortificationFixedPlayers/message'
    FORTIFICATIONFIXEDPLAYERS_SUBMIT = b'#dialogs:fortificationFixedPlayers/submit'
    FORTIFICATIONFIXEDPLAYERS_CANCEL = b'#dialogs:fortificationFixedPlayers/cancel'
    FORTIFICATIONCLOSEDIRECTION_SUBMIT = b'#dialogs:fortificationCloseDirection/submit'
    FORTIFICATIONCLOSEDIRECTION_CANCEL = b'#dialogs:fortificationCloseDirection/cancel'
    REPORTBUG_TITLE = b'#dialogs:reportBug/title'
    REPORTBUG_MESSAGE = b'#dialogs:reportBug/message'
    REPORTBUG_SUBMIT = b'#dialogs:reportBug/submit'
    REPORTBUG_CANCEL = b'#dialogs:reportBug/cancel'
    FORTTURNEDOFF_CANCEL = b'#dialogs:fortTurnedOff/cancel'
    FORTTURNEDOFF_TITLE = b'#dialogs:fortTurnedOff/title'
    FORTTURNEDOFF_MESSAGE = b'#dialogs:fortTurnedOff/message'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_TITLE = b'#dialogs:confirmExchangeDialog/exchangeCredits/title'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_TITLE = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/title'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_TITLE = b'#dialogs:confirmExchangeDialog/exchangeXp/title'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_NEEDITEMSTEXT = b'#dialogs:confirmExchangeDialog/exchangeCredits/needItemsText'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_NEEDITEMSTEXT = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/needItemsText'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_NEEDITEMSTEXT = b'#dialogs:confirmExchangeDialog/exchangeXp/needItemsText'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_NEEDGOLDTEXT = b'#dialogs:confirmExchangeDialog/exchangeCredits/needGoldText'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_NEEDGOLDTEXT = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/needGoldText'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_NEEDGOLDTEXT = b'#dialogs:confirmExchangeDialog/exchangeXp/needGoldText'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_NEEDITEMSSTEPPERTITLE = b'#dialogs:confirmExchangeDialog/exchangeCredits/needItemsStepperTitle'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_NEEDITEMSSTEPPERTITLE = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/needItemsStepperTitle'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_NEEDITEMSSTEPPERTITLE = b'#dialogs:confirmExchangeDialog/exchangeXp/needItemsStepperTitle'
    CONFIRMEXCHANGEDIALOG_GOLDITEMSSTEPPERTITLE = b'#dialogs:confirmExchangeDialog/goldItemsStepperTitle'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_SUBMIT = b'#dialogs:confirmExchangeDialog/exchangeCredits/submit'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_SUBMIT = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/submit'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_SUBMIT = b'#dialogs:confirmExchangeDialog/exchangeXp/submit'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_CANCEL = b'#dialogs:confirmExchangeDialog/exchangeCredits/cancel'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_CANCEL = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/cancel'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_CANCEL = b'#dialogs:confirmExchangeDialog/exchangeXp/cancel'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_EXCHANGENONEEDTEXT = b'#dialogs:confirmExchangeDialog/exchangeCredits/exchangeNoNeedText'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_EXCHANGENONEEDTEXT = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/exchangeNoNeedText'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_EXCHANGENONEEDTEXT = b'#dialogs:confirmExchangeDialog/exchangeXp/exchangeNoNeedText'
    CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_GOLDNOTENOUGHTEXT = b'#dialogs:confirmExchangeDialog/exchangeCredits/goldNotEnoughText'
    CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_GOLDNOTENOUGHTEXT = b'#dialogs:confirmExchangeDialog/restoreExchangeCredits/goldNotEnoughText'
    CONFIRMEXCHANGEDIALOG_EXCHANGEXP_GOLDNOTENOUGHTEXT = b'#dialogs:confirmExchangeDialog/exchangeXp/goldNotEnoughText'
    QUESTSCONFIRMDIALOG_TITLE = b'#dialogs:questsConfirmDialog/title'
    QUESTSCONFIRMDIALOG_MESSAGE = b'#dialogs:questsConfirmDialog/message'
    QUESTSCONFIRMDIALOG_SUBMIT = b'#dialogs:questsConfirmDialog/submit'
    QUESTSCONFIRMDIALOG_CANCEL = b'#dialogs:questsConfirmDialog/cancel'
    QUESTSCONFIRMDIALOG_CHECKBOX = b'#dialogs:questsConfirmDialog/checkBox'
    QUESTSCONFIRMPM3DIALOG_TITLE = b'#dialogs:questsConfirmPm3Dialog/title'
    QUESTSCONFIRMPM3DIALOG_MESSAGE = b'#dialogs:questsConfirmPm3Dialog/message'
    QUESTSCONFIRMPM3DIALOG_SUBMIT = b'#dialogs:questsConfirmPm3Dialog/submit'
    QUESTSCONFIRMPM3DIALOG_CANCEL = b'#dialogs:questsConfirmPm3Dialog/cancel'
    QUESTSCONFIRMPM3DIALOG_CHECKBOX = b'#dialogs:questsConfirmPm3Dialog/checkBox'
    QUESTSCONFIRMPROGRESSDIALOG_TITLE = b'#dialogs:questsConfirmProgressDialog/title'
    QUESTSCONFIRMPROGRESSDIALOG_MESSAGE = b'#dialogs:questsConfirmProgressDialog/message'
    QUESTSCONFIRMPROGRESSDIALOG_MESSAGE_ALERT = b'#dialogs:questsConfirmProgressDialog/message/alert'
    QUESTSCONFIRMPROGRESSDIALOG_SUBMIT = b'#dialogs:questsConfirmProgressDialog/submit'
    QUESTSCONFIRMPROGRESSDIALOG_CANCEL = b'#dialogs:questsConfirmProgressDialog/cancel'
    QUESTSDISMISSPROGRESSDIALOG_TITLE = b'#dialogs:questsDismissProgressDialog/title'
    QUESTSCONFIRMDISCARDDIALOG_TITLE = b'#dialogs:questsConfirmDiscardDialog/title'
    QUESTSDISMISSPROGRESSDIALOG_MESSAGE = b'#dialogs:questsDismissProgressDialog/message'
    QUESTSDISMISSPROGRESSDIALOG_MESSAGE_ALERT = b'#dialogs:questsDismissProgressDialog/message/alert'
    QUESTSDISMISSPROGRESSDIALOG_SUBMIT = b'#dialogs:questsDismissProgressDialog/submit'
    QUESTSDISMISSPROGRESSDIALOG_CANCEL = b'#dialogs:questsDismissProgressDialog/cancel'
    QUESTSCONFIRMDISCARDDIALOG_MESSAGE = b'#dialogs:questsConfirmDiscardDialog/message'
    QUESTSCONFIRMDISCARDDIALOG_MESSAGE_ALERT = b'#dialogs:questsConfirmDiscardDialog/message/alert'
    QUESTSCONFIRMDISCARDDIALOG_SUBMIT = b'#dialogs:questsConfirmDiscardDialog/submit'
    QUESTSCONFIRMDISCARDDIALOG_CANCEL = b'#dialogs:questsConfirmDiscardDialog/cancel'
    EPICBATTLECONFIRMDIALOG_TITLE = b'#dialogs:epicBattleConfirmDialog/title'
    EPICBATTLECONFIRMDIALOG_MESSAGE = b'#dialogs:epicBattleConfirmDialog/message'
    EPICBATTLECONFIRMDIALOG_SUBMIT = b'#dialogs:epicBattleConfirmDialog/submit'
    EPICBATTLECONFIRMDIALOG_CANCEL = b'#dialogs:epicBattleConfirmDialog/cancel'
    EPICBATTLECONFIRMDIALOG_CHECKBOX = b'#dialogs:epicBattleConfirmDialog/checkBox'
    BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_TITLE = b'#dialogs:boostersWindow/activationConfirmation/title'
    BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_MESSAGE = b'#dialogs:boostersWindow/activationConfirmation/message'
    BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_SUBMIT = b'#dialogs:boostersWindow/activationConfirmation/submit'
    BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_CANCEL = b'#dialogs:boostersWindow/activationConfirmation/cancel'
    BOOSTERSWINDOW_REPLACECONFIRMATION_TITLE = b'#dialogs:boostersWindow/replaceConfirmation/title'
    BOOSTERSWINDOW_REPLACECONFIRMATION_MESSAGE = b'#dialogs:boostersWindow/replaceConfirmation/message'
    BOOSTERSWINDOW_REPLACECONFIRMATION_SUBMIT = b'#dialogs:boostersWindow/replaceConfirmation/submit'
    BOOSTERSWINDOW_REPLACECONFIRMATION_CANCEL = b'#dialogs:boostersWindow/replaceConfirmation/cancel'
    CLANCONFIRMJOINING_TITLE = b'#dialogs:clanConfirmJoining/title'
    CLANCONFIRMJOINING_MESSAGE = b'#dialogs:clanConfirmJoining/message'
    CLANCONFIRMJOINING_MESSAGE_CLANNAME = b'#dialogs:clanConfirmJoining/message/clanName'
    CLANCONFIRMJOINING_MESSAGE_CLANEXIT = b'#dialogs:clanConfirmJoining/message/clanExit'
    CLANCONFIRMJOINING_SUBMIT = b'#dialogs:clanConfirmJoining/submit'
    CLANCONFIRMJOINING_CANCEL = b'#dialogs:clanConfirmJoining/cancel'
    CUSTOMIZATION_CLOSE_TITLE = b'#dialogs:customization/close/title'
    CUSTOMIZATION_CLOSE_SUBMIT = b'#dialogs:customization/close/submit'
    CUSTOMIZATION_CLOSE_CANCEL = b'#dialogs:customization/close/cancel'
    CUSTOMIZATION_EXITTOSHOP_TITLE = b'#dialogs:customization/exitToShop/title'
    CUSTOMIZATION_EXITTOSHOP_SUBMIT = b'#dialogs:customization/exitToShop/submit'
    CUSTOMIZATION_EXITTOSHOP_CANCEL = b'#dialogs:customization/exitToShop/cancel'
    CUSTOMIZATION_FILTER_TITLE = b'#dialogs:customization/filter/title'
    CUSTOMIZATION_FILTER_MESSAGE = b'#dialogs:customization/filter/message'
    CUSTOMIZATION_FILTER_SUBMIT = b'#dialogs:customization/filter/submit'
    CUSTOMIZATION_FILTER_CANCEL = b'#dialogs:customization/filter/cancel'
    CUSTOMIZATION_REMOVE_ELEMENT_TITLE = b'#dialogs:customization/remove_element/title'
    CUSTOMIZATION_REMOVE_ELEMENT_MESSAGE = b'#dialogs:customization/remove_element/message'
    CUSTOMIZATION_REMOVE_ELEMENT_SUBMIT = b'#dialogs:customization/remove_element/submit'
    CUSTOMIZATION_REMOVE_ELEMENT_CANCEL = b'#dialogs:customization/remove_element/cancel'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_WILL_BE_DELETED = b'#dialogs:customization/install_invoice_item/will_be_deleted'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_TITLE = b'#dialogs:customization/install_invoice_item/temporary/title'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_MESSAGE = b'#dialogs:customization/install_invoice_item/temporary/message'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_SUBMIT = b'#dialogs:customization/install_invoice_item/temporary/submit'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_CANCEL = b'#dialogs:customization/install_invoice_item/temporary/cancel'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_TITLE = b'#dialogs:customization/install_invoice_item/permanent/title'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_MESSAGE = b'#dialogs:customization/install_invoice_item/permanent/message'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_SUBMIT = b'#dialogs:customization/install_invoice_item/permanent/submit'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_CANCEL = b'#dialogs:customization/install_invoice_item/permanent/cancel'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_TITLE = b'#dialogs:customization/install_invoice_item/permanent_last/title'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_MESSAGE = b'#dialogs:customization/install_invoice_item/permanent_last/message'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_SUBMIT = b'#dialogs:customization/install_invoice_item/permanent_last/submit'
    CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_CANCEL = b'#dialogs:customization/install_invoice_item/permanent_last/cancel'
    CUSTOMIZATION_BUY_INSTALL_BOUND_TITLE = b'#dialogs:customization/buy_install_bound/title'
    CUSTOMIZATION_BUY_INSTALL_BOUND_MESSAGE = b'#dialogs:customization/buy_install_bound/message'
    CUSTOMIZATION_CHANGE_INSTALL_BOUND_TITLE = b'#dialogs:customization/change_install_bound/title'
    CUSTOMIZATION_CHANGE_INSTALL_BOUND_MESSAGE = b'#dialogs:customization/change_install_bound/message'
    CUSTOMIZATION_INSTALL_BOUND_SUBMIT = b'#dialogs:customization/install_bound/submit'
    CUSTOMIZATION_INSTALL_BOUND_CANCEL = b'#dialogs:customization/install_bound/cancel'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_TITLE = b'#dialogs:customization/applyToOtherSeasons/title'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_MESSAGE = b'#dialogs:customization/applyToOtherSeasons/message'
    CUSTOMIZATION_APPLYTOOTHERSEASON_MESSAGE = b'#dialogs:customization/applyToOtherSeason/message'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_ALERT_MESSAGE = b'#dialogs:customization/applyToOtherSeasons/alert_message'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_SUBMIT = b'#dialogs:customization/applyToOtherSeasons/submit'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_CANCEL = b'#dialogs:customization/applyToOtherSeasons/cancel'
    CUSTOMIZATION_APPLYTOOTHERSEASON_SUMMER = b'#dialogs:customization/applyToOtherSeason/summer'
    CUSTOMIZATION_APPLYTOOTHERSEASON_WINTER = b'#dialogs:customization/applyToOtherSeason/winter'
    CUSTOMIZATION_APPLYTOOTHERSEASON_DESERT = b'#dialogs:customization/applyToOtherSeason/desert'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_SUMMER = b'#dialogs:customization/applyToOtherSeasons/summer'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_WINTER = b'#dialogs:customization/applyToOtherSeasons/winter'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_DESERT = b'#dialogs:customization/applyToOtherSeasons/desert'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_SUMMER_WINTER = b'#dialogs:customization/applyToOtherSeasons/summer_winter'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_WINTER_DESERT = b'#dialogs:customization/applyToOtherSeasons/winter_desert'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_SUMMER_DESERT = b'#dialogs:customization/applyToOtherSeasons/summer_desert'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_REMOVED = b'#dialogs:customization/applyToOtherSeasons/removed'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_THIS = b'#dialogs:customization/applyToOtherSeasons/this'
    CUSTOMIZATION_APPLYTOOTHERSEASONS_THESE = b'#dialogs:customization/applyToOtherSeasons/these'
    FORTDISABLED_TITLE = b'#dialogs:fortDisabled/title'
    FORTDISABLED_MESSAGE = b'#dialogs:fortDisabled/message'
    FORTDISABLED_CANCEL = b'#dialogs:fortDisabled/cancel'
    ELENDISABLED_TITLE = b'#dialogs:elenDisabled/title'
    ELENDISABLED_MESSAGE = b'#dialogs:elenDisabled/message'
    ELENDISABLED_CANCEL = b'#dialogs:elenDisabled/cancel'
    CLAN_DATA_NOT_AVAILABLE_TITLE = b'#dialogs:clan_data_not_available/title'
    CLAN_DATA_NOT_AVAILABLE_MESSAGE = b'#dialogs:clan_data_not_available/message'
    CLAN_DATA_NOT_AVAILABLE_CANCEL = b'#dialogs:clan_data_not_available/cancel'
    SOUNDSPEAKERSPRESETDOESNOTMATCH_TITLE = b'#dialogs:soundSpeakersPresetDoesNotMatch/title'
    SOUNDSPEAKERSPRESETDOESNOTMATCH_MESSAGE = b'#dialogs:soundSpeakersPresetDoesNotMatch/message'
    SOUNDSPEAKERSPRESETDOESNOTMATCH_SUBMIT = b'#dialogs:soundSpeakersPresetDoesNotMatch/submit'
    SOUNDSPEAKERSPRESETDOESNOTMATCH_CANCEL = b'#dialogs:soundSpeakersPresetDoesNotMatch/cancel'
    SOUNDSPEAKERSPRESETRESET_TITLE = b'#dialogs:soundSpeakersPresetReset/title'
    SOUNDSPEAKERSPRESETRESET_MESSAGE = b'#dialogs:soundSpeakersPresetReset/message'
    SOUNDSPEAKERSPRESETRESET_SUBMIT = b'#dialogs:soundSpeakersPresetReset/submit'
    SOUNDSPEAKERSPRESETRESET_CANCEL = b'#dialogs:soundSpeakersPresetReset/cancel'
    STRONGHOLD_LEAVE_TITLE = b'#dialogs:stronghold/leave/title'
    STRONGHOLD_LEAVE_MESSAGE = b'#dialogs:stronghold/leave/message'
    STRONGHOLD_LEAVEDEFEAT_TITLE = b'#dialogs:stronghold/leaveDefeat/title'
    STRONGHOLD_LEAVEDEFEAT_MESSAGE = b'#dialogs:stronghold/leaveDefeat/message'
    STRONGHOLD_LEAVE_SUBMIT = b'#dialogs:stronghold/leave/submit'
    STRONGHOLD_LEAVE_CANCEL = b'#dialogs:stronghold/leave/cancel'
    TRADEINCONFIRMATION_TITLE = b'#dialogs:tradeInConfirmation/title'
    TRADEINCONFIRMATION_MESSAGE = b'#dialogs:tradeInConfirmation/message'
    TRADEINCONFIRMATION_MESSAGE_ADDITION = b'#dialogs:tradeInConfirmation/message/addition'
    TRADEINCONFIRMATION_MESSAGE_CREW = b'#dialogs:tradeInConfirmation/message/crew'
    TRADEINCONFIRMATION_MESSAGE_SHELLS = b'#dialogs:tradeInConfirmation/message/shells'
    TRADEINCONFIRMATION_MESSAGE_EQUIPMENTS = b'#dialogs:tradeInConfirmation/message/equipments'
    TRADEINCONFIRMATION_MESSAGE_OPTIONALDEVICES = b'#dialogs:tradeInConfirmation/message/optionalDevices'
    TRADEINCONFIRMATION_MESSAGE_PAIRMODIFICATIONS = b'#dialogs:tradeInConfirmation/message/pairModifications'
    TRADEINCONFIRMATION_SUBMIT = b'#dialogs:tradeInConfirmation/submit'
    TRADEINCONFIRMATION_CANCEL = b'#dialogs:tradeInConfirmation/cancel'
    VEHCONF_EXITDIALOG_TITLE = b'#dialogs:vehConf/exitDialog/title'
    VEHCONF_EXITDIALOG_MESSAGE = b'#dialogs:vehConf/exitDialog/message'
    VEHCONF_EXITDIALOG_SUBMIT = b'#dialogs:vehConf/exitDialog/submit'
    VEHCONF_EXITDIALOG_CANCEL = b'#dialogs:vehConf/exitDialog/cancel'
    CONFIRMBATTLEBOOSTERINSTALL_TITLE = b'#dialogs:confirmBattleBoosterInstall/title'
    CONFIRMBATTLEBOOSTERINSTALL_MESSAGE = b'#dialogs:confirmBattleBoosterInstall/message'
    CONFIRMBATTLEBOOSTERINSTALL_SUBMIT = b'#dialogs:confirmBattleBoosterInstall/submit'
    CONFIRMBATTLEBOOSTERINSTALL_CANCEL = b'#dialogs:confirmBattleBoosterInstall/cancel'
    CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_TITLE = b'#dialogs:confirmBattleBoosterInstallNotSuitable/title'
    CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_MESSAGE = b'#dialogs:confirmBattleBoosterInstallNotSuitable/message'
    CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_SUBMIT = b'#dialogs:confirmBattleBoosterInstallNotSuitable/submit'
    CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_CANCEL = b'#dialogs:confirmBattleBoosterInstallNotSuitable/cancel'
    CONFIRMBATTLEBOOSTERBUYANDINSTALL_TITLE = b'#dialogs:confirmBattleBoosterBuyAndInstall/title'
    CONFIRMBATTLEBOOSTERBUYANDINSTALL_SUBMIT = b'#dialogs:confirmBattleBoosterBuyAndInstall/submit'
    CONFIRMBATTLEBOOSTERBUYANDINSTALL_CANCEL = b'#dialogs:confirmBattleBoosterBuyAndInstall/cancel'
    BOOTCAMP_PREMIUMTYPE_BASIC = b'#dialogs:bootcamp/premiumType/basic'
    BOOTCAMP_PREMIUMTYPE_PLUS = b'#dialogs:bootcamp/premiumType/plus'
    BOOTCAMP_SKIP_TITLE = b'#dialogs:bootcamp/skip/title'
    BOOTCAMP_SKIP_LABEL = b'#dialogs:bootcamp/skip/label'
    BOOTCAMP_SKIP_MESSAGE = b'#dialogs:bootcamp/skip/message'
    BOOTCAMP_SKIP_SUBMIT = b'#dialogs:bootcamp/skip/submit'
    BOOTCAMP_SKIP_CANCEL = b'#dialogs:bootcamp/skip/cancel'
    BOOTCAMP_SKIP_REFERRAL_TITLE = b'#dialogs:bootcamp/skip/referral/title'
    BOOTCAMP_SKIP_REFERRAL_LABEL = b'#dialogs:bootcamp/skip/referral/label'
    BOOTCAMP_SKIP_REFERRAL_MESSAGE = b'#dialogs:bootcamp/skip/referral/message'
    BOOTCAMP_SKIP_REFERRAL_SUBMIT = b'#dialogs:bootcamp/skip/referral/submit'
    BOOTCAMP_SKIP_REFERRAL_CANCEL = b'#dialogs:bootcamp/skip/referral/cancel'
    BOOTCAMP_START_TITLE = b'#dialogs:bootcamp/start/title'
    BOOTCAMP_START_LABEL = b'#dialogs:bootcamp/start/label'
    BOOTCAMP_START_MESSAGE = b'#dialogs:bootcamp/start/message'
    BOOTCAMP_START_SUBMIT = b'#dialogs:bootcamp/start/submit'
    BOOTCAMP_START_CANCEL = b'#dialogs:bootcamp/start/cancel'
    BOOTCAMP_RETRY_TITLE = b'#dialogs:bootcamp/retry/title'
    BOOTCAMP_RETRY_LABEL = b'#dialogs:bootcamp/retry/label'
    BOOTCAMP_RETRY_MESSAGE = b'#dialogs:bootcamp/retry/message'
    BOOTCAMP_RETRY_SUBMIT = b'#dialogs:bootcamp/retry/submit'
    BOOTCAMP_RETRY_CANCEL = b'#dialogs:bootcamp/retry/cancel'
    BOOTCAMPCENTERUNAVAILABLE_TITLE = b'#dialogs:bootcampCenterUnavailable/title'
    BOOTCAMPCENTERUNAVAILABLE_MESSAGE = b'#dialogs:bootcampCenterUnavailable/message'
    BOOTCAMPCENTERUNAVAILABLE_CANCEL = b'#dialogs:bootcampCenterUnavailable/cancel'
    HOF_EXCLUDERATING_TITLE = b'#dialogs:hof/excludeRating/title'
    HOF_EXCLUDERATING_MESSAGE = b'#dialogs:hof/excludeRating/message'
    HOF_EXCLUDERATING_SUBMIT = b'#dialogs:hof/excludeRating/submit'
    HOF_EXCLUDERATING_CANCEL = b'#dialogs:hof/excludeRating/cancel'
    HOFDISABLED_TITLE = b'#dialogs:hofDisabled/title'
    HOFDISABLED_MESSAGE = b'#dialogs:hofDisabled/message'
    HOFDISABLED_CANCEL = b'#dialogs:hofDisabled/cancel'
    CUSTOMIZATIONCONFIRMSELL_TITLE = b'#dialogs:customizationConfirmSell/title'
    CUSTOMIZATIONCONFIRMSELL_MESSAGE = b'#dialogs:customizationConfirmSell/message'
    LEAVEEVENT_TITLE = b'#dialogs:leaveEvent/title'
    LEAVEEVENT_MESSAGE = b'#dialogs:leaveEvent/message'
    LEAVEEVENT_SUBMIT = b'#dialogs:leaveEvent/submit'
    LEAVEEVENT_CANCEL = b'#dialogs:leaveEvent/cancel'
    LEAVESTARTEDEVENT_TITLE = b'#dialogs:leaveStartedEvent/title'
    LEAVESTARTEDEVENT_MESSAGE = b'#dialogs:leaveStartedEvent/message'
    LEAVESTARTEDEVENT_SUBMIT = b'#dialogs:leaveStartedEvent/submit'
    LEAVESTARTEDEVENT_CANCEL = b'#dialogs:leaveStartedEvent/cancel'
    LEAVEEVENT_MESSAGE_WARNING = b'#dialogs:leaveEvent/message/warning'
    GAMMADIALOG_TITLE = b'#dialogs:gammaDialog/title'
    GAMMADIALOG_MESSAGE_HEADER = b'#dialogs:gammaDialog/message/header'
    GAMMADIALOG_MESSAGE_DESCRIPTION = b'#dialogs:gammaDialog/message/description'
    GAMMADIALOG_CANCEL = b'#dialogs:gammaDialog/cancel'
    REFERRALREWARD_TITLE = b'#dialogs:referralReward/title'
    REFERRALREWARD_MESSAGE = b'#dialogs:referralReward/message'
    REFERRALREWARD_SUBMIT = b'#dialogs:referralReward/submit'
    REFERRALREWARD_CANCEL = b'#dialogs:referralReward/cancel'
    SESSIONSTATS_CONFIRMRESET_TITLE = b'#dialogs:sessionStats/confirmReset/title'
    SESSIONSTATS_CONFIRMRESET_MESSAGE = b'#dialogs:sessionStats/confirmReset/message'
    SESSIONSTATS_CONFIRMRESET_TIME = b'#dialogs:sessionStats/confirmReset/time'
    SESSIONSTATS_CONFIRMRESET_SUBMIT = b'#dialogs:sessionStats/confirmReset/submit'
    SESSIONSTATS_CONFIRMRESET_CANCEL = b'#dialogs:sessionStats/confirmReset/cancel'
    EDITABLESTYLES_CONFIRMRESET_TITLE = b'#dialogs:editableStyles/confirmReset/title'
    EDITABLESTYLES_CONFIRMRESET_MESSAGE = b'#dialogs:editableStyles/confirmReset/message'
    EDITABLESTYLES_CONFIRMRESET_FORMATTEDPARTOFMESSAGE = b'#dialogs:editableStyles/confirmReset/formattedPartOfMessage'
    EDITABLESTYLES_CONFIRMRESET_CHECKBOXLABEL = b'#dialogs:editableStyles/confirmReset/checkboxLabel'
    EDITABLESTYLES_CONFIRMRESET_SUBMIT = b'#dialogs:editableStyles/confirmReset/submit'
    EDITABLESTYLES_CONFIRMRESET_CANCEL = b'#dialogs:editableStyles/confirmReset/cancel'
    CONFIRMEQUIPMENTBUYINSTALL_SUBMIT = b'#dialogs:confirmEquipmentBuyInstall/submit'
    EQUIPMENTPURCASE_CONFORMATION_ALL = b'#dialogs:equipmentPurcase/conformation/all'
    EQUIPMENTBUYINSTALL_PRICE = b'#dialogs:equipmentBuyInstall/price'
    BUYCONFIRMATION_STRINGEQUIPMENT_SUBMIT = b'#dialogs:buyConfirmation/stringEquipment/submit'
    CONFIRMEQUIPMENTINSTALL_SUBMIT = b'#dialogs:confirmEquipmentInstall/submit'
    EQUIPMENTDESTROY_CONFORMATION = b'#dialogs:equipmentDestroy/conformation'
    EQUIPMENTDESTROY_WARNINGMSG = b'#dialogs:equipmentDestroy/warningMsg'
    EQUIPMENTSALE_CONFORMATION_HEADER = b'#dialogs:equipmentSale/conformation/header'
    EQUIPMENTDECONSTRUCT_CONFIRMATION_HEADER = b'#dialogs:equipmentDeconstruct/confirmation/header'
    MODULESALE_CONFORMATION_HEADER = b'#dialogs:moduleSale/conformation/header'
    ELEMENTTYPE_GUN = b'#dialogs:elementType/gun'
    ELEMENTTYPE_TURRET = b'#dialogs:elementType/turret'
    ELEMENTTYPE_ENGINE = b'#dialogs:elementType/engine'
    ELEMENTTYPE_CHASSIS = b'#dialogs:elementType/chassis'
    ELEMENTTYPE_RADIOSTATION = b'#dialogs:elementType/radiostation'
    SELLSHELLCONFIRMATION_SUBMIT = b'#dialogs:sellShellConfirmation/submit'
    EQUIPMENTDESTROY_DEMOUNTOPTIONS_GOLDORDEMOKIT = b'#dialogs:equipmentDestroy/DemountOptions/goldOrDemoKit'
    EQUIPMENTDESTROY_DEMOUNTOPTIONS_BONDS = b'#dialogs:equipmentDestroy/DemountOptions/bonds'
    DAILYQUESTS_DIALOGINFOCONFIRMREROLL_TITLE = b'#dialogs:dailyQuests/dialogInfoConfirmReroll/title'
    DAILYQUESTS_DIALOGINFOCONFIRMREROLL_MESSAGE = b'#dialogs:dailyQuests/dialogInfoConfirmReroll/message'
    DAILYQUESTS_DIALOGINFOCONFIRMREROLL_SUBMIT = b'#dialogs:dailyQuests/dialogInfoConfirmReroll/submit'
    DAILYQUESTS_DIALOGCONFIRMREROLL_TIMELIMITMSGHOURS = b'#dialogs:dailyQuests/dialogConfirmReroll/timeLimitMsgHours'
    DAILYQUESTS_DIALOGCONFIRMREROLL_TIMELIMITMSGHOURSMINS = b'#dialogs:dailyQuests/dialogConfirmReroll/timeLimitMsgHoursMins'
    DAILYQUESTS_DIALOGCONFIRMREROLL_TIMELIMITMSGMINS = b'#dialogs:dailyQuests/dialogConfirmReroll/timeLimitMsgMins'
    DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_TITLE = b'#dialogs:dailyQuests/dialogWarningConfirmReroll/title'
    DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_MESSAGE = b'#dialogs:dailyQuests/dialogWarningConfirmReroll/message'
    DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_SUBMIT = b'#dialogs:dailyQuests/dialogWarningConfirmReroll/submit'
    DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_WARNING = b'#dialogs:dailyQuests/dialogWarningConfirmReroll/warning'
    SQUAD_EVENTDISABLED_TITLE = b'#dialogs:squad/eventDisabled/title'
    SQUAD_EVENTDISABLED_MESSAGE = b'#dialogs:squad/eventDisabled/message'
    SQUAD_EVENTDISABLED_CANCEL = b'#dialogs:squad/eventDisabled/cancel'
    DEDICATION_HEADLINE = b'#dialogs:dedication/headline'
    DEDICATION_SUB_HEADLINE = b'#dialogs:dedication/sub-headline'
    BATTLEROYALE_PREBATTLE_TITLE = b'#dialogs:battleRoyale/preBattle/title'
    BATTLEROYALE_PREBATTLE_MESSAGE = b'#dialogs:battleRoyale/preBattle/message'
    BATTLEROYALE_PREBATTLE_SUBMIT = b'#dialogs:battleRoyale/preBattle/submit'
    BATTLEROYALE_PREBATTLE_CANCEL = b'#dialogs:battleRoyale/preBattle/cancel'
    ACCOUNTCOMPLETION_SUBMIT = b'#dialogs:accountCompletion/submit'
    ACCOUNTCOMPLETION_CANCEL = b'#dialogs:accountCompletion/cancel'
    ACCOUNTCOMPLETION_WARNINGSERVERUNAVAILABLETIMED = b'#dialogs:accountCompletion/warningServerUnavailableTimed'
    ACCOUNTCOMPLETION_WARNINGSERVERUNAVAILABLE = b'#dialogs:accountCompletion/warningServerUnavailable'
    ACCOUNTCOMPLETION_WARNINGSOMETHINGWENTWRONG = b'#dialogs:accountCompletion/warningSomethingWentWrong'
    ACCOUNTCOMPLETION_ERRORISWRONG = b'#dialogs:accountCompletion/errorIsWrong'
    ACCOUNTCOMPLETION_EMAILFORBIDDEN = b'#dialogs:accountCompletion/emailForbidden'
    ACCOUNTCOMPLETION_EMAILPROVIDERBANNED = b'#dialogs:accountCompletion/emailProviderBanned'
    ACCOUNTCOMPLETION_EMAILRESTRICTEDBYCOUNTRYHEADER = b'#dialogs:accountCompletion/emailRestrictedByCountryHeader'
    ACCOUNTCOMPLETION_EMAILRESTRICTEDBYCOUNTRY = b'#dialogs:accountCompletion/emailRestrictedByCountry'
    ACCOUNTCOMPLETION_EMAILALREADYTAKEN = b'#dialogs:accountCompletion/emailAlreadyTaken'
    ACCOUNTCOMPLETION_LOGINALREADYTAKEN = b'#dialogs:accountCompletion/loginAlreadyTaken'
    ACCOUNTCOMPLETION_ACCOUNTALREADYHASEMAIL = b'#dialogs:accountCompletion/accountAlreadyHasEmail'
    ACCOUNTCOMPLETION_EMAILISTOOSHORT = b'#dialogs:accountCompletion/emailIsTooShort'
    ACCOUNTCOMPLETION_EMAILISTOOLONG = b'#dialogs:accountCompletion/emailIsTooLong'
    ACCOUNTCOMPLETION_TOOMANYREQUESTS = b'#dialogs:accountCompletion/tooManyRequests'
    ACCOUNTCOMPLETION_REWARDSTITLE = b'#dialogs:accountCompletion/rewardsTitle'
    ACCOUNTCOMPLETION_REGISTRATIONREWARDSTITLE = b'#dialogs:accountCompletion/registrationRewardsTitle'
    ACCOUNTCOMPLETION_EMAIL_FIELDNAME = b'#dialogs:accountCompletion/email/fieldName'
    ACCOUNTCOMPLETION_EMAIL_FIELDPLACEHOLDER = b'#dialogs:accountCompletion/email/fieldPlaceholder'
    ACCOUNTCOMPLETION_PASSWORD_FIELDNAME = b'#dialogs:accountCompletion/password/fieldName'
    ACCOUNTCOMPLETION_EMAIL_TITLE = b'#dialogs:accountCompletion/email/title'
    ACCOUNTCOMPLETION_EMAIL_SUBTITLE = b'#dialogs:accountCompletion/email/subTitle'
    ACCOUNTCOMPLETION_EMAIL_FULLACCESS_TITLE = b'#dialogs:accountCompletion/email/fullAccess/title'
    ACCOUNTCOMPLETION_EMAIL_FULLACCESS_SUBTITLE = b'#dialogs:accountCompletion/email/fullAccess/subTitle'
    ACCOUNTCOMPLETION_ACTIVATE_TITLE = b'#dialogs:accountCompletion/activate/title'
    ACCOUNTCOMPLETION_ACTIVATE_TEXT = b'#dialogs:accountCompletion/activate/text'
    ACCOUNTCOMPLETION_ACTIVATE_KEYERROR = b'#dialogs:accountCompletion/activate/keyError'
    ACCOUNTCOMPLETION_ACTIVATE_MISSPELL = b'#dialogs:accountCompletion/activate/misspell'
    ACCOUNTCOMPLETION_ACTIVATE_TOOMANYINCORRECTTRIES = b'#dialogs:accountCompletion/activate/tooManyIncorrectTries'
    ACCOUNTCOMPLETION_ACTIVATE_KEYDIED = b'#dialogs:accountCompletion/activate/keyDied'
    ACCOUNTCOMPLETION_ACTIVATE_ENTERCREDENTIALSAGAIN = b'#dialogs:accountCompletion/activate/enterCredentialsAgain'
    ACCOUNTCOMPLETION_ACTIVATE_BUTTON = b'#dialogs:accountCompletion/activate/button'
    ACCOUNTCOMPLETION_ACTIVATE_COUNDOWNTEXT = b'#dialogs:accountCompletion/activate/coundownText'
    ACCOUNTCOMPLETION_ALREADYLINKED_TITLE = b'#dialogs:accountCompletion/alreadyLinked/title'
    ACCOUNTCOMPLETION_ALREADYLINKED_SUBTITLE = b'#dialogs:accountCompletion/alreadyLinked/subTitle'
    ACCOUNTCOMPLETION_EMAILOVERLAY_ERROR_CODEALREADYSENT = b'#dialogs:accountCompletion/emailOverlay/error/codeAlreadySent'
    ACCOUNTCOMPLETION_EMAILOVERLAY_ALREADYCONFIRMED_TITLE = b'#dialogs:accountCompletion/emailOverlay/alreadyConfirmed/title'
    ACCOUNTCOMPLETION_EMAILOVERLAY_ALREADYCONFIRMED_SUBTITLE = b'#dialogs:accountCompletion/emailOverlay/alreadyConfirmed/subTitle'
    ACCOUNTCOMPLETION_CREDENTIALS_TITLE = b'#dialogs:accountCompletion/credentials/title'
    ACCOUNTCOMPLETION_CREDENTIALS_SUBTITLE = b'#dialogs:accountCompletion/credentials/subTitle'
    ACCOUNTCOMPLETION_BADPASSWORD = b'#dialogs:accountCompletion/badPassword'
    ACCOUNTCOMPLETION_PASSWORDISTOOSHORT = b'#dialogs:accountCompletion/passwordIsTooShort'
    ACCOUNTCOMPLETION_PASSWORDISTOOLONG = b'#dialogs:accountCompletion/passwordIsTooLong'
    ACCOUNTCOMPLETION_PASSWORDISWEAK = b'#dialogs:accountCompletion/passwordIsWeak'
    ACCOUNTCOMPLETION_DEMOCOMPLETE_TITLE = b'#dialogs:accountCompletion/demoComplete/title'
    ACCOUNTCOMPLETION_DEMOCOMPLETE_DESCRIPTION = b'#dialogs:accountCompletion/demoComplete/description'
    ACCOUNTCOMPLETION_DEMOCOMPLETE_BUTTON = b'#dialogs:accountCompletion/demoComplete/button'
    ACCOUNTCOMPLETION_ERROR_NOTAVAILABLE = b'#dialogs:accountCompletion/error/notAvailable'
    ACCOUNTCOMPLETION_ERROR_BUTTON_TRYAGAIN = b'#dialogs:accountCompletion/error/button/tryAgain'
    ACCOUNTCOMPLETION_ERROR_TRYAGAINTIMERMESSAGE = b'#dialogs:accountCompletion/error/tryAgainTimerMessage'
    ACCOUNTCOMPLETION_ERROR_BUTTON_CONTINUE = b'#dialogs:accountCompletion/error/button/continue'
    ACCOUNTCOMPLETION_ERROR_RENAMINGNOTAVAILABLE = b'#dialogs:accountCompletion/error/renamingNotAvailable'
    ACCOUNTCOMPLETION_WAITING_CONFIRMATION = b'#dialogs:accountCompletion/waiting/confirmation'
    ACCOUNTCOMPLETION_WAITING_QUEUE = b'#dialogs:accountCompletion/waiting/queue'
    ACCOUNTCOMPLETION_CONTACTSUPPORT = b'#dialogs:accountCompletion/contactSupport'
    ACCOUNTCOMPLETION_ERROR_SOMETHINGWENTWRONG = b'#dialogs:accountCompletion/error/somethingWentWrong'
    ACCOUNTCOMPLETION_ERROR_RENAMINGMALFUNCTION = b'#dialogs:accountCompletion/error/renamingMalfunction'
    ACCOUNTCOMPLETION_SPA_PASSWORDISWEAK = b'#dialogs:accountCompletion/spa/passwordIsWeak'
    ACCOUNTCOMPLETION_LEAVESQUAD_TITLE = b'#dialogs:accountCompletion/leaveSquad/title'
    ACCOUNTCOMPLETION_LEAVESQUAD_MESSAGE = b'#dialogs:accountCompletion/leaveSquad/message'
    ACCOUNTCOMPLETION_LEAVESQUAD_SUBMIT = b'#dialogs:accountCompletion/leaveSquad/submit'
    ACCOUNTCOMPLETION_LEAVESQUAD_CANCEL = b'#dialogs:accountCompletion/leaveSquad/cancel'
    ACCOUNTCOMPLETION_RENAMING_SKIP_TITLE = b'#dialogs:accountCompletion/renaming/skip/title'
    ACCOUNTCOMPLETION_RENAMING_SKIP_MESSAGE = b'#dialogs:accountCompletion/renaming/skip/message'
    ACCOUNTCOMPLETION_RENAMING_SKIP_SUBMIT = b'#dialogs:accountCompletion/renaming/skip/submit'
    ACCOUNTCOMPLETION_RENAMING_SKIP_CANCEL = b'#dialogs:accountCompletion/renaming/skip/cancel'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_TITLE = b'#dialogs:accountCompletion/renamingOverlay/title'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_SUBTITLE = b'#dialogs:accountCompletion/renamingOverlay/subTitle'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_BUTTON = b'#dialogs:accountCompletion/renamingOverlay/button'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_FIELDNAME = b'#dialogs:accountCompletion/renamingOverlay/fieldName'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMEFORBIDDEN = b'#dialogs:accountCompletion/renamingOverlay/nameForbidden'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMEFORBIDDENPICKVARIANT = b'#dialogs:accountCompletion/renamingOverlay/nameForbiddenPickVariant'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETAKEN = b'#dialogs:accountCompletion/renamingOverlay/nameTaken'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETAKENPICKVARIANT = b'#dialogs:accountCompletion/renamingOverlay/nameTakenPickVariant'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMEINVALID = b'#dialogs:accountCompletion/renamingOverlay/nameInvalid'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETOOSHORT = b'#dialogs:accountCompletion/renamingOverlay/nameTooShort'
    ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETOOLONG = b'#dialogs:accountCompletion/renamingOverlay/nameToolong'
    ACCOUNTCOMPLETION_RENAMINGCOMPLETEOVERLAY_TITLE = b'#dialogs:accountCompletion/renamingCompleteOverlay/title'
    ACCOUNTCOMPLETION_RENAMINGCOMPLETEOVERLAY_SUBTITLE = b'#dialogs:accountCompletion/renamingCompleteOverlay/subTitle'
    DIALOGTEMPLATES_CONFIRM = b'#dialogs:dialogTemplates/confirm'
    DIALOGTEMPLATES_CANCEL = b'#dialogs:dialogTemplates/cancel'
    DIALOGTEMPLATES_OK = b'#dialogs:dialogTemplates/ok'
    BATTLEROYALE_CONFIRMRENT_TESTDRIVE_BUTTON = b'#dialogs:battleRoyale/confirmRent/testDrive/Button'
    BATTLEROYALE_CONFIRMRENT_TESTDRIVE_TITLE = b'#dialogs:battleRoyale/confirmRent/testDrive/Title'
    BATTLEROYALE_CONFIRMRENT_TESTDRIVE_DESCRIPTION = b'#dialogs:battleRoyale/confirmRent/testDrive/Description'
    BATTLEROYALE_CONFIRMRENT_RENT_BUTTON = b'#dialogs:battleRoyale/confirmRent/rent/Button'
    BATTLEROYALE_CONFIRMRENT_RENT_TITLE = b'#dialogs:battleRoyale/confirmRent/rent/Title'
    BATTLEROYALE_CONFIRMRENT_RENT_DESCRIPTION = b'#dialogs:battleRoyale/confirmRent/rent/Description'
    BATTLEROYALE_CONFIRMRENT_RENTPRICE = b'#dialogs:battleRoyale/confirmRent/rentPrice'
    BATTLEROYALE_CONFIRMRENT_EVENTENDSSOON = b'#dialogs:battleRoyale/confirmRent/eventEndsSoon'
    FREESKILLSLEARNING_TITLE_LEARNING = b'#dialogs:freeSkillsLearning/title/learning'
    FREESKILLSLEARNING_TITLE_RELEARNING = b'#dialogs:freeSkillsLearning/title/relearning'
    FREESKILLSLEARNING_MESSAGE = b'#dialogs:freeSkillsLearning/message'
    PERKLEARNCONFIRM_TITLE = b'#dialogs:perkLearnConfirm/title'
    PERKLEARNCONFIRM_DESC = b'#dialogs:perkLearnConfirm/desc'
    PERKLEARNCONFIRM_LEARN = b'#dialogs:perkLearnConfirm/learn'
    COMP7_DESERTER_TITLE = b'#dialogs:comp7/deserter/title'
    COMP7_DESERTER_MSGTITLE = b'#dialogs:comp7/deserter/msgTitle'
    COMP7_DESERTER_MESSAGE = b'#dialogs:comp7/deserter/message'
    COMP7_DESERTER_SUBMIT = b'#dialogs:comp7/deserter/submit'
    COMP7_DESERTER_CANCEL = b'#dialogs:comp7/deserter/cancel'
    COMP7_PUNISHMENTWINDOW_TITLE = b'#dialogs:comp7/punishmentWindow/title'
    COMP7_PUNISHMENTWINDOW_MSGTITLE = b'#dialogs:comp7/punishmentWindow/msgTitle'
    COMP7_PUNISHMENTWINDOW_MESSAGE = b'#dialogs:comp7/punishmentWindow/message'
    COMP7_PUNISHMENTWINDOW_CANCEL = b'#dialogs:comp7/punishmentWindow/cancel'
    EQUIPMENTUPGRADE_CONFIRMBUTTON = b'#dialogs:equipmentUpgrade/confirmButton'
    EQUIPMENTUPGRADE_GETMORECURRENCYBUTTON = b'#dialogs:equipmentUpgrade/getMoreCurrencyButton'
    EQUIPMENTUPGRADE_GETMORECURRENCYBUTTONTOOLTIP_BODY = b'#dialogs:equipmentUpgrade/getMoreCurrencyButtonTooltip/body'
    EQUIPMENTUPGRADE_CANCELBUTTON = b'#dialogs:equipmentUpgrade/cancelButton'
    EQUIPMENTDECONSTRUCTION_CONFIRMBUTTON = b'#dialogs:equipmentDeconstruction/confirmButton'
    EQUIPMENTDECONSTRUCTION_CONFIRMANDUPGRADEBUTTON = b'#dialogs:equipmentDeconstruction/confirmAndUpgradeButton'
    EQUIPMENTDECONSTRUCTION_CANCELBUTTON = b'#dialogs:equipmentDeconstruction/cancelButton'
    PRICECARD_FREE_TITLE = b'#dialogs:priceCard/free/title'
    PRICECARD_CREDITS_TITLE = b'#dialogs:priceCard/credits/title'
    PRICECARD_GOLD_TITLE = b'#dialogs:priceCard/gold/title'
    PRICECARD_RECERTIFICATION_TITLE = b'#dialogs:priceCard/recertification/title'
    PRICECARD_PRICE_FREE = b'#dialogs:priceCard/price/free'
    PERKSREST_TITLE = b'#dialogs:perksRest/title'
    PERKSREST_FREE_DESCRIPTION = b'#dialogs:perksRest/free/description'
    PERKSREST_BEFORE = b'#dialogs:perksRest/before'
    PERKSREST_AFTER = b'#dialogs:perksRest/after'
    PERKSREST_NONEWPERKS = b'#dialogs:perksRest/noNewPerks'
    PERKSREST_SUBMIT = b'#dialogs:perksRest/submit'
    PERKSREST_CANCEL = b'#dialogs:perksRest/cancel'
    PERKSREST_PRICECARD_FREE_DESCRIPTION = b'#dialogs:perksRest/priceCard/free/description'
    PERKSREST_PRICECARD_CREDITS_DESCRIPTION = b'#dialogs:perksRest/priceCard/credits/description'
    PERKSREST_PRICECARD_GOLD_DESCRIPTION = b'#dialogs:perksRest/priceCard/gold/description'
    RETRAIN_HEADER = b'#dialogs:retrain/header'
    RETRAIN_TITLE_SINGLE = b'#dialogs:retrain/title/single'
    RETRAIN_TITLE_MASSIVE = b'#dialogs:retrain/title/massive'
    RETRAIN_WARNING_PREMIUMVEHICLE = b'#dialogs:retrain/warning/premiumVehicle'
    RETRAIN_PRICECARD_FREE_DESCRIPTION = b'#dialogs:retrain/priceCard/free/description'
    RETRAIN_PRICECARD_CREDITS_DESCRIPTION = b'#dialogs:retrain/priceCard/credits/description'
    RETRAIN_PRICECARD_GOLD_DESCRIPTION = b'#dialogs:retrain/priceCard/gold/description'
    RETRAIN_MASSIVE_TANKMENCOUNT = b'#dialogs:retrain/massive/tankmenCount'
    RETRAIN_SINGLE_CHECKBOXLABEL = b'#dialogs:retrain/single/checkBoxLabel'
    RETRAIN_PRICE = b'#dialogs:retrain/price'
    RETRAIN_SUBMIT = b'#dialogs:retrain/submit'
    RETRAIN_CANCEL = b'#dialogs:retrain/cancel'
    RECRUIT_TITLE = b'#dialogs:recruit/title'
    RECRUIT_WARNING_PREMIUMVEHICLE = b'#dialogs:recruit/warning/premiumVehicle'
    RECRUIT_PRICECARD_FREE_DESCRIPTION = b'#dialogs:recruit/priceCard/free/description'
    RECRUIT_PRICECARD_CREDITS_DESCRIPTION = b'#dialogs:recruit/priceCard/credits/description'
    RECRUIT_PRICECARD_GOLD_DESCRIPTION = b'#dialogs:recruit/priceCard/gold/description'
    RECRUIT_SUBMIT = b'#dialogs:recruit/submit'
    RECRUIT_CANCEL = b'#dialogs:recruit/cancel'
    TANKMANRETRAINING_SUBMIT = b'#dialogs:tankmanRetraining/submit'
    TANKMANRETRAINING_CANCEL = b'#dialogs:tankmanRetraining/cancel'
    CREWMEMBERTANKCHANGE_TITLE = b'#dialogs:crewMemberTankChange/title'
    CREWMEMBERTANKCHANGE_DESC = b'#dialogs:crewMemberTankChange/desc'
    CREWMEMBERTANKCHANGE_TRANSFER = b'#dialogs:crewMemberTankChange/transfer'
    CREWMEMBERROLECHANGE_TITLE_SIMPLE = b'#dialogs:crewMemberRoleChange/title/simple'
    CREWMEMBERROLECHANGE_TITLE_EXTENDED = b'#dialogs:crewMemberRoleChange/title/extended'
    CREWMEMBERROLECHANGE_BULLET = b'#dialogs:crewMemberRoleChange/bullet'
    CREWMEMBERROLECHANGE_DESC_SIMPLE = b'#dialogs:crewMemberRoleChange/desc/simple'
    CREWMEMBERROLECHANGE_DESC_WRONGSPECIALIZATION = b'#dialogs:crewMemberRoleChange/desc/wrongSpecialization'
    CREWMEMBERROLECHANGE_DESC_PREMIUM = b'#dialogs:crewMemberRoleChange/desc/premium'
    CREWMEMBERROLECHANGE_PRICE = b'#dialogs:crewMemberRoleChange/price'
    CREWMEMBERROLECHANGE_CHANGE = b'#dialogs:crewMemberRoleChange/change'
    RUDYINFO_TITLE = b'#dialogs:rudyInfo/title'
    RUDYINFO_MESSAGE = b'#dialogs:rudyInfo/message'
    RUDYINFO_SUBMIT = b'#dialogs:rudyInfo/submit'
    CREWBOOKPURCHASE_PURCHASE = b'#dialogs:crewBookPurchase/purchase'
    CREWBOOKPURCHASE_PURCHASE_TITLE = b'#dialogs:crewBookPurchase/purchase/title'
    CREWBOOKPURCHASE_DESCRIPTION_PERSONAL = b'#dialogs:crewBookPurchase/description/personal'
    CREWBOOKPURCHASE_DESCRIPTION_CREW = b'#dialogs:crewBookPurchase/description/crew'
    CREWBOOKPURCHASE_BTNDISABLEDTOOLTIP = b'#dialogs:crewBookPurchase/btnDisabledTooltip'
    SKINCHANGEDIALOG_TITLE = b'#dialogs:skinChangeDialog/title'
    SKINCHANGEDIALOG_BUTTON_SUBMIT = b'#dialogs:skinChangeDialog/button/submit'
    SKINCHANGEDIALOG_TEXT = b'#dialogs:skinChangeDialog/text'
    SKINCHANGEDIALOG_WARNING = b'#dialogs:skinChangeDialog/warning'
    SKINAPPLYDIALOG_BUTTON_SUBMIT = b'#dialogs:skinApplyDialog/button/submit'
    SKINAPPLYDIALOG_WARNING = b'#dialogs:skinApplyDialog/warning'
    DISMISSTANKMAN_HEADER = b'#dialogs:dismissTankman/header'
    DISMISSTANKMAN_DESCRIPTION_TIME = b'#dialogs:dismissTankman/description/time'
    DISMISSTANKMAN_DESCRIPTION_TIMETEXT = b'#dialogs:dismissTankman/description/timeText'
    DISMISSTANKMAN_LIMITED = b'#dialogs:dismissTankman/limited'
    DISMISSTANKMAN_NORECOVERY = b'#dialogs:dismissTankman/noRecovery'
    DISMISSTANKMAN_BUTTONS_DISMISS = b'#dialogs:dismissTankman/buttons/dismiss'
    DISMISSTANKMAN_BUTTONS_RESTORE = b'#dialogs:dismissTankman/buttons/restore'
    RESTORETANKMAN_HEADER = b'#dialogs:restoreTankman/header'
    RESTORETANKMAN_DESCRIPTION = b'#dialogs:restoreTankman/description'
    RESTORETANKMAN_PRICE = b'#dialogs:restoreTankman/price'
    RESTORETANKMAN_FREE = b'#dialogs:restoreTankman/free'
    RESTORETANKMAN_BUTTONS_RECOVER = b'#dialogs:restoreTankman/buttons/recover'
    DISMISSORRESTORE_HEADER_DISMISS = b'#dialogs:dismissOrRestore/header/dismiss'
    DISMISSORRESTORE_HEADER_RESTORE = b'#dialogs:dismissOrRestore/header/restore'
    DISMISSORRESTORE_SELECTTANKMANS_DISMISS = b'#dialogs:dismissOrRestore/selectTankmans/dismiss'
    DISMISSORRESTORE_SELECTTANKMANS_RESTORE = b'#dialogs:dismissOrRestore/selectTankmans/restore'
    DISMISSORRESTORE_RESTORE_CURRENCY = b'#dialogs:dismissOrRestore/restore/currency'
    DISMISSORRESTORE_DISMISS_CAPCHA_TITLE_NORMAL = b'#dialogs:dismissOrRestore/dismiss/capcha/title/normal'
    DISMISSORRESTORE_DISMISS_CAPCHA_TITLEHIGHLIGHT_NORMAL = b'#dialogs:dismissOrRestore/dismiss/capcha/titleHighlight/normal'
    DISMISSORRESTORE_ERROR_TEXT = b'#dialogs:dismissOrRestore/error/text'
    DISMISSORRESTORE_LIMITERROR_ERROR = b'#dialogs:dismissOrRestore/limitError/error'
    DISMISSORRESTORE_DISMISS_CAPCHA_TITLE_LIMITERROR = b'#dialogs:dismissOrRestore/dismiss/capcha/title/limitError'
    DISMISSORRESTORE_DISMISS_CAPCHA_TITLEHIGHLIGHT_LIMITERROR = b'#dialogs:dismissOrRestore/dismiss/capcha/titleHighlight/limitError'
    DISMISSORRESTORE_DISMISS_CAPCHA_TITLEHIGHLIGHTKEYWORD = b'#dialogs:dismissOrRestore/dismiss/capcha/titleHighlightKeyword'
    BUYBERTHSCONFIRMATION_MESSAGE = b'#dialogs:buyBerthsConfirmation/message'
    BUYBERTHSCONFIRMATION_TITLE = b'#dialogs:buyBerthsConfirmation/title'
    BUYBERTHSCONFIRMATION_SUBMIT = b'#dialogs:buyBerthsConfirmation/submit'
    BUYBERTHSCONFIRMATION_CANCEL = b'#dialogs:buyBerthsConfirmation/cancel'
    BUYBERTHSNOTENOUGH_CREDITS_TITLE = b'#dialogs:buyBerthsNotEnough/credits/title'
    BUYBERTHSNOTENOUGH_CREDITS_MESSAGE = b'#dialogs:buyBerthsNotEnough/credits/message'
    BUYBERTHSNOTENOUGH_CREDITS_CANCEL = b'#dialogs:buyBerthsNotEnough/credits/cancel'
    BUYBERTHS_HANGARBERTHS_HEADER = b'#dialogs:buyBerths/hangarBerths/header'
    VEHICLESELLDIALOG_VEHICLETYPE_ENUM = (
     VEHICLESELLDIALOG_VEHICLETYPE_LIGHTTANK,
     VEHICLESELLDIALOG_VEHICLETYPE_MEDIUMTANK,
     VEHICLESELLDIALOG_VEHICLETYPE_HEAVYTANK,
     VEHICLESELLDIALOG_VEHICLETYPE_SPG,
     VEHICLESELLDIALOG_VEHICLETYPE_AT_SPG)
    ALL_ENUM = (
     INTERVIEWQUIT_TITLE,
     INTERVIEWQUIT_MESSAGE,
     INTERVIEWQUIT_SUBMIT,
     INTERVIEWQUIT_CANCEL,
     SURVEYQUIT_TITLE,
     SURVEYQUIT_MESSAGE,
     SURVEYQUIT_SUBMIT,
     SURVEYQUIT_CANCEL,
     APPLICATIONQUIT_TITLE,
     APPLICATIONQUIT_MESSAGE,
     APPLICATIONQUIT_SUBMIT,
     APPLICATIONQUIT_CANCEL,
     LEGALINFOWINDOW_TITLE,
     COMMON_SUBMIT,
     COMMON_CANCEL,
     COMMON_CONFIRM_SUBMIT,
     COMMON_CONFIRM_CANCEL,
     COMMON_ERROR_CANCEL,
     COMMON_COST,
     DISCONNECT_TITLE,
     DISCONNECT_MESSAGE,
     DISCONNECT_SUBMIT,
     DISCONNECT_CANCEL,
     QUIT_TITLE,
     QUIT_SUBMIT,
     QUIT_CANCEL,
     QUITBATTLE_TITLE,
     QUITBATTLE_SUBMIT,
     QUITBATTLE_CANCEL,
     QUITBATTLE_LEAVER_TITLE,
     QUITBATTLE_LEAVER_SUBMIT,
     QUITBATTLE_LEAVER_CANCEL,
     QUITBATTLE_LEAVER_DESCRIPTIONALIVE,
     QUITBATTLE_IGR_LEAVER_TITLE,
     QUITBATTLE_IGR_LEAVER_SUBMIT,
     QUITBATTLE_IGR_LEAVER_CANCEL,
     QUITBATTLE_IGR_LEAVER_DESCRIPTIONALIVE,
     QUITBATTLE_REPLAY_TITLE,
     QUITBATTLE_REPLAY_SUBMIT,
     QUITBATTLE_REPLAY_CANCEL,
     QUITPREBATTLE_TITLE,
     QUITPREBATTLE_MESSAGE,
     QUITPREBATTLE_SUBMIT,
     QUITPREBATTLE_CANCEL,
     GRAPHICSPRESETRESTARTCONFIRMATION_TITLE,
     GRAPHICSPRESETRESTARTCONFIRMATION_MESSAGE,
     GRAPHICSPRESETRESTARTCONFIRMATION_SUBMIT,
     GRAPHICSPRESETRESTARTCONFIRMATION_DELAY,
     GRAPHICSPRESETRESTARTCONFIRMATION_CANCEL,
     GRAPHICSPRESETNOTINSTALLED_TITLE,
     GRAPHICSPRESETNOTINSTALLED_MESSAGE,
     GRAPHICSPRESETNOTINSTALLED_CANCEL,
     GRAPHICSPRESETDELAYEDCONFIRMATION_TITLE,
     GRAPHICSPRESETDELAYEDCONFIRMATION_MESSAGE,
     GRAPHICSPRESETDELAYEDCONFIRMATION_SUBMIT,
     GRAPHICSPRESETDELAYEDCONFIRMATION_CANCEL,
     NEXTBATTLEOPTIONCONFIRMATION_TITLE,
     NEXTBATTLEOPTIONCONFIRMATION_MESSAGE,
     NEXTBATTLEOPTIONCONFIRMATION_SUBMIT,
     NEXTBATTLEOPTIONCONFIRMATION_CANCEL,
     GRAPHICSPRESETAUTODETECTCONFIRMATION_TITLE,
     GRAPHICSPRESETAUTODETECTCONFIRMATION_MESSAGE,
     GRAPHICSPRESETAUTODETECTCONFIRMATION_SUBMIT,
     GRAPHICSPRESETAUTODETECTCONFIRMATION_CANCEL,
     GRAPHICSPRESETNOTPOSSIBLE_TITLE,
     GRAPHICSPRESETNOTPOSSIBLE_MESSAGE,
     GRAPHICSPRESETNOTPOSSIBLE_CANCEL,
     GRAPHICSCHANGECONFIRMATION_TITLE,
     GRAPHICSCHANGECONFIRMATION_MESSAGE,
     GRAPHICSCHANGECONFIRMATION_SUBMIT,
     GRAPHICSCHANGECONFIRMATION_CANCEL,
     WATERQUALITYNOTPOSSIBLE_TITLE,
     WATERQUALITYNOTPOSSIBLE_MESSAGE,
     WATERQUALITYNOTPOSSIBLE_CANCEL,
     PREMIUMBUYCONFIRMATION_TITLE,
     PREMIUMBUYCONFIRMATION_MESSAGE,
     PREMIUMBUYCONFIRMATION_SUBMIT,
     PREMIUMBUYCONFIRMATION_CANCEL,
     PREMIUMCONTINUECONFIRMATION_TITLE,
     PREMIUMCONTINUECONFIRMATION_MESSAGE,
     PREMIUMCONTINUECONFIRMATION_SUBMIT,
     PREMIUMCONTINUECONFIRMATION_CANCEL,
     BUYPREMWITHOUTBENEFITSCONFIRMATION_TITLE,
     BUYPREMWITHOUTBENEFITSCONFIRMATION_MESSAGE,
     BUYPREMWITHOUTBENEFITSCONFIRMATION_SUBMIT,
     BUYPREMWITHOUTBENEFITSCONFIRMATION_CANCEL,
     BUYINSTALLCONFIRMATION_TITLE,
     BUYINSTALLCONFIRMATION_MESSAGECOMBINE,
     BUYINSTALLCONFIRMATION_MESSAGE,
     BUYINSTALLCONFIRMATION_CONFLICTEDMESSAGE_PREFIX,
     BUYINSTALLCONFIRMATION_CONFLICTEDMESSAGE_HIGHLIGHTENTEXT,
     BUYINSTALLCONFIRMATION_CONFLICTEDMESSAGE_POSTFIX,
     BUYINSTALLCONFIRMATION_SUBMIT,
     BUYINSTALLCONFIRMATION_CANCEL,
     REMOVECONFIRMATIONNOTREMOVABLE_SUBMIT,
     SELLCONFIRMATION_SUBMIT,
     SELLCONFIRMATION_CANCEL,
     SELLMODULECONFIRMATION_TITLE,
     SELLMODULECONFIRMATION_SUBMIT,
     SELLMODULECONFIRMATION_CANCEL,
     CONFIRMMODULEDIALOG_PRICELABEL,
     CONFIRMMODULEDIALOG_COUNTLABEL,
     CONFIRMMODULEDIALOG_TOTALLABEL,
     CONFIRMMODULEDIALOG_COUNTLABEL1,
     CONFIRMMODULEDIALOG_PRICELABEL1,
     CONFIRMMODULEDIALOG_SHOP_TOTALLABEL1,
     CONFIRMMODULEDIALOG_INVENTORY_TOTALLABEL1,
     CONFIRMMODULEDIALOG_REZULTLABEL1,
     RENTCONFIRMATION_TITLE,
     RENTCONFIRMATION_MESSAGE,
     RENTCONFIRMATION_SUBMIT,
     RENTCONFIRMATION_CANCEL,
     RENTCONFIRMATION_EVENT,
     RENTCONFIRMATIONRENEW_TITLE,
     RENTCONFIRMATIONRENEW_MESSAGE,
     RENTCONFIRMATIONRENEW_SUBMIT,
     RENTCONFIRMATIONRENEW_CANCEL,
     BUYCONFIRMATION_TITLE,
     BUYCONFIRMATION_MESSAGECOMBINE,
     BUYCONFIRMATION_MESSAGE,
     BUYCONFIRMATION_SUBMIT,
     BUYCONFIRMATION_CANCEL,
     IDLECREWBONUS_TITLE,
     IDLECREWBONUS_MESSAGE_REMOVETYPE,
     IDLECREWBONUS_MESSAGE_REMOVENAME,
     IDLECREWBONUS_MESSAGE_CREWWARNING,
     IDLECREWBONUS_MESSAGE_CREWINCOMPLETE,
     IDLECREWBONUS_MESSAGE_CREWUNSUITABLE,
     IDLECREWBONUS_SUBMIT,
     IDLECREWBONUS_CANCEL,
     WOTPLUSRENTAL_TITLE,
     WOTPLUSRENTAL_DESCRIPTION,
     WOTPLUSRENTAL_SUBMIT,
     WOTPLUSRENTAL_CANCEL,
     DISCONNECTED_TITLE,
     DISCONNECTED_MESSAGE,
     DISCONNECTED_MESSAGEKICK,
     DISCONNECTED_MESSAGEBAN,
     DISCONNECTED_MESSAGEBANPERIOD,
     DISCONNECTED_REASON,
     DISCONNECTED_CANCEL,
     LOWAMMO_TITLE,
     LOWAMMO_MESSAGE,
     LOWAMMO_SUBMIT,
     LOWAMMO_CANCEL,
     LOWAMMOAUTOLOAD_TITLE,
     LOWAMMOAUTOLOAD_MESSAGE,
     LOWALTERNATIVEAMMOAUTOLOAD_TITLE,
     LOWALTERNATIVEAMMOAUTOLOAD_MESSAGE,
     LOWAMMOAUTOLOAD_SUBMIT,
     LOWAMMOAUTOLOAD_CANCEL,
     BUYSLOTCONFIRMATION_TITLE,
     BUYSLOTCONFIRMATION_MESSAGE,
     BUYSLOTCONFIRMATION_SUBMIT,
     BUYSLOTCONFIRMATION_CANCEL,
     FREESLOTCONFIRMATION_TITLE,
     FREESLOTCONFIRMATION_MESSAGE,
     FREESLOTCONFIRMATION_SUBMIT,
     FREESLOTCONFIRMATION_CANCEL,
     REPLACEPASSPORT_UNIQUE_TITLE,
     REPLACEPASSPORT_UNIQUE_MESSAGE,
     REPLACEPASSPORT_UNIQUE_SUBMIT,
     REPLACEPASSPORT_UNIQUE_CANCEL,
     REPLACEPASSPORTCONFIRMATION_TITLE,
     REPLACEPASSPORTCONFIRMATION_MESSAGE,
     REPLACEPASSPORTCONFIRMATION_SUBMIT,
     REPLACEPASSPORTCONFIRMATION_CANCEL,
     BUYSLOT_HANGARSLOT_HEADER,
     BUYSLOTSHOPCONFIRMATION_TITLE,
     BUYSLOTSHOPCONFIRMATION_MESSAGECOMBINE,
     BUYSLOTSHOPCONFIRMATION_SUBMIT,
     BUYSLOTSHOPCONFIRMATION_CANCEL,
     UPGRADETANKMANSCOOLCONFIRMATION_TITLE,
     UPGRADETANKMANSCOOLCONFIRMATION_MESSAGECOMBINE,
     UPGRADETANKMANSCOOLCONFIRMATION_SUBMIT,
     UPGRADETANKMANSCOOLCONFIRMATION_CANCEL,
     UPGRADETANKMANACADEMYCONFIRMATION_TITLE,
     UPGRADETANKMANACADEMYCONFIRMATION_MESSAGECOMBINE,
     UPGRADETANKMANACADEMYCONFIRMATION_SUBMIT,
     UPGRADETANKMANACADEMYCONFIRMATION_CANCEL,
     UPGRADETANKMANSCOOLNOTENOUGHMONEY_TITLE,
     UPGRADETANKMANSCOOLNOTENOUGHMONEY_MESSAGE,
     UPGRADETANKMANSCOOLNOTENOUGHMONEY_SUBMIT,
     UPGRADETANKMANSCOOLNOTENOUGHMONEY_CANCEL,
     UPGRADETANKMANACADEMYNOTENOUGHMONEY_TITLE,
     UPGRADETANKMANACADEMYNOTENOUGHMONEY_MESSAGE,
     UPGRADETANKMANACADEMYNOTENOUGHMONEY_SUBMIT,
     UPGRADETANKMANACADEMYNOTENOUGHMONEY_CANCEL,
     RECRUITDIALOG_TITLE,
     RECRUITDIALOG_NAME_TITLE,
     RECRUITWINDOW_NATION,
     RECRUITWINDOW_SPECIALIZATION,
     RECRUITWINDOW_VEHICLECLASS,
     RECRUITWINDOW_VEHICLETYPE,
     RECRUITWINDOW_MENUEMPTYROW,
     RECRUITWINDOW_SUBMIT,
     RECRUITWINDOW_CANCEL,
     BUYSLOTNOTENOUGH_CREDITS_TITLE,
     BUYSLOTNOTENOUGH_CREDITS_MESSAGE,
     BUYSLOTNOTENOUGH_CREDITS_SUBMIT,
     BUYSLOTNOTENOUGH_CREDITS_CANCEL,
     BUYSLOTNOTENOUGH_GOLD_TITLE,
     BUYSLOTNOTENOUGH_GOLD_MESSAGE,
     BUYSLOTNOTENOUGH_GOLD_SUBMIT,
     BUYSLOTNOTENOUGH_GOLD_CANCEL,
     BUYVEHICLEWINDOW_TITLE,
     BUYVEHICLEWINDOW_TRADEIN_TITLE,
     BUYVEHICLEWINDOW_TRADEIN_PRICELABEL,
     BUYVEHICLEWINDOW_PRICELABEL,
     BUYVEHICLEWINDOW_SUBMITBTN,
     BUYVEHICLEWINDOW_TRADEIN_SUBMITBTN,
     BUYVEHICLEWINDOW_CANCELBTN,
     BUYVEHICLEWINDOW_TRADEIN_CANCELBTN,
     BUYVEHICLEWINDOW_WARNING,
     BUYVEHICLEWINDOW_TRADEIN_WARNING,
     BUYVEHICLEWINDOW_FREERENTSLOT,
     BUYVEHICLEWINDOW_FULLAMMO,
     BUYVEHICLEWINDOW_TANKMENCHECKBOX,
     BUYVEHICLEWINDOW_TRADEIN_TANKMENCHECKBOX,
     BUYVEHICLEWINDOW_TANKMENLABEL,
     BUYVEHICLEWINDOW_TANKMENTOTALLABEL,
     BUYVEHICLEWINDOW_SLOTCHECKBOX,
     BUYVEHICLEWINDOW_AMMOCHECKBOX,
     BUYVEHICLEWINDOW_CREWINVEHICLE,
     BUYVEHICLEWINDOW_TOTALLABEL,
     BUYVEHICLEWINDOW_TABS_BUY,
     BUYVEHICLEWINDOW_TABS_TRADE,
     BUYVEHICLEWINDOW_TRADEIN_STUDYLABEL,
     BUYVEHICLEWINDOW_TRADEIN_TOTALLABEL,
     BUYVEHICLEWINDOW_TRADEIN_CONFIRMATION_TITLE,
     BUYVEHICLEWINDOW_TRADEIN_CONFIRMATION_QUESTION,
     BUYVEHICLEWINDOW_TRADEIN_CONFIRMATION_ERRORMESSAGE,
     BUYVEHICLEWINDOW_TRADEIN_INFO_NOVEHICLES,
     BUYVEHICLEWINDOW_TRADEIN_WARNING_CHOOSE,
     BUYVEHICLEWINDOW_TRADEIN_INFO_SAVING,
     BUYVEHICLEWINDOW_TRADEIN_VEHICLE_CHOOSE,
     TRADEINPOPOVER_DESCR,
     TRADEINPOPOVER_TITLE,
     TRADEINPOPOVER_SORTING_NATION_HEADER,
     TRADEINPOPOVER_SORTING_NATION_BODY,
     TRADEINPOPOVER_SORTING_VEHTYPE_HEADER,
     TRADEINPOPOVER_SORTING_VEHTYPE_BODY,
     TRADEINPOPOVER_SORTING_VEHLVL_HEADER,
     TRADEINPOPOVER_SORTING_VEHLVL_BODY,
     TRADEINPOPOVER_SORTING_VEHNAME_HEADER,
     TRADEINPOPOVER_SORTING_VEHNAME_BODY,
     TRADEINPOPOVER_SORTING_SAVING_FORMATTED,
     TRADEINPOPOVER_SORTING_SAVING_HEADER,
     TRADEINPOPOVER_SORTING_SAVING_BODY,
     TRADEOFFWIDGET_SELECTVEHICLE,
     RESTOREEQUIPMENT_HEADER,
     RESTOREEQUIPMENT_TEXT,
     RESTOREEQUIPMENT_BUTTON_RESTORE,
     RESTOREEQUIPMENT_BUTTON_CANCEL,
     RESTOREVEHICLEDIALOG_TITLE,
     RESTOREVEHICLEDIALOG_PRICELABEL,
     RESTOREVEHICLEDIALOG_TANKMENCHECKBOX,
     RESTOREVEHICLEDIALOG_SUBMITBTN,
     RESTOREVEHICLEDIALOG_CANCELBTN,
     RESTOREVEHICLEDIALOG_WARNING,
     BARRACKSEXPAND_TITLE,
     BARRACKSEXPAND_MESSAGE,
     BARRACKSEXPAND_SUBMIT,
     BARRACKSEXPAND_CANCEL,
     BARRACKSEXPANDNOTENOUGHMONEY_TITLE,
     BARRACKSEXPANDNOTENOUGHMONEY_MESSAGE,
     BARRACKSEXPANDNOTENOUGHMONEY_SUBMIT,
     BARRACKSEXPANDNOTENOUGHMONEY_CANCEL,
     EULA_P1,
     EULA_P2,
     CONFIRMUNLOCK_TITLE,
     CONFIRMUNLOCK_ITEM_MESSAGE,
     CONFIRMUNLOCK_VEHICLE_MESSAGE,
     CONFIRMUNLOCK_SUBMIT,
     CONFIRMUNLOCK_CANCEL,
     CONFIRMBUY_TITLE,
     CONFIRMBUYANDINSTALL_TITLE,
     CONFIRMBUYANDINSTALL_MESSAGE,
     CONFIRMBUYANDINSTALL_SELLMESSAGE,
     CONFIRMBUYANDINSTALL_DEPOTMESSAGE,
     CONFIRMBUYANDINSTALL_SOLDMODULEINFO_DESCRIPTION,
     CONFIRMBUYANDINSTALL_SOLDMODULEINFO_COMPATIBLETANKS,
     CONFIRMBUYANDINSTALL_INSUFFICIENTFUNDSTOOLTIP_HEADER,
     CONFIRMBUYANDINSTALL_INSUFFICIENTFUNDSTOOLTIP_BODY,
     CONFIRMBUYANDINSTALL_INSUFFICIENTFUNDSTOOLTIP_AMOUNT,
     CONFIRMBUYANDINSTALL_SUBMIT,
     CONFIRMBUYANDINSTALL_CANCEL,
     POSTMORTEM_TITLE,
     POSTMORTEM_MESSAGE,
     POSTMORTEM_SUBMIT,
     POSTMORTEM_CANCEL,
     DISMISSEDBUFFEROVERFLAW_TITLE,
     DISMISSEDBUFFEROVERFLAW_MESSAGE,
     DISMISSEDBUFFEROVERFLAW_SUBMIT,
     DISMISSEDBUFFEROVERFLAW_CANCEL,
     DISMISSEDBUFFEROVERFLAWMULTIPLE_TITLE,
     DISMISSEDBUFFEROVERFLAWMULTIPLE_MESSAGE,
     DISMISSEDBUFFEROVERFLAWMULTIPLE_SUBMIT,
     DISMISSEDBUFFEROVERFLAWMULTIPLE_CANCEL,
     DROPSKILL_TITLE,
     DROPSKILL_MESSAGE,
     DROPSKILL_SUBMIT,
     DROPSKILL_CANCEL,
     SQUADPREMIUMNEEDED_TITLE,
     SQUADPREMIUMNEEDED_MESSAGE,
     SQUADPREMIUMNEEDED_CANCEL,
     SQUADHAVENOTREADYPLAYERS_TITLE,
     SQUADHAVENOTREADYPLAYERS_MESSAGE,
     SQUADHAVENOTREADYPLAYERS_SUBMIT,
     SQUADHAVENOTREADYPLAYERS_CANCEL,
     SQUADHAVENOTREADYPLAYERSAUTO_TITLE,
     SQUADHAVENOTREADYPLAYERSAUTO_MESSAGE,
     SQUADHAVENOTREADYPLAYERSAUTO_SUBMIT,
     SQUADHAVENOTREADYPLAYERSAUTO_CANCEL,
     SQUADHAVENOTREADYPLAYERAUTO_TITLE,
     SQUADHAVENOTREADYPLAYERAUTO_MESSAGE,
     SQUADHAVENOTREADYPLAYERAUTO_SUBMIT,
     SQUADHAVENOTREADYPLAYERAUTO_CANCEL,
     SQUADHAVENOTREADYPLAYER_TITLE,
     SQUADHAVENOTREADYPLAYER_MESSAGE,
     SQUADHAVENOTREADYPLAYER_SUBMIT,
     SQUADHAVENOTREADYPLAYER_CANCEL,
     SQUADHAVENOPLAYERS_TITLE,
     SQUADHAVENOPLAYERS_MESSAGE,
     SQUADHAVENOPLAYERS_SUBMIT,
     SQUADHAVENOPLAYERS_CANCEL,
     SQUADHAVENOPLAYERSAUTO_TITLE,
     SQUADHAVENOPLAYERSAUTO_MESSAGE,
     SQUADHAVENOPLAYERSAUTO_SUBMIT,
     SQUADHAVENOPLAYERSAUTO_CANCEL,
     SQUADHAVENOPLAYERAUTO_TITLE,
     SQUADHAVENOPLAYERAUTO_MESSAGE,
     SQUADHAVENOPLAYERAUTO_SUBMIT,
     SQUADHAVENOPLAYERAUTO_CANCEL,
     SQUADHAVEPLAYERSINBATTLE_TITLE,
     SQUADHAVEPLAYERSINBATTLE_MESSAGE,
     SQUADHAVEPLAYERSINBATTLE_SUBMIT,
     LEFTPREBATTLEANDACCEPTINVITE_TITLE,
     LEFTPREBATTLEANDACCEPTINVITE_MESSAGE,
     LEFTPREBATTLEANDACCEPTINVITE_SUBMIT,
     LEFTPREBATTLEANDACCEPTINVITE_CANCEL,
     LEFTTRAININGANDACCEPTINVITE_TITLE,
     LEFTTRAININGANDACCEPTINVITE_MESSAGE,
     LEFTTRAININGANDACCEPTINVITE_SUBMIT,
     LEFTTRAININGANDACCEPTINVITE_CANCEL,
     LEFTSQUADANDACCEPTINVITE_TITLE,
     LEFTSQUADANDACCEPTINVITE_MESSAGE,
     LEFTSQUADANDACCEPTINVITE_SUBMIT,
     LEFTSQUADANDACCEPTINVITE_CANCEL,
     GATHERINGXPFORM_TITLE,
     GATHERINGXPFORM_BEFOREOPERATION,
     GATHERINGXPFORM_CURRENTAMOUNT,
     GATHERINGXPFORM_AFTEROPERATION,
     GATHERINGXPFORM_HEADERBUTTONS_VEHICLE,
     GATHERINGXPFORM_HEADERBUTTONS_XP,
     GATHERINGXPFORM_HEADERBUTTONS_CREW,
     GATHERINGXPFORM_TOCHANGELABEL,
     GATHERINGXPFORM_TOTALLABEL,
     GATHERINGXPFORM_SELECTALLLABEL,
     GATHERINGXPFORM_TOTALXP,
     GATHERINGXPFORM_SORTBY_SELECTION_HEADER,
     GATHERINGXPFORM_SORTBY_SELECTION_BODY,
     GATHERINGXPFORM_SORTBY_VEHICLE_HEADER,
     GATHERINGXPFORM_SORTBY_VEHICLE_BODY,
     GATHERINGXPFORM_SORTBY_XP_HEADER,
     GATHERINGXPFORM_SORTBY_XP_BODY,
     EXCHANGEXPWINDOW_ERROR_NOELITEVEHICLEINHANGAR,
     EXCHANGEXPWINDOW_ERROR_NOVEHICLESWITHXP,
     GATHERINGXPFORM_TOOLTIPS_CHECKBOXCREWSELECTED,
     GATHERINGXPFORM_TOOLTIPS_CHECKBOXCREWUNSELECTED,
     GATHERINGXPFORM_BTNSUBMIT,
     GATHERINGXPFORM_BTNCANCEL,
     EXCHANGEXPCONFIRMATION_TITLE,
     EXCHANGEXPCONFIRMATION_MESSAGE,
     EXCHANGEXPCONFIRMATION_AVAILABLE_FORFREE_MESSAGE,
     EXCHANGEXPCONFIRMATION_SUBMIT,
     EXCHANGEXPCONFIRMATION_CANCEL,
     EXCHANGEGOLDCONFIRMATION_TITLE,
     EXCHANGEGOLDCONFIRMATION_MESSAGE,
     EXCHANGEGOLDCONFIRMATION_SUBMIT,
     EXCHANGEGOLDCONFIRMATION_CANCEL,
     CONTROLSWRONGNOTIFICATION_TITLE,
     CONTROLSWRONGNOTIFICATION_MESSAGE,
     CONTROLSWRONGNOTIFICATION_SUBMIT,
     CONTROLSWRONGNOTIFICATION_CANCEL,
     MINIMAPALPHANOTIFICATION_TITLE,
     MINIMAPALPHANOTIFICATION_MESSAGE,
     MINIMAPALPHANOTIFICATION_MESSAGE_ALERT,
     MINIMAPALPHANOTIFICATION_SUBMIT,
     MINIMAPALPHANOTIFICATION_CANCEL,
     LIMITEDUIOFFNOTIFICATION_TITLE,
     LIMITEDUIOFFNOTIFICATION_MESSAGE,
     LIMITEDUIOFFNOTIFICATION_MESSAGE_ALERT,
     LIMITEDUIOFFNOTIFICATION_SUBMIT,
     LIMITEDUIOFFNOTIFICATION_CANCEL,
     SOUNDMODEINVALID_TITLE,
     SOUNDMODEINVALID_MESSAGE,
     SOUNDMODEINVALID_SUBMIT,
     SOUNDMODEINVALID_CANCEL,
     CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_TITLE,
     CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_MESSAGE,
     CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_SUBMIT,
     CONTROLSWRONGNOTIFICATIONSOUNDMODEINVALID_CANCEL,
     EULA_TITLE,
     EULA_LABELS_AGREE,
     EULA_BUTTONS_APPLY,
     HAVENOEMPTYSLOTS_TITLE,
     HAVENOEMPTYSLOTS_MESSAGE,
     HAVENOEMPTYSLOTS_SUBMIT,
     HAVENOEMPTYSLOTS_CANCEL,
     MONEYTRANSFER_TITLE,
     MONEYTRANSFER_LABELTOTALPRICE,
     MONEYTRANSFER_LABELTO,
     MONEYTRANSFER_LABELGOLD,
     MONEYTRANSFER_NOT_A_CLAN,
     MONEYTRANSFER_LABELFEEPRICE,
     MONEYTRANSFER_LABELNORMAL,
     MONEYTRANSFER_LABELNORMALCREDITS,
     MONEYTRANSFER_LABELNORMALGOLD,
     MONEYTRANSFER_LABELCLAN,
     MONEYTRANSFER_LABELCLANCREDITS,
     MONEYTRANSFER_LABELCLANGOLD,
     MONEYTRANSFER_SUBMITBTN,
     MONEYTRANSFER_CANCELBTN,
     MONEYTRANSFERCONFIRMATION_TITLE,
     MONEYTRANSFERCONFIRMATION_MESSAGE,
     MONEYTRANSFERCONFIRMATION_SUBMIT,
     MONEYTRANSFERCONFIRMATION_CANCEL,
     MONEYTRANSFERRESTRICTION_TITLE,
     MONEYTRANSFERRESTRICTION_MESSAGE,
     MONEYTRANSFERRESTRICTION_MESSAGE_EXPIRY,
     MONEYTRANSFERRESTRICTION_SUBMIT,
     MONEYTRANSFERRESTRICTION_CANCEL,
     MONEYTRANSFERLINK_SET_PASSWORD,
     FINANCE_DIALOG_HEADER,
     FINANCE_DIALOG_SUBMITBTN,
     FINANCE_DIALOG_CANCELBTN,
     FINANCE_DIALOG_RESULTS_DEFAULTMESSAGE,
     FINANCE_DIALOG_RESULTS_VALID,
     FINANCE_DIALOG_RESULTS_INVALID,
     FINANCE_DIALOG_RESULTS_LIMIT,
     FINANCE_DIALOG_RESULTS_WRONG,
     FREEVEHICLELEFTLIMIT_TITLE,
     FREEVEHICLELEFTLIMIT_MESSAGE,
     FREEVEHICLELEFTLIMIT_CANCEL,
     FREEVEHICLELEFTLIMIT_SUBMIT,
     VOICECHATINITFAILED_TITLE,
     VOICECHATINITFAILED_MESSAGE,
     VOICECHATINITFAILED_CANCEL,
     VOICECHATINITSUCCEDED_TITLE,
     VOICECHATINITSUCCEDED_MESSAGE,
     VOICECHATINITSUCCEDED_CANCEL,
     INGAMEBROWSER_TEXTURELOADINGFAILED_TITLE,
     INGAMEBROWSER_TEXTURELOADINGFAILED_MESSAGE,
     MESSENGER_USERINFOHIDDEN_TITLE,
     MESSENGER_USERINFOHIDDEN_MESSAGE,
     MESSENGER_USERINFOHIDDEN_SUBMIT,
     MESSENGER_USERINFOHIDDEN_CANCEL,
     MESSENGER_USERINFONOTAVAILABLE_TITLE,
     MESSENGER_USERINFONOTAVAILABLE_MESSAGE,
     MESSENGER_USERINFONOTAVAILABLE_SUBMIT,
     MESSENGER_USERINFONOTAVAILABLE_CANCEL,
     VEHICLEREMOVEDIALOG_TITLE,
     VEHICLESELLDIALOG_EXPANDBTNLABEL,
     VEHICLESELLDIALOG_TITLE,
     VEHICLESELLDIALOG_MESSAGE,
     VEHICLESELLDIALOG_MESSAGE_MULTINATIONAL,
     VEHICLESELLDIALOG_VEHICLETYPE_LIGHTTANK,
     VEHICLESELLDIALOG_VEHICLETYPE_MEDIUMTANK,
     VEHICLESELLDIALOG_VEHICLETYPE_HEAVYTANK,
     VEHICLESELLDIALOG_VEHICLETYPE_SPG,
     VEHICLESELLDIALOG_VEHICLETYPE_AT_SPG,
     VEHICLESELLDIALOG_VEHICLE_LEVEL,
     VEHICLESELLDIALOG_VEHICLE_ROLE,
     VEHICLESELLDIALOG_VEHICLE_EMPTYSELLPRICE,
     VEHICLESELLDIALOG_PROFFIT,
     VEHICLESELLDIALOG_LOSS,
     VEHICLESELLDIALOG_CREW_LABEL,
     VEHICLESELLDIALOG_OPTIONALDEVICE,
     VEHICLESELLDIALOG_EQUIPMENT,
     VEHICLESELLDIALOG_BATTLEBOSTER,
     VEHICLESELLDIALOG_CUSTOMIZATION,
     VEHICLESELLDIALOG_AMMO_LABEL,
     VEHICLESELLDIALOG_COMMONRESULT,
     VEHICLESELLDIALOG_INVENTORY,
     VEHICLESELLDIALOG_UNLOAD,
     VEHICLESELLDIALOG_DECONSTRUCT,
     VEHICLESELLDIALOG_NOTINSTALLED_MODULES,
     VEHICLESELLDIALOG_COUNT,
     VEHICLESELLDIALOG_REMOVE,
     VEHICLESELLDIALOG_SUBMIT,
     VEHICLESELLDIALOG_CANCEL,
     VEHICLESELLDIALOG_VEHICLE_ELITE,
     VEHICLESELLDIALOG_CREW_UNLOAD,
     VEHICLESELLDIALOG_CREW_DISSMISS,
     VEHICLESELLDIALOG_CTRLQUESTION_HEADER,
     VEHICLESELLDIALOG_CTRLQUESTION_QUESTION,
     VEHICLESELLDIALOG_CTRLQUESTION_ERRORMESSAGE,
     VEHICLESELLDIALOG_PRICE_SIGN_ADD,
     VEHICLESELLDIALOG_POSTPROGRESSIONINFO,
     VEHICLESELLDIALOG_POSTPROGRESSIONINFO_SUBSCRIPTION,
     VEHICLESELL_UNIQUE_TITLE,
     VEHICLESELL_UNIQUE_MESSAGE,
     VEHICLESELL_UNIQUE_SUBMIT,
     VEHICLESELL_UNIQUE_CANCEL,
     VEHICLESELL_UNIQUE_CREWLOCKED_TITLE,
     VEHICLESELL_UNIQUE_CREWLOCKED_MESSAGE,
     VEHICLESELL_UNIQUE_CREWLOCKED_SUBMIT,
     VEHICLESELL_UNIQUE_CREWLOCKED_CANCEL,
     VEHICLESELL_RESTORECOOLDOWN_TITLE,
     VEHICLESELL_RESTORECOOLDOWN_MESSAGE,
     VEHICLESELL_RESTORECOOLDOWN_SUBMIT,
     VEHICLESELL_RESTORECOOLDOWN_CANCEL,
     VEHICLESELL_RESTOREUNLIMITED_TITLE,
     VEHICLESELL_RESTOREUNLIMITED_MESSAGE,
     VEHICLESELL_RESTOREUNLIMITED_SUBMIT,
     VEHICLESELL_RESTOREUNLIMITED_CANCEL,
     UPDATENEEDED_TITLE,
     UPDATENEEDED_MESSAGE,
     UPDATENEEDED_SUBMIT,
     UPDATENEEDED_CANCEL,
     DEMOACCOUNTBOOTCAMPFAILURE_TITLE,
     DEMOACCOUNTBOOTCAMPFAILURE_MESSAGE,
     DEMOACCOUNTBOOTCAMPFAILURE_CANCEL,
     STEAMSTARTNEEDED_TITLE,
     STEAMSTARTNEEDED_MESSAGE,
     STEAMSTARTNEEDED_CANCEL,
     REPLAYNOTIFICATION_TITLE,
     REPLAYNOTIFICATION_MESSAGE,
     REPLAYNOTIFICATION_SUBMIT,
     REPLAYNOTIFICATION_CANCEL,
     REPLAYSTOPPED_TITLE,
     REPLAYSTOPPED_MESSAGE,
     REPLAYSTOPPED_SUBMIT,
     REPLAYSTOPPED_CANCEL,
     PUNISHMENTWINDOW_TITLE,
     PUNISHMENTWINDOW_MSGTITLE_WARNING,
     PUNISHMENTWINDOW_MSGTITLE_PENALTY,
     PUNISHMENTWINDOW_MESSAGE_WARNING,
     PUNISHMENTWINDOW_MESSAGE_PENALTY,
     PUNISHMENTWINDOW_MESSAGE_EXTRA_PENALTY,
     PUNISHMENTWINDOW_CANCEL,
     PUNISHMENTWINDOW_REASON_DESERTER,
     PUNISHMENTWINDOW_REASON_EPIC_DESERTER,
     PUNISHMENTWINDOW_REASON_SUICIDE,
     PUNISHMENTWINDOW_REASON_AFK,
     PUNISHMENTWINDOW_REASON_BATTLEROYALE_DESERTER,
     PUNISHMENTWINDOW_REASON_BATTLEROYALE_AFK,
     REMOVEINCOMPATIBLEEQS_TITLE,
     REMOVEINCOMPATIBLEEQS_MESSAGE,
     REMOVEINCOMPATIBLEEQS_MESSAGE_REASON,
     REMOVEINCOMPATIBLEEQS_SUBMIT,
     REMOVEINCOMPATIBLEEQS_CANCEL,
     REFUSETRAINING_TITLE,
     REFUSETRAINING_MESSAGE,
     REFUSETRAINING_SUBMIT,
     REFUSETRAINING_CANCEL,
     SHOPSYNCERROR_TITLE,
     SHOPSYNCERROR_MESSAGE,
     SHOPSYNCERROR_CANCEL,
     RESETGRAPHICS_TITLE,
     RESETGRAPHICS_MESSAGE,
     RESETGRAPHICS_SUBMIT,
     RESETGRAPHICS_CANCEL,
     CHANGEGRAPHICS_TITLE,
     CHANGEGRAPHICS_MESSAGE,
     CHANGEGRAPHICS_SUBMIT,
     CHANGEGRAPHICS_CANCEL,
     GRAPHICS_MESSAGE_ALERT,
     LOWFPSWARNING_TITLE,
     LOWFPSWARNING_MESSAGE,
     LOWFPSWARNING_SUBMIT,
     LOWFPSWARNING_CANCEL,
     KOREAPARENTNOTIFICATION_TITLE,
     KOREAPARENTNOTIFICATION_MESSAGE,
     KOREAPARENTNOTIFICATION_SUBMIT,
     KOREAPARENTNOTIFICATION_CANCEL,
     KOREAPLAYTIMENOTIFICATION_TITLE,
     KOREAPLAYTIMENOTIFICATION_MESSAGE,
     KOREAPLAYTIMENOTIFICATION_SUBMIT,
     KOREAPLAYTIMENOTIFICATION_CANCEL,
     SENDINVITES_COMMON_TITLE,
     RALLY_AUTOSEARCH_TITLE,
     RALLY_AUTOSEARCH_MESSAGE,
     RALLY_AUTOSEARCH_SUBMIT,
     RALLY_AUTOSEARCH_CANCEL,
     RALLY_STARTBATTLE_TITLE,
     RALLY_STARTBATTLE_MESSAGE,
     RALLY_STARTBATTLE_SUBMIT,
     RALLY_STARTBATTLE_CANCEL,
     RALLY_CHANGEPERIPHERY_TITLE,
     RALLY_CHANGEPERIPHERY_MESSAGE,
     RALLY_CHANGEPERIPHERY_SUBMIT,
     RALLY_CHANGEPERIPHERY_CANCEL,
     RALLY_GOTOANOTHER_TITLE,
     RALLY_GOTOANOTHER_MESSAGE,
     RALLY_GOTOANOTHER_SUBMIT,
     RALLY_GOTOANOTHER_CANCEL,
     RALLY_GOTOSQUAD_TITLE,
     RALLY_GOTOSQUAD_MESSAGE,
     RALLY_GOTOSQUAD_SUBMIT,
     RALLY_GOTOSQUAD_CANCEL,
     SQUAD_GOTOSQUAD_TITLE,
     SQUAD_GOTOSQUAD_MESSAGE,
     SQUAD_GOTOSQUAD_SUBMIT,
     SQUAD_GOTOSQUAD_CANCEL,
     SQUAD_GOTOANOTHER_TITLE,
     SQUAD_GOTOANOTHER_MESSAGE,
     SQUAD_GOTOANOTHER_SUBMIT,
     SQUAD_GOTOANOTHER_CANCEL,
     RALLY_LEAVE_TITLE,
     RALLY_LEAVE_MESSAGE,
     RALLY_LEAVE_SUBMIT,
     RALLY_LEAVE_CANCEL,
     RALLY_GOTOINTRO_TITLE,
     RALLY_GOTOINTRO_MESSAGE,
     RALLY_GOTOINTRO_SUBMIT,
     RALLY_GOTOINTRO_CANCEL,
     SQUAD_LEAVE_TITLE,
     SQUAD_LEAVE_MESSAGE,
     SQUAD_LEAVE_SUBMIT,
     SQUAD_LEAVE_CANCEL,
     RALLY_LEAVEDISABLED_TITLE,
     RALLY_LEAVEDISABLED_MESSAGE,
     RALLY_LEAVEDISABLED_CANCEL,
     SQUAD_LEAVEDISABLED_TITLE,
     SQUAD_LEAVEDISABLED_MESSAGE,
     SQUAD_LEAVEDISABLED_CANCEL,
     CHANGEPERIPHERY_TITLE,
     CHANGEPERIPHERY_MESSAGE,
     CHANGEPERIPHERY_SUBMIT,
     CHANGEPERIPHERY_CANCEL,
     CHANGEROAMINGPERIPHERY_TITLE,
     CHANGEROAMINGPERIPHERY_MESSAGE,
     CHANGEROAMINGPERIPHERY_SUBMIT,
     CHANGEROAMINGPERIPHERY_CANCEL,
     CHANGEPERIPHERYANDREMEMBER_TITLE,
     CHANGEPERIPHERYANDREMEMBER_MESSAGE,
     CHANGEPERIPHERYANDREMEMBER_SUBMIT,
     CHANGEPERIPHERYANDREMEMBER_CANCEL,
     CHANGEROAMINGPERIPHERYANDREMEMBER_TITLE,
     CHANGEROAMINGPERIPHERYANDREMEMBER_MESSAGE,
     CHANGEROAMINGPERIPHERYANDREMEMBER_SUBMIT,
     CHANGEROAMINGPERIPHERYANDREMEMBER_CANCEL,
     LOGINTOPERIPHERYANDREMEMBER_TITLE,
     LOGINTOPERIPHERYANDREMEMBER_MESSAGE,
     LOGINTOPERIPHERYANDREMEMBER_SUBMIT,
     LOGINTOPERIPHERYANDREMEMBER_CANCEL,
     FREEXPINFO_TITLE,
     FREEXPINFO_MESSAGE,
     FREEXPINFO_SUBMITBTNLBL,
     SWITCHPERIPHERYWINDOW_WINDOWTITLE,
     SWITCHPERIPHERYWINDOW_BTNSWITCH,
     SWITCHPERIPHERYWINDOW_BTNCANCEL,
     CREATEORDERCONFIRMATION_TITLE,
     CREATEORDERCONFIRMATION_SUBMIT,
     CREATEORDERCONFIRMATION_CANCEL,
     FORTIFICATIONFIXEDPLAYERS_TITLE,
     FORTIFICATIONFIXEDPLAYERS_MESSAGE,
     FORTIFICATIONFIXEDPLAYERS_SUBMIT,
     FORTIFICATIONFIXEDPLAYERS_CANCEL,
     FORTIFICATIONCLOSEDIRECTION_SUBMIT,
     FORTIFICATIONCLOSEDIRECTION_CANCEL,
     REPORTBUG_TITLE,
     REPORTBUG_MESSAGE,
     REPORTBUG_SUBMIT,
     REPORTBUG_CANCEL,
     FORTTURNEDOFF_CANCEL,
     FORTTURNEDOFF_TITLE,
     FORTTURNEDOFF_MESSAGE,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_TITLE,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_TITLE,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_TITLE,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_NEEDITEMSTEXT,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_NEEDITEMSTEXT,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_NEEDITEMSTEXT,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_NEEDGOLDTEXT,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_NEEDGOLDTEXT,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_NEEDGOLDTEXT,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_NEEDITEMSSTEPPERTITLE,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_NEEDITEMSSTEPPERTITLE,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_NEEDITEMSSTEPPERTITLE,
     CONFIRMEXCHANGEDIALOG_GOLDITEMSSTEPPERTITLE,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_SUBMIT,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_SUBMIT,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_SUBMIT,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_CANCEL,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_CANCEL,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_CANCEL,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_EXCHANGENONEEDTEXT,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_EXCHANGENONEEDTEXT,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_EXCHANGENONEEDTEXT,
     CONFIRMEXCHANGEDIALOG_EXCHANGECREDITS_GOLDNOTENOUGHTEXT,
     CONFIRMEXCHANGEDIALOG_RESTOREEXCHANGECREDITS_GOLDNOTENOUGHTEXT,
     CONFIRMEXCHANGEDIALOG_EXCHANGEXP_GOLDNOTENOUGHTEXT,
     QUESTSCONFIRMDIALOG_TITLE,
     QUESTSCONFIRMDIALOG_MESSAGE,
     QUESTSCONFIRMDIALOG_SUBMIT,
     QUESTSCONFIRMDIALOG_CANCEL,
     QUESTSCONFIRMDIALOG_CHECKBOX,
     QUESTSCONFIRMPM3DIALOG_TITLE,
     QUESTSCONFIRMPM3DIALOG_MESSAGE,
     QUESTSCONFIRMPM3DIALOG_SUBMIT,
     QUESTSCONFIRMPM3DIALOG_CANCEL,
     QUESTSCONFIRMPM3DIALOG_CHECKBOX,
     QUESTSCONFIRMPROGRESSDIALOG_TITLE,
     QUESTSCONFIRMPROGRESSDIALOG_MESSAGE,
     QUESTSCONFIRMPROGRESSDIALOG_MESSAGE_ALERT,
     QUESTSCONFIRMPROGRESSDIALOG_SUBMIT,
     QUESTSCONFIRMPROGRESSDIALOG_CANCEL,
     QUESTSDISMISSPROGRESSDIALOG_TITLE,
     QUESTSCONFIRMDISCARDDIALOG_TITLE,
     QUESTSDISMISSPROGRESSDIALOG_MESSAGE,
     QUESTSDISMISSPROGRESSDIALOG_MESSAGE_ALERT,
     QUESTSDISMISSPROGRESSDIALOG_SUBMIT,
     QUESTSDISMISSPROGRESSDIALOG_CANCEL,
     QUESTSCONFIRMDISCARDDIALOG_MESSAGE,
     QUESTSCONFIRMDISCARDDIALOG_MESSAGE_ALERT,
     QUESTSCONFIRMDISCARDDIALOG_SUBMIT,
     QUESTSCONFIRMDISCARDDIALOG_CANCEL,
     EPICBATTLECONFIRMDIALOG_TITLE,
     EPICBATTLECONFIRMDIALOG_MESSAGE,
     EPICBATTLECONFIRMDIALOG_SUBMIT,
     EPICBATTLECONFIRMDIALOG_CANCEL,
     EPICBATTLECONFIRMDIALOG_CHECKBOX,
     BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_TITLE,
     BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_MESSAGE,
     BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_SUBMIT,
     BOOSTERSWINDOW_ACTIVATIONCONFIRMATION_CANCEL,
     BOOSTERSWINDOW_REPLACECONFIRMATION_TITLE,
     BOOSTERSWINDOW_REPLACECONFIRMATION_MESSAGE,
     BOOSTERSWINDOW_REPLACECONFIRMATION_SUBMIT,
     BOOSTERSWINDOW_REPLACECONFIRMATION_CANCEL,
     CLANCONFIRMJOINING_TITLE,
     CLANCONFIRMJOINING_MESSAGE,
     CLANCONFIRMJOINING_MESSAGE_CLANNAME,
     CLANCONFIRMJOINING_MESSAGE_CLANEXIT,
     CLANCONFIRMJOINING_SUBMIT,
     CLANCONFIRMJOINING_CANCEL,
     CUSTOMIZATION_CLOSE_TITLE,
     CUSTOMIZATION_CLOSE_SUBMIT,
     CUSTOMIZATION_CLOSE_CANCEL,
     CUSTOMIZATION_EXITTOSHOP_TITLE,
     CUSTOMIZATION_EXITTOSHOP_SUBMIT,
     CUSTOMIZATION_EXITTOSHOP_CANCEL,
     CUSTOMIZATION_FILTER_TITLE,
     CUSTOMIZATION_FILTER_MESSAGE,
     CUSTOMIZATION_FILTER_SUBMIT,
     CUSTOMIZATION_FILTER_CANCEL,
     CUSTOMIZATION_REMOVE_ELEMENT_TITLE,
     CUSTOMIZATION_REMOVE_ELEMENT_MESSAGE,
     CUSTOMIZATION_REMOVE_ELEMENT_SUBMIT,
     CUSTOMIZATION_REMOVE_ELEMENT_CANCEL,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_WILL_BE_DELETED,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_TITLE,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_MESSAGE,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_SUBMIT,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_TEMPORARY_CANCEL,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_TITLE,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_MESSAGE,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_SUBMIT,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_CANCEL,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_TITLE,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_MESSAGE,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_SUBMIT,
     CUSTOMIZATION_INSTALL_INVOICE_ITEM_PERMANENT_LAST_CANCEL,
     CUSTOMIZATION_BUY_INSTALL_BOUND_TITLE,
     CUSTOMIZATION_BUY_INSTALL_BOUND_MESSAGE,
     CUSTOMIZATION_CHANGE_INSTALL_BOUND_TITLE,
     CUSTOMIZATION_CHANGE_INSTALL_BOUND_MESSAGE,
     CUSTOMIZATION_INSTALL_BOUND_SUBMIT,
     CUSTOMIZATION_INSTALL_BOUND_CANCEL,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_TITLE,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_MESSAGE,
     CUSTOMIZATION_APPLYTOOTHERSEASON_MESSAGE,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_ALERT_MESSAGE,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_SUBMIT,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_CANCEL,
     CUSTOMIZATION_APPLYTOOTHERSEASON_SUMMER,
     CUSTOMIZATION_APPLYTOOTHERSEASON_WINTER,
     CUSTOMIZATION_APPLYTOOTHERSEASON_DESERT,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_SUMMER,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_WINTER,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_DESERT,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_SUMMER_WINTER,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_WINTER_DESERT,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_SUMMER_DESERT,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_REMOVED,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_THIS,
     CUSTOMIZATION_APPLYTOOTHERSEASONS_THESE,
     FORTDISABLED_TITLE,
     FORTDISABLED_MESSAGE,
     FORTDISABLED_CANCEL,
     ELENDISABLED_TITLE,
     ELENDISABLED_MESSAGE,
     ELENDISABLED_CANCEL,
     CLAN_DATA_NOT_AVAILABLE_TITLE,
     CLAN_DATA_NOT_AVAILABLE_MESSAGE,
     CLAN_DATA_NOT_AVAILABLE_CANCEL,
     SOUNDSPEAKERSPRESETDOESNOTMATCH_TITLE,
     SOUNDSPEAKERSPRESETDOESNOTMATCH_MESSAGE,
     SOUNDSPEAKERSPRESETDOESNOTMATCH_SUBMIT,
     SOUNDSPEAKERSPRESETDOESNOTMATCH_CANCEL,
     SOUNDSPEAKERSPRESETRESET_TITLE,
     SOUNDSPEAKERSPRESETRESET_MESSAGE,
     SOUNDSPEAKERSPRESETRESET_SUBMIT,
     SOUNDSPEAKERSPRESETRESET_CANCEL,
     STRONGHOLD_LEAVE_TITLE,
     STRONGHOLD_LEAVE_MESSAGE,
     STRONGHOLD_LEAVEDEFEAT_TITLE,
     STRONGHOLD_LEAVEDEFEAT_MESSAGE,
     STRONGHOLD_LEAVE_SUBMIT,
     STRONGHOLD_LEAVE_CANCEL,
     TRADEINCONFIRMATION_TITLE,
     TRADEINCONFIRMATION_MESSAGE,
     TRADEINCONFIRMATION_MESSAGE_ADDITION,
     TRADEINCONFIRMATION_MESSAGE_CREW,
     TRADEINCONFIRMATION_MESSAGE_SHELLS,
     TRADEINCONFIRMATION_MESSAGE_EQUIPMENTS,
     TRADEINCONFIRMATION_MESSAGE_OPTIONALDEVICES,
     TRADEINCONFIRMATION_MESSAGE_PAIRMODIFICATIONS,
     TRADEINCONFIRMATION_SUBMIT,
     TRADEINCONFIRMATION_CANCEL,
     VEHCONF_EXITDIALOG_TITLE,
     VEHCONF_EXITDIALOG_MESSAGE,
     VEHCONF_EXITDIALOG_SUBMIT,
     VEHCONF_EXITDIALOG_CANCEL,
     CONFIRMBATTLEBOOSTERINSTALL_TITLE,
     CONFIRMBATTLEBOOSTERINSTALL_MESSAGE,
     CONFIRMBATTLEBOOSTERINSTALL_SUBMIT,
     CONFIRMBATTLEBOOSTERINSTALL_CANCEL,
     CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_TITLE,
     CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_MESSAGE,
     CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_SUBMIT,
     CONFIRMBATTLEBOOSTERINSTALLNOTSUITABLE_CANCEL,
     CONFIRMBATTLEBOOSTERBUYANDINSTALL_TITLE,
     CONFIRMBATTLEBOOSTERBUYANDINSTALL_SUBMIT,
     CONFIRMBATTLEBOOSTERBUYANDINSTALL_CANCEL,
     BOOTCAMP_PREMIUMTYPE_BASIC,
     BOOTCAMP_PREMIUMTYPE_PLUS,
     BOOTCAMP_SKIP_TITLE,
     BOOTCAMP_SKIP_LABEL,
     BOOTCAMP_SKIP_MESSAGE,
     BOOTCAMP_SKIP_SUBMIT,
     BOOTCAMP_SKIP_CANCEL,
     BOOTCAMP_SKIP_REFERRAL_TITLE,
     BOOTCAMP_SKIP_REFERRAL_LABEL,
     BOOTCAMP_SKIP_REFERRAL_MESSAGE,
     BOOTCAMP_SKIP_REFERRAL_SUBMIT,
     BOOTCAMP_SKIP_REFERRAL_CANCEL,
     BOOTCAMP_START_TITLE,
     BOOTCAMP_START_LABEL,
     BOOTCAMP_START_MESSAGE,
     BOOTCAMP_START_SUBMIT,
     BOOTCAMP_START_CANCEL,
     BOOTCAMP_RETRY_TITLE,
     BOOTCAMP_RETRY_LABEL,
     BOOTCAMP_RETRY_MESSAGE,
     BOOTCAMP_RETRY_SUBMIT,
     BOOTCAMP_RETRY_CANCEL,
     BOOTCAMPCENTERUNAVAILABLE_TITLE,
     BOOTCAMPCENTERUNAVAILABLE_MESSAGE,
     BOOTCAMPCENTERUNAVAILABLE_CANCEL,
     HOF_EXCLUDERATING_TITLE,
     HOF_EXCLUDERATING_MESSAGE,
     HOF_EXCLUDERATING_SUBMIT,
     HOF_EXCLUDERATING_CANCEL,
     HOFDISABLED_TITLE,
     HOFDISABLED_MESSAGE,
     HOFDISABLED_CANCEL,
     CUSTOMIZATIONCONFIRMSELL_TITLE,
     CUSTOMIZATIONCONFIRMSELL_MESSAGE,
     LEAVEEVENT_TITLE,
     LEAVEEVENT_MESSAGE,
     LEAVEEVENT_SUBMIT,
     LEAVEEVENT_CANCEL,
     LEAVESTARTEDEVENT_TITLE,
     LEAVESTARTEDEVENT_MESSAGE,
     LEAVESTARTEDEVENT_SUBMIT,
     LEAVESTARTEDEVENT_CANCEL,
     LEAVEEVENT_MESSAGE_WARNING,
     GAMMADIALOG_TITLE,
     GAMMADIALOG_MESSAGE_HEADER,
     GAMMADIALOG_MESSAGE_DESCRIPTION,
     GAMMADIALOG_CANCEL,
     REFERRALREWARD_TITLE,
     REFERRALREWARD_MESSAGE,
     REFERRALREWARD_SUBMIT,
     REFERRALREWARD_CANCEL,
     SESSIONSTATS_CONFIRMRESET_TITLE,
     SESSIONSTATS_CONFIRMRESET_MESSAGE,
     SESSIONSTATS_CONFIRMRESET_TIME,
     SESSIONSTATS_CONFIRMRESET_SUBMIT,
     SESSIONSTATS_CONFIRMRESET_CANCEL,
     EDITABLESTYLES_CONFIRMRESET_TITLE,
     EDITABLESTYLES_CONFIRMRESET_MESSAGE,
     EDITABLESTYLES_CONFIRMRESET_FORMATTEDPARTOFMESSAGE,
     EDITABLESTYLES_CONFIRMRESET_CHECKBOXLABEL,
     EDITABLESTYLES_CONFIRMRESET_SUBMIT,
     EDITABLESTYLES_CONFIRMRESET_CANCEL,
     CONFIRMEQUIPMENTBUYINSTALL_SUBMIT,
     EQUIPMENTPURCASE_CONFORMATION_ALL,
     EQUIPMENTBUYINSTALL_PRICE,
     BUYCONFIRMATION_STRINGEQUIPMENT_SUBMIT,
     CONFIRMEQUIPMENTINSTALL_SUBMIT,
     EQUIPMENTDESTROY_CONFORMATION,
     EQUIPMENTDESTROY_WARNINGMSG,
     EQUIPMENTSALE_CONFORMATION_HEADER,
     EQUIPMENTDECONSTRUCT_CONFIRMATION_HEADER,
     MODULESALE_CONFORMATION_HEADER,
     ELEMENTTYPE_GUN,
     ELEMENTTYPE_TURRET,
     ELEMENTTYPE_ENGINE,
     ELEMENTTYPE_CHASSIS,
     ELEMENTTYPE_RADIOSTATION,
     SELLSHELLCONFIRMATION_SUBMIT,
     EQUIPMENTDESTROY_DEMOUNTOPTIONS_GOLDORDEMOKIT,
     EQUIPMENTDESTROY_DEMOUNTOPTIONS_BONDS,
     DAILYQUESTS_DIALOGINFOCONFIRMREROLL_TITLE,
     DAILYQUESTS_DIALOGINFOCONFIRMREROLL_MESSAGE,
     DAILYQUESTS_DIALOGINFOCONFIRMREROLL_SUBMIT,
     DAILYQUESTS_DIALOGCONFIRMREROLL_TIMELIMITMSGHOURS,
     DAILYQUESTS_DIALOGCONFIRMREROLL_TIMELIMITMSGHOURSMINS,
     DAILYQUESTS_DIALOGCONFIRMREROLL_TIMELIMITMSGMINS,
     DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_TITLE,
     DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_MESSAGE,
     DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_SUBMIT,
     DAILYQUESTS_DIALOGWARNINGCONFIRMREROLL_WARNING,
     SQUAD_EVENTDISABLED_TITLE,
     SQUAD_EVENTDISABLED_MESSAGE,
     SQUAD_EVENTDISABLED_CANCEL,
     DEDICATION_HEADLINE,
     DEDICATION_SUB_HEADLINE,
     BATTLEROYALE_PREBATTLE_TITLE,
     BATTLEROYALE_PREBATTLE_MESSAGE,
     BATTLEROYALE_PREBATTLE_SUBMIT,
     BATTLEROYALE_PREBATTLE_CANCEL,
     ACCOUNTCOMPLETION_SUBMIT,
     ACCOUNTCOMPLETION_CANCEL,
     ACCOUNTCOMPLETION_WARNINGSERVERUNAVAILABLETIMED,
     ACCOUNTCOMPLETION_WARNINGSERVERUNAVAILABLE,
     ACCOUNTCOMPLETION_WARNINGSOMETHINGWENTWRONG,
     ACCOUNTCOMPLETION_ERRORISWRONG,
     ACCOUNTCOMPLETION_EMAILFORBIDDEN,
     ACCOUNTCOMPLETION_EMAILPROVIDERBANNED,
     ACCOUNTCOMPLETION_EMAILRESTRICTEDBYCOUNTRYHEADER,
     ACCOUNTCOMPLETION_EMAILRESTRICTEDBYCOUNTRY,
     ACCOUNTCOMPLETION_EMAILALREADYTAKEN,
     ACCOUNTCOMPLETION_LOGINALREADYTAKEN,
     ACCOUNTCOMPLETION_ACCOUNTALREADYHASEMAIL,
     ACCOUNTCOMPLETION_EMAILISTOOSHORT,
     ACCOUNTCOMPLETION_EMAILISTOOLONG,
     ACCOUNTCOMPLETION_TOOMANYREQUESTS,
     ACCOUNTCOMPLETION_REWARDSTITLE,
     ACCOUNTCOMPLETION_REGISTRATIONREWARDSTITLE,
     ACCOUNTCOMPLETION_EMAIL_FIELDNAME,
     ACCOUNTCOMPLETION_EMAIL_FIELDPLACEHOLDER,
     ACCOUNTCOMPLETION_PASSWORD_FIELDNAME,
     ACCOUNTCOMPLETION_EMAIL_TITLE,
     ACCOUNTCOMPLETION_EMAIL_SUBTITLE,
     ACCOUNTCOMPLETION_EMAIL_FULLACCESS_TITLE,
     ACCOUNTCOMPLETION_EMAIL_FULLACCESS_SUBTITLE,
     ACCOUNTCOMPLETION_ACTIVATE_TITLE,
     ACCOUNTCOMPLETION_ACTIVATE_TEXT,
     ACCOUNTCOMPLETION_ACTIVATE_KEYERROR,
     ACCOUNTCOMPLETION_ACTIVATE_MISSPELL,
     ACCOUNTCOMPLETION_ACTIVATE_TOOMANYINCORRECTTRIES,
     ACCOUNTCOMPLETION_ACTIVATE_KEYDIED,
     ACCOUNTCOMPLETION_ACTIVATE_ENTERCREDENTIALSAGAIN,
     ACCOUNTCOMPLETION_ACTIVATE_BUTTON,
     ACCOUNTCOMPLETION_ACTIVATE_COUNDOWNTEXT,
     ACCOUNTCOMPLETION_ALREADYLINKED_TITLE,
     ACCOUNTCOMPLETION_ALREADYLINKED_SUBTITLE,
     ACCOUNTCOMPLETION_EMAILOVERLAY_ERROR_CODEALREADYSENT,
     ACCOUNTCOMPLETION_EMAILOVERLAY_ALREADYCONFIRMED_TITLE,
     ACCOUNTCOMPLETION_EMAILOVERLAY_ALREADYCONFIRMED_SUBTITLE,
     ACCOUNTCOMPLETION_CREDENTIALS_TITLE,
     ACCOUNTCOMPLETION_CREDENTIALS_SUBTITLE,
     ACCOUNTCOMPLETION_BADPASSWORD,
     ACCOUNTCOMPLETION_PASSWORDISTOOSHORT,
     ACCOUNTCOMPLETION_PASSWORDISTOOLONG,
     ACCOUNTCOMPLETION_PASSWORDISWEAK,
     ACCOUNTCOMPLETION_DEMOCOMPLETE_TITLE,
     ACCOUNTCOMPLETION_DEMOCOMPLETE_DESCRIPTION,
     ACCOUNTCOMPLETION_DEMOCOMPLETE_BUTTON,
     ACCOUNTCOMPLETION_ERROR_NOTAVAILABLE,
     ACCOUNTCOMPLETION_ERROR_BUTTON_TRYAGAIN,
     ACCOUNTCOMPLETION_ERROR_TRYAGAINTIMERMESSAGE,
     ACCOUNTCOMPLETION_ERROR_BUTTON_CONTINUE,
     ACCOUNTCOMPLETION_ERROR_RENAMINGNOTAVAILABLE,
     ACCOUNTCOMPLETION_WAITING_CONFIRMATION,
     ACCOUNTCOMPLETION_WAITING_QUEUE,
     ACCOUNTCOMPLETION_CONTACTSUPPORT,
     ACCOUNTCOMPLETION_ERROR_SOMETHINGWENTWRONG,
     ACCOUNTCOMPLETION_ERROR_RENAMINGMALFUNCTION,
     ACCOUNTCOMPLETION_SPA_PASSWORDISWEAK,
     ACCOUNTCOMPLETION_LEAVESQUAD_TITLE,
     ACCOUNTCOMPLETION_LEAVESQUAD_MESSAGE,
     ACCOUNTCOMPLETION_LEAVESQUAD_SUBMIT,
     ACCOUNTCOMPLETION_LEAVESQUAD_CANCEL,
     ACCOUNTCOMPLETION_RENAMING_SKIP_TITLE,
     ACCOUNTCOMPLETION_RENAMING_SKIP_MESSAGE,
     ACCOUNTCOMPLETION_RENAMING_SKIP_SUBMIT,
     ACCOUNTCOMPLETION_RENAMING_SKIP_CANCEL,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_TITLE,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_SUBTITLE,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_BUTTON,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_FIELDNAME,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMEFORBIDDEN,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMEFORBIDDENPICKVARIANT,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETAKEN,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETAKENPICKVARIANT,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMEINVALID,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETOOSHORT,
     ACCOUNTCOMPLETION_RENAMINGOVERLAY_NAMETOOLONG,
     ACCOUNTCOMPLETION_RENAMINGCOMPLETEOVERLAY_TITLE,
     ACCOUNTCOMPLETION_RENAMINGCOMPLETEOVERLAY_SUBTITLE,
     DIALOGTEMPLATES_CONFIRM,
     DIALOGTEMPLATES_CANCEL,
     DIALOGTEMPLATES_OK,
     BATTLEROYALE_CONFIRMRENT_TESTDRIVE_BUTTON,
     BATTLEROYALE_CONFIRMRENT_TESTDRIVE_TITLE,
     BATTLEROYALE_CONFIRMRENT_TESTDRIVE_DESCRIPTION,
     BATTLEROYALE_CONFIRMRENT_RENT_BUTTON,
     BATTLEROYALE_CONFIRMRENT_RENT_TITLE,
     BATTLEROYALE_CONFIRMRENT_RENT_DESCRIPTION,
     BATTLEROYALE_CONFIRMRENT_RENTPRICE,
     BATTLEROYALE_CONFIRMRENT_EVENTENDSSOON,
     FREESKILLSLEARNING_TITLE_LEARNING,
     FREESKILLSLEARNING_TITLE_RELEARNING,
     FREESKILLSLEARNING_MESSAGE,
     PERKLEARNCONFIRM_TITLE,
     PERKLEARNCONFIRM_DESC,
     PERKLEARNCONFIRM_LEARN,
     COMP7_DESERTER_TITLE,
     COMP7_DESERTER_MSGTITLE,
     COMP7_DESERTER_MESSAGE,
     COMP7_DESERTER_SUBMIT,
     COMP7_DESERTER_CANCEL,
     COMP7_PUNISHMENTWINDOW_TITLE,
     COMP7_PUNISHMENTWINDOW_MSGTITLE,
     COMP7_PUNISHMENTWINDOW_MESSAGE,
     COMP7_PUNISHMENTWINDOW_CANCEL,
     EQUIPMENTUPGRADE_CONFIRMBUTTON,
     EQUIPMENTUPGRADE_GETMORECURRENCYBUTTON,
     EQUIPMENTUPGRADE_GETMORECURRENCYBUTTONTOOLTIP_BODY,
     EQUIPMENTUPGRADE_CANCELBUTTON,
     EQUIPMENTDECONSTRUCTION_CONFIRMBUTTON,
     EQUIPMENTDECONSTRUCTION_CONFIRMANDUPGRADEBUTTON,
     EQUIPMENTDECONSTRUCTION_CANCELBUTTON,
     PRICECARD_FREE_TITLE,
     PRICECARD_CREDITS_TITLE,
     PRICECARD_GOLD_TITLE,
     PRICECARD_RECERTIFICATION_TITLE,
     PRICECARD_PRICE_FREE,
     PERKSREST_TITLE,
     PERKSREST_FREE_DESCRIPTION,
     PERKSREST_BEFORE,
     PERKSREST_AFTER,
     PERKSREST_NONEWPERKS,
     PERKSREST_SUBMIT,
     PERKSREST_CANCEL,
     PERKSREST_PRICECARD_FREE_DESCRIPTION,
     PERKSREST_PRICECARD_CREDITS_DESCRIPTION,
     PERKSREST_PRICECARD_GOLD_DESCRIPTION,
     RETRAIN_HEADER,
     RETRAIN_TITLE_SINGLE,
     RETRAIN_TITLE_MASSIVE,
     RETRAIN_WARNING_PREMIUMVEHICLE,
     RETRAIN_PRICECARD_FREE_DESCRIPTION,
     RETRAIN_PRICECARD_CREDITS_DESCRIPTION,
     RETRAIN_PRICECARD_GOLD_DESCRIPTION,
     RETRAIN_MASSIVE_TANKMENCOUNT,
     RETRAIN_SINGLE_CHECKBOXLABEL,
     RETRAIN_PRICE,
     RETRAIN_SUBMIT,
     RETRAIN_CANCEL,
     RECRUIT_TITLE,
     RECRUIT_WARNING_PREMIUMVEHICLE,
     RECRUIT_PRICECARD_FREE_DESCRIPTION,
     RECRUIT_PRICECARD_CREDITS_DESCRIPTION,
     RECRUIT_PRICECARD_GOLD_DESCRIPTION,
     RECRUIT_SUBMIT,
     RECRUIT_CANCEL,
     TANKMANRETRAINING_SUBMIT,
     TANKMANRETRAINING_CANCEL,
     CREWMEMBERTANKCHANGE_TITLE,
     CREWMEMBERTANKCHANGE_DESC,
     CREWMEMBERTANKCHANGE_TRANSFER,
     CREWMEMBERROLECHANGE_TITLE_SIMPLE,
     CREWMEMBERROLECHANGE_TITLE_EXTENDED,
     CREWMEMBERROLECHANGE_BULLET,
     CREWMEMBERROLECHANGE_DESC_SIMPLE,
     CREWMEMBERROLECHANGE_DESC_WRONGSPECIALIZATION,
     CREWMEMBERROLECHANGE_DESC_PREMIUM,
     CREWMEMBERROLECHANGE_PRICE,
     CREWMEMBERROLECHANGE_CHANGE,
     RUDYINFO_TITLE,
     RUDYINFO_MESSAGE,
     RUDYINFO_SUBMIT,
     CREWBOOKPURCHASE_PURCHASE,
     CREWBOOKPURCHASE_PURCHASE_TITLE,
     CREWBOOKPURCHASE_DESCRIPTION_PERSONAL,
     CREWBOOKPURCHASE_DESCRIPTION_CREW,
     CREWBOOKPURCHASE_BTNDISABLEDTOOLTIP,
     SKINCHANGEDIALOG_TITLE,
     SKINCHANGEDIALOG_BUTTON_SUBMIT,
     SKINCHANGEDIALOG_TEXT,
     SKINCHANGEDIALOG_WARNING,
     SKINAPPLYDIALOG_BUTTON_SUBMIT,
     SKINAPPLYDIALOG_WARNING,
     DISMISSTANKMAN_HEADER,
     DISMISSTANKMAN_DESCRIPTION_TIME,
     DISMISSTANKMAN_DESCRIPTION_TIMETEXT,
     DISMISSTANKMAN_LIMITED,
     DISMISSTANKMAN_NORECOVERY,
     DISMISSTANKMAN_BUTTONS_DISMISS,
     DISMISSTANKMAN_BUTTONS_RESTORE,
     RESTORETANKMAN_HEADER,
     RESTORETANKMAN_DESCRIPTION,
     RESTORETANKMAN_PRICE,
     RESTORETANKMAN_FREE,
     RESTORETANKMAN_BUTTONS_RECOVER,
     DISMISSORRESTORE_HEADER_DISMISS,
     DISMISSORRESTORE_HEADER_RESTORE,
     DISMISSORRESTORE_SELECTTANKMANS_DISMISS,
     DISMISSORRESTORE_SELECTTANKMANS_RESTORE,
     DISMISSORRESTORE_RESTORE_CURRENCY,
     DISMISSORRESTORE_DISMISS_CAPCHA_TITLE_NORMAL,
     DISMISSORRESTORE_DISMISS_CAPCHA_TITLEHIGHLIGHT_NORMAL,
     DISMISSORRESTORE_ERROR_TEXT,
     DISMISSORRESTORE_LIMITERROR_ERROR,
     DISMISSORRESTORE_DISMISS_CAPCHA_TITLE_LIMITERROR,
     DISMISSORRESTORE_DISMISS_CAPCHA_TITLEHIGHLIGHT_LIMITERROR,
     DISMISSORRESTORE_DISMISS_CAPCHA_TITLEHIGHLIGHTKEYWORD,
     BUYBERTHSCONFIRMATION_MESSAGE,
     BUYBERTHSCONFIRMATION_TITLE,
     BUYBERTHSCONFIRMATION_SUBMIT,
     BUYBERTHSCONFIRMATION_CANCEL,
     BUYBERTHSNOTENOUGH_CREDITS_TITLE,
     BUYBERTHSNOTENOUGH_CREDITS_MESSAGE,
     BUYBERTHSNOTENOUGH_CREDITS_CANCEL,
     BUYBERTHS_HANGARBERTHS_HEADER)

    @classmethod
    def vehicleselldialog_vehicletype(cls, key0):
        outcome = (b'#dialogs:vehicleSellDialog/vehicleType/{}').format(key0)
        if outcome not in cls.VEHICLESELLDIALOG_VEHICLETYPE_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def all(cls, key0):
        outcome = (b'#dialogs:{}').format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
