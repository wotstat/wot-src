import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Dn as s,
  En as a,
  G as n,
  Lt as t,
  Nn as r,
  St as o,
  W as i,
  _n as l,
  _t as c,
  at as d,
  it as _,
  lt as m,
  nt as p,
  ot as u,
  q as f,
  qt as h,
  st as x,
  vt as b,
  xn as j,
  yt as I,
} from "../chunks/lib.js";
import "../chunks/_wg-global-styles.js";
var v = e(s(), 1),
  g = {
    base: "InfoItem_a5beac91",
    base__reversed: "InfoItem_base__reversed_36b9aa51",
    textBlock: "InfoItem_textBlock_aaa46241",
    base__additional: "InfoItem_base__additional_2d64e841",
    title: "InfoItem_title_10b9bb3b",
    description: "InfoItem_description_c2dea9a8",
    iconWrapper: "InfoItem_iconWrapper_7115ec4b",
    icon: "InfoItem_icon_9f7d5e9f",
  },
  P = e(h(), 1),
  N = (e, s) => (s > 0 ? (e > 0 ? "hrs_mins" : "mins") : "hrs"),
  $ = v.memo(function ({
    titlePath: e,
    descriptionPath: s,
    iconPath: n,
    type: t,
    reversed: r,
    rerollInterval: o = 0,
  }) {
    const [i, c] = l(j(o), ["h", "m"]);
    return (0, P.jsxs)("div", {
      className: a(g.base, g[`base__${t}`], r && g.base__reversed),
      children: [
        (0, P.jsxs)("div", {
          className: g.textBlock,
          children: [
            (0, P.jsx)(x, { path: e, className: g.title }),
            (0, P.jsx)(x, {
              path: s,
              split: !0,
              params: {
                time: (0, P.jsx)(x, {
                  path: `user_missions.common.duration.${N(Number(i), Number(c))}`,
                  params: { hours: i, minutes: c },
                }),
              },
              className: g.description,
            }),
          ],
        }),
        (0, P.jsx)("div", {
          className: g.iconWrapper,
          children: (0, P.jsx)(u, { path: n, className: g.icon }),
        }),
      ],
    });
  }),
  k = "standard",
  y = "weekly",
  w = "main",
  B = "additional",
  W = [k, "premium", y],
  C = ["conditions", "bonus", "reward", "reroll"];
function M({ src: e }) {
  const s = d(e);
  if ("failure" === s.status || "loading" === s.status) return null;
  const a = s.result.component;
  return _(a)
    ? (0, P.jsx)(a, {})
    : (console.error(`Plugin result is not a React component. Source: ${e}`), null);
}
var [S, q] = o()(
    ({ observableModel: e }) => e.object(),
    ({ externalModel: e }) => ({ close: e.createCallbackNoArgs("onClose") }),
  ),
  A = "InfoPage_48433e5a",
  E = "InfoPage_closeButton_23a55aae",
  D = "InfoPage_wrapper_f38244dc",
  F = "InfoPage_content_4cbf7ee4",
  G = "InfoPage_verticalBar_a70fa964",
  L = "InfoPage_header_47fea8de",
  O = "InfoPage_separator_86a318ea",
  R = r.resolve("strings"),
  z = (e, s) => `user_missions.info_page.${e}.${s}.title`,
  H = (e, s) => `user_missions.info_page.${e}.${s}.description`,
  J = (e) => `userMissions.info_page.${e}`,
  K = c(function () {
    const { model: e, controls: s } = q(),
      { isWeeklySectionAvailable: a, rerollInterval: r, standardBlockPlugin: o } = e.get();
    return (
      t(s.close),
      (0, P.jsxs)("div", {
        className: A,
        children: [
          (0, P.jsx)(p, { className: E, onClose: s.close }),
          (0, P.jsxs)(i, {
            children: [
              (0, P.jsxs)(n, {
                classNames: { wrapper: D, content: F },
                children: [
                  (0, P.jsx)("div", {
                    className: L,
                    children: R.readOrEmpty("user_missions.info_page.header"),
                  }),
                  W.map((e, s) =>
                    a || e !== y
                      ? o && e === k
                        ? (0, P.jsx)(
                            v.Fragment,
                            { children: (0, P.jsx)(M, { src: o }) },
                            `index_${s}`,
                          )
                        : (0, P.jsx)(
                            $,
                            {
                              type: w,
                              reversed: s % 2 != 0,
                              titlePath: z(w, e),
                              descriptionPath: H(w, e),
                              iconPath: J(e),
                            },
                            `index_${s}`,
                          )
                      : null,
                  ),
                  (0, P.jsx)("div", { className: O }),
                  C.map((e, s) =>
                    (0, P.jsx)(
                      $,
                      {
                        type: B,
                        reversed: !0,
                        titlePath: z(B, e),
                        descriptionPath: H(B, e),
                        iconPath: J(e),
                        rerollInterval: r,
                      },
                      `index_${s}`,
                    ),
                  ),
                ],
              }),
              (0, P.jsx)(f, { classNames: { base: G } }),
            ],
          }),
        ],
      })
    );
  });
(m(), I((0, P.jsx)(b, { children: (0, P.jsx)(S, { children: (0, P.jsx)(K, {}) }) })));
