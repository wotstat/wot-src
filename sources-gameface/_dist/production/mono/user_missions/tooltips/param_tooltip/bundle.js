import { n as s, r as e } from "../../chunks/rolldown-runtime.js";
import {
  A as t,
  Dn as a,
  En as n,
  Nn as r,
  Sn as o,
  St as i,
  _n as l,
  _t as m,
  bn as c,
  bt as d,
  ct as p,
  dt as u,
  ft as x,
  j as h,
  kt as j,
  ln as _,
  qt as f,
  st as v,
  un as b,
  ut as y,
  v as k,
  wn as N,
  xn as g,
  xt as w,
  yn as C,
  yt as I,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ import { t as A } from "../../chunks/divider.js";
import { t as S } from "../../chunks/spec_conditions.js";
import { t as D } from "../../chunks/helpers.js";
var O = e(a(), 1),
  [T, E] = i()(({ observableModel: s }) => {
    const e = s.primitives(["params", "type"]);
    return {
      type: e.type,
      computes: {
        params: w.primitive(function (s) {
          return s(e.params.get());
        }),
      },
    };
  }, _);
function M(s) {
  return function () {
    return E().model.computes.params(s);
  };
}
var $ = "Index_62decda",
  P = "Index_header_805f33ff",
  q = "Index_description_21b8299a",
  B = "Index_timerBlock_6d6f592",
  L = "Index_divider_835afce3",
  R = s({ RerollTooltipParamsSchema: () => z, default: () => J }),
  U = e(f(), 1),
  z = x({ rerollCooldown: u(), rerollAvailableTimestamp: u() }),
  F = M(k(z)),
  G = (s, e, t) =>
    s > 0 ? (e > 0 ? "days_hrs" : "days") : e > 0 ? (t > 0 ? "hrs_mins" : "hrs") : "mins",
  H = r.resolve("strings");
function J() {
  const { rerollCooldown: s, rerollAvailableTimestamp: e } = F(),
    [a, n, r] = l(g(s), ["D", "h", "m"]),
    i = j((0, O.useMemo)(() => ({ until: C(e), tick: g(1) }), [e])),
    m = (0, O.useMemo)(() => b(C(e), (s) => o(s, c()), N), [e]);
  return (0, U.jsx)(t, {
    children: (0, U.jsx)(t.Decorator, {
      children: (0, U.jsxs)("div", {
        className: $,
        children: [
          (0, U.jsx)(v, { path: "user_missions.tooltip.daily_reroll.header", className: P }),
          (0, U.jsx)("div", {
            className: q,
            children: H.readOrEmpty("user_missions.tooltip.weekly_reroll.description")
              .split("\n")
              .map((s, e) =>
                (0, U.jsx)(
                  p,
                  {
                    text: s,
                    split: !0,
                    params: {
                      time: (0, U.jsx)(v, {
                        path: `user_missions.common.duration.${G(Number(a), Number(n), Number(r))}`,
                        params: { days: a, hours: n, minutes: r },
                      }),
                    },
                  },
                  `${s}-${e}`,
                ),
              ),
          }),
          !1 === i.done &&
            (0, U.jsxs)("div", {
              className: B,
              children: [
                (0, U.jsx)(A, { className: L }),
                (0, U.jsx)(v, {
                  path: "user_missions.tooltip.common.timer",
                  params: { timeLeft: (0, U.jsx)(h, { start: m }) },
                }),
              ],
            }),
        ],
      }),
    }),
  });
}
var K = "Index_d037ad5c",
  Q = s({ SpecConditionsTooltipParamsSchema: () => V, default: () => X }),
  V = x({ specConditions: y(D) }),
  W = M(k(V));
function X() {
  const { specConditions: s } = W();
  return (0, U.jsx)(t, {
    children: (0, U.jsx)(t.Decorator, {
      children: (0, U.jsx)("div", { className: K, children: (0, U.jsx)(S, { specConditions: s }) }),
    }),
  });
}
var Y = "App_text_13feac86",
  Z = "App_text__bold_f88f7b4e";
function ss({ type: s }) {
  return (0, U.jsxs)("div", {
    className: Y,
    children: [
      "Unknown tooltip type:",
      (0, U.jsx)("span", { className: n(Y, Z), children: s.length > 0 ? s : "<empty>" }),
    ],
  });
}
var es = Object.fromEntries(
  Object.entries(Object.assign({ "./reroll/index.tsx": R, "./spec_conditions/index.tsx": Q })).map(
    ([s, e]) => [s.split("/").at(-2), { Component: e.default }],
  ),
);
var ts = m(function () {
  const { model: s } = E(),
    e = s.type.get(),
    a = es[e]?.Component;
  return (0, U.jsx)(t, { children: a ? (0, U.jsx)(a, {}) : (0, U.jsx)(ss, { type: e }) });
});
I(new d().add(T).render((0, U.jsx)(ts, {})));
