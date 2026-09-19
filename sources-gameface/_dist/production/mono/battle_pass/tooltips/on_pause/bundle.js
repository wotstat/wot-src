import { r as s } from "../../chunks/rolldown-runtime.js";
import { Xn as n, fn as t, n as a, pn as e, tn as i, ui as r } from "../../chunks/lib.js";
import "../../chunks/global.js";
r();
var o = "Content_bc5bf6b3",
  d = "Content_title_bbf31abd",
  l = "Content_description_68c5b5a4",
  c = n(),
  b = () =>
    (0, c.jsxs)("div", {
      className: o,
      children: [
        (0, c.jsx)("div", {
          className: d,
          children: R.strings.battle_pass.tooltips.entryPoint.disabled.header(),
        }),
        (0, c.jsx)("div", {
          className: l,
          children: R.strings.battle_pass.tooltips.entryPoint.disabled.body(),
        }),
      ],
    }),
  j = () => (0, c.jsx)(a, { children: (0, c.jsx)(a.Decorator, { children: (0, c.jsx)(b, {}) }) });
t(new e().add(i).render((0, c.jsx)(j, {})));
