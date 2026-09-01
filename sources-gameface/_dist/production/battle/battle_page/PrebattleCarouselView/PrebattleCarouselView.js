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
        (t.r(e), t.d(e, { mouse: () => i, onResize: () => a }));
        var r = t(2472),
          n = t(1176);
        const a = (0, r.E)("clientResized"),
          o = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const i = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && (0, n.R)(!1);
          }
          function t() {
            u.enabled && (0, n.R)(!0);
          }
          function r() {
            u.enabled
              ? u.listeners < 1
                ? ((u.initialized = !1),
                  document.body.removeEventListener("mouseenter", e),
                  document.body.removeEventListener("mouseleave", t))
                : u.initialized ||
                  ((u.initialized = !0),
                  document.body.addEventListener("mouseenter", e),
                  document.body.addEventListener("mouseleave", t))
              : (0, n.R)(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (e, t) => (
              (e[t] = (function (e) {
                return (t) => {
                  u.listeners += 1;
                  let n = !0;
                  const a = `mouse${e}`,
                    i = o[e]((u) => t([u, "outside"]));
                  function l(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(a, l),
                    r(),
                    () => {
                      n &&
                        (i(), window.removeEventListener(a, l), (u.listeners -= 1), r(), (n = !1));
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
              ((u.enabled = !1), r());
            },
            enable() {
              ((u.enabled = !0), r());
            },
            enableOutside() {
              u.enabled && (0, n.R)(!0);
            },
            disableOutside() {
              u.enabled && (0, n.R)(!1);
            },
          });
        })();
      },
      5959: (u, e, t) => {
        "use strict";
        (t.r(e),
          t.d(e, {
            events: () => r,
            getMouseGlobalPosition: () => a,
            getSize: () => n,
            graphicsQuality: () => o,
          }));
        var r = t(527);
        function n(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function a(u = "px") {
          return "rem" === u
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const o = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (u, e, t) => {
        "use strict";
        function r(u) {
          viewEnv.setTrackMouseOnStage(u);
        }
        t.d(e, { R: () => r });
      },
      2472: (u, e, t) => {
        "use strict";
        function r(u) {
          return (e) => (
            engine.on(u, e),
            () => {
              engine.off(u, e);
            }
          );
        }
        t.d(e, { E: () => r });
      },
      3138: (u, e, t) => {
        "use strict";
        t.d(e, { O: () => n });
        var r = t(5959);
        const n = { view: t(7641), client: r };
      },
      3722: (u, e, t) => {
        "use strict";
        function r(u, e, t = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, t);
        }
        function n(u, e, t) {
          return `url(${r(u, e, t)})`;
        }
        (t.r(e), t.d(e, { getBgUrl: () => n, getTextureUrl: () => r }));
      },
      6112: (u, e, t) => {
        "use strict";
        t.d(e, { W: () => r });
        const r = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => n });
        var r = t(2472);
        const n = {
          onTextureFrozen: (0, r.E)("self.onTextureFrozen"),
          onTextureReady: (0, r.E)("self.onTextureReady"),
          onDomBuilt: (0, r.E)("self.onDomBuilt"),
          onLoaded: (0, r.E)("self.onLoaded"),
          onDisplayChanged: (0, r.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, r.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, r.E)("children.onAdded"),
            onLoaded: (0, r.E)("children.onLoaded"),
            onRemoved: (0, r.E)("children.onRemoved"),
            onAttached: (0, r.E)("children.onAttached"),
            onTextureReady: (0, r.E)("children.onTextureReady"),
            onRequestPosition: (0, r.E)("children.requestPosition"),
          },
        };
      },
      7641: (u, e, t) => {
        "use strict";
        (t.r(e),
          t.d(e, {
            addModelObserver: () => c,
            addPreloadTexture: () => i,
            children: () => r,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => a.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => p,
            freezeTextureBeforeResize: () => m,
            getBrowserTexturePath: () => s,
            getDisplayStatus: () => b,
            getScale: () => d,
            getSize: () => A,
            getViewGlobalPosition: () => F,
            isClientAccessible: () => h,
            isEventHandled: () => v,
            isFocused: () => g,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => _,
            sendEvent: () => o.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => f,
            setInputPaddingsRem: () => l,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => x,
          }));
        var r = t(3722),
          n = t(6112),
          a = t(6538),
          o = t(8566);
        function i(u) {
          viewEnv.addPreloadTexture(u);
        }
        function l(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function s(u, e, t, r = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, r);
        }
        function c(u, e, t) {
          return viewEnv.addDataChangedCallback(u, e, t);
        }
        function E(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function A(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function _(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function F(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: B(e.x), y: B(e.y) };
        }
        function m() {
          viewEnv.freezeTextureBeforeResize();
        }
        function d() {
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
        function g() {
          return viewEnv.isFocused();
        }
        function h() {
          return viewEnv.isClientAccessible();
        }
        function f() {
          return viewEnv.setEventHandled();
        }
        function v() {
          return viewEnv.isEventHandled();
        }
        function p() {
          viewEnv.forceTriggerMouseMove();
        }
        function b() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(n.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === n.W[e]), u),
            {},
          ),
          S = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          x = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : a.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        "use strict";
        t.d(e, { qP: () => s });
        const r = ["args"];
        const n = 2,
          a = 16,
          o = 32,
          i = 64,
          l = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const a = e.args,
                o = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    r,
                    n = {},
                    a = Object.keys(u);
                  for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                  return n;
                })(e, r);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, o, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, o));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: u });
            var n;
          },
          s = {
            close(u) {
              l("popover" === u ? n : o);
            },
            minimize() {
              l(i);
            },
            move(u) {
              l(a, { isMouseEvent: !0, on: u });
            },
          };
      },
      5521: (u, e, t) => {
        "use strict";
        let r, n;
        (t.d(e, { n: () => r }),
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
          })(r || (r = {})),
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
          })(n || (n = {})));
      },
      1358: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => a });
        var r = t(3138);
        class n {
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
            return (window.__dataTracker || (window.__dataTracker = new n()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(u, e, t = 0, n = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const a = r.O.view.addModelObserver(u, t, n);
            return (
              a > 0
                ? ((this._callbacks[a] = e),
                  t > 0 && (this._views[t] ? this._views[t].push(a) : (this._views[t] = [a])))
                : console.error("Can't add callback for model:", u),
              a
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
              const r = this._callbacks[t];
              void 0 !== r && r(u, e);
            });
          }
        }
        n.__instance = void 0;
        const a = n;
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
        t.d(e, { B0: () => l, wU: () => p, ry: () => B, Eu: () => C, SW: () => f, P3: () => v });
        class r {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (u) => {
                this.entries.forEach(({ container: e, callback: t }) => {
                  let r = u.target;
                  do {
                    if (r === e) return;
                    r = r.parentNode;
                  } while (r);
                  t();
                });
              }));
          }
          static get instance() {
            return (r.__instance || (r.__instance = new r()), r.__instance);
          }
          register(u, e) {
            (this.addMouseListener(), this.entries.push({ container: u, callback: e }));
          }
          unregister(u, e) {
            const t = u,
              r = e;
            ((this.entries = this.entries.filter(
              ({ container: u, callback: e }) => u !== t || e !== r,
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
        var a = t(1358);
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
        let l;
        !(function (u) {
          ((u[(u.UNDEFINED = 0)] = "UNDEFINED"),
            (u[(u.TOOLTIP = 1)] = "TOOLTIP"),
            (u[(u.POP_OVER = 2)] = "POP_OVER"),
            (u[(u.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (u[(u.DROP_DOWN = 8)] = "DROP_DOWN"),
            (u[(u.MOVE = 16)] = "MOVE"),
            (u[(u.CLOSE = 32)] = "CLOSE"),
            (u[(u.MINIMIZE = 64)] = "MINIMIZE"));
        })(l || (l = {}));
        const s = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          A = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = t(5521),
          F = t(3138);
        const m = ["args"];
        function d(u, e, t, r, n, a, o) {
          try {
            var i = u[a](o),
              l = i.value;
          } catch (u) {
            return void t(u);
          }
          i.done ? e(l) : Promise.resolve(l).then(r, n);
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
                  return new Promise(function (r, n) {
                    var a = u.apply(e, t);
                    function o(u) {
                      d(a, r, n, o, i, "next", u);
                    }
                    function i(u) {
                      d(a, r, n, o, i, "throw", u);
                    }
                    o(void 0);
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
          g = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const n = e.args,
                a = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    r,
                    n = {},
                    a = Object.keys(u);
                  for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                  return n;
                })(e, m);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, a, {
                      arguments:
                        ((r = n),
                        Object.entries(r).map(([u, e]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, a));
            } else viewEnv.handleViewEvent({ __Type: t, type: u });
            var r;
          },
          h = () => g(l.CLOSE),
          f = () => g(l.POP_OVER, { on: !1 }),
          v = (u, e, t, r, n = R.invalid("resId"), a) => {
            const o = F.O.view.getViewGlobalPosition(),
              i = t.getBoundingClientRect(),
              s = i.x,
              c = i.y,
              E = i.width,
              A = i.height,
              _ = {
                x: F.O.view.pxToRem(s) + o.x,
                y: F.O.view.pxToRem(c) + o.y,
                width: F.O.view.pxToRem(E),
                height: F.O.view.pxToRem(A),
              };
            g(l.POP_OVER, {
              isMouseEvent: !0,
              contentID: u,
              decoratorID: r || R.invalid("resId"),
              targetID: n,
              direction: e,
              bbox: D(_),
              on: !0,
              args: a,
            });
          },
          p = () => viewEnv.isWindowShownByViewEvent(l.POP_OVER),
          b = (u, e) => {
            u.keyCode === _.n.ESCAPE && e();
          };
        var w = t(7572);
        const S = n.instance,
          x = {
            DataTracker: a.Z,
            ViewModel: w.Z,
            ViewEventType: l,
            NumberFormatType: s,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: A,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (u) => g(l.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: h,
            sendClosePopOverEvent: f,
            sendShowContextMenuEvent: (u, e, t = 0) => {
              g(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: v,
            addEscapeListener: (u) => {
              const e = (e) => b(e, u);
              return (
                window.addEventListener("keydown", e),
                () => window.removeEventListener("keydown", e)
              );
            },
            closeOnEsc: (u) => {
              b(u, h);
            },
            handleViewEvent: g,
            onBindingsReady: B,
            onLayoutReady: C,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(l.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(l.CONTEXT_MENU),
            isPopOverShown: p,
            dumpViewModel: function u(e) {
              const t = {};
              if ("object" != typeof e) return e;
              for (const r in e)
                if (Object.prototype.hasOwnProperty.call(e, r)) {
                  const n = Object.prototype.toString.call(e[r]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = e[r];
                    t[r] = [];
                    for (let e = 0; e < n.length; e++) t[r].push({ value: u(n[e].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[r] = u(e[r]))
                      : (t[r] = e[r]);
                }
              return t;
            },
            ClickOutsideManager: S,
            SystemLocale: o,
            UserLocale: i,
          };
        window.ViewEnvHelper = x;
      },
      4545: (u, e, t) => {
        "use strict";
        var r = {};
        (t.r(r),
          t.d(r, {
            Area: () => lt,
            Bar: () => at,
            DefaultScroll: () => it,
            Direction: () => Ue,
            defaultSettings: () => ze,
            useHorizontalScrollApi: () => Xe,
          }));
        var n = {};
        (t.r(n),
          t.d(n, {
            Area: () => wt,
            Bar: () => vt,
            Default: () => bt,
            useVerticalScrollApi: () => st,
          }));
        var a = t(6179),
          o = t.n(a);
        const i = (u, e, t) =>
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
        var l = t(3138);
        const s = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function E(u, e, t) {
          const r = (function (u, e) {
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
            n = (function (u, e) {
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
        })(c || (c = {}));
        const A = l.O.client.getSize("rem"),
          _ = A.width,
          F = A.height,
          m = Object.assign({ width: _, height: F }, E(_, F, s)),
          d = (0, a.createContext)(m),
          D = ["children"];
        const B = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, D);
          const r = (0, a.useContext)(d),
            n = r.extraLarge,
            o = r.large,
            l = r.medium,
            s = r.small,
            c = r.extraSmall,
            E = r.extraLargeWidth,
            A = r.largeWidth,
            _ = r.mediumWidth,
            F = r.smallWidth,
            m = r.extraSmallWidth,
            B = r.extraLargeHeight,
            C = r.largeHeight,
            g = r.mediumHeight,
            h = r.smallHeight,
            f = r.extraSmallHeight,
            v = { extraLarge: B, large: C, medium: g, small: h, extraSmall: f };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && n) return e;
            if (t.large && o) return e;
            if (t.medium && l) return e;
            if (t.small && s) return e;
            if (t.extraSmall && c) return e;
          } else {
            if (t.extraLargeWidth && E) return i(e, t, v);
            if (t.largeWidth && A) return i(e, t, v);
            if (t.mediumWidth && _) return i(e, t, v);
            if (t.smallWidth && F) return i(e, t, v);
            if (t.extraSmallWidth && m) return i(e, t, v);
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
              if (t.smallHeight && h) return e;
              if (t.extraSmallHeight && f) return e;
            }
          }
          return null;
        };
        B.defaultProps = {
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
        (0, a.memo)(B);
        const C = (u) => {
            const e = (0, a.useRef)(!1);
            e.current || (u(), (e.current = !0));
          },
          g = (0, a.memo)(({ children: u }) => {
            const e = (0, a.useContext)(d),
              t = (0, a.useState)(e),
              r = t[0],
              n = t[1],
              i = (0, a.useCallback)((u, e) => {
                const t = l.O.view.pxToRem(u),
                  r = l.O.view.pxToRem(e);
                n(Object.assign({ width: t, height: r }, E(t, r, s)));
              }, []);
            (C(() => {
              engine.on("clientResized", i);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", i), [i]));
            const c = (0, a.useMemo)(() => Object.assign({}, r), [r]);
            return o().createElement(d.Provider, { value: c }, u);
          });
        var h = t(6483),
          f = t.n(h),
          v = t(926),
          p = t.n(v);
        let b, w, S;
        (!(function (u) {
          ((u[(u.ExtraSmall = s.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = s.small.width)] = "Small"),
            (u[(u.Medium = s.medium.width)] = "Medium"),
            (u[(u.Large = s.large.width)] = "Large"),
            (u[(u.ExtraLarge = s.extraLarge.width)] = "ExtraLarge"));
        })(b || (b = {})),
          (function (u) {
            ((u[(u.ExtraSmall = s.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = s.small.width)] = "Small"),
              (u[(u.Medium = s.medium.width)] = "Medium"),
              (u[(u.Large = s.large.width)] = "Large"),
              (u[(u.ExtraLarge = s.extraLarge.width)] = "ExtraLarge"));
          })(w || (w = {})),
          (function (u) {
            ((u[(u.ExtraSmall = s.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = s.small.height)] = "Small"),
              (u[(u.Medium = s.medium.height)] = "Medium"),
              (u[(u.Large = s.large.height)] = "Large"),
              (u[(u.ExtraLarge = s.extraLarge.height)] = "ExtraLarge"));
          })(S || (S = {})));
        const x = () => {
            const u = (0, a.useContext)(d),
              e = u.width,
              t = u.height,
              r = ((u) => {
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
              n = ((u) => {
                switch (!0) {
                  case u.extraLargeWidth:
                    return w.ExtraLarge;
                  case u.largeWidth:
                    return w.Large;
                  case u.mediumWidth:
                    return w.Medium;
                  case u.smallWidth:
                    return w.Small;
                  case u.extraSmallWidth:
                    return w.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), w.ExtraSmall);
                }
              })(u),
              o = ((u) => {
                switch (!0) {
                  case u.extraLargeHeight:
                    return S.ExtraLarge;
                  case u.largeHeight:
                    return S.Large;
                  case u.mediumHeight:
                    return S.Medium;
                  case u.smallHeight:
                    return S.Small;
                  case u.extraSmallHeight:
                    return S.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), S.ExtraSmall);
                }
              })(u);
            return {
              mediaSize: r,
              mediaWidth: n,
              mediaHeight: o,
              remScreenWidth: e,
              remScreenHeight: t,
            };
          },
          y = ["children", "className"];
        function M() {
          return (
            (M =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            M.apply(this, arguments)
          );
        }
        const L = {
            [w.ExtraSmall]: "",
            [w.Small]: p().SMALL_WIDTH,
            [w.Medium]: `${p().SMALL_WIDTH} ${p().MEDIUM_WIDTH}`,
            [w.Large]: `${p().SMALL_WIDTH} ${p().MEDIUM_WIDTH} ${p().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${p().SMALL_WIDTH} ${p().MEDIUM_WIDTH} ${p().LARGE_WIDTH} ${p().EXTRA_LARGE_WIDTH}`,
          },
          T = {
            [S.ExtraSmall]: "",
            [S.Small]: p().SMALL_HEIGHT,
            [S.Medium]: `${p().SMALL_HEIGHT} ${p().MEDIUM_HEIGHT}`,
            [S.Large]: `${p().SMALL_HEIGHT} ${p().MEDIUM_HEIGHT} ${p().LARGE_HEIGHT}`,
            [S.ExtraLarge]: `${p().SMALL_HEIGHT} ${p().MEDIUM_HEIGHT} ${p().LARGE_HEIGHT} ${p().EXTRA_LARGE_HEIGHT}`,
          },
          O = {
            [b.ExtraSmall]: "",
            [b.Small]: p().SMALL,
            [b.Medium]: `${p().SMALL} ${p().MEDIUM}`,
            [b.Large]: `${p().SMALL} ${p().MEDIUM} ${p().LARGE}`,
            [b.ExtraLarge]: `${p().SMALL} ${p().MEDIUM} ${p().LARGE} ${p().EXTRA_LARGE}`,
          },
          k = (u) => {
            let e = u.children,
              t = u.className,
              r = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, y);
            const n = x(),
              a = n.mediaWidth,
              i = n.mediaHeight,
              l = n.mediaSize;
            return o().createElement("div", M({ className: f()(t, L[a], T[i], O[l]) }, r), e);
          },
          P = ["children"];
        const N = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, P);
          return o().createElement(g, null, o().createElement(k, t, e));
        };
        var H = t(493),
          I = t.n(H),
          W = t(3403);
        const V = {
          header: R.strings.tooltips.battleCarousel.filter.reset.header(),
          body: R.strings.tooltips.battleCarousel.filter.reset.body(),
        };
        function G(u) {
          return u;
        }
        function U() {
          return !1;
        }
        console.log;
        var z = t(9174);
        function j(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return X(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return X(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            t && (u = t);
            var r = 0;
            return function () {
              return r >= u.length ? { done: !0 } : { done: !1, value: u[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function X(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, r = new Array(e); t < e; t++) r[t] = u[t];
          return r;
        }
        const $ = (u) => (0 === u ? window : window.subViews.get(u));
        var K = t(3946);
        const Y = ((u, e) => {
            const t = (0, a.createContext)({});
            return [
              function ({ mode: r = "real", options: n, children: i, mocks: s }) {
                const c = (0, a.useRef)([]),
                  E = (t, r, n) => {
                    var a;
                    const o = (function ({
                        initializer: u = !0,
                        rootId: e = 0,
                        getRoot: t = $,
                        context: r = "model",
                      } = {}) {
                        const n = new Map();
                        function a(u, e = 0) {
                          viewEnv.removeDataChangedCallback(u, e)
                            ? n.delete(u)
                            : console.error("Can't remove callback by id:", u);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (u, e, t) => {
                            t.forEach((e) => {
                              const t = n.get(e);
                              void 0 !== t && t(u);
                            });
                          });
                        });
                        const o = (u) => {
                          const n = t(e),
                            a = r.split(".").reduce((u, e) => u[e], n);
                          return "string" != typeof u || 0 === u.length
                            ? a
                            : u.split(".").reduce((u, e) => {
                                const t = u[e];
                                return "function" == typeof t ? t.bind(u) : t;
                              }, a);
                        };
                        return {
                          subscribe: (t, a) => {
                            const i = "string" == typeof a ? `${r}.${a}` : r,
                              s = l.O.view.addModelObserver(i, e, !0);
                            return (n.set(s, t), u && t(o(a)), s);
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
                            for (var u, t = j(n.keys()); !(u = t()).done;) a(u.value, e);
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
                      s = (u) =>
                        "mocks" === t ? (null == n ? void 0 : n.getter(u)) : i.readByPath(u),
                      E = (u) => c.current.push(u),
                      A = u({
                        mode: t,
                        readByPath: s,
                        externalModel: i,
                        observableModel: {
                          array: (u, e) => {
                            const r = null != e ? e : s(u),
                              n = z.LO.box(r, { equals: U });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, z.aD)((u) => n.set(u)),
                                  u,
                                ),
                              n
                            );
                          },
                          object: (u, e) => {
                            const r = null != e ? e : s(u),
                              n = z.LO.box(r, { equals: U });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, z.aD)((u) => n.set(u)),
                                  u,
                                ),
                              n
                            );
                          },
                          primitives: (u, e) => {
                            const r = s(e);
                            if (Array.isArray(u)) {
                              const n = u.reduce((u, e) => ((u[e] = z.LO.box(r[e], {})), u), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, z.aD)((e) => {
                                      u.forEach((u) => {
                                        n[u].set(e[u]);
                                      });
                                    }),
                                    e,
                                  ),
                                n
                              );
                            }
                            {
                              const n = u,
                                a = Object.entries(n),
                                o = a.reduce((u, [e, t]) => ((u[t] = z.LO.box(r[e], {})), u), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, z.aD)((u) => {
                                      a.forEach(([e, t]) => {
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
                      _ = { mode: t, model: A, externalModel: i, cleanup: E };
                    return {
                      model: A,
                      controls: "mocks" === t && n ? n.controls(_) : e(_),
                      externalModel: i,
                      mode: t,
                    };
                  },
                  A = (0, a.useRef)(!1),
                  _ = (0, a.useState)(r),
                  F = _[0],
                  m = _[1],
                  d = (0, a.useState)(() => E(r, n, s)),
                  D = d[0],
                  B = d[1];
                return (
                  (0, a.useEffect)(() => {
                    A.current ? B(E(F, n, s)) : (A.current = !0);
                  }, [s, F, n]),
                  (0, a.useEffect)(() => {
                    m(r);
                  }, [r]),
                  (0, a.useEffect)(
                    () => () => {
                      (D.externalModel.dispose(), c.current.forEach((u) => u()));
                    },
                    [D],
                  ),
                  o().createElement(t.Provider, { value: D }, i)
                );
              },
              () => (0, a.useContext)(t),
            ];
          })(
            ({ observableModel: u }) => {
              const e = { root: u.object(), vehicles: u.array("vehicles.items") },
                t = (0, K.Om)(() => e.vehicles.get().length),
                r = (0, K.Om)(
                  () => {
                    return (
                      (u = e.vehicles.get()),
                      (t = G),
                      Array.isArray(u)
                        ? u.map(t)
                        : u.map((u, e, r) => t(null == u ? void 0 : u.value, e, r))
                    );
                    var u, t;
                  },
                  { equals: U },
                ),
                n = (0, K.Om)(() => {
                  let u = 0;
                  const e = r();
                  for (let r = 0; r < t(); ++r) {
                    const t = e[r];
                    if (t.isSelected && t.isVisible) return u;
                    t.isVisible && ++u;
                  }
                  return 0;
                });
              return Object.assign({}, e, {
                computes: { getVehicleItems: r, vehiclesItemsLength: t, selectedIndex: n },
              });
            },
            ({ externalModel: u }) => ({
              onApplyFavoritesFilter: u.createCallbackNoArgs("onApplyFavoritesFilter"),
              onApplyRentedFilter: u.createCallbackNoArgs("onApplyRentedFilter"),
              onClickVehicle: u.createCallback((u) => ({ intCD: u }), "onVehicleClick"),
              onClearFilters: u.createCallbackNoArgs("onClearFilters"),
              onSetDualRow: u.createCallbackNoArgs("onSetDualRow"),
            }),
          ),
          q = Y[0],
          Z = Y[1];
        let Q, J;
        function uu(u) {
          engine.call("PlaySound", u);
        }
        (!(function (u) {
          ((u.main = "main"),
            (u.primary = "primary"),
            (u.primaryGreen = "primaryGreen"),
            (u.primaryRed = "primaryRed"),
            (u.secondary = "secondary"),
            (u.ghost = "ghost"));
        })(Q || (Q = {})),
          (function (u) {
            ((u.extraSmall = "extraSmall"), (u.small = "small"), (u.medium = "medium"));
          })(J || (J = {})));
        const eu = {
            playHighlight() {
              uu("highlight");
            },
            playClick() {
              uu("play");
            },
            playYes() {
              uu("yes1");
            },
          },
          tu = {
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
        let ru;
        !(function (u) {
          ((u.Button = "button"), (u.Slot = "slot"));
        })(ru || (ru = {}));
        const nu = () => {},
          au = o().memo(
            ({
              active: u = !1,
              className: e,
              children: t,
              toggleType: r = ru.Button,
              toggleButtonType: n = Q.secondary,
              onClick: i,
              disabled: l,
              soundClick: s = "play",
              soundHover: c = "highlight",
              onMouseEnter: E = nu,
              onMouseDown: A = nu,
              onMouseUp: _ = nu,
              onMouseLeave: F = nu,
            }) => {
              const m = (0, a.useCallback)(
                  (e) => {
                    l || (uu(s), i && i(e, u));
                  },
                  [i, l, u, s],
                ),
                d = (0, a.useCallback)(
                  (u) => {
                    l || (uu(c), E && E(u));
                  },
                  [l, c, E],
                ),
                D = (0, a.useCallback)(
                  (u) => {
                    l || ((1 !== u.button && 2 !== u.button) || (null !== s && uu(s)), A && A(u));
                  },
                  [A, l, s],
                ),
                B = f()(tu.base, e, tu[`base__${r}`], u && tu.base__active, l && tu.base__disabled);
              return o().createElement(
                "div",
                {
                  className: B,
                  onClick: m,
                  onMouseEnter: d,
                  onMouseUp: l ? nu : _,
                  onMouseDown: D,
                  onMouseLeave: l ? nu : F,
                },
                o().createElement("div", { className: tu.content }, t),
                r === ru.Button &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement("div", {
                      className: f()(tu.background, tu[`background__${n}`]),
                    }),
                    o().createElement("div", { className: tu.texture }),
                  ),
                o().createElement("div", { className: tu.overlay }),
                o().createElement("div", { className: tu.indicator }),
              );
            },
          );
        var ou = t(4179);
        const iu = [
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
        function lu(u) {
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
        const su = (u, e, t = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: ou.B0.TOOLTIP,
                  contentID: u,
                  decoratorID: e,
                  targetID: r,
                },
                t,
              ),
            );
          },
          cu = (u) => {
            let e = u.children,
              t = u.contentId,
              r = u.args,
              n = u.onMouseEnter,
              o = u.onMouseLeave,
              i = u.onMouseDown,
              l = u.onClick,
              s = u.ignoreShowDelay,
              c = void 0 !== s && s,
              E = u.ignoreMouseClick,
              A = void 0 !== E && E,
              _ = u.decoratorId,
              F = void 0 === _ ? 0 : _,
              m = u.isEnabled,
              d = void 0 === m || m,
              D = u.targetId,
              B = void 0 === D ? 0 : D,
              C = u.onShow,
              g = u.onHide,
              h = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, iu);
            const f = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              v = (0, a.useMemo)(
                () =>
                  B ||
                  ((u = 1) => {
                    const e = new Error().stack;
                    let t,
                      r = R.invalid("resId");
                    return (
                      e &&
                        ((t = e.split("\n")[u].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== t &&
                          window.subViews[t] &&
                          (r = window.subViews[t].id)),
                      { caller: t, stack: e, resId: r }
                    );
                  })().resId,
                [B],
              ),
              p = (0, a.useCallback)(() => {
                (f.current.isVisible && f.current.timeoutId) ||
                  (su(t, F, { isMouseEvent: !0, on: !0, arguments: lu(r) }, v),
                  C && C(),
                  (f.current.isVisible = !0));
              }, [t, F, r, v, C]),
              b = (0, a.useCallback)(() => {
                if (f.current.isVisible || f.current.timeoutId) {
                  const u = f.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (f.current.timeoutId = 0)),
                    su(t, F, { on: !1 }, v),
                    f.current.isVisible && g && g(),
                    (f.current.isVisible = !1));
                }
              }, [t, F, v, g]),
              w = (0, a.useCallback)((u) => {
                f.current.isVisible &&
                  ((f.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (f.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(f.current.prevTarget) && b();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const u = f.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    u && window.clearTimeout(u));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === d && b();
              }, [d, b]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", b),
                  () => {
                    (window.removeEventListener("mouseleave", b), b());
                  }
                ),
                [b],
              ));
            return d
              ? (0, a.cloneElement)(
                  e,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((f.current.timeoutId = window.setTimeout(p, c ? 100 : 400)),
                            n && n(u),
                            S && S(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (b(), null == o || o(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === A && b(), null == l || l(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === A && b(), null == i || i(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    h,
                  ),
                )
              : e;
            var S;
          },
          Eu = ["children", "body", "header", "note", "alert", "args"];
        function Au() {
          return (
            (Au =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Au.apply(this, arguments)
          );
        }
        const _u = R.views.common.tooltip_window.simple_tooltip_content,
          Fu = (u) => {
            let e = u.children,
              t = u.body,
              r = u.header,
              n = u.note,
              i = u.alert,
              l = u.args,
              s = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, Eu);
            const c = (0, a.useMemo)(() => {
              const u = Object.assign({}, l, { body: t, header: r, note: n, alert: i });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [i, t, r, n, l]);
            return o().createElement(
              cu,
              Au(
                {
                  contentId:
                    ((E = null == l ? void 0 : l.hasHtmlContent),
                    E ? _u.SimpleTooltipHtmlContent("resId") : _u.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                s,
              ),
              e,
            );
            var E;
          },
          mu = "FavoritesButton_base_1f",
          du = "FavoritesButton_button_45",
          Du = "FavoritesButton_icon_32",
          Bu = (0, W.Pi)(({ className: u }) => {
            const e = Z(),
              t = e.model,
              r = e.controls,
              n = t.root.get().favoritesFilter,
              a = r.onApplyFavoritesFilter;
            return o().createElement(
              "div",
              { id: "filter_favorites_button", className: f()(mu, u), onClick: a },
              o().createElement(
                Fu,
                {
                  header: R.strings.tank_carousel_filter.tooltip.favorite.header(),
                  body: R.strings.tank_carousel_filter.tooltip.favorite.body(),
                },
                o().createElement(
                  "div",
                  null,
                  o().createElement(
                    au,
                    { active: n, className: du, toggleButtonType: Q.primary },
                    o().createElement("div", { className: Du }),
                  ),
                ),
              ),
            );
          }),
          Cu = "FiltersBlock_base_72",
          gu = "FiltersBlock_button_6a",
          hu = {
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
          fu = ({
            children: u,
            size: e,
            isFocused: t,
            type: r,
            disabled: n,
            mixClass: i,
            soundHover: l,
            soundClick: s,
            onMouseEnter: c,
            onMouseMove: E,
            onMouseDown: A,
            onMouseUp: _,
            onMouseLeave: F,
            onClick: m,
          }) => {
            const d = (0, a.useRef)(null),
              D = (0, a.useState)(t),
              B = D[0],
              C = D[1],
              g = (0, a.useState)(!1),
              h = g[0],
              v = g[1],
              p = (0, a.useState)(!1),
              b = p[0],
              w = p[1],
              S = (0, a.useCallback)(() => {
                n || (d.current && (d.current.focus(), C(!0)));
              }, [n]),
              x = (0, a.useCallback)(
                (u) => {
                  B && null !== d.current && !d.current.contains(u.target) && C(!1);
                },
                [B],
              ),
              y = (0, a.useCallback)(
                (u) => {
                  n || (m && m(u));
                },
                [n, m],
              ),
              M = (0, a.useCallback)(
                (u) => {
                  n || (null !== l && uu(l), c && c(u), w(!0));
                },
                [n, l, c],
              ),
              L = (0, a.useCallback)(
                (u) => {
                  E && E(u);
                },
                [E],
              ),
              T = (0, a.useCallback)(
                (u) => {
                  n || (_ && _(u), v(!1));
                },
                [n, _],
              ),
              O = (0, a.useCallback)(
                (u) => {
                  n || (null !== s && uu(s), A && A(u), t && S(), v(!0));
                },
                [n, s, A, S, t],
              ),
              k = (0, a.useCallback)(
                (u) => {
                  n || (F && F(u), v(!1));
                },
                [n, F],
              ),
              P = f()(
                hu.base,
                hu[`base__${r}`],
                {
                  [hu.base__disabled]: n,
                  [hu[`base__${e}`]]: e,
                  [hu.base__focus]: B,
                  [hu.base__highlightActive]: h,
                  [hu.base__firstHover]: b,
                },
                i,
              ),
              N = f()(hu.state, hu.state__default);
            return (
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mousedown", x),
                  () => {
                    document.removeEventListener("mousedown", x);
                  }
                ),
                [x],
              ),
              (0, a.useEffect)(() => {
                C(t);
              }, [t]),
              o().createElement(
                "div",
                {
                  ref: d,
                  className: P,
                  onMouseEnter: M,
                  onMouseMove: L,
                  onMouseUp: T,
                  onMouseDown: O,
                  onMouseLeave: k,
                  onClick: y,
                },
                r !== Q.ghost &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement("div", { className: hu.back }),
                    o().createElement("span", { className: hu.texture }),
                  ),
                o().createElement(
                  "span",
                  { className: N },
                  o().createElement("span", { className: hu.stateDisabled }),
                  o().createElement("span", { className: hu.stateHighlightHover }),
                  o().createElement("span", { className: hu.stateHighlightActive }),
                ),
                o().createElement(
                  "span",
                  { className: hu.content, lang: R.strings.settings.LANGUAGE_CODE() },
                  u,
                ),
              )
            );
          };
        fu.defaultProps = {
          type: Q.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const vu = (0, a.memo)(fu),
          pu = (u) => {
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
          },
          bu = (u) => {
            (0, a.useEffect)(u, []);
          },
          wu = {
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
        var Su;
        !(function (u) {
          ((u[(u.Left = 0)] = "Left"),
            (u[(u.Right = 1)] = "Right"),
            (u[(u.Top = 2)] = "Top"),
            (u[(u.Bottom = 3)] = "Bottom"));
        })(Su || (Su = {}));
        const xu = ["__left", "__right", "__top", "__bottom"],
          yu =
            ((0, a.forwardRef)(
              (
                { children: u, disableAutoSizeUpdate: e, onOutsideClick: t, customStyles: r = {} },
                n,
              ) => {
                const i = (0, a.useRef)(null),
                  s = (0, a.useRef)(null),
                  c = (0, a.useRef)(null),
                  E = (0, a.useState)(window.decorator && window.decorator.directionType),
                  A = E[0],
                  _ = E[1],
                  F = (0, a.useCallback)(() => {
                    (eu.playClick(), l.O.view.sendEvent.close());
                  }, []),
                  m = (0, a.useCallback)(() => {
                    eu.playHighlight();
                  }, []),
                  d = f()(wu.arrow, wu[`arrow${xu[A]}`]);
                bu(
                  () => (
                    l.O.client.events.mouse.enableOutside(),
                    l.O.client.events.mouse.down(([, u]) => {
                      "outside" === u && (t ? t() : l.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const D = (0, a.useCallback)(
                    (u) => {
                      let e = u.target;
                      do {
                        if (e === i.current || e === c.current) return;
                        e = e.parentNode;
                      } while (e);
                      const r = window.decorator;
                      if (void 0 !== window.decorator) {
                        const u = l.O.client.getMouseGlobalPosition(),
                          e = ![r.boundX, r.boundY, r.boundWidth, r.boundHeight].includes(void 0),
                          t =
                            u.x < r.boundX ||
                            u.x > r.boundX + r.boundWidth ||
                            u.y > r.boundY + r.boundHeight ||
                            u.y < r.boundY;
                        if (e && !t) return;
                      }
                      t ? t() : l.O.view.sendEvent.close("popover");
                    },
                    [i, c, t],
                  ),
                  B = (0, a.useCallback)(
                    () => (
                      l.O.view.freezeTextureBeforeResize(),
                      pu(() => {
                        if (s.current) {
                          const u = s.current.scrollWidth,
                            e = s.current.scrollHeight;
                          (l.O.view.resize(u, e), _(window.decorator.directionType));
                        }
                      })
                    ),
                    [],
                  );
                return (
                  (0, a.useImperativeHandle)(n, () => ({ updateSize: B })),
                  bu(() => {
                    l.O.view.setInputPaddingsRem(58);
                  }),
                  (0, a.useEffect)(() => {
                    document.addEventListener("mousedown", D, { capture: !0 });
                    const u = ((u) => {
                      let e = !1;
                      return {
                        promise: new Promise((t, r) => {
                          u.then((u) => !e && t(u)).catch((u) => !e && r(u));
                        }),
                        cancel() {
                          e = !0;
                        },
                      };
                    })((0, ou.Eu)());
                    return (
                      !e && u.promise.then(() => B()),
                      () => {
                        (u.cancel(), document.removeEventListener("mousedown", D));
                      }
                    );
                  }, [B, D, e]),
                  o().createElement(
                    "div",
                    { className: wu.base, ref: s },
                    o().createElement(
                      "div",
                      { className: wu.decorator },
                      o().createElement(
                        "div",
                        { className: wu.content, ref: i },
                        u,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          o().createElement(
                            Fu,
                            { body: R.strings.dialogs.common.error.cancel() },
                            o().createElement("div", {
                              className: wu.closeBtn,
                              onClick: F,
                              onMouseEnter: m,
                              ref: c,
                            }),
                          ),
                      ),
                      o().createElement("div", { className: d, style: r.arrow }),
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
        function Mu() {
          return (
            (Mu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Mu.apply(this, arguments)
          );
        }
        const Lu = (u) => {
            let e = u.contentId,
              t = u.decoratorId,
              r = u.direction,
              n = void 0 === r ? Su.Top : r,
              i = u.targetId,
              l = u.args,
              s = u.onClick,
              c = u.children,
              E = u.isEnabled,
              A = void 0 === E || E,
              _ = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, yu);
            const F = (0, a.useRef)(null),
              m = (0, a.useCallback)(() => {
                if ((0, ou.wU)()) return (0, ou.SW)();
                F.current && (0, ou.P3)(e, n, F.current, t, i, l);
              }, [e, n, l, t, i]);
            return o().createElement(
              "div",
              Mu(
                {
                  ref: F,
                  onClick:
                    ((d = c.props.onClick),
                    (u) => {
                      A && (m(), s && s(u), d && d(u));
                    }),
                },
                _,
              ),
              c,
            );
            var d;
          },
          Ru = ["children"];
        function Tu() {
          return (
            (Tu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Tu.apply(this, arguments)
          );
        }
        const Ou = (u) => {
            let e = u.children,
              t = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, Ru);
            return o().createElement(
              Lu,
              Tu(
                {
                  decoratorId:
                    R.views.common.pop_over_window.backport_pop_over.BackportPopOverWindow("resId"),
                  contentId:
                    R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent(
                      "resId",
                    ),
                },
                t,
              ),
              e,
            );
          },
          ku = "FiltersButton_base_83",
          Pu = "FiltersButton_button_49",
          Nu = "FiltersButton_icon_b3",
          Hu = (0, W.Pi)(({ className: u }) => {
            const e = Z().model.root.get().isPopoverOpen;
            return o().createElement(
              "div",
              { id: "filters_button", className: f()(ku, u) },
              !e &&
                o().createElement(
                  Ou,
                  null,
                  o().createElement(
                    Fu,
                    {
                      header: R.strings.tank_carousel_filter.tooltip.params.header(),
                      body: R.strings.tank_carousel_filter.tooltip.params.body(),
                    },
                    o().createElement(
                      "div",
                      null,
                      o().createElement(
                        vu,
                        { type: Q.primary, mixClass: Pu, isFocused: e },
                        o().createElement("div", { className: Nu }),
                      ),
                    ),
                  ),
                ),
              e &&
                o().createElement(
                  Fu,
                  {
                    header: R.strings.tank_carousel_filter.tooltip.params.header(),
                    body: R.strings.tank_carousel_filter.tooltip.params.body(),
                  },
                  o().createElement(
                    "div",
                    null,
                    o().createElement(
                      vu,
                      { type: Q.primary, mixClass: Pu, isFocused: e },
                      o().createElement("div", { className: Nu }),
                    ),
                  ),
                ),
            );
          }),
          Iu = "RentedButton_base_71",
          Wu = "RentedButton_button_da",
          Vu = "RentedButton_icon_85",
          Gu = (0, W.Pi)(({ className: u }) => {
            const e = Z(),
              t = e.model,
              r = e.controls,
              n = t.root.get().rentedFilter,
              a = r.onApplyRentedFilter;
            return o().createElement(
              "div",
              { id: "filter_rented_button", className: f()(Iu, u), onClick: a },
              o().createElement(
                Fu,
                {
                  header: R.strings.tank_carousel_filter.tooltip.rented.header(),
                  body: R.strings.tank_carousel_filter.tooltip.rented.body(),
                },
                o().createElement(
                  "div",
                  null,
                  o().createElement(
                    au,
                    { active: n, className: Wu, toggleButtonType: Q.primary },
                    o().createElement("div", { className: Vu }),
                  ),
                ),
              ),
            );
          }),
          Uu = (0, W.Pi)(({ className: u }) => {
            const e = f()(u, Cu);
            return o().createElement(
              "div",
              { className: e },
              o().createElement(Hu, { className: f()(gu) }),
              o().createElement(Gu, { className: f()(gu) }),
              o().createElement(Bu, { className: f()(gu) }),
            );
          });
        var zu = t(9887),
          ju = t.n(zu);
        const Xu = ["xl", "lg", "md", "sm", "xs"],
          $u = (u) => u.includes("_") && ((u) => Xu.includes(u))(u.split("_").at(-1)),
          Ku = [b.ExtraLarge, b.Large, b.Medium, b.Small, b.ExtraSmall],
          Yu = (u, e) =>
            Object.keys(u).reduce((t, r) => {
              if (r in t) return t;
              if ($u(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const a = Ku.indexOf(e),
                  o = (-1 !== a ? Xu.slice(a) : [])
                    .map((u) => n + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  i = o ? u[o] : void 0;
                return ((t[n] = void 0 !== i ? i : u[n]), t);
              }
              const n = u[r];
              return (
                void 0 === n ||
                  ((u, e) => Xu.some((t) => void 0 !== e[`${u}_${t}`]))(r, u) ||
                  (t[r] = n),
                t
              );
            }, {}),
          qu = (u, e = Yu) => {
            const t = (
              (u, e = Yu) =>
              (t) => {
                const r = x().mediaSize,
                  n = (0, a.useMemo)(() => e(t, r), [t, r]);
                return o().createElement(u, n);
              }
            )(u, e);
            return o().memo((e) =>
              Object.keys(e).some((u) => $u(u) && void 0 !== e[u])
                ? o().createElement(t, e)
                : o().createElement(u, e),
            );
          },
          Zu = {
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
          Qu = [
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
        function Ju() {
          return (
            (Ju =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Ju.apply(this, arguments)
          );
        }
        Object.keys(ju());
        const ue = {
            XL: { mt: Zu.mt__XL, mr: Zu.mr__XL, mb: Zu.mb__XL, ml: Zu.ml__XL },
            LG: { mt: Zu.mt__LG, mr: Zu.mr__LG, mb: Zu.mb__LG, ml: Zu.ml__LG },
            MDp: { mt: Zu.mt__MDp, mr: Zu.mr__MDp, mb: Zu.mb__MDp, ml: Zu.ml__MDp },
            MD: { mt: Zu.mt__MD, mr: Zu.mr__MD, mb: Zu.mb__MD, ml: Zu.ml__MD },
            SMp: { mt: Zu.mt__SMp, mr: Zu.mr__SMp, mb: Zu.mb__SMp, ml: Zu.ml__SMp },
            SM: { mt: Zu.mt__SM, mr: Zu.mr__SM, mb: Zu.mb__SM, ml: Zu.ml__SM },
            XS: { mt: Zu.mt__XS, mr: Zu.mr__XS, mb: Zu.mb__XS, ml: Zu.ml__XS },
          },
          ee = (Object.keys(ue), ["mt", "mr", "mb", "ml"]),
          te = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          re = qu((u) => {
            let e = u.className,
              t = u.width,
              r = u.height,
              n = u.m,
              i = u.mt,
              l = void 0 === i ? n : i,
              s = u.mr,
              c = void 0 === s ? n : s,
              E = u.mb,
              A = void 0 === E ? n : E,
              _ = u.ml,
              F = void 0 === _ ? n : _,
              m = u.column,
              d = u.row,
              D = u.flexDirection,
              B = void 0 === D ? (m ? "column" : d && "row") || void 0 : D,
              C = u.flexStart,
              g = u.center,
              h = u.flexEnd,
              v = u.spaceBetween,
              p = u.spaceAround,
              b = u.justifyContent,
              w =
                void 0 === b
                  ? (C ? "flex-start" : g && "center") ||
                    (h && "flex-end") ||
                    (v && "space-between") ||
                    (p && "space-around") ||
                    void 0
                  : b,
              S = u.alignItems,
              x =
                void 0 === S
                  ? (C ? "flex-start" : g && "center") || (h && "flex-end") || void 0
                  : S,
              y = u.alignSelf,
              M = u.wrap,
              L = u.flexWrap,
              R = void 0 === L ? (M ? "wrap" : void 0) : L,
              T = u.grow,
              O = u.shrink,
              k = u.flex,
              P = void 0 === k ? (T || O ? `${T ? 1 : 0} ${O ? 1 : 0} auto` : void 0) : k,
              N = u.style,
              H = u.children,
              I = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, Qu);
            const W = (0, a.useMemo)(() => {
                const u = { mt: l, mr: c, mb: A, ml: F },
                  e = ((u) =>
                    ee.reduce((e, t) => {
                      const r = u[t];
                      return r && "number" != typeof r ? e.concat(ue[!0 === r ? "MD" : r][t]) : e;
                    }, []))(u),
                  n = ((u) =>
                    ee.reduce((e, t) => {
                      const r = u[t];
                      return ("number" == typeof r && (e[te[t]] = r + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, N, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: P,
                    alignSelf: y,
                    display: B || x ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: R,
                    justifyContent: w,
                    alignItems: x,
                  }),
                  computedClassNames: e,
                };
              }, [t, r, l, c, A, F, N, P, y, B, R, w, x]),
              V = W.computedStyle,
              G = W.computedClassNames;
            return o().createElement(
              "div",
              Ju({ className: f()(Zu.base, ...G, e), style: V }, I),
              H,
            );
          });
        let ne;
        function ae(u) {
          return u.replace(/-/g, "_");
        }
        !(function (u) {
          ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
        })(ne || (ne = {}));
        const oe = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          ie = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          le = (u, e, t = ne.left) => u.split(e).reduce(t === ne.left ? oe : ie, []),
          se = (() => {
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
          ce = ["zh_cn", "zh_sg", "zh_tw"],
          Ee = (u, e = ne.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return ce.includes(t)
              ? se(u)
              : ((u, e = ne.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = u.replace(/&nbsp;/g, " ");
                  return (le(n, /( )/, e).forEach((u) => (t = t.concat(le(u, r, ne.left)))), t);
                })(u, e);
          },
          Ae = "FormatText_base_d0",
          _e = ({ binding: u, text: e = "", classMix: t, alignment: r = ne.left }) =>
            null === e
              ? (console.error("FormatText was supplied with 'null'"), null)
              : o().createElement(
                  a.Fragment,
                  null,
                  e.split("\n").map((e, n) =>
                    o().createElement(
                      "div",
                      { className: f()(Ae, t), key: `${e}-${n}` },
                      ((u, e, t) =>
                        u
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((u) => (t && u in t ? t[u] : Ee(u, e))))(e, r, u).map((u, e) =>
                        o().createElement(a.Fragment, { key: `${e}-${u}` }, u),
                      ),
                    ),
                  ),
                );
        var Fe = t(3532),
          me = t.n(Fe);
        const de = {
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
          De = [
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
        function Be() {
          return (
            (Be =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Be.apply(this, arguments)
          );
        }
        Object.keys(ju());
        const Ce = Object.keys(me()),
          ge = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          he = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          fe = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          ve = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          pe =
            (Object.keys(ve),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": ge,
              "heading-H36": ge,
              "heading-H28": he,
              "heading-H24": he,
              "heading-H24R": he,
              "heading-H22": he,
              "heading-H20R": he,
              "heading-H18": he,
              "heading-H15": fe,
              "heading-H14": fe,
              "paragraph-P24": he,
              "paragraph-P18": he,
              "paragraph-P16": he,
              "paragraph-P14": fe,
              "paragraph-P12": fe,
              "paragraph-P10": fe,
            }),
          be =
            (Object.keys(pe),
            (u) =>
              u
                ? ((u) => Ce.includes(u))(u)
                  ? { colorClassName: de[u] }
                  : { colorStyle: { color: u } }
                : {}),
          we = qu((u) => {
            let e = u.text,
              t = u.variant,
              r = u.className,
              n = u.color,
              i = u.m,
              l = u.mt,
              s = void 0 === l ? i : l,
              c = u.mr,
              E = void 0 === c ? i : c,
              A = u.mb,
              _ = void 0 === A ? i : A,
              F = u.ml,
              m = void 0 === F ? i : F,
              d = u.style,
              D = u.format,
              B = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, De);
            const C = (0, a.useMemo)(() => {
                const u = be(n),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, d, r), colorClassName: e };
              }, [d, n]),
              g = C.computedStyle,
              h = C.colorClassName;
            return o().createElement(
              re,
              Be(
                {
                  className: f()(de.base, t && de[t], h, r),
                  style: g,
                  mt: !0 === s ? pe[t || "paragraph-P16"].mt : s,
                  mr: !0 === E ? pe[t || "paragraph-P16"].mr : E,
                  mb: !0 === _ ? pe[t || "paragraph-P16"].mb : _,
                  ml: !0 === m ? pe[t || "paragraph-P16"].ml : m,
                },
                B,
              ),
              void 0 !== D ? o().createElement(_e, Be({}, D, { text: e })) : e,
            );
          }),
          Se = "PopoverInfoBlock_base_50",
          xe = "PopoverInfoBlock_base__invisible_a3",
          ye = "PopoverInfoBlock_counter_a5",
          Me = "PopoverInfoBlock_divider_58",
          Le = "PopoverInfoBlock_glow_af",
          Re = "PopoverInfoBlock_button_df",
          Te = "PopoverInfoBlock_icon_6d",
          Oe = (0, W.Pi)(({ className: u }) => {
            const e = Z(),
              t = e.model,
              r = e.controls,
              n = t.computes,
              i = t.root.get().isPopoverOpen,
              l = n.getVehicleItems(),
              s = (0, a.useState)(l),
              c = s[0],
              E = s[1];
            (0, a.useEffect)(() => {
              E(l.filter((u) => u.isVisible));
            }, [l]);
            const A = 0 === c.length;
            return o().createElement(
              "div",
              { className: f()(Se, u, (i || l.length === c.length) && xe) },
              o().createElement("div", { className: Le }),
              o().createElement(
                "div",
                { className: ye },
                o().createElement(we, {
                  text: String(c.length),
                  variant: "paragraph-P16",
                  color: A ? "RED" : "WHITE",
                }),
                o().createElement(we, {
                  text: "/",
                  variant: "paragraph-P16",
                  className: Me,
                  color: "BOND",
                }),
                o().createElement(we, {
                  text: String(l.length),
                  variant: "paragraph-P16",
                  color: "BOND",
                }),
                o().createElement(
                  Fu,
                  V,
                  o().createElement(
                    vu,
                    { mixClass: Re, onClick: r.onClearFilters, type: Q.ghost, size: J.small },
                    o().createElement("div", { className: Te }),
                  ),
                ),
              ),
            );
          }),
          ke = (u, e, t) => (t < u ? u : t > e ? e : t),
          Pe = [];
        function Ne(u) {
          const e = (0, a.useRef)(u);
          return (
            (0, a.useLayoutEffect)(() => {
              e.current = u;
            }),
            (0, a.useCallback)((...u) => (0, e.current)(...u), Pe)
          );
        }
        function He(u, e, t = []) {
          const r = (0, a.useRef)(0),
            n = (0, a.useCallback)(() => window.clearInterval(r.current), t || []);
          (0, a.useEffect)(() => n, [n]);
          const o = (null != t ? t : []).concat([e]);
          return [
            (0, a.useCallback)((t) => {
              ((r.current = window.setInterval(() => u(t, !0), e)), u(t, !1));
            }, o),
            n,
          ];
        }
        function Ie(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return We(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return We(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            t && (u = t);
            var r = 0;
            return function () {
              return r >= u.length ? { done: !0 } : { done: !1, value: u[r++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function We(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, r = new Array(e); t < e; t++) r[t] = u[t];
          return r;
        }
        function Ve(u, e, t) {
          const r = (0, a.useMemo)(
            () =>
              (function (u, e, t, r) {
                let n,
                  a = !1,
                  o = 0;
                function i() {
                  n && clearTimeout(n);
                }
                function l(...l) {
                  const s = this,
                    c = Date.now() - o;
                  function E() {
                    ((o = Date.now()), t.apply(s, l));
                  }
                  a ||
                    (r && !n && E(),
                    i(),
                    void 0 === r && c > u
                      ? E()
                      : !0 !== e &&
                        (n = setTimeout(
                          r
                            ? function () {
                                n = void 0;
                              }
                            : E,
                          void 0 === r ? u - c : u,
                        )));
                }
                return (
                  "boolean" != typeof e && ((r = t), (t = e), (e = void 0)),
                  (l.cancel = function () {
                    (i(), (a = !0));
                  }),
                  l
                );
              })(t, u),
            e,
          );
          return ((0, a.useEffect)(() => r.cancel, [r]), r);
        }
        var Ge = t(7030);
        let Ue;
        !(function (u) {
          ((u[(u.Next = -1)] = "Next"), (u[(u.Prev = 1)] = "Prev"));
        })(Ue || (Ue = {}));
        const ze = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          je = ({
            getContainerSize: u,
            getBounds: e,
            setScrollPosition: t,
            getDirection: r,
            getWrapperSize: n,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const i = (u, t) => {
              const r = e(u),
                n = r[0],
                a = r[1];
              return ke(n, a, t);
            };
            return (s = {}) => {
              const c = s.settings,
                E = void 0 === c ? ze : c,
                A = (0, a.useRef)(null),
                _ = (0, a.useRef)(null),
                F = (() => {
                  const u = (0, a.useMemo)(() => ({}), []),
                    e = (e) => (u[e] || (u[e] = new Map()), u[e]),
                    t = (u, t) => {
                      e(u).set(t, t);
                    },
                    r = (u, t) => {
                      e(u).delete(t);
                    },
                    n = (u, ...t) => {
                      for (var r, n = Ie(e(u).values()); !(r = n()).done;) (0, r.value)(...t);
                    };
                  return (0, a.useMemo)(() => ({ on: t, off: r, trigger: n }), []);
                })(),
                m = Ve(
                  () => {
                    l.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                d = (0, Ge.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (u) => {
                    const e = A.current;
                    e && (t(e, u), F.trigger("change", u), o && m());
                  },
                  onRest: (u) => F.trigger("rest", u),
                  onStart: (u) => F.trigger("start", u),
                  onPause: (u) => F.trigger("pause", u),
                })),
                D = d[0],
                B = d[1],
                C = (0, a.useCallback)(
                  (u, e, t) => {
                    var r;
                    const n = D.scrollPosition.get(),
                      a = (null != (r = D.scrollPosition.goal) ? r : 0) - n;
                    return i(u, e * t + a + n);
                  },
                  [D.scrollPosition],
                ),
                g = (0, a.useCallback)(
                  (u, { immediate: e = !1, reset: t = !0 } = {}) => {
                    const r = A.current;
                    r &&
                      B.start({
                        scrollPosition: i(r, u),
                        immediate: e,
                        reset: t,
                        config: E.animationConfig,
                        from: { scrollPosition: i(r, D.scrollPosition.get()) },
                      });
                  },
                  [B, E.animationConfig, D.scrollPosition],
                ),
                h = (0, a.useCallback)(
                  (u) => {
                    const e = A.current,
                      t = _.current;
                    if (!e || !t) return;
                    const r = ((u, e) => {
                        switch (e.type) {
                          case "proportional":
                            return n(u) / e.factor;
                          case "fixed":
                            return e.value;
                        }
                      })(t, E.step),
                      a = C(e, u, r);
                    g(a);
                  },
                  [g, C, E.step],
                ),
                f = (0, a.useCallback)(
                  (u) => {
                    (0 !== u.deltaY && h(r(u)),
                      A.current && F.trigger("mouseWheel", u, D.scrollPosition, e(A.current)));
                  },
                  [D.scrollPosition, h, F],
                ),
                v = ((u, e = []) => {
                  const t = (0, a.useRef)(),
                    r = (0, a.useCallback)((...e) => {
                      (t.current && t.current(), (t.current = u(...e)));
                    }, e);
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
                    pu(() => {
                      const u = A.current;
                      u &&
                        (g(i(u, D.scrollPosition.goal), { immediate: !0 }),
                        F.trigger("resizeHandled"));
                    }),
                  [g, D.scrollPosition.goal],
                ),
                p = Ne(() => {
                  const u = A.current;
                  if (!u) return;
                  const e = i(u, D.scrollPosition.goal);
                  (e !== D.scrollPosition.goal && g(e, { immediate: !0 }),
                    F.trigger("recalculateContent"));
                });
              (0, a.useEffect)(
                () => (
                  window.addEventListener("resize", v),
                  () => {
                    window.removeEventListener("resize", v);
                  }
                ),
                [v],
              );
              const b = (0, a.useCallback)((u) => F.trigger("isThumbDraggingChanged", u), [F]);
              return (0, a.useMemo)(
                () => ({
                  getWrapperSize: () => (_.current ? n(_.current) : void 0),
                  getContainerSize: () => (A.current ? u(A.current) : void 0),
                  getBounds: () =>
                    A.current
                      ? e(A.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: E.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: f,
                  applyScroll: g,
                  applyStepTo: h,
                  contentRef: A,
                  wrapperRef: _,
                  scrollPosition: B,
                  animationScroll: D,
                  recalculateContent: p,
                  handleIsThumbDragging: b,
                  events: { on: F.on, off: F.off },
                }),
                [D.scrollPosition, g, h, b, F.off, F.on, p, f, B, E.step.clampedArrowStepTimeout],
              );
            };
          },
          Xe = je({
            getBounds: (u) => {
              var e, t;
              return [
                0,
                u.offsetWidth -
                  (null != (e = null == (t = u.parentElement) ? void 0 : t.offsetWidth) ? e : 0),
              ];
            },
            getContainerSize: (u) => u.offsetWidth,
            getWrapperSize: (u) => u.offsetWidth,
            setScrollPosition: (u, e) => {
              u.style.transform = `translateX(-${e.value.scrollPosition}px)`;
            },
            getDirection: (u) => (u.deltaY > 1 ? Ue.Next : Ue.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          $e = "HorizontalBar_base_49",
          Ke = "HorizontalBar_base__nonActive_82",
          Ye = "HorizontalBar_leftButton_5f",
          qe = "HorizontalBar_rightButton_03",
          Ze = "HorizontalBar_track_0d",
          Qe = "HorizontalBar_thumb_fd",
          Je = "HorizontalBar_rail_32",
          ut = "disable",
          et = { pending: !1, offset: 0 },
          tt = (u) => {
            var e;
            return 0.9 * (null != (e = u.getWrapperSize()) ? e : 0);
          },
          rt = () => {},
          nt = (u, e) => Math.max(20, u.offsetWidth * e),
          at = (0, a.memo)(
            ({ api: u, classNames: e = {}, getStepByRailClick: t = tt, onDrag: r = rt }) => {
              const n = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                s = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = u.stepTimeout || 100,
                A = (0, a.useState)(et),
                _ = A[0],
                F = A[1],
                m = (0, a.useCallback)(
                  (u) => {
                    (F(u),
                      c.current &&
                        r({ type: u.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                d = () => {
                  const e = s.current,
                    t = c.current,
                    r = u.getWrapperSize(),
                    n = u.getContainerSize();
                  if (!(r && e && t && n)) return;
                  const a = u.animationScroll.scrollPosition.get(),
                    o = Math.min(1, r / n),
                    E = ke(0, 1, a / (n - r)),
                    A = (e.offsetWidth - nt(e, o)) * E;
                  ((t.style.transform = `translateX(${0 | A}px)`),
                    ((u) => {
                      if (i.current && l.current && s.current && c.current) {
                        if (0 === u)
                          return (i.current.classList.add(ut), void l.current.classList.remove(ut));
                        if (
                          ((e = s.current),
                          (t = c.current),
                          u - (e.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(ut), void l.current.classList.add(ut));
                        var e, t;
                        (i.current.classList.remove(ut), l.current.classList.remove(ut));
                      }
                    })(A));
                },
                D = Ne(() => {
                  ((() => {
                    const e = c.current,
                      t = s.current,
                      r = u.getWrapperSize(),
                      a = u.getContainerSize();
                    if (!(a && e && r && t)) return;
                    const o = Math.min(1, r / a);
                    ((e.style.width = `${nt(t, o)}px`),
                      (e.style.display = "flex"),
                      n.current &&
                        (1 === o ? n.current.classList.add(Ke) : n.current.classList.remove(Ke)));
                  })(),
                    d());
                });
              ((0, a.useEffect)(() => pu(D)),
                (0, a.useEffect)(
                  () =>
                    pu(() => {
                      const e = () => {
                        d();
                      };
                      let t = rt;
                      const r = () => {
                        (t(), (t = pu(D)));
                      };
                      return (
                        u.events.on("recalculateContent", D),
                        u.events.on("rest", e),
                        u.events.on("change", e),
                        u.events.on("resizeHandled", r),
                        () => {
                          (t(),
                            u.events.off("recalculateContent", D),
                            u.events.off("rest", e),
                            u.events.off("change", e),
                            u.events.off("resizeHandled", r));
                        }
                      );
                    }),
                  [u],
                ),
                (0, a.useEffect)(() => {
                  if (!_.pending) return;
                  const e = (e) => {
                      var t;
                      const n = u.contentRef.current;
                      if (!n) return;
                      const a = s.current,
                        o = c.current;
                      if (!n || !a || !o) return;
                      const i = e.screenX - _.offset - a.getBoundingClientRect().x,
                        l = (i / a.offsetWidth) * (null != (t = u.getContainerSize()) ? t : 0);
                      (u.scrollPosition.start({
                        scrollPosition: u.clampPosition(n, l),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: u.animationScroll.scrollPosition.get() },
                      }),
                        r({ type: "dragging", thumb: o, thumbOffset: i, contentOffset: l }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", e), m(et));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [u, _.offset, _.pending, r, m]));
              const B = He((e) => u.applyStepTo(e), E, [u]),
                C = B[0],
                g = B[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", g, !0),
                  () => document.removeEventListener("mouseup", g, !0)
                ),
                [g],
              );
              const h = (u) => {
                u.target.classList.contains(ut) || uu("highlight");
              };
              return o().createElement(
                "div",
                { className: f()($e, e.base), ref: n, onWheel: u.handleMouseWheel },
                o().createElement("div", {
                  className: f()(Ye, e.leftButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(ut) || 0 !== u.button || (uu("play"), C(Ue.Next));
                  },
                  onMouseUp: g,
                  ref: i,
                  onMouseEnter: h,
                }),
                o().createElement(
                  "div",
                  {
                    className: f()(Ze, e.track),
                    onMouseDown: (e) => {
                      const r = c.current;
                      if (r && 0 === e.button)
                        if ((uu("play"), e.target === r))
                          m({ pending: !0, offset: e.screenX - r.getBoundingClientRect().x });
                        else {
                          ((e) => {
                            const r = c.current,
                              n = u.contentRef.current;
                            if (!r || !n) return;
                            const a = t(u);
                            u.applyScroll(u.animationScroll.scrollPosition.get() + a * e);
                          })(e.screenX > r.getBoundingClientRect().x ? Ue.Prev : Ue.Next);
                        }
                    },
                    ref: s,
                    onMouseEnter: h,
                  },
                  o().createElement("div", { ref: c, className: f()(Qe, e.thumb) }),
                  o().createElement("div", { className: f()(Je, e.rail) }),
                ),
                o().createElement("div", {
                  className: f()(qe, e.rightButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(ut) || 0 !== u.button || (uu("play"), C(Ue.Prev));
                  },
                  onMouseUp: g,
                  ref: l,
                  onMouseEnter: h,
                }),
              );
            },
          ),
          ot = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          it = ({
            children: u,
            api: e,
            className: t,
            barClassNames: r,
            areaClassName: n,
            classNames: i,
            scrollClassName: l,
            getStepByRailClick: s,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const u = r || {};
                return Object.assign({}, u, { base: f()(ot.base, u.base) });
              }, [r]),
              A = (0, a.useMemo)(() => Object.assign({}, e, { handleMouseWheel: () => {} }), [e]);
            return o().createElement(
              "div",
              { className: f()(ot.defaultScroll, t), onWheel: e.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(ot.defaultScrollArea, n) },
                o().createElement(lt, { className: l, api: A, classNames: i }, u),
              ),
              o().createElement(at, { getStepByRailClick: s, api: e, onDrag: c, classNames: E }),
            );
          },
          lt = ({ api: u, className: e, classNames: t, children: r, style: n }) => (
            (0, a.useEffect)(() => pu(u.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(ot.base, e), style: n },
              o().createElement(
                "div",
                {
                  className: f()(ot.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: u.handleMouseWheel,
                  ref: u.wrapperRef,
                },
                o().createElement(
                  "div",
                  { className: f()(ot.content, null == t ? void 0 : t.content), ref: u.contentRef },
                  r,
                ),
              ),
            )
          );
        ((lt.Bar = at),
          (lt.Default = it),
          (lt.SeniorityAwards = ({ api: u, className: e, classNames: t, children: r }) => (
            (0, a.useEffect)(() => pu(u.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(ot.base, e) },
              o().createElement(
                "div",
                { className: f()(ot.wrapper, null == t ? void 0 : t.wrapper), ref: u.wrapperRef },
                o().createElement(
                  "div",
                  { className: f()(ot.content, null == t ? void 0 : t.content), ref: u.contentRef },
                  r,
                ),
              ),
            )
          )));
        const st = je({
            getBounds: (u) => [0, u.scrollHeight - u.offsetHeight],
            getContainerSize: (u) => u.scrollHeight,
            getWrapperSize: (u) => u.offsetHeight,
            setScrollPosition: (u, e) => {
              u.scrollTop = e.value.scrollPosition;
            },
            getDirection: (u) => (u.deltaY > 1 ? Ue.Next : Ue.Prev),
          }),
          ct = "VerticalBar_base_f3",
          Et = "VerticalBar_base__nonActive_42",
          At = "VerticalBar_topButton_d7",
          _t = "VerticalBar_bottomButton_06",
          Ft = "VerticalBar_track_df",
          mt = "VerticalBar_thumb_32",
          dt = "VerticalBar_rail_43",
          Dt = "disable",
          Bt = () => {},
          Ct = { pending: !1, offset: 0 },
          gt = (u) => {
            var e;
            return 0.9 * (null != (e = u.getWrapperSize()) ? e : 0);
          },
          ht = (u, e) => {
            u.contentRef.current && e(u.contentRef.current);
          },
          ft = (u, e) => Math.max(20, u.offsetHeight * e),
          vt = (0, a.memo)(
            ({ api: u, classNames: e = {}, getStepByRailClick: t = gt, onDrag: r = Bt }) => {
              const n = (0, a.useRef)(null),
                i = (0, a.useRef)(null),
                l = (0, a.useRef)(null),
                s = (0, a.useRef)(null),
                c = (0, a.useRef)(null),
                E = u.stepTimeout || 100,
                A = (0, a.useState)(Ct),
                _ = A[0],
                F = A[1],
                m = (0, a.useCallback)(
                  (u) => {
                    (F(u),
                      c.current &&
                        r({ type: u.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                d = Ne(() => {
                  const e = c.current,
                    t = s.current,
                    r = u.getWrapperSize(),
                    a = u.getContainerSize();
                  if (!(r && a && e && t)) return;
                  const o = Math.min(1, r / a);
                  return (
                    (e.style.height = `${ft(t, o)}px`),
                    e.classList.add(mt),
                    n.current &&
                      (1 === o ? n.current.classList.add(Et) : n.current.classList.remove(Et)),
                    o
                  );
                }),
                D = Ne(() => {
                  const e = s.current,
                    t = c.current,
                    r = u.getWrapperSize(),
                    n = u.getContainerSize();
                  if (!(r && e && t && n)) return;
                  const a = u.animationScroll.scrollPosition.get(),
                    o = Math.min(1, r / n),
                    E = ke(0, 1, a / (n - r)),
                    A = (e.offsetHeight - ft(e, o)) * E;
                  ((t.style.transform = `translateY(${0 | A}px)`),
                    ((u) => {
                      if (i.current && l.current && s.current && c.current) {
                        if (0 === u)
                          return (i.current.classList.add(Dt), void l.current.classList.remove(Dt));
                        if (
                          ((e = s.current),
                          (t = c.current),
                          u - (e.offsetHeight - t.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(Dt), void l.current.classList.add(Dt));
                        var e, t;
                        (i.current.classList.remove(Dt), l.current.classList.remove(Dt));
                      }
                    })(A));
                }),
                B = Ne(() => {
                  ht(u, () => {
                    (d(), D());
                  });
                });
              ((0, a.useEffect)(() => pu(B)),
                (0, a.useEffect)(() => {
                  const e = () => {
                    ht(u, () => {
                      D();
                    });
                  };
                  let t = Bt;
                  const r = () => {
                    (t(), (t = pu(B)));
                  };
                  return (
                    u.events.on("recalculateContent", B),
                    u.events.on("rest", e),
                    u.events.on("change", e),
                    u.events.on("resizeHandled", r),
                    () => {
                      (t(),
                        u.events.off("recalculateContent", B),
                        u.events.off("rest", e),
                        u.events.off("change", e),
                        u.events.off("resizeHandled", r));
                    }
                  );
                }, [u]),
                (0, a.useEffect)(() => {
                  if (!_.pending) return;
                  const e = (e) => {
                      ht(u, (t) => {
                        const n = s.current,
                          a = c.current,
                          o = u.getContainerSize();
                        if (!n || !a || !o) return;
                        const i = e.screenY - _.offset - n.getBoundingClientRect().y,
                          l = (i / n.offsetHeight) * o;
                        (u.scrollPosition.start({
                          scrollPosition: u.clampPosition(t, l),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: t.scrollTop },
                        }),
                          r({ type: "dragging", thumb: a, thumbOffset: i, contentOffset: l }));
                      });
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", e),
                        u.handleIsThumbDragging(!1),
                        m(Ct));
                    };
                  return (
                    window.addEventListener("mousemove", e),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", e),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [u, _.offset, _.pending, r, m]));
              const C = He((e) => u.applyStepTo(e), E, [u]),
                g = C[0],
                h = C[1];
              (0, a.useEffect)(
                () => (
                  document.addEventListener("mouseup", h, !0),
                  () => document.removeEventListener("mouseup", h, !0)
                ),
                [h],
              );
              const v = (u) => {
                u.target.classList.contains(Dt) || uu("highlight");
              };
              return o().createElement(
                "div",
                { className: f()(ct, e.base), ref: n, onWheel: u.handleMouseWheel },
                o().createElement("div", {
                  className: f()(At, e.topButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(Dt) || 0 !== u.button || (uu("play"), g(Ue.Next));
                  },
                  ref: i,
                  onMouseEnter: v,
                }),
                o().createElement(
                  "div",
                  {
                    className: f()(Ft, e.track),
                    onMouseDown: (e) => {
                      const r = c.current;
                      if (r && 0 === e.button)
                        if ((uu("play"), e.target === r))
                          (u.handleIsThumbDragging(!0),
                            m({ pending: !0, offset: e.screenY - r.getBoundingClientRect().y }));
                        else {
                          ((e) => {
                            c.current &&
                              ht(u, (r) => {
                                if (!r) return;
                                const n = t(u),
                                  a = u.clampPosition(r, r.scrollTop + n * e);
                                u.applyScroll(a);
                              });
                          })(e.screenY > r.getBoundingClientRect().y ? Ue.Prev : Ue.Next);
                        }
                    },
                    ref: s,
                    onMouseEnter: v,
                  },
                  o().createElement("div", { ref: c, className: e.thumb }),
                  o().createElement("div", { className: f()(dt, e.rail) }),
                ),
                o().createElement("div", {
                  className: f()(_t, e.bottomButton),
                  onMouseDown: (u) => {
                    u.target.classList.contains(Dt) || 0 !== u.button || (uu("play"), g(Ue.Prev));
                  },
                  onMouseUp: h,
                  ref: l,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          pt = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          bt = ({
            children: u,
            api: e,
            className: t,
            barClassNames: r,
            areaClassName: n,
            scrollClassName: i,
            scrollClassNames: l,
            getStepByRailClick: s,
            onDrag: c,
          }) => {
            const E = (0, a.useMemo)(() => {
                const u = r || {};
                return Object.assign({}, u, { base: f()(pt.base, u.base) });
              }, [r]),
              A = (0, a.useMemo)(() => Object.assign({}, e, { handleMouseWheel: () => {} }), [e]);
            return o().createElement(
              "div",
              { className: f()(pt.defaultScroll, t), onWheel: e.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(pt.area, n) },
                o().createElement(wt, { className: i, classNames: l, api: A }, u),
              ),
              o().createElement(vt, { getStepByRailClick: s, api: e, onDrag: c, classNames: E }),
            );
          },
          wt = ({ className: u, classNames: e, children: t, api: r }) => (
            (0, a.useEffect)(() => pu(r.recalculateContent)),
            o().createElement(
              "div",
              { className: f()(pt.base, u), ref: r.wrapperRef, onWheel: r.handleMouseWheel },
              o().createElement(
                "div",
                { className: f()(pt.content, null == e ? void 0 : e.content), ref: r.contentRef },
                t,
              ),
            )
          );
        wt.Default = bt;
        const St = { Vertical: n, Horizontal: r },
          xt = { type: "idle" };
        const yt = "VehiclesBlock_base_24",
          Mt = "VehiclesBlock_base__textMessage_5b",
          Lt = "VehiclesBlock_prev_29",
          Rt = "VehiclesBlock_next_46",
          Tt = "VehiclesBlock_prev__hovered_8c",
          Ot = "VehiclesBlock_next__hovered_db",
          kt = "VehiclesBlock_prev__disabled_6a",
          Pt = "VehiclesBlock_next__disabled_ca",
          Nt = "VehiclesBlock_content_e9",
          Ht = "VehiclesBlock_scrollContainer_c8",
          It = "VehiclesBlock_horizontalWrapper_95",
          Wt = "VehiclesBlock_scroll_83",
          Vt = "VehiclesBlock_noFilteredVehiclesMessage_32",
          Gt = {
            base: "VehicleSlot_base_c0",
            base__small: "VehicleSlot_base__small_63",
            frame: "VehicleSlot_frame_9d",
            frame__hover: "VehicleSlot_frame__hover_01",
            frame__small: "VehicleSlot_frame__small_ca",
            highlightFrame: "VehicleSlot_highlightFrame_0e",
            highlightCircle: "VehicleSlot_highlightCircle_5c",
            shadow: "VehicleSlot_shadow_34",
            shadow__hover: "VehicleSlot_shadow__hover_4a",
            vehicle: "VehicleSlot_vehicle_c9",
            vehicle__small: "VehicleSlot_vehicle__small_27",
            vehicle__selected: "VehicleSlot_vehicle__selected_7f",
            vehicleWrapper: "VehicleSlot_vehicleWrapper_97",
            vehicleTypeIcon: "VehicleSlot_vehicleTypeIcon_99",
            vehicleTypeIcon__small: "VehicleSlot_vehicleTypeIcon__small_d6",
            vehicleRoleIcon: "VehicleSlot_vehicleRoleIcon_91",
            vehicleRoleIcon__small: "VehicleSlot_vehicleRoleIcon__small_af",
            flag: "VehicleSlot_flag_f0",
            flag__small: "VehicleSlot_flag__small_b8",
            vehicleIcon: "VehicleSlot_vehicleIcon_19",
            vehicleIcon__small: "VehicleSlot_vehicleIcon__small_49",
            favorite: "VehicleSlot_favorite_4f",
            favorite__small: "VehicleSlot_favorite__small_7a",
          },
          Ut = R.images.gui.maps.icons,
          zt = (0, W.Pi)(function ({
            name: u,
            techName: e,
            type: t,
            nation: r,
            roleKey: n,
            vehicleCD: i,
            clickEvent: l,
            isSelected: s,
            isFavorite: c,
          }) {
            const E = Z().model.root.get().isDualRow,
              A = (0, a.useState)(E),
              _ = A[0],
              F = A[1];
            (0, a.useEffect)(() => {
              F(E);
            }, [E]);
            const m = (0, a.useState)(!1),
              d = m[0],
              D = m[1],
              B = (0, a.useCallback)(() => {
                (eu.playHighlight(), D(!0));
              }, []),
              C = (0, a.useCallback)(() => D(!1), []),
              g = (0, a.useCallback)(() => {
                (l(i), eu.playClick());
              }, [l, i]),
              h = _ ? Ut.vehicleTypes.battleCarousel.small : Ut.vehicleTypes.battleCarousel.big,
              v = (0, a.useMemo)(() => ({ backgroundImage: `url(${h.$dyn(ae(t))})` }), [t, h]),
              p = _ ? Ut.roleExp.roles.c_14x14 : Ut.roleExp.roles.c_22x22,
              b = (0, a.useMemo)(() => ({ backgroundImage: `url(${p.$dyn(n)})` }), [n, p]),
              w = _ ? Ut.flags.c_158x33 : Ut.flags.c_160x100,
              S = (0, a.useMemo)(() => ({ backgroundImage: `url(${w.$dyn(r)})` }), [r, w]),
              x = _
                ? "R.images.gui.maps.icons.library.favorite_small"
                : "R.images.gui.maps.icons.tooltip.main_type",
              y = (0, a.useMemo)(() => ({ backgroundImage: `url(${x})` }), [x]),
              M = _ ? Ut.vehicle.small : Ut.vehicle,
              L = (0, a.useMemo)(
                () => ({ backgroundImage: `url(${M.$dyn(ae(`${r}-${e}`))})` }),
                [r, e, M],
              );
            return o().createElement(
              "div",
              {
                id: "vehicleSlot",
                onMouseEnter: B,
                onMouseLeave: C,
                onClick: g,
                className: f()(Gt.base, _ && Gt.base__small),
              },
              s &&
                o().createElement("div", {
                  className: f()(Gt.highlightFrame, _ && Gt.highlightFrame__small),
                }),
              s &&
                o().createElement("div", {
                  className: f()(Gt.highlightCircle, _ && Gt.highlightCircle__small),
                }),
              o().createElement(
                "div",
                { className: Gt.vehicleWrapper },
                o().createElement("div", {
                  style: S,
                  className: f()(Gt.flag, _ && Gt.flag__small),
                }),
                o().createElement("div", {
                  style: L,
                  className: f()(Gt.vehicleIcon, _ && Gt.vehicleIcon__small),
                }),
              ),
              o().createElement(
                "div",
                null,
                o().createElement("div", {
                  style: v,
                  className: f()(Gt.vehicleTypeIcon, _ && Gt.vehicleTypeIcon__small),
                }),
                o().createElement("div", {
                  style: b,
                  className: f()(Gt.vehicleRoleIcon, _ && Gt.vehicleRoleIcon__small),
                }),
              ),
              !s && o().createElement("div", { className: f()(Gt.shadow, d && Gt.shadow__hover) }),
              c &&
                o().createElement("div", {
                  style: y,
                  className: f()(Gt.favorite, _ && Gt.favorite__small),
                }),
              o().createElement(
                "div",
                { className: f()(Gt.vehicle, _ && Gt.vehicle__small, s && Gt.vehicle__selected) },
                u,
              ),
              o().createElement("div", {
                className: f()(Gt.frame, d && Gt.frame__hover, _ && Gt.frame__small),
              }),
            );
          });
        function jt() {
          return (
            (jt =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            jt.apply(this, arguments)
          );
        }
        const Xt = (0, W.Pi)(function ({ className: u }) {
            const e = Z(),
              t = e.model,
              r = e.controls,
              n = r.onClickVehicle,
              i = r.onSetDualRow,
              s = t.computes,
              c = s.getVehicleItems(),
              E = s.selectedIndex(),
              A = t.root.get().isDualRow,
              _ = (0, a.useState)(c),
              F = _[0],
              m = _[1],
              d = x().mediaSize,
              D = (0, a.useState)(A),
              B = D[0],
              C = D[1],
              g = (0, a.useState)(!1),
              h = g[0],
              v = g[1],
              p = (0, a.useState)(!1),
              w = p[0],
              S = p[1],
              y = (0, a.useState)(viewEnv.getViewSizeRem().width),
              M = y[0],
              L = y[1];
            ((0, a.useEffect)(() => {
              const u = (u) => {
                L(u.width);
              };
              return (
                engine.on("screenResized", u),
                () => {
                  engine.off("screenResized", u);
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                d < b.Medium && i();
              }, [d, i]));
            const T = (0, a.useState)(M - 136),
              O = T[0],
              k = T[1];
            (0, a.useEffect)(() => {
              k(M - 136);
            }, [M]);
            const P = O > 170 * (B ? (F.length + 1) / 2 : F.length),
              N = (0, a.useCallback)(() => {
                (eu.playHighlight(), v(!0));
              }, []),
              H = (0, a.useCallback)(() => v(!1), []),
              I = (0, a.useCallback)(() => {
                (eu.playHighlight(), S(!0));
              }, []),
              W = (0, a.useCallback)(() => S(!1), []);
            ((0, a.useEffect)(() => {
              m(c.filter((u) => u.isVisible));
            }, [c]),
              (0, a.useEffect)(() => {
                C(A);
              }, [A]));
            const V = (0, a.useMemo)(
                () => ({
                  settings: {
                    step: { type: "fixed", value: 170, clampedArrowStepTimeout: 0.3 },
                    animationConfig: { frequency: 0.5 },
                  },
                }),
                [],
              ),
              G = Xe(V),
              U = (0, a.useState)(E),
              z = U[0],
              j = U[1],
              X = (0, a.useState)(0),
              $ = X[0],
              K = X[1],
              Y = (0, a.useState)([0, 0]),
              q = Y[0],
              Q = Y[1],
              J = { left: q[0], right: q[1] };
            (!(function (u, e, t) {
              const r = u.contentRef,
                n = u.wrapperRef,
                o = u.scrollPosition,
                i = u.clampPosition,
                s = u.animationScroll,
                c = u.events,
                E = (0, a.useState)(xt),
                A = E[0],
                _ = E[1];
              ((0, a.useEffect)(() => {
                const u = r.current;
                u && (u.style.cursor = "dragging" === A.type ? "move" : "grab");
              }, [r, A.type]),
                (0, a.useEffect)(() => {
                  if ("dragging" !== A.type) return;
                  const u = l.O.client.events.mouse.move(([u, t]) => {
                      const a = r.current,
                        l = n.current;
                      if (!a || !l) return;
                      if ("inside" === t && u.clientX < 0) return;
                      const c = "inside" === t ? u.clientX : u.clientX - l.offsetLeft,
                        E = A.positionFrom - c,
                        _ = A.previousScrollPosition + E;
                      o.start(
                        Object.assign(
                          {
                            scrollPosition: i(a, _),
                            from: { scrollPosition: s.scrollPosition.get() },
                          },
                          e && { config: e },
                        ),
                      );
                    }),
                    t = l.O.client.events.mouse.up(function () {
                      _({ type: "scrollingToEnd" });
                    });
                  return () => {
                    (u(), t());
                  };
                }, [s.scrollPosition, i, r, A, o, n, e]),
                (0, a.useEffect)(() => {
                  if ("scrollingToEnd" !== A.type) return;
                  const u = () => {
                    _(xt);
                  };
                  return (s.scrollPosition.idle && u(), c.on("rest", u), () => c.off("rest", u));
                }, [s.scrollPosition, A.type, c]),
                (0, a.useEffect)(() => {
                  const u = r.current;
                  if (!u) return;
                  const e = (u) => {
                    (t &&
                      t.allowedButtons &&
                      -1 === t.allowedButtons.findIndex((e) => u.button === e)) ||
                      _({
                        type: "dragging",
                        positionFrom: u.screenX,
                        previousScrollPosition: s.scrollPosition.get(),
                      });
                  };
                  return (
                    u.addEventListener("mousedown", e),
                    () => u.removeEventListener("mousedown", e)
                  );
                }, [s.scrollPosition, r, t]));
            })(G),
              (0, a.useEffect)(() => {
                const u = () => {
                  const u = G.animationScroll.scrollPosition.goal;
                  K(u);
                  const e = G.getBounds(),
                    t = e[0],
                    r = e[1];
                  (t === J.left && r === J.right) || Q([t, r]);
                };
                return (
                  G.events.on("change", u),
                  G.events.on("recalculateContent", u),
                  G.events.on("resizeHandled", u),
                  () => {
                    (G.events.off("change", u),
                      G.events.off("recalculateContent", u),
                      G.events.off("resizeHandled", u));
                  }
                );
              }, [G, J.left, J.right]),
              (0, a.useEffect)(() => {
                setTimeout(() => G.applyScroll(170 * ((B ? Math.floor(z / 2) : z) - 2)));
              }, [B, G, z]),
              (0, a.useEffect)(() => {
                j(E);
              }, [E]),
              (0, a.useLayoutEffect)(() => {
                j(z);
              }, [z]));
            const uu = f()(Lt, h && Tt, ($ === J.left || P) && kt),
              tu = f()(Rt, w && Ot, ($ === J.right || P) && Pt);
            return o().createElement(
              "div",
              { className: f()(u, yt, 0 === F.length && Mt) },
              F.length > 0 &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement("div", {
                    className: uu,
                    style: { "--arrow-width": "30rem" },
                    onMouseEnter: N,
                    onMouseLeave: H,
                    onClick: () => {
                      G.applyStepTo(Ue.Next);
                    },
                  }),
                  o().createElement(
                    "div",
                    { className: Ht, style: { "--arrow-width": "30rem" } },
                    o().createElement(
                      St.Horizontal.Area,
                      {
                        api: G,
                        classNames: { content: Nt, wrapper: It },
                        className: Wt,
                        style: { "--scroll-width": `${O}rem` },
                      },
                      F.map((u) =>
                        o().createElement(zt, jt({ key: u.vehicleCD, clickEvent: n }, u)),
                      ),
                    ),
                  ),
                  o().createElement("div", {
                    className: tu,
                    style: { "--arrow-width": "30rem" },
                    onMouseEnter: I,
                    onMouseLeave: W,
                    onClick: () => {
                      G.applyStepTo(Ue.Prev);
                    },
                  }),
                ),
              0 === F.length &&
                o().createElement(we, {
                  text: R.strings.comp7.battleCarousel.noFilteredVehiclesMessage(),
                  className: Vt,
                  variant: "paragraph-P16",
                  style: { "--filter-width": "72rem" },
                }),
            );
          }),
          $t = "CarouselView_base_d3",
          Kt = "CarouselView_filters_3c",
          Yt = "CarouselView_vehicles_04",
          qt = "CarouselView_popoverInfo_a4",
          Zt = "CarouselView_blur_9e",
          Qt = "CarouselView_blur__hide_04",
          Jt = (0, W.Pi)(() => {
            const u = Z().model.root.get().isLoading,
              e = (0, a.useState)(viewEnv.getViewSizeRem().width),
              t = e[0],
              r = e[1];
            (0, a.useEffect)(() => {
              const u = (u) => {
                r(u.width);
              };
              return (
                engine.on("screenResized", u),
                () => {
                  engine.off("screenResized", u);
                }
              );
            }, []);
            const n = (0, a.useState)(Math.ceil((76 / t) * 100)),
              i = n[0],
              l = n[1];
            return (
              (0, a.useEffect)(() => {
                l(Math.ceil((76 / t) * 100));
              }, [t]),
              o().createElement(
                "div",
                { className: $t, style: { "--filters-width": "72", "--outer-gap": `${i}%` } },
                o().createElement(Oe, { className: qt }),
                o().createElement(Uu, { className: Kt }),
                o().createElement(Xt, { className: Yt }),
                o().createElement("div", { className: f()(Zt, !u && Qt) }),
              )
            );
          });
        engine.whenReady.then(() => {
          I().render(
            o().createElement(q, null, o().createElement(N, null, o().createElement(Jt, null))),
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
    (__webpack_require__.O = (u, e, t, r) => {
      if (!e) {
        var n = 1 / 0;
        for (l = 0; l < deferred.length; l++) {
          for (var [e, t, r] = deferred[l], a = !0, o = 0; o < e.length; o++)
            (!1 & r || n >= r) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[o]))
              ? e.splice(o--, 1)
              : ((a = !1), r < n && (n = r));
          if (a) {
            deferred.splice(l--, 1);
            var i = t();
            void 0 !== i && (u = i);
          }
        }
        return u;
      }
      r = r || 0;
      for (var l = deferred.length; l > 0 && deferred[l - 1][2] > r; l--)
        deferred[l] = deferred[l - 1];
      deferred[l] = [e, t, r];
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
    (__webpack_require__.j = 199),
    (() => {
      var u = { 199: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var r,
            n,
            [a, o, i] = t,
            l = 0;
          if (a.some((e) => 0 !== u[e])) {
            for (r in o) __webpack_require__.o(o, r) && (__webpack_require__.m[r] = o[r]);
            if (i) var s = i(__webpack_require__);
          }
          for (e && e(t); l < a.length; l++)
            ((n = a[l]), __webpack_require__.o(u, n) && u[n] && u[n][0](), (u[n] = 0));
          return __webpack_require__.O(s);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [532], () => __webpack_require__(4545));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
