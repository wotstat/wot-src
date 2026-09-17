import { j as e, e as o } from "./vendor.js";
import { D as s } from "./divider.js";
import { w as r, x as t, a1 as i, F as a, y as d } from "./lib.js";
const c = "ExtendedTooltipDecorator_312a767e",
  n = "ExtendedTooltipDecorator_header_37374fa6",
  l = "ExtendedTooltipDecorator_base__invertedColors_d4c2e366",
  m = "ExtendedTooltipDecorator_description_edb17499",
  x = "ExtendedTooltipDecorator_timerBlock_7b7647e1",
  p = "ExtendedTooltipDecorator_divider_24cd0041";
function _({
  header: _,
  description: j,
  descriptionParams: h,
  invertedColors: D,
  timerTimeLeft: f = 0,
  timerPath: v = "user_missions.tooltip.common.timer",
  className: E,
  children: T,
}) {
  return e.jsx(r, {
    children: e.jsx(r.Decorator, {
      children: e.jsxs("div", {
        className: o(c, D && l, E),
        children: [
          _ && e.jsx(t, { text: _, className: n }),
          e.jsx(i, { text: j, binding: h, classMix: m }),
          T,
          f > 0 &&
            e.jsxs("div", {
              className: x,
              children: [
                e.jsx(s, { className: p }),
                e.jsx(a, { path: v, params: { timeLeft: e.jsx(d, { start: f }) } }),
              ],
            }),
        ],
      }),
    }),
  });
}
export { _ as E };
