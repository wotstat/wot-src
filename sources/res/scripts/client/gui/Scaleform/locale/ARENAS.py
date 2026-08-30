from debug_utils import LOG_WARNING

class ARENAS(object):
    TYPE_CTF_NAME = b'#arenas:type/ctf/name'
    TYPE_CTF_DESCRIPTION = b'#arenas:type/ctf/description'
    TYPE_DOMINATION_NAME = b'#arenas:type/domination/name'
    TYPE_DOMINATION_DESCRIPTION = b'#arenas:type/domination/description'
    TYPE_ASSAULT_NAME = b'#arenas:type/assault/name'
    TYPE_ASSAULT_DESCRIPTION1 = b'#arenas:type/assault/description1'
    TYPE_ASSAULT_DESCRIPTION2 = b'#arenas:type/assault/description2'
    TYPE_ASSAULT2_NAME = b'#arenas:type/assault2/name'
    TYPE_ASSAULT2_DESCRIPTION1 = b'#arenas:type/assault2/description1'
    TYPE_ASSAULT2_DESCRIPTION2 = b'#arenas:type/assault2/description2'
    TYPE_CTF2_NAME = b'#arenas:type/ctf2/name'
    TYPE_CTF2_DESCRIPTION = b'#arenas:type/ctf2/description'
    TYPE_ESCORT_NAME = b'#arenas:type/escort/name'
    TYPE_ESCORT_DESCRIPTION1 = b'#arenas:type/escort/description1'
    TYPE_ESCORT_DESCRIPTION2 = b'#arenas:type/escort/description2'
    TYPE_NATIONS_NAME = b'#arenas:type/nations/name'
    TYPE_NATIONS_DESCRIPTION = b'#arenas:type/nations/description'
    TYPE_FALLOUT_NAME = b'#arenas:type/fallout/name'
    TYPE_FALLOUT_DESCRIPTION = b'#arenas:type/fallout/description'
    TYPE_FALLOUT1_NAME = b'#arenas:type/fallout1/name'
    TYPE_FALLOUT1_DESCRIPTION = b'#arenas:type/fallout1/description'
    TYPE_FALLOUT2_NAME = b'#arenas:type/fallout2/name'
    TYPE_FALLOUT2_DESCRIPTION = b'#arenas:type/fallout2/description'
    TYPE_FALLOUT3_NAME = b'#arenas:type/fallout3/name'
    TYPE_FALLOUT3_DESCRIPTION = b'#arenas:type/fallout3/description'
    TYPE_FALLOUT4_NAME = b'#arenas:type/fallout4/name'
    TYPE_FALLOUT4_DESCRIPTION = b'#arenas:type/fallout4/description'
    TYPE_FALLOUT5_NAME = b'#arenas:type/fallout5/name'
    TYPE_FALLOUT5_DESCRIPTION = b'#arenas:type/fallout5/description'
    TYPE_FALLOUT6_NAME = b'#arenas:type/fallout6/name'
    TYPE_FALLOUT6_DESCRIPTION = b'#arenas:type/fallout6/description'
    TYPE_FALLOUTMUTLITEAM_DESCRIPTION = b'#arenas:type/falloutMutliteam/description'
    TYPE_CTF30X30_NAME = b'#arenas:type/ctf30x30/name'
    TYPE_CTF30X30_DESCRIPTION = b'#arenas:type/ctf30x30/description'
    TYPE_DOMINATION30X30_NAME = b'#arenas:type/domination30x30/name'
    TYPE_DOMINATION30X30_DESCRIPTION = b'#arenas:type/domination30x30/description'
    TYPE_RTS_NAME = b'#arenas:type/rts/name'
    TYPE_RTS_DESCRIPTION_COMMANDER = b'#arenas:type/rts/description/commander'
    TYPE_RTS_DESCRIPTION_TANKMAN = b'#arenas:type/rts/description/tankman'
    TYPE_RTS_BOOTCAMP_NAME = b'#arenas:type/rts_bootcamp/name'
    TYPE_RTS_BOOTCAMP_DESCRIPTION_COMMANDER = b'#arenas:type/rts_bootcamp/description/commander'
    TYPE_COMP7_NAME = b'#arenas:type/comp7/name'
    TYPE_COMP7_DESCRIPTION = b'#arenas:type/comp7/description'
    TYPE_COMP7_SHORT_DESCRIPTION = b'#arenas:type/comp7/short_description'
    INVALID_MAP_NAME = b'#arenas:invalid_map/name'
    C_01_KARELIA_NAME = b'#arenas:01_karelia/name'
    C_01_KARELIA_DESCRIPTION = b'#arenas:01_karelia/description'
    C_02_MALINOVKA_NAME = b'#arenas:02_malinovka/name'
    C_02_MALINOVKA_DESCRIPTION = b'#arenas:02_malinovka/description'
    C_04_HIMMELSDORF_NAME = b'#arenas:04_himmelsdorf/name'
    C_04_HIMMELSDORF_DESCRIPTION = b'#arenas:04_himmelsdorf/description'
    C_05_PROHOROVKA_NAME = b'#arenas:05_prohorovka/name'
    C_05_PROHOROVKA_DESCRIPTION = b'#arenas:05_prohorovka/description'
    C_06_ENSK_NAME = b'#arenas:06_ensk/name'
    C_06_ENSK_DESCRIPTION = b'#arenas:06_ensk/description'
    C_07_LAKEVILLE_NAME = b'#arenas:07_lakeville/name'
    C_07_LAKEVILLE_DESCRIPTION = b'#arenas:07_lakeville/description'
    C_08_RUINBERG_NAME = b'#arenas:08_ruinberg/name'
    C_08_RUINBERG_DESCRIPTION = b'#arenas:08_ruinberg/description'
    C_10_HILLS_NAME = b'#arenas:10_hills/name'
    C_10_HILLS_DESCRIPTION = b'#arenas:10_hills/description'
    C_11_MUROVANKA_NAME = b'#arenas:11_murovanka/name'
    C_11_MUROVANKA_DESCRIPTION = b'#arenas:11_murovanka/description'
    C_13_ERLENBERG_NAME = b'#arenas:13_erlenberg/name'
    C_13_ERLENBERG_DESCRIPTION = b'#arenas:13_erlenberg/description'
    C_14_SIEGFRIED_LINE_NAME = b'#arenas:14_siegfried_line/name'
    C_14_SIEGFRIED_LINE_DESCRIPTION = b'#arenas:14_siegfried_line/description'
    C_17_MUNCHEN_NAME = b'#arenas:17_munchen/name'
    C_17_MUNCHEN_DESCRIPTION = b'#arenas:17_munchen/description'
    C_18_CLIFF_NAME = b'#arenas:18_cliff/name'
    C_18_CLIFF_DESCRIPTION = b'#arenas:18_cliff/description'
    C_29_EL_HALLOUF_DESCRIPTION = b'#arenas:29_el_hallouf/description'
    C_31_AIRFIELD_NAME = b'#arenas:31_airfield/name'
    C_31_AIRFIELD_DESCRIPTION = b'#arenas:31_airfield/description'
    C_33_FJORD_NAME = b'#arenas:33_fjord/name'
    C_33_FJORD_DESCRIPTION = b'#arenas:33_fjord/description'
    C_34_REDSHIRE_NAME = b'#arenas:34_redshire/name'
    C_34_REDSHIRE_DESCRIPTION = b'#arenas:34_redshire/description'
    C_35_STEPPES_NAME = b'#arenas:35_steppes/name'
    C_35_STEPPES_DESCRIPTION = b'#arenas:35_steppes/description'
    C_36_FISHING_BAY_NAME = b'#arenas:36_fishing_bay/name'
    C_36_FISHING_BAY_DESCRIPTION = b'#arenas:36_fishing_bay/description'
    C_37_CAUCASUS_NAME = b'#arenas:37_caucasus/name'
    C_37_CAUCASUS_DESCRIPTION = b'#arenas:37_caucasus/description'
    C_38_MANNERHEIM_LINE_NAME = b'#arenas:38_mannerheim_line/name'
    C_38_MANNERHEIM_LINE_DESCRIPTION = b'#arenas:38_mannerheim_line/description'
    C_44_NORTH_AMERICA_NAME = b'#arenas:44_north_america/name'
    C_44_NORTH_AMERICA_DESCRIPTION = b'#arenas:44_north_america/description'
    C_19_MONASTERY_NAME = b'#arenas:19_monastery/name'
    C_19_MONASTERY_DESCRIPTION = b'#arenas:19_monastery/description'
    C_23_WESTFELD_NAME = b'#arenas:23_westfeld/name'
    C_23_WESTFELD_DESCRIPTION = b'#arenas:23_westfeld/description'
    C_28_DESERT_NAME = b'#arenas:28_desert/name'
    C_28_DESERT_DESCRIPTION = b'#arenas:28_desert/description'
    C_29_EL_HALLOUF_NAME = b'#arenas:29_el_hallouf/name'
    C_45_NORTH_AMERICA_NAME = b'#arenas:45_north_america/name'
    C_45_NORTH_AMERICA_DESCRIPTION = b'#arenas:45_north_america/description'
    C_47_CANADA_A_NAME = b'#arenas:47_canada_a/name'
    C_47_CANADA_A_DESCRIPTION = b'#arenas:47_canada_a/description'
    C_59_ASIA_GREAT_WALL_NAME = b'#arenas:59_asia_great_wall/name'
    C_59_ASIA_GREAT_WALL_DESCRIPTION = b'#arenas:59_asia_great_wall/description'
    C_63_TUNDRA_NAME = b'#arenas:63_tundra/name'
    C_63_TUNDRA_DESCRIPTION = b'#arenas:63_tundra/description'
    C_101_DDAY_NAME = b'#arenas:101_dday/name'
    C_101_DDAY_DESCRIPTION = b'#arenas:101_dday/description'
    C_101_DDAY_SM24_NAME = b'#arenas:101_dday_sm24/name'
    C_101_DDAY_SM24_DESCRIPTION = b'#arenas:101_dday_sm24/description'
    C_115_SWEDEN_DESCRIPTION = b'#arenas:115_sweden/description'
    C_112_EIFFEL_TOWER_CTF_NAME = b'#arenas:112_eiffel_tower_ctf/name'
    C_112_EIFFEL_TOWER_CTF_DESCRIPTION = b'#arenas:112_eiffel_tower_ctf/description'
    C_114_CZECH_DESCRIPTION = b'#arenas:114_czech/description'
    C_115_SWEDEN_NAME = b'#arenas:115_sweden/name'
    C_208_BF_EPIC_NORMANDY_NAME = b'#arenas:208_bf_epic_normandy/name'
    C_208_BF_EPIC_NORMANDY_DESCRIPTION = b'#arenas:208_bf_epic_normandy/description'
    TYPE_EPIC_NAME = b'#arenas:type/epic/name'
    TYPE_EPIC_NAME_INQUOTES = b'#arenas:type/epic/name/inQuotes'
    TYPE_EPIC_DESCRIPTION1 = b'#arenas:type/epic/description1'
    TYPE_EPIC_DESCRIPTION2 = b'#arenas:type/epic/description2'
    C_03_CAMPANIA_BIG_NAME = b'#arenas:03_campania_big/name'
    C_03_CAMPANIA_BIG_DESCRIPTION = b'#arenas:03_campania_big/description'
    C_217_ER_ALASKA_NAME = b'#arenas:217_er_alaska/name'
    C_217_ER_ALASKA_DESCRIPTION = b'#arenas:217_er_alaska/description'
    C_114_CZECH_NAME = b'#arenas:114_czech/name'
    C_99_POLAND_NAME = b'#arenas:99_poland/name'
    C_99_POLAND_DESCRIPTION = b'#arenas:99_poland/description'
    C_250_BR_BATTLE_CITY2_1_NAME = b'#arenas:250_br_battle_city2-1/name'
    C_250_BR_BATTLE_CITY2_1_DESCRIPTION = b'#arenas:250_br_battle_city2-1/description'
    C_95_LOST_CITY_CTF_NAME = b'#arenas:95_lost_city_ctf/name'
    C_95_LOST_CITY_CTF_DESCRIPTION = b'#arenas:95_lost_city_ctf/description'
    C_209_WG_EPIC_SUBURBIA_NAME = b'#arenas:209_wg_epic_suburbia/name'
    C_209_WG_EPIC_SUBURBIA_DESCRIPTION = b'#arenas:209_wg_epic_suburbia/description'
    C_105_GERMANY_SM24_NAME = b'#arenas:105_germany_sm24/name'
    C_105_GERMANY_SM24_DESCRIPTION = b'#arenas:105_germany_sm24/description'
    C_105_GERMANY_NAME = b'#arenas:105_germany/name'
    C_105_GERMANY_DESCRIPTION = b'#arenas:105_germany/description'
    C_60_ASIA_MIAO_NAME = b'#arenas:60_asia_miao/name'
    C_60_ASIA_MIAO_DESCRIPTION = b'#arenas:60_asia_miao/description'
    C_251_BR_BATTLE_CITY3_NAME = b'#arenas:251_br_battle_city3/name'
    C_127_JAPORT_NAME = b'#arenas:127_japort/name'
    C_127_JAPORT_DESCRIPTION = b'#arenas:127_japort/description'
    C_252_BR_BATTLE_CITY4_NAME = b'#arenas:252_br_battle_city4/name'
    C_252_BR_BATTLE_CITY4_DESCRIPTION = b'#arenas:252_br_battle_city4/description'
    C_128_LAST_FRONTIER_V_NAME = b'#arenas:128_last_frontier_v/name'
    C_128_LAST_FRONTIER_V_DESCRIPTION = b'#arenas:128_last_frontier_v/description'
    C_108_NORMANDY_NOM_NAME = b'#arenas:108_normandy_nom/name'
    C_108_NORMANDY_NOM_DESCRIPTION = b'#arenas:108_normandy_nom/description'
    C_14_SIEGFRIED_LINE_NOM_NAME = b'#arenas:14_siegfried_line_nom/name'
    C_14_SIEGFRIED_LINE_NOM_DESCRIPTION = b'#arenas:14_siegfried_line_nom/description'
    C_121_LOST_PARADISE_V_NAME = b'#arenas:121_lost_paradise_v/name'
    C_121_LOST_PARADISE_V_DESCRIPTION = b'#arenas:121_lost_paradise_v/description'
    TYPE_WINBACK_NAME = b'#arenas:type/winback/name'
    TYPE_WINBACK_DESCRIPTION = b'#arenas:type/winback/description'
    C_210_BF_EPIC_DESERT_NAME = b'#arenas:210_bf_epic_desert/name'
    C_210_BF_EPIC_DESERT_DESCRIPTION = b'#arenas:210_bf_epic_desert/description'
    C_140_FALL_TANKS_NAME = b'#arenas:140_fall_tanks/name'
    C_140_FALL_TANKS_DESCRIPTION = b'#arenas:140_fall_tanks/description'
    C_141_DASH_TO_GO_NAME = b'#arenas:141_dash_to_go/name'
    C_141_DASH_TO_GO_DESCRIPTION = b'#arenas:141_dash_to_go/description'
    C_142_ROAD_TO_DASH_NAME = b'#arenas:142_road_to_dash/name'
    C_142_ROAD_TO_DASH_DESCRIPTION = b'#arenas:142_road_to_dash/description'
    C_08_RUINBERG_SM24_NAME = b'#arenas:08_ruinberg_sm24/name'
    C_08_RUINBERG_SM24_DESCRIPTION = b'#arenas:08_ruinberg_sm24/description'
    C_14_SIEGFRIED_LINE_WT_NAME = b'#arenas:14_siegfried_line_wt/name'
    C_34_REDSHIRE_WT_NAME = b'#arenas:34_redshire_wt/name'
    C_35_STEPPES_WT_NAME = b'#arenas:35_steppes_wt/name'
    C_06_ENSK_BIG_NAME = b'#arenas:06_ensk_big/name'
    C_06_ENSK_BIG_DESCRIPTION = b'#arenas:06_ensk_big/description'
    C_212_EPIC_RANDOM_VALLEY_SM25_NAME = b'#arenas:212_epic_random_valley_sm25/name'
    C_212_EPIC_RANDOM_VALLEY_SM25_DESCRIPTION = b'#arenas:212_epic_random_valley_sm25/description'
    C_120_GRAF_ZEPPELIN_SCC_NAME = b'#arenas:120_graf_zeppelin_scc/name'
    C_120_GRAF_ZEPPELIN_SCC_DESCRIPTION = b'#arenas:120_graf_zeppelin_scc/description'
    C_120_GRAF_ZEPPELIN_NAME = b'#arenas:120_graf_zeppelin/name'
    C_120_GRAF_ZEPPELIN_DESCRIPTION = b'#arenas:120_graf_zeppelin/description'
    C_28_DESERT_COMP7_NB_NAME = b'#arenas:28_desert_comp7_nb/name'
    C_28_DESERT_COMP7_NB_DESCRIPTION = b'#arenas:28_desert_comp7_nb/description'
    C_115_SWEDEN_COMP7_NB_NAME = b'#arenas:115_sweden_comp7_nb/name'
    C_115_SWEDEN_COMP7_NB_DESCRIPTION = b'#arenas:115_sweden_comp7_nb/description'
    C_35_STEPPES_COMP7_NB_NAME = b'#arenas:35_steppes_comp7_nb/name'
    C_35_STEPPES_COMP7_NB_DESCRIPTION = b'#arenas:35_steppes_comp7_nb/description'
    C_128_LAST_FRONTIER_V_COMP7_NB_NAME = b'#arenas:128_last_frontier_v_comp7_nb/name'
    C_128_LAST_FRONTIER_V_COMP7_NB_DESCRIPTION = b'#arenas:128_last_frontier_v_comp7_nb/description'
    ALL_ENUM = (
     TYPE_CTF_NAME,
     TYPE_CTF_DESCRIPTION,
     TYPE_DOMINATION_NAME,
     TYPE_DOMINATION_DESCRIPTION,
     TYPE_ASSAULT_NAME,
     TYPE_ASSAULT_DESCRIPTION1,
     TYPE_ASSAULT_DESCRIPTION2,
     TYPE_ASSAULT2_NAME,
     TYPE_ASSAULT2_DESCRIPTION1,
     TYPE_ASSAULT2_DESCRIPTION2,
     TYPE_CTF2_NAME,
     TYPE_CTF2_DESCRIPTION,
     TYPE_ESCORT_NAME,
     TYPE_ESCORT_DESCRIPTION1,
     TYPE_ESCORT_DESCRIPTION2,
     TYPE_NATIONS_NAME,
     TYPE_NATIONS_DESCRIPTION,
     TYPE_FALLOUT_NAME,
     TYPE_FALLOUT_DESCRIPTION,
     TYPE_FALLOUT1_NAME,
     TYPE_FALLOUT1_DESCRIPTION,
     TYPE_FALLOUT2_NAME,
     TYPE_FALLOUT2_DESCRIPTION,
     TYPE_FALLOUT3_NAME,
     TYPE_FALLOUT3_DESCRIPTION,
     TYPE_FALLOUT4_NAME,
     TYPE_FALLOUT4_DESCRIPTION,
     TYPE_FALLOUT5_NAME,
     TYPE_FALLOUT5_DESCRIPTION,
     TYPE_FALLOUT6_NAME,
     TYPE_FALLOUT6_DESCRIPTION,
     TYPE_FALLOUTMUTLITEAM_DESCRIPTION,
     TYPE_CTF30X30_NAME,
     TYPE_CTF30X30_DESCRIPTION,
     TYPE_DOMINATION30X30_NAME,
     TYPE_DOMINATION30X30_DESCRIPTION,
     TYPE_RTS_NAME,
     TYPE_RTS_DESCRIPTION_COMMANDER,
     TYPE_RTS_DESCRIPTION_TANKMAN,
     TYPE_RTS_BOOTCAMP_NAME,
     TYPE_RTS_BOOTCAMP_DESCRIPTION_COMMANDER,
     TYPE_COMP7_NAME,
     TYPE_COMP7_DESCRIPTION,
     TYPE_COMP7_SHORT_DESCRIPTION,
     INVALID_MAP_NAME,
     C_01_KARELIA_NAME,
     C_01_KARELIA_DESCRIPTION,
     C_02_MALINOVKA_NAME,
     C_02_MALINOVKA_DESCRIPTION,
     C_04_HIMMELSDORF_NAME,
     C_04_HIMMELSDORF_DESCRIPTION,
     C_05_PROHOROVKA_NAME,
     C_05_PROHOROVKA_DESCRIPTION,
     C_06_ENSK_NAME,
     C_06_ENSK_DESCRIPTION,
     C_07_LAKEVILLE_NAME,
     C_07_LAKEVILLE_DESCRIPTION,
     C_08_RUINBERG_NAME,
     C_08_RUINBERG_DESCRIPTION,
     C_10_HILLS_NAME,
     C_10_HILLS_DESCRIPTION,
     C_11_MUROVANKA_NAME,
     C_11_MUROVANKA_DESCRIPTION,
     C_13_ERLENBERG_NAME,
     C_13_ERLENBERG_DESCRIPTION,
     C_14_SIEGFRIED_LINE_NAME,
     C_14_SIEGFRIED_LINE_DESCRIPTION,
     C_17_MUNCHEN_NAME,
     C_17_MUNCHEN_DESCRIPTION,
     C_18_CLIFF_NAME,
     C_18_CLIFF_DESCRIPTION,
     C_29_EL_HALLOUF_DESCRIPTION,
     C_31_AIRFIELD_NAME,
     C_31_AIRFIELD_DESCRIPTION,
     C_33_FJORD_NAME,
     C_33_FJORD_DESCRIPTION,
     C_34_REDSHIRE_NAME,
     C_34_REDSHIRE_DESCRIPTION,
     C_35_STEPPES_NAME,
     C_35_STEPPES_DESCRIPTION,
     C_36_FISHING_BAY_NAME,
     C_36_FISHING_BAY_DESCRIPTION,
     C_37_CAUCASUS_NAME,
     C_37_CAUCASUS_DESCRIPTION,
     C_38_MANNERHEIM_LINE_NAME,
     C_38_MANNERHEIM_LINE_DESCRIPTION,
     C_44_NORTH_AMERICA_NAME,
     C_44_NORTH_AMERICA_DESCRIPTION,
     C_19_MONASTERY_NAME,
     C_19_MONASTERY_DESCRIPTION,
     C_23_WESTFELD_NAME,
     C_23_WESTFELD_DESCRIPTION,
     C_28_DESERT_NAME,
     C_28_DESERT_DESCRIPTION,
     C_29_EL_HALLOUF_NAME,
     C_45_NORTH_AMERICA_NAME,
     C_45_NORTH_AMERICA_DESCRIPTION,
     C_47_CANADA_A_NAME,
     C_47_CANADA_A_DESCRIPTION,
     C_59_ASIA_GREAT_WALL_NAME,
     C_59_ASIA_GREAT_WALL_DESCRIPTION,
     C_63_TUNDRA_NAME,
     C_63_TUNDRA_DESCRIPTION,
     C_101_DDAY_NAME,
     C_101_DDAY_DESCRIPTION,
     C_101_DDAY_SM24_NAME,
     C_101_DDAY_SM24_DESCRIPTION,
     C_115_SWEDEN_DESCRIPTION,
     C_112_EIFFEL_TOWER_CTF_NAME,
     C_112_EIFFEL_TOWER_CTF_DESCRIPTION,
     C_114_CZECH_DESCRIPTION,
     C_115_SWEDEN_NAME,
     C_208_BF_EPIC_NORMANDY_NAME,
     C_208_BF_EPIC_NORMANDY_DESCRIPTION,
     TYPE_EPIC_NAME,
     TYPE_EPIC_NAME_INQUOTES,
     TYPE_EPIC_DESCRIPTION1,
     TYPE_EPIC_DESCRIPTION2,
     C_03_CAMPANIA_BIG_NAME,
     C_03_CAMPANIA_BIG_DESCRIPTION,
     C_217_ER_ALASKA_NAME,
     C_217_ER_ALASKA_DESCRIPTION,
     C_114_CZECH_NAME,
     C_99_POLAND_NAME,
     C_99_POLAND_DESCRIPTION,
     C_250_BR_BATTLE_CITY2_1_NAME,
     C_250_BR_BATTLE_CITY2_1_DESCRIPTION,
     C_95_LOST_CITY_CTF_NAME,
     C_95_LOST_CITY_CTF_DESCRIPTION,
     C_209_WG_EPIC_SUBURBIA_NAME,
     C_209_WG_EPIC_SUBURBIA_DESCRIPTION,
     C_105_GERMANY_SM24_NAME,
     C_105_GERMANY_SM24_DESCRIPTION,
     C_105_GERMANY_NAME,
     C_105_GERMANY_DESCRIPTION,
     C_60_ASIA_MIAO_NAME,
     C_60_ASIA_MIAO_DESCRIPTION,
     C_251_BR_BATTLE_CITY3_NAME,
     C_127_JAPORT_NAME,
     C_127_JAPORT_DESCRIPTION,
     C_252_BR_BATTLE_CITY4_NAME,
     C_252_BR_BATTLE_CITY4_DESCRIPTION,
     C_128_LAST_FRONTIER_V_NAME,
     C_128_LAST_FRONTIER_V_DESCRIPTION,
     C_108_NORMANDY_NOM_NAME,
     C_108_NORMANDY_NOM_DESCRIPTION,
     C_14_SIEGFRIED_LINE_NOM_NAME,
     C_14_SIEGFRIED_LINE_NOM_DESCRIPTION,
     C_121_LOST_PARADISE_V_NAME,
     C_121_LOST_PARADISE_V_DESCRIPTION,
     TYPE_WINBACK_NAME,
     TYPE_WINBACK_DESCRIPTION,
     C_210_BF_EPIC_DESERT_NAME,
     C_210_BF_EPIC_DESERT_DESCRIPTION,
     C_140_FALL_TANKS_NAME,
     C_140_FALL_TANKS_DESCRIPTION,
     C_141_DASH_TO_GO_NAME,
     C_141_DASH_TO_GO_DESCRIPTION,
     C_142_ROAD_TO_DASH_NAME,
     C_142_ROAD_TO_DASH_DESCRIPTION,
     C_08_RUINBERG_SM24_NAME,
     C_08_RUINBERG_SM24_DESCRIPTION,
     C_14_SIEGFRIED_LINE_WT_NAME,
     C_34_REDSHIRE_WT_NAME,
     C_35_STEPPES_WT_NAME,
     C_06_ENSK_BIG_NAME,
     C_06_ENSK_BIG_DESCRIPTION,
     C_212_EPIC_RANDOM_VALLEY_SM25_NAME,
     C_212_EPIC_RANDOM_VALLEY_SM25_DESCRIPTION,
     C_120_GRAF_ZEPPELIN_SCC_NAME,
     C_120_GRAF_ZEPPELIN_SCC_DESCRIPTION,
     C_120_GRAF_ZEPPELIN_NAME,
     C_120_GRAF_ZEPPELIN_DESCRIPTION,
     C_28_DESERT_COMP7_NB_NAME,
     C_28_DESERT_COMP7_NB_DESCRIPTION,
     C_115_SWEDEN_COMP7_NB_NAME,
     C_115_SWEDEN_COMP7_NB_DESCRIPTION,
     C_35_STEPPES_COMP7_NB_NAME,
     C_35_STEPPES_COMP7_NB_DESCRIPTION,
     C_128_LAST_FRONTIER_V_COMP7_NB_NAME,
     C_128_LAST_FRONTIER_V_COMP7_NB_DESCRIPTION)

    @classmethod
    def all(cls, key0):
        outcome = (b'#arenas:{}').format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING((b'Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
