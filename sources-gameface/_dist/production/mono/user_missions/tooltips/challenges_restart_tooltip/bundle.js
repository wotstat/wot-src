import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  A as e,
  Dn as r,
  Nn as t,
  St as a,
  _t as c,
  ln as n,
  qt as i,
  vt as o,
  w as d,
  x as l,
  yt as p,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ r();
var [m, _] = a()(({ observableModel: s }) => ({ root: s.object() }), n),
  x = "App_8ee77ed",
  j = "App_title_f53d8db4",
  u = "App_description_c94a25d1",
  b = "App_footer_6954e057",
  h = "App_icon_efac1a20",
  N = "App_separator_edcf04ac",
  y = "App_textBlock_a1aa5c7e",
  v = "App_currentNumber_d28826b0",
  A = "App_commonNumber_c5925018",
  f = "App_currency_d28826b0",
  g = s(i(), 1),
  $ = t.resolve("strings"),
  k = "R.strings.user_missions.tooltip.hub.restart",
  E = c(function () {
    const { model: s } = _(),
      { freeRestarts: e, usedFreeRestarts: r, restartCost: t, currency: a } = s.root.get();
    return (0, g.jsxs)("div", {
      className: x,
      children: [
        (0, g.jsx)("div", { className: j, children: $.readOrEmpty(`${k}.title`) }),
        (0, g.jsx)("div", {
          className: u,
          children: (0, g.jsx)(d, { text: $.readOrEmpty(`${k}.description`) }),
        }),
        (0, g.jsxs)("div", {
          className: b,
          children: [
            (0, g.jsx)("div", { className: N }),
            (0, g.jsxs)("div", {
              className: y,
              children: [
                e - r > 0 &&
                  (0, g.jsx)(d, {
                    text: $.readOrEmpty(`${k}.free_restarts_text`),
                    binding: {
                      currentNumber: (0, g.jsx)("span", { className: v, children: e - r }),
                      commonNumber: (0, g.jsx)("span", { className: A, children: `/ ${e}` }),
                    },
                  }),
                (0, g.jsx)(d, {
                  text:
                    e - r <= 0
                      ? $.readOrEmpty(`${k}.only_paid_restart`)
                      : $.readOrEmpty(`${k}.free_restarts_cost`),
                  binding: {
                    currency: (0, g.jsx)(l, {
                      type: a,
                      reverse: !0,
                      classNames: { base: f, icon: h },
                      children: t,
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
  (0, g.jsx)(o, {
    children: (0, g.jsx)(m, {
      children: (0, g.jsx)(e, {
        children: (0, g.jsx)(e.Decorator, { children: (0, g.jsx)(E, {}) }),
      }),
    }),
  }),
);
