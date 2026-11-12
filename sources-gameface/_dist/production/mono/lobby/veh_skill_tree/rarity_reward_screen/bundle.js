import { r as e } from "../../chunks/rolldown-runtime.js";
import {
  Ct as a,
  Et as t,
  Hn as s,
  Jt as i,
  K as o,
  Rt as r,
  St as n,
  Tn as c,
  Wt as l,
  xt as p,
  yt as m,
  zn as d,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
import { m as _ } from "../../chunks/vendor.js";
var u = e(d(), 1),
  f = e(p(), 1),
  [b, x] = t()(
    ({ observableModel: e }) => ({ root: e.object() }),
    ({ externalModel: e }) => ({ close: e.createCallbackNoArgs("onClose") }),
  ),
  h = {
    base: "App_680dbe67",
    backgroundAlpha: "App_backgroundAlpha_0",
    animationWrapper: "App_animationWrapper_9a2017cb",
    animation: "App_animation_3ff7d031",
    animation__hidden: "App_animation__hidden_8afb9008",
    icon: "App_icon_f43f6c92",
    itemEffect: "App_itemEffect_0",
    content: "App_content_ccd9c029",
    footer: "App_footer_cc11a117",
    textMask: "App_textMask_0",
    footer__epic: "App_footer__epic_b5fc3751",
    title: "App_title_167b9150",
    subTitle: "App_subTitle_dc235974",
  },
  j = i(),
  y = _(function () {
    const { model: e, controls: a } = x(),
      { name: t, title: i, rarity: n } = e.root.get(),
      [p, d] = (0, u.useState)(!0),
      _ = s.resolve("intl"),
      b = s.resolve("strings"),
      y = s.resolve("videos");
    r(c.ESCAPE, a.close);
    const A = l(
        { size: "s400x300" },
        { large: { size: "s600x450" }, extraLarge: { size: "s900x675" } },
      ),
      v = (0, u.useCallback)(() => {
        (d(!1), a.close());
      }, [a]);
    return (0, j.jsx)("div", {
      className: h.base,
      children: (0, j.jsxs)("div", {
        className: h.content,
        children: [
          (0, j.jsxs)("div", {
            className: h.animationWrapper,
            children: [
              (0, j.jsx)("div", {
                className: h.icon,
                style: {
                  backgroundImage: `url('R.images.gui.maps.vehicles.attachments.${A.size}.${t}')`,
                },
              }),
              p &&
                (0, j.jsx)(o, {
                  className: h.animation,
                  src: y.readOrEmpty(`rarity.intro_${n}`),
                  autoplay: !0,
                  onEnded: v,
                }),
              (0, j.jsx)(o, {
                className: (0, f.default)(h.animation, p && h.animation__hidden),
                src: y.readOrEmpty(`rarity.cycle_${n}`),
                autoplay: !p,
                loop: !0,
              }),
            ],
          }),
          (0, j.jsxs)("div", {
            className: (0, f.default)(h.footer, h[`footer__${n}`]),
            children: [
              (0, j.jsx)("div", { className: h.title, children: _.toUpperCase(i) }),
              (0, j.jsx)(m, {
                text: b.readOrEmpty(
                  "vehicle_customization.customization.RarityRewardScreen.subtitle",
                ),
                upgradeLegacy: !0,
                params: {
                  rarity: _.toUpperCase(
                    b.readOrEmpty(`vehicle_customization.customization.rarity.${n}`),
                  ),
                },
                className: h.subTitle,
              }),
            ],
          }),
        ],
      }),
    });
  });
a((0, j.jsx)(b, { children: (0, j.jsx)(n, { children: (0, j.jsx)(y, {}) }) }));
