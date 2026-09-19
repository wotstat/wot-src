import { r as e } from "./rolldown-runtime.js";
import { A as t, Dn as r, F as o, Jt as s, j as i, lt as a, ut as d } from "./lib.js";
import { t as c } from "./divider.js";
var n = "ExtendedTooltipDecorator_312a767e",
  l = "ExtendedTooltipDecorator_header_37374fa6",
  m = "ExtendedTooltipDecorator_base__invertedColors_d4c2e366",
  x = "ExtendedTooltipDecorator_description_edb17499",
  p = "ExtendedTooltipDecorator_timerBlock_7b7647e1",
  _ = "ExtendedTooltipDecorator_divider_24cd0041",
  j = e(s(), 1);
function h({
  header: e,
  description: s,
  descriptionParams: h,
  invertedColors: D,
  timerTimeLeft: f = 0,
  timerPath: v = "user_missions.tooltip.common.timer",
  className: T,
  children: E,
}) {
  return (0, j.jsx)(t, {
    children: (0, j.jsx)(t.Decorator, {
      children: (0, j.jsxs)("div", {
        className: r(n, D && m, T),
        children: [
          e && (0, j.jsx)(d, { text: e, className: l }),
          (0, j.jsx)(o, { text: s, binding: h, classMix: x }),
          E,
          f > 0 &&
            (0, j.jsxs)("div", {
              className: p,
              children: [
                (0, j.jsx)(c, { className: _ }),
                (0, j.jsx)(a, { path: v, params: { timeLeft: (0, j.jsx)(i, { start: f }) } }),
              ],
            }),
        ],
      }),
    }),
  });
}
export { h as t };
