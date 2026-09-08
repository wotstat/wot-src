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
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => i, onResize: () => r }));
        var a = t(472),
          s = t(176);
        const r = (0, a.E)("clientResized"),
          n = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, s.R)(!1);
          }
          function t() {
            e.enabled && (0, s.R)(!0);
          }
          function a() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", u),
                  document.body.removeEventListener("mouseleave", t))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", u),
                  document.body.addEventListener("mouseleave", t))
              : (0, s.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let s = !0;
                  const r = `mouse${u}`,
                    i = n[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, o),
                    a(),
                    () => {
                      s &&
                        (i(), window.removeEventListener(r, o), (e.listeners -= 1), a(), (s = !1));
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
              ((e.enabled = !1), a());
            },
            enable() {
              ((e.enabled = !0), a());
            },
            enableOutside() {
              e.enabled && (0, s.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, s.R)(!1);
            },
          });
        })();
      },
      959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => a,
            getMouseGlobalPosition: () => r,
            getSize: () => s,
            graphicsQuality: () => n,
          }));
        var a = t(527);
        function s(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const n = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      176: (e, u, t) => {
        "use strict";
        function a(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => a });
      },
      472: (e, u, t) => {
        "use strict";
        function a(e) {
          return (u) => (
            engine.on(e, u),
            () => {
              engine.off(e, u);
            }
          );
        }
        t.d(u, { E: () => a });
      },
      138: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => s });
        var a = t(959);
        const s = { view: t(641), client: a };
      },
      722: (e, u, t) => {
        "use strict";
        function a(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function s(e, u, t) {
          return `url(${a(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => s, getTextureUrl: () => a }));
      },
      112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => s });
        var a = t(472);
        const s = {
          onTextureFrozen: (0, a.E)("self.onTextureFrozen"),
          onTextureReady: (0, a.E)("self.onTextureReady"),
          onDomBuilt: (0, a.E)("self.onDomBuilt"),
          onLoaded: (0, a.E)("self.onLoaded"),
          onDisplayChanged: (0, a.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, a.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, a.E)("children.onAdded"),
            onLoaded: (0, a.E)("children.onLoaded"),
            onRemoved: (0, a.E)("children.onRemoved"),
            onAttached: (0, a.E)("children.onAttached"),
            onTextureReady: (0, a.E)("children.onTextureReady"),
            onRequestPosition: (0, a.E)("children.requestPosition"),
          },
        };
      },
      641: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            addModelObserver: () => _,
            addPreloadTexture: () => i,
            children: () => a,
            displayStatus: () => s.W,
            displayStatusIs: () => f,
            events: () => r.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => w,
            getScale: () => F,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => C,
            isEventHandled: () => h,
            isFocused: () => B,
            pxToRem: () => p,
            remToPx: () => D,
            resize: () => m,
            sendEvent: () => n.qP,
            setAnimateWindow: () => g,
            setEventHandled: () => b,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => c,
            whenTutorialReady: () => x,
          }));
        var a = t(722),
          s = t(112),
          r = t(538),
          n = t(566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, u, t, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, a);
        }
        function _(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function c(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function E(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: D(u.x), y: D(u.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
          return viewEnv.getScale();
        }
        function p(e) {
          return viewEnv.pxToRem(e);
        }
        function D(e) {
          return viewEnv.remToPx(e);
        }
        function g(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function B() {
          return viewEnv.isFocused();
        }
        function C() {
          return viewEnv.isClientAccessible();
        }
        function b() {
          return viewEnv.setEventHandled();
        }
        function h() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function w() {
          return viewEnv.getShowingStatus();
        }
        const f = Object.keys(s.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === s.W[u]), e),
            {},
          ),
          S = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          x = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => l });
        const a = ["args"];
        const s = 2,
          r = 16,
          n = 32,
          i = 64,
          o = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                n = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    s = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                  return s;
                })(u, a);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, n, {
                      arguments:
                        ((s = r),
                        Object.entries(s).map(([e, u]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, n));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var s;
          },
          l = {
            close(e) {
              o("popover" === e ? s : n);
            },
            minimize() {
              o(i);
            },
            move(e) {
              o(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      521: (e, u, t) => {
        "use strict";
        let a, s;
        (t.d(u, { n: () => a }),
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
          })(a || (a = {})),
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
          })(s || (s = {})));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var a = t(138);
        class s {
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
            return (window.__dataTracker || (window.__dataTracker = new s()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(e, u, t = 0, s = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = a.O.view.addModelObserver(e, t, s);
            return (
              r > 0
                ? ((this._callbacks[r] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(r) : (this._views[t] = [r])))
                : console.error("Can't add callback for model:", e),
              r
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
              const a = this._callbacks[t];
              void 0 !== a && a(e, u);
            });
          }
        }
        s.__instance = void 0;
        const r = s;
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
        t.d(u, { B3: () => l, Gr: () => _, Z5: () => n, B0: () => o, ry: () => D });
        class a {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: u, callback: t }) => {
                  let a = e.target;
                  do {
                    if (a === u) return;
                    a = a.parentNode;
                  } while (a);
                  t();
                });
              }));
          }
          static get instance() {
            return (a.__instance || (a.__instance = new a()), a.__instance);
          }
          register(e, u) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: u }));
          }
          unregister(e, u) {
            const t = e,
              a = u;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: u }) => e !== t || u !== a,
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
        a.__instance = void 0;
        const s = a;
        var r = t(358);
        const n = {
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
          _ = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          c = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = t(521),
          E = t(138);
        const A = ["args"];
        function F(e, u, t, a, s, r, n) {
          try {
            var i = e[r](n),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(a, s);
        }
        const p = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          D = (function () {
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
                  return new Promise(function (a, s) {
                    var r = e.apply(u, t);
                    function n(e) {
                      F(r, a, s, n, i, "next", e);
                    }
                    function i(e) {
                      F(r, a, s, n, i, "throw", e);
                    }
                    n(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          g = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const s = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    s = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                  return s;
                })(u, A);
              void 0 !== s
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
                      arguments:
                        ((a = s),
                        Object.entries(a).map(([e, u]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var a;
          },
          B = () => g(o.CLOSE),
          C = (e, u) => {
            e.keyCode === m.n.ESCAPE && u();
          };
        var b = t(572);
        const h = s.instance,
          v = {
            DataTracker: r.Z,
            ViewModel: b.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: _,
            TimeFormatType: c,
            DateFormatType: d,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => g(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: B,
            sendClosePopOverEvent: () => g(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              g(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, a, s = R.invalid("resId"), r) => {
              const n = E.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                _ = i.y,
                c = i.width,
                d = i.height,
                m = {
                  x: E.O.view.pxToRem(l) + n.x,
                  y: E.O.view.pxToRem(_) + n.y,
                  width: E.O.view.pxToRem(c),
                  height: E.O.view.pxToRem(d),
                };
              g(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: a || R.invalid("resId"),
                targetID: s,
                direction: u,
                bbox: p(m),
                on: !0,
                args: r,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => C(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              C(e, B);
            },
            handleViewEvent: g,
            onBindingsReady: D,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(o.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(o.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(o.POP_OVER),
            dumpViewModel: function e(u) {
              const t = {};
              if ("object" != typeof u) return u;
              for (const a in u)
                if (Object.prototype.hasOwnProperty.call(u, a)) {
                  const s = Object.prototype.toString.call(u[a]);
                  if (s.startsWith("[object CoherentArrayProxy]")) {
                    const s = u[a];
                    t[a] = [];
                    for (let u = 0; u < s.length; u++) t[a].push({ value: e(s[u].value) });
                  } else
                    s.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[a] = e(u[a]))
                      : (t[a] = u[a]);
                }
              return t;
            },
            ClickOutsideManager: h,
            SystemLocale: n,
            UserLocale: i,
          };
        window.ViewEnvHelper = v;
      },
      877: (e, u, t) => {
        "use strict";
        var a = t(179),
          s = t.n(a);
        const r = (e, u, t) =>
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
        var n = t(138);
        const i = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var o;
        function l(e, u, t) {
          const a = (function (e, u) {
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
            s = (function (e, u) {
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
            r = Math.min(a, s);
          return {
            extraLarge: r === t.extraLarge.weight,
            large: r === t.large.weight,
            medium: r === t.medium.weight,
            small: r === t.small.weight,
            extraSmall: r === t.extraSmall.weight,
            extraLargeWidth: a === t.extraLarge.weight,
            largeWidth: a === t.large.weight,
            mediumWidth: a === t.medium.weight,
            smallWidth: a === t.small.weight,
            extraSmallWidth: a === t.extraSmall.weight,
            extraLargeHeight: s === t.extraLarge.weight,
            largeHeight: s === t.large.weight,
            mediumHeight: s === t.medium.weight,
            smallHeight: s === t.small.weight,
            extraSmallHeight: s === t.extraSmall.weight,
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
        })(o || (o = {}));
        const _ = n.O.client.getSize("rem"),
          c = _.width,
          d = _.height,
          m = Object.assign({ width: c, height: d }, l(c, d, i)),
          E = (0, a.createContext)(m),
          A = ["children"];
        const F = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                s = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
              return s;
            })(e, A);
          const s = (0, a.useContext)(E),
            n = s.extraLarge,
            i = s.large,
            o = s.medium,
            l = s.small,
            _ = s.extraSmall,
            c = s.extraLargeWidth,
            d = s.largeWidth,
            m = s.mediumWidth,
            F = s.smallWidth,
            p = s.extraSmallWidth,
            D = s.extraLargeHeight,
            g = s.largeHeight,
            B = s.mediumHeight,
            C = s.smallHeight,
            b = s.extraSmallHeight,
            h = { extraLarge: D, large: g, medium: B, small: C, extraSmall: b };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && n) return u;
            if (t.large && i) return u;
            if (t.medium && o) return u;
            if (t.small && l) return u;
            if (t.extraSmall && _) return u;
          } else {
            if (t.extraLargeWidth && c) return r(u, t, h);
            if (t.largeWidth && d) return r(u, t, h);
            if (t.mediumWidth && m) return r(u, t, h);
            if (t.smallWidth && F) return r(u, t, h);
            if (t.extraSmallWidth && p) return r(u, t, h);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && D) return u;
              if (t.largeHeight && g) return u;
              if (t.mediumHeight && B) return u;
              if (t.smallHeight && C) return u;
              if (t.extraSmallHeight && b) return u;
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
        (0, a.memo)(F);
        const p = (e) => {
            const u = (0, a.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          D = (0, a.memo)(({ children: e }) => {
            const u = (0, a.useContext)(E),
              t = (0, a.useState)(u),
              r = t[0],
              o = t[1],
              _ = (0, a.useCallback)((e, u) => {
                const t = n.O.view.pxToRem(e),
                  a = n.O.view.pxToRem(u);
                o(Object.assign({ width: t, height: a }, l(t, a, i)));
              }, []);
            (p(() => {
              engine.on("clientResized", _);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", _), [_]));
            const c = (0, a.useMemo)(() => Object.assign({}, r), [r]);
            return s().createElement(E.Provider, { value: c }, e);
          });
        var g = t(483),
          B = t.n(g),
          C = t(926),
          b = t.n(C);
        let h, v, w;
        (!(function (e) {
          ((e[(e.ExtraSmall = i.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = i.small.width)] = "Small"),
            (e[(e.Medium = i.medium.width)] = "Medium"),
            (e[(e.Large = i.large.width)] = "Large"),
            (e[(e.ExtraLarge = i.extraLarge.width)] = "ExtraLarge"));
        })(h || (h = {})),
          (function (e) {
            ((e[(e.ExtraSmall = i.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = i.small.width)] = "Small"),
              (e[(e.Medium = i.medium.width)] = "Medium"),
              (e[(e.Large = i.large.width)] = "Large"),
              (e[(e.ExtraLarge = i.extraLarge.width)] = "ExtraLarge"));
          })(v || (v = {})),
          (function (e) {
            ((e[(e.ExtraSmall = i.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = i.small.height)] = "Small"),
              (e[(e.Medium = i.medium.height)] = "Medium"),
              (e[(e.Large = i.large.height)] = "Large"),
              (e[(e.ExtraLarge = i.extraLarge.height)] = "ExtraLarge"));
          })(w || (w = {})));
        const f = () => {
            const e = (0, a.useContext)(E),
              u = e.width,
              t = e.height,
              s = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return h.ExtraLarge;
                  case e.large:
                    return h.Large;
                  case e.medium:
                    return h.Medium;
                  case e.small:
                    return h.Small;
                  case e.extraSmall:
                    return h.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), h.ExtraSmall);
                }
              })(e),
              r = ((e) => {
                switch (!0) {
                  case e.extraLargeWidth:
                    return v.ExtraLarge;
                  case e.largeWidth:
                    return v.Large;
                  case e.mediumWidth:
                    return v.Medium;
                  case e.smallWidth:
                    return v.Small;
                  case e.extraSmallWidth:
                    return v.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), v.ExtraSmall);
                }
              })(e),
              n = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return w.ExtraLarge;
                  case e.largeHeight:
                    return w.Large;
                  case e.mediumHeight:
                    return w.Medium;
                  case e.smallHeight:
                    return w.Small;
                  case e.extraSmallHeight:
                    return w.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), w.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: s,
              mediaWidth: r,
              mediaHeight: n,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          S = ["children", "className"];
        function x() {
          return (
            (x =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            x.apply(this, arguments)
          );
        }
        const T = {
            [v.ExtraSmall]: "",
            [v.Small]: b().SMALL_WIDTH,
            [v.Medium]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH}`,
            [v.Large]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH}`,
            [v.ExtraLarge]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH} ${b().EXTRA_LARGE_WIDTH}`,
          },
          L = {
            [w.ExtraSmall]: "",
            [w.Small]: b().SMALL_HEIGHT,
            [w.Medium]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT}`,
            [w.Large]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT}`,
            [w.ExtraLarge]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT} ${b().EXTRA_LARGE_HEIGHT}`,
          },
          P = {
            [h.ExtraSmall]: "",
            [h.Small]: b().SMALL,
            [h.Medium]: `${b().SMALL} ${b().MEDIUM}`,
            [h.Large]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE}`,
            [h.ExtraLarge]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE} ${b().EXTRA_LARGE}`,
          },
          N = (e) => {
            let u = e.children,
              t = e.className,
              a = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  s = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                return s;
              })(e, S);
            const r = f(),
              n = r.mediaWidth,
              i = r.mediaHeight,
              o = r.mediaSize;
            return s().createElement("div", x({ className: B()(t, T[n], L[i], P[o]) }, a), u);
          },
          y = ["children"];
        const I = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                s = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
              return s;
            })(e, y);
          return s().createElement(D, null, s().createElement(N, t, u));
        };
        var O = t(493),
          k = t.n(O);
        function M(e) {
          engine.call("PlaySound", e);
        }
        const H = {
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
          Q = [
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
        function W() {
          return (
            (W =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            W.apply(this, arguments)
          );
        }
        class V extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && M(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && M(this.props.soundClick));
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
              a = e.goto,
              r = e.side,
              n = e.type,
              i = e.classNames,
              o = e.onMouseEnter,
              l = e.onMouseLeave,
              _ = e.onMouseDown,
              c = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    s = {},
                    r = Object.keys(e);
                  for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                  return s;
                })(e, Q)),
              m = B()(H.base, H[`base__${n}`], H[`base__${r}`], null == i ? void 0 : i.base),
              E = B()(H.icon, H[`icon__${n}`], H[`icon__${r}`], null == i ? void 0 : i.icon),
              A = B()(H.glow, null == i ? void 0 : i.glow),
              F = B()(H.caption, H[`caption__${n}`], null == i ? void 0 : i.caption),
              p = B()(H.goto, null == i ? void 0 : i.goto);
            return s().createElement(
              "div",
              W(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(_),
                  onMouseUp: this._onMouseUp(c),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                d,
              ),
              "info" !== n && s().createElement("div", { className: H.shine }),
              s().createElement(
                "div",
                { className: E },
                s().createElement("div", { className: A }),
              ),
              s().createElement("div", { className: F }, u),
              a && s().createElement("div", { className: p }, a),
            );
          }
        }
        let U;
        ((V.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        }),
          (function (e) {
            ((e[(e.Quests = 0)] = "Quests"), (e[(e.Quest = 1)] = "Quest"));
          })(U || (U = {})));
        const G = (e, u) => {
          let t;
          const a = setTimeout(() => {
            t = e();
          }, u);
          return () => {
            ("function" == typeof t && t(), clearTimeout(a));
          };
        };
        var q = t(515);
        let $, j;
        (!(function (e) {
          ((e[(e.W_1024 = 1024)] = "W_1024"),
            (e[(e.W_1280 = 1280)] = "W_1280"),
            (e[(e.W_2000 = 2e3)] = "W_2000"),
            (e[(e.W_2200 = 2200)] = "W_2200"),
            (e[(e.W_2560 = 2560)] = "W_2560"));
        })($ || ($ = {})),
          (function (e) {
            e[(e.H_1200 = 1200)] = "H_1200";
          })(j || (j = {})));
        const z = () => {
          const e = f(),
            u = e.remScreenWidth,
            t = e.remScreenHeight;
          return {
            isCustomSmall: u > $.W_1024 && u <= $.W_1280,
            isCustomLarge: u > $.W_2000 && u <= $.W_2560 && t > j.H_1200,
          };
        };
        function X(e) {
          return e;
        }
        function Y() {
          return !1;
        }
        console.log;
        var K = t(174);
        function Z(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return J(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return J(e, u);
            })(e)) ||
            (u && e && "number" == typeof e.length)
          ) {
            t && (e = t);
            var a = 0;
            return function () {
              return a >= e.length ? { done: !0 } : { done: !1, value: e[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function J(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, a = new Array(u); t < u; t++) a[t] = e[t];
          return a;
        }
        const ee = (e) => (0 === e ? window : window.subViews.get(e));
        function ue(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, a) => u(null == e ? void 0 : e.value, t, a));
        }
        var te = t(946);
        const ae = ((e, u) => {
            const t = (0, a.createContext)({});
            return [
              function ({ mode: r = "real", options: i, children: o, mocks: l }) {
                const _ = (0, a.useRef)([]),
                  c = (t, a, s) => {
                    var r;
                    const i = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = ee,
                        context: a = "model",
                      } = {}) {
                        const s = new Map();
                        function r(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? s.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = s.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const i = (e) => {
                          const s = t(u),
                            r = a.split(".").reduce((e, u) => e[u], s);
                          return "string" != typeof e || 0 === e.length
                            ? r
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, r);
                        };
                        return {
                          subscribe: (t, r) => {
                            const o = "string" == typeof r ? `${a}.${r}` : a,
                              l = n.O.view.addModelObserver(o, u, !0);
                            return (s.set(l, t), e && t(i(r)), l);
                          },
                          readByPath: i,
                          createCallback: (e, u) => {
                            const t = i(u);
                            return (...u) => {
                              t(e(...u));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const u = i(e);
                            return () => {
                              u();
                            };
                          },
                          dispose: function () {
                            for (var e, t = Z(s.keys()); !(e = t()).done;) r(e.value, u);
                          },
                          unsubscribe: r,
                        };
                      })(a),
                      o =
                        "real" === t
                          ? i
                          : Object.assign({}, i, {
                              readByPath:
                                null != (r = null == s ? void 0 : s.getter) ? r : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == s ? void 0 : s.getter(e)) : o.readByPath(e),
                      c = (e) => _.current.push(e),
                      d = e({
                        mode: t,
                        readByPath: l,
                        externalModel: o,
                        observableModel: {
                          array: (e, u) => {
                            const a = null != u ? u : l(e),
                              s = K.LO.box(a, { equals: Y });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, K.aD)((e) => s.set(e)),
                                  e,
                                ),
                              s
                            );
                          },
                          object: (e, u) => {
                            const a = null != u ? u : l(e),
                              s = K.LO.box(a, { equals: Y });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, K.aD)((e) => s.set(e)),
                                  e,
                                ),
                              s
                            );
                          },
                          primitives: (e, u) => {
                            const a = l(u);
                            if (Array.isArray(e)) {
                              const s = e.reduce((e, u) => ((e[u] = K.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, K.aD)((u) => {
                                      e.forEach((e) => {
                                        s[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                s
                              );
                            }
                            {
                              const s = e,
                                r = Object.entries(s),
                                n = r.reduce((e, [u, t]) => ((e[t] = K.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, K.aD)((e) => {
                                      r.forEach(([u, t]) => {
                                        n[t].set(e[u]);
                                      });
                                    }),
                                    u,
                                  ),
                                n
                              );
                            }
                          },
                        },
                        cleanup: c,
                      }),
                      m = { mode: t, model: d, externalModel: o, cleanup: c };
                    return {
                      model: d,
                      controls: "mocks" === t && s ? s.controls(m) : u(m),
                      externalModel: o,
                      mode: t,
                    };
                  },
                  d = (0, a.useRef)(!1),
                  m = (0, a.useState)(r),
                  E = m[0],
                  A = m[1],
                  F = (0, a.useState)(() => c(r, i, l)),
                  p = F[0],
                  D = F[1];
                return (
                  (0, a.useEffect)(() => {
                    d.current ? D(c(E, i, l)) : (d.current = !0);
                  }, [l, E, i]),
                  (0, a.useEffect)(() => {
                    A(r);
                  }, [r]),
                  (0, a.useEffect)(
                    () => () => {
                      (p.externalModel.dispose(), _.current.forEach((e) => e()));
                    },
                    [p],
                  ),
                  s().createElement(t.Provider, { value: p }, o)
                );
              },
              () => (0, a.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  quest: e.object("quest"),
                  quests: e.object("quests"),
                  isSwitched: K.LO.box(!1),
                  isIncrease: K.LO.box(!1),
                  isDecrease: K.LO.box(!1),
                  isHideQuests: K.LO.box(!1),
                  isLightVisible: K.LO.box(!0),
                  tabId: K.LO.box(1),
                },
                t = (e) => ue(e, X),
                a = (e) => ue(e, (e) => Object.assign({}, e)),
                s = (0, te.Om)(
                  () =>
                    ue(u.quests.get().questsLines, (e) =>
                      Object.assign({}, e, { cards: t(e.cards) }),
                    ),
                  { equals: Y },
                ),
                r = (0, te.Om)(() => a(u.quests.get().tabs), { equals: Y }),
                n = (e) => ({
                  isDone: e.isDone,
                  quests: ue(e.quests, (e) =>
                    Object.assign({}, e, { progression: a(e.progression) }),
                  ),
                  rewards: a(e.rewards),
                  relation: Object.assign({}, e.relation, {
                    groups: ue(e.relation.groups, (e) => ({ names: t(e.names) })),
                  }),
                }),
                i = (0, te.Om)(() => n(u.quest.get().questData.mainQuests), { equals: Y }),
                o = (0, te.Om)(() => n(u.quest.get().questData.addQuests), { equals: Y }),
                l = (0, te.Om)(
                  (e) =>
                    e.reduce(
                      (e, u) =>
                        u.isFailed
                          ? { done: e.done, failed: e.failed + 1 }
                          : u.currentValue === u.to
                            ? { done: e.done + 1, failed: e.failed }
                            : e,
                      { done: 0, failed: 0 },
                    ),
                  { equals: Y },
                ),
                _ = (0, te.Om)(() => t(u.quest.get().cardsList), { equals: Y });
              return Object.assign({}, u, {
                computes: {
                  getQuestsLine: s,
                  getTabs: r,
                  getCardList: _,
                  getIdentityArray: t,
                  getDoneFailedCount: l,
                  getQuestData: () => [i(), o()],
                },
              });
            },
            ({ externalModel: e, model: u }) =>
              Object.assign(
                {
                  switchTab: e.createCallback((e) => ({ tabId: e }), "quests.switchTab"),
                  openQuest: e.createCallback((e) => ({ questId: e }), "openQuest"),
                  openRewardOperation: e.createCallbackNoArgs("quests.openVehicleViewWindow"),
                  close: e.createCallbackNoArgs("onClose"),
                  onBackToOperations: e.createCallbackNoArgs("onBackToOperations"),
                  switchSelected: e.createCallback((e) => ({ id: e }), "quest.switchSelected"),
                  getSelectionBonus: e.createCallback(
                    (e) => ({ questId: e }),
                    "quest.getSelectionBonus",
                  ),
                  applyQuest: e.createCallback((e) => ({ id: e }), "quest.applyQuest"),
                  nextQuest: e.createCallbackNoArgs("quest.nextQuest"),
                  prevQuest: e.createCallbackNoArgs("quest.prevQuest"),
                  resetQuest: e.createCallback((e) => ({ id: e }), "quest.resetQuest"),
                  pauseQuest: e.createCallback((e) => ({ id: e }), "quest.pauseQuest"),
                  updateRewards: e.createCallbackNoArgs("quest.updateRewards"),
                },
                (function (e) {
                  const u = {};
                  for (const t in e)
                    if (Object.prototype.hasOwnProperty.call(e, t)) {
                      const a = e[t];
                      u[t] = (0, K.aD)(a);
                    }
                  return u;
                })({
                  setIsSwitched: (e) => u.isSwitched.set(e),
                  setIncrease: (e) => u.isIncrease.set(e),
                  setDecrease: (e) => u.isDecrease.set(e),
                  setLightVisible: (e) => u.isLightVisible.set(e),
                  setHideQuests: (e) => u.isHideQuests.set(e),
                  setTabId: (e) => u.tabId.set(e),
                }),
              ),
          ),
          se = ae[0],
          re = ae[1],
          ne = {
            base: "App_base_cf",
            baseWrapper: "App_baseWrapper_16",
            base__customSmall: "App_base__customSmall_24",
            base__customLarge: "App_base__customLarge_4b",
            base__scaled: "App_base__scaled_01",
            content: "App_content_ac",
            bg: "App_bg_f4",
            bg__increase: "App_bg__increase_49",
            increaseBg: "App_increaseBg_ad",
            bg__decrease: "App_bg__decrease_2f",
            decreaseBg: "App_decreaseBg_af",
            board: "App_board_8a",
            board__quest: "App_board__quest_df",
            board__increase: "App_board__increase_64",
            "increaseBoard-extraSmall": "App_increaseBoard-extraSmall_96",
            "increaseBoard-small": "App_increaseBoard-small_e6",
            "increaseBoard-medium": "App_increaseBoard-medium_32",
            "increaseBoard-large": "App_increaseBoard-large_f9",
            "increaseBoard-extraLarge": "App_increaseBoard-extraLarge_8b",
            "increaseBoard-custom-large": "App_increaseBoard-custom-large_53",
            "increaseBoard-scaled-medium": "App_increaseBoard-scaled-medium_42",
            "increaseBoard-scaled-large": "App_increaseBoard-scaled-large_6b",
            board__decrease: "App_board__decrease_d7",
            "decreaseBoard-extraSmall": "App_decreaseBoard-extraSmall_85",
            "decreaseBoard-small": "App_decreaseBoard-small_6d",
            "decreaseBoard-medium": "App_decreaseBoard-medium_8a",
            "decreaseBoard-large": "App_decreaseBoard-large_41",
            "decreaseBoard-extraLarge": "App_decreaseBoard-extraLarge_68",
            "decreaseBoard-custom-large": "App_decreaseBoard-custom-large_dd",
            "decreaseBoard-custom-extraLarge": "App_decreaseBoard-custom-extraLarge_3a",
            "decreaseBoard-scaled-medium": "App_decreaseBoard-scaled-medium_47",
            "decreaseBoard-scaled-large": "App_decreaseBoard-scaled-large_b5",
            vignette: "App_vignette_b4",
            headerBtn: "App_headerBtn_dd",
            fadeIn: "App_fadeIn_61",
            fadeOut: "App_fadeOut_2b",
            translateRightWithFadeIn: "App_translateRightWithFadeIn_ce",
            translateLeftWithFadeOut: "App_translateLeftWithFadeOut_94",
            translateTopWithFadeIn: "App_translateTopWithFadeIn_c1",
            translateTopWithFadeOut: "App_translateTopWithFadeOut_9e",
            translateBottomWithFadeIn: "App_translateBottomWithFadeIn_19",
            translateBottomWithFadeOut: "App_translateBottomWithFadeOut_f4",
            showQuests: "App_showQuests_d2",
            switchedQuests: "App_switchedQuests_15",
            switchCardAnim: "App_switchCardAnim_f1",
            switchCardAnimIn: "App_switchCardAnimIn_ee",
            switchCardAnimOut: "App_switchCardAnimOut_9e",
          };
        let ie, oe;
        (!(function (e) {
          ((e.Locked = "locked"),
            (e.LockedNoVehicle = "lockedNoVehicle"),
            (e.Active = "active"),
            (e.Alert = "alert"),
            (e.CompleteWithHonor = "completeWithHonor"),
            (e.Complete = "complete"));
        })(ie || (ie = {})),
          (function (e) {
            ((e.Switch = "switch"),
              (e.NotAvailable = "notAvailable"),
              (e.Available = "available"),
              (e.Pause = "pause"),
              (e.InProgress = "inProgress"),
              (e.DoneS = "doneSwitch"),
              (e.Done = "done"),
              (e.DoneP = "donePause"),
              (e.DoneH = "doneHonor"));
          })(oe || (oe = {})));
        var le = t(521),
          _e = t(364);
        const ce = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function de(e = le.n.NONE, u = ce, t = !1) {
          (0, a.useEffect)(() => {
            if (e !== le.n.NONE)
              return (
                window.addEventListener("keydown", a, t),
                () => {
                  window.removeEventListener("keydown", a, t);
                }
              );
            function a(a) {
              if (a.keyCode === e) {
                if (n.O.view.isEventHandled()) return;
                (n.O.view.setEventHandled(), u(a), t && a.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        function me(e) {
          de(le.n.ESCAPE, e);
        }
        const Ee = {
            base: "Character_base_65",
            bg: "Character_bg_87",
            bg__complete: "Character_bg__complete_28",
            bg__completeAdd: "Character_bg__completeAdd_17",
            bg__completeWithHonor: "Character_bg__completeWithHonor_ab",
            bg__active: "Character_bg__active_4c",
          },
          Ae = (0, a.memo)(({ className: e, state: u }) => {
            const t = z().isCustomLarge,
              a = B()(Ee.base, t && Ee.base__custom, e),
              r = B()(Ee.bg, Ee[`bg__${u}`]);
            return s().createElement(
              "div",
              { className: a },
              s().createElement("div", { className: r }),
            );
          }),
          Fe = {
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
        let pe, De;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(pe || (pe = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(De || (De = {})));
        const ge = ({
          children: e,
          size: u,
          isFocused: t,
          type: r,
          disabled: n,
          mixClass: i,
          soundHover: o,
          soundClick: l,
          onMouseEnter: _,
          onMouseMove: c,
          onMouseDown: d,
          onMouseUp: m,
          onMouseLeave: E,
          onClick: A,
        }) => {
          const F = (0, a.useRef)(null),
            p = (0, a.useState)(t),
            D = p[0],
            g = p[1],
            C = (0, a.useState)(!1),
            b = C[0],
            h = C[1],
            v = (0, a.useState)(!1),
            w = v[0],
            f = v[1],
            S = (0, a.useCallback)(() => {
              n || (F.current && (F.current.focus(), g(!0)));
            }, [n]),
            x = (0, a.useCallback)(
              (e) => {
                D && null !== F.current && !F.current.contains(e.target) && g(!1);
              },
              [D],
            ),
            T = (0, a.useCallback)(
              (e) => {
                n || (A && A(e));
              },
              [n, A],
            ),
            L = (0, a.useCallback)(
              (e) => {
                n || (null !== o && M(o), _ && _(e), f(!0));
              },
              [n, o, _],
            ),
            P = (0, a.useCallback)(
              (e) => {
                c && c(e);
              },
              [c],
            ),
            N = (0, a.useCallback)(
              (e) => {
                n || (m && m(e), h(!1));
              },
              [n, m],
            ),
            y = (0, a.useCallback)(
              (e) => {
                n || (null !== l && M(l), d && d(e), t && S(), h(!0));
              },
              [n, l, d, S, t],
            ),
            I = (0, a.useCallback)(
              (e) => {
                n || (E && E(e), h(!1));
              },
              [n, E],
            ),
            O = B()(
              Fe.base,
              Fe[`base__${r}`],
              {
                [Fe.base__disabled]: n,
                [Fe[`base__${u}`]]: u,
                [Fe.base__focus]: D,
                [Fe.base__highlightActive]: b,
                [Fe.base__firstHover]: w,
              },
              i,
            ),
            k = B()(Fe.state, Fe.state__default);
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
              g(t);
            }, [t]),
            s().createElement(
              "div",
              {
                ref: F,
                className: O,
                onMouseEnter: L,
                onMouseMove: P,
                onMouseUp: N,
                onMouseDown: y,
                onMouseLeave: I,
                onClick: T,
              },
              r !== pe.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: Fe.back }),
                  s().createElement("span", { className: Fe.texture }),
                ),
              s().createElement(
                "span",
                { className: k },
                s().createElement("span", { className: Fe.stateDisabled }),
                s().createElement("span", { className: Fe.stateHighlightHover }),
                s().createElement("span", { className: Fe.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: Fe.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        ge.defaultProps = {
          type: pe.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Be = (0, a.memo)(ge);
        var Ce = t(887),
          be = t.n(Ce);
        const he = ["xl", "lg", "md", "sm", "xs"],
          ve = (e) => e.includes("_") && ((e) => he.includes(e))(e.split("_").at(-1)),
          we = [h.ExtraLarge, h.Large, h.Medium, h.Small, h.ExtraSmall],
          fe = (e, u) =>
            Object.keys(e).reduce((t, a) => {
              if (a in t) return t;
              if (ve(a)) {
                const s = a.split("_").slice(0, -1).join("_");
                if (s in t) return t;
                const r = we.indexOf(u),
                  n = (-1 !== r ? he.slice(r) : [])
                    .map((e) => s + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  i = n ? e[n] : void 0;
                return ((t[s] = void 0 !== i ? i : e[s]), t);
              }
              const s = e[a];
              return (
                void 0 === s ||
                  ((e, u) => he.some((t) => void 0 !== u[`${e}_${t}`]))(a, e) ||
                  (t[a] = s),
                t
              );
            }, {}),
          Se = (e, u = fe) => {
            const t = (
              (e, u = fe) =>
              (t) => {
                const r = f().mediaSize,
                  n = (0, a.useMemo)(() => u(t, r), [t, r]);
                return s().createElement(e, n);
              }
            )(e, u);
            return s().memo((u) =>
              Object.keys(u).some((e) => ve(e) && void 0 !== u[e])
                ? s().createElement(t, u)
                : s().createElement(e, u),
            );
          },
          xe = {
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
          Te = [
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
        function Le() {
          return (
            (Le =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Le.apply(this, arguments)
          );
        }
        Object.keys(be());
        const Pe = {
            XL: { mt: xe.mt__XL, mr: xe.mr__XL, mb: xe.mb__XL, ml: xe.ml__XL },
            LG: { mt: xe.mt__LG, mr: xe.mr__LG, mb: xe.mb__LG, ml: xe.ml__LG },
            MDp: { mt: xe.mt__MDp, mr: xe.mr__MDp, mb: xe.mb__MDp, ml: xe.ml__MDp },
            MD: { mt: xe.mt__MD, mr: xe.mr__MD, mb: xe.mb__MD, ml: xe.ml__MD },
            SMp: { mt: xe.mt__SMp, mr: xe.mr__SMp, mb: xe.mb__SMp, ml: xe.ml__SMp },
            SM: { mt: xe.mt__SM, mr: xe.mr__SM, mb: xe.mb__SM, ml: xe.ml__SM },
            XS: { mt: xe.mt__XS, mr: xe.mr__XS, mb: xe.mb__XS, ml: xe.ml__XS },
          },
          Ne = (Object.keys(Pe), ["mt", "mr", "mb", "ml"]),
          Re = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          ye = Se((e) => {
            let u = e.className,
              t = e.width,
              r = e.height,
              n = e.m,
              i = e.mt,
              o = void 0 === i ? n : i,
              l = e.mr,
              _ = void 0 === l ? n : l,
              c = e.mb,
              d = void 0 === c ? n : c,
              m = e.ml,
              E = void 0 === m ? n : m,
              A = e.column,
              F = e.row,
              p = e.flexDirection,
              D = void 0 === p ? (A ? "column" : F && "row") || void 0 : p,
              g = e.flexStart,
              C = e.center,
              b = e.flexEnd,
              h = e.spaceBetween,
              v = e.spaceAround,
              w = e.justifyContent,
              f =
                void 0 === w
                  ? (g ? "flex-start" : C && "center") ||
                    (b && "flex-end") ||
                    (h && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : w,
              S = e.alignItems,
              x =
                void 0 === S
                  ? (g ? "flex-start" : C && "center") || (b && "flex-end") || void 0
                  : S,
              T = e.alignSelf,
              L = e.wrap,
              P = e.flexWrap,
              N = void 0 === P ? (L ? "wrap" : void 0) : P,
              R = e.grow,
              y = e.shrink,
              I = e.flex,
              O = void 0 === I ? (R || y ? `${R ? 1 : 0} ${y ? 1 : 0} auto` : void 0) : I,
              k = e.style,
              M = e.children,
              H = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  s = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                return s;
              })(e, Te);
            const Q = (0, a.useMemo)(() => {
                const e = { mt: o, mr: _, mb: d, ml: E },
                  u = ((e) =>
                    Ne.reduce((u, t) => {
                      const a = e[t];
                      return a && "number" != typeof a ? u.concat(Pe[!0 === a ? "MD" : a][t]) : u;
                    }, []))(e),
                  a = ((e) =>
                    Ne.reduce((u, t) => {
                      const a = e[t];
                      return ("number" == typeof a && (u[Re[t]] = a + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, k, a, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: O,
                    alignSelf: T,
                    display: D || x ? "flex" : void 0,
                    flexDirection: D,
                    flexWrap: N,
                    justifyContent: f,
                    alignItems: x,
                  }),
                  computedClassNames: u,
                };
              }, [t, r, o, _, d, E, k, O, T, D, N, f, x]),
              W = Q.computedStyle,
              V = Q.computedClassNames;
            return s().createElement(
              "div",
              Le({ className: B()(xe.base, ...V, u), style: W }, H),
              M,
            );
          });
        let Ie;
        function Oe(e, u) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const t = 0 === e.indexOf("%") ? 2 : 1;
            return String(u[e.slice(t, -t)]);
          });
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(Ie || (Ie = {}));
        const ke = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          Me = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          He = (e, u, t = Ie.left) => e.split(u).reduce(t === Ie.left ? ke : Me, []),
          Qe = (() => {
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
          We = ["zh_cn", "zh_sg", "zh_tw"],
          Ve = (e, u = Ie.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return We.includes(t)
              ? Qe(e)
              : ((e, u = Ie.left) => {
                  let t = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    s = e.replace(/&nbsp;/g, " ");
                  return (He(s, /( )/, u).forEach((e) => (t = t.concat(He(e, a, Ie.left)))), t);
                })(e, u);
          },
          Ue = "FormatText_base_d0",
          Ge = ({ binding: e, text: u = "", classMix: t, alignment: r = Ie.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : s().createElement(
                  a.Fragment,
                  null,
                  u.split("\n").map((u, n) =>
                    s().createElement(
                      "div",
                      { className: B()(Ue, t), key: `${u}-${n}` },
                      ((e, u, t) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (t && e in t ? t[e] : Ve(e, u))))(u, r, e).map((e, u) =>
                        s().createElement(a.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var qe = t(532),
          $e = t.n(qe);
        const je = {
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
          ze = [
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
        function Xe() {
          return (
            (Xe =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Xe.apply(this, arguments)
          );
        }
        Object.keys(be());
        const Ye = Object.keys($e()),
          Ke = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Ze = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Je = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          eu = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          uu =
            (Object.keys(eu),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ke,
              "heading-H36": Ke,
              "heading-H28": Ze,
              "heading-H24": Ze,
              "heading-H24R": Ze,
              "heading-H22": Ze,
              "heading-H20R": Ze,
              "heading-H18": Ze,
              "heading-H15": Je,
              "heading-H14": Je,
              "paragraph-P24": Ze,
              "paragraph-P18": Ze,
              "paragraph-P16": Ze,
              "paragraph-P14": Je,
              "paragraph-P12": Je,
              "paragraph-P10": Je,
            }),
          tu =
            (Object.keys(uu),
            (e) =>
              e
                ? ((e) => Ye.includes(e))(e)
                  ? { colorClassName: je[e] }
                  : { colorStyle: { color: e } }
                : {}),
          au = Se((e) => {
            let u = e.text,
              t = e.variant,
              r = e.className,
              n = e.color,
              i = e.m,
              o = e.mt,
              l = void 0 === o ? i : o,
              _ = e.mr,
              c = void 0 === _ ? i : _,
              d = e.mb,
              m = void 0 === d ? i : d,
              E = e.ml,
              A = void 0 === E ? i : E,
              F = e.style,
              p = e.format,
              D = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  s = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                return s;
              })(e, ze);
            const g = (0, a.useMemo)(() => {
                const e = tu(n),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  a = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, a), colorClassName: u };
              }, [F, n]),
              C = g.computedStyle,
              b = g.colorClassName;
            return s().createElement(
              ye,
              Xe(
                {
                  className: B()(je.base, t && je[t], b, r),
                  style: C,
                  mt: !0 === l ? uu[t || "paragraph-P16"].mt : l,
                  mr: !0 === c ? uu[t || "paragraph-P16"].mr : c,
                  mb: !0 === m ? uu[t || "paragraph-P16"].mb : m,
                  ml: !0 === A ? uu[t || "paragraph-P16"].ml : A,
                },
                D,
              ),
              void 0 !== p ? s().createElement(Ge, Xe({}, p, { text: u })) : u,
            );
          }),
          su = "Footer_base_7f",
          ru = "Footer_bg_50",
          nu = "Footer_vignette_29",
          iu = R.strings.personal_missions_3.QuestsView.footer,
          ou = (0, a.memo)(({ onShowRewardClick: e, className: u }) =>
            s().createElement(
              "div",
              { className: B()(su, u) },
              s().createElement("div", { className: nu }),
              s().createElement(
                "div",
                { className: ru },
                s().createElement(
                  Be,
                  { type: pe.ghost, size: De.medium, onClick: e },
                  s().createElement(au, { text: iu.rewardBtn.text() }),
                ),
              ),
            ),
          ),
          lu = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          _u = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const cu = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          du = (e) =>
            cu
              ? `${e}`
              : (function (e) {
                  let u = "";
                  for (let t = _u.length - 1; t >= 0; t--)
                    for (; e >= _u[t];) ((u += lu[t]), (e -= _u[t]));
                  return u;
                })(e),
          mu = {
            base: "Header_base_e4",
            title: "Header_title_af",
            subtitleWrapper: "Header_subtitleWrapper_84",
            iconSubtitle: "Header_iconSubtitle_54",
            iconSubtitle__locked: "Header_iconSubtitle__locked_85",
            iconSubtitle__lockedNoVehicle: "Header_iconSubtitle__lockedNoVehicle_7c",
            iconSubtitle__active: "Header_iconSubtitle__active_b2",
            subtitle: "Header_subtitle_48",
            subtitle__locked: "Header_subtitle__locked_80",
            subtitle__active: "Header_subtitle__active_a6",
            subtitle__alert: "Header_subtitle__alert_b0",
            subtitle__lockedNoVehicle: "Header_subtitle__lockedNoVehicle_a4",
            subtitle__complete: "Header_subtitle__complete_8c",
            subtitle__completeWithHonor: "Header_subtitle__completeWithHonor_66",
          },
          Eu = R.strings.personal_missions_3.QuestsView.header,
          Au = (0, a.memo)(
            ({
              state: e,
              minVehicleLevel: u,
              maxVehicleLevel: t,
              prevOperationName: a,
              operationName: r,
            }) => {
              const n = {
                  minVehicleLevel: du(u),
                  maxVehicleLevel: du(t),
                  prevOperationName: a,
                  operationName: r,
                },
                i = B()(mu.subtitle, mu[`subtitle__${e}`]),
                o = B()(mu.iconSubtitle, mu[`iconSubtitle__${e}`]),
                l = `url(${R.images.gui.maps.icons.personalMissions3.QuestsView.header.$dyn(e)})`;
              return s().createElement(
                "div",
                { className: mu.base },
                s().createElement(au, {
                  className: mu.title,
                  text: Eu.title.text(),
                  format: { binding: n },
                }),
                s().createElement(
                  "div",
                  { className: mu.subtitleWrapper },
                  s().createElement("div", { className: o, style: { backgroundImage: l } }),
                  s().createElement(au, {
                    className: B()(i),
                    text: Eu.subtitle.$dyn(e),
                    format: { binding: n },
                  }),
                ),
              );
            },
          ),
          Fu = [
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
        function pu(e) {
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
        const Du = (e, u, t = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: _e.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: a,
                },
                t,
              ),
            );
          },
          gu = (e) => {
            let u = e.children,
              t = e.contentId,
              s = e.args,
              r = e.onMouseEnter,
              n = e.onMouseLeave,
              i = e.onMouseDown,
              o = e.onClick,
              l = e.ignoreShowDelay,
              _ = void 0 !== l && l,
              c = e.ignoreMouseClick,
              d = void 0 !== c && c,
              m = e.decoratorId,
              E = void 0 === m ? 0 : m,
              A = e.isEnabled,
              F = void 0 === A || A,
              p = e.targetId,
              D = void 0 === p ? 0 : p,
              g = e.onShow,
              B = e.onHide,
              C = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  s = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                return s;
              })(e, Fu);
            const b = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              h = (0, a.useMemo)(
                () =>
                  D ||
                  ((e = 1) => {
                    const u = new Error().stack;
                    let t,
                      a = R.invalid("resId");
                    return (
                      u &&
                        ((t = u.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== t &&
                          window.subViews[t] &&
                          (a = window.subViews[t].id)),
                      { caller: t, stack: u, resId: a }
                    );
                  })().resId,
                [D],
              ),
              v = (0, a.useCallback)(() => {
                (b.current.isVisible && b.current.timeoutId) ||
                  (Du(t, E, { isMouseEvent: !0, on: !0, arguments: pu(s) }, h),
                  g && g(),
                  (b.current.isVisible = !0));
              }, [t, E, s, h, g]),
              w = (0, a.useCallback)(() => {
                if (b.current.isVisible || b.current.timeoutId) {
                  const e = b.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (b.current.timeoutId = 0)),
                    Du(t, E, { on: !1 }, h),
                    b.current.isVisible && B && B(),
                    (b.current.isVisible = !1));
                }
              }, [t, E, h, B]),
              f = (0, a.useCallback)((e) => {
                b.current.isVisible &&
                  ((b.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (b.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(b.current.prevTarget) && w();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const e = b.current.hideTimerId;
              return (
                document.addEventListener("wheel", f, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", f, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === F && w();
              }, [F, w]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", w),
                  () => {
                    (window.removeEventListener("mouseleave", w), w());
                  }
                ),
                [w],
              ));
            return F
              ? (0, a.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((b.current.timeoutId = window.setTimeout(v, _ ? 100 : 400)),
                            r && r(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (w(), null == n || n(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === d && w(), null == o || o(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === d && w(), null == i || i(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    C,
                  ),
                )
              : u;
            var S;
          },
          Bu = ["children"];
        function Cu() {
          return (
            (Cu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Cu.apply(this, arguments)
          );
        }
        const bu = (e) => {
            let u = e.children,
              t = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  s = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                return s;
              })(e, Bu);
            return s().createElement(
              gu,
              Cu(
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
          hu = ["children", "body", "header", "note", "alert", "args"];
        function vu() {
          return (
            (vu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            vu.apply(this, arguments)
          );
        }
        const wu = R.views.common.tooltip_window.simple_tooltip_content,
          fu = (e) => {
            let u = e.children,
              t = e.body,
              r = e.header,
              n = e.note,
              i = e.alert,
              o = e.args,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  s = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                return s;
              })(e, hu);
            const _ = (0, a.useMemo)(() => {
              const e = Object.assign({}, o, { body: t, header: r, note: n, alert: i });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [i, t, r, n, o]);
            return s().createElement(
              gu,
              vu(
                {
                  contentId:
                    ((c = null == o ? void 0 : o.hasHtmlContent),
                    c ? wu.SimpleTooltipHtmlContent("resId") : wu.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: _,
                },
                l,
              ),
              u,
            );
            var c;
          };
        function Su() {
          return (
            (Su =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Su.apply(this, arguments)
          );
        }
        const xu = ({ children: e, tooltipArgs: u, className: t }) => {
          if (!u) return e;
          const a = s().createElement("div", { className: t }, e);
          if (u.header || u.body) return s().createElement(fu, u, a);
          const r = u.contentId,
            n = u.args,
            i = null == n ? void 0 : n.contentId;
          return r || i
            ? s().createElement(gu, Su({}, u, { contentId: r || i }), a)
            : s().createElement(bu, u, a);
        };
        let Tu, Lu;
        (!(function (e) {
          ((e.Switch = "switch"),
            (e.NotAvailable = "notAvailable"),
            (e.Available = "available"),
            (e.Pause = "pause"),
            (e.InProgress = "inProgress"),
            (e.InProgressHonor = "inProgressHonor"),
            (e.DoneS = "doneSwitch"),
            (e.Done = "done"),
            (e.DoneP = "donePause"),
            (e.DoneH = "doneHonor"));
        })(Tu || (Tu = {})),
          (function (e) {
            ((e.CompleteBasic = "completeBasic"),
              (e.Complete = "complete"),
              (e.CompleteHonor = "completeHonor"),
              (e.InProgress = "inProgress"),
              (e.InProgressHonor = "inProgressHonor"),
              (e.OnPause = "isOnPause"),
              (e.Unlock = "unlock"),
              (e.UnlockInProgress = "unlockInProgress"),
              (e.SwitchHonorProgress = "switchHonorProgress"),
              (e.SwitchHonorPause = "switchHonorPause"),
              (e.SwitchPause = "switchPause"),
              (e.SwitchProgress = "switchProgress"),
              (e.Locked = "locked"),
              (e.Default = "default"),
              (e.SwitchCompleteInProgress = "switchCompleteInProgress"),
              (e.SwitchInProgressComplete = "switchInProgressComplete"));
          })(Lu || (Lu = {})));
        const Pu = "AnimatedQuestCard_base_48",
          Nu = "AnimatedQuestCard_stroke_5c",
          Ru = "AnimatedQuestCard_stroke__scaledBlink_af",
          yu = "AnimatedQuestCard_stroke__show_e0",
          Iu = "AnimatedQuestCard_stroke__lock_3a",
          Ou = "AnimatedQuestCard_stroke__progress_75",
          ku = "AnimatedQuestCard_stroke__pause_ac",
          Mu = "AnimatedQuestCard_stroke__complete_66",
          Hu = "AnimatedQuestCard_bg_2b",
          Qu = "AnimatedQuestCard_bg__show_29",
          Wu = "AnimatedQuestCard_bg__hide_b9",
          Vu = "AnimatedQuestCard_bg__lock_b2",
          Uu = "AnimatedQuestCard_bg__progress_b9",
          Gu = "AnimatedQuestCard_bg__pause_2b",
          qu = "AnimatedQuestCard_bg__complete_45",
          $u = "AnimatedQuestCard_icon_dc",
          ju = "AnimatedQuestCard_icon__show_56",
          zu = "AnimatedQuestCard_icon__downScale_90",
          Xu = "AnimatedQuestCard_icon__upScale_68",
          Yu = "AnimatedQuestCard_icon__unlock_6d",
          Ku = "AnimatedQuestCard_icon__showScale_a0",
          Zu = "AnimatedQuestCard_icon__pause_a8",
          Ju = "AnimatedQuestCard_icon__lock_20",
          et = "AnimatedQuestCard_icon__complete_65",
          ut = "AnimatedQuestCard_icon__progress_72",
          tt = {
            [Lu.InProgress]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, Ou, yu) }),
              s().createElement("div", { className: B()(Nu, Ou, Ru) }),
              s().createElement("div", { className: B()(Hu, Uu, Qu) }),
              s().createElement("div", { className: B()($u, ut, ju) }),
            ),
            [Lu.InProgressHonor]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Hu, qu, Qu) }),
              s().createElement("div", { className: B()($u, ut, ju) }),
            ),
            [Lu.Unlock]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, Iu, yu) }),
              s().createElement("div", { className: B()(Nu, Iu, Ru) }),
              s().createElement("div", { className: B()(Hu, Vu, Wu) }),
              s().createElement("div", { className: B()($u, Ju, Yu) }),
            ),
            [Lu.UnlockInProgress]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, Iu, yu) }),
              s().createElement("div", { className: B()(Nu, Iu, Ru) }),
              s().createElement("div", { className: B()(Hu, Vu, Wu) }),
              s().createElement("div", { className: B()($u, Ju, Yu) }),
              s().createElement("div", { className: B()(Hu, Uu, Qu) }),
              s().createElement("div", { className: B()($u, ut, ju) }),
            ),
            [Lu.CompleteBasic]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, Mu, yu) }),
              s().createElement("div", { className: B()(Nu, Mu, Ru) }),
              s().createElement("div", { className: B()(Hu, qu, Qu) }),
              s().createElement("div", { className: B()($u, et, ju) }),
            ),
            [Lu.Complete]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, Mu, yu) }),
              s().createElement("div", { className: B()(Nu, Mu, Ru) }),
              s().createElement("div", { className: B()(Hu, qu, Qu) }),
            ),
            [Lu.CompleteHonor]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Hu, qu) }),
              s().createElement("div", { className: B()($u, et, ju) }),
            ),
            [Lu.SwitchHonorProgress]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, ku, yu) }),
              s().createElement("div", { className: B()(Hu, qu, Wu) }),
              s().createElement("div", { className: B()(Hu, Gu, Qu) }),
              s().createElement("div", { className: B()($u, ut, zu) }),
              s().createElement("div", { className: B()($u, Zu, Xu) }),
            ),
            [Lu.SwitchHonorPause]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, Mu, yu) }),
              s().createElement("div", { className: B()(Hu, Gu, Wu) }),
              s().createElement("div", { className: B()(Hu, qu, Qu) }),
              s().createElement("div", { className: B()($u, Zu, Yu) }),
              s().createElement("div", { className: B()($u, ut, Ku) }),
            ),
            [Lu.SwitchPause]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, ku, yu) }),
              s().createElement("div", { className: B()(Hu, Uu, Wu) }),
              s().createElement("div", { className: B()(Hu, Gu, Qu) }),
              s().createElement("div", { className: B()($u, ut, zu) }),
              s().createElement("div", { className: B()($u, Zu, Xu) }),
            ),
            [Lu.SwitchProgress]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, Ou, yu) }),
              s().createElement("div", { className: B()(Hu, Gu, Wu) }),
              s().createElement("div", { className: B()(Hu, Uu, Qu) }),
              s().createElement("div", { className: B()($u, ut, Ku) }),
              s().createElement("div", { className: B()($u, Zu, Yu) }),
            ),
            [Lu.OnPause]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Nu, ku, yu) }),
              s().createElement("div", { className: B()(Hu, Gu, Qu) }),
              s().createElement("div", { className: B()($u, Zu, Ku) }),
            ),
            [Lu.SwitchCompleteInProgress]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Hu, qu) }),
              s().createElement("div", { className: B()($u, ut, Ku) }),
            ),
            [Lu.SwitchInProgressComplete]: s().createElement(
              s().Fragment,
              null,
              s().createElement("div", { className: B()(Hu, qu) }),
              s().createElement("div", { className: B()($u, ut, zu) }),
            ),
          },
          at = (0, a.memo)(({ state: e, className: u }) => {
            const t = ((e) => {
              if (e !== Lu.Default && e !== Lu.Locked) return tt[e];
            })(e);
            return s().createElement("div", { className: B()(Pu, u) }, t);
          }),
          st = {
            base: "QuestCard_base_18",
            base__available: "QuestCard_base__available_6b",
            base__hover: "QuestCard_base__hover_13",
            base__notAvailable: "QuestCard_base__notAvailable_d9",
            base__doneSwitch: "QuestCard_base__doneSwitch_f7",
            base__switch: "QuestCard_base__switch_eb",
            base__inProgress: "QuestCard_base__inProgress_21",
            base__inProgressHonor: "QuestCard_base__inProgressHonor_a9",
            base__done: "QuestCard_base__done_9d",
            base__doneHonor: "QuestCard_base__doneHonor_27",
            base__pause: "QuestCard_base__pause_7d",
            base__donePause: "QuestCard_base__donePause_e7",
            animQuest: "QuestCard_animQuest_52",
            contentWrapper: "QuestCard_contentWrapper_d9",
            questID: "QuestCard_questID_98",
            conditionsImg: "QuestCard_conditionsImg_80",
            cardWrapper: "QuestCard_cardWrapper_b5",
            cardIcon: "QuestCard_cardIcon_3f",
            disableWrapper: "QuestCard_disableWrapper_c1",
            disableIcon: "QuestCard_disableIcon_fe",
            disableIcon__isUnlock: "QuestCard_disableIcon__isUnlock_3f",
            lastIconWrapper: "QuestCard_lastIconWrapper_6d",
            complete: "QuestCard_complete_ca",
            complete__isUnlock: "QuestCard_complete__isUnlock_8a",
            doneHonor: "QuestCard_doneHonor_d4",
            complete__withHonor: "QuestCard_complete__withHonor_e8",
            complete__inProgressHonor: "QuestCard_complete__inProgressHonor_c8",
            inProgress: "QuestCard_inProgress_fc",
          },
          rt = (0, q.Pi)(
            ({
              questId: e,
              isLast: u = !1,
              state: t = Tu.Available,
              animationType: r = Lu.Default,
              selectionAvailable: n = !1,
              isSelected: i = !1,
              onQuestClicked: o,
              questName: l,
              className: _,
            }) => {
              const c = re().controls,
                d = (0, a.useState)(!1),
                m = d[0],
                E = d[1],
                A = t !== Tu.Available,
                F = u && (t === Tu.DoneP || t === Tu.Pause),
                p = t !== Tu.Switch && t !== Tu.DoneS,
                D = u && t === Tu.InProgressHonor,
                g = r === Lu.Default || r === Lu.Locked,
                C = (t === Tu.Done || t === Tu.DoneH || D) && g,
                b = t === Tu.DoneH,
                h = t === Tu.InProgressHonor,
                v = t === Tu.InProgress && g,
                w =
                  !(
                    t === Tu.Available ||
                    t === Tu.Pause ||
                    (t === Tu.Done && u) ||
                    t === Tu.DoneP ||
                    t === Tu.InProgressHonor
                  ) &&
                  !C &&
                  !v &&
                  g,
                f = t === Tu.DoneS || t === Tu.Switch,
                S = B()(
                  st.base,
                  _,
                  st[`base__${g ? t : st.base__available}`],
                  w && st.base__disabled,
                  u && st.base__last,
                  i && st.base__selected,
                  m && st.base__hover,
                ),
                x = (0, a.useState)(!1),
                T = x[0],
                L = x[1];
              (0, a.useEffect)(
                () =>
                  G(() => {
                    T && (o(e), c.setIncrease(!0), L(!1));
                  }, 500),
                [T, o, c, e],
              );
              const P = B()(
                st.complete,
                b && st.complete__withHonor,
                h && st.complete__inProgressHonor,
              );
              return s().createElement(
                "div",
                {
                  className: S,
                  onMouseEnter: () => {
                    p && (M(R.sounds.highlight()), E(!0));
                  },
                  onMouseLeave: () => {
                    E(!1);
                  },
                  onClick: () => {
                    n && !f && (M(R.sounds.play()), c.setHideQuests(!0), L(!0));
                  },
                },
                s().createElement(
                  "div",
                  { className: st.contentWrapper },
                  s().createElement(at, { state: r, className: st.animQuest }),
                  A &&
                    (F || !u) &&
                    s().createElement(
                      "div",
                      { className: st.cardWrapper },
                      s().createElement("div", { className: B()(st.cardIcon) }),
                    ),
                  u &&
                    s().createElement(
                      s().Fragment,
                      null,
                      w &&
                        s().createElement(
                          "div",
                          { className: st.disableWrapper },
                          s().createElement("div", { className: st.disableIcon }),
                        ),
                      s().createElement(
                        "div",
                        { className: st.lastIconWrapper },
                        C && s().createElement("div", { className: P }),
                        v && s().createElement("div", { className: st.inProgress }),
                      ),
                    ),
                  s().createElement(au, { className: st.questID, text: l }),
                ),
              );
            },
          ),
          nt = "QuestLine_base_29",
          it = "QuestLine_questCard_3f";
        function ot() {
          return (
            (ot =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ot.apply(this, arguments)
          );
        }
        const lt = R.strings.personal_missions_3.tooltips.questCard,
          _t = (e, u) =>
            e.type === Tu.Switch || e.type === Tu.DoneS
              ? {
                  header: Oe(lt.header.switch(), { questName: e.questName }),
                  body: lt.body.switch(),
                }
              : {
                  contentId: R.views.lobby.personal_missions.tooltips.QuestCardTooltip("resId"),
                  args: { questId: u },
                },
          ct = (0, a.memo)(({ cards: e, onQuestClicked: u }) =>
            s().createElement(
              "div",
              { className: nt },
              e.map((t, a) => {
                const r = a === e.length - 1;
                return s().createElement(
                  "div",
                  { key: t.id },
                  s().createElement(
                    xu,
                    { tooltipArgs: _t(t, t.id) },
                    s().createElement(
                      "div",
                      { key: t.id },
                      s().createElement(
                        rt,
                        ot({}, t, {
                          questId: String(t.id),
                          selectionAvailable: !0,
                          state: t.type,
                          isLast: r,
                          onQuestClicked: u,
                          className: it,
                        }),
                      ),
                    ),
                  ),
                );
              }),
            ),
          ),
          dt = "QuestType_base_52",
          mt = R.images.gui.maps.icons.personalMissions3.QuestsView.types,
          Et = (0, a.memo)(({ type: e, className: u }) => {
            const t = `url(${mt.$dyn(e)})`;
            return s().createElement(
              gu,
              {
                contentId:
                  R.views.lobby.personal_missions.tooltips.PersonalMissionsQuestsTypeTooltip(
                    "resId",
                  ),
                args: { type: e },
              },
              s().createElement("div", { className: B()(dt, u), style: { backgroundImage: t } }),
            );
          }),
          At = "Quests_base_3a",
          Ft = "Quests_questsContainer_3b",
          pt = "Quests_questsLine_49",
          Dt = "Quests_questType_80",
          gt = (0, a.memo)(({ className: e, questsLines: u, onQuestClicked: t }) =>
            s().createElement(
              "div",
              { className: B()(At, e) },
              u.map((e) =>
                s().createElement(
                  "div",
                  { key: e.id, className: Ft },
                  s().createElement(
                    "div",
                    { className: pt },
                    s().createElement(Et, { key: e.id, type: e.type, className: Dt }),
                    s().createElement(ct, { cards: e.cards, onQuestClicked: t }),
                  ),
                ),
              ),
            ),
          ),
          Bt = {
            base: "Stand_base_44",
            standIcon: "Stand_standIcon_13",
            standIcon__complete: "Stand_standIcon__complete_51",
            standIcon__completeWithHonor: "Stand_standIcon__completeWithHonor_15",
          },
          Ct = (0, a.memo)(({ state: e, className: u }) => {
            const t = B()(Bt.standIcon, Bt[`standIcon__${e}`]);
            return s().createElement(
              "div",
              { className: B()(Bt.base, u) },
              s().createElement("div", { className: t }),
            );
          }),
          bt = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let ht, vt;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(ht || (ht = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(vt || (vt = {})));
        const wt = ({ size: e = ht.Default, classMix: u }) =>
            s().createElement("div", { className: B()(bt.background, bt[`background__${e}`], u) }),
          ft = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          St = ({ size: e }) => {
            const u = B()(ft.base, ft[`base__${e}`]);
            return s().createElement("div", { className: u });
          },
          xt = {
            base: "ProgressLineImpose_base_80",
            base__disabled: "ProgressLineImpose_base__disabled_cc",
            base__finished: "ProgressLineImpose_base__finished_d4",
            base__withoutBounce: "ProgressLineImpose_base__withoutBounce_56",
            pattern: "ProgressLineImpose_pattern_1c",
            base__small: "ProgressLineImpose_base__small_55",
            gradient: "ProgressLineImpose_gradient_35",
            glow: "ProgressLineImpose_glow_a5",
            glow__left: "ProgressLineImpose_glow__left_d8",
          },
          Tt = (0, a.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: a,
              isComplete: r,
              withoutBounce: n,
            }) => {
              const i = B()(
                  xt.base,
                  xt[`base__${e}`],
                  t && xt.base__disabled,
                  r && xt.base__finished,
                  n && xt.base__withoutBounce,
                ),
                o = !t && !r;
              return s().createElement(
                "div",
                { className: i, style: a, ref: u },
                s().createElement("div", { className: xt.pattern }),
                s().createElement("div", { className: xt.gradient }),
                o && s().createElement(St, { size: e }),
              );
            },
          ),
          Lt = ({ size: e, value: u, lineRef: t, disabled: r, onComplete: n }) => {
            const i = (0, a.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              o = 100 === u;
            return (
              (0, a.useEffect)(() => {
                o && n && n();
              }, [o, n]),
              s().createElement(Tt, {
                size: e,
                disabled: r,
                baseStyles: i,
                isComplete: o,
                lineRef: t,
              })
            );
          };
        let Pt, Nt;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(Pt || (Pt = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(Nt || (Nt = {})));
        const Rt = "ProgressBarDeltaSimple_base_6c",
          yt = "ProgressBarDeltaSimple_delta_99",
          It = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: n,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
            }) => {
              const _ = i < r,
                c = (0, a.useState)(Nt.Idle),
                d = c[0],
                m = c[1],
                E = d === Nt.In,
                A = d === Nt.End,
                F = d === Nt.Idle,
                p = (0, a.useCallback)(
                  (e) => {
                    (m(e), l && l(e));
                  },
                  [l],
                );
              ((0, a.useEffect)(() => {
                if (F && !t) {
                  return G(() => {
                    p(Nt.In);
                  }, u);
                }
              }, [p, t, F, u]),
                (0, a.useEffect)(() => {
                  if (E) {
                    return G(() => {
                      (o && o(), p(Nt.End));
                    }, e + u);
                  }
                }, [p, E, o, u, e]));
              const D = (0, a.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, u, e],
                ),
                g = (0, a.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, u, e],
                ),
                B = (0, a.useMemo)(
                  () => ({ width: `${Math.abs(r - i)}%`, left: `${_ ? i : r}%` }),
                  [r, _, i],
                );
              return A
                ? null
                : s().createElement(
                    "div",
                    { className: Rt, style: B },
                    s().createElement(
                      "div",
                      { style: F ? D : g, className: yt },
                      s().createElement(St, { size: n }),
                    ),
                  );
            },
          ),
          Ot = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: n,
              isComplete: i,
              animationSettings: o,
              onChangeAnimationState: l,
              onEndAnimation: _,
            }) => {
              const c = (0, a.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${o.line.duration}ms`,
                  transitionDelay: `${o.line.delay}ms`,
                }),
                [o.line.delay, o.line.duration, e],
              );
              return s().createElement(
                s().Fragment,
                null,
                s().createElement(Tt, {
                  size: u,
                  lineRef: r,
                  disabled: n,
                  isComplete: i,
                  baseStyles: c,
                }),
                t >= 0 &&
                  s().createElement(It, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    freezed: o.freezed,
                    from: t,
                    size: u,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: _,
                  }),
              );
            },
          ),
          kt = "ProgressBarDeltaGrow_base_7e",
          Mt = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          Ht = "ProgressBarDeltaGrow_glow_68",
          Qt = (e) => (e ? { left: 0 } : { right: 0 }),
          Wt = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          Vt = (e) => ({ transitionDuration: `${e}ms` }),
          Ut = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: n,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
              className: _,
            }) => {
              const c = i < r,
                d = (0, a.useState)(Pt.Idle),
                m = d[0],
                E = d[1],
                A = m === Pt.End,
                F = m === Pt.Idle,
                p = m === Pt.Grow,
                D = m === Pt.Shrink,
                g = (0, a.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                ),
                C = (0, a.useCallback)(
                  (e, u) =>
                    G(() => {
                      g(e);
                    }, u),
                  [g],
                );
              (0, a.useEffect)(() => {
                if (!t)
                  return F
                    ? C(Pt.Grow, u)
                    : p
                      ? C(Pt.Shrink, e)
                      : D
                        ? C(Pt.End, e)
                        : void (A && o && o());
              }, [C, t, A, p, F, D, o, u, e]);
              const b = (0, a.useMemo)(
                  () => Object.assign({ width: "100%" }, Vt(e), Qt(c)),
                  [c, e],
                ),
                h = (0, a.useMemo)(() => Object.assign({ width: "0%" }, Vt(e), Qt(c)), [c, e]),
                v = (0, a.useMemo)(
                  () => Object.assign({ width: "0%" }, Wt(c, r), Vt(e)),
                  [r, c, e],
                ),
                w = (0, a.useMemo)(
                  () => Object.assign({ width: `${Math.abs(i - r)}%` }, Wt(c, r), Vt(e)),
                  [r, c, i, e],
                );
              if (A) return null;
              const f = B()(kt, _, c && 0 === i && Mt);
              return s().createElement(
                "div",
                { style: F ? v : w, className: f },
                s().createElement(
                  "div",
                  { style: D ? h : b, className: Ht },
                  s().createElement(St, { size: n }),
                ),
              );
            },
          ),
          Gt = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: n,
              isComplete: i,
              animationSettings: o,
              onEndAnimation: l,
              onChangeAnimationState: _,
            }) => {
              const c = e < t,
                d = (0, a.useState)(!1),
                m = d[0],
                E = d[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (e === Pt.Shrink && E(!0), _ && _(e));
                  },
                  [_],
                ),
                F = (0, a.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                p = (0, a.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return s().createElement(
                s().Fragment,
                null,
                s().createElement(Tt, {
                  size: u,
                  lineRef: r,
                  disabled: n,
                  isComplete: i,
                  withoutBounce: c && 0 === e,
                  baseStyles: m ? p : F,
                }),
                t >= 0 &&
                  s().createElement(Ut, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    onChangeAnimationState: A,
                    freezed: o.freezed,
                    onEndAnimation: l,
                    from: t,
                    size: u,
                    to: e,
                    className: o.delta.className,
                  }),
              );
            },
          ),
          qt = ["onComplete", "onEndAnimation"];
        function $t() {
          return (
            ($t =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            $t.apply(this, arguments)
          );
        }
        const jt = (0, a.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              r = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  s = {},
                  r = Object.keys(e);
                for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
                return s;
              })(e, qt);
            const n = (0, a.useState)(!1),
              i = n[0],
              o = n[1],
              l = (0, a.useCallback)(() => {
                const e = 100 === r.to;
                (e !== i && o(e), e && u && u(), t && t());
              }, [i, u, t, r.to]);
            switch (r.animationSettings.type) {
              case vt.Simple:
                return s().createElement(Ot, $t({}, r, { onEndAnimation: l, isComplete: i }));
              case vt.Growing:
                return s().createElement(Gt, $t({}, r, { onEndAnimation: l, isComplete: i }));
              default:
                return null;
            }
          }),
          zt = ["onEndAnimation"];
        function Xt() {
          return (
            (Xt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Xt.apply(this, arguments)
          );
        }
        const Yt = (0, a.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                s = {},
                r = Object.keys(e);
              for (a = 0; a < r.length; a++) ((t = r[a]), u.indexOf(t) >= 0 || (s[t] = e[t]));
              return s;
            })(e, zt);
          const r = (0, a.useRef)({}),
            n = (0, a.useCallback)(() => {
              ((r.current.from = void 0), u && u());
            }, [u]),
            i = "number" == typeof r.current.from ? r.current.from : t.from;
          return (
            (r.current.from = i),
            s().createElement(jt, Xt({}, t, { onEndAnimation: n, key: `${i}-${t.to}`, from: i }))
          );
        });
        function Kt() {
          return (
            (Kt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Kt.apply(this, arguments)
          );
        }
        const Zt = (0, a.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: a,
              deltaFrom: r,
              animationSettings: n,
              onEndAnimation: i,
              onChangeAnimationState: o,
              onComplete: l,
            }) => {
              if (r === u)
                return s().createElement(Lt, {
                  key: `${r}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: a,
                  onComplete: l,
                });
              const _ = {
                from: r,
                to: u,
                size: e,
                lineRef: t,
                disabled: a,
                animationSettings: n,
                onComplete: l,
                onEndAnimation: i,
                onChangeAnimationState: o,
              };
              return n.withStack
                ? s().createElement(Yt, _)
                : s().createElement(jt, Kt({ key: `${r}-${u}` }, _));
            },
          ),
          Jt = (e) => ({
            "--progress-base": `url(${e.bgImageBase})`,
            "--progress-line-base": e.line.bgColorBase,
            "--progress-line-disabled": e.line.bgColorDisabled,
            "--progress-line-finished": e.line.bgColorFinished,
            "--progress-pattern-base": `url(${e.pattern.bgImageBase})`,
            "--progress-pattern-disabled": `url(${e.pattern.bgImageDisabled})`,
            "--progress-pattern-finished": `url(${e.pattern.bgImageFinished})`,
            "--progress-glow": `url('${e.glow}')`,
            "--progress-glow-small": `url('${e.glowSmall}')`,
            "--progress-delta-color": e.delta.color,
            "--progress-delta-shadow": e.delta.shadow,
          }),
          ea = (e, u, t) => (t < e ? e : t > u ? u : t),
          ua = (e, u, t) => {
            if ("number" == typeof t) {
              return (ea(0, u, t) / u) * 100;
            }
            return e;
          },
          ta = {
            bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_grey",
            line: {
              bgColorBase: "#f50",
              bgColorDisabled: "transparent",
              bgColorFinished: "#59a011",
            },
            pattern: {
              bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_orange",
              bgImageDisabled: "R.images.gui.maps.icons.components.progress_bar.pattern_disabled",
              bgImageFinished: "R.images.gui.maps.icons.components.progress_bar.pattern_green",
            },
            glow: "R.images.gui.maps.icons.components.progress_bar.glow",
            glowSmall: "R.images.gui.maps.icons.components.progress_bar.glow_small",
            delta: {
              color: "#ffc",
              shadow:
                "0 0 4px 1px #ffaa0066, 0 0 9px 1px #ffaa0066, 0 0 12px 2px #ff550066, 0 0 12px 4px #ff000066",
            },
          },
          aa = {
            freezed: !1,
            withStack: !1,
            type: vt.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          sa = (0, a.memo)(
            ({
              maxValue: e = 100,
              theme: u = ta,
              size: t = ht.Default,
              animationSettings: r = aa,
              disabled: n = !1,
              withoutBackground: i = !1,
              progressBarBackgroundClassMix: o,
              value: l,
              deltaFrom: _,
              lineRef: c,
              onChangeAnimationState: d,
              onEndAnimation: m,
              onComplete: E,
            }) => {
              const A = ((e, u, t) =>
                (0, a.useMemo)(() => {
                  const a = (ea(0, u, e) / u) * 100;
                  return { value: a, deltaFrom: ua(a, u, t) };
                }, [t, u, e]))(l, e, _);
              return s().createElement(
                "div",
                { className: B()(bt.base, bt[`base__${t}`]), style: Jt(u) },
                !i && s().createElement(wt, { size: t, classMix: o }),
                s().createElement(Zt, {
                  size: t,
                  lineRef: c,
                  disabled: n,
                  value: A.value,
                  deltaFrom: A.deltaFrom,
                  animationSettings: r,
                  onEndAnimation: m,
                  onChangeAnimationState: d,
                  onComplete: E,
                }),
              );
            },
          );
        let ra;
        !(function (e) {
          ((e.Disabled = "disabled"),
            (e.IsAvailable = "isAvailable"),
            (e.CompleteWithHonor = "completeWithHonor"),
            (e.Completed = "completed"));
        })(ra || (ra = {}));
        const na = {
            base: "VehicleTab_base_90",
            bg: "VehicleTab_bg_3f",
            bg__hover: "VehicleTab_bg__hover_54",
            bg__selected: "VehicleTab_bg__selected_bc",
            bg__inProgress: "VehicleTab_bg__inProgress_c7",
            bg__completed: "VehicleTab_bg__completed_8a",
            bg__completeWithHonord: "VehicleTab_bg__completeWithHonord_08",
            bg__completeWithHonor: "VehicleTab_bg__completeWithHonor_a9",
            textWrapper: "VehicleTab_textWrapper_8c",
            vehicleLevel: "VehicleTab_vehicleLevel_5b",
            questsCount: "VehicleTab_questsCount_c9",
            totalQuests: "VehicleTab_totalQuests_cf",
            currentQuests: "VehicleTab_currentQuests_38",
            divider: "VehicleTab_divider_75",
            iconComplete: "VehicleTab_iconComplete_48",
            iconComplete__withHonor: "VehicleTab_iconComplete__withHonor_a4",
          },
          ia = R.strings.personal_missions_3.QuestsView.tab,
          oa = (0, a.memo)(
            ({
              state: e,
              value: u,
              maxValue: t,
              selected: r,
              minVehicleLevel: n,
              maxVehicleLevel: i,
              onSelected: o,
              onTabClicked: l,
              id: _,
              isSwitched: c,
            }) => {
              const d = (0, a.useState)(!1),
                m = d[0],
                E = d[1],
                A = B()(na.bg, na[`bg__${e}`], r && na.bg__selected, m && na.bg__hover),
                F = e === ra.Disabled,
                p = e === ra.Completed || e === ra.CompleteWithHonor;
              return s().createElement(
                "div",
                {
                  className: na.base,
                  onMouseOver: () => {
                    (M(R.sounds.highlight()), E(!0));
                  },
                  onMouseLeave: () => {
                    E(!1);
                  },
                  onClick: () => {
                    c || r || (M(R.sounds.play()), E(!1), l(!0), o(_));
                  },
                },
                s().createElement(
                  "div",
                  { className: A },
                  s().createElement(
                    "div",
                    { className: na.textWrapper },
                    s().createElement(au, {
                      className: na.vehicleLevel,
                      text: ia.progress(),
                      format: { binding: { minVehicleLevel: du(n), maxVehicleLevel: du(i) } },
                    }),
                    p
                      ? s().createElement("div", {
                          className: B()(
                            na.iconComplete,
                            e === ra.CompleteWithHonor && na.iconComplete__withHonor,
                          ),
                        })
                      : s().createElement(
                          "div",
                          { className: na.questsCount },
                          s().createElement(au, { className: na.currentQuests, text: String(u) }),
                          s().createElement(au, { className: na.divider, text: ia.divider() }),
                          s().createElement(au, { className: na.totalQuests, text: String(t) }),
                        ),
                  ),
                  s().createElement(sa, { disabled: F, size: ht.Small, value: u, maxValue: t }),
                ),
              );
            },
          ),
          la = "VehicleTabs_base_f4",
          _a = "VehicleTabs_tab_6e";
        function ca() {
          return (
            (ca =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ca.apply(this, arguments)
          );
        }
        const da = R.strings.personal_missions_3.VehicleTabs.tooltip,
          ma = (0, a.memo)(
            ({ className: e, tabs: u, onSelected: t, onTabClicked: a, isSwitched: r }) =>
              s().createElement(
                "div",
                { className: B()(la, e) },
                u.map((e) =>
                  s().createElement(
                    fu,
                    {
                      key: e.id,
                      header: Oe(da.title(), {
                        minVehicleLevel: du(e.minVehicleLevel),
                        maxVehicleLevel: du(e.maxVehicleLevel),
                      }),
                      body: Oe(da.subtitle(), {
                        minVehicleLevel: du(e.minVehicleLevel),
                        maxVehicleLevel: du(e.maxVehicleLevel),
                      }),
                    },
                    s().createElement(
                      "div",
                      { className: _a },
                      s().createElement(
                        oa,
                        ca({}, e, { onTabClicked: a, onSelected: t, isSwitched: r }),
                      ),
                    ),
                  ),
                ),
              ),
          ),
          Ea = {
            base: "QuestsView_base_be",
            backBtn: "QuestsView_backBtn_32",
            base__hide: "QuestsView_base__hide_f0",
            fadeOut: "QuestsView_fadeOut_1c",
            content: "QuestsView_content_a3",
            content__show: "QuestsView_content__show_a0",
            fadeIn: "QuestsView_fadeIn_1e",
            base__customLarge: "QuestsView_base__customLarge_45",
            content__switched: "QuestsView_content__switched_a3",
            switchedQuests: "QuestsView_switchedQuests_78",
            content__scaled: "QuestsView_content__scaled_33",
            light: "QuestsView_light_a4",
            bottomLight: "QuestsView_bottomLight_e0",
            bottomLight__show: "QuestsView_bottomLight__show_bb",
            lightBlink: "QuestsView_lightBlink_16",
            grid: "QuestsView_grid_b2",
            lightWrapper: "QuestsView_lightWrapper_80",
            quests: "QuestsView_quests_26",
            quests__blinked: "QuestsView_quests__blinked_80",
            character: "QuestsView_character_3a",
            character__scaled: "QuestsView_character__scaled_9c",
            stand: "QuestsView_stand_6f",
            tabs: "QuestsView_tabs_e0",
            header: "QuestsView_header_df",
            translateBottomWithFadeIn: "QuestsView_translateBottomWithFadeIn_18",
            translateTopWithFadeOut: "QuestsView_translateTopWithFadeOut_f8",
            footer: "QuestsView_footer_09",
            translateTopWithFadeIn: "QuestsView_translateTopWithFadeIn_33",
            translateBottomWithFadeOut: "QuestsView_translateBottomWithFadeOut_9b",
            base__scaled: "QuestsView_base__scaled_fa",
            vignette: "QuestsView_vignette_a5",
            translateRightWithFadeIn: "QuestsView_translateRightWithFadeIn_86",
            translateLeftWithFadeOut: "QuestsView_translateLeftWithFadeOut_b5",
            showQuests: "QuestsView_showQuests_f7",
            moveLight: "QuestsView_moveLight_28",
          },
          Aa = (0, q.Pi)(() => {
            const e = re(),
              u = e.controls,
              t = e.model,
              r = z().isCustomLarge,
              i = f().mediaSize,
              o = t.quests.get(),
              l = o.operationName,
              _ = o.prevOperationName,
              c = o.minVehicleLevel,
              d = o.maxVehicleLevel,
              m = o.state,
              E = t.computes.getQuestsLine(),
              A = t.isSwitched.get(),
              F = t.isHideQuests.get(),
              p = t.tabId.get(),
              D = t.computes.getTabs(),
              g = i >= h.Small,
              C = m === ie.Complete || m === ie.CompleteWithHonor,
              b = m === ie.Locked,
              v = `url(R.images.gui.maps.icons.personalMissions3.QuestsView.grid_${p})`,
              w = (0, a.useState)(!0),
              S = w[0],
              x = w[1],
              T = (0, a.useState)(!0),
              L = T[0],
              P = T[1],
              N = D.filter((e) => e.selected)[0].id,
              R = 2 === n.O.view.getScale();
            (me(u.close),
              (0, a.useEffect)(() => {
                u.setTabId(N);
              }, [u, N]),
              (0, a.useEffect)(
                () => (
                  A && x(!1),
                  u.setDecrease(!1),
                  u.setIncrease(!1),
                  () => {
                    (u.setHideQuests(!1), x(!1));
                  }
                ),
                [u, A],
              ),
              (0, a.useEffect)(
                () =>
                  G(() => {
                    u.setIsSwitched(!1);
                  }, 500),
                [u, E],
              ),
              (0, a.useEffect)(() => {
                const e = setInterval(
                  () => {
                    P((e) => !e);
                  },
                  L ? ((u = 2e3), (t = 3e3), Math.floor(u + Math.random() * (t - u + 1))) : 3e4,
                );
                var u, t;
                return () => clearInterval(e);
              }, [L]));
            const y = B()(
                Ea.base,
                F && Ea.base__hide,
                r && Ea.base__customLarge,
                R && Ea.base__scaled,
              ),
              I = B()(Ea.light, r && Ea.light__customLarge),
              O = B()(Ea.character, R && Ea.character__scaled),
              k = B()(
                Ea.content,
                A && Ea.content__switched,
                S && Ea.content__show,
                R && Ea.content__scaled,
              );
            return s().createElement(
              "div",
              { className: y },
              s().createElement(
                "div",
                { className: Ea.header },
                s().createElement(Au, {
                  state: m,
                  operationName: l,
                  prevOperationName: _,
                  minVehicleLevel: c,
                  maxVehicleLevel: d,
                }),
                s().createElement(ma, {
                  tabs: D,
                  className: Ea.tabs,
                  isSwitched: A,
                  onTabClicked: u.setIsSwitched,
                  onSelected: u.switchTab,
                }),
              ),
              s().createElement(
                "div",
                { className: k },
                s().createElement(
                  "div",
                  { className: Ea.lightWrapper },
                  s().createElement("div", { className: I }),
                  s().createElement("div", {
                    className: B()(Ea.bottomLight, L && Ea.bottomLight__show),
                  }),
                  s().createElement("div", { className: Ea.grid, style: { backgroundImage: v } }),
                  s().createElement(gt, {
                    className: Ea.quests,
                    onQuestClicked: u.openQuest,
                    questsLines: E,
                  }),
                ),
              ),
              g && !C && !b && s().createElement(Ae, { className: O, state: m }),
              g && (b || C) && s().createElement(Ct, { state: m, className: Ea.stand }),
              s().createElement(ou, {
                className: B()(Ea.footer, F && Ea.footer__hide),
                onShowRewardClick: u.openRewardOperation,
              }),
            );
          });
        let Fa, pa;
        (!(function (e) {
          ((e.NAPrevious = "previous_progress"),
            (e.NAPreviousAll = "previous_progress_all"),
            (e.NATech = "no_tech"),
            (e.Available = "available"),
            (e.InProgress = "in_progress"),
            (e.InProgressHonor = "in_progress_honor"),
            (e.Pause = "pause"),
            (e.Done = "done"),
            (e.DoneBasic = "done_basic"),
            (e.DoneHonor = "done_honor"),
            (e.DonePause = "done_pause"));
        })(Fa || (Fa = {})),
          (function (e) {
            ((e.Hit = "hit"),
              (e.Kills = "kills"),
              (e.Assist = "assist"),
              (e.Battle = "battle"),
              (e.Master = "master"));
          })(pa || (pa = {})));
        const Da = "ProgressLine_base_48",
          ga = "ProgressLine_conditionProgress_db",
          Ba = "ProgressLine_progressLineProgress_96",
          Ca = "ProgressLine_progressLineIcon_69",
          ba = "ProgressLine_progressLineText_1c",
          ha = "ProgressLine_progressLineText__from_94",
          va = "ProgressLine_iconWrapper_25",
          wa = "ProgressLine_icon_fd",
          fa = "TimeoutProgressBar_base_1c",
          Sa = "TimeoutProgressBar_lineWrapper_fa",
          xa = "TimeoutProgressBar_lineWrapper__red_fc",
          Ta = "TimeoutProgressBar_stepIcon_58",
          La = "TimeoutProgressBar_stepIcon__done_fb",
          Pa = (0, a.memo)(
            ({
              value: e = 0,
              maxValue: u,
              deltaFrom: t = 0,
              isLast: r = !1,
              withSteps: n = !1,
              animationIndex: i = 0,
              failed: o = !1,
            }) => {
              const l = (0, a.useState)(e),
                _ = l[0],
                c = l[1],
                d = (0, a.useState)(t),
                m = d[0],
                E = d[1],
                A = (0, a.useState)(e === u),
                F = A[0],
                p = A[1];
              (0, a.useEffect)(() => {
                if (i && !o) {
                  return G(
                    () => {
                      (c(e), E(t), p(e === u));
                    },
                    1 === i ? 1 : 1300 * (i - 1),
                  );
                }
                (c(e), E(t), p(e === u));
              }, [i, t, o, u, e]);
              return s().createElement(
                "div",
                { className: fa },
                s().createElement(
                  "div",
                  { className: B()(Sa, o && xa) },
                  s().createElement(sa, {
                    size: ht.Small,
                    value: o ? 0 : _,
                    maxValue: u,
                    deltaFrom: o ? 0 : m,
                    disabled: 0 === _ || o,
                    onComplete: () => {
                      p(!0);
                    },
                    withoutBackground: !0,
                  }),
                ),
                !r && n && s().createElement("div", { className: B()(Ta, F && !o && La) }),
              );
            },
          ),
          Na = R.strings.personal_missions_3.QuestView,
          Ra = (0, a.memo)(({ repeatData: e = [], withSteps: u = !1 }) => {
            const t = (0, a.useState)(0),
              r = t[0],
              n = t[1];
            return (
              (0, a.useEffect)(() => {
                const t = u ? 21 : 8,
                  a = 1 === e.length ? 326 : 326 - (t * e.length - 1),
                  s = e.length || 1;
                n(a / s);
              }, [e.length, u]),
              s().createElement(
                "div",
                { className: Da },
                e.map((t, a) =>
                  s().createElement(
                    "div",
                    { key: `repeatProgressLine_${a}` },
                    s().createElement(
                      "div",
                      { className: ga, style: { width: `${r}rem` } },
                      s().createElement(Pa, {
                        value: t.currentValue || 0,
                        maxValue: t.to || 0,
                        deltaFrom: t.previousValue || 0,
                        isLast: a === e.length - 1,
                        withSteps: u,
                        animationIndex: t.animationIndex,
                        failed: t.isFailed,
                      }),
                      t.isOnlyIcon &&
                        s().createElement(
                          "div",
                          { className: va },
                          s().createElement("div", {
                            className: wa,
                            style: { backgroundImage: t.icon },
                          }),
                        ),
                    ),
                    t.icon &&
                      !t.isOnlyIcon &&
                      s().createElement(
                        "div",
                        { className: Ba },
                        s().createElement("div", {
                          className: Ca,
                          style: { backgroundImage: `url('${t.icon}')` },
                        }),
                        s().createElement(au, {
                          className: ba,
                          text: Na.conditionProgress.short(),
                          format: {
                            binding: {
                              from: s().createElement(au, {
                                className: ha,
                                text: String(t.currentValue),
                              }),
                              to: t.to,
                            },
                          },
                        }),
                      ),
                  ),
                ),
              )
            );
          });
        let ya, Ia, Oa;
        (!(function (e) {
          ((e.DEFAULT = "default"),
            (e.MANY = "many"),
            (e.ROW = "row"),
            (e.ANY = "any"),
            (e.LIMITED = "limited"),
            (e.BIATHLON = "biathlon"),
            (e.SERIES = "series"),
            (e.COUNTER = "counter"));
        })(ya || (ya = {})),
          (function (e) {
            ((e.DEFAULT = "default"), (e.DONE = "done"), (e.FAILED = "failed"));
          })(Ia || (Ia = {})),
          (function (e) {
            ((e.PAUSE = "pause"), (e.RESUME = "resume"));
          })(Oa || (Oa = {})));
        const ka = {
          base: "Condition_base_82",
          repeatProgressWrapper: "Condition_repeatProgressWrapper_d8",
          repeatCountWrapper: "Condition_repeatCountWrapper_fb",
          repeatTitleWrapper: "Condition_repeatTitleWrapper_08",
          repeatIcon: "Condition_repeatIcon_49",
          conditionWrapper: "Condition_conditionWrapper_26",
          conditionIcon: "Condition_conditionIcon_4b",
          conditionTitle: "Condition_conditionTitle_97",
          conditionSubTitle: "Condition_conditionSubTitle_28",
          wholeProgressText: "Condition_wholeProgressText_fc",
          wholeProgressText__from: "Condition_wholeProgressText__from_42",
          wholeProgressText__failed: "Condition_wholeProgressText__failed_94",
          wholeProgressText__done: "Condition_wholeProgressText__done_7f",
          divider: "Condition_divider_5b",
          divider__and: "Condition_divider__and_ea",
          separatorOrWrapper: "Condition_separatorOrWrapper_29",
          separatorBlock: "Condition_separatorBlock_3d",
          separatorBlock__left: "Condition_separatorBlock__left_a0",
          separatorBlock__right: "Condition_separatorBlock__right_28",
          separatorArrow: "Condition_separatorArrow_1f",
          separatorText: "Condition_separatorText_e3",
          separatorText__header: "Condition_separatorText__header_b1",
          separatorSoloLine: "Condition_separatorSoloLine_65",
        };
        let Ma;
        !(function (e) {
          ((e.DEFAULT = "default"), (e.FAILED = "failed"), (e.DONE = "done"));
        })(Ma || (Ma = {}));
        const Ha = R.strings.personal_missions_3.QuestView,
          Qa = (e) => _e.Z5.getRealFormat(e, _e.Gr.WO_ZERO_DIGITS),
          Wa = (0, q.Pi)(
            ({
              name: e,
              description: u,
              icon: t,
              headerDescription: r,
              isLast: n,
              biathlonGoal: i,
              progression: o,
            }) => {
              const l = re().model.computes.getDoneFailedCount(o || []),
                _ = (0, a.useState)(0),
                c = _[0],
                d = _[1],
                m = (0, a.useState)(Ma.DEFAULT),
                E = m[0],
                A = m[1],
                F = `R.images.gui.maps.icons.personalMissions3.questTypes.battle_conditions.icon_battle_condition_${t}_128x128`,
                p = i || o.length;
              return (
                (0, a.useEffect)(() => {
                  o &&
                    r &&
                    (d(l.done),
                    A(() => Ma.DEFAULT),
                    l.done === o.length && A(() => Ma.DONE),
                    l.failed === o.length && A(() => Ma.FAILED));
                }, [r, l, l.done, l.failed, o]),
                s().createElement(
                  "div",
                  { className: ka.base },
                  "" !== r
                    ? s().createElement(
                        "div",
                        { className: ka.repeatCountWrapper },
                        s().createElement(
                          "div",
                          { className: ka.repeatTitleWrapper },
                          s().createElement(au, { className: ka.conditionTitle, text: u }),
                          r !== ya.LIMITED &&
                            s().createElement(
                              fu,
                              { body: Ha.repeatTitle.tooltip.$dyn(r) },
                              s().createElement("div", { className: ka.repeatIcon }),
                            ),
                        ),
                        s().createElement(Ra, { repeatData: o, withSteps: r === ya.SERIES }),
                        s().createElement(au, {
                          className: B()(ka.wholeProgressText, ka[`wholeProgressText__${E}`]),
                          text: Ha.repeatProgress.$dyn(E),
                          format: {
                            binding: {
                              from: s().createElement(au, {
                                className: ka.wholeProgressText__from,
                                text: Qa(1 === o.length ? o[0].currentValue : c),
                              }),
                              to: Qa(1 === o.length ? o[0].to : p),
                            },
                          },
                        }),
                      )
                    : s().createElement(
                        "div",
                        { className: B()(ka.conditionWrapper, n && ka.conditionWrapper__last) },
                        s().createElement("div", {
                          className: ka.conditionIcon,
                          style: { backgroundImage: `url('${F}')` },
                        }),
                        s().createElement(
                          "div",
                          null,
                          s().createElement(au, { className: ka.conditionTitle, text: e || "" }),
                          s().createElement(au, { className: ka.conditionSubTitle, text: u || "" }),
                          o &&
                            o.length > 0 &&
                            s().createElement(
                              s().Fragment,
                              null,
                              s().createElement(Ra, { repeatData: o }),
                              1 === o.length &&
                                s().createElement(au, {
                                  className: B()(
                                    ka.wholeProgressText,
                                    o[0].currentValue === o[0].to && ka.wholeProgressText__done,
                                  ),
                                  text: Ha.conditionProgress.full(),
                                  format: {
                                    binding: {
                                      from: s().createElement(au, {
                                        className: B()(
                                          ka.wholeProgressText__from,
                                          o[0].currentValue === o[0].to &&
                                            ka.wholeProgressText__done,
                                        ),
                                        text: Qa(o[0].currentValue),
                                      }),
                                      to: Qa(o[0].to),
                                    },
                                  },
                                }),
                            ),
                        ),
                      ),
                )
              );
            },
          ),
          Va = {
            base: "ConditionsList_base_42",
            base__columns: "ConditionsList_base__columns_23",
            separatorOrWrapper: "ConditionsList_separatorOrWrapper_97",
            separatorBlock: "ConditionsList_separatorBlock_22",
            separatorBlock__right: "ConditionsList_separatorBlock__right_cf",
            separatorLine: "ConditionsList_separatorLine_42",
            separatorArrow: "ConditionsList_separatorArrow_bb",
            separatorText: "ConditionsList_separatorText_6c",
            separatorText__header: "ConditionsList_separatorText__header_b0",
            separatorText__done: "ConditionsList_separatorText__done_18",
            separatorSoloLine: "ConditionsList_separatorSoloLine_90",
          };
        let Ua;
        !(function (e) {
          ((e.And = "and"), (e.Or = "or"));
        })(Ua || (Ua = {}));
        const Ga = (e) =>
            e === Ua.Or
              ? s().createElement(
                  "div",
                  { className: Va.separatorOrWrapper },
                  s().createElement(
                    "div",
                    { className: B()(Va.separatorBlock, Va.separatorBlock__left) },
                    s().createElement("div", { className: Va.separatorLine }),
                  ),
                  s().createElement("div", { className: Va.separatorArrow }),
                  s().createElement(
                    "div",
                    { className: B()(Va.separatorBlock, Va.separatorBlock__right) },
                    s().createElement("div", { className: Va.separatorLine }),
                  ),
                )
              : s().createElement("div", { className: Va.separatorSoloLine }),
          qa = (0, a.memo)(({ quest: e }) =>
            s().createElement(
              "div",
              { className: Va.base },
              e.relation.groups.map((u, t) => {
                const a = u.names;
                return s().createElement(
                  "div",
                  { key: `relationGroup_${t}` },
                  a.map((u, r) =>
                    e.quests
                      .filter((e) => e.idName === u)
                      .map((e) => {
                        const u = !e.headerDescription && e.progression.length > 0;
                        return s().createElement(
                          "div",
                          { key: `relation_${t}__quest_${r}` },
                          s().createElement(Wa, {
                            name: e.name,
                            description: e.description,
                            icon: e.icon,
                            headerDescription: e.headerDescription,
                            isLast: r === a.length - 1,
                            biathlonGoal: e.biathlonGoal,
                            progression: e.progression,
                          }),
                          u && r !== a.length - 1 && Ga(""),
                        );
                      }),
                  ),
                  t !== e.relation.groups.length - 1 && Ga(e.relation.relationType),
                );
              }),
            ),
          );
        let $a, ja, za, Xa, Ya, Ka, Za, Ja, es;
        (!(function (e) {
          ((e.Items = "items"),
            (e.Equipment = "equipment"),
            (e.Xp = "xp"),
            (e.XpFactor = "xpFactor"),
            (e.Blueprints = "blueprints"),
            (e.BlueprintsAny = "blueprintsAny"),
            (e.Goodies = "goodies"),
            (e.Berths = "berths"),
            (e.Slots = "slots"),
            (e.Tokens = "tokens"),
            (e.CrewSkins = "crewSkins"),
            (e.CrewBooks = "crewBooks"),
            (e.Customizations = "customizations"),
            (e.CreditsFactor = "creditsFactor"),
            (e.Currency = "currency"),
            (e.TankmenXp = "tankmenXP"),
            (e.TankmenXpFactor = "tankmenXPFactor"),
            (e.FreeXpFactor = "freeXPFactor"),
            (e.BattleToken = "battleToken"),
            (e.PremiumUniversal = "premium_universal"),
            (e.Gold = "gold"),
            (e.Credits = "credits"),
            (e.Crystal = "crystal"),
            (e.FreeXp = "freeXP"),
            (e.Premium = "premium"),
            (e.PremiumPlus = "premium_plus"),
            (e.BattlePassPoints = "battlePassPoints"),
            (e.BattlePassSelectToken = "battlePassSelectToken"),
            (e.SelectableBonus = "selectableBonus"),
            (e.StyleProgressToken = "styleProgressToken"),
            (e.TmanToken = "tmanToken"),
            (e.NaturalCover = "naturalCover"),
            (e.BpCoin = "bpcoin"),
            (e.BattlaPassFinalAchievement = "dossier_achievement"),
            (e.BattleBadge = "dossier_badge"),
            (e.NewYearAlbumsAccess = "newYearAlbumsAccess"),
            (e.NewYearFillers = "ny22Fillers"),
            (e.NewYearInvoice = "newYearInvoice"),
            (e.NewYearToyFragments = "ny22ToyFragments"),
            (e.NewYearSlot = "newYearSlot"),
            (e.BonusX5 = "battle_bonus_x5"),
            (e.CrewBonusX3 = "crew_bonus_x3"),
            (e.Vehicles = "vehicles"),
            (e.EpicSelectToken = "epicSelectToken"),
            (e.CollectionItem = "collectionItem"),
            (e.Comp7TokenWeeklyReward = "comp7TokenWeeklyReward"),
            (e.Comp7TokenCouponReward = "comp7TokenCouponReward"),
            (e.BattleBoosterGift = "battleBooster_gift"),
            (e.CosmicLootboxSilver = "lootBoxToken"),
            (e.CosmicLootboxCommon = "cosmic_2024_2"),
            (e.Branch = "branch"),
            (e.VehicleSelect = "vehicleSelect"),
            (e.StyleProgress = "styleProgress"),
            (e.ParagonsUnlocks = "paragonsUnlocks"),
            (e.LootBoxToken = "lootBoxToken"),
            (e.PostStamp = "giftsystem_5_stamp"),
            (e.Quests = "quests"),
            (e.ArmoryCoin = "armory_coin"),
            (e.PremiumPlusUniversal = "premium_plus_universal"),
            (e.DogTagType = "dogTagComponents"),
            (e.GoldenTicket = "goldenticket"),
            (e.LbStyleProgress = "lbStyleProgress"),
            (e.RewardsSlots = "rewardsSlots"),
            (e.WtStamp = "stamp"),
            (e.WtHunter = "wt_hunter"),
            (e.WtBoss = "wt_boss"),
            (e.WtHunterCollection = "hunter_collection"),
            (e.WtTicket = "wtevent_ticket"),
            (e.WtMainPrizeDiscount = "main_prize_discount"),
            (e.WtTicket25 = "wtevent_ticket25"));
        })($a || ($a = {})),
          (function (e) {
            ((e.Gold = "gold"),
              (e.Credits = "credits"),
              (e.Crystal = "crystal"),
              (e.Premium = "premium"),
              (e.PremiumPlus = "premium_plus"),
              (e.Vehicles = "vehicles"),
              (e.Customizations = "customizations"),
              (e.Blueprints = "blueprints"),
              (e.BlueprintsAny = "blueprintsAny"),
              (e.BlueprintsFinal = "finalBlueprints"),
              (e.Goodies = "goodies"),
              (e.CrewSkins = "crewSkins"),
              (e.Xp = "xp"),
              (e.XpFactor = "xpFactor"),
              (e.FreeXp = "freeXP"),
              (e.FreeXPFactor = "freeXPFactor"),
              (e.TankmenXP = "tankmenXP"),
              (e.TankmenXPFactor = "tankmenXPFactor"),
              (e.DailyXPFactor = "dailyXPFactor"),
              (e.CreditsFactor = "creditsFactor"),
              (e.Items = "items"),
              (e.StrBonus = "strBonus"),
              (e.Groups = "groups"),
              (e.Berths = "berths"),
              (e.Slots = "slots"),
              (e.Meta = "meta"),
              (e.Tokens = "tokens"),
              (e.Dossier = "dossier"),
              (e.OneOf = "oneof"),
              (e.PremiumUniversal = "premium_universal"),
              (e.BadgesGroup = "badgesGroup"),
              (e.Entitlements = "entitlements"),
              (e.RankedDailyBattles = "rankedDailyBattles"),
              (e.RankedBonusBattles = "rankedBonusBattles"),
              (e.BattlePassPoints = "battlePassPoints"),
              (e.BattleBadge = "dossier_badge"),
              (e.BattleAchievement = "dossier_achievement"));
          })(ja || (ja = {})),
          (function (e) {
            ((e.Big = "big"),
              (e.Small = "small"),
              (e.Mini = "mini"),
              (e.S600x450 = "s600x450"),
              (e.S400x300 = "s400x300"),
              (e.S296x222 = "s296x222"),
              (e.S232x174 = "s232x174"),
              (e.S180x135 = "s180x135"),
              (e.S128x100 = "s128x100"),
              (e.S80x80 = "s80x80"),
              (e.S48x48 = "s48x48"));
          })(za || (za = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(Xa || (Xa = {})),
          (function (e) {
            ((e.BATTLE_BOOSTER = "battleBooster"),
              (e.BATTLE_BOOSTER_REPLACE = "battleBoosterReplace"),
              (e.BUILT_IN_EQUIPMENT = "builtInEquipment"),
              (e.EQUIPMENT_PLUS = "equipmentPlus"),
              (e.EQUIPMENT_TROPHY_BASIC = "equipmentTrophyBasic"),
              (e.EQUIPMENT_TROPHY_UPGRADED = "equipmentTrophyUpgraded"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_1 = "equipmentModernized_1"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_2 = "equipmentModernized_2"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_3 = "equipmentModernized_3"),
              (e.PROGRESSION_STYLE_UPGRADED_1 = "progressionStyleUpgraded_1"),
              (e.PROGRESSION_STYLE_UPGRADED_2 = "progressionStyleUpgraded_2"),
              (e.PROGRESSION_STYLE_UPGRADED_3 = "progressionStyleUpgraded_3"),
              (e.PROGRESSION_STYLE_UPGRADED_4 = "progressionStyleUpgraded_4"));
          })(Ya || (Ya = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(Ka || (Ka = {})),
          (function (e) {
            ((e.BATTLE_BOOSTER = "battleBooster"),
              (e.BATTLE_BOOSTER_REPLACE = "battleBoosterReplace"),
              (e.BUILT_IN_EQUIPMENT = "builtInEquipment"),
              (e.EQUIPMENT_PLUS = "equipmentPlus"),
              (e.EQUIPMENT_TROPHY_BASIC = "equipmentTrophyBasic"),
              (e.EQUIPMENT_TROPHY_UPGRADED = "equipmentTrophyUpgraded"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_1 = "equipmentModernized_1"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_2 = "equipmentModernized_2"),
              (e.EQUIPMENT_MODERNIZED_UPGRADED_3 = "equipmentModernized_3"),
              (e.PROGRESSION_STYLE_UPGRADED_1 = "progressionStyleUpgraded_1"),
              (e.PROGRESSION_STYLE_UPGRADED_2 = "progressionStyleUpgraded_2"),
              (e.PROGRESSION_STYLE_UPGRADED_3 = "progressionStyleUpgraded_3"),
              (e.PROGRESSION_STYLE_UPGRADED_4 = "progressionStyleUpgraded_4"));
          })(Za || (Za = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(Ja || (Ja = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(es || (es = {})));
        class us extends s().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = _e.B3.GOLD;
            else e = _e.B3.INTEGRAL;
            const u = _e.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        us.defaultProps = { format: "integral" };
        const ts = [
            $a.Items,
            $a.Equipment,
            $a.Xp,
            $a.XpFactor,
            $a.Blueprints,
            $a.BlueprintsAny,
            $a.Goodies,
            $a.Berths,
            $a.Slots,
            $a.Tokens,
            $a.CrewSkins,
            $a.CrewBooks,
            $a.Customizations,
            $a.CreditsFactor,
            $a.TankmenXp,
            $a.TankmenXpFactor,
            $a.FreeXpFactor,
            $a.BattleToken,
            $a.PremiumUniversal,
            $a.NaturalCover,
            $a.BpCoin,
            $a.BattlePassSelectToken,
            $a.BattlaPassFinalAchievement,
            $a.BattleBadge,
            $a.BonusX5,
            $a.CrewBonusX3,
            $a.NewYearFillers,
            $a.NewYearInvoice,
            $a.EpicSelectToken,
            $a.Comp7TokenWeeklyReward,
            $a.Comp7TokenCouponReward,
            $a.BattleBoosterGift,
            $a.CosmicLootboxCommon,
            $a.CosmicLootboxSilver,
            $a.SelectableBonus,
            $a.PostStamp,
            $a.PremiumPlusUniversal,
            $a.GoldenTicket,
            $a.RewardsSlots,
            $a.WtStamp,
            $a.WtTicket,
            $a.WtMainPrizeDiscount,
            $a.WtHunter,
            $a.WtHunterCollection,
          ],
          as = [$a.Gold, $a.Credits, $a.Crystal, $a.FreeXp],
          ss = [$a.BattlePassPoints],
          rs = [$a.PremiumPlus, $a.Premium];
        let ns;
        !(function (e) {
          ((e.s16 = "16"),
            (e.s32 = "32"),
            (e.s48 = "48"),
            (e.s66 = "66"),
            (e.s80 = "80"),
            (e.s116 = "116"),
            (e.s296 = "296"),
            (e.s360 = "360"),
            (e.s400 = "400"),
            (e.s600 = "600"));
        })(ns || (ns = {}));
        const is = ["engravings", "backgrounds"],
          os = ["engraving", "background"],
          ls = (e, u = za.Small) => {
            const t = e.name,
              a = e.type,
              s = e.value,
              r = e.icon,
              n = e.item,
              i = e.dogTagType,
              o = ((e) => {
                switch (e) {
                  case za.S600x450:
                    return "c_600x450";
                  case za.S400x300:
                    return "c_400x300";
                  case za.S296x222:
                    return "c_296x222";
                  case za.S232x174:
                    return "c_232x174";
                  case za.Big:
                    return "c_80x80";
                  case za.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (t) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${a}_${s}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${s}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${s}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${r}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case za.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case za.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${r}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const a = is[e];
                  if (a) {
                    const s = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(a),
                      r = s.$dyn(t);
                    return r ? `${r}` : `${s.$dyn(os[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(i, u, r);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${o}.${r}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case za.S600x450:
                      return "c_600x450";
                    case za.S400x300:
                      return "c_400x300";
                    case za.S296x222:
                      return "c_296x222";
                    case za.S232x174:
                      return "c_232x174";
                    case za.S180x135:
                      return "big";
                    case za.Big:
                    case za.S80x80:
                      return "c_80x80";
                    case za.Small:
                    case za.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(u)}.${r}`;
              case "xp":
              case "xpFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.exp`;
              case "creditsFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.credits`;
              case "tankmenXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.tankmenXP`;
              case "dailyXPFactor":
              case "freeXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.freeXP`;
              case "tmanToken":
              case "battlePassSelectToken":
              case "selectableBonus":
              case "groups":
              case "lootBoxToken":
              case "customizations":
              case "crewSkins":
              case "goodies":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${r}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${o}.${r}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case za.Mini:
                      return ns.s32;
                    case za.Small:
                    case za.S48x48:
                      return ns.s48;
                    case za.S80x80:
                    case za.Big:
                      return ns.s80;
                    case za.S128x100:
                      return ns.s116;
                    case za.S180x135:
                    case za.S232x174:
                    case za.S296x222:
                      return ns.s296;
                    case za.S400x300:
                      return ns.s400;
                    case za.S600x450:
                      return ns.s600;
                  }
                })(u)}`;
              case $a.StyleProgress:
              case $a.LbStyleProgress:
                return cs(r, u, es.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}`;
            }
          },
          _s = (e, u, t) => {
            const a = u && { contentId: u };
            return Object.assign(
              {
                args: e,
                isEnabled: Boolean((e && e.tooltipId) || u),
                ignoreMouseClick: !0,
                ignoreShowDelay: !u,
              },
              a,
              t,
            );
          },
          cs = (e, u, t) => {
            const a = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              s = a.$dyn(e);
            return String(null != s ? s : a.$dyn(t));
          };
        function ds() {
          return (
            (ds =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ds.apply(this, arguments)
          );
        }
        const ms = (e) => ("overlayType" in e ? e.overlayType : void 0),
          Es = {
            base: "Reward_base_ea",
            base__s48x48: "Reward_base__s48x48_46",
            base__small: "Reward_base__small_c0",
            base__s80x80: "Reward_base__s80x80_ce",
            base__big: "Reward_base__big_e5",
            base__s128x100: "Reward_base__s128x100_c3",
            base__s180x135: "Reward_base__s180x135_7c",
            base__s232x174: "Reward_base__s232x174_67",
            base__s296x222: "Reward_base__s296x222_78",
            base__s400x300: "Reward_base__s400x300_07",
            base__s600x450: "Reward_base__s600x450_f8",
            tooltipWrapper: "Reward_tooltipWrapper_b5",
            icon: "Reward_icon_df",
            overlay: "Reward_overlay_68",
            highlight: "Reward_highlight_36",
            image: "Reward_image_89",
            info: "Reward_info_72",
            info__multi: "Reward_info__multi_63",
            info__credits: "Reward_info__credits_ef",
            info__gold: "Reward_info__gold_36",
            info__crystal: "Reward_info__crystal_36",
            info__premiumTank: "Reward_info__premiumTank_d3",
            timer: "Reward_timer_d3",
          },
          As = ({
            name: e,
            image: u,
            isPeriodic: t = !1,
            size: a = za.Big,
            special: r,
            value: n,
            valueType: i,
            style: o,
            className: l,
            classNames: _,
            tooltipArgs: c,
            periodicIconTooltipArgs: d,
          }) => {
            const m = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Ya.BATTLE_BOOSTER:
                  case Ya.BATTLE_BOOSTER_REPLACE:
                    return Ka.BATTLE_BOOSTER;
                }
              })(r),
              E = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Ya.BATTLE_BOOSTER:
                    return Za.BATTLE_BOOSTER;
                  case Ya.BATTLE_BOOSTER_REPLACE:
                    return Za.BATTLE_BOOSTER_REPLACE;
                  case Ya.BUILT_IN_EQUIPMENT:
                    return Za.BUILT_IN_EQUIPMENT;
                  case Ya.EQUIPMENT_PLUS:
                    return Za.EQUIPMENT_PLUS;
                  case Ya.EQUIPMENT_TROPHY_BASIC:
                    return Za.EQUIPMENT_TROPHY_BASIC;
                  case Ya.EQUIPMENT_TROPHY_UPGRADED:
                    return Za.EQUIPMENT_TROPHY_UPGRADED;
                  case Ya.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return Za.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case Ya.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return Za.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case Ya.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return Za.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case Ya.PROGRESSION_STYLE_UPGRADED_1:
                    return Za.PROGRESSION_STYLE_UPGRADED_1;
                  case Ya.PROGRESSION_STYLE_UPGRADED_2:
                    return Za.PROGRESSION_STYLE_UPGRADED_2;
                  case Ya.PROGRESSION_STYLE_UPGRADED_3:
                    return Za.PROGRESSION_STYLE_UPGRADED_3;
                  case Ya.PROGRESSION_STYLE_UPGRADED_4:
                    return Za.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(r),
              A = ((e, u) => {
                if (void 0 === e) return null;
                switch (u) {
                  case Xa.MULTI: {
                    const u = Number(e);
                    return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
                  }
                  case Xa.CURRENCY:
                  case Xa.NUMBER:
                    return s().createElement(us, { format: "integral", value: Number(e) });
                  case Xa.PREMIUM_PLUS: {
                    const u = Number(e);
                    return isNaN(u) ? e : null;
                  }
                  default:
                    return e;
                }
              })(n, i);
            return s().createElement(
              "div",
              { className: B()(Es.base, Es[`base__${a}`], l), style: o },
              s().createElement(
                xu,
                { tooltipArgs: c, className: Es.tooltipWrapper },
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement(
                    "div",
                    { className: B()(Es.image, null == _ ? void 0 : _.image) },
                    m &&
                      s().createElement("div", {
                        className: B()(Es.highlight, null == _ ? void 0 : _.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${m}_highlight)`,
                        },
                      }),
                    u &&
                      s().createElement("div", {
                        className: B()(Es.icon, null == _ ? void 0 : _.rewardIcon),
                        style: { backgroundImage: `url(${u})` },
                      }),
                    E &&
                      s().createElement("div", {
                        className: B()(Es.overlay, null == _ ? void 0 : _.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${E}_overlay)`,
                        },
                      }),
                  ),
                  A &&
                    s().createElement(
                      "div",
                      {
                        className: B()(
                          Es.info,
                          Es[`info__${e}`],
                          i === Xa.MULTI && Es.info__multi,
                          null == _ ? void 0 : _.info,
                        ),
                      },
                      A,
                    ),
                ),
              ),
              t &&
                s().createElement(
                  xu,
                  { tooltipArgs: d },
                  s().createElement("div", {
                    className: B()(Es.timer, null == _ ? void 0 : _.periodicIcon),
                  }),
                ),
            );
          },
          Fs = "AnimatedReward_base_8f",
          ps = "AnimatedReward_reward_b0",
          Ds = "AnimatedReward_reward__opacity_74",
          gs = "AnimatedReward_reward__disappear_af",
          Bs = "AnimatedReward_reward__appear_18",
          Cs = "AnimatedReward_reward__moreThanOne_12",
          bs = "AnimatedReward_rewardText_88",
          hs = "AnimatedReward_shine_e2",
          vs = "AnimatedReward_shine__disappear_22",
          ws = "AnimatedReward_shine__appear_53";
        function fs() {
          return (
            (fs =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            fs.apply(this, arguments)
          );
        }
        const Ss = (0, a.memo)(
            ({
              reward: e,
              isWithOpacity: u = !1,
              state: t = !1,
              animationEnd: r,
              isLastReward: n,
              isMoreThanOne: i,
            }) => {
              const o = (0, a.useState)(!1),
                l = o[0],
                _ = o[1],
                c = (0, a.useState)(!1),
                d = c[0],
                m = c[1],
                E = ((e.isChooseReward && t) || e.isShowAnimation || l) && !d;
              (0, a.useEffect)(() => {
                if (e.isShowAnimation)
                  return (
                    l && _(!1),
                    n && i && m(!0),
                    G(() => {
                      (r(), _(!0));
                    }, 1e3)
                  );
              }, [r, e.isShowAnimation, n, i]);
              const A = B()(hs, e.isShowAnimation && !i && vs, l && ws),
                F = B()(ps, e.isShowAnimation && gs, l && Bs, d && Cs, u && !l && Ds);
              return s().createElement(
                "div",
                { className: Fs },
                E && s().createElement("div", { className: A }),
                s().createElement(
                  As,
                  fs({ className: F, classNames: { info: bs } }, e, {
                    image: e.icon
                      ? `R.images.gui.maps.icons.quests.bonuses.big.${e.icon}`
                      : e.image,
                  }),
                ),
              );
            },
          ),
          xs = "ChooseRewardButton_base_aa",
          Ts = "ChooseRewardButton_buttonHolder_45",
          Ls = "ChooseRewardButton_buttonInner_6e",
          Ps = "ChooseRewardButton_button_66",
          Ns = "ChooseRewardButton_buttonBlink_a7",
          Rs = "ChooseRewardButton_buttonText_52",
          ys = R.strings.personal_missions_3.QuestView.content.btn,
          Is = (0, a.memo)(({ onClick: e, className: u }) =>
            s().createElement(
              "div",
              { className: B()(xs, u) },
              s().createElement(
                "div",
                { className: Ts },
                s().createElement(
                  "div",
                  { className: Ls },
                  s().createElement(
                    Be,
                    { type: pe.ghost, size: De.extraSmall, disabled: !1, onClick: e, mixClass: Ps },
                    s().createElement("div", { className: Ns }),
                    s().createElement(au, { className: Rs, text: ys.chooseReward() }),
                  ),
                ),
              ),
            ),
          ),
          Os = "RewardList_base_2c",
          ks = "RewardList_base__withButton_13",
          Ms = "RewardList_rewardWrapper_3e",
          Hs = "RewardList_rewardWrapper__withMargin_b2",
          Qs = "RewardList_rewardWrapper__withChooseReward_93",
          Ws = "RewardList_chooseButton_e0",
          Vs = (0, q.Pi)(({ rewardList: e, state: u, marginBlocker: t }) => {
            const r = ((e, u) => {
                const t = f(),
                  a = u || (t.mediaSize < h.Medium ? za.Small : za.Big);
                return {
                  parsedRewards: ue(e, (e) => {
                    let u = ds({}, e);
                    return Object.assign({}, u, {
                      special: ms(u),
                      image: ls(u, a),
                      size: a,
                      valueType:
                        ((t = u.name),
                        ts.includes(t)
                          ? Xa.MULTI
                          : as.includes(t)
                            ? Xa.CURRENCY
                            : ss.includes(t)
                              ? Xa.NUMBER
                              : rs.includes(t)
                                ? Xa.PREMIUM_PLUS
                                : Xa.STRING),
                      tooltipArgs: _s({
                        tooltipId: u.tooltipId,
                        tooltipContentId: u.tooltipContentId,
                      }),
                    });
                    var t;
                  }),
                  imageSize: a,
                };
              })(e, f().mediaSize < h.Large ? za.Small : za.Big),
              n = r.parsedRewards,
              i = re().controls,
              o = (0, a.useCallback)(
                (e) => () => {
                  i.getSelectionBonus(e);
                },
                [i],
              ),
              l = n.filter((e) => e.isChooseReward).length > 0,
              _ = 1 === n.length,
              c = n.filter((e) => e.isShowAnimation).length > 1;
            return s().createElement(
              "div",
              { className: B()(Os, !t && ks) },
              n.map((e, t) =>
                s().createElement(
                  "div",
                  {
                    className: B()(Ms, t !== n.length - 1 && Hs, (l || _) && Qs),
                    key: `conditionReward_${t}`,
                  },
                  s().createElement(Ss, {
                    reward: e,
                    isWithOpacity: (u && !e.isChooseReward) || c,
                    state: u,
                    animationEnd: i.updateRewards,
                    isLastReward: 3 === t,
                    isMoreThanOne: c,
                  }),
                  e.isChooseReward && s().createElement(Is, { className: Ws, onClick: o(e.id) }),
                ),
              ),
            );
          }),
          Us = (0, a.memo)(Vs),
          Gs = "Content_base_51",
          qs = "Content_headerWrapper_14",
          $s = "Content_infoWrapper_40",
          js = "Content_headerIcon_13",
          zs = "Content_headerSeparator_ae",
          Xs = "Content_headerInfo_4f",
          Ys = "Content_columnsSeparator_25",
          Ks = "Content_conditionBlock_e4",
          Zs = "Content_base__columns_52",
          Js = "Content_separatorText_ad",
          er = "Content_separatorText__header_bf",
          ur = "Content_separatorText__done_e3",
          tr = ["561", "569"],
          ar = R.strings.personal_missions_3.QuestView,
          sr = (0, a.memo)(({ questData: e, classMix: u, questId: t, questState: a }) => {
            const r = e[1].quests.length > 0;
            return s().createElement(
              "div",
              { className: B()(Gs, r && Zs, u) },
              e.map((e, u) => {
                if (e.quests.length < 1) return;
                const n = r && 1 === u,
                  i = n ? ar.questTitle.honor : ar.questTitle,
                  o = e.isDone ? i.tooltip.body.done() : i.tooltip.body.available(),
                  l = e.isDone ? i.done() : i.available(),
                  _ = a === Fa.NAPrevious || a === Fa.NAPreviousAll || a === Fa.NATech;
                return s().createElement(
                  "div",
                  { className: Ks, key: `conditionBlock_${u}` },
                  r &&
                    s().createElement(
                      s().Fragment,
                      null,
                      s().createElement(
                        "div",
                        { className: qs },
                        s().createElement(
                          fu,
                          { header: i.tooltip.header.available() || "", body: o || "" },
                          s().createElement(
                            "div",
                            { className: $s },
                            e.isDone && s().createElement("div", { className: js }),
                            s().createElement(au, {
                              className: B()(Js, er, e.isDone && ur),
                              text: l,
                            }),
                            s().createElement(
                              fu,
                              { body: ar.questTitle.honor.info.tooltip.body() },
                              s().createElement(
                                "div",
                                null,
                                n && !e.isDone && s().createElement("div", { className: Xs }),
                              ),
                            ),
                          ),
                        ),
                        s().createElement("div", { className: zs }),
                      ),
                      0 !== u && s().createElement("div", { className: Ys }),
                    ),
                  s().createElement(qa, { quest: e }),
                  s().createElement(Us, {
                    state: e.isDone || _,
                    rewardList: e.rewards,
                    marginBlocker: -1 !== tr.findIndex((e) => e === t),
                  }),
                );
              }),
            );
          });
        let rr;
        !(function (e) {
          ((e.Enabled = "enabled"), (e.Disabled = "disabled"), (e.Invisible = "invisible"));
        })(rr || (rr = {}));
        const nr = "Footer_base_d1",
          ir = "Footer_button_a2",
          or = "Footer_button__doneBasic_cb",
          lr = "Footer_button__withInfo_37",
          _r = "Footer_infoWrapper_3e",
          cr = "Footer_infoIcon_c9",
          dr = "Footer_infoText_90",
          mr = "Footer_doneText_cd",
          Er = "Footer_progressButtonWrapper_68",
          Ar = "Footer_pauseResetButtons_f5",
          Fr = "Footer_pauseResetButtons__pause_61",
          pr = R.strings.personal_missions_3.QuestView,
          Dr = (0, a.memo)(
            ({
              state: e,
              classMix: u,
              handleApplyQuest: t,
              infoText: a,
              isPauseButtonEnabled: r,
              resetButtonStatus: n,
              handleResetQuest: i,
              handlePauseQuest: o,
            }) => {
              const l = e === Fa.NAPrevious || e === Fa.NAPreviousAll || e === Fa.NATech,
                _ = l || e === Fa.Available || e === Fa.DoneBasic,
                c = (e === Fa.InProgress || e === Fa.InProgressHonor) && !r,
                d = !c && !_ && !r,
                m = e === Fa.Pause || e === Fa.DonePause ? Oa.RESUME : Oa.PAUSE,
                E = B()(ir, c && lr, e === Fa.DoneBasic && or);
              return s().createElement(
                "div",
                { className: B()(nr, u) },
                _ &&
                  s().createElement(
                    fu,
                    {
                      header: pr.acceptButton.tooltip.header.$dyn(e),
                      body: pr.acceptButton.tooltip.body.$dyn(e),
                    },
                    s().createElement(
                      "div",
                      null,
                      s().createElement(
                        Be,
                        { type: pe.primary, size: De.small, mixClass: E, onClick: t, disabled: l },
                        s().createElement(au, {
                          text: pr.acceptButton.$dyn(e) || pr.acceptButton.default(),
                        }),
                      ),
                    ),
                  ),
                r &&
                  s().createElement(
                    "div",
                    { className: Er },
                    s().createElement(
                      fu,
                      { body: pr.pauseButton.tooltip.body.$dyn(m) },
                      s().createElement(
                        "div",
                        null,
                        s().createElement(
                          Be,
                          { type: pe.secondary, size: De.small, mixClass: B()(Ar, Fr), onClick: o },
                          s().createElement(au, { text: pr.pauseButton.name.$dyn(m) }),
                        ),
                      ),
                    ),
                    n !== rr.Invisible &&
                      s().createElement(
                        fu,
                        { body: pr.resetButton.tooltip.body.$dyn(n) },
                        s().createElement(
                          "div",
                          null,
                          s().createElement(
                            Be,
                            {
                              type: pe.primary,
                              size: De.small,
                              mixClass: Ar,
                              onClick: i,
                              disabled: n === rr.Disabled,
                            },
                            s().createElement(au, { text: pr.resetButton.name() }),
                          ),
                        ),
                      ),
                  ),
                c &&
                  s().createElement(
                    "div",
                    { className: _r },
                    s().createElement("div", { className: cr }),
                    s().createElement(au, {
                      className: dr,
                      text: pr.infoText.default(),
                      format: { binding: { value: a } },
                    }),
                  ),
                d && s().createElement(au, { className: mr, text: pr.infoText.done() }),
              );
            },
          ),
          gr = {
            base: "Header_base_70",
            backButton: "Header_backButton_2f",
            pageTitle: "Header_pageTitle_6b",
            mainTitle: "Header_mainTitle_23",
            mainTitleText: "Header_mainTitleText_ad",
            infoIcon: "Header_infoIcon_fe",
            subTitle: "Header_subTitle_2f",
            subTitleIcon: "Header_subTitleIcon_ee",
            base__previous_progress_all: "Header_base__previous_progress_all_ed",
            base__no_tech: "Header_base__no_tech_0b",
            base__previous_progress: "Header_base__previous_progress_b2",
            base__in_progress: "Header_base__in_progress_ba",
            base__in_progress_honor: "Header_base__in_progress_honor_b1",
            base__done: "Header_base__done_c8",
            base__done_basic: "Header_base__done_basic_b8",
            base__done_honor: "Header_base__done_honor_04",
            subTitleText: "Header_subTitleText_53",
          },
          Br = R.strings.personal_missions_3.QuestView,
          Cr = ({ questName: e, questId: u, questState: t, classMix: a, titleValue: r }) => {
            const n = t === Fa.Pause || t === Fa.DonePause,
              i = t !== Fa.Available && !n,
              o = n ? Fa.Pause : t;
            return s().createElement(
              "div",
              { className: B()(gr.base, gr[`base__${o}`]) },
              s().createElement(
                "div",
                { className: B()(gr.pageTitle, a) },
                s().createElement(
                  "div",
                  { className: gr.mainTitle },
                  s().createElement(au, {
                    className: gr.mainTitleText,
                    text: Br.title(),
                    format: { binding: { id: u, name: e } },
                  }),
                  s().createElement(
                    gu,
                    {
                      contentId:
                        R.views.lobby.personal_missions.tooltips.PersonalMissionsQuestInfoTooltip(
                          "resId",
                        ),
                      args: { questId: u },
                    },
                    s().createElement("div", { className: gr.infoIcon }),
                  ),
                ),
                s().createElement(
                  "div",
                  { className: gr.subTitle },
                  i && s().createElement("div", { className: gr.subTitleIcon }),
                  s().createElement(au, {
                    className: gr.subTitleText,
                    text: Br.subtitle.$dyn(o),
                    format: { binding: { value: r } },
                  }),
                ),
              ),
            );
          },
          br = {
            base: "SmallQuestCard_base_a7",
            base__notAvailable: "SmallQuestCard_base__notAvailable_4c",
            base__switch: "SmallQuestCard_base__switch_45",
            base__notReady: "SmallQuestCard_base__notReady_14",
            base__available: "SmallQuestCard_base__available_70",
            base__selected: "SmallQuestCard_base__selected_09",
            base__pause: "SmallQuestCard_base__pause_86",
            base__hover: "SmallQuestCard_base__hover_8a",
            base__doneSwitch: "SmallQuestCard_base__doneSwitch_bf",
            base__inProgress: "SmallQuestCard_base__inProgress_8c",
            base__done: "SmallQuestCard_base__done_04",
            base__doneHonor: "SmallQuestCard_base__doneHonor_75",
            base__donePause: "SmallQuestCard_base__donePause_4f",
            contentWrapper: "SmallQuestCard_contentWrapper_be",
            questID: "SmallQuestCard_questID_d1",
            conditionsWrapper: "SmallQuestCard_conditionsWrapper_16",
            startButton: "SmallQuestCard_startButton_b3",
          };
        let hr;
        !(function (e) {
          ((e.Switch = "switch"),
            (e.NotAvailable = "notAvailable"),
            (e.Available = "available"),
            (e.Pause = "pause"),
            (e.InProgress = "inProgress"),
            (e.DoneS = "doneSwitch"),
            (e.Done = "done"),
            (e.DoneP = "donePause"),
            (e.DoneH = "doneHonor"));
        })(hr || (hr = {}));
        const vr = (0, q.Pi)(
            ({
              questId: e,
              index: u,
              state: t,
              isSelected: r = !1,
              switchQuest: n,
              isAnimated: i,
              setIsAnimated: o,
            }) => {
              const l = (0, a.useState)(!1),
                _ = l[0],
                c = l[1],
                d = B()(
                  br.base,
                  br[`base__${t}`],
                  r && br.base__selected,
                  _ && br.base__hover,
                  i && br.base__notReady,
                ),
                m = t !== hr.Switch && t !== hr.DoneS,
                E = t === hr.DoneS || t === hr.Switch;
              return s().createElement(
                "div",
                {
                  className: d,
                  onMouseEnter: () => {
                    m && (c(!0), M("highlight"));
                  },
                  onMouseLeave: () => {
                    c(!1);
                  },
                  onClick: () => {
                    if (!i && !E)
                      return (
                        o(!0),
                        M("play"),
                        G(() => {
                          n(Number(e));
                        }, 500)
                      );
                  },
                },
                s().createElement(
                  "div",
                  { className: br.contentWrapper },
                  s().createElement(au, { className: br.questID, text: du(u) }),
                ),
              );
            },
          ),
          wr = "QuestsLine_base_23",
          fr = "QuestsLine_cardWrapper_0d",
          Sr = "QuestsLine_cardWrapper__withoutMargin_0b";
        function xr() {
          return (
            (xr =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            xr.apply(this, arguments)
          );
        }
        const Tr = R.strings.personal_missions_3.tooltips.questCard,
          Lr = (0, q.Pi)(({ questsList: e, isAnimated: u, setIsAnimated: t }) => {
            const a = re().controls;
            return s().createElement(
              "div",
              { className: wr },
              e.map((r, n) => {
                return s().createElement(
                  xu,
                  {
                    key: `questCard_${r.questId}`,
                    tooltipArgs:
                      ((i = r),
                      (o = r.questId),
                      i.state === hr.Switch || i.state === hr.DoneS
                        ? {
                            header: Oe(Tr.header.switch(), { questName: i.questName }),
                            body: Tr.body.switch(),
                          }
                        : {
                            contentId:
                              R.views.lobby.personal_missions.tooltips.QuestCardTooltip("resId"),
                            args: { questId: o },
                          }),
                  },
                  s().createElement(
                    "div",
                    { className: B()(fr, n === e.length - 1 && Sr) },
                    s().createElement(
                      vr,
                      xr({}, r, {
                        index: n + 1,
                        switchQuest: a.switchSelected,
                        isAnimated: u,
                        setIsAnimated: t,
                      }),
                    ),
                  ),
                );
                var i, o;
              }),
            );
          }),
          Pr = {
            base: "QuestView_base_f3",
            animated: "QuestView_animated_1c",
            switchCardAnim: "QuestView_switchCardAnim_68",
            baseWrapper: "QuestView_baseWrapper_1c",
            baseWrapper__fadeIn: "QuestView_baseWrapper__fadeIn_e0",
            switchCardAnimIn: "QuestView_switchCardAnimIn_68",
            baseWrapper__fadeOut: "QuestView_baseWrapper__fadeOut_42",
            switchCardAnimOut: "QuestView_switchCardAnimOut_70",
            headerPosition: "QuestView_headerPosition_7e",
            base__customLarge: "QuestView_base__customLarge_39",
            base__scaled: "QuestView_base__scaled_17",
            contentWrapper: "QuestView_contentWrapper_ae",
            arrow: "QuestView_arrow_05",
            arrow__enabled: "QuestView_arrow__enabled_75",
            arrow__left: "QuestView_arrow__left_24",
            arrow__right: "QuestView_arrow__right_76",
            arrow__disabled: "QuestView_arrow__disabled_76",
            arrow__fadeIn: "QuestView_arrow__fadeIn_3f",
            arrow__fadeOut: "QuestView_arrow__fadeOut_b1",
            footerPosition: "QuestView_footerPosition_19",
            questLineWrapper: "QuestView_questLineWrapper_a4",
            lightWrapper: "QuestView_lightWrapper_20",
            lightWrapper__lightOff: "QuestView_lightWrapper__lightOff_fc",
            boardLight: "QuestView_boardLight_35",
            bottomLight: "QuestView_bottomLight_3e",
            bottomLight__blinked: "QuestView_bottomLight__blinked_31",
            lightBlink: "QuestView_lightBlink_52",
            "increaseBoard-extraSmall": "QuestView_increaseBoard-extraSmall_14",
            "increaseBoard-small": "QuestView_increaseBoard-small_3e",
            "increaseBoard-medium": "QuestView_increaseBoard-medium_89",
            "increaseBoard-scaled-medium": "QuestView_increaseBoard-scaled-medium_ec",
            "increaseBoard-scaled-large": "QuestView_increaseBoard-scaled-large_12",
            "increaseBoard-large": "QuestView_increaseBoard-large_b4",
            "increaseBoard-extraLarge": "QuestView_increaseBoard-extraLarge_e1",
            "decreaseBoard-extraSmall": "QuestView_decreaseBoard-extraSmall_d8",
            "decreaseBoard-small": "QuestView_decreaseBoard-small_05",
            "decreaseBoard-medium": "QuestView_decreaseBoard-medium_49",
            "decreaseBoard-scaled-medium": "QuestView_decreaseBoard-scaled-medium_bb",
            "decreaseBoard-scaled-large": "QuestView_decreaseBoard-scaled-large_4d",
            "decreaseBoard-custom-large": "QuestView_decreaseBoard-custom-large_98",
            "increaseBoard-custom-large": "QuestView_increaseBoard-custom-large_90",
            "decreaseBoard-large": "QuestView_decreaseBoard-large_7f",
            "decreaseBoard-extraLarge": "QuestView_decreaseBoard-extraLarge_84",
            "decreaseBoard-custom-extraLarge": "QuestView_decreaseBoard-custom-extraLarge_4c",
            increaseBg: "QuestView_increaseBg_0f",
            decreaseBg: "QuestView_decreaseBg_43",
          },
          Nr = 500,
          Rr = (0, q.Pi)(() => {
            const e = re(),
              u = e.controls,
              t = e.model,
              r = t.quest.get(),
              i = t.isDecrease.get(),
              o = t.computes.getCardList(),
              l = t.computes.getQuestData(),
              _ = (0, a.useState)(!0),
              c = _[0],
              d = _[1],
              m = (0, a.useState)(!1),
              E = m[0],
              A = m[1],
              F = t.isLightVisible.get(),
              p = (() => {
                const e = (0, a.useState)(n.O.view.getScale()),
                  u = e[0],
                  t = e[1];
                return (
                  (0, a.useEffect)(() => {
                    const e = () => {
                      t(n.O.view.getScale());
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
              })(),
              D = z().isCustomLarge,
              g = (0, a.useState)(!0),
              C = g[0],
              b = g[1],
              h = r.state,
              v = r.questData,
              w = v.id,
              f = w === Number(o[0].questId),
              S = w === Number(o[o.length - 1].questId);
            ((0, a.useEffect)(
              () => (
                c && u.setLightVisible(!1),
                G(
                  () => (
                    u.setLightVisible(!0),
                    G(() => {
                      d(!1);
                    }, Nr)
                  ),
                  Nr,
                )
              ),
              [u, c],
            ),
              (0, a.useEffect)(() => {
                const e = setInterval(
                  () => {
                    b((e) => !e);
                  },
                  C ? 2e3 : 15e3,
                );
                return () => clearInterval(e);
              }, [C]));
            const x = (0, a.useCallback)(() => {
              u.applyQuest(w);
            }, [u, w]);
            me(
              (0, a.useCallback)(() => {
                (A(!0), u.setDecrease(!0), u.onBackToOperations());
              }, [u]),
            );
            const T = B()(
                Pr.arrow,
                Pr.arrow__left,
                f ? Pr.arrow__disabled : Pr.arrow__enabled,
                E || i ? Pr.arrow__fadeOut : Pr.arrow__fadeIn,
              ),
              L = B()(
                Pr.arrow,
                Pr.arrow__right,
                S ? Pr.arrow__disabled : Pr.arrow__enabled,
                E || i ? Pr.arrow__fadeOut : Pr.arrow__fadeIn,
              ),
              P = () => {
                M("highlight");
              };
            return s().createElement(
              "div",
              { className: B()(Pr.base, 2 === p && Pr.base__scaled, D && Pr.base__customLarge) },
              s().createElement(
                "div",
                {
                  className: B()(
                    Pr.baseWrapper,
                    E || i ? Pr.baseWrapper__fadeOut : Pr.baseWrapper__fadeIn,
                  ),
                },
                s().createElement(
                  "div",
                  { className: B()(Pr.lightWrapper, !F && Pr.lightWrapper__lightOff) },
                  s().createElement("div", { className: Pr.boardLight }),
                  s().createElement("div", {
                    className: B()(Pr.bottomLight, C && Pr.bottomLight__blinked),
                  }),
                ),
                s().createElement(Cr, {
                  classMix: B()(Pr.headerPosition, c && Pr.animated),
                  questName: v.name,
                  questId: String(w),
                  questState: h,
                  titleValue: r.titleValue,
                }),
                s().createElement(
                  "div",
                  { className: Pr.contentWrapper },
                  s().createElement(sr, {
                    classMix: B()(c && Pr.animated),
                    questData: l,
                    questState: h,
                    questId: String(w),
                  }),
                ),
                s().createElement(Dr, {
                  classMix: B()(
                    Pr.footerPosition,
                    D && Pr.footerPosition__customLarge,
                    c && Pr.animated,
                  ),
                  state: h,
                  handleApplyQuest: x,
                  infoText: r.titleValue,
                  resetButtonStatus: v.resetButtonStatus,
                  isPauseButtonEnabled: v.isPauseButtonEnabled,
                  handleResetQuest: () => u.resetQuest(w),
                  handlePauseQuest: () => u.pauseQuest(w),
                }),
                s().createElement(
                  "div",
                  { className: Pr.questLineWrapper },
                  s().createElement(Lr, { questsList: o, isAnimated: c, setIsAnimated: d }),
                ),
              ),
              s().createElement("div", {
                className: T,
                onClick: () => {
                  if (!c && !f)
                    return (
                      M("play"),
                      d(!0),
                      G(() => {
                        u.prevQuest();
                      }, Nr)
                    );
                },
                onMouseEnter: P,
              }),
              s().createElement("div", {
                className: L,
                onClick: () => {
                  if (!c && !S)
                    return (
                      M("play"),
                      d(!0),
                      G(() => {
                        u.nextQuest();
                      }, Nr)
                    );
                },
                onMouseEnter: P,
              }),
            );
          });
        let yr;
        !(function (e) {
          ((e[(e.QUESTS = 0)] = "QUESTS"), (e[(e.QUEST = 1)] = "QUEST"));
        })(yr || (yr = {}));
        const Ir = { [U.Quests]: Aa, [U.Quest]: Rr },
          Or = ({ viewType: e }) => {
            const u = Ir[e];
            return u
              ? s().createElement(
                  a.Suspense,
                  { fallback: s().createElement("div", null) },
                  s().createElement(u, null),
                )
              : (console.error("Unknown view type for render", e), null);
          },
          kr = (0, q.Pi)(() => {
            const e = re(),
              u = e.controls,
              t = e.model,
              r = t.root.get().pageViewId,
              i = (0, a.useState)(r),
              o = i[0],
              l = i[1],
              _ = z(),
              c = _.isCustomLarge,
              d = _.isCustomSmall,
              m = t.isIncrease.get(),
              E = t.isDecrease.get(),
              A = r === U.Quest,
              F = 2 === n.O.view.getScale();
            var p, D;
            ((p = () => {
              (u.setIncrease(!1), u.setDecrease(!1));
            }),
              (D = []),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("resize", p),
                  () => window.removeEventListener("resize", p)
                ),
                D,
              ),
              (0, a.useEffect)(() => {
                if (E)
                  return G(() => {
                    l(r);
                  }, 1e3);
                l(r);
              }, [E, r]));
            const g = B()(
                ne.base,
                F && ne.base__scaled,
                d && ne.base__customSmall,
                c && ne.base__customLarge,
              ),
              C = B()(
                ne.board,
                m && ne.board__increase,
                E && ne.board__decrease,
                A && ne.board__quest,
              ),
              b = B()(
                ne.bg,
                c && ne.bg__customLarge,
                d && ne.bg__customSmall,
                m && ne.bg__increase,
                E && ne.bg__decrease,
              ),
              h = R.strings.personal_missions_3.QuestsView,
              v = R.strings.personal_missions_3.QuestView;
            return s().createElement(
              "div",
              { className: g },
              s().createElement(
                "div",
                { className: ne.baseWrapper },
                s().createElement(
                  "div",
                  { className: ne.headerBtn },
                  s().createElement(V, {
                    caption: A ? v.backButton.backText() : h.backButton.caption(),
                    goto: A ? v.backButton.to() : h.backButton.to(),
                    type: "back",
                    onClick: A
                      ? () => {
                          (u.setDecrease(!0), u.onBackToOperations());
                        }
                      : u.close,
                  }),
                ),
                s().createElement("div", { className: b }),
                s().createElement("div", { className: ne.vignette }),
                s().createElement("div", { className: C }),
                s().createElement(
                  "div",
                  { className: ne.content },
                  s().createElement(Or, { viewType: o }),
                ),
              ),
            );
          });
        engine.whenReady.then(() => {
          k().render(
            s().createElement(se, null, s().createElement(I, null, s().createElement(kr, null))),
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
    (__webpack_require__.O = (e, u, t, a) => {
      if (!u) {
        var s = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [u, t, a] = deferred[o], r = !0, n = 0; n < u.length; n++)
            (!1 & a || s >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[n]))
              ? u.splice(n--, 1)
              : ((r = !1), a < s && (s = a));
          if (r) {
            deferred.splice(o--, 1);
            var i = t();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      a = a || 0;
      for (var o = deferred.length; o > 0 && deferred[o - 1][2] > a; o--)
        deferred[o] = deferred[o - 1];
      deferred[o] = [u, t, a];
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
    (__webpack_require__.j = 451),
    (() => {
      var e = { 451: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var a,
            s,
            [r, n, i] = t,
            o = 0;
          if (r.some((u) => 0 !== e[u])) {
            for (a in n) __webpack_require__.o(n, a) && (__webpack_require__.m[a] = n[a]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); o < r.length; o++)
            ((s = r[o]), __webpack_require__.o(e, s) && e[s] && e[s][0](), (e[s] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [650], () => __webpack_require__(877));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
