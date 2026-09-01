(() => {
  var __webpack_modules__ = {
      3779: (e, t, u) => {
        "use strict";
        u.d(t, { ZP: () => A });
        var a = u(6483),
          n = u.n(a),
          r = u(9887),
          s = u.n(r),
          o = u(3377),
          i = u(6179),
          l = u.n(i),
          c = u(5026);
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
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        Object.keys(s());
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
          g = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          A = (0, o.ZP)((e) => {
            let t = e.className,
              u = e.width,
              a = e.height,
              r = e.m,
              s = e.mt,
              o = void 0 === s ? r : s,
              A = e.mr,
              p = void 0 === A ? r : A,
              D = e.mb,
              h = void 0 === D ? r : D,
              F = e.ml,
              C = void 0 === F ? r : F,
              B = e.column,
              v = e.row,
              b = e.flexDirection,
              f = void 0 === b ? (B ? "column" : v && "row") || void 0 : b,
              w = e.flexStart,
              S = e.center,
              x = e.flexEnd,
              R = e.spaceBetween,
              P = e.spaceAround,
              L = e.justifyContent,
              y =
                void 0 === L
                  ? (w ? "flex-start" : S && "center") ||
                    (x && "flex-end") ||
                    (R && "space-between") ||
                    (P && "space-around") ||
                    void 0
                  : L,
              T = e.alignItems,
              N =
                void 0 === T
                  ? (w ? "flex-start" : S && "center") || (x && "flex-end") || void 0
                  : T,
              M = e.alignSelf,
              k = e.wrap,
              O = e.flexWrap,
              I = void 0 === O ? (k ? "wrap" : void 0) : O,
              H = e.grow,
              U = e.shrink,
              $ = e.flex,
              W = void 0 === $ ? (H || U ? `${H ? 1 : 0} ${U ? 1 : 0} auto` : void 0) : $,
              G = e.style,
              V = e.children,
              z = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, m);
            const j = (0, i.useMemo)(() => {
                const e = { mt: o, mr: p, mb: h, ml: C },
                  t = ((e) =>
                    _.reduce((t, u) => {
                      const a = e[u];
                      return a && "number" != typeof a ? t.concat(E[!0 === a ? "MD" : a][u]) : t;
                    }, []))(e),
                  n = ((e) =>
                    _.reduce((t, u) => {
                      const a = e[u];
                      return ("number" == typeof a && (t[g[u]] = a + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, G, n, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    flex: W,
                    alignSelf: M,
                    display: f || N ? "flex" : void 0,
                    flexDirection: f,
                    flexWrap: I,
                    justifyContent: y,
                    alignItems: N,
                  }),
                  computedClassNames: t,
                };
              }, [u, a, o, p, h, C, G, W, M, f, I, y, N]),
              X = j.computedStyle,
              q = j.computedClassNames;
            return l().createElement(
              "div",
              d({ className: n()(c.Z.base, ...q, t), style: X }, z),
              V,
            );
          });
      },
      2372: (e, t, u) => {
        "use strict";
        u.d(t, { A: () => s });
        var a = u(6179),
          n = u.n(a),
          r = u(4179);
        class s extends n().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = r.B3.GOLD;
            else e = r.B3.INTEGRAL;
            const t = r.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        s.defaultProps = { format: "integral" };
      },
      280: (e, t, u) => {
        "use strict";
        u.d(t, { z: () => l });
        var a = u(6179),
          n = u.n(a),
          r = u(6483),
          s = u.n(r),
          o = u(3649),
          i = u(5287);
        const l = ({ binding: e, text: t = "", classMix: u, alignment: r = o.v2.left }) =>
          null === t
            ? (console.error("FormatText was supplied with 'null'"), null)
            : n().createElement(
                a.Fragment,
                null,
                t.split("\n").map((t, l) =>
                  n().createElement(
                    "div",
                    { className: s()(i.Z.base, u), key: `${t}-${l}` },
                    (0, o.Uw)(t, r, e).map((e, t) =>
                      n().createElement(a.Fragment, { key: `${t}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, t, u) => {
        "use strict";
        u.d(t, { Y: () => m });
        var a = u(3138),
          n = u(6179),
          r = u(1043),
          s = u(5262);
        const o = a.O.client.getSize("rem"),
          i = o.width,
          l = o.height,
          c = Object.assign({ width: i, height: l }, (0, s.T)(i, l, r.j)),
          m = (0, n.createContext)(c);
      },
      1039: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => c });
        var a = u(6179),
          n = u.n(a),
          r = u(6536),
          s = u(3495),
          o = u(1043),
          i = u(5262),
          l = u(3138);
        const c = (0, a.memo)(({ children: e }) => {
          const t = (0, a.useContext)(s.Y),
            u = (0, a.useState)(t),
            c = u[0],
            m = u[1],
            d = (0, a.useCallback)((e, t) => {
              const u = l.O.view.pxToRem(e),
                a = l.O.view.pxToRem(t);
              m(Object.assign({ width: u, height: a }, (0, i.T)(u, a, o.j)));
            }, []);
          ((0, r.Z)(() => {
            engine.on("clientResized", d);
          }),
            (0, a.useEffect)(() => () => engine.off("clientResized", d), [d]));
          const E = (0, a.useMemo)(() => Object.assign({}, c), [c]);
          return n().createElement(s.Y.Provider, { value: E }, e);
        });
      },
      6010: (e, t, u) => {
        "use strict";
        var a = u(6179),
          n = u(7382),
          r = u(3495);
        const s = ["children"];
        const o = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, s);
          const o = (0, a.useContext)(r.Y),
            i = o.extraLarge,
            l = o.large,
            c = o.medium,
            m = o.small,
            d = o.extraSmall,
            E = o.extraLargeWidth,
            _ = o.largeWidth,
            g = o.mediumWidth,
            A = o.smallWidth,
            p = o.extraSmallWidth,
            D = o.extraLargeHeight,
            h = o.largeHeight,
            F = o.mediumHeight,
            C = o.smallHeight,
            B = o.extraSmallHeight,
            v = { extraLarge: D, large: h, medium: F, small: C, extraSmall: B };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && i) return t;
            if (u.large && l) return t;
            if (u.medium && c) return t;
            if (u.small && m) return t;
            if (u.extraSmall && d) return t;
          } else {
            if (u.extraLargeWidth && E) return (0, n.H)(t, u, v);
            if (u.largeWidth && _) return (0, n.H)(t, u, v);
            if (u.mediumWidth && g) return (0, n.H)(t, u, v);
            if (u.smallWidth && A) return (0, n.H)(t, u, v);
            if (u.extraSmallWidth && p) return (0, n.H)(t, u, v);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && D) return t;
              if (u.largeHeight && h) return t;
              if (u.mediumHeight && F) return t;
              if (u.smallHeight && C) return t;
              if (u.extraSmallHeight && B) return t;
            }
          }
          return null;
        };
        o.defaultProps = {
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
        (0, a.memo)(o);
      },
      7382: (e, t, u) => {
        "use strict";
        u.d(t, { H: () => a });
        const a = (e, t, u) =>
          t.extraLargeHeight ||
          t.largeHeight ||
          t.mediumHeight ||
          t.smallHeight ||
          t.extraSmallHeight
            ? (t.extraLargeHeight && u.extraLarge) ||
              (t.largeHeight && u.large) ||
              (t.mediumHeight && u.medium) ||
              (t.smallHeight && u.small) ||
              (t.extraSmallHeight && u.extraSmall)
              ? e
              : null
            : e;
      },
      7739: (e, t, u) => {
        "use strict";
        u.d(t, { YN: () => n.Y, ZN: () => a.Z });
        u(6010);
        var a = u(1039),
          n = u(3495);
      },
      1043: (e, t, u) => {
        "use strict";
        u.d(t, { j: () => a });
        const a = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, t, u) => {
        "use strict";
        var a;
        function n(e, t, u) {
          const a = (function (e, t) {
              switch (!0) {
                case e >= t.extraLarge.width:
                  return t.extraLarge.weight;
                case e >= t.large.width && e < t.extraLarge.width:
                  return t.large.weight;
                case e >= t.medium.width && e < t.large.width:
                  return t.medium.weight;
                case e >= t.small.width && e < t.medium.width:
                  return t.small.weight;
                default:
                  return t.extraSmall.weight;
              }
            })(e, u),
            n = (function (e, t) {
              switch (!0) {
                case e >= t.extraLarge.height:
                  return t.extraLarge.weight;
                case e >= t.large.height && e < t.extraLarge.height:
                  return t.large.weight;
                case e >= t.medium.height && e < t.large.height:
                  return t.medium.weight;
                case e >= t.small.height && e < t.medium.height:
                  return t.small.weight;
                default:
                  return t.extraSmall.weight;
              }
            })(t, u),
            r = Math.min(a, n);
          return {
            extraLarge: r === u.extraLarge.weight,
            large: r === u.large.weight,
            medium: r === u.medium.weight,
            small: r === u.small.weight,
            extraSmall: r === u.extraSmall.weight,
            extraLargeWidth: a === u.extraLarge.weight,
            largeWidth: a === u.large.weight,
            mediumWidth: a === u.medium.weight,
            smallWidth: a === u.small.weight,
            extraSmallWidth: a === u.extraSmall.weight,
            extraLargeHeight: n === u.extraLarge.weight,
            largeHeight: n === u.large.weight,
            mediumHeight: n === u.medium.weight,
            smallHeight: n === u.small.weight,
            extraSmallHeight: n === u.extraSmall.weight,
          };
        }
        (u.d(t, { T: () => n }),
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
          })(a || (a = {})));
      },
      2862: (e, t, u) => {
        "use strict";
        let a, n, r, s, o, i, l, c, m;
        (u.d(t, {
          $h: () => s,
          A2: () => i,
          E4: () => a,
          h2: () => r,
          kK: () => o,
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
              (e.RewardsSlots = "rewardsSlots"));
          })(a || (a = {})),
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
          })(r || (r = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(s || (s = {})),
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
          })(o || (o = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(i || (i = {})),
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
      729: (e, t, u) => {
        "use strict";
        u.d(t, { L_: () => p, i2: () => D, m9: () => h, p3: () => d, pI: () => A, ry: () => g });
        var a = u(2372),
          n = u(6179),
          r = u.n(n),
          s = u(2862);
        const o = [
            s.E4.Items,
            s.E4.Equipment,
            s.E4.Xp,
            s.E4.XpFactor,
            s.E4.Blueprints,
            s.E4.BlueprintsAny,
            s.E4.Goodies,
            s.E4.Berths,
            s.E4.Slots,
            s.E4.Tokens,
            s.E4.CrewSkins,
            s.E4.CrewBooks,
            s.E4.Customizations,
            s.E4.CreditsFactor,
            s.E4.TankmenXp,
            s.E4.TankmenXpFactor,
            s.E4.FreeXpFactor,
            s.E4.BattleToken,
            s.E4.PremiumUniversal,
            s.E4.NaturalCover,
            s.E4.BpCoin,
            s.E4.BattlePassSelectToken,
            s.E4.BattlaPassFinalAchievement,
            s.E4.BattleBadge,
            s.E4.BonusX5,
            s.E4.CrewBonusX3,
            s.E4.NewYearFillers,
            s.E4.NewYearInvoice,
            s.E4.EpicSelectToken,
            s.E4.Comp7TokenWeeklyReward,
            s.E4.Comp7TokenCouponReward,
            s.E4.BattleBoosterGift,
            s.E4.CosmicLootboxCommon,
            s.E4.CosmicLootboxSilver,
            s.E4.SelectableBonus,
            s.E4.PostStamp,
            s.E4.PremiumPlusUniversal,
            s.E4.GoldenTicket,
            s.E4.RewardsSlots,
          ],
          i = [s.E4.Gold, s.E4.Credits, s.E4.Crystal, s.E4.FreeXp],
          l = [s.E4.BattlePassPoints],
          c = [s.E4.PremiumPlus, s.E4.Premium];
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
            o.includes(e)
              ? s.$h.MULTI
              : i.includes(e)
                ? s.$h.CURRENCY
                : l.includes(e)
                  ? s.$h.NUMBER
                  : c.includes(e)
                    ? s.$h.PREMIUM_PLUS
                    : s.$h.STRING,
          E = ["engravings", "backgrounds"],
          _ = ["engraving", "background"],
          g = (e, t = s.h2.Small) => {
            const u = e.name,
              a = e.type,
              n = e.value,
              r = e.icon,
              o = e.item,
              i = e.dogTagType,
              l = ((e) => {
                switch (e) {
                  case s.h2.S600x450:
                    return "c_600x450";
                  case s.h2.S400x300:
                    return "c_400x300";
                  case s.h2.S296x222:
                    return "c_296x222";
                  case s.h2.S232x174:
                    return "c_232x174";
                  case s.h2.Big:
                    return "c_80x80";
                  case s.h2.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(t);
            switch (u) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}_${n}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${u}_plus_${n}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${u}_${n}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${o}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${t}.${r}`;
              case "tokens":
              case "battleToken":
                return ((e, t) => {
                  switch (t) {
                    case s.h2.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case s.h2.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${t}.${e.icon}`;
                  }
                })(e, t);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${t}.${r}`;
              case "dogTagComponents":
                return ((e, t, u) => {
                  const a = E[e];
                  if (a) {
                    const n = R.images.gui.maps.icons.dogtags.$dyn(t).$dyn(a),
                      r = n.$dyn(u);
                    return r ? `${r}` : `${n.$dyn(_[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(i, t, r);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${l}.${r}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case s.h2.S600x450:
                      return "c_600x450";
                    case s.h2.S400x300:
                      return "c_400x300";
                    case s.h2.S296x222:
                      return "c_296x222";
                    case s.h2.S232x174:
                      return "c_232x174";
                    case s.h2.S180x135:
                      return "big";
                    case s.h2.Big:
                    case s.h2.S80x80:
                      return "c_80x80";
                    case s.h2.Small:
                    case s.h2.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(t)}.${r}`;
              case "xp":
              case "xpFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.exp`;
              case "creditsFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.credits`;
              case "tankmenXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.tankmenXP`;
              case "dailyXPFactor":
              case "freeXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.freeXP`;
              case "tmanToken":
              case "battlePassSelectToken":
              case "selectableBonus":
              case "groups":
              case "lootBoxToken":
              case "customizations":
              case "crewSkins":
              case "goodies":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${r}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${l}.${r}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case s.h2.Mini:
                      return m.s32;
                    case s.h2.Small:
                    case s.h2.S48x48:
                      return m.s48;
                    case s.h2.S80x80:
                    case s.h2.Big:
                      return m.s80;
                    case s.h2.S128x100:
                      return m.s116;
                    case s.h2.S180x135:
                    case s.h2.S232x174:
                    case s.h2.S296x222:
                      return m.s296;
                    case s.h2.S400x300:
                      return m.s400;
                    case s.h2.S600x450:
                      return m.s600;
                  }
                })(t)}`;
              case s.E4.StyleProgress:
              case s.E4.LbStyleProgress:
                return F(r, t, s.ye.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${u}`;
            }
          },
          A = (e, t, u) => {
            const a = t && { contentId: t };
            return Object.assign(
              {
                args: e,
                isEnabled: Boolean((e && e.tooltipId) || t),
                ignoreMouseClick: !0,
                ignoreShowDelay: !t,
              },
              a,
              u,
            );
          },
          p = (e) => {
            if (void 0 === e) return null;
            switch (e) {
              case s.kK.BATTLE_BOOSTER:
              case s.kK.BATTLE_BOOSTER_REPLACE:
                return s.A2.BATTLE_BOOSTER;
            }
          },
          D = (e) => {
            if (void 0 === e) return null;
            switch (e) {
              case s.kK.BATTLE_BOOSTER:
                return s.sh.BATTLE_BOOSTER;
              case s.kK.BATTLE_BOOSTER_REPLACE:
                return s.sh.BATTLE_BOOSTER_REPLACE;
              case s.kK.BUILT_IN_EQUIPMENT:
                return s.sh.BUILT_IN_EQUIPMENT;
              case s.kK.EQUIPMENT_PLUS:
                return s.sh.EQUIPMENT_PLUS;
              case s.kK.EQUIPMENT_TROPHY_BASIC:
                return s.sh.EQUIPMENT_TROPHY_BASIC;
              case s.kK.EQUIPMENT_TROPHY_UPGRADED:
                return s.sh.EQUIPMENT_TROPHY_UPGRADED;
              case s.kK.EQUIPMENT_MODERNIZED_UPGRADED_1:
                return s.sh.EQUIPMENT_MODERNIZED_UPGRADED_1;
              case s.kK.EQUIPMENT_MODERNIZED_UPGRADED_2:
                return s.sh.EQUIPMENT_MODERNIZED_UPGRADED_2;
              case s.kK.EQUIPMENT_MODERNIZED_UPGRADED_3:
                return s.sh.EQUIPMENT_MODERNIZED_UPGRADED_3;
              case s.kK.PROGRESSION_STYLE_UPGRADED_1:
                return s.sh.PROGRESSION_STYLE_UPGRADED_1;
              case s.kK.PROGRESSION_STYLE_UPGRADED_2:
                return s.sh.PROGRESSION_STYLE_UPGRADED_2;
              case s.kK.PROGRESSION_STYLE_UPGRADED_3:
                return s.sh.PROGRESSION_STYLE_UPGRADED_3;
              case s.kK.PROGRESSION_STYLE_UPGRADED_4:
                return s.sh.PROGRESSION_STYLE_UPGRADED_4;
            }
          },
          h = (e, t) => {
            if (void 0 === e) return null;
            switch (t) {
              case s.$h.MULTI: {
                const t = Number(e);
                return isFinite(t) && t > 1 ? `x${Math.floor(t)}` : null;
              }
              case s.$h.CURRENCY:
              case s.$h.NUMBER:
                return r().createElement(a.A, { format: "integral", value: Number(e) });
              case s.$h.PREMIUM_PLUS: {
                const t = Number(e);
                return isNaN(t) ? e : null;
              }
              default:
                return e;
            }
          },
          F = (e, t, u) => {
            const a = R.images.gui.maps.icons.quests.bonuses.$dyn(t),
              n = a.$dyn(e);
            return String(null != n ? n : a.$dyn(u));
          };
      },
      7613: (e, t, u) => {
        "use strict";
        u.d(t, { ZP: () => b });
        var a = u(6483),
          n = u.n(a),
          r = u(3779),
          s = u(280),
          o = u(3532),
          i = u.n(o),
          l = u(9887),
          c = u.n(l),
          m = u(3377),
          d = u(6179),
          E = u.n(d),
          _ = u(3393);
        const g = [
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
        function A() {
          return (
            (A =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            A.apply(this, arguments)
          );
        }
        Object.keys(c());
        const p = Object.keys(i()),
          D = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          h = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          F = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          C = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          B =
            (Object.keys(C),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": D,
              "heading-H36": D,
              "heading-H28": h,
              "heading-H24": h,
              "heading-H24R": h,
              "heading-H22": h,
              "heading-H20R": h,
              "heading-H18": h,
              "heading-H15": F,
              "heading-H14": F,
              "paragraph-P24": h,
              "paragraph-P18": h,
              "paragraph-P16": h,
              "paragraph-P14": F,
              "paragraph-P12": F,
              "paragraph-P10": F,
            }),
          v =
            (Object.keys(B),
            (e) =>
              e
                ? ((e) => p.includes(e))(e)
                  ? { colorClassName: _.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          b = (0, m.ZP)((e) => {
            let t = e.text,
              u = e.variant,
              a = e.className,
              o = e.color,
              i = e.m,
              l = e.mt,
              c = void 0 === l ? i : l,
              m = e.mr,
              p = void 0 === m ? i : m,
              D = e.mb,
              h = void 0 === D ? i : D,
              F = e.ml,
              C = void 0 === F ? i : F,
              b = e.style,
              f = e.format,
              w = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, g);
            const S = (0, d.useMemo)(() => {
                const e = v(o),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  a = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, b, a), colorClassName: t };
              }, [b, o]),
              x = S.computedStyle,
              R = S.colorClassName;
            return E().createElement(
              r.ZP,
              A(
                {
                  className: n()(_.Z.base, u && _.Z[u], R, a),
                  style: x,
                  mt: !0 === c ? B[u || "paragraph-P16"].mt : c,
                  mr: !0 === p ? B[u || "paragraph-P16"].mr : p,
                  mb: !0 === h ? B[u || "paragraph-P16"].mb : h,
                  ml: !0 === C ? B[u || "paragraph-P16"].ml : C,
                },
                w,
              ),
              void 0 !== f ? E().createElement(s.z, A({}, f, { text: t })) : t,
            );
          });
      },
      926: (e) => {
        e.exports = {
          SMALL_WIDTH: "mediaSmallWidth",
          MEDIUM_WIDTH: "mediaMediumWidth",
          LARGE_WIDTH: "mediaLargeWidth",
          EXTRA_LARGE_WIDTH: "mediaExtraLargeWidth",
          SMALL_HEIGHT: "mediaSmallHeight",
          MEDIUM_HEIGHT: "mediaMediumHeight",
          LARGE_HEIGHT: "mediaLargeHeight",
          EXTRA_LARGE_HEIGHT: "mediaExtraLargeHeight",
          SMALL: "mediaSmall",
          MEDIUM: "mediaMedium",
          LARGE: "mediaLarge",
          EXTRA_LARGE: "mediaExtraLarge",
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
      7044: (e, t, u) => {
        "use strict";
        u.d(t, { U9: () => o, f8: () => i, oG: () => a, s_: () => n });
        (u(3649), u(728), u(4179));
        const a = 60,
          n = 1e3,
          r = 3600,
          s = 86400;
        Date.now();
        function o(e) {
          return e.toString().padStart(2, "0");
        }
        function i(e = 0) {
          let t = e;
          const u = Math.trunc(t / s);
          t -= u * s;
          const a = Math.trunc(t / r);
          t -= a * r;
          const n = Math.trunc(t / 60);
          return ((t -= 60 * n), { days: u, hours: a, minutes: n, seconds: t });
        }
      },
      527: (e, t, u) => {
        "use strict";
        (u.r(t), u.d(t, { mouse: () => o, onResize: () => r }));
        var a = u(2472),
          n = u(1176);
        const r = (0, a.E)("clientResized"),
          s = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const o = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, n.R)(!1);
          }
          function u() {
            e.enabled && (0, n.R)(!0);
          }
          function a() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", u))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", u))
              : (0, n.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let n = !0;
                  const r = `mouse${t}`,
                    o = s[t]((e) => u([e, "outside"]));
                  function i(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, i),
                    a(),
                    () => {
                      n &&
                        (o(), window.removeEventListener(r, i), (e.listeners -= 1), a(), (n = !1));
                    }
                  );
                };
              })(u)),
              t
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), a());
            },
            enable() {
              ((e.enabled = !0), a());
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
      5959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => a,
            getMouseGlobalPosition: () => r,
            getSize: () => n,
            graphicsQuality: () => s,
          }));
        var a = u(527);
        function n(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const s = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, t, u) => {
        "use strict";
        function a(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        u.d(t, { R: () => a });
      },
      2472: (e, t, u) => {
        "use strict";
        function a(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        u.d(t, { E: () => a });
      },
      3138: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => n });
        var a = u(5959);
        const n = { view: u(7641), client: a };
      },
      3722: (e, t, u) => {
        "use strict";
        function a(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function n(e, t, u) {
          return `url(${a(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => n, getTextureUrl: () => a }));
      },
      6112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => n });
        var a = u(2472);
        const n = {
          onTextureFrozen: (0, a.E)("self.onTextureFrozen"),
          onTextureReady: (0, a.E)("self.onTextureReady"),
          onDomBuilt: (0, a.E)("self.onDomBuilt"),
          onLoaded: (0, a.E)("self.onLoaded"),
          onDisplayChanged: (0, a.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, a.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, a.E)("children.onAdded"),
            onLoaded: (0, a.E)("children.onLoaded"),
            onRemoved: (0, a.E)("children.onRemoved"),
            onAttached: (0, a.E)("children.onAttached"),
            onTextureReady: (0, a.E)("children.onTextureReady"),
            onRequestPosition: (0, a.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => o,
            children: () => a,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => r.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => b,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => A,
            getSize: () => d,
            getViewGlobalPosition: () => _,
            isClientAccessible: () => C,
            isEventHandled: () => v,
            isFocused: () => F,
            pxToRem: () => p,
            remToPx: () => D,
            resize: () => E,
            sendEvent: () => s.qP,
            setAnimateWindow: () => h,
            setEventHandled: () => B,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => m,
            whenTutorialReady: () => x,
          }));
        var a = u(3722),
          n = u(6112),
          r = u(6538),
          s = u(8566);
        function o(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, u, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, a);
        }
        function c(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function m(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function E(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function _(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: D(t.x), y: D(t.y) };
        }
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function A() {
          return viewEnv.getScale();
        }
        function p(e) {
          return viewEnv.pxToRem(e);
        }
        function D(e) {
          return viewEnv.remToPx(e);
        }
        function h(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function F() {
          return viewEnv.isFocused();
        }
        function C() {
          return viewEnv.isClientAccessible();
        }
        function B() {
          return viewEnv.setEventHandled();
        }
        function v() {
          return viewEnv.isEventHandled();
        }
        function b() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(n.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === n.W[t]), e),
            {},
          ),
          S = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          x = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => l });
        const a = ["args"];
        const n = 2,
          r = 16,
          s = 32,
          o = 64,
          i = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                s = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                  return n;
                })(t, a);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, s, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, t]) => {
                          const u = "GFValueProxy";
                          switch (typeof t) {
                            case "number":
                              return { __Type: u, name: e, number: t };
                            case "boolean":
                              return { __Type: u, name: e, bool: t };
                            default:
                              return { __Type: u, name: e, string: t.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, s));
            }
            return viewEnv.handleViewEvent({ __Type: u, type: e });
            var n;
          },
          l = {
            close(e) {
              i("popover" === e ? n : s);
            },
            minimize() {
              i(o);
            },
            move(e) {
              i(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      3377: (e, t, u) => {
        "use strict";
        u.d(t, { ZP: () => c });
        var a = u(5415),
          n = u(6179),
          r = u.n(n);
        const s = ["xl", "lg", "md", "sm", "xs"],
          o = (e) => e.includes("_") && ((e) => s.includes(e))(e.split("_").at(-1)),
          i = [a.cJ.ExtraLarge, a.cJ.Large, a.cJ.Medium, a.cJ.Small, a.cJ.ExtraSmall],
          l = (e, t) =>
            Object.keys(e).reduce((u, a) => {
              if (a in u) return u;
              if (o(a)) {
                const n = a.split("_").slice(0, -1).join("_");
                if (n in u) return u;
                const r = i.indexOf(t),
                  o = (-1 !== r ? s.slice(r) : [])
                    .map((e) => n + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  l = o ? e[o] : void 0;
                return ((u[n] = void 0 !== l ? l : e[n]), u);
              }
              const n = e[a];
              return (
                void 0 === n ||
                  ((e, t) => s.some((u) => void 0 !== t[`${e}_${u}`]))(a, e) ||
                  (u[a] = n),
                u
              );
            }, {}),
          c = (e, t = l) => {
            const u = (
              (e, t = l) =>
              (u) => {
                const s = (0, a.GS)().mediaSize,
                  o = (0, n.useMemo)(() => t(u, s), [u, s]);
                return r().createElement(e, o);
              }
            )(e, t);
            return r().memo((t) =>
              Object.keys(t).some((e) => o(e) && void 0 !== t[e])
                ? r().createElement(u, t)
                : r().createElement(e, t),
            );
          };
      },
      6536: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
        var a = u(6179);
        const n = (e) => {
          const t = (0, a.useRef)(!1);
          t.current || (e(), (t.current = !0));
        };
      },
      5415: (e, t, u) => {
        "use strict";
        u.d(t, { Aq: () => i, GS: () => l, cJ: () => s, fd: () => o });
        var a = u(6179),
          n = u(7739),
          r = u(1043);
        let s, o, i;
        (!(function (e) {
          ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = r.j.small.width)] = "Small"),
            (e[(e.Medium = r.j.medium.width)] = "Medium"),
            (e[(e.Large = r.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
        })(s || (s = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.width)] = "Small"),
              (e[(e.Medium = r.j.medium.width)] = "Medium"),
              (e[(e.Large = r.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
          })(o || (o = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.height)] = "Small"),
              (e[(e.Medium = r.j.medium.height)] = "Medium"),
              (e[(e.Large = r.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.height)] = "ExtraLarge"));
          })(i || (i = {})));
        const l = () => {
          const e = (0, a.useContext)(n.YN),
            t = e.width,
            u = e.height,
            r = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return s.ExtraLarge;
                case e.large:
                  return s.Large;
                case e.medium:
                  return s.Medium;
                case e.small:
                  return s.Small;
                case e.extraSmall:
                  return s.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), s.ExtraSmall);
              }
            })(e),
            l = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return o.ExtraLarge;
                case e.largeWidth:
                  return o.Large;
                case e.mediumWidth:
                  return o.Medium;
                case e.smallWidth:
                  return o.Small;
                case e.extraSmallWidth:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(e),
            c = ((e) => {
              switch (!0) {
                case e.extraLargeHeight:
                  return i.ExtraLarge;
                case e.largeHeight:
                  return i.Large;
                case e.mediumHeight:
                  return i.Medium;
                case e.smallHeight:
                  return i.Small;
                case e.extraSmallHeight:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(e);
          return {
            mediaSize: r,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: t,
            remScreenHeight: u,
          };
        };
      },
      5521: (e, t, u) => {
        "use strict";
        let a, n;
        (u.d(t, { n: () => a }),
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
          })(a || (a = {})),
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
      3649: (e, t, u) => {
        "use strict";
        let a;
        function n(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const u = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(u, -u)]);
          });
        }
        function r(e) {
          return e.replace(/-/g, "_");
        }
        (u.d(t, { BN: () => r, Uw: () => d, uF: () => n, v2: () => a }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(a || (a = {})));
        const s = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          o = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          i = (e, t, u = a.left) => e.split(t).reduce(u === a.left ? s : o, []),
          l = (() => {
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
            return (t) =>
              t
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(e);
          })(),
          c = ["zh_cn", "zh_sg", "zh_tw"],
          m = (e, t = a.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return c.includes(u)
              ? l(e)
              : ((e, t = a.left) => {
                  let u = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (i(r, /( )/, t).forEach((e) => (u = u.concat(i(e, n, a.left)))), u);
                })(e, t);
          },
          d = (e, t, u) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (u && e in u ? u[e] : m(e, t)));
      },
      728: (e, t, u) => {
        "use strict";
        let a;
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
        })(a || (a = {}));
      },
      1358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => r });
        var a = u(3138);
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
          addCallback(e, t, u = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = a.O.view.addModelObserver(e, u, n);
            return (
              r > 0
                ? ((this._callbacks[r] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(r) : (this._views[u] = [r])))
                : console.error("Can't add callback for model:", e),
              r
            );
          }
          removeCallback(e, t = 0) {
            let u = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((u = viewEnv.removeDataChangedCallback(e, t)), delete this._callbacks[e]),
              u || console.error("Can't remove callback by id:", e),
              u
            );
          }
          _emmitDataChanged(e, t, u) {
            u.forEach((u) => {
              const a = this._callbacks[u];
              void 0 !== a && a(e, t);
            });
          }
        }
        n.__instance = void 0;
        const r = n;
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
      4179: (e, t, u) => {
        "use strict";
        u.d(t, { B3: () => l, Z5: () => s, B0: () => i, ry: () => D });
        class a {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: u }) => {
                  let a = e.target;
                  do {
                    if (a === t) return;
                    a = a.parentNode;
                  } while (a);
                  u();
                });
              }));
          }
          static get instance() {
            return (a.__instance || (a.__instance = new a()), a.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const u = e,
              a = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== u || t !== a,
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
        a.__instance = void 0;
        const n = a;
        var r = u(1358);
        const s = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          o = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, u) => userLocale.getTimeFormat(e, t, void 0 === u || u),
            getTimeString: (e, t, u) => userLocale.getTimeString(e, t, void 0 === u || u),
          };
        let i;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(i || (i = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = u(5521),
          _ = u(3138);
        const g = ["args"];
        function A(e, t, u, a, n, r, s) {
          try {
            var o = e[r](s),
              i = o.value;
          } catch (e) {
            return void u(e);
          }
          o.done ? t(i) : Promise.resolve(i).then(a, n);
        }
        const p = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          D = (function () {
            var e,
              t =
                ((e = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((e) => {
                      engine.on("Ready", e);
                    })
                  );
                }),
                function () {
                  var t = this,
                    u = arguments;
                  return new Promise(function (a, n) {
                    var r = e.apply(t, u);
                    function s(e) {
                      A(r, a, n, s, o, "next", e);
                    }
                    function o(e) {
                      A(r, a, n, s, o, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          h = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const n = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                  return n;
                })(t, g);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, r, {
                      arguments:
                        ((a = n),
                        Object.entries(a).map(([e, t]) => {
                          const u = { __Type: "GFValueProxy", name: e };
                          switch (typeof t) {
                            case "number":
                              u.number = t;
                              break;
                            case "boolean":
                              u.bool = t;
                              break;
                            default:
                              u.string = t.toString();
                          }
                          return u;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var a;
          },
          F = () => h(i.CLOSE),
          C = (e, t) => {
            e.keyCode === E.n.ESCAPE && t();
          };
        var B = u(7572);
        const v = n.instance,
          b = {
            DataTracker: r.Z,
            ViewModel: B.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: m,
            DateFormatType: d,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => h(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: F,
            sendClosePopOverEvent: () => h(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, u = 0) => {
              h(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, u, a, n = R.invalid("resId"), r) => {
              const s = _.O.view.getViewGlobalPosition(),
                o = u.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                m = o.width,
                d = o.height,
                E = {
                  x: _.O.view.pxToRem(l) + s.x,
                  y: _.O.view.pxToRem(c) + s.y,
                  width: _.O.view.pxToRem(m),
                  height: _.O.view.pxToRem(d),
                };
              h(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: a || R.invalid("resId"),
                targetID: n,
                direction: t,
                bbox: p(E),
                on: !0,
                args: r,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => C(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              C(e, F);
            },
            handleViewEvent: h,
            onBindingsReady: D,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
            dumpViewModel: function e(t) {
              const u = {};
              if ("object" != typeof t) return t;
              for (const a in t)
                if (Object.prototype.hasOwnProperty.call(t, a)) {
                  const n = Object.prototype.toString.call(t[a]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = t[a];
                    u[a] = [];
                    for (let t = 0; t < n.length; t++) u[a].push({ value: e(n[t].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[a] = e(t[a]))
                      : (u[a] = t[a]);
                }
              return u;
            },
            ClickOutsideManager: v,
            SystemLocale: s,
            UserLocale: o,
          };
        window.ViewEnvHelper = b;
      },
      1630: (e, t, u) => {
        "use strict";
        var a = {};
        (u.r(a),
          u.d(a, {
            Area: () => vn,
            Bar: () => Fn,
            DefaultScroll: () => Bn,
            Direction: () => an,
            defaultSettings: () => nn,
            useHorizontalScrollApi: () => sn,
          }));
        var n = {};
        (u.r(n),
          u.d(n, {
            Area: () => $n,
            Bar: () => In,
            Default: () => Un,
            useVerticalScrollApi: () => bn,
          }));
        var r = u(7739),
          s = u(6179),
          o = u.n(s),
          i = u(6483),
          l = u.n(i),
          c = u(926),
          m = u.n(c),
          d = u(5415);
        const E = ["children", "className"];
        function _() {
          return (
            (_ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            _.apply(this, arguments)
          );
        }
        const g = {
            [d.fd.ExtraSmall]: "",
            [d.fd.Small]: m().SMALL_WIDTH,
            [d.fd.Medium]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH}`,
            [d.fd.Large]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH}`,
            [d.fd.ExtraLarge]:
              `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH} ${m().EXTRA_LARGE_WIDTH}`,
          },
          A = {
            [d.Aq.ExtraSmall]: "",
            [d.Aq.Small]: m().SMALL_HEIGHT,
            [d.Aq.Medium]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT}`,
            [d.Aq.Large]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT}`,
            [d.Aq.ExtraLarge]:
              `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT} ${m().EXTRA_LARGE_HEIGHT}`,
          },
          p = {
            [d.cJ.ExtraSmall]: "",
            [d.cJ.Small]: m().SMALL,
            [d.cJ.Medium]: `${m().SMALL} ${m().MEDIUM}`,
            [d.cJ.Large]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE}`,
            [d.cJ.ExtraLarge]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE} ${m().EXTRA_LARGE}`,
          },
          D = (e) => {
            let t = e.children,
              u = e.className,
              a = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, E);
            const n = (0, d.GS)(),
              r = n.mediaWidth,
              s = n.mediaHeight,
              i = n.mediaSize;
            return o().createElement("div", _({ className: l()(u, g[r], A[s], p[i]) }, a), t);
          },
          h = ["children"];
        const F = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, h);
          return o().createElement(r.ZN, null, o().createElement(D, u, t));
        };
        var C = u(493),
          B = u.n(C);
        function v() {}
        function b() {
          return !1;
        }
        console.log;
        var f = u(9174),
          w = u(3138);
        function S(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return x(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return x(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var a = 0;
            return function () {
              return a >= e.length ? { done: !0 } : { done: !1, value: e[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function x(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, a = new Array(t); u < t; u++) a[u] = e[u];
          return a;
        }
        const P = (e) => (0 === e ? window : window.subViews.get(e));
        const L = () => (e, t) => {
          const u = (0, s.createContext)({});
          return [
            function ({ mode: a = "real", options: n, children: r, mocks: i }) {
              const l = (0, s.useRef)([]),
                c = (u, a, n) => {
                  var r;
                  const s = (function ({
                      initializer: e = !0,
                      rootId: t = 0,
                      getRoot: u = P,
                      context: a = "model",
                    } = {}) {
                      const n = new Map();
                      function r(e, t = 0) {
                        viewEnv.removeDataChangedCallback(e, t)
                          ? n.delete(e)
                          : console.error("Can't remove callback by id:", e);
                      }
                      engine.whenReady.then(() => {
                        engine.on("viewEnv.onDataChanged", (e, t, u) => {
                          u.forEach((t) => {
                            const u = n.get(t);
                            void 0 !== u && u(e);
                          });
                        });
                      });
                      const s = (e) => {
                        const n = u(t),
                          r = a.split(".").reduce((e, t) => e[t], n);
                        return "string" != typeof e || 0 === e.length
                          ? r
                          : e.split(".").reduce((e, t) => {
                              const u = e[t];
                              return "function" == typeof u ? u.bind(e) : u;
                            }, r);
                      };
                      return {
                        subscribe: (u, r) => {
                          const o = "string" == typeof r ? `${a}.${r}` : a,
                            i = w.O.view.addModelObserver(o, t, !0);
                          return (n.set(i, u), e && u(s(r)), i);
                        },
                        readByPath: s,
                        createCallback: (e, t) => {
                          const u = s(t);
                          return (...t) => {
                            u(e(...t));
                          };
                        },
                        createCallbackNoArgs: (e) => {
                          const t = s(e);
                          return () => {
                            t();
                          };
                        },
                        dispose: function () {
                          for (var e, u = S(n.keys()); !(e = u()).done;) r(e.value, t);
                        },
                        unsubscribe: r,
                      };
                    })(a),
                    o =
                      "real" === u
                        ? s
                        : Object.assign({}, s, {
                            readByPath: null != (r = null == n ? void 0 : n.getter) ? r : () => {},
                          }),
                    i = (e) =>
                      "mocks" === u ? (null == n ? void 0 : n.getter(e)) : o.readByPath(e),
                    c = (e) => l.current.push(e),
                    m = e({
                      mode: u,
                      readByPath: i,
                      externalModel: o,
                      observableModel: {
                        array: (e, t) => {
                          const a = null != t ? t : i(e),
                            n = f.LO.box(a, { equals: b });
                          return (
                            "real" === u &&
                              o.subscribe(
                                (0, f.aD)((e) => n.set(e)),
                                e,
                              ),
                            n
                          );
                        },
                        object: (e, t) => {
                          const a = null != t ? t : i(e),
                            n = f.LO.box(a, { equals: b });
                          return (
                            "real" === u &&
                              o.subscribe(
                                (0, f.aD)((e) => n.set(e)),
                                e,
                              ),
                            n
                          );
                        },
                        primitives: (e, t) => {
                          const a = i(t);
                          if (Array.isArray(e)) {
                            const n = e.reduce((e, t) => ((e[t] = f.LO.box(a[t], {})), e), {});
                            return (
                              "real" === u &&
                                o.subscribe(
                                  (0, f.aD)((t) => {
                                    e.forEach((e) => {
                                      n[e].set(t[e]);
                                    });
                                  }),
                                  t,
                                ),
                              n
                            );
                          }
                          {
                            const n = e,
                              r = Object.entries(n),
                              s = r.reduce((e, [t, u]) => ((e[u] = f.LO.box(a[t], {})), e), {});
                            return (
                              "real" === u &&
                                o.subscribe(
                                  (0, f.aD)((e) => {
                                    r.forEach(([t, u]) => {
                                      s[u].set(e[t]);
                                    });
                                  }),
                                  t,
                                ),
                              s
                            );
                          }
                        },
                      },
                      cleanup: c,
                    }),
                    d = { mode: u, model: m, externalModel: o, cleanup: c };
                  return {
                    model: m,
                    controls: "mocks" === u && n ? n.controls(d) : t(d),
                    externalModel: o,
                    mode: u,
                  };
                },
                m = (0, s.useRef)(!1),
                d = (0, s.useState)(a),
                E = d[0],
                _ = d[1],
                g = (0, s.useState)(() => c(a, n, i)),
                A = g[0],
                p = g[1];
              return (
                (0, s.useEffect)(() => {
                  m.current ? p(c(E, n, i)) : (m.current = !0);
                }, [i, E, n]),
                (0, s.useEffect)(() => {
                  _(a);
                }, [a]),
                (0, s.useEffect)(
                  () => () => {
                    (A.externalModel.dispose(), l.current.forEach((e) => e()));
                  },
                  [A],
                ),
                o().createElement(u.Provider, { value: A }, r)
              );
            },
            () => (0, s.useContext)(u),
          ];
        };
        var y = u(3946);
        let T, N, M, k;
        (!(function (e) {
          ((e.Initialization = "initialization"),
            (e.Loading = "loading"),
            (e.ForceLoading = "forceLoading"),
            (e.Loaded = "loaded"));
        })(T || (T = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.Loading = "loading"),
              (e.Loaded = "loaded"),
              (e.Failed = "failed"));
          })(N || (N = {})),
          (function (e) {
            ((e.Initialization = "initialization"), (e.Loaded = "loaded"), (e.Failed = "failed"));
          })(M || (M = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.BrowserLoading = "browserLoading"),
              (e.PageLoading = "pageLoading"),
              (e.ForceLoading = "forceLoading"),
              (e.PageFailed = "pageFailed"),
              (e.TextureFailed = "textureFailed"),
              (e.Loaded = "loaded"));
          })(k || (k = {})));
        (T.Initialization, N.Initialization);
        const O = (e) => e > 0,
          I = (e) => !O(e);
        function H(e, t) {
          var u;
          if (I(e)) return void console.warn("Invalid id, should be greater than zero", e);
          const a = 0 === t.scale ? 1e-5 : null != (u = t.scale) ? u : 1;
          return w.O.view.getBrowserTexturePath(e, Math.max(t.width, 1), Math.max(t.height, 1), a);
        }
        const U = L()(
            ({ observableModel: e }) => {
              const t = e.object(),
                u = (0, y.Om)(() =>
                  (function ({ pageState: e, browserState: t, texState: u }) {
                    return t === T.Initialization
                      ? k.Initialization
                      : t === T.ForceLoading
                        ? k.ForceLoading
                        : t === T.Loading
                          ? k.BrowserLoading
                          : e === N.Loaded && t === T.Loaded && u === M.Loaded
                            ? k.Loaded
                            : u === M.Failed
                              ? k.TextureFailed
                              : e === N.Failed
                                ? k.PageFailed
                                : k.PageLoading;
                  })(t.get()),
                );
              return { root: t, getState: u };
            },
            ({ externalModel: e }) => ({
              blur: e.createCallbackNoArgs("unfocus"),
              focus: e.createCallbackNoArgs("focus"),
              createWebView: e.createCallbackNoArgs("createWebView"),
            }),
          ),
          $ = U[0],
          W = U[1],
          G = (e) => {
            (0, s.useEffect)(e, []);
          };
        var V = u(3403);
        function z() {
          const e = (0, s.useRef)(0);
          var t;
          return (
            (t = () => {
              window.cancelAnimationFrame(e.current);
            }),
            (0, s.useEffect)(() => t, []),
            (0, s.useMemo)(
              () => ({
                run: (t) => {
                  (window.cancelAnimationFrame(e.current),
                    (e.current = window.requestAnimationFrame(() => {
                      e.current = window.requestAnimationFrame(() => {
                        (t(), (e.current = 0));
                      });
                    })));
                },
                clear: () => {
                  (window.cancelAnimationFrame(e.current), (e.current = 0));
                },
                get isRunning() {
                  return 0 !== e.current;
                },
              }),
              [],
            )
          );
        }
        const j = "BrowserView_base_6b",
          X = "BrowserView_texture_17",
          q = "Spinner_base_87",
          Z = "Spinner_caption_cf",
          Y = "Spinner_gear_c4",
          K = "Spinner_logo_bf",
          Q = ({ message: e, className: t, classNames: u }) =>
            o().createElement(
              "div",
              { className: l()(q, t) },
              e &&
                o().createElement("div", { className: l()(Z, null == u ? void 0 : u.caption) }, e),
              o().createElement("div", { className: l()(Y, null == u ? void 0 : u.gear) }),
              o().createElement("div", { className: l()(K, null == u ? void 0 : u.logo) }),
            );
        function J(e) {
          engine.call("PlaySound", e);
        }
        const ee = {
            playHighlight() {
              J("highlight");
            },
            playClick() {
              J("play");
            },
            playYes() {
              J("yes1");
            },
          },
          te = {
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
        let ue, ae;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(ue || (ue = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(ae || (ae = {})));
        const ne = ({
          children: e,
          size: t,
          isFocused: u,
          type: a,
          disabled: n,
          mixClass: r,
          soundHover: i,
          soundClick: c,
          onMouseEnter: m,
          onMouseMove: d,
          onMouseDown: E,
          onMouseUp: _,
          onMouseLeave: g,
          onClick: A,
        }) => {
          const p = (0, s.useRef)(null),
            D = (0, s.useState)(u),
            h = D[0],
            F = D[1],
            C = (0, s.useState)(!1),
            B = C[0],
            v = C[1],
            b = (0, s.useState)(!1),
            f = b[0],
            w = b[1],
            S = (0, s.useCallback)(() => {
              n || (p.current && (p.current.focus(), F(!0)));
            }, [n]),
            x = (0, s.useCallback)(
              (e) => {
                h && null !== p.current && !p.current.contains(e.target) && F(!1);
              },
              [h],
            ),
            P = (0, s.useCallback)(
              (e) => {
                n || (A && A(e));
              },
              [n, A],
            ),
            L = (0, s.useCallback)(
              (e) => {
                n || (null !== i && J(i), m && m(e), w(!0));
              },
              [n, i, m],
            ),
            y = (0, s.useCallback)(
              (e) => {
                d && d(e);
              },
              [d],
            ),
            T = (0, s.useCallback)(
              (e) => {
                n || (_ && _(e), v(!1));
              },
              [n, _],
            ),
            N = (0, s.useCallback)(
              (e) => {
                n || (null !== c && J(c), E && E(e), u && S(), v(!0));
              },
              [n, c, E, S, u],
            ),
            M = (0, s.useCallback)(
              (e) => {
                n || (g && g(e), v(!1));
              },
              [n, g],
            ),
            k = l()(
              te.base,
              te[`base__${a}`],
              {
                [te.base__disabled]: n,
                [te[`base__${t}`]]: t,
                [te.base__focus]: h,
                [te.base__highlightActive]: B,
                [te.base__firstHover]: f,
              },
              r,
            ),
            O = l()(te.state, te.state__default);
          return (
            (0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", x),
                () => {
                  document.removeEventListener("mousedown", x);
                }
              ),
              [x],
            ),
            (0, s.useEffect)(() => {
              F(u);
            }, [u]),
            o().createElement(
              "div",
              {
                ref: p,
                className: k,
                onMouseEnter: L,
                onMouseMove: y,
                onMouseUp: T,
                onMouseDown: N,
                onMouseLeave: M,
                onClick: P,
              },
              a !== ue.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: te.back }),
                  o().createElement("span", { className: te.texture }),
                ),
              o().createElement(
                "span",
                { className: O },
                o().createElement("span", { className: te.stateDisabled }),
                o().createElement("span", { className: te.stateHighlightHover }),
                o().createElement("span", { className: te.stateHighlightActive }),
              ),
              o().createElement(
                "span",
                { className: te.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        ne.defaultProps = {
          type: ue.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const re = (0, s.memo)(ne),
          se = "Error_base_46",
          oe = "Error_alertIcon_04",
          ie = "Error_errorCaption_f2",
          le = "Error_button_cd",
          ce = ({ errorBtnLabel: e, errorBtnClickHandler: t, errorMessage: u }) =>
            o().createElement(
              "div",
              { className: se },
              o().createElement("div", { className: oe }),
              o().createElement("div", { className: ie }, u),
              o().createElement(re, { size: ae.medium, mixClass: le, onClick: t }, e),
            );
        ce.defaultProps = { errorBtnLabel: "", errorMessage: "" };
        const me = "Waiting_base_c5",
          de = "Waiting_blackOverlay_55",
          Ee = ({
            message: e,
            isError: t,
            errorMessage: u,
            errorBtnLabel: a,
            errorBtnClickHandler: n,
            overlayAlpha: r,
          }) => {
            const i = o().createRef();
            return (
              (0, s.useEffect)(() => {
                const e = i.current;
                e && r && (e.style.opacity = r);
              }, [i, r]),
              o().createElement(
                "div",
                { className: me },
                o().createElement("div", { className: de, ref: i }),
                t
                  ? o().createElement(ce, {
                      errorBtnLabel: a,
                      errorMessage: u,
                      errorBtnClickHandler: n,
                    })
                  : o().createElement(Q, { message: e }),
              )
            );
          };
        Ee.defaultProps = {
          isError: !1,
          message: "",
          overlayAlpha: "0.8",
          errorBtnLabel: R.strings.dialogs.disconnected.cancel(),
          errorMessage: "",
        };
        const _e = "DisplayBrowserState_base_e7",
          ge = "DisplayBrowserState_error_4e",
          Ae = "DisplayBrowserState_alertIcon_c4",
          pe = "DisplayBrowserState_errorCaption_dd",
          De = ({ waitingText: e, className: t }) =>
            o().createElement(
              "div",
              { className: l()(_e, t) },
              o().createElement(Ee, { errorBtnClickHandler: v, message: e }),
            ),
          he = () =>
            o().createElement(
              "div",
              { className: ge },
              o().createElement("div", { className: Ae }),
              o().createElement(
                "div",
                { className: pe },
                R.strings.dialogs.messenger.userInfoNotAvailable.title(),
              ),
            ),
          Fe = () =>
            o().createElement(
              "div",
              { className: ge },
              o().createElement("div", { className: Ae }),
              o().createElement(
                "div",
                { className: pe },
                R.strings.dialogs.inGameBrowser.textureLoadingFailed.title(),
              ),
              o().createElement(
                "div",
                { className: pe },
                R.strings.dialogs.inGameBrowser.textureLoadingFailed.message(),
              ),
            );
        function Ce(e) {
          const t = (0, s.useRef)(e);
          return (
            (function (e) {
              return e !== k.BrowserLoading && e !== k.PageLoading;
            })(e) && (t.current = e),
            t.current
          );
        }
        function Be(e) {
          const t = (function (e) {
              const t = (0, s.useRef)(!1);
              return (
                (e !== k.Loaded && e !== k.PageFailed && e !== k.TextureFailed) || (t.current = !0),
                t.current
              );
            })(e),
            u = Ce(e);
          return t ? u : e;
        }
        const ve = ({ viewState: e, waitingText: t, waitingClassName: u }) => {
            switch (Be(e)) {
              case k.BrowserLoading:
              case k.PageLoading:
              case k.ForceLoading:
                return o().createElement(De, { waitingText: t, className: u });
              case k.PageFailed:
                return o().createElement(he, null);
              case k.TextureFailed:
                return o().createElement(Fe, null);
              default:
                return null;
            }
          },
          be = (e) =>
            "width" in e &&
            "height" in e &&
            "number" == typeof e.width &&
            "number" == typeof e.height;
        function fe(e) {
          return null != e ? e : viewEnv.getScale();
        }
        function we(e) {
          const t = (0, s.useState)(fe(e.scale)),
            u = t[0],
            a = t[1],
            n = (function (e) {
              return be(e) ? H(e.id, e) : void 0;
            })(Object.assign({}, e, { scale: u })),
            r = (0, s.useState)(n),
            o = r[0],
            i = r[1],
            l = (0, s.useRef)(!1),
            c = "width" in e ? e.width : 0,
            m = "height" in e ? e.height : 0,
            d = z();
          return (
            (0, s.useEffect)(() => {
              const t = () => {
                a(fe(e.scale));
              };
              return (
                window.addEventListener("resize", t),
                () => {
                  window.removeEventListener("resize", t);
                }
              );
            }, [e.scale]),
            (0, s.useEffect)(() => {
              if (void 0 === n || 0 === c || 0 === m || n === o) return;
              const e = () => {
                i(n);
              };
              if (!1 === l.current) return ((l.current = !0), void e());
              const t = new Image(),
                u = () => {
                  d.run(e);
                };
              return (
                t.addEventListener("load", u),
                (t.src = n),
                () => {
                  (t.removeEventListener("load", u), (t.src = ""));
                }
              );
            }, [n, o]),
            o
          );
        }
        const Se = o().memo(function (e) {
            const t = e.id,
              u = e.className,
              a = e.classNameTexture,
              n = e.waitingClassName,
              r = e.onMouseEnter,
              s = e.onMouseLeave,
              i = e.onMouseWheel,
              c = e.onMouseMove,
              m = e.onMouseDown,
              d = e.onMouseUp,
              E = e.renderStateDisplay,
              _ = e.viewState,
              g = e.statusCode,
              A = e.waitingText,
              p = e.scrollSpeed,
              D = void 0 === p ? 20 : p,
              h = we(e);
            return o().createElement(
              "div",
              { className: l()(j, u), onMouseEnter: r, onMouseLeave: s },
              h &&
                o().createElement("div", {
                  onWheel: i,
                  onMouseMove: c,
                  onMouseDown: m,
                  onMouseUp: d,
                  className: l()(j, X, a),
                  "data-browser-id": t,
                  "data-browser-scroll-speed": D,
                  style: { backgroundImage: `url(${h})` },
                }),
              "function" == typeof E
                ? E({ viewState: _, statusCode: g, waitingText: A, waitingClassName: n })
                : o().createElement(ve, {
                    viewState: _,
                    statusCode: g,
                    waitingText: A,
                    waitingClassName: n,
                  }),
            );
          }),
          xe = (e) => {
            let t,
              u = null;
            return (
              (u = requestAnimationFrame(() => {
                u = requestAnimationFrame(() => {
                  ((u = null), (t = e()));
                });
              })),
              () => {
                ("function" == typeof t && t(), null !== u && cancelAnimationFrame(u));
              }
            );
          },
          Re = (e, t = []) => {
            const u = (0, s.useRef)(),
              a = (0, s.useCallback)((...t) => {
                (u.current && u.current(), (u.current = e(...t)));
              }, t);
            return (
              (0, s.useEffect)(
                () => () => {
                  u.current && u.current();
                },
                [a],
              ),
              a
            );
          },
          Pe = "none-ref",
          Le = "measured",
          ye = { type: "measuring" };
        function Te() {
          return (
            (Te =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Te.apply(this, arguments)
          );
        }
        const Ne = o().memo(function (e) {
          const t = (function () {
              const e = (0, s.useRef)(null),
                t = (0, s.useState)(ye),
                u = t[0],
                a = t[1],
                n = Re(
                  () => (
                    a(ye),
                    xe(() => {
                      e.current
                        ? a({
                            type: Le,
                            size: { width: e.current.offsetWidth, height: e.current.offsetHeight },
                          })
                        : a({ type: Pe });
                    })
                  ),
                  [],
                );
              return (
                (0, s.useEffect)(
                  () => (
                    window.addEventListener("resize", n),
                    n(),
                    () => window.removeEventListener("resize", n)
                  ),
                  [n],
                ),
                [e, u, n]
              );
            })(),
            u = t[0],
            a = t[1];
          return o().createElement(
            "div",
            { ref: u, className: j },
            o().createElement(
              Se,
              Te(
                {},
                e,
                (function (e, t = {}) {
                  return "measured" === e.type ? Object.assign({}, e.size, t) : t;
                })(a),
              ),
            ),
          );
        });
        function Me() {
          return (
            (Me =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Me.apply(this, arguments)
          );
        }
        const ke = (0, V.Pi)(function (e) {
            const t = e.defaultWaitingText,
              u = e.className,
              a = e.waitingClassName,
              n = e.isLazy,
              r = void 0 === n || n,
              i = e.displayContentWhenLoading,
              l = void 0 === i || i,
              c = e.renderStateDisplay,
              m = e.onMouseEnter,
              d = e.onMouseLeave,
              E = e.onMouseMove,
              _ = e.onMouseWheel,
              g = e.onMouseDown,
              A = e.onMouseUp,
              p = W(),
              D = p.model,
              h = p.controls,
              F = D.root.get(),
              C = F.id,
              B = F.httpStatusCode,
              v = F.waitingMessage,
              b = D.getState(),
              f = l || b === k.Loaded;
            (G(() => {
              r && I(C) && h.createWebView();
            }),
              (0, s.useEffect)(() => {
                O(C) && h.focus();
              }, [C, h]),
              G(
                () => (
                  window.addEventListener("mouseleave", h.blur),
                  window.addEventListener("mouseenter", h.focus),
                  () => {
                    (window.removeEventListener("mouseleave", h.blur),
                      window.removeEventListener("mouseenter", h.focus));
                  }
                ),
              ));
            const w = (0, s.useMemo)(() => {
              const e = {
                onMouseEnter: m,
                onMouseLeave: d,
                onMouseMove: E,
                onMouseWheel: _,
                onMouseDown: g,
                onMouseUp: A,
              };
              return f
                ? Object.assign({}, e, {
                    onMouseEnter: (e) => {
                      (h.focus(), null == m || m(e));
                    },
                    onMouseLeave: (e) => {
                      (h.blur(), null == d || d(e));
                    },
                  })
                : e;
            }, [f, h, g, m, d, E, A, _]);
            if (I(C)) return null;
            const S = be(e)
                ? (function (e, t) {
                    const u = {};
                    return (
                      t.forEach((t) => {
                        u[t] = e[t];
                      }),
                      u
                    );
                  })(e, ["width", "height"])
                : {},
              x = v.length > 0 ? v : t;
            return e.isFullSize
              ? o().createElement(
                  Ne,
                  Me({}, w, {
                    id: C,
                    className: u,
                    waitingClassName: a,
                    statusCode: B,
                    viewState: b,
                    waitingText: x,
                    renderStateDisplay: c,
                  }),
                )
              : o().createElement(
                  Se,
                  Me({}, w, S, {
                    id: C,
                    className: u,
                    waitingClassName: a,
                    statusCode: B,
                    viewState: b,
                    waitingText: x,
                    renderStateDisplay: c,
                  }),
                );
          }),
          Oe = ["options", "mocks", "mode"];
        const Ie = (0, s.memo)(function (e) {
            let t = e.options,
              u = e.mocks,
              a = e.mode,
              n = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Oe);
            return o().createElement(
              $,
              { options: t, mocks: u, mode: a },
              o().createElement(ke, n),
            );
          }),
          He = {
            base: "TextButton_base_b6",
            base__right: "TextButton_base__right_39",
            icon: "TextButton_icon_17",
            icon__back: "TextButton_icon__back_43",
            icon__forward: "TextButton_icon__forward_59",
            icon__close: "TextButton_icon__close_53",
            icon__info: "TextButton_icon__info_33",
            glow: "TextButton_glow_a4",
            caption: "TextButton_caption_82",
            caption__back: "TextButton_caption__back_b9",
            caption__forward: "TextButton_caption__forward_4e",
            caption__close: "TextButton_caption__close_36",
            caption__info: "TextButton_caption__info_23",
            goto: "TextButton_goto_e7",
            base__left: "TextButton_base__left_ff",
            shine: "TextButton_shine_e2",
          },
          Ue = [
            "caption",
            "onClick",
            "goto",
            "side",
            "type",
            "classNames",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onMouseUp",
            "soundClick",
            "soundHover",
          ];
        function $e() {
          return (
            ($e =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            $e.apply(this, arguments)
          );
        }
        class We extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && J(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && J(this.props.soundClick));
              }),
              (this._onMouseUp = (e) => (t) => {
                (e && e(t), this.setState({ click: !1 }));
              }),
              (this.handleFocus = () => this.setState({ focus: !0 })),
              (this.handleBlur = () => this.setState({ focus: !1 })));
          }
          render() {
            const e = this.props,
              t = e.caption,
              u = e.onClick,
              a = e.goto,
              n = e.side,
              r = e.type,
              s = e.classNames,
              i = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onMouseUp,
              E =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var u,
                    a,
                    n = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                  return n;
                })(e, Ue)),
              _ = l()(He.base, He[`base__${r}`], He[`base__${n}`], null == s ? void 0 : s.base),
              g = l()(He.icon, He[`icon__${r}`], He[`icon__${n}`], null == s ? void 0 : s.icon),
              A = l()(He.glow, null == s ? void 0 : s.glow),
              p = l()(He.caption, He[`caption__${r}`], null == s ? void 0 : s.caption),
              D = l()(He.goto, null == s ? void 0 : s.goto);
            return o().createElement(
              "div",
              $e(
                {
                  className: _,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(m),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: u,
                },
                E,
              ),
              "info" !== r && o().createElement("div", { className: He.shine }),
              o().createElement(
                "div",
                { className: g },
                o().createElement("div", { className: A }),
              ),
              o().createElement("div", { className: p }, t),
              a && o().createElement("div", { className: D }, a),
            );
          }
        }
        let Ge, Ve;
        ((We.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        }),
          (function (e) {
            ((e.DEFAULT = "default"),
              (e.DISABLED = "disabled"),
              (e.ACTIVE = "active"),
              (e.FINISHED = "finished"),
              (e.ANNOUNCEMENT = "announcement"),
              (e.PAUSED = "paused"));
          })(Ge || (Ge = {})),
          (function (e) {
            ((e[(e.progress = 0)] = "progress"),
              (e[(e.chapters = 2)] = "chapters"),
              (e[(e.about = 3)] = "about"));
          })(Ve || (Ve = {})));
        var ze = u(5521),
          je = u(4179);
        const Xe = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function qe(e = ze.n.NONE, t = Xe, u = !1) {
          (0, s.useEffect)(() => {
            if (e !== ze.n.NONE)
              return (
                window.addEventListener("keydown", a, u),
                () => {
                  window.removeEventListener("keydown", a, u);
                }
              );
            function a(a) {
              if (a.keyCode === e) {
                if (w.O.view.isEventHandled()) return;
                (w.O.view.setEventHandled(), t(a), u && a.stopPropagation());
              }
            }
          }, [t, e, u]);
        }
        var Ze = u(1685);
        const Ye = (e) => {
          return null !== e && "object" == typeof e
            ? "CoherentArrayProxy" === e.constructor.name
              ? ((t = e),
                (u = (e) => ("object" == typeof e ? Ye(e) : e)),
                Array.isArray(t)
                  ? t.map(u)
                  : t.map((e, t, a) => u(null == e ? void 0 : e.value, t, a)))
              : Array.isArray(e)
                ? e.map((e) => ("object" == typeof e ? Ye(e) : e))
                : Object.fromEntries(
                    Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? Ye(t) : t]),
                  )
            : e;
          var t, u;
        };
        var Ke = u(8998);
        const Qe = { 1: [10545, 7937281, 33825], 2: [7937601, 7938385, 7937041], 3: [] },
          Je = L()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  progression: e.object("progression"),
                  stages: e.array("progression.stages"),
                },
                u = (0, y.Om)(() => t.progression.get().currentStage, { equals: b }),
                a = (0, y.Om)(() => t.root.get().previewSeasonId, { equals: b }),
                n = (0, y.Om)(
                  () => {
                    return ((e = t.stages.get()), Ye(e)).map((e) =>
                      Object.assign({}, e, {
                        levels: e.levels.map((t) =>
                          Object.assign({}, t, {
                            hasSelectableRewards: t.rewards.some((e) =>
                              e.value.startsWith("paragon_rewards_choice"),
                            ),
                            rewards: t.rewards.map((u) => (0, Ke.lW)(u, t.number, e.id)),
                          }),
                        ),
                        finalVehicleCDs: Qe[e.id],
                      }),
                    );
                    var e;
                  },
                  { equals: b },
                ),
                r = (0, y.Om)(() => n().find((e) => e.id === a()), { equals: b }),
                s = (0, y.Om)(() => n().find((e) => e.id === u()), { equals: b }),
                o = (0, y.Om)(
                  () => {
                    const e = r() || s();
                    return e ? e.levels[e.levels.length - 1 || 0].maxPoints : 0;
                  },
                  { equals: b },
                ),
                i = (0, y.Om)((e) => n().filter((t) => t.chapterStatus.status === e).length, {
                  equals: b,
                }),
                l = (0, y.Om)(
                  () => n().length - i(Ge.FINISHED) + i(Ge.DISABLED) + i(Ge.ANNOUNCEMENT) === 0,
                  { equals: b },
                );
              return Object.assign({}, t, {
                computes: {
                  getStages: n,
                  hasActiveSeason: () => i(Ge.ACTIVE),
                  isAllAvailableSeasonsCompleted: l,
                  getCurrentStageNumber: u,
                  getCurrentSeason: s,
                  getPreviewSeason: r,
                  getCurrentSeasonMaxPointsCount: o,
                },
              });
            },
            ({ externalModel: e, cleanup: t }) => {
              const u = window.subViews.addChildChangedCallback(Ve.about);
              return (
                t(() => {
                  window.subViews.removeChildChangedCallback(u);
                }),
                {
                  onBack: e.createCallbackNoArgs("onBack"),
                  onBackToSeasons: e.createCallbackNoArgs("onBackToSeasons"),
                  onClose: e.createCallbackNoArgs("onClose"),
                  onToStagesView: e.createCallbackNoArgs("onToChaptersView"),
                  onTabChange: e.createCallback((e) => ({ tabId: e }), "onTabChange"),
                  onPreviewVehicle: e.createCallback(
                    (e, t) => ({ vehicleCD: e, seasonID: t }),
                    "progression.onPreviewVehicle",
                  ),
                  onSelectVehicleReward: e.createCallback(
                    (e, t, u) => ({ levelID: e, entCode: t, chapterID: u }),
                    "progression.onSelectVehicle",
                  ),
                  onSelectChapter: e.createCallback(
                    (e) => ({ id: e }),
                    "allChapters.onSelectChapter",
                  ),
                  onToChapterRewards: e.createCallback(
                    (e) => ({ id: e }),
                    "allChapters.onToChapterRewards",
                  ),
                  onPreviewStyle: e.createCallback(
                    (e, t, u) => ({ styleID: e, group: t, styleLevel: u }),
                    "progression.onPreviewStyle",
                  ),
                  onSeasonActivate: e.createCallback((e) => ({ id: e }), "onSeasonActivate"),
                }
              );
            },
          ),
          et = Je[0],
          tt = Je[1],
          ut = "App_base_4b",
          at = "App_infoBackground_84",
          nt = "App_vignette_ba",
          rt = "App_button_76",
          st = "App_back_b6",
          ot = "App_close_76",
          it = "App_navigationContainer_c0",
          lt = "App_navigation_01",
          ct = "App_content_3b",
          mt = "App_infoHeaderWrapper_74",
          dt = "App_infoContainer_af";
        var Et = u(7613);
        const _t = [
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
        function gt(e) {
          return Object.entries(e || {}).map(([e, t]) => {
            const u = { __Type: "GFValueProxy", name: e };
            switch (typeof t) {
              case "number":
                u.number = t;
                break;
              case "boolean":
                u.bool = t;
                break;
              case "undefined":
                break;
              default:
                u.string = t.toString();
            }
            return u;
          });
        }
        const At = (e, t, u = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: je.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: a,
                },
                u,
              ),
            );
          },
          pt = (e) => {
            let t = e.children,
              u = e.contentId,
              a = e.args,
              n = e.onMouseEnter,
              r = e.onMouseLeave,
              o = e.onMouseDown,
              i = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              m = e.ignoreMouseClick,
              d = void 0 !== m && m,
              E = e.decoratorId,
              _ = void 0 === E ? 0 : E,
              g = e.isEnabled,
              A = void 0 === g || g,
              p = e.targetId,
              D = void 0 === p ? 0 : p,
              h = e.onShow,
              F = e.onHide,
              C = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, _t);
            const B = (0, s.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              v = (0, s.useMemo)(
                () =>
                  D ||
                  ((e = 1) => {
                    const t = new Error().stack;
                    let u,
                      a = R.invalid("resId");
                    return (
                      t &&
                        ((u = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== u &&
                          window.subViews[u] &&
                          (a = window.subViews[u].id)),
                      { caller: u, stack: t, resId: a }
                    );
                  })().resId,
                [D],
              ),
              b = (0, s.useCallback)(() => {
                (B.current.isVisible && B.current.timeoutId) ||
                  (At(u, _, { isMouseEvent: !0, on: !0, arguments: gt(a) }, v),
                  h && h(),
                  (B.current.isVisible = !0));
              }, [u, _, a, v, h]),
              f = (0, s.useCallback)(() => {
                if (B.current.isVisible || B.current.timeoutId) {
                  const e = B.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (B.current.timeoutId = 0)),
                    At(u, _, { on: !1 }, v),
                    B.current.isVisible && F && F(),
                    (B.current.isVisible = !1));
                }
              }, [u, _, v, F]),
              w = (0, s.useCallback)((e) => {
                B.current.isVisible &&
                  ((B.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (B.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(B.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, s.useEffect)(() => {
              const e = B.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, s.useEffect)(() => {
                !1 === A && f();
              }, [A, f]),
              (0, s.useEffect)(
                () => (
                  window.addEventListener("mouseleave", f),
                  () => {
                    (window.removeEventListener("mouseleave", f), f());
                  }
                ),
                [f],
              ));
            return A
              ? (0, s.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((B.current.timeoutId = window.setTimeout(b, c ? 100 : 400)),
                            n && n(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (f(), null == r || r(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === d && f(), null == i || i(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === d && f(), null == o || o(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    C,
                  ),
                )
              : t;
            var S;
          },
          Dt = ["children", "body", "header", "note", "alert", "args"];
        function ht() {
          return (
            (ht =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            ht.apply(this, arguments)
          );
        }
        const Ft = R.views.common.tooltip_window.simple_tooltip_content,
          Ct = (e) => {
            let t = e.children,
              u = e.body,
              a = e.header,
              n = e.note,
              r = e.alert,
              i = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Dt);
            const c = (0, s.useMemo)(() => {
              const e = Object.assign({}, i, { body: u, header: a, note: n, alert: r });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [r, u, a, n, i]);
            return o().createElement(
              pt,
              ht(
                {
                  contentId:
                    ((m = null == i ? void 0 : i.hasHtmlContent),
                    m ? Ft.SimpleTooltipHtmlContent("resId") : Ft.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var m;
          },
          Bt = "NavItem_base_22",
          vt = "NavItem_base__hovered_1d",
          bt = "NavItem_base__selected_6d",
          ft = "NavItem_border_dc",
          wt = "NavItem_border__visible_10",
          St = "NavItem_glow_e8",
          xt = "NavItem_glow__visible_f5",
          Rt = "NavItem_icon_d8",
          Pt = "NavItem_icon__invsible_e5",
          Lt = "NavItem_icon__visible_f9",
          yt = "NavItem_text_3d",
          Tt = "NavItem_bubble_74",
          Nt = "R.images.gui.maps.icons.paragons.navigation.icons",
          Mt = R.strings.paragons.navigation,
          kt = (0, s.memo)(
            ({ tabId: e, seasonId: t, isSelected: u, hasNewItems: a, onClick: n }) => {
              const r = (0, s.useState)(!1),
                i = r[0],
                c = r[1],
                m = (0, d.GS)().mediaSize >= d.cJ.Medium ? "_large" : "",
                E = Number(e) === Number(Ve.progress) ? `season_${t}_` : "",
                _ = l()(Bt, i && vt, u && bt);
              return o().createElement(
                Ct,
                {
                  header: String(Mt.tooltip.header.$dyn(Ve[e])),
                  body: String(Mt.tooltip.body.$dyn(`${Ve[e]}`)),
                },
                o().createElement(
                  "div",
                  {
                    className: _,
                    onMouseEnter: () => {
                      (ee.playHighlight(), c(!0));
                    },
                    onMouseLeave: () => {
                      c(!1);
                    },
                    onClick: () => {
                      (n(), ee.playClick());
                    },
                  },
                  o().createElement("div", { className: l()(ft, u && wt) }),
                  o().createElement("div", { className: l()(St, u && xt) }),
                  a && o().createElement("div", { className: Tt }),
                  o().createElement("div", {
                    className: Rt,
                    style: { backgroundImage: `url(${Nt}.${E + Ve[e] + m})` },
                  }),
                  o().createElement("div", {
                    className: l()(Rt, Pt, (u || i) && Lt),
                    style: { backgroundImage: `url(${Nt}.${E + Ve[e] + m + "_active"})` },
                  }),
                  o().createElement(Et.ZP, { text: String(Mt.$dyn(Ve[e])), className: yt }),
                ),
              );
            },
          ),
          Ot = {
            base: "ActionButton_base_a0",
            base__hovered: "ActionButton_base__hovered_ea",
            icon: "ActionButton_icon_6f",
            icon__small: "ActionButton_icon__small_50",
            icon__normal: "ActionButton_icon__normal_d8",
            base__mouseDown: "ActionButton_base__mouseDown_b7",
            label: "ActionButton_label_76",
            base__visibleLabel: "ActionButton_base__visibleLabel_f7",
          };
        let It, Ht;
        (!(function (e) {
          ((e.COMPARE = "compare"), (e.PREVIEW = "preview"));
        })(It || (It = {})),
          (function (e) {
            ((e.SMALL = "small"), (e.NORMAL = "normal"));
          })(Ht || (Ht = {})));
        const Ut = [
          "label",
          "isVisibleLabel",
          "autofocus",
          "soundHover",
          "soundClick",
          "size",
          "onClick",
          "onMouseEnter",
          "onMouseLeave",
          "onMouseDown",
          "onMouseUp",
          "onFocus",
          "onBlur",
          "type",
        ];
        function $t() {
          return (
            ($t =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            $t.apply(this, arguments)
          );
        }
        const Wt = {
            [It.PREVIEW]: "R.images.gui.maps.icons.library.previewVehicle",
            [It.COMPARE]: "R.images.gui.maps.icons.library.compareVehicle",
          },
          Gt = (0, s.memo)((e) => {
            let t = e.label,
              u = e.isVisibleLabel,
              a = void 0 !== u && u,
              n = e.autofocus,
              r = void 0 !== n && n,
              i = e.soundHover,
              c = void 0 === i ? "highlight" : i,
              m = e.soundClick,
              d = void 0 === m ? "play" : m,
              E = e.size,
              _ = void 0 === E ? Ht.NORMAL : E,
              g = e.onClick,
              A = e.onMouseEnter,
              p = e.onMouseLeave,
              D = e.onMouseDown,
              h = e.onMouseUp,
              F = e.onFocus,
              C = e.onBlur,
              B = e.type,
              v = void 0 === B ? It.PREVIEW : B,
              b = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Ut);
            const f = (0, s.useState)(!1),
              w = f[0],
              S = f[1],
              x = (0, s.useState)(!1),
              R = x[0],
              P = x[1],
              L = (0, s.useState)(r),
              y = L[0],
              T = L[1],
              N = (0, s.useRef)(null),
              M = (0, s.useCallback)(() => {
                N.current && (N.current.focus(), T(!0));
              }, []),
              k = (0, s.useCallback)(
                (e) => {
                  y && null !== N.current && !N.current.contains(e.target) && T(!1);
                },
                [y],
              );
            ((0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", k),
                () => {
                  document.removeEventListener("mousedown", k);
                }
              ),
              [k],
            ),
              (0, s.useEffect)(() => {
                T(r);
              }, [r]));
            const O = (0, s.useCallback)(
                (e) => {
                  g && g(e);
                },
                [g],
              ),
              I = (0, s.useCallback)(
                (e) => {
                  (S(!0), D && D(e), d && J(d), r && M());
                },
                [r, D, M, d],
              ),
              H = (0, s.useCallback)(
                (e) => {
                  (S(!1), h && h(e));
                },
                [h],
              ),
              U = (0, s.useCallback)(
                (e) => {
                  (A && A(e), c && J(c), P(!0));
                },
                [A, c],
              ),
              $ = (0, s.useCallback)(
                (e) => {
                  (S(!1), P(!1), p && p(e));
                },
                [p],
              ),
              W = (0, s.useCallback)(
                (e) => {
                  (T(!0), F && F(e));
                },
                [F],
              ),
              G = (0, s.useCallback)(
                (e) => {
                  (T(!1), C && C(e));
                },
                [C],
              ),
              V = l()(
                Ot.base,
                a && Ot.base__visibleLabel,
                w && Ot.base__mouseDown,
                R && Ot.base__hovered,
                y && Ot.base__focused,
              ),
              z = l()(Ot.icon, Ot[`icon__${_}`]);
            return o().createElement(
              "div",
              $t(
                {
                  ref: N,
                  className: V,
                  onClick: O,
                  onMouseEnter: U,
                  onMouseLeave: $,
                  onMouseDown: I,
                  onMouseUp: H,
                  onFocus: W,
                  onBlur: G,
                },
                b,
              ),
              o().createElement("div", {
                className: z,
                style: { backgroundImage: `url(${Wt[v]})` },
              }),
              o().createElement("div", { className: Ot.label }, t),
            );
          });
        var Vt = u(7104);
        const zt = (e, t, u) => (u < e ? e : u > t ? t : u),
          jt = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let Xt, qt;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(Xt || (Xt = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(qt || (qt = {})));
        const Zt = ({ size: e = Xt.Default, classMix: t }) =>
            o().createElement("div", { className: l()(jt.background, jt[`background__${e}`], t) }),
          Yt = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          Kt = ({ size: e }) => {
            const t = l()(Yt.base, Yt[`base__${e}`]);
            return o().createElement("div", { className: t });
          },
          Qt = {
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
          Jt = (0, s.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: u,
              baseStyles: a,
              isComplete: n,
              withoutBounce: r,
            }) => {
              const s = l()(
                  Qt.base,
                  Qt[`base__${e}`],
                  u && Qt.base__disabled,
                  n && Qt.base__finished,
                  r && Qt.base__withoutBounce,
                ),
                i = !u && !n;
              return o().createElement(
                "div",
                { className: s, style: a, ref: t },
                o().createElement("div", { className: Qt.pattern }),
                o().createElement("div", { className: Qt.gradient }),
                i && o().createElement(Kt, { size: e }),
              );
            },
          ),
          eu = ({ size: e, value: t, lineRef: u, disabled: a, onComplete: n }) => {
            const r = (0, s.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              i = 100 === t;
            return (
              (0, s.useEffect)(() => {
                i && n && n();
              }, [i, n]),
              o().createElement(Jt, {
                size: e,
                disabled: a,
                baseStyles: r,
                isComplete: i,
                lineRef: u,
              })
            );
          },
          tu = (e, t) => {
            let u;
            const a = setTimeout(() => {
              u = e();
            }, t);
            return () => {
              ("function" == typeof u && u(), clearTimeout(a));
            };
          };
        let uu, au;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(uu || (uu = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(au || (au = {})));
        const nu = "ProgressBarDeltaSimple_base_6c",
          ru = "ProgressBarDeltaSimple_delta_99",
          su = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: a,
              size: n,
              to: r,
              onEndAnimation: i,
              onChangeAnimationState: l,
            }) => {
              const c = r < a,
                m = (0, s.useState)(au.Idle),
                d = m[0],
                E = m[1],
                _ = d === au.In,
                g = d === au.End,
                A = d === au.Idle,
                p = (0, s.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                );
              ((0, s.useEffect)(() => {
                if (A && !u) {
                  return tu(() => {
                    p(au.In);
                  }, t);
                }
              }, [p, u, A, t]),
                (0, s.useEffect)(() => {
                  if (_) {
                    return tu(() => {
                      (i && i(), p(au.End));
                    }, e + t);
                  }
                }, [p, _, i, t, e]));
              const D = (0, s.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                h = (0, s.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                F = (0, s.useMemo)(
                  () => ({ width: `${Math.abs(a - r)}%`, left: `${c ? r : a}%` }),
                  [a, c, r],
                );
              return g
                ? null
                : o().createElement(
                    "div",
                    { className: nu, style: F },
                    o().createElement(
                      "div",
                      { style: A ? D : h, className: ru },
                      o().createElement(Kt, { size: n }),
                    ),
                  );
            },
          ),
          ou = (0, s.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: a,
              disabled: n,
              isComplete: r,
              animationSettings: i,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const m = (0, s.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${i.line.duration}ms`,
                  transitionDelay: `${i.line.delay}ms`,
                }),
                [i.line.delay, i.line.duration, e],
              );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(Jt, {
                  size: t,
                  lineRef: a,
                  disabled: n,
                  isComplete: r,
                  baseStyles: m,
                }),
                u >= 0 &&
                  o().createElement(su, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    freezed: i.freezed,
                    from: u,
                    size: t,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          iu = "ProgressBarDeltaGrow_base_7e",
          lu = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          cu = "ProgressBarDeltaGrow_glow_68",
          mu = (e) => (e ? { left: 0 } : { right: 0 }),
          du = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          Eu = (e) => ({ transitionDuration: `${e}ms` }),
          _u = (0, s.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: u,
              from: a,
              size: n,
              to: r,
              onEndAnimation: i,
              onChangeAnimationState: c,
              className: m,
            }) => {
              const d = r < a,
                E = (0, s.useState)(uu.Idle),
                _ = E[0],
                g = E[1],
                A = _ === uu.End,
                p = _ === uu.Idle,
                D = _ === uu.Grow,
                h = _ === uu.Shrink,
                F = (0, s.useCallback)(
                  (e) => {
                    (g(e), c && c(e));
                  },
                  [c],
                ),
                C = (0, s.useCallback)(
                  (e, t) =>
                    tu(() => {
                      F(e);
                    }, t),
                  [F],
                );
              (0, s.useEffect)(() => {
                if (!u)
                  return p
                    ? C(uu.Grow, t)
                    : D
                      ? C(uu.Shrink, e)
                      : h
                        ? C(uu.End, e)
                        : void (A && i && i());
              }, [C, u, A, D, p, h, i, t, e]);
              const B = (0, s.useMemo)(
                  () => Object.assign({ width: "100%" }, Eu(e), mu(d)),
                  [d, e],
                ),
                v = (0, s.useMemo)(() => Object.assign({ width: "0%" }, Eu(e), mu(d)), [d, e]),
                b = (0, s.useMemo)(
                  () => Object.assign({ width: "0%" }, du(d, a), Eu(e)),
                  [a, d, e],
                ),
                f = (0, s.useMemo)(
                  () => Object.assign({ width: `${Math.abs(r - a)}%` }, du(d, a), Eu(e)),
                  [a, d, r, e],
                );
              if (A) return null;
              const w = l()(iu, m, d && 0 === r && lu);
              return o().createElement(
                "div",
                { style: p ? b : f, className: w },
                o().createElement(
                  "div",
                  { style: h ? v : B, className: cu },
                  o().createElement(Kt, { size: n }),
                ),
              );
            },
          ),
          gu = (0, s.memo)(
            ({
              to: e,
              size: t,
              from: u,
              lineRef: a,
              disabled: n,
              isComplete: r,
              animationSettings: i,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const m = e < u,
                d = (0, s.useState)(!1),
                E = d[0],
                _ = d[1],
                g = (0, s.useCallback)(
                  (e) => {
                    (e === uu.Shrink && _(!0), c && c(e));
                  },
                  [c],
                ),
                A = (0, s.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
                p = (0, s.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${i.line.duration}ms` }),
                  [i.line.duration, e],
                );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(Jt, {
                  size: t,
                  lineRef: a,
                  disabled: n,
                  isComplete: r,
                  withoutBounce: m && 0 === e,
                  baseStyles: E ? p : A,
                }),
                u >= 0 &&
                  o().createElement(_u, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    onChangeAnimationState: g,
                    freezed: i.freezed,
                    onEndAnimation: l,
                    from: u,
                    size: t,
                    to: e,
                    className: i.delta.className,
                  }),
              );
            },
          ),
          Au = ["onComplete", "onEndAnimation"];
        function pu() {
          return (
            (pu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            pu.apply(this, arguments)
          );
        }
        const Du = (0, s.memo)((e) => {
            let t = e.onComplete,
              u = e.onEndAnimation,
              a = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, Au);
            const n = (0, s.useState)(!1),
              r = n[0],
              i = n[1],
              l = (0, s.useCallback)(() => {
                const e = 100 === a.to;
                (e !== r && i(e), e && t && t(), u && u());
              }, [r, t, u, a.to]);
            switch (a.animationSettings.type) {
              case qt.Simple:
                return o().createElement(ou, pu({}, a, { onEndAnimation: l, isComplete: r }));
              case qt.Growing:
                return o().createElement(gu, pu({}, a, { onEndAnimation: l, isComplete: r }));
              default:
                return null;
            }
          }),
          hu = ["onEndAnimation"];
        function Fu() {
          return (
            (Fu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Fu.apply(this, arguments)
          );
        }
        const Cu = (0, s.memo)((e) => {
          let t = e.onEndAnimation,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, hu);
          const a = (0, s.useRef)({}),
            n = (0, s.useCallback)(() => {
              ((a.current.from = void 0), t && t());
            }, [t]),
            r = "number" == typeof a.current.from ? a.current.from : u.from;
          return (
            (a.current.from = r),
            o().createElement(Du, Fu({}, u, { onEndAnimation: n, key: `${r}-${u.to}`, from: r }))
          );
        });
        function Bu() {
          return (
            (Bu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Bu.apply(this, arguments)
          );
        }
        const vu = (0, s.memo)(
            ({
              size: e,
              value: t,
              lineRef: u,
              disabled: a,
              deltaFrom: n,
              animationSettings: r,
              onEndAnimation: s,
              onChangeAnimationState: i,
              onComplete: l,
            }) => {
              if (n === t)
                return o().createElement(eu, {
                  key: `${n}-${t}`,
                  size: e,
                  value: t,
                  lineRef: u,
                  disabled: a,
                  onComplete: l,
                });
              const c = {
                from: n,
                to: t,
                size: e,
                lineRef: u,
                disabled: a,
                animationSettings: r,
                onComplete: l,
                onEndAnimation: s,
                onChangeAnimationState: i,
              };
              return r.withStack
                ? o().createElement(Cu, c)
                : o().createElement(Du, Bu({ key: `${n}-${t}` }, c));
            },
          ),
          bu = (e) => ({
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
          fu = (e, t, u) => {
            if ("number" == typeof u) {
              return (zt(0, t, u) / t) * 100;
            }
            return e;
          },
          wu = {
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
          Su = {
            freezed: !1,
            withStack: !1,
            type: qt.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          xu = (0, s.memo)(
            ({
              maxValue: e = 100,
              theme: t = wu,
              size: u = Xt.Default,
              animationSettings: a = Su,
              disabled: n = !1,
              withoutBackground: r = !1,
              progressBarBackgroundClassMix: i,
              value: c,
              deltaFrom: m,
              lineRef: d,
              onChangeAnimationState: E,
              onEndAnimation: _,
              onComplete: g,
            }) => {
              const A = ((e, t, u) =>
                (0, s.useMemo)(() => {
                  const a = (zt(0, t, e) / t) * 100;
                  return { value: a, deltaFrom: fu(a, t, u) };
                }, [u, t, e]))(c, e, m);
              return o().createElement(
                "div",
                { className: l()(jt.base, jt[`base__${u}`]), style: bu(t) },
                !r && o().createElement(Zt, { size: u, classMix: i }),
                o().createElement(vu, {
                  size: u,
                  lineRef: d,
                  disabled: n,
                  value: A.value,
                  deltaFrom: A.deltaFrom,
                  animationSettings: a,
                  onEndAnimation: _,
                  onChangeAnimationState: E,
                  onComplete: g,
                }),
              );
            },
          ),
          Ru = "OptimizedProgressBar_base_1f",
          Pu = "OptimizedProgressBar_wrapper_ab",
          Lu = "OptimizedProgressBar_background_ce",
          yu = ["api", "value", "maxValue", "theme"];
        function Tu() {
          return (
            (Tu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            Tu.apply(this, arguments)
          );
        }
        const Nu = (e, t) => ("number" == typeof t ? t : e.offsetLeft),
          Mu = (e) => {
            let t = e.api,
              u = e.value,
              a = e.maxValue,
              n = void 0 === a ? 100 : a,
              r = e.theme,
              i = void 0 === r ? wu : r,
              c = (function (e, t) {
                if (null == e) return {};
                var u,
                  a,
                  n = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
                return n;
              })(e, yu);
            const m = (0, s.useRef)(null),
              d = (0, s.useRef)(null),
              E = (0, s.useRef)(null),
              _ = zt(0, u, n) / n,
              g = (0, s.useCallback)(
                (e) => {
                  (E.current &&
                    m.current &&
                    (({ horizontalScrollPosition: e, leftOffset: t }, u, a) => {
                      const n = u.offsetWidth - a.offsetWidth,
                        r = e - Nu(u, t),
                        s = zt(0, n, r);
                      a.style.left = `${s}px`;
                    })(e, m.current, E.current),
                    d.current &&
                      m.current &&
                      ((
                        { horizontalScrollPosition: e, leftOffset: t },
                        u,
                        { container: a, line: n },
                      ) => {
                        const r = Math.max(0, Math.floor(a.offsetWidth * u) - 8e3),
                          s = e - Nu(a, t),
                          o = zt(0, r, s);
                        n.style.left = `${o}px`;
                      })(e, _, { line: d.current, container: m.current }));
                },
                [_],
              ),
              A = (0, s.useMemo)(() => bu(i), [i]);
            return (
              (t.current.update = g),
              o().createElement(
                "div",
                { className: Ru, ref: m },
                o().createElement(
                  "div",
                  { className: Pu },
                  o().createElement(
                    "div",
                    { style: A, className: l()(Lu, c.progressBarBackgroundClassMix), ref: E },
                    o().createElement(Zt, {
                      size: c.size,
                      classMix: c.progressBarBackgroundClassMix,
                    }),
                  ),
                  o().createElement(
                    xu,
                    Tu({}, c, {
                      lineRef: d,
                      value: u,
                      theme: i,
                      maxValue: n,
                      withoutBackground: !0,
                    }),
                  ),
                ),
              )
            );
          },
          ku = Object.assign({}, Su, {
            withStack: !0,
            type: qt.Growing,
            delta: { duration: 400, delay: 300 },
            line: { duration: 400, delay: 300 },
          }),
          Ou = "LevelsRewards_base_34",
          Iu = "LevelsRewards_header_46",
          Hu = "LevelsRewards_base__disabled_87",
          Uu = "LevelsRewards_rewards_c6",
          $u = "LevelsRewards_scrollArea_22",
          Wu = "LevelsRewards_column_4f",
          Gu = "LevelsRewards_column__completed_88",
          Vu = "LevelsRewards_column__active_9b",
          zu = "LevelsRewards_progressBarContainer_b4",
          ju = "RewardsColumn_base_79",
          Xu = "RewardsColumn_particlesLine_af",
          qu = "RewardsColumn_particlesLine__left_21",
          Zu = "RewardsColumn_particlesLine__active_98",
          Yu = "RewardsColumn_particlesLine__disabled_27",
          Ku = "RewardsColumn_pointsContainer_5b",
          Qu = "RewardsColumn_achievedWrapper_e6",
          Ju = "RewardsColumn_achieved_c3",
          ea = "RewardsColumn_rewards_0a",
          ta = "RewardsColumn_splittedValueText_c6",
          ua = "RewardsColumn_splittedValueText__colored_a8",
          aa = "RewardsColumn_pointsIcon_96";
        var na = u(2862),
          ra = u(729);
        const sa = ["children"];
        function oa() {
          return (
            (oa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            oa.apply(this, arguments)
          );
        }
        const ia = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                a,
                n = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((u = r[a]), t.indexOf(u) >= 0 || (n[u] = e[u]));
              return n;
            })(e, sa);
          return o().createElement(
            pt,
            oa(
              {
                contentId:
                  R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                    "resId",
                  ),
                ignoreShowDelay: !0,
              },
              u,
            ),
            t,
          );
        };
        function la() {
          return (
            (la =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var a in u) Object.prototype.hasOwnProperty.call(u, a) && (e[a] = u[a]);
                }
                return e;
              }),
            la.apply(this, arguments)
          );
        }
        const ca = ({ children: e, tooltipArgs: t, className: u }) => {
            if (!t) return e;
            const a = o().createElement("div", { className: u }, e);
            if (t.header || t.body) return o().createElement(Ct, t, a);
            const n = t.contentId,
              r = t.args,
              s = null == r ? void 0 : r.contentId;
            return n || s
              ? o().createElement(pt, la({}, t, { contentId: n || s }), a)
              : o().createElement(ia, t, a);
          },
          ma = {
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
          da = ({
            name: e,
            image: t,
            isPeriodic: u = !1,
            size: a = na.h2.Big,
            special: n,
            value: r,
            valueType: s,
            style: i,
            className: c,
            classNames: m,
            tooltipArgs: d,
            periodicIconTooltipArgs: E,
          }) => {
            const _ = (0, ra.L_)(n),
              g = (0, ra.i2)(n),
              A = (0, ra.m9)(r, s);
            return o().createElement(
              "div",
              { className: l()(ma.base, ma[`base__${a}`], c), style: i },
              o().createElement(
                ca,
                { tooltipArgs: d, className: ma.tooltipWrapper },
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement(
                    "div",
                    { className: l()(ma.image, null == m ? void 0 : m.image) },
                    _ &&
                      o().createElement("div", {
                        className: l()(ma.highlight, null == m ? void 0 : m.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${_}_highlight)`,
                        },
                      }),
                    t &&
                      o().createElement("div", {
                        className: l()(ma.icon, null == m ? void 0 : m.rewardIcon),
                        style: { backgroundImage: `url(${t})` },
                      }),
                    g &&
                      o().createElement("div", {
                        className: l()(ma.overlay, null == m ? void 0 : m.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${g}_overlay)`,
                        },
                      }),
                  ),
                  A &&
                    o().createElement(
                      "div",
                      {
                        className: l()(
                          ma.info,
                          ma[`info__${e}`],
                          s === na.$h.MULTI && ma.info__multi,
                          null == m ? void 0 : m.info,
                        ),
                      },
                      A,
                    ),
                ),
              ),
              u &&
                o().createElement(
                  ca,
                  { tooltipArgs: E },
                  o().createElement("div", {
                    className: l()(ma.timer, null == m ? void 0 : m.periodicIcon),
                  }),
                ),
            );
          };
        var Ea = u(5190);
        const _a = "RewardLabel_base_b8",
          ga = "RewardLabel_base__rewardSelect_ff",
          Aa = "RewardLabel_base__label_b4",
          pa = "RewardLabel_base__disabled_c0",
          Da = "RewardLabel_button_00",
          ha = R.strings.paragons.allRewards,
          Fa = (0, s.memo)(
            ({
              reward: e,
              isLevelAchieved: t,
              currentLevel: u,
              isSelectableVehicle: a,
              isShortVehicleName: n,
              isDisabledState: r,
              onOpenOverlay: i,
            }) => {
              const c = l()(_a, a ? ga : Aa, r && !a && pa),
                m = (0, s.useCallback)(
                  (e, t) => () => {
                    i(e, t);
                  },
                  [i],
                );
              return o().createElement(
                "div",
                { className: c },
                a
                  ? o().createElement(
                      re,
                      {
                        size: ae.small,
                        type: t ? ue.main : ue.primary,
                        mixClass: Da,
                        onClick: m(u, e.value),
                      },
                      o().createElement(Et.ZP, { text: t ? ha.button.select() : ha.button.list() }),
                    )
                  : o().createElement(Ea.M2, {
                      isElite: e.isElite,
                      vehicleName: e.label,
                      vehicleType: e.type,
                      vehicleLvl: e.vehicleLvl,
                      size: Ea.uA.ExtraSmall,
                      isShortVehicleName: n,
                      type: Ea.YH.Cream,
                    }),
              );
            },
          ),
          Ca = "RewardsList_base_34",
          Ba = "RewardsList_reward_8c",
          va = "RewardsList_reward__last_ac",
          ba = "RewardsList_reward__disabled_91",
          fa = "RewardsList_rewardIcon_a0",
          wa = "RewardsList_rewardLabelContainer_8e",
          Sa = "RewardsList_rewardLabelContainer__rewardSelect_e6",
          xa = "RewardsList_rewardLabelContainer__label_18",
          Ra = "RewardsList_info_5a",
          Pa = "RewardsList_preview_88",
          La = (e) => {
            switch (e) {
              case d.cJ.ExtraSmall:
              case d.cJ.Small:
                return na.h2.Small;
              case d.cJ.Medium:
              case d.cJ.Large:
                return na.h2.Big;
              case d.cJ.ExtraLarge:
                return na.h2.S180x135;
              default:
                return na.h2.Big;
            }
          },
          ya = (0, s.memo)(
            ({
              rewardsData: e,
              isLevelAchieved: t,
              currentLevel: u,
              className: a,
              classNames: n,
              isDisabledState: r,
              onOpenOverlay: s,
              onPreviewVehicle: i,
            }) => {
              const c = (0, d.GS)().mediaSize,
                m = l()(Ca, a),
                E = l()(Ba, null == n ? void 0 : n.rewardItem),
                _ = e.length;
              return o().createElement(
                "div",
                { className: m },
                e.map((e, a) => {
                  const n = e.name === na.E4.Vehicles,
                    m = e.name === na.E4.VehicleSelect,
                    g = n && c < d.cJ.ExtraLarge,
                    A = (t && !m) || r,
                    p = m || (e.name === na.E4.Vehicles && c > d.cJ.Large),
                    D = a === _ - 1,
                    h = c < d.cJ.ExtraLarge,
                    F = c < d.cJ.Medium ? Ht.SMALL : Ht.NORMAL;
                  return o().createElement(
                    ca,
                    { tooltipArgs: Object.assign({}, e.tooltipArgs), key: `${e.name}_${a}` },
                    o().createElement(
                      "div",
                      { className: l()(E, A && ba, D && va) },
                      o().createElement(da, {
                        size: La(c),
                        name: e.name,
                        image: e.image(La(c)),
                        value: g ? e.label : void 0,
                        valueType: (0, ra.p3)(e.name),
                        className: fa,
                        classNames: { info: Ra },
                      }),
                      n &&
                        o().createElement(
                          "div",
                          { className: Pa },
                          o().createElement(Gt, {
                            onClick: i(e.vehicleCD),
                            type: It.PREVIEW,
                            size: F,
                          }),
                        ),
                      p &&
                        o().createElement(
                          "div",
                          { className: l()(wa, m ? Sa : xa) },
                          o().createElement(Fa, {
                            reward: e,
                            isLevelAchieved: t,
                            currentLevel: u,
                            isSelectableVehicle: m,
                            onOpenOverlay: s,
                            isShortVehicleName: h,
                            isDisabledState: r,
                          }),
                        ),
                    ),
                  );
                }),
              );
            },
          ),
          Ta = R.strings.paragons.navigation.progression.points,
          Na = (0, s.memo)(
            ({
              isCompleted: e,
              rewards: t,
              currentLevel: u,
              hasLeftBorder: a,
              hasActiveBorder: n,
              isLastLevelActive: r,
              maxLevelPointsCount: s,
              currentLevelPointsCount: i,
              isCurrentLevel: c,
              isDisabledState: m,
              isActiveState: d,
              onOpenOverlay: E,
              onPreviewVehicle: _,
            }) =>
              o().createElement(
                "div",
                { className: ju },
                o().createElement("div", { className: l()(Xu, qu, n && Zu, (m || !d) && Yu) }),
                a && o().createElement("div", { className: l()(Xu, r && Zu) }),
                e
                  ? o().createElement(
                      "div",
                      { className: Qu },
                      o().createElement("div", { className: Ju }),
                    )
                  : o().createElement(
                      pt,
                      {
                        contentId: R.views.lobby.paragons.tooltips.RewardsHeaderTooltip("resId"),
                        args: { isParagonsPoints: !0 },
                      },
                      o().createElement(
                        "div",
                        { className: Ku },
                        o().createElement(Et.ZP, {
                          text: c && d ? Ta.splittedValue() : String(s),
                          format: {
                            binding: {
                              currentValue: o().createElement(Et.ZP, {
                                text: String(i),
                                className: ua,
                              }),
                              maxValue: o().createElement(Et.ZP, { text: String(s) }),
                            },
                          },
                          className: ta,
                        }),
                        o().createElement("div", { className: aa }),
                      ),
                    ),
                o().createElement(
                  "div",
                  { className: ea },
                  o().createElement(ya, {
                    currentLevel: u,
                    onOpenOverlay: E,
                    rewardsData: t,
                    isLevelAchieved: e,
                    isDisabledState: m || !d,
                    onPreviewVehicle: _,
                  }),
                ),
              ),
          ),
          Ma = "RewardsHeader_base_5e",
          ka = "RewardsHeader_level_b6",
          Oa = "RewardsHeader_level__completed_af",
          Ia = "RewardsHeader_level__current_a3",
          Ha = "RewardsHeader_numeral_3a",
          Ua = "RewardsHeader_numeral__disabled_1b",
          $a = "RewardsHeader_particlesLine_36",
          Wa = "RewardsHeader_particlesLine__left_b1",
          Ga = "RewardsHeader_particlesLine__active_45",
          Va = (0, s.memo)(
            ({
              isCompleted: e,
              currentLevel: t,
              stageLevel: u,
              hasLeftBorder: a,
              isActiveBorder: n,
              isActiveLastBorder: r,
              hasActiveGlow: s,
              hasSelectableRewards: i,
            }) => {
              const c = l()(Ha, !e && t < u && Ua),
                m = t === u && !e && s,
                d = l()(ka, e && Oa, m && Ia);
              return o().createElement(
                pt,
                {
                  contentId: R.views.lobby.paragons.tooltips.RewardsHeaderTooltip("resId"),
                  args: { isCompleted: e, isCurrentLevel: m, hasSelectableRewards: i },
                },
                o().createElement(
                  "div",
                  { className: Ma },
                  o().createElement("div", { className: l()($a, Wa, n && Ga) }),
                  a && o().createElement("div", { className: l()($a, r && Ga) }),
                  o().createElement(
                    "div",
                    { className: d },
                    o().createElement(Et.ZP, { text: String(u), className: c }),
                  ),
                ),
              );
            },
          ),
          za = (0, s.memo)(
            ({
              currentLevel: e,
              levels: t,
              paragonPoints: u,
              maxPointsCount: a,
              isDisabledState: n,
              hasProgress: r,
              isActiveState: i,
              isProgressionActive: c,
              onOpenOverlay: m,
              onPreviewVehicle: d,
            }) => {
              const E = (0, s.useRef)({ update: () => {} }),
                _ = t.length,
                g = i || r;
              return o().createElement(
                "div",
                { className: l()(Ou, (n || !c) && Hu) },
                o().createElement(
                  "div",
                  { className: $u },
                  o().createElement(
                    "div",
                    { className: zu },
                    o().createElement(Mu, {
                      animationSettings: ku,
                      value: (0, Ke.ZI)(u, e, t),
                      maxValue: a,
                      api: E,
                    }),
                  ),
                  o().createElement(
                    "div",
                    {
                      className: Uu,
                      onMouseEnter: () => {
                        ee.playHighlight();
                      },
                      onMouseDown: () => {
                        ee.playClick();
                      },
                    },
                    t.map((a, r) => {
                      var s;
                      const E = r === e - 1 && !a.isCompleted && g,
                        A = r === _ - 1,
                        p = (r === e && !t[r - 1].isCompleted && g) || E,
                        D = (null == (s = t[r - 1]) ? void 0 : s.maxPoints) || 0,
                        h = a.maxPoints - D,
                        F = u - D,
                        C = e === _ && !a.isCompleted && g;
                      return o().createElement(
                        "div",
                        { key: `level_${r}`, className: l()(Wu, a.isCompleted && Gu, E && Vu) },
                        o().createElement(
                          "div",
                          { className: Iu },
                          o().createElement(Va, {
                            currentLevel: e,
                            stageLevel: a.number,
                            isCompleted: a.isCompleted,
                            hasLeftBorder: A,
                            isActiveBorder: p,
                            hasActiveGlow: g,
                            isActiveLastBorder: C,
                            hasSelectableRewards: a.hasSelectableRewards,
                          }),
                        ),
                        o().createElement(Na, {
                          currentLevel: r + 1,
                          isCompleted: a.isCompleted,
                          rewards: a.rewards,
                          onOpenOverlay: m,
                          hasLeftBorder: A,
                          hasActiveBorder: p,
                          isCurrentLevel: r === e - 1,
                          maxLevelPointsCount: h,
                          currentLevelPointsCount: F,
                          isDisabledState: n,
                          isActiveState: i || c,
                          onPreviewVehicle: d,
                          isLastLevelActive: C,
                        }),
                      );
                    }),
                  ),
                ),
              );
            },
          ),
          ja = {
            base: "ProgressionView_base_a0",
            fadeIn: "ProgressionView_fadeIn_02",
            background: "ProgressionView_background_ab",
            base__disabled: "ProgressionView_base__disabled_c7",
            base__paused: "ProgressionView_base__paused_6c",
            header: "ProgressionView_header_6c",
            dateTextProgression: "ProgressionView_dateTextProgression_62",
            warning: "ProgressionView_warning_0b",
            warningText: "ProgressionView_warningText_f6",
            content: "ProgressionView_content_6d",
            progressionContainer: "ProgressionView_progressionContainer_81",
            disabledPattern: "ProgressionView_disabledPattern_4a",
            previewPanel: "ProgressionView_previewPanel_e1",
            activateButton: "ProgressionView_activateButton_64",
            pausedButton: "ProgressionView_pausedButton_13",
          },
          Xa = R.strings.paragons,
          qa = Xa.navigation.progression,
          Za = (0, s.memo)(
            ({
              currentSeason: e,
              paragonPoints: t,
              necessaryVehicleCount: u,
              vehicleCount: a,
              hasSeasonActivateButton: n,
              selectedSeason: r,
              onPreviewVehicle: i,
              onSelectVehicleReward: c,
              onSeasonActivate: m,
            }) => {
              const d = e.levels[e.levels.length - 1].maxPoints,
                E = e.chapterStatus.status === Ge.DISABLED,
                _ = e.chapterStatus.status === Ge.PAUSED,
                g = e.chapterStatus.status === Ge.ACTIVE,
                A = e.chapterStatus.status === Ge.DEFAULT,
                p = E || _,
                D = Boolean(e.points),
                h = E || (e.chapterStatus.status === Ge.FINISHED && e.isAllRewardsClaimed),
                F = (0, s.useCallback)(
                  (e) => () => {
                    i(e, r);
                  },
                  [i, r],
                ),
                C = (0, s.useCallback)(
                  (e) => () => {
                    m(e);
                  },
                  [m],
                );
              return o().createElement(
                "div",
                { className: l()(ja.base, ja[`base__${e.chapterStatus.status}`]) },
                o().createElement("div", {
                  className: ja.background,
                  style: {
                    backgroundImage: `url('R.images.gui.maps.icons.paragons.backgrounds.background_season_${e.id}')`,
                  },
                }),
                o().createElement(
                  "div",
                  { className: ja.header },
                  o().createElement(Ze.h, {
                    stage: Xa.chapterName.shortUpperCase.$dyn(`id_${e.id}`),
                    topTitle: Xa.project.name(),
                    mainTitle: qa.title.level(),
                  }),
                  n &&
                    o().createElement(
                      re,
                      {
                        size: ae.medium,
                        type: ue.primary,
                        mixClass: ja.activateButton,
                        onClick: C(e.id),
                      },
                      o().createElement(Et.ZP, {
                        text: Xa.seasonsProgression.stageText.selectStage(),
                      }),
                    ),
                  (0, Ke.P8)(e.timeStamp) &&
                    !h &&
                    o().createElement(Vt.N, {
                      mixClass: ja.dateTextProgression,
                      text: Xa.seasonsProgression.timeLeft.timeText(),
                      timeStamp: e.timeStamp,
                    }),
                ),
                o().createElement(
                  "div",
                  { className: ja.content },
                  p
                    ? o().createElement(
                        "div",
                        { className: ja.warning },
                        o().createElement(Et.ZP, {
                          text: qa.warning.$dyn(e.chapterStatus.status),
                          className: ja.warningText,
                          format: { binding: { necessaryVehicleCount: u, vehicleCount: a } },
                        }),
                        _ &&
                          o().createElement(
                            re,
                            {
                              size: ae.medium,
                              type: ue.primary,
                              mixClass: ja.pausedButton,
                              onClick: C(e.id),
                            },
                            o().createElement(Et.ZP, {
                              text: Xa.seasonsProgression.stageText.selectStage(),
                            }),
                          ),
                      )
                    : o().createElement(
                        "div",
                        { className: ja.previewPanel },
                        e.finalVehicleCDs.map((e) =>
                          o().createElement(
                            "div",
                            { className: ja.preview, key: e },
                            o().createElement(
                              Ct,
                              { body: qa.button.preview() },
                              o().createElement(Gt, {
                                onClick: F(e),
                                type: It.PREVIEW,
                                size: Ht.NORMAL,
                              }),
                            ),
                          ),
                        ),
                      ),
                  o().createElement(
                    "div",
                    { className: ja.progressionContainer },
                    E && o().createElement("div", { className: ja.disabledPattern }),
                    o().createElement(za, {
                      levels: e.levels,
                      currentLevel: e.chapterLevel,
                      onOpenOverlay: c,
                      paragonPoints: t,
                      maxPointsCount: d,
                      isDisabledState: E || _,
                      hasProgress: D,
                      isActiveState: g,
                      onPreviewVehicle: F,
                      isProgressionActive: g || A,
                    }),
                  ),
                ),
              );
            },
          ),
          Ya = [];
        function Ka(e) {
          const t = (0, s.useRef)(e);
          return (
            (0, s.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, s.useCallback)((...e) => (0, t.current)(...e), Ya)
          );
        }
        function Qa(e, t, u = []) {
          const a = (0, s.useRef)(0),
            n = (0, s.useCallback)(() => window.clearInterval(a.current), u || []);
          (0, s.useEffect)(() => n, [n]);
          const r = (null != u ? u : []).concat([t]);
          return [
            (0, s.useCallback)((u) => {
              ((a.current = window.setInterval(() => e(u, !0), t)), e(u, !1));
            }, r),
            n,
          ];
        }
        function Ja(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return en(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return en(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var a = 0;
            return function () {
              return a >= e.length ? { done: !0 } : { done: !1, value: e[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function en(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, a = new Array(t); u < t; u++) a[u] = e[u];
          return a;
        }
        function tn(e, t, u) {
          const a = (0, s.useMemo)(
            () =>
              (function (e, t, u, a) {
                let n,
                  r = !1,
                  s = 0;
                function o() {
                  n && clearTimeout(n);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - s;
                  function m() {
                    ((s = Date.now()), u.apply(l, i));
                  }
                  r ||
                    (a && !n && m(),
                    o(),
                    void 0 === a && c > e
                      ? m()
                      : !0 !== t &&
                        (n = setTimeout(
                          a
                            ? function () {
                                n = void 0;
                              }
                            : m,
                          void 0 === a ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof t && ((a = u), (u = t), (t = void 0)),
                  (i.cancel = function () {
                    (o(), (r = !0));
                  }),
                  i
                );
              })(u, e),
            t,
          );
          return ((0, s.useEffect)(() => a.cancel, [a]), a);
        }
        var un = u(7030);
        let an;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(an || (an = {}));
        const nn = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          rn = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: u,
            getDirection: a,
            getWrapperSize: n,
            triggerMouseMoveOnUpdate: r = !1,
          }) => {
            const o = (e, u) => {
              const a = t(e),
                n = a[0],
                r = a[1];
              return zt(n, r, u);
            };
            return (i = {}) => {
              const l = i.settings,
                c = void 0 === l ? nn : l,
                m = (0, s.useRef)(null),
                d = (0, s.useRef)(null),
                E = (() => {
                  const e = (0, s.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    u = (e, u) => {
                      t(e).set(u, u);
                    },
                    a = (e, u) => {
                      t(e).delete(u);
                    },
                    n = (e, ...u) => {
                      for (var a, n = Ja(t(e).values()); !(a = n()).done;) (0, a.value)(...u);
                    };
                  return (0, s.useMemo)(() => ({ on: u, off: a, trigger: n }), []);
                })(),
                _ = tn(
                  () => {
                    w.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                g = (0, un.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = m.current;
                    t && (u(t, e), E.trigger("change", e), r && _());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                A = g[0],
                p = g[1],
                D = (0, s.useCallback)(
                  (e, t, u) => {
                    var a;
                    const n = A.scrollPosition.get(),
                      r = (null != (a = A.scrollPosition.goal) ? a : 0) - n;
                    return o(e, t * u + r + n);
                  },
                  [A.scrollPosition],
                ),
                h = (0, s.useCallback)(
                  (e, { immediate: t = !1, reset: u = !0 } = {}) => {
                    const a = m.current;
                    a &&
                      p.start({
                        scrollPosition: o(a, e),
                        immediate: t,
                        reset: u,
                        config: c.animationConfig,
                        from: { scrollPosition: o(a, A.scrollPosition.get()) },
                      });
                  },
                  [p, c.animationConfig, A.scrollPosition],
                ),
                F = (0, s.useCallback)(
                  (e) => {
                    const t = m.current,
                      u = d.current;
                    if (!t || !u) return;
                    const a = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return n(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(u, c.step),
                      r = D(t, e, a);
                    h(r);
                  },
                  [h, D, c.step],
                ),
                C = (0, s.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && F(a(e)),
                      m.current && E.trigger("mouseWheel", e, A.scrollPosition, t(m.current)));
                  },
                  [A.scrollPosition, F, E],
                ),
                B = Re(
                  () =>
                    xe(() => {
                      const e = m.current;
                      e &&
                        (h(o(e, A.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [h, A.scrollPosition.goal],
                ),
                v = Ka(() => {
                  const e = m.current;
                  if (!e) return;
                  const t = o(e, A.scrollPosition.goal);
                  (t !== A.scrollPosition.goal && h(t, { immediate: !0 }),
                    E.trigger("recalculateContent"));
                });
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", B),
                  () => {
                    window.removeEventListener("resize", B);
                  }
                ),
                [B],
              );
              const b = (0, s.useCallback)((e) => E.trigger("isThumbDraggingChanged", e), [E]);
              return (0, s.useMemo)(
                () => ({
                  getWrapperSize: () => (d.current ? n(d.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? t(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: c.step.clampedArrowStepTimeout,
                  clampPosition: o,
                  handleMouseWheel: C,
                  applyScroll: h,
                  applyStepTo: F,
                  contentRef: m,
                  wrapperRef: d,
                  scrollPosition: p,
                  animationScroll: A,
                  recalculateContent: v,
                  handleIsThumbDragging: b,
                  events: { on: E.on, off: E.off },
                }),
                [A.scrollPosition, h, F, b, E.off, E.on, v, C, p, c.step.clampedArrowStepTimeout],
              );
            };
          },
          sn = rn({
            getBounds: (e) => {
              var t, u;
              return [
                0,
                e.offsetWidth -
                  (null != (t = null == (u = e.parentElement) ? void 0 : u.offsetWidth) ? t : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, t) => {
              e.style.transform = `translateX(-${t.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? an.Next : an.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          on = "HorizontalBar_base_49",
          ln = "HorizontalBar_base__nonActive_82",
          cn = "HorizontalBar_leftButton_5f",
          mn = "HorizontalBar_rightButton_03",
          dn = "HorizontalBar_track_0d",
          En = "HorizontalBar_thumb_fd",
          _n = "HorizontalBar_rail_32",
          gn = "disable",
          An = { pending: !1, offset: 0 },
          pn = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          Dn = () => {},
          hn = (e, t) => Math.max(20, e.offsetWidth * t),
          Fn = (0, s.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = pn, onDrag: a = Dn }) => {
              const n = (0, s.useRef)(null),
                r = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                d = e.stepTimeout || 100,
                E = (0, s.useState)(An),
                _ = E[0],
                g = E[1],
                A = (0, s.useCallback)(
                  (e) => {
                    (g(e),
                      m.current &&
                        a({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [a],
                ),
                p = () => {
                  const t = c.current,
                    u = m.current,
                    a = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(a && t && u && n)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, a / n),
                    l = zt(0, 1, s / (n - a)),
                    d = (t.offsetWidth - hn(t, o)) * l;
                  ((u.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (r.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (r.current.classList.add(gn), void i.current.classList.remove(gn));
                        if (
                          ((t = c.current),
                          (u = m.current),
                          e - (t.offsetWidth - u.offsetWidth) >= -0.5)
                        )
                          return (r.current.classList.remove(gn), void i.current.classList.add(gn));
                        var t, u;
                        (r.current.classList.remove(gn), i.current.classList.remove(gn));
                      }
                    })(d));
                },
                D = Ka(() => {
                  ((() => {
                    const t = m.current,
                      u = c.current,
                      a = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && a && u)) return;
                    const s = Math.min(1, a / r);
                    ((t.style.width = `${hn(u, s)}px`),
                      (t.style.display = "flex"),
                      n.current &&
                        (1 === s ? n.current.classList.add(ln) : n.current.classList.remove(ln)));
                  })(),
                    p());
                });
              ((0, s.useEffect)(() => xe(D)),
                (0, s.useEffect)(
                  () =>
                    xe(() => {
                      const t = () => {
                        p();
                      };
                      let u = Dn;
                      const a = () => {
                        (u(), (u = xe(D)));
                      };
                      return (
                        e.events.on("recalculateContent", D),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", a),
                        () => {
                          (u(),
                            e.events.off("recalculateContent", D),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", a));
                        }
                      );
                    }),
                  [e],
                ),
                (0, s.useEffect)(() => {
                  if (!_.pending) return;
                  const t = (t) => {
                      var u;
                      const n = e.contentRef.current;
                      if (!n) return;
                      const r = c.current,
                        s = m.current;
                      if (!n || !r || !s) return;
                      const o = t.screenX - _.offset - r.getBoundingClientRect().x,
                        i = (o / r.offsetWidth) * (null != (u = e.getContainerSize()) ? u : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(n, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        a({ type: "dragging", thumb: s, thumbOffset: o, contentOffset: i }));
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t), A(An));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, _.offset, _.pending, a, A]));
              const h = Qa((t) => e.applyStepTo(t), d, [e]),
                F = h[0],
                C = h[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", C, !0),
                  () => document.removeEventListener("mouseup", C, !0)
                ),
                [C],
              );
              const B = (e) => {
                e.target.classList.contains(gn) || J("highlight");
              };
              return o().createElement(
                "div",
                { className: l()(on, t.base), ref: n, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: l()(cn, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(gn) || 0 !== e.button || (J("play"), F(an.Next));
                  },
                  onMouseUp: C,
                  ref: r,
                  onMouseEnter: B,
                }),
                o().createElement(
                  "div",
                  {
                    className: l()(dn, t.track),
                    onMouseDown: (t) => {
                      const a = m.current;
                      if (a && 0 === t.button)
                        if ((J("play"), t.target === a))
                          A({ pending: !0, offset: t.screenX - a.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const a = m.current,
                              n = e.contentRef.current;
                            if (!a || !n) return;
                            const r = u(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * t);
                          })(t.screenX > a.getBoundingClientRect().x ? an.Prev : an.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: B,
                  },
                  o().createElement("div", { ref: m, className: l()(En, t.thumb) }),
                  o().createElement("div", { className: l()(_n, t.rail) }),
                ),
                o().createElement("div", {
                  className: l()(mn, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(gn) || 0 !== e.button || (J("play"), F(an.Prev));
                  },
                  onMouseUp: C,
                  ref: i,
                  onMouseEnter: B,
                }),
              );
            },
          ),
          Cn = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Bn = ({
            children: e,
            api: t,
            className: u,
            barClassNames: a,
            areaClassName: n,
            classNames: r,
            scrollClassName: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = a || {};
                return Object.assign({}, e, { base: l()(Cn.base, e.base) });
              }, [a]),
              E = (0, s.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: l()(Cn.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Cn.defaultScrollArea, n) },
                o().createElement(vn, { className: i, api: E, classNames: r }, e),
              ),
              o().createElement(Fn, { getStepByRailClick: c, api: t, onDrag: m, classNames: d }),
            );
          },
          vn = ({ api: e, className: t, classNames: u, children: a, style: n }) => (
            (0, s.useEffect)(() => xe(e.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(Cn.base, t), style: n },
              o().createElement(
                "div",
                {
                  className: l()(Cn.wrapper, null == u ? void 0 : u.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: l()(Cn.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  a,
                ),
              ),
            )
          );
        ((vn.Bar = Fn),
          (vn.Default = Bn),
          (vn.SeniorityAwards = ({ api: e, className: t, classNames: u, children: a }) => (
            (0, s.useEffect)(() => xe(e.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(Cn.base, t) },
              o().createElement(
                "div",
                { className: l()(Cn.wrapper, null == u ? void 0 : u.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: l()(Cn.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  a,
                ),
              ),
            )
          )));
        const bn = rn({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? an.Next : an.Prev),
          }),
          fn = "VerticalBar_base_f3",
          wn = "VerticalBar_base__nonActive_42",
          Sn = "VerticalBar_topButton_d7",
          xn = "VerticalBar_bottomButton_06",
          Rn = "VerticalBar_track_df",
          Pn = "VerticalBar_thumb_32",
          Ln = "VerticalBar_rail_43",
          yn = "disable",
          Tn = () => {},
          Nn = { pending: !1, offset: 0 },
          Mn = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          kn = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          On = (e, t) => Math.max(20, e.offsetHeight * t),
          In = (0, s.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = Mn, onDrag: a = Tn }) => {
              const n = (0, s.useRef)(null),
                r = (0, s.useRef)(null),
                i = (0, s.useRef)(null),
                c = (0, s.useRef)(null),
                m = (0, s.useRef)(null),
                d = e.stepTimeout || 100,
                E = (0, s.useState)(Nn),
                _ = E[0],
                g = E[1],
                A = (0, s.useCallback)(
                  (e) => {
                    (g(e),
                      m.current &&
                        a({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [a],
                ),
                p = Ka(() => {
                  const t = m.current,
                    u = c.current,
                    a = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(a && r && t && u)) return;
                  const s = Math.min(1, a / r);
                  return (
                    (t.style.height = `${On(u, s)}px`),
                    t.classList.add(Pn),
                    n.current &&
                      (1 === s ? n.current.classList.add(wn) : n.current.classList.remove(wn)),
                    s
                  );
                }),
                D = Ka(() => {
                  const t = c.current,
                    u = m.current,
                    a = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(a && t && u && n)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, a / n),
                    l = zt(0, 1, s / (n - a)),
                    d = (t.offsetHeight - On(t, o)) * l;
                  ((u.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (r.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (r.current.classList.add(yn), void i.current.classList.remove(yn));
                        if (
                          ((t = c.current),
                          (u = m.current),
                          e - (t.offsetHeight - u.offsetHeight) >= -0.5)
                        )
                          return (r.current.classList.remove(yn), void i.current.classList.add(yn));
                        var t, u;
                        (r.current.classList.remove(yn), i.current.classList.remove(yn));
                      }
                    })(d));
                }),
                h = Ka(() => {
                  kn(e, () => {
                    (p(), D());
                  });
                });
              ((0, s.useEffect)(() => xe(h)),
                (0, s.useEffect)(() => {
                  const t = () => {
                    kn(e, () => {
                      D();
                    });
                  };
                  let u = Tn;
                  const a = () => {
                    (u(), (u = xe(h)));
                  };
                  return (
                    e.events.on("recalculateContent", h),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", a),
                    () => {
                      (u(),
                        e.events.off("recalculateContent", h),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", a));
                    }
                  );
                }, [e]),
                (0, s.useEffect)(() => {
                  if (!_.pending) return;
                  const t = (t) => {
                      kn(e, (u) => {
                        const n = c.current,
                          r = m.current,
                          s = e.getContainerSize();
                        if (!n || !r || !s) return;
                        const o = t.screenY - _.offset - n.getBoundingClientRect().y,
                          i = (o / n.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(u, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: u.scrollTop },
                        }),
                          a({ type: "dragging", thumb: r, thumbOffset: o, contentOffset: i }));
                      });
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        A(Nn));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, _.offset, _.pending, a, A]));
              const F = Qa((t) => e.applyStepTo(t), d, [e]),
                C = F[0],
                B = F[1];
              (0, s.useEffect)(
                () => (
                  document.addEventListener("mouseup", B, !0),
                  () => document.removeEventListener("mouseup", B, !0)
                ),
                [B],
              );
              const v = (e) => {
                e.target.classList.contains(yn) || J("highlight");
              };
              return o().createElement(
                "div",
                { className: l()(fn, t.base), ref: n, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: l()(Sn, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(yn) || 0 !== e.button || (J("play"), C(an.Next));
                  },
                  ref: r,
                  onMouseEnter: v,
                }),
                o().createElement(
                  "div",
                  {
                    className: l()(Rn, t.track),
                    onMouseDown: (t) => {
                      const a = m.current;
                      if (a && 0 === t.button)
                        if ((J("play"), t.target === a))
                          (e.handleIsThumbDragging(!0),
                            A({ pending: !0, offset: t.screenY - a.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            m.current &&
                              kn(e, (a) => {
                                if (!a) return;
                                const n = u(e),
                                  r = e.clampPosition(a, a.scrollTop + n * t);
                                e.applyScroll(r);
                              });
                          })(t.screenY > a.getBoundingClientRect().y ? an.Prev : an.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: v,
                  },
                  o().createElement("div", { ref: m, className: t.thumb }),
                  o().createElement("div", { className: l()(Ln, t.rail) }),
                ),
                o().createElement("div", {
                  className: l()(xn, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(yn) || 0 !== e.button || (J("play"), C(an.Prev));
                  },
                  onMouseUp: B,
                  ref: i,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          Hn = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Un = ({
            children: e,
            api: t,
            className: u,
            barClassNames: a,
            areaClassName: n,
            scrollClassName: r,
            scrollClassNames: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, s.useMemo)(() => {
                const e = a || {};
                return Object.assign({}, e, { base: l()(Hn.base, e.base) });
              }, [a]),
              E = (0, s.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return o().createElement(
              "div",
              { className: l()(Hn.defaultScroll, u), onWheel: t.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Hn.area, n) },
                o().createElement($n, { className: r, classNames: i, api: E }, e),
              ),
              o().createElement(In, { getStepByRailClick: c, api: t, onDrag: m, classNames: d }),
            );
          },
          $n = ({ className: e, classNames: t, children: u, api: a }) => (
            (0, s.useEffect)(() => xe(a.recalculateContent)),
            o().createElement(
              "div",
              { className: l()(Hn.base, e), ref: a.wrapperRef, onWheel: a.handleMouseWheel },
              o().createElement(
                "div",
                { className: l()(Hn.content, null == t ? void 0 : t.content), ref: a.contentRef },
                u,
              ),
            )
          );
        $n.Default = Un;
        const Wn = { Vertical: n, Horizontal: a },
          Gn = { type: "idle" };
        const Vn = "AnnouncementChapter_base_fd",
          zn = "AnnouncementChapter_base__hover_2c",
          jn = "AnnouncementChapter_background_6a",
          Xn = "AnnouncementChapter_baseBackground_57",
          qn = "AnnouncementChapter_baseShadow_bc",
          Zn = "AnnouncementChapter_stateStage_0f",
          Yn = "AnnouncementChapter_announcementText_2b",
          Kn = "AnnouncementChapter_topLeftBorder_0b",
          Qn = "AnnouncementChapter_topRightBorder_42",
          Jn = "AnnouncementChapter_bottomLeftBorder_d6",
          er = "AnnouncementChapter_bottomRightBorder_14",
          tr = R.strings.paragons.seasonsProgression,
          ur = (0, s.memo)(() => {
            const e = (0, s.useState)(!1),
              t = e[0],
              u = e[1],
              a = l()(Vn, t && zn);
            return o().createElement(
              "div",
              {
                className: a,
                onMouseEnter: () => {
                  u(!0);
                },
                onMouseLeave: () => {
                  u(!1);
                },
              },
              o().createElement("div", { className: jn }),
              o().createElement("div", { className: Xn }),
              o().createElement("div", { className: qn }),
              o().createElement(
                "div",
                { className: Zn },
                o().createElement(Et.ZP, { text: tr.stageText.availableSoon(), className: Yn }),
              ),
              o().createElement("div", { className: Kn }),
              o().createElement("div", { className: Qn }),
              o().createElement("div", { className: Jn }),
              o().createElement("div", { className: er }),
            );
          }),
          ar = "Chapter_dynamicWrapper_26";
        var nr = u(7044);
        const rr = {
            base: "BottomStage_base_2d",
            name: "BottomStage_name_e4",
            base__paused: "BottomStage_base__paused_61",
            base__hovered: "BottomStage_base__hovered_22",
            textButton: "BottomStage_textButton_c4",
            completedBlock: "BottomStage_completedBlock_d0",
            completed: "BottomStage_completed_22",
            pausedBlock: "BottomStage_pausedBlock_0c",
            paused: "BottomStage_paused_0a",
            activeText: "BottomStage_activeText_3e",
            disabledText: "BottomStage_disabledText_62",
            pausedText: "BottomStage_pausedText_29",
            finishedHasRewardsText: "BottomStage_finishedHasRewardsText_68",
            btn: "BottomStage_btn_24",
            rewardStage: "BottomStage_rewardStage_a1",
            base__disabled: "BottomStage_base__disabled_66",
          },
          sr = R.strings.paragons,
          or = sr.seasonsProgression,
          ir = (0, s.memo)(({ chapter: e, isHovered: t, onSelectChapter: u }) => {
            const a = e.id,
              n = e.chapterStatus.status,
              r = e.isAllRewardsClaimed,
              i = sr.chapterName.$dyn(`id_${a}`),
              c = (0, s.useCallback)(
                (e) => (t) => {
                  (t.stopPropagation(), u(e));
                },
                [u],
              );
            return o().createElement(
              "div",
              { className: l()(rr.base, rr[`base__${n}`], t && rr.base__hovered) },
              o().createElement(Et.ZP, { text: i, className: rr.name }),
              n === Ge.ACTIVE &&
                o().createElement(Et.ZP, {
                  text: or.stageText.activeStage(),
                  className: rr.activeText,
                }),
              n === Ge.DISABLED &&
                o().createElement(Et.ZP, {
                  text: or.stageText.disabledStage(),
                  className: rr.disabledText,
                }),
              n === Ge.PAUSED &&
                o().createElement(
                  "div",
                  null,
                  t
                    ? o().createElement(
                        re,
                        { mixClass: rr.btn, size: ae.medium, type: ue.primary, onClick: c(a) },
                        o().createElement(Et.ZP, {
                          text: or.stageText.selectStage(),
                          className: rr.textButton,
                        }),
                      )
                    : o().createElement(
                        "div",
                        { className: rr.pausedBlock },
                        o().createElement("div", { className: rr.paused }),
                        o().createElement(Et.ZP, {
                          text: or.stageText.pausedStage(),
                          className: rr.pausedText,
                        }),
                      ),
                ),
              n === Ge.FINISHED &&
                !r &&
                o().createElement(Et.ZP, {
                  text: or.stageText.finishedHasRewardsStage(),
                  className: rr.finishedHasRewardsText,
                }),
              n === Ge.DEFAULT &&
                o().createElement(
                  re,
                  { mixClass: rr.btn, size: ae.medium, type: ue.primary, onClick: c(a) },
                  o().createElement(Et.ZP, {
                    text: or.stageText.selectStage(),
                    className: rr.textButton,
                  }),
                ),
              n === Ge.FINISHED &&
                r &&
                o().createElement(
                  "div",
                  { className: rr.completedBlock },
                  o().createElement("div", { className: rr.completed }),
                ),
            );
          }),
          lr = "Progression_base_d0",
          cr = "Progression_progressLineContainer_c4",
          mr = "Progression_progressLineContainer__instantAnimation_60",
          dr = "Progression_point_53",
          Er = "Progression_line_75",
          _r = "Progression_line__top_b6",
          gr = "Progression_line__bottom_ae",
          Ar = {
            [d.cJ.ExtraSmall]: { pointsDistance: 47, pointsFirstIndent: 10 },
            [d.cJ.Small]: { pointsDistance: 47, pointsFirstIndent: 10 },
            [d.cJ.Medium]: { pointsDistance: 68, pointsFirstIndent: 10 },
            [d.cJ.Large]: { pointsDistance: 68, pointsFirstIndent: 10 },
            [d.cJ.ExtraLarge]: { pointsDistance: 68, pointsFirstIndent: 10 },
          },
          pr = (0, s.memo)(
            ({
              points: e,
              currentLevel: t,
              levels: u,
              maxPointsCount: a,
              maxLevel: n,
              progressionConfig: r = Ar,
              isResize: i,
            }) => {
              const c = (0, s.useRef)({ update: () => {} }),
                m = (0, d.GS)().mediaSize,
                E = r[m].pointsDistance,
                _ = (0, s.useMemo)(() => [0, ...u.map((e) => e.number)], [u]),
                g = -1 * (t - 1) * E + r[m].pointsFirstIndent;
              return o().createElement(
                "div",
                { className: lr },
                o().createElement(
                  "div",
                  {
                    className: l()(cr, i && mr),
                    style: { width: E * n + "rem", transform: `translateX(${g}rem)` },
                  },
                  _.map((e, t) =>
                    o().createElement(
                      "div",
                      {
                        key: e,
                        className: l()(dr),
                        style: { transform: `translateX(${t * E}rem)` },
                      },
                      o().createElement("div", { className: l()(Er, _r) }),
                      o().createElement("div", { className: l()(Er, gr) }),
                    ),
                  ),
                  o().createElement(Mu, {
                    animationSettings: ku,
                    value: (0, Ke.ZI)(e, t, u),
                    maxValue: a,
                    api: c,
                    size: Xt.Small,
                  }),
                ),
              );
            },
          ),
          Dr = {
            base: "UnifiedChapter_base_be",
            base__active: "UnifiedChapter_base__active_35",
            base__active__hover: "UnifiedChapter_base__active__hover_b0",
            base__default: "UnifiedChapter_base__default_d3",
            base__default__hover: "UnifiedChapter_base__default__hover_85",
            base__paused: "UnifiedChapter_base__paused_fd",
            base__disabled: "UnifiedChapter_base__disabled_f7",
            base__finished: "UnifiedChapter_base__finished_c7",
            base__finished__hover: "UnifiedChapter_base__finished__hover_68",
            base__hover: "UnifiedChapter_base__hover_fb",
            allSpace: "UnifiedChapter_allSpace_aa",
            baseBackground: "UnifiedChapter_baseBackground_83",
            baseBackgroundHover: "UnifiedChapter_baseBackgroundHover_5d",
            backgroundDots: "UnifiedChapter_backgroundDots_d0",
            baseBorder: "UnifiedChapter_baseBorder_ab",
            background: "UnifiedChapter_background_cc",
            crewIcon: "UnifiedChapter_crewIcon_9e",
            backgroundShadow: "UnifiedChapter_backgroundShadow_07",
            tankForeground: "UnifiedChapter_tankForeground_f0",
            tankForeground__instantAnimation: "UnifiedChapter_tankForeground__instantAnimation_fb",
            bottomContentStage: "UnifiedChapter_bottomContentStage_66",
            rewardStage: "UnifiedChapter_rewardStage_2f",
            btn: "UnifiedChapter_btn_c8",
            widgetContainer: "UnifiedChapter_widgetContainer_d6",
            miniProgress: "UnifiedChapter_miniProgress_d6",
            timeInfo: "UnifiedChapter_timeInfo_72",
            timeText: "UnifiedChapter_timeText_44",
            rectangleTop: "UnifiedChapter_rectangleTop_21",
            rectangleButton: "UnifiedChapter_rectangleButton_88",
            rectangleLeft: "UnifiedChapter_rectangleLeft_e5",
            rectangleRight: "UnifiedChapter_rectangleRight_01",
            progress: "UnifiedChapter_progress_f2",
            textButton: "UnifiedChapter_textButton_d6",
            topLeftBorder: "UnifiedChapter_topLeftBorder_5b",
            topRightBorder: "UnifiedChapter_topRightBorder_e3",
            bottomLeftBorder: "UnifiedChapter_bottomLeftBorder_28",
            bottomRightBorder: "UnifiedChapter_bottomRightBorder_c0",
          },
          hr = "WidgetChapter_base_a7",
          Fr = "WidgetChapter_base__instantAnimation_73",
          Cr = "WidgetChapter_iconStage_24",
          Br = "WidgetChapter_counter_21",
          vr = "WidgetChapter_iconShadow_1e",
          br = "WidgetChapter_base__hover_da",
          fr = "WidgetChapter_level_d7",
          wr = (0, s.memo)(({ isHovered: e, level: t, isResize: u }) => {
            const a = l()(hr, e && br, u && Fr);
            return o().createElement(
              "div",
              { className: a },
              o().createElement(
                "div",
                { className: Cr },
                o().createElement(
                  "div",
                  { className: Br },
                  o().createElement(Et.ZP, { text: String(t), className: fr }),
                ),
              ),
              o().createElement("div", { className: vr }),
            );
          }),
          Sr = "R.images.gui.maps.icons.paragons.seasons",
          xr = 10 * nr.s_,
          Rr = {
            [d.cJ.ExtraSmall]: { pointsDistance: 80, pointsFirstIndent: 20 },
            [d.cJ.Small]: { pointsDistance: 80, pointsFirstIndent: 20 },
            [d.cJ.Medium]: { pointsDistance: 80, pointsFirstIndent: 20 },
            [d.cJ.Large]: { pointsDistance: 120, pointsFirstIndent: 20 },
            [d.cJ.ExtraLarge]: { pointsDistance: 160, pointsFirstIndent: 20 },
          },
          Pr = (0, s.memo)(({ chapter: e, onSelectChapter: t, onToChapterRewards: u }) => {
            var a;
            const n = (0, s.useState)(!1),
              r = n[0],
              i = n[1],
              c = (0, s.useState)(!1),
              m = c[0],
              d = c[1],
              E = (0, s.useState)(""),
              _ = E[0],
              g = E[1],
              A = (0, s.useState)(!1),
              p = A[0],
              D = A[1],
              h = e.timeStamp,
              F = e.chapterStatus.status,
              C = e.chapterLevel,
              B = e.levels,
              v = e.points,
              b = e.id,
              f = B.length,
              w = (null == (a = B[f - 1]) ? void 0 : a.maxPoints) || 0,
              S = F === Ge.ACTIVE,
              x = F === Ge.PAUSED,
              P = l()(Dr.base, r && Dr.base__hover, Dr[`base__${F}`], r && Dr[`base__${F}__hover`]),
              L = `url('${Sr}.season_${b}.tank')`,
              y = `url('${Sr}.season_${b}.card')`,
              T = `url('${Sr}.season_${b}.background')`,
              N = S || x || F === Ge.DEFAULT || (F === Ge.FINISHED && !e.isAllRewardsClaimed);
            var M, k, O;
            return (
              (M = () => d(!0)),
              (k = []),
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", M),
                  () => window.removeEventListener("resize", M)
                ),
                k,
              ),
              (0, s.useEffect)(() => {
                m &&
                  tu(() => {
                    d(!1);
                  }, 0);
              }, [m]),
              (0, s.useEffect)(() => {
                (g((0, Ke.ST)(h)), D((0, Ke.P8)(h) && N));
                const e = setInterval(() => {
                  (g((0, Ke.ST)(h)), D((0, Ke.P8)(h) && N));
                }, xr);
                return () => {
                  clearInterval(e);
                };
              }, [h, N]),
              o().createElement(
                "div",
                {
                  className: P,
                  onMouseEnter: () => {
                    (J(R.sounds.paragons_card_hover()), i(!0));
                  },
                  onMouseLeave: () => {
                    (J(R.sounds.paragons_card_hover()), i(!1));
                  },
                  onClick:
                    ((O = b),
                    () => {
                      (u(O), ee.playClick());
                    }),
                },
                o().createElement("div", {
                  className: l()(Dr.background, Dr.allSpace),
                  style: { backgroundImage: T },
                }),
                o().createElement("div", {
                  className: l()(Dr.tankForeground, m && Dr.tankForeground__instantAnimation),
                  style: { backgroundImage: L },
                }),
                o().createElement(
                  "div",
                  { className: l()(Dr.baseBackground, Dr.allSpace) },
                  o().createElement(
                    "div",
                    { className: l()(Dr.backgroundDots, Dr.allSpace) },
                    S && o().createElement("div", { className: l()(Dr.baseBorder, Dr.allSpace) }),
                  ),
                ),
                o().createElement("div", { className: l()(Dr.baseBackgroundHover, Dr.allSpace) }),
                o().createElement("div", {
                  className: l()(Dr.crewIcon, Dr.allSpace),
                  style: { backgroundImage: y },
                }),
                o().createElement(
                  "div",
                  { className: Dr.bottomContentStage },
                  (S || x) &&
                    o().createElement(
                      o().Fragment,
                      null,
                      o().createElement(
                        "div",
                        { className: Dr.widgetContainer },
                        o().createElement(wr, { isHovered: r, level: C, isResize: m }),
                      ),
                      o().createElement(
                        "div",
                        { className: Dr.miniProgress },
                        o().createElement(pr, {
                          points: v,
                          currentLevel: C,
                          maxLevel: f,
                          maxPointsCount: w,
                          levels: B,
                          progressionConfig: Rr,
                          isResize: m,
                        }),
                      ),
                    ),
                  o().createElement(ir, { chapter: e, onSelectChapter: t, isHovered: r }),
                ),
                p &&
                  o().createElement(
                    "div",
                    { className: Dr.timeInfo },
                    o().createElement(Vt.N, {
                      text: _,
                      timeStamp: h,
                      showBg: !0,
                      mixClass: Dr.timeText,
                    }),
                  ),
                o().createElement("div", { className: Dr.topLeftBorder }),
                o().createElement("div", { className: Dr.topRightBorder }),
                o().createElement("div", { className: Dr.bottomLeftBorder }),
                o().createElement("div", { className: Dr.bottomRightBorder }),
              )
            );
          }),
          Lr = (0, s.memo)(({ chapter: e, onSelectChapter: t, onToChapterRewards: u }) => {
            const a = e.chapterStatus.status,
              n = e.id,
              r = a === Ge.ACTIVE,
              s = a === Ge.ANNOUNCEMENT,
              i = {
                contentId: r
                  ? R.views.lobby.paragons.tooltips.EntryPointTooltip("resId")
                  : R.views.lobby.paragons.tooltips.SeasonTooltip("resId"),
                args: { chapterId: n },
              };
            return o().createElement(
              ca,
              { tooltipArgs: i, className: ar },
              s
                ? o().createElement(ur, null)
                : o().createElement(Pr, { chapter: e, onSelectChapter: t, onToChapterRewards: u }),
            );
          }),
          yr = "SeasonsProgress_base_a2",
          Tr = "SeasonsProgress_scrollArea_51",
          Nr = "SeasonsProgress_chaptersWrapper_64",
          Mr = "SeasonsProgress_scrollWrapper_f6",
          kr = "SeasonsProgress_scrollContent_04",
          Or = "SeasonsProgress_scrollBar_36",
          Ir = "SeasonsProgress_chapterListContainer_f8",
          Hr = (0, s.memo)(({ allChapters: e, onSelectChapter: t, onToChapterRewards: u }) => {
            const a = sn();
            return (
              (function (e, t, u) {
                const a = e.contentRef,
                  n = e.wrapperRef,
                  r = e.scrollPosition,
                  o = e.clampPosition,
                  i = e.animationScroll,
                  l = e.events,
                  c = (0, s.useState)(Gn),
                  m = c[0],
                  d = c[1];
                ((0, s.useEffect)(() => {
                  const e = a.current;
                  e && (e.style.cursor = "dragging" === m.type ? "move" : "grab");
                }, [a, m.type]),
                  (0, s.useEffect)(() => {
                    if ("dragging" !== m.type) return;
                    const e = w.O.client.events.mouse.move(([e, u]) => {
                        const s = a.current,
                          l = n.current;
                        if (!s || !l) return;
                        if ("inside" === u && e.clientX < 0) return;
                        const c = "inside" === u ? e.clientX : e.clientX - l.offsetLeft,
                          d = m.positionFrom - c,
                          E = m.previousScrollPosition + d;
                        r.start(
                          Object.assign(
                            {
                              scrollPosition: o(s, E),
                              from: { scrollPosition: i.scrollPosition.get() },
                            },
                            t && { config: t },
                          ),
                        );
                      }),
                      u = w.O.client.events.mouse.up(function () {
                        d({ type: "scrollingToEnd" });
                      });
                    return () => {
                      (e(), u());
                    };
                  }, [i.scrollPosition, o, a, m, r, n, t]),
                  (0, s.useEffect)(() => {
                    if ("scrollingToEnd" !== m.type) return;
                    const e = () => {
                      d(Gn);
                    };
                    return (i.scrollPosition.idle && e(), l.on("rest", e), () => l.off("rest", e));
                  }, [i.scrollPosition, m.type, l]),
                  (0, s.useEffect)(() => {
                    const e = a.current;
                    if (!e) return;
                    const t = (e) => {
                      (u &&
                        u.allowedButtons &&
                        -1 === u.allowedButtons.findIndex((t) => e.button === t)) ||
                        d({
                          type: "dragging",
                          positionFrom: e.screenX,
                          previousScrollPosition: i.scrollPosition.get(),
                        });
                    };
                    return (
                      e.addEventListener("mousedown", t),
                      () => e.removeEventListener("mousedown", t)
                    );
                  }, [i.scrollPosition, a, u]));
              })(Object.assign({}, a)),
              o().createElement(
                "div",
                { className: yr },
                o().createElement(
                  "div",
                  { className: Tr },
                  o().createElement(
                    Wn.Horizontal.Area.Default,
                    {
                      api: a,
                      className: Nr,
                      classNames: { content: kr, wrapper: Mr },
                      barClassNames: { base: Or },
                    },
                    o().createElement(
                      "div",
                      { className: Ir },
                      e.map((e) =>
                        o().createElement(Lr, {
                          key: e.id,
                          chapter: e,
                          onSelectChapter: t,
                          onToChapterRewards: u,
                        }),
                      ),
                    ),
                  ),
                ),
              )
            );
          }),
          Ur = "SeasonsView_base_89",
          $r = "SeasonsView_headerWrapper_b2",
          Wr = R.strings.paragons,
          Gr = Wr.seasonsProgression,
          Vr = (0, V.Pi)(() => {
            const e = tt(),
              t = e.model,
              u = e.controls,
              a = t.computes.hasActiveSeason(),
              n = t.computes.isAllAvailableSeasonsCompleted(),
              r = t.computes.getStages(),
              s = n ? Gr.subtitle.allStagesCompleted() : Gr.subtitle.selectStageForGetReward(),
              i = a ? "" : s;
            return o().createElement(
              "div",
              { className: Ur },
              o().createElement(
                "div",
                { className: $r },
                o().createElement(Ze.h, {
                  topTitle: Wr.project.name(),
                  mainTitle: Gr.title.projectStages(),
                  subtitle: i,
                }),
              ),
              o().createElement(Hr, {
                allChapters: r,
                onSelectChapter: u.onSelectChapter,
                onToChapterRewards: u.onToChapterRewards,
              }),
            );
          }),
          zr = R.strings.paragons,
          jr = zr.navigation,
          Xr = (0, V.Pi)(() => {
            const e = tt(),
              t = e.controls,
              u = e.model,
              a = u.root.get(),
              n = a.hasNewProgress,
              r = a.hasNewChapters,
              i = a.currentTabId,
              c = a.vehicleCount,
              m = a.necessaryVehicleCount,
              d = u.computes.getPreviewSeason(),
              E = u.computes.getCurrentSeason(),
              _ = (null == E ? void 0 : E.id) || -1,
              g = d || E,
              A = (null == g ? void 0 : g.id) || -1,
              p = Boolean(d),
              D = p || _ > 0,
              h = p && _ <= 0,
              F = h ? jr.button.gotoSeasons() : jr.button.goto(),
              C = p && (null == g ? void 0 : g.chapterStatus.status) === Ge.DEFAULT,
              B = (0, s.useCallback)(() => {
                h ? t.onBackToSeasons() : t.onBack();
              }, [t, h]),
              v = (0, s.useCallback)(
                (e) => () => {
                  t.onTabChange(e);
                },
                [t],
              ),
              b = (0, s.useCallback)(
                (e, u) => {
                  t.onSelectVehicleReward(e, u, A);
                },
                [t, A],
              ),
              f = (0, s.useMemo)(
                () => ({
                  [Ve.progress]: {
                    hasNewItems: n,
                    isVisibleTab: D,
                    component:
                      g &&
                      o().createElement(Za, {
                        currentSeason: g,
                        paragonPoints: g.points,
                        onPreviewVehicle: t.onPreviewVehicle,
                        onSelectVehicleReward: b,
                        onSeasonActivate: t.onSeasonActivate,
                        necessaryVehicleCount: m,
                        vehicleCount: c,
                        hasSeasonActivateButton: C,
                        selectedSeason: A,
                      }),
                  },
                  [Ve.chapters]: {
                    hasNewItems: r,
                    isVisibleTab: !0,
                    component: o().createElement(Vr, null),
                  },
                  [Ve.about]: {
                    hasNewItems: !1,
                    isVisibleTab: !0,
                    component: o().createElement(
                      "div",
                      { className: at },
                      o().createElement("div", { className: nt }),
                      o().createElement(
                        "div",
                        { className: mt },
                        o().createElement(Ze.h, { mainTitle: zr.project.name() }),
                      ),
                      o().createElement(
                        "div",
                        { className: dt },
                        o().createElement(Ie, { isFullSize: !0, options: { rootId: Ve.about } }),
                      ),
                    ),
                  },
                }),
                [n, D, g, t.onPreviewVehicle, t.onSeasonActivate, b, m, c, C, A, r],
              ),
              S = (0, s.useMemo)(() => Object.keys(f).filter((e) => f[e].isVisibleTab), [f]);
            return (
              (function ({
                key: e = ze.n.ESCAPE,
                callback: t = () => w.O.view.sendEvent.close(),
                preventPropagation: u = !0,
              } = {}) {
                qe(e, t, u);
              })({ callback: t.onBack, preventPropagation: !1 }),
              o().createElement(
                "div",
                { className: ut },
                o().createElement(
                  "div",
                  { className: l()(rt, st) },
                  o().createElement(We, {
                    caption: jr.button.back(),
                    side: "left",
                    type: "back",
                    onClick: B,
                    goto: F,
                  }),
                ),
                (!p || Boolean(E)) &&
                  o().createElement(
                    "div",
                    { className: l()(rt, ot) },
                    o().createElement(We, {
                      caption: jr.button.close(),
                      side: "right",
                      type: "close",
                      onClick: t.onClose,
                    }),
                  ),
                !h &&
                  o().createElement(
                    "div",
                    { className: it },
                    o().createElement(
                      "div",
                      { className: lt },
                      S.map((e) =>
                        o().createElement(kt, {
                          key: e,
                          tabId: e,
                          seasonId: A,
                          isSelected: i === Number(e),
                          onClick: v(e),
                          hasNewItems: f[e].hasNewItems,
                        }),
                      ),
                    ),
                  ),
                o().createElement("div", { className: ct }, f[i].component),
              )
            );
          });
        const qr = {
            wasSold: !1,
            inInventory: !0,
            rentBattles: 0,
            rentDays: 0,
            isRent: !1,
            isElite: !0,
            nationTag: "ussr",
            shortVehicleLabel: "Об. 274а",
            level: 8,
            type: "mediumTank",
            vehicleName: "R180_Object_274_A",
            overlayType: "",
            item: "",
            label: "Объект 274а",
            tooltipContentId: "25",
            tooltipId: "1",
            isCompensation: !1,
            value: "",
            name: "vehicles",
            index: 0,
            isReceived: !1,
            isClaimed: !0,
            isSelectable: !1,
            isSelectableClaimed: !1,
            icon: "",
          },
          Zr = {
            name: "tmanToken",
            label: "Mock Tankman label",
            value: "Mock Tankman value",
            icon: "tankmen_BP14_1",
            isClaimed: !0,
            index: 1,
            isCompensation: !1,
            tooltipId: "",
            tooltipContentId: "",
          },
          Yr = {
            name: "credits",
            value: "50000",
            icon: "credits",
            isClaimed: !0,
            label: "Mock Tankman label",
            index: 1,
            isCompensation: !1,
            tooltipId: "",
            tooltipContentId: "",
          },
          Kr = {
            name: "branch",
            icon: "branch",
            value: "Branch selection",
            isReceived: !1,
            isClaimed: !1,
            isSelectable: !0,
            isSelectableClaimed: !1,
            label: "",
            index: 1,
            isCompensation: !1,
            tooltipId: "",
            tooltipContentId: "",
          },
          Qr = {
            name: "vehicleSelect",
            icon: "vehicleSelect",
            isReceived: !1,
            isVehicleSelectAvailable: !0,
            value: "",
            isClaimed: !1,
            label: "",
            index: 1,
            isCompensation: !1,
            tooltipId: "",
            tooltipContentId: "",
          },
          Jr = {
            name: "vehicleSelect",
            icon: "vehicleSelect",
            isReceived: !1,
            isVehicleSelectAvailable: !1,
            value: "",
            isClaimed: !1,
            label: "",
            index: 1,
            isCompensation: !1,
            tooltipId: "",
            tooltipContentId: "",
          },
          es = [
            {
              number: 1,
              maxPoints: 150,
              isCompleted: !1,
              mainRewards: [Zr],
              equalRewards: [qr, Yr],
              rewards: [qr, Zr, Yr],
            },
            {
              number: 2,
              maxPoints: 300,
              isCompleted: !1,
              mainRewards: [qr],
              equalRewards: [Zr, Yr],
              rewards: [qr, Zr, Yr],
            },
            {
              number: 3,
              maxPoints: 450,
              isCompleted: !1,
              mainRewards: [Jr],
              equalRewards: [qr, Yr],
              rewards: [Jr, qr, Yr],
            },
            {
              number: 4,
              maxPoints: 600,
              isCompleted: !1,
              mainRewards: [],
              equalRewards: [Zr],
              rewards: [Zr],
            },
            {
              number: 5,
              maxPoints: 750,
              isCompleted: !1,
              mainRewards: [],
              equalRewards: [Zr, qr, Yr],
              rewards: [Zr, qr, Yr],
            },
            {
              number: 6,
              maxPoints: 1050,
              isCompleted: !1,
              mainRewards: [Qr],
              equalRewards: [Yr],
              rewards: [Qr, Yr],
            },
            {
              number: 7,
              maxPoints: 1350,
              isCompleted: !1,
              mainRewards: [],
              equalRewards: [Kr, qr],
              rewards: [Kr, qr],
            },
            {
              number: 8,
              maxPoints: 1650,
              isCompleted: !1,
              mainRewards: [Yr],
              equalRewards: [Zr, qr],
              rewards: [Yr, Zr, qr],
            },
            {
              number: 9,
              maxPoints: 1950,
              isCompleted: !1,
              mainRewards: [Zr],
              equalRewards: [qr, Yr],
              rewards: [Zr, qr, Yr],
            },
            {
              number: 10,
              maxPoints: 2250,
              isCompleted: !1,
              mainRewards: [qr],
              equalRewards: [Zr, Yr],
              rewards: [qr, Zr, Yr],
            },
          ],
          ts = {
            id: 1,
            name: "+++Название этапа 1",
            chapterStatus: { status: Ge.DEFAULT },
            chapterLevel: 5,
            points: 650,
            levels: [
              { number: 1, maxPoints: 150, isCompleted: !0, rewards: [qr, Zr, Yr] },
              { number: 2, maxPoints: 300, isCompleted: !0, rewards: [qr, Zr, Yr] },
              { number: 3, maxPoints: 450, isCompleted: !0, rewards: [Jr, qr, Yr] },
              { number: 4, maxPoints: 600, isCompleted: !0, rewards: [Zr] },
              { number: 5, maxPoints: 750, isCompleted: !1, rewards: [Zr, qr, Yr] },
              { number: 6, maxPoints: 1050, isCompleted: !1, rewards: [Qr, Yr] },
              { number: 7, maxPoints: 1350, isCompleted: !1, rewards: [Kr, qr] },
              { number: 8, maxPoints: 1650, isCompleted: !1, rewards: [Yr, Zr, qr] },
              { number: 9, maxPoints: 1950, isCompleted: !1, rewards: [Zr, qr, Yr] },
              { number: 10, maxPoints: 2250, isCompleted: !1, rewards: [qr, Zr, Yr] },
            ],
            finalVehicleCDs: [7937041, 7937601, 7938385],
          },
          us = {
            id: 2,
            name: "+++Название этапа 2",
            chapterStatus: { status: Ge.DEFAULT },
            chapterLevel: 1,
            points: 0,
            levels: [
              { number: 1, maxPoints: 150, isCompleted: !1, rewards: [qr, Zr, Yr] },
              { number: 2, maxPoints: 300, isCompleted: !1, rewards: [qr, Zr, Yr] },
              { number: 3, maxPoints: 450, isCompleted: !1, rewards: [Jr, qr, Yr] },
              { number: 4, maxPoints: 600, isCompleted: !1, rewards: [Zr] },
              { number: 5, maxPoints: 750, isCompleted: !1, rewards: [Zr, qr, Yr] },
              { number: 6, maxPoints: 1050, isCompleted: !1, rewards: [Qr, Yr] },
              { number: 7, maxPoints: 1350, isCompleted: !1, rewards: [Kr, qr] },
              { number: 8, maxPoints: 1650, isCompleted: !1, rewards: [Yr, Zr, qr] },
              { number: 9, maxPoints: 1950, isCompleted: !1, rewards: [Zr, qr, Yr] },
              { number: 10, maxPoints: 2250, isCompleted: !1, rewards: [qr, Zr, Yr] },
            ],
            finalVehicleCDs: [7937041, 7937601, 7938385],
          },
          as = (Ge.DISABLED, Ge.ACTIVE, Ge.FINISHED, Ge.ANNOUNCEMENT, [ts]),
          ns = {
            hasNewProgress: !1,
            hasNewChapters: !1,
            wasChapterSelected: !0,
            currentTabId: Ve.progress,
            previewSeasonId: 2,
            progression: { stages: [ts, us], currentStage: 1 },
            allRewards: { levels: es },
            allChapters: { allChapters: as },
          },
          rs = {
            getter: ((ss = ns), (e) => (e ? e.split(".").reduce((e, t) => e[t], ss) : ss)),
            controls: () =>
              (function (e) {
                const t = {};
                for (const u in e)
                  if (Object.prototype.hasOwnProperty.call(e, u)) {
                    const a = e[u];
                    t[u] = (0, f.aD)(a);
                  }
                return t;
              })({
                onBack: () => {
                  console.log("onBack");
                },
                onClose: () => {
                  console.log("onClose");
                },
                onTabChange: (e) => {
                  console.log("onChange", e);
                },
                onToStagesView: () => {
                  console.log("onToStagesView");
                },
                onPreviewVehicle: () => {
                  console.log("onPreviewVehicle");
                },
                onCompareVehicle: () => {
                  console.log("onCompareVehicle");
                },
                onSelectVehicle: () => {
                  console.log("onSelectVehicle");
                },
                onSelectChapter: (e) => {
                  console.log("onSelectChapter", e);
                },
                onSelectVehicleReward: (e, t) => {
                  console.log("onSelectVehicleReward", e, t);
                },
                onPreviewStyle: (e, t, u) => {
                  console.log("onPreviewStyle", e, t, u);
                },
                onToChapterRewards: (e) => {
                  console.log("onToChapterRewards", e);
                },
                onSeasonActivate: (e) => {
                  console.log("onSeasonActivate", e);
                },
                onBackToSeasons: () => {
                  console.log("onBackToSeasons");
                },
              }),
          };
        var ss;
        engine.whenReady.then(() => {
          B().render(
            o().createElement(
              et,
              { mode: "real", mocks: rs },
              o().createElement(F, null, o().createElement(Xr, null)),
            ),
            document.getElementById("root"),
          );
        });
      },
      7104: (e, t, u) => {
        "use strict";
        u.d(t, { N: () => l });
        var a = u(7613),
          n = u(6179),
          r = u.n(n),
          s = u(8998);
        const o = "DateTimer_base_55",
          i = "DateTimer_timeBg_2d",
          l = (0, n.memo)(({ text: e, timeStamp: t, showBg: u = !1, mixClass: n }) => {
            const l = (0, s._3)(t),
              c = l.day,
              m = l.month,
              d = l.hours,
              E = l.min;
            return r().createElement(
              "div",
              { className: o },
              u && r().createElement("div", { className: i }),
              r().createElement(a.ZP, {
                text: e,
                className: n,
                format: {
                  binding: {
                    day: c,
                    month: R.strings.menu.dateTime.months.$num(m + 1),
                    hours: d,
                    minutes: E,
                  },
                },
              }),
            );
          });
      },
      1685: (e, t, u) => {
        "use strict";
        u.d(t, { h: () => c });
        var a = u(7613),
          n = u(6179),
          r = u.n(n);
        const s = "Header_base_37",
          o = "Header_textContainer_22",
          i = "Header_mainTitle_85",
          l = "Header_subTitle_fb",
          c = (0, n.memo)(({ stage: e = 0, topTitle: t = "", mainTitle: u, subtitle: n = "" }) =>
            r().createElement(
              "div",
              { className: s },
              r().createElement(
                "div",
                { className: o },
                t && r().createElement(a.ZP, { text: t, className: l }),
                r().createElement(a.ZP, {
                  text: u,
                  format: { binding: { level: e } },
                  className: i,
                }),
                n && r().createElement(a.ZP, { text: n, className: l }),
              ),
            ),
          );
      },
      5190: (e, t, u) => {
        "use strict";
        u.d(t, { M2: () => p, uA: () => g, YH: () => A });
        var a = u(6483),
          n = u.n(a),
          r = u(7613);
        const s = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          o = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const i = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          l = (e) =>
            i
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let u = o.length - 1; u >= 0; u--)
                    for (; e >= o[u];) ((t += s[u]), (e -= o[u]));
                  return t;
                })(e);
        var c = u(3649),
          m = u(6179),
          d = u.n(m);
        const E = {
            base: "VehicleName_base_f4",
            base__white: "VehicleName_base__white_3d",
            base__whiteSpanish: "VehicleName_base__whiteSpanish_90",
            base__whiteOrange: "VehicleName_base__whiteOrange_52",
            base__cream: "VehicleName_base__cream_b3",
            nation: "VehicleName_nation_8b",
            base__colored: "VehicleName_base__colored_f2",
            level: "VehicleName_level_7d",
            type: "VehicleName_type_12",
            type__elite: "VehicleName_type__elite_0d",
            base__extraSmall: "VehicleName_base__extraSmall_74",
            base__medium: "VehicleName_base__medium_16",
            name: "VehicleName_name_5c",
          },
          _ = "R.images.gui.maps.icons",
          g = { ExtraSmall: "extraSmall", Small: "small", Medium: "medium" },
          A = {
            Colored: "colored",
            White: "white",
            WhiteSpanish: "whiteSpanish",
            WhiteOrange: "whiteOrange",
            Cream: "cream",
          },
          p = (0, m.memo)(
            ({
              isElite: e = !0,
              vehicleName: t,
              vehicleNation: u,
              vehicleType: a,
              vehicleLvl: s,
              isShortVehicleName: o = !1,
              size: i = g.Small,
              type: m = A.WhiteOrange,
              className: p,
            }) => {
              const D = n()(E.base, E[`base__${i}`], E[`base__${m}`], p),
                h = n()(E.type, e && E.type__elite),
                F = g.Medium ? "big" : "c_64x64";
              return d().createElement(
                "div",
                { className: D },
                !o &&
                  d().createElement(
                    d().Fragment,
                    null,
                    u &&
                      d().createElement("div", {
                        className: E.nation,
                        style: { backgroundImage: `url(${_}.flags.c_25x17.${u})` },
                      }),
                    d().createElement(r.ZP, { text: l(s), className: E.level }),
                    d().createElement("div", {
                      className: h,
                      style: {
                        backgroundImage: `url(${_}.vehicleTypes.${F}.${(0, c.BN)(a)}${e ? "_elite" : ""})`,
                      },
                    }),
                  ),
                d().createElement(r.ZP, { text: t, className: E.name }),
              );
            },
          );
      },
      8998: (e, t, u) => {
        "use strict";
        u.d(t, { P8: () => E, ST: () => _, ZI: () => m, _3: () => d, lW: () => l });
        var a = u(2862),
          n = u(729),
          r = u(7044),
          s = u(3649);
        u(4179);
        const o = [a.E4.Branch, a.E4.VehicleSelect, a.E4.ParagonsUnlocks, a.E4.StyleProgress],
          i = R.strings.paragons.seasonsProgression.timeLeft,
          l = (e, t, u) => ({
            name: e.name,
            image: (t) =>
              ((e, t = a.h2.Small) => {
                const u = (0, s.BN)(e.vehicleName || "");
                if (e.name === a.E4.Vehicles)
                  switch (t) {
                    case a.h2.Mini:
                    case a.h2.Small:
                    case a.h2.S48x48:
                      return e.isRent
                        ? "R.images.gui.maps.icons.quests.bonuses.small.vehicles_rent"
                        : `R.images.gui.maps.icons.quests.bonuses.small.${u}`;
                    case a.h2.Big:
                    case a.h2.S80x80:
                      return e.isRent
                        ? "R.images.gui.maps.icons.quests.bonuses.big.vehicles_rent"
                        : `R.images.gui.maps.icons.quests.bonuses.big.${u}`;
                    case a.h2.S128x100:
                    case a.h2.S180x135:
                      return `R.images.gui.maps.shop.vehicles.c_180x135.${u}`;
                    case a.h2.S232x174:
                    case a.h2.S296x222:
                      return `R.images.gui.maps.shop.vehicles.c_360x270.${u}`;
                    case a.h2.S400x300:
                    case a.h2.S600x450:
                      return `R.images.gui.maps.shop.vehicles.c_600x450.${u}`;
                    default:
                      return (
                        console.error("Unknown vehicle image size", t, e.vehicleName),
                        "R.images.gui.maps.icons.quests.bonuses.big.vehicles"
                      );
                  }
                if (e.name === a.E4.TmanToken)
                  switch (t) {
                    case a.h2.Mini:
                    case a.h2.Small:
                    case a.h2.S48x48:
                    case a.h2.Big:
                    case a.h2.S80x80:
                      return `R.images.gui.maps.icons.tankmen.icons.s80x80.${e.icon}`;
                    case a.h2.S128x100:
                    case a.h2.S180x135:
                    case a.h2.S232x174:
                      return `R.images.gui.maps.icons.tankmen.icons.s232x174.${e.icon}`;
                    case a.h2.S296x222:
                      return `R.images.gui.maps.icons.tankmen.icons.s296x222.${e.icon}`;
                    case a.h2.S400x300:
                      return `R.images.gui.maps.icons.tankmen.icons.s400x300.${e.icon}`;
                    case a.h2.S600x450:
                      return `R.images.gui.maps.icons.tankmen.icons.s600x450.${e.icon}`;
                    default:
                      return (
                        console.error("Unknown image size", t),
                        "R.images.gui.maps.icons.tankmen.icons.s600x450.tankman"
                      );
                  }
                if (e.name === a.E4.CollectionItem)
                  switch (t) {
                    case a.h2.Mini:
                    case a.h2.Small:
                    case a.h2.S48x48:
                      return `R.images.gui.maps.icons.collectionItems.c_48x48.${e.icon}`;
                    case a.h2.Big:
                    case a.h2.S80x80:
                      return `R.images.gui.maps.icons.collectionItems.c_80x80.${e.icon}`;
                    case a.h2.S128x100:
                    case a.h2.S180x135:
                    case a.h2.S232x174:
                      return `R.images.gui.maps.icons.collectionItems.c_232x174.${e.icon}`;
                    case a.h2.S296x222:
                      return `R.images.gui.maps.icons.collectionItems.c_296x222.${e.icon}`;
                    case a.h2.S400x300:
                      return `R.images.gui.maps.icons.collectionItems.c_400x300.${e.icon}`;
                    case a.h2.S600x450:
                      return `R.images.gui.maps.icons.collectionItems.c_600x450.${e.icon}`;
                    default:
                      console.error("Unknown image size", t);
                  }
                if (e.name === a.E4.StyleProgress)
                  switch (t) {
                    case a.h2.Small:
                    case a.h2.Big:
                      return `R.images.gui.maps.icons.quests.bonuses.${t}.progressionStyle`;
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${t}.${e.icon}`;
                  }
                if (o.includes(e.name))
                  switch (e.name) {
                    case "branch":
                    case "vehicleSelect":
                    case "paragonsUnlocks":
                      return `R.images.gui.maps.icons.paragons.allRewards.${t}.${e.icon}`;
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${t}.${e.icon}`;
                  }
                return (0, n.ry)(e, t);
              })(e, t),
            value: e.value,
            valueType: (0, n.p3)(e.name),
            label: e.label,
            tooltipArgs: (0, n.pI)(
              { tooltipId: e.tooltipId, entitlementID: e.value, level: t, chapterID: u },
              Number(e.tooltipContentId),
            ),
            type: e.type,
            vehicleNation: e.nationTag,
            vehicleLvl: e.level,
            vehicleName: e.vehicleName,
            vehicleCD: e.vehicleCD,
            isElite: e.isElite,
            isRent: e.isRent,
            rentBattles: e.rentBattles,
            rentDays: e.rentDays,
            isCompensation: e.isCompensation,
            compensatedBonus: e.compensatedBonus,
            icon: e.icon,
            styleID: e.styleID,
            banchID: e.branchID,
            styleProgressLevel: e.progressLevel,
          }),
          c = (e, t) => (t < 0 ? 0 : e[t].maxPoints),
          m = (e, t, u) => {
            let a = 0;
            const n = c(u, t - 2),
              r = c(u, u.length - 1) / u.length;
            return (
              u.forEach((u, s) => {
                s < t &&
                  (a += ((e, t, u, a) => (e >= t ? a : (a / (t - u)) * (e - u)))(
                    e,
                    u.maxPoints,
                    n,
                    r,
                  ));
              }),
              a
            );
          },
          d = (e) => {
            const t = new Date(e * r.s_);
            return {
              day: t.getDate(),
              month: t.getMonth(),
              years: t.getFullYear(),
              hours: (0, r.U9)(t.getHours()),
              min: (0, r.U9)(t.getMinutes()),
            };
          },
          E = (e) => e > Date.now() / r.s_,
          _ = (e) => {
            const t = (0, r.f8)(e - Date.now() / r.s_);
            return t.days
              ? i.shortTimeText()
              : (({ hours: e, minutes: t }) =>
                  e > 0 || t === r.oG - 1
                    ? t === r.oG - 1
                      ? (0, s.uF)(i.hour(), { hours: e + 1 })
                      : (0, s.uF)(i.hours(), { hours: e, minutes: t + 1 })
                    : t > 0
                      ? (0, s.uF)(i.minutes(), { minutes: t + 1 })
                      : i.lessOneMin())(t);
          };
      },
      5026: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => a });
        const a = {
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
      5287: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => a });
        const a = { base: "FormatText_base_d0" };
      },
      3393: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => a });
        const a = {
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
    var t = __webpack_module_cache__[e];
    if (void 0 !== t) return t.exports;
    var u = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](u, u.exports, __webpack_require__), u.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, u, a) => {
      if (!t) {
        var n = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, u, a] = deferred[i], r = !0, s = 0; s < t.length; s++)
            (!1 & a || n >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[s]))
              ? t.splice(s--, 1)
              : ((r = !1), a < n && (n = a));
          if (r) {
            deferred.splice(i--, 1);
            var o = u();
            void 0 !== o && (e = o);
          }
        }
        return e;
      }
      a = a || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > a; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, u, a];
    }),
    (__webpack_require__.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(t, { a: t }), t);
    }),
    (__webpack_require__.d = (e, t) => {
      for (var u in t)
        __webpack_require__.o(t, u) &&
          !__webpack_require__.o(e, u) &&
          Object.defineProperty(e, u, { enumerable: !0, get: t[u] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t)),
    (__webpack_require__.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (__webpack_require__.j = 314),
    (() => {
      var e = { 314: 0, 965: 0, 921: 0, 731: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var a,
            n,
            [r, s, o] = u,
            i = 0;
          if (r.some((t) => 0 !== e[t])) {
            for (a in s) __webpack_require__.o(s, a) && (__webpack_require__.m[a] = s[a]);
            if (o) var l = o(__webpack_require__);
          }
          for (t && t(u); i < r.length; i++)
            ((n = r[i]), __webpack_require__.o(e, n) && e[n] && e[n][0](), (e[n] = 0));
          return __webpack_require__.O(l);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [454], () => __webpack_require__(1630));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
