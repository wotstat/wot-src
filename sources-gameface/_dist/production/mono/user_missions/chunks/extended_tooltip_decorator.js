import { r as e } from "./rolldown-runtime.js";
import { A as t, Dn as r, E as s, I as o, Jt as i, ct as a, st as d } from "./lib.js";
import { t as c } from "./divider.js";
var n = "ExtendedTooltipDecorator_312a767e",
  l = "ExtendedTooltipDecorator_header_37374fa6",
  m = "ExtendedTooltipDecorator_base__invertedColors_d4c2e366",
  x = "ExtendedTooltipDecorator_description_edb17499",
  p = "ExtendedTooltipDecorator_timerBlock_7b7647e1",
  _ = "ExtendedTooltipDecorator_divider_24cd0041",
  j = e(i(), 1);
function h({
  header: e,
  description: i,
  descriptionParams: h,
  invertedColors: D,
  timerTimeLeft: f = 0,
  timerPath: v = "user_missions.tooltip.common.timer",
  className: E,
  children: T,
}) {
  return (0, j.jsx)(o, {
    children: (0, j.jsx)(o.Decorator, {
      children: (0, j.jsxs)("div", {
        className: r(n, D && m, E),
        children: [
          e && (0, j.jsx)(a, { text: e, className: l }),
          (0, j.jsx)(t, { text: i, binding: h, classMix: x }),
          T,
          f > 0 &&
            (0, j.jsxs)("div", {
              className: p,
              children: [
                (0, j.jsx)(c, { className: _ }),
                (0, j.jsx)(d, { path: v, params: { timeLeft: (0, j.jsx)(s, { start: f }) } }),
              ],
            }),
        ],
      }),
    }),
  });
}
export { h as t };
