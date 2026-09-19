import { r as a } from "../../chunks/rolldown-runtime.js";
import {
  Br as e,
  G as s,
  J as r,
  Jn as n,
  Ot as i,
  Pr as t,
  Ur as o,
  X as l,
  Xn as d,
  _n as c,
  ci as _,
  ei as f,
  en as m,
  fn as p,
  gn as b,
  n as w,
  pi as v,
  q as u,
  ui as j,
} from "../../chunks/lib.js";
import "../../chunks/global.js";
import { h } from "../../chunks/vendor.js";
import { a as x } from "../../chunks/utils.js";
import { t as I } from "../../chunks/tank_name.js";
j();
var [R, N] = c()(({ observableModel: a }) => {
    const s = {
        root: a.object(),
        initialRewardsArray: a.array("initialReward"),
        compensationRewardsArray: a.array("compensationReward"),
      },
      r = b((a = 0) => t(s.initialRewardsArray.get().items, a), { equals: e }),
      n = b((a = 0) => t(s.compensationRewardsArray.get().items, a), { equals: e });
    return { ...s, computes: { initialReward: r, compensationReward: n } };
  }, o),
  k = "Arrow_c612004f",
  g = "Arrow_icon_ca620234",
  y = d();
function D({ className: a }) {
  return (0, y.jsx)("div", { className: _(k, a), children: (0, y.jsx)("div", { className: g }) });
}
var O = {
    base: "Divider_d6b67ddd",
    base__top: "Divider_base__top_6e207943",
    base__bottom: "Divider_base__bottom_6fbb70c2",
    fadeInWithScale: "Divider_fadeInWithScale_76b1f722",
    slideUp: "Divider_slideUp_76b1f722",
    blink: "Divider_blink_76b1f722",
    scale: "Divider_scale_76b1f722",
    rotate: "Divider_rotate_76b1f722",
    windowIn: "Divider_windowIn_76b1f722",
    fadeOut: "Divider_fadeOut_76b1f722",
    fadeIn: "Divider_fadeIn_76b1f722",
  },
  A = "top",
  C = "bottom";
function E({ position: a }) {
  return (0, y.jsx)("div", { className: _(O.base, O[`base__${a}`]) });
}
var S = {
    base: "RewardInfo_16031c66",
    label: "RewardInfo_label_e66cbfb1",
    label__credits: "RewardInfo_label__credits_aa1c1024",
    label__gold: "RewardInfo_label__gold_a5de1414",
    tankLevel: "RewardInfo_tankLevel_4a85f1a2",
    tankName: "RewardInfo_tankName_c36dc6e0",
    fadeInWithScale: "RewardInfo_fadeInWithScale_4a85f1a2",
    slideUp: "RewardInfo_slideUp_4a85f1a2",
    blink: "RewardInfo_blink_4a85f1a2",
    scale: "RewardInfo_scale_4a85f1a2",
    rotate: "RewardInfo_rotate_4a85f1a2",
    windowIn: "RewardInfo_windowIn_4a85f1a2",
    fadeOut: "RewardInfo_fadeOut_4a85f1a2",
    fadeIn: "RewardInfo_fadeIn_4a85f1a2",
  },
  U = (a) => {
    const { name: e, value: s, userName: n } = a;
    if (
      e === l.Vehicles &&
      ((a) => ["vehicleName", "vehicleType", "vehicleLvl", "isElite"].every((e) => e in a))(a)
    ) {
      const e = { base: S.label, name: S.tankName, level: S.tankLevel };
      return (0, y.jsx)(I, { ...a, vehicleTypeIconSize: i.x24x24, classNames: e });
    }
    if (e === l.Customizations) return (0, y.jsx)("span", { className: S.label, children: n });
    const t = u(s, r(e));
    return (0, y.jsx)("span", {
      className: _(S.label, S[`label__${e}`]),
      children: "string" == typeof t ? t : s,
    });
  };
function L({ reward: a }) {
  const { value: e, tooltipArgs: r, ...n } = x(a);
  return (0, y.jsxs)("div", { className: S.base, children: [(0, y.jsx)(s, { ...n }), U(a)] });
}
var W = "Content_c10787ee",
  $ = "Content_highlight_209aac4a",
  q = "Content_arrow_e7a821c";
function F({ initialReward: a, compensationReward: e }) {
  return (0, y.jsxs)("div", {
    className: W,
    children: [
      (0, y.jsx)("div", { className: $ }),
      (0, y.jsx)(E, { position: A }),
      (0, y.jsx)(L, { reward: a }),
      (0, y.jsx)(D, { className: q }),
      (0, y.jsx)(L, { reward: e }),
      (0, y.jsx)(E, { position: C }),
    ],
  });
}
var P = "Footer_9d3d3a12",
  z = "Footer_compensation_b57b9f53",
  J = v.resolve("images"),
  T = v.resolve("strings");
function X() {
  const a = n(
    J.readOrEmpty("battlePass.tooltips.compensation"),
    J.readOrEmpty("battlePass.tooltips.compensation_large"),
  );
  return (0, y.jsxs)("div", {
    className: P,
    children: [
      (0, y.jsx)("div", { className: z, style: { backgroundImage: `url(${a})` } }),
      (0, y.jsx)("span", {
        children: T.readOrEmpty("battle_pass.tooltips.rewardCompensation.footer"),
      }),
    ],
  });
}
var B = "Header_title_487f6f3f",
  G = v.resolve("strings");
function H({ rewardName: a }) {
  return (0, y.jsxs)(y.Fragment, {
    children: [
      (0, y.jsx)("span", { className: B, children: f(a) }),
      (0, y.jsx)(m, {
        text: G.readOrEmpty(`battle_pass.tooltips.rewardCompensation.description.${a}`),
      }),
    ],
  });
}
var M = "App_fc800ea3",
  V = h(() => {
    const { model: a } = N(),
      e = a.computes.initialReward(),
      s = a.computes.compensationReward();
    return (0, y.jsxs)("div", {
      className: M,
      children: [
        (0, y.jsx)(H, { rewardName: s.name }),
        (0, y.jsx)(F, { initialReward: e, compensationReward: s }),
        (0, y.jsx)(X, {}),
      ],
    });
  });
p(
  (0, y.jsx)(R, {
    children: (0, y.jsx)(w, { children: (0, y.jsx)(w.Decorator, { children: (0, y.jsx)(V, {}) }) }),
  }),
);
