import { r as e } from "../chunks/rolldown-runtime.js";
import {
  Ar as t,
  Br as a,
  C as s,
  Cn as r,
  Cr as n,
  Dn as o,
  Er as c,
  Et as d,
  Hn as l,
  In as i,
  Jt as _,
  K as b,
  Lr as u,
  Or as m,
  Pr as p,
  Qn as f,
  Qr as g,
  Rn as C,
  Sr as w,
  Tn as h,
  Tt as v,
  Xn as y,
  Y as x,
  Yn as k,
  Yt as j,
  Zt as N,
  _n as I,
  ci as T,
  cr as B,
  ct as S,
  dr as E,
  dt as O,
  en as A,
  fn as G,
  ft as $,
  gn as W,
  gr as z,
  pi as M,
  pn as L,
  qt as D,
  sr as U,
  st as P,
  ti as q,
  tn as F,
  ui as H,
  ut as Y,
  vt as Q,
  w as J,
  wt as K,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { h as X } from "../chunks/vendor.js";
import { n as Z, t as V } from "../chunks/filename.js";
var ee = e(H()),
  te = "state_limited",
  ae = "state_received",
  se = M.resolve("strings"),
  re = M.resolve("images");
function ne(e) {
  const t = e.match(/(?:_(?:t|tier))?(\d+)\b/);
  if (t && void 0 !== t[1]) return t && t[1] ? parseInt(t[1], 10) : null;
}
var oe = (function (e) {
  return (
    (e.None = "none"),
    (e.Trophy = "trophy"),
    (e.Deluxe = "deluxe"),
    (e.Modernized = "modernized_device"),
    (e.BattleBooster = "battleBooster"),
    e
  );
})({});
function ce(e) {
  return e.includes("delux")
    ? "deluxe"
    : e.includes("modernized")
      ? "modernized_device"
      : e.includes("trophy")
        ? "trophy"
        : e.toLowerCase().endsWith("battleBooster".toLowerCase())
          ? "battleBooster"
          : "none";
}
function de(e, t) {
  return t && "none" !== t ? t : e;
}
var le = (e, t = x.Small, a) => {
    if ("modernized_device" === a) {
      const a = ne(e);
      if (a) return re.readOrEmpty(`quests.bonuses.${t}.modernized_devices_t${a}_gift`, "silent");
    }
    return re.readOrEmpty(`quests.bonuses.${t}.${de(e, a)}_gift`, "silent");
  },
  ie = (e, t) => {
    const a = e.match(/^offer:([^:]+):/);
    return a
      ? void 0 === a[1]
        ? ""
        : se.readOrEmpty(`selectable_reward.tabs.items.${a[1]}`, "silent")
      : se.readOrEmpty(`selectable_reward.tabs.items.${de(e, t)}`, "silent");
  },
  _e = (e) => {
    const t = e.split("_")[1],
      a = t && se.readOrEmpty(`blueprints.nations.${t}`, "silent"),
      s = se.readOrEmpty(`artefacts.${e}.name`, "silent");
    return (
      a ||
      (s && "string" == typeof s ? q(s) : (console.error("title for reward is not provided"), null))
    );
  };
function be(e, t) {
  if ("modernized_device" === t) {
    const t = ne(e);
    if (t)
      return re.readOrEmpty(
        `selectableReward.reward.optDeviceType.modernized_devices_t${t}`,
        "silent",
      );
  }
  return re.readOrEmpty(`selectableReward.reward.optDeviceType.${t}`, "silent");
}
var ue = (e, t = "s180x135", a = "R.images.gui.maps.icons.selectableReward.reward") =>
  `${a}.${t}.${e}`;
var me = (function (e) {
    return ((e.None = "none"), (e.Accepting = "accepting"), e);
  })({}),
  [pe, fe] = I()(
    ({ observableModel: e }) => {
      const s = {
          root: e.object(),
          tabs: e.array("tabs"),
          rewards: e.array("rewards"),
          animationState: z.box("none"),
        },
        r = W(
          (e) => {
            const t = p(s.tabs.get(), e);
            return { ...t, optDeviceType: ce(t.type) };
          },
          { equals: a },
        ),
        n = W(
          (e) => {
            const t = p(s.rewards.get(), e);
            return { ...t, optDeviceType: ce(t.type) };
          },
          { equals: a },
        ),
        o = W(() => t(s.tabs.get(), (e, t) => e + t.limit, 0));
      return { ...s, computes: { tabByIndex: r, rewardByIndex: n, rewardsToClaimTotal: o } };
    },
    ({ externalModel: e, model: t }) => {
      const a = E((e) => t.animationState.set(e));
      return {
        close: e.createCallbackNoArgs("onCloseClick"),
        submit: e.createCallbackNoArgs("onOkClick"),
        reduceReward: e.createCallback((e) => ({ type: e }), "onRewardReduce"),
        addReward: e.createCallback((e) => ({ type: e }), "onRewardAdd"),
        openTab: e.createCallback((e) => ({ type: e }), "onTabClick"),
        setAnimationState: a,
      };
    },
  ),
  ge = {
    base: "Category_a031eac",
    title: "Category_title_372b86f3",
    base__completed: "Category_base__completed_b894c2f0",
    imageContainer: "Category_imageContainer_4669b2b4",
    image: "Category_image_16708176",
    base__accepting: "Category_base__accepting_b894c2f0",
    blink: "Category_blink_b894c2f0",
    check: "Category_check_d9fca567",
    counter: "Category_counter_53ffc003",
    fadeInWithScale: "Category_fadeInWithScale_b894c2f0",
    slideUp: "Category_slideUp_b894c2f0",
    scale: "Category_scale_b894c2f0",
    rotate: "Category_rotate_b894c2f0",
    windowIn: "Category_windowIn_b894c2f0",
    fadeOut: "Category_fadeOut_b894c2f0",
    fadeIn: "Category_fadeIn_b894c2f0",
  },
  Ce = y(),
  we = M.resolve("strings"),
  he = M.resolve("views").read((e) =>
    e.common.tooltip_window.backport_tooltip_content.BackportTooltipContent("resId"),
  ),
  ve = X(({ index: e, className: t, classNames: a }) => {
    const {
        breakpoint: { weight: s },
      } = k(),
      { model: r, controls: n } = fe(),
      o = r.animationState.get(),
      { optDeviceType: c, count: d, limit: l, type: i } = r.computes.tabByIndex(e),
      _ = d === l,
      u = r.root.get().selectedTab === i,
      m = we.readOrEmpty(`selectable_reward.tabs.items.${c}`, "silent"),
      p = s >= f.medium.weight ? x.Big : x.Small,
      C = h((0, ee.useMemo)(() => ({ contentId: he, args: { type: i } }), [i]));
    return (0, Ce.jsxs)("div", {
      className: T(ge.base, _ && ge.base__completed, !u && d && ge[`base__${o}`], t),
      onClick: () => {
        (g.sound("bp_click"), n.openTab(i));
      },
      onMouseEnter: () => g.sound("bp_highlight"),
      children: [
        (0, Ce.jsxs)("div", {
          ...C,
          className: ge.imageContainer,
          children: [
            (0, Ce.jsx)("div", {
              className: ge.image,
              style: { backgroundImage: `url(${le(i, p, c)})` },
            }),
            (0, Ce.jsx)("div", { className: ge.check }),
          ],
        }),
        (0, Ce.jsx)("div", {
          className: ge.counter,
          children: b(we.readOrEmpty("selectable_reward.tabs.counter"), { count: d, limit: l }),
        }),
        (0, Ce.jsx)("div", {
          className: T(ge.title, a?.title),
          children: (0, Ce.jsx)(A, { text: ie(i, c), params: { equipmentType: m } }),
        }),
      ],
    });
  });
var ye = {
    base: "SelectButton_696eeaa5",
    base__plus: "SelectButton_base__plus_caa30688",
    base__disabled: "SelectButton_base__disabled_953b567",
    base__minus: "SelectButton_base__minus_2b97334c",
    fadeInWithScale: "SelectButton_fadeInWithScale_41cc3cb2",
    slideUp: "SelectButton_slideUp_41cc3cb2",
    blink: "SelectButton_blink_41cc3cb2",
    scale: "SelectButton_scale_41cc3cb2",
    rotate: "SelectButton_rotate_41cc3cb2",
    windowIn: "SelectButton_windowIn_41cc3cb2",
    fadeOut: "SelectButton_fadeOut_41cc3cb2",
    fadeIn: "SelectButton_fadeIn_41cc3cb2",
  },
  xe = (function (e) {
    return ((e.Plus = "plus"), (e.Minus = "minus"), e);
  })({}),
  ke = ({ type: e = "plus", isEnabled: t = !0, onClick: a }) =>
    (0, Ce.jsx)("div", {
      className: T(ye.base, ye[`base__${e}`], !t && ye.base__disabled),
      onClick: (e) => {
        (e.stopPropagation(), t && a(e));
      },
    }),
  je = {
    base: "Reward_aafd9d9f",
    reward: "Reward_d159ded4",
    image: "Reward_image_cdd2db9f",
    base__stateReceived: "Reward_base__stateReceived_21f091ec",
    base__stateLimited: "Reward_base__stateLimited_21f091ec",
    base__selected: "Reward_base__selected_21f091ec",
    base__accepting: "Reward_base__accepting_21f091ec",
    blink: "Reward_blink_21f091ec",
    optDeviceType: "Reward_optDeviceType_c9161298",
    packSize: "Reward_packSize_89374a40",
    label: "Reward_label_d9eb8f07",
    storage: "Reward_storage_5970894c",
    storage__hidden: "Reward_storage__hidden_4483c3c4",
    storageIcon: "Reward_storageIcon_3aa10d5a",
    selectControls: "Reward_selectControls_91575dd3",
    countText: "Reward_countText_a516c1a0",
    select: "Reward_select_98cf6062",
    state: "Reward_state_f012fad1",
    stateText: "Reward_stateText_3f71ade9",
    fadeInWithScale: "Reward_fadeInWithScale_21f091ec",
    slideUp: "Reward_slideUp_21f091ec",
    scale: "Reward_scale_21f091ec",
    rotate: "Reward_rotate_21f091ec",
    windowIn: "Reward_windowIn_21f091ec",
    fadeOut: "Reward_fadeOut_21f091ec",
    fadeIn: "Reward_fadeIn_21f091ec",
  },
  Ne = M.resolve("strings"),
  Ie = M.resolve("views").read((e) =>
    e.common.tooltip_window.backport_tooltip_content.BackportTooltipContent("resId"),
  ),
  Re = X(({ index: e, className: t }) => {
    const { model: a, controls: s } = fe(),
      n = a.animationState.get(),
      {
        type: o,
        count: c,
        state: d,
        storageCount: l,
        packSize: i,
        optDeviceType: _,
      } = a.computes.rewardByIndex(e),
      { addReward: u, reduceReward: m } = s,
      p = "state_normal" === d,
      f = d === te,
      C = d === ae,
      w = c > 0 && !C,
      v = w || p,
      y = n === me.Accepting && w,
      x = r(
        (0, ee.useMemo)(
          () =>
            f && 0 === c
              ? {
                  header: Ne.readOrEmpty("selectable_reward.reward.tooltip.state_limited.header"),
                  body: Ne.readOrEmpty("selectable_reward.reward.tooltip.state_limited.body"),
                }
              : { isEnabled: !1 },
          [f, c],
        ),
      ),
      k = h((0, ee.useMemo)(() => ({ contentId: Ie, args: { type: o } }), [o]));
    return (0, Ce.jsxs)("div", {
      className: T(
        je.base,
        t,
        w && je.base__selected,
        y && je.base__accepting,
        je[`base__${((j = d), j.replace(/_\w/g, (e) => e[1]?.toUpperCase() ?? e))}`],
      ),
      onClick: () => {
        p ? (g.sound("bp_click"), u(o)) : (f || C) && g.sound("bp_click_limit");
      },
      onMouseEnter: () => g.sound("bp_highlight"),
      children: [
        (0, Ce.jsxs)("div", {
          className: T(je.storage, l <= 0 && je.storage__hidden),
          children: [(0, Ce.jsx)("div", { className: je.storageIcon }), l],
        }),
        (0, Ce.jsxs)("div", {
          ...k,
          className: je.reward,
          children: [
            (0, Ce.jsx)("div", {
              className: je.image,
              style: { backgroundImage: `url(${ue(o)})` },
            }),
            _ !== oe.None &&
              (0, Ce.jsx)("div", {
                className: je.optDeviceType,
                style: { backgroundImage: `url(${be(o, _)})` },
              }),
            i > 1 &&
              (0, Ce.jsx)("div", {
                className: je.packSize,
                children: b(Ne.readOrEmpty("selectable_reward.reward.packSizeCount"), {
                  packSize: i,
                }),
              }),
          ],
        }),
        (0, Ce.jsx)("div", { className: je.label, children: _e(o) }),
        v
          ? (0, Ce.jsxs)("div", {
              className: je.selectControls,
              children: [
                (0, Ce.jsx)("span", { className: je.countText, children: c }),
                (0, Ce.jsxs)("div", {
                  className: je.select,
                  children: [
                    (0, Ce.jsx)(ke, {
                      type: xe.Minus,
                      isEnabled: w,
                      onClick: () => {
                        (g.sound("bp_click_minus"), m(o));
                      },
                    }),
                    (0, Ce.jsx)(ke, {
                      type: xe.Plus,
                      isEnabled: p,
                      onClick: () => {
                        p && (g.sound("bp_click_plus"), u(o));
                      },
                    }),
                  ],
                }),
              ],
            })
          : (f || C) &&
            (0, Ce.jsx)("div", {
              ...(f ? x : {}),
              className: je.state,
              children: (0, Ce.jsx)("div", {
                className: je.stateText,
                children: Ne.readOrEmpty(`selectable_reward.reward.${d}`),
              }),
            }),
      ],
    });
    var j;
  }),
  Te = {
    base: "ContentGrid_37546c98",
    scrollAreaContent: "ContentGrid_scrollAreaContent_d60bdc1",
    scrollAreaContent__centered: "ContentGrid_scrollAreaContent__centered_56ff9561",
    scrollArea: "ContentGrid_scrollArea_4b1babd8",
    cardsGrid: "ContentGrid_cardsGrid_3142d80",
    mask: "ContentGrid_mask_569ab401",
    mask__top: "ContentGrid_mask__top_a118e885",
    mask__bottom: "ContentGrid_mask__bottom_1cf7186f",
    mask__both: "ContentGrid_mask__both_b371be52",
    scrollBar: "ContentGrid_scrollBar_cc7e0d82",
    rewardCard: "ContentGrid_rewardCard_d9ece749",
    cardContent: "ContentGrid_cardContent_99c00bf7",
    statusWrapper: "ContentGrid_statusWrapper_7a9a6db7",
    statusWrapper__done: "ContentGrid_statusWrapper__done_bb2f9462",
    statusWrapper__alert: "ContentGrid_statusWrapper__alert_bb2f9462",
    icon: "ContentGrid_icon_ec9e371",
    fadeInWithScale: "ContentGrid_fadeInWithScale_e365c19f",
    slideUp: "ContentGrid_slideUp_e365c19f",
    blink: "ContentGrid_blink_e365c19f",
    scale: "ContentGrid_scale_e365c19f",
    rotate: "ContentGrid_rotate_e365c19f",
    windowIn: "ContentGrid_windowIn_e365c19f",
    fadeOut: "ContentGrid_fadeOut_e365c19f",
    fadeIn: "ContentGrid_fadeIn_e365c19f",
  },
  Be = X(({ className: e, onScrollableChange: t }) => {
    const { model: a } = fe(),
      { selectedTab: r } = a.root.get(),
      n = a.rewards.get(),
      o = a.tabs.get(),
      c = w(o, (e) => e.type === r),
      d = c.count >= c.limit,
      { api: l } = $(),
      [i, _] = Q(l),
      [b, u] = (0, ee.useState)(!1),
      p = (0, ee.useRef)(t);
    return (
      (p.current = t),
      (0, ee.useEffect)(() => {
        const e = () => {
          const [, e] = l.getBounds(),
            t = e > 0;
          u((e) => (e !== t ? t : e));
        };
        return (l.recalculateContent(), e(), l.events.on("recalculateContent", e));
      }, [n.length, l, r]),
      (0, ee.useEffect)(() => {
        p.current?.(b);
      }, [b]),
      (0, Ce.jsxs)("div", {
        className: T(Te.base, e),
        children: [
          (0, Ce.jsx)("div", {
            className: T(Te.mask, Te[`mask__${Y(i, _)}`]),
            children: (0, Ce.jsx)(S, {
              classNames: {
                content: T(Te.scrollAreaContent, !b && Te.scrollAreaContent__centered),
              },
              children: (0, Ce.jsx)("div", {
                className: Te.scrollArea,
                children: (0, Ce.jsx)(s, {
                  border: "contour",
                  enabled: !0,
                  className: Te.cardsGrid,
                  children: m(n, (e, t) => {
                    const { count: a, state: s, type: r } = e,
                      { disabled: n, statusType: o } = (function (e, t, a) {
                        const s = e === te,
                          r = e === ae,
                          n = 0 === t;
                        return {
                          disabled: n && (s || r || a),
                          statusType: r ? "done" : s && n ? "alert" : void 0,
                        };
                      })(s, a, d);
                    return (0, Ce.jsx)(
                      J,
                      {
                        selected: a > 0,
                        disabled: n,
                        status: o,
                        className: Te.rewardCard,
                        classNames: {
                          mainContainerContent: Te.cardContent,
                          status: {
                            wrapper: T(Te.statusWrapper, Te[`statusWrapper__${o}`]),
                            icon: Te.icon,
                          },
                        },
                        soundTarget: "reward-selection:card",
                        children: (0, Ce.jsx)(Re, { index: t }),
                      },
                      r,
                    );
                  }),
                }),
              }),
            }),
          }),
          (0, Ce.jsx)(O, { classNames: { base: Te.scrollBar } }),
        ],
      })
    );
  }),
  Se = "Footer_775b7239",
  Ee = "Footer_buttons_877c593c",
  Oe = M.resolve("strings"),
  Ae = X(({ buttonsSize: e, classNames: t }) => {
    const { model: a, controls: s } = fe(),
      { totalRewardCount: n } = a.root.get(),
      c = n > 0,
      {
        breakpoint: { weight: l },
      } = k(),
      i = e ?? ((e) => (e > f.small.weight ? v.medium : v.small))(l),
      _ = o(),
      b = r(
        (0, ee.useMemo)(
          () => ({ disabled: c, body: Oe.readOrEmpty("selectable_reward.tooltips.footer.body") }),
          [c],
        ),
      );
    return (0, Ce.jsx)("div", {
      className: Se,
      children: (0, Ce.jsx)("div", {
        ...b,
        className: Ee,
        children: (0, Ce.jsx)(K, {
          size: i,
          theme: d.primary,
          disabled: !c,
          className: t?.button,
          onClick: () => {
            (s.setAnimationState(me.Accepting), _.run(s.submit, 600));
          },
          children: Oe.readOrEmpty("selectable_reward.footer.okBtn.label"),
        }),
      }),
    });
  }),
  Ge = {
    base: "Content_563e7cb8",
    base__accepting: "Content_base__accepting_cb7209e5",
    wrapper: "Content_wrapper_8961ad17",
    fadeIn: "Content_fadeIn_da09528a",
    wrapper__shown: "Content_wrapper__shown_9936ffdd",
    heading: "Content_heading_d9a7d80b",
    slideUp: "Content_slideUp_da09528a",
    title: "Content_title_f7727432",
    subTitle: "Content_subTitle_9c09656d",
    tabs: "Content_tabs_2049c8a6",
    tabBase: "Content_tabBase_da4d47fc",
    tabBackground: "Content_tabBackground_d4f2412",
    tabBackground__active: "Content_tabBackground__active_2055b5b",
    tabBackground__hover: "Content_tabBackground__hover_b301ca04",
    tabBorderImage: "Content_tabBorderImage_c9d862a4",
    tabBorderImage__active: "Content_tabBorderImage__active_81864d24",
    tabBorderImage__hover: "Content_tabBorderImage__hover_a26dd782",
    tabContent: "Content_tabContent_c4bf3aa",
    contentTab: "Content_contentTab_d65f5b89",
    contentTab__shown: "Content_contentTab__shown_9936ffdd",
    footer: "Content_footer_eaf6c6e0",
    bottomLip: "Content_bottomLip_f6b13712",
    fadeInWithScale: "Content_fadeInWithScale_da09528a",
    blink: "Content_blink_da09528a",
    scale: "Content_scale_da09528a",
    rotate: "Content_rotate_da09528a",
    windowIn: "Content_windowIn_da09528a",
    fadeOut: "Content_fadeOut_da09528a",
  },
  $e = X(({ title: e, subTitle: t, classNames: a, buttonsSize: s }) => {
    const r = (0, ee.useRef)(!1),
      [o, d] = (0, ee.useState)(!1),
      [l, i] = (0, ee.useState)(null),
      [b, p] = (0, ee.useState)(!1),
      { model: f, controls: g } = fe(),
      w = f.tabs.get(),
      { selectedTab: h } = f.root.get(),
      v = f.animationState.get(),
      y = n(w, (e) => e.type === h) ?? -1;
    return (
      (0, ee.useEffect)(() => {
        if (!o)
          return U(() => {
            d(!0);
          }, 300);
      }, [o]),
      (0, ee.useEffect)(() => {
        const e = (e) => {
          (e.code !== u.ARROW_LEFT && e.code !== u.ARROW_RIGHT) || (r.current = !1);
        };
        return (window.addEventListener("keyup", e), () => window.removeEventListener("keyup", e));
      }, []),
      C(u.ARROW_LEFT, () => {
        if (r.current) return;
        if (((r.current = !0), y <= 0)) return;
        const e = c(w, y - 1);
        g.openTab(e.type);
      }),
      C(u.ARROW_RIGHT, () => {
        if (r.current) return;
        if (((r.current = !0), y < 0 || y === w.length - 1)) return;
        const e = c(w, y + 1);
        g.openTab(e.type);
      }),
      (0, Ce.jsxs)("div", {
        className: T(Ge.base, Ge[`base__${v}`]),
        children: [
          (0, Ce.jsxs)(D, {
            size: _.large,
            theme: j.custom,
            active: h,
            children: [
              (0, Ce.jsxs)("div", {
                className: T(Ge.wrapper, o && Ge.wrapper__shown),
                children: [
                  (0, Ce.jsxs)("div", {
                    className: T(Ge.heading, a?.heading),
                    children: [
                      (0, Ce.jsx)("div", { className: T(Ge.title, a?.title), children: e }),
                      (0, Ce.jsx)("div", { className: T(Ge.subTitle, a?.subTitle), children: t }),
                    ],
                  }),
                  (0, Ce.jsx)("div", {
                    className: Ge.tabs,
                    children: m(w, (e, t) => {
                      const s = h === e.type,
                        r = l === e.type && !s,
                        n = {
                          base: Ge.tabBase,
                          background: T(
                            Ge.tabBackground,
                            s && Ge.tabBackground__active,
                            r && Ge.tabBackground__hover,
                          ),
                          borderImage: T(
                            Ge.tabBorderImage,
                            s && Ge.tabBorderImage__active,
                            r && Ge.tabBorderImage__hover,
                          ),
                          content: Ge.tabContent,
                        };
                      return (0, Ce.jsx)(
                        D.Tab,
                        {
                          tabId: e.type,
                          classNames: n,
                          onMouseEnter: () => i(e.type),
                          onMouseLeave: () => i(null),
                          onClick: () => g.openTab(e.type),
                          children: (0, Ce.jsx)(ve, {
                            index: t,
                            className: a?.category,
                            classNames: { title: a?.categoryTitle },
                          }),
                        },
                        e.type,
                      );
                    }),
                  }),
                ],
              }),
              (0, Ce.jsx)(D.Content, {
                children: () =>
                  (0, Ce.jsx)("div", {
                    className: T(Ge.contentTab, o && Ge.contentTab__shown),
                    children: (0, Ce.jsx)(P, {
                      children: (0, Ce.jsx)(Be, { onScrollableChange: p }),
                    }),
                  }),
              }),
            ],
          }),
          (0, Ce.jsxs)("div", {
            className: T(Ge.footer, a?.footer),
            children: [
              b && (0, Ce.jsx)("div", { className: Ge.bottomLip }),
              (0, Ce.jsx)(Ae, { buttonsSize: s, classNames: a?.footerClassNames }),
            ],
          }),
        ],
      })
    );
  }),
  We = "Error_9f7ff239",
  ze = "Error_title_881f33d",
  Me = "Error_description_9cc31237",
  Le = "Error_footer_2ba80f61",
  De = "Error_button_1befe7e6",
  Ue = M.resolve("strings"),
  Pe = X(() => {
    const { controls: e } = fe();
    return (0, Ce.jsxs)("div", {
      className: We,
      children: [
        (0, Ce.jsx)("div", {
          className: ze,
          children: Ue.readOrEmpty("selectable_reward.error.title"),
        }),
        (0, Ce.jsx)("div", {
          className: Me,
          children: Ue.readOrEmpty("selectable_reward.error.description"),
        }),
        (0, Ce.jsx)("div", {
          className: Le,
          children: (0, Ce.jsx)(K, {
            className: De,
            theme: d.primary,
            size: v.medium,
            onClick: e.close,
            children: Ue.readOrEmpty("selectable_reward.error.button"),
          }),
        }),
      ],
    });
  }),
  qe = "RewardSelection_496b50e",
  Fe = X(({ title: e, subTitle: t, classNames: a, buttonsSize: s }) => {
    const { model: r } = fe(),
      n = r.tabs.get();
    return (0, Ce.jsx)("div", {
      className: qe,
      children:
        n.length > 0
          ? (0, Ce.jsx)($e, { title: e, subTitle: t, classNames: a, buttonsSize: s })
          : (0, Ce.jsx)(Pe, {}),
    });
  }),
  He = ({ title: e = "", subTitle: t = "", modelProviderContext: a }) =>
    (0, Ce.jsx)(pe, {
      options: { context: a },
      children: (0, Ce.jsx)(Fe, { title: e, subTitle: t }),
    }),
  [Ye, Qe] = I()(
    ({ observableModel: e }) => ({ root: e.object() }),
    ({ externalModel: e }) => ({
      close: e.createCallbackNoArgs("selectableRewardModel.onCloseClick"),
    }),
  ),
  Je = "App_285de3af",
  Ke = "App_background_189ce663",
  Xe = "App_backgroundBlur_b6c090aa",
  Ze = "App_shadow_b56b33f2",
  Ve = "App_content_54c70e4",
  et = "App_close_fbc86043",
  tt = R.strings.battle_pass.rewardChoice,
  at = X(() => {
    const { model: e, controls: t } = Qe(),
      { chapterID: a, level: s } = e.root.get(),
      r = Boolean(s),
      [n, o] = (0, ee.useState)(!1);
    (l(t.close),
      i(t.close),
      (0, ee.useEffect)(
        () =>
          B(() => {
            o(!0);
          }),
        [],
      ));
    const c = (0, ee.useMemo)(
      () =>
        ((e, t) =>
          t
            ? {
                backgroundImage: `url(${Z(R.images.gui.maps.icons.battlePass.backgrounds.chapter_general, e)})`,
              }
            : V())(a, r),
      [a, r],
    );
    return (0, Ce.jsxs)("div", {
      className: Je,
      children: [
        (0, Ce.jsx)("div", {
          className: Ke,
          style: c,
          children: (0, Ce.jsx)("div", { className: Xe }),
        }),
        (0, Ce.jsx)("div", { className: Ze }),
        n &&
          (0, Ce.jsxs)("div", {
            className: Ve,
            children: [
              (0, Ce.jsx)(N, { className: et, onClose: t.close }),
              (0, Ce.jsx)(He, {
                modelProviderContext: "model.selectableRewardModel",
                title: tt.title(),
              }),
            ],
          }),
      ],
    });
  });
G(
  new L()
    .add(F)
    .add(Ye)
    .render((0, Ce.jsx)(at, {})),
);
