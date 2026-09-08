(() => {
  var __webpack_modules__ = {
      3457: (e, u, t) => {
        "use strict";
        t.d(u, { L$: () => l.L, qE: () => l.q, u5: () => _ });
        var r = t(6483),
          a = t.n(r),
          n = t(7727),
          s = t(6179),
          i = t.n(s),
          o = t(6880),
          l = t(2106);
        const c = ({
          children: e,
          size: u,
          isFocused: t,
          type: r,
          disabled: c,
          mixClass: _,
          soundHover: E,
          soundClick: m,
          onMouseEnter: d,
          onMouseMove: A,
          onMouseDown: D,
          onMouseUp: F,
          onMouseLeave: g,
          onClick: C,
        }) => {
          const p = (0, s.useRef)(null),
            B = (0, s.useState)(t),
            h = B[0],
            f = B[1],
            v = (0, s.useState)(!1),
            b = v[0],
            w = v[1],
            y = (0, s.useState)(!1),
            S = y[0],
            x = y[1],
            T = (0, s.useCallback)(() => {
              c || (p.current && (p.current.focus(), f(!0)));
            }, [c]),
            P = (0, s.useCallback)(
              (e) => {
                h && null !== p.current && !p.current.contains(e.target) && f(!1);
              },
              [h],
            ),
            M = (0, s.useCallback)(
              (e) => {
                c || (C && C(e));
              },
              [c, C],
            ),
            k = (0, s.useCallback)(
              (e) => {
                c || (null !== E && (0, n.G)(E), d && d(e), x(!0));
              },
              [c, E, d],
            ),
            L = (0, s.useCallback)(
              (e) => {
                A && A(e);
              },
              [A],
            ),
            N = (0, s.useCallback)(
              (e) => {
                c || (F && F(e), w(!1));
              },
              [c, F],
            ),
            O = (0, s.useCallback)(
              (e) => {
                c || (null !== m && (0, n.G)(m), D && D(e), t && T(), w(!0));
              },
              [c, m, D, T, t],
            ),
            I = (0, s.useCallback)(
              (e) => {
                c || (g && g(e), w(!1));
              },
              [c, g],
            ),
            H = a()(
              o.Z.base,
              o.Z[`base__${r}`],
              {
                [o.Z.base__disabled]: c,
                [o.Z[`base__${u}`]]: u,
                [o.Z.base__focus]: h,
                [o.Z.base__highlightActive]: b,
                [o.Z.base__firstHover]: S,
              },
              _,
            ),
            U = a()(o.Z.state, o.Z.state__default);
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
              f(t);
            }, [t]),
            i().createElement(
              "div",
              {
                ref: p,
                className: H,
                onMouseEnter: k,
                onMouseMove: L,
                onMouseUp: N,
                onMouseDown: O,
                onMouseLeave: I,
                onClick: M,
              },
              r !== l.L.ghost &&
                i().createElement(
                  i().Fragment,
                  null,
                  i().createElement("div", { className: o.Z.back }),
                  i().createElement("span", { className: o.Z.texture }),
                ),
              i().createElement(
                "span",
                { className: U },
                i().createElement("span", { className: o.Z.stateDisabled }),
                i().createElement("span", { className: o.Z.stateHighlightHover }),
                i().createElement("span", { className: o.Z.stateHighlightActive }),
              ),
              i().createElement(
                "span",
                { className: o.Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        c.defaultProps = {
          type: l.L.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const _ = (0, s.memo)(c);
      },
      2106: (e, u, t) => {
        "use strict";
        let r, a;
        (t.d(u, { L: () => r, q: () => a }),
          (function (e) {
            ((e.main = "main"),
              (e.primary = "primary"),
              (e.primaryGreen = "primaryGreen"),
              (e.primaryRed = "primaryRed"),
              (e.secondary = "secondary"),
              (e.ghost = "ghost"));
          })(r || (r = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(a || (a = {})));
      },
      2372: (e, u, t) => {
        "use strict";
        t.d(u, { A: () => s });
        var r = t(6179),
          a = t.n(r),
          n = t(4179);
        class s extends a().PureComponent {
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
        var r = t(6179),
          a = t.n(r),
          n = t(6483),
          s = t.n(n),
          i = t(3649),
          o = t(5287);
        const l = ({ binding: e, text: u = "", classMix: t, alignment: n = i.v2.left }) =>
          null === u
            ? (console.error("FormatText was supplied with 'null'"), null)
            : a().createElement(
                r.Fragment,
                null,
                u.split("\n").map((u, l) =>
                  a().createElement(
                    "div",
                    { className: s()(o.Z.base, t), key: `${u}-${l}` },
                    (0, i.Uw)(u, n, e).map((e, u) =>
                      a().createElement(r.Fragment, { key: `${u}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, u, t) => {
        "use strict";
        t.d(u, { Y: () => _ });
        var r = t(3138),
          a = t(6179),
          n = t(1043),
          s = t(5262);
        const i = r.O.client.getSize("rem"),
          o = i.width,
          l = i.height,
          c = Object.assign({ width: o, height: l }, (0, s.T)(o, l, n.j)),
          _ = (0, a.createContext)(c);
      },
      1039: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => c });
        var r = t(6179),
          a = t.n(r),
          n = t(6536),
          s = t(3495),
          i = t(1043),
          o = t(5262),
          l = t(3138);
        const c = (0, r.memo)(({ children: e }) => {
          const u = (0, r.useContext)(s.Y),
            t = (0, r.useState)(u),
            c = t[0],
            _ = t[1],
            E = (0, r.useCallback)((e, u) => {
              const t = l.O.view.pxToRem(e),
                r = l.O.view.pxToRem(u);
              _(Object.assign({ width: t, height: r }, (0, o.T)(t, r, i.j)));
            }, []);
          ((0, n.Z)(() => {
            engine.on("clientResized", E);
          }),
            (0, r.useEffect)(() => () => engine.off("clientResized", E), [E]));
          const m = (0, r.useMemo)(() => Object.assign({}, c), [c]);
          return a().createElement(s.Y.Provider, { value: m }, e);
        });
      },
      6010: (e, u, t) => {
        "use strict";
        var r = t(6179),
          a = t(7382),
          n = t(3495);
        const s = ["children"];
        const i = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                a = {},
                n = Object.keys(e);
              for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, s);
          const i = (0, r.useContext)(n.Y),
            o = i.extraLarge,
            l = i.large,
            c = i.medium,
            _ = i.small,
            E = i.extraSmall,
            m = i.extraLargeWidth,
            d = i.largeWidth,
            A = i.mediumWidth,
            D = i.smallWidth,
            F = i.extraSmallWidth,
            g = i.extraLargeHeight,
            C = i.largeHeight,
            p = i.mediumHeight,
            B = i.smallHeight,
            h = i.extraSmallHeight,
            f = { extraLarge: g, large: C, medium: p, small: B, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && o) return u;
            if (t.large && l) return u;
            if (t.medium && c) return u;
            if (t.small && _) return u;
            if (t.extraSmall && E) return u;
          } else {
            if (t.extraLargeWidth && m) return (0, a.H)(u, t, f);
            if (t.largeWidth && d) return (0, a.H)(u, t, f);
            if (t.mediumWidth && A) return (0, a.H)(u, t, f);
            if (t.smallWidth && D) return (0, a.H)(u, t, f);
            if (t.extraSmallWidth && F) return (0, a.H)(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && g) return u;
              if (t.largeHeight && C) return u;
              if (t.mediumHeight && p) return u;
              if (t.smallHeight && B) return u;
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
        t.d(u, { YN: () => a.Y, ZN: () => r.Z });
        t(6010);
        var r = t(1039),
          a = t(3495);
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
        function a(e, u, t) {
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
            a = (function (e, u) {
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
            n = Math.min(r, a);
          return {
            extraLarge: n === t.extraLarge.weight,
            large: n === t.large.weight,
            medium: n === t.medium.weight,
            small: n === t.small.weight,
            extraSmall: n === t.extraSmall.weight,
            extraLargeWidth: r === t.extraLarge.weight,
            largeWidth: r === t.large.weight,
            mediumWidth: r === t.medium.weight,
            smallWidth: r === t.small.weight,
            extraSmallWidth: r === t.extraSmall.weight,
            extraLargeHeight: a === t.extraLarge.weight,
            largeHeight: a === t.large.weight,
            mediumHeight: a === t.medium.weight,
            smallHeight: a === t.small.weight,
            extraSmallHeight: a === t.extraSmall.weight,
          };
        }
        (t.d(u, { T: () => a }),
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
      5739: (e, u, t) => {
        "use strict";
        t.d(u, { Q: () => _ });
        var r = t(6483),
          a = t.n(r),
          n = t(6179),
          s = t.n(n),
          i = t(3415),
          o = t(2862),
          l = t(729),
          c = t(1609);
        const _ = ({
          name: e,
          image: u,
          isPeriodic: t = !1,
          size: r = o.h2.Big,
          special: n,
          value: _,
          valueType: E,
          style: m,
          className: d,
          classNames: A,
          tooltipArgs: D,
          periodicIconTooltipArgs: F,
        }) => {
          const g = (0, l.L_)(n),
            C = (0, l.i2)(n),
            p = (0, l.m9)(_, E);
          return s().createElement(
            "div",
            { className: a()(c.Z.base, c.Z[`base__${r}`], d), style: m },
            s().createElement(
              i.l,
              { tooltipArgs: D, className: c.Z.tooltipWrapper },
              s().createElement(
                s().Fragment,
                null,
                s().createElement(
                  "div",
                  { className: a()(c.Z.image, null == A ? void 0 : A.image) },
                  g &&
                    s().createElement("div", {
                      className: a()(c.Z.highlight, null == A ? void 0 : A.highlight),
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${r}.${g}_highlight)`,
                      },
                    }),
                  u &&
                    s().createElement("div", {
                      className: a()(c.Z.icon, null == A ? void 0 : A.rewardIcon),
                      style: { backgroundImage: `url(${u})` },
                    }),
                  C &&
                    s().createElement("div", {
                      className: a()(c.Z.overlay, null == A ? void 0 : A.overlay),
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${r}.${C}_overlay)`,
                      },
                    }),
                ),
                p &&
                  s().createElement(
                    "div",
                    {
                      className: a()(
                        c.Z.info,
                        c.Z[`info__${e}`],
                        E === o.$h.MULTI && c.Z.info__multi,
                        null == A ? void 0 : A.info,
                      ),
                    },
                    p,
                  ),
              ),
            ),
            t &&
              s().createElement(
                i.l,
                { tooltipArgs: F },
                s().createElement("div", {
                  className: a()(c.Z.timer, null == A ? void 0 : A.periodicIcon),
                }),
              ),
          );
        };
      },
      2862: (e, u, t) => {
        "use strict";
        let r, a, n, s, i, o, l, c, _;
        (t.d(u, {
          $h: () => s,
          A2: () => o,
          E4: () => r,
          h2: () => n,
          kK: () => i,
          sh: () => l,
          ye: () => _,
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
          })(a || (a = {})),
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
          })(_ || (_ = {})));
      },
      729: (e, u, t) => {
        "use strict";
        t.d(u, { L_: () => F, i2: () => g, m9: () => C, p3: () => E, pI: () => D, ry: () => A });
        var r = t(2372),
          a = t(6179),
          n = t.n(a),
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
            s.E4.WtStamp,
            s.E4.WtTicket,
            s.E4.WtMainPrizeDiscount,
            s.E4.WtHunter,
            s.E4.WtHunterCollection,
          ],
          o = [s.E4.Gold, s.E4.Credits, s.E4.Crystal, s.E4.FreeXp],
          l = [s.E4.BattlePassPoints],
          c = [s.E4.PremiumPlus, s.E4.Premium];
        let _;
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
        })(_ || (_ = {}));
        const E = (e) =>
            i.includes(e)
              ? s.$h.MULTI
              : o.includes(e)
                ? s.$h.CURRENCY
                : l.includes(e)
                  ? s.$h.NUMBER
                  : c.includes(e)
                    ? s.$h.PREMIUM_PLUS
                    : s.$h.STRING,
          m = ["engravings", "backgrounds"],
          d = ["engraving", "background"],
          A = (e, u = s.h2.Small) => {
            const t = e.name,
              r = e.type,
              a = e.value,
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
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${r}_${a}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${a}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${a}`;
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
                  const r = m[e];
                  if (r) {
                    const a = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(r),
                      n = a.$dyn(t);
                    return n ? `${n}` : `${a.$dyn(d[e])}`;
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
                      return _.s32;
                    case s.h2.Small:
                    case s.h2.S48x48:
                      return _.s48;
                    case s.h2.S80x80:
                    case s.h2.Big:
                      return _.s80;
                    case s.h2.S128x100:
                      return _.s116;
                    case s.h2.S180x135:
                    case s.h2.S232x174:
                    case s.h2.S296x222:
                      return _.s296;
                    case s.h2.S400x300:
                      return _.s400;
                    case s.h2.S600x450:
                      return _.s600;
                  }
                })(u)}`;
              case s.E4.StyleProgress:
              case s.E4.LbStyleProgress:
                return p(n, u, s.ye.ProgressionStyle);
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
              case s.kK.BATTLE_BOOSTER:
              case s.kK.BATTLE_BOOSTER_REPLACE:
                return s.A2.BATTLE_BOOSTER;
            }
          },
          g = (e) => {
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
          C = (e, u) => {
            if (void 0 === e) return null;
            switch (u) {
              case s.$h.MULTI: {
                const u = Number(e);
                return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
              }
              case s.$h.CURRENCY:
              case s.$h.NUMBER:
                return n().createElement(r.A, { format: "integral", value: Number(e) });
              case s.$h.PREMIUM_PLUS: {
                const u = Number(e);
                return isNaN(u) ? e : null;
              }
              default:
                return e;
            }
          },
          p = (e, u, t) => {
            const r = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              a = r.$dyn(e);
            return String(null != a ? a : r.$dyn(t));
          };
      },
      7078: (e, u, t) => {
        "use strict";
        t.d(u, { t: () => o });
        var r = t(6179),
          a = t.n(r),
          n = t(2056);
        const s = ["children"];
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
                a = {},
                n = Object.keys(e);
              for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, s);
          return a().createElement(
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
        var r = t(6179),
          a = t.n(r),
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
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const l = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const r = a().createElement("div", { className: t }, e);
          if (u.header || u.body) return a().createElement(s.i, u, r);
          const l = u.contentId,
            c = u.args,
            _ = null == c ? void 0 : c.contentId;
          return l || _
            ? a().createElement(i.u, o({}, u, { contentId: l || _ }), r)
            : a().createElement(n.t, u, r);
        };
      },
      6373: (e, u, t) => {
        "use strict";
        t.d(u, { i: () => l });
        var r = t(2056),
          a = t(6179),
          n = t.n(a);
        const s = ["children", "body", "header", "note", "alert", "args"];
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
              _ = e.alert,
              E = e.args,
              m = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  a = {},
                  n = Object.keys(e);
                for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, s);
            const d = (0, a.useMemo)(() => {
              const e = Object.assign({}, E, { body: t, header: l, note: c, alert: _ });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [_, t, l, c, E]);
            return n().createElement(
              r.u,
              i(
                {
                  contentId:
                    ((A = null == E ? void 0 : E.hasHtmlContent),
                    A ? o.SimpleTooltipHtmlContent("resId") : o.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: d,
                },
                m,
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
          a = t(4179),
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
        const o = (e, u, t = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: a.B0.TOOLTIP,
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
              a = e.args,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              _ = e.onMouseDown,
              E = e.onClick,
              m = e.ignoreShowDelay,
              d = void 0 !== m && m,
              A = e.ignoreMouseClick,
              D = void 0 !== A && A,
              F = e.decoratorId,
              g = void 0 === F ? 0 : F,
              C = e.isEnabled,
              p = void 0 === C || C,
              B = e.targetId,
              h = void 0 === B ? 0 : B,
              f = e.onShow,
              v = e.onHide,
              b = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  a = {},
                  n = Object.keys(e);
                for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, s);
            const w = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              y = (0, n.useMemo)(() => h || (0, r.F)().resId, [h]),
              S = (0, n.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (o(t, g, { isMouseEvent: !0, on: !0, arguments: i(a) }, y),
                  f && f(),
                  (w.current.isVisible = !0));
              }, [t, g, a, y, f]),
              R = (0, n.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    o(t, g, { on: !1 }, y),
                    w.current.isVisible && v && v(),
                    (w.current.isVisible = !1));
                }
              }, [t, g, y, v]),
              x = (0, n.useCallback)((e) => {
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
                document.addEventListener("wheel", x, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", x, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === p && R();
              }, [p, R]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", R),
                  () => {
                    (window.removeEventListener("mouseleave", R), R());
                  }
                ),
                [R],
              ));
            return p
              ? (0, n.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((T = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(S, d ? 100 : 400)),
                            l && l(e),
                            T && T(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (R(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === D && R(), null == E || E(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === D && R(), null == _ || _(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    b,
                  ),
                )
              : u;
            var T;
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
        t.d(u, { u: () => r });
        const r = (e, u, t) => (t < e ? e : t > u ? u : t);
      },
      1856: (e, u, t) => {
        "use strict";
        t.d(u, { v: () => r });
        const r = (e) => {
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
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => i, onResize: () => n }));
        var r = t(2472),
          a = t(1176);
        const n = (0, r.E)("clientResized"),
          s = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, a.R)(!1);
          }
          function t() {
            e.enabled && (0, a.R)(!0);
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
              : (0, a.R)(!1);
          }
          const n = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let a = !0;
                  const n = `mouse${u}`,
                    i = s[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(n, o),
                    r(),
                    () => {
                      a &&
                        (i(), window.removeEventListener(n, o), (e.listeners -= 1), r(), (a = !1));
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
              ((e.enabled = !1), r());
            },
            enable() {
              ((e.enabled = !0), r());
            },
            enableOutside() {
              e.enabled && (0, a.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, a.R)(!1);
            },
          });
        })();
      },
      5959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => r,
            getMouseGlobalPosition: () => n,
            getSize: () => a,
            graphicsQuality: () => s,
          }));
        var r = t(527);
        function a(e = "px") {
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
        t.d(u, { O: () => a });
        var r = t(5959);
        const a = { view: t(7641), client: r };
      },
      3722: (e, u, t) => {
        "use strict";
        function r(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function a(e, u, t) {
          return `url(${r(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => a, getTextureUrl: () => r }));
      },
      6112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => r });
        const r = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => a });
        var r = t(2472);
        const a = {
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
            displayStatus: () => a.W,
            displayStatusIs: () => w,
            events: () => n.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => b,
            getScale: () => D,
            getSize: () => E,
            getViewGlobalPosition: () => d,
            isClientAccessible: () => B,
            isEventHandled: () => f,
            isFocused: () => p,
            pxToRem: () => F,
            remToPx: () => g,
            resize: () => m,
            sendEvent: () => s.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => h,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => _,
            whenTutorialReady: () => S,
          }));
        var r = t(3722),
          a = t(6112),
          n = t(6538),
          s = t(8566);
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
        function _(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function E(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function d(e = "rem") {
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
        function C(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function p() {
          return viewEnv.isFocused();
        }
        function B() {
          return viewEnv.isClientAccessible();
        }
        function h() {
          return viewEnv.setEventHandled();
        }
        function f() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function b() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(a.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === a.W[u]), e),
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
        const r = ["args"];
        const a = 2,
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
                    r,
                    a = {},
                    n = Object.keys(e);
                  for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, r);
              return void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, s, {
                      arguments:
                        ((a = n),
                        Object.entries(a).map(([e, u]) => {
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
            var a;
          },
          l = {
            close(e) {
              o("popover" === e ? a : s);
            },
            minimize() {
              o(i);
            },
            move(e) {
              o(n, { isMouseEvent: !0, on: e });
            },
          };
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
      6536: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        var r = t(6179);
        const a = (e) => {
          const u = (0, r.useRef)(!1);
          u.current || (e(), (u.current = !0));
        };
      },
      3815: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => n });
        var r = t(6179);
        const a = [];
        function n(e) {
          const u = (0, r.useRef)(e);
          return (
            (0, r.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, r.useCallback)((...e) => (0, u.current)(...e), a)
          );
        }
      },
      5415: (e, u, t) => {
        "use strict";
        t.d(u, { Aq: () => o, GS: () => l, cJ: () => s, fd: () => i });
        var r = t(6179),
          a = t(7739),
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
          const e = (0, r.useContext)(a.YN),
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
      5521: (e, u, t) => {
        "use strict";
        let r, a;
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
          })(a || (a = {})));
      },
      9480: (e, u, t) => {
        "use strict";
        t.d(u, {
          DZ: () => _,
          G: () => o,
          U2: () => a,
          UI: () => i,
          hX: () => l,
          sE: () => c,
          v: () => E,
        });
        var r = t(8968);
        function a(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        const n = a;
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
            : e.map((e, t, r) => u(null == e ? void 0 : e.value, t, r));
        }
        function o(e, u) {
          if (Array.isArray(e)) return e.some(u);
          for (let t = 0; t < e.length; t++) {
            if (u(n(e, t), t, e)) return !0;
          }
          return !1;
        }
        function l(e, u) {
          if (Array.isArray(e)) return e.filter(u);
          const t = [];
          for (let a = 0; a < e.length; a++) {
            var r;
            const n = null == (r = e[a]) ? void 0 : r.value;
            u(n, a, e) && t.push(n);
          }
          return t;
        }
        function c(e, u) {
          for (let t = 0; t < e.length; t++) {
            const r = s(e[t]);
            if (u(r, t, e)) return r;
          }
        }
        function _(e, u, t) {
          const r = [];
          for (let a = 0; a < e.length; a++) {
            const s = n(e, a);
            u(s, a, e) && r.push(t(s, a, e));
          }
          return r;
        }
        function E(e, u) {
          return _(e, r.C, u);
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
        t.d(u, { $: () => a, G: () => r });
        const a = {
          playHighlight() {
            r("highlight");
          },
          playClick() {
            r("play");
          },
          playYes() {
            r("yes1");
          },
        };
      },
      3649: (e, u, t) => {
        "use strict";
        let r;
        function a(e, u) {
          return e.replace(/\{\w+\}/g, (e) => String(u[e.slice(1, -1)]));
        }
        function n(e, u) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const t = 0 === e.indexOf("%") ? 2 : 1;
            return String(u[e.slice(t, -t)]);
          });
        }
        (t.d(u, { Uw: () => E, WU: () => a, uF: () => n, v2: () => r }),
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
          i = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          o = (e, u, t = r.left) => e.split(u).reduce(t === r.left ? s : i, []),
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
            return (u) =>
              u
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(e);
          })(),
          c = ["zh_cn", "zh_sg", "zh_tw"],
          _ = (e, u = r.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return c.includes(t)
              ? l(e)
              : ((e, u = r.left) => {
                  let t = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (o(n, /( )/, u).forEach((e) => (t = t.concat(o(e, a, r.left)))), t);
                })(e, u);
          },
          E = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : _(e, u)));
      },
      1358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        var r = t(3138);
        class a {
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
            return (window.__dataTracker || (window.__dataTracker = new a()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const n = r.O.view.addModelObserver(e, t, a);
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
              const r = this._callbacks[t];
              void 0 !== r && r(e, u);
            });
          }
        }
        a.__instance = void 0;
        const n = a;
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
        t.d(u, { Sw: () => n.Z, B3: () => l, Z5: () => s, B0: () => o, ry: () => g, Eu: () => C });
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
        const a = r;
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
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = t(5521),
          d = t(3138);
        const A = ["args"];
        function D(e, u, t, r, a, n, s) {
          try {
            var i = e[n](s),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(r, a);
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
                  return new Promise(function (r, a) {
                    var n = e.apply(u, t);
                    function s(e) {
                      D(n, r, a, s, i, "next", e);
                    }
                    function i(e) {
                      D(n, r, a, s, i, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          C = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          p = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                n = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    a = {},
                    n = Object.keys(e);
                  for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, A);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, n, {
                      arguments:
                        ((r = a),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, n));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var r;
          },
          B = () => p(o.CLOSE),
          h = (e, u) => {
            e.keyCode === m.n.ESCAPE && u();
          };
        var f = t(7572);
        const v = a.instance,
          b = {
            DataTracker: n.Z,
            ViewModel: f.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: _,
            DateFormatType: E,
            makeGlobalBoundingBox: F,
            sendMoveEvent: (e) => p(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: B,
            sendClosePopOverEvent: () => p(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              p(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, r, a = R.invalid("resId"), n) => {
              const s = d.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                _ = i.width,
                E = i.height,
                m = {
                  x: d.O.view.pxToRem(l) + s.x,
                  y: d.O.view.pxToRem(c) + s.y,
                  width: d.O.view.pxToRem(_),
                  height: d.O.view.pxToRem(E),
                };
              p(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: r || R.invalid("resId"),
                targetID: a,
                direction: u,
                bbox: F(m),
                on: !0,
                args: n,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => h(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              h(e, B);
            },
            handleViewEvent: p,
            onBindingsReady: g,
            onLayoutReady: C,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(o.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(o.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(o.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const r in u)
                if (Object.prototype.hasOwnProperty.call(u, r)) {
                  const a = Object.prototype.toString.call(u[r]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = u[r];
                    t[r] = [];
                    for (let u = 0; u < a.length; u++) t[r].push({ value: e(a[u].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[r] = e(u[r]))
                      : (t[r] = u[r]);
                }
              return t;
            },
            ClickOutsideManager: v,
            SystemLocale: s,
            UserLocale: i,
          };
        window.ViewEnvHelper = b;
      },
      9334: (e, u, t) => {
        "use strict";
        var r = t(7739),
          a = t(6179),
          n = t.n(a),
          s = t(6483),
          i = t.n(s),
          o = t(926),
          l = t.n(o),
          c = t(5415);
        const _ = ["children", "className"];
        function E() {
          return (
            (E =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            E.apply(this, arguments)
          );
        }
        const m = {
            [c.fd.ExtraSmall]: "",
            [c.fd.Small]: l().SMALL_WIDTH,
            [c.fd.Medium]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH}`,
            [c.fd.Large]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH}`,
            [c.fd.ExtraLarge]:
              `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH} ${l().EXTRA_LARGE_WIDTH}`,
          },
          d = {
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
          D = (e) => {
            let u = e.children,
              t = e.className,
              r = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  a = {},
                  n = Object.keys(e);
                for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, _);
            const a = (0, c.GS)(),
              s = a.mediaWidth,
              o = a.mediaHeight,
              l = a.mediaSize;
            return n().createElement("div", E({ className: i()(t, m[s], d[o], A[l]) }, r), u);
          },
          F = ["children"];
        const g = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                a = {},
                n = Object.keys(e);
              for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, F);
          return n().createElement(r.ZN, null, n().createElement(D, t, u));
        };
        var C = t(493),
          p = t.n(C);
        const B = "BattlePassBuyView_base_d6",
          h = "buyState";
        var f = t(3403);
        let v, b, w, y, S, x;
        function T() {}
        (!(function (e) {
          ((e.small = "small"),
            (e.big = "big"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(v || (v = {})),
          (function (e) {
            ((e.credits = "credits"),
              (e.gold = "gold"),
              (e.crystal = "crystal"),
              (e.xp = "xp"),
              (e.freeXP = "freeXP"),
              (e.equipCoin = "equipCoin"));
          })(b || (b = {})),
          (function (e) {
            ((e.Red = "RedActionBG"), (e.Blue = "BlueActionBG"));
          })(w || (w = {})),
          (function (e) {
            ((e[(e.Active = 0)] = "Active"),
              (e[(e.Paused = 1)] = "Paused"),
              (e[(e.Completed = 2)] = "Completed"),
              (e[(e.NotStarted = 3)] = "NotStarted"),
              (e[(e.Disabled = 4)] = "Disabled"));
          })(y || (y = {})),
          (function (e) {
            ((e[(e.BattlePass = 0)] = "BattlePass"),
              (e[(e.AnyLevels = 1)] = "AnyLevels"),
              (e[(e.ShopOffer = 2)] = "ShopOffer"));
          })(S || (S = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(x || (x = {})));
        function P(e) {
          return e;
        }
        function M() {
          return !1;
        }
        console.log;
        var k = t(9174),
          L = t(3138);
        function N(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return O(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return O(e, u);
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
        function O(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, r = new Array(u); t < u; t++) r[t] = e[t];
          return r;
        }
        const I = (e) => (0 === e ? window : window.subViews.get(e));
        const H = () => (e, u) => {
          const t = (0, a.createContext)({});
          return [
            function ({ mode: r = "real", options: s, children: i, mocks: o }) {
              const l = (0, a.useRef)([]),
                c = (t, r, a) => {
                  var n;
                  const s = (function ({
                      initializer: e = !0,
                      rootId: u = 0,
                      getRoot: t = I,
                      context: r = "model",
                    } = {}) {
                      const a = new Map();
                      function n(e, u = 0) {
                        viewEnv.removeDataChangedCallback(e, u)
                          ? a.delete(e)
                          : console.error("Can't remove callback by id:", e);
                      }
                      engine.whenReady.then(() => {
                        engine.on("viewEnv.onDataChanged", (e, u, t) => {
                          t.forEach((u) => {
                            const t = a.get(u);
                            void 0 !== t && t(e);
                          });
                        });
                      });
                      const s = (e) => {
                        const a = t(u),
                          n = r.split(".").reduce((e, u) => e[u], a);
                        return "string" != typeof e || 0 === e.length
                          ? n
                          : e.split(".").reduce((e, u) => {
                              const t = e[u];
                              return "function" == typeof t ? t.bind(e) : t;
                            }, n);
                      };
                      return {
                        subscribe: (t, n) => {
                          const i = "string" == typeof n ? `${r}.${n}` : r,
                            o = L.O.view.addModelObserver(i, u, !0);
                          return (a.set(o, t), e && t(s(n)), o);
                        },
                        readByPath: s,
                        createCallback: (e, u) => {
                          const t = s(u);
                          return (...u) => {
                            t(e(...u));
                          };
                        },
                        createCallbackNoArgs: (e) => {
                          const u = s(e);
                          return () => {
                            u();
                          };
                        },
                        dispose: function () {
                          for (var e, t = N(a.keys()); !(e = t()).done;) n(e.value, u);
                        },
                        unsubscribe: n,
                      };
                    })(r),
                    i =
                      "real" === t
                        ? s
                        : Object.assign({}, s, {
                            readByPath: null != (n = null == a ? void 0 : a.getter) ? n : () => {},
                          }),
                    o = (e) =>
                      "mocks" === t ? (null == a ? void 0 : a.getter(e)) : i.readByPath(e),
                    c = (e) => l.current.push(e),
                    _ = e({
                      mode: t,
                      readByPath: o,
                      externalModel: i,
                      observableModel: {
                        array: (e, u) => {
                          const r = null != u ? u : o(e),
                            a = k.LO.box(r, { equals: M });
                          return (
                            "real" === t &&
                              i.subscribe(
                                (0, k.aD)((e) => a.set(e)),
                                e,
                              ),
                            a
                          );
                        },
                        object: (e, u) => {
                          const r = null != u ? u : o(e),
                            a = k.LO.box(r, { equals: M });
                          return (
                            "real" === t &&
                              i.subscribe(
                                (0, k.aD)((e) => a.set(e)),
                                e,
                              ),
                            a
                          );
                        },
                        primitives: (e, u) => {
                          const r = o(u);
                          if (Array.isArray(e)) {
                            const a = e.reduce((e, u) => ((e[u] = k.LO.box(r[u], {})), e), {});
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, k.aD)((u) => {
                                    e.forEach((e) => {
                                      a[e].set(u[e]);
                                    });
                                  }),
                                  u,
                                ),
                              a
                            );
                          }
                          {
                            const a = e,
                              n = Object.entries(a),
                              s = n.reduce((e, [u, t]) => ((e[t] = k.LO.box(r[u], {})), e), {});
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, k.aD)((e) => {
                                    n.forEach(([u, t]) => {
                                      s[t].set(e[u]);
                                    });
                                  }),
                                  u,
                                ),
                              s
                            );
                          }
                        },
                      },
                      cleanup: c,
                    }),
                    E = { mode: t, model: _, externalModel: i, cleanup: c };
                  return {
                    model: _,
                    controls: "mocks" === t && a ? a.controls(E) : u(E),
                    externalModel: i,
                    mode: t,
                  };
                },
                _ = (0, a.useRef)(!1),
                E = (0, a.useState)(r),
                m = E[0],
                d = E[1],
                A = (0, a.useState)(() => c(r, s, o)),
                D = A[0],
                F = A[1];
              return (
                (0, a.useEffect)(() => {
                  _.current ? F(c(m, s, o)) : (_.current = !0);
                }, [o, m, s]),
                (0, a.useEffect)(() => {
                  d(r);
                }, [r]),
                (0, a.useEffect)(
                  () => () => {
                    (D.externalModel.dispose(), l.current.forEach((e) => e()));
                  },
                  [D],
                ),
                n().createElement(t.Provider, { value: D }, i)
              );
            },
            () => (0, a.useContext)(t),
          ];
        };
        var U = t(9480);
        const W = (e) =>
          null !== e && "object" == typeof e
            ? "CoherentArrayProxy" === e.constructor.name
              ? U.UI(e, (e) => ("object" == typeof e ? W(e) : e))
              : Array.isArray(e)
                ? e.map((e) => ("object" == typeof e ? W(e) : e))
                : Object.fromEntries(
                    Object.entries(e).map(([e, u]) => [e, "object" == typeof u ? W(u) : u]),
                  )
            : e;
        var G = t(3946),
          $ = t(930);
        const z = Object.values(b),
          V = H()(
            ({ observableModel: e }) => {
              const u = e.primitives(
                  ["price", "chapterID", "isActive", "compoundPriceDefaultID"],
                  "confirm",
                ),
                t = k.LO.box(""),
                r = {
                  main: e.primitives([
                    "state",
                    "shopOfferDiscount",
                    "isShopOfferAvailable",
                    "shopOfferTimeLeft",
                    "isWalletAvailable",
                    "isSingleChapter",
                  ]),
                  confirm: u,
                  topPriorityRewards: e.array("rewards.topPriorityRewards.items"),
                  nowRewards: e.array("rewards.nowRewards.items"),
                  futureRewards: e.array("rewards.futureRewards.items"),
                  packages: e.array("packages.items"),
                  compoundPrice: e.array("confirm.compoundPrice"),
                  priceID: t,
                },
                a = (0, G.Om)(() => r.topPriorityRewards.get(), { equals: M }),
                n = (0, G.Om)(
                  () => r.nowRewards.get().length + r.futureRewards.get().length - a().length,
                ),
                s = (0, G.Om)(() => r.packages.get(), { equals: M }),
                i = (0, G.Om)(() => U.U2(r.packages.get(), 0), { equals: M }),
                o = (0, G.Om)((e) => U.hX(r.packages.get(), (u) => u.chapterID === e)[0]),
                l = (0, G.Om)((e) => {
                  const u = o(e).compoundPrice;
                  return 0 === u.prices.length
                    ? []
                    : U.v(u.prices, (e) => {
                        const u = U.v(e.price, P),
                          t = { isMultiPrice: u.length > 1, isEnough: !0 };
                        return u.reduce(
                          (e, { name: u, value: t, isEnough: r }) => (
                            (e[u] = { value: t, isEnough: r }),
                            (e.isEnough = e.isEnough && r),
                            e
                          ),
                          t,
                        );
                      });
                }),
                c = (0, G.Om)((e, u) => {
                  var t;
                  return null == (t = l(e).find((e) => e[u])) ? void 0 : t[u];
                }),
                _ = (0, G.Om)((e) =>
                  z.filter((u) => c(e, u)).map((u) => ({ currencyType: u, currency: c(e, u) })),
                ),
                E = (0, G.Om)((e, u) =>
                  U.G(r.packages.get(), (t) => t.chapterID === e && t.chapterType === u),
                ),
                m = (0, G.Om)((e) => {
                  const u = U.sE(
                    r.packages.get(),
                    (u) => u.chapterID === e && u.chapterState === y.Disabled,
                  );
                  return Boolean(u);
                }),
                d = (0, G.Om)(
                  () => {
                    var e;
                    return [...((e = r.compoundPrice.get().prices), W(e))]
                      .sort((e, u) => {
                        var t, r;
                        return (
                          z.indexOf(null == (t = U.U2(e.price, 0)) ? void 0 : t.name) -
                          z.indexOf(null == (r = U.U2(u.price, 0)) ? void 0 : r.name)
                        );
                      })
                      .map((e) => {
                        var u, t;
                        return Object.assign({}, e, {
                          currencyType: null == (u = U.U2(e.price, 0)) ? void 0 : u.name,
                          value: null == (t = U.U2(e.price, 0)) ? void 0 : t.value,
                        });
                      });
                  },
                  { equals: M },
                ),
                A = (0, G.Om)(() => r.compoundPrice.get().prices.length > 1),
                D = (0, G.Om)(() => U.hX(s(), (e) => e.chapterType !== $._U.Marathon).length, {
                  equals: M,
                });
              return Object.assign({}, r, {
                computes: {
                  topPriorityRewards: a,
                  firstChapter: i,
                  chapters: s,
                  chapter: o,
                  getChapterPrices: l,
                  findCurrencyByType: c,
                  isTypedChapter: E,
                  isDisabled: m,
                  rewardsCount: n,
                  prices: d,
                  isMulticurrency: A,
                  getWideItemsCount: D,
                  getChapterCurrencies: _,
                },
              });
            },
            ({ model: e, externalModel: u }) => ({
              setPriceID: (0, k.aD)((u) => {
                e.priceID.set(u);
              }),
              back: u.createCallback((e) => ({ isClose: e }), "onBackClick"),
              showConfirm: u.createCallbackNoArgs("showConfirm"),
              choosePackage: u.createCallback((e) => ({ packageID: e.packageID }), "choosePackage"),
              shopOffer: u.createCallbackNoArgs("onShopOfferClick"),
              closeConfirm: u.createCallbackNoArgs("confirm.onCloseClick"),
              buy: u.createCallback(() => ({ priceID: e.priceID.get() }), "confirm.onBuyClick"),
              showRewards: u.createCallbackNoArgs("confirm.onShowRewardsClick"),
            }),
          ),
          j = V[0],
          X = V[1];
        var q = t(7727);
        const Y = {
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
          K = [
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
        function Z() {
          return (
            (Z =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Z.apply(this, arguments)
          );
        }
        class Q extends n().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, q.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, q.G)(this.props.soundClick));
              }),
              (this._onMouseUp = (e) => (u) => {
                (e && e(u), this.setState({ click: !1 }));
              }),
              (this.handleFocus = () => this.setState({ focus: !0 })),
              (this.handleBlur = () => this.setState({ focus: !1 })));
          }
          render() {
            const e = this.props,
              u = e.caption,
              t = e.onClick,
              r = e.goto,
              a = e.side,
              s = e.type,
              o = e.classNames,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              _ = e.onMouseDown,
              E = e.onMouseUp,
              m =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    a = {},
                    n = Object.keys(e);
                  for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(e, K)),
              d = i()(Y.base, Y[`base__${s}`], Y[`base__${a}`], null == o ? void 0 : o.base),
              A = i()(Y.icon, Y[`icon__${s}`], Y[`icon__${a}`], null == o ? void 0 : o.icon),
              D = i()(Y.glow, null == o ? void 0 : o.glow),
              F = i()(Y.caption, Y[`caption__${s}`], null == o ? void 0 : o.caption),
              g = i()(Y.goto, null == o ? void 0 : o.goto);
            return n().createElement(
              "div",
              Z(
                {
                  className: d,
                  onMouseEnter: this._onMouseEnter(l),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(_),
                  onMouseUp: this._onMouseUp(E),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                m,
              ),
              "info" !== s && n().createElement("div", { className: Y.shine }),
              n().createElement(
                "div",
                { className: A },
                n().createElement("div", { className: D }),
              ),
              n().createElement("div", { className: F }, u),
              r && n().createElement("div", { className: g }, r),
            );
          }
        }
        Q.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var J = t(5521),
          ee = t(4179);
        const ue = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function te(e = J.n.NONE, u = ue, t = !1) {
          (0, a.useEffect)(() => {
            if (e !== J.n.NONE)
              return (
                window.addEventListener("keydown", r, t),
                () => {
                  window.removeEventListener("keydown", r, t);
                }
              );
            function r(r) {
              if (r.keyCode === e) {
                if (L.O.view.isEventHandled()) return;
                (L.O.view.setEventHandled(), u(r), t && r.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        function re({
          key: e = J.n.ESCAPE,
          callback: u = () => L.O.view.sendEvent.close(),
          preventPropagation: t = !0,
        } = {}) {
          return (te(e, u, t), u);
        }
        var ae = t(903),
          ne = t(4420);
        const se = "BattlePassBuyViewContent_base_85",
          ie = "BattlePassBuyViewContent_background_15",
          oe = "BattlePassBuyViewContent_blackout_3d",
          le = "BattlePassBuyViewContent_back_d2",
          ce = "BattlePassBuyViewContent_header_50",
          _e = "BattlePassBuyViewContent_title_8a",
          Ee = "BattlePassBuyViewContent_subtitle_72",
          me = {
            base: "Illustration_base_d3",
            imgWrapper: "Illustration_imgWrapper_61",
            img: "Illustration_img_44",
            base__hover: "Illustration_base__hover_70",
            base__disabled: "Illustration_base__disabled_a8",
            vignette: "Illustration_vignette_e0",
            asset: "Illustration_asset_e2",
            highlight: "Illustration_highlight_36",
            highlight__default: "Illustration_highlight__default_2b",
            highlight__active: "Illustration_highlight__active_f1",
            highlight__shine: "Illustration_highlight__shine_b0",
          };
        let de;
        !(function (e) {
          ((e.Hover = "hover"), (e.Disabled = "disabled"));
        })(de || (de = {}));
        const Ae = ({ className: e, isHighlight: u, isActive: t, chapterID: r, state: a }) =>
            n().createElement(
              "div",
              { className: i()(me.base, a && me[`base__${a}`], e) },
              n().createElement(
                "div",
                { className: me.imgWrapper },
                n().createElement("div", {
                  className: me.img,
                  style: {
                    backgroundImage: `url('${(0, ae.wD)(R.images.gui.maps.icons.battlePass.buy.illustrations.commander, r)}')`,
                  },
                }),
              ),
              n().createElement("div", { className: me.asset }),
              n().createElement("div", { className: i()(me.highlight, me.highlight__default) }),
              u &&
                n().createElement("div", {
                  className: i()(me.highlight, t ? me.highlight__active : me.highlight__shine),
                }),
            ),
          De = "State_base_b0",
          Fe = "State_bg_49",
          ge = "State_content_d1",
          Ce = "State_ico_5b",
          pe = ({ className: e }) =>
            n().createElement(
              "div",
              { className: i()(De, e) },
              n().createElement("div", { className: Fe }),
              n().createElement(
                "div",
                { className: ge },
                n().createElement("div", { className: Ce }),
                R.strings.battle_pass.battlePassBuyView.card.purchased(),
              ),
            );
        var Be = t(2893);
        const he = {
          base: "BattlePassBuyExtraCard_base_cf",
          base__smallWidth: "BattlePassBuyExtraCard_base__smallWidth_4b",
          base__small: "BattlePassBuyExtraCard_base__small_d2",
          base__disabled: "BattlePassBuyExtraCard_base__disabled_a5",
          timer: "BattlePassBuyExtraCard_timer_8f",
          content: "BattlePassBuyExtraCard_content_1a",
          title: "BattlePassBuyExtraCard_title_6c",
          price: "BattlePassBuyExtraCard_price_8a",
          illustration: "BattlePassBuyExtraCard_illustration_6b",
          state: "BattlePassBuyExtraCard_state_9a",
          chapterActiveText: "BattlePassBuyExtraCard_chapterActiveText_70",
          fadeOut: "BattlePassBuyExtraCard_fadeOut_bb",
          fadeIn: "BattlePassBuyExtraCard_fadeIn_c8",
          fadeInWithScale: "BattlePassBuyExtraCard_fadeInWithScale_df",
          slideUp: "BattlePassBuyExtraCard_slideUp_da",
          scale: "BattlePassBuyExtraCard_scale_5a",
          rotate: "BattlePassBuyExtraCard_rotate_06",
        };
        var fe = t(3649);
        let ve;
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
        })(ve || (ve = {}));
        const be = 60,
          we = 3600,
          ye = 86400;
        Date.now();
        function Se(e = 0) {
          let u = e;
          const t = Math.trunc(u / ye);
          u -= t * ye;
          const r = Math.trunc(u / we);
          u -= r * we;
          const a = Math.trunc(u / be);
          return ((u -= a * be), { days: t, hours: r, minutes: a, seconds: u });
        }
        const Re = (e, u = !0) =>
            e.days > 7 && u
              ? (0, fe.WU)(R.strings.common.duration.days(), { days: e.days })
              : e.days >= 1
                ? 0 === e.hours
                  ? (0, fe.WU)(R.strings.common.duration.days(), { days: e.days })
                  : `${(0, fe.WU)(R.strings.common.duration.days(), { days: e.days })} ${(0, fe.WU)(R.strings.common.duration.hours(), { hours: e.hours })}`
                : e.hours >= 1
                  ? 0 === e.minutes
                    ? (0, fe.WU)(R.strings.common.duration.hours(), { hours: e.hours })
                    : `${(0, fe.WU)(R.strings.common.duration.hours(), { hours: e.hours })} ${(0, fe.WU)(R.strings.common.duration.minutes(), { minutes: e.minutes })}`
                  : (0, fe.WU)(R.strings.common.duration.minutes(), { minutes: e.minutes || 1 }),
          xe = () => {},
          Te = (e = 0, u, t = 0, r = xe) => {
            const n = (0, a.useState)(e),
              s = n[0],
              i = n[1];
            return (
              (0, a.useEffect)(() => {
                if (e > 0) {
                  i(e);
                  const a = Date.now(),
                    n = setInterval(
                      () => {
                        const u = e - Math.floor((Date.now() - a) / 1e3);
                        null !== t && u <= t ? (i(t), r && r(), clearInterval(n)) : i(u);
                      },
                      1e3 * (u || (e > 120 ? be : 1)),
                    );
                  return () => {
                    clearInterval(n);
                  };
                }
                i(0);
              }, [e, u, t, r]),
              s
            );
          };
        t(6536);
        ee.Sw.instance;
        let Pe;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(Pe || (Pe = {}));
        ee.Sw.instance;
        const Me = Te,
          ke = "CardTimer_base_84",
          Le = "CardTimer_light_ae",
          Ne = "CardTimer_icon_e1",
          Oe = "CardTimer_value_eb",
          Ie = R.strings.battle_pass.battlePassBuyView.card.timer,
          He = ({ expireTime: e }) => {
            const u = Me(e),
              t = u <= 60 ? Ie.lessMinute() : (0, fe.uF)(Ie.time(), { time: Re(Se(u), !1) });
            return n().createElement(
              "div",
              { className: ke },
              n().createElement("div", { className: Le }),
              n().createElement("div", { className: Ne }),
              n().createElement("div", { className: Oe }, t),
            );
          },
          Ue = "CurrentLevel_base_5e",
          We = "CurrentLevel_base__isHovered_d1",
          Ge = "CurrentLevel_level_fb",
          $e = "CurrentLevel_text_7b",
          ze = R.strings.battle_pass.battlePassBuyView.card,
          Ve = ({ isHovered: e, currentLevel: u }) => {
            const t = e ? ze.currentLevelHovered.text() : ze.currentLevel.text(),
              r = i()(Ue, e && We);
            return n().createElement(
              "div",
              { className: r },
              n().createElement("div", { className: $e }, t),
              n().createElement("div", { className: Ge }, u),
            );
          },
          je = "Description_base_af",
          Xe = "Description_base__disabled_35",
          qe = "Description_text_ee",
          Ye = "Description_text__hidden_51",
          Ke = R.strings.battle_pass.battlePassBuyView.card.descr,
          Ze = ({
            currentLevel: e,
            isLevelShow: u,
            isHovered: t,
            isBought: r,
            isResource: a = !1,
          }) => {
            const s = a ? Ke.chapterResource() : Ke.chapter(),
              o = r ? Ke.bought() : s;
            return n().createElement(
              "div",
              { className: i()(je, r && Xe) },
              u && n().createElement(Ve, { currentLevel: e, isHovered: t }),
              n().createElement("div", { className: i()(qe, !t && Ye) }, o),
            );
          },
          Qe = (e, u) => {
            let t;
            const r = setTimeout(() => {
              t = e();
            }, u);
            return () => {
              ("function" == typeof t && t(), clearTimeout(r));
            };
          },
          Je = "Logo_base_8b",
          eu = "Logo_light_62",
          uu = "Logo_light__hovered_29",
          tu = "Logo_lightAppear_e4",
          ru = "Logo_logoIcon_60",
          au = "Logo_base__notAvailable_23",
          nu = (e, u) => {
            const t = R.images.gui.maps.icons.battlePass.buy.logo,
              r = u <= c.cJ.Small ? "small" : "";
            return (0, ae.wD)(t, e, r);
          },
          su = ({
            chapterID: e,
            animationOrder: u,
            isAvailable: t,
            isHovered: r,
            isActiveChapter: s,
          }) => {
            const o = 800 + 100 * u;
            (0, a.useEffect)(() => {
              if (t) return Qe(() => (0, q.G)("bp_buy_pass_02"), o);
            }, [t, o]);
            const l = (0, c.GS)().mediaSize,
              _ = { animationDelay: `${o}ms` };
            return n().createElement(
              "div",
              { className: i()(Je, !t && au) },
              s &&
                n().createElement(
                  "div",
                  { style: _, className: tu },
                  n().createElement("div", { className: i()(eu, r && uu) }),
                ),
              n().createElement("div", {
                className: ru,
                style: { backgroundImage: `url(${nu(e, l)})` },
              }),
            );
          };
        var iu = t(2372);
        const ou = {
            base: "Currency_base_57",
            icon: "Currency_icon_c5",
            base__small: "Currency_base__small_af",
            base__big: "Currency_base__big_bc",
            base__large: "Currency_base__large_65",
            base__extraLarge: "Currency_base__extraLarge_4d",
            "icon__credits-small": "Currency_icon__credits-small_9b",
            "icon__credits-big": "Currency_icon__credits-big_96",
            "icon__credits-large": "Currency_icon__credits-large_ac",
            "icon__credits-extraLarge": "Currency_icon__credits-extraLarge_16",
            "icon__gold-small": "Currency_icon__gold-small_86",
            "icon__gold-big": "Currency_icon__gold-big_15",
            "icon__gold-large": "Currency_icon__gold-large_36",
            "icon__gold-extraLarge": "Currency_icon__gold-extraLarge_a0",
            "icon__crystal-small": "Currency_icon__crystal-small_27",
            "icon__crystal-big": "Currency_icon__crystal-big_cd",
            "icon__crystal-large": "Currency_icon__crystal-large_d3",
            "icon__crystal-extraLarge": "Currency_icon__crystal-extraLarge_09",
            "icon__xp-small": "Currency_icon__xp-small_a7",
            "icon__xp-big": "Currency_icon__xp-big_97",
            "icon__xp-large": "Currency_icon__xp-large_6b",
            "icon__xp-extraLarge": "Currency_icon__xp-extraLarge_67",
            "icon__freeXP-small": "Currency_icon__freeXP-small_ca",
            "icon__freeXP-big": "Currency_icon__freeXP-big_21",
            "icon__freeXP-large": "Currency_icon__freeXP-large_c8",
            "icon__freeXP-extraLarge": "Currency_icon__freeXP-extraLarge_58",
            "icon__equipCoin-small": "Currency_icon__equipCoin-small_32",
            "icon__equipCoin-big": "Currency_icon__equipCoin-big_79",
            "icon__equipCoin-large": "Currency_icon__equipCoin-large_2c",
            "icon__equipCoin-extraLarge": "Currency_icon__equipCoin-extraLarge_8a",
            value: "Currency_value_e1",
            value__freeXP: "Currency_value__freeXP_cb",
            value__credits: "Currency_value__credits_76",
            value__gold: "Currency_value__gold_dd",
            value__xp: "Currency_value__xp_b0",
            value__crystal: "Currency_value__crystal_19",
            value__equipCoin: "Currency_value__equipCoin_d0",
            value__notEnough: "Currency_value__notEnough_56",
            stock: "Currency_stock_87",
            stock__indent: "Currency_stock__indent_a1",
            stock__interactive: "Currency_stock__interactive_93",
            stockBackground: "Currency_stockBackground_82",
          },
          lu = ({
            isDiscount: e,
            isInteractiveDiscount: u,
            size: t,
            type: r,
            isEnough: a,
            value: s,
            discountValue: o,
            showPlus: l,
            stockBackgroundName: c = w.Red,
          }) => {
            const _ = i()(ou.value, ou[`value__${r}`], !a && ou.value__notEnough),
              E = i()(ou.icon, ou[`icon__${r}-${t}`]),
              m = i()(ou.stock, o && ou.stock__indent, u && ou.stock__interactive),
              d = l && s > 0 && "+",
              A = i()(ou.base, ou[`base__${t}`]);
            return n().createElement(
              "span",
              { className: A },
              n().createElement(
                "span",
                { className: _ },
                d,
                n().createElement(iu.A, { value: s, format: r === b.gold ? "gold" : "integral" }),
              ),
              n().createElement("span", { className: E }),
              e &&
                n().createElement(
                  "span",
                  { className: m },
                  n().createElement("span", {
                    className: ou.stockBackground,
                    style: { backgroundImage: `url(R.images.gui.maps.icons.library.${c})` },
                  }),
                  Boolean(o) && o,
                ),
            );
          };
        lu.defaultProps = { isEnough: !0 };
        const cu = n().memo(lu);
        var _u = t(9887),
          Eu = t.n(_u);
        const mu = ["xl", "lg", "md", "sm", "xs"],
          du = (e) => e.includes("_") && ((e) => mu.includes(e))(e.split("_").at(-1)),
          Au = [c.cJ.ExtraLarge, c.cJ.Large, c.cJ.Medium, c.cJ.Small, c.cJ.ExtraSmall],
          Du = (e, u) =>
            Object.keys(e).reduce((t, r) => {
              if (r in t) return t;
              if (du(r)) {
                const a = r.split("_").slice(0, -1).join("_");
                if (a in t) return t;
                const n = Au.indexOf(u),
                  s = (-1 !== n ? mu.slice(n) : [])
                    .map((e) => a + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  i = s ? e[s] : void 0;
                return ((t[a] = void 0 !== i ? i : e[a]), t);
              }
              const a = e[r];
              return (
                void 0 === a ||
                  ((e, u) => mu.some((t) => void 0 !== u[`${e}_${t}`]))(r, e) ||
                  (t[r] = a),
                t
              );
            }, {}),
          Fu = (e, u = Du) => {
            const t = (
              (e, u = Du) =>
              (t) => {
                const r = (0, c.GS)().mediaSize,
                  s = (0, a.useMemo)(() => u(t, r), [t, r]);
                return n().createElement(e, s);
              }
            )(e, u);
            return n().memo((u) =>
              Object.keys(u).some((e) => du(e) && void 0 !== u[e])
                ? n().createElement(t, u)
                : n().createElement(e, u),
            );
          },
          gu = {
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
          },
          Cu = [
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
        function pu() {
          return (
            (pu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            pu.apply(this, arguments)
          );
        }
        Object.keys(Eu());
        const Bu = {
            XL: { mt: gu.mt__XL, mr: gu.mr__XL, mb: gu.mb__XL, ml: gu.ml__XL },
            LG: { mt: gu.mt__LG, mr: gu.mr__LG, mb: gu.mb__LG, ml: gu.ml__LG },
            MDp: { mt: gu.mt__MDp, mr: gu.mr__MDp, mb: gu.mb__MDp, ml: gu.ml__MDp },
            MD: { mt: gu.mt__MD, mr: gu.mr__MD, mb: gu.mb__MD, ml: gu.ml__MD },
            SMp: { mt: gu.mt__SMp, mr: gu.mr__SMp, mb: gu.mb__SMp, ml: gu.ml__SMp },
            SM: { mt: gu.mt__SM, mr: gu.mr__SM, mb: gu.mb__SM, ml: gu.ml__SM },
            XS: { mt: gu.mt__XS, mr: gu.mr__XS, mb: gu.mb__XS, ml: gu.ml__XS },
          },
          hu = (Object.keys(Bu), ["mt", "mr", "mb", "ml"]),
          fu = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          vu = Fu((e) => {
            let u = e.className,
              t = e.width,
              r = e.height,
              s = e.m,
              o = e.mt,
              l = void 0 === o ? s : o,
              c = e.mr,
              _ = void 0 === c ? s : c,
              E = e.mb,
              m = void 0 === E ? s : E,
              d = e.ml,
              A = void 0 === d ? s : d,
              D = e.column,
              F = e.row,
              g = e.flexDirection,
              C = void 0 === g ? (D ? "column" : F && "row") || void 0 : g,
              p = e.flexStart,
              B = e.center,
              h = e.flexEnd,
              f = e.spaceBetween,
              v = e.spaceAround,
              b = e.justifyContent,
              w =
                void 0 === b
                  ? (p ? "flex-start" : B && "center") ||
                    (h && "flex-end") ||
                    (f && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : b,
              y = e.alignItems,
              S =
                void 0 === y
                  ? (p ? "flex-start" : B && "center") || (h && "flex-end") || void 0
                  : y,
              R = e.alignSelf,
              x = e.wrap,
              T = e.flexWrap,
              P = void 0 === T ? (x ? "wrap" : void 0) : T,
              M = e.grow,
              k = e.shrink,
              L = e.flex,
              N = void 0 === L ? (M || k ? `${M ? 1 : 0} ${k ? 1 : 0} auto` : void 0) : L,
              O = e.style,
              I = e.children,
              H = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  a = {},
                  n = Object.keys(e);
                for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, Cu);
            const U = (0, a.useMemo)(() => {
                const e = { mt: l, mr: _, mb: m, ml: A },
                  u = ((e) =>
                    hu.reduce((u, t) => {
                      const r = e[t];
                      return r && "number" != typeof r ? u.concat(Bu[!0 === r ? "MD" : r][t]) : u;
                    }, []))(e),
                  a = ((e) =>
                    hu.reduce((u, t) => {
                      const r = e[t];
                      return ("number" == typeof r && (u[fu[t]] = r + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, O, a, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: N,
                    alignSelf: R,
                    display: C || S ? "flex" : void 0,
                    flexDirection: C,
                    flexWrap: P,
                    justifyContent: w,
                    alignItems: S,
                  }),
                  computedClassNames: u,
                };
              }, [t, r, l, _, m, A, O, N, R, C, P, w, S]),
              W = U.computedStyle,
              G = U.computedClassNames;
            return n().createElement(
              "div",
              pu({ className: i()(gu.base, ...G, u), style: W }, H),
              I,
            );
          });
        var bu = t(280),
          wu = t(3532),
          yu = t.n(wu);
        const Su = {
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
          },
          Ru = [
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
        function xu() {
          return (
            (xu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            xu.apply(this, arguments)
          );
        }
        Object.keys(Eu());
        const Tu = Object.keys(yu()),
          Pu = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Mu = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          ku = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Lu = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Nu =
            (Object.keys(Lu),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Pu,
              "heading-H36": Pu,
              "heading-H28": Mu,
              "heading-H24": Mu,
              "heading-H24R": Mu,
              "heading-H22": Mu,
              "heading-H20R": Mu,
              "heading-H18": Mu,
              "heading-H15": ku,
              "heading-H14": ku,
              "paragraph-P24": Mu,
              "paragraph-P18": Mu,
              "paragraph-P16": Mu,
              "paragraph-P14": ku,
              "paragraph-P12": ku,
              "paragraph-P10": ku,
            }),
          Ou =
            (Object.keys(Nu),
            (e) =>
              e
                ? ((e) => Tu.includes(e))(e)
                  ? { colorClassName: Su[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Iu = Fu((e) => {
            let u = e.text,
              t = e.variant,
              r = e.className,
              s = e.color,
              o = e.m,
              l = e.mt,
              c = void 0 === l ? o : l,
              _ = e.mr,
              E = void 0 === _ ? o : _,
              m = e.mb,
              d = void 0 === m ? o : m,
              A = e.ml,
              D = void 0 === A ? o : A,
              F = e.style,
              g = e.format,
              C = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  a = {},
                  n = Object.keys(e);
                for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, Ru);
            const p = (0, a.useMemo)(() => {
                const e = Ou(s),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, r), colorClassName: u };
              }, [F, s]),
              B = p.computedStyle,
              h = p.colorClassName;
            return n().createElement(
              vu,
              xu(
                {
                  className: i()(Su.base, t && Su[t], h, r),
                  style: B,
                  mt: !0 === c ? Nu[t || "paragraph-P16"].mt : c,
                  mr: !0 === E ? Nu[t || "paragraph-P16"].mr : E,
                  mb: !0 === d ? Nu[t || "paragraph-P16"].mb : d,
                  ml: !0 === D ? Nu[t || "paragraph-P16"].ml : D,
                },
                C,
              ),
              void 0 !== g ? n().createElement(bu.z, xu({}, g, { text: u })) : u,
            );
          }),
          Hu = "Price_base_d1",
          Uu = "Price_divider_2d",
          Wu = R.strings.battle_pass.battlePassBuyView.card,
          Gu = (0, a.memo)(({ className: e, chapterPrices: u }) =>
            u.length
              ? n().createElement(
                  "div",
                  { className: i()(Hu, e) },
                  u.map((e, u) => {
                    var t;
                    return n().createElement(
                      a.Fragment,
                      { key: `price_${e.currencyType}` },
                      u > 0 && n().createElement(Iu, { text: Wu.priceDivider(), className: Uu }),
                      n().createElement(cu, {
                        type: e.currencyType,
                        size: v.small,
                        value: Number(null == (t = e.currency) ? void 0 : t.value),
                      }),
                    );
                  }),
                )
              : null,
          ),
          $u = R.strings.battle_pass.battlePassBuyView.card,
          zu = (0, f.Pi)(
            ({
              chapterID: e = 1,
              animationOrder: u = 0,
              isShopOfferAvailable: t = !1,
              isMarathon: r = !1,
              isSmallWidth: s = !1,
              expireTime: o = 0,
            }) => {
              const l = X(),
                c = l.model.computes,
                _ = l.controls.choosePackage,
                E = c.chapter(e),
                m = E.isBought,
                d = E.chapterState,
                A = E.currentLevel,
                D = E.packageID,
                F = (0, a.useState)(!1),
                g = F[0],
                C = F[1],
                p = d === y.Active,
                B = d === y.Paused,
                h = c.isTypedChapter(e, $._U.Resource),
                f = t && !r,
                v = c.getChapterCurrencies(e);
              return n().createElement(
                "div",
                {
                  className: i()(
                    he.base,
                    f && he.base__small,
                    p && he.base__activeChapter,
                    m && he.base__disabled,
                    s && he.base__smallWidth,
                  ),
                  onClick: () => {
                    (q.$.playClick(), m || (D && _({ packageID: D })));
                  },
                  onMouseEnter: () => {
                    ((0, q.G)("bp_highlight"), m || C(!0));
                  },
                  onMouseLeave: () => {
                    C(!1);
                  },
                },
                n().createElement(Ae, {
                  chapterID: e,
                  isHighlight: p,
                  isActive: m,
                  state: m ? de.Disabled : g ? de.Hover : void 0,
                  className: he.illustration,
                }),
                r &&
                  o > 0 &&
                  n().createElement(
                    "div",
                    { className: he.timer },
                    n().createElement(He, { expireTime: o }),
                  ),
                n().createElement(
                  "div",
                  { className: he.content },
                  n().createElement(su, {
                    chapterID: e,
                    animationOrder: u,
                    isAvailable: !m,
                    isHovered: g,
                    isActiveChapter: p,
                  }),
                  n().createElement("div", { className: he.title }, (0, Be.pC)(e, !1)),
                  n().createElement(Ze, {
                    isHovered: g,
                    currentLevel: A,
                    isLevelShow: p || B,
                    isBought: m,
                    isResource: h,
                  }),
                ),
                m
                  ? n().createElement(pe, { className: he.state })
                  : n().createElement(Gu, { chapterPrices: v, className: he.price }),
                p &&
                  n().createElement(
                    "div",
                    { className: he.chapterActiveText },
                    $u.activeChapter.text(),
                  ),
              );
            },
          );
        var Vu = t(3457),
          ju = t(3815);
        const Xu = "ShopOfferCard_base_3a",
          qu = "ShopOfferCard_base__wide_1c",
          Yu = "ShopOfferCard_background_44",
          Ku = "ShopOfferCard_shopOfferBorder_25",
          Zu = "ShopOfferCard_illustrationWrapper_94",
          Qu = "ShopOfferCard_illustration_0c",
          Ju = "ShopOfferCard_illustration__wide_c6",
          et = "ShopOfferCard_backgroundAsset_a4",
          ut = "ShopOfferCard_backgroundColor_45",
          tt = "ShopOfferCard_shopOfferDiscount_a1",
          rt = "ShopOfferCard_timer_42",
          at = "ShopOfferCard_content_ce",
          nt = "ShopOfferCard_title_4d",
          st = "ShopOfferCard_description_1c",
          it = "ShopOfferCard_buttonContainer_99",
          ot = "ShopOfferCard_button_d0",
          lt = R.strings.battle_pass.battlePassBuyView.card,
          ct = (0, f.Pi)(({ isWide: e = !1 }) => {
            const u = X(),
              t = u.controls,
              r = u.model.main.shopOfferTimeLeft.get(),
              a = (0, c.GS)().mediaSize < c.cJ.Medium,
              s = (0, ju.z)(() => {
                (q.$.playClick(), t.shopOffer());
              }),
              o = (0, ju.z)(() => {
                (0, q.G)("bp_highlight");
              }),
              l = i()(Xu, e && qu);
            return n().createElement(
              "div",
              { className: l, onClick: s, onMouseEnter: o },
              n().createElement(
                "div",
                { className: Yu },
                n().createElement(
                  "div",
                  { className: Zu },
                  n().createElement("div", { className: i()(Qu, e && Ju) }),
                ),
                n().createElement("div", { className: Ku }),
                n().createElement("div", { className: et }),
                n().createElement("div", { className: ut }),
                n().createElement("div", { className: tt }),
              ),
              r
                ? n().createElement(
                    "div",
                    { className: rt },
                    n().createElement(He, { expireTime: r }),
                  )
                : "",
              n().createElement(
                "div",
                { className: at },
                n().createElement(
                  "div",
                  { className: nt },
                  e ? lt.title.shopOfferWide() : lt.title.shopOffer(),
                ),
                n().createElement(Iu, { text: lt.descr.shopOffer(), className: st }),
                n().createElement(
                  "div",
                  { className: it },
                  n().createElement(
                    Vu.u5,
                    {
                      type: Vu.L$.main,
                      size: a ? Vu.qE.small : Vu.qE.medium,
                      mixClass: ot,
                      onClick: s,
                    },
                    lt.button.shopOffer(),
                  ),
                ),
              ),
            );
          }),
          _t = "CardAppearTransition_base_2e",
          Et = ({ animationOrder: e = 0, children: u }) => {
            const t = 600 + 100 * e;
            (0, a.useEffect)(() => Qe(() => (0, q.G)("bp_buy_pass_01"), t), [t]);
            const r = (0, a.useMemo)(() => ({ animationDelay: `${t}ms` }), [t]);
            return n().createElement("div", { style: r, className: _t }, u);
          },
          mt = "ExtraContent_base_4d",
          dt = "ExtraContent_cardsWrapper_31",
          At = "ExtraContent_cards_b2",
          Dt = "ExtraContent_card__isShopOfferAvailable_25",
          Ft = "ExtraContent_card_4c",
          gt = "ExtraContent_card__extra_fe",
          Ct = (0, f.Pi)(() => {
            const e = X().model,
              u = e.main.isShopOfferAvailable.get(),
              t = e.computes.getWideItemsCount(),
              r = e.computes.chapters(),
              a = t > 3;
            return n().createElement(
              "div",
              { className: mt },
              n().createElement(
                "div",
                { className: dt },
                u &&
                  n().createElement(
                    "div",
                    { className: i()(Ft, Dt) },
                    n().createElement(Et, null, n().createElement(ct, { isWide: a })),
                  ),
                n().createElement(
                  "div",
                  { className: At },
                  U.DZ(
                    r,
                    (e) => !(e.chapterType === $._U.Marathon),
                    (e, t) =>
                      n().createElement(
                        "div",
                        { key: e.packageID, className: Ft },
                        n().createElement(
                          Et,
                          { animationOrder: t + 1 },
                          n().createElement(zu, {
                            chapterID: e.chapterID,
                            isShopOfferAvailable: u,
                            animationOrder: t + 1,
                            isSmallWidth: a,
                          }),
                        ),
                      ),
                  ),
                ),
              ),
              U.DZ(
                r,
                (e) => e.chapterType === $._U.Marathon,
                (e) =>
                  n().createElement(
                    "div",
                    { key: e.packageID, className: i()(Ft, gt) },
                    n().createElement(
                      Et,
                      { animationOrder: r.length + 1 },
                      n().createElement(zu, {
                        chapterID: e.chapterID,
                        isShopOfferAvailable: !1,
                        isMarathon: !0,
                        expireTime: e.expireTime,
                        animationOrder: r.length + 1,
                        isSmallWidth: a,
                      }),
                    ),
                  ),
              ),
            );
          }),
          pt = R.strings.battle_pass.battlePassBuyView,
          Bt = (0, f.Pi)(({ onClose: e }) => {
            const u = X().model.computes.firstChapter(),
              t = (0, c.GS)().mediaSize,
              r = (0, ae.jz)(t),
              a = () => {
                e(!1);
              };
            return (
              re({ callback: a, preventPropagation: !1 }),
              n().createElement(
                "div",
                { className: se },
                n().createElement(
                  "div",
                  { className: ie },
                  n().createElement(ne.N, {
                    key: null == u ? void 0 : u.packageID,
                    isCurrent: !0,
                    customBackgroundStyle: { backgroundImage: `url(${(0, ae.Sc)(r)})` },
                  }),
                  n().createElement("div", { className: oe }),
                ),
                n().createElement(
                  "div",
                  { className: le },
                  n().createElement(Q, {
                    caption: R.strings.menu.viewHeader.backBtn.label(),
                    onClick: a,
                  }),
                ),
                n().createElement(
                  "div",
                  { className: ce },
                  n().createElement("div", { className: _e }, pt.title()),
                  n().createElement("div", { className: Ee }, pt.descr()),
                ),
                n().createElement(Ct, null),
              )
            );
          });
        var ht = t(2862),
          ft = t(5739);
        let vt;
        !(function (e) {
          ((e[(e.Space = 32)] = "Space"),
            (e[(e.Enter = 13)] = "Enter"),
            (e[(e.A = 65)] = "A"),
            (e[(e.B = 66)] = "B"),
            (e[(e.C = 67)] = "C"),
            (e[(e.D = 68)] = "D"),
            (e[(e.E = 69)] = "E"),
            (e[(e.F = 70)] = "F"),
            (e[(e.G = 71)] = "G"),
            (e[(e.H = 72)] = "H"),
            (e[(e.I = 73)] = "I"),
            (e[(e.J = 74)] = "J"),
            (e[(e.K = 75)] = "K"),
            (e[(e.L = 76)] = "L"),
            (e[(e.M = 77)] = "M"),
            (e[(e.N = 78)] = "N"),
            (e[(e.O = 79)] = "O"),
            (e[(e.P = 80)] = "P"),
            (e[(e.Q = 81)] = "Q"),
            (e[(e.R = 82)] = "R"),
            (e[(e.S = 83)] = "S"),
            (e[(e.T = 84)] = "T"),
            (e[(e.U = 85)] = "U"),
            (e[(e.V = 86)] = "V"),
            (e[(e.W = 87)] = "W"),
            (e[(e.X = 88)] = "X"),
            (e[(e.Y = 89)] = "Y"),
            (e[(e.Z = 90)] = "Z"));
        })(vt || (vt = {}));
        const bt = (e = {}) => {
          (0, a.useEffect)(() => {
            const u = (u) => {
              if (!u.altKey && !u.ctrlKey && !u.shiftKey) {
                const t = e[u.keyCode];
                "function" == typeof t && t(u);
              }
            };
            return (
              window.addEventListener("keyup", u),
              () => {
                window.removeEventListener("keyup", u);
              }
            );
          }, [e]);
        };
        var wt = t(7030),
          yt = t(7264),
          St = t(3942),
          Rt = t(9525);
        const xt = "ChapterWarning_base_fe",
          Tt = "ChapterWarning_base__isMulticurrency_be",
          Pt = "ChapterWarning_lip_a0",
          Mt = "ChapterWarning_message_62",
          kt = "ChapterWarning_icon_d2",
          Lt = R.strings.battle_pass.battlePassBuyView.confirm,
          Nt = ({ className: e, isMulticurrency: u, isDisabled: t = !1 }) =>
            n().createElement(
              "div",
              { className: i()(xt, e, u && Tt) },
              n().createElement("div", { className: Pt }),
              n().createElement(
                "div",
                { className: Mt },
                n().createElement("span", { className: kt }),
                t ? Lt.shopOfferWarningDisabledChapter() : Lt.shopOfferWarningNoActiveChapter(),
              ),
            );
        let Ot;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(Ot || (Ot = {}));
        var It = t(1856);
        let Ht;
        !(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"));
        })(Ht || (Ht = {}));
        const Ut = {
            base: "RadioButton_base_d9",
            base__disabled: "RadioButton_base__disabled_84",
            input: "RadioButton_input_24",
            base__small: "RadioButton_base__small_71",
            base__medium: "RadioButton_base__medium_d8",
            blank: "RadioButton_blank_b5",
            blankHover: "RadioButton_blankHover_5e",
            blankMousedown: "RadioButton_blankMousedown_0e",
            check: "RadioButton_check_f2",
            checkHover: "RadioButton_checkHover_c6",
            checkMousedown: "RadioButton_checkMousedown_a7",
            transition: "RadioButton_transition_b3",
            base__blank: "RadioButton_base__blank_46",
            base__blankHover: "RadioButton_base__blankHover_9a",
            base__blankMousedown: "RadioButton_base__blankMousedown_cd",
            base__check: "RadioButton_base__check_fe",
            base__checkHover: "RadioButton_base__checkHover_2f",
            base__checkMousedown: "RadioButton_base__checkMousedown_83",
            label: "RadioButton_label_7f",
          },
          Wt = [
            "children",
            "labelRenderer",
            "value",
            "currentValue",
            "autofocus",
            "disabled",
            "size",
            "label",
            "soundHover",
            "soundClick",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseUp",
            "onMouseDown",
            "onClick",
            "onChange",
            "onFocus",
            "onBlur",
          ];
        function Gt() {
          return (
            (Gt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Gt.apply(this, arguments)
          );
        }
        const $t = (0, a.memo)((e) => {
            let u = e.children,
              t = e.labelRenderer,
              r = e.value,
              s = e.currentValue,
              o = e.autofocus,
              l = void 0 !== o && o,
              c = e.disabled,
              _ = void 0 !== c && c,
              E = e.size,
              m = void 0 === E ? Ht.Medium : E,
              d = e.label,
              A = e.soundHover,
              D = void 0 === A ? "highlight" : A,
              F = e.soundClick,
              g = void 0 === F ? "play" : F,
              C = e.onMouseEnter,
              p = e.onMouseLeave,
              B = e.onMouseUp,
              h = e.onMouseDown,
              f = e.onClick,
              v = e.onChange,
              b = e.onFocus,
              w = e.onBlur,
              y = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  a = {},
                  n = Object.keys(e);
                for (r = 0; r < n.length; r++) ((t = n[r]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, Wt);
            const S = r === s,
              R = (0, a.useState)(!1),
              x = R[0],
              T = R[1],
              P = (0, a.useState)(!1),
              M = P[0],
              k = P[1],
              L = (0, a.useState)(l),
              N = L[0],
              O = L[1],
              I = (0, a.useRef)(null),
              H = (0, a.useCallback)(() => {
                !_ && I.current && (I.current.focus(), O(!0));
              }, [_]),
              U = (0, a.useCallback)(
                (e) => {
                  N && null !== I.current && !I.current.contains(e.target) && O(!1);
                },
                [N],
              );
            ((0, a.useEffect)(
              () => (
                document.addEventListener("mousedown", U),
                () => {
                  document.removeEventListener("mousedown", U);
                }
              ),
              [U],
            ),
              (0, a.useEffect)(() => {
                O(l);
              }, [l]));
            const W = (0, a.useCallback)(
                (e) => {
                  _ || (v && v(r), f && f(r, e));
                },
                [_, v, f, r],
              ),
              G = (0, a.useCallback)(
                (e) => {
                  if (!_) {
                    const u = e.button === Ot.LEFT;
                    (u && T(!0), u && h && h(r, e), g && (0, q.G)(g), l && H());
                  }
                },
                [l, _, h, H, g, r],
              ),
              $ = (0, a.useCallback)(
                (e) => {
                  _ || (T(!1), B && B(r, e));
                },
                [_, B, r],
              ),
              z = (0, a.useCallback)(
                (e) => {
                  _ || (C && C(r, e), D && (0, q.G)(D), k(!0));
                },
                [_, C, D, r],
              ),
              V = (0, a.useCallback)(
                (e) => {
                  _ || (T(!1), k(!1), p && p(r, e));
                },
                [_, p, r],
              ),
              j = (0, a.useCallback)(
                (e) => {
                  _ || (O(!0), b && b(r, e));
                },
                [_, b, r],
              ),
              X = (0, a.useCallback)(
                (e) => {
                  _ || (O(!1), w && w(r, e));
                },
                [_, w, r],
              ),
              Y = i()(Ut.base, Ut[`base__${m}`], {
                [Ut.base__blank]: !S && !M,
                [Ut.base__blankHover]: !S && M && !x,
                [Ut.base__blankMousedown]: !S && M && x,
                [Ut.base__check]: S && !M,
                [Ut.base__checkHover]: S && M && !x,
                [Ut.base__checkMousedown]: S && M && x,
                [Ut.base__focused]: N,
                [Ut.base__disabled]: _,
              }),
              K = (0, a.useMemo)(
                () => ({ isHovered: M, isMouseDown: x, isFocused: N, isChecked: S }),
                [M, x, N, S],
              ),
              Z = (0, a.useRef)(Ut.blank),
              Q = (0, a.useRef)(Ut.blankHover),
              J = (0, a.useRef)(Ut.blankMousedown),
              ee = (0, a.useRef)(Ut.check),
              ue = (0, a.useRef)(Ut.checkHover),
              te = (0, a.useRef)(Ut.checkMousedown);
            return (
              (0, a.useEffect)(
                (0, It.v)(() => {
                  ((Z.current = i()(Ut.blank, Ut.transition)),
                    (Q.current = i()(Ut.blankHover, Ut.transition)),
                    (J.current = i()(Ut.blankMousedown, Ut.transition)),
                    (ee.current = i()(Ut.check, Ut.transition)),
                    (ue.current = i()(Ut.checkHover, Ut.transition)),
                    (te.current = i()(Ut.checkMousedown, Ut.transition)));
                }),
                [],
              ),
              n().createElement(
                "div",
                Gt(
                  {
                    ref: I,
                    className: Y,
                    onClick: W,
                    onMouseEnter: z,
                    onMouseLeave: V,
                    onMouseDown: G,
                    onMouseUp: $,
                    onFocus: j,
                    onBlur: X,
                  },
                  y,
                ),
                n().createElement(
                  "div",
                  { className: Ut.input },
                  n().createElement("div", { className: Z.current }),
                  n().createElement("div", { className: Q.current }),
                  n().createElement("div", { className: J.current }),
                  n().createElement("div", { className: ee.current }),
                  n().createElement("div", { className: ue.current }),
                  n().createElement("div", { className: te.current }),
                ),
                n().createElement("div", { className: Ut.label }, d || u || (t && t(K))),
              )
            );
          }),
          zt = "CurrencyRadioButton_currency_80",
          Vt = "CurrencyRadioButton_gold_4b",
          jt = "CurrencyRadioButton_value_db",
          Xt = "CurrencyRadioButton_icon_ae",
          qt = (0, f.Pi)(
            ({ currencyType: e, value: u, priceID: t, currentPriceID: r, onClick: a }) =>
              n().createElement(
                $t,
                {
                  value: t,
                  currentValue: r,
                  onClick: () => {
                    a(t);
                  },
                },
                n().createElement(
                  "div",
                  { className: zt },
                  e === b.gold
                    ? n().createElement(
                        "div",
                        { className: Vt },
                        n().createElement(
                          "div",
                          { className: jt },
                          n().createElement(iu.A, { value: u, format: "gold" }),
                        ),
                        n().createElement("div", { className: Xt }),
                      )
                    : n().createElement(cu, { type: e, size: v.big, value: u }),
                ),
              ),
          ),
          Yt = "Price_base_70",
          Kt = "Price_label_84",
          Zt = "Price_label__isMulticurrency_b4",
          Qt = "Price_priceDivider_b4",
          Jt = R.strings.battle_pass.battlePassBuyView,
          er = (0, f.Pi)(({ className: e }) => {
            const u = X(),
              t = u.model,
              r = u.controls,
              s = t.priceID.get(),
              o = t.computes.prices(),
              l = o.length > 1;
            return (
              (0, a.useEffect)(() => {
                s || r.setPriceID(t.confirm.compoundPriceDefaultID.get());
              }, [r, s, t.confirm.compoundPriceDefaultID]),
              n().createElement(
                "div",
                { className: i()(Yt, e) },
                l
                  ? n().createElement(Iu, { text: Jt.multicurrencyPrice(), className: i()(Kt, Zt) })
                  : n().createElement(Iu, { text: Jt.price(), className: Kt }),
                l
                  ? o.map((e, u) =>
                      n().createElement(
                        a.Fragment,
                        { key: e.currencyType },
                        u > 0 && n().createElement("div", { className: Qt }, Jt.priceDivider()),
                        n().createElement(qt, {
                          currencyType: e.currencyType,
                          value: e.value,
                          priceID: e.priceID,
                          currentPriceID: s,
                          onClick: r.setPriceID,
                        }),
                      ),
                    )
                  : n().createElement(cu, {
                      type: o[0].currencyType,
                      size: v.big,
                      value: o[0].value,
                    }),
              )
            );
          }),
          ur = "Footer_base_9a",
          tr = "Footer_price_b6",
          rr = "Footer_warning_de",
          ar = "Footer_buttons_32",
          nr = "Footer_chapterWarning_c1",
          sr = R.strings.battle_pass.battlePassBuyView,
          ir = (0, f.Pi)(({ onBackClick: e }) => {
            const u = X(),
              t = u.model,
              r = u.controls,
              a = t.confirm,
              s = a.chapterID,
              o = a.isActive,
              l = t.main,
              c = l.isWalletAvailable,
              _ = l.isShopOfferAvailable,
              E = t.computes.isTypedChapter(s.get(), $._U.Marathon),
              m = t.computes.isDisabled(s.get()),
              d = !E && _.get();
            return n().createElement(
              "div",
              { className: i()(ur) },
              n().createElement(er, { className: tr }),
              d && n().createElement("div", { className: rr }, sr.confirm.shopOfferWarning()),
              n().createElement(Rt._, {
                onAccept: r.buy,
                onCancel: e,
                isWalletAvailable: c.get(),
                buttonAcceptText: sr.btnBuy(),
                className: ar,
              }),
              !o.get() && n().createElement(Nt, { className: i()(d && nr), isDisabled: m }),
            );
          }),
          or = {
            base: "ConfirmBuyViewContent_base_e3",
            fadeIn: "ConfirmBuyViewContent_fadeIn_bd",
            control: "ConfirmBuyViewContent_control_17",
            content: "ConfirmBuyViewContent_content_9d",
            windowIn: "ConfirmBuyViewContent_windowIn_81",
            content__warning: "ConfirmBuyViewContent_content__warning_3e",
            content__activeChapterWarning: "ConfirmBuyViewContent_content__activeChapterWarning_60",
            backgroundCommanderWrapper: "ConfirmBuyViewContent_backgroundCommanderWrapper_31",
            backgroundCommander: "ConfirmBuyViewContent_backgroundCommander_19",
            descriptionText: "ConfirmBuyViewContent_descriptionText_c2",
            rewardsContainer: "ConfirmBuyViewContent_rewardsContainer_0b",
            priorityRewards: "ConfirmBuyViewContent_priorityRewards_0c",
            background: "ConfirmBuyViewContent_background_73",
            ico: "ConfirmBuyViewContent_ico_2d",
            indentBlock: "ConfirmBuyViewContent_indentBlock_dc",
            rewardBtn: "ConfirmBuyViewContent_rewardBtn_64",
            fadeOut: "ConfirmBuyViewContent_fadeOut_95",
            fadeInWithScale: "ConfirmBuyViewContent_fadeInWithScale_f4",
            slideUp: "ConfirmBuyViewContent_slideUp_b4",
            scale: "ConfirmBuyViewContent_scale_18",
            rotate: "ConfirmBuyViewContent_rotate_2c",
            "fade-in": "ConfirmBuyViewContent_fade-in_b0",
          };
        function lr() {
          return (
            (lr =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            lr.apply(this, arguments)
          );
        }
        const cr = (e) => ({
            from: { opacity: 0 },
            to: { opacity: 1 },
            delay: 400 + 100 * e,
            config: { duration: 300 },
            onStart: () => {
              (0, q.G)("bp_reward");
            },
          }),
          _r = R.strings.battle_pass.battlePassBuyView,
          Er = (0, f.Pi)(({ onBack: e }) => {
            const u = X(),
              t = u.model,
              r = u.controls,
              s = t.confirm,
              o = s.chapterID,
              l = s.isActive,
              _ = t.computes.topPriorityRewards(),
              E = t.computes.rewardsCount(),
              m = t.main,
              d = m.isShopOfferAvailable,
              A = m.isWalletAvailable,
              D = m.isSingleChapter,
              F = (0, c.GS)(),
              g = F.remScreenHeight,
              C = F.mediaSize,
              p = (0, wt.useSpring)(cr(_.length)),
              B = A.get(),
              h = D.get(),
              f = (0, ae.jz)(C),
              v = (0, ae.sM)(o.get(), f),
              b = (0, a.useCallback)(() => ({ [J.n.ENTER]: r.buy, [J.n.SPACE]: r.buy }), [r.buy]),
              w = (0, a.useCallback)(() => {
                e(h);
              }, [h, e]);
            (re({ callback: w, preventPropagation: !1 }), bt(B ? b() : void 0));
            const y = C < c.cJ.Medium ? ht.h2.Small : ht.h2.Big,
              S = !t.computes.isTypedChapter(o.get(), $._U.Marathon) && d.get();
            return n().createElement(
              "div",
              { className: or.base },
              n().createElement(
                "div",
                { className: or.control },
                n().createElement(Q, {
                  caption: R.strings.menu.viewHeader.backBtn.label(),
                  onClick: w,
                  goto: h ? "" : _r.confirm.backBtnText(),
                }),
              ),
              n().createElement("div", { className: or.background, style: v }),
              n().createElement(
                "div",
                {
                  className: i()(
                    or.content,
                    S && or.content__warning,
                    !l && or.content__activeChapterWarning,
                  ),
                },
                n().createElement(
                  "div",
                  { className: or.backgroundCommanderWrapper },
                  n().createElement("div", {
                    className: i()(
                      or.backgroundCommander,
                      g >= 1200 && g < 1440 && or.backgroundCommander__large,
                    ),
                    style: {
                      backgroundImage: `url(${(0, ae.wD)(R.images.gui.maps.icons.battlePass.buy.confirm.commander, o.get())})`,
                    },
                  }),
                ),
                n().createElement(St.D, { chapter: o.get(), buyBP: _r.confirm.title() }),
                n().createElement(
                  "div",
                  { className: or.descriptionText },
                  _r.confirm.description(),
                ),
                n().createElement(
                  "div",
                  { className: or.rewardsContainer },
                  n().createElement(
                    "div",
                    { className: or.priorityRewards },
                    U.UI(_, (e, u) =>
                      n().createElement(
                        yt.d,
                        { animationConfig: cr(u), key: `${e.item}_${u}` },
                        n().createElement(ft.Q, lr({}, (0, Be.$n)(e, y), { className: or.reward })),
                      ),
                    ),
                  ),
                  E > 0
                    ? n().createElement(
                        wt.animated.div,
                        { style: p },
                        n().createElement(
                          Vu.u5,
                          {
                            type: Vu.L$.ghost,
                            size: Vu.qE.medium,
                            mixClass: or.rewardBtn,
                            onClick: r.showRewards,
                          },
                          n().createElement(bu.z, {
                            text: _r.confirmAnyNumber.moreRewards(),
                            binding: { count: E },
                          }),
                        ),
                      )
                    : n().createElement("div", { className: or.indentBlock }),
                ),
                n().createElement(ir, { onBackClick: w }),
              ),
            );
          }),
          mr = H()(({ observableModel: e }) => {
            const u = {
                levels: e.primitives(["fromLevel", "toLevel", "chapterID", "packageState"]),
                nowRewards: e.array("nowRewards.items"),
                futureRewards: e.array("futureRewards.items"),
              },
              t = (0, G.Om)(() => u.nowRewards.get(), { equals: M }),
              r = (0, G.Om)(() => u.futureRewards.get(), { equals: M });
            return Object.assign({}, u, { computes: { nowRewards: t, futureRewards: r } });
          }, T),
          dr = mr[0],
          Ar = mr[1];
        var Dr = t(3862),
          Fr = t(9430),
          gr = t(9791);
        const Cr = "Content_base_27",
          pr = "Content_mainContent_dd",
          Br = R.strings.battle_pass.battlePassBuyView.reward,
          hr = ({ fromLevel: e, toLevel: u, nowRewards: t, futureRewards: r }) => {
            const a = ((e, u) =>
                e < u
                  ? { title: Br.titleNowRewards(), completedSteps: `${e} - ${u}` }
                  : { title: Br.titleNowRewardsSingle(), completedSteps: `${u}` })(e, u),
              s = a.title,
              i = a.completedSteps;
            return n().createElement(
              gr.z,
              { className: Cr },
              n().createElement(
                "div",
                { className: pr },
                t.length > 0 &&
                  n().createElement(Fr.r, { title: s, iconType: Dr.Q.now, rewards: t, steps: i }),
                r.length > 0 &&
                  n().createElement(Fr.r, {
                    title: Br.titleFutureRewards(),
                    iconType: Dr.Q.future,
                    rewards: r,
                  }),
              ),
            );
          },
          fr = "RewardsViewContent_base_eb",
          vr = "RewardsViewContent_background_89",
          br = "RewardsViewContent_shadow_d6",
          wr = "RewardsViewContent_back_05",
          yr = "RewardsViewContent_content_9f",
          Sr = "RewardsViewContent_header_0b",
          Rr = "RewardsViewContent_title_8b",
          xr = "RewardsViewContent_description_4e",
          Tr = "RewardsViewContent_footerButton_f4",
          Pr = R.strings.battle_pass.battlePassBuyView.reward,
          Mr = (0, f.Pi)(({ onBack: e }) => {
            const u = Ar().model,
              t = u.levels,
              r = t.fromLevel,
              a = t.toLevel,
              s = t.chapterID;
            re({ callback: e, preventPropagation: !1 });
            const i = {
              backgroundImage: `url(${(0, ae.wD)(R.images.gui.maps.icons.battlePass.backgrounds.rewards, s.get())})`,
            };
            return n().createElement(
              "div",
              { className: fr },
              n().createElement(
                "div",
                { className: vr },
                n().createElement(ne.N, {
                  chapter: s.get(),
                  isCurrent: !0,
                  customBackgroundStyle: i,
                }),
              ),
              n().createElement("div", { className: br }),
              n().createElement(
                "div",
                { className: wr },
                n().createElement(Q, {
                  caption: R.strings.menu.viewHeader.backBtn.label(),
                  onClick: e,
                }),
              ),
              n().createElement(
                "div",
                { className: Sr },
                n().createElement(
                  "div",
                  { className: Rr },
                  n().createElement(bu.z, {
                    text: Pr.chapter(),
                    binding: { chapterName: (0, Be.pC)(s.get(), !0) },
                  }),
                ),
                n().createElement("div", { className: xr }, Pr.titleBattlePass()),
              ),
              n().createElement(
                "div",
                { className: yr },
                n().createElement(hr, {
                  nowRewards: u.computes.nowRewards(),
                  futureRewards: u.computes.futureRewards(),
                  toLevel: a.get(),
                  fromLevel: r.get(),
                }),
                n().createElement(
                  Vu.u5,
                  { type: Vu.L$.secondary, size: Vu.qE.medium, mixClass: Tr, onClick: e },
                  Pr.backBtn(),
                ),
              ),
            );
          }),
          kr = { context: "model.rewards" },
          Lr = (0, f.Pi)(() => {
            const e = X(),
              u = e.model,
              t = e.controls,
              r = u.main.state.get();
            switch (
              ((0, a.useEffect)(() => {
                u.priceID.get() && r === h && t.setPriceID("");
              }, [t, u.priceID, r]),
              r)
            ) {
              case h:
                return n().createElement(Bt, { onClose: t.back });
              case "confirmState":
                return n().createElement(Er, { onBack: t.back });
              case "rewardsState":
                return n().createElement(
                  dr,
                  { options: kr },
                  n().createElement(Mr, { onBack: t.showConfirm }),
                );
              default:
                return n().createElement(Bt, { onClose: t.back });
            }
          });
        engine.whenReady.then(() => {
          p().render(
            n().createElement(
              j,
              null,
              n().createElement(g, { className: B }, n().createElement(Lr, null)),
            ),
            document.getElementById("root"),
          );
        });
      },
      903: (e, u, t) => {
        "use strict";
        t.d(u, { Sc: () => s, W4: () => c, jz: () => o, sM: () => l, wD: () => i });
        var r = t(5415),
          a = t(8546);
        const n = (e) => {
            switch (e) {
              case a.$u.Micro:
                return "s";
              case a.$u.Small:
                return "m";
              default:
                return "l";
            }
          },
          s = (e = a.$u.Medium) => {
            const u = R.images.gui.maps.icons.battlePass.backgrounds,
              t = n(e);
            return u.$dyn(`common_${t}`);
          },
          i = (e, u, t = "") => {
            const r = t.length > 0 ? `_${t}` : t,
              a = e.$dyn(`c_${u}${r}`),
              n = e.$dyn(`common${r}`);
            return a || n;
          },
          o = (e) => {
            switch (e) {
              case r.cJ.ExtraSmall:
              case r.cJ.Small:
                return a.$u.Micro;
              case r.cJ.Medium:
                return a.$u.Small;
              default:
                return a.$u.Medium;
            }
          },
          l = (e, u) => {
            const t = R.images.gui.maps.icons.battlePass.backgrounds.confirm,
              r = n(u);
            return { backgroundImage: `url(${i(t, e, r)})` };
          },
          c = (e, u = a.$u.Medium) => {
            const t = R.images.gui.maps.icons.battlePass.backgrounds,
              r = n(u);
            return { backgroundImage: `url(${i(t.chapter, e, r)})` };
          };
      },
      930: (e, u, t) => {
        "use strict";
        let r, a;
        (t.d(u, { _U: () => a }),
          (function (e) {
            ((e.style = "style"),
              (e.tankman = "tankman"),
              (e.vehicle = "vehicle"),
              (e.mixed = "mixed"));
          })(r || (r = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(a || (a = {})));
        (r.style, r.tankman);
      },
      2893: (e, u, t) => {
        "use strict";
        t.d(u, { $n: () => s, pC: () => n });
        var r = t(2862),
          a = t(729);
        (t(5216), t(8546), t(930));
        const n = (e, u) =>
            u
              ? R.strings.battle_pass.chapter.fullNameUppercased.quoted.$dyn(`c_${e}`) || ""
              : R.strings.battle_pass.chapter.fullNameUppercased.$dyn(`c_${e}`) || "",
          s = (e, u = r.h2.Big) => {
            const t = e.item,
              n = e.name,
              s = e.icon,
              i = e.value,
              o = e.overlayType,
              l = e.tooltipId,
              c = e.tooltipContentId;
            return {
              name: t || n,
              image:
                n === r.E4.DogTagType
                  ? `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_${s}`
                  : (0, a.ry)(e, u),
              special: o,
              value: i,
              valueType: (0, a.p3)(n),
              tooltipArgs: (0, a.pI)({ tooltipId: l }, Number(c), { ignoreShowDelay: !0 }),
              size: u,
            };
          };
      },
      7264: (e, u, t) => {
        "use strict";
        t.d(u, { d: () => l });
        var r = t(6483),
          a = t.n(r),
          n = t(6179),
          s = t.n(n),
          i = t(7030);
        const o = "AnimatedReward_base_f0",
          l = ({ children: e, animationConfig: u, className: t }) => {
            const r = (0, i.useSpring)(u);
            return s().createElement(i.animated.div, { style: r, className: a()(o, t) }, e);
          };
      },
      9525: (e, u, t) => {
        "use strict";
        t.d(u, { _: () => _ });
        var r = t(6483),
          a = t.n(r),
          n = t(3457),
          s = t(6179),
          i = t.n(s);
        const o = "BuyButtons_base_4b",
          l = "BuyButtons_button_32",
          c = R.strings.battle_pass.battlePassBuyView,
          _ = ({
            isWalletAvailable: e,
            onAccept: u,
            buttonAcceptText: t,
            onCancel: r,
            className: s,
            isMulticurrency: _ = !1,
          }) =>
            i().createElement(
              "div",
              { className: a()(o, s) },
              i().createElement(
                n.u5,
                { type: n.L$.main, size: n.qE.medium, disabled: !e, onClick: u, mixClass: l },
                t,
              ),
              !_ &&
                i().createElement(
                  n.u5,
                  { type: n.L$.primary, size: n.qE.medium, onClick: r, mixClass: l },
                  c.btnCancel(),
                ),
            );
      },
      4420: (e, u, t) => {
        "use strict";
        t.d(u, { N: () => _ });
        var r = t(6483),
          a = t.n(r),
          n = t(5415),
          s = t(6179),
          i = t.n(s),
          o = t(903);
        const l = "ChapterBackground_base_fa",
          c = "ChapterBackground_base__current_7a",
          _ = ({ chapter: e, isCurrent: u, customBackgroundStyle: t }) => {
            const r = (0, n.GS)().mediaSize,
              s = (0, o.jz)(r);
            return i().createElement("div", {
              className: a()(l, u && c),
              style: t || (0, o.W4)(null != e ? e : 0, s),
            });
          };
      },
      8546: (e, u, t) => {
        "use strict";
        let r, a, n, s;
        (t.d(u, { $u: () => r }),
          (function (e) {
            ((e.Micro = "micro"), (e.Small = "small"), (e.Medium = "medium"));
          })(r || (r = {})),
          (function (e) {
            ((e.ACTIVE = "active"), (e.COMPLETED = "completed"), (e.NOT_CHOSEN = "notChosen"));
          })(a || (a = {})),
          (function (e) {
            ((e.AwaitSeason = "awaitSeason"),
              (e.Bought = "bought"),
              (e.Free = "free"),
              (e.Completed = "completed"),
              (e.CompletedRightNow = "completedRightNow"),
              (e.SwitchedChapterRightNow = "switchedChapterRightNow"),
              (e.NoVehiclesBase = "noVehiclesBase"),
              (e.ChapterNotChosen = "chapterNotChosen"));
          })(n || (n = {})),
          (function (e) {
            ((e.None = ""),
              (e.ShowLevel = "show"),
              (e.HideLevel = "hide"),
              (e.HideLevelWithDelay = "hideWithDelay"));
          })(s || (s = {})));
      },
      9430: (e, u, t) => {
        "use strict";
        t.d(u, { r: () => p });
        var r = t(6483),
          a = t.n(r),
          n = t(6179),
          s = t.n(n),
          i = t(2862),
          o = t(5739),
          l = t(5415),
          c = t(9480),
          _ = t(2893);
        const E = "GroupRewards_base_70",
          m = "GroupRewards_item_af",
          d = ({ rewards: e, className: u }) => {
            const t = (0, l.GS)().mediaSize < l.cJ.Medium ? i.h2.Small : i.h2.Big;
            return s().createElement(
              "div",
              { className: a()(E, u) },
              c.UI(e, (e, u) =>
                s().createElement(
                  "div",
                  { key: `reward_${u}_${e.name}`, className: m },
                  s().createElement(o.Q, (0, _.$n)(e, t)),
                ),
              ),
            );
          };
        var A = t(3862);
        const D = "RewardsBlock_base_0e",
          F = "RewardsBlock_groupTitle_2f",
          g = "RewardsBlock_groupRewards_38",
          C = "RewardsBlock_groupRewards__future_b9",
          p = ({ title: e, iconType: u, steps: t, rewards: r, className: n }) =>
            s().createElement(
              "div",
              { className: a()(D, n) },
              s().createElement(A.p, { text: e, type: u, steps: t, className: F }),
              s().createElement(d, { rewards: r, className: a()(g, u === A.Q.future && C) }),
            );
      },
      3862: (e, u, t) => {
        "use strict";
        t.d(u, { p: () => c, Q: () => l });
        var r = t(6483),
          a = t.n(r),
          n = t(280),
          s = t(6179),
          i = t.n(s);
        const o = {
          base: "GroupTitle_base_e8",
          text: "GroupTitle_text_b7",
          divider: "GroupTitle_divider_19",
          divider__left: "GroupTitle_divider__left_d2",
          divider__right: "GroupTitle_divider__right_24",
          inner: "GroupTitle_inner_f2",
          icon: "GroupTitle_icon_62",
          base__now: "GroupTitle_base__now_fa",
          base__future: "GroupTitle_base__future_42",
          steps: "GroupTitle_steps_8d",
        };
        let l;
        !(function (e) {
          ((e.now = "now"), (e.future = "future"));
        })(l || (l = {}));
        const c = ({ text: e, type: u, steps: t, className: r }) =>
          i().createElement(
            "div",
            { className: a()(o.base, o[`base__${u}`], r) },
            i().createElement("div", { className: a()(o.divider, o.divider__left) }),
            i().createElement(
              "div",
              { className: o.inner },
              i().createElement("div", { className: o.icon }),
              i().createElement(n.z, {
                classMix: o.text,
                text: e,
                binding: { steps: i().createElement("span", { className: o.steps, key: t }, t) },
              }),
            ),
            i().createElement("div", { className: a()(o.divider, o.divider__right) }),
          );
      },
      9791: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => pe });
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => I,
            Bar: () => L,
            DefaultScroll: () => O,
            Direction: () => C,
            defaultSettings: () => p,
            useHorizontalScrollApi: () => h,
          }));
        var a = {};
        (t.r(a),
          t.d(a, {
            Area: () => te,
            Bar: () => J,
            Default: () => ue,
            useVerticalScrollApi: () => H,
          }));
        var n = t(6483),
          s = t.n(n),
          i = t(1856),
          o = t(6179),
          l = t.n(o),
          c = t(7515),
          _ = t(3815);
        function E(e, u, t = []) {
          const r = (0, o.useRef)(0),
            a = (0, o.useCallback)(() => window.clearInterval(r.current), t || []);
          (0, o.useEffect)(() => a, [a]);
          const n = (null != t ? t : []).concat([u]);
          return [
            (0, o.useCallback)((t) => {
              ((r.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, n),
            a,
          ];
        }
        var m = t(7727),
          d = t(3138);
        function A(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return D(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return D(e, u);
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
        function D(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, r = new Array(u); t < u; t++) r[t] = e[t];
          return r;
        }
        function F(e, u, t) {
          const r = (0, o.useMemo)(
            () =>
              (function (e, u, t, r) {
                let a,
                  n = !1,
                  s = 0;
                function i() {
                  a && clearTimeout(a);
                }
                function o(...o) {
                  const l = this,
                    c = Date.now() - s;
                  function _() {
                    ((s = Date.now()), t.apply(l, o));
                  }
                  n ||
                    (r && !a && _(),
                    i(),
                    void 0 === r && c > e
                      ? _()
                      : !0 !== u &&
                        (a = setTimeout(
                          r
                            ? function () {
                                a = void 0;
                              }
                            : _,
                          void 0 === r ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((r = t), (t = u), (u = void 0)),
                  (o.cancel = function () {
                    (i(), (n = !0));
                  }),
                  o
                );
              })(t, e),
            u,
          );
          return ((0, o.useEffect)(() => r.cancel, [r]), r);
        }
        var g = t(7030);
        let C;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(C || (C = {}));
        const p = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          B = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: r,
            getWrapperSize: a,
            triggerMouseMoveOnUpdate: n = !1,
          }) => {
            const s = (e, t) => {
              const r = u(e),
                a = r[0],
                n = r[1];
              return (0, c.u)(a, n, t);
            };
            return (l = {}) => {
              const c = l.settings,
                E = void 0 === c ? p : c,
                m = (0, o.useRef)(null),
                D = (0, o.useRef)(null),
                C = (() => {
                  const e = (0, o.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    r = (e, t) => {
                      u(e).delete(t);
                    },
                    a = (e, ...t) => {
                      for (var r, a = A(u(e).values()); !(r = a()).done;) (0, r.value)(...t);
                    };
                  return (0, o.useMemo)(() => ({ on: t, off: r, trigger: a }), []);
                })(),
                B = F(
                  () => {
                    d.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                h = (0, g.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = m.current;
                    u && (t(u, e), C.trigger("change", e), n && B());
                  },
                  onRest: (e) => C.trigger("rest", e),
                  onStart: (e) => C.trigger("start", e),
                  onPause: (e) => C.trigger("pause", e),
                })),
                f = h[0],
                v = h[1],
                b = (0, o.useCallback)(
                  (e, u, t) => {
                    var r;
                    const a = f.scrollPosition.get(),
                      n = (null != (r = f.scrollPosition.goal) ? r : 0) - a;
                    return s(e, u * t + n + a);
                  },
                  [f.scrollPosition],
                ),
                w = (0, o.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const r = m.current;
                    r &&
                      v.start({
                        scrollPosition: s(r, e),
                        immediate: u,
                        reset: t,
                        config: E.animationConfig,
                        from: { scrollPosition: s(r, f.scrollPosition.get()) },
                      });
                  },
                  [v, E.animationConfig, f.scrollPosition],
                ),
                y = (0, o.useCallback)(
                  (e) => {
                    const u = m.current,
                      t = D.current;
                    if (!u || !t) return;
                    const r = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return a(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, E.step),
                      n = b(u, e, r);
                    w(n);
                  },
                  [w, b, E.step],
                ),
                S = (0, o.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && y(r(e)),
                      m.current && C.trigger("mouseWheel", e, f.scrollPosition, u(m.current)));
                  },
                  [f.scrollPosition, y, C],
                ),
                R = ((e, u = []) => {
                  const t = (0, o.useRef)(),
                    r = (0, o.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, o.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [r],
                    ),
                    r
                  );
                })(
                  () =>
                    (0, i.v)(() => {
                      const e = m.current;
                      e &&
                        (w(s(e, f.scrollPosition.goal), { immediate: !0 }),
                        C.trigger("resizeHandled"));
                    }),
                  [w, f.scrollPosition.goal],
                ),
                x = (0, _.z)(() => {
                  const e = m.current;
                  if (!e) return;
                  const u = s(e, f.scrollPosition.goal);
                  (u !== f.scrollPosition.goal && w(u, { immediate: !0 }),
                    C.trigger("recalculateContent"));
                });
              (0, o.useEffect)(
                () => (
                  window.addEventListener("resize", R),
                  () => {
                    window.removeEventListener("resize", R);
                  }
                ),
                [R],
              );
              const T = (0, o.useCallback)((e) => C.trigger("isThumbDraggingChanged", e), [C]);
              return (0, o.useMemo)(
                () => ({
                  getWrapperSize: () => (D.current ? a(D.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? u(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: E.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: S,
                  applyScroll: w,
                  applyStepTo: y,
                  contentRef: m,
                  wrapperRef: D,
                  scrollPosition: v,
                  animationScroll: f,
                  recalculateContent: x,
                  handleIsThumbDragging: T,
                  events: { on: C.on, off: C.off },
                }),
                [f.scrollPosition, w, y, T, C.off, C.on, x, S, v, E.step.clampedArrowStepTimeout],
              );
            };
          },
          h = B({
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
            getDirection: (e) => (e.deltaY > 1 ? C.Next : C.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          f = "HorizontalBar_base_49",
          v = "HorizontalBar_base__nonActive_82",
          b = "HorizontalBar_leftButton_5f",
          w = "HorizontalBar_rightButton_03",
          y = "HorizontalBar_track_0d",
          S = "HorizontalBar_thumb_fd",
          R = "HorizontalBar_rail_32",
          x = "disable",
          T = { pending: !1, offset: 0 },
          P = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          M = () => {},
          k = (e, u) => Math.max(20, e.offsetWidth * u),
          L = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = P, onDrag: r = M }) => {
              const a = (0, o.useRef)(null),
                n = (0, o.useRef)(null),
                d = (0, o.useRef)(null),
                A = (0, o.useRef)(null),
                D = (0, o.useRef)(null),
                F = e.stepTimeout || 100,
                g = (0, o.useState)(T),
                p = g[0],
                B = g[1],
                h = (0, o.useCallback)(
                  (e) => {
                    (B(e),
                      D.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: D.current }));
                  },
                  [r],
                ),
                L = () => {
                  const u = A.current,
                    t = D.current,
                    r = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(r && u && t && a)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    i = Math.min(1, r / a),
                    o = (0, c.u)(0, 1, s / (a - r)),
                    l = (u.offsetWidth - k(u, i)) * o;
                  ((t.style.transform = `translateX(${0 | l}px)`),
                    ((e) => {
                      if (n.current && d.current && A.current && D.current) {
                        if (0 === e)
                          return (n.current.classList.add(x), void d.current.classList.remove(x));
                        if (
                          ((u = A.current),
                          (t = D.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (n.current.classList.remove(x), void d.current.classList.add(x));
                        var u, t;
                        (n.current.classList.remove(x), d.current.classList.remove(x));
                      }
                    })(l));
                },
                N = (0, _.z)(() => {
                  ((() => {
                    const u = D.current,
                      t = A.current,
                      r = e.getWrapperSize(),
                      n = e.getContainerSize();
                    if (!(n && u && r && t)) return;
                    const s = Math.min(1, r / n);
                    ((u.style.width = `${k(t, s)}px`),
                      (u.style.display = "flex"),
                      a.current &&
                        (1 === s ? a.current.classList.add(v) : a.current.classList.remove(v)));
                  })(),
                    L());
                });
              ((0, o.useEffect)(() => (0, i.v)(N)),
                (0, o.useEffect)(
                  () =>
                    (0, i.v)(() => {
                      const u = () => {
                        L();
                      };
                      let t = M;
                      const r = () => {
                        (t(), (t = (0, i.v)(N)));
                      };
                      return (
                        e.events.on("recalculateContent", N),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", r),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", N),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", r));
                        }
                      );
                    }),
                  [e],
                ),
                (0, o.useEffect)(() => {
                  if (!p.pending) return;
                  const u = (u) => {
                      var t;
                      const a = e.contentRef.current;
                      if (!a) return;
                      const n = A.current,
                        s = D.current;
                      if (!a || !n || !s) return;
                      const i = u.screenX - p.offset - n.getBoundingClientRect().x,
                        o = (i / n.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(a, o),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        r({ type: "dragging", thumb: s, thumbOffset: i, contentOffset: o }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), h(T));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, p.offset, p.pending, r, h]));
              const O = E((u) => e.applyStepTo(u), F, [e]),
                I = O[0],
                H = O[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", H, !0),
                  () => document.removeEventListener("mouseup", H, !0)
                ),
                [H],
              );
              const U = (e) => {
                e.target.classList.contains(x) || (0, m.G)("highlight");
              };
              return l().createElement(
                "div",
                { className: s()(f, u.base), ref: a, onWheel: e.handleMouseWheel },
                l().createElement("div", {
                  className: s()(b, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(x) ||
                      0 !== e.button ||
                      ((0, m.G)("play"), I(C.Next));
                  },
                  onMouseUp: H,
                  ref: n,
                  onMouseEnter: U,
                }),
                l().createElement(
                  "div",
                  {
                    className: s()(y, u.track),
                    onMouseDown: (u) => {
                      const r = D.current;
                      if (r && 0 === u.button)
                        if (((0, m.G)("play"), u.target === r))
                          h({ pending: !0, offset: u.screenX - r.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const r = D.current,
                              a = e.contentRef.current;
                            if (!r || !a) return;
                            const n = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + n * u);
                          })(u.screenX > r.getBoundingClientRect().x ? C.Prev : C.Next);
                        }
                    },
                    ref: A,
                    onMouseEnter: U,
                  },
                  l().createElement("div", { ref: D, className: s()(S, u.thumb) }),
                  l().createElement("div", { className: s()(R, u.rail) }),
                ),
                l().createElement("div", {
                  className: s()(w, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(x) ||
                      0 !== e.button ||
                      ((0, m.G)("play"), I(C.Prev));
                  },
                  onMouseUp: H,
                  ref: d,
                  onMouseEnter: U,
                }),
              );
            },
          ),
          N = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          O = ({
            children: e,
            api: u,
            className: t,
            barClassNames: r,
            areaClassName: a,
            classNames: n,
            scrollClassName: i,
            getStepByRailClick: c,
            onDrag: _,
          }) => {
            const E = (0, o.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: s()(N.base, e.base) });
              }, [r]),
              m = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return l().createElement(
              "div",
              { className: s()(N.defaultScroll, t), onWheel: u.handleMouseWheel },
              l().createElement(
                "div",
                { className: s()(N.defaultScrollArea, a) },
                l().createElement(I, { className: i, api: m, classNames: n }, e),
              ),
              l().createElement(L, { getStepByRailClick: c, api: u, onDrag: _, classNames: E }),
            );
          },
          I = ({ api: e, className: u, classNames: t, children: r, style: a }) => (
            (0, o.useEffect)(() => (0, i.v)(e.recalculateContent)),
            l().createElement(
              "div",
              { className: s()(N.base, u), style: a },
              l().createElement(
                "div",
                {
                  className: s()(N.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                l().createElement(
                  "div",
                  { className: s()(N.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          );
        ((I.Bar = L),
          (I.Default = O),
          (I.SeniorityAwards = ({ api: e, className: u, classNames: t, children: r }) => (
            (0, o.useEffect)(() => (0, i.v)(e.recalculateContent)),
            l().createElement(
              "div",
              { className: s()(N.base, u) },
              l().createElement(
                "div",
                { className: s()(N.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                l().createElement(
                  "div",
                  { className: s()(N.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          )));
        const H = B({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? C.Next : C.Prev),
          }),
          U = "VerticalBar_base_f3",
          W = "VerticalBar_base__nonActive_42",
          G = "VerticalBar_topButton_d7",
          $ = "VerticalBar_bottomButton_06",
          z = "VerticalBar_track_df",
          V = "VerticalBar_thumb_32",
          j = "VerticalBar_rail_43",
          X = "disable",
          q = () => {},
          Y = { pending: !1, offset: 0 },
          K = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          Z = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          Q = (e, u) => Math.max(20, e.offsetHeight * u),
          J = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = K, onDrag: r = q }) => {
              const a = (0, o.useRef)(null),
                n = (0, o.useRef)(null),
                d = (0, o.useRef)(null),
                A = (0, o.useRef)(null),
                D = (0, o.useRef)(null),
                F = e.stepTimeout || 100,
                g = (0, o.useState)(Y),
                p = g[0],
                B = g[1],
                h = (0, o.useCallback)(
                  (e) => {
                    (B(e),
                      D.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: D.current }));
                  },
                  [r],
                ),
                f = (0, _.z)(() => {
                  const u = D.current,
                    t = A.current,
                    r = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(r && n && u && t)) return;
                  const s = Math.min(1, r / n);
                  return (
                    (u.style.height = `${Q(t, s)}px`),
                    u.classList.add(V),
                    a.current &&
                      (1 === s ? a.current.classList.add(W) : a.current.classList.remove(W)),
                    s
                  );
                }),
                v = (0, _.z)(() => {
                  const u = A.current,
                    t = D.current,
                    r = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(r && u && t && a)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    i = Math.min(1, r / a),
                    o = (0, c.u)(0, 1, s / (a - r)),
                    l = (u.offsetHeight - Q(u, i)) * o;
                  ((t.style.transform = `translateY(${0 | l}px)`),
                    ((e) => {
                      if (n.current && d.current && A.current && D.current) {
                        if (0 === e)
                          return (n.current.classList.add(X), void d.current.classList.remove(X));
                        if (
                          ((u = A.current),
                          (t = D.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (n.current.classList.remove(X), void d.current.classList.add(X));
                        var u, t;
                        (n.current.classList.remove(X), d.current.classList.remove(X));
                      }
                    })(l));
                }),
                b = (0, _.z)(() => {
                  Z(e, () => {
                    (f(), v());
                  });
                });
              ((0, o.useEffect)(() => (0, i.v)(b)),
                (0, o.useEffect)(() => {
                  const u = () => {
                    Z(e, () => {
                      v();
                    });
                  };
                  let t = q;
                  const r = () => {
                    (t(), (t = (0, i.v)(b)));
                  };
                  return (
                    e.events.on("recalculateContent", b),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", r),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", b),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", r));
                    }
                  );
                }, [e]),
                (0, o.useEffect)(() => {
                  if (!p.pending) return;
                  const u = (u) => {
                      Z(e, (t) => {
                        const a = A.current,
                          n = D.current,
                          s = e.getContainerSize();
                        if (!a || !n || !s) return;
                        const i = u.screenY - p.offset - a.getBoundingClientRect().y,
                          o = (i / a.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, o),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          r({ type: "dragging", thumb: n, thumbOffset: i, contentOffset: o }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        h(Y));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, p.offset, p.pending, r, h]));
              const w = E((u) => e.applyStepTo(u), F, [e]),
                y = w[0],
                S = w[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", S, !0),
                  () => document.removeEventListener("mouseup", S, !0)
                ),
                [S],
              );
              const R = (e) => {
                e.target.classList.contains(X) || (0, m.G)("highlight");
              };
              return l().createElement(
                "div",
                { className: s()(U, u.base), ref: a, onWheel: e.handleMouseWheel },
                l().createElement("div", {
                  className: s()(G, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(X) ||
                      0 !== e.button ||
                      ((0, m.G)("play"), y(C.Next));
                  },
                  ref: n,
                  onMouseEnter: R,
                }),
                l().createElement(
                  "div",
                  {
                    className: s()(z, u.track),
                    onMouseDown: (u) => {
                      const r = D.current;
                      if (r && 0 === u.button)
                        if (((0, m.G)("play"), u.target === r))
                          (e.handleIsThumbDragging(!0),
                            h({ pending: !0, offset: u.screenY - r.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            D.current &&
                              Z(e, (r) => {
                                if (!r) return;
                                const a = t(e),
                                  n = e.clampPosition(r, r.scrollTop + a * u);
                                e.applyScroll(n);
                              });
                          })(u.screenY > r.getBoundingClientRect().y ? C.Prev : C.Next);
                        }
                    },
                    ref: A,
                    onMouseEnter: R,
                  },
                  l().createElement("div", { ref: D, className: u.thumb }),
                  l().createElement("div", { className: s()(j, u.rail) }),
                ),
                l().createElement("div", {
                  className: s()($, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(X) ||
                      0 !== e.button ||
                      ((0, m.G)("play"), y(C.Prev));
                  },
                  onMouseUp: S,
                  ref: d,
                  onMouseEnter: R,
                }),
              );
            },
          ),
          ee = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          ue = ({
            children: e,
            api: u,
            className: t,
            barClassNames: r,
            areaClassName: a,
            scrollClassName: n,
            scrollClassNames: i,
            getStepByRailClick: c,
            onDrag: _,
          }) => {
            const E = (0, o.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: s()(ee.base, e.base) });
              }, [r]),
              m = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return l().createElement(
              "div",
              { className: s()(ee.defaultScroll, t), onWheel: u.handleMouseWheel },
              l().createElement(
                "div",
                { className: s()(ee.area, a) },
                l().createElement(te, { className: n, classNames: i, api: m }, e),
              ),
              l().createElement(J, { getStepByRailClick: c, api: u, onDrag: _, classNames: E }),
            );
          },
          te = ({ className: e, classNames: u, children: t, api: r }) => (
            (0, o.useEffect)(() => (0, i.v)(r.recalculateContent)),
            l().createElement(
              "div",
              { className: s()(ee.base, e), ref: r.wrapperRef, onWheel: r.handleMouseWheel },
              l().createElement(
                "div",
                { className: s()(ee.content, null == u ? void 0 : u.content), ref: r.contentRef },
                t,
              ),
            )
          );
        te.Default = ue;
        const re = { Vertical: a, Horizontal: r };
        "undefined" != typeof Element &&
          (Element.prototype.matches ||
            Element.prototype.webkitMatchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector);
        ("undefined" != typeof document && document.documentElement.style,
          "undefined" != typeof window &&
            ("ontouchstart" in window ||
              (window.DocumentTouch && (document, window.DocumentTouch))),
          "undefined" != typeof navigator && navigator.msMaxTouchPoints,
          "undefined" != typeof navigator && /Chrome/i.test(navigator && navigator.userAgent));
        var ae = t(4179);
        function ne(e, u, t, r, a, n, s) {
          try {
            var i = e[n](s),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(r, a);
        }
        function se(e) {
          return function () {
            var u = this,
              t = arguments;
            return new Promise(function (r, a) {
              var n = e.apply(u, t);
              function s(e) {
                ne(n, r, a, s, i, "next", e);
              }
              function i(e) {
                ne(n, r, a, s, i, "throw", e);
              }
              s(void 0);
            });
          };
        }
        let ie;
        !(function (e) {
          ((e[(e.Idle = 0)] = "Idle"),
            (e[(e.Start = 1)] = "Start"),
            (e[(e.Between = 2)] = "Between"),
            (e[(e.End = 3)] = "End"));
        })(ie || (ie = {}));
        const oe = (e) => {
            const u = (0, o.useState)(ie.Idle),
              t = u[0],
              r = u[1],
              a = e.animationScroll,
              n = e.getContainerSize,
              s = e.getWrapperSize,
              l = e.events,
              c = (0, o.useCallback)(() => {
                const e = a.scrollPosition.get(),
                  u = n() - s();
                switch (!0) {
                  case !u:
                    return r(ie.Idle);
                  case e <= 0:
                    return r(ie.Start);
                  case e >= u:
                    return r(ie.End);
                  default:
                    r(ie.Between);
                }
              }, [a.scrollPosition, n, s]);
            return (
              (0, o.useEffect)(
                () => (
                  (function () {
                    var e = se(function* () {
                      yield (0, i.v)(c);
                    });
                    return function () {
                      return e.apply(this, arguments);
                    };
                  })()(),
                  l.on("change", c),
                  () => l.off("change", c)
                ),
                [l, c],
              ),
              (0, o.useEffect)(() => {
                const e = (function () {
                  var e = se(function* () {
                    (yield (0, ae.Eu)(),
                      yield new Promise((e) => {
                        requestAnimationFrame(() => {
                          requestAnimationFrame(() => {
                            e();
                          });
                        });
                      }),
                      c());
                  });
                  return function () {
                    return e.apply(this, arguments);
                  };
                })();
                return (
                  engine.on("clientResized", e),
                  () => {
                    engine.off("clientResized", e);
                  }
                );
              }, [c]),
              t
            );
          },
          le = { type: "idle" };
        const ce = "ScrollWithLips_base_69",
          _e = "ScrollWithLips_scrollContent_19",
          Ee = "ScrollWithLips_lip_90",
          me = "ScrollWithLips_lip__top_ab",
          de = "ScrollWithLips_lip__bottom_17",
          Ae = "ScrollWithLips_scroll_7e",
          De = "ScrollWithLips_scroll__loaded_b2",
          Fe = "ScrollWithLips_topButton_4e",
          ge = "ScrollWithLips_bottomButton_1e",
          Ce = "ScrollWithLips_track_4f",
          pe = ({ className: e, children: u }) => {
            const t = H();
            !(function (e, u) {
              const t = e.contentRef,
                r = e.wrapperRef,
                a = e.scrollPosition,
                n = e.clampPosition,
                s = e.animationScroll,
                i = e.events,
                l = (0, o.useState)(le),
                c = l[0],
                _ = l[1];
              ((0, o.useEffect)(() => {
                const e = t.current;
                e && (e.style.cursor = "dragging" === c.type ? "grabbing" : "grab");
              }, [t, c.type]),
                (0, o.useEffect)(() => {
                  if ("dragging" !== c.type) return;
                  const e = (e) => {
                      const i = t.current,
                        o = r.current;
                      if (!i || !o) return;
                      const l = c.positionFrom - e.screenY,
                        _ = c.previousScrollPosition + l;
                      a.start(
                        Object.assign(
                          {
                            scrollPosition: n(i, _),
                            from: { scrollPosition: s.scrollPosition.get() },
                          },
                          u && { config: u },
                        ),
                      );
                    },
                    i = () => {
                      (window.removeEventListener("mousemove", e), _({ type: "scrollingToEnd" }));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", i),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", i));
                    }
                  );
                }, [s.scrollPosition, n, t, c, a, r, u]),
                (0, o.useEffect)(() => {
                  if ("scrollingToEnd" !== c.type) return;
                  const e = () => {
                    _(le);
                  };
                  return (s.scrollPosition.idle && e(), i.on("rest", e), () => i.off("rest", e));
                }, [s.scrollPosition, c.type, i]),
                (0, o.useEffect)(() => {
                  const e = t.current;
                  if (!e) return;
                  const u = (e) => {
                    0 === e.button &&
                      _({
                        type: "dragging",
                        positionFrom: e.screenY,
                        previousScrollPosition: s.scrollPosition.get(),
                      });
                  };
                  return (
                    e.addEventListener("mousedown", u),
                    () => e.removeEventListener("mousedown", u)
                  );
                }, [s.scrollPosition, t]));
            })(t);
            const r = oe(t),
              a = r !== ie.Idle;
            return l().createElement(
              "div",
              { className: s()(ce, e) },
              r !== ie.Start &&
                r !== ie.Idle &&
                l().createElement("div", { className: s()(Ee, me) }),
              r !== ie.End && r !== ie.Idle && l().createElement("div", { className: s()(Ee, de) }),
              l().createElement(
                re.Vertical.Area.Default,
                {
                  api: t,
                  barClassNames: {
                    base: s()(Ae, a && De),
                    topButton: Fe,
                    bottomButton: ge,
                    track: Ce,
                  },
                  scrollClassNames: { content: _e },
                },
                u,
              ),
            );
          };
      },
      3942: (e, u, t) => {
        "use strict";
        t.d(u, { D: () => d });
        var r = t(6483),
          a = t.n(r),
          n = t(3649),
          s = t(6179),
          i = t.n(s),
          o = t(2893);
        const l = "Title_base_29",
          c = "Title_chapter_74",
          _ = "Title_buyBPTitle_dd",
          E = "Title_subTitle_52",
          m = R.strings.battle_pass.battlePassBuyView.confirm,
          d = ({ chapter: e, buyBP: u, subTitle: t, className: r }) => {
            const s = (0, n.uF)(m.chapter(), { name: (0, o.pC)(e, !0) });
            return i().createElement(
              "div",
              { className: a()(l, r) },
              i().createElement("span", { className: c }, s),
              i().createElement("span", { className: _ }, u),
              i().createElement("span", { className: E }, t),
            );
          };
      },
      5216: (e, u, t) => {
        "use strict";
        let r, a;
        (!(function (e) {
          ((e.Active = "active"),
            (e.Paused = "paused"),
            (e.Completed = "completed"),
            (e.NotStarted = "notStarted"),
            (e.Disabled = "disabled"));
        })(r || (r = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(a || (a = {})));
      },
      6880: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        const r = {
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
      },
      5287: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        const r = { base: "FormatText_base_d0" };
      },
      1609: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        const r = {
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
        var a = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [u, t, r] = deferred[o], n = !0, s = 0; s < u.length; s++)
            (!1 & r || a >= r) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[s]))
              ? u.splice(s--, 1)
              : ((n = !1), r < a && (a = r));
          if (n) {
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
    (__webpack_require__.j = 4217),
    (() => {
      var e = { 4217: 0, 8872: 0, 1523: 0, 8805: 0, 6488: 0, 2670: 0, 3132: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var r,
            a,
            [n, s, i] = t,
            o = 0;
          if (n.some((u) => 0 !== e[u])) {
            for (r in s) __webpack_require__.o(s, r) && (__webpack_require__.m[r] = s[r]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); o < n.length; o++)
            ((a = n[o]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [1519], () => __webpack_require__(9334));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
