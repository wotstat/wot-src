import { r as t } from "../../chunks/rolldown-runtime.js";
import {
  Et as e,
  Ir as s,
  Tt as a,
  Xn as i,
  Zt as n,
  _n as r,
  bt as o,
  fn as c,
  pn as l,
  qn as d,
  tn as h,
  ui as p,
  wt as m,
  zn as x,
} from "../../chunks/lib.js";
import "../../chunks/global.js";
import { h as b } from "../../chunks/vendor.js";
p();
var _ = "ExtraChapterDescription_b9765d9b",
  u = "ExtraChapterDescription_description_6781df64",
  j = "ExtraChapterDescription_warningIcon_be590846",
  C = "ExtraChapterDescription_highlightText_3444159b",
  g = i(),
  f = R.strings.battle_pass.chapterChoice.confirmation,
  N = () =>
    (0, g.jsx)("div", {
      className: _,
      children: (0, g.jsx)(o, {
        text: f.extraChapterDescription.text(),
        binding: {
          icon: (0, g.jsx)("span", { className: j }),
          highlightText: (0, g.jsx)("span", {
            className: C,
            children: f.extraChapterDescription.highlightText(),
          }),
        },
        classMix: u,
      }),
    }),
  [v, A] = r()(
    ({ observableModel: t }) => ({ root: t.object() }),
    ({ externalModel: t }) => ({
      confirm: t.createCallbackNoArgs("onAccept"),
      close: t.createCallbackNoArgs("onCancel"),
    }),
  ),
  k = "Container_28f8549e",
  z = "Container_buttons_4ace6ad5",
  E = "Container_closeButton_1a873580",
  w = "Container_divider_9b7ebff",
  S = R.strings.battle_pass.chapterChoice.confirmation,
  D = b(function () {
    const { model: t, controls: i } = A(),
      { prevChapter: n } = t.root.get(),
      r = d(
        { buttonSize: a.small },
        { medium: { buttonSize: a.medium }, extraLarge: { buttonSize: a.large } },
      );
    return (
      x(s.ESCAPE, i.close),
      (0, g.jsxs)("div", {
        className: k,
        children: [
          (0, g.jsx)("div", { className: w }),
          (0, g.jsxs)("div", {
            className: z,
            children: [
              (0, g.jsx)(m, {
                size: r.buttonSize,
                onClick: i.confirm,
                "data-test-id": "confirmButton",
                children: 0 === n ? S.button.submit() : S.button.switch(),
              }),
              (0, g.jsx)(m, {
                size: r.buttonSize,
                theme: e.secondary,
                onClick: i.close,
                className: E,
                "data-test-id": "cancelButton",
                children: S.button.cancel(),
              }),
            ],
          }),
        ],
      })
    );
  }),
  T = "App_3018b200",
  B = "App_title_50c7a92f",
  P = "App_subTitle_78a165db",
  y = "App_topRight_6cd3f8f6",
  M = "App_closeBtn_bc1dfeba",
  $ = R.strings.battle_pass.chapterChoice.confirmation,
  I = (t) => R.strings.battle_pass.chapter.fullName.$num(t),
  q = b(() => {
    const { model: t, controls: e } = A(),
      {
        prevChapter: s,
        nextChapter: a,
        isSwitchFromPostProgressionToExtraChapter: i,
      } = t.root.get(),
      r = 0 !== s ? "switch" : "select";
    return (0, g.jsxs)("div", {
      className: T,
      children: [
        (0, g.jsx)("div", {
          className: y,
          children: (0, g.jsx)("div", {
            className: M,
            children: (0, g.jsx)(n, { onClose: e.close }),
          }),
        }),
        (0, g.jsx)("div", {
          className: B,
          children: (0, g.jsx)(o, { text: $.title.$dyn(r), binding: { chName: I(a) } }),
        }),
        i
          ? (0, g.jsx)(N, {})
          : (0, g.jsx)("div", {
              className: P,
              children: (0, g.jsx)(o, { text: $.description.$dyn(r), binding: { chName: I(s) } }),
            }),
        (0, g.jsx)(D, {}),
      ],
    });
  });
c(
  new l()
    .add(h)
    .addWithProps(v, {})
    .render((0, g.jsx)(q, {})),
);
