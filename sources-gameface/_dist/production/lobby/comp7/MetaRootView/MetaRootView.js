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
      527: (e, t, a) => {
        "use strict";
        (a.r(t), a.d(t, { mouse: () => i, onResize: () => u }));
        var n = a(2472),
          r = a(1176);
        const u = (0, n.E)("clientResized"),
          s = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const i = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, r.R)(!1);
          }
          function a() {
            e.enabled && (0, r.R)(!0);
          }
          function n() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", a))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", a))
              : (0, r.R)(!1);
          }
          const u = ["down", "up", "move"].reduce(
            (t, a) => (
              (t[a] = (function (t) {
                return (a) => {
                  e.listeners += 1;
                  let r = !0;
                  const u = `mouse${t}`,
                    i = s[t]((e) => a([e, "outside"]));
                  function o(e) {
                    a([e, "inside"]);
                  }
                  return (
                    window.addEventListener(u, o),
                    n(),
                    () => {
                      r &&
                        (i(), window.removeEventListener(u, o), (e.listeners -= 1), n(), (r = !1));
                    }
                  );
                };
              })(a)),
              t
            ),
            {},
          );
          return Object.assign({}, u, {
            disable() {
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
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
      5959: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            events: () => n,
            getMouseGlobalPosition: () => u,
            getSize: () => r,
            graphicsQuality: () => s,
          }));
        var n = a(527);
        function r(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function u(e = "px") {
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
      1176: (e, t, a) => {
        "use strict";
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        a.d(t, { R: () => n });
      },
      2472: (e, t, a) => {
        "use strict";
        function n(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        a.d(t, { E: () => n });
      },
      3138: (e, t, a) => {
        "use strict";
        a.d(t, { O: () => r });
        var n = a(5959);
        const r = { view: a(7641), client: n };
      },
      3722: (e, t, a) => {
        "use strict";
        function n(e, t, a = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, a);
        }
        function r(e, t, a) {
          return `url(${n(e, t, a)})`;
        }
        (a.r(t), a.d(t, { getBgUrl: () => r, getTextureUrl: () => n }));
      },
      6112: (e, t, a) => {
        "use strict";
        a.d(t, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, a) => {
        "use strict";
        a.d(t, { U: () => r });
        var n = a(2472);
        const r = {
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
      7641: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => i,
            children: () => n,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => u.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => C,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => B,
            getScale: () => p,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => b,
            isEventHandled: () => D,
            isFocused: () => v,
            pxToRem: () => f,
            remToPx: () => A,
            resize: () => _,
            sendEvent: () => s.qP,
            setAnimateWindow: () => h,
            setEventHandled: () => F,
            setInputPaddingsRem: () => o,
            setSidePaddingsRem: () => m,
            whenTutorialReady: () => y,
          }));
        var n = a(3722),
          r = a(6112),
          u = a(6538),
          s = a(8566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function o(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, a, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, a, n);
        }
        function c(e, t, a) {
          return viewEnv.addDataChangedCallback(e, t, a);
        }
        function m(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function _(e, t, a = "px") {
          return "rem" === a ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: A(t.x), y: A(t.y) };
        }
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function p() {
          return viewEnv.getScale();
        }
        function f(e) {
          return viewEnv.pxToRem(e);
        }
        function A(e) {
          return viewEnv.remToPx(e);
        }
        function h(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function v() {
          return viewEnv.isFocused();
        }
        function b() {
          return viewEnv.isClientAccessible();
        }
        function F() {
          return viewEnv.setEventHandled();
        }
        function D() {
          return viewEnv.isEventHandled();
        }
        function C() {
          viewEnv.forceTriggerMouseMove();
        }
        function B() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(r.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === r.W[t]), e),
            {},
          ),
          S = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          y = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : u.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, a) => {
        "use strict";
        a.d(t, { qP: () => l });
        const n = ["args"];
        const r = 2,
          u = 16,
          s = 32,
          i = 64,
          o = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const u = t.args,
                s = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    n,
                    r = {},
                    u = Object.keys(e);
                  for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                  return r;
                })(t, n);
              return void 0 !== u
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, s, {
                      arguments:
                        ((r = u),
                        Object.entries(r).map(([e, t]) => {
                          const a = "GFValueProxy";
                          switch (typeof t) {
                            case "number":
                              return { __Type: a, name: e, number: t };
                            case "boolean":
                              return { __Type: a, name: e, bool: t };
                            default:
                              return { __Type: a, name: e, string: t.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, s));
            }
            return viewEnv.handleViewEvent({ __Type: a, type: e });
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
              o(u, { isMouseEvent: !0, on: e });
            },
          };
      },
      5521: (e, t, a) => {
        "use strict";
        let n, r;
        (a.d(t, { n: () => n }),
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
      1358: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => u });
        var n = a(3138);
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
          addCallback(e, t, a = 0, r = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const u = n.O.view.addModelObserver(e, a, r);
            return (
              u > 0
                ? ((this._callbacks[u] = t),
                  a > 0 && (this._views[a] ? this._views[a].push(u) : (this._views[a] = [u])))
                : console.error("Can't add callback for model:", e),
              u
            );
          }
          removeCallback(e, t = 0) {
            let a = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((a = viewEnv.removeDataChangedCallback(e, t)), delete this._callbacks[e]),
              a || console.error("Can't remove callback by id:", e),
              a
            );
          }
          _emmitDataChanged(e, t, a) {
            a.forEach((a) => {
              const n = this._callbacks[a];
              void 0 !== n && n(e, t);
            });
          }
        }
        r.__instance = void 0;
        const u = r;
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
      4179: (e, t, a) => {
        "use strict";
        a.d(t, {
          Sw: () => u.Z,
          kH: () => d,
          B3: () => l,
          Z5: () => s,
          lf: () => m,
          cy: () => i,
          B0: () => o,
          ry: () => A,
          Eu: () => h,
        });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: a }) => {
                  let n = e.target;
                  do {
                    if (n === t) return;
                    n = n.parentNode;
                  } while (n);
                  a();
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
            const a = e,
              n = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== a || t !== n,
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
        var u = a(1358);
        const s = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          i = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, a) => userLocale.getTimeFormat(e, t, void 0 === a || a),
            getTimeString: (e, t, a) => userLocale.getTimeString(e, t, void 0 === a || a),
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
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = a(5521),
          E = a(3138);
        const g = ["args"];
        function p(e, t, a, n, r, u, s) {
          try {
            var i = e[u](s),
              o = i.value;
          } catch (e) {
            return void a(e);
          }
          i.done ? t(o) : Promise.resolve(o).then(n, r);
        }
        const f = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          A = (function () {
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
                    a = arguments;
                  return new Promise(function (n, r) {
                    var u = e.apply(t, a);
                    function s(e) {
                      p(u, n, r, s, i, "next", e);
                    }
                    function i(e) {
                      p(u, n, r, s, i, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          h = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          v = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                u = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    n,
                    r = {},
                    u = Object.keys(e);
                  for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                  return r;
                })(t, g);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, u, {
                      arguments:
                        ((n = r),
                        Object.entries(n).map(([e, t]) => {
                          const a = { __Type: "GFValueProxy", name: e };
                          switch (typeof t) {
                            case "number":
                              a.number = t;
                              break;
                            case "boolean":
                              a.bool = t;
                              break;
                            default:
                              a.string = t.toString();
                          }
                          return a;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, u));
            } else viewEnv.handleViewEvent({ __Type: a, type: e });
            var n;
          },
          b = () => v(o.CLOSE),
          F = (e, t) => {
            e.keyCode === _.n.ESCAPE && t();
          };
        var D = a(7572);
        const C = r.instance,
          B = {
            DataTracker: u.Z,
            ViewModel: D.Z,
            ViewEventType: o,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: m,
            DateFormatType: d,
            makeGlobalBoundingBox: f,
            sendMoveEvent: (e) => v(o.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: b,
            sendClosePopOverEvent: () => v(o.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, a = 0) => {
              v(o.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: a,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, a, n, r = R.invalid("resId"), u) => {
              const s = E.O.view.getViewGlobalPosition(),
                i = a.getBoundingClientRect(),
                l = i.x,
                c = i.y,
                m = i.width,
                d = i.height,
                _ = {
                  x: E.O.view.pxToRem(l) + s.x,
                  y: E.O.view.pxToRem(c) + s.y,
                  width: E.O.view.pxToRem(m),
                  height: E.O.view.pxToRem(d),
                };
              v(o.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: r,
                direction: t,
                bbox: f(_),
                on: !0,
                args: u,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => F(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              F(e, b);
            },
            handleViewEvent: v,
            onBindingsReady: A,
            onLayoutReady: h,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(o.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(o.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(o.POP_OVER),
            dumpViewModel: function e(t) {
              const a = {};
              if ("object" != typeof t) return t;
              for (const n in t)
                if (Object.prototype.hasOwnProperty.call(t, n)) {
                  const r = Object.prototype.toString.call(t[n]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = t[n];
                    a[n] = [];
                    for (let t = 0; t < r.length; t++) a[n].push({ value: e(r[t].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (a[n] = e(t[n]))
                      : (a[n] = t[n]);
                }
              return a;
            },
            ClickOutsideManager: C,
            SystemLocale: s,
            UserLocale: i,
          };
        window.ViewEnvHelper = B;
      },
      7860: (e, t, a) => {
        "use strict";
        var n = {};
        (a.r(n),
          a.d(n, {
            Area: () => Nu,
            Bar: () => ku,
            DefaultScroll: () => Lu,
            Direction: () => pu,
            defaultSettings: () => fu,
            useHorizontalScrollApi: () => hu,
          }));
        var r = {};
        (a.r(r),
          a.d(r, {
            Area: () => um,
            Bar: () => am,
            Default: () => rm,
            useVerticalScrollApi: () => zc,
          }));
        var u = a(6179),
          s = a.n(u);
        const i = (e, t, a) =>
          t.extraLargeHeight ||
          t.largeHeight ||
          t.mediumHeight ||
          t.smallHeight ||
          t.extraSmallHeight
            ? (t.extraLargeHeight && a.extraLarge) ||
              (t.largeHeight && a.large) ||
              (t.mediumHeight && a.medium) ||
              (t.smallHeight && a.small) ||
              (t.extraSmallHeight && a.extraSmall)
              ? e
              : null
            : e;
        var o = a(3138);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function m(e, t, a) {
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
            })(e, a),
            r = (function (e, t) {
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
            })(t, a),
            u = Math.min(n, r);
          return {
            extraLarge: u === a.extraLarge.weight,
            large: u === a.large.weight,
            medium: u === a.medium.weight,
            small: u === a.small.weight,
            extraSmall: u === a.extraSmall.weight,
            extraLargeWidth: n === a.extraLarge.weight,
            largeWidth: n === a.large.weight,
            mediumWidth: n === a.medium.weight,
            smallWidth: n === a.small.weight,
            extraSmallWidth: n === a.extraSmall.weight,
            extraLargeHeight: r === a.extraLarge.weight,
            largeHeight: r === a.large.weight,
            mediumHeight: r === a.medium.weight,
            smallHeight: r === a.small.weight,
            extraSmallHeight: r === a.extraSmall.weight,
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
        const d = o.O.client.getSize("rem"),
          _ = d.width,
          E = d.height,
          g = Object.assign({ width: _, height: E }, m(_, E, l)),
          p = (0, u.createContext)(g),
          f = ["children"];
        const A = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, f);
          const n = (0, u.useContext)(p),
            r = n.extraLarge,
            s = n.large,
            o = n.medium,
            l = n.small,
            c = n.extraSmall,
            m = n.extraLargeWidth,
            d = n.largeWidth,
            _ = n.mediumWidth,
            E = n.smallWidth,
            g = n.extraSmallWidth,
            A = n.extraLargeHeight,
            h = n.largeHeight,
            v = n.mediumHeight,
            b = n.smallHeight,
            F = n.extraSmallHeight,
            D = { extraLarge: A, large: h, medium: v, small: b, extraSmall: F };
          if (a.extraLarge || a.large || a.medium || a.small || a.extraSmall) {
            if (a.extraLarge && r) return t;
            if (a.large && s) return t;
            if (a.medium && o) return t;
            if (a.small && l) return t;
            if (a.extraSmall && c) return t;
          } else {
            if (a.extraLargeWidth && m) return i(t, a, D);
            if (a.largeWidth && d) return i(t, a, D);
            if (a.mediumWidth && _) return i(t, a, D);
            if (a.smallWidth && E) return i(t, a, D);
            if (a.extraSmallWidth && g) return i(t, a, D);
            if (!(
              a.extraLargeWidth ||
              a.largeWidth ||
              a.mediumWidth ||
              a.smallWidth ||
              a.extraSmallWidth
            )) {
              if (a.extraLargeHeight && A) return t;
              if (a.largeHeight && h) return t;
              if (a.mediumHeight && v) return t;
              if (a.smallHeight && b) return t;
              if (a.extraSmallHeight && F) return t;
            }
          }
          return null;
        };
        A.defaultProps = {
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
        (0, u.memo)(A);
        const h = (e) => {
            const t = (0, u.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          v = (0, u.memo)(({ children: e }) => {
            const t = (0, u.useContext)(p),
              a = (0, u.useState)(t),
              n = a[0],
              r = a[1],
              i = (0, u.useCallback)((e, t) => {
                const a = o.O.view.pxToRem(e),
                  n = o.O.view.pxToRem(t);
                r(Object.assign({ width: a, height: n }, m(a, n, l)));
              }, []);
            (h(() => {
              engine.on("clientResized", i);
            }),
              (0, u.useEffect)(() => () => engine.off("clientResized", i), [i]));
            const c = (0, u.useMemo)(() => Object.assign({}, n), [n]);
            return s().createElement(p.Provider, { value: c }, e);
          });
        var b = a(6483),
          F = a.n(b),
          D = a(926),
          C = a.n(D);
        let B, w, S;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.small.width)] = "Small"),
            (e[(e.Medium = l.medium.width)] = "Medium"),
            (e[(e.Large = l.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(B || (B = {})),
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
          })(S || (S = {})));
        const y = () => {
            const e = (0, u.useContext)(p),
              t = e.width,
              a = e.height,
              n = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return B.ExtraLarge;
                  case e.large:
                    return B.Large;
                  case e.medium:
                    return B.Medium;
                  case e.small:
                    return B.Small;
                  case e.extraSmall:
                    return B.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), B.ExtraSmall);
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
              s = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return S.ExtraLarge;
                  case e.largeHeight:
                    return S.Large;
                  case e.mediumHeight:
                    return S.Medium;
                  case e.smallHeight:
                    return S.Small;
                  case e.extraSmallHeight:
                    return S.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), S.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: n,
              mediaWidth: r,
              mediaHeight: s,
              remScreenWidth: t,
              remScreenHeight: a,
            };
          },
          x = ["children", "className"];
        function P() {
          return (
            (P =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            P.apply(this, arguments)
          );
        }
        const k = {
            [w.ExtraSmall]: "",
            [w.Small]: C().SMALL_WIDTH,
            [w.Medium]: `${C().SMALL_WIDTH} ${C().MEDIUM_WIDTH}`,
            [w.Large]: `${C().SMALL_WIDTH} ${C().MEDIUM_WIDTH} ${C().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${C().SMALL_WIDTH} ${C().MEDIUM_WIDTH} ${C().LARGE_WIDTH} ${C().EXTRA_LARGE_WIDTH}`,
          },
          T = {
            [S.ExtraSmall]: "",
            [S.Small]: C().SMALL_HEIGHT,
            [S.Medium]: `${C().SMALL_HEIGHT} ${C().MEDIUM_HEIGHT}`,
            [S.Large]: `${C().SMALL_HEIGHT} ${C().MEDIUM_HEIGHT} ${C().LARGE_HEIGHT}`,
            [S.ExtraLarge]: `${C().SMALL_HEIGHT} ${C().MEDIUM_HEIGHT} ${C().LARGE_HEIGHT} ${C().EXTRA_LARGE_HEIGHT}`,
          },
          L = {
            [B.ExtraSmall]: "",
            [B.Small]: C().SMALL,
            [B.Medium]: `${C().SMALL} ${C().MEDIUM}`,
            [B.Large]: `${C().SMALL} ${C().MEDIUM} ${C().LARGE}`,
            [B.ExtraLarge]: `${C().SMALL} ${C().MEDIUM} ${C().LARGE} ${C().EXTRA_LARGE}`,
          },
          N = (e) => {
            let t = e.children,
              a = e.className,
              n = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, x);
            const r = y(),
              u = r.mediaWidth,
              i = r.mediaHeight,
              o = r.mediaSize;
            return s().createElement("div", P({ className: F()(a, k[u], T[i], L[o]) }, n), t);
          },
          I = ["children"];
        const M = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, I);
          return s().createElement(v, null, s().createElement(N, a, t));
        };
        var O = a(493),
          H = a.n(O),
          W = a(3403);
        function $(e) {
          engine.call("PlaySound", e);
        }
        const z = {
            playHighlight() {
              $("highlight");
            },
            playClick() {
              $("play");
            },
            playYes() {
              $("yes1");
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
          G = [
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
        function q() {
          return (
            (q =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            q.apply(this, arguments)
          );
        }
        class V extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && $(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && $(this.props.soundClick));
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
              a = e.onClick,
              n = e.goto,
              r = e.side,
              u = e.type,
              i = e.classNames,
              o = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              m = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var a,
                    n,
                    r = {},
                    u = Object.keys(e);
                  for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                  return r;
                })(e, G)),
              _ = F()(U.base, U[`base__${u}`], U[`base__${r}`], null == i ? void 0 : i.base),
              E = F()(U.icon, U[`icon__${u}`], U[`icon__${r}`], null == i ? void 0 : i.icon),
              g = F()(U.glow, null == i ? void 0 : i.glow),
              p = F()(U.caption, U[`caption__${u}`], null == i ? void 0 : i.caption),
              f = F()(U.goto, null == i ? void 0 : i.goto);
            return s().createElement(
              "div",
              q(
                {
                  className: _,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(m),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: a,
                },
                d,
              ),
              "info" !== u && s().createElement("div", { className: U.shine }),
              s().createElement(
                "div",
                { className: E },
                s().createElement("div", { className: g }),
              ),
              s().createElement("div", { className: p }, t),
              n && s().createElement("div", { className: f }, n),
            );
          }
        }
        V.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var j = a(5521),
          X = a(4179);
        const Q = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function Y(e = j.n.NONE, t = Q, a = !1) {
          (0, u.useEffect)(() => {
            if (e !== j.n.NONE)
              return (
                window.addEventListener("keydown", n, a),
                () => {
                  window.removeEventListener("keydown", n, a);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (o.O.view.isEventHandled()) return;
                (o.O.view.setEventHandled(), t(n), a && n.stopPropagation());
              }
            }
          }, [t, e, a]);
        }
        const K = "page_heading_05",
          Z = "page_close_a4",
          J = ({ onClose: e, className: t }) => {
            var a;
            return (
              (a = e),
              Y(j.n.ESCAPE, a),
              s().createElement(
                "div",
                { className: F()(Z, t) },
                s().createElement(V, {
                  caption: R.strings.comp7.closeButtonLabel(),
                  type: "close",
                  side: "right",
                  onClick: e,
                }),
              )
            );
          },
          ee = () => o.O.client.graphicsQuality.isHigh();
        function te() {}
        function ae() {
          return !1;
        }
        console.log;
        var ne = a(9174);
        function re(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return ue(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return ue(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function ue(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, n = new Array(t); a < t; a++) n[a] = e[a];
          return n;
        }
        const se = (e) => (0 === e ? window : window.subViews.get(e));
        const ie = () => (e, t) => {
            const a = (0, u.createContext)({});
            return [
              function ({ mode: n = "real", options: r, children: i, mocks: l }) {
                const c = (0, u.useRef)([]),
                  m = (a, n, r) => {
                    var u;
                    const s = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: a = se,
                        context: n = "model",
                      } = {}) {
                        const r = new Map();
                        function u(e, t = 0) {
                          viewEnv.removeDataChangedCallback(e, t)
                            ? r.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, t, a) => {
                            a.forEach((t) => {
                              const a = r.get(t);
                              void 0 !== a && a(e);
                            });
                          });
                        });
                        const s = (e) => {
                          const r = a(t),
                            u = n.split(".").reduce((e, t) => e[t], r);
                          return "string" != typeof e || 0 === e.length
                            ? u
                            : e.split(".").reduce((e, t) => {
                                const a = e[t];
                                return "function" == typeof a ? a.bind(e) : a;
                              }, u);
                        };
                        return {
                          subscribe: (a, u) => {
                            const i = "string" == typeof u ? `${n}.${u}` : n,
                              l = o.O.view.addModelObserver(i, t, !0);
                            return (r.set(l, a), e && a(s(u)), l);
                          },
                          readByPath: s,
                          createCallback: (e, t) => {
                            const a = s(t);
                            return (...t) => {
                              a(e(...t));
                            };
                          },
                          createCallbackNoArgs: (e) => {
                            const t = s(e);
                            return () => {
                              t();
                            };
                          },
                          dispose: function () {
                            for (var e, a = re(r.keys()); !(e = a()).done;) u(e.value, t);
                          },
                          unsubscribe: u,
                        };
                      })(n),
                      i =
                        "real" === a
                          ? s
                          : Object.assign({}, s, {
                              readByPath:
                                null != (u = null == r ? void 0 : r.getter) ? u : () => {},
                            }),
                      l = (e) =>
                        "mocks" === a ? (null == r ? void 0 : r.getter(e)) : i.readByPath(e),
                      m = (e) => c.current.push(e),
                      d = e({
                        mode: a,
                        readByPath: l,
                        externalModel: i,
                        observableModel: {
                          array: (e, t) => {
                            const n = null != t ? t : l(e),
                              r = ne.LO.box(n, { equals: ae });
                            return (
                              "real" === a &&
                                i.subscribe(
                                  (0, ne.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, t) => {
                            const n = null != t ? t : l(e),
                              r = ne.LO.box(n, { equals: ae });
                            return (
                              "real" === a &&
                                i.subscribe(
                                  (0, ne.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, t) => {
                            const n = l(t);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, t) => ((e[t] = ne.LO.box(n[t], {})), e), {});
                              return (
                                "real" === a &&
                                  i.subscribe(
                                    (0, ne.aD)((t) => {
                                      e.forEach((e) => {
                                        r[e].set(t[e]);
                                      });
                                    }),
                                    t,
                                  ),
                                r
                              );
                            }
                            {
                              const r = e,
                                u = Object.entries(r),
                                s = u.reduce((e, [t, a]) => ((e[a] = ne.LO.box(n[t], {})), e), {});
                              return (
                                "real" === a &&
                                  i.subscribe(
                                    (0, ne.aD)((e) => {
                                      u.forEach(([t, a]) => {
                                        s[a].set(e[t]);
                                      });
                                    }),
                                    t,
                                  ),
                                s
                              );
                            }
                          },
                        },
                        cleanup: m,
                      }),
                      _ = { mode: a, model: d, externalModel: i, cleanup: m };
                    return {
                      model: d,
                      controls: "mocks" === a && r ? r.controls(_) : t(_),
                      externalModel: i,
                      mode: a,
                    };
                  },
                  d = (0, u.useRef)(!1),
                  _ = (0, u.useState)(n),
                  E = _[0],
                  g = _[1],
                  p = (0, u.useState)(() => m(n, r, l)),
                  f = p[0],
                  A = p[1];
                return (
                  (0, u.useEffect)(() => {
                    d.current ? A(m(E, r, l)) : (d.current = !0);
                  }, [l, E, r]),
                  (0, u.useEffect)(() => {
                    g(n);
                  }, [n]),
                  (0, u.useEffect)(
                    () => () => {
                      (f.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [f],
                  ),
                  s().createElement(a.Provider, { value: f }, i)
                );
              },
              () => (0, u.useContext)(a),
            ];
          },
          oe = ie()(
            ({ observableModel: e }) => ({
              root: e.object(),
              season: e.primitives(
                ["startTimestamp", "endTimestamp", "serverTimestamp", "state"],
                "season",
              ),
              year: e.primitives(["state"], "year"),
            }),
            ({ externalModel: e }) => ({
              pollServerTime: e.createCallbackNoArgs("season.pollServerTime"),
            }),
          ),
          le = oe[0],
          ce = oe[1];
        let me;
        !(function (e) {
          ((e[(e.Progression = 0)] = "Progression"),
            (e[(e.RankRewards = 1)] = "RankRewards"),
            (e[(e.WeeklyQuests = 2)] = "WeeklyQuests"),
            (e[(e.Leaderboard = 3)] = "Leaderboard"));
        })(me || (me = {}));
        const de = {
            [me.Progression]: "progression",
            [me.RankRewards]: "rankRewards",
            [me.WeeklyQuests]: "weeklyQuests",
            [me.Leaderboard]: "leaderboard",
          },
          _e = { from: { opacity: 0 }, to: { opacity: 1 }, delay: 300, config: { duration: 300 } };
        var Ee = a(3946);
        const ge = ie()(
            ({ observableModel: e }) => {
              const t = { root: e.object() },
                a = e.object("progressionModel.qualificationModel"),
                n = (0, Ee.Om)(
                  () => t.root.get().pageViewId === me.Progression && a.get().isActive,
                );
              return Object.assign({}, t, { computes: { isProgressionInQualification: n } });
            },
            ({ externalModel: e, cleanup: t }) => {
              const a = window.subViews.addChildChangedCallback(me.Leaderboard);
              return (
                t(() => {
                  window.subViews.removeChildChangedCallback(a);
                }),
                {
                  close: e.createCallbackNoArgs("onClose"),
                  openInfoPage: e.createCallbackNoArgs("onInfoPageOpen"),
                }
              );
            },
          ),
          pe = ge[0],
          fe = ge[1];
        function Ae(e, t) {
          var a;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (a = e[t]) ? void 0 : a.value;
        }
        const he = Ae;
        function ve(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function be(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, a, n) => t(null == e ? void 0 : e.value, a, n));
        }
        function Fe(e, t = 0, a = e.length - 1) {
          return {
            [Symbol.iterator]() {
              let n = Math.max(t, 0);
              const r = Math.min(
                a,
                (function (e) {
                  return Math.max(0, e.length - 1);
                })(e),
              );
              return {
                next: function () {
                  if (n > r) return { done: !0, value: null };
                  const t = e[n++];
                  return t ? { value: ve(t), done: !1 } : { done: !0, value: null };
                },
              };
            },
          };
        }
        function De(e, t) {
          for (let a = 0; a < e.length; a++) {
            const n = ve(e[a]);
            if (t(n, a, e)) return n;
          }
        }
        function Ce(e, t) {
          for (let a = 0; a < e.length; a++) {
            if (t(he(e, a), a, e)) return a;
          }
        }
        const Be = R.images.comp7.gui.maps.icons.comp7.metaTabs,
          we = (e, t) => (t ? `${Be.$dyn(e)}` : `${Be.small.$dyn(e)}`),
          Se = ie()(
            ({ observableModel: e }) => {
              const t = { root: e.object() },
                a = e.array("items"),
                n = (0, Ee.Om)(
                  (e) => [
                    {
                      id: 0,
                      items: [
                        ...be(a.get(), ({ id: t, hasNotification: a }) =>
                          Object.assign(
                            { id: t, icon: we(de[t], e) },
                            a && { notification: { type: "dot" } },
                          ),
                        ),
                        { id: -1, icon: we("aboutComp7", e) },
                      ],
                    },
                  ],
                  { equals: ae },
                );
              return Object.assign({}, t, { computes: { tabs: n } });
            },
            ({ externalModel: e }) => ({
              changeSidebarTab: e.createCallback((e) => ({ tabId: e }), "onSideBarTabChange"),
            }),
          ),
          ye = Se[0],
          Re = Se[1],
          xe = (e) => {
            let t,
              a = null;
            return (
              (a = requestAnimationFrame(() => {
                a = requestAnimationFrame(() => {
                  ((a = null), (t = e()));
                });
              })),
              () => {
                ("function" == typeof t && t(), null !== a && cancelAnimationFrame(a));
              }
            );
          };
        var Pe = a(7030);
        const ke = {
            base: "Frame_base_af",
            base__small: "Frame_base__small_f0",
            base__medium: "Frame_base__medium_05",
            border: "Frame_border_17",
            border__top: "Frame_border__top_f7",
            border__bottom: "Frame_border__bottom_52",
            arrow: "Frame_arrow_c3",
          },
          Te = s().forwardRef(function (
            { classNames: e, arrowRef: t, size: a = "medium", className: n },
            r,
          ) {
            return s().createElement(
              "div",
              { className: F()(ke.base, ke[`base__${a}`], n), ref: r },
              s().createElement("div", {
                className: F()(
                  ke.border,
                  ke.border__top,
                  null == e ? void 0 : e.border,
                  null == e ? void 0 : e.borderTop,
                ),
              }),
              s().createElement("div", {
                className: F()(
                  ke.border,
                  ke.border__bottom,
                  null == e ? void 0 : e.border,
                  null == e ? void 0 : e.borderBottom,
                ),
              }),
              s().createElement("div", {
                className: F()(ke.arrow, null == e ? void 0 : e.arrow),
                ref: t,
              }),
            );
          }),
          Le = {
            base: "Tab_base_cd",
            base__small: "Tab_base__small_bf",
            base__medium: "Tab_base__medium_96",
            base__active: "Tab_base__active_7e",
            highlight: "Tab_highlight_b6",
            icon: "Tab_icon_28",
            icon__small: "Tab_icon__small_48",
            icon__medium: "Tab_icon__medium_73",
            notification: "Tab_notification_86",
            notification__symbol: "Tab_notification__symbol_9b",
            notification__small: "Tab_notification__small_92",
            notification__dot: "Tab_notification__dot_51",
            notification__medium: "Tab_notification__medium_e6",
            notification__large: "Tab_notification__large_6b",
          },
          Ne = { mouseEnter: "highlight", click: "play" },
          Ie = s().forwardRef(function (
            {
              id: e,
              isActive: t,
              className: a,
              classNames: n,
              sounds: r = Ne,
              notification: u,
              icon: i,
              size: o,
              additionContent: l,
              onClick: c,
              onMouseEnter: m,
              onMouseLeave: d,
              WrapperElement: _,
            },
            E,
          ) {
            const g = (e, a) => {
                !t && r[a] && $(r[a]);
              },
              p = s().createElement(
                "div",
                {
                  className: F()(
                    Le.base,
                    Le[`base__${o}`],
                    t && F()(Le.base__active, null == n ? void 0 : n.activeTab),
                    a,
                  ),
                  onClick: ((e) => () => {
                    (g(0, "click"), null == c || c(e));
                  })(e),
                  onMouseEnter: ((e) => () => {
                    (g(0, "mouseEnter"), null == m || m(e));
                  })(e),
                  onMouseLeave: ((e) => () => {
                    (g(0, "mouseLeave"), null == d || d(e));
                  })(e),
                  ref: t ? E : null,
                },
                s().createElement("div", {
                  className: F()(Le.highlight, null == n ? void 0 : n.highlight),
                }),
                "function" == typeof i && o
                  ? i(o)
                  : s().createElement("div", {
                      className: F()(Le.icon, Le[`icon__${o}`], null == n ? void 0 : n.icon),
                      style: { backgroundImage: `url(${i})` },
                    }),
                l && l({ id: e, isActive: t, size: o }),
                u &&
                  s().createElement(
                    "div",
                    {
                      className: F()(
                        Le.notification,
                        Le[`notification__${u.type}`],
                        u.size ? Le[`notification__${u.size}`] : Le.notification__medium,
                        null == n ? void 0 : n.notification,
                      ),
                    },
                    "dot" !== u.type && u.value,
                  ),
              );
            return _ ? s().createElement(_, { key: e, id: e }, p) : p;
          }),
          Me = {
            base: "VerticalTabs_base_41",
            title: "VerticalTabs_title_8c",
            group: "VerticalTabs_group_08",
            group__small: "VerticalTabs_group__small_69",
            group__medium: "VerticalTabs_group__medium_68",
          },
          Oe = s().memo(function ({
            active: e,
            tabs: t,
            sounds: a,
            className: n,
            classNames: r,
            size: i = "medium",
            additionContent: l,
            onClick: c,
            onMouseEnter: m,
            onMouseLeave: d,
            WrapperElement: _,
          }) {
            const E = (0, u.useRef)(null),
              g = (0, u.useRef)(null),
              p = (0, u.useRef)(null),
              f = (0, u.useRef)(null),
              A = (0, Pe.useSpring)(() => ({
                marginLeft: 0,
                onChange: (e) => {
                  const t = E.current;
                  t && (t.style.marginLeft = `${e.value.marginLeft}rem`);
                },
              }))[1],
              h = (0, Pe.useSpring)(() => ({
                opacity: 0,
                onChange: (e) => {
                  const t = E.current;
                  t && (t.style.opacity = `${e.value.opacity}`);
                },
              }))[1],
              v = (0, Pe.useSpring)(() => ({
                position: 0,
                onChange: (e) => {
                  const t = g.current;
                  t &&
                    (t.style.transform = `translateY(${e.value.position / o.O.view.getScale()}rem)`);
                },
                onStart: () => {
                  (A.start({
                    from: { marginLeft: 12 },
                    to: { marginLeft: 0 },
                    config: { duration: 50 },
                  }),
                    h.start({
                      from: { opacity: 1 },
                      to: { opacity: 0 },
                      config: { duration: 50 },
                    }));
                },
                onRest: () => {
                  (A.start({
                    from: { marginLeft: 0 },
                    to: { marginLeft: 12 },
                    config: { duration: 150 },
                  }),
                    h.start({
                      from: { opacity: 0 },
                      to: { opacity: 1 },
                      config: { duration: 150 },
                    }));
                },
              }))[1],
              b = (0, u.useCallback)((e) => {
                if (null !== p.current && null !== f.current) {
                  e(p.current.getBoundingClientRect().top - f.current.getBoundingClientRect().top);
                }
              }, []);
            var D, C;
            return (
              (0, u.useEffect)(() => {
                b((e) => {
                  v.start({ position: e, config: { duration: 200 } });
                });
              }, [v, e, b]),
              (0, u.useEffect)(
                () =>
                  xe(() => {
                    b((e) => {
                      v.start({ position: e, immediate: !0 });
                    });
                  }),
                [v, b, i],
              ),
              (D = () => {
                b((e) => {
                  v.start({ position: e, config: { duration: 200 } });
                });
              }),
              (C = [v, b]),
              (0, u.useEffect)(() => {
                let e = () => {};
                const t = () => {
                  (e(), (e = xe(D)));
                };
                return (
                  window.addEventListener("resize", t),
                  () => {
                    (e(), window.removeEventListener("resize", t));
                  }
                );
              }, C),
              s().createElement(
                "div",
                { className: F()(Me.base, n), ref: f },
                t.map(({ id: t, items: n, title: u, groupClassNames: o }) =>
                  s().createElement(
                    "div",
                    {
                      key: t,
                      className: F()(Me.group, Me[`group__${i}`], null == o ? void 0 : o.group),
                    },
                    u &&
                      s().createElement(
                        "div",
                        { className: F()(Me.title, null == o ? void 0 : o.title) },
                        u,
                      ),
                    n.map(({ id: t, icon: n, notification: u }) =>
                      s().createElement(Ie, {
                        key: t,
                        id: t,
                        icon: n,
                        notification: u,
                        ref: p,
                        sounds: a,
                        isActive: e === t,
                        size: i,
                        className: null == r ? void 0 : r.tab,
                        classNames: r,
                        additionContent: l,
                        onMouseEnter: m,
                        onMouseLeave: d,
                        onClick: c,
                        WrapperElement: _,
                      }),
                    ),
                  ),
                ),
                s().createElement(Te, {
                  arrowRef: E,
                  ref: g,
                  size: i,
                  className: null == r ? void 0 : r.frame,
                  classNames: r,
                }),
              )
            );
          }),
          He = [
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
            const a = { __Type: "GFValueProxy", name: e };
            switch (typeof t) {
              case "number":
                a.number = t;
                break;
              case "boolean":
                a.bool = t;
                break;
              case "undefined":
                break;
              default:
                a.string = t.toString();
            }
            return a;
          });
        }
        const $e = (e, t, a = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: X.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                a,
              ),
            );
          },
          ze = (e) => {
            let t = e.children,
              a = e.contentId,
              n = e.args,
              r = e.onMouseEnter,
              s = e.onMouseLeave,
              i = e.onMouseDown,
              o = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              m = e.ignoreMouseClick,
              d = void 0 !== m && m,
              _ = e.decoratorId,
              E = void 0 === _ ? 0 : _,
              g = e.isEnabled,
              p = void 0 === g || g,
              f = e.targetId,
              A = void 0 === f ? 0 : f,
              h = e.onShow,
              v = e.onHide,
              b = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, He);
            const F = (0, u.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              D = (0, u.useMemo)(
                () =>
                  A ||
                  ((e = 1) => {
                    const t = new Error().stack;
                    let a,
                      n = R.invalid("resId");
                    return (
                      t &&
                        ((a = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== a &&
                          window.subViews[a] &&
                          (n = window.subViews[a].id)),
                      { caller: a, stack: t, resId: n }
                    );
                  })().resId,
                [A],
              ),
              C = (0, u.useCallback)(() => {
                (F.current.isVisible && F.current.timeoutId) ||
                  ($e(a, E, { isMouseEvent: !0, on: !0, arguments: We(n) }, D),
                  h && h(),
                  (F.current.isVisible = !0));
              }, [a, E, n, D, h]),
              B = (0, u.useCallback)(() => {
                if (F.current.isVisible || F.current.timeoutId) {
                  const e = F.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (F.current.timeoutId = 0)),
                    $e(a, E, { on: !1 }, D),
                    F.current.isVisible && v && v(),
                    (F.current.isVisible = !1));
                }
              }, [a, E, D, v]),
              w = (0, u.useCallback)((e) => {
                F.current.isVisible &&
                  ((F.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (F.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(F.current.prevTarget) && B();
                  }, 200)));
              }, []);
            ((0, u.useEffect)(() => {
              const e = F.current.hideTimerId;
              return (
                document.addEventListener("wheel", w, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", w, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, u.useEffect)(() => {
                !1 === p && B();
              }, [p, B]),
              (0, u.useEffect)(
                () => (
                  window.addEventListener("mouseleave", B),
                  () => {
                    (window.removeEventListener("mouseleave", B), B());
                  }
                ),
                [B],
              ));
            return p
              ? (0, u.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((F.current.timeoutId = window.setTimeout(C, c ? 100 : 400)),
                            r && r(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (B(), null == s || s(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === d && B(), null == o || o(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === d && B(), null == i || i(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    b,
                  ),
                )
              : t;
            var S;
          },
          Ue = ["children", "body", "header", "note", "alert", "args"];
        function Ge() {
          return (
            (Ge =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ge.apply(this, arguments)
          );
        }
        const qe = R.views.common.tooltip_window.simple_tooltip_content,
          Ve = (e) => {
            let t = e.children,
              a = e.body,
              n = e.header,
              r = e.note,
              i = e.alert,
              o = e.args,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Ue);
            const c = (0, u.useMemo)(() => {
              const e = Object.assign({}, o, { body: a, header: n, note: r, alert: i });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [i, a, n, r, o]);
            return s().createElement(
              ze,
              Ge(
                {
                  contentId:
                    ((m = null == o ? void 0 : o.hasHtmlContent),
                    m ? qe.SimpleTooltipHtmlContent("resId") : qe.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              t,
            );
            var m;
          },
          je = Object.assign({}, de, { [-1]: "infoPage" }),
          Xe = R.strings.comp7.sidebar.tabs.tooltip,
          Qe = ({ children: e, id: t }) => {
            const a = ((e) => je[e])(t),
              n = `${Xe.header.$dyn(a)}`,
              r = `${Xe.body.$dyn(a)}`;
            return s().createElement(Ve, { header: n, body: r }, e);
          },
          Ye = { icon: "Tabs_icon_78" },
          Ke = (0, W.Pi)(({ pageView: e, className: t }) => {
            const a = Re(),
              n = a.model,
              r = a.controls,
              i = fe().controls,
              o = y().mediaSize >= B.Medium,
              l = n.computes.tabs(o),
              c = o ? "medium" : "small",
              m = (0, u.useCallback)(
                (e) => {
                  -1 !== e ? r.changeSidebarTab(e) : i.openInfoPage();
                },
                [r, i],
              );
            return s().createElement(Oe, {
              tabs: l,
              onClick: m,
              active: e,
              size: c,
              className: t,
              classNames: Ye,
              WrapperElement: Qe,
            });
          });
        let Ze, Je, et, tt;
        (!(function (e) {
          ((e.Initialization = "initialization"),
            (e.Loading = "loading"),
            (e.ForceLoading = "forceLoading"),
            (e.Loaded = "loaded"));
        })(Ze || (Ze = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.Loading = "loading"),
              (e.Loaded = "loaded"),
              (e.Failed = "failed"));
          })(Je || (Je = {})),
          (function (e) {
            ((e.Initialization = "initialization"), (e.Loaded = "loaded"), (e.Failed = "failed"));
          })(et || (et = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.BrowserLoading = "browserLoading"),
              (e.PageLoading = "pageLoading"),
              (e.ForceLoading = "forceLoading"),
              (e.PageFailed = "pageFailed"),
              (e.TextureFailed = "textureFailed"),
              (e.Loaded = "loaded"));
          })(tt || (tt = {})));
        (Ze.Initialization, Je.Initialization);
        const at = (e) => e > 0,
          nt = (e) => !at(e);
        function rt(e, t) {
          var a;
          if (nt(e)) return void console.warn("Invalid id, should be greater than zero", e);
          const n = 0 === t.scale ? 1e-5 : null != (a = t.scale) ? a : 1;
          return o.O.view.getBrowserTexturePath(e, Math.max(t.width, 1), Math.max(t.height, 1), n);
        }
        const ut = ie()(
            ({ observableModel: e }) => {
              const t = e.object(),
                a = (0, Ee.Om)(() =>
                  (function ({ pageState: e, browserState: t, texState: a }) {
                    return t === Ze.Initialization
                      ? tt.Initialization
                      : t === Ze.ForceLoading
                        ? tt.ForceLoading
                        : t === Ze.Loading
                          ? tt.BrowserLoading
                          : e === Je.Loaded && t === Ze.Loaded && a === et.Loaded
                            ? tt.Loaded
                            : a === et.Failed
                              ? tt.TextureFailed
                              : e === Je.Failed
                                ? tt.PageFailed
                                : tt.PageLoading;
                  })(t.get()),
                );
              return { root: t, getState: a };
            },
            ({ externalModel: e }) => ({
              blur: e.createCallbackNoArgs("unfocus"),
              focus: e.createCallbackNoArgs("focus"),
              createWebView: e.createCallbackNoArgs("createWebView"),
            }),
          ),
          st = ut[0],
          it = ut[1],
          ot = (e) => {
            (0, u.useEffect)(e, []);
          };
        function lt() {
          const e = (0, u.useRef)(0);
          var t;
          return (
            (t = () => {
              window.cancelAnimationFrame(e.current);
            }),
            (0, u.useEffect)(() => t, []),
            (0, u.useMemo)(
              () => ({
                run: (t) => {
                  (window.cancelAnimationFrame(e.current),
                    (e.current = window.requestAnimationFrame(() => {
                      e.current = window.requestAnimationFrame(() => {
                        (t(), (e.current = 0));
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
        const ct = "BrowserView_base_6b",
          mt = "BrowserView_texture_17",
          dt = "Spinner_base_87",
          _t = "Spinner_caption_cf",
          Et = "Spinner_gear_c4",
          gt = "Spinner_logo_bf",
          pt = ({ message: e, className: t, classNames: a }) =>
            s().createElement(
              "div",
              { className: F()(dt, t) },
              e &&
                s().createElement("div", { className: F()(_t, null == a ? void 0 : a.caption) }, e),
              s().createElement("div", { className: F()(Et, null == a ? void 0 : a.gear) }),
              s().createElement("div", { className: F()(gt, null == a ? void 0 : a.logo) }),
            ),
          ft = {
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
        let At, ht;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(At || (At = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(ht || (ht = {})));
        const vt = ({
          children: e,
          size: t,
          isFocused: a,
          type: n,
          disabled: r,
          mixClass: i,
          soundHover: o,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: m,
          onMouseDown: d,
          onMouseUp: _,
          onMouseLeave: E,
          onClick: g,
        }) => {
          const p = (0, u.useRef)(null),
            f = (0, u.useState)(a),
            A = f[0],
            h = f[1],
            v = (0, u.useState)(!1),
            b = v[0],
            D = v[1],
            C = (0, u.useState)(!1),
            B = C[0],
            w = C[1],
            S = (0, u.useCallback)(() => {
              r || (p.current && (p.current.focus(), h(!0)));
            }, [r]),
            y = (0, u.useCallback)(
              (e) => {
                A && null !== p.current && !p.current.contains(e.target) && h(!1);
              },
              [A],
            ),
            x = (0, u.useCallback)(
              (e) => {
                r || (g && g(e));
              },
              [r, g],
            ),
            P = (0, u.useCallback)(
              (e) => {
                r || (null !== o && $(o), c && c(e), w(!0));
              },
              [r, o, c],
            ),
            k = (0, u.useCallback)(
              (e) => {
                m && m(e);
              },
              [m],
            ),
            T = (0, u.useCallback)(
              (e) => {
                r || (_ && _(e), D(!1));
              },
              [r, _],
            ),
            L = (0, u.useCallback)(
              (e) => {
                r || (null !== l && $(l), d && d(e), a && S(), D(!0));
              },
              [r, l, d, S, a],
            ),
            N = (0, u.useCallback)(
              (e) => {
                r || (E && E(e), D(!1));
              },
              [r, E],
            ),
            I = F()(
              ft.base,
              ft[`base__${n}`],
              {
                [ft.base__disabled]: r,
                [ft[`base__${t}`]]: t,
                [ft.base__focus]: A,
                [ft.base__highlightActive]: b,
                [ft.base__firstHover]: B,
              },
              i,
            ),
            M = F()(ft.state, ft.state__default);
          return (
            (0, u.useEffect)(
              () => (
                document.addEventListener("mousedown", y),
                () => {
                  document.removeEventListener("mousedown", y);
                }
              ),
              [y],
            ),
            (0, u.useEffect)(() => {
              h(a);
            }, [a]),
            s().createElement(
              "div",
              {
                ref: p,
                className: I,
                onMouseEnter: P,
                onMouseMove: k,
                onMouseUp: T,
                onMouseDown: L,
                onMouseLeave: N,
                onClick: x,
              },
              n !== At.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: ft.back }),
                  s().createElement("span", { className: ft.texture }),
                ),
              s().createElement(
                "span",
                { className: M },
                s().createElement("span", { className: ft.stateDisabled }),
                s().createElement("span", { className: ft.stateHighlightHover }),
                s().createElement("span", { className: ft.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: ft.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        vt.defaultProps = {
          type: At.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const bt = (0, u.memo)(vt),
          Ft = "Error_base_46",
          Dt = "Error_alertIcon_04",
          Ct = "Error_errorCaption_f2",
          Bt = "Error_button_cd",
          wt = ({ errorBtnLabel: e, errorBtnClickHandler: t, errorMessage: a }) =>
            s().createElement(
              "div",
              { className: Ft },
              s().createElement("div", { className: Dt }),
              s().createElement("div", { className: Ct }, a),
              s().createElement(bt, { size: ht.medium, mixClass: Bt, onClick: t }, e),
            );
        wt.defaultProps = { errorBtnLabel: "", errorMessage: "" };
        const St = "Waiting_base_c5",
          yt = "Waiting_blackOverlay_55",
          Rt = ({
            message: e,
            isError: t,
            errorMessage: a,
            errorBtnLabel: n,
            errorBtnClickHandler: r,
            overlayAlpha: i,
          }) => {
            const o = s().createRef();
            return (
              (0, u.useEffect)(() => {
                const e = o.current;
                e && i && (e.style.opacity = i);
              }, [o, i]),
              s().createElement(
                "div",
                { className: St },
                s().createElement("div", { className: yt, ref: o }),
                t
                  ? s().createElement(wt, {
                      errorBtnLabel: n,
                      errorMessage: a,
                      errorBtnClickHandler: r,
                    })
                  : s().createElement(pt, { message: e }),
              )
            );
          };
        Rt.defaultProps = {
          isError: !1,
          message: "",
          overlayAlpha: "0.8",
          errorBtnLabel: R.strings.dialogs.disconnected.cancel(),
          errorMessage: "",
        };
        const xt = "DisplayBrowserState_base_e7",
          Pt = "DisplayBrowserState_error_4e",
          kt = "DisplayBrowserState_alertIcon_c4",
          Tt = "DisplayBrowserState_errorCaption_dd",
          Lt = ({ waitingText: e, className: t }) =>
            s().createElement(
              "div",
              { className: F()(xt, t) },
              s().createElement(Rt, { errorBtnClickHandler: te, message: e }),
            ),
          Nt = () =>
            s().createElement(
              "div",
              { className: Pt },
              s().createElement("div", { className: kt }),
              s().createElement(
                "div",
                { className: Tt },
                R.strings.dialogs.messenger.userInfoNotAvailable.title(),
              ),
            ),
          It = () =>
            s().createElement(
              "div",
              { className: Pt },
              s().createElement("div", { className: kt }),
              s().createElement(
                "div",
                { className: Tt },
                R.strings.dialogs.inGameBrowser.textureLoadingFailed.title(),
              ),
              s().createElement(
                "div",
                { className: Tt },
                R.strings.dialogs.inGameBrowser.textureLoadingFailed.message(),
              ),
            );
        function Mt(e) {
          const t = (0, u.useRef)(e);
          return (
            (function (e) {
              return e !== tt.BrowserLoading && e !== tt.PageLoading;
            })(e) && (t.current = e),
            t.current
          );
        }
        function Ot(e) {
          const t = (function (e) {
              const t = (0, u.useRef)(!1);
              return (
                (e !== tt.Loaded && e !== tt.PageFailed && e !== tt.TextureFailed) ||
                  (t.current = !0),
                t.current
              );
            })(e),
            a = Mt(e);
          return t ? a : e;
        }
        const Ht = ({ viewState: e, waitingText: t, waitingClassName: a }) => {
            switch (Ot(e)) {
              case tt.BrowserLoading:
              case tt.PageLoading:
              case tt.ForceLoading:
                return s().createElement(Lt, { waitingText: t, className: a });
              case tt.PageFailed:
                return s().createElement(Nt, null);
              case tt.TextureFailed:
                return s().createElement(It, null);
              default:
                return null;
            }
          },
          Wt = (e) =>
            "width" in e &&
            "height" in e &&
            "number" == typeof e.width &&
            "number" == typeof e.height;
        function $t(e) {
          return null != e ? e : viewEnv.getScale();
        }
        function zt(e) {
          const t = (0, u.useState)($t(e.scale)),
            a = t[0],
            n = t[1],
            r = (function (e) {
              return Wt(e) ? rt(e.id, e) : void 0;
            })(Object.assign({}, e, { scale: a })),
            s = (0, u.useState)(r),
            i = s[0],
            o = s[1],
            l = (0, u.useRef)(!1),
            c = "width" in e ? e.width : 0,
            m = "height" in e ? e.height : 0,
            d = lt();
          return (
            (0, u.useEffect)(() => {
              const t = () => {
                n($t(e.scale));
              };
              return (
                window.addEventListener("resize", t),
                () => {
                  window.removeEventListener("resize", t);
                }
              );
            }, [e.scale]),
            (0, u.useEffect)(() => {
              if (void 0 === r || 0 === c || 0 === m || r === i) return;
              const e = () => {
                o(r);
              };
              if (!1 === l.current) return ((l.current = !0), void e());
              const t = new Image(),
                a = () => {
                  d.run(e);
                };
              return (
                t.addEventListener("load", a),
                (t.src = r),
                () => {
                  (t.removeEventListener("load", a), (t.src = ""));
                }
              );
            }, [r, i]),
            i
          );
        }
        const Ut = s().memo(function (e) {
            const t = e.id,
              a = e.className,
              n = e.classNameTexture,
              r = e.waitingClassName,
              u = e.onMouseEnter,
              i = e.onMouseLeave,
              o = e.onMouseWheel,
              l = e.onMouseMove,
              c = e.onMouseDown,
              m = e.onMouseUp,
              d = e.renderStateDisplay,
              _ = e.viewState,
              E = e.statusCode,
              g = e.waitingText,
              p = e.scrollSpeed,
              f = void 0 === p ? 20 : p,
              A = zt(e);
            return s().createElement(
              "div",
              { className: F()(ct, a), onMouseEnter: u, onMouseLeave: i },
              A &&
                s().createElement("div", {
                  onWheel: o,
                  onMouseMove: l,
                  onMouseDown: c,
                  onMouseUp: m,
                  className: F()(ct, mt, n),
                  "data-browser-id": t,
                  "data-browser-scroll-speed": f,
                  style: { backgroundImage: `url(${A})` },
                }),
              "function" == typeof d
                ? d({ viewState: _, statusCode: E, waitingText: g, waitingClassName: r })
                : s().createElement(Ht, {
                    viewState: _,
                    statusCode: E,
                    waitingText: g,
                    waitingClassName: r,
                  }),
            );
          }),
          Gt = (e, t = []) => {
            const a = (0, u.useRef)(),
              n = (0, u.useCallback)((...t) => {
                (a.current && a.current(), (a.current = e(...t)));
              }, t);
            return (
              (0, u.useEffect)(
                () => () => {
                  a.current && a.current();
                },
                [n],
              ),
              n
            );
          },
          qt = "none-ref",
          Vt = "measured",
          jt = { type: "measuring" };
        function Xt() {
          return (
            (Xt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Xt.apply(this, arguments)
          );
        }
        const Qt = s().memo(function (e) {
          const t = (function () {
              const e = (0, u.useRef)(null),
                t = (0, u.useState)(jt),
                a = t[0],
                n = t[1],
                r = Gt(
                  () => (
                    n(jt),
                    xe(() => {
                      e.current
                        ? n({
                            type: Vt,
                            size: { width: e.current.offsetWidth, height: e.current.offsetHeight },
                          })
                        : n({ type: qt });
                    })
                  ),
                  [],
                );
              return (
                (0, u.useEffect)(
                  () => (
                    window.addEventListener("resize", r),
                    r(),
                    () => window.removeEventListener("resize", r)
                  ),
                  [r],
                ),
                [e, a, r]
              );
            })(),
            a = t[0],
            n = t[1];
          return s().createElement(
            "div",
            { ref: a, className: ct },
            s().createElement(
              Ut,
              Xt(
                {},
                e,
                (function (e, t = {}) {
                  return "measured" === e.type ? Object.assign({}, e.size, t) : t;
                })(n),
              ),
            ),
          );
        });
        function Yt() {
          return (
            (Yt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Yt.apply(this, arguments)
          );
        }
        const Kt = (0, W.Pi)(function (e) {
            const t = e.defaultWaitingText,
              a = e.className,
              n = e.waitingClassName,
              r = e.isLazy,
              i = void 0 === r || r,
              o = e.displayContentWhenLoading,
              l = void 0 === o || o,
              c = e.renderStateDisplay,
              m = e.onMouseEnter,
              d = e.onMouseLeave,
              _ = e.onMouseMove,
              E = e.onMouseWheel,
              g = e.onMouseDown,
              p = e.onMouseUp,
              f = it(),
              A = f.model,
              h = f.controls,
              v = A.root.get(),
              b = v.id,
              F = v.httpStatusCode,
              D = v.waitingMessage,
              C = A.getState(),
              B = l || C === tt.Loaded;
            (ot(() => {
              i && nt(b) && h.createWebView();
            }),
              (0, u.useEffect)(() => {
                at(b) && h.focus();
              }, [b, h]),
              ot(
                () => (
                  window.addEventListener("mouseleave", h.blur),
                  window.addEventListener("mouseenter", h.focus),
                  () => {
                    (window.removeEventListener("mouseleave", h.blur),
                      window.removeEventListener("mouseenter", h.focus));
                  }
                ),
              ));
            const w = (0, u.useMemo)(() => {
              const e = {
                onMouseEnter: m,
                onMouseLeave: d,
                onMouseMove: _,
                onMouseWheel: E,
                onMouseDown: g,
                onMouseUp: p,
              };
              return B
                ? Object.assign({}, e, {
                    onMouseEnter: (e) => {
                      (h.focus(), null == m || m(e));
                    },
                    onMouseLeave: (e) => {
                      (h.blur(), null == d || d(e));
                    },
                  })
                : e;
            }, [B, h, g, m, d, _, p, E]);
            if (nt(b)) return null;
            const S = Wt(e)
                ? (function (e, t) {
                    const a = {};
                    return (
                      t.forEach((t) => {
                        a[t] = e[t];
                      }),
                      a
                    );
                  })(e, ["width", "height"])
                : {},
              y = D.length > 0 ? D : t;
            return e.isFullSize
              ? s().createElement(
                  Qt,
                  Yt({}, w, {
                    id: b,
                    className: a,
                    waitingClassName: n,
                    statusCode: F,
                    viewState: C,
                    waitingText: y,
                    renderStateDisplay: c,
                  }),
                )
              : s().createElement(
                  Ut,
                  Yt({}, w, S, {
                    id: b,
                    className: a,
                    waitingClassName: n,
                    statusCode: F,
                    viewState: C,
                    waitingText: y,
                    renderStateDisplay: c,
                  }),
                );
          }),
          Zt = ["options", "mocks", "mode"];
        const Jt = (0, u.memo)(function (e) {
            let t = e.options,
              a = e.mocks,
              n = e.mode,
              r = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Zt);
            return s().createElement(
              st,
              { options: t, mocks: a, mode: n },
              s().createElement(Kt, r),
            );
          }),
          ea = "LeaderboardPage_base_4a",
          ta = () =>
            s().createElement(
              "div",
              { className: ea },
              s().createElement(Jt, { options: { rootId: me.Leaderboard }, isFullSize: !0 }),
            );
        let aa, na;
        (!(function (e) {
          ((e[(e.A = 1)] = "A"),
            (e[(e.B = 2)] = "B"),
            (e[(e.C = 3)] = "C"),
            (e[(e.D = 4)] = "D"),
            (e[(e.E = 5)] = "E"));
        })(aa || (aa = {})),
          (function (e) {
            ((e[(e.Achieved = 0)] = "Achieved"),
              (e[(e.Current = 1)] = "Current"),
              (e[(e.Inactive = 2)] = "Inactive"));
          })(na || (na = {})));
        const ra = (e, t) =>
          Object.keys(e).length === Object.keys(t).length &&
          Object.keys(e).every((a) => Object.prototype.hasOwnProperty.call(t, a) && e[a] === t[a]);
        let ua;
        function sa(e, t) {
          return e.replace(/\{\w+\}/g, (e) => String(t[e.slice(1, -1)]));
        }
        function ia(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const a = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(a, -a)]);
          });
        }
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(ua || (ua = {}));
        const oa = (e, t, a) => {
            if (a % 2) {
              const a = e.pop();
              return [...e, a + t];
            }
            return [...e, t];
          },
          la = (e, t, a) => {
            if (0 === a) return [t];
            if (a % 2) return [...e, " " === t ? " " : t];
            {
              const a = e.pop();
              return [...e, a + t];
            }
          },
          ca = (e, t, a = ua.left) => e.split(t).reduce(a === ua.left ? oa : la, []),
          ma = (() => {
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
          da = ["zh_cn", "zh_sg", "zh_tw"],
          _a = (e, t = ua.left) => {
            const a = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return da.includes(a)
              ? ma(e)
              : ((e, t = ua.left) => {
                  let a = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (ca(r, /( )/, t).forEach((e) => (a = a.concat(ca(e, n, ua.left)))), a);
                })(e, t);
          },
          Ea = R.strings.comp7.division,
          ga = { [aa.A]: "A", [aa.B]: "B", [aa.C]: "C", [aa.D]: "D", [aa.E]: "E" },
          pa = (e) => Ea.$dyn(ga[e]),
          fa = (e) => be(e, (e) => pa(e.name)).join(R.strings.comp7.listSeparator()),
          Aa = (e) => be(e, (e) => e.elitePercent).sort((e, t) => t - e)[0];
        let ha, va, ba;
        (!(function (e) {
          ((e.Previous = "previous"), (e.Current = "current"), (e.Future = "future"));
        })(ha || (ha = {})),
          (function (e) {
            ((e[(e.Page = 0)] = "Page"),
              (e[(e.Maps = 1)] = "Maps"),
              (e[(e.SeasonVehicles = 2)] = "SeasonVehicles"));
          })(va || (va = {})),
          (function (e) {
            ((e[(e.BASIC = 0)] = "BASIC"),
              (e[(e.TRANSFER = 1)] = "TRANSFER"),
              (e[(e.ELITE = 2)] = "ELITE"));
          })(ba || (ba = {})));
        const Fa = (e, t, a) => (e > t || a ? ha.Future : e < t ? ha.Previous : ha.Current),
          Da = (e) => ({ from: e[0].from, to: e[e.length - 1].to }),
          Ca = ie()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  qualificationModel: e.primitives(
                    ["isActive", "battlesCount", "maxBattlesCount", "isRatingCalculation"],
                    "qualificationModel",
                  ),
                  isRewardLayerVisible: ne.LO.box(!1),
                  isParallaxPreloaded: ne.LO.box(!1),
                },
                a = e.array("items"),
                n = e.array("qualificationModel.battles"),
                r = (0, Ee.Om)(
                  (e) => {
                    const t = Ae(a.get(), e);
                    if (!t) throw new Error(`item with index ${e} was not found`);
                    return { hasRankInactivity: t.hasRankInactivity, rank: t.rank };
                  },
                  { equals: ra },
                ),
                u = (0, Ee.Om)(
                  (e) => {
                    const t = Ae(a.get(), e);
                    if (!t) throw new Error(`rank with index ${e} was not found`);
                    const n = be(t.divisions, (e) => Object.assign({}, e));
                    if (n.length > 0) return Da(n);
                    throw new Error(`no basic divisions for rank with ${e}`);
                  },
                  { equals: ae },
                ),
                s = (0, Ee.Om)(
                  (e) => {
                    const t = Ae(a.get(), e);
                    if (!t) throw new Error(`item with index ${e} was not found`);
                    return be(t.divisions, (e) => Object.assign({}, e));
                  },
                  { equals: ae },
                ),
                i = (0, Ee.Om)(
                  (e, t) => {
                    const a = s(e);
                    if (!a) throw new Error(`divisions from rank index ${e} was not found`);
                    return a.filter((e) => e.type === t);
                  },
                  { equals: ae },
                ),
                o = (0, Ee.Om)(
                  (e) => {
                    const t = s(e);
                    return {
                      list: fa(t),
                      count: t.length,
                      currentDivisionIndex: Ce(t, (e) => e.state === na.Current),
                      elitePercent: Aa(t),
                    };
                  },
                  { equals: ra },
                ),
                l = (0, Ee.Om)(() => {
                  const e = t.root.get().currentItemIndex,
                    n = Ae(a.get(), e);
                  if (!n) throw new Error(`current item with currentItemIndex ${e} was not found`);
                  return n.hasRankInactivity;
                }),
                c = (0, Ee.Om)(
                  (e, a) => {
                    var n;
                    return {
                      state: Fa(e, t.root.get().currentItemIndex, a),
                      division:
                        null == (n = De(s(e), (e) => e.state === na.Current)) ? void 0 : n.name,
                    };
                  },
                  { equals: ra },
                ),
                m = (0, Ee.Om)(
                  (e) => {
                    const t = Ae(n.get(), e);
                    if (!t) throw new Error(`qualification battle with index ${e} was not found`);
                    return t;
                  },
                  { equals: ae },
                );
              return Object.assign({}, t, {
                computes: {
                  modelItems: (0, Ee.Om)(() =>
                    be(a.get(), (e) =>
                      Object.assign({}, e, {
                        divisions: be(e.divisions, (e) => Object.assign({}, e)),
                      }),
                    ),
                  ),
                  itemsLength: (0, Ee.Om)(() => a.get().length),
                  qualificationBattlesLength: (0, Ee.Om)(() => n.get().length),
                  item: r,
                  rankPointsDiapason: u,
                  qualificationBattle: m,
                  rankSettings: c,
                  hasCurrentItemRankInactivity: l,
                  divisions: s,
                  divisionsConfig: o,
                  divisionsByType: i,
                },
              });
            },
            ({ externalModel: e, model: t }) => {
              const a = (0, ne.aD)((e) => t.isRewardLayerVisible.set(e));
              return {
                setIsParallaxPreloaded: (0, ne.aD)((e) => t.isParallaxPreloaded.set(e)),
                setRewardLayerVisible: a,
                goToRankRewardsPage: e.createCallbackNoArgs(
                  "qualificationModel.onRankRewardsPageOpen",
                ),
                goToLeaderboardPage: e.createCallbackNoArgs("onLeaderboardLinkClick"),
              };
            },
          ),
          Ba = Ca[0],
          wa = Ca[1],
          Sa = "Heading_base_74",
          ya = ({ children: e, className: t }) =>
            s().createElement("div", { className: F()(Sa, t) }, e),
          Ra = (e, t) => {
            let a;
            const n = setTimeout(() => {
              a = e();
            }, t);
            return () => {
              ("function" == typeof a && a(), clearTimeout(n));
            };
          };
        let xa;
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
        })(xa || (xa = {}));
        const Pa = 60,
          ka = 3600,
          Ta = 86400;
        Date.now();
        const La = (0, u.memo)(({ datetime: e, format: t = xa.SHORT_DATE, localize: a = !0 }) =>
            ((e, t, a) => {
              switch (t) {
                case xa.SHORT_DATE:
                  return a
                    ? X.Z5.getDateFormat(e, X.kH.SHORT_FORMAT)
                    : X.cy.getTimeFormat("%d.%m.%y", e, !0);
                case xa.SHORT_TIME:
                  return a
                    ? X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)
                    : X.cy.getTimeFormat("%I:%M %p", e, !0);
                case xa.SHORT_DATE_TIME:
                  return a
                    ? `${X.Z5.getDateFormat(e, X.kH.SHORT_FORMAT)}, ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                    : X.cy.getTimeFormat("%d.%m.%y, %I:%M %p", e, !0);
                case xa.FULL_DATE:
                  return a
                    ? X.Z5.getDateFormat(e, X.kH.LONG_FORMAT)
                    : X.cy.getTimeFormat("%B %d, %Y", e, !0);
                case xa.FULL_DATE_TIME:
                  return a
                    ? `${X.Z5.getDateFormat(e, X.kH.LONG_FORMAT)}, ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                    : X.cy.getTimeFormat("%B %d, %Y, %I:%M %p", e, !0);
                case xa.MONTH:
                  return X.cy.getTimeFormat("%B", e, !0);
                case xa.MONTH_DATE:
                  return X.cy.getTimeFormat("%B %e", e, !0);
                case xa.DATE_MONTH:
                  return X.cy.getTimeFormat("%e %B", e, !0);
                case xa.MONTH_YEAR:
                  return X.cy.getTimeFormat("%B %Y", e, !0);
                case xa.WEEK_DAY:
                  return X.cy.getTimeFormat("%A", e, !0);
                case xa.WEEK_DAY_TIME:
                  return a
                    ? `${X.cy.getTimeFormat("%A", e, !0)} ${X.Z5.getTimeFormat(e, X.lf.SHORT_FORMAT)}`
                    : X.cy.getTimeFormat("%A, %I:%M %p", e, !0);
                case xa.YEAR:
                  return X.cy.getTimeFormat("%Y", e, !0);
                case xa.DATE_YEAR:
                  return X.cy.getTimeFormat("%d, %Y", e, !0);
              }
            })(e, t, a),
          ),
          Na = "FormatText_base_d0",
          Ia = ({ binding: e, text: t = "", classMix: a, alignment: n = ua.left }) =>
            null === t
              ? (console.error("FormatText was supplied with 'null'"), null)
              : s().createElement(
                  u.Fragment,
                  null,
                  t.split("\n").map((t, r) =>
                    s().createElement(
                      "div",
                      { className: F()(Na, a), key: `${t}-${r}` },
                      ((e, t, a) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (a && e in a ? a[e] : _a(e, t))))(t, n, e).map((e, t) =>
                        s().createElement(u.Fragment, { key: `${t}-${e}` }, e),
                      ),
                    ),
                  ),
                ),
          Ma = ["children"];
        function Oa() {
          return (
            (Oa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Oa.apply(this, arguments)
          );
        }
        const Ha = (e) => {
            let t = e.children,
              a = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Ma);
            return s().createElement(
              ze,
              Oa(
                {
                  contentId:
                    R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                      "resId",
                    ),
                  ignoreShowDelay: !0,
                },
                a,
              ),
              t,
            );
          },
          Wa = (e) => {
            const t = Math.floor(e);
            return {
              totalSecondsLeft: t,
              seconds: Math.floor(t % 60),
              minutes: Math.floor(t / 60) % 60,
              hours: Math.floor((t / 3600) % 24),
              totalDays: Math.floor(t / 86400),
            };
          },
          $a = "ActiveSeasonState_base_55",
          za = "ActiveSeasonState_calendarIcon_df",
          Ua = "ActiveSeasonState_divider_5b",
          Ga = R.strings.comp7.season,
          qa = (e, t) => ({
            startDate: s().createElement(La, { datetime: e, format: xa.SHORT_DATE }),
            endDate: s().createElement(La, { datetime: t, format: xa.SHORT_DATE }),
          }),
          Va = (e, t, a) => {
            const n = t - a,
              r = ((e, t) => Wa(e - t))(t, a);
            return n >= 604800
              ? s().createElement(Ia, { text: Ga.range(), binding: qa(e, t) })
              : n >= Ta
                ? s().createElement(Ia, { text: Ga.daysLeft(), binding: r })
                : n >= ka
                  ? s().createElement(Ia, { text: Ga.hoursLeft(), binding: r })
                  : n >= Pa
                    ? s().createElement(Ia, { text: Ga.minutesLeft(), binding: r })
                    : n >= 1
                      ? s().createElement(Ia, { text: Ga.secondsLeft(), binding: r })
                      : void 0;
          },
          ja = ({
            startTimestamp: e,
            endTimestamp: t,
            currentTimestamp: a,
            tooltipId: n = "",
            hasSeasonName: r = !0,
          }) =>
            s().createElement(
              Ha,
              { args: { tooltipId: n }, isEnabled: Boolean(n) },
              s().createElement(
                "div",
                { className: $a },
                s().createElement("div", { className: za }),
                r &&
                  s().createElement(
                    s().Fragment,
                    null,
                    Ga.name(),
                    s().createElement("div", { className: Ua }),
                  ),
                Va(e, t, a),
              ),
            ),
          Xa = "ScheduleSubheading_base_f7",
          Qa = (0, W.Pi)(({ className: e, hasSeasonName: t = !0 }) => {
            const a = ce(),
              n = a.model,
              r = a.controls,
              i = n.season.startTimestamp.get(),
              o = n.season.endTimestamp.get(),
              l = n.season.serverTimestamp.get();
            return (
              (function (e, t, a) {
                (0, u.useEffect)(() => {
                  if (!(e >= t))
                    return Ra(() => {
                      a();
                    }, 950);
                }, [t, a, e]);
              })(l, o, r.pollServerTime),
              s().createElement(
                "div",
                { className: F()(Xa, e) },
                l < o
                  ? s().createElement(ja, {
                      startTimestamp: i,
                      endTimestamp: o,
                      currentTimestamp: l,
                      tooltipId: n.root.get().tooltipId,
                      hasSeasonName: t,
                    })
                  : R.strings.comp7.season.over(),
              )
            );
          });
        var Ya = a(7006);
        const Ka = ["iron", "bronze", "silver", "gold", "champion", "legend"],
          Za = (e, t, a) => {
            const n = (0, u.useMemo)(() => {
                return (t = e) >= 0 && t < Ka.length
                  ? Ka[t]
                  : (console.warn(`Invalid rank index: ${t}, fallback to 'iron'`), "iron");
                var t;
              }, [e]),
              r = (0, u.useState)(n),
              s = r[0],
              i = r[1];
            (0, u.useEffect)(() => {
              const e = setTimeout(() => i(n), t);
              return () => clearTimeout(e);
            }, [n, t]);
            const o = (0, u.useState)(s),
              l = o[0],
              c = o[1],
              m = (0, u.useState)(null),
              d = m[0],
              _ = m[1],
              E = (0, u.useRef)(l);
            E.current = l;
            const g = (0, Ya.useSpring)(() => ({ opacity: 0, config: { duration: a } })),
              p = g[0],
              f = g[1];
            return (
              (0, u.useEffect)(() => {
                if (s === E.current) return;
                const e = E.current;
                (c(s), _(e), f.set({ opacity: 1 }), f.start({ opacity: 0, onRest: () => _(null) }));
              }, [s, f]),
              { currentBg: l, prevBg: d, spring: p }
            );
          };
        class Ja extends s().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = X.B3.GOLD;
            else e = X.B3.INTEGRAL;
            const t = X.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        Ja.defaultProps = { format: "integral" };
        var en = a(9887),
          tn = a.n(en);
        const an = ["xl", "lg", "md", "sm", "xs"],
          nn = (e) => e.includes("_") && ((e) => an.includes(e))(e.split("_").at(-1)),
          rn = [B.ExtraLarge, B.Large, B.Medium, B.Small, B.ExtraSmall],
          un = (e, t) =>
            Object.keys(e).reduce((a, n) => {
              if (n in a) return a;
              if (nn(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in a) return a;
                const u = rn.indexOf(t),
                  s = (-1 !== u ? an.slice(u) : [])
                    .map((e) => r + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  i = s ? e[s] : void 0;
                return ((a[r] = void 0 !== i ? i : e[r]), a);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, t) => an.some((a) => void 0 !== t[`${e}_${a}`]))(n, e) ||
                  (a[n] = r),
                a
              );
            }, {}),
          sn = (e, t = un) => {
            const a = (
              (e, t = un) =>
              (a) => {
                const n = y().mediaSize,
                  r = (0, u.useMemo)(() => t(a, n), [a, n]);
                return s().createElement(e, r);
              }
            )(e, t);
            return s().memo((t) =>
              Object.keys(t).some((e) => nn(e) && void 0 !== t[e])
                ? s().createElement(a, t)
                : s().createElement(e, t),
            );
          },
          on = {
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
          ln = [
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
        function cn() {
          return (
            (cn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            cn.apply(this, arguments)
          );
        }
        Object.keys(tn());
        const mn = {
            XL: { mt: on.mt__XL, mr: on.mr__XL, mb: on.mb__XL, ml: on.ml__XL },
            LG: { mt: on.mt__LG, mr: on.mr__LG, mb: on.mb__LG, ml: on.ml__LG },
            MDp: { mt: on.mt__MDp, mr: on.mr__MDp, mb: on.mb__MDp, ml: on.ml__MDp },
            MD: { mt: on.mt__MD, mr: on.mr__MD, mb: on.mb__MD, ml: on.ml__MD },
            SMp: { mt: on.mt__SMp, mr: on.mr__SMp, mb: on.mb__SMp, ml: on.ml__SMp },
            SM: { mt: on.mt__SM, mr: on.mr__SM, mb: on.mb__SM, ml: on.ml__SM },
            XS: { mt: on.mt__XS, mr: on.mr__XS, mb: on.mb__XS, ml: on.ml__XS },
          },
          dn = (Object.keys(mn), ["mt", "mr", "mb", "ml"]),
          _n = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          En = sn((e) => {
            let t = e.className,
              a = e.width,
              n = e.height,
              r = e.m,
              i = e.mt,
              o = void 0 === i ? r : i,
              l = e.mr,
              c = void 0 === l ? r : l,
              m = e.mb,
              d = void 0 === m ? r : m,
              _ = e.ml,
              E = void 0 === _ ? r : _,
              g = e.column,
              p = e.row,
              f = e.flexDirection,
              A = void 0 === f ? (g ? "column" : p && "row") || void 0 : f,
              h = e.flexStart,
              v = e.center,
              b = e.flexEnd,
              D = e.spaceBetween,
              C = e.spaceAround,
              B = e.justifyContent,
              w =
                void 0 === B
                  ? (h ? "flex-start" : v && "center") ||
                    (b && "flex-end") ||
                    (D && "space-between") ||
                    (C && "space-around") ||
                    void 0
                  : B,
              S = e.alignItems,
              y =
                void 0 === S
                  ? (h ? "flex-start" : v && "center") || (b && "flex-end") || void 0
                  : S,
              R = e.alignSelf,
              x = e.wrap,
              P = e.flexWrap,
              k = void 0 === P ? (x ? "wrap" : void 0) : P,
              T = e.grow,
              L = e.shrink,
              N = e.flex,
              I = void 0 === N ? (T || L ? `${T ? 1 : 0} ${L ? 1 : 0} auto` : void 0) : N,
              M = e.style,
              O = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, ln);
            const W = (0, u.useMemo)(() => {
                const e = { mt: o, mr: c, mb: d, ml: E },
                  t = ((e) =>
                    dn.reduce((t, a) => {
                      const n = e[a];
                      return n && "number" != typeof n ? t.concat(mn[!0 === n ? "MD" : n][a]) : t;
                    }, []))(e),
                  r = ((e) =>
                    dn.reduce((t, a) => {
                      const n = e[a];
                      return ("number" == typeof n && (t[_n[a]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, M, r, {
                    width: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: I,
                    alignSelf: R,
                    display: A || y ? "flex" : void 0,
                    flexDirection: A,
                    flexWrap: k,
                    justifyContent: w,
                    alignItems: y,
                  }),
                  computedClassNames: t,
                };
              }, [a, n, o, c, d, E, M, I, R, A, k, w, y]),
              $ = W.computedStyle,
              z = W.computedClassNames;
            return s().createElement(
              "div",
              cn({ className: F()(on.base, ...z, t), style: $ }, H),
              O,
            );
          });
        var gn = a(3532),
          pn = a.n(gn);
        const fn = {
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
          An = [
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
        function hn() {
          return (
            (hn =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            hn.apply(this, arguments)
          );
        }
        Object.keys(tn());
        const vn = Object.keys(pn()),
          bn = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Fn = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Dn = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Cn = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Bn =
            (Object.keys(Cn),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": bn,
              "heading-H36": bn,
              "heading-H28": Fn,
              "heading-H24": Fn,
              "heading-H24R": Fn,
              "heading-H22": Fn,
              "heading-H20R": Fn,
              "heading-H18": Fn,
              "heading-H15": Dn,
              "heading-H14": Dn,
              "paragraph-P24": Fn,
              "paragraph-P18": Fn,
              "paragraph-P16": Fn,
              "paragraph-P14": Dn,
              "paragraph-P12": Dn,
              "paragraph-P10": Dn,
            }),
          wn =
            (Object.keys(Bn),
            (e) =>
              e
                ? ((e) => vn.includes(e))(e)
                  ? { colorClassName: fn[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Sn = sn((e) => {
            let t = e.text,
              a = e.variant,
              n = e.className,
              r = e.color,
              i = e.m,
              o = e.mt,
              l = void 0 === o ? i : o,
              c = e.mr,
              m = void 0 === c ? i : c,
              d = e.mb,
              _ = void 0 === d ? i : d,
              E = e.ml,
              g = void 0 === E ? i : E,
              p = e.style,
              f = e.format,
              A = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, An);
            const h = (0, u.useMemo)(() => {
                const e = wn(r),
                  t = e.colorClassName,
                  a = e.colorStyle,
                  n = void 0 === a ? {} : a;
                return { computedStyle: Object.assign({}, p, n), colorClassName: t };
              }, [p, r]),
              v = h.computedStyle,
              b = h.colorClassName;
            return s().createElement(
              En,
              hn(
                {
                  className: F()(fn.base, a && fn[a], b, n),
                  style: v,
                  mt: !0 === l ? Bn[a || "paragraph-P16"].mt : l,
                  mr: !0 === m ? Bn[a || "paragraph-P16"].mr : m,
                  mb: !0 === _ ? Bn[a || "paragraph-P16"].mb : _,
                  ml: !0 === g ? Bn[a || "paragraph-P16"].ml : g,
                },
                A,
              ),
              void 0 !== f ? s().createElement(Ia, hn({}, f, { text: t })) : t,
            );
          }),
          yn = {
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
          Rn =
            /(?:%\(|{)\w*(?:_[Oo]pen|Start)(?:\)s|})?(.*?)(?:%\(|{)\w*(?:_[Cc]lose|End)(?:\)s|})?/g,
          xn = /(?<=(?:%\(|{))(.*?)(?=(?:_[Oo]pen|Start))/,
          Pn = /(?<=(?:_[Oo]pen|Start)(?:\)s?|}))(.*?)(?=(?:%\(|{))/,
          kn = (0, u.memo)(({ text: e, binding: t, classMix: a }) => {
            const n = (0, u.useCallback)((e) => ({ color: `#${e}` }), []),
              r = (0, u.useMemo)(() => t || {}, [t]);
            let i = Rn.exec(e),
              o = e,
              l = 0;
            for (; i;) {
              const a = i[0],
                u = xn.exec(a),
                c = Pn.exec(a),
                m = i[1];
              if (u && c) {
                const e = u[0],
                  i = e + l++ + e;
                ((o = o.replace(a, `%(${i})`)),
                  (r[i] = yn[e]
                    ? s().createElement(
                        "span",
                        { className: yn[e] },
                        s().createElement(Ia, { text: m, binding: t }),
                      )
                    : s().createElement(
                        "span",
                        { style: n(e) },
                        s().createElement(Ia, { text: m, binding: t }),
                      )));
              }
              i = Rn.exec(e);
            }
            return s().createElement(Ia, { text: o, classMix: a, binding: r });
          }),
          Tn = "FailedFetchPointsText_base_be",
          Ln = "FailedFetchPointsText_icon_76",
          Nn = "FailedFetchPointsText_text_ea",
          In = ({ containerStyles: e }) =>
            s().createElement(
              "div",
              { className: F()(Tn, e) },
              s().createElement("div", { className: Ln }),
              s().createElement(Sn, {
                text: R.strings.comp7.honorsPlace.failedFetchPointsText(),
                className: Nn,
              }),
            ),
          Mn = "HonorsPlace_base_57",
          On = "HonorsPlace_base__error_c4",
          Hn = "HonorsPlace_base__tooltip_b9",
          Wn = "HonorsPlace_base__tooltipError_3c",
          $n = "HonorsPlace_transferPlace_46",
          zn = "HonorsPlace_elitePlace_eb",
          Un = "HonorsPlace_elitePlace__bronze_5b",
          Gn = "HonorsPlace_elitePlace__silver_cd",
          qn = "HonorsPlace_elitePlace__gold_87",
          Vn = "HonorsPlace_elitePlace__tooltip_0a",
          jn = "HonorsPlace_elitePlace__modeSelector_dc",
          Xn = "HonorsPlace_garland_ab",
          Qn = "HonorsPlace_garland__transferPlaceLeft_e7",
          Yn = "HonorsPlace_garland__transferPlaceLeft__tooltip_23",
          Kn = "HonorsPlace_garland__transferPlaceLeft__modeSelector_5a",
          Zn = "HonorsPlace_garland__transferPlaceRight_d4",
          Jn = "HonorsPlace_garland__transferPlaceRight__tooltip_20",
          er = "HonorsPlace_garland__transferPlaceRight__modeSelector_9f",
          tr = "HonorsPlace_garland__tooltip_3f",
          ar = "HonorsPlace_garland__modeSelector_e0",
          nr = "HonorsPlace_placeText_23",
          rr = "HonorsPlace_placeText__transfer_d3",
          ur = "HonorsPlace_placeText__transfer__copied_0f",
          sr = "HonorsPlace_placeText__tooltip_98",
          ir = "HonorsPlace_placeText__notInLeaderboard_81",
          or = "HonorsPlace_placeText__modeSelector_57",
          lr = "HonorsPlace_positionTitle_c9",
          cr = "HonorsPlace_positionTitle__tooltip_8a",
          mr = "HonorsPlace_positionTitle__modeSelector_c7",
          dr = "HonorsPlace_titleDescriptionContainer_15",
          _r = "HonorsPlace_descriptionText_b8",
          Er = "HonorsPlace_descriptionText__tooltip_70",
          gr = "HonorsPlace_descriptionText__withoutMargin_a9",
          pr = "HonorsPlace_descriptionText__blackout_3a",
          fr = "HonorsPlace_rankInactivityCount_34",
          Ar = "HonorsPlace_failedFetchPointsText_e2",
          hr =
            (ia(R.strings.comp7.lastUpdateNote.lastBestUserPoints.description(), { count: 15 }),
            "LastUpdateNote_base_7f"),
          vr = "LastUpdateNote_infoIcon_5c",
          br = "LastUpdateNote_lineDivider_2c";
        let Fr;
        !(function (e) {
          ((e[(e.ICON = 0)] = "ICON"), (e[(e.LINE = 1)] = "LINE"));
        })(Fr || (Fr = {}));
        const Dr = R.strings.comp7.lastUpdateNote,
          Cr = ({
            timestamp: e,
            className: t,
            classNames: a,
            dateTimeFormat: n = xa.SHORT_TIME,
            dividerType: r = Fr.ICON,
          }) =>
            s().createElement(
              "div",
              { className: F()(hr, t) },
              s().createElement(Sn, {
                text: Dr.info(),
                format: { binding: { date: s().createElement(La, { datetime: e, format: n }) } },
              }),
              r === Fr.ICON &&
                s().createElement(
                  Ve,
                  { body: Dr.tooltip.info() },
                  s().createElement("div", { className: F()(vr, null == a ? void 0 : a.icon) }),
                ),
              r === Fr.LINE &&
                s().createElement("div", { className: F()(br, null == a ? void 0 : a.line) }),
            ),
          Br = "RankInactivityCount_base_c2",
          wr = "RankInactivityCount_count_28",
          Sr = "RankInactivityCount_iconContainer_85",
          yr = "RankInactivityCount_icon_52",
          Rr = ({ count: e, containerStyles: t }) => {
            const a = F()(Br, t);
            return s().createElement(
              ze,
              {
                ignoreShowDelay: !0,
                contentId: R.views.lobby.comp7.tooltips.RankInactivityTooltip("resId"),
                args: { count: e },
              },
              s().createElement(
                "div",
                { className: a },
                s().createElement("div", { className: wr }, e),
                s().createElement(
                  "div",
                  { className: Sr },
                  s().createElement("div", { className: yr }),
                ),
              ),
            );
          },
          xr = R.strings.comp7.honorsPlace.description;
        var Pr;
        let kr;
        (!(function (e) {
          ((e[(e.BRONZE = 3)] = "BRONZE"),
            (e[(e.SILVER = 2)] = "SILVER"),
            (e[(e.GOLD = 1)] = "GOLD"),
            (e[(e.NOT_IN_LEADERBOARD = 0)] = "NOT_IN_LEADERBOARD"),
            (e[(e.ERROR = -1)] = "ERROR"));
        })(Pr || (Pr = {})),
          (function (e) {
            ((e.PROGRESSION = "PROGRESSION"),
              (e.TOOLTIP = "TOOLTIP"),
              (e.MODE_SELECTOR = "MODE_SELECTOR"));
          })(kr || (kr = {})));
        const Tr = ({ mode: e, model: t }) => {
            var a, n;
            const r = t.root.get(),
              u = r.myPosition,
              i = r.currentScore,
              o = r.rankInactivityCount,
              l = r.leaderboardUpdateTimestamp,
              c =
                null == t || null == (a = t.computes) || null == a.hasCurrentItemRankInactivity
                  ? void 0
                  : a.hasCurrentItemRankInactivity(),
              m = u === Pr.ERROR,
              d = u === Pr.BRONZE,
              _ = u === Pr.SILVER,
              E = u === Pr.GOLD,
              g = !m && (d || _ || E),
              p = u === Pr.NOT_IN_LEADERBOARD,
              f = e === kr.TOOLTIP,
              A = e === kr.MODE_SELECTOR,
              h = (({
                isErrorLoadingPointsValue: e,
                isElitePlace: t,
                isTooltip: a,
                isBronze: n,
                isSilver: r,
                isGold: u,
                isNotInLeaderboard: s,
                isModeSelector: i,
              }) => {
                const o = F()(Mn, e && !a && On, a && e && Wn, a && Hn),
                  l = F()(lr, a && cr, i && mr);
                return {
                  baseStyles: o,
                  leftGarlandStyle: F()(Xn, !t && Qn, a && Yn, a && tr, i && ar, i && Kn),
                  rightGarlandStyle: F()(Xn, !t && Zn, a && Jn, a && tr, i && ar, i && er),
                  placeTextStyle: F()(nr, !t && rr, a && sr, s && ir, i && or),
                  placeTextCopiedStyle: F()(nr, rr, ur, a && sr, s && ir, i && or),
                  elitePlaceStyle: F()(zn, n && Un, r && Gn, u && qn, a && Vn, i && jn),
                  positionTitleStyle: l,
                  lastUpdateNoteStyle: F()(_r, a && Er, a && pr),
                };
              })({
                isErrorLoadingPointsValue: m,
                isElitePlace: g,
                isTooltip: f,
                isBronze: d,
                isSilver: _,
                isGold: E,
                isNotInLeaderboard: p,
                isModeSelector: A,
              }),
              v = h.baseStyles,
              b = h.leftGarlandStyle,
              D = h.rightGarlandStyle,
              C = h.placeTextStyle,
              B = h.placeTextCopiedStyle,
              w = h.elitePlaceStyle,
              S = h.positionTitleStyle,
              y = h.lastUpdateNoteStyle,
              R =
                e === kr.PROGRESSION &&
                (null == (n = t.computes) || null == n.hasCurrentItemRankInactivity
                  ? void 0
                  : n.hasCurrentItemRankInactivity()),
              x = p ? "--" : X.Z5.getNumberFormat(u, X.B3.INTEGRAL);
            return s().createElement(
              "div",
              { className: v },
              m && !A && s().createElement(In, { containerStyles: Ar }),
              !m &&
                s().createElement(
                  s().Fragment,
                  null,
                  g
                    ? s().createElement("div", { className: w })
                    : s().createElement(
                        "div",
                        { className: $n },
                        s().createElement("div", { className: b }),
                        s().createElement(Sn, { text: String(x), className: C }),
                        s().createElement(Sn, { text: String(x), className: B }),
                        s().createElement("div", { className: D }),
                      ),
                  s().createElement(Sn, { text: xr.title(), className: S }),
                ),
              s().createElement(
                "div",
                { className: dr },
                !m &&
                  "number" == typeof l &&
                  s().createElement(Cr, {
                    timestamp: l,
                    className: y,
                    dividerType: f ? Fr.LINE : Fr.ICON,
                  }),
                !A &&
                  s().createElement(kn, {
                    text: xr.ratingCount(),
                    binding: { count: s().createElement(Ja, { value: i }) },
                    classMix: F()(_r, f && Er, f && gr),
                  }),
                c &&
                  "number" == typeof o &&
                  R &&
                  s().createElement(Rr, { count: o, containerStyles: fr }),
              ),
            );
          },
          Lr = "RatingScore_base_bd",
          Nr = "RatingScore_rating_c9",
          Ir = "RatingScore_content_62",
          Mr = "RatingScore_score_33",
          Or = "RatingScore_counter_1a",
          Hr = "RatingScore_title_e4",
          Wr = ({ currentScore: e, hasRankInactivity: t, rankInactivityCount: a, className: n }) =>
            s().createElement(
              "div",
              { className: F()(Lr, n) },
              s().createElement(
                "div",
                { className: Nr },
                s().createElement(
                  "div",
                  { className: Ir },
                  s().createElement("div", { className: Mr }, e),
                  s().createElement("div", { className: Hr }, R.strings.comp7.ratingScore.title()),
                ),
                t && s().createElement(Rr, { containerStyles: Or, count: a }),
              ),
            ),
          $r = "ItemFooter_base_0f",
          zr = "ItemFooter_background_bf",
          Ur = "ItemFooter_divider_bb",
          Gr = "ItemFooter_light_79",
          qr = "ItemFooter_footer_e7",
          Vr = "ItemFooter_rankItemFooter_e6",
          jr = (0, W.Pi)(({ className: e }) => {
            var t;
            const a = wa().model,
              n = a.root.get(),
              r = n.currentScore,
              u = n.myPosition,
              i = n.rankInactivityCount,
              o = n.currentItemIndex,
              l = a.computes.modelItems(),
              c = a.computes.divisionsConfig(o).currentDivisionIndex,
              m = a.computes.divisions(o),
              d =
                (null == m || null == (t = m[null != c ? c : -1]) ? void 0 : t.type) ===
                ba.TRANSFER,
              _ = l.findIndex((e) => e.divisions.findIndex((e) => e.type === ba.TRANSFER) > -1),
              E = l.findIndex((e) => e.divisions.findIndex((e) => e.type === ba.ELITE) > -1),
              g = isFinite(u) && ((o >= _ && d) || o === E),
              p = F()($r, e),
              f = a.computes.hasCurrentItemRankInactivity();
            return s().createElement(
              "div",
              { className: p },
              s().createElement("div", { className: zr }),
              s().createElement("div", { className: Ur }),
              s().createElement("div", { className: Gr }),
              s().createElement(
                "div",
                { className: qr },
                g
                  ? s().createElement(Tr, { model: a, mode: kr.PROGRESSION })
                  : s().createElement(Wr, {
                      currentScore: r,
                      hasRankInactivity: f,
                      rankInactivityCount: i,
                      className: Vr,
                    }),
              ),
            );
          }),
          Xr = [
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_5(),
              speedX: -0.053,
              speedY: -0.01,
            },
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_4(),
              speedX: -0.037,
              speedY: -0.0055,
            },
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_3(),
              speedX: -0.025,
              speedY: -0.0016,
            },
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_2(),
              speedX: 0,
              speedY: 0,
            },
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_1(),
              speedX: 0.015,
              speedY: 0.002,
            },
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_1_1(),
              speedX: 0.015,
              speedY: 0.002,
            },
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_0(),
              speedX: 0.03,
              speedY: 0.014,
            },
            {
              path: R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_0_1(),
              speedX: 0.03,
              speedY: 0.014,
            },
          ],
          Qr = () => {
            const e = o.O.view.getSize("rem"),
              t = (0, u.useState)({ height: e.height, width: e.width }),
              a = t[0],
              n = t[1];
            return (
              (0, u.useEffect)(() => {
                const e = (e) => {
                  n(e);
                };
                return (
                  engine.on("screenResized", e),
                  () => {
                    engine.off("screenResized", e);
                  }
                );
              }, []),
              a
            );
          },
          Yr = "Parallax_base_c9",
          Kr = "Parallax_layer_15",
          Zr = "Parallax_shadow_45",
          Jr = [
            R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_1_1(),
            R.images.comp7.gui.maps.icons.comp7.qualificationParallax.c_0_1(),
          ],
          eu = Xr.reduce((e, t) => {
            const a = Math.abs(t.speedX);
            return a > e ? a : e;
          }, 0),
          tu = (0, W.Pi)(({ className: e }) => {
            const t = wa().model,
              a = Qr().width,
              n = (0, u.createRef)(),
              r = eu * a,
              i = (0, Pe.useSpring)({
                to: { opacity: t.isRewardLayerVisible.get() ? 1 : 0 },
                config: { duration: 300 },
              }),
              l = ((e) => {
                const t = (0, u.useCallback)(
                    (t) => {
                      if (!e.current) return;
                      const a = e.current.getBoundingClientRect(),
                        n = a.width,
                        r = a.height;
                      return (
                        0 !== t.clientX &&
                        0 !== t.clientY &&
                        t.clientX <= n - 2 &&
                        t.clientY <= r - 2
                      );
                    },
                    [e],
                  ),
                  a = (0, Pe.useSpring)(
                    () => Object.assign({}, o.O.client.getMouseGlobalPosition("px")),
                    [],
                  );
                return (
                  (0, u.useEffect)(() => {
                    const e = (e) => {
                      t(e) && a[1].start({ x: e.clientX, y: e.clientY });
                    };
                    return (
                      document.addEventListener("mousemove", e),
                      () => {
                        document.removeEventListener("mousemove", e);
                      }
                    );
                  }, [t, a]),
                  a
                );
              })(n),
              c = l[0];
            return s().createElement(
              "div",
              { ref: n, className: F()(Yr, e) },
              Xr.map((e, t) =>
                s().createElement(
                  Pe.animated.div,
                  {
                    key: t,
                    className: Kr,
                    style: Object.assign(
                      {
                        width: `${a + 2 * r}rem`,
                        left: -r + "rem",
                        x: c.x.to((t) => t * e.speedX),
                        y: c.y.to((t) => t * e.speedY),
                        backgroundImage: `url(${e.path})`,
                      },
                      Jr.includes(e.path) && i,
                    ),
                  },
                  3 === t && s().createElement(Pe.animated.div, { className: Zr, style: i }),
                ),
              ),
            );
          }),
          au = "ParallaxContainer_base_17",
          nu = Xr.map((e) => e.path),
          ru = (0, W.Pi)(({ className: e }) => {
            const t = wa(),
              a = t.model,
              n = t.controls,
              r = a.isParallaxPreloaded.get(),
              i = (0, Pe.useSpring)({ to: { opacity: r ? 1 : 0 }, config: { duration: 300 } });
            return (
              "success" ===
                ((e) => {
                  const t = (0, u.useState)("pending"),
                    a = t[0],
                    n = t[1];
                  return (
                    (0, u.useLayoutEffect)(() => {
                      let t = 0,
                        a = 0;
                      const r = () => {
                        t + a === e.length && n(0 === t ? "success" : "error");
                      };
                      e.forEach((e) => {
                        const n = new Image();
                        ((n.src = e),
                          n.addEventListener("load", () => {
                            (a++, r());
                          }),
                          n.addEventListener("error", () => {
                            (t++, r());
                          }));
                      });
                    }, [e]),
                    a
                  );
                })(nu) && n.setIsParallaxPreloaded(!0),
              s().createElement(
                Pe.animated.div,
                { className: F()(au, e), style: i },
                s().createElement(tu, null),
              )
            );
          }),
          uu = () => {
            const e = (0, u.useState)(o.O.view.getScale()),
              t = e[0],
              a = e[1];
            return (
              (0, u.useEffect)(() => {
                const e = () => {
                  a(o.O.view.getScale());
                };
                return (
                  window.addEventListener("resize", e),
                  () => {
                    window.removeEventListener("resize", e);
                  }
                );
              }, []),
              t
            );
          },
          su = (e, t) => {
            const a = [];
            for (let n = 0; n < e; n++) a.push(t(n));
            return a;
          },
          iu = { type: "idle" };
        const ou = (e, t = 100) =>
            ((viewEnv.pxToRem(o.O.client.getSize("px").width) * t) / 100 - e) / 2,
          lu = (e, t, a) => (a < e ? e : a > t ? t : a),
          cu = [];
        function mu(e) {
          const t = (0, u.useRef)(e);
          return (
            (0, u.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, u.useCallback)((...e) => (0, t.current)(...e), cu)
          );
        }
        function du(e, t, a = []) {
          const n = (0, u.useRef)(0),
            r = (0, u.useCallback)(() => window.clearInterval(n.current), a || []);
          (0, u.useEffect)(() => r, [r]);
          const s = (null != a ? a : []).concat([t]);
          return [
            (0, u.useCallback)((a) => {
              ((n.current = window.setInterval(() => e(a, !0), t)), e(a, !1));
            }, s),
            r,
          ];
        }
        function _u(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Eu(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return Eu(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Eu(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, n = new Array(t); a < t; a++) n[a] = e[a];
          return n;
        }
        function gu(e, t, a) {
          const n = (0, u.useMemo)(
            () =>
              (function (e, t, a, n) {
                let r,
                  u = !1,
                  s = 0;
                function i() {
                  r && clearTimeout(r);
                }
                function o(...o) {
                  const l = this,
                    c = Date.now() - s;
                  function m() {
                    ((s = Date.now()), a.apply(l, o));
                  }
                  u ||
                    (n && !r && m(),
                    i(),
                    void 0 === n && c > e
                      ? m()
                      : !0 !== t &&
                        (r = setTimeout(
                          n
                            ? function () {
                                r = void 0;
                              }
                            : m,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof t && ((n = a), (a = t), (t = void 0)),
                  (o.cancel = function () {
                    (i(), (u = !0));
                  }),
                  o
                );
              })(a, e),
            t,
          );
          return ((0, u.useEffect)(() => n.cancel, [n]), n);
        }
        let pu;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(pu || (pu = {}));
        const fu = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          Au = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: a,
            getDirection: n,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: s = !1,
          }) => {
            const i = (e, a) => {
              const n = t(e),
                r = n[0],
                u = n[1];
              return lu(r, u, a);
            };
            return (l = {}) => {
              const c = l.settings,
                m = void 0 === c ? fu : c,
                d = (0, u.useRef)(null),
                _ = (0, u.useRef)(null),
                E = (() => {
                  const e = (0, u.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    a = (e, a) => {
                      t(e).set(a, a);
                    },
                    n = (e, a) => {
                      t(e).delete(a);
                    },
                    r = (e, ...a) => {
                      for (var n, r = _u(t(e).values()); !(n = r()).done;) (0, n.value)(...a);
                    };
                  return (0, u.useMemo)(() => ({ on: a, off: n, trigger: r }), []);
                })(),
                g = gu(
                  () => {
                    o.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                p = (0, Pe.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = d.current;
                    t && (a(t, e), E.trigger("change", e), s && g());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                f = p[0],
                A = p[1],
                h = (0, u.useCallback)(
                  (e, t, a) => {
                    var n;
                    const r = f.scrollPosition.get(),
                      u = (null != (n = f.scrollPosition.goal) ? n : 0) - r;
                    return i(e, t * a + u + r);
                  },
                  [f.scrollPosition],
                ),
                v = (0, u.useCallback)(
                  (e, { immediate: t = !1, reset: a = !0 } = {}) => {
                    const n = d.current;
                    n &&
                      A.start({
                        scrollPosition: i(n, e),
                        immediate: t,
                        reset: a,
                        config: m.animationConfig,
                        from: { scrollPosition: i(n, f.scrollPosition.get()) },
                      });
                  },
                  [A, m.animationConfig, f.scrollPosition],
                ),
                b = (0, u.useCallback)(
                  (e) => {
                    const t = d.current,
                      a = _.current;
                    if (!t || !a) return;
                    const n = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return r(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(a, m.step),
                      u = h(t, e, n);
                    v(u);
                  },
                  [v, h, m.step],
                ),
                F = (0, u.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && b(n(e)),
                      d.current && E.trigger("mouseWheel", e, f.scrollPosition, t(d.current)));
                  },
                  [f.scrollPosition, b, E],
                ),
                D = Gt(
                  () =>
                    xe(() => {
                      const e = d.current;
                      e &&
                        (v(i(e, f.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [v, f.scrollPosition.goal],
                ),
                C = mu(() => {
                  const e = d.current;
                  if (!e) return;
                  const t = i(e, f.scrollPosition.goal);
                  (t !== f.scrollPosition.goal && v(t, { immediate: !0 }),
                    E.trigger("recalculateContent"));
                });
              (0, u.useEffect)(
                () => (
                  window.addEventListener("resize", D),
                  () => {
                    window.removeEventListener("resize", D);
                  }
                ),
                [D],
              );
              const B = (0, u.useCallback)((e) => E.trigger("isThumbDraggingChanged", e), [E]);
              return (0, u.useMemo)(
                () => ({
                  getWrapperSize: () => (_.current ? r(_.current) : void 0),
                  getContainerSize: () => (d.current ? e(d.current) : void 0),
                  getBounds: () =>
                    d.current
                      ? t(d.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: m.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: F,
                  applyScroll: v,
                  applyStepTo: b,
                  contentRef: d,
                  wrapperRef: _,
                  scrollPosition: A,
                  animationScroll: f,
                  recalculateContent: C,
                  handleIsThumbDragging: B,
                  events: { on: E.on, off: E.off },
                }),
                [f.scrollPosition, v, b, B, E.off, E.on, C, F, A, m.step.clampedArrowStepTimeout],
              );
            };
          },
          hu = Au({
            getBounds: (e) => {
              var t, a;
              return [
                0,
                e.offsetWidth -
                  (null != (t = null == (a = e.parentElement) ? void 0 : a.offsetWidth) ? t : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, t) => {
              e.style.transform = `translateX(-${t.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? pu.Next : pu.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          vu = "HorizontalBar_base_49",
          bu = "HorizontalBar_base__nonActive_82",
          Fu = "HorizontalBar_leftButton_5f",
          Du = "HorizontalBar_rightButton_03",
          Cu = "HorizontalBar_track_0d",
          Bu = "HorizontalBar_thumb_fd",
          wu = "HorizontalBar_rail_32",
          Su = "disable",
          yu = { pending: !1, offset: 0 },
          Ru = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          xu = () => {},
          Pu = (e, t) => Math.max(20, e.offsetWidth * t),
          ku = (0, u.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = Ru, onDrag: n = xu }) => {
              const r = (0, u.useRef)(null),
                i = (0, u.useRef)(null),
                o = (0, u.useRef)(null),
                l = (0, u.useRef)(null),
                c = (0, u.useRef)(null),
                m = e.stepTimeout || 100,
                d = (0, u.useState)(yu),
                _ = d[0],
                E = d[1],
                g = (0, u.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                p = () => {
                  const t = l.current,
                    a = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && a && r)) return;
                  const u = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    m = lu(0, 1, u / (r - n)),
                    d = (t.offsetWidth - Pu(t, s)) * m;
                  ((a.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (i.current && o.current && l.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Su), void o.current.classList.remove(Su));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetWidth - a.offsetWidth) >= -0.5)
                        )
                          return (i.current.classList.remove(Su), void o.current.classList.add(Su));
                        var t, a;
                        (i.current.classList.remove(Su), o.current.classList.remove(Su));
                      }
                    })(d));
                },
                f = mu(() => {
                  ((() => {
                    const t = c.current,
                      a = l.current,
                      n = e.getWrapperSize(),
                      u = e.getContainerSize();
                    if (!(u && t && n && a)) return;
                    const s = Math.min(1, n / u);
                    ((t.style.width = `${Pu(a, s)}px`),
                      (t.style.display = "flex"),
                      r.current &&
                        (1 === s ? r.current.classList.add(bu) : r.current.classList.remove(bu)));
                  })(),
                    p());
                });
              ((0, u.useEffect)(() => xe(f)),
                (0, u.useEffect)(
                  () =>
                    xe(() => {
                      const t = () => {
                        p();
                      };
                      let a = xu;
                      const n = () => {
                        (a(), (a = xe(f)));
                      };
                      return (
                        e.events.on("recalculateContent", f),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", n),
                        () => {
                          (a(),
                            e.events.off("recalculateContent", f),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, u.useEffect)(() => {
                  if (!_.pending) return;
                  const t = (t) => {
                      var a;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const u = l.current,
                        s = c.current;
                      if (!r || !u || !s) return;
                      const i = t.screenX - _.offset - u.getBoundingClientRect().x,
                        o = (i / u.offsetWidth) * (null != (a = e.getContainerSize()) ? a : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, o),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: s, thumbOffset: i, contentOffset: o }));
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t), g(yu));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, _.offset, _.pending, n, g]));
              const A = du((t) => e.applyStepTo(t), m, [e]),
                h = A[0],
                v = A[1];
              (0, u.useEffect)(
                () => (
                  document.addEventListener("mouseup", v, !0),
                  () => document.removeEventListener("mouseup", v, !0)
                ),
                [v],
              );
              const b = (e) => {
                e.target.classList.contains(Su) || $("highlight");
              };
              return s().createElement(
                "div",
                { className: F()(vu, t.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: F()(Fu, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Su) || 0 !== e.button || ($("play"), h(pu.Next));
                  },
                  onMouseUp: v,
                  ref: i,
                  onMouseEnter: b,
                }),
                s().createElement(
                  "div",
                  {
                    className: F()(Cu, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if (($("play"), t.target === n))
                          g({ pending: !0, offset: t.screenX - n.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const n = c.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const u = a(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + u * t);
                          })(t.screenX > n.getBoundingClientRect().x ? pu.Prev : pu.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: b,
                  },
                  s().createElement("div", { ref: c, className: F()(Bu, t.thumb) }),
                  s().createElement("div", { className: F()(wu, t.rail) }),
                ),
                s().createElement("div", {
                  className: F()(Du, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Su) || 0 !== e.button || ($("play"), h(pu.Prev));
                  },
                  onMouseUp: v,
                  ref: o,
                  onMouseEnter: b,
                }),
              );
            },
          ),
          Tu = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Lu = ({
            children: e,
            api: t,
            className: a,
            barClassNames: n,
            areaClassName: r,
            classNames: i,
            scrollClassName: o,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const m = (0, u.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: F()(Tu.base, e.base) });
              }, [n]),
              d = (0, u.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return s().createElement(
              "div",
              { className: F()(Tu.defaultScroll, a), onWheel: t.handleMouseWheel },
              s().createElement(
                "div",
                { className: F()(Tu.defaultScrollArea, r) },
                s().createElement(Nu, { className: o, api: d, classNames: i }, e),
              ),
              s().createElement(ku, { getStepByRailClick: l, api: t, onDrag: c, classNames: m }),
            );
          },
          Nu = ({ api: e, className: t, classNames: a, children: n, style: r }) => (
            (0, u.useEffect)(() => xe(e.recalculateContent)),
            s().createElement(
              "div",
              { className: F()(Tu.base, t), style: r },
              s().createElement(
                "div",
                {
                  className: F()(Tu.wrapper, null == a ? void 0 : a.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                s().createElement(
                  "div",
                  { className: F()(Tu.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((Nu.Bar = ku),
          (Nu.Default = Lu),
          (Nu.SeniorityAwards = ({ api: e, className: t, classNames: a, children: n }) => (
            (0, u.useEffect)(() => xe(e.recalculateContent)),
            s().createElement(
              "div",
              { className: F()(Tu.base, t) },
              s().createElement(
                "div",
                { className: F()(Tu.wrapper, null == a ? void 0 : a.wrapper), ref: e.wrapperRef },
                s().createElement(
                  "div",
                  { className: F()(Tu.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const Iu = "ProgressionScroll_base_0f",
          Mu = "ProgressionScroll_areaWrapper_dc",
          Ou = "ProgressionScroll_areaContent_2f",
          Hu = ({
            api: e,
            stuckIndex: t,
            itemWidth: a,
            itemsOffset: n = 0,
            children: r,
            onStick: i,
            className: l,
            areaClassNames: c,
            barClassNames: m,
            staticContent: d,
            containerMaxWidth: _,
          }) => {
            const E = viewEnv.remToPx(a),
              g = e.animationScroll,
              p = e.events,
              f = e.applyScroll,
              A = (function (e, t, a) {
                const n = e.contentRef,
                  r = e.wrapperRef,
                  s = e.scrollPosition,
                  i = e.clampPosition,
                  l = e.animationScroll,
                  c = e.events,
                  m = (0, u.useState)(iu),
                  d = m[0],
                  _ = m[1];
                return (
                  (0, u.useEffect)(() => {
                    const e = n.current;
                    e && (e.style.cursor = "dragging" === d.type ? "move" : "grab");
                  }, [n, d.type]),
                  (0, u.useEffect)(() => {
                    if ("dragging" !== d.type) return;
                    const e = o.O.client.events.mouse.move(([e, a]) => {
                        const u = n.current,
                          o = r.current;
                        if (!u || !o) return;
                        if ("inside" === a && e.clientX < 0) return;
                        const c = "inside" === a ? e.clientX : e.clientX - o.offsetLeft,
                          m = d.positionFrom - c,
                          _ = d.previousScrollPosition + m;
                        s.start(
                          Object.assign(
                            {
                              scrollPosition: i(u, _),
                              from: { scrollPosition: l.scrollPosition.get() },
                            },
                            t && { config: t },
                          ),
                        );
                      }),
                      a = o.O.client.events.mouse.up(function () {
                        _({ type: "scrollingToEnd" });
                      });
                    return () => {
                      (e(), a());
                    };
                  }, [l.scrollPosition, i, n, d, s, r, t]),
                  (0, u.useEffect)(() => {
                    if ("scrollingToEnd" !== d.type) return;
                    const e = () => {
                      _(iu);
                    };
                    return (l.scrollPosition.idle && e(), c.on("rest", e), () => c.off("rest", e));
                  }, [l.scrollPosition, d.type, c]),
                  (0, u.useEffect)(() => {
                    const e = n.current;
                    if (!e) return;
                    const t = (e) => {
                      (a &&
                        a.allowedButtons &&
                        -1 === a.allowedButtons.findIndex((t) => e.button === t)) ||
                        _({
                          type: "dragging",
                          positionFrom: e.screenX,
                          previousScrollPosition: l.scrollPosition.get(),
                        });
                    };
                    return (
                      e.addEventListener("mousedown", t),
                      () => e.removeEventListener("mousedown", t)
                    );
                  }, [l.scrollPosition, n, a]),
                  d
                );
              })(e),
              h = (0, u.useCallback)(
                (e) => {
                  f(t * E, e);
                },
                [f, E, t],
              ),
              v = (0, u.useCallback)(() => {
                null == i || i(Math.round(g.scrollPosition.goal / E));
              }, [i, g.scrollPosition, E]);
            ((0, u.useEffect)(() => (p.on("rest", v), () => p.off("rest", v)), [p, v]),
              (0, u.useEffect)(() => {
                const e = () => {
                  h({ immediate: !0, reset: !0 });
                };
                return (
                  p.on("resizeHandled", e),
                  () => {
                    p.off("resizeHandled", e);
                  }
                );
              }, [h, p]),
              (0, u.useEffect)(
                () =>
                  xe(() => {
                    "idle" === A.type && g.scrollPosition.idle && h();
                  }),
                [g.scrollPosition, A, h],
              ));
            const b = (0, u.useCallback)(
              (e) => {
                "dragEnd" === e.type && f(t * E);
              },
              [f, E, t],
            );
            return s().createElement(
              "div",
              {
                className: F()(Iu, l),
                style: { "--offset": `${n}rem`, maxWidth: _ ? `${_}rem` : "100%" },
              },
              s().createElement(
                Nu,
                {
                  api: e,
                  className: null == c ? void 0 : c.base,
                  classNames: {
                    wrapper: F()(Mu, null == c ? void 0 : c.wrapper),
                    content: F()(Ou, null == c ? void 0 : c.content),
                  },
                },
                r,
              ),
              d,
              s().createElement(ku, { api: e, onDrag: b, classNames: m }),
            );
          },
          Wu = (e, t = 150, a) => {
            const n = viewEnv.remToPx(e),
              r = (0, u.useMemo)(
                () => ({
                  settings: {
                    step: { type: "fixed", value: n, clampedArrowStepTimeout: t },
                    animationConfig: Object.assign({ frequency: 0.5 }, a),
                  },
                }),
                [a, n, t],
              );
            return hu(r);
          };
        let $u;
        !(function (e) {
          ((e[(e.First = 6)] = "First"),
            (e[(e.Second = 5)] = "Second"),
            (e[(e.Third = 4)] = "Third"),
            (e[(e.Fourth = 3)] = "Fourth"),
            (e[(e.Fifth = 2)] = "Fifth"),
            (e[(e.Sixth = 1)] = "Sixth"));
        })($u || ($u = {}));
        const zu = {
            [$u.First]: "first",
            [$u.Second]: "second",
            [$u.Third]: "third",
            [$u.Fourth]: "fourth",
            [$u.Fifth]: "fifth",
            [$u.Sixth]: "sixth",
          },
          Uu = (e, t) => `${e.$dyn(zu[t])}`,
          Gu = (e) => Uu(R.strings.comp7.rank, e),
          qu = (e) => ia(R.strings.comp7.rank.text(), { rank: Gu(e) }),
          Vu = {
            [$u.First]: "first",
            [$u.Second]: "second",
            [$u.Third]: "third",
            [$u.Fourth]: "fourth",
            [$u.Fifth]: "fifth",
            [$u.Sixth]: "sixth",
          },
          ju = (e) => Vu[e],
          Xu = [$u.First, $u.Second, $u.Third, $u.Fourth, $u.Fifth, $u.Sixth],
          Qu = (e) => Xu.includes(e),
          Yu = "RankEmblem_base_ec";
        let Ku;
        !(function (e) {
          ((e[(e.x22 = 22)] = "x22"),
            (e[(e.x40 = 40)] = "x40"),
            (e[(e.x48 = 48)] = "x48"),
            (e[(e.x64 = 64)] = "x64"),
            (e[(e.x84 = 84)] = "x84"),
            (e[(e.x110 = 110)] = "x110"),
            (e[(e.x150 = 150)] = "x150"),
            (e[(e.x200 = 200)] = "x200"),
            (e[(e.x260 = 260)] = "x260"),
            (e[(e.x320 = 320)] = "x320"),
            (e[(e.x420 = 420)] = "x420"),
            (e[(e.x600 = 600)] = "x600"));
        })(Ku || (Ku = {}));
        const Zu = ({ rank: e, size: t, division: a, className: n }) => {
            const r = (0, u.useMemo)(() => {
              const n = R.images.comp7.gui.maps.icons.comp7.ranks.$num(t),
                r = Qu(e) && void 0 !== a ? `_${pa(a)}` : "";
              return {
                backgroundImage: `url(${n.$dyn(`${ju(e)}${r}`)})`,
                "--imageSize": `${t}rem`,
              };
            }, [e, t, a]);
            return s().createElement("div", { className: F()(Yu, n), style: r });
          },
          Ju = {
            "--pageContentWidth": "78vw",
            base: "HighlightedRankEmblem_base_e2",
            highlights: "HighlightedRankEmblem_highlights_cc",
            highlights__gold: "HighlightedRankEmblem_highlights__gold_9f",
            highlights__silver: "HighlightedRankEmblem_highlights__silver_f4",
            highlights__hidden: "HighlightedRankEmblem_highlights__hidden_10",
            highlight: "HighlightedRankEmblem_highlight_72",
            highlightAppearance: "HighlightedRankEmblem_highlightAppearance_60",
            rotate: "HighlightedRankEmblem_rotate_0f",
            highlight__second: "HighlightedRankEmblem_highlight__second_91",
            base__static: "HighlightedRankEmblem_base__static_87",
            rankEmblem: "HighlightedRankEmblem_rankEmblem_29",
            fadeIn: "HighlightedRankEmblem_fadeIn_3a",
            fadeInThreeQuarters: "HighlightedRankEmblem_fadeInThreeQuarters_a4",
            fadeInHalf: "HighlightedRankEmblem_fadeInHalf_6e",
            fadeOut: "HighlightedRankEmblem_fadeOut_48",
            fadeInWithScale: "HighlightedRankEmblem_fadeInWithScale_a8",
            slideUp: "HighlightedRankEmblem_slideUp_82",
            scale: "HighlightedRankEmblem_scale_ec",
            raysAppearance: "HighlightedRankEmblem_raysAppearance_a6",
            "reverse-rotate": "HighlightedRankEmblem_reverse-rotate_e8",
            glowAppearance: "HighlightedRankEmblem_glowAppearance_2a",
            blink: "HighlightedRankEmblem_blink_ce",
            slideUpIn: "HighlightedRankEmblem_slideUpIn_80",
          };
        let es, ts;
        (!(function (e) {
          ((e.Silver = "silver"), (e.Gold = "gold"), (e.Hidden = "hidden"));
        })(es || (es = {})),
          (function (e) {
            ((e.Dynamic = "dynamic"), (e.Static = "static"));
          })(ts || (ts = {})));
        const as = {
            [Ku.x48]: 64,
            [Ku.x64]: 80,
            [Ku.x110]: 140,
            [Ku.x200]: 260,
            [Ku.x260]: 340,
            [Ku.x320]: 400,
            [Ku.x420]: 550,
          },
          ns = ({
            size: e,
            rank: t,
            division: a,
            type: n = ts.Dynamic,
            state: r,
            classNames: u,
          }) => {
            const i = ((e) => ({
              backgroundImage: `url(${R.images.comp7.gui.maps.icons.comp7.ranks.$num(e).$dyn("highlight")})`,
            }))(e);
            return s().createElement(
              "div",
              { className: F()(Ju.base, Ju[`base__${n}`]) },
              s().createElement(
                "div",
                {
                  className: F()(
                    Ju.highlights,
                    Ju[`highlights__${r}`],
                    null == u ? void 0 : u.highlights,
                  ),
                  style: { "--highlightsSize": `${as[e]}rem` },
                },
                s().createElement("div", {
                  className: F()(
                    Ju.highlight,
                    Ju.highlight__first,
                    null == u ? void 0 : u.highlight,
                  ),
                  style: i,
                }),
                n === ts.Dynamic &&
                  s().createElement("div", {
                    className: F()(
                      Ju.highlight,
                      Ju.highlight__second,
                      null == u ? void 0 : u.highlight,
                    ),
                    style: i,
                  }),
              ),
              s().createElement(Zu, {
                size: e,
                rank: t,
                division: a,
                className: F()(Ju.rankEmblem, null == u ? void 0 : u.rankEmblem),
              }),
            );
          },
          rs = [$u.Fifth, $u.Sixth],
          us = (e, t, a) =>
            e !== ha.Current || a ? es.Hidden : rs.includes(t) ? es.Gold : es.Silver,
          ss = "RankItemDivider_base_c4",
          is = () => s().createElement("div", { className: ss }),
          os = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let ls, cs;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(ls || (ls = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(cs || (cs = {})));
        const ms = ({ size: e = ls.Default, classMix: t }) =>
            s().createElement("div", { className: F()(os.background, os[`background__${e}`], t) }),
          ds = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          _s = ({ size: e }) => {
            const t = F()(ds.base, ds[`base__${e}`]);
            return s().createElement("div", { className: t });
          },
          Es = {
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
          gs = (0, u.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: a,
              baseStyles: n,
              isComplete: r,
              withoutBounce: u,
            }) => {
              const i = F()(
                  Es.base,
                  Es[`base__${e}`],
                  a && Es.base__disabled,
                  r && Es.base__finished,
                  u && Es.base__withoutBounce,
                ),
                o = !a && !r;
              return s().createElement(
                "div",
                { className: i, style: n, ref: t },
                s().createElement("div", { className: Es.pattern }),
                s().createElement("div", { className: Es.gradient }),
                o && s().createElement(_s, { size: e }),
              );
            },
          ),
          ps = ({ size: e, value: t, lineRef: a, disabled: n, onComplete: r }) => {
            const i = (0, u.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              o = 100 === t;
            return (
              (0, u.useEffect)(() => {
                o && r && r();
              }, [o, r]),
              s().createElement(gs, {
                size: e,
                disabled: n,
                baseStyles: i,
                isComplete: o,
                lineRef: a,
              })
            );
          };
        let fs, As;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(fs || (fs = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(As || (As = {})));
        const hs = "ProgressBarDeltaSimple_base_6c",
          vs = "ProgressBarDeltaSimple_delta_99",
          bs = (0, u.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: n,
              size: r,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
            }) => {
              const c = i < n,
                m = (0, u.useState)(As.Idle),
                d = m[0],
                _ = m[1],
                E = d === As.In,
                g = d === As.End,
                p = d === As.Idle,
                f = (0, u.useCallback)(
                  (e) => {
                    (_(e), l && l(e));
                  },
                  [l],
                );
              ((0, u.useEffect)(() => {
                if (p && !a) {
                  return Ra(() => {
                    f(As.In);
                  }, t);
                }
              }, [f, a, p, t]),
                (0, u.useEffect)(() => {
                  if (E) {
                    return Ra(() => {
                      (o && o(), f(As.End));
                    }, e + t);
                  }
                }, [f, E, o, t, e]));
              const A = (0, u.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                h = (0, u.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                v = (0, u.useMemo)(
                  () => ({ width: `${Math.abs(n - i)}%`, left: `${c ? i : n}%` }),
                  [n, c, i],
                );
              return g
                ? null
                : s().createElement(
                    "div",
                    { className: hs, style: v },
                    s().createElement(
                      "div",
                      { style: p ? A : h, className: vs },
                      s().createElement(_s, { size: r }),
                    ),
                  );
            },
          ),
          Fs = (0, u.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: n,
              disabled: r,
              isComplete: i,
              animationSettings: o,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const m = (0, u.useMemo)(
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
                s().createElement(gs, {
                  size: t,
                  lineRef: n,
                  disabled: r,
                  isComplete: i,
                  baseStyles: m,
                }),
                a >= 0 &&
                  s().createElement(bs, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    freezed: o.freezed,
                    from: a,
                    size: t,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          Ds = "ProgressBarDeltaGrow_base_7e",
          Cs = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          Bs = "ProgressBarDeltaGrow_glow_68",
          ws = (e) => (e ? { left: 0 } : { right: 0 }),
          Ss = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          ys = (e) => ({ transitionDuration: `${e}ms` }),
          Rs = (0, u.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: n,
              size: r,
              to: i,
              onEndAnimation: o,
              onChangeAnimationState: l,
              className: c,
            }) => {
              const m = i < n,
                d = (0, u.useState)(fs.Idle),
                _ = d[0],
                E = d[1],
                g = _ === fs.End,
                p = _ === fs.Idle,
                f = _ === fs.Grow,
                A = _ === fs.Shrink,
                h = (0, u.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                ),
                v = (0, u.useCallback)(
                  (e, t) =>
                    Ra(() => {
                      h(e);
                    }, t),
                  [h],
                );
              (0, u.useEffect)(() => {
                if (!a)
                  return p
                    ? v(fs.Grow, t)
                    : f
                      ? v(fs.Shrink, e)
                      : A
                        ? v(fs.End, e)
                        : void (g && o && o());
              }, [v, a, g, f, p, A, o, t, e]);
              const b = (0, u.useMemo)(
                  () => Object.assign({ width: "100%" }, ys(e), ws(m)),
                  [m, e],
                ),
                D = (0, u.useMemo)(() => Object.assign({ width: "0%" }, ys(e), ws(m)), [m, e]),
                C = (0, u.useMemo)(
                  () => Object.assign({ width: "0%" }, Ss(m, n), ys(e)),
                  [n, m, e],
                ),
                B = (0, u.useMemo)(
                  () => Object.assign({ width: `${Math.abs(i - n)}%` }, Ss(m, n), ys(e)),
                  [n, m, i, e],
                );
              if (g) return null;
              const w = F()(Ds, c, m && 0 === i && Cs);
              return s().createElement(
                "div",
                { style: p ? C : B, className: w },
                s().createElement(
                  "div",
                  { style: A ? D : b, className: Bs },
                  s().createElement(_s, { size: r }),
                ),
              );
            },
          ),
          xs = (0, u.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: n,
              disabled: r,
              isComplete: i,
              animationSettings: o,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const m = e < a,
                d = (0, u.useState)(!1),
                _ = d[0],
                E = d[1],
                g = (0, u.useCallback)(
                  (e) => {
                    (e === fs.Shrink && E(!0), c && c(e));
                  },
                  [c],
                ),
                p = (0, u.useMemo)(() => ({ width: `${a}%`, transitionProperty: "none" }), [a]),
                f = (0, u.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${o.line.duration}ms` }),
                  [o.line.duration, e],
                );
              return s().createElement(
                s().Fragment,
                null,
                s().createElement(gs, {
                  size: t,
                  lineRef: n,
                  disabled: r,
                  isComplete: i,
                  withoutBounce: m && 0 === e,
                  baseStyles: _ ? f : p,
                }),
                a >= 0 &&
                  s().createElement(Rs, {
                    transitionDuration: o.delta.duration,
                    transitionDelay: o.delta.delay,
                    onChangeAnimationState: g,
                    freezed: o.freezed,
                    onEndAnimation: l,
                    from: a,
                    size: t,
                    to: e,
                    className: o.delta.className,
                  }),
              );
            },
          ),
          Ps = ["onComplete", "onEndAnimation"];
        function ks() {
          return (
            (ks =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            ks.apply(this, arguments)
          );
        }
        const Ts = (0, u.memo)((e) => {
            let t = e.onComplete,
              a = e.onEndAnimation,
              n = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Ps);
            const r = (0, u.useState)(!1),
              i = r[0],
              o = r[1],
              l = (0, u.useCallback)(() => {
                const e = 100 === n.to;
                (e !== i && o(e), e && t && t(), a && a());
              }, [i, t, a, n.to]);
            switch (n.animationSettings.type) {
              case cs.Simple:
                return s().createElement(Fs, ks({}, n, { onEndAnimation: l, isComplete: i }));
              case cs.Growing:
                return s().createElement(xs, ks({}, n, { onEndAnimation: l, isComplete: i }));
              default:
                return null;
            }
          }),
          Ls = ["onEndAnimation"];
        function Ns() {
          return (
            (Ns =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ns.apply(this, arguments)
          );
        }
        const Is = (0, u.memo)((e) => {
          let t = e.onEndAnimation,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, Ls);
          const n = (0, u.useRef)({}),
            r = (0, u.useCallback)(() => {
              ((n.current.from = void 0), t && t());
            }, [t]),
            i = "number" == typeof n.current.from ? n.current.from : a.from;
          return (
            (n.current.from = i),
            s().createElement(Ts, Ns({}, a, { onEndAnimation: r, key: `${i}-${a.to}`, from: i }))
          );
        });
        function Ms() {
          return (
            (Ms =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ms.apply(this, arguments)
          );
        }
        const Os = (0, u.memo)(
            ({
              size: e,
              value: t,
              lineRef: a,
              disabled: n,
              deltaFrom: r,
              animationSettings: u,
              onEndAnimation: i,
              onChangeAnimationState: o,
              onComplete: l,
            }) => {
              if (r === t)
                return s().createElement(ps, {
                  key: `${r}-${t}`,
                  size: e,
                  value: t,
                  lineRef: a,
                  disabled: n,
                  onComplete: l,
                });
              const c = {
                from: r,
                to: t,
                size: e,
                lineRef: a,
                disabled: n,
                animationSettings: u,
                onComplete: l,
                onEndAnimation: i,
                onChangeAnimationState: o,
              };
              return u.withStack
                ? s().createElement(Is, c)
                : s().createElement(Ts, Ms({ key: `${r}-${t}` }, c));
            },
          ),
          Hs = (e) => ({
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
          Ws = (e, t, a) => {
            if ("number" == typeof a) {
              return (lu(0, t, a) / t) * 100;
            }
            return e;
          },
          $s = {
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
          zs = {
            freezed: !1,
            withStack: !1,
            type: cs.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          Us = (0, u.memo)(
            ({
              maxValue: e = 100,
              theme: t = $s,
              size: a = ls.Default,
              animationSettings: n = zs,
              disabled: r = !1,
              withoutBackground: i = !1,
              progressBarBackgroundClassMix: o,
              value: l,
              deltaFrom: c,
              lineRef: m,
              onChangeAnimationState: d,
              onEndAnimation: _,
              onComplete: E,
            }) => {
              const g = ((e, t, a) =>
                (0, u.useMemo)(() => {
                  const n = (lu(0, t, e) / t) * 100;
                  return { value: n, deltaFrom: Ws(n, t, a) };
                }, [a, t, e]))(l, e, c);
              return s().createElement(
                "div",
                { className: F()(os.base, os[`base__${a}`]), style: Hs(t) },
                !i && s().createElement(ms, { size: a, classMix: o }),
                s().createElement(Os, {
                  size: a,
                  lineRef: m,
                  disabled: r,
                  value: g.value,
                  deltaFrom: g.deltaFrom,
                  animationSettings: n,
                  onEndAnimation: _,
                  onChangeAnimationState: d,
                  onComplete: E,
                }),
              );
            },
          ),
          Gs = "ProgressionDivision_base_6e",
          qs = "ProgressionDivision_highlightContainer_3d",
          Vs = "ProgressionDivision_radialBack_d2",
          js = "ProgressionDivision_mainBack_d2",
          Xs = "ProgressionDivision_bottomLine_f5",
          Qs = "ProgressionDivision_bottomLine__first_d9",
          Ys = "ProgressionDivision_bottomLine__second_8d",
          Ks = "ProgressionDivision_bottomLine__third_91",
          Zs = "ProgressionDivision_divisionText_c7",
          Js = "ProgressionDivision_divisionText__current_74",
          ei = "ProgressionDivision_note_53",
          ti = ({ rank: e, division: t, isCurrentDivision: a }) => {
            const n = F()(Zs, a && Js);
            return s().createElement(
              ze,
              {
                contentId: R.views.lobby.comp7.tooltips.DivisionTooltip("resId"),
                args: {
                  rank: e,
                  division: t.name,
                  from: t.from,
                  to: t.to + 1,
                  type: t.type,
                  elitePercent: t.elitePercent,
                },
              },
              s().createElement(
                "div",
                { className: Gs },
                a &&
                  s().createElement(
                    "div",
                    { className: qs },
                    s().createElement("div", { className: Vs }),
                    s().createElement("div", { className: js }),
                    s().createElement("div", { className: F()(Xs, Qs) }),
                    s().createElement("div", { className: F()(Xs, Ys) }),
                    s().createElement("div", { className: F()(Xs, Ks) }),
                  ),
                s().createElement(
                  "div",
                  { className: n },
                  a && s().createElement("div", { className: ei }, R.strings.comp7.division.note()),
                  pa(t.name),
                ),
              ),
            );
          },
          ai = "RankProgressDivisions_base_54",
          ni = (0, W.Pi)(({ itemIndex: e, rank: t, customDivisions: a }) => {
            const n = wa().model,
              r = null != a ? a : n.computes.divisions(e);
            return s().createElement(
              "div",
              { className: ai },
              be(r, (e) => {
                const a = e.state === na.Current;
                return s().createElement(ti, {
                  key: e.name,
                  rank: t,
                  division: e,
                  isCurrentDivision: a,
                });
              }),
            );
          }),
          ri = {
            point: "RankProgressPoint_point_b1",
            point__top: "RankProgressPoint_point__top_d2",
            point__bottom: "RankProgressPoint_point__bottom_d9",
            pointLine: "RankProgressPoint_pointLine_56",
            pointLine__extended: "RankProgressPoint_pointLine__extended_05",
            pointLine__top: "RankProgressPoint_pointLine__top_0e",
            pointLine__bottom: "RankProgressPoint_pointLine__bottom_ee",
            pointValue: "RankProgressPoint_pointValue_22",
            pointValue__highlight: "RankProgressPoint_pointValue__highlight_65",
            pointValue__top: "RankProgressPoint_pointValue__top_a7",
            pointValue__bottom: "RankProgressPoint_pointValue__bottom_7a",
          },
          ui = ({
            value: e,
            isHighlightPointValue: t,
            isHaveExtendedPointLine: a,
            style: n,
            direction: r,
          }) => {
            const u = "number" == typeof e ? s().createElement(Ja, { value: e }) : e,
              i = F()(ri.point, ri[`point__${r}`]),
              o = F()(ri.pointLine, ri[`pointLine__${r}`], a && ri.pointLine__extended),
              l = F()(ri.pointValue, ri[`pointValue__${r}`], t && ri.pointValue__highlight);
            return s().createElement(
              "div",
              { className: i, style: n },
              s().createElement("div", { className: o }),
              void 0 !== e && s().createElement("div", { className: l }, u),
            );
          },
          si = { "--pointLineWidth": "1rem", base: "RankProgressPoints_base_86" };
        let ii, oi;
        (!(function (e) {
          ((e.Top = "top"), (e.Bottom = "bottom"));
        })(ii || (ii = {})),
          (function (e) {
            ((e[(e.Start = 0)] = "Start"), (e[(e.End = 1)] = "End"), (e[(e.All = 2)] = "All"));
          })(oi || (oi = {})));
        const li = (e, t) => {
            const a = t > 0 ? (100 / t) * e + "%" : "0%";
            return e === t
              ? { left: a, transform: `translateX(-${si["--pointLineWidth"]})` }
              : { left: a };
          },
          ci = { [oi.Start]: (e) => e % 2 == 0, [oi.End]: (e) => e % 2 == 1, [oi.All]: () => !0 },
          mi = ({
            divisionsCount: e,
            from: t,
            currentDivisionIndex: a,
            direction: n = ii.Bottom,
            viewPosition: r = oi.All,
            divisions: u,
          }) => {
            const i = n === ii.Bottom ? ci[r] : () => !1,
              o = Math.max(0, e),
              l = (e, a) => {
                var n;
                return (
                  t ||
                  (e === o
                    ? (null != (n = null == a ? void 0 : a.to) ? n : 0) + 1
                    : null == a
                      ? void 0
                      : a.from)
                );
              };
            return s().createElement(
              "div",
              { className: F()(si.base, si[`base__${n}`]) },
              u
                ? su(o + 1, (e) => {
                    const r = u[e === o ? e - 1 : e],
                      c = !t && void 0 !== a && e === a + 1,
                      m = void 0 !== a && e === a,
                      d = void 0 === (null == r ? void 0 : r.from) && (m || c),
                      _ = Boolean(t) && void 0 !== a && e === a - 1;
                    return s().createElement(ui, {
                      key: `${null == r ? void 0 : r.name}-${e}`,
                      value: i(e) ? l(e, r) : void 0,
                      isHighlightPointValue: c || _,
                      isHaveExtendedPointLine: d,
                      style: li(e, o),
                      direction: n,
                    });
                  })
                : s().createElement(ui, {
                    value: t,
                    isHighlightPointValue: !0,
                    isHaveExtendedPointLine: !0,
                    style: li(0, 1),
                    direction: n,
                  }),
            );
          },
          di = {
            "--pageContentWidth": "78vw",
            base: "RankProgress_base_97",
            base__hidden: "RankProgress_base__hidden_b9",
            base__inactive: "RankProgress_base__inactive_49",
            base__active: "RankProgress_base__active_a2",
            progressWrapper: "RankProgress_progressWrapper_4e",
          },
          _i = {
            freezed: !0,
            withStack: !1,
            type: cs.Simple,
            delta: { duration: 0, delay: 0 },
            line: { duration: 0, delay: 0 },
          },
          Ei = (0, W.Pi)(({ itemIndex: e, progressState: t }) => {
            const a = wa().model,
              n = a.root.get().currentScore,
              r = a.qualificationModel.isActive.get(),
              u = a.computes.item(e).rank,
              i = a.computes.rankSettings(e, r).state,
              o = a.computes.divisionsConfig(e),
              l = a.computes.divisions(e).filter((e) => e.type === ba.BASIC),
              c = l.length,
              m = Da(l),
              d = m.from,
              _ = m.to - d,
              E = 105 * c;
            return s().createElement(
              "div",
              { style: { width: `${E}rem` }, className: F()(di.base, di[`base__${t}`]) },
              s().createElement(ni, { itemIndex: e, rank: u, customDivisions: l }),
              s().createElement(mi, {
                divisionsCount: c,
                direction: ii.Top,
                currentDivisionIndex: o.currentDivisionIndex,
                divisions: l,
              }),
              s().createElement(
                "div",
                { className: di.progressWrapper },
                i === ha.Current
                  ? s().createElement(Us, { maxValue: _, value: n - d, animationSettings: _i })
                  : s().createElement(Us, { maxValue: _, value: n < d ? 0 : _, disabled: n < d }),
              ),
              s().createElement(mi, {
                divisionsCount: c,
                currentDivisionIndex: o.currentDivisionIndex,
                divisions: l,
              }),
            );
          }),
          gi = "HighlightedRectangles_base_4c",
          pi = "HighlightedRectangles_triangle_ae",
          fi = "HighlightedRectangles_running_cc",
          Ai = ({ isVisible: e }) => {
            const t = F()(gi, e && fi);
            return s().createElement(
              "div",
              { className: t },
              s().createElement("div", { className: pi }),
              s().createElement("div", { className: pi }),
              s().createElement("div", { className: pi }),
            );
          },
          hi = {
            "--pageContentWidth": "78vw",
            base: "RankTransferProgression_base_28",
            transferProgression: "RankTransferProgression_transferProgression_8c",
            transferProgression__inactive:
              "RankTransferProgression_transferProgression__inactive_87",
            progressWrapper: "RankTransferProgression_progressWrapper_f9",
            default: "RankTransferProgression_default_35",
            complete: "RankTransferProgression_complete_e7",
            visible: "RankTransferProgression_visible_c9",
            fadeIn: "RankTransferProgression_fadeIn_17",
            fadeInThreeQuarters: "RankTransferProgression_fadeInThreeQuarters_31",
            fadeInHalf: "RankTransferProgression_fadeInHalf_ee",
            fadeOut: "RankTransferProgression_fadeOut_9d",
            fadeInWithScale: "RankTransferProgression_fadeInWithScale_f9",
            slideUp: "RankTransferProgression_slideUp_2b",
            scale: "RankTransferProgression_scale_28",
            raysAppearance: "RankTransferProgression_raysAppearance_59",
            rotate: "RankTransferProgression_rotate_3d",
            "reverse-rotate": "RankTransferProgression_reverse-rotate_19",
            glowAppearance: "RankTransferProgression_glowAppearance_5c",
            highlightAppearance: "RankTransferProgression_highlightAppearance_12",
            blink: "RankTransferProgression_blink_12",
            slideUpIn: "RankTransferProgression_slideUpIn_f3",
          },
          vi = (0, W.Pi)(({ itemIndex: e, progressState: t }) => {
            var a, n;
            const r = wa().model,
              u = r.computes.modelItems(),
              i = r.computes.divisionsConfig(e),
              o = r.computes.divisionsByType(e, ba.TRANSFER),
              l = u.findIndex((e) => e.divisions.findIndex((e) => e.type === ba.TRANSFER) > -1),
              c = null == u ? void 0 : u[l],
              m =
                null !=
                (a =
                  null == c || null == (n = c.divisions)
                    ? void 0
                    : n.findIndex((e) => e.type === ba.TRANSFER && e.state === na.Current))
                  ? a
                  : -1,
              d = e === l && m === i.currentDivisionIndex,
              _ = r.computes.rankSettings(e, !1).state === ha.Previous;
            return s().createElement(
              "div",
              { className: hi.base },
              s().createElement(Ei, { itemIndex: e, progressState: t }),
              s().createElement(
                "div",
                { className: F()(hi.transferProgression, hi[`transferProgression__${t}`]) },
                s().createElement(ni, { itemIndex: e, rank: c.rank, customDivisions: o }),
                s().createElement(mi, {
                  divisionsCount: 1,
                  direction: ii.Top,
                  currentDivisionIndex: i.currentDivisionIndex,
                  divisions: o,
                }),
                s().createElement(
                  "div",
                  { className: hi.progressWrapper },
                  s().createElement("div", { className: hi.default }),
                  s().createElement("div", { className: F()(hi.complete, _ && hi.visible) }),
                  s().createElement(Ai, { isVisible: d }),
                ),
                s().createElement(mi, {
                  divisionsCount: 1,
                  direction: ii.Bottom,
                  currentDivisionIndex: i.currentDivisionIndex,
                  from: R.strings.comp7.rankTransferProgression.transferPoint(),
                  viewPosition: oi.End,
                  divisions: o,
                }),
              ),
            );
          }),
          bi = "AchievedRankStatus_base_70",
          Fi = (0, W.Pi)(({ itemIndex: e, progressState: t }) => {
            const a = wa().model.computes.item(e).rank;
            switch (a) {
              case $u.First:
              case $u.Second:
              case $u.Third:
              case $u.Fourth:
                return s().createElement(Ei, { itemIndex: e, progressState: t });
              case $u.Fifth:
                return s().createElement(
                  "div",
                  { className: bi },
                  s().createElement(vi, { itemIndex: e, progressState: t }),
                );
              default:
                return (
                  console.warn(`Status for rank '${a}' was not mapped to any react component.`),
                  null
                );
            }
          }),
          Di = "LinkButton_base_fa",
          Ci = { mouseEnter: "highlight", click: "play" },
          Bi = ({ onClick: e, children: t, className: a }) => {
            const n = (e) => {
              const t = Ci[e];
              t && $(t);
            };
            return s().createElement(
              "div",
              {
                className: F()(Di, a),
                onClick: (t) => {
                  (n("click"), e(t));
                },
                onMouseEnter: () => {
                  n("mouseEnter");
                },
                onMouseLeave: () => {
                  n("mouseLeave");
                },
              },
              t,
            );
          },
          wi = "HonorRankDescription_base_fd",
          Si = "HonorRankDescription_text_38",
          yi = "HonorRankDescription_button_88",
          Ri = R.strings.comp7.honorRankDescription,
          xi = (0, W.Pi)(() => {
            var e, t, a;
            const n = wa(),
              r = n.model,
              u = n.controls,
              i = r.computes.modelItems(),
              o = i.flatMap((e) => e.divisions).find((e) => e.type === ba.TRANSFER),
              l = i.find((e) => e.divisions.filter((e) => e.type === ba.ELITE).length > 0),
              c = null != (e = null == o ? void 0 : o.from) ? e : 0,
              m = null != (t = Aa(null != (a = null == l ? void 0 : l.divisions) ? a : [])) ? t : 0;
            return s().createElement(
              "div",
              { className: wi },
              s().createElement(kn, {
                text: Ri.text(),
                binding: {
                  pointCount: s().createElement(
                    s().Fragment,
                    null,
                    X.Z5.getNumberFormat(c, X.B3.INTEGRAL),
                  ),
                  button: s().createElement(
                    s().Fragment,
                    null,
                    s().createElement(
                      Bi,
                      { className: yi, onClick: () => u.goToLeaderboardPage() },
                      Ri.button(),
                    ),
                    s().createElement(Sn, { text: Ri.dot(), className: Si }),
                  ),
                  percent: m,
                },
                classMix: Si,
              }),
            );
          }),
          Pi = "RankEliteProgression_base_4d",
          ki = "RankEliteProgression_elite_00",
          Ti = "RankEliteProgression_elitePercent_61",
          Li = "RankEliteProgression_elitePercent__current_d1",
          Ni = (0, W.Pi)(({ itemIndex: e }) => {
            const t = wa().model,
              a = t.computes.item(e).rank,
              n = t.computes.divisions(e);
            return s().createElement(
              s().Fragment,
              null,
              s().createElement(
                "div",
                { className: Pi },
                be(n, (e) => {
                  const t = e.state === na.Current;
                  return s().createElement(ti, {
                    key: e.name,
                    rank: a,
                    division: e,
                    isCurrentDivision: t,
                  });
                }),
              ),
              s().createElement(
                "div",
                { className: ki },
                be(n, (e, t) => {
                  const a = e.state === na.Current;
                  return s().createElement(Sn, {
                    key: t,
                    text: R.strings.comp7.division.elite(),
                    format: { binding: { elitePercent: e.elitePercent } },
                    className: F()(Ti, a && Li),
                  });
                }),
              ),
            );
          });
        let Ii;
        !(function (e) {
          ((e.Active = "active"), (e.Inactive = "inactive"), (e.Hidden = "hidden"));
        })(Ii || (Ii = {}));
        const Mi = "CurrentRankStatus_base_d4",
          Oi = (0, W.Pi)(({ itemIndex: e, progressState: t }) => {
            const a = wa().model,
              n = a.computes.item(e).rank,
              r = a.qualificationModel.isActive.get(),
              i = a.computes.rankSettings(e, r).division;
            return (
              (0, u.useEffect)(() => {
                t === Ii.Active && $("comp_7_progression_rank_active");
              }, [t]),
              s().createElement(
                "div",
                { className: Mi },
                (() => {
                  switch (n) {
                    case $u.First:
                    case $u.Second:
                    case $u.Third:
                    case $u.Fourth:
                      return s().createElement(Ei, { itemIndex: e, progressState: t });
                    case $u.Fifth:
                      return s().createElement(
                        "div",
                        { className: Mi },
                        s().createElement(vi, { itemIndex: e, progressState: t }),
                        i === aa.A && s().createElement(xi, null),
                      );
                    case $u.Sixth:
                      return s().createElement(
                        "div",
                        { className: Mi },
                        s().createElement(Ni, { itemIndex: e }),
                        s().createElement(xi, null),
                      );
                    default:
                      return (
                        console.warn(
                          `Status for rank '${n}' was not mapped to any react component.`,
                        ),
                        null
                      );
                  }
                })(),
              )
            );
          }),
          Hi = "RankStatusDescription_base_07",
          Wi = ({ text: e, binding: t, className: a }) => {
            const n = ((e) =>
              "number" == typeof (null == e ? void 0 : e.pointsCount)
                ? Object.assign({}, e, {
                    pointsCount: s().createElement(Ja, { value: e.pointsCount }),
                  })
                : e)(t);
            return s().createElement(kn, { text: e, binding: n, classMix: F()(Hi, a) });
          },
          $i = "FutureRankStatus_base_c2",
          zi = "FutureRankStatus_lock_d0",
          Ui = (0, W.Pi)(({ itemIndex: e }) => {
            const t = wa().model,
              a = t.computes.item(e).rank,
              n = t.computes.rankPointsDiapason(e),
              r = n.from,
              i = n.to,
              o = (0, u.useMemo)(() => {
                const e = s().createElement(Ja, { value: r }),
                  t = s().createElement(Ja, { value: i + 1 });
                return a === $u.Fifth ? { fromScore: e } : { fromScore: e, toScore: t };
              }, [r, i, a]);
            return s().createElement(
              "div",
              { className: $i },
              s().createElement("div", { className: zi }),
              a === $u.Sixth
                ? s().createElement(xi, null)
                : s().createElement(Wi, {
                    text: Uu(R.strings.comp7.rankItemStatus.future.description, a),
                    binding: o,
                  }),
            );
          }),
          Gi = ({ rankState: e, itemIndex: t, progressState: a }) => {
            switch (e) {
              case ha.Previous:
                return s().createElement(Fi, { itemIndex: t, progressState: a });
              case ha.Current:
                return s().createElement(Oi, { itemIndex: t, progressState: a });
              case ha.Future:
                return s().createElement(Ui, { itemIndex: t });
              default:
                return (
                  console.error(`Unreachable code for state '${e}' in RankStatusResolver.`),
                  null
                );
            }
          };
        let qi;
        !(function (e) {
          ((e.Progress = "progress"), (e.Text = "text"));
        })(qi || (qi = {}));
        const Vi = {
            "--pageContentWidth": "78vw",
            base: "RankItem_base_60",
            rankEmblem__future: "RankItem_rankEmblem__future_08",
            rankDescription: "RankItem_rankDescription_32",
            rankDescription__text: "RankItem_rankDescription__text_90",
            rankDescription__progress: "RankItem_rankDescription__progress_e2",
            rankDescription__viewed: "RankItem_rankDescription__viewed_6b",
            rankInfo: "RankItem_rankInfo_6f",
            dividerContainer: "RankItem_dividerContainer_0f",
            fadeIn: "RankItem_fadeIn_95",
            fadeInThreeQuarters: "RankItem_fadeInThreeQuarters_f1",
            fadeInHalf: "RankItem_fadeInHalf_8a",
            fadeOut: "RankItem_fadeOut_56",
            fadeInWithScale: "RankItem_fadeInWithScale_68",
            slideUp: "RankItem_slideUp_74",
            scale: "RankItem_scale_6b",
            raysAppearance: "RankItem_raysAppearance_a8",
            rotate: "RankItem_rotate_da",
            "reverse-rotate": "RankItem_reverse-rotate_3e",
            glowAppearance: "RankItem_glowAppearance_90",
            highlightAppearance: "RankItem_highlightAppearance_5c",
            blink: "RankItem_blink_7e",
            slideUpIn: "RankItem_slideUpIn_ee",
          },
          ji = (0, W.Pi)(({ itemIndex: e, isViewed: t, hasDivider: a = !0 }) => {
            const n = wa().model,
              r = n.qualificationModel.isActive.get(),
              u = y().mediaSize,
              i = n.computes.item(e).rank,
              o = n.computes.rankPointsDiapason(e),
              l = o.from,
              c = o.to,
              m = n.computes.divisionsConfig(e),
              d = n.computes.rankSettings(e, r),
              _ = d.state,
              E = d.division,
              g = ((e) => {
                switch (!0) {
                  case e >= B.ExtraLarge:
                    return Ku.x420;
                  case e >= B.Large:
                    return Ku.x320;
                  case e >= B.Medium:
                    return Ku.x260;
                  default:
                    return Ku.x200;
                }
              })(u),
              p = us(_, i, r),
              f = ((e, t) => (t ? (e === ha.Current ? Ii.Active : Ii.Inactive) : Ii.Hidden))(_, t),
              A = ((e, t) => {
                const a = Qu(t);
                switch (e) {
                  case ha.Previous:
                  case ha.Current:
                    return a ? qi.Progress : qi.Text;
                  default:
                    return qi.Text;
                }
              })(_, i);
            return s().createElement(
              "div",
              { className: Vi.base },
              s().createElement(
                ze,
                {
                  contentId: R.views.lobby.comp7.tooltips.GeneralRankTooltip("resId"),
                  args: {
                    rank: i,
                    divisions: m.list,
                    from: l,
                    to: c + 1,
                    elitePercent: m.elitePercent,
                  },
                },
                s().createElement(
                  "div",
                  null,
                  s().createElement(ns, {
                    size: g,
                    rank: i,
                    division: E,
                    state: p,
                    classNames: { rankEmblem: Vi[`rankEmblem__${_}`] },
                  }),
                ),
              ),
              s().createElement(
                "div",
                {
                  className: F()(
                    Vi.rankDescription,
                    Vi[`rankDescription__${A}`],
                    t && Vi.rankDescription__viewed,
                  ),
                },
                s().createElement(Gi, { rankState: _, itemIndex: e, progressState: f }),
              ),
              a &&
                s().createElement(
                  "div",
                  { className: Vi.dividerContainer, style: { "--emblemSize": `${g}rem` } },
                  s().createElement(is, null),
                ),
            );
          }),
          Xi = "RankItemContainer_base_b3",
          Qi = "RankItemContainer_title_d5",
          Yi = "RankItemContainer_title__active_f0",
          Ki = (0, W.Pi)(
            ({ itemIndex: e, itemWidth: t, isViewed: a, onMouseDown: n, hasDivider: r }) => {
              const u = wa().model.computes.item(e);
              return s().createElement(
                "div",
                { className: Xi, style: { "--itemWidth": `${t}rem` }, onMouseDown: n },
                s().createElement("div", { className: F()(Qi, a && Yi) }, qu(u.rank)),
                s().createElement(ji, { itemIndex: e, isViewed: a, hasDivider: r }),
              );
            },
          ),
          Zi = "Progression_base_97",
          Ji = { base: "Progression_areaContainer_09", wrapper: "Progression_areaWrapper_5f" },
          eo = { base: "Progression_bar_4d" },
          to = (0, W.Pi)(
            ({
              staticContent: e,
              className: t,
              currentViewedItemIndex: a,
              setCurrentViewedItemIndex: n,
            }) => {
              const r = wa().model,
                i = r.root.get().currentItemIndex,
                o = r.computes.itemsLength(),
                l = y().mediaSize,
                c = uu(),
                m = ((e) =>
                  e >= B.ExtraLarge ? 640 : e >= B.Large ? 500 : e >= B.Medium ? 440 : 400)(l),
                d = ou(m),
                _ = Wu(m),
                E = (0, u.useCallback)(
                  (e) => () => {
                    (z.playClick(), n(e));
                  },
                  [n],
                );
              return (
                (0, u.useLayoutEffect)(() => {
                  _.scrollPosition.start({ scrollPosition: viewEnv.remToPx(i * m), immediate: !0 });
                }, [c]),
                s().createElement(
                  Hu,
                  {
                    api: _,
                    stuckIndex: a,
                    itemWidth: m,
                    itemsOffset: d,
                    staticContent: e,
                    onStick: n,
                    className: F()(Zi, t),
                    areaClassNames: Ji,
                    barClassNames: eo,
                  },
                  su(o, (e) =>
                    s().createElement(Ki, {
                      key: e,
                      itemIndex: e,
                      isViewed: a === e,
                      hasDivider: e < o - 1,
                      itemWidth: m,
                      onMouseDown: E(e),
                    }),
                  ),
                )
              );
            },
          ),
          ao = R.strings.comp7.qualification,
          no = { hasHtmlContent: !0 },
          ro = ({ maxBattlesCount: e, children: t }) =>
            s().createElement(
              Ve,
              {
                header: ao.conditionTooltip.header(),
                body: ia(ao.conditionTooltip.body(e), { maxBattlesCount: e }),
                args: no,
              },
              s().createElement("div", null, t),
            ),
          uo = "BattlesCounter_base_f1",
          so = "BattlesCounter_battlesCount_ef",
          io = ({ battlesCount: e, maxBattlesCount: t, className: a }) =>
            s().createElement(Ia, {
              text: R.strings.comp7.qualification.counter(),
              binding: {
                battlesCount: s().createElement("div", { className: so }, e),
                maxBattlesCount: t,
              },
              classMix: F()(uo, a),
            }),
          oo = {
            "--pageContentWidth": "78vw",
            base: "QualificationBattleItem_base_0d",
            base__size_234: "QualificationBattleItem_base__size_234_ab",
            battleBackground: "QualificationBattleItem_battleBackground_67",
            base__inProgress: "QualificationBattleItem_base__inProgress_2a",
            blink: "QualificationBattleItem_blink_3b",
            fadeIn: "QualificationBattleItem_fadeIn_c9",
            fadeInThreeQuarters: "QualificationBattleItem_fadeInThreeQuarters_20",
            fadeInHalf: "QualificationBattleItem_fadeInHalf_89",
            fadeOut: "QualificationBattleItem_fadeOut_c3",
            fadeInWithScale: "QualificationBattleItem_fadeInWithScale_4f",
            slideUp: "QualificationBattleItem_slideUp_1f",
            scale: "QualificationBattleItem_scale_37",
            raysAppearance: "QualificationBattleItem_raysAppearance_8f",
            rotate: "QualificationBattleItem_rotate_2d",
            "reverse-rotate": "QualificationBattleItem_reverse-rotate_9d",
            glowAppearance: "QualificationBattleItem_glowAppearance_56",
            highlightAppearance: "QualificationBattleItem_highlightAppearance_a0",
            slideUpIn: "QualificationBattleItem_slideUpIn_be",
          },
          lo = {
            notPlayed: "notFinished",
            inProgress: "notFinished",
            victory: "victory",
            defeat: "defeat",
          },
          co = { x173: 173, x234: 234 },
          mo = ({ className: e, state: t, size: a = "x173" }) => {
            const n = co[a],
              r = R.images.comp7.gui.maps.icons.comp7.icons.$dyn(`battle_${lo[t]}`);
            return s().createElement(
              "div",
              { className: F()(oo.base, e, oo[`base__${t}`], oo[`base__size_${n}`]) },
              s().createElement("div", {
                className: oo.battleBackground,
                style: { backgroundImage: `url(${r})`, "--imageSize": `${n}rem` },
              }),
            );
          },
          _o = (0, W.Pi)(({ index: e, className: t }) => {
            const a = wa().model,
              n = y().mediaSize,
              r = a.computes.qualificationBattle(e);
            return s().createElement(mo, {
              state: r.state,
              className: t,
              key: e,
              size: n >= B.ExtraLarge ? "x234" : "x173",
            });
          }),
          Eo = "BattlesProgression_base_a1",
          go = "BattlesProgression_item_73",
          po = (0, W.Pi)(({ className: e }) => {
            const t = wa().model;
            return s().createElement(
              "div",
              { className: F()(Eo, e) },
              su(t.computes.qualificationBattlesLength(), (e) =>
                s().createElement(_o, { index: e, className: go, key: e }),
              ),
            );
          }),
          fo = "Qualification_base_0f",
          Ao = "Qualification_content_64",
          ho = "Qualification_footer_8f",
          vo = "Qualification_qualificationEmblem_e2",
          bo = "Qualification_battlesProgression_51",
          Fo = "Qualification_counterDescription_20",
          Do = "Qualification_ratingCalculationDescription_7a",
          Co = "Qualification_timerIcon_35",
          Bo = "Qualification_conditionContainer_c4",
          wo = "Qualification_condition_23",
          So = "Qualification_rewardsDescription_c2",
          yo = "Qualification_infoIcon_fe",
          Ro = "Qualification_rewardsButton_db",
          xo = "Qualification_buttonIcon_39",
          Po = "Qualification_waiting_de",
          ko = R.strings.comp7.qualification,
          To = { base: Ro, icon: xo },
          Lo = (0, W.Pi)(({ className: e }) => {
            const t = wa(),
              a = t.model,
              n = t.controls,
              r = a.qualificationModel.battlesCount.get(),
              u = a.qualificationModel.maxBattlesCount.get(),
              i = a.qualificationModel.isRatingCalculation.get(),
              o = a.isParallaxPreloaded.get(),
              l = (0, Pe.useSpring)({
                from: { opacity: 0 },
                to: ee() ? { opacity: o ? 1 : 0 } : { opacity: 1 },
                delay: 300,
                config: { duration: 300 },
              });
            return ee() && !o
              ? s().createElement("div", { className: Po }, s().createElement(pt, null))
              : s().createElement(
                  Pe.animated.div,
                  { style: l, className: F()(fo, e) },
                  s().createElement(
                    "div",
                    { className: Ao },
                    s().createElement("div", { className: vo }),
                    i
                      ? s().createElement(
                          s().Fragment,
                          null,
                          s().createElement(io, { battlesCount: r, maxBattlesCount: u }),
                          s().createElement(
                            Ve,
                            { body: R.strings.comp7.qualification.ratingCalculationTooltip() },
                            s().createElement(
                              "div",
                              null,
                              s().createElement(Ia, {
                                text: ko.ratingCalculationDescription(),
                                binding: { timerIcon: s().createElement("div", { className: Co }) },
                                classMix: Do,
                              }),
                            ),
                          ),
                        )
                      : s().createElement(kn, {
                          text: ko.counterWithDescription(),
                          classMix: Fo,
                          binding: {
                            counter: s().createElement(io, { battlesCount: r, maxBattlesCount: u }),
                          },
                        }),
                    s().createElement(po, { className: bo }),
                  ),
                  s().createElement(
                    "div",
                    { className: ho },
                    s().createElement(
                      "div",
                      { className: Bo },
                      s().createElement(kn, {
                        text: ko.condition(u),
                        classMix: wo,
                        binding: { maxBattlesCount: u },
                      }),
                      s().createElement(
                        ro,
                        { maxBattlesCount: u },
                        s().createElement("div", { className: yo }),
                      ),
                    ),
                    s().createElement(Ia, { text: ko.rewardsDescription(), classMix: So }),
                    s().createElement(V, {
                      caption: ko.rewardsButton(),
                      classNames: To,
                      onMouseEnter: () => n.setRewardLayerVisible(!0),
                      onMouseLeave: () => n.setRewardLayerVisible(!1),
                      onClick: () => n.goToRankRewardsPage(),
                      soundHover: "comp_7_rank_rewards_hover",
                    }),
                  ),
                );
          }),
          No = {
            "--pageContentWidth": "78vw",
            base: "ProgressionPage_base_fa",
            bgLayer: "ProgressionPage_bgLayer_41",
            bgLayer__qualification: "ProgressionPage_bgLayer__qualification_e9",
            bgLayer__iron: "ProgressionPage_bgLayer__iron_79",
            bgLayer__bronze: "ProgressionPage_bgLayer__bronze_46",
            bgLayer__silver: "ProgressionPage_bgLayer__silver_53",
            bgLayer__gold: "ProgressionPage_bgLayer__gold_ef",
            bgLayer__champion: "ProgressionPage_bgLayer__champion_73",
            bgLayer__legend: "ProgressionPage_bgLayer__legend_8f",
            parallaxContainer: "ProgressionPage_parallaxContainer_c4",
            contentWrapper: "ProgressionPage_contentWrapper_cf",
            content: "ProgressionPage_content_4a",
            content__progression: "ProgressionPage_content__progression_c5",
            footer: "ProgressionPage_footer_d1",
            fadeIn: "ProgressionPage_fadeIn_16",
            fadeInThreeQuarters: "ProgressionPage_fadeInThreeQuarters_a8",
            fadeInHalf: "ProgressionPage_fadeInHalf_9d",
            fadeOut: "ProgressionPage_fadeOut_0e",
            fadeInWithScale: "ProgressionPage_fadeInWithScale_ee",
            slideUp: "ProgressionPage_slideUp_e2",
            scale: "ProgressionPage_scale_2c",
            raysAppearance: "ProgressionPage_raysAppearance_a2",
            rotate: "ProgressionPage_rotate_75",
            "reverse-rotate": "ProgressionPage_reverse-rotate_bc",
            glowAppearance: "ProgressionPage_glowAppearance_12",
            highlightAppearance: "ProgressionPage_highlightAppearance_da",
            blink: "ProgressionPage_blink_57",
            slideUpIn: "ProgressionPage_slideUpIn_0f",
          },
          Io = R.strings.comp7.page.heading,
          Mo = (0, W.Pi)(() => {
            const e = wa().model,
              t = e.root.get().currentItemIndex,
              a = (0, u.useState)(t),
              n = a[0],
              r = a[1];
            (0, u.useLayoutEffect)(() => {
              r(t);
            }, [t]);
            const i = Za(n, 200, 500),
              o = i.currentBg,
              l = i.prevBg,
              c = i.spring,
              m = e.qualificationModel.isActive.get(),
              d = (0, Pe.useSpring)(_e);
            return s().createElement(
              "div",
              { className: No.base },
              s().createElement("div", {
                className: F()(No.bgLayer, No[`bgLayer__${m ? "qualification" : o}`]),
              }),
              l &&
                s().createElement(Pe.animated.div, {
                  style: c,
                  className: F()(No.bgLayer, No[`bgLayer__${l}`]),
                }),
              ee() && m && s().createElement(ru, { className: No.parallaxContainer }),
              s().createElement(ya, { className: K }, m ? Io.qualification() : Io.progression()),
              s().createElement(Qa, null),
              m
                ? s().createElement(
                    "div",
                    { className: No.contentWrapper },
                    s().createElement(Lo, { className: No.content }),
                  )
                : s().createElement(
                    Pe.animated.div,
                    { style: d, className: No.contentWrapper },
                    s().createElement(to, {
                      className: F()(No.content, No.content__progression),
                      staticContent: s().createElement(jr, { className: No.footer }),
                      currentViewedItemIndex: n,
                      setCurrentViewedItemIndex: r,
                    }),
                  ),
            );
          }),
          Oo = { context: "model.progressionModel" },
          Ho = ie()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  qualification: e.primitives(["isActive"], "qualificationModel"),
                },
                a = e.array("items"),
                n = (0, Ee.Om)(() => a.get().length),
                r = (0, Ee.Om)(
                  (e) => {
                    const t = Ae(a.get(), e);
                    if (!t) throw new Error(`rank rewards item with index ${e} was not found`);
                    return {
                      hasRewardsReceived: t.hasRewardsReceived,
                      rank: t.rank,
                      from: t.from,
                      to: t.to,
                    };
                  },
                  { equals: ae },
                ),
                u = (0, Ee.Om)(
                  (e) => {
                    const t = Ae(a.get(), e);
                    if (!t) throw new Error(`rank rewards item with index ${e} was not found`);
                    return be(t.rewards, (e) => Object.assign({}, e));
                  },
                  { equals: ae },
                ),
                s = (0, Ee.Om)(
                  (e) => {
                    const t = Ae(u(e), 0);
                    if (!t)
                      throw new Error(
                        `rank rewards item with index ${e} has no any main reward at index: 0`,
                      );
                    return t;
                  },
                  { equals: ae },
                ),
                i = (0, Ee.Om)((e) => [...Fe(u(e), 1)], { equals: ae }),
                o = (0, Ee.Om)((e) => {
                  const t = Ae(a.get(), e);
                  if (!t) throw new Error(`item with index ${e} was not found`);
                  const n = be(t.divisions, (e) => Object.assign({}, e));
                  return fa(n);
                }),
                l = (0, Ee.Om)((e) => {
                  const t = Ae(a.get(), e);
                  if (!t) throw new Error(`item with index ${e} was not found`);
                  const n = be(t.divisions, (e) => Object.assign({}, e));
                  return Aa(n);
                }),
                c = (0, Ee.Om)(
                  () => {
                    const e = Ce(a.get(), (e) => !e.hasRewardsReceived);
                    return {
                      nextNotAchievedItemIndex: null != e ? e : n(),
                      hasForceScroll: -1 !== t.root.get().initialItemIndex,
                    };
                  },
                  { equals: ra },
                );
              return Object.assign({}, t, {
                computes: {
                  rankRewardsItemsLength: n,
                  rankRewardsItem: r,
                  mainReward: s,
                  additionalRewards: i,
                  additionalRewardsCount: (0, Ee.Om)((e) => i(e).length),
                  divisionsString: o,
                  elitePercent: l,
                  scrollingSettings: c,
                },
              });
            },
            ({ externalModel: e, model: t }) => {
              const a = e.createCallback((e, t) => ({ rank: e, index: t }), "onPreviewOpen");
              return {
                openComp7Shop: e.createCallbackNoArgs("onComp7ShopOpen"),
                goToPreview: (0, ne.aD)((e, n) => {
                  const r = t.computes.rankRewardsItem(e).rank;
                  a(r, n);
                }),
              };
            },
          ),
          Wo = Ho[0],
          $o = Ho[1];
        let zo, Uo, Go, qo, Vo, jo, Xo, Qo, Yo;
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
            (e.Entitlements = "entitlements"),
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
            (e.NyPetGoodies = "nyPetGoodies"),
            (e.HiddenVehicle = "hidden_vehicle"),
            (e.NyStaticDogTag = "nyStaticDogTag"),
            (e.NyToys = "nyToys"),
            (e.NyLootboxFragment = "nyLootboxFragment"));
        })(zo || (zo = {})),
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
          })(Uo || (Uo = {})),
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
          })(Go || (Go = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(qo || (qo = {})),
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
          })(Vo || (Vo = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(jo || (jo = {})),
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
          })(Xo || (Xo = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(Qo || (Qo = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(Yo || (Yo = {})));
        const Ko = "LootboxTransition_base_9c",
          Zo = "LootboxTransition_lootbox_62",
          Jo = "LootboxTransition_smoke_43",
          el = (0, u.memo)(({ delay: e, isEnabled: t = !0, children: a }) =>
            t
              ? s().createElement(
                  "div",
                  { className: Ko },
                  s().createElement("div", {
                    className: Jo,
                    style: { animationDelay: `${e + 500}ms` },
                  }),
                  s().createElement(
                    "div",
                    { className: Zo, style: { animationDelay: `${e}ms, ${e + 500}ms` } },
                    a,
                  ),
                )
              : a,
          );
        function tl() {
          return (
            (tl =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            tl.apply(this, arguments)
          );
        }
        const al = ({ children: e, tooltipArgs: t, className: a }) => {
            if (!t) return e;
            const n = s().createElement("div", { className: a }, e);
            if (t.header || t.body) return s().createElement(Ve, t, n);
            const r = t.contentId,
              u = t.args,
              i = null == u ? void 0 : u.contentId;
            return r || i
              ? s().createElement(ze, tl({}, t, { contentId: r || i }), n)
              : s().createElement(Ha, t, n);
          },
          nl = [
            zo.Items,
            zo.Equipment,
            zo.Xp,
            zo.XpFactor,
            zo.Blueprints,
            zo.BlueprintsAny,
            zo.Goodies,
            zo.Berths,
            zo.Slots,
            zo.Tokens,
            zo.CrewSkins,
            zo.CrewBooks,
            zo.Customizations,
            zo.CreditsFactor,
            zo.TankmenXp,
            zo.TankmenXpFactor,
            zo.FreeXpFactor,
            zo.BattleToken,
            zo.Entitlements,
            zo.PremiumUniversal,
            zo.NaturalCover,
            zo.BpCoin,
            zo.BattlePassSelectToken,
            zo.BattlaPassFinalAchievement,
            zo.BattleBadge,
            zo.BonusX5,
            zo.CrewBonusX3,
            zo.NewYearFillers,
            zo.NewYearInvoice,
            zo.EpicSelectToken,
            zo.Comp7TokenWeeklyReward,
            zo.Comp7TokenCouponReward,
            zo.BattleBoosterGift,
            zo.NewYearFillers,
            zo.NewYearInvoice,
            zo.LootBoxToken,
            zo.CosmicLootboxCommon,
            zo.CosmicLootboxSilver,
            zo.SelectableBonus,
            zo.PostStamp,
            zo.PremiumPlusUniversal,
            zo.GoldenTicket,
            zo.RewardsSlots,
            zo.NyPetGoodies,
            zo.HiddenVehicle,
            zo.NyLootboxFragment,
          ],
          rl = [zo.Gold, zo.Credits, zo.Crystal, zo.FreeXp, zo.NewYearToyFragments],
          ul = [zo.BattlePassPoints],
          sl = [zo.PremiumPlus, zo.Premium];
        let il;
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
        })(il || (il = {}));
        const ol = ["engravings", "backgrounds"],
          ll = ["engraving", "background"],
          cl = (e, t = Go.Small, a) => {
            const n = e.name,
              r = e.type,
              u = e.value,
              s = e.icon,
              i = e.item,
              o = e.dogTagType,
              l = ((e) => {
                switch (e) {
                  case Go.S600x450:
                    return "c_600x450";
                  case Go.S400x300:
                    return "c_400x300";
                  case Go.S296x222:
                    return "c_296x222";
                  case Go.S232x174:
                    return "c_232x174";
                  case Go.Big:
                    return "c_80x80";
                  case Go.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(t);
            switch (n) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${r}_${u}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${n}_plus_${u}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${n}_${u}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${i}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${t}.${s}`;
              case "tokens":
              case "battleToken":
                return ((e, t) => {
                  switch (t) {
                    case Go.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case Go.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${t}.${e.icon}`;
                  }
                })(e, t);
              case "entitlements":
                return "big" === t
                  ? e.iconBig.replace("..", "img://gui")
                  : e.iconSmall.replace("..", "img://gui");
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${t}.${s}`;
              case "dogTagComponents":
                return ((e, t, a) => {
                  const n = ol[e];
                  if (n) {
                    const r = R.images.gui.maps.icons.dogtags.$dyn(t).$dyn(n),
                      u = r.$dyn(a);
                    return u ? `${u}` : `${r.$dyn(ll[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, t, s);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${l}.${s}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case Go.S600x450:
                      return "c_600x450";
                    case Go.S400x300:
                      return "c_400x300";
                    case Go.S296x222:
                      return "c_296x222";
                    case Go.S232x174:
                      return "c_232x174";
                    case Go.S180x135:
                      return "big";
                    case Go.Big:
                    case Go.S80x80:
                      return "c_80x80";
                    case Go.Small:
                    case Go.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(t)}.${s}`;
              case "xp":
              case "xpFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.exp`;
              case "creditsFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.credits`;
              case "tankmenXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.tankmenXP`;
              case "dailyXPFactor":
              case "freeXPFactor":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.freeXP`;
              case "tmanToken":
              case "battlePassSelectToken":
              case "selectableBonus":
              case "groups":
              case "lootBoxToken":
              case "customizations":
              case "crewSkins":
              case "goodies":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${s}`;
              case "nyPetGoodies":
                return `R.images.new_year.gui.maps.icons.newYear.common.categoriesIcons.${t}.${s}`;
              case "nyLootboxFragment":
                return `R.images.new_year.gui.maps.icons.newYear.common.rewards.fragments.${t}.lootbox_fragment`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${l}.${s}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case Go.Mini:
                      return il.s32;
                    case Go.Small:
                    case Go.S48x48:
                      return il.s48;
                    case Go.S80x80:
                    case Go.Big:
                      return il.s80;
                    case Go.S128x100:
                      return il.s116;
                    case Go.S180x135:
                    case Go.S232x174:
                    case Go.S296x222:
                      return il.s296;
                    case Go.S400x300:
                      return il.s400;
                    case Go.S600x450:
                      return il.s600;
                  }
                })(t)}`;
              case zo.StyleProgress:
              case zo.LbStyleProgress:
                return ml(s, t, Yo.ProgressionStyle);
              case "newYearAlbumsAccess":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${t}.albumsAccess`;
              case "nyFillers":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${t}.fillers`;
              case "nyToyFragments":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${t}.shards`;
              case "newYearSlot":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${t}.slot`;
              case "hidden_vehicle":
                return "R.images.new_year.gui.maps.icons.newYear.common.rewards.vehicles.hidden_vehicle";
              case "nyStaticDogTag":
                return `R.images.new_year.gui.maps.icons.newYear.common.rewards.dogtags.${t}.dogtag_${a}`;
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${n}`;
            }
          },
          ml = (e, t, a) => {
            const n = R.images.gui.maps.icons.quests.bonuses.$dyn(t),
              r = n.$dyn(e);
            return String(null != r ? r : n.$dyn(a));
          },
          dl = {
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
          _l = ({
            name: e,
            image: t,
            isPeriodic: a = !1,
            size: n = Go.Big,
            special: r,
            value: u,
            valueType: i,
            style: o,
            className: l,
            classNames: c,
            tooltipArgs: m,
            periodicIconTooltipArgs: d,
          }) => {
            const _ = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Vo.BATTLE_BOOSTER:
                  case Vo.BATTLE_BOOSTER_REPLACE:
                    return jo.BATTLE_BOOSTER;
                }
              })(r),
              E = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case Vo.BATTLE_BOOSTER:
                    return Xo.BATTLE_BOOSTER;
                  case Vo.BATTLE_BOOSTER_REPLACE:
                    return Xo.BATTLE_BOOSTER_REPLACE;
                  case Vo.BUILT_IN_EQUIPMENT:
                    return Xo.BUILT_IN_EQUIPMENT;
                  case Vo.EQUIPMENT_PLUS:
                    return Xo.EQUIPMENT_PLUS;
                  case Vo.EQUIPMENT_TROPHY_BASIC:
                    return Xo.EQUIPMENT_TROPHY_BASIC;
                  case Vo.EQUIPMENT_TROPHY_UPGRADED:
                    return Xo.EQUIPMENT_TROPHY_UPGRADED;
                  case Vo.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return Xo.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case Vo.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return Xo.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case Vo.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return Xo.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case Vo.PROGRESSION_STYLE_UPGRADED_1:
                    return Xo.PROGRESSION_STYLE_UPGRADED_1;
                  case Vo.PROGRESSION_STYLE_UPGRADED_2:
                    return Xo.PROGRESSION_STYLE_UPGRADED_2;
                  case Vo.PROGRESSION_STYLE_UPGRADED_3:
                    return Xo.PROGRESSION_STYLE_UPGRADED_3;
                  case Vo.PROGRESSION_STYLE_UPGRADED_4:
                    return Xo.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(r),
              g = ((e, t) => {
                if (void 0 === e) return null;
                switch (t) {
                  case qo.MULTI: {
                    const t = Number(e);
                    return isFinite(t) && t > 1 ? `x${Math.floor(t)}` : null;
                  }
                  case qo.CURRENCY:
                  case qo.NUMBER:
                    return s().createElement(Ja, { format: "integral", value: Number(e) });
                  case qo.PREMIUM_PLUS: {
                    const t = Number(e);
                    return isNaN(t) ? e : null;
                  }
                  default:
                    return e;
                }
              })(u, i);
            return s().createElement(
              "div",
              { className: F()(dl.base, dl[`base__${n}`], l), style: o },
              s().createElement(
                al,
                { tooltipArgs: m, className: dl.tooltipWrapper },
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement(
                    "div",
                    { className: F()(dl.image, null == c ? void 0 : c.image) },
                    _ &&
                      s().createElement("div", {
                        className: F()(dl.highlight, null == c ? void 0 : c.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${_}_highlight)`,
                        },
                      }),
                    t &&
                      s().createElement("div", {
                        className: F()(dl.icon, null == c ? void 0 : c.rewardIcon),
                        style: { backgroundImage: `url(${t})` },
                      }),
                    E &&
                      s().createElement("div", {
                        className: F()(dl.overlay, null == c ? void 0 : c.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${E}_overlay)`,
                        },
                      }),
                  ),
                  g &&
                    s().createElement(
                      "div",
                      {
                        className: F()(
                          dl.info,
                          dl[`info__${e}`],
                          i === qo.MULTI && dl.info__multi,
                          null == c ? void 0 : c.info,
                        ),
                      },
                      g,
                    ),
                ),
              ),
              a &&
                s().createElement(
                  al,
                  { tooltipArgs: d },
                  s().createElement("div", {
                    className: F()(dl.timer, null == c ? void 0 : c.periodicIcon),
                  }),
                ),
            );
          },
          El = "Rewards_base_26",
          gl = "Rewards_base__vertical_9f",
          pl = "Rewards_reward_7b",
          fl = "Rewards_reward__vertical_c6";
        function Al() {
          return (
            (Al =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Al.apply(this, arguments)
          );
        }
        const hl = [zo.BattleToken],
          vl = s().memo(
            ({
              data: e,
              size: t = Go.Big,
              isVertical: a = !1,
              count: n,
              classMix: r,
              rewardItemClassMix: i,
              boxRewardTooltip: o,
              boxRewardValue: l,
              isLootboxAnimationEnabled: c = !1,
              delay: m = 0,
            }) => {
              const d = (0, u.useMemo)(
                  () =>
                    n && n < e.length ? `R.images.gui.maps.icons.quests.bonuses.${t}.default` : "",
                  [n, e.length, t],
                ),
                _ =
                  l ||
                  ia(R.strings.tooltips.quests.awards.additional.bottom(), {
                    count: e.length - (n || 0),
                  }),
                E = F()(El, a && gl, r),
                g = F()(pl, a && fl, i);
              return s().createElement(
                "div",
                { className: E },
                d
                  ? s().createElement(
                      s().Fragment,
                      null,
                      e
                        .slice(0, n)
                        .map((e, a) =>
                          s().createElement(
                            "div",
                            { key: a, className: g },
                            s().createElement(_l, Al({ size: t }, e)),
                          ),
                        ),
                      s().createElement(
                        "div",
                        { className: g },
                        s().createElement(_l, {
                          name: "more",
                          image: d,
                          size: t,
                          value: _,
                          tooltipArgs: o,
                        }),
                      ),
                    )
                  : e.map((e, a) => {
                      const n = e.name,
                        r = c && hl.includes(n);
                      return s().createElement(
                        u.Fragment,
                        { key: a },
                        s().createElement(
                          el,
                          { delay: m, isEnabled: r },
                          s().createElement(
                            "div",
                            { key: a, className: g },
                            s().createElement(_l, Al({ size: t }, e)),
                          ),
                        ),
                      );
                    }),
              );
            },
          ),
          bl = ["overlayType"];
        const Fl = (e, t) => {
            if ("dogTagComponents" === e.name) {
              if (t === Go.Big) return Go.S80x80;
              if (t === Go.Small) return Go.S48x48;
            }
            return t;
          },
          Dl = (e) => ("vehicles_rent" === e.name ? e.label : e.value),
          Cl = ({ reward: e, rank: t, index: a }) => {
            const n = e.tooltipId,
              r = e.tooltipContentId;
            return ((e, t, a) => {
              const n = t && { contentId: t };
              return Object.assign(
                {
                  args: e,
                  isEnabled: Boolean((e && e.tooltipId) || t),
                  ignoreMouseClick: !0,
                  ignoreShowDelay: !t,
                },
                n,
                a,
              );
            })(
              Object.assign(
                { tooltipId: n },
                void 0 !== t && { rank: t },
                void 0 !== a && { index: a },
              ),
              Number(r),
              { ignoreShowDelay: !0 },
            );
          },
          Bl = ({ reward: e, size: t, rank: a, index: n }) => {
            const r = e.overlayType,
              u = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, bl),
              s = Fl(e, t);
            return Object.assign({}, u, {
              size: s,
              image: cl(e, s),
              value: Dl(e),
              valueType:
                ((i = e.name),
                nl.includes(i)
                  ? qo.MULTI
                  : rl.includes(i)
                    ? qo.CURRENCY
                    : ul.includes(i)
                      ? qo.NUMBER
                      : sl.includes(i)
                        ? qo.PREMIUM_PLUS
                        : qo.STRING),
              special: r,
              tooltipArgs: Cl({ reward: e, rank: a, index: n }),
              periodicIconTooltipArgs: {
                header: R.strings.tooltips.periodicReward.header(),
                body: R.strings.tooltips.periodicReward.comp7.body(),
              },
            });
            var i;
          },
          wl = ({ rewards: e, size: t, rank: a, index: n }) =>
            be(e, (e) => Bl({ reward: e, size: t, rank: a, index: n })),
          Sl = (e, t) => (e > t ? t - 1 : void 0),
          yl = "AdditionalRewards_reward_16",
          Rl = "AdditionalRewards_vehiclesRentBase_d4",
          xl = "AdditionalRewards_vehiclesRentLabel_3e",
          Pl = Go.Small,
          kl = (0, W.Pi)(({ rank: e, itemIndex: t, visibleRewardsCount: a, className: n }) => {
            const r = $o().model,
              u = r.computes.additionalRewards(t),
              i = r.computes.additionalRewardsCount(t),
              o = be(u, (t) => {
                const a = "vehicles_rent" === t.name;
                return Object.assign({}, Bl({ reward: t, size: Pl, rank: e }), {
                  className: F()(a && Rl),
                  classNames: { info: F()(a && xl) },
                });
              });
            return s().createElement(vl, {
              data: o,
              size: Pl,
              count: Sl(i, a),
              rewardItemClassMix: yl,
              boxRewardTooltip: {
                contentId: R.views.lobby.tooltips.AdditionalRewardsTooltip("resId"),
                args: { fromIndex: a, rank: e },
              },
              classMix: n,
            });
          });
        let Tl;
        !(function (e) {
          ((e[(e.NotStarted = 0)] = "NotStarted"),
            (e[(e.Active = 1)] = "Active"),
            (e[(e.OffSeason = 3)] = "OffSeason"),
            (e[(e.Finished = 4)] = "Finished"));
        })(Tl || (Tl = {}));
        const Ll = {
            base: "Heading_base_99",
            tooltipArea: "Heading_tooltipArea_c9",
            rankEmblem__future: "Heading_rankEmblem__future_6d",
            lock: "Heading_lock_a8",
            description: "Heading_description_6f",
            rankName: "Heading_rankName_05",
            rankStatus: "Heading_rankStatus_63",
          },
          Nl = (0, W.Pi)(
            ({
              rank: e,
              from: t,
              to: a,
              elitePercent: n,
              divisions: r,
              rankEmblemSize: u,
              rankState: i,
            }) => {
              const o = $o().model,
                l = ce().model,
                c = o.qualification.isActive.get(),
                m = us(i, e, c),
                d = i === ha.Current && !c;
              return s().createElement(
                "div",
                { className: Ll.base },
                s().createElement(
                  ze,
                  {
                    contentId: R.views.lobby.comp7.tooltips.GeneralRankTooltip("resId"),
                    ignoreShowDelay: !0,
                    args: { rank: e, divisions: r, from: t, to: a, elitePercent: n },
                  },
                  s().createElement(
                    "div",
                    { className: Ll.tooltipArea },
                    s().createElement(ns, {
                      rank: e,
                      size: u,
                      type: ts.Static,
                      state: m,
                      classNames: { rankEmblem: Ll[`rankEmblem__${i}`] },
                    }),
                    i === ha.Future && s().createElement("div", { className: Ll.lock }),
                  ),
                ),
                s().createElement(
                  "div",
                  { className: Ll.description },
                  s().createElement("div", { className: Ll.rankName }, qu(e)),
                  d &&
                    s().createElement(
                      "div",
                      { className: Ll.rankStatus },
                      ((e) => {
                        switch (e) {
                          case Tl.OffSeason:
                          case Tl.Finished:
                            return R.strings.comp7.rank.achieved();
                          case Tl.Active:
                            return R.strings.comp7.rank.current();
                          default:
                            return "";
                        }
                      })(l.year.state.get()),
                    ),
                ),
              );
            },
          ),
          Il = {
            base: "Preview_base_1f",
            base__hovered: "Preview_base__hovered_ee",
            icon: "Preview_icon_f3",
            icon__small: "Preview_icon__small_a1",
            icon__normal: "Preview_icon__normal_5c",
            base__mouseDown: "Preview_base__mouseDown_d0",
            label: "Preview_label_2e",
            base__visibleLabel: "Preview_base__visibleLabel_92",
          },
          Ml = [
            "label",
            "isVisibleLabel",
            "autofocus",
            "soundHover",
            "soundClick",
            "size",
            "classNames",
            "onClick",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseDown",
            "onMouseUp",
            "onFocus",
            "onBlur",
          ];
        function Ol() {
          return (
            (Ol =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ol.apply(this, arguments)
          );
        }
        let Hl;
        !(function (e) {
          ((e.SMALL = "small"), (e.NORMAL = "normal"));
        })(Hl || (Hl = {}));
        const Wl = (0, u.memo)((e) => {
            let t = e.label,
              a = e.isVisibleLabel,
              n = void 0 !== a && a,
              r = e.autofocus,
              i = void 0 !== r && r,
              o = e.soundHover,
              l = void 0 === o ? "highlight" : o,
              c = e.soundClick,
              m = void 0 === c ? "play" : c,
              d = e.size,
              _ = void 0 === d ? Hl.NORMAL : d,
              E = e.classNames,
              g = e.onClick,
              p = e.onMouseEnter,
              f = e.onMouseLeave,
              A = e.onMouseDown,
              h = e.onMouseUp,
              v = e.onFocus,
              b = e.onBlur,
              D = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Ml);
            const C = (0, u.useState)(!1),
              B = C[0],
              w = C[1],
              S = (0, u.useState)(!1),
              y = S[0],
              R = S[1],
              x = (0, u.useState)(i),
              P = x[0],
              k = x[1],
              T = (0, u.useRef)(null),
              L = (0, u.useCallback)(() => {
                T.current && (T.current.focus(), k(!0));
              }, []),
              N = (0, u.useCallback)(
                (e) => {
                  P && null !== T.current && !T.current.contains(e.target) && k(!1);
                },
                [P],
              );
            ((0, u.useEffect)(
              () => (
                document.addEventListener("mousedown", N),
                () => {
                  document.removeEventListener("mousedown", N);
                }
              ),
              [N],
            ),
              (0, u.useEffect)(() => {
                k(i);
              }, [i]));
            const I = (0, u.useCallback)(
                (e) => {
                  g && g(e);
                },
                [g],
              ),
              M = (0, u.useCallback)(
                (e) => {
                  (w(!0), A && A(e), m && $(m), i && L());
                },
                [i, A, L, m],
              ),
              O = (0, u.useCallback)(
                (e) => {
                  (w(!1), h && h(e));
                },
                [h],
              ),
              H = (0, u.useCallback)(
                (e) => {
                  (p && p(e), l && $(l), R(!0));
                },
                [p, l],
              ),
              W = (0, u.useCallback)(
                (e) => {
                  (w(!1), R(!1), f && f(e));
                },
                [f],
              ),
              z = (0, u.useCallback)(
                (e) => {
                  (k(!0), v && v(e));
                },
                [v],
              ),
              U = (0, u.useCallback)(
                (e) => {
                  (k(!1), b && b(e));
                },
                [b],
              ),
              G = F()(
                Il.base,
                n && Il.base__visibleLabel,
                B && Il.base__mouseDown,
                y && Il.base__hovered,
                P && Il.base__focused,
                null == E ? void 0 : E.base,
              ),
              q = F()(Il.icon, Il[`icon__${_}`], null == E ? void 0 : E.icon),
              V = F()(Il.label, null == E ? void 0 : E.label);
            return s().createElement(
              "div",
              Ol(
                {
                  ref: T,
                  className: G,
                  onClick: I,
                  onMouseEnter: H,
                  onMouseLeave: W,
                  onMouseDown: M,
                  onMouseUp: O,
                  onFocus: z,
                  onBlur: U,
                },
                D,
              ),
              s().createElement("div", { className: q }),
              s().createElement("div", { className: V }, t),
            );
          }),
          $l = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          zl = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const Ul = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          Gl = (e) =>
            Ul
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let a = zl.length - 1; a >= 0; a--)
                    for (; e >= zl[a];) ((t += $l[a]), (e -= zl[a]));
                  return t;
                })(e),
          ql = "MainReward_base_32",
          Vl = "MainReward_imageContainer_37",
          jl = "MainReward_highlightContainer_cf",
          Xl = "MainReward_highlight_06",
          Ql = "MainReward_preview_7a",
          Yl = "MainReward_info_58",
          Kl = "MainReward_title_6d",
          Zl = "MainReward_subTitle_e2",
          Jl = (0, W.Pi)(
            ({ index: e, rank: t, size: a, hasHighlight: n, onPreviewClick: r, className: u }) => {
              const i = $o().model.computes.mainReward(e);
              return s().createElement(
                "div",
                { className: F()(ql, u) },
                s().createElement(
                  "div",
                  { className: Vl },
                  n &&
                    s().createElement(
                      "div",
                      { className: jl },
                      s().createElement("div", { className: Xl }),
                    ),
                  s().createElement(_l, Bl({ reward: i, size: a, rank: t })),
                  ((e) => "styleProgress" === e.name)(i) &&
                    s().createElement(
                      "div",
                      { className: Ql },
                      s().createElement(Wl, {
                        label: R.strings.comp7.rewards.preview(),
                        onClick: r,
                      }),
                    ),
                ),
                s().createElement(
                  "div",
                  { className: Yl },
                  s().createElement("div", { className: Kl }, i.label),
                  s().createElement(kn, {
                    text: String(R.strings.comp7.rewards.subtitle.$dyn(i.name)),
                    binding: { vehicleLevel: Gl(10) },
                    classMix: Zl,
                  }),
                ),
              );
            },
          ),
          ec = "RankRewardsItem_base_a7",
          tc = "RankRewardsItem_mainRewardContainer_e0",
          ac = "RankRewardsItem_rewardsContainer_69",
          nc = "RankRewardsItem_rewardsContainer__qualification_b0",
          rc = "RankRewardsItem_statusContainer_bf",
          uc = "RankRewardsItem_statusContainer__hidden_c8",
          sc = "RankRewardsItem_icon_7d",
          ic = (0, W.Pi)(
            ({
              itemIndex: e,
              itemWidth: t,
              rankState: a,
              mainRewardSize: n,
              hasHighlight: r,
              visibleRewardsCount: u,
              rankEmblemSize: i,
              isQualification: o,
              onPreviewClick: l,
            }) => {
              const c = $o().model,
                m = c.computes.rankRewardsItem(e),
                d = m.rank,
                _ = m.from,
                E = m.to,
                g = m.hasRewardsReceived,
                p = c.computes.divisionsString(e),
                f = c.computes.elitePercent(e);
              return s().createElement(
                "div",
                { className: ec, style: { "--itemWidth": `${t}rem` } },
                s().createElement(Nl, {
                  rank: d,
                  from: _,
                  to: E,
                  divisions: p,
                  elitePercent: f,
                  rankEmblemSize: i,
                  rankState: a,
                }),
                s().createElement(Jl, {
                  index: e,
                  rank: d,
                  size: n,
                  hasHighlight: r,
                  onPreviewClick: l,
                  className: tc,
                }),
                s().createElement(
                  "div",
                  { className: F()(ac, o && nc) },
                  s().createElement(kl, { itemIndex: e, visibleRewardsCount: u, rank: d }),
                ),
                s().createElement(
                  "div",
                  { className: F()(rc, !g && uc) },
                  s().createElement("div", { className: sc }),
                  R.strings.comp7.rewards.status.achieved(),
                ),
              );
            },
          ),
          oc = (e) => (e >= B.Large ? Ku.x110 : e >= B.Medium ? Ku.x64 : Ku.x48),
          lc = (e) =>
            e >= B.ExtraLarge
              ? Go.S600x450
              : e >= B.Large
                ? Go.S400x300
                : e >= B.Medium
                  ? Go.S296x222
                  : Go.S232x174,
          cc = (e) => (e >= w.Medium ? 5 : 4),
          mc = "RankRewardsPage_base_fd",
          dc = "RankRewardsPage_content_3f",
          _c = "RankRewardsPage_scrollContainer_f2",
          Ec = "RankRewardsPage_areaContainer_9e",
          gc = "RankRewardsPage_areaWrapper_fb",
          pc = "RankRewardsPage_bar_59",
          fc = "RankRewardsPage_qualificationFooter_71",
          Ac = "RankRewardsPage_shopButtonContainer_90",
          hc = "RankRewardsPage_shopButton_4e",
          vc = "RankRewardsPage_comp7ShopButtonBackground_cc",
          bc = "RankRewardsPage_shopButtonIcon_51",
          Fc = { duration: 700, easing: (e) => Math.pow(e, 4) },
          Dc = R.strings.comp7.rewards,
          Cc = (0, W.Pi)(() => {
            const e = y(),
              t = e.mediaSize,
              a = e.mediaWidth,
              n = $o(),
              r = n.model,
              i = n.controls,
              o = r.root.get(),
              l = o.currentItemIndex,
              c = o.initialItemIndex,
              m = r.qualification.isActive.get(),
              d = r.computes.rankRewardsItemsLength(),
              _ = r.computes.scrollingSettings(),
              E = _.nextNotAchievedItemIndex,
              g = _.hasForceScroll,
              p = (0, u.useState)(g ? "idle" : "initial"),
              f = p[0],
              A = p[1],
              h = (0, u.useState)(g ? c : E),
              v = h[0],
              b = h[1],
              F = ((e) =>
                e >= B.ExtraLarge
                  ? 600
                  : e >= B.Large
                    ? 460
                    : e >= B.Medium
                      ? 400
                      : e >= B.Small
                        ? 340
                        : 300)(t),
              D = d * F,
              C = Wu(F),
              w = C.scrollPosition,
              S = C.clampPosition,
              x = C.contentRef,
              P = (function () {
                const e = (0, u.useRef)(!1);
                return (
                  (0, u.useEffect)(
                    () => () => {
                      e.current = !0;
                    },
                    [],
                  ),
                  e
                );
              })();
            ((0, u.useLayoutEffect)(() => {
              "idle" === f
                ? w.start({ scrollPosition: viewEnv.remToPx(c * F), immediate: !0 })
                : "initial" === f && w.start({ scrollPosition: viewEnv.remToPx(D), immediate: !0 });
            }, []),
              (0, u.useEffect)(
                () =>
                  xe(() => {
                    const e = x.current;
                    if (e && "initial" === f) {
                      const t = S(e, viewEnv.remToPx(E * F - F)),
                        a = S(e, viewEnv.remToPx(D));
                      if (t === a) return void A("idle");
                      w.start({
                        scrollPosition: t,
                        from: { scrollPosition: a },
                        config: Fc,
                        onStart: () => {
                          A("scrolling");
                        },
                        onRest: () => {
                          P.current || A("idle");
                        },
                      });
                    }
                  }),
                [S, x, P, F, E, f, D, w],
              ));
            const k = (e) => "idle" === f && e === E && !m,
              T = (0, Pe.useSpring)(_e),
              L = { lineHeight: 1.5 },
              N = ou(F) - F;
            return s().createElement(
              "div",
              { className: mc },
              s().createElement(ya, { className: K }, R.strings.comp7.page.heading.rankRewards()),
              s().createElement(Qa, null),
              s().createElement(
                Pe.animated.div,
                { className: dc, style: T },
                s().createElement(
                  Hu,
                  {
                    api: C,
                    stuckIndex: v,
                    itemWidth: F,
                    itemsOffset: N,
                    onStick: b,
                    className: _c,
                    areaClassNames: { base: Ec, wrapper: gc },
                    barClassNames: { base: pc },
                  },
                  su(d, (e) =>
                    s().createElement(ic, {
                      key: e,
                      itemIndex: e,
                      visibleRewardsCount: cc(a),
                      rankState: Fa(e, l, m),
                      rankEmblemSize: oc(t),
                      mainRewardSize: lc(t),
                      itemWidth: F,
                      hasHighlight: k(e),
                      isQualification: m,
                      onPreviewClick: () => i.goToPreview(e, v),
                    }),
                  ),
                ),
              ),
              !m &&
                s().createElement(
                  "div",
                  { className: Ac },
                  s().createElement(
                    bt,
                    { type: At.ghost, size: ht.medium, mixClass: hc, onClick: i.openComp7Shop },
                    s().createElement("div", { className: vc }),
                    s().createElement("div", { className: bc }),
                    s().createElement(Sn, {
                      text: Dc.shopButton(),
                      color: "WHITE",
                      variant: "paragraph-P14",
                      variant_md: "paragraph-P18",
                      style: { fontWeight: 700 },
                    }),
                  ),
                ),
              m &&
                s().createElement(
                  "div",
                  { className: fc },
                  s().createElement(Sn, {
                    text: Dc.qualification.condition.first(),
                    color: "WHITE_REAL",
                    variant: "paragraph-P14",
                    variant_md: "paragraph-P16",
                    style: L,
                  }),
                  s().createElement(Sn, {
                    text: Dc.qualification.condition.second(),
                    color: "WHITE_REAL",
                    variant: "paragraph-P14",
                    variant_md: "paragraph-P16",
                    style: L,
                  }),
                ),
            );
          }),
          Bc = { context: "model.rankRewardsModel" };
        let wc;
        !(function (e) {
          ((e.LockedByNoXVehicles = "lockedByNoXVehicles"),
            (e.LockedByInactiveSeason = "lockedByInactiveSeason"),
            (e.LockedByPreviousQuest = "lockedByPreviousQuest"),
            (e.Active = "active"),
            (e.Completed = "completed"));
        })(wc || (wc = {}));
        const Sc = [wc.LockedByNoXVehicles, wc.LockedByInactiveSeason, wc.LockedByPreviousQuest];
        let yc;
        !(function (e) {
          ((e[(e.Scrolling = 0)] = "Scrolling"),
            (e[(e.ProgressChange = 1)] = "ProgressChange"),
            (e[(e.HighlightCard = 2)] = "HighlightCard"),
            (e[(e.ChangeCompleted = 3)] = "ChangeCompleted"),
            (e[(e.ProgressFinished = 4)] = "ProgressFinished"),
            (e[(e.ProgressAlreadyFinished = 5)] = "ProgressAlreadyFinished"));
        })(yc || (yc = {}));
        const Rc = 2140,
          xc = 1500,
          Pc = 1264,
          kc = 1104,
          Tc = 804,
          Lc = 187,
          Nc = 158,
          Ic = ie()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  {
                    root: e.object(),
                    questCards: e.array("questCards"),
                    progressPoints: e.array("progressPoints"),
                  },
                  e.primitives(["currentTokenValue", "previousTokenValue"]),
                  { progressAnimationState: ne.LO.box(yc.HighlightCard) },
                ),
                a = (0, Ee.Om)(
                  (e) => {
                    const a = Ae(t.questCards.get(), e);
                    if (!a) throw new Error(`Unexpected card index: ${e}`);
                    return Object.assign({}, a);
                  },
                  { equals: ae },
                ),
                n = (0, Ee.Om)(
                  (e, t) => {
                    const n = a(e).rewards;
                    return wl({ rewards: n, size: t });
                  },
                  { equals: ae },
                ),
                r = (0, Ee.Om)(() =>
                  (function (e, t) {
                    if (Array.isArray(e)) return e.every(t);
                    for (let a = 0; a < e.length; a++) if (!t(he(e, a), a, e)) return !1;
                    return !0;
                  })(t.questCards.get(), (e) => e.state === wc.Completed),
                ),
                u = (0, Ee.Om)((e) => Sc.includes(a(e).state)),
                s = (0, Ee.Om)(() => t.questCards.get().length),
                i = (0, Ee.Om)(() => 5 >= s(), { equals: ae }),
                o = (0, Ee.Om)(() => (r() ? wc.Completed : wc.Active), { equals: ae }),
                l = (0, Ee.Om)(() => t.currentTokenValue.get(), { equals: ae }),
                c = (0, Ee.Om)(() => t.previousTokenValue.get(), { equals: ae }),
                m = (0, Ee.Om)(
                  (e) => ({
                    wasProgressionVisited: c() === l(),
                    isRecentlyCompletedLevel: c() <= e && e <= l(),
                    isPrevLevel: e <= c(),
                  }),
                  { equals: ae },
                ),
                d = (0, Ee.Om)(
                  () => {
                    const e = t.currentTokenValue.get(),
                      a = t.progressPoints.get();
                    return be(a, ({ rewards: t }, n) => ({
                      level: n + 1,
                      isCompleted: n < e,
                      isActive: n === e,
                      isLast: n === a.length - 1,
                      rewards: t,
                    }));
                  },
                  { equals: ae },
                ),
                _ = (0, Ee.Om)(
                  () => {
                    const e = 1 * t.progressPoints.get().length;
                    return t.currentTokenValue.get() >= e;
                  },
                  { equals: ae },
                ),
                E = (0, Ee.Om)(
                  () => _() && t.currentTokenValue.get() === t.previousTokenValue.get(),
                  { equals: ae },
                ),
                g = (0, Ee.Om)(
                  () => {
                    var e;
                    const a = t.progressPoints.get(),
                      n = Ae(a, a.length - 1),
                      r = null != (e = null == n ? void 0 : n.count) ? e : 0;
                    return t.currentTokenValue.get() >= r;
                  },
                  { equals: ae },
                ),
                p = (0, Ee.Om)(
                  () => {
                    var e;
                    return null != (e = Ce(t.questCards.get(), (e) => e.state === wc.Active))
                      ? e
                      : 0;
                  },
                  { equals: ae },
                ),
                f = (0, Ee.Om)(
                  (e, t, a, n) => {
                    if (t && t.length) {
                      const r = t.length * a + (t.length - 1) * n,
                        u = (e, t) => (e >= t ? t : e);
                      switch (!0) {
                        case e >= B.ExtraLarge:
                          return u(r, Rc);
                        case e >= B.Large:
                          return u(r, xc);
                        case e >= B.Medium:
                          return u(r, Pc);
                        case e >= B.Small:
                          return u(r, kc);
                        default:
                          return u(r, Tc);
                      }
                    }
                    return 0;
                  },
                  { equals: ae },
                );
              return Object.assign({}, t, {
                computes: {
                  questCardsLength: s,
                  questCard: a,
                  questCards: t.questCards,
                  questRewards: n,
                  isQuestLocked: u,
                  areDefaultNumberQuests: i,
                  battleTasksStatus: o,
                  isAllQuestsCompleted: r,
                  levels: d,
                  currentLevel: l,
                  levelStatus: m,
                  isProgressionCompleted: _,
                  wasProgressionCompletedBeforeStart: E,
                  initialItemScrollIndex: p,
                  getScrollContainerMaxWidth: f,
                  isDoneProgression: g,
                },
              });
            },
            ({ externalModel: e, model: t }) => {
              const a = (function (e) {
                const t = {};
                for (const a in e)
                  if (Object.prototype.hasOwnProperty.call(e, a)) {
                    const n = e[a];
                    t[a] = (0, ne.aD)(n);
                  }
                return t;
              })({
                finishScrolling: () => t.progressAnimationState.set(yc.ProgressChange),
                finishProgressionChange: () => t.progressAnimationState.set(yc.HighlightCard),
                finishHighlightCard: () => t.progressAnimationState.set(yc.ChangeCompleted),
                completeProgression: () => t.progressAnimationState.set(yc.ProgressFinished),
              });
              return Object.assign({}, a, {
                animationStart: e.createCallbackNoArgs("onAnimationStart"),
                animationEnd: e.createCallbackNoArgs("onAnimationEnd"),
              });
            },
          ),
          Mc = Ic[0],
          Oc = Ic[1],
          Hc = {
            base: "Prompt_base_74",
            defaultText: "Prompt_defaultText_05",
            defaultText__done: "Prompt_defaultText__done_b0",
          },
          Wc = R.strings.comp7.weeklyQuests.tokenProgress.description,
          $c = (0, W.Pi)(({ className: e }) => {
            const t = Oc().model.computes.isDoneProgression();
            return s().createElement(
              "div",
              { className: F()(Hc.base, t && Hc.base__done, e) },
              t
                ? s().createElement(Sn, {
                    text: Wc.done(),
                    variant: "paragraph-P14",
                    className: Hc.defaultText__done,
                  })
                : s().createElement(Sn, {
                    text: Wc.normal(),
                    variant: "paragraph-P14",
                    className: Hc.defaultText,
                  }),
            );
          }),
          zc = Au({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? pu.Next : pu.Prev),
          }),
          Uc = "VerticalBar_base_f3",
          Gc = "VerticalBar_base__nonActive_42",
          qc = "VerticalBar_topButton_d7",
          Vc = "VerticalBar_bottomButton_06",
          jc = "VerticalBar_track_df",
          Xc = "VerticalBar_thumb_32",
          Qc = "VerticalBar_rail_43",
          Yc = "disable",
          Kc = () => {},
          Zc = { pending: !1, offset: 0 },
          Jc = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          em = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          tm = (e, t) => Math.max(20, e.offsetHeight * t),
          am = (0, u.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = Jc, onDrag: n = Kc }) => {
              const r = (0, u.useRef)(null),
                i = (0, u.useRef)(null),
                o = (0, u.useRef)(null),
                l = (0, u.useRef)(null),
                c = (0, u.useRef)(null),
                m = e.stepTimeout || 100,
                d = (0, u.useState)(Zc),
                _ = d[0],
                E = d[1],
                g = (0, u.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [n],
                ),
                p = mu(() => {
                  const t = c.current,
                    a = l.current,
                    n = e.getWrapperSize(),
                    u = e.getContainerSize();
                  if (!(n && u && t && a)) return;
                  const s = Math.min(1, n / u);
                  return (
                    (t.style.height = `${tm(a, s)}px`),
                    t.classList.add(Xc),
                    r.current &&
                      (1 === s ? r.current.classList.add(Gc) : r.current.classList.remove(Gc)),
                    s
                  );
                }),
                f = mu(() => {
                  const t = l.current,
                    a = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && a && r)) return;
                  const u = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / r),
                    m = lu(0, 1, u / (r - n)),
                    d = (t.offsetHeight - tm(t, s)) * m;
                  ((a.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (i.current && o.current && l.current && c.current) {
                        if (0 === e)
                          return (i.current.classList.add(Yc), void o.current.classList.remove(Yc));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetHeight - a.offsetHeight) >= -0.5)
                        )
                          return (i.current.classList.remove(Yc), void o.current.classList.add(Yc));
                        var t, a;
                        (i.current.classList.remove(Yc), o.current.classList.remove(Yc));
                      }
                    })(d));
                }),
                A = mu(() => {
                  em(e, () => {
                    (p(), f());
                  });
                });
              ((0, u.useEffect)(() => xe(A)),
                (0, u.useEffect)(() => {
                  const t = () => {
                    em(e, () => {
                      f();
                    });
                  };
                  let a = Kc;
                  const n = () => {
                    (a(), (a = xe(A)));
                  };
                  return (
                    e.events.on("recalculateContent", A),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", n),
                    () => {
                      (a(),
                        e.events.off("recalculateContent", A),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, u.useEffect)(() => {
                  if (!_.pending) return;
                  const t = (t) => {
                      em(e, (a) => {
                        const r = l.current,
                          u = c.current,
                          s = e.getContainerSize();
                        if (!r || !u || !s) return;
                        const i = t.screenY - _.offset - r.getBoundingClientRect().y,
                          o = (i / r.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(a, o),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: a.scrollTop },
                        }),
                          n({ type: "dragging", thumb: u, thumbOffset: i, contentOffset: o }));
                      });
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        g(Zc));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, _.offset, _.pending, n, g]));
              const h = du((t) => e.applyStepTo(t), m, [e]),
                v = h[0],
                b = h[1];
              (0, u.useEffect)(
                () => (
                  document.addEventListener("mouseup", b, !0),
                  () => document.removeEventListener("mouseup", b, !0)
                ),
                [b],
              );
              const D = (e) => {
                e.target.classList.contains(Yc) || $("highlight");
              };
              return s().createElement(
                "div",
                { className: F()(Uc, t.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: F()(qc, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Yc) || 0 !== e.button || ($("play"), v(pu.Next));
                  },
                  ref: i,
                  onMouseEnter: D,
                }),
                s().createElement(
                  "div",
                  {
                    className: F()(jc, t.track),
                    onMouseDown: (t) => {
                      const n = c.current;
                      if (n && 0 === t.button)
                        if (($("play"), t.target === n))
                          (e.handleIsThumbDragging(!0),
                            g({ pending: !0, offset: t.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            c.current &&
                              em(e, (n) => {
                                if (!n) return;
                                const r = a(e),
                                  u = e.clampPosition(n, n.scrollTop + r * t);
                                e.applyScroll(u);
                              });
                          })(t.screenY > n.getBoundingClientRect().y ? pu.Prev : pu.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: D,
                  },
                  s().createElement("div", { ref: c, className: t.thumb }),
                  s().createElement("div", { className: F()(Qc, t.rail) }),
                ),
                s().createElement("div", {
                  className: F()(Vc, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Yc) || 0 !== e.button || ($("play"), v(pu.Prev));
                  },
                  onMouseUp: b,
                  ref: o,
                  onMouseEnter: D,
                }),
              );
            },
          ),
          nm = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          rm = ({
            children: e,
            api: t,
            className: a,
            barClassNames: n,
            areaClassName: r,
            scrollClassName: i,
            scrollClassNames: o,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const m = (0, u.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: F()(nm.base, e.base) });
              }, [n]),
              d = (0, u.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return s().createElement(
              "div",
              { className: F()(nm.defaultScroll, a), onWheel: t.handleMouseWheel },
              s().createElement(
                "div",
                { className: F()(nm.area, r) },
                s().createElement(um, { className: i, classNames: o, api: d }, e),
              ),
              s().createElement(am, { getStepByRailClick: l, api: t, onDrag: c, classNames: m }),
            );
          },
          um = ({ className: e, classNames: t, children: a, api: n }) => (
            (0, u.useEffect)(() => xe(n.recalculateContent)),
            s().createElement(
              "div",
              { className: F()(nm.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              s().createElement(
                "div",
                { className: F()(nm.content, null == t ? void 0 : t.content), ref: n.contentRef },
                a,
              ),
            )
          );
        um.Default = rm;
        const sm = { Vertical: r, Horizontal: n };
        "undefined" != typeof Element &&
          (Element.prototype.matches ||
            Element.prototype.webkitMatchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector);
        ("undefined" != typeof document && document.documentElement.style,
          "undefined" != typeof window &&
            ("ontouchstart" in window ||
              (window.DocumentTouch && (document, window.DocumentTouch))),
          "undefined" != typeof navigator && navigator.msMaxTouchPoints,
          "undefined" != typeof navigator && /Chrome/i.test(navigator && navigator.userAgent));
        const im = {
            base: "LevelCard_base_cd",
            bgCompleted: "LevelCard_bgCompleted_e8",
            bgCompleted__completed: "LevelCard_bgCompleted__completed_53",
            bgCompleted__fast: "LevelCard_bgCompleted__fast_2a",
            completedIconContainer: "LevelCard_completedIconContainer_28",
            completedIconContainer__completed: "LevelCard_completedIconContainer__completed_47",
            completedIconContainer__prevLevel: "LevelCard_completedIconContainer__prevLevel_05",
            completedIcon: "LevelCard_completedIcon_40",
            completedIconGlow: "LevelCard_completedIconGlow_27",
            border: "LevelCard_border_b4",
            border__right: "LevelCard_border__right_c1",
          },
          om = "LevelLabel_base_10",
          lm = "LevelLabel_activeGlow_6d",
          cm = "LevelLabel_activeGlow__completed_b9",
          mm = "LevelLabel_level_4c",
          dm = "LevelLabel_level__completed_c4",
          _m = "LevelLabel_level__active_85",
          Em = "LevelLabel_tokenIcon_67",
          gm = "LevelLabel_tokenIcon__active_7a",
          pm = "LevelLabel_levelCurrent_ce",
          fm = "LevelLabel_levelCurrent__completed_97",
          Am = R.strings.tooltips.awardItem.comp7TokenWeeklyReward,
          hm = ({ level: e, isActive: t, isCompleted: a }) => {
            const n = F()(mm, a && dm, t && _m);
            return s().createElement(
              Ve,
              { header: Am.header(), body: Am.body() },
              s().createElement(
                "div",
                { className: om },
                s().createElement("div", { className: F()(lm, t && cm) }),
                t && s().createElement("div", { className: F()(pm, t && fm) }, e),
                !t && s().createElement("div", { className: n }, e),
                s().createElement("div", { className: F()(Em, { [gm]: t }) }),
              ),
            );
          },
          vm = "prevLevel",
          bm = "completed",
          Fm = "inProgress",
          Dm = (e, t, a) => (e ? bm : t ? Fm : a),
          Cm = (0, W.Pi)(({ level: e, isActive: t, isCompleted: a, isLast: n }) => {
            const r = (0, u.useState)(),
              i = r[0],
              o = r[1],
              l = Oc().model,
              c = (0, u.useRef)(null),
              m = l.computes.levelStatus(e),
              d = m.wasProgressionVisited,
              _ = m.isRecentlyCompletedLevel,
              E = m.isPrevLevel;
            (0, u.useEffect)(() => {
              a && !d && _ && o(vm);
            }, [a, d, _]);
            const g = (0, u.useCallback)(() => {
              $("pr_progress_tick");
            }, []);
            return (
              (0, u.useEffect)(() => {
                const e = c.current;
                return xe(() => {
                  if (e)
                    return (
                      e.addEventListener("transitionstart", g),
                      () => {
                        e.removeEventListener("transitionstart", g);
                      }
                    );
                });
              }, [c, g]),
              s().createElement(
                "div",
                { className: im.base },
                s().createElement("div", {
                  className: F()(im.bgCompleted, (t || a) && im.bgCompleted__completed),
                  ref: c,
                }),
                s().createElement(
                  "div",
                  {
                    className: F()(
                      im.completedIconContainer,
                      im[`completedIconContainer__${Dm(E, !a, i)}`],
                    ),
                  },
                  s().createElement("div", { className: im.completedIconGlow }),
                  s().createElement("div", { className: im.completedIcon }),
                ),
                s().createElement(hm, { level: e, isCompleted: a, isActive: t }),
                s().createElement("div", { className: im.border }),
                n && s().createElement("div", { className: F()(im.border, im.border__right) }),
              )
            );
          }),
          Bm = "LevelCards_base_b9";
        function wm() {
          return (
            (wm =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            wm.apply(this, arguments)
          );
        }
        const Sm = (0, W.Pi)(
            ({ levelRef: e }) => {
              const t = Oc().model.computes.levels();
              return s().createElement(
                "div",
                { className: Bm, ref: e },
                t.map((e) => s().createElement(Cm, wm({ key: e.level }, e))),
              );
            },
            { forwardRef: !0 },
          ),
          ym = {
            base: "RewardCard_base_1f",
            base__mediaLarge: "RewardCard_base__mediaLarge_1a",
            base__mediaExtraExtraLarge: "RewardCard_base__mediaExtraExtraLarge_c5",
            activeBlock: "RewardCard_activeBlock_0f",
            activeBlock__completed: "RewardCard_activeBlock__completed_7c",
            activeBlock__fast: "RewardCard_activeBlock__fast_1a",
            bgCompleted: "RewardCard_bgCompleted_3c",
            bgCompleted__completed: "RewardCard_bgCompleted__completed_c9",
            bgCompleted__fast: "RewardCard_bgCompleted__fast_93",
            border: "RewardCard_border_ab",
            border__right: "RewardCard_border__right_55",
          },
          Rm = "Rewards_base_76",
          xm = "Rewards_base__completed_f5",
          Pm = "Rewards_base__wide_f7",
          km = "Rewards_reward_24";
        function Tm() {
          return (
            (Tm =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Tm.apply(this, arguments)
          );
        }
        const Lm = ({ isCompleted: e, isActive: t, rewards: a, fixedSize: n }) => {
            const r = y(),
              u = null != n ? n : r.mediaSize <= B.Medium ? Go.Small : Go.Big,
              i = (e) => wl({ rewards: e, size: u }),
              o = F()(Rm, u === Go.Small && i(a).length > 2 && Pm, e && !t && xm);
            return s().createElement(
              "div",
              { className: o },
              be(i(a), (e) => s().createElement(_l, Tm({ className: km, key: e.name }, e))),
            );
          },
          Nm = ({ isCompleted: e, isActive: t, isLast: a, rewards: n }) => {
            const r = y(),
              u = F()(
                ym.base,
                r.mediaSize === B.Medium && ym.base__mediaMedium,
                r.mediaSize === B.Large && ym.base__mediaLarge,
                r.remScreenHeight >= 1200 && ym.base__mediaExtraExtraLarge,
              ),
              i = F()(ym.activeBlock, t && ym.activeBlock__completed),
              o = F()(ym.bgCompleted, (t || e) && ym.bgCompleted__completed);
            return s().createElement(
              "div",
              { className: u },
              s().createElement("div", { className: i }),
              s().createElement("div", { className: o }),
              s().createElement(Lm, { rewards: n, isActive: t, isCompleted: e }),
              s().createElement("div", { className: ym.border }),
              a && s().createElement("div", { className: F()(ym.border, ym.border__right) }),
            );
          },
          Im = "RewardCards_base_07",
          Mm = (0, W.Pi)(() => {
            const e = Oc().model.computes.levels();
            return s().createElement(
              "div",
              { className: Im },
              e.map(({ isCompleted: e, isActive: t, isLast: a, rewards: n }, r) =>
                s().createElement(Nm, {
                  key: r,
                  isCompleted: e,
                  isActive: t,
                  isLast: a,
                  rewards: n,
                }),
              ),
            );
          }),
          Om = "OptimizedProgressBar_base_1f",
          Hm = "OptimizedProgressBar_wrapper_ab",
          Wm = "OptimizedProgressBar_background_ce",
          $m = ["api", "value", "maxValue", "theme"];
        function zm() {
          return (
            (zm =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            zm.apply(this, arguments)
          );
        }
        const Um = (e, t) => ("number" == typeof t ? t : e.offsetLeft),
          Gm = (e) => {
            let t = e.api,
              a = e.value,
              n = e.maxValue,
              r = void 0 === n ? 100 : n,
              i = e.theme,
              o = void 0 === i ? $s : i,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, $m);
            const c = (0, u.useRef)(null),
              m = (0, u.useRef)(null),
              d = (0, u.useRef)(null),
              _ = lu(0, a, r) / r,
              E = (0, u.useCallback)(
                (e) => {
                  (d.current &&
                    c.current &&
                    (({ horizontalScrollPosition: e, leftOffset: t }, a, n) => {
                      const r = a.offsetWidth - n.offsetWidth,
                        u = e - Um(a, t),
                        s = lu(0, r, u);
                      n.style.left = `${s}px`;
                    })(e, c.current, d.current),
                    m.current &&
                      c.current &&
                      ((
                        { horizontalScrollPosition: e, leftOffset: t },
                        a,
                        { container: n, line: r },
                      ) => {
                        const u = Math.max(0, Math.floor(n.offsetWidth * a) - 8e3),
                          s = e - Um(n, t),
                          i = lu(0, u, s);
                        r.style.left = `${i}px`;
                      })(e, _, { line: m.current, container: c.current }));
                },
                [_],
              ),
              g = (0, u.useMemo)(() => Hs(o), [o]);
            return (
              (t.current.update = E),
              s().createElement(
                "div",
                { className: Om, ref: c },
                s().createElement(
                  "div",
                  { className: Hm },
                  s().createElement(
                    "div",
                    { style: g, className: F()(Wm, l.progressBarBackgroundClassMix), ref: d },
                    s().createElement(ms, {
                      size: l.size,
                      classMix: l.progressBarBackgroundClassMix,
                    }),
                  ),
                  s().createElement(
                    Us,
                    zm({}, l, {
                      lineRef: m,
                      value: a,
                      theme: o,
                      maxValue: r,
                      withoutBackground: !0,
                    }),
                  ),
                ),
              )
            );
          },
          qm = (e, t, a) =>
            F()(
              e[a],
              t === yc.ProgressAlreadyFinished
                ? e[`${a}__fast`]
                : t >= yc.ProgressFinished
                  ? e[`${a}__completed`]
                  : void 0,
            ),
          Vm = {
            base: "Container_base_31",
            progressWrapper: "Container_progressWrapper_e1",
            progressWrapper__completed: "Container_progressWrapper__completed_9e",
            progressWrapper__fast: "Container_progressWrapper__fast_af",
            bg: "Container_bg_d7",
          },
          jm = (0, W.Pi)(({ api: e, theme: t }) => {
            const a = Oc(),
              n = a.model,
              r = a.controls,
              i = n.progressAnimationState.get(),
              o = n.computes,
              l = n.previousTokenValue.get(),
              c = n.currentTokenValue.get(),
              m = (0, u.useRef)({ update: () => {} });
            e.current.moveProgressBars = (0, u.useCallback)((e) => {
              m.current.update(e);
            }, []);
            const d = (0, u.useState)({
                maxPoints: 1 * o.levels().length,
                previousEarnedPoints: l,
                progressionSize: l,
              }),
              _ = d[0],
              E = _.previousEarnedPoints,
              g = _.maxPoints,
              p = _.progressionSize,
              f = d[1];
            (0, u.useEffect)(() => {
              (f((e) => {
                const t = 0 === e.progressionSize ? l : e.progressionSize;
                return {
                  maxPoints: 1 * o.levels().length,
                  previousEarnedPoints: t,
                  progressionSize: c,
                };
              }),
                l !== c && $("pr_progress_bar"));
            }, [l, c, o]);
            const A = (0, u.useMemo)(
              () =>
                Object.assign({}, zs, {
                  withStack: !0,
                  type: cs.Growing,
                  delta: { duration: 400, delay: 300 },
                  line: { duration: 400, delay: 300 },
                }),
              [],
            );
            return (
              (0, u.useEffect)(() => {
                if (i === yc.ProgressChange)
                  return Ra(() => {
                    r.finishProgressionChange();
                  }, 700);
              }, [r, i]),
              s().createElement(
                "div",
                { className: Vm.base },
                s().createElement("div", { className: Vm.bg }),
                s().createElement(
                  "div",
                  { className: qm(Vm, i, "progressWrapper") },
                  s().createElement(Gm, {
                    animationSettings: A,
                    deltaFrom: E,
                    value: p,
                    maxValue: g,
                    api: m,
                    theme: t,
                  }),
                ),
              )
            );
          }),
          Xm = {
            base: "Content_base_d5",
            base__centered: "Content_base__centered_e6",
            base__layoutReady: "Content_base__layoutReady_84",
            horizontalContent: "Content_horizontalContent_91",
            wrapper: "Content_wrapper_d8",
            progress: "Content_progress_35",
            progressArea: "Content_progressArea_68",
          },
          Qm = "ScrollDrag_base_bd",
          Ym = "ScrollDrag_base__grabbing_1f",
          Km = ({ api: e, children: t, updateProgressBarPosition: a }) => {
            const n = (0, u.useState)(0),
              r = n[0],
              i = n[1],
              o = (0, u.useState)(0),
              l = o[0],
              c = o[1],
              m = (0, u.useState)(!1),
              d = m[0],
              _ = m[1];
            (0, u.useEffect)(
              () =>
                xe(() => {
                  const t = (e) => {
                    const t = e.value.scrollPosition;
                    d || i(-t);
                  };
                  return (
                    e.events.on("change", t),
                    () => {
                      e.events.off("change", t);
                    }
                  );
                }),
              [e, d],
            );
            const E = (0, u.useCallback)(
                (e) => {
                  (_(!0), c(e.clientX), a());
                },
                [a],
              ),
              g = (0, u.useCallback)(() => {
                (_(!1), c(0), a());
              }, [a]),
              p = (0, u.useCallback)(
                (t) => {
                  if (d) {
                    const n = lu(-(e.getBounds()[1] || 0), 0, r + t.clientX - l);
                    (e.applyScroll(-n, !0), c(t.clientX), i(n), a());
                  }
                },
                [d, e, r, l, a],
              );
            return s().createElement(
              "div",
              {
                className: F()(Qm, d && Ym),
                onMouseDown: E,
                onMouseUp: g,
                onMouseMove: p,
                onMouseLeave: g,
              },
              t,
            );
          };
        function Zm(e, t, a, n, r, u, s) {
          try {
            var i = e[u](s),
              o = i.value;
          } catch (e) {
            return void a(e);
          }
          i.done ? t(o) : Promise.resolve(o).then(n, r);
        }
        const Jm = (0, W.Pi)(() => {
            const e = Oc().model,
              t = hu(),
              a = e.computes,
              n = a.levels,
              r = a.getScrollContainerMaxWidth,
              i = a.currentLevel,
              o = y(),
              l = (0, u.useState)(!1),
              c = l[0],
              m = l[1],
              d = (0, u.useState)(!1),
              _ = d[0],
              E = d[1],
              g = n().length,
              p = e.currentTokenValue.get(),
              f = r(o.mediaSize, e.computes.levels(), o.mediaSize >= B.Large ? Lc : Nc, 0),
              A = (0, u.useRef)({ moveProgressBars: te }),
              h = (0, u.useRef)(null),
              v = (0, u.useRef)(null),
              b = t.animationScroll.scrollPosition,
              D = t.getWrapperSize,
              C = t.contentRef,
              w = t.wrapperRef,
              S = t.getContainerSize,
              R = t.applyScroll;
            (0, u.useLayoutEffect)(
              () =>
                xe(() => {
                  const e = w.current,
                    t = v.current;
                  if (!e || !t) return;
                  const a = parseFloat(getComputedStyle(t.children[0]).width),
                    n = parseFloat(getComputedStyle(t).paddingRight),
                    r = parseFloat(getComputedStyle(e).paddingLeft);
                  (m(o.remScreenWidth >= g * a + n + r), E(!0));
                }),
              [o.remScreenWidth, w, g],
            );
            const x = (0, u.useCallback)(
                (e) => {
                  if (h.current) {
                    const t = D();
                    A.current.moveProgressBars({
                      viewPort: h.current,
                      horizontalScrollPosition: t ? e - t : e,
                    });
                  }
                },
                [D],
              ),
              P = () => {
                x(b.goal);
              },
              k = (0, u.useCallback)(() => {
                const e = C.current,
                  t = n().length;
                if (e && t > 0) {
                  const a = S() || 0,
                    n = D() || 0,
                    r = a / t,
                    u = i() * r,
                    s = (n - e.offsetLeft - r) / 2;
                  R(lu(0, a - n, u - s));
                }
                0 === b.goal && x(b.goal);
              }, [R, i, n, C, S, D, b.goal, x]);
            return (
              (0, u.useEffect)(() => {
                k();
              }, [p, k]),
              (0, u.useEffect)(() => {
                const e = (function () {
                  var e,
                    t =
                      ((e = function* () {
                        const e = S(),
                          t = b.goal;
                        (yield (0, X.Eu)(),
                          yield new Promise((e) => {
                            requestAnimationFrame(() => {
                              requestAnimationFrame(() => {
                                e();
                              });
                            });
                          }));
                        const a = S();
                        (x(a && e && a !== e ? (t * a) / e : t), k());
                      }),
                      function () {
                        var t = this,
                          a = arguments;
                        return new Promise(function (n, r) {
                          var u = e.apply(t, a);
                          function s(e) {
                            Zm(u, n, r, s, i, "next", e);
                          }
                          function i(e) {
                            Zm(u, n, r, s, i, "throw", e);
                          }
                          s(void 0);
                        });
                      });
                  return function () {
                    return t.apply(this, arguments);
                  };
                })();
                return (
                  engine.on("clientResized", e),
                  () => {
                    engine.off("clientResized", e);
                  }
                );
              }, []),
              (0, u.useEffect)(() => Ra(() => x(b.goal), 0), [p, b.goal, x]),
              s().createElement(
                "div",
                {
                  className: F()(Xm.base, c && Xm.base__centered, _ && Xm.base__layoutReady),
                  ref: h,
                  onWheel: () => x(b.goal),
                  style: { maxWidth: `${f}rem` },
                },
                s().createElement(
                  sm.Horizontal.Area.Default,
                  {
                    api: t,
                    className: Xm.horizontalContent,
                    classNames: { wrapper: Xm.wrapper },
                    barClassNames: { base: Xm.bar },
                    onDrag: P,
                  },
                  s().createElement(
                    Km,
                    { api: t, updateProgressBarPosition: P },
                    s().createElement(Sm, { levelRef: v }),
                    s().createElement(
                      "div",
                      { className: Xm.progress },
                      s().createElement(
                        "div",
                        { className: Xm.progressArea },
                        s().createElement(jm, { api: A }),
                      ),
                    ),
                    s().createElement(Mm, null),
                  ),
                ),
              )
            );
          }),
          ed = {
            base: "Progression_base_d2",
            contentWrapper: "Progression_contentWrapper_6f",
            progressionContentWrapper: "Progression_progressionContentWrapper_59",
            progressionContentWrapper__completed:
              "Progression_progressionContentWrapper__completed_a7",
            progressionContentWrapper__fast: "Progression_progressionContentWrapper__fast_58",
            prompt: "Progression_prompt_7b",
            "add-blur": "Progression_add-blur_31",
            hide: "Progression_hide_32",
            show: "Progression_show_89",
          },
          td = (0, W.Pi)(({ className: e }) => {
            const t = Oc(),
              a = t.model,
              n = t.controls,
              r = a.progressAnimationState.get(),
              i = a.computes.isProgressionCompleted(),
              o = a.computes.wasProgressionCompletedBeforeStart();
            return (
              (0, u.useEffect)(
                () =>
                  o || (r === yc.ChangeCompleted && i)
                    ? Ra(() => {
                        n.completeProgression();
                      }, 500)
                    : r === yc.HighlightCard
                      ? Ra(() => {
                          n.finishHighlightCard();
                        }, 500)
                      : void 0,
                [r, o, i, n],
              ),
              s().createElement(
                "div",
                { className: F()(ed.base, e) },
                s().createElement(
                  "div",
                  { className: ed.contentWrapper },
                  s().createElement(
                    "div",
                    { className: qm(ed, r, "progressionContentWrapper") },
                    s().createElement(Jm, null),
                  ),
                  s().createElement($c, { className: ed.prompt }),
                ),
              )
            );
          });
        let ad, nd, rd;
        (!(function (e) {
          ((e.NotStarted = "notStarted"),
            (e.Active = "active"),
            (e.LastWeek = "lastWeek"),
            (e.Finished = "finished"));
        })(ad || (ad = {})),
          (function (e) {
            ((e.Timer = "timer"),
              (e.Countdown = "countdown"),
              (e.Cooldown = "cooldown"),
              (e.None = "none"));
          })(nd || (nd = {})),
          (function (e) {
            ((e.Description = "description"),
              (e.Short = "short"),
              (e.Long = "long"),
              (e.Extended = "extended"));
          })(rd || (rd = {})));
        const ud = () => {},
          sd = (e = 0, t, a = 0, n = ud) => {
            const r = (0, u.useState)(e),
              s = r[0],
              i = r[1];
            return (
              (0, u.useEffect)(() => {
                if (e > 0) {
                  i(e);
                  const r = Date.now(),
                    u = setInterval(
                      () => {
                        const t = e - Math.floor((Date.now() - r) / 1e3);
                        null !== a && t <= a ? (i(a), n && n(), clearInterval(u)) : i(t);
                      },
                      1e3 * (t || (e > 120 ? Pa : 1)),
                    );
                  return () => {
                    clearInterval(u);
                  };
                }
                i(0);
              }, [e, t, a, n]),
              s
            );
          };
        X.Sw.instance;
        let id;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(id || (id = {}));
        X.Sw.instance;
        const od = sd,
          ld = "Countdown_base_fe",
          cd = "Countdown_icon_8b",
          md = "Countdown_description_8d",
          dd = (e) => e.toString().padStart(2, "0"),
          _d = (e, t, a = !1) => {
            switch (t) {
              case rd.Description:
                return ((e, t = !0, a = !1) =>
                  e.days > 7 && t
                    ? sa(R.strings.common.duration.days(), { days: e.days })
                    : e.days >= 1
                      ? 0 === e.hours
                        ? sa(R.strings.common.duration.days(), { days: e.days })
                        : `${sa(R.strings.common.duration.days(), { days: e.days })} ${sa(R.strings.common.duration.hours(), { hours: e.hours })}`
                      : e.hours >= 1
                        ? 0 === e.minutes
                          ? sa(R.strings.common.duration.hours(), { hours: e.hours })
                          : `${sa(R.strings.common.duration.hours(), { hours: e.hours })} ${sa(a ? R.strings.common.duration.shortMinutes() : R.strings.common.duration.minutes(), { minutes: e.minutes })}`
                        : sa(R.strings.common.duration.minutes(), { minutes: e.minutes || 1 }))(
                  e,
                  !0,
                  a,
                );
              case rd.Short:
                return `${dd(e.minutes)}:${dd(e.seconds)}`;
              case rd.Long:
                return `${dd(e.hours)}:${dd(e.minutes)}:${dd(e.seconds)}`;
              case rd.Extended:
                return `${sa(R.strings.common.duration.days(), { days: e.days })} | ${dd(e.hours)}:${dd(e.minutes)}:${dd(e.seconds)}`;
            }
          },
          Ed = R.images.gui.maps.icons.components.countdown,
          gd = (e, t) => {
            const a = 2 === t ? Ed.big : Ed;
            switch (e) {
              case nd.Timer:
                return a.clock();
              case nd.Countdown:
                return a.hourglass();
              case nd.Cooldown:
                return a.lock();
            }
          },
          pd = (0, u.memo)(
            ({
              duration: e,
              withShortMinutes: t = !1,
              icon: a = nd.Timer,
              style: n = rd.Description,
              onTimeReached: r,
              className: u = "",
              classNames: i = {},
              labelFormat: o = "",
            }) => {
              const l = n !== rd.Description ? 1 : void 0,
                c = od(e, l),
                m = uu();
              r && r[c] && r[c]();
              const d = _d(
                (function (e = 0) {
                  let t = e;
                  const a = Math.trunc(t / Ta);
                  t -= a * Ta;
                  const n = Math.trunc(t / ka);
                  t -= n * ka;
                  const r = Math.trunc(t / Pa);
                  return ((t -= r * Pa), { days: a, hours: n, minutes: r, seconds: t });
                })(c),
                n,
                t,
              );
              return s().createElement(
                "div",
                { className: F()(ld, u) },
                a !== nd.None &&
                  s().createElement("div", {
                    className: F()(cd, i.icon),
                    style: { backgroundImage: `url('${gd(a, m)}')` },
                  }),
                o
                  ? s().createElement(
                      "div",
                      { className: F()(md, i.text) },
                      s().createElement(Ia, { text: o, binding: { timerText: d } }),
                    )
                  : s().createElement("div", { className: F()(md, i.text) }, d),
              );
            },
          ),
          fd = {
            base: "Separator_base_81",
            separator: "Separator_separator_9e",
            base__completedBattleQuests: "Separator_base__completedBattleQuests_ef",
            separator__left: "Separator_separator__left_74",
            base__inProgressBattleQuests: "Separator_base__inProgressBattleQuests_4d",
            base__condition: "Separator_base__condition_d9",
            base__awards: "Separator_base__awards_d6",
            base__lockedByNoXVehicles: "Separator_base__lockedByNoXVehicles_00",
            base__lockedByInactiveSeason: "Separator_base__lockedByInactiveSeason_66",
            base__lockedByPreviousQuest: "Separator_base__lockedByPreviousQuest_75",
            base__completed: "Separator_base__completed_5f",
            show: "Separator_show_ca",
            separator__right: "Separator_separator__right_3d",
            ellipse: "Separator_ellipse_c0",
            firstLayer: "Separator_firstLayer_34",
            secondLayer: "Separator_secondLayer_54",
            "add-blur": "Separator_add-blur_ba",
            hide: "Separator_hide_0e",
          };
        let Ad;
        !(function (e) {
          ((e.Awards = "awards"),
            (e.Condition = "condition"),
            (e.CompletedBattleQuests = "completedBattleQuests"),
            (e.InProgressBattleQuests = "inProgressBattleQuests"));
        })(Ad || (Ad = {}));
        const hd = ({ children: e, statusAnimation: t, type: a }) =>
            s().createElement(
              "div",
              { className: F()(fd.base, fd[`base__${a}`], fd[`base__${t}`]) },
              s().createElement(
                "div",
                { className: F()(fd.separator, fd.separator__left) },
                s().createElement(
                  "div",
                  { className: fd.ellipse },
                  s().createElement(
                    "div",
                    { className: fd.firstLayer },
                    s().createElement("div", { className: fd.secondLayer }),
                  ),
                ),
              ),
              e,
              s().createElement(
                "div",
                { className: F()(fd.separator, fd.separator__right) },
                s().createElement(
                  "div",
                  { className: fd.ellipse },
                  s().createElement(
                    "div",
                    { className: fd.firstLayer },
                    s().createElement("div", { className: fd.secondLayer }),
                  ),
                ),
              ),
            ),
          vd = {
            base: "Timer_base_ad",
            timer: "Timer_timer_4c",
            block: "Timer_block_de",
            base__small: "Timer_base__small_5a",
            base__big: "Timer_base__big_03",
            text: "Timer_text_35",
            bgCountdown: "Timer_bgCountdown_86",
            description: "Timer_description_bc",
            countdown: "Timer_countdown_e1",
            "add-blur": "Timer_add-blur_c0",
            hide: "Timer_hide_7d",
            show: "Timer_show_1b",
          };
        let bd;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(bd || (bd = {}));
        const Fd = ({ size: e, currentTimerDate: t, text: a, onlyText: n = !1 }) => {
            const r = e === bd.Big;
            return s().createElement(
              "div",
              { className: F()(vd.base, vd[`base__${e}`]) },
              s().createElement(
                "div",
                { className: vd.timer },
                s().createElement(
                  hd,
                  { type: r ? Ad.CompletedBattleQuests : Ad.InProgressBattleQuests },
                  s().createElement(
                    "div",
                    { className: vd.block },
                    a && s().createElement("div", { className: vd.text }, a),
                    !n &&
                      t &&
                      s().createElement(
                        "div",
                        { className: vd.countdown },
                        s().createElement("div", { className: vd.bgCountdown }),
                        s().createElement(pd, {
                          duration: t,
                          style: rd.Description,
                          classNames: { text: vd.description },
                          className: vd.countdown,
                        }),
                      ),
                  ),
                ),
              ),
            );
          },
          Dd = "ResetStatus_base_25",
          Cd = "ResetStatus_base__ended_5e",
          Bd = "ResetStatus_endedTextTitle_20",
          wd = "ResetStatus_endedTextSubtitle_6e",
          Sd = R.strings.comp7.weeklyQuests.resetStatus,
          yd = (0, W.Pi)(({ className: e }) => {
            const t = Oc().model,
              a = t.root.get(),
              n = a.seasonState,
              r = a.resetTimeLeft,
              u = t.computes.isAllQuestsCompleted;
            return u() && n === ad.LastWeek
              ? s().createElement(
                  "div",
                  { className: F()(Dd, Cd, e) },
                  s().createElement(Ia, { text: Sd.ended.lastWeek.title(), classMix: Bd }),
                )
              : u()
                ? s().createElement(
                    "div",
                    { className: F()(Dd, Cd, e) },
                    s().createElement(Ia, { text: Sd.ended.title(), classMix: Bd }),
                    s().createElement(Ia, { text: Sd.ended.subtitle(), classMix: wd }),
                    s().createElement(Fd, {
                      size: bd.Big,
                      currentTimerDate: r,
                      text: Sd.ended.title(),
                    }),
                  )
                : n === ad.LastWeek
                  ? s().createElement(
                      "div",
                      { className: F()(Dd, e) },
                      s().createElement(Fd, {
                        size: bd.Small,
                        currentTimerDate: r,
                        text: Sd.lastWeek(),
                      }),
                    )
                  : s().createElement(
                      "div",
                      { className: F()(Dd, e) },
                      s().createElement(Fd, {
                        size: bd.Small,
                        currentTimerDate: r,
                        text: Sd.timer(),
                      }),
                    );
          }),
          Rd = "Progress_base_d5",
          xd = "Progress_counter_3b",
          Pd = "Progress_current_fd",
          kd = "Progress_progressBar_d2",
          Td = R.strings.comp7.weeklyQuests.card.progress,
          Ld = ({ current: e, total: t, isDisabled: a, className: n }) =>
            s().createElement(
              "div",
              { className: F()(Rd, n) },
              s().createElement(Ia, {
                classMix: xd,
                text: Td.counter(),
                binding: {
                  current: s().createElement(
                    "div",
                    { className: Pd },
                    s().createElement(Ja, { value: e }),
                  ),
                  total: s().createElement(Ja, { value: t }),
                },
              }),
              s().createElement(
                "div",
                { className: kd },
                s().createElement(Us, { size: ls.Small, value: e, maxValue: t, disabled: a }),
              ),
            ),
          Nd = {
            nextArrowWrapper: "TaskBattle_nextArrowWrapper_bb",
            nextArrow: "TaskBattle_nextArrow_32",
            nextArrow__completed: "TaskBattle_nextArrow__completed_0d",
            nextArrow__active: "TaskBattle_nextArrow__active_0a",
            base: "TaskBattle_base_44",
            base__completed: "TaskBattle_base__completed_96",
            "add-shadow": "TaskBattle_add-shadow_a9",
            base__lockedByNoXVehicles: "TaskBattle_base__lockedByNoXVehicles_65",
            base__lockedByInactiveSeason: "TaskBattle_base__lockedByInactiveSeason_b0",
            base__lockedByPreviousQuest: "TaskBattle_base__lockedByPreviousQuest_34",
            base__mediaMediumHeight: "TaskBattle_base__mediaMediumHeight_96",
            taskType: "TaskBattle_taskType_94",
            conditions: "TaskBattle_conditions_2d",
            description: "TaskBattle_description_f6",
            description__completed: "TaskBattle_description__completed_a2",
            "update-condition": "TaskBattle_update-condition_a0",
            description__completedWasVisited: "TaskBattle_description__completedWasVisited_42",
            awards: "TaskBattle_awards_0a",
            "add-blur": "TaskBattle_add-blur_68",
            base__completedWasVisited: "TaskBattle_base__completedWasVisited_8a",
            awardsList: "TaskBattle_awardsList_bf",
            award: "TaskBattle_award_8b",
            hide: "TaskBattle_hide_e0",
            show: "TaskBattle_show_4d",
          },
          Id = {
            base: "TaskType_base_d9",
            ellipse: "TaskType_ellipse_95",
            base__completed: "TaskType_base__completed_00",
            hide: "TaskType_hide_4e",
            base__completedWasVisited: "TaskType_base__completedWasVisited_28",
            base__lockedByNoXVehicles: "TaskType_base__lockedByNoXVehicles_99",
            base__lockedByInactiveSeason: "TaskType_base__lockedByInactiveSeason_c5",
            base__lockedByPreviousQuest: "TaskType_base__lockedByPreviousQuest_42",
            typeIcon: "TaskType_typeIcon_0c",
            completedIcon: "TaskType_completedIcon_cf",
            lockIcon: "TaskType_lockIcon_20",
            "slide-down": "TaskType_slide-down_53",
            "add-blur": "TaskType_add-blur_1d",
            show: "TaskType_show_a3",
          },
          Md = ({ taskBattleIcon: e, statusAnimation: t }) =>
            s().createElement(
              "div",
              { className: F()(Id.base, Id[`base__${t}`]) },
              s().createElement("div", { className: Id.ellipse }),
              s().createElement("div", {
                className: Id.typeIcon,
                style: {
                  backgroundImage: `url('${R.images.comp7.gui.maps.icons.comp7.weekly_quests.$dyn(e)}')`,
                },
              }),
              s().createElement("div", { className: Id.completedIcon }),
              s().createElement("div", { className: Id.lockIcon }),
            );
        function Od() {
          return (
            (Od =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Od.apply(this, arguments)
          );
        }
        const Hd = (0, W.Pi)(({ index: e }) => {
            const t = (0, u.useState)(wc.Active),
              a = t[0],
              n = t[1],
              r = Oc().model,
              i = r.computes.questRewards,
              o = r.computes.questCard(e),
              l = o.state,
              c = o.currentProgress,
              m = o.totalProgress,
              d = o.description,
              _ = o.iconKey,
              E = y();
            return (
              (0, u.useEffect)(() => {
                n(l);
              }, [l]),
              s().createElement(
                s().Fragment,
                null,
                Boolean(e) &&
                  s().createElement(
                    "div",
                    { className: Nd.nextArrowWrapper },
                    s().createElement("div", {
                      className: F()(Nd.nextArrow, Nd[`nextArrow__${a}`]),
                    }),
                  ),
                s().createElement(
                  "div",
                  {
                    className: F()(
                      Nd.base,
                      Nd[`base__${a}`],
                      E.mediaSize === B.Medium &&
                        E.remScreenHeight >= 1024 &&
                        Nd.base__mediaMediumHeight,
                    ),
                  },
                  s().createElement(
                    "div",
                    { className: Nd.taskType },
                    s().createElement(Md, { taskBattleIcon: _, statusAnimation: a }),
                  ),
                  s().createElement(
                    "div",
                    { className: Nd.conditions },
                    s().createElement(
                      "div",
                      { className: F()(Nd.description, Nd[`description__${a}`]) },
                      d,
                    ),
                    l === wc.Active &&
                      s().createElement(Ld, { current: c, total: m, isDisabled: l !== wc.Active }),
                  ),
                  s().createElement(
                    "div",
                    { className: Nd.awards },
                    s().createElement(
                      hd,
                      { statusAnimation: a, type: Ad.Awards },
                      s().createElement(
                        "div",
                        { className: Nd.awardsList },
                        be(i(e, Go.Small), (e) =>
                          s().createElement(_l, Od({ className: Nd.award, key: e.name }, e)),
                        ),
                      ),
                    ),
                  ),
                ),
              )
            );
          }),
          Wd = {
            "--pageContentWidth": "78vw",
            base__completed: "TaskBattleList_base__completed_e6",
            "hidden-tasks-list": "TaskBattleList_hidden-tasks-list_39",
            base: "TaskBattleList_base_c6",
            scroll: "TaskBattleList_scroll_73",
            timerWithQuestsTotal: "TaskBattleList_timerWithQuestsTotal_39",
            timer: "TaskBattleList_timer_fe",
            taskList: "TaskBattleList_taskList_d4",
            scrollContainer: "TaskBattleList_scrollContainer_e0",
            areaContainer: "TaskBattleList_areaContainer_fb",
            areaWrapper: "TaskBattleList_areaWrapper_04",
            bar: "TaskBattleList_bar_d9",
            "add-blur": "TaskBattleList_add-blur_67",
            hide: "TaskBattleList_hide_56",
            show: "TaskBattleList_show_f9",
            fadeIn: "TaskBattleList_fadeIn_38",
            fadeInThreeQuarters: "TaskBattleList_fadeInThreeQuarters_b4",
            fadeInHalf: "TaskBattleList_fadeInHalf_5a",
            fadeOut: "TaskBattleList_fadeOut_f6",
            fadeInWithScale: "TaskBattleList_fadeInWithScale_0a",
            slideUp: "TaskBattleList_slideUp_dd",
            scale: "TaskBattleList_scale_d4",
            raysAppearance: "TaskBattleList_raysAppearance_32",
            rotate: "TaskBattleList_rotate_3f",
            "reverse-rotate": "TaskBattleList_reverse-rotate_56",
            glowAppearance: "TaskBattleList_glowAppearance_55",
            highlightAppearance: "TaskBattleList_highlightAppearance_7c",
            blink: "TaskBattleList_blink_1d",
            slideUpIn: "TaskBattleList_slideUpIn_33",
          },
          $d = (0, W.Pi)(() => {
            const e = Oc().model.computes,
              t = e.questCards,
              a = e.battleTasksStatus,
              n = e.initialItemScrollIndex,
              r = e.getScrollContainerMaxWidth,
              i = y(),
              o = (0, u.useState)(n()),
              l = o[0],
              c = o[1],
              m = Wu(268),
              d = t.get();
            return s().createElement(
              "div",
              { className: F()(Wd.base, Wd[`base__${a()}`]) },
              s().createElement(
                "div",
                { className: Wd.taskList },
                s().createElement(
                  Hu,
                  {
                    api: m,
                    stuckIndex: l,
                    itemWidth: 268,
                    onStick: c,
                    className: Wd.scrollContainer,
                    areaClassNames: { base: Wd.areaContainer, wrapper: Wd.areaWrapper },
                    barClassNames: { base: Wd.bar },
                    containerMaxWidth: r(i.mediaSize, d, 268, 38),
                  },
                  be(d, (e, t) => s().createElement(Hd, { key: t, index: t })),
                ),
              ),
            );
          }),
          zd = "WeeklyQuestsPage_base_6c",
          Ud = "WeeklyQuestsPage_content_cc",
          Gd = "WeeklyQuestsPage_resetStatus_8a",
          qd = "WeeklyQuestsPage_progression_25",
          Vd = () => {
            const e = (0, Pe.useSpring)(_e);
            return s().createElement(
              "div",
              { className: zd },
              s().createElement(ya, { className: K }, R.strings.comp7.page.heading.weeklyQuests()),
              s().createElement(Qa, null),
              s().createElement(
                Pe.animated.div,
                { className: Ud, style: e },
                s().createElement(yd, { className: Gd }),
                s().createElement($d, null),
                s().createElement(td, { className: qd }),
              ),
            );
          },
          jd = { context: "model.weeklyQuestsModel" },
          Xd = {
            [me.Progression]: () =>
              s().createElement(Ba, { options: Oo }, s().createElement(Mo, null)),
            [me.RankRewards]: () =>
              s().createElement(Wo, { options: Bc }, s().createElement(Cc, null)),
            [me.WeeklyQuests]: () =>
              s().createElement(Mc, { options: jd }, s().createElement(Vd, null)),
          },
          Qd = (0, u.memo)(({ pageView: e }) => {
            if (e === me.Leaderboard) return s().createElement(ta, null);
            const t = Xd[e];
            return t
              ? s().createElement(t, null)
              : (console.error("Unreachable code: ViewResolver"), null);
          }),
          Yd = {
            "--pageContentWidth": "78vw",
            base: "App_base_ef",
            base__qualification: "App_base__qualification_73",
            base__leaderboard: "App_base__leaderboard_da",
            base__rankRewards: "App_base__rankRewards_55",
            base__weeklyQuests: "App_base__weeklyQuests_58",
            viewContainer: "App_viewContainer_81",
            sidebar: "App_sidebar_95",
          },
          Kd = { context: "model.sidebar" },
          Zd = { context: "model.scheduleInfo" },
          Jd = (0, W.Pi)(() => {
            const e = fe(),
              t = e.model,
              a = e.controls,
              n = t.root.get().pageViewId,
              r = t.computes.isProgressionInQualification(),
              u = null == de ? void 0 : de[n],
              i = r && !ee(),
              o = !r && Boolean(u),
              l = F()(Yd.base, i && Yd.base__qualification, o && Yd[`base__${u}`]);
            return s().createElement(
              "div",
              { className: l },
              s().createElement(
                "div",
                { className: Yd.viewContainer },
                s().createElement(le, { options: Zd }, s().createElement(Qd, { pageView: n })),
              ),
              s().createElement(
                ye,
                { options: Kd },
                s().createElement(Ke, { pageView: n, className: Yd.sidebar }),
              ),
              s().createElement(J, { onClose: a.close }),
            );
          });
        engine.whenReady.then(() => {
          H().render(
            s().createElement(M, null, s().createElement(pe, null, s().createElement(Jd, null))),
            document.getElementById("root"),
          );
        });
      },
    },
    __webpack_module_cache__ = {},
    deferred;
  function __webpack_require__(e) {
    var t = __webpack_module_cache__[e];
    if (void 0 !== t) return t.exports;
    var a = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](a, a.exports, __webpack_require__), a.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, a, n) => {
      if (!t) {
        var r = 1 / 0;
        for (o = 0; o < deferred.length; o++) {
          for (var [t, a, n] = deferred[o], u = !0, s = 0; s < t.length; s++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[s]))
              ? t.splice(s--, 1)
              : ((u = !1), n < r && (r = n));
          if (u) {
            deferred.splice(o--, 1);
            var i = a();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      n = n || 0;
      for (var o = deferred.length; o > 0 && deferred[o - 1][2] > n; o--)
        deferred[o] = deferred[o - 1];
      deferred[o] = [t, a, n];
    }),
    (__webpack_require__.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(t, { a: t }), t);
    }),
    (__webpack_require__.d = (e, t) => {
      for (var a in t)
        __webpack_require__.o(t, a) &&
          !__webpack_require__.o(e, a) &&
          Object.defineProperty(e, a, { enumerable: !0, get: t[a] });
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
    (__webpack_require__.j = 992),
    (() => {
      var e = { 992: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, a) => {
          var n,
            r,
            [u, s, i] = a,
            o = 0;
          if (u.some((t) => 0 !== e[t])) {
            for (n in s) __webpack_require__.o(s, n) && (__webpack_require__.m[n] = s[n]);
            if (i) var l = i(__webpack_require__);
          }
          for (t && t(a); o < u.length; o++)
            ((r = u[o]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        a = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (a.forEach(t.bind(null, 0)), (a.push = t.bind(null, a.push.bind(a))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [926], () => __webpack_require__(7860));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
