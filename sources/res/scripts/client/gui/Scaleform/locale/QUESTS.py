from debug_utils import LOG_WARNING

class QUESTS(object):
    BONUSES_COMPENSATION = b'#quests:bonuses/compensation'
    MISSIONS_TAB_KURSK = b'#quests:missions/tab/kursk'
    MISSIONS_TAB_MARATHONS = b'#quests:missions/tab/marathons'
    MISSIONS_TAB_EVENTBOARDS = b'#quests:missions/tab/eventBoards'
    MISSIONS_TAB_CATEGORIES = b'#quests:missions/tab/categories'
    MISSIONS_TAB_CURRENTVEHICLE = b'#quests:missions/tab/currentVehicle'
    MISSIONS_TAB_BATTLE_PASS = b'#quests:missions/tab/battle_pass'
    MISSIONS_TAB_DAILY = b'#quests:missions/tab/daily'
    MISSIONS_TAB_MAPBOX = b'#quests:missions/tab/mapbox'
    MISSIONS_TAB_MAY21_MARATHON = b'#quests:missions/tab/may21_marathon'
    MISSIONS_TAB_BATTLEMATTERS = b'#quests:missions/tab/battleMatters'
    MISSIONS_TAB_WINBACK = b'#quests:missions/tab/winback'
    IGR_TOOLTIP_BATTLESLABEL = b'#quests:igr/tooltip/battlesLabel'
    IGR_TOOLTIP_WINSLABEL = b'#quests:igr/tooltip/winsLabel'
    POSTBATTLE_PROGRESSRESET = b'#quests:postBattle/progressReset'
    TOOLTIP_PROGRESS_GROUPBY_HEADER = b'#quests:tooltip/progress/groupBy/header'
    TOOLTIP_PROGRESS_GROUPBY_BODY = b'#quests:tooltip/progress/groupBy/body'
    TOOLTIP_PROGRESS_GROUPBY_NOTE = b'#quests:tooltip/progress/groupBy/note'
    TOOLTIP_PROGRESS_GROUPBY_NOTE_LEVEL = b'#quests:tooltip/progress/groupBy/note/level'
    TOOLTIP_VEHTABLE_NATION_HEADER = b'#quests:tooltip/vehTable/nation/header'
    TOOLTIP_VEHTABLE_NATION_BODY = b'#quests:tooltip/vehTable/nation/body'
    TOOLTIP_VEHTABLE_CLASS_HEADER = b'#quests:tooltip/vehTable/class/header'
    TOOLTIP_VEHTABLE_CLASS_BODY = b'#quests:tooltip/vehTable/class/body'
    TOOLTIP_VEHTABLE_LEVEL_HEADER = b'#quests:tooltip/vehTable/level/header'
    TOOLTIP_VEHTABLE_LEVEL_BODY = b'#quests:tooltip/vehTable/level/body'
    TOOLTIP_VEHTABLE_NAME_HEADER = b'#quests:tooltip/vehTable/name/header'
    TOOLTIP_VEHTABLE_NAME_BODY = b'#quests:tooltip/vehTable/name/body'
    TOOLTIP_VEHTABLE_AVAILABILITY_HEADER = b'#quests:tooltip/vehTable/availability/header'
    TOOLTIP_VEHTABLE_AVAILABILITY_BODY = b'#quests:tooltip/vehTable/availability/body'
    TOOLTIP_VEHTABLE_DISCOUNT_HEADER = b'#quests:tooltip/vehTable/discount/header'
    TOOLTIP_VEHTABLE_DISCOUNT_BODY = b'#quests:tooltip/vehTable/discount/body'
    BONUSES_COMPENSATION_HEADER = b'#quests:bonuses/compensation/header'
    BONUSES_COMPENSATION_BODY = b'#quests:bonuses/compensation/body'
    BONUSES_ITEMS_NAME = b'#quests:bonuses/items/name'
    BONUSES_BOOSTERS_NAME = b'#quests:bonuses/boosters/name'
    BONUSES_DISCOUNT_NAME = b'#quests:bonuses/discount/name'
    BONUSES_CUSTOMIZATION_VALUE = b'#quests:bonuses/customization/value'
    BONUSES_VEHICLES_NAME = b'#quests:bonuses/vehicles/name'
    BONUSES_VEHICLES_CREWLVL = b'#quests:bonuses/vehicles/crewLvl'
    BONUSES_VEHICLES_RENTDAYS = b'#quests:bonuses/vehicles/rentDays'
    BONUSES_VEHICLES_DESCRIPTION = b'#quests:bonuses/vehicles/description'
    BONUSES_ITEM_TANKMENXP = b'#quests:bonuses/item/tankmenXP'
    BONUSES_ITEM_XPFACTOR = b'#quests:bonuses/item/xpFactor'
    BONUSES_ITEM_CREDITSFACTOR = b'#quests:bonuses/item/creditsFactor'
    BONUSES_ITEM_FREEXPFACTOR = b'#quests:bonuses/item/freeXPFactor'
    BONUSES_ITEM_TANKMENXPFACTOR = b'#quests:bonuses/item/tankmenXPFactor'
    BONUSES_ITEM_SLOTS = b'#quests:bonuses/item/slots'
    BONUSES_ITEM_BERTHS = b'#quests:bonuses/item/berths'
    BONUSES_ITEM_PREMIUM = b'#quests:bonuses/item/premium'
    BONUSES_ITEM_PREMIUMPLUS = b'#quests:bonuses/item/premiumPlus'
    BONUSES_ITEM_CREWSKIN = b'#quests:bonuses/item/crewSkin'
    BONUSES_ITEM_LOOTBOXES = b'#quests:bonuses/item/lootBoxes'
    BONUSES_ITEM_LOCKPICK = b'#quests:bonuses/item/lockpick'
    BONUSES_ITEM_LOOTBOXKEY = b'#quests:bonuses/item/lootBoxKey'
    BONUSES_ITEM_EARLYACCESSTOKEN = b'#quests:bonuses/item/earlyAccessToken'
    BONUSNAME_BLUEPRINTS_ANY = b'#quests:bonusName/blueprints/any'
    BONUSES_CREWBOOK_TEXT = b'#quests:bonuses/crewBook/text'
    BONUSES_CREWSKIN_TEXT = b'#quests:bonuses/crewSkin/text'
    BONUSES_PREFERREDMAPSLOTS_POSTBATTLE = b'#quests:bonuses/preferredMapSlots/postBattle'
    BONUSES_DOSSIER_ACHIVE = b'#quests:bonuses/dossier/achive'
    BONUSES_DOSSIER_BADGE = b'#quests:bonuses/dossier/badge'
    BONUSNAME_BLUEPRINTS_VEHICLE = b'#quests:bonusName/blueprints/vehicle'
    BONUSNAME_BLUEPRINTS_VEHICLE_ANY = b'#quests:bonusName/blueprints/vehicle/any'
    BONUSNAME_BLUEPRINTS_NATION = b'#quests:bonusName/blueprints/nation'
    BONUSNAME_BLUEPRINTS_NATION_ANY = b'#quests:bonusName/blueprints/nation/any'
    BONUSNAME_BLUEPRINTS_UNIVERSAL = b'#quests:bonusName/blueprints/universal'
    BONUSNAME_PARAGONSUNLOCKS = b'#quests:bonusName/paragonsUnlocks'
    BONUSNAME_TMANTOKEN = b'#quests:bonusName/tmanToken'
    BONUSNAME_STYLEPROGRESS = b'#quests:bonusName/styleProgress'
    BONUSES_CREDITS_DESCRIPTION = b'#quests:bonuses/credits/description'
    BONUSES_GOLD_DESCRIPTION = b'#quests:bonuses/gold/description'
    BONUSES_CRYSTAL_DESCRIPTION = b'#quests:bonuses/crystal/description'
    BONUSES_EVENTCOIN_DESCRIPTION = b'#quests:bonuses/eventCoin/description'
    BONUSES_BPCOIN_DESCRIPTION = b'#quests:bonuses/bpcoin/description'
    BONUSES_FREEXP_DESCRIPTION = b'#quests:bonuses/freeXP/description'
    BONUSES_EQUIPCOIN_DESCRIPTION = b'#quests:bonuses/equipCoin/description'
    BONUSES_PREMIUM_PLUS_DESCRIPTION = b'#quests:bonuses/premium_plus/description'
    BONUSES_TANKMEN_DESCRIPTION = b'#quests:bonuses/tankmen/description'
    BONUSES_ITEM_TANKWOMAN = b'#quests:bonuses/item/tankwoman'
    BONUSES_ITEM_TANKMAN = b'#quests:bonuses/item/tankman'
    BONUSES_ITEM_ADDITIONBONUS = b'#quests:bonuses/item/additionBonus'
    BONUSES_ITEM_TANKMEN_NO_SKILLS = b'#quests:bonuses/item/tankmen/no_skills'
    BONUSES_ITEM_TANKMEN_WITH_SKILLS = b'#quests:bonuses/item/tankmen/with_skills'
    BONUSES_NOTAVAILABLE = b'#quests:bonuses/notAvailable'
    QUESTS_TITLE = b'#quests:quests/title'
    QUESTS_TITLE_MANEUVERSQUESTS = b'#quests:quests/title/maneuversQuests'
    QUESTS_TITLE_CURRENTLYAVAILABLE = b'#quests:quests/title/currentlyAvailable'
    QUESTS_TITLE_UNGOUPEDQUESTS = b'#quests:quests/title/ungoupedQuests'
    QUESTS_TITLE_LADDERQUESTS = b'#quests:quests/title/ladderQuests'
    QUESTS_TITLE_UNGOUPEDACTIONS = b'#quests:quests/title/ungoupedActions'
    QUESTS_CONDITIONS = b'#quests:quests/conditions'
    QUESTS_REQUIREMENTS = b'#quests:quests/requirements'
    QUESTS_EMPTY_QUESTS_HEADER = b'#quests:quests/empty/quests/header'
    QUESTS_EMPTY_QUESTS_BODY = b'#quests:quests/empty/quests/body'
    QUESTS_EMPTY_ACTIONS_HEADER = b'#quests:quests/empty/actions/header'
    QUESTS_EMPTY_ACTIONS_BODY = b'#quests:quests/empty/actions/body'
    QUESTS_EMPTY_VEHICLE_HEADER = b'#quests:quests/empty/vehicle/header'
    QUESTS_EMPTY_VEHICLE_BODY = b'#quests:quests/empty/vehicle/body'
    QUESTS_FUTURE_NODATA = b'#quests:quests/future/nodata'
    QUESTS_CONTENT_NOQUESTSINROAMING = b'#quests:quests/content/noQuestsInRoaming'
    QUESTS_TABS_PERSONAL = b'#quests:quests/tabs/personal'
    QUESTS_TABS_CURRENT = b'#quests:quests/tabs/current'
    QUESTS_TABS_LADDER = b'#quests:quests/tabs/ladder'
    QUESTS_TABS_BEGINNER = b'#quests:quests/tabs/beginner'
    QUESTS_TABS_FUTURE = b'#quests:quests/tabs/future'
    QUESTSCONTROL_TITLE = b'#quests:questsControl/title'
    QUESTS_STATUS_DONE = b'#quests:quests/status/done'
    QUESTS_STATUS_NOTAVAILABLE = b'#quests:quests/status/notAvailable'
    QUESTS_STATUS_NOTDONE = b'#quests:quests/status/notDone'
    QUESTS_STATUS_ALLDONE = b'#quests:quests/status/allDone'
    QUESTS_TABLE_NOVEHICLES = b'#quests:quests/table/noVehicles'
    QUESTS_TABLE_AMOUNT = b'#quests:quests/table/amount'
    QUESTS_TABLE_BATTLESLEFT = b'#quests:quests/table/battlesLeft'
    QUESTS_TABLE_INHANGAR = b'#quests:quests/table/inHangar'
    QUESTS_TABLE_NOTINHANGAR = b'#quests:quests/table/notInHangar'
    QUESTS_CURRENTTAB_HEADER_CHECKBOX_TEXT = b'#quests:quests/currentTab/header/checkBox/text'
    QUESTS_CURRENTTAB_HEADER_DROPDOWN_DATE = b'#quests:quests/currentTab/header/dropdown/date'
    QUESTS_CURRENTTAB_HEADER_DROPDOWN_TIME = b'#quests:quests/currentTab/header/dropdown/time'
    QUESTS_CURRENTTAB_HEADER_DROPDOWN_SPECIALMISSION = b'#quests:quests/currentTab/header/dropdown/specialMission'
    QUESTS_CURRENTTAB_HEADER_TAB_ALL = b'#quests:quests/currentTab/header/tab/all'
    QUESTS_CURRENTTAB_HEADER_TAB_ACTION = b'#quests:quests/currentTab/header/tab/action'
    QUESTS_CURRENTTAB_HEADER_TAB_VEHICLE = b'#quests:quests/currentTab/header/tab/vehicle'
    QUESTS_LIST_COMPLETE = b'#quests:quests/list/complete'
    QUESTS_LIST_CURRENT_NOALL = b'#quests:quests/list/current/noAll'
    QUESTS_LIST_CURRENT_NOQUESTS = b'#quests:quests/list/current/noQuests'
    QUESTS_LIST_CURRENT_NOACTIONS = b'#quests:quests/list/current/noActions'
    QUESTS_LIST_FUTURE_NOALL = b'#quests:quests/list/future/noAll'
    QUESTS_LIST_FUTURE_NOQUESTS = b'#quests:quests/list/future/noQuests'
    QUESTS_LIST_FUTURE_NOACTIONS = b'#quests:quests/list/future/noActions'
    QUESTS_LIST_CLICKCHECKBOX = b'#quests:quests/list/clickCheckbox'
    QUESTS_TABS_NOSELECTED_TEXT = b'#quests:quests/tabs/noselected/text'
    QUESTS_TABS_AWARD_TEXT = b'#quests:quests/tabs/award/text'
    QUESTS_TABS_ADDAWARD_TEXT = b'#quests:quests/tabs/addAward/text'
    ITEM_TYPE_ACTION = b'#quests:item/type/action'
    ITEM_TYPE_QUEST = b'#quests:item/type/quest'
    ITEM_TYPE_QUESTDAILY = b'#quests:item/type/questDaily'
    ITEM_TYPE_SPECIALMISSION = b'#quests:item/type/specialMission'
    ITEM_TYPE_QUESTSTRATEGIC = b'#quests:item/type/questStrategic'
    ITEM_TYPE_PERSONALMISSION = b'#quests:item/type/personalMission'
    ITEM_TYPE_LADDER = b'#quests:item/type/ladder'
    ITEM_TIMER_TILLSTART = b'#quests:item/timer/tillStart'
    ITEM_TIMER_TILLSTART_DAYS = b'#quests:item/timer/tillStart/days'
    ITEM_TIMER_TILLSTART_HOURS = b'#quests:item/timer/tillStart/hours'
    ITEM_TIMER_TILLSTART_MIN = b'#quests:item/timer/tillStart/min'
    ITEM_TIMER_TILLFINISH = b'#quests:item/timer/tillFinish'
    ITEM_TIMER_TILLFINISH_DAYS = b'#quests:item/timer/tillFinish/days'
    ITEM_TIMER_TILLFINISH_HOURS = b'#quests:item/timer/tillFinish/hours'
    ITEM_TIMER_TILLFINISH_LONGFORMAT = b'#quests:item/timer/tillFinish/longFormat'
    ITEM_TIMER_TILLFINISH_ONLYHOURS = b'#quests:item/timer/tillFinish/onlyHours'
    ITEM_TIMER_TILLFINISH_LESSTHANHOUR = b'#quests:item/timer/tillFinish/lessThanHour'
    ITEM_TIMER_TILLFINISH_LESSTHANDAY = b'#quests:item/timer/tillFinish/lessThanDay'
    ITEM_TIMER_TILLFINISH_SHORTFORMAT = b'#quests:item/timer/tillFinish/shortFormat'
    ITEM_TIMER_TILLFINISH_SHORTFULLFORMAT = b'#quests:item/timer/tillFinish/shortFullFormat'
    ITEM_TIMER_TILLFINISH_LONGFULLFORMAT = b'#quests:item/timer/tillFinish/longFullFormat'
    ITEM_TIMER_TILLFINISH_LONGFULLFORMATMIN = b'#quests:item/timer/tillFinish/longFullFormatMin'
    PERSONAL_SEASONS_AWARDSBUTTON = b'#quests:personal/seasons/awardsButton'
    PERSONAL_SEASONS_TAB_RANDOM = b'#quests:personal/seasons/tab/random'
    PERSONAL_SEASONS_TAB_FALLOUT = b'#quests:personal/seasons/tab/fallout'
    PERSONAL_SEASONS_ITEMTITLE = b'#quests:personal/seasons/itemTitle'
    PERSONAL_SEASONS_SHORTSEASONNAME = b'#quests:personal/seasons/shortSeasonName'
    PERSONAL_SEASONS_TILELABEL = b'#quests:personal/seasons/tileLabel'
    PERSONAL_SEASONS_TILEPROGRESS = b'#quests:personal/seasons/tileProgress'
    PERSONAL_SEASONS_SLOTS_NODATA = b'#quests:personal/seasons/slots/noData'
    PERSONAL_SEASONS_SLOTS_GETAWARD = b'#quests:personal/seasons/slots/getAward'
    PERSONAL_SEASONS_SLOTS_TITLE = b'#quests:personal/seasons/slots/title'
    PERSONAL_SEASONS_SLOTS_NOACTIVESLOTS_HEADER = b'#quests:personal/seasons/slots/noActiveSlots/header'
    PERSONAL_SEASONS_SLOTS_NOACTIVESLOTS_BODY = b'#quests:personal/seasons/slots/noActiveSlots/body'
    DETAILS_HEADER_INFO_TITLE = b'#quests:details/header/info/title'
    DETAILS_HEADER_INFO_DESCR_PARALLEL = b'#quests:details/header/info/descr_parallel'
    DETAILS_HEADER_INFO_DESCR_SERIAL = b'#quests:details/header/info/descr_serial'
    DETAILS_HEADER_TILLDATE = b'#quests:details/header/tillDate'
    DETAILS_HEADER_TILLDATETIMES = b'#quests:details/header/tillDateTimes'
    DETAILS_HEADER_TILLDATEDAYS = b'#quests:details/header/tillDateDays'
    DETAILS_HEADER_TILLDATEDAYSTIMES = b'#quests:details/header/tillDateDaysTimes'
    DETAILS_HEADER_ACTIVEDURATION = b'#quests:details/header/activeDuration'
    DETAILS_HEADER_ACTIVEDURATIONTIMES = b'#quests:details/header/activeDurationTimes'
    DETAILS_HEADER_ACTIVEDURATIONDAYS = b'#quests:details/header/activeDurationDays'
    DETAILS_HEADER_ACTIVEDURATIONDAYSTIMES = b'#quests:details/header/activeDurationDaysTimes'
    DETAILS_HEADER_SCHEDULEDAYS = b'#quests:details/header/scheduleDays'
    DETAILS_HEADER_SCHEDULETIMES = b'#quests:details/header/scheduleTimes'
    DETAILS_HEADER_SCHEDULEDAYSTIMES = b'#quests:details/header/scheduleDaysTimes'
    DETAILS_HEADER_HASNOVEHICLES = b'#quests:details/header/hasNoVehicles'
    DETAILS_HEADER_COMPLETION_DAILY = b'#quests:details/header/completion/daily'
    DETAILS_HEADER_COMPLETION_DAILY_GROUPBYVEHICLE = b'#quests:details/header/completion/daily/groupByVehicle'
    DETAILS_HEADER_COMPLETION_DAILY_GROUPBYNATION = b'#quests:details/header/completion/daily/groupByNation'
    DETAILS_HEADER_COMPLETION_DAILY_GROUPBYLEVEL = b'#quests:details/header/completion/daily/groupByLevel'
    DETAILS_HEADER_COMPLETION_DAILY_GROUPBYCLASS = b'#quests:details/header/completion/daily/groupByClass'
    DETAILS_HEADER_COMPLETION_UNLIMITED = b'#quests:details/header/completion/unlimited'
    DETAILS_HEADER_COMPLETION_SINGLE = b'#quests:details/header/completion/single'
    DETAILS_HEADER_COMPLETION_SINGLE_GROUPBYVEHICLE = b'#quests:details/header/completion/single/groupByVehicle'
    DETAILS_HEADER_COMPLETION_SINGLE_GROUPBYNATION = b'#quests:details/header/completion/single/groupByNation'
    DETAILS_HEADER_COMPLETION_SINGLE_GROUPBYLEVEL = b'#quests:details/header/completion/single/groupByLevel'
    DETAILS_HEADER_COMPLETION_SINGLE_GROUPBYCLASS = b'#quests:details/header/completion/single/groupByClass'
    DETAILS_HEADER_COMETOEND = b'#quests:details/header/comeToEnd'
    DETAILS_HEADER_COMETOENDINMINUTES = b'#quests:details/header/comeToEndInMinutes'
    DETAILS_HEADER_COMETOENDINMINUTES_SEPARATED = b'#quests:details/header/comeToEndInMinutes/separated'
    DETAILS_TASKS_SUBTASK = b'#quests:details/tasks/subTask'
    DETAILS_TASKS_NEXTTASK = b'#quests:details/tasks/nextTask'
    DETAILS_TASKS_STRATEGIC = b'#quests:details/tasks/strategic'
    DETAILS_TASKS_REQUIREMENTS_ACCOUNTLABEL = b'#quests:details/tasks/requirements/accountLabel'
    DETAILS_TASKS_REQUIREMENTS_VEHICLELABEL = b'#quests:details/tasks/requirements/vehicleLabel'
    DETAILS_TASKS_REQUIREMENTS_VEHICLELABEL_SUITABLE = b'#quests:details/tasks/requirements/vehicleLabel/suitable'
    DETAILS_TASKS_REQUIREMENTS_VEHICLELABEL_FROM = b'#quests:details/tasks/requirements/vehicleLabel/from'
    DETAILS_REQUIREMENTS_VEHICLESTABLE_NAME = b'#quests:details/requirements/vehiclesTable/name'
    DETAILS_REQUIREMENTS_VEHICLESTABLE_DISCOUNT = b'#quests:details/requirements/vehiclesTable/discount'
    DETAILS_REQUIREMENTS_VEHICLESTABLE_COUNT = b'#quests:details/requirements/vehiclesTable/count'
    DETAILS_CONDITIONS_LABEL = b'#quests:details/conditions/label'
    DETAILS_STATUS_COMPLETED = b'#quests:details/status/completed'
    DETAILS_STATUS_COMPLETED_DAILY = b'#quests:details/status/completed/daily'
    DETAILS_STATUS_COMPLETED_WEEKLY = b'#quests:details/status/completed/weekly'
    DETAILS_STATUS_NOTAVAILABLE_IN_FUTURE = b'#quests:details/status/notAvailable/in_future'
    DETAILS_STATUS_NOTAVAILABLE_INVALID_WEEKDAY = b'#quests:details/status/notAvailable/invalid_weekday'
    DETAILS_STATUS_NOTAVAILABLE_INVALID_TIME_INTERVAL = b'#quests:details/status/notAvailable/invalid_time_interval'
    DETAILS_STATUS_NOTAVAILABLE_OUT_OF_DATE = b'#quests:details/status/notAvailable/out_of_date'
    DETAILS_STATUS_NOTAVAILABLE_REQUIREMENTS = b'#quests:details/status/notAvailable/requirements'
    DETAILS_RELATIONS1_GREATER = b'#quests:details/relations1/greater'
    DETAILS_RELATIONS1_LESS = b'#quests:details/relations1/less'
    DETAILS_RELATIONS1_EQUAL = b'#quests:details/relations1/equal'
    DETAILS_RELATIONS1_NOTEQUAL = b'#quests:details/relations1/notEqual'
    DETAILS_RELATIONS1_LESSOREQUAL = b'#quests:details/relations1/lessOrEqual'
    DETAILS_RELATIONS1_GREATEROREQUAL = b'#quests:details/relations1/greaterOrEqual'
    DETAILS_RELATIONS2_GREATER = b'#quests:details/relations2/greater'
    DETAILS_RELATIONS2_LESS = b'#quests:details/relations2/less'
    DETAILS_RELATIONS2_EQUAL = b'#quests:details/relations2/equal'
    DETAILS_RELATIONS2_NOTEQUAL = b'#quests:details/relations2/notEqual'
    DETAILS_RELATIONS2_LESSOREQUAL = b'#quests:details/relations2/lessOrEqual'
    DETAILS_RELATIONS2_GREATEROREQUAL = b'#quests:details/relations2/greaterOrEqual'
    DETAILS_REQUIREMENTSRELATION_GREATER = b'#quests:details/requirementsRelation/greater'
    DETAILS_REQUIREMENTSRELATION_LESS = b'#quests:details/requirementsRelation/less'
    DETAILS_REQUIREMENTSRELATION_EQUAL = b'#quests:details/requirementsRelation/equal'
    DETAILS_REQUIREMENTSRELATION_NOTEQUAL = b'#quests:details/requirementsRelation/notEqual'
    DETAILS_REQUIREMENTSRELATION_LESSOREQUAL = b'#quests:details/requirementsRelation/lessOrEqual'
    DETAILS_REQUIREMENTSRELATION_GREATEROREQUAL = b'#quests:details/requirementsRelation/greaterOrEqual'
    DETAILS_GROUPS_OR = b'#quests:details/groups/or'
    DETAILS_REQUIREMENTS_IGR = b'#quests:details/requirements/igr'
    DETAILS_REQUIREMENTS_IGRBASIC = b'#quests:details/requirements/igrBasic'
    DETAILS_REQUIREMENTS_IGRPREMIUM = b'#quests:details/requirements/igrPremium'
    DETAILS_REQUIREMENTS_TOKEN = b'#quests:details/requirements/token'
    DETAILS_REQUIREMENTS_TOKEN_N = b'#quests:details/requirements/token/N'
    DETAILS_REQUIREMENTS_GROUP_TOKEN_N = b'#quests:details/requirements/group/token/N'
    DETAILS_REQUIREMENTS_PREMIUMACCOUNT = b'#quests:details/requirements/premiumAccount'
    DETAILS_REQUIREMENTS_NOTPREMIUMACCOUNT = b'#quests:details/requirements/notPremiumAccount'
    DETAILS_REQUIREMENTS_PREMIUMPLUSACCOUNT = b'#quests:details/requirements/premiumPlusAccount'
    DETAILS_REQUIREMENTS_WOTPLUS = b'#quests:details/requirements/wotPlus'
    DETAILS_REQUIREMENTS_WITHOUTWOTPLUS = b'#quests:details/requirements/withoutWotPlus'
    DETAILS_REQUIREMENTS_INCLAN = b'#quests:details/requirements/inClan'
    DETAILS_REQUIREMENTS_NOTINCLAN = b'#quests:details/requirements/notInClan'
    DETAILS_REQUIREMENTS_INANYCLAN = b'#quests:details/requirements/inAnyClan'
    DETAILS_REQUIREMENTS_NOTINANYCLAN = b'#quests:details/requirements/notInAnyClan'
    DETAILS_REQUIREMENTS_FORCURRENTCLAN = b'#quests:details/requirements/forCurrentClan'
    DETAILS_REQUIREMENTS_NOTFORCURRENTCLAN = b'#quests:details/requirements/notForCurrentClan'
    DETAILS_REQUIREMENTS_GLOBALRATING = b'#quests:details/requirements/globalRating'
    DETAILS_REQUIREMENTS_DOSSIERVALUE = b'#quests:details/requirements/dossierValue'
    DETAILS_REQUIREMENTS_DOSSIERAVGVALUE = b'#quests:details/requirements/dossierAvgValue'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED = b'#quests:details/requirements/vehiclesUnlocked'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NOT = b'#quests:details/requirements/vehiclesUnlocked/not'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_ALL = b'#quests:details/requirements/vehiclesUnlocked/all'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION = b'#quests:details/requirements/vehiclesUnlocked/nation'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION_NOT = b'#quests:details/requirements/vehiclesUnlocked/nation/not'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_TYPE = b'#quests:details/requirements/vehiclesUnlocked/type'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_TYPE_NOT = b'#quests:details/requirements/vehiclesUnlocked/type/not'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_LEVEL = b'#quests:details/requirements/vehiclesUnlocked/level'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_LEVEL_NOT = b'#quests:details/requirements/vehiclesUnlocked/level/not'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION_TYPE = b'#quests:details/requirements/vehiclesUnlocked/nation_type'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION_TYPE_NOT = b'#quests:details/requirements/vehiclesUnlocked/nation_type/not'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION_LEVEL = b'#quests:details/requirements/vehiclesUnlocked/nation_level'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION_LEVEL_NOT = b'#quests:details/requirements/vehiclesUnlocked/nation_level/not'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_TYPE_LEVEL = b'#quests:details/requirements/vehiclesUnlocked/type_level'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_TYPE_LEVEL_NOT = b'#quests:details/requirements/vehiclesUnlocked/type_level/not'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION_TYPE_LEVEL = b'#quests:details/requirements/vehiclesUnlocked/nation_type_level'
    DETAILS_REQUIREMENTS_VEHICLESUNLOCKED_NATION_TYPE_LEVEL_NOT = b'#quests:details/requirements/vehiclesUnlocked/nation_type_level/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED = b'#quests:details/requirements/vehiclesOwned'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NOT = b'#quests:details/requirements/vehiclesOwned/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_ALL = b'#quests:details/requirements/vehiclesOwned/all'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION = b'#quests:details/requirements/vehiclesOwned/nation'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION_NOT = b'#quests:details/requirements/vehiclesOwned/nation/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_TYPE = b'#quests:details/requirements/vehiclesOwned/type'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_TYPE_NOT = b'#quests:details/requirements/vehiclesOwned/type/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_LEVEL = b'#quests:details/requirements/vehiclesOwned/level'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_LEVEL_NOT = b'#quests:details/requirements/vehiclesOwned/level/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION_TYPE = b'#quests:details/requirements/vehiclesOwned/nation_type'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION_TYPE_NOT = b'#quests:details/requirements/vehiclesOwned/nation_type/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION_LEVEL = b'#quests:details/requirements/vehiclesOwned/nation_level'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION_LEVEL_NOT = b'#quests:details/requirements/vehiclesOwned/nation_level/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_TYPE_LEVEL = b'#quests:details/requirements/vehiclesOwned/type_level'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_TYPE_LEVEL_NOT = b'#quests:details/requirements/vehiclesOwned/type_level/not'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION_TYPE_LEVEL = b'#quests:details/requirements/vehiclesOwned/nation_type_level'
    DETAILS_REQUIREMENTS_VEHICLESOWNED_NATION_TYPE_LEVEL_NOT = b'#quests:details/requirements/vehiclesOwned/nation_type_level/not'
    DETAILS_REQUIREMENTS_VEHICLE_RECEIVEDMULTXP = b'#quests:details/requirements/vehicle/receivedMultXp'
    DETAILS_REQUIREMENTS_VEHICLE_NOTRECEIVEDMULTXP = b'#quests:details/requirements/vehicle/notReceivedMultXp'
    DETAILS_REQUIREMENTS_VEHICLE_ANY = b'#quests:details/requirements/vehicle/any'
    DETAILS_REQUIREMENTS_LADDER = b'#quests:details/requirements/ladder'
    DETAILS_REQUIREMENTS_RELATION = b'#quests:details/requirements/relation'
    DETAILS_CONDITIONS_TITLE = b'#quests:details/conditions/title'
    DETAILS_CONDITIONS_INSTALLEDMODULE_TITLE = b'#quests:details/conditions/installedModule/title'
    DETAILS_CONDITIONS_TARGET_TITLE = b'#quests:details/conditions/target/title'
    DETAILS_CONDITIONS_WIN_TITLE = b'#quests:details/conditions/win/title'
    DETAILS_CONDITIONS_WIN_DESCRIPTION = b'#quests:details/conditions/win/description'
    DETAILS_CONDITIONS_ALIVE_TITLE = b'#quests:details/conditions/alive/title'
    DETAILS_CONDITIONS_ALIVE_DESCRIPTION = b'#quests:details/conditions/alive/description'
    DETAILS_CONDITIONS_ACHIEVEMENTS_TITLE = b'#quests:details/conditions/achievements/title'
    DETAILS_CONDITIONS_CLANKILLS_TITLE = b'#quests:details/conditions/clanKills/title'
    DETAILS_CONDITIONS_VEHICLESKILLS_TITLE = b'#quests:details/conditions/vehiclesKills/title'
    DETAILS_CONDITIONS_VEHICLESKILLS_TITLE_NOT = b'#quests:details/conditions/vehiclesKills/title/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_TITLE = b'#quests:details/conditions/vehicleDamage/title'
    DETAILS_CONDITIONS_ADDITIONAL_TITLE = b'#quests:details/conditions/additional/title'
    DETAILS_CONDITIONS_INSTALLEDCAMOUFLAGE_TITLE = b'#quests:details/conditions/installedCamouflage/title'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_TITLE_NOT = b'#quests:details/conditions/vehicleDamage/title/not'
    DETAILS_CONDITIONS_VEHICLESTUN_TITLE = b'#quests:details/conditions/vehicleStun/title'
    DETAILS_CONDITIONS_MULTISTUNEVENT_TITLE = b'#quests:details/conditions/multiStunEvent/title'
    DETAILS_CONDITIONS_MULTISTUNEVENT_TITLE_NOT = b'#quests:details/conditions/multiStunEvent/title/not'
    DETAILS_CONDITIONS_VEHICLESTUN_TITLE_NOT = b'#quests:details/conditions/vehicleStun/title/not'
    DETAILS_CONDITIONS_FIREDAMAGE_TITLE = b'#quests:details/conditions/fireDamage/title'
    DETAILS_CONDITIONS_FIREDAMAGE_TITLE_NOT = b'#quests:details/conditions/fireDamage/title/not'
    DETAILS_CONDITIONS_RAMDAMAGE_TITLE = b'#quests:details/conditions/ramDamage/title'
    DETAILS_CONDITIONS_RAMDAMAGE_TITLE_NOT = b'#quests:details/conditions/ramDamage/title/not'
    DETAILS_CONDITIONS_PLAYBATTLE_TITLE = b'#quests:details/conditions/playBattle/title'
    DETAILS_CONDITIONS_TOP_TITLE = b'#quests:details/conditions/top/title'
    DETAILS_CONDITIONS_ALTERNATIVE = b'#quests:details/conditions/alternative'
    DETAILS_CONDITIONS_ADDITIONAL = b'#quests:details/conditions/additional'
    DETAILS_CONDITIONS_VEHICLEDESCR = b'#quests:details/conditions/vehicleDescr'
    DETAILS_CONDITIONS_VEHICLE = b'#quests:details/conditions/vehicle'
    DETAILS_CONDITIONS_VEHICLEKILLS = b'#quests:details/conditions/vehicleKills'
    DETAILS_CONDITIONS_VEHICLESUNLOCKED = b'#quests:details/conditions/vehiclesUnlocked'
    DETAILS_CONDITIONS_VEHICLESOWNED = b'#quests:details/conditions/vehiclesOwned'
    DETAILS_CONDITIONS_BATTLEBONUSTYPE = b'#quests:details/conditions/battleBonusType'
    DETAILS_CONDITIONS_FORMATION = b'#quests:details/conditions/formation'
    DETAILS_CONDITIONS_MAP = b'#quests:details/conditions/map'
    DETAILS_CONDITIONS_MAP_NOT = b'#quests:details/conditions/map/not'
    DETAILS_CONDITIONS_MAPS = b'#quests:details/conditions/maps'
    DETAILS_CONDITIONS_MAPS_NOT = b'#quests:details/conditions/maps/not'
    DETAILS_CONDITIONS_MAPSTYPE = b'#quests:details/conditions/mapsType'
    DETAILS_CONDITIONS_MAPSTYPE_SUMMER = b'#quests:details/conditions/mapsType/summer'
    DETAILS_CONDITIONS_MAPSTYPE_DESERT = b'#quests:details/conditions/mapsType/desert'
    DETAILS_CONDITIONS_MAPSTYPE_WINTER = b'#quests:details/conditions/mapsType/winter'
    DETAILS_CONDITIONS_FORMATION_SQUAD = b'#quests:details/conditions/formation/squad'
    DETAILS_CONDITIONS_NOTSQUAD = b'#quests:details/conditions/notSquad'
    DETAILS_CONDITIONS_CLANMEMBERSHIP_ANY_FORMATION = b'#quests:details/conditions/clanMembership/any/formation'
    DETAILS_CONDITIONS_CLANMEMBERSHIP_ANY_SQUAD = b'#quests:details/conditions/clanMembership/any/squad'
    DETAILS_CONDITIONS_CLANMEMBERSHIP_ANY_TEAM7X7 = b'#quests:details/conditions/clanMembership/any/team7x7'
    DETAILS_CONDITIONS_CLANMEMBERSHIP_SAME_FORMATION = b'#quests:details/conditions/clanMembership/same/formation'
    DETAILS_CONDITIONS_CLANMEMBERSHIP_SAME_SQUAD = b'#quests:details/conditions/clanMembership/same/squad'
    DETAILS_CONDITIONS_CLANMEMBERSHIP_SAME_TEAM7X7 = b'#quests:details/conditions/clanMembership/same/team7x7'
    DETAILS_CONDITIONS_FORMATION_CLAN = b'#quests:details/conditions/formation/clan'
    DETAILS_CONDITIONS_HISTORICALBATTLES = b'#quests:details/conditions/historicalBattles'
    DETAILS_CONDITIONS_BATTLES = b'#quests:details/conditions/battles'
    DETAILS_CONDITIONS_BATTLESINROW = b'#quests:details/conditions/battlesInRow'
    DETAILS_CONDITIONS_ACHIEVEMENTS = b'#quests:details/conditions/achievements'
    DETAILS_CONDITIONS_ACHIEVEMENTS_NOT = b'#quests:details/conditions/achievements/not'
    DETAILS_CONDITIONS_CLANKILLS = b'#quests:details/conditions/clanKills'
    DETAILS_CONDITIONS_CLANKILLS_NOT = b'#quests:details/conditions/clanKills/not'
    DETAILS_CONDITIONS_CLANKILLS_CAMO_RED = b'#quests:details/conditions/clanKills/camo/red'
    DETAILS_CONDITIONS_CLANKILLS_CAMO_SILVER = b'#quests:details/conditions/clanKills/camo/silver'
    DETAILS_CONDITIONS_CLANKILLS_CAMO_GOLD = b'#quests:details/conditions/clanKills/camo/gold'
    DETAILS_CONDITIONS_CLANKILLS_CAMO_BLACK = b'#quests:details/conditions/clanKills/camo/black'
    DETAILS_CONDITIONS_ONEACHIEVEMENT = b'#quests:details/conditions/oneAchievement'
    DETAILS_CONDITIONS_ONEACHIEVEMENT_NOT = b'#quests:details/conditions/oneAchievement/not'
    DETAILS_CONDITIONS_WIN = b'#quests:details/conditions/win'
    DETAILS_CONDITIONS_NOTWIN = b'#quests:details/conditions/notWin'
    DETAILS_CONDITIONS_SURVIVE = b'#quests:details/conditions/survive'
    DETAILS_CONDITIONS_NOTSURVIVE = b'#quests:details/conditions/notSurvive'
    DETAILS_CONDITIONS_INSTALLEDCAMOUFLAGE = b'#quests:details/conditions/installedCamouflage'
    DETAILS_CONDITIONS_NOINSTALLEDCAMOUFLAGE = b'#quests:details/conditions/noInstalledCamouflage'
    DETAILS_CONDITIONS_RESULTS_SINGLE_SIMPLE = b'#quests:details/conditions/results/single/simple'
    DETAILS_CONDITIONS_RESULTS_SINGLE_AVG = b'#quests:details/conditions/results/single/avg'
    DETAILS_CONDITIONS_RESULTS_SINGLE_HALFTEAM_TOP = b'#quests:details/conditions/results/single/halfTeam/top'
    DETAILS_CONDITIONS_RESULTS_SINGLE_HALFTEAM_TOP_NOT = b'#quests:details/conditions/results/single/halfTeam/top/not'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BATTLEROYALE_TOP1 = b'#quests:details/conditions/results/single/battleRoyale/top1'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BOTHTEAMS_TOP = b'#quests:details/conditions/results/single/bothTeams/top'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BOTHTEAMS_TOP1 = b'#quests:details/conditions/results/single/bothTeams/top1'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BOTHTEAMS_TOP_NOT = b'#quests:details/conditions/results/single/bothTeams/top/not'
    DETAILS_CONDITIONS_RESULTS_SINGLE_HALFTEAM_RANGE = b'#quests:details/conditions/results/single/halfTeam/range'
    DETAILS_CONDITIONS_RESULTS_SINGLE_HALFTEAM_RANGE_NOT = b'#quests:details/conditions/results/single/halfTeam/range/not'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BOTHTEAMS_RANGE = b'#quests:details/conditions/results/single/bothTeams/range'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BOTHTEAMS_RANGE_NOT = b'#quests:details/conditions/results/single/bothTeams/range/not'
    DETAILS_CONDITIONS_RESULTS_SINGLE_HALFTEAM_POSITION = b'#quests:details/conditions/results/single/halfTeam/position'
    DETAILS_CONDITIONS_RESULTS_SINGLE_HALFTEAM_POSITION_NOT = b'#quests:details/conditions/results/single/halfTeam/position/not'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BOTHTEAMS_POSITION = b'#quests:details/conditions/results/single/bothTeams/position'
    DETAILS_CONDITIONS_RESULTS_SINGLE_BOTHTEAMS_POSITION_NOT = b'#quests:details/conditions/results/single/bothTeams/position/not'
    DETAILS_CONDITIONS_RESULTS_FORMATION_ALIVE = b'#quests:details/conditions/results/formation/alive'
    DETAILS_CONDITIONS_RESULTS_FORMATION_ALIVE_NOT = b'#quests:details/conditions/results/formation/alive/not'
    DETAILS_CONDITIONS_RESULTS_FORMATION_SIMPLE = b'#quests:details/conditions/results/formation/simple'
    DETAILS_CONDITIONS_RESULTS_FORMATION_AVG = b'#quests:details/conditions/results/formation/avg'
    DETAILS_CONDITIONS_RESULTS_SQUAD_ALIVE = b'#quests:details/conditions/results/squad/alive'
    DETAILS_CONDITIONS_RESULTS_SQUAD_ALIVE_NOT = b'#quests:details/conditions/results/squad/alive/not'
    DETAILS_CONDITIONS_RESULTS_SQUAD_SIMPLE = b'#quests:details/conditions/results/squad/simple'
    DETAILS_CONDITIONS_RESULTS_SQUAD_AVG = b'#quests:details/conditions/results/squad/avg'
    DETAILS_CONDITIONS_RESULTS_TEAM7X7_ALIVE = b'#quests:details/conditions/results/team7x7/alive'
    DETAILS_CONDITIONS_RESULTS_TEAM7X7_ALIVE_NOT = b'#quests:details/conditions/results/team7x7/alive/not'
    DETAILS_CONDITIONS_RESULTS_TEAM7X7_SIMPLE = b'#quests:details/conditions/results/team7x7/simple'
    DETAILS_CONDITIONS_RESULTS_TEAM7X7_AVG = b'#quests:details/conditions/results/team7x7/avg'
    DETAILS_CONDITIONS_CUMULATIVE_SINGLE = b'#quests:details/conditions/cumulative/single'
    DETAILS_CONDITIONS_CUMULATIVE_FORMATION = b'#quests:details/conditions/cumulative/formation'
    DETAILS_CONDITIONS_CUMULATIVE_SQUAD = b'#quests:details/conditions/cumulative/squad'
    DETAILS_CONDITIONS_CUMULATIVE_TEAM7X7 = b'#quests:details/conditions/cumulative/team7x7'
    DETAILS_CONDITIONS_VEHICLESKILLS = b'#quests:details/conditions/vehiclesKills'
    DETAILS_CONDITIONS_VEHICLESKILLS_NOT = b'#quests:details/conditions/vehiclesKills/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_ALL = b'#quests:details/conditions/vehiclesKills/all'
    DETAILS_CONDITIONS_VEHICLESKILLS_ALL_NOT = b'#quests:details/conditions/vehiclesKills/all/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_LIST = b'#quests:details/conditions/vehiclesKills/list'
    DETAILS_CONDITIONS_VEHICLESKILLS_LIST_NOT = b'#quests:details/conditions/vehiclesKills/list/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION = b'#quests:details/conditions/vehiclesKills/nation'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION_NOT = b'#quests:details/conditions/vehiclesKills/nation/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_TYPE = b'#quests:details/conditions/vehiclesKills/type'
    DETAILS_CONDITIONS_VEHICLESKILLS_TYPE_NOT = b'#quests:details/conditions/vehiclesKills/type/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_LEVEL = b'#quests:details/conditions/vehiclesKills/level'
    DETAILS_CONDITIONS_VEHICLESKILLS_LEVEL_NOT = b'#quests:details/conditions/vehiclesKills/level/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION_TYPE = b'#quests:details/conditions/vehiclesKills/nation_type'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION_TYPE_NOT = b'#quests:details/conditions/vehiclesKills/nation_type/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION_LEVEL = b'#quests:details/conditions/vehiclesKills/nation_level'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION_LEVEL_NOT = b'#quests:details/conditions/vehiclesKills/nation_level/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_TYPE_LEVEL = b'#quests:details/conditions/vehiclesKills/type_level'
    DETAILS_CONDITIONS_VEHICLESKILLS_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehiclesKills/type_level/not'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION_TYPE_LEVEL = b'#quests:details/conditions/vehiclesKills/nation_type_level'
    DETAILS_CONDITIONS_VEHICLESKILLS_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehiclesKills/nation_type_level/not'
    DETAILS_CONDITIONS_FIREKILLS = b'#quests:details/conditions/fireKills'
    DETAILS_CONDITIONS_FIREKILLS_NOT = b'#quests:details/conditions/fireKills/not'
    DETAILS_CONDITIONS_FIREKILLS_ALL_NOT = b'#quests:details/conditions/fireKills/all/not'
    DETAILS_CONDITIONS_FIREKILLS_ALL = b'#quests:details/conditions/fireKills/all'
    DETAILS_CONDITIONS_FIREKILLS_LIST = b'#quests:details/conditions/fireKills/list'
    DETAILS_CONDITIONS_FIREKILLS_LIST_NOT = b'#quests:details/conditions/fireKills/list/not'
    DETAILS_CONDITIONS_FIREKILLS_NATION = b'#quests:details/conditions/fireKills/nation'
    DETAILS_CONDITIONS_FIREKILLS_NATION_NOT = b'#quests:details/conditions/fireKills/nation/not'
    DETAILS_CONDITIONS_FIREKILLS_TYPE = b'#quests:details/conditions/fireKills/type'
    DETAILS_CONDITIONS_FIREKILLS_TYPE_NOT = b'#quests:details/conditions/fireKills/type/not'
    DETAILS_CONDITIONS_FIREKILLS_LEVEL = b'#quests:details/conditions/fireKills/level'
    DETAILS_CONDITIONS_FIREKILLS_LEVEL_NOT = b'#quests:details/conditions/fireKills/level/not'
    DETAILS_CONDITIONS_FIREKILLS_NATION_TYPE = b'#quests:details/conditions/fireKills/nation_type'
    DETAILS_CONDITIONS_FIREKILLS_NATION_TYPE_NOT = b'#quests:details/conditions/fireKills/nation_type/not'
    DETAILS_CONDITIONS_FIREKILLS_NATION_LEVEL = b'#quests:details/conditions/fireKills/nation_level'
    DETAILS_CONDITIONS_FIREKILLS_NATION_LEVEL_NOT = b'#quests:details/conditions/fireKills/nation_level/not'
    DETAILS_CONDITIONS_FIREKILLS_TYPE_LEVEL = b'#quests:details/conditions/fireKills/type_level'
    DETAILS_CONDITIONS_FIREKILLS_TYPE_LEVEL_NOT = b'#quests:details/conditions/fireKills/type_level/not'
    DETAILS_CONDITIONS_FIREKILLS_NATION_TYPE_LEVEL = b'#quests:details/conditions/fireKills/nation_type_level'
    DETAILS_CONDITIONS_FIREKILLS_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/fireKills/nation_type_level/not'
    DETAILS_CONDITIONS_RAMKILLS = b'#quests:details/conditions/ramKills'
    DETAILS_CONDITIONS_RAMKILLS_NOT = b'#quests:details/conditions/ramKills/not'
    DETAILS_CONDITIONS_RAMKILLS_ALL_NOT = b'#quests:details/conditions/ramKills/all/not'
    DETAILS_CONDITIONS_RAMKILLS_ALL = b'#quests:details/conditions/ramKills/all'
    DETAILS_CONDITIONS_RAMKILLS_LIST = b'#quests:details/conditions/ramKills/list'
    DETAILS_CONDITIONS_RAMKILLS_LIST_NOT = b'#quests:details/conditions/ramKills/list/not'
    DETAILS_CONDITIONS_RAMKILLS_NATION = b'#quests:details/conditions/ramKills/nation'
    DETAILS_CONDITIONS_RAMKILLS_NATION_NOT = b'#quests:details/conditions/ramKills/nation/not'
    DETAILS_CONDITIONS_RAMKILLS_TYPE = b'#quests:details/conditions/ramKills/type'
    DETAILS_CONDITIONS_RAMKILLS_TYPE_NOT = b'#quests:details/conditions/ramKills/type/not'
    DETAILS_CONDITIONS_RAMKILLS_LEVEL = b'#quests:details/conditions/ramKills/level'
    DETAILS_CONDITIONS_RAMKILLS_LEVEL_NOT = b'#quests:details/conditions/ramKills/level/not'
    DETAILS_CONDITIONS_RAMKILLS_NATION_TYPE = b'#quests:details/conditions/ramKills/nation_type'
    DETAILS_CONDITIONS_RAMKILLS_NATION_TYPE_NOT = b'#quests:details/conditions/ramKills/nation_type/not'
    DETAILS_CONDITIONS_RAMKILLS_NATION_LEVEL = b'#quests:details/conditions/ramKills/nation_level'
    DETAILS_CONDITIONS_RAMKILLS_NATION_LEVEL_NOT = b'#quests:details/conditions/ramKills/nation_level/not'
    DETAILS_CONDITIONS_RAMKILLS_TYPE_LEVEL = b'#quests:details/conditions/ramKills/type_level'
    DETAILS_CONDITIONS_RAMKILLS_TYPE_LEVEL_NOT = b'#quests:details/conditions/ramKills/type_level/not'
    DETAILS_CONDITIONS_RAMKILLS_NATION_TYPE_LEVEL = b'#quests:details/conditions/ramKills/nation_type_level'
    DETAILS_CONDITIONS_RAMKILLS_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/ramKills/nation_type_level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE = b'#quests:details/conditions/vehicleDamage'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NOT = b'#quests:details/conditions/vehicleDamage/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_ALL = b'#quests:details/conditions/vehicleDamage/all'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_ALL_NOT = b'#quests:details/conditions/vehicleDamage/all/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION = b'#quests:details/conditions/vehicleDamage/nation'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION_NOT = b'#quests:details/conditions/vehicleDamage/nation/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_TYPE = b'#quests:details/conditions/vehicleDamage/type'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_TYPE_NOT = b'#quests:details/conditions/vehicleDamage/type/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_LEVEL = b'#quests:details/conditions/vehicleDamage/level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION_TYPE = b'#quests:details/conditions/vehicleDamage/nation_type'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION_TYPE_NOT = b'#quests:details/conditions/vehicleDamage/nation_type/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION_LEVEL = b'#quests:details/conditions/vehicleDamage/nation_level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/nation_level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_TYPE_LEVEL = b'#quests:details/conditions/vehicleDamage/type_level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/type_level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION_TYPE_LEVEL = b'#quests:details/conditions/vehicleDamage/nation_type_level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/nation_type_level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT = b'#quests:details/conditions/vehicleDamage/eventCount'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_ALL = b'#quests:details/conditions/vehicleDamage/eventCount/all'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_ALL_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/all/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION = b'#quests:details/conditions/vehicleDamage/eventCount/nation'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/nation/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_TYPE = b'#quests:details/conditions/vehicleDamage/eventCount/type'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_TYPE_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/type/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_LEVEL = b'#quests:details/conditions/vehicleDamage/eventCount/level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION_TYPE = b'#quests:details/conditions/vehicleDamage/eventCount/nation_type'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION_TYPE_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/nation_type/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION_LEVEL = b'#quests:details/conditions/vehicleDamage/eventCount/nation_level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/nation_level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_TYPE_LEVEL = b'#quests:details/conditions/vehicleDamage/eventCount/type_level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/type_level/not'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION_TYPE_LEVEL = b'#quests:details/conditions/vehicleDamage/eventCount/nation_type_level'
    DETAILS_CONDITIONS_VEHICLEDAMAGE_EVENTCOUNT_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleDamage/eventCount/nation_type_level/not'
    DETAILS_CONDITIONS_FIREDAMAGE = b'#quests:details/conditions/fireDamage'
    DETAILS_CONDITIONS_FIREDAMAGE_NOT = b'#quests:details/conditions/fireDamage/not'
    DETAILS_CONDITIONS_FIREDAMAGE_ALL = b'#quests:details/conditions/fireDamage/all'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION = b'#quests:details/conditions/fireDamage/nation'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION_NOT = b'#quests:details/conditions/fireDamage/nation/not'
    DETAILS_CONDITIONS_FIREDAMAGE_TYPE = b'#quests:details/conditions/fireDamage/type'
    DETAILS_CONDITIONS_FIREDAMAGE_TYPE_NOT = b'#quests:details/conditions/fireDamage/type/not'
    DETAILS_CONDITIONS_FIREDAMAGE_LEVEL = b'#quests:details/conditions/fireDamage/level'
    DETAILS_CONDITIONS_FIREDAMAGE_LEVEL_NOT = b'#quests:details/conditions/fireDamage/level/not'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION_TYPE = b'#quests:details/conditions/fireDamage/nation_type'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION_TYPE_NOT = b'#quests:details/conditions/fireDamage/nation_type/not'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION_LEVEL = b'#quests:details/conditions/fireDamage/nation_level'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION_LEVEL_NOT = b'#quests:details/conditions/fireDamage/nation_level/not'
    DETAILS_CONDITIONS_FIREDAMAGE_TYPE_LEVEL = b'#quests:details/conditions/fireDamage/type_level'
    DETAILS_CONDITIONS_FIREDAMAGE_TYPE_LEVEL_NOT = b'#quests:details/conditions/fireDamage/type_level/not'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION_TYPE_LEVEL = b'#quests:details/conditions/fireDamage/nation_type_level'
    DETAILS_CONDITIONS_FIREDAMAGE_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/fireDamage/nation_type_level/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT = b'#quests:details/conditions/fireDamage/eventCount'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NOT = b'#quests:details/conditions/fireDamage/eventCount/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_ALL = b'#quests:details/conditions/fireDamage/eventCount/all'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_ALL_NOT = b'#quests:details/conditions/fireDamage/eventCount/all/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION = b'#quests:details/conditions/fireDamage/eventCount/nation'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION_NOT = b'#quests:details/conditions/fireDamage/eventCount/nation/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_TYPE = b'#quests:details/conditions/fireDamage/eventCount/type'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_TYPE_NOT = b'#quests:details/conditions/fireDamage/eventCount/type/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_LEVEL = b'#quests:details/conditions/fireDamage/eventCount/level'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_LEVEL_NOT = b'#quests:details/conditions/fireDamage/eventCount/level/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION_TYPE = b'#quests:details/conditions/fireDamage/eventCount/nation_type'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION_TYPE_NOT = b'#quests:details/conditions/fireDamage/eventCount/nation_type/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION_LEVEL = b'#quests:details/conditions/fireDamage/eventCount/nation_level'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION_LEVEL_NOT = b'#quests:details/conditions/fireDamage/eventCount/nation_level/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_TYPE_LEVEL = b'#quests:details/conditions/fireDamage/eventCount/type_level'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_TYPE_LEVEL_NOT = b'#quests:details/conditions/fireDamage/eventCount/type_level/not'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION_TYPE_LEVEL = b'#quests:details/conditions/fireDamage/eventCount/nation_type_level'
    DETAILS_CONDITIONS_FIREDAMAGE_EVENTCOUNT_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/fireDamage/eventCount/nation_type_level/not'
    DETAILS_CONDITIONS_RAMDAMAGE = b'#quests:details/conditions/ramDamage'
    DETAILS_CONDITIONS_RAMDAMAGE_NOT = b'#quests:details/conditions/ramDamage/not'
    DETAILS_CONDITIONS_RAMDAMAGE_ALL = b'#quests:details/conditions/ramDamage/all'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION = b'#quests:details/conditions/ramDamage/nation'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION_NOT = b'#quests:details/conditions/ramDamage/nation/not'
    DETAILS_CONDITIONS_RAMDAMAGE_TYPE = b'#quests:details/conditions/ramDamage/type'
    DETAILS_CONDITIONS_RAMDAMAGE_TYPE_NOT = b'#quests:details/conditions/ramDamage/type/not'
    DETAILS_CONDITIONS_RAMDAMAGE_LEVEL = b'#quests:details/conditions/ramDamage/level'
    DETAILS_CONDITIONS_RAMDAMAGE_LEVEL_NOT = b'#quests:details/conditions/ramDamage/level/not'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION_TYPE = b'#quests:details/conditions/ramDamage/nation_type'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION_TYPE_NOT = b'#quests:details/conditions/ramDamage/nation_type/not'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION_LEVEL = b'#quests:details/conditions/ramDamage/nation_level'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION_LEVEL_NOT = b'#quests:details/conditions/ramDamage/nation_level/not'
    DETAILS_CONDITIONS_RAMDAMAGE_TYPE_LEVEL = b'#quests:details/conditions/ramDamage/type_level'
    DETAILS_CONDITIONS_RAMDAMAGE_TYPE_LEVEL_NOT = b'#quests:details/conditions/ramDamage/type_level/not'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION_TYPE_LEVEL = b'#quests:details/conditions/ramDamage/nation_type_level'
    DETAILS_CONDITIONS_RAMDAMAGE_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/ramDamage/nation_type_level/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT = b'#quests:details/conditions/ramDamage/eventCount'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NOT = b'#quests:details/conditions/ramDamage/eventCount/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_ALL = b'#quests:details/conditions/ramDamage/eventCount/all'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_ALL_NOT = b'#quests:details/conditions/ramDamage/eventCount/all/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION = b'#quests:details/conditions/ramDamage/eventCount/nation'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION_NOT = b'#quests:details/conditions/ramDamage/eventCount/nation/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_TYPE = b'#quests:details/conditions/ramDamage/eventCount/type'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_TYPE_NOT = b'#quests:details/conditions/ramDamage/eventCount/type/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_LEVEL = b'#quests:details/conditions/ramDamage/eventCount/level'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_LEVEL_NOT = b'#quests:details/conditions/ramDamage/eventCount/level/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION_TYPE = b'#quests:details/conditions/ramDamage/eventCount/nation_type'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION_TYPE_NOT = b'#quests:details/conditions/ramDamage/eventCount/nation_type/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION_LEVEL = b'#quests:details/conditions/ramDamage/eventCount/nation_level'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION_LEVEL_NOT = b'#quests:details/conditions/ramDamage/eventCount/nation_level/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_TYPE_LEVEL = b'#quests:details/conditions/ramDamage/eventCount/type_level'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_TYPE_LEVEL_NOT = b'#quests:details/conditions/ramDamage/eventCount/type_level/not'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION_TYPE_LEVEL = b'#quests:details/conditions/ramDamage/eventCount/nation_type_level'
    DETAILS_CONDITIONS_RAMDAMAGE_EVENTCOUNT_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/ramDamage/eventCount/nation_type_level/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_TRACK = b'#quests:details/conditions/crits/destroyed/track'
    DETAILS_CONDITIONS_CRITS_DESTROYED_TRACK_NOT = b'#quests:details/conditions/crits/destroyed/track/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_ENGINE = b'#quests:details/conditions/crits/destroyed/engine'
    DETAILS_CONDITIONS_CRITS_DESTROYED_ENGINE_NOT = b'#quests:details/conditions/crits/destroyed/engine/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_AMMOBAY = b'#quests:details/conditions/crits/destroyed/ammoBay'
    DETAILS_CONDITIONS_CRITS_DESTROYED_AMMOBAY_NOT = b'#quests:details/conditions/crits/destroyed/ammoBay/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_FUELTANK = b'#quests:details/conditions/crits/destroyed/fuelTank'
    DETAILS_CONDITIONS_CRITS_DESTROYED_FUELTANK_NOT = b'#quests:details/conditions/crits/destroyed/fuelTank/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_RADIO = b'#quests:details/conditions/crits/destroyed/radio'
    DETAILS_CONDITIONS_CRITS_DESTROYED_RADIO_NOT = b'#quests:details/conditions/crits/destroyed/radio/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_GUN = b'#quests:details/conditions/crits/destroyed/gun'
    DETAILS_CONDITIONS_CRITS_DESTROYED_GUN_NOT = b'#quests:details/conditions/crits/destroyed/gun/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_TURRETROTATOR = b'#quests:details/conditions/crits/destroyed/turretRotator'
    DETAILS_CONDITIONS_CRITS_DESTROYED_TURRETROTATOR_NOT = b'#quests:details/conditions/crits/destroyed/turretRotator/not'
    DETAILS_CONDITIONS_CRITS_DESTROYED_SURVEYINGDEVICE = b'#quests:details/conditions/crits/destroyed/surveyingDevice'
    DETAILS_CONDITIONS_CRITS_DESTROYED_SURVEYINGDEVICE_NOT = b'#quests:details/conditions/crits/destroyed/surveyingDevice/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_TRACK = b'#quests:details/conditions/crits/critical/track'
    DETAILS_CONDITIONS_CRITS_CRITICAL_TRACK_NOT = b'#quests:details/conditions/crits/critical/track/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_ENGINE = b'#quests:details/conditions/crits/critical/engine'
    DETAILS_CONDITIONS_CRITS_CRITICAL_ENGINE_NOT = b'#quests:details/conditions/crits/critical/engine/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_AMMOBAY = b'#quests:details/conditions/crits/critical/ammoBay'
    DETAILS_CONDITIONS_CRITS_CRITICAL_AMMOBAY_NOT = b'#quests:details/conditions/crits/critical/ammoBay/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_FUELTANK = b'#quests:details/conditions/crits/critical/fuelTank'
    DETAILS_CONDITIONS_CRITS_CRITICAL_FUELTANK_NOT = b'#quests:details/conditions/crits/critical/fuelTank/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_RADIO = b'#quests:details/conditions/crits/critical/radio'
    DETAILS_CONDITIONS_CRITS_CRITICAL_RADIO_NOT = b'#quests:details/conditions/crits/critical/radio/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_GUN = b'#quests:details/conditions/crits/critical/gun'
    DETAILS_CONDITIONS_CRITS_CRITICAL_GUN_NOT = b'#quests:details/conditions/crits/critical/gun/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_TURRETROTATOR = b'#quests:details/conditions/crits/critical/turretRotator'
    DETAILS_CONDITIONS_CRITS_CRITICAL_TURRETROTATOR_NOT = b'#quests:details/conditions/crits/critical/turretRotator/not'
    DETAILS_CONDITIONS_CRITS_CRITICAL_SURVEYINGDEVICE = b'#quests:details/conditions/crits/critical/surveyingDevice'
    DETAILS_CONDITIONS_CRITS_CRITICAL_SURVEYINGDEVICE_NOT = b'#quests:details/conditions/crits/critical/surveyingDevice/not'
    DETAILS_CONDITIONS_CRITS_TANKMAN_COMMANDER = b'#quests:details/conditions/crits/tankman/commander'
    DETAILS_CONDITIONS_CRITS_TANKMAN_COMMANDER_NOT = b'#quests:details/conditions/crits/tankman/commander/not'
    DETAILS_CONDITIONS_CRITS_TANKMAN_DRIVER = b'#quests:details/conditions/crits/tankman/driver'
    DETAILS_CONDITIONS_CRITS_TANKMAN_DRIVER_NOT = b'#quests:details/conditions/crits/tankman/driver/not'
    DETAILS_CONDITIONS_CRITS_TANKMAN_GUNNER = b'#quests:details/conditions/crits/tankman/gunner'
    DETAILS_CONDITIONS_CRITS_TANKMAN_GUNNER_NOT = b'#quests:details/conditions/crits/tankman/gunner/not'
    DETAILS_CONDITIONS_CRITS_TANKMAN_LOADER = b'#quests:details/conditions/crits/tankman/loader'
    DETAILS_CONDITIONS_CRITS_TANKMAN_LOADER_NOT = b'#quests:details/conditions/crits/tankman/loader/not'
    DETAILS_CONDITIONS_CRITS_TANKMAN_RADIOMAN = b'#quests:details/conditions/crits/tankman/radioman'
    DETAILS_CONDITIONS_CRITS_TANKMAN_RADIOMAN_NOT = b'#quests:details/conditions/crits/tankman/radioman/not'
    DETAILS_CONDITIONS_INSTALLEDMODULE_GUNS = b'#quests:details/conditions/installedModule/guns'
    DETAILS_CONDITIONS_INSTALLEDMODULE_ENGINES = b'#quests:details/conditions/installedModule/engines'
    DETAILS_CONDITIONS_INSTALLEDMODULE_CHASSIS = b'#quests:details/conditions/installedModule/chassis'
    DETAILS_CONDITIONS_INSTALLEDMODULE_TURRETS = b'#quests:details/conditions/installedModule/turrets'
    DETAILS_CONDITIONS_INSTALLEDMODULE_RADIOS = b'#quests:details/conditions/installedModule/radios'
    DETAILS_CONDITIONS_INSTALLEDMODULE_OPTIONALDEVICE = b'#quests:details/conditions/installedModule/optionalDevice'
    DETAILS_CONDITIONS_INSTALLEDMODULE_GUNS_NOT = b'#quests:details/conditions/installedModule/guns/not'
    DETAILS_CONDITIONS_INSTALLEDMODULE_ENGINES_NOT = b'#quests:details/conditions/installedModule/engines/not'
    DETAILS_CONDITIONS_INSTALLEDMODULE_CHASSIS_NOT = b'#quests:details/conditions/installedModule/chassis/not'
    DETAILS_CONDITIONS_INSTALLEDMODULE_TURRETS_NOT = b'#quests:details/conditions/installedModule/turrets/not'
    DETAILS_CONDITIONS_INSTALLEDMODULE_RADIOS_NOT = b'#quests:details/conditions/installedModule/radios/not'
    DETAILS_CONDITIONS_INSTALLEDMODULE_OPTIONALDEVICE_NOT = b'#quests:details/conditions/installedModule/optionalDevice/not'
    DETAILS_CONDITIONS_MULTISTUNEVENT = b'#quests:details/conditions/multiStunEvent'
    DETAILS_CONDITIONS_MULTISTUNEVENT_NOT = b'#quests:details/conditions/multiStunEvent/not'
    DETAILS_CONDITIONS_VEHICLESTUN = b'#quests:details/conditions/vehicleStun'
    DETAILS_CONDITIONS_VEHICLESTUN_NOT = b'#quests:details/conditions/vehicleStun/not'
    DETAILS_CONDITIONS_VEHICLESTUN_CUMULATIVE = b'#quests:details/conditions/vehicleStun/cumulative'
    DETAILS_CONDITIONS_VEHICLESTUN_CUMULATIVE_ALL = b'#quests:details/conditions/vehicleStun/cumulative/all'
    DETAILS_CONDITIONS_VEHICLESTUN_ALL = b'#quests:details/conditions/vehicleStun/all'
    DETAILS_CONDITIONS_VEHICLESTUN_ALL_NOT = b'#quests:details/conditions/vehicleStun/all/not'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION = b'#quests:details/conditions/vehicleStun/nation'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION_NOT = b'#quests:details/conditions/vehicleStun/nation/not'
    DETAILS_CONDITIONS_VEHICLESTUN_TYPE = b'#quests:details/conditions/vehicleStun/type'
    DETAILS_CONDITIONS_VEHICLESTUN_TYPE_NOT = b'#quests:details/conditions/vehicleStun/type/not'
    DETAILS_CONDITIONS_VEHICLESTUN_LEVEL = b'#quests:details/conditions/vehicleStun/level'
    DETAILS_CONDITIONS_VEHICLESTUN_LEVEL_NOT = b'#quests:details/conditions/vehicleStun/level/not'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION_TYPE = b'#quests:details/conditions/vehicleStun/nation_type'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION_TYPE_NOT = b'#quests:details/conditions/vehicleStun/nation_type/not'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION_LEVEL = b'#quests:details/conditions/vehicleStun/nation_level'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION_LEVEL_NOT = b'#quests:details/conditions/vehicleStun/nation_level/not'
    DETAILS_CONDITIONS_VEHICLESTUN_TYPE_LEVEL = b'#quests:details/conditions/vehicleStun/type_level'
    DETAILS_CONDITIONS_VEHICLESTUN_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleStun/type_level/not'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION_TYPE_LEVEL = b'#quests:details/conditions/vehicleStun/nation_type_level'
    DETAILS_CONDITIONS_VEHICLESTUN_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleStun/nation_type_level/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT = b'#quests:details/conditions/vehicleStunEventCount'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NOT = b'#quests:details/conditions/vehicleStunEventCount/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_CUMULATIVE = b'#quests:details/conditions/vehicleStunEventCount/cumulative'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_CUMULATIVE_ALL = b'#quests:details/conditions/vehicleStunEventCount/cumulative/all'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_ALL = b'#quests:details/conditions/vehicleStunEventCount/all'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_ALL_NOT = b'#quests:details/conditions/vehicleStunEventCount/all/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION = b'#quests:details/conditions/vehicleStunEventCount/nation'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION_NOT = b'#quests:details/conditions/vehicleStunEventCount/nation/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_TYPE = b'#quests:details/conditions/vehicleStunEventCount/type'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_TYPE_NOT = b'#quests:details/conditions/vehicleStunEventCount/type/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_LEVEL = b'#quests:details/conditions/vehicleStunEventCount/level'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_LEVEL_NOT = b'#quests:details/conditions/vehicleStunEventCount/level/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION_TYPE = b'#quests:details/conditions/vehicleStunEventCount/nation_type'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION_TYPE_NOT = b'#quests:details/conditions/vehicleStunEventCount/nation_type/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION_LEVEL = b'#quests:details/conditions/vehicleStunEventCount/nation_level'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION_LEVEL_NOT = b'#quests:details/conditions/vehicleStunEventCount/nation_level/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_TYPE_LEVEL = b'#quests:details/conditions/vehicleStunEventCount/type_level'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleStunEventCount/type_level/not'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION_TYPE_LEVEL = b'#quests:details/conditions/vehicleStunEventCount/nation_type_level'
    DETAILS_CONDITIONS_VEHICLESTUNEVENTCOUNT_NATION_TYPE_LEVEL_NOT = b'#quests:details/conditions/vehicleStunEventCount/nation_type_level/not'
    DETAILS_CONDITIONS_GROUPBY_NATION = b'#quests:details/conditions/groupBy/nation'
    DETAILS_CONDITIONS_GROUPBY_CLASS = b'#quests:details/conditions/groupBy/class'
    DETAILS_CONDITIONS_GROUPBY_LEVEL = b'#quests:details/conditions/groupBy/level'
    DETAILS_CONDITIONS_GROUPBY_VEHICLE = b'#quests:details/conditions/groupBy/vehicle'
    DETAILS_CONDITIONS_GROUPBY_LEVELLABEL = b'#quests:details/conditions/groupBy/levelLabel'
    DETAILS_CONDITIONS_POSTBATTLE_SEPARATOR = b'#quests:details/conditions/postBattle/separator'
    DETAILS_CONDITIONS_POSTBATTLE_DAILYRESET_TIMEFMT = b'#quests:details/conditions/postBattle/dailyReset/timeFmt'
    DETAILS_CONDITIONS_POSTBATTLE_DELTADAILYRESET_TIMEFMT = b'#quests:details/conditions/postBattle/deltaDailyReset/timeFmt'
    DETAILS_CONDITIONS_POSTBATTLE_WEEKLYRESET_TIMEFMT = b'#quests:details/conditions/postBattle/weeklyReset/timeFmt'
    DETAILS_CONDITIONS_POSTBATTLE_DAILYRESET = b'#quests:details/conditions/postBattle/dailyReset'
    DETAILS_CONDITIONS_CUMULATIVE_HEALTH = b'#quests:details/conditions/cumulative/health'
    DETAILS_CONDITIONS_CUMULATIVE_XP = b'#quests:details/conditions/cumulative/xp'
    DETAILS_CONDITIONS_CUMULATIVE_DIRECTHITS = b'#quests:details/conditions/cumulative/directHits'
    DETAILS_CONDITIONS_CUMULATIVE_DIRECTENEMYHITS = b'#quests:details/conditions/cumulative/directEnemyHits'
    DETAILS_CONDITIONS_CUMULATIVE_ENEMYHITS = b'#quests:details/conditions/cumulative/enemyHits'
    DETAILS_CONDITIONS_CUMULATIVE_INDIRECTENEMYHITS = b'#quests:details/conditions/cumulative/indirectEnemyHits'
    DETAILS_CONDITIONS_CUMULATIVE_DIRECTTEAMHITS = b'#quests:details/conditions/cumulative/directTeamHits'
    DETAILS_CONDITIONS_CUMULATIVE_EXPLOSIONHITS = b'#quests:details/conditions/cumulative/explosionHits'
    DETAILS_CONDITIONS_CUMULATIVE_EXPLOSIONENEMYHITS = b'#quests:details/conditions/cumulative/explosionEnemyHits'
    DETAILS_CONDITIONS_CUMULATIVE_PIERCINGS = b'#quests:details/conditions/cumulative/piercings'
    DETAILS_CONDITIONS_CUMULATIVE_PIERCINGENEMYHITS = b'#quests:details/conditions/cumulative/piercingEnemyHits'
    DETAILS_CONDITIONS_CUMULATIVE_SHOTS = b'#quests:details/conditions/cumulative/shots'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEDEALT = b'#quests:details/conditions/cumulative/damageDealt'
    DETAILS_CONDITIONS_CUMULATIVE_MAXDAMAGE = b'#quests:details/conditions/cumulative/maxDamage'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEASSISTED = b'#quests:details/conditions/cumulative/damageAssisted'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGERECEIVED = b'#quests:details/conditions/cumulative/damageReceived'
    DETAILS_CONDITIONS_CUMULATIVE_DIRECTHITSRECEIVED = b'#quests:details/conditions/cumulative/directHitsReceived'
    DETAILS_CONDITIONS_CUMULATIVE_NODAMAGEDIRECTHITSRECEIVED = b'#quests:details/conditions/cumulative/noDamageDirectHitsReceived'
    DETAILS_CONDITIONS_CUMULATIVE_EXPLOSIONHITSRECEIVED = b'#quests:details/conditions/cumulative/explosionHitsReceived'
    DETAILS_CONDITIONS_CUMULATIVE_PIERCINGSRECEIVED = b'#quests:details/conditions/cumulative/piercingsReceived'
    DETAILS_CONDITIONS_CUMULATIVE_SPOTTED = b'#quests:details/conditions/cumulative/spotted'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGED = b'#quests:details/conditions/cumulative/damaged'
    DETAILS_CONDITIONS_CUMULATIVE_KILLS = b'#quests:details/conditions/cumulative/kills'
    DETAILS_CONDITIONS_CUMULATIVE_TDAMAGEDEALT = b'#quests:details/conditions/cumulative/tdamageDealt'
    DETAILS_CONDITIONS_CUMULATIVE_TKILLS = b'#quests:details/conditions/cumulative/tkills'
    DETAILS_CONDITIONS_CUMULATIVE_CAPTUREPOINTS = b'#quests:details/conditions/cumulative/capturePoints'
    DETAILS_CONDITIONS_CUMULATIVE_DROPPEDCAPTUREPOINTS = b'#quests:details/conditions/cumulative/droppedCapturePoints'
    DETAILS_CONDITIONS_CUMULATIVE_ACHIEVEMENTS = b'#quests:details/conditions/cumulative/achievements'
    DETAILS_CONDITIONS_CUMULATIVE_POTENTIALDAMAGERECEIVED = b'#quests:details/conditions/cumulative/potentialDamageReceived'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEBLOCKEDBYARMOR = b'#quests:details/conditions/cumulative/damageBlockedByArmor'
    DETAILS_CONDITIONS_CUMULATIVE_FREEXP = b'#quests:details/conditions/cumulative/freeXP'
    DETAILS_CONDITIONS_CUMULATIVE_SUBTOTALXP = b'#quests:details/conditions/cumulative/subtotalXP'
    DETAILS_CONDITIONS_CUMULATIVE_POTENTIALDAMAGEDEALT = b'#quests:details/conditions/cumulative/potentialDamageDealt'
    DETAILS_CONDITIONS_CUMULATIVE_SOLOHITSASSISTED = b'#quests:details/conditions/cumulative/soloHitsAssisted'
    DETAILS_CONDITIONS_CUMULATIVE_ORIGINALXP = b'#quests:details/conditions/cumulative/originalXP'
    DETAILS_CONDITIONS_CUMULATIVE_ORIGINALCREDITS = b'#quests:details/conditions/cumulative/originalCredits'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEASSISTEDTRACK = b'#quests:details/conditions/cumulative/damageAssistedTrack'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEASSISTEDRADIO = b'#quests:details/conditions/cumulative/damageAssistedRadio'
    DETAILS_CONDITIONS_CUMULATIVE_MARKOFMASTERY = b'#quests:details/conditions/cumulative/markOfMastery'
    DETAILS_CONDITIONS_CUMULATIVE_MARKOFMASTERY0 = b'#quests:details/conditions/cumulative/markOfMastery0'
    DETAILS_CONDITIONS_CUMULATIVE_MARKOFMASTERY0_NOT = b'#quests:details/conditions/cumulative/markOfMastery0/not'
    DETAILS_CONDITIONS_CUMULATIVE_MARKOFMASTERY1 = b'#quests:details/conditions/cumulative/markOfMastery1'
    DETAILS_CONDITIONS_CUMULATIVE_MARKOFMASTERY2 = b'#quests:details/conditions/cumulative/markOfMastery2'
    DETAILS_CONDITIONS_CUMULATIVE_MARKOFMASTERY3 = b'#quests:details/conditions/cumulative/markOfMastery3'
    DETAILS_CONDITIONS_CUMULATIVE_MARKOFMASTERY4 = b'#quests:details/conditions/cumulative/markOfMastery4'
    DETAILS_CONDITIONS_CUMULATIVE_INNERMODULECRITCOUNT = b'#quests:details/conditions/cumulative/innerModuleCritCount'
    DETAILS_CONDITIONS_CUMULATIVE_CRITSCOUNT = b'#quests:details/conditions/cumulative/critsCount'
    DETAILS_CONDITIONS_CUMULATIVE_STUNNUM = b'#quests:details/conditions/cumulative/stunNum'
    DETAILS_CONDITIONS_CUMULATIVE_SNIPERDAMAGEDEALT = b'#quests:details/conditions/cumulative/sniperDamageDealt'
    DETAILS_CONDITIONS_CUMULATIVE_MILEAGE = b'#quests:details/conditions/cumulative/mileage'
    DETAILS_CONDITIONS_CUMULATIVE_LIFETIME = b'#quests:details/conditions/cumulative/lifeTime'
    DETAILS_CONDITIONS_CUMULATIVE_INNERMODULEDESTRCOUNT = b'#quests:details/conditions/cumulative/innerModuleDestrCount'
    DETAILS_CONDITIONS_CUMULATIVE_KILLSASSISTEDRADIO = b'#quests:details/conditions/cumulative/killsAssistedRadio'
    DETAILS_CONDITIONS_CUMULATIVE_KILLSASSISTEDTRACK = b'#quests:details/conditions/cumulative/killsAssistedTrack'
    DETAILS_CONDITIONS_CUMULATIVE_KILLSASSISTEDSTUN = b'#quests:details/conditions/cumulative/killsAssistedStun'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEDVEHICLECNTASSISTEDRADIO = b'#quests:details/conditions/cumulative/damagedVehicleCntAssistedRadio'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEDVEHICLECNTASSISTEDTRACK = b'#quests:details/conditions/cumulative/damagedVehicleCntAssistedTrack'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEDVEHICLECNTASSISTEDSTUN = b'#quests:details/conditions/cumulative/damagedVehicleCntAssistedStun'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEASSISTEDRADIOWHILEINVISIBLE = b'#quests:details/conditions/cumulative/damageAssistedRadioWhileInvisible'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEASSISTEDTRACKWHILEINVISIBLE = b'#quests:details/conditions/cumulative/damageAssistedTrackWhileInvisible'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEASSISTEDSTUNWHILEINVISIBLE = b'#quests:details/conditions/cumulative/damageAssistedStunWhileInvisible'
    DETAILS_CONDITIONS_CUMULATIVE_FORTRESOURCE = b'#quests:details/conditions/cumulative/fortResource'
    DETAILS_CONDITIONS_CUMULATIVE_PERCENTFROMTOTALTEAMDAMAGE = b'#quests:details/conditions/cumulative/percentFromTotalTeamDamage'
    DETAILS_CONDITIONS_CUMULATIVE_KILLEDANDDAMAGEDBYALLSQUADMATES = b'#quests:details/conditions/cumulative/killedAndDamagedByAllSquadmates'
    DETAILS_CONDITIONS_CUMULATIVE_MARKSONGUN = b'#quests:details/conditions/cumulative/marksOnGun'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEDWHILEENEMYMOVING = b'#quests:details/conditions/cumulative/damagedWhileEnemyMoving'
    DETAILS_CONDITIONS_CUMULATIVE_INBATTLEMAXPIERCINGSERIES = b'#quests:details/conditions/cumulative/inBattleMaxPiercingSeries'
    DETAILS_CONDITIONS_CUMULATIVE_INBATTLEMAXSNIPERSERIES = b'#quests:details/conditions/cumulative/inBattleMaxSniperSeries'
    DETAILS_CONDITIONS_CUMULATIVE_SPOTTEDANDDAMAGEDSPG = b'#quests:details/conditions/cumulative/spottedAndDamagedSPG'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEASSISTEDSTUN = b'#quests:details/conditions/cumulative/damageAssistedStun'
    DETAILS_CONDITIONS_CUMULATIVE_STUNDURATION = b'#quests:details/conditions/cumulative/stunDuration'
    DETAILS_CONDITIONS_CUMULATIVE_STUNNED = b'#quests:details/conditions/cumulative/stunned'
    DETAILS_CONDITIONS_CUMULATIVE_SPOTTEDBEFOREWEBECAMESPOTTED = b'#quests:details/conditions/cumulative/spottedBeforeWeBecameSpotted'
    DETAILS_CONDITIONS_CUMULATIVE_ISANYOURCRITTEDINNERMODULES = b'#quests:details/conditions/cumulative/isAnyOurCrittedInnerModules'
    DETAILS_CONDITIONS_CUMULATIVE_ISENEMYBASECAPTURED = b'#quests:details/conditions/cumulative/isEnemyBaseCaptured'
    DETAILS_CONDITIONS_CUMULATIVE_AGGREGATED = b'#quests:details/conditions/cumulative/aggregated'
    DETAILS_CONDITIONS_CUMULATIVE_RANKCHANGE = b'#quests:details/conditions/cumulative/rankChange'
    DETAILS_CONDITIONS_CUMULATIVE_XP_OTHER = b'#quests:details/conditions/cumulative/xp/other'
    DETAILS_DOSSIER_SNIPERSERIES = b'#quests:details/dossier/sniperSeries'
    DETAILS_DOSSIER_MAXSNIPERSERIES = b'#quests:details/dossier/maxSniperSeries'
    DETAILS_DOSSIER_INVINCIBLESERIES = b'#quests:details/dossier/invincibleSeries'
    DETAILS_DOSSIER_MAXINVINCIBLESERIES = b'#quests:details/dossier/maxInvincibleSeries'
    DETAILS_DOSSIER_DIEHARDSERIES = b'#quests:details/dossier/diehardSeries'
    DETAILS_DOSSIER_MAXDIEHARDSERIES = b'#quests:details/dossier/maxDiehardSeries'
    DETAILS_DOSSIER_KILLINGSERIES = b'#quests:details/dossier/killingSeries'
    DETAILS_DOSSIER_MAXKILLINGSERIES = b'#quests:details/dossier/maxKillingSeries'
    DETAILS_DOSSIER_PIERCINGSERIES = b'#quests:details/dossier/piercingSeries'
    DETAILS_DOSSIER_MAXPIERCINGSERIES = b'#quests:details/dossier/maxPiercingSeries'
    DETAILS_DOSSIER_MAXXP = b'#quests:details/dossier/maxXP'
    DETAILS_DOSSIER_MAXXPVEHICLE = b'#quests:details/dossier/maxXPVehicle'
    DETAILS_DOSSIER_MAXFRAGS = b'#quests:details/dossier/maxFrags'
    DETAILS_DOSSIER_MAXFRAGSVEHICLE = b'#quests:details/dossier/maxFragsVehicle'
    DETAILS_DOSSIER_MAXDAMAGE = b'#quests:details/dossier/maxDamage'
    DETAILS_DOSSIER_MAXDAMAGEVEHICLE = b'#quests:details/dossier/maxDamageVehicle'
    DETAILS_DOSSIER_MARKOFMASTERY = b'#quests:details/dossier/markOfMastery'
    DETAILS_DOSSIER_WARRIOR = b'#quests:details/dossier/warrior'
    DETAILS_DOSSIER_INVADER = b'#quests:details/dossier/invader'
    DETAILS_DOSSIER_SNIPER = b'#quests:details/dossier/sniper'
    DETAILS_DOSSIER_SNIPER2 = b'#quests:details/dossier/sniper2'
    DETAILS_DOSSIER_MAINGUN = b'#quests:details/dossier/mainGun'
    DETAILS_DOSSIER_ARMOREDFIST = b'#quests:details/dossier/armoredFist'
    DETAILS_DOSSIER_GENIUSFORWARMEDAL = b'#quests:details/dossier/geniusForWarMedal'
    DETAILS_DOSSIER_WOLFAMONGSHEEPMEDAL = b'#quests:details/dossier/wolfAmongSheepMedal'
    DETAILS_DOSSIER_TACTICALBREAKTHROUGH = b'#quests:details/dossier/tacticalBreakthrough'
    DETAILS_DOSSIER_KINGOFTHEHILL = b'#quests:details/dossier/kingOfTheHill'
    DETAILS_DOSSIER_DEFENDER = b'#quests:details/dossier/defender'
    DETAILS_DOSSIER_STEELWALL = b'#quests:details/dossier/steelwall'
    DETAILS_DOSSIER_SUPPORTER = b'#quests:details/dossier/supporter'
    DETAILS_DOSSIER_SCOUT = b'#quests:details/dossier/scout'
    DETAILS_DOSSIER_MEDALKAY = b'#quests:details/dossier/medalKay'
    DETAILS_DOSSIER_MEDALSAMOKHIN = b'#quests:details/dossier/medalSamokhin'
    DETAILS_DOSSIER_MEDALGUDZ = b'#quests:details/dossier/medalGudz'
    DETAILS_DOSSIER_MEDALPOPPEL = b'#quests:details/dossier/medalPoppel'
    DETAILS_DOSSIER_MEDALABRAMS = b'#quests:details/dossier/medalAbrams'
    DETAILS_DOSSIER_MEDALLECLERC = b'#quests:details/dossier/medalLeClerc'
    DETAILS_DOSSIER_MEDALLAVRINENKO = b'#quests:details/dossier/medalLavrinenko'
    DETAILS_DOSSIER_MEDALEKINS = b'#quests:details/dossier/medalEkins'
    DETAILS_DOSSIER_MEDALUSHAKOV = b'#quests:details/dossier/medalUshakov'
    DETAILS_DOSSIER_MEDALORLIK = b'#quests:details/dossier/medalOrlik'
    DETAILS_DOSSIER_MEDALOSKIN = b'#quests:details/dossier/medalOskin'
    DETAILS_DOSSIER_MEDALKRYSOV = b'#quests:details/dossier/medalKrysov'
    DETAILS_DOSSIER_MEDALBURDA = b'#quests:details/dossier/medalBurda'
    DETAILS_DOSSIER_MEDALBILLOTTE = b'#quests:details/dossier/medalBillotte'
    DETAILS_DOSSIER_MEDALKOLOBANOV = b'#quests:details/dossier/medalKolobanov'
    DETAILS_DOSSIER_MEDALFADIN = b'#quests:details/dossier/medalFadin'
    DETAILS_DOSSIER_TITLESNIPER = b'#quests:details/dossier/titleSniper'
    DETAILS_DOSSIER_INVINCIBLE = b'#quests:details/dossier/invincible'
    DETAILS_DOSSIER_DIEHARD = b'#quests:details/dossier/diehard'
    DETAILS_DOSSIER_RAIDER = b'#quests:details/dossier/raider'
    DETAILS_DOSSIER_HANDOFDEATH = b'#quests:details/dossier/handOfDeath'
    DETAILS_DOSSIER_ARMORPIERCER = b'#quests:details/dossier/armorPiercer'
    DETAILS_DOSSIER_KAMIKAZE = b'#quests:details/dossier/kamikaze'
    DETAILS_DOSSIER_BEASTHUNTER = b'#quests:details/dossier/beasthunter'
    DETAILS_DOSSIER_MOUSEBANE = b'#quests:details/dossier/mousebane'
    DETAILS_DOSSIER_EVILEYE = b'#quests:details/dossier/evileye'
    DETAILS_DOSSIER_BATTLECITIZEN = b'#quests:details/dossier/battleCitizen'
    DETAILS_DOSSIER_MEDALRADLEYWALTERS = b'#quests:details/dossier/medalRadleyWalters'
    DETAILS_DOSSIER_MEDALLAFAYETTEPOOL = b'#quests:details/dossier/medalLafayettePool'
    DETAILS_DOSSIER_MEDALFOKIN = b'#quests:details/dossier/medalFokin'
    DETAILS_DOSSIER_MEDALLYUBUSHKIN = b'#quests:details/dossier/medalLyubushkin'
    DETAILS_DOSSIER_MEDALSLYUNYAYEV = b'#quests:details/dossier/medalSlyunyayev'
    DETAILS_DOSSIER_MEDALDUMITRU = b'#quests:details/dossier/medalDumitru'
    DETAILS_DOSSIER_MEDALKHAZOV = b'#quests:details/dossier/medalKhazov'
    DETAILS_DOSSIER_MEDALNIKOLAS = b'#quests:details/dossier/medalNikolas'
    DETAILS_DOSSIER_FRAGSSINAI = b'#quests:details/dossier/fragsSinai'
    DETAILS_DOSSIER_SINAI = b'#quests:details/dossier/sinai'
    DETAILS_DOSSIER_HEROESOFRASSENAY = b'#quests:details/dossier/heroesOfRassenay'
    DETAILS_DOSSIER_MEDALBROTHERSINARMS = b'#quests:details/dossier/medalBrothersInArms'
    DETAILS_DOSSIER_MEDALCRUCIALCONTRIBUTION = b'#quests:details/dossier/medalCrucialContribution'
    DETAILS_DOSSIER_MEDALDELANGLADE = b'#quests:details/dossier/medalDeLanglade'
    DETAILS_DOSSIER_MEDALTRUBIN = b'#quests:details/dossier/medalTrubin'
    DETAILS_DOSSIER_MEDALFOMIN = b'#quests:details/dossier/medalFomin'
    DETAILS_DOSSIER_MEDALKROCKENBERGER = b'#quests:details/dossier/medalKrockenberger'
    DETAILS_DOSSIER_MEDALGAVRYUSHOV = b'#quests:details/dossier/medalGavryushov'
    DETAILS_DOSSIER_BOMBARDIER = b'#quests:details/dossier/bombardier'
    DETAILS_DOSSIER_HUNTSMAN = b'#quests:details/dossier/huntsman'
    DETAILS_DOSSIER_STURDY = b'#quests:details/dossier/sturdy'
    DETAILS_DOSSIER_IRONMAN = b'#quests:details/dossier/ironMan'
    DETAILS_DOSSIER_FRAGSPATTON = b'#quests:details/dossier/fragsPatton'
    DETAILS_DOSSIER_PATTONVALLEY = b'#quests:details/dossier/pattonValley'
    DETAILS_DOSSIER_RANDOM_XP = b'#quests:details/dossier/random/xp'
    DETAILS_DOSSIER_RANDOM_MAXXP = b'#quests:details/dossier/random/maxXP'
    DETAILS_DOSSIER_RANDOM_WINS = b'#quests:details/dossier/random/wins'
    DETAILS_DOSSIER_RANDOM_LOSSES = b'#quests:details/dossier/random/losses'
    DETAILS_DOSSIER_RANDOM_SURVIVEDBATTLES = b'#quests:details/dossier/random/survivedBattles'
    DETAILS_DOSSIER_RANDOM_LASTBATTLETIME = b'#quests:details/dossier/random/lastBattleTime'
    DETAILS_DOSSIER_RANDOM_WINANDSURVIVED = b'#quests:details/dossier/random/winAndSurvived'
    DETAILS_DOSSIER_RANDOM_BATTLEHEROES = b'#quests:details/dossier/random/battleHeroes'
    DETAILS_DOSSIER_RANDOM_FRAGS = b'#quests:details/dossier/random/frags'
    DETAILS_DOSSIER_RANDOM_MAXFRAGS = b'#quests:details/dossier/random/maxFrags'
    DETAILS_DOSSIER_RANDOM_MAXDAMAGE = b'#quests:details/dossier/random/maxDamage'
    DETAILS_DOSSIER_RANDOM_FRAGS8P = b'#quests:details/dossier/random/frags8p'
    DETAILS_DOSSIER_RANDOM_FRAGSBEAST = b'#quests:details/dossier/random/fragsBeast'
    DETAILS_DOSSIER_RANDOM_DIRECTHITS = b'#quests:details/dossier/random/directHits'
    DETAILS_DOSSIER_RANDOM_SPOTTED = b'#quests:details/dossier/random/spotted'
    DETAILS_DOSSIER_RANDOM_DAMAGEDEALT = b'#quests:details/dossier/random/damageDealt'
    DETAILS_DOSSIER_RANDOM_DAMAGERECEIVED = b'#quests:details/dossier/random/damageReceived'
    DETAILS_DOSSIER_RANDOM_DIRECTHITSRECEIVED = b'#quests:details/dossier/random/directHitsReceived'
    DETAILS_DOSSIER_RANDOM_CAPTUREPOINTS = b'#quests:details/dossier/random/capturePoints'
    DETAILS_DOSSIER_RANDOM_DROPPEDCAPTUREPOINTS = b'#quests:details/dossier/random/droppedCapturePoints'
    DETAILS_DOSSIER_RANDOM_PIERCINGS = b'#quests:details/dossier/random/piercings'
    DETAILS_DOSSIER_RANDOM_NODAMAGEDIRECTHITSRECEIVED = b'#quests:details/dossier/random/noDamageDirectHitsReceived'
    DETAILS_DOSSIER_RANDOM_PIERCINGSRECEIVED = b'#quests:details/dossier/random/piercingsReceived'
    DETAILS_DOSSIER_RANDOM_POTENTIALDAMAGERECEIVED = b'#quests:details/dossier/random/potentialDamageReceived'
    DETAILS_DOSSIER_RANDOM_DAMAGEBLOCKEDBYARMOR = b'#quests:details/dossier/random/damageBlockedByArmor'
    DETAILS_DOSSIER_RANDOM_ORIGINALXP = b'#quests:details/dossier/random/originalXP'
    DETAILS_DOSSIER_RANDOM_DAMAGEASSISTEDTRACK = b'#quests:details/dossier/random/damageAssistedTrack'
    DETAILS_DOSSIER_RANDOM_DAMAGEASSISTEDRADIO = b'#quests:details/dossier/random/damageAssistedRadio'
    DETAILS_DOSSIER_RANDOM_SHOTS = b'#quests:details/dossier/random/shots'
    DETAILS_DOSSIER_RANDOM_EXPLOSIONHITSRECEIVED = b'#quests:details/dossier/random/explosionHitsReceived'
    DETAILS_DOSSIER_RANDOM_BATTLESCOUNT = b'#quests:details/dossier/random/battlesCount'
    DETAILS_DOSSIER_CLAN_XP = b'#quests:details/dossier/clan/xp'
    DETAILS_DOSSIER_CLAN_BATTLESCOUNT = b'#quests:details/dossier/clan/battlesCount'
    DETAILS_DOSSIER_CLAN_WINS = b'#quests:details/dossier/clan/wins'
    DETAILS_DOSSIER_CLAN_LOSSES = b'#quests:details/dossier/clan/losses'
    DETAILS_DOSSIER_CLAN_SURVIVEDBATTLES = b'#quests:details/dossier/clan/survivedBattles'
    DETAILS_DOSSIER_CLAN_FRAGS = b'#quests:details/dossier/clan/frags'
    DETAILS_DOSSIER_CLAN_DIRECTHITS = b'#quests:details/dossier/clan/directHits'
    DETAILS_DOSSIER_CLAN_SPOTTED = b'#quests:details/dossier/clan/spotted'
    DETAILS_DOSSIER_CLAN_DAMAGEDEALT = b'#quests:details/dossier/clan/damageDealt'
    DETAILS_DOSSIER_CLAN_MAXDAMAGE = b'#quests:details/dossier/clan/maxDamage'
    DETAILS_DOSSIER_CLAN_DAMAGERECEIVED = b'#quests:details/dossier/clan/damageReceived'
    DETAILS_DOSSIER_CLAN_CAPTUREPOINTS = b'#quests:details/dossier/clan/capturePoints'
    DETAILS_DOSSIER_CLAN_DROPPEDCAPTUREPOINTS = b'#quests:details/dossier/clan/droppedCapturePoints'
    DETAILS_DOSSIER_CLAN_PIERCINGS = b'#quests:details/dossier/clan/piercings'
    DETAILS_DOSSIER_CLAN_NODAMAGEDIRECTHITSRECEIVED = b'#quests:details/dossier/clan/noDamageDirectHitsReceived'
    DETAILS_DOSSIER_CLAN_PIERCINGSRECEIVED = b'#quests:details/dossier/clan/piercingsReceived'
    DETAILS_DOSSIER_CLAN_POTENTIALDAMAGERECEIVED = b'#quests:details/dossier/clan/potentialDamageReceived'
    DETAILS_DOSSIER_CLAN_DAMAGEBLOCKEDBYARMOR = b'#quests:details/dossier/clan/damageBlockedByArmor'
    DETAILS_DOSSIER_CLAN_ORIGINALXP = b'#quests:details/dossier/clan/originalXP'
    DETAILS_DOSSIER_CLAN_DAMAGEASSISTEDTRACK = b'#quests:details/dossier/clan/damageAssistedTrack'
    DETAILS_DOSSIER_CLAN_DAMAGEASSISTEDRADIO = b'#quests:details/dossier/clan/damageAssistedRadio'
    DETAILS_DOSSIER_HISTORICAL_XP = b'#quests:details/dossier/historical/xp'
    DETAILS_DOSSIER_HISTORICAL_BATTLESCOUNT = b'#quests:details/dossier/historical/battlesCount'
    DETAILS_DOSSIER_HISTORICAL_WINS = b'#quests:details/dossier/historical/wins'
    DETAILS_DOSSIER_HISTORICAL_LOSSES = b'#quests:details/dossier/historical/losses'
    DETAILS_DOSSIER_HISTORICAL_SURVIVEDBATTLES = b'#quests:details/dossier/historical/survivedBattles'
    DETAILS_DOSSIER_HISTORICAL_FRAGS = b'#quests:details/dossier/historical/frags'
    DETAILS_DOSSIER_HISTORICAL_DIRECTHITS = b'#quests:details/dossier/historical/directHits'
    DETAILS_DOSSIER_HISTORICAL_SPOTTED = b'#quests:details/dossier/historical/spotted'
    DETAILS_DOSSIER_HISTORICAL_DAMAGEDEALT = b'#quests:details/dossier/historical/damageDealt'
    DETAILS_DOSSIER_HISTORICAL_MAXDAMAGE = b'#quests:details/dossier/historical/maxDamage'
    DETAILS_DOSSIER_HISTORICAL_DAMAGERECEIVED = b'#quests:details/dossier/historical/damageReceived'
    DETAILS_DOSSIER_HISTORICAL_CAPTUREPOINTS = b'#quests:details/dossier/historical/capturePoints'
    DETAILS_DOSSIER_HISTORICAL_DROPPEDCAPTUREPOINTS = b'#quests:details/dossier/historical/droppedCapturePoints'
    DETAILS_DOSSIER_HISTORICAL_PIERCINGS = b'#quests:details/dossier/historical/piercings'
    DETAILS_DOSSIER_HISTORICAL_NODAMAGEDIRECTHITSRECEIVED = b'#quests:details/dossier/historical/noDamageDirectHitsReceived'
    DETAILS_DOSSIER_HISTORICAL_PIERCINGSRECEIVED = b'#quests:details/dossier/historical/piercingsReceived'
    DETAILS_DOSSIER_HISTORICAL_POTENTIALDAMAGERECEIVED = b'#quests:details/dossier/historical/potentialDamageReceived'
    DETAILS_DOSSIER_HISTORICAL_DAMAGEBLOCKEDBYARMOR = b'#quests:details/dossier/historical/damageBlockedByArmor'
    DETAILS_DOSSIER_HISTORICAL_ORIGINALXP = b'#quests:details/dossier/historical/originalXP'
    DETAILS_DOSSIER_HISTORICAL_DAMAGEASSISTEDTRACK = b'#quests:details/dossier/historical/damageAssistedTrack'
    DETAILS_DOSSIER_HISTORICAL_DAMAGEASSISTEDRADIO = b'#quests:details/dossier/historical/damageAssistedRadio'
    DETAILS_DOSSIER_TEAM_XP = b'#quests:details/dossier/team/xp'
    DETAILS_DOSSIER_TEAM_BATTLESCOUNT = b'#quests:details/dossier/team/battlesCount'
    DETAILS_DOSSIER_TEAM_WINS = b'#quests:details/dossier/team/wins'
    DETAILS_DOSSIER_TEAM_LOSSES = b'#quests:details/dossier/team/losses'
    DETAILS_DOSSIER_TEAM_SURVIVEDBATTLES = b'#quests:details/dossier/team/survivedBattles'
    DETAILS_DOSSIER_TEAM_FRAGS = b'#quests:details/dossier/team/frags'
    DETAILS_DOSSIER_TEAM_DIRECTHITS = b'#quests:details/dossier/team/directHits'
    DETAILS_DOSSIER_TEAM_SPOTTED = b'#quests:details/dossier/team/spotted'
    DETAILS_DOSSIER_TEAM_DAMAGEDEALT = b'#quests:details/dossier/team/damageDealt'
    DETAILS_DOSSIER_TEAM_MAXDAMAGE = b'#quests:details/dossier/team/maxDamage'
    DETAILS_DOSSIER_TEAM_DAMAGERECEIVED = b'#quests:details/dossier/team/damageReceived'
    DETAILS_DOSSIER_TEAM_CAPTUREPOINTS = b'#quests:details/dossier/team/capturePoints'
    DETAILS_DOSSIER_TEAM_DROPPEDCAPTUREPOINTS = b'#quests:details/dossier/team/droppedCapturePoints'
    DETAILS_DOSSIER_TEAM_PIERCINGS = b'#quests:details/dossier/team/piercings'
    DETAILS_DOSSIER_TEAM_NODAMAGEDIRECTHITSRECEIVED = b'#quests:details/dossier/team/noDamageDirectHitsReceived'
    DETAILS_DOSSIER_TEAM_PIERCINGSRECEIVED = b'#quests:details/dossier/team/piercingsReceived'
    DETAILS_DOSSIER_TEAM_POTENTIALDAMAGERECEIVED = b'#quests:details/dossier/team/potentialDamageReceived'
    DETAILS_DOSSIER_TEAM_DAMAGEBLOCKEDBYARMOR = b'#quests:details/dossier/team/damageBlockedByArmor'
    DETAILS_DOSSIER_TEAM_ORIGINALXP = b'#quests:details/dossier/team/originalXP'
    DETAILS_DOSSIER_TEAM_DAMAGEASSISTEDTRACK = b'#quests:details/dossier/team/damageAssistedTrack'
    DETAILS_DOSSIER_TEAM_DAMAGEASSISTEDRADIO = b'#quests:details/dossier/team/damageAssistedRadio'
    DETAILS_DOSSIER_LADDER_XP = b'#quests:details/dossier/ladder/xp'
    DETAILS_DOSSIER_LADDER_BATTLESCOUNT = b'#quests:details/dossier/ladder/battlesCount'
    DETAILS_DOSSIER_LADDER_WINS = b'#quests:details/dossier/ladder/wins'
    DETAILS_DOSSIER_LADDER_LOSSES = b'#quests:details/dossier/ladder/losses'
    DETAILS_DOSSIER_LADDER_SURVIVEDBATTLES = b'#quests:details/dossier/ladder/survivedBattles'
    DETAILS_DOSSIER_LADDER_FRAGS = b'#quests:details/dossier/ladder/frags'
    DETAILS_DOSSIER_LADDER_DIRECTHITS = b'#quests:details/dossier/ladder/directHits'
    DETAILS_DOSSIER_LADDER_SPOTTED = b'#quests:details/dossier/ladder/spotted'
    DETAILS_DOSSIER_LADDER_DAMAGEDEALT = b'#quests:details/dossier/ladder/damageDealt'
    DETAILS_DOSSIER_LADDER_MAXDAMAGE = b'#quests:details/dossier/ladder/maxDamage'
    DETAILS_DOSSIER_LADDER_DAMAGERECEIVED = b'#quests:details/dossier/ladder/damageReceived'
    DETAILS_DOSSIER_LADDER_CAPTUREPOINTS = b'#quests:details/dossier/ladder/capturePoints'
    DETAILS_DOSSIER_LADDER_DROPPEDCAPTUREPOINTS = b'#quests:details/dossier/ladder/droppedCapturePoints'
    DETAILS_DOSSIER_LADDER_PIERCINGS = b'#quests:details/dossier/ladder/piercings'
    DETAILS_DOSSIER_LADDER_NODAMAGEDIRECTHITSRECEIVED = b'#quests:details/dossier/ladder/noDamageDirectHitsReceived'
    DETAILS_DOSSIER_LADDER_PIERCINGSRECEIVED = b'#quests:details/dossier/ladder/piercingsReceived'
    DETAILS_DOSSIER_LADDER_POTENTIALDAMAGERECEIVED = b'#quests:details/dossier/ladder/potentialDamageReceived'
    DETAILS_DOSSIER_LADDER_DAMAGEBLOCKEDBYARMOR = b'#quests:details/dossier/ladder/damageBlockedByArmor'
    DETAILS_DOSSIER_LADDER_ORIGINALXP = b'#quests:details/dossier/ladder/originalXP'
    DETAILS_DOSSIER_LADDER_DAMAGEASSISTEDTRACK = b'#quests:details/dossier/ladder/damageAssistedTrack'
    DETAILS_DOSSIER_LADDER_DAMAGEASSISTEDRADIO = b'#quests:details/dossier/ladder/damageAssistedRadio'
    DETAILS_DOSSIER_BATTLESCOUNT = b'#quests:details/dossier/battlesCount'
    DETAILS_DOSSIER_0_BATTLESCOUNT = b'#quests:details/dossier/0/battlesCount'
    DETAILS_DOSSIER_1_BATTLESCOUNT = b'#quests:details/dossier/1/battlesCount'
    DETAILS_DOSSIER_2_BATTLESCOUNT = b'#quests:details/dossier/2/battlesCount'
    DETAILS_DOSSIER_4_BATTLESCOUNT = b'#quests:details/dossier/4/battlesCount'
    DETAILS_DOSSIER_5_BATTLESCOUNT = b'#quests:details/dossier/5/battlesCount'
    DETAILS_DOSSIER_6_BATTLESCOUNT = b'#quests:details/dossier/6/battlesCount'
    DETAILS_DOSSIER_7_BATTLESCOUNT = b'#quests:details/dossier/7/battlesCount'
    DETAILS_DOSSIER_9_BATTLESCOUNT = b'#quests:details/dossier/9/battlesCount'
    DETAILS_DOSSIER_13_BATTLESCOUNT = b'#quests:details/dossier/13/battlesCount'
    DETAILS_DOSSIER_16_BATTLESCOUNT = b'#quests:details/dossier/16/battlesCount'
    DETAILS_DOSSIER_18_BATTLESCOUNT = b'#quests:details/dossier/18/battlesCount'
    DETAILS_DOSSIER_19_BATTLESCOUNT = b'#quests:details/dossier/19/battlesCount'
    DETAILS_DOSSIER_20_BATTLESCOUNT = b'#quests:details/dossier/20/battlesCount'
    DETAILS_DOSSIER_21_BATTLESCOUNT = b'#quests:details/dossier/21/battlesCount'
    DETAILS_DOSSIER_22_BATTLESCOUNT = b'#quests:details/dossier/22/battlesCount'
    DETAILS_DOSSIER_24_BATTLESCOUNT = b'#quests:details/dossier/24/battlesCount'
    DETAILS_DOSSIER_27_BATTLESCOUNT = b'#quests:details/dossier/27/battlesCount'
    DETAILS_DOSSIER_37_BATTLESCOUNT = b'#quests:details/dossier/37/battlesCount'
    DETAILS_DOSSIER_39_BATTLESCOUNT = b'#quests:details/dossier/39/battlesCount'
    DETAILS_DOSSIER_42_BATTLESCOUNT = b'#quests:details/dossier/42/battlesCount'
    DETAILS_DOSSIER_43_BATTLESCOUNT = b'#quests:details/dossier/43/battlesCount'
    DETAILS_DOSSIER_50_BATTLESCOUNT = b'#quests:details/dossier/50/battlesCount'
    DETAILS_MODIFIERS_TITLE_DISCOUNT = b'#quests:details/modifiers/title/discount'
    DETAILS_MODIFIERS_TITLE_SELLING = b'#quests:details/modifiers/title/selling'
    DETAILS_MODIFIERS_TITLE_AVAILABILITY = b'#quests:details/modifiers/title/availability'
    DETAILS_MODIFIERS_ECONOMICS_SLOTSPRICES = b'#quests:details/modifiers/economics/slotsPrices'
    DETAILS_MODIFIERS_ECONOMICS_BERTHSPRICES = b'#quests:details/modifiers/economics/berthsPrices'
    DETAILS_MODIFIERS_ECONOMICS_CREDITSTANKMANCOST = b'#quests:details/modifiers/economics/creditsTankmanCost'
    DETAILS_MODIFIERS_ECONOMICS_GOLDTANKMANCOST = b'#quests:details/modifiers/economics/goldTankmanCost'
    DETAILS_MODIFIERS_ECONOMICS_CREDITSDROPSKILLSCOST = b'#quests:details/modifiers/economics/creditsDropSkillsCost'
    DETAILS_MODIFIERS_ECONOMICS_GOLDDROPSKILLSCOST = b'#quests:details/modifiers/economics/goldDropSkillsCost'
    DETAILS_MODIFIERS_ECONOMICS_EXCHANGERATE = b'#quests:details/modifiers/economics/exchangeRate'
    DETAILS_MODIFIERS_ECONOMICS_EXCHANGERATEFORSHELLSANDEQS = b'#quests:details/modifiers/economics/exchangeRateForShellsAndEqs'
    DETAILS_MODIFIERS_ECONOMICS_PASSPORTCHANGECOST = b'#quests:details/modifiers/economics/passportChangeCost'
    DETAILS_MODIFIERS_ECONOMICS_FEMALEPASSPORTCHANGECOST = b'#quests:details/modifiers/economics/femalePassportChangeCost'
    DETAILS_MODIFIERS_ECONOMICS_CLANCREATIONCOST = b'#quests:details/modifiers/economics/clanCreationCost'
    DETAILS_MODIFIERS_ECONOMICS_FREEXPCONVERSIONDISCRECITY = b'#quests:details/modifiers/economics/freeXPConversionDiscrecity'
    DETAILS_MODIFIERS_ECONOMICS_FREEXPTOTMANXPRATE = b'#quests:details/modifiers/economics/freeXPToTManXPRate'
    DETAILS_MODIFIERS_ECONOMICS_AVAILABLE_FREEXPTOTMANXPRATE = b'#quests:details/modifiers/economics/available/freeXPToTManXPRate'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET1 = b'#quests:details/modifiers/economics/premiumPacket1'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET3 = b'#quests:details/modifiers/economics/premiumPacket3'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET7 = b'#quests:details/modifiers/economics/premiumPacket7'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET14 = b'#quests:details/modifiers/economics/premiumPacket14'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET30 = b'#quests:details/modifiers/economics/premiumPacket30'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET90 = b'#quests:details/modifiers/economics/premiumPacket90'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET180 = b'#quests:details/modifiers/economics/premiumPacket180'
    DETAILS_MODIFIERS_ECONOMICS_PREMIUMPACKET360 = b'#quests:details/modifiers/economics/premiumPacket360'
    DETAILS_MODIFIERS_EQUIPMENT_GOLD = b'#quests:details/modifiers/equipment/gold'
    DETAILS_MODIFIERS_EQUIPMENT_CREDITS = b'#quests:details/modifiers/equipment/credits'
    DETAILS_MODIFIERS_EQUIPMENT_CRYSTAL = b'#quests:details/modifiers/equipment/crystal'
    DETAILS_MODIFIERS_EQUIPMENT_EVENTCOIN = b'#quests:details/modifiers/equipment/eventCoin'
    DETAILS_MODIFIERS_EQUIPMENT_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/equipment/goldPriceMultiplier'
    DETAILS_MODIFIERS_EQUIPMENT_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/equipment/creditsPriceMultiplier'
    DETAILS_MODIFIERS_EQUIPMENT_CRYSTALPRICEMULTIPLIER = b'#quests:details/modifiers/equipment/crystalPriceMultiplier'
    DETAILS_MODIFIERS_OPTDEVICE = b'#quests:details/modifiers/optDevice'
    DETAILS_MODIFIERS_OPTDEVICE_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/optDevice/goldPriceMultiplier'
    DETAILS_MODIFIERS_OPTDEVICE_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/optDevice/creditsPriceMultiplier'
    DETAILS_MODIFIERS_SHELL_GOLD = b'#quests:details/modifiers/shell/gold'
    DETAILS_MODIFIERS_SHELL_CREDITS = b'#quests:details/modifiers/shell/credits'
    DETAILS_MODIFIERS_SHELL_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/shell/goldPriceMultiplier'
    DETAILS_MODIFIERS_SHELL_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/shell/creditsPriceMultiplier'
    DETAILS_MODIFIERS_SHELL_NATION_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/shell/nation/goldPriceMultiplier'
    DETAILS_MODIFIERS_SHELL_NATION_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/shell/nation/creditsPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE = b'#quests:details/modifiers/vehicle'
    DETAILS_MODIFIERS_RENTVEHICLE = b'#quests:details/modifiers/rentVehicle'
    DETAILS_MODIFIERS_VEHRENTPACKAGE = b'#quests:details/modifiers/vehRentPackage'
    DETAILS_MODIFIERS_VEHICLE_SELL = b'#quests:details/modifiers/vehicle/sell'
    DETAILS_MODIFIERS_VEHICLE_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/goldPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/creditsPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE_RENT_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/rent/goldPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE_RENT_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/rent/creditsPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE_NATION_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/nation/goldPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE_NATION_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/nation/creditsPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE_RENT_NATION_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/rent/nation/goldPriceMultiplier'
    DETAILS_MODIFIERS_VEHICLE_RENT_NATION_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/vehicle/rent/nation/creditsPriceMultiplier'
    DETAILS_MODIFIERS_BOOSTER = b'#quests:details/modifiers/booster'
    DETAILS_MODIFIERS_BOOSTERS_GOLDPRICEMULTIPLIER = b'#quests:details/modifiers/boosters/goldPriceMultiplier'
    DETAILS_MODIFIERS_BOOSTERS_CREDITSPRICEMULTIPLIER = b'#quests:details/modifiers/boosters/creditsPriceMultiplier'
    DETAILS_MODIFIERS_BOOSTERS_CRYSTALPRICEMULTIPLIER = b'#quests:details/modifiers/boosters/crystalPriceMultiplier'
    CLASSES_LIGHTTANK = b'#quests:classes/lightTank'
    CLASSES_MEDIUMTANK = b'#quests:classes/mediumTank'
    CLASSES_HEAVYTANK = b'#quests:classes/heavyTank'
    CLASSES_SPG = b'#quests:classes/SPG'
    CLASSES_AT_SPG = b'#quests:classes/AT-SPG'
    CLASSES_SMALL_LIGHTTANK = b'#quests:classes/small/lightTank'
    CLASSES_SMALL_MEDIUMTANK = b'#quests:classes/small/mediumTank'
    CLASSES_SMALL_HEAVYTANK = b'#quests:classes/small/heavyTank'
    CLASSES_SMALL_SPG = b'#quests:classes/small/SPG'
    CLASSES_SMALL_AT_SPG = b'#quests:classes/small/AT-SPG'
    TILECHAINSVIEW_TITLE = b'#quests:tileChainsView/title'
    MISSIONS_GROUP_OTHERS_LABEL = b'#quests:missions/group/others/label'
    MISSIONS_GROUP_MOTIVE_LABEL = b'#quests:missions/group/motive/label'
    MISSIONS_AWARDS_MERGED = b'#quests:missions/awards/merged'
    MISSIONS_TAB_LABEL_KURSK = b'#quests:missions/tab/label/kursk'
    MISSIONS_TAB_LABEL_MARATHON = b'#quests:missions/tab/label/marathon'
    MISSIONS_TAB_KURSK_HEADER = b'#quests:missions/tab/kursk/header'
    MISSIONS_TAB_KURSK_BODY = b'#quests:missions/tab/kursk/body'
    MISSIONS_TAB_MARATHONS_HEADER = b'#quests:missions/tab/marathons/header'
    MISSIONS_TAB_MARATHONS_BODY = b'#quests:missions/tab/marathons/body'
    MISSIONS_TAB_LABEL_MAY21_MARATHON = b'#quests:missions/tab/label/may21_marathon'
    MISSIONS_TAB_MAY21_MARATHON_HEADER = b'#quests:missions/tab/may21_marathon/header'
    MISSIONS_TAB_MOON_MARATHON_BODY = b'#quests:missions/tab/moon_marathon/body'
    MISSIONS_TAB_MISSIONS_HEADER = b'#quests:missions/tab/missions/header'
    MISSIONS_TAB_MISSIONS_BODY = b'#quests:missions/tab/missions/body'
    MISSIONS_TAB_LABEL_MISSIONS = b'#quests:missions/tab/label/missions'
    MISSIONS_TAB_LABEL_EVENTBOARDS = b'#quests:missions/tab/label/eventBoards'
    MISSIONS_TAB_LABEL_DAILY = b'#quests:missions/tab/label/daily'
    MISSIONS_TAB_EVENTBOARDS_HEADER = b'#quests:missions/tab/eventBoards/header'
    MISSIONS_TAB_EVENTBOARDS_BODY = b'#quests:missions/tab/eventBoards/body'
    MISSIONS_TAB_EVENTBOARDS_DISABLED = b'#quests:missions/tab/eventBoards/disabled'
    MISSIONS_TAB_EVENTBOARDS_DISABLED_HEADER = b'#quests:missions/tab/eventBoards/disabled/header'
    MISSIONS_TAB_EVENTBOARDS_DISABLED_BODY = b'#quests:missions/tab/eventBoards/disabled/body'
    MISSIONS_BATTLE_EVENTBOARDS_DATE = b'#quests:missions/battle/eventBoards/date'
    MISSIONS_BATTLE_EVENTBOARDS_VEHICLES = b'#quests:missions/battle/eventBoards/vehicles'
    MISSIONS_BATTLE_EVENTBOARDS_RESULT = b'#quests:missions/battle/eventBoards/result'
    MISSIONS_TAB_LABEL_CATEGORIES = b'#quests:missions/tab/label/categories'
    MISSIONS_TAB_CATEGORIES_HEADER = b'#quests:missions/tab/categories/header'
    MISSIONS_TAB_CATEGORIES_BODY = b'#quests:missions/tab/categories/body'
    MISSIONS_TAB_DAILY_HEADER = b'#quests:missions/tab/daily/header'
    MISSIONS_TAB_DAILY_BODY = b'#quests:missions/tab/daily/body'
    MISSIONS_TAB_WINBACK_HEADER = b'#quests:missions/tab/winback/header'
    MISSIONS_TAB_WINBACK_BODY = b'#quests:missions/tab/winback/body'
    MISSIONS_TAB_BATTLE_PASS_BODY = b'#quests:missions/tab/battle_pass/body'
    MISSIONS_TAB_BATTLE_PASS_HEADER = b'#quests:missions/tab/battle_pass/header'
    MISSIONS_TAB_MAPBOX_HEADER = b'#quests:missions/tab/mapbox/header'
    MISSIONS_TAB_MAPBOX_BODY = b'#quests:missions/tab/mapbox/body'
    MISSIONS_TAB_BATTLEMATTERS_HEADER = b'#quests:missions/tab/battleMatters/header'
    MISSIONS_TAB_BATTLEMATTERS_BODY = b'#quests:missions/tab/battleMatters/body'
    MISSIONS_TAB_LABEL_CURRENTVEHICLE = b'#quests:missions/tab/label/currentVehicle'
    MISSIONS_TAB_CURRENTVEHICLE_HEADER = b'#quests:missions/tab/currentVehicle/header'
    MISSIONS_TAB_CURRENTVEHICLE_BODY = b'#quests:missions/tab/currentVehicle/body'
    MISSIONS_FILTERCOUNTER_LABEL = b'#quests:missions/filterCounter/label'
    MISSIONS_FILTERCOUNTER_CLOSEBUTTON_HEADER = b'#quests:missions/filterCounter/closeButton/header'
    MISSIONS_FILTERCOUNTER_CLOSEBUTTON_BODY = b'#quests:missions/filterCounter/closeButton/body'
    MISSIONS_FILTER_FILTERBUTTON_HEADER = b'#quests:missions/filter/filterButton/header'
    MISSIONS_FILTER_FILTERBUTTON_BODY = b'#quests:missions/filter/filterButton/body'
    MISSIONS_TAB_MARATHONS_HEADER_TITLE_ACTION = b'#quests:missions/tab/marathons/header/title/action'
    MISSIONS_TAB_MARATHONS_HEADER_PERIOD = b'#quests:missions/tab/marathons/header/period'
    MISSIONS_TAB_MARATHONS_HEADER_DESC = b'#quests:missions/tab/marathons/header/desc'
    MISSIONS_TAB_MARATHONS_HEADER_CONDITION = b'#quests:missions/tab/marathons/header/condition'
    MISSIONS_TAB_MARATHONS_HEADER_AWARD = b'#quests:missions/tab/marathons/header/award'
    MISSIONS_TAB_MARATHONS_HEADER_MOREAWARDS = b'#quests:missions/tab/marathons/header/moreAwards'
    MISSIONS_TAB_CATEGORY_HEADER_PERFORMEDTASKS = b'#quests:missions/tab/category/header/performedTasks'
    MISSIONS_TAB_LABEL_TEMP = b'#quests:missions/tab/label/temp'
    MISSIONS_FILTER_POPOVER_TITLE = b'#quests:missions/filter/popover/title'
    MISSIONS_FILTER_POPOVER_HIDEUNAVAILABLE = b'#quests:missions/filter/popover/hideUnavailable'
    MISSIONS_FILTER_POPOVER_HIDEDONE = b'#quests:missions/filter/popover/hideDone'
    MISSIONS_FILTER_POPOVER_DEFAULTBUTTON_LABEL = b'#quests:missions/filter/popover/defaultButton/label'
    MISSIONS_FILTER_POPOVER_DEFAULTBUTTON_HEADER = b'#quests:missions/filter/popover/defaultButton/header'
    MISSIONS_FILTER_POPOVER_DEFAULTBUTTON_BODY = b'#quests:missions/filter/popover/defaultButton/body'
    MISSIONS_NOTASKS_DUMMY_TEXT = b'#quests:missions/noTasks/dummy/text'
    MISSIONS_NOTASKSBODY_DUMMY_TEXT = b'#quests:missions/noTasksBody/dummy/text'
    MISSIONS_NOTASKSMARATHON_DUMMY_TEXT = b'#quests:missions/noTasksMarathon/dummy/text'
    MISSIONS_NOTASKSBODY_DUMMY_BTNLABEL = b'#quests:missions/noTasksBody/dummy/btnLabel'
    MISSIONDETAILS_VEHICLE_CONDITIONS_HEADER = b'#quests:missionDetails/vehicle/conditions/header'
    MISSIONDETAILS_VEHICLE_CONDITIONS_NATIONS = b'#quests:missionDetails/vehicle/conditions/nations'
    MISSIONDETAILS_VEHICLE_CONDITIONS_NATIONS_ALL = b'#quests:missionDetails/vehicle/conditions/nations/all'
    MISSIONDETAILS_VEHICLE_CONDITIONS_NATIONS_TOOLTIP = b'#quests:missionDetails/vehicle/conditions/nations/tooltip'
    MISSIONDETAILS_VEHICLE_CONDITIONS_TYPE = b'#quests:missionDetails/vehicle/conditions/type'
    MISSIONDETAILS_VEHICLE_CONDITIONS_TYPE_ALL = b'#quests:missionDetails/vehicle/conditions/type/all'
    MISSIONDETAILS_VEHICLE_CONDITIONS_TYPE_TOOLTIP = b'#quests:missionDetails/vehicle/conditions/type/tooltip'
    MISSIONDETAILS_VEHICLE_CONDITIONS_LEVEL = b'#quests:missionDetails/vehicle/conditions/level'
    MISSIONDETAILS_VEHICLE_CONDITIONS_LEVEL_ALL = b'#quests:missionDetails/vehicle/conditions/level/all'
    MISSIONDETAILS_STATUS_COMPLETED_DAILY = b'#quests:missionDetails/status/completed/daily'
    MISSIONDETAILS_STATUS_COMPLETED_WEEKLY = b'#quests:missionDetails/status/completed/weekly'
    MISSIONDETAILS_STATUS_NOTAVAILABLE = b'#quests:missionDetails/status/notAvailable'
    MISSIONDETAILS_STATUS_WRONGVEHICLE = b'#quests:missionDetails/status/wrongVehicle'
    MISSIONDETAILS_STATUS_DISABLED = b'#quests:missionDetails/status/disabled'
    MISSIONDETAILS_STATUS_NOTAVAILABLEBYTIME = b'#quests:missionDetails/status/notAvailableByTime'
    MISSIONDETAILS_STATUS_WRONGTIME = b'#quests:missionDetails/status/wrongTime'
    MISSIONDETAILS_BATTLECONDITION_LIST = b'#quests:missionDetails/battleCondition/list'
    MISSIONDETAILS_STATUS_NOTAVAILABLE_IN_FUTURE = b'#quests:missionDetails/status/notAvailable/in_future'
    MISSIONDETAILS_STATUS_NOTAVAILABLE_INVALID_WEEKDAY = b'#quests:missionDetails/status/notAvailable/invalid_weekday'
    MISSIONDETAILS_STATUS_NOTAVAILABLE_INVALID_TIME_INTERVAL = b'#quests:missionDetails/status/notAvailable/invalid_time_interval'
    MISSIONDETAILS_STATUS_NOTAVAILABLE_NEARESTTIME = b'#quests:missionDetails/status/notAvailable/nearestTime'
    MISSIONDETAILS_CONDITIONS_MAPSTYPE = b'#quests:missionDetails/conditions/mapsType'
    MISSIONDETAILS_CONDITIONS_MAPSTYPE_BODY = b'#quests:missionDetails/conditions/mapsType/body'
    MISSIONDETAILS_CONDITIONS_MAPS = b'#quests:missionDetails/conditions/maps'
    MISSIONDETAILS_CONDITIONS_MAPS_NOT = b'#quests:missionDetails/conditions/maps/not'
    MISSIONDETAILS_CONDITIONS_CLANMEMBERSHIP_SAME = b'#quests:missionDetails/conditions/clanMembership/same'
    MISSIONDETAILS_CONDITIONS_CLANMEMBERSHIP_ANY = b'#quests:missionDetails/conditions/clanMembership/any'
    MISSIONDETAILS_CONDITIONS_FORMATION = b'#quests:missionDetails/conditions/formation'
    MISSIONDETAILS_CONDITIONS_FORMATION_SQUAD = b'#quests:missionDetails/conditions/formation/squad'
    MISSIONDETAILS_CONDITIONS_BATTLEBONUSTYPE = b'#quests:missionDetails/conditions/battleBonusType'
    MISSIONDETAILS_CONDITIONS_BATTLEBONUSTYPE_BODY = b'#quests:missionDetails/conditions/battleBonusType/body'
    MISSIONDETAILS_CONDITIONS_LEVEL = b'#quests:missionDetails/conditions/level'
    MISSIONDETAILS_CONDITIONS_PLAYBATTLE = b'#quests:missionDetails/conditions/playBattle'
    MISSIONDETAILS_CONDITIONS_BATTLES = b'#quests:missionDetails/conditions/battles'
    MISSIONDETAILS_CONDITIONS_BATTLESUPPERLIMIT = b'#quests:missionDetails/conditions/battlesUpperLimit'
    MISSIONDETAILS_CONDITIONS_BATTLESINROW = b'#quests:missionDetails/conditions/battlesInRow'
    MISSIONDETAILS_CONDITIONS_GROUPBY_NOPROGRESS = b'#quests:missionDetails/conditions/groupBy/noProgress'
    MISSIONDETAILS_MISSIONSCOMPLETE = b'#quests:missionDetails/missionsComplete'
    MISSIONDETAILS_MISSIONSCOMPLETE_DAILY = b'#quests:missionDetails/missionsComplete/daily'
    MISSIONDETAILS_MISSIONSCOMPLETE_WEEKLY = b'#quests:missionDetails/missionsComplete/weekly'
    MISSIONDETAILS_MISSIONSCOMPLETECOUNTER = b'#quests:missionDetails/missionsCompleteCounter'
    MISSIONDETAILS_PERSONALQUEST_COMPLETE_LEFT = b'#quests:missionDetails/personalQuest/complete/left'
    MISSIONDETAILS_PERSONALQUEST_COMPLETE_LEFT_DAILY = b'#quests:missionDetails/personalQuest/complete/left/daily'
    MISSIONDETAILS_PERSONALQUEST_DETAILS_COMPLETE_LEFT_DAILY = b'#quests:missionDetails/personalQuest/details/complete/left/daily'
    MISSIONDETAILS_PERSONALQUEST_COMPLETE_LEFT_WEEKLY = b'#quests:missionDetails/personalQuest/complete/left/weekly'
    MISSIONDETAILS_PERSONALQUEST_DETAILS_COMPLETE_LEFT_WEEKLY = b'#quests:missionDetails/personalQuest/details/complete/left/weekly'
    MISSIONDETAILS_RESETDATE = b'#quests:missionDetails/resetDate'
    MISSIONDETAILS_WEEKLYRESET = b'#quests:missionDetails/weeklyReset'
    MISSIONDETAILS_DATE = b'#quests:missionDetails/date'
    MISSIONDETAILS_DATESINCE = b'#quests:missionDetails/dateSince'
    MISSIONDETAILS_DATETO = b'#quests:missionDetails/dateTo'
    MISSIONDETAILS_DESCRIPTION = b'#quests:missionDetails/description'
    MISSIONDETAILS_REQUIREMENTS_HEADER_UNAVAILABLE = b'#quests:missionDetails/requirements/header/unavailable'
    MISSIONDETAILS_REQUIREMENTS_HEADER_AVAILABLE = b'#quests:missionDetails/requirements/header/available'
    MISSIONDETAILS_REQUIREMENTS_CONCLUSION_AVAILABLE = b'#quests:missionDetails/requirements/conclusion/available'
    MISSIONDETAILS_REQUIREMENTS_CONCLUSION_UNAVAILABLE = b'#quests:missionDetails/requirements/conclusion/unavailable'
    MISSIONDETAILS_VEHICLESSELECT = b'#quests:missionDetails/vehiclesSelect'
    MISSIONDETAILS_VEHICLESAVAILABLE = b'#quests:missionDetails/vehiclesAvailable'
    MISSIONDETAILS_BOTTOMSTATUSCOMPLETE = b'#quests:missionDetails/bottomStatusComplete'
    MISSIONDETAILS_BOTTOMSTATUSTOKENS = b'#quests:missionDetails/bottomStatusTokens'
    MISSIONDETAILS_BOTTOMSTATUSNEXTTRY = b'#quests:missionDetails/bottomStatusNextTry'
    MISSIONDETAILS_NEXTPAGEBTN_LABEL = b'#quests:missionDetails/nextPageBtn/label'
    MISSIONDETAILS_PREVPAGEBTN_LABEL = b'#quests:missionDetails/prevPageBtn/label'
    MISSIONS_TOKENPOPOVER_HEADER = b'#quests:missions/tokenPopover/header'
    MISSIONS_TOKENPOPOVER_DESCR = b'#quests:missions/tokenPopover/descr'
    MISSIONS_TOKENPOPOVER_DESCR_SHOP = b'#quests:missions/tokenPopover/descr/shop'
    MISSIONS_TOKENPOPOVER_BUYBTN_LABEL = b'#quests:missions/tokenPopover/buyBtn/label'
    MISSIONS_TOKENPOPOVER_QUEST_HEADER = b'#quests:missions/tokenPopover/quest/header'
    MISSIONS_TOKENPOPOVER_QUEST_DESCR_DATE = b'#quests:missions/tokenPopover/quest/descr/date'
    MISSIONS_TOKENPOPOVER_QUEST_DESCR_READY = b'#quests:missions/tokenPopover/quest/descr/ready'
    MISSIONS_TOKENPOPOVER_QUEST_DESCR_NOTAVAILABLE = b'#quests:missions/tokenPopover/quest/descr/notAvailable'
    MISSIONS_VEHICLESELECTOR_TITLE = b'#quests:missions/vehicleSelector/title'
    MISSIONS_VEHICLESELECTOR_STATUS_SELECTED = b'#quests:missions/vehicleSelector/status/selected'
    MISSIONS_VEHICLESELECTOR_STATUS_SELECT = b'#quests:missions/vehicleSelector/status/select'
    MISSIONS_VEHICLESELECTOR_STATUS_LIST = b'#quests:missions/vehicleSelector/status/list'
    MISSIONS_VEHICLESELECTOR_STATUS_NOTAVAILABLE = b'#quests:missions/vehicleSelector/status/notAvailable'
    MISSIONS_VEHICLESELECTOR_STATUS_NOITEMS = b'#quests:missions/vehicleSelector/status/noItems'
    TOKEN_UNDEFINED = b'#quests:token/undefined'
    TOKEN_DEFAULT_USSR = b'#quests:token/default/ussr'
    TOKEN_DEFAULT_GERMANY = b'#quests:token/default/germany'
    TOKEN_DEFAULT_USA = b'#quests:token/default/usa'
    TOKEN_DEFAULT_FRANCE = b'#quests:token/default/france'
    TOKEN_DEFAULT_UK = b'#quests:token/default/uk'
    TOKEN_DEFAULT_CZECH = b'#quests:token/default/czech'
    TOKEN_DEFAULT_CHINA = b'#quests:token/default/china'
    TOKEN_DEFAULT_JAPAN = b'#quests:token/default/japan'
    TOKEN_DEFAULT_POLAND = b'#quests:token/default/poland'
    TOKEN_DEFAULT_SWEDEN = b'#quests:token/default/sweden'
    TOKEN_DEFAULT_ITALY = b'#quests:token/default/italy'
    TOKEN_DEFAULT_INTUNION = b'#quests:token/default/intunion'
    TOKEN_DEFAULT_WOT = b'#quests:token/default/wot'
    TOKEN_DEFAULT_DEFAULT = b'#quests:token/default/default'
    TOKEN_DEFAULT_LIGHTTANK = b'#quests:token/default/lightTank'
    TOKEN_DEFAULT_MEDIUMTANK = b'#quests:token/default/mediumTank'
    TOKEN_DEFAULT_HEAVYTANK = b'#quests:token/default/heavyTank'
    TOKEN_DEFAULT_AT_SPG = b'#quests:token/default/at-spg'
    TOKEN_DEFAULT_SPG = b'#quests:token/default/spg'
    TOKEN_DEFAULT_SHELL = b'#quests:token/default/shell'
    TOKEN_DEFAULT_RICOCHET = b'#quests:token/default/ricochet'
    TOKEN_DEFAULT_PENETRATION = b'#quests:token/default/penetration'
    TOKEN_DEFAULT_AIM = b'#quests:token/default/aim'
    TOKEN_DEFAULT_FIRE = b'#quests:token/default/fire'
    TOKEN_DEFAULT_TURRET = b'#quests:token/default/turret'
    TOKEN_DEFAULT_TRACK = b'#quests:token/default/track'
    TOKEN_DEFAULT_FOLDER = b'#quests:token/default/folder'
    TOKEN_DEFAULT_LEAFLET = b'#quests:token/default/leaflet'
    TOKEN_DEFAULT_WHEEL = b'#quests:token/default/wheel'
    TOKEN_DEFAULT_BOX = b'#quests:token/default/box'
    TOKEN_DEFAULT_TANKREWARDS = b'#quests:token/default/tankrewards'
    TOKEN_DEFAULT_BATTLE_ROYALE = b'#quests:token/default/battle_royale'
    TOKEN_DEFAULT_VERSUS_AI_REGULAR = b'#quests:token/default/versus_ai_regular'
    TOKEN_DEFAULT_VERSUS_AI_WINBACK = b'#quests:token/default/versus_ai_winback'
    BONUSNAME_CREDITS = b'#quests:bonusName/credits'
    BONUSNAME_GOLD = b'#quests:bonusName/gold'
    BONUSNAME_CRYSTAL = b'#quests:bonusName/crystal'
    BONUSNAME_EVENTCOIN = b'#quests:bonusName/eventCoin'
    BONUSNAME_BPCOIN = b'#quests:bonusName/bpcoin'
    BONUSNAME_EQUIPCOIN = b'#quests:bonusName/equipCoin'
    BONUSNAME_XP = b'#quests:bonusName/xp'
    BONUSNAME_FREEXP = b'#quests:bonusName/freeXP'
    BONUSNAME_TANKMENXP = b'#quests:bonusName/tankmenXP'
    BONUSNAME_XPFACTOR = b'#quests:bonusName/xpFactor'
    BONUSNAME_CREDITSFACTOR = b'#quests:bonusName/creditsFactor'
    BONUSNAME_FREEXPFACTOR = b'#quests:bonusName/freeXPFactor'
    BONUSNAME_TANKMENXPFACTOR = b'#quests:bonusName/tankmenXPFactor'
    BONUSNAME_DAILYXPFACTOR = b'#quests:bonusName/dailyXPFactor'
    BONUSNAME_SLOTS = b'#quests:bonusName/slots'
    BONUSNAME_BERTHS = b'#quests:bonusName/berths'
    BONUSNAME_PREMIUM = b'#quests:bonusName/premium'
    BONUSNAME_PREMIUM_PLUS = b'#quests:bonusName/premium_plus'
    BONUSNAME_TANKMEN_WITH_SKILLS = b'#quests:bonusName/tankmen/with_skills'
    BONUSNAME_TANKMEN_NO_SKILLS = b'#quests:bonusName/tankmen/no_skills'
    BONUSNAME_CAMOUFLAGE = b'#quests:bonusName/camouflage'
    BONUSNAME_EMBLEM = b'#quests:bonusName/emblem'
    BONUSNAME_INSCRIPTION = b'#quests:bonusName/inscription'
    BONUSNAME_DECAL = b'#quests:bonusName/decal'
    BONUSNAME_PAINT = b'#quests:bonusName/paint'
    BONUSNAME_STYLE = b'#quests:bonusName/style'
    BONUSNAME_MODIFICATION = b'#quests:bonusName/modification'
    BONUSNAME_FREETOKENS = b'#quests:bonusName/freeTokens'
    BONUSNAME_COMPLETIONTOKENS = b'#quests:bonusName/completionTokens'
    BONUSNAME_COMPLETIONTOKENS_1_1 = b'#quests:bonusName/completionTokens_1_1'
    BONUSNAME_COMPLETIONTOKENS_1_2 = b'#quests:bonusName/completionTokens_1_2'
    BONUSNAME_COMPLETIONTOKENS_1_3 = b'#quests:bonusName/completionTokens_1_3'
    BONUSNAME_COMPLETIONTOKENS_1_4 = b'#quests:bonusName/completionTokens_1_4'
    BONUSNAME_COMPLETIONTOKENS_1_5 = b'#quests:bonusName/completionTokens_1_5'
    BONUSNAME_COMPLETIONTOKENS_2_1 = b'#quests:bonusName/completionTokens_2_1'
    BONUSNAME_COMPLETIONTOKENS_2_2 = b'#quests:bonusName/completionTokens_2_2'
    BONUSNAME_COMPLETIONTOKENS_2_3 = b'#quests:bonusName/completionTokens_2_3'
    BONUSNAME_COMPLETIONTOKENS_2_4 = b'#quests:bonusName/completionTokens_2_4'
    BONUSNAME_COMPLETIONTOKENS_2_5 = b'#quests:bonusName/completionTokens_2_5'
    BONUSNAME_COMPLETIONTOKENS_3_1 = b'#quests:bonusName/completionTokens_3_1'
    BONUSNAME_COMPLETIONTOKENS_3_2 = b'#quests:bonusName/completionTokens_3_2'
    BONUSNAME_COMPLETIONTOKENS_3_3 = b'#quests:bonusName/completionTokens_3_3'
    BONUSNAME_COMPLETIONTOKENS_3_4 = b'#quests:bonusName/completionTokens_3_4'
    BONUSNAME_COMPLETIONTOKENS_3_5 = b'#quests:bonusName/completionTokens_3_5'
    BONUSNAME_COMPLETIONTOKENS_4_1 = b'#quests:bonusName/completionTokens_4_1'
    BONUSNAME_COMPLETIONTOKENS_4_2 = b'#quests:bonusName/completionTokens_4_2'
    BONUSNAME_COMPLETIONTOKENS_4_3 = b'#quests:bonusName/completionTokens_4_3'
    BONUSNAME_COMPLETIONTOKENS_4_4 = b'#quests:bonusName/completionTokens_4_4'
    BONUSNAME_COMPLETIONTOKENS_4_5 = b'#quests:bonusName/completionTokens_4_5'
    BONUSNAME_COMPLETIONTOKENS_5_1 = b'#quests:bonusName/completionTokens_5_1'
    BONUSNAME_COMPLETIONTOKENS_5_2 = b'#quests:bonusName/completionTokens_5_2'
    BONUSNAME_COMPLETIONTOKENS_5_3 = b'#quests:bonusName/completionTokens_5_3'
    BONUSNAME_COMPLETIONTOKENS_5_4 = b'#quests:bonusName/completionTokens_5_4'
    BONUSNAME_COMPLETIONTOKENS_6_1 = b'#quests:bonusName/completionTokens_6_1'
    BONUSNAME_COMPLETIONTOKENS_6_2 = b'#quests:bonusName/completionTokens_6_2'
    BONUSNAME_COMPLETIONTOKENS_6_3 = b'#quests:bonusName/completionTokens_6_3'
    BONUSNAME_COMPLETIONTOKENS_6_4 = b'#quests:bonusName/completionTokens_6_4'
    BONUSNAME_COMPLETIONTOKENS_7_1 = b'#quests:bonusName/completionTokens_7_1'
    BONUSNAME_COMPLETIONTOKENS_7_2 = b'#quests:bonusName/completionTokens_7_2'
    BONUSNAME_COMPLETIONTOKENS_7_3 = b'#quests:bonusName/completionTokens_7_3'
    BONUSNAME_COMPLETIONTOKENS_7_4 = b'#quests:bonusName/completionTokens_7_4'
    BONUSNAME_PROJECTIONDECAL = b'#quests:bonusName/projectionDecal'
    BONUSNAME_PERSONALNUMBER = b'#quests:bonusName/personalNumber'
    BONUSNAME_RANKEDDAILYBATTLES = b'#quests:bonusName/rankedDailyBattles'
    BONUSNAME_RANKEDBONUSBATTLES = b'#quests:bonusName/rankedBonusBattles'
    BONUSNAME_ENTITLEMENTS_TESTENTITLEMENT = b'#quests:bonusName/entitlements/testEntitlement'
    BONUSNAME_ENTITLEMENTS_RANKED_2020_DISCOUNT = b'#quests:bonusName/entitlements/ranked_2020_discount'
    BONUSNAME_ENTITLEMENTS_RANKED_202203_ACCESS = b'#quests:bonusName/entitlements/ranked_202203_access'
    BONUSNAME_ENTITLEMENTS_PARAGON_REWARDS_CHOICE_V_11 = b'#quests:bonusName/entitlements/paragon_rewards_choice_v_11'
    BONUSNAME_ENTITLEMENTS_SHEVENTS_CLAN_COUPON = b'#quests:bonusName/entitlements/shevents_clan_coupon'
    BONUSNAME_ENTITLEMENTS_SHEVENTS_CLAN_CHEVRON = b'#quests:bonusName/entitlements/shevents_clan_chevron'
    BONUSNAME_BATTLE_BONUS_X5 = b'#quests:bonusName/battle_bonus_x5'
    BONUSNAME_CREW_BONUS_X3 = b'#quests:bonusName/crew_bonus_x3'
    BONUSNAME_BATTLEPASSPOINTS = b'#quests:bonusName/battlePassPoints'
    BONUSNAME_BATTLEPASSPOINTS_PREVIEW = b'#quests:bonusName/battlePassPoints/preview'
    BONUSNAME_BRCOIN = b'#quests:bonusName/brcoin'
    BONUSNAME_GOLD_BANK = b'#quests:bonusName/gold_bank'
    BONUSNAME_IDLE_CREW_XP = b'#quests:bonusName/idle_crew_xp'
    BONUSNAME_EXCLUDED_MAP = b'#quests:bonusName/excluded_map'
    BONUSNAME_FREE_EQUIPMENT_DEMOUNTING = b'#quests:bonusName/free_equipment_demounting'
    BONUSNAME_EXCLUSIVE_VEHICLE = b'#quests:bonusName/exclusive_vehicle'
    BONUSNAME_ATTENDANCE_REWARD = b'#quests:bonusName/attendance_reward'
    BONUSNAME_TEAM_CREDITS_BONUS = b'#quests:bonusName/team_credits_bonus'
    BONUSNAME_DAILY_QUESTS_REWARDS = b'#quests:bonusName/daily_quests_rewards'
    BONUSNAME_CLAN_SEASON_PROGRESS = b'#quests:bonusName/clan_season_progress'
    BONUSNAME_BUMBLEBEE_COIN = b'#quests:bonusName/bumblebee_coin'
    BONUSNAME_HONEY_COIN = b'#quests:bonusName/honey_coin'
    BONUSNAME_REWARDSSLOTS = b'#quests:bonusName/rewardsSlots'
    ACTION_AUTO_CALENDAR = b'#quests:action/auto/calendar'
    ACTION_FULL_CALENDAR = b'#quests:action/full/calendar'
    ACTION_HERO_FULL_CALENDAR = b'#quests:action/hero/full/calendar'
    ACTION_BUTTON_CALENDAR = b'#quests:action/button/calendar'
    ACTION_SHORT_CALENDAR = b'#quests:action/short/calendar'
    ACTION_SUBHEADER_CALENDAR = b'#quests:action/subheader/calendar'
    ACTION_AUTO_EXCHANGERATE = b'#quests:action/auto/exchangeRate'
    ACTION_FULL_EXCHANGERATE = b'#quests:action/full/exchangeRate'
    ACTION_HERO_FULL_EXCHANGERATE = b'#quests:action/hero/full/exchangeRate'
    ACTION_SHORT_EXCHANGERATE = b'#quests:action/short/exchangeRate'
    ACTION_BUTTON_EXCHANGERATE = b'#quests:action/button/exchangeRate'
    ACTION_AUTO_PAIDREMOVALCOST = b'#quests:action/auto/paidRemovalCost'
    ACTION_FULL_PAIDREMOVALCOST = b'#quests:action/full/paidRemovalCost'
    ACTION_HERO_FULL_PAIDREMOVALCOST = b'#quests:action/hero/full/paidRemovalCost'
    ACTION_SHORT_PAIDREMOVALCOST = b'#quests:action/short/paidRemovalCost'
    ACTION_BUTTON_PAIDREMOVALCOST = b'#quests:action/button/paidRemovalCost'
    ACTION_AUTO_CHANGEROLECOST = b'#quests:action/auto/changeRoleCost'
    ACTION_FULL_CHANGEROLECOST = b'#quests:action/full/changeRoleCost'
    ACTION_HERO_FULL_CHANGEROLECOST = b'#quests:action/hero/full/changeRoleCost'
    ACTION_SHORT_CHANGEROLECOST = b'#quests:action/short/changeRoleCost'
    ACTION_BUTTON_CHANGEROLECOST = b'#quests:action/button/changeRoleCost'
    ACTION_AUTO_FREEXPCONVERSIONDISCRECITY = b'#quests:action/auto/freeXPConversionDiscrecity'
    ACTION_FULL_FREEXPCONVERSIONDISCRECITY = b'#quests:action/full/freeXPConversionDiscrecity'
    ACTION_HERO_FULL_FREEXPCONVERSIONDISCRECITY = b'#quests:action/hero/full/freeXPConversionDiscrecity'
    ACTION_SHORT_FREEXPCONVERSIONDISCRECITY = b'#quests:action/short/freeXPConversionDiscrecity'
    ACTION_BUTTON_FREEXPCONVERSIONDISCRECITY = b'#quests:action/button/freeXPConversionDiscrecity'
    ACTION_AUTO_SLOTSPRICES = b'#quests:action/auto/slotsPrices'
    ACTION_FULL_SLOTSPRICES = b'#quests:action/full/slotsPrices'
    ACTION_HERO_FULL_SLOTSPRICES = b'#quests:action/hero/full/slotsPrices'
    ACTION_SHORT_SLOTSPRICES = b'#quests:action/short/slotsPrices'
    ACTION_BUTTON_SLOTSPRICES = b'#quests:action/button/slotsPrices'
    ACTION_AUTO_BERTHSPRICES = b'#quests:action/auto/berthsPrices'
    ACTION_FULL_BERTHSPRICES = b'#quests:action/full/berthsPrices'
    ACTION_HERO_FULL_BERTHSPRICES = b'#quests:action/hero/full/berthsPrices'
    ACTION_SHORT_BERTHSPRICES = b'#quests:action/short/berthsPrices'
    ACTION_BUTTON_BERTHSPRICES = b'#quests:action/button/berthsPrices'
    ACTION_AUTO_CREDITSTANKMANCOST = b'#quests:action/auto/creditsTankmanCost'
    ACTION_FULL_CREDITSTANKMANCOST = b'#quests:action/full/creditsTankmanCost'
    ACTION_HERO_FULL_CREDITSTANKMANCOST = b'#quests:action/hero/full/creditsTankmanCost'
    ACTION_SHORT_CREDITSTANKMANCOST = b'#quests:action/short/creditsTankmanCost'
    ACTION_BUTTON_CREDITSTANKMANCOST = b'#quests:action/button/creditsTankmanCost'
    ACTION_AUTO_GOLDTANKMANCOST = b'#quests:action/auto/goldTankmanCost'
    ACTION_FULL_GOLDTANKMANCOST = b'#quests:action/full/goldTankmanCost'
    ACTION_HERO_FULL_GOLDTANKMANCOST = b'#quests:action/hero/full/goldTankmanCost'
    ACTION_SHORT_GOLDTANKMANCOST = b'#quests:action/short/goldTankmanCost'
    ACTION_BUTTON_GOLDTANKMANCOST = b'#quests:action/button/goldTankmanCost'
    ACTION_AUTO_TANKMEN_MIXED = b'#quests:action/auto/tankmen/mixed'
    ACTION_FULL_TANKMEN_MIXED = b'#quests:action/full/tankmen/mixed'
    ACTION_HERO_FULL_TANKMEN_MIXED = b'#quests:action/hero/full/tankmen/mixed'
    ACTION_SHORT_TANKMEN_MIXED = b'#quests:action/short/tankmen/mixed'
    ACTION_BUTTON_TANKMEN_MIXED = b'#quests:action/button/tankmen/mixed'
    ACTION_AUTO_CREDITSDROPSKILLSCOST = b'#quests:action/auto/creditsDropSkillsCost'
    ACTION_FULL_CREDITSDROPSKILLSCOST = b'#quests:action/full/creditsDropSkillsCost'
    ACTION_HERO_FULL_CREDITSDROPSKILLSCOST = b'#quests:action/hero/full/creditsDropSkillsCost'
    ACTION_SHORT_CREDITSDROPSKILLSCOST = b'#quests:action/short/creditsDropSkillsCost'
    ACTION_BUTTON_CREDITSDROPSKILLSCOST = b'#quests:action/button/creditsDropSkillsCost'
    ACTION_AUTO_GOLDDROPSKILLSCOST = b'#quests:action/auto/goldDropSkillsCost'
    ACTION_FULL_GOLDDROPSKILLSCOST = b'#quests:action/full/goldDropSkillsCost'
    ACTION_HERO_FULL_GOLDDROPSKILLSCOST = b'#quests:action/hero/full/goldDropSkillsCost'
    ACTION_SHORT_GOLDDROPSKILLSCOST = b'#quests:action/short/goldDropSkillsCost'
    ACTION_BUTTON_GOLDDROPSKILLSCOST = b'#quests:action/button/goldDropSkillsCost'
    ACTION_AUTO_DROPSKILLS_MIXED = b'#quests:action/auto/dropSkills/mixed'
    ACTION_FULL_DROPSKILLS_MIXED = b'#quests:action/full/dropSkills/mixed'
    ACTION_HERO_FULL_DROPSKILLS_MIXED = b'#quests:action/hero/full/dropSkills/mixed'
    ACTION_SHORT_DROPSKILLS_MIXED = b'#quests:action/short/dropSkills/mixed'
    ACTION_BUTTON_DROPSKILLS_MIXED = b'#quests:action/button/dropSkills/mixed'
    ACTION_AUTO_PASSPORTCHANGECOST = b'#quests:action/auto/passportChangeCost'
    ACTION_FULL_PASSPORTCHANGECOST = b'#quests:action/full/passportChangeCost'
    ACTION_HERO_FULL_PASSPORTCHANGECOST = b'#quests:action/hero/full/passportChangeCost'
    ACTION_SHORT_PASSPORTCHANGECOST = b'#quests:action/short/passportChangeCost'
    ACTION_BUTTON_PASSPORTCHANGECOST = b'#quests:action/button/passportChangeCost'
    ACTION_AUTO_FEMALEPASSPORTCHANGECOST = b'#quests:action/auto/femalePassportChangeCost'
    ACTION_FULL_FEMALEPASSPORTCHANGECOST = b'#quests:action/full/femalePassportChangeCost'
    ACTION_HERO_FULL_FEMALEPASSPORTCHANGECOST = b'#quests:action/hero/full/femalePassportChangeCost'
    ACTION_SHORT_FEMALEPASSPORTCHANGECOST = b'#quests:action/short/femalePassportChangeCost'
    ACTION_BUTTON_FEMALEPASSPORTCHANGECOST = b'#quests:action/button/femalePassportChangeCost'
    ACTION_AUTO_MUL_EQUIPMENTPRICEALL = b'#quests:action/auto/mul_EquipmentPriceAll'
    ACTION_AUTO_EQUIPMENT_CREDITSPRICEMULTIPLIER = b'#quests:action/auto/equipment/creditsPriceMultiplier'
    ACTION_SHORT_EQUIPMENT_CREDITSPRICEMULTIPLIER = b'#quests:action/short/equipment/creditsPriceMultiplier'
    ACTION_BUTTON_EQUIPMENT_CREDITSPRICEMULTIPLIER = b'#quests:action/button/equipment/creditsPriceMultiplier'
    ACTION_AUTO_EQUIPMENT_GOLDPRICEMULTIPLIER = b'#quests:action/auto/equipment/goldPriceMultiplier'
    ACTION_SHORT_EQUIPMENT_GOLDPRICEMULTIPLIER = b'#quests:action/short/equipment/goldPriceMultiplier'
    ACTION_BUTTON_EQUIPMENT_GOLDPRICEMULTIPLIER = b'#quests:action/button/equipment/goldPriceMultiplier'
    ACTION_AUTO_EQUIPMENT_MIXED = b'#quests:action/auto/equipment/mixed'
    ACTION_SHORT_EQUIPMENT_MIXED = b'#quests:action/short/equipment/mixed'
    ACTION_BUTTON_EQUIPMENT_MIXED = b'#quests:action/button/equipment/mixed'
    ACTION_AUTO_SET_EQUIPMENTPRICE = b'#quests:action/auto/set_EquipmentPrice'
    ACTION_SHORT_SET_EQUIPMENTPRICE = b'#quests:action/short/set_EquipmentPrice'
    ACTION_BUTTON_SET_EQUIPMENTPRICE = b'#quests:action/button/set_EquipmentPrice'
    ACTION_AUTO_MUL_EQUIPMENTPRICE = b'#quests:action/auto/mul_EquipmentPrice'
    ACTION_SHORT_MUL_EQUIPMENTPRICE = b'#quests:action/short/mul_EquipmentPrice'
    ACTION_BUTTON_MUL_EQUIPMENTPRICE = b'#quests:action/button/mul_EquipmentPrice'
    ACTION_AUTO_MUL_OPTIONALDEVICEPRICEALL = b'#quests:action/auto/mul_OptionalDevicePriceAll'
    ACTION_SHORT_MUL_OPTIONALDEVICEPRICEALL = b'#quests:action/short/mul_OptionalDevicePriceAll'
    ACTION_BUTTON_MUL_OPTIONALDEVICEPRICEALL = b'#quests:action/button/mul_OptionalDevicePriceAll'
    ACTION_AUTO_SET_OPTIONALDEVICEPRICE = b'#quests:action/auto/set_OptionalDevicePrice'
    ACTION_SHORT_SET_OPTIONALDEVICEPRICE = b'#quests:action/short/set_OptionalDevicePrice'
    ACTION_BUTTON_SET_OPTIONALDEVICEPRICE = b'#quests:action/button/set_OptionalDevicePrice'
    ACTION_AUTO_MUL_OPTIONALDEVICEPRICE = b'#quests:action/auto/mul_OptionalDevicePrice'
    ACTION_SHORT_MUL_OPTIONALDEVICEPRICE = b'#quests:action/short/mul_OptionalDevicePrice'
    ACTION_BUTTON_MUL_OPTIONALDEVICEPRICE = b'#quests:action/button/mul_OptionalDevicePrice'
    ACTION_AUTO_MUL_SHELLPRICEALL = b'#quests:action/auto/mul_ShellPriceAll'
    ACTION_AUTO_SHELL_CREDITSPRICEMULTIPLIER = b'#quests:action/auto/shell/creditsPriceMultiplier'
    ACTION_FULL_SHELL_CREDITSPRICEMULTIPLIER = b'#quests:action/full/shell/creditsPriceMultiplier'
    ACTION_HERO_FULL_SHELL_CREDITSPRICEMULTIPLIER = b'#quests:action/hero/full/shell/creditsPriceMultiplier'
    ACTION_SHORT_SHELL_CREDITSPRICEMULTIPLIER = b'#quests:action/short/shell/creditsPriceMultiplier'
    ACTION_BUTTON_SHELL_CREDITSPRICEMULTIPLIER = b'#quests:action/button/shell/creditsPriceMultiplier'
    ACTION_AUTO_SHELL_GOLDPRICEMULTIPLIER = b'#quests:action/auto/shell/goldPriceMultiplier'
    ACTION_FULL_SHELL_GOLDPRICEMULTIPLIER = b'#quests:action/full/shell/goldPriceMultiplier'
    ACTION_HERO_FULL_SHELL_GOLDPRICEMULTIPLIER = b'#quests:action/hero/full/shell/goldPriceMultiplier'
    ACTION_SHORT_SHELL_GOLDPRICEMULTIPLIER = b'#quests:action/short/shell/goldPriceMultiplier'
    ACTION_BUTTON_SHELL_GOLDPRICEMULTIPLIER = b'#quests:action/button/shell/goldPriceMultiplier'
    ACTION_AUTO_SHELL_MIXED = b'#quests:action/auto/shell/mixed'
    ACTION_FULL_SHELL_MIXED = b'#quests:action/full/shell/mixed'
    ACTION_HERO_FULL_SHELL_MIXED = b'#quests:action/hero/full/shell/mixed'
    ACTION_SHORT_SHELL_MIXED = b'#quests:action/short/shell/mixed'
    ACTION_BUTTON_SHELL_MIXED = b'#quests:action/button/shell/mixed'
    ACTION_AUTO_MUL_SHELLPRICE = b'#quests:action/auto/mul_ShellPrice'
    ACTION_FULL_MUL_SHELLPRICE = b'#quests:action/full/mul_ShellPrice'
    ACTION_HERO_FULL_MUL_SHELLPRICE = b'#quests:action/hero/full/mul_ShellPrice'
    ACTION_SHORT_MUL_SHELLPRICE = b'#quests:action/short/mul_ShellPrice'
    ACTION_BUTTON_MUL_SHELLPRICE = b'#quests:action/button/mul_ShellPrice'
    ACTION_AUTO_SET_SHELLPRICE = b'#quests:action/auto/set_ShellPrice'
    ACTION_FULL_SET_SHELLPRICE = b'#quests:action/full/set_ShellPrice'
    ACTION_HERO_FULL_SET_SHELLPRICE = b'#quests:action/hero/full/set_ShellPrice'
    ACTION_SHORT_SET_SHELLPRICE = b'#quests:action/short/set_ShellPrice'
    ACTION_BUTTON_SET_SHELLPRICE = b'#quests:action/button/set_ShellPrice'
    ACTION_AUTO_VEHICLEBUYPRICE = b'#quests:action/auto/vehicleBuyPrice'
    ACTION_FULL_VEHICLEBUYPRICE = b'#quests:action/full/vehicleBuyPrice'
    ACTION_SHORT_VEHICLEBUYPRICE_MORE = b'#quests:action/short/vehicleBuyPrice/more'
    ACTION_SHORT_VEHICLEBUYPRICE_TWO = b'#quests:action/short/vehicleBuyPrice/two'
    ACTION_SHORT_VEHICLEBUYPRICE_ONE = b'#quests:action/short/vehicleBuyPrice/one'
    ACTION_BUTTON_VEHICLEBUYPRICE = b'#quests:action/button/vehicleBuyPrice'
    ACTION_AUTO_VEHICLERENTPRICE = b'#quests:action/auto/vehicleRentPrice'
    ACTION_SHORT_VEHICLERENTPRICE_MORE = b'#quests:action/short/vehicleRentPrice/more'
    ACTION_SHORT_VEHICLERENTPRICE_TWO = b'#quests:action/short/vehicleRentPrice/two'
    ACTION_SHORT_VEHICLERENTPRICE_ONE = b'#quests:action/short/vehicleRentPrice/one'
    ACTION_FULL_VEHICLERENTPRICE = b'#quests:action/full/vehicleRentPrice'
    ACTION_BUTTON_VEHICLERENTPRICE = b'#quests:action/button/vehicleRentPrice'
    ACTION_AUTO_CLANCREATIONCOST = b'#quests:action/auto/clanCreationCost'
    ACTION_FULL_CLANCREATIONCOST = b'#quests:action/full/clanCreationCost'
    ACTION_HERO_FULL_CLANCREATIONCOST = b'#quests:action/hero/full/clanCreationCost'
    ACTION_SHORT_CLANCREATIONCOST = b'#quests:action/short/clanCreationCost'
    ACTION_BUTTON_CLANCREATIONCOST = b'#quests:action/button/clanCreationCost'
    ACTION_AUTO_PREMIUMPACKET1COST = b'#quests:action/auto/premiumPacket1Cost'
    ACTION_FULL_PREMIUMPACKET1COST = b'#quests:action/full/premiumPacket1Cost'
    ACTION_HERO_FULL_PREMIUMPACKET1COST = b'#quests:action/hero/full/premiumPacket1Cost'
    ACTION_SHORT_PREMIUMPACKET1COST = b'#quests:action/short/premiumPacket1Cost'
    ACTION_AUTO_PREMIUMPACKET3COST = b'#quests:action/auto/premiumPacket3Cost'
    ACTION_FULL_PREMIUMPACKET3COST = b'#quests:action/full/premiumPacket3Cost'
    ACTION_HERO_FULL_PREMIUMPACKET3COST = b'#quests:action/hero/full/premiumPacket3Cost'
    ACTION_SHORT_PREMIUMPACKET3COST = b'#quests:action/short/premiumPacket3Cost'
    ACTION_AUTO_PREMIUMPACKET7COST = b'#quests:action/auto/premiumPacket7Cost'
    ACTION_FULL_PREMIUMPACKET7COST = b'#quests:action/full/premiumPacket7Cost'
    ACTION_HERO_FULL_PREMIUMPACKET7COST = b'#quests:action/hero/full/premiumPacket7Cost'
    ACTION_SHORT_PREMIUMPACKET7COST = b'#quests:action/short/premiumPacket7Cost'
    ACTION_AUTO_PREMIUMPACKET14COST = b'#quests:action/auto/premiumPacket14Cost'
    ACTION_FULL_PREMIUMPACKET14COST = b'#quests:action/full/premiumPacket14Cost'
    ACTION_HERO_FULL_PREMIUMPACKET14COST = b'#quests:action/hero/full/premiumPacket14Cost'
    ACTION_SHORT_PREMIUMPACKET14COST = b'#quests:action/short/premiumPacket14Cost'
    ACTION_AUTO_PREMIUMPACKET30COST = b'#quests:action/auto/premiumPacket30Cost'
    ACTION_FULL_PREMIUMPACKET30COST = b'#quests:action/full/premiumPacket30Cost'
    ACTION_HERO_FULL_PREMIUMPACKET30COST = b'#quests:action/hero/full/premiumPacket30Cost'
    ACTION_SHORT_PREMIUMPACKET30COST = b'#quests:action/short/premiumPacket30Cost'
    ACTION_AUTO_PREMIUMPACKET90COST = b'#quests:action/auto/premiumPacket90Cost'
    ACTION_FULL_PREMIUMPACKET90COST = b'#quests:action/full/premiumPacket90Cost'
    ACTION_HERO_FULL_PREMIUMPACKET90COST = b'#quests:action/hero/full/premiumPacket90Cost'
    ACTION_SHORT_PREMIUMPACKET90COST = b'#quests:action/short/premiumPacket90Cost'
    ACTION_AUTO_PREMIUMPACKET180COST = b'#quests:action/auto/premiumPacket180Cost'
    ACTION_FULL_PREMIUMPACKET180COST = b'#quests:action/full/premiumPacket180Cost'
    ACTION_HERO_FULL_PREMIUMPACKET180COST = b'#quests:action/hero/full/premiumPacket180Cost'
    ACTION_SHORT_PREMIUMPACKET180COST = b'#quests:action/short/premiumPacket180Cost'
    ACTION_AUTO_PREMIUMPACKET360COST = b'#quests:action/auto/premiumPacket360Cost'
    ACTION_FULL_PREMIUMPACKET360COST = b'#quests:action/full/premiumPacket360Cost'
    ACTION_HERO_FULL_PREMIUMPACKET360COST = b'#quests:action/hero/full/premiumPacket360Cost'
    ACTION_SHORT_PREMIUMPACKET360COST = b'#quests:action/short/premiumPacket360Cost'
    ACTION_BUTTON_PREMIUMPACKET_NEW = b'#quests:action/button/premiumPacket/new'
    ACTION_BUTTON_PREMIUMPACKET_CONTINUE = b'#quests:action/button/premiumPacket/continue'
    ACTION_AUTO_WINXPFACTORMODE_ALWAYS = b'#quests:action/auto/winXPFactorMode/always'
    ACTION_FULL_WINXPFACTORMODE_ALWAYS = b'#quests:action/full/winXPFactorMode/always'
    ACTION_SHORT_WINXPFACTORMODE_ALWAYS = b'#quests:action/short/winXPFactorMode/always'
    ACTION_BUTTON_WINXPFACTORMODE_ALWAYS = b'#quests:action/button/winXPFactorMode/always'
    ACTION_AUTO_WINXPFACTORMODE_DAILY = b'#quests:action/auto/winXPFactorMode/daily'
    ACTION_FULL_WINXPFACTORMODE_DAILY = b'#quests:action/full/winXPFactorMode/daily'
    ACTION_SHORT_WINXPFACTORMODE_DAILY = b'#quests:action/short/winXPFactorMode/daily'
    ACTION_BUTTON_WINXPFACTORMODE_DAILY = b'#quests:action/button/winXPFactorMode/daily'
    ACTION_AUTO_FREEXPTOTMANXPRATE = b'#quests:action/auto/freeXPToTManXPRate'
    ACTION_FULL_FREEXPTOTMANXPRATE = b'#quests:action/full/freeXPToTManXPRate'
    ACTION_HERO_FULL_FREEXPTOTMANXPRATE = b'#quests:action/hero/full/freeXPToTManXPRate'
    ACTION_SHORT_FREEXPTOTMANXPRATE = b'#quests:action/short/freeXPToTManXPRate'
    ACTION_BUTTON_FREEXPTOTMANXPRATE = b'#quests:action/button/freeXPToTManXPRate'
    ACTION_AUTO_MUL_GOODIEPRICEALL = b'#quests:action/auto/mul_GoodiePriceAll'
    ACTION_SHORT_MUL_GOODIEPRICEALL = b'#quests:action/short/mul_GoodiePriceAll'
    ACTION_BUTTON_MUL_GOODIEPRICEALL = b'#quests:action/button/mul_GoodiePriceAll'
    ACTION_AUTO_SET_GOODIEPRICE = b'#quests:action/auto/set_GoodiePrice'
    ACTION_SHORT_SET_GOODIEPRICE = b'#quests:action/short/set_GoodiePrice'
    ACTION_BUTTON_SET_GOODIEPRICE = b'#quests:action/button/set_GoodiePrice'
    ACTION_AUTO_MUL_GOODIEPRICE = b'#quests:action/auto/mul_GoodiePrice'
    ACTION_SHORT_MUL_GOODIEPRICE = b'#quests:action/short/mul_GoodiePrice'
    ACTION_BUTTON_MUL_GOODIEPRICE = b'#quests:action/button/mul_GoodiePrice'
    ACTION_AUTO_SET_PRICEGROUPPRICE = b'#quests:action/auto/set_PriceGroupPrice'
    ACTION_SHORT_SET_PRICEGROUPPRICE = b'#quests:action/short/set_PriceGroupPrice'
    ACTION_BUTTON_SET_PRICEGROUPPRICE = b'#quests:action/button/set_PriceGroupPrice'
    ACTION_AUTO_MUL_PRICEGROUPPRICE = b'#quests:action/auto/mul_PriceGroupPrice'
    ACTION_SHORT_MUL_PRICEGROUPPRICE = b'#quests:action/short/mul_PriceGroupPrice'
    ACTION_BUTTON_MUL_PRICEGROUPPRICE = b'#quests:action/button/mul_PriceGroupPrice'
    ACTION_AUTO_MUL_PRICEGROUPPRICEBYTAG = b'#quests:action/auto/mul_PriceGroupPriceByTag'
    ACTION_SHORT_MUL_PRICEGROUPPRICEBYTAG = b'#quests:action/short/mul_PriceGroupPriceByTag'
    ACTION_BUTTON_MUL_PRICEGROUPPRICEBYTAG = b'#quests:action/button/mul_PriceGroupPriceByTag'
    ACTION_AUTO_MUL_PRICEGROUPPRICEALL = b'#quests:action/auto/mul_PriceGroupPriceAll'
    ACTION_SHORT_MUL_PRICEGROUPPRICEALL = b'#quests:action/short/mul_PriceGroupPriceAll'
    ACTION_BUTTON_MUL_PRICEGROUPPRICEALL = b'#quests:action/button/mul_PriceGroupPriceAll'
    ACTION_AUTO_TRADEINSELLPRICEFACTOR = b'#quests:action/auto/tradeInSellPriceFactor'
    ACTION_FULL_TRADEINSELLPRICEFACTOR = b'#quests:action/full/tradeInSellPriceFactor'
    ACTION_HERO_FULL_TRADEINSELLPRICEFACTOR = b'#quests:action/hero/full/tradeInSellPriceFactor'
    ACTION_SHORT_TRADEINSELLPRICEFACTOR = b'#quests:action/short/tradeInSellPriceFactor'
    ACTION_BUTTON_TRADEINSELLPRICEFACTOR = b'#quests:action/button/tradeInSellPriceFactor'
    ACTION_DISCOUNT_MORE = b'#quests:action/discount/more'
    ACTION_DISCOUNT_DISCOUNTTEXT = b'#quests:action/discount/discountText'
    ACTION_DISCOUNT_DISCOUNTUPTOTEXT = b'#quests:action/discount/discountUpToText'
    ACTION_DISCOUNT_TRADEINLABELTEXT = b'#quests:action/discount/tradeInLabelText'
    ACTION_DISCOUNT_PERCENT = b'#quests:action/discount/percent'
    ACTION_DISCOUNT_MODIFIER = b'#quests:action/discount/modifier'
    ACTION_DISCOUNT_XP = b'#quests:action/discount/xp'
    ACTION_CHAIN_HINT_REMOVALCOST = b'#quests:action/chain/hint/removalCost'
    ACTION_CHAIN_HINT_SHELLSPRICE = b'#quests:action/chain/hint/shellsPrice'
    ACTION_CHAIN_HINT_OPENPERSONALCASE = b'#quests:action/chain/hint/openPersonalCase'
    ACTION_CHAIN_HINT_CHANGEROLEDISCOUNTAVAILABLE = b'#quests:action/chain/hint/changeRoleDiscountAvailable'
    ACTION_CHAIN_HINT_RETRAININGDISCOUNTAVAILABLE = b'#quests:action/chain/hint/retrainingDiscountAvailable'
    ACTION_CHAIN_HINT_OPENCREWBOOKS = b'#quests:action/chain/hint/openCrewBooks'
    ACTION_CHAIN_HINT_CREWRETAININGDISCOUNTAVAILABLE = b'#quests:action/chain/hint/crewRetainingDiscountAvailable'
    ACTION_CHAIN_HINT_DROPSKILLS = b'#quests:action/chain/hint/dropSkills'
    ACTION_CHAIN_HINT_CHANGEDOCUMENTS = b'#quests:action/chain/hint/changeDocuments'
    ACTION_CHAIN_HINT_CREWRETRAINING = b'#quests:action/chain/hint/crewRetraining'
    ACTION_CHAIN_HINT_WINXPFACTORMODE = b'#quests:action/chain/hint/winXPFactorMode'
    ACTION_CHAIN_HINT_PREMDAYS = b'#quests:action/chain/hint/premDays'
    ACTION_CHAIN_HINT_CUSTOMIZATION = b'#quests:action/chain/hint/customization'
    ACTION_CHAIN_HINT_CAMOUFLAGES = b'#quests:action/chain/hint/camouflages'
    ACTION_CHAIN_HINT_EMBLEMS = b'#quests:action/chain/hint/emblems'
    ACTION_CHAIN_HINT_INSCRIPTIONS = b'#quests:action/chain/hint/inscriptions'
    QUEST_CHAIN_HINT_HOLDAWARDSHEET = b'#quests:quest/chain/hint/holdAwardSheet'
    QUEST_CHAIN_HINT_PAUSE = b'#quests:quest/chain/hint/pause'
    ACTION_LABEL_BATTLEQUESTS = b'#quests:action/label/battleQuests'
    ACTION_EMPTY_INFO = b'#quests:action/empty/info'
    ACTION_EMPTY_BTNLABEL = b'#quests:action/empty/btnLabel'
    ACTION_COMINGSOON_LABEL = b'#quests:action/comingsoon/label'
    ACTION_COMINGSOON_TIME = b'#quests:action/comingsoon/time'
    ACTION_TIME_FINISH = b'#quests:action/time/finish'
    ACTION_TIME_LEFT = b'#quests:action/time/left'
    ACTION_MORE_TYPE_EQUIPMENT = b'#quests:action/more/type/equipment'
    ACTION_MORE_TYPE_OPTIONALDEVICES = b'#quests:action/more/type/optionalDevices'
    ACTION_MORE_TYPE_GOODIES = b'#quests:action/more/type/goodies'
    ACTION_MORE_TYPE_VEHICLES = b'#quests:action/more/type/vehicles'
    ACTION_MORE_TYPE_CUSTOMIZATIONS = b'#quests:action/more/type/customizations'
    ACTION_BOOSTER_BOOSTER_XP = b'#quests:action/booster/booster_xp'
    ACTION_BOOSTER_BOOSTER_FREE_XP = b'#quests:action/booster/booster_free_xp'
    ACTION_BOOSTER_BOOSTER_CREW_XP = b'#quests:action/booster/booster_crew_xp'
    ACTION_BOOSTER_BOOSTER_CREDITS = b'#quests:action/booster/booster_credits'
    ACTION_BOOSTER_BOOSTER_REPAIR = b'#quests:action/booster/booster_repair'
    ACTION_EXCHANGERATE_GOLD2CREDIT = b'#quests:action/exchangeRate/gold2credit'
    PERSONALMISSION_STATUS_LASTDONEWITHPAWN = b'#quests:personalMission/status/lastDoneWithPawn'
    PERSONALMISSION_STATUS_ONLYMAINDONE = b'#quests:personalMission/status/onlyMainDone'
    PERSONALMISSION_STATUS_ONLYADDDONE = b'#quests:personalMission/status/onlyAddDone'
    PERSONALMISSION_STATUS_MAINDONE = b'#quests:personalMission/status/mainDone'
    PERSONALMISSION_STATUS_FULLDONE = b'#quests:personalMission/status/fullDone'
    PERSONALMISSION_STATUS_ALLDONE = b'#quests:personalMission/status/allDone'
    PERSONALMISSION_STATUS_DONEWITHPAWN = b'#quests:personalMission/status/doneWithPawn'
    PERSONALMISSION_STATUS_INPROGRESS = b'#quests:personalMission/status/inProgress'
    PERSONALMISSION_STATUS_ISONPAUSE = b'#quests:personalMission/status/isOnPause'
    PERSONALMISSION_STATUS_FAILED = b'#quests:personalMission/status/failed'
    PERSONALMISSION_STATUS_ADDINPROGRESS = b'#quests:personalMission/status/addInProgress'
    PERSONALMISSION_STATUS_SHEETRECOVERYINPROGRESS = b'#quests:personalMission/status/sheetRecoveryInProgress'
    PERSONALMISSION_STATUS_ADDBOTTOMLOCKED_REGULAR = b'#quests:personalMission/status/addBottomLocked/regular'
    PERSONALMISSION_STATUS_ADDBOTTOMLOCKED_PM2 = b'#quests:personalMission/status/addBottomLocked/pm2'
    PERSONALMISSION_STATUS_ADDBOTTOMINFO_REGULAR = b'#quests:personalMission/status/addBottomInfo/regular'
    PERSONALMISSION_STATUS_ADDBOTTOMINFO_PM2 = b'#quests:personalMission/status/addBottomInfo/pm2'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_USSR = b'#quests:personalMission/status/addBottom/vehicleType/Alliance-USSR'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_GERMANY = b'#quests:personalMission/status/addBottom/vehicleType/Alliance-Germany'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_USA = b'#quests:personalMission/status/addBottom/vehicleType/Alliance-USA'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_FRANCE = b'#quests:personalMission/status/addBottom/vehicleType/Alliance-France'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_LIGHTTANK = b'#quests:personalMission/status/addBottom/vehicleType/lightTank'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_MEDIUMTANK = b'#quests:personalMission/status/addBottom/vehicleType/mediumTank'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_HEAVYTANK = b'#quests:personalMission/status/addBottom/vehicleType/heavyTank'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_AT_SPG = b'#quests:personalMission/status/addBottom/vehicleType/AT-SPG'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_SPG = b'#quests:personalMission/status/addBottom/vehicleType/SPG'
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ANY = b'#quests:personalMission/status/addBottom/vehicleType/any'
    PERSONALMISSION_STATUS_MISSIONDISABLED = b'#quests:personalMission/status/missionDisabled'
    PERSONALMISSION_STATUS_LOCKEDBYPREVMISSIONS = b'#quests:personalMission/status/lockedByPrevMissions'
    PERSONALMISSION_STATUS_LOCKEDBYPREVOPERATION = b'#quests:personalMission/status/lockedByPrevOperation'
    PERSONALMISSION_BOTTOMSTATUS_ALLAWARDSRECEIVED = b'#quests:personalMission/bottomStatus/allAwardsReceived'
    QUEST_CONDITION_DOT = b'#quests:quest/condition/dot'
    QUEST_CONDITION_OR = b'#quests:quest/condition/or'
    METRICS_STATE_DONE = b'#quests:metrics/state/done'
    METRICS_STATE_INPROGRESS = b'#quests:metrics/state/inProgress'
    METRICS_STATE_FAILED = b'#quests:metrics/state/failed'
    METRICS_TITLE_PROGRESS = b'#quests:metrics/title/progress'
    METRICS_TITLE_DONE = b'#quests:metrics/title/done'
    METRICS_TITLE_POSITION = b'#quests:metrics/title/position'
    METRICS_TITLE_LEFT = b'#quests:metrics/title/left'
    METRICS_TITLE_TRIESLEFT = b'#quests:metrics/title/triesLeft'
    METRICS_TITLE_TARGETS = b'#quests:metrics/title/targets'
    BATTLECONDITION_STATE_COMPLETED = b'#quests:battleCondition/state/completed'
    BATTLECONDITION_STATE_COMPLETED_PERFECTLY = b'#quests:battleCondition/state/completed_perfectly'
    BATTLECONDITION_STATE_IN_PROGRESS = b'#quests:battleCondition/state/in_progress'
    BATTLECONDITION_STATE_FAILED = b'#quests:battleCondition/state/failed'
    BATTLECONDITION_TASK_STATUS_DONE = b'#quests:battleCondition/task/status/done'
    BATTLECONDITION_TASK_STATUS_FAILED = b'#quests:battleCondition/task/status/failed'
    BATTLEPROGRESS_LIMITEDBYTIME = b'#quests:battleProgress/limitedByTime'
    BATTLEPROGRESS_POSITION_SHORT = b'#quests:battleProgress/position/short'
    BATTLEPROGRESS_POSITION_LEFT = b'#quests:battleProgress/position/left'
    BATTLEPROGRESS_POSITION_ADVANTAGE = b'#quests:battleProgress/position/advantage'
    BATTLEPROGRESS_DAMAGELEFT = b'#quests:battleProgress/damageLeft'
    BATTLEPROGRESS_KILLSLEFT = b'#quests:battleProgress/killsLeft'
    BATTLEPROGRESS_ALERTLABEL_TITLE = b'#quests:battleProgress/alertLabel/title'
    BATTLEPROGRESS_ALERTLABEL_REPAIRMODULES = b'#quests:battleProgress/alertLabel/repairModules'
    BATTLEPROGRESS_AFTERBATTLERESULT = b'#quests:battleProgress/afterBattleResult'
    QUEST_FLAG_STATUS_NOT_STARTED = b'#quests:quest/flag/status/not_started'
    QUEST_FLAG_STATUS_LOCKED = b'#quests:quest/flag/status/locked'
    QUEST_FLAG_STATUS_FAILED = b'#quests:quest/flag/status/failed'
    QUEST_FLAG_STATUS_COMPLETED = b'#quests:quest/flag/status/completed'
    QUEST_FLAG_STATUS_IN_PROGRESS = b'#quests:quest/flag/status/in_progress'
    QUEST_FLAG_STATUS_COMPLETED_PERFECTLY = b'#quests:quest/flag/status/completed_perfectly'
    PREMIUMQUESTS_BODY_TITLE = b'#quests:premiumQuests/body/title'
    PREMIUMQUESTS_BODY_DESCRIPTION = b'#quests:premiumQuests/body/description'
    PREMIUMQUESTS_BODY_BUTTONDETAILS = b'#quests:premiumQuests/body/buttonDetails'
    PREMIUMQUESTS_BODY_COMPLETE = b'#quests:premiumQuests/body/complete'
    PREMIUMQUESTS_QUESTS_PREM_ACC_Q01_TITLE = b'#quests:premiumQuests/quests/prem_acc_q01/title'
    PREMIUMQUESTS_QUESTS_PREM_ACC_Q02_TITLE = b'#quests:premiumQuests/quests/prem_acc_q02/title'
    PREMIUMQUESTS_QUESTS_PREM_ACC_Q03_TITLE = b'#quests:premiumQuests/quests/prem_acc_q03/title'
    PREMIUMQUESTS_DETAILEDQUESTS_REQUIREMENTS_PREMIUMACCOUNT = b'#quests:premiumQuests/detailedQuests/requirements/premiumAccount'
    PREMIUMQUESTS_DETAILEDQUESTS_REQUIREMENTS_TOKEN = b'#quests:premiumQuests/detailedQuests/requirements/token'
    PREMIUMQUESTS_CONDITION_DMGTOP_5 = b'#quests:premiumQuests/condition/dmgTop_5'
    PREMIUMQUESTS_CONDITION_WIN_WINLONG = b'#quests:premiumQuests/condition/win/winLong'
    DAILYQUESTS_HEADER_DEFAULT = b'#quests:dailyQuests/header/default'
    PREMIUMQUESTS_HEADER_DEFAULT = b'#quests:premiumQuests/header/default'
    WEEKLYQUEST_HEADER_DEFAULT = b'#quests:weeklyQuest/header/default'
    WEEKLYQUEST_DESCRIPTION_DEFAULT = b'#quests:weeklyQuest/description/default'
    DAILYQUESTS_HEADER_WINBACK = b'#quests:dailyQuests/header/winback'
    PREMIUMQUESTS_HEADER_WINBACK = b'#quests:premiumQuests/header/winback'
    DAILYQUESTS_TAB_LABEL = b'#quests:dailyQuests/tab/label'
    PREMIUMQUESTS_TAB_LABEL = b'#quests:premiumQuests/tab/label'
    DAILYQUESTS_TAB_DISABLED_TITLE = b'#quests:dailyQuests/tab/disabled/title'
    PREMIUMQUESTS_TAB_DISABLED_TITLE = b'#quests:premiumQuests/tab/disabled/title'
    DAILYQUESTS_TAB_DISABLED_REASON = b'#quests:dailyQuests/tab/disabled/reason'
    PREMIUMQUESTS_TAB_DISABLED_NOPREM = b'#quests:premiumQuests/tab/disabled/noPrem'
    DAILYQUESTS_TAB_COMPLETED = b'#quests:dailyQuests/tab/completed'
    DAILYQUESTS_TAB_PROGRESS = b'#quests:dailyQuests/tab/progress'
    DAILYQUESTS_TAB_BULL = b'#quests:dailyQuests/tab/bull'
    DAILYQUESTS_TAB_HIDDENBATTLETYPES = b'#quests:dailyQuests/tab/hiddenBattleTypes'
    DAILYQUESTS_TAB_CATHEGORY_TOOLTIP_DAILY_HEADER = b'#quests:dailyQuests/tab/cathegory/tooltip/daily/header'
    DAILYQUESTS_TAB_CATHEGORY_TOOLTIP_DAILY_BODY = b'#quests:dailyQuests/tab/cathegory/tooltip/daily/body'
    DAILYQUESTS_BODY_REROLL = b'#quests:dailyQuests/body/reroll'
    DAILYQUESTS_MISSIONSWITCH_TOOLTIP_HEADER = b'#quests:dailyQuests/missionSwitch/tooltip/header'
    DAILYQUESTS_MISSIONSWITCH_TOOLTIP_BODY_AVAILABLE = b'#quests:dailyQuests/missionSwitch/tooltip/body/available'
    DAILYQUESTS_MISSIONSWITCH_TOOLTIP_BODY_DESC_HRS = b'#quests:dailyQuests/missionSwitch/tooltip/body/desc_hrs'
    DAILYQUESTS_MISSIONSWITCH_TOOLTIP_BODY_DESC_HRS_MIN = b'#quests:dailyQuests/missionSwitch/tooltip/body/desc_hrs_min'
    DAILYQUESTS_MISSIONSWITCH_TOOLTIP_BODY_DESC_MIN_ONLY = b'#quests:dailyQuests/missionSwitch/tooltip/body/desc_min_only'
    DAILYQUESTS_MISSIONSWITCH_TOOLTIP_BODY_DESC = b'#quests:dailyQuests/missionSwitch/tooltip/body/desc'
    PREMIUMQUESTS_TOOLTIPS_LOCKED_HEADER = b'#quests:premiumQuests/tooltips/locked/header'
    PREMIUMQUESTS_TOOLTIPS_LOCKED_BODY = b'#quests:premiumQuests/tooltips/locked/body'
    PREMIUMQUESTS_NOTPREMIUMACCOUNT_TITLE = b'#quests:premiumQuests/notPremiumAccount/title'
    PREMIUMQUESTS_NOTPREMIUMACCOUNT_PARAGRAPH = b'#quests:premiumQuests/notPremiumAccount/paragraph'
    PREMIUMQUESTS_NOTPREMIUMACCOUNT_PARAGRAPHSMALL = b'#quests:premiumQuests/notPremiumAccount/paragraphSmall'
    PREMIUMQUESTS_NOTPREMIUMACCOUNT_BUTTON = b'#quests:premiumQuests/notPremiumAccount/button'
    PREMIUMQUESTS_COUNTDOWN_TITLE = b'#quests:premiumQuests/countDown/title'
    PREMIUMQUESTS_COUNTDOWN_REMAININGTEXT = b'#quests:premiumQuests/countDown/remainingText'
    DAILYQUESTS_COUNTDOWN_TITLE = b'#quests:dailyQuests/countDown/title'
    DAILYQUESTS_LOCKED_TITLE = b'#quests:dailyQuests/locked/title'
    DAILYQUESTS_COMPLETED_TITLE = b'#quests:dailyQuests/completed/title'
    EPICQUEST_COUNTDOWN_REMAININGTEXT = b'#quests:epicQuest/countDown/remainingText'
    DAILYQUESTS_COUNTDOWN_REMAININGTEXT = b'#quests:dailyQuests/countDown/remainingText'
    DAILYQUESTS_FOOTER_TITLE = b'#quests:dailyQuests/footer/title'
    DAILYQUESTS_FOOTER_PARAGRAPH = b'#quests:dailyQuests/footer/paragraph'
    DAILYQUESTS_BONUS_TOOLTIPTITLE = b'#quests:dailyQuests/bonus/tooltipTitle'
    DAILYQUESTS_BONUS_TOOLTIPDESCRIPTION = b'#quests:dailyQuests/bonus/tooltipDescription'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_EASY = b'#quests:dailyQuests/postBattle/genericTitle_easy'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_MEDIUM = b'#quests:dailyQuests/postBattle/genericTitle_medium'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_HARD = b'#quests:dailyQuests/postBattle/genericTitle_hard'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_EASY_SUBS = b'#quests:dailyQuests/postBattle/genericTitle_easy_subs'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_MEDIUM_SUBS = b'#quests:dailyQuests/postBattle/genericTitle_medium_subs'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_HARD_SUBS = b'#quests:dailyQuests/postBattle/genericTitle_hard_subs'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_BONUS_SUBS = b'#quests:dailyQuests/postBattle/genericTitle_bonus_subs'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_BONUS = b'#quests:dailyQuests/postBattle/genericTitle_bonus'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_EPIC = b'#quests:dailyQuests/postBattle/genericTitle_epic'
    DAILYQUESTS_POSTBATTLE_EPIC_CONDITION_PROGRESS = b'#quests:dailyQuests/postBattle/epic_condition_progress'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_EASY_PREMIUM = b'#quests:dailyQuests/postBattle/genericTitle_easy_premium'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_MEDIUM_PREMIUM = b'#quests:dailyQuests/postBattle/genericTitle_medium_premium'
    DAILYQUESTS_POSTBATTLE_GENERICTITLE_HARD_PREMIUM = b'#quests:dailyQuests/postBattle/genericTitle_hard_premium'
    DAILYQUESTS_BONUSQUEST_BONUSMISSIONTITLE = b'#quests:dailyQuests/bonusQuest/bonusMissionTitle'
    DAILYQUESTS_BONUSQUEST_COUNTDOWN_HRS = b'#quests:dailyQuests/bonusQuest/countDown_hrs'
    DAILYQUESTS_BONUSQUEST_COUNTDOWN_MINSEC = b'#quests:dailyQuests/bonusQuest/countDown_minSec'
    PREMIUMQUESTS_POSTBATTLE_GENERICTITLE_EASY = b'#quests:premiumQuests/postBattle/genericTitle_easy'
    PREMIUMQUESTS_POSTBATTLE_GENERICTITLE_MEDIUM = b'#quests:premiumQuests/postBattle/genericTitle_medium'
    PREMIUMQUESTS_POSTBATTLE_GENERICTITLE_HARD = b'#quests:premiumQuests/postBattle/genericTitle_hard'
    GENERAL_COUNTDOWN_TEXT_TIMER_HRS = b'#quests:general/countdown/text/timer_hrs'
    GENERAL_COUNTDOWN_TEXT_TIMER_HRS_ONLY = b'#quests:general/countdown/text/timer_hrs_only'
    GENERAL_COUNTDOWN_TEXT_TIMER_MIN_ONLY = b'#quests:general/countdown/text/timer_min_only'
    GENERAL_COUNTDOWN_TEXT_TIMER_MIN = b'#quests:general/countdown/text/timer_min'
    GENERAL_COUNTDOWN_TEXT_TIMER_SEC = b'#quests:general/countdown/text/timer_sec'
    GENERAL_COUNTDOWN_TIMER_HRS = b'#quests:general/countdown/timer_hrs'
    GENERAL_COUNTDOWN_TIMER_HRS_ONLY = b'#quests:general/countdown/timer_hrs_only'
    GENERAL_COUNTDOWN_TIMER_MIN_ONLY = b'#quests:general/countdown/timer_min_only'
    GENERAL_COUNTDOWN_TIMER_MIN = b'#quests:general/countdown/timer_min'
    GENERAL_COUNTDOWN_TIMER_SEC = b'#quests:general/countdown/timer_sec'
    DAILYQUESTS_POSTBATTLE_GENERICAMPERSAND = b'#quests:dailyQuests/postBattle/genericAmpersand'
    DAILYQUESTS_POSTBATTLE_AND = b'#quests:dailyQuests/postBattle/and'
    DAILYQUESTS_TAKEREWARDSBUTTON_TEXT = b'#quests:dailyQuests/takeRewardsButton/text'
    DAILYQUESTS_TAKEREWARDSBUTTON_COUNTDOWN = b'#quests:dailyQuests/takeRewardsButton/countdown'
    DAILYQUESTS_TAKEREWARDSBUTTON_TOOLTIP = b'#quests:dailyQuests/takeRewardsButton/tooltip'
    DAILYQUESTS_TAKEREWARDSBUTTON_TOOLTIPDISABLE = b'#quests:dailyQuests/takeRewardsButton/tooltipDisable'
    WEEKLYQUEST_COUNTDOWN_TOOLTIP_HEADER = b'#quests:weeklyQuest/countDown/tooltip/header'
    WEEKLYQUEST_COUNTDOWN_TOOLTIP_BODY = b'#quests:weeklyQuest/countDown/tooltip/body'
    DAILYQUESTS_COUNTDOWN_TOOLTIP_HEADER = b'#quests:dailyQuests/countDown/tooltip/header'
    DAILYQUESTS_COUNTDOWN_TOOLTIP_BODY = b'#quests:dailyQuests/countDown/tooltip/body'
    DAILYQUESTS_PREMIUM_LOCKED_TOOLTIP_HEADER = b'#quests:dailyQuests/premium/locked/tooltip/header'
    DAILYQUESTS_PREMIUM_LOCKED_TOOLTIP_BODY = b'#quests:dailyQuests/premium/locked/tooltip/body'
    DAILYQUESTS_BONUS_LOCKED_TOOLTIP_HEADER = b'#quests:dailyQuests/bonus/locked/tooltip/header'
    DAILYQUESTS_BONUS_LOCKED_TOOLTIP_BODY = b'#quests:dailyQuests/bonus/locked/tooltip/body'
    INFOPAGE_HEADER_DEFAULT = b'#quests:infoPage/header/default'
    INFOPAGE_HEADER_WINBACK = b'#quests:infoPage/header/winback'
    INFOPAGE_INFOBUTTON_DEFAULT = b'#quests:infoPage/infoButton/default'
    INFOPAGE_INFOBUTTON_WINBACK = b'#quests:infoPage/infoButton/winback'
    INFOPAGE_INFOBUTTON_BACK_TITLE = b'#quests:infoPage/infoButton/back/title'
    INFOPAGE_INFOBUTTON_BACK_GOTO = b'#quests:infoPage/infoButton/back/goto'
    INFOPAGE_INFOBUTTONTOOLTIP_BODY = b'#quests:infoPage/infoButtonTooltip/body'
    INFOPAGE_INFOBUTTONTOOLTIP_HEADER_DEFAULT = b'#quests:infoPage/infoButtonTooltip/header/default'
    INFOPAGE_INFOBUTTONTOOLTIP_HEADER_WINBACK = b'#quests:infoPage/infoButtonTooltip/header/winback'
    INFOPAGE_DAILYMISSIONTITLE = b'#quests:infoPage/dailyMissionTitle'
    INFOPAGE_PREMIUMMISSIONSTITLE = b'#quests:infoPage/premiumMissionsTitle'
    INFOPAGE_DAILYMISSIONS_DEFAULT = b'#quests:infoPage/dailyMissions/default'
    INFOPAGE_DAILYMISSIONS_SUBSCRIPTION_DEFAULT = b'#quests:infoPage/dailyMissions/subscription/default'
    INFOPAGE_DAILYMISSIONS_BATTLEPASSDAILYMISSIONS_DEFAULT = b'#quests:infoPage/dailyMissions/battlePassDailyMissions/default'
    INFOPAGE_DAILYMISSIONS_WINBACK = b'#quests:infoPage/dailyMissions/winback'
    INFOPAGE_DAILYMISSIONS_BATTLEPASSDAILYMISSIONS_WINBACK = b'#quests:infoPage/dailyMissions/battlePassDailyMissions/winback'
    INFOPAGE_PREMIUMMISSIONS_DEFAULT = b'#quests:infoPage/premiumMissions/default'
    INFOPAGE_PREMIUMMISSIONS_WINBACK = b'#quests:infoPage/premiumMissions/winback'
    INFOPAGE_PREMIUMMISSIONS_WINBACK_COMP7ACTIVE = b'#quests:infoPage/premiumMissions/winback_comp7Active'
    INFOPAGE_CONDITIONSTITLE = b'#quests:infoPage/conditionsTitle'
    INFOPAGE_CONDITIONS_DEFAULT = b'#quests:infoPage/conditions/default'
    INFOPAGE_CONDITIONS_WINBACK = b'#quests:infoPage/conditions/winback'
    INFOPAGE_CONDITIONS_WINBACK_COMP7ACTIVE = b'#quests:infoPage/conditions/winback_comp7Active'
    INFOPAGE_BONUSMISSIONTITLE = b'#quests:infoPage/bonusMissionTitle'
    INFOPAGE_BONUSMISSION_DEFAULT = b'#quests:infoPage/bonusMission/default'
    INFOPAGE_BONUSMISSION_WINBACK = b'#quests:infoPage/bonusMission/winback'
    INFOPAGE_EPICREWARDSTITLE = b'#quests:infoPage/epicRewardsTitle'
    INFOPAGE_EPICREWARDS_DEFAULT = b'#quests:infoPage/epicRewards/default'
    INFOPAGE_EPICREWARDS_WINBACK = b'#quests:infoPage/epicRewards/winback'
    INFOPAGE_MISSIONSWITCHTITLE = b'#quests:infoPage/missionSwitchTitle'
    INFOPAGE_MISSIONSWITCH_HRS = b'#quests:infoPage/missionSwitch_hrs'
    INFOPAGE_MISSIONSWITCH_MIN = b'#quests:infoPage/missionSwitch_min'
    INFOPAGE_MISSIONSWITCH_WINBACK = b'#quests:infoPage/missionSwitch/winback'
    DAILYQUESTS_CONDITION_DODAMAGE = b'#quests:dailyQuests/condition/doDamage'
    DAILYQUESTS_CONDITION_EARNEXP = b'#quests:dailyQuests/condition/earnExp'
    DAILYQUESTS_CONDITION_DESTROYMODULE_FEW = b'#quests:dailyQuests/condition/destroyModule_few'
    DAILYQUESTS_CONDITION_DESTROYMODULE_PLURAL = b'#quests:dailyQuests/condition/destroyModule_plural'
    DAILYQUESTS_CONDITION_DESTROYVEH_SINGULAR = b'#quests:dailyQuests/condition/destroyVeh_singular'
    DAILYQUESTS_CONDITION_DESTROYVEH_FEW = b'#quests:dailyQuests/condition/destroyVeh_few'
    DAILYQUESTS_CONDITION_DESTROYVEH_PLURAL = b'#quests:dailyQuests/condition/destroyVeh_plural'
    DAILYQUESTS_CONDITION_DODAMAGEVEH = b'#quests:dailyQuests/condition/doDamageVeh'
    DAILYQUESTS_CONDITION_EXPTOP = b'#quests:dailyQuests/condition/expTop'
    DAILYQUESTS_CONDITION_EXPTOP_FIRST = b'#quests:dailyQuests/condition/expTop_first'
    DAILYQUESTS_CONDITION_DMGTOP = b'#quests:dailyQuests/condition/dmgTop'
    DAILYQUESTS_CONDITION_DMGTOP_FIRST = b'#quests:dailyQuests/condition/dmgTop_first'
    DAILYQUESTS_CONDITION_SPOTVEH_FEW = b'#quests:dailyQuests/condition/spotVeh_few'
    DAILYQUESTS_CONDITION_WINBATTLE = b'#quests:dailyQuests/condition/winBattle'
    DAILYQUESTS_CONDITION_WINBATTLE_ACCUM = b'#quests:dailyQuests/condition/winBattle_accum'
    DAILYQUESTS_CONDITION_DODAMAGE_ACCUM = b'#quests:dailyQuests/condition/doDamage_accum'
    DAILYQUESTS_CONDITION_EARNEXP_ACCUM = b'#quests:dailyQuests/condition/earnExp_accum'
    DAILYQUESTS_CONDITION_DESTROYMODULE_FEW_ACCUM = b'#quests:dailyQuests/condition/destroyModule_few_accum'
    DAILYQUESTS_CONDITION_DESTROYMODULE_PLURAL_ACCUM = b'#quests:dailyQuests/condition/destroyModule_plural_accum'
    DAILYQUESTS_CONDITION_DODAMAGEVEH_ACCUM = b'#quests:dailyQuests/condition/doDamageVeh_accum'
    DAILYQUESTS_CONDITION_DESTROYVEH_FEW_ACCUM = b'#quests:dailyQuests/condition/destroyVeh_few_accum'
    DAILYQUESTS_CONDITION_DESTROYVEH_PLURAL_ACCUM = b'#quests:dailyQuests/condition/destroyVeh_plural_accum'
    DAILYQUESTS_CONDITION_SPOTVEH_FEW_ACCUM = b'#quests:dailyQuests/condition/spotVeh_few_accum'
    DETAILS_CONDITIONS_CUMULATIVE_DAMAGEDHP = b'#quests:details/conditions/cumulative/damagedHp'
    DETAILS_CONDITIONS_CUMULATIVE_COMP7PRESTIGEPOINTS = b'#quests:details/conditions/cumulative/comp7PrestigePoints'
    DEBUTBOXES_MISSIONS_HEADER_CAPTION1 = b'#quests:debutBoxes/missions/header/caption1'
    DEBUTBOXES_MISSIONS_HEADER_CAPTION2 = b'#quests:debutBoxes/missions/header/caption2'
    DEBUTBOXES_MISSIONS_HEADER_CAPTION3 = b'#quests:debutBoxes/missions/header/caption3'
    DEBUTBOXES_MISSIONS_HEADER_DISABLED = b'#quests:debutBoxes/missions/header/disabled'
    DEBUTBOXES_MISSIONS_HEADER_INFO = b'#quests:debutBoxes/missions/header/info'
    SUMMERSALE_MISSIONS_HEADER_CAPTION1 = b'#quests:summerSale/missions/header/caption1'
    SUMMERSALE_MISSIONS_HEADER_CAPTION2 = b'#quests:summerSale/missions/header/caption2'
    SUMMERSALE_MISSIONS_HEADER_CAPTION3 = b'#quests:summerSale/missions/header/caption3'
    SUMMERSALE_MISSIONS_HEADER_DISABLED = b'#quests:summerSale/missions/header/disabled'
    SUMMERSALE_MISSIONS_HEADER_INFO = b'#quests:summerSale/missions/header/info'
    SUMMERSALE_MISSIONS_HEADER_BUTTON_GOTOSHOP = b'#quests:summerSale/missions/header/button/gotoShop'
    SUMMERSALE_MISSIONS_HEADER_BUTTON_GOTOEVENT = b'#quests:summerSale/missions/header/button/gotoEvent'
    WEEKLYQUEST_REWARDSCREEN_HEADER = b'#quests:weeklyQuest/rewardScreen/header'
    WEEKLYQUEST_REWARDSCREEN_SUBHEADER = b'#quests:weeklyQuest/rewardScreen/subheader'
    WEEKLYQUEST_REWARDSCREEN_CLOSE = b'#quests:weeklyQuest/rewardScreen/close'
    WEEKLYQUEST_REWARDSCREEN_CONFIRM = b'#quests:weeklyQuest/rewardScreen/confirm'
    DAILYWIDGET_PROGRESS = b'#quests:dailyWidget/progress'
    DAILYWIDGET_TOOLTIP_HEADER_DAILY = b'#quests:dailyWidget/tooltip/header/daily'
    DAILYWIDGET_TOOLTIP_HEADER_PREMIUM = b'#quests:dailyWidget/tooltip/header/premium'
    DAILYWIDGET_TOOLTIP_HEADER_BONUS = b'#quests:dailyWidget/tooltip/header/bonus'
    DAILYWIDGET_TOOLTIP_HEADER_EPIC = b'#quests:dailyWidget/tooltip/header/epic'
    DAILYWIDGET_TOOLTIP_TIMER = b'#quests:dailyWidget/tooltip/timer'
    DAILYWIDGET_TOOLTIP_HIDEQUESTS = b'#quests:dailyWidget/tooltip/hideQuests'
    DAILYWIDGET_TOOLTIP_COMPLETED = b'#quests:dailyWidget/tooltip/completed'
    DAILYWIDGET_TOOLTIP_NOTAVAILABLE_HEADER = b'#quests:dailyWidget/tooltip/notAvailable/header'
    DAILYWIDGET_TOOLTIP_NOTAVAILABLE_DESCRIPTION = b'#quests:dailyWidget/tooltip/notAvailable/description'
    DAILYWIDGET_TOOLTIP_HIDDENREWARDS = b'#quests:dailyWidget/tooltip/hiddenRewards'
    INTROSCREEN_TITLE = b'#quests:introScreen/title'
    INTROSCREEN_SUBTITLE = b'#quests:introScreen/subtitle'
    INTROSCREEN_SUBTITLEDAILYQUESTSONLY = b'#quests:introScreen/subtitleDailyQuestsOnly'
    INTROSCREEN_DAILYQUESTS_HEADER = b'#quests:introScreen/dailyQuests/header'
    INTROSCREEN_DAILYQUESTS_DESCRIPTION = b'#quests:introScreen/dailyQuests/description'
    INTROSCREEN_CONFIRM = b'#quests:introScreen/confirm'
    INTROSCREEN_CLOSE = b'#quests:introScreen/close'
    DAILYREROLL_TITLE = b'#quests:dailyReroll/title'
    DAILYREROLL_SUBTITLE = b'#quests:dailyReroll/subtitle'
    DAILYREROLL_SUBTITLEPREMIUM = b'#quests:dailyReroll/subtitlePremium'
    DAILYREROLL_SUBTITLE_ALERT = b'#quests:dailyReroll/subtitle_alert'
    DAILYREROLL_CONDITION = b'#quests:dailyReroll/condition'
    DAILYREROLL_REPLACE = b'#quests:dailyReroll/replace'
    DAILYREROLL_CANCEL = b'#quests:dailyReroll/cancel'
    DAILYREROLL_CLOSE = b'#quests:dailyReroll/close'
    DAILYREROLL_TOOLTIP_USUAL = b'#quests:dailyReroll/tooltip/usual'
    DAILYREROLL_TOOLTIP_PREMIUM = b'#quests:dailyReroll/tooltip/premium'
    DAILYREROLL_TOOLTIP_HEADER_TITLE = b'#quests:dailyReroll/tooltip/header/title'
    DAILYREROLL_TOOLTIP_HEADER_NOACCESS = b'#quests:dailyReroll/tooltip/header/noAccess'
    DAILYREROLL_TOOLTIP_BODY_AVAILABLE = b'#quests:dailyReroll/tooltip/body/available'
    DAILYREROLL_TOOLTIP_BODY_TIMEUPDATE = b'#quests:dailyReroll/tooltip/body/timeUpdate'
    DAILYREROLL_TOOLTIP_BODY_TIMETEXT = b'#quests:dailyReroll/tooltip/body/timeText'
    DAILYREROLL_TOOLTIP_BODY_CANTREROLL = b'#quests:dailyReroll/tooltip/body/cantReroll'
    DAILYREROLL_TOOLTIP_BODY_AFTERUPDATE = b'#quests:dailyReroll/tooltip/body/afterUpdate'
    DAILYREROLL_TOOLTIP_BODY_AFTERUPDATEPREMIUM = b'#quests:dailyReroll/tooltip/body/afterUpdatePremium'
    REWARD_TOOLTIP_ADDITIONREWARD = b'#quests:reward/tooltip/additionReward'
    REWARD_TOOLTIP_NOADDITIONREWARD = b'#quests:reward/tooltip/noAdditionReward'
    REWARD_TOOLTIP_SIMPLEBODY = b'#quests:reward/tooltip/simpleBody'
    REWARD_TOOLTIP_TITLE = b'#quests:reward/tooltip/title'
    REWARD_TOOLTIP_CUSTOMBODY = b'#quests:reward/tooltip/customBody'
    DAILYREROLL_TOOLTIP_BODY_ISENABLEDREROLL = b'#quests:dailyReroll/tooltip/body/isEnabledReroll'
    MODESELECTOR_TOOLTIP_TITLE = b'#quests:modeSelector/tooltip/title'
    MODESELECTOR_TOOLTIP_TEXT = b'#quests:modeSelector/tooltip/text'
    SWITCH_ISDAILYPREMENABLED = b'#quests:switch/isDailyPremEnabled'
    SWITCH_ISDAILYREGULARENABLED = b'#quests:switch/isDailyRegularEnabled'
    SWITCH_ISWEEKLYENABLED = b'#quests:switch/isWeeklyEnabled'
    SWITCH_ISWEEKLYENABLEDTITLE = b'#quests:switch/isWeeklyEnabledTitle'
    BONUSNAME_GOLDENTICKET = b'#quests:bonusName/goldenticket'
    TOKEN_DEFAULT_ENUM = (
     TOKEN_DEFAULT_USSR,
     TOKEN_DEFAULT_GERMANY,
     TOKEN_DEFAULT_USA,
     TOKEN_DEFAULT_FRANCE,
     TOKEN_DEFAULT_UK,
     TOKEN_DEFAULT_CZECH,
     TOKEN_DEFAULT_CHINA,
     TOKEN_DEFAULT_JAPAN,
     TOKEN_DEFAULT_POLAND,
     TOKEN_DEFAULT_SWEDEN,
     TOKEN_DEFAULT_ITALY,
     TOKEN_DEFAULT_INTUNION,
     TOKEN_DEFAULT_WOT,
     TOKEN_DEFAULT_DEFAULT,
     TOKEN_DEFAULT_LIGHTTANK,
     TOKEN_DEFAULT_MEDIUMTANK,
     TOKEN_DEFAULT_HEAVYTANK,
     TOKEN_DEFAULT_AT_SPG,
     TOKEN_DEFAULT_SPG,
     TOKEN_DEFAULT_SHELL,
     TOKEN_DEFAULT_RICOCHET,
     TOKEN_DEFAULT_PENETRATION,
     TOKEN_DEFAULT_AIM,
     TOKEN_DEFAULT_FIRE,
     TOKEN_DEFAULT_TURRET,
     TOKEN_DEFAULT_TRACK,
     TOKEN_DEFAULT_FOLDER,
     TOKEN_DEFAULT_LEAFLET,
     TOKEN_DEFAULT_WHEEL,
     TOKEN_DEFAULT_BOX,
     TOKEN_DEFAULT_TANKREWARDS,
     TOKEN_DEFAULT_BATTLE_ROYALE,
     TOKEN_DEFAULT_VERSUS_AI_REGULAR,
     TOKEN_DEFAULT_VERSUS_AI_WINBACK)
    BONUSNAME_ENUM = (
     BONUSNAME_BLUEPRINTS_ANY,
     BONUSNAME_BLUEPRINTS_VEHICLE,
     BONUSNAME_BLUEPRINTS_VEHICLE_ANY,
     BONUSNAME_BLUEPRINTS_NATION,
     BONUSNAME_BLUEPRINTS_NATION_ANY,
     BONUSNAME_BLUEPRINTS_UNIVERSAL,
     BONUSNAME_PARAGONSUNLOCKS,
     BONUSNAME_TMANTOKEN,
     BONUSNAME_STYLEPROGRESS,
     BONUSNAME_CREDITS,
     BONUSNAME_GOLD,
     BONUSNAME_CRYSTAL,
     BONUSNAME_EVENTCOIN,
     BONUSNAME_BPCOIN,
     BONUSNAME_EQUIPCOIN,
     BONUSNAME_XP,
     BONUSNAME_FREEXP,
     BONUSNAME_TANKMENXP,
     BONUSNAME_XPFACTOR,
     BONUSNAME_CREDITSFACTOR,
     BONUSNAME_FREEXPFACTOR,
     BONUSNAME_TANKMENXPFACTOR,
     BONUSNAME_DAILYXPFACTOR,
     BONUSNAME_SLOTS,
     BONUSNAME_BERTHS,
     BONUSNAME_PREMIUM,
     BONUSNAME_PREMIUM_PLUS,
     BONUSNAME_TANKMEN_WITH_SKILLS,
     BONUSNAME_TANKMEN_NO_SKILLS,
     BONUSNAME_CAMOUFLAGE,
     BONUSNAME_EMBLEM,
     BONUSNAME_INSCRIPTION,
     BONUSNAME_DECAL,
     BONUSNAME_PAINT,
     BONUSNAME_STYLE,
     BONUSNAME_MODIFICATION,
     BONUSNAME_FREETOKENS,
     BONUSNAME_COMPLETIONTOKENS,
     BONUSNAME_COMPLETIONTOKENS_1_1,
     BONUSNAME_COMPLETIONTOKENS_1_2,
     BONUSNAME_COMPLETIONTOKENS_1_3,
     BONUSNAME_COMPLETIONTOKENS_1_4,
     BONUSNAME_COMPLETIONTOKENS_1_5,
     BONUSNAME_COMPLETIONTOKENS_2_1,
     BONUSNAME_COMPLETIONTOKENS_2_2,
     BONUSNAME_COMPLETIONTOKENS_2_3,
     BONUSNAME_COMPLETIONTOKENS_2_4,
     BONUSNAME_COMPLETIONTOKENS_2_5,
     BONUSNAME_COMPLETIONTOKENS_3_1,
     BONUSNAME_COMPLETIONTOKENS_3_2,
     BONUSNAME_COMPLETIONTOKENS_3_3,
     BONUSNAME_COMPLETIONTOKENS_3_4,
     BONUSNAME_COMPLETIONTOKENS_3_5,
     BONUSNAME_COMPLETIONTOKENS_4_1,
     BONUSNAME_COMPLETIONTOKENS_4_2,
     BONUSNAME_COMPLETIONTOKENS_4_3,
     BONUSNAME_COMPLETIONTOKENS_4_4,
     BONUSNAME_COMPLETIONTOKENS_4_5,
     BONUSNAME_COMPLETIONTOKENS_5_1,
     BONUSNAME_COMPLETIONTOKENS_5_2,
     BONUSNAME_COMPLETIONTOKENS_5_3,
     BONUSNAME_COMPLETIONTOKENS_5_4,
     BONUSNAME_COMPLETIONTOKENS_6_1,
     BONUSNAME_COMPLETIONTOKENS_6_2,
     BONUSNAME_COMPLETIONTOKENS_6_3,
     BONUSNAME_COMPLETIONTOKENS_6_4,
     BONUSNAME_COMPLETIONTOKENS_7_1,
     BONUSNAME_COMPLETIONTOKENS_7_2,
     BONUSNAME_COMPLETIONTOKENS_7_3,
     BONUSNAME_COMPLETIONTOKENS_7_4,
     BONUSNAME_PROJECTIONDECAL,
     BONUSNAME_PERSONALNUMBER,
     BONUSNAME_RANKEDDAILYBATTLES,
     BONUSNAME_RANKEDBONUSBATTLES,
     BONUSNAME_ENTITLEMENTS_TESTENTITLEMENT,
     BONUSNAME_ENTITLEMENTS_RANKED_2020_DISCOUNT,
     BONUSNAME_ENTITLEMENTS_RANKED_202203_ACCESS,
     BONUSNAME_ENTITLEMENTS_PARAGON_REWARDS_CHOICE_V_11,
     BONUSNAME_ENTITLEMENTS_SHEVENTS_CLAN_COUPON,
     BONUSNAME_ENTITLEMENTS_SHEVENTS_CLAN_CHEVRON,
     BONUSNAME_BATTLE_BONUS_X5,
     BONUSNAME_CREW_BONUS_X3,
     BONUSNAME_BATTLEPASSPOINTS,
     BONUSNAME_BATTLEPASSPOINTS_PREVIEW,
     BONUSNAME_BRCOIN,
     BONUSNAME_GOLD_BANK,
     BONUSNAME_IDLE_CREW_XP,
     BONUSNAME_EXCLUDED_MAP,
     BONUSNAME_FREE_EQUIPMENT_DEMOUNTING,
     BONUSNAME_EXCLUSIVE_VEHICLE,
     BONUSNAME_ATTENDANCE_REWARD,
     BONUSNAME_TEAM_CREDITS_BONUS,
     BONUSNAME_DAILY_QUESTS_REWARDS,
     BONUSNAME_CLAN_SEASON_PROGRESS,
     BONUSNAME_BUMBLEBEE_COIN,
     BONUSNAME_HONEY_COIN,
     BONUSNAME_REWARDSSLOTS,
     BONUSNAME_GOLDENTICKET)
    ACTION_ENUM = (
     ACTION_AUTO_CALENDAR,
     ACTION_FULL_CALENDAR,
     ACTION_HERO_FULL_CALENDAR,
     ACTION_BUTTON_CALENDAR,
     ACTION_SHORT_CALENDAR,
     ACTION_SUBHEADER_CALENDAR,
     ACTION_AUTO_EXCHANGERATE,
     ACTION_FULL_EXCHANGERATE,
     ACTION_HERO_FULL_EXCHANGERATE,
     ACTION_SHORT_EXCHANGERATE,
     ACTION_BUTTON_EXCHANGERATE,
     ACTION_AUTO_PAIDREMOVALCOST,
     ACTION_FULL_PAIDREMOVALCOST,
     ACTION_HERO_FULL_PAIDREMOVALCOST,
     ACTION_SHORT_PAIDREMOVALCOST,
     ACTION_BUTTON_PAIDREMOVALCOST,
     ACTION_AUTO_CHANGEROLECOST,
     ACTION_FULL_CHANGEROLECOST,
     ACTION_HERO_FULL_CHANGEROLECOST,
     ACTION_SHORT_CHANGEROLECOST,
     ACTION_BUTTON_CHANGEROLECOST,
     ACTION_AUTO_FREEXPCONVERSIONDISCRECITY,
     ACTION_FULL_FREEXPCONVERSIONDISCRECITY,
     ACTION_HERO_FULL_FREEXPCONVERSIONDISCRECITY,
     ACTION_SHORT_FREEXPCONVERSIONDISCRECITY,
     ACTION_BUTTON_FREEXPCONVERSIONDISCRECITY,
     ACTION_AUTO_SLOTSPRICES,
     ACTION_FULL_SLOTSPRICES,
     ACTION_HERO_FULL_SLOTSPRICES,
     ACTION_SHORT_SLOTSPRICES,
     ACTION_BUTTON_SLOTSPRICES,
     ACTION_AUTO_BERTHSPRICES,
     ACTION_FULL_BERTHSPRICES,
     ACTION_HERO_FULL_BERTHSPRICES,
     ACTION_SHORT_BERTHSPRICES,
     ACTION_BUTTON_BERTHSPRICES,
     ACTION_AUTO_CREDITSTANKMANCOST,
     ACTION_FULL_CREDITSTANKMANCOST,
     ACTION_HERO_FULL_CREDITSTANKMANCOST,
     ACTION_SHORT_CREDITSTANKMANCOST,
     ACTION_BUTTON_CREDITSTANKMANCOST,
     ACTION_AUTO_GOLDTANKMANCOST,
     ACTION_FULL_GOLDTANKMANCOST,
     ACTION_HERO_FULL_GOLDTANKMANCOST,
     ACTION_SHORT_GOLDTANKMANCOST,
     ACTION_BUTTON_GOLDTANKMANCOST,
     ACTION_AUTO_TANKMEN_MIXED,
     ACTION_FULL_TANKMEN_MIXED,
     ACTION_HERO_FULL_TANKMEN_MIXED,
     ACTION_SHORT_TANKMEN_MIXED,
     ACTION_BUTTON_TANKMEN_MIXED,
     ACTION_AUTO_CREDITSDROPSKILLSCOST,
     ACTION_FULL_CREDITSDROPSKILLSCOST,
     ACTION_HERO_FULL_CREDITSDROPSKILLSCOST,
     ACTION_SHORT_CREDITSDROPSKILLSCOST,
     ACTION_BUTTON_CREDITSDROPSKILLSCOST,
     ACTION_AUTO_GOLDDROPSKILLSCOST,
     ACTION_FULL_GOLDDROPSKILLSCOST,
     ACTION_HERO_FULL_GOLDDROPSKILLSCOST,
     ACTION_SHORT_GOLDDROPSKILLSCOST,
     ACTION_BUTTON_GOLDDROPSKILLSCOST,
     ACTION_AUTO_DROPSKILLS_MIXED,
     ACTION_FULL_DROPSKILLS_MIXED,
     ACTION_HERO_FULL_DROPSKILLS_MIXED,
     ACTION_SHORT_DROPSKILLS_MIXED,
     ACTION_BUTTON_DROPSKILLS_MIXED,
     ACTION_AUTO_PASSPORTCHANGECOST,
     ACTION_FULL_PASSPORTCHANGECOST,
     ACTION_HERO_FULL_PASSPORTCHANGECOST,
     ACTION_SHORT_PASSPORTCHANGECOST,
     ACTION_BUTTON_PASSPORTCHANGECOST,
     ACTION_AUTO_FEMALEPASSPORTCHANGECOST,
     ACTION_FULL_FEMALEPASSPORTCHANGECOST,
     ACTION_HERO_FULL_FEMALEPASSPORTCHANGECOST,
     ACTION_SHORT_FEMALEPASSPORTCHANGECOST,
     ACTION_BUTTON_FEMALEPASSPORTCHANGECOST,
     ACTION_AUTO_MUL_EQUIPMENTPRICEALL,
     ACTION_AUTO_EQUIPMENT_CREDITSPRICEMULTIPLIER,
     ACTION_SHORT_EQUIPMENT_CREDITSPRICEMULTIPLIER,
     ACTION_BUTTON_EQUIPMENT_CREDITSPRICEMULTIPLIER,
     ACTION_AUTO_EQUIPMENT_GOLDPRICEMULTIPLIER,
     ACTION_SHORT_EQUIPMENT_GOLDPRICEMULTIPLIER,
     ACTION_BUTTON_EQUIPMENT_GOLDPRICEMULTIPLIER,
     ACTION_AUTO_EQUIPMENT_MIXED,
     ACTION_SHORT_EQUIPMENT_MIXED,
     ACTION_BUTTON_EQUIPMENT_MIXED,
     ACTION_AUTO_SET_EQUIPMENTPRICE,
     ACTION_SHORT_SET_EQUIPMENTPRICE,
     ACTION_BUTTON_SET_EQUIPMENTPRICE,
     ACTION_AUTO_MUL_EQUIPMENTPRICE,
     ACTION_SHORT_MUL_EQUIPMENTPRICE,
     ACTION_BUTTON_MUL_EQUIPMENTPRICE,
     ACTION_AUTO_MUL_OPTIONALDEVICEPRICEALL,
     ACTION_SHORT_MUL_OPTIONALDEVICEPRICEALL,
     ACTION_BUTTON_MUL_OPTIONALDEVICEPRICEALL,
     ACTION_AUTO_SET_OPTIONALDEVICEPRICE,
     ACTION_SHORT_SET_OPTIONALDEVICEPRICE,
     ACTION_BUTTON_SET_OPTIONALDEVICEPRICE,
     ACTION_AUTO_MUL_OPTIONALDEVICEPRICE,
     ACTION_SHORT_MUL_OPTIONALDEVICEPRICE,
     ACTION_BUTTON_MUL_OPTIONALDEVICEPRICE,
     ACTION_AUTO_MUL_SHELLPRICEALL,
     ACTION_AUTO_SHELL_CREDITSPRICEMULTIPLIER,
     ACTION_FULL_SHELL_CREDITSPRICEMULTIPLIER,
     ACTION_HERO_FULL_SHELL_CREDITSPRICEMULTIPLIER,
     ACTION_SHORT_SHELL_CREDITSPRICEMULTIPLIER,
     ACTION_BUTTON_SHELL_CREDITSPRICEMULTIPLIER,
     ACTION_AUTO_SHELL_GOLDPRICEMULTIPLIER,
     ACTION_FULL_SHELL_GOLDPRICEMULTIPLIER,
     ACTION_HERO_FULL_SHELL_GOLDPRICEMULTIPLIER,
     ACTION_SHORT_SHELL_GOLDPRICEMULTIPLIER,
     ACTION_BUTTON_SHELL_GOLDPRICEMULTIPLIER,
     ACTION_AUTO_SHELL_MIXED,
     ACTION_FULL_SHELL_MIXED,
     ACTION_HERO_FULL_SHELL_MIXED,
     ACTION_SHORT_SHELL_MIXED,
     ACTION_BUTTON_SHELL_MIXED,
     ACTION_AUTO_MUL_SHELLPRICE,
     ACTION_FULL_MUL_SHELLPRICE,
     ACTION_HERO_FULL_MUL_SHELLPRICE,
     ACTION_SHORT_MUL_SHELLPRICE,
     ACTION_BUTTON_MUL_SHELLPRICE,
     ACTION_AUTO_SET_SHELLPRICE,
     ACTION_FULL_SET_SHELLPRICE,
     ACTION_HERO_FULL_SET_SHELLPRICE,
     ACTION_SHORT_SET_SHELLPRICE,
     ACTION_BUTTON_SET_SHELLPRICE,
     ACTION_AUTO_VEHICLEBUYPRICE,
     ACTION_FULL_VEHICLEBUYPRICE,
     ACTION_SHORT_VEHICLEBUYPRICE_MORE,
     ACTION_SHORT_VEHICLEBUYPRICE_TWO,
     ACTION_SHORT_VEHICLEBUYPRICE_ONE,
     ACTION_BUTTON_VEHICLEBUYPRICE,
     ACTION_AUTO_VEHICLERENTPRICE,
     ACTION_SHORT_VEHICLERENTPRICE_MORE,
     ACTION_SHORT_VEHICLERENTPRICE_TWO,
     ACTION_SHORT_VEHICLERENTPRICE_ONE,
     ACTION_FULL_VEHICLERENTPRICE,
     ACTION_BUTTON_VEHICLERENTPRICE,
     ACTION_AUTO_CLANCREATIONCOST,
     ACTION_FULL_CLANCREATIONCOST,
     ACTION_HERO_FULL_CLANCREATIONCOST,
     ACTION_SHORT_CLANCREATIONCOST,
     ACTION_BUTTON_CLANCREATIONCOST,
     ACTION_AUTO_PREMIUMPACKET1COST,
     ACTION_FULL_PREMIUMPACKET1COST,
     ACTION_HERO_FULL_PREMIUMPACKET1COST,
     ACTION_SHORT_PREMIUMPACKET1COST,
     ACTION_AUTO_PREMIUMPACKET3COST,
     ACTION_FULL_PREMIUMPACKET3COST,
     ACTION_HERO_FULL_PREMIUMPACKET3COST,
     ACTION_SHORT_PREMIUMPACKET3COST,
     ACTION_AUTO_PREMIUMPACKET7COST,
     ACTION_FULL_PREMIUMPACKET7COST,
     ACTION_HERO_FULL_PREMIUMPACKET7COST,
     ACTION_SHORT_PREMIUMPACKET7COST,
     ACTION_AUTO_PREMIUMPACKET14COST,
     ACTION_FULL_PREMIUMPACKET14COST,
     ACTION_HERO_FULL_PREMIUMPACKET14COST,
     ACTION_SHORT_PREMIUMPACKET14COST,
     ACTION_AUTO_PREMIUMPACKET30COST,
     ACTION_FULL_PREMIUMPACKET30COST,
     ACTION_HERO_FULL_PREMIUMPACKET30COST,
     ACTION_SHORT_PREMIUMPACKET30COST,
     ACTION_AUTO_PREMIUMPACKET90COST,
     ACTION_FULL_PREMIUMPACKET90COST,
     ACTION_HERO_FULL_PREMIUMPACKET90COST,
     ACTION_SHORT_PREMIUMPACKET90COST,
     ACTION_AUTO_PREMIUMPACKET180COST,
     ACTION_FULL_PREMIUMPACKET180COST,
     ACTION_HERO_FULL_PREMIUMPACKET180COST,
     ACTION_SHORT_PREMIUMPACKET180COST,
     ACTION_AUTO_PREMIUMPACKET360COST,
     ACTION_FULL_PREMIUMPACKET360COST,
     ACTION_HERO_FULL_PREMIUMPACKET360COST,
     ACTION_SHORT_PREMIUMPACKET360COST,
     ACTION_BUTTON_PREMIUMPACKET_NEW,
     ACTION_BUTTON_PREMIUMPACKET_CONTINUE,
     ACTION_AUTO_WINXPFACTORMODE_ALWAYS,
     ACTION_FULL_WINXPFACTORMODE_ALWAYS,
     ACTION_SHORT_WINXPFACTORMODE_ALWAYS,
     ACTION_BUTTON_WINXPFACTORMODE_ALWAYS,
     ACTION_AUTO_WINXPFACTORMODE_DAILY,
     ACTION_FULL_WINXPFACTORMODE_DAILY,
     ACTION_SHORT_WINXPFACTORMODE_DAILY,
     ACTION_BUTTON_WINXPFACTORMODE_DAILY,
     ACTION_AUTO_FREEXPTOTMANXPRATE,
     ACTION_FULL_FREEXPTOTMANXPRATE,
     ACTION_HERO_FULL_FREEXPTOTMANXPRATE,
     ACTION_SHORT_FREEXPTOTMANXPRATE,
     ACTION_BUTTON_FREEXPTOTMANXPRATE,
     ACTION_AUTO_MUL_GOODIEPRICEALL,
     ACTION_SHORT_MUL_GOODIEPRICEALL,
     ACTION_BUTTON_MUL_GOODIEPRICEALL,
     ACTION_AUTO_SET_GOODIEPRICE,
     ACTION_SHORT_SET_GOODIEPRICE,
     ACTION_BUTTON_SET_GOODIEPRICE,
     ACTION_AUTO_MUL_GOODIEPRICE,
     ACTION_SHORT_MUL_GOODIEPRICE,
     ACTION_BUTTON_MUL_GOODIEPRICE,
     ACTION_AUTO_SET_PRICEGROUPPRICE,
     ACTION_SHORT_SET_PRICEGROUPPRICE,
     ACTION_BUTTON_SET_PRICEGROUPPRICE,
     ACTION_AUTO_MUL_PRICEGROUPPRICE,
     ACTION_SHORT_MUL_PRICEGROUPPRICE,
     ACTION_BUTTON_MUL_PRICEGROUPPRICE,
     ACTION_AUTO_MUL_PRICEGROUPPRICEBYTAG,
     ACTION_SHORT_MUL_PRICEGROUPPRICEBYTAG,
     ACTION_BUTTON_MUL_PRICEGROUPPRICEBYTAG,
     ACTION_AUTO_MUL_PRICEGROUPPRICEALL,
     ACTION_SHORT_MUL_PRICEGROUPPRICEALL,
     ACTION_BUTTON_MUL_PRICEGROUPPRICEALL,
     ACTION_AUTO_TRADEINSELLPRICEFACTOR,
     ACTION_FULL_TRADEINSELLPRICEFACTOR,
     ACTION_HERO_FULL_TRADEINSELLPRICEFACTOR,
     ACTION_SHORT_TRADEINSELLPRICEFACTOR,
     ACTION_BUTTON_TRADEINSELLPRICEFACTOR,
     ACTION_DISCOUNT_MORE,
     ACTION_DISCOUNT_DISCOUNTTEXT,
     ACTION_DISCOUNT_DISCOUNTUPTOTEXT,
     ACTION_DISCOUNT_TRADEINLABELTEXT,
     ACTION_DISCOUNT_PERCENT,
     ACTION_DISCOUNT_MODIFIER,
     ACTION_DISCOUNT_XP,
     ACTION_CHAIN_HINT_REMOVALCOST,
     ACTION_CHAIN_HINT_SHELLSPRICE,
     ACTION_CHAIN_HINT_OPENPERSONALCASE,
     ACTION_CHAIN_HINT_CHANGEROLEDISCOUNTAVAILABLE,
     ACTION_CHAIN_HINT_RETRAININGDISCOUNTAVAILABLE,
     ACTION_CHAIN_HINT_OPENCREWBOOKS,
     ACTION_CHAIN_HINT_CREWRETAININGDISCOUNTAVAILABLE,
     ACTION_CHAIN_HINT_DROPSKILLS,
     ACTION_CHAIN_HINT_CHANGEDOCUMENTS,
     ACTION_CHAIN_HINT_CREWRETRAINING,
     ACTION_CHAIN_HINT_WINXPFACTORMODE,
     ACTION_CHAIN_HINT_PREMDAYS,
     ACTION_CHAIN_HINT_CUSTOMIZATION,
     ACTION_CHAIN_HINT_CAMOUFLAGES,
     ACTION_CHAIN_HINT_EMBLEMS,
     ACTION_CHAIN_HINT_INSCRIPTIONS,
     ACTION_LABEL_BATTLEQUESTS,
     ACTION_EMPTY_INFO,
     ACTION_EMPTY_BTNLABEL,
     ACTION_COMINGSOON_LABEL,
     ACTION_COMINGSOON_TIME,
     ACTION_TIME_FINISH,
     ACTION_TIME_LEFT,
     ACTION_MORE_TYPE_EQUIPMENT,
     ACTION_MORE_TYPE_OPTIONALDEVICES,
     ACTION_MORE_TYPE_GOODIES,
     ACTION_MORE_TYPE_VEHICLES,
     ACTION_MORE_TYPE_CUSTOMIZATIONS,
     ACTION_BOOSTER_BOOSTER_XP,
     ACTION_BOOSTER_BOOSTER_FREE_XP,
     ACTION_BOOSTER_BOOSTER_CREW_XP,
     ACTION_BOOSTER_BOOSTER_CREDITS,
     ACTION_BOOSTER_BOOSTER_REPAIR,
     ACTION_EXCHANGERATE_GOLD2CREDIT)
    DETAILS_DOSSIER_ALL_ENUM = (
     DETAILS_DOSSIER_RANDOM_XP,
     DETAILS_DOSSIER_RANDOM_MAXXP,
     DETAILS_DOSSIER_RANDOM_WINS,
     DETAILS_DOSSIER_RANDOM_LOSSES,
     DETAILS_DOSSIER_RANDOM_SURVIVEDBATTLES,
     DETAILS_DOSSIER_RANDOM_LASTBATTLETIME,
     DETAILS_DOSSIER_RANDOM_WINANDSURVIVED,
     DETAILS_DOSSIER_RANDOM_BATTLEHEROES,
     DETAILS_DOSSIER_RANDOM_FRAGS,
     DETAILS_DOSSIER_RANDOM_MAXFRAGS,
     DETAILS_DOSSIER_RANDOM_MAXDAMAGE,
     DETAILS_DOSSIER_RANDOM_FRAGS8P,
     DETAILS_DOSSIER_RANDOM_FRAGSBEAST,
     DETAILS_DOSSIER_RANDOM_DIRECTHITS,
     DETAILS_DOSSIER_RANDOM_SPOTTED,
     DETAILS_DOSSIER_RANDOM_DAMAGEDEALT,
     DETAILS_DOSSIER_RANDOM_DAMAGERECEIVED,
     DETAILS_DOSSIER_RANDOM_DIRECTHITSRECEIVED,
     DETAILS_DOSSIER_RANDOM_CAPTUREPOINTS,
     DETAILS_DOSSIER_RANDOM_DROPPEDCAPTUREPOINTS,
     DETAILS_DOSSIER_RANDOM_PIERCINGS,
     DETAILS_DOSSIER_RANDOM_NODAMAGEDIRECTHITSRECEIVED,
     DETAILS_DOSSIER_RANDOM_PIERCINGSRECEIVED,
     DETAILS_DOSSIER_RANDOM_POTENTIALDAMAGERECEIVED,
     DETAILS_DOSSIER_RANDOM_DAMAGEBLOCKEDBYARMOR,
     DETAILS_DOSSIER_RANDOM_ORIGINALXP,
     DETAILS_DOSSIER_RANDOM_DAMAGEASSISTEDTRACK,
     DETAILS_DOSSIER_RANDOM_DAMAGEASSISTEDRADIO,
     DETAILS_DOSSIER_RANDOM_SHOTS,
     DETAILS_DOSSIER_RANDOM_EXPLOSIONHITSRECEIVED,
     DETAILS_DOSSIER_RANDOM_BATTLESCOUNT,
     DETAILS_DOSSIER_CLAN_XP,
     DETAILS_DOSSIER_CLAN_BATTLESCOUNT,
     DETAILS_DOSSIER_CLAN_WINS,
     DETAILS_DOSSIER_CLAN_LOSSES,
     DETAILS_DOSSIER_CLAN_SURVIVEDBATTLES,
     DETAILS_DOSSIER_CLAN_FRAGS,
     DETAILS_DOSSIER_CLAN_DIRECTHITS,
     DETAILS_DOSSIER_CLAN_SPOTTED,
     DETAILS_DOSSIER_CLAN_DAMAGEDEALT,
     DETAILS_DOSSIER_CLAN_MAXDAMAGE,
     DETAILS_DOSSIER_CLAN_DAMAGERECEIVED,
     DETAILS_DOSSIER_CLAN_CAPTUREPOINTS,
     DETAILS_DOSSIER_CLAN_DROPPEDCAPTUREPOINTS,
     DETAILS_DOSSIER_CLAN_PIERCINGS,
     DETAILS_DOSSIER_CLAN_NODAMAGEDIRECTHITSRECEIVED,
     DETAILS_DOSSIER_CLAN_PIERCINGSRECEIVED,
     DETAILS_DOSSIER_CLAN_POTENTIALDAMAGERECEIVED,
     DETAILS_DOSSIER_CLAN_DAMAGEBLOCKEDBYARMOR,
     DETAILS_DOSSIER_CLAN_ORIGINALXP,
     DETAILS_DOSSIER_CLAN_DAMAGEASSISTEDTRACK,
     DETAILS_DOSSIER_CLAN_DAMAGEASSISTEDRADIO,
     DETAILS_DOSSIER_HISTORICAL_XP,
     DETAILS_DOSSIER_HISTORICAL_BATTLESCOUNT,
     DETAILS_DOSSIER_HISTORICAL_WINS,
     DETAILS_DOSSIER_HISTORICAL_LOSSES,
     DETAILS_DOSSIER_HISTORICAL_SURVIVEDBATTLES,
     DETAILS_DOSSIER_HISTORICAL_FRAGS,
     DETAILS_DOSSIER_HISTORICAL_DIRECTHITS,
     DETAILS_DOSSIER_HISTORICAL_SPOTTED,
     DETAILS_DOSSIER_HISTORICAL_DAMAGEDEALT,
     DETAILS_DOSSIER_HISTORICAL_MAXDAMAGE,
     DETAILS_DOSSIER_HISTORICAL_DAMAGERECEIVED,
     DETAILS_DOSSIER_HISTORICAL_CAPTUREPOINTS,
     DETAILS_DOSSIER_HISTORICAL_DROPPEDCAPTUREPOINTS,
     DETAILS_DOSSIER_HISTORICAL_PIERCINGS,
     DETAILS_DOSSIER_HISTORICAL_NODAMAGEDIRECTHITSRECEIVED,
     DETAILS_DOSSIER_HISTORICAL_PIERCINGSRECEIVED,
     DETAILS_DOSSIER_HISTORICAL_POTENTIALDAMAGERECEIVED,
     DETAILS_DOSSIER_HISTORICAL_DAMAGEBLOCKEDBYARMOR,
     DETAILS_DOSSIER_HISTORICAL_ORIGINALXP,
     DETAILS_DOSSIER_HISTORICAL_DAMAGEASSISTEDTRACK,
     DETAILS_DOSSIER_HISTORICAL_DAMAGEASSISTEDRADIO,
     DETAILS_DOSSIER_TEAM_XP,
     DETAILS_DOSSIER_TEAM_BATTLESCOUNT,
     DETAILS_DOSSIER_TEAM_WINS,
     DETAILS_DOSSIER_TEAM_LOSSES,
     DETAILS_DOSSIER_TEAM_SURVIVEDBATTLES,
     DETAILS_DOSSIER_TEAM_FRAGS,
     DETAILS_DOSSIER_TEAM_DIRECTHITS,
     DETAILS_DOSSIER_TEAM_SPOTTED,
     DETAILS_DOSSIER_TEAM_DAMAGEDEALT,
     DETAILS_DOSSIER_TEAM_MAXDAMAGE,
     DETAILS_DOSSIER_TEAM_DAMAGERECEIVED,
     DETAILS_DOSSIER_TEAM_CAPTUREPOINTS,
     DETAILS_DOSSIER_TEAM_DROPPEDCAPTUREPOINTS,
     DETAILS_DOSSIER_TEAM_PIERCINGS,
     DETAILS_DOSSIER_TEAM_NODAMAGEDIRECTHITSRECEIVED,
     DETAILS_DOSSIER_TEAM_PIERCINGSRECEIVED,
     DETAILS_DOSSIER_TEAM_POTENTIALDAMAGERECEIVED,
     DETAILS_DOSSIER_TEAM_DAMAGEBLOCKEDBYARMOR,
     DETAILS_DOSSIER_TEAM_ORIGINALXP,
     DETAILS_DOSSIER_TEAM_DAMAGEASSISTEDTRACK,
     DETAILS_DOSSIER_TEAM_DAMAGEASSISTEDRADIO,
     DETAILS_DOSSIER_LADDER_XP,
     DETAILS_DOSSIER_LADDER_BATTLESCOUNT,
     DETAILS_DOSSIER_LADDER_WINS,
     DETAILS_DOSSIER_LADDER_LOSSES,
     DETAILS_DOSSIER_LADDER_SURVIVEDBATTLES,
     DETAILS_DOSSIER_LADDER_FRAGS,
     DETAILS_DOSSIER_LADDER_DIRECTHITS,
     DETAILS_DOSSIER_LADDER_SPOTTED,
     DETAILS_DOSSIER_LADDER_DAMAGEDEALT,
     DETAILS_DOSSIER_LADDER_MAXDAMAGE,
     DETAILS_DOSSIER_LADDER_DAMAGERECEIVED,
     DETAILS_DOSSIER_LADDER_CAPTUREPOINTS,
     DETAILS_DOSSIER_LADDER_DROPPEDCAPTUREPOINTS,
     DETAILS_DOSSIER_LADDER_PIERCINGS,
     DETAILS_DOSSIER_LADDER_NODAMAGEDIRECTHITSRECEIVED,
     DETAILS_DOSSIER_LADDER_PIERCINGSRECEIVED,
     DETAILS_DOSSIER_LADDER_POTENTIALDAMAGERECEIVED,
     DETAILS_DOSSIER_LADDER_DAMAGEBLOCKEDBYARMOR,
     DETAILS_DOSSIER_LADDER_ORIGINALXP,
     DETAILS_DOSSIER_LADDER_DAMAGEASSISTEDTRACK,
     DETAILS_DOSSIER_LADDER_DAMAGEASSISTEDRADIO,
     DETAILS_DOSSIER_0_BATTLESCOUNT,
     DETAILS_DOSSIER_1_BATTLESCOUNT,
     DETAILS_DOSSIER_2_BATTLESCOUNT,
     DETAILS_DOSSIER_4_BATTLESCOUNT,
     DETAILS_DOSSIER_5_BATTLESCOUNT,
     DETAILS_DOSSIER_6_BATTLESCOUNT,
     DETAILS_DOSSIER_7_BATTLESCOUNT,
     DETAILS_DOSSIER_9_BATTLESCOUNT,
     DETAILS_DOSSIER_13_BATTLESCOUNT,
     DETAILS_DOSSIER_16_BATTLESCOUNT,
     DETAILS_DOSSIER_18_BATTLESCOUNT,
     DETAILS_DOSSIER_19_BATTLESCOUNT,
     DETAILS_DOSSIER_20_BATTLESCOUNT,
     DETAILS_DOSSIER_21_BATTLESCOUNT,
     DETAILS_DOSSIER_22_BATTLESCOUNT,
     DETAILS_DOSSIER_24_BATTLESCOUNT,
     DETAILS_DOSSIER_27_BATTLESCOUNT,
     DETAILS_DOSSIER_37_BATTLESCOUNT,
     DETAILS_DOSSIER_39_BATTLESCOUNT,
     DETAILS_DOSSIER_42_BATTLESCOUNT,
     DETAILS_DOSSIER_43_BATTLESCOUNT,
     DETAILS_DOSSIER_50_BATTLESCOUNT)
    PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ENUM = (
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_USSR,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_GERMANY,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_USA,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ALLIANCE_FRANCE,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_LIGHTTANK,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_MEDIUMTANK,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_HEAVYTANK,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_AT_SPG,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_SPG,
     PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ANY)

    @classmethod
    def getTokenTitle(cls, style):
        outcome = (b'#quests:token/default/{}').format(style)
        if outcome not in cls.TOKEN_DEFAULT_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getBonusName(cls, bonusName):
        outcome = (b'#quests:bonusName/{}').format(bonusName)
        if outcome not in cls.BONUSNAME_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getActionDescription(cls, action):
        outcome = (b'#quests:action/{}').format(action)
        if outcome not in cls.ACTION_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getDetailsDossier(cls, battleTypeName, keyName):
        outcome = (b'#quests:details/dossier/{}/{}').format(battleTypeName, keyName)
        if outcome not in cls.DETAILS_DOSSIER_ALL_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome

    @classmethod
    def getAddBottomVehType(cls, alliance):
        outcome = (b'#quests:personalMission/status/addBottom/vehicleType/{}').format(alliance)
        if outcome not in cls.PERSONALMISSION_STATUS_ADDBOTTOM_VEHICLETYPE_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
