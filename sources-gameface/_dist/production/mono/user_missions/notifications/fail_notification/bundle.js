import { r as s } from "../../chunks/rolldown-runtime.js";
import {
  Dn as e,
  H as a,
  Jt as l,
  L as i,
  St as n,
  U as o,
  V as c,
  at as t,
  dt as r,
  it as p,
  un as m,
  ut as d,
  vt as _,
  yt as g,
} from "../../chunks/lib.js";
import "../../chunks/_wg-global-styles.js";
/* empty css                 */ var [h, u] = n()(
    ({ observableModel: s }) => ({ root: s.object() }),
    ({ externalModel: s }) => ({ openChallenge: s.createCallbackNoArgs("onClick") }),
  ),
  b = "App_image_95a6abe1",
  j = "App_32d4293d",
  x = "App_base__popup_a2438b5f",
  f = "App_wrapper_ffdbb6e9",
  A = "App_description_1dcdd2b2",
  N = "App_title_8c05c489",
  k = "App_button_111c82e",
  v = "App_close_654073f5",
  C = s(l(), 1),
  y = R.strings.user_missions.hub.challenge_missions.notification.fail,
  w = _(function () {
    const { model: s, controls: l } = u(),
      { challengeName: n, isPopUp: r } = s.root.get();
    return (0, C.jsxs)(i, {
      className: e(j, r && x),
      children: [
        (0, C.jsxs)("div", {
          className: f,
          children: [
            (0, C.jsx)("div", {
              className: b,
              style: {
                backgroundImage: `url(${R.images.gui.maps.icons.userMissions.hub.challenge.fail_challenge()})`,
              },
            }),
            (0, C.jsx)("div", {
              className: A,
              children: (0, C.jsx)(d, {
                params: { challenge: n },
                text: y.title(),
                className: N,
                upgradeLegacy: !0,
              }),
            }),
            (0, C.jsx)(c, {
              className: k,
              size: a.small,
              onClick: l.openChallenge,
              theme: o.primary,
              children: y.button(),
            }),
          ],
        }),
        r && (0, C.jsx)(p, { size: t.small, onClose: m, className: v }),
      ],
    });
  });
g((0, C.jsx)(h, { children: (0, C.jsx)(r, { children: (0, C.jsx)(w, {}) }) }));
