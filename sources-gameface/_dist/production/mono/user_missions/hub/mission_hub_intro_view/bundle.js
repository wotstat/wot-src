import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  H as e,
  Jt as i,
  Rt as n,
  St as o,
  U as t,
  V as r,
  dt as a,
  vt as l,
  yt as c,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
var [d, m] = o()(
    ({ observableModel: s }) => ({
      ...s.primitives(["header", "description", "buttonText", "icon"]),
    }),
    ({ externalModel: s }) => ({ onClose: s.createCallbackNoArgs("onClose") }),
  ),
  u = "MissionHubIntroView_23a12109",
  b = "MissionHubIntroView_content_61444cea",
  h = "MissionHubIntroView_image_c296ca82",
  j = "MissionHubIntroView_info_938a77f3",
  x = "MissionHubIntroView_title_d8509827",
  _ = "MissionHubIntroView_description_f111e687",
  v = "MissionHubIntroView_divider_c63a837",
  g = s(i(), 1),
  p = l(() => {
    n();
    const { model: s, controls: i } = m();
    return (0, g.jsx)("div", {
      className: u,
      children: (0, g.jsxs)("div", {
        className: b,
        children: [
          (0, g.jsx)("div", {
            className: h,
            style: { background: `url(${s.icon.get()}) no-repeat center` },
          }),
          (0, g.jsxs)("div", {
            className: j,
            children: [
              (0, g.jsx)("div", { className: x, children: s.header.get() }),
              (0, g.jsx)("div", { className: _, children: s.description.get() }),
              (0, g.jsx)("div", { className: v }),
              (0, g.jsx)(r, {
                size: e.small,
                theme: t.primary,
                onClick: i.onClose,
                children: s.buttonText.get(),
              }),
            ],
          }),
        ],
      }),
    });
  });
c((0, g.jsx)(a, { children: (0, g.jsx)(d, { children: (0, g.jsx)(p, {}) }) }));
