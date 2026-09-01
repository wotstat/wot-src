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
        (t.r(u), t.d(u, { mouse: () => i, onResize: () => n }));
        var a = t(472),
          r = t(176);
        const n = (0, a.E)("clientResized"),
          s = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function u() {
            e.enabled && (0, r.R)(!1);
          }
          function t() {
            e.enabled && (0, r.R)(!0);
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
              : (0, r.R)(!1);
          }
          const n = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let r = !0;
                  const n = `mouse${u}`,
                    i = s[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(n, o),
                    a(),
                    () => {
                      r &&
                        (i(), window.removeEventListener(n, o), (e.listeners -= 1), a(), (r = !1));
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
              ((e.enabled = !1), a());
            },
            enable() {
              ((e.enabled = !0), a());
            },
            enableOutside() {
              e.enabled && (0, r.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, r.R)(!1);
            },
          });
        })();
      },
      959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => a,
            getMouseGlobalPosition: () => n,
            getSize: () => r,
            graphicsQuality: () => s,
          }));
        var a = t(527);
        function r(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function n(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const s = {
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
        t.d(u, { O: () => r });
        var a = t(959);
        const r = { view: t(641), client: a };
      },
      722: (e, u, t) => {
        "use strict";
        function a(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function r(e, u, t) {
          return `url(${a(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => r, getTextureUrl: () => a }));
      },
      112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => r });
        var a = t(472);
        const r = {
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
            addModelObserver: () => E,
            addPreloadTexture: () => i,
            children: () => a,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => n.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => F,
            getSize: () => _,
            getViewGlobalPosition: () => d,
            isClientAccessible: () => p,
            isEventHandled: () => b,
            isFocused: () => g,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => m,
            sendEvent: () => s.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => h,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => c,
            whenTutorialReady: () => x,
          }));
        var a = t(722),
          r = t(112),
          n = t(538),
          s = t(566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, u, t, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, a);
        }
        function E(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function c(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function _(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function d(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: B(u.x), y: B(u.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function F() {
          return viewEnv.getScale();
        }
        function D(e) {
          return viewEnv.pxToRem(e);
        }
        function B(e) {
          return viewEnv.remToPx(e);
        }
        function C(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function g() {
          return viewEnv.isFocused();
        }
        function p() {
          return viewEnv.isClientAccessible();
        }
        function h() {
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
        const w = Object.keys(r.W).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === r.W[u]), e),
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
              window.isDomBuilt ? e() : n.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => l });
        const a = ["args"];
        const r = 2,
          n = 16,
          s = 32,
          i = 64,
          o = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                s = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    r = {},
                    n = Object.keys(e);
                  for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, a);
              return void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, s, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, s));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var r;
          },
          l = {
            close(e) {
              o("popover" === e ? r : s);
            },
            minimize() {
              o(i);
            },
            move(e) {
              o(n, { isMouseEvent: !0, on: e });
            },
          };
      },
      521: (e, u, t) => {
        "use strict";
        let a, r;
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
          })(r || (r = {})));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        var a = t(138);
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
            const n = a.O.view.addModelObserver(e, t, r);
            return (
              n > 0
                ? ((this._callbacks[n] = u),
                  t > 0 && (this._views[t] ? this._views[t].push(n) : (this._views[t] = [n])))
                : console.error("Can't add callback for model:", e),
              n
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
        r.__instance = void 0;
        const n = r;
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
        t.d(u, { B3: () => l, Z5: () => s, B0: () => o, ry: () => B });
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
        const r = a;
        var n = t(358);
        const s = {
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
          E = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          c = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = t(521),
          d = t(138);
        const A = ["args"];
        function F(e, u, t, a, r, n, s) {
          try {
            var i = e[n](s),
              o = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(o) : Promise.resolve(o).then(a, r);
        }
        const D = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          B = (function () {
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
                  return new Promise(function (a, r) {
                    var n = e.apply(u, t);
                    function s(e) {
                      F(n, a, r, s, i, "next", e);
                    }
                    function i(e) {
                      F(n, a, r, s, i, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          C = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const r = u.args,
                n = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    r = {},
                    n = Object.keys(e);
                  for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(u, A);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, n, {
                      arguments:
                        ((a = r),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, n));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var a;
          },
          g = () => C(o.CLOSE),
          p = (e, u) => {
            e.keyCode === m.n.ESCAPE && u();
          };
        var h = t(572);
        const b = r.instance,
          v = {
            DataTracker: n.Z,
            ViewModel: h.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: E,
            TimeFormatType: c,
            DateFormatType: _,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (e) => C(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: g,
            sendClosePopOverEvent: () => C(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              C(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, a, r = R.invalid("resId"), n) => {
              const s = d.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                l = i.x,
                E = i.y,
                c = i.width,
                _ = i.height,
                m = {
                  x: d.O.view.pxToRem(l) + s.x,
                  y: d.O.view.pxToRem(E) + s.y,
                  width: d.O.view.pxToRem(c),
                  height: d.O.view.pxToRem(_),
                };
              C(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: a || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: D(m),
                on: !0,
                args: n,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => p(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              p(e, g);
            },
            handleViewEvent: C,
            onBindingsReady: B,
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
                  const r = Object.prototype.toString.call(u[a]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = u[a];
                    t[a] = [];
                    for (let u = 0; u < r.length; u++) t[a].push({ value: e(r[u].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[a] = e(u[a]))
                      : (t[a] = u[a]);
                }
              return t;
            },
            ClickOutsideManager: b,
            SystemLocale: s,
            UserLocale: i,
          };
        window.ViewEnvHelper = v;
      },
      512: (e, u, t) => {
        "use strict";
        var a = t(179),
          r = t.n(a);
        const n = (e, u, t) =>
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
        var s = t(138);
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
            n = Math.min(a, r);
          return {
            extraLarge: n === t.extraLarge.weight,
            large: n === t.large.weight,
            medium: n === t.medium.weight,
            small: n === t.small.weight,
            extraSmall: n === t.extraSmall.weight,
            extraLargeWidth: a === t.extraLarge.weight,
            largeWidth: a === t.large.weight,
            mediumWidth: a === t.medium.weight,
            smallWidth: a === t.small.weight,
            extraSmallWidth: a === t.extraSmall.weight,
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
        })(o || (o = {}));
        const E = s.O.client.getSize("rem"),
          c = E.width,
          _ = E.height,
          m = Object.assign({ width: c, height: _ }, l(c, _, i)),
          d = (0, a.createContext)(m),
          A = ["children"];
        const F = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, A);
          const r = (0, a.useContext)(d),
            s = r.extraLarge,
            i = r.large,
            o = r.medium,
            l = r.small,
            E = r.extraSmall,
            c = r.extraLargeWidth,
            _ = r.largeWidth,
            m = r.mediumWidth,
            F = r.smallWidth,
            D = r.extraSmallWidth,
            B = r.extraLargeHeight,
            C = r.largeHeight,
            g = r.mediumHeight,
            p = r.smallHeight,
            h = r.extraSmallHeight,
            b = { extraLarge: B, large: C, medium: g, small: p, extraSmall: h };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && s) return u;
            if (t.large && i) return u;
            if (t.medium && o) return u;
            if (t.small && l) return u;
            if (t.extraSmall && E) return u;
          } else {
            if (t.extraLargeWidth && c) return n(u, t, b);
            if (t.largeWidth && _) return n(u, t, b);
            if (t.mediumWidth && m) return n(u, t, b);
            if (t.smallWidth && F) return n(u, t, b);
            if (t.extraSmallWidth && D) return n(u, t, b);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && B) return u;
              if (t.largeHeight && C) return u;
              if (t.mediumHeight && g) return u;
              if (t.smallHeight && p) return u;
              if (t.extraSmallHeight && h) return u;
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
        const D = (e) => {
            const u = (0, a.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          B = (0, a.memo)(({ children: e }) => {
            const u = (0, a.useContext)(d),
              t = (0, a.useState)(u),
              n = t[0],
              o = t[1],
              E = (0, a.useCallback)((e, u) => {
                const t = s.O.view.pxToRem(e),
                  a = s.O.view.pxToRem(u);
                o(Object.assign({ width: t, height: a }, l(t, a, i)));
              }, []);
            (D(() => {
              engine.on("clientResized", E);
            }),
              (0, a.useEffect)(() => () => engine.off("clientResized", E), [E]));
            const c = (0, a.useMemo)(() => Object.assign({}, n), [n]);
            return r().createElement(d.Provider, { value: c }, e);
          });
        var C = t(483),
          g = t.n(C),
          p = t(926),
          h = t.n(p);
        let b, v, f;
        (!(function (e) {
          ((e[(e.ExtraSmall = i.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = i.small.width)] = "Small"),
            (e[(e.Medium = i.medium.width)] = "Medium"),
            (e[(e.Large = i.large.width)] = "Large"),
            (e[(e.ExtraLarge = i.extraLarge.width)] = "ExtraLarge"));
        })(b || (b = {})),
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
          })(f || (f = {})));
        const w = () => {
            const e = (0, a.useContext)(d),
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
              s = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return f.ExtraLarge;
                  case e.largeHeight:
                    return f.Large;
                  case e.mediumHeight:
                    return f.Medium;
                  case e.smallHeight:
                    return f.Small;
                  case e.extraSmallHeight:
                    return f.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), f.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: r,
              mediaWidth: n,
              mediaHeight: s,
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
            [v.Small]: h().SMALL_WIDTH,
            [v.Medium]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH}`,
            [v.Large]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH}`,
            [v.ExtraLarge]: `${h().SMALL_WIDTH} ${h().MEDIUM_WIDTH} ${h().LARGE_WIDTH} ${h().EXTRA_LARGE_WIDTH}`,
          },
          M = {
            [f.ExtraSmall]: "",
            [f.Small]: h().SMALL_HEIGHT,
            [f.Medium]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT}`,
            [f.Large]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT}`,
            [f.ExtraLarge]: `${h().SMALL_HEIGHT} ${h().MEDIUM_HEIGHT} ${h().LARGE_HEIGHT} ${h().EXTRA_LARGE_HEIGHT}`,
          },
          y = {
            [b.ExtraSmall]: "",
            [b.Small]: h().SMALL,
            [b.Medium]: `${h().SMALL} ${h().MEDIUM}`,
            [b.Large]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE}`,
            [b.ExtraLarge]: `${h().SMALL} ${h().MEDIUM} ${h().LARGE} ${h().EXTRA_LARGE}`,
          },
          P = (e) => {
            let u = e.children,
              t = e.className,
              a = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, S);
            const n = w(),
              s = n.mediaWidth,
              i = n.mediaHeight,
              o = n.mediaSize;
            return r().createElement("div", x({ className: g()(t, T[s], M[i], y[o]) }, a), u);
          },
          L = ["children"];
        const O = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, L);
          return r().createElement(B, null, r().createElement(P, t, u));
        };
        var N = t(493),
          k = t.n(N);
        function I(e) {
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
          U = [
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
        function G() {
          return (
            (G =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            G.apply(this, arguments)
          );
        }
        class W extends r().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && I(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && I(this.props.soundClick));
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
              n = e.side,
              s = e.type,
              i = e.classNames,
              o = e.onMouseEnter,
              l = e.onMouseLeave,
              E = e.onMouseDown,
              c = e.onMouseUp,
              _ =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    a,
                    r = {},
                    n = Object.keys(e);
                  for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                  return r;
                })(e, U)),
              m = g()(H.base, H[`base__${s}`], H[`base__${n}`], null == i ? void 0 : i.base),
              d = g()(H.icon, H[`icon__${s}`], H[`icon__${n}`], null == i ? void 0 : i.icon),
              A = g()(H.glow, null == i ? void 0 : i.glow),
              F = g()(H.caption, H[`caption__${s}`], null == i ? void 0 : i.caption),
              D = g()(H.goto, null == i ? void 0 : i.goto);
            return r().createElement(
              "div",
              G(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(E),
                  onMouseUp: this._onMouseUp(c),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                _,
              ),
              "info" !== s && r().createElement("div", { className: H.shine }),
              r().createElement(
                "div",
                { className: d },
                r().createElement("div", { className: A }),
              ),
              r().createElement("div", { className: F }, u),
              a && r().createElement("div", { className: D }, a),
            );
          }
        }
        W.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var $ = t(521),
          q = t(364);
        const j = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function X(e = $.n.NONE, u = j, t = !1) {
          (0, a.useEffect)(() => {
            if (e !== $.n.NONE)
              return (
                window.addEventListener("keydown", a, t),
                () => {
                  window.removeEventListener("keydown", a, t);
                }
              );
            function a(a) {
              if (a.keyCode === e) {
                if (s.O.view.isEventHandled()) return;
                (s.O.view.setEventHandled(), u(a), t && a.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        var z = t(515);
        const Y = {
          base: "Character_base_65",
          bg: "Character_bg_87",
          bg__complete: "Character_bg__complete_28",
          bg__completeAdd: "Character_bg__completeAdd_17",
          bg__completeWithHonor: "Character_bg__completeWithHonor_ab",
          bg__active: "Character_bg__active_4c",
        };
        let V, Q;
        (!(function (e) {
          ((e[(e.W_1024 = 1024)] = "W_1024"),
            (e[(e.W_1280 = 1280)] = "W_1280"),
            (e[(e.W_2000 = 2e3)] = "W_2000"),
            (e[(e.W_2200 = 2200)] = "W_2200"),
            (e[(e.W_2560 = 2560)] = "W_2560"));
        })(V || (V = {})),
          (function (e) {
            e[(e.H_1200 = 1200)] = "H_1200";
          })(Q || (Q = {})));
        const K = (0, a.memo)(({ className: e, state: u }) => {
          const t = (() => {
              const e = w(),
                u = e.remScreenWidth,
                t = e.remScreenHeight;
              return {
                isCustomSmall: u > V.W_1024 && u <= V.W_1280,
                isCustomLarge: u > V.W_2000 && u <= V.W_2560 && t > Q.H_1200,
              };
            })().isCustomLarge,
            a = g()(Y.base, t && Y.base__custom, e),
            n = g()(Y.bg, Y[`bg__${u}`]);
          return r().createElement(
            "div",
            { className: a },
            r().createElement("div", { className: n }),
          );
        });
        function Z(e) {
          return e;
        }
        function J() {
          return !1;
        }
        console.log;
        var ee = t(174);
        function ue(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return te(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return te(e, u);
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
        function te(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, a = new Array(u); t < u; t++) a[t] = e[t];
          return a;
        }
        const ae = (e) => (0 === e ? window : window.subViews.get(e));
        function re(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, a) => u(null == e ? void 0 : e.value, t, a));
        }
        var ne = t(946);
        const se = ((e, u) => {
            const t = (0, a.createContext)({});
            return [
              function ({ mode: n = "real", options: i, children: o, mocks: l }) {
                const E = (0, a.useRef)([]),
                  c = (t, a, r) => {
                    var n;
                    const i = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = ae,
                        context: a = "model",
                      } = {}) {
                        const r = new Map();
                        function n(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? r.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = r.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const i = (e) => {
                          const r = t(u),
                            n = a.split(".").reduce((e, u) => e[u], r);
                          return "string" != typeof e || 0 === e.length
                            ? n
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, n);
                        };
                        return {
                          subscribe: (t, n) => {
                            const o = "string" == typeof n ? `${a}.${n}` : a,
                              l = s.O.view.addModelObserver(o, u, !0);
                            return (r.set(l, t), e && t(i(n)), l);
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
                            for (var e, t = ue(r.keys()); !(e = t()).done;) n(e.value, u);
                          },
                          unsubscribe: n,
                        };
                      })(a),
                      o =
                        "real" === t
                          ? i
                          : Object.assign({}, i, {
                              readByPath:
                                null != (n = null == r ? void 0 : r.getter) ? n : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == r ? void 0 : r.getter(e)) : o.readByPath(e),
                      c = (e) => E.current.push(e),
                      _ = e({
                        mode: t,
                        readByPath: l,
                        externalModel: o,
                        observableModel: {
                          array: (e, u) => {
                            const a = null != u ? u : l(e),
                              r = ee.LO.box(a, { equals: J });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, ee.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, u) => {
                            const a = null != u ? u : l(e),
                              r = ee.LO.box(a, { equals: J });
                            return (
                              "real" === t &&
                                o.subscribe(
                                  (0, ee.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, u) => {
                            const a = l(u);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, u) => ((e[u] = ee.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, ee.aD)((u) => {
                                      e.forEach((e) => {
                                        r[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                r
                              );
                            }
                            {
                              const r = e,
                                n = Object.entries(r),
                                s = n.reduce((e, [u, t]) => ((e[t] = ee.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  o.subscribe(
                                    (0, ee.aD)((e) => {
                                      n.forEach(([u, t]) => {
                                        s[t].set(e[u]);
                                      });
                                    }),
                                    u,
                                  ),
                                s
                              );
                            }
                          },
                        },
                        cleanup: c,
                      }),
                      m = { mode: t, model: _, externalModel: o, cleanup: c };
                    return {
                      model: _,
                      controls: "mocks" === t && r ? r.controls(m) : u(m),
                      externalModel: o,
                      mode: t,
                    };
                  },
                  _ = (0, a.useRef)(!1),
                  m = (0, a.useState)(n),
                  d = m[0],
                  A = m[1],
                  F = (0, a.useState)(() => c(n, i, l)),
                  D = F[0],
                  B = F[1];
                return (
                  (0, a.useEffect)(() => {
                    _.current ? B(c(d, i, l)) : (_.current = !0);
                  }, [l, d, i]),
                  (0, a.useEffect)(() => {
                    A(n);
                  }, [n]),
                  (0, a.useEffect)(
                    () => () => {
                      (D.externalModel.dispose(), E.current.forEach((e) => e()));
                    },
                    [D],
                  ),
                  r().createElement(t.Provider, { value: D }, o)
                );
              },
              () => (0, a.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  questModel: e.object("questModel"),
                  rewards: e.array("rewards"),
                  mainRewards: e.object("questModel.mainQuests.rewards"),
                  addRewards: e.object("questModel.addQuests.rewards"),
                },
                t = (e) => re(e, (e) => Object.assign({}, e)),
                a = (e) => ({
                  isDone: e.isDone,
                  quests: re(e.quests, (e) =>
                    Object.assign({}, e, { progression: t(e.progression) }),
                  ),
                  rewards: t(e.rewards),
                  relation: Object.assign({}, e.relation, {
                    groups: re(e.relation.groups, (e) => {
                      return { names: ((u = e.names), re(u, Z)) };
                      var u;
                    }),
                  }),
                }),
                r = (0, ne.Om)(() => a(u.questModel.get().mainQuests), { equals: J }),
                n = (0, ne.Om)(() => a(u.questModel.get().addQuests), { equals: J }),
                s = (0, ne.Om)(() => t(u.mainRewards.get()), { equals: J }),
                i = (0, ne.Om)(() => t(u.addRewards.get()), { equals: J }),
                o = (0, ne.Om)(() => t(u.rewards.get()), { equals: J });
              return Object.assign({}, u, {
                computes: {
                  getQuestData: () => [r(), n()],
                  getMainRewards: s,
                  getAdditionalRewards: i,
                  getSelectedRewards: o,
                },
              });
            },
            ({ externalModel: e }) => ({
              close: e.createCallbackNoArgs("onClose"),
              openQuest: e.createCallback((e) => ({ id: e }), "onOpenQuest"),
              onChooseReward: e.createCallback((e) => ({ id: e }), "onChooseReward"),
            }),
          ),
          ie = se[0],
          oe = se[1];
        let le, Ee, ce, _e, me, de, Ae, Fe, De, Be, Ce;
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
            (e.RewardsSlots = "rewardsSlots"));
        })(le || (le = {})),
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
          })(Ee || (Ee = {})),
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
          })(ce || (ce = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(_e || (_e = {})),
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
          })(me || (me = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(de || (de = {})),
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
          })(Ae || (Ae = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(Fe || (Fe = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(De || (De = {})),
          (function (e) {
            ((e.COMPLETE = "complete"),
              (e.COMPLETE_WITH_HONOR = "completeWithHonor"),
              (e.COMPLETE_ADD = "completeAdd"),
              (e.COMPLETE_BASIC = "completeBasic"));
          })(Be || (Be = {})),
          (function (e) {
            ((e.Hit = "hit"),
              (e.Kills = "kills"),
              (e.Assist = "assist"),
              (e.Battle = "battle"),
              (e.Master = "master"));
          })(Ce || (Ce = {})));
        class ge extends r().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = q.B3.GOLD;
            else e = q.B3.INTEGRAL;
            const u = q.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        ge.defaultProps = { format: "integral" };
        const pe = [
            le.Items,
            le.Equipment,
            le.Xp,
            le.XpFactor,
            le.Blueprints,
            le.BlueprintsAny,
            le.Goodies,
            le.Berths,
            le.Slots,
            le.Tokens,
            le.CrewSkins,
            le.CrewBooks,
            le.Customizations,
            le.CreditsFactor,
            le.TankmenXp,
            le.TankmenXpFactor,
            le.FreeXpFactor,
            le.BattleToken,
            le.PremiumUniversal,
            le.NaturalCover,
            le.BpCoin,
            le.BattlePassSelectToken,
            le.BattlaPassFinalAchievement,
            le.BattleBadge,
            le.BonusX5,
            le.CrewBonusX3,
            le.NewYearFillers,
            le.NewYearInvoice,
            le.EpicSelectToken,
            le.Comp7TokenWeeklyReward,
            le.Comp7TokenCouponReward,
            le.BattleBoosterGift,
            le.CosmicLootboxCommon,
            le.CosmicLootboxSilver,
            le.SelectableBonus,
            le.PostStamp,
            le.PremiumPlusUniversal,
            le.GoldenTicket,
            le.RewardsSlots,
          ],
          he = [le.Gold, le.Credits, le.Crystal, le.FreeXp],
          be = [le.BattlePassPoints],
          ve = [le.PremiumPlus, le.Premium];
        let fe;
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
        })(fe || (fe = {}));
        const we = ["engravings", "backgrounds"],
          Se = ["engraving", "background"],
          xe = (e, u = ce.Small) => {
            const t = e.name,
              a = e.type,
              r = e.value,
              n = e.icon,
              s = e.item,
              i = e.dogTagType,
              o = ((e) => {
                switch (e) {
                  case ce.S600x450:
                    return "c_600x450";
                  case ce.S400x300:
                    return "c_400x300";
                  case ce.S296x222:
                    return "c_296x222";
                  case ce.S232x174:
                    return "c_232x174";
                  case ce.Big:
                    return "c_80x80";
                  case ce.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (t) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${a}_${r}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_plus_${r}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}_${r}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${s}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${n}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case ce.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case ce.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${n}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const a = we[e];
                  if (a) {
                    const r = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(a),
                      n = r.$dyn(t);
                    return n ? `${n}` : `${r.$dyn(Se[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(i, u, n);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${o}.${n}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case ce.S600x450:
                      return "c_600x450";
                    case ce.S400x300:
                      return "c_400x300";
                    case ce.S296x222:
                      return "c_296x222";
                    case ce.S232x174:
                      return "c_232x174";
                    case ce.S180x135:
                      return "big";
                    case ce.Big:
                    case ce.S80x80:
                      return "c_80x80";
                    case ce.Small:
                    case ce.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(u)}.${n}`;
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
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${o}.${n}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case ce.Mini:
                      return fe.s32;
                    case ce.Small:
                    case ce.S48x48:
                      return fe.s48;
                    case ce.S80x80:
                    case ce.Big:
                      return fe.s80;
                    case ce.S128x100:
                      return fe.s116;
                    case ce.S180x135:
                    case ce.S232x174:
                    case ce.S296x222:
                      return fe.s296;
                    case ce.S400x300:
                      return fe.s400;
                    case ce.S600x450:
                      return fe.s600;
                  }
                })(u)}`;
              case le.StyleProgress:
              case le.LbStyleProgress:
                return Te(n, u, De.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${t}`;
            }
          },
          Re = (e, u, t) => {
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
          Te = (e, u, t) => {
            const a = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              r = a.$dyn(e);
            return String(null != r ? r : a.$dyn(t));
          };
        function Me() {
          return (
            (Me =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Me.apply(this, arguments)
          );
        }
        const ye = (e) => ("overlayType" in e ? e.overlayType : void 0),
          Pe = (e, u) => {
            const t = w(),
              a = u || (t.mediaSize < b.Medium ? ce.Small : ce.Big);
            return {
              parsedRewards: re(e, (e) => {
                let u = Me({}, e);
                return Object.assign({}, u, {
                  special: ye(u),
                  image: xe(u, a),
                  size: a,
                  valueType:
                    ((t = u.name),
                    pe.includes(t)
                      ? _e.MULTI
                      : he.includes(t)
                        ? _e.CURRENCY
                        : be.includes(t)
                          ? _e.NUMBER
                          : ve.includes(t)
                            ? _e.PREMIUM_PLUS
                            : _e.STRING),
                  tooltipArgs: Re({ tooltipId: u.tooltipId, tooltipContentId: u.tooltipContentId }),
                });
                var t;
              }),
              imageSize: a,
            };
          },
          Le = [
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
        function Oe(e) {
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
        const Ne = (e, u, t = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: q.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: a,
                },
                t,
              ),
            );
          },
          ke = (e) => {
            let u = e.children,
              t = e.contentId,
              r = e.args,
              n = e.onMouseEnter,
              s = e.onMouseLeave,
              i = e.onMouseDown,
              o = e.onClick,
              l = e.ignoreShowDelay,
              E = void 0 !== l && l,
              c = e.ignoreMouseClick,
              _ = void 0 !== c && c,
              m = e.decoratorId,
              d = void 0 === m ? 0 : m,
              A = e.isEnabled,
              F = void 0 === A || A,
              D = e.targetId,
              B = void 0 === D ? 0 : D,
              C = e.onShow,
              g = e.onHide,
              p = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Le);
            const h = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              b = (0, a.useMemo)(
                () =>
                  B ||
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
                [B],
              ),
              v = (0, a.useCallback)(() => {
                (h.current.isVisible && h.current.timeoutId) ||
                  (Ne(t, d, { isMouseEvent: !0, on: !0, arguments: Oe(r) }, b),
                  C && C(),
                  (h.current.isVisible = !0));
              }, [t, d, r, b, C]),
              f = (0, a.useCallback)(() => {
                if (h.current.isVisible || h.current.timeoutId) {
                  const e = h.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (h.current.timeoutId = 0)),
                    Ne(t, d, { on: !1 }, b),
                    h.current.isVisible && g && g(),
                    (h.current.isVisible = !1));
                }
              }, [t, d, b, g]),
              w = (0, a.useCallback)((e) => {
                h.current.isVisible &&
                  ((h.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (h.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(h.current.prevTarget) && f();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const e = h.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === F && f();
              }, [F, f]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", f),
                  () => {
                    (window.removeEventListener("mouseleave", f), f());
                  }
                ),
                [f],
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
                            ((h.current.timeoutId = window.setTimeout(v, E ? 100 : 400)),
                            n && n(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (f(), null == s || s(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === _ && f(), null == o || o(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === _ && f(), null == i || i(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    p,
                  ),
                )
              : u;
            var S;
          },
          Ie = ["children"];
        function He() {
          return (
            (He =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            He.apply(this, arguments)
          );
        }
        const Ue = (e) => {
            let u = e.children,
              t = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Ie);
            return r().createElement(
              ke,
              He(
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
          Ge = ["children", "body", "header", "note", "alert", "args"];
        function We() {
          return (
            (We =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            We.apply(this, arguments)
          );
        }
        const $e = R.views.common.tooltip_window.simple_tooltip_content,
          qe = (e) => {
            let u = e.children,
              t = e.body,
              n = e.header,
              s = e.note,
              i = e.alert,
              o = e.args,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Ge);
            const E = (0, a.useMemo)(() => {
              const e = Object.assign({}, o, { body: t, header: n, note: s, alert: i });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [i, t, n, s, o]);
            return r().createElement(
              ke,
              We(
                {
                  contentId:
                    ((c = null == o ? void 0 : o.hasHtmlContent),
                    c ? $e.SimpleTooltipHtmlContent("resId") : $e.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: E,
                },
                l,
              ),
              u,
            );
            var c;
          };
        function je() {
          return (
            (je =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            je.apply(this, arguments)
          );
        }
        const Xe = ({ children: e, tooltipArgs: u, className: t }) => {
            if (!u) return e;
            const a = r().createElement("div", { className: t }, e);
            if (u.header || u.body) return r().createElement(qe, u, a);
            const n = u.contentId,
              s = u.args,
              i = null == s ? void 0 : s.contentId;
            return n || i
              ? r().createElement(ke, je({}, u, { contentId: n || i }), a)
              : r().createElement(Ue, u, a);
          },
          ze = {
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
          Ye = ({
            name: e,
            image: u,
            isPeriodic: t = !1,
            size: a = ce.Big,
            special: n,
            value: s,
            valueType: i,
            style: o,
            className: l,
            classNames: E,
            tooltipArgs: c,
            periodicIconTooltipArgs: _,
          }) => {
            const m = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case me.BATTLE_BOOSTER:
                  case me.BATTLE_BOOSTER_REPLACE:
                    return de.BATTLE_BOOSTER;
                }
              })(n),
              d = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case me.BATTLE_BOOSTER:
                    return Ae.BATTLE_BOOSTER;
                  case me.BATTLE_BOOSTER_REPLACE:
                    return Ae.BATTLE_BOOSTER_REPLACE;
                  case me.BUILT_IN_EQUIPMENT:
                    return Ae.BUILT_IN_EQUIPMENT;
                  case me.EQUIPMENT_PLUS:
                    return Ae.EQUIPMENT_PLUS;
                  case me.EQUIPMENT_TROPHY_BASIC:
                    return Ae.EQUIPMENT_TROPHY_BASIC;
                  case me.EQUIPMENT_TROPHY_UPGRADED:
                    return Ae.EQUIPMENT_TROPHY_UPGRADED;
                  case me.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return Ae.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case me.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return Ae.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case me.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return Ae.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case me.PROGRESSION_STYLE_UPGRADED_1:
                    return Ae.PROGRESSION_STYLE_UPGRADED_1;
                  case me.PROGRESSION_STYLE_UPGRADED_2:
                    return Ae.PROGRESSION_STYLE_UPGRADED_2;
                  case me.PROGRESSION_STYLE_UPGRADED_3:
                    return Ae.PROGRESSION_STYLE_UPGRADED_3;
                  case me.PROGRESSION_STYLE_UPGRADED_4:
                    return Ae.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(n),
              A = ((e, u) => {
                if (void 0 === e) return null;
                switch (u) {
                  case _e.MULTI: {
                    const u = Number(e);
                    return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
                  }
                  case _e.CURRENCY:
                  case _e.NUMBER:
                    return r().createElement(ge, { format: "integral", value: Number(e) });
                  case _e.PREMIUM_PLUS: {
                    const u = Number(e);
                    return isNaN(u) ? e : null;
                  }
                  default:
                    return e;
                }
              })(s, i);
            return r().createElement(
              "div",
              { className: g()(ze.base, ze[`base__${a}`], l), style: o },
              r().createElement(
                Xe,
                { tooltipArgs: c, className: ze.tooltipWrapper },
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement(
                    "div",
                    { className: g()(ze.image, null == E ? void 0 : E.image) },
                    m &&
                      r().createElement("div", {
                        className: g()(ze.highlight, null == E ? void 0 : E.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${m}_highlight)`,
                        },
                      }),
                    u &&
                      r().createElement("div", {
                        className: g()(ze.icon, null == E ? void 0 : E.rewardIcon),
                        style: { backgroundImage: `url(${u})` },
                      }),
                    d &&
                      r().createElement("div", {
                        className: g()(ze.overlay, null == E ? void 0 : E.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${a}.${d}_overlay)`,
                        },
                      }),
                  ),
                  A &&
                    r().createElement(
                      "div",
                      {
                        className: g()(
                          ze.info,
                          ze[`info__${e}`],
                          i === _e.MULTI && ze.info__multi,
                          null == E ? void 0 : E.info,
                        ),
                      },
                      A,
                    ),
                ),
              ),
              t &&
                r().createElement(
                  Xe,
                  { tooltipArgs: _ },
                  r().createElement("div", {
                    className: g()(ze.timer, null == E ? void 0 : E.periodicIcon),
                  }),
                ),
            );
          };
        var Ve = t(887),
          Qe = t.n(Ve);
        const Ke = ["xl", "lg", "md", "sm", "xs"],
          Ze = (e) => e.includes("_") && ((e) => Ke.includes(e))(e.split("_").at(-1)),
          Je = [b.ExtraLarge, b.Large, b.Medium, b.Small, b.ExtraSmall],
          eu = (e, u) =>
            Object.keys(e).reduce((t, a) => {
              if (a in t) return t;
              if (Ze(a)) {
                const r = a.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const n = Je.indexOf(u),
                  s = (-1 !== n ? Ke.slice(n) : [])
                    .map((e) => r + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  i = s ? e[s] : void 0;
                return ((t[r] = void 0 !== i ? i : e[r]), t);
              }
              const r = e[a];
              return (
                void 0 === r ||
                  ((e, u) => Ke.some((t) => void 0 !== u[`${e}_${t}`]))(a, e) ||
                  (t[a] = r),
                t
              );
            }, {}),
          uu = (e, u = eu) => {
            const t = (
              (e, u = eu) =>
              (t) => {
                const n = w().mediaSize,
                  s = (0, a.useMemo)(() => u(t, n), [t, n]);
                return r().createElement(e, s);
              }
            )(e, u);
            return r().memo((u) =>
              Object.keys(u).some((e) => Ze(e) && void 0 !== u[e])
                ? r().createElement(t, u)
                : r().createElement(e, u),
            );
          },
          tu = {
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
          au = [
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
        function ru() {
          return (
            (ru =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ru.apply(this, arguments)
          );
        }
        Object.keys(Qe());
        const nu = {
            XL: { mt: tu.mt__XL, mr: tu.mr__XL, mb: tu.mb__XL, ml: tu.ml__XL },
            LG: { mt: tu.mt__LG, mr: tu.mr__LG, mb: tu.mb__LG, ml: tu.ml__LG },
            MDp: { mt: tu.mt__MDp, mr: tu.mr__MDp, mb: tu.mb__MDp, ml: tu.ml__MDp },
            MD: { mt: tu.mt__MD, mr: tu.mr__MD, mb: tu.mb__MD, ml: tu.ml__MD },
            SMp: { mt: tu.mt__SMp, mr: tu.mr__SMp, mb: tu.mb__SMp, ml: tu.ml__SMp },
            SM: { mt: tu.mt__SM, mr: tu.mr__SM, mb: tu.mb__SM, ml: tu.ml__SM },
            XS: { mt: tu.mt__XS, mr: tu.mr__XS, mb: tu.mb__XS, ml: tu.ml__XS },
          },
          su = (Object.keys(nu), ["mt", "mr", "mb", "ml"]),
          iu = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          ou = uu((e) => {
            let u = e.className,
              t = e.width,
              n = e.height,
              s = e.m,
              i = e.mt,
              o = void 0 === i ? s : i,
              l = e.mr,
              E = void 0 === l ? s : l,
              c = e.mb,
              _ = void 0 === c ? s : c,
              m = e.ml,
              d = void 0 === m ? s : m,
              A = e.column,
              F = e.row,
              D = e.flexDirection,
              B = void 0 === D ? (A ? "column" : F && "row") || void 0 : D,
              C = e.flexStart,
              p = e.center,
              h = e.flexEnd,
              b = e.spaceBetween,
              v = e.spaceAround,
              f = e.justifyContent,
              w =
                void 0 === f
                  ? (C ? "flex-start" : p && "center") ||
                    (h && "flex-end") ||
                    (b && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : f,
              S = e.alignItems,
              x =
                void 0 === S
                  ? (C ? "flex-start" : p && "center") || (h && "flex-end") || void 0
                  : S,
              R = e.alignSelf,
              T = e.wrap,
              M = e.flexWrap,
              y = void 0 === M ? (T ? "wrap" : void 0) : M,
              P = e.grow,
              L = e.shrink,
              O = e.flex,
              N = void 0 === O ? (P || L ? `${P ? 1 : 0} ${L ? 1 : 0} auto` : void 0) : O,
              k = e.style,
              I = e.children,
              H = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, au);
            const U = (0, a.useMemo)(() => {
                const e = { mt: o, mr: E, mb: _, ml: d },
                  u = ((e) =>
                    su.reduce((u, t) => {
                      const a = e[t];
                      return a && "number" != typeof a ? u.concat(nu[!0 === a ? "MD" : a][t]) : u;
                    }, []))(e),
                  a = ((e) =>
                    su.reduce((u, t) => {
                      const a = e[t];
                      return ("number" == typeof a && (u[iu[t]] = a + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, k, a, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: N,
                    alignSelf: R,
                    display: B || x ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: y,
                    justifyContent: w,
                    alignItems: x,
                  }),
                  computedClassNames: u,
                };
              }, [t, n, o, E, _, d, k, N, R, B, y, w, x]),
              G = U.computedStyle,
              W = U.computedClassNames;
            return r().createElement(
              "div",
              ru({ className: g()(tu.base, ...W, u), style: G }, H),
              I,
            );
          });
        let lu;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(lu || (lu = {}));
        const Eu = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          cu = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          _u = (e, u, t = lu.left) => e.split(u).reduce(t === lu.left ? Eu : cu, []),
          mu = (() => {
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
          du = ["zh_cn", "zh_sg", "zh_tw"],
          Au = (e, u = lu.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return du.includes(t)
              ? mu(e)
              : ((e, u = lu.left) => {
                  let t = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (_u(r, /( )/, u).forEach((e) => (t = t.concat(_u(e, a, lu.left)))), t);
                })(e, u);
          },
          Fu = "FormatText_base_d0",
          Du = ({ binding: e, text: u = "", classMix: t, alignment: n = lu.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : r().createElement(
                  a.Fragment,
                  null,
                  u.split("\n").map((u, s) =>
                    r().createElement(
                      "div",
                      { className: g()(Fu, t), key: `${u}-${s}` },
                      ((e, u, t) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (t && e in t ? t[e] : Au(e, u))))(u, n, e).map((e, u) =>
                        r().createElement(a.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        var Bu = t(532),
          Cu = t.n(Bu);
        const gu = {
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
          pu = [
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
        function hu() {
          return (
            (hu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            hu.apply(this, arguments)
          );
        }
        Object.keys(Qe());
        const bu = Object.keys(Cu()),
          vu = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          fu = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          wu = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Su = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          xu =
            (Object.keys(Su),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": vu,
              "heading-H36": vu,
              "heading-H28": fu,
              "heading-H24": fu,
              "heading-H24R": fu,
              "heading-H22": fu,
              "heading-H20R": fu,
              "heading-H18": fu,
              "heading-H15": wu,
              "heading-H14": wu,
              "paragraph-P24": fu,
              "paragraph-P18": fu,
              "paragraph-P16": fu,
              "paragraph-P14": wu,
              "paragraph-P12": wu,
              "paragraph-P10": wu,
            }),
          Ru =
            (Object.keys(xu),
            (e) =>
              e
                ? ((e) => bu.includes(e))(e)
                  ? { colorClassName: gu[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Tu = uu((e) => {
            let u = e.text,
              t = e.variant,
              n = e.className,
              s = e.color,
              i = e.m,
              o = e.mt,
              l = void 0 === o ? i : o,
              E = e.mr,
              c = void 0 === E ? i : E,
              _ = e.mb,
              m = void 0 === _ ? i : _,
              d = e.ml,
              A = void 0 === d ? i : d,
              F = e.style,
              D = e.format,
              B = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, pu);
            const C = (0, a.useMemo)(() => {
                const e = Ru(s),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  a = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, F, a), colorClassName: u };
              }, [F, s]),
              p = C.computedStyle,
              h = C.colorClassName;
            return r().createElement(
              ou,
              hu(
                {
                  className: g()(gu.base, t && gu[t], h, n),
                  style: p,
                  mt: !0 === l ? xu[t || "paragraph-P16"].mt : l,
                  mr: !0 === c ? xu[t || "paragraph-P16"].mr : c,
                  mb: !0 === m ? xu[t || "paragraph-P16"].mb : m,
                  ml: !0 === A ? xu[t || "paragraph-P16"].ml : A,
                },
                B,
              ),
              void 0 !== D ? r().createElement(Du, hu({}, D, { text: u })) : u,
            );
          });
        var Mu = t(30);
        const yu = (e) => Math.sqrt(1 - Math.pow(e - 1, 2)),
          Pu = "AnimatedReward_base_72",
          Lu = ({ index: e = 0, delay: u = 0, children: t }) => {
            const a = (0, Mu.useSpring)({
              from: { scale: 1.2, opacity: 0, transform: "translateY(20rem)" },
              to: { scale: 1, opacity: 1, transform: "translateY(0)" },
              delay: u + 900 + 200 * e,
              config: { duration: 400, easing: yu },
              onStart: () => {
                I(R.sounds.gui_random_reward_appear());
              },
            });
            return r().createElement(Mu.animated.div, { className: Pu, style: a }, t);
          },
          Ou = {
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
        let Nu, ku;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(Nu || (Nu = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(ku || (ku = {})));
        const Iu = ({
          children: e,
          size: u,
          isFocused: t,
          type: n,
          disabled: s,
          mixClass: i,
          soundHover: o,
          soundClick: l,
          onMouseEnter: E,
          onMouseMove: c,
          onMouseDown: _,
          onMouseUp: m,
          onMouseLeave: d,
          onClick: A,
        }) => {
          const F = (0, a.useRef)(null),
            D = (0, a.useState)(t),
            B = D[0],
            C = D[1],
            p = (0, a.useState)(!1),
            h = p[0],
            b = p[1],
            v = (0, a.useState)(!1),
            f = v[0],
            w = v[1],
            S = (0, a.useCallback)(() => {
              s || (F.current && (F.current.focus(), C(!0)));
            }, [s]),
            x = (0, a.useCallback)(
              (e) => {
                B && null !== F.current && !F.current.contains(e.target) && C(!1);
              },
              [B],
            ),
            T = (0, a.useCallback)(
              (e) => {
                s || (A && A(e));
              },
              [s, A],
            ),
            M = (0, a.useCallback)(
              (e) => {
                s || (null !== o && I(o), E && E(e), w(!0));
              },
              [s, o, E],
            ),
            y = (0, a.useCallback)(
              (e) => {
                c && c(e);
              },
              [c],
            ),
            P = (0, a.useCallback)(
              (e) => {
                s || (m && m(e), b(!1));
              },
              [s, m],
            ),
            L = (0, a.useCallback)(
              (e) => {
                s || (null !== l && I(l), _ && _(e), t && S(), b(!0));
              },
              [s, l, _, S, t],
            ),
            O = (0, a.useCallback)(
              (e) => {
                s || (d && d(e), b(!1));
              },
              [s, d],
            ),
            N = g()(
              Ou.base,
              Ou[`base__${n}`],
              {
                [Ou.base__disabled]: s,
                [Ou[`base__${u}`]]: u,
                [Ou.base__focus]: B,
                [Ou.base__highlightActive]: h,
                [Ou.base__firstHover]: f,
              },
              i,
            ),
            k = g()(Ou.state, Ou.state__default);
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
            r().createElement(
              "div",
              {
                ref: F,
                className: N,
                onMouseEnter: M,
                onMouseMove: y,
                onMouseUp: P,
                onMouseDown: L,
                onMouseLeave: O,
                onClick: T,
              },
              n !== Nu.ghost &&
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement("div", { className: Ou.back }),
                  r().createElement("span", { className: Ou.texture }),
                ),
              r().createElement(
                "span",
                { className: k },
                r().createElement("span", { className: Ou.stateDisabled }),
                r().createElement("span", { className: Ou.stateHighlightHover }),
                r().createElement("span", { className: Ou.stateHighlightActive }),
              ),
              r().createElement(
                "span",
                { className: Ou.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Iu.defaultProps = {
          type: Nu.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const Hu = (0, a.memo)(Iu),
          Uu = "ChooseRewardButton_base_56",
          Gu = "ChooseRewardButton_buttonHolder_05",
          Wu = "ChooseRewardButton_buttonInner_a6",
          $u = "ChooseRewardButton_button_78",
          qu = "ChooseRewardButton_buttonBlink_15",
          ju = "ChooseRewardButton_buttonText_b2",
          Xu = R.strings.personal_missions_3.RewardsView.content,
          zu = (0, a.memo)(({ onClick: e }) =>
            r().createElement(
              "div",
              { className: Uu },
              r().createElement(
                "div",
                { className: Gu },
                r().createElement(
                  "div",
                  { className: Wu },
                  r().createElement(
                    Hu,
                    { type: Nu.ghost, size: ku.extraSmall, onClick: e, mixClass: $u },
                    r().createElement("div", { className: qu }),
                    r().createElement(Tu, { className: ju, text: Xu.btn.chooseReward() }),
                  ),
                ),
              ),
            ),
          ),
          Yu = "Rewards_base_74",
          Vu = "Rewards_rewardWrapper_f0",
          Qu = "Rewards_rewardWrapper__last_8e",
          Ku = "Rewards_box_a8",
          Zu = "Rewards_label_ce";
        function Ju() {
          return (
            (Ju =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Ju.apply(this, arguments)
          );
        }
        const et = R.strings.personal_missions_3.RewardsView.content.awards.additional,
          ut = (0, a.memo)(
            ({
              rewards: e,
              delay: u,
              maxRewards: t = 0,
              onChooseBtnClick: n,
              classNames: s,
              className: i,
              isEnabled: o,
              isSelectedRewards: l,
            }) => {
              const E = w().mediaSize < b.Medium ? ce.Small : ce.Big,
                c = Boolean(t) && t < e.length,
                _ = c ? e.slice(0, t - 1) : e,
                m = (0, a.useMemo)(
                  () => (c ? `R.images.gui.maps.icons.quests.bonuses.${E}.default` : ""),
                  [c, E],
                ),
                d = c
                  ? ((A = et.bottom()),
                    (F = { count: e.length - (t - 1) }),
                    A.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
                      const u = 0 === e.indexOf("%") ? 2 : 1;
                      return String(F[e.slice(u, -u)]);
                    }))
                  : "";
              var A, F;
              const D = (0, a.useMemo)(
                () =>
                  c
                    ? Re(
                        { inBoxCount: e.length - (t - 1) },
                        R.views.lobby.personal_missions.tooltips.RestRewardsTooltipView("resId"),
                      )
                    : void 0,
                [t, c, e.length],
              );
              return r().createElement(
                "div",
                { className: Yu },
                _.map((e, t) =>
                  r().createElement(
                    "div",
                    { className: l ? g()(Vu, t === _.length - 1 && Qu) : void 0, key: t },
                    r().createElement(
                      Lu,
                      { index: t, delay: u },
                      r().createElement(
                        Ye,
                        Ju({ classNames: Object.assign({}, s) }, e, {
                          className: i,
                          tooltipArgs: Object.assign({}, e.tooltipArgs, { isEnabled: o }),
                        }),
                      ),
                      e.size !== ce.Big &&
                        e.size !== ce.Small &&
                        r().createElement(Tu, { className: g()(Zu), text: e.userName || e.label }),
                      e.isChooseReward &&
                        r().createElement(zu, { onClick: () => (null == n ? void 0 : n(e.id)) }),
                    ),
                  ),
                ),
                c &&
                  r().createElement(
                    Lu,
                    { index: t - 1, delay: u },
                    r().createElement(Ye, {
                      name: "more",
                      image: m,
                      size: E,
                      value: d,
                      tooltipArgs: D,
                      className: Ku,
                    }),
                  ),
              );
            },
          ),
          tt = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let at, rt;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(at || (at = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(rt || (rt = {})));
        const nt = ({ size: e = at.Default, classMix: u }) =>
            r().createElement("div", { className: g()(tt.background, tt[`background__${e}`], u) }),
          st = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          it = ({ size: e }) => {
            const u = g()(st.base, st[`base__${e}`]);
            return r().createElement("div", { className: u });
          },
          ot = {
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
          lt = (0, a.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: a,
              isComplete: n,
              withoutBounce: s,
            }) => {
              const i = g()(
                  ot.base,
                  ot[`base__${e}`],
                  t && ot.base__disabled,
                  n && ot.base__finished,
                  s && ot.base__withoutBounce,
                ),
                o = !t && !n;
              return r().createElement(
                "div",
                { className: i, style: a, ref: u },
                r().createElement("div", { className: ot.pattern }),
                r().createElement("div", { className: ot.gradient }),
                o && r().createElement(it, { size: e }),
              );
            },
          ),
          Et = ({ size: e, value: u, lineRef: t, disabled: n, onComplete: s }) => {
            const i = (0, a.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              o = 100 === u;
            return (
              (0, a.useEffect)(() => {
                o && s && s();
              }, [o, s]),
              r().createElement(lt, {
                size: e,
                disabled: n,
                baseStyles: i,
                isComplete: o,
                lineRef: t,
              })
            );
          },
          ct = (e, u) => {
            let t;
            const a = setTimeout(() => {
              t = e();
            }, u);
            return () => {
              ("function" == typeof t && t(), clearTimeout(a));
            };
          };
        let _t, mt;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(_t || (_t = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(mt || (mt = {})));
        const dt = "ProgressBarDeltaSimple_base_6c",
          At = "ProgressBarDeltaSimple_delta_99",
          Ft = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: n,
              size: s,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
            }) => {
              const E = i < n,
                c = (0, a.useState)(mt.Idle),
                _ = c[0],
                m = c[1],
                d = _ === mt.In,
                A = _ === mt.End,
                F = _ === mt.Idle,
                D = (0, a.useCallback)(
                  (e) => {
                    (m(e), l && l(e));
                  },
                  [l],
                );
              ((0, a.useEffect)(() => {
                if (F && !t) {
                  return ct(() => {
                    D(mt.In);
                  }, u);
                }
              }, [D, t, F, u]),
                (0, a.useEffect)(() => {
                  if (d) {
                    return ct(() => {
                      (o && o(), D(mt.End));
                    }, e + u);
                  }
                }, [D, d, o, u, e]));
              const B = (0, a.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [E ? "left" : "right"]: "0",
                  }),
                  [E, u, e],
                ),
                C = (0, a.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [E ? "left" : "right"]: "0",
                  }),
                  [E, u, e],
                ),
                g = (0, a.useMemo)(
                  () => ({ width: `${Math.abs(n - i)}%`, left: `${E ? i : n}%` }),
                  [n, E, i],
                );
              return A
                ? null
                : r().createElement(
                    "div",
                    { className: dt, style: g },
                    r().createElement(
                      "div",
                      { style: F ? B : C, className: At },
                      r().createElement(it, { size: s }),
                    ),
                  );
            },
          ),
          Dt = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: n,
              disabled: s,
              isComplete: i,
              animationSettings: o,
              onChangeAnimationState: l,
              onEndAnimation: E,
            }) => {
              const c = (0, a.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${o.line.duration}ms`,
                  transitionDelay: `${o.line.delay}ms`,
                }),
                [o.line.delay, o.line.duration, e],
              );
              return r().createElement(
                r().Fragment,
                null,
                r().createElement(lt, {
                  size: u,
                  lineRef: n,
                  disabled: s,
                  isComplete: i,
                  baseStyles: c,
                }),
                t >= 0 &&
                  r().createElement(Ft, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    freezed: o.freezed,
                    from: t,
                    size: u,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: E,
                  }),
              );
            },
          ),
          Bt = "ProgressBarDeltaGrow_base_7e",
          Ct = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          gt = "ProgressBarDeltaGrow_glow_68",
          pt = (e) => (e ? { left: 0 } : { right: 0 }),
          ht = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          bt = (e) => ({ transitionDuration: `${e}ms` }),
          vt = (0, a.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: n,
              size: s,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
              className: E,
            }) => {
              const c = i < n,
                _ = (0, a.useState)(_t.Idle),
                m = _[0],
                d = _[1],
                A = m === _t.End,
                F = m === _t.Idle,
                D = m === _t.Grow,
                B = m === _t.Shrink,
                C = (0, a.useCallback)(
                  (e) => {
                    (d(e), l && l(e));
                  },
                  [l],
                ),
                p = (0, a.useCallback)(
                  (e, u) =>
                    ct(() => {
                      C(e);
                    }, u),
                  [C],
                );
              (0, a.useEffect)(() => {
                if (!t)
                  return F
                    ? p(_t.Grow, u)
                    : D
                      ? p(_t.Shrink, e)
                      : B
                        ? p(_t.End, e)
                        : void (A && o && o());
              }, [p, t, A, D, F, B, o, u, e]);
              const h = (0, a.useMemo)(
                  () => Object.assign({ width: "100%" }, bt(e), pt(c)),
                  [c, e],
                ),
                b = (0, a.useMemo)(() => Object.assign({ width: "0%" }, bt(e), pt(c)), [c, e]),
                v = (0, a.useMemo)(
                  () => Object.assign({ width: "0%" }, ht(c, n), bt(e)),
                  [n, c, e],
                ),
                f = (0, a.useMemo)(
                  () => Object.assign({ width: `${Math.abs(i - n)}%` }, ht(c, n), bt(e)),
                  [n, c, i, e],
                );
              if (A) return null;
              const w = g()(Bt, E, c && 0 === i && Ct);
              return r().createElement(
                "div",
                { style: F ? v : f, className: w },
                r().createElement(
                  "div",
                  { style: B ? b : h, className: gt },
                  r().createElement(it, { size: s }),
                ),
              );
            },
          ),
          ft = (0, a.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: n,
              disabled: s,
              isComplete: i,
              animationSettings: o,
              onEndAnimation: l,
              onChangeAnimationState: E,
            }) => {
              const c = e < t,
                _ = (0, a.useState)(!1),
                m = _[0],
                d = _[1],
                A = (0, a.useCallback)(
                  (e) => {
                    (e === _t.Shrink && d(!0), E && E(e));
                  },
                  [E],
                ),
                F = (0, a.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                D = (0, a.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return r().createElement(
                r().Fragment,
                null,
                r().createElement(lt, {
                  size: u,
                  lineRef: n,
                  disabled: s,
                  isComplete: i,
                  withoutBounce: c && 0 === e,
                  baseStyles: m ? D : F,
                }),
                t >= 0 &&
                  r().createElement(vt, {
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
          wt = ["onComplete", "onEndAnimation"];
        function St() {
          return (
            (St =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            St.apply(this, arguments)
          );
        }
        const xt = (0, a.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, wt);
            const s = (0, a.useState)(!1),
              i = s[0],
              o = s[1],
              l = (0, a.useCallback)(() => {
                const e = 100 === n.to;
                (e !== i && o(e), e && u && u(), t && t());
              }, [i, u, t, n.to]);
            switch (n.animationSettings.type) {
              case rt.Simple:
                return r().createElement(Dt, St({}, n, { onEndAnimation: l, isComplete: i }));
              case rt.Growing:
                return r().createElement(ft, St({}, n, { onEndAnimation: l, isComplete: i }));
              default:
                return null;
            }
          }),
          Rt = ["onEndAnimation"];
        function Tt() {
          return (
            (Tt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Tt.apply(this, arguments)
          );
        }
        const Mt = (0, a.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, Rt);
          const n = (0, a.useRef)({}),
            s = (0, a.useCallback)(() => {
              ((n.current.from = void 0), u && u());
            }, [u]),
            i = "number" == typeof n.current.from ? n.current.from : t.from;
          return (
            (n.current.from = i),
            r().createElement(xt, Tt({}, t, { onEndAnimation: s, key: `${i}-${t.to}`, from: i }))
          );
        });
        function yt() {
          return (
            (yt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            yt.apply(this, arguments)
          );
        }
        const Pt = (0, a.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: a,
              deltaFrom: n,
              animationSettings: s,
              onEndAnimation: i,
              onChangeAnimationState: o,
              onComplete: l,
            }) => {
              if (n === u)
                return r().createElement(Et, {
                  key: `${n}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: a,
                  onComplete: l,
                });
              const E = {
                from: n,
                to: u,
                size: e,
                lineRef: t,
                disabled: a,
                animationSettings: s,
                onComplete: l,
                onEndAnimation: i,
                onChangeAnimationState: o,
              };
              return s.withStack
                ? r().createElement(Mt, E)
                : r().createElement(xt, yt({ key: `${n}-${u}` }, E));
            },
          ),
          Lt = (e) => ({
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
          Ot = {
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
          Nt = (e, u, t) => (t < e ? e : t > u ? u : t),
          kt = (e, u, t) => {
            if ("number" == typeof t) {
              return (Nt(0, u, t) / u) * 100;
            }
            return e;
          },
          It = Ot,
          Ht = {
            freezed: !1,
            withStack: !1,
            type: rt.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          Ut = (0, a.memo)(
            ({
              maxValue: e = 100,
              theme: u = It,
              size: t = at.Default,
              animationSettings: n = Ht,
              disabled: s = !1,
              withoutBackground: i = !1,
              progressBarBackgroundClassMix: o,
              value: l,
              deltaFrom: E,
              lineRef: c,
              onChangeAnimationState: _,
              onEndAnimation: m,
              onComplete: d,
            }) => {
              const A = ((e, u, t) =>
                (0, a.useMemo)(() => {
                  const a = (Nt(0, u, e) / u) * 100;
                  return { value: a, deltaFrom: kt(a, u, t) };
                }, [t, u, e]))(l, e, E);
              return r().createElement(
                "div",
                { className: g()(tt.base, tt[`base__${t}`]), style: Lt(u) },
                !i && r().createElement(nt, { size: t, classMix: o }),
                r().createElement(Pt, {
                  size: t,
                  lineRef: c,
                  disabled: s,
                  value: A.value,
                  deltaFrom: A.deltaFrom,
                  animationSettings: n,
                  onEndAnimation: m,
                  onChangeAnimationState: _,
                  onComplete: d,
                }),
              );
            },
          ),
          Gt = "VehicleProgression_base_59",
          Wt = "VehicleProgression_base__main_ea",
          $t = "VehicleProgression_vehicleWrapper_31",
          qt = "VehicleProgression_vehicle_f3",
          jt = "VehicleProgression_glow_36",
          Xt = "VehicleProgression_questsCountWrapper_ec",
          zt = "VehicleProgression_countTitle_ba",
          Yt = "VehicleProgression_progressBar_16",
          Vt = "VehicleProgression_current_22",
          Qt = "VehicleProgression_total_f6",
          Kt = "VehicleProgression_divider_c6",
          Zt = "VehicleProgression_description_20",
          Jt = R.strings.personal_missions_3.RewardsView.content.questCount,
          ea = (0, a.memo)(({ isMain: e = !1, className: u, value: t, maxValue: a, delta: n }) => {
            const s = g()(Gt, u, e && Wt);
            return r().createElement(
              "div",
              { className: s },
              r().createElement(
                "div",
                { className: $t },
                r().createElement("div", { className: jt }),
                r().createElement("div", { className: qt }),
              ),
              r().createElement(
                "div",
                { className: Xt },
                r().createElement(
                  "div",
                  { className: zt },
                  r().createElement(Tu, { text: String(t), className: Vt }),
                  r().createElement(Tu, { text: Jt.divider(), className: Qt }),
                  r().createElement(Tu, { text: String(a), className: Qt }),
                  r().createElement("div", { className: Kt }),
                  r().createElement(Tu, { className: Zt, text: Jt.text() }),
                ),
                r().createElement(
                  "div",
                  { className: Yt },
                  r().createElement(Ut, { value: t, maxValue: a, deltaFrom: n, theme: Ot }),
                ),
              ),
            );
          }),
          ua = "Content_base_b9",
          ta = "Content_ribbon_8b",
          aa = "Content_ribbon__selected_a1",
          ra = "Content_rewards_b2",
          na = "Content_reward_5a",
          sa = "Content_addRewards_ea",
          ia = "Content_addRewardInfo_b1",
          oa = "Content_additionalRewards_1c",
          la = "Content_additionalRewards__selected_8d",
          Ea = "Content_lines_95",
          ca = "Content_progression_a8";
        var _a;
        !(function (e) {
          ((e.SELECTABLE_BONUS = "selectableBonus"),
            (e.CRYSTAL = "crystal"),
            (e.PREMIUM = "premium"),
            (e.PREMIUM_PLUS = "premium_plus"),
            (e.FREE_XP = "freeXP"),
            (e.CREDITS = "credits"));
        })(_a || (_a = {}));
        const ma = [
            _a.SELECTABLE_BONUS,
            _a.CRYSTAL,
            _a.PREMIUM,
            _a.PREMIUM_PLUS,
            _a.FREE_XP,
            _a.CREDITS,
          ],
          da = (e) => e.sort((e, u) => ma.indexOf(e.name) - ma.indexOf(u.name)),
          Aa = (0, z.Pi)(({ className: e, isEnabled: u = !0, isFinal: t }) => {
            const a = oe(),
              n = a.model,
              s = a.controls,
              i = w().mediaSize,
              o = n.root.get(),
              l = o.isSelectedRewards,
              E = o.questTypeComplete,
              c = o.value,
              _ = o.maxValue,
              m = o.delta,
              d = o.isOperationAddRewards,
              A = i < b.Medium ? ce.S180x135 : ce.S232x174,
              F = i >= b.Large ? ce.S296x222 : A,
              D = i < b.Medium ? ce.Small : ce.Big,
              B = i < b.Medium ? ce.S232x174 : ce.S296x222,
              C = n.computes.getMainRewards(),
              p = n.computes.getAdditionalRewards(),
              h = n.computes.getSelectedRewards(),
              v = E === Be.COMPLETE_WITH_HONOR,
              f = E === Be.COMPLETE_ADD,
              S = (f || v) && t,
              x = Pe(C, F).parsedRewards,
              R = Pe(p, F).parsedRewards,
              T = ((e) => e.sort((e, u) => ("" === e.special) - ("" === u.special)))(
                Pe(h, d ? B : A).parsedRewards,
              ),
              M = Pe(T.slice(3), D).parsedRewards,
              y = da(v ? [...x, ...R] : x),
              P = (e) => {
                s.onChooseReward(e);
              };
            return r().createElement(
              "div",
              { className: g()(ua, e) },
              r().createElement("div", { className: Ea }),
              r().createElement(
                "div",
                { className: g()(ta, l && aa) },
                l || d
                  ? r().createElement(
                      r().Fragment,
                      null,
                      r().createElement(
                        "div",
                        { className: ra },
                        r().createElement(ut, {
                          rewards: T.slice(0, 3),
                          classNames: { info: na },
                          onChooseBtnClick: P,
                          isEnabled: u,
                          isSelectedRewards: l,
                        }),
                      ),
                      M.length > 0 &&
                        r().createElement(
                          "div",
                          { className: g()(oa, l && la) },
                          r().createElement(ut, {
                            rewards: M,
                            maxRewards: 10,
                            className: sa,
                            classNames: { info: ia },
                            delay: 1e3,
                            isEnabled: u,
                          }),
                        ),
                    )
                  : r().createElement(
                      "div",
                      { className: ra },
                      r().createElement(ut, {
                        rewards: f ? R : y,
                        classNames: { info: na },
                        onChooseBtnClick: P,
                        isEnabled: u,
                      }),
                    ),
                S && r().createElement(ea, { className: ca, maxValue: _, value: c, delta: m }),
              ),
            );
          }),
          Fa = "Footer_base_2e",
          Da = "Footer_buttons_ea",
          Ba = "Footer_button_73",
          Ca = "Footer_button__nextTask_d7",
          ga = "Footer_nextTaskBtn_ec",
          pa = "Footer_nextTaskIcon_7b",
          ha = "Footer_nextTaskWrapper_51",
          ba = "Footer_nextTaskTitle_c6",
          va = "Footer_nextTaskName_91",
          fa = "Footer_nextTask_56",
          wa = "Footer_fullCompleteTitle_2b",
          Sa = R.strings.personal_missions_3.RewardsView.footer,
          xa = (0, z.Pi)(({ className: e }) => {
            const u = oe(),
              t = u.controls,
              a = u.model,
              n = a.root.get(),
              s = n.nextTaskName,
              i = n.nextQuestID,
              o = n.questTypeComplete,
              l = n.isSelectedRewards,
              E = n.isFullChainComplete,
              c = n.questID,
              _ = n.type,
              m = n.isOperationAddRewards,
              d = a.questModel.get(),
              A = d.questLevelTo,
              F = d.questLevelFrom,
              D = d.isFinal,
              B = o === Be.COMPLETE_WITH_HONOR || o === Be.COMPLETE_ADD,
              C = o === Be.COMPLETE_BASIC,
              p = B || l || m || C,
              h = !B && !l,
              b = () => {
                t.openQuest(D ? c : i);
              };
            return r().createElement(
              "div",
              { className: g()(Fa, e) },
              !l &&
                !E &&
                !m &&
                r().createElement(
                  "div",
                  { className: ha },
                  B
                    ? r().createElement(Tu, {
                        className: ba,
                        text: E ? Sa.allTasksComplete() : Sa.allFlagTasksComplete(),
                        format: {
                          binding: { questLevelTo: A, questLevelFrom: F, type: Sa.type.$dyn(_) },
                        },
                      })
                    : r().createElement(
                        r().Fragment,
                        null,
                        r().createElement(Tu, {
                          className: ba,
                          text: D ? Sa.nextTask.improve() : Sa.nextTask.title(),
                        }),
                        r().createElement(
                          "div",
                          { className: fa },
                          r().createElement(Tu, { className: va, text: s }),
                          r().createElement(
                            Hu,
                            { type: Nu.secondary, mixClass: ga, onClick: b },
                            r().createElement("div", { className: pa }),
                          ),
                        ),
                      ),
                ),
              E &&
                r().createElement(Tu, {
                  className: wa,
                  text: Sa.allTasksComplete(),
                  format: { binding: { questLevelTo: A, questLevelFrom: F } },
                }),
              r().createElement(
                "div",
                { className: Da },
                r().createElement(
                  Hu,
                  { mixClass: Ba, type: Nu.primary, size: ku.medium, onClick: t.close },
                  r().createElement(Tu, { text: p ? Sa.btn.accept() : Sa.btn.continue() }),
                ),
                h &&
                  !D &&
                  !m &&
                  r().createElement(
                    Hu,
                    { mixClass: g()(Ba, Ca), type: Nu.secondary, size: ku.medium, onClick: b },
                    r().createElement(Tu, { text: Sa.btn.nextTask() }),
                  ),
              ),
            );
          });
        let Ra, Ta;
        (!(function (e) {
          ((e.BINARY = "binaryProgress"),
            (e.BIATHLON = "biathlonProgress"),
            (e.SERIES = "seriesProgress"),
            (e.LIMITED = "limitedProgress"),
            (e.VALUE = "valueProgress"),
            (e.COUNTER = "counterProgress"));
        })(Ra || (Ra = {})),
          (function (e) {
            ((e.And = "and"), (e.Or = "or"), (e.Default = "default"));
          })(Ta || (Ta = {})));
        const Ma = "CompleteQuestType_base_f9",
          ya = "CompleteQuestType_cycle_12",
          Pa = "CompleteQuestType_hexagon_fb",
          La = "CompleteQuestType_questIcon_7e",
          Oa = (0, a.memo)(
            ({
              icon: e,
              headerDescription: u,
              questTooltipID: t,
              idName: a,
              isEnabled: n,
              isCycle: s,
            }) => {
              const i = s ? ya : Pa;
              return r().createElement(
                "div",
                { className: Ma },
                !u &&
                  e &&
                  r().createElement(
                    "div",
                    { className: i },
                    r().createElement(
                      Xe,
                      { tooltipArgs: { contentId: t, args: { idName: a }, isEnabled: n } },
                      r().createElement("div", {
                        className: La,
                        style: {
                          backgroundImage:
                            ((o = e),
                            `url('R.images.gui.maps.icons.quests.battleCondition.c_128.icon_battle_condition_${o}_128x128')`),
                        },
                      }),
                    ),
                  ),
              );
              var o;
            },
          ),
          Na = {
            base: "CompleteQuestsList_base_58",
            separatorOrWrapper: "CompleteQuestsList_separatorOrWrapper_cf",
            separatorOr: "CompleteQuestsList_separatorOr_1a",
            divider: "CompleteQuestsList_divider_13",
            divider__default: "CompleteQuestsList_divider__default_a0",
            divider__or: "CompleteQuestsList_divider__or_b6",
            divider__and: "CompleteQuestsList_divider__and_ac",
            groups: "CompleteQuestsList_groups_16",
          };
        function ka() {
          return (
            (ka =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ka.apply(this, arguments)
          );
        }
        const Ia = (e = Ta.Default) =>
            e === Ta.Or
              ? r().createElement(
                  "div",
                  { className: Na.separatorOrWrapper },
                  r().createElement("div", { className: Na.separatorOr }),
                )
              : e === Ta.And
                ? r().createElement("div", { className: g()(Na.divider, Na.divider__and) })
                : r().createElement("div", { className: g()(Na.divider, Na[`divider__${e}`]) }),
          Ha = (0, a.memo)(({ quests: e, isDefaultDivider: u, isEnabled: t }) =>
            r().createElement(
              "div",
              { className: Na.base },
              u && Ia(),
              e.relation.groups.map((u, a) => {
                const n = u.names;
                return r().createElement(
                  "div",
                  { className: Na.groups, key: a },
                  n.map((u) =>
                    e.quests
                      .filter((e) => e.idName === u)
                      .map((e) =>
                        r().createElement(
                          "div",
                          { key: `relation_${a}__quest_${u}` },
                          r().createElement(Oa, ka({}, e, { isEnabled: t })),
                        ),
                      ),
                  ),
                  a !== e.relation.groups.length - 1 && Ia(e.relation.relationType),
                );
              }),
            ),
          ),
          Ua = {
            base: "Header_base_f4",
            content: "Header_content_ec",
            slideDown: "Header_slideDown_8f",
            title: "Header_title_ca",
            subtitle: "Header_subtitle_46",
            competedTask: "Header_competedTask_de",
            completedTitleWrapper: "Header_completedTitleWrapper_b2",
            completeImg: "Header_completeImg_b9",
            completeImg__completeWithHonor: "Header_completeImg__completeWithHonor_c4",
            completeImg__completeAdd: "Header_completeImg__completeAdd_71",
            completedTitle: "Header_completedTitle_e1",
            conditions: "Header_conditions_60",
            fadeOut: "Header_fadeOut_45",
            fadeIn: "Header_fadeIn_2e",
            slideUp: "Header_slideUp_d5",
            raysAppearance: "Header_raysAppearance_74",
            rotate: "Header_rotate_6c",
          },
          Ga = R.strings.personal_missions_3.RewardsView.header,
          Wa = (0, z.Pi)(({ isEnabled: e }) => {
            const u = oe().model,
              t = u.root.get(),
              a = t.operationName,
              n = t.currentTaskName,
              s = t.questTypeComplete,
              i = t.isSelectedRewards,
              o = t.isOperationAddRewards,
              l = u.computes.getQuestData(),
              E = l[0],
              c = l[1],
              _ = s === Be.COMPLETE_ADD,
              m = s === Be.COMPLETE_WITH_HONOR,
              d = (c.quests.length > 0 && m) || _;
            return r().createElement(
              "div",
              { className: Ua.base },
              r().createElement(
                "div",
                { className: Ua.content },
                o
                  ? r().createElement(
                      r().Fragment,
                      null,
                      r().createElement(Tu, {
                        className: Ua.title,
                        text: Ga.titleWithHonor(),
                        format: { binding: { operationName: a } },
                      }),
                      r().createElement(Tu, { className: Ua.subtitle, text: Ga.gotOneReward() }),
                    )
                  : r().createElement(
                      r().Fragment,
                      null,
                      r().createElement(Tu, {
                        className: Ua.title,
                        text: i ? Ga.company() : Ga.title(),
                        format: { binding: { operationName: a } },
                      }),
                      r().createElement(Tu, {
                        className: Ua.subtitle,
                        text: i ? Ga.gotRewards() : Ga.subtitle(),
                        format: { binding: { questID: n } },
                      }),
                    ),
                !i &&
                  !o &&
                  r().createElement(
                    "div",
                    { className: Ua.competedTask },
                    r().createElement(
                      "div",
                      { className: Ua.completedTitleWrapper },
                      r().createElement("div", {
                        className: g()(Ua.completeImg, Ua[`completeImg__${s}`]),
                      }),
                      r().createElement(Tu, {
                        className: Ua.completedTitle,
                        text: Ga.taskStatus.$dyn(s),
                      }),
                    ),
                    r().createElement(
                      "div",
                      { className: Ua.conditions },
                      !_ && r().createElement(Ha, { quests: E, isEnabled: e }),
                      d && r().createElement(Ha, { quests: c, isEnabled: e, isDefaultDivider: !_ }),
                    ),
                  ),
              ),
            );
          }),
          $a = "App_base_9f",
          qa = "App_view_d8",
          ja = "App_view__final_40",
          Xa = "App_content_f7",
          za = "App_footer_bc",
          Ya = "App_closeBtn_02",
          Va = "App_character_4f",
          Qa = R.strings.personal_missions_3.RewardsView.header,
          Ka = (0, z.Pi)(() => {
            const e = oe(),
              u = e.controls,
              t = e.model,
              n = t.root.get().questTypeComplete,
              s = t.questModel.get().isFinal,
              i = (0, a.useState)(!0),
              o = i[0],
              l = i[1];
            var E;
            return (
              (E = () => {
                (l(!1), u.close());
              }),
              X($.n.ESCAPE, E),
              r().createElement(
                "div",
                { className: $a },
                r().createElement(W, {
                  caption: Qa.btn.close(),
                  type: "close",
                  side: "right",
                  classNames: { base: Ya },
                  onClick: u.close,
                }),
                r().createElement(
                  "div",
                  { className: g()(qa, s && ja) },
                  r().createElement(Wa, { isEnabled: o }),
                  r().createElement(Aa, { className: Xa, isEnabled: o, isFinal: s }),
                  r().createElement(xa, { className: za }),
                  s && r().createElement(K, { className: Va, state: n }),
                ),
              )
            );
          });
        engine.whenReady.then(() => {
          k().render(
            r().createElement(ie, null, r().createElement(O, null, r().createElement(Ka, null))),
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
        var r = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [u, t, a] = deferred[o], n = !0, s = 0; s < u.length; s++)
            (!1 & a || r >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[s]))
              ? u.splice(s--, 1)
              : ((n = !1), a < r && (r = a));
          if (n) {
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
    (__webpack_require__.j = 981),
    (() => {
      var e = { 981: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var a,
            r,
            [n, s, i] = t,
            o = 0;
          if (n.some((u) => 0 !== e[u])) {
            for (a in s) __webpack_require__.o(s, a) && (__webpack_require__.m[a] = s[a]);
            if (i) var l = i(__webpack_require__);
          }
          for (u && u(t); o < n.length; o++)
            ((r = n[o]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [650], () => __webpack_require__(512));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
