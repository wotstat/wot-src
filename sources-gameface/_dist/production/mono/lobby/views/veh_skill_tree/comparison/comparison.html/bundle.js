import { t as e, j as s, k as a } from "../../../../chunks/vendor.js";
import { i as r, m as d, r as l, a1 as t, c, U as i } from "../../../../chunks/lib.js";
const [o, n] = r()(
    ({ observableModel: e }) => ({
      upgrades: e.transform(
        (e) => d(e, (e) => ({ state: e.state, isSelected: e.isSelected })),
        "upgrades",
      ),
    }),
    ({ externalModel: e }) => ({
      select: e.createCallback((e) => ({ upgradeState: e }), "onSelectUpgrades"),
    }),
  ),
  p = "Upgrade_d729e0ca",
  _ = "Upgrade_base__selected_ce84880a",
  m = "Upgrade_background_5842edd3",
  g = "Upgrade_icon_9713156d",
  h = "Upgrade_base__doubled_f669c22b",
  v = "Upgrade_description_88857dd8",
  u = "Upgrade_text_8b58d19c",
  b = "Upgrade_achievement_f4280c6d",
  j = l.resolve("strings"),
  x = l.resolve("images"),
  f = l.resolve("sounds"),
  k = e(function ({ state: e, isSelected: r, doubled: d }) {
    const { controls: l } = n();
    return s.jsxs("div", {
      className: a(p, r && _, d && h),
      onClick: function () {
        (f.play("play"), l.select(e));
      },
      onMouseEnter: function () {
        f.play("highlight");
      },
      children: [
        s.jsx("div", { className: m }),
        s.jsx("div", {
          className: g,
          style: { backgroundImage: `url(${x.readOrEmpty(`skillTree.comparison.${e}`)})` },
        }),
        s.jsx("div", {
          className: v,
          children: s.jsx("div", {
            className: u,
            children: j.readOrEmpty(`veh_skill_tree.comparison.${e}.title`),
          }),
        }),
        s.jsx("div", { className: b }),
      ],
    });
  }),
  y = "App_bd668828",
  N = "App_title_214d16af",
  U = "App_info_91a5ec20",
  E = "App_list_2a86fbc8",
  O = l.resolve("strings"),
  S = e(function () {
    const { model: e } = n(),
      a = e.upgrades.get(),
      r = t({
        header: O.readOrEmpty("veh_skill_tree.comparison.tooltip.header"),
        body: O.readOrEmpty("veh_skill_tree.comparison.tooltip.body"),
      });
    return s.jsxs("div", {
      className: y,
      children: [
        s.jsxs("div", {
          className: N,
          children: [
            O.readOrEmpty("veh_skill_tree.comparison.title"),
            s.jsx("div", { className: U, ...r }),
          ],
        }),
        s.jsx("div", {
          className: E,
          children: d(a, (e, r) => s.jsx(k, { ...e, doubled: a.length < 3 }, r)),
        }),
      ],
    });
  });
c(s.jsx(o, { children: s.jsx(i, { children: s.jsx(S, {}) }) }));
