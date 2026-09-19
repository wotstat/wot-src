import { n as s, r as e } from "../../chunks/rolldown-runtime.js";
import {
  A as t,
  Cn as a,
  Dn as n,
  Jt as r,
  On as o,
  Pn as i,
  Sn as l,
  St as m,
  Tn as c,
  bn as d,
  bt as p,
  dn as u,
  gt as x,
  ht as h,
  j,
  kt as _,
  lt as f,
  mt as v,
  un as b,
  ut as y,
  v as k,
  vn as N,
  vt as g,
  xn as C,
  xt as w,
  yt as I,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ import { t as A } from "../../chunks/divider.js";
import { t as O } from "../../chunks/helpers.js";
import { t as S } from "../../chunks/spec_conditions.js";
var T = e(o(), 1),
  [D, M] = m()(({ observableModel: s }) => {
    const e = s.primitives(["params", "type"]);
    return {
      type: e.type,
      computes: {
        params: w.primitive(function (s) {
          return s(e.params.get());
        }),
      },
    };
  }, b);
function P(s) {
  return function () {
    return M().model.computes.params(s);
  };
}
var $ = "Index_62decda",
  E = "Index_header_805f33ff",
  B = "Index_description_21b8299a",
  J = "Index_timerBlock_6d6f592",
  L = "Index_divider_835afce3",
  R = s({ RerollTooltipParamsSchema: () => q, default: () => H }),
  U = e(r(), 1),
  q = x({ rerollCooldown: h(), rerollAvailableTimestamp: h() }),
  z = P(k(q)),
  F = (s, e, t) =>
    s > 0 ? (e > 0 ? "days_hrs" : "days") : e > 0 ? (t > 0 ? "hrs_mins" : "hrs") : "mins",
  G = i.resolve("strings");
function H() {
  const { rerollCooldown: s, rerollAvailableTimestamp: e } = z(),
    [n, r, o] = N(l(s), ["D", "h", "m"]),
    i = _((0, T.useMemo)(() => ({ until: d(e), tick: l(1) }), [e])),
    m = (0, T.useMemo)(() => u(d(e), (s) => a(s, C()), c), [e]);
  return (0, U.jsx)(t, {
    children: (0, U.jsx)(t.Decorator, {
      children: (0, U.jsxs)("div", {
        className: $,
        children: [
          (0, U.jsx)(f, { path: "user_missions.tooltip.daily_reroll.header", className: E }),
          (0, U.jsx)("div", {
            className: B,
            children: G.readOrEmpty("user_missions.tooltip.weekly_reroll.description")
              .split("\n")
              .map((s, e) =>
                (0, U.jsx)(
                  y,
                  {
                    text: s,
                    split: !0,
                    params: {
                      time: (0, U.jsx)(f, {
                        path: `user_missions.common.duration.${F(Number(n), Number(r), Number(o))}`,
                        params: { days: n, hours: r, minutes: o },
                      }),
                    },
                  },
                  `${s}-${e}`,
                ),
              ),
          }),
          !1 === i.done &&
            (0, U.jsxs)("div", {
              className: J,
              children: [
                (0, U.jsx)(A, { className: L }),
                (0, U.jsx)(f, {
                  path: "user_missions.tooltip.common.timer",
                  params: { timeLeft: (0, U.jsx)(j, { start: m }) },
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
  V = x({ specConditions: v(O) }),
  W = P(k(V));
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
var ts = g(function () {
  const { model: s } = M(),
    e = s.type.get(),
    a = es[e]?.Component;
  return (0, U.jsx)(t, { children: a ? (0, U.jsx)(a, {}) : (0, U.jsx)(ss, { type: e }) });
});
I(new p().add(D).render((0, U.jsx)(ts, {})));
