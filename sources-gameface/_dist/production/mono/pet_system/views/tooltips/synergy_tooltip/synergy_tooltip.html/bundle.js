import { s, j as e } from "../../../../chunks/vendor.js";
import { i as r, t as a, r as i, af as o, ag as t, k as c } from "../../../../chunks/lib.js";
/* empty css                       */ const [l, d] = r()(
    ({ observableModel: s }) => ({ root: s.object() }),
    a,
  ),
  n = "App_28e29989",
  p = "App_header_5ad7c3ec",
  m = "App_icon_45384927",
  j = "App_progress_790cf5a6",
  h = "App_title_2eabf3c8",
  _ = "App_content_d43d99eb",
  x = i.resolve("strings"),
  v = s(function () {
    const { model: s } = d(),
      { progress: r } = s.root.get(),
      a = 100 === r;
    return e.jsx(o, {
      children: e.jsx(o.Decorator, {
        children: e.jsxs("div", {
          className: n,
          children: [
            e.jsxs("div", {
              className: p,
              children: [
                e.jsx("div", { className: m }),
                e.jsxs("div", {
                  className: j,
                  children: [
                    e.jsx("div", {
                      className: h,
                      children: x.readOrEmpty("pet_system.synergyTooltip.title"),
                    }),
                    e.jsx(t, { value: r, size: "small", maxValue: 100 }),
                  ],
                }),
              ],
            }),
            e.jsx("div", {
              className: _,
              children: x.readOrEmpty(
                "pet_system.synergyTooltip.description." + (a ? "done" : "inProgress"),
              ),
            }),
          ],
        }),
      }),
    });
  });
c(e.jsx(l, { children: e.jsx(v, {}) }), { withMedia: !1 });
