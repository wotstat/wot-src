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
      532: (e) => {
        e.exports = {
          BLACK_REAL: "#000000",
          WHITE_REAL: "#FFFFFF",
          WHITE: "#F2F2F7",
          WHITE_ORANGE: "#FEFEEC",
          WHITE_SPANISH: "#E9E2BF",
          PAR: "#8C8C7E",
          PAR_SECONDARY: "#595950",
          PAR_TERTIARY: "#37362E",
          INFO_RED: "#FF0000",
          RED: "#FF2717",
          RED_DARK: "#B70000",
          YELLOW: "#FEAB34",
          ORANGE: "#EE7000",
          CREAM: "#FFDD99",
          BROWN: "#CBAC77",
          GREEN_BRIGHT: "#80D43A",
          GREEN: "#7AB300",
          GREEN_DARK: "#497212",
          BLUE_BOOSTER: "#CCFFFF",
          BLUE_TEAMKILLER: "#09E2FF",
          CRED: "#CED9D9",
          GOLD: "#FFC363",
          BOND: "#C9C9B6",
          PROM: "#A29B70",
        };
      },
      887: (e) => {
        e.exports = {
          XS: "4rem",
          SM: "8rem",
          SMp: "10rem",
          MD: "16rem",
          MDp: "20rem",
          LG: "32rem",
          XL: "64rem",
        };
      },
      67: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => Y });
        var r = {};
        (t.r(r), t.d(r, { mouse: () => E, onResize: () => l }));
        var n = {};
        (t.r(n),
          t.d(n, {
            events: () => r,
            getMouseGlobalPosition: () => _,
            getSize: () => m,
            graphicsQuality: () => d,
          }));
        var a = {};
        (t.r(a), t.d(a, { getBgUrl: () => F, getTextureUrl: () => A }));
        var o = {};
        function i(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        function s(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        (t.r(o),
          t.d(o, {
            addModelObserver: () => S,
            addPreloadTexture: () => w,
            children: () => a,
            displayStatus: () => D,
            displayStatusIs: () => j,
            events: () => C,
            extraSize: () => $,
            forceTriggerMouseMove: () => V,
            freezeTextureBeforeResize: () => O,
            getBrowserTexturePath: () => M,
            getDisplayStatus: () => z,
            getScale: () => N,
            getSize: () => y,
            getViewGlobalPosition: () => R,
            isClientAccessible: () => W,
            isEventHandled: () => U,
            isFocused: () => I,
            pxToRem: () => k,
            remToPx: () => H,
            resize: () => L,
            sendEvent: () => b,
            setAnimateWindow: () => P,
            setEventHandled: () => G,
            setInputPaddingsRem: () => x,
            setSidePaddingsRem: () => T,
            whenTutorialReady: () => X,
          }));
        const l = i("clientResized"),
          c = { down: i("mousedown"), up: i("mouseup"), move: i("mousemove") };
        const E = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && s(!1);
          }
          function t() {
            e.enabled && s(!0);
          }
          function r() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : s(!1);
          }
          const n = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let n = !0;
                  const a = `mouse${u}`,
                    o = c[u]((e) => t([e, "outside"]));
                  function i(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(a, i),
                    r(),
                    () => {
                      n &&
                        (o(), window.removeEventListener(a, i), (e.listeners -= 1), r(), (n = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, n, {
            disable() {
              ((e.enabled = !1), r());
            },
            enable() {
              ((e.enabled = !0), r());
            },
            enableOutside() {
              e.enabled && s(!0);
            },
            disableOutside() {
              e.enabled && s(!1);
            },
          });
        })();
        function m(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function _(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const d = {
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
        const D = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          C = {
            onTextureFrozen: i("self.onTextureFrozen"),
            onTextureReady: i("self.onTextureReady"),
            onDomBuilt: i("self.onDomBuilt"),
            onLoaded: i("self.onLoaded"),
            onDisplayChanged: i("self.onShowingStatusChanged"),
            onFocusUpdated: i("self.onFocusChanged"),
            children: {
              onAdded: i("children.onAdded"),
              onLoaded: i("children.onLoaded"),
              onRemoved: i("children.onRemoved"),
              onAttached: i("children.onAttached"),
              onTextureReady: i("children.onTextureReady"),
              onRequestPosition: i("children.requestPosition"),
            },
          },
          B = ["args"];
        const h = 2,
          g = 16,
          p = 32,
          f = 64,
          v = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    n = {},
                    a = Object.keys(e);
                  for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, B);
              return void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([e, u]) => {
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
            var r;
          },
          b = {
            close(e) {
              v("popover" === e ? h : p);
            },
            minimize() {
              v(f);
            },
            move(e) {
              v(g, { isMouseEvent: !0, on: e });
            },
          };
        function w(e) {
          viewEnv.addPreloadTexture(e);
        }
        function x(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function M(e, u, t, r = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, r);
        }
        function S(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function T(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function y(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function L(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function R(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: H(u.x), y: H(u.y) };
        }
        function O() {
          viewEnv.freezeTextureBeforeResize();
        }
        function N() {
          return viewEnv.getScale();
        }
        function k(e) {
          return viewEnv.pxToRem(e);
        }
        function H(e) {
          return viewEnv.remToPx(e);
        }
        function P(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function I() {
          return viewEnv.isFocused();
        }
        function W() {
          return viewEnv.isClientAccessible();
        }
        function G() {
          return viewEnv.setEventHandled();
        }
        function U() {
          return viewEnv.isEventHandled();
        }
        function V() {
          viewEnv.forceTriggerMouseMove();
        }
        function z() {
          return viewEnv.getShowingStatus();
        }
        const j = Object.keys(D).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === D[u]), e),
            {},
          ),
          $ = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          X = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : C.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          Y = { view: o, client: n };
      },
      521: (e, u, t) => {
        "use strict";
        let r, n;
        (t.d(u, { n: () => r }),
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
          })(r || (r = {})),
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
          })(n || (n = {})));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        var r = t(67);
        class n {
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
            return (window.__dataTracker || (window.__dataTracker = new n()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const a = r.O.view.addModelObserver(e, t, n);
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
              const r = this._callbacks[t];
              void 0 !== r && r(e, u);
            });
          }
        }
        n.__instance = void 0;
        const a = n;
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
        t.d(u, {
          Sw: () => a.Z,
          kH: () => m,
          Z5: () => o,
          lf: () => E,
          cy: () => i,
          B0: () => s,
          wU: () => v,
          ry: () => C,
          Eu: () => B,
          SW: () => p,
          P3: () => f,
        });
        class r {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let r = e.target;
                  do {
                    if (r === u) return;
                    r = r.parentNode;
                  } while (r);
                  t();
                });
              }));
          }
          static get instance() {
            return (r.__instance || (r.__instance = new r()), r.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              r = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== r,
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
        r.__instance = void 0;
        const n = r;
        var a = t(358);
        const o = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          i = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, u, t) => userLocale.getTimeFormat(e, u, void 0 === t || t),
            getTimeString: (e, u, t) => userLocale.getTimeString(e, u, void 0 === t || t),
          };
        let s;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(s || (s = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = t(521),
          d = t(67);
        const A = ["args"];
        function F(e, u, t, r, n, a, o) {
          try {
            var i = e[a](o),
              s = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(s) : Promise.resolve(s).then(r, n);
        }
        const D = (e) => ({
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
                  return new Promise(function (r, n) {
                    var a = e.apply(u, t);
                    function o(e) {
                      F(a, r, n, o, i, "next", e);
                    }
                    function i(e) {
                      F(a, r, n, o, i, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          B = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          h = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                a = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    n = {},
                    a = Object.keys(e);
                  for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(u, A);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, a, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([e, u]) => {
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
            var r;
          },
          g = () => h(s.CLOSE),
          p = () => h(s.POP_OVER, { on: !1 }),
          f = (e, u, t, r, n = R.invalid("resId"), a) => {
            const o = d.O.view.getViewGlobalPosition(),
              i = t.getBoundingClientRect(),
              l = i.x,
              c = i.y,
              E = i.width,
              m = i.height,
              _ = {
                x: d.O.view.pxToRem(l) + o.x,
                y: d.O.view.pxToRem(c) + o.y,
                width: d.O.view.pxToRem(E),
                height: d.O.view.pxToRem(m),
              };
            h(s.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: r || R.invalid("resId"),
              targetID: n,
              direction: u,
              bbox: D(_),
              on: !0,
              args: a,
            });
          },
          v = () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
          b = (e, u) => {
            e.keyCode === _.n.ESCAPE && u();
          };
        var w = t(572);
        const x = n.instance,
          M = {
            DataTracker: a.Z,
            ViewModel: w.Z,
            ViewEventType: s,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: m,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => h(s.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: g,
            sendClosePopOverEvent: p,
            sendShowContextMenuEvent: (e, u, t = 0) => {
              h(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: f,
            addEscapeListener: (e) => {
              const u = (u) => b(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              b(e, g);
            },
            handleViewEvent: h,
            onBindingsReady: C,
            onLayoutReady: B,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: v,
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const r in u)
                if (Object.prototype.hasOwnProperty.call(u, r)) {
                  const n = Object.prototype.toString.call(u[r]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = u[r];
                    t[r] = [];
                    for (let u = 0; u < n.length; u++) t[r].push({ value: e(n[u].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[r] = e(u[r]))
                      : (t[r] = u[r]);
                }
              return t;
            },
            ClickOutsideManager: x,
            SystemLocale: o,
            UserLocale: i,
          };
        window.ViewEnvHelper = M;
      },
      19: (e, u, t) => {
        "use strict";
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => Ue,
            Bar: () => Ie,
            DefaultScroll: () => Ge,
            Direction: () => fe,
            defaultSettings: () => ve,
            useHorizontalScrollApi: () => we,
          }));
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => ou,
            Bar: () => ru,
            Default: () => au,
            useVerticalScrollApi: () => Ve,
          }));
        var a = t(179),
          o = t.n(a);
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
            : e;
        var s = t(67);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function E(e, u, t) {
          const r = (function (e, u) {
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
            n = (function (e, u) {
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
            a = Math.min(r, n);
          return {
            extraLarge: a === t.extraLarge.weight,
            large: a === t.large.weight,
            medium: a === t.medium.weight,
            small: a === t.small.weight,
            extraSmall: a === t.extraSmall.weight,
            extraLargeWidth: r === t.extraLarge.weight,
            largeWidth: r === t.large.weight,
            mediumWidth: r === t.medium.weight,
            smallWidth: r === t.small.weight,
            extraSmallWidth: r === t.extraSmall.weight,
            extraLargeHeight: n === t.extraLarge.weight,
            largeHeight: n === t.large.weight,
            mediumHeight: n === t.medium.weight,
            smallHeight: n === t.small.weight,
            extraSmallHeight: n === t.extraSmall.weight,
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
        const m = s.O.client.getSize("rem"),
          _ = m.width,
          d = m.height,
          A = Object.assign({ width: _, height: d }, E(_, d, l)),
          F = (0, a.createContext)(A),
          D = ["children"];
        const C = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                a = Object.keys(e);
              for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, D);
          const r = (0, a.useContext)(F),
            n = r.extraLarge,
            o = r.large,
            s = r.medium,
            l = r.small,
            c = r.extraSmall,
            E = r.extraLargeWidth,
            m = r.largeWidth,
            _ = r.mediumWidth,
            d = r.smallWidth,
            A = r.extraSmallWidth,
            C = r.extraLargeHeight,
            B = r.largeHeight,
            h = r.mediumHeight,
            g = r.smallHeight,
            p = r.extraSmallHeight,
            f = { extraLarge: C, large: B, medium: h, small: g, extraSmall: p };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && n) return u;
            if (t.large && o) return u;
            if (t.medium && s) return u;
            if (t.small && l) return u;
            if (t.extraSmall && c) return u;
          } else {
            if (t.extraLargeWidth && E) return i(u, t, f);
            if (t.largeWidth && m) return i(u, t, f);
            if (t.mediumWidth && _) return i(u, t, f);
            if (t.smallWidth && d) return i(u, t, f);
            if (t.extraSmallWidth && A) return i(u, t, f);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && C) return u;
              if (t.largeHeight && B) return u;
              if (t.mediumHeight && h) return u;
              if (t.smallHeight && g) return u;
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
        (0, a.memo)(C);
        const B = (e) => {
            const u = (0, a.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          h = (0, a.memo)(({ children: e }) => {
            const u = (0, a.useContext)(F),
              t = (0, a.useState)(u),
              r = t[0],
              n = t[1],
              i = (0, a.useCallback)((e, u) => {
                const t = s.O.view.pxToRem(e),
                  r = s.O.view.pxToRem(u);
                n(Object.assign({ width: t, height: r }, E(t, r, l)));
              }, []);
            (B(() => {
              engine.on("clientResized", i);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", i), [i]));
            const c = (0, a.useMemo)(() => Object.assign({}, r), [r]);
            return o().createElement(F.Provider, { value: c }, e);
          });
        var g = t(483),
          p = t.n(g),
          f = t(926),
          v = t.n(f);
        let b, w, x;
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
          })(x || (x = {})));
        const M = () => {
            const e = (0, a.useContext)(F),
              u = e.width,
              t = e.height,
              r = ((e) => {
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
              n = ((e) => {
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
              o = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return x.ExtraLarge;
                  case e.largeHeight:
                    return x.Large;
                  case e.mediumHeight:
                    return x.Medium;
                  case e.smallHeight:
                    return x.Small;
                  case e.extraSmallHeight:
                    return x.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), x.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: r,
              mediaWidth: n,
              mediaHeight: o,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          S = ["children", "className"];
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        const y = {
            [w.ExtraSmall]: "",
            [w.Small]: v().SMALL_WIDTH,
            [w.Medium]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH}`,
            [w.Large]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH} ${v().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${v().SMALL_WIDTH} ${v().MEDIUM_WIDTH} ${v().LARGE_WIDTH} ${v().EXTRA_LARGE_WIDTH}`,
          },
          L = {
            [x.ExtraSmall]: "",
            [x.Small]: v().SMALL_HEIGHT,
            [x.Medium]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT}`,
            [x.Large]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT} ${v().LARGE_HEIGHT}`,
            [x.ExtraLarge]: `${v().SMALL_HEIGHT} ${v().MEDIUM_HEIGHT} ${v().LARGE_HEIGHT} ${v().EXTRA_LARGE_HEIGHT}`,
          },
          O = {
            [b.ExtraSmall]: "",
            [b.Small]: v().SMALL,
            [b.Medium]: `${v().SMALL} ${v().MEDIUM}`,
            [b.Large]: `${v().SMALL} ${v().MEDIUM} ${v().LARGE}`,
            [b.ExtraLarge]: `${v().SMALL} ${v().MEDIUM} ${v().LARGE} ${v().EXTRA_LARGE}`,
          },
          N = (e) => {
            let u = e.children,
              t = e.className,
              r = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(e);
                for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, S);
            const n = M(),
              a = n.mediaWidth,
              i = n.mediaHeight,
              s = n.mediaSize;
            return o().createElement("div", T({ className: p()(t, y[a], L[i], O[s]) }, r), u);
          },
          k = ["children"];
        const H = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                a = Object.keys(e);
              for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, k);
          return o().createElement(h, null, o().createElement(N, t, u));
        };
        var P = t(493),
          I = t.n(P);
        function W(e) {
          engine.call("PlaySound", e);
        }
        const G = {
            playHighlight() {
              W("highlight");
            },
            playClick() {
              W("play");
            },
            playYes() {
              W("yes1");
            },
          },
          U = {
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
          V = [
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
        function z() {
          return (
            (z =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            z.apply(this, arguments)
          );
        }
        class j extends o().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && W(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && W(this.props.soundClick));
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
              r = e.goto,
              n = e.side,
              a = e.type,
              i = e.classNames,
              s = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              E = e.onMouseUp,
              m =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    r,
                    n = {},
                    a = Object.keys(e);
                  for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                  return n;
                })(e, V)),
              _ = p()(U.base, U[`base__${a}`], U[`base__${n}`], null == i ? void 0 : i.base),
              d = p()(U.icon, U[`icon__${a}`], U[`icon__${n}`], null == i ? void 0 : i.icon),
              A = p()(U.glow, null == i ? void 0 : i.glow),
              F = p()(U.caption, U[`caption__${a}`], null == i ? void 0 : i.caption),
              D = p()(U.goto, null == i ? void 0 : i.goto);
            return o().createElement(
              "div",
              z(
                {
                  className: _,
                  onMouseEnter: this._onMouseEnter(s),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(E),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                m,
              ),
              "info" !== a && o().createElement("div", { className: U.shine }),
              o().createElement(
                "div",
                { className: d },
                o().createElement("div", { className: A }),
              ),
              o().createElement("div", { className: F }, u),
              r && o().createElement("div", { className: D }, r),
            );
          }
        }
        j.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var $ = t(521),
          X = t(364);
        const Y = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function K(e = $.n.NONE, u = Y, t = !1) {
          (0, a.useEffect)(() => {
            if (e !== $.n.NONE)
              return (
                window.addEventListener("keydown", r, t),
                () => {
                  window.removeEventListener("keydown", r, t);
                }
              );
            function r(r) {
              if (r.keyCode === e) {
                if (s.O.view.isEventHandled()) return;
                (s.O.view.setEventHandled(), u(r), t && r.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        var q = t(403);
        const Z = "Background_base_1b",
          Q = "Background_image_71",
          J = ({ isBlurred: e, children: u, onLoaded: t }) => {
            const r = e
              ? "img://gui/maps/icons/battleMatters/common/background_blurred.dds"
              : R.images.gui.maps.icons.battleMatters.common.background();
            var n, i;
            return (
              (n = r),
              (i = t),
              (0, a.useEffect)(() => {
                if (!i) return;
                const e = new Image();
                return (
                  e.addEventListener("load", i),
                  e.addEventListener("error", i),
                  (e.src = n),
                  () => {
                    (e.removeEventListener("load", i), e.removeEventListener("error", i));
                  }
                );
              }, [i, n]),
              o().createElement(
                "div",
                { className: Z },
                o().createElement(
                  "div",
                  { className: Q, style: { backgroundImage: `url(${r})` } },
                  u,
                ),
              )
            );
          },
          ee = "vehCD";
        function ue() {
          return !1;
        }
        console.log;
        var te = t(174);
        function re(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return ne(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return ne(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var r = 0;
            return function () {
              return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function ne(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, r = new Array(u); t < u; t++) r[t] = e[t];
          return r;
        }
        const ae = (e) => (0 === e ? window : window.subViews.get(e));
        var oe = t(946);
        const ie = ((e, u) => {
            const t = (0, a.createContext)({});
            return [
              function ({ mode: r = "real", options: n, children: i, mocks: l }) {
                const c = (0, a.useRef)([]),
                  E = (t, r, n) => {
                    var a;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = ae,
                        context: r = "model",
                      } = {}) {
                        const n = new Map();
                        function a(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? n.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = n.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const o = (e) => {
                          const n = t(u),
                            a = r.split(".").reduce((e, u) => e[u], n);
                          return "string" != typeof e || 0 === e.length
                            ? a
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, a);
                        };
                        return {
                          subscribe: (t, a) => {
                            const i = "string" == typeof a ? `${r}.${a}` : r,
                              l = s.O.view.addModelObserver(i, u, !0);
                            return (n.set(l, t), e && t(o(a)), l);
                          },
                          readByPath: o,
                          createCallback: (e, u) => {
                            const t = o(u);
                            return (...u) => {
                              t(e(...u));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const u = o(e);
                            return () => {
                              u();
                            };
                          },
                          dispose: function () {
                            for (var e, t = re(n.keys()); !(e = t()).done;) a(e.value, u);
                          },
                          unsubscribe: a,
                        };
                      })(r),
                      i =
                        "real" === t
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (a = null == n ? void 0 : n.getter) ? a : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == n ? void 0 : n.getter(e)) : i.readByPath(e),
                      E = (e) => c.current.push(e),
                      m = e({
                        mode: t,
                        readByPath: l,
                        externalModel: i,
                        observableModel: {
                          array: (e, u) => {
                            const r = null != u ? u : l(e),
                              n = te.LO.box(r, { equals: ue });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, te.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          object: (e, u) => {
                            const r = null != u ? u : l(e),
                              n = te.LO.box(r, { equals: ue });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, te.aD)((e) => n.set(e)),
                                  e,
                                ),
                              n
                            );
                          },
                          primitives: (e, u) => {
                            const r = l(u);
                            if (Array.isArray(e)) {
                              const n = e.reduce((e, u) => ((e[u] = te.LO.box(r[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, te.aD)((u) => {
                                      e.forEach((e) => {
                                        n[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                n
                              );
                            }
                            {
                              const n = e,
                                a = Object.entries(n),
                                o = a.reduce((e, [u, t]) => ((e[t] = te.LO.box(r[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, te.aD)((e) => {
                                      a.forEach(([u, t]) => {
                                        o[t].set(e[u]);
                                      });
                                    }),
                                    u,
                                  ),
                                o
                              );
                            }
                          },
                        },
                        cleanup: E,
                      }),
                      _ = { mode: t, model: m, externalModel: i, cleanup: E };
                    return {
                      model: m,
                      controls: "mocks" === t && n ? n.controls(_) : u(_),
                      externalModel: i,
                      mode: t,
                    };
                  },
                  m = (0, a.useRef)(!1),
                  _ = (0, a.useState)(r),
                  d = _[0],
                  A = _[1],
                  F = (0, a.useState)(() => E(r, n, l)),
                  D = F[0],
                  C = F[1];
                return (
                  (0, a.useEffect)(() => {
                    m.current ? C(E(d, n, l)) : (m.current = !0);
                  }, [l, d, n]),
                  (0, a.useEffect)(() => {
                    A(r);
                  }, [r]),
                  (0, a.useEffect)(
                    () => () => {
                      (D.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [D],
                  ),
                  o().createElement(t.Provider, { value: D }, i)
                );
              },
              () => (0, a.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = te.LO.box(""),
                t = te.LO.box(!1),
                r = {
                  primitives: e.primitives(["endDate", "totalVehiclesCount", "level"]),
                  vehicles: e.array("vehicles", []),
                },
                n = (0, oe.Om)(() => {
                  return (
                    (e = r.vehicles.get()),
                    (u = ({ userName: e }) => systemLocale.toLowerCase(e)),
                    Array.isArray(e)
                      ? e.map(u)
                      : e.map((e, t, r) => u(null == e ? void 0 : e.value, t, r))
                  );
                  var e, u;
                }),
                a = (0, oe.Om)(() => {
                  const e = u.get();
                  return (function (e, u) {
                    if (Array.isArray(e)) return e.filter(u);
                    const t = [];
                    for (let n = 0; n < e.length; n++) {
                      var r;
                      const a = null == (r = e[n]) ? void 0 : r.value;
                      u(a, n, e) && t.push(a);
                    }
                    return t;
                  })(r.vehicles.get(), (u, t) => n()[t].includes(e));
                }),
                o = (0, oe.Om)(() => a().length),
                i = (0, oe.Om)(() => o() < r.primitives.totalVehiclesCount.get());
              return Object.assign({}, r.primitives, {
                filterString: u,
                isLoaded: t,
                computes: { getVehicles: a, getVehiclesCount: o, isFilterApplied: i },
              });
            },
            ({ externalModel: e, model: u }) => {
              const t = e.createCallbackNoArgs("onResetFilter");
              return {
                goBack: e.createCallbackNoArgs("onGoBack"),
                showVehicle: e.createCallback((e) => ({ [ee]: e }), "onShowVehicle"),
                compareVehicle: e.createCallback((e) => ({ [ee]: e }), "onCompareVehicle"),
                setFilter: (0, te.aD)((e) => u.filterString.set(e && systemLocale.toLowerCase(e))),
                loaded: (0, te.aD)(() => u.isLoaded.set(!0)),
                resetFilter: (0, te.aD)(() => {
                  (u.filterString.set(""), t());
                }),
              };
            },
          ),
          se = ie[0],
          le = ie[1],
          ce = "App_base_4d",
          Ee = "App_base__visible_2f",
          me = "App_content_fc",
          _e = "App_backButton_05",
          de = (e) => {
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
          },
          Ae = (e, u, t) => (t < e ? e : t > u ? u : t),
          Fe = [];
        function De(e) {
          const u = (0, a.useRef)(e);
          return (
            (0, a.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, a.useCallback)((...e) => (0, u.current)(...e), Fe)
          );
        }
        function Ce(e, u, t = []) {
          const r = (0, a.useRef)(0),
            n = (0, a.useCallback)(() => window.clearInterval(r.current), t || []);
          (0, a.useEffect)(() => n, [n]);
          const o = (null != t ? t : []).concat([u]);
          return [
            (0, a.useCallback)((t) => {
              ((r.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
            }, o),
            n,
          ];
        }
        function Be(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return he(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return he(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var r = 0;
            return function () {
              return r >= e.length ? { done: !0 } : { done: !1, value: e[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function he(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, r = new Array(u); t < u; t++) r[t] = e[t];
          return r;
        }
        function ge(e, u, t) {
          const r = (0, a.useMemo)(
            () =>
              (function (e, u, t, r) {
                let n,
                  a = !1,
                  o = 0;
                function i() {
                  n && clearTimeout(n);
                }
                function s(...s) {
                  const l = this,
                    c = Date.now() - o;
                  function E() {
                    ((o = Date.now()), t.apply(l, s));
                  }
                  a ||
                    (r && !n && E(),
                    i(),
                    void 0 === r && c > e
                      ? E()
                      : !0 !== u &&
                        (n = setTimeout(
                          r
                            ? function () {
                                n = void 0;
                              }
                            : E,
                          void 0 === r ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((r = t), (t = u), (u = void 0)),
                  (s.cancel = function () {
                    (i(), (a = !0));
                  }),
                  s
                );
              })(t, e),
            u,
          );
          return ((0, a.useEffect)(() => r.cancel, [r]), r);
        }
        var pe = t(30);
        let fe;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(fe || (fe = {}));
        const ve = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          be = ({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: r,
            getWrapperSize: n,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const i = (e, t) => {
              const r = u(e),
                n = r[0],
                a = r[1];
              return Ae(n, a, t);
            };
            return (l = {}) => {
              const c = l.settings,
                E = void 0 === c ? ve : c,
                m = (0, a.useRef)(null),
                _ = (0, a.useRef)(null),
                d = (() => {
                  const e = (0, a.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    r = (e, t) => {
                      u(e).delete(t);
                    },
                    n = (e, ...t) => {
                      for (var r, n = Be(u(e).values()); !(r = n()).done;) (0, r.value)(...t);
                    };
                  return (0, a.useMemo)(() => ({ on: t, off: r, trigger: n }), []);
                })(),
                A = ge(
                  () => {
                    s.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                F = (0, pe.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = m.current;
                    u && (t(u, e), d.trigger("change", e), o && A());
                  },
                  onRest: (e) => d.trigger("rest", e),
                  onStart: (e) => d.trigger("start", e),
                  onPause: (e) => d.trigger("pause", e),
                })),
                D = F[0],
                C = F[1],
                B = (0, a.useCallback)(
                  (e, u, t) => {
                    var r;
                    const n = D.scrollPosition.get(),
                      a = (null != (r = D.scrollPosition.goal) ? r : 0) - n;
                    return i(e, u * t + a + n);
                  },
                  [D.scrollPosition],
                ),
                h = (0, a.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const r = m.current;
                    r &&
                      C.start({
                        scrollPosition: i(r, e),
                        immediate: u,
                        reset: t,
                        config: E.animationConfig,
                        from: { scrollPosition: i(r, D.scrollPosition.get()) },
                      });
                  },
                  [C, E.animationConfig, D.scrollPosition],
                ),
                g = (0, a.useCallback)(
                  (e) => {
                    const u = m.current,
                      t = _.current;
                    if (!u || !t) return;
                    const r = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return n(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, E.step),
                      a = B(u, e, r);
                    h(a);
                  },
                  [h, B, E.step],
                ),
                p = (0, a.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && g(r(e)),
                      m.current && d.trigger("mouseWheel", e, D.scrollPosition, u(m.current)));
                  },
                  [D.scrollPosition, g, d],
                ),
                f = ((e, u = []) => {
                  const t = (0, a.useRef)(),
                    r = (0, a.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
                  return (
                    (0, a.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [r],
                    ),
                    r
                  );
                })(
                  () =>
                    de(() => {
                      const e = m.current;
                      e &&
                        (h(i(e, D.scrollPosition.goal), { immediate: !0 }),
                        d.trigger("resizeHandled"));
                    }),
                  [h, D.scrollPosition.goal],
                ),
                v = De(() => {
                  const e = m.current;
                  if (!e) return;
                  const u = i(e, D.scrollPosition.goal);
                  (u !== D.scrollPosition.goal && h(u, { immediate: !0 }),
                    d.trigger("recalculateContent"));
                });
              (0, a.useEffect)(
                () => (
                  window.addEventListener("resize", f),
                  () => {
                    window.removeEventListener("resize", f);
                  }
                ),
                [f],
              );
              const b = (0, a.useCallback)((e) => d.trigger("isThumbDraggingChanged", e), [d]);
              return (0, a.useMemo)(
                () => ({
                  getWrapperSize: () => (_.current ? n(_.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? u(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: E.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: p,
                  applyScroll: h,
                  applyStepTo: g,
                  contentRef: m,
                  wrapperRef: _,
                  scrollPosition: C,
                  animationScroll: D,
                  recalculateContent: v,
                  handleIsThumbDragging: b,
                  events: { on: d.on, off: d.off },
                }),
                [D.scrollPosition, h, g, b, d.off, d.on, v, p, C, E.step.clampedArrowStepTimeout],
              );
            };
          },
          we = be({
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
            getDirection: (e) => (e.deltaY > 1 ? fe.Next : fe.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          xe = "HorizontalBar_base_49",
          Me = "HorizontalBar_base__nonActive_82",
          Se = "HorizontalBar_leftButton_5f",
          Te = "HorizontalBar_rightButton_03",
          ye = "HorizontalBar_track_0d",
          Le = "HorizontalBar_thumb_fd",
          Re = "HorizontalBar_rail_32",
          Oe = "disable",
          Ne = { pending: !1, offset: 0 },
          ke = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          He = () => {},
          Pe = (e, u) => Math.max(20, e.offsetWidth * u),
          Ie = (0, a.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = ke, onDrag: r = He }) => {
              const n = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                s = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = e.stepTimeout || 100,
                m = (0, a.useState)(Ne),
                _ = m[0],
                d = m[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (d(e),
                      c.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                F = () => {
                  const u = l.current,
                    t = c.current,
                    r = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(r && u && t && n)) return;
                  const a = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, r / n),
                    E = Ae(0, 1, a / (n - r)),
                    m = (u.offsetWidth - Pe(u, o)) * E;
                  ((t.style.transform = `translateX(${0 | m}px)`),
                    ((e) => {
                      if (i.current && s.current && l.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Oe), void s.current.classList.remove(Oe));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(Oe), void s.current.classList.add(Oe));
                        var u, t;
                        (i.current.classList.remove(Oe), s.current.classList.remove(Oe));
                      }
                    })(m));
                },
                D = De(() => {
                  ((() => {
                    const u = c.current,
                      t = l.current,
                      r = e.getWrapperSize(),
                      a = e.getContainerSize();
                    if (!(a && u && r && t)) return;
                    const o = Math.min(1, r / a);
                    ((u.style.width = `${Pe(t, o)}px`),
                      (u.style.display = "flex"),
                      n.current &&
                        (1 === o ? n.current.classList.add(Me) : n.current.classList.remove(Me)));
                  })(),
                    F());
                });
              ((0, a.useEffect)(() => de(D)),
                (0, a.useEffect)(
                  () =>
                    de(() => {
                      const u = () => {
                        F();
                      };
                      let t = He;
                      const r = () => {
                        (t(), (t = de(D)));
                      };
                      return (
                        e.events.on("recalculateContent", D),
                        e.events.on("rest", u),
                        e.events.on("change", u),
                        e.events.on("resizeHandled", r),
                        () => {
                          (t(),
                            e.events.off("recalculateContent", D),
                            e.events.off("rest", u),
                            e.events.off("change", u),
                            e.events.off("resizeHandled", r));
                        }
                      );
                    }),
                  [e],
                ),
                (0, a.useEffect)(() => {
                  if (!_.pending) return;
                  const u = (u) => {
                      var t;
                      const n = e.contentRef.current;
                      if (!n) return;
                      const a = l.current,
                        o = c.current;
                      if (!n || !a || !o) return;
                      const i = u.screenX - _.offset - a.getBoundingClientRect().x,
                        s = (i / a.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(n, s),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        r({ type: "dragging", thumb: o, thumbOffset: i, contentOffset: s }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), A(Ne));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, _.offset, _.pending, r, A]));
              const C = Ce((u) => e.applyStepTo(u), E, [e]),
                B = C[0],
                h = C[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const g = (e) => {
                e.target.classList.contains(Oe) || W("highlight");
              };
              return o().createElement(
                "div",
                { className: p()(xe, u.base), ref: n, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: p()(Se, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Oe) || 0 !== e.button || (W("play"), B(fe.Next));
                  },
                  onMouseUp: h,
                  ref: i,
                  onMouseEnter: g,
                }),
                o().createElement(
                  "div",
                  {
                    className: p()(ye, u.track),
                    onMouseDown: (u) => {
                      const r = c.current;
                      if (r && 0 === u.button)
                        if ((W("play"), u.target === r))
                          A({ pending: !0, offset: u.screenX - r.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const r = c.current,
                              n = e.contentRef.current;
                            if (!r || !n) return;
                            const a = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + a * u);
                          })(u.screenX > r.getBoundingClientRect().x ? fe.Prev : fe.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: g,
                  },
                  o().createElement("div", { ref: c, className: p()(Le, u.thumb) }),
                  o().createElement("div", { className: p()(Re, u.rail) }),
                ),
                o().createElement("div", {
                  className: p()(Te, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Oe) || 0 !== e.button || (W("play"), B(fe.Prev));
                  },
                  onMouseUp: h,
                  ref: s,
                  onMouseEnter: g,
                }),
              );
            },
          ),
          We = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Ge = ({
            children: e,
            api: u,
            className: t,
            barClassNames: r,
            areaClassName: n,
            classNames: i,
            scrollClassName: s,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: p()(We.base, e.base) });
              }, [r]),
              m = (0, a.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return o().createElement(
              "div",
              { className: p()(We.defaultScroll, t), onWheel: u.handleMouseWheel },
              o().createElement(
                "div",
                { className: p()(We.defaultScrollArea, n) },
                o().createElement(Ue, { className: s, api: m, classNames: i }, e),
              ),
              o().createElement(Ie, { getStepByRailClick: l, api: u, onDrag: c, classNames: E }),
            );
          },
          Ue = ({ api: e, className: u, classNames: t, children: r, style: n }) => (
            (0, a.useEffect)(() => de(e.recalculateContent)),
            o().createElement(
              "div",
              { className: p()(We.base, u), style: n },
              o().createElement(
                "div",
                {
                  className: p()(We.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: p()(We.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          );
        ((Ue.Bar = Ie),
          (Ue.Default = Ge),
          (Ue.SeniorityAwards = ({ api: e, className: u, classNames: t, children: r }) => (
            (0, a.useEffect)(() => de(e.recalculateContent)),
            o().createElement(
              "div",
              { className: p()(We.base, u) },
              o().createElement(
                "div",
                { className: p()(We.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                o().createElement(
                  "div",
                  { className: p()(We.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          )));
        const Ve = be({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, u) => {
              e.scrollTop = u.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? fe.Next : fe.Prev),
          }),
          ze = "VerticalBar_base_f3",
          je = "VerticalBar_base__nonActive_42",
          $e = "VerticalBar_topButton_d7",
          Xe = "VerticalBar_bottomButton_06",
          Ye = "VerticalBar_track_df",
          Ke = "VerticalBar_thumb_32",
          qe = "VerticalBar_rail_43",
          Ze = "disable",
          Qe = () => {},
          Je = { pending: !1, offset: 0 },
          eu = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          uu = (e, u) => {
            e.contentRef.current && u(e.contentRef.current);
          },
          tu = (e, u) => Math.max(20, e.offsetHeight * u),
          ru = (0, a.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = eu, onDrag: r = Qe }) => {
              const n = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                s = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = e.stepTimeout || 100,
                m = (0, a.useState)(Je),
                _ = m[0],
                d = m[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (d(e),
                      c.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                F = De(() => {
                  const u = c.current,
                    t = l.current,
                    r = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(r && a && u && t)) return;
                  const o = Math.min(1, r / a);
                  return (
                    (u.style.height = `${tu(t, o)}px`),
                    u.classList.add(Ke),
                    n.current &&
                      (1 === o ? n.current.classList.add(je) : n.current.classList.remove(je)),
                    o
                  );
                }),
                D = De(() => {
                  const u = l.current,
                    t = c.current,
                    r = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(r && u && t && n)) return;
                  const a = e.animationScroll.scrollPosition.get(),
                    o = Math.min(1, r / n),
                    E = Ae(0, 1, a / (n - r)),
                    m = (u.offsetHeight - tu(u, o)) * E;
                  ((t.style.transform = `translateY(${0 | m}px)`),
                    ((e) => {
                      if (i.current && s.current && l.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Ze), void s.current.classList.remove(Ze));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(Ze), void s.current.classList.add(Ze));
                        var u, t;
                        (i.current.classList.remove(Ze), s.current.classList.remove(Ze));
                      }
                    })(m));
                }),
                C = De(() => {
                  uu(e, () => {
                    (F(), D());
                  });
                });
              ((0, a.useEffect)(() => de(C)),
                (0, a.useEffect)(() => {
                  const u = () => {
                    uu(e, () => {
                      D();
                    });
                  };
                  let t = Qe;
                  const r = () => {
                    (t(), (t = de(C)));
                  };
                  return (
                    e.events.on("recalculateContent", C),
                    e.events.on("rest", u),
                    e.events.on("change", u),
                    e.events.on("resizeHandled", r),
                    () => {
                      (t(),
                        e.events.off("recalculateContent", C),
                        e.events.off("rest", u),
                        e.events.off("change", u),
                        e.events.off("resizeHandled", r));
                    }
                  );
                }, [e]),
                (0, a.useEffect)(() => {
                  if (!_.pending) return;
                  const u = (u) => {
                      uu(e, (t) => {
                        const n = l.current,
                          a = c.current,
                          o = e.getContainerSize();
                        if (!n || !a || !o) return;
                        const i = u.screenY - _.offset - n.getBoundingClientRect().y,
                          s = (i / n.offsetHeight) * o;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(t, s),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          r({ type: "dragging", thumb: a, thumbOffset: i, contentOffset: s }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u),
                        e.handleIsThumbDragging(!1),
                        A(Je));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, _.offset, _.pending, r, A]));
              const B = Ce((u) => e.applyStepTo(u), E, [e]),
                h = B[0],
                g = B[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", g, !0),
                  () => document.removeEventListener("mouseup", g, !0)
                ),
                [g],
              );
              const f = (e) => {
                e.target.classList.contains(Ze) || W("highlight");
              };
              return o().createElement(
                "div",
                { className: p()(ze, u.base), ref: n, onWheel: e.handleMouseWheel },
                o().createElement("div", {
                  className: p()($e, u.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ze) || 0 !== e.button || (W("play"), h(fe.Next));
                  },
                  ref: i,
                  onMouseEnter: f,
                }),
                o().createElement(
                  "div",
                  {
                    className: p()(Ye, u.track),
                    onMouseDown: (u) => {
                      const r = c.current;
                      if (r && 0 === u.button)
                        if ((W("play"), u.target === r))
                          (e.handleIsThumbDragging(!0),
                            A({ pending: !0, offset: u.screenY - r.getBoundingClientRect().y }));
                        else {
                          ((u) => {
                            c.current &&
                              uu(e, (r) => {
                                if (!r) return;
                                const n = t(e),
                                  a = e.clampPosition(r, r.scrollTop + n * u);
                                e.applyScroll(a);
                              });
                          })(u.screenY > r.getBoundingClientRect().y ? fe.Prev : fe.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: f,
                  },
                  o().createElement("div", { ref: c, className: u.thumb }),
                  o().createElement("div", { className: p()(qe, u.rail) }),
                ),
                o().createElement("div", {
                  className: p()(Xe, u.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Ze) || 0 !== e.button || (W("play"), h(fe.Prev));
                  },
                  onMouseUp: g,
                  ref: s,
                  onMouseEnter: f,
                }),
              );
            },
          ),
          nu = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          au = ({
            children: e,
            api: u,
            className: t,
            barClassNames: r,
            areaClassName: n,
            scrollClassName: i,
            scrollClassNames: s,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: p()(nu.base, e.base) });
              }, [r]),
              m = (0, a.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return o().createElement(
              "div",
              { className: p()(nu.defaultScroll, t), onWheel: u.handleMouseWheel },
              o().createElement(
                "div",
                { className: p()(nu.area, n) },
                o().createElement(ou, { className: i, classNames: s, api: m }, e),
              ),
              o().createElement(ru, { getStepByRailClick: l, api: u, onDrag: c, classNames: E }),
            );
          },
          ou = ({ className: e, classNames: u, children: t, api: r }) => (
            (0, a.useEffect)(() => de(r.recalculateContent)),
            o().createElement(
              "div",
              { className: p()(nu.base, e), ref: r.wrapperRef, onWheel: r.handleMouseWheel },
              o().createElement(
                "div",
                { className: p()(nu.content, null == u ? void 0 : u.content), ref: r.contentRef },
                t,
              ),
            )
          );
        ou.Default = au;
        const iu = { Vertical: n, Horizontal: r };
        var su = t(887),
          lu = t.n(su);
        const cu = ["xl", "lg", "md", "sm", "xs"],
          Eu = (e) => e.includes("_") && ((e) => cu.includes(e))(e.split("_").at(-1)),
          mu = [b.ExtraLarge, b.Large, b.Medium, b.Small, b.ExtraSmall],
          _u = (e, u) =>
            Object.keys(e).reduce((t, r) => {
              if (r in t) return t;
              if (Eu(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const a = mu.indexOf(u),
                  o = (-1 !== a ? cu.slice(a) : [])
                    .map((e) => n + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  i = o ? e[o] : void 0;
                return ((t[n] = void 0 !== i ? i : e[n]), t);
              }
              const n = e[r];
              return (
                void 0 === n ||
                  ((e, u) => cu.some((t) => void 0 !== u[`${e}_${t}`]))(r, e) ||
                  (t[r] = n),
                t
              );
            }, {}),
          du = (e, u = _u) => {
            const t = (
              (e, u = _u) =>
              (t) => {
                const r = M().mediaSize,
                  n = (0, a.useMemo)(() => u(t, r), [t, r]);
                return o().createElement(e, n);
              }
            )(e, u);
            return o().memo((u) =>
              Object.keys(u).some((e) => Eu(e) && void 0 !== u[e])
                ? o().createElement(t, u)
                : o().createElement(e, u),
            );
          },
          Au = {
            mt__XS: "Box_mt__XS_0c",
            mt__SM: "Box_mt__SM_eb",
            mt__SMp: "Box_mt__SMp_cf",
            mt__MD: "Box_mt__MD_25",
            mt__MDp: "Box_mt__MDp_49",
            mt__LG: "Box_mt__LG_e8",
            mt__XL: "Box_mt__XL_83",
            mr__XS: "Box_mr__XS_7c",
            mr__SM: "Box_mr__SM_08",
            mr__SMp: "Box_mr__SMp_06",
            mr__MD: "Box_mr__MD_4a",
            mr__MDp: "Box_mr__MDp_b6",
            mr__LG: "Box_mr__LG_d0",
            mr__XL: "Box_mr__XL_db",
            mb__XS: "Box_mb__XS_bb",
            mb__SM: "Box_mb__SM_83",
            mb__SMp: "Box_mb__SMp_04",
            mb__MD: "Box_mb__MD_ed",
            mb__MDp: "Box_mb__MDp_65",
            mb__LG: "Box_mb__LG_c8",
            mb__XL: "Box_mb__XL_f8",
            ml__XS: "Box_ml__XS_8a",
            ml__SM: "Box_ml__SM_e6",
            ml__SMp: "Box_ml__SMp_fb",
            ml__MD: "Box_ml__MD_2b",
            ml__MDp: "Box_ml__MDp_c7",
            ml__LG: "Box_ml__LG_39",
            ml__XL: "Box_ml__XL_4a",
          },
          Fu = [
            "className",
            "width",
            "height",
            "m",
            "mt",
            "mr",
            "mb",
            "ml",
            "column",
            "row",
            "flexDirection",
            "flexStart",
            "center",
            "flexEnd",
            "spaceBetween",
            "spaceAround",
            "justifyContent",
            "alignItems",
            "alignSelf",
            "wrap",
            "flexWrap",
            "grow",
            "shrink",
            "flex",
            "style",
            "children",
          ];
        function Du() {
          return (
            (Du =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Du.apply(this, arguments)
          );
        }
        Object.keys(lu());
        const Cu = {
            XL: { mt: Au.mt__XL, mr: Au.mr__XL, mb: Au.mb__XL, ml: Au.ml__XL },
            LG: { mt: Au.mt__LG, mr: Au.mr__LG, mb: Au.mb__LG, ml: Au.ml__LG },
            MDp: { mt: Au.mt__MDp, mr: Au.mr__MDp, mb: Au.mb__MDp, ml: Au.ml__MDp },
            MD: { mt: Au.mt__MD, mr: Au.mr__MD, mb: Au.mb__MD, ml: Au.ml__MD },
            SMp: { mt: Au.mt__SMp, mr: Au.mr__SMp, mb: Au.mb__SMp, ml: Au.ml__SMp },
            SM: { mt: Au.mt__SM, mr: Au.mr__SM, mb: Au.mb__SM, ml: Au.ml__SM },
            XS: { mt: Au.mt__XS, mr: Au.mr__XS, mb: Au.mb__XS, ml: Au.ml__XS },
          },
          Bu = (Object.keys(Cu), ["mt", "mr", "mb", "ml"]),
          hu = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          gu = du((e) => {
            let u = e.className,
              t = e.width,
              r = e.height,
              n = e.m,
              i = e.mt,
              s = void 0 === i ? n : i,
              l = e.mr,
              c = void 0 === l ? n : l,
              E = e.mb,
              m = void 0 === E ? n : E,
              _ = e.ml,
              d = void 0 === _ ? n : _,
              A = e.column,
              F = e.row,
              D = e.flexDirection,
              C = void 0 === D ? (A ? "column" : F && "row") || void 0 : D,
              B = e.flexStart,
              h = e.center,
              g = e.flexEnd,
              f = e.spaceBetween,
              v = e.spaceAround,
              b = e.justifyContent,
              w =
                void 0 === b
                  ? (B ? "flex-start" : h && "center") ||
                    (g && "flex-end") ||
                    (f && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : b,
              x = e.alignItems,
              M =
                void 0 === x
                  ? (B ? "flex-start" : h && "center") || (g && "flex-end") || void 0
                  : x,
              S = e.alignSelf,
              T = e.wrap,
              y = e.flexWrap,
              L = void 0 === y ? (T ? "wrap" : void 0) : y,
              R = e.grow,
              O = e.shrink,
              N = e.flex,
              k = void 0 === N ? (R || O ? `${R ? 1 : 0} ${O ? 1 : 0} auto` : void 0) : N,
              H = e.style,
              P = e.children,
              I = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(e);
                for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, Fu);
            const W = (0, a.useMemo)(() => {
                const e = { mt: s, mr: c, mb: m, ml: d },
                  u = ((e) =>
                    Bu.reduce((u, t) => {
                      const r = e[t];
                      return r && "number" != typeof r ? u.concat(Cu[!0 === r ? "MD" : r][t]) : u;
                    }, []))(e),
                  n = ((e) =>
                    Bu.reduce((u, t) => {
                      const r = e[t];
                      return ("number" == typeof r && (u[hu[t]] = r + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, H, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: k,
                    alignSelf: S,
                    display: C || M ? "flex" : void 0,
                    flexDirection: C,
                    flexWrap: L,
                    justifyContent: w,
                    alignItems: M,
                  }),
                  computedClassNames: u,
                };
              }, [t, r, s, c, m, d, H, k, S, C, L, w, M]),
              G = W.computedStyle,
              U = W.computedClassNames;
            return o().createElement(
              "div",
              Du({ className: p()(Au.base, ...U, u), style: G }, I),
              P,
            );
          });
        let pu;
        function fu(e) {
          return e.replace(/-/g, "_");
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(pu || (pu = {}));
        const vu = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          bu = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          wu = (e, u, t = pu.left) => e.split(u).reduce(t === pu.left ? vu : bu, []),
          xu = (() => {
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
            return (u) =>
              u
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(e);
          })(),
          Mu = ["zh_cn", "zh_sg", "zh_tw"],
          Su = (e, u = pu.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return Mu.includes(t)
              ? xu(e)
              : ((e, u = pu.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (wu(n, /( )/, u).forEach((e) => (t = t.concat(wu(e, r, pu.left)))), t);
                })(e, u);
          },
          Tu = "FormatText_base_d0",
          yu = ({ binding: e, text: u = "", classMix: t, alignment: r = pu.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : o().createElement(
                  a.Fragment,
                  null,
                  u.split("\n").map((u, n) =>
                    o().createElement(
                      "div",
                      { className: p()(Tu, t), key: `${u}-${n}` },
                      ((e, u, t) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (t && e in t ? t[e] : Su(e, u))))(u, r, e).map((e, u) =>
                        o().createElement(a.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var Lu = t(532),
          Ru = t.n(Lu);
        const Ou = {
            "paragraph-P10": "Text_paragraph-P10_2c",
            "paragraph-P12": "Text_paragraph-P12_22",
            "paragraph-P14": "Text_paragraph-P14_a7",
            "paragraph-P16": "Text_paragraph-P16_90",
            "paragraph-P18": "Text_paragraph-P18_50",
            "paragraph-P24": "Text_paragraph-P24_33",
            "heading-H14": "Text_heading-H14_8b",
            "heading-H15": "Text_heading-H15_9e",
            "heading-H18": "Text_heading-H18_b7",
            "heading-H20R": "Text_heading-H20R_f6",
            "heading-H22": "Text_heading-H22_27",
            "heading-H24R": "Text_heading-H24R_be",
            "heading-H24": "Text_heading-H24_0c",
            "heading-H28": "Text_heading-H28_78",
            "heading-H36": "Text_heading-H36_32",
            "heading-H56": "Text_heading-H56_c3",
            "heading-H73": "Text_heading-H73_8f",
            "heading-H144": "Text_heading-H144_a9",
            BLACK_REAL: "Text_BLACK_REAL_30",
            WHITE_REAL: "Text_WHITE_REAL_bc",
            WHITE: "Text_WHITE_62",
            WHITE_ORANGE: "Text_WHITE_ORANGE_54",
            WHITE_SPANISH: "Text_WHITE_SPANISH_df",
            PAR: "Text_PAR_15",
            PAR_SECONDARY: "Text_PAR_SECONDARY_5d",
            PAR_TERTIARY: "Text_PAR_TERTIARY_c9",
            INFO_RED: "Text_INFO_RED_30",
            RED: "Text_RED_66",
            RED_DARK: "Text_RED_DARK_d8",
            YELLOW: "Text_YELLOW_ed",
            ORANGE: "Text_ORANGE_be",
            CREAM: "Text_CREAM_57",
            BROWN: "Text_BROWN_18",
            GREEN_BRIGHT: "Text_GREEN_BRIGHT_3f",
            GREEN: "Text_GREEN_e3",
            GREEN_DARK: "Text_GREEN_DARK_f1",
            BLUE_BOOSTER: "Text_BLUE_BOOSTER_21",
            BLUE_TEAMKILLER: "Text_BLUE_TEAMKILLER_ab",
            CRED: "Text_CRED_f7",
            GOLD: "Text_GOLD_28",
            BOND: "Text_BOND_be",
            PROM: "Text_PROM_65",
          },
          Nu = [
            "text",
            "variant",
            "className",
            "color",
            "m",
            "mt",
            "mr",
            "mb",
            "ml",
            "style",
            "format",
          ];
        function ku() {
          return (
            (ku =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            ku.apply(this, arguments)
          );
        }
        Object.keys(lu());
        const Hu = Object.keys(Ru()),
          Pu = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Iu = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Wu = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Gu = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Uu =
            (Object.keys(Gu),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Pu,
              "heading-H36": Pu,
              "heading-H28": Iu,
              "heading-H24": Iu,
              "heading-H24R": Iu,
              "heading-H22": Iu,
              "heading-H20R": Iu,
              "heading-H18": Iu,
              "heading-H15": Wu,
              "heading-H14": Wu,
              "paragraph-P24": Iu,
              "paragraph-P18": Iu,
              "paragraph-P16": Iu,
              "paragraph-P14": Wu,
              "paragraph-P12": Wu,
              "paragraph-P10": Wu,
            }),
          Vu =
            (Object.keys(Uu),
            (e) =>
              e
                ? ((e) => Hu.includes(e))(e)
                  ? { colorClassName: Ou[e] }
                  : { colorStyle: { color: e } }
                : {}),
          zu = du((e) => {
            let u = e.text,
              t = e.variant,
              r = e.className,
              n = e.color,
              i = e.m,
              s = e.mt,
              l = void 0 === s ? i : s,
              c = e.mr,
              E = void 0 === c ? i : c,
              m = e.mb,
              _ = void 0 === m ? i : m,
              d = e.ml,
              A = void 0 === d ? i : d,
              F = e.style,
              D = e.format,
              C = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(e);
                for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, Nu);
            const B = (0, a.useMemo)(() => {
                const e = Vu(n),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, r), colorClassName: u };
              }, [F, n]),
              h = B.computedStyle,
              g = B.colorClassName;
            return o().createElement(
              gu,
              ku(
                {
                  className: p()(Ou.base, t && Ou[t], g, r),
                  style: h,
                  mt: !0 === l ? Uu[t || "paragraph-P16"].mt : l,
                  mr: !0 === E ? Uu[t || "paragraph-P16"].mr : E,
                  mb: !0 === _ ? Uu[t || "paragraph-P16"].mb : _,
                  ml: !0 === A ? Uu[t || "paragraph-P16"].ml : A,
                },
                C,
              ),
              void 0 !== D ? o().createElement(yu, ku({}, D, { text: u })) : u,
            );
          }),
          ju = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          $u = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        function Xu(e) {
          let u = "";
          for (let t = $u.length - 1; t >= 0; t--) for (; e >= $u[t];) ((u += ju[t]), (e -= $u[t]));
          return u;
        }
        const Yu = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          Ku = [
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
        function qu(e) {
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
        const Zu = (e, u, t = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: X.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: r,
                },
                t,
              ),
            );
          },
          Qu = (e) => {
            let u = e.children,
              t = e.contentId,
              r = e.args,
              n = e.onMouseEnter,
              o = e.onMouseLeave,
              i = e.onMouseDown,
              s = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              E = e.ignoreMouseClick,
              m = void 0 !== E && E,
              _ = e.decoratorId,
              d = void 0 === _ ? 0 : _,
              A = e.isEnabled,
              F = void 0 === A || A,
              D = e.targetId,
              C = void 0 === D ? 0 : D,
              B = e.onShow,
              h = e.onHide,
              g = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(e);
                for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, Ku);
            const p = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              f = (0, a.useMemo)(
                () =>
                  C ||
                  ((e = 1) => {
                    const u = new Error().stack;
                    let t,
                      r = R.invalid("resId");
                    return (
                      u &&
                        ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== t &&
                          window.subViews[t] &&
                          (r = window.subViews[t].id)),
                      { caller: t, stack: u, resId: r }
                    );
                  })().resId,
                [C],
              ),
              v = (0, a.useCallback)(() => {
                (p.current.isVisible && p.current.timeoutId) ||
                  (Zu(t, d, { isMouseEvent: !0, on: !0, arguments: qu(r) }, f),
                  B && B(),
                  (p.current.isVisible = !0));
              }, [t, d, r, f, B]),
              b = (0, a.useCallback)(() => {
                if (p.current.isVisible || p.current.timeoutId) {
                  const e = p.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (p.current.timeoutId = 0)),
                    Zu(t, d, { on: !1 }, f),
                    p.current.isVisible && h && h(),
                    (p.current.isVisible = !1));
                }
              }, [t, d, f, h]),
              w = (0, a.useCallback)((e) => {
                p.current.isVisible &&
                  ((p.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (p.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(p.current.prevTarget) && b();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const e = p.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === F && b();
              }, [F, b]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", b),
                  () => {
                    (window.removeEventListener("mouseleave", b), b());
                  }
                ),
                [b],
              ));
            return F
              ? (0, a.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((p.current.timeoutId = window.setTimeout(v, c ? 100 : 400)),
                            n && n(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (b(), null == o || o(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === m && b(), null == s || s(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === m && b(), null == i || i(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    g,
                  ),
                )
              : u;
            var x;
          },
          Ju = ["children", "body", "header", "note", "alert", "args"];
        function et() {
          return (
            (et =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            et.apply(this, arguments)
          );
        }
        const ut = R.views.common.tooltip_window.simple_tooltip_content,
          tt = (e) => {
            let u = e.children,
              t = e.body,
              r = e.header,
              n = e.note,
              i = e.alert,
              s = e.args,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(e);
                for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, Ju);
            const c = (0, a.useMemo)(() => {
              const e = Object.assign({}, s, { body: t, header: r, note: n, alert: i });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [i, t, r, n, s]);
            return o().createElement(
              Qu,
              et(
                {
                  contentId:
                    ((E = null == s ? void 0 : s.hasHtmlContent),
                    E ? ut.SimpleTooltipHtmlContent("resId") : ut.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              u,
            );
            var E;
          },
          rt = {
            blackReal: "FormatTextWithColorTags_blackReal_3c",
            whiteReal: "FormatTextWithColorTags_whiteReal_8a",
            white: "FormatTextWithColorTags_white_16",
            whiteOrange: "FormatTextWithColorTags_whiteOrange_18",
            whiteSpanish: "FormatTextWithColorTags_whiteSpanish_10",
            par: "FormatTextWithColorTags_par_ca",
            parSecondary: "FormatTextWithColorTags_parSecondary_8d",
            parTertiary: "FormatTextWithColorTags_parTertiary_a3",
            red: "FormatTextWithColorTags_red_60",
            redDark: "FormatTextWithColorTags_redDark_03",
            yellow: "FormatTextWithColorTags_yellow_ad",
            orange: "FormatTextWithColorTags_orange_e4",
            cream: "FormatTextWithColorTags_cream_cd",
            brown: "FormatTextWithColorTags_brown_c8",
            greenBright: "FormatTextWithColorTags_greenBright_f0",
            green: "FormatTextWithColorTags_green_c5",
            greenDark: "FormatTextWithColorTags_greenDark_af",
            blueBooster: "FormatTextWithColorTags_blueBooster_ac",
            blueTeamkiller: "FormatTextWithColorTags_blueTeamkiller_6f",
            cred: "FormatTextWithColorTags_cred_4e",
            gold: "FormatTextWithColorTags_gold_90",
            bond: "FormatTextWithColorTags_bond_71",
            prom: "FormatTextWithColorTags_prom_dd",
          },
          nt =
            /(?:%\(|{)\w*(?:_[Oo]pen|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Cc]lose|End)(?:\)s|})?/g,
          at = /(?<=(?:%\(|{))(.*?)(?=(?:_[Oo]pen|Start))/,
          ot = /(?<=(?:_[Oo]pen|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
          it = (0, a.memo)(({ text: e, binding: u, classMix: t }) => {
            const r = (0, a.useCallback)((e) => ({ color: `#${e}` }), []),
              n = (0, a.useMemo)(() => u || {}, [u]);
            let i = nt.exec(e),
              s = e,
              l = 0;
            for (; i;) {
              const t = i[0],
                a = at.exec(t),
                c = ot.exec(t),
                E = i[1];
              if (a && c) {
                const e = a[0],
                  i = e + l++ + e;
                ((s = s.replace(t, `%(${i})`)),
                  (n[i] = rt[e]
                    ? o().createElement(
                        "span",
                        { className: rt[e] },
                        o().createElement(yu, { text: E, binding: u }),
                      )
                    : o().createElement(
                        "span",
                        { style: r(e) },
                        o().createElement(yu, { text: E, binding: u }),
                      )));
              }
              i = nt.exec(e);
            }
            return o().createElement(yu, { text: s, classMix: t, binding: n });
          }),
          st = "Card_base_00",
          lt = "Card_wrapper_9e",
          ct = "Card_nationImage_e0",
          Et = "Card_vehicleImage_07",
          mt = "Card_overlay_44",
          _t = "Card_text_b9",
          dt = "Card_vehicleName_fc",
          At = "Card_additionsText_cb",
          Ft = "Card_crewIcon_de",
          Dt = "Card_hangarIcon_1f",
          Ct = "Card_compareButton_36",
          Bt = R.strings.battle_matters.vehicleSelection,
          ht = (0, q.Pi)(
            ({
              vehicleName: e,
              vehicleType: u,
              nation: t,
              level: r,
              vehicleCD: n,
              userName: a,
            }) => {
              const i = le().controls,
                s = R.images.gui.maps.shop.vehicles.c_360x270.$dyn(fu(e)),
                l = R.images.gui.maps.shop.nations.$dyn(`flag_${t}`);
              return o().createElement(
                "div",
                {
                  className: st,
                  onMouseEnter: () => {
                    G.playHighlight();
                  },
                },
                o().createElement(
                  "div",
                  {
                    className: lt,
                    onClick: () => {
                      (i.showVehicle(n), G.playClick());
                    },
                  },
                  o().createElement("div", {
                    className: ct,
                    style: { backgroundImage: `url(${l})` },
                  }),
                  o().createElement("div", {
                    className: Et,
                    style: { backgroundImage: `url(${s})` },
                  }),
                  o().createElement("div", { className: mt }),
                  o().createElement(
                    "div",
                    { className: _t },
                    o().createElement(it, {
                      text: Bt.vehicleName(),
                      binding: {
                        type: Bt.vehicleType.$dyn(fu(u)),
                        level: ((c = r), Yu ? `${c}` : Xu(c)),
                        name: a,
                      },
                      classMix: dt,
                    }),
                    o().createElement(it, {
                      text: Bt.additions.base(),
                      binding: {
                        crewIcon: o().createElement("div", { className: Ft }),
                        hangarIcon: o().createElement("div", { className: Dt }),
                      },
                      classMix: At,
                    }),
                  ),
                ),
                o().createElement(
                  tt,
                  { body: Bt.compare.tooltip.body() },
                  o().createElement("div", {
                    className: Ct,
                    onClick: () => {
                      (i.compareVehicle(n), G.playClick());
                    },
                  }),
                ),
              );
              var c;
            },
          ),
          gt = "Cards_base_68",
          pt = "Cards_card_3b",
          ft = "Cards_card__lastInRow_d7",
          vt = (0, q.Pi)(() => {
            const e = le().model;
            return o().createElement(
              "div",
              { className: gt },
              e.computes
                .getVehicles()
                .map((e, u) =>
                  o().createElement(
                    "div",
                    { key: e.vehCD, className: p()(pt, (u + 1) % 3 == 0 && ft) },
                    o().createElement(ht, {
                      vehicleName: e.vehName,
                      vehicleType: e.vehType,
                      nation: e.nation,
                      level: e.level,
                      vehicleCD: e.vehCD,
                      userName: e.userName,
                    }),
                  ),
                ),
            );
          }),
          bt = "DefaultView_base_e8",
          wt = "DefaultView_container_63",
          xt = "DefaultView_title_11",
          Mt = "DefaultView_subtitle_14",
          St = "DefaultView_tokenExpiring_d9",
          Tt = "DefaultView_noFilteredVehicles_a5",
          yt = "DefaultView_cards_71",
          Lt = "DefaultView_scrollSensitiveArea_ea",
          Rt = "DefaultView_scrollableArea_f3",
          Ot = "DefaultView_scrollBar_f7",
          Nt = {
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
        let kt, Ht;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(kt || (kt = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(Ht || (Ht = {})));
        const Pt = ({
          children: e,
          size: u,
          isFocused: t,
          type: r,
          disabled: n,
          mixClass: i,
          soundHover: s,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: E,
          onMouseDown: m,
          onMouseUp: _,
          onMouseLeave: d,
          onClick: A,
        }) => {
          const F = (0, a.useRef)(null),
            D = (0, a.useState)(t),
            C = D[0],
            B = D[1],
            h = (0, a.useState)(!1),
            g = h[0],
            f = h[1],
            v = (0, a.useState)(!1),
            b = v[0],
            w = v[1],
            x = (0, a.useCallback)(() => {
              n || (F.current && (F.current.focus(), B(!0)));
            }, [n]),
            M = (0, a.useCallback)(
              (e) => {
                C && null !== F.current && !F.current.contains(e.target) && B(!1);
              },
              [C],
            ),
            S = (0, a.useCallback)(
              (e) => {
                n || (A && A(e));
              },
              [n, A],
            ),
            T = (0, a.useCallback)(
              (e) => {
                n || (null !== s && W(s), c && c(e), w(!0));
              },
              [n, s, c],
            ),
            y = (0, a.useCallback)(
              (e) => {
                E && E(e);
              },
              [E],
            ),
            L = (0, a.useCallback)(
              (e) => {
                n || (_ && _(e), f(!1));
              },
              [n, _],
            ),
            O = (0, a.useCallback)(
              (e) => {
                n || (null !== l && W(l), m && m(e), t && x(), f(!0));
              },
              [n, l, m, x, t],
            ),
            N = (0, a.useCallback)(
              (e) => {
                n || (d && d(e), f(!1));
              },
              [n, d],
            ),
            k = p()(
              Nt.base,
              Nt[`base__${r}`],
              {
                [Nt.base__disabled]: n,
                [Nt[`base__${u}`]]: u,
                [Nt.base__focus]: C,
                [Nt.base__highlightActive]: g,
                [Nt.base__firstHover]: b,
              },
              i,
            ),
            H = p()(Nt.state, Nt.state__default);
          return (
            (0, a.useEffect)(
              () => (
                document.addEventListener("mousedown", M),
                () => {
                  document.removeEventListener("mousedown", M);
                }
              ),
              [M],
            ),
            (0, a.useEffect)(() => {
              B(t);
            }, [t]),
            o().createElement(
              "div",
              {
                ref: F,
                className: k,
                onMouseEnter: T,
                onMouseMove: y,
                onMouseUp: L,
                onMouseDown: O,
                onMouseLeave: N,
                onClick: S,
              },
              r !== kt.ghost &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", { className: Nt.back }),
                  o().createElement("span", { className: Nt.texture }),
                ),
              o().createElement(
                "span",
                { className: H },
                o().createElement("span", { className: Nt.stateDisabled }),
                o().createElement("span", { className: Nt.stateHighlightHover }),
                o().createElement("span", { className: Nt.stateHighlightActive }),
              ),
              o().createElement(
                "span",
                { className: Nt.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Pt.defaultProps = {
          type: kt.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const It = (0, a.memo)(Pt),
          Wt = "NoFilteredVehicles_base_64",
          Gt = "NoFilteredVehicles_header_f2",
          Ut = "NoFilteredVehicles_alertIcon_19",
          Vt = "NoFilteredVehicles_text_ec",
          zt = R.strings.battle_matters.vehicleSelection,
          jt = (0, q.Pi)(() => {
            const e = le().controls;
            return o().createElement(
              "div",
              { className: Wt },
              o().createElement(
                "div",
                { className: Gt },
                o().createElement("div", { className: Ut }),
                o().createElement("div", { className: Vt }, zt.noFilteredVehicles()),
              ),
              o().createElement(
                It,
                { type: kt.secondary, size: Ht.small, onClick: e.resetFilter },
                zt.noFilteredVehiclesResetButton(),
              ),
            );
          }),
          $t = ["children"];
        function Xt() {
          return (
            (Xt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Xt.apply(this, arguments)
          );
        }
        const Yt = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                r,
                n = {},
                a = Object.keys(e);
              for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
              return n;
            })(e, $t);
          return o().createElement(
            Qu,
            Xt(
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
        };
        function Kt() {
          return (
            (Kt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Kt.apply(this, arguments)
          );
        }
        const qt = ({ children: e, tooltipArgs: u, className: t }) => {
            if (!u) return e;
            const r = o().createElement("div", { className: t }, e);
            if (u.header || u.body) return o().createElement(tt, u, r);
            const n = u.contentId,
              a = u.args,
              i = null == a ? void 0 : a.contentId;
            return n || i
              ? o().createElement(Qu, Kt({}, u, { contentId: n || i }), r)
              : o().createElement(Yt, u, r);
          },
          Zt = "default",
          Qt = "search",
          Jt = "email",
          er = "password",
          ur = "normal",
          tr = "disabled",
          rr = "alert",
          nr = "error",
          ar = "medium",
          or = {
            [Zt]: "",
            [Jt]: R.strings.common.input.placeholder.email(),
            [Qt]: R.strings.common.input.placeholder.search(),
            [er]: R.strings.common.input.placeholder.password(),
          },
          ir = { [Zt]: "text", [Jt]: "text", [Qt]: "text", [er]: "password" },
          sr = { [Zt]: "", [Jt]: "Invalid email", [Qt]: "", [er]: "" },
          lr = R.images.gui.maps.icons.components.input;
        function cr(e, u) {
          return (
            u !== Jt ||
            (function (e) {
              const u = e.match(
                /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
              );
              return Boolean(u);
            })(e)
          );
        }
        const Er = {
            base: "InputControl_base_68",
            base__focused: "InputControl_base__focused_aa",
            base__alert: "InputControl_base__alert_22",
            base__error: "InputControl_base__error_ff",
            base__done: "InputControl_base__done_a7",
            base__disabled: "InputControl_base__disabled_f8",
            input: "InputControl_input_93",
            base__small: "InputControl_base__small_85",
            base__medium: "InputControl_base__medium_a2",
            base__large: "InputControl_base__large_32",
            base__withIcon: "InputControl_base__withIcon_9e",
            input__search: "InputControl_input__search_85",
            disabled: "InputControl_disabled_78",
            placeholder: "InputControl_placeholder_e3",
            placeholder__search: "InputControl_placeholder__search_d5",
            icon: "InputControl_icon_13",
            icon__search: "InputControl_icon__search_57",
            clear: "InputControl_clear_bb",
          },
          mr = o().memo(
            ({
              componentId: e,
              value: u = "",
              type: t = Zt,
              size: r = ar,
              variant: n = ur,
              placeholder: i = "",
              highlighted: s,
              withClear: l,
              selectOnFocus: c = !0,
              maxLength: E,
              iconSource: m,
              classMix: _,
              onMouseEnter: d,
              onMouseLeave: A,
              onMouseDown: F,
              onMouseUp: D,
              onClick: C,
              onChange: B,
              onClear: h,
              onFocus: g,
              onBlur: f,
            }) => {
              const v = (0, a.useState)(!1),
                b = v[0],
                w = v[1],
                x = (0, a.useRef)(null),
                M = (0, a.useRef)({ mouseOver: !1, mouseDown: !1 }),
                S = n !== tr,
                T = (0, a.useCallback)(
                  (e) => {
                    S && (w(!0), g && g(e));
                  },
                  [S, g],
                ),
                y = (0, a.useCallback)(
                  (e) => {
                    S && !M.current.mouseOver && (w(!1), f && f(e));
                  },
                  [S, f],
                );
              (0, a.useEffect)(() => {
                S && b && c && x.current && x.current.select();
              }, [c, b, S]);
              const L = (0, a.useCallback)(
                  (e) => {
                    S && B && B(e.target.value);
                  },
                  [S, B],
                ),
                R = (0, a.useCallback)(
                  (e) => {
                    S && ((M.current.mouseOver = !0), d && d(e));
                  },
                  [S, d],
                ),
                O = (0, a.useCallback)(
                  (e) => {
                    S &&
                      x.current &&
                      (M.current.mouseDown && x.current.focus(),
                      (M.current.mouseOver = !1),
                      A && A(e));
                  },
                  [S, A],
                ),
                N = (0, a.useCallback)(
                  (e) => {
                    S && ((M.current.mouseDown = !0), F && F(e));
                  },
                  [S, F],
                ),
                k = (0, a.useCallback)(
                  (e) => {
                    S && ((M.current.mouseDown = !1), D && D(e));
                  },
                  [S, D],
                ),
                H = (0, a.useCallback)(
                  (e) => {
                    if (S && x.current) {
                      ((!b || (b && e.target !== x.current)) && x.current.focus(), C && C(e));
                    }
                  },
                  [b, S, C],
                ),
                P = i || or[t],
                I = Boolean(m),
                W = p()(
                  Er.base,
                  Er[`base__${r}`],
                  s && Er[`base__${n}`],
                  b && Er.base__focused,
                  I && Er.base__withIcon,
                  _,
                ),
                U = (0, a.useMemo)(() => (m ? { backgroundImage: `url(${m})` } : null), [m]),
                V = p()(Er.input, Er[`input__${t}`]),
                z = p()(Er.icon, Er[`icon__${t}`]),
                j = p()(Er.placeholder, Er[`placeholder__${t}`]);
              return o().createElement(
                "div",
                {
                  id: e,
                  className: W,
                  onMouseEnter: R,
                  onMouseDown: N,
                  onMouseUp: k,
                  onMouseLeave: O,
                  onClick: H,
                },
                !S && o().createElement("div", { className: Er.disabled }),
                U && o().createElement("div", { style: U, className: z }),
                o().createElement("input", {
                  ref: x,
                  className: V,
                  type: ir[t],
                  value: u,
                  onChange: L,
                  disabled: !S,
                  onFocus: T,
                  onBlur: y,
                  maxLength: E,
                }),
                P && !u && !b && o().createElement("div", { className: j }, P),
                l &&
                  o().createElement("div", {
                    className: Er.clear,
                    onClick: (e) => {
                      (G.playClick(), h && h(e));
                    },
                    onMouseEnter: G.playHighlight,
                  }),
              );
            },
          ),
          _r = {
            base: "HelperMessage_base_1e",
            base__shown: "HelperMessage_base__shown_ab",
            icon: "HelperMessage_icon_10",
            message: "HelperMessage_message_f4",
            message__alert: "HelperMessage_message__alert_b5",
            message__error: "HelperMessage_message__error_45",
            message__done: "HelperMessage_message__done_2b",
          },
          dr = ({ variant: e, show: u = !0, helperText: t, helperIcon: r, classMix: n }) => {
            const i = (0, a.useMemo)(() => {
                const u =
                  r ||
                  (function (e) {
                    return e === rr ? R.images.gui.maps.icons.library.alertIcon() : "";
                  })(e);
                return u && { backgroundImage: `url(${u})` };
              }, [r, e]),
              s = p()(_r.base, u && _r.base__shown),
              l = p()(_r.message, _r[`message__${e}`], n);
            return o().createElement(
              "div",
              { className: s },
              i && o().createElement("div", { className: _r.icon, style: i }),
              o().createElement("div", { className: l }, t),
            );
          },
          Ar = {
            base: "Input_base_cd",
            base__small: "Input_base__small_c7",
            base__medium: "Input_base__medium_1f",
            base__large: "Input_base__large_11",
            helper: "Input_helper_ea",
          },
          Fr = [
            "componentId",
            "type",
            "variant",
            "size",
            "value",
            "tooltipArgs",
            "helperText",
            "isValidated",
            "showHelper",
            "error",
            "options",
            "onFocus",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseUp",
            "onMouseDown",
            "onChange",
            "classMix",
            "controlClassMix",
            "helperClassMix",
          ];
        function Dr() {
          return (
            (Dr =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            Dr.apply(this, arguments)
          );
        }
        const Cr = {
            debounceTime: 200,
            performChangeValidation: !0,
            selectOnFocus: !0,
            withTypeIcon: !0,
            disableHighlightOnFocus: !0,
          },
          Br = (e) => {
            let u = e.componentId,
              t = e.type,
              r = void 0 === t ? Zt : t,
              n = e.variant,
              i = void 0 === n ? ur : n,
              s = e.size,
              l = void 0 === s ? ar : s,
              c = e.value,
              E = e.tooltipArgs,
              m = e.helperText,
              _ = void 0 === m ? "" : m,
              d = e.isValidated,
              A = void 0 === d || d,
              F = e.showHelper,
              D = void 0 === F || F,
              C = e.error,
              B = e.options,
              h = e.onFocus,
              g = e.onMouseEnter,
              f = e.onMouseLeave,
              v = e.onMouseUp,
              b = e.onMouseDown,
              w = e.onChange,
              x = e.classMix,
              M = e.controlClassMix,
              S = e.helperClassMix,
              T = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(e);
                for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, Fr);
            const y = (0, a.useState)(c),
              L = y[0],
              R = y[1],
              O = (0, a.useState)(A),
              N = O[0],
              k = O[1],
              H = (0, a.useMemo)(() => Object.assign({}, Cr, B), [B]),
              P = (0, a.useRef)({ debounceTimeout: 0, isChangeHandled: !0, value: c, type: r }),
              I = (0, a.useCallback)((e) => {
                e !== P.current.value &&
                  ((P.current.value = e), (P.current.isChangeHandled = !1), R(e));
              }, []),
              W = (0, a.useCallback)(
                (e) => {
                  let u = !0;
                  (H.performChangeValidation &&
                    (u = H.changesValidator ? H.changesValidator(e) : cr(e, P.current.type)),
                    w && w(e, u));
                },
                [w, H],
              ),
              G = (0, a.useCallback)(() => {
                P.current.debounceTimeout &&
                  (window.clearTimeout(P.current.debounceTimeout), (P.current.debounceTimeout = 0));
              }, []),
              U = (0, a.useCallback)(() => I(""), [I]);
            (0, a.useEffect)(() => () => G(), [G]);
            const V = (0, a.useCallback)(
              (e) => {
                (G(),
                  H.debounceTime
                    ? (P.current.debounceTimeout = window.setTimeout(() => {
                        W(e);
                      }, H.debounceTime))
                    : W(e));
              },
              [W, G, H.debounceTime],
            );
            ((0, a.useEffect)(() => {
              P.current.isChangeHandled ||
                P.current.value !== L ||
                (V(P.current.value), (P.current.isChangeHandled = !0));
            }, [L, V]),
              (0, a.useEffect)(() => {
                (P.current.isChangeHandled &&
                  c !== P.current.value &&
                  ((P.current.value = c), R(c)),
                  (P.current.type = r));
              }, [c, r]),
              (0, a.useEffect)(() => {
                k(A);
              }, [A, i]));
            const z = (0, a.useCallback)((e) => g && g(e), [g]),
              j = (0, a.useCallback)(
                (e) => {
                  (H.disableHighlightOnFocus && N && k(!1), h && h(e));
                },
                [N, h, H.disableHighlightOnFocus],
              ),
              $ = (0, a.useCallback)((e) => v && v(e), [v]),
              X = (0, a.useCallback)((e) => b && b(e), [b]),
              Y = (0, a.useCallback)((e) => f && f(e), [f]),
              K = (0, a.useMemo)(
                () =>
                  H.withTypeIcon
                    ? (function (e, u) {
                        return e === Qt ? lr.$dyn(`search_${u}`) : "";
                      })(r, l)
                    : "",
                [r, l, H.withTypeIcon],
              ),
              q = _ || sr[r],
              Z = Boolean(L),
              Q = C ? nr : i,
              J = Boolean(C) || N,
              ee = (0, a.useMemo)(
                () => ("boolean" == typeof H.withClear ? Z && H.withClear : Z && r === Qt),
                [r, Z, H],
              ),
              ue = p()(Ar.base, Ar[`base__${l}`], Ar[`base__${i}`], x);
            return o().createElement(
              "div",
              {
                id: u,
                className: ue,
                onMouseEnter: z,
                onMouseDown: X,
                onMouseUp: $,
                onMouseLeave: Y,
              },
              o().createElement(
                qt,
                { tooltipArgs: E },
                o().createElement(
                  mr,
                  Dr(
                    {
                      componentId: u ? `${u}-inputControl` : void 0,
                      iconSource: K,
                      size: l,
                      type: r,
                      variant: Q,
                      value: L,
                      withClear: ee,
                      highlighted: J,
                      selectOnFocus: H.selectOnFocus,
                      maxLength: H.maxLength,
                      classMix: M,
                      onFocus: j,
                      onChange: I,
                      onClear: U,
                    },
                    T,
                  ),
                ),
              ),
              q &&
                o().createElement(
                  "div",
                  { className: Ar.helper },
                  o().createElement(dr, {
                    variant: Q,
                    show: D && (H.isPermanentHelper || J),
                    helperText: C || q,
                    helperIcon: H.helperIconSource,
                    classMix: S,
                  }),
                ),
            );
          },
          hr = (e) => {
            (0, a.useEffect)(e, []);
          },
          gr = {
            base: "PopoverDecorator_base_ed",
            decorator: "PopoverDecorator_decorator_d3",
            arrow: "PopoverDecorator_arrow_8a",
            arrow__bottom: "PopoverDecorator_arrow__bottom_c3",
            arrow__top: "PopoverDecorator_arrow__top_6e",
            arrow__left: "PopoverDecorator_arrow__left_7a",
            arrow__right: "PopoverDecorator_arrow__right_b6",
            closeBtn: "PopoverDecorator_closeBtn_32",
            content: "PopoverDecorator_content_f0",
          };
        var pr;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(pr || (pr = {}));
        const fr = ["__left", "__right", "__top", "__bottom"],
          vr =
            ((0, a.forwardRef)(
              (
                { children: e, disableAutoSizeUpdate: u, onOutsideClick: t, customStyles: r = {} },
                n,
              ) => {
                const i = (0, a.useRef)(null),
                  l = (0, a.useRef)(null),
                  c = (0, a.useRef)(null),
                  E = (0, a.useState)(window.decorator && window.decorator.directionType),
                  m = E[0],
                  _ = E[1],
                  d = (0, a.useCallback)(() => {
                    (G.playClick(), s.O.view.sendEvent.close());
                  }, []),
                  A = (0, a.useCallback)(() => {
                    G.playHighlight();
                  }, []),
                  F = p()(gr.arrow, gr[`arrow${fr[m]}`]);
                hr(
                  () => (
                    s.O.client.events.mouse.enableOutside(),
                    s.O.client.events.mouse.down(([, e]) => {
                      "outside" === e && (t ? t() : s.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const D = (0, a.useCallback)(
                    (e) => {
                      let u = e.target;
                      do {
                        if (u === i.current || u === c.current) return;
                        u = u.parentNode;
                      } while (u);
                      const r = window.decorator;
                      if (void 0 !== window.decorator) {
                        const e = s.O.client.getMouseGlobalPosition(),
                          u = ![r.boundX, r.boundY, r.boundWidth, r.boundHeight].includes(void 0),
                          t =
                            e.x < r.boundX ||
                            e.x > r.boundX + r.boundWidth ||
                            e.y > r.boundY + r.boundHeight ||
                            e.y < r.boundY;
                        if (u && !t) return;
                      }
                      t ? t() : s.O.view.sendEvent.close("popover");
                    },
                    [i, c, t],
                  ),
                  C = (0, a.useCallback)(
                    () => (
                      s.O.view.freezeTextureBeforeResize(),
                      de(() => {
                        if (l.current) {
                          const e = l.current.scrollWidth,
                            u = l.current.scrollHeight;
                          (s.O.view.resize(e, u), _(window.decorator.directionType));
                        }
                      })
                    ),
                    [],
                  );
                return (
                  (0, a.useImperativeHandle)(n, () => ({ updateSize: C })),
                  hr(() => {
                    s.O.view.setInputPaddingsRem(58);
                  }),
                  (0, a.useEffect)(() => {
                    document.addEventListener("mousedown", D, { capture: !0 });
                    const e = ((e) => {
                      let u = !1;
                      return {
                        promise: new Promise((t, r) => {
                          e.then((e) => !u && t(e)).catch((e) => !u && r(e));
                        }),
                        cancel() {
                          u = !0;
                        },
                      };
                    })((0, X.Eu)());
                    return (
                      !u && e.promise.then(() => C()),
                      () => {
                        (e.cancel(), document.removeEventListener("mousedown", D));
                      }
                    );
                  }, [C, D, u]),
                  o().createElement(
                    "div",
                    { className: gr.base, ref: l },
                    o().createElement(
                      "div",
                      { className: gr.decorator },
                      o().createElement(
                        "div",
                        { className: gr.content, ref: i },
                        e,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          o().createElement(
                            tt,
                            { body: R.strings.dialogs.common.error.cancel() },
                            o().createElement("div", {
                              className: gr.closeBtn,
                              onClick: d,
                              onMouseEnter: A,
                              ref: c,
                            }),
                          ),
                      ),
                      o().createElement("div", { className: F, style: r.arrow }),
                    ),
                  )
                );
              },
            ),
            [
              "contentId",
              "decoratorId",
              "direction",
              "targetId",
              "args",
              "onClick",
              "children",
              "isEnabled",
            ]);
        function br() {
          return (
            (br =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (e[r] = t[r]);
                }
                return e;
              }),
            br.apply(this, arguments)
          );
        }
        const wr = (e) => {
            let u = e.contentId,
              t = e.decoratorId,
              r = e.direction,
              n = void 0 === r ? pr.Top : r,
              i = e.targetId,
              s = e.args,
              l = e.onClick,
              c = e.children,
              E = e.isEnabled,
              m = void 0 === E || E,
              _ = (function (e, u) {
                if (null == e) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(e);
                for (r = 0; r < a.length; r++) ((t = a[r]), u.indexOf(t) >= 0 || (n[t] = e[t]));
                return n;
              })(e, vr);
            const d = (0, a.useRef)(null),
              A = (0, a.useCallback)(() => {
                if ((0, X.wU)()) return (0, X.SW)();
                d.current && (0, X.P3)(u, n, d.current, t, i, s);
              }, [u, n, s, t, i]);
            return o().createElement(
              "div",
              br(
                {
                  ref: d,
                  onClick:
                    ((F = c.props.onClick),
                    (e) => {
                      m && (A(), l && l(e), F && F(e));
                    }),
                },
                _,
              ),
              c,
            );
            var F;
          },
          xr = "SearchPanel_base_0e",
          Mr = "SearchPanel_controls_c6",
          Sr = "SearchPanel_searchField_ce",
          Tr = "SearchPanel_input_6c",
          yr = "SearchPanel_filterButton_62",
          Lr = "SearchPanel_filterButtonIcon_77",
          Rr = "SearchPanel_divider_20",
          Or = "SearchResult_base_a4",
          Nr = "SearchResult_text_59",
          kr = "SearchResult_filterApplied_9e",
          Hr = "SearchResult_filterAppliedIcon_d9",
          Pr = "SearchResult_showedCount_78",
          Ir = "SearchResult_filterApplied__empty_d8",
          Wr = "SearchResult_searchResults_53",
          Gr = "SearchResult_resetHoverArea_5c",
          Ur = "SearchResult_resetIconBg_8c",
          Vr = "SearchResult_resetIcon_15",
          zr = R.strings.battle_matters.vehicleSelection,
          jr = (0, q.Pi)(() => {
            const e = le(),
              u = e.model,
              t = e.controls,
              r = u.totalVehiclesCount.get(),
              n = u.computes.getVehiclesCount();
            return o().createElement(
              "div",
              { className: Or },
              o().createElement("div", { className: Nr }, zr.showed()),
              r === n
                ? o().createElement("div", { className: Pr }, n)
                : o().createElement(
                    "div",
                    { className: p()(kr, 0 === n && Ir) },
                    o().createElement("div", { className: Hr }),
                    o().createElement(it, {
                      text: zr.searchResults(),
                      classMix: Wr,
                      binding: {
                        showedCount: o().createElement("div", { className: Pr }, n),
                        totalCount: r,
                      },
                    }),
                  ),
              u.computes.isFilterApplied() &&
                o().createElement(
                  tt,
                  {
                    header: zr.filter.tooltip.reset.header(),
                    body: zr.filter.tooltip.reset.description(),
                  },
                  o().createElement(
                    "div",
                    { className: Gr, onClick: t.resetFilter },
                    o().createElement("div", { className: Ur }),
                    o().createElement("div", { className: Vr }),
                  ),
                ),
            );
          }),
          $r = R.strings.battle_matters.vehicleSelection,
          Xr = { maxLength: 50 },
          Yr = (0, q.Pi)(() => {
            const e = le(),
              u = e.model,
              t = e.controls,
              r = De((e) => {
                t.setFilter(e);
              });
            return o().createElement(
              "div",
              { className: xr },
              o().createElement(jr, null),
              o().createElement(
                "div",
                { className: Mr },
                o().createElement(
                  tt,
                  {
                    header: $r.search.tooltip.header(),
                    body:
                      ((n = $r.search.tooltip.body()),
                      (a = { maxLength: 50 }),
                      n.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
                        const u = 0 === e.indexOf("%") ? 2 : 1;
                        return String(a[e.slice(u, -u)]);
                      })),
                  },
                  o().createElement(
                    "div",
                    { className: Sr },
                    o().createElement(Br, {
                      value: u.filterString.get(),
                      type: Qt,
                      placeholder: $r.search.placeholder(),
                      onChange: r,
                      options: Xr,
                      classMix: Tr,
                    }),
                  ),
                ),
                o().createElement(
                  wr,
                  {
                    contentId:
                      R.views.lobby.battle_matters.popovers.BattleMattersFilterPopoverView("resId"),
                    direction: pr.Bottom,
                  },
                  o().createElement(
                    tt,
                    { header: $r.filter.tooltip.header(), body: $r.filter.tooltip.body() },
                    o().createElement(
                      It,
                      { mixClass: yr },
                      o().createElement("div", { className: Lr }),
                    ),
                  ),
                ),
              ),
              o().createElement("div", { className: Rr }),
            );
            var n, a;
          });
        let Kr;
        !(function (e) {
          ((e.SHORT_DATE = "short-date"),
            (e.SHORT_TIME = "short-time"),
            (e.SHORT_DATE_TIME = "short-date-time"),
            (e.FULL_DATE = "full-date"),
            (e.FULL_DATE_TIME = "full-date-time"),
            (e.MONTH = "month"),
            (e.MONTH_DATE = "month-date"),
            (e.DATE_MONTH = "date-month"),
            (e.MONTH_YEAR = "month-year"),
            (e.WEEK_DAY = "week-day"),
            (e.WEEK_DAY_TIME = "week-day-time"),
            (e.YEAR = "year"),
            (e.DATE_YEAR = "date-year"));
        })(Kr || (Kr = {}));
        const qr = 1e3,
          Zr = 60,
          Qr = 3600,
          Jr = 86400;
        Date.now();
        const en = () => {},
          un = (e = 0, u, t = 0, r = en) => {
            const n = (0, a.useState)(e),
              o = n[0],
              i = n[1];
            return (
              (0, a.useEffect)(() => {
                if (e > 0) {
                  i(e);
                  const n = Date.now(),
                    a = setInterval(
                      () => {
                        const u = e - Math.floor((Date.now() - n) / qr);
                        null !== t && u <= t ? (i(t), r && r(), clearInterval(a)) : i(u);
                      },
                      (u || (e > 120 ? Zr : 1)) * qr,
                    );
                  return () => {
                    clearInterval(a);
                  };
                }
                i(0);
              }, [e, u, t, r]),
              o
            );
          };
        X.Sw.instance;
        let tn;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(tn || (tn = {}));
        X.Sw.instance;
        const rn = un,
          nn = "Timer_base_41",
          an = "Timer_icon_26",
          on = (0, a.memo)(({ endDate: e, className: u }) => {
            const t = Math.floor(Date.now() / qr),
              r = (function (e = 0) {
                let u = e;
                const t = Math.trunc(u / Jr);
                u -= t * Jr;
                const r = Math.trunc(u / Qr);
                u -= r * Qr;
                const n = Math.trunc(u / Zr);
                return ((u -= n * Zr), { days: t, hours: r, minutes: n, seconds: u });
              })(rn(e - t, 1)),
              n = ((e, u, t) => {
                switch (u) {
                  case Kr.SHORT_DATE:
                    return t
                      ? X.Z5.getDateFormat(e, X.kH.SHORT_FORMAT)
                      : X.cy.getTimeFormat("%d.%m.%y", e, !0);
                  case Kr.SHORT_TIME:
                    return t
                      ? X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)
                      : X.cy.getTimeFormat("%I:%M %p", e, !0);
                  case Kr.SHORT_DATE_TIME:
                    return t
                      ? `${X.Z5.getDateFormat(e, X.kH.SHORT_FORMAT)}, ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                      : X.cy.getTimeFormat("%d.%m.%y, %I:%M %p", e, !0);
                  case Kr.FULL_DATE:
                    return t
                      ? X.Z5.getDateFormat(e, X.kH.LONG_FORMAT)
                      : X.cy.getTimeFormat("%B %d, %Y", e, !0);
                  case Kr.FULL_DATE_TIME:
                    return t
                      ? `${X.Z5.getDateFormat(e, X.kH.LONG_FORMAT)}, ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                      : X.cy.getTimeFormat("%B %d, %Y, %I:%M %p", e, !0);
                  case Kr.MONTH:
                    return X.cy.getTimeFormat("%B", e, !0);
                  case Kr.MONTH_DATE:
                    return X.cy.getTimeFormat("%B %e", e, !0);
                  case Kr.DATE_MONTH:
                    return X.cy.getTimeFormat("%e %B", e, !0);
                  case Kr.MONTH_YEAR:
                    return X.cy.getTimeFormat("%B %Y", e, !0);
                  case Kr.WEEK_DAY:
                    return X.cy.getTimeFormat("%A", e, !0);
                  case Kr.WEEK_DAY_TIME:
                    return t
                      ? `${X.cy.getTimeFormat("%A", e, !0)} ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                      : X.cy.getTimeFormat("%A, %I:%M %p", e, !0);
                  case Kr.YEAR:
                    return X.cy.getTimeFormat("%Y", e, !0);
                  case Kr.DATE_YEAR:
                    return X.cy.getTimeFormat("%d, %Y", e, !0);
                }
              })(e, Kr.FULL_DATE, !0).replaceAll(" ", " ");
            return o().createElement(
              "div",
              { className: p()(nn, u) },
              o().createElement("div", { className: an }),
              (() => {
                if (r.days > 30)
                  return o().createElement(it, {
                    text: R.strings.battle_matters.tokenTooltip.timer.fullDate(),
                    binding: { fullDate: n },
                  });
                if (r.days)
                  return o().createElement(it, {
                    text: R.strings.battle_matters.tokenTooltip.timer.days(),
                    binding: { days: r.days },
                  });
                if (r.hours)
                  return o().createElement(it, {
                    text: R.strings.battle_matters.tokenTooltip.timer.hours(),
                    binding: { hours: r.hours },
                  });
                if (r.minutes) {
                  const e = r.seconds >= 30;
                  return 59 === r.minutes && e
                    ? o().createElement(it, {
                        text: R.strings.battle_matters.tokenTooltip.timer.hours(),
                        binding: { hours: 1 },
                      })
                    : o().createElement(it, {
                        text: R.strings.battle_matters.tokenTooltip.timer.minutes(),
                        binding: { minutes: e ? r.minutes + 1 : r.minutes },
                      });
                }
                return o().createElement(it, {
                  text: R.strings.battle_matters.tokenTooltip.timer.minutes(),
                  binding: { minutes: 1 },
                });
              })(),
            );
          }),
          sn = "TokenExpiring_base_b9",
          ln = "TokenExpiring_glow_9d",
          cn = "TokenExpiring_glow__left_a7",
          En = "TokenExpiring_timer_7f",
          mn = ({ endDate: e }) =>
            o().createElement(
              "div",
              { className: sn },
              o().createElement("div", { className: p()(ln, cn) }),
              o().createElement(on, { endDate: e, className: En }),
              o().createElement("div", { className: ln }),
            ),
          _n = R.strings.battle_matters.vehicleSelection,
          dn = (0, q.Pi)(() => {
            const e = le().model,
              u = e.endDate.get(),
              t = Xu(e.level.get()),
              r = Ve();
            return o().createElement(
              "div",
              { className: bt },
              o().createElement(zu, {
                className: xt,
                format: { binding: { level: t } },
                text: _n.title(),
              }),
              o().createElement(zu, {
                className: Mt,
                format: { binding: { level: t } },
                text: _n.subtitle(),
              }),
              0 !== u &&
                o().createElement("div", { className: St }, o().createElement(mn, { endDate: u })),
              o().createElement("div", { className: wt }, o().createElement(Yr, null)),
              0 === e.computes.getVehiclesCount()
                ? o().createElement("div", { className: Tt }, o().createElement(jt, null))
                : o().createElement(
                    "div",
                    { className: yt },
                    o().createElement(
                      iu.Vertical.Area,
                      { api: r, className: Lt, classNames: { content: Rt } },
                      o().createElement("div", { className: wt }, o().createElement(vt, null)),
                    ),
                    o().createElement(iu.Vertical.Bar, { api: r, classNames: { base: Ot } }),
                  ),
            );
          }),
          An = "NoVehicles_base_76",
          Fn = "NoVehicles_image_57",
          Dn = "NoVehicles_title_23",
          Cn = "NoVehicles_subtitle_ee",
          Bn = R.strings.battle_matters.vehicleSelection.noVehicles,
          hn = (0, q.Pi)(() => {
            const e = Xu(le().model.level.get());
            return o().createElement(
              "div",
              { className: An },
              o().createElement("div", { className: Fn }),
              o().createElement("div", { className: Dn }, Bn.title()),
              o().createElement(zu, {
                className: Cn,
                format: { binding: { level: e } },
                text: Bn.subtitle(),
              }),
            );
          }),
          gn = R.strings.battle_matters.vehicleSelection,
          pn = (0, q.Pi)(() => {
            const e = le(),
              u = e.model,
              t = e.controls;
            var r;
            ((r = t.goBack), K($.n.ESCAPE, r));
            const n = M().mediaSize === b.ExtraSmall;
            return o().createElement(
              "div",
              { className: p()(ce, u.isLoaded.get() && Ee) },
              o().createElement(J, { isBlurred: !0, onLoaded: t.loaded }),
              o().createElement(
                "div",
                { className: me },
                o().createElement(
                  "div",
                  { className: _e },
                  o().createElement(j, {
                    caption: gn.back(),
                    goto: n ? "" : gn.backTo(),
                    onClick: t.goBack,
                  }),
                ),
                0 === u.totalVehiclesCount.get()
                  ? o().createElement(hn, null)
                  : o().createElement(dn, null),
              ),
            );
          });
        engine.whenReady.then(() => {
          I().render(
            o().createElement(H, null, o().createElement(se, null, o().createElement(pn, null))),
            document.getElementById("root"),
          );
        });
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
    (__webpack_require__.O = (e, u, t, r) => {
      if (!u) {
        var n = 1 / 0;
        for (s = 0; s < deferred.length; s++) {
          for (var [u, t, r] = deferred[s], a = !0, o = 0; o < u.length; o++)
            (!1 & r || n >= r) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[o]))
              ? u.splice(o--, 1)
              : ((a = !1), r < n && (n = r));
          if (a) {
            deferred.splice(s--, 1);
            var i = t();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      r = r || 0;
      for (var s = deferred.length; s > 0 && deferred[s - 1][2] > r; s--)
        deferred[s] = deferred[s - 1];
      deferred[s] = [u, t, r];
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
    (__webpack_require__.j = 395),
    (() => {
      var e = { 395: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var r,
            n,
            [a, o, i] = t,
            s = 0;
          if (a.some((u) => 0 !== e[u])) {
            for (r in o) __webpack_require__.o(o, r) && (__webpack_require__.m[r] = o[r]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); s < a.length; s++)
            ((n = a[s]), __webpack_require__.o(e, n) && e[n] && e[n][0](), (e[n] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [965], () => __webpack_require__(19));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
