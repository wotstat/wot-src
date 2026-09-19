import { r as s } from "../../chunks/rolldown-runtime.js";
import { Xn as e, fn as t, n, pn as a, tn as i, ui as c } from "../../chunks/lib.js";
import "../../chunks/global.js";
c();
var l = "Content_7bb15980",
  r = "Content_separator_9582cf97",
  o = "Content_image_2c4b4824",
  d = "Content_section_cf0c3481",
  x = "Content_title_73d62fc4",
  j = "Content_text_8f35597f",
  m = "Content_secondaryText_69f1894",
  _ = e(),
  h = R.strings.battle_pass.tooltips.battlePassCoins,
  f = h.title(),
  v = h.text(),
  C = h.secondaryText(),
  N = () =>
    (0, _.jsxs)("div", {
      className: l,
      children: [
        (0, _.jsx)("div", { className: o }),
        (0, _.jsxs)("div", {
          className: d,
          children: [
            (0, _.jsx)("div", { className: r }),
            (0, _.jsx)("div", { className: x, children: f }),
            (0, _.jsx)("div", { className: j, children: v }),
            (0, _.jsx)("div", { className: r }),
          ],
        }),
        (0, _.jsx)("div", { className: m, children: C }),
      ],
    }),
  b = () => (0, _.jsx)(n, { children: (0, _.jsx)(n.Decorator, { children: (0, _.jsx)(N, {}) }) });
t(new a().add(i).render((0, _.jsx)(b, {})));
