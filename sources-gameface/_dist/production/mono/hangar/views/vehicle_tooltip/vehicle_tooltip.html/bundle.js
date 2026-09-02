import { j as e, f as s, L as t } from "../../../chunks/vendor.js";
import {
  i as a,
  c as r,
  aE as i,
  n as l,
  G as n,
  dj as c,
  dk as o,
  dl as m,
  cj as d,
  ax as u,
  r as p,
  au as _,
  o as h,
  aJ as x,
  aI as g,
  b9 as v,
  av as j,
  aK as b,
  bZ as f,
  a6 as N,
  aO as y,
  by as E,
  dm as P,
  S as w,
  dn as C,
  bz as R,
  aT as T,
  aa as O,
  H as S,
  dp as k,
  dq as B,
  cu as L,
  dr as I,
  ds as M,
  bx as $,
  aU as G,
  J as A,
  E as z,
  F as V,
} from "../../../chunks/lib.js";
import { f as D, g as F, i as H, u as X, M as W, h as J } from "../../../chunks/index.js";
import { T as K } from "../../../chunks/tankman_role.js";
/* empty css                    */ const [U, Z] = a("VehicleTooltipModelProvider")(
    ({ observableModel: e }) => {
      const s = {
          ...e.primitives(["status", "stateLevel", "bpEntityValid"]),
          statistics: e.object("statistics"),
          earnings: e.object("earnings"),
          serviceRecords: e.object("serviceRecords"),
          numberOfCrystalEarned: e.arrayClone("earnings.numberOfCrystalEarned"),
          slots: e.arrayClone("statistics.slots"),
          mechanics: e.arrayClone("mechanics"),
        },
        t = r.primitive(() => s.statistics.get().elite),
        a = r.primitive(
          () =>
            (t() && "undefined" !== s.serviceRecords.get().prestigeType) ||
            s.serviceRecords.get().marksOfMastery > 0 ||
            s.serviceRecords.get().marksOnGun > 0 ||
            s.serviceRecords.get().battlesCount > 0,
        ),
        l = r.primitive(() => s.numberOfCrystalEarned.get()[0] ?? 0),
        n = r.primitive(() => s.numberOfCrystalEarned.get()[1] ?? 0),
        c = r.primitive(() => -1 !== s.earnings.get().bonusMultiplier),
        o = r.primitive(
          () =>
            s.earnings.get().bpActive &&
            s.earnings.get().maxBpScore > 0 &&
            s.status.get() !== D.unsuitableToQueue,
        ),
        m = r.primitive(() => i(s.mechanics.get(), (e) => e.priority >= F));
      return {
        ...s,
        computes: {
          elite: t,
          serviceRecords: a,
          battlePoints: o,
          currentNumberOfCrystal: l,
          maxNumberOfCrystal: n,
          hasBonusMultiplier: c,
          hasSpecialMechanics: m,
        },
      };
    },
    l,
  ),
  q = "INACTIVE",
  Q = "ACTIVE",
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
  return "string" == typeof e && e in n;
}
const ie = {
    [n.lightTank]: "LT",
    [n.mediumTank]: "MT",
    [n.heavyTank]: "HT",
    [n.SPG]: "SPG",
    [n["AT-SPG"]]: "ATSPG",
  },
  le = "level",
  ne = "role",
  ce = "crewRoles",
  oe = "battles",
  me = "wins",
  de = "days",
  ue = "hours";
const pe = "Row_title_6c4bc0c8",
  _e = "Row_title__colon_6c475686",
  he = u("Row", "Row_a52ddf2a");
function xe({ className: t, title: a, params: r, children: i }) {
  const l = p.resolve("strings");
  return e.jsxs(he, {
    className: t,
    children: [
      void 0 !== a &&
        e.jsxs(e.Fragment, {
          children: [
            e.jsx(_, { className: pe, path: `tooltips.vehicle.${a}`, params: r }),
            e.jsx("div", { className: s(pe, _e), children: l.readOrEmpty("common.common.colon") }),
          ],
        }),
      i,
    ],
  });
}
const ge = "BattlePassPoints_row__battlePassPoints_4e755749",
  ve = "BattlePassPoints_row__reward_4e755749",
  je = "BattlePassPoints_leftColumn_b241ec5",
  be = "BattlePassPoints_row_bfb51350",
  fe = "BattlePassPoints_property_c8f33cb7",
  Ne = "BattlePassPoints_property__limitReached_aee9a154",
  ye = "BattlePassPoints_currency_28a36732",
  Ee = "BattlePassPoints_icon_bf5b9876",
  Pe = "BattlePassPoints_text_fe4f3086",
  we = function ({
    title: t,
    value: a,
    currentBpScore: r = 0,
    limitReached: i = !1,
    reward: l = !1,
    battlePassPoints: n = !1,
  }) {
    const c = p.resolve("strings"),
      o = h(
        "hangar.carousel.cards.bp_points_bonus",
        "hangar.carousel.cards.bp_points_bonus_upscale",
      );
    return e.jsxs(xe, {
      className: s(be, l && ve, n && ge),
      children: [
        e.jsx("div", {
          className: s(je),
          children: e.jsxs(x, {
            type: "battlePassPointsBonus",
            size: g.small,
            classNames: { base: ye },
            children: [
              r > 0 &&
                e.jsxs(e.Fragment, {
                  children: [
                    e.jsx("div", { children: v.formatNumber("integral", r) }),
                    e.jsx("div", { className: fe, children: c.readOrEmpty("common.common.slash") }),
                  ],
                }),
              void 0 !== a &&
                e.jsx("div", {
                  className: s(fe, i && Ne),
                  children: v.formatNumber("integral", a),
                }),
              e.jsx(j, { className: Ee, width: 24, height: 24, path: o }),
            ],
          }),
        }),
        e.jsx("div", {
          className: Pe,
          children: c.readOrEmpty(`tooltips.vehicle.battlePass.${t}`),
        }),
      ],
    });
  },
  Ce = t(function () {
    const { model: s } = Z(),
      { maxBpScore: t, currentBpScore: a, bpReward: r } = s.earnings.get();
    return e.jsx(e.Fragment, {
      children:
        t > a
          ? e.jsxs(e.Fragment, {
              children: [
                e.jsx(we, {
                  currentBpScore: a,
                  title: "earningLimit",
                  value: t,
                  battlePassPoints: !0,
                }),
                e.jsx(we, { title: "reward", value: r, limitReached: !0 }),
              ],
            })
          : e.jsx(we, { title: "limitReached", reward: !0 }),
    });
  }),
  Re = "Bonds_row__bonds_34572d0b",
  Te = "Bonds_row__limitReached_34572d0b",
  Oe = "Bonds_leftColumn_a37479d6",
  Se = "Bonds_row_eedc2ff2",
  ke = "Bonds_row__displayTimer_34572d0b",
  Be = "Bonds_timerWrapper_520aac9d",
  Le = "Bonds_timer_49fb046e",
  Ie = "Bonds_currency_e32a6c4d",
  Me = "Bonds_icon_4ddeb604",
  $e = "Bonds_property_57b4db27",
  Ge = "Bonds_property__limit_e8d508c6",
  Ae = "Bonds_property__earningProgress_1dc4f208",
  ze = "Bonds_text_dad80fb6",
  Ve = t(function () {
    const { model: t } = Z(),
      { crystalTimeout: a } = t.earnings.get(),
      r = t.computes.maxNumberOfCrystal() <= t.computes.currentNumberOfCrystal(),
      i = t.computes.currentNumberOfCrystal() <= 0,
      l = r && a,
      n = p.resolve("strings");
    return e.jsxs(xe, {
      className: s(Se, l && ke, r ? Te : Re),
      children: [
        e.jsx("div", {
          className: Oe,
          children: e.jsx(x, {
            reverse: !0,
            size: g.small,
            classNames: { base: Ie, icon: Me },
            type: r ? "limitReachedCrystal" : b.crystal,
            children: l
              ? e.jsx(f, { className: Be, classNames: { icon: Le }, start: a })
              : e.jsxs(e.Fragment, {
                  children: [
                    e.jsx("div", {
                      className: s($e, Ge),
                      children: v.formatNumber("integral", t.computes.maxNumberOfCrystal()),
                    }),
                    e.jsx("div", {
                      className: s($e, !i && Ge),
                      children: n.readOrEmpty("common.common.slash"),
                    }),
                    e.jsx("div", {
                      className: s($e, !i && Ae),
                      children: v.formatNumber("integral", t.computes.currentNumberOfCrystal()),
                    }),
                  ],
                }),
          }),
        }),
        e.jsx("div", {
          className: ze,
          children: n.readOrEmpty(
            "tooltips.vehicle.bonds." + ("" + (r ? "limitReached" : "earningLimit")),
          ),
        }),
      ],
    });
  }),
  De = {
    row__multiplier: "Earnings_row__multiplier_16fcb8c8",
    leftColumn: "Earnings_leftColumn_940b9a0e",
    earnings: "Earnings_96294922",
    row: "Earnings_row_850c7c9b",
    icon: "Earnings_icon_c10adc2c",
    currency: "Earnings_currency_61ac411b",
    text: "Earnings_text_a6c4a45b",
  },
  Fe = t(function () {
    const { model: s } = Z(),
      { xp: t } = s.earnings.get(),
      a = p.resolve("strings");
    return e.jsxs(xe, {
      className: De.row,
      children: [
        e.jsx("div", {
          className: De.leftColumn,
          children: e.jsx(x, {
            reverse: !0,
            classNames: { base: De.currency, icon: De.icon },
            size: g.small,
            type: s.computes.elite() ? b.eliteXp : b.tankXP,
            children: e.jsx("div", { children: v.formatNumber("integral", t) }),
          }),
        }),
        e.jsx("div", { className: De.text, children: a.readOrEmpty("tooltips.vehicle.xp") }),
      ],
    });
  }),
  He = t(function () {
    const { model: t } = Z(),
      { bonusMultiplier: a } = t.earnings.get(),
      r = p.resolve("strings"),
      i = h("hangar.carousel.cards.bonus", "hangar.carousel.cards.bonus_upscale");
    return e.jsxs(xe, {
      className: s(De.row, H(a) && De.row__multiplier),
      children: [
        e.jsx("div", {
          className: De.leftColumn,
          children: e.jsxs(x, {
            type: "bonus",
            size: g.small,
            classNames: { base: De.currency },
            children: [
              e.jsx("div", { children: r.readOrEmpty("common.multiplierSmall") }),
              e.jsx("div", { children: v.formatNumber("integral", a) }),
              e.jsx(j, { path: i, className: De.icon, width: 24, height: 24 }),
            ],
          }),
        }),
        e.jsx("div", {
          className: De.text,
          children: r.readOrEmpty("tooltips.vehicle.dailyXPFactor"),
        }),
      ],
    });
  }),
  Xe = u("Earnings", De.base),
  We = t(function ({ className: s }) {
    const t = X()?.model,
      a = !t || t.isCrystalEarnEnabled.get(),
      r = !t || t.isDailyMultipliedXpEnabled.get(),
      { model: i } = Z(),
      { crystalEarning: l } = i.earnings.get(),
      n = p.resolve("strings");
    return e.jsxs(Xe, {
      className: s,
      children: [
        e.jsx("div", {
          className: De.earnings,
          children: n.readOrEmpty("tooltips.tankCaruselTooltip.earnings.header"),
        }),
        r && i.computes.hasBonusMultiplier() && e.jsx(He, {}),
        e.jsx(Fe, {}),
        a && l && e.jsx(Ve, {}),
        i.bpEntityValid.get() && i.computes.battlePoints() && e.jsx(Ce, {}),
      ],
    });
  }),
  Je = "Crew_2339425e",
  Ke = "Crew_79af07ed",
  Ue = "Crew_icon_26258836",
  Ze = "Crew_sign_a456f030",
  qe = t(function ({ className: t }) {
    const { model: a } = Z(),
      r = a.slots.get(),
      i = p.resolve("strings");
    return e.jsx(xe, {
      title: ce,
      params: { count: r.length },
      className: s(Je, t),
      children: N(r, (s) =>
        e.jsxs(
          "div",
          {
            className: Ke,
            children: [
              e.jsx(K, { role: y(s.roles, 0), className: Ue }),
              s.roles.length > 1 &&
                e.jsx("div", { className: Ze, children: i.readOrEmpty("crew_perks.sign.plus") }),
            ],
          },
          s.id,
        ),
      ),
    });
  }),
  Qe = "Rent_leftColumn_a909b981",
  Ye = "Rent_rentValue_f91a4efd",
  es = "Rent_text_94f0c0d7";
function ss({ rentPeriodLeft: s, rentType: t }) {
  const a = p.resolve("strings"),
    r = h("ui_kit.rental_counter.rent_x24x24", "ui_kit.rental_counter.rent_x48x48");
  return e.jsxs(xe, {
    children: [
      e.jsxs("div", {
        className: Qe,
        children: [
          e.jsx("div", { className: Ye, children: v.formatNumber("integral", Math.ceil(s)) }),
          e.jsx(j, { path: r, width: 24, height: 24 }),
        ],
      }),
      e.jsx("div", { className: es, children: a.readOrEmpty(`tooltips.vehicle.rentLeft.${t}`) }),
    ],
  });
}
const ts = t(function () {
    const { model: s } = Z(),
      { rentLeftTime: t, rentLeftBattles: a, rentLeftWins: r } = s.statistics.get(),
      i = (function (e) {
        const s = d(e);
        return c(s, o(1)) ? m(s, de) : m(s, ue);
      })(t);
    return t > 0
      ? e.jsx(ss, { rentPeriodLeft: i.value, rentType: i.unit })
      : a > 0
        ? e.jsx(ss, { rentPeriodLeft: a, rentType: oe })
        : r > 0
          ? e.jsx(ss, { rentPeriodLeft: r, rentType: me })
          : null;
  }),
  as = "Role_c276c189",
  rs = "Role_vehicleRoleIcon_a0c92760",
  is = "Role_property_8f6d69d9",
  ls = t(function ({ className: t }) {
    const { model: a } = Z(),
      { type: r, role: i } = a.statistics.get(),
      l = p.resolve("strings");
    return e.jsxs(xe, {
      className: s(as, t),
      title: ne,
      children: [
        e.jsx(E, { classNames: { icon: rs }, roleKey: w(i), size: P.x16x16 }),
        re(r) &&
          e.jsx("div", {
            className: is,
            children: l.readOrEmpty(`menu.roleExp.roleGroupName.role_${ie[r]}_${w(i)}`),
          }),
      ],
    });
  }),
  ns = p.resolve("strings"),
  cs = t(function ({ className: s }) {
    return e.jsx(xe, {
      className: s,
      children: ns.readOrEmpty("tooltips.vehicle.telecomRentalsRenting"),
    });
  }),
  os = {
    leftColumn: "TradeIn_leftColumn_e8d75ad6",
    tradeInIcon: "TradeIn_tradeInIcon_2cde5b72",
    text: "TradeIn_text_1e5d2ead",
  },
  ms = p.resolve("strings"),
  ds = t(function ({ className: t }) {
    return e.jsxs(xe, {
      className: s(os.base, t),
      children: [
        e.jsx("div", {
          className: os.leftColumn,
          children: e.jsx("div", { className: os.tradeInIcon }),
        }),
        e.jsx("div", { className: os.text, children: ms.readOrEmpty("tooltips.vehicle.trade") }),
      ],
    });
  }),
  us = "WotPlus_wotPlus_c07472c2",
  ps = "WotPlus_wotPlus__timer_fb00f649",
  _s = t(function ({ className: t }) {
    const { model: a } = Z(),
      { wotPlusExpiryTime: r, wotPlusState: i } = a.earnings.get(),
      l = p.resolve("strings");
    return e.jsxs(e.Fragment, {
      children: [
        e.jsx(xe, {
          className: t,
          children: e.jsx("div", {
            className: us,
            children: l.readOrEmpty("tooltips.vehicle.wotPlusRenting.title"),
          }),
        }),
        i !== Q &&
          e.jsx(xe, {
            className: t,
            children: (() => {
              switch (i) {
                case Y:
                  return e.jsx(_, {
                    upgradeLegacy: !0,
                    className: s(us, ps),
                    path: "tooltips.vehicle.wotPlusRenting.remainingTime",
                    params: { time: e.jsx(C, { datetime: r, format: "ShortDateTime" }) },
                  });
                case q:
                  return e.jsx("div", {
                    className: s(us, ps),
                    children: l.readOrEmpty("tooltips.vehicle.wotPlusRenting.inactive"),
                  });
                default:
                  return (console.error(`Unknown wotPlus state: ${i}`), null);
              }
            })(),
          }),
      ],
    });
  }),
  hs = "Header_name_154815cc",
  xs = "Header_tier_e0bb96ee",
  gs = "Header_level_d1428bec",
  vs = "Header_tierText_ab47090b",
  js = "Header_row_d4a891e5",
  bs = u("Header"),
  fs = t(function ({ className: s }) {
    const { model: t } = Z(),
      { wotPlus: a, telecomRent: r, tradeIn: i } = t.earnings.get(),
      { name: l, role: n, type: c, elite: o, level: m } = t.statistics.get(),
      d = w(n);
    return e.jsxs(bs, {
      className: s,
      children: [
        e.jsx("div", { className: hs, children: l }),
        e.jsx(xe, {
          className: xs,
          title: le,
          children: e.jsx(_, {
            className: vs,
            path: `tooltips.tankCaruselTooltip.vehicleType.tier.${o ? "elite" : "normal"}.${T(c)}`,
            params: { tier: e.jsx(R, { value: m, className: gs }) },
          }),
        }),
        d !== O && d !== S.spg && e.jsx(ls, { className: js }),
        e.jsx(qe, { className: js }),
        a && e.jsx(_s, { className: js }),
        r && e.jsx(cs, { className: js }),
        i && e.jsx(ds, {}),
        e.jsx(ts, {}),
      ],
    });
  }),
  Ns = "EliteSystem_leftColumn_6aa7810f",
  ys = "EliteSystem_c476a5a0",
  Es = "EliteSystem_eliteSystem_5a135969",
  Ps = "EliteSystem_eliteSystem__prestige_2b06b89c",
  ws = "EliteSystem_values_c91f1a15",
  Cs = "EliteSystem_currency_4591b107",
  Rs = "EliteSystem_icon_505ae9fd",
  Ts = "EliteSystem_slash_f65daa35",
  Os = "EliteSystem_xp_4e0b1db9",
  Ss = "EliteSystem_progressBarBorder_45636892",
  ks = t(function ({ className: t }) {
    const a = p.resolve("strings"),
      { model: r } = Z(),
      {
        prestigeLevel: i,
        prestigeGrade: l,
        prestigeType: n,
        prestigeXp: c,
        prestigeXpNextLevel: o,
      } = r.serviceRecords.get(),
      m = n === I.prestige;
    return e.jsxs(xe, {
      className: s(ys, t),
      children: [
        e.jsx("div", {
          className: Ns,
          children: e.jsx(k, { level: i, grade: l, type: n, size: B.xs }),
        }),
        e.jsxs("div", {
          className: s(Es, m && Ps),
          children: [
            e.jsxs("div", {
              className: ws,
              children: [
                e.jsx("div", {
                  children: a.readOrEmpty(
                    "tooltips.tankCaruselTooltip.serviceRecords." +
                      (m ? "prestigeEliteSystem" : "eliteSystem"),
                  ),
                }),
                !m &&
                  e.jsxs(x, {
                    reverse: !0,
                    size: g.small,
                    type: b.tankXP,
                    classNames: { base: Cs, icon: Rs },
                    children: [
                      e.jsx("div", { children: v.formatNumber("integral", o) }),
                      e.jsx("div", {
                        className: Ts,
                        children: a.readOrEmpty("common.common.slash"),
                      }),
                      e.jsx("div", { className: Os, children: v.formatNumber("integral", c) }),
                    ],
                  }),
              ],
            }),
            !m &&
              e.jsx(L, { value: c, size: "small", maxValue: o, classNames: { background: Ss } }),
          ],
        }),
      ],
    });
  }),
  Bs = {
    leftColumn: "ServiceRecords_leftColumn_c596dc1b",
    title: "ServiceRecords_title_40d609e8",
    eliteSystem: "ServiceRecords_eliteSystem_aeef0cfd",
    text: "ServiceRecords_text_e426fb24",
  },
  Ls = t(function () {
    const { model: s } = Z(),
      { marksOnGunPercentage: t, marksOnGun: a } = s.serviceRecords.get(),
      r = p.resolve("strings");
    return e.jsxs(xe, {
      children: [
        e.jsxs("div", {
          className: Bs.leftColumn,
          children: [
            e.jsx(_, {
              upgradeLegacy: !0,
              path: "common.percentValue",
              params: { value: v.formatReal("woZeroDigits", Number(t)) },
            }),
            e.jsx(j, { path: `library.marksOnGun.mark_${a}`, width: 24, height: 24 }),
          ],
        }),
        e.jsx("div", {
          className: Bs.text,
          children: r.pluralOrEmpty("achievements.marksOnGun.count", a),
        }),
      ],
    });
  }),
  Is = t(function () {
    const { model: s } = Z(),
      { marksOfMastery: t } = s.serviceRecords.get(),
      a = h(
        `tooltip.proficiency.class_icons_${te[t]}`,
        `tooltip.proficiency.class_icons_${te[t]}_upscale`,
      );
    return e.jsxs(xe, {
      children: [
        e.jsx("div", {
          className: Bs.leftColumn,
          children: e.jsx(j, { path: a, width: 24, height: 24 }),
        }),
        e.jsx(_, { className: Bs.text, path: `achievements.markOfMastery${te[t]}` }),
      ],
    });
  });
function Ms({ rate: s }) {
  const t = p.resolve("strings");
  return e.jsxs(xe, {
    children: [
      e.jsx(_, {
        upgradeLegacy: !0,
        className: Bs.leftColumn,
        path: "common.percentValue",
        params: { value: v.formatNumber("integral", Math.round(s)) },
      }),
      e.jsx("div", { className: Bs.text, children: t.readOrEmpty("achievements.winRate") }),
    ],
  });
}
const $s = u("ServiceRecords", Bs.base),
  Gs = t(function ({ className: s }) {
    const { model: t } = Z(),
      {
        prestigeType: a,
        marksOfMastery: r,
        winsCount: i,
        battlesCount: l,
        marksOnGun: n,
      } = t.serviceRecords.get(),
      c = p.resolve("strings"),
      o = l > 0 ? (i / l) * 100 : 0;
    return e.jsxs($s, {
      className: s,
      children: [
        e.jsx("div", {
          className: Bs.title,
          children: c.readOrEmpty("tooltips.tankCaruselTooltip.serviceRecords.header"),
        }),
        t.computes.elite() && "undefined" !== a && e.jsx(ks, { className: Bs.eliteSystem }),
        r > 0 && e.jsx(Is, {}),
        n > 0 && e.jsx(Ls, {}),
        l > 0 && e.jsx(Ms, { rate: o }),
      ],
    });
  }),
  As = {
    gradient: "SpecialAbility_gradient_73f7ba6b",
    leftColumn: "SpecialAbility_leftColumn_7e97137f",
    rightColumn: "SpecialAbility_rightColumn_4229b20e",
    title: "SpecialAbility_title_10243315",
    icon: "SpecialAbility_icon_eed3b29c",
    text: "SpecialAbility_text_f255c0f5",
  },
  zs = u("SpecialAbility", As.base),
  Vs = t(function ({ className: s }) {
    const { model: t } = Z(),
      a = t.mechanics.get(),
      r = p.resolve("strings");
    return e.jsxs(zs, {
      className: s,
      children: [
        e.jsx("div", { className: As.gradient }),
        N(a, (s, t) => {
          if (!(s.priority < F))
            return e.jsxs(
              xe,
              {
                children: [
                  e.jsx("div", {
                    className: As.leftColumn,
                    children: e.jsx(j, {
                      path:
                        s.rank === W.GOLD
                          ? `vehicle_hub.mechanics.special.x48x48.${s.name}`
                          : `vehicle_hub.mechanics.x48x48.${s.name}`,
                      width: 48,
                      height: 48,
                      className: As.icon,
                    }),
                  }),
                  e.jsxs("div", {
                    className: As.rightColumn,
                    children: [
                      e.jsx("div", {
                        className: As.title,
                        children: r.readOrEmpty(`vehicle_hub.abilities.special.name.${s.name}`),
                      }),
                      e.jsx("div", {
                        className: As.text,
                        children: e.jsx(_, {
                          split: !0,
                          path: `vehicle_hub.abilities.special.shortDescription.${s.name}`,
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
  Ds = "Tooltip_decorator_9aef02ef",
  Fs = "Tooltip_fdfde46e",
  Hs = "Tooltip_base__elite_ae2bf179",
  Xs = "Tooltip_vehicleType_b877a704",
  Ws = "Tooltip_vehicleType__elite_bb248964",
  Js = "Tooltip_section_b726d2f2",
  Ks = "Tooltip_section__header_c649b074",
  Us = "Tooltip_section__earnings_e52798af",
  Zs = "Tooltip_status_29b423b3",
  qs = t(function ({ className: t }) {
    const { model: a } = Z(),
      { type: r } = a.statistics.get();
    return e.jsx(M, {
      className: t,
      children: e.jsxs(M.Decorator, {
        className: Ds,
        children: [
          re(r) &&
            e.jsx($, {
              type: r,
              premium: a.computes.elite(),
              size: G.x64x64,
              className: s(Xs, a.computes.elite() && Ws),
            }),
          e.jsxs("div", {
            className: s(Fs, a.computes.elite() && Hs),
            children: [
              e.jsx(fs, { className: s(Js, Ks) }),
              a.computes.hasSpecialMechanics() && e.jsx(Vs, { className: Js }),
              e.jsx(We, { className: s(Js, Us) }),
              a.computes.serviceRecords() && e.jsx(Gs, { className: Js }),
              e.jsx(_, {
                upgradeLegacy: !0,
                style: { color: ae(a.stateLevel.get()) },
                className: Zs,
                path: `tooltips.vehicleStatus.${a.status.get()}.header`,
                params: {
                  icon: e.jsx(j, { path: "library.premium_igr_small", width: 26, height: 16 }),
                },
              }),
            ],
          }),
        ],
      }),
    });
  }),
  Qs = p.resolve("aliases");
var Ys;
V(
  new A()
    .add(U)
    .add(z)
    .addWithProps(
      J,
      ((Ys = (e) => e.common.shared.DynamicEconomics("resId")),
      { options: { rootId: Qs.read(Ys) } }),
    )
    .render(e.jsx(qs, {})),
);
