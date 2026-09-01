(() => {
  "use strict";
  var e,
    n = {
      7855: (e, n, t) => {
        var r = {};
        (t.r(r), t.d(r, { mouse: () => x, onResize: () => E }));
        var i = {};
        (t.r(i),
          t.d(i, {
            events: () => r,
            getMouseGlobalPosition: () => P,
            getSize: () => _,
            graphicsQuality: () => T,
          }));
        var o = {};
        (t.r(o), t.d(o, { getBgUrl: () => O, getTextureUrl: () => S }));
        var a = {};
        (t.r(a),
          t.d(a, {
            addModelObserver: () => H,
            addPreloadTexture: () => B,
            children: () => o,
            displayStatus: () => z,
            displayStatusIs: () => re,
            events: () => j,
            extraSize: () => ie,
            forceTriggerMouseMove: () => ne,
            freezeTextureBeforeResize: () => W,
            getBrowserTexturePath: () => G,
            getDisplayStatus: () => te,
            getScale: () => U,
            getSize: () => I,
            getViewGlobalPosition: () => Q,
            isClientAccessible: () => Y,
            isEventHandled: () => ee,
            isFocused: () => X,
            pxToRem: () => $,
            remToPx: () => J,
            resize: () => q,
            sendEvent: () => k,
            setAnimateWindow: () => K,
            setEventHandled: () => Z,
            setInputPaddingsRem: () => D,
            setSidePaddingsRem: () => N,
            whenTutorialReady: () => oe,
          }));
        var s = t(6179),
          u = t.n(s),
          d = t(493),
          c = t.n(d);
        const l = "Content_base_3a",
          v = "Content_title_3c",
          f = "Content_description1_09",
          m = "Content_description2_d4",
          g = () =>
            u().createElement(
              "div",
              { className: l },
              u().createElement(
                "div",
                { className: v },
                R.strings.battle_pass.tooltips.iconLock.title(),
              ),
              u().createElement(
                "div",
                { className: f },
                R.strings.battle_pass.tooltips.iconLock.descr1(),
              ),
              u().createElement(
                "div",
                { className: m },
                R.strings.battle_pass.tooltips.iconLock.descr2(),
              ),
            );
        var w = t(6483),
          p = t.n(w);
        function h(e) {
          return (n) => (
            engine.on(e, n),
            () => {
              engine.off(e, n);
            }
          );
        }
        function b(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        const E = h("clientResized"),
          y = { down: h("mousedown"), up: h("mouseup"), move: h("mousemove") };
        const x = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function n() {
            e.enabled && b(!1);
          }
          function t() {
            e.enabled && b(!0);
          }
          function r() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", n),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", n),
                  document.body.addEventListener("mouseleave", t))
              : b(!1);
          }
          const i = ["down", "up", "move"].reduce(
            (n, t) => (
              (n[t] = (function (n) {
                return (t) => {
                  e.listeners += 1;
                  let i = !0;
                  const o = `mouse${n}`,
                    a = y[n]((e) => t([e, "outside"]));
                  function s(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(o, s),
                    r(),
                    () => {
                      i &&
                        (a(), window.removeEventListener(o, s), (e.listeners -= 1), r(), (i = !1));
                    }
                  );
                };
              })(t)),
              n
            ),
            {},
          );
          return Object.assign({}, i, {
            disable() {
              ((e.enabled = !1), r());
            },
            enable() {
              ((e.enabled = !0), r());
            },
            enableOutside() {
              e.enabled && b(!0);
            },
            disableOutside() {
              e.enabled && b(!1);
            },
          });
        })();
        function _(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function P(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const T = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function S(e, n, t = 1) {
          return viewEnv.getChildTexturePath(e, n.width, n.height, t);
        }
        function O(e, n, t) {
          return `url(${S(e, n, t)})`;
        }
        const z = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          j = {
            onTextureFrozen: h("self.onTextureFrozen"),
            onTextureReady: h("self.onTextureReady"),
            onDomBuilt: h("self.onDomBuilt"),
            onLoaded: h("self.onLoaded"),
            onDisplayChanged: h("self.onShowingStatusChanged"),
            onFocusUpdated: h("self.onFocusChanged"),
            children: {
              onAdded: h("children.onAdded"),
              onLoaded: h("children.onLoaded"),
              onRemoved: h("children.onRemoved"),
              onAttached: h("children.onAttached"),
              onTextureReady: h("children.onTextureReady"),
              onRequestPosition: h("children.requestPosition"),
            },
          },
          C = ["args"];
        const A = 2,
          V = 16,
          F = 32,
          L = 64,
          M = (e, n) => {
            const t = "GFViewEventProxy";
            if (void 0 !== n) {
              const i = n.args,
                o = (function (e, n) {
                  if (null == e) return {};
                  var t,
                    r,
                    i = {},
                    o = Object.keys(e);
                  for (r = 0; r < o.length; r++) ((t = o[r]), n.indexOf(t) >= 0 || (i[t] = e[t]));
                  return i;
                })(n, C);
              return void 0 !== i
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, o, {
                      arguments:
                        ((r = i),
                        Object.entries(r).map(([e, n]) => {
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
            var r;
          },
          k = {
            close(e) {
              M("popover" === e ? A : F);
            },
            minimize() {
              M(L);
            },
            move(e) {
              M(V, { isMouseEvent: !0, on: e });
            },
          };
        function B(e) {
          viewEnv.addPreloadTexture(e);
        }
        function D(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function G(e, n, t, r = 1) {
          return viewEnv.getWebBrowserTexturePath(e, n, t, r);
        }
        function H(e, n, t) {
          return viewEnv.addDataChangedCallback(e, n, t);
        }
        function N(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function I(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function q(e, n, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, n) : viewEnv.resizeViewPx(e, n);
        }
        function Q(e = "rem") {
          const n = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? n : { x: J(n.x), y: J(n.y) };
        }
        function W() {
          viewEnv.freezeTextureBeforeResize();
        }
        function U() {
          return viewEnv.getScale();
        }
        function $(e) {
          return viewEnv.pxToRem(e);
        }
        function J(e) {
          return viewEnv.remToPx(e);
        }
        function K(e, n) {
          viewEnv.setAnimateWindow(e, n);
        }
        function X() {
          return viewEnv.isFocused();
        }
        function Y() {
          return viewEnv.isClientAccessible();
        }
        function Z() {
          return viewEnv.setEventHandled();
        }
        function ee() {
          return viewEnv.isEventHandled();
        }
        function ne() {
          viewEnv.forceTriggerMouseMove();
        }
        function te() {
          return viewEnv.getShowingStatus();
        }
        const re = Object.keys(z).reduce(
            (e, n) => ((e[n] = () => viewEnv.getShowingStatus() === z[n]), e),
            {},
          ),
          ie = {
            set: (e, n) => {
              viewEnv.setExtraSizeRem(e, n);
            },
            get: (e, n) => {
              viewEnv.getExtraSizeRem(e, n);
            },
          },
          oe = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : j.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          ae = { view: a, client: i };
        function se() {
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
        const ue = {
            base: "TooltipDecorator_base_c9",
            "base__theme-default": "TooltipDecorator_base__theme-default_6d",
            decorator: "TooltipDecorator_decorator_3d",
          },
          de = ["children", "className", "theme"];
        function ce() {
          return (
            (ce =
              Object.assign ||
              function (e) {
                for (var n = 1; n < arguments.length; n++) {
                  var t = arguments[n];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            ce.apply(this, arguments)
          );
        }
        const le = u().forwardRef(function (e, n) {
            let t = e.children,
              r = e.className,
              i = e.theme,
              o = void 0 === i ? "default" : i,
              a = (function (e, n) {
                if (null == e) return {};
                var t,
                  r,
                  i = {},
                  o = Object.keys(e);
                for (r = 0; r < o.length; r++) ((t = o[r]), n.indexOf(t) >= 0 || (i[t] = e[t]));
                return i;
              })(e, de);
            const d = se(),
              c = u().useRef(null);
            var l;
            return (
              (l = () => {
                d.run(() => {
                  const e = c.current;
                  if (!e) return;
                  const n = e.scrollWidth,
                    t = e.scrollHeight;
                  ae.view.resize(n, t);
                  const r = window.getComputedStyle(e);
                  ae.view.setSidePaddingsRem({
                    left: parseInt(r.getPropertyValue("padding-left"), 10),
                    top: parseInt(r.getPropertyValue("padding-top"), 10),
                    right: parseInt(r.getPropertyValue("padding-right"), 10),
                    bottom: parseInt(r.getPropertyValue("padding-bottom"), 10),
                  });
                });
              }),
              (0, s.useEffect)(l, []),
              u().createElement(
                "div",
                ce({}, a, {
                  className: p()(ue.base, ue[`base__theme-${o}`], r),
                  ref: function (e) {
                    ((c.current = e), "function" == typeof n ? n(e) : n && (n.current = e));
                  },
                }),
                u().createElement("div", { className: ue.decorator }, t),
              )
            );
          }),
          ve = () => u().createElement(le, null, u().createElement(g, null));
        engine.whenReady.then(() => {
          c().render(u().createElement(ve, null), document.getElementById("root"));
        });
      },
    },
    t = {};
  function r(e) {
    var i = t[e];
    if (void 0 !== i) return i.exports;
    var o = (t[e] = { exports: {} });
    return (n[e](o, o.exports, r), o.exports);
  }
  ((r.m = n),
    (e = []),
    (r.O = (n, t, i, o) => {
      if (!t) {
        var a = 1 / 0;
        for (c = 0; c < e.length; c++) {
          for (var [t, i, o] = e[c], s = !0, u = 0; u < t.length; u++)
            (!1 & o || a >= o) && Object.keys(r.O).every((e) => r.O[e](t[u]))
              ? t.splice(u--, 1)
              : ((s = !1), o < a && (a = o));
          if (s) {
            e.splice(c--, 1);
            var d = i();
            void 0 !== d && (n = d);
          }
        }
        return n;
      }
      o = o || 0;
      for (var c = e.length; c > 0 && e[c - 1][2] > o; c--) e[c] = e[c - 1];
      e[c] = [t, i, o];
    }),
    (r.n = (e) => {
      var n = e && e.__esModule ? () => e.default : () => e;
      return (r.d(n, { a: n }), n);
    }),
    (r.d = (e, n) => {
      for (var t in n)
        r.o(n, t) && !r.o(e, t) && Object.defineProperty(e, t, { enumerable: !0, get: n[t] });
    }),
    (r.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (r.o = (e, n) => Object.prototype.hasOwnProperty.call(e, n)),
    (r.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (r.j = 5610),
    (() => {
      var e = { 5610: 0 };
      r.O.j = (n) => 0 === e[n];
      var n = (n, t) => {
          var i,
            o,
            [a, s, u] = t,
            d = 0;
          if (a.some((n) => 0 !== e[n])) {
            for (i in s) r.o(s, i) && (r.m[i] = s[i]);
            if (u) var c = u(r);
          }
          for (n && n(t); d < a.length; d++)
            ((o = a[d]), r.o(e, o) && e[o] && e[o][0](), (e[o] = 0));
          return r.O(c);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(n.bind(null, 0)), (t.push = n.bind(null, t.push.bind(t))));
    })());
  var i = r.O(void 0, [1519], () => r(7855));
  i = r.O(i);
})();
