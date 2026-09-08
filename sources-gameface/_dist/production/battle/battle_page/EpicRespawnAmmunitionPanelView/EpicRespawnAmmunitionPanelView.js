(() => {
  var __webpack_modules__ = {
      3532: (e) => {
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
      9887: (e) => {
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
      527: (e, t, u) => {
        "use strict";
        (u.r(t), u.d(t, { mouse: () => s, onResize: () => i }));
        var n = u(2472),
          a = u(1176);
        const i = (0, n.E)("clientResized"),
          r = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, a.R)(!1);
          }
          function u() {
            e.enabled && (0, a.R)(!0);
          }
          function n() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", u))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", u))
              : (0, a.R)(!1);
          }
          const i = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let a = !0;
                  const i = `mouse${t}`,
                    s = r[t]((e) => u([e, "outside"]));
                  function o(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(i, o),
                    n(),
                    () => {
                      a &&
                        (s(), window.removeEventListener(i, o), (e.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(u)),
              t
            ),
            {},
          );
          return Object.assign({}, i, {
            disable() {
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
            },
            enableOutside() {
              e.enabled && (0, a.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, a.R)(!1);
            },
          });
        })();
      },
      5959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => n,
            getMouseGlobalPosition: () => i,
            getSize: () => a,
            graphicsQuality: () => r,
          }));
        var n = u(527);
        function a(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function i(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const r = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, t, u) => {
        "use strict";
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        u.d(t, { R: () => n });
      },
      2472: (e, t, u) => {
        "use strict";
        function n(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        u.d(t, { E: () => n });
      },
      3138: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => a });
        var n = u(5959);
        const a = { view: u(7641), client: n };
      },
      3722: (e, t, u) => {
        "use strict";
        function n(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function a(e, t, u) {
          return `url(${n(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => a, getTextureUrl: () => n }));
      },
      6112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => a });
        var n = u(2472);
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
      7641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => s,
            children: () => n,
            displayStatus: () => a.W,
            displayStatusIs: () => v,
            events: () => i.U,
            extraSize: () => w,
            forceTriggerMouseMove: () => S,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => b,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => C,
            isEventHandled: () => h,
            isFocused: () => g,
            pxToRem: () => F,
            remToPx: () => D,
            resize: () => m,
            sendEvent: () => r.qP,
            setAnimateWindow: () => p,
            setEventHandled: () => B,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => _,
            whenTutorialReady: () => y,
          }));
        var n = u(3722),
          a = u(6112),
          i = u(6538),
          r = u(8566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, u, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, n);
        }
        function c(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function _(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: D(t.x), y: D(t.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function b() {
          return viewEnv.getScale();
        }
        function F(e) {
          return viewEnv.pxToRem(e);
        }
        function D(e) {
          return viewEnv.remToPx(e);
        }
        function p(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function g() {
          return viewEnv.isFocused();
        }
        function C() {
          return viewEnv.isClientAccessible();
        }
        function B() {
          return viewEnv.setEventHandled();
        }
        function h() {
          return viewEnv.isEventHandled();
        }
        function S() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const v = Object.keys(a.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === a.W[t]), e),
            {},
          ),
          w = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          y = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : i.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => l });
        const n = ["args"];
        const a = 2,
          i = 16,
          r = 32,
          s = 64,
          o = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const i = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    i = Object.keys(e);
                  for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(t, n);
              return void 0 !== i
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, r, {
                      arguments:
                        ((a = i),
                        Object.entries(a).map(([e, t]) => {
                          const u = "GFValueProxy";
                          switch (typeof t) {
                            case "number":
                              return { __Type: u, name: e, number: t };
                            case "boolean":
                              return { __Type: u, name: e, bool: t };
                            default:
                              return { __Type: u, name: e, string: t.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, r));
            }
            return viewEnv.handleViewEvent({ __Type: u, type: e });
            var a;
          },
          l = {
            close(e) {
              o("popover" === e ? a : r);
            },
            minimize() {
              o(s);
            },
            move(e) {
              o(i, { isMouseEvent: !0, on: e });
            },
          };
      },
      5521: (e, t, u) => {
        "use strict";
        let n, a;
        (u.d(t, { n: () => n }),
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
          })(a || (a = {})));
      },
      1358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => i });
        var n = u(3138);
        class a {
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
            return (window.__dataTracker || (window.__dataTracker = new a()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, t, u = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const i = n.O.view.addModelObserver(e, u, a);
            return (
              i > 0
                ? ((this._callbacks[i] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(i) : (this._views[u] = [i])))
                : console.error("Can't add callback for model:", e),
              i
            );
          }
          removeCallback(e, t = 0) {
            let u = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((u = viewEnv.removeDataChangedCallback(e, t)), delete this._callbacks[e]),
              u || console.error("Can't remove callback by id:", e),
              u
            );
          }
          _emmitDataChanged(e, t, u) {
            u.forEach((u) => {
              const n = this._callbacks[u];
              void 0 !== n && n(e, t);
            });
          }
        }
        a.__instance = void 0;
        const i = a;
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
      4179: (e, t, u) => {
        "use strict";
        u.d(t, {
          Sw: () => i.Z,
          B0: () => o,
          c9: () => g,
          wU: () => S,
          ry: () => D,
          Eu: () => p,
          SW: () => B,
          P3: () => h,
        });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: u }) => {
                  let n = e.target;
                  do {
                    if (n === t) return;
                    n = n.parentNode;
                  } while (n);
                  u();
                });
              }));
          }
          static get instance() {
            return (n.__instance || (n.__instance = new n()), n.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const u = e,
              n = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== u || t !== n,
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
        var i = u(1358);
        const r = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          s = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, u) => userLocale.getTimeFormat(e, t, void 0 === u || u),
            getTimeString: (e, t, u) => userLocale.getTimeString(e, t, void 0 === u || u),
          };
        let o;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(o || (o = {}));
        const l = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = u(5521),
          E = u(3138);
        const A = ["args"];
        function b(e, t, u, n, a, i, r) {
          try {
            var s = e[i](r),
              o = s.value;
          } catch (e) {
            return void u(e);
          }
          s.done ? t(o) : Promise.resolve(o).then(n, a);
        }
        const F = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          D = (function () {
            var e,
              t =
                ((e = function* () {
                  return (
                    !(!engine._BindingsReady || !engine._WindowLoaded) ||
                    new Promise((e) => {
                      engine.on("Ready", e);
                    })
                  );
                }),
                function () {
                  var t = this,
                    u = arguments;
                  return new Promise(function (n, a) {
                    var i = e.apply(t, u);
                    function r(e) {
                      b(i, n, a, r, s, "next", e);
                    }
                    function s(e) {
                      b(i, n, a, r, s, "throw", e);
                    }
                    r(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          p = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          g = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const a = t.args,
                i = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    i = Object.keys(e);
                  for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(t, A);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, i, {
                      arguments:
                        ((n = a),
                        Object.entries(n).map(([e, t]) => {
                          const u = { __Type: "GFValueProxy", name: e };
                          switch (typeof t) {
                            case "number":
                              u.number = t;
                              break;
                            case "boolean":
                              u.bool = t;
                              break;
                            default:
                              u.string = t.toString();
                          }
                          return u;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, i));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var n;
          },
          C = () => g(o.CLOSE),
          B = () => g(o.POP_OVER, { on: !1 }),
          h = (e, t, u, n, a = R.invalid("resId"), i) => {
            const r = E.O.view.getViewGlobalPosition(),
              s = u.getBoundingClientRect(),
              l = s.x,
              c = s.y,
              _ = s.width,
              d = s.height,
              m = {
                x: E.O.view.pxToRem(l) + r.x,
                y: E.O.view.pxToRem(c) + r.y,
                width: E.O.view.pxToRem(_),
                height: E.O.view.pxToRem(d),
              };
            g(o.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: n || R.invalid("resId"),
              targetID: a,
              direction: t,
              bbox: F(m),
              on: !0,
              args: i,
            });
          },
          S = () => viewEnv.isWindowShownByViewEvent(o.POP_OVER),
          f = (e, t) => {
            e.keyCode === m.n.ESCAPE && t();
          };
        var v = u(7572);
        const w = a.instance,
          y = {
            DataTracker: i.Z,
            ViewModel: v.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: _,
            DateFormatType: d,
            makeGlobalBoundingBox: F,
            sendMoveEvent: (e) => g(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: B,
            sendShowContextMenuEvent: (e, t, u = 0) => {
              g(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
                args: t,
              });
            },
            sendShowPopOverEvent: h,
            addEscapeListener: (e) => {
              const t = (t) => f(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              f(e, C);
            },
            handleViewEvent: g,
            onBindingsReady: D,
            onLayoutReady: p,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(o.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(o.CONTEXT_MENU),
            isPopOverShown: S,
            dumpViewModel: function e(t) {
              const u = {};
              if ("object" != typeof t) return t;
              for (const n in t)
                if (Object.prototype.hasOwnProperty.call(t, n)) {
                  const a = Object.prototype.toString.call(t[n]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = t[n];
                    u[n] = [];
                    for (let t = 0; t < a.length; t++) u[n].push({ value: e(a[t].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[n] = e(t[n]))
                      : (u[n] = t[n]);
                }
              return u;
            },
            ClickOutsideManager: w,
            SystemLocale: r,
            UserLocale: s,
          };
        window.ViewEnvHelper = y;
      },
      9376: (e, t, u) => {
        "use strict";
        var n = u(6179),
          a = u.n(n),
          i = u(493),
          r = u.n(i);
        const s = (e = 1) => {
            const t = new Error().stack;
            let u,
              n = R.invalid("resId");
            return (
              t &&
                ((u = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                window.__feature &&
                  window.__feature !== u &&
                  window.subViews[u] &&
                  (n = window.subViews[u].id)),
              { caller: u, stack: t, resId: n }
            );
          },
          o = (e, t) => e.split(".").reduce((e, t) => e && e[t], t),
          l = (e) => {
            const t = (0, n.useRef)(!1);
            t.current || (e(), (t.current = !0));
          };
        var c = u(4179);
        const _ = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          d = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          m = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, u) => {
                const n = o(`${e}.${u}`, window);
                return _(n) ? t(e, u, n) : `${e}.${u}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          E = (e) => {
            const t = ((e) => {
                const t = s(),
                  u = t.caller,
                  n = t.resId,
                  a = window.__feature && window.__feature !== u && u ? `subViews.${u}` : "";
                return { modelPrefix: a, modelPath: d(a, e || ""), resId: n };
              })(),
              u = t.modelPrefix,
              n = e.split(".");
            if (n.length > 0) {
              const e = [n[0]];
              return (
                n.reduce((t, n) => {
                  const a = o(d(u, `${t}.${n}`), window);
                  return _(a) ? (e.push(a.id), `${t}.${n}.value`) : (e.push(n), `${t}.${n}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          A = c.Sw.instance;
        let b;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(b || (b = {}));
        const F = (e = "model", t = b.Deep) => {
          const u = (0, n.useState)(0),
            a = (u[0], u[1]),
            i = (0, n.useMemo)(() => s(), []),
            r = i.caller,
            c = i.resId,
            d = (0, n.useMemo)(
              () => (window.__feature && window.__feature !== r ? `subViews.${r}.${e}` : e),
              [r, e],
            ),
            F = (0, n.useState)(() =>
              ((e) => {
                const t = o(e, window);
                for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                return _(t) ? t.value : t;
              })(m(d)),
            ),
            D = F[0],
            p = F[1],
            g = (0, n.useRef)(-1);
          return (
            l(() => {
              if (
                ("boolean" == typeof t &&
                  ((t = t ? b.Deep : b.None),
                  console.warn(
                    'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                  )),
                t !== b.None)
              ) {
                const u = (e) => {
                    ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                    t === b.Deep
                      ? (e === D && a((e) => e + 1), p(e))
                      : p(Object.assign([], e));
                  },
                  n = E(e);
                g.current = A.addCallback(n, u, c, t === b.Deep);
              }
            }),
            (0, n.useEffect)(() => {
              if (t !== b.None)
                return () => {
                  A.removeCallback(g.current, c);
                };
            }, [c, t]),
            D
          );
        };
        var D = u(3138),
          p = u(5521);
        const g = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function C(e = p.n.NONE, t = g, u = !1) {
          (0, n.useEffect)(() => {
            if (e !== p.n.NONE)
              return (
                window.addEventListener("keydown", n, u),
                () => {
                  window.removeEventListener("keydown", n, u);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (D.O.view.isEventHandled()) return;
                (D.O.view.setEventHandled(), t(n), u && n.stopPropagation());
              }
            }
          }, [t, e, u]);
        }
        var B = u(6483),
          h = u.n(B);
        const S = (e) => {
          (0, n.useEffect)(e, []);
        };
        const f = (0, n.createContext)(null);
        function v() {
          return (0, n.useContext)(f);
        }
        const w = (e) => {
            let t,
              u = null;
            return (
              (u = requestAnimationFrame(() => {
                u = requestAnimationFrame(() => {
                  ((u = null), (t = e()));
                });
              })),
              () => {
                ("function" == typeof t && t(), null !== u && cancelAnimationFrame(u));
              }
            );
          },
          y = (e) => {
            const t = (0, n.useRef)();
            return (
              (0, n.useEffect)(() => {
                t.current = e;
              }, [e]),
              t.current
            );
          };
        let x;
        function T(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(x || (x = {}));
        const k = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          I = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          O = (e, t, u = x.left) => e.split(t).reduce(u === x.left ? k : I, []),
          M = (() => {
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
            return (t) =>
              t
                .replace(/&nbsp;/g, " ")
                .replace(/ /g, " ")
                .match(e);
          })(),
          N = ["zh_cn", "zh_sg", "zh_tw"],
          L = (e, t = x.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return N.includes(u)
              ? M(e)
              : ((e, t = x.left) => {
                  let u = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = e.replace(/&nbsp;/g, " ");
                  return (O(a, /( )/, t).forEach((e) => (u = u.concat(O(e, n, x.left)))), u);
                })(e, t);
          };
        let P;
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
        })(P || (P = {}));
        Date.now();
        const H = c.Sw.instance,
          G = (e = "model", t = !0) => {
            const u = (0, n.useState)(0),
              a = (u[0], u[1]),
              i = (0, n.useMemo)(() => s(), []),
              r = i.caller,
              l = i.resId,
              c = (0, n.useMemo)(
                () => (window.__feature && window.__feature !== r ? `children.${r}.${e}` : e),
                [r, e],
              ),
              _ = (0, n.useMemo)(
                () =>
                  ((e) => {
                    const t = o(e, window);
                    for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                    return t;
                  })(c),
                [c],
              );
            return (
              (0, n.useEffect)(() => {
                if (t) {
                  const t = () => {
                      a((e) => e + 1);
                    },
                    u = H.addCallback(e, t, l);
                  return () => H.removeCallback(u, l);
                }
              }, [e, t, l]),
              _
            );
          },
          $ = y,
          W = (e, t, u) =>
            t.extraLargeHeight ||
            t.largeHeight ||
            t.mediumHeight ||
            t.smallHeight ||
            t.extraSmallHeight
              ? (t.extraLargeHeight && u.extraLarge) ||
                (t.largeHeight && u.large) ||
                (t.mediumHeight && u.medium) ||
                (t.smallHeight && u.small) ||
                (t.extraSmallHeight && u.extraSmall)
                ? e
                : null
              : e,
          z = {
            extraLarge: { weight: 4, width: 2560, height: 1440 },
            large: { weight: 3, width: 1920, height: 1080 },
            medium: { weight: 2, width: 1600, height: 900 },
            small: { weight: 1, width: 1366, height: 768 },
            extraSmall: { weight: 0, width: 1024, height: 768 },
          };
        var U;
        function X(e, t, u) {
          const n = (function (e, t) {
              switch (!0) {
                case e >= t.extraLarge.width:
                  return t.extraLarge.weight;
                case e >= t.large.width && e < t.extraLarge.width:
                  return t.large.weight;
                case e >= t.medium.width && e < t.large.width:
                  return t.medium.weight;
                case e >= t.small.width && e < t.medium.width:
                  return t.small.weight;
                default:
                  return t.extraSmall.weight;
              }
            })(e, u),
            a = (function (e, t) {
              switch (!0) {
                case e >= t.extraLarge.height:
                  return t.extraLarge.weight;
                case e >= t.large.height && e < t.extraLarge.height:
                  return t.large.weight;
                case e >= t.medium.height && e < t.large.height:
                  return t.medium.weight;
                case e >= t.small.height && e < t.medium.height:
                  return t.small.weight;
                default:
                  return t.extraSmall.weight;
              }
            })(t, u),
            i = Math.min(n, a);
          return {
            extraLarge: i === u.extraLarge.weight,
            large: i === u.large.weight,
            medium: i === u.medium.weight,
            small: i === u.small.weight,
            extraSmall: i === u.extraSmall.weight,
            extraLargeWidth: n === u.extraLarge.weight,
            largeWidth: n === u.large.weight,
            mediumWidth: n === u.medium.weight,
            smallWidth: n === u.small.weight,
            extraSmallWidth: n === u.extraSmall.weight,
            extraLargeHeight: a === u.extraLarge.weight,
            largeHeight: a === u.large.weight,
            mediumHeight: a === u.medium.weight,
            smallHeight: a === u.small.weight,
            extraSmallHeight: a === u.extraSmall.weight,
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
        })(U || (U = {}));
        const j = D.O.client.getSize("rem"),
          V = j.width,
          K = j.height,
          q = Object.assign({ width: V, height: K }, X(V, K, z)),
          Y = (0, n.createContext)(q),
          Z = ["children"];
        const Q = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                i = Object.keys(e);
              for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, Z);
          const a = (0, n.useContext)(Y),
            i = a.extraLarge,
            r = a.large,
            s = a.medium,
            o = a.small,
            l = a.extraSmall,
            c = a.extraLargeWidth,
            _ = a.largeWidth,
            d = a.mediumWidth,
            m = a.smallWidth,
            E = a.extraSmallWidth,
            A = a.extraLargeHeight,
            b = a.largeHeight,
            F = a.mediumHeight,
            D = a.smallHeight,
            p = a.extraSmallHeight,
            g = { extraLarge: A, large: b, medium: F, small: D, extraSmall: p };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && i) return t;
            if (u.large && r) return t;
            if (u.medium && s) return t;
            if (u.small && o) return t;
            if (u.extraSmall && l) return t;
          } else {
            if (u.extraLargeWidth && c) return W(t, u, g);
            if (u.largeWidth && _) return W(t, u, g);
            if (u.mediumWidth && d) return W(t, u, g);
            if (u.smallWidth && m) return W(t, u, g);
            if (u.extraSmallWidth && E) return W(t, u, g);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && A) return t;
              if (u.largeHeight && b) return t;
              if (u.mediumHeight && F) return t;
              if (u.smallHeight && D) return t;
              if (u.extraSmallHeight && p) return t;
            }
          }
          return null;
        };
        Q.defaultProps = {
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
        ((0, n.memo)(Q),
          (0, n.memo)(({ children: e }) => {
            const t = (0, n.useContext)(Y),
              u = (0, n.useState)(t),
              i = u[0],
              r = u[1],
              s = (0, n.useCallback)((e, t) => {
                const u = D.O.view.pxToRem(e),
                  n = D.O.view.pxToRem(t);
                r(Object.assign({ width: u, height: n }, X(u, n, z)));
              }, []);
            (l(() => {
              engine.on("clientResized", s);
            }),
              (0, n.useEffect)(() => () => engine.off("clientResized", s), [s]));
            const o = (0, n.useMemo)(() => Object.assign({}, i), [i]);
            return a().createElement(Y.Provider, { value: o }, e);
          }));
        function J(e, t, u) {
          const a = (0, n.useContext)(Y);
          let i = Object.entries(a).filter(([e, t]) => !0 === t && e in U);
          return (
            u && (i = i.filter((e) => u.includes(e[0]))),
            e.reduce((e, u) => {
              const n = i.map((e) =>
                h()(t[((e, t) => e + "__" + t)(u, e[0])], t[((e, t) => e + T(t))(u, e[0])]),
              );
              return ((e[u] = h()(t[u], ...n)), e);
            }, {})
          );
        }
        function ee(e) {
          return (
            !1 ===
            (function (e) {
              return null == e;
            })(e)
          );
        }
        function te(e, t) {
          var u;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (u = e[t]) ? void 0 : u.value;
        }
        const ue = te;
        function ne(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, u, n) => t(null == e ? void 0 : e.value, u, n));
        }
        function ae(e, t, u) {
          const n = [];
          for (let a = 0; a < e.length; a++) {
            const i = ue(e, a);
            t(i, a, e) && n.push(u(i, a, e));
          }
          return n;
        }
        function ie(e, t) {
          return ae(e, ee, t);
        }
        var re = u(8934);
        const se = (e, t, u, a = []) => {
          const i = ((e, t = []) => {
            const u = (0, n.useRef)(),
              a = (0, n.useCallback)((...t) => {
                (u.current && u.current(), (u.current = e(...t)));
              }, t);
            return (
              (0, n.useEffect)(
                () => () => {
                  u.current && u.current();
                },
                [a],
              ),
              a
            );
          })(
            () =>
              w(() =>
                w(() => {
                  if (e.current) {
                    const u = e.current.getBoundingClientRect(),
                      n = {
                        width: D.O.view.pxToRem(u.width),
                        height: D.O.view.pxToRem(u.height),
                        offsetX: D.O.view.pxToRem(u.left),
                        offsetY: D.O.view.pxToRem(u.top),
                      };
                    (window.tutorialApi.updateComponents(), t(n));
                  }
                }),
              ),
            [t, e],
          );
          return (
            (0, n.useEffect)(() => {
              i();
            }, [i, ...a]),
            (0, n.useEffect)(() => {
              if (u)
                return (
                  engine.on("clientResized", i),
                  () => {
                    engine.off("clientResized", i);
                  }
                );
            }, [u, i]),
            i
          );
        };
        var oe = u(9887),
          le = u.n(oe);
        let ce, _e, de;
        (!(function (e) {
          ((e[(e.ExtraSmall = z.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = z.small.width)] = "Small"),
            (e[(e.Medium = z.medium.width)] = "Medium"),
            (e[(e.Large = z.large.width)] = "Large"),
            (e[(e.ExtraLarge = z.extraLarge.width)] = "ExtraLarge"));
        })(ce || (ce = {})),
          (function (e) {
            ((e[(e.ExtraSmall = z.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = z.small.width)] = "Small"),
              (e[(e.Medium = z.medium.width)] = "Medium"),
              (e[(e.Large = z.large.width)] = "Large"),
              (e[(e.ExtraLarge = z.extraLarge.width)] = "ExtraLarge"));
          })(_e || (_e = {})),
          (function (e) {
            ((e[(e.ExtraSmall = z.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = z.small.height)] = "Small"),
              (e[(e.Medium = z.medium.height)] = "Medium"),
              (e[(e.Large = z.large.height)] = "Large"),
              (e[(e.ExtraLarge = z.extraLarge.height)] = "ExtraLarge"));
          })(de || (de = {})));
        const me = () => {
            const e = (0, n.useContext)(Y),
              t = e.width,
              u = e.height,
              a = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return ce.ExtraLarge;
                  case e.large:
                    return ce.Large;
                  case e.medium:
                    return ce.Medium;
                  case e.small:
                    return ce.Small;
                  case e.extraSmall:
                    return ce.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), ce.ExtraSmall);
                }
              })(e),
              i = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return _e.ExtraLarge;
                  case e.largeWidth:
                    return _e.Large;
                  case e.mediumWidth:
                    return _e.Medium;
                  case e.smallWidth:
                    return _e.Small;
                  case e.extraSmallWidth:
                    return _e.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), _e.ExtraSmall);
                }
              })(e),
              r = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return de.ExtraLarge;
                  case e.largeHeight:
                    return de.Large;
                  case e.mediumHeight:
                    return de.Medium;
                  case e.smallHeight:
                    return de.Small;
                  case e.extraSmallHeight:
                    return de.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), de.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: a,
              mediaWidth: i,
              mediaHeight: r,
              remScreenWidth: t,
              remScreenHeight: u,
            };
          },
          Ee = ["xl", "lg", "md", "sm", "xs"],
          Ae = (e) => e.includes("_") && ((e) => Ee.includes(e))(e.split("_").at(-1)),
          be = [ce.ExtraLarge, ce.Large, ce.Medium, ce.Small, ce.ExtraSmall],
          Fe = (e, t) =>
            Object.keys(e).reduce((u, n) => {
              if (n in u) return u;
              if (Ae(n)) {
                const a = n.split("_").slice(0, -1).join("_");
                if (a in u) return u;
                const i = be.indexOf(t),
                  r = (-1 !== i ? Ee.slice(i) : [])
                    .map((e) => a + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  s = r ? e[r] : void 0;
                return ((u[a] = void 0 !== s ? s : e[a]), u);
              }
              const a = e[n];
              return (
                void 0 === a ||
                  ((e, t) => Ee.some((u) => void 0 !== t[`${e}_${u}`]))(n, e) ||
                  (u[n] = a),
                u
              );
            }, {}),
          De = (e, t = Fe) => {
            const u = (
              (e, t = Fe) =>
              (u) => {
                const i = me().mediaSize,
                  r = (0, n.useMemo)(() => t(u, i), [u, i]);
                return a().createElement(e, r);
              }
            )(e, t);
            return a().memo((t) =>
              Object.keys(t).some((e) => Ae(e) && void 0 !== t[e])
                ? a().createElement(u, t)
                : a().createElement(e, t),
            );
          },
          pe = {
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
          ge = [
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
        function Ce() {
          return (
            (Ce =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ce.apply(this, arguments)
          );
        }
        Object.keys(le());
        const Be = {
            XL: { mt: pe.mt__XL, mr: pe.mr__XL, mb: pe.mb__XL, ml: pe.ml__XL },
            LG: { mt: pe.mt__LG, mr: pe.mr__LG, mb: pe.mb__LG, ml: pe.ml__LG },
            MDp: { mt: pe.mt__MDp, mr: pe.mr__MDp, mb: pe.mb__MDp, ml: pe.ml__MDp },
            MD: { mt: pe.mt__MD, mr: pe.mr__MD, mb: pe.mb__MD, ml: pe.ml__MD },
            SMp: { mt: pe.mt__SMp, mr: pe.mr__SMp, mb: pe.mb__SMp, ml: pe.ml__SMp },
            SM: { mt: pe.mt__SM, mr: pe.mr__SM, mb: pe.mb__SM, ml: pe.ml__SM },
            XS: { mt: pe.mt__XS, mr: pe.mr__XS, mb: pe.mb__XS, ml: pe.ml__XS },
          },
          he = (Object.keys(Be), ["mt", "mr", "mb", "ml"]),
          Se = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          fe = De((e) => {
            let t = e.className,
              u = e.width,
              i = e.height,
              r = e.m,
              s = e.mt,
              o = void 0 === s ? r : s,
              l = e.mr,
              c = void 0 === l ? r : l,
              _ = e.mb,
              d = void 0 === _ ? r : _,
              m = e.ml,
              E = void 0 === m ? r : m,
              A = e.column,
              b = e.row,
              F = e.flexDirection,
              D = void 0 === F ? (A ? "column" : b && "row") || void 0 : F,
              p = e.flexStart,
              g = e.center,
              C = e.flexEnd,
              B = e.spaceBetween,
              S = e.spaceAround,
              f = e.justifyContent,
              v =
                void 0 === f
                  ? (p ? "flex-start" : g && "center") ||
                    (C && "flex-end") ||
                    (B && "space-between") ||
                    (S && "space-around") ||
                    void 0
                  : f,
              w = e.alignItems,
              y =
                void 0 === w
                  ? (p ? "flex-start" : g && "center") || (C && "flex-end") || void 0
                  : w,
              x = e.alignSelf,
              T = e.wrap,
              k = e.flexWrap,
              I = void 0 === k ? (T ? "wrap" : void 0) : k,
              R = e.grow,
              O = e.shrink,
              M = e.flex,
              N = void 0 === M ? (R || O ? `${R ? 1 : 0} ${O ? 1 : 0} auto` : void 0) : M,
              L = e.style,
              P = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, ge);
            const G = (0, n.useMemo)(() => {
                const e = { mt: o, mr: c, mb: d, ml: E },
                  t = ((e) =>
                    he.reduce((t, u) => {
                      const n = e[u];
                      return n && "number" != typeof n ? t.concat(Be[!0 === n ? "MD" : n][u]) : t;
                    }, []))(e),
                  n = ((e) =>
                    he.reduce((t, u) => {
                      const n = e[u];
                      return ("number" == typeof n && (t[Se[u]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, L, n, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== i && "number" == typeof i ? i + "rem" : i,
                    flex: N,
                    alignSelf: x,
                    display: D || y ? "flex" : void 0,
                    flexDirection: D,
                    flexWrap: I,
                    justifyContent: v,
                    alignItems: y,
                  }),
                  computedClassNames: t,
                };
              }, [u, i, o, c, d, E, L, N, x, D, I, v, y]),
              $ = G.computedStyle,
              W = G.computedClassNames;
            return a().createElement(
              "div",
              Ce({ className: h()(pe.base, ...W, t), style: $ }, H),
              P,
            );
          }),
          ve = "FormatText_base_d0",
          we = ({ binding: e, text: t = "", classMix: u, alignment: i = x.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  n.Fragment,
                  null,
                  t.split("\n").map((t, r) =>
                    a().createElement(
                      "div",
                      { className: h()(ve, u), key: `${t}-${r}` },
                      ((e, t, u) =>
                        e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (u && e in u ? u[e] : L(e, t))))(
                        t,
                        i,
                        e,
                      ).map((e, t) => a().createElement(n.Fragment, { key: `${t}-${e}` }, e)),
                    ),
                  ),
                );
        var ye = u(3532),
          xe = u.n(ye);
        const Te = {
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
          ke = [
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
        function Ie() {
          return (
            (Ie =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ie.apply(this, arguments)
          );
        }
        Object.keys(le());
        const Re = Object.keys(xe()),
          Oe = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Me = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Ne = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Le = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Pe =
            (Object.keys(Le),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Oe,
              "heading-H36": Oe,
              "heading-H28": Me,
              "heading-H24": Me,
              "heading-H24R": Me,
              "heading-H22": Me,
              "heading-H20R": Me,
              "heading-H18": Me,
              "heading-H15": Ne,
              "heading-H14": Ne,
              "paragraph-P24": Me,
              "paragraph-P18": Me,
              "paragraph-P16": Me,
              "paragraph-P14": Ne,
              "paragraph-P12": Ne,
              "paragraph-P10": Ne,
            }),
          He =
            (Object.keys(Pe),
            (e) =>
              e
                ? ((e) => Re.includes(e))(e)
                  ? { colorClassName: Te[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Ge = De((e) => {
            let t = e.text,
              u = e.variant,
              i = e.className,
              r = e.color,
              s = e.m,
              o = e.mt,
              l = void 0 === o ? s : o,
              c = e.mr,
              _ = void 0 === c ? s : c,
              d = e.mb,
              m = void 0 === d ? s : d,
              E = e.ml,
              A = void 0 === E ? s : E,
              b = e.style,
              F = e.format,
              D = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, ke);
            const p = (0, n.useMemo)(() => {
                const e = He(r),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  n = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, b, n), colorClassName: t };
              }, [b, r]),
              g = p.computedStyle,
              C = p.colorClassName;
            return a().createElement(
              fe,
              Ie(
                {
                  className: h()(Te.base, u && Te[u], C, i),
                  style: g,
                  mt: !0 === l ? Pe[u || "paragraph-P16"].mt : l,
                  mr: !0 === _ ? Pe[u || "paragraph-P16"].mr : _,
                  mb: !0 === m ? Pe[u || "paragraph-P16"].mb : m,
                  ml: !0 === A ? Pe[u || "paragraph-P16"].ml : A,
                },
                D,
              ),
              void 0 !== F ? a().createElement(we, Ie({}, F, { text: t })) : t,
            );
          }),
          $e = [
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
        function We(e) {
          return Object.entries(e || {}).map(([e, t]) => {
            const u = { __Type: "GFValueProxy", name: e };
            switch (typeof t) {
              case "number":
                u.number = t;
                break;
              case "boolean":
                u.bool = t;
                break;
              case "undefined":
                break;
              default:
                u.string = t.toString();
            }
            return u;
          });
        }
        const ze = (e, t, u = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: c.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                u,
              ),
            );
          },
          Ue = (e) => {
            let t = e.children,
              u = e.contentId,
              a = e.args,
              i = e.onMouseEnter,
              r = e.onMouseLeave,
              o = e.onMouseDown,
              l = e.onClick,
              c = e.ignoreShowDelay,
              _ = void 0 !== c && c,
              d = e.ignoreMouseClick,
              m = void 0 !== d && d,
              E = e.decoratorId,
              A = void 0 === E ? 0 : E,
              b = e.isEnabled,
              F = void 0 === b || b,
              D = e.targetId,
              p = void 0 === D ? 0 : D,
              g = e.onShow,
              C = e.onHide,
              B = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, $e);
            const h = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, n.useMemo)(() => p || s().resId, [p]),
              f = (0, n.useCallback)(() => {
                (h.current.isVisible && h.current.timeoutId) ||
                  (ze(u, A, { isMouseEvent: !0, on: !0, arguments: We(a) }, S),
                  g && g(),
                  (h.current.isVisible = !0));
              }, [u, A, a, S, g]),
              v = (0, n.useCallback)(() => {
                if (h.current.isVisible || h.current.timeoutId) {
                  const e = h.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (h.current.timeoutId = 0)),
                    ze(u, A, { on: !1 }, S),
                    h.current.isVisible && C && C(),
                    (h.current.isVisible = !1));
                }
              }, [u, A, S, C]),
              w = (0, n.useCallback)((e) => {
                h.current.isVisible &&
                  ((h.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (h.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(h.current.prevTarget) && v();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const e = h.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === F && v();
              }, [F, v]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", v),
                  () => {
                    (window.removeEventListener("mouseleave", v), v());
                  }
                ),
                [v],
              ));
            return F
              ? (0, n.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((y = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((h.current.timeoutId = window.setTimeout(f, _ ? 100 : 400)),
                            i && i(e),
                            y && y(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (v(), null == r || r(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === m && v(), null == l || l(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === m && v(), null == o || o(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    B,
                  ),
                )
              : t;
            var y;
          },
          Xe = ["children"];
        function je() {
          return (
            (je =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            je.apply(this, arguments)
          );
        }
        const Ve = (e) => {
            let t = e.children,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Xe);
            return a().createElement(
              Ue,
              je(
                {
                  contentId:
                    R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                      "resId",
                    ),
                  ignoreShowDelay: !0,
                },
                u,
              ),
              t,
            );
          },
          Ke = ["children", "body", "header", "note", "alert", "args"];
        function qe() {
          return (
            (qe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            qe.apply(this, arguments)
          );
        }
        const Ye = R.views.common.tooltip_window.simple_tooltip_content,
          Ze = (e) => {
            let t = e.children,
              u = e.body,
              i = e.header,
              r = e.note,
              s = e.alert,
              o = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Ke);
            const c = (0, n.useMemo)(() => {
              const e = Object.assign({}, o, { body: u, header: i, note: r, alert: s });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [s, u, i, r, o]);
            return a().createElement(
              Ue,
              qe(
                {
                  contentId:
                    ((_ = null == o ? void 0 : o.hasHtmlContent),
                    _ ? Ye.SimpleTooltipHtmlContent("resId") : Ye.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var _;
          };
        function Qe() {
          return (
            (Qe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Qe.apply(this, arguments)
          );
        }
        const Je = ({ children: e, tooltipArgs: t, className: u }) => {
            if (!t) return e;
            const n = a().createElement("div", { className: u }, e);
            if (t.header || t.body) return a().createElement(Ze, t, n);
            const i = t.contentId,
              r = t.args,
              s = null == r ? void 0 : r.contentId;
            return i || s
              ? a().createElement(Ue, Qe({}, t, { contentId: i || s }), n)
              : a().createElement(Ve, t, n);
          },
          et = "AbilitySkillSlot_base_d7",
          tt = "AbilitySkillSlot_slotText_1e",
          ut = "AbilitySkillSlot_icon_d2",
          nt = ({ skillName: e, tooltipId: t, tooltipHeader: u, tooltipBody: i, className: r }) => {
            const s = (0, n.useMemo)(
                () => ({
                  args: { tooltipId: t, skillName: e, header: u, body: i, hasHtmlContent: !0 },
                  header: u,
                  body: i,
                  ignoreShowDelay: !0,
                }),
                [e, u, i, t],
              ),
              o = R.images.gui.maps.icons.roleSkills.c_48x48;
            return a().createElement(
              Je,
              { tooltipArgs: s, className: h()(et, r) },
              a().createElement(
                a().Fragment,
                null,
                a().createElement(Ge, {
                  className: tt,
                  text: R.strings.tank_setup.tooltips.abilitySlot.title(),
                }),
                a().createElement("div", {
                  className: ut,
                  style: { backgroundImage: `url(${o.$dyn(e) || o.$dyn("not_found_artefact")})` },
                }),
              ),
            );
          },
          at = {
            base: "AmmunitionPanel_base_f8",
            base__locked: "AmmunitionPanel_base__locked_71",
            base__disabled: "AmmunitionPanel_base__disabled_41",
            base__hidden: "AmmunitionPanel_base__hidden_10",
            base__comp7Prebattle: "AmmunitionPanel_base__comp7Prebattle_59",
            border: "AmmunitionPanel_border_38",
            border__hidden: "AmmunitionPanel_border__hidden_7d",
            roleSkillSlot: "AmmunitionPanel_roleSkillSlot_21",
            roleSkillSlot__battle: "AmmunitionPanel_roleSkillSlot__battle_e4",
            roleSkillSlot__small: "AmmunitionPanel_roleSkillSlot__small_8b",
            roleSkillSlot__extraSmall: "AmmunitionPanel_roleSkillSlot__extraSmall_7a",
            roleSkillSlot__prebattle: "AmmunitionPanel_roleSkillSlot__prebattle_00",
            skillSelectAnimation: "AmmunitionPanel_skillSelectAnimation_1e",
            skillSelectAnimation__exitActive: "AmmunitionPanel_skillSelectAnimation__exitActive_9e",
            roleSkillButton: "AmmunitionPanel_roleSkillButton_e7",
            roleSkillSelectBorder: "AmmunitionPanel_roleSkillSelectBorder_59",
            roleSkillSelectBorder__visible: "AmmunitionPanel_roleSkillSelectBorder__visible_5f",
            abilitySkillSlot: "AmmunitionPanel_abilitySkillSlot_50",
            abilitySkillSlot__battle: "AmmunitionPanel_abilitySkillSlot__battle_ac",
            abilitySkillSlot__small: "AmmunitionPanel_abilitySkillSlot__small_c1",
            abilitySkillSlot__extraSmall: "AmmunitionPanel_abilitySkillSlot__extraSmall_bd",
            abilitySkillSlot__prebattle: "AmmunitionPanel_abilitySkillSlot__prebattle_f0",
          },
          it = "Border_base_f9",
          rt = "Border_border_83",
          st = "Border_wrapper_17",
          ot = "Border_active_e8",
          lt = (0, n.memo)(({ slotOffset: e, slotWidth: t, onAnimationEnd: u }) => {
            const i = (0, n.useRef)(null),
              r = (0, n.useRef)(!1);
            (0, n.useEffect)(() => {
              r.current = !0;
            }, [e, t]);
            const s = (0, n.useCallback)(() => {
              (r.current && u(), (r.current = !1));
            }, [u]);
            (0, n.useEffect)(() => {
              const e = i.current;
              return (
                e && e.addEventListener("transitionend", s),
                () => {
                  e && e.removeEventListener("transitionend", s);
                }
              );
            }, [s]);
            const o = (0, n.useMemo)(() => ({ left: e }), [e]),
              l = (0, n.useMemo)(() => ({ width: t }), [t]);
            return a().createElement(
              "div",
              { className: it },
              a().createElement(
                "div",
                { ref: i, className: rt, style: o },
                a().createElement(
                  "div",
                  { className: st },
                  a().createElement("div", { className: ot, style: l }),
                ),
              ),
            );
          });
        function ct(e) {
          engine.call("PlaySound", e);
        }
        const _t = {
          playHighlight() {
            ct("highlight");
          },
          playClick() {
            ct("play");
          },
          playYes() {
            ct("yes1");
          },
        };
        let dt;
        !(function (e) {
          ((e[(e.NORMAL = 0)] = "NORMAL"), (e[(e.WARNING = 1)] = "WARNING"));
        })(dt || (dt = {}));
        const mt = "SwitchButton_base_23",
          Et = "SwitchButton_base__active_31",
          At = "SwitchButton_base__warning_71",
          bt = "SwitchButton_buttonBack_ce",
          Ft = "SwitchButton_buttonBackHovered_45",
          Dt = "SwitchButton_base__hovered_b4",
          pt = "SwitchButton_buttonGlow_4c",
          gt = "SwitchButton_buttonIcon_d3",
          Ct = "SwitchButton_buttonWarning_3f",
          Bt = "SwitchButton_number_8a",
          ht = ({ id: e, state: t, currentIndex: u, isHovered: i }) => {
            const r = (0, n.useMemo)(
                () => ({
                  backgroundImage: `url('${R.images.gui.maps.icons.tanksetup.panel.indexes.$dyn(`setup_${e + 1}`)}')`,
                }),
                [e],
              ),
              s = e === u,
              o = !s && t === dt.WARNING;
            return a().createElement(
              "div",
              { className: h()(mt, { [Et]: s, [At]: o, [Dt]: i }) },
              a().createElement("div", { className: bt }),
              a().createElement("div", { className: Ft }),
              a().createElement("div", { className: gt }),
              a().createElement("div", { className: pt }),
              a().createElement("div", { className: Ct }),
              a().createElement("div", { style: r, className: Bt }),
            );
          },
          St = "SwitchEquipment_base_1a",
          ft = "SwitchEquipment_base__disabled_73",
          vt = "SwitchEquipment_cover_b3",
          wt = ({
            onClick: e,
            totalCount: t,
            currentIndex: u,
            states: i,
            isDisabled: r,
            groupId: s,
          }) => {
            const o = (0, n.useRef)(null),
              l = (0, n.useState)(!1),
              c = l[0],
              _ = l[1],
              d = (u + 1) % t,
              m = (0, n.useCallback)(() => {
                r || e({ groupId: s, currentIndex: d });
              }, [s, r, d, e]),
              E = (0, n.useCallback)(() => {
                r || (_(!0), _t.playHighlight());
              }, [r]),
              A = (0, n.useCallback)(() => {
                r || _(!1);
              }, [r]),
              b = h()(St, r && ft);
            return a().createElement(
              "div",
              {
                id: `switch-equipment-group-${s}`,
                className: b,
                onClick: m,
                onMouseEnter: E,
                onMouseLeave: A,
                ref: o,
              },
              Array.from({ length: t }, (e, t) =>
                a().createElement(ht, {
                  key: t,
                  id: t,
                  state: ue(i, t),
                  currentIndex: u,
                  isHovered: c,
                }),
              ),
              r && a().createElement("div", { className: vt }),
            );
          };
        var yt = u(2558);
        const xt = {
            base__enterUp: "GroupAnimation_base__enterUp_b3",
            animationEnterTop: "GroupAnimation_animationEnterTop_92",
            base__enterDown: "GroupAnimation_base__enterDown_f0",
            animationEnterDown: "GroupAnimation_animationEnterDown_73",
            base__exitUp: "GroupAnimation_base__exitUp_92",
            animationExitTop: "GroupAnimation_animationExitTop_89",
            base__exitDown: "GroupAnimation_base__exitDown_67",
            animationExitDown: "GroupAnimation_animationExitDown_02",
          },
          Tt = "up",
          kt = "down",
          It = ({ children: e, index: t, setSetupSwitching: u, disabled: i = !1 }) => {
            const r = (0, n.useRef)(1 - t),
              s = (0, n.useMemo)(() => {
                const e = ((u = t), (n = r.current), u === n ? "" : u > n ? kt : Tt);
                var u, n;
                const a = e && T(e);
                return i ? {} : { enter: xt[`base__enter${a}`], exit: xt[`base__exit${a}`] };
              }, [t, i]);
            return (
              (r.current = t),
              a().createElement(
                yt.Z,
                { className: xt.base },
                a().createElement(
                  re.Z,
                  {
                    timeout: 300,
                    key: t,
                    classNames: s,
                    onEnter: () => u(!0),
                    onExited: () => u(!1),
                  },
                  e,
                ),
              )
            );
          };
        let Rt, Ot;
        (!(function (e) {
          ((e.Hangar = "hangar"),
            (e.Setup = "setup"),
            (e.Compare = "compare"),
            (e.Battle = "battle"),
            (e.Respawn = "respawn"),
            (e.Prebattle = "prebattle"));
        })(Rt || (Rt = {})),
          (function (e) {
            ((e[(e.One = 1)] = "One"), (e[(e.Two = 2)] = "Two"), (e[(e.Three = 3)] = "Three"));
          })(Ot || (Ot = {})));
        const Mt = (e) => e.imageSource === R.images.gui.maps.icons.tanksetup.panel.empty(),
          Nt = (e) => e === Rt.Battle || e === Rt.Prebattle,
          Lt = (e) => !Nt(e),
          Pt = (e) => Nt(e) || e === Rt.Respawn,
          Ht = "shells",
          Gt = "consumables",
          $t = "battleAbilities",
          Wt = "toggleShells",
          zt = "toggleCamouflage",
          Ut = {
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
          Xt = [
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
        function jt() {
          return (
            (jt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            jt.apply(this, arguments)
          );
        }
        class Vt extends a().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && ct(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && ct(this.props.soundClick));
              }),
              (this._onMouseUp = (e) => (t) => {
                (e && e(t), this.setState({ click: !1 }));
              }),
              (this.handleFocus = () => this.setState({ focus: !0 })),
              (this.handleBlur = () => this.setState({ focus: !1 })));
          }
          render() {
            const e = this.props,
              t = e.caption,
              u = e.onClick,
              n = e.goto,
              i = e.side,
              r = e.type,
              s = e.classNames,
              o = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              _ = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    i = Object.keys(e);
                  for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(e, Xt)),
              m = h()(Ut.base, Ut[`base__${r}`], Ut[`base__${i}`], null == s ? void 0 : s.base),
              E = h()(Ut.icon, Ut[`icon__${r}`], Ut[`icon__${i}`], null == s ? void 0 : s.icon),
              A = h()(Ut.glow, null == s ? void 0 : s.glow),
              b = h()(Ut.caption, Ut[`caption__${r}`], null == s ? void 0 : s.caption),
              F = h()(Ut.goto, null == s ? void 0 : s.goto);
            return a().createElement(
              "div",
              jt(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: u,
                },
                d,
              ),
              "info" !== r && a().createElement("div", { className: Ut.shine }),
              a().createElement(
                "div",
                { className: E },
                a().createElement("div", { className: A }),
              ),
              a().createElement("div", { className: b }, t),
              n && a().createElement("div", { className: F }, n),
            );
          }
        }
        Vt.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        let Kt;
        !(function (e) {
          ((e.None = ""),
            (e.Tiny = "tiny"),
            (e.Small = "small"),
            (e.Medium = "medium"),
            (e.Large = "large"),
            (e.Huge = "huge"));
        })(Kt || (Kt = {}));
        const qt = "setup-content";
        function Yt(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Zt(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return Zt(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Zt(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        const Qt = (e, t = []) => {
            const u = document.getElementById("root");
            u && (u.style.cursor = e ? "grabbing" : "default");
            for (var n, a = Yt(t); !(n = a()).done;) {
              const t = n.value,
                u = document.getElementById(t);
              u && (u.style.pointerEvents = e ? "none" : "auto");
            }
          },
          Jt = (e, t, u) => {
            let n = "",
              a = 8e3;
            for (var i, r = Yt(u); !(i = r()).done;) {
              const e = i.value,
                u = Math.abs(e.centerX - t);
              u < a && ((n = e.id), (a = u));
            }
            return n;
          },
          eu = (e, t) => {
            const u = t.find((t) => t.id === e);
            return u ? u.centerX : 0;
          };
        let tu, uu;
        (!(function (e) {
          ((e.Waiting = "waiting"),
            (e.Active = "active"),
            (e.InEffect = "in"),
            (e.Rollback = "rollback"));
        })(tu || (tu = {})),
          (function (e) {
            ((e.Ready = "ready"),
              (e.DragStart = "start"),
              (e.Drag = "drag"),
              (e.Drop = "drop"),
              (e.DropExit = "exit"));
          })(uu || (uu = {})));
        const nu = (e) => `panel-${e}-section`,
          au = (e, t) => {
            const u = nu(e),
              n = t.filter((e) => e !== u);
            return { selfId: u, blockOnGrabIds: [qt, ...n] };
          },
          iu = ({
            baseId: e,
            slotsLength: t,
            handleSwap: u,
            setIsExitBlocked: a,
            syncInitiator: i,
          }) => {
            const r = ((e, t, u) => {
                const a = (0, n.useRef)([]),
                  i = (0, n.useRef)({ dragId: "", dropId: "", prevPotentialDropId: "" }),
                  r = (0, n.useState)({ activeDragId: "", potentialDropId: "" }),
                  s = r[0],
                  o = r[1],
                  l = (0, n.useCallback)((e) => {
                    i.current.dropId ||
                      i.current.prevPotentialDropId ||
                      ((i.current.prevPotentialDropId = e),
                      o({ activeDragId: e, potentialDropId: e }));
                  }, []),
                  c = (0, n.useCallback)((e, t) => {
                    if (a.current) {
                      const u = Jt(0, t, a.current);
                      u !== i.current.prevPotentialDropId &&
                        ((i.current.prevPotentialDropId = u),
                        o({ activeDragId: e, potentialDropId: u }));
                    }
                  }, []),
                  _ = (0, n.useCallback)((e, t) => {
                    if (a.current && t) {
                      const u = i.current,
                        n = Jt(0, t, a.current);
                      ((u.dropId = n),
                        (u.dragId = e),
                        (u.prevPotentialDropId = ""),
                        o({ activeDragId: e, potentialDropId: "" }),
                        n !== e && ct("cons_equipment_swipe"));
                    }
                  }, []),
                  d = (0, n.useCallback)(() => {
                    const e = i.current,
                      t = e.dragId,
                      u = e.dropId,
                      n = e.prevPotentialDropId;
                    (t || u || n) &&
                      ((i.current = { dragId: "", dropId: "", prevPotentialDropId: "" }),
                      o({ activeDragId: "", potentialDropId: "" }));
                  }, []),
                  m = (0, n.useCallback)(
                    (e) => {
                      const t = i.current.dropId;
                      t && t !== e ? u(e, t) : d();
                    },
                    [d, u],
                  ),
                  E = (0, n.useCallback)((e, t) => {
                    const u = a.current.find((t) => t.id === e);
                    u && t && (u.centerX = t);
                  }, []),
                  A = (0, n.useCallback)(
                    (e, t) => {
                      const u = t.dragId,
                        n = t.currentCenterX;
                      switch (e) {
                        case uu.Ready:
                          return E(u, n);
                        case uu.DragStart:
                          return l(u);
                        case uu.Drag:
                          return c(u, n);
                        case uu.Drop:
                          return _(u, n);
                        case uu.DropExit:
                          return m(u);
                        default:
                          return;
                      }
                    },
                    [l, c, _, m, E],
                  );
                return (
                  (0, n.useEffect)(() => {
                    if (e !== a.current.length) {
                      const u = new Array(e).fill(null);
                      a.current = u.map((e, u) => ({ id: `${t}-${u}`, centerX: 0 }));
                    }
                  }, [e, t]),
                  {
                    dragState: s,
                    handleGrabberAction: A,
                    getForceCenterX: (0, n.useCallback)((e) => {
                      const t = i.current,
                        u = t.dragId,
                        n = t.dropId;
                      return e === u ? eu(n, a.current) : e === n ? eu(u, a.current) : 0;
                    }, []),
                    resetDragResults: d,
                  }
                );
              })(t, e, u),
              s = r.dragState,
              o = r.handleGrabberAction,
              l = r.getForceCenterX,
              c = r.resetDragResults,
              _ = (0, n.useCallback)(
                (e, t) => {
                  if (a)
                    switch (e) {
                      case uu.DragStart:
                      case uu.Drag:
                        a(!0);
                        break;
                      default:
                        a(!1);
                    }
                  o(e, t);
                },
                [o, a],
              );
            return (
              (0, n.useEffect)(() => {
                a && a(!1);
              }, [a]),
              (0, n.useEffect)(() => {
                c();
              }, [i, c]),
              { handleGrabberAction: _, dragState: s, getForceCenterX: l }
            );
          },
          ru = {
            base: "Counter_base_9e",
            show: "Counter_show_be",
            base__big: "Counter_base__big_19",
            base__small: "Counter_base__small_3b",
            base__empty: "Counter_base__empty_98",
            base__animated: "Counter_base__animated_40",
            base__hidden: "Counter_base__hidden_56",
            hide: "Counter_hide_b6",
            bg: "Counter_bg_74",
            value: "Counter_value_3e",
            value__text: "Counter_value__text_d6",
            base__pattern: "Counter_base__pattern_71",
            plus: "Counter_plus_15",
            pattern: "Counter_pattern_83",
          },
          su = [
            "size",
            "value",
            "isEmpty",
            "fadeInAnimation",
            "hide",
            "maximumNumber",
            "className",
          ];
        function ou() {
          return (
            (ou =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            ou.apply(this, arguments)
          );
        }
        const lu = (e) => {
          let t = e.size,
            u = e.value,
            n = e.isEmpty,
            i = e.fadeInAnimation,
            r = e.hide,
            s = e.maximumNumber,
            o = e.className,
            l = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                i = Object.keys(e);
              for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, su);
          const c = n ? null : u,
            _ = "string" == typeof c;
          if ((c && !_ && c < 0) || 0 === c) return null;
          const d = c && !_ && c > s,
            m = h()(
              ru.base,
              ru[`base__${t}`],
              i && ru.base__animated,
              r && ru.base__hidden,
              !c && ru.base__pattern,
              n && ru.base__empty,
              o,
            );
          return a().createElement(
            "div",
            ou({ className: m }, l),
            a().createElement("div", { className: ru.bg }),
            a().createElement("div", { className: ru.pattern }),
            a().createElement(
              "div",
              { className: h()(ru.value, _ && ru.value__text) },
              d ? s : c,
              d && a().createElement("span", { className: ru.plus }, "+"),
            ),
          );
        };
        lu.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        const cu = "display",
          _u = "visible_change",
          du = _u,
          mu = "TopLabel_base_7f",
          Eu = "TopLabel_base__ready_00",
          Au = "TopLabel_text_d0",
          bu = "TopLabel_text__hangar_36",
          Fu = "TopLabel_text__shown_25",
          Du = "TopLabel_text__hidden_79",
          pu = "TopLabel_text__truncated_29",
          gu = (0, n.memo)(
            ({ panelType: e, text: t, parentRef: u, isTruncated: i = !1, show: r = !1 }) => {
              const s = (0, n.useRef)(!1),
                o = (0, n.useState)(!1),
                l = o[0],
                c = o[1];
              (0, n.useEffect)(() => {
                u || (r && !s.current && (s.current = !0), c(r));
              }, [r, u]);
              const _ = (0, n.useCallback)(() => {
                  ((s.current = !0), c(!0));
                }, []),
                d = (0, n.useCallback)(() => {
                  c(!1);
                }, []);
              (0, n.useEffect)(() => {
                const e = u && u.current;
                if (e)
                  return (
                    e.addEventListener("mouseenter", _),
                    e.addEventListener("mouseleave", d),
                    () => {
                      (e.removeEventListener("mouseenter", _),
                        e.removeEventListener("mouseleave", d));
                    }
                  );
              }, [u, _, d]);
              const m = h()(mu, s.current && Eu),
                E = h()(Au, e !== Rt.Setup && bu, i && pu, r && l ? Fu : Du);
              return a().createElement(
                "div",
                { className: m },
                a().createElement("div", { className: E }, t),
              );
            },
          ),
          Cu = "notUsableSection",
          Bu = "Section_base_8a",
          hu = "Section_base__hidden_f0",
          Su = "Section_label_73",
          fu = "Section_counter_8a",
          vu = "Section_configLabel_c9",
          wu = "Section_configText_eb",
          yu = "Section_configVehicleIcon_20";
        let xu;
        !(function (e) {
          ((e[(e.NonSet = 0)] = "NonSet"),
            (e[(e.Debug = 10)] = "Debug"),
            (e[(e.Info = 20)] = "Info"),
            (e[(e.Warning = 30)] = "Warning"));
        })(xu || (xu = {}));
        const Tu = "tooltip_watched";
        let ku;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(ku || (ku = {}));
        let Iu, Ru, Ou;
        (!(function (e) {
          ((e.HangarView = "hangar"),
            (e.SetupView = "setup_view"),
            (e.ProgressView = "progress_view"),
            (e.RewardsView = "rewards_view"),
            (e.RewardsSelectionView = "rewards_selection_view"),
            (e.SkillsView = "skills_view"),
            (e.AwardsView = "awards_view"),
            (e.ContainerView = "container_view"));
        })(Iu || (Iu = {})),
          (function (e) {
            ((e.AbilitiesCheckboxTooltip = "abilities_checkbox_tooltip"),
              (e.EpicWidgetTooltip = "epic_widget_tooltip"),
              (e.BannerPerformance = "banner_performance_tooltip"),
              (e.SkillPointsTooltip = "skill_points_tooltip"),
              (e.AbilityLevelsTooltip = "ability_levels_tooltip"),
              (e.SkillOrderTooltip = "skill_order_tooltip"),
              (e.SkillLevelTab = "skill_level_tab"),
              (e.RewardsButton = "rewards_button"),
              (e.RewardsButtonTooltip = "rewards_button_tooltip"),
              (e.RewardTooltip = "reward_tooltip"),
              (e.AwardsOkButton = "awards_ok"),
              (e.AwardsView = "awards_view"),
              (e.RewardsSelectionView = "rewards_selection_view"));
          })(Ru || (Ru = {})),
          (function (e) {
            ((e.Click = "click"), (e.Close = "close"));
          })(Ou || (Ou = {})));
        const Mu = "metrics",
          Nu = () => Date.now(),
          Lu = ({ partnerID: e, item: t, parentScreen: u, itemState: n, info: a }) => ({
            item: t,
            partnerID: e || null,
            parent_screen: u || null,
            item_state: n || null,
            additional_info: a || null,
          }),
          Pu = (e, t) => {
            const u = (0, n.useCallback)(
              (u, n = xu.Info, a) => {
                (a || (a = {}),
                  Object.keys(a).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: t,
                      action: u,
                      logLevel: n,
                      params: JSON.stringify(a),
                    }));
              },
              [e, t],
            );
            return (e, t, n) => u(e, t, n);
          },
          Hu = (e, t) => {
            const u = Pu(e, t),
              a = (0, n.useRef)(new Map()),
              i = (0, n.useRef)(new Map()),
              r = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  (void 0 !== t && t > 0) || a.current.set(e, Nu());
                },
                [a],
              ),
              s = (0, n.useCallback)(() => {
                (a.current.clear(), i.current.clear());
              }, [a, i]),
              o = (0, n.useCallback)(
                (e) => {
                  e &&
                    void 0 !== a.current.get(e) &&
                    void 0 === i.current.get(e) &&
                    i.current.set(e, Nu());
                },
                [a, i],
              ),
              l = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  if (void 0 === t) return;
                  const u = i.current.get(e);
                  if (void 0 === u) return;
                  i.current.delete(e);
                  const n = Nu() - u;
                  a.current.set(e, t + n);
                },
                [a, i],
              ),
              c = (0, n.useCallback)(
                (e, t = 0, n, r) => {
                  const s = a.current.get(e);
                  if (void 0 === s) return;
                  (void 0 !== i.current.get(e) && l(e), a.current.delete(e));
                  const o = (Nu() - s) / 1e3;
                  o <= t ||
                    ((r = ((e, t) => (void 0 === e && (e = {}), (e.timeSpent = t), e))(r, o)),
                    u(e, n, r));
                },
                [a, i, u, l],
              );
            return [
              (e) => r(e),
              (e, t, u, n) => c(e, t, u, n),
              () => s(),
              (e) => o(e),
              (e) => l(e),
            ];
          },
          Gu = (e) => {
            const t = Hu(e, Mu),
              u = t[0],
              a = t[1],
              i = t[2],
              r = t[3],
              s = t[4],
              o = (0, n.useCallback)(
                (e) => {
                  const t = e.action,
                    u = e.timeLimit,
                    n = e.logLevel;
                  a(t, u, n, Lu(e));
                },
                [a],
              );
            return [(e) => u(e), (e) => o(e), () => i(), (e) => r(e), (e) => s(e)];
          },
          $u = a().memo(function ({ className: e, children: t }) {
            const u = ((e, t, u, a) => {
                const i = Gu("epic_battle"),
                  r = i[0],
                  s = i[1];
                return [
                  (0, n.useCallback)(() => r(Tu), [r]),
                  (0, n.useCallback)(
                    () =>
                      s({
                        action: Tu,
                        timeLimit: 2,
                        item: e,
                        parentScreen: t,
                        itemState: u,
                        info: a,
                      }),
                    [s, e, t, u, a],
                  ),
                ];
              })(Ru.SkillOrderTooltip, Iu.SetupView),
              i = u[0],
              r = u[1];
            return a().createElement(
              Ue,
              {
                contentId: R.views.frontline.lobby.tooltips.SkillOrderTooltip("resId"),
                onMouseEnter: i,
                onMouseLeave: r,
              },
              a().createElement("div", { className: e }, t),
            );
          }),
          Wu = "SlotDivider_base_60",
          zu = () => a().createElement("div", { className: Wu }),
          Uu = ({ wrapper: e, children: t, when: u, withProps: n }) =>
            u ? a().createElement(e, n, t) : a().createElement(a().Fragment, null, t),
          Xu = {
            base: "Container_base_9a",
            base__grabbing: "Container_base__grabbing_73",
            base__hangar: "Container_base__hangar_ab",
            base__setup: "Container_base__setup_1c",
            base__compare: "Container_base__compare_0b",
            base__selected: "Container_base__selected_17",
            base__dragIn: "Container_base__dragIn_a6",
            base__dragInActive: "Container_base__dragInActive_e5",
            base__toggle: "Container_base__toggle_94",
            base__disabled: "Container_base__disabled_22",
          },
          ju = ({
            activeDragId: e,
            slotType: t,
            isSelected: u,
            isBorderActive: n,
            children: i,
            panelType: r,
            isDisabled: s,
            isPotentialDrop: o,
            onClick: l,
          }) => {
            const c = h()(
              Xu.base,
              !e && Xu[`base__${r}`],
              t && Xu[`base__${t}`],
              u && !o && !n && Xu.base__selected,
              o && Xu["base__dragIn" + (u ? "Active" : "")],
              s && Xu.base__disabled,
            );
            return a().createElement("div", { className: c, onClick: l }, i);
          },
          Vu = {
            base: "Bonus_base_dd",
            base__fitting: "Bonus_base__fitting_d1",
            icon: "Bonus_icon_3b",
            icon__battleBooster: "Bonus_icon__battleBooster_66",
            icon__battleBoosterReplace: "Bonus_icon__battleBoosterReplace_8d",
            icon__equipmentPlus: "Bonus_icon__equipmentPlus_48",
            icon__builtInEquipment: "Bonus_icon__builtInEquipment_77",
            icon__equipmentModernized: "Bonus_icon__equipmentModernized_76",
            icon__equipmentTrophyBasic: "Bonus_icon__equipmentTrophyBasic_a4",
            icon__equipmentTrophyUpgraded: "Bonus_icon__equipmentTrophyUpgraded_6d",
          },
          Ku = a().memo(({ isTemporary: e, overlayType: t, overlaySource: u }) => {
            const i = h()(Vu.base, e && Vu.base__fitting),
              r = h()(Vu.icon, Vu[`icon__${t}`]),
              s = (0, n.useMemo)(() => ({ backgroundImage: `url(${u})` }), [u]);
            return a().createElement(
              "div",
              { className: i },
              a().createElement("div", { className: r, style: s }),
            );
          }),
          qu = {
            base: "Level_base_57",
            base__level1: "Level_base__level1_c4",
            base__level2: "Level_base__level2_9c",
            base__level3: "Level_base__level3_39",
            base__level4: "Level_base__level4_e3",
            base__level5: "Level_base__level5_ea",
            base__level6: "Level_base__level6_5d",
            base__level7: "Level_base__level7_03",
            base__level8: "Level_base__level8_b5",
            base__level9: "Level_base__level9_d6",
            base__level10: "Level_base__level10_89",
          },
          Yu = ({ level: e }) => {
            const t = (0, n.useMemo)(
                () => ({
                  backgroundImage: `url(${R.images.gui.maps.icons.levels.$dyn(`tank_level_${e}`)})`,
                }),
                [e],
              ),
              u = h()(qu.base, qu[`base__level${e}`]);
            return a().createElement("div", { style: t, className: u });
          },
          Zu = "Inside_image_e5",
          Qu = "Inside_image__fitting_11",
          Ju = "Inside_warning_e4",
          en = "Inside_change_5a",
          tn = ({
            level: e,
            overlayType: t,
            isTemporary: u,
            withAttention: i,
            imageSource: r,
            isIncompatible: s,
          }) => {
            const o = (0, n.useMemo)(() => {
                const u = "equipmentModernized" === t ? `${t}_${e}_overlay` : `${t}_overlay`;
                return R.images.gui.maps.icons.quests.bonuses.small.$dyn(u);
              }, [t, e]),
              l = (0, n.useMemo)(() => ({ backgroundImage: `url(${r})` }), [r]),
              c = !o && Boolean(t) && e;
            return a().createElement(
              "div",
              null,
              c && a().createElement(Yu, { level: e }),
              a().createElement("div", { className: h()(Zu, (u || i) && Qu), style: l }),
              i && a().createElement("div", { className: Ju }),
              s && a().createElement("div", { className: en }),
              o && a().createElement(Ku, { isTemporary: u, overlaySource: o, overlayType: t }),
            );
          },
          un = "Grabber_base_cf",
          nn = "Grabber_base__enabled_b0",
          an = "Grabber_base__waitingUpdate_1d",
          rn = "Grabber_base__updating_f1",
          sn = "Grabber_base__active_71",
          on = "Grabber_base__exit_1f",
          ln = "Grabber_base__showAnimation_d9",
          cn = a().memo(
            ({
              children: e,
              id: t,
              containerRef: u,
              isEnabled: i = !0,
              onClick: r,
              forceCenterX: s,
              isUpdateAvailable: o,
              handleAction: l,
              blockOnGrabIds: c = [],
            }) => {
              const _ = me().mediaSize,
                d = (0, n.useRef)({
                  actualX: 0,
                  clickCenterOffset: 0,
                  dropCenterX: 0,
                  grabActivationPassed: !1,
                  isDragActive: !1,
                  id: t,
                }),
                m = (0, n.useRef)({
                  isValid: !1,
                  startX: 0,
                  startCenterX: 0,
                  minXRestriction: 0,
                  maxXRestriction: 8e3,
                }),
                E = (0, n.useRef)(null),
                A = (0, n.useState)(!1),
                b = A[0],
                F = A[1],
                g = (0, n.useState)(0),
                B = g[0],
                S = g[1],
                f = 0 !== s && i;
              (0, n.useEffect)(() => {
                if (((m.current.isValid = !1), t))
                  return w(() => {
                    const e = E.current,
                      n = u.current;
                    if (n && e) {
                      const u = e.getBoundingClientRect(),
                        a = n.getBoundingClientRect(),
                        i = u.left + 0.5 * u.width;
                      ((m.current = {
                        isValid: !0,
                        minXRestriction: a.left,
                        maxXRestriction: a.left + a.width,
                        startX: u.left,
                        startCenterX: i,
                      }),
                        l(uu.Ready, { dragId: t, currentCenterX: i }));
                    }
                  });
              }, [_]);
              const v = (0, n.useCallback)(
                  (e) => {
                    ((d.current.isDragActive = e),
                      F(e),
                      d.current.grabActivationPassed && !e && Qt(!1, c));
                  },
                  [c],
                ),
                y = (0, n.useCallback)(() => {
                  (l(uu.DragStart, { dragId: d.current.id }),
                    (d.current.grabActivationPassed = !0),
                    Qt(!0, c));
                }, [l, c]),
                x = (0, n.useCallback)((e) => {
                  const t = d.current,
                    u = m.current,
                    n = u.startX,
                    a = u.startCenterX,
                    i = u.minXRestriction,
                    r = u.maxXRestriction,
                    s = a - n,
                    o = e - t.clickCenterOffset;
                  t.dropCenterX = ((e, t, u, n) => {
                    const a = u + t,
                      i = n - t;
                    return e < a ? a : e > i ? i : e;
                  })(o, s, i, r);
                }, []),
                T = (0, n.useCallback)(
                  (e) => {
                    const t = d.current,
                      u = m.current;
                    0 === e.button &&
                      !t.isDragActive &&
                      u.isValid &&
                      i &&
                      !o &&
                      E.current &&
                      ((t.actualX = e.clientX),
                      (t.clickCenterOffset = t.actualX - u.startCenterX),
                      v(!0));
                  },
                  [i, o, v],
                ),
                k = (0, n.useCallback)(() => {
                  !r || (i && m.current.isValid) || r();
                }, [i, r]),
                I = (0, n.useCallback)(
                  (e) => {
                    const t = d.current;
                    e.target === E.current &&
                      t.grabActivationPassed &&
                      ((t.grabActivationPassed = !1),
                      setTimeout(() => l(uu.DropExit, { dragId: t.id })));
                  },
                  [l],
                );
              (C(p.n.ESCAPE, () => v(!1)),
                (0, n.useEffect)(() => {
                  i && s && S(0);
                }, [s, i]));
              const R = !b && d.current.grabActivationPassed;
              ((0, n.useEffect)(() => {
                d.current.id = t;
              }, [t]),
                (0, n.useEffect)(() => {
                  R && l(uu.Drop, { dragId: d.current.id, currentCenterX: d.current.dropCenterX });
                }, [R, l]),
                (0, n.useEffect)(() => {
                  const e = E.current;
                  if (f && e)
                    return (
                      e.addEventListener("transitionend", I),
                      () => {
                        e.removeEventListener("transitionend", I);
                      }
                    );
                }, [f, I]),
                (0, n.useEffect)(() => {
                  if (i && b && d.current.id) {
                    const e = D.O.client.events.mouse.up(([e, t]) => {
                        if ("outside" === t) return v(!1);
                        const u = d.current,
                          n = e.clientX;
                        (n === u.actualX && 0 === e.button && !d.current.grabActivationPassed
                          ? r && r()
                          : d.current.grabActivationPassed && x(n),
                          d.current.isDragActive && v(!1));
                      }),
                      t = D.O.client.events.mouse.move(([e]) => {
                        const t = d.current;
                        if ((0 === e.clientX && 0 === e.clientY) || !t.isDragActive) return;
                        const u = e.clientX,
                          n = t.grabActivationPassed;
                        (!n && y(),
                          u !== t.actualX &&
                            ((t.actualX = u),
                            x(u),
                            n && l(uu.Drag, { dragId: t.id, currentCenterX: t.dropCenterX }),
                            S(t.dropCenterX - m.current.startCenterX)));
                      });
                    return () => {
                      (t(), e());
                    };
                  }
                }, [y, l, b, i, r, v, x]));
              const O = (0, n.useMemo)(
                  () => (s ? { left: s - m.current.startCenterX } : { left: B }),
                  [B, s],
                ),
                M = i ? h()(un, nn, b && sn, R && on, f && an, s && rn) : h()(un, s && ln);
              return a().createElement(
                "div",
                { id: t, ref: E, onClick: k, onMouseDown: T, className: M, style: O },
                e,
              );
            },
          );
        let _n;
        !(function (e) {
          ((e[(e.Normal = 0)] = "Normal"),
            (e[(e.Current = 1)] = "Current"),
            (e[(e.Next = 2)] = "Next"));
        })(_n || (_n = {}));
        const dn = "KeyLabel_base_ec",
          mn = "KeyLabel_base__current_c2",
          En = "KeyLabel_base__next_fa",
          An = ({ text: e, show: t, panelType: u, shellState: n }) => {
            if (!e) return null;
            e = "KEY_NONE" === e ? ".." : R.strings.readable_key_names.$dyn(e);
            const i = h()(dn, n === _n.Current && mn, n === _n.Next && En);
            return a().createElement(
              "div",
              { className: i },
              a().createElement(gu, { isTruncated: !0, text: e, show: t, panelType: u }),
            );
          },
          bn = ({ children: e, slotType: t, slotId: u, isEnabled: i = !0 }) => {
            const r = (0, n.useMemo)(() => ({ slotType: t, slotId: u }), [t, u]);
            return a().createElement(
              Ve,
              { isEnabled: i, args: r },
              a().createElement("div", null, e),
            );
          },
          Fn = "Close_base_f3",
          Dn = "Close_base__invisible_0e",
          pn = "Close_base__shown_a2",
          gn = "Close_base__hover_6d",
          Cn = "Close_base__down_2b",
          Bn = (0, n.memo)(
            ({
              id: e,
              show: t = !0,
              onClick: u,
              soundHover: i = "highlight",
              soundClick: r = "play",
            }) => {
              const s = (0, n.useState)(!1),
                o = s[0],
                l = s[1],
                c = (0, n.useState)(!1),
                _ = c[0],
                d = c[1],
                m = (0, n.useState)(!1),
                E = m[0],
                A = m[1],
                b = (0, n.useCallback)((e) => {
                  e.stopPropagation();
                }, []),
                F = (0, n.useCallback)(() => {
                  (d(!0), i && ct(i));
                }, [i]),
                D = (0, n.useCallback)(() => {
                  (l(!1), d(!1));
                }, []),
                p = (0, n.useCallback)(
                  (e) => {
                    t && 0 === e.button && (l(!0), r && ct(r));
                  },
                  [t, r],
                ),
                g = (0, n.useCallback)(
                  (e) => {
                    t && 0 === e.button && u && u();
                  },
                  [t, u],
                );
              (0, n.useEffect)(
                () =>
                  w(() => {
                    A(!0);
                  }),
                [],
              );
              const C = h()(Fn, !E && Dn, E && t && pn, o && Cn, _ && gn);
              return a().createElement("div", {
                id: e,
                onMouseOver: F,
                onMouseLeave: D,
                onMouseDown: p,
                onMouseUp: g,
                className: C,
                onClick: b,
              });
            },
          ),
          hn = "Slot_base_3a",
          Sn = "Slot_label_e6",
          fn = "Slot_close_bb",
          vn = "Slot_disabled_5d",
          wn = "Slot_shadow_a7",
          yn = "Slot_category_2c";
        let xn;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(xn || (xn = {}));
        const Tn = ({
            children: e,
            contentID: t,
            decoratorID: u = 0,
            targetId: a = 0,
            args: i,
            isEnabled: r = !0,
            onMouseDown: s,
          }) => {
            const o = (0, n.useCallback)(() => {
                ((0, c.c9)(c.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: a,
                  isMouseEvent: !0,
                  on: !0,
                  args: i,
                }),
                  _t.playYes());
              }, [i, t, u, a]),
              l = (0, n.useCallback)(() => {
                (0, c.c9)(c.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: a,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, u, a]),
              _ = (0, n.useCallback)(
                (e) => {
                  (s && s(e), ((e) => e.button === xn.RIGHT)(e) && o());
                },
                [s, o],
              );
            return (
              (0, n.useEffect)(() => {
                !1 === r && l();
              }, [r, l]),
              r ? (0, n.cloneElement)(e, { onMouseDown: _ }) : e
            );
          },
          kn = ["children"];
        function In() {
          return (
            (In =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            In.apply(this, arguments)
          );
        }
        const Rn = (e) => {
            let t = e.children,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, kn);
            return a().createElement(
              Tn,
              In({}, u, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          On = "select",
          Mn = "undo",
          Nn = "swap",
          Ln = "demount",
          Pn = "demount_from_setups",
          Hn = "destroy",
          Gn = 1600;
        let $n;
        !(function (e) {
          ((e.RIGHT = "Right"),
            (e.LEFT = "Left"),
            (e.SWAP = "Swap"),
            (e.FITTING = "Fitting"),
            (e.FITTING_REMOVE = "FittingRemove"),
            (e.FADE = "Fade"),
            (e.DESTROY = "Destroy"),
            (e.DEMOUNT = "Demount"));
        })($n || ($n = {}));
        const Wn = {
            [Nn]: 200,
            [Mn]: 250,
            [On]: 250,
            [Hn]: 1400,
            [Ln]: Gn,
            [Pn]: Gn,
            demount_from_setup: Gn,
          },
          zn = "BackEffects_shine_f6",
          Un = "BackEffects_sparks_55",
          Xn = "BackEffects_nut_79",
          jn = "BackEffects_wrench_5a",
          Vn = { enterActive: "BackEffects_shine__enterActive_54" },
          Kn = { enterActive: "BackEffects_sparks__enterActive_79" },
          qn = { enterActive: "BackEffects_nut__enterActive_b8" },
          Yn = { enterActive: "BackEffects_wrench__enterActive_ca" },
          Zn = [Ln, Pn],
          Qn = a().memo(({ in: e, actionType: t }) =>
            a().createElement(
              a().Fragment,
              null,
              a().createElement(
                re.Z,
                { in: e, timeout: 200, classNames: Vn },
                a().createElement("div", { className: zn }),
              ),
              a().createElement(
                re.Z,
                { in: e, timeout: 400, classNames: Kn },
                a().createElement("div", { className: Un }),
              ),
              Zn.includes(t) &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement(
                    re.Z,
                    { in: e, timeout: 600, classNames: qn },
                    a().createElement("div", { className: Xn }),
                  ),
                  a().createElement(
                    re.Z,
                    { in: e, timeout: 600, classNames: Yn },
                    a().createElement("div", { className: jn }),
                  ),
                ),
            ),
          ),
          Jn = "ColorMask_base_60",
          ea = "ColorMask_base__enterActive_62",
          ta = ({ in: e, maskImage: t }) => {
            const u = (0, n.useMemo)(() => ({ enterActive: ea }), []),
              i = (0, n.useMemo)(() => ({ maskImage: `url(${t})` }), [t]);
            return a().createElement(
              re.Z,
              { in: e, timeout: 1200, classNames: u },
              a().createElement("div", { className: Jn, style: i }),
            );
          },
          ua = {
            base__exitLeft: "SlotTransitions_base__exitLeft_d8",
            "animation-left": "SlotTransitions_animation-left_27",
            base__exitLeftFade: "SlotTransitions_base__exitLeftFade_53",
            "animation-fade": "SlotTransitions_animation-fade_ce",
            base__enterRight: "SlotTransitions_base__enterRight_bb",
            "animation-right": "SlotTransitions_animation-right_31",
            base__enterRightFade: "SlotTransitions_base__enterRightFade_63",
            base__exitRight: "SlotTransitions_base__exitRight_b9",
            base__enterLeft: "SlotTransitions_base__enterLeft_e9",
            base__exitRightSwap: "SlotTransitions_base__exitRightSwap_64",
            "animation-right-long": "SlotTransitions_animation-right-long_bd",
            base__enterRightSwap: "SlotTransitions_base__enterRightSwap_5e",
            base__enterLeftSwap: "SlotTransitions_base__enterLeftSwap_da",
            "animation-left-long": "SlotTransitions_animation-left-long_ec",
            base__exitLeftSwap: "SlotTransitions_base__exitLeftSwap_c3",
            base__exitFade: "SlotTransitions_base__exitFade_4c",
            base__enterFade: "SlotTransitions_base__enterFade_77",
            base: "SlotTransitions_base_6d",
            base__enter: "SlotTransitions_base__enter_54",
            base__enterFitting: "SlotTransitions_base__enterFitting_c7",
            baseShells__exitLeft: "SlotTransitions_baseShells__exitLeft_1e",
            "animation-left-shells": "SlotTransitions_animation-left-shells_0d",
            baseShells__enterRight: "SlotTransitions_baseShells__enterRight_66",
            "animation-right-shells": "SlotTransitions_animation-right-shells_7c",
            baseShells__exitRight: "SlotTransitions_baseShells__exitRight_e4",
            baseShells__enterLeft: "SlotTransitions_baseShells__enterLeft_94",
            baseShells__exitRightSwap: "SlotTransitions_baseShells__exitRightSwap_fd",
            "animation-right-long-shells": "SlotTransitions_animation-right-long-shells_41",
            baseShells__enterRightSwap: "SlotTransitions_baseShells__enterRightSwap_41",
            baseShells__enterLeftSwap: "SlotTransitions_baseShells__enterLeftSwap_19",
            "animation-left-long-shells": "SlotTransitions_animation-left-long-shells_00",
            baseShells__exitLeftSwap: "SlotTransitions_baseShells__exitLeftSwap_04",
            baseShells__exitFade: "SlotTransitions_baseShells__exitFade_1b",
            baseShells__enterFade: "SlotTransitions_baseShells__enterFade_72",
            baseOptDevices__exitLeft: "SlotTransitions_baseOptDevices__exitLeft_fe",
            baseOptDevices__exitLeftFade: "SlotTransitions_baseOptDevices__exitLeftFade_8a",
            baseOptDevices__enterRight: "SlotTransitions_baseOptDevices__enterRight_5d",
            baseOptDevices__enterRightFade: "SlotTransitions_baseOptDevices__enterRightFade_2c",
            baseOptDevices__exitRight: "SlotTransitions_baseOptDevices__exitRight_72",
            baseOptDevices__enterLeft: "SlotTransitions_baseOptDevices__enterLeft_0f",
            baseOptDevices__exitRightSwap: "SlotTransitions_baseOptDevices__exitRightSwap_09",
            baseOptDevices__enterRightSwap: "SlotTransitions_baseOptDevices__enterRightSwap_04",
            baseOptDevices__enterLeftSwap: "SlotTransitions_baseOptDevices__enterLeftSwap_52",
            baseOptDevices__exitLeftSwap: "SlotTransitions_baseOptDevices__exitLeftSwap_e9",
            baseOptDevices__enterFitting: "SlotTransitions_baseOptDevices__enterFitting_8b",
            "animation-fitting": "SlotTransitions_animation-fitting_24",
            baseOptDevices__exitFittingRemove:
              "SlotTransitions_baseOptDevices__exitFittingRemove_fc",
            "animation-fitting-remove": "SlotTransitions_animation-fitting-remove_e0",
            baseOptDevices__exitActiveFitting:
              "SlotTransitions_baseOptDevices__exitActiveFitting_d0",
            baseOptDevices__exitDestroy: "SlotTransitions_baseOptDevices__exitDestroy_c9",
            "animation-destroy": "SlotTransitions_animation-destroy_12",
            baseOptDevices__enterDestroy: "SlotTransitions_baseOptDevices__enterDestroy_19",
            baseOptDevices__exitDemount: "SlotTransitions_baseOptDevices__exitDemount_e3",
            "animation-bright-up": "SlotTransitions_animation-bright-up_8e",
            "animation-demount": "SlotTransitions_animation-demount_d8",
            baseOptDevices__enterDemount: "SlotTransitions_baseOptDevices__enterDemount_8a",
            baseOptDevices__exitFade: "SlotTransitions_baseOptDevices__exitFade_10",
            baseOptDevices__enterFade: "SlotTransitions_baseOptDevices__enterFade_cf",
            baseOptDevices__enterDemountFade: "SlotTransitions_baseOptDevices__enterDemountFade_57",
            baseConsumables__exitLeft: "SlotTransitions_baseConsumables__exitLeft_d9",
            baseConsumables__exitLeftFade: "SlotTransitions_baseConsumables__exitLeftFade_4f",
            baseConsumables__enterRight: "SlotTransitions_baseConsumables__enterRight_02",
            baseConsumables__enterRightFade: "SlotTransitions_baseConsumables__enterRightFade_c6",
            baseConsumables__exitRight: "SlotTransitions_baseConsumables__exitRight_39",
            baseConsumables__enterLeft: "SlotTransitions_baseConsumables__enterLeft_97",
            baseConsumables__exitRightSwap: "SlotTransitions_baseConsumables__exitRightSwap_8a",
            baseConsumables__enterRightSwap: "SlotTransitions_baseConsumables__enterRightSwap_28",
            baseConsumables__enterLeftSwap: "SlotTransitions_baseConsumables__enterLeftSwap_8e",
            baseConsumables__exitLeftSwap: "SlotTransitions_baseConsumables__exitLeftSwap_0e",
            baseConsumables__enterFitting: "SlotTransitions_baseConsumables__enterFitting_13",
            baseConsumables__exitFittingRemove:
              "SlotTransitions_baseConsumables__exitFittingRemove_01",
            baseConsumables__exitActiveFitting:
              "SlotTransitions_baseConsumables__exitActiveFitting_10",
            baseConsumables__exitFade: "SlotTransitions_baseConsumables__exitFade_5b",
            baseConsumables__enterFade: "SlotTransitions_baseConsumables__enterFade_bd",
            baseBattleAbilities__exitLeft: "SlotTransitions_baseBattleAbilities__exitLeft_52",
            baseBattleAbilities__exitLeftFade:
              "SlotTransitions_baseBattleAbilities__exitLeftFade_a9",
            baseBattleAbilities__enterRight: "SlotTransitions_baseBattleAbilities__enterRight_7b",
            baseBattleAbilities__enterRightFade:
              "SlotTransitions_baseBattleAbilities__enterRightFade_d3",
            baseBattleAbilities__exitRight: "SlotTransitions_baseBattleAbilities__exitRight_fc",
            baseBattleAbilities__enterLeft: "SlotTransitions_baseBattleAbilities__enterLeft_97",
            baseBattleAbilities__exitRightSwap:
              "SlotTransitions_baseBattleAbilities__exitRightSwap_7d",
            baseBattleAbilities__enterRightSwap:
              "SlotTransitions_baseBattleAbilities__enterRightSwap_e5",
            baseBattleAbilities__enterLeftSwap:
              "SlotTransitions_baseBattleAbilities__enterLeftSwap_ca",
            baseBattleAbilities__exitLeftSwap:
              "SlotTransitions_baseBattleAbilities__exitLeftSwap_c0",
            baseBattleAbilities__enterFitting:
              "SlotTransitions_baseBattleAbilities__enterFitting_de",
            baseBattleAbilities__exitFittingRemove:
              "SlotTransitions_baseBattleAbilities__exitFittingRemove_bc",
            baseBattleAbilities__exitActiveFitting:
              "SlotTransitions_baseBattleAbilities__exitActiveFitting_3d",
            baseBattleAbilities__exitFade: "SlotTransitions_baseBattleAbilities__exitFade_21",
            baseBattleAbilities__enterFade: "SlotTransitions_baseBattleAbilities__enterFade_15",
            baseBattleBoosters__enterFitting: "SlotTransitions_baseBattleBoosters__enterFitting_56",
            baseBattleBoosters__exitFittingRemove:
              "SlotTransitions_baseBattleBoosters__exitFittingRemove_e5",
            baseBattleBoosters__exitActiveFitting:
              "SlotTransitions_baseBattleBoosters__exitActiveFitting_f1",
          },
          na = { enter: ua.base__enter, exit: ua.base__enter },
          aa = a().memo(
            ({
              children: e,
              slotIndex: t,
              uniqueKey: u,
              slotType: i,
              isEmpty: r = !1,
              imageSource: s,
              itemInstalledSetupIdx: o,
            }) => {
              const l = G("model.lastSlotAction"),
                c = l.leftID,
                _ = l.rightID,
                d = l.leftIntCD,
                m = l.rightIntCD,
                E = l.actionType,
                A = l.intCD,
                b = (0, n.useState)(!0),
                F = b[0],
                D = b[1],
                p = (0, n.useState)(!0),
                g = p[0],
                C = p[1],
                B = (0, n.useState)(s),
                h = B[0],
                S = B[1],
                f = (0, n.useState)(u),
                v = f[0],
                w = f[1],
                y = (0, n.useState)(o),
                x = y[0],
                T = y[1],
                k = (0, n.useRef)(),
                I = (0, n.useRef)(),
                R = (A === u || A === v) && x !== o && [Hn, Ln, Pn].includes(E),
                O = -1 === d || -1 === m,
                M = i ? `base${i[0].toUpperCase() + i.slice(1)}` : "base",
                N = Wn[E] || 0;
              ((0, n.useEffect)(
                () => () => {
                  (k.current && clearTimeout(k.current), I.current && clearTimeout(I.current));
                },
                [],
              ),
                (0, n.useEffect)(() => {
                  r || S(s);
                }, [r, s]));
              const L = (0, n.useCallback)(
                  (e) => {
                    const u = Object.assign({}, na);
                    switch (E) {
                      case Nn: {
                        const e = c === t ? $n.RIGHT : $n.LEFT,
                          n = _ - c != 1 ? $n.SWAP : "";
                        ((u.enterDone = ua[`${M}__enter${e}${n}`]),
                          (u.exit = ua[`${M}__exit${e}${n}`]),
                          O &&
                            (r
                              ? (u.enterDone = ua[`${M}__enter${$n.FADE}`])
                              : (u.exit = ua[`${M}__exit${$n.FADE}`])));
                        break;
                      }
                      case Hn:
                        ((u.enterDone = ua[`${M}__enter${$n.DESTROY}`]),
                          (u.exit = ua[`${M}__exit${$n.DESTROY}`]),
                          (k.current = setTimeout(() => D(!0), 900)),
                          C(!0));
                        break;
                      case Pn:
                      case Ln:
                        ((u.enter = ua[`${M}__enter${$n.DEMOUNT}${$n.FADE}`]),
                          (u.exit = ua[`${M}__exit${$n.DEMOUNT}`]),
                          (k.current = setTimeout(() => D(!0), 900)));
                        break;
                      case On:
                      case Mn:
                        if (i !== Ht) {
                          const e = E === On ? $n.FITTING : $n.FITTING_REMOVE;
                          ((u.enter = ua[`${M}__enter${e}`]),
                            (u.exit = ua[`${M}__exit${e}`]),
                            (u.exitActive = ua[`${M}__exitActive${$n.FITTING}`]));
                        } else
                          ((u.enterDone = ua[`${M}__enter${$n.FADE}`]),
                            (u.exit = ua[`${M}__exit${$n.FADE}`]));
                        break;
                      default:
                        return e;
                    }
                    return a().cloneElement(e, { classNames: u, timeout: N });
                  },
                  [E, i, M, N, c, t, _, r, O],
                ),
                P = (0, n.useCallback)(
                  (e) => {
                    I.current = setTimeout(() => {
                      ((e.className = ""), e.classList.add(ua.base), w(u), T(o));
                    }, N);
                  },
                  [N, u, o],
                ),
                H = (0, n.useCallback)(() => {
                  (D(!1), C(!1));
                }, []);
              return a().createElement(
                a().Fragment,
                null,
                a().createElement(
                  yt.Z,
                  { component: null, childFactory: L },
                  a().createElement(
                    re.Z,
                    {
                      key: u,
                      timeout: N,
                      classNames: na,
                      onEntered: P,
                      onExiting: H,
                      unmountOnExit: !0,
                    },
                    a().createElement("div", { className: ua.base }, e),
                  ),
                ),
                R &&
                  a().createElement(
                    a().Fragment,
                    null,
                    a().createElement(Qn, { in: F, actionType: E }),
                    a().createElement(ta, { in: g, maskImage: h }),
                  ),
              );
            },
          ),
          ia = a().memo(
            ({
              intCD: e,
              id: t,
              itemInstalledSetupIdx: u,
              isMountedMoreThanOne: i,
              isInstalled: r,
              isDisabled: s,
              imageSource: o,
              isEmpty: l,
              slotIndex: c,
              slotType: _,
              isBootCamp: d,
              contextMenuDisabled: m,
              isSetupSwitching: E,
              children: A,
            }) => {
              const b = (0, n.useMemo)(
                () => ({
                  intCD: e,
                  slotType: _,
                  installedSlotId: t,
                  isMounted: r,
                  fieldType: 1,
                  itemInstalledSetupIdx: u,
                  itemInstalledSetupSlotIdx: t,
                  isMountedMoreThanOne: i,
                }),
                [e, _, t, u, r, i],
              );
              return a().createElement(
                aa,
                {
                  uniqueKey: e,
                  isEmpty: l,
                  slotIndex: c,
                  slotType: _,
                  imageSource: o,
                  itemInstalledSetupIdx: u,
                },
                a().createElement(
                  Rn,
                  { isEnabled: !(E || m || s || l || d), args: b },
                  a().createElement("div", null, A),
                ),
              );
            },
          ),
          ra = ({
            id: e,
            intCD: t,
            slotType: u,
            imageSource: i,
            isInstalled: r,
            itemInstalledSetupIdx: s,
            isMountedMoreThanOne: o,
            overlayType: l,
            keyName: c,
            slotIndex: _,
            level: d,
            isBootCamp: m,
            isSelected: E,
            isSetupSwitching: A,
            isSectionSelected: b,
            withAttention: F,
            onActiveSlotChanged: D,
            onSlotSelected: p,
            onActiveSlotRefChanged: g,
            onSlotClear: C,
            panelType: B,
            isDisabled: h = !1,
            isBorderActive: S,
            isIncompatible: f = !1,
            grabberId: v,
            containerRef: y,
            activeDragId: x,
            handleGrabberAction: T,
            forceLeftUpdate: k,
            potentialDropId: I,
            blockOnGrabIds: R,
            categoryImgSource: O,
            contextMenuDisabled: M,
          }) => {
            const N = B === Rt.Setup,
              L = !Pt(B),
              P = B === Rt.Compare,
              H = N && b && L,
              G = (0, n.useRef)(!1),
              $ = (0, n.useRef)(null),
              W = -1 === t;
            ((0, n.useEffect)(() => {
              if (!G.current && b && E)
                return w(() => {
                  (D && D($, u, e), (G.current = !0));
                });
              G.current = !0;
            }, [e, b, E, D, u]),
              (0, n.useEffect)(() => {
                E && g($);
              }, [E, g]));
            const z = ((e) => {
                const t = (0, n.useRef)(-1),
                  u = (0, n.useCallback)(
                    (u) => {
                      if (-1 === t.current) {
                        const n = e(u);
                        n &&
                          (t.current = window.setTimeout(() => {
                            t.current = -1;
                          }, n));
                      }
                    },
                    [e],
                  );
                return ((0, n.useEffect)(() => () => clearTimeout(t.current), []), u);
              })((0, n.useCallback)(() => (!E && L && !A && p(u, e), 500), [e, L, E, A, p, u])),
              U = (0, n.useCallback)(() => {
                h || z("");
              }, [z, h]),
              X = (0, n.useCallback)(() => {
                !E && !x && !h && _t.playHighlight();
              }, [E, x, h]);
            (0, n.useEffect)(() => {
              I && _t.playHighlight();
            }, [I]);
            const j = (0, n.useCallback)(() => {
                null == C || C(e, u);
              }, [e, C, u]),
              V = N && !r,
              K = Boolean(v && I === v),
              q = v && (H || P),
              Y = `${u}-slot-${e}`,
              Z = O && O.length > 0,
              Q = Z ? { backgroundImage: `url(${O})` } : {},
              J = {
                id: v,
                containerRef: y,
                isEnabled: !W,
                onClick: U,
                isUpdateAvailable: Boolean(x),
                handleAction: T,
                forceCenterX: k,
                blockOnGrabIds: R,
              },
              ee = {
                isEmpty: W,
                intCD: t,
                slotType: u,
                slotIndex: _,
                imageSource: i,
                isBootCamp: m,
                isDisabled: h,
                isInstalled: r,
                id: e,
                itemInstalledSetupIdx: s,
                isMountedMoreThanOne: o,
                contextMenuDisabled: M,
                isSetupSwitching: A,
              };
            return a().createElement(
              "div",
              { className: hn, onMouseEnter: X, id: Y },
              (b || P) &&
                !r &&
                a().createElement(
                  "div",
                  { className: fn },
                  a().createElement(Bn, { id: `close-${Y}`, show: !x, onClick: j }),
                ),
              a().createElement(
                bn,
                { slotType: u, slotId: e, isEnabled: !x && Lt(B) },
                a().createElement(
                  "div",
                  { ref: $ },
                  a().createElement(
                    ju,
                    {
                      activeDragId: x,
                      slotType: u,
                      isSelected: E,
                      isBorderActive: Boolean(S),
                      panelType: B,
                      isDisabled: h,
                      isPotentialDrop: K,
                      onClick: q ? void 0 : U,
                    },
                    L &&
                      a().createElement(
                        "div",
                        { className: Sn },
                        a().createElement(An, { text: c, show: Boolean(b), panelType: B }),
                      ),
                    a().createElement(
                      Uu,
                      { when: Boolean(q), wrapper: cn, withProps: J },
                      a().createElement(
                        Uu,
                        { when: L, wrapper: ia, withProps: ee },
                        a().createElement(tn, {
                          imageSource: i,
                          isIncompatible: f,
                          overlayType: l,
                          level: d,
                          isTemporary: V,
                          withAttention: F,
                        }),
                      ),
                    ),
                    Z &&
                      a().createElement(
                        a().Fragment,
                        null,
                        a().createElement("span", { className: wn }),
                        a().createElement("span", { className: yn, style: Q }),
                      ),
                    h && a().createElement("div", { className: vn }),
                  ),
                ),
              ),
            );
          },
          sa = "BattleAbilitySlot_base_74",
          oa = "BattleAbilitySlot_rank_01",
          la = ["rank"];
        const ca = (0, n.memo)((e) => {
            let t = e.rank,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, la);
            const i = (0, n.useMemo)(() => ({ backgroundImage: `url(${t})` }), [t]),
              r = h()(sa);
            return a().createElement(
              "div",
              { className: r },
              a().createElement(ra, u),
              t && a().createElement("div", { className: oa, style: i }),
            );
          }),
          _a = {
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
        let da, ma;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(da || (da = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(ma || (ma = {})));
        const Ea = ({
          children: e,
          size: t,
          isFocused: u,
          type: i,
          disabled: r,
          mixClass: s,
          soundHover: o,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: _,
          onMouseDown: d,
          onMouseUp: m,
          onMouseLeave: E,
          onClick: A,
        }) => {
          const b = (0, n.useRef)(null),
            F = (0, n.useState)(u),
            D = F[0],
            p = F[1],
            g = (0, n.useState)(!1),
            C = g[0],
            B = g[1],
            S = (0, n.useState)(!1),
            f = S[0],
            v = S[1],
            w = (0, n.useCallback)(() => {
              r || (b.current && (b.current.focus(), p(!0)));
            }, [r]),
            y = (0, n.useCallback)(
              (e) => {
                D && null !== b.current && !b.current.contains(e.target) && p(!1);
              },
              [D],
            ),
            x = (0, n.useCallback)(
              (e) => {
                r || (A && A(e));
              },
              [r, A],
            ),
            T = (0, n.useCallback)(
              (e) => {
                r || (null !== o && ct(o), c && c(e), v(!0));
              },
              [r, o, c],
            ),
            k = (0, n.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            I = (0, n.useCallback)(
              (e) => {
                r || (m && m(e), B(!1));
              },
              [r, m],
            ),
            O = (0, n.useCallback)(
              (e) => {
                r || (null !== l && ct(l), d && d(e), u && w(), B(!0));
              },
              [r, l, d, w, u],
            ),
            M = (0, n.useCallback)(
              (e) => {
                r || (E && E(e), B(!1));
              },
              [r, E],
            ),
            N = h()(
              _a.base,
              _a[`base__${i}`],
              {
                [_a.base__disabled]: r,
                [_a[`base__${t}`]]: t,
                [_a.base__focus]: D,
                [_a.base__highlightActive]: C,
                [_a.base__firstHover]: f,
              },
              s,
            ),
            L = h()(_a.state, _a.state__default);
          return (
            (0, n.useEffect)(
              () => (
                document.addEventListener("mousedown", y),
                () => {
                  document.removeEventListener("mousedown", y);
                }
              ),
              [y],
            ),
            (0, n.useEffect)(() => {
              p(u);
            }, [u]),
            a().createElement(
              "div",
              {
                ref: b,
                className: N,
                onMouseEnter: T,
                onMouseMove: k,
                onMouseUp: I,
                onMouseDown: O,
                onMouseLeave: M,
                onClick: x,
              },
              i !== da.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: _a.back }),
                  a().createElement("span", { className: _a.texture }),
                ),
              a().createElement(
                "span",
                { className: L },
                a().createElement("span", { className: _a.stateDisabled }),
                a().createElement("span", { className: _a.stateHighlightHover }),
                a().createElement("span", { className: _a.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: _a.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Ea.defaultProps = {
          type: da.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Aa = (0, n.memo)(Ea),
          ba = {
            base: "Specialization_base_ec",
            base__tiny: "Specialization_base__tiny_fe",
            base__small: "Specialization_base__small_a3",
            base__medium: "Specialization_base__medium_85",
            base__large: "Specialization_base__large_07",
            base__huge: "Specialization_base__huge_33",
            base__setup: "Specialization_base__setup_5e",
            base__correct: "Specialization_base__correct_4c",
            glow: "Specialization_glow_f0",
            icon: "Specialization_icon_3a",
            icon__tiny: "Specialization_icon__tiny_05",
            icon__small: "Specialization_icon__small_cf",
            icon__medium: "Specialization_icon__medium_ed",
            icon__large: "Specialization_icon__large_98",
            icon__huge: "Specialization_icon__huge_f7",
            specializationWrapper: "Specialization_specializationWrapper_bf",
            specializationButton: "Specialization_specializationButton_45",
          },
          Fa = ({
            name: e,
            isCorrect: t,
            isSpecializationActive: u = !0,
            isDynamic: i,
            mediaSize: r,
            isClickable: s,
            onSpecializationClick: o,
            index: l,
          }) => {
            const c = r !== Kt.None,
              _ = (0, n.useCallback)(() => {
                s && u && o && o(l);
              }, [l, s, u, o]),
              d = (0, n.useMemo)(() => {
                let u = "";
                c && (u = (r === Kt.Large || r === Kt.Huge ? Kt.Large : Kt.Medium) + "_");
                const n = `${u}${e}_${t ? "on" : "off"}`,
                  a = R.images.gui.maps.icons.specialization.$dyn(n);
                return a && { backgroundImage: `url(${a})` };
              }, [e, t, r, c]),
              m = (0, n.useMemo)(
                () => ({ spec: e, isDyn: i, isClickable: s, tooltip: "hangarSlotSpec" }),
                [e, i, s],
              );
            if (!d) return null;
            const E = h()(
                `specialization-${e}`,
                ba.base,
                c && ba[`base__${r}`],
                u && ba.base__setup,
                t && ba.base__correct,
              ),
              A = h()(ba.icon, c && ba[`icon__${r}`]),
              b = c ? "" : ba.specializationWrapper,
              F = a().createElement(
                "div",
                { key: e, className: E },
                a().createElement("div", { className: ba.glow }),
                a().createElement("div", { className: A, style: d }),
              );
            return a().createElement(
              Ve,
              { args: m },
              s && u
                ? a().createElement(
                    Aa,
                    {
                      size: ma.small,
                      type: da.ghost,
                      mixClass: ba.specializationButton,
                      onClick: _,
                    },
                    F,
                  )
                : a().createElement("div", { className: b }, F),
            );
          },
          Da = "Specializations_base_ab";
        function pa() {
          return (
            (pa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            pa.apply(this, arguments)
          );
        }
        const ga = ({
            specializations: e,
            isSpecializationActive: t = !0,
            isDynamic: u,
            mediaSize: n = Kt.None,
            activeSpecsMask: i,
            onSpecializationClick: r,
          }) =>
            e.length
              ? a().createElement(
                  "div",
                  { className: Da, key: i },
                  ne(e, (e, i) =>
                    a().createElement(
                      Fa,
                      pa({ index: i, key: e.name }, e, {
                        isSpecializationActive: t,
                        isDynamic: u,
                        mediaSize: n,
                        onSpecializationClick: r,
                      }),
                    ),
                  ),
                )
              : null,
          Ca = "OptDeviceSlot_base_14",
          Ba = "OptDeviceSlot_specializations_c3",
          ha = ["specializations", "activeSpecsMask", "isChangeSetupIndex", "isDynamic"];
        const Sa = (e) => {
            let t = e.specializations,
              u = e.activeSpecsMask,
              n = e.isChangeSetupIndex,
              i = e.isDynamic,
              r = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, ha);
            const s = F("model.ammunitionPanel", b.None).onSpecializationSelect,
              o = r.panelType === Rt.Setup || r.panelType === Rt.Compare,
              l = !Pt(r.panelType);
            return a().createElement(
              "div",
              { className: h()(Ca, t.length && !i && !n && "specializationsSlot") },
              l &&
                a().createElement(
                  "div",
                  { className: Ba },
                  a().createElement(ga, {
                    specializations: t,
                    isDynamic: i,
                    activeSpecsMask: u,
                    isSpecializationActive: o,
                    onSpecializationClick: (e) => {
                      s({ slotId: r.id, specializationIndex: e });
                    },
                  }),
                ),
              a().createElement(ra, r),
            );
          },
          fa = {
            base: "ToggleCamouflageSlot_base_17",
            base__grabbing: "ToggleCamouflageSlot_base__grabbing_79",
            base__hangar: "ToggleCamouflageSlot_base__hangar_e7",
            base__setup: "ToggleCamouflageSlot_base__setup_44",
            base__compare: "ToggleCamouflageSlot_base__compare_0d",
            base__selected: "ToggleCamouflageSlot_base__selected_0c",
            base__dragIn: "ToggleCamouflageSlot_base__dragIn_68",
            base__dragInActive: "ToggleCamouflageSlot_base__dragInActive_b1",
            base__toggle: "ToggleCamouflageSlot_base__toggle_fc",
            base__disabled: "ToggleCamouflageSlot_base__disabled_1e",
            image: "ToggleCamouflageSlot_image_ee",
            glow: "ToggleCamouflageSlot_glow_45",
            toggle: "ToggleCamouflageSlot_toggle_c2",
          },
          va = ({ id: e, isSelected: t, isLocked: u, onSlotSelected: i, panelType: r }) => {
            const s = zt,
              o = (0, n.useCallback)(() => {
                i(s, e);
              }, [e, i, s]),
              l = h()(fa.base, fa[`base__${r}`], u && fa.base__disabled, t && fa.base__toggle),
              c = (0, n.useMemo)(
                () => ({
                  backgroundImage: "url(R.images.gui.maps.icons.quests.bonuses.small.camouflage)",
                }),
                [],
              ),
              _ = (0, n.useMemo)(
                () => ({
                  backgroundImage: `url(R.images.gui.maps.icons.tanksetup.shells.icon_selected_${t ? "on" : "off"})`,
                }),
                [t],
              ),
              d = `toggle-camouflage-slot-${e}`;
            return a().createElement(
              bn,
              { slotType: s, slotId: e },
              a().createElement(
                "div",
                { id: d, className: l, onClick: o, onMouseEnter: _t.playHighlight },
                t && a().createElement("div", { className: fa.glow }),
                a().createElement("div", { className: fa.image, style: c }),
                a().createElement("div", { className: fa.toggle, style: _ }),
              ),
            );
          },
          wa = ["value", "sectionType"];
        function ya() {
          return (
            (ya =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            ya.apply(this, arguments)
          );
        }
        const xa = (e) => {
            let t = e.value,
              u = e.sectionType,
              n = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, wa);
            switch (u) {
              case "optDevices": {
                const e = t;
                return a().createElement(
                  Sa,
                  ya({}, e, n, {
                    specializations: e.specializations.specializations,
                    isDynamic: e.specializations.isDynamic,
                  }),
                );
              }
              case zt: {
                const e = t;
                return a().createElement(va, ya({}, n, e));
              }
              case $t: {
                const e = t;
                return a().createElement(ca, ya({}, n, e));
              }
              default:
                return a().createElement(ra, ya({}, n, t));
            }
          },
          Ta = "Slots_base_27",
          ka = ({
            slots: e,
            sectionType: t,
            panelType: u,
            isBorderActive: i,
            onActiveSlotChanged: r,
            isDisabled: s,
            isBootCamp: o,
            selectedSection: l,
            selectedSlot: c,
            syncInitiator: _,
            blockOnGrabIds: d,
            isChangeSetupIndex: m,
            setIsExitBlocked: E,
          }) => {
            const A = (0, n.useRef)(null),
              D = (0, n.useRef)(null),
              p = F("model.ammunitionPanel", b.None),
              g = p.onSectionSelect,
              C = p.onDragDropSwap,
              B = p.onSlotClear,
              S = (0, n.useCallback)(
                (e, u) => {
                  C({
                    sectionType: t,
                    dragId: Number(e[e.length - 1]),
                    dropId: Number(u[u.length - 1]),
                  });
                },
                [C, t],
              ),
              f = l === t,
              v = f ? c : -1,
              w = `${t}-${e.length}slots`,
              y = iu({
                baseId: w,
                slotsLength: e.length,
                handleSwap: S,
                setIsExitBlocked: E,
                syncInitiator: _,
              }),
              x = y.handleGrabberAction,
              T = y.dragState,
              k = y.getForceCenterX;
            (0, n.useEffect)(() => {
              f && -1 !== v && A.current && r(A, l, v);
            }, [r, f, l, v]);
            const I = (e, t) => {
                if ((s || _t.playClick(), "number" != typeof t))
                  return console.warn("selectedSlot is not a number");
                g({ selectedSlot: t, selectedSection: e });
              },
              R = (e) => {
                A.current = e ? e.current : null;
              },
              O = (e, t) => {
                B({ slotId: e, sectionType: t });
              };
            return a().createElement(
              "div",
              { id: w, ref: D, className: h()(Ta, t) },
              ie(e, (l, c) => {
                const _ = t === $t,
                  E = !_ && e.length > 1 ? `${w}-${c}` : "";
                return a().createElement(
                  n.Fragment,
                  { key: `${l.id}-${c}` },
                  c > 0 && a().createElement(zu, null),
                  a().createElement(xa, {
                    value: l,
                    sectionType: t,
                    panelType: u,
                    isSelected: v === l.id,
                    isSectionSelected: f,
                    isDisabled: s,
                    isBootCamp: o,
                    isBorderActive: i,
                    contextMenuDisabled: _,
                    slotType: t,
                    onActiveSlotChanged: r,
                    onSlotSelected: I,
                    onActiveSlotRefChanged: R,
                    onSlotClear: O,
                    slotIndex: c,
                    grabberId: E,
                    containerRef: D,
                    forceLeftUpdate: k(E),
                    activeDragId: T.activeDragId,
                    handleGrabberAction: x,
                    potentialDropId: T.potentialDropId,
                    blockOnGrabIds: d,
                    isSetupSwitching: m,
                    isChangeSetupIndex: m,
                  }),
                );
              }),
            );
          },
          Ia = ({
            type: e,
            slots: t,
            newItemsCount: u,
            isDisabled: i,
            panelType: r,
            onActiveSlotChanged: s,
            isBorderActive: o,
            isBootCamp: l = !0,
            selectedSection: c,
            selectedSlot: _,
            syncInitiator: d,
            sectionsIds: m,
            onBootcampPanelAppear: E,
            vehicle: A,
            vehicleType: b,
            isSetupSwitching: D,
            isChangeSetupIndex: p,
            classMix: g,
            setIsExitBlocked: C,
          }) => {
            const B = (0, n.useRef)(null),
              S = (0, n.useState)(l),
              f = S[0],
              y = S[1],
              x = (0, n.useMemo)(
                () =>
                  r === Rt.Setup
                    ? e === Gt
                      ? "AmmunitionSetupHangarEquipmentSlots"
                      : "AmmunitionSetupOptionalDeviceSlots"
                    : e === Gt
                      ? "HangarEquipmentSlots"
                      : "HangarOptionalDeviceSlots",
                [r, e],
              ),
              T = ((e, t) => {
                const u = F("tutorialModel.effects.items").filter((u) => {
                  if (!u) return !1;
                  const n = u.value,
                    a = window.__featureId.toString();
                  return n.componentId === e && n.type === t && n.viewId === a;
                });
                if (0 === u.length) return null;
                const n = Object.assign({}, u[0].value);
                return {
                  effect: n,
                  completeEffect: () => {
                    (tutorialModel.onEffectCompleted({
                      componentId: e,
                      viewId: window.__featureId.toFixed(0),
                      effectType: t,
                      effectBuilder: n.builder,
                    }),
                      t === cu && window.tutorialApi && window.tutorialApi.updateComponents());
                  },
                };
              })(x, cu);
            (0, n.useEffect)(
              () => (
                null !== T && y(!T.effect.visible),
                w(() => {
                  null !== T && T.completeEffect();
                })
              ),
              [T, e],
            );
            const k = v();
            (0, n.useEffect)(() => {
              k && (k.freeze(), k.resize());
            }, [t.length, k, x, f]);
            const I = ((e, t) => {
              const u = F("tutorialModel.triggers.items").filter((u) => {
                if (!u) return !1;
                const n = u.value,
                  a = n.triggers.filter((e) => e.value === t);
                return n.componentId === e && a.length > 0;
              });
              return 0 === u.length
                ? null
                : window.tutorialModel.foundComponents.items.some((t) => t.value.componentId === e)
                  ? {
                      trigger: u[0].value,
                      runTrigger: (u) => {
                        window.tutorialModel.onTriggerActivated({
                          componentId: e,
                          triggerType: t,
                          state: u,
                        });
                      },
                    }
                  : null;
            })("AmmunitionPanelBattleAbilities", du);
            (0, n.useEffect)(() => {
              null == I || I.runTrigger(!0);
            }, [I]);
            const O = c === e,
              M = au(e, m),
              N = M.selfId,
              L = M.blockOnGrabIds;
            ((0, n.useEffect)(() => {
              r === Rt.Hangar && y(l);
            }, [r, l]),
              (0, n.useEffect)(() => {
                if (l && !f && E)
                  return w(() => {
                    (E(), k && k.resize());
                  });
              }, [f, l, E, k]));
            const P =
                d >= 0 &&
                (function (e, t) {
                  if (Array.isArray(e)) return e.some(t);
                  for (let u = 0; u < e.length; u++) if (t(ue(e, u), u, e)) return !0;
                  return !1;
                })(t, (e) => e.intCD > 0),
              H = h()(
                Bu,
                g,
                f && hu,
                O && "sectionSelected",
                t.length > 1 && "multiSlot",
                P && "existFilledSlots",
              ),
              G =
                ((A && A.length > 0) || (b && b.length > 0)) && r !== Rt.Battle && r !== Rt.Respawn,
              $ = (0, n.useMemo)(
                () => ({
                  backgroundImage: b
                    ? `url(${R.images.gui.maps.icons.vehicleTypes.extraSmall.$dyn(b)})`
                    : "",
                }),
                [b],
              ),
              W = (0, n.useMemo)(
                () => ({
                  icon: a().createElement("span", { className: yu, style: $ }),
                  vehicle: A,
                }),
                [$, A],
              ),
              z =
                t.length > 0 &&
                r !== Rt.Compare &&
                r !== Rt.Battle &&
                r !== Rt.Respawn &&
                t.length > 0,
              U = R.strings.tank_setup.section.$dyn(e);
            if ("string" != typeof U)
              throw new Error(`No top label text for section type ${e} or it's not a string`);
            return a().createElement(
              "div",
              { id: D ? Cu : N, ref: B, className: H },
              G &&
                a().createElement(
                  $u,
                  { className: vu },
                  a().createElement(we, {
                    classMix: wu,
                    text: R.strings.tank_setup.categories.reserves.config(),
                    binding: W,
                  }),
                ),
              z &&
                a().createElement(
                  "div",
                  { className: Su },
                  a().createElement(gu, { text: U, parentRef: B, show: !O, panelType: r }),
                ),
              a().createElement(ka, {
                slots: t,
                sectionType: e,
                panelType: r,
                isBorderActive: o,
                onActiveSlotChanged: s,
                isDisabled: i,
                isBootCamp: l,
                syncInitiator: d,
                selectedSection: c,
                selectedSlot: _,
                blockOnGrabIds: L,
                isChangeSetupIndex: p,
                setIsExitBlocked: C,
              }),
              Boolean(u) &&
                a().createElement(
                  "div",
                  { className: fu },
                  a().createElement(lu, { value: u, size: "small", fadeInAnimation: !0 }),
                ),
            );
          },
          Ra = "Count_base_e4",
          Oa = "Count_base__zero_64",
          Ma = ({ count: e }) => {
            const t = h()(Ra, !e && Oa);
            return a().createElement("div", { className: t }, e);
          },
          Na = "ShellsSlot_base_05",
          La = "ShellsSlot_shell_ab",
          Pa = "ShellsSlot_shell__grabbing_98",
          Ha = "ShellsSlot_shell__active_7e",
          Ga = "ShellsSlot_shell__potential_30",
          $a = "ShellsSlot_label_da",
          Wa = "ShellsSlot_image_3f",
          za = ({
            id: e,
            itemInstalledSetupIdx: t,
            isMountedMoreThanOne: u,
            imageSource: i,
            count: r,
            isSelected: s,
            keyName: o,
            panelType: l,
            intCD: c,
            slotIndex: _,
            grabberId: d,
            isSetupSwitching: m,
            containerRef: E,
            activeDragId: A,
            handleGrabberAction: b,
            forceLeftUpdate: F,
            potentialDropId: D,
            blockOnGrabIds: p,
            shellState: g,
            isDisabled: C,
          }) => {
            const B = !Pt(l),
              S = (0, n.useMemo)(() => ({ backgroundImage: `url(${i})` }), [i]),
              f = d && d === D,
              v = d && d === A,
              w = (0, n.useMemo)(() => {
                const n = { slotType: Ht, slotId: e, fieldType: 1, intCD: c };
                return [
                  n,
                  Object.assign({}, n, {
                    installedSlotId: e,
                    itemInstalledSetupIdx: t,
                    itemInstalledSetupSlotIdx: e,
                    isMountedMoreThanOne: u,
                  }),
                ];
              }, [c, e, t, u]),
              y = w[0],
              x = w[1],
              T = h()(La, !A && B && !C && Ha, v && Pa, !v && f && Ga),
              k = (0, n.useMemo)(
                () => ({
                  id: d,
                  containerRef: E,
                  isEnabled: Boolean(d) && s,
                  isUpdateAvailable: Boolean(A),
                  handleAction: b,
                  forceCenterX: F,
                  blockOnGrabIds: p,
                }),
                [A, p, E, F, d, b, s],
              ),
              I = (0, n.useMemo)(
                () => ({ slotIndex: _, uniqueKey: c, slotType: Ht, imageSource: null }),
                [c, _],
              );
            return a().createElement(
              Rn,
              { isEnabled: B && !m && !C, args: x },
              a().createElement(
                Ve,
                { args: y, isEnabled: !A && Lt(l) },
                a().createElement(
                  "div",
                  { id: `shell-slot-${_}`, className: Na },
                  o &&
                    a().createElement(
                      "div",
                      { className: $a },
                      a().createElement(An, {
                        text: o,
                        show: s || l === Rt.Battle || l === Rt.Respawn,
                        shellState: g,
                        panelType: l,
                      }),
                    ),
                  a().createElement(
                    "div",
                    { className: T },
                    a().createElement(
                      Uu,
                      { when: B, wrapper: cn, withProps: k },
                      a().createElement(
                        Uu,
                        { when: B, wrapper: aa, withProps: I },
                        a().createElement("div", { className: Wa, style: S }),
                        a().createElement(Ma, { count: r }),
                      ),
                    ),
                  ),
                ),
              ),
            );
          },
          Ua = {
            base: "ToggleSlot_base_93",
            slot: "ToggleSlot_slot_cd",
            slot__grabbing: "ToggleSlot_slot__grabbing_df",
            image: "ToggleSlot_image_e0",
            slot__active: "ToggleSlot_slot__active_15",
            glow: "ToggleSlot_glow_48",
            toggle: "ToggleSlot_toggle_73",
          },
          Xa = ({ id: e, isSelected: t, imageSource: u, onSlotSelected: i }) => {
            const r = (0, n.useCallback)(() => {
                !t && i(e);
              }, [e, t, i]),
              s = h()(Ua.slot, !t && Ua.slot__active, Ua.slot__compare),
              o = (0, n.useMemo)(() => ({ backgroundImage: `url(${u})` }), [u]),
              l = (0, n.useMemo)(
                () => ({
                  backgroundImage: `url(R.images.gui.maps.icons.tanksetup.shells.icon_selected_${t ? "on" : "off"})`,
                }),
                [t],
              );
            return a().createElement(
              bn,
              { slotType: Wt, slotId: e },
              a().createElement(
                "div",
                { className: Ua.base },
                a().createElement(
                  "div",
                  { className: s, onClick: r, id: `shell-slot-${e}` },
                  t && a().createElement("div", { className: Ua.glow }),
                  a().createElement("div", { className: Ua.image, style: o }),
                  a().createElement("div", { className: Ua.toggle, style: l }),
                ),
              ),
            );
          },
          ja = "Shells_base_f9",
          Va = "Shells_shell_3f",
          Ka = "Shells_shell__compressed_2e";
        function qa() {
          return (
            (qa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            qa.apply(this, arguments)
          );
        }
        const Ya = ({
            shells: e,
            panelType: t,
            onSelected: u,
            isCompare: i,
            isSelected: r,
            syncInitiator: s,
            blockOnGrabIds: o,
            isDisabled: l,
            isSetupSwitching: c,
            setIsExitBlocked: _,
          }) => {
            const d = F("model.ammunitionPanel", b.None),
              m = d.onSectionSelect,
              E = d.onDragDropSwap,
              A = (0, n.useRef)(!1),
              D = (0, n.useRef)(null),
              p = i ? Wt : Ht,
              g = `${p}-${e.length}shells`,
              C = (0, n.useCallback)(
                (e) => {
                  (m({ selectedSlot: e, selectedSection: p }), _t.playClick());
                },
                [m, p],
              ),
              B = (0, n.useCallback)(() => {
                r || i || l || c || C(0);
              }, [r, i, c, l, C]),
              S = (0, n.useCallback)(
                (e, t) => {
                  E({
                    sectionType: p,
                    dragId: Number(e[e.length - 1]),
                    dropId: Number(t[t.length - 1]),
                  });
                },
                [E, p],
              ),
              f = iu({
                baseId: g,
                slotsLength: e.length,
                handleSwap: S,
                setIsExitBlocked: _,
                syncInitiator: s,
              }),
              v = f.handleGrabberAction,
              y = f.dragState,
              x = f.getForceCenterX;
            return (
              (0, n.useEffect)(
                () =>
                  w(() => {
                    A.current = !0;
                  }),
                [],
              ),
              (0, n.useEffect)(() => {
                if (r && t === Rt.Setup) {
                  if (!A.current)
                    return w(() => {
                      u();
                    });
                  u();
                }
              }, [r, t, u]),
              a().createElement(
                "div",
                {
                  id: g,
                  ref: D,
                  className: ja,
                  onClick: B,
                  onMouseEnter: () => {
                    l || _t.playHighlight();
                  },
                },
                ie(e, (u, n) => {
                  if (Mt(u)) return null;
                  const s = !i && e.length > 1 ? `${g}-${u.id}` : "";
                  return a().createElement(
                    "div",
                    { key: u.id, className: h()(Va, !i && 0 !== n && Ka) },
                    i
                      ? a().createElement(Xa, qa({}, u, { onSlotSelected: C }))
                      : a().createElement(
                          za,
                          qa({}, u, {
                            slotIndex: n,
                            isSetupSwitching: c,
                            isSelected: r,
                            panelType: t,
                            grabberId: s,
                            containerRef: D,
                            forceLeftUpdate: x(s),
                            activeDragId: y.activeDragId,
                            handleGrabberAction: v,
                            potentialDropId: y.potentialDropId,
                            blockOnGrabIds: o,
                            isDisabled: l,
                          }),
                        ),
                  );
                }),
              )
            );
          },
          Za = {
            base: "ShellsSection_base_08",
            base__grabbing: "ShellsSection_base__grabbing_2e",
            base__hangar: "ShellsSection_base__hangar_24",
            base__setup: "ShellsSection_base__setup_c8",
            base__compare: "ShellsSection_base__compare_e3",
            base__selected: "ShellsSection_base__selected_fd",
            base__dragIn: "ShellsSection_base__dragIn_39",
            base__dragInActive: "ShellsSection_base__dragInActive_96",
            base__toggle: "ShellsSection_base__toggle_bd",
            base__disabled: "ShellsSection_base__disabled_7e",
            label: "ShellsSection_label_38",
            attention: "ShellsSection_attention_7e",
            blinking: "ShellsSection_blinking_57",
            attention__once: "ShellsSection_attention__once_a3",
            attention__double: "ShellsSection_attention__double_38",
            border: "ShellsSection_border_0d",
            border__double: "ShellsSection_border__double_a1",
            border__triple: "ShellsSection_border__triple_f2",
            counter: "ShellsSection_counter_74",
            disabled: "ShellsSection_disabled_c2",
          },
          Qa = [Rt.Hangar, Rt.Battle, Rt.Prebattle, Rt.Respawn],
          Ja = ({
            slots: e,
            ammoNotFull: t,
            type: u,
            sectionsIds: i,
            panelType: r,
            onActiveSlotChanged: s,
            isDisabled: o,
            isBorderActive: l,
            selectedSection: c,
            syncInitiator: _,
            classMix: d,
            isSetupSwitching: m,
            setIsExitBlocked: E,
            newItemsCount: A,
          }) => {
            const b = (0, n.useRef)(null),
              F = r === Rt.Compare,
              D = c === u,
              p = (0, n.useCallback)(() => {
                s(b, c, 0);
              }, [s, c]),
              g = au(u, i),
              C = g.selfId,
              B = g.blockOnGrabIds,
              S = ((e) => Qa.includes(e))(r) && !o && t,
              f = (function (e, t) {
                if (Array.isArray(e)) return e.filter(t);
                const u = [];
                for (let a = 0; a < e.length; a++) {
                  var n;
                  const i = null == (n = e[a]) ? void 0 : n.value;
                  t(i, a, e) && u.push(i);
                }
                return u;
              })(e, (e) => Boolean(e) && !Mt(e)).length,
              v = (0, n.useMemo)(() => {
                if (!S) return null;
                const e = h()(
                  Za.border,
                  f === Ot.Two && Za.border__double,
                  f === Ot.Three && Za.border__triple,
                );
                return a().createElement("div", { className: e });
              }, [S, f]),
              w = h()(
                Za.base,
                d,
                Za[`base__${r}`],
                !l && D && Za.base__selected,
                F && Za.base__compare,
                o && Za.base__disabled,
              ),
              y = h()(
                Za.attention,
                f === Ot.One && Za.attention__once,
                f >= Ot.Two && Za.attention__double,
              ),
              x = !F && r !== Rt.Battle && r !== Rt.Respawn;
            return a().createElement(
              "div",
              { id: m ? Cu : C, className: w, ref: b },
              S && a().createElement("div", { className: y }),
              x &&
                a().createElement(
                  "div",
                  { className: Za.label },
                  a().createElement(gu, {
                    text: R.strings.tank_setup.section.shells(),
                    parentRef: b,
                    show: !D,
                    panelType: r,
                  }),
                ),
              v,
              a().createElement(Ya, {
                shells: e,
                panelType: r,
                onSelected: p,
                isSelected: D,
                isCompare: F,
                syncInitiator: _,
                blockOnGrabIds: B,
                isDisabled: o,
                isSetupSwitching: m,
                setIsExitBlocked: E,
              }),
              Boolean(A) &&
                a().createElement(
                  "div",
                  { className: Za.counter },
                  a().createElement(lu, { value: A, size: "small", fadeInAnimation: !0 }),
                ),
              o && a().createElement("div", { className: Za.disabled }),
            );
          },
          ei = {
            base: "Sections_base_13",
            section: "Sections_section_35",
            section__battle: "Sections_section__battle_d3",
            section__small: "Sections_section__small_73",
            section__extraSmall: "Sections_section__extraSmall_5f",
            section__first: "Sections_section__first_e2",
          };
        function ti() {
          return (
            (ti =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            ti.apply(this, arguments)
          );
        }
        const ui = ({
            panelType: e,
            isDisabled: t = !1,
            onActiveSlotChanged: u,
            isBorderActive: n,
            isBootCamp: i = !1,
            sections: r,
            selectedSection: s,
            selectedSlot: o,
            syncInitiator: l,
            ammoNotFull: c,
            onBootcampPanelAppear: _,
            isChangeSetupIndex: d,
            setIsExitBlocked: m,
          }) => {
            const E = J(["section"], ei),
              A = ie(r, (e) => nu(e.type)),
              b = {
                panelType: e,
                isDisabled: t,
                onActiveSlotChanged: u,
                isBorderActive: n,
                selectedSection: s,
                selectedSlot: o,
                syncInitiator: l,
                sectionsIds: A,
                isChangeSetupIndex: d,
                setIsExitBlocked: m,
              };
            return a().createElement(
              "div",
              { className: ei.base },
              ie(r, (t, u) => {
                if (!t.slots || !t.slots.length) return null;
                const n = h()(
                    E.section,
                    0 !== u && Pt(e) && ei.section__battle,
                    0 === u && ei.section__first,
                  ),
                  r = ne(t.slots, (e) => Object.assign({}, e));
                if (t.type === Ht || t.type === Wt) {
                  const e = t;
                  return a().createElement(
                    Ja,
                    ti({}, e, b, {
                      isSetupSwitching: d,
                      slots: r,
                      key: `${t.name}${u}${t.slots.length}`,
                      classMix: n,
                      ammoNotFull: c,
                    }),
                  );
                }
                return a().createElement(
                  Ia,
                  ti({}, t, b, {
                    isSetupSwitching: d,
                    slots: r,
                    key: `${t.name}${u}${t.slots.length}`,
                    classMix: n,
                    isBootCamp: i,
                    onBootcampPanelAppear: _,
                  }),
                );
              }),
            );
          },
          ni = "KeyboardKey_base_57",
          ai = "KeyboardKey_back_43",
          ii = a().memo(({ text: e }) =>
            a().createElement(
              "div",
              { className: ni },
              a().createElement("div", { className: ai }, e),
            ),
          ),
          ri = "SetupSwitchHotkey_base_4c",
          si = "SetupSwitchHotkey_hotKeyWrapper_8d",
          oi = "SetupSwitchHotkey_plusWrapper_f0",
          li = "SetupSwitchHotkey_plus_f0",
          ci = "SetupSwitchHotkey_plus__horizontal_e0",
          _i = "SetupSwitchHotkey_plus__vertical_5b",
          di = a().memo(({ hotKeys: e }) =>
            a().createElement(
              "div",
              { className: ri },
              e.map((e, t) => {
                if (!e) return null;
                const u = e.value;
                return 0 === t
                  ? a().createElement(ii, { key: t, text: u })
                  : a().createElement(
                      "div",
                      { key: t, className: si },
                      a().createElement(
                        "div",
                        { className: oi },
                        a().createElement("div", { className: `${li} ${ci}` }),
                        a().createElement("div", { className: `${li} ${_i}` }),
                      ),
                      a().createElement(ii, { text: u }),
                    );
              }),
            ),
          ),
          mi = {
            base: "Groups_base_de",
            group: "Groups_group_1f",
            groupWrapper: "Groups_groupWrapper_70",
            switch: "Groups_switch_98",
            switch__battle: "Groups_switch__battle_0f",
            switch__small: "Groups_switch__small_45",
            switch__extraSmall: "Groups_switch__extraSmall_b5",
            prebattleSwitchIndicator: "Groups_prebattleSwitchIndicator_da",
            hint: "Groups_hint_49",
            hint__disabled: "Groups_hint__disabled_17",
          };
        function Ei() {
          return (
            (Ei =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Ei.apply(this, arguments)
          );
        }
        const Ai = (e) => e.setupSelector.hotKeys,
          bi = (e) =>
            Object.assign({}, e, {
              slots: ie(e.slots, (e) => {
                if ("specializations" in e) {
                  const t = e;
                  return Object.assign({}, t, {
                    specializations: Object.assign({}, t.specializations, {
                      specializations: ie(t.specializations.specializations, (e) =>
                        Object.assign({}, e),
                      ),
                    }),
                  });
                }
                return Object.assign({}, e);
              }),
            }),
          Fi = (e) =>
            ae(
              e,
              (e) => {
                var t;
                const u = (function (e, t) {
                  if (Array.isArray(e)) return e.every(t);
                  for (let u = 0; u < e.length; u++) if (!t(ue(e, u), u, e)) return !1;
                  return !0;
                })(null != (t = null == e ? void 0 : e.sections) ? t : [], (e) => {
                  var t, u;
                  return 0 === (null != (t = null == (u = e.slots) ? void 0 : u.length) ? t : 0);
                });
                return !(!e || u);
              },
              (e) =>
                Object.assign({}, e, {
                  setupSelector: Object.assign({}, e.setupSelector, {
                    states: ne(e.setupSelector.states, (e) => e),
                  }),
                  sections: ie(e.sections, bi),
                }),
            ),
          Di = ({
            sectionProps: e,
            isSetupSwitching: t,
            isReady: u,
            setSetupSwitching: i,
            children: r,
          }) => {
            const s = J(["switch"], mi),
              o = F("model"),
              l = o.isDisabled,
              c = o.vehicleInfo,
              _ = F("model.ammunitionPanel"),
              d = _.sectionGroups,
              m = _.onChangeSetupIndex,
              E = _.selectedSection,
              A = _.selectedSlot,
              b = _.syncInitiator,
              D = _.ammoNotFull,
              p = null == c ? void 0 : c.vehicleName,
              g = Fi(d);
            ((0, n.useEffect)(() => {
              (e.panelType !== Rt.Hangar && e.panelType !== Rt.Setup) || !u || i(!1);
            }, [u, e.panelType, i]),
              (0, n.useEffect)(() => {
                e.panelType === Rt.Respawn && i(!1);
              }, [p, e.panelType, i]));
            const C = (0, n.useCallback)(
                (t) => {
                  (e.panelType === Rt.Respawn && i(!0), m(t));
                },
                [m, e.panelType, i],
              ),
              B = (e.panelType !== Rt.Respawn && u) || (e.panelType === Rt.Respawn && t);
            return a().createElement(
              "div",
              { className: mi.base },
              ne(g, (u) => {
                const n = R.strings.tank_setup.tooltips.prebattleSwitchIndicator.desc.$dyn(
                  `c_${u.groupId}`,
                );
                return a().createElement(
                  "div",
                  { key: u.groupId, className: mi.group },
                  a().createElement(
                    "div",
                    { className: mi.groupWrapper },
                    a().createElement(
                      It,
                      Ei(
                        { disabled: !B && Boolean(e.isBootCamp) },
                        ((e, t) => ({ index: e.currentIndex, setSetupSwitching: t }))(u, i),
                      ),
                      a().createElement(
                        ui,
                        Ei({}, e, {
                          sections: u.sections,
                          selectedSection: E,
                          selectedSlot: A,
                          syncInitiator: b,
                          ammoNotFull: D,
                          isChangeSetupIndex: t,
                        }),
                      ),
                    ),
                    u.setupSelector.isSwitchEnabled &&
                      a().createElement(
                        "div",
                        { className: h()(s.switch, Nt(e.panelType) && mi.switch__battle) },
                        a().createElement(wt, {
                          states: u.setupSelector.states,
                          onClick: C,
                          totalCount: u.totalCount,
                          currentIndex: u.currentIndex,
                          groupId: u.groupId,
                          isDisabled: e.isDisabled,
                        }),
                        u.setupSelector.isPrebattleSwitchDisabled &&
                          a().createElement(
                            Ze,
                            {
                              header:
                                R.strings.tank_setup.tooltips.prebattleSwitchIndicator.title(),
                              body: "string" == typeof n ? n : void 0,
                            },
                            a().createElement("div", { className: mi.prebattleSwitchIndicator }),
                          ),
                      ),
                  ),
                  ((r = u),
                  ((o = e.panelType) === Rt.Battle || o === Rt.Respawn) &&
                    r.setupSelector.isSwitchEnabled &&
                    Ai(r) &&
                    a().createElement(
                      "div",
                      { className: h()(mi.hint, l && mi.hint__disabled) },
                      a().createElement(di, { hotKeys: Ai(u) }),
                    )),
                );
                var r, o;
              }),
              r,
            );
          },
          pi = {
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
        var gi;
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(gi || (gi = {}));
        const Ci = ["__left", "__right", "__top", "__bottom"],
          Bi =
            ((0, n.forwardRef)(
              (
                { children: e, disableAutoSizeUpdate: t, onOutsideClick: u, customStyles: i = {} },
                r,
              ) => {
                const s = (0, n.useRef)(null),
                  o = (0, n.useRef)(null),
                  l = (0, n.useRef)(null),
                  _ = (0, n.useState)(window.decorator && window.decorator.directionType),
                  d = _[0],
                  m = _[1],
                  E = (0, n.useCallback)(() => {
                    (_t.playClick(), D.O.view.sendEvent.close());
                  }, []),
                  A = (0, n.useCallback)(() => {
                    _t.playHighlight();
                  }, []),
                  b = h()(pi.arrow, pi[`arrow${Ci[d]}`]);
                S(
                  () => (
                    D.O.client.events.mouse.enableOutside(),
                    D.O.client.events.mouse.down(([, e]) => {
                      "outside" === e && (u ? u() : D.O.view.sendEvent.close("popover"));
                    })
                  ),
                );
                const F = (0, n.useCallback)(
                    (e) => {
                      let t = e.target;
                      do {
                        if (t === s.current || t === l.current) return;
                        t = t.parentNode;
                      } while (t);
                      const n = window.decorator;
                      if (void 0 !== window.decorator) {
                        const e = D.O.client.getMouseGlobalPosition(),
                          t = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                          u =
                            e.x < n.boundX ||
                            e.x > n.boundX + n.boundWidth ||
                            e.y > n.boundY + n.boundHeight ||
                            e.y < n.boundY;
                        if (t && !u) return;
                      }
                      u ? u() : D.O.view.sendEvent.close("popover");
                    },
                    [s, l, u],
                  ),
                  p = (0, n.useCallback)(
                    () => (
                      D.O.view.freezeTextureBeforeResize(),
                      w(() => {
                        if (o.current) {
                          const e = o.current.scrollWidth,
                            t = o.current.scrollHeight;
                          (D.O.view.resize(e, t), m(window.decorator.directionType));
                        }
                      })
                    ),
                    [],
                  );
                return (
                  (0, n.useImperativeHandle)(r, () => ({ updateSize: p })),
                  S(() => {
                    D.O.view.setInputPaddingsRem(58);
                  }),
                  (0, n.useEffect)(() => {
                    document.addEventListener("mousedown", F, { capture: !0 });
                    const e = ((e) => {
                      let t = !1;
                      return {
                        promise: new Promise((u, n) => {
                          e.then((e) => !t && u(e)).catch((e) => !t && n(e));
                        }),
                        cancel() {
                          t = !0;
                        },
                      };
                    })((0, c.Eu)());
                    return (
                      !t && e.promise.then(() => p()),
                      () => {
                        (e.cancel(), document.removeEventListener("mousedown", F));
                      }
                    );
                  }, [p, F, t]),
                  a().createElement(
                    "div",
                    { className: pi.base, ref: o },
                    a().createElement(
                      "div",
                      { className: pi.decorator },
                      a().createElement(
                        "div",
                        { className: pi.content, ref: s },
                        e,
                        window.decorator &&
                          window.decorator.isCloseBtnVisible &&
                          a().createElement(
                            Ze,
                            { body: R.strings.dialogs.common.error.cancel() },
                            a().createElement("div", {
                              className: pi.closeBtn,
                              onClick: E,
                              onMouseEnter: A,
                              ref: l,
                            }),
                          ),
                      ),
                      a().createElement("div", { className: b, style: i.arrow }),
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
        function hi() {
          return (
            (hi =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            hi.apply(this, arguments)
          );
        }
        const Si = (e) => {
            let t = e.contentId,
              u = e.decoratorId,
              i = e.direction,
              r = void 0 === i ? gi.Top : i,
              s = e.targetId,
              o = e.args,
              l = e.onClick,
              _ = e.children,
              d = e.isEnabled,
              m = void 0 === d || d,
              E = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  i = Object.keys(e);
                for (n = 0; n < i.length; n++) ((u = i[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Bi);
            const A = (0, n.useRef)(null),
              b = (0, n.useCallback)(() => {
                if ((0, c.wU)()) return (0, c.SW)();
                A.current && (0, c.P3)(t, r, A.current, u, s, o);
              }, [t, r, o, u, s]);
            return a().createElement(
              "div",
              hi(
                {
                  ref: A,
                  onClick:
                    ((F = _.props.onClick),
                    (e) => {
                      m && (b(), l && l(e), F && F(e));
                    }),
                },
                E,
              ),
              _,
            );
            var F;
          },
          fi = "RoleSkillSlot_base_c4",
          vi = "RoleSkillSlot_base__disabled_be",
          wi = "RoleSkillSlot_content_e2",
          yi = "RoleSkillSlot_icon_79",
          xi = "RoleSkillSlot_hover_3c",
          Ti = "RoleSkillSlot_label_9f",
          ki = ({
            roleSkill: e,
            roleName: t,
            intCD: u,
            contentId: i,
            onClick: r,
            isDisabled: s = !1,
            soundHover: o = "highlight",
            soundClick: l = "play",
            className: c,
          }) => {
            const _ = (0, n.useState)(!1),
              d = _[0],
              m = _[1],
              E = (0, n.useMemo)(
                () => ({
                  args: { roleSkill: e, roleName: t, intCD: u, hasHtmlContent: !0 },
                  ignoreShowDelay: !0,
                  contentId: i,
                }),
                [u, e, t, i],
              ),
              A = (0, n.useCallback)(() => {
                (m(!0), s || ct(o));
              }, [s, o]),
              b = () => m(!1),
              F = (0, n.useCallback)(() => {
                s || (null == r || r(), ct(l));
              }, [s, r, l]),
              D = (0, n.useMemo)(
                () =>
                  a().createElement(
                    Je,
                    { tooltipArgs: E, className: h()(fi, { [vi]: s }, c) },
                    a().createElement(
                      "div",
                      { className: wi, onMouseEnter: A, onMouseLeave: b, onClick: F },
                      a().createElement("div", { className: h()({ [xi]: d && !s }) }),
                      a().createElement(
                        "div",
                        { className: Ti },
                        a().createElement(gu, {
                          text: R.strings.artefacts.comp7_roleSkillSlot.title(),
                          show: d,
                          panelType: Rt.Hangar,
                        }),
                      ),
                      a().createElement("div", {
                        id: "panel-comp7Skill-section",
                        className: yi,
                        style: {
                          backgroundImage: `url(${R.images.gui.maps.icons.roleSkills.c_48x48.$dyn(e)})`,
                        },
                      }),
                    ),
                  ),
                [c, s, d, F, A, e, E],
              );
            return s
              ? D
              : a().createElement(
                  Si,
                  {
                    contentId: R.views.battle.battle_page.SkillSelectPopover("resId"),
                    direction: gi.Top,
                  },
                  D,
                );
          },
          Ii = "SlotGlow_base_40",
          Ri = "SlotGlow_glow_a9",
          Oi = "SlotGlow_glow__shown_f2",
          Mi = "SlotGlow_glow__hidden_94",
          Ni = (0, n.memo)(({ slotOffset: e, slotWidth: t, isAnimationRunning: u }) => {
            const i = (0, n.useState)({ offset: e, slotWidth: t }),
              r = i[0],
              s = i[1],
              o = (0, n.useRef)({ initialized: !1, offset: e, slotWidth: t });
            ((0, n.useEffect)(() => {
              let u = o.current.initialized;
              (!u && e && ((u = !0), s({ offset: e, slotWidth: t })),
                (o.current = { initialized: u, offset: e, slotWidth: t }));
            }, [e, t]),
              (0, n.useEffect)(() => {
                u || s(o.current);
              }, [u]));
            const l = (0, n.useMemo)(() => {
                const e = r.slotWidth + 25;
                return {
                  left: r.offset,
                  width: e,
                  backgroundSize: `${D.O.view.pxToRem(e)}rem 100%`,
                };
              }, [r.offset, r.slotWidth]),
              c = !u && r.offset === o.current.offset,
              _ = h()(Ri, c ? Oi : Mi);
            return a().createElement(
              "div",
              { className: Ii },
              o.current.initialized && a().createElement("div", { className: _, style: l }),
            );
          }),
          Li = R.views.lobby.comp7.tooltips.Comp7SkillTooltip("resId"),
          Pi =
            R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent("resId"),
          Hi = { exitActive: at.skillSelectAnimation__exitActive },
          Gi = ({
            show: e = !0,
            isReady: t = !0,
            panelType: u,
            isBootCamp: i = !1,
            isDisabled: r = !1,
            onBootcampPanelAppear: s,
            onResize: o,
            setIsExitBlocked: l,
          }) => {
            const c = F("model.ammunitionPanel"),
              _ = c.isSetupSwitchInProgress,
              d = c.syncInitiator,
              m = c.sectionGroups,
              E = c.onSectionResized,
              A = (function (e, t, u) {
                if (Array.isArray(e)) return e.reduce(t, u);
                let n = u;
                for (let u = 0; u < e.length; u++) n = t(n, ue(e, u), u, e);
                return n;
              })(m, (e, t) => e + t.sections.length, 0),
              b = F("model.roleSkillSlot"),
              D = F("model.roleSkillSlot"),
              p = D.onClick,
              g = D.isPopoverOpen,
              C = F("model.abilitySlot"),
              B = (0, n.useCallback)(() => p(), [p]),
              S = (0, n.useState)(!1),
              f = S[0],
              y = S[1],
              x = $(b.roleSkill),
              T = u === Rt.Hangar ? Li : Pi,
              k = !b.canSwitch || (r && u !== Rt.Prebattle),
              I = (null == b ? void 0 : b.roleSkill) && u === Rt.Prebattle,
              R = Boolean(x) && b.roleSkill !== x && u === Rt.Prebattle,
              O = (0, n.useRef)(!1),
              M = (0, n.useState)({ slotWidth: 0, slotOffset: 0 }),
              N = M[0],
              L = M[1],
              P = (0, n.useState)(!1),
              H = P[0],
              G = P[1],
              W = (0, n.useState)(!1),
              z = W[0],
              U = W[1],
              X = (0, n.useRef)(null),
              j = v(),
              V = (0, n.useRef)({
                element: null,
                generation: 0,
                slotIndex: null,
                sectionIndex: null,
              }),
              K = (0, n.useCallback)(
                (e, t) => {
                  if (f || _ || i || u !== Rt.Hangar) return;
                  const n = t || { width: 0, height: 0, offsetX: 0, offsetY: 0 };
                  (E(Object.assign({ sectionType: e }, n)), j && (j.freeze(), j.resize()));
                },
                [f, _, i, u, E, j],
              ),
              q = (0, n.useCallback)(
                (e) => {
                  K("main", e);
                },
                [K],
              );
            (se(X, q, !0, [d]), (0, n.useEffect)(() => () => q(), [q]));
            const Y = (0, n.useCallback)(() => {
                G(!1);
              }, []),
              Z = (0, n.useCallback)(() => {
                if (V.current.element && X.current) {
                  const e = V.current.element.getBoundingClientRect(),
                    t = X.current.getBoundingClientRect();
                  L({ slotWidth: e.width, slotOffset: e.left - t.left + 0.5 * e.width });
                }
              }, []),
              Q = (0, n.useCallback)(
                (e, t, u) => {
                  if (e.current && X.current) {
                    const n = ((e, t, u) =>
                      e !== u.current.slotIndex || t !== u.current.sectionIndex)(u, t, V);
                    ((V.current.element = e.current),
                      (V.current.slotIndex = u),
                      (V.current.sectionIndex = t),
                      O.current && n ? G(!0) : (O.current = !0),
                      V.current.generation && Z());
                  }
                },
                [Z],
              ),
              ee = (0, n.useCallback)(
                () =>
                  w(() => {
                    ((V.current.generation += 1), Z());
                  }),
                [V, Z],
              );
            ((0, n.useEffect)(() => w(ee), [ee]),
              (0, n.useEffect)(
                () => (
                  engine.on("clientResized", ee),
                  () => {
                    engine.off("clientResized", ee);
                  }
                ),
                [ee],
              ));
            const te = (0, n.useCallback)(() => {
                ((V.current.generation += 1),
                  A >= V.current.generation && (null == s || s(), null == o || o()),
                  Z());
              }, [s, o, A, Z]),
              ne = N.slotWidth,
              ae = N.slotOffset,
              ie = h()(
                at.base,
                !t && at.base__locked,
                !e && at.base__hidden,
                r && at.base__disabled,
                I && at.base__comp7Prebattle,
              ),
              oe = h()(at.border, !H && at.border__hidden),
              le = h()(at.roleSkillSelectBorder, (g || z) && at.roleSkillSelectBorder__visible),
              ce = h()(at.roleSkillSelectBorder, z && at.roleSkillSelectBorder__visible),
              _e = u === Rt.Setup || u === Rt.Compare,
              de = {
                panelType: u,
                isDisabled: r,
                onActiveSlotChanged: Q,
                isBorderActive: H,
                isBootCamp: i,
                onBootcampPanelAppear: te,
                setIsExitBlocked: l,
              };
            (0, n.useEffect)(() => {
              !1 === i && (null == o || o());
            }, [o, b.roleSkill, C.ability, i]);
            const me = J(["roleSkillSlot", "abilitySkillSlot"], at),
              Ee = (0, n.useCallback)(() => {
                U(!0);
              }, []),
              Ae = (0, n.useCallback)(() => {
                U(!1);
              }, []);
            return a().createElement(
              "div",
              { ref: X, className: ie },
              _e &&
                a().createElement(Ni, {
                  key: V.current.generation,
                  slotOffset: ae,
                  slotWidth: ne,
                  isAnimationRunning: H,
                }),
              a().createElement(
                Di,
                { isSetupSwitching: _ || f, sectionProps: de, isReady: t, setSetupSwitching: y },
                b.roleSkill &&
                  a().createElement(
                    re.Z,
                    {
                      in: R,
                      timeout: 400,
                      className: at.skillSelectAnimation,
                      classNames: Hi,
                      onEnter: Ee,
                      onExited: Ae,
                    },
                    a().createElement(
                      "div",
                      {
                        className: h()(
                          at.roleSkillSlot,
                          at[`roleSkillSlot__${u}`],
                          me.roleSkillSlot,
                        ),
                      },
                      a().createElement(ki, {
                        roleSkill: b.roleSkill,
                        roleName: b.roleName,
                        intCD: b.intCD,
                        isDisabled: k,
                        contentId: T,
                        onClick: B,
                        className: at.roleSkillButton,
                      }),
                      a().createElement("div", { className: le }),
                      a().createElement("div", { className: ce }),
                    ),
                  ),
                C.ability &&
                  a().createElement(nt, {
                    skillName: C.ability,
                    tooltipId: C.tooltipId,
                    tooltipHeader: C.tooltipHeader,
                    tooltipBody: C.tooltipBody,
                    className: h()(
                      at.abilitySkillSlot,
                      at[`abilitySkillSlot__${u}`],
                      me.abilitySkillSlot,
                    ),
                  }),
              ),
              _e &&
                a().createElement(
                  "div",
                  { className: oe },
                  a().createElement(lt, { slotWidth: ne, slotOffset: ae, onAnimationEnd: Y }),
                ),
            );
          },
          $i = "Content_base_1a",
          Wi = () => {
            const e = F("model"),
              t = e.isDisabled,
              u = e.isReady,
              i = e.isBootcamp,
              r = e.onEscKeyDown,
              s = (0, n.useCallback)(() => r(), [r]);
            return (
              C(p.n.ESCAPE, s),
              a().createElement(
                "div",
                { className: $i },
                a().createElement(Gi, {
                  panelType: Rt.Respawn,
                  isDisabled: t,
                  isReady: u,
                  isBootCamp: i,
                }),
              )
            );
          },
          zi = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          Ui = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const Xi = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          ji = (e) =>
            Xi
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let u = Ui.length - 1; u >= 0; u--)
                    for (; e >= Ui[u];) ((t += zi[u]), (e -= Ui[u]));
                  return t;
                })(e),
          Vi = {
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
        let Ki, qi;
        (!(function (e) {
          ((e.extraSmall = "extraSmall"), (e.medium = "medium"), (e.big = "big"));
        })(Ki || (Ki = {})),
          (function (e) {
            ((e.colored = "colored"), (e.white = "white"), (e.whiteSpanish = "whiteSpanish"));
          })(qi || (qi = {})));
        const Yi = ({
            isElite: e,
            vehicleName: t,
            vehicleShortName: u,
            vehicleType: n,
            vehicleLvl: i,
            tags: r,
            isPremiumIGR: s,
            size: o = Ki.extraSmall,
            type: l = qi.colored,
            className: c,
            classNames: _,
            isShortName: d = !1,
          }) => {
            const m = `${((E = n), E.replace(/-/g, "_"))}${e ? "_elite" : ""}`;
            var E;
            const A = R.images.gui.maps.icons.vehicleTypes.big.$dyn(m);
            return a().createElement(
              "div",
              {
                className: h()(
                  Vi.base,
                  Vi[`base__size${T(o)}`],
                  Vi[`base__type${T(l)}`],
                  r && ne(r, (e) => Vi[`base__tag${T(e)}`]),
                  c,
                ),
              },
              a().createElement(
                "div",
                { className: h()(Vi.level, null == _ ? void 0 : _.level) },
                ji(i),
              ),
              a().createElement("div", {
                className: h()(Vi.type, e && Vi.type__elite, null == _ ? void 0 : _.typeIcon),
                style: { backgroundImage: `url(${A})` },
              }),
              s && a().createElement("div", { className: Vi.premiumIGR }),
              a().createElement(
                "div",
                { className: h()(Vi.name, null == _ ? void 0 : _.name) },
                d ? u : t,
              ),
            );
          },
          Zi = "Header_base_bc";
        function Qi() {
          return (
            (Qi =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Qi.apply(this, arguments)
          );
        }
        const Ji = () => {
            const e = F("model.vehicleInfo");
            return a().createElement(
              "div",
              { className: Zi },
              a().createElement(Yi, Qi({}, e, { size: Ki.medium, type: qi.white })),
            );
          },
          er = "App_base_55",
          tr = () =>
            a().createElement(
              "div",
              { className: er },
              a().createElement(Ji, null),
              a().createElement(Wi, null),
            );
        engine.whenReady.then(() => {
          r().render(a().createElement(tr, null), document.getElementById("root"));
        });
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(e) {
    var t = __webpack_module_cache__[e];
    if (void 0 !== t) return t.exports;
    var u = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](u, u.exports, __webpack_require__), u.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, u, n) => {
      if (!t) {
        var a = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [t, u, n] = deferred[o], i = !0, r = 0; r < t.length; r++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[r]))
              ? t.splice(r--, 1)
              : ((i = !1), n < a && (a = n));
          if (i) {
            deferred.splice(o--, 1);
            var s = u();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      n = n || 0;
      for (var o = deferred.length; o > 0 && deferred[o - 1][2] > n; o--)
        deferred[o] = deferred[o - 1];
      deferred[o] = [t, u, n];
    }),
    (__webpack_require__.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(t, { a: t }), t);
    }),
    (__webpack_require__.d = (e, t) => {
      for (var u in t)
        __webpack_require__.o(t, u) &&
          !__webpack_require__.o(e, u) &&
          Object.defineProperty(e, u, { enumerable: !0, get: t[u] });
    }),
    (__webpack_require__.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (e) {
        if ("object" == typeof window) return window;
      }
    })()),
    (__webpack_require__.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t)),
    (__webpack_require__.r = (e) => {
      ("undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 }));
    }),
    (__webpack_require__.j = 876),
    (() => {
      var e = { 876: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var n,
            a,
            [i, r, s] = u,
            o = 0;
          if (i.some((t) => 0 !== e[t])) {
            for (n in r) __webpack_require__.o(r, n) && (__webpack_require__.m[n] = r[n]);
            if (s) var l = s(__webpack_require__);
          }
          for (t && t(u); o < i.length; o++)
            ((a = i[o]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(l);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [532], () => __webpack_require__(9376));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
