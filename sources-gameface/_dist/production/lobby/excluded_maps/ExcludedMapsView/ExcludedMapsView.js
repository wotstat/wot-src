(() => {
  var __webpack_modules__ = {
      926: (u) => {
        u.exports = {
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
      532: (u) => {
        u.exports = {
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
      887: (u) => {
        u.exports = {
          XS: "4rem",
          SM: "8rem",
          SMp: "10rem",
          MD: "16rem",
          MDp: "20rem",
          LG: "32rem",
          XL: "64rem",
        };
      },
      67: (u, e, t) => {
        "use strict";
        t.d(e, { O: () => X });
        var n = {};
        (t.r(n), t.d(n, { mouse: () => E, onResize: () => l }));
        var a = {};
        (t.r(a),
          t.d(a, {
            events: () => n,
            getMouseGlobalPosition: () => A,
            getSize: () => m,
            graphicsQuality: () => d,
          }));
        var r = {};
        (t.r(r), t.d(r, { getBgUrl: () => F, getTextureUrl: () => _ }));
        var o = {};
        function i(u) {
          return (e) => (
            engine.on(u, e),
            () => {
              engine.off(u, e);
            }
          );
        }
        function s(u) {
          viewEnv.setTrackMouseOnStage(u);
        }
        (t.r(o),
          t.d(o, {
            addModelObserver: () => M,
            addPreloadTexture: () => w,
            children: () => r,
            displayStatus: () => D,
            displayStatusIs: () => K,
            events: () => B,
            extraSize: () => $,
            forceTriggerMouseMove: () => j,
            freezeTextureBeforeResize: () => O,
            getBrowserTexturePath: () => T,
            getDisplayStatus: () => V,
            getScale: () => k,
            getSize: () => L,
            getViewGlobalPosition: () => R,
            isClientAccessible: () => W,
            isEventHandled: () => U,
            isFocused: () => H,
            pxToRem: () => N,
            remToPx: () => I,
            resize: () => y,
            sendEvent: () => f,
            setAnimateWindow: () => P,
            setEventHandled: () => G,
            setInputPaddingsRem: () => S,
            setSidePaddingsRem: () => x,
            whenTutorialReady: () => z,
          }));
        const l = i("clientResized"),
          c = { down: i("mousedown"), up: i("mouseup"), move: i("mousemove") };
        const E = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && s(!1);
          }
          function t() {
            u.enabled && s(!0);
          }
          function n() {
            u.enabled
              ? u.listeners < 1
                ? ((u.initialized = !1),
                  document.body.removeEventListener("mouseenter", e),
                  document.body.removeEventListener("mouseleave", t))
                : u.initialized ||
                  ((u.initialized = !0),
                  document.body.addEventListener("mouseenter", e),
                  document.body.addEventListener("mouseleave", t))
              : s(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (e, t) => (
              (e[t] = (function (e) {
                return (t) => {
                  u.listeners += 1;
                  let a = !0;
                  const r = `mouse${e}`,
                    o = c[e]((u) => t([u, "outside"]));
                  function i(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(r, i),
                    n(),
                    () => {
                      a &&
                        (o(), window.removeEventListener(r, i), (u.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(t)),
              e
            ),
            {},
          );
          return Object.assign({}, a, {
            disable() {
              ((u.enabled = !1), n());
            },
            enable() {
              ((u.enabled = !0), n());
            },
            enableOutside() {
              u.enabled && s(!0);
            },
            disableOutside() {
              u.enabled && s(!1);
            },
          });
        })();
        function m(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function A(u = "px") {
          return "rem" === u
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const d = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
        function _(u, e, t = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, t);
        }
        function F(u, e, t) {
          return `url(${_(u, e, t)})`;
        }
        const D = { showing: 0, shown: 1, hiding: 2, hidden: 3 },
          B = {
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
          C = ["args"];
        const g = 2,
          p = 16,
          h = 32,
          b = 64,
          v = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const a = e.args,
                r = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(u);
                  for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                  return a;
                })(e, C);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, r, {
                      arguments:
                        ((n = a),
                        Object.entries(n).map(([u, e]) => {
                          const t = "GFValueProxy";
                          switch (typeof e) {
                            case "number":
                              return { __Type: t, name: u, number: e };
                            case "boolean":
                              return { __Type: t, name: u, bool: e };
                            default:
                              return { __Type: t, name: u, string: e.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, r));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: u });
            var n;
          },
          f = {
            close(u) {
              v("popover" === u ? g : h);
            },
            minimize() {
              v(b);
            },
            move(u) {
              v(p, { isMouseEvent: !0, on: u });
            },
          };
        function w(u) {
          viewEnv.addPreloadTexture(u);
        }
        function S(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function T(u, e, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, n);
        }
        function M(u, e, t) {
          return viewEnv.addDataChangedCallback(u, e, t);
        }
        function x(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function L(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function y(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function R(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: I(e.x), y: I(e.y) };
        }
        function O() {
          viewEnv.freezeTextureBeforeResize();
        }
        function k() {
          return viewEnv.getScale();
        }
        function N(u) {
          return viewEnv.pxToRem(u);
        }
        function I(u) {
          return viewEnv.remToPx(u);
        }
        function P(u, e) {
          viewEnv.setAnimateWindow(u, e);
        }
        function H() {
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
        function j() {
          viewEnv.forceTriggerMouseMove();
        }
        function V() {
          return viewEnv.getShowingStatus();
        }
        const K = Object.keys(D).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === D[e]), u),
            {},
          ),
          $ = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          z = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : B.onDomBuilt(u);
            }),
            engine.whenReady,
          ]),
          X = { view: o, client: a };
      },
      521: (u, e, t) => {
        "use strict";
        let n, a;
        (t.d(e, { n: () => n }),
          (function (u) {
            ((u[(u.NONE = -1)] = "NONE"),
              (u[(u.ALT = 165)] = "ALT"),
              (u[(u.ENTER = 13)] = "ENTER"),
              (u[(u.ESCAPE = 27)] = "ESCAPE"),
              (u[(u.SPACE = 32)] = "SPACE"),
              (u[(u.END = 35)] = "END"),
              (u[(u.HOME = 36)] = "HOME"),
              (u[(u.ARROW_LEFT = 37)] = "ARROW_LEFT"),
              (u[(u.ARROW_UP = 38)] = "ARROW_UP"),
              (u[(u.ARROW_RIGHT = 39)] = "ARROW_RIGHT"),
              (u[(u.ARROW_DOWN = 40)] = "ARROW_DOWN"),
              (u[(u.NUM_PLUS = 107)] = "NUM_PLUS"),
              (u[(u.NUM_MINUS = 109)] = "NUM_MINUS"),
              (u[(u.PLUS = 187)] = "PLUS"),
              (u[(u.MINUS = 189)] = "MINUS"),
              (u[(u.PAGE_UP = 33)] = "PAGE_UP"),
              (u[(u.PAGE_DOWN = 34)] = "PAGE_DOWN"),
              (u[(u.BACKSPACE = 8)] = "BACKSPACE"),
              (u[(u.DELETE = 46)] = "DELETE"),
              (u[(u.TAB = 9)] = "TAB"),
              (u[(u.KEY_N = 78)] = "KEY_N"),
              (u[(u.KEY_0 = 48)] = "KEY_0"),
              (u[(u.KEY_1 = 49)] = "KEY_1"),
              (u[(u.KEY_2 = 50)] = "KEY_2"),
              (u[(u.KEY_3 = 51)] = "KEY_3"),
              (u[(u.KEY_4 = 52)] = "KEY_4"),
              (u[(u.KEY_5 = 53)] = "KEY_5"),
              (u[(u.KEY_6 = 54)] = "KEY_6"),
              (u[(u.KEY_7 = 55)] = "KEY_7"),
              (u[(u.KEY_8 = 56)] = "KEY_8"),
              (u[(u.KEY_9 = 57)] = "KEY_9"),
              (u[(u.CAPS_LOCK = 20)] = "CAPS_LOCK"),
              (u[(u.INSERT = 45)] = "INSERT"),
              (u[(u.F1 = 112)] = "F1"),
              (u[(u.F2 = 113)] = "F2"),
              (u[(u.F3 = 114)] = "F3"),
              (u[(u.F4 = 115)] = "F4"),
              (u[(u.F5 = 116)] = "F5"),
              (u[(u.F6 = 117)] = "F6"),
              (u[(u.F7 = 118)] = "F7"),
              (u[(u.F8 = 119)] = "F8"),
              (u[(u.F9 = 120)] = "F9"),
              (u[(u.F10 = 121)] = "F10"),
              (u[(u.F11 = 122)] = "F11"),
              (u[(u.F12 = 123)] = "F12"),
              (u[(u.SELECT = 93)] = "SELECT"),
              (u[(u.NUMPAD_0 = 96)] = "NUMPAD_0"),
              (u[(u.NUMPAD_1 = 97)] = "NUMPAD_1"),
              (u[(u.NUMPAD_2 = 98)] = "NUMPAD_2"),
              (u[(u.NUMPAD_3 = 99)] = "NUMPAD_3"),
              (u[(u.NUMPAD_4 = 100)] = "NUMPAD_4"),
              (u[(u.NUMPAD_5 = 101)] = "NUMPAD_5"),
              (u[(u.NUMPAD_6 = 102)] = "NUMPAD_6"),
              (u[(u.NUMPAD_7 = 103)] = "NUMPAD_7"),
              (u[(u.NUMPAD_8 = 104)] = "NUMPAD_8"),
              (u[(u.NUMPAD_9 = 105)] = "NUMPAD_9"),
              (u[(u.NUM_DECIMAL = 110)] = "NUM_DECIMAL"),
              (u[(u.STAR = 106)] = "STAR"),
              (u[(u.NUM_SLASH = 111)] = "NUM_SLASH"),
              (u[(u.FORWARD_SLASH = 191)] = "FORWARD_SLASH"),
              (u[(u.COMMA = 188)] = "COMMA"),
              (u[(u.DASH = 189)] = "DASH"),
              (u[(u.PERIOD = 190)] = "PERIOD"));
          })(n || (n = {})),
          (function (u) {
            ((u.ALT = "Alt"),
              (u.ALT_GRAPH = "AltGraph"),
              (u.CAPS_LOCK = "CapsLock"),
              (u.CONTROL = "Control"),
              (u.FN = "Fn"),
              (u.FN_LOCK = "FnLock"),
              (u.META = "Meta"),
              (u.NUM_LOCK = "NumLock"),
              (u.SCROLL_LOCK = "ScrollLock"),
              (u.SHIFT = "Shift"),
              (u.SYMBOL = "Symbol"),
              (u.SYMBOL_LOCK = "SymbolLock"));
          })(a || (a = {})));
      },
      358: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        var n = t(67);
        class a {
          constructor() {
            ((this._callbacks = void 0),
              (this._updateHandler = void 0),
              (this._views = void 0),
              (this.clearViewCallbacks = (u) => {
                this._views[u] &&
                  (this._views[u].forEach((u) => {
                    delete this._callbacks[u];
                  }),
                  delete this._views[u]);
              }),
              (this._callbacks = {}),
              (this._views = {}),
              (this._updateHandler = void 0));
          }
          static get instance() {
            return (window.__dataTracker || (window.__dataTracker = new a()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(u, e, t = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = n.O.view.addModelObserver(u, t, a);
            return (
              r > 0
                ? ((this._callbacks[r] = e),
                  t > 0 && (this._views[t] ? this._views[t].push(r) : (this._views[t] = [r])))
                : console.error("Can't add callback for model:", u),
              r
            );
          }
          removeCallback(u, e = 0) {
            let t = !1;
            return (
              void 0 !== u &&
                void 0 !== this._callbacks[u] &&
                ((t = viewEnv.removeDataChangedCallback(u, e)), delete this._callbacks[u]),
              t || console.error("Can't remove callback by id:", u),
              t
            );
          }
          _emmitDataChanged(u, e, t) {
            t.forEach((t) => {
              const n = this._callbacks[t];
              void 0 !== n && n(u, e);
            });
          }
        }
        a.__instance = void 0;
        const r = a;
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
                  this.callbacks.forEach((u) => {
                    u(this.data);
                  }));
              }),
              (this.dataTracker = new _DataTracker__WEBPACK_IMPORTED_MODULE_0__.Z()),
              (this.modelPath = path),
              (this.callbacks = new Set()),
              (0, _index__WEBPACK_IMPORTED_MODULE_1__.ry)().then(() => {
                (this._addCallback(path),
                  watchingFields.forEach((u) => {
                    this._addCallback(path + "." + u);
                  }),
                  this._notifyObservers());
              }));
          }
          subscribe(u) {
            (this.callbacks.add(u), null !== this.data && void 0 !== this.data && u(this.data));
          }
          unsubscribe(u) {
            this.callbacks.delete(u);
          }
          destroy() {
            (this.dataTracker.clear(), this.callbacks.clear());
          }
          _addCallback(u) {
            this.dataTracker.addCallback(u, this._notifyObservers);
          }
        }
        const __WEBPACK_DEFAULT_EXPORT__ = ViewModel;
      },
      364: (u, e, t) => {
        "use strict";
        t.d(e, { Sw: () => r.Z, B0: () => s, ry: () => B });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (u) => {
                this.entries.forEach(({ container: e, callback: t }) => {
                  let n = u.target;
                  do {
                    if (n === e) return;
                    n = n.parentNode;
                  } while (n);
                  t();
                });
              }));
          }
          static get instance() {
            return (n.__instance || (n.__instance = new n()), n.__instance);
          }
          register(u, e) {
            (this.addMouseListener(), this.entries.push({ container: u, callback: e }));
          }
          unregister(u, e) {
            const t = u,
              n = e;
            ((this.entries = this.entries.filter(
              ({ container: u, callback: e }) => u !== t || e !== n,
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
        const a = n;
        var r = t(358);
        const o = {
            getNumberFormat: (u, e) => systemLocale.getNumberFormat(u, e),
            getRealFormat: (u, e) => systemLocale.getRealFormat(u, e),
            getTimeFormat: (u, e) => systemLocale.getTimeFormat(u, e),
            getDateFormat: (u, e) => systemLocale.getDateFormat(u, e),
            toUpperCase: (u) => systemLocale.toUpperCase(u),
            toLowerCase: (u) => systemLocale.toUpperCase(u),
          },
          i = {
            getNumberFormat: (u) => userLocale.getNumberFormat(u),
            getTimeFormat: (u, e, t) => userLocale.getTimeFormat(u, e, void 0 === t || t),
            getTimeString: (u, e, t) => userLocale.getTimeString(u, e, void 0 === t || t),
          };
        let s;
        !(function (u) {
          ((u[(u.UNDEFINED = 0)] = "UNDEFINED"),
            (u[(u.TOOLTIP = 1)] = "TOOLTIP"),
            (u[(u.POP_OVER = 2)] = "POP_OVER"),
            (u[(u.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (u[(u.DROP_DOWN = 8)] = "DROP_DOWN"),
            (u[(u.MOVE = 16)] = "MOVE"),
            (u[(u.CLOSE = 32)] = "CLOSE"),
            (u[(u.MINIMIZE = 64)] = "MINIMIZE"));
        })(s || (s = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var A = t(521),
          d = t(67);
        const _ = ["args"];
        function F(u, e, t, n, a, r, o) {
          try {
            var i = u[r](o),
              s = i.value;
          } catch (u) {
            return void t(u);
          }
          i.done ? e(s) : Promise.resolve(s).then(n, a);
        }
        const D = (u) => ({
            __Type: "GFBoundingBox",
            x: u.x,
            y: u.y,
            width: u.width,
            height: u.height,
          }),
          B = (function () {
            var u,
              e =
                ((u = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((u) => {
                      engine.on("Ready", u);
                    })
                  );
                }),
                function () {
                  var e = this,
                    t = arguments;
                  return new Promise(function (n, a) {
                    var r = u.apply(e, t);
                    function o(u) {
                      F(r, n, a, o, i, "next", u);
                    }
                    function i(u) {
                      F(r, n, a, o, i, "throw", u);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          C = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const a = e.args,
                r = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(u);
                  for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                  return a;
                })(e, _);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, r, {
                      arguments:
                        ((n = a),
                        Object.entries(n).map(([u, e]) => {
                          const t = { __Type: "GFValueProxy", name: u };
                          switch (typeof e) {
                            case "number":
                              t.number = e;
                              break;
                            case "boolean":
                              t.bool = e;
                              break;
                            default:
                              t.string = e.toString();
                          }
                          return t;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, r));
            } else viewEnv.handleViewEvent({ __Type: t, type: u });
            var n;
          },
          g = () => C(s.CLOSE),
          p = (u, e) => {
            u.keyCode === A.n.ESCAPE && e();
          };
        var h = t(572);
        const b = a.instance,
          v = {
            DataTracker: r.Z,
            ViewModel: h.Z,
            ViewEventType: s,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: m,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (u) => C(s.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: g,
            sendClosePopOverEvent: () => C(s.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (u, e, t = 0) => {
              C(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, n, a = R.invalid("resId"), r) => {
              const o = d.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                E = i.width,
                m = i.height,
                A = {
                  x: d.O.view.pxToRem(l) + o.x,
                  y: d.O.view.pxToRem(c) + o.y,
                  width: d.O.view.pxToRem(E),
                  height: d.O.view.pxToRem(m),
                };
              C(s.POP_OVER, {
                isMouseEvent: !0,
                contentID: u,
                decoratorID: n || R.invalid("resId"),
                targetID: a,
                direction: e,
                bbox: D(A),
                on: !0,
                args: r,
              });
            },
            addEscapeListener: (u) => {
              const e = (e) => p(e, u);
              return (
                window.addEventListener("keydown", e),
                () => window.removeEventListener("keydown", e)
              );
            },
            closeOnEsc: (u) => {
              p(u, g);
            },
            handleViewEvent: C,
            onBindingsReady: B,
            onLayoutReady: () =>
              new Promise((u) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    u();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
            dumpViewModel: function u(e) {
              const t = {};
              if ("object" != typeof e) return e;
              for (const n in e)
                if (Object.prototype.hasOwnProperty.call(e, n)) {
                  const a = Object.prototype.toString.call(e[n]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = e[n];
                    t[n] = [];
                    for (let e = 0; e < a.length; e++) t[n].push({ value: u(a[e].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = u(e[n]))
                      : (t[n] = e[n]);
                }
              return t;
            },
            ClickOutsideManager: b,
            SystemLocale: o,
            UserLocale: i,
          };
        window.ViewEnvHelper = v;
      },
      343: (u, e, t) => {
        "use strict";
        var n = t(179),
          a = t.n(n);
        const r = (u, e, t) =>
          e.extraLargeHeight ||
          e.largeHeight ||
          e.mediumHeight ||
          e.smallHeight ||
          e.extraSmallHeight
            ? (e.extraLargeHeight && t.extraLarge) ||
              (e.largeHeight && t.large) ||
              (e.mediumHeight && t.medium) ||
              (e.smallHeight && t.small) ||
              (e.extraSmallHeight && t.extraSmall)
              ? u
              : null
            : u;
        var o = t(67);
        const i = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var s;
        function l(u, e, t) {
          const n = (function (u, e) {
              switch (!0) {
                case u >= e.extraLarge.width:
                  return e.extraLarge.weight;
                case u >= e.large.width && u < e.extraLarge.width:
                  return e.large.weight;
                case u >= e.medium.width && u < e.large.width:
                  return e.medium.weight;
                case u >= e.small.width && u < e.medium.width:
                  return e.small.weight;
                default:
                  return e.extraSmall.weight;
              }
            })(u, t),
            a = (function (u, e) {
              switch (!0) {
                case u >= e.extraLarge.height:
                  return e.extraLarge.weight;
                case u >= e.large.height && u < e.extraLarge.height:
                  return e.large.weight;
                case u >= e.medium.height && u < e.large.height:
                  return e.medium.weight;
                case u >= e.small.height && u < e.medium.height:
                  return e.small.weight;
                default:
                  return e.extraSmall.weight;
              }
            })(e, t),
            r = Math.min(n, a);
          return {
            extraLarge: r === t.extraLarge.weight,
            large: r === t.large.weight,
            medium: r === t.medium.weight,
            small: r === t.small.weight,
            extraSmall: r === t.extraSmall.weight,
            extraLargeWidth: n === t.extraLarge.weight,
            largeWidth: n === t.large.weight,
            mediumWidth: n === t.medium.weight,
            smallWidth: n === t.small.weight,
            extraSmallWidth: n === t.extraSmall.weight,
            extraLargeHeight: a === t.extraLarge.weight,
            largeHeight: a === t.large.weight,
            mediumHeight: a === t.medium.weight,
            smallHeight: a === t.small.weight,
            extraSmallHeight: a === t.extraSmall.weight,
          };
        }
        !(function (u) {
          ((u.extraLarge = "extraLarge"),
            (u.large = "large"),
            (u.medium = "medium"),
            (u.small = "small"),
            (u.extraSmall = "extraSmall"),
            (u.extraLargeWidth = "extraLargeWidth"),
            (u.largeWidth = "largeWidth"),
            (u.mediumWidth = "mediumWidth"),
            (u.smallWidth = "smallWidth"),
            (u.extraSmallWidth = "extraSmallWidth"),
            (u.extraLargeHeight = "extraLargeHeight"),
            (u.largeHeight = "largeHeight"),
            (u.mediumHeight = "mediumHeight"),
            (u.smallHeight = "smallHeight"),
            (u.extraSmallHeight = "extraSmallHeight"));
        })(s || (s = {}));
        const c = o.O.client.getSize("rem"),
          E = c.width,
          m = c.height,
          A = Object.assign({ width: E, height: m }, l(E, m, i)),
          d = (0, n.createContext)(A),
          _ = ["children"];
        const F = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                a = {},
                r = Object.keys(u);
              for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
              return a;
            })(u, _);
          const a = (0, n.useContext)(d),
            o = a.extraLarge,
            i = a.large,
            s = a.medium,
            l = a.small,
            c = a.extraSmall,
            E = a.extraLargeWidth,
            m = a.largeWidth,
            A = a.mediumWidth,
            F = a.smallWidth,
            D = a.extraSmallWidth,
            B = a.extraLargeHeight,
            C = a.largeHeight,
            g = a.mediumHeight,
            p = a.smallHeight,
            h = a.extraSmallHeight,
            b = { extraLarge: B, large: C, medium: g, small: p, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && o) return e;
            if (t.large && i) return e;
            if (t.medium && s) return e;
            if (t.small && l) return e;
            if (t.extraSmall && c) return e;
          } else {
            if (t.extraLargeWidth && E) return r(e, t, b);
            if (t.largeWidth && m) return r(e, t, b);
            if (t.mediumWidth && A) return r(e, t, b);
            if (t.smallWidth && F) return r(e, t, b);
            if (t.extraSmallWidth && D) return r(e, t, b);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && B) return e;
              if (t.largeHeight && C) return e;
              if (t.mediumHeight && g) return e;
              if (t.smallHeight && p) return e;
              if (t.extraSmallHeight && h) return e;
            }
          }
          return null;
        };
        F.defaultProps = {
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
        (0, n.memo)(F);
        const D = (u) => {
            const e = (0, n.useRef)(!1);
            e.current || (u(), (e.current = !0));
          },
          B = (0, n.memo)(({ children: u }) => {
            const e = (0, n.useContext)(d),
              t = (0, n.useState)(e),
              r = t[0],
              s = t[1],
              c = (0, n.useCallback)((u, e) => {
                const t = o.O.view.pxToRem(u),
                  n = o.O.view.pxToRem(e);
                s(Object.assign({ width: t, height: n }, l(t, n, i)));
              }, []);
            (D(() => {
              engine.on("clientResized", c);
            }),
              (0, n.useEffect)(() => () => engine.off("clientResized", c), [c]));
            const E = (0, n.useMemo)(() => Object.assign({}, r), [r]);
            return a().createElement(d.Provider, { value: E }, u);
          });
        var C = t(483),
          g = t.n(C),
          p = t(926),
          h = t.n(p);
        let b, v, f;
        (!(function (u) {
          ((u[(u.ExtraSmall = i.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = i.small.width)] = "Small"),
            (u[(u.Medium = i.medium.width)] = "Medium"),
            (u[(u.Large = i.large.width)] = "Large"),
            (u[(u.ExtraLarge = i.extraLarge.width)] = "ExtraLarge"));
        })(b || (b = {})),
          (function (u) {
            ((u[(u.ExtraSmall = i.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = i.small.width)] = "Small"),
              (u[(u.Medium = i.medium.width)] = "Medium"),
              (u[(u.Large = i.large.width)] = "Large"),
              (u[(u.ExtraLarge = i.extraLarge.width)] = "ExtraLarge"));
          })(v || (v = {})),
          (function (u) {
            ((u[(u.ExtraSmall = i.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = i.small.height)] = "Small"),
              (u[(u.Medium = i.medium.height)] = "Medium"),
              (u[(u.Large = i.large.height)] = "Large"),
              (u[(u.ExtraLarge = i.extraLarge.height)] = "ExtraLarge"));
          })(f || (f = {})));
        const w = () => {
            const u = (0, n.useContext)(d),
              e = u.width,
              t = u.height,
              a = ((u) => {
                switch (!0) {
                  case u.extraLarge:
                    return b.ExtraLarge;
                  case u.large:
                    return b.Large;
                  case u.medium:
                    return b.Medium;
                  case u.small:
                    return b.Small;
                  case u.extraSmall:
                    return b.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), b.ExtraSmall);
                }
              })(u),
              r = ((u) => {
                switch (!0) {
                  case u.extraLargeWidth:
                    return v.ExtraLarge;
                  case u.largeWidth:
                    return v.Large;
                  case u.mediumWidth:
                    return v.Medium;
                  case u.smallWidth:
                    return v.Small;
                  case u.extraSmallWidth:
                    return v.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), v.ExtraSmall);
                }
              })(u),
              o = ((u) => {
                switch (!0) {
                  case u.extraLargeHeight:
                    return f.ExtraLarge;
                  case u.largeHeight:
                    return f.Large;
                  case u.mediumHeight:
                    return f.Medium;
                  case u.smallHeight:
                    return f.Small;
                  case u.extraSmallHeight:
                    return f.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), f.ExtraSmall);
                }
              })(u);
            return {
              mediaSize: a,
              mediaWidth: r,
              mediaHeight: o,
              remScreenWidth: e,
              remScreenHeight: t,
            };
          },
          S = ["children", "className"];
        function T() {
          return (
            (T =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            T.apply(this, arguments)
          );
        }
        const M = {
            [v.ExtraSmall]: "",
            [v.Small]: h().SMALL_WIDTH,
            [v.Medium]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH}`,
            [v.Large]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH}`,
            [v.ExtraLarge]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH} ${h().EXTRA_LARGE_WIDTH}`,
          },
          x = {
            [f.ExtraSmall]: "",
            [f.Small]: h().SMALL_HEIGHT,
            [f.Medium]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT}`,
            [f.Large]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT}`,
            [f.ExtraLarge]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT} ${h().EXTRA_LARGE_HEIGHT}`,
          },
          L = {
            [b.ExtraSmall]: "",
            [b.Small]: h().SMALL,
            [b.Medium]: `${h().SMALL} ${h().MEDIUM}`,
            [b.Large]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE}`,
            [b.ExtraLarge]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE} ${h().EXTRA_LARGE}`,
          },
          y = (u) => {
            let e = u.children,
              t = u.className,
              n = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, S);
            const r = w(),
              o = r.mediaWidth,
              i = r.mediaHeight,
              s = r.mediaSize;
            return a().createElement("div", T({ className: g()(t, M[o], x[i], L[s]) }, n), e);
          },
          O = ["children"];
        const k = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                a = {},
                r = Object.keys(u);
              for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
              return a;
            })(u, O);
          return a().createElement(B, null, a().createElement(y, t, e));
        };
        var N = t(493),
          I = t.n(N);
        const P = (u, e, t) => (t < u ? u : t > e ? e : t),
          H = (u) => {
            let e,
              t = null;
            return (
              (t = requestAnimationFrame(() => {
                t = requestAnimationFrame(() => {
                  ((t = null), (e = u()));
                });
              })),
              () => {
                ("function" == typeof e && e(), null !== t && cancelAnimationFrame(t));
              }
            );
          };
        function W(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return G(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return G(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            t && (u = t);
            var n = 0;
            return function () {
              return n >= u.length ? { done: !0 } : { done: !1, value: u[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function G(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, n = new Array(e); t < e; t++) n[t] = u[t];
          return n;
        }
        const U = [];
        function j(u) {
          const e = (0, n.useRef)(u);
          return (
            (0, n.useLayoutEffect)(() => {
              e.current = u;
            }),
            (0, n.useCallback)((...u) => (0, e.current)(...u), U)
          );
        }
        function V(u, e, t) {
          const a = (0, n.useMemo)(
            () =>
              (function (u, e, t, n) {
                let a,
                  r = !1,
                  o = 0;
                function i() {
                  a && clearTimeout(a);
                }
                function s(...s) {
                  const l = this,
                    c = Date.now() - o;
                  function E() {
                    ((o = Date.now()), t.apply(l, s));
                  }
                  r ||
                    (n && !a && E(),
                    i(),
                    void 0 === n && c > u
                      ? E()
                      : !0 !== e &&
                        (a = setTimeout(
                          n
                            ? function () {
                                a = void 0;
                              }
                            : E,
                          void 0 === n ? u - c : u,
                        )));
                }
                return (
                  "boolean" != typeof e && ((n = t), (t = e), (e = void 0)),
                  (s.cancel = function () {
                    (i(), (r = !0));
                  }),
                  s
                );
              })(t, u),
            e,
          );
          return ((0, n.useEffect)(() => a.cancel, [a]), a);
        }
        var K = t(30);
        let $;
        !(function (u) {
          ((u[(u.Next = -1)] = "Next"), (u[(u.Prev = 1)] = "Prev"));
        })($ || ($ = {}));
        const z = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          X = (({
            getContainerSize: u,
            getBounds: e,
            setScrollPosition: t,
            getDirection: a,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: i = !1,
          }) => {
            const s = (u, t) => {
              const n = e(u),
                a = n[0],
                r = n[1];
              return P(a, r, t);
            };
            return (l = {}) => {
              const c = l.settings,
                E = void 0 === c ? z : c,
                m = (0, n.useRef)(null),
                A = (0, n.useRef)(null),
                d = (() => {
                  const u = (0, n.useMemo)(() => ({}), []),
                    e = (e) => (u[e] || (u[e] = new Map()), u[e]),
                    t = (u, t) => {
                      e(u).set(t, t);
                    },
                    a = (u, t) => {
                      e(u).delete(t);
                    },
                    r = (u, ...t) => {
                      for (var n, a = W(e(u).values()); !(n = a()).done;) (0, n.value)(...t);
                    };
                  return (0, n.useMemo)(() => ({ on: t, off: a, trigger: r }), []);
                })(),
                _ = V(
                  () => {
                    o.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                F = (0, K.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (u) => {
                    const e = m.current;
                    e && (t(e, u), d.trigger("change", u), i && _());
                  },
                  onRest: (u) => d.trigger("rest", u),
                  onStart: (u) => d.trigger("start", u),
                  onPause: (u) => d.trigger("pause", u),
                })),
                D = F[0],
                B = F[1],
                C = (0, n.useCallback)(
                  (u, e, t) => {
                    var n;
                    const a = D.scrollPosition.get(),
                      r = (null != (n = D.scrollPosition.goal) ? n : 0) - a;
                    return s(u, e * t + r + a);
                  },
                  [D.scrollPosition],
                ),
                g = (0, n.useCallback)(
                  (u, { immediate: e = !1, reset: t = !0 } = {}) => {
                    const n = m.current;
                    n &&
                      B.start({
                        scrollPosition: s(n, u),
                        immediate: e,
                        reset: t,
                        config: E.animationConfig,
                        from: { scrollPosition: s(n, D.scrollPosition.get()) },
                      });
                  },
                  [B, E.animationConfig, D.scrollPosition],
                ),
                p = (0, n.useCallback)(
                  (u) => {
                    const e = m.current,
                      t = A.current;
                    if (!e || !t) return;
                    const n = ((u, e) => {
                        switch (e.type) {
                          case "proportional":
                            return r(u) / e.factor;
                          case "fixed":
                            return e.value;
                        }
                      })(t, E.step),
                      a = C(e, u, n);
                    g(a);
                  },
                  [g, C, E.step],
                ),
                h = (0, n.useCallback)(
                  (u) => {
                    (0 !== u.deltaY && p(a(u)),
                      m.current && d.trigger("mouseWheel", u, D.scrollPosition, e(m.current)));
                  },
                  [D.scrollPosition, p, d],
                ),
                b = ((u, e = []) => {
                  const t = (0, n.useRef)(),
                    a = (0, n.useCallback)((...e) => {
                      (t.current && t.current(), (t.current = u(...e)));
                    }, e);
                  return (
                    (0, n.useEffect)(
                      () => () => {
                        t.current && t.current();
                      },
                      [a],
                    ),
                    a
                  );
                })(
                  () =>
                    H(() => {
                      const u = m.current;
                      u &&
                        (g(s(u, D.scrollPosition.goal), { immediate: !0 }),
                        d.trigger("resizeHandled"));
                    }),
                  [g, D.scrollPosition.goal],
                ),
                v = j(() => {
                  const u = m.current;
                  if (!u) return;
                  const e = s(u, D.scrollPosition.goal);
                  (e !== D.scrollPosition.goal && g(e, { immediate: !0 }),
                    d.trigger("recalculateContent"));
                });
              (0, n.useEffect)(
                () => (
                  window.addEventListener("resize", b),
                  () => {
                    window.removeEventListener("resize", b);
                  }
                ),
                [b],
              );
              const f = (0, n.useCallback)((u) => d.trigger("isThumbDraggingChanged", u), [d]);
              return (0, n.useMemo)(
                () => ({
                  getWrapperSize: () => (A.current ? r(A.current) : void 0),
                  getContainerSize: () => (m.current ? u(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? e(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: E.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: h,
                  applyScroll: g,
                  applyStepTo: p,
                  contentRef: m,
                  wrapperRef: A,
                  scrollPosition: B,
                  animationScroll: D,
                  recalculateContent: v,
                  handleIsThumbDragging: f,
                  events: { on: d.on, off: d.off },
                }),
                [D.scrollPosition, g, p, f, d.off, d.on, v, h, B, E.step.clampedArrowStepTimeout],
              );
            };
          })({
            getBounds: (u) => [0, u.scrollHeight - u.offsetHeight],
            getContainerSize: (u) => u.scrollHeight,
            getWrapperSize: (u) => u.offsetHeight,
            setScrollPosition: (u, e) => {
              u.scrollTop = e.value.scrollPosition;
            },
            getDirection: (u) => (u.deltaY > 1 ? $.Next : $.Prev),
          });
        function Y(u) {
          engine.call("PlaySound", u);
        }
        const q = "VerticalBar_base_f3",
          Z = "VerticalBar_base__nonActive_42",
          Q = "VerticalBar_topButton_d7",
          J = "VerticalBar_bottomButton_06",
          uu = "VerticalBar_track_df",
          eu = "VerticalBar_thumb_32",
          tu = "VerticalBar_rail_43",
          nu = "disable",
          au = () => {},
          ru = { pending: !1, offset: 0 },
          ou = (u) => {
            var e;
            return 0.9 * (null != (e = u.getWrapperSize()) ? e : 0);
          },
          iu = (u, e) => {
            u.contentRef.current && e(u.contentRef.current);
          },
          su = (u, e) => Math.max(20, u.offsetHeight * e),
          lu = (0, n.memo)(
            ({ api: u, classNames: e = {}, getStepByRailClick: t = ou, onDrag: r = au }) => {
              const o = (0, n.useRef)(null),
                i = (0, n.useRef)(null),
                s = (0, n.useRef)(null),
                l = (0, n.useRef)(null),
                c = (0, n.useRef)(null),
                E = u.stepTimeout || 100,
                m = (0, n.useState)(ru),
                A = m[0],
                d = m[1],
                _ = (0, n.useCallback)(
                  (u) => {
                    (d(u),
                      c.current &&
                        r({ type: u.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                F = j(() => {
                  const e = c.current,
                    t = l.current,
                    n = u.getWrapperSize(),
                    a = u.getContainerSize();
                  if (!(n && a && e && t)) return;
                  const r = Math.min(1, n / a);
                  return (
                    (e.style.height = `${su(t, r)}px`),
                    e.classList.add(eu),
                    o.current &&
                      (1 === r ? o.current.classList.add(Z) : o.current.classList.remove(Z)),
                    r
                  );
                }),
                D = j(() => {
                  const e = l.current,
                    t = c.current,
                    n = u.getWrapperSize(),
                    a = u.getContainerSize();
                  if (!(n && e && t && a)) return;
                  const r = u.animationScroll.scrollPosition.get(),
                    o = Math.min(1, n / a),
                    E = P(0, 1, r / (a - n)),
                    m = (e.offsetHeight - su(e, o)) * E;
                  ((t.style.transform = `translateY(${0 | m}px)`),
                    ((u) => {
                      if (i.current && s.current && l.current && c.current) {
                        if (0 === u)
                          return (i.current.classList.add(nu), void s.current.classList.remove(nu));
                        if (
                          ((e = l.current),
                          (t = c.current),
                          u - (e.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(nu), void s.current.classList.add(nu));
                        var e, t;
                        (i.current.classList.remove(nu), s.current.classList.remove(nu));
                      }
                    })(m));
                }),
                B = j(() => {
                  iu(u, () => {
                    (F(), D());
                  });
                });
              ((0, n.useEffect)(() => H(B)),
                (0, n.useEffect)(() => {
                  const e = () => {
                    iu(u, () => {
                      D();
                    });
                  };
                  let t = au;
                  const n = () => {
                    (t(), (t = H(B)));
                  };
                  return (
                    u.events.on("recalculateContent", B),
                    u.events.on("rest", e),
                    u.events.on("change", e),
                    u.events.on("resizeHandled", n),
                    () => {
                      (t(),
                        u.events.off("recalculateContent", B),
                        u.events.off("rest", e),
                        u.events.off("change", e),
                        u.events.off("resizeHandled", n));
                    }
                  );
                }, [u]),
                (0, n.useEffect)(() => {
                  if (!A.pending) return;
                  const e = (e) => {
                      iu(u, (t) => {
                        const n = l.current,
                          a = c.current,
                          o = u.getContainerSize();
                        if (!n || !a || !o) return;
                        const i = e.screenY - A.offset - n.getBoundingClientRect().y,
                          s = (i / n.offsetHeight) * o;
                        (u.scrollPosition.start({
                          scrollPosition: u.clampPosition(t, s),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          r({ type: "dragging", thumb: a, thumbOffset: i, contentOffset: s }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", e),
                        u.handleIsThumbDragging(!1),
                        _(ru));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [u, A.offset, A.pending, r, _]));
              const C = (function (u, e, t = []) {
                  const a = (0, n.useRef)(0),
                    r = (0, n.useCallback)(() => window.clearInterval(a.current), t || []);
                  (0, n.useEffect)(() => r, [r]);
                  const o = (null != t ? t : []).concat([e]);
                  return [
                    (0, n.useCallback)((t) => {
                      ((a.current = window.setInterval(() => u(t, !0), e)), u(t, !1));
                    }, o),
                    r,
                  ];
                })((e) => u.applyStepTo(e), E, [u]),
                p = C[0],
                h = C[1];
              (0, n.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const b = (u) => {
                u.target.classList.contains(nu) || Y("highlight");
              };
              return a().createElement(
                "div",
                { className: g()(q, e.base), ref: o, onWheel: u.handleMouseWheel },
                a().createElement("div", {
                  className: g()(Q, e.topButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(nu) || 0 !== u.button || (Y("play"), p($.Next));
                  },
                  ref: i,
                  onMouseEnter: b,
                }),
                a().createElement(
                  "div",
                  {
                    className: g()(uu, e.track),
                    onMouseDown: (e) => {
                      const n = c.current;
                      if (n && 0 === e.button)
                        if ((Y("play"), e.target === n))
                          (u.handleIsThumbDragging(!0),
                            _({ pending: !0, offset: e.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((e) => {
                            c.current &&
                              iu(u, (n) => {
                                if (!n) return;
                                const a = t(u),
                                  r = u.clampPosition(n, n.scrollTop + a * e);
                                u.applyScroll(r);
                              });
                          })(e.screenY > n.getBoundingClientRect().y ? $.Prev : $.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: b,
                  },
                  a().createElement("div", { ref: c, className: e.thumb }),
                  a().createElement("div", { className: g()(tu, e.rail) }),
                ),
                a().createElement("div", {
                  className: g()(J, e.bottomButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(nu) || 0 !== u.button || (Y("play"), p($.Prev));
                  },
                  onMouseUp: h,
                  ref: s,
                  onMouseEnter: b,
                }),
              );
            },
          ),
          cu = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Eu = ({
            children: u,
            api: e,
            className: t,
            barClassNames: r,
            areaClassName: o,
            scrollClassName: i,
            scrollClassNames: s,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const E = (0, n.useMemo)(() => {
                const u = r || {};
                return Object.assign({}, u, { base: g()(cu.base, u.base) });
              }, [r]),
              m = (0, n.useMemo)(() => Object.assign({}, e, { handleMouseWheel: () => {} }), [e]);
            return a().createElement(
              "div",
              { className: g()(cu.defaultScroll, t), onWheel: e.handleMouseWheel },
              a().createElement(
                "div",
                { className: g()(cu.area, o) },
                a().createElement(mu, { className: i, classNames: s, api: m }, u),
              ),
              a().createElement(lu, { getStepByRailClick: l, api: e, onDrag: c, classNames: E }),
            );
          },
          mu = ({ className: u, classNames: e, children: t, api: r }) => (
            (0, n.useEffect)(() => H(r.recalculateContent)),
            a().createElement(
              "div",
              { className: g()(cu.base, u), ref: r.wrapperRef, onWheel: r.handleMouseWheel },
              a().createElement(
                "div",
                { className: g()(cu.content, null == e ? void 0 : e.content), ref: r.contentRef },
                t,
              ),
            )
          );
        mu.Default = Eu;
        const Au = {
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
          du = [
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
        function _u() {
          return (
            (_u =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            _u.apply(this, arguments)
          );
        }
        class Fu extends a().PureComponent {
          constructor(...u) {
            (super(...u),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (u) => (e) => {
                (u && u(e),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && Y(this.props.soundHover));
              }),
              (this._onMouseLeave = (u) => (e) => {
                (u && u(e), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (u) => (e) => {
                (u && u(e),
                  this.setState({ click: !0 }),
                  this.props.soundClick && Y(this.props.soundClick));
              }),
              (this._onMouseUp = (u) => (e) => {
                (u && u(e), this.setState({ click: !1 }));
              }),
              (this.handleFocus = () => this.setState({ focus: !0 })),
              (this.handleBlur = () => this.setState({ focus: !1 })));
          }
          render() {
            const u = this.props,
              e = u.caption,
              t = u.onClick,
              n = u.goto,
              r = u.side,
              o = u.type,
              i = u.classNames,
              s = u.onMouseEnter,
              l = u.onMouseLeave,
              c = u.onMouseDown,
              E = u.onMouseUp,
              m =
                (u.soundClick,
                u.soundHover,
                (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(u);
                  for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                  return a;
                })(u, du)),
              A = g()(Au.base, Au[`base__${o}`], Au[`base__${r}`], null == i ? void 0 : i.base),
              d = g()(Au.icon, Au[`icon__${o}`], Au[`icon__${r}`], null == i ? void 0 : i.icon),
              _ = g()(Au.glow, null == i ? void 0 : i.glow),
              F = g()(Au.caption, Au[`caption__${o}`], null == i ? void 0 : i.caption),
              D = g()(Au.goto, null == i ? void 0 : i.goto);
            return a().createElement(
              "div",
              _u(
                {
                  className: A,
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
              "info" !== o && a().createElement("div", { className: Au.shine }),
              a().createElement(
                "div",
                { className: d },
                a().createElement("div", { className: _ }),
              ),
              a().createElement("div", { className: F }, e),
              n && a().createElement("div", { className: D }, n),
            );
          }
        }
        Fu.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var Du = t(364);
        const Bu = [
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
        function Cu(u) {
          return Object.entries(u || {}).map(([u, e]) => {
            const t = { __Type: "GFValueProxy", name: u };
            switch (typeof e) {
              case "number":
                t.number = e;
                break;
              case "boolean":
                t.bool = e;
                break;
              case "undefined":
                break;
              default:
                t.string = e.toString();
            }
            return t;
          });
        }
        const gu = (u, e, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: Du.B0.TOOLTIP,
                  contentID: u,
                  decoratorID: e,
                  targetID: n,
                },
                t,
              ),
            );
          },
          pu = (u) => {
            let e = u.children,
              t = u.contentId,
              a = u.args,
              r = u.onMouseEnter,
              o = u.onMouseLeave,
              i = u.onMouseDown,
              s = u.onClick,
              l = u.ignoreShowDelay,
              c = void 0 !== l && l,
              E = u.ignoreMouseClick,
              m = void 0 !== E && E,
              A = u.decoratorId,
              d = void 0 === A ? 0 : A,
              _ = u.isEnabled,
              F = void 0 === _ || _,
              D = u.targetId,
              B = void 0 === D ? 0 : D,
              C = u.onShow,
              g = u.onHide,
              p = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, Bu);
            const h = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              b = (0, n.useMemo)(
                () =>
                  B ||
                  ((u = 1) => {
                    const e = new Error().stack;
                    let t,
                      n = R.invalid("resId");
                    return (
                      e &&
                        ((t = e.split("\n")[u].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== t &&
                          window.subViews[t] &&
                          (n = window.subViews[t].id)),
                      { caller: t, stack: e, resId: n }
                    );
                  })().resId,
                [B],
              ),
              v = (0, n.useCallback)(() => {
                (h.current.isVisible && h.current.timeoutId) ||
                  (gu(t, d, { isMouseEvent: !0, on: !0, arguments: Cu(a) }, b),
                  C && C(),
                  (h.current.isVisible = !0));
              }, [t, d, a, b, C]),
              f = (0, n.useCallback)(() => {
                if (h.current.isVisible || h.current.timeoutId) {
                  const u = h.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (h.current.timeoutId = 0)),
                    gu(t, d, { on: !1 }, b),
                    h.current.isVisible && g && g(),
                    (h.current.isVisible = !1));
                }
              }, [t, d, b, g]),
              w = (0, n.useCallback)((u) => {
                h.current.isVisible &&
                  ((h.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (h.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(h.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const u = h.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    u && window.clearTimeout(u));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === F && f();
              }, [F, f]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", f),
                  () => {
                    (window.removeEventListener("mouseleave", f), f());
                  }
                ),
                [f],
              ));
            return F
              ? (0, n.cloneElement)(
                  e,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((h.current.timeoutId = window.setTimeout(v, c ? 100 : 400)),
                            r && r(u),
                            S && S(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (f(), null == o || o(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === m && f(), null == s || s(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === m && f(), null == i || i(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    p,
                  ),
                )
              : e;
            var S;
          };
        var hu = t(521);
        const bu = (u) => {
          console.error(u.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function vu(u = hu.n.NONE, e = bu, t = !1) {
          (0, n.useEffect)(() => {
            if (u !== hu.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === u) {
                if (o.O.view.isEventHandled()) return;
                (o.O.view.setEventHandled(), e(n), t && n.stopPropagation());
              }
            }
          }, [e, u, t]);
        }
        var fu = t(515);
        function wu() {}
        function Su(u) {
          return u;
        }
        function Tu() {
          return !1;
        }
        console.log;
        var Mu = t(174);
        function xu(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return Lu(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return Lu(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            t && (u = t);
            var n = 0;
            return function () {
              return n >= u.length ? { done: !0 } : { done: !1, value: u[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Lu(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, n = new Array(e); t < e; t++) n[t] = u[t];
          return n;
        }
        const yu = (u) => (0 === u ? window : window.subViews.get(u));
        const Ru = () => (u, e) => {
          const t = (0, n.createContext)({});
          return [
            function ({ mode: r = "real", options: i, children: s, mocks: l }) {
              const c = (0, n.useRef)([]),
                E = (t, n, a) => {
                  var r;
                  const i = (function ({
                      initializer: u = !0,
                      rootId: e = 0,
                      getRoot: t = yu,
                      context: n = "model",
                    } = {}) {
                      const a = new Map();
                      function r(u, e = 0) {
                        viewEnv.removeDataChangedCallback(u, e)
                          ? a.delete(u)
                          : console.error("Can't remove callback by id:", u);
                      }
                      engine.whenReady.then(() => {
                        engine.on("viewEnv.onDataChanged", (u, e, t) => {
                          t.forEach((e) => {
                            const t = a.get(e);
                            void 0 !== t && t(u);
                          });
                        });
                      });
                      const i = (u) => {
                        const a = t(e),
                          r = n.split(".").reduce((u, e) => u[e], a);
                        return "string" != typeof u || 0 === u.length
                          ? r
                          : u.split(".").reduce((u, e) => {
                              const t = u[e];
                              return "function" == typeof t ? t.bind(u) : t;
                            }, r);
                      };
                      return {
                        subscribe: (t, r) => {
                          const s = "string" == typeof r ? `${n}.${r}` : n,
                            l = o.O.view.addModelObserver(s, e, !0);
                          return (a.set(l, t), u && t(i(r)), l);
                        },
                        readByPath: i,
                        createCallback: (u, e) => {
                          const t = i(e);
                          return (...e) => {
                            t(u(...e));
                          };
                        },
                        createCallbackNoArgs: (u) => {
                          const e = i(u);
                          return () => {
                            e();
                          };
                        },
                        dispose: function () {
                          for (var u, t = xu(a.keys()); !(u = t()).done;) r(u.value, e);
                        },
                        unsubscribe: r,
                      };
                    })(n),
                    s =
                      "real" === t
                        ? i
                        : Object.assign({}, i, {
                            readByPath: null != (r = null == a ? void 0 : a.getter) ? r : () => {},
                          }),
                    l = (u) =>
                      "mocks" === t ? (null == a ? void 0 : a.getter(u)) : s.readByPath(u),
                    E = (u) => c.current.push(u),
                    m = u({
                      mode: t,
                      readByPath: l,
                      externalModel: s,
                      observableModel: {
                        array: (u, e) => {
                          const n = null != e ? e : l(u),
                            a = Mu.LO.box(n, { equals: Tu });
                          return (
                            "real" === t &&
                              s.subscribe(
                                (0, Mu.aD)((u) => a.set(u)),
                                u,
                              ),
                            a
                          );
                        },
                        object: (u, e) => {
                          const n = null != e ? e : l(u),
                            a = Mu.LO.box(n, { equals: Tu });
                          return (
                            "real" === t &&
                              s.subscribe(
                                (0, Mu.aD)((u) => a.set(u)),
                                u,
                              ),
                            a
                          );
                        },
                        primitives: (u, e) => {
                          const n = l(e);
                          if (Array.isArray(u)) {
                            const a = u.reduce((u, e) => ((u[e] = Mu.LO.box(n[e], {})), u), {});
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, Mu.aD)((e) => {
                                    u.forEach((u) => {
                                      a[u].set(e[u]);
                                    });
                                  }),
                                  e,
                                ),
                              a
                            );
                          }
                          {
                            const a = u,
                              r = Object.entries(a),
                              o = r.reduce((u, [e, t]) => ((u[t] = Mu.LO.box(n[e], {})), u), {});
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, Mu.aD)((u) => {
                                    r.forEach(([e, t]) => {
                                      o[t].set(u[e]);
                                    });
                                  }),
                                  e,
                                ),
                              o
                            );
                          }
                        },
                      },
                      cleanup: E,
                    }),
                    A = { mode: t, model: m, externalModel: s, cleanup: E };
                  return {
                    model: m,
                    controls: "mocks" === t && a ? a.controls(A) : e(A),
                    externalModel: s,
                    mode: t,
                  };
                },
                m = (0, n.useRef)(!1),
                A = (0, n.useState)(r),
                d = A[0],
                _ = A[1],
                F = (0, n.useState)(() => E(r, i, l)),
                D = F[0],
                B = F[1];
              return (
                (0, n.useEffect)(() => {
                  m.current ? B(E(d, i, l)) : (m.current = !0);
                }, [l, d, i]),
                (0, n.useEffect)(() => {
                  _(r);
                }, [r]),
                (0, n.useEffect)(
                  () => () => {
                    (D.externalModel.dispose(), c.current.forEach((u) => u()));
                  },
                  [D],
                ),
                a().createElement(t.Provider, { value: D }, s)
              );
            },
            () => (0, n.useContext)(t),
          ];
        };
        var Ou = t(946);
        const ku = Ru()(
            ({ observableModel: u }) => {
              const e = Object.assign(
                  {
                    filterInfo: u.primitives(["mapsSelected", "mapsTotal", "isFilterApplied"]),
                    cooldownTime: u.primitives(["cooldownTime"]),
                  },
                  u.primitives(["isWotPlusEnabled"]),
                ),
                t = (0, Ou.Om)(() => e.cooldownTime.cooldownTime.get() - Date.now() / 1e3 >= 0, {
                  equals: Tu,
                });
              return Object.assign({ computes: { getIsInCooldown: t } }, e);
            },
            ({ externalModel: u }) => ({
              onBackAction: u.createCallbackNoArgs("onBackAction"),
              onMapAddToBlacklist: u.createCallback(
                (u) => ({ mapId: u }),
                "onMapAddToBlacklistEvent",
              ),
              onMapRemoveFromBlacklist: u.createCallback(
                (u) => ({ mapId: u }),
                "onMapRemoveFromBlacklistEvent",
              ),
              onFilterReset: u.createCallbackNoArgs("onFilterReset"),
              onFilterClick: u.createCallback((u) => ({ seasonID: u }), "onFilterClick"),
              buyPremiumClick: u.createCallbackNoArgs("onBuyPremiumClick"),
              getSubscriptionClick: u.createCallbackNoArgs("onGetSubscriptionClick"),
            }),
          ),
          Nu = ku[0],
          Iu = ku[1],
          Pu = {
            get header() {
              return R.strings.excluded_maps.header.title();
            },
            get filterTooltipDesc() {
              return R.strings.excluded_maps.filtersTooltip.desc();
            },
            get cooldownHeader() {
              return R.strings.excluded_maps.header.cooldown();
            },
            get totalMapsDisplayed() {
              return R.strings.excluded_maps.totalMapsDisplayed();
            },
            get filteredMapsDisplayed() {
              return R.strings.excluded_maps.filteredMapsDisplayed();
            },
            get backButtonLabel() {
              return R.strings.excluded_maps.backButton.label();
            },
            get backButtonTo() {
              return R.strings.excluded_maps.backButton.to();
            },
            get mapsFilterLabel() {
              return R.strings.excluded_maps.mapsFilterLabel();
            },
            get hoverExclude() {
              return R.strings.excluded_maps.mapTile.hoverExclude();
            },
            get hoverExcludeButton() {
              return R.strings.excluded_maps.mapTile.hoverExcludeButton();
            },
            get hoverInclude() {
              return R.strings.excluded_maps.mapTile.hoverInclude();
            },
            get hoverIncludeButton() {
              return R.strings.excluded_maps.mapTile.hoverIncludeButton();
            },
            get cooldownTooltipBody() {
              return R.strings.excluded_maps.mapTile.cooldownTooltipBody();
            },
            get cooldownTooltipHeader() {
              return R.strings.excluded_maps.mapTile.cooldownTooltipHeader();
            },
            get notSelected() {
              return R.strings.excluded_maps.notSelected();
            },
          };
        let Hu;
        function Wu(u, e) {
          return u.replace(/\{\w+\}/g, (u) => String(e[u.slice(1, -1)]));
        }
        !(function (u) {
          ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
        })(Hu || (Hu = {}));
        const Gu = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          Uu = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          ju = (u, e, t = Hu.left) => u.split(e).reduce(t === Hu.left ? Gu : Uu, []),
          Vu = (() => {
            const u = new RegExp(
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
            return (e) =>
              e
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(u);
          })(),
          Ku = ["zh_cn", "zh_sg", "zh_tw"],
          $u = (u, e = Hu.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return Ku.includes(t)
              ? Vu(u)
              : ((u, e = Hu.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = u.replace(/&nbsp;/g, " ");
                  return (ju(a, /( )/, e).forEach((u) => (t = t.concat(ju(u, n, Hu.left)))), t);
                })(u, e);
          },
          zu = "FormatText_base_d0",
          Xu = ({ binding: u, text: e = "", classMix: t, alignment: r = Hu.left }) =>
            null === e
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  n.Fragment,
                  null,
                  e.split("\n").map((e, o) =>
                    a().createElement(
                      "div",
                      { className: g()(zu, t), key: `${e}-${o}` },
                      ((u, e, t) =>
                        u
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((u) => (t && u in t ? t[u] : $u(u, e))))(e, r, u).map((u, e) =>
                        a().createElement(n.Fragment, { key: `${e}-${u}` }, u),
                      ),
                    ),
                  ),
                );
        let Yu;
        !(function (u) {
          ((u.SHORT_DATE = "short-date"),
            (u.SHORT_TIME = "short-time"),
            (u.SHORT_DATE_TIME = "short-date-time"),
            (u.FULL_DATE = "full-date"),
            (u.FULL_DATE_TIME = "full-date-time"),
            (u.MONTH = "month"),
            (u.MONTH_DATE = "month-date"),
            (u.DATE_MONTH = "date-month"),
            (u.MONTH_YEAR = "month-year"),
            (u.WEEK_DAY = "week-day"),
            (u.WEEK_DAY_TIME = "week-day-time"),
            (u.YEAR = "year"),
            (u.DATE_YEAR = "date-year"));
        })(Yu || (Yu = {}));
        const qu = 1e3,
          Zu = 60,
          Qu = 3600,
          Ju = 86400;
        Date.now();
        function ue(u = 0) {
          let e = u;
          const t = Math.trunc(e / Ju);
          e -= t * Ju;
          const n = Math.trunc(e / Qu);
          e -= n * Qu;
          const a = Math.trunc(e / Zu);
          return ((e -= a * Zu), { days: t, hours: n, minutes: a, seconds: e });
        }
        const ee = () => {},
          te = (u = 0, e, t = 0, a = ee) => {
            const r = (0, n.useState)(u),
              o = r[0],
              i = r[1];
            return (
              (0, n.useEffect)(() => {
                if (u > 0) {
                  i(u);
                  const n = Date.now(),
                    r = setInterval(
                      () => {
                        const e = u - Math.floor((Date.now() - n) / qu);
                        null !== t && e <= t ? (i(t), a && a(), clearInterval(r)) : i(e);
                      },
                      (e || (u > 120 ? Zu : 1)) * qu,
                    );
                  return () => {
                    clearInterval(r);
                  };
                }
                i(0);
              }, [u, e, t, a]),
              o
            );
          },
          ne = (u) =>
            u.days > 0
              ? Wu(R.strings.common.duration.days(), { days: u.days })
              : u.hours > 0
                ? Wu(R.strings.common.duration.hours(), { hours: u.hours })
                : u.minutes > 0
                  ? Wu(R.strings.common.duration.minutes(), { minutes: u.minutes })
                  : Wu(R.strings.common.duration.seconds(), { seconds: u.seconds }),
          ae =
            ((0, n.memo)(({ duration: u }) => {
              const e = u >= 0 ? ne(ue(u)) : R.strings.common.duration.unlimited();
              return a().createElement("span", null, e);
            }),
            { days: 0, hours: 0, minutes: 0, seconds: 0 }),
          re = (u) =>
            ne(
              ((u) => {
                const e = ue(Math.max(0, Math.ceil(u))),
                  t = e.minutes > 0 || e.seconds > 0,
                  n = e.hours > 0 || t;
                return e.days > 0
                  ? Object.assign({}, ae, { days: e.days + (n ? 1 : 0) })
                  : e.hours > 0
                    ? Object.assign({}, ae, { hours: e.hours + (t ? 1 : 0) })
                    : e.minutes > 0
                      ? Object.assign({}, ae, { minutes: e.minutes + (e.seconds > 0 ? 1 : 0) })
                      : e.seconds > 0
                        ? Object.assign({}, ae, { minutes: 1 })
                        : ae;
              })(u),
            ),
          oe = (u) => u - Date.now() / qu,
          ie = (u) => {
            const e = R.strings.arenas;
            return e[`c_${u.mapId}`] && e[`c_${u.mapId}`].name ? e[`c_${u.mapId}`].name() : "";
          },
          se = (u) => {
            const e = R.images.gui.maps.icons.map;
            return e[`c_${u.mapId}`] ? e[`c_${u.mapId}`]() : "";
          },
          le = "CooldownHeader_base_54",
          ce = "CooldownHeader_endTime_02",
          Ee = "CooldownHeader_glow_f6",
          me = (0, fu.Pi)(({ className: u }) => {
            const e = Iu().model.cooldownTime.cooldownTime.get(),
              t = oe(e),
              n = te(t),
              r = { cooldownEndTime: a().createElement("span", { className: ce }, re(n)) };
            return a().createElement(
              "div",
              { className: g()(le, u) },
              a().createElement("img", {
                src: R.images.gui.maps.icons.excluded_maps.cooldown_bg(),
                className: Ee,
              }),
              a().createElement(Xu, { text: Pu.cooldownHeader, binding: r }),
            );
          }),
          Ae = "ExcludedMapsViewApp_base_a0",
          de = "ExcludedMapsViewApp_backButton_20",
          _e = "ExcludedMapsViewApp_headerBlock_1a",
          Fe = "ExcludedMapsViewApp_infoIcon_0f",
          De = "ExcludedMapsViewApp_header_fe",
          Be = "ExcludedMapsViewApp_cooldownHeader_d8",
          Ce = "ExcludedMapsViewApp_slotsContainer_14",
          ge = "ExcludedMapsViewApp_filterContainer_4f",
          pe = "ExcludedMapsViewApp_mainContainer_d8",
          he = "ExcludedMapsViewApp_maps_68",
          be = "ExcludedMapsViewApp_scrollArea_4c",
          ve = "ExcludedMapsViewApp_scrollBar_f4",
          fe = "ExcludedMapsViewApp_mapTile_05",
          we = "ExcludedMapsViewApp_divider_1a";
        let Se, Te;
        (!(function (u) {
          ((u.main = "main"),
            (u.primary = "primary"),
            (u.primaryGreen = "primaryGreen"),
            (u.primaryRed = "primaryRed"),
            (u.secondary = "secondary"),
            (u.ghost = "ghost"));
        })(Se || (Se = {})),
          (function (u) {
            ((u.extraSmall = "extraSmall"), (u.small = "small"), (u.medium = "medium"));
          })(Te || (Te = {})));
        const Me = {
          base: "ToggleButton_base_2c",
          base__button: "ToggleButton_base__button_cb",
          base__active: "ToggleButton_base__active_a6",
          base__slot: "ToggleButton_base__slot_98",
          base__disabled: "ToggleButton_base__disabled_19",
          texture: "ToggleButton_texture_f1",
          background: "ToggleButton_background_ef",
          background__main: "ToggleButton_background__main_68",
          background__primary: "ToggleButton_background__primary_a9",
          background__primaryGreen: "ToggleButton_background__primaryGreen_4f",
          background__primaryRed: "ToggleButton_background__primaryRed_ca",
          background__secondary: "ToggleButton_background__secondary_b2",
          background__ghost: "ToggleButton_background__ghost_d6",
          content: "ToggleButton_content_63",
          overlay: "ToggleButton_overlay_23",
          indicator: "ToggleButton_indicator_a7",
        };
        let xe;
        !(function (u) {
          ((u.Button = "button"), (u.Slot = "slot"));
        })(xe || (xe = {}));
        const Le = () => {},
          ye = a().memo(
            ({
              active: u = !1,
              className: e,
              children: t,
              toggleType: r = xe.Button,
              toggleButtonType: o = Se.secondary,
              onClick: i,
              disabled: s,
              soundClick: l = "play",
              soundHover: c = "highlight",
              onMouseEnter: E = Le,
              onMouseDown: m = Le,
              onMouseUp: A = Le,
              onMouseLeave: d = Le,
            }) => {
              const _ = (0, n.useCallback)(
                  (e) => {
                    s || (Y(l), i && i(e, u));
                  },
                  [i, s, u, l],
                ),
                F = (0, n.useCallback)(
                  (u) => {
                    s || (Y(c), E && E(u));
                  },
                  [s, c, E],
                ),
                D = (0, n.useCallback)(
                  (u) => {
                    s || ((1 !== u.button && 2 !== u.button) || (null !== l && Y(l)), m && m(u));
                  },
                  [m, s, l],
                ),
                B = g()(Me.base, e, Me[`base__${r}`], u && Me.base__active, s && Me.base__disabled);
              return a().createElement(
                "div",
                {
                  className: B,
                  onClick: _,
                  onMouseEnter: F,
                  onMouseUp: s ? Le : A,
                  onMouseDown: D,
                  onMouseLeave: s ? Le : d,
                },
                a().createElement("div", { className: Me.content }, t),
                r === xe.Button &&
                  a().createElement(
                    a().Fragment,
                    null,
                    a().createElement("div", {
                      className: g()(Me.background, Me[`background__${o}`]),
                    }),
                    a().createElement("div", { className: Me.texture }),
                  ),
                a().createElement("div", { className: Me.overlay }),
                a().createElement("div", { className: Me.indicator }),
              );
            },
          ),
          Re = ["children", "body", "header", "note", "alert", "args"];
        function Oe() {
          return (
            (Oe =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Oe.apply(this, arguments)
          );
        }
        const ke = R.views.common.tooltip_window.simple_tooltip_content,
          Ne = (u) => {
            let e = u.children,
              t = u.body,
              r = u.header,
              o = u.note,
              i = u.alert,
              s = u.args,
              l = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, Re);
            const c = (0, n.useMemo)(() => {
              const u = Object.assign({}, s, { body: t, header: r, note: o, alert: i });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [i, t, r, o, s]);
            return a().createElement(
              pu,
              Oe(
                {
                  contentId:
                    ((E = null == s ? void 0 : s.hasHtmlContent),
                    E ? ke.SimpleTooltipHtmlContent("resId") : ke.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              e,
            );
            var E;
          },
          Ie = (u, e) => !["$dyn", "$num", "$plural"].includes(u) && u in e,
          Pe = "FilterControls_base_17",
          He = "FilterControls_filterLabel_d0";
        function We(u, e) {
          return Array.isArray(u)
            ? u.map(e)
            : u.map((u, t, n) => e(null == u ? void 0 : u.value, t, n));
        }
        const Ge = Ru()(({ observableModel: u }) => {
            const e = { mapFilters: u.array("items", []) },
              t = (0, Ou.Om)(() => We(e.mapFilters.get(), Su), { equals: Tu });
            return Object.assign({ computes: { getMapFilters: t } }, e);
          }, wu),
          Ue = Ge[0],
          je = Ge[1],
          Ve = (u) => {
            const e = R.images.gui.maps.icons.customization.items_popover,
              t = u + "16x16";
            return Ie(t, e) ? e[t]() : "";
          },
          Ke = (u) => {
            const e = R.strings.excluded_maps.filtersTooltip.header;
            return Ie(u, e) ? e[u]() : "";
          },
          $e = (0, fu.Pi)(({ onFilterClick: u }) => {
            const e = je().model.computes.getMapFilters();
            return a().createElement(
              "div",
              { className: Pe },
              a().createElement("div", { className: He }, Pu.mapsFilterLabel),
              e.map((e) =>
                a().createElement(
                  Ne,
                  { key: e.filterID, header: Ke(e.filterName), body: Pu.filterTooltipDesc },
                  a().createElement(
                    ye,
                    { active: e.selected, onClick: () => u(e.filterID) },
                    a().createElement("img", { src: Ve(e.filterName) }),
                  ),
                ),
              ),
            );
          }),
          ze = { context: "model.mapsFilters" },
          Xe = ({ onFilterClick: u }) =>
            a().createElement(Ue, { options: ze }, a().createElement($e, { onFilterClick: u })),
          Ye = {
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
          },
          qe = ({
            children: u,
            size: e,
            isFocused: t,
            type: r,
            disabled: o,
            mixClass: i,
            soundHover: s,
            soundClick: l,
            onMouseEnter: c,
            onMouseMove: E,
            onMouseDown: m,
            onMouseUp: A,
            onMouseLeave: d,
            onClick: _,
          }) => {
            const F = (0, n.useRef)(null),
              D = (0, n.useState)(t),
              B = D[0],
              C = D[1],
              p = (0, n.useState)(!1),
              h = p[0],
              b = p[1],
              v = (0, n.useState)(!1),
              f = v[0],
              w = v[1],
              S = (0, n.useCallback)(() => {
                o || (F.current && (F.current.focus(), C(!0)));
              }, [o]),
              T = (0, n.useCallback)(
                (u) => {
                  B && null !== F.current && !F.current.contains(u.target) && C(!1);
                },
                [B],
              ),
              M = (0, n.useCallback)(
                (u) => {
                  o || (_ && _(u));
                },
                [o, _],
              ),
              x = (0, n.useCallback)(
                (u) => {
                  o || (null !== s && Y(s), c && c(u), w(!0));
                },
                [o, s, c],
              ),
              L = (0, n.useCallback)(
                (u) => {
                  E && E(u);
                },
                [E],
              ),
              y = (0, n.useCallback)(
                (u) => {
                  o || (A && A(u), b(!1));
                },
                [o, A],
              ),
              O = (0, n.useCallback)(
                (u) => {
                  o || (null !== l && Y(l), m && m(u), t && S(), b(!0));
                },
                [o, l, m, S, t],
              ),
              k = (0, n.useCallback)(
                (u) => {
                  o || (d && d(u), b(!1));
                },
                [o, d],
              ),
              N = g()(
                Ye.base,
                Ye[`base__${r}`],
                {
                  [Ye.base__disabled]: o,
                  [Ye[`base__${e}`]]: e,
                  [Ye.base__focus]: B,
                  [Ye.base__highlightActive]: h,
                  [Ye.base__firstHover]: f,
                },
                i,
              ),
              I = g()(Ye.state, Ye.state__default);
            return (
              (0, n.useEffect)(
                () => (
                  document.addEventListener("mousedown", T),
                  () => {
                    document.removeEventListener("mousedown", T);
                  }
                ),
                [T],
              ),
              (0, n.useEffect)(() => {
                C(t);
              }, [t]),
              a().createElement(
                "div",
                {
                  ref: F,
                  className: N,
                  onMouseEnter: x,
                  onMouseMove: L,
                  onMouseUp: y,
                  onMouseDown: O,
                  onMouseLeave: k,
                  onClick: M,
                },
                r !== Se.ghost &&
                  a().createElement(
                    a().Fragment,
                    null,
                    a().createElement("div", { className: Ye.back }),
                    a().createElement("span", { className: Ye.texture }),
                  ),
                a().createElement(
                  "span",
                  { className: I },
                  a().createElement("span", { className: Ye.stateDisabled }),
                  a().createElement("span", { className: Ye.stateHighlightHover }),
                  a().createElement("span", { className: Ye.stateHighlightActive }),
                ),
                a().createElement(
                  "span",
                  { className: Ye.content, lang: R.strings.settings.LANGUAGE_CODE() },
                  u,
                ),
              )
            );
          };
        qe.defaultProps = {
          type: Se.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Ze = (0, n.memo)(qe),
          Qe = {
            base: "MapCounter_base_ef",
            highlightedCount: "MapCounter_highlightedCount_5a",
            clearButton: "MapCounter_clearButton_26",
            clearButton__hidden: "MapCounter_clearButton__hidden_63",
            closeIcon: "MapCounter_closeIcon_0a",
            filterGlow: "MapCounter_filterGlow_8c",
          },
          Je = (0, fu.Pi)(() => {
            const u = Iu(),
              e = u.model,
              t = u.controls,
              n = e.filterInfo.isFilterApplied.get(),
              r = e.filterInfo.mapsSelected.get(),
              o = e.filterInfo.mapsTotal.get(),
              i = t.onFilterReset;
            return a().createElement(
              "div",
              { className: Qe.base },
              n
                ? a().createElement(
                    a().Fragment,
                    null,
                    a().createElement(Xu, {
                      text: Pu.filteredMapsDisplayed,
                      classMix: Qe.label,
                      binding: {
                        count: a().createElement("span", { className: Qe.highlightedCount }, r),
                        total: o,
                      },
                    }),
                    a().createElement("img", {
                      src: R.images.gui.maps.icons.excluded_maps.filter_glow(),
                      className: Qe.filterGlow,
                    }),
                  )
                : a().createElement(Xu, {
                    text: Pu.totalMapsDisplayed,
                    classMix: Qe.label,
                    binding: {
                      count: a().createElement("span", { className: Qe.highlightedCount }, o),
                    },
                  }),
              a().createElement(
                Ze,
                {
                  type: "ghost",
                  mixClass: g()(Qe.clearButton, !n && Qe.clearButton__hidden),
                  onClick: () => i(),
                },
                a().createElement("img", {
                  src: R.images.gui.maps.icons.library.cross(),
                  className: Qe.closeIcon,
                }),
              ),
            );
          });
        let ut, et;
        (!(function (u) {
          ((u.MAPS_BLACKLIST_SLOT_STATE_ACTIVE = "active"),
            (u.MAPS_BLACKLIST_SLOT_STATE_CHANGE = "change"),
            (u.MAPS_BLACKLIST_SLOT_STATE_DISABLED = "disabled"),
            (u.MAPS_BLACKLIST_SLOT_STATE_DISABLED_BY_KILL_SWITCH = "disabledByKillSwitch"),
            (u.MAPS_BLACKLIST_SLOT_STATE_COOLDOWN = "cooldown"),
            (u.MAPS_BLACKLIST_SLOT_STATE_SELECTED = "selected"),
            (u.MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER = "activeNoHover"));
        })(ut || (ut = {})),
          (function (u) {
            ((u.DEFAULT = "defaultSlots"),
              (u.PREMIUM = "premiumSlots"),
              (u.SUBSCRB = "subscrbSlots"),
              (u.REWARDS = "rewardsSlots"));
          })(et || (et = {})));
        const tt = "MapTile_base_fe",
          nt = "MapTile_glowFrame_4e",
          at = "MapTile_mapCross_da",
          rt = "MapTile_lockIcon_bb",
          ot = "MapTile_hoverText_35",
          it = "MapTile_mapOverlay_5c",
          st = "MapTile_base__available_d2",
          lt = "MapTile_hoverOverlay_93",
          ct = "MapTile_base__excluded_3c",
          Et = "MapTile_hoverButton_d3",
          mt = "MapTile_base__cooldown_d6",
          At = "MapTile_mapImage_c8",
          dt = "MapTile_disabledTile_ec",
          _t = "MapTile_mapName_d1",
          Ft = "MapTile_base__disabled_95",
          Dt = "MapTile_hoverMapName_db",
          Bt = "MapTile_hoverButtonContainer_bf",
          Ct = ({
            state: u,
            mapId: e,
            onMapAddToBlacklist: t,
            onMapRemoveFromBlacklist: r,
            className: o,
          }) => {
            const i = ie({ mapId: e }),
              s = g()(
                o,
                tt,
                u === ut.MAPS_BLACKLIST_SLOT_STATE_ACTIVE && st,
                u === ut.MAPS_BLACKLIST_SLOT_STATE_COOLDOWN && mt,
                u === ut.MAPS_BLACKLIST_SLOT_STATE_CHANGE && ct,
                u === ut.MAPS_BLACKLIST_SLOT_STATE_DISABLED && Ft,
              ),
              l = (0, n.useMemo)(
                () => ({ mapName: a().createElement("span", { className: Dt }, `"${i}"`) }),
                [i],
              );
            return u === ut.MAPS_BLACKLIST_SLOT_STATE_ACTIVE
              ? a().createElement(
                  "div",
                  { className: s },
                  a().createElement("img", { src: se({ mapId: e }), className: At }),
                  a().createElement("img", {
                    src: R.images.gui.maps.icons.excluded_maps.map_shadow(),
                    className: it,
                  }),
                  a().createElement("div", { className: _t }, ie({ mapId: e })),
                  a().createElement(
                    "div",
                    { className: lt },
                    a().createElement(
                      "div",
                      null,
                      a().createElement(Xu, { text: Pu.hoverExclude, binding: l, classMix: ot }),
                    ),
                    a().createElement(
                      "div",
                      { className: Bt },
                      a().createElement(
                        Ze,
                        { mixClass: Et, onClick: () => t(e) },
                        Pu.hoverExcludeButton,
                      ),
                    ),
                  ),
                )
              : u === ut.MAPS_BLACKLIST_SLOT_STATE_COOLDOWN
                ? a().createElement(
                    Ne,
                    { header: Pu.cooldownTooltipHeader, body: Pu.cooldownTooltipBody },
                    a().createElement(
                      "div",
                      { className: s },
                      a().createElement("img", { src: se({ mapId: e }), className: At }),
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.excluded_maps.map_shadow(),
                        className: it,
                      }),
                      a().createElement("div", { className: dt }),
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.excluded_maps.map_glow_frame(),
                        className: nt,
                      }),
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.excluded_maps.map_deleted_cross(),
                        className: at,
                      }),
                      a().createElement("div", { className: _t }, ie({ mapId: e })),
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.excluded_maps.icon_lock(),
                        className: rt,
                      }),
                    ),
                  )
                : u === ut.MAPS_BLACKLIST_SLOT_STATE_CHANGE
                  ? a().createElement(
                      "div",
                      { className: s },
                      a().createElement("img", { src: se({ mapId: e }), className: At }),
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.excluded_maps.map_shadow(),
                        className: it,
                      }),
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.excluded_maps.map_glow_frame(),
                        className: nt,
                      }),
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.excluded_maps.map_deleted_cross(),
                        className: at,
                      }),
                      a().createElement("div", { className: _t }, ie({ mapId: e })),
                      a().createElement(
                        "div",
                        { className: lt },
                        a().createElement(
                          "div",
                          null,
                          a().createElement(Xu, {
                            text: Pu.hoverInclude,
                            binding: l,
                            classMix: ot,
                          }),
                        ),
                        a().createElement(
                          "div",
                          { className: Bt },
                          a().createElement(
                            Ze,
                            { mixClass: Et, onClick: () => r(e) },
                            Pu.hoverIncludeButton,
                          ),
                        ),
                      ),
                    )
                  : a().createElement(
                      Ne,
                      { header: Pu.cooldownTooltipHeader, body: Pu.cooldownTooltipBody },
                      a().createElement(
                        "div",
                        { className: s },
                        a().createElement("img", { src: se({ mapId: e }), className: At }),
                        a().createElement("img", {
                          src: R.images.gui.maps.icons.excluded_maps.map_shadow(),
                          className: it,
                        }),
                        a().createElement("div", { className: _t }, ie({ mapId: e })),
                      ),
                    );
          },
          gt = Ru()(({ observableModel: u }) => {
            const e = { maps: u.array("items", []) },
              t = (0, Ou.Om)(() => We(e.maps.get(), Su).filter((u) => u.filtered), { equals: Tu });
            return Object.assign({ computes: { getMaps: t } }, e);
          }, wu),
          pt = gt[0],
          ht = gt[1],
          bt = (0, fu.Pi)(
            ({ className: u, onMapAddToBlacklist: e, onMapRemoveFromBlacklist: t }) => {
              const n = ht().model.computes.getMaps();
              return a().createElement(
                "div",
                { className: u },
                n.map((u) =>
                  a().createElement(Ct, {
                    mapCooldownTime: u.cooldownTime,
                    mapId: u.mapId,
                    state: u.state,
                    onMapAddToBlacklist: e,
                    onMapRemoveFromBlacklist: t,
                    className: fe,
                    key: u.mapId,
                  }),
                ),
              );
            },
          ),
          vt = { context: "model.maps" },
          ft = (0, n.memo)(function ({
            className: u,
            onMapAddToBlacklist: e,
            onMapRemoveFromBlacklist: t,
          }) {
            return a().createElement(
              pt,
              { options: vt },
              a().createElement(bt, {
                className: u,
                onMapAddToBlacklist: e,
                onMapRemoveFromBlacklist: t,
              }),
            );
          });
        var wt = t(887),
          St = t.n(wt);
        const Tt = ["xl", "lg", "md", "sm", "xs"],
          Mt = (u) => u.includes("_") && ((u) => Tt.includes(u))(u.split("_").at(-1)),
          xt = [b.ExtraLarge, b.Large, b.Medium, b.Small, b.ExtraSmall],
          Lt = (u, e) =>
            Object.keys(u).reduce((t, n) => {
              if (n in t) return t;
              if (Mt(n)) {
                const a = n.split("_").slice(0, -1).join("_");
                if (a in t) return t;
                const r = xt.indexOf(e),
                  o = (-1 !== r ? Tt.slice(r) : [])
                    .map((u) => a + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  i = o ? u[o] : void 0;
                return ((t[a] = void 0 !== i ? i : u[a]), t);
              }
              const a = u[n];
              return (
                void 0 === a ||
                  ((u, e) => Tt.some((t) => void 0 !== e[`${u}_${t}`]))(n, u) ||
                  (t[n] = a),
                t
              );
            }, {}),
          yt = (u, e = Lt) => {
            const t = (
              (u, e = Lt) =>
              (t) => {
                const r = w().mediaSize,
                  o = (0, n.useMemo)(() => e(t, r), [t, r]);
                return a().createElement(u, o);
              }
            )(u, e);
            return a().memo((e) =>
              Object.keys(e).some((u) => Mt(u) && void 0 !== e[u])
                ? a().createElement(t, e)
                : a().createElement(u, e),
            );
          },
          Rt = {
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
          Ot = [
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
        function kt() {
          return (
            (kt =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            kt.apply(this, arguments)
          );
        }
        Object.keys(St());
        const Nt = {
            XL: { mt: Rt.mt__XL, mr: Rt.mr__XL, mb: Rt.mb__XL, ml: Rt.ml__XL },
            LG: { mt: Rt.mt__LG, mr: Rt.mr__LG, mb: Rt.mb__LG, ml: Rt.ml__LG },
            MDp: { mt: Rt.mt__MDp, mr: Rt.mr__MDp, mb: Rt.mb__MDp, ml: Rt.ml__MDp },
            MD: { mt: Rt.mt__MD, mr: Rt.mr__MD, mb: Rt.mb__MD, ml: Rt.ml__MD },
            SMp: { mt: Rt.mt__SMp, mr: Rt.mr__SMp, mb: Rt.mb__SMp, ml: Rt.ml__SMp },
            SM: { mt: Rt.mt__SM, mr: Rt.mr__SM, mb: Rt.mb__SM, ml: Rt.ml__SM },
            XS: { mt: Rt.mt__XS, mr: Rt.mr__XS, mb: Rt.mb__XS, ml: Rt.ml__XS },
          },
          It = (Object.keys(Nt), ["mt", "mr", "mb", "ml"]),
          Pt = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Ht = yt((u) => {
            let e = u.className,
              t = u.width,
              r = u.height,
              o = u.m,
              i = u.mt,
              s = void 0 === i ? o : i,
              l = u.mr,
              c = void 0 === l ? o : l,
              E = u.mb,
              m = void 0 === E ? o : E,
              A = u.ml,
              d = void 0 === A ? o : A,
              _ = u.column,
              F = u.row,
              D = u.flexDirection,
              B = void 0 === D ? (_ ? "column" : F && "row") || void 0 : D,
              C = u.flexStart,
              p = u.center,
              h = u.flexEnd,
              b = u.spaceBetween,
              v = u.spaceAround,
              f = u.justifyContent,
              w =
                void 0 === f
                  ? (C ? "flex-start" : p && "center") ||
                    (h && "flex-end") ||
                    (b && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : f,
              S = u.alignItems,
              T =
                void 0 === S
                  ? (C ? "flex-start" : p && "center") || (h && "flex-end") || void 0
                  : S,
              M = u.alignSelf,
              x = u.wrap,
              L = u.flexWrap,
              y = void 0 === L ? (x ? "wrap" : void 0) : L,
              R = u.grow,
              O = u.shrink,
              k = u.flex,
              N = void 0 === k ? (R || O ? `${R ? 1 : 0} ${O ? 1 : 0} auto` : void 0) : k,
              I = u.style,
              P = u.children,
              H = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, Ot);
            const W = (0, n.useMemo)(() => {
                const u = { mt: s, mr: c, mb: m, ml: d },
                  e = ((u) =>
                    It.reduce((e, t) => {
                      const n = u[t];
                      return n && "number" != typeof n ? e.concat(Nt[!0 === n ? "MD" : n][t]) : e;
                    }, []))(u),
                  n = ((u) =>
                    It.reduce((e, t) => {
                      const n = u[t];
                      return ("number" == typeof n && (e[Pt[t]] = n + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, I, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: N,
                    alignSelf: M,
                    display: B || T ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: y,
                    justifyContent: w,
                    alignItems: T,
                  }),
                  computedClassNames: e,
                };
              }, [t, r, s, c, m, d, I, N, M, B, y, w, T]),
              G = W.computedStyle,
              U = W.computedClassNames;
            return a().createElement(
              "div",
              kt({ className: g()(Rt.base, ...U, e), style: G }, H),
              P,
            );
          });
        var Wt = t(532),
          Gt = t.n(Wt);
        const Ut = {
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
          jt = [
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
        function Vt() {
          return (
            (Vt =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Vt.apply(this, arguments)
          );
        }
        Object.keys(St());
        const Kt = Object.keys(Gt()),
          $t = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          zt = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Xt = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Yt = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          qt =
            (Object.keys(Yt),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": $t,
              "heading-H36": $t,
              "heading-H28": zt,
              "heading-H24": zt,
              "heading-H24R": zt,
              "heading-H22": zt,
              "heading-H20R": zt,
              "heading-H18": zt,
              "heading-H15": Xt,
              "heading-H14": Xt,
              "paragraph-P24": zt,
              "paragraph-P18": zt,
              "paragraph-P16": zt,
              "paragraph-P14": Xt,
              "paragraph-P12": Xt,
              "paragraph-P10": Xt,
            }),
          Zt =
            (Object.keys(qt),
            (u) =>
              u
                ? ((u) => Kt.includes(u))(u)
                  ? { colorClassName: Ut[u] }
                  : { colorStyle: { color: u } }
                : {}),
          Qt = yt((u) => {
            let e = u.text,
              t = u.variant,
              r = u.className,
              o = u.color,
              i = u.m,
              s = u.mt,
              l = void 0 === s ? i : s,
              c = u.mr,
              E = void 0 === c ? i : c,
              m = u.mb,
              A = void 0 === m ? i : m,
              d = u.ml,
              _ = void 0 === d ? i : d,
              F = u.style,
              D = u.format,
              B = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, jt);
            const C = (0, n.useMemo)(() => {
                const u = Zt(o),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  n = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, n), colorClassName: e };
              }, [F, o]),
              p = C.computedStyle,
              h = C.colorClassName;
            return a().createElement(
              Ht,
              Vt(
                {
                  className: g()(Ut.base, t && Ut[t], h, r),
                  style: p,
                  mt: !0 === l ? qt[t || "paragraph-P16"].mt : l,
                  mr: !0 === E ? qt[t || "paragraph-P16"].mr : E,
                  mb: !0 === A ? qt[t || "paragraph-P16"].mb : A,
                  ml: !0 === _ ? qt[t || "paragraph-P16"].ml : _,
                },
                B,
              ),
              void 0 !== D ? a().createElement(Xu, Vt({}, D, { text: e })) : e,
            );
          }),
          Jt = ["children"];
        function un() {
          return (
            (un =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            un.apply(this, arguments)
          );
        }
        const en = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                a = {},
                r = Object.keys(u);
              for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
              return a;
            })(u, Jt);
          return a().createElement(
            pu,
            un(
              {
                contentId:
                  R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                    "resId",
                  ),
                ignoreShowDelay: !0,
              },
              t,
            ),
            e,
          );
        };
        function tn() {
          return (
            (tn =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            tn.apply(this, arguments)
          );
        }
        const nn = ({ children: u, tooltipArgs: e, className: t }) => {
          if (!e) return u;
          const n = a().createElement("div", { className: t }, u);
          if (e.header || e.body) return a().createElement(Ne, e, n);
          const r = e.contentId,
            o = e.args,
            i = null == o ? void 0 : o.contentId;
          return r || i
            ? a().createElement(pu, tn({}, e, { contentId: r || i }), n)
            : a().createElement(en, e, n);
        };
        Du.Sw.instance;
        let an;
        !(function (u) {
          ((u.None = "None"), (u.Shallow = "Shallow"), (u.Deep = "Deep"));
        })(an || (an = {}));
        Du.Sw.instance;
        const rn = te,
          on = {
            base: "Slot_base_d5",
            base__cooldown: "Slot_base__cooldown_73",
            mapImage: "Slot_mapImage_29",
            base__next: "Slot_base__next_e1",
            base__disabled: "Slot_base__disabled_09",
            base__active: "Slot_base__active_94",
            cooldownContainer: "Slot_cooldownContainer_ef",
            cooldownIcon: "Slot_cooldownIcon_5a",
            cooldownText: "Slot_cooldownText_4b",
            timerContainer: "Slot_timerContainer_ff",
            timerIcon: "Slot_timerIcon_ba",
            timerText: "Slot_timerText_b9",
            type: "Slot_type_0b",
            base__premiumSlots: "Slot_base__premiumSlots_41",
            base__subscrbSlots: "Slot_base__subscrbSlots_06",
            mapTitle: "Slot_mapTitle_a0",
            removeButton: "Slot_removeButton_ce",
            removeButton__icon: "Slot_removeButton__icon_39",
            background: "Slot_background_53",
            base__disabled__premiumSlots: "Slot_base__disabled__premiumSlots_0d",
            base__disabled__subscrbSlots: "Slot_base__disabled__subscrbSlots_ff",
            lock: "Slot_lock_c9",
            lockGlow: "Slot_lockGlow_86",
            button: "Slot_button_ab",
          },
          sn = R.strings.excluded_maps.slot,
          ln = (0, n.memo)(
            ({
              isActive: u,
              map: e,
              isNext: t,
              isEnabled: r,
              isKillSwitch: o,
              getSubscriptionClick: i,
              buyPremiumClick: s,
              onRemoveButtonClick: l,
            }) => {
              const c = (0, n.useMemo)(() => {
                  const u = oe(e.cooldownTime),
                    t = oe(e.expirationTime);
                  return {
                    isInCooldown: u > 0,
                    isEventSlotActive: e.type === et.REWARDS && t > 0,
                    timeUntilCooldownEnd: u,
                    timeUntilEventSlotEnd: t,
                  };
                }, [e.cooldownTime, e.expirationTime, e.type]),
                E = c.isInCooldown,
                m = c.isEventSlotActive,
                A = c.timeUntilCooldownEnd,
                d = c.timeUntilEventSlotEnd,
                _ = e.type === et.REWARDS,
                F = rn(E ? Math.max(0, A) : 0, Zu),
                D = rn(m ? Math.max(0, d) : 0, Zu),
                B = E && F > 0,
                C = m && !B && D > 0,
                p = (0, n.useMemo)(() => {
                  return B
                    ? {
                        cooldownString: re(F),
                        timerString: null,
                        tooltipCooldownString: ((u = F), re(u)),
                      }
                    : C
                      ? { cooldownString: null, timerString: re(D), tooltipCooldownString: null }
                      : { cooldownString: null, timerString: null, tooltipCooldownString: null };
                  var u;
                }, [F, D, B, C]),
                h = p.cooldownString,
                b = p.timerString,
                v = p.tooltipCooldownString,
                f = g()(
                  on.base,
                  !B && "" !== e.mapId && on.base__replace,
                  B && on.base__cooldown,
                  on[`base__${e.type}`],
                  t && on.base__next,
                  u && on.base__active,
                ),
                w = ie(e);
              if (B) {
                const u = Wu(sn.cooldownTooltipBody(), { cooldownStr: v });
                return a().createElement(
                  nn,
                  {
                    tooltipArgs: _
                      ? {
                          contentId:
                            R.views.lobby.account_dashboard.tooltips.ExcludedMapsRewardSlotsTooltipView(
                              "resId",
                            ),
                        }
                      : { header: sn.cooldownTooltipHeader(), body: u },
                  },
                  a().createElement(
                    "div",
                    { className: f, "data-testid": "slot" },
                    a().createElement("img", { src: se(e), className: on.mapImage }),
                    a().createElement("div", { className: on.type }),
                    a().createElement(
                      "div",
                      { className: on.cooldownContainer, "data-testid": "timer" },
                      a().createElement("div", { className: on.cooldownIcon }),
                      a().createElement(Qt, { className: on.cooldownText, text: h }),
                    ),
                    a().createElement(Qt, { className: on.mapTitle, text: w }),
                  ),
                );
              }
              if (u)
                return a().createElement(
                  nn,
                  {
                    tooltipArgs: _
                      ? {
                          contentId:
                            R.views.lobby.account_dashboard.tooltips.ExcludedMapsRewardSlotsTooltipView(
                              "resId",
                            ),
                        }
                      : { header: sn.replaceTooltipHeader(), body: sn.replaceTooltipBody() },
                  },
                  a().createElement(
                    "div",
                    { className: f, "data-testid": "slot" },
                    l &&
                      a().createElement(
                        Ze,
                        { type: "ghost", mixClass: on.removeButton, onClick: () => l(e.mapId) },
                        a().createElement("img", {
                          src: R.images.gui.maps.icons.library.cross(),
                          className: on.removeButton__icon,
                        }),
                      ),
                    a().createElement("img", { src: se(e), className: on.mapImage }),
                    a().createElement("div", { className: on.mapTitle }, w),
                    a().createElement("div", { className: on.type }),
                    C &&
                      a().createElement(
                        "div",
                        { className: on.timerContainer, "data-testid": "timerEvent" },
                        a().createElement("div", { className: on.timerIcon }),
                        a().createElement(Qt, { className: on.timerText, text: b }),
                      ),
                  ),
                );
              if (!r) {
                const u =
                  !o ||
                  (e.type !== et.DEFAULT &&
                    e.type !== et.PREMIUM &&
                    e.type !== et.SUBSCRB &&
                    e.type !== et.REWARDS)
                    ? sn.disabledTooltipBody.$dyn(e.type)
                    : sn.disabledTooltipBody.defaultSlots();
                return a().createElement(
                  "div",
                  null,
                  a().createElement(
                    Ne,
                    { header: sn.disabledTooltipHeader(), body: u },
                    a().createElement(
                      "div",
                      {
                        className: g()(on.base, on.base__disabled, on[`base__disabled__${e.type}`]),
                        "data-testid": "slot",
                      },
                      a().createElement("div", { className: on.background }),
                      a().createElement("div", { className: on.lockGlow }),
                      a().createElement("div", { className: on.lock }),
                    ),
                  ),
                  e.type === et.PREMIUM &&
                    a().createElement(
                      Ze,
                      { mixClass: on.button, size: Te.small, type: Se.main, onClick: s },
                      a().createElement(Qt, { text: sn.buyPremButton() }),
                    ),
                  e.type === et.SUBSCRB &&
                    a().createElement(
                      Ze,
                      { mixClass: on.button, size: Te.small, type: Se.main, onClick: i },
                      a().createElement(Qt, { text: sn.buyWotPlusButton() }),
                    ),
                );
              }
              return a().createElement(
                nn,
                {
                  tooltipArgs: _
                    ? {
                        contentId:
                          R.views.lobby.account_dashboard.tooltips.ExcludedMapsRewardSlotsTooltipView(
                            "resId",
                          ),
                      }
                    : { header: sn.selectTooltipHeader(), body: sn.selectTooltipBody() },
                },
                a().createElement(
                  "div",
                  {
                    className: g()(on.base, on[`base__${e.type}`], t && on.base__next),
                    "data-testid": "slot",
                  },
                  a().createElement("div", { className: on.background }),
                  C &&
                    a().createElement(
                      "div",
                      { className: on.timerContainer, "data-testid": "timerEvent" },
                      a().createElement("div", { className: on.timerIcon }),
                      a().createElement(Qt, { className: on.timerText, text: b }),
                    ),
                ),
              );
            },
          ),
          cn = (u) =>
            null !== u && "object" == typeof u
              ? "CoherentArrayProxy" === u.constructor.name
                ? We(u, (u) => ("object" == typeof u ? cn(u) : u))
                : Array.isArray(u)
                  ? u.map((u) => ("object" == typeof u ? cn(u) : u))
                  : Object.fromEntries(
                      Object.entries(u).map(([u, e]) => [u, "object" == typeof e ? cn(e) : e]),
                    )
              : u,
          En = Ru()(({ observableModel: u }) => {
            const e = { excludedMaps: u.array("items", []) },
              t = (0, Ou.Om)(
                () => {
                  return ((u = e.excludedMaps.get()), cn(u));
                  var u;
                },
                { equals: Tu },
              );
            return Object.assign({ computes: { getExcludedMapSlots: t } }, e);
          }, wu),
          mn = En[0],
          An = En[1],
          dn = [
            ut.MAPS_BLACKLIST_SLOT_STATE_ACTIVE_NO_HOVER,
            ut.MAPS_BLACKLIST_SLOT_STATE_CHANGE,
            ut.MAPS_BLACKLIST_SLOT_STATE_COOLDOWN,
            ut.MAPS_BLACKLIST_SLOT_STATE_SELECTED,
          ],
          _n = (0, fu.Pi)(
            ({
              className: u,
              onMapRemoveFromBlacklist: e,
              getSubscriptionClick: t,
              buyPremiumClick: n,
            }) => {
              const r = An().model.computes.getExcludedMapSlots(),
                o = r.find(
                  (u) => "" === u.mapId && u.state === ut.MAPS_BLACKLIST_SLOT_STATE_ACTIVE,
                );
              return a().createElement(
                "div",
                { className: u },
                r.map((u, r) =>
                  a().createElement(ln, {
                    key: `${u.type}_${r}`,
                    map: u,
                    isActive: dn.includes(u.state),
                    isNext: (null == o ? void 0 : o.type) === u.type,
                    onRemoveButtonClick: e,
                    isEnabled:
                      u.state !== ut.MAPS_BLACKLIST_SLOT_STATE_DISABLED &&
                      u.state !== ut.MAPS_BLACKLIST_SLOT_STATE_DISABLED_BY_KILL_SWITCH,
                    isKillSwitch: u.state === ut.MAPS_BLACKLIST_SLOT_STATE_DISABLED_BY_KILL_SWITCH,
                    buyPremiumClick: n,
                    getSubscriptionClick: t,
                  }),
                ),
              );
            },
          ),
          Fn = { context: "model.disabledMaps" },
          Dn = (0, n.memo)(
            ({
              className: u,
              isWotPlusEnabled: e,
              onMapRemoveFromBlacklist: t,
              buyPremiumClick: n,
              getSubscriptionClick: r,
            }) =>
              a().createElement(
                mn,
                { options: Fn },
                a().createElement(_n, {
                  className: u,
                  isWotPlusEnabled: e,
                  onMapRemoveFromBlacklist: t,
                  buyPremiumClick: n,
                  getSubscriptionClick: r,
                }),
              ),
          ),
          Bn = { base: de },
          Cn = { base: ve },
          gn = (0, fu.Pi)(() => {
            const u = Iu(),
              e = u.model,
              t = u.controls;
            e.filterInfo.mapsSelected.get();
            const n = e.computes.getIsInCooldown(),
              r = e.isWotPlusEnabled.get();
            return (
              (function ({
                key: u = hu.n.ESCAPE,
                callback: e = () => o.O.view.sendEvent.close(),
                preventPropagation: t = !0,
              } = {}) {
                vu(u, e, t);
              })({ callback: t.onBackAction }),
              a().createElement(
                "div",
                { className: Ae },
                a().createElement(
                  "div",
                  { className: _e },
                  a().createElement(
                    "div",
                    { className: De },
                    a().createElement("h1", null, Pu.header),
                    a().createElement(
                      pu,
                      {
                        contentId:
                          R.views.lobby.premacc.maps_blacklist.maps_blacklist_tooltips.MapsBlacklistInfoTooltipContent(
                            "resId",
                          ),
                        decoratorId:
                          R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                      },
                      a().createElement("img", {
                        src: R.images.gui.maps.icons.library.info(),
                        alt: "",
                        className: Fe,
                      }),
                    ),
                  ),
                  n && a().createElement(me, { className: Be }),
                ),
                a().createElement(Fu, {
                  caption: Pu.backButtonLabel,
                  goto: Pu.backButtonTo,
                  classNames: Bn,
                  onClick: t.onBackAction,
                }),
                a().createElement(Dn, {
                  className: Ce,
                  isWotPlusEnabled: r,
                  onMapRemoveFromBlacklist: t.onMapRemoveFromBlacklist,
                  buyPremiumClick: t.buyPremiumClick,
                  getSubscriptionClick: t.getSubscriptionClick,
                }),
                a().createElement(
                  "div",
                  { className: pe },
                  a().createElement(
                    "div",
                    { className: ge },
                    a().createElement(Je, null),
                    a().createElement(Xe, { onFilterClick: t.onFilterClick }),
                  ),
                  a().createElement("div", { className: we }),
                  a().createElement(
                    Eu,
                    { api: X(), className: be, barClassNames: Cn },
                    a().createElement(ft, {
                      className: he,
                      onMapAddToBlacklist: t.onMapAddToBlacklist,
                      onMapRemoveFromBlacklist: t.onMapRemoveFromBlacklist,
                    }),
                  ),
                ),
              )
            );
          });
        engine.whenReady.then(() => {
          I().render(
            a().createElement(
              Nu,
              { mode: "real" },
              a().createElement(k, null, a().createElement(gn, null)),
            ),
            document.getElementById("root"),
          );
        });
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(u) {
    var e = __webpack_module_cache__[u];
    if (void 0 !== e) return e.exports;
    var t = (__webpack_module_cache__[u] = { exports: {} });
    return (__webpack_modules__[u](t, t.exports, __webpack_require__), t.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (u, e, t, n) => {
      if (!e) {
        var a = 1 / 0;
        for (s = 0; s < deferred.length; s++) {
          for (var [e, t, n] = deferred[s], r = !0, o = 0; o < e.length; o++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[o]))
              ? e.splice(o--, 1)
              : ((r = !1), n < a && (a = n));
          if (r) {
            deferred.splice(s--, 1);
            var i = t();
            void 0 !== i && (u = i);
          }
        }
        return u;
      }
      n = n || 0;
      for (var s = deferred.length; s > 0 && deferred[s - 1][2] > n; s--)
        deferred[s] = deferred[s - 1];
      deferred[s] = [e, t, n];
    }),
    (__webpack_require__.n = (u) => {
      var e = u && u.__esModule ? () => u.default : () => u;
      return (__webpack_require__.d(e, { a: e }), e);
    }),
    (__webpack_require__.d = (u, e) => {
      for (var t in e)
        __webpack_require__.o(e, t) &&
          !__webpack_require__.o(u, t) &&
          Object.defineProperty(u, t, { enumerable: !0, get: e[t] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (u) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (u, e) => Object.prototype.hasOwnProperty.call(u, e)),
    (__webpack_require__.r = (u) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(u, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(u, "__esModule", { value: !0 }));
    }),
    (() => {
      var u = { 877: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var n,
            a,
            [r, o, i] = t,
            s = 0;
          if (r.some((e) => 0 !== u[e])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (i) var l = i(__webpack_require__);
          }
          for (e && e(t); s < r.length; s++)
            ((a = r[s]), __webpack_require__.o(u, a) && u[a] && u[a][0](), (u[a] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [182], () => __webpack_require__(343));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
