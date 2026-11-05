import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  En as e,
  H as a,
  L as l,
  St as n,
  U as o,
  V as i,
  _t as c,
  ct as t,
  ln as r,
  nt as p,
  qt as m,
  rt as d,
  vt as _,
  yt as g,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ var [h, b] = n()(
    ({ observableModel: s }) => ({ root: s.object() }),
    ({ externalModel: s }) => ({ openChallenge: s.createCallbackNoArgs("onClick") }),
  ),
  u = "App_image_95a6abe1",
  j = "App_32d4293d",
  x = "App_base__popup_a2438b5f",
  f = "App_wrapper_ffdbb6e9",
  A = "App_description_1dcdd2b2",
  N = "App_title_8c05c489",
  k = "App_button_111c82e",
  v = "App_close_654073f5",
  C = s(m(), 1),
  y = R.strings.user_missions.hub.challenge_missions.notification.fail,
  w = c(function () {
    const { model: s, controls: n } = b(),
      { challengeName: c, isPopUp: m } = s.root.get();
    return (0, C.jsxs)(l, {
      className: e(j, m && x),
      children: [
        (0, C.jsxs)("div", {
          className: f,
          children: [
            (0, C.jsx)("div", {
              className: u,
              style: {
                backgroundImage: `url(${R.images.gui.maps.icons.userMissions.hub.challenge.fail_challenge()})`,
              },
            }),
            (0, C.jsx)("div", {
              className: A,
              children: (0, C.jsx)(t, {
                params: { challenge: c },
                text: y.title(),
                className: N,
                upgradeLegacy: !0,
              }),
            }),
            (0, C.jsx)(i, {
              className: k,
              size: a.small,
              onClick: n.openChallenge,
              theme: o.primary,
              children: y.button(),
            }),
          ],
        }),
        m && (0, C.jsx)(p, { size: d.small, onClose: r, className: v }),
      ],
    });
  });
g((0, C.jsx)(h, { children: (0, C.jsx)(_, { children: (0, C.jsx)(w, {}) }) }));
