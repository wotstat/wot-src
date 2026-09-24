import { r as a } from "../../chunks/rolldown-runtime.js";
import {
  Br as e,
  G as s,
  J as r,
  Jn as n,
  Jt as i,
  Pr as t,
  Tt as o,
  Ur as l,
  X as d,
  Xn as c,
  _n as _,
  ci as f,
  ei as m,
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
var [R, N] = _()(({ observableModel: a }) => {
    const s = {
        root: a.object(),
        initialRewardsArray: a.array("initialReward"),
        compensationRewardsArray: a.array("compensationReward"),
      },
      r = b((a = 0) => t(s.initialRewardsArray.get().items, a), { equals: e }),
      n = b((a = 0) => t(s.compensationRewardsArray.get().items, a), { equals: e });
    return { ...s, computes: { initialReward: r, compensationReward: n } };
  }, l),
  k = "Arrow_c612004f",
  g = "Arrow_icon_ca620234",
  y = c();
function D({ className: a }) {
  return (0, y.jsx)("div", { className: f(k, a), children: (0, y.jsx)("div", { className: g }) });
}
var A = {
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
  O = "top",
  C = "bottom";
function E({ position: a }) {
  return (0, y.jsx)("div", { className: f(A.base, A[`base__${a}`]) });
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
      e === d.Vehicles &&
      ((a) => ["vehicleName", "vehicleType", "vehicleLvl", "isElite"].every((e) => e in a))(a)
    ) {
      const e = { base: S.label, name: S.tankName, level: S.tankLevel };
      return (0, y.jsx)(I, { ...a, vehicleTypeIconSize: o.x24x24, classNames: e });
    }
    if (e === d.Customizations) return (0, y.jsx)("span", { className: S.label, children: n });
    const i = u(s, r(e));
    return (0, y.jsx)("span", {
      className: f(S.label, S[`label__${e}`]),
      children: "string" == typeof i ? i : s,
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
      (0, y.jsx)(E, { position: O }),
      (0, y.jsx)(L, { reward: a }),
      (0, y.jsx)(D, { className: q }),
      (0, y.jsx)(L, { reward: e }),
      (0, y.jsx)(E, { position: C }),
    ],
  });
}
var J = "Footer_9d3d3a12",
  P = "Footer_compensation_b57b9f53",
  T = v.resolve("images"),
  z = v.resolve("strings");
function X() {
  const a = n(
    T.readOrEmpty("battlePass.tooltips.compensation"),
    T.readOrEmpty("battlePass.tooltips.compensation_large"),
  );
  return (0, y.jsxs)("div", {
    className: J,
    children: [
      (0, y.jsx)("div", { className: P, style: { backgroundImage: `url(${a})` } }),
      (0, y.jsx)("span", {
        children: z.readOrEmpty("battle_pass.tooltips.rewardCompensation.footer"),
      }),
    ],
  });
}
var B = "Header_title_487f6f3f",
  G = v.resolve("strings");
function H({ rewardName: a }) {
  return (0, y.jsxs)(y.Fragment, {
    children: [
      (0, y.jsx)("span", { className: B, children: m(a) }),
      (0, y.jsx)(i, {
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
