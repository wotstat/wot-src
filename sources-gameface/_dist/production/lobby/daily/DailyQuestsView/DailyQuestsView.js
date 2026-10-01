(() => {
  var __webpack_modules__ = {
      3779: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => g });
        var a = t(6483),
          r = t.n(a),
          n = t(9887),
          s = t.n(n),
          i = t(3377),
          o = t(6179),
          l = t.n(o),
          c = t(5026);
        const d = [
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
        function m() {
          return (
            (m =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            m.apply(this, arguments)
          );
        }
        Object.keys(s());
        const _ = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          E = (Object.keys(_), ["mt", "mr", "mb", "ml"]),
          A = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          g = (0, i.ZP)((e) => {
            let u = e.className,
              t = e.width,
              a = e.height,
              n = e.m,
              s = e.mt,
              i = void 0 === s ? n : s,
              g = e.mr,
              D = void 0 === g ? n : g,
              p = e.mb,
              F = void 0 === p ? n : p,
              B = e.ml,
              C = void 0 === B ? n : B,
              b = e.column,
              f = e.row,
              h = e.flexDirection,
              v = void 0 === h ? (b ? "column" : f && "row") || void 0 : h,
              w = e.flexStart,
              y = e.center,
              S = e.flexEnd,
              R = e.spaceBetween,
              P = e.spaceAround,
              x = e.justifyContent,
              N =
                void 0 === x
                  ? (w ? "flex-start" : y && "center") ||
                    (S && "flex-end") ||
                    (R && "space-between") ||
                    (P && "space-around") ||
                    void 0
                  : x,
              T = e.alignItems,
              M =
                void 0 === T
                  ? (w ? "flex-start" : y && "center") || (S && "flex-end") || void 0
                  : T,
              L = e.alignSelf,
              k = e.wrap,
              O = e.flexWrap,
              I = void 0 === O ? (k ? "wrap" : void 0) : O,
              H = e.grow,
              Q = e.shrink,
              U = e.flex,
              G = void 0 === U ? (H || Q ? `${H ? 1 : 0} ${Q ? 1 : 0} auto` : void 0) : U,
              W = e.style,
              $ = e.children,
              j = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, d);
            const q = (0, o.useMemo)(() => {
                const e = { mt: i, mr: D, mb: F, ml: C },
                  u = ((e) =>
                    E.reduce((u, t) => {
                      const a = e[t];
                      return a && "number" != typeof a ? u.concat(_[!0 === a ? "MD" : a][t]) : u;
                    }, []))(e),
                  r = ((e) =>
                    E.reduce((u, t) => {
                      const a = e[t];
                      return ("number" == typeof a && (u[A[t]] = a + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, W, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    flex: G,
                    alignSelf: L,
                    display: v || M ? "flex" : void 0,
                    flexDirection: v,
                    flexWrap: I,
                    justifyContent: N,
                    alignItems: M,
                  }),
                  computedClassNames: u,
                };
              }, [t, a, i, D, F, C, W, G, L, v, I, N, M]),
              z = q.computedStyle,
              Z = q.computedClassNames;
            return l().createElement(
              "div",
              m({ className: r()(c.Z.base, ...Z, u), style: z }, j),
              $,
            );
          });
      },
      2372: (e, u, t) => {
        "use strict";
        t.d(u, { A: () => s });
        var a = t(6179),
          r = t.n(a),
          n = t(4179);
        class s extends r().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = n.B3.GOLD;
            else e = n.B3.INTEGRAL;
            const u = n.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        s.defaultProps = { format: "integral" };
      },
      280: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => l });
        var a = t(6179),
          r = t.n(a),
          n = t(6483),
          s = t.n(n),
          i = t(3649),
          o = t(5287);
        const l = ({ binding: e, text: u = "", classMix: t, alignment: n = i.v2.left }) =>
          null === u
            ? (console.error("FormatText was supplied with 'null'"), null)
            : r().createElement(
                a.Fragment,
                null,
                u.split("\n").map((u, l) =>
                  r().createElement(
                    "div",
                    { className: s()(o.Z.base, t), key: `${u}-${l}` },
                    (0, i.Uw)(u, n, e).map((e, u) =>
                      r().createElement(a.Fragment, { key: `${u}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, u, t) => {
        "use strict";
        t.d(u, { Y: () => d });
        var a = t(3138),
          r = t(6179),
          n = t(1043),
          s = t(5262);
        const i = a.O.client.getSize("rem"),
          o = i.width,
          l = i.height,
          c = Object.assign({ width: o, height: l }, (0, s.T)(o, l, n.j)),
          d = (0, r.createContext)(c);
      },
      1039: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => c });
        var a = t(6179),
          r = t.n(a),
          n = t(6536),
          s = t(3495),
          i = t(1043),
          o = t(5262),
          l = t(3138);
        const c = (0, a.memo)(({ children: e }) => {
          const u = (0, a.useContext)(s.Y),
            t = (0, a.useState)(u),
            c = t[0],
            d = t[1],
            m = (0, a.useCallback)((e, u) => {
              const t = l.O.view.pxToRem(e),
                a = l.O.view.pxToRem(u);
              d(Object.assign({ width: t, height: a }, (0, o.T)(t, a, i.j)));
            }, []);
          ((0, n.Z)(() => {
            engine.on("clientResized", m);
          }),
            (0, a.useEffect)(() => () => engine.off("clientResized", m), [m]));
          const _ = (0, a.useMemo)(() => Object.assign({}, c), [c]);
          return r().createElement(s.Y.Provider, { value: _ }, e);
        });
      },
      6010: (e, u, t) => {
        "use strict";
        var a = t(6179),
          r = t(7382),
          n = t(3495);
        const s = ["children"];
        const i = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, s);
          const i = (0, a.useContext)(n.Y),
            o = i.extraLarge,
            l = i.large,
            c = i.medium,
            d = i.small,
            m = i.extraSmall,
            _ = i.extraLargeWidth,
            E = i.largeWidth,
            A = i.mediumWidth,
            g = i.smallWidth,
            D = i.extraSmallWidth,
            p = i.extraLargeHeight,
            F = i.largeHeight,
            B = i.mediumHeight,
            C = i.smallHeight,
            b = i.extraSmallHeight,
            f = { extraLarge: p, large: F, medium: B, small: C, extraSmall: b };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && o) return u;
            if (t.large && l) return u;
            if (t.medium && c) return u;
            if (t.small && d) return u;
            if (t.extraSmall && m) return u;
          } else {
            if (t.extraLargeWidth && _) return (0, r.H)(u, t, f);
            if (t.largeWidth && E) return (0, r.H)(u, t, f);
            if (t.mediumWidth && A) return (0, r.H)(u, t, f);
            if (t.smallWidth && g) return (0, r.H)(u, t, f);
            if (t.extraSmallWidth && D) return (0, r.H)(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && p) return u;
              if (t.largeHeight && F) return u;
              if (t.mediumHeight && B) return u;
              if (t.smallHeight && C) return u;
              if (t.extraSmallHeight && b) return u;
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
        (0, a.memo)(i);
      },
      7382: (e, u, t) => {
        "use strict";
        t.d(u, { H: () => a });
        const a = (e, u, t) =>
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
        t.d(u, { YN: () => r.Y, ZN: () => a.Z });
        t(6010);
        var a = t(1039),
          r = t(3495);
      },
      1043: (e, u, t) => {
        "use strict";
        t.d(u, { j: () => a });
        const a = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, u, t) => {
        "use strict";
        var a;
        function r(e, u, t) {
          const a = (function (e, u) {
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
            r = (function (e, u) {
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
            n = Math.min(a, r);
          return {
            extraLarge: n === t.extraLarge.weight,
            large: n === t.large.weight,
            medium: n === t.medium.weight,
            small: n === t.small.weight,
            extraSmall: n === t.extraSmall.weight,
            extraLargeWidth: a === t.extraLarge.weight,
            largeWidth: a === t.large.weight,
            mediumWidth: a === t.medium.weight,
            smallWidth: a === t.small.weight,
            extraSmallWidth: a === t.extraSmall.weight,
            extraLargeHeight: r === t.extraLarge.weight,
            largeHeight: r === t.large.weight,
            mediumHeight: r === t.medium.weight,
            smallHeight: r === t.small.weight,
            extraSmallHeight: r === t.extraSmall.weight,
          };
        }
        (t.d(u, { T: () => r }),
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
      5739: (e, u, t) => {
        "use strict";
        t.d(u, { Q: () => d });
        var a = t(6483),
          r = t.n(a),
          n = t(6179),
          s = t.n(n),
          i = t(3415),
          o = t(2862),
          l = t(729),
          c = t(1609);
        const d = ({
          name: e,
          image: u,
          isPeriodic: t = !1,
          size: a = o.h2.Big,
          special: n,
          value: d,
          valueType: m,
          style: _,
          className: E,
          classNames: A,
          tooltipArgs: g,
          periodicIconTooltipArgs: D,
        }) => {
          const p = (0, l.L_)(n),
            F = (0, l.i2)(n),
            B = (0, l.m9)(d, m);
          return s().createElement(
            "div",
            { className: r()(c.Z.base, c.Z[`base__${a}`], E), style: _ },
            s().createElement(
              i.l,
              { tooltipArgs: g, className: c.Z.tooltipWrapper },
              s().createElement(
                s().Fragment,
                null,
                s().createElement(
                  "div",
                  { className: r()(c.Z.image, null == A ? void 0 : A.image) },
                  p &&
                    s().createElement("div", {
                      className: r()(c.Z.highlight, null == A ? void 0 : A.highlight),
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${p}_highlight)`,
                      },
                    }),
                  u &&
                    s().createElement("div", {
                      className: r()(c.Z.icon, null == A ? void 0 : A.rewardIcon),
                      style: { backgroundImage: `url(${u})` },
                    }),
                  F &&
                    s().createElement("div", {
                      className: r()(c.Z.overlay, null == A ? void 0 : A.overlay),
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${F}_overlay)`,
                      },
                    }),
                ),
                B &&
                  s().createElement(
                    "div",
                    {
                      className: r()(
                        c.Z.info,
                        c.Z[`info__${e}`],
                        m === o.$h.MULTI && c.Z.info__multi,
                        null == A ? void 0 : A.info,
                      ),
                    },
                    B,
                  ),
              ),
            ),
            t &&
              s().createElement(
                i.l,
                { tooltipArgs: D },
                s().createElement("div", {
                  className: r()(c.Z.timer, null == A ? void 0 : A.periodicIcon),
                }),
              ),
          );
        };
      },
      2862: (e, u, t) => {
        "use strict";
        let a, r, n, s, i, o, l, c, d;
        (t.d(u, {
          $h: () => s,
          A2: () => o,
          E4: () => a,
          h2: () => n,
          kK: () => i,
          sh: () => l,
          ye: () => d,
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
              (e.PortalEventDiscount25 = "portalEventDiscountToken"),
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
              (e.RazlomCoin = "razlom_coin"));
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
          })(r || (r = {})),
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
          })(n || (n = {})),
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
          })(d || (d = {})));
      },
      729: (e, u, t) => {
        "use strict";
        t.d(u, { L_: () => D, i2: () => p, m9: () => F, p3: () => m, pI: () => g, ry: () => A });
        var a = t(2372),
          r = t(6179),
          n = t.n(r),
          s = t(2862);
        const i = [
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
          o = [s.E4.Gold, s.E4.Credits, s.E4.Crystal, s.E4.FreeXp],
          l = [s.E4.BattlePassPoints],
          c = [s.E4.PremiumPlus, s.E4.Premium];
        let d;
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
        })(d || (d = {}));
        const m = (e) =>
            i.includes(e)
              ? s.$h.MULTI
              : o.includes(e)
                ? s.$h.CURRENCY
                : l.includes(e)
                  ? s.$h.NUMBER
                  : c.includes(e)
                    ? s.$h.PREMIUM_PLUS
                    : s.$h.STRING,
          _ = ["engravings", "backgrounds"],
          E = ["engraving", "background"],
          A = (e, u = s.h2.Small) => {
            const t = e.name,
              a = e.type,
              r = e.value,
              n = e.icon,
              i = e.item,
              o = e.dogTagType,
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
              })(u);
            switch (t) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${a}_${r}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${r}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${r}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${i}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${n}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case s.h2.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case s.h2.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${n}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const a = _[e];
                  if (a) {
                    const r = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(a),
                      n = r.$dyn(t);
                    return n ? `${n}` : `${r.$dyn(E[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, u, n);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${l}.${n}`;
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
                })(u)}.${n}`;
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
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${l}.${n}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case s.h2.Mini:
                      return d.s32;
                    case s.h2.Small:
                    case s.h2.S48x48:
                      return d.s48;
                    case s.h2.S80x80:
                    case s.h2.Big:
                      return d.s80;
                    case s.h2.S128x100:
                      return d.s116;
                    case s.h2.S180x135:
                    case s.h2.S232x174:
                    case s.h2.S296x222:
                      return d.s296;
                    case s.h2.S400x300:
                      return d.s400;
                    case s.h2.S600x450:
                      return d.s600;
                  }
                })(u)}`;
              case s.E4.StyleProgress:
              case s.E4.LbStyleProgress:
                return B(n, u, s.ye.ProgressionStyle);
              case "portal":
                return `R.images.gui.maps.icons.rewards.${u}.${i}`;
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}`;
            }
          },
          g = (e, u, t) => {
            const a = u && { contentId: u };
            return Object.assign(
              {
                args: e,
                isEnabled: Boolean((e && e.tooltipId) || u),
                ignoreMouseClick: !0,
                ignoreShowDelay: !u,
              },
              a,
              t,
            );
          },
          D = (e) => {
            if (void 0 === e) return null;
            switch (e) {
              case s.kK.BATTLE_BOOSTER:
              case s.kK.BATTLE_BOOSTER_REPLACE:
                return s.A2.BATTLE_BOOSTER;
            }
          },
          p = (e) => {
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
          F = (e, u) => {
            if (void 0 === e) return null;
            switch (u) {
              case s.$h.MULTI: {
                const u = Number(e);
                return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
              }
              case s.$h.CURRENCY:
              case s.$h.NUMBER:
                return n().createElement(a.A, { format: "integral", value: Number(e) });
              case s.$h.PREMIUM_PLUS: {
                const u = Number(e);
                return isNaN(u) ? e : null;
              }
              default:
                return e;
            }
          },
          B = (e, u, t) => {
            const a = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              r = a.$dyn(e);
            return String(null != r ? r : a.$dyn(t));
          };
      },
      7701: (e, u, t) => {
        "use strict";
        t.d(u, { Nm: () => a.Nm, c4: () => r });
        var a = t(9482);
        const r = (0, a.EO)({
          getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
          getContainerSize: (e) => e.scrollHeight,
          getWrapperSize: (e) => e.offsetHeight,
          setScrollPosition: (e, u) => {
            e.scrollTop = u.value.scrollPosition;
          },
          getDirection: (e) => (e.deltaY > 1 ? a.Nm.Next : a.Nm.Prev),
        });
      },
      9482: (e, u, t) => {
        "use strict";
        t.d(u, { Nm: () => m, EO: () => E, he: () => _ });
        var a = t(7515),
          r = t(1856),
          n = t(3138),
          s = t(6179);
        function i(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return o(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return o(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var a = 0;
            return function () {
              return a >= e.length ? { done: !0 } : { done: !1, value: e[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function o(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, a = new Array(u); t < u; t++) a[t] = e[t];
          return a;
        }
        var l = t(3815);
        function c(e, u, t) {
          const a = (0, s.useMemo)(
            () =>
              (function (e, u, t, a) {
                let r,
                  n = !1,
                  s = 0;
                function i() {
                  r && clearTimeout(r);
                }
                function o(...o) {
                  const l = this,
                    c = Date.now() - s;
                  function d() {
                    ((s = Date.now()), t.apply(l, o));
                  }
                  n ||
                    (a && !r && d(),
                    i(),
                    void 0 === a && c > e
                      ? d()
                      : !0 !== u &&
                        (r = setTimeout(
                          a
                            ? function () {
                                r = void 0;
                              }
                            : d,
                          void 0 === a ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((a = t), (t = u), (u = void 0)),
                  (o.cancel = function () {
                    (i(), (n = !0));
                  }),
                  o
                );
              })(t, e),
            u,
          );
          return ((0, s.useEffect)(() => a.cancel, [a]), a);
        }
        var d = t(7030);
        let m;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(m || (m = {}));
        const _ = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          E = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: o,
            getWrapperSize: m,
            triggerMouseMoveOnUpdate: E = !1,
          }) => {
            const A = (e, t) => {
              const r = u(e),
                n = r[0],
                s = r[1];
              return (0, a.u)(n, s, t);
            };
            return (a = {}) => {
              const g = a.settings,
                D = void 0 === g ? _ : g,
                p = (0, s.useRef)(null),
                F = (0, s.useRef)(null),
                B = (() => {
                  const e = (0, s.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    a = (e, t) => {
                      u(e).delete(t);
                    },
                    r = (e, ...t) => {
                      for (var a, r = i(u(e).values()); !(a = r()).done;) (0, a.value)(...t);
                    };
                  return (0, s.useMemo)(() => ({ on: t, off: a, trigger: r }), []);
                })(),
                C = c(
                  () => {
                    n.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                b = (0, d.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = p.current;
                    u && (t(u, e), B.trigger("change", e), E && C());
                  },
                  onRest: (e) => B.trigger("rest", e),
                  onStart: (e) => B.trigger("start", e),
                  onPause: (e) => B.trigger("pause", e),
                })),
                f = b[0],
                h = b[1],
                v = (0, s.useCallback)(
                  (e, u, t) => {
                    var a;
                    const r = f.scrollPosition.get(),
                      n = (null != (a = f.scrollPosition.goal) ? a : 0) - r;
                    return A(e, u * t + n + r);
                  },
                  [f.scrollPosition],
                ),
                w = (0, s.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const a = p.current;
                    a &&
                      h.start({
                        scrollPosition: A(a, e),
                        immediate: u,
                        reset: t,
                        config: D.animationConfig,
                        from: { scrollPosition: A(a, f.scrollPosition.get()) },
                      });
                  },
                  [h, D.animationConfig, f.scrollPosition],
                ),
                y = (0, s.useCallback)(
                  (e) => {
                    const u = p.current,
                      t = F.current;
                    if (!u || !t) return;
                    const a = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return m(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, D.step),
                      r = v(u, e, a);
                    w(r);
                  },
                  [w, v, D.step],
                ),
                S = (0, s.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && y(o(e)),
                      p.current && B.trigger("mouseWheel", e, f.scrollPosition, u(p.current)));
                  },
                  [f.scrollPosition, y, B],
                ),
                R = ((e, u = []) => {
                  const t = (0, s.useRef)(),
                    a = (0, s.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, s.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [a],
                    ),
                    a
                  );
                })(
                  () =>
                    (0, r.v)(() => {
                      const e = p.current;
                      e &&
                        (w(A(e, f.scrollPosition.goal), { immediate: !0 }),
                        B.trigger("resizeHandled"));
                    }),
                  [w, f.scrollPosition.goal],
                ),
                P = (0, l.z)(() => {
                  const e = p.current;
                  if (!e) return;
                  const u = A(e, f.scrollPosition.goal);
                  (u !== f.scrollPosition.goal && w(u, { immediate: !0 }),
                    B.trigger("recalculateContent"));
                });
              (0, s.useEffect)(
                () => (
                  window.addEventListener("resize", R),
                  () => {
                    window.removeEventListener("resize", R);
                  }
                ),
                [R],
              );
              const x = (0, s.useCallback)((e) => B.trigger("isThumbDraggingChanged", e), [B]);
              return (0, s.useMemo)(
                () => ({
                  getWrapperSize: () => (F.current ? m(F.current) : void 0),
                  getContainerSize: () => (p.current ? e(p.current) : void 0),
                  getBounds: () =>
                    p.current
                      ? u(p.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: D.step.clampedArrowStepTimeout,
                  clampPosition: A,
                  handleMouseWheel: S,
                  applyScroll: w,
                  applyStepTo: y,
                  contentRef: p,
                  wrapperRef: F,
                  scrollPosition: h,
                  animationScroll: f,
                  recalculateContent: P,
                  handleIsThumbDragging: x,
                  events: { on: B.on, off: B.off },
                }),
                [f.scrollPosition, w, y, x, B.off, B.on, P, S, h, D.step.clampedArrowStepTimeout],
              );
            };
          };
      },
      8899: (e, u, t) => {
        "use strict";
        t.d(u, { X: () => Y });
        var a = {};
        (t.r(a),
          t.d(a, {
            Area: () => x,
            Bar: () => S,
            DefaultScroll: () => P,
            Direction: () => E.Nm,
            defaultSettings: () => E.he,
            useHorizontalScrollApi: () => A,
          }));
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => X,
            Bar: () => q,
            Default: () => Z,
            useVerticalScrollApi: () => N.c4,
          }));
        var n = t(6483),
          s = t.n(n),
          i = t(1856),
          o = t(6179),
          l = t.n(o),
          c = t(7515),
          d = t(3815);
        function m(e, u, t = []) {
          const a = (0, o.useRef)(0),
            r = (0, o.useCallback)(() => window.clearInterval(a.current), t || []);
          (0, o.useEffect)(() => r, [r]);
          const n = (null != t ? t : []).concat([u]);
          return [
            (0, o.useCallback)((t) => {
              ((a.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, n),
            r,
          ];
        }
        var _ = t(7727),
          E = t(9482);
        const A = (0, E.EO)({
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
            getDirection: (e) => (e.deltaY > 1 ? E.Nm.Next : E.Nm.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          g = "HorizontalBar_base_49",
          D = "HorizontalBar_base__nonActive_82",
          p = "HorizontalBar_leftButton_5f",
          F = "HorizontalBar_rightButton_03",
          B = "HorizontalBar_track_0d",
          C = "HorizontalBar_thumb_fd",
          b = "HorizontalBar_rail_32",
          f = "disable",
          h = { pending: !1, offset: 0 },
          v = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          w = () => {},
          y = (e, u) => Math.max(20, e.offsetWidth * u),
          S = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = v, onDrag: a = w }) => {
              const r = (0, o.useRef)(null),
                n = (0, o.useRef)(null),
                A = (0, o.useRef)(null),
                S = (0, o.useRef)(null),
                R = (0, o.useRef)(null),
                P = e.stepTimeout || 100,
                x = (0, o.useState)(h),
                N = x[0],
                T = x[1],
                M = (0, o.useCallback)(
                  (e) => {
                    (T(e),
                      R.current &&
                        a({ type: e.pending ? "dragStart" : "dragEnd", thumb: R.current }));
                  },
                  [a],
                ),
                L = () => {
                  const u = S.current,
                    t = R.current,
                    a = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(a && u && t && r)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    i = Math.min(1, a / r),
                    o = (0, c.u)(0, 1, s / (r - a)),
                    l = (u.offsetWidth - y(u, i)) * o;
                  ((t.style.transform = `translateX(${0 | l}px)`),
                    ((e) => {
                      if (n.current && A.current && S.current && R.current) {
                        if (0 === e)
                          return (n.current.classList.add(f), void A.current.classList.remove(f));
                        if (
                          ((u = S.current),
                          (t = R.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (n.current.classList.remove(f), void A.current.classList.add(f));
                        var u, t;
                        (n.current.classList.remove(f), A.current.classList.remove(f));
                      }
                    })(l));
                },
                k = (0, d.z)(() => {
                  ((() => {
                    const u = R.current,
                      t = S.current,
                      a = e.getWrapperSize(),
                      n = e.getContainerSize();
                    if (!(n && u && a && t)) return;
                    const s = Math.min(1, a / n);
                    ((u.style.width = `${y(t, s)}px`),
                      (u.style.display = "flex"),
                      r.current &&
                        (1 === s ? r.current.classList.add(D) : r.current.classList.remove(D)));
                  })(),
                    L());
                });
              ((0, o.useEffect)(() => (0, i.v)(k)),
                (0, o.useEffect)(
                  () =>
                    (0, i.v)(() => {
                      const u = () => {
                        L();
                      };
                      let t = w;
                      const a = () => {
                        (t(), (t = (0, i.v)(k)));
                      };
                      return (
                        e.events.on("recalculateContent", k),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", a),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", k),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", a));
                        }
                      );
                    }),
                  [e],
                ),
                (0, o.useEffect)(() => {
                  if (!N.pending) return;
                  const u = (u) => {
                      var t;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const n = S.current,
                        s = R.current;
                      if (!r || !n || !s) return;
                      const i = u.screenX - N.offset - n.getBoundingClientRect().x,
                        o = (i / n.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, o),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        a({ type: "dragging", thumb: s, thumbOffset: i, contentOffset: o }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), M(h));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, N.offset, N.pending, a, M]));
              const O = m((u) => e.applyStepTo(u), P, [e]),
                I = O[0],
                H = O[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", H, !0),
                  () => document.removeEventListener("mouseup", H, !0)
                ),
                [H],
              );
              const Q = (e) => {
                e.target.classList.contains(f) || (0, _.G)("highlight");
              };
              return l().createElement(
                "div",
                { className: s()(g, u.base), ref: r, onWheel: e.handleMouseWheel },
                l().createElement("div", {
                  className: s()(p, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(f) ||
                      0 !== e.button ||
                      ((0, _.G)("play"), I(E.Nm.Next));
                  },
                  onMouseUp: H,
                  ref: n,
                  onMouseEnter: Q,
                }),
                l().createElement(
                  "div",
                  {
                    className: s()(B, u.track),
                    onMouseDown: (u) => {
                      const a = R.current;
                      if (a && 0 === u.button)
                        if (((0, _.G)("play"), u.target === a))
                          M({ pending: !0, offset: u.screenX - a.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const a = R.current,
                              r = e.contentRef.current;
                            if (!a || !r) return;
                            const n = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + n * u);
                          })(u.screenX > a.getBoundingClientRect().x ? E.Nm.Prev : E.Nm.Next);
                        }
                    },
                    ref: S,
                    onMouseEnter: Q,
                  },
                  l().createElement("div", { ref: R, className: s()(C, u.thumb) }),
                  l().createElement("div", { className: s()(b, u.rail) }),
                ),
                l().createElement("div", {
                  className: s()(F, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(f) ||
                      0 !== e.button ||
                      ((0, _.G)("play"), I(E.Nm.Prev));
                  },
                  onMouseUp: H,
                  ref: A,
                  onMouseEnter: Q,
                }),
              );
            },
          ),
          R = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          P = ({
            children: e,
            api: u,
            className: t,
            barClassNames: a,
            areaClassName: r,
            classNames: n,
            scrollClassName: i,
            getStepByRailClick: c,
            onDrag: d,
          }) => {
            const m = (0, o.useMemo)(() => {
                const e = a || {};
                return Object.assign({}, e, { base: s()(R.base, e.base) });
              }, [a]),
              _ = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return l().createElement(
              "div",
              { className: s()(R.defaultScroll, t), onWheel: u.handleMouseWheel },
              l().createElement(
                "div",
                { className: s()(R.defaultScrollArea, r) },
                l().createElement(x, { className: i, api: _, classNames: n }, e),
              ),
              l().createElement(S, { getStepByRailClick: c, api: u, onDrag: d, classNames: m }),
            );
          },
          x = ({ api: e, className: u, classNames: t, children: a, style: r }) => (
            (0, o.useEffect)(() => (0, i.v)(e.recalculateContent)),
            l().createElement(
              "div",
              { className: s()(R.base, u), style: r },
              l().createElement(
                "div",
                {
                  className: s()(R.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                l().createElement(
                  "div",
                  { className: s()(R.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  a,
                ),
              ),
            )
          );
        ((x.Bar = S),
          (x.Default = P),
          (x.SeniorityAwards = ({ api: e, className: u, classNames: t, children: a }) => (
            (0, o.useEffect)(() => (0, i.v)(e.recalculateContent)),
            l().createElement(
              "div",
              { className: s()(R.base, u) },
              l().createElement(
                "div",
                { className: s()(R.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                l().createElement(
                  "div",
                  { className: s()(R.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  a,
                ),
              ),
            )
          )));
        var N = t(7701);
        const T = "VerticalBar_base_f3",
          M = "VerticalBar_base__nonActive_42",
          L = "VerticalBar_topButton_d7",
          k = "VerticalBar_bottomButton_06",
          O = "VerticalBar_track_df",
          I = "VerticalBar_thumb_32",
          H = "VerticalBar_rail_43",
          Q = "disable",
          U = () => {},
          G = { pending: !1, offset: 0 },
          W = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          $ = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          j = (e, u) => Math.max(20, e.offsetHeight * u),
          q = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = W, onDrag: a = U }) => {
              const r = (0, o.useRef)(null),
                n = (0, o.useRef)(null),
                E = (0, o.useRef)(null),
                A = (0, o.useRef)(null),
                g = (0, o.useRef)(null),
                D = e.stepTimeout || 100,
                p = (0, o.useState)(G),
                F = p[0],
                B = p[1],
                C = (0, o.useCallback)(
                  (e) => {
                    (B(e),
                      g.current &&
                        a({ type: e.pending ? "dragStart" : "dragEnd", thumb: g.current }));
                  },
                  [a],
                ),
                b = (0, d.z)(() => {
                  const u = g.current,
                    t = A.current,
                    a = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(a && n && u && t)) return;
                  const s = Math.min(1, a / n);
                  return (
                    (u.style.height = `${j(t, s)}px`),
                    u.classList.add(I),
                    r.current &&
                      (1 === s ? r.current.classList.add(M) : r.current.classList.remove(M)),
                    s
                  );
                }),
                f = (0, d.z)(() => {
                  const u = A.current,
                    t = g.current,
                    a = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(a && u && t && r)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    i = Math.min(1, a / r),
                    o = (0, c.u)(0, 1, s / (r - a)),
                    l = (u.offsetHeight - j(u, i)) * o;
                  ((t.style.transform = `translateY(${0 | l}px)`),
                    ((e) => {
                      if (n.current && E.current && A.current && g.current) {
                        if (0 === e)
                          return (n.current.classList.add(Q), void E.current.classList.remove(Q));
                        if (
                          ((u = A.current),
                          (t = g.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (n.current.classList.remove(Q), void E.current.classList.add(Q));
                        var u, t;
                        (n.current.classList.remove(Q), E.current.classList.remove(Q));
                      }
                    })(l));
                }),
                h = (0, d.z)(() => {
                  $(e, () => {
                    (b(), f());
                  });
                });
              ((0, o.useEffect)(() => (0, i.v)(h)),
                (0, o.useEffect)(() => {
                  const u = () => {
                    $(e, () => {
                      f();
                    });
                  };
                  let t = U;
                  const a = () => {
                    (t(), (t = (0, i.v)(h)));
                  };
                  return (
                    e.events.on("recalculateContent", h),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", a),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", h),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", a));
                    }
                  );
                }, [e]),
                (0, o.useEffect)(() => {
                  if (!F.pending) return;
                  const u = (u) => {
                      $(e, (t) => {
                        const r = A.current,
                          n = g.current,
                          s = e.getContainerSize();
                        if (!r || !n || !s) return;
                        const i = u.screenY - F.offset - r.getBoundingClientRect().y,
                          o = (i / r.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, o),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          a({ type: "dragging", thumb: n, thumbOffset: i, contentOffset: o }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        C(G));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, F.offset, F.pending, a, C]));
              const v = m((u) => e.applyStepTo(u), D, [e]),
                w = v[0],
                y = v[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", y, !0),
                  () => document.removeEventListener("mouseup", y, !0)
                ),
                [y],
              );
              const S = (e) => {
                e.target.classList.contains(Q) || (0, _.G)("highlight");
              };
              return l().createElement(
                "div",
                { className: s()(T, u.base), ref: r, onWheel: e.handleMouseWheel },
                l().createElement("div", {
                  className: s()(L, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Q) ||
                      0 !== e.button ||
                      ((0, _.G)("play"), w(N.Nm.Next));
                  },
                  ref: n,
                  onMouseEnter: S,
                }),
                l().createElement(
                  "div",
                  {
                    className: s()(O, u.track),
                    onMouseDown: (u) => {
                      const a = g.current;
                      if (a && 0 === u.button)
                        if (((0, _.G)("play"), u.target === a))
                          (e.handleIsThumbDragging(!0),
                            C({ pending: !0, offset: u.screenY - a.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            g.current &&
                              $(e, (a) => {
                                if (!a) return;
                                const r = t(e),
                                  n = e.clampPosition(a, a.scrollTop + r * u);
                                e.applyScroll(n);
                              });
                          })(u.screenY > a.getBoundingClientRect().y ? N.Nm.Prev : N.Nm.Next);
                        }
                    },
                    ref: A,
                    onMouseEnter: S,
                  },
                  l().createElement("div", { ref: g, className: u.thumb }),
                  l().createElement("div", { className: s()(H, u.rail) }),
                ),
                l().createElement("div", {
                  className: s()(k, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Q) ||
                      0 !== e.button ||
                      ((0, _.G)("play"), w(N.Nm.Prev));
                  },
                  onMouseUp: y,
                  ref: E,
                  onMouseEnter: S,
                }),
              );
            },
          ),
          z = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Z = ({
            children: e,
            api: u,
            className: t,
            barClassNames: a,
            areaClassName: r,
            scrollClassName: n,
            scrollClassNames: i,
            getStepByRailClick: c,
            onDrag: d,
          }) => {
            const m = (0, o.useMemo)(() => {
                const e = a || {};
                return Object.assign({}, e, { base: s()(z.base, e.base) });
              }, [a]),
              _ = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return l().createElement(
              "div",
              { className: s()(z.defaultScroll, t), onWheel: u.handleMouseWheel },
              l().createElement(
                "div",
                { className: s()(z.area, r) },
                l().createElement(X, { className: n, classNames: i, api: _ }, e),
              ),
              l().createElement(q, { getStepByRailClick: c, api: u, onDrag: d, classNames: m }),
            );
          },
          X = ({ className: e, classNames: u, children: t, api: a }) => (
            (0, o.useEffect)(() => (0, i.v)(a.recalculateContent)),
            l().createElement(
              "div",
              { className: s()(z.base, e), ref: a.wrapperRef, onWheel: a.handleMouseWheel },
              l().createElement(
                "div",
                { className: s()(z.content, null == u ? void 0 : u.content), ref: a.contentRef },
                t,
              ),
            )
          );
        X.Default = Z;
        const Y = { Vertical: r, Horizontal: a };
      },
      7613: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => h });
        var a = t(6483),
          r = t.n(a),
          n = t(3779),
          s = t(280),
          i = t(3532),
          o = t.n(i),
          l = t(9887),
          c = t.n(l),
          d = t(3377),
          m = t(6179),
          _ = t.n(m),
          E = t(3393);
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
        function g() {
          return (
            (g =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            g.apply(this, arguments)
          );
        }
        Object.keys(c());
        const D = Object.keys(o()),
          p = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          F = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          B = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          C = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          b =
            (Object.keys(C),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": p,
              "heading-H36": p,
              "heading-H28": F,
              "heading-H24": F,
              "heading-H24R": F,
              "heading-H22": F,
              "heading-H20R": F,
              "heading-H18": F,
              "heading-H15": B,
              "heading-H14": B,
              "paragraph-P24": F,
              "paragraph-P18": F,
              "paragraph-P16": F,
              "paragraph-P14": B,
              "paragraph-P12": B,
              "paragraph-P10": B,
            }),
          f =
            (Object.keys(b),
            (e) =>
              e
                ? ((e) => D.includes(e))(e)
                  ? { colorClassName: E.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          h = (0, d.ZP)((e) => {
            let u = e.text,
              t = e.variant,
              a = e.className,
              i = e.color,
              o = e.m,
              l = e.mt,
              c = void 0 === l ? o : l,
              d = e.mr,
              D = void 0 === d ? o : d,
              p = e.mb,
              F = void 0 === p ? o : p,
              B = e.ml,
              C = void 0 === B ? o : B,
              h = e.style,
              v = e.format,
              w = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, A);
            const y = (0, m.useMemo)(() => {
                const e = f(i),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  a = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, h, a), colorClassName: u };
              }, [h, i]),
              S = y.computedStyle,
              R = y.colorClassName;
            return _().createElement(
              n.ZP,
              g(
                {
                  className: r()(E.Z.base, t && E.Z[t], R, a),
                  style: S,
                  mt: !0 === c ? b[t || "paragraph-P16"].mt : c,
                  mr: !0 === D ? b[t || "paragraph-P16"].mr : D,
                  mb: !0 === F ? b[t || "paragraph-P16"].mb : F,
                  ml: !0 === C ? b[t || "paragraph-P16"].ml : C,
                },
                w,
              ),
              void 0 !== v ? _().createElement(s.z, g({}, v, { text: u })) : u,
            );
          });
      },
      7078: (e, u, t) => {
        "use strict";
        t.d(u, { t: () => o });
        var a = t(6179),
          r = t.n(a),
          n = t(2056);
        const s = ["children"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
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
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, s);
          return r().createElement(
            n.u,
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
        var a = t(6179),
          r = t.n(a),
          n = t(7078),
          s = t(6373),
          i = t(2056);
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const l = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const a = r().createElement("div", { className: t }, e);
          if (u.header || u.body) return r().createElement(s.i, u, a);
          const l = u.contentId,
            c = u.args,
            d = null == c ? void 0 : c.contentId;
          return l || d
            ? r().createElement(i.u, o({}, u, { contentId: l || d }), a)
            : r().createElement(n.t, u, a);
        };
      },
      6373: (e, u, t) => {
        "use strict";
        t.d(u, { i: () => l });
        var a = t(2056),
          r = t(6179),
          n = t.n(r);
        const s = ["children", "body", "header", "note", "alert", "args"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
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
              d = e.alert,
              m = e.args,
              _ = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, s);
            const E = (0, r.useMemo)(() => {
              const e = Object.assign({}, m, { body: t, header: l, note: c, alert: d });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [d, t, l, c, m]);
            return n().createElement(
              a.u,
              i(
                {
                  contentId:
                    ((A = null == m ? void 0 : m.hasHtmlContent),
                    A ? o.SimpleTooltipHtmlContent("resId") : o.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: E,
                },
                _,
              ),
              u,
            );
            var A;
          };
      },
      2056: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => l });
        var a = t(7902),
          r = t(4179),
          n = t(6179);
        const s = [
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
        const o = (e, u, t = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: r.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: a,
                },
                t,
              ),
            );
          },
          l = (e) => {
            let u = e.children,
              t = e.contentId,
              r = e.args,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              d = e.onMouseDown,
              m = e.onClick,
              _ = e.ignoreShowDelay,
              E = void 0 !== _ && _,
              A = e.ignoreMouseClick,
              g = void 0 !== A && A,
              D = e.decoratorId,
              p = void 0 === D ? 0 : D,
              F = e.isEnabled,
              B = void 0 === F || F,
              C = e.targetId,
              b = void 0 === C ? 0 : C,
              f = e.onShow,
              h = e.onHide,
              v = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, s);
            const w = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              y = (0, n.useMemo)(() => b || (0, a.F)().resId, [b]),
              S = (0, n.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (o(t, p, { isMouseEvent: !0, on: !0, arguments: i(r) }, y),
                  f && f(),
                  (w.current.isVisible = !0));
              }, [t, p, r, y, f]),
              R = (0, n.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    o(t, p, { on: !1 }, y),
                    w.current.isVisible && h && h(),
                    (w.current.isVisible = !1));
                }
              }, [t, p, y, h]),
              P = (0, n.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(w.current.prevTarget) && R();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", P, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", P, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === B && R();
              }, [B, R]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", R),
                  () => {
                    (window.removeEventListener("mouseleave", R), R());
                  }
                ),
                [R],
              ));
            return B
              ? (0, n.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(S, E ? 100 : 400)),
                            l && l(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (R(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === g && R(), null == m || m(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === g && R(), null == d || d(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    v,
                  ),
                )
              : u;
            var x;
          };
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
      7515: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => a });
        const a = (e, u, t) => (t < e ? e : t > u ? u : t);
      },
      1856: (e, u, t) => {
        "use strict";
        t.d(u, { v: () => a });
        const a = (e) => {
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
      },
      122: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => a });
        const a = (e, u) => {
          let t;
          const a = setTimeout(() => {
            t = e();
          }, u);
          return () => {
            ("function" == typeof t && t(), clearTimeout(a));
          };
        };
      },
      8246: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => i });
        var a = t(3138);
        function r(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return n(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return n(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var a = 0;
            return function () {
              return a >= e.length ? { done: !0 } : { done: !1, value: e[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function n(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, a = new Array(u); t < u; t++) a[t] = e[t];
          return a;
        }
        const s = (e) => (0 === e ? window : window.subViews.get(e));
        function i({
          initializer: e = !0,
          rootId: u = 0,
          getRoot: t = s,
          context: n = "model",
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
            const a = t(u),
              r = n.split(".").reduce((e, u) => e[u], a);
            return "string" != typeof e || 0 === e.length
              ? r
              : e.split(".").reduce((e, u) => {
                  const t = e[u];
                  return "function" == typeof t ? t.bind(e) : t;
                }, r);
          };
          return {
            subscribe: (t, r) => {
              const s = "string" == typeof r ? `${n}.${r}` : n,
                o = a.O.view.addModelObserver(s, u, !0);
              return (i.set(o, t), e && t(l(r)), o);
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
              for (var e, t = r(i.keys()); !(e = t()).done;) {
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
        var a = t(4598),
          r = t(9174),
          n = t(6179),
          s = t.n(n),
          i = t(8246);
        const o = () => (e, u) => {
          const t = (0, n.createContext)({});
          return [
            function ({ mode: o = "real", options: l, children: c, mocks: d }) {
              const m = (0, n.useRef)([]),
                _ = (t, n, s) => {
                  var o;
                  const l = i.U(n),
                    c =
                      "real" === t
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (o = null == s ? void 0 : s.getter) ? o : () => {},
                          }),
                    d = (e) =>
                      "mocks" === t ? (null == s ? void 0 : s.getter(e)) : c.readByPath(e),
                    _ = (e) => m.current.push(e),
                    E = e({
                      mode: t,
                      readByPath: d,
                      externalModel: c,
                      observableModel: {
                        array: (e, u) => {
                          const n = null != u ? u : d(e),
                            s = r.LO.box(n, { equals: a.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, r.aD)((e) => s.set(e)),
                                e,
                              ),
                            s
                          );
                        },
                        object: (e, u) => {
                          const n = null != u ? u : d(e),
                            s = r.LO.box(n, { equals: a.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, r.aD)((e) => s.set(e)),
                                e,
                              ),
                            s
                          );
                        },
                        primitives: (e, u) => {
                          const a = d(u);
                          if (Array.isArray(e)) {
                            const n = e.reduce((e, u) => ((e[u] = r.LO.box(a[u], {})), e), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, r.aD)((u) => {
                                    e.forEach((e) => {
                                      n[e].set(u[e]);
                                    });
                                  }),
                                  u,
                                ),
                              n
                            );
                          }
                          {
                            const n = e,
                              s = Object.entries(n),
                              i = s.reduce((e, [u, t]) => ((e[t] = r.LO.box(a[u], {})), e), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, r.aD)((e) => {
                                    s.forEach(([u, t]) => {
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
                      cleanup: _,
                    }),
                    A = { mode: t, model: E, externalModel: c, cleanup: _ };
                  return {
                    model: E,
                    controls: "mocks" === t && s ? s.controls(A) : u(A),
                    externalModel: c,
                    mode: t,
                  };
                },
                E = (0, n.useRef)(!1),
                A = (0, n.useState)(o),
                g = A[0],
                D = A[1],
                p = (0, n.useState)(() => _(o, l, d)),
                F = p[0],
                B = p[1];
              return (
                (0, n.useEffect)(() => {
                  E.current ? B(_(g, l, d)) : (E.current = !0);
                }, [d, g, l]),
                (0, n.useEffect)(() => {
                  D(o);
                }, [o]),
                (0, n.useEffect)(
                  () => () => {
                    (F.externalModel.dispose(), m.current.forEach((e) => e()));
                  },
                  [F],
                ),
                s().createElement(t.Provider, { value: F }, c)
              );
            },
            () => (0, n.useContext)(t),
          ];
        };
      },
      7044: (e, u, t) => {
        "use strict";
        t.d(u, { f8: () => o, s_: () => r, wB: () => l, yR: () => n });
        var a = t(3649);
        (t(728), t(4179));
        const r = 1e3,
          n = 60,
          s = 60 * n,
          i = 24 * s;
        Date.now();
        function o(e = 0) {
          let u = e;
          const t = Math.trunc(u / i);
          u -= t * i;
          const a = Math.trunc(u / s);
          u -= a * s;
          const r = Math.trunc(u / n);
          return ((u -= r * n), { days: t, hours: a, minutes: r, seconds: u });
        }
        const l = (e, u = !0) =>
          e.days > 7 && u
            ? (0, a.WU)(R.strings.common.duration.days(), { days: e.days })
            : e.days >= 1
              ? 0 === e.hours
                ? (0, a.WU)(R.strings.common.duration.days(), { days: e.days })
                : `${(0, a.WU)(R.strings.common.duration.days(), { days: e.days })} ${(0, a.WU)(R.strings.common.duration.hours(), { hours: e.hours })}`
              : e.hours >= 1
                ? 0 === e.minutes
                  ? (0, a.WU)(R.strings.common.duration.hours(), { hours: e.hours })
                  : `${(0, a.WU)(R.strings.common.duration.hours(), { hours: e.hours })} ${(0, a.WU)(R.strings.common.duration.minutes(), { minutes: e.minutes })}`
                : (0, a.WU)(R.strings.common.duration.minutes(), { minutes: e.minutes || 1 });
      },
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => i, onResize: () => n }));
        var a = t(2472),
          r = t(1176);
        const n = (0, a.E)("clientResized"),
          s = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, r.R)(!1);
          }
          function t() {
            e.enabled && (0, r.R)(!0);
          }
          function a() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : (0, r.R)(!1);
          }
          const n = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let r = !0;
                  const n = `mouse${u}`,
                    i = s[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(n, o),
                    a(),
                    () => {
                      r &&
                        (i(), window.removeEventListener(n, o), (e.listeners -= 1), a(), (r = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, n, {
            disable() {
              ((e.enabled = !1), a());
            },
            enable() {
              ((e.enabled = !0), a());
            },
            enableOutside() {
              e.enabled && (0, r.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, r.R)(!1);
            },
          });
        })();
      },
      5959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => a,
            getMouseGlobalPosition: () => n,
            getSize: () => r,
            graphicsQuality: () => s,
          }));
        var a = t(527);
        function r(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function n(e = "px") {
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
      1176: (e, u, t) => {
        "use strict";
        function a(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => a });
      },
      2472: (e, u, t) => {
        "use strict";
        function a(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        t.d(u, { E: () => a });
      },
      3138: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => r });
        var a = t(5959);
        const r = { view: t(7641), client: a };
      },
      3722: (e, u, t) => {
        "use strict";
        function a(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function r(e, u, t) {
          return `url(${a(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => r, getTextureUrl: () => a }));
      },
      6112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => r });
        var a = t(2472);
        const r = {
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
      7641: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            addModelObserver: () => c,
            addPreloadTexture: () => i,
            children: () => a,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => n.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => h,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => v,
            getScale: () => g,
            getSize: () => m,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => C,
            isEventHandled: () => f,
            isFocused: () => B,
            pxToRem: () => D,
            remToPx: () => p,
            resize: () => _,
            sendEvent: () => s.qP,
            setAnimateWindow: () => F,
            setEventHandled: () => b,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => d,
            whenTutorialReady: () => S,
          }));
        var a = t(3722),
          r = t(6112),
          n = t(6538),
          s = t(8566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, u, t, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, a);
        }
        function c(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function d(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function m(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function _(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function E(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: p(u.x), y: p(u.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function g() {
          return viewEnv.getScale();
        }
        function D(e) {
          return viewEnv.pxToRem(e);
        }
        function p(e) {
          return viewEnv.remToPx(e);
        }
        function F(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function B() {
          return viewEnv.isFocused();
        }
        function C() {
          return viewEnv.isClientAccessible();
        }
        function b() {
          return viewEnv.setEventHandled();
        }
        function f() {
          return viewEnv.isEventHandled();
        }
        function h() {
          viewEnv.forceTriggerMouseMove();
        }
        function v() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(r.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === r.W[u]), e),
            {},
          ),
          y = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          S = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : n.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => l });
        const a = ["args"];
        const r = 2,
          n = 16,
          s = 32,
          i = 64,
          o = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                s = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    r = {},
                    n = Object.keys(e);
                  for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, a);
              return void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, s, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([e, u]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, s));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var r;
          },
          l = {
            close(e) {
              o("popover" === e ? r : s);
            },
            minimize() {
              o(i);
            },
            move(e) {
              o(n, { isMouseEvent: !0, on: e });
            },
          };
      },
      4598: (e, u, t) => {
        "use strict";
        function a() {}
        t.d(u, { ZT: () => a, jv: () => n, yR: () => r });
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
        t.d(u, { F: () => a });
        const a = (e = 1) => {
          const u = new Error().stack;
          let t,
            a = R.invalid("resId");
          return (
            u &&
              ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
              window.__feature &&
                window.__feature !== t &&
                window.subViews[t] &&
                (a = window.subViews[t].id)),
            { caller: t, stack: u, resId: a }
          );
        };
      },
      3377: (e, u, t) => {
        "use strict";
        t.d(u, { ZP: () => c });
        var a = t(5415),
          r = t(6179),
          n = t.n(r);
        const s = ["xl", "lg", "md", "sm", "xs"],
          i = (e) => e.includes("_") && ((e) => s.includes(e))(e.split("_").at(-1)),
          o = [a.cJ.ExtraLarge, a.cJ.Large, a.cJ.Medium, a.cJ.Small, a.cJ.ExtraSmall],
          l = (e, u) =>
            Object.keys(e).reduce((t, a) => {
              if (a in t) return t;
              if (i(a)) {
                const r = a.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const n = o.indexOf(u),
                  i = (-1 !== n ? s.slice(n) : [])
                    .map((e) => r + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  l = i ? e[i] : void 0;
                return ((t[r] = void 0 !== l ? l : e[r]), t);
              }
              const r = e[a];
              return (
                void 0 === r ||
                  ((e, u) => s.some((t) => void 0 !== u[`${e}_${t}`]))(a, e) ||
                  (t[a] = r),
                t
              );
            }, {}),
          c = (e, u = l) => {
            const t = (
              (e, u = l) =>
              (t) => {
                const s = (0, a.GS)().mediaSize,
                  i = (0, r.useMemo)(() => u(t, s), [t, s]);
                return n().createElement(e, i);
              }
            )(e, u);
            return n().memo((u) =>
              Object.keys(u).some((e) => i(e) && void 0 !== u[e])
                ? n().createElement(t, u)
                : n().createElement(e, u),
            );
          };
      },
      2344: (e, u, t) => {
        "use strict";
        t.d(u, { D9: () => s, au: () => i, tp: () => o });
        var a = t(2790),
          r = t(3469),
          n = t(2133);
        (t(579), t(5360), t(9056));
        const s = a.Z,
          i = r.Z,
          o = n.Z;
      },
      6536: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var a = t(6179);
        const r = (e) => {
          const u = (0, a.useRef)(!1);
          u.current || (e(), (u.current = !0));
        };
      },
      3469: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => s });
        var a = t(7044),
          r = t(6179);
        const n = () => {},
          s = (e = 0, u, t = 0, s = n) => {
            const i = (0, r.useState)(e),
              o = i[0],
              l = i[1];
            return (
              (0, r.useEffect)(() => {
                if (e > 0) {
                  l(e);
                  const r = Date.now(),
                    n = u || (e > 2 * a.yR ? a.yR : 1),
                    i = setInterval(() => {
                      const u = e - Math.floor((Date.now() - r) / a.s_);
                      null !== t && u <= t ? (l(t), s && s(), clearInterval(i)) : l(u);
                    }, n * a.s_);
                  return () => {
                    clearInterval(i);
                  };
                }
                l(0);
              }, [e, u, t, s]),
              o
            );
          };
      },
      2133: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        var a = t(122),
          r = t(6179);
        const n = (e, u) => {
          const t = (0, r.useState)(e),
            n = t[0],
            s = t[1];
          return ((0, r.useEffect)(() => (0, a.F)(() => s(e), u), [e, u]), n);
        };
      },
      3815: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => n });
        var a = t(6179);
        const r = [];
        function n(e) {
          const u = (0, a.useRef)(e);
          return (
            (0, a.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, a.useCallback)((...e) => (0, u.current)(...e), r)
          );
        }
      },
      5415: (e, u, t) => {
        "use strict";
        t.d(u, { Aq: () => o, GS: () => l, cJ: () => s, fd: () => i });
        var a = t(6179),
          r = t(7739),
          n = t(1043);
        let s, i, o;
        (!(function (e) {
          ((e[(e.ExtraSmall = n.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = n.j.small.width)] = "Small"),
            (e[(e.Medium = n.j.medium.width)] = "Medium"),
            (e[(e.Large = n.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = n.j.extraLarge.width)] = "ExtraLarge"));
        })(s || (s = {})),
          (function (e) {
            ((e[(e.ExtraSmall = n.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = n.j.small.width)] = "Small"),
              (e[(e.Medium = n.j.medium.width)] = "Medium"),
              (e[(e.Large = n.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = n.j.extraLarge.width)] = "ExtraLarge"));
          })(i || (i = {})),
          (function (e) {
            ((e[(e.ExtraSmall = n.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = n.j.small.height)] = "Small"),
              (e[(e.Medium = n.j.medium.height)] = "Medium"),
              (e[(e.Large = n.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = n.j.extraLarge.height)] = "ExtraLarge"));
          })(o || (o = {})));
        const l = () => {
          const e = (0, a.useContext)(r.YN),
            u = e.width,
            t = e.height,
            n = ((e) => {
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
            mediaSize: n,
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
        var a = t(4179);
        t(6179);
        a.Sw.instance;
        let r;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(r || (r = {}));
      },
      9056: (e, u, t) => {
        "use strict";
        var a = t(4179);
        t(6179);
        a.Sw.instance;
      },
      2790: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var a = t(6179);
        const r = (e) => {
          const u = (0, a.useRef)();
          return (
            (0, a.useEffect)(() => {
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
        let a, r;
        (t.d(u, { n: () => a }),
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
          })(r || (r = {})));
      },
      5175: (e, u, t) => {
        "use strict";
        t.d(u, { Q: () => s, c: () => n });
        var a = t(9480);
        const r = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? a.map(e, (e) => ("object" == typeof e ? r(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? r(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, u]) => [e, "object" == typeof u ? r(u) : u]),
                    )
              : e,
          n = (e) => r(e),
          s = (e) =>
            a.map(e || [], (e) => (null !== e && "object" == typeof e ? Object.assign({}, e) : e));
      },
      9480: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            contains: () => E,
            every: () => o,
            filter: () => c,
            filterMap: () => h,
            find: () => b,
            findIndex: () => w,
            findIndexLast: () => y,
            findLast: () => C,
            get: () => r,
            includes: () => f,
            join: () => S,
            lastElement: () => D,
            lastIndex: () => A,
            lastIndexZero: () => g,
            map: () => i,
            mapExists: () => v,
            pop: () => _,
            push: () => d,
            reduce: () => R,
            set: () => m,
            slice: () => p,
            some: () => l,
            splice: () => B,
            tail: () => F,
            unsafeGet: () => n,
            unwrapItem: () => s,
          }));
        var a = t(8968);
        function r(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        const n = r;
        function s(e) {
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
            : e.map((e, t, a) => u(null == e ? void 0 : e.value, t, a));
        }
        function o(e, u) {
          if (Array.isArray(e)) return e.every(u);
          for (let t = 0; t < e.length; t++) {
            if (!u(n(e, t), t, e)) return !1;
          }
          return !0;
        }
        function l(e, u) {
          if (Array.isArray(e)) return e.some(u);
          for (let t = 0; t < e.length; t++) {
            if (u(n(e, t), t, e)) return !0;
          }
          return !1;
        }
        function c(e, u) {
          if (Array.isArray(e)) return e.filter(u);
          const t = [];
          for (let r = 0; r < e.length; r++) {
            var a;
            const n = null == (a = e[r]) ? void 0 : a.value;
            u(n, r, e) && t.push(n);
          }
          return t;
        }
        function d(e, u) {
          if (Array.isArray(e)) return (e.push(u), e);
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function m(e, u, t) {
          if (Array.isArray(e)) return ((e[u] = t), e);
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function _(e, u = e.length - 1) {
          if (Array.isArray(e)) return e.splice(u, 1)[0];
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function E(e, u, t) {
          for (let a = 0; a < e.length; a++) {
            const r = n(e, a);
            if (t && t(r)) return !0;
            if (u === r) return !0;
          }
          return !1;
        }
        function A(e) {
          return e.length - 1;
        }
        function g(e) {
          return Math.max(0, e.length - 1);
        }
        function D(e) {
          if (0 !== e.length) return r(e, e.length - 1);
        }
        function p(e, u = 0, t = e.length - 1) {
          return {
            [Symbol.iterator]() {
              let a = Math.max(u, 0);
              const r = Math.min(t, g(e));
              return {
                next: function () {
                  if (a > r) return { done: !0, value: null };
                  const u = e[a++];
                  return u ? { value: s(u), done: !1 } : { done: !0, value: null };
                },
              };
            },
          };
        }
        function F(e, u) {
          return p(e, Math.max(0, e.length - 1 - u), A(e));
        }
        function B(e, u, t) {
          if (Array.isArray(e)) return e.splice(u, t);
          throw new Error("Mutate CoherentArrayProxy is not available");
        }
        function C(e, u) {
          for (let t = e.length - 1; t >= 0; t--) {
            const a = s(e[t]);
            if (u(a, t, e)) return a;
          }
        }
        function b(e, u) {
          for (let t = 0; t < e.length; t++) {
            const a = s(e[t]);
            if (u(a, t, e)) return a;
          }
        }
        function f(e, u) {
          for (let t = 0; t < e.length; t++) {
            if (n(e, t) === u) return !0;
          }
          return !1;
        }
        function h(e, u, t) {
          const a = [];
          for (let r = 0; r < e.length; r++) {
            const s = n(e, r);
            u(s, r, e) && a.push(t(s, r, e));
          }
          return a;
        }
        function v(e, u) {
          return h(e, a.C, u);
        }
        function w(e, u) {
          for (let t = 0; t < e.length; t++) {
            if (u(n(e, t), t, e)) return t;
          }
        }
        function y(e, u) {
          for (let t = e.length - 1; t >= 0; t--) {
            if (u(n(e, t), t, e)) return t;
          }
        }
        function S(e, u = ",") {
          let t = "";
          for (let a = 0; a < e.length; a++) {
            a > 0 && (t += u);
            const r = n(e, a);
            t += null == r ? "" : String(r);
          }
          return t;
        }
        function R(e, u, t) {
          if (Array.isArray(e)) return e.reduce(u, t);
          let a = t;
          for (let t = 0; t < e.length; t++) {
            a = u(a, n(e, t), t, e);
          }
          return a;
        }
      },
      8968: (e, u, t) => {
        "use strict";
        function a(e) {
          return (
            !1 ===
            (function (e) {
              return null == e;
            })(e)
          );
        }
        t.d(u, { C: () => a });
      },
      7727: (e, u, t) => {
        "use strict";
        function a(e) {
          engine.call("PlaySound", e);
        }
        t.d(u, { $: () => r, G: () => a });
        const r = {
          playHighlight() {
            a("highlight");
          },
          playClick() {
            a("play");
          },
          playYes() {
            a("yes1");
          },
        };
      },
      3649: (e, u, t) => {
        "use strict";
        let a;
        function r(e, u) {
          return e.replace(/\{\w+\}/g, (e) => String(u[e.slice(1, -1)]));
        }
        (t.d(u, { Uw: () => d, WU: () => r, v2: () => a }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(a || (a = {})));
        const n = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          s = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          i = (e, u, t = a.left) => e.split(u).reduce(t === a.left ? n : s, []),
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
          c = (e, u = a.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return l.includes(t)
              ? o(e)
              : ((e, u = a.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (i(n, /( )/, u).forEach((e) => (t = t.concat(i(e, r, a.left)))), t);
                })(e, u);
          },
          d = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : c(e, u)));
      },
      728: (e, u, t) => {
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
      1358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        var a = t(3138);
        class r {
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
            return (window.__dataTracker || (window.__dataTracker = new r()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const n = a.O.view.addModelObserver(e, t, r);
            return (
              n > 0
                ? ((this._callbacks[n] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(n) : (this._views[t] = [n])))
                : console.error("Can't add callback for model:", e),
              n
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
              const a = this._callbacks[t];
              void 0 !== a && a(e, u);
            });
          }
        }
        r.__instance = void 0;
        const n = r;
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
        t.d(u, { Sw: () => n.Z, B3: () => l, Z5: () => s, B0: () => o, ry: () => p });
        class a {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let a = e.target;
                  do {
                    if (a === u) return;
                    a = a.parentNode;
                  } while (a);
                  t();
                });
              }));
          }
          static get instance() {
            return (a.__instance || (a.__instance = new a()), a.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              a = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== a,
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
        const r = a;
        var n = t(1358);
        const s = {
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
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = t(5521),
          E = t(3138);
        const A = ["args"];
        function g(e, u, t, a, r, n, s) {
          try {
            var i = e[n](s),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(a, r);
        }
        const D = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          p = (function () {
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
                  return new Promise(function (a, r) {
                    var n = e.apply(u, t);
                    function s(e) {
                      g(n, a, r, s, i, "next", e);
                    }
                    function i(e) {
                      g(n, a, r, s, i, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          F = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                n = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    r = {},
                    n = Object.keys(e);
                  for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, A);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, n, {
                      arguments:
                        ((a = r),
                        Object.entries(a).map(([e, u]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, n));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var a;
          },
          B = () => F(o.CLOSE),
          C = (e, u) => {
            e.keyCode === _.n.ESCAPE && u();
          };
        var b = t(7572);
        const f = r.instance,
          h = {
            DataTracker: n.Z,
            ViewModel: b.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: m,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => F(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: B,
            sendClosePopOverEvent: () => F(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              F(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, a, r = R.invalid("resId"), n) => {
              const s = E.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                d = i.width,
                m = i.height,
                _ = {
                  x: E.O.view.pxToRem(l) + s.x,
                  y: E.O.view.pxToRem(c) + s.y,
                  width: E.O.view.pxToRem(d),
                  height: E.O.view.pxToRem(m),
                };
              F(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: a || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: D(_),
                on: !0,
                args: n,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => C(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              C(e, B);
            },
            handleViewEvent: F,
            onBindingsReady: p,
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
              for (const a in u)
                if (Object.prototype.hasOwnProperty.call(u, a)) {
                  const r = Object.prototype.toString.call(u[a]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = u[a];
                    t[a] = [];
                    for (let u = 0; u < r.length; u++) t[a].push({ value: e(r[u].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[a] = e(u[a]))
                      : (t[a] = u[a]);
                }
              return t;
            },
            ClickOutsideManager: f,
            SystemLocale: s,
            UserLocale: i,
          };
        window.ViewEnvHelper = h;
      },
      2603: (e, u, t) => {
        "use strict";
        t.d(u, { V: () => b });
        var a = t(6179),
          r = t.n(a),
          n = t(3099),
          s = t(3215),
          i = t(4598),
          o = t(9480),
          l = t(5175),
          c = t(3946);
        const d = (0, s.q)()(({ observableModel: e }) => {
            const u = { root: e.object(), quests: e.array("quests", []) },
              t = (0, c.Om)(() => Boolean(d() && d() === m())),
              a = (0, c.Om)(() => o.find(s(), (e) => e.status !== n.N.Done)),
              r = (0, c.Om)((e) =>
                e && e.postBattleCondition.items.length >= 1
                  ? o.map(e.postBattleCondition.items, i.yR)
                  : e && e.bonusCondition.items.length >= 1
                    ? o.map(e.bonusCondition.items, i.yR)
                    : void 0,
              ),
              s = (0, c.Om)(() => (0, l.c)(u.quests.get()), { equals: i.jv }),
              d = (0, c.Om)(() => s().length),
              m = (0, c.Om)(() => s().filter((e) => e.status === n.N.Done).length),
              _ = (0, c.Om)(() => {
                const e = a(),
                  u = r(e);
                return (u && u.length) > 0 ? u[0].descrData : void 0;
              });
            return Object.assign({}, u, {
              computes: {
                getCurrentQuest: a,
                getQuests: s,
                getQuestsLength: d,
                getCompletedlQuestLength: m,
                getAllQuestsCompleted: t,
                getConditionDescr: _,
              },
            });
          }, i.ZT),
          m = d[0],
          _ = d[1];
        var E = t(8515),
          A = t(9153),
          g = t(8975),
          D = t(122),
          p = t(3509);
        const F = R.strings.quests.premiumQuests.tab,
          B = R.strings.quests.dailyQuests.tab,
          C = (0, E.Pi)(({ isSelected: e, onClick: u }) => {
            const t = _().model,
              n = t.root.get(),
              s = n.isEnabled,
              i = n.hasPremiumAccount,
              o = n.unseenCount,
              l = t.computes.getAllQuestsCompleted(),
              c = t.computes.getCurrentQuest(),
              d = s ? F.label() : F.disabled.title(),
              m = ((e, u, t, a) =>
                e ? (u ? B.completed() : t ? a : F.disabled.noPrem()) : B.disabled.reason())(
                s,
                l,
                i,
                t.computes.getConditionDescr(),
              ),
              E = (0, a.useState)(m),
              C = E[0],
              b = E[1],
              f = (0, a.useState)(c && c.icon),
              h = f[0],
              v = f[1];
            return (
              (0, a.useEffect)(() => {
                if (i)
                  return (0, D.F)(() => {
                    (b(m), v(c && c.icon));
                  }, p.ji.unlockTabPremiumDuration);
                (b(m), v(c && c.icon));
              }, [i, m, c]),
              r().createElement(g.q, {
                tabIdx: A.g.PremiumQuests,
                isEnabled: s,
                isCompleted: l,
                isSelected: e,
                isPremium: !0,
                hasPremium: i,
                title: d,
                description: C,
                total: t.computes.getQuestsLength(),
                current: t.computes.getCompletedlQuestLength(),
                icon: h,
                bubbleCounter: o,
                onClick: u,
              })
            );
          }),
          b = (0, a.memo)(function (e) {
            const u = (0, a.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
            return r().createElement(m, { options: u }, r().createElement(C, e));
          });
      },
      648: (e, u, t) => {
        "use strict";
        t.d(u, { _: () => F });
        var a = t(6179),
          r = t.n(a),
          n = t(3099),
          s = t(3215),
          i = t(4598),
          o = t(9480),
          l = t(5175),
          c = t(3946);
        const d = (0, s.q)()(({ observableModel: e }) => {
            const u = { root: e.object(), quests: e.array("quests", []) },
              t = (0, c.Om)(() => Boolean(d() && d() === m())),
              a = (0, c.Om)(() => o.find(s(), (e) => e.status !== n.N.Done)),
              r = (0, c.Om)((e) =>
                e && e.postBattleCondition.items.length >= 1
                  ? o.map(e.postBattleCondition.items, i.yR)
                  : e && e.bonusCondition.items.length >= 1
                    ? o.map(e.bonusCondition.items, i.yR)
                    : void 0,
              ),
              s = (0, c.Om)(() => (0, l.c)(u.quests.get()), { equals: i.jv }),
              d = (0, c.Om)(() => s().length),
              m = (0, c.Om)(() => s().filter((e) => e.status === n.N.Done).length),
              _ = (0, c.Om)(() => {
                const e = a(),
                  u = r(e);
                return (u && u.length) > 0 ? u[0].descrData : void 0;
              });
            return Object.assign({}, u, {
              computes: {
                getCurrentQuest: a,
                getQuests: s,
                getQuestsLength: d,
                getCompletedlQuestLength: m,
                getAllQuestsCompleted: t,
                getConditionDescr: _,
              },
            });
          }, i.ZT),
          m = d[0],
          _ = d[1];
        var E = t(8515),
          A = t(8975),
          g = t(9153);
        const D = R.strings.quests.dailyQuests.tab,
          p = (0, E.Pi)(({ isSelected: e, onClick: u }) => {
            const t = _().model,
              a = t.root.get(),
              n = a.isEnabled,
              s = a.unseenCount,
              i = t.computes.getAllQuestsCompleted(),
              o = n ? D.label() : D.disabled.title(),
              l = ((e, u, t) => (e ? (u ? D.completed() : t) : D.disabled.reason()))(
                n,
                i,
                t.computes.getConditionDescr(),
              ),
              c = t.computes.getCurrentQuest();
            return r().createElement(A.q, {
              tabIdx: g.g.DailyQuests,
              isEnabled: n,
              isCompleted: i,
              isSelected: e,
              title: o,
              description: l,
              total: t.computes.getQuestsLength(),
              current: t.computes.getCompletedlQuestLength(),
              icon: c && c.icon,
              onClick: u,
              bubbleCounter: s,
            });
          }),
          F = (0, a.memo)(function (e) {
            const u = (0, a.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
            return r().createElement(m, { options: u }, r().createElement(p, e));
          });
      },
      8025: (e, u, t) => {
        "use strict";
        t.d(u, { Q: () => Ea });
        var a = t(6179),
          r = t.n(a),
          n = t(6483),
          s = t.n(n),
          i = t(7701),
          o = t(7613),
          l = t(6373),
          c = t(122),
          d = t(2344),
          m = t(7727),
          _ = t(8515);
        let E, A;
        (!(function (e) {
          ((e.Timer = "timer"),
            (e.Countdown = "countdown"),
            (e.Cooldown = "cooldown"),
            (e.None = "none"));
        })(E || (E = {})),
          (function (e) {
            ((e.Description = "description"),
              (e.Short = "short"),
              (e.Long = "long"),
              (e.Extended = "extended"));
          })(A || (A = {})));
        var g = t(7044),
          D = t(3138);
        var p = t(3649);
        const F = "Countdown_base_fe",
          B = "Countdown_icon_8b",
          C = "Countdown_description_8d";
        var b = t(280);
        const f = (e) => e.toString().padStart(2, "0"),
          h = R.images.gui.maps.icons.components.countdown,
          v = (e, u) => {
            const t = 2 === u ? h.big : h;
            switch (e) {
              case E.Timer:
                return t.clock();
              case E.Countdown:
                return t.hourglass();
              case E.Cooldown:
                return t.lock();
            }
          },
          w = (0, a.memo)(
            ({
              duration: e,
              icon: u = E.Timer,
              style: t = A.Description,
              onTimeReached: n,
              className: i = "",
              classNames: o = {},
              labelFormat: l = "",
            }) => {
              const c = t !== A.Description ? 1 : void 0,
                m = (0, d.au)(e, c),
                _ = (() => {
                  const e = (0, a.useState)(D.O.view.getScale()),
                    u = e[0],
                    t = e[1];
                  return (
                    (0, a.useEffect)(() => {
                      const e = () => {
                        t(D.O.view.getScale());
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
              n && n[m] && n[m]();
              const h = ((e, u) => {
                switch (u) {
                  case A.Description:
                    return (0, g.wB)(e);
                  case A.Short:
                    return `${f(e.minutes)}:${f(e.seconds)}`;
                  case A.Long:
                    return `${f(e.hours)}:${f(e.minutes)}:${f(e.seconds)}`;
                  case A.Extended:
                    return `${(0, p.WU)(R.strings.common.duration.days(), { days: e.days })} | ${f(e.hours)}:${f(e.minutes)}:${f(e.seconds)}`;
                }
              })((0, g.f8)(m), t);
              return r().createElement(
                "div",
                { className: s()(F, i) },
                u !== E.None &&
                  r().createElement("div", {
                    className: s()(B, o.icon),
                    style: { backgroundImage: `url('${v(u, _)}')` },
                  }),
                l
                  ? r().createElement(
                      "div",
                      { className: s()(C, o.text) },
                      r().createElement(b.z, { text: l, binding: { timerText: h } }),
                    )
                  : r().createElement("div", { className: s()(C, o.text) }, h),
              );
            },
          ),
          y = "DailyCountdown_base_75",
          S = "DailyCountdown_icon_2d",
          P = "DailyCountdown_countdownText_65",
          x = ({ timeToUpdate: e }) =>
            r().createElement(
              "div",
              { className: y },
              r().createElement(w, { duration: e, className: P, classNames: { icon: S } }),
            );
        var N = t(9922);
        const T = { type: "idle" };
        const M = {
          base: "ProgressBar_base_45",
          base__medium: "ProgressBar_base__medium_62",
          base__small: "ProgressBar_base__small_df",
          background: "ProgressBar_background_51",
          background__medium: "ProgressBar_background__medium_6e",
          background__small: "ProgressBar_background__small_46",
          lineWrapper: "ProgressBar_lineWrapper_6a",
        };
        let L, k;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(L || (L = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(k || (k = {})));
        const O = ({ size: e = L.Default, classMix: u }) =>
            r().createElement("div", { className: s()(M.background, M[`background__${e}`], u) }),
          I = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          H = ({ size: e }) => {
            const u = s()(I.base, I[`base__${e}`]);
            return r().createElement("div", { className: u });
          },
          Q = {
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
          U = (0, a.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: a,
              isComplete: n,
              withoutBounce: i,
            }) => {
              const o = s()(
                  Q.base,
                  Q[`base__${e}`],
                  t && Q.base__disabled,
                  n && Q.base__finished,
                  i && Q.base__withoutBounce,
                ),
                l = !t && !n;
              return r().createElement(
                "div",
                { className: o, style: a, ref: u },
                r().createElement("div", { className: Q.pattern }),
                r().createElement("div", { className: Q.gradient }),
                l && r().createElement(H, { size: e }),
              );
            },
          ),
          G = ({ size: e, value: u, lineRef: t, disabled: n, onComplete: s }) => {
            const i = (0, a.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              o = 100 === u;
            return (
              (0, a.useEffect)(() => {
                o && s && s();
              }, [o, s]),
              r().createElement(U, {
                size: e,
                disabled: n,
                baseStyles: i,
                isComplete: o,
                lineRef: t,
              })
            );
          };
        let W, $;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(W || (W = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })($ || ($ = {})));
        const j = "ProgressBarDeltaSimple_base_6c",
          q = "ProgressBarDeltaSimple_delta_99",
          z = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: n,
              size: s,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
            }) => {
              const d = i < n,
                m = (0, a.useState)($.Idle),
                _ = m[0],
                E = m[1],
                A = _ === $.In,
                g = _ === $.End,
                D = _ === $.Idle,
                p = (0, a.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                );
              ((0, a.useEffect)(() => {
                if (D && !t) {
                  const e = u;
                  return (0, c.F)(() => {
                    p($.In);
                  }, e);
                }
              }, [p, t, D, u]),
                (0, a.useEffect)(() => {
                  if (A) {
                    const t = e + u;
                    return (0, c.F)(() => {
                      (o && o(), p($.End));
                    }, t);
                  }
                }, [p, A, o, u, e]));
              const F = (0, a.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [d ? "left" : "right"]: "0",
                  }),
                  [d, u, e],
                ),
                B = (0, a.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [d ? "left" : "right"]: "0",
                  }),
                  [d, u, e],
                ),
                C = (0, a.useMemo)(
                  () => ({ width: `${Math.abs(n - i)}%`, left: `${d ? i : n}%` }),
                  [n, d, i],
                );
              return g
                ? null
                : r().createElement(
                    "div",
                    { className: j, style: C },
                    r().createElement(
                      "div",
                      { style: D ? F : B, className: q },
                      r().createElement(H, { size: s }),
                    ),
                  );
            },
          ),
          Z = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: n,
              disabled: s,
              isComplete: i,
              animationSettings: o,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const d = (0, a.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${o.line.duration}ms`,
                  transitionDelay: `${o.line.delay}ms`,
                }),
                [o.line.delay, o.line.duration, e],
              );
              return r().createElement(
                r().Fragment,
                null,
                r().createElement(U, {
                  size: u,
                  lineRef: n,
                  disabled: s,
                  isComplete: i,
                  baseStyles: d,
                }),
                t >= 0 &&
                  r().createElement(z, {
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
          X = "ProgressBarDeltaGrow_base_7e",
          Y = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          V = "ProgressBarDeltaGrow_glow_68",
          K = (e) => (e ? { left: 0 } : { right: 0 }),
          J = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          ee = (e) => ({ transitionDuration: `${e}ms` }),
          ue = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: n,
              size: i,
              to: o,
              onEndAnimation: l,
              onChangeAnimationState: d,
              className: m,
            }) => {
              const _ = o < n,
                E = (0, a.useState)(W.Idle),
                A = E[0],
                g = E[1],
                D = A === W.End,
                p = A === W.Idle,
                F = A === W.Grow,
                B = A === W.Shrink,
                C = (0, a.useCallback)(
                  (e) => {
                    (g(e), d && d(e));
                  },
                  [d],
                ),
                b = (0, a.useCallback)(
                  (e, u) =>
                    (0, c.F)(() => {
                      C(e);
                    }, u),
                  [C],
                );
              (0, a.useEffect)(() => {
                if (!t)
                  return p
                    ? b(W.Grow, u)
                    : F
                      ? b(W.Shrink, e)
                      : B
                        ? b(W.End, e)
                        : void (D && l && l());
              }, [b, t, D, F, p, B, l, u, e]);
              const f = (0, a.useMemo)(() => Object.assign({ width: "100%" }, ee(e), K(_)), [_, e]),
                h = (0, a.useMemo)(() => Object.assign({ width: "0%" }, ee(e), K(_)), [_, e]),
                v = (0, a.useMemo)(() => Object.assign({ width: "0%" }, J(_, n), ee(e)), [n, _, e]),
                w = (0, a.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - n)}%` }, J(_, n), ee(e)),
                  [n, _, o, e],
                );
              if (D) return null;
              const y = s()(X, m, _ && 0 === o && Y);
              return r().createElement(
                "div",
                { style: p ? v : w, className: y },
                r().createElement(
                  "div",
                  { style: B ? h : f, className: V },
                  r().createElement(H, { size: i }),
                ),
              );
            },
          ),
          te = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: n,
              disabled: s,
              isComplete: i,
              animationSettings: o,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const d = e < t,
                m = (0, a.useState)(!1),
                _ = m[0],
                E = m[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (e === W.Shrink && E(!0), c && c(e));
                  },
                  [c],
                ),
                g = (0, a.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                D = (0, a.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return r().createElement(
                r().Fragment,
                null,
                r().createElement(U, {
                  size: u,
                  lineRef: n,
                  disabled: s,
                  isComplete: i,
                  withoutBounce: d && 0 === e,
                  baseStyles: _ ? D : g,
                }),
                t >= 0 &&
                  r().createElement(ue, {
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
          ae = ["onComplete", "onEndAnimation"];
        function re() {
          return (
            (re =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            re.apply(this, arguments)
          );
        }
        const ne = (0, a.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, ae);
            const s = (0, a.useState)(!1),
              i = s[0],
              o = s[1],
              l = (0, a.useCallback)(() => {
                const e = 100 === n.to;
                (e !== i && o(e), e && u && u(), t && t());
              }, [i, u, t, n.to]);
            switch (n.animationSettings.type) {
              case k.Simple:
                return r().createElement(Z, re({}, n, { onEndAnimation: l, isComplete: i }));
              case k.Growing:
                return r().createElement(te, re({}, n, { onEndAnimation: l, isComplete: i }));
              default:
                return null;
            }
          }),
          se = ["onEndAnimation"];
        function ie() {
          return (
            (ie =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ie.apply(this, arguments)
          );
        }
        const oe = (0, a.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, se);
          const n = (0, a.useRef)({}),
            s = (0, a.useCallback)(() => {
              ((n.current.from = void 0), u && u());
            }, [u]),
            i = "number" == typeof n.current.from ? n.current.from : t.from;
          return (
            (n.current.from = i),
            r().createElement(ne, ie({}, t, { onEndAnimation: s, key: `${i}-${t.to}`, from: i }))
          );
        });
        function le() {
          return (
            (le =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            le.apply(this, arguments)
          );
        }
        const ce = (0, a.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: a,
              deltaFrom: n,
              animationSettings: s,
              onEndAnimation: i,
              onChangeAnimationState: o,
              onComplete: l,
            }) => {
              if (n === u)
                return r().createElement(G, {
                  key: `${n}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: a,
                  onComplete: l,
                });
              const c = {
                from: n,
                to: u,
                size: e,
                lineRef: t,
                disabled: a,
                animationSettings: s,
                onComplete: l,
                onEndAnimation: i,
                onChangeAnimationState: o,
              };
              return s.withStack
                ? r().createElement(oe, c)
                : r().createElement(ne, le({ key: `${n}-${u}` }, c));
            },
          ),
          de = (e) => ({
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
          });
        var me = t(7515);
        const _e = (e, u, t) => {
            if ("number" == typeof t) {
              return ((0, me.u)(0, u, t) / u) * 100;
            }
            return e;
          },
          Ee = {
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
          Ae = {
            freezed: !1,
            withStack: !1,
            type: k.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          ge = (0, a.memo)(
            ({
              maxValue: e = 100,
              theme: u = Ee,
              size: t = L.Default,
              animationSettings: n = Ae,
              disabled: i = !1,
              withoutBackground: o = !1,
              progressBarBackgroundClassMix: l,
              value: c,
              deltaFrom: d,
              lineRef: m,
              onChangeAnimationState: _,
              onEndAnimation: E,
              onComplete: A,
            }) => {
              const g = ((e, u, t) =>
                (0, a.useMemo)(() => {
                  const a = ((0, me.u)(0, u, e) / u) * 100;
                  return { value: a, deltaFrom: _e(a, u, t) };
                }, [t, u, e]))(c, e, d);
              return r().createElement(
                "div",
                { className: s()(M.base, M[`base__${t}`]), style: de(u) },
                !o && r().createElement(O, { size: t, classMix: l }),
                r().createElement(ce, {
                  size: t,
                  lineRef: m,
                  disabled: i,
                  value: g.value,
                  deltaFrom: g.deltaFrom,
                  animationSettings: n,
                  onEndAnimation: E,
                  onChangeAnimationState: _,
                  onComplete: A,
                }),
              );
            },
          );
        var De = t(5415);
        const pe = {
            [De.cJ.ExtraSmall]: {
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
            [De.cJ.Small]: {
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
            [De.cJ.Medium]: {
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
            [De.cJ.Large]: {
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
            [De.cJ.ExtraLarge]: {
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
          Fe = Ae.delta.delay + Ae.delta.duration + Ae.line.delay + Ae.line.duration,
          Be = 2e3,
          Ce = 500,
          be = 0,
          fe = 500,
          he = 300,
          ve = Be + Ce,
          we = 500,
          ye = 500,
          Se = 500;
        var Re = t(2862),
          Pe = t(3099),
          xe = t(3215),
          Ne = t(4598),
          Te = t(9480),
          Me = t(5175),
          Le = t(9174);
        var ke = t(3946),
          Oe = t(9153),
          Ie = t(3017),
          He = t(3509);
        const Qe = [Pe.N.Locked, Pe.N.Active],
          Ue = (e, u, t, a) => {
            const r = u ? pe[t].premiumBannerHeight : 0;
            let n = pe[t].questListMarginBottom + r;
            const s = pe[t].questCard.dailyHeight + pe[t].questCard.dailyMarginBottom,
              i = pe[t].questDividerHeight - pe[t].questCard.dailyMarginBottom;
            return e.map((u, r) => {
              if (!r) return n;
              if (u === Pe.N.Active) return (n += s);
              if (u === Pe.N.Locked) return (n += a ? s : s - pe[t].questCard.dailyMarginBottom);
              const o = e.find((e) => e === Pe.N.Locked),
                l = ((e, u) => {
                  const t = e[u - 1],
                    a = e[u - 2];
                  return (
                    (t === Pe.N.Done || t === Pe.N.UndoneSubscription) &&
                    a !== Pe.N.Done &&
                    a !== Pe.N.UndoneSubscription
                  );
                })(e, r);
              return (n += o || l ? (l ? s + i + pe[t].questCard.dailyMarginBottom : s + i) : s);
            });
          },
          Ge = [...Array(He.vW + 1)],
          We = (e, u) => (u <= 1 ? e : 2 === u ? Pe.N.Active : 3 === u ? Pe.N.Locked : void 0),
          $e = (0, xe.q)()(
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
                  isRegularWindowLoaded: Le.LO.box(!1),
                  isPremiumWindowLoaded: Le.LO.box(!1),
                },
                t = (0, ke.Om)(() => u.primitives.currentTabIdx.get()),
                a = (0, ke.Om)((e = Re.h2.Big) => c(e) === d(e)),
                r = (0, ke.Om)(() => Te.find(s(), (e) => e.status !== Pe.N.Done)),
                n = (0, ke.Om)((e) => {
                  var u, t, a, r, n;
                  let s;
                  var i, o;
                  e &&
                    e.bonusCondition &&
                    (null == (u = e.bonusCondition) || null == (t = u.items) ? void 0 : t.length) >=
                      1 &&
                    (s = Te.map(null == (i = e.bonusCondition) ? void 0 : i.items, Ne.yR));
                  e &&
                    (null == (a = e.postBattleCondition) || null == (r = a.items)
                      ? void 0
                      : r.length) >= 1 &&
                    (s = Te.map(null == (o = e.postBattleCondition) ? void 0 : o.items, Ne.yR));
                  return (s && (null == (n = s) ? void 0 : n.length)) > 0 ? s[0] : s;
                }),
                s = (0, ke.Om)(
                  (e = Re.h2.Big) => {
                    const t = u.isRegularWindowLoaded.get(),
                      a = u.regular.get().firstSeenNewBonusMissions && !t;
                    return (0, Me.c)(i()).map((t, r) =>
                      Object.assign({}, t, {
                        allRewards: [
                          ...(0, Ie.rl)(t.bonuses, t.id, e),
                          ...(0, Ie.rl)(t.subscriptionBonuses, t.id, e, !0),
                        ],
                        isQuestUnseen: (0, Ie.ix)(t, (0, Me.Q)(u.unseenQuests.get().unseenQuests)),
                        status: a ? We(t.status, r) : t.status,
                      }),
                    );
                  },
                  { equals: Ne.jv },
                ),
                i = (0, ke.Om)(
                  () => {
                    switch (t()) {
                      case Oe.g.DailyQuests:
                        return u.regularQuests.get();
                      case Oe.g.PremiumQuests:
                        return u.premiumQuests.get();
                      default:
                        return [];
                    }
                  },
                  { equals: Ne.jv },
                ),
                o = (0, ke.Om)(
                  () => {
                    switch (t()) {
                      case Oe.g.DailyQuests:
                        return u.regular.get();
                      case Oe.g.PremiumQuests:
                        return u.premium.get();
                      default:
                        return [];
                    }
                  },
                  { equals: Ne.jv },
                ),
                l = (0, ke.Om)(
                  (e = Re.h2.Big) => {
                    var t;
                    return Object.assign({}, u.epicQuest.get(), {
                      allRewards: [
                        ...(0, Ie.rl)(u.epicQuest.get().bonuses, u.epicQuest.get().id, e),
                        ...(0, Ie.rl)(
                          null == (t = u.epicQuest.get()) ? void 0 : t.subscriptionBonuses,
                          u.epicQuest.get().id,
                          e,
                          !0,
                        ),
                      ],
                    });
                  },
                  { equals: Ne.jv },
                ),
                c = (0, ke.Om)((e = Re.h2.Big) => s(e).length),
                d = (0, ke.Om)(
                  (e = Re.h2.Big) =>
                    s(e).filter(
                      (e) => e.status === Pe.N.Done || e.status === Pe.N.UndoneSubscription,
                    ).length,
                ),
                m = (0, ke.Om)(() => {
                  const e = r(),
                    u = n(e);
                  return null == u ? void 0 : u.descrData;
                }),
                _ = (0, ke.Om)(() => t() === Oe.g.PremiumQuests),
                E = (0, ke.Om)(() => {
                  const e = u.isPremiumWindowLoaded.get();
                  return (
                    _() &&
                    (!u.premium.get().hasPremiumAccount ||
                      (!e && u.premium.get().premMissionsTabDiscovered))
                  );
                });
              return Object.assign({}, u, {
                computes: {
                  getCurrentTabIndex: t,
                  getCurrentQuest: r,
                  getQuests: s,
                  getQuestsInfo: o,
                  getQuestsLength: c,
                  getCompletedlQuestLength: d,
                  getAllQuestsCompleted: a,
                  getConditions: n,
                  getConditionDescr: m,
                  getEpicQuests: l,
                  getCurrQuests: i,
                  isPremiumTab: _,
                  isPremiumBannerVisible: E,
                },
              });
            },
            ({ model: e, externalModel: u }) => {
              const t = (function (e) {
                const u = {};
                for (const t in e)
                  if (Object.prototype.hasOwnProperty.call(e, t)) {
                    const a = e[t];
                    u[t] = (0, Le.aD)(a);
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
          je = $e[0],
          qe = $e[1];
        var ze = t(8899);
        var Ze = t(7030),
          Xe = t(5739),
          Ye = t(3415);
        const Ve = "Progress_base_1a",
          Ke = "Progress_base__completed_99",
          Je = "Progress_base__disabled_94",
          eu = "Progress_currentProgress_a5",
          uu = "Progress_maxProgress_27",
          tu = (0, a.memo)(
            ({ current: e, max: u, completed: t, disabled: a = !1, classNames: n, className: i }) =>
              r().createElement(o.ZP, {
                text: R.strings.quests.dailyWidget.progress(),
                className: s()(Ve, t && Ke, a && Je, i),
                format: {
                  binding: {
                    currentProgress: r().createElement(o.ZP, {
                      text: String(e),
                      className: s()(eu, null == n ? void 0 : n.currentProgress),
                    }),
                    maxProgress: r().createElement(o.ZP, {
                      text: String(u),
                      className: s()(uu, null == n ? void 0 : n.maxProgress),
                    }),
                  },
                },
              }),
          ),
          au = "QuestCard_base_ac",
          ru = "QuestCard_base__weekly_15",
          nu = "QuestCard_base__completed_34",
          su = "QuestCard_base__disabled_7e",
          iu = "QuestCard_border_eb",
          ou = "QuestCard_disableBackground_29",
          lu = "QuestCard_background_f3",
          cu = "QuestCard_base__enabled_f0",
          du = "QuestCard_enableText_00",
          mu = "QuestCard_bubble_5e",
          _u = "QuestCard_rerollBackground_ab",
          Eu = "QuestCard_rerollBackground__visible_ca",
          Au = "QuestCard_header_bb",
          gu = "QuestCard_timerWrapper_9f",
          Du = "QuestCard_timer_e2",
          pu = "QuestCard_countdown_ef",
          Fu = "QuestCard_headerDivider_9b",
          Bu = "QuestCard_weekly_3e",
          Cu = "QuestCard_cardWrapper_62",
          bu = "QuestCard_contentWrapper_a9",
          fu = "QuestCard_content_55",
          hu = "QuestCard_content__hidden_e3",
          vu = "QuestCard_description_5a",
          wu = "QuestCard_progressWrapper_12",
          yu = "QuestCard_progressContainer_09",
          Su = "QuestCard_progress_74",
          Ru = "QuestCard_currentProgress_19",
          Pu = "QuestCard_maxProgress_0a",
          xu = "QuestCard_questIcon_c1",
          Nu = "QuestCard_divider_fa",
          Tu = "QuestCard_rewards_95",
          Mu = "QuestCard_rewardWrapper_9e",
          Lu = "QuestCard_rewardWrapper__appear_4b",
          ku = "QuestCard_opacityContainer_5f",
          Ou = "QuestCard_opacityContainer__unlock_a8",
          Iu = "QuestCard_rewardIcon_b9",
          Hu = "QuestCard_rewardIcon__unlock_f8",
          Qu = "QuestCard_subscriptionIcon_a9",
          Uu = "QuestCard_rewardInfo_08",
          Gu = "QuestCard_rewardHighlight_0d",
          Wu = "QuestCard_rewardOverlay_dc",
          $u = "QuestCard_rewardOverlay__unlock_c2",
          ju = "QuestCard_animationSmoke_c6";
        function qu() {
          return (
            (qu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            qu.apply(this, arguments)
          );
        }
        const zu = R.strings.quests,
          Zu = ["battlePassPoints"],
          Xu = "idle",
          Yu = "wait",
          Vu = "flash",
          Ku = (0, a.memo)(
            ({
              quest: e,
              conditions: u,
              disabledTooltipArgs: t,
              isEpic: n,
              isDisabled: i,
              isRerollAnimation: _,
              isUnlockAnimation: E,
              unlockPremiumAnimationState: A,
              position: g = 1,
            }) => {
              var D;
              const p = null != (D = (0, d.D9)(e)) ? D : e,
                F = (0, d.tp)(e, fe),
                B = (0, d.tp)(u, fe),
                C = _ ? F : e,
                b = C.isFirstView,
                f = C.allRewards,
                h = C.icon,
                v = C.isActiveSubscription,
                w = C.status,
                y = C.countDown,
                S = C.isQuestUnseen,
                P = C.isCompleted,
                N = _ ? B : u,
                T = N.earned,
                M = N.total,
                k = N.current,
                O = N.descrData,
                I = P ? M : k,
                H = e.status === Pe.N.UndoneSubscription,
                Q = e.status === Pe.N.Done,
                U = (e) => !Q && e.withSubscription && (!v || H),
                G = (0, a.useState)(!1),
                W = G[0],
                $ = G[1],
                j = (0, a.useState)(!1),
                q = j[0],
                z = j[1],
                Z = (0, a.useState)(Xu),
                X = Z[0],
                Y = Z[1],
                V = (0, De.GS)().mediaSize >= De.cJ.Medium ? "c_80" : "c_48",
                K = ((w === Pe.N.Done || w === Pe.N.UndoneSubscription) && !W) || P,
                J = Boolean(i || X !== Xu || (A && A !== Jt.COMPLETED && A !== Jt.IDLE)),
                ee = _ && !J && !K,
                ue = (0, a.useMemo)(() => 0.2 * g, [g]);
              return (
                (0, a.useEffect)(() => {
                  ((e.status !== Pe.N.Done && e.status !== Pe.N.UndoneSubscription) ||
                    !p ||
                    (null == p ? void 0 : p.status) === Pe.N.Done ||
                    (null == p ? void 0 : p.status) === Pe.N.UndoneSubscription ||
                    ($(!0), (0, m.G)(R.sounds.dq_widget_slide_in())),
                    (null != p && p.isActiveSubscription) ||
                      !e.isActiveSubscription ||
                      (z(!0), (0, m.G)(R.sounds.dq_subscription_reward_unlock())));
                }, [e, p]),
                (0, a.useEffect)(() => {
                  if (q)
                    return (0, c.F)(() => {
                      z(!1);
                    }, He.ji.unlockSubscriptionBonusDuration);
                }, [q]),
                (0, a.useEffect)(() => {
                  if (W)
                    return (0, c.F)(() => {
                      $(!1);
                    }, Fe);
                }, [W]),
                (0, a.useEffect)(() => {
                  E && Y(Yu);
                }, [E]),
                (0, a.useEffect)(
                  () =>
                    X === Yu
                      ? (0, c.F)(() => {
                          ((0, m.G)(R.sounds.dq_widget_slide_in()), Y(Vu));
                        }, He.ji.unlockBonusQuestDelay)
                      : X === Vu
                        ? (0, c.F)(() => {
                            Y(Xu);
                          }, He.ji.unlockBonusQuestDuration)
                        : void 0,
                  [X],
                ),
                n && !e.isEnabled
                  ? r().createElement(
                      l.i,
                      {
                        header: zu.switch.isWeeklyEnabled(),
                        body: zu.switch.isWeeklyEnabledTitle(),
                      },
                      r().createElement(
                        "div",
                        { className: s()(au, cu) },
                        r().createElement("div", { className: iu }),
                        r().createElement("div", { className: lu }),
                        r().createElement(o.ZP, {
                          text: zu.switch.isWeeklyEnabled(),
                          className: du,
                        }),
                      ),
                    )
                  : r().createElement(
                      "div",
                      { className: s()(au, n && ru, K && nu, J && su) },
                      J && r().createElement(l.i, t, r().createElement("div", { className: ou })),
                      r().createElement("div", { className: iu }),
                      r().createElement("div", { className: lu }),
                      S && r().createElement("div", { className: mu }),
                      r().createElement("div", {
                        className: s()(_u, (ee || X === Vu || A === Jt.QUESTS_UNLOCK) && Eu),
                      }),
                      n &&
                        r().createElement(
                          r().Fragment,
                          null,
                          r().createElement(
                            "div",
                            { className: Au },
                            r().createElement(o.ZP, {
                              text: zu.weeklyQuest.header.default(),
                              className: Bu,
                            }),
                            r().createElement(
                              l.i,
                              {
                                header: zu.weeklyQuest.countDown.tooltip.header(),
                                body: zu.weeklyQuest.countDown.tooltip.body(),
                              },
                              r().createElement(
                                "div",
                                { className: gu },
                                r().createElement(o.ZP, {
                                  text: zu.epicQuest.countDown.remainingText(),
                                  className: Du,
                                }),
                                r().createElement(
                                  "div",
                                  { className: pu },
                                  r().createElement(x, { timeToUpdate: y }),
                                ),
                              ),
                            ),
                          ),
                          r().createElement("div", { className: Fu }),
                        ),
                      r().createElement(
                        "div",
                        { className: Cu },
                        r().createElement(
                          "div",
                          { className: bu },
                          r().createElement(
                            "div",
                            { className: s()(fu, ee && hu) },
                            !n && r().createElement(o.ZP, { text: O, className: vu }),
                            r().createElement(
                              "div",
                              { className: wu },
                              r().createElement(
                                "div",
                                { className: yu },
                                n
                                  ? r().createElement(o.ZP, {
                                      text: zu.weeklyQuest.description.default(),
                                      className: vu,
                                    })
                                  : r().createElement("div", {
                                      className: xu,
                                      style: {
                                        backgroundImage: `url(${R.images.gui.maps.icons.daily.icons.$dyn(`${V}_${h}`)})`,
                                      },
                                    }),
                                Boolean(M) &&
                                  r().createElement(tu, {
                                    current: I,
                                    completed: K,
                                    max: M,
                                    className: Su,
                                    classNames: { currentProgress: Ru, maxProgress: Pu },
                                    disabled: i,
                                  }),
                              ),
                              Boolean(M) &&
                                r().createElement(ge, {
                                  disabled: J,
                                  size: n ? L.Medium : L.Small,
                                  value: I,
                                  deltaFrom: I - T,
                                  maxValue: M,
                                }),
                            ),
                          ),
                          r().createElement("div", { className: Nu }),
                          r().createElement(
                            "div",
                            { className: Tu },
                            f.map((e, u) => {
                              const t = e.withSubscription && !v,
                                a = Zu.includes(e.name) && b,
                                n = q && e.withSubscription;
                              return r().createElement(
                                "div",
                                {
                                  className: s()(Mu, a && Lu),
                                  style: { animationDelay: `${ue}s, ${0.5 + ue}s` },
                                  key: `reward-wrapper-${u}`,
                                },
                                r().createElement(
                                  "div",
                                  { className: s()((t || n) && ku, n && Ou) },
                                  ((e, u, t) => {
                                    const a = u.withSubscription && !v,
                                      n = q && u.withSubscription;
                                    return u.withSubscription && e
                                      ? r().createElement(
                                          r().Fragment,
                                          null,
                                          r().createElement(
                                            Ye.l,
                                            {
                                              tooltipArgs: {
                                                header: zu.reward.tooltip.noAdditionReward(),
                                                body: zu.reward.tooltip.simpleBody(),
                                              },
                                            },
                                            r().createElement(
                                              Xe.Q,
                                              qu({}, u, {
                                                classNames: {
                                                  info: Uu,
                                                  rewardIcon: s()((U(u) || n) && Iu, n && Hu),
                                                },
                                              }),
                                            ),
                                          ),
                                          u.withSubscription &&
                                            r().createElement(
                                              r().Fragment,
                                              null,
                                              r().createElement("div", { className: Qu }),
                                              r().createElement("div", { className: Gu }),
                                            ),
                                        )
                                      : r().createElement(
                                          r().Fragment,
                                          null,
                                          r().createElement(
                                            Ye.l,
                                            {
                                              tooltipArgs: !Q &&
                                                u.withSubscription &&
                                                !v && {
                                                  contentId:
                                                    R.views.lobby.daily.tooltips.LockedSubscriptionBonusTooltip(
                                                      "resId",
                                                    ),
                                                },
                                              key: `quest-reward-${t}`,
                                            },
                                            r().createElement(
                                              Xe.Q,
                                              qu({}, u, {
                                                classNames: {
                                                  info: Uu,
                                                  rewardIcon: s()(a && Iu, n && Hu),
                                                },
                                              }),
                                            ),
                                          ),
                                          u.withSubscription &&
                                            r().createElement(
                                              Ye.l,
                                              {
                                                tooltipArgs: {
                                                  contentId:
                                                    R.views.lobby.daily.tooltips.LockedSubscriptionBonusTooltip(
                                                      "resId",
                                                    ),
                                                  args: { isQuestDone: Q },
                                                },
                                                key: `quest-reward-icon${t}`,
                                              },
                                              r().createElement(
                                                r().Fragment,
                                                null,
                                                r().createElement("div", { className: Qu }),
                                                r().createElement("div", { className: Gu }),
                                              ),
                                            ),
                                        );
                                  })(H, e, u),
                                  a &&
                                    r().createElement("div", {
                                      className: ju,
                                      style: { animationDelay: `${0.5 + ue}s` },
                                    }),
                                ),
                                r().createElement("div", {
                                  className: s()((U(e) || q) && Wu, q && $u),
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
          Ju = {
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
        let et, ut;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(et || (et = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(ut || (ut = {})));
        const tt = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: i,
          mixClass: o,
          soundHover: l,
          soundClick: c,
          onMouseEnter: d,
          onMouseMove: _,
          onMouseDown: E,
          onMouseUp: A,
          onMouseLeave: g,
          onClick: D,
        }) => {
          const p = (0, a.useRef)(null),
            F = (0, a.useState)(t),
            B = F[0],
            C = F[1],
            b = (0, a.useState)(!1),
            f = b[0],
            h = b[1],
            v = (0, a.useState)(!1),
            w = v[0],
            y = v[1],
            S = (0, a.useCallback)(() => {
              i || (p.current && (p.current.focus(), C(!0)));
            }, [i]),
            P = (0, a.useCallback)(
              (e) => {
                B && null !== p.current && !p.current.contains(e.target) && C(!1);
              },
              [B],
            ),
            x = (0, a.useCallback)(
              (e) => {
                i || (D && D(e));
              },
              [i, D],
            ),
            N = (0, a.useCallback)(
              (e) => {
                i || (null !== l && (0, m.G)(l), d && d(e), y(!0));
              },
              [i, l, d],
            ),
            T = (0, a.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            M = (0, a.useCallback)(
              (e) => {
                i || (A && A(e), h(!1));
              },
              [i, A],
            ),
            L = (0, a.useCallback)(
              (e) => {
                i || (null !== c && (0, m.G)(c), E && E(e), t && S(), h(!0));
              },
              [i, c, E, S, t],
            ),
            k = (0, a.useCallback)(
              (e) => {
                i || (g && g(e), h(!1));
              },
              [i, g],
            ),
            O = s()(
              Ju.base,
              Ju[`base__${n}`],
              {
                [Ju.base__disabled]: i,
                [Ju[`base__${u}`]]: u,
                [Ju.base__focus]: B,
                [Ju.base__highlightActive]: f,
                [Ju.base__firstHover]: w,
              },
              o,
            ),
            I = s()(Ju.state, Ju.state__default);
          return (
            (0, a.useEffect)(
              () => (
                document.addEventListener("mousedown", P),
                () => {
                  document.removeEventListener("mousedown", P);
                }
              ),
              [P],
            ),
            (0, a.useEffect)(() => {
              C(t);
            }, [t]),
            r().createElement(
              "div",
              {
                ref: p,
                className: O,
                onMouseEnter: N,
                onMouseMove: T,
                onMouseUp: M,
                onMouseDown: L,
                onMouseLeave: k,
                onClick: x,
              },
              n !== et.ghost &&
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement("div", { className: Ju.back }),
                  r().createElement("span", { className: Ju.texture }),
                ),
              r().createElement(
                "span",
                { className: I },
                r().createElement("span", { className: Ju.stateDisabled }),
                r().createElement("span", { className: Ju.stateHighlightHover }),
                r().createElement("span", { className: Ju.stateHighlightActive }),
              ),
              r().createElement(
                "span",
                { className: Ju.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        tt.defaultProps = {
          type: et.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const at = (0, a.memo)(tt),
          rt = "PremiumBanner_base_d5",
          nt = "PremiumBanner_glow1_e4",
          st = "PremiumBanner_base__hide_c6",
          it = "PremiumBanner_glow2_e6",
          ot = "PremiumBanner_icon_9e",
          lt = "PremiumBanner_header_76",
          ct = "PremiumBanner_description_ce",
          dt = "PremiumBanner_button_9d",
          mt = R.strings.quests.premiumQuests.notPremiumAccount,
          _t = (0, a.memo)(({ onBuyPremium: e, hideBanner: u }) => {
            const t = (0, De.GS)().mediaSize >= De.cJ.Medium ? mt.paragraph() : mt.paragraphSmall();
            return r().createElement(
              "div",
              { className: s()(rt, u && st) },
              r().createElement("div", { className: it }),
              r().createElement("div", { className: nt }),
              r().createElement("div", { className: ot }),
              r().createElement(o.ZP, { text: mt.title(), className: lt }),
              r().createElement(o.ZP, { text: t, className: ct }),
              r().createElement(
                at,
                {
                  type: et.main,
                  mixClass: dt,
                  onClick: () => {
                    ((0, m.G)(R.sounds.play()), e());
                  },
                },
                r().createElement(o.ZP, { text: mt.button() }),
              ),
            );
          }),
          Et = "QuestCardBlock_base_bf",
          At = "QuestCardBlock_base__divider_63",
          gt = "QuestCardBlock_base__blinkAnimation_dc",
          Dt = "QuestCardBlock_divider_a9",
          pt = "QuestCardBlock_dividerBackground_62",
          Ft = "QuestCardBlock_divider__completed_b7",
          Bt = "QuestCardBlock_dividerContent_7a",
          Ct = "QuestCardBlock_dividerContent__hide_65",
          bt = "QuestCardBlock_dividerIcon_aa",
          ft = "QuestCardBlock_dividerDescription_64",
          ht = "QuestCardBlock_dividerMask_13",
          vt = "QuestCardBlock_progress_71",
          wt = "QuestCardBlock_progress__disabled_a4",
          yt = "QuestCardBlock_currentProgress_be",
          St = "QuestCardBlock_currentProgressItem_fb",
          Rt = "QuestCardBlock_maxProgress_7a",
          Pt = "QuestCardBlock_dividerBottom_f2",
          xt = R.strings.quests;
        let Nt;
        !(function (e) {
          ((e.IDLE = "idle"), (e.COMPLETE = "complete"), (e.BLINK = "blink"));
        })(Nt || (Nt = {}));
        const Tt = (0, _.Pi)(
            ({
              quest: e,
              prevQuestStatus: u,
              completedQuestsLength: t,
              position: n,
              isRerollAnimation: i,
              isAllQuestsCompletedDelayed: l,
              unlockPremiumAnimationState: m,
              isPremium: _,
            }) => {
              var E, A;
              const g = qe().model.computes.getConditions(e),
                D = (0, a.useState)(Nt.IDLE),
                p = D[0],
                F = D[1],
                B = (0, a.useState)(!1),
                C = B[0],
                b = B[1],
                f = null != (E = (0, d.D9)(e)) ? E : e,
                h = p === Nt.IDLE,
                v = p === Nt.BLINK,
                w = e.status === Pe.N.Locked,
                y = w && u !== Pe.N.Locked && !_,
                S =
                  (e.status === Pe.N.Done || e.status === Pe.N.UndoneSubscription) &&
                  u !== Pe.N.Done &&
                  u !== Pe.N.UndoneSubscription,
                P = null != (A = (0, d.D9)(y)) ? A : y,
                x = C && t === He.vW,
                N =
                  (e.status === Pe.N.Done || e.status === Pe.N.UndoneSubscription) &&
                  f &&
                  (null == f ? void 0 : f.status) !== Pe.N.Done &&
                  (null == f ? void 0 : f.status) !== Pe.N.UndoneSubscription,
                T = ((y || P || S) && h) || C,
                M = C && t === He.vW,
                L = y || P || C,
                k = (0, a.useMemo)(
                  () =>
                    _
                      ? {
                          header: xt.dailyQuests.premium.locked.tooltip.header(),
                          body: xt.dailyQuests.premium.locked.tooltip.body(),
                        }
                      : {
                          header: xt.dailyQuests.bonus.locked.tooltip.header(),
                          body: xt.dailyQuests.bonus.locked.tooltip.body(),
                        },
                  [_],
                );
              return (
                (0, a.useEffect)(
                  () => (
                    N && F(Nt.COMPLETE),
                    p === Nt.BLINK
                      ? (0, c.F)(() => {
                          F(Nt.IDLE);
                        }, Ce)
                      : p === Nt.COMPLETE
                        ? (0, c.F)(() => {
                            F(Nt.BLINK);
                          }, Be)
                        : void 0
                  ),
                  [N, p],
                ),
                (0, a.useEffect)(() => {
                  P && !y && b(!0);
                }, [P, y]),
                (0, a.useEffect)(() => {
                  if (C)
                    return (0, c.F)(() => {
                      b(!1);
                    }, ve);
                }, [C]),
                r().createElement(
                  "div",
                  { className: s()(Et, y && At, v && gt) },
                  T &&
                    r().createElement(
                      "div",
                      { className: s()(Dt, S && Ft) },
                      r().createElement("div", { className: pt }),
                      r().createElement("div", { className: Pt }),
                      y && r().createElement("div", { className: ht }),
                      r().createElement(
                        "div",
                        { className: s()(Bt, M && Ct) },
                        r().createElement("div", { className: bt }),
                        r().createElement(o.ZP, {
                          text: S
                            ? l
                              ? _
                                ? xt.premiumQuests.countDown.title()
                                : xt.dailyQuests.countDown.title()
                              : xt.dailyQuests.completed.title()
                            : xt.dailyQuests.locked.title(),
                          className: ft,
                        }),
                        L &&
                          r().createElement(o.ZP, {
                            text: R.strings.quests.dailyWidget.progress(),
                            className: s()(vt, !t && wt),
                            format: {
                              binding: {
                                currentProgress: r().createElement(
                                  "div",
                                  { className: yt, style: { "--currentProgress": t } },
                                  Ge.map((e, u) =>
                                    r().createElement(o.ZP, {
                                      key: u,
                                      text: String(u),
                                      className: St,
                                    }),
                                  ),
                                ),
                                maxProgress: r().createElement(o.ZP, {
                                  text: String(He.vW),
                                  className: Rt,
                                }),
                              },
                            },
                          }),
                      ),
                    ),
                  r().createElement(Ku, {
                    quest: e,
                    conditions: g,
                    disabledTooltipArgs: k,
                    isDisabled: w,
                    position: n,
                    isRerollAnimation: i,
                    isUnlockAnimation: x,
                    unlockPremiumAnimationState: m,
                  }),
                )
              );
            },
          ),
          Mt = "QuestCardList_base_a1",
          Lt = "QuestCardList_cardList_86",
          kt = "QuestCardList_cardList__allComplete_57",
          Ot = "QuestCardList_cardList__hide_cc",
          It = "QuestCardList_attentionMessage_3c",
          Ht = "QuestCardList_titleIcon_3f",
          Qt = "QuestCardList_title_a6",
          Ut = "QuestCardList_scroll_b1",
          Gt = "QuestCardList_scroll__maskTop_99",
          Wt = "QuestCardList_scroll__maskBottom_04",
          $t = "QuestCardList_scroll__maskBoth_d0",
          jt = "QuestCardList_scrollContent_3d",
          qt = "QuestCardList_questCardBlock_c2",
          zt = "QuestCardList_bannerWrapper_72",
          Zt = "QuestCardList_divider_3c",
          Xt = "QuestCardList_divider__hide_be",
          Yt = "QuestCardList_scrollBar_d4",
          Vt = "QuestCardList_barThumb_7d",
          Kt = "QuestCardList_barRail_3c";
        let Jt;
        !(function (e) {
          ((e.IDLE = "idle"),
            (e.BANNER_HIDE = "banner_hide"),
            (e.CARD_BLINK = "card_blink"),
            (e.QUESTS_UNLOCK = "quests_unlock"),
            (e.COMPLETED = "completed"));
        })(Jt || (Jt = {}));
        const ea = R.strings.quests.switch,
          ua = (0, _.Pi)(
            ({ hasTopMask: e, hasBottomMask: u, scrollApi: t, isRerollAnimation: n }) => {
              var i, l, _;
              const E = qe(),
                A = E.model,
                g = E.controls,
                D = (0, De.GS)().mediaSize,
                p = D >= De.cJ.Medium ? Re.h2.Big : Re.h2.Small,
                F = (0, a.useState)(!1),
                B = F[0],
                C = F[1],
                b = (0, a.useState)(!1),
                f = b[0],
                h = b[1],
                v = (0, a.useState)(!1),
                w = v[0],
                y = v[1],
                S = (0, a.useState)(Jt.IDLE),
                P = S[0],
                x = S[1],
                N = P === Jt.BANNER_HIDE,
                T = (0, d.tp)(A.computes.getCompletedlQuestLength(p), he),
                M = B ? T : A.computes.getCompletedlQuestLength(p),
                L = (0, d.tp)(A.computes.getAllQuestsCompleted(p), he),
                k = B ? L : A.computes.getAllQuestsCompleted(p),
                O = (0, d.tp)(A.computes.isPremiumTab(), he),
                I = B ? O : A.computes.isPremiumTab(),
                H = A.regular.get().isEnabled,
                Q = A.premium.get().isEnabled,
                U = I ? Q : H,
                G = (0, d.tp)(A.computes.isPremiumBannerVisible(), he),
                W = B ? G : A.computes.isPremiumBannerVisible(),
                $ = (0, d.tp)(A.computes.getQuests(p), he),
                j = B ? $ : A.computes.getQuests(p),
                q = A.computes.getEpicQuests(p),
                z = A.computes.getCurrentTabIndex(),
                Z = null != (i = (0, d.D9)(z)) ? i : z,
                X = null != (l = (0, d.D9)(W)) ? l : W,
                Y = (W && !k) || N,
                V = j.sort((e, u) => Qe.indexOf(u.status) - Qe.indexOf(e.status));
              const K = V.map((e) => e.status),
                J = null != (_ = (0, d.D9)(K)) ? _ : K,
                ee = Ue(K, Y, D, I),
                ue = f || B,
                te = X && !W && I && !B,
                ae = (0, Ze.useTransition)(
                  V.map((e, u) => {
                    const t = V.length - 1 === u;
                    return Object.assign(
                      {},
                      e,
                      { y: `${ee[u]}rem` },
                      t && { marginBottom: `${pe[D].questListMarginBottom}rem` },
                      { index: u },
                    );
                  }),
                  {
                    key: (e) => e.id,
                    enter: ({ y: e, marginBottom: u }) => ({ y: e, marginBottom: u }),
                    update: ({ y: e, marginBottom: u }) => ({ y: e, marginBottom: u }),
                    config: ue ? { duration: be } : { duration: Ce },
                    delay: ue || P !== Jt.IDLE ? be : Be,
                  },
                );
              var re, ne;
              return (
                (0, a.useEffect)(
                  () => (
                    te && ((0, m.G)(R.sounds.dq_widget_slide_in()), x(Jt.BANNER_HIDE)),
                    P === Jt.BANNER_HIDE
                      ? (0, c.F)(() => {
                          x(Jt.CARD_BLINK);
                        }, we)
                      : P === Jt.CARD_BLINK
                        ? (0, c.F)(() => {
                            x(Jt.QUESTS_UNLOCK);
                          }, ye)
                        : P === Jt.QUESTS_UNLOCK
                          ? (0, c.F)(() => {
                              x(Jt.COMPLETED);
                            }, Se)
                          : void 0
                  ),
                  [te, P],
                ),
                (0, a.useEffect)(() => {
                  J && JSON.stringify(K) !== JSON.stringify(J) && z === Z && !B && y(!0);
                }, [K, J, z, Z, B]),
                (0, a.useEffect)(() => {
                  if (w)
                    return (0, c.F)(() => {
                      y(!1);
                    }, Be);
                }, [w]),
                (re = () => (
                  h(!0),
                  (0, c.F)(() => {
                    h(!1);
                  }, be)
                )),
                (ne = []),
                (0, a.useEffect)(
                  () => (
                    window.addEventListener("resize", re),
                    () => window.removeEventListener("resize", re)
                  ),
                  ne,
                ),
                (0, a.useEffect)(() => {
                  Z !== z && C(!0);
                }, [Z, z]),
                (0, a.useEffect)(() => {
                  if (B)
                    return (0, c.F)(() => {
                      ((0, m.G)(R.sounds.dq_widget_slide_in()), C(!1));
                    }, he);
                }, [B]),
                r().createElement(
                  "div",
                  { className: Mt },
                  U &&
                    r().createElement(Ku, { quest: q, conditions: q, isEpic: !0, isDisabled: !1 }),
                  U
                    ? r().createElement(
                        "div",
                        { className: s()(Lt, k && kt, B && Ot) },
                        r().createElement(
                          ze.X.Vertical.Area,
                          {
                            api: t,
                            className: s()(Ut, e && !u && Gt, u && !e && Wt, e && u && $t),
                            classNames: { content: jt },
                          },
                          Y &&
                            r().createElement(
                              "div",
                              { className: s()(N && zt) },
                              r().createElement(_t, {
                                hideBanner: N,
                                onBuyPremium: g.onBuyPremium,
                              }),
                              r().createElement("div", { className: s()(Zt, N && Xt) }),
                            ),
                          ae((e, u) => {
                            var t;
                            const a = null == (t = j[u.index - 1]) ? void 0 : t.status;
                            return r().createElement(
                              Ze.animated.div,
                              { style: Object.assign({}, e), className: qt },
                              r().createElement(Tt, {
                                key: u.id,
                                quest: u,
                                prevQuestStatus: a,
                                isAllQuestsCompletedDelayed: L,
                                completedQuestsLength: M,
                                position: u.index + 1,
                                isRerollAnimation: n,
                                isCompleteAnimation: w,
                                unlockPremiumAnimationState: P,
                                isPremium: I,
                              }),
                            );
                          }),
                        ),
                        r().createElement(ze.X.Vertical.Bar, {
                          api: t,
                          classNames: { base: Yt, thumb: Vt, rail: Kt },
                        }),
                      )
                    : r().createElement(
                        "div",
                        { className: It },
                        r().createElement("div", { className: Ht }),
                        r().createElement(o.ZP, {
                          text: I ? ea.isDailyPremEnabled() : ea.isDailyRegularEnabled(),
                          format: { classMix: Qt },
                        }),
                      ),
                )
              );
            },
          ),
          ta = "App_base_f7",
          aa = "App_footer_f1",
          ra = "App_lip_3f",
          na = "App_lipDivider_a1",
          sa = "App_lip__hidden_ca",
          ia = "App_lipDivider__hidden_f5",
          oa = "App_divider_d4",
          la = "App_countdownWrapper_6e",
          ca = "App_countdownText_f1",
          da = "App_countdown_4c",
          ma = R.strings.quests.dailyQuests.countDown.tooltip,
          _a = (0, _.Pi)(() => {
            var e, u;
            const t = qe(),
              n = t.model,
              _ = t.controls,
              E = n.computes.isPremiumTab(),
              A = n.computes.getCurrentTabIndex(),
              g = E ? n.premium.get().isEnabled : n.regular.get().isEnabled,
              D = n.computes.getQuestsInfo(),
              p = D.countDown,
              F = D.rerollEnabled,
              B = D.rerollCountDown,
              C = null != (e = (0, d.D9)(A)) ? e : A,
              b = null != (u = (0, d.D9)(F)) ? u : F,
              f = (0, a.useState)(!1),
              h = f[0],
              v = f[1],
              w = (0, a.useState)(!1),
              y = w[0],
              S = w[1],
              P = (0, a.useState)(!1),
              M = P[0],
              L = P[1],
              k = (0, i.c4)();
            (!(function (e, u) {
              const t = e.contentRef,
                r = e.wrapperRef,
                n = e.scrollPosition,
                s = e.clampPosition,
                i = e.animationScroll,
                o = e.events,
                l = (0, a.useState)(T),
                c = l[0],
                d = l[1];
              ((0, a.useEffect)(() => {
                const e = t.current;
                e && (e.style.cursor = "dragging" === c.type ? "grabbing" : "grab");
              }, [t, c.type]),
                (0, a.useEffect)(() => {
                  if ("dragging" !== c.type) return;
                  const e = (e) => {
                      const a = t.current,
                        o = r.current;
                      if (!a || !o) return;
                      const l = c.positionFrom - e.screenY,
                        d = c.previousScrollPosition + l;
                      n.start(
                        Object.assign(
                          {
                            scrollPosition: s(a, d),
                            from: { scrollPosition: i.scrollPosition.get() },
                          },
                          u && { config: u },
                        ),
                      );
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", e), d({ type: "scrollingToEnd" }));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [i.scrollPosition, s, t, c, n, r, u]),
                (0, a.useEffect)(() => {
                  if ("scrollingToEnd" !== c.type) return;
                  const e = () => {
                    d(T);
                  };
                  return (i.scrollPosition.idle && e(), o.on("rest", e), () => o.off("rest", e));
                }, [i.scrollPosition, c.type, o]),
                (0, a.useEffect)(() => {
                  const e = t.current;
                  if (!e) return;
                  const u = (e) => {
                    (e.stopPropagation(),
                      0 === e.button &&
                        d({
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
            })(k),
              (0, a.useEffect)(() => {
                const e = () => {
                  const e = k.animationScroll.scrollPosition.goal,
                    u = k.getBounds()[1];
                  (v(e > 3), S(e < u - 3));
                };
                return (
                  k.events.on("recalculateContent", e),
                  k.events.on("change", e),
                  () => {
                    (k.events.off("recalculateContent", e), k.events.off("change", e));
                  }
                );
              }, [k]),
              (0, a.useEffect)(() => {
                E ? _.onPremiumWindowLoaded() : _.onRegularWindowLoaded();
              }, [_, E]),
              (0, a.useEffect)(() => {
                b && !F && C === A && B && (L(!0), (0, m.G)(R.sounds.dq_widget_slide_in()));
              }, [F, b, A, C, B]),
              (0, a.useEffect)(() => {
                if (M)
                  return (0, c.F)(() => {
                    L(!1);
                  }, fe);
              }, [M]));
            const O = (0, a.useCallback)(() => {
              _.onReroll(E);
            }, [_, E]);
            return r().createElement(
              "div",
              { className: ta },
              r().createElement(ua, {
                hasTopMask: h,
                hasBottomMask: y,
                scrollApi: k,
                isRerollAnimation: M,
              }),
              g &&
                r().createElement(
                  "div",
                  { className: aa },
                  r().createElement("div", { className: s()(ra, !y && sa) }),
                  r().createElement("div", { className: s()(na, y && ia) }),
                  r().createElement(N.q, { canReroll: F, onReroll: O, rerollPremium: E }),
                  r().createElement("div", { className: oa }),
                  r().createElement(
                    l.i,
                    { header: ma.header(), body: ma.body() },
                    r().createElement(
                      "div",
                      { className: la },
                      r().createElement(o.ZP, {
                        text: R.strings.quests.dailyQuests.countDown.remainingText(),
                        className: ca,
                      }),
                      r().createElement(
                        "div",
                        { className: da },
                        r().createElement(x, { timeToUpdate: p }),
                      ),
                    ),
                  ),
                ),
            );
          }),
          Ea = (0, a.memo)(function (e) {
            const u = (0, a.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
            return r().createElement(je, { options: u }, r().createElement(_a, null));
          });
      },
      6892: (e, u, t) => {
        "use strict";
        var a = t(7739),
          r = t(6179),
          n = t.n(r),
          s = t(6483),
          i = t.n(s),
          o = t(926),
          l = t.n(o),
          c = t(5415);
        const d = ["children", "className"];
        function m() {
          return (
            (m =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            m.apply(this, arguments)
          );
        }
        const _ = {
            [c.fd.ExtraSmall]: "",
            [c.fd.Small]: l().SMALL_WIDTH,
            [c.fd.Medium]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH}`,
            [c.fd.Large]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH}`,
            [c.fd.ExtraLarge]:
              `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH} ${l().EXTRA_LARGE_WIDTH}`,
          },
          E = {
            [c.Aq.ExtraSmall]: "",
            [c.Aq.Small]: l().SMALL_HEIGHT,
            [c.Aq.Medium]: `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT}`,
            [c.Aq.Large]: `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT} ${l().LARGE_HEIGHT}`,
            [c.Aq.ExtraLarge]:
              `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT} ${l().LARGE_HEIGHT} ${l().EXTRA_LARGE_HEIGHT}`,
          },
          A = {
            [c.cJ.ExtraSmall]: "",
            [c.cJ.Small]: l().SMALL,
            [c.cJ.Medium]: `${l().SMALL} ${l().MEDIUM}`,
            [c.cJ.Large]: `${l().SMALL} ${l().MEDIUM} ${l().LARGE}`,
            [c.cJ.ExtraLarge]: `${l().SMALL} ${l().MEDIUM} ${l().LARGE} ${l().EXTRA_LARGE}`,
          },
          g = (e) => {
            let u = e.children,
              t = e.className,
              a = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, d);
            const r = (0, c.GS)(),
              s = r.mediaWidth,
              o = r.mediaHeight,
              l = r.mediaSize;
            return n().createElement("div", m({ className: i()(t, _[s], E[o], A[l]) }, a), u);
          },
          D = ["children"];
        const p = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, D);
          return n().createElement(a.ZN, null, n().createElement(g, t, u));
        };
        var F = t(493),
          B = t.n(F),
          C = t(3138),
          b = t(5521);
        t(4179);
        const f = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function h(e = b.n.NONE, u = f, t = !1) {
          (0, r.useEffect)(() => {
            if (e !== b.n.NONE)
              return (
                window.addEventListener("keydown", a, t),
                () => {
                  window.removeEventListener("keydown", a, t);
                }
              );
            function a(a) {
              if (a.keyCode === e) {
                if (C.O.view.isEventHandled()) return;
                (C.O.view.setEventHandled(), u(a), t && a.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        var v = t(8515),
          w = t(7030),
          y = t(3017),
          S = t(3215),
          P = t(4598),
          x = t(9480),
          N = t(3946),
          T = t(9153);
        const M = (0, S.q)()(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  primitives: e.primitives(["currentTabIdx"]),
                  dailyBattleTypes: e.array("dailyBattleTypes", []),
                  serialEnterBattleTypes: e.array("serialEnterBattleTypes", []),
                },
                t = (0, N.Om)(() => [
                  { tabIndex: T.g.DailyQuests, isEnabled: u.root.get().isDailyRegularEnabled },
                  { tabIndex: T.g.PremiumQuests, isEnabled: u.root.get().isDailyPremEnabled },
                  {
                    tabIndex: T.g.SerialEnter,
                    isEnabled: Boolean(u.root.get().isSerialEnterEnabled),
                  },
                ]),
                a = (0, N.Om)(() => t().some((e) => e.tabIndex === T.g.SerialEnter && e.isEnabled)),
                r = (0, N.Om)(() => {
                  var e, a, r;
                  const n = Number(u.primitives.currentTabIdx.get()),
                    s = t(),
                    i = s.find((e) => e.tabIndex === n);
                  return null != i && i.isEnabled
                    ? i.tabIndex
                    : null != (e = null == (a = s.find((e) => e.isEnabled)) ? void 0 : a.tabIndex)
                      ? e
                      : null == (r = s[0])
                        ? void 0
                        : r.tabIndex;
                }),
                n = (0, N.Om)(() => x.map(u.dailyBattleTypes.get(), P.yR), { equals: P.jv }),
                s = (0, N.Om)(() => x.map(u.serialEnterBattleTypes.get(), P.yR), { equals: P.jv });
              return Object.assign({}, u, {
                computes: {
                  getEnabledFeatures: t,
                  getCurrentTabIndex: r,
                  getDailyBattleTypes: n,
                  getSerialEnterBattleTypes: s,
                  isSerialEnterEnabled: a,
                },
              });
            },
            ({ externalModel: e }) => ({
              close: e.createCallbackNoArgs("onClose"),
              infoClick: e.createCallbackNoArgs("onInfoClick"),
              tabClick: e.createCallback((e) => ({ tabIdx: e }), "onTabClick"),
              onShowInfo: e.createCallbackNoArgs("onShowInfo"),
            }),
          ),
          L = M[0],
          k = M[1];
        var O = t(8899),
          I = t(7701),
          H = t(2344),
          Q = t(8025),
          U = t(9440),
          G = t(2603),
          W = t(648),
          $ = t(4528),
          j = t(7613),
          q = t(3415),
          z = t(6373),
          Z = t(7727);
        const X = "TabCathegory_base_76",
          Y = "TabCathegory_info_bd",
          V = "TabCathegory_battleModes_cb",
          K = "TabCathegory_battleModeIcon_35",
          J = "TabCathegory_battleModeHidden_22",
          ee = ({ label: e, infoTooltipAgs: u, battleModes: t, onInfoClick: a }) => {
            const r = t.slice(0, 3);
            return n().createElement(
              "div",
              { className: X },
              n().createElement("div", null, e),
              n().createElement(
                z.i,
                u,
                n().createElement("div", {
                  className: Y,
                  onClick: () => {
                    ((0, Z.G)(R.sounds.play()), a());
                  },
                  onMouseEnter: Z.$.playHighlight,
                }),
              ),
              n().createElement(
                q.l,
                {
                  tooltipArgs: {
                    contentId: R.views.lobby.daily.tooltips.ModeSelectorTooltip("resId"),
                  },
                  className: V,
                },
                n().createElement(
                  n().Fragment,
                  null,
                  r.map((e, u) =>
                    n().createElement("div", {
                      className: K,
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.battleTypeIcons.c_32x32.c_${e})`,
                      },
                      key: u,
                    }),
                  ),
                  t.length > 3 &&
                    n().createElement(j.ZP, {
                      className: J,
                      text: R.strings.quests.dailyQuests.tab.hiddenBattleTypes(),
                    }),
                ),
              ),
            );
          },
          ue = "Tabs_base_5f",
          te = R.strings.quests,
          ae = R.views.lobby,
          re = (0, v.Pi)(({ selectedTabIndex: e, onTabClick: u }) => {
            const t = k(),
              a = t.model,
              r = t.controls,
              s = a.computes.isSerialEnterEnabled();
            return n().createElement(
              "div",
              { className: ue },
              s &&
                n().createElement(
                  n().Fragment,
                  null,
                  n().createElement(ee, {
                    label: te.missions.tab.serialEnter.header(),
                    infoTooltipAgs: {
                      header: te.dailyQuests.tab.cathegory.tooltip.serialEnter.header(),
                      body: te.dailyQuests.tab.cathegory.tooltip.serialEnter.body(),
                    },
                    onInfoClick: r.onShowInfo,
                    battleModes: a.computes.getSerialEnterBattleTypes(),
                  }),
                  n().createElement($.B, {
                    resId: ae.daily.SerialEnterTabView("resId"),
                    onClick: u,
                    isSelected: e === T.g.SerialEnter,
                  }),
                ),
              n().createElement(ee, {
                label: te.missions.tab.daily.header(),
                infoTooltipAgs: {
                  header: te.dailyQuests.tab.cathegory.tooltip.daily.header(),
                  body: te.dailyQuests.tab.cathegory.tooltip.daily.body(),
                },
                onInfoClick: r.infoClick,
                battleModes: a.computes.getDailyBattleTypes(),
              }),
              n().createElement(W._, {
                resId: ae.daily.DailyQuestRegularTabView("resId"),
                onClick: u,
                isSelected: e === T.g.DailyQuests,
              }),
              n().createElement(G.V, {
                resId: ae.daily.DailyQuestPremiumTabView("resId"),
                onClick: u,
                isSelected: e === T.g.PremiumQuests,
              }),
            );
          }),
          ne = "MainPage_base_fa",
          se = "MainPage_contentWrapper_03",
          ie = "MainPage_scroll_e6",
          oe = "MainPage_scrollArea_2e",
          le = "MainPage_scrollContent_27",
          ce = (0, v.Pi)(() => {
            const e = k(),
              u = e.model,
              t = e.controls,
              a = u.computes.isSerialEnterEnabled(),
              s = u.computes.getCurrentTabIndex(),
              i = (0, r.useState)(s),
              o = i[0],
              l = i[1],
              c = (0, H.tp)(o, 500),
              d = (0, I.c4)();
            (0, r.useEffect)(() => {
              l(s);
            }, [s]);
            const m = (0, r.useCallback)(
                (e) => {
                  (l(e), t.tabClick(e));
                },
                [t],
              ),
              _ = (0, r.useMemo)(() => (a || c !== T.g.SerialEnter ? c : s), [c, a, s]),
              E = _ === T.g.DailyQuests || _ === T.g.PremiumQuests,
              A = a && _ === T.g.SerialEnter;
            return n().createElement(
              "div",
              { className: ne },
              n().createElement(re, { selectedTabIndex: o, onTabClick: m }),
              n().createElement(
                "div",
                { className: se },
                E &&
                  n().createElement(Q.Q, {
                    resId: R.views.lobby.daily.DailyQuestsRegularView("resId"),
                  }),
                A &&
                  n().createElement(
                    O.X.Vertical.Default,
                    {
                      className: ie,
                      scrollClassName: oe,
                      scrollClassNames: { content: le },
                      api: d,
                    },
                    n().createElement(U.k, { resId: R.views.lobby.daily.SerialEnterView("resId") }),
                  ),
              ),
            );
          }),
          de = {
            base: "App_base_db",
            background: "App_background_4b",
            background__dailyQuests: "App_background__dailyQuests_ab",
            background__serialEnter: "App_background__serialEnter_7e",
            background__premiumQuests: "App_background__premiumQuests_35",
            infoButton: "App_infoButton_85",
            infoButton__info: "App_infoButton__info_f9",
            fadeIn: "App_fadeIn_ab",
            rewardsButton: "App_rewardsButton_34",
            hiddenBlink: "App_hiddenBlink_62",
            zoomOut: "App_zoomOut_51",
            appear: "App_appear_f7",
            fade: "App_fade_f2",
            smokeDispersion: "App_smokeDispersion_9a",
            lockIconZoomOut: "App_lockIconZoomOut_2b",
            lightIn: "App_lightIn_57",
            lightInIcon: "App_lightInIcon_5e",
          },
          me = (0, v.Pi)(() => {
            var e;
            const u = k(),
              t = u.model;
            !(function ({
              key: e = b.n.ESCAPE,
              callback: u = () => C.O.view.sendEvent.close(),
              preventPropagation: t = !0,
            } = {}) {
              h(e, u, t);
            })({ callback: u.controls.close });
            const a = null != (e = (0, y.vh)(t.computes.getCurrentTabIndex())) ? e : "",
              r = (0, w.useTransition)(a, {
                from: { opacity: 0 },
                enter: { opacity: 1 },
                leave: { opacity: 0 },
                delay: 200,
              });
            return n().createElement(
              "div",
              { className: i()(de.base, de[`base__${a}`]) },
              r((e, u) =>
                n().createElement(w.animated.div, {
                  style: e,
                  className: i()(de.background, de[`background__${u}`]),
                }),
              ),
              n().createElement(ce, null),
            );
          });
        engine.whenReady.then(() => {
          B().render(
            n().createElement(p, null, n().createElement(L, null, n().createElement(me, null))),
            document.getElementById("root"),
          );
        });
      },
      3017: (e, u, t) => {
        "use strict";
        t.d(u, { WO: () => i, ix: () => d, rl: () => c, vh: () => l });
        var a = t(2862),
          r = t(729),
          n = t(9480),
          s = t(9153);
        const i = "tooltipId",
          o = {
            [s.g.DailyQuests]: "dailyQuests",
            [s.g.PremiumQuests]: "premiumQuests",
            [s.g.SerialEnter]: "serialEnter",
          },
          l = (e) => {
            if (void 0 !== e)
              return (
                void 0 === o[e] &&
                  console.error(`Content resource name was not found for tab index ${e}`),
                o[e]
              );
          },
          c = (e, u, t = a.h2.Big, s) =>
            null != e && e.length
              ? null == n
                ? void 0
                : n.map(e, (e) => ({
                    name: e.name,
                    size: t,
                    image: (0, r.ry)(e, t),
                    special: e.overlayType,
                    value: e.value,
                    valueType: (0, r.p3)(e.name),
                    tooltipArgs: (0, r.pI)({ [i]: `${u}:${e.index}` }, Number(e.tooltipContentId), {
                      ignoreShowDelay: !0,
                    }),
                    withSubscription: s,
                  }))
              : [],
          d = (e, u) => u.some((u) => u.questID === e.id);
      },
      4528: (e, u, t) => {
        "use strict";
        t.d(u, { B: () => h });
        var a = t(6179),
          r = t.n(a),
          n = t(6483),
          s = t.n(n),
          i = t(7613),
          o = t(7727),
          l = t(8515),
          c = t(9153);
        const d = {
          base: "App_base_af",
          base__selected: "App_base__selected_17",
          base__claiming: "App_base__claiming_00",
          line1: "App_line1_59",
          line2: "App_line2_be",
          bg: "App_bg_ee",
          hoverBg: "App_hoverBg_8f",
          base__default: "App_base__default_3e",
          base__done: "App_base__done_fe",
          base__hover: "App_base__hover_f8",
          selectedBg: "App_selectedBg_85",
          claimSelectedBg: "App_claimSelectedBg_9e",
          claimSelectedBg__default: "App_claimSelectedBg__default_fb",
          claimSelectedBg__done: "App_claimSelectedBg__done_cf",
          claimSelectedBg__out: "App_claimSelectedBg__out_93",
          fadeOut: "App_fadeOut_24",
          claimSelectedBg__in: "App_claimSelectedBg__in_84",
          fadeIn: "App_fadeIn_51",
          claimDefaultBg: "App_claimDefaultBg_a2",
          claimDefaultBg__default: "App_claimDefaultBg__default_ea",
          claimDefaultBg__done: "App_claimDefaultBg__done_6b",
          claimDefaultBg__out: "App_claimDefaultBg__out_83",
          claimDefaultBg__in: "App_claimDefaultBg__in_c0",
          content: "App_content_6a",
          iconWrapper: "App_iconWrapper_95",
          icon: "App_icon_0c",
          separator: "App_separator_06",
          textBlock: "App_textBlock_4e",
          textLayerMeasure: "App_textLayerMeasure_31",
          textLayer: "App_textLayer_08",
          textBlock__claiming: "App_textBlock__claiming_b0",
          textLayer__out: "App_textLayer__out_4b",
          textLayer__in: "App_textLayer__in_11",
          claimLine2OpacityIn: "App_claimLine2OpacityIn_bd",
        };
        var m = t(3215),
          _ = t(4598);
        const E = (0, m.q)()(({ observableModel: e }) => {
            const u = { root: e.object() };
            return Object.assign({}, u, { computes: {} });
          }, _.ZT),
          A = E[0],
          g = E[1];
        var D = t(122),
          p = t(6970);
        let F;
        !(function (e) {
          ((e.Default = "default"), (e.Done = "done"));
        })(F || (F = {}));
        const B = R.strings.quests.serialEnter.tab,
          C = (e, u) =>
            u && e === F.Done
              ? { line1: B.final.title(), line2: B.final.description() }
              : e === F.Done
                ? { line1: B.completed.title(), line2: B.completed.description() }
                : { line1: B.label(), line2: B.description() },
          b = ({ line1: e, line2: u }) =>
            r().createElement(
              r().Fragment,
              null,
              r().createElement(i.ZP, { className: d.line1, text: e }),
              r().createElement(i.ZP, { className: d.line2, text: u }),
            ),
          f = (0, l.Pi)(({ isSelected: e, onClick: u }) => {
            const t = g().model.root.get(),
              n = t.isEnabled,
              i = t.isViewed,
              l = t.isCompleted,
              m = t.isFinal,
              _ = Boolean(n),
              E = Boolean(i),
              A = Boolean(m),
              B = ((e, u) => {
                const t = (0, a.useState)(!1),
                  r = t[0],
                  n = t[1],
                  s = (0, a.useState)(() => (u ? F.Done : F.Default)),
                  i = s[0],
                  o = s[1];
                return (
                  (0, a.useEffect)(
                    () =>
                      e
                        ? u
                          ? (o(F.Done), void n(!1))
                          : (o(F.Default),
                            (0, D.F)(
                              () => (
                                n(!0),
                                (0, D.F)(() => {
                                  (o(F.Done), n(!1));
                                }, p.i$)
                              ),
                              p.ul,
                            ))
                        : (o(F.Default), void n(!1)),
                    [e, u],
                  ),
                  { isClaiming: r, state: i }
                );
              })(_ && Boolean(l), E),
              f = B.isClaiming,
              h = B.state,
              v = (0, a.useState)(!1),
              w = v[0],
              y = v[1],
              S = C(h, A),
              R = f ? C(F.Done, A) : S,
              P = !e && !f && w,
              x = (0, a.useCallback)(() => {
                e || f || (o.$.playHighlight(), y(!0));
              }, [e, f]),
              N = (0, a.useCallback)(() => {
                e || y(!1);
              }, [e]),
              T = (0, a.useCallback)(() => {
                _ && !f && (o.$.playClick(), u(c.g.SerialEnter), y(!1));
              }, [_, f, u]);
            return r().createElement(
              "div",
              {
                className: s()(
                  d.base,
                  f ? d.base__claiming : d[`base__${h}`],
                  P && d.base__hover,
                  e && !f && d.base__selected,
                ),
                onMouseEnter: x,
                onMouseLeave: N,
                onClick: T,
              },
              f &&
                e &&
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement("div", {
                    className: s()(
                      d.claimSelectedBg,
                      d.claimSelectedBg__done,
                      d.claimSelectedBg__in,
                    ),
                  }),
                  r().createElement("div", {
                    className: s()(
                      d.claimSelectedBg,
                      d.claimSelectedBg__default,
                      d.claimSelectedBg__out,
                    ),
                  }),
                ),
              f &&
                !e &&
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement("div", {
                    className: s()(d.claimDefaultBg, d.claimDefaultBg__done, d.claimDefaultBg__in),
                  }),
                  r().createElement("div", {
                    className: s()(
                      d.claimDefaultBg,
                      d.claimDefaultBg__default,
                      d.claimDefaultBg__out,
                    ),
                  }),
                ),
              !f &&
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement("div", { className: d.bg }),
                  r().createElement("div", { className: d.hoverBg }),
                  r().createElement("div", { className: d.selectedBg }),
                ),
              r().createElement(
                "div",
                { className: d.content },
                r().createElement(
                  "div",
                  { className: d.iconWrapper },
                  r().createElement("div", { className: d.icon }),
                ),
                r().createElement("div", { className: d.separator }),
                r().createElement(
                  "div",
                  { className: s()(d.textBlock, f && d.textBlock__claiming) },
                  f
                    ? r().createElement(
                        r().Fragment,
                        null,
                        r().createElement(
                          "div",
                          { className: d.textLayerMeasure },
                          r().createElement(b, R),
                        ),
                        r().createElement(
                          "div",
                          { className: s()(d.textLayer, d.textLayer__in) },
                          r().createElement(b, R),
                        ),
                        r().createElement(
                          "div",
                          { className: s()(d.textLayer, d.textLayer__out) },
                          r().createElement(b, S),
                        ),
                      )
                    : r().createElement(b, S),
                ),
              ),
            );
          }),
          h = (0, a.memo)(function (e) {
            const u = (0, a.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
            return r().createElement(A, { options: u }, r().createElement(f, e));
          });
      },
      9440: (e, u, t) => {
        "use strict";
        t.d(u, { k: () => le });
        var a = t(6179),
          r = t.n(a),
          n = t(8515),
          s = t(5415);
        const i = "App_base_a6",
          o = "App_grid_61",
          l = "App_lastRow_97";
        var c = t(6483),
          d = t.n(c),
          m = t(5739),
          _ = t(7613),
          E = t(2862);
        const A = (e) => e === E.E4.Vehicles,
          g = (e) => (e >= s.cJ.Medium ? E.h2.Big : E.h2.Small);
        let D;
        !(function (e) {
          ((e.Disabled = "disabled"),
            (e.Current = "current"),
            (e.NeedRelogin = "needRelogin"),
            (e.Today = "today"),
            (e.Completed = "completed"));
        })(D || (D = {}));
        const p = [D.Completed, D.Today],
          F = [D.Current, D.NeedRelogin],
          B = (e) => p.includes(e),
          C = (e, u, t, a) => {
            if (t && void 0 !== e.base__claiming) return e.base__claiming;
            if (a && void 0 !== e.base__today) return e.base__today;
            return e[`base__${u === D.NeedRelogin ? D.Current : u}`];
          };
        var b = t(122),
          f = t(6970);
        const h = (e) => {
            const u = (0, a.useState)(!1),
              t = u[0],
              r = u[1],
              n = (0, a.useState)(!1),
              s = n[0],
              i = n[1],
              o = (0, a.useRef)(!1),
              l = e === D.Today || s;
            return (
              (0, a.useEffect)(() => {
                if (e === D.Current && !o.current)
                  return (
                    (o.current = !0),
                    (0, b.F)(
                      () => (
                        r(!0),
                        (0, b.F)(() => {
                          (r(!1), i(!0));
                        }, f.i$)
                      ),
                      f.ul,
                    )
                  );
              }, [e]),
              { isClaiming: t, isTodayStyle: l }
            );
          },
          v = {
            base: "CalendarHeader_base_70",
            base__current: "CalendarHeader_base__current_43",
            border: "CalendarHeader_border_93",
            rewards: "CalendarHeader_rewards_44",
            base__today: "CalendarHeader_base__today_aa",
            base__claiming: "CalendarHeader_base__claiming_b5",
            check: "CalendarHeader_check_53",
            claimCheckAppear: "CalendarHeader_claimCheckAppear_49",
            base__completed: "CalendarHeader_base__completed_98",
            base__disabled: "CalendarHeader_base__disabled_34",
            claimBg: "CalendarHeader_claimBg_9b",
            claimBg__current: "CalendarHeader_claimBg__current_09",
            claimBg__today: "CalendarHeader_claimBg__today_b9",
            claimBg__out: "CalendarHeader_claimBg__out_93",
            fadeOut: "CalendarHeader_fadeOut_70",
            claimBg__in: "CalendarHeader_claimBg__in_d6",
            fadeIn: "CalendarHeader_fadeIn_8b",
            border__current: "CalendarHeader_border__current_4d",
            border__today: "CalendarHeader_border__today_e3",
            border__out: "CalendarHeader_border__out_8d",
            border__in: "CalendarHeader_border__in_6d",
            day: "CalendarHeader_day_85",
            content: "CalendarHeader_content_79",
            reward: "CalendarHeader_reward_98",
            separator: "CalendarHeader_separator_aa",
            textBlock: "CalendarHeader_textBlock_9c",
            title: "CalendarHeader_title_22",
            titleMain: "CalendarHeader_titleMain_50",
            subtitle: "CalendarHeader_subtitle_24",
          };
        function w() {
          return (
            (w =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            w.apply(this, arguments)
          );
        }
        const y = R.strings.quests.serialEnter.calendar,
          S = r().memo(function ({ dayData: e }) {
            const u = e.day,
              t = e.rewards,
              a = e.state,
              n = (0, s.GS)().mediaSize,
              i = g(n),
              o = h(a),
              l = o.isClaiming,
              c = o.isTodayStyle,
              E = B(a) || c || l;
            return r().createElement(
              "div",
              { className: d()(v.base, C(v, a, l, c)) },
              l &&
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement("div", {
                    className: d()(v.claimBg, v.claimBg__today, v.claimBg__in),
                  }),
                  r().createElement("div", {
                    className: d()(v.claimBg, v.claimBg__current, v.claimBg__out),
                  }),
                  r().createElement("div", {
                    className: d()(v.border, v.border__today, v.border__in),
                  }),
                  r().createElement("div", {
                    className: d()(v.border, v.border__current, v.border__out),
                  }),
                ),
              !l && r().createElement("div", { className: v.border }),
              r().createElement(_.ZP, { className: v.day, text: String(u) }),
              E && r().createElement("div", { className: v.check }),
              r().createElement(
                "div",
                { className: v.content },
                r().createElement(
                  "div",
                  { className: v.rewards },
                  t.map((e, u) =>
                    r().createElement(
                      m.Q,
                      w({ key: `header-${e.name}-${u}` }, e, { size: i, className: v.reward }),
                    ),
                  ),
                ),
                r().createElement("div", { className: v.separator }),
                r().createElement(
                  "div",
                  { className: v.textBlock },
                  r().createElement(
                    "div",
                    { className: v.title },
                    r().createElement(_.ZP, { className: v.titleMain, text: y.title() }),
                  ),
                  r().createElement(_.ZP, { className: v.subtitle, text: y.description() }),
                ),
              ),
            );
          });
        var P = t(7727);
        const x = {
            base: "Preview_base_1f",
            base__hovered: "Preview_base__hovered_ee",
            icon: "Preview_icon_f3",
            icon__small: "Preview_icon__small_a1",
            icon__normal: "Preview_icon__normal_5c",
            base__mouseDown: "Preview_base__mouseDown_d0",
            label: "Preview_label_2e",
            base__visibleLabel: "Preview_base__visibleLabel_92",
          },
          N = [
            "label",
            "isVisibleLabel",
            "autofocus",
            "soundHover",
            "soundClick",
            "size",
            "classNames",
            "onClick",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onMouseUp",
            "onFocus",
            "onBlur",
          ];
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        let M;
        !(function (e) {
          ((e.SMALL = "small"), (e.NORMAL = "normal"));
        })(M || (M = {}));
        const L = (0, a.memo)((e) => {
          let u = e.label,
            t = e.isVisibleLabel,
            n = void 0 !== t && t,
            s = e.autofocus,
            i = void 0 !== s && s,
            o = e.soundHover,
            l = void 0 === o ? "highlight" : o,
            c = e.soundClick,
            m = void 0 === c ? "play" : c,
            _ = e.size,
            E = void 0 === _ ? M.NORMAL : _,
            A = e.classNames,
            g = e.onClick,
            D = e.onMouseEnter,
            p = e.onMouseLeave,
            F = e.onMouseDown,
            B = e.onMouseUp,
            C = e.onFocus,
            b = e.onBlur,
            f = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, N);
          const h = (0, a.useState)(!1),
            v = h[0],
            w = h[1],
            y = (0, a.useState)(!1),
            S = y[0],
            R = y[1],
            L = (0, a.useState)(i),
            k = L[0],
            O = L[1],
            I = (0, a.useRef)(null),
            H = (0, a.useCallback)(() => {
              I.current && (I.current.focus(), O(!0));
            }, []),
            Q = (0, a.useCallback)(
              (e) => {
                k && null !== I.current && !I.current.contains(e.target) && O(!1);
              },
              [k],
            );
          ((0, a.useEffect)(
            () => (
              document.addEventListener("mousedown", Q),
              () => {
                document.removeEventListener("mousedown", Q);
              }
            ),
            [Q],
          ),
            (0, a.useEffect)(() => {
              O(i);
            }, [i]));
          const U = (0, a.useCallback)(
              (e) => {
                g && g(e);
              },
              [g],
            ),
            G = (0, a.useCallback)(
              (e) => {
                (w(!0), F && F(e), m && (0, P.G)(m), i && H());
              },
              [i, F, H, m],
            ),
            W = (0, a.useCallback)(
              (e) => {
                (w(!1), B && B(e));
              },
              [B],
            ),
            $ = (0, a.useCallback)(
              (e) => {
                (D && D(e), l && (0, P.G)(l), R(!0));
              },
              [D, l],
            ),
            j = (0, a.useCallback)(
              (e) => {
                (w(!1), R(!1), p && p(e));
              },
              [p],
            ),
            q = (0, a.useCallback)(
              (e) => {
                (O(!0), C && C(e));
              },
              [C],
            ),
            z = (0, a.useCallback)(
              (e) => {
                (O(!1), b && b(e));
              },
              [b],
            ),
            Z = d()(
              x.base,
              n && x.base__visibleLabel,
              v && x.base__mouseDown,
              S && x.base__hovered,
              k && x.base__focused,
              null == A ? void 0 : A.base,
            ),
            X = d()(x.icon, x[`icon__${E}`], null == A ? void 0 : A.icon),
            Y = d()(x.label, null == A ? void 0 : A.label);
          return r().createElement(
            "div",
            T(
              {
                ref: I,
                className: Z,
                onClick: U,
                onMouseEnter: $,
                onMouseLeave: j,
                onMouseDown: G,
                onMouseUp: W,
                onFocus: q,
                onBlur: z,
              },
              f,
            ),
            r().createElement("div", { className: X }),
            r().createElement("div", { className: Y }, u),
          );
        });
        var k = t(3415),
          O = t(3017);
        const I = {
            base: "RewardCard_base_7a",
            base__final: "RewardCard_base__final_cf",
            base__disabled: "RewardCard_base__disabled_58",
            bg: "RewardCard_bg_c6",
            border: "RewardCard_border_b7",
            day: "RewardCard_day_4e",
            reward: "RewardCard_reward_4b",
            finalMain: "RewardCard_finalMain_74",
            base__current: "RewardCard_base__current_dc",
            base__today: "RewardCard_base__today_0a",
            base__completed: "RewardCard_base__completed_9c",
            base__claiming: "RewardCard_base__claiming_0f",
            check: "RewardCard_check_8f",
            claimCheckAppear: "RewardCard_claimCheckAppear_62",
            claimBg: "RewardCard_claimBg_83",
            claimBg__current: "RewardCard_claimBg__current_cb",
            claimBg__today: "RewardCard_claimBg__today_88",
            claimBg__out: "RewardCard_claimBg__out_11",
            fadeOut: "RewardCard_fadeOut_cd",
            claimBg__in: "RewardCard_claimBg__in_f6",
            fadeIn: "RewardCard_fadeIn_3e",
            glow: "RewardCard_glow_86",
            glow__current: "RewardCard_glow__current_41",
            glow__today: "RewardCard_glow__today_96",
            glow__out: "RewardCard_glow__out_da",
            claimGlowOut: "RewardCard_claimGlowOut_98",
            glow__in: "RewardCard_glow__in_bd",
            claimGlowIn: "RewardCard_claimGlowIn_f0",
            disabledOverlay: "RewardCard_disabledOverlay_3c",
            border__current: "RewardCard_border__current_16",
            border__today: "RewardCard_border__today_96",
            border__out: "RewardCard_border__out_ff",
            border__in: "RewardCard_border__in_f9",
            rewards: "RewardCard_rewards_49",
            rewards__final: "RewardCard_rewards__final_76",
            topReward: "RewardCard_topReward_ec",
            bottomRow: "RewardCard_bottomRow_5f",
            finalMainLight: "RewardCard_finalMainLight_32",
            finalMainTooltip: "RewardCard_finalMainTooltip_b1",
            preview: "RewardCard_preview_9e",
            previewButton: "RewardCard_previewButton_5f",
            finalAside: "RewardCard_finalAside_7e",
          },
          H = R.strings.quests.serialEnter.calendar,
          Q = (e, u) => () => {
            e(u);
          },
          U = (e, u, t, a = !0) => {
            var n;
            return r().createElement(m.Q, {
              key: `${e}-${u.name}-${null != (n = u.value) ? n : ""}-${u.image}`,
              name: u.name,
              image: u.image,
              value: u.value,
              valueType: u.valueType,
              tooltipArgs: a ? u.tooltipArgs : void 0,
              size: t,
              className: I.reward,
            });
          },
          G = r().memo(function ({ dayData: e, onPreviewVehicle: u }) {
            var t, a;
            const n = e.day,
              i = e.rewards,
              o = e.isFinal,
              l = e.state,
              c = (0, s.GS)().mediaSize,
              m = g(c),
              p = E.h2.S180x135,
              b = c >= s.cJ.Large ? M.NORMAL : M.SMALL,
              f = h(l),
              v = f.isClaiming,
              w = f.isTodayStyle,
              y = o ? i : i.slice(0, 3),
              S = !o && 3 === y.length,
              R = S ? y[0] : null,
              P = S ? y.slice(1) : y,
              x = B(l) || w || v,
              N = (((e) => F.includes(e))(l) && !w) || v,
              T = w || v,
              G = y[0],
              W =
                null == G || null == (t = G.tooltipArgs) || null == (a = t.args) ? void 0 : a[O.WO],
              $ = Boolean(o && G && A(G.name) && W);
            return r().createElement(
              "div",
              { className: d()(I.base, o && I.base__final, C(I, l, v, w)) },
              v
                ? r().createElement(
                    r().Fragment,
                    null,
                    r().createElement("div", {
                      className: d()(I.claimBg, I.claimBg__today, I.claimBg__in),
                    }),
                    r().createElement("div", {
                      className: d()(I.claimBg, I.claimBg__current, I.claimBg__out),
                    }),
                    r().createElement("div", {
                      className: d()(I.border, I.border__today, I.border__in),
                    }),
                    r().createElement("div", {
                      className: d()(I.border, I.border__current, I.border__out),
                    }),
                  )
                : r().createElement(
                    r().Fragment,
                    null,
                    r().createElement("div", { className: I.bg }),
                    r().createElement("div", { className: I.border }),
                  ),
              l === D.Disabled && r().createElement("div", { className: I.disabledOverlay }),
              T &&
                r().createElement("div", {
                  className: d()(I.glow, I.glow__today, v && I.glow__in),
                }),
              N &&
                r().createElement("div", {
                  className: d()(I.glow, I.glow__current, v && I.glow__out),
                }),
              r().createElement(_.ZP, { className: I.day, text: String(n) }),
              x && r().createElement("div", { className: I.check }),
              r().createElement(
                "div",
                { className: d()(I.rewards, o && I.rewards__final) },
                o && G
                  ? r().createElement(
                      r().Fragment,
                      null,
                      r().createElement(
                        "div",
                        { className: I.finalMain },
                        r().createElement("div", { className: I.finalMainLight }),
                        r().createElement(
                          k.l,
                          { tooltipArgs: G.tooltipArgs, className: I.finalMainTooltip },
                          r().createElement(
                            r().Fragment,
                            null,
                            U(n, G, p, !1),
                            $ &&
                              r().createElement(
                                "div",
                                { className: I.preview },
                                r().createElement(L, {
                                  classNames: { base: I.previewButton },
                                  size: b,
                                  onClick: Q(u, W),
                                  soundClick: "",
                                  isVisibleLabel: !0,
                                  label: H.preview(),
                                }),
                              ),
                          ),
                        ),
                      ),
                      r().createElement(
                        "div",
                        { className: I.finalAside },
                        y.slice(1).map((e) => U(n, e, m)),
                      ),
                    )
                  : r().createElement(
                      r().Fragment,
                      null,
                      R && r().createElement("div", { className: I.topReward }, U(n, R, m)),
                      r().createElement(
                        "div",
                        { className: I.bottomRow },
                        P.map((e) => U(n, e, m)),
                      ),
                    ),
              ),
            );
          });
        var W = t(729),
          $ = t(3215),
          j = t(4598),
          q = t(9480),
          z = t(5175),
          Z = t(3946);
        const X = R.images.gui.maps.icons.daily.calendar.card.rewards,
          Y = ["handExtinguishers", "smallMedkit", "smallRepairkit"],
          V = ["autoExtinguishers", "largeMedkit", "largeRepairkit"],
          K = [Y, V],
          J = new Set(V),
          ee = new Set([...Y, ...V]),
          ue = (e) => {
            const u = e
              .map((e) => e.tooltipId)
              .filter(Boolean)
              .join(",");
            return u
              ? (0, W.pI)(
                  { tooltipIds: u },
                  R.views.lobby.tooltips.AdditionalRewardsTooltip("resId"),
                  { ignoreShowDelay: !0 },
                )
              : {
                  body: e
                    .map((e) => e.label)
                    .filter(Boolean)
                    .join(", "),
                  ignoreShowDelay: !0,
                };
          },
          te = (e, u, t) => {
            const a = new Map();
            return (
              e.forEach((e) => {
                ((e) => e.name === E.E4.Items && void 0 !== e.item && ee.has(e.item))(e) &&
                  e.item &&
                  !a.has(e.item) &&
                  a.set(e.item, e);
              }),
              u.every((e) => a.has(e)) ? { items: u, reward: t(u.map((e) => a.get(e))) } : null
            );
          },
          ae = (e, u) =>
            e.name === E.E4.Vehicles
              ? ((e) => `R.images.gui.maps.shop.vehicles.c_360x270.${e.value}`)(e)
              : (0, W.ry)(e, u),
          re = (e, u = E.h2.Small) => {
            if (null == e || !e.length) return [];
            return ((e, u, t) => {
              const a = K.map((u) => te(e, u, t)).filter((e) => null !== e),
                r = new Set(a.flatMap((e) => e.items)),
                n = e.filter((e) => void 0 === e.item || !r.has(e.item)).map(u);
              return [...a.map((e) => e.reward), ...n];
            })(
              q.map(e, (e) => e),
              (e) =>
                ((e, u) => ({
                  name: e.name,
                  image: ae(e, u),
                  value: A(e.name) ? "" : e.value,
                  valueType: (0, W.p3)(e.name),
                  tooltipArgs: (0, W.pI)({ [O.WO]: e.tooltipId }, Number(e.tooltipContentId), {
                    ignoreShowDelay: !0,
                  }),
                }))(e, u),
              (e) =>
                ((e) => {
                  return {
                    name: E.E4.Items,
                    image:
                      ((u = e[0]),
                      void 0 !== (null == u ? void 0 : u.item) && J.has(u.item)
                        ? X.combinedRewardsBig()
                        : X.combinedRewards()),
                    value: "",
                    valueType: E.$h.MULTI,
                    tooltipArgs: ue(e),
                    isCombined: !0,
                  };
                  var u;
                })(e),
            );
          },
          ne = (0, $.q)()(
            ({ observableModel: e }) => {
              const u = { root: e.object(), days: e.array("days", []) },
                t = (0, Z.Om)(
                  (e = E.h2.Small) =>
                    (0, z.c)(u.days.get()).map((u) => ({
                      day: u.day,
                      state: u.state,
                      isFinal: u.isFinal,
                      rewards: re(u.bonuses, e),
                    })),
                  { equals: j.jv },
                );
              return Object.assign({}, u, { computes: { getDays: t } });
            },
            ({ externalModel: e }) => ({
              onPreviewVehicle: e.createCallback((e) => ({ tooltipId: e }), "onPreviewVehicle"),
            }),
          ),
          se = ne[0],
          ie = ne[1],
          oe = (0, n.Pi)(function () {
            const e = ie(),
              u = e.model,
              t = e.controls,
              n = g((0, s.GS)().mediaSize),
              c = u.computes.getDays(n),
              d = (0, a.useMemo)(() => {
                if (!c.length) return { headerDay: void 0, fullRowsDays: [], lastRowDays: [] };
                const e = c[0],
                  u = c.slice(1),
                  t = u.filter((e) => !e.isFinal),
                  a = u.filter((e) => e.isFinal);
                return {
                  headerDay: e,
                  fullRowsDays: t.slice(0, 10),
                  lastRowDays: [...t.slice(10), ...a],
                };
              }, [c]),
              m = d.headerDay,
              _ = d.fullRowsDays,
              E = d.lastRowDays;
            return m
              ? r().createElement(
                  "div",
                  { className: i },
                  r().createElement(S, { dayData: m }),
                  r().createElement(
                    "div",
                    { className: o },
                    _.map((e) =>
                      r().createElement(G, {
                        key: e.day,
                        dayData: e,
                        onPreviewVehicle: t.onPreviewVehicle,
                      }),
                    ),
                  ),
                  r().createElement(
                    "div",
                    { className: l },
                    E.map((e) =>
                      r().createElement(G, {
                        key: e.day,
                        dayData: e,
                        onPreviewVehicle: t.onPreviewVehicle,
                      }),
                    ),
                  ),
                )
              : null;
          }),
          le = (0, a.memo)(function (e) {
            const u = (0, a.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
            return r().createElement(se, { options: u }, r().createElement(oe, null));
          });
      },
      6970: (e, u, t) => {
        "use strict";
        t.d(u, { i$: () => r, ul: () => a });
        const a = 1e3,
          r = Math.max(800, 700);
      },
      9922: (e, u, t) => {
        "use strict";
        t.d(u, { q: () => F });
        var a = t(6483),
          r = t.n(a),
          n = t(7613),
          s = t(2056),
          i = t(7727),
          o = t(8515),
          l = t(6179),
          c = t.n(l);
        const d = "RerollButton_base_7a",
          m = "RerollButton_base__disabled_2e",
          _ = "RerollButton_iconWrapper_19",
          E = "RerollButton_icon_62",
          A = "RerollButton_iconHover_e2",
          g = "RerollButton_iconDisabled_8f",
          D = "RerollButton_text_0b",
          p = "RerollButton_shine_75",
          F = (0, o.Pi)(({ canReroll: e, onReroll: u, rerollPremium: t, className: a }) =>
            c().createElement(
              s.u,
              {
                ignoreMouseClick: !e,
                contentId: R.views.lobby.daily.tooltips.RerollTooltip("resId"),
                args: { rerollPremium: t },
              },
              c().createElement(
                "div",
                {
                  className: r()(d, a, !e && m),
                  onClick: e ? u : void 0,
                  onMouseEnter: e ? () => (0, i.G)(R.sounds.highlight()) : void 0,
                },
                c().createElement(
                  "div",
                  { className: _ },
                  e
                    ? c().createElement(
                        c().Fragment,
                        null,
                        c().createElement("div", { className: E }),
                        c().createElement("div", { className: A }),
                        c().createElement("div", { className: p }),
                      )
                    : c().createElement("div", { className: g }),
                ),
                c().createElement(n.ZP, {
                  className: D,
                  text: R.strings.quests.dailyQuests.body.reroll(),
                }),
              ),
            ),
          );
      },
      8975: (e, u, t) => {
        "use strict";
        t.d(u, { q: () => H });
        var a = t(6483),
          r = t.n(a),
          n = t(6179),
          s = t.n(n);
        const i = "DailyQuestsTab_base_fd",
          o = "DailyQuestsTab_base__selected_83",
          l = "DailyQuestsTab_bg_ed",
          c = "DailyQuestsTab_hoverBg_a8",
          d = "DailyQuestsTab_selectedBg_25",
          m = "DailyQuestsTab_disabledBg_6c",
          _ = "DailyQuestsTab_premBg_16",
          E = "DailyQuestsTab_base__hover_d3",
          A = "DailyQuestsTab_base__completed_3f",
          g = "DailyQuestsTab_base__notEnabled_eb",
          D = "DailyQuestsTab_contentWrapper_5b",
          p = "DailyQuestsTab_base__unlock_34",
          F = "DailyQuestsTab_iconWrapper_da",
          B = "DailyQuestsTab_icon_40",
          C = "DailyQuestsTab_status_fe",
          b = "DailyQuestsTab_status__lock_ae",
          f = "DailyQuestsTab_status__alert_43",
          h = "DailyQuestsTab_status__check_15",
          v = "DailyQuestsTab_progress_2c",
          w = "DailyQuestsTab_current_8e",
          y = "DailyQuestsTab_separator_79",
          S = "DailyQuestsTab_rightBlockWrapper_22",
          P = "DailyQuestsTab_bubble_5f",
          x = "DailyQuestsTab_title_3d",
          N = "DailyQuestsTab_description_78",
          T = "DailyQuestsTab_bull_be";
        var M = t(7727),
          L = t(7613),
          k = t(122),
          O = t(2344),
          I = t(3509);
        const H = ({
          tabIdx: e,
          isEnabled: u,
          isSelected: t,
          isCompleted: a,
          isPremium: H,
          hasPremium: Q,
          icon: U = "win",
          current: G,
          total: W,
          bubbleCounter: $,
          title: j,
          description: q,
          onClick: z,
        }) => {
          var Z;
          const X = null != (Z = (0, O.D9)(Q)) ? Z : Q,
            Y = (0, n.useState)(!1),
            V = Y[0],
            K = Y[1],
            J = (0, n.useState)(!1),
            ee = J[0],
            ue = J[1],
            te = (0, n.useState)(Q),
            ae = te[0],
            re = te[1],
            ne = H && !ae,
            se = !u || ne,
            ie = !u || ne || a;
          ((0, n.useEffect)(() => {
            !X && Q && ue(!0);
          }, [X, Q]),
            (0, n.useEffect)(() => {
              if (ee)
                return (
                  re(!1),
                  (0, k.F)(() => {
                    (ue(!1), re(!0));
                  }, I.ji.unlockTabPremiumDuration)
                );
              re(Q);
            }, [ee, Q]));
          const oe = (0, n.useCallback)(() => {
              t || (M.$.playHighlight(), K(!0));
            }, [t]),
            le = (0, n.useCallback)(() => {
              t || K(!1);
            }, [t]),
            ce = (0, n.useCallback)(() => {
              (M.$.playClick(), z(e), K(!1));
            }, [z, e]);
          return s().createElement(
            "div",
            {
              className: r()(i, V && E, t && o, u && a && A, !u && g, ee && p),
              onMouseEnter: oe,
              onMouseLeave: le,
              onClick: ce,
            },
            s().createElement("div", { className: l }),
            s().createElement("div", { className: c }),
            s().createElement("div", { className: d }),
            H && s().createElement("div", { className: _ }),
            se && s().createElement("div", { className: m }),
            s().createElement(
              "div",
              { className: D },
              Boolean($) && s().createElement(L.ZP, { className: P, text: $.toString() }),
              s().createElement(
                "div",
                { className: F },
                ie
                  ? s().createElement("div", { className: r()(C, ne && b, !u && f, a && h) })
                  : s().createElement("div", {
                      className: B,
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.missions.icons.c_48_${U}_silver)`,
                      },
                    }),
              ),
              s().createElement("div", { className: y }),
              s().createElement(
                "div",
                { className: S },
                s().createElement(
                  "div",
                  { className: x },
                  s().createElement(L.ZP, { text: j }),
                  u &&
                    s().createElement(L.ZP, {
                      text: R.strings.quests.dailyQuests.tab.progress(),
                      format: {
                        binding: {
                          current: s().createElement(L.ZP, {
                            text: G.toString(),
                            className: r()(G > 0 && w),
                          }),
                          total: s().createElement(L.ZP, { text: W.toString() }),
                        },
                      },
                      className: v,
                    }),
                ),
                s().createElement(
                  "div",
                  { className: N },
                  !ie &&
                    s().createElement(L.ZP, {
                      text: R.strings.quests.dailyQuests.tab.bull(),
                      className: T,
                    }),
                  s().createElement(L.ZP, { text: q }),
                ),
              ),
            ),
          );
        };
      },
      3509: (e, u, t) => {
        "use strict";
        t.d(u, { ji: () => r, vW: () => a });
        const a = 3,
          r = {
            unlockSubscriptionBonusDuration: 2e3,
            unlockBonusQuestDelay: 3e3,
            unlockBonusQuestDuration: 500,
            unlockTabPremiumDuration: 700,
          };
      },
      9153: (e, u, t) => {
        "use strict";
        let a;
        (t.d(u, { g: () => a }),
          (function (e) {
            ((e[(e.DailyQuests = 0)] = "DailyQuests"),
              (e[(e.PremiumQuests = 1)] = "PremiumQuests"),
              (e[(e.SerialEnter = 2)] = "SerialEnter"));
          })(a || (a = {})));
      },
      3099: (e, u, t) => {
        "use strict";
        let a;
        (t.d(u, { N: () => a }),
          (function (e) {
            ((e.Done = "done"),
              (e.UndoneSubscription = "undoneSubscription"),
              (e.Locked = "notAvailable"),
              (e.Active = ""));
          })(a || (a = {})));
      },
      5026: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
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
      5287: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        const a = { base: "FormatText_base_d0" };
      },
      1609: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        const a = {
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
        };
      },
      3393: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
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
    var u = __webpack_module_cache__[e];
    if (void 0 !== u) return u.exports;
    var t = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](t, t.exports, __webpack_require__), t.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, u, t, a) => {
      if (!u) {
        var r = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [u, t, a] = deferred[o], n = !0, s = 0; s < u.length; s++)
            (!1 & a || r >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[s]))
              ? u.splice(s--, 1)
              : ((n = !1), a < r && (r = a));
          if (n) {
            deferred.splice(o--, 1);
            var i = t();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      a = a || 0;
      for (var o = deferred.length; o > 0 && deferred[o - 1][2] > a; o--)
        deferred[o] = deferred[o - 1];
      deferred[o] = [u, t, a];
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
    (__webpack_require__.j = 982),
    (() => {
      var e = { 982: 0, 306: 0, 83: 0, 800: 0, 444: 0, 446: 0, 815: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var a,
            r,
            [n, s, i] = t,
            o = 0;
          if (n.some((u) => 0 !== e[u])) {
            for (a in s) __webpack_require__.o(s, a) && (__webpack_require__.m[a] = s[a]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); o < n.length; o++)
            ((r = n[o]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [272], () => __webpack_require__(6892));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
