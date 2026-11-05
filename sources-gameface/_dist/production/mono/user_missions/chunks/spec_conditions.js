import { r as s } from "./rolldown-runtime.js";
import { Nn as i, an as t, ot as e, qt as o, st as a } from "./lib.js";
var n = "SpecConditions_title_af03f2f",
  r = "SpecConditions_specCondition_b0565ee6",
  c = "SpecConditions_specConditionText_5455dba",
  d = s(o(), 1),
  l = i.resolve("strings");
function p(s) {
  return (0, d.jsxs)("div", {
    className: s.className,
    children: [
      (0, d.jsx)(a, { path: "user_missions.tooltip.vehicle_restrictions", className: n }),
      t(s.specConditions, (s) =>
        (0, d.jsxs)(
          "div",
          {
            className: r,
            children: [
              (0, d.jsx)(e, { width: 24, height: 24, path: s.iconPath }),
              (0, d.jsx)(a, {
                path: "weekly_quests.specialCondition.tooltip",
                params: { condition: l.read(s.textPath) },
                className: c,
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
