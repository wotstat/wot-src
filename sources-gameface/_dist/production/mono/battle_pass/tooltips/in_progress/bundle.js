import { r as e } from "../../chunks/rolldown-runtime.js";
import {
  I as s,
  It as a,
  Ur as t,
  Xn as o,
  _n as l,
  ai as r,
  an as n,
  bt as i,
  ci as d,
  cn as c,
  f as _,
  fn as m,
  ii as b,
  l as h,
  ln as u,
  n as p,
  pn as x,
  rn as f,
  sn as w,
  tn as g,
  ui as P,
  un as j,
  xt as N,
} from "../../chunks/lib.js";
import "../../chunks/global.js";
import { h as v } from "../../chunks/vendor.js";
import { u as k } from "../../chunks/utils.js";
import { t as I } from "../../chunks/types.js";
import { a as T, i as y, n as B, r as C, t as E } from "../../chunks/per_battle_points_table.js";
import { t as S } from "../../chunks/separator.js";
import { t as O } from "../../chunks/icon_text_block.js";
var W = e(P(), 1),
  L = (function (e) {
    return (
      (e.COMMON = "common"),
      (e.EXTRA = "extra"),
      (e.HOLIDAY = "holiday"),
      (e.POST_PROGRESSION = "postProgression"),
      e
    );
  })({}),
  [M, H] = l()(
    ({ observableModel: e }) => ({
      root: e.object(),
      rewardPoints: e.array("rewardPoints"),
      battleRoyaleRewardPoints: e.array("battleRoyaleRewardPoints"),
      rewardsCommon: e.array("rewardsCommon"),
      rewardsElite: e.array("rewardsElite"),
    }),
    t,
  ),
  U = "Rewards_3f324c43",
  A = o(),
  D = ({ className: e = "", children: s = null }) =>
    (0, A.jsx)("div", { className: d(U, e), children: s }),
  G = "ClaimInfo_63bb6cbd",
  $ = "ClaimInfo_unlock_c22806f7",
  F = R.strings.battle_pass.tooltips.claimRewards,
  Y = v(({ className: e = "" }) => {
    const { model: s } = H(),
      { notChosenRewardCount: a } = s.root.get();
    return (0, A.jsx)("div", {
      className: d(G, e),
      children: (0, A.jsx)(O, {
        icon: R.images.gui.maps.icons.battlePass.tooltips.bow_small(),
        text: F[a > 1 ? "multiple" : "c_1"](),
        className: $,
      }),
    });
  }),
  q = (0, W.memo)(({ header: e, points: s, columnClassMix: a, hasAdditionalPoints: t }) =>
    (0, A.jsxs)("div", {
      className: d(T.pointsColumn, a),
      children: [
        (0, A.jsx)("div", { className: T.tableHeader, children: e }),
        s.map((e, s) =>
          (0, A.jsx)(
            "div",
            {
              className: T.label,
              children: (0, A.jsx)(C, {
                value: e.points,
                hasAdditionalPoints: t,
                externalValue: e.externalPoints,
                showIcon: !1,
              }),
            },
            s,
          ),
        ),
      ],
    }),
  ),
  V = {
    pointsIcon: "BattleRoyaleTable_pointsIcon_fa2c60ed",
    pointsColumn1: "BattleRoyaleTable_pointsColumn1_85de316a",
    header: "BattleRoyaleTable_header_8385939f",
    label: "BattleRoyaleTable_label_e7fdd3ac",
    fadeInWithScale: "BattleRoyaleTable_fadeInWithScale_13433de7",
    slideUp: "BattleRoyaleTable_slideUp_13433de7",
    blink: "BattleRoyaleTable_blink_13433de7",
    scale: "BattleRoyaleTable_scale_13433de7",
    rotate: "BattleRoyaleTable_rotate_13433de7",
    windowIn: "BattleRoyaleTable_windowIn_13433de7",
    fadeOut: "BattleRoyaleTable_fadeOut_13433de7",
    fadeIn: "BattleRoyaleTable_fadeIn_13433de7",
  },
  X = R.strings.battle_pass.tooltips.pointsTable,
  z = ({ rewardPoints: e, hasAdditionalPoints: s }) => {
    const a = (0, W.useMemo)(
        () =>
          e.soloMode.map(({ value: e }) =>
            (0, A.jsx)(i, { text: X.places(), binding: { place: e.place } }),
          ),
        [e],
      ),
      t = (0, W.useMemo)(() => e.soloMode.map(({ value: e }) => e), [e]),
      o = (0, W.useMemo)(
        () =>
          e.squadMode.map(({ value: e }, s) =>
            (0, A.jsx)(i, { text: s > 0 ? X.places() : X.place(), binding: { place: e.place } }),
          ),
        [e],
      ),
      l = (0, W.useMemo)(() => e.squadMode.map(({ value: e }) => e), [e]);
    return (0, A.jsxs)(A.Fragment, {
      children: [
        (0, A.jsx)(y, {
          columnWidth: 140,
          header: X.solo(),
          headerClassMix: V.header,
          labels: a,
          labelClassMix: V.label,
        }),
        (0, A.jsx)(q, {
          points: t,
          columnClassMix: V.pointsColumn1,
          hasAdditionalPoints: s,
          header: (0, A.jsx)("div", { className: V.pointsIcon }),
        }),
        (0, A.jsx)(y, {
          columnWidth: 140,
          header: X.squad(),
          headerClassMix: V.header,
          labels: o,
          labelClassMix: V.label,
        }),
        (0, A.jsx)(q, {
          columnClassMix: V.pointsColumn2,
          points: l,
          hasAdditionalPoints: s,
          header: (0, A.jsx)("div", { className: V.pointsIcon }),
        }),
      ],
    });
  },
  J = {
    base: "HeaderWithPoints_3979d534",
    modeIcon: "HeaderWithPoints_modeIcon_fefd91cd",
    modeIcon__battleRoyale: "HeaderWithPoints_modeIcon__battleRoyale_98f862f2",
    modeIcon__epic: "HeaderWithPoints_modeIcon__epic_14f8b63",
    highlight: "HeaderWithPoints_highlight_8e3610ae",
    fadeInWithScale: "HeaderWithPoints_fadeInWithScale_46eb29ed",
    slideUp: "HeaderWithPoints_slideUp_46eb29ed",
    blink: "HeaderWithPoints_blink_46eb29ed",
    scale: "HeaderWithPoints_scale_46eb29ed",
    rotate: "HeaderWithPoints_rotate_46eb29ed",
    windowIn: "HeaderWithPoints_windowIn_46eb29ed",
    fadeOut: "HeaderWithPoints_fadeOut_46eb29ed",
    fadeIn: "HeaderWithPoints_fadeIn_46eb29ed",
  },
  K = v(() => {
    const { model: e } = H(),
      { battleType: s, customBattleTypeIcon: a } = e.root.get(),
      t = k(s),
      o = a ? { backgroundImage: `url(${a})` } : {};
    return (0, A.jsxs)("div", {
      className: J.base,
      children: [
        (0, A.jsx)("div", { className: d(J.modeIcon, J[`modeIcon__${t}`]), style: o }),
        (0, A.jsx)(i, {
          text: R.strings.battle_pass.tooltips.inProgress.getPointsFrom(),
          binding: {
            battleType: (0, A.jsx)("div", {
              className: J.highlight,
              children: `${R.strings.battle_pass.tooltips.inProgress.$dyn(t)}`,
            }),
          },
        }),
      ],
    });
  }),
  Q = {
    header: "RulesTable_header_3dadec54",
    playGame: "RulesTable_playGame_8b1d2ff9",
    perBattlePointsTable: "RulesTable_perBattlePointsTable_9ccd09af",
    footer: "RulesTable_footer_3838100b",
    footer_text: "RulesTable_footer_text_5b78b966",
    extraPointsDivider: "RulesTable_extraPointsDivider_ec32c66c",
    extraPointsGlow: "RulesTable_extraPointsGlow_c65c2dc",
    fadeInWithScale: "RulesTable_fadeInWithScale_1d6097e4",
    slideUp: "RulesTable_slideUp_1d6097e4",
    blink: "RulesTable_blink_1d6097e4",
    scale: "RulesTable_scale_1d6097e4",
    rotate: "RulesTable_rotate_1d6097e4",
    windowIn: "RulesTable_windowIn_1d6097e4",
    fadeOut: "RulesTable_fadeOut_1d6097e4",
    fadeIn: "RulesTable_fadeIn_1d6097e4",
  },
  Z = R.strings.battle_pass.tooltips,
  ee = {
    randoms: "c_1",
    ranked: "ranked",
    mapbox: "c_22",
    comp7: "c_24",
    comp7_light: "comp7_light",
    winback: "winback",
  },
  se = R.strings.battle_pass.tooltips.pointsTable,
  ae = R.strings.battle_pass.tooltips.prestigePoints,
  te = [I.BATTLE_ROYALE, I.FRONTLINE],
  oe = [I.COMP7, I.COMP7_LIGHT],
  le = v(() => {
    const { model: e } = H(),
      { battleType: s, isWotPlusShown: t } = e.root.get(),
      o = e.rewardPoints.get(),
      l = e.battleRoyaleRewardPoints.get(),
      r = s === I.BATTLE_ROYALE,
      n =
        null !== Z.inProgress.playGame.$dyn(s)
          ? (0, A.jsx)(O, {
              icon: R.images.gui.maps.icons.battleTypes.$dyn(ee[s]),
              text: Z.inProgress.playGame.$dyn(s),
              className: Q.playGame,
            })
          : null;
    return (0, A.jsxs)(A.Fragment, {
      children: [
        (0, A.jsx)("div", {
          className: Q.header,
          children: te.includes(s) ? (0, A.jsx)(K, {}) : n,
        }),
        (0, A.jsx)(E, {
          mixClass: Q.perBattlePointsTable,
          separatorRows: r ? l.soloMode : o.items,
          children: r
            ? (0, A.jsx)(z, { rewardPoints: l, hasAdditionalPoints: t })
            : (0, A.jsx)(B, {
                rewardPoints: o,
                hasAdditionalPoints: t,
                hasDraw: s !== I.FRONTLINE,
                topPlace: (oe.includes(s) ? ae : se).topPlace(),
                battleType: s,
              }),
        }),
        t &&
          (0, A.jsxs)("div", {
            className: Q.footer,
            children: [
              (0, A.jsx)(a, {
                width: 32,
                height: 32,
                src: R.images.gui.maps.icons.battlePass.tooltips.plus_logo(),
                className: Q.footerIcon,
              }),
              (0, A.jsx)("div", { className: Q.extraPointsDivider }),
              (0, A.jsx)("div", { className: Q.extraPointsGlow }),
              (0, A.jsx)("div", {
                className: Q.footer_text,
                children: Z.inProgress.wotPlusProFooter(),
              }),
            ],
          }),
      ],
    });
  }),
  re = "EndSoon_c24403ee",
  ne = "EndSoon_content_9cbdeacc",
  ie = "EndSoon_timerLight_32dfe31",
  de = "EndSoon_timer_a08253f1",
  ce = "EndSoon_timerIcon_7fa43c71",
  _e = "EndSoon_timerLabel_a39df14c",
  me = "EndSoon_timerValue_3b8b21cd",
  be = R.strings.battle_pass.tooltips.inProgress,
  he = v(({ className: e }) => {
    const { model: s } = H(),
      { timeTillEnd: a } = s.root.get();
    return (0, A.jsx)("div", {
      className: re,
      children: (0, A.jsx)("div", {
        className: d(e, ne),
        children: (0, A.jsxs)("div", {
          className: de,
          children: [
            (0, A.jsx)("div", { className: ie }),
            (0, A.jsx)("div", { className: ce }),
            (0, A.jsx)("div", { className: me, children: a }),
            (0, A.jsx)("div", { className: _e, children: be.timeLeft() }),
          ],
        }),
      }),
    });
  }),
  ue = "Level_d583bdeb",
  pe = "Level_label_5ce8f3eb",
  xe = R.strings.battle_pass.tooltips.inProgress,
  fe = v(() => {
    const { model: e } = H(),
      { level: s } = e.root.get();
    return (0, A.jsxs)(A.Fragment, {
      children: [
        (0, A.jsx)("div", { className: ue, children: s + 1 }),
        (0, A.jsx)("div", { className: pe, children: xe.level() }),
      ],
    });
  }),
  we = "Points_967b0112",
  Re = "Points_pointsCurrent_b498b3a9",
  ge = "Points_pointsMax_2f7dc8fa",
  Pe = "Points_pointsIcon_615fd6e8",
  je = ({ currentPoints: e, maxPoints: s, className: a = "" }) =>
    (0, A.jsxs)("div", {
      className: d(we, a),
      children: [
        (0, A.jsx)("div", { className: Re, children: e }),
        "/",
        (0, A.jsx)("div", { className: ge, children: s }),
        (0, A.jsx)("div", { className: Pe }),
      ],
    }),
  Ne = "Progression_5cdbad76",
  ve = "Progression_progressionBar_6bb904d3",
  ke = "Progression_points_fa2aa3d9",
  Ie = v(({ isDisabled: e = !1, className: s = "" }) => {
    const { model: a } = H(),
      { currentPoints: t, maxPoints: o } = a.root.get();
    return (0, A.jsxs)("div", {
      className: d(Ne, s),
      children: [
        (0, A.jsx)("div", {
          className: ve,
          children: (0, A.jsx)(h, { value: t, maxValue: o, theme: _, disabled: e }),
        }),
        (0, A.jsx)(je, { maxPoints: o, currentPoints: t, className: ke }),
      ],
    });
  }),
  Te = (Date.now(), w.getRegionalDateTime, w.getFormattedDateTime, "ExpireTime_d2bc0e02"),
  ye = "ExpireTime_light_ff99b79d",
  Be = "ExpireTime_icon_8036e60f",
  Ce = "ExpireTime_value_6d799e0c",
  Ee = v(() => {
    const { model: e } = H(),
      { expireTime: s } = e.root.get(),
      a = ((e, s = !0) =>
        e.days > 7 && s
          ? N(R.strings.common.duration.days(), { days: e.days })
          : e.days >= 1
            ? 0 === e.hours
              ? N(R.strings.common.duration.days(), { days: e.days })
              : `${N(R.strings.common.duration.days(), { days: e.days })} ${N(R.strings.common.duration.hours(), { hours: e.hours })}`
            : e.hours >= 1
              ? 0 === e.minutes
                ? N(R.strings.common.duration.hours(), { hours: e.hours })
                : `${N(R.strings.common.duration.hours(), { hours: e.hours })} ${N(R.strings.common.duration.minutes(), { minutes: e.minutes })}`
              : N(R.strings.common.duration.minutes(), { minutes: e.minutes || 1 }))(r(s), !1);
    return (0, A.jsxs)("div", {
      className: Te,
      children: [
        (0, A.jsx)("div", { className: ye }),
        (0, A.jsx)("div", { className: Be }),
        (0, A.jsx)("div", { className: Ce, children: a }),
      ],
    });
  }),
  Se = "Header_71860ac",
  Oe = "Header_chapter_92802c23",
  We = "Header_name_d009752f",
  Le = v(() => {
    const { model: e } = H(),
      { chapter: s, expireTime: a } = e.root.get(),
      t = (() => {
        switch (e.root.get().chapterType) {
          case L.EXTRA:
          case L.HOLIDAY:
            return a > 0 && a < 172800;
          case L.COMMON:
            return !1;
        }
      })();
    return (0, A.jsxs)("div", {
      className: Se,
      children: [
        (0, A.jsxs)("div", {
          className: Oe,
          children: [
            (0, A.jsx)("div", {
              className: We,
              children:
                s &&
                (0, A.jsx)(i, {
                  text: R.strings.battle_pass.tooltips.inProgress.chapter(),
                  binding: { name: R.strings.battle_pass.chapter.fullName.$dyn(`c_${s}`) },
                }),
            }),
            t && (0, A.jsx)(Ee, {}),
          ],
        }),
        (0, A.jsx)(fe, {}),
        (0, A.jsx)(Ie, {}),
      ],
    });
  }),
  Me = {
    base: "RewardsBlock_a66e0ba7",
    nextRewards: "RewardsBlock_nextRewards_580b2817",
    rewardsList: "RewardsBlock_rewardsList_bd0e0d04",
    rewardsList__locked: "RewardsBlock_rewardsList__locked_d962e74b",
    reward: "RewardsBlock_reward_ba99e1fe",
    reward__shiftUp: "RewardsBlock_reward__shiftUp_c85a723b",
    reward__styleUpgrade: "RewardsBlock_reward__styleUpgrade_5feff608",
    reward__wide: "RewardsBlock_reward__wide_6b8de2f3",
    reward__next: "RewardsBlock_reward__next_37ab73ce",
    reward__single: "RewardsBlock_reward__single_56d6a3b7",
    lockIcon: "RewardsBlock_lockIcon_b3ad9975",
    overlay: "RewardsBlock_overlay_adaa44ea",
    fadeInWithScale: "RewardsBlock_fadeInWithScale_5feff608",
    slideUp: "RewardsBlock_slideUp_5feff608",
    blink: "RewardsBlock_blink_5feff608",
    scale: "RewardsBlock_scale_5feff608",
    rotate: "RewardsBlock_rotate_5feff608",
    windowIn: "RewardsBlock_windowIn_5feff608",
    fadeOut: "RewardsBlock_fadeOut_5feff608",
    fadeIn: "RewardsBlock_fadeIn_5feff608",
  },
  He = [
    j.PROGRESSION_STYLE_UPGRADED_1,
    j.PROGRESSION_STYLE_UPGRADED_2,
    j.PROGRESSION_STYLE_UPGRADED_3,
    j.PROGRESSION_STYLE_UPGRADED_4,
  ],
  Ue = ({ label: e, isLocked: a = !1, rewards: { items: t } }) => {
    const o = t.length > 1 && t.length % 2 == 1,
      l = 1 === t.length,
      r = 2 === t.length,
      i = l ? c.S180x135 : c.Small,
      _ = t.every(({ value: e }) => {
        const s = Number(e.value);
        return !isNaN(s) && s > 1;
      });
    return (0, A.jsxs)("div", {
      className: Me.base,
      children: [
        (0, A.jsxs)("div", {
          className: Me.nextRewards,
          children: [a && (0, A.jsx)("div", { className: Me.lockIcon }), e],
        }),
        (0, A.jsx)("div", {
          className: d(Me.rewardsList, a && Me.rewardsList__locked),
          children: t.map((e, a) => {
            const t = ((e, s) => ({
                name: e.item || e.name,
                image: f(e, s),
                special: e.overlayType,
                value: e.value,
                valueType: n(e.name),
              }))(e.value, i),
              c = t.name === u.Attachment,
              m = t.special && He.includes(t.special);
            return (0, W.createElement)(s, {
              ...t,
              size: i,
              key: `${t.name}_${a}`,
              className: d(
                !r && Me.reward,
                a > 0 && Me.reward__next,
                m && Me.reward__styleUpgrade,
                _ && !o && Me.reward__wide,
                o && a % 2 == 1 && Me.reward__shiftUp,
                l && Me.reward__single,
              ),
              classNames: { overlay: d(!c && l && Me.overlay) },
            });
          }),
        }),
      ],
    });
  },
  Ae = "InProgressContent_a8ca87b2",
  De = "InProgressContent_content_524dcedb",
  Ge = "InProgressContent_rewards_2fa1b734",
  $e = "InProgressContent_unlockBattlePass_c7983742",
  Fe = "InProgressContent_claim_4bd431ea",
  Ye = R.strings.battle_pass.tooltips,
  qe = v(() => {
    const { model: e } = H(),
      { timeTillEnd: s, isBattlePassPurchased: a, notChosenRewardCount: t } = e.root.get(),
      o = e.rewardsCommon.get(),
      l = e.rewardsElite.get(),
      r = 0 !== s.length,
      n = 0 !== t;
    return (0, A.jsxs)("div", {
      className: Ae,
      children: [
        (0, A.jsxs)("div", {
          className: De,
          children: [
            (0, A.jsx)(Le, {}),
            (0, A.jsxs)(D, {
              className: Ge,
              children: [
                (0, A.jsx)(Ue, { label: Ye.inProgress.baseReward(), rewards: o }),
                (0, A.jsx)(Ue, { label: Ye.inProgress.improvedReward(), rewards: l, isLocked: !a }),
              ],
            }),
            !r &&
              !a &&
              (0, A.jsx)(O, {
                icon: R.images.gui.maps.icons.battlePass.progression.icon_lock_current_small(),
                text: Ye.unlockBattlePass(),
                className: $e,
              }),
          ],
        }),
        (0, A.jsx)(le, {}),
        n &&
          (0, A.jsxs)(A.Fragment, {
            children: [(0, A.jsx)(S, {}), (0, A.jsx)(Y, { className: Fe })],
          }),
        r && (0, A.jsx)(he, {}),
      ],
    });
  }),
  Ve = "Header_71860ac",
  Xe = "Header_name_1aee0b18",
  ze = R.strings.battle_pass.tooltips.inProgress.postProgression,
  Je = ({ className: e = "" }) =>
    (0, A.jsxs)("div", {
      className: d(Ve, e),
      children: [
        (0, A.jsx)("div", { className: Xe, children: ze.header() }),
        (0, A.jsx)(fe, {}),
        (0, A.jsx)(Ie, {}),
      ],
    }),
  Ke = {
    base: "RewardsBlock_f8eba448",
    ribbon: "RewardsBlock_ribbon_63a6acee",
    rewards: "RewardsBlock_rewards_259e5467",
    reward__big: "RewardsBlock_reward__big_6e09459f",
    fadeInWithScale: "RewardsBlock_fadeInWithScale_5feff608",
    slideUp: "RewardsBlock_slideUp_5feff608",
    blink: "RewardsBlock_blink_5feff608",
    scale: "RewardsBlock_scale_5feff608",
    rotate: "RewardsBlock_rotate_5feff608",
    windowIn: "RewardsBlock_windowIn_5feff608",
    fadeOut: "RewardsBlock_fadeOut_5feff608",
    fadeIn: "RewardsBlock_fadeIn_5feff608",
  },
  Qe = (e, s) => ({
    name: e.item || e.name,
    image: f(e, s),
    special: e.overlayType,
    value: e.value,
    valueType: n(e.name),
  }),
  Ze = ({ rewards: { items: e }, className: a = "" }) => {
    const t = e.length < 3 ? c.S180x135 : c.Big;
    return (0, A.jsxs)("div", {
      className: d(Ke.base, a),
      children: [
        (0, A.jsx)("div", { className: Ke.ribbon }),
        (0, A.jsx)("div", {
          className: Ke.rewards,
          children: e.map((e, a) =>
            (0, A.jsx)(
              s,
              { ...Qe(e.value, t), className: Ke[`reward__${t}`], size: t },
              `${e.name}_${a}`,
            ),
          ),
        }),
      ],
    });
  },
  es = "PostProgressionContent_61673cb3",
  ss = "PostProgressionContent_header_d2b5683d",
  as = "PostProgressionContent_content_208e84c4",
  ts = "PostProgressionContent_rewardsBlock_dbb9691f",
  os = "PostProgressionContent_claim_1f3e4c4d",
  ls = "PostProgressionContent_separatorWrapper_6e8e0fa1",
  rs = "PostProgressionContent_unlockBattlePass_4ea37eb7",
  ns = R.strings.battle_pass.tooltips,
  is = v(() => {
    const { model: e } = H(),
      { isBattlePassPurchased: s, notChosenRewardCount: a } = e.root.get(),
      t = 0 !== a;
    return (0, A.jsxs)("div", {
      className: es,
      children: [
        (0, A.jsx)(Je, { className: ss }),
        (0, A.jsx)(Ze, { rewards: e.rewardsCommon.get(), className: ts }),
        (0, A.jsx)(le, {}),
        (t || !s) && (0, A.jsx)(S, {}),
        (0, A.jsxs)("div", {
          className: as,
          children: [
            t && (0, A.jsx)(Y, { className: d(s && os) }),
            t && !s && (0, A.jsx)(S, { className: ls }),
            !s &&
              (0, A.jsx)("div", {
                children: (0, A.jsx)(O, {
                  icon: R.images.gui.maps.icons.battlePass.progression.icon_lock_current_small(),
                  text: ns.unlockBattlePassForPostProgression(),
                  className: rs,
                }),
              }),
          ],
        }),
      ],
    });
  }),
  ds = v(() => {
    const { model: e } = H(),
      { chapterType: s } = e.root.get(),
      a = s === L.POST_PROGRESSION ? (0, A.jsx)(is, {}) : (0, A.jsx)(qe, {});
    return (0, A.jsx)(p, { children: (0, A.jsx)(p.Decorator, { children: a }) });
  });
m(
  new x()
    .add(g)
    .addWithProps(M, {})
    .render((0, A.jsx)(ds, {})),
);
