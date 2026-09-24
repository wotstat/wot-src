import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  F as e,
  I as r,
  Jt as t,
  M as a,
  On as c,
  Pn as n,
  St as i,
  _t as o,
  un as d,
  vt as l,
  yt as p,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ c();
var [m, _] = i()(({ observableModel: s }) => ({ root: s.object() }), d),
  j = "App_8ee77ed",
  x = "App_title_f53d8db4",
  u = "App_description_c94a25d1",
  b = "App_footer_6954e057",
  h = "App_icon_efac1a20",
  N = "App_separator_edcf04ac",
  y = "App_textBlock_a1aa5c7e",
  v = "App_currentNumber_d28826b0",
  f = "App_commonNumber_c5925018",
  A = "App_currency_d28826b0",
  g = s(t(), 1),
  O = n.resolve("strings"),
  $ = "R.strings.user_missions.tooltip.hub.restart",
  k = o(function () {
    const { model: s } = _(),
      { freeRestarts: r, usedFreeRestarts: t, restartCost: c, currency: n } = s.root.get();
    return (0, g.jsxs)("div", {
      className: j,
      children: [
        (0, g.jsx)("div", { className: x, children: O.readOrEmpty(`${$}.title`) }),
        (0, g.jsx)("div", {
          className: u,
          children: (0, g.jsx)(e, { text: O.readOrEmpty(`${$}.description`) }),
        }),
        (0, g.jsxs)("div", {
          className: b,
          children: [
            (0, g.jsx)("div", { className: N }),
            (0, g.jsxs)("div", {
              className: y,
              children: [
                r - t > 0 &&
                  (0, g.jsx)(e, {
                    text: O.readOrEmpty(`${$}.free_restarts_text`),
                    binding: {
                      currentNumber: (0, g.jsx)("span", { className: v, children: r - t }),
                      commonNumber: (0, g.jsx)("span", { className: f, children: `/ ${r}` }),
                    },
                  }),
                (0, g.jsx)(e, {
                  text:
                    r - t <= 0
                      ? O.readOrEmpty(`${$}.only_paid_restart`)
                      : O.readOrEmpty(`${$}.free_restarts_cost`),
                  binding: {
                    currency: (0, g.jsx)(a, {
                      type: n,
                      reverse: !0,
                      classNames: { base: A, icon: h },
                      children: c,
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
  (0, g.jsx)(l, {
    children: (0, g.jsx)(m, {
      children: (0, g.jsx)(r, {
        children: (0, g.jsx)(r.Decorator, { children: (0, g.jsx)(k, {}) }),
      }),
    }),
  }),
);
