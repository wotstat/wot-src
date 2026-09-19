import { r } from "../../chunks/rolldown-runtime.js";
import {
  Jt as s,
  Pn as e,
  Sn as t,
  St as o,
  un as i,
  vn as l,
  vt as a,
  yt as n,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ import { t as m } from "../../chunks/extended_tooltip_decorator.js";
var [d, p] = o()(
    ({ observableModel: r }) => ({ ...r.primitives(["timeLeft", "rerollInterval"]) }),
    i,
  ),
  c = r(s(), 1),
  u = a(function () {
    const { model: r } = p(),
      s = e.resolve("strings"),
      [o] = l(t(r.rerollInterval.get()), ["h"]);
    return (0, c.jsx)(m, {
      header: s.readOrEmpty("user_missions.tooltip.daily_reroll.header"),
      description: s.readOrEmpty("user_missions.tooltip.daily_reroll.description"),
      descriptionParams: { time: o },
      timerTimeLeft: r.timeLeft.get(),
    });
  });
n((0, c.jsx)(d, { children: (0, c.jsx)(u, {}) }));
