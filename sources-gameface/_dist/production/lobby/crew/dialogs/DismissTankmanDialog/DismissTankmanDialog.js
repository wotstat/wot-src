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
      3532: (u) => {
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
      9887: (u) => {
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
      527: (u, e, t) => {
        "use strict";
        (t.r(e), t.d(e, { mouse: () => o, onResize: () => r }));
        var n = t(2472),
          a = t(1176);
        const r = (0, n.E)("clientResized"),
          i = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const o = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && (0, a.R)(!1);
          }
          function t() {
            u.enabled && (0, a.R)(!0);
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
              : (0, a.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (e, t) => (
              (e[t] = (function (e) {
                return (t) => {
                  u.listeners += 1;
                  let a = !0;
                  const r = `mouse${e}`,
                    o = i[e]((u) => t([u, "outside"]));
                  function s(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(r, s),
                    n(),
                    () => {
                      a &&
                        (o(), window.removeEventListener(r, s), (u.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(t)),
              e
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((u.enabled = !1), n());
            },
            enable() {
              ((u.enabled = !0), n());
            },
            enableOutside() {
              u.enabled && (0, a.R)(!0);
            },
            disableOutside() {
              u.enabled && (0, a.R)(!1);
            },
          });
        })();
      },
      5959: (u, e, t) => {
        "use strict";
        (t.r(e),
          t.d(e, {
            events: () => n,
            getMouseGlobalPosition: () => r,
            getSize: () => a,
            graphicsQuality: () => i,
          }));
        var n = t(527);
        function a(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(u = "px") {
          return "rem" === u
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const i = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (u, e, t) => {
        "use strict";
        function n(u) {
          viewEnv.setTrackMouseOnStage(u);
        }
        t.d(e, { R: () => n });
      },
      2472: (u, e, t) => {
        "use strict";
        function n(u) {
          return (e) => (
            engine.on(u, e),
            () => {
              engine.off(u, e);
            }
          );
        }
        t.d(e, { E: () => n });
      },
      3138: (u, e, t) => {
        "use strict";
        t.d(e, { O: () => a });
        var n = t(5959);
        const a = { view: t(7641), client: n };
      },
      3722: (u, e, t) => {
        "use strict";
        function n(u, e, t = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, t);
        }
        function a(u, e, t) {
          return `url(${n(u, e, t)})`;
        }
        (t.r(e), t.d(e, { getBgUrl: () => a, getTextureUrl: () => n }));
      },
      6112: (u, e, t) => {
        "use strict";
        t.d(e, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => a });
        var n = t(2472);
        const a = {
          onTextureFrozen: (0, n.E)("self.onTextureFrozen"),
          onTextureReady: (0, n.E)("self.onTextureReady"),
          onDomBuilt: (0, n.E)("self.onDomBuilt"),
          onLoaded: (0, n.E)("self.onLoaded"),
          onDisplayChanged: (0, n.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, n.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, n.E)("children.onAdded"),
            onLoaded: (0, n.E)("children.onLoaded"),
            onRemoved: (0, n.E)("children.onRemoved"),
            onAttached: (0, n.E)("children.onAttached"),
            onTextureReady: (0, n.E)("children.onTextureReady"),
            onRequestPosition: (0, n.E)("children.requestPosition"),
          },
        };
      },
      7641: (u, e, t) => {
        "use strict";
        (t.r(e),
          t.d(e, {
            addModelObserver: () => c,
            addPreloadTexture: () => o,
            children: () => n,
            displayStatus: () => a.W,
            displayStatusIs: () => w,
            events: () => r.U,
            extraSize: () => T,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => d,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => F,
            getSize: () => _,
            getViewGlobalPosition: () => m,
            isClientAccessible: () => g,
            isEventHandled: () => b,
            isFocused: () => h,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => A,
            sendEvent: () => i.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => p,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => x,
          }));
        var n = t(3722),
          a = t(6112),
          r = t(6538),
          i = t(8566);
        function o(u) {
          viewEnv.addPreloadTexture(u);
        }
        function s(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function l(u, e, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, n);
        }
        function c(u, e, t) {
          return viewEnv.addDataChangedCallback(u, e, t);
        }
        function E(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function _(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function A(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function m(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: B(e.x), y: B(e.y) };
        }
        function d() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
          return viewEnv.getScale();
        }
        function D(u) {
          return viewEnv.pxToRem(u);
        }
        function B(u) {
          return viewEnv.remToPx(u);
        }
        function C(u, e) {
          viewEnv.setAnimateWindow(u, e);
        }
        function h() {
          return viewEnv.isFocused();
        }
        function g() {
          return viewEnv.isClientAccessible();
        }
        function p() {
          return viewEnv.setEventHandled();
        }
        function b() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(a.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === a.W[e]), u),
            {},
          ),
          T = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          x = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : r.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        "use strict";
        t.d(e, { qP: () => l });
        const n = ["args"];
        const a = 2,
          r = 16,
          i = 32,
          o = 64,
          s = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const r = e.args,
                i = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(u);
                  for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                  return a;
                })(e, n);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, i, {
                      arguments:
                        ((a = r),
                        Object.entries(a).map(([u, e]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, i));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: u });
            var a;
          },
          l = {
            close(u) {
              s("popover" === u ? a : i);
            },
            minimize() {
              s(o);
            },
            move(u) {
              s(r, { isMouseEvent: !0, on: u });
            },
          };
      },
      5521: (u, e, t) => {
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
      1358: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        var n = t(3138);
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
      7572: (__unused_webpack_module, __webpack_exports__, __webpack_require__) => {
        "use strict";
        __webpack_require__.d(__webpack_exports__, { Z: () => __WEBPACK_DEFAULT_EXPORT__ });
        var _DataTracker__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(1358),
          _index__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(4179);
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
      4179: (u, e, t) => {
        "use strict";
        t.d(e, { Sw: () => r.Z, B0: () => s, ry: () => B, Eu: () => C });
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
        var r = t(1358);
        const i = {
            getNumberFormat: (u, e) => systemLocale.getNumberFormat(u, e),
            getRealFormat: (u, e) => systemLocale.getRealFormat(u, e),
            getTimeFormat: (u, e) => systemLocale.getTimeFormat(u, e),
            getDateFormat: (u, e) => systemLocale.getDateFormat(u, e),
            toUpperCase: (u) => systemLocale.toUpperCase(u),
            toLowerCase: (u) => systemLocale.toUpperCase(u),
          },
          o = {
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
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var A = t(5521),
          m = t(3138);
        const d = ["args"];
        function F(u, e, t, n, a, r, i) {
          try {
            var o = u[r](i),
              s = o.value;
          } catch (u) {
            return void t(u);
          }
          o.done ? e(s) : Promise.resolve(s).then(n, a);
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
                    function i(u) {
                      F(r, n, a, i, o, "next", u);
                    }
                    function o(u) {
                      F(r, n, a, i, o, "throw", u);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          C = () =>
            new Promise((u) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  u();
                });
              });
            }),
          h = (u, e) => {
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
                })(e, d);
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
          g = () => h(s.CLOSE),
          p = (u, e) => {
            u.keyCode === A.n.ESCAPE && e();
          };
        var b = t(7572);
        const v = a.instance,
          f = {
            DataTracker: r.Z,
            ViewModel: b.Z,
            ViewEventType: s,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: _,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (u) => h(s.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: g,
            sendClosePopOverEvent: () => h(s.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (u, e, t = 0) => {
              h(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, n, a = R.invalid("resId"), r) => {
              const i = m.O.view.getViewGlobalPosition(),
                o = t.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                E = o.width,
                _ = o.height,
                A = {
                  x: m.O.view.pxToRem(l) + i.x,
                  y: m.O.view.pxToRem(c) + i.y,
                  width: m.O.view.pxToRem(E),
                  height: m.O.view.pxToRem(_),
                };
              h(s.POP_OVER, {
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
            handleViewEvent: h,
            onBindingsReady: B,
            onLayoutReady: C,
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
            ClickOutsideManager: v,
            SystemLocale: i,
            UserLocale: o,
          };
        window.ViewEnvHelper = f;
      },
      2754: (u, e, t) => {
        "use strict";
        var n = t(6179),
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
        var i = t(3138);
        const o = {
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
        const c = i.O.client.getSize("rem"),
          E = c.width,
          _ = c.height,
          A = Object.assign({ width: E, height: _ }, l(E, _, o)),
          m = (0, n.createContext)(A),
          d = ["children"];
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
            })(u, d);
          const a = (0, n.useContext)(m),
            i = a.extraLarge,
            o = a.large,
            s = a.medium,
            l = a.small,
            c = a.extraSmall,
            E = a.extraLargeWidth,
            _ = a.largeWidth,
            A = a.mediumWidth,
            F = a.smallWidth,
            D = a.extraSmallWidth,
            B = a.extraLargeHeight,
            C = a.largeHeight,
            h = a.mediumHeight,
            g = a.smallHeight,
            p = a.extraSmallHeight,
            b = { extraLarge: B, large: C, medium: h, small: g, extraSmall: p };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && i) return e;
            if (t.large && o) return e;
            if (t.medium && s) return e;
            if (t.small && l) return e;
            if (t.extraSmall && c) return e;
          } else {
            if (t.extraLargeWidth && E) return r(e, t, b);
            if (t.largeWidth && _) return r(e, t, b);
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
              if (t.mediumHeight && h) return e;
              if (t.smallHeight && g) return e;
              if (t.extraSmallHeight && p) return e;
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
            const e = (0, n.useContext)(m),
              t = (0, n.useState)(e),
              r = t[0],
              s = t[1],
              c = (0, n.useCallback)((u, e) => {
                const t = i.O.view.pxToRem(u),
                  n = i.O.view.pxToRem(e);
                s(Object.assign({ width: t, height: n }, l(t, n, o)));
              }, []);
            (D(() => {
              engine.on("clientResized", c);
            }),
              (0, n.useEffect)(() => () => engine.off("clientResized", c), [c]));
            const E = (0, n.useMemo)(() => Object.assign({}, r), [r]);
            return a().createElement(m.Provider, { value: E }, u);
          });
        var C = t(6483),
          h = t.n(C),
          g = t(926),
          p = t.n(g);
        let b, v, f;
        (!(function (u) {
          ((u[(u.ExtraSmall = o.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = o.small.width)] = "Small"),
            (u[(u.Medium = o.medium.width)] = "Medium"),
            (u[(u.Large = o.large.width)] = "Large"),
            (u[(u.ExtraLarge = o.extraLarge.width)] = "ExtraLarge"));
        })(b || (b = {})),
          (function (u) {
            ((u[(u.ExtraSmall = o.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = o.small.width)] = "Small"),
              (u[(u.Medium = o.medium.width)] = "Medium"),
              (u[(u.Large = o.large.width)] = "Large"),
              (u[(u.ExtraLarge = o.extraLarge.width)] = "ExtraLarge"));
          })(v || (v = {})),
          (function (u) {
            ((u[(u.ExtraSmall = o.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = o.small.height)] = "Small"),
              (u[(u.Medium = o.medium.height)] = "Medium"),
              (u[(u.Large = o.large.height)] = "Large"),
              (u[(u.ExtraLarge = o.extraLarge.height)] = "ExtraLarge"));
          })(f || (f = {})));
        const w = () => {
            const u = (0, n.useContext)(m),
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
              i = ((u) => {
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
              mediaHeight: i,
              remScreenWidth: e,
              remScreenHeight: t,
            };
          },
          T = ["children", "className"];
        function x() {
          return (
            (x =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            x.apply(this, arguments)
          );
        }
        const S = {
            [v.ExtraSmall]: "",
            [v.Small]: p().SMALL_WIDTH,
            [v.Medium]: `${p().SMALL_WIDTH} ${p().MEDIUM_WIDTH}`,
            [v.Large]: `${p().SMALL_WIDTH} ${p().MEDIUM_WIDTH} ${p().LARGE_WIDTH}`,
            [v.ExtraLarge]: `${p().SMALL_WIDTH} ${p().MEDIUM_WIDTH} ${p().LARGE_WIDTH} ${p().EXTRA_LARGE_WIDTH}`,
          },
          k = {
            [f.ExtraSmall]: "",
            [f.Small]: p().SMALL_HEIGHT,
            [f.Medium]: `${p().SMALL_HEIGHT} ${p().MEDIUM_HEIGHT}`,
            [f.Large]: `${p().SMALL_HEIGHT} ${p().MEDIUM_HEIGHT} ${p().LARGE_HEIGHT}`,
            [f.ExtraLarge]: `${p().SMALL_HEIGHT} ${p().MEDIUM_HEIGHT} ${p().LARGE_HEIGHT} ${p().EXTRA_LARGE_HEIGHT}`,
          },
          y = {
            [b.ExtraSmall]: "",
            [b.Small]: p().SMALL,
            [b.Medium]: `${p().SMALL} ${p().MEDIUM}`,
            [b.Large]: `${p().SMALL} ${p().MEDIUM} ${p().LARGE}`,
            [b.ExtraLarge]: `${p().SMALL} ${p().MEDIUM} ${p().LARGE} ${p().EXTRA_LARGE}`,
          },
          M = (u) => {
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
              })(u, T);
            const r = w(),
              i = r.mediaWidth,
              o = r.mediaHeight,
              s = r.mediaSize;
            return a().createElement("div", x({ className: h()(t, S[i], k[o], y[s]) }, n), e);
          },
          L = ["children"];
        const O = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                a = {},
                r = Object.keys(u);
              for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
              return a;
            })(u, L);
          return a().createElement(B, null, a().createElement(M, t, e));
        };
        var N = t(493),
          H = t.n(N);
        let I;
        function P(u, e) {
          return u.replace(/\{\w+\}/g, (u) => String(e[u.slice(1, -1)]));
        }
        function W(u, e) {
          return u.replace(/(\{|%\()\w+(\}|\)s)/g, (u) => {
            const t = 0 === u.indexOf("%") ? 2 : 1;
            return String(e[u.slice(t, -t)]);
          });
        }
        function G(u) {
          return u.replace(/-/g, "_");
        }
        function $(u) {
          return u[0].toUpperCase() + u.slice(1);
        }
        !(function (u) {
          ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
        })(I || (I = {}));
        const j = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          U = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          V = (u, e, t = I.left) => u.split(e).reduce(t === I.left ? j : U, []),
          X = (() => {
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
          z = ["zh_cn", "zh_sg", "zh_tw"],
          K = (u, e = I.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return z.includes(t)
              ? X(u)
              : ((u, e = I.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = u.replace(/&nbsp;/g, " ");
                  return (V(a, /( )/, e).forEach((u) => (t = t.concat(V(u, n, I.left)))), t);
                })(u, e);
          };
        let q;
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
        })(q || (q = {}));
        var Y = t(4179);
        const Z = 60,
          Q = 3600,
          J = 86400;
        Date.now();
        const uu = () => {},
          eu = (u = 0, e, t = 0, a = uu) => {
            const r = (0, n.useState)(u),
              i = r[0],
              o = r[1];
            return (
              (0, n.useEffect)(() => {
                if (u > 0) {
                  o(u);
                  const n = Date.now(),
                    r = setInterval(
                      () => {
                        const e = u - Math.floor((Date.now() - n) / 1e3);
                        null !== t && e <= t ? (o(t), a && a(), clearInterval(r)) : o(e);
                      },
                      1e3 * (e || (u > 120 ? Z : 1)),
                    );
                  return () => {
                    clearInterval(r);
                  };
                }
                o(0);
              }, [u, e, t, a]),
              i
            );
          },
          tu = (u = 1) => {
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
          },
          nu = (u, e) => u.split(".").reduce((u, e) => u && u[e], e),
          au = (u) => u && "ArrayItem" === u.__proto__.constructor.name,
          ru = (u, e) => (u.length > 0 ? `${u}.${e}` : e),
          iu = (u) =>
            ((u, e) =>
              u.split(".").reduce((u, t) => {
                const n = nu(`${u}.${t}`, window);
                return au(n) ? e(u, t, n) : `${u}.${t}`;
              }))(u, (u, e) => `${u}.${e}.value`),
          ou = (u) => {
            const e = ((u) => {
                const e = tu(),
                  t = e.caller,
                  n = e.resId,
                  a = window.__feature && window.__feature !== t && t ? `subViews.${t}` : "";
                return { modelPrefix: a, modelPath: ru(a, u || ""), resId: n };
              })(),
              t = e.modelPrefix,
              n = u.split(".");
            if (n.length > 0) {
              const u = [n[0]];
              return (
                n.reduce((e, n) => {
                  const a = nu(ru(t, `${e}.${n}`), window);
                  return au(a) ? (u.push(a.id), `${e}.${n}.value`) : (u.push(n), `${e}.${n}`);
                }),
                u.reduce((u, e) => u + "." + e)
              );
            }
            return "";
          },
          su = Y.Sw.instance;
        let lu;
        !(function (u) {
          ((u.None = "None"), (u.Shallow = "Shallow"), (u.Deep = "Deep"));
        })(lu || (lu = {}));
        const cu = (u = "model", e = lu.Deep) => {
            const t = (0, n.useState)(0),
              a = (t[0], t[1]),
              r = (0, n.useMemo)(() => tu(), []),
              i = r.caller,
              o = r.resId,
              s = (0, n.useMemo)(
                () => (window.__feature && window.__feature !== i ? `subViews.${i}.${u}` : u),
                [i, u],
              ),
              l = (0, n.useState)(() =>
                ((u) => {
                  const e = nu(u, window);
                  for (const u in e) "function" == typeof e[u] && (e[u] = e[u].bind(e));
                  return au(e) ? e.value : e;
                })(iu(s)),
              ),
              c = l[0],
              E = l[1],
              _ = (0, n.useRef)(-1);
            return (
              D(() => {
                if (
                  ("boolean" == typeof e &&
                    ((e = e ? lu.Deep : lu.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  e !== lu.None)
                ) {
                  const t = (u) => {
                      ((u) => u && "CoherentArrayProxy" === u.__proto__.constructor.name)(u) &&
                      e === lu.Deep
                        ? (u === c && a((u) => u + 1), E(u))
                        : E(Object.assign([], u));
                    },
                    n = ou(u);
                  _.current = su.addCallback(n, t, o, e === lu.Deep);
                }
              }),
              (0, n.useEffect)(() => {
                if (e !== lu.None)
                  return () => {
                    su.removeCallback(_.current, o);
                  };
              }, [o, e]),
              c
            );
          },
          Eu = (Y.Sw.instance, eu);
        var _u = t(5521);
        const Au = (u) => {
          console.error(u.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function mu(u = _u.n.NONE, e = Au, t = !1) {
          (0, n.useEffect)(() => {
            if (u !== _u.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === u) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), e(n), t && n.stopPropagation());
              }
            }
          }, [e, u, t]);
        }
        const du = /<link.*?>/g,
          Fu = /\.\.\//g,
          Du = /<script.*?>/g,
          Bu = "default.css",
          Cu = (u) => {
            const e = u.match(Fu);
            return e && e.join("");
          },
          hu = () => {
            for (
              var u = 0, e = Array.from(document.head.querySelectorAll('link[rel="stylesheet"]'));
              u < e.length;
              u++
            ) {
              const t = e[u];
              if (!t.href.includes(Bu)) return t.href;
            }
            return "";
          },
          gu = (u, e) => {
            const t = hu(),
              n = Cu(t);
            let a,
              r = u;
            for (; null !== (a = Du.exec(u));) {
              const u = a[0].match(/<script (defer|defer="defer") src="(.*?)">/);
              if (u) {
                const t = n + u[2].replace(Fu, "");
                ((r = r.replace(u[2], t)),
                  (r = r.replace('<div id="root"', `<div data-root-id=${e} id="root"`)));
              }
            }
            return r;
          },
          pu = "SubView_base_df",
          bu = "subViews.onChanged",
          vu = (() => {
            const u = [];
            let e = !1;
            const t = () => {
              if (!u.length) return void (e = !1);
              const n = u.shift();
              n && ((e = !0), n().then(() => t()));
            };
            return {
              add: (n) => {
                (u.push(n), e || t());
              },
            };
          })(),
          fu = (0, n.memo)(({ id: u, fallback: e, onLoadCallback: t, mixClass: r }) => {
            const i = (0, n.useState)(""),
              o = i[0],
              s = i[1],
              l = (0, n.useMemo)(() => ({ __html: gu(o, u) }), [o, u]),
              c = (0, n.useMemo)(() => window.subViews.addChildChangedCallback(u), [u]),
              E = (0, n.useState)(!1),
              _ = E[0],
              A = E[1],
              m = (0, n.useCallback)(
                (u) => {
                  u.includes(c) &&
                    (A(!0), engine.off(bu, m), window.subViews.removeChildChangedCallback(c));
                },
                [c],
              ),
              d = (0, n.useCallback)((u) => {
                vu.add(
                  () =>
                    new Promise((e) => {
                      s(u);
                      const t = new MutationObserver(() => {
                          (t.disconnect(), e());
                        }),
                        n = document.getElementById("root");
                      n && t.observe(n, { childList: !0 });
                    }),
                );
              }, []);
            ((0, n.useEffect)(() => {
              if (window.subViews.ids().includes(u)) {
                const e = window.subViews.get(u),
                  t = e.path;
                let n;
                if ((n = t.split("/").pop()))
                  return (
                    (n = n.split(".")[0]),
                    (window.subViews[n] = Object.assign({ id: u }, e)),
                    engine.on(`subView:inject->${n}`, d),
                    (({ path: u, name: e }) => {
                      const t = new XMLHttpRequest();
                      ((t.onreadystatechange = () => {
                        4 === t.readyState &&
                          (200 === t.status
                            ? (0, Y.Eu)().then(() => {
                                (console.info(`Sub view ${e} loaded: ${u}`),
                                  engine.TriggerEvent(`subView:inject->${e}`, t.responseText));
                              })
                            : console.error(`subView: status: ${t.status} - can't get bundle`));
                      }),
                        t.open("GET", u),
                        t.send());
                    })({ name: n, path: t }),
                    () => {
                      (n && window.subViews[n] && delete window.subViews[n],
                        engine.trigger("subView:destroy", { viewName: n, viewId: u }),
                        window.__dataTracker &&
                          window.__dataTracker.clearViewCallbacks &&
                          window.__dataTracker.clearViewCallbacks(u),
                        engine.off(`subView:inject->${n}`, d),
                        console.info(`Sub view ${n} is destroyed: ${t}`));
                    }
                  );
                console.error("subView: can't get View component name");
              } else engine.on(bu, m);
            }, [m, d, u, _]),
              (0, n.useEffect)(
                () => () => {
                  o &&
                    ((u) => {
                      const e = Cu(hu());
                      let t;
                      for (; null !== (t = du.exec(u));) {
                        const u = t[0].match(/href="(.*?)"/);
                        if (u) {
                          const t = e + u[1].replace(Fu, ""),
                            n = document.head.querySelector(`[href="${t}"]`);
                          n && document.head.removeChild(n);
                        }
                      }
                    })(o);
                },
                [o],
              ));
            const F = h()(pu, r);
            if (o) {
              let e;
              return (
                (e = document.getElementById("root")) && e.setAttribute("id", "bugSubView"),
                ((u) => {
                  let e;
                  const t = hu(),
                    n = Cu(t);
                  for (; null !== (e = du.exec(u));) {
                    const u = e[0].match(/href="(.*?)"/);
                    if (u && !u[1].includes(Bu) && n) {
                      const e = n + u[1].replace(Fu, ""),
                        t = document.createElement("link");
                      ((t.href = e), (t.rel = "stylesheet"), document.head.appendChild(t));
                    }
                  }
                })(o),
                t && t(u),
                a().createElement("div", { className: F, dangerouslySetInnerHTML: l })
              );
            }
            return e
              ? a().createElement("div", { className: F }, a().createElement(e, null))
              : null;
          });
        function wu(u) {
          engine.call("PlaySound", u);
        }
        const Tu = {
            playHighlight() {
              wu("highlight");
            },
            playClick() {
              wu("play");
            },
            playYes() {
              wu("yes1");
            },
          },
          xu = {
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
        let Su, ku;
        (!(function (u) {
          ((u.main = "main"),
            (u.primary = "primary"),
            (u.primaryGreen = "primaryGreen"),
            (u.primaryRed = "primaryRed"),
            (u.secondary = "secondary"),
            (u.ghost = "ghost"));
        })(Su || (Su = {})),
          (function (u) {
            ((u.extraSmall = "extraSmall"), (u.small = "small"), (u.medium = "medium"));
          })(ku || (ku = {})));
        const yu = ({
          children: u,
          size: e,
          isFocused: t,
          type: r,
          disabled: i,
          mixClass: o,
          soundHover: s,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: E,
          onMouseDown: _,
          onMouseUp: A,
          onMouseLeave: m,
          onClick: d,
        }) => {
          const F = (0, n.useRef)(null),
            D = (0, n.useState)(t),
            B = D[0],
            C = D[1],
            g = (0, n.useState)(!1),
            p = g[0],
            b = g[1],
            v = (0, n.useState)(!1),
            f = v[0],
            w = v[1],
            T = (0, n.useCallback)(() => {
              i || (F.current && (F.current.focus(), C(!0)));
            }, [i]),
            x = (0, n.useCallback)(
              (u) => {
                B && null !== F.current && !F.current.contains(u.target) && C(!1);
              },
              [B],
            ),
            S = (0, n.useCallback)(
              (u) => {
                i || (d && d(u));
              },
              [i, d],
            ),
            k = (0, n.useCallback)(
              (u) => {
                i || (null !== s && wu(s), c && c(u), w(!0));
              },
              [i, s, c],
            ),
            y = (0, n.useCallback)(
              (u) => {
                E && E(u);
              },
              [E],
            ),
            M = (0, n.useCallback)(
              (u) => {
                i || (A && A(u), b(!1));
              },
              [i, A],
            ),
            L = (0, n.useCallback)(
              (u) => {
                i || (null !== l && wu(l), _ && _(u), t && T(), b(!0));
              },
              [i, l, _, T, t],
            ),
            O = (0, n.useCallback)(
              (u) => {
                i || (m && m(u), b(!1));
              },
              [i, m],
            ),
            N = h()(
              xu.base,
              xu[`base__${r}`],
              {
                [xu.base__disabled]: i,
                [xu[`base__${e}`]]: e,
                [xu.base__focus]: B,
                [xu.base__highlightActive]: p,
                [xu.base__firstHover]: f,
              },
              o,
            ),
            H = h()(xu.state, xu.state__default);
          return (
            (0, n.useEffect)(
              () => (
                document.addEventListener("mousedown", x),
                () => {
                  document.removeEventListener("mousedown", x);
                }
              ),
              [x],
            ),
            (0, n.useEffect)(() => {
              C(t);
            }, [t]),
            a().createElement(
              "div",
              {
                ref: F,
                className: N,
                onMouseEnter: k,
                onMouseMove: y,
                onMouseUp: M,
                onMouseDown: L,
                onMouseLeave: O,
                onClick: S,
              },
              r !== Su.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: xu.back }),
                  a().createElement("span", { className: xu.texture }),
                ),
              a().createElement(
                "span",
                { className: H },
                a().createElement("span", { className: xu.stateDisabled }),
                a().createElement("span", { className: xu.stateHighlightHover }),
                a().createElement("span", { className: xu.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: xu.content, lang: R.strings.settings.LANGUAGE_CODE() },
                u,
              ),
            )
          );
        };
        yu.defaultProps = {
          type: Su.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Mu = (0, n.memo)(yu),
          Lu = [
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
        function Ru(u) {
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
        const Ou = (u, e, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: Y.B0.TOOLTIP,
                  contentID: u,
                  decoratorID: e,
                  targetID: n,
                },
                t,
              ),
            );
          },
          Nu = (u) => {
            let e = u.children,
              t = u.contentId,
              a = u.args,
              r = u.onMouseEnter,
              i = u.onMouseLeave,
              o = u.onMouseDown,
              s = u.onClick,
              l = u.ignoreShowDelay,
              c = void 0 !== l && l,
              E = u.ignoreMouseClick,
              _ = void 0 !== E && E,
              A = u.decoratorId,
              m = void 0 === A ? 0 : A,
              d = u.isEnabled,
              F = void 0 === d || d,
              D = u.targetId,
              B = void 0 === D ? 0 : D,
              C = u.onShow,
              h = u.onHide,
              g = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, Lu);
            const p = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              b = (0, n.useMemo)(() => B || tu().resId, [B]),
              v = (0, n.useCallback)(() => {
                (p.current.isVisible && p.current.timeoutId) ||
                  (Ou(t, m, { isMouseEvent: !0, on: !0, arguments: Ru(a) }, b),
                  C && C(),
                  (p.current.isVisible = !0));
              }, [t, m, a, b, C]),
              f = (0, n.useCallback)(() => {
                if (p.current.isVisible || p.current.timeoutId) {
                  const u = p.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (p.current.timeoutId = 0)),
                    Ou(t, m, { on: !1 }, b),
                    p.current.isVisible && h && h(),
                    (p.current.isVisible = !1));
                }
              }, [t, m, b, h]),
              w = (0, n.useCallback)((u) => {
                p.current.isVisible &&
                  ((p.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (p.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(p.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const u = p.current.hideTimerId;
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
                        ((T = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((p.current.timeoutId = window.setTimeout(v, c ? 100 : 400)),
                            r && r(u),
                            T && T(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (f(), null == i || i(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === _ && f(), null == s || s(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === _ && f(), null == o || o(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    g,
                  ),
                )
              : e;
            var T;
          },
          Hu = ["children", "body", "header", "note", "alert", "args"];
        function Iu() {
          return (
            (Iu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Iu.apply(this, arguments)
          );
        }
        const Pu = R.views.common.tooltip_window.simple_tooltip_content,
          Wu = (u) => {
            let e = u.children,
              t = u.body,
              r = u.header,
              i = u.note,
              o = u.alert,
              s = u.args,
              l = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, Hu);
            const c = (0, n.useMemo)(() => {
              const u = Object.assign({}, s, { body: t, header: r, note: i, alert: o });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [o, t, r, i, s]);
            return a().createElement(
              Nu,
              Iu(
                {
                  contentId:
                    ((E = null == s ? void 0 : s.hasHtmlContent),
                    E ? Pu.SimpleTooltipHtmlContent("resId") : Pu.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              e,
            );
            var E;
          },
          Gu = "TextOverflow_base_3b",
          $u = ({ content: u, classMix: e }) => {
            const t = (0, n.useRef)(null),
              r = (0, n.useState)(!0),
              i = r[0],
              o = r[1];
            return (
              (0, n.useEffect)(() =>
                ((u) => {
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
                })(() => {
                  const u = t.current;
                  u && u.offsetWidth >= u.scrollWidth && o(!1);
                }),
              ),
              a().createElement(
                Wu,
                { isEnabled: i, body: u },
                a().createElement("div", { ref: t, className: h()(Gu, e) }, u),
              )
            );
          };
        let ju;
        !(function (u) {
          ((u.backport = "backport"), (u.normal = "normal"), (u.absent = "absent"));
        })(ju || (ju = {}));
        const Uu = "DialogTemplateButton_base_0b",
          Vu = "DialogTemplateButton_label_83",
          Xu = "DialogTemplateButton_label__noTooltip_14",
          zu = (0, n.memo)(
            ({
              onClick: u,
              isFocused: e,
              buttonID: t,
              isDisabled: r,
              label: i,
              tooltip: o,
              type: s,
            }) => {
              const l = (0, n.useCallback)(() => {
                  u({ buttonID: t });
                }, [u, t]),
                c = (0, n.useCallback)(
                  (u) => {
                    u.altKey || !e || r || l();
                  },
                  [e, r, l],
                );
              mu(_u.n.ENTER, c);
              const E = (0, n.useMemo)(() => {
                  return (
                    (u = o.type),
                    (e = { buttonID: t }),
                    {
                      isEnabled: u !== ju.absent,
                      args: e,
                      contentId: R.views.dialogs.common.DialogTemplateGenericTooltip("resId"),
                      decoratorId:
                        u === ju.normal
                          ? R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId")
                          : void 0,
                      ignoreShowDelay: u === ju.backport,
                      ignoreMouseClick: !0,
                    }
                  );
                  var u, e;
                }, [o.type, t]),
                _ = h()(Vu, o.type !== ju.absent && Xu);
              return a().createElement(
                Nu,
                E,
                a().createElement(
                  "div",
                  { className: Uu },
                  a().createElement(
                    Mu,
                    { size: ku.medium, type: s, disabled: r, onClick: l, isFocused: e },
                    a().createElement($u, { classMix: _, content: i || "" }),
                  ),
                ),
              );
            },
          ),
          Ku = "DialogTemplateButtonList_base_8e";
        function qu() {
          return (
            (qu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            qu.apply(this, arguments)
          );
        }
        const Yu = (0, n.memo)(() => {
            const u = cu("model").onButtonClicked,
              e = cu("model.focus"),
              t = e.focusedIndex,
              r = e.onTabPressed,
              i = cu("model.buttons"),
              o = (0, n.useCallback)(
                (u) => {
                  r({ shift: u.shiftKey });
                },
                [r],
              );
            return (
              mu(_u.n.TAB, o),
              a().createElement(
                "div",
                { className: Ku },
                i.map(({ value: e }, n) =>
                  a().createElement(zu, qu({ key: e.buttonID, isFocused: n === t, onClick: u }, e)),
                ),
              )
            );
          }),
          Zu = "DialogTemplateWrapper_base_f7",
          Qu = "DialogTemplateWrapper_base__hidden_5f",
          Ju = "DialogTemplateWrapper_subView_30";
        function ue() {
          return (
            (ue =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            ue.apply(this, arguments)
          );
        }
        const ee = (0, n.memo)(({ Template: u }) => {
          const e = cu("model", lu.None),
            t = e.onCloseClicked,
            r = e.placeHolders,
            i = e.background,
            o = e.dimmerAlpha,
            s = e.displayFlags;
          (0, n.useEffect)(() => {
            const u = document.getElementById("root");
            u && u.setAttribute("id", "stubDialogTemplate");
          }, []);
          const l = s.map(({ value: u }) => u),
            c = (0, n.useRef)(r.map(({ value: u }) => u.resourceID)),
            E = (0, n.useState)(0 !== c.current.length),
            _ = E[0],
            A = E[1],
            m = (0, n.useCallback)(
              (u = "default") => {
                t({ reason: u });
              },
              [t],
            ),
            d = (0, n.useCallback)(() => {
              m("escape");
            }, [m]);
          var F;
          ((F = d), mu(_u.n.ESCAPE, F));
          const D = (0, n.useCallback)((u) => {
              const e = c.current,
                t = e.indexOf(u);
              t > -1 && (e.splice(t, 1), 0 === e.length && A(!1));
            }, []),
            C = (0, n.useMemo)(() => {
              const u = { backgroundColor: `rgba(19, 18, 16, ${o})` };
              return (i && (u.backgroundImage = `url(${i})`), u);
            }, [i, o]),
            g = (0, n.useMemo)(
              () =>
                r.reduce(
                  (u, { value: e }) => (
                    (u[e.placeHolder] = a().createElement(fu, {
                      key: e.placeHolder,
                      id: e.resourceID,
                      mixClass: Ju,
                      onLoadCallback: D,
                    })),
                    u
                  ),
                  {},
                ),
              [D, r],
            ),
            p = h()(Zu, _ && Qu);
          return a().createElement(
            B,
            null,
            a().createElement(
              "div",
              { className: p, style: C },
              a().createElement(
                u,
                ue(
                  {
                    onClose: m,
                    buttons: a().createElement(Yu, null),
                    displayFlags: l,
                    isShown: !_,
                  },
                  g,
                ),
              ),
            ),
          );
        });
        var te = t(3403);
        const ne = {
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
          ae = [
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
        function re() {
          return (
            (re =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            re.apply(this, arguments)
          );
        }
        class ie extends a().PureComponent {
          constructor(...u) {
            (super(...u),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (u) => (e) => {
                (u && u(e),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && wu(this.props.soundHover));
              }),
              (this._onMouseLeave = (u) => (e) => {
                (u && u(e), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (u) => (e) => {
                (u && u(e),
                  this.setState({ click: !0 }),
                  this.props.soundClick && wu(this.props.soundClick));
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
              i = u.type,
              o = u.classNames,
              s = u.onMouseEnter,
              l = u.onMouseLeave,
              c = u.onMouseDown,
              E = u.onMouseUp,
              _ =
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
                })(u, ae)),
              A = h()(ne.base, ne[`base__${i}`], ne[`base__${r}`], null == o ? void 0 : o.base),
              m = h()(ne.icon, ne[`icon__${i}`], ne[`icon__${r}`], null == o ? void 0 : o.icon),
              d = h()(ne.glow, null == o ? void 0 : o.glow),
              F = h()(ne.caption, ne[`caption__${i}`], null == o ? void 0 : o.caption),
              D = h()(ne.goto, null == o ? void 0 : o.goto);
            return a().createElement(
              "div",
              re(
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
                _,
              ),
              "info" !== i && a().createElement("div", { className: ne.shine }),
              a().createElement(
                "div",
                { className: m },
                a().createElement("div", { className: d }),
              ),
              a().createElement("div", { className: F }, e),
              n && a().createElement("div", { className: D }, n),
            );
          }
        }
        let oe;
        ((ie.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        }),
          (function (u) {
            ((u.responsiveHeader = "responsiveHeader"),
              (u.responsiveClosePosition = "responsiveClosePosition"),
              (u.disableResponsiveContentPosition = "disableResponsiveContentPosition"));
          })(oe || (oe = {})));
        function se(u, e, t) {
          const a = (0, n.useContext)(m);
          let r = Object.entries(a).filter(([u, e]) => !0 === e && u in s);
          return (
            t && (r = r.filter((u) => t.includes(u[0]))),
            u.reduce((u, t) => {
              const n = r.map((u) =>
                h()(e[((u, e) => u + "__" + e)(t, u[0])], e[((u, e) => u + $(e))(t, u[0])]),
              );
              return ((u[t] = h()(e[t], ...n)), u);
            }, {})
          );
        }
        const le = {
            base: "DefaultDialogTemplate_base_d2",
            topRight: "DefaultDialogTemplate_topRight_eb",
            center: "DefaultDialogTemplate_center_b4",
            center__shown: "DefaultDialogTemplate_center__shown_e1",
            windowIn: "DefaultDialogTemplate_windowIn_3b",
            center__withIcon: "DefaultDialogTemplate_center__withIcon_f9",
            base__extraSmallHeight: "DefaultDialogTemplate_base__extraSmallHeight_f5",
            center__responsive: "DefaultDialogTemplate_center__responsive_21",
            base__smallHeight: "DefaultDialogTemplate_base__smallHeight_52",
            icon: "DefaultDialogTemplate_icon_36",
            icon__responsive: "DefaultDialogTemplate_icon__responsive_e0",
            title: "DefaultDialogTemplate_title_c6",
            title__responsive: "DefaultDialogTemplate_title__responsive_6e",
            content: "DefaultDialogTemplate_content_22",
            footer: "DefaultDialogTemplate_footer_4e",
            buttons: "DefaultDialogTemplate_buttons_f7",
            divider: "DefaultDialogTemplate_divider_d5",
            divider__noContent: "DefaultDialogTemplate_divider__noContent_3f",
            divider__noFooter: "DefaultDialogTemplate_divider__noFooter_10",
            closeBtn: "DefaultDialogTemplate_closeBtn_5e",
            closeBtn__responsive: "DefaultDialogTemplate_closeBtn__responsive_49",
          },
          ce = (0, n.memo)(
            ({
              isShown: u = !0,
              classMix: e,
              onClose: t,
              icon: r,
              topRight: i,
              title: o,
              content: s,
              buttons: l,
              footer: c,
              displayFlags: E,
              classNames: _,
            }) => {
              const A = ((u, e) =>
                  Object.keys(e).reduce((e, t) => ((e[t] = u.includes(t)), e), {}))(E, oe),
                m = A.responsiveHeader,
                d = A.responsiveClosePosition,
                F = A.disableResponsiveContentPosition,
                D = se(["base"], le),
                B = (0, n.useCallback)(() => {
                  t && t();
                }, [t]),
                C = h()(D.base, e),
                g = h()(
                  le.center,
                  r && le.center__withIcon,
                  u && le.center__shown,
                  !F && le.center__responsive,
                  null == _ ? void 0 : _.center,
                ),
                p = h()(le.icon, m && le.icon__responsive),
                b = h()(le.title, m && le.title__responsive),
                v = h()(le.closeBtn, d && le.closeBtn__responsive),
                f = h()(
                  le.divider,
                  !s && le.divider__noContent,
                  !c && le.divider__noFooter,
                  null == _ ? void 0 : _.divider,
                );
              return a().createElement(
                "div",
                { className: C },
                a().createElement(
                  "div",
                  { className: le.topRight },
                  i,
                  a().createElement(
                    "div",
                    { className: v },
                    a().createElement(ie, {
                      caption: R.strings.menu.viewHeader.closeBtn.label(),
                      type: "close",
                      side: "right",
                      onClick: B,
                    }),
                  ),
                ),
                a().createElement(
                  "div",
                  { className: g },
                  r && a().createElement("div", { className: p }, r),
                  o && a().createElement("div", { className: b }, o),
                  s && a().createElement("div", { className: le.content }, s),
                  a().createElement("div", { className: f }),
                  c && a().createElement("div", { className: le.footer }, c),
                  l && a().createElement("div", { className: le.buttons }, l),
                ),
              );
            },
          );
        function Ee() {}
        function _e() {
          return !1;
        }
        console.log;
        var Ae = t(9174);
        function me(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return de(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return de(u, e);
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
        function de(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, n = new Array(e); t < e; t++) n[t] = u[t];
          return n;
        }
        const Fe = (u) => (0 === u ? window : window.subViews.get(u));
        function De(u, e) {
          return Array.isArray(u)
            ? u.map(e)
            : u.map((u, t, n) => e(null == u ? void 0 : u.value, t, n));
        }
        const Be = (u) =>
            null !== u && "object" == typeof u
              ? "CoherentArrayProxy" === u.constructor.name
                ? De(u, (u) => ("object" == typeof u ? Be(u) : u))
                : Array.isArray(u)
                  ? u.map((u) => ("object" == typeof u ? Be(u) : u))
                  : Object.fromEntries(
                      Object.entries(u).map(([u, e]) => [u, "object" == typeof e ? Be(e) : e]),
                    )
              : u,
          Ce = (u) => Be(u);
        var he = t(3946);
        const ge = ((u, e) => {
            const t = (0, n.createContext)({});
            return [
              function ({ mode: r = "real", options: o, children: s, mocks: l }) {
                const c = (0, n.useRef)([]),
                  E = (t, n, a) => {
                    var r;
                    const o = (function ({
                        initializer: u = !0,
                        rootId: e = 0,
                        getRoot: t = Fe,
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
                        const o = (u) => {
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
                              l = i.O.view.addModelObserver(s, e, !0);
                            return (a.set(l, t), u && t(o(r)), l);
                          },
                          readByPath: o,
                          createCallback: (u, e) => {
                            const t = o(e);
                            return (...e) => {
                              t(u(...e));
                            };
                          },
                          createCallbackNoArgs: (u) => {
                            const e = o(u);
                            return () => {
                              e();
                            };
                          },
                          dispose: function () {
                            for (var u, t = me(a.keys()); !(u = t()).done;) r(u.value, e);
                          },
                          unsubscribe: r,
                        };
                      })(n),
                      s =
                        "real" === t
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (r = null == a ? void 0 : a.getter) ? r : () => {},
                            }),
                      l = (u) =>
                        "mocks" === t ? (null == a ? void 0 : a.getter(u)) : s.readByPath(u),
                      E = (u) => c.current.push(u),
                      _ = u({
                        mode: t,
                        readByPath: l,
                        externalModel: s,
                        observableModel: {
                          array: (u, e) => {
                            const n = null != e ? e : l(u),
                              a = Ae.LO.box(n, { equals: _e });
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, Ae.aD)((u) => a.set(u)),
                                  u,
                                ),
                              a
                            );
                          },
                          object: (u, e) => {
                            const n = null != e ? e : l(u),
                              a = Ae.LO.box(n, { equals: _e });
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, Ae.aD)((u) => a.set(u)),
                                  u,
                                ),
                              a
                            );
                          },
                          primitives: (u, e) => {
                            const n = l(e);
                            if (Array.isArray(u)) {
                              const a = u.reduce((u, e) => ((u[e] = Ae.LO.box(n[e], {})), u), {});
                              return (
                                "real" === t &&
                                  s.subscribe(
                                    (0, Ae.aD)((e) => {
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
                                i = r.reduce((u, [e, t]) => ((u[t] = Ae.LO.box(n[e], {})), u), {});
                              return (
                                "real" === t &&
                                  s.subscribe(
                                    (0, Ae.aD)((u) => {
                                      r.forEach(([e, t]) => {
                                        i[t].set(u[e]);
                                      });
                                    }),
                                    e,
                                  ),
                                i
                              );
                            }
                          },
                        },
                        cleanup: E,
                      }),
                      A = { mode: t, model: _, externalModel: s, cleanup: E };
                    return {
                      model: _,
                      controls: "mocks" === t && a ? a.controls(A) : e(A),
                      externalModel: s,
                      mode: t,
                    };
                  },
                  _ = (0, n.useRef)(!1),
                  A = (0, n.useState)(r),
                  m = A[0],
                  d = A[1],
                  F = (0, n.useState)(() => E(r, o, l)),
                  D = F[0],
                  B = F[1];
                return (
                  (0, n.useEffect)(() => {
                    _.current ? B(E(m, o, l)) : (_.current = !0);
                  }, [l, m, o]),
                  (0, n.useEffect)(() => {
                    d(r);
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
          })(({ observableModel: u }) => {
            const e = Object.assign(
                {},
                u.primitives([
                  "isRecoveryPossible",
                  "isLimitReached",
                  "dismissPeriod",
                  "perkName",
                  "perkLevel",
                  "trainingLevel",
                ]),
                { tankman: u.array("tankman"), replacedTankman: u.array("replacedTankman") },
              ),
              t = (0, he.Om)(() => Ce(e.tankman.get()), { equals: _e }),
              n = (0, he.Om)(() => Ce(e.replacedTankman.get()), { equals: _e }),
              a = (0, he.Om)(() => Ce(e.replacedTankman.get()).tankmanVehicleInfo, { equals: _e });
            return Object.assign({}, e, {
              computes: { getTankman: t, getReplacedTankman: n, getReplacedTankmanVehicleInfo: a },
            });
          }, Ee),
          pe = ge[0],
          be = ge[1];
        let ve, fe, we, Te, xe;
        (!(function (u) {
          ((u.Any = "any"),
            (u.Commander = "commander"),
            (u.Radioman = "radioman"),
            (u.Driver = "driver"),
            (u.Gunner = "gunner"),
            (u.Loader = "loader"));
        })(ve || (ve = {})),
          (function (u) {
            ((u.InBarracks = "in_barracks"), (u.InTank = "in_tank"), (u.Dismissed = "dismissed"));
          })(fe || (fe = {})),
          (function (u) {
            ((u.Tankman = "tankman"),
              (u.Recruit = "recruit"),
              (u.Dismissed = "dismissed"),
              (u.Unique = "unique"));
          })(we || (we = {})),
          (function (u) {
            ((u.Default = "default"), (u.Selected = "selected"), (u.Disabled = "disabled"));
          })(Te || (Te = {})),
          (function (u) {
            ((u.IsLockCrew = "isLockCrew"), (u.TankmanHasRole = "tankmanHasRole"));
          })(xe || (xe = {})));
        const Se = R.strings.common.percentValue(),
          ke = (u) => W(Se, { value: u });
        let ye;
        !(function (u) {
          ((u.Objective = "objective"), (u.Possessive = "possessive"));
        })(ye || (ye = {}));
        (R.strings.crew.filterPanel.counter.reset.header(),
          R.strings.crew.filterPanel.counter.reset.body(),
          R.strings.crew.filterPanel.counterMultySelect.reset.header(),
          R.strings.crew.filterPanel.counterMultySelect.reset.body());
        let Me;
        !(function (u) {
          ((u.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (u.SHOP_INFO = "shop_info"),
            (u.RUDY = "rudy"));
        })(Me || (Me = {}));
        function Le(u, e, t, n) {
          let a,
            r = !1,
            i = 0;
          function o() {
            a && clearTimeout(a);
          }
          function s(...s) {
            const l = this,
              c = Date.now() - i;
            function E() {
              ((i = Date.now()), t.apply(l, s));
            }
            r ||
              (n && !a && E(),
              o(),
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
              (o(), (r = !0));
            }),
            s
          );
        }
        function Re(u, e, t) {
          const a = (0, n.useMemo)(
            () =>
              (function (u, e, t) {
                return void 0 === t ? Le(u, e, !1) : Le(u, t, !1 !== e);
              })(t, u),
            e,
          );
          return ((0, n.useEffect)(() => a.cancel, [a]), a);
        }
        const Oe = {
          base: "TankmanIcon_base_f9",
          base__big: "TankmanIcon_base__big_98",
          base__small: "TankmanIcon_base__small_b2",
          base__barracks: "TankmanIcon_base__barracks_62",
          base__special: "TankmanIcon_base__special_3f",
          base__c_204x256: "TankmanIcon_base__c_204x256_97",
          innerShadow: "TankmanIcon_innerShadow_c6",
        };
        let Ne;
        !(function (u) {
          ((u.c158x118 = "big"),
            (u.c100x60 = "small"),
            (u.c100x60Barracks = "barracks"),
            (u.c444x300 = "special"),
            (u.c204x256 = "c_204x256"));
        })(Ne || (Ne = {}));
        const He = R.images.gui.maps.icons.tankmen.icons,
          Ie = (0, n.memo)(({ name: u, size: e = Ne.c100x60, className: t, isSkin: n = !1 }) => {
            const r = (n ? He.$dyn(e).$dyn("crewSkins") : He.$dyn(e)).$dyn(G(u)),
              i = e === Ne.c204x256;
            return a().createElement(
              "div",
              {
                style: { backgroundImage: `url(${r})` },
                className: h()(Oe.base, Oe[`base__${e}`], t),
              },
              i && a().createElement("div", { className: Oe.innerShadow }),
            );
          }),
          Pe = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          We = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const Ge = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          $e = (u) =>
            Ge
              ? `${u}`
              : (function (u) {
                  let e = "";
                  for (let t = We.length - 1; t >= 0; t--)
                    for (; u >= We[t];) ((e += Pe[t]), (u -= We[t]));
                  return e;
                })(u),
          je = {
            base: "TankName_base_f1",
            base__sizeMedium: "TankName_base__sizeMedium_3a",
            base__sizBig: "TankName_base__sizBig_a9",
            base__typeWhite: "TankName_base__typeWhite_32",
            base__typeWhiteSpanish: "TankName_base__typeWhiteSpanish_e2",
            base__typeColored: "TankName_base__typeColored_bc",
            level: "TankName_level_bb",
            type: "TankName_type_3c",
            type__elite: "TankName_type__elite_cc",
            base__sizeBig: "TankName_base__sizeBig_2b",
            name: "TankName_name_56",
            base__tagPremiumIGR: "TankName_base__tagPremiumIGR_26",
            premiumIGR: "TankName_premiumIGR_25",
          };
        let Ue, Ve;
        (!(function (u) {
          ((u.extraSmall = "extraSmall"), (u.medium = "medium"), (u.big = "big"));
        })(Ue || (Ue = {})),
          (function (u) {
            ((u.colored = "colored"), (u.white = "white"), (u.whiteSpanish = "whiteSpanish"));
          })(Ve || (Ve = {})));
        const Xe = ({
            isElite: u,
            vehicleName: e,
            vehicleShortName: t,
            vehicleType: n,
            vehicleLvl: r,
            tags: i,
            isPremiumIGR: o,
            size: s = Ue.extraSmall,
            type: l = Ve.colored,
            className: c,
            classNames: E,
            isShortName: _ = !1,
          }) => {
            const A = `${G(n)}${u ? "_elite" : ""}`,
              m = R.images.gui.maps.icons.vehicleTypes.big.$dyn(A);
            return a().createElement(
              "div",
              {
                className: h()(
                  je.base,
                  je[`base__size${$(s)}`],
                  je[`base__type${$(l)}`],
                  i && De(i, (u) => je[`base__tag${$(u)}`]),
                  c,
                ),
              },
              a().createElement(
                "div",
                { className: h()(je.level, null == E ? void 0 : E.level) },
                $e(r),
              ),
              a().createElement("div", {
                className: h()(je.type, u && je.type__elite, null == E ? void 0 : E.typeIcon),
                style: { backgroundImage: `url(${m})` },
              }),
              o && a().createElement("div", { className: je.premiumIGR }),
              a().createElement(
                "div",
                { className: h()(je.name, null == E ? void 0 : E.name) },
                _ ? t : e,
              ),
            );
          },
          ze = "Content_base_48",
          Ke = "Content_name_7b",
          qe = "Content_specializationInfo_ac",
          Ye = "Content_recruitLabel_17",
          Ze = "Content_levelPercentage_f1",
          Qe = "Content_levelPercentage__red_c9";
        function Je() {
          return (
            (Je =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Je.apply(this, arguments)
          );
        }
        const ut = ({
            fullUserName: u,
            isRecruit: e,
            tankmanVehicleInfo: t,
            specializationLevel: r,
            hasSpecializationLevelPenalty: i,
            className: o,
          }) => {
            const s = (0, n.useMemo)(() => ke(Math.floor(r)), [r]);
            return a().createElement(
              "div",
              { className: h()(ze, o) },
              a().createElement("div", { className: Ke }, u),
              a().createElement(
                "div",
                { className: qe },
                e
                  ? a().createElement("div", { className: Ye }, R.strings.crew.tankman.recruit())
                  : a().createElement(
                      a().Fragment,
                      null,
                      a().createElement(Xe, Je({}, t, { type: Ve.whiteSpanish, isShortName: !0 })),
                      a().createElement("div", { className: h()(Ze, i && Qe) }, `(${s})`),
                    ),
              ),
            );
          },
          et = (0, n.memo)(({ duration: u }) => {
            const e =
              u >= 0
                ? (t = (function (u = 0) {
                    let e = u;
                    const t = Math.trunc(e / J);
                    e -= t * J;
                    const n = Math.trunc(e / Q);
                    e -= n * Q;
                    const a = Math.trunc(e / Z);
                    return ((e -= a * Z), { days: t, hours: n, minutes: a, seconds: e });
                  })(u)).days > 0
                  ? P(R.strings.common.duration.days(), { days: t.days })
                  : t.hours > 0
                    ? P(R.strings.common.duration.hours(), { hours: t.hours })
                    : t.minutes > 0
                      ? P(R.strings.common.duration.minutes(), { minutes: t.minutes })
                      : P(R.strings.common.duration.seconds(), { seconds: t.seconds })
                : R.strings.common.duration.unlimited();
            var t;
            return a().createElement("span", null, e);
          }),
          tt = a().memo(function ({ duration: u, className: e }) {
            const t = Eu(u, 1);
            return a().createElement(
              "div",
              { className: e },
              a().createElement(et, { duration: t }),
            );
          }),
          nt = "Location_base_4d",
          at = "Location_duration_5d",
          rt = "Location_icon_eb",
          it = a().memo(function ({ location: u, className: e, timeToDismiss: t }) {
            return a().createElement(
              "div",
              { className: h()(nt, e) },
              u === fe.Dismissed && a().createElement(tt, { className: at, duration: t }),
              a().createElement("div", {
                className: rt,
                style: {
                  backgroundImage: `url(R.images.gui.maps.icons.tankmen.card.location.${u})`,
                },
              }),
            );
          });
        let ot, st;
        (!(function (u) {
          ((u.Default = "default"), (u.Selected = "selected"), (u.InBattle = "in_battle"));
        })(ot || (ot = {})),
          (function (u) {
            ((u.White = "white"), (u.Red = "red"));
          })(st || (st = {})));
        const lt = "Role_base_68",
          ct = a().memo(function ({ role: u, className: e, roleIconColor: t = st.White }) {
            return a().createElement("div", {
              className: h()(lt, e),
              style: {
                backgroundImage: `url(R.images.gui.maps.icons.tankmen.roles.opaque.${t}.${u})`,
              },
            });
          });
        let Et;
        !(function (u) {
          ((u.New = "new"),
            (u.Learned = "learned"),
            (u.Learning = "learning"),
            (u.Irrelevant = "irrelevant"),
            (u.Possible = "possible"),
            (u.ZeroSkill = "zeroSkill"));
        })(Et || (Et = {}));
        const _t = {
          base: "TankmanSkill_base_84",
          base__big: "TankmanSkill_base__big_a0",
          bg: "TankmanSkill_bg_f9",
          icon: "TankmanSkill_icon_1b",
          icon__irrelevant: "TankmanSkill_icon__irrelevant_50",
        };
        let At;
        !(function (u) {
          ((u.Big = "big"), (u.Small = "small"));
        })(At || (At = {}));
        const mt = a().memo(function ({ icon: u, type: e, size: t }) {
            const r = (0, n.useMemo)(() => {
                let u;
                return (
                  (u =
                    e === Et.Possible || e === Et.New
                      ? R.images.gui.maps.icons.tankmen.skills.medium.new_skill()
                      : R.images.gui.maps.icons.crew.$dyn(`${e}SkillFrame_${t}`)),
                  { backgroundImage: `url(${u})` }
                );
              }, [e, t]),
              i = (0, n.useMemo)(() => {
                if (!u) return null;
                return {
                  backgroundImage: `url(${R.images.gui.maps.icons.tankmen.skills.$dyn(t === At.Big ? "c_22x22" : "small").$dyn(u)})`,
                };
              }, [u, t]);
            return a().createElement(
              "div",
              { className: h()(_t.base, _t[`base__${t}`]) },
              a().createElement("div", { className: _t.bg, style: r }),
              i &&
                a().createElement("div", { className: h()(_t.icon, _t[`icon__${e}`]), style: i }),
            );
          }),
          dt = {
            base: "Skill_base_a9",
            base__double: "Skill_base__double_7a",
            base__collapsed: "Skill_base__collapsed_6e",
            skillLevel: "Skill_skillLevel_85",
          };
        let Ft;
        !(function (u) {
          ((u.Default = "default"), (u.Double = "double"), (u.Collapsed = "collapsed"));
        })(Ft || (Ft = {}));
        const Dt = ({ icon: u, type: e, isLevelVisible: t, skillLevel: n, theme: r }) =>
            a().createElement(
              "div",
              {
                className: h()(
                  dt.base,
                  dt[`base__${r}`],
                  t && dt.base__hasSkillLevel,
                  "new_skill" === u && dt.base__isNewSkill,
                ),
              },
              a().createElement(mt, { icon: u, size: At.Big, type: e }),
              t && a().createElement("div", { className: dt.skillLevel }, ke(n)),
            ),
          Bt = "Skills_base_d8",
          Ct = "Skills_skillContainer_54",
          ht = "Skills_divider_ee";
        function gt() {
          return (
            (gt =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            gt.apply(this, arguments)
          );
        }
        const pt = (0, n.memo)(({ skills: u, lastSkillLevel: e, className: t }) => {
            const n = u.length - 1,
              r = u.filter((u) => u.type === Et.ZeroSkill).length,
              i = r > 0,
              o = r === u.length;
            return a().createElement(
              "div",
              { className: h()(Bt, t) },
              u.map((t, s) => {
                const l = s === n,
                  c = i ? 26 : 28,
                  E = l && u.length < c && e < 100 && -1 !== e,
                  _ = ((u, e, t, n, a) => {
                    const r = a ? 16 : 18,
                      i = a ? 13 : 14,
                      o = a ? 8 : 9;
                    return e && t
                      ? Ft.Double
                      : n > r
                        ? u === i - 1 || e
                          ? Ft.Default
                          : Ft.Collapsed
                        : n > o && u === o - 1
                          ? Ft.Double
                          : Ft.Default;
                  })(s, l, E, u.length, i);
                return a().createElement(
                  "div",
                  { key: t.name + s, className: Ct },
                  a().createElement(Dt, gt({ theme: _, isLevelVisible: E, skillLevel: e }, t)),
                  s === r - 1 && !o && a().createElement("div", { className: ht }),
                );
              }),
            );
          }),
          bt = "ThemeHelper_base_39",
          vt = "ThemeHelper_disabledContent_20",
          ft = "ThemeHelper_disabledIcon_95",
          wt = "ThemeHelper_disabledTitle_57",
          Tt = a().memo(function ({
            isDisabled: u,
            className: e,
            disableReason: t,
            disableIcon: n,
          }) {
            return a().createElement(
              "div",
              { className: h()(bt, e) },
              u &&
                a().createElement(
                  "div",
                  { className: vt },
                  n &&
                    a().createElement("div", {
                      className: ft,
                      style: { backgroundImage: `url(${n})` },
                    }),
                  a().createElement("div", { className: wt }, t),
                ),
            );
          }),
          xt = ["children"];
        function St() {
          return (
            (St =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            St.apply(this, arguments)
          );
        }
        const kt = (u) => {
            let e = u.children,
              t = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, xt);
            return a().createElement(
              Nu,
              St(
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
          },
          yt = ({ cantBeSelected: u, args: e, children: t, isTooltipEnabled: n }) =>
            u
              ? a().createElement(
                  Wu,
                  { body: R.strings.crew.tankman.tooltip.cantBeSelected.body() },
                  t,
                )
              : a().createElement(kt, { args: e, isEnabled: n }, t),
          Mt = {
            base: "TankmanCard_base_dd",
            base__hovered: "TankmanCard_base__hovered_96",
            base__selected: "TankmanCard_base__selected_24",
            base__selectedFromMultiselect: "TankmanCard_base__selectedFromMultiselect_cb",
            base__selectDisabled: "TankmanCard_base__selectDisabled_b1",
            base__disabled: "TankmanCard_base__disabled_1f",
            themeHelper: "TankmanCard_themeHelper_78",
            locationIcon: "TankmanCard_locationIcon_26",
            crewRole: "TankmanCard_crewRole_2e",
            iconWrapper: "TankmanCard_iconWrapper_a3",
            base__isCollapsedOnHover: "TankmanCard_base__isCollapsedOnHover_5e",
            flag: "TankmanCard_flag_78",
            icon: "TankmanCard_icon_a5",
            separatorWrapper: "TankmanCard_separatorWrapper_fe",
            separator: "TankmanCard_separator_73",
            separator__top: "TankmanCard_separator__top_72",
            content: "TankmanCard_content_0c",
            fadeForSkills: "TankmanCard_fadeForSkills_3b",
            skills: "TankmanCard_skills_ef",
            helperLayer: "TankmanCard_helperLayer_09",
          },
          Lt = (0, n.memo)(
            ({
              tankmanID: u,
              recruitID: e,
              nation: t,
              skills: r,
              lastSkillLevel: i,
              specializationLevel: o,
              role: s,
              fullUserName: l,
              iconName: c,
              tankmanVehicleInfo: E,
              className: _,
              location: A,
              tankmanKind: m,
              onClick: d,
              onMouseDown: F,
              timeToDismiss: D,
              recruitGlowImage: B,
              isInSkin: C,
              isSelectedMode: g = !1,
              disableReason: p,
              disableIcon: b,
              cardState: v = Te.Default,
              isCollapsedOnHover: f = !1,
              isTooltipEnabled: w = !0,
              isSelectedTankmanFromMultySelect: T = !1,
              isSelectedLimitReached: x = !1,
              hasSpecializationLevelPenalty: S = !1,
              hasRolePenalty: k = !1,
              children: y,
            }) => {
              const M = m === we.Recruit,
                L = M && g ? Te.Disabled : v,
                R = v === Te.Selected,
                O = L === Te.Disabled,
                N = g && x && !T && !O,
                H = ((u, e, t = 150) => {
                  const a = (0, n.useState)(u),
                    r = a[0],
                    i = a[1],
                    o = Re((u) => i(u), e, t);
                  return {
                    isHovered: r,
                    handleMouseEnter: (0, n.useCallback)(() => o(!0), [o]),
                    handleMouseLeave: (0, n.useCallback)(() => o(!1), [o]),
                  };
                })(!1, []),
                I = H.isHovered,
                P = H.handleMouseEnter,
                W = H.handleMouseLeave,
                G = (0, n.useMemo)(() => {
                  if (B && M) return { backgroundImage: `url(${B})` };
                }, [B, M]);
              (0, n.useEffect)(() => {
                !I || R || O || (Tu.playHighlight(), f && wu(Me.SHOP_INFO));
              }, [I, R, O, f]);
              return a().createElement(
                "div",
                {
                  className: h()(
                    Mt.base,
                    _,
                    !N && I && Mt.base__hovered,
                    N && Mt.base__selectDisabled,
                    f && !O && Mt.base__isCollapsedOnHover,
                    Mt[`base__${T ? "selectedFromMultiselect" : L}`],
                  ),
                  onMouseEnter: P,
                  onMouseLeave: W,
                  onMouseDown: F,
                },
                a().createElement(Tt, {
                  isDisabled: O,
                  disableReason: null != p ? p : void 0,
                  disableIcon: null != b ? b : void 0,
                  className: Mt.themeHelper,
                }),
                s !== ve.Any &&
                  a().createElement(ct, {
                    role: s,
                    roleIconColor: k ? st.Red : st.White,
                    className: Mt.crewRole,
                  }),
                a().createElement(it, {
                  className: Mt.locationIcon,
                  location: A,
                  timeToDismiss: D,
                }),
                a().createElement(
                  "div",
                  { className: Mt.iconWrapper, style: G },
                  t &&
                    a().createElement("div", {
                      className: Mt.flag,
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.tankmen.card.nations.${t})`,
                      },
                    }),
                  a().createElement(Ie, {
                    name: c,
                    size: Ne.c158x118,
                    className: Mt.icon,
                    isSkin: C,
                  }),
                ),
                a().createElement(
                  "div",
                  { className: Mt.separatorWrapper },
                  a().createElement("div", { className: h()(Mt.separator, Mt.separator__top) }),
                  a().createElement("div", { className: Mt.separator }),
                ),
                a().createElement(
                  "div",
                  { className: Mt.content },
                  a().createElement(ut, {
                    fullUserName: l,
                    isRecruit: M,
                    tankmanVehicleInfo: E,
                    specializationLevel: o,
                    hasSpecializationLevelPenalty: S,
                  }),
                  a().createElement(pt, {
                    skills: r,
                    lastSkillLevel: i,
                    className: h()(Mt.skills, g && Mt.fadeForSkills),
                  }),
                ),
                a().createElement(
                  yt,
                  {
                    args: { tooltipId: M ? "tankmanNotRecruited" : "tankman", targetId: M ? e : u },
                    cantBeSelected: x && !O && !T,
                    isTooltipEnabled: w,
                  },
                  a().createElement("div", {
                    className: Mt.helperLayer,
                    onClick: () => {
                      O || R || !d || (d(), Tu.playClick());
                    },
                  }),
                ),
                !O && (null == y ? void 0 : y(I)),
              );
            },
          ),
          Rt = "WarningText_base_10",
          Ot = "WarningText_alertIcon_8f",
          Nt = (0, n.memo)(({ className: u, children: e }) =>
            a().createElement(
              "div",
              { className: h()(Rt, u) },
              a().createElement("div", { className: Ot }),
              e,
            ),
          );
        var Ht = t(9887),
          It = t.n(Ht);
        const Pt = ["xl", "lg", "md", "sm", "xs"],
          Wt = (u) => u.includes("_") && ((u) => Pt.includes(u))(u.split("_").at(-1)),
          Gt = [b.ExtraLarge, b.Large, b.Medium, b.Small, b.ExtraSmall],
          $t = (u, e) =>
            Object.keys(u).reduce((t, n) => {
              if (n in t) return t;
              if (Wt(n)) {
                const a = n.split("_").slice(0, -1).join("_");
                if (a in t) return t;
                const r = Gt.indexOf(e),
                  i = (-1 !== r ? Pt.slice(r) : [])
                    .map((u) => a + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  o = i ? u[i] : void 0;
                return ((t[a] = void 0 !== o ? o : u[a]), t);
              }
              const a = u[n];
              return (
                void 0 === a ||
                  ((u, e) => Pt.some((t) => void 0 !== e[`${u}_${t}`]))(n, u) ||
                  (t[n] = a),
                t
              );
            }, {}),
          jt = (u, e = $t) => {
            const t = (
              (u, e = $t) =>
              (t) => {
                const r = w().mediaSize,
                  i = (0, n.useMemo)(() => e(t, r), [t, r]);
                return a().createElement(u, i);
              }
            )(u, e);
            return a().memo((e) =>
              Object.keys(e).some((u) => Wt(u) && void 0 !== e[u])
                ? a().createElement(t, e)
                : a().createElement(u, e),
            );
          },
          Ut = {
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
          Vt = [
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
        function Xt() {
          return (
            (Xt =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            Xt.apply(this, arguments)
          );
        }
        Object.keys(It());
        const zt = {
            XL: { mt: Ut.mt__XL, mr: Ut.mr__XL, mb: Ut.mb__XL, ml: Ut.ml__XL },
            LG: { mt: Ut.mt__LG, mr: Ut.mr__LG, mb: Ut.mb__LG, ml: Ut.ml__LG },
            MDp: { mt: Ut.mt__MDp, mr: Ut.mr__MDp, mb: Ut.mb__MDp, ml: Ut.ml__MDp },
            MD: { mt: Ut.mt__MD, mr: Ut.mr__MD, mb: Ut.mb__MD, ml: Ut.ml__MD },
            SMp: { mt: Ut.mt__SMp, mr: Ut.mr__SMp, mb: Ut.mb__SMp, ml: Ut.ml__SMp },
            SM: { mt: Ut.mt__SM, mr: Ut.mr__SM, mb: Ut.mb__SM, ml: Ut.ml__SM },
            XS: { mt: Ut.mt__XS, mr: Ut.mr__XS, mb: Ut.mb__XS, ml: Ut.ml__XS },
          },
          Kt = (Object.keys(zt), ["mt", "mr", "mb", "ml"]),
          qt = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Yt = jt((u) => {
            let e = u.className,
              t = u.width,
              r = u.height,
              i = u.m,
              o = u.mt,
              s = void 0 === o ? i : o,
              l = u.mr,
              c = void 0 === l ? i : l,
              E = u.mb,
              _ = void 0 === E ? i : E,
              A = u.ml,
              m = void 0 === A ? i : A,
              d = u.column,
              F = u.row,
              D = u.flexDirection,
              B = void 0 === D ? (d ? "column" : F && "row") || void 0 : D,
              C = u.flexStart,
              g = u.center,
              p = u.flexEnd,
              b = u.spaceBetween,
              v = u.spaceAround,
              f = u.justifyContent,
              w =
                void 0 === f
                  ? (C ? "flex-start" : g && "center") ||
                    (p && "flex-end") ||
                    (b && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : f,
              T = u.alignItems,
              x =
                void 0 === T
                  ? (C ? "flex-start" : g && "center") || (p && "flex-end") || void 0
                  : T,
              S = u.alignSelf,
              k = u.wrap,
              y = u.flexWrap,
              M = void 0 === y ? (k ? "wrap" : void 0) : y,
              L = u.grow,
              R = u.shrink,
              O = u.flex,
              N = void 0 === O ? (L || R ? `${L ? 1 : 0} ${R ? 1 : 0} auto` : void 0) : O,
              H = u.style,
              I = u.children,
              P = (function (u, e) {
                if (null == u) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(u);
                for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
                return a;
              })(u, Vt);
            const W = (0, n.useMemo)(() => {
                const u = { mt: s, mr: c, mb: _, ml: m },
                  e = ((u) =>
                    Kt.reduce((e, t) => {
                      const n = u[t];
                      return n && "number" != typeof n ? e.concat(zt[!0 === n ? "MD" : n][t]) : e;
                    }, []))(u),
                  n = ((u) =>
                    Kt.reduce((e, t) => {
                      const n = u[t];
                      return ("number" == typeof n && (e[qt[t]] = n + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, H, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: N,
                    alignSelf: S,
                    display: B || x ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: M,
                    justifyContent: w,
                    alignItems: x,
                  }),
                  computedClassNames: e,
                };
              }, [t, r, s, c, _, m, H, N, S, B, M, w, x]),
              G = W.computedStyle,
              $ = W.computedClassNames;
            return a().createElement(
              "div",
              Xt({ className: h()(Ut.base, ...$, e), style: G }, P),
              I,
            );
          }),
          Zt = "FormatText_base_d0",
          Qt = ({ binding: u, text: e = "", classMix: t, alignment: r = I.left }) =>
            null === e
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  n.Fragment,
                  null,
                  e.split("\n").map((e, i) =>
                    a().createElement(
                      "div",
                      { className: h()(Zt, t), key: `${e}-${i}` },
                      ((u, e, t) =>
                        u.split(/%\((.*?)\)(?:[sd])?/g).map((u) => (t && u in t ? t[u] : K(u, e))))(
                        e,
                        r,
                        u,
                      ).map((u, e) => a().createElement(n.Fragment, { key: `${e}-${u}` }, u)),
                    ),
                  ),
                );
        var Jt = t(3532),
          un = t.n(Jt);
        const en = {
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
          tn = [
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
        function nn() {
          return (
            (nn =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            nn.apply(this, arguments)
          );
        }
        Object.keys(It());
        const an = Object.keys(un()),
          rn = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          on = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          sn = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          ln = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          cn =
            (Object.keys(ln),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": rn,
              "heading-H36": rn,
              "heading-H28": on,
              "heading-H24": on,
              "heading-H24R": on,
              "heading-H22": on,
              "heading-H20R": on,
              "heading-H18": on,
              "heading-H15": sn,
              "heading-H14": sn,
              "paragraph-P24": on,
              "paragraph-P18": on,
              "paragraph-P16": on,
              "paragraph-P14": sn,
              "paragraph-P12": sn,
              "paragraph-P10": sn,
            }),
          En =
            (Object.keys(cn),
            (u) =>
              u
                ? ((u) => an.includes(u))(u)
                  ? { colorClassName: en[u] }
                  : { colorStyle: { color: u } }
                : {}),
          _n = jt((u) => {
            let e = u.text,
              t = u.variant,
              r = u.className,
              i = u.color,
              o = u.m,
              s = u.mt,
              l = void 0 === s ? o : s,
              c = u.mr,
              E = void 0 === c ? o : c,
              _ = u.mb,
              A = void 0 === _ ? o : _,
              m = u.ml,
              d = void 0 === m ? o : m,
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
              })(u, tn);
            const C = (0, n.useMemo)(() => {
                const u = En(i),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  n = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, n), colorClassName: e };
              }, [F, i]),
              g = C.computedStyle,
              p = C.colorClassName;
            return a().createElement(
              Yt,
              nn(
                {
                  className: h()(en.base, t && en[t], p, r),
                  style: g,
                  mt: !0 === l ? cn[t || "paragraph-P16"].mt : l,
                  mr: !0 === E ? cn[t || "paragraph-P16"].mr : E,
                  mb: !0 === A ? cn[t || "paragraph-P16"].mb : A,
                  ml: !0 === d ? cn[t || "paragraph-P16"].ml : d,
                },
                B,
              ),
              void 0 !== D ? a().createElement(Qt, nn({}, D, { text: e })) : e,
            );
          }),
          An = "DismissTankmanDescription_base_1e",
          mn = "DismissTankmanDescription_warning_8c",
          dn = "DismissTankmanDescription_timeValue_6f",
          Fn = R.strings.dialogs.dismissTankman,
          Dn = (0, te.Pi)(() => {
            const u = be().model,
              e = u.computes.getReplacedTankman(),
              t = u.computes.getReplacedTankmanVehicleInfo();
            return a().createElement(
              "div",
              { className: An },
              u.isRecoveryPossible.get()
                ? a().createElement(
                    a().Fragment,
                    null,
                    u.isLimitReached.get() &&
                      a().createElement(
                        Nt,
                        { className: mn },
                        W(Fn.limited(), {
                          name: e.fullUserName,
                          role: R.strings.item_types.tankman.roles.$dyn(e.role),
                          vehicle: t.vehicleName,
                        }),
                      ),
                    a().createElement(_n, {
                      text: Fn.description.time(),
                      format: {
                        binding: {
                          time: a().createElement(_n, {
                            className: dn,
                            format: { binding: { time: u.dismissPeriod.get() } },
                            text: Fn.description.timeText(),
                          }),
                        },
                      },
                    }),
                  )
                : a().createElement(Nt, null, R.strings.dialogs.dismissTankman.noRecovery()),
            );
          }),
          Bn = "DismissTankmanContent_base_57",
          Cn = (0, te.Pi)(() => {
            const u = be().model;
            return a().createElement(
              "div",
              { className: Bn },
              u.isRecoveryPossible.get()
                ? a().createElement(Dn, null)
                : a().createElement(Nt, null, R.strings.dialogs.dismissTankman.noRecovery()),
            );
          }),
          hn = "DismissTankmanApp_tankmanWrapper_05",
          gn = ["onClose", "buttons", "isShown", "displayFlags"];
        function pn() {
          return (
            (pn =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (u[n] = t[n]);
                }
                return u;
              }),
            pn.apply(this, arguments)
          );
        }
        const bn = (0, te.Pi)((u) => {
          let e = u.onClose,
            t = u.buttons,
            n = u.isShown,
            r = u.displayFlags,
            i = (function (u, e) {
              if (null == u) return {};
              var t,
                n,
                a = {},
                r = Object.keys(u);
              for (n = 0; n < r.length; n++) ((t = r[n]), e.indexOf(t) >= 0 || (a[t] = u[t]));
              return a;
            })(u, gn);
          const o = be().model.computes.getTankman();
          return a().createElement(
            ce,
            pn({ onClose: e, buttons: t, displayFlags: r, isShown: n }, i, {
              icon: a().createElement(Lt, pn({}, o, { className: hn })),
              title: R.strings.dialogs.dismissTankman.header(),
              content: a().createElement(Cn, null),
            }),
          );
        });
        engine.whenReady.then(() => {
          H().render(
            a().createElement(
              pe,
              null,
              a().createElement(O, null, a().createElement(ee, { Template: bn })),
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
          for (var [e, t, n] = deferred[s], r = !0, i = 0; i < e.length; i++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[i]))
              ? e.splice(i--, 1)
              : ((r = !1), n < a && (a = n));
          if (r) {
            deferred.splice(s--, 1);
            var o = t();
            void 0 !== o && (u = o);
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
    (__webpack_require__.j = 97),
    (() => {
      var u = { 97: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var n,
            a,
            [r, i, o] = t,
            s = 0;
          if (r.some((e) => 0 !== u[e])) {
            for (n in i) __webpack_require__.o(i, n) && (__webpack_require__.m[n] = i[n]);
            if (o) var l = o(__webpack_require__);
          }
          for (e && e(t); s < r.length; s++)
            ((a = r[s]), __webpack_require__.o(u, a) && u[a] && u[a][0](), (u[a] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(2754));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
