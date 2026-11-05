import { r as e } from "./rolldown-runtime.js";
import { A as t, En as r, F as s, ct as o, j as i, qt as a, st as d } from "./lib.js";
import { t as c } from "./divider.js";
var n = "ExtendedTooltipDecorator_312a767e",
  l = "ExtendedTooltipDecorator_header_37374fa6",
  m = "ExtendedTooltipDecorator_base__invertedColors_d4c2e366",
  x = "ExtendedTooltipDecorator_description_edb17499",
  p = "ExtendedTooltipDecorator_timerBlock_7b7647e1",
  _ = "ExtendedTooltipDecorator_divider_24cd0041",
  j = e(a(), 1);
function h({
  header: e,
  description: a,
  descriptionParams: h,
  invertedColors: f,
  timerTimeLeft: v = 0,
  timerPath: D = "user_missions.tooltip.common.timer",
  className: E,
  children: T,
}) {
  return (0, j.jsx)(t, {
    children: (0, j.jsx)(t.Decorator, {
      children: (0, j.jsxs)("div", {
        className: r(n, f && m, E),
        children: [
          e && (0, j.jsx)(o, { text: e, className: l }),
          (0, j.jsx)(s, { text: a, binding: h, classMix: x }),
          T,
          v > 0 &&
            (0, j.jsxs)("div", {
              className: p,
              children: [
                (0, j.jsx)(c, { className: _ }),
                (0, j.jsx)(d, { path: D, params: { timeLeft: (0, j.jsx)(i, { start: v }) } }),
              ],
            }),
        ],
      }),
    }),
  });
}
export { h as t };
