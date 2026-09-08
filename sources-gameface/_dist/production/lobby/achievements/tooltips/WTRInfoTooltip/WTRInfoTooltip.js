(() => {
  "use strict";
  var e,
    n = {
      254: (e, n, t) => {
        var i = {};
        (t.r(i), t.d(i, { mouse: () => w, onResize: () => p }));
        var r = {};
        (t.r(r),
          t.d(r, {
            events: () => i,
            getMouseGlobalPosition: () => E,
            getSize: () => h,
            graphicsQuality: () => b,
          }));
        var o = {};
        (t.r(o), t.d(o, { getBgUrl: () => _, getTextureUrl: () => y }));
        var a = {};
        (t.r(a),
          t.d(a, {
            addModelObserver: () => C,
            addPreloadTexture: () => F,
            children: () => o,
            displayStatus: () => x,
            displayStatusIs: () => Y,
            events: () => T,
            extraSize: () => Z,
            forceTriggerMouseMove: () => K,
            freezeTextureBeforeResize: () => G,
            getBrowserTexturePath: () => k,
            getDisplayStatus: () => X,
            getScale: () => H,
            getSize: () => B,
            getViewGlobalPosition: () => D,
            isClientAccessible: () => U,
            isEventHandled: () => J,
            isFocused: () => Q,
            pxToRem: () => I,
            remToPx: () => W,
            resize: () => L,
            sendEvent: () => V,
            setAnimateWindow: () => q,
            setEventHandled: () => $,
            setInputPaddingsRem: () => M,
            setSidePaddingsRem: () => N,
            whenTutorialReady: () => ee,
          }));
        var s = t(6179),
          u = t.n(s),
          l = t(493),
          d = t.n(l),
          c = t(6483),
          v = t.n(c);
        function m(e) {
          return (n) => (
            engine.on(e, n),
            () => {
              engine.off(e, n);
            }
          );
        }
        function f(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        const p = m("clientResized"),
          g = { down: m("mousedown"), up: m("mouseup"), move: m("mousemove") };
        const w = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function n() {
            e.enabled && f(!1);
          }
          function t() {
            e.enabled && f(!0);
          }
          function i() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", n),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", n),
                  document.body.addEventListener("mouseleave", t))
              : f(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (n, t) => (
              (n[t] = (function (n) {
                return (t) => {
                  e.listeners += 1;
                  let r = !0;
                  const o = `mouse${n}`,
                    a = g[n]((e) => t([e, "outside"]));
                  function s(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(o, s),
                    i(),
                    () => {
                      r &&
                        (a(), window.removeEventListener(o, s), (e.listeners -= 1), i(), (r = !1));
                    }
                  );
                };
              })(t)),
              n
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), i());
            },
            enable() {
              ((e.enabled = !0), i());
            },
            enableOutside() {
              e.enabled && f(!0);
            },
            disableOutside() {
              e.enabled && f(!1);
            },
          });
        })();
        function h(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function E(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const b = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function y(e, n, t = 1) {
          return viewEnv.getChildTexturePath(e, n.width, n.height, t);
        }
        function _(e, n, t) {
          return `url(${y(e, n, t)})`;
        }
        const x = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          T = {
            onTextureFrozen: m("self.onTextureFrozen"),
            onTextureReady: m("self.onTextureReady"),
            onDomBuilt: m("self.onDomBuilt"),
            onLoaded: m("self.onLoaded"),
            onDisplayChanged: m("self.onShowingStatusChanged"),
            onFocusUpdated: m("self.onFocusChanged"),
            children: {
              onAdded: m("children.onAdded"),
              onLoaded: m("children.onLoaded"),
              onRemoved: m("children.onRemoved"),
              onAttached: m("children.onAttached"),
              onTextureReady: m("children.onTextureReady"),
              onRequestPosition: m("children.requestPosition"),
            },
          },
          P = ["args"];
        const S = 2,
          O = 16,
          z = 32,
          A = 64,
          j = (e, n) => {
            const t = "GFViewEventProxy";
            if (void 0 !== n) {
              const r = n.args,
                o = (function (e, n) {
                  if (null == e) return {};
                  var t,
                    i,
                    r = {},
                    o = Object.keys(e);
                  for (i = 0; i < o.length; i++) ((t = o[i]), n.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(n, P);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, o, {
                      arguments:
                        ((i = r),
                        Object.entries(i).map(([e, n]) => {
                          const t = "GFValueProxy";
                          switch (typeof n) {
                            case "number":
                              return { __Type: t, name: e, number: n };
                            case "boolean":
                              return { __Type: t, name: e, bool: n };
                            default:
                              return { __Type: t, name: e, string: n.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, o));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var i;
          },
          V = {
            close(e) {
              j("popover" === e ? S : z);
            },
            minimize() {
              j(A);
            },
            move(e) {
              j(O, { isMouseEvent: !0, on: e });
            },
          };
        function F(e) {
          viewEnv.addPreloadTexture(e);
        }
        function M(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function k(e, n, t, i = 1) {
          return viewEnv.getWebBrowserTexturePath(e, n, t, i);
        }
        function C(e, n, t) {
          return viewEnv.addDataChangedCallback(e, n, t);
        }
        function N(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function B(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function L(e, n, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, n) : viewEnv.resizeViewPx(e, n);
        }
        function D(e = "rem") {
          const n = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? n : { x: W(n.x), y: W(n.y) };
        }
        function G() {
          viewEnv.freezeTextureBeforeResize();
        }
        function H() {
          return viewEnv.getScale();
        }
        function I(e) {
          return viewEnv.pxToRem(e);
        }
        function W(e) {
          return viewEnv.remToPx(e);
        }
        function q(e, n) {
          viewEnv.setAnimateWindow(e, n);
        }
        function Q() {
          return viewEnv.isFocused();
        }
        function U() {
          return viewEnv.isClientAccessible();
        }
        function $() {
          return viewEnv.setEventHandled();
        }
        function J() {
          return viewEnv.isEventHandled();
        }
        function K() {
          viewEnv.forceTriggerMouseMove();
        }
        function X() {
          return viewEnv.getShowingStatus();
        }
        const Y = Object.keys(x).reduce(
            (e, n) => ((e[n] = () => viewEnv.getShowingStatus() === x[n]), e),
            {},
          ),
          Z = {
            set: (e, n) => {
              viewEnv.setExtraSizeRem(e, n);
            },
            get: (e, n) => {
              viewEnv.getExtraSizeRem(e, n);
            },
          },
          ee = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : T.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          ne = { view: a, client: r };
        function te() {
          const e = (0, s.useRef)(0);
          var n;
          return (
            (n = () => {
              window.cancelAnimationFrame(e.current);
            }),
            (0, s.useEffect)(() => n, []),
            (0, s.useMemo)(
              () => ({
                run: (n) => {
                  (window.cancelAnimationFrame(e.current),
                    (e.current = window.requestAnimationFrame(() => {
                      e.current = window.requestAnimationFrame(() => {
                        (n(), (e.current = 0));
                      });
                    })));
                },
                clear: () => {
                  (window.cancelAnimationFrame(e.current), (e.current = 0));
                },
                get isRunning() {
                  return 0 !== e.current;
                },
              }),
              [],
            )
          );
        }
        const ie = {
            base: "TooltipDecorator_base_c9",
            "base__theme-default": "TooltipDecorator_base__theme-default_6d",
            decorator: "TooltipDecorator_decorator_3d",
          },
          re = ["children", "className", "theme"];
        function oe() {
          return (
            (oe =
              Object.assign ||
              function (e) {
                for (var n = 1; n < arguments.length; n++) {
                  var t = arguments[n];
                  for (var i in t) Object.prototype.hasOwnProperty.call(t, i) && (e[i] = t[i]);
                }
                return e;
              }),
            oe.apply(this, arguments)
          );
        }
        const ae = u().forwardRef(function (e, n) {
            let t = e.children,
              i = e.className,
              r = e.theme,
              o = void 0 === r ? "default" : r,
              a = (function (e, n) {
                if (null == e) return {};
                var t,
                  i,
                  r = {},
                  o = Object.keys(e);
                for (i = 0; i < o.length; i++) ((t = o[i]), n.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, re);
            const l = te(),
              d = u().useRef(null);
            var c;
            return (
              (c = () => {
                l.run(() => {
                  const e = d.current;
                  if (!e) return;
                  const n = e.scrollWidth,
                    t = e.scrollHeight;
                  ne.view.resize(n, t);
                  const i = window.getComputedStyle(e);
                  ne.view.setSidePaddingsRem({
                    left: parseInt(i.getPropertyValue("padding-left"), 10),
                    top: parseInt(i.getPropertyValue("padding-top"), 10),
                    right: parseInt(i.getPropertyValue("padding-right"), 10),
                    bottom: parseInt(i.getPropertyValue("padding-bottom"), 10),
                  });
                });
              }),
              (0, s.useEffect)(c, []),
              u().createElement(
                "div",
                oe({}, a, {
                  className: v()(ie.base, ie[`base__theme-${o}`], i),
                  ref: function (e) {
                    ((d.current = e), "function" == typeof n ? n(e) : n && (n.current = e));
                  },
                }),
                u().createElement("div", { className: ie.decorator }, t),
              )
            );
          }),
          se = "App_base_e7",
          ue = "App_topBlock_f3",
          le = "App_bottomBlock_ce",
          de = "App_title_38",
          ce = "App_subTitle_5d",
          ve = "App_description_f5",
          me = "App_list_89",
          fe = "App_item_3b",
          pe = "App_divider_f7",
          ge = R.strings.achievements_page.tooltips.WTR.info,
          we = [ge.list.text1(), ge.list.text2(), ge.list.text3(), ge.list.text4()],
          he = () =>
            u().createElement(
              ae,
              null,
              u().createElement(
                "div",
                { className: se },
                u().createElement(
                  "div",
                  { className: ue },
                  u().createElement("div", { className: de }, ge.title.main()),
                  u().createElement("div", { className: ve }, ge.description.main()),
                ),
                u().createElement(
                  "div",
                  { className: le },
                  u().createElement("div", { className: pe }),
                  u().createElement("div", { className: ce }, ge.title.about()),
                  u().createElement("div", null, ge.description.about()),
                  u().createElement(
                    "div",
                    { className: me },
                    we.map((e, n) => u().createElement("div", { className: fe, key: n }, e)),
                  ),
                  u().createElement("div", null, ge.caption()),
                ),
              ),
            );
        engine.whenReady.then(() => {
          d().render(u().createElement(he, null), document.getElementById("root"));
        });
      },
    },
    t = {};
  function i(e) {
    var r = t[e];
    if (void 0 !== r) return r.exports;
    var o = (t[e] = { exports: {} });
    return (n[e](o, o.exports, i), o.exports);
  }
  ((i.m = n),
    (e = []),
    (i.O = (n, t, r, o) => {
      if (!t) {
        var a = 1 / 0;
        for (d = 0; d < e.length; d++) {
          for (var [t, r, o] = e[d], s = !0, u = 0; u < t.length; u++)
            (!1 & o || a >= o) && Object.keys(i.O).every((e) => i.O[e](t[u]))
              ? t.splice(u--, 1)
              : ((s = !1), o < a && (a = o));
          if (s) {
            e.splice(d--, 1);
            var l = r();
            void 0 !== l && (n = l);
          }
        }
        return n;
      }
      o = o || 0;
      for (var d = e.length; d > 0 && e[d - 1][2] > o; d--) e[d] = e[d - 1];
      e[d] = [t, r, o];
    }),
    (i.n = (e) => {
      var n = e && e.__esModule ? () => e.default : () => e;
      return (i.d(n, { a: n }), n);
    }),
    (i.d = (e, n) => {
      for (var t in n)
        i.o(n, t) && !i.o(e, t) && Object.defineProperty(e, t, { enumerable: !0, get: n[t] });
    }),
    (i.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (i.o = (e, n) => Object.prototype.hasOwnProperty.call(e, n)),
    (i.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (i.j = 924),
    (() => {
      var e = { 924: 0 };
      i.O.j = (n) => 0 === e[n];
      var n = (n, t) => {
          var r,
            o,
            [a, s, u] = t,
            l = 0;
          if (a.some((n) => 0 !== e[n])) {
            for (r in s) i.o(s, r) && (i.m[r] = s[r]);
            if (u) var d = u(i);
          }
          for (n && n(t); l < a.length; l++)
            ((o = a[l]), i.o(e, o) && e[o] && e[o][0](), (e[o] = 0));
          return i.O(d);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(n.bind(null, 0)), (t.push = n.bind(null, t.push.bind(t))));
    })());
  var r = i.O(void 0, [549], () => i(254));
  r = i.O(r);
})();
