import { n as s, r as e } from "../../chunks/rolldown-runtime.js";
import {
  Cn as t,
  Dn as a,
  E as n,
  I as r,
  Jt as o,
  On as i,
  Pn as l,
  Sn as m,
  St as c,
  Tn as d,
  _t as p,
  b as u,
  bn as x,
  bt as h,
  ct as j,
  dn as _,
  dt as f,
  ft as v,
  kt as b,
  st as y,
  un as k,
  ut as N,
  vn as C,
  xn as g,
  xt as w,
  yt as I,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ import { t as O } from "../../chunks/divider.js";
import { t as S } from "../../chunks/helpers.js";
import { t as T } from "../../chunks/spec_conditions.js";
var A = e(i(), 1),
  [D, E] = c()(({ observableModel: s }) => {
    const e = s.primitives(["params", "type"]);
    return {
      type: e.type,
      computes: {
        params: w.primitive(function (s) {
          return s(e.params.get());
        }),
      },
    };
  }, k);
function M(s) {
  return function () {
    return E().model.computes.params(s);
  };
}
var P = "Index_62decda",
  $ = "Index_header_805f33ff",
  B = "Index_description_21b8299a",
  J = "Index_timerBlock_6d6f592",
  L = "Index_divider_835afce3",
  R = s({ RerollTooltipParamsSchema: () => q, default: () => H }),
  U = e(o(), 1),
  q = v({ rerollCooldown: f(), rerollAvailableTimestamp: f() }),
  z = M(u(q)),
  F = (s, e, t) =>
    s > 0 ? (e > 0 ? "days_hrs" : "days") : e > 0 ? (t > 0 ? "hrs_mins" : "hrs") : "mins",
  G = l.resolve("strings");
function H() {
  const { rerollCooldown: s, rerollAvailableTimestamp: e } = z(),
    [a, o, i] = C(m(s), ["D", "h", "m"]),
    l = b((0, A.useMemo)(() => ({ until: x(e), tick: m(1) }), [e])),
    c = (0, A.useMemo)(() => _(x(e), (s) => t(s, g()), d), [e]);
  return (0, U.jsx)(r, {
    children: (0, U.jsx)(r.Decorator, {
      children: (0, U.jsxs)("div", {
        className: P,
        children: [
          (0, U.jsx)(y, { path: "user_missions.tooltip.daily_reroll.header", className: $ }),
          (0, U.jsx)("div", {
            className: B,
            children: G.readOrEmpty("user_missions.tooltip.weekly_reroll.description")
              .split("\n")
              .map((s, e) =>
                (0, U.jsx)(
                  j,
                  {
                    text: s,
                    split: !0,
                    params: {
                      time: (0, U.jsx)(y, {
                        path: `user_missions.common.duration.${F(Number(a), Number(o), Number(i))}`,
                        params: { days: a, hours: o, minutes: i },
                      }),
                    },
                  },
                  `${s}-${e}`,
                ),
              ),
          }),
          !1 === l.done &&
            (0, U.jsxs)("div", {
              className: J,
              children: [
                (0, U.jsx)(O, { className: L }),
                (0, U.jsx)(y, {
                  path: "user_missions.tooltip.common.timer",
                  params: { timeLeft: (0, U.jsx)(n, { start: c }) },
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
  V = v({ specConditions: N(S) }),
  W = M(u(V));
function X() {
  const { specConditions: s } = W();
  return (0, U.jsx)(r, {
    children: (0, U.jsx)(r.Decorator, {
      children: (0, U.jsx)("div", { className: K, children: (0, U.jsx)(T, { specConditions: s }) }),
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
      (0, U.jsx)("span", { className: a(Y, Z), children: s.length > 0 ? s : "<empty>" }),
    ],
  });
}
var es = Object.fromEntries(
  Object.entries(Object.assign({ "./reroll/index.tsx": R, "./spec_conditions/index.tsx": Q })).map(
    ([s, e]) => [s.split("/").at(-2), { Component: e.default }],
  ),
);
var ts = p(function () {
  const { model: s } = E(),
    e = s.type.get(),
    t = es[e]?.Component;
  return (0, U.jsx)(r, { children: t ? (0, U.jsx)(t, {}) : (0, U.jsx)(ss, { type: e }) });
});
I(new h().add(D).render((0, U.jsx)(ts, {})));
