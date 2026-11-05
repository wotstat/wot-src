import { r } from "../../chunks/rolldown-runtime.js";
import {
  Nn as s,
  St as e,
  _n as t,
  _t as o,
  ln as i,
  qt as l,
  xn as a,
  yt as n,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ import { t as m } from "../../chunks/extended_tooltip_decorator.js";
var [d, p] = e()(
    ({ observableModel: r }) => ({ ...r.primitives(["timeLeft", "rerollInterval"]) }),
    i,
  ),
  c = r(l(), 1),
  u = o(function () {
    const { model: r } = p(),
      e = s.resolve("strings"),
      [o] = t(a(r.rerollInterval.get()), ["h"]);
    return (0, c.jsx)(m, {
      header: e.readOrEmpty("user_missions.tooltip.daily_reroll.header"),
      description: e.readOrEmpty("user_missions.tooltip.daily_reroll.description"),
      descriptionParams: { time: o },
      timerTimeLeft: r.timeLeft.get(),
    });
  });
n((0, c.jsx)(d, { children: (0, c.jsx)(u, {}) }));
