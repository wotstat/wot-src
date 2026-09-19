import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  Ur as e,
  Xn as a,
  _n as t,
  bt as n,
  ci as i,
  fn as r,
  kn as c,
  n as o,
  pn as l,
  tn as d,
  ui as _,
} from "../../chunks/lib.js";
import "../../chunks/global.js";
import { h as p } from "../../chunks/vendor.js";
_();
var [j, h] = t()(({ observableModel: s }) => ({ root: s.object() }), e),
  m = "Message_2be04282",
  x = "Message_separator_8e93a926",
  b = "Message_content_892e4ad6",
  v = "Message_text_4b17d86",
  g = "Message_lightWrapper_3117043c",
  N = "Message_lightWrapper__x2_2e75acbc",
  f = "Message_light_b62af34c",
  u = "Message_points_65c3ecdb",
  M = "Message_check_3a018192",
  C = a(),
  k = R.strings.battle_pass.tooltips.notChosen,
  W = ({ points: s }) => {
    const e = c();
    return (0, C.jsxs)("div", {
      className: m,
      children: [
        (0, C.jsx)("div", { className: x }),
        (0, C.jsx)("div", {
          className: b,
          children: (0, C.jsx)("div", {
            className: v,
            children: (0, C.jsx)(n, {
              text: k.points(),
              binding: {
                points: (0, C.jsxs)("div", {
                  className: u,
                  children: [
                    (0, C.jsx)("div", {
                      className: i(g, 2 === e && N),
                      children: (0, C.jsx)("div", { className: f }),
                    }),
                    (0, C.jsx)("div", { className: M, children: s }),
                  ],
                }),
              },
            }),
          }),
        }),
        (0, C.jsx)("div", { className: x }),
      ],
    });
  },
  w = "Content_3b8aeff8",
  D = "Content_separator_9582cf97",
  P = "Content_title_53d25156",
  T = "Content_subtitle_9986b7c5",
  U = "Content_messageWrapper_563c2e09",
  X = "Content_description_bf1180f1",
  q = "Content_separatorWrapper_162c2d2f",
  y = R.strings.battle_pass.tooltips.notChosen,
  z = p(() => {
    const { model: s } = h(),
      { points: e } = s.root.get();
    return (0, C.jsxs)("div", {
      className: w,
      children: [
        (0, C.jsx)("div", { className: P, children: y.title() }),
        (0, C.jsx)("div", { className: T, children: y.subTitle() }),
        e > 0
          ? (0, C.jsx)("div", { className: U, children: (0, C.jsx)(W, { points: e }) })
          : (0, C.jsx)("div", { className: q, children: (0, C.jsx)("div", { className: D }) }),
        (0, C.jsx)("div", { className: X, children: y.description() }),
      ],
    });
  }),
  A = () => (0, C.jsx)(o, { children: (0, C.jsx)(o.Decorator, { children: (0, C.jsx)(z, {}) }) });
r(
  new l()
    .add(d)
    .addWithProps(j, {})
    .render((0, C.jsx)(A, {})),
);
