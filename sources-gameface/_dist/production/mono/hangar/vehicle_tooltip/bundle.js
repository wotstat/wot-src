import { r as e } from "../chunks/rolldown-runtime.js";
import {
  $n as s,
  An as t,
  Ba as a,
  Bt as r,
  F as i,
  Fa as l,
  Ja as n,
  St as c,
  Ua as o,
  Va as m,
  Vt as d,
  Xi as u,
  _t as _,
  a as p,
  aa as h,
  ao as x,
  ar as g,
  bn as v,
  c as j,
  cr as b,
  dr as f,
  ea as N,
  fi as y,
  ga as w,
  gn as E,
  hi as P,
  hn as C,
  hr as R,
  jn as O,
  lr as S,
  o as T,
  pr as B,
  rr as k,
  s as L,
  to as $,
  u as I,
  uo as M,
  ur as A,
  vn as G,
  w as V,
  wn as z,
  xt as D,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { a as F, n as X, s as H, t as W } from "../chunks/dynamic_economics_provider.js";
import { r as U, t as J } from "../chunks/tankman_role.js";
var [K, Q] = R("VehicleTooltipModelProvider")(({ observableModel: e }) => {
    const s = {
        ...e.primitives(["status", "stateLevel", "bpEntityValid"]),
        statistics: e.object("statistics"),
        earnings: e.object("earnings"),
        serviceRecords: e.object("serviceRecords"),
        numberOfCrystalEarned: e.arrayClone("earnings.numberOfCrystalEarned"),
        slots: e.arrayClone("statistics.slots"),
        mechanics: e.arrayClone("mechanics"),
      },
      t = B.primitive(() => s.statistics.get().elite),
      a = B.primitive(
        () =>
          (t() && "undefined" !== s.serviceRecords.get().prestigeType) ||
          s.serviceRecords.get().marksOfMastery > 0 ||
          s.serviceRecords.get().marksOnGun > 0 ||
          s.serviceRecords.get().battlesCount > 0,
      ),
      r = B.primitive(() => s.numberOfCrystalEarned.get()[0] ?? 0),
      i = B.primitive(() => s.numberOfCrystalEarned.get()[1] ?? 0),
      l = B.primitive(() => -1 !== s.earnings.get().bonusMultiplier),
      n = B.primitive(
        () =>
          s.earnings.get().bpActive &&
          s.earnings.get().maxBpScore > 0 &&
          s.status.get() !== F.unsuitableToQueue,
      ),
      c = B.primitive(() => h(s.mechanics.get(), (e) => e.priority >= 1));
    return {
      ...s,
      computes: {
        elite: t,
        serviceRecords: a,
        battlePoints: n,
        currentNumberOfCrystal: r,
        maxNumberOfCrystal: i,
        hasBonusMultiplier: l,
        hasSpecialMechanics: c,
      },
    };
  }, w),
  Z = "INACTIVE",
  q = "ACTIVE",
  Y = "CANCELLED",
  ee = "critical",
  se = "info",
  te = { 1: 3, 2: 2, 3: 1, 4: 4 },
  ae = (e) => {
    switch (e) {
      case ee:
        return "#f31201";
      case se:
        return "#7ab300";
      default:
        return "#ee7000";
    }
  };
function re(e) {
  return "string" == typeof e && e in t;
}
var ie = {
    [t.lightTank]: "LT",
    [t.mediumTank]: "MT",
    [t.heavyTank]: "HT",
    [t.SPG]: "SPG",
    [t["AT-SPG"]]: "ATSPG",
  },
  le = "level",
  ne = "role",
  ce = "crewRoles",
  oe = "battles",
  me = "wins",
  de = "days",
  ue = "hours";
var _e = "Row_a52ddf2a",
  pe = "Row_title_6c4bc0c8",
  he = "Row_title__colon_6c475686",
  xe = e(P()),
  ge = k("Row", _e);
function ve({ className: e, title: t, params: a, children: r }) {
  const i = M.resolve("strings");
  return (0, xe.jsxs)(ge, {
    className: e,
    children: [
      void 0 !== t &&
        (0, xe.jsxs)(xe.Fragment, {
          children: [
            (0, xe.jsx)(s, { className: pe, path: `tooltips.vehicle.${t}`, params: a }),
            (0, xe.jsx)("div", {
              className: $(pe, he),
              children: i.readOrEmpty("common.common.colon"),
            }),
          ],
        }),
      r,
    ],
  });
}
var je = "BattlePassPoints_row__battlePassPoints_4e755749",
  be = "BattlePassPoints_row__reward_4e755749",
  fe = "BattlePassPoints_leftColumn_b241ec5",
  Ne = "BattlePassPoints_row_bfb51350",
  ye = "BattlePassPoints_property_c8f33cb7",
  we = "BattlePassPoints_property__limitReached_aee9a154",
  Ee = "BattlePassPoints_currency_28a36732",
  Pe = "BattlePassPoints_icon_bf5b9876",
  Ce = "BattlePassPoints_text_fe4f3086",
  Re = function ({
    title: e,
    value: s,
    currentBpScore: t = 0,
    limitReached: a = !1,
    reward: r = !1,
    battlePassPoints: i = !1,
  }) {
    const l = M.resolve("strings"),
      n = y(
        "hangar.carousel.cards.bp_points_bonus",
        "hangar.carousel.cards.bp_points_bonus_upscale",
      );
    return (0, xe.jsxs)(ve, {
      className: $(Ne, r && be, i && je),
      children: [
        (0, xe.jsx)("div", {
          className: $(fe),
          children: (0, xe.jsxs)(_, {
            type: "battlePassPointsBonus",
            size: D.small,
            classNames: { base: Ee },
            children: [
              t > 0 &&
                (0, xe.jsxs)(xe.Fragment, {
                  children: [
                    (0, xe.jsx)("div", { children: x.formatNumber("integral", t) }),
                    (0, xe.jsx)("div", {
                      className: ye,
                      children: l.readOrEmpty("common.common.slash"),
                    }),
                  ],
                }),
              void 0 !== s &&
                (0, xe.jsx)("div", {
                  className: $(ye, a && we),
                  children: x.formatNumber("integral", s),
                }),
              (0, xe.jsx)(g, { className: Pe, width: 24, height: 24, path: n }),
            ],
          }),
        }),
        (0, xe.jsx)("div", {
          className: Ce,
          children: l.readOrEmpty(`tooltips.vehicle.battlePass.${e}`),
        }),
      ],
    });
  },
  Oe = b(function () {
    const { model: e } = Q(),
      { maxBpScore: s, currentBpScore: t, bpReward: a } = e.earnings.get();
    return (0, xe.jsx)(xe.Fragment, {
      children:
        s > t
          ? (0, xe.jsxs)(xe.Fragment, {
              children: [
                (0, xe.jsx)(Re, {
                  currentBpScore: t,
                  title: "earningLimit",
                  value: s,
                  battlePassPoints: !0,
                }),
                (0, xe.jsx)(Re, { title: "reward", value: a, limitReached: !0 }),
              ],
            })
          : (0, xe.jsx)(Re, { title: "limitReached", reward: !0 }),
    });
  }),
  Se = "Bonds_row__bonds_34572d0b",
  Te = "Bonds_row__limitReached_34572d0b",
  Be = "Bonds_leftColumn_a37479d6",
  ke = "Bonds_row_eedc2ff2",
  Le = "Bonds_row__displayTimer_34572d0b",
  $e = "Bonds_timerWrapper_520aac9d",
  Ie = "Bonds_timer_49fb046e",
  Me = "Bonds_currency_e32a6c4d",
  Ae = "Bonds_icon_4ddeb604",
  Ge = "Bonds_property_57b4db27",
  Ve = "Bonds_property__limit_e8d508c6",
  ze = "Bonds_property__earningProgress_1dc4f208",
  De = "Bonds_text_dad80fb6",
  Fe = b(function () {
    const { model: e } = Q(),
      { crystalTimeout: s } = e.earnings.get(),
      t = e.computes.maxNumberOfCrystal() <= e.computes.currentNumberOfCrystal(),
      a = e.computes.currentNumberOfCrystal() <= 0,
      r = t && s,
      l = M.resolve("strings");
    return (0, xe.jsxs)(ve, {
      className: $(ke, r && Le, t ? Te : Se),
      children: [
        (0, xe.jsx)("div", {
          className: Be,
          children: (0, xe.jsx)(_, {
            reverse: !0,
            size: D.small,
            classNames: { base: Me, icon: Ae },
            type: t ? "limitReachedCrystal" : c.crystal,
            children: r
              ? (0, xe.jsx)(i, { className: $e, classNames: { icon: Ie }, start: s })
              : (0, xe.jsxs)(xe.Fragment, {
                  children: [
                    (0, xe.jsx)("div", {
                      className: $(Ge, Ve),
                      children: x.formatNumber("integral", e.computes.maxNumberOfCrystal()),
                    }),
                    (0, xe.jsx)("div", {
                      className: $(Ge, !a && Ve),
                      children: l.readOrEmpty("common.common.slash"),
                    }),
                    (0, xe.jsx)("div", {
                      className: $(Ge, !a && ze),
                      children: x.formatNumber("integral", e.computes.currentNumberOfCrystal()),
                    }),
                  ],
                }),
          }),
        }),
        (0, xe.jsx)("div", {
          className: De,
          children: l.readOrEmpty(
            "tooltips.vehicle.bonds." + ("" + (t ? "limitReached" : "earningLimit")),
          ),
        }),
      ],
    });
  }),
  Xe = {
    row__multiplier: "Earnings_row__multiplier_16fcb8c8",
    leftColumn: "Earnings_leftColumn_940b9a0e",
    earnings: "Earnings_96294922",
    row: "Earnings_row_850c7c9b",
    icon: "Earnings_icon_c10adc2c",
    currency: "Earnings_currency_61ac411b",
    text: "Earnings_text_a6c4a45b",
  },
  He = b(function () {
    const { model: e } = Q(),
      { xp: s } = e.earnings.get(),
      t = M.resolve("strings");
    return (0, xe.jsxs)(ve, {
      className: Xe.row,
      children: [
        (0, xe.jsx)("div", {
          className: Xe.leftColumn,
          children: (0, xe.jsx)(_, {
            reverse: !0,
            classNames: { base: Xe.currency, icon: Xe.icon },
            size: D.small,
            type: e.computes.elite() ? c.eliteXp : c.tankXP,
            children: (0, xe.jsx)("div", { children: x.formatNumber("integral", s) }),
          }),
        }),
        (0, xe.jsx)("div", { className: Xe.text, children: t.readOrEmpty("tooltips.vehicle.xp") }),
      ],
    });
  }),
  We = b(function () {
    const { model: e } = Q(),
      { bonusMultiplier: s } = e.earnings.get(),
      t = M.resolve("strings"),
      a = y("hangar.carousel.cards.bonus", "hangar.carousel.cards.bonus_upscale");
    return (0, xe.jsxs)(ve, {
      className: $(Xe.row, H(s) && Xe.row__multiplier),
      children: [
        (0, xe.jsx)("div", {
          className: Xe.leftColumn,
          children: (0, xe.jsxs)(_, {
            type: "bonus",
            size: D.small,
            classNames: { base: Xe.currency },
            children: [
              (0, xe.jsx)("div", { children: t.readOrEmpty("common.multiplierSmall") }),
              (0, xe.jsx)("div", { children: x.formatNumber("integral", s) }),
              (0, xe.jsx)(g, { path: a, className: Xe.icon, width: 24, height: 24 }),
            ],
          }),
        }),
        (0, xe.jsx)("div", {
          className: Xe.text,
          children: t.readOrEmpty("tooltips.vehicle.dailyXPFactor"),
        }),
      ],
    });
  }),
  Ue = k("Earnings", Xe.base),
  Je = b(function ({ className: e }) {
    const s = X()?.model,
      t = !s || s.isCrystalEarnEnabled.get(),
      a = !s || s.isDailyMultipliedXpEnabled.get(),
      { model: r } = Q(),
      { crystalEarning: i } = r.earnings.get(),
      l = M.resolve("strings");
    return (0, xe.jsxs)(Ue, {
      className: e,
      children: [
        (0, xe.jsx)("div", {
          className: Xe.earnings,
          children: l.readOrEmpty("tooltips.tankCaruselTooltip.earnings.header"),
        }),
        a && r.computes.hasBonusMultiplier() && (0, xe.jsx)(We, {}),
        (0, xe.jsx)(He, {}),
        t && i && (0, xe.jsx)(Fe, {}),
        r.bpEntityValid.get() && r.computes.battlePoints() && (0, xe.jsx)(Oe, {}),
      ],
    });
  }),
  Ke = "Crew_2339425e",
  Qe = "Crew_79af07ed",
  Ze = "Crew_icon_26258836",
  qe = "Crew_sign_a456f030",
  Ye = b(function ({ className: e }) {
    const { model: s } = Q(),
      t = s.slots.get(),
      a = M.resolve("strings");
    return (0, xe.jsx)(ve, {
      title: ce,
      params: { count: t.length },
      className: $(Ke, e),
      children: N(t, (e) =>
        (0, xe.jsxs)(
          "div",
          {
            className: Qe,
            children: [
              (0, xe.jsx)(J, { role: u(e.roles, 0), className: Ze }),
              e.roles.length > 1 &&
                (0, xe.jsx)("div", {
                  className: qe,
                  children: a.readOrEmpty("crew_perks.sign.plus"),
                }),
            ],
          },
          e.id,
        ),
      ),
    });
  }),
  es = "Rent_leftColumn_a909b981",
  ss = "Rent_rentValue_f91a4efd",
  ts = "Rent_text_94f0c0d7";
function as({ rentPeriodLeft: e, rentType: s }) {
  const t = M.resolve("strings"),
    a = y("ui_kit.rental_counter.rent_x24x24", "ui_kit.rental_counter.rent_x48x48");
  return (0, xe.jsxs)(ve, {
    children: [
      (0, xe.jsxs)("div", {
        className: es,
        children: [
          (0, xe.jsx)("div", { className: ss, children: x.formatNumber("integral", Math.ceil(e)) }),
          (0, xe.jsx)(g, { path: a, width: 24, height: 24 }),
        ],
      }),
      (0, xe.jsx)("div", {
        className: ts,
        children: t.readOrEmpty(`tooltips.vehicle.rentLeft.${s}`),
      }),
    ],
  });
}
var rs = b(function () {
    const { model: e } = Q(),
      { rentLeftTime: s, rentLeftBattles: t, rentLeftWins: r } = e.statistics.get(),
      i = (function (e) {
        const s = n(e);
        return o(s, m(1)) ? a(s, de) : a(s, ue);
      })(s);
    return s > 0
      ? (0, xe.jsx)(as, { rentPeriodLeft: i.value, rentType: i.unit })
      : t > 0
        ? (0, xe.jsx)(as, { rentPeriodLeft: t, rentType: oe })
        : r > 0
          ? (0, xe.jsx)(as, { rentPeriodLeft: r, rentType: me })
          : null;
  }),
  is = "Role_c276c189",
  ls = "Role_vehicleRoleIcon_a0c92760",
  ns = "Role_property_8f6d69d9",
  cs = b(function ({ className: e }) {
    const { model: s } = Q(),
      { type: t, role: a } = s.statistics.get(),
      i = M.resolve("strings");
    return (0, xe.jsxs)(ve, {
      className: $(is, e),
      title: ne,
      children: [
        (0, xe.jsx)(r, { classNames: { icon: ls }, roleKey: v(a), size: d.x16x16 }),
        re(t) &&
          (0, xe.jsx)("div", {
            className: ns,
            children: i.readOrEmpty(`menu.roleExp.roleGroupName.role_${ie[t]}_${v(a)}`),
          }),
      ],
    });
  }),
  os = M.resolve("strings"),
  ms = b(function ({ className: e }) {
    return (0, xe.jsx)(ve, {
      className: e,
      children: os.readOrEmpty("tooltips.vehicle.telecomRentalsRenting"),
    });
  }),
  ds = {
    leftColumn: "TradeIn_leftColumn_e8d75ad6",
    tradeInIcon: "TradeIn_tradeInIcon_2cde5b72",
    text: "TradeIn_text_1e5d2ead",
  },
  us = M.resolve("strings"),
  _s = b(function ({ className: e }) {
    return (0, xe.jsxs)(ve, {
      className: $(ds.base, e),
      children: [
        (0, xe.jsx)("div", {
          className: ds.leftColumn,
          children: (0, xe.jsx)("div", { className: ds.tradeInIcon }),
        }),
        (0, xe.jsx)("div", {
          className: ds.text,
          children: us.readOrEmpty("tooltips.vehicle.trade"),
        }),
      ],
    });
  }),
  ps = "WotPlus_wotPlus_c07472c2",
  hs = "WotPlus_wotPlus__timer_fb00f649",
  xs = b(function ({ className: e }) {
    const { model: t } = Q(),
      { wotPlusExpiryTime: a, wotPlusState: r } = t.earnings.get(),
      i = M.resolve("strings");
    return (0, xe.jsxs)(xe.Fragment, {
      children: [
        (0, xe.jsx)(ve, {
          className: e,
          children: (0, xe.jsx)("div", {
            className: ps,
            children: i.readOrEmpty("tooltips.vehicle.wotPlusRenting.title"),
          }),
        }),
        r !== q &&
          (0, xe.jsx)(ve, {
            className: e,
            children: (() => {
              switch (r) {
                case Y:
                  return (0, xe.jsx)(s, {
                    upgradeLegacy: !0,
                    className: $(ps, hs),
                    path: "tooltips.vehicle.wotPlusRenting.remainingTime",
                    params: { time: (0, xe.jsx)(j, { datetime: a, format: "ShortDateTime" }) },
                  });
                case Z:
                  return (0, xe.jsx)("div", {
                    className: $(ps, hs),
                    children: i.readOrEmpty("tooltips.vehicle.wotPlusRenting.inactive"),
                  });
                default:
                  return (console.error(`Unknown wotPlus state: ${r}`), null);
              }
            })(),
          }),
      ],
    });
  }),
  gs = "Header_name_154815cc",
  vs = "Header_tier_e0bb96ee",
  js = "Header_level_d1428bec",
  bs = "Header_tierText_ab47090b",
  fs = "Header_row_d4a891e5",
  Ns = k("Header"),
  ys = b(function ({ className: e }) {
    const { model: t } = Q(),
      { wotPlus: a, telecomRent: r, tradeIn: i } = t.earnings.get(),
      { name: n, role: c, type: o, elite: m, level: d } = t.statistics.get(),
      u = v(c);
    return (0, xe.jsxs)(Ns, {
      className: e,
      children: [
        (0, xe.jsx)("div", { className: gs, children: n }),
        (0, xe.jsx)(ve, {
          className: vs,
          title: le,
          children: (0, xe.jsx)(s, {
            className: bs,
            path: `tooltips.tankCaruselTooltip.vehicleType.tier.${m ? "elite" : "normal"}.${l(o)}`,
            params: { tier: (0, xe.jsx)(O, { value: d, className: js }) },
          }),
        }),
        "without_role" !== u && u !== z.spg && (0, xe.jsx)(cs, { className: fs }),
        (0, xe.jsx)(Ye, { className: fs }),
        a && (0, xe.jsx)(xs, { className: fs }),
        r && (0, xe.jsx)(ms, { className: fs }),
        i && (0, xe.jsx)(_s, {}),
        (0, xe.jsx)(rs, {}),
      ],
    });
  }),
  ws = "EliteSystem_leftColumn_6aa7810f",
  Es = "EliteSystem_c476a5a0",
  Ps = "EliteSystem_eliteSystem_5a135969",
  Cs = "EliteSystem_eliteSystem__prestige_2b06b89c",
  Rs = "EliteSystem_values_c91f1a15",
  Os = "EliteSystem_currency_4591b107",
  Ss = "EliteSystem_icon_505ae9fd",
  Ts = "EliteSystem_slash_f65daa35",
  Bs = "EliteSystem_xp_4e0b1db9",
  ks = "EliteSystem_progressBarBorder_45636892",
  Ls = b(function ({ className: e }) {
    const s = M.resolve("strings"),
      { model: t } = Q(),
      {
        prestigeLevel: a,
        prestigeGrade: r,
        prestigeType: i,
        prestigeXp: l,
        prestigeXpNextLevel: n,
      } = t.serviceRecords.get(),
      o = i === T.prestige;
    return (0, xe.jsxs)(ve, {
      className: $(Es, e),
      children: [
        (0, xe.jsx)("div", {
          className: ws,
          children: (0, xe.jsx)(p, { level: a, grade: r, type: i, size: L.xs }),
        }),
        (0, xe.jsxs)("div", {
          className: $(Ps, o && Cs),
          children: [
            (0, xe.jsxs)("div", {
              className: Rs,
              children: [
                (0, xe.jsx)("div", {
                  children: s.readOrEmpty(
                    "tooltips.tankCaruselTooltip.serviceRecords." +
                      (o ? "prestigeEliteSystem" : "eliteSystem"),
                  ),
                }),
                !o &&
                  (0, xe.jsxs)(_, {
                    reverse: !0,
                    size: D.small,
                    type: c.tankXP,
                    classNames: { base: Os, icon: Ss },
                    children: [
                      (0, xe.jsx)("div", { children: x.formatNumber("integral", n) }),
                      (0, xe.jsx)("div", {
                        className: Ts,
                        children: s.readOrEmpty("common.common.slash"),
                      }),
                      (0, xe.jsx)("div", {
                        className: Bs,
                        children: x.formatNumber("integral", l),
                      }),
                    ],
                  }),
              ],
            }),
            !o &&
              (0, xe.jsx)(V, {
                value: l,
                size: "small",
                maxValue: n,
                classNames: { background: ks },
              }),
          ],
        }),
      ],
    });
  }),
  $s = {
    leftColumn: "ServiceRecords_leftColumn_c596dc1b",
    title: "ServiceRecords_title_40d609e8",
    eliteSystem: "ServiceRecords_eliteSystem_aeef0cfd",
    text: "ServiceRecords_text_e426fb24",
  },
  Is = b(function () {
    const { model: e } = Q(),
      { marksOnGunPercentage: t, marksOnGun: a } = e.serviceRecords.get(),
      r = M.resolve("strings");
    return (0, xe.jsxs)(ve, {
      children: [
        (0, xe.jsxs)("div", {
          className: $s.leftColumn,
          children: [
            (0, xe.jsx)(s, {
              upgradeLegacy: !0,
              path: "common.percentValue",
              params: { value: x.formatReal("woZeroDigits", Number(t)) },
            }),
            (0, xe.jsx)(g, { path: `library.marksOnGun.mark_${a}`, width: 24, height: 24 }),
          ],
        }),
        (0, xe.jsx)("div", {
          className: $s.text,
          children: r.pluralOrEmpty("achievements.marksOnGun.count", a),
        }),
      ],
    });
  }),
  Ms = b(function () {
    const { model: e } = Q(),
      { marksOfMastery: t } = e.serviceRecords.get(),
      a = y(
        `tooltip.proficiency.class_icons_${te[t]}`,
        `tooltip.proficiency.class_icons_${te[t]}_upscale`,
      );
    return (0, xe.jsxs)(ve, {
      children: [
        (0, xe.jsx)("div", {
          className: $s.leftColumn,
          children: (0, xe.jsx)(g, { path: a, width: 24, height: 24 }),
        }),
        (0, xe.jsx)(s, { className: $s.text, path: `achievements.markOfMastery${te[t]}` }),
      ],
    });
  });
function As({ rate: e }) {
  const t = M.resolve("strings");
  return (0, xe.jsxs)(ve, {
    children: [
      (0, xe.jsx)(s, {
        upgradeLegacy: !0,
        className: $s.leftColumn,
        path: "common.percentValue",
        params: { value: x.formatNumber("integral", Math.round(e)) },
      }),
      (0, xe.jsx)("div", { className: $s.text, children: t.readOrEmpty("achievements.winRate") }),
    ],
  });
}
var Gs,
  Vs,
  zs = k("ServiceRecords", $s.base),
  Ds = b(function ({ className: e }) {
    const { model: s } = Q(),
      {
        prestigeType: t,
        marksOfMastery: a,
        winsCount: r,
        battlesCount: i,
        marksOnGun: l,
      } = s.serviceRecords.get(),
      n = M.resolve("strings"),
      c = i > 0 ? (r / i) * 100 : 0;
    return (0, xe.jsxs)(zs, {
      className: e,
      children: [
        (0, xe.jsx)("div", {
          className: $s.title,
          children: n.readOrEmpty("tooltips.tankCaruselTooltip.serviceRecords.header"),
        }),
        s.computes.elite() && "undefined" !== t && (0, xe.jsx)(Ls, { className: $s.eliteSystem }),
        a > 0 && (0, xe.jsx)(Ms, {}),
        l > 0 && (0, xe.jsx)(Is, {}),
        i > 0 && (0, xe.jsx)(As, { rate: c }),
      ],
    });
  }),
  Fs = {
    gradient: "SpecialAbility_gradient_73f7ba6b",
    leftColumn: "SpecialAbility_leftColumn_7e97137f",
    rightColumn: "SpecialAbility_rightColumn_4229b20e",
    title: "SpecialAbility_title_10243315",
    icon: "SpecialAbility_icon_eed3b29c",
    text: "SpecialAbility_text_f255c0f5",
  },
  Xs = k("SpecialAbility", Fs.base),
  Hs = b(function ({ className: e }) {
    const { model: t } = Q(),
      a = t.mechanics.get(),
      r = M.resolve("strings"),
      i = (e) => (e === U.GOLD ? "special" : "common");
    return (0, xe.jsxs)(Xs, {
      className: e,
      children: [
        (0, xe.jsx)("div", { className: Fs.gradient }),
        N(a, (e, t) => {
          if (!(e.priority < 1))
            return (0, xe.jsxs)(
              ve,
              {
                children: [
                  (0, xe.jsx)("div", {
                    className: Fs.leftColumn,
                    children: (0, xe.jsx)(g, {
                      path:
                        e.rank === U.GOLD
                          ? `vehicle_hub.mechanics.special.x48x48.${e.name}`
                          : `vehicle_hub.mechanics.x48x48.${e.name}`,
                      width: 48,
                      height: 48,
                      className: Fs.icon,
                    }),
                  }),
                  (0, xe.jsxs)("div", {
                    className: Fs.rightColumn,
                    children: [
                      (0, xe.jsx)("div", {
                        className: Fs.title,
                        children: r.readOrEmpty(
                          `vehicle_hub.abilities.${i(e.rank)}.name.${e.name}`,
                        ),
                      }),
                      (0, xe.jsx)("div", {
                        className: Fs.text,
                        children: (0, xe.jsx)(s, {
                          split: !0,
                          path: `vehicle_hub.abilities.${i(e.rank)}.shortDescription.${e.name}`,
                        }),
                      }),
                    ],
                  }),
                ],
              },
              t,
            );
        }),
      ],
    });
  }),
  Ws = "Tooltip_decorator_9aef02ef",
  Us = "Tooltip_fdfde46e",
  Js = "Tooltip_base__elite_ae2bf179",
  Ks = "Tooltip_vehicleType_b877a704",
  Qs = "Tooltip_vehicleType__elite_bb248964",
  Zs = "Tooltip_section_b726d2f2",
  qs = "Tooltip_section__header_c649b074",
  Ys = "Tooltip_section__earnings_e52798af",
  et = "Tooltip_status_29b423b3",
  st = b(function ({ className: e }) {
    const { model: t } = Q(),
      { type: a } = t.statistics.get();
    return (0, xe.jsx)(I, {
      className: e,
      children: (0, xe.jsxs)(I.Decorator, {
        className: Ws,
        children: [
          re(a) &&
            (0, xe.jsx)(C, {
              type: a,
              premium: t.computes.elite(),
              size: E.x64x64,
              className: $(Ks, t.computes.elite() && Qs),
            }),
          (0, xe.jsxs)("div", {
            className: $(Us, t.computes.elite() && Js),
            children: [
              (0, xe.jsx)(ys, { className: $(Zs, qs) }),
              t.computes.hasSpecialMechanics() && (0, xe.jsx)(Hs, { className: Zs }),
              (0, xe.jsx)(Je, { className: $(Zs, Ys) }),
              t.computes.serviceRecords() && (0, xe.jsx)(Ds, { className: Zs }),
              (0, xe.jsx)(s, {
                upgradeLegacy: !0,
                style: { color: ae(t.stateLevel.get()) },
                className: et,
                path: `tooltips.vehicleStatus.${t.status.get()}.header`,
                params: {
                  icon: (0, xe.jsx)(g, {
                    path: "library.premium_igr_small",
                    width: 26,
                    height: 16,
                  }),
                },
              }),
            ],
          }),
        ],
      }),
    });
  }),
  tt = M.resolve("aliases");
A(
  new f()
    .add(K)
    .add(S)
    .addWithProps(
      W,
      ((Gs = (e) => e.common.shared.DynamicEconomics("resId")),
      (Vs = tt),
      { options: { rootId: Vs.read(Gs) } }),
    )
    .render((0, xe.jsx)(st, {})),
);
