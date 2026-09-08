(() => {
  var __webpack_modules__ = {
      3779: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => D });
        var r = t(6483),
          n = t.n(r),
          s = t(9887),
          a = t.n(s),
          i = t(3377),
          o = t(6179),
          l = t.n(o),
          c = t(5026);
        const m = [
          "className",
          "width",
          "height",
          "m",
          "mt",
          "mr",
          "mb",
          "ml",
          "column",
          "row",
          "flexDirection",
          "flexStart",
          "center",
          "flexEnd",
          "spaceBetween",
          "spaceAround",
          "justifyContent",
          "alignItems",
          "alignSelf",
          "wrap",
          "flexWrap",
          "grow",
          "shrink",
          "flex",
          "style",
          "children",
        ];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        Object.keys(a());
        const E = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          _ = (Object.keys(E), ["mt", "mr", "mb", "ml"]),
          A = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          D = (0, i.ZP)((e) => {
            let u = e.className,
              t = e.width,
              r = e.height,
              s = e.m,
              a = e.mt,
              i = void 0 === a ? s : a,
              D = e.mr,
              F = void 0 === D ? s : D,
              g = e.mb,
              B = void 0 === g ? s : g,
              C = e.ml,
              p = void 0 === C ? s : C,
              h = e.column,
              f = e.row,
              b = e.flexDirection,
              v = void 0 === b ? (h ? "column" : f && "row") || void 0 : b,
              w = e.flexStart,
              S = e.center,
              y = e.flexEnd,
              P = e.spaceBetween,
              R = e.spaceAround,
              x = e.justifyContent,
              T =
                void 0 === x
                  ? (w ? "flex-start" : S && "center") ||
                    (y && "flex-end") ||
                    (P && "space-between") ||
                    (R && "space-around") ||
                    void 0
                  : x,
              N = e.alignItems,
              L =
                void 0 === N
                  ? (w ? "flex-start" : S && "center") || (y && "flex-end") || void 0
                  : N,
              M = e.alignSelf,
              k = e.wrap,
              O = e.flexWrap,
              I = void 0 === O ? (k ? "wrap" : void 0) : O,
              H = e.grow,
              U = e.shrink,
              W = e.flex,
              Q = void 0 === W ? (H || U ? `${H ? 1 : 0} ${U ? 1 : 0} auto` : void 0) : W,
              G = e.style,
              j = e.children,
              $ = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, m);
            const z = (0, o.useMemo)(() => {
                const e = { mt: i, mr: F, mb: B, ml: p },
                  u = ((e) =>
                    _.reduce((u, t) => {
                      const r = e[t];
                      return r && "number" != typeof r ? u.concat(E[!0 === r ? "MD" : r][t]) : u;
                    }, []))(e),
                  n = ((e) =>
                    _.reduce((u, t) => {
                      const r = e[t];
                      return ("number" == typeof r && (u[A[t]] = r + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, G, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: Q,
                    alignSelf: M,
                    display: v || L ? "flex" : void 0,
                    flexDirection: v,
                    flexWrap: I,
                    justifyContent: T,
                    alignItems: L,
                  }),
                  computedClassNames: u,
                };
              }, [t, r, i, F, B, p, G, Q, M, v, I, T, L]),
              q = z.computedStyle,
              X = z.computedClassNames;
            return l().createElement(
              "div",
              d({ className: n()(c.Z.base, ...X, u), style: q }, $),
              j,
            );
          });
      },
      2372: (e, u, t) => {
        "use strict";
        t.d(u, { A: () => a });
        var r = t(6179),
          n = t.n(r),
          s = t(4179);
        class a extends n().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = s.B3.GOLD;
            else e = s.B3.INTEGRAL;
            const u = s.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        a.defaultProps = { format: "integral" };
      },
      280: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => l });
        var r = t(6179),
          n = t.n(r),
          s = t(6483),
          a = t.n(s),
          i = t(3649),
          o = t(5287);
        const l = ({ binding: e, text: u = "", classMix: t, alignment: s = i.v2.left }) =>
          null === u
            ? (console.error("FormatText was supplied with 'null'"), null)
            : n().createElement(
                r.Fragment,
                null,
                u.split("\n").map((u, l) =>
                  n().createElement(
                    "div",
                    { className: a()(o.Z.base, t), key: `${u}-${l}` },
                    (0, i.Uw)(u, s, e).map((e, u) =>
                      n().createElement(r.Fragment, { key: `${u}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, u, t) => {
        "use strict";
        t.d(u, { Y: () => m });
        var r = t(3138),
          n = t(6179),
          s = t(1043),
          a = t(5262);
        const i = r.O.client.getSize("rem"),
          o = i.width,
          l = i.height,
          c = Object.assign({ width: o, height: l }, (0, a.T)(o, l, s.j)),
          m = (0, n.createContext)(c);
      },
      1039: (e, u, t) => {
        "use strict";
        var r = t(6179),
          n = t.n(r),
          s = t(6536),
          a = t(3495),
          i = t(1043),
          o = t(5262),
          l = t(3138);
        (0, r.memo)(({ children: e }) => {
          const u = (0, r.useContext)(a.Y),
            t = (0, r.useState)(u),
            c = t[0],
            m = t[1],
            d = (0, r.useCallback)((e, u) => {
              const t = l.O.view.pxToRem(e),
                r = l.O.view.pxToRem(u);
              m(Object.assign({ width: t, height: r }, (0, o.T)(t, r, i.j)));
            }, []);
          ((0, s.Z)(() => {
            engine.on("clientResized", d);
          }),
            (0, r.useEffect)(() => () => engine.off("clientResized", d), [d]));
          const E = (0, r.useMemo)(() => Object.assign({}, c), [c]);
          return n().createElement(a.Y.Provider, { value: E }, e);
        });
      },
      6010: (e, u, t) => {
        "use strict";
        var r = t(6179),
          n = t(7382),
          s = t(3495);
        const a = ["children"];
        const i = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                s = Object.keys(e);
              for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, a);
          const i = (0, r.useContext)(s.Y),
            o = i.extraLarge,
            l = i.large,
            c = i.medium,
            m = i.small,
            d = i.extraSmall,
            E = i.extraLargeWidth,
            _ = i.largeWidth,
            A = i.mediumWidth,
            D = i.smallWidth,
            F = i.extraSmallWidth,
            g = i.extraLargeHeight,
            B = i.largeHeight,
            C = i.mediumHeight,
            p = i.smallHeight,
            h = i.extraSmallHeight,
            f = { extraLarge: g, large: B, medium: C, small: p, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && o) return u;
            if (t.large && l) return u;
            if (t.medium && c) return u;
            if (t.small && m) return u;
            if (t.extraSmall && d) return u;
          } else {
            if (t.extraLargeWidth && E) return (0, n.H)(u, t, f);
            if (t.largeWidth && _) return (0, n.H)(u, t, f);
            if (t.mediumWidth && A) return (0, n.H)(u, t, f);
            if (t.smallWidth && D) return (0, n.H)(u, t, f);
            if (t.extraSmallWidth && F) return (0, n.H)(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && g) return u;
              if (t.largeHeight && B) return u;
              if (t.mediumHeight && C) return u;
              if (t.smallHeight && p) return u;
              if (t.extraSmallHeight && h) return u;
            }
          }
          return null;
        };
        i.defaultProps = {
          extraLarge: !1,
          large: !1,
          medium: !1,
          small: !1,
          extraSmall: !1,
          extraLargeWidth: !1,
          largeWidth: !1,
          mediumWidth: !1,
          smallWidth: !1,
          extraSmallWidth: !1,
          extraLargeHeight: !1,
          largeHeight: !1,
          mediumHeight: !1,
          smallHeight: !1,
          extraSmallHeight: !1,
        };
        (0, r.memo)(i);
      },
      7382: (e, u, t) => {
        "use strict";
        t.d(u, { H: () => r });
        const r = (e, u, t) =>
          u.extraLargeHeight ||
          u.largeHeight ||
          u.mediumHeight ||
          u.smallHeight ||
          u.extraSmallHeight
            ? (u.extraLargeHeight && t.extraLarge) ||
              (u.largeHeight && t.large) ||
              (u.mediumHeight && t.medium) ||
              (u.smallHeight && t.small) ||
              (u.extraSmallHeight && t.extraSmall)
              ? e
              : null
            : e;
      },
      7739: (e, u, t) => {
        "use strict";
        t.d(u, { YN: () => r.Y });
        (t(6010), t(1039));
        var r = t(3495);
      },
      1043: (e, u, t) => {
        "use strict";
        t.d(u, { j: () => r });
        const r = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, u, t) => {
        "use strict";
        var r;
        function n(e, u, t) {
          const r = (function (e, u) {
              switch (!0) {
                case e >= u.extraLarge.width:
                  return u.extraLarge.weight;
                case e >= u.large.width && e < u.extraLarge.width:
                  return u.large.weight;
                case e >= u.medium.width && e < u.large.width:
                  return u.medium.weight;
                case e >= u.small.width && e < u.medium.width:
                  return u.small.weight;
                default:
                  return u.extraSmall.weight;
              }
            })(e, t),
            n = (function (e, u) {
              switch (!0) {
                case e >= u.extraLarge.height:
                  return u.extraLarge.weight;
                case e >= u.large.height && e < u.extraLarge.height:
                  return u.large.weight;
                case e >= u.medium.height && e < u.large.height:
                  return u.medium.weight;
                case e >= u.small.height && e < u.medium.height:
                  return u.small.weight;
                default:
                  return u.extraSmall.weight;
              }
            })(u, t),
            s = Math.min(r, n);
          return {
            extraLarge: s === t.extraLarge.weight,
            large: s === t.large.weight,
            medium: s === t.medium.weight,
            small: s === t.small.weight,
            extraSmall: s === t.extraSmall.weight,
            extraLargeWidth: r === t.extraLarge.weight,
            largeWidth: r === t.large.weight,
            mediumWidth: r === t.medium.weight,
            smallWidth: r === t.small.weight,
            extraSmallWidth: r === t.extraSmall.weight,
            extraLargeHeight: n === t.extraLarge.weight,
            largeHeight: n === t.large.weight,
            mediumHeight: n === t.medium.weight,
            smallHeight: n === t.small.weight,
            extraSmallHeight: n === t.extraSmall.weight,
          };
        }
        (t.d(u, { T: () => n }),
          (function (e) {
            ((e.extraLarge = "extraLarge"),
              (e.large = "large"),
              (e.medium = "medium"),
              (e.small = "small"),
              (e.extraSmall = "extraSmall"),
              (e.extraLargeWidth = "extraLargeWidth"),
              (e.largeWidth = "largeWidth"),
              (e.mediumWidth = "mediumWidth"),
              (e.smallWidth = "smallWidth"),
              (e.extraSmallWidth = "extraSmallWidth"),
              (e.extraLargeHeight = "extraLargeHeight"),
              (e.largeHeight = "largeHeight"),
              (e.mediumHeight = "mediumHeight"),
              (e.smallHeight = "smallHeight"),
              (e.extraSmallHeight = "extraSmallHeight"));
          })(r || (r = {})));
      },
      2862: (e, u, t) => {
        "use strict";
        let r, n, s, a, i, o, l, c, m;
        (t.d(u, {
          $h: () => a,
          A2: () => o,
          E4: () => r,
          h2: () => s,
          kK: () => i,
          sh: () => l,
          ye: () => m,
        }),
          (function (e) {
            ((e.Items = "items"),
              (e.Equipment = "equipment"),
              (e.Xp = "xp"),
              (e.XpFactor = "xpFactor"),
              (e.Blueprints = "blueprints"),
              (e.BlueprintsAny = "blueprintsAny"),
              (e.Goodies = "goodies"),
              (e.Berths = "berths"),
              (e.Slots = "slots"),
              (e.Tokens = "tokens"),
              (e.CrewSkins = "crewSkins"),
              (e.CrewBooks = "crewBooks"),
              (e.Customizations = "customizations"),
              (e.CreditsFactor = "creditsFactor"),
              (e.Currency = "currency"),
              (e.TankmenXp = "tankmenXP"),
              (e.TankmenXpFactor = "tankmenXPFactor"),
              (e.FreeXpFactor = "freeXPFactor"),
              (e.BattleToken = "battleToken"),
              (e.PremiumUniversal = "premium_universal"),
              (e.Gold = "gold"),
              (e.Credits = "credits"),
              (e.Crystal = "crystal"),
              (e.FreeXp = "freeXP"),
              (e.Premium = "premium"),
              (e.PremiumPlus = "premium_plus"),
              (e.BattlePassPoints = "battlePassPoints"),
              (e.BattlePassSelectToken = "battlePassSelectToken"),
              (e.SelectableBonus = "selectableBonus"),
              (e.StyleProgressToken = "styleProgressToken"),
              (e.TmanToken = "tmanToken"),
              (e.NaturalCover = "naturalCover"),
              (e.BpCoin = "bpcoin"),
              (e.BattlaPassFinalAchievement = "dossier_achievement"),
              (e.BattleBadge = "dossier_badge"),
              (e.NewYearAlbumsAccess = "newYearAlbumsAccess"),
              (e.NewYearFillers = "ny22Fillers"),
              (e.NewYearInvoice = "newYearInvoice"),
              (e.NewYearToyFragments = "ny22ToyFragments"),
              (e.NewYearSlot = "newYearSlot"),
              (e.BonusX5 = "battle_bonus_x5"),
              (e.CrewBonusX3 = "crew_bonus_x3"),
              (e.Vehicles = "vehicles"),
              (e.EpicSelectToken = "epicSelectToken"),
              (e.CollectionItem = "collectionItem"),
              (e.Comp7TokenWeeklyReward = "comp7TokenWeeklyReward"),
              (e.Comp7TokenCouponReward = "comp7TokenCouponReward"),
              (e.BattleBoosterGift = "battleBooster_gift"),
              (e.CosmicLootboxSilver = "lootBoxToken"),
              (e.CosmicLootboxCommon = "cosmic_2024_2"),
              (e.Branch = "branch"),
              (e.VehicleSelect = "vehicleSelect"),
              (e.StyleProgress = "styleProgress"),
              (e.ParagonsUnlocks = "paragonsUnlocks"),
              (e.LootBoxToken = "lootBoxToken"),
              (e.PostStamp = "giftsystem_5_stamp"),
              (e.Quests = "quests"),
              (e.ArmoryCoin = "armory_coin"),
              (e.PremiumPlusUniversal = "premium_plus_universal"),
              (e.DogTagType = "dogTagComponents"),
              (e.GoldenTicket = "goldenticket"),
              (e.LbStyleProgress = "lbStyleProgress"),
              (e.RewardsSlots = "rewardsSlots"),
              (e.WtStamp = "stamp"),
              (e.WtHunter = "wt_hunter"),
              (e.WtBoss = "wt_boss"),
              (e.WtHunterCollection = "hunter_collection"),
              (e.WtTicket = "wtevent_ticket"),
              (e.WtMainPrizeDiscount = "main_prize_discount"),
              (e.WtTicket25 = "wtevent_ticket25"));
          })(r || (r = {})),
          (function (e) {
            ((e.Gold = "gold"),
              (e.Credits = "credits"),
              (e.Crystal = "crystal"),
              (e.Premium = "premium"),
              (e.PremiumPlus = "premium_plus"),
              (e.Vehicles = "vehicles"),
              (e.Customizations = "customizations"),
              (e.Blueprints = "blueprints"),
              (e.BlueprintsAny = "blueprintsAny"),
              (e.BlueprintsFinal = "finalBlueprints"),
              (e.Goodies = "goodies"),
              (e.CrewSkins = "crewSkins"),
              (e.Xp = "xp"),
              (e.XpFactor = "xpFactor"),
              (e.FreeXp = "freeXP"),
              (e.FreeXPFactor = "freeXPFactor"),
              (e.TankmenXP = "tankmenXP"),
              (e.TankmenXPFactor = "tankmenXPFactor"),
              (e.DailyXPFactor = "dailyXPFactor"),
              (e.CreditsFactor = "creditsFactor"),
              (e.Items = "items"),
              (e.StrBonus = "strBonus"),
              (e.Groups = "groups"),
              (e.Berths = "berths"),
              (e.Slots = "slots"),
              (e.Meta = "meta"),
              (e.Tokens = "tokens"),
              (e.Dossier = "dossier"),
              (e.OneOf = "oneof"),
              (e.PremiumUniversal = "premium_universal"),
              (e.BadgesGroup = "badgesGroup"),
              (e.Entitlements = "entitlements"),
              (e.RankedDailyBattles = "rankedDailyBattles"),
              (e.RankedBonusBattles = "rankedBonusBattles"),
              (e.BattlePassPoints = "battlePassPoints"),
              (e.BattleBadge = "dossier_badge"),
              (e.BattleAchievement = "dossier_achievement"));
          })(n || (n = {})),
          (function (e) {
            ((e.Big = "big"),
              (e.Small = "small"),
              (e.Mini = "mini"),
              (e.S600x450 = "s600x450"),
              (e.S400x300 = "s400x300"),
              (e.S296x222 = "s296x222"),
              (e.S232x174 = "s232x174"),
              (e.S180x135 = "s180x135"),
              (e.S128x100 = "s128x100"),
              (e.S80x80 = "s80x80"),
              (e.S48x48 = "s48x48"));
          })(s || (s = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(a || (a = {})),
          (function (e) {
            ((e.BATTLE_BOOSTER = "battleBooster"),
              (e.BATTLE_BOOSTER_REPLACE = "battleBoosterReplace"),
              (e.BUILT_IN_EQUIPMENT = "builtInEquipment"),
              (e.EQUIPMENT_PLUS = "equipmentPlus"),
              (e.EQUIPMENT_TROPHY_BASIC = "equipmentTrophyBasic"),
              (e.EQUIPMENT_TROPHY_UPGRADED = "equipmentTrophyUpgraded"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_1 = "equipmentModernized_1"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_2 = "equipmentModernized_2"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_3 = "equipmentModernized_3"),
              (e.PROGRESSION_STYLE_UPGRADED_1 = "progressionStyleUpgraded_1"),
              (e.PROGRESSION_STYLE_UPGRADED_2 = "progressionStyleUpgraded_2"),
              (e.PROGRESSION_STYLE_UPGRADED_3 = "progressionStyleUpgraded_3"),
              (e.PROGRESSION_STYLE_UPGRADED_4 = "progressionStyleUpgraded_4"));
          })(i || (i = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(o || (o = {})),
          (function (e) {
            ((e.BATTLE_BOOSTER = "battleBooster"),
              (e.BATTLE_BOOSTER_REPLACE = "battleBoosterReplace"),
              (e.BUILT_IN_EQUIPMENT = "builtInEquipment"),
              (e.EQUIPMENT_PLUS = "equipmentPlus"),
              (e.EQUIPMENT_TROPHY_BASIC = "equipmentTrophyBasic"),
              (e.EQUIPMENT_TROPHY_UPGRADED = "equipmentTrophyUpgraded"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_1 = "equipmentModernized_1"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_2 = "equipmentModernized_2"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_3 = "equipmentModernized_3"),
              (e.PROGRESSION_STYLE_UPGRADED_1 = "progressionStyleUpgraded_1"),
              (e.PROGRESSION_STYLE_UPGRADED_2 = "progressionStyleUpgraded_2"),
              (e.PROGRESSION_STYLE_UPGRADED_3 = "progressionStyleUpgraded_3"),
              (e.PROGRESSION_STYLE_UPGRADED_4 = "progressionStyleUpgraded_4"));
          })(l || (l = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(c || (c = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(m || (m = {})));
      },
      729: (e, u, t) => {
        "use strict";
        t.d(u, { L_: () => F, i2: () => g, m9: () => B, p3: () => d, pI: () => D, ry: () => A });
        var r = t(2372),
          n = t(6179),
          s = t.n(n),
          a = t(2862);
        const i = [
            a.E4.Items,
            a.E4.Equipment,
            a.E4.Xp,
            a.E4.XpFactor,
            a.E4.Blueprints,
            a.E4.BlueprintsAny,
            a.E4.Goodies,
            a.E4.Berths,
            a.E4.Slots,
            a.E4.Tokens,
            a.E4.CrewSkins,
            a.E4.CrewBooks,
            a.E4.Customizations,
            a.E4.CreditsFactor,
            a.E4.TankmenXp,
            a.E4.TankmenXpFactor,
            a.E4.FreeXpFactor,
            a.E4.BattleToken,
            a.E4.PremiumUniversal,
            a.E4.NaturalCover,
            a.E4.BpCoin,
            a.E4.BattlePassSelectToken,
            a.E4.BattlaPassFinalAchievement,
            a.E4.BattleBadge,
            a.E4.BonusX5,
            a.E4.CrewBonusX3,
            a.E4.NewYearFillers,
            a.E4.NewYearInvoice,
            a.E4.EpicSelectToken,
            a.E4.Comp7TokenWeeklyReward,
            a.E4.Comp7TokenCouponReward,
            a.E4.BattleBoosterGift,
            a.E4.CosmicLootboxCommon,
            a.E4.CosmicLootboxSilver,
            a.E4.SelectableBonus,
            a.E4.PostStamp,
            a.E4.PremiumPlusUniversal,
            a.E4.GoldenTicket,
            a.E4.RewardsSlots,
            a.E4.WtStamp,
            a.E4.WtTicket,
            a.E4.WtMainPrizeDiscount,
            a.E4.WtHunter,
            a.E4.WtHunterCollection,
          ],
          o = [a.E4.Gold, a.E4.Credits, a.E4.Crystal, a.E4.FreeXp],
          l = [a.E4.BattlePassPoints],
          c = [a.E4.PremiumPlus, a.E4.Premium];
        let m;
        !(function (e) {
          ((e.s16 = "16"),
            (e.s32 = "32"),
            (e.s48 = "48"),
            (e.s66 = "66"),
            (e.s80 = "80"),
            (e.s116 = "116"),
            (e.s296 = "296"),
            (e.s360 = "360"),
            (e.s400 = "400"),
            (e.s600 = "600"));
        })(m || (m = {}));
        const d = (e) =>
            i.includes(e)
              ? a.$h.MULTI
              : o.includes(e)
                ? a.$h.CURRENCY
                : l.includes(e)
                  ? a.$h.NUMBER
                  : c.includes(e)
                    ? a.$h.PREMIUM_PLUS
                    : a.$h.STRING,
          E = ["engravings", "backgrounds"],
          _ = ["engraving", "background"],
          A = (e, u = a.h2.Small) => {
            const t = e.name,
              r = e.type,
              n = e.value,
              s = e.icon,
              i = e.item,
              o = e.dogTagType,
              l = ((e) => {
                switch (e) {
                  case a.h2.S600x450:
                    return "c_600x450";
                  case a.h2.S400x300:
                    return "c_400x300";
                  case a.h2.S296x222:
                    return "c_296x222";
                  case a.h2.S232x174:
                    return "c_232x174";
                  case a.h2.Big:
                    return "c_80x80";
                  case a.h2.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (t) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${r}_${n}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${n}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${n}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${i}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${s}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case a.h2.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case a.h2.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${s}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const r = E[e];
                  if (r) {
                    const n = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(r),
                      s = n.$dyn(t);
                    return s ? `${s}` : `${n.$dyn(_[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, u, s);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${l}.${s}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case a.h2.S600x450:
                      return "c_600x450";
                    case a.h2.S400x300:
                      return "c_400x300";
                    case a.h2.S296x222:
                      return "c_296x222";
                    case a.h2.S232x174:
                      return "c_232x174";
                    case a.h2.S180x135:
                      return "big";
                    case a.h2.Big:
                    case a.h2.S80x80:
                      return "c_80x80";
                    case a.h2.Small:
                    case a.h2.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(u)}.${s}`;
              case "xp":
              case "xpFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.exp`;
              case "creditsFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.credits`;
              case "tankmenXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.tankmenXP`;
              case "dailyXPFactor":
              case "freeXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.freeXP`;
              case "tmanToken":
              case "battlePassSelectToken":
              case "selectableBonus":
              case "groups":
              case "lootBoxToken":
              case "customizations":
              case "crewSkins":
              case "goodies":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${s}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${l}.${s}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case a.h2.Mini:
                      return m.s32;
                    case a.h2.Small:
                    case a.h2.S48x48:
                      return m.s48;
                    case a.h2.S80x80:
                    case a.h2.Big:
                      return m.s80;
                    case a.h2.S128x100:
                      return m.s116;
                    case a.h2.S180x135:
                    case a.h2.S232x174:
                    case a.h2.S296x222:
                      return m.s296;
                    case a.h2.S400x300:
                      return m.s400;
                    case a.h2.S600x450:
                      return m.s600;
                  }
                })(u)}`;
              case a.E4.StyleProgress:
              case a.E4.LbStyleProgress:
                return C(s, u, a.ye.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}`;
            }
          },
          D = (e, u, t) => {
            const r = u && { contentId: u };
            return Object.assign(
              {
                args: e,
                isEnabled: Boolean((e && e.tooltipId) || u),
                ignoreMouseClick: !0,
                ignoreShowDelay: !u,
              },
              r,
              t,
            );
          },
          F = (e) => {
            if (void 0 === e) return null;
            switch (e) {
              case a.kK.BATTLE_BOOSTER:
              case a.kK.BATTLE_BOOSTER_REPLACE:
                return a.A2.BATTLE_BOOSTER;
            }
          },
          g = (e) => {
            if (void 0 === e) return null;
            switch (e) {
              case a.kK.BATTLE_BOOSTER:
                return a.sh.BATTLE_BOOSTER;
              case a.kK.BATTLE_BOOSTER_REPLACE:
                return a.sh.BATTLE_BOOSTER_REPLACE;
              case a.kK.BUILT_IN_EQUIPMENT:
                return a.sh.BUILT_IN_EQUIPMENT;
              case a.kK.EQUIPMENT_PLUS:
                return a.sh.EQUIPMENT_PLUS;
              case a.kK.EQUIPMENT_TROPHY_BASIC:
                return a.sh.EQUIPMENT_TROPHY_BASIC;
              case a.kK.EQUIPMENT_TROPHY_UPGRADED:
                return a.sh.EQUIPMENT_TROPHY_UPGRADED;
              case a.kK.EQUIPMENT_MODERNIZED_UPGRADED_1:
                return a.sh.EQUIPMENT_MODERNIZED_UPGRADED_1;
              case a.kK.EQUIPMENT_MODERNIZED_UPGRADED_2:
                return a.sh.EQUIPMENT_MODERNIZED_UPGRADED_2;
              case a.kK.EQUIPMENT_MODERNIZED_UPGRADED_3:
                return a.sh.EQUIPMENT_MODERNIZED_UPGRADED_3;
              case a.kK.PROGRESSION_STYLE_UPGRADED_1:
                return a.sh.PROGRESSION_STYLE_UPGRADED_1;
              case a.kK.PROGRESSION_STYLE_UPGRADED_2:
                return a.sh.PROGRESSION_STYLE_UPGRADED_2;
              case a.kK.PROGRESSION_STYLE_UPGRADED_3:
                return a.sh.PROGRESSION_STYLE_UPGRADED_3;
              case a.kK.PROGRESSION_STYLE_UPGRADED_4:
                return a.sh.PROGRESSION_STYLE_UPGRADED_4;
            }
          },
          B = (e, u) => {
            if (void 0 === e) return null;
            switch (u) {
              case a.$h.MULTI: {
                const u = Number(e);
                return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
              }
              case a.$h.CURRENCY:
              case a.$h.NUMBER:
                return s().createElement(r.A, { format: "integral", value: Number(e) });
              case a.$h.PREMIUM_PLUS: {
                const u = Number(e);
                return isNaN(u) ? e : null;
              }
              default:
                return e;
            }
          },
          C = (e, u, t) => {
            const r = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              n = r.$dyn(e);
            return String(null != n ? n : r.$dyn(t));
          };
      },
      7613: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => b });
        var r = t(6483),
          n = t.n(r),
          s = t(3779),
          a = t(280),
          i = t(3532),
          o = t.n(i),
          l = t(9887),
          c = t.n(l),
          m = t(3377),
          d = t(6179),
          E = t.n(d),
          _ = t(3393);
        const A = [
          "text",
          "variant",
          "className",
          "color",
          "m",
          "mt",
          "mr",
          "mb",
          "ml",
          "style",
          "format",
        ];
        function D() {
          return (
            (D =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            D.apply(this, arguments)
          );
        }
        Object.keys(c());
        const F = Object.keys(o()),
          g = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          B = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          C = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          p = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          h =
            (Object.keys(p),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": g,
              "heading-H36": g,
              "heading-H28": B,
              "heading-H24": B,
              "heading-H24R": B,
              "heading-H22": B,
              "heading-H20R": B,
              "heading-H18": B,
              "heading-H15": C,
              "heading-H14": C,
              "paragraph-P24": B,
              "paragraph-P18": B,
              "paragraph-P16": B,
              "paragraph-P14": C,
              "paragraph-P12": C,
              "paragraph-P10": C,
            }),
          f =
            (Object.keys(h),
            (e) =>
              e
                ? ((e) => F.includes(e))(e)
                  ? { colorClassName: _.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          b = (0, m.ZP)((e) => {
            let u = e.text,
              t = e.variant,
              r = e.className,
              i = e.color,
              o = e.m,
              l = e.mt,
              c = void 0 === l ? o : l,
              m = e.mr,
              F = void 0 === m ? o : m,
              g = e.mb,
              B = void 0 === g ? o : g,
              C = e.ml,
              p = void 0 === C ? o : C,
              b = e.style,
              v = e.format,
              w = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, A);
            const S = (0, d.useMemo)(() => {
                const e = f(i),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, b, r), colorClassName: u };
              }, [b, i]),
              y = S.computedStyle,
              P = S.colorClassName;
            return E().createElement(
              s.ZP,
              D(
                {
                  className: n()(_.Z.base, t && _.Z[t], P, r),
                  style: y,
                  mt: !0 === c ? h[t || "paragraph-P16"].mt : c,
                  mr: !0 === F ? h[t || "paragraph-P16"].mr : F,
                  mb: !0 === B ? h[t || "paragraph-P16"].mb : B,
                  ml: !0 === p ? h[t || "paragraph-P16"].ml : p,
                },
                w,
              ),
              void 0 !== v ? E().createElement(a.z, D({}, v, { text: u })) : u,
            );
          });
      },
      7078: (e, u, t) => {
        "use strict";
        t.d(u, { t: () => o });
        var r = t(6179),
          n = t.n(r),
          s = t(2056);
        const a = ["children"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const o = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                s = Object.keys(e);
              for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, a);
          return n().createElement(
            s.u,
            i(
              {
                contentId:
                  R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                    "resId",
                  ),
                ignoreShowDelay: !0,
              },
              t,
            ),
            u,
          );
        };
      },
      3415: (e, u, t) => {
        "use strict";
        t.d(u, { l: () => l });
        var r = t(6179),
          n = t.n(r),
          s = t(7078),
          a = t(6373),
          i = t(2056);
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const l = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const r = n().createElement("div", { className: t }, e);
          if (u.header || u.body) return n().createElement(a.i, u, r);
          const l = u.contentId,
            c = u.args,
            m = null == c ? void 0 : c.contentId;
          return l || m
            ? n().createElement(i.u, o({}, u, { contentId: l || m }), r)
            : n().createElement(s.t, u, r);
        };
      },
      6373: (e, u, t) => {
        "use strict";
        t.d(u, { i: () => l });
        var r = t(2056),
          n = t(6179),
          s = t.n(n);
        const a = ["children", "body", "header", "note", "alert", "args"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const o = R.views.common.tooltip_window.simple_tooltip_content,
          l = (e) => {
            let u = e.children,
              t = e.body,
              l = e.header,
              c = e.note,
              m = e.alert,
              d = e.args,
              E = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, a);
            const _ = (0, n.useMemo)(() => {
              const e = Object.assign({}, d, { body: t, header: l, note: c, alert: m });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [m, t, l, c, d]);
            return s().createElement(
              r.u,
              i(
                {
                  contentId:
                    ((A = null == d ? void 0 : d.hasHtmlContent),
                    A ? o.SimpleTooltipHtmlContent("resId") : o.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: _,
                },
                E,
              ),
              u,
            );
            var A;
          };
      },
      2056: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => l });
        var r = t(7902),
          n = t(4179),
          s = t(6179);
        const a = [
          "children",
          "contentId",
          "args",
          "onMouseEnter",
          "onMouseLeave",
          "onMouseDown",
          "onClick",
          "ignoreShowDelay",
          "ignoreMouseClick",
          "decoratorId",
          "isEnabled",
          "targetId",
          "onShow",
          "onHide",
        ];
        function i(e) {
          return Object.entries(e || {}).map(([e, u]) => {
            const t = { __Type: "GFValueProxy", name: e };
            switch (typeof u) {
              case "number":
                t.number = u;
                break;
              case "boolean":
                t.bool = u;
                break;
              case "undefined":
                break;
              default:
                t.string = u.toString();
            }
            return t;
          });
        }
        const o = (e, u, t = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: n.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: r,
                },
                t,
              ),
            );
          },
          l = (e) => {
            let u = e.children,
              t = e.contentId,
              n = e.args,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onClick,
              E = e.ignoreShowDelay,
              _ = void 0 !== E && E,
              A = e.ignoreMouseClick,
              D = void 0 !== A && A,
              F = e.decoratorId,
              g = void 0 === F ? 0 : F,
              B = e.isEnabled,
              C = void 0 === B || B,
              p = e.targetId,
              h = void 0 === p ? 0 : p,
              f = e.onShow,
              b = e.onHide,
              v = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, a);
            const w = (0, s.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, s.useMemo)(() => h || (0, r.F)().resId, [h]),
              y = (0, s.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (o(t, g, { isMouseEvent: !0, on: !0, arguments: i(n) }, S),
                  f && f(),
                  (w.current.isVisible = !0));
              }, [t, g, n, S, f]),
              P = (0, s.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    o(t, g, { on: !1 }, S),
                    w.current.isVisible && b && b(),
                    (w.current.isVisible = !1));
                }
              }, [t, g, S, b]),
              R = (0, s.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(w.current.prevTarget) && P();
                  }, 200)));
              }, []);
            ((0, s.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", R, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", R, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, s.useEffect)(() => {
                !1 === C && P();
              }, [C, P]),
              (0, s.useEffect)(
                () => (
                  window.addEventListener("mouseleave", P),
                  () => {
                    (window.removeEventListener("mouseleave", P), P());
                  }
                ),
                [P],
              ));
            return C
              ? (0, s.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(y, _ ? 100 : 400)),
                            l && l(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (P(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === D && P(), null == d || d(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === D && P(), null == m || m(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    v,
                  ),
                )
              : u;
            var x;
          };
      },
      3532: (e) => {
        e.exports = {
          BLACK_REAL: "#000000",
          WHITE_REAL: "#FFFFFF",
          WHITE: "#F2F2F7",
          WHITE_ORANGE: "#FEFEEC",
          WHITE_SPANISH: "#E9E2BF",
          PAR: "#8C8C7E",
          PAR_SECONDARY: "#595950",
          PAR_TERTIARY: "#37362E",
          INFO_RED: "#FF0000",
          RED: "#FF2717",
          RED_DARK: "#B70000",
          YELLOW: "#FEAB34",
          ORANGE: "#EE7000",
          CREAM: "#FFDD99",
          BROWN: "#CBAC77",
          GREEN_BRIGHT: "#80D43A",
          GREEN: "#7AB300",
          GREEN_DARK: "#497212",
          BLUE_BOOSTER: "#CCFFFF",
          BLUE_TEAMKILLER: "#09E2FF",
          CRED: "#CED9D9",
          GOLD: "#FFC363",
          BOND: "#C9C9B6",
          PROM: "#A29B70",
        };
      },
      9887: (e) => {
        e.exports = {
          XS: "4rem",
          SM: "8rem",
          SMp: "10rem",
          MD: "16rem",
          MDp: "20rem",
          LG: "32rem",
          XL: "64rem",
        };
      },
      122: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => r });
        const r = (e, u) => {
          let t;
          const r = setTimeout(() => {
            t = e();
          }, u);
          return () => {
            ("function" == typeof t && t(), clearTimeout(r));
          };
        };
      },
      8246: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => i });
        var r = t(3138);
        function n(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return s(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return s(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var r = 0;
            return function () {
              return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function s(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, r = new Array(u); t < u; t++) r[t] = e[t];
          return r;
        }
        const a = (e) => (0 === e ? window : window.subViews.get(e));
        function i({
          initializer: e = !0,
          rootId: u = 0,
          getRoot: t = a,
          context: s = "model",
        } = {}) {
          const i = new Map();
          function o(e, u = 0) {
            viewEnv.removeDataChangedCallback(e, u)
              ? i.delete(e)
              : console.error("Can't remove callback by id:", e);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (e, u, t) => {
              t.forEach((u) => {
                const t = i.get(u);
                void 0 !== t && t(e);
              });
            });
          });
          const l = (e) => {
            const r = t(u),
              n = s.split(".").reduce((e, u) => e[u], r);
            return "string" != typeof e || 0 === e.length
              ? n
              : e.split(".").reduce((e, u) => {
                  const t = e[u];
                  return "function" == typeof t ? t.bind(e) : t;
                }, n);
          };
          return {
            subscribe: (t, n) => {
              const a = "string" == typeof n ? `${s}.${n}` : s,
                o = r.O.view.addModelObserver(a, u, !0);
              return (i.set(o, t), e && t(l(n)), o);
            },
            readByPath: l,
            createCallback: (e, u) => {
              const t = l(u);
              return (...u) => {
                t(e(...u));
              };
            },
            createCallbackNoArgs: (e) => {
              const u = l(e);
              return () => {
                u();
              };
            },
            dispose: function () {
              for (var e, t = n(i.keys()); !(e = t()).done;) {
                o(e.value, u);
              }
            },
            unsubscribe: o,
          };
        }
      },
      3215: (e, u, t) => {
        "use strict";
        t.d(u, { q: () => o });
        var r = t(4598),
          n = t(9174),
          s = t(6179),
          a = t.n(s),
          i = t(8246);
        const o = () => (e, u) => {
          const t = (0, s.createContext)({});
          return [
            function ({ mode: o = "real", options: l, children: c, mocks: m }) {
              const d = (0, s.useRef)([]),
                E = (t, s, a) => {
                  var o;
                  const l = i.U(s),
                    c =
                      "real" === t
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (o = null == a ? void 0 : a.getter) ? o : () => {},
                          }),
                    m = (e) =>
                      "mocks" === t ? (null == a ? void 0 : a.getter(e)) : c.readByPath(e),
                    E = (e) => d.current.push(e),
                    _ = e({
                      mode: t,
                      readByPath: m,
                      externalModel: c,
                      observableModel: {
                        array: (e, u) => {
                          const s = null != u ? u : m(e),
                            a = n.LO.box(s, { equals: r.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, n.aD)((e) => a.set(e)),
                                e,
                              ),
                            a
                          );
                        },
                        object: (e, u) => {
                          const s = null != u ? u : m(e),
                            a = n.LO.box(s, { equals: r.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, n.aD)((e) => a.set(e)),
                                e,
                              ),
                            a
                          );
                        },
                        primitives: (e, u) => {
                          const r = m(u);
                          if (Array.isArray(e)) {
                            const s = e.reduce((e, u) => ((e[u] = n.LO.box(r[u], {})), e), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, n.aD)((u) => {
                                    e.forEach((e) => {
                                      s[e].set(u[e]);
                                    });
                                  }),
                                  u,
                                ),
                              s
                            );
                          }
                          {
                            const s = e,
                              a = Object.entries(s),
                              i = a.reduce((e, [u, t]) => ((e[t] = n.LO.box(r[u], {})), e), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, n.aD)((e) => {
                                    a.forEach(([u, t]) => {
                                      i[t].set(e[u]);
                                    });
                                  }),
                                  u,
                                ),
                              i
                            );
                          }
                        },
                      },
                      cleanup: E,
                    }),
                    A = { mode: t, model: _, externalModel: c, cleanup: E };
                  return {
                    model: _,
                    controls: "mocks" === t && a ? a.controls(A) : u(A),
                    externalModel: c,
                    mode: t,
                  };
                },
                _ = (0, s.useRef)(!1),
                A = (0, s.useState)(o),
                D = A[0],
                F = A[1],
                g = (0, s.useState)(() => E(o, l, m)),
                B = g[0],
                C = g[1];
              return (
                (0, s.useEffect)(() => {
                  _.current ? C(E(D, l, m)) : (_.current = !0);
                }, [m, D, l]),
                (0, s.useEffect)(() => {
                  F(o);
                }, [o]),
                (0, s.useEffect)(
                  () => () => {
                    (B.externalModel.dispose(), d.current.forEach((e) => e()));
                  },
                  [B],
                ),
                a().createElement(t.Provider, { value: B }, c)
              );
            },
            () => (0, s.useContext)(t),
          ];
        };
      },
      7044: (e, u, t) => {
        "use strict";
        t.d(u, { f8: () => o, s_: () => n, wB: () => l, yR: () => s });
        var r = t(3649);
        (t(728), t(4179));
        const n = 1e3,
          s = 60,
          a = 60 * s,
          i = 24 * a;
        Date.now();
        function o(e = 0) {
          let u = e;
          const t = Math.trunc(u / i);
          u -= t * i;
          const r = Math.trunc(u / a);
          u -= r * a;
          const n = Math.trunc(u / s);
          return ((u -= n * s), { days: t, hours: r, minutes: n, seconds: u });
        }
        const l = (e, u = !0) =>
          e.days > 7 && u
            ? (0, r.WU)(R.strings.common.duration.days(), { days: e.days })
            : e.days >= 1
              ? 0 === e.hours
                ? (0, r.WU)(R.strings.common.duration.days(), { days: e.days })
                : `${(0, r.WU)(R.strings.common.duration.days(), { days: e.days })} ${(0, r.WU)(R.strings.common.duration.hours(), { hours: e.hours })}`
              : e.hours >= 1
                ? 0 === e.minutes
                  ? (0, r.WU)(R.strings.common.duration.hours(), { hours: e.hours })
                  : `${(0, r.WU)(R.strings.common.duration.hours(), { hours: e.hours })} ${(0, r.WU)(R.strings.common.duration.minutes(), { minutes: e.minutes })}`
                : (0, r.WU)(R.strings.common.duration.minutes(), { minutes: e.minutes || 1 });
      },
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => i, onResize: () => s }));
        var r = t(2472),
          n = t(1176);
        const s = (0, r.E)("clientResized"),
          a = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, n.R)(!1);
          }
          function t() {
            e.enabled && (0, n.R)(!0);
          }
          function r() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : (0, n.R)(!1);
          }
          const s = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let n = !0;
                  const s = `mouse${u}`,
                    i = a[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(s, o),
                    r(),
                    () => {
                      n &&
                        (i(), window.removeEventListener(s, o), (e.listeners -= 1), r(), (n = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, s, {
            disable() {
              ((e.enabled = !1), r());
            },
            enable() {
              ((e.enabled = !0), r());
            },
            enableOutside() {
              e.enabled && (0, n.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, n.R)(!1);
            },
          });
        })();
      },
      5959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => r,
            getMouseGlobalPosition: () => s,
            getSize: () => n,
            graphicsQuality: () => a,
          }));
        var r = t(527);
        function n(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function s(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const a = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, u, t) => {
        "use strict";
        function r(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => r });
      },
      2472: (e, u, t) => {
        "use strict";
        function r(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        t.d(u, { E: () => r });
      },
      3138: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => n });
        var r = t(5959);
        const n = { view: t(7641), client: r };
      },
      3722: (e, u, t) => {
        "use strict";
        function r(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function n(e, u, t) {
          return `url(${r(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => n, getTextureUrl: () => r }));
      },
      6112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => r });
        const r = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => n });
        var r = t(2472);
        const n = {
          onTextureFrozen: (0, r.E)("self.onTextureFrozen"),
          onTextureReady: (0, r.E)("self.onTextureReady"),
          onDomBuilt: (0, r.E)("self.onDomBuilt"),
          onLoaded: (0, r.E)("self.onLoaded"),
          onDisplayChanged: (0, r.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, r.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, r.E)("children.onAdded"),
            onLoaded: (0, r.E)("children.onLoaded"),
            onRemoved: (0, r.E)("children.onRemoved"),
            onAttached: (0, r.E)("children.onAttached"),
            onTextureReady: (0, r.E)("children.onTextureReady"),
            onRequestPosition: (0, r.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            addModelObserver: () => c,
            addPreloadTexture: () => i,
            children: () => r,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => s.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => b,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => v,
            getScale: () => D,
            getSize: () => d,
            getViewGlobalPosition: () => _,
            isClientAccessible: () => p,
            isEventHandled: () => f,
            isFocused: () => C,
            pxToRem: () => F,
            remToPx: () => g,
            resize: () => E,
            sendEvent: () => a.qP,
            setAnimateWindow: () => B,
            setEventHandled: () => h,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => m,
            whenTutorialReady: () => y,
          }));
        var r = t(3722),
          n = t(6112),
          s = t(6538),
          a = t(8566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, u, t, r = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, r);
        }
        function c(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function m(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function E(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function _(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: g(u.x), y: g(u.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function D() {
          return viewEnv.getScale();
        }
        function F(e) {
          return viewEnv.pxToRem(e);
        }
        function g(e) {
          return viewEnv.remToPx(e);
        }
        function B(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function p() {
          return viewEnv.isClientAccessible();
        }
        function h() {
          return viewEnv.setEventHandled();
        }
        function f() {
          return viewEnv.isEventHandled();
        }
        function b() {
          viewEnv.forceTriggerMouseMove();
        }
        function v() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(n.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === n.W[u]), e),
            {},
          ),
          S = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          y = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : s.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => l });
        const r = ["args"];
        const n = 2,
          s = 16,
          a = 32,
          i = 64,
          o = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const s = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    n = {},
                    s = Object.keys(e);
                  for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, r);
              return void 0 !== s
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((n = s),
                        Object.entries(n).map(([e, u]) => {
                          const t = "GFValueProxy";
                          switch (typeof u) {
                            case "number":
                              return { __Type: t, name: e, number: u };
                            case "boolean":
                              return { __Type: t, name: e, bool: u };
                            default:
                              return { __Type: t, name: e, string: u.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, a));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          l = {
            close(e) {
              o("popover" === e ? n : a);
            },
            minimize() {
              o(i);
            },
            move(e) {
              o(s, { isMouseEvent: !0, on: e });
            },
          };
      },
      4598: (e, u, t) => {
        "use strict";
        t.d(u, { jv: () => n, yR: () => r });
        function r(e) {
          return e;
        }
        function n() {
          return !1;
        }
        console.log;
      },
      7902: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => r });
        const r = (e = 1) => {
          const u = new Error().stack;
          let t,
            r = R.invalid("resId");
          return (
            u &&
              ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
              window.__feature &&
                window.__feature !== t &&
                window.subViews[t] &&
                (r = window.subViews[t].id)),
            { caller: t, stack: u, resId: r }
          );
        };
      },
      3377: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => c });
        var r = t(5415),
          n = t(6179),
          s = t.n(n);
        const a = ["xl", "lg", "md", "sm", "xs"],
          i = (e) => e.includes("_") && ((e) => a.includes(e))(e.split("_").at(-1)),
          o = [r.cJ.ExtraLarge, r.cJ.Large, r.cJ.Medium, r.cJ.Small, r.cJ.ExtraSmall],
          l = (e, u) =>
            Object.keys(e).reduce((t, r) => {
              if (r in t) return t;
              if (i(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const s = o.indexOf(u),
                  i = (-1 !== s ? a.slice(s) : [])
                    .map((e) => n + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  l = i ? e[i] : void 0;
                return ((t[n] = void 0 !== l ? l : e[n]), t);
              }
              const n = e[r];
              return (
                void 0 === n ||
                  ((e, u) => a.some((t) => void 0 !== u[`${e}_${t}`]))(r, e) ||
                  (t[r] = n),
                t
              );
            }, {}),
          c = (e, u = l) => {
            const t = (
              (e, u = l) =>
              (t) => {
                const a = (0, r.GS)().mediaSize,
                  i = (0, n.useMemo)(() => u(t, a), [t, a]);
                return s().createElement(e, i);
              }
            )(e, u);
            return s().memo((u) =>
              Object.keys(u).some((e) => i(e) && void 0 !== u[e])
                ? s().createElement(t, u)
                : s().createElement(e, u),
            );
          };
      },
      2344: (e, u, t) => {
        "use strict";
        t.d(u, { D9: () => a, au: () => i, tp: () => o });
        var r = t(2790),
          n = t(3469),
          s = t(2133);
        (t(579), t(5360), t(9056));
        const a = r.Z,
          i = n.Z,
          o = s.Z;
      },
      6536: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        var r = t(6179);
        const n = (e) => {
          const u = (0, r.useRef)(!1);
          u.current || (e(), (u.current = !0));
        };
      },
      3469: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        var r = t(7044),
          n = t(6179);
        const s = () => {},
          a = (e = 0, u, t = 0, a = s) => {
            const i = (0, n.useState)(e),
              o = i[0],
              l = i[1];
            return (
              (0, n.useEffect)(() => {
                if (e > 0) {
                  l(e);
                  const n = Date.now(),
                    s = u || (e > 2 * r.yR ? r.yR : 1),
                    i = setInterval(() => {
                      const u = e - Math.floor((Date.now() - n) / r.s_);
                      null !== t && u <= t ? (l(t), a && a(), clearInterval(i)) : l(u);
                    }, s * r.s_);
                  return () => {
                    clearInterval(i);
                  };
                }
                l(0);
              }, [e, u, t, a]),
              o
            );
          };
      },
      2133: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => s });
        var r = t(122),
          n = t(6179);
        const s = (e, u) => {
          const t = (0, n.useState)(e),
            s = t[0],
            a = t[1];
          return ((0, n.useEffect)(() => (0, r.F)(() => a(e), u), [e, u]), s);
        };
      },
      5415: (e, u, t) => {
        "use strict";
        t.d(u, { GS: () => l, cJ: () => a });
        var r = t(6179),
          n = t(7739),
          s = t(1043);
        let a, i, o;
        (!(function (e) {
          ((e[(e.ExtraSmall = s.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = s.j.small.width)] = "Small"),
            (e[(e.Medium = s.j.medium.width)] = "Medium"),
            (e[(e.Large = s.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = s.j.extraLarge.width)] = "ExtraLarge"));
        })(a || (a = {})),
          (function (e) {
            ((e[(e.ExtraSmall = s.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = s.j.small.width)] = "Small"),
              (e[(e.Medium = s.j.medium.width)] = "Medium"),
              (e[(e.Large = s.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = s.j.extraLarge.width)] = "ExtraLarge"));
          })(i || (i = {})),
          (function (e) {
            ((e[(e.ExtraSmall = s.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = s.j.small.height)] = "Small"),
              (e[(e.Medium = s.j.medium.height)] = "Medium"),
              (e[(e.Large = s.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = s.j.extraLarge.height)] = "ExtraLarge"));
          })(o || (o = {})));
        const l = () => {
          const e = (0, r.useContext)(n.YN),
            u = e.width,
            t = e.height,
            s = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return a.ExtraLarge;
                case e.large:
                  return a.Large;
                case e.medium:
                  return a.Medium;
                case e.small:
                  return a.Small;
                case e.extraSmall:
                  return a.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), a.ExtraSmall);
              }
            })(e),
            l = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return i.ExtraLarge;
                case e.largeWidth:
                  return i.Large;
                case e.mediumWidth:
                  return i.Medium;
                case e.smallWidth:
                  return i.Small;
                case e.extraSmallWidth:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(e),
            c = ((e) => {
              switch (!0) {
                case e.extraLargeHeight:
                  return o.ExtraLarge;
                case e.largeHeight:
                  return o.Large;
                case e.mediumHeight:
                  return o.Medium;
                case e.smallHeight:
                  return o.Small;
                case e.extraSmallHeight:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(e);
          return {
            mediaSize: s,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: u,
            remScreenHeight: t,
          };
        };
      },
      5360: (e, u, t) => {
        "use strict";
        t(6536);
        var r = t(4179);
        t(6179);
        r.Sw.instance;
        let n;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(n || (n = {}));
      },
      9056: (e, u, t) => {
        "use strict";
        var r = t(4179);
        t(6179);
        r.Sw.instance;
      },
      2790: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        var r = t(6179);
        const n = (e) => {
          const u = (0, r.useRef)();
          return (
            (0, r.useEffect)(() => {
              u.current = e;
            }, [e]),
            u.current
          );
        };
      },
      579: (e, u, t) => {
        "use strict";
        (t(3138), t(6179));
      },
      5521: (e, u, t) => {
        "use strict";
        let r, n;
        (t.d(u, { n: () => r }),
          (function (e) {
            ((e[(e.NONE = -1)] = "NONE"),
              (e[(e.ALT = 165)] = "ALT"),
              (e[(e.ENTER = 13)] = "ENTER"),
              (e[(e.ESCAPE = 27)] = "ESCAPE"),
              (e[(e.SPACE = 32)] = "SPACE"),
              (e[(e.END = 35)] = "END"),
              (e[(e.HOME = 36)] = "HOME"),
              (e[(e.ARROW_LEFT = 37)] = "ARROW_LEFT"),
              (e[(e.ARROW_UP = 38)] = "ARROW_UP"),
              (e[(e.ARROW_RIGHT = 39)] = "ARROW_RIGHT"),
              (e[(e.ARROW_DOWN = 40)] = "ARROW_DOWN"),
              (e[(e.NUM_PLUS = 107)] = "NUM_PLUS"),
              (e[(e.NUM_MINUS = 109)] = "NUM_MINUS"),
              (e[(e.PLUS = 187)] = "PLUS"),
              (e[(e.MINUS = 189)] = "MINUS"),
              (e[(e.PAGE_UP = 33)] = "PAGE_UP"),
              (e[(e.PAGE_DOWN = 34)] = "PAGE_DOWN"),
              (e[(e.BACKSPACE = 8)] = "BACKSPACE"),
              (e[(e.DELETE = 46)] = "DELETE"),
              (e[(e.TAB = 9)] = "TAB"),
              (e[(e.KEY_N = 78)] = "KEY_N"),
              (e[(e.KEY_0 = 48)] = "KEY_0"),
              (e[(e.KEY_1 = 49)] = "KEY_1"),
              (e[(e.KEY_2 = 50)] = "KEY_2"),
              (e[(e.KEY_3 = 51)] = "KEY_3"),
              (e[(e.KEY_4 = 52)] = "KEY_4"),
              (e[(e.KEY_5 = 53)] = "KEY_5"),
              (e[(e.KEY_6 = 54)] = "KEY_6"),
              (e[(e.KEY_7 = 55)] = "KEY_7"),
              (e[(e.KEY_8 = 56)] = "KEY_8"),
              (e[(e.KEY_9 = 57)] = "KEY_9"),
              (e[(e.CAPS_LOCK = 20)] = "CAPS_LOCK"),
              (e[(e.INSERT = 45)] = "INSERT"),
              (e[(e.F1 = 112)] = "F1"),
              (e[(e.F2 = 113)] = "F2"),
              (e[(e.F3 = 114)] = "F3"),
              (e[(e.F4 = 115)] = "F4"),
              (e[(e.F5 = 116)] = "F5"),
              (e[(e.F6 = 117)] = "F6"),
              (e[(e.F7 = 118)] = "F7"),
              (e[(e.F8 = 119)] = "F8"),
              (e[(e.F9 = 120)] = "F9"),
              (e[(e.F10 = 121)] = "F10"),
              (e[(e.F11 = 122)] = "F11"),
              (e[(e.F12 = 123)] = "F12"),
              (e[(e.SELECT = 93)] = "SELECT"),
              (e[(e.NUMPAD_0 = 96)] = "NUMPAD_0"),
              (e[(e.NUMPAD_1 = 97)] = "NUMPAD_1"),
              (e[(e.NUMPAD_2 = 98)] = "NUMPAD_2"),
              (e[(e.NUMPAD_3 = 99)] = "NUMPAD_3"),
              (e[(e.NUMPAD_4 = 100)] = "NUMPAD_4"),
              (e[(e.NUMPAD_5 = 101)] = "NUMPAD_5"),
              (e[(e.NUMPAD_6 = 102)] = "NUMPAD_6"),
              (e[(e.NUMPAD_7 = 103)] = "NUMPAD_7"),
              (e[(e.NUMPAD_8 = 104)] = "NUMPAD_8"),
              (e[(e.NUMPAD_9 = 105)] = "NUMPAD_9"),
              (e[(e.NUM_DECIMAL = 110)] = "NUM_DECIMAL"),
              (e[(e.STAR = 106)] = "STAR"),
              (e[(e.NUM_SLASH = 111)] = "NUM_SLASH"),
              (e[(e.FORWARD_SLASH = 191)] = "FORWARD_SLASH"),
              (e[(e.COMMA = 188)] = "COMMA"),
              (e[(e.DASH = 189)] = "DASH"),
              (e[(e.PERIOD = 190)] = "PERIOD"));
          })(r || (r = {})),
          (function (e) {
            ((e.ALT = "Alt"),
              (e.ALT_GRAPH = "AltGraph"),
              (e.CAPS_LOCK = "CapsLock"),
              (e.CONTROL = "Control"),
              (e.FN = "Fn"),
              (e.FN_LOCK = "FnLock"),
              (e.META = "Meta"),
              (e.NUM_LOCK = "NumLock"),
              (e.SCROLL_LOCK = "ScrollLock"),
              (e.SHIFT = "Shift"),
              (e.SYMBOL = "Symbol"),
              (e.SYMBOL_LOCK = "SymbolLock"));
          })(n || (n = {})));
      },
      5175: (e, u, t) => {
        "use strict";
        t.d(u, { Q: () => a, c: () => s });
        var r = t(9480);
        const n = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? r.map(e, (e) => ("object" == typeof e ? n(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? n(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, u]) => [e, "object" == typeof u ? n(u) : u]),
                    )
              : e,
          s = (e) => n(e),
          a = (e) =>
            r.map(e || [], (e) => (null !== e && "object" == typeof e ? Object.assign({}, e) : e));
      },
      9480: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            contains: () => _,
            every: () => o,
            filter: () => c,
            filterMap: () => b,
            find: () => h,
            findIndex: () => w,
            findIndexLast: () => S,
            findLast: () => p,
            get: () => n,
            includes: () => f,
            join: () => y,
            lastElement: () => F,
            lastIndex: () => A,
            lastIndexZero: () => D,
            map: () => i,
            mapExists: () => v,
            pop: () => E,
            push: () => m,
            reduce: () => P,
            set: () => d,
            slice: () => g,
            some: () => l,
            splice: () => C,
            tail: () => B,
            unsafeGet: () => s,
            unwrapItem: () => a,
          }));
        var r = t(8968);
        function n(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        const s = n;
        function a(e) {
          var u;
          return e && "value" in e && null != (u = e.constructor) && u.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function i(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, r) => u(null == e ? void 0 : e.value, t, r));
        }
        function o(e, u) {
          if (Array.isArray(e)) return e.every(u);
          for (let t = 0; t < e.length; t++) {
            if (!u(s(e, t), t, e)) return !1;
          }
          return !0;
        }
        function l(e, u) {
          if (Array.isArray(e)) return e.some(u);
          for (let t = 0; t < e.length; t++) {
            if (u(s(e, t), t, e)) return !0;
          }
          return !1;
        }
        function c(e, u) {
          if (Array.isArray(e)) return e.filter(u);
          const t = [];
          for (let n = 0; n < e.length; n++) {
            var r;
            const s = null == (r = e[n]) ? void 0 : r.value;
            u(s, n, e) && t.push(s);
          }
          return t;
        }
        function m(e, u) {
          if (Array.isArray(e)) return (e.push(u), e);
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function d(e, u, t) {
          if (Array.isArray(e)) return ((e[u] = t), e);
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function E(e, u = e.length - 1) {
          if (Array.isArray(e)) return e.splice(u, 1)[0];
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function _(e, u, t) {
          for (let r = 0; r < e.length; r++) {
            const n = s(e, r);
            if (t && t(n)) return !0;
            if (u === n) return !0;
          }
          return !1;
        }
        function A(e) {
          return e.length - 1;
        }
        function D(e) {
          return Math.max(0, e.length - 1);
        }
        function F(e) {
          if (0 !== e.length) return n(e, e.length - 1);
        }
        function g(e, u = 0, t = e.length - 1) {
          return {
            [Symbol.iterator]() {
              let r = Math.max(u, 0);
              const n = Math.min(t, D(e));
              return {
                next: function () {
                  if (r > n) return { done: !0, value: null };
                  const u = e[r++];
                  return u ? { value: a(u), done: !1 } : { done: !0, value: null };
                },
              };
            },
          };
        }
        function B(e, u) {
          return g(e, Math.max(0, e.length - 1 - u), A(e));
        }
        function C(e, u, t) {
          if (Array.isArray(e)) return e.splice(u, t);
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function p(e, u) {
          for (let t = e.length - 1; t >= 0; t--) {
            const r = a(e[t]);
            if (u(r, t, e)) return r;
          }
        }
        function h(e, u) {
          for (let t = 0; t < e.length; t++) {
            const r = a(e[t]);
            if (u(r, t, e)) return r;
          }
        }
        function f(e, u) {
          for (let t = 0; t < e.length; t++) {
            if (s(e, t) === u) return !0;
          }
          return !1;
        }
        function b(e, u, t) {
          const r = [];
          for (let n = 0; n < e.length; n++) {
            const a = s(e, n);
            u(a, n, e) && r.push(t(a, n, e));
          }
          return r;
        }
        function v(e, u) {
          return b(e, r.C, u);
        }
        function w(e, u) {
          for (let t = 0; t < e.length; t++) {
            if (u(s(e, t), t, e)) return t;
          }
        }
        function S(e, u) {
          for (let t = e.length - 1; t >= 0; t--) {
            if (u(s(e, t), t, e)) return t;
          }
        }
        function y(e, u = ",") {
          let t = "";
          for (let r = 0; r < e.length; r++) {
            r > 0 && (t += u);
            const n = s(e, r);
            t += null == n ? "" : String(n);
          }
          return t;
        }
        function P(e, u, t) {
          if (Array.isArray(e)) return e.reduce(u, t);
          let r = t;
          for (let t = 0; t < e.length; t++) {
            r = u(r, s(e, t), t, e);
          }
          return r;
        }
      },
      8968: (e, u, t) => {
        "use strict";
        function r(e) {
          return (
            !1 ===
            (function (e) {
              return null == e;
            })(e)
          );
        }
        t.d(u, { C: () => r });
      },
      7727: (e, u, t) => {
        "use strict";
        function r(e) {
          engine.call("PlaySound", e);
        }
        t.d(u, { G: () => r });
      },
      3649: (e, u, t) => {
        "use strict";
        let r;
        function n(e, u) {
          return e.replace(/\{\w+\}/g, (e) => String(u[e.slice(1, -1)]));
        }
        (t.d(u, { Uw: () => m, WU: () => n, v2: () => r }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(r || (r = {})));
        const s = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          a = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          i = (e, u, t = r.left) => e.split(u).reduce(t === r.left ? s : a, []),
          o = (() => {
            const e = new RegExp(
              /[\(\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?[ %\+\x2D-9A-Za-\{\}\xA0\xC0-\u0237\u2013\u2014\u2026]+[\)\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3002\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\uFF01\uFF0C\uFF1A\uFF1B\uFF1F\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?/gmu
                .source +
                "|" +
                /[\(\xAB\u201C\u275D][\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}][\0-\u2E7F\u2E9A\u2EF4-\u2EFF\u2FD6-\u3004\u3006\u3008-\u3020\u302A-\u3037\u303C-\u33FF\u4DC0-\u4DFF\uA000-\uF8FF\uFA6E\uFA6F\uFADA-\u{16FE1}\u{16FE4}-\u{16FEF}\u{16FF2}-\u{1FFFF}\u{2A6E0}-\u{2A6FF}\u{2B739}-\u{2B73F}\u{2B81E}\u{2B81F}\u{2CEA2}-\u{2CEAF}\u{2EBE1}-\u{2F7FF}\u{2FA1E}-\u{2FFFF}\u{3134B}-\u{10FFFF}]?|[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}][\0-\u2E7F\u2E9A\u2EF4-\u2EFF\u2FD6-\u3004\u3006\u3008-\u3020\u302A-\u3037\u303C-\u33FF\u4DC0-\u4DFF\uA000-\uF8FF\uFA6E\uFA6F\uFADA-\u{16FE1}\u{16FE4}-\u{16FEF}\u{16FF2}-\u{1FFFF}\u{2A6E0}-\u{2A6FF}\u{2B739}-\u{2B73F}\u{2B81E}\u{2B81F}\u{2CEA2}-\u{2CEAF}\u{2EBE1}-\u{2F7FF}\u{2FA1E}-\u{2FFFF}\u{3134B}-\u{10FFFF}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?[\)\xBB\u201D\u275E][\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?/gmu
                  .source +
                "|" +
                /[A-Za-z\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u052F\u0531-\u0556\u0559\u0560-\u0588\u05D0-\u05EA\u05EF-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u0860-\u086A\u0870-\u0887\u0889-\u088E\u08A0-\u08C9\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u09FC\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0AF9\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D\u0C58-\u0C5A\u0C5D\u0C60\u0C61\u0C80\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D04-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D54-\u0D56\u0D5F-\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E86-\u0E8A\u0E8C-\u0EA3\u0EA5\u0EA7-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F5\u13F8-\u13FD\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16F1-\u16F8\u1700-\u1711\u171F-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1878\u1880-\u1884\u1887-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191E\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19B0-\u19C9\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4C\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1C80-\u1C88\u1C90-\u1CBA\u1CBD-\u1CBF\u1CE9-\u1CEC\u1CEE-\u1CF3\u1CF5\u1CF6\u1CFA\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2183\u2184\u2C00-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005\u3006\u3031-\u3035\u303B\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312F\u3131-\u318E\u31A0-\u31BF\u31F0-\u31FF\u3400-\u4DBF\u4E00-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA69D\uA6A0-\uA6E5\uA717-\uA71F\uA722-\uA788\uA78B-\uA7CA\uA7D0\uA7D1\uA7D3\uA7D5-\uA7D9\uA7F2-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA8FD\uA8FE\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uA9E0-\uA9E4\uA9E6-\uA9EF\uA9FA-\uA9FE\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA7E-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB69\uAB70-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC\u{10000}-\u{1000B}\u{1000D}-\u{10026}\u{10028}-\u{1003A}\u{1003C}\u{1003D}\u{1003F}-\u{1004D}\u{10050}-\u{1005D}\u{10080}-\u{100FA}\u{10280}-\u{1029C}\u{102A0}-\u{102D0}\u{10300}-\u{1031F}\u{1032D}-\u{10340}\u{10342}-\u{10349}\u{10350}-\u{10375}\u{10380}-\u{1039D}\u{103A0}-\u{103C3}\u{103C8}-\u{103CF}\u{10400}-\u{1049D}\u{104B0}-\u{104D3}\u{104D8}-\u{104FB}\u{10500}-\u{10527}\u{10530}-\u{10563}\u{10570}-\u{1057A}\u{1057C}-\u{1058A}\u{1058C}-\u{10592}\u{10594}\u{10595}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10600}-\u{10736}\u{10740}-\u{10755}\u{10760}-\u{10767}\u{10780}-\u{10785}\u{10787}-\u{107B0}\u{107B2}-\u{107BA}\u{10800}-\u{10805}\u{10808}\u{1080A}-\u{10835}\u{10837}\u{10838}\u{1083C}\u{1083F}-\u{10855}\u{10860}-\u{10876}\u{10880}-\u{1089E}\u{108E0}-\u{108F2}\u{108F4}\u{108F5}\u{10900}-\u{10915}\u{10920}-\u{10939}\u{10980}-\u{109B7}\u{109BE}\u{109BF}\u{10A00}\u{10A10}-\u{10A13}\u{10A15}-\u{10A17}\u{10A19}-\u{10A35}\u{10A60}-\u{10A7C}\u{10A80}-\u{10A9C}\u{10AC0}-\u{10AC7}\u{10AC9}-\u{10AE4}\u{10B00}-\u{10B35}\u{10B40}-\u{10B55}\u{10B60}-\u{10B72}\u{10B80}-\u{10B91}\u{10C00}-\u{10C48}\u{10C80}-\u{10CB2}\u{10CC0}-\u{10CF2}\u{10D00}-\u{10D23}\u{10E80}-\u{10EA9}\u{10EB0}\u{10EB1}\u{10F00}-\u{10F1C}\u{10F27}\u{10F30}-\u{10F45}\u{10F70}-\u{10F81}\u{10FB0}-\u{10FC4}\u{10FE0}-\u{10FF6}\u{11003}-\u{11037}\u{11071}\u{11072}\u{11075}\u{11083}-\u{110AF}\u{110D0}-\u{110E8}\u{11103}-\u{11126}\u{11144}\u{11147}\u{11150}-\u{11172}\u{11176}\u{11183}-\u{111B2}\u{111C1}-\u{111C4}\u{111DA}\u{111DC}\u{11200}-\u{11211}\u{11213}-\u{1122B}\u{11280}-\u{11286}\u{11288}\u{1128A}-\u{1128D}\u{1128F}-\u{1129D}\u{1129F}-\u{112A8}\u{112B0}-\u{112DE}\u{11305}-\u{1130C}\u{1130F}\u{11310}\u{11313}-\u{11328}\u{1132A}-\u{11330}\u{11332}\u{11333}\u{11335}-\u{11339}\u{1133D}\u{11350}\u{1135D}-\u{11361}\u{11400}-\u{11434}\u{11447}-\u{1144A}\u{1145F}-\u{11461}\u{11480}-\u{114AF}\u{114C4}\u{114C5}\u{114C7}\u{11580}-\u{115AE}\u{115D8}-\u{115DB}\u{11600}-\u{1162F}\u{11644}\u{11680}-\u{116AA}\u{116B8}\u{11700}-\u{1171A}\u{11740}-\u{11746}\u{11800}-\u{1182B}\u{118A0}-\u{118DF}\u{118FF}-\u{11906}\u{11909}\u{1190C}-\u{11913}\u{11915}\u{11916}\u{11918}-\u{1192F}\u{1193F}\u{11941}\u{119A0}-\u{119A7}\u{119AA}-\u{119D0}\u{119E1}\u{119E3}\u{11A00}\u{11A0B}-\u{11A32}\u{11A3A}\u{11A50}\u{11A5C}-\u{11A89}\u{11A9D}\u{11AB0}-\u{11AF8}\u{11C00}-\u{11C08}\u{11C0A}-\u{11C2E}\u{11C40}\u{11C72}-\u{11C8F}\u{11D00}-\u{11D06}\u{11D08}\u{11D09}\u{11D0B}-\u{11D30}\u{11D46}\u{11D60}-\u{11D65}\u{11D67}\u{11D68}\u{11D6A}-\u{11D89}\u{11D98}\u{11EE0}-\u{11EF2}\u{11FB0}\u{12000}-\u{12399}\u{12480}-\u{12543}\u{12F90}-\u{12FF0}\u{13000}-\u{1342E}\u{14400}-\u{14646}\u{16800}-\u{16A38}\u{16A40}-\u{16A5E}\u{16A70}-\u{16ABE}\u{16AD0}-\u{16AED}\u{16B00}-\u{16B2F}\u{16B40}-\u{16B43}\u{16B63}-\u{16B77}\u{16B7D}-\u{16B8F}\u{16E40}-\u{16E7F}\u{16F00}-\u{16F4A}\u{16F50}\u{16F93}-\u{16F9F}\u{16FE0}\u{16FE1}\u{16FE3}\u{17000}-\u{187F7}\u{18800}-\u{18CD5}\u{18D00}-\u{18D08}\u{1AFF0}-\u{1AFF3}\u{1AFF5}-\u{1AFFB}\u{1AFFD}\u{1AFFE}\u{1B000}-\u{1B122}\u{1B150}-\u{1B152}\u{1B164}-\u{1B167}\u{1B170}-\u{1B2FB}\u{1BC00}-\u{1BC6A}\u{1BC70}-\u{1BC7C}\u{1BC80}-\u{1BC88}\u{1BC90}-\u{1BC99}\u{1D400}-\u{1D454}\u{1D456}-\u{1D49C}\u{1D49E}\u{1D49F}\u{1D4A2}\u{1D4A5}\u{1D4A6}\u{1D4A9}-\u{1D4AC}\u{1D4AE}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D505}\u{1D507}-\u{1D50A}\u{1D50D}-\u{1D514}\u{1D516}-\u{1D51C}\u{1D51E}-\u{1D539}\u{1D53B}-\u{1D53E}\u{1D540}-\u{1D544}\u{1D546}\u{1D54A}-\u{1D550}\u{1D552}-\u{1D6A5}\u{1D6A8}-\u{1D6C0}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6FA}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D734}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D76E}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D7A8}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7CB}\u{1DF00}-\u{1DF1E}\u{1E100}-\u{1E12C}\u{1E137}-\u{1E13D}\u{1E14E}\u{1E290}-\u{1E2AD}\u{1E2C0}-\u{1E2EB}\u{1E7E0}-\u{1E7E6}\u{1E7E8}-\u{1E7EB}\u{1E7ED}\u{1E7EE}\u{1E7F0}-\u{1E7FE}\u{1E800}-\u{1E8C4}\u{1E900}-\u{1E943}\u{1E94B}\u{1EE00}-\u{1EE03}\u{1EE05}-\u{1EE1F}\u{1EE21}\u{1EE22}\u{1EE24}\u{1EE27}\u{1EE29}-\u{1EE32}\u{1EE34}-\u{1EE37}\u{1EE39}\u{1EE3B}\u{1EE42}\u{1EE47}\u{1EE49}\u{1EE4B}\u{1EE4D}-\u{1EE4F}\u{1EE51}\u{1EE52}\u{1EE54}\u{1EE57}\u{1EE59}\u{1EE5B}\u{1EE5D}\u{1EE5F}\u{1EE61}\u{1EE62}\u{1EE64}\u{1EE67}-\u{1EE6A}\u{1EE6C}-\u{1EE72}\u{1EE74}-\u{1EE77}\u{1EE79}-\u{1EE7C}\u{1EE7E}\u{1EE80}-\u{1EE89}\u{1EE8B}-\u{1EE9B}\u{1EEA1}-\u{1EEA3}\u{1EEA5}-\u{1EEA9}\u{1EEAB}-\u{1EEBB}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[ \):;\u2022\u3001\u3002\u300A-\u300D\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]|[\(,1A-Za-\{\}\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u052F\u0531-\u0556\u0559\u0560-\u0588\u05D0-\u05EA\u05EF-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u0860-\u086A\u0870-\u0887\u0889-\u088E\u08A0-\u08C9\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u09FC\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0AF9\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D\u0C58-\u0C5A\u0C5D\u0C60\u0C61\u0C80\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D04-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D54-\u0D56\u0D5F-\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E86-\u0E8A\u0E8C-\u0EA3\u0EA5\u0EA7-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F5\u13F8-\u13FD\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16F1-\u16F8\u1700-\u1711\u171F-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1878\u1880-\u1884\u1887-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191E\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19B0-\u19C9\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4C\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1C80-\u1C88\u1C90-\u1CBA\u1CBD-\u1CBF\u1CE9-\u1CEC\u1CEE-\u1CF3\u1CF5\u1CF6\u1CFA\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2183\u2184\u2C00-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005\u3006\u3031-\u3035\u303B\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312F\u3131-\u318E\u31A0-\u31BF\u31F0-\u31FF\u3400-\u4DBF\u4E00-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA69D\uA6A0-\uA6E5\uA717-\uA71F\uA722-\uA788\uA78B-\uA7CA\uA7D0\uA7D1\uA7D3\uA7D5-\uA7D9\uA7F2-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA8FD\uA8FE\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uA9E0-\uA9E4\uA9E6-\uA9EF\uA9FA-\uA9FE\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA7E-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB69\uAB70-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC\u{10000}-\u{1000B}\u{1000D}-\u{10026}\u{10028}-\u{1003A}\u{1003C}\u{1003D}\u{1003F}-\u{1004D}\u{10050}-\u{1005D}\u{10080}-\u{100FA}\u{10280}-\u{1029C}\u{102A0}-\u{102D0}\u{10300}-\u{1031F}\u{1032D}-\u{10340}\u{10342}-\u{10349}\u{10350}-\u{10375}\u{10380}-\u{1039D}\u{103A0}-\u{103C3}\u{103C8}-\u{103CF}\u{10400}-\u{1049D}\u{104B0}-\u{104D3}\u{104D8}-\u{104FB}\u{10500}-\u{10527}\u{10530}-\u{10563}\u{10570}-\u{1057A}\u{1057C}-\u{1058A}\u{1058C}-\u{10592}\u{10594}\u{10595}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10600}-\u{10736}\u{10740}-\u{10755}\u{10760}-\u{10767}\u{10780}-\u{10785}\u{10787}-\u{107B0}\u{107B2}-\u{107BA}\u{10800}-\u{10805}\u{10808}\u{1080A}-\u{10835}\u{10837}\u{10838}\u{1083C}\u{1083F}-\u{10855}\u{10860}-\u{10876}\u{10880}-\u{1089E}\u{108E0}-\u{108F2}\u{108F4}\u{108F5}\u{10900}-\u{10915}\u{10920}-\u{10939}\u{10980}-\u{109B7}\u{109BE}\u{109BF}\u{10A00}\u{10A10}-\u{10A13}\u{10A15}-\u{10A17}\u{10A19}-\u{10A35}\u{10A60}-\u{10A7C}\u{10A80}-\u{10A9C}\u{10AC0}-\u{10AC7}\u{10AC9}-\u{10AE4}\u{10B00}-\u{10B35}\u{10B40}-\u{10B55}\u{10B60}-\u{10B72}\u{10B80}-\u{10B91}\u{10C00}-\u{10C48}\u{10C80}-\u{10CB2}\u{10CC0}-\u{10CF2}\u{10D00}-\u{10D23}\u{10E80}-\u{10EA9}\u{10EB0}\u{10EB1}\u{10F00}-\u{10F1C}\u{10F27}\u{10F30}-\u{10F45}\u{10F70}-\u{10F81}\u{10FB0}-\u{10FC4}\u{10FE0}-\u{10FF6}\u{11003}-\u{11037}\u{11071}\u{11072}\u{11075}\u{11083}-\u{110AF}\u{110D0}-\u{110E8}\u{11103}-\u{11126}\u{11144}\u{11147}\u{11150}-\u{11172}\u{11176}\u{11183}-\u{111B2}\u{111C1}-\u{111C4}\u{111DA}\u{111DC}\u{11200}-\u{11211}\u{11213}-\u{1122B}\u{11280}-\u{11286}\u{11288}\u{1128A}-\u{1128D}\u{1128F}-\u{1129D}\u{1129F}-\u{112A8}\u{112B0}-\u{112DE}\u{11305}-\u{1130C}\u{1130F}\u{11310}\u{11313}-\u{11328}\u{1132A}-\u{11330}\u{11332}\u{11333}\u{11335}-\u{11339}\u{1133D}\u{11350}\u{1135D}-\u{11361}\u{11400}-\u{11434}\u{11447}-\u{1144A}\u{1145F}-\u{11461}\u{11480}-\u{114AF}\u{114C4}\u{114C5}\u{114C7}\u{11580}-\u{115AE}\u{115D8}-\u{115DB}\u{11600}-\u{1162F}\u{11644}\u{11680}-\u{116AA}\u{116B8}\u{11700}-\u{1171A}\u{11740}-\u{11746}\u{11800}-\u{1182B}\u{118A0}-\u{118DF}\u{118FF}-\u{11906}\u{11909}\u{1190C}-\u{11913}\u{11915}\u{11916}\u{11918}-\u{1192F}\u{1193F}\u{11941}\u{119A0}-\u{119A7}\u{119AA}-\u{119D0}\u{119E1}\u{119E3}\u{11A00}\u{11A0B}-\u{11A32}\u{11A3A}\u{11A50}\u{11A5C}-\u{11A89}\u{11A9D}\u{11AB0}-\u{11AF8}\u{11C00}-\u{11C08}\u{11C0A}-\u{11C2E}\u{11C40}\u{11C72}-\u{11C8F}\u{11D00}-\u{11D06}\u{11D08}\u{11D09}\u{11D0B}-\u{11D30}\u{11D46}\u{11D60}-\u{11D65}\u{11D67}\u{11D68}\u{11D6A}-\u{11D89}\u{11D98}\u{11EE0}-\u{11EF2}\u{11FB0}\u{12000}-\u{12399}\u{12480}-\u{12543}\u{12F90}-\u{12FF0}\u{13000}-\u{1342E}\u{14400}-\u{14646}\u{16800}-\u{16A38}\u{16A40}-\u{16A5E}\u{16A70}-\u{16ABE}\u{16AD0}-\u{16AED}\u{16B00}-\u{16B2F}\u{16B40}-\u{16B43}\u{16B63}-\u{16B77}\u{16B7D}-\u{16B8F}\u{16E40}-\u{16E7F}\u{16F00}-\u{16F4A}\u{16F50}\u{16F93}-\u{16F9F}\u{16FE0}\u{16FE1}\u{16FE3}\u{17000}-\u{187F7}\u{18800}-\u{18CD5}\u{18D00}-\u{18D08}\u{1AFF0}-\u{1AFF3}\u{1AFF5}-\u{1AFFB}\u{1AFFD}\u{1AFFE}\u{1B000}-\u{1B122}\u{1B150}-\u{1B152}\u{1B164}-\u{1B167}\u{1B170}-\u{1B2FB}\u{1BC00}-\u{1BC6A}\u{1BC70}-\u{1BC7C}\u{1BC80}-\u{1BC88}\u{1BC90}-\u{1BC99}\u{1D400}-\u{1D454}\u{1D456}-\u{1D49C}\u{1D49E}\u{1D49F}\u{1D4A2}\u{1D4A5}\u{1D4A6}\u{1D4A9}-\u{1D4AC}\u{1D4AE}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D505}\u{1D507}-\u{1D50A}\u{1D50D}-\u{1D514}\u{1D516}-\u{1D51C}\u{1D51E}-\u{1D539}\u{1D53B}-\u{1D53E}\u{1D540}-\u{1D544}\u{1D546}\u{1D54A}-\u{1D550}\u{1D552}-\u{1D6A5}\u{1D6A8}-\u{1D6C0}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6FA}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D734}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D76E}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D7A8}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7CB}\u{1DF00}-\u{1DF1E}\u{1E100}-\u{1E12C}\u{1E137}-\u{1E13D}\u{1E14E}\u{1E290}-\u{1E2AD}\u{1E2C0}-\u{1E2EB}\u{1E7E0}-\u{1E7E6}\u{1E7E8}-\u{1E7EB}\u{1E7ED}\u{1E7EE}\u{1E7F0}-\u{1E7FE}\u{1E800}-\u{1E8C4}\u{1E900}-\u{1E943}\u{1E94B}\u{1EE00}-\u{1EE03}\u{1EE05}-\u{1EE1F}\u{1EE21}\u{1EE22}\u{1EE24}\u{1EE27}\u{1EE29}-\u{1EE32}\u{1EE34}-\u{1EE37}\u{1EE39}\u{1EE3B}\u{1EE42}\u{1EE47}\u{1EE49}\u{1EE4B}\u{1EE4D}-\u{1EE4F}\u{1EE51}\u{1EE52}\u{1EE54}\u{1EE57}\u{1EE59}\u{1EE5B}\u{1EE5D}\u{1EE5F}\u{1EE61}\u{1EE62}\u{1EE64}\u{1EE67}-\u{1EE6A}\u{1EE6C}-\u{1EE72}\u{1EE74}-\u{1EE77}\u{1EE79}-\u{1EE7C}\u{1EE7E}\u{1EE80}-\u{1EE89}\u{1EE8B}-\u{1EE9B}\u{1EEA1}-\u{1EEA3}\u{1EEA5}-\u{1EEA9}\u{1EEAB}-\u{1EEBB}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]/gmu
                  .source +
                "|" +
                /[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]/gmu
                  .source,
              "gum",
            );
            return (u) =>
              u
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(e);
          })(),
          l = ["zh_cn", "zh_sg", "zh_tw"],
          c = (e, u = r.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return l.includes(t)
              ? o(e)
              : ((e, u = r.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    s = e.replace(/&nbsp;/g, " ");
                  return (i(s, /( )/, u).forEach((e) => (t = t.concat(i(e, n, r.left)))), t);
                })(e, u);
          },
          m = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : c(e, u)));
      },
      728: (e, u, t) => {
        "use strict";
        let r;
        !(function (e) {
          ((e.SHORT_DATE = "short-date"),
            (e.SHORT_TIME = "short-time"),
            (e.SHORT_DATE_TIME = "short-date-time"),
            (e.FULL_DATE = "full-date"),
            (e.FULL_DATE_TIME = "full-date-time"),
            (e.MONTH = "month"),
            (e.MONTH_DATE = "month-date"),
            (e.DATE_MONTH = "date-month"),
            (e.MONTH_YEAR = "month-year"),
            (e.WEEK_DAY = "week-day"),
            (e.WEEK_DAY_TIME = "week-day-time"),
            (e.YEAR = "year"),
            (e.DATE_YEAR = "date-year"));
        })(r || (r = {}));
      },
      1358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => s });
        var r = t(3138);
        class n {
          constructor() {
            ((this._callbacks = void 0),
              (this._updateHandler = void 0),
              (this._views = void 0),
              (this.clearViewCallbacks = (e) => {
                this._views[e] &&
                  (this._views[e].forEach((e) => {
                    delete this._callbacks[e];
                  }),
                  delete this._views[e]);
              }),
              (this._callbacks = {}),
              (this._views = {}),
              (this._updateHandler = void 0));
          }
          static get instance() {
            return (window.__dataTracker || (window.__dataTracker = new n()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const s = r.O.view.addModelObserver(e, t, n);
            return (
              s > 0
                ? ((this._callbacks[s] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(s) : (this._views[t] = [s])))
                : console.error("Can't add callback for model:", e),
              s
            );
          }
          removeCallback(e, u = 0) {
            let t = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((t = viewEnv.removeDataChangedCallback(e, u)), delete this._callbacks[e]),
              t || console.error("Can't remove callback by id:", e),
              t
            );
          }
          _emmitDataChanged(e, u, t) {
            t.forEach((t) => {
              const r = this._callbacks[t];
              void 0 !== r && r(e, u);
            });
          }
        }
        n.__instance = void 0;
        const s = n;
      },
      7572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
        "use strict";
        __webpack_require__.d(__webpack_exports__, { Z: () => __WEBPACK_DEFAULT_EXPORT__ });
        var _DataTracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(1358),
          _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(4179);
        class ViewModel {
          constructor(path, watchingFields = []) {
            ((this.dataTracker = void 0),
              (this.modelPath = void 0),
              (this.callbacks = void 0),
              (this.data = void 0),
              (this._notifyObservers = () => {
                ((this.data = eval(this.modelPath)),
                  this.callbacks.forEach((e) => {
                    e(this.data);
                  }));
              }),
              (this.dataTracker = new _DataTracker__WEBPACK_IMPORTED_MODULE_0__.Z()),
              (this.modelPath = path),
              (this.callbacks = new Set()),
              (0, _index__WEBPACK_IMPORTED_MODULE_1__.ry)().then(() => {
                (this._addCallback(path),
                  watchingFields.forEach((e) => {
                    this._addCallback(path + "." + e);
                  }),
                  this._notifyObservers());
              }));
          }
          subscribe(e) {
            (this.callbacks.add(e), null !== this.data && void 0 !== this.data && e(this.data));
          }
          unsubscribe(e) {
            this.callbacks.delete(e);
          }
          destroy() {
            (this.dataTracker.clear(), this.callbacks.clear());
          }
          _addCallback(e) {
            this.dataTracker.addCallback(e, this._notifyObservers);
          }
        }
        const __WEBPACK_DEFAULT_EXPORT__ = ViewModel;
      },
      4179: (e, u, t) => {
        "use strict";
        t.d(u, { Sw: () => s.Z, B3: () => l, Z5: () => a, B0: () => o, ry: () => g });
        class r {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let r = e.target;
                  do {
                    if (r === u) return;
                    r = r.parentNode;
                  } while (r);
                  t();
                });
              }));
          }
          static get instance() {
            return (r.__instance || (r.__instance = new r()), r.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              r = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== r,
            )),
              this.removeMouseListener());
          }
          addMouseListener() {
            this._listenMouse ||
              (document.addEventListener("mousedown", this.onMouseDown), (this._listenMouse = !0));
          }
          removeMouseListener() {
            this._listenMouse &&
              0 === this.entries.length &&
              (document.removeEventListener("mousedown", this.onMouseDown),
              (this._listenMouse = !1));
          }
        }
        r.__instance = void 0;
        const n = r;
        var s = t(1358);
        const a = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          i = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, u, t) => userLocale.getTimeFormat(e, u, void 0 === t || t),
            getTimeString: (e, u, t) => userLocale.getTimeString(e, u, void 0 === t || t),
          };
        let o;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(o || (o = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = t(5521),
          _ = t(3138);
        const A = ["args"];
        function D(e, u, t, r, n, s, a) {
          try {
            var i = e[s](a),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(r, n);
        }
        const F = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          g = (function () {
            var e,
              u =
                ((e = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((e) => {
                      engine.on("Ready", e);
                    })
                  );
                }),
                function () {
                  var u = this,
                    t = arguments;
                  return new Promise(function (r, n) {
                    var s = e.apply(u, t);
                    function a(e) {
                      D(s, r, n, a, i, "next", e);
                    }
                    function i(e) {
                      D(s, r, n, a, i, "throw", e);
                    }
                    a(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          B = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                s = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    n = {},
                    s = Object.keys(e);
                  for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, A);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, s, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([e, u]) => {
                          const t = { __Type: "GFValueProxy", name: e };
                          switch (typeof u) {
                            case "number":
                              t.number = u;
                              break;
                            case "boolean":
                              t.bool = u;
                              break;
                            default:
                              t.string = u.toString();
                          }
                          return t;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, s));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var r;
          },
          C = () => B(o.CLOSE),
          p = (e, u) => {
            e.keyCode === E.n.ESCAPE && u();
          };
        var h = t(7572);
        const f = n.instance,
          b = {
            DataTracker: s.Z,
            ViewModel: h.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: m,
            DateFormatType: d,
            makeGlobalBoundingBox: F,
            sendMoveEvent: (e) => B(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => B(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              B(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, r, n = R.invalid("resId"), s) => {
              const a = _.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                m = i.width,
                d = i.height,
                E = {
                  x: _.O.view.pxToRem(l) + a.x,
                  y: _.O.view.pxToRem(c) + a.y,
                  width: _.O.view.pxToRem(m),
                  height: _.O.view.pxToRem(d),
                };
              B(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: r || R.invalid("resId"),
                targetID: n,
                direction: u,
                bbox: F(E),
                on: !0,
                args: s,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => p(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              p(e, C);
            },
            handleViewEvent: B,
            onBindingsReady: g,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(o.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(o.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(o.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const r in u)
                if (Object.prototype.hasOwnProperty.call(u, r)) {
                  const n = Object.prototype.toString.call(u[r]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = u[r];
                    t[r] = [];
                    for (let u = 0; u < n.length; u++) t[r].push({ value: e(n[u].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[r] = e(u[r]))
                      : (t[r] = u[r]);
                }
              return t;
            },
            ClickOutsideManager: f,
            SystemLocale: a,
            UserLocale: i,
          };
        window.ViewEnvHelper = b;
      },
      2263: (e, u, t) => {
        "use strict";
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => hu,
            Bar: () => Bu,
            DefaultScroll: () => pu,
            Direction: () => g,
            defaultSettings: () => B,
            useHorizontalScrollApi: () => au,
          }));
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => Hu,
            Bar: () => ku,
            Default: () => Iu,
            useVerticalScrollApi: () => p,
          }));
        var s = t(6179),
          a = t.n(s),
          i = t(6483),
          o = t.n(i);
        const l = (e, u, t) => (t < e ? e : t > u ? u : t),
          c = (e) => {
            let u,
              t = null;
            return (
              (t = requestAnimationFrame(() => {
                t = requestAnimationFrame(() => {
                  ((t = null), (u = e()));
                });
              })),
              () => {
                ("function" == typeof u && u(), null !== t && cancelAnimationFrame(t));
              }
            );
          };
        var m = t(3138);
        function d(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return E(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return E(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var r = 0;
            return function () {
              return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function E(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, r = new Array(u); t < u; t++) r[t] = e[t];
          return r;
        }
        const _ = [];
        function A(e) {
          const u = (0, s.useRef)(e);
          return (
            (0, s.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, s.useCallback)((...e) => (0, u.current)(...e), _)
          );
        }
        function D(e, u, t) {
          const r = (0, s.useMemo)(
            () =>
              (function (e, u, t, r) {
                let n,
                  s = !1,
                  a = 0;
                function i() {
                  n && clearTimeout(n);
                }
                function o(...o) {
                  const l = this,
                    c = Date.now() - a;
                  function m() {
                    ((a = Date.now()), t.apply(l, o));
                  }
                  s ||
                    (r && !n && m(),
                    i(),
                    void 0 === r && c > e
                      ? m()
                      : !0 !== u &&
                        (n = setTimeout(
                          r
                            ? function () {
                                n = void 0;
                              }
                            : m,
                          void 0 === r ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((r = t), (t = u), (u = void 0)),
                  (o.cancel = function () {
                    (i(), (s = !0));
                  }),
                  o
                );
              })(t, e),
            u,
          );
          return ((0, s.useEffect)(() => r.cancel, [r]), r);
        }
        var F = t(7030);
        let g;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(g || (g = {}));
        const B = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          C = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: r,
            getWrapperSize: n,
            triggerMouseMoveOnUpdate: a = !1,
          }) => {
            const i = (e, t) => {
              const r = u(e),
                n = r[0],
                s = r[1];
              return l(n, s, t);
            };
            return (o = {}) => {
              const l = o.settings,
                E = void 0 === l ? B : l,
                _ = (0, s.useRef)(null),
                g = (0, s.useRef)(null),
                C = (() => {
                  const e = (0, s.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    r = (e, t) => {
                      u(e).delete(t);
                    },
                    n = (e, ...t) => {
                      for (var r, n = d(u(e).values()); !(r = n()).done;) (0, r.value)(...t);
                    };
                  return (0, s.useMemo)(() => ({ on: t, off: r, trigger: n }), []);
                })(),
                p = D(
                  () => {
                    m.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                h = (0, F.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = _.current;
                    u && (t(u, e), C.trigger("change", e), a && p());
                  },
                  onRest: (e) => C.trigger("rest", e),
                  onStart: (e) => C.trigger("start", e),
                  onPause: (e) => C.trigger("pause", e),
                })),
                f = h[0],
                b = h[1],
                v = (0, s.useCallback)(
                  (e, u, t) => {
                    var r;
                    const n = f.scrollPosition.get(),
                      s = (null != (r = f.scrollPosition.goal) ? r : 0) - n;
                    return i(e, u * t + s + n);
                  },
                  [f.scrollPosition],
                ),
                w = (0, s.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const r = _.current;
                    r &&
                      b.start({
                        scrollPosition: i(r, e),
                        immediate: u,
                        reset: t,
                        config: E.animationConfig,
                        from: { scrollPosition: i(r, f.scrollPosition.get()) },
                      });
                  },
                  [b, E.animationConfig, f.scrollPosition],
                ),
                S = (0, s.useCallback)(
                  (e) => {
                    const u = _.current,
                      t = g.current;
                    if (!u || !t) return;
                    const r = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return n(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, E.step),
                      s = v(u, e, r);
                    w(s);
                  },
                  [w, v, E.step],
                ),
                y = (0, s.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && S(r(e)),
                      _.current && C.trigger("mouseWheel", e, f.scrollPosition, u(_.current)));
                  },
                  [f.scrollPosition, S, C],
                ),
                P = ((e, u = []) => {
                  const t = (0, s.useRef)(),
                    r = (0, s.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, s.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [r],
                    ),
                    r
                  );
                })(
                  () =>
                    c(() => {
                      const e = _.current;
                      e &&
                        (w(i(e, f.scrollPosition.goal), { immediate: !0 }),
                        C.trigger("resizeHandled"));
                    }),
                  [w, f.scrollPosition.goal],
                ),
                R = A(() => {
                  const e = _.current;
                  if (!e) return;
                  const u = i(e, f.scrollPosition.goal);
                  (u !== f.scrollPosition.goal && w(u, { immediate: !0 }),
                    C.trigger("recalculateContent"));
                });
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", P),
                  () => {
                    window.removeEventListener("resize", P);
                  }
                ),
                [P],
              );
              const x = (0, s.useCallback)((e) => C.trigger("isThumbDraggingChanged", e), [C]);
              return (0, s.useMemo)(
                () => ({
                  getWrapperSize: () => (g.current ? n(g.current) : void 0),
                  getContainerSize: () => (_.current ? e(_.current) : void 0),
                  getBounds: () =>
                    _.current
                      ? u(_.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: E.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: y,
                  applyScroll: w,
                  applyStepTo: S,
                  contentRef: _,
                  wrapperRef: g,
                  scrollPosition: b,
                  animationScroll: f,
                  recalculateContent: R,
                  handleIsThumbDragging: x,
                  events: { on: C.on, off: C.off },
                }),
                [f.scrollPosition, w, S, x, C.off, C.on, R, y, b, E.step.clampedArrowStepTimeout],
              );
            };
          },
          p = C({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? g.Next : g.Prev),
          });
        var h = t(7613),
          f = t(6373),
          b = t(122),
          v = t(2344),
          w = t(7727),
          S = t(8515);
        let y, P;
        (!(function (e) {
          ((e.Timer = "timer"),
            (e.Countdown = "countdown"),
            (e.Cooldown = "cooldown"),
            (e.None = "none"));
        })(y || (y = {})),
          (function (e) {
            ((e.Description = "description"),
              (e.Short = "short"),
              (e.Long = "long"),
              (e.Extended = "extended"));
          })(P || (P = {})));
        var x = t(7044);
        var T = t(3649);
        const N = "Countdown_base_fe",
          L = "Countdown_icon_8b",
          M = "Countdown_description_8d";
        var k = t(280);
        const O = (e) => e.toString().padStart(2, "0"),
          I = R.images.gui.maps.icons.components.countdown,
          H = (e, u) => {
            const t = 2 === u ? I.big : I;
            switch (e) {
              case y.Timer:
                return t.clock();
              case y.Countdown:
                return t.hourglass();
              case y.Cooldown:
                return t.lock();
            }
          },
          U = (0, s.memo)(
            ({
              duration: e,
              icon: u = y.Timer,
              style: t = P.Description,
              onTimeReached: r,
              className: n = "",
              classNames: i = {},
              labelFormat: l = "",
            }) => {
              const c = t !== P.Description ? 1 : void 0,
                d = (0, v.au)(e, c),
                E = (() => {
                  const e = (0, s.useState)(m.O.view.getScale()),
                    u = e[0],
                    t = e[1];
                  return (
                    (0, s.useEffect)(() => {
                      const e = () => {
                        t(m.O.view.getScale());
                      };
                      return (
                        window.addEventListener("resize", e),
                        () => {
                          window.removeEventListener("resize", e);
                        }
                      );
                    }, []),
                    u
                  );
                })();
              r && r[d] && r[d]();
              const _ = ((e, u) => {
                switch (u) {
                  case P.Description:
                    return (0, x.wB)(e);
                  case P.Short:
                    return `${O(e.minutes)}:${O(e.seconds)}`;
                  case P.Long:
                    return `${O(e.hours)}:${O(e.minutes)}:${O(e.seconds)}`;
                  case P.Extended:
                    return `${(0, T.WU)(R.strings.common.duration.days(), { days: e.days })} | ${O(e.hours)}:${O(e.minutes)}:${O(e.seconds)}`;
                }
              })((0, x.f8)(d), t);
              return a().createElement(
                "div",
                { className: o()(N, n) },
                u !== y.None &&
                  a().createElement("div", {
                    className: o()(L, i.icon),
                    style: { backgroundImage: `url('${H(u, E)}')` },
                  }),
                l
                  ? a().createElement(
                      "div",
                      { className: o()(M, i.text) },
                      a().createElement(k.z, { text: l, binding: { timerText: _ } }),
                    )
                  : a().createElement("div", { className: o()(M, i.text) }, _),
              );
            },
          ),
          W = "DailyCountdown_base_75",
          Q = "DailyCountdown_icon_2d",
          G = "DailyCountdown_countdownText_65",
          j = ({ timeToUpdate: e }) =>
            a().createElement(
              "div",
              { className: W },
              a().createElement(U, { duration: e, className: G, classNames: { icon: Q } }),
            );
        var $ = t(9922);
        const z = { type: "idle" };
        const q = {
          base: "ProgressBar_base_45",
          base__medium: "ProgressBar_base__medium_62",
          base__small: "ProgressBar_base__small_df",
          background: "ProgressBar_background_51",
          background__medium: "ProgressBar_background__medium_6e",
          background__small: "ProgressBar_background__small_46",
          lineWrapper: "ProgressBar_lineWrapper_6a",
        };
        let X, Y;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(X || (X = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(Y || (Y = {})));
        const Z = ({ size: e = X.Default, classMix: u }) =>
            a().createElement("div", { className: o()(q.background, q[`background__${e}`], u) }),
          K = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          V = ({ size: e }) => {
            const u = o()(K.base, K[`base__${e}`]);
            return a().createElement("div", { className: u });
          },
          J = {
            base: "ProgressLineImpose_base_80",
            base__disabled: "ProgressLineImpose_base__disabled_cc",
            base__finished: "ProgressLineImpose_base__finished_d4",
            base__withoutBounce: "ProgressLineImpose_base__withoutBounce_56",
            pattern: "ProgressLineImpose_pattern_1c",
            base__small: "ProgressLineImpose_base__small_55",
            gradient: "ProgressLineImpose_gradient_35",
            glow: "ProgressLineImpose_glow_a5",
            glow__left: "ProgressLineImpose_glow__left_d8",
          },
          ee = (0, s.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: r,
              isComplete: n,
              withoutBounce: s,
            }) => {
              const i = o()(
                  J.base,
                  J[`base__${e}`],
                  t && J.base__disabled,
                  n && J.base__finished,
                  s && J.base__withoutBounce,
                ),
                l = !t && !n;
              return a().createElement(
                "div",
                { className: i, style: r, ref: u },
                a().createElement("div", { className: J.pattern }),
                a().createElement("div", { className: J.gradient }),
                l && a().createElement(V, { size: e }),
              );
            },
          ),
          ue = ({ size: e, value: u, lineRef: t, disabled: r, onComplete: n }) => {
            const i = (0, s.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              o = 100 === u;
            return (
              (0, s.useEffect)(() => {
                o && n && n();
              }, [o, n]),
              a().createElement(ee, {
                size: e,
                disabled: r,
                baseStyles: i,
                isComplete: o,
                lineRef: t,
              })
            );
          };
        let te, re;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(te || (te = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(re || (re = {})));
        const ne = "ProgressBarDeltaSimple_base_6c",
          se = "ProgressBarDeltaSimple_delta_99",
          ae = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: n,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
            }) => {
              const c = i < r,
                m = (0, s.useState)(re.Idle),
                d = m[0],
                E = m[1],
                _ = d === re.In,
                A = d === re.End,
                D = d === re.Idle,
                F = (0, s.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                );
              ((0, s.useEffect)(() => {
                if (D && !t) {
                  const e = u;
                  return (0, b.F)(() => {
                    F(re.In);
                  }, e);
                }
              }, [F, t, D, u]),
                (0, s.useEffect)(() => {
                  if (_) {
                    const t = e + u;
                    return (0, b.F)(() => {
                      (o && o(), F(re.End));
                    }, t);
                  }
                }, [F, _, o, u, e]));
              const g = (0, s.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, u, e],
                ),
                B = (0, s.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, u, e],
                ),
                C = (0, s.useMemo)(
                  () => ({ width: `${Math.abs(r - i)}%`, left: `${c ? i : r}%` }),
                  [r, c, i],
                );
              return A
                ? null
                : a().createElement(
                    "div",
                    { className: ne, style: C },
                    a().createElement(
                      "div",
                      { style: D ? g : B, className: se },
                      a().createElement(V, { size: n }),
                    ),
                  );
            },
          ),
          ie = (0, s.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: n,
              isComplete: i,
              animationSettings: o,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const m = (0, s.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${o.line.duration}ms`,
                  transitionDelay: `${o.line.delay}ms`,
                }),
                [o.line.delay, o.line.duration, e],
              );
              return a().createElement(
                a().Fragment,
                null,
                a().createElement(ee, {
                  size: u,
                  lineRef: r,
                  disabled: n,
                  isComplete: i,
                  baseStyles: m,
                }),
                t >= 0 &&
                  a().createElement(ae, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    freezed: o.freezed,
                    from: t,
                    size: u,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          oe = "ProgressBarDeltaGrow_base_7e",
          le = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          ce = "ProgressBarDeltaGrow_glow_68",
          me = (e) => (e ? { left: 0 } : { right: 0 }),
          de = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          Ee = (e) => ({ transitionDuration: `${e}ms` }),
          _e = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: n,
              to: i,
              onEndAnimation: l,
              onChangeAnimationState: c,
              className: m,
            }) => {
              const d = i < r,
                E = (0, s.useState)(te.Idle),
                _ = E[0],
                A = E[1],
                D = _ === te.End,
                F = _ === te.Idle,
                g = _ === te.Grow,
                B = _ === te.Shrink,
                C = (0, s.useCallback)(
                  (e) => {
                    (A(e), c && c(e));
                  },
                  [c],
                ),
                p = (0, s.useCallback)(
                  (e, u) =>
                    (0, b.F)(() => {
                      C(e);
                    }, u),
                  [C],
                );
              (0, s.useEffect)(() => {
                if (!t)
                  return F
                    ? p(te.Grow, u)
                    : g
                      ? p(te.Shrink, e)
                      : B
                        ? p(te.End, e)
                        : void (D && l && l());
              }, [p, t, D, g, F, B, l, u, e]);
              const h = (0, s.useMemo)(
                  () => Object.assign({ width: "100%" }, Ee(e), me(d)),
                  [d, e],
                ),
                f = (0, s.useMemo)(() => Object.assign({ width: "0%" }, Ee(e), me(d)), [d, e]),
                v = (0, s.useMemo)(
                  () => Object.assign({ width: "0%" }, de(d, r), Ee(e)),
                  [r, d, e],
                ),
                w = (0, s.useMemo)(
                  () => Object.assign({ width: `${Math.abs(i - r)}%` }, de(d, r), Ee(e)),
                  [r, d, i, e],
                );
              if (D) return null;
              const S = o()(oe, m, d && 0 === i && le);
              return a().createElement(
                "div",
                { style: F ? v : w, className: S },
                a().createElement(
                  "div",
                  { style: B ? f : h, className: ce },
                  a().createElement(V, { size: n }),
                ),
              );
            },
          ),
          Ae = (0, s.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: n,
              isComplete: i,
              animationSettings: o,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const m = e < t,
                d = (0, s.useState)(!1),
                E = d[0],
                _ = d[1],
                A = (0, s.useCallback)(
                  (e) => {
                    (e === te.Shrink && _(!0), c && c(e));
                  },
                  [c],
                ),
                D = (0, s.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                F = (0, s.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return a().createElement(
                a().Fragment,
                null,
                a().createElement(ee, {
                  size: u,
                  lineRef: r,
                  disabled: n,
                  isComplete: i,
                  withoutBounce: m && 0 === e,
                  baseStyles: E ? F : D,
                }),
                t >= 0 &&
                  a().createElement(_e, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    onChangeAnimationState: A,
                    freezed: o.freezed,
                    onEndAnimation: l,
                    from: t,
                    size: u,
                    to: e,
                    className: o.delta.className,
                  }),
              );
            },
          ),
          De = ["onComplete", "onEndAnimation"];
        function Fe() {
          return (
            (Fe =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Fe.apply(this, arguments)
          );
        }
        const ge = (0, s.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              r = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  s = Object.keys(e);
                for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, De);
            const n = (0, s.useState)(!1),
              i = n[0],
              o = n[1],
              l = (0, s.useCallback)(() => {
                const e = 100 === r.to;
                (e !== i && o(e), e && u && u(), t && t());
              }, [i, u, t, r.to]);
            switch (r.animationSettings.type) {
              case Y.Simple:
                return a().createElement(ie, Fe({}, r, { onEndAnimation: l, isComplete: i }));
              case Y.Growing:
                return a().createElement(Ae, Fe({}, r, { onEndAnimation: l, isComplete: i }));
              default:
                return null;
            }
          }),
          Be = ["onEndAnimation"];
        function Ce() {
          return (
            (Ce =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Ce.apply(this, arguments)
          );
        }
        const pe = (0, s.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                s = Object.keys(e);
              for (r = 0; r < s.length; r++) ((t = s[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, Be);
          const r = (0, s.useRef)({}),
            n = (0, s.useCallback)(() => {
              ((r.current.from = void 0), u && u());
            }, [u]),
            i = "number" == typeof r.current.from ? r.current.from : t.from;
          return (
            (r.current.from = i),
            a().createElement(ge, Ce({}, t, { onEndAnimation: n, key: `${i}-${t.to}`, from: i }))
          );
        });
        function he() {
          return (
            (he =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            he.apply(this, arguments)
          );
        }
        const fe = (0, s.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: r,
              deltaFrom: n,
              animationSettings: s,
              onEndAnimation: i,
              onChangeAnimationState: o,
              onComplete: l,
            }) => {
              if (n === u)
                return a().createElement(ue, {
                  key: `${n}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: r,
                  onComplete: l,
                });
              const c = {
                from: n,
                to: u,
                size: e,
                lineRef: t,
                disabled: r,
                animationSettings: s,
                onComplete: l,
                onEndAnimation: i,
                onChangeAnimationState: o,
              };
              return s.withStack
                ? a().createElement(pe, c)
                : a().createElement(ge, he({ key: `${n}-${u}` }, c));
            },
          ),
          be = (e) => ({
            "--progress-base": `url(${e.bgImageBase})`,
            "--progress-line-base": e.line.bgColorBase,
            "--progress-line-disabled": e.line.bgColorDisabled,
            "--progress-line-finished": e.line.bgColorFinished,
            "--progress-pattern-base": `url(${e.pattern.bgImageBase})`,
            "--progress-pattern-disabled": `url(${e.pattern.bgImageDisabled})`,
            "--progress-pattern-finished": `url(${e.pattern.bgImageFinished})`,
            "--progress-glow": `url('${e.glow}')`,
            "--progress-glow-small": `url('${e.glowSmall}')`,
            "--progress-delta-color": e.delta.color,
            "--progress-delta-shadow": e.delta.shadow,
          }),
          ve = (e, u, t) => {
            if ("number" == typeof t) {
              return (l(0, u, t) / u) * 100;
            }
            return e;
          },
          we = {
            bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_grey",
            line: {
              bgColorBase: "#f50",
              bgColorDisabled: "transparent",
              bgColorFinished: "#59a011",
            },
            pattern: {
              bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_orange",
              bgImageDisabled: "R.images.gui.maps.icons.components.progress_bar.pattern_disabled",
              bgImageFinished: "R.images.gui.maps.icons.components.progress_bar.pattern_green",
            },
            glow: "R.images.gui.maps.icons.components.progress_bar.glow",
            glowSmall: "R.images.gui.maps.icons.components.progress_bar.glow_small",
            delta: {
              color: "#ffc",
              shadow:
                "0 0 4px 1px #ffaa0066, 0 0 9px 1px #ffaa0066, 0 0 12px 2px #ff550066, 0 0 12px 4px #ff000066",
            },
          },
          Se = {
            freezed: !1,
            withStack: !1,
            type: Y.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          ye = (0, s.memo)(
            ({
              maxValue: e = 100,
              theme: u = we,
              size: t = X.Default,
              animationSettings: r = Se,
              disabled: n = !1,
              withoutBackground: i = !1,
              progressBarBackgroundClassMix: c,
              value: m,
              deltaFrom: d,
              lineRef: E,
              onChangeAnimationState: _,
              onEndAnimation: A,
              onComplete: D,
            }) => {
              const F = ((e, u, t) =>
                (0, s.useMemo)(() => {
                  const r = (l(0, u, e) / u) * 100;
                  return { value: r, deltaFrom: ve(r, u, t) };
                }, [t, u, e]))(m, e, d);
              return a().createElement(
                "div",
                { className: o()(q.base, q[`base__${t}`]), style: be(u) },
                !i && a().createElement(Z, { size: t, classMix: c }),
                a().createElement(fe, {
                  size: t,
                  lineRef: E,
                  disabled: n,
                  value: F.value,
                  deltaFrom: F.deltaFrom,
                  animationSettings: r,
                  onEndAnimation: A,
                  onChangeAnimationState: _,
                  onComplete: D,
                }),
              );
            },
          );
        var Pe = t(5415);
        const Re = {
            [Pe.cJ.ExtraSmall]: {
              mainPagePaddingTop: 48,
              questDividerHeight: 50,
              questCard: {
                weeklyHeight: 120,
                dailyHeight: 110,
                weeklyMarginBottom: 10,
                dailyMarginBottom: 6,
              },
              questListMarginBottom: 10,
              footerHeight: 55,
              premiumBannerHeight: 248,
            },
            [Pe.cJ.Small]: {
              mainPagePaddingTop: 48,
              questDividerHeight: 50,
              questCard: {
                weeklyHeight: 120,
                dailyHeight: 110,
                weeklyMarginBottom: 10,
                dailyMarginBottom: 6,
              },
              questListMarginBottom: 10,
              footerHeight: 55,
              premiumBannerHeight: 248,
            },
            [Pe.cJ.Medium]: {
              mainPagePaddingTop: 58,
              questDividerHeight: 50,
              questCard: {
                weeklyHeight: 160,
                dailyHeight: 140,
                weeklyMarginBottom: 10,
                dailyMarginBottom: 6,
              },
              questListMarginBottom: 10,
              footerHeight: 65,
              premiumBannerHeight: 260,
            },
            [Pe.cJ.Large]: {
              mainPagePaddingTop: 78,
              questDividerHeight: 60,
              questCard: {
                weeklyHeight: 170,
                dailyHeight: 160,
                weeklyMarginBottom: 10,
                dailyMarginBottom: 6,
              },
              questListMarginBottom: 10,
              footerHeight: 78,
              premiumBannerHeight: 300,
            },
            [Pe.cJ.ExtraLarge]: {
              mainPagePaddingTop: 111,
              questDividerHeight: 60,
              questCard: {
                weeklyHeight: 170,
                dailyHeight: 160,
                weeklyMarginBottom: 10,
                dailyMarginBottom: 6,
              },
              questListMarginBottom: 10,
              footerHeight: 111,
              premiumBannerHeight: 300,
            },
          },
          xe = Se.delta.delay + Se.delta.duration + Se.line.delay + Se.line.duration,
          Te = 2e3,
          Ne = 500,
          Le = 0,
          Me = 500,
          ke = 300,
          Oe = Te + Ne,
          Ie = 500,
          He = 500,
          Ue = 500;
        var We = t(2862),
          Qe = t(3099),
          Ge = t(3215),
          je = t(4598),
          $e = t(9480),
          ze = t(5175),
          qe = t(9174);
        var Xe = t(3946),
          Ye = t(9153),
          Ze = t(3017),
          Ke = t(3509);
        const Ve = [Qe.N.Locked, Qe.N.Active],
          Je = (e, u, t, r) => {
            const n = u ? Re[t].premiumBannerHeight : 0;
            let s = Re[t].questListMarginBottom + n;
            const a = Re[t].questCard.dailyHeight + Re[t].questCard.dailyMarginBottom,
              i = Re[t].questDividerHeight - Re[t].questCard.dailyMarginBottom;
            return e.map((u, n) => {
              if (!n) return s;
              if (u === Qe.N.Active) return (s += a);
              if (u === Qe.N.Locked) return (s += r ? a : a - Re[t].questCard.dailyMarginBottom);
              const o = e.find((e) => e === Qe.N.Locked),
                l = ((e, u) => {
                  const t = e[u - 1],
                    r = e[u - 2];
                  return (
                    (t === Qe.N.Done || t === Qe.N.UndoneSubscription) &&
                    r !== Qe.N.Done &&
                    r !== Qe.N.UndoneSubscription
                  );
                })(e, n);
              return (s += o || l ? (l ? a + i + Re[t].questCard.dailyMarginBottom : a + i) : a);
            });
          },
          eu = [...Array(Ke.vW + 1)],
          uu = (e, u) => (u <= 1 ? e : 2 === u ? Qe.N.Active : 3 === u ? Qe.N.Locked : void 0),
          tu = (0, Ge.q)()(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  primitives: e.primitives(["currentTabIdx"]),
                  regular: e.object("regular"),
                  regularQuests: e.array("regular.quests", []),
                  premium: e.object("premium"),
                  premiumQuests: e.array("premium.quests", []),
                  epicQuest: e.object("epic"),
                  unseenQuests: e.object("unseenQuests"),
                  isRegularWindowLoaded: qe.LO.box(!1),
                  isPremiumWindowLoaded: qe.LO.box(!1),
                },
                t = (0, Xe.Om)(() => u.primitives.currentTabIdx.get()),
                r = (0, Xe.Om)((e = We.h2.Big) => c(e) === m(e)),
                n = (0, Xe.Om)(() => $e.find(a(), (e) => e.status !== Qe.N.Done)),
                s = (0, Xe.Om)((e) => {
                  var u, t, r, n, s;
                  let a;
                  var i, o;
                  e &&
                    e.bonusCondition &&
                    (null == (u = e.bonusCondition) || null == (t = u.items) ? void 0 : t.length) >=
                      1 &&
                    (a = $e.map(null == (i = e.bonusCondition) ? void 0 : i.items, je.yR));
                  e &&
                    (null == (r = e.postBattleCondition) || null == (n = r.items)
                      ? void 0
                      : n.length) >= 1 &&
                    (a = $e.map(null == (o = e.postBattleCondition) ? void 0 : o.items, je.yR));
                  return (a && (null == (s = a) ? void 0 : s.length)) > 0 ? a[0] : a;
                }),
                a = (0, Xe.Om)(
                  (e = We.h2.Big) => {
                    const t = u.isRegularWindowLoaded.get(),
                      r = u.regular.get().firstSeenNewBonusMissions && !t;
                    return (0, ze.c)(i()).map((t, n) =>
                      Object.assign({}, t, {
                        allRewards: [
                          ...(0, Ze.rl)(t.bonuses, t.id, e),
                          ...(0, Ze.rl)(t.subscriptionBonuses, t.id, e, !0),
                        ],
                        isQuestUnseen: (0, Ze.ix)(t, (0, ze.Q)(u.unseenQuests.get().unseenQuests)),
                        status: r ? uu(t.status, n) : t.status,
                      }),
                    );
                  },
                  { equals: je.jv },
                ),
                i = (0, Xe.Om)(
                  () => {
                    switch (t()) {
                      case Ye.g.DailyQuests:
                        return u.regularQuests.get();
                      case Ye.g.PremiumQuests:
                        return u.premiumQuests.get();
                      default:
                        return [];
                    }
                  },
                  { equals: je.jv },
                ),
                o = (0, Xe.Om)(
                  () => {
                    switch (t()) {
                      case Ye.g.DailyQuests:
                        return u.regular.get();
                      case Ye.g.PremiumQuests:
                        return u.premium.get();
                      default:
                        return [];
                    }
                  },
                  { equals: je.jv },
                ),
                l = (0, Xe.Om)(
                  (e = We.h2.Big) => {
                    var t;
                    return Object.assign({}, u.epicQuest.get(), {
                      allRewards: [
                        ...(0, Ze.rl)(u.epicQuest.get().bonuses, u.epicQuest.get().id, e),
                        ...(0, Ze.rl)(
                          null == (t = u.epicQuest.get()) ? void 0 : t.subscriptionBonuses,
                          u.epicQuest.get().id,
                          e,
                          !0,
                        ),
                      ],
                    });
                  },
                  { equals: je.jv },
                ),
                c = (0, Xe.Om)((e = We.h2.Big) => a(e).length),
                m = (0, Xe.Om)(
                  (e = We.h2.Big) =>
                    a(e).filter(
                      (e) => e.status === Qe.N.Done || e.status === Qe.N.UndoneSubscription,
                    ).length,
                ),
                d = (0, Xe.Om)(() => {
                  const e = n(),
                    u = s(e);
                  return null == u ? void 0 : u.descrData;
                }),
                E = (0, Xe.Om)(() => t() === Ye.g.PremiumQuests),
                _ = (0, Xe.Om)(() => {
                  const e = u.isPremiumWindowLoaded.get();
                  return (
                    E() &&
                    (!u.premium.get().hasPremiumAccount ||
                      (!e && u.premium.get().premMissionsTabDiscovered))
                  );
                });
              return Object.assign({}, u, {
                computes: {
                  getCurrentTabIndex: t,
                  getCurrentQuest: n,
                  getQuests: a,
                  getQuestsInfo: o,
                  getQuestsLength: c,
                  getCompletedlQuestLength: m,
                  getAllQuestsCompleted: r,
                  getConditions: s,
                  getConditionDescr: d,
                  getEpicQuests: l,
                  getCurrQuests: i,
                  isPremiumTab: E,
                  isPremiumBannerVisible: _,
                },
              });
            },
            ({ model: e, externalModel: u }) => {
              const t = (function (e) {
                const u = {};
                for (const t in e)
                  if (Object.prototype.hasOwnProperty.call(e, t)) {
                    const r = e[t];
                    u[t] = (0, qe.aD)(r);
                  }
                return u;
              })({
                onRegularWindowLoaded: () => e.isRegularWindowLoaded.set(!0),
                onPremiumWindowLoaded: () => e.isPremiumWindowLoaded.set(!0),
              });
              return Object.assign({}, t, {
                onReroll: u.createCallback((e) => ({ rerollPremium: e }), "onReroll"),
                onBuyPremium: u.createCallbackNoArgs("onBuyPremiumBtnClick"),
              });
            },
          ),
          ru = tu[0],
          nu = tu[1];
        function su(e, u, t = []) {
          const r = (0, s.useRef)(0),
            n = (0, s.useCallback)(() => window.clearInterval(r.current), t || []);
          (0, s.useEffect)(() => n, [n]);
          const a = (null != t ? t : []).concat([u]);
          return [
            (0, s.useCallback)((t) => {
              ((r.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, a),
            n,
          ];
        }
        const au = C({
            getBounds: (e) => {
              var u, t;
              return [
                0,
                e.offsetWidth -
                  (null != (u = null == (t = e.parentElement) ? void 0 : t.offsetWidth) ? u : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, u) => {
              e.style.transform = `translateX(-${u.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? g.Next : g.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          iu = "HorizontalBar_base_49",
          ou = "HorizontalBar_base__nonActive_82",
          lu = "HorizontalBar_leftButton_5f",
          cu = "HorizontalBar_rightButton_03",
          mu = "HorizontalBar_track_0d",
          du = "HorizontalBar_thumb_fd",
          Eu = "HorizontalBar_rail_32",
          _u = "disable",
          Au = { pending: !1, offset: 0 },
          Du = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          Fu = () => {},
          gu = (e, u) => Math.max(20, e.offsetWidth * u),
          Bu = (0, s.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = Du, onDrag: r = Fu }) => {
              const n = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                d = (0, s.useRef)(null),
                E = (0, s.useRef)(null),
                _ = e.stepTimeout || 100,
                D = (0, s.useState)(Au),
                F = D[0],
                B = D[1],
                C = (0, s.useCallback)(
                  (e) => {
                    (B(e),
                      E.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: E.current }));
                  },
                  [r],
                ),
                p = () => {
                  const u = d.current,
                    t = E.current,
                    r = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(r && u && t && n)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    a = Math.min(1, r / n),
                    o = l(0, 1, s / (n - r)),
                    c = (u.offsetWidth - gu(u, a)) * o;
                  ((t.style.transform = `translateX(${0 | c}px)`),
                    ((e) => {
                      if (i.current && m.current && d.current && E.current) {
                        if (0 === e)
                          return (i.current.classList.add(_u), void m.current.classList.remove(_u));
                        if (
                          ((u = d.current),
                          (t = E.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(_u), void m.current.classList.add(_u));
                        var u, t;
                        (i.current.classList.remove(_u), m.current.classList.remove(_u));
                      }
                    })(c));
                },
                h = A(() => {
                  ((() => {
                    const u = E.current,
                      t = d.current,
                      r = e.getWrapperSize(),
                      s = e.getContainerSize();
                    if (!(s && u && r && t)) return;
                    const a = Math.min(1, r / s);
                    ((u.style.width = `${gu(t, a)}px`),
                      (u.style.display = "flex"),
                      n.current &&
                        (1 === a ? n.current.classList.add(ou) : n.current.classList.remove(ou)));
                  })(),
                    p());
                });
              ((0, s.useEffect)(() => c(h)),
                (0, s.useEffect)(
                  () =>
                    c(() => {
                      const u = () => {
                        p();
                      };
                      let t = Fu;
                      const r = () => {
                        (t(), (t = c(h)));
                      };
                      return (
                        e.events.on("recalculateContent", h),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", r),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", h),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", r));
                        }
                      );
                    }),
                  [e],
                ),
                (0, s.useEffect)(() => {
                  if (!F.pending) return;
                  const u = (u) => {
                      var t;
                      const n = e.contentRef.current;
                      if (!n) return;
                      const s = d.current,
                        a = E.current;
                      if (!n || !s || !a) return;
                      const i = u.screenX - F.offset - s.getBoundingClientRect().x,
                        o = (i / s.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(n, o),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        r({ type: "dragging", thumb: a, thumbOffset: i, contentOffset: o }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), C(Au));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, F.offset, F.pending, r, C]));
              const f = su((u) => e.applyStepTo(u), _, [e]),
                b = f[0],
                v = f[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", v, !0),
                  () => document.removeEventListener("mouseup", v, !0)
                ),
                [v],
              );
              const S = (e) => {
                e.target.classList.contains(_u) || (0, w.G)("highlight");
              };
              return a().createElement(
                "div",
                { className: o()(iu, u.base), ref: n, onWheel: e.handleMouseWheel },
                a().createElement("div", {
                  className: o()(lu, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(_u) ||
                      0 !== e.button ||
                      ((0, w.G)("play"), b(g.Next));
                  },
                  onMouseUp: v,
                  ref: i,
                  onMouseEnter: S,
                }),
                a().createElement(
                  "div",
                  {
                    className: o()(mu, u.track),
                    onMouseDown: (u) => {
                      const r = E.current;
                      if (r && 0 === u.button)
                        if (((0, w.G)("play"), u.target === r))
                          C({ pending: !0, offset: u.screenX - r.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const r = E.current,
                              n = e.contentRef.current;
                            if (!r || !n) return;
                            const s = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + s * u);
                          })(u.screenX > r.getBoundingClientRect().x ? g.Prev : g.Next);
                        }
                    },
                    ref: d,
                    onMouseEnter: S,
                  },
                  a().createElement("div", { ref: E, className: o()(du, u.thumb) }),
                  a().createElement("div", { className: o()(Eu, u.rail) }),
                ),
                a().createElement("div", {
                  className: o()(cu, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(_u) ||
                      0 !== e.button ||
                      ((0, w.G)("play"), b(g.Prev));
                  },
                  onMouseUp: v,
                  ref: m,
                  onMouseEnter: S,
                }),
              );
            },
          ),
          Cu = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          pu = ({
            children: e,
            api: u,
            className: t,
            barClassNames: r,
            areaClassName: n,
            classNames: i,
            scrollClassName: l,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: o()(Cu.base, e.base) });
              }, [r]),
              E = (0, s.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return a().createElement(
              "div",
              { className: o()(Cu.defaultScroll, t), onWheel: u.handleMouseWheel },
              a().createElement(
                "div",
                { className: o()(Cu.defaultScrollArea, n) },
                a().createElement(hu, { className: l, api: E, classNames: i }, e),
              ),
              a().createElement(Bu, { getStepByRailClick: c, api: u, onDrag: m, classNames: d }),
            );
          },
          hu = ({ api: e, className: u, classNames: t, children: r, style: n }) => (
            (0, s.useEffect)(() => c(e.recalculateContent)),
            a().createElement(
              "div",
              { className: o()(Cu.base, u), style: n },
              a().createElement(
                "div",
                {
                  className: o()(Cu.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                a().createElement(
                  "div",
                  { className: o()(Cu.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          );
        ((hu.Bar = Bu),
          (hu.Default = pu),
          (hu.SeniorityAwards = ({ api: e, className: u, classNames: t, children: r }) => (
            (0, s.useEffect)(() => c(e.recalculateContent)),
            a().createElement(
              "div",
              { className: o()(Cu.base, u) },
              a().createElement(
                "div",
                { className: o()(Cu.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                a().createElement(
                  "div",
                  { className: o()(Cu.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          )));
        const fu = "VerticalBar_base_f3",
          bu = "VerticalBar_base__nonActive_42",
          vu = "VerticalBar_topButton_d7",
          wu = "VerticalBar_bottomButton_06",
          Su = "VerticalBar_track_df",
          yu = "VerticalBar_thumb_32",
          Pu = "VerticalBar_rail_43",
          Ru = "disable",
          xu = () => {},
          Tu = { pending: !1, offset: 0 },
          Nu = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          Lu = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          Mu = (e, u) => Math.max(20, e.offsetHeight * u),
          ku = (0, s.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = Nu, onDrag: r = xu }) => {
              const n = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                d = (0, s.useRef)(null),
                E = (0, s.useRef)(null),
                _ = e.stepTimeout || 100,
                D = (0, s.useState)(Tu),
                F = D[0],
                B = D[1],
                C = (0, s.useCallback)(
                  (e) => {
                    (B(e),
                      E.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: E.current }));
                  },
                  [r],
                ),
                p = A(() => {
                  const u = E.current,
                    t = d.current,
                    r = e.getWrapperSize(),
                    s = e.getContainerSize();
                  if (!(r && s && u && t)) return;
                  const a = Math.min(1, r / s);
                  return (
                    (u.style.height = `${Mu(t, a)}px`),
                    u.classList.add(yu),
                    n.current &&
                      (1 === a ? n.current.classList.add(bu) : n.current.classList.remove(bu)),
                    a
                  );
                }),
                h = A(() => {
                  const u = d.current,
                    t = E.current,
                    r = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(r && u && t && n)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    a = Math.min(1, r / n),
                    o = l(0, 1, s / (n - r)),
                    c = (u.offsetHeight - Mu(u, a)) * o;
                  ((t.style.transform = `translateY(${0 | c}px)`),
                    ((e) => {
                      if (i.current && m.current && d.current && E.current) {
                        if (0 === e)
                          return (i.current.classList.add(Ru), void m.current.classList.remove(Ru));
                        if (
                          ((u = d.current),
                          (t = E.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(Ru), void m.current.classList.add(Ru));
                        var u, t;
                        (i.current.classList.remove(Ru), m.current.classList.remove(Ru));
                      }
                    })(c));
                }),
                f = A(() => {
                  Lu(e, () => {
                    (p(), h());
                  });
                });
              ((0, s.useEffect)(() => c(f)),
                (0, s.useEffect)(() => {
                  const u = () => {
                    Lu(e, () => {
                      h();
                    });
                  };
                  let t = xu;
                  const r = () => {
                    (t(), (t = c(f)));
                  };
                  return (
                    e.events.on("recalculateContent", f),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", r),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", f),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", r));
                    }
                  );
                }, [e]),
                (0, s.useEffect)(() => {
                  if (!F.pending) return;
                  const u = (u) => {
                      Lu(e, (t) => {
                        const n = d.current,
                          s = E.current,
                          a = e.getContainerSize();
                        if (!n || !s || !a) return;
                        const i = u.screenY - F.offset - n.getBoundingClientRect().y,
                          o = (i / n.offsetHeight) * a;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, o),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          r({ type: "dragging", thumb: s, thumbOffset: i, contentOffset: o }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        C(Tu));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, F.offset, F.pending, r, C]));
              const b = su((u) => e.applyStepTo(u), _, [e]),
                v = b[0],
                S = b[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", S, !0),
                  () => document.removeEventListener("mouseup", S, !0)
                ),
                [S],
              );
              const y = (e) => {
                e.target.classList.contains(Ru) || (0, w.G)("highlight");
              };
              return a().createElement(
                "div",
                { className: o()(fu, u.base), ref: n, onWheel: e.handleMouseWheel },
                a().createElement("div", {
                  className: o()(vu, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ru) ||
                      0 !== e.button ||
                      ((0, w.G)("play"), v(g.Next));
                  },
                  ref: i,
                  onMouseEnter: y,
                }),
                a().createElement(
                  "div",
                  {
                    className: o()(Su, u.track),
                    onMouseDown: (u) => {
                      const r = E.current;
                      if (r && 0 === u.button)
                        if (((0, w.G)("play"), u.target === r))
                          (e.handleIsThumbDragging(!0),
                            C({ pending: !0, offset: u.screenY - r.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            E.current &&
                              Lu(e, (r) => {
                                if (!r) return;
                                const n = t(e),
                                  s = e.clampPosition(r, r.scrollTop + n * u);
                                e.applyScroll(s);
                              });
                          })(u.screenY > r.getBoundingClientRect().y ? g.Prev : g.Next);
                        }
                    },
                    ref: d,
                    onMouseEnter: y,
                  },
                  a().createElement("div", { ref: E, className: u.thumb }),
                  a().createElement("div", { className: o()(Pu, u.rail) }),
                ),
                a().createElement("div", {
                  className: o()(wu, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ru) ||
                      0 !== e.button ||
                      ((0, w.G)("play"), v(g.Prev));
                  },
                  onMouseUp: S,
                  ref: m,
                  onMouseEnter: y,
                }),
              );
            },
          ),
          Ou = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Iu = ({
            children: e,
            api: u,
            className: t,
            barClassNames: r,
            areaClassName: n,
            scrollClassName: i,
            scrollClassNames: l,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: o()(Ou.base, e.base) });
              }, [r]),
              E = (0, s.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return a().createElement(
              "div",
              { className: o()(Ou.defaultScroll, t), onWheel: u.handleMouseWheel },
              a().createElement(
                "div",
                { className: o()(Ou.area, n) },
                a().createElement(Hu, { className: i, classNames: l, api: E }, e),
              ),
              a().createElement(ku, { getStepByRailClick: c, api: u, onDrag: m, classNames: d }),
            );
          },
          Hu = ({ className: e, classNames: u, children: t, api: r }) => (
            (0, s.useEffect)(() => c(r.recalculateContent)),
            a().createElement(
              "div",
              { className: o()(Ou.base, e), ref: r.wrapperRef, onWheel: r.handleMouseWheel },
              a().createElement(
                "div",
                { className: o()(Ou.content, null == u ? void 0 : u.content), ref: r.contentRef },
                t,
              ),
            )
          );
        Hu.Default = Iu;
        const Uu = { Vertical: n, Horizontal: r };
        var Wu = t(3415),
          Qu = t(729);
        const Gu = {
            base: "Reward_base_ea",
            base__s48x48: "Reward_base__s48x48_46",
            base__small: "Reward_base__small_c0",
            base__s80x80: "Reward_base__s80x80_ce",
            base__big: "Reward_base__big_e5",
            base__s128x100: "Reward_base__s128x100_c3",
            base__s180x135: "Reward_base__s180x135_7c",
            base__s232x174: "Reward_base__s232x174_67",
            base__s296x222: "Reward_base__s296x222_78",
            base__s400x300: "Reward_base__s400x300_07",
            base__s600x450: "Reward_base__s600x450_f8",
            tooltipWrapper: "Reward_tooltipWrapper_b5",
            icon: "Reward_icon_df",
            overlay: "Reward_overlay_68",
            highlight: "Reward_highlight_36",
            image: "Reward_image_89",
            info: "Reward_info_72",
            info__multi: "Reward_info__multi_63",
            info__credits: "Reward_info__credits_ef",
            info__gold: "Reward_info__gold_36",
            info__crystal: "Reward_info__crystal_36",
            info__premiumTank: "Reward_info__premiumTank_d3",
            timer: "Reward_timer_d3",
          },
          ju = ({
            name: e,
            image: u,
            isPeriodic: t = !1,
            size: r = We.h2.Big,
            special: n,
            value: s,
            valueType: i,
            style: l,
            className: c,
            classNames: m,
            tooltipArgs: d,
            periodicIconTooltipArgs: E,
          }) => {
            const _ = (0, Qu.L_)(n),
              A = (0, Qu.i2)(n),
              D = (0, Qu.m9)(s, i);
            return a().createElement(
              "div",
              { className: o()(Gu.base, Gu[`base__${r}`], c), style: l },
              a().createElement(
                Wu.l,
                { tooltipArgs: d, className: Gu.tooltipWrapper },
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement(
                    "div",
                    { className: o()(Gu.image, null == m ? void 0 : m.image) },
                    _ &&
                      a().createElement("div", {
                        className: o()(Gu.highlight, null == m ? void 0 : m.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${r}.${_}_highlight)`,
                        },
                      }),
                    u &&
                      a().createElement("div", {
                        className: o()(Gu.icon, null == m ? void 0 : m.rewardIcon),
                        style: { backgroundImage: `url(${u})` },
                      }),
                    A &&
                      a().createElement("div", {
                        className: o()(Gu.overlay, null == m ? void 0 : m.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${r}.${A}_overlay)`,
                        },
                      }),
                  ),
                  D &&
                    a().createElement(
                      "div",
                      {
                        className: o()(
                          Gu.info,
                          Gu[`info__${e}`],
                          i === We.$h.MULTI && Gu.info__multi,
                          null == m ? void 0 : m.info,
                        ),
                      },
                      D,
                    ),
                ),
              ),
              t &&
                a().createElement(
                  Wu.l,
                  { tooltipArgs: E },
                  a().createElement("div", {
                    className: o()(Gu.timer, null == m ? void 0 : m.periodicIcon),
                  }),
                ),
            );
          },
          $u = "Progress_base_1a",
          zu = "Progress_base__completed_99",
          qu = "Progress_base__disabled_94",
          Xu = "Progress_currentProgress_a5",
          Yu = "Progress_maxProgress_27",
          Zu = (0, s.memo)(
            ({ current: e, max: u, completed: t, disabled: r = !1, classNames: n, className: s }) =>
              a().createElement(h.ZP, {
                text: R.strings.quests.dailyWidget.progress(),
                className: o()($u, t && zu, r && qu, s),
                format: {
                  binding: {
                    currentProgress: a().createElement(h.ZP, {
                      text: String(e),
                      className: o()(Xu, null == n ? void 0 : n.currentProgress),
                    }),
                    maxProgress: a().createElement(h.ZP, {
                      text: String(u),
                      className: o()(Yu, null == n ? void 0 : n.maxProgress),
                    }),
                  },
                },
              }),
          ),
          Ku = "QuestCard_base_ac",
          Vu = "QuestCard_base__weekly_15",
          Ju = "QuestCard_base__completed_34",
          et = "QuestCard_base__disabled_7e",
          ut = "QuestCard_border_eb",
          tt = "QuestCard_disableBackground_29",
          rt = "QuestCard_background_f3",
          nt = "QuestCard_base__enabled_f0",
          st = "QuestCard_enableText_00",
          at = "QuestCard_bubble_5e",
          it = "QuestCard_rerollBackground_ab",
          ot = "QuestCard_rerollBackground__visible_ca",
          lt = "QuestCard_header_bb",
          ct = "QuestCard_timerWrapper_9f",
          mt = "QuestCard_timer_e2",
          dt = "QuestCard_countdown_ef",
          Et = "QuestCard_headerDivider_9b",
          _t = "QuestCard_weekly_3e",
          At = "QuestCard_cardWrapper_62",
          Dt = "QuestCard_contentWrapper_a9",
          Ft = "QuestCard_content_55",
          gt = "QuestCard_content__hidden_e3",
          Bt = "QuestCard_description_5a",
          Ct = "QuestCard_progressWrapper_12",
          pt = "QuestCard_progressContainer_09",
          ht = "QuestCard_progress_74",
          ft = "QuestCard_currentProgress_19",
          bt = "QuestCard_maxProgress_0a",
          vt = "QuestCard_questIcon_c1",
          wt = "QuestCard_divider_fa",
          St = "QuestCard_rewards_95",
          yt = "QuestCard_rewardWrapper_9e",
          Pt = "QuestCard_rewardWrapper__appear_4b",
          Rt = "QuestCard_opacityContainer_5f",
          xt = "QuestCard_opacityContainer__unlock_a8",
          Tt = "QuestCard_rewardIcon_b9",
          Nt = "QuestCard_rewardIcon__unlock_f8",
          Lt = "QuestCard_subscriptionIcon_a9",
          Mt = "QuestCard_rewardInfo_08",
          kt = "QuestCard_rewardHighlight_0d",
          Ot = "QuestCard_rewardOverlay_dc",
          It = "QuestCard_rewardOverlay__unlock_c2",
          Ht = "QuestCard_animationSmoke_c6";
        function Ut() {
          return (
            (Ut =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Ut.apply(this, arguments)
          );
        }
        const Wt = R.strings.quests,
          Qt = ["battlePassPoints"],
          Gt = "idle",
          jt = "wait",
          $t = "flash",
          zt = (0, s.memo)(
            ({
              quest: e,
              conditions: u,
              disabledTooltipArgs: t,
              isEpic: r,
              isDisabled: n,
              isRerollAnimation: i,
              isUnlockAnimation: l,
              unlockPremiumAnimationState: c,
              position: m = 1,
            }) => {
              var d;
              const E = null != (d = (0, v.D9)(e)) ? d : e,
                _ = (0, v.tp)(e, Me),
                A = (0, v.tp)(u, Me),
                D = i ? _ : e,
                F = D.isFirstView,
                g = D.allRewards,
                B = D.icon,
                C = D.isActiveSubscription,
                p = D.status,
                S = D.countDown,
                y = D.isQuestUnseen,
                P = D.isCompleted,
                x = i ? A : u,
                T = x.earned,
                N = x.total,
                L = x.current,
                M = x.descrData,
                k = P ? N : L,
                O = e.status === Qe.N.UndoneSubscription,
                I = e.status === Qe.N.Done,
                H = (e) => !I && e.withSubscription && (!C || O),
                U = (0, s.useState)(!1),
                W = U[0],
                Q = U[1],
                G = (0, s.useState)(!1),
                $ = G[0],
                z = G[1],
                q = (0, s.useState)(Gt),
                Y = q[0],
                Z = q[1],
                K = (0, Pe.GS)().mediaSize >= Pe.cJ.Medium ? "c_80" : "c_48",
                V = ((p === Qe.N.Done || p === Qe.N.UndoneSubscription) && !W) || P,
                J = Boolean(n || Y !== Gt || (c && c !== qr.COMPLETED && c !== qr.IDLE)),
                ee = i && !J && !V,
                ue = (0, s.useMemo)(() => 0.2 * m, [m]);
              return (
                (0, s.useEffect)(() => {
                  ((e.status !== Qe.N.Done && e.status !== Qe.N.UndoneSubscription) ||
                    !E ||
                    (null == E ? void 0 : E.status) === Qe.N.Done ||
                    (null == E ? void 0 : E.status) === Qe.N.UndoneSubscription ||
                    (Q(!0), (0, w.G)(R.sounds.dq_widget_slide_in())),
                    (null != E && E.isActiveSubscription) ||
                      !e.isActiveSubscription ||
                      (z(!0), (0, w.G)(R.sounds.dq_subscription_reward_unlock())));
                }, [e, E]),
                (0, s.useEffect)(() => {
                  if ($)
                    return (0, b.F)(() => {
                      z(!1);
                    }, Ke.ji.unlockSubscriptionBonusDuration);
                }, [$]),
                (0, s.useEffect)(() => {
                  if (W)
                    return (0, b.F)(() => {
                      Q(!1);
                    }, xe);
                }, [W]),
                (0, s.useEffect)(() => {
                  l && Z(jt);
                }, [l]),
                (0, s.useEffect)(
                  () =>
                    Y === jt
                      ? (0, b.F)(() => {
                          ((0, w.G)(R.sounds.dq_widget_slide_in()), Z($t));
                        }, Ke.ji.unlockBonusQuestDelay)
                      : Y === $t
                        ? (0, b.F)(() => {
                            Z(Gt);
                          }, Ke.ji.unlockBonusQuestDuration)
                        : void 0,
                  [Y],
                ),
                r && !e.isEnabled
                  ? a().createElement(
                      f.i,
                      {
                        header: Wt.switch.isWeeklyEnabled(),
                        body: Wt.switch.isWeeklyEnabledTitle(),
                      },
                      a().createElement(
                        "div",
                        { className: o()(Ku, nt) },
                        a().createElement("div", { className: ut }),
                        a().createElement("div", { className: rt }),
                        a().createElement(h.ZP, {
                          text: Wt.switch.isWeeklyEnabled(),
                          className: st,
                        }),
                      ),
                    )
                  : a().createElement(
                      "div",
                      { className: o()(Ku, r && Vu, V && Ju, J && et) },
                      J && a().createElement(f.i, t, a().createElement("div", { className: tt })),
                      a().createElement("div", { className: ut }),
                      a().createElement("div", { className: rt }),
                      y && a().createElement("div", { className: at }),
                      a().createElement("div", {
                        className: o()(it, (ee || Y === $t || c === qr.QUESTS_UNLOCK) && ot),
                      }),
                      r &&
                        a().createElement(
                          a().Fragment,
                          null,
                          a().createElement(
                            "div",
                            { className: lt },
                            a().createElement(h.ZP, {
                              text: Wt.weeklyQuest.header.default(),
                              className: _t,
                            }),
                            a().createElement(
                              f.i,
                              {
                                header: Wt.weeklyQuest.countDown.tooltip.header(),
                                body: Wt.weeklyQuest.countDown.tooltip.body(),
                              },
                              a().createElement(
                                "div",
                                { className: ct },
                                a().createElement(h.ZP, {
                                  text: Wt.epicQuest.countDown.remainingText(),
                                  className: mt,
                                }),
                                a().createElement(
                                  "div",
                                  { className: dt },
                                  a().createElement(j, { timeToUpdate: S }),
                                ),
                              ),
                            ),
                          ),
                          a().createElement("div", { className: Et }),
                        ),
                      a().createElement(
                        "div",
                        { className: At },
                        a().createElement(
                          "div",
                          { className: Dt },
                          a().createElement(
                            "div",
                            { className: o()(Ft, ee && gt) },
                            !r && a().createElement(h.ZP, { text: M, className: Bt }),
                            a().createElement(
                              "div",
                              { className: Ct },
                              a().createElement(
                                "div",
                                { className: pt },
                                r
                                  ? a().createElement(h.ZP, {
                                      text: Wt.weeklyQuest.description.default(),
                                      className: Bt,
                                    })
                                  : a().createElement("div", {
                                      className: vt,
                                      style: {
                                        backgroundImage: `url(${R.images.gui.maps.icons.daily.icons.$dyn(`${K}_${B}`)})`,
                                      },
                                    }),
                                Boolean(N) &&
                                  a().createElement(Zu, {
                                    current: k,
                                    completed: V,
                                    max: N,
                                    className: ht,
                                    classNames: { currentProgress: ft, maxProgress: bt },
                                    disabled: n,
                                  }),
                              ),
                              Boolean(N) &&
                                a().createElement(ye, {
                                  disabled: J,
                                  size: r ? X.Medium : X.Small,
                                  value: k,
                                  deltaFrom: k - T,
                                  maxValue: N,
                                }),
                            ),
                          ),
                          a().createElement("div", { className: wt }),
                          a().createElement(
                            "div",
                            { className: St },
                            g.map((e, u) => {
                              const t = e.withSubscription && !C,
                                r = Qt.includes(e.name) && F,
                                n = $ && e.withSubscription;
                              return a().createElement(
                                "div",
                                {
                                  className: o()(yt, r && Pt),
                                  style: { animationDelay: `${ue}s, ${0.5 + ue}s` },
                                  key: `reward-wrapper-${u}`,
                                },
                                a().createElement(
                                  "div",
                                  { className: o()((t || n) && Rt, n && xt) },
                                  ((e, u, t) => {
                                    const r = u.withSubscription && !C,
                                      n = $ && u.withSubscription;
                                    return u.withSubscription && e
                                      ? a().createElement(
                                          a().Fragment,
                                          null,
                                          a().createElement(
                                            Wu.l,
                                            {
                                              tooltipArgs: {
                                                header: Wt.reward.tooltip.noAdditionReward(),
                                                body: Wt.reward.tooltip.simpleBody(),
                                              },
                                            },
                                            a().createElement(
                                              ju,
                                              Ut({}, u, {
                                                classNames: {
                                                  info: Mt,
                                                  rewardIcon: o()((H(u) || n) && Tt, n && Nt),
                                                },
                                              }),
                                            ),
                                          ),
                                          u.withSubscription &&
                                            a().createElement(
                                              a().Fragment,
                                              null,
                                              a().createElement("div", { className: Lt }),
                                              a().createElement("div", { className: kt }),
                                            ),
                                        )
                                      : a().createElement(
                                          a().Fragment,
                                          null,
                                          a().createElement(
                                            Wu.l,
                                            {
                                              tooltipArgs: !I &&
                                                u.withSubscription &&
                                                !C && {
                                                  contentId:
                                                    R.views.lobby.daily.tooltips.LockedSubscriptionBonusTooltip(
                                                      "resId",
                                                    ),
                                                },
                                              key: `quest-reward-${t}`,
                                            },
                                            a().createElement(
                                              ju,
                                              Ut({}, u, {
                                                classNames: {
                                                  info: Mt,
                                                  rewardIcon: o()(r && Tt, n && Nt),
                                                },
                                              }),
                                            ),
                                          ),
                                          u.withSubscription &&
                                            a().createElement(
                                              Wu.l,
                                              {
                                                tooltipArgs: {
                                                  contentId:
                                                    R.views.lobby.daily.tooltips.LockedSubscriptionBonusTooltip(
                                                      "resId",
                                                    ),
                                                  args: { isQuestDone: I },
                                                },
                                                key: `quest-reward-icon${t}`,
                                              },
                                              a().createElement(
                                                a().Fragment,
                                                null,
                                                a().createElement("div", { className: Lt }),
                                                a().createElement("div", { className: kt }),
                                              ),
                                            ),
                                        );
                                  })(O, e, u),
                                  r &&
                                    a().createElement("div", {
                                      className: Ht,
                                      style: { animationDelay: `${0.5 + ue}s` },
                                    }),
                                ),
                                a().createElement("div", {
                                  className: o()((H(e) || $) && Ot, $ && It),
                                }),
                              );
                            }),
                          ),
                        ),
                      ),
                    )
              );
            },
          ),
          qt = {
            base: "CButton_base_40",
            base__main: "CButton_base__main_42",
            base__primary: "CButton_base__primary_7f",
            base__primaryGreen: "CButton_base__primaryGreen_6f",
            base__primaryRed: "CButton_base__primaryRed_ec",
            base__secondary: "CButton_base__secondary_50",
            base__ghost: "CButton_base__ghost_ed",
            base__extraSmall: "CButton_base__extraSmall_27",
            base__small: "CButton_base__small_df",
            base__medium: "CButton_base__medium_74",
            base__disabled: "CButton_base__disabled_d9",
            back: "CButton_back_e5",
            texture: "CButton_texture_fe",
            state: "CButton_state_11",
            base__focus: "CButton_base__focus_83",
            stateHighlightHover: "CButton_stateHighlightHover_ff",
            stateHighlightActive: "CButton_stateHighlightActive_35",
            stateDisabled: "CButton_stateDisabled_54",
            base__firstHover: "CButton_base__firstHover_d5",
            base__highlightActive: "CButton_base__highlightActive_b2",
            content: "CButton_content_cc",
          };
        let Xt, Yt;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(Xt || (Xt = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(Yt || (Yt = {})));
        const Zt = ({
          children: e,
          size: u,
          isFocused: t,
          type: r,
          disabled: n,
          mixClass: i,
          soundHover: l,
          soundClick: c,
          onMouseEnter: m,
          onMouseMove: d,
          onMouseDown: E,
          onMouseUp: _,
          onMouseLeave: A,
          onClick: D,
        }) => {
          const F = (0, s.useRef)(null),
            g = (0, s.useState)(t),
            B = g[0],
            C = g[1],
            p = (0, s.useState)(!1),
            h = p[0],
            f = p[1],
            b = (0, s.useState)(!1),
            v = b[0],
            S = b[1],
            y = (0, s.useCallback)(() => {
              n || (F.current && (F.current.focus(), C(!0)));
            }, [n]),
            P = (0, s.useCallback)(
              (e) => {
                B && null !== F.current && !F.current.contains(e.target) && C(!1);
              },
              [B],
            ),
            x = (0, s.useCallback)(
              (e) => {
                n || (D && D(e));
              },
              [n, D],
            ),
            T = (0, s.useCallback)(
              (e) => {
                n || (null !== l && (0, w.G)(l), m && m(e), S(!0));
              },
              [n, l, m],
            ),
            N = (0, s.useCallback)(
              (e) => {
                d && d(e);
              },
              [d],
            ),
            L = (0, s.useCallback)(
              (e) => {
                n || (_ && _(e), f(!1));
              },
              [n, _],
            ),
            M = (0, s.useCallback)(
              (e) => {
                n || (null !== c && (0, w.G)(c), E && E(e), t && y(), f(!0));
              },
              [n, c, E, y, t],
            ),
            k = (0, s.useCallback)(
              (e) => {
                n || (A && A(e), f(!1));
              },
              [n, A],
            ),
            O = o()(
              qt.base,
              qt[`base__${r}`],
              {
                [qt.base__disabled]: n,
                [qt[`base__${u}`]]: u,
                [qt.base__focus]: B,
                [qt.base__highlightActive]: h,
                [qt.base__firstHover]: v,
              },
              i,
            ),
            I = o()(qt.state, qt.state__default);
          return (
            (0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", P),
                () => {
                  document.removeEventListener("mousedown", P);
                }
              ),
              [P],
            ),
            (0, s.useEffect)(() => {
              C(t);
            }, [t]),
            a().createElement(
              "div",
              {
                ref: F,
                className: O,
                onMouseEnter: T,
                onMouseMove: N,
                onMouseUp: L,
                onMouseDown: M,
                onMouseLeave: k,
                onClick: x,
              },
              r !== Xt.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: qt.back }),
                  a().createElement("span", { className: qt.texture }),
                ),
              a().createElement(
                "span",
                { className: I },
                a().createElement("span", { className: qt.stateDisabled }),
                a().createElement("span", { className: qt.stateHighlightHover }),
                a().createElement("span", { className: qt.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: qt.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Zt.defaultProps = {
          type: Xt.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Kt = (0, s.memo)(Zt),
          Vt = "PremiumBanner_base_d5",
          Jt = "PremiumBanner_glow1_e4",
          er = "PremiumBanner_base__hide_c6",
          ur = "PremiumBanner_glow2_e6",
          tr = "PremiumBanner_icon_9e",
          rr = "PremiumBanner_header_76",
          nr = "PremiumBanner_description_ce",
          sr = "PremiumBanner_button_9d",
          ar = R.strings.quests.premiumQuests.notPremiumAccount,
          ir = (0, s.memo)(({ onBuyPremium: e, hideBanner: u }) => {
            const t = (0, Pe.GS)().mediaSize >= Pe.cJ.Medium ? ar.paragraph() : ar.paragraphSmall();
            return a().createElement(
              "div",
              { className: o()(Vt, u && er) },
              a().createElement("div", { className: ur }),
              a().createElement("div", { className: Jt }),
              a().createElement("div", { className: tr }),
              a().createElement(h.ZP, { text: ar.title(), className: rr }),
              a().createElement(h.ZP, { text: t, className: nr }),
              a().createElement(
                Kt,
                {
                  type: Xt.main,
                  mixClass: sr,
                  onClick: () => {
                    ((0, w.G)(R.sounds.play()), e());
                  },
                },
                a().createElement(h.ZP, { text: ar.button() }),
              ),
            );
          }),
          or = "QuestCardBlock_base_bf",
          lr = "QuestCardBlock_base__divider_63",
          cr = "QuestCardBlock_base__blinkAnimation_dc",
          mr = "QuestCardBlock_divider_a9",
          dr = "QuestCardBlock_dividerBackground_62",
          Er = "QuestCardBlock_divider__completed_b7",
          _r = "QuestCardBlock_dividerContent_7a",
          Ar = "QuestCardBlock_dividerContent__hide_65",
          Dr = "QuestCardBlock_dividerIcon_aa",
          Fr = "QuestCardBlock_dividerDescription_64",
          gr = "QuestCardBlock_dividerMask_13",
          Br = "QuestCardBlock_progress_71",
          Cr = "QuestCardBlock_progress__disabled_a4",
          pr = "QuestCardBlock_currentProgress_be",
          hr = "QuestCardBlock_currentProgressItem_fb",
          fr = "QuestCardBlock_maxProgress_7a",
          br = "QuestCardBlock_dividerBottom_f2",
          vr = R.strings.quests;
        let wr;
        !(function (e) {
          ((e.IDLE = "idle"), (e.COMPLETE = "complete"), (e.BLINK = "blink"));
        })(wr || (wr = {}));
        const Sr = (0, S.Pi)(
            ({
              quest: e,
              prevQuestStatus: u,
              completedQuestsLength: t,
              position: r,
              isRerollAnimation: n,
              isAllQuestsCompletedDelayed: i,
              unlockPremiumAnimationState: l,
              isPremium: c,
            }) => {
              var m, d;
              const E = nu().model.computes.getConditions(e),
                _ = (0, s.useState)(wr.IDLE),
                A = _[0],
                D = _[1],
                F = (0, s.useState)(!1),
                g = F[0],
                B = F[1],
                C = null != (m = (0, v.D9)(e)) ? m : e,
                p = A === wr.IDLE,
                f = A === wr.BLINK,
                w = e.status === Qe.N.Locked,
                S = w && u !== Qe.N.Locked && !c,
                y =
                  (e.status === Qe.N.Done || e.status === Qe.N.UndoneSubscription) &&
                  u !== Qe.N.Done &&
                  u !== Qe.N.UndoneSubscription,
                P = null != (d = (0, v.D9)(S)) ? d : S,
                x = g && t === Ke.vW,
                T =
                  (e.status === Qe.N.Done || e.status === Qe.N.UndoneSubscription) &&
                  C &&
                  (null == C ? void 0 : C.status) !== Qe.N.Done &&
                  (null == C ? void 0 : C.status) !== Qe.N.UndoneSubscription,
                N = ((S || P || y) && p) || g,
                L = g && t === Ke.vW,
                M = S || P || g,
                k = (0, s.useMemo)(
                  () =>
                    c
                      ? {
                          header: vr.dailyQuests.premium.locked.tooltip.header(),
                          body: vr.dailyQuests.premium.locked.tooltip.body(),
                        }
                      : {
                          header: vr.dailyQuests.bonus.locked.tooltip.header(),
                          body: vr.dailyQuests.bonus.locked.tooltip.body(),
                        },
                  [c],
                );
              return (
                (0, s.useEffect)(
                  () => (
                    T && D(wr.COMPLETE),
                    A === wr.BLINK
                      ? (0, b.F)(() => {
                          D(wr.IDLE);
                        }, Ne)
                      : A === wr.COMPLETE
                        ? (0, b.F)(() => {
                            D(wr.BLINK);
                          }, Te)
                        : void 0
                  ),
                  [T, A],
                ),
                (0, s.useEffect)(() => {
                  P && !S && B(!0);
                }, [P, S]),
                (0, s.useEffect)(() => {
                  if (g)
                    return (0, b.F)(() => {
                      B(!1);
                    }, Oe);
                }, [g]),
                a().createElement(
                  "div",
                  { className: o()(or, S && lr, f && cr) },
                  N &&
                    a().createElement(
                      "div",
                      { className: o()(mr, y && Er) },
                      a().createElement("div", { className: dr }),
                      a().createElement("div", { className: br }),
                      S && a().createElement("div", { className: gr }),
                      a().createElement(
                        "div",
                        { className: o()(_r, L && Ar) },
                        a().createElement("div", { className: Dr }),
                        a().createElement(h.ZP, {
                          text: y
                            ? i
                              ? c
                                ? vr.premiumQuests.countDown.title()
                                : vr.dailyQuests.countDown.title()
                              : vr.dailyQuests.completed.title()
                            : vr.dailyQuests.locked.title(),
                          className: Fr,
                        }),
                        M &&
                          a().createElement(h.ZP, {
                            text: R.strings.quests.dailyWidget.progress(),
                            className: o()(Br, !t && Cr),
                            format: {
                              binding: {
                                currentProgress: a().createElement(
                                  "div",
                                  { className: pr, style: { "--currentProgress": t } },
                                  eu.map((e, u) =>
                                    a().createElement(h.ZP, {
                                      key: u,
                                      text: String(u),
                                      className: hr,
                                    }),
                                  ),
                                ),
                                maxProgress: a().createElement(h.ZP, {
                                  text: String(Ke.vW),
                                  className: fr,
                                }),
                              },
                            },
                          }),
                      ),
                    ),
                  a().createElement(zt, {
                    quest: e,
                    conditions: E,
                    disabledTooltipArgs: k,
                    isDisabled: w,
                    position: r,
                    isRerollAnimation: n,
                    isUnlockAnimation: x,
                    unlockPremiumAnimationState: l,
                  }),
                )
              );
            },
          ),
          yr = "QuestCardList_base_a1",
          Pr = "QuestCardList_cardList_86",
          Rr = "QuestCardList_cardList__allComplete_57",
          xr = "QuestCardList_cardList__hide_cc",
          Tr = "QuestCardList_attentionMessage_3c",
          Nr = "QuestCardList_titleIcon_3f",
          Lr = "QuestCardList_title_a6",
          Mr = "QuestCardList_scroll_b1",
          kr = "QuestCardList_scroll__maskTop_99",
          Or = "QuestCardList_scroll__maskBottom_04",
          Ir = "QuestCardList_scroll__maskBoth_d0",
          Hr = "QuestCardList_scrollContent_3d",
          Ur = "QuestCardList_questCardBlock_c2",
          Wr = "QuestCardList_bannerWrapper_72",
          Qr = "QuestCardList_divider_3c",
          Gr = "QuestCardList_divider__hide_be",
          jr = "QuestCardList_scrollBar_d4",
          $r = "QuestCardList_barThumb_7d",
          zr = "QuestCardList_barRail_3c";
        let qr;
        !(function (e) {
          ((e.IDLE = "idle"),
            (e.BANNER_HIDE = "banner_hide"),
            (e.CARD_BLINK = "card_blink"),
            (e.QUESTS_UNLOCK = "quests_unlock"),
            (e.COMPLETED = "completed"));
        })(qr || (qr = {}));
        const Xr = R.strings.quests.switch,
          Yr = (0, S.Pi)(
            ({ hasTopMask: e, hasBottomMask: u, scrollApi: t, isRerollAnimation: r }) => {
              var n, i, l;
              const c = nu(),
                m = c.model,
                d = c.controls,
                E = (0, Pe.GS)().mediaSize,
                _ = E >= Pe.cJ.Medium ? We.h2.Big : We.h2.Small,
                A = (0, s.useState)(!1),
                D = A[0],
                g = A[1],
                B = (0, s.useState)(!1),
                C = B[0],
                p = B[1],
                f = (0, s.useState)(!1),
                S = f[0],
                y = f[1],
                P = (0, s.useState)(qr.IDLE),
                x = P[0],
                T = P[1],
                N = x === qr.BANNER_HIDE,
                L = (0, v.tp)(m.computes.getCompletedlQuestLength(_), ke),
                M = D ? L : m.computes.getCompletedlQuestLength(_),
                k = (0, v.tp)(m.computes.getAllQuestsCompleted(_), ke),
                O = D ? k : m.computes.getAllQuestsCompleted(_),
                I = (0, v.tp)(m.computes.isPremiumTab(), ke),
                H = D ? I : m.computes.isPremiumTab(),
                U = m.regular.get().isEnabled,
                W = m.premium.get().isEnabled,
                Q = H ? W : U,
                G = (0, v.tp)(m.computes.isPremiumBannerVisible(), ke),
                j = D ? G : m.computes.isPremiumBannerVisible(),
                $ = (0, v.tp)(m.computes.getQuests(_), ke),
                z = D ? $ : m.computes.getQuests(_),
                q = m.computes.getEpicQuests(_),
                X = m.computes.getCurrentTabIndex(),
                Y = null != (n = (0, v.D9)(X)) ? n : X,
                Z = null != (i = (0, v.D9)(j)) ? i : j,
                K = (j && !O) || N,
                V = z.sort((e, u) => Ve.indexOf(u.status) - Ve.indexOf(e.status));
              const J = V.map((e) => e.status),
                ee = null != (l = (0, v.D9)(J)) ? l : J,
                ue = Je(J, K, E, H),
                te = C || D,
                re = Z && !j && H && !D,
                ne = (0, F.useTransition)(
                  V.map((e, u) => {
                    const t = V.length - 1 === u;
                    return Object.assign(
                      {},
                      e,
                      { y: `${ue[u]}rem` },
                      t && { marginBottom: `${Re[E].questListMarginBottom}rem` },
                      { index: u },
                    );
                  }),
                  {
                    key: (e) => e.id,
                    enter: ({ y: e, marginBottom: u }) => ({ y: e, marginBottom: u }),
                    update: ({ y: e, marginBottom: u }) => ({ y: e, marginBottom: u }),
                    config: te ? { duration: Le } : { duration: Ne },
                    delay: te || x !== qr.IDLE ? Le : Te,
                  },
                );
              var se, ae;
              return (
                (0, s.useEffect)(
                  () => (
                    re && ((0, w.G)(R.sounds.dq_widget_slide_in()), T(qr.BANNER_HIDE)),
                    x === qr.BANNER_HIDE
                      ? (0, b.F)(() => {
                          T(qr.CARD_BLINK);
                        }, Ie)
                      : x === qr.CARD_BLINK
                        ? (0, b.F)(() => {
                            T(qr.QUESTS_UNLOCK);
                          }, He)
                        : x === qr.QUESTS_UNLOCK
                          ? (0, b.F)(() => {
                              T(qr.COMPLETED);
                            }, Ue)
                          : void 0
                  ),
                  [re, x],
                ),
                (0, s.useEffect)(() => {
                  ee && JSON.stringify(J) !== JSON.stringify(ee) && X === Y && !D && y(!0);
                }, [J, ee, X, Y, D]),
                (0, s.useEffect)(() => {
                  if (S)
                    return (0, b.F)(() => {
                      y(!1);
                    }, Te);
                }, [S]),
                (se = () => (
                  p(!0),
                  (0, b.F)(() => {
                    p(!1);
                  }, Le)
                )),
                (ae = []),
                (0, s.useEffect)(
                  () => (
                    window.addEventListener("resize", se),
                    () => window.removeEventListener("resize", se)
                  ),
                  ae,
                ),
                (0, s.useEffect)(() => {
                  Y !== X && g(!0);
                }, [Y, X]),
                (0, s.useEffect)(() => {
                  if (D)
                    return (0, b.F)(() => {
                      ((0, w.G)(R.sounds.dq_widget_slide_in()), g(!1));
                    }, ke);
                }, [D]),
                a().createElement(
                  "div",
                  { className: yr },
                  Q &&
                    a().createElement(zt, { quest: q, conditions: q, isEpic: !0, isDisabled: !1 }),
                  Q
                    ? a().createElement(
                        "div",
                        { className: o()(Pr, O && Rr, D && xr) },
                        a().createElement(
                          Uu.Vertical.Area,
                          {
                            api: t,
                            className: o()(Mr, e && !u && kr, u && !e && Or, e && u && Ir),
                            classNames: { content: Hr },
                          },
                          K &&
                            a().createElement(
                              "div",
                              { className: o()(N && Wr) },
                              a().createElement(ir, {
                                hideBanner: N,
                                onBuyPremium: d.onBuyPremium,
                              }),
                              a().createElement("div", { className: o()(Qr, N && Gr) }),
                            ),
                          ne((e, u) => {
                            var t;
                            const n = null == (t = z[u.index - 1]) ? void 0 : t.status;
                            return a().createElement(
                              F.animated.div,
                              { style: Object.assign({}, e), className: Ur },
                              a().createElement(Sr, {
                                key: u.id,
                                quest: u,
                                prevQuestStatus: n,
                                isAllQuestsCompletedDelayed: k,
                                completedQuestsLength: M,
                                position: u.index + 1,
                                isRerollAnimation: r,
                                isCompleteAnimation: S,
                                unlockPremiumAnimationState: x,
                                isPremium: H,
                              }),
                            );
                          }),
                        ),
                        a().createElement(Uu.Vertical.Bar, {
                          api: t,
                          classNames: { base: jr, thumb: $r, rail: zr },
                        }),
                      )
                    : a().createElement(
                        "div",
                        { className: Tr },
                        a().createElement("div", { className: Nr }),
                        a().createElement(h.ZP, {
                          text: H ? Xr.isDailyPremEnabled() : Xr.isDailyRegularEnabled(),
                          format: { classMix: Lr },
                        }),
                      ),
                )
              );
            },
          ),
          Zr = "App_base_f7",
          Kr = "App_footer_f1",
          Vr = "App_lip_3f",
          Jr = "App_lipDivider_a1",
          en = "App_lip__hidden_ca",
          un = "App_lipDivider__hidden_f5",
          tn = "App_divider_d4",
          rn = "App_countdownWrapper_6e",
          nn = "App_countdownText_f1",
          sn = "App_countdown_4c",
          an = R.strings.quests.dailyQuests.countDown.tooltip,
          on = (0, S.Pi)(() => {
            var e, u;
            const t = nu(),
              r = t.model,
              n = t.controls,
              i = r.computes.isPremiumTab(),
              l = r.computes.getCurrentTabIndex(),
              c = i ? r.premium.get().isEnabled : r.regular.get().isEnabled,
              m = r.computes.getQuestsInfo(),
              d = m.countDown,
              E = m.rerollEnabled,
              _ = m.rerollCountDown,
              A = null != (e = (0, v.D9)(l)) ? e : l,
              D = null != (u = (0, v.D9)(E)) ? u : E,
              F = (0, s.useState)(!1),
              g = F[0],
              B = F[1],
              C = (0, s.useState)(!1),
              S = C[0],
              y = C[1],
              P = (0, s.useState)(!1),
              x = P[0],
              T = P[1],
              N = p();
            (!(function (e, u) {
              const t = e.contentRef,
                r = e.wrapperRef,
                n = e.scrollPosition,
                a = e.clampPosition,
                i = e.animationScroll,
                o = e.events,
                l = (0, s.useState)(z),
                c = l[0],
                m = l[1];
              ((0, s.useEffect)(() => {
                const e = t.current;
                e && (e.style.cursor = "dragging" === c.type ? "grabbing" : "grab");
              }, [t, c.type]),
                (0, s.useEffect)(() => {
                  if ("dragging" !== c.type) return;
                  const e = (e) => {
                      const s = t.current,
                        o = r.current;
                      if (!s || !o) return;
                      const l = c.positionFrom - e.screenY,
                        m = c.previousScrollPosition + l;
                      n.start(
                        Object.assign(
                          {
                            scrollPosition: a(s, m),
                            from: { scrollPosition: i.scrollPosition.get() },
                          },
                          u && { config: u },
                        ),
                      );
                    },
                    s = () => {
                      (window.removeEventListener("mousemove", e), m({ type: "scrollingToEnd" }));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", s),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", s));
                    }
                  );
                }, [i.scrollPosition, a, t, c, n, r, u]),
                (0, s.useEffect)(() => {
                  if ("scrollingToEnd" !== c.type) return;
                  const e = () => {
                    m(z);
                  };
                  return (i.scrollPosition.idle && e(), o.on("rest", e), () => o.off("rest", e));
                }, [i.scrollPosition, c.type, o]),
                (0, s.useEffect)(() => {
                  const e = t.current;
                  if (!e) return;
                  const u = (e) => {
                    (e.stopPropagation(),
                      0 === e.button &&
                        m({
                          type: "dragging",
                          positionFrom: e.screenY,
                          previousScrollPosition: i.scrollPosition.get(),
                        }));
                  };
                  return (
                    e.addEventListener("mousedown", u),
                    () => e.removeEventListener("mousedown", u)
                  );
                }, [i.scrollPosition, t]));
            })(N),
              (0, s.useEffect)(() => {
                const e = () => {
                  const e = N.animationScroll.scrollPosition.goal,
                    u = N.getBounds()[1];
                  (B(e > 3), y(e < u - 3));
                };
                return (
                  N.events.on("recalculateContent", e),
                  N.events.on("change", e),
                  () => {
                    (N.events.off("recalculateContent", e), N.events.off("change", e));
                  }
                );
              }, [N]),
              (0, s.useEffect)(() => {
                i ? n.onPremiumWindowLoaded() : n.onRegularWindowLoaded();
              }, [n, i]),
              (0, s.useEffect)(() => {
                D && !E && A === l && _ && (T(!0), (0, w.G)(R.sounds.dq_widget_slide_in()));
              }, [E, D, l, A, _]),
              (0, s.useEffect)(() => {
                if (x)
                  return (0, b.F)(() => {
                    T(!1);
                  }, Me);
              }, [x]));
            const L = (0, s.useCallback)(() => {
              n.onReroll(i);
            }, [n, i]);
            return a().createElement(
              "div",
              { className: Zr },
              a().createElement(Yr, {
                hasTopMask: g,
                hasBottomMask: S,
                scrollApi: N,
                isRerollAnimation: x,
              }),
              c &&
                a().createElement(
                  "div",
                  { className: Kr },
                  a().createElement("div", { className: o()(Vr, !S && en) }),
                  a().createElement("div", { className: o()(Jr, S && un) }),
                  a().createElement($.q, { canReroll: E, onReroll: L, rerollPremium: i }),
                  a().createElement("div", { className: tn }),
                  a().createElement(
                    f.i,
                    { header: an.header(), body: an.body() },
                    a().createElement(
                      "div",
                      { className: rn },
                      a().createElement(h.ZP, {
                        text: R.strings.quests.dailyQuests.countDown.remainingText(),
                        className: nn,
                      }),
                      a().createElement(
                        "div",
                        { className: sn },
                        a().createElement(j, { timeToUpdate: d }),
                      ),
                    ),
                  ),
                ),
            );
          });
        (0, s.memo)(function (e) {
          const u = (0, s.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
          return a().createElement(ru, { options: u }, a().createElement(on, null));
        });
      },
      3017: (e, u, t) => {
        "use strict";
        t.d(u, { ix: () => o, rl: () => i });
        var r = t(2862),
          n = t(729),
          s = t(9480);
        let a;
        !(function (e) {
          ((e[(e.DailyQuests = 0)] = "DailyQuests"), (e[(e.PremiumQuests = 1)] = "PremiumQuests"));
        })(a || (a = {}));
        (a.DailyQuests, a.PremiumQuests);
        const i = (e, u, t = r.h2.Big, a) =>
            null != e && e.length
              ? null == s
                ? void 0
                : s.map(e, (e) => ({
                    name: e.name,
                    size: t,
                    image: (0, n.ry)(e, t),
                    special: e.overlayType,
                    value: e.value,
                    valueType: (0, n.p3)(e.name),
                    tooltipArgs: (0, n.pI)(
                      { tooltipId: `${u}:${e.index}` },
                      Number(e.tooltipContentId),
                      { ignoreShowDelay: !0 },
                    ),
                    withSubscription: a,
                  }))
              : [],
          o = (e, u) => u.some((u) => u.questID === e.id);
      },
      9922: (e, u, t) => {
        "use strict";
        t.d(u, { q: () => B });
        var r = t(6483),
          n = t.n(r),
          s = t(7613),
          a = t(2056),
          i = t(7727),
          o = t(8515),
          l = t(6179),
          c = t.n(l);
        const m = "RerollButton_base_7a",
          d = "RerollButton_base__disabled_2e",
          E = "RerollButton_iconWrapper_19",
          _ = "RerollButton_icon_62",
          A = "RerollButton_iconHover_e2",
          D = "RerollButton_iconDisabled_8f",
          F = "RerollButton_text_0b",
          g = "RerollButton_shine_75",
          B = (0, o.Pi)(({ canReroll: e, onReroll: u, rerollPremium: t, className: r }) =>
            c().createElement(
              a.u,
              {
                ignoreMouseClick: !e,
                contentId: R.views.lobby.daily.tooltips.RerollTooltip("resId"),
                args: { rerollPremium: t },
              },
              c().createElement(
                "div",
                {
                  className: n()(m, r, !e && d),
                  onClick: e ? u : void 0,
                  onMouseEnter: e ? () => (0, i.G)(R.sounds.highlight()) : void 0,
                },
                c().createElement(
                  "div",
                  { className: E },
                  e
                    ? c().createElement(
                        c().Fragment,
                        null,
                        c().createElement("div", { className: _ }),
                        c().createElement("div", { className: A }),
                        c().createElement("div", { className: g }),
                      )
                    : c().createElement("div", { className: D }),
                ),
                c().createElement(s.ZP, {
                  className: F,
                  text: R.strings.quests.dailyQuests.body.reroll(),
                }),
              ),
            ),
          );
      },
      3509: (e, u, t) => {
        "use strict";
        t.d(u, { ji: () => n, vW: () => r });
        const r = 3,
          n = {
            unlockSubscriptionBonusDuration: 2e3,
            unlockBonusQuestDelay: 3e3,
            unlockBonusQuestDuration: 500,
            unlockTabPremiumDuration: 700,
          };
      },
      9153: (e, u, t) => {
        "use strict";
        let r;
        (t.d(u, { g: () => r }),
          (function (e) {
            ((e[(e.DailyQuests = 0)] = "DailyQuests"),
              (e[(e.PremiumQuests = 1)] = "PremiumQuests"));
          })(r || (r = {})));
      },
      3099: (e, u, t) => {
        "use strict";
        let r;
        (t.d(u, { N: () => r }),
          (function (e) {
            ((e.Done = "done"),
              (e.UndoneSubscription = "undoneSubscription"),
              (e.Locked = "notAvailable"),
              (e.Active = ""));
          })(r || (r = {})));
      },
      5026: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        const r = {
          mt__XS: "Box_mt__XS_0c",
          mt__SM: "Box_mt__SM_eb",
          mt__SMp: "Box_mt__SMp_cf",
          mt__MD: "Box_mt__MD_25",
          mt__MDp: "Box_mt__MDp_49",
          mt__LG: "Box_mt__LG_e8",
          mt__XL: "Box_mt__XL_83",
          mr__XS: "Box_mr__XS_7c",
          mr__SM: "Box_mr__SM_08",
          mr__SMp: "Box_mr__SMp_06",
          mr__MD: "Box_mr__MD_4a",
          mr__MDp: "Box_mr__MDp_b6",
          mr__LG: "Box_mr__LG_d0",
          mr__XL: "Box_mr__XL_db",
          mb__XS: "Box_mb__XS_bb",
          mb__SM: "Box_mb__SM_83",
          mb__SMp: "Box_mb__SMp_04",
          mb__MD: "Box_mb__MD_ed",
          mb__MDp: "Box_mb__MDp_65",
          mb__LG: "Box_mb__LG_c8",
          mb__XL: "Box_mb__XL_f8",
          ml__XS: "Box_ml__XS_8a",
          ml__SM: "Box_ml__SM_e6",
          ml__SMp: "Box_ml__SMp_fb",
          ml__MD: "Box_ml__MD_2b",
          ml__MDp: "Box_ml__MDp_c7",
          ml__LG: "Box_ml__LG_39",
          ml__XL: "Box_ml__XL_4a",
        };
      },
      5287: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        const r = { base: "FormatText_base_d0" };
      },
      3393: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        const r = {
          "paragraph-P10": "Text_paragraph-P10_2c",
          "paragraph-P12": "Text_paragraph-P12_22",
          "paragraph-P14": "Text_paragraph-P14_a7",
          "paragraph-P16": "Text_paragraph-P16_90",
          "paragraph-P18": "Text_paragraph-P18_50",
          "paragraph-P24": "Text_paragraph-P24_33",
          "heading-H14": "Text_heading-H14_8b",
          "heading-H15": "Text_heading-H15_9e",
          "heading-H18": "Text_heading-H18_b7",
          "heading-H20R": "Text_heading-H20R_f6",
          "heading-H22": "Text_heading-H22_27",
          "heading-H24R": "Text_heading-H24R_be",
          "heading-H24": "Text_heading-H24_0c",
          "heading-H28": "Text_heading-H28_78",
          "heading-H36": "Text_heading-H36_32",
          "heading-H56": "Text_heading-H56_c3",
          "heading-H73": "Text_heading-H73_8f",
          "heading-H144": "Text_heading-H144_a9",
          BLACK_REAL: "Text_BLACK_REAL_30",
          WHITE_REAL: "Text_WHITE_REAL_bc",
          WHITE: "Text_WHITE_62",
          WHITE_ORANGE: "Text_WHITE_ORANGE_54",
          WHITE_SPANISH: "Text_WHITE_SPANISH_df",
          PAR: "Text_PAR_15",
          PAR_SECONDARY: "Text_PAR_SECONDARY_5d",
          PAR_TERTIARY: "Text_PAR_TERTIARY_c9",
          INFO_RED: "Text_INFO_RED_30",
          RED: "Text_RED_66",
          RED_DARK: "Text_RED_DARK_d8",
          YELLOW: "Text_YELLOW_ed",
          ORANGE: "Text_ORANGE_be",
          CREAM: "Text_CREAM_57",
          BROWN: "Text_BROWN_18",
          GREEN_BRIGHT: "Text_GREEN_BRIGHT_3f",
          GREEN: "Text_GREEN_e3",
          GREEN_DARK: "Text_GREEN_DARK_f1",
          BLUE_BOOSTER: "Text_BLUE_BOOSTER_21",
          BLUE_TEAMKILLER: "Text_BLUE_TEAMKILLER_ab",
          CRED: "Text_CRED_f7",
          GOLD: "Text_GOLD_28",
          BOND: "Text_BOND_be",
          PROM: "Text_PROM_65",
        };
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(e) {
    var u = __webpack_module_cache__[e];
    if (void 0 !== u) return u.exports;
    var t = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](t, t.exports, __webpack_require__), t.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, u, t, r) => {
      if (!u) {
        var n = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [u, t, r] = deferred[o], s = !0, a = 0; a < u.length; a++)
            (!1 & r || n >= r) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[a]))
              ? u.splice(a--, 1)
              : ((s = !1), r < n && (n = r));
          if (s) {
            deferred.splice(o--, 1);
            var i = t();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      r = r || 0;
      for (var o = deferred.length; o > 0 && deferred[o - 1][2] > r; o--)
        deferred[o] = deferred[o - 1];
      deferred[o] = [u, t, r];
    }),
    (__webpack_require__.n = (e) => {
      var u = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(u, { a: u }), u);
    }),
    (__webpack_require__.d = (e, u) => {
      for (var t in u)
        __webpack_require__.o(u, t) &&
          !__webpack_require__.o(e, t) &&
          Object.defineProperty(e, t, { enumerable: !0, get: u[t] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (e, u) => Object.prototype.hasOwnProperty.call(e, u)),
    (__webpack_require__.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (__webpack_require__.j = 444),
    (() => {
      var e = { 444: 0, 306: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var r,
            n,
            [s, a, i] = t,
            o = 0;
          if (s.some((u) => 0 !== e[u])) {
            for (r in a) __webpack_require__.o(a, r) && (__webpack_require__.m[r] = a[r]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); o < s.length; o++)
            ((n = s[o]), __webpack_require__.o(e, n) && e[n] && e[n][0](), (e[n] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [272], () => __webpack_require__(2263));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
