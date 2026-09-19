import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Br as s,
  Et as t,
  In as a,
  Lr as n,
  Or as l,
  Qn as r,
  Qr as o,
  Rn as i,
  Tt as d,
  Xn as c,
  Yn as _,
  Zn as u,
  Zr as m,
  Zt as b,
  _n as p,
  ar as f,
  ci as h,
  fn as C,
  gn as v,
  pi as x,
  pn as j,
  ti as g,
  tn as k,
  ui as S,
  wt as N,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as w } from "../chunks/vendor.js";
var y = e(S(), 1),
  I = "Bullets_212d5391",
  E = "Bullets_bullet_ba77929c",
  B = "Bullets_bullet__active_abbe1a09",
  W = c();
function O({ count: e, current: s, className: t }) {
  return (0, W.jsx)("div", {
    className: h(I, t),
    children: f(e, (e) => (0, W.jsx)("div", { className: h(E, e + 1 === s && B) }, e)),
  });
}
var $ = {
    base: "Slider_ada98126",
    trackWrapper: "Slider_trackWrapper_5523de93",
    track: "Slider_track_58cb30a5",
    slide: "Slider_slide_d2a68aac",
    slide__active: "Slider_slide__active_b616c59f",
    fadeInWithScale: "Slider_fadeInWithScale_263edf46",
    slideUp: "Slider_slideUp_263edf46",
    blink: "Slider_blink_263edf46",
    scale: "Slider_scale_263edf46",
    rotate: "Slider_rotate_263edf46",
    windowIn: "Slider_windowIn_263edf46",
    fadeOut: "Slider_fadeOut_263edf46",
    fadeIn: "Slider_fadeIn_263edf46",
  },
  L = ({ children: e, currentSlide: s }) => {
    const t = (0, y.useRef)(null),
      { breakpoint: a } = _(),
      n = a.weight < r.medium.weight,
      l = e,
      [o, i] = (0, y.useState)(0),
      d = () => {
        if (!t.current) return;
        const e = viewEnv.getScale();
        i(t.current.offsetWidth / e);
      };
    return (
      (0, y.useLayoutEffect)(() => {
        d();
      }, []),
      (0, y.useEffect)(
        () => (
          window.addEventListener("resize", d),
          () => {
            window.removeEventListener("resize", d);
          }
        ),
        [],
      ),
      (0, W.jsx)("div", {
        className: h($.base, n && $.base__large),
        children: (0, W.jsx)("div", {
          className: $.trackWrapper,
          ref: t,
          children: (0, W.jsx)("div", {
            className: $.track,
            style: { transform: `translateX(-${o * (s - 1)}rem)` },
            children: l.map((e, t) =>
              (0, W.jsx)(
                "div",
                {
                  className: h($.slide, n && $.slide__large, t + 1 === s && $.slide__active),
                  style: { width: `${o}rem` },
                  children: e,
                },
                `slide-${t}`,
              ),
            ),
          }),
        }),
      })
    );
  },
  D = "DescriptioBlock_cd7c382c",
  M = "DescriptioBlock_icon_be43f59b",
  P = "DescriptioBlock_title_62eb5c5",
  U = "DescriptioBlock_description_2e359fe8",
  z = ({ icon: e, title: s, descr: t }) => {
    const a = (0, y.useCallback)((e) => {
      e.stopPropagation();
    }, []);
    return (0, W.jsxs)("div", {
      className: D,
      onClick: a,
      children: [
        (0, W.jsx)("div", { className: M, style: { backgroundImage: `url(${e})` } }),
        (0, W.jsx)("div", { className: P, children: s }),
        (0, W.jsx)("div", { className: U, children: t && g(t) }),
      ],
    });
  },
  T = {
    base: "Content_90bca771",
    bg: "Content_bg_3c3188a8",
    shadow: "Content_shadow_7e9b4ef",
    content: "Content_77ec8abc",
    sliderControl: "Content_sliderControl_d45c0238",
    sliderControl__prev: "Content_sliderControl__prev_964ca0e4",
    sliderControl__next: "Content_sliderControl__next_30dcc216",
    next: "Content_next_f3b98def",
    prev: "Content_prev_b66800aa",
    bottomContainer: "Content_bottomContainer_ccf84a96",
    buttonWrapper: "Content_buttonWrapper_a1158cfa",
    actionButton: "Content_actionButton_76948240",
    closeButton: "Content_closeButton_b94862e0",
    fadeInWithScale: "Content_fadeInWithScale_da09528a",
    slideUp: "Content_slideUp_da09528a",
    blink: "Content_blink_da09528a",
    scale: "Content_scale_da09528a",
    rotate: "Content_rotate_da09528a",
    windowIn: "Content_windowIn_da09528a",
    fadeOut: "Content_fadeOut_da09528a",
    fadeIn: "Content_fadeIn_da09528a",
  },
  Z = x.resolve("images"),
  A = x.resolve("strings"),
  F = ({ slides: e, onClose: s }) => {
    const [a, l] = (0, y.useState)(1),
      r = 1 === a,
      c = a === e.length,
      m = e.length <= 1,
      { breakpoint: p } = _(),
      f = p.height <= u.Small ? d.small : d.medium,
      C = Z.readOrEmpty("battlePass.backgrounds.common", "silent"),
      v = (0, y.useCallback)(
        function () {
          r || (l(a - 1), o.sound(R.sounds.play()), o.sound(R.sounds.bp_glide_01()));
        },
        [r, a],
      ),
      x = (0, y.useCallback)(
        function () {
          c || (l(a + 1), o.sound(R.sounds.play()), o.sound(R.sounds.bp_glide_01()));
        },
        [c, a],
      ),
      j = () => o.sound(R.sounds.highlight());
    return (
      i(n.ARROW_LEFT, v),
      i(n.ARROW_RIGHT, x),
      (0, W.jsxs)("div", {
        className: T.base,
        style: { backgroundImage: `url(${C})` },
        children: [
          (0, W.jsxs)(W.Fragment, {
            children: [
              (0, W.jsx)("div", { className: T.bg, style: { backgroundImage: `url(${C})` } }),
              (0, W.jsx)("div", { className: T.shadow }),
            ],
          }),
          (0, W.jsx)(b, { onClose: s, className: T.closeButton }),
          (0, W.jsxs)("div", {
            className: T.content,
            children: [
              !m &&
                (0, W.jsx)(N, {
                  theme: t.secondary,
                  onClick: v,
                  onMouseEnter: j,
                  className: h(T.sliderControl, T.sliderControl__prev),
                  disabled: r,
                  children: (0, W.jsx)("div", { className: T.prev }),
                }),
              !m &&
                (0, W.jsx)(N, {
                  theme: t.secondary,
                  onClick: x,
                  onMouseEnter: j,
                  className: h(T.sliderControl, T.sliderControl__next),
                  disabled: c,
                  children: (0, W.jsx)("div", { className: T.next }),
                }),
              (0, W.jsx)(L, {
                currentSlide: a,
                children: e.map((e, s) =>
                  (0, W.jsx)(
                    z,
                    {
                      icon: Z.readOrEmpty(`battlePass.intro.${e}`),
                      title: A.readOrEmpty(`battle_pass.intro.${e}.title`),
                      descr: A.readOrEmpty(`battle_pass.intro.${e}.text`),
                    },
                    s,
                  ),
                ),
              }),
              (0, W.jsxs)("div", {
                className: T.bottomContainer,
                children: [
                  (0, W.jsx)("div", {
                    className: T.buttonWrapper,
                    children: (0, W.jsx)(N, {
                      theme: t.primary,
                      size: f,
                      className: T.actionButton,
                      onClick: c ? s : x,
                      children: c
                        ? A.readOrEmpty("battle_pass.intro.affirmative.button")
                        : A.readOrEmpty("battle_pass.intro.next.button"),
                    }),
                  }),
                  (0, W.jsx)(O, { count: e.length, current: a, className: T.bullets }),
                ],
              }),
            ],
          }),
        ],
      })
    );
  },
  [Q, X] = p()(
    ({ observableModel: e }) => {
      const t = { root: e.object(), slides: e.array("slides") },
        a = v(() => l(t.slides.get(), (e) => e), { equals: s });
      return { ...t, computes: { getSlides: a } };
    },
    ({ externalModel: e }) => ({}),
  ),
  q = w(() => {
    const { model: e } = X(),
      s = e.computes.getSlides();
    return (a(() => m.close()), (0, W.jsx)(F, { slides: s, onClose: m.close }));
  });
C(
  new j()
    .add(k)
    .addWithProps(Q, {})
    .render((0, W.jsx)(q, {})),
);
