import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  A as e,
  E as r,
  Jt as t,
  On as a,
  Pn as c,
  St as n,
  dt as i,
  k as o,
  un as d,
  vt as l,
  yt as p,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ a();
var [m, _] = n()(({ observableModel: s }) => ({ root: s.object() }), d),
  j = "App_8ee77ed",
  x = "App_title_f53d8db4",
  u = "App_description_c94a25d1",
  b = "App_footer_6954e057",
  h = "App_icon_efac1a20",
  N = "App_separator_edcf04ac",
  y = "App_textBlock_a1aa5c7e",
  v = "App_currentNumber_d28826b0",
  A = "App_commonNumber_c5925018",
  f = "App_currency_d28826b0",
  g = s(t(), 1),
  k = c.resolve("strings"),
  E = "R.strings.user_missions.tooltip.hub.restart",
  O = l(function () {
    const { model: s } = _(),
      { freeRestarts: e, usedFreeRestarts: t, restartCost: a, currency: c } = s.root.get();
    return (0, g.jsxs)("div", {
      className: j,
      children: [
        (0, g.jsx)("div", { className: x, children: k.readOrEmpty(`${E}.title`) }),
        (0, g.jsx)("div", {
          className: u,
          children: (0, g.jsx)(o, { text: k.readOrEmpty(`${E}.description`) }),
        }),
        (0, g.jsxs)("div", {
          className: b,
          children: [
            (0, g.jsx)("div", { className: N }),
            (0, g.jsxs)("div", {
              className: y,
              children: [
                e - t > 0 &&
                  (0, g.jsx)(o, {
                    text: k.readOrEmpty(`${E}.free_restarts_text`),
                    binding: {
                      currentNumber: (0, g.jsx)("span", { className: v, children: e - t }),
                      commonNumber: (0, g.jsx)("span", { className: A, children: `/ ${e}` }),
                    },
                  }),
                (0, g.jsx)(o, {
                  text:
                    e - t <= 0
                      ? k.readOrEmpty(`${E}.only_paid_restart`)
                      : k.readOrEmpty(`${E}.free_restarts_cost`),
                  binding: {
                    currency: (0, g.jsx)(r, {
                      type: c,
                      reverse: !0,
                      classNames: { base: f, icon: h },
                      children: a,
                    }),
                  },
                }),
              ],
            }),
          ],
        }),
      ],
    });
  });
p(
  (0, g.jsx)(i, {
    children: (0, g.jsx)(m, {
      children: (0, g.jsx)(e, {
        children: (0, g.jsx)(e.Decorator, { children: (0, g.jsx)(O, {}) }),
      }),
    }),
  }),
);
