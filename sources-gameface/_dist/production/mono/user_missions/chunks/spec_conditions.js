import { r as s } from "./rolldown-runtime.js";
import { Jt as i, Pn as t, ct as e, lt as o, on as a } from "./lib.js";
var n = "SpecConditions_title_af03f2f",
  c = "SpecConditions_specCondition_b0565ee6",
  r = "SpecConditions_specConditionText_5455dba",
  l = s(i(), 1),
  d = t.resolve("strings");
function p(s) {
  return (0, l.jsxs)("div", {
    className: s.className,
    children: [
      (0, l.jsx)(o, { path: "user_missions.tooltip.vehicle_restrictions", className: n }),
      a(s.specConditions, (s) =>
        (0, l.jsxs)(
          "div",
          {
            className: c,
            children: [
              (0, l.jsx)(e, { width: 24, height: 24, path: s.iconPath }),
              (0, l.jsx)(o, {
                path: "weekly_quests.specialCondition.tooltip",
                params: { condition: d.read(s.textPath) },
                className: r,
              }),
            ],
          },
          s.id,
        ),
      ),
    ],
  });
}
export { p as t };
