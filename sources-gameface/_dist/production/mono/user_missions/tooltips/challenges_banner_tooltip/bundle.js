import { r as e } from "../../chunks/rolldown-runtime.js";
import {
  Dn as s,
  E as a,
  I as r,
  Jt as i,
  O as t,
  Pn as n,
  St as l,
  T as c,
  Yt as d,
  _t as o,
  ct as m,
  k as _,
  ln as u,
  on as g,
  qt as x,
  un as j,
  vt as h,
  x as v,
  yt as p,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ import { t as b } from "../../chunks/utils.js";
import { i as f, t as N } from "../../chunks/get_reward_image.js";
var w = ["gold", "credits", "freeXP", "crystal", "equipCoin", "bptaler"],
  [y, I] = l()(
    ({ observableModel: e }) => ({
      root: e.object(),
      ...e.primitives([
        "time",
        "challengeName",
        "completedMissions",
        "totalMissions",
        "remainingAttempts",
      ]),
      bonuses: e.array("mission.bonuses"),
      conditions: e.object("mission.postBattleCondition"),
    }),
    j,
  ),
  L = "Default_img_81672d94",
  k = "Default_header_314adb08",
  C = "Default_description_e8e99be8",
  O = "Default_separator_4490ce49",
  $ = "Default_timerStatus_b2f607e",
  E = e(i(), 1),
  M = n.resolve("strings"),
  B = "hangar_event_banners.event.ChallengeEventBanner.tooltip",
  H = o(function () {
    const { model: e } = I(),
      s = e.time.get();
    return (0, E.jsxs)(E.Fragment, {
      children: [
        (0, E.jsx)("div", {
          className: L,
          style: {
            backgroundImage: `url(${R.images.gui.maps.icons.tooltip.challengesBannerBg()})`,
          },
        }),
        (0, E.jsx)("div", {
          className: k,
          children: (0, E.jsx)(m, { text: M.readOrEmpty(`${B}.title`) }),
        }),
        (0, E.jsx)("div", {
          className: C,
          children: (0, E.jsx)(m, { text: M.readOrEmpty(`${B}.description`) }),
        }),
        s > 0 &&
          (0, E.jsxs)(E.Fragment, {
            children: [
              (0, E.jsx)("div", { className: O }),
              (0, E.jsx)(m, {
                text: M.readOrEmpty(`${B}.timer.text`),
                params: { timer: (0, E.jsx)(a, { size: t.x24x24, type: _.accent, start: s }, s) },
                className: $,
                upgradeLegacy: !0,
              }),
            ],
          }),
      ],
    });
  }),
  D = "Header_3d842ff",
  T = "Header_title_a2935114",
  z = "Header_info_e7e5cf7c",
  P = "Header_progress_2c5b28cb",
  S = "Header_accent_78fe2ee9",
  X = "Header_divider_e9b65048",
  F = "Header_shields_ae11a84e",
  q = "Header_shieldsCount_eb5f7f96",
  A = "Header_shieldIcon_155019e1",
  K = n.resolve("strings"),
  J = o(function () {
    const { model: e } = I(),
      s = e.challengeName.get(),
      a = e.completedMissions.get(),
      r = e.totalMissions.get(),
      i = e.remainingAttempts.get();
    return (0, E.jsxs)("div", {
      className: D,
      children: [
        (0, E.jsx)("div", {
          className: T,
          children: (0, E.jsx)(m, {
            text: K.readOrEmpty(
              "user_missions.challenge_missions.entrypoint.tooltip.challengeTitle",
            ),
            params: { challengeName: s },
          }),
        }),
        (0, E.jsxs)("div", {
          className: z,
          children: [
            (0, E.jsx)("div", {
              className: P,
              children: (0, E.jsx)(m, {
                text: K.readOrEmpty("user_missions.hub.challenge_missions.missionsCount"),
                params: {
                  currentMissions: (0, E.jsx)("span", { className: S, children: a }),
                  totalMissions: r,
                },
              }),
            }),
            (0, E.jsx)("div", { className: X }),
            (0, E.jsxs)("div", {
              className: F,
              children: [
                (0, E.jsx)("span", { className: q, children: i }),
                (0, E.jsx)("div", { className: A }),
              ],
            }),
          ],
        }),
      ],
    });
  }),
  Y = "ConditionItem_a08966eb",
  G = "ConditionItem_icon_3b7a4890",
  Q = "ConditionItem_conditionBg_e5e2cf8e",
  U = "ConditionItem_text_5a72400a",
  V = "ConditionItem_description_a047788c",
  W = n.resolve("images"),
  Z = ({ condition: e }) => {
    const { iconKey: s, descrData: a } = e,
      { breakpoint: r } = x(),
      i = r.weight >= d.large.weight ? 4 : 3,
      t = `userMissions.challenges.missionIcons.c_80.${s}`,
      n =
        W.readOrEmpty(t, "silent") ||
        W.readOrEmpty("userMissions.challenges.missionIcons.c_80.folder");
    return (0, E.jsxs)("div", {
      className: Y,
      children: [
        (0, E.jsx)("div", {
          className: G,
          children: (0, E.jsx)("div", { className: Q, style: { backgroundImage: `url(${n})` } }),
        }),
        (0, E.jsx)("div", {
          className: U,
          children: (0, E.jsx)(c, { text: `${a}`, lines: i, className: V }),
        }),
      ],
    });
  },
  ee = "OrSeparator_b6b48c7a",
  se = "OrSeparator_arrow_4d71dcce",
  ae = "OrSeparator_arrow__rotate_1d0c168d",
  re = n.resolve("strings"),
  ie = () =>
    (0, E.jsxs)("div", {
      className: ee,
      children: [
        (0, E.jsx)("div", { className: s(se, ae) }),
        (0, E.jsx)("span", {
          children: re.readOrEmpty("user_missions.hub.challenge_missions.card.or"),
        }),
        (0, E.jsx)("div", { className: se }),
      ],
    }),
  te = "ConditionsList_ee6c89f3",
  ne = "ConditionsList_condition_726a545",
  le = o(function () {
    const { model: e } = I(),
      s = e.conditions.get();
    return (0, E.jsx)("div", {
      className: te,
      children: g(s.items, (e, s, a) =>
        (0, E.jsxs)(
          "div",
          {
            className: ne,
            children: [(0, E.jsx)(Z, { condition: e }), s < a.length - 1 && (0, E.jsx)(ie, {})],
          },
          e.iconKey || s,
        ),
      ),
    });
  }),
  ce = "customization";
var de = "Overlay_7ff640ef",
  oe = n.resolve("images");
function me({ size: e, special: a, className: r }) {
  return (0, E.jsx)("div", {
    className: s(de, r),
    style: { backgroundImage: `url(${oe.readOrEmpty(`quests.bonuses.${e}.${v(a)}_overlay`)})` },
  });
}
var _e = "RewardImage_98da984",
  ue = "RewardImage_count_971e488d";
function ge({ showCounter: e, count: a, image: r, className: i = "" }) {
  return (0, E.jsx)("div", {
    className: s(_e, i),
    style: { backgroundImage: `url(${r})` },
    children:
      e &&
      (0, E.jsx)(m, {
        text: R.strings.user_missions.hub.challenge_missions.reward.multi(),
        className: ue,
        params: { count: a },
      }),
  });
}
var xe = "RewardName_text_79eb0561";
function je({ reward: e, className: a = "" }) {
  const { label: r } = e;
  return (0, E.jsx)(m, { className: s(xe, a), text: b(r), upgradeLegacy: !0 });
}
var he = {
    base: "RewardsList_397c9761",
    divider: "RewardsList_divider_78e650ae",
    rewardsContainer: "RewardsList_rewardsContainer_aebf6314",
    reward: "RewardsList_reward_ac2ccaa7",
    rewardImage__counter: "RewardsList_rewardImage__counter_be4a503f",
    rewardImage: "RewardsList_rewardImage_353bd5f0",
    overlay: "RewardsList_overlay_3f25e670",
    label: "RewardsList_label_b98ce7b5",
    label__credits: "RewardsList_label__credits_fc72d779",
    label__gold: "RewardsList_label__gold_6d38ffaa",
    label__freeXP: "RewardsList_label__freeXP_175e2503",
    label__crystal: "RewardsList_label__crystal_ad6e788d",
    label__tankXP: "RewardsList_label__tankXP_2ee96a57",
  },
  ve = o(function () {
    const { model: e } = I(),
      a = e.bonuses.get(),
      r = u(a),
      i = (function (e) {
        const s = e.filter((e) => e.name === ce),
          a = e.filter((e) => e.name !== ce),
          r = [];
        return (s.length > 0 && s[0] && r.push(s[0]), r.push(...a), r.slice(0, 5));
      })(r);
    return (0, E.jsxs)("div", {
      className: he.base,
      children: [
        (0, E.jsx)("div", { className: he.divider }),
        (0, E.jsx)("div", {
          className: he.rewardsContainer,
          children: i.map((e, a) => {
            const i = w.includes(e.name ?? ""),
              t = (function (e, s) {
                const a = s.filter((e) => e.name === ce).length;
                return "customization" === e.name && a > 1 ? a : (e.count ?? 0);
              })(e, r),
              n = t > 1 && !i,
              l = e.overlayType;
            return (0, E.jsxs)(
              "div",
              {
                className: he.reward,
                children: [
                  (0, E.jsx)(ge, {
                    showCounter: n,
                    count: t,
                    image: f(e, N.Big),
                    className: s(he.rewardImage, n && he.rewardImage__counter),
                  }),
                  l && (0, E.jsx)(me, { special: l, size: N.Small, className: he.overlay }),
                  i &&
                    (0, E.jsx)(je, { reward: e, className: s(he.label, he[`label__${e.name}`]) }),
                ],
              },
              `${e.id}__${a}`,
            );
          }),
        }),
      ],
    });
  }),
  pe = "Mission_1a8e8c9";
function be() {
  return (0, E.jsxs)("div", { className: pe, children: [(0, E.jsx)(le, {}), (0, E.jsx)(ve, {})] });
}
var fe = "TimerBlock_divider_c31a7a65",
  Ne = "TimerBlock_fbeff754",
  we = "TimerBlock_timerText_66570163",
  ye = n.resolve("strings"),
  Ie = o(function () {
    const { model: e } = I(),
      s = e.time.get();
    return (0, E.jsxs)(E.Fragment, {
      children: [
        (0, E.jsx)("div", { className: fe }),
        (0, E.jsx)("div", {
          className: Ne,
          children: (0, E.jsx)(m, {
            text: ye.readOrEmpty("user_missions.hub.challenge_missions.header.timer.text"),
            params: { timer: (0, E.jsx)(a, { size: t.x24x24, type: _.accent, start: s }, s) },
            className: we,
            upgradeLegacy: !0,
          }),
        }),
      ],
    });
  }),
  Le = "App_b3d5c0d8",
  Re = "active",
  ke = "default",
  Ce = o(function () {
    const { model: e } = I(),
      s = e.time.get() > 0,
      a = e.conditions.get(),
      r =
        (e.challengeName.get() ? Re : ke) === Re
          ? (0, E.jsxs)(E.Fragment, {
              children: [(0, E.jsx)(J, {}), a && (0, E.jsx)(be, {}), s && (0, E.jsx)(Ie, {})],
            })
          : (0, E.jsx)(H, {});
    return (0, E.jsx)("div", { className: Le, children: r });
  });
p(
  (0, E.jsx)(h, {
    children: (0, E.jsx)(y, {
      children: (0, E.jsx)(r, {
        children: (0, E.jsx)(r.Decorator, { children: (0, E.jsx)(Ce, {}) }),
      }),
    }),
  }),
);
