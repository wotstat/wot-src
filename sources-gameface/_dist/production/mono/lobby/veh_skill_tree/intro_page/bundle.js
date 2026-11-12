import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  Ct as e,
  Et as a,
  Jt as t,
  Ln as i,
  Lt as n,
  Pn as l,
  Pt as o,
  Rt as c,
  St as r,
  Tn as d,
  Tt as p,
  dt as m,
  ht as _,
  mt as h,
  nn as u,
  vn as b,
  zn as j,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
import { m as x } from "../../chunks/vendor.js";
var v = s(j(), 1),
  f = "Description_9a429ac6",
  y = "Description_icon_61bd7cae",
  C = "Description_title_fd356bf",
  N = "Description_9c2cbcb1",
  g = t(),
  k = ({ icon: s, title: e, description: a }) =>
    (0, g.jsxs)("div", {
      className: f,
      children: [
        (0, g.jsx)("div", { className: C, children: e }),
        (0, g.jsx)("div", { className: y, style: { backgroundImage: `url(${s})` } }),
        (0, g.jsx)("div", { className: N, children: a && l(a) }),
      ],
    }),
  [A, w] = a()(
    ({ observableModel: s }) => {
      const e = { slides: s.arrayClone("slides"), ...s.primitives(["title", "buttonLabel"]) },
        a = p.shallow((s) => {
          const a = b(e.slides.get(), s);
          return (u(void 0 !== a, `Could not find slide with index ${s}.`), a);
        });
      return { ...e, computed: { getSlideByIndex: a } };
    },
    ({ externalModel: s }) => ({ onClose: s.createCallbackNoArgs("onClose") }),
  ),
  B = "App_508c0064",
  E = "App_content_3c8fdc2c",
  S = "App_slidesWrapper_2389a8ac",
  D = "App_slide_24421c1a",
  L = "App_counter_1ccae048",
  $ = "App_arrowButton_4108196b",
  I = "App_arrowButton__left_1ff87043",
  P = "App_arrowButton__disabled_6db15a44",
  T = x(function () {
    const { model: s, controls: e } = w(),
      [a, t] = (0, v.useState)(0),
      l = s.slides.get().length;
    (c(d.ESCAPE, e.onClose), c(d.ENTER, e.onClose));
    const r = n(a, {
      key: a,
      from: { opacity: 0 },
      enter: { opacity: 1 },
      leave: { opacity: 0 },
      config: { tension: 280, friction: 60 },
    });
    return (0, g.jsxs)("div", {
      className: B,
      children: [
        (0, g.jsxs)("div", {
          className: E,
          children: [
            (0, g.jsx)(m, {
              classNames: { base: i($, I, 0 === a && P) },
              disabled: 0 === a,
              theme: _.secondary,
              onClick: () => {
                t((s) => s - 1);
              },
            }),
            (0, g.jsx)("div", {
              className: S,
              children: r((e, a) =>
                (0, g.jsxs)(o.div, {
                  className: D,
                  style: e,
                  children: [
                    (0, g.jsx)("div", { className: L, children: `${a + 1} / ${l}` }),
                    (0, g.jsx)(k, { ...s.computed.getSlideByIndex(a) }),
                  ],
                }),
              ),
            }),
            (0, g.jsx)(m, {
              classNames: { base: i($, a === l - 1 && P) },
              disabled: a === l - 1,
              theme: _.secondary,
              onClick: () => {
                t((s) => s + 1);
              },
            }),
          ],
        }),
        (0, g.jsx)(m, {
          size: h.medium,
          theme: _.primary,
          onClick: e.onClose,
          children: s.buttonLabel.get(),
        }),
      ],
    });
  });
e((0, g.jsx)(A, { children: (0, g.jsx)(r, { children: (0, g.jsx)(T, {}) }) }));
