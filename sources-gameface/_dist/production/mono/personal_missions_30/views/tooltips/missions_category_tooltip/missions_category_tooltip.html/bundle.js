import { s as e, j as s, f as n } from "../../../../chunks/vendor.js";
import {
  i as o,
  v as a,
  I as t,
  F as i,
  L as r,
  a2 as l,
  a0 as c,
  a4 as m,
  a3 as _,
  a1 as p,
  az as d,
  M as h,
  d as x,
} from "../../../../chunks/lib.js";
import { G as j } from "../../../../chunks/gradient_decorator.js";
import { M as u } from "../../../../chunks/enums.js";
/* empty css                       */ const [b, y] = o()(
    ({ observableModel: e }) => e.primitives(["category", "operationName", "minLevel", "maxLevel"]),
    a,
  ),
  v = "Header_a57509ea",
  g = "Header_content_84bb0203",
  N = "Header_category_73a14ab3",
  f = "Header_title_e89d676b",
  T = "Header_description_2cc816f6",
  k = e(function () {
    const { model: e } = y(),
      n = e.category.get();
    return s.jsxs("div", {
      className: v,
      children: [
        s.jsx(t, {
          path: `personal_missions_30.category.c_64x64.${n}`,
          width: "64rem",
          height: "64rem",
          className: N,
        }),
        s.jsxs("div", {
          className: g,
          children: [
            s.jsx(i, { className: f, path: `personal_missions_30.common.category.${n}` }),
            s.jsx(i, {
              split: !0,
              className: T,
              path: `personal_missions_30.tooltip.missionsCategory.description.${n}`,
            }),
          ],
        }),
      ],
    });
  }),
  I = "roles",
  B = "vehicleTypes",
  C = { [I]: "personal_missions_30.common.role", [B]: "menu.header.vehicleType" },
  L = {
    base: "ColumnItem_f772e009",
    base__roles: "ColumnItem_base__roles_fabefe49",
    icon: "ColumnItem_icon_876d9b1b",
    text: "ColumnItem_text_f537f721",
  };
function $({ item: e, contentType: o = "roles", className: a }) {
  return s.jsxs("div", {
    className: n(L.base, L[`base__${o}`], a),
    children: [
      s.jsx(t, { path: `personal_missions_30.common.${o}.${r(e)}`, className: L.icon }),
      s.jsx(i, { className: L.text, path: `${C[o]}.${r(e)}` }),
    ],
  });
}
const R = "assault",
  w = "breakthrough",
  S = "sniper",
  M = "support",
  P = "universal",
  F = (e) => {
    switch (e) {
      case u.ASSAULT:
      case u.SNIPER:
        return s.jsxs(s.Fragment, {
          children: [
            s.jsx($, { item: m, contentType: "vehicleTypes" }),
            s.jsx($, { item: _, contentType: "vehicleTypes" }),
            s.jsx($, { item: p, contentType: "vehicleTypes" }),
          ],
        });
      case u.SUPPORT:
        return s.jsxs(s.Fragment, {
          children: [
            s.jsx($, { item: l, contentType: "vehicleTypes" }),
            s.jsx($, { item: c, contentType: "vehicleTypes" }),
          ],
        });
      default:
        throw new Error(`unhandled categoryType ${e}`);
    }
  },
  H = (e) => {
    switch (e) {
      case u.ASSAULT:
        return s.jsxs(s.Fragment, {
          children: [s.jsx($, { item: w }), s.jsx($, { item: R }), s.jsx($, { item: P })],
        });
      case u.SNIPER:
        return s.jsxs(s.Fragment, { children: [s.jsx($, { item: S }), s.jsx($, { item: M })] });
      case u.SUPPORT:
        return null;
      default:
        throw new Error(`unhandled categoryType ${e}`);
    }
  },
  A = {
    base: "InnerBlock_4e0a1101",
    description: "InnerBlock_description_e25909eb",
    base__support: "InnerBlock_base__support_8a259d83",
    content: "InnerBlock_content_dd2985b",
    content__noRoles: "InnerBlock_content__noRoles_b0516207",
    subtitle: "InnerBlock_subtitle_c3819b5a",
    column: "InnerBlock_column_9f423fea",
    verticalLine: "InnerBlock_verticalLine_af25fb85",
  },
  E = e(function () {
    const { model: e } = y(),
      o = e.category.get(),
      a = Boolean(H(o));
    return s.jsxs("div", {
      className: n(A.base, A[`base__${o}`]),
      children: [
        s.jsx(i, {
          split: !0,
          className: A.description,
          path: `personal_missions_30.tooltip.missionsCategory.innerBlock.description.${o}`,
        }),
        a
          ? s.jsxs("div", {
              className: A.content,
              children: [
                s.jsxs("div", {
                  className: A.column,
                  children: [
                    s.jsx(i, {
                      className: A.subtitle,
                      path: "personal_missions_30.tooltip.missionsCategory.innerBlock.vehiclesTypes",
                    }),
                    F(o),
                  ],
                }),
                s.jsx("div", { className: A.verticalLine }),
                s.jsxs("div", {
                  className: A.column,
                  children: [
                    s.jsx(i, {
                      className: A.subtitle,
                      path: "personal_missions_30.tooltip.missionsCategory.innerBlock.withRoles",
                    }),
                    H(o),
                  ],
                }),
              ],
            })
          : s.jsxs("div", {
              className: n(A.content, A.content__noRoles),
              children: [
                s.jsx(i, {
                  className: A.subtitle,
                  path: "personal_missions_30.tooltip.missionsCategory.innerBlock.noRoles",
                }),
                s.jsx("div", { className: A.column, children: F(o) }),
              ],
            }),
      ],
    });
  }),
  U = "MissionsCategoryTooltip_c7151f3b",
  O = "MissionsCategoryTooltip_footer_e1c7b92d",
  z = e(function () {
    const { model: e } = y();
    return s.jsx(d, {
      className: U,
      "data-name": "MissionsCategoryTooltip",
      children: s.jsxs(d.Decorator, {
        children: [
          s.jsx(k, {}),
          s.jsx(j, { children: s.jsx(E, {}) }),
          s.jsx(i, {
            path: "personal_missions_30.tooltip.missionsCategory.footer",
            params: {
              operationName: e.operationName.get(),
              minLevel: h(e.minLevel.get()),
              maxLevel: h(e.maxLevel.get()),
            },
            split: !0,
            className: O,
          }),
        ],
      }),
    });
  });
x(s.jsx(b, { children: s.jsx(z, {}) }));
