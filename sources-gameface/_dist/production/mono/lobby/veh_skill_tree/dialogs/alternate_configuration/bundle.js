import { r as e } from "../../../chunks/rolldown-runtime.js";
import {
  Ct as s,
  Dt as a,
  Et as t,
  Hn as o,
  Jt as i,
  Ln as l,
  Ot as r,
  Rt as n,
  St as c,
  Tn as d,
  Tt as m,
  Wt as p,
  Y as v,
  _t as h,
  ct as _,
  dt as u,
  ht as f,
  jt as g,
  mt as j,
  nn as x,
  pt as y,
  q as N,
  t as C,
  yn as b,
  zn as k,
} from "../../../chunks/lib.js";
import "../../../chunks/_wg-global-styles.js";
import { m as E } from "../../../chunks/vendor.js";
var I = e(k(), 1),
  T = {
    base: "Card_24797002",
    card: "Card_8b5a7d32",
    content: "Card_content_e830473a",
    image: "Card_image_e613669d",
    name: "Card_name_99ab4a1d",
  },
  S = i();
function O({ type: e, iconName: s, pressed: t, onClick: i, nodeID: r }) {
  const n = o.resolve("strings"),
    c = a(),
    {
      onMouseEnter: d,
      onMouseLeave: m,
      onClick: p,
    } = g({
      contentId: R.views.lobby.veh_post_progression.tooltip.SetupTooltipView("resId"),
      args: { nodeID: r, type: e },
    });
  return (0, S.jsxs)("div", {
    className: l(T.base, t && T.base__pressed),
    onMouseEnter: d,
    onMouseLeave: m,
    onClick: () => {
      (p(), i(), c.play("click", { target: t ? "deselect" : "select" }));
    },
    children: [
      (0, S.jsx)(C, {
        className: T.card,
        selected: t,
        status: t ? "done" : void 0,
        children: (0, S.jsx)("div", {
          className: T.content,
          children: (0, S.jsx)(h, {
            className: T.image,
            path: `skillTree.tree.dialogs.alternateConfiguration.${s}`,
          }),
        }),
      }),
      (0, S.jsx)("div", {
        className: T.name,
        children: n.readOrEmpty(`veh_skill_tree.dialog.altConfiguration.${e}`),
      }),
    ],
  });
}
var A = "Footer_info_b48c491b",
  z = "Footer_separator_3f705b18",
  D = "Footer_button_197c4535",
  H = y("AlternateConfigurationFooter", "Footer_fb231f23");
function M({ onClose: e, ...s }) {
  const a = o.resolve("strings"),
    t = p({ size: j.small }, { medium: { size: j.medium } });
  return (0, S.jsxs)(H, {
    ...s,
    children: [
      (0, S.jsx)("div", {
        className: A,
        children: a.readOrEmpty("veh_skill_tree.dialog.altConfiguration.info"),
      }),
      (0, S.jsx)("div", { className: z }),
      (0, S.jsx)(u, {
        className: D,
        theme: f.primary,
        size: t.size,
        onClick: e,
        children: a.readOrEmpty("veh_skill_tree.dialog.common.accept"),
      }),
    ],
  });
}
var w = {
  vehicle: "Header_vehicle_2fc02200",
  vehicleTier: "Header_vehicleTier_135eaea3",
  vehicleName: "Header_vehicleName_135eaea3",
  title: "Header_title_1c6e5cde",
  description: "Header_description_edbe210e",
};
function F({ level: e, type: s, name: a, premium: t }) {
  const i = o.resolve("strings");
  return (0, S.jsxs)("div", {
    className: w.base,
    children: [
      (0, S.jsxs)(N, {
        className: w.vehicle,
        children: [
          (0, S.jsx)(N.Level, { className: w.vehicleTier, value: e }),
          s && (0, S.jsx)(N.Type, { type: s, size: v.x64x64, premium: t }),
          (0, S.jsx)(N.Name, {
            children: (0, S.jsx)("div", { className: w.vehicleName, children: a }),
          }),
        ],
      }),
      (0, S.jsx)("div", {
        className: w.title,
        children: i.readOrEmpty("veh_skill_tree.dialog.altConfiguration.title"),
      }),
      (0, S.jsx)("div", {
        className: w.description,
        children: i.readOrEmpty("veh_skill_tree.dialog.altConfiguration.description"),
      }),
    ],
  });
}
var [L, $] = t()(
    ({ observableModel: e }) => {
      const s = {
          vehicleInfo: e.transform(
            ({ vehicleLvl: e, vehicleType: s, vehicleName: a, isElite: t }) => ({
              level: e,
              type: s,
              name: a,
              premium: t,
            }),
            "vehicleInfo",
          ),
          loadouts: e.transform((e) => b(e, (e) => ({ ...e })), "loadouts"),
          ...e.primitives(["nodeID"]),
        },
        a = m.shallow(() => b(s.loadouts.get(), ({ isSelected: e }) => e));
      return { ...s, computeds: { loadoutStates: a } };
    },
    ({ externalModel: e }) => ({
      close: e.createCallbackNoArgs("onClose"),
      affirmate: e.createCallback((e) => ({ loadoutStates: JSON.stringify(e) }), "onAffirmate"),
    }),
  ),
  J = "App_170f5fe6",
  q = "App_cards_2833612d",
  P = "App_footer_d8aec517",
  V = E(function () {
    const { model: e, controls: s } = $();
    (n(d.ESCAPE, s.close), n(d.ENTER, () => s.affirmate(i)));
    const a = e.vehicleInfo.get(),
      t = e.loadouts.get(),
      o = e.nodeID.get(),
      [i, l] = (0, I.useState)(e.computeds.loadoutStates());
    x.log(_(a.type), `Incorrect vehicle type: ${a.type}`);
    const r = _(a.type) ? a.type : void 0;
    return (0, S.jsxs)("div", {
      className: J,
      children: [
        (0, S.jsx)(F, { ...a, type: r }),
        (0, S.jsx)("div", {
          className: q,
          children: t.map(({ type: e, iconName: s }, a) =>
            (0, S.jsx)(
              O,
              {
                type: e,
                iconName: s,
                pressed: i[a],
                nodeID: o,
                onClick: () => {
                  l((e) => e.map((e, s) => (s === a ? !e : e)));
                },
              },
              `loadout-card-${e}`,
            ),
          ),
        }),
        (0, S.jsx)(M, { className: P, onClose: () => s.affirmate(i) }),
      ],
    });
  }),
  W = r({ click: { select: "yes1", deselect: "yes" } });
s((0, S.jsx)(c, { soundsOverrides: W, children: (0, S.jsx)(L, { children: (0, S.jsx)(V, {}) }) }));
