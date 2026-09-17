import {
  r as s,
  j as e,
  v as t,
  E as o,
  F as r,
  e as n,
  D as a,
} from "../../../../chunks/vendor.js";
import {
  i,
  O as l,
  n as c,
  g as m,
  f as d,
  b as p,
  P as u,
  Q as j,
  R as x,
  S as _,
  V as h,
  W as f,
  w as b,
  F as y,
  x as v,
  y as g,
  X as N,
  J as k,
  r as S,
} from "../../../../chunks/lib.js";
import { D as O } from "../../../../chunks/divider.js";
import { S as C } from "../../../../chunks/helpers.js";
import { S as w } from "../../../../chunks/spec_conditions.js";
/* empty css                       */ const [I, T] = i()(({ observableModel: s }) => {
  const e = s.primitives(["params", "type"]);
  return {
    type: e.type,
    computes: {
      params: l.primitive(function (s) {
        return s(e.params.get());
      }),
    },
  };
}, c);
function D(s) {
  return function () {
    return T().model.computes.params(s);
  };
}
const M = "Index_62decda",
  P = "Index_header_805f33ff",
  A = "Index_description_21b8299a",
  E = "Index_timerBlock_6d6f592",
  $ = "Index_divider_835afce3",
  z = t({ rerollCooldown: o(), rerollAvailableTimestamp: o() }),
  F = D(N(z)),
  R = (s, e, t) =>
    s > 0 ? (e > 0 ? "days_hrs" : "days") : e > 0 ? (t > 0 ? "hrs_mins" : "hrs") : "mins",
  B = m.resolve("strings");
const J = Object.freeze(
    Object.defineProperty(
      {
        __proto__: null,
        RerollTooltipParamsSchema: z,
        default: function () {
          const { rerollCooldown: t, rerollAvailableTimestamp: o } = F(),
            [r, n, a] = d(p(t), ["D", "h", "m"]),
            i = u(s.useMemo(() => ({ until: j(o), tick: p(1) }), [o])),
            l = s.useMemo(() => x(j(o), (s) => h(s, f()), _), [o]);
          return e.jsx(b, {
            children: e.jsx(b.Decorator, {
              children: e.jsxs("div", {
                className: M,
                children: [
                  e.jsx(y, { path: "user_missions.tooltip.daily_reroll.header", className: P }),
                  e.jsx("div", {
                    className: A,
                    children: B.readOrEmpty("user_missions.tooltip.weekly_reroll.description")
                      .split("\n")
                      .map((s, t) =>
                        e.jsx(
                          v,
                          {
                            text: s,
                            split: !0,
                            params: {
                              time: e.jsx(y, {
                                path: `user_missions.common.duration.${R(Number(r), Number(n), Number(a))}`,
                                params: { days: r, hours: n, minutes: a },
                              }),
                            },
                          },
                          `${s}-${t}`,
                        ),
                      ),
                  }),
                  !1 === i.done &&
                    e.jsxs("div", {
                      className: E,
                      children: [
                        e.jsx(O, { className: $ }),
                        e.jsx(y, {
                          path: "user_missions.tooltip.common.timer",
                          params: { timeLeft: e.jsx(g, { start: l }) },
                        }),
                      ],
                    }),
                ],
              }),
            }),
          });
        },
      },
      Symbol.toStringTag,
      { value: "Module" },
    ),
  ),
  L = "Index_d037ad5c",
  Q = t({ specConditions: r(C) }),
  U = D(N(Q));
const V = Object.freeze(
    Object.defineProperty(
      {
        __proto__: null,
        SpecConditionsTooltipParamsSchema: Q,
        default: function () {
          const { specConditions: s } = U();
          return e.jsx(b, {
            children: e.jsx(b.Decorator, {
              children: e.jsx("div", { className: L, children: e.jsx(w, { specConditions: s }) }),
            }),
          });
        },
      },
      Symbol.toStringTag,
      { value: "Module" },
    ),
  ),
  W = "App_text_13feac86",
  X = "App_text__bold_f88f7b4e";
function q({ type: s }) {
  return e.jsxs("div", {
    className: W,
    children: [
      "Unknown tooltip type:",
      e.jsx("span", { className: n(W, X), children: s.length > 0 ? s : "<empty>" }),
    ],
  });
}
const G = Object.fromEntries(
  Object.entries(Object.assign({ "./reroll/index.tsx": J, "./spec_conditions/index.tsx": V })).map(
    ([s, e]) => [s.split("/").at(-2), { Component: e.default }],
  ),
);
const H = a(function () {
  const { model: s } = T(),
    t = s.type.get(),
    o = G[t]?.Component;
  return e.jsx(b, { children: o ? e.jsx(o, {}) : e.jsx(q, { type: t }) });
});
S(new k().add(I).render(e.jsx(H, {})));
