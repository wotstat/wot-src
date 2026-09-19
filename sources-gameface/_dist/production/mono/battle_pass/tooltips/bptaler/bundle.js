import { r as s } from "../../chunks/rolldown-runtime.js";
import { Xn as e, fn as t, n, pn as a, tn as r, ui as i } from "../../chunks/lib.js";
import "../../chunks/global.js";
import { t as c } from "../../chunks/separator.js";
i();
var l = "Content_b5324543",
  o = "Content_image_f3e02a04",
  d = "Content_section_cf0c3481",
  j = "Content_title_73d62fc4",
  x = "Content_text_8f35597f",
  m = "Content_secondaryText_69f1894",
  _ = e(),
  h = R.strings.battle_pass.tooltips.battlePassTaler,
  f = () =>
    (0, _.jsxs)("div", {
      className: l,
      children: [
        (0, _.jsx)("div", { className: o }),
        (0, _.jsxs)("div", {
          className: d,
          children: [
            (0, _.jsx)(c, {}),
            (0, _.jsx)("div", { className: j, children: h.title() }),
            (0, _.jsx)("div", { className: x, children: h.text() }),
            (0, _.jsx)(c, {}),
          ],
        }),
        (0, _.jsx)("div", { className: m, children: h.secondaryText() }),
      ],
    }),
  p = () => (0, _.jsx)(n, { children: (0, _.jsx)(n.Decorator, { children: (0, _.jsx)(f, {}) }) });
t(new a().add(r).render((0, _.jsx)(p, {})));
