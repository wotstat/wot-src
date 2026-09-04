import { t as e, r as a, j as s, k as t } from "../../../../chunks/vendor.js";
import {
  i,
  r as o,
  b as r,
  k as c,
  u as n,
  o as l,
  F as p,
  c as _,
  U as m,
} from "../../../../chunks/lib.js";
const [d, u] = i()(
    ({ observableModel: e }) => ({ root: e.object() }),
    ({ externalModel: e }) => ({ close: e.createCallbackNoArgs("onClose") }),
  ),
  b = {
    root: "App_root_0",
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
  x = e(function () {
    const { model: e, controls: i } = u(),
      { name: _, title: m, rarity: d } = e.root.get(),
      [x, f] = a.useState(!0),
      h = o.resolve("intl"),
      A = o.resolve("strings"),
      j = o.resolve("videos");
    r(c.ESCAPE, i.close);
    const v = n(
        { size: "s400x300" },
        { large: { size: "s600x450" }, extraLarge: { size: "s900x675" } },
      ),
      y = a.useCallback(() => {
        (f(!1), i.close());
      }, [i]);
    return s.jsx("div", {
      className: b.base,
      children: s.jsxs("div", {
        className: b.content,
        children: [
          s.jsxs("div", {
            className: b.animationWrapper,
            children: [
              s.jsx("div", {
                className: b.icon,
                style: {
                  backgroundImage: `url('R.images.gui.maps.vehicles.attachments.${v.size}.${_}')`,
                },
              }),
              x &&
                s.jsx(l, {
                  className: b.animation,
                  src: j.readOrEmpty(`rarity.intro_${d}`),
                  autoplay: !0,
                  onEnded: y,
                }),
              s.jsx(l, {
                className: t(b.animation, x && b.animation__hidden),
                src: j.readOrEmpty(`rarity.cycle_${d}`),
                autoplay: !x,
                loop: !0,
              }),
            ],
          }),
          s.jsxs("div", {
            className: t(b.footer, b[`footer__${d}`]),
            children: [
              s.jsx("div", { className: b.title, children: h.toUpperCase(m) }),
              s.jsx(p, {
                text: A.readOrEmpty(
                  "vehicle_customization.customization.RarityRewardScreen.subtitle",
                ),
                upgradeLegacy: !0,
                params: {
                  rarity: h.toUpperCase(
                    A.readOrEmpty(`vehicle_customization.customization.rarity.${d}`),
                  ),
                },
                className: b.subTitle,
              }),
            ],
          }),
        ],
      }),
    });
  });
_(s.jsx(d, { children: s.jsx(m, { children: s.jsx(x, {}) }) }));
