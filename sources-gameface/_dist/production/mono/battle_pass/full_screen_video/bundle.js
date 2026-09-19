import { r as s } from "../chunks/rolldown-runtime.js";
import {
  Gn as e,
  In as o,
  Qr as n,
  Xn as a,
  _n as r,
  fn as t,
  kn as l,
  nn as i,
  pi as c,
  pn as d,
  sr as u,
  tn as m,
  ui as p,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as f } from "../chunks/vendor.js";
import { d as h } from "../chunks/utils.js";
var j = s(p(), 1),
  [b, v] = r()(
    ({ observableModel: s }) => ({ root: s.object() }),
    ({ externalModel: s }) => ({ close: s.createCallbackNoArgs("onClose") }),
  ),
  k = "App_fab90a23",
  g = "App_video_826e570a",
  y = a(),
  N = f(() => {
    const { model: s, controls: a } = v(),
      { videoName: r, audioName: t, isWindowAccessible: d } = s.root.get(),
      { width: m, height: p } = e(),
      f = l(),
      b = (0, j.useRef)(null),
      N = c.resolve("videos").readOrEmpty(r);
    return (
      (0, j.useEffect)(() => {
        const s = b.current;
        if (s)
          return d
            ? Boolean(s.getCurrentTime())
              ? s.play()
              : u(() => {
                  (s.play(), n.sound(t));
                }, 300)
            : s.pause();
      }, [b, d, t]),
      (0, j.useEffect)(() => {
        const s = b.current;
        engine.on("clientMinimized", (e) => {
          s && (e ? s.pause() : s.play());
        });
      }, [b]),
      o(a.close),
      (0, y.jsx)("div", {
        className: k,
        children: (0, y.jsx)(i, {
          className: g,
          src: N,
          onEnded: a.close,
          ref: b,
          style: h(m, p, f, r),
        }),
      })
    );
  });
t(
  new d()
    .add(m)
    .addWithProps(b, {})
    .render((0, y.jsx)(N, {})),
);
