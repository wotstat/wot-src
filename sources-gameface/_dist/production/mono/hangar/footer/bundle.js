const __vite__mapDeps = (
  i,
  m = __vite__mapDeps,
  d = m.f || (m.f = ["../chunks/lib.css", "../chunks/widget2.css"]),
) => i.map((i) => d[i]);
import { r as e } from "../chunks/rolldown-runtime.js";
import {
  $i as t,
  Bi as a,
  Br as o,
  Hr as n,
  In as s,
  Kn as r,
  Mi as i,
  Mn as l,
  Mr as c,
  Nn as d,
  Nr as u,
  Or as m,
  Pi as _,
  Qn as h,
  Ri as f,
  Rn as y,
  Sa as b,
  Ta as p,
  Xn as g,
  Yn as v,
  Zn as x,
  ai as w,
  ci as C,
  cr as B,
  dr as N,
  ei as j,
  eo as M,
  fi as R,
  ga as k,
  gn as S,
  hi as P,
  hn as E,
  hr as I,
  ir as O,
  ji as z,
  jn as W,
  kr as A,
  li as L,
  lr as V,
  mr as D,
  nr as F,
  pa as $,
  pr as G,
  qr as H,
  ro as T,
  to as U,
  ui as q,
  uo as Q,
  ur as K,
  wa as X,
  xr as Y,
  yr as Z,
  zn as J,
} from "../chunks/lib.js";
import "../chunks/global.js";
import { t as ee } from "../chunks/divider.js";
var [te, ae] = I("ChatsProvider")(
    ({ observableModel: e }) => {
      const t = { chats: e.dict("messages") },
        a = G.shallow(() =>
          Array.from(
            t.chats.values().sort((e, t) => {
              const { order: a, prebattle: o } = e.get(),
                { order: n, prebattle: s } = t.get();
              return o !== s ? (o ? -1 : 1) : a - n;
            }),
          ),
        );
      return { ...t, computes: { sortedChats: a } };
    },
    ({ externalModel: e }) => ({
      openChat: e.createCallback((e, t) => ({ sessionID: e, ...t }), "onViewMessageAction"),
      deleteChat: e.createCallback((e) => ({ sessionID: e }), "onDeleteMessageAction"),
      updateWindowAnchor: e.createCallback((e) => e, "onWindowAnchorPositionUpdated"),
      openChannelsWindow: e.createCallback((e) => e, "onChatsAction"),
    }),
  ),
  [oe, ne] = I("ContactsListModel")(
    ({ observableModel: e }) => ({ ...e.primitives(["contactsCount"]) }),
    k,
  ),
  [se, re] = I()(
    ({ observableModel: e }) => ({ ...e.primitives(["oldStyle"]) }),
    ({ externalModel: e }) => ({ openGameMenu: e.createCallbackNoArgs("onOpenGameMenu") }),
  ),
  [ie, le] = I()(
    ({ observableModel: e }) => ({
      ...e.primitives({
        newNotificationsCount: "newNotificationsCount",
        hasImportantNotification: "importantNotificationPresent",
      }),
    }),
    k,
  ),
  [ce, de] = I("ReferralProgramProvider")(
    ({ observableModel: e }) => ({
      ...e.primitives(["firstIndication", "enabled", "bubbleCount"]),
    }),
    ({ externalModel: e }) => ({ openReferralProgram: e.createCallbackNoArgs("onClick") }),
  ),
  [ue, me] = I("ServerInfoProvider")(
    ({ observableModel: e }) => ({ ...e.primitives(["serverName", "status", "colorBlind"]) }),
    k,
  ),
  [_e, he] = I("SessionStatisticProvider")(
    ({ observableModel: e }) => ({
      ...e.primitives(["battleCount", "enabled", "sessionStatsEnabled", "winback"]),
    }),
    k,
  ),
  [fe, ye] = I("VehicleCompareProvider")(
    ({ observableModel: e }) => {
      const o = {
          ...e.primitives({ isEnabled: "enabled" }),
          vehicles: e.arrayClone("vehicles"),
          compareButtonDOMRect: a.box({ left: 0, width: 0 }, { deep: !1 }),
        },
        n = D(() => t(o.vehicles.get())),
        s = D(() => o.vehicles.get().length);
      return { ...o, computes: { getLastVehicle: n, getVehiclesCount: s } };
    },
    ({ model: e }) => ({
      setCompareButtonDOMRect: f((t) => {
        e.compareButtonDOMRect.set(t);
      }),
    }),
  ),
  be = e(T(), 1),
  pe = {
    frames: {
      commanderPlayer_ready: { h: 64, w: 64, x: 0, y: 0 },
      commander_ready: { h: 64, w: 64, x: 64, y: 0 },
      member_ready: { h: 64, w: 64, x: 0, y: 64 },
      notification_button: { h: 64, w: 64, x: 64, y: 64 },
      player_ready: { h: 64, w: 64, x: 0, y: 128 },
      referral_program: { h: 64, w: 64, x: 64, y: 128 },
    },
    meta: { size: { h: 192, w: 128 } },
  },
  ge = {
    frames: {
      commanderPlayer_ready: { h: 48, w: 48, x: 0, y: 0 },
      commander_ready: { h: 48, w: 48, x: 48, y: 0 },
      member_ready: { h: 48, w: 48, x: 0, y: 48 },
      notification_button: { h: 48, w: 48, x: 48, y: 48 },
      player_ready: { h: 48, w: 48, x: 0, y: 96 },
      referral_program: { h: 48, w: 48, x: 48, y: 96 },
    },
    meta: { size: { h: 144, w: 96 } },
  },
  ve = {
    frames: {
      commanderPlayer_ready: { h: 128, w: 128, x: 0, y: 0 },
      commander_ready: { h: 128, w: 128, x: 128, y: 0 },
      member_ready: { h: 128, w: 128, x: 0, y: 128 },
      notification_button: { h: 128, w: 128, x: 128, y: 128 },
      player_ready: { h: 128, w: 128, x: 0, y: 256 },
      referral_program: { h: 128, w: 128, x: 128, y: 256 },
    },
    meta: { size: { h: 384, w: 256 } },
  },
  xe = {
    frames: {
      chat: { h: 32, w: 32, x: 0, y: 0 },
      commanderPlayer_inBattle: { h: 32, w: 32, x: 32, y: 0 },
      commanderPlayer_notReady: { h: 32, w: 32, x: 64, y: 0 },
      commander_inBattle: { h: 32, w: 32, x: 96, y: 0 },
      commander_notReady: { h: 32, w: 32, x: 0, y: 32 },
      comparison: { h: 32, w: 32, x: 32, y: 32 },
      contacts: { h: 32, w: 32, x: 64, y: 32 },
      creation: { h: 32, w: 32, x: 96, y: 32 },
      creation_disabled: { h: 32, w: 32, x: 0, y: 64 },
      empty_member: { h: 32, w: 32, x: 32, y: 64 },
      game_menu_button: { h: 32, w: 32, x: 64, y: 64 },
      member_inBattle: { h: 32, w: 32, x: 96, y: 64 },
      member_notReady: { h: 32, w: 32, x: 0, y: 96 },
      notification_button: { h: 32, w: 32, x: 32, y: 96 },
      player_inBattle: { h: 32, w: 32, x: 0, y: 128 },
      player_notReady: { h: 32, w: 32, x: 64, y: 96 },
      referral_program: { h: 32, w: 32, x: 32, y: 128 },
      search: { h: 32, w: 32, x: 96, y: 96 },
      session_stats: { h: 32, w: 32, x: 64, y: 128 },
      session_stats_disabled: { h: 32, w: 32, x: 96, y: 128 },
    },
    meta: { size: { h: 160, w: 128 } },
  },
  we = {
    frames: {
      chat: { h: 24, w: 24, x: 0, y: 0 },
      commanderPlayer_inBattle: { h: 24, w: 24, x: 24, y: 0 },
      commanderPlayer_notReady: { h: 24, w: 24, x: 48, y: 0 },
      commander_inBattle: { h: 24, w: 24, x: 72, y: 0 },
      commander_notReady: { h: 24, w: 24, x: 96, y: 0 },
      comparison: { h: 24, w: 24, x: 0, y: 24 },
      contacts: { h: 24, w: 24, x: 24, y: 24 },
      creation: { h: 24, w: 24, x: 48, y: 24 },
      creation_disabled: { h: 24, w: 24, x: 72, y: 24 },
      empty_member: { h: 24, w: 24, x: 96, y: 24 },
      game_menu_button: { h: 24, w: 24, x: 0, y: 48 },
      member_inBattle: { h: 24, w: 24, x: 24, y: 48 },
      member_notReady: { h: 24, w: 24, x: 0, y: 72 },
      notification_button: { h: 24, w: 24, x: 48, y: 48 },
      player_inBattle: { h: 24, w: 24, x: 24, y: 72 },
      player_notReady: { h: 24, w: 24, x: 72, y: 48 },
      referral_program: { h: 24, w: 24, x: 48, y: 72 },
      search: { h: 24, w: 24, x: 96, y: 48 },
      session_stats: { h: 24, w: 24, x: 72, y: 72 },
      session_stats_disabled: { h: 24, w: 24, x: 96, y: 72 },
    },
    meta: { size: { h: 96, w: 120 } },
  },
  Ce = {
    frames: {
      chat: { h: 64, w: 64, x: 0, y: 0 },
      commanderPlayer_inBattle: { h: 64, w: 64, x: 64, y: 0 },
      commanderPlayer_notReady: { h: 64, w: 64, x: 128, y: 0 },
      commander_inBattle: { h: 64, w: 64, x: 192, y: 0 },
      commander_notReady: { h: 64, w: 64, x: 0, y: 64 },
      comparison: { h: 64, w: 64, x: 64, y: 64 },
      contacts: { h: 64, w: 64, x: 128, y: 64 },
      creation: { h: 64, w: 64, x: 192, y: 64 },
      creation_disabled: { h: 64, w: 64, x: 0, y: 128 },
      empty_member: { h: 64, w: 64, x: 64, y: 128 },
      game_menu_button: { h: 64, w: 64, x: 128, y: 128 },
      member_inBattle: { h: 64, w: 64, x: 192, y: 128 },
      member_notReady: { h: 64, w: 64, x: 0, y: 192 },
      notification_button: { h: 64, w: 64, x: 64, y: 192 },
      player_inBattle: { h: 64, w: 64, x: 0, y: 256 },
      player_notReady: { h: 64, w: 64, x: 128, y: 192 },
      referral_program: { h: 64, w: 64, x: 64, y: 256 },
      search: { h: 64, w: 64, x: 192, y: 192 },
      session_stats: { h: 64, w: 64, x: 128, y: 256 },
      session_stats_disabled: { h: 64, w: 64, x: 192, y: 256 },
    },
    meta: { size: { h: 320, w: 256 } },
  },
  Be = { small: "small", medium: "medium", upscale: "upscale" };
function Ne(e) {
  return (
    "string" == typeof e &&
    (e in xe.frames ||
      e in we.frames ||
      e in Ce.frames ||
      e in ge.frames ||
      e in pe.frames ||
      e in ve.frames)
  );
}
function je(e, t, a = !1) {
  return e === Be.upscale
    ? a
      ? { config: ve, path: "header_footer.footer_highlighted_upscale", icon: t }
      : { config: Ce, path: "header_footer.footer_upscale", icon: t }
    : e === Be.medium
      ? a
        ? { config: pe, path: "header_footer.footer_highlighted_large", icon: t }
        : { config: xe, path: "header_footer.footer_large", icon: t }
      : a
        ? { config: ge, path: "header_footer.footer_highlighted_small", icon: t }
        : { config: we, path: "header_footer.footer_small", icon: t };
}
function Me(e, t) {
  const a = b("px");
  return { x: X(e + a.x - 8), y: X(t + a.y - 8 - 356), width: 424, height: 356 };
}
var Re = "maskLeft",
  ke = "maskRight",
  Se = "maskBoth",
  Pe = "none";
function Ee(e, t, a) {
  const o = t.left - e.left + a,
    n = 0.04 * e.width;
  return (
    (s = o - n),
    (r = o - e.width + t.width + n),
    (i = a),
    Math.abs(s - i) < Math.abs(r - i) ? s : r
  );
  var s, r, i;
}
var Ie = "ChatButton_58c17ddd",
  Oe = "ChatButton_base__glow_e84e99cd",
  ze = "ChatButton_overlay_d0e16554",
  We = "ChatButton_base__unreadMessages_1daa9390",
  Ae = "ChatButton_content_1735f2eb",
  Le = "ChatButton_name_a3b5f0d7",
  Ve = "ChatButton_closeIcon_7b57d2d1",
  De = e(P(), 1),
  Fe = /^#.*?:/,
  $e = Q.resolve("strings");
function Ge(e) {
  return e.match(Fe) ? $e.readOrEmpty(e.slice(1).replace(/[:/]/g, ".")) : e;
}
var He = B(
    (0, be.forwardRef)(function (
      {
        id: e,
        name: t,
        tooltipId: a,
        opened: o,
        systemChat: n,
        hasUnreadMessages: r,
        className: i,
        onClick: l,
        onClose: c,
      },
      d,
    ) {
      const u = m({ header: a ? `${a}/header` : void 0, body: a ? `${a}/body` : t }),
        _ = Z(
          "channelList",
          (0, be.useMemo)(() => ({ clientID: e, canClose: !n }), [e, n]),
        );
      return (0, De.jsxs)(s, {
        ref: d,
        ...u,
        ..._,
        theme: J.secondary,
        size: y.small,
        onClick: function (t) {
          const { left: a, top: o } = t.currentTarget.getBoundingClientRect();
          (u.onClick(), l(e, Me(a, o)));
        },
        className: U(Ie, (o || r) && Oe, r && We, i),
        classNames: { overlay: ze, content: Ae },
        autoAlignContent: !1,
        children: [
          (0, De.jsx)("div", { className: Le, children: Ge(t) }),
          !n &&
            (0, De.jsx)("div", {
              className: Ve,
              onClick: function (t) {
                (t.stopPropagation(), c(e));
              },
            }),
        ],
      });
    }),
  ),
  Te = {
    base: "ScrollControlButtons_bd2f5f8c",
    content: "ScrollControlButtons_content_4ec4a98f",
    content__maskLeft: "ScrollControlButtons_content__maskLeft_41708133",
    content__maskRight: "ScrollControlButtons_content__maskRight_d3dadb5b",
    content__maskBoth: "ScrollControlButtons_content__maskBoth_b1d09564",
    arrowButton: "ScrollControlButtons_arrowButton_dd11fcee",
    arrowButton__left: "ScrollControlButtons_arrowButton__left_e553b5a0",
    arrowButton__right: "ScrollControlButtons_arrowButton__right_22c9e28b",
    arrowButton__disabled: "ScrollControlButtons_arrowButton__disabled_e38b51c",
  };
function Ue({ itemWidth: e, api: t, children: a }) {
  const o = (0, be.useRef)(null),
    [n, r] = (0, be.useState)(!1),
    [i, l] = g(t),
    { disabled: c, animationScroll: d, applyScroll: u } = t;
  function m(t) {
    function a() {
      u(d.scrollPosition.get() + t * e);
    }
    n || (a(), (o.current = window.setInterval(a, 100)), r(!0));
  }
  function _() {
    (null !== o.current && (clearInterval(o.current), (o.current = null)), r(!1));
  }
  return (0, De.jsxs)("div", {
    className: Te.base,
    children: [
      !c &&
        (0, De.jsx)(s, {
          theme: J.secondary,
          size: y.small,
          autoAlignContent: !1,
          onMouseDown: () => m(-1),
          onMouseUp: _,
          onMouseLeave: _,
          disabled: i,
          className: U(Te.arrowButton, Te.arrowButton__left, i && Te.arrowButton__disabled),
        }),
      (0, De.jsx)("div", {
        className: U(
          Te.content,
          Te[`content__${((h = i), (f = l), h || f ? (f ? (h ? Pe : Re) : ke) : Se)}`],
        ),
        children: a,
      }),
      !c &&
        (0, De.jsx)(s, {
          theme: J.secondary,
          size: y.small,
          autoAlignContent: !1,
          onMouseDown: () => m(1),
          onMouseUp: _,
          onMouseLeave: _,
          disabled: l,
          className: U(Te.arrowButton, Te.arrowButton__right, l && Te.arrowButton__disabled),
        }),
    ],
  });
  var h, f;
}
var qe = "ChatCarousel_545467f0",
  Qe = "ChatCarousel_scrollWrapper_578773a",
  Ke = "ChatCarousel_scrollContent_61109c3c",
  Xe = "ChatCarousel_button_8bb458f8",
  Ye = "ChatCarousel_button__firstItem_e66db7f4",
  Ze = "ChatCarousel_divider_312a4ca4",
  Je = B(function ({ className: e }) {
    const { api: t } = x(),
      { model: a, controls: o } = ae(),
      n = a.computes.sortedChats(),
      s = C(n),
      [r, i] = (0, be.useState)(-1),
      [l, c] = (0, be.useState)(!1),
      d = (0, be.useRef)(null),
      m = (0, be.useRef)(null);
    ((0, be.useLayoutEffect)(() => {
      const e = t.getContainerSize(),
        a = t.getWrapperSize();
      if (e && a) {
        if ((e < a && t.applyScroll(0), m.current)) {
          const a = m.current - e;
          if (0 !== a) {
            const e = t.animationScroll.scrollPosition.get();
            t.applyScroll(e - a);
          }
        }
        m.current = e;
      }
    }, [n.length, t]),
      (0, be.useEffect)(() => {
        const e = () => {
          const e = t.getContainerSize(),
            a = t.getWrapperSize();
          e && a ? t.setDisabled(a > e) : t.setDisabled(!0);
        };
        return (
          e(),
          new $().add(t.events.on("resizeHandled", e)).add(t.events.on("recalculateContent", e))
            .dispose
        );
      }, [t, n.length]),
      (0, be.useEffect)(() => {
        function e() {
          const e = t.contentRef.current?.getBoundingClientRect();
          e && o.updateWindowAnchor(Me(e.right, e.top));
        }
        return new $()
          .add(t.events.on("resizeHandled", e))
          .add(t.events.on("recalculateContent", e)).dispose;
      }, [t, o]),
      (0, be.useEffect)(() => {
        if (s && n.length > s.length) {
          const e = n.findIndex((e) => !s.includes(e));
          -1 !== e && (i(e), c(!0));
        }
      }, [n, s, t]));
    const _ = (0, be.useRef)(0);
    (H(() => {
      if (-1 !== r && d.current && t.wrapperRef.current && l) {
        const e = t.animationScroll.scrollPosition.get(),
          a = d.current.getBoundingClientRect(),
          o = t.wrapperRef.current.getBoundingClientRect();
        ((a.left >= o.left && a.right <= o.right) ||
          (_.current = window.setTimeout(() => t.applyScroll(Ee(o, a, e)), 100)),
          c(!1));
      }
    }, [r, t, l]),
      j(() => clearTimeout(_.current)));
    const h = u(92, []);
    return (0, De.jsxs)(De.Fragment, {
      children: [
        n.length > 0 && (0, De.jsx)(ee, { className: Ze }),
        (0, De.jsx)("div", {
          className: U(qe, e),
          children: (0, De.jsx)(Ue, {
            api: t,
            itemWidth: h,
            children: (0, De.jsx)(v, {
              classNames: { wrapper: Qe, content: Ke },
              children: n.map((e, t) => {
                const { id: a, name: n, selected: s, viewed: i, system: l, tooltipId: c } = e.get();
                return (0, De.jsx)(
                  He,
                  {
                    ref: t === r ? d : null,
                    id: a,
                    name: n,
                    opened: s,
                    hasUnreadMessages: !i,
                    systemChat: l,
                    tooltipId: c,
                    onClick: o.openChat,
                    onClose: o.deleteChat,
                    className: U(Xe, 0 === t && Ye),
                  },
                  n,
                );
              }),
            }),
          }),
        }),
      ],
    });
  });
function et(e) {
  return (0, De.jsx)(r, { children: (0, De.jsx)(Je, { ...e }) });
}
var tt = "ChatChannels_c801bb1d",
  at = "ChatChannels_icon_a3ff928f";
var ot = B(function ({ className: e }) {
    const { controls: t } = ae(),
      a = Y(),
      o = Q.resolve("strings"),
      n = R(L({ value: Be.small }, { medium: { value: Be.medium } }).value, q),
      s = m({
        header: o.readOrEmpty("tooltips.loby_messenger.channels_button.header"),
        body: o.readOrEmpty("tooltips.loby_messenger.channels_button.body"),
      });
    return (0, De.jsx)("div", {
      ...s,
      onClick: function (e) {
        const { left: o, top: n } = e.currentTarget.getBoundingClientRect();
        (a.play("click", { target: "ChannelsButton", original: e }),
          t.openChannelsWindow(
            (function (e, t) {
              const a = b("px");
              return { x: X(e + a.x - 8), y: X(t + a.y - 8 - 347), width: 269, height: 347 };
            })(o, n),
          ),
          s.onClick());
      },
      onMouseEnter: function (e) {
        (a.play("mouse-enter", { target: "ChannelsButton", original: e }), s.onMouseEnter(e));
      },
      className: U(tt, e),
      children: (0, De.jsx)(O, { ...je(n, "chat"), className: at }),
    });
  }),
  nt = "Contacts_51abbb46",
  st = "Contacts_icon_a516b2cd",
  rt = "Contacts_friendsOnlineCount_20e5b06c",
  it = B(function () {
    const e = Q.resolve("intl"),
      t = Q.resolve("strings"),
      { model: a } = ne(),
      o = a.contactsCount.get(),
      n = R(L({ value: Be.small }, { medium: { value: Be.medium } }).value, q),
      s = m({
        header: t.readOrEmpty("tooltips.loby_messenger.contacts_button.header"),
        body: t.readOrEmpty("tooltips.loby_messenger.contacts_button.body"),
      }),
      r = c("ContactsPopover"),
      i = Y();
    return (0, De.jsxs)("div", {
      ...r,
      ...s,
      className: nt,
      onClick: function (e) {
        (i.play("click", { target: "ContactsButton", original: e }), r?.onClick(e), s?.onClick());
      },
      onMouseEnter: function (e) {
        (i.play("mouse-enter", { target: "ContactsButton", original: e }), s?.onMouseEnter(e));
      },
      "data-test-id": "contacts",
      children: [
        (0, De.jsx)(O, { ...je(n, "contacts"), className: st }),
        o > 0 && (0, De.jsx)("div", { className: rt, children: e.formatNumber("integral", o) }),
      ],
    });
  }),
  lt = (function (e) {
    return (
      (e[(e.Requested = 0)] = "Requested"),
      (e[(e.High = 1)] = "High"),
      (e[(e.Norm = 2)] = "Norm"),
      (e[(e.Low = 3)] = "Low"),
      e
    );
  })({}),
  ct = {
    base: "Ping_da5c25be",
    serverName: "Ping_serverName_74565bce",
    indicator: "Ping_indicator_42a6616c",
    indicatorBar: "Ping_indicatorBar_74c4fee6",
    indicatorBar__active: "Ping_indicatorBar__active_7a80c240",
    indicatorBar__weak: "Ping_indicatorBar__weak_8e4c0bd9",
    base__protanopia: "Ping_base__protanopia_7471c73e",
  },
  dt = "active",
  ut = "weak",
  mt = "none";
function _t(e, t) {
  return 0 === e && t === lt.High ? ut : e < t ? dt : mt;
}
var ht = B(function () {
    const { model: e } = me(),
      t = e.serverName.get(),
      a = e.status.get(),
      o = e.colorBlind.get();
    return (0, De.jsxs)("div", {
      ...A(
        "serversInfo",
        (0, be.useMemo)(() => [], []),
      ),
      className: U(ct.base, ct[`base__${o}`]),
      children: [
        (0, De.jsx)("div", { className: ct.serverName, children: t }),
        (0, De.jsx)("div", {
          className: ct.indicator,
          children: i(3, (e) =>
            (0, De.jsx)(
              "div",
              { className: U(ct.indicatorBar, ct[`indicatorBar__${_t(e, a)}`]) },
              `indicatorBar-${e}`,
            ),
          ),
        }),
      ],
    });
  }),
  ft = (0, be.lazy)(() =>
    l(() => import("../chunks/widget2.js"), __vite__mapDeps([0, 1]), import.meta.url),
  );
function yt(e) {
  const t = e.options.rootId;
  if (t)
    return (0, De.jsx)(d, {
      id: t,
      children: (0, De.jsx)(be.Suspense, { children: (0, De.jsx)(ft, { ...e }) }),
    });
  console.error("PlatoonWidget: rootId is not given");
}
var bt = "ReferralProgram_valueContainer_a1a1e336",
  pt = "ReferralProgram_value_b1636df4",
  gt = "ReferralProgram_54cc6b2f",
  vt = "ReferralProgram_icon_219cf8",
  xt = "ReferralProgram_icon__highlighted_77ea5c59",
  wt = "ReferralProgram_notifications_d09a7c8a",
  Ct = B(function ({ className: e }) {
    const t = Y(),
      a = Q.resolve("strings"),
      { model: o, controls: n } = de(),
      s = o.bubbleCount.get() > 0,
      r = o.firstIndication.get(),
      i = L({ value: F.small }, { medium: { value: F.medium } }),
      l = R(i.value, q),
      c = m({
        header: s
          ? a.readOrEmpty("tooltips.loby_messenger.referral_button.new_season.header")
          : a.readOrEmpty("tooltips.loby_messenger.referral_button.header"),
        body: s
          ? a.readOrEmpty("tooltips.loby_messenger.referral_button.new_season.body")
          : a.readOrEmpty("tooltips.loby_messenger.referral_button.body"),
      });
    return (0, De.jsxs)("div", {
      "data-test-id": "referral-program",
      className: U(gt, e),
      onClick: function (e) {
        (t.play("click", { target: "ReferralProgram", original: e }),
          n.openReferralProgram(),
          c?.onClick());
      },
      onMouseEnter: function (e) {
        (t.play("mouse-enter", { target: "ReferralProgram", original: e }), c?.onMouseEnter(e));
      },
      onMouseLeave: c?.onMouseLeave,
      children: [
        (0, De.jsx)(O, { ...je(l, "referral_program", r), className: U(vt, r && xt) }),
        (0, De.jsx)(h.Root, {
          hidden: !s,
          className: wt,
          children: (0, De.jsx)(h.Value, {
            value: o.bubbleCount.get(),
            size: i.value,
            classNames: { valueContainer: bt, value: pt },
          }),
        }),
      ],
    });
  }),
  Bt = "SessionStatistic_2cb87b7d",
  Nt = "SessionStatistic_base__enabled_aac72629",
  jt = "SessionStatistic_icon_ebed106f",
  Mt = "SessionStatistic_icon__enabled_bd94c361",
  Rt = "SessionStatistic_battleCount_488e1028",
  kt = "enabled",
  St = "disabled",
  Pt = "winback";
var Et = B(function () {
    const e = Q.resolve("intl"),
      { model: t } = he(),
      a = t.battleCount.get(),
      o = t.enabled.get(),
      n = t.sessionStatsEnabled.get(),
      { sessionStatisticState: s, iconEnabled: r } =
        ((i = o),
        t.winback.get()
          ? { sessionStatisticState: Pt, iconEnabled: !1 }
          : { sessionStatisticState: i ? kt : St, iconEnabled: i });
    var i;
    const l = R(L({ value: Be.small }, { medium: { value: Be.medium } }).value, q),
      d = Q.resolve("strings"),
      u = m({
        header: d.readOrEmpty("session_stats.tooltip.mainBtn.header"),
        body: d.readOrEmpty(`session_stats.tooltip.mainBtn.body.${s}`),
      }),
      _ = c("SessionStatsPopover"),
      h = Y();
    return (
      n &&
      (0, De.jsxs)("div", {
        ..._,
        ...u,
        className: U(Bt, r && Nt),
        onClick: function (e) {
          (r && (h.play("click", { target: "SessionStatisticButton", original: e }), _?.onClick(e)),
            u?.onClick());
        },
        onMouseEnter: function (e) {
          (r && h.play("mouse-enter", { target: "SessionStatisticButton", original: e }),
            u?.onMouseEnter(e));
        },
        children: [
          (0, De.jsx)(O, {
            ...je(l, r ? "session_stats" : "session_stats_disabled"),
            className: U(jt, r && Mt),
          }),
          a > 0 && (0, De.jsx)("div", { className: Rt, children: e.formatNumber("integral", a) }),
        ],
      })
    );
  }),
  It = "VehicleCompare_cff2d129",
  Ot = "VehicleCompare_icon_cbce43e9",
  zt = "VehicleCompare_vehicleCount_691224b7",
  Wt = B(function (e) {
    const { model: t } = ye(),
      a = t.computes.getVehiclesCount(),
      o = a > 0 && t.enabled.get();
    return (0, De.jsx)(At, { className: e.className, count: a, visible: o });
  }),
  At = B(function ({ count: e, visible: t, className: a }) {
    const { controls: o } = ye(),
      n = C(e),
      s = (0, be.useRef)(null),
      r = Q.resolve("intl"),
      i = Q.resolve("strings"),
      l = c("VehicleCompareCartPopover");
    ((0, be.useEffect)(() => {
      if (void 0 !== n) {
        if (0 === n && 1 === e && s.current) {
          const e = new MouseEvent("click", { bubbles: !0 });
          s.current.dispatchEvent(e);
        }
        n > 0 && 0 === e && l.hide();
      }
    }, [l, e, n]),
      (0, be.useEffect)(() => {
        _(() => {
          s.current && o.setCompareButtonDOMRect(s.current.getBoundingClientRect());
        });
      }));
    const d = R(L({ value: Be.small }, { medium: { value: Be.medium } }).value, q),
      u = m({ body: i.readOrEmpty("tooltips.loby_messenger.vehicle_compare_button.body") }),
      h = Y();
    if (t)
      return (0, De.jsxs)("div", {
        ...l,
        ...u,
        ref: s,
        className: U(It, a),
        onClick: function (e) {
          (h.play("click", { target: "VehicleCompareButton", original: e }),
            l?.onClick(e),
            u?.onClick());
        },
        onMouseEnter: function (e) {
          (h.play("mouse-enter", { target: "VehicleCompareButton", original: e }),
            u?.onMouseEnter(e));
        },
        children: [
          (0, De.jsx)(O, { ...je(d, "comparison"), className: Ot }),
          (0, De.jsx)("div", { className: zt, children: r.formatNumber("integral", e) }),
        ],
      });
  }),
  Lt = "Footer_valueContainer_f6f9da36",
  Vt = "Footer_value_96c42424",
  Dt = "Footer_c3a0f302",
  Ft = "Footer_section_9d3d3a12",
  $t = "Footer_button_c7203e02",
  Gt = "Footer_icon_6ff60f47",
  Ht = "Footer_icon__notification_827f4505",
  Tt = "Footer_iconImage_50c8b940",
  Ut = "Footer_notifications_d2687e3",
  qt = "Footer_divider_4ccd0230",
  Qt = "Footer_vehicleCompare_531bca52";
var Kt = B(
    (0, be.forwardRef)(function ({ className: e }, t) {
      const { model: a } = le(),
        { model: o } = de(),
        n = a.newNotificationsCount.get(),
        s = n > 0,
        { controls: r } = re(),
        i = Y(),
        l = Q.resolve("strings"),
        d = (0, be.useMemo)(() => [], []),
        u = C(n) ?? n,
        _ = L({ value: F.small }, { medium: { value: F.medium } }),
        f = R(_.value, q),
        y = A("settingsButton", d),
        b = m({
          header: l.readOrEmpty("tooltips.loby_messenger.service_button.header"),
          body: l.readOrEmpty("tooltips.loby_messenger.service_button.body"),
        }),
        p = c("notificationsList");
      const g = (0, be.useMemo)(
        () => ({
          rootId: Q.resolve("aliases").read((e) => e.lobby_footer.default.Platoon("resId")),
        }),
        [],
      );
      return (0, De.jsxs)("div", {
        ref: t,
        className: U(Dt, e),
        children: [
          (0, De.jsxs)("div", {
            className: Ft,
            children: [
              (0, De.jsx)(it, {}),
              (0, De.jsx)(ot, { className: $t }),
              o.enabled.get() && (0, De.jsx)(Ct, { className: $t }),
              (0, De.jsx)(yt, { options: g }),
            ],
          }),
          (0, De.jsx)(et, {}),
          (0, De.jsxs)("div", {
            className: Ft,
            children: [
              (0, De.jsx)(Wt, { className: Qt }),
              (0, De.jsx)(Et, {}),
              (0, De.jsx)(ee, { className: qt }),
              (0, De.jsx)(ht, {}),
              (0, De.jsx)("div", {
                ...y,
                className: Gt,
                "data-test-id": "menu",
                onClick: function (e) {
                  (i.play("click", { target: "GameMenuButton", original: e }),
                    r.openGameMenu(),
                    y?.onClick());
                },
                onMouseEnter: function (e) {
                  (i.play("mouse-enter", { target: "GameMenuButton", original: e }),
                    y?.onMouseEnter(e));
                },
                children: (0, De.jsx)(O, { ...je(f, "game_menu_button"), className: Tt }),
              }),
              (0, De.jsx)(ee, { className: qt }),
              (0, De.jsxs)("div", {
                ...p,
                ...b,
                className: U(Gt, Ht),
                "data-test-id": "notificationCenter",
                onClick: function (e) {
                  (i.play("click", { target: "GameMenuButton", original: e }),
                    p?.onClick(e),
                    b?.onClick());
                },
                onMouseEnter: function (e) {
                  (i.play("mouse-enter", { target: "GameMenuButton", original: e }),
                    b?.onMouseEnter(e));
                },
                children: [
                  (0, De.jsx)(O, { ...je(f, "notification_button", s), className: Tt }),
                  (0, De.jsx)(h.Root, {
                    hidden: n <= 0,
                    className: Ut,
                    children: (0, De.jsx)(h.Value, {
                      value: ((v = n), (x = u), 0 === v ? x : v),
                      size: _.value,
                      classNames: { valueContainer: Lt, value: Vt },
                    }),
                  }),
                ],
              }),
            ],
          }),
        ],
      });
      var v, x;
    }),
  ),
  Xt = "CompareBubble_border_741a305",
  Yt = "CompareBubble_f502af37",
  Zt = "CompareBubble_text_46c430aa",
  Jt = "CompareBubble_type_573849d2";
function ea({ tier: e, type: t, isPremium: a, longName: s, onRest: r }) {
  const [i] = n(() => ({
    from: { opacity: 0, y: 0 },
    to: async (e) => {
      (await e({ opacity: 1, y: p(20) }), await z(1e3), await e({ opacity: 0, y: p(40) }));
    },
    config: { duration: 300, easing: M.easeInQuad },
    onRest: r,
  }));
  return (0, De.jsxs)(o.div, {
    className: Yt,
    style: i,
    children: [
      (0, De.jsx)("div", { className: Xt }),
      (0, De.jsx)(W, { value: e, className: Zt }),
      (0, De.jsx)(E, { className: Jt, type: t, size: S.x24x24, premium: a }),
      (0, De.jsx)("div", { className: Zt, children: s }),
    ],
  });
}
var ta = "App_bcf56f63",
  aa = "App_bubble_ce2d4ee4",
  oa = "App_footer_8633140e",
  na = "App_footer__oldStyle_ed955e9f";
var sa = B(function () {
  const e = w(250, 0),
    { model: t } = re(),
    { model: a } = ye(),
    o = a.computes.getVehiclesCount(),
    n = a.compareButtonDOMRect.get(),
    s = C(o),
    r = (0, be.useRef)(0),
    [i, l] = (0, be.useState)(!1),
    c = o > 0 && a.enabled.get() && i,
    d = a.computes.getLastVehicle();
  return (
    (0, be.useEffect)(() => {
      e.current && (r.current = e.current.getBoundingClientRect().height + 45);
    }, [e]),
    (0, be.useEffect)(() => {
      void 0 !== s && (o < 2 || (o > s && l(!0)));
    }, [o, s]),
    (0, De.jsxs)("div", {
      className: ta,
      children: [
        c &&
          d &&
          (0, De.jsx)("div", {
            className: aa,
            style: { bottom: `${r.current}rem`, left: `${n.left + n.width / 2}rem` },
            children: (0, De.jsx)(ea, {
              ...d,
              onRest: () => {
                l(!1);
              },
            }),
          }),
        (0, De.jsx)(Kt, { ref: e, className: U(oa, t.oldStyle.get() && na) }),
      ],
    })
  );
});
K(
  new N()
    .add(V)
    .add(se)
    .addWithProps(oe, {
      options: {
        rootId: Q.resolve("aliases").read((e) => e.lobby_footer.default.ContactsList("resId")),
      },
    })
    .addWithProps(ce, {
      options: {
        rootId: Q.resolve("aliases").read((e) => e.lobby_footer.default.ReferralProgram("resId")),
      },
    })
    .addWithProps(fe, {
      options: {
        rootId: Q.resolve("aliases").read((e) => e.lobby_footer.default.VehicleCompare("resId")),
      },
    })
    .addWithProps(_e, {
      options: {
        rootId: Q.resolve("aliases").read((e) => e.lobby_footer.default.SessionStats("resId")),
      },
    })
    .addWithProps(ie, {
      options: {
        rootId: Q.resolve("aliases").read((e) =>
          e.lobby_footer.default.NotificationsCenter("resId"),
        ),
      },
    })
    .addWithProps(te, {
      options: { rootId: Q.resolve("aliases").read((e) => e.lobby_footer.default.Chats("resId")) },
    })
    .addWithProps(ue, {
      options: {
        rootId: Q.resolve("aliases").read((e) => e.lobby_footer.default.ServerInfo("resId")),
      },
    })
    .render((0, De.jsx)(sa, {})),
);
export { Be as n, je as r, Ne as t };
