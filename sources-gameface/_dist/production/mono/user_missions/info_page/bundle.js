import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Dn as s,
  Jt as a,
  K as t,
  Lt as n,
  On as r,
  Pn as o,
  Sn as i,
  St as l,
  Y as c,
  ct as d,
  dt as m,
  ft as _,
  it as p,
  lt as u,
  ot as f,
  q as h,
  st as x,
  vn as b,
  vt as j,
  yt as I,
} from "../chunks/lib.js";
import "../chunks/_wg-global-styles.js";
var v = e(r(), 1),
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
  P = e(a(), 1),
  N = (e, s) => (s > 0 ? (e > 0 ? "hrs_mins" : "mins") : "hrs"),
  $ = v.memo(function ({
    titlePath: e,
    descriptionPath: a,
    iconPath: t,
    type: n,
    reversed: r,
    rerollInterval: o = 0,
  }) {
    const [l, c] = b(i(o), ["h", "m"]);
    return (0, P.jsxs)("div", {
      className: s(g.base, g[`base__${n}`], r && g.base__reversed),
      children: [
        (0, P.jsxs)("div", {
          className: g.textBlock,
          children: [
            (0, P.jsx)(u, { path: e, className: g.title }),
            (0, P.jsx)(u, {
              path: a,
              split: !0,
              params: {
                time: (0, P.jsx)(u, {
                  path: `user_missions.common.duration.${N(Number(l), Number(c))}`,
                  params: { hours: l, minutes: c },
                }),
              },
              className: g.description,
            }),
          ],
        }),
        (0, P.jsx)("div", {
          className: g.iconWrapper,
          children: (0, P.jsx)(d, { path: t, className: g.icon }),
        }),
      ],
    });
  }),
  k = "standard",
  y = "weekly",
  w = "main",
  B = "additional",
  S = [k, "premium", y],
  W = ["conditions", "bonus", "reward", "reroll"];
function C({ src: e }) {
  const s = x(e);
  if ("failure" === s.status || "loading" === s.status) return null;
  const a = s.result.component;
  return f(a)
    ? (0, P.jsx)(a, {})
    : (console.error(`Plugin result is not a React component. Source: ${e}`), null);
}
var [M, A] = l()(
    ({ observableModel: e }) => e.object(),
    ({ externalModel: e }) => ({ close: e.createCallbackNoArgs("onClose") }),
  ),
  O = "InfoPage_48433e5a",
  q = "InfoPage_closeButton_23a55aae",
  D = "InfoPage_wrapper_f38244dc",
  E = "InfoPage_content_4cbf7ee4",
  F = "InfoPage_verticalBar_a70fa964",
  J = "InfoPage_header_47fea8de",
  K = "InfoPage_separator_86a318ea",
  L = o.resolve("strings"),
  R = (e, s) => `user_missions.info_page.${e}.${s}.title`,
  Y = (e, s) => `user_missions.info_page.${e}.${s}.description`,
  z = (e) => `userMissions.info_page.${e}`,
  G = j(function () {
    const { model: e, controls: s } = A(),
      { isWeeklySectionAvailable: a, rerollInterval: r, standardBlockPlugin: o } = e.get();
    return (
      n(s.close),
      (0, P.jsxs)("div", {
        className: O,
        children: [
          (0, P.jsx)(p, { className: q, onClose: s.close }),
          (0, P.jsxs)(t, {
            children: [
              (0, P.jsxs)(h, {
                classNames: { wrapper: D, content: E },
                children: [
                  (0, P.jsx)("div", {
                    className: J,
                    children: L.readOrEmpty("user_missions.info_page.header"),
                  }),
                  S.map((e, s) =>
                    a || e !== y
                      ? o && e === k
                        ? (0, P.jsx)(
                            v.Fragment,
                            { children: (0, P.jsx)(C, { src: o }) },
                            `index_${s}`,
                          )
                        : (0, P.jsx)(
                            $,
                            {
                              type: w,
                              reversed: s % 2 != 0,
                              titlePath: R(w, e),
                              descriptionPath: Y(w, e),
                              iconPath: z(e),
                            },
                            `index_${s}`,
                          )
                      : null,
                  ),
                  (0, P.jsx)("div", { className: K }),
                  W.map((e, s) =>
                    (0, P.jsx)(
                      $,
                      {
                        type: B,
                        reversed: !0,
                        titlePath: R(B, e),
                        descriptionPath: Y(B, e),
                        iconPath: z(e),
                        rerollInterval: r,
                      },
                      `index_${s}`,
                    ),
                  ),
                ],
              }),
              (0, P.jsx)(c, { classNames: { base: F } }),
            ],
          }),
        ],
      })
    );
  });
(_(), I((0, P.jsx)(m, { children: (0, P.jsx)(M, { children: (0, P.jsx)(G, {}) }) })));
