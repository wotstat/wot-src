(() => {
  var __webpack_modules__ = {
      926: (e) => {
        e.exports = {
          SMALL_WIDTH: "mediaSmallWidth",
          MEDIUM_WIDTH: "mediaMediumWidth",
          LARGE_WIDTH: "mediaLargeWidth",
          EXTRA_LARGE_WIDTH: "mediaExtraLargeWidth",
          SMALL_HEIGHT: "mediaSmallHeight",
          MEDIUM_HEIGHT: "mediaMediumHeight",
          LARGE_HEIGHT: "mediaLargeHeight",
          EXTRA_LARGE_HEIGHT: "mediaExtraLargeHeight",
          SMALL: "mediaSmall",
          MEDIUM: "mediaMedium",
          LARGE: "mediaLarge",
          EXTRA_LARGE: "mediaExtraLarge",
        };
      },
      67: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => K });
        var n = {};
        (t.r(n), t.d(n, { mouse: () => _, onResize: () => l }));
        var r = {};
        (t.r(r),
          t.d(r, {
            events: () => n,
            getMouseGlobalPosition: () => E,
            getSize: () => d,
            graphicsQuality: () => m,
          }));
        var a = {};
        (t.r(a), t.d(a, { getBgUrl: () => F, getTextureUrl: () => A }));
        var o = {};
        function s(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        function i(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        (t.r(o),
          t.d(o, {
            addModelObserver: () => S,
            addPreloadTexture: () => w,
            children: () => a,
            displayStatus: () => g,
            displayStatusIs: () => G,
            events: () => C,
            extraSize: () => j,
            forceTriggerMouseMove: () => V,
            freezeTextureBeforeResize: () => T,
            getBrowserTexturePath: () => x,
            getDisplayStatus: () => $,
            getScale: () => P,
            getSize: () => M,
            getViewGlobalPosition: () => N,
            isClientAccessible: () => W,
            isEventHandled: () => U,
            isFocused: () => I,
            pxToRem: () => R,
            remToPx: () => O,
            resize: () => k,
            sendEvent: () => b,
            setAnimateWindow: () => H,
            setEventHandled: () => z,
            setInputPaddingsRem: () => y,
            setSidePaddingsRem: () => L,
            whenTutorialReady: () => q,
          }));
        const l = s("clientResized"),
          c = { down: s("mousedown"), up: s("mouseup"), move: s("mousemove") };
        const _ = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && i(!1);
          }
          function t() {
            e.enabled && i(!0);
          }
          function n() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : i(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let r = !0;
                  const a = `mouse${u}`,
                    o = c[u]((e) => t([e, "outside"]));
                  function s(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(a, s),
                    n(),
                    () => {
                      r &&
                        (o(), window.removeEventListener(a, s), (e.listeners -= 1), n(), (r = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
            },
            enableOutside() {
              e.enabled && i(!0);
            },
            disableOutside() {
              e.enabled && i(!1);
            },
          });
        })();
        function d(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function E(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const m = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function A(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function F(e, u, t) {
          return `url(${A(e, u, t)})`;
        }
        const g = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          C = {
            onTextureFrozen: s("self.onTextureFrozen"),
            onTextureReady: s("self.onTextureReady"),
            onDomBuilt: s("self.onDomBuilt"),
            onLoaded: s("self.onLoaded"),
            onDisplayChanged: s("self.onShowingStatusChanged"),
            onFocusUpdated: s("self.onFocusChanged"),
            children: {
              onAdded: s("children.onAdded"),
              onLoaded: s("children.onLoaded"),
              onRemoved: s("children.onRemoved"),
              onAttached: s("children.onAttached"),
              onTextureReady: s("children.onTextureReady"),
              onRequestPosition: s("children.requestPosition"),
            },
          },
          D = ["args"];
        const h = 2,
          B = 16,
          p = 32,
          v = 64,
          f = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, D);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, u]) => {
                          const t = "GFValueProxy";
                          switch (typeof u) {
                            case "number":
                              return { __Type: t, name: e, number: u };
                            case "boolean":
                              return { __Type: t, name: e, bool: u };
                            default:
                              return { __Type: t, name: e, string: u.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, a));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          b = {
            close(e) {
              f("popover" === e ? h : p);
            },
            minimize() {
              f(v);
            },
            move(e) {
              f(B, { isMouseEvent: !0, on: e });
            },
          };
        function w(e) {
          viewEnv.addPreloadTexture(e);
        }
        function y(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function x(e, u, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, n);
        }
        function S(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function L(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function M(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function k(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function N(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: O(u.x), y: O(u.y) };
        }
        function T() {
          viewEnv.freezeTextureBeforeResize();
        }
        function P() {
          return viewEnv.getScale();
        }
        function R(e) {
          return viewEnv.pxToRem(e);
        }
        function O(e) {
          return viewEnv.remToPx(e);
        }
        function H(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function I() {
          return viewEnv.isFocused();
        }
        function W() {
          return viewEnv.isClientAccessible();
        }
        function z() {
          return viewEnv.setEventHandled();
        }
        function U() {
          return viewEnv.isEventHandled();
        }
        function V() {
          viewEnv.forceTriggerMouseMove();
        }
        function $() {
          return viewEnv.getShowingStatus();
        }
        const G = Object.keys(g).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === g[u]), e),
            {},
          ),
          j = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          q = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : C.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          K = { view: o, client: r };
      },
      521: (e, u, t) => {
        "use strict";
        let n, r;
        (t.d(u, { n: () => n }),
          (function (e) {
            ((e[(e.NONE = -1)] = "NONE"),
              (e[(e.ALT = 165)] = "ALT"),
              (e[(e.ENTER = 13)] = "ENTER"),
              (e[(e.ESCAPE = 27)] = "ESCAPE"),
              (e[(e.SPACE = 32)] = "SPACE"),
              (e[(e.END = 35)] = "END"),
              (e[(e.HOME = 36)] = "HOME"),
              (e[(e.ARROW_LEFT = 37)] = "ARROW_LEFT"),
              (e[(e.ARROW_UP = 38)] = "ARROW_UP"),
              (e[(e.ARROW_RIGHT = 39)] = "ARROW_RIGHT"),
              (e[(e.ARROW_DOWN = 40)] = "ARROW_DOWN"),
              (e[(e.NUM_PLUS = 107)] = "NUM_PLUS"),
              (e[(e.NUM_MINUS = 109)] = "NUM_MINUS"),
              (e[(e.PLUS = 187)] = "PLUS"),
              (e[(e.MINUS = 189)] = "MINUS"),
              (e[(e.PAGE_UP = 33)] = "PAGE_UP"),
              (e[(e.PAGE_DOWN = 34)] = "PAGE_DOWN"),
              (e[(e.BACKSPACE = 8)] = "BACKSPACE"),
              (e[(e.DELETE = 46)] = "DELETE"),
              (e[(e.TAB = 9)] = "TAB"),
              (e[(e.KEY_N = 78)] = "KEY_N"),
              (e[(e.KEY_0 = 48)] = "KEY_0"),
              (e[(e.KEY_1 = 49)] = "KEY_1"),
              (e[(e.KEY_2 = 50)] = "KEY_2"),
              (e[(e.KEY_3 = 51)] = "KEY_3"),
              (e[(e.KEY_4 = 52)] = "KEY_4"),
              (e[(e.KEY_5 = 53)] = "KEY_5"),
              (e[(e.KEY_6 = 54)] = "KEY_6"),
              (e[(e.KEY_7 = 55)] = "KEY_7"),
              (e[(e.KEY_8 = 56)] = "KEY_8"),
              (e[(e.KEY_9 = 57)] = "KEY_9"),
              (e[(e.CAPS_LOCK = 20)] = "CAPS_LOCK"),
              (e[(e.INSERT = 45)] = "INSERT"),
              (e[(e.F1 = 112)] = "F1"),
              (e[(e.F2 = 113)] = "F2"),
              (e[(e.F3 = 114)] = "F3"),
              (e[(e.F4 = 115)] = "F4"),
              (e[(e.F5 = 116)] = "F5"),
              (e[(e.F6 = 117)] = "F6"),
              (e[(e.F7 = 118)] = "F7"),
              (e[(e.F8 = 119)] = "F8"),
              (e[(e.F9 = 120)] = "F9"),
              (e[(e.F10 = 121)] = "F10"),
              (e[(e.F11 = 122)] = "F11"),
              (e[(e.F12 = 123)] = "F12"),
              (e[(e.SELECT = 93)] = "SELECT"),
              (e[(e.NUMPAD_0 = 96)] = "NUMPAD_0"),
              (e[(e.NUMPAD_1 = 97)] = "NUMPAD_1"),
              (e[(e.NUMPAD_2 = 98)] = "NUMPAD_2"),
              (e[(e.NUMPAD_3 = 99)] = "NUMPAD_3"),
              (e[(e.NUMPAD_4 = 100)] = "NUMPAD_4"),
              (e[(e.NUMPAD_5 = 101)] = "NUMPAD_5"),
              (e[(e.NUMPAD_6 = 102)] = "NUMPAD_6"),
              (e[(e.NUMPAD_7 = 103)] = "NUMPAD_7"),
              (e[(e.NUMPAD_8 = 104)] = "NUMPAD_8"),
              (e[(e.NUMPAD_9 = 105)] = "NUMPAD_9"),
              (e[(e.NUM_DECIMAL = 110)] = "NUM_DECIMAL"),
              (e[(e.STAR = 106)] = "STAR"),
              (e[(e.NUM_SLASH = 111)] = "NUM_SLASH"),
              (e[(e.FORWARD_SLASH = 191)] = "FORWARD_SLASH"),
              (e[(e.COMMA = 188)] = "COMMA"),
              (e[(e.DASH = 189)] = "DASH"),
              (e[(e.PERIOD = 190)] = "PERIOD"));
          })(n || (n = {})),
          (function (e) {
            ((e.ALT = "Alt"),
              (e.ALT_GRAPH = "AltGraph"),
              (e.CAPS_LOCK = "CapsLock"),
              (e.CONTROL = "Control"),
              (e.FN = "Fn"),
              (e.FN_LOCK = "FnLock"),
              (e.META = "Meta"),
              (e.NUM_LOCK = "NumLock"),
              (e.SCROLL_LOCK = "ScrollLock"),
              (e.SHIFT = "Shift"),
              (e.SYMBOL = "Symbol"),
              (e.SYMBOL_LOCK = "SymbolLock"));
          })(r || (r = {})));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        var n = t(67);
        class r {
          constructor() {
            ((this._callbacks = void 0),
              (this._updateHandler = void 0),
              (this._views = void 0),
              (this.clearViewCallbacks = (e) => {
                this._views[e] &&
                  (this._views[e].forEach((e) => {
                    delete this._callbacks[e];
                  }),
                  delete this._views[e]);
              }),
              (this._callbacks = {}),
              (this._views = {}),
              (this._updateHandler = void 0));
          }
          static get instance() {
            return (window.__dataTracker || (window.__dataTracker = new r()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const a = n.O.view.addModelObserver(e, t, r);
            return (
              a > 0
                ? ((this._callbacks[a] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(a) : (this._views[t] = [a])))
                : console.error("Can't add callback for model:", e),
              a
            );
          }
          removeCallback(e, u = 0) {
            let t = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((t = viewEnv.removeDataChangedCallback(e, u)), delete this._callbacks[e]),
              t || console.error("Can't remove callback by id:", e),
              t
            );
          }
          _emmitDataChanged(e, u, t) {
            t.forEach((t) => {
              const n = this._callbacks[t];
              void 0 !== n && n(e, u);
            });
          }
        }
        r.__instance = void 0;
        const a = r;
      },
      572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
        "use strict";
        __webpack_require__.d(__webpack_exports__, { Z: () => __WEBPACK_DEFAULT_EXPORT__ });
        var _DataTracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(358),
          _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(364);
        class ViewModel {
          constructor(path, watchingFields = []) {
            ((this.dataTracker = void 0),
              (this.modelPath = void 0),
              (this.callbacks = void 0),
              (this.data = void 0),
              (this._notifyObservers = () => {
                ((this.data = eval(this.modelPath)),
                  this.callbacks.forEach((e) => {
                    e(this.data);
                  }));
              }),
              (this.dataTracker = new _DataTracker__WEBPACK_IMPORTED_MODULE_0__.Z()),
              (this.modelPath = path),
              (this.callbacks = new Set()),
              (0, _index__WEBPACK_IMPORTED_MODULE_1__.ry)().then(() => {
                (this._addCallback(path),
                  watchingFields.forEach((e) => {
                    this._addCallback(path + "." + e);
                  }),
                  this._notifyObservers());
              }));
          }
          subscribe(e) {
            (this.callbacks.add(e), null !== this.data && void 0 !== this.data && e(this.data));
          }
          unsubscribe(e) {
            this.callbacks.delete(e);
          }
          destroy() {
            (this.dataTracker.clear(), this.callbacks.clear());
          }
          _addCallback(e) {
            this.dataTracker.addCallback(e, this._notifyObservers);
          }
        }
        const __WEBPACK_DEFAULT_EXPORT__ = ViewModel;
      },
      364: (e, u, t) => {
        "use strict";
        t.d(u, { Sw: () => a.Z, B3: () => l, Z5: () => o, B0: () => i, ry: () => C });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let n = e.target;
                  do {
                    if (n === u) return;
                    n = n.parentNode;
                  } while (n);
                  t();
                });
              }));
          }
          static get instance() {
            return (n.__instance || (n.__instance = new n()), n.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              n = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== n,
            )),
              this.removeMouseListener());
          }
          addMouseListener() {
            this._listenMouse ||
              (document.addEventListener("mousedown", this.onMouseDown), (this._listenMouse = !0));
          }
          removeMouseListener() {
            this._listenMouse &&
              0 === this.entries.length &&
              (document.removeEventListener("mousedown", this.onMouseDown),
              (this._listenMouse = !1));
          }
        }
        n.__instance = void 0;
        const r = n;
        var a = t(358);
        const o = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          s = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, u, t) => userLocale.getTimeFormat(e, u, void 0 === t || t),
            getTimeString: (e, u, t) => userLocale.getTimeString(e, u, void 0 === t || t),
          };
        let i;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(i || (i = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var E = t(521),
          m = t(67);
        const A = ["args"];
        function F(e, u, t, n, r, a, o) {
          try {
            var s = e[a](o),
              i = s.value;
          } catch (e) {
            return void t(e);
          }
          s.done ? u(i) : Promise.resolve(i).then(n, r);
        }
        const g = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          C = (function () {
            var e,
              u =
                ((e = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((e) => {
                      engine.on("Ready", e);
                    })
                  );
                }),
                function () {
                  var u = this,
                    t = arguments;
                  return new Promise(function (n, r) {
                    var a = e.apply(u, t);
                    function o(e) {
                      F(a, n, r, o, s, "next", e);
                    }
                    function s(e) {
                      F(a, n, r, o, s, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          D = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, A);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, u]) => {
                          const t = { __Type: "GFValueProxy", name: e };
                          switch (typeof u) {
                            case "number":
                              t.number = u;
                              break;
                            case "boolean":
                              t.bool = u;
                              break;
                            default:
                              t.string = u.toString();
                          }
                          return t;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, a));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          h = () => D(i.CLOSE),
          B = (e, u) => {
            e.keyCode === E.n.ESCAPE && u();
          };
        var p = t(572);
        const v = r.instance,
          f = {
            DataTracker: a.Z,
            ViewModel: p.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: _,
            DateFormatType: d,
            makeGlobalBoundingBox: g,
            sendMoveEvent: (e) => D(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: h,
            sendClosePopOverEvent: () => D(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              D(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, r = R.invalid("resId"), a) => {
              const o = m.O.view.getViewGlobalPosition(),
                s = t.getBoundingClientRect(),
                l = s.x,
                c = s.y,
                _ = s.width,
                d = s.height,
                E = {
                  x: m.O.view.pxToRem(l) + o.x,
                  y: m.O.view.pxToRem(c) + o.y,
                  width: m.O.view.pxToRem(_),
                  height: m.O.view.pxToRem(d),
                };
              D(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: g(E),
                on: !0,
                args: a,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => B(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              B(e, h);
            },
            handleViewEvent: D,
            onBindingsReady: C,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const n in u)
                if (Object.prototype.hasOwnProperty.call(u, n)) {
                  const r = Object.prototype.toString.call(u[n]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = u[n];
                    t[n] = [];
                    for (let u = 0; u < r.length; u++) t[n].push({ value: e(r[u].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = e(u[n]))
                      : (t[n] = u[n]);
                }
              return t;
            },
            ClickOutsideManager: v,
            SystemLocale: o,
            UserLocale: s,
          };
        window.ViewEnvHelper = f;
      },
      609: (e, u, t) => {
        "use strict";
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => ju,
            Bar: () => Vu,
            DefaultScroll: () => Gu,
            Direction: () => K,
            defaultSettings: () => Y,
            useHorizontalScrollApi: () => Lu,
          }));
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => lt,
            Bar: () => ot,
            Default: () => it,
            useVerticalScrollApi: () => Z,
          }));
        var a = t(67),
          o = t(179),
          s = t.n(o);
        const i = (e, u, t) =>
            u.extraLargeHeight ||
            u.largeHeight ||
            u.mediumHeight ||
            u.smallHeight ||
            u.extraSmallHeight
              ? (u.extraLargeHeight && t.extraLarge) ||
                (u.largeHeight && t.large) ||
                (u.mediumHeight && t.medium) ||
                (u.smallHeight && t.small) ||
                (u.extraSmallHeight && t.extraSmall)
                ? e
                : null
              : e,
          l = {
            extraLarge: { weight: 4, width: 2560, height: 1440 },
            large: { weight: 3, width: 1920, height: 1080 },
            medium: { weight: 2, width: 1600, height: 900 },
            small: { weight: 1, width: 1366, height: 768 },
            extraSmall: { weight: 0, width: 1024, height: 768 },
          };
        var c;
        function _(e, u, t) {
          const n = (function (e, u) {
              switch (!0) {
                case e >= u.extraLarge.width:
                  return u.extraLarge.weight;
                case e >= u.large.width && e < u.extraLarge.width:
                  return u.large.weight;
                case e >= u.medium.width && e < u.large.width:
                  return u.medium.weight;
                case e >= u.small.width && e < u.medium.width:
                  return u.small.weight;
                default:
                  return u.extraSmall.weight;
              }
            })(e, t),
            r = (function (e, u) {
              switch (!0) {
                case e >= u.extraLarge.height:
                  return u.extraLarge.weight;
                case e >= u.large.height && e < u.extraLarge.height:
                  return u.large.weight;
                case e >= u.medium.height && e < u.large.height:
                  return u.medium.weight;
                case e >= u.small.height && e < u.medium.height:
                  return u.small.weight;
                default:
                  return u.extraSmall.weight;
              }
            })(u, t),
            a = Math.min(n, r);
          return {
            extraLarge: a === t.extraLarge.weight,
            large: a === t.large.weight,
            medium: a === t.medium.weight,
            small: a === t.small.weight,
            extraSmall: a === t.extraSmall.weight,
            extraLargeWidth: n === t.extraLarge.weight,
            largeWidth: n === t.large.weight,
            mediumWidth: n === t.medium.weight,
            smallWidth: n === t.small.weight,
            extraSmallWidth: n === t.extraSmall.weight,
            extraLargeHeight: r === t.extraLarge.weight,
            largeHeight: r === t.large.weight,
            mediumHeight: r === t.medium.weight,
            smallHeight: r === t.small.weight,
            extraSmallHeight: r === t.extraSmall.weight,
          };
        }
        !(function (e) {
          ((e.extraLarge = "extraLarge"),
            (e.large = "large"),
            (e.medium = "medium"),
            (e.small = "small"),
            (e.extraSmall = "extraSmall"),
            (e.extraLargeWidth = "extraLargeWidth"),
            (e.largeWidth = "largeWidth"),
            (e.mediumWidth = "mediumWidth"),
            (e.smallWidth = "smallWidth"),
            (e.extraSmallWidth = "extraSmallWidth"),
            (e.extraLargeHeight = "extraLargeHeight"),
            (e.largeHeight = "largeHeight"),
            (e.mediumHeight = "mediumHeight"),
            (e.smallHeight = "smallHeight"),
            (e.extraSmallHeight = "extraSmallHeight"));
        })(c || (c = {}));
        const d = a.O.client.getSize("rem"),
          E = d.width,
          m = d.height,
          A = Object.assign({ width: E, height: m }, _(E, m, l)),
          F = (0, o.createContext)(A),
          g = ["children"];
        const C = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, g);
          const n = (0, o.useContext)(F),
            r = n.extraLarge,
            a = n.large,
            s = n.medium,
            l = n.small,
            c = n.extraSmall,
            _ = n.extraLargeWidth,
            d = n.largeWidth,
            E = n.mediumWidth,
            m = n.smallWidth,
            A = n.extraSmallWidth,
            C = n.extraLargeHeight,
            D = n.largeHeight,
            h = n.mediumHeight,
            B = n.smallHeight,
            p = n.extraSmallHeight,
            v = { extraLarge: C, large: D, medium: h, small: B, extraSmall: p };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && r) return u;
            if (t.large && a) return u;
            if (t.medium && s) return u;
            if (t.small && l) return u;
            if (t.extraSmall && c) return u;
          } else {
            if (t.extraLargeWidth && _) return i(u, t, v);
            if (t.largeWidth && d) return i(u, t, v);
            if (t.mediumWidth && E) return i(u, t, v);
            if (t.smallWidth && m) return i(u, t, v);
            if (t.extraSmallWidth && A) return i(u, t, v);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && C) return u;
              if (t.largeHeight && D) return u;
              if (t.mediumHeight && h) return u;
              if (t.smallHeight && B) return u;
              if (t.extraSmallHeight && p) return u;
            }
          }
          return null;
        };
        C.defaultProps = {
          extraLarge: !1,
          large: !1,
          medium: !1,
          small: !1,
          extraSmall: !1,
          extraLargeWidth: !1,
          largeWidth: !1,
          mediumWidth: !1,
          smallWidth: !1,
          extraSmallWidth: !1,
          extraLargeHeight: !1,
          largeHeight: !1,
          mediumHeight: !1,
          smallHeight: !1,
          extraSmallHeight: !1,
        };
        (0, o.memo)(C);
        const D = (e) => {
            const u = (0, o.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          h = (0, o.memo)(({ children: e }) => {
            const u = (0, o.useContext)(F),
              t = (0, o.useState)(u),
              n = t[0],
              r = t[1],
              i = (0, o.useCallback)((e, u) => {
                const t = a.O.view.pxToRem(e),
                  n = a.O.view.pxToRem(u);
                r(Object.assign({ width: t, height: n }, _(t, n, l)));
              }, []);
            (D(() => {
              engine.on("clientResized", i);
            }),
              (0, o.useEffect)(() => () => engine.off("clientResized", i), [i]));
            const c = (0, o.useMemo)(() => Object.assign({}, n), [n]);
            return s().createElement(F.Provider, { value: c }, e);
          });
        var B = t(483),
          p = t.n(B),
          v = t(926),
          f = t.n(v);
        let b, w, y;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.small.width)] = "Small"),
            (e[(e.Medium = l.medium.width)] = "Medium"),
            (e[(e.Large = l.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(b || (b = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = l.small.width)] = "Small"),
              (e[(e.Medium = l.medium.width)] = "Medium"),
              (e[(e.Large = l.large.width)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
          })(w || (w = {})),
          (function (e) {
            ((e[(e.ExtraSmall = l.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = l.small.height)] = "Small"),
              (e[(e.Medium = l.medium.height)] = "Medium"),
              (e[(e.Large = l.large.height)] = "Large"),
              (e[(e.ExtraLarge = l.extraLarge.height)] = "ExtraLarge"));
          })(y || (y = {})));
        const x = () => {
            const e = (0, o.useContext)(F),
              u = e.width,
              t = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return b.ExtraLarge;
                  case e.large:
                    return b.Large;
                  case e.medium:
                    return b.Medium;
                  case e.small:
                    return b.Small;
                  case e.extraSmall:
                    return b.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), b.ExtraSmall);
                }
              })(e),
              r = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return w.ExtraLarge;
                  case e.largeWidth:
                    return w.Large;
                  case e.mediumWidth:
                    return w.Medium;
                  case e.smallWidth:
                    return w.Small;
                  case e.extraSmallWidth:
                    return w.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), w.ExtraSmall);
                }
              })(e),
              a = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return y.ExtraLarge;
                  case e.largeHeight:
                    return y.Large;
                  case e.mediumHeight:
                    return y.Medium;
                  case e.smallHeight:
                    return y.Small;
                  case e.extraSmallHeight:
                    return y.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), y.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: n,
              mediaWidth: r,
              mediaHeight: a,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          S = ["children", "className"];
        function L() {
          return (
            (L =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            L.apply(this, arguments)
          );
        }
        const M = {
            [w.ExtraSmall]: "",
            [w.Small]: f().SMALL_WIDTH,
            [w.Medium]: `${f().SMALL_WIDTH} ${f().MEDIUM_WIDTH}`,
            [w.Large]: `${f().SMALL_WIDTH} ${f().MEDIUM_WIDTH} ${f().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${f().SMALL_WIDTH} ${f().MEDIUM_WIDTH} ${f().LARGE_WIDTH} ${f().EXTRA_LARGE_WIDTH}`,
          },
          k = {
            [y.ExtraSmall]: "",
            [y.Small]: f().SMALL_HEIGHT,
            [y.Medium]: `${f().SMALL_HEIGHT} ${f().MEDIUM_HEIGHT}`,
            [y.Large]: `${f().SMALL_HEIGHT} ${f().MEDIUM_HEIGHT} ${f().LARGE_HEIGHT}`,
            [y.ExtraLarge]: `${f().SMALL_HEIGHT} ${f().MEDIUM_HEIGHT} ${f().LARGE_HEIGHT} ${f().EXTRA_LARGE_HEIGHT}`,
          },
          N = {
            [b.ExtraSmall]: "",
            [b.Small]: f().SMALL,
            [b.Medium]: `${f().SMALL} ${f().MEDIUM}`,
            [b.Large]: `${f().SMALL} ${f().MEDIUM} ${f().LARGE}`,
            [b.ExtraLarge]: `${f().SMALL} ${f().MEDIUM} ${f().LARGE} ${f().EXTRA_LARGE}`,
          },
          T = (e) => {
            let u = e.children,
              t = e.className,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, S);
            const r = x(),
              a = r.mediaWidth,
              o = r.mediaHeight,
              i = r.mediaSize;
            return s().createElement("div", L({ className: p()(t, M[a], k[o], N[i]) }, n), u);
          },
          P = ["children"];
        const O = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, P);
          return s().createElement(h, null, s().createElement(T, t, u));
        };
        var H = t(493),
          I = t.n(H);
        const W = (e, u, t) => (t < e ? e : t > u ? u : t),
          z = (e) => {
            let u,
              t = null;
            return (
              (t = requestAnimationFrame(() => {
                t = requestAnimationFrame(() => {
                  ((t = null), (u = e()));
                });
              })),
              () => {
                ("function" == typeof u && u(), null !== t && cancelAnimationFrame(t));
              }
            );
          };
        function U(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return V(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return V(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function V(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const $ = [];
        function G(e) {
          const u = (0, o.useRef)(e);
          return (
            (0, o.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, o.useCallback)((...e) => (0, u.current)(...e), $)
          );
        }
        function j(e, u, t) {
          const n = (0, o.useMemo)(
            () =>
              (function (e, u, t, n) {
                let r,
                  a = !1,
                  o = 0;
                function s() {
                  r && clearTimeout(r);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - o;
                  function _() {
                    ((o = Date.now()), t.apply(l, i));
                  }
                  a ||
                    (n && !r && _(),
                    s(),
                    void 0 === n && c > e
                      ? _()
                      : !0 !== u &&
                        (r = setTimeout(
                          n
                            ? function () {
                                r = void 0;
                              }
                            : _,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((n = t), (t = u), (u = void 0)),
                  (i.cancel = function () {
                    (s(), (a = !0));
                  }),
                  i
                );
              })(t, e),
            u,
          );
          return ((0, o.useEffect)(() => n.cancel, [n]), n);
        }
        var q = t(30);
        let K;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(K || (K = {}));
        const Y = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          X = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: s = !1,
          }) => {
            const i = (e, t) => {
              const n = u(e),
                r = n[0],
                a = n[1];
              return W(r, a, t);
            };
            return (l = {}) => {
              const c = l.settings,
                _ = void 0 === c ? Y : c,
                d = (0, o.useRef)(null),
                E = (0, o.useRef)(null),
                m = (() => {
                  const e = (0, o.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    n = (e, t) => {
                      u(e).delete(t);
                    },
                    r = (e, ...t) => {
                      for (var n, r = U(u(e).values()); !(n = r()).done;) (0, n.value)(...t);
                    };
                  return (0, o.useMemo)(() => ({ on: t, off: n, trigger: r }), []);
                })(),
                A = j(
                  () => {
                    a.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                F = (0, q.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = d.current;
                    u && (t(u, e), m.trigger("change", e), s && A());
                  },
                  onRest: (e) => m.trigger("rest", e),
                  onStart: (e) => m.trigger("start", e),
                  onPause: (e) => m.trigger("pause", e),
                })),
                g = F[0],
                C = F[1],
                D = (0, o.useCallback)(
                  (e, u, t) => {
                    var n;
                    const r = g.scrollPosition.get(),
                      a = (null != (n = g.scrollPosition.goal) ? n : 0) - r;
                    return i(e, u * t + a + r);
                  },
                  [g.scrollPosition],
                ),
                h = (0, o.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const n = d.current;
                    n &&
                      C.start({
                        scrollPosition: i(n, e),
                        immediate: u,
                        reset: t,
                        config: _.animationConfig,
                        from: { scrollPosition: i(n, g.scrollPosition.get()) },
                      });
                  },
                  [C, _.animationConfig, g.scrollPosition],
                ),
                B = (0, o.useCallback)(
                  (e) => {
                    const u = d.current,
                      t = E.current;
                    if (!u || !t) return;
                    const n = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return r(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, _.step),
                      a = D(u, e, n);
                    h(a);
                  },
                  [h, D, _.step],
                ),
                p = (0, o.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && B(n(e)),
                      d.current && m.trigger("mouseWheel", e, g.scrollPosition, u(d.current)));
                  },
                  [g.scrollPosition, B, m],
                ),
                v = ((e, u = []) => {
                  const t = (0, o.useRef)(),
                    n = (0, o.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, o.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    z(() => {
                      const e = d.current;
                      e &&
                        (h(i(e, g.scrollPosition.goal), { immediate: !0 }),
                        m.trigger("resizeHandled"));
                    }),
                  [h, g.scrollPosition.goal],
                ),
                f = G(() => {
                  const e = d.current;
                  if (!e) return;
                  const u = i(e, g.scrollPosition.goal);
                  (u !== g.scrollPosition.goal && h(u, { immediate: !0 }),
                    m.trigger("recalculateContent"));
                });
              (0, o.useEffect)(
                () => (
                  window.addEventListener("resize", v),
                  () => {
                    window.removeEventListener("resize", v);
                  }
                ),
                [v],
              );
              const b = (0, o.useCallback)((e) => m.trigger("isThumbDraggingChanged", e), [m]);
              return (0, o.useMemo)(
                () => ({
                  getWrapperSize: () => (E.current ? r(E.current) : void 0),
                  getContainerSize: () => (d.current ? e(d.current) : void 0),
                  getBounds: () =>
                    d.current
                      ? u(d.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: _.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: p,
                  applyScroll: h,
                  applyStepTo: B,
                  contentRef: d,
                  wrapperRef: E,
                  scrollPosition: C,
                  animationScroll: g,
                  recalculateContent: f,
                  handleIsThumbDragging: b,
                  events: { on: m.on, off: m.off },
                }),
                [g.scrollPosition, h, B, b, m.off, m.on, f, p, C, _.step.clampedArrowStepTimeout],
              );
            };
          },
          Z = X({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? K.Next : K.Prev),
          });
        var Q = t(521),
          J = t(364);
        const ee = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function ue(e = Q.n.NONE, u = ee, t = !1) {
          (0, o.useEffect)(() => {
            if (e !== Q.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (a.O.view.isEventHandled()) return;
                (a.O.view.setEventHandled(), u(n), t && n.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        const te = (e = 1) => {
            const u = new Error().stack;
            let t,
              n = R.invalid("resId");
            return (
              u &&
                ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                window.__feature &&
                  window.__feature !== t &&
                  window.subViews[t] &&
                  (n = window.subViews[t].id)),
              { caller: t, stack: u, resId: n }
            );
          },
          ne = (e, u) => e.split(".").reduce((e, u) => e && e[u], u),
          re = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          ae = (e, u) => (e.length > 0 ? `${e}.${u}` : u),
          oe = (e) =>
            ((e, u) =>
              e.split(".").reduce((e, t) => {
                const n = ne(`${e}.${t}`, window);
                return re(n) ? u(e, t, n) : `${e}.${t}`;
              }))(e, (e, u) => `${e}.${u}.value`),
          se = (e) => {
            const u = ((e) => {
                const u = te(),
                  t = u.caller,
                  n = u.resId,
                  r = window.__feature && window.__feature !== t && t ? `subViews.${t}` : "";
                return { modelPrefix: r, modelPath: ae(r, e || ""), resId: n };
              })(),
              t = u.modelPrefix,
              n = e.split(".");
            if (n.length > 0) {
              const e = [n[0]];
              return (
                n.reduce((u, n) => {
                  const r = ne(ae(t, `${u}.${n}`), window);
                  return re(r) ? (e.push(r.id), `${u}.${n}.value`) : (e.push(n), `${u}.${n}`);
                }),
                e.reduce((e, u) => e + "." + u)
              );
            }
            return "";
          },
          ie = J.Sw.instance;
        let le;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(le || (le = {}));
        const ce = (e = "model", u = le.Deep) => {
            const t = (0, o.useState)(0),
              n = (t[0], t[1]),
              r = (0, o.useMemo)(() => te(), []),
              a = r.caller,
              s = r.resId,
              i = (0, o.useMemo)(
                () => (window.__feature && window.__feature !== a ? `subViews.${a}.${e}` : e),
                [a, e],
              ),
              l = (0, o.useState)(() =>
                ((e) => {
                  const u = ne(e, window);
                  for (const e in u) "function" == typeof u[e] && (u[e] = u[e].bind(u));
                  return re(u) ? u.value : u;
                })(oe(i)),
              ),
              c = l[0],
              _ = l[1],
              d = (0, o.useRef)(-1);
            return (
              D(() => {
                if (
                  ("boolean" == typeof u &&
                    ((u = u ? le.Deep : le.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  u !== le.None)
                ) {
                  const t = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      u === le.Deep
                        ? (e === c && n((e) => e + 1), _(e))
                        : _(Object.assign([], e));
                    },
                    r = se(e);
                  d.current = ie.addCallback(r, t, s, u === le.Deep);
                }
              }),
              (0, o.useEffect)(() => {
                if (u !== le.None)
                  return () => {
                    ie.removeCallback(d.current, s);
                  };
              }, [s, u]),
              c
            );
          },
          _e = () => {
            const e = (0, o.useState)(a.O.view.getScale()),
              u = e[0],
              t = e[1];
            return (
              (0, o.useEffect)(() => {
                const e = () => {
                  t(a.O.view.getScale());
                };
                return (
                  window.addEventListener("resize", e),
                  () => {
                    window.removeEventListener("resize", e);
                  }
                );
              }, []),
              u
            );
          };
        function de() {}
        console.log;
        let Ee, me;
        (!(function (e) {
          e[(e.W_2048 = 2048)] = "W_2048";
        })(Ee || (Ee = {})),
          (function (e) {
            e[(e.H_1536 = 1536)] = "H_1536";
          })(me || (me = {})));
        const Ae = (e) => {
          const u = x(),
            t = u.remScreenWidth,
            n = u.remScreenHeight,
            r = Math.floor(w.Large / e),
            a = Math.floor(Ee.W_2048 / e),
            o = Math.floor(me.H_1536 / e),
            s = Math.floor(w.ExtraLarge / e),
            i = n === Math.floor(y.ExtraLarge / e);
          return (
            (t === r && i && 1.5 === e) ||
            (t === a && n === o && 1.5 === e) ||
            (t === s && i && 1.75 === e)
          );
        };
        function Fe(e) {
          engine.call("PlaySound", e);
        }
        const ge = {
            base: "TextButton_base_b6",
            base__right: "TextButton_base__right_39",
            icon: "TextButton_icon_17",
            icon__back: "TextButton_icon__back_43",
            icon__forward: "TextButton_icon__forward_59",
            icon__close: "TextButton_icon__close_53",
            icon__info: "TextButton_icon__info_33",
            glow: "TextButton_glow_a4",
            caption: "TextButton_caption_82",
            caption__back: "TextButton_caption__back_b9",
            caption__forward: "TextButton_caption__forward_4e",
            caption__close: "TextButton_caption__close_36",
            caption__info: "TextButton_caption__info_23",
            goto: "TextButton_goto_e7",
            base__left: "TextButton_base__left_ff",
            shine: "TextButton_shine_e2",
          },
          Ce = [
            "caption",
            "onClick",
            "goto",
            "side",
            "type",
            "classNames",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onMouseUp",
            "soundClick",
            "soundHover",
          ];
        function De() {
          return (
            (De =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            De.apply(this, arguments)
          );
        }
        class he extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && Fe(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && Fe(this.props.soundClick));
              }),
              (this._onMouseUp = (e) => (u) => {
                (e && e(u), this.setState({ click: !1 }));
              }),
              (this.handleFocus = () => this.setState({ focus: !0 })),
              (this.handleBlur = () => this.setState({ focus: !1 })));
          }
          render() {
            const e = this.props,
              u = e.caption,
              t = e.onClick,
              n = e.goto,
              r = e.side,
              a = e.type,
              o = e.classNames,
              i = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              _ = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    r = {},
                    a = Object.keys(e);
                  for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(e, Ce)),
              E = p()(ge.base, ge[`base__${a}`], ge[`base__${r}`], null == o ? void 0 : o.base),
              m = p()(ge.icon, ge[`icon__${a}`], ge[`icon__${r}`], null == o ? void 0 : o.icon),
              A = p()(ge.glow, null == o ? void 0 : o.glow),
              F = p()(ge.caption, ge[`caption__${a}`], null == o ? void 0 : o.caption),
              g = p()(ge.goto, null == o ? void 0 : o.goto);
            return s().createElement(
              "div",
              De(
                {
                  className: E,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                d,
              ),
              "info" !== a && s().createElement("div", { className: ge.shine }),
              s().createElement(
                "div",
                { className: m },
                s().createElement("div", { className: A }),
              ),
              s().createElement("div", { className: F }, u),
              n && s().createElement("div", { className: g }, n),
            );
          }
        }
        he.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const Be = "BackButton_base_a6",
          pe = "BackButton_base__left_75",
          ve = "BackButton_base__right_db",
          fe = "BackButton_base__scaled_19",
          be = ({ onClick: e }) => {
            const u = ce("model.style", le.None).isProlongStyleRent,
              t = _e(),
              n = Ae(t);
            if (u) {
              const u = p()(Be, ve);
              return s().createElement(
                "div",
                { className: u },
                s().createElement(he, {
                  caption: R.strings.menu.viewHeader.closeBtn.label(),
                  type: "close",
                  side: "right",
                  onClick: e,
                }),
              );
            }
            const r = p()(Be, pe, n && fe);
            return s().createElement(
              "div",
              { className: r },
              s().createElement(he, {
                caption: R.strings.menu.viewHeader.backBtn.label(),
                onClick: e,
              }),
            );
          },
          we = {
            base: "CButton_base_40",
            base__main: "CButton_base__main_42",
            base__primary: "CButton_base__primary_7f",
            base__primaryGreen: "CButton_base__primaryGreen_6f",
            base__primaryRed: "CButton_base__primaryRed_ec",
            base__secondary: "CButton_base__secondary_50",
            base__ghost: "CButton_base__ghost_ed",
            base__extraSmall: "CButton_base__extraSmall_27",
            base__small: "CButton_base__small_df",
            base__medium: "CButton_base__medium_74",
            base__disabled: "CButton_base__disabled_d9",
            back: "CButton_back_e5",
            texture: "CButton_texture_fe",
            state: "CButton_state_11",
            base__focus: "CButton_base__focus_83",
            stateHighlightHover: "CButton_stateHighlightHover_ff",
            stateHighlightActive: "CButton_stateHighlightActive_35",
            stateDisabled: "CButton_stateDisabled_54",
            base__firstHover: "CButton_base__firstHover_d5",
            base__highlightActive: "CButton_base__highlightActive_b2",
            content: "CButton_content_cc",
          };
        let ye, xe;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(ye || (ye = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(xe || (xe = {})));
        const Se = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: r,
          mixClass: a,
          soundHover: i,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: _,
          onMouseDown: d,
          onMouseUp: E,
          onMouseLeave: m,
          onClick: A,
        }) => {
          const F = (0, o.useRef)(null),
            g = (0, o.useState)(t),
            C = g[0],
            D = g[1],
            h = (0, o.useState)(!1),
            B = h[0],
            v = h[1],
            f = (0, o.useState)(!1),
            b = f[0],
            w = f[1],
            y = (0, o.useCallback)(() => {
              r || (F.current && (F.current.focus(), D(!0)));
            }, [r]),
            x = (0, o.useCallback)(
              (e) => {
                C && null !== F.current && !F.current.contains(e.target) && D(!1);
              },
              [C],
            ),
            S = (0, o.useCallback)(
              (e) => {
                r || (A && A(e));
              },
              [r, A],
            ),
            L = (0, o.useCallback)(
              (e) => {
                r || (null !== i && Fe(i), c && c(e), w(!0));
              },
              [r, i, c],
            ),
            M = (0, o.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            k = (0, o.useCallback)(
              (e) => {
                r || (E && E(e), v(!1));
              },
              [r, E],
            ),
            N = (0, o.useCallback)(
              (e) => {
                r || (null !== l && Fe(l), d && d(e), t && y(), v(!0));
              },
              [r, l, d, y, t],
            ),
            T = (0, o.useCallback)(
              (e) => {
                r || (m && m(e), v(!1));
              },
              [r, m],
            ),
            P = p()(
              we.base,
              we[`base__${n}`],
              {
                [we.base__disabled]: r,
                [we[`base__${u}`]]: u,
                [we.base__focus]: C,
                [we.base__highlightActive]: B,
                [we.base__firstHover]: b,
              },
              a,
            ),
            O = p()(we.state, we.state__default);
          return (
            (0, o.useEffect)(
              () => (
                document.addEventListener("mousedown", x),
                () => {
                  document.removeEventListener("mousedown", x);
                }
              ),
              [x],
            ),
            (0, o.useEffect)(() => {
              D(t);
            }, [t]),
            s().createElement(
              "div",
              {
                ref: F,
                className: P,
                onMouseEnter: L,
                onMouseMove: M,
                onMouseUp: k,
                onMouseDown: N,
                onMouseLeave: T,
                onClick: S,
              },
              n !== ye.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: we.back }),
                  s().createElement("span", { className: we.texture }),
                ),
              s().createElement(
                "span",
                { className: O },
                s().createElement("span", { className: we.stateDisabled }),
                s().createElement("span", { className: we.stateHighlightHover }),
                s().createElement("span", { className: we.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: we.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Se.defaultProps = {
          type: ye.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Le = (0, o.memo)(Se);
        let Me;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(Me || (Me = {}));
        const ke = {
          base: "Checkbox_base_36",
          base__disabled: "Checkbox_base__disabled_08",
          base__center: "Checkbox_base__center_52",
          base__bottom: "Checkbox_base__bottom_28",
          input: "Checkbox_input_37",
          base__mouseDown: "Checkbox_base__mouseDown_45",
          base__small: "Checkbox_base__small_18",
          base__medium: "Checkbox_base__medium_12",
          base__large: "Checkbox_base__large_f7",
          base__extraLarge: "Checkbox_base__extraLarge_c9",
          alertOverlay: "Checkbox_alertOverlay_52",
          base__alert: "Checkbox_base__alert_b7",
          blink: "Checkbox_blink_5e",
          base__checked: "Checkbox_base__checked_a2",
          inputHoverOverlay: "Checkbox_inputHoverOverlay_36",
          highlight: "Checkbox_highlight_b8",
          base__main: "Checkbox_base__main_3a",
          base__primary: "Checkbox_base__primary_ab",
          checkmark: "Checkbox_checkmark_60",
          fadeIn: "Checkbox_fadeIn_1a",
          label: "Checkbox_label_bc",
          labelContent: "Checkbox_labelContent_64",
        };
        let Ne, Te, Pe;
        (!(function (e) {
          ((e.small = "small"),
            (e.medium = "medium"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(Ne || (Ne = {})),
          (function (e) {
            ((e.primary = "primary"), (e.main = "main"));
          })(Te || (Te = {})),
          (function (e) {
            ((e.Center = "center"), (e.Bottom = "bottom"));
          })(Pe || (Pe = {})));
        const Re = [
          "id",
          "isChecked",
          "isDisabled",
          "isAlert",
          "size",
          "type",
          "soundHover",
          "soundClick",
          "onMouseEnter",
          "onMouseLeave",
          "onMouseUp",
          "onMouseDown",
          "onClick",
          "onChange",
          "onFocus",
          "onBlur",
          "text",
          "contentStyles",
          "children",
          "alignment",
        ];
        function Oe() {
          return (
            (Oe =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Oe.apply(this, arguments)
          );
        }
        const He = (e) => {
          let u = e.id,
            t = e.isChecked,
            n = void 0 !== t && t,
            r = e.isDisabled,
            a = void 0 !== r && r,
            i = e.isAlert,
            l = void 0 !== i && i,
            c = e.size,
            _ = void 0 === c ? Ne.medium : c,
            d = e.type,
            E = void 0 === d ? Te.primary : d,
            m = e.soundHover,
            A = void 0 === m ? "highlight" : m,
            F = e.soundClick,
            g = void 0 === F ? "play" : F,
            C = e.onMouseEnter,
            D = e.onMouseLeave,
            h = e.onMouseUp,
            B = e.onMouseDown,
            v = e.onClick,
            f = e.onChange,
            b = e.onFocus,
            w = e.onBlur,
            y = e.text,
            x = e.contentStyles,
            S = e.children,
            L = e.alignment,
            M = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                r = {},
                a = Object.keys(e);
              for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, Re);
          const k = (0, o.useState)(!1),
            N = k[0],
            T = k[1],
            P = (0, o.useState)(!1),
            R = (P[0], P[1]),
            O = (0, o.useCallback)(
              (e) => {
                a || (f && f(), v && v(e));
              },
              [a, f, v],
            ),
            H = (0, o.useCallback)(
              (e) => {
                const u = e.button === Me.LEFT;
                a || (u && T(!0), u && B && B(e), g && Fe(g));
              },
              [a, B, g],
            ),
            I = (0, o.useCallback)(
              (e) => {
                a || (T(!1), h && h(e));
              },
              [a, h],
            ),
            W = (0, o.useCallback)(
              (e) => {
                a || (C && C(e), A && Fe(A));
              },
              [a, C, A],
            ),
            z = (0, o.useCallback)(
              (e) => {
                a || (T(!1), D && D(e));
              },
              [a, D],
            ),
            U = (0, o.useCallback)(
              (e) => {
                a || (R(!0), b && b(e));
              },
              [a, b],
            ),
            V = (0, o.useCallback)(
              (e) => {
                a || (R(!1), w && w(e));
              },
              [a, w],
            ),
            $ = s().createElement(
              "div",
              { className: ke.label },
              s().createElement(
                "div",
                { className: p()(ke.labelContent, "s-labelContent"), style: x },
                y || S,
              ),
            );
          return s().createElement(
            "div",
            Oe(
              {
                id: u,
                className: p()(ke.base, ke[`base__${_}`], ke[`base__${E}`], {
                  [ke.base__checked]: n,
                  [ke.base__disabled]: a,
                  [ke.base__mouseDown]: N,
                  [ke.base__alert]: l,
                  [ke.base__center]: L === Pe.Center,
                  [ke.base__bottom]: L === Pe.Bottom,
                }),
                onClick: O,
                onMouseEnter: W,
                onMouseLeave: z,
                onMouseDown: H,
                onMouseUp: I,
                onFocus: U,
                onBlur: V,
              },
              M,
            ),
            s().createElement(
              "div",
              { className: ke.input },
              s().createElement("div", { className: ke.alertOverlay }),
              s().createElement("div", { className: ke.inputHoverOverlay }),
              s().createElement("div", { className: ke.highlight }),
            ),
            s().createElement("div", { className: ke.checkmark }),
            ((y || S) && $) || null,
          );
        };
        let Ie, We, ze;
        (!(function (e) {
          ((e.small = "small"),
            (e.big = "big"),
            (e.large = "large"),
            (e.extraLarge = "extraLarge"));
        })(Ie || (Ie = {})),
          (function (e) {
            ((e.credits = "credits"),
              (e.gold = "gold"),
              (e.crystal = "crystal"),
              (e.xp = "xp"),
              (e.freeXP = "freeXP"),
              (e.equipCoin = "equipCoin"));
          })(We || (We = {})),
          (function (e) {
            ((e.Red = "RedActionBG"), (e.Blue = "BlueActionBG"));
          })(ze || (ze = {})));
        class Ue extends s().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = J.B3.GOLD;
            else e = J.B3.INTEGRAL;
            const u = J.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        Ue.defaultProps = { format: "integral" };
        const Ve = {
            base: "Currency_base_57",
            icon: "Currency_icon_c5",
            base__small: "Currency_base__small_af",
            base__big: "Currency_base__big_bc",
            base__large: "Currency_base__large_65",
            base__extraLarge: "Currency_base__extraLarge_4d",
            "icon__credits-small": "Currency_icon__credits-small_9b",
            "icon__credits-big": "Currency_icon__credits-big_96",
            "icon__credits-large": "Currency_icon__credits-large_ac",
            "icon__credits-extraLarge": "Currency_icon__credits-extraLarge_16",
            "icon__gold-small": "Currency_icon__gold-small_86",
            "icon__gold-big": "Currency_icon__gold-big_15",
            "icon__gold-large": "Currency_icon__gold-large_36",
            "icon__gold-extraLarge": "Currency_icon__gold-extraLarge_a0",
            "icon__crystal-small": "Currency_icon__crystal-small_27",
            "icon__crystal-big": "Currency_icon__crystal-big_cd",
            "icon__crystal-large": "Currency_icon__crystal-large_d3",
            "icon__crystal-extraLarge": "Currency_icon__crystal-extraLarge_09",
            "icon__xp-small": "Currency_icon__xp-small_a7",
            "icon__xp-big": "Currency_icon__xp-big_97",
            "icon__xp-large": "Currency_icon__xp-large_6b",
            "icon__xp-extraLarge": "Currency_icon__xp-extraLarge_67",
            "icon__freeXP-small": "Currency_icon__freeXP-small_ca",
            "icon__freeXP-big": "Currency_icon__freeXP-big_21",
            "icon__freeXP-large": "Currency_icon__freeXP-large_c8",
            "icon__freeXP-extraLarge": "Currency_icon__freeXP-extraLarge_58",
            "icon__equipCoin-small": "Currency_icon__equipCoin-small_32",
            "icon__equipCoin-big": "Currency_icon__equipCoin-big_79",
            "icon__equipCoin-large": "Currency_icon__equipCoin-large_2c",
            "icon__equipCoin-extraLarge": "Currency_icon__equipCoin-extraLarge_8a",
            value: "Currency_value_e1",
            value__freeXP: "Currency_value__freeXP_cb",
            value__credits: "Currency_value__credits_76",
            value__gold: "Currency_value__gold_dd",
            value__xp: "Currency_value__xp_b0",
            value__crystal: "Currency_value__crystal_19",
            value__equipCoin: "Currency_value__equipCoin_d0",
            value__notEnough: "Currency_value__notEnough_56",
            stock: "Currency_stock_87",
            stock__indent: "Currency_stock__indent_a1",
            stock__interactive: "Currency_stock__interactive_93",
            stockBackground: "Currency_stockBackground_82",
          },
          $e = ({
            isDiscount: e,
            isInteractiveDiscount: u,
            size: t,
            type: n,
            isEnough: r,
            value: a,
            discountValue: o,
            showPlus: i,
            stockBackgroundName: l = ze.Red,
          }) => {
            const c = p()(Ve.value, Ve[`value__${n}`], !r && Ve.value__notEnough),
              _ = p()(Ve.icon, Ve[`icon__${n}-${t}`]),
              d = p()(Ve.stock, o && Ve.stock__indent, u && Ve.stock__interactive),
              E = i && a > 0 && "+",
              m = p()(Ve.base, Ve[`base__${t}`]);
            return s().createElement(
              "span",
              { className: m },
              s().createElement(
                "span",
                { className: c },
                E,
                s().createElement(Ue, { value: a, format: n === We.gold ? "gold" : "integral" }),
              ),
              s().createElement("span", { className: _ }),
              e &&
                s().createElement(
                  "span",
                  { className: d },
                  s().createElement("span", {
                    className: Ve.stockBackground,
                    style: { backgroundImage: `url(R.images.gui.maps.icons.library.${l})` },
                  }),
                  Boolean(o) && o,
                ),
            );
          };
        $e.defaultProps = { isEnough: !0 };
        const Ge = s().memo($e),
          je = [
            "children",
            "contentId",
            "args",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onClick",
            "ignoreShowDelay",
            "ignoreMouseClick",
            "decoratorId",
            "isEnabled",
            "targetId",
            "onShow",
            "onHide",
          ];
        function qe(e) {
          return Object.entries(e || {}).map(([e, u]) => {
            const t = { __Type: "GFValueProxy", name: e };
            switch (typeof u) {
              case "number":
                t.number = u;
                break;
              case "boolean":
                t.bool = u;
                break;
              case "undefined":
                break;
              default:
                t.string = u.toString();
            }
            return t;
          });
        }
        const Ke = (e, u, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: J.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: n,
                },
                t,
              ),
            );
          },
          Ye = (e) => {
            let u = e.children,
              t = e.contentId,
              n = e.args,
              r = e.onMouseEnter,
              a = e.onMouseLeave,
              s = e.onMouseDown,
              i = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              _ = e.ignoreMouseClick,
              d = void 0 !== _ && _,
              E = e.decoratorId,
              m = void 0 === E ? 0 : E,
              A = e.isEnabled,
              F = void 0 === A || A,
              g = e.targetId,
              C = void 0 === g ? 0 : g,
              D = e.onShow,
              h = e.onHide,
              B = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, je);
            const p = (0, o.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              v = (0, o.useMemo)(() => C || te().resId, [C]),
              f = (0, o.useCallback)(() => {
                (p.current.isVisible && p.current.timeoutId) ||
                  (Ke(t, m, { isMouseEvent: !0, on: !0, arguments: qe(n) }, v),
                  D && D(),
                  (p.current.isVisible = !0));
              }, [t, m, n, v, D]),
              b = (0, o.useCallback)(() => {
                if (p.current.isVisible || p.current.timeoutId) {
                  const e = p.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (p.current.timeoutId = 0)),
                    Ke(t, m, { on: !1 }, v),
                    p.current.isVisible && h && h(),
                    (p.current.isVisible = !1));
                }
              }, [t, m, v, h]),
              w = (0, o.useCallback)((e) => {
                p.current.isVisible &&
                  ((p.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (p.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(p.current.prevTarget) && b();
                  }, 200)));
              }, []);
            ((0, o.useEffect)(() => {
              const e = p.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, o.useEffect)(() => {
                !1 === F && b();
              }, [F, b]),
              (0, o.useEffect)(
                () => (
                  window.addEventListener("mouseleave", b),
                  () => {
                    (window.removeEventListener("mouseleave", b), b());
                  }
                ),
                [b],
              ));
            return F
              ? (0, o.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((y = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((p.current.timeoutId = window.setTimeout(f, c ? 100 : 400)),
                            r && r(e),
                            y && y(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (b(), null == a || a(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === d && b(), null == i || i(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === d && b(), null == s || s(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    B,
                  ),
                )
              : u;
            var y;
          },
          Xe = ["children"];
        function Ze() {
          return (
            (Ze =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Ze.apply(this, arguments)
          );
        }
        const Qe = (e) => {
            let u = e.children,
              t = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  r = {},
                  a = Object.keys(e);
                for (n = 0; n < a.length; n++) ((t = a[n]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Xe);
            return s().createElement(
              Ye,
              Ze(
                {
                  contentId:
                    R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                      "resId",
                    ),
                  ignoreShowDelay: !0,
                },
                t,
              ),
              u,
            );
          },
          Je = "Tutorial_tutorial_ce",
          eu = "Tutorial_tutorial_border_ab",
          uu = "Tutorial_tutorial__hidden_8a",
          tu = "Tutorial_tutorial_hint_bc",
          nu = "Tutorial_tutorial_hintSubstrate_c7",
          ru = "Tutorial_tutorial_hintArrow_75",
          au = "Tutorial_tutorial_hintText_b5";
        class ou extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.onClick = () => {
                !this.props.isHidden && this.props.onClick && this.props.onClick();
              }));
          }
          componentDidMount() {
            this.handlerID = document.addEventListener("click", () => {
              this.props.onCancel && this.props.onCancel();
            });
          }
          componentWillUnmount() {
            document.removeEventListener("click", this.handlerID);
          }
          render() {
            const e = p()(Je, { [uu]: this.props.isHidden });
            return s().createElement(
              "div",
              { className: e, onClick: this.onClick },
              s().createElement("div", { className: eu }),
              s().createElement(
                "div",
                { className: tu },
                s().createElement("div", { className: nu }),
                s().createElement("div", { className: ru }),
                s().createElement("div", { className: au }, this.props.text),
              ),
            );
          }
        }
        const su = "gold";
        class iu {
          constructor(e = null) {
            ((this._prices = []), null !== e && null !== e.prices && (this._prices = e.prices));
          }
          get length() {
            return null !== this._prices ? this._prices.length : 0;
          }
          isEmpty(e = 0) {
            return 0 === this.getValue(e);
          }
          hasDiscount(e = 0) {
            return this.getDiscountValue(e) > 0;
          }
          getType(e = 0) {
            const u = this._prices[e];
            return u ? this._getPriceItemType(u.value.price) : "";
          }
          getValue(e = 0) {
            const u = this._prices[e];
            return u ? this._getPriceItemValue(u.value.price) : 0;
          }
          getDefValue(e = 0) {
            const u = this._prices[e];
            return u ? this._getPriceItemValue(u.value.defPrice) : 0;
          }
          getDiscountValue(e = 0) {
            const u = this._prices[e];
            return u ? this._getPriceItemValue(u.value.discount) : 0;
          }
          _getPriceItemType(e) {
            let u = "";
            return e.some((e) => ((u = e.value.name), e.value.value > 0)) ? u : "";
          }
          _getPriceItemValue(e) {
            let u = 0;
            return e.some((e) => ((u = e.value.value), u > 0)) ? u : 0;
          }
        }
        let lu;
        function cu(e, u) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const t = 0 === e.indexOf("%") ? 2 : 1;
            return String(u[e.slice(t, -t)]);
          });
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(lu || (lu = {}));
        (() => {
          const e = new RegExp(
            /[\(\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?[ %\+\x2D-9A-Za-\{\}\xA0\xC0-\u0237\u2013\u2014\u2026]+[\)\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3002\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\uFF01\uFF0C\uFF1A\uFF1B\uFF1F\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?/gmu
              .source +
              "|" +
              /[\(\xAB\u201C\u275D][\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}][\0-\u2E7F\u2E9A\u2EF4-\u2EFF\u2FD6-\u3004\u3006\u3008-\u3020\u302A-\u3037\u303C-\u33FF\u4DC0-\u4DFF\uA000-\uF8FF\uFA6E\uFA6F\uFADA-\u{16FE1}\u{16FE4}-\u{16FEF}\u{16FF2}-\u{1FFFF}\u{2A6E0}-\u{2A6FF}\u{2B739}-\u{2B73F}\u{2B81E}\u{2B81F}\u{2CEA2}-\u{2CEAF}\u{2EBE1}-\u{2F7FF}\u{2FA1E}-\u{2FFFF}\u{3134B}-\u{10FFFF}]?|[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}][\0-\u2E7F\u2E9A\u2EF4-\u2EFF\u2FD6-\u3004\u3006\u3008-\u3020\u302A-\u3037\u303C-\u33FF\u4DC0-\u4DFF\uA000-\uF8FF\uFA6E\uFA6F\uFADA-\u{16FE1}\u{16FE4}-\u{16FEF}\u{16FF2}-\u{1FFFF}\u{2A6E0}-\u{2A6FF}\u{2B739}-\u{2B73F}\u{2B81E}\u{2B81F}\u{2CEA2}-\u{2CEAF}\u{2EBE1}-\u{2F7FF}\u{2FA1E}-\u{2FFFF}\u{3134B}-\u{10FFFF}]?[\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?[\)\xBB\u201D\u275E][\u3002\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]?/gmu
                .source +
              "|" +
              /[A-Za-z\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u052F\u0531-\u0556\u0559\u0560-\u0588\u05D0-\u05EA\u05EF-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u0860-\u086A\u0870-\u0887\u0889-\u088E\u08A0-\u08C9\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u09FC\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0AF9\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D\u0C58-\u0C5A\u0C5D\u0C60\u0C61\u0C80\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D04-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D54-\u0D56\u0D5F-\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E86-\u0E8A\u0E8C-\u0EA3\u0EA5\u0EA7-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F5\u13F8-\u13FD\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16F1-\u16F8\u1700-\u1711\u171F-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1878\u1880-\u1884\u1887-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191E\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19B0-\u19C9\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4C\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1C80-\u1C88\u1C90-\u1CBA\u1CBD-\u1CBF\u1CE9-\u1CEC\u1CEE-\u1CF3\u1CF5\u1CF6\u1CFA\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2183\u2184\u2C00-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005\u3006\u3031-\u3035\u303B\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312F\u3131-\u318E\u31A0-\u31BF\u31F0-\u31FF\u3400-\u4DBF\u4E00-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA69D\uA6A0-\uA6E5\uA717-\uA71F\uA722-\uA788\uA78B-\uA7CA\uA7D0\uA7D1\uA7D3\uA7D5-\uA7D9\uA7F2-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA8FD\uA8FE\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uA9E0-\uA9E4\uA9E6-\uA9EF\uA9FA-\uA9FE\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA7E-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB69\uAB70-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC\u{10000}-\u{1000B}\u{1000D}-\u{10026}\u{10028}-\u{1003A}\u{1003C}\u{1003D}\u{1003F}-\u{1004D}\u{10050}-\u{1005D}\u{10080}-\u{100FA}\u{10280}-\u{1029C}\u{102A0}-\u{102D0}\u{10300}-\u{1031F}\u{1032D}-\u{10340}\u{10342}-\u{10349}\u{10350}-\u{10375}\u{10380}-\u{1039D}\u{103A0}-\u{103C3}\u{103C8}-\u{103CF}\u{10400}-\u{1049D}\u{104B0}-\u{104D3}\u{104D8}-\u{104FB}\u{10500}-\u{10527}\u{10530}-\u{10563}\u{10570}-\u{1057A}\u{1057C}-\u{1058A}\u{1058C}-\u{10592}\u{10594}\u{10595}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10600}-\u{10736}\u{10740}-\u{10755}\u{10760}-\u{10767}\u{10780}-\u{10785}\u{10787}-\u{107B0}\u{107B2}-\u{107BA}\u{10800}-\u{10805}\u{10808}\u{1080A}-\u{10835}\u{10837}\u{10838}\u{1083C}\u{1083F}-\u{10855}\u{10860}-\u{10876}\u{10880}-\u{1089E}\u{108E0}-\u{108F2}\u{108F4}\u{108F5}\u{10900}-\u{10915}\u{10920}-\u{10939}\u{10980}-\u{109B7}\u{109BE}\u{109BF}\u{10A00}\u{10A10}-\u{10A13}\u{10A15}-\u{10A17}\u{10A19}-\u{10A35}\u{10A60}-\u{10A7C}\u{10A80}-\u{10A9C}\u{10AC0}-\u{10AC7}\u{10AC9}-\u{10AE4}\u{10B00}-\u{10B35}\u{10B40}-\u{10B55}\u{10B60}-\u{10B72}\u{10B80}-\u{10B91}\u{10C00}-\u{10C48}\u{10C80}-\u{10CB2}\u{10CC0}-\u{10CF2}\u{10D00}-\u{10D23}\u{10E80}-\u{10EA9}\u{10EB0}\u{10EB1}\u{10F00}-\u{10F1C}\u{10F27}\u{10F30}-\u{10F45}\u{10F70}-\u{10F81}\u{10FB0}-\u{10FC4}\u{10FE0}-\u{10FF6}\u{11003}-\u{11037}\u{11071}\u{11072}\u{11075}\u{11083}-\u{110AF}\u{110D0}-\u{110E8}\u{11103}-\u{11126}\u{11144}\u{11147}\u{11150}-\u{11172}\u{11176}\u{11183}-\u{111B2}\u{111C1}-\u{111C4}\u{111DA}\u{111DC}\u{11200}-\u{11211}\u{11213}-\u{1122B}\u{11280}-\u{11286}\u{11288}\u{1128A}-\u{1128D}\u{1128F}-\u{1129D}\u{1129F}-\u{112A8}\u{112B0}-\u{112DE}\u{11305}-\u{1130C}\u{1130F}\u{11310}\u{11313}-\u{11328}\u{1132A}-\u{11330}\u{11332}\u{11333}\u{11335}-\u{11339}\u{1133D}\u{11350}\u{1135D}-\u{11361}\u{11400}-\u{11434}\u{11447}-\u{1144A}\u{1145F}-\u{11461}\u{11480}-\u{114AF}\u{114C4}\u{114C5}\u{114C7}\u{11580}-\u{115AE}\u{115D8}-\u{115DB}\u{11600}-\u{1162F}\u{11644}\u{11680}-\u{116AA}\u{116B8}\u{11700}-\u{1171A}\u{11740}-\u{11746}\u{11800}-\u{1182B}\u{118A0}-\u{118DF}\u{118FF}-\u{11906}\u{11909}\u{1190C}-\u{11913}\u{11915}\u{11916}\u{11918}-\u{1192F}\u{1193F}\u{11941}\u{119A0}-\u{119A7}\u{119AA}-\u{119D0}\u{119E1}\u{119E3}\u{11A00}\u{11A0B}-\u{11A32}\u{11A3A}\u{11A50}\u{11A5C}-\u{11A89}\u{11A9D}\u{11AB0}-\u{11AF8}\u{11C00}-\u{11C08}\u{11C0A}-\u{11C2E}\u{11C40}\u{11C72}-\u{11C8F}\u{11D00}-\u{11D06}\u{11D08}\u{11D09}\u{11D0B}-\u{11D30}\u{11D46}\u{11D60}-\u{11D65}\u{11D67}\u{11D68}\u{11D6A}-\u{11D89}\u{11D98}\u{11EE0}-\u{11EF2}\u{11FB0}\u{12000}-\u{12399}\u{12480}-\u{12543}\u{12F90}-\u{12FF0}\u{13000}-\u{1342E}\u{14400}-\u{14646}\u{16800}-\u{16A38}\u{16A40}-\u{16A5E}\u{16A70}-\u{16ABE}\u{16AD0}-\u{16AED}\u{16B00}-\u{16B2F}\u{16B40}-\u{16B43}\u{16B63}-\u{16B77}\u{16B7D}-\u{16B8F}\u{16E40}-\u{16E7F}\u{16F00}-\u{16F4A}\u{16F50}\u{16F93}-\u{16F9F}\u{16FE0}\u{16FE1}\u{16FE3}\u{17000}-\u{187F7}\u{18800}-\u{18CD5}\u{18D00}-\u{18D08}\u{1AFF0}-\u{1AFF3}\u{1AFF5}-\u{1AFFB}\u{1AFFD}\u{1AFFE}\u{1B000}-\u{1B122}\u{1B150}-\u{1B152}\u{1B164}-\u{1B167}\u{1B170}-\u{1B2FB}\u{1BC00}-\u{1BC6A}\u{1BC70}-\u{1BC7C}\u{1BC80}-\u{1BC88}\u{1BC90}-\u{1BC99}\u{1D400}-\u{1D454}\u{1D456}-\u{1D49C}\u{1D49E}\u{1D49F}\u{1D4A2}\u{1D4A5}\u{1D4A6}\u{1D4A9}-\u{1D4AC}\u{1D4AE}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D505}\u{1D507}-\u{1D50A}\u{1D50D}-\u{1D514}\u{1D516}-\u{1D51C}\u{1D51E}-\u{1D539}\u{1D53B}-\u{1D53E}\u{1D540}-\u{1D544}\u{1D546}\u{1D54A}-\u{1D550}\u{1D552}-\u{1D6A5}\u{1D6A8}-\u{1D6C0}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6FA}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D734}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D76E}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D7A8}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7CB}\u{1DF00}-\u{1DF1E}\u{1E100}-\u{1E12C}\u{1E137}-\u{1E13D}\u{1E14E}\u{1E290}-\u{1E2AD}\u{1E2C0}-\u{1E2EB}\u{1E7E0}-\u{1E7E6}\u{1E7E8}-\u{1E7EB}\u{1E7ED}\u{1E7EE}\u{1E7F0}-\u{1E7FE}\u{1E800}-\u{1E8C4}\u{1E900}-\u{1E943}\u{1E94B}\u{1EE00}-\u{1EE03}\u{1EE05}-\u{1EE1F}\u{1EE21}\u{1EE22}\u{1EE24}\u{1EE27}\u{1EE29}-\u{1EE32}\u{1EE34}-\u{1EE37}\u{1EE39}\u{1EE3B}\u{1EE42}\u{1EE47}\u{1EE49}\u{1EE4B}\u{1EE4D}-\u{1EE4F}\u{1EE51}\u{1EE52}\u{1EE54}\u{1EE57}\u{1EE59}\u{1EE5B}\u{1EE5D}\u{1EE5F}\u{1EE61}\u{1EE62}\u{1EE64}\u{1EE67}-\u{1EE6A}\u{1EE6C}-\u{1EE72}\u{1EE74}-\u{1EE77}\u{1EE79}-\u{1EE7C}\u{1EE7E}\u{1EE80}-\u{1EE89}\u{1EE8B}-\u{1EE9B}\u{1EEA1}-\u{1EEA3}\u{1EEA5}-\u{1EEA9}\u{1EEAB}-\u{1EEBB}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]?[ \):;\u2022\u3001\u3002\u300A-\u300D\uFF01\uFF0C\uFF1A\uFF1B\uFF1F]|[\(,1A-Za-\{\}\xAA\xB5\xBA\xC0-\xD6\xD8-\xF6\xF8-\u02C1\u02C6-\u02D1\u02E0-\u02E4\u02EC\u02EE\u0370-\u0374\u0376\u0377\u037A-\u037D\u037F\u0386\u0388-\u038A\u038C\u038E-\u03A1\u03A3-\u03F5\u03F7-\u0481\u048A-\u052F\u0531-\u0556\u0559\u0560-\u0588\u05D0-\u05EA\u05EF-\u05F2\u0620-\u064A\u066E\u066F\u0671-\u06D3\u06D5\u06E5\u06E6\u06EE\u06EF\u06FA-\u06FC\u06FF\u0710\u0712-\u072F\u074D-\u07A5\u07B1\u07CA-\u07EA\u07F4\u07F5\u07FA\u0800-\u0815\u081A\u0824\u0828\u0840-\u0858\u0860-\u086A\u0870-\u0887\u0889-\u088E\u08A0-\u08C9\u0904-\u0939\u093D\u0950\u0958-\u0961\u0971-\u0980\u0985-\u098C\u098F\u0990\u0993-\u09A8\u09AA-\u09B0\u09B2\u09B6-\u09B9\u09BD\u09CE\u09DC\u09DD\u09DF-\u09E1\u09F0\u09F1\u09FC\u0A05-\u0A0A\u0A0F\u0A10\u0A13-\u0A28\u0A2A-\u0A30\u0A32\u0A33\u0A35\u0A36\u0A38\u0A39\u0A59-\u0A5C\u0A5E\u0A72-\u0A74\u0A85-\u0A8D\u0A8F-\u0A91\u0A93-\u0AA8\u0AAA-\u0AB0\u0AB2\u0AB3\u0AB5-\u0AB9\u0ABD\u0AD0\u0AE0\u0AE1\u0AF9\u0B05-\u0B0C\u0B0F\u0B10\u0B13-\u0B28\u0B2A-\u0B30\u0B32\u0B33\u0B35-\u0B39\u0B3D\u0B5C\u0B5D\u0B5F-\u0B61\u0B71\u0B83\u0B85-\u0B8A\u0B8E-\u0B90\u0B92-\u0B95\u0B99\u0B9A\u0B9C\u0B9E\u0B9F\u0BA3\u0BA4\u0BA8-\u0BAA\u0BAE-\u0BB9\u0BD0\u0C05-\u0C0C\u0C0E-\u0C10\u0C12-\u0C28\u0C2A-\u0C39\u0C3D\u0C58-\u0C5A\u0C5D\u0C60\u0C61\u0C80\u0C85-\u0C8C\u0C8E-\u0C90\u0C92-\u0CA8\u0CAA-\u0CB3\u0CB5-\u0CB9\u0CBD\u0CDD\u0CDE\u0CE0\u0CE1\u0CF1\u0CF2\u0D04-\u0D0C\u0D0E-\u0D10\u0D12-\u0D3A\u0D3D\u0D4E\u0D54-\u0D56\u0D5F-\u0D61\u0D7A-\u0D7F\u0D85-\u0D96\u0D9A-\u0DB1\u0DB3-\u0DBB\u0DBD\u0DC0-\u0DC6\u0E01-\u0E30\u0E32\u0E33\u0E40-\u0E46\u0E81\u0E82\u0E84\u0E86-\u0E8A\u0E8C-\u0EA3\u0EA5\u0EA7-\u0EB0\u0EB2\u0EB3\u0EBD\u0EC0-\u0EC4\u0EC6\u0EDC-\u0EDF\u0F00\u0F40-\u0F47\u0F49-\u0F6C\u0F88-\u0F8C\u1000-\u102A\u103F\u1050-\u1055\u105A-\u105D\u1061\u1065\u1066\u106E-\u1070\u1075-\u1081\u108E\u10A0-\u10C5\u10C7\u10CD\u10D0-\u10FA\u10FC-\u1248\u124A-\u124D\u1250-\u1256\u1258\u125A-\u125D\u1260-\u1288\u128A-\u128D\u1290-\u12B0\u12B2-\u12B5\u12B8-\u12BE\u12C0\u12C2-\u12C5\u12C8-\u12D6\u12D8-\u1310\u1312-\u1315\u1318-\u135A\u1380-\u138F\u13A0-\u13F5\u13F8-\u13FD\u1401-\u166C\u166F-\u167F\u1681-\u169A\u16A0-\u16EA\u16F1-\u16F8\u1700-\u1711\u171F-\u1731\u1740-\u1751\u1760-\u176C\u176E-\u1770\u1780-\u17B3\u17D7\u17DC\u1820-\u1878\u1880-\u1884\u1887-\u18A8\u18AA\u18B0-\u18F5\u1900-\u191E\u1950-\u196D\u1970-\u1974\u1980-\u19AB\u19B0-\u19C9\u1A00-\u1A16\u1A20-\u1A54\u1AA7\u1B05-\u1B33\u1B45-\u1B4C\u1B83-\u1BA0\u1BAE\u1BAF\u1BBA-\u1BE5\u1C00-\u1C23\u1C4D-\u1C4F\u1C5A-\u1C7D\u1C80-\u1C88\u1C90-\u1CBA\u1CBD-\u1CBF\u1CE9-\u1CEC\u1CEE-\u1CF3\u1CF5\u1CF6\u1CFA\u1D00-\u1DBF\u1E00-\u1F15\u1F18-\u1F1D\u1F20-\u1F45\u1F48-\u1F4D\u1F50-\u1F57\u1F59\u1F5B\u1F5D\u1F5F-\u1F7D\u1F80-\u1FB4\u1FB6-\u1FBC\u1FBE\u1FC2-\u1FC4\u1FC6-\u1FCC\u1FD0-\u1FD3\u1FD6-\u1FDB\u1FE0-\u1FEC\u1FF2-\u1FF4\u1FF6-\u1FFC\u2071\u207F\u2090-\u209C\u2102\u2107\u210A-\u2113\u2115\u2119-\u211D\u2124\u2126\u2128\u212A-\u212D\u212F-\u2139\u213C-\u213F\u2145-\u2149\u214E\u2183\u2184\u2C00-\u2CE4\u2CEB-\u2CEE\u2CF2\u2CF3\u2D00-\u2D25\u2D27\u2D2D\u2D30-\u2D67\u2D6F\u2D80-\u2D96\u2DA0-\u2DA6\u2DA8-\u2DAE\u2DB0-\u2DB6\u2DB8-\u2DBE\u2DC0-\u2DC6\u2DC8-\u2DCE\u2DD0-\u2DD6\u2DD8-\u2DDE\u2E2F\u3005\u3006\u3031-\u3035\u303B\u303C\u3041-\u3096\u309D-\u309F\u30A1-\u30FA\u30FC-\u30FF\u3105-\u312F\u3131-\u318E\u31A0-\u31BF\u31F0-\u31FF\u3400-\u4DBF\u4E00-\uA48C\uA4D0-\uA4FD\uA500-\uA60C\uA610-\uA61F\uA62A\uA62B\uA640-\uA66E\uA67F-\uA69D\uA6A0-\uA6E5\uA717-\uA71F\uA722-\uA788\uA78B-\uA7CA\uA7D0\uA7D1\uA7D3\uA7D5-\uA7D9\uA7F2-\uA801\uA803-\uA805\uA807-\uA80A\uA80C-\uA822\uA840-\uA873\uA882-\uA8B3\uA8F2-\uA8F7\uA8FB\uA8FD\uA8FE\uA90A-\uA925\uA930-\uA946\uA960-\uA97C\uA984-\uA9B2\uA9CF\uA9E0-\uA9E4\uA9E6-\uA9EF\uA9FA-\uA9FE\uAA00-\uAA28\uAA40-\uAA42\uAA44-\uAA4B\uAA60-\uAA76\uAA7A\uAA7E-\uAAAF\uAAB1\uAAB5\uAAB6\uAAB9-\uAABD\uAAC0\uAAC2\uAADB-\uAADD\uAAE0-\uAAEA\uAAF2-\uAAF4\uAB01-\uAB06\uAB09-\uAB0E\uAB11-\uAB16\uAB20-\uAB26\uAB28-\uAB2E\uAB30-\uAB5A\uAB5C-\uAB69\uAB70-\uABE2\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFA6D\uFA70-\uFAD9\uFB00-\uFB06\uFB13-\uFB17\uFB1D\uFB1F-\uFB28\uFB2A-\uFB36\uFB38-\uFB3C\uFB3E\uFB40\uFB41\uFB43\uFB44\uFB46-\uFBB1\uFBD3-\uFD3D\uFD50-\uFD8F\uFD92-\uFDC7\uFDF0-\uFDFB\uFE70-\uFE74\uFE76-\uFEFC\uFF21-\uFF3A\uFF41-\uFF5A\uFF66-\uFFBE\uFFC2-\uFFC7\uFFCA-\uFFCF\uFFD2-\uFFD7\uFFDA-\uFFDC\u{10000}-\u{1000B}\u{1000D}-\u{10026}\u{10028}-\u{1003A}\u{1003C}\u{1003D}\u{1003F}-\u{1004D}\u{10050}-\u{1005D}\u{10080}-\u{100FA}\u{10280}-\u{1029C}\u{102A0}-\u{102D0}\u{10300}-\u{1031F}\u{1032D}-\u{10340}\u{10342}-\u{10349}\u{10350}-\u{10375}\u{10380}-\u{1039D}\u{103A0}-\u{103C3}\u{103C8}-\u{103CF}\u{10400}-\u{1049D}\u{104B0}-\u{104D3}\u{104D8}-\u{104FB}\u{10500}-\u{10527}\u{10530}-\u{10563}\u{10570}-\u{1057A}\u{1057C}-\u{1058A}\u{1058C}-\u{10592}\u{10594}\u{10595}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10600}-\u{10736}\u{10740}-\u{10755}\u{10760}-\u{10767}\u{10780}-\u{10785}\u{10787}-\u{107B0}\u{107B2}-\u{107BA}\u{10800}-\u{10805}\u{10808}\u{1080A}-\u{10835}\u{10837}\u{10838}\u{1083C}\u{1083F}-\u{10855}\u{10860}-\u{10876}\u{10880}-\u{1089E}\u{108E0}-\u{108F2}\u{108F4}\u{108F5}\u{10900}-\u{10915}\u{10920}-\u{10939}\u{10980}-\u{109B7}\u{109BE}\u{109BF}\u{10A00}\u{10A10}-\u{10A13}\u{10A15}-\u{10A17}\u{10A19}-\u{10A35}\u{10A60}-\u{10A7C}\u{10A80}-\u{10A9C}\u{10AC0}-\u{10AC7}\u{10AC9}-\u{10AE4}\u{10B00}-\u{10B35}\u{10B40}-\u{10B55}\u{10B60}-\u{10B72}\u{10B80}-\u{10B91}\u{10C00}-\u{10C48}\u{10C80}-\u{10CB2}\u{10CC0}-\u{10CF2}\u{10D00}-\u{10D23}\u{10E80}-\u{10EA9}\u{10EB0}\u{10EB1}\u{10F00}-\u{10F1C}\u{10F27}\u{10F30}-\u{10F45}\u{10F70}-\u{10F81}\u{10FB0}-\u{10FC4}\u{10FE0}-\u{10FF6}\u{11003}-\u{11037}\u{11071}\u{11072}\u{11075}\u{11083}-\u{110AF}\u{110D0}-\u{110E8}\u{11103}-\u{11126}\u{11144}\u{11147}\u{11150}-\u{11172}\u{11176}\u{11183}-\u{111B2}\u{111C1}-\u{111C4}\u{111DA}\u{111DC}\u{11200}-\u{11211}\u{11213}-\u{1122B}\u{11280}-\u{11286}\u{11288}\u{1128A}-\u{1128D}\u{1128F}-\u{1129D}\u{1129F}-\u{112A8}\u{112B0}-\u{112DE}\u{11305}-\u{1130C}\u{1130F}\u{11310}\u{11313}-\u{11328}\u{1132A}-\u{11330}\u{11332}\u{11333}\u{11335}-\u{11339}\u{1133D}\u{11350}\u{1135D}-\u{11361}\u{11400}-\u{11434}\u{11447}-\u{1144A}\u{1145F}-\u{11461}\u{11480}-\u{114AF}\u{114C4}\u{114C5}\u{114C7}\u{11580}-\u{115AE}\u{115D8}-\u{115DB}\u{11600}-\u{1162F}\u{11644}\u{11680}-\u{116AA}\u{116B8}\u{11700}-\u{1171A}\u{11740}-\u{11746}\u{11800}-\u{1182B}\u{118A0}-\u{118DF}\u{118FF}-\u{11906}\u{11909}\u{1190C}-\u{11913}\u{11915}\u{11916}\u{11918}-\u{1192F}\u{1193F}\u{11941}\u{119A0}-\u{119A7}\u{119AA}-\u{119D0}\u{119E1}\u{119E3}\u{11A00}\u{11A0B}-\u{11A32}\u{11A3A}\u{11A50}\u{11A5C}-\u{11A89}\u{11A9D}\u{11AB0}-\u{11AF8}\u{11C00}-\u{11C08}\u{11C0A}-\u{11C2E}\u{11C40}\u{11C72}-\u{11C8F}\u{11D00}-\u{11D06}\u{11D08}\u{11D09}\u{11D0B}-\u{11D30}\u{11D46}\u{11D60}-\u{11D65}\u{11D67}\u{11D68}\u{11D6A}-\u{11D89}\u{11D98}\u{11EE0}-\u{11EF2}\u{11FB0}\u{12000}-\u{12399}\u{12480}-\u{12543}\u{12F90}-\u{12FF0}\u{13000}-\u{1342E}\u{14400}-\u{14646}\u{16800}-\u{16A38}\u{16A40}-\u{16A5E}\u{16A70}-\u{16ABE}\u{16AD0}-\u{16AED}\u{16B00}-\u{16B2F}\u{16B40}-\u{16B43}\u{16B63}-\u{16B77}\u{16B7D}-\u{16B8F}\u{16E40}-\u{16E7F}\u{16F00}-\u{16F4A}\u{16F50}\u{16F93}-\u{16F9F}\u{16FE0}\u{16FE1}\u{16FE3}\u{17000}-\u{187F7}\u{18800}-\u{18CD5}\u{18D00}-\u{18D08}\u{1AFF0}-\u{1AFF3}\u{1AFF5}-\u{1AFFB}\u{1AFFD}\u{1AFFE}\u{1B000}-\u{1B122}\u{1B150}-\u{1B152}\u{1B164}-\u{1B167}\u{1B170}-\u{1B2FB}\u{1BC00}-\u{1BC6A}\u{1BC70}-\u{1BC7C}\u{1BC80}-\u{1BC88}\u{1BC90}-\u{1BC99}\u{1D400}-\u{1D454}\u{1D456}-\u{1D49C}\u{1D49E}\u{1D49F}\u{1D4A2}\u{1D4A5}\u{1D4A6}\u{1D4A9}-\u{1D4AC}\u{1D4AE}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D505}\u{1D507}-\u{1D50A}\u{1D50D}-\u{1D514}\u{1D516}-\u{1D51C}\u{1D51E}-\u{1D539}\u{1D53B}-\u{1D53E}\u{1D540}-\u{1D544}\u{1D546}\u{1D54A}-\u{1D550}\u{1D552}-\u{1D6A5}\u{1D6A8}-\u{1D6C0}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6FA}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D734}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D76E}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D7A8}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7CB}\u{1DF00}-\u{1DF1E}\u{1E100}-\u{1E12C}\u{1E137}-\u{1E13D}\u{1E14E}\u{1E290}-\u{1E2AD}\u{1E2C0}-\u{1E2EB}\u{1E7E0}-\u{1E7E6}\u{1E7E8}-\u{1E7EB}\u{1E7ED}\u{1E7EE}\u{1E7F0}-\u{1E7FE}\u{1E800}-\u{1E8C4}\u{1E900}-\u{1E943}\u{1E94B}\u{1EE00}-\u{1EE03}\u{1EE05}-\u{1EE1F}\u{1EE21}\u{1EE22}\u{1EE24}\u{1EE27}\u{1EE29}-\u{1EE32}\u{1EE34}-\u{1EE37}\u{1EE39}\u{1EE3B}\u{1EE42}\u{1EE47}\u{1EE49}\u{1EE4B}\u{1EE4D}-\u{1EE4F}\u{1EE51}\u{1EE52}\u{1EE54}\u{1EE57}\u{1EE59}\u{1EE5B}\u{1EE5D}\u{1EE5F}\u{1EE61}\u{1EE62}\u{1EE64}\u{1EE67}-\u{1EE6A}\u{1EE6C}-\u{1EE72}\u{1EE74}-\u{1EE77}\u{1EE79}-\u{1EE7C}\u{1EE7E}\u{1EE80}-\u{1EE89}\u{1EE8B}-\u{1EE9B}\u{1EEA1}-\u{1EEA3}\u{1EEA5}-\u{1EEA9}\u{1EEAB}-\u{1EEBB}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]/gmu
                .source +
              "|" +
              /[\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u3005\u3007\u3021-\u3029\u3038-\u303B\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFA6D\uFA70-\uFAD9\u{16FE2}\u{16FE3}\u{16FF0}\u{16FF1}\u{20000}-\u{2A6DF}\u{2A700}-\u{2B738}\u{2B740}-\u{2B81D}\u{2B820}-\u{2CEA1}\u{2CEB0}-\u{2EBE0}\u{2F800}-\u{2FA1D}\u{30000}-\u{3134A}]/gmu
                .source,
            "gum",
          );
        })();
        const _u = "Footer_base_0d",
          du = "Footer_content_fd",
          Eu = "Footer_button_7d",
          mu = "Footer_price_29",
          Au = "Footer_price__stock_fd",
          Fu = "Footer_fights_5e",
          gu = "Footer_extension_2b",
          Cu = "Footer_cButton_b6",
          Du = "Footer_footnote_21",
          hu = "Footer_footnote_icon_e4",
          Bu = ({ className: e }) => {
            const u = (0, o.useState)(!1),
              t = u[0],
              n = u[1],
              r = (0, o.useState)(R.strings.vehicle_customization.window.purchase.btnBuy()),
              a = r[0],
              i = r[1],
              l = ce().isAnySelected,
              c = ce("model.style").isEditable,
              _ = ce("model.tutorial"),
              d = _.onTutorialClose,
              E = _.showProlongHint,
              m = ce("model.purchase.totalPrice"),
              A = (0, o.useMemo)(() => new iu(m), [m]),
              F = ce("model.purchase"),
              g = F.onBuyAction,
              C = F.purchasedCount,
              D = F.isEnoughMoney,
              h = F.isShopEnabled,
              B = ce("model.rent"),
              v = B.hasAutoRent,
              f = B.isAutoRentSelected,
              b = B.isRentable,
              w = B.rentCount,
              y = B.onSelectAutoRent;
            (0, o.useEffect)(() => {
              if (l) {
                const e = C > 0 ? "btnBuy" : "btnApply";
                i(R.strings.vehicle_customization.window.purchase[e]());
              }
            }, [l, C]);
            const x = (0, o.useCallback)(() => {
                g();
              }, [g]),
              S = (0, o.useMemo)(
                () =>
                  cu(R.strings.vehicle_customization.carousel.rentalBattles(), { battlesNum: w }),
                [w],
              ),
              L = A.getType() === su ? su : "credits";
            let M = D;
            L === su && (M = D || h);
            const k = M && l;
            let N = "";
            k ||
              (N = l
                ? R.strings.vehicle_customization.customization.buyDisabled.body()
                : R.strings.vehicle_customization.customization.notSelectedItems());
            const T =
                R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent("resId"),
              P = R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
              O = A.getValue() > 0,
              H = A.hasDiscount(),
              I = A.getValue(),
              W = A.getDefValue(),
              z = R.strings.vehicle_customization.window.purchase.autoProlongationLabel(),
              U = R.strings.vehicle_customization.window.purchase.changedItemsLabel(),
              V = R.strings.tutorial.customization.autoprolongation(),
              $ = p()(mu, H && Au),
              G = p()(_u, e),
              j = (0, o.useMemo)(
                () => ({ tooltip: "priceDiscount", price: I, defPrice: W, currencyType: L }),
                [W, I, L],
              ),
              q = (0, o.useMemo)(() => ({ body: N }), [N]);
            return s().createElement(
              "div",
              { className: G },
              s().createElement(
                "div",
                { className: du },
                c &&
                  s().createElement(
                    "div",
                    { className: Du },
                    s().createElement("span", { className: hu }),
                    U,
                  ),
                v &&
                  s().createElement(
                    "div",
                    { className: gu },
                    E && s().createElement(ou, { text: V, isHidden: t }),
                    s().createElement(He, {
                      isChecked: f,
                      size: "medium",
                      text: z,
                      type: "primary",
                      soundHover: "highlight",
                      soundClick: "play",
                      onChange: () => {
                        (E && (n(!0), d && d()), y({ selected: !f }));
                      },
                    }),
                  ),
                b && s().createElement("div", { className: Fu }, S),
                O &&
                  s().createElement(
                    "div",
                    { className: $ },
                    s().createElement(
                      Qe,
                      { args: j, isEnabled: H },
                      s().createElement(
                        "div",
                        null,
                        s().createElement(Ge, {
                          isDiscount: H,
                          isInteractiveDiscount: !0,
                          size: "big",
                          type: L,
                          value: I,
                          isEnough: M,
                        }),
                      ),
                    ),
                  ),
                s().createElement(
                  "div",
                  { className: Eu },
                  s().createElement(
                    Ye,
                    { contentId: T, decoratorId: P, isEnabled: "" !== N, args: q },
                    s().createElement(
                      "div",
                      null,
                      s().createElement(
                        Le,
                        { type: ye.main, size: xe.medium, mixClass: Cu, disabled: !k, onClick: x },
                        a,
                      ),
                    ),
                  ),
                ),
              ),
            );
          },
          pu = "Header_base_fa",
          vu = "Header_bg_d4",
          fu = "Header_title_a1",
          bu = "Header_base__scaled_26",
          wu = "Header_itemsTitle_06",
          yu = "Header_extraTitle_54",
          xu = ({ className: e }) => {
            const u = ce("model.style", le.None),
              t = (({ isStyle: e, styleTypeName: u, styleName: t }) => {
                if (e) {
                  const e = cu(
                    R.strings.vehicle_customization.customization.infotype.type.style.multiline(),
                    { group: u, value: t },
                  ).split("\n");
                  return { title: e[0], extraTitle: e[1] };
                }
                return { title: null, extraTitle: null };
              })({ isStyle: u.isStyle, styleName: u.styleName, styleTypeName: u.styleTypeName }),
              n = t.title,
              r = t.extraTitle,
              a = _e(),
              o = Ae(a),
              i = p()(pu, o && bu, e);
            if (!n) {
              const e = R.strings.vehicle_customization.customization.buyWindow.title();
              return s().createElement(
                "div",
                { className: i },
                s().createElement("span", { className: wu }, e),
              );
            }
            return s().createElement(
              "div",
              { className: i },
              s().createElement("div", { className: vu }),
              s().createElement("span", { className: fu }, n),
              r && s().createElement("span", { className: yu }, r),
            );
          };
        function Su(e, u, t = []) {
          const n = (0, o.useRef)(0),
            r = (0, o.useCallback)(() => window.clearInterval(n.current), t || []);
          (0, o.useEffect)(() => r, [r]);
          const a = (null != t ? t : []).concat([u]);
          return [
            (0, o.useCallback)((t) => {
              ((n.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, a),
            r,
          ];
        }
        const Lu = X({
            getBounds: (e) => {
              var u, t;
              return [
                0,
                e.offsetWidth -
                  (null != (u = null == (t = e.parentElement) ? void 0 : t.offsetWidth) ? u : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, u) => {
              e.style.transform = `translateX(-${u.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? K.Next : K.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          Mu = "HorizontalBar_base_49",
          ku = "HorizontalBar_base__nonActive_82",
          Nu = "HorizontalBar_leftButton_5f",
          Tu = "HorizontalBar_rightButton_03",
          Pu = "HorizontalBar_track_0d",
          Ru = "HorizontalBar_thumb_fd",
          Ou = "HorizontalBar_rail_32",
          Hu = "disable",
          Iu = { pending: !1, offset: 0 },
          Wu = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          zu = () => {},
          Uu = (e, u) => Math.max(20, e.offsetWidth * u),
          Vu = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = Wu, onDrag: n = zu }) => {
              const r = (0, o.useRef)(null),
                a = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                l = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, o.useState)(Iu),
                E = d[0],
                m = d[1],
                A = (0, o.useCallback)(
                  (e) => {
                    (m(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                F = () => {
                  const u = l.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    _ = W(0, 1, o / (r - n)),
                    d = (u.offsetWidth - Uu(u, s)) * _;
                  ((t.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (a.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (a.current.classList.add(Hu), void i.current.classList.remove(Hu));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (a.current.classList.remove(Hu), void i.current.classList.add(Hu));
                        var u, t;
                        (a.current.classList.remove(Hu), i.current.classList.remove(Hu));
                      }
                    })(d));
                },
                g = G(() => {
                  ((() => {
                    const u = c.current,
                      t = l.current,
                      n = e.getWrapperSize(),
                      a = e.getContainerSize();
                    if (!(a && u && n && t)) return;
                    const o = Math.min(1, n / a);
                    ((u.style.width = `${Uu(t, o)}px`),
                      (u.style.display = "flex"),
                      r.current &&
                        (1 === o ? r.current.classList.add(ku) : r.current.classList.remove(ku)));
                  })(),
                    F());
                });
              ((0, o.useEffect)(() => z(g)),
                (0, o.useEffect)(
                  () =>
                    z(() => {
                      const u = () => {
                        F();
                      };
                      let t = zu;
                      const n = () => {
                        (t(), (t = z(g)));
                      };
                      return (
                        e.events.on("recalculateContent", g),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", n),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", g),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, o.useEffect)(() => {
                  if (!E.pending) return;
                  const u = (u) => {
                      var t;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const a = l.current,
                        o = c.current;
                      if (!r || !a || !o) return;
                      const s = u.screenX - E.offset - a.getBoundingClientRect().x,
                        i = (s / a.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: o, thumbOffset: s, contentOffset: i }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), A(Iu));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, E.offset, E.pending, n, A]));
              const C = Su((u) => e.applyStepTo(u), _, [e]),
                D = C[0],
                h = C[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const B = (e) => {
                e.target.classList.contains(Hu) || Fe("highlight");
              };
              return s().createElement(
                "div",
                { className: p()(Mu, u.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: p()(Nu, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Hu) || 0 !== e.button || (Fe("play"), D(K.Next));
                  },
                  onMouseUp: h,
                  ref: a,
                  onMouseEnter: B,
                }),
                s().createElement(
                  "div",
                  {
                    className: p()(Pu, u.track),
                    onMouseDown: (u) => {
                      const n = c.current;
                      if (n && 0 === u.button)
                        if ((Fe("play"), u.target === n))
                          A({ pending: !0, offset: u.screenX - n.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const n = c.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const a = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + a * u);
                          })(u.screenX > n.getBoundingClientRect().x ? K.Prev : K.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: B,
                  },
                  s().createElement("div", { ref: c, className: p()(Ru, u.thumb) }),
                  s().createElement("div", { className: p()(Ou, u.rail) }),
                ),
                s().createElement("div", {
                  className: p()(Tu, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Hu) || 0 !== e.button || (Fe("play"), D(K.Prev));
                  },
                  onMouseUp: h,
                  ref: i,
                  onMouseEnter: B,
                }),
              );
            },
          ),
          $u = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Gu = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            classNames: a,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: p()($u.base, e.base) });
              }, [n]),
              d = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: p()($u.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: p()($u.defaultScrollArea, r) },
                s().createElement(ju, { className: i, api: d, classNames: a }, e),
              ),
              s().createElement(Vu, { getStepByRailClick: l, api: u, onDrag: c, classNames: _ }),
            );
          },
          ju = ({ api: e, className: u, classNames: t, children: n, style: r }) => (
            (0, o.useEffect)(() => z(e.recalculateContent)),
            s().createElement(
              "div",
              { className: p()($u.base, u), style: r },
              s().createElement(
                "div",
                {
                  className: p()($u.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                s().createElement(
                  "div",
                  { className: p()($u.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((ju.Bar = Vu),
          (ju.Default = Gu),
          (ju.SeniorityAwards = ({ api: e, className: u, classNames: t, children: n }) => (
            (0, o.useEffect)(() => z(e.recalculateContent)),
            s().createElement(
              "div",
              { className: p()($u.base, u) },
              s().createElement(
                "div",
                { className: p()($u.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                s().createElement(
                  "div",
                  { className: p()($u.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const qu = "VerticalBar_base_f3",
          Ku = "VerticalBar_base__nonActive_42",
          Yu = "VerticalBar_topButton_d7",
          Xu = "VerticalBar_bottomButton_06",
          Zu = "VerticalBar_track_df",
          Qu = "VerticalBar_thumb_32",
          Ju = "VerticalBar_rail_43",
          et = "disable",
          ut = () => {},
          tt = { pending: !1, offset: 0 },
          nt = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          rt = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          at = (e, u) => Math.max(20, e.offsetHeight * u),
          ot = (0, o.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = nt, onDrag: n = ut }) => {
              const r = (0, o.useRef)(null),
                a = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                l = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, o.useState)(tt),
                E = d[0],
                m = d[1],
                A = (0, o.useCallback)(
                  (e) => {
                    (m(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                F = G(() => {
                  const u = c.current,
                    t = l.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && a && u && t)) return;
                  const o = Math.min(1, n / a);
                  return (
                    (u.style.height = `${at(t, o)}px`),
                    u.classList.add(Qu),
                    r.current &&
                      (1 === o ? r.current.classList.add(Ku) : r.current.classList.remove(Ku)),
                    o
                  );
                }),
                g = G(() => {
                  const u = l.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && u && t && r)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    _ = W(0, 1, o / (r - n)),
                    d = (u.offsetHeight - at(u, s)) * _;
                  ((t.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (a.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (a.current.classList.add(et), void i.current.classList.remove(et));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (a.current.classList.remove(et), void i.current.classList.add(et));
                        var u, t;
                        (a.current.classList.remove(et), i.current.classList.remove(et));
                      }
                    })(d));
                }),
                C = G(() => {
                  rt(e, () => {
                    (F(), g());
                  });
                });
              ((0, o.useEffect)(() => z(C)),
                (0, o.useEffect)(() => {
                  const u = () => {
                    rt(e, () => {
                      g();
                    });
                  };
                  let t = ut;
                  const n = () => {
                    (t(), (t = z(C)));
                  };
                  return (
                    e.events.on("recalculateContent", C),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", n),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", C),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, o.useEffect)(() => {
                  if (!E.pending) return;
                  const u = (u) => {
                      rt(e, (t) => {
                        const r = l.current,
                          a = c.current,
                          o = e.getContainerSize();
                        if (!r || !a || !o) return;
                        const s = u.screenY - E.offset - r.getBoundingClientRect().y,
                          i = (s / r.offsetHeight) * o;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          n({ type: "dragging", thumb: a, thumbOffset: s, contentOffset: i }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        A(tt));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, E.offset, E.pending, n, A]));
              const D = Su((u) => e.applyStepTo(u), _, [e]),
                h = D[0],
                B = D[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", B, !0),
                  () => document.removeEventListener("mouseup", B, !0)
                ),
                [B],
              );
              const v = (e) => {
                e.target.classList.contains(et) || Fe("highlight");
              };
              return s().createElement(
                "div",
                { className: p()(qu, u.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: p()(Yu, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(et) || 0 !== e.button || (Fe("play"), h(K.Next));
                  },
                  ref: a,
                  onMouseEnter: v,
                }),
                s().createElement(
                  "div",
                  {
                    className: p()(Zu, u.track),
                    onMouseDown: (u) => {
                      const n = c.current;
                      if (n && 0 === u.button)
                        if ((Fe("play"), u.target === n))
                          (e.handleIsThumbDragging(!0),
                            A({ pending: !0, offset: u.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            c.current &&
                              rt(e, (n) => {
                                if (!n) return;
                                const r = t(e),
                                  a = e.clampPosition(n, n.scrollTop + r * u);
                                e.applyScroll(a);
                              });
                          })(u.screenY > n.getBoundingClientRect().y ? K.Prev : K.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: v,
                  },
                  s().createElement("div", { ref: c, className: u.thumb }),
                  s().createElement("div", { className: p()(Ju, u.rail) }),
                ),
                s().createElement("div", {
                  className: p()(Xu, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(et) || 0 !== e.button || (Fe("play"), h(K.Prev));
                  },
                  onMouseUp: B,
                  ref: i,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          st = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          it = ({
            children: e,
            api: u,
            className: t,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: a,
            scrollClassNames: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: p()(st.base, e.base) });
              }, [n]),
              d = (0, o.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return s().createElement(
              "div",
              { className: p()(st.defaultScroll, t), onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: p()(st.area, r) },
                s().createElement(lt, { className: a, classNames: i, api: d }, e),
              ),
              s().createElement(ot, { getStepByRailClick: l, api: u, onDrag: c, classNames: _ }),
            );
          },
          lt = ({ className: e, classNames: u, children: t, api: n }) => (
            (0, o.useEffect)(() => z(n.recalculateContent)),
            s().createElement(
              "div",
              { className: p()(st.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              s().createElement(
                "div",
                { className: p()(st.content, null == u ? void 0 : u.content), ref: n.contentRef },
                t,
              ),
            )
          );
        lt.Default = it;
        const ct = { Vertical: r, Horizontal: n },
          _t = "Season_base_cb",
          dt = "Season_list_b5",
          Et = "Season_list__scaled_e6",
          mt = "Season_title_10",
          At = "FormFactor_base_70",
          Ft = {
            formfactor_square: R.images.gui.maps.icons.customization.icon_form_1(),
            formfactor_rect1x2: R.images.gui.maps.icons.customization.icon_form_2(),
            formfactor_rect1x3: R.images.gui.maps.icons.customization.icon_form_3(),
            formfactor_rect1x4: R.images.gui.maps.icons.customization.icon_form_4(),
            formfactor_rect1x6: R.images.gui.maps.icons.customization.icon_form_6(),
          },
          gt = (0, o.memo)(({ formFactor: e, classMix: u }) => {
            const t = Ft[e],
              n = p()(At, u),
              r = (0, o.useMemo)(() => ({ backgroundImage: `url(${t})` }), [t]);
            return e && t ? s().createElement("span", { className: n, style: r }) : null;
          }),
          Ct = "Image_base_26",
          Dt = "Image_shine_3d",
          ht = "Image_content_69",
          Bt = (0, o.memo)(({ isOwn: e, isDim: u, icon: t, isStyle: n }) => {
            const r = (0, o.useMemo)(() => ({ backgroundImage: `url(${t})` }), [t]);
            return e || n
              ? s().createElement(
                  "span",
                  { className: Ct },
                  u && s().createElement("span", { className: Dt }),
                  s().createElement("span", { className: ht, style: r }),
                )
              : s().createElement("span", { className: ht });
          }),
          pt = "Price_base_94",
          vt = "Price_base__stock_16",
          ft = "Price_factor_d3",
          bt = "Price_storage_93",
          wt = (0, o.memo)(
            ({ isStub: e, isStyle: u, isFromStorage: t, price: n, quantity: r, classMix: a }) => {
              if (u || e) return null;
              if (t)
                return s().createElement(
                  "span",
                  { className: p()(pt, a) },
                  s().createElement("span", { className: bt }, r),
                );
              const o = r && r > 1,
                i = n.hasDiscount(),
                l = p()(pt, i && vt, a);
              return s().createElement(
                "span",
                { className: l },
                o && s().createElement("span", { className: ft }, r, "×"),
                s().createElement(Ge, {
                  isDiscount: i,
                  size: Ie.small,
                  type: n.getType(),
                  value: n.getValue(),
                }),
              );
            },
          ),
          yt = "ProgressionLevelIcon_base_c3",
          xt = "ProgressionLevelIcon_icon_0b",
          St = "ProgressionLevelIcon_icon__big_c2",
          Lt = "ProgressionLevelIcon_icon__small_37",
          Mt = ({ typeId: e, progressionLevel: u, classMix: t }) => {
            const n = `level_${u}`,
              r =
                32 === e
                  ? R.images.gui.maps.icons.customization.progression_styles.icons
                  : R.images.gui.maps.icons.customization.progression_icons,
              a = r.$dyn(n),
              i = r.$dyn(n.concat("_small")),
              l = (0, o.useMemo)(() => ({ backgroundImage: `url(${i})` }), [i]),
              c = (0, o.useMemo)(() => ({ backgroundImage: `url(${a})` }), [a]);
            return a && i
              ? s().createElement(
                  "div",
                  { className: yt },
                  s().createElement("div", { className: p()(xt, Lt, t), style: l }),
                  s().createElement("div", { className: p()(xt, St, t), style: c }),
                )
              : null;
          },
          kt = "Slot_base_a9",
          Nt = "Slot_base__big_f1",
          Tt = "Slot_base__own_45",
          Pt = "Slot_border_d9",
          Rt = "Slot_base__style_4a",
          Ot = "Slot_base__unchecked_8f",
          Ht = "Slot_checkbox_d2",
          It = "Slot_checkbox__checked_a8",
          Wt = "Slot_base__checked_ea",
          zt = "Slot_topLeftCorner_8b",
          Ut = "Slot_icon_b3",
          Vt = "Slot_icon__edited_66",
          $t = "Slot_icon__rewindable_f5",
          Gt = "Slot_icon__special_36",
          jt = "Slot_icon__alert_4e",
          qt = "Slot_icon__unHistorical_66",
          Kt = "Slot_icon__fantastical_e3",
          Yt = "Slot_icon__formFactor_d1",
          Xt = "Slot_hover_ab",
          Zt = "Slot_price_03",
          Qt = { soundHover: R.sounds.highlight(), soundClick: R.sounds.cust_select() },
          Jt = ({
            id: e,
            typeId: u,
            locked: t,
            soundHover: n,
            soundClick: r,
            isFromStorage: a,
            selected: i,
            customizationDisplayType: l,
            tooltipId: c,
            isSpecial: _,
            showUnsupportedAlert: d,
            isDim: E,
            formFactor: m,
            icon: A,
            isWide: F,
            quantity: g,
            price: C,
            classMix: D,
            progressionLevel: h,
            isProgressionRewindEnabled: B,
            isEdited: v,
            isStyle: f,
          }) => {
            const b = ce("model.seasons", le.None).onSelectItem,
              w = (0, o.useMemo)(() => -1 === e, [e]),
              y = (0, o.useMemo)(() => !t, [t]),
              x = (0, o.useMemo)(() => new iu(C), [C]),
              S = (0, o.useMemo)(() => !f && !x.isEmpty(), [f, x]),
              L = (0, o.useCallback)(() => {
                y && n && Fe(n);
              }, [y, n]),
              M = (0, o.useCallback)(
                (e) => {
                  y && r && 0 === e.button && Fe(r);
                },
                [y, r],
              ),
              k = (0, o.useCallback)(() => {
                b && !t && e && b({ id: e, isFromStorage: a, selected: !i });
              }, [e, a, t, b, i]),
              N = p()(kt, D, F && Nt, S && Tt, f && Rt, S && i && Wt, S && !i && Ot),
              T = p()(Ht, i && It),
              P = (0, o.useMemo)(
                () => ({ id: e, tooltip: c, showInventoryBlock: !t, progressionLevel: h }),
                [e, t, h, c],
              );
            return s().createElement(
              Qe,
              { args: P, isEnabled: !w },
              s().createElement(
                "div",
                { className: N, onMouseEnter: L, onMouseDown: M, onClick: k },
                S && !t && s().createElement("span", { className: T }),
                s().createElement(
                  "span",
                  { className: Pt },
                  s().createElement(Bt, { isOwn: S, isDim: E, icon: A, isStyle: f }),
                  s().createElement(
                    "div",
                    { className: zt },
                    v && s().createElement("span", { className: p()(Ut, Vt) }),
                    B && s().createElement("span", { className: p()(Ut, $t) }),
                    !B &&
                      Boolean(h) &&
                      h > 0 &&
                      s().createElement(Mt, { typeId: u, progressionLevel: h, classMix: p()(Ut) }),
                    _ && s().createElement("span", { className: p()(Ut, Gt) }),
                    d && s().createElement("span", { className: p()(Ut, jt) }),
                  ),
                  1 === l && !w && s().createElement("span", { className: p()(Ut, qt) }),
                  2 === l && !w && s().createElement("span", { className: p()(Ut, Kt) }),
                  s().createElement(gt, { classMix: p()(Ut, Yt), formFactor: m }),
                  s().createElement(wt, {
                    classMix: Zt,
                    isStub: w,
                    isStyle: f,
                    isFromStorage: a,
                    price: x,
                    quantity: g,
                  }),
                  !f && s().createElement("span", { className: Xt }),
                ),
              ),
            );
          };
        Jt.defaultProps = Qt;
        const en = (0, o.memo)(Jt),
          un = "Slots_slot_44";
        function tn() {
          return (
            (tn =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            tn.apply(this, arguments)
          );
        }
        const nn = s().memo(({ type: e }) => {
            const u = ce(`model.seasons.${e}.items.items`);
            return u
              ? u.map(({ value: e }) => s().createElement(en, tn({ key: e.id, classMix: un }, e)))
              : null;
          }),
          rn = {
            base: "Title_base_0d",
            ico: "Title_ico_b2",
            ico__summer: "Title_ico__summer_ce",
            ico__winter: "Title_ico__winter_0e",
            ico__desert: "Title_ico__desert_dd",
            bonus: "Title_bonus_03",
            count: "Title_count_0d",
            count__zero: "Title_count__zero_ba",
          },
          an = ({ count: e, name: u, bonusValue: t, bonusType: n, classMix: r }) => {
            const a = u ? R.strings.vehicle_customization.buyWindow.title.$dyn(u) : "",
              o = ((e, u) =>
                e && u
                  ? cu(String(R.strings.vehicle_customization.buyWindow.title.bonus.$dyn(u)), {
                      bonus: e,
                    })
                  : "")(t, n),
              i = p()(rn.base, r);
            return s().createElement(
              "div",
              { className: i, lang: R.strings.settings.LANGUAGE_CODE() },
              s().createElement("span", { className: p()(rn.ico, rn["ico__" + u]) }),
              a,
              e >= 0 &&
                s().createElement(
                  "span",
                  { className: p()(rn.count, { [rn.count__zero]: 0 === e }) },
                  "(",
                  e,
                  ")",
                ),
              Boolean(o) && s().createElement("span", { className: rn.bonus }, o),
            );
          };
        an.defaultProps = { count: 0, name: "", bonusValue: "", bonusType: "" };
        const on = ({ type: e }) => {
            const u = ce(`model.seasons.${e}`),
              t = u.count,
              n = u.name,
              r = u.bonusType,
              a = u.bonusValue,
              o = _e(),
              i = Ae(o);
            return s().createElement(
              "div",
              { className: _t },
              s().createElement(an, {
                count: t,
                name: n,
                bonusValue: a,
                bonusType: r,
                classMix: mt,
              }),
              s().createElement(
                "div",
                { className: p()(dt, i && Et) },
                s().createElement(nn, { type: e }),
              ),
            );
          },
          sn = "Seasons_base_d0",
          ln = "Seasons_lip_93",
          cn = "Seasons_lip__top_bd",
          _n = "Seasons_lip__bottom_9b",
          dn = "Seasons_scroll_a5",
          En = "Seasons_areaBase_4e",
          mn = "Seasons_areaContent_4a",
          An = ["summer", "winter", "desert"],
          Fn = ({ scrollApi: e, className: u }) => {
            const t = p()(sn, u),
              n = p()(ln, cn),
              r = p()(ln, _n);
            return s().createElement(
              "div",
              { className: t },
              s().createElement("div", { className: n }),
              s().createElement(
                ct.Vertical.Default,
                { api: e, className: dn, scrollClassName: En, scrollClassNames: { content: mn } },
                An.map((e) => s().createElement(on, { key: e, type: e })),
              ),
              s().createElement("div", { className: r }),
            );
          },
          gn = "CustomizationCartApp_base_b8",
          Cn = "CustomizationCartApp_base__scaled_1d",
          Dn = "CustomizationCartApp_overlay_f0",
          hn = "CustomizationCartApp_overlay__lowSettings_2d",
          Bn = "CustomizationCartApp_header_f5",
          pn = "CustomizationCartApp_seasons_e0",
          vn = "CustomizationCartApp_footer_9d",
          fn = "CustomizationCartApp_scroll_87",
          bn = { settings: Object.assign({}, Y, { step: { type: "fixed", value: 30 } }) },
          wn = () => {
            const e = ce("model", le.None),
              u = e.isRendererPipelineDeferred,
              t = e.onCloseAction,
              n = Z(bn),
              r = _e(),
              a = Ae(r),
              i = ((e) => {
                const u = (0, o.useRef)(null);
                return (
                  (0, o.useEffect)(() => {
                    let t = de;
                    const n = () => {
                      t = z(() => {
                        const t = u.current;
                        if (t)
                          return (
                            (t.style.height = document.body.offsetHeight - 1 + "px"),
                            z(e.recalculateContent)
                          );
                      });
                    };
                    return (
                      n(),
                      window.addEventListener("resize", n),
                      () => {
                        (window.removeEventListener("resize", n), t());
                      }
                    );
                  }, [e]),
                  u
                );
              })(n),
              l = (0, o.useCallback)(() => {
                t && t();
              }, [t]);
            ue(Q.n.ESCAPE, l);
            const c = p()(Dn, !u && hn);
            return s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: c }),
              s().createElement(
                "div",
                { className: p()(gn, a && Cn), ref: i },
                s().createElement(be, { onClick: l }),
                s().createElement(xu, { className: Bn }),
                s().createElement(Fn, { scrollApi: n, className: p()(pn, fn) }),
                s().createElement(Bu, { className: vn }),
              ),
            );
          };
        (a.O.view.addPreloadTexture("gui/flash/atlases/components.dds"),
          engine.whenReady.then(() => {
            I().render(
              s().createElement(O, null, s().createElement(wn, null)),
              document.getElementById("root"),
            );
          }));
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(e) {
    var u = __webpack_module_cache__[e];
    if (void 0 !== u) return u.exports;
    var t = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](t, t.exports, __webpack_require__), t.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, u, t, n) => {
      if (!u) {
        var r = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [u, t, n] = deferred[i], a = !0, o = 0; o < u.length; o++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[o]))
              ? u.splice(o--, 1)
              : ((a = !1), n < r && (r = n));
          if (a) {
            deferred.splice(i--, 1);
            var s = t();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      n = n || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > n; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [u, t, n];
    }),
    (__webpack_require__.n = (e) => {
      var u = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(u, { a: u }), u);
    }),
    (__webpack_require__.d = (e, u) => {
      for (var t in u)
        __webpack_require__.o(u, t) &&
          !__webpack_require__.o(e, t) &&
          Object.defineProperty(e, t, { enumerable: !0, get: u[t] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (e, u) => Object.prototype.hasOwnProperty.call(e, u)),
    (__webpack_require__.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (__webpack_require__.j = 982),
    (() => {
      var e = { 982: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            r,
            [a, o, s] = t,
            i = 0;
          if (a.some((u) => 0 !== e[u])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (s) var l = s(__webpack_require__);
          }
          for (u && u(t); i < a.length; i++)
            ((r = a[i]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [858], () => __webpack_require__(609));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
