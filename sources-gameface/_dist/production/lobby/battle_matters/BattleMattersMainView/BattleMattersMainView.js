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
        t.d(u, { O: () => Y });
        var n = {};
        (t.r(n), t.d(n, { mouse: () => d, onResize: () => l }));
        var a = {};
        (t.r(a),
          t.d(a, {
            events: () => n,
            getMouseGlobalPosition: () => m,
            getSize: () => E,
            graphicsQuality: () => _,
          }));
        var r = {};
        (t.r(r), t.d(r, { getBgUrl: () => F, getTextureUrl: () => A }));
        var s = {};
        function o(e) {
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
        (t.r(s),
          t.d(s, {
            addModelObserver: () => y,
            addPreloadTexture: () => w,
            children: () => r,
            displayStatus: () => g,
            displayStatusIs: () => z,
            events: () => D,
            extraSize: () => q,
            forceTriggerMouseMove: () => W,
            freezeTextureBeforeResize: () => N,
            getBrowserTexturePath: () => P,
            getDisplayStatus: () => Q,
            getScale: () => k,
            getSize: () => R,
            getViewGlobalPosition: () => M,
            isClientAccessible: () => U,
            isEventHandled: () => $,
            isFocused: () => H,
            pxToRem: () => I,
            remToPx: () => L,
            resize: () => T,
            sendEvent: () => v,
            setAnimateWindow: () => O,
            setEventHandled: () => G,
            setInputPaddingsRem: () => S,
            setSidePaddingsRem: () => x,
            whenTutorialReady: () => j,
          }));
        const l = o("clientResized"),
          c = { down: o("mousedown"), up: o("mouseup"), move: o("mousemove") };
        const d = (function () {
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
          const a = ["down", "up", "move"].reduce(
            (u, t) => (
              (u[t] = (function (u) {
                return (t) => {
                  e.listeners += 1;
                  let a = !0;
                  const r = `mouse${u}`,
                    s = c[u]((e) => t([e, "outside"]));
                  function o(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, o),
                    n(),
                    () => {
                      a &&
                        (s(), window.removeEventListener(r, o), (e.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(t)),
              u
            ),
            {},
          );
          return Object.assign({}, a, {
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
        function E(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function m(e = "px") {
          return "rem" === e
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const _ = {
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
          D = {
            onTextureFrozen: o("self.onTextureFrozen"),
            onTextureReady: o("self.onTextureReady"),
            onDomBuilt: o("self.onDomBuilt"),
            onLoaded: o("self.onLoaded"),
            onDisplayChanged: o("self.onShowingStatusChanged"),
            onFocusUpdated: o("self.onFocusChanged"),
            children: {
              onAdded: o("children.onAdded"),
              onLoaded: o("children.onLoaded"),
              onRemoved: o("children.onRemoved"),
              onAttached: o("children.onAttached"),
              onTextureReady: o("children.onTextureReady"),
              onRequestPosition: o("children.requestPosition"),
            },
          },
          B = ["args"];
        const C = 2,
          p = 16,
          b = 32,
          h = 64,
          f = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, B);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
                      arguments:
                        ((n = a),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, r));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          v = {
            close(e) {
              f("popover" === e ? C : b);
            },
            minimize() {
              f(h);
            },
            move(e) {
              f(p, { isMouseEvent: !0, on: e });
            },
          };
        function w(e) {
          viewEnv.addPreloadTexture(e);
        }
        function S(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function P(e, u, t, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, n);
        }
        function y(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function x(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function R(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function T(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function M(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: L(u.x), y: L(u.y) };
        }
        function N() {
          viewEnv.freezeTextureBeforeResize();
        }
        function k() {
          return viewEnv.getScale();
        }
        function I(e) {
          return viewEnv.pxToRem(e);
        }
        function L(e) {
          return viewEnv.remToPx(e);
        }
        function O(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function H() {
          return viewEnv.isFocused();
        }
        function U() {
          return viewEnv.isClientAccessible();
        }
        function G() {
          return viewEnv.setEventHandled();
        }
        function $() {
          return viewEnv.isEventHandled();
        }
        function W() {
          viewEnv.forceTriggerMouseMove();
        }
        function Q() {
          return viewEnv.getShowingStatus();
        }
        const z = Object.keys(g).reduce(
            (e, u) => ((e[u] = () => viewEnv.getShowingStatus() === g[u]), e),
            {},
          ),
          q = {
            set: (e, u) => {
              viewEnv.setExtraSizeRem(e, u);
            },
            get: (e, u) => {
              viewEnv.getExtraSizeRem(e, u);
            },
          },
          j = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : D.onDomBuilt(e);
            }),
            engine.whenReady,
          ]),
          Y = { view: s, client: a };
      },
      521: (e, u, t) => {
        "use strict";
        let n, a;
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
          })(a || (a = {})));
      },
      358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var n = t(67);
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
          addCallback(e, u, t = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = n.O.view.addModelObserver(e, t, a);
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
              const n = this._callbacks[t];
              void 0 !== n && n(e, u);
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
        t.d(u, { B3: () => l, Z5: () => s, B0: () => i, ry: () => D });
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
        const a = n;
        var r = t(358);
        const s = {
            getNumberFormat: (e, u) => systemLocale.getNumberFormat(e, u),
            getRealFormat: (e, u) => systemLocale.getRealFormat(e, u),
            getTimeFormat: (e, u) => systemLocale.getTimeFormat(e, u),
            getDateFormat: (e, u) => systemLocale.getDateFormat(e, u),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          o = {
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
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var m = t(521),
          _ = t(67);
        const A = ["args"];
        function F(e, u, t, n, a, r, s) {
          try {
            var o = e[r](s),
              i = o.value;
          } catch (e) {
            return void t(e);
          }
          o.done ? u(i) : Promise.resolve(i).then(n, a);
        }
        const g = (e) => ({
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
                  return new Promise(function (n, a) {
                    var r = e.apply(u, t);
                    function s(e) {
                      F(r, n, a, s, o, "next", e);
                    }
                    function o(e) {
                      F(r, n, a, s, o, "throw", e);
                    }
                    s(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          B = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const a = u.args,
                r = (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(u, A);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: e }, r, {
                      arguments:
                        ((n = a),
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: t, type: e });
            var n;
          },
          C = () => B(i.CLOSE),
          p = (e, u) => {
            e.keyCode === m.n.ESCAPE && u();
          };
        var b = t(572);
        const h = a.instance,
          f = {
            DataTracker: r.Z,
            ViewModel: b.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: d,
            DateFormatType: E,
            makeGlobalBoundingBox: g,
            sendMoveEvent: (e) => B(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: () => B(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              B(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, n, a = R.invalid("resId"), r) => {
              const s = _.O.view.getViewGlobalPosition(),
                o = t.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                d = o.width,
                E = o.height,
                m = {
                  x: _.O.view.pxToRem(l) + s.x,
                  y: _.O.view.pxToRem(c) + s.y,
                  width: _.O.view.pxToRem(d),
                  height: _.O.view.pxToRem(E),
                };
              B(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: n || R.invalid("resId"),
                targetID: a,
                direction: u,
                bbox: g(m),
                on: !0,
                args: r,
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
              p(e, C);
            },
            handleViewEvent: B,
            onBindingsReady: D,
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
                  const a = Object.prototype.toString.call(u[n]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = u[n];
                    t[n] = [];
                    for (let u = 0; u < a.length; u++) t[n].push({ value: e(a[u].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[n] = e(u[n]))
                      : (t[n] = u[n]);
                }
              return t;
            },
            ClickOutsideManager: h,
            SystemLocale: s,
            UserLocale: o,
          };
        window.ViewEnvHelper = f;
      },
      86: (e, u, t) => {
        "use strict";
        var n = t(179),
          a = t.n(n);
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
        var s = t(67);
        const o = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var i;
        function l(e, u, t) {
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
            a = (function (e, u) {
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
        })(i || (i = {}));
        const c = s.O.client.getSize("rem"),
          d = c.width,
          E = c.height,
          m = Object.assign({ width: d, height: E }, l(d, E, o)),
          _ = (0, n.createContext)(m),
          A = ["children"];
        const F = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, A);
          const a = (0, n.useContext)(_),
            s = a.extraLarge,
            o = a.large,
            i = a.medium,
            l = a.small,
            c = a.extraSmall,
            d = a.extraLargeWidth,
            E = a.largeWidth,
            m = a.mediumWidth,
            F = a.smallWidth,
            g = a.extraSmallWidth,
            D = a.extraLargeHeight,
            B = a.largeHeight,
            C = a.mediumHeight,
            p = a.smallHeight,
            b = a.extraSmallHeight,
            h = { extraLarge: D, large: B, medium: C, small: p, extraSmall: b };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && s) return u;
            if (t.large && o) return u;
            if (t.medium && i) return u;
            if (t.small && l) return u;
            if (t.extraSmall && c) return u;
          } else {
            if (t.extraLargeWidth && d) return r(u, t, h);
            if (t.largeWidth && E) return r(u, t, h);
            if (t.mediumWidth && m) return r(u, t, h);
            if (t.smallWidth && F) return r(u, t, h);
            if (t.extraSmallWidth && g) return r(u, t, h);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && D) return u;
              if (t.largeHeight && B) return u;
              if (t.mediumHeight && C) return u;
              if (t.smallHeight && p) return u;
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
        (0, n.memo)(F);
        const g = (e) => {
            const u = (0, n.useRef)(!1);
            u.current || (e(), (u.current = !0));
          },
          D = (0, n.memo)(({ children: e }) => {
            const u = (0, n.useContext)(_),
              t = (0, n.useState)(u),
              r = t[0],
              i = t[1],
              c = (0, n.useCallback)((e, u) => {
                const t = s.O.view.pxToRem(e),
                  n = s.O.view.pxToRem(u);
                i(Object.assign({ width: t, height: n }, l(t, n, o)));
              }, []);
            (g(() => {
              engine.on("clientResized", c);
            }),
              (0, n.useEffect)(() => () => engine.off("clientResized", c), [c]));
            const d = (0, n.useMemo)(() => Object.assign({}, r), [r]);
            return a().createElement(_.Provider, { value: d }, e);
          });
        var B = t(483),
          C = t.n(B),
          p = t(926),
          b = t.n(p);
        let h, f, v;
        (!(function (e) {
          ((e[(e.ExtraSmall = o.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = o.small.width)] = "Small"),
            (e[(e.Medium = o.medium.width)] = "Medium"),
            (e[(e.Large = o.large.width)] = "Large"),
            (e[(e.ExtraLarge = o.extraLarge.width)] = "ExtraLarge"));
        })(h || (h = {})),
          (function (e) {
            ((e[(e.ExtraSmall = o.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = o.small.width)] = "Small"),
              (e[(e.Medium = o.medium.width)] = "Medium"),
              (e[(e.Large = o.large.width)] = "Large"),
              (e[(e.ExtraLarge = o.extraLarge.width)] = "ExtraLarge"));
          })(f || (f = {})),
          (function (e) {
            ((e[(e.ExtraSmall = o.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = o.small.height)] = "Small"),
              (e[(e.Medium = o.medium.height)] = "Medium"),
              (e[(e.Large = o.large.height)] = "Large"),
              (e[(e.ExtraLarge = o.extraLarge.height)] = "ExtraLarge"));
          })(v || (v = {})));
        const w = () => {
            const e = (0, n.useContext)(_),
              u = e.width,
              t = e.height,
              a = ((e) => {
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
                    return f.ExtraLarge;
                  case e.largeWidth:
                    return f.Large;
                  case e.mediumWidth:
                    return f.Medium;
                  case e.smallWidth:
                    return f.Small;
                  case e.extraSmallWidth:
                    return f.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), f.ExtraSmall);
                }
              })(e),
              s = ((e) => {
                switch (!0) {
                  case e.extraLargeHeight:
                    return v.ExtraLarge;
                  case e.largeHeight:
                    return v.Large;
                  case e.mediumHeight:
                    return v.Medium;
                  case e.smallHeight:
                    return v.Small;
                  case e.extraSmallHeight:
                    return v.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), v.ExtraSmall);
                }
              })(e);
            return {
              mediaSize: a,
              mediaWidth: r,
              mediaHeight: s,
              remScreenWidth: u,
              remScreenHeight: t,
            };
          },
          S = ["children", "className"];
        function P() {
          return (
            (P =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            P.apply(this, arguments)
          );
        }
        const y = {
            [f.ExtraSmall]: "",
            [f.Small]: b().SMALL_WIDTH,
            [f.Medium]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH}`,
            [f.Large]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH}`,
            [f.ExtraLarge]: `${b().SMALL_WIDTH} ${b().MEDIUM_WIDTH} ${b().LARGE_WIDTH} ${b().EXTRA_LARGE_WIDTH}`,
          },
          x = {
            [v.ExtraSmall]: "",
            [v.Small]: b().SMALL_HEIGHT,
            [v.Medium]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT}`,
            [v.Large]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT}`,
            [v.ExtraLarge]: `${b().SMALL_HEIGHT} ${b().MEDIUM_HEIGHT} ${b().LARGE_HEIGHT} ${b().EXTRA_LARGE_HEIGHT}`,
          },
          T = {
            [h.ExtraSmall]: "",
            [h.Small]: b().SMALL,
            [h.Medium]: `${b().SMALL} ${b().MEDIUM}`,
            [h.Large]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE}`,
            [h.ExtraLarge]: `${b().SMALL} ${b().MEDIUM} ${b().LARGE} ${b().EXTRA_LARGE}`,
          },
          M = (e) => {
            let u = e.children,
              t = e.className,
              n = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, S);
            const r = w(),
              s = r.mediaWidth,
              o = r.mediaHeight,
              i = r.mediaSize;
            return a().createElement("div", P({ className: C()(t, y[s], x[o], T[i]) }, n), u);
          },
          N = ["children"];
        const k = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, N);
          return a().createElement(D, null, a().createElement(M, t, u));
        };
        var I = t(493),
          L = t.n(I),
          O = t(521),
          H = t(364);
        const U = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function G(e = O.n.NONE, u = U, t = !1) {
          (0, n.useEffect)(() => {
            if (e !== O.n.NONE)
              return (
                window.addEventListener("keydown", n, t),
                () => {
                  window.removeEventListener("keydown", n, t);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (s.O.view.isEventHandled()) return;
                (s.O.view.setEventHandled(), u(n), t && n.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        var $ = t(403);
        const W = "Background_base_1b",
          Q = "Background_image_71",
          z = ({ isBlurred: e, children: u, onLoaded: t }) => {
            const r = e
              ? "img://gui/maps/icons/battleMatters/common/background_blurred.dds"
              : R.images.gui.maps.icons.battleMatters.common.background();
            var s, o;
            return (
              (s = r),
              (o = t),
              (0, n.useEffect)(() => {
                if (!o) return;
                const e = new Image();
                return (
                  e.addEventListener("load", o),
                  e.addEventListener("error", o),
                  (e.src = s),
                  () => {
                    (e.removeEventListener("load", o), e.removeEventListener("error", o));
                  }
                );
              }, [o, s]),
              a().createElement(
                "div",
                { className: W },
                a().createElement(
                  "div",
                  { className: Q, style: { backgroundImage: `url(${r})` } },
                  u,
                ),
              )
            );
          };
        class q extends a().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = H.B3.GOLD;
            else e = H.B3.INTEGRAL;
            const u = H.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        let j, Y, V, X, K, Z, J, ee, ue;
        ((q.defaultProps = { format: "integral" }),
          (function (e) {
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
          })(j || (j = {})),
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
          })(Y || (Y = {})),
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
          })(V || (V = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(X || (X = {})),
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
          })(K || (K = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(Z || (Z = {})),
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
          })(J || (J = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(ee || (ee = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(ue || (ue = {})));
        const te = [
            j.Items,
            j.Equipment,
            j.Xp,
            j.XpFactor,
            j.Blueprints,
            j.BlueprintsAny,
            j.Goodies,
            j.Berths,
            j.Slots,
            j.Tokens,
            j.CrewSkins,
            j.CrewBooks,
            j.Customizations,
            j.CreditsFactor,
            j.TankmenXp,
            j.TankmenXpFactor,
            j.FreeXpFactor,
            j.BattleToken,
            j.Entitlements,
            j.PremiumUniversal,
            j.NaturalCover,
            j.BpCoin,
            j.BattlePassSelectToken,
            j.BattlaPassFinalAchievement,
            j.BattleBadge,
            j.BonusX5,
            j.CrewBonusX3,
            j.NewYearFillers,
            j.NewYearInvoice,
            j.EpicSelectToken,
            j.Comp7TokenWeeklyReward,
            j.Comp7TokenCouponReward,
            j.BattleBoosterGift,
            j.NewYearFillers,
            j.NewYearInvoice,
            j.LootBoxToken,
            j.CosmicLootboxCommon,
            j.CosmicLootboxSilver,
            j.SelectableBonus,
            j.PostStamp,
            j.PremiumPlusUniversal,
            j.GoldenTicket,
            j.RewardsSlots,
            j.NyPetGoodies,
            j.HiddenVehicle,
            j.NyLootboxFragment,
          ],
          ne = [j.Gold, j.Credits, j.Crystal, j.FreeXp, j.NewYearToyFragments],
          ae = [j.BattlePassPoints],
          re = [j.PremiumPlus, j.Premium];
        let se;
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
        })(se || (se = {}));
        const oe = (e) =>
            te.includes(e)
              ? X.MULTI
              : ne.includes(e)
                ? X.CURRENCY
                : ae.includes(e)
                  ? X.NUMBER
                  : re.includes(e)
                    ? X.PREMIUM_PLUS
                    : X.STRING,
          ie = ["engravings", "backgrounds"],
          le = ["engraving", "background"],
          ce = (e, u = V.Small, t) => {
            const n = e.name,
              a = e.type,
              r = e.value,
              s = e.icon,
              o = e.item,
              i = e.dogTagType,
              l = ((e) => {
                switch (e) {
                  case V.S600x450:
                    return "c_600x450";
                  case V.S400x300:
                    return "c_400x300";
                  case V.S296x222:
                    return "c_296x222";
                  case V.S232x174:
                    return "c_232x174";
                  case V.Big:
                    return "c_80x80";
                  case V.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(u);
            switch (n) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${a}_${r}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_plus_${r}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}_${r}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${o}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${u}.${s}`;
              case "tokens":
              case "battleToken":
                return ((e, u) => {
                  switch (u) {
                    case V.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case V.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${u}.${e.icon}`;
                  }
                })(e, u);
              case "entitlements":
                return "big" === u
                  ? e.iconBig.replace("..", "img://gui")
                  : e.iconSmall.replace("..", "img://gui");
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${u}.${s}`;
              case "dogTagComponents":
                return ((e, u, t) => {
                  const n = ie[e];
                  if (n) {
                    const a = R.images.gui.maps.icons.dogtags.$dyn(u).$dyn(n),
                      r = a.$dyn(t);
                    return r ? `${r}` : `${a.$dyn(le[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(i, u, s);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${l}.${s}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case V.S600x450:
                      return "c_600x450";
                    case V.S400x300:
                      return "c_400x300";
                    case V.S296x222:
                      return "c_296x222";
                    case V.S232x174:
                      return "c_232x174";
                    case V.S180x135:
                      return "big";
                    case V.Big:
                    case V.S80x80:
                      return "c_80x80";
                    case V.Small:
                    case V.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(u)}.${s}`;
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
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${s}`;
              case "nyPetGoodies":
                return `R.images.new_year.gui.maps.icons.newYear.common.categoriesIcons.${u}.${s}`;
              case "nyLootboxFragment":
                return `R.images.new_year.gui.maps.icons.newYear.common.rewards.fragments.${u}.lootbox_fragment`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${l}.${s}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${u}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case V.Mini:
                      return se.s32;
                    case V.Small:
                    case V.S48x48:
                      return se.s48;
                    case V.S80x80:
                    case V.Big:
                      return se.s80;
                    case V.S128x100:
                      return se.s116;
                    case V.S180x135:
                    case V.S232x174:
                    case V.S296x222:
                      return se.s296;
                    case V.S400x300:
                      return se.s400;
                    case V.S600x450:
                      return se.s600;
                  }
                })(u)}`;
              case j.StyleProgress:
              case j.LbStyleProgress:
                return Ee(s, u, ue.ProgressionStyle);
              case "newYearAlbumsAccess":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.albumsAccess`;
              case "nyFillers":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.fillers`;
              case "nyToyFragments":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.shards`;
              case "newYearSlot":
                return `R.images.new_year.gui.maps.icons.newYear.rewards.${u}.slot`;
              case "hidden_vehicle":
                return "R.images.new_year.gui.maps.icons.newYear.common.rewards.vehicles.hidden_vehicle";
              case "nyStaticDogTag":
                return `R.images.new_year.gui.maps.icons.newYear.common.rewards.dogtags.${u}.dogtag_${t}`;
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${u}.${n}`;
            }
          },
          de = (e, u, t) => {
            const n = u && { contentId: u };
            return Object.assign(
              {
                args: e,
                isEnabled: Boolean((e && e.tooltipId) || u),
                ignoreMouseClick: !0,
                ignoreShowDelay: !u,
              },
              n,
              t,
            );
          },
          Ee = (e, u, t) => {
            const n = R.images.gui.maps.icons.quests.bonuses.$dyn(u),
              a = n.$dyn(e);
            return String(null != a ? a : n.$dyn(t));
          },
          me = "questID";
        let _e;
        !(function (e) {
          ((e.Done = "done"), (e.InProgress = "inProgress"), (e.Unavailable = "unavailable"));
        })(_e || (_e = {}));
        function Ae(e) {
          return e;
        }
        function Fe() {
          return !1;
        }
        console.log;
        var ge = t(174);
        function De(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return Be(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return Be(e, u);
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
        function Be(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        const Ce = (e) => (0 === e ? window : window.subViews.get(e));
        function pe(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        const be = pe;
        function he(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, n) => u(null == e ? void 0 : e.value, t, n));
        }
        var fe = t(946);
        let ve;
        !(function (e) {
          ((e.Scrolling = "scrolling"),
            (e.ToDone = "toDone"),
            (e.ToDoneFinished = "toDoneFinished"),
            (e.ToInProgress = "toInProgress"),
            (e.None = "none"));
        })(ve || (ve = {}));
        const we = (e) => ({ tokenID: e }),
          Se = ((e, u) => {
            const t = (0, n.createContext)({});
            return [
              function ({ mode: r = "real", options: o, children: i, mocks: l }) {
                const c = (0, n.useRef)([]),
                  d = (t, n, a) => {
                    var r;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = Ce,
                        context: n = "model",
                      } = {}) {
                        const a = new Map();
                        function r(e, u = 0) {
                          viewEnv.removeDataChangedCallback(e, u)
                            ? a.delete(e)
                            : console.error("Can't remove callback by id:", e);
                        }
                        engine.whenReady.then(() => {
                          engine.on("viewEnv.onDataChanged", (e, u, t) => {
                            t.forEach((u) => {
                              const t = a.get(u);
                              void 0 !== t && t(e);
                            });
                          });
                        });
                        const o = (e) => {
                          const a = t(u),
                            r = n.split(".").reduce((e, u) => e[u], a);
                          return "string" != typeof e || 0 === e.length
                            ? r
                            : e.split(".").reduce((e, u) => {
                                const t = e[u];
                                return "function" == typeof t ? t.bind(e) : t;
                              }, r);
                        };
                        return {
                          subscribe: (t, r) => {
                            const i = "string" == typeof r ? `${n}.${r}` : n,
                              l = s.O.view.addModelObserver(i, u, !0);
                            return (a.set(l, t), e && t(o(r)), l);
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
                            for (var e, t = De(a.keys()); !(e = t()).done;) r(e.value, u);
                          },
                          unsubscribe: r,
                        };
                      })(n),
                      i =
                        "real" === t
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (r = null == a ? void 0 : a.getter) ? r : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == a ? void 0 : a.getter(e)) : i.readByPath(e),
                      d = (e) => c.current.push(e),
                      E = e({
                        mode: t,
                        readByPath: l,
                        externalModel: i,
                        observableModel: {
                          array: (e, u) => {
                            const n = null != u ? u : l(e),
                              a = ge.LO.box(n, { equals: Fe });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, ge.aD)((e) => a.set(e)),
                                  e,
                                ),
                              a
                            );
                          },
                          object: (e, u) => {
                            const n = null != u ? u : l(e),
                              a = ge.LO.box(n, { equals: Fe });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, ge.aD)((e) => a.set(e)),
                                  e,
                                ),
                              a
                            );
                          },
                          primitives: (e, u) => {
                            const n = l(u);
                            if (Array.isArray(e)) {
                              const a = e.reduce((e, u) => ((e[u] = ge.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, ge.aD)((u) => {
                                      e.forEach((e) => {
                                        a[e].set(u[e]);
                                      });
                                    }),
                                    u,
                                  ),
                                a
                              );
                            }
                            {
                              const a = e,
                                r = Object.entries(a),
                                s = r.reduce((e, [u, t]) => ((e[t] = ge.LO.box(n[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, ge.aD)((e) => {
                                      r.forEach(([u, t]) => {
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
                        cleanup: d,
                      }),
                      m = { mode: t, model: E, externalModel: i, cleanup: d };
                    return {
                      model: E,
                      controls: "mocks" === t && a ? a.controls(m) : u(m),
                      externalModel: i,
                      mode: t,
                    };
                  },
                  E = (0, n.useRef)(!1),
                  m = (0, n.useState)(r),
                  _ = m[0],
                  A = m[1],
                  F = (0, n.useState)(() => d(r, o, l)),
                  g = F[0],
                  D = F[1];
                return (
                  (0, n.useEffect)(() => {
                    E.current ? D(d(_, o, l)) : (E.current = !0);
                  }, [l, _, o]),
                  (0, n.useEffect)(() => {
                    A(r);
                  }, [r]),
                  (0, n.useEffect)(
                    () => () => {
                      (g.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [g],
                  ),
                  a().createElement(t.Provider, { value: g }, i)
                );
              },
              () => (0, n.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = Object.assign(
                  {
                    bootcampInfo: e.primitives(["bootcampIsAvailable", "isBootcampCompleted"]),
                    progression: e.primitives(
                      ["countCompleted", "totalQuests", "lastSeenProgress", "mainRewardReceived"],
                      "questProgress",
                    ),
                    intermediateQuests: e.array("questProgress.intermediateQuests", []),
                    quests: e.array("quests", []),
                  },
                  e.primitives(["isRewardsViewOpen"]),
                ),
                t = ge.LO.box(!1),
                n = ge.LO.box(ve.None),
                a = ge.LO.box(void 0),
                r = (0, fe.Om)(() =>
                  he(u.intermediateQuests.get(), (e) =>
                    Object.assign({}, e, { rewards: he(e.rewards, Ae) }),
                  ),
                ),
                s = (0, fe.Om)(() =>
                  he(u.quests.get(), (e) => Object.assign({}, e, { rewards: he(e.rewards, Ae) })),
                ),
                o = (0, fe.Om)(() => s().length),
                i = (0, fe.Om)((e) => pe(s(), e), { equals: Fe }),
                l = (0, fe.Om)(
                  (e, u) => {
                    const t = i(e),
                      n = t
                        ? he(t.rewards, (e) => ({
                            name: e.name,
                            valueType: oe(e.name),
                            value: e.value,
                            special: e.overlayType,
                            image: ce(e, u),
                            tooltipArgs: de(
                              { tooltipId: e.tooltipId },
                              Number(e.tooltipContentId),
                              { ignoreShowDelay: !0 },
                            ),
                          }))
                        : [],
                      a = n.length > 5 ? 4 : 5;
                    return {
                      data: n,
                      count: a,
                      boxRewardTooltip: t
                        ? de(
                            { showCount: a, [me]: t.number },
                            R.views.lobby.tooltips.AdditionalRewardsTooltip("resId"),
                          )
                        : void 0,
                    };
                  },
                  { equals: Fe },
                ),
                c = (0, fe.Om)(() =>
                  (function (e, u) {
                    for (let t = e.length - 1; t >= 0; t--) if (u(be(e, t), t, e)) return t;
                  })(s(), (e) => e.state === _e.Done),
                ),
                d = (0, fe.Om)(() =>
                  (function (e, u) {
                    for (let t = 0; t < e.length; t++) if (u(be(e, t), t, e)) return t;
                  })(s(), (e) => e.state === _e.InProgress),
                ),
                E = (0, fe.Om)(() => {
                  const e = c(),
                    t = u.progression.lastSeenProgress.get();
                  return void 0 !== e && t - 1 < e;
                }),
                m = (0, fe.Om)(() => {
                  const e = d(),
                    u = c();
                  return void 0 === e ? u : e;
                }),
                _ = (0, fe.Om)((e) => {
                  const u = i(e);
                  return u ? u.maxProgress > 0 : void 0;
                });
              return Object.assign({}, u, {
                isLoaded: t,
                questSwitchAnimationPhase: n,
                lastPlayedToDoneAnimationQuestIndex: a,
                computes: {
                  getQuests: s,
                  getIntermediateQuests: r,
                  getQuestsLength: o,
                  getQuest: i,
                  getQuestRewardsProps: l,
                  getLastDoneQuestIndex: c,
                  getFirstInProgressQuestIndex: d,
                  getIsQuestSwitchAnimationNeeded: E,
                  getCurrentQuestIndex: m,
                  getIsProgressionQuest: _,
                },
              });
            },
            ({ externalModel: e, model: u }) => ({
              showView: e.createCallbackNoArgs("onShowView"),
              close: e.createCallbackNoArgs("onClose"),
              openBootcamp: e.createCallbackNoArgs("onRunBootcamp"),
              showManual: e.createCallbackNoArgs("onShowManual"),
              showMainReward: e.createCallbackNoArgs("onShowMainReward"),
              exchangeToken: e.createCallback(we, "onSelectDelayedReward"),
              loaded: (0, ge.aD)(() => u.isLoaded.set(!0)),
              setQuestSwitchAnimationPhase: (0, ge.aD)((e) => u.questSwitchAnimationPhase.set(e)),
              setLastPlayedToDoneAnimationQuestIndex: (0, ge.aD)((e) =>
                u.lastPlayedToDoneAnimationQuestIndex.set(e),
              ),
              showAnimForQuest: e.createCallback((e) => ({ [me]: e }), "onShowAnimForQuest"),
              showManualForQuest: e.createCallback((e) => ({ [me]: e }), "onShowManualForQuest"),
            }),
          ),
          Pe = Se[0],
          ye = Se[1];
        let xe;
        !(function (e) {
          ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
        })(xe || (xe = {}));
        const Re = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          Te = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          Me = (e, u, t = xe.left) => e.split(u).reduce(t === xe.left ? Re : Te, []),
          Ne = (() => {
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
          ke = ["zh_cn", "zh_sg", "zh_tw"],
          Ie = (e, u = xe.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return ke.includes(t)
              ? Ne(e)
              : ((e, u = xe.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = e.replace(/&nbsp;/g, " ");
                  return (Me(a, /( )/, u).forEach((e) => (t = t.concat(Me(e, n, xe.left)))), t);
                })(e, u);
          },
          Le = "FormatText_base_d0",
          Oe = ({ binding: e, text: u = "", classMix: t, alignment: r = xe.left }) =>
            null === u
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  n.Fragment,
                  null,
                  u.split("\n").map((u, s) =>
                    a().createElement(
                      "div",
                      { className: C()(Le, t), key: `${u}-${s}` },
                      ((e, u, t) =>
                        e
                          .split(/%\((.*?)\)(?:[sd])?/g)
                          .map((e) => (t && e in t ? t[e] : Ie(e, u))))(u, r, e).map((e, u) =>
                        a().createElement(n.Fragment, { key: `${u}-${e}` }, e),
                      ),
                    ),
                  ),
                );
        function He(e) {
          engine.call("PlaySound", e);
        }
        const Ue = {
            playHighlight() {
              He("highlight");
            },
            playClick() {
              He("play");
            },
            playYes() {
              He("yes1");
            },
          },
          Ge = {
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
        let $e, We;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })($e || ($e = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(We || (We = {})));
        const Qe = ({
          children: e,
          size: u,
          isFocused: t,
          type: r,
          disabled: s,
          mixClass: o,
          soundHover: i,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: d,
          onMouseDown: E,
          onMouseUp: m,
          onMouseLeave: _,
          onClick: A,
        }) => {
          const F = (0, n.useRef)(null),
            g = (0, n.useState)(t),
            D = g[0],
            B = g[1],
            p = (0, n.useState)(!1),
            b = p[0],
            h = p[1],
            f = (0, n.useState)(!1),
            v = f[0],
            w = f[1],
            S = (0, n.useCallback)(() => {
              s || (F.current && (F.current.focus(), B(!0)));
            }, [s]),
            P = (0, n.useCallback)(
              (e) => {
                D && null !== F.current && !F.current.contains(e.target) && B(!1);
              },
              [D],
            ),
            y = (0, n.useCallback)(
              (e) => {
                s || (A && A(e));
              },
              [s, A],
            ),
            x = (0, n.useCallback)(
              (e) => {
                s || (null !== i && He(i), c && c(e), w(!0));
              },
              [s, i, c],
            ),
            T = (0, n.useCallback)(
              (e) => {
                d && d(e);
              },
              [d],
            ),
            M = (0, n.useCallback)(
              (e) => {
                s || (m && m(e), h(!1));
              },
              [s, m],
            ),
            N = (0, n.useCallback)(
              (e) => {
                s || (null !== l && He(l), E && E(e), t && S(), h(!0));
              },
              [s, l, E, S, t],
            ),
            k = (0, n.useCallback)(
              (e) => {
                s || (_ && _(e), h(!1));
              },
              [s, _],
            ),
            I = C()(
              Ge.base,
              Ge[`base__${r}`],
              {
                [Ge.base__disabled]: s,
                [Ge[`base__${u}`]]: u,
                [Ge.base__focus]: D,
                [Ge.base__highlightActive]: b,
                [Ge.base__firstHover]: v,
              },
              o,
            ),
            L = C()(Ge.state, Ge.state__default);
          return (
            (0, n.useEffect)(
              () => (
                document.addEventListener("mousedown", P),
                () => {
                  document.removeEventListener("mousedown", P);
                }
              ),
              [P],
            ),
            (0, n.useEffect)(() => {
              B(t);
            }, [t]),
            a().createElement(
              "div",
              {
                ref: F,
                className: I,
                onMouseEnter: x,
                onMouseMove: T,
                onMouseUp: M,
                onMouseDown: N,
                onMouseLeave: k,
                onClick: y,
              },
              r !== $e.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: Ge.back }),
                  a().createElement("span", { className: Ge.texture }),
                ),
              a().createElement(
                "span",
                { className: L },
                a().createElement("span", { className: Ge.stateDisabled }),
                a().createElement("span", { className: Ge.stateHighlightHover }),
                a().createElement("span", { className: Ge.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: Ge.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Qe.defaultProps = {
          type: $e.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const ze = (0, n.memo)(Qe),
          qe = "MainReward_base_54",
          je = "MainReward_image_a5",
          Ye = "MainReward_received_f6",
          Ve = "MainReward_receivedText_59",
          Xe = "MainReward_checkMarkWrapper_b9",
          Ke = "MainReward_checkMark_87",
          Ze = "MainReward_back_dc",
          Je = "MainReward_button_0f",
          eu = R.strings.battle_matters.mainScreen,
          uu = (0, $.Pi)(() => {
            const e = ye(),
              u = e.controls,
              t = e.model;
            return a().createElement(
              "div",
              { className: qe },
              a().createElement("div", { className: je }),
              t.progression.mainRewardReceived.get()
                ? a().createElement(
                    "div",
                    { className: Ye },
                    a().createElement(
                      "div",
                      { className: Xe },
                      a().createElement("div", { className: Ze }),
                      a().createElement("div", { className: Ke }),
                    ),
                    a().createElement("div", { className: Ve }, eu.mainRewardReceived()),
                  )
                : a().createElement(
                    ze,
                    { mixClass: Je, size: We.medium, type: $e.ghost, onClick: u.showMainReward },
                    eu.showMainReward(),
                  ),
            );
          }),
          tu = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let nu, au;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(nu || (nu = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(au || (au = {})));
        const ru = ({ size: e = nu.Default, classMix: u }) =>
            a().createElement("div", { className: C()(tu.background, tu[`background__${e}`], u) }),
          su = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          ou = ({ size: e }) => {
            const u = C()(su.base, su[`base__${e}`]);
            return a().createElement("div", { className: u });
          },
          iu = {
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
          lu = (0, n.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: n,
              isComplete: r,
              withoutBounce: s,
            }) => {
              const o = C()(
                  iu.base,
                  iu[`base__${e}`],
                  t && iu.base__disabled,
                  r && iu.base__finished,
                  s && iu.base__withoutBounce,
                ),
                i = !t && !r;
              return a().createElement(
                "div",
                { className: o, style: n, ref: u },
                a().createElement("div", { className: iu.pattern }),
                a().createElement("div", { className: iu.gradient }),
                i && a().createElement(ou, { size: e }),
              );
            },
          ),
          cu = ({ size: e, value: u, lineRef: t, disabled: r, onComplete: s }) => {
            const o = (0, n.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              i = 100 === u;
            return (
              (0, n.useEffect)(() => {
                i && s && s();
              }, [i, s]),
              a().createElement(lu, {
                size: e,
                disabled: r,
                baseStyles: o,
                isComplete: i,
                lineRef: t,
              })
            );
          },
          du = (e, u) => {
            let t;
            const n = setTimeout(() => {
              t = e();
            }, u);
            return () => {
              ("function" == typeof t && t(), clearTimeout(n));
            };
          };
        let Eu, mu;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(Eu || (Eu = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(mu || (mu = {})));
        const _u = "ProgressBarDeltaSimple_base_6c",
          Au = "ProgressBarDeltaSimple_delta_99",
          Fu = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: s,
              to: o,
              onEndAnimation: i,
              onChangeAnimationState: l,
            }) => {
              const c = o < r,
                d = (0, n.useState)(mu.Idle),
                E = d[0],
                m = d[1],
                _ = E === mu.In,
                A = E === mu.End,
                F = E === mu.Idle,
                g = (0, n.useCallback)(
                  (e) => {
                    (m(e), l && l(e));
                  },
                  [l],
                );
              ((0, n.useEffect)(() => {
                if (F && !t) {
                  return du(() => {
                    g(mu.In);
                  }, u);
                }
              }, [g, t, F, u]),
                (0, n.useEffect)(() => {
                  if (_) {
                    return du(() => {
                      (i && i(), g(mu.End));
                    }, e + u);
                  }
                }, [g, _, i, u, e]));
              const D = (0, n.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, u, e],
                ),
                B = (0, n.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, u, e],
                ),
                C = (0, n.useMemo)(
                  () => ({ width: `${Math.abs(r - o)}%`, left: `${c ? o : r}%` }),
                  [r, c, o],
                );
              return A
                ? null
                : a().createElement(
                    "div",
                    { className: _u, style: C },
                    a().createElement(
                      "div",
                      { style: F ? D : B, className: Au },
                      a().createElement(ou, { size: s }),
                    ),
                  );
            },
          ),
          gu = (0, n.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: s,
              isComplete: o,
              animationSettings: i,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const d = (0, n.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${i.line.duration}ms`,
                  transitionDelay: `${i.line.delay}ms`,
                }),
                [i.line.delay, i.line.duration, e],
              );
              return a().createElement(
                a().Fragment,
                null,
                a().createElement(lu, {
                  size: u,
                  lineRef: r,
                  disabled: s,
                  isComplete: o,
                  baseStyles: d,
                }),
                t >= 0 &&
                  a().createElement(Fu, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    freezed: i.freezed,
                    from: t,
                    size: u,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          Du = "ProgressBarDeltaGrow_base_7e",
          Bu = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          Cu = "ProgressBarDeltaGrow_glow_68",
          pu = (e) => (e ? { left: 0 } : { right: 0 }),
          bu = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          hu = (e) => ({ transitionDuration: `${e}ms` }),
          fu = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: r,
              size: s,
              to: o,
              onEndAnimation: i,
              onChangeAnimationState: l,
              className: c,
            }) => {
              const d = o < r,
                E = (0, n.useState)(Eu.Idle),
                m = E[0],
                _ = E[1],
                A = m === Eu.End,
                F = m === Eu.Idle,
                g = m === Eu.Grow,
                D = m === Eu.Shrink,
                B = (0, n.useCallback)(
                  (e) => {
                    (_(e), l && l(e));
                  },
                  [l],
                ),
                p = (0, n.useCallback)(
                  (e, u) =>
                    du(() => {
                      B(e);
                    }, u),
                  [B],
                );
              (0, n.useEffect)(() => {
                if (!t)
                  return F
                    ? p(Eu.Grow, u)
                    : g
                      ? p(Eu.Shrink, e)
                      : D
                        ? p(Eu.End, e)
                        : void (A && i && i());
              }, [p, t, A, g, F, D, i, u, e]);
              const b = (0, n.useMemo)(
                  () => Object.assign({ width: "100%" }, hu(e), pu(d)),
                  [d, e],
                ),
                h = (0, n.useMemo)(() => Object.assign({ width: "0%" }, hu(e), pu(d)), [d, e]),
                f = (0, n.useMemo)(
                  () => Object.assign({ width: "0%" }, bu(d, r), hu(e)),
                  [r, d, e],
                ),
                v = (0, n.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - r)}%` }, bu(d, r), hu(e)),
                  [r, d, o, e],
                );
              if (A) return null;
              const w = C()(Du, c, d && 0 === o && Bu);
              return a().createElement(
                "div",
                { style: F ? f : v, className: w },
                a().createElement(
                  "div",
                  { style: D ? h : b, className: Cu },
                  a().createElement(ou, { size: s }),
                ),
              );
            },
          ),
          vu = (0, n.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: r,
              disabled: s,
              isComplete: o,
              animationSettings: i,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const d = e < t,
                E = (0, n.useState)(!1),
                m = E[0],
                _ = E[1],
                A = (0, n.useCallback)(
                  (e) => {
                    (e === Eu.Shrink && _(!0), c && c(e));
                  },
                  [c],
                ),
                F = (0, n.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                g = (0, n.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${i.line.duration}ms` }),
                  [i.line.duration, e],
                );
              return a().createElement(
                a().Fragment,
                null,
                a().createElement(lu, {
                  size: u,
                  lineRef: r,
                  disabled: s,
                  isComplete: o,
                  withoutBounce: d && 0 === e,
                  baseStyles: m ? g : F,
                }),
                t >= 0 &&
                  a().createElement(fu, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    onChangeAnimationState: A,
                    freezed: i.freezed,
                    onEndAnimation: l,
                    from: t,
                    size: u,
                    to: e,
                    className: i.delta.className,
                  }),
              );
            },
          ),
          wu = ["onComplete", "onEndAnimation"];
        function Su() {
          return (
            (Su =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Su.apply(this, arguments)
          );
        }
        const Pu = (0, n.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              r = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, wu);
            const s = (0, n.useState)(!1),
              o = s[0],
              i = s[1],
              l = (0, n.useCallback)(() => {
                const e = 100 === r.to;
                (e !== o && i(e), e && u && u(), t && t());
              }, [o, u, t, r.to]);
            switch (r.animationSettings.type) {
              case au.Simple:
                return a().createElement(gu, Su({}, r, { onEndAnimation: l, isComplete: o }));
              case au.Growing:
                return a().createElement(vu, Su({}, r, { onEndAnimation: l, isComplete: o }));
              default:
                return null;
            }
          }),
          yu = ["onEndAnimation"];
        function xu() {
          return (
            (xu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            xu.apply(this, arguments)
          );
        }
        const Ru = (0, n.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
              return a;
            })(e, yu);
          const r = (0, n.useRef)({}),
            s = (0, n.useCallback)(() => {
              ((r.current.from = void 0), u && u());
            }, [u]),
            o = "number" == typeof r.current.from ? r.current.from : t.from;
          return (
            (r.current.from = o),
            a().createElement(Pu, xu({}, t, { onEndAnimation: s, key: `${o}-${t.to}`, from: o }))
          );
        });
        function Tu() {
          return (
            (Tu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Tu.apply(this, arguments)
          );
        }
        const Mu = (0, n.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: n,
              deltaFrom: r,
              animationSettings: s,
              onEndAnimation: o,
              onChangeAnimationState: i,
              onComplete: l,
            }) => {
              if (r === u)
                return a().createElement(cu, {
                  key: `${r}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: n,
                  onComplete: l,
                });
              const c = {
                from: r,
                to: u,
                size: e,
                lineRef: t,
                disabled: n,
                animationSettings: s,
                onComplete: l,
                onEndAnimation: o,
                onChangeAnimationState: i,
              };
              return s.withStack
                ? a().createElement(Ru, c)
                : a().createElement(Pu, Tu({ key: `${r}-${u}` }, c));
            },
          ),
          Nu = (e) => ({
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
          ku = (e, u, t) => (t < e ? e : t > u ? u : t),
          Iu = (e, u, t) => {
            if ("number" == typeof t) {
              return (ku(0, u, t) / u) * 100;
            }
            return e;
          },
          Lu = {
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
          Ou = {
            freezed: !1,
            withStack: !1,
            type: au.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          Hu = (0, n.memo)(
            ({
              maxValue: e = 100,
              theme: u = Lu,
              size: t = nu.Default,
              animationSettings: r = Ou,
              disabled: s = !1,
              withoutBackground: o = !1,
              progressBarBackgroundClassMix: i,
              value: l,
              deltaFrom: c,
              lineRef: d,
              onChangeAnimationState: E,
              onEndAnimation: m,
              onComplete: _,
            }) => {
              const A = ((e, u, t) =>
                (0, n.useMemo)(() => {
                  const n = (ku(0, u, e) / u) * 100;
                  return { value: n, deltaFrom: Iu(n, u, t) };
                }, [t, u, e]))(l, e, c);
              return a().createElement(
                "div",
                { className: C()(tu.base, tu[`base__${t}`]), style: Nu(u) },
                !o && a().createElement(ru, { size: t, classMix: i }),
                a().createElement(Mu, {
                  size: t,
                  lineRef: d,
                  disabled: s,
                  value: A.value,
                  deltaFrom: A.deltaFrom,
                  animationSettings: r,
                  onEndAnimation: m,
                  onChangeAnimationState: E,
                  onComplete: _,
                }),
              );
            },
          ),
          Uu = {
            base: "IntermediateQuest_base_5b",
            base__last: "IntermediateQuest_base__last_12",
            questNumber: "IntermediateQuest_questNumber_29",
            base__currentCompleted: "IntermediateQuest_base__currentCompleted_82",
            base__allCompleted: "IntermediateQuest_base__allCompleted_c9",
            serif: "IntermediateQuest_serif_73",
            serif__top: "IntermediateQuest_serif__top_88",
            serif__bottom: "IntermediateQuest_serif__bottom_1e",
            rewards: "IntermediateQuest_rewards_38",
          };
        let Gu;
        !(function (e) {
          ((e.Regular = "regular"),
            (e.CurrentCompleted = "currentCompleted"),
            (e.AllCompleted = "allCompleted"));
        })(Gu || (Gu = {}));
        const $u = ({ children: e, questNumber: u, questsCount: t, state: n, zIndex: r }) => {
            const s = { left: `${(100 * u) / t}%`, zIndex: r };
            return a().createElement(
              "div",
              { className: C()(Uu.base, Uu[`base__${n}`], u === t && Uu.base__last), style: s },
              a().createElement("div", { className: Uu.questNumber }, u),
              a().createElement("div", { className: C()(Uu.serif, Uu.serif__top) }),
              a().createElement("div", { className: C()(Uu.serif, Uu.serif__bottom) }),
              a().createElement("div", { className: Uu.rewards }, e),
            );
          },
          Wu = [
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
        function Qu(e) {
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
        const zu = (e, u, t = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: H.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: n,
                },
                t,
              ),
            );
          },
          qu = (e) => {
            let u = e.children,
              t = e.contentId,
              a = e.args,
              r = e.onMouseEnter,
              s = e.onMouseLeave,
              o = e.onMouseDown,
              i = e.onClick,
              l = e.ignoreShowDelay,
              c = void 0 !== l && l,
              d = e.ignoreMouseClick,
              E = void 0 !== d && d,
              m = e.decoratorId,
              _ = void 0 === m ? 0 : m,
              A = e.isEnabled,
              F = void 0 === A || A,
              g = e.targetId,
              D = void 0 === g ? 0 : g,
              B = e.onShow,
              C = e.onHide,
              p = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, Wu);
            const b = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              h = (0, n.useMemo)(
                () =>
                  D ||
                  ((e = 1) => {
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
                  })().resId,
                [D],
              ),
              f = (0, n.useCallback)(() => {
                (b.current.isVisible && b.current.timeoutId) ||
                  (zu(t, _, { isMouseEvent: !0, on: !0, arguments: Qu(a) }, h),
                  B && B(),
                  (b.current.isVisible = !0));
              }, [t, _, a, h, B]),
              v = (0, n.useCallback)(() => {
                if (b.current.isVisible || b.current.timeoutId) {
                  const e = b.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (b.current.timeoutId = 0)),
                    zu(t, _, { on: !1 }, h),
                    b.current.isVisible && C && C(),
                    (b.current.isVisible = !1));
                }
              }, [t, _, h, C]),
              w = (0, n.useCallback)((e) => {
                b.current.isVisible &&
                  ((b.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (b.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(b.current.prevTarget) && v();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const e = b.current.hideTimerId;
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
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((b.current.timeoutId = window.setTimeout(f, c ? 100 : 400)),
                            r && r(e),
                            S && S(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (v(), null == s || s(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === E && v(), null == i || i(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === E && v(), null == o || o(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    p,
                  ),
                )
              : u;
            var S;
          },
          ju = ["children"];
        function Yu() {
          return (
            (Yu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Yu.apply(this, arguments)
          );
        }
        const Vu = (e) => {
            let u = e.children,
              t = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, ju);
            return a().createElement(
              qu,
              Yu(
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
          Xu = ["children", "body", "header", "note", "alert", "args"];
        function Ku() {
          return (
            (Ku =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Ku.apply(this, arguments)
          );
        }
        const Zu = R.views.common.tooltip_window.simple_tooltip_content,
          Ju = (e) => {
            let u = e.children,
              t = e.body,
              r = e.header,
              s = e.note,
              o = e.alert,
              i = e.args,
              l = (function (e, u) {
                if (null == e) return {};
                var t,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                return a;
              })(e, Xu);
            const c = (0, n.useMemo)(() => {
              const e = Object.assign({}, i, { body: t, header: r, note: s, alert: o });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [o, t, r, s, i]);
            return a().createElement(
              qu,
              Ku(
                {
                  contentId:
                    ((d = null == i ? void 0 : i.hasHtmlContent),
                    d ? Zu.SimpleTooltipHtmlContent("resId") : Zu.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: c,
                },
                l,
              ),
              u,
            );
            var d;
          };
        function et() {
          return (
            (et =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            et.apply(this, arguments)
          );
        }
        const ut = ({ children: e, tooltipArgs: u, className: t }) => {
            if (!u) return e;
            const n = a().createElement("div", { className: t }, e);
            if (u.header || u.body) return a().createElement(Ju, u, n);
            const r = u.contentId,
              s = u.args,
              o = null == s ? void 0 : s.contentId;
            return r || o
              ? a().createElement(qu, et({}, u, { contentId: r || o }), n)
              : a().createElement(Vu, u, n);
          },
          tt = {
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
          nt = ({
            name: e,
            image: u,
            isPeriodic: t = !1,
            size: n = V.Big,
            special: r,
            value: s,
            valueType: o,
            style: i,
            className: l,
            classNames: c,
            tooltipArgs: d,
            periodicIconTooltipArgs: E,
          }) => {
            const m = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case K.BATTLE_BOOSTER:
                  case K.BATTLE_BOOSTER_REPLACE:
                    return Z.BATTLE_BOOSTER;
                }
              })(r),
              _ = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case K.BATTLE_BOOSTER:
                    return J.BATTLE_BOOSTER;
                  case K.BATTLE_BOOSTER_REPLACE:
                    return J.BATTLE_BOOSTER_REPLACE;
                  case K.BUILT_IN_EQUIPMENT:
                    return J.BUILT_IN_EQUIPMENT;
                  case K.EQUIPMENT_PLUS:
                    return J.EQUIPMENT_PLUS;
                  case K.EQUIPMENT_TROPHY_BASIC:
                    return J.EQUIPMENT_TROPHY_BASIC;
                  case K.EQUIPMENT_TROPHY_UPGRADED:
                    return J.EQUIPMENT_TROPHY_UPGRADED;
                  case K.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return J.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case K.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return J.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case K.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return J.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case K.PROGRESSION_STYLE_UPGRADED_1:
                    return J.PROGRESSION_STYLE_UPGRADED_1;
                  case K.PROGRESSION_STYLE_UPGRADED_2:
                    return J.PROGRESSION_STYLE_UPGRADED_2;
                  case K.PROGRESSION_STYLE_UPGRADED_3:
                    return J.PROGRESSION_STYLE_UPGRADED_3;
                  case K.PROGRESSION_STYLE_UPGRADED_4:
                    return J.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(r),
              A = ((e, u) => {
                if (void 0 === e) return null;
                switch (u) {
                  case X.MULTI: {
                    const u = Number(e);
                    return isFinite(u) && u > 1 ? `x${Math.floor(u)}` : null;
                  }
                  case X.CURRENCY:
                  case X.NUMBER:
                    return a().createElement(q, { format: "integral", value: Number(e) });
                  case X.PREMIUM_PLUS: {
                    const u = Number(e);
                    return isNaN(u) ? e : null;
                  }
                  default:
                    return e;
                }
              })(s, o);
            return a().createElement(
              "div",
              { className: C()(tt.base, tt[`base__${n}`], l), style: i },
              a().createElement(
                ut,
                { tooltipArgs: d, className: tt.tooltipWrapper },
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement(
                    "div",
                    { className: C()(tt.image, null == c ? void 0 : c.image) },
                    m &&
                      a().createElement("div", {
                        className: C()(tt.highlight, null == c ? void 0 : c.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${m}_highlight)`,
                        },
                      }),
                    u &&
                      a().createElement("div", {
                        className: C()(tt.icon, null == c ? void 0 : c.rewardIcon),
                        style: { backgroundImage: `url(${u})` },
                      }),
                    _ &&
                      a().createElement("div", {
                        className: C()(tt.overlay, null == c ? void 0 : c.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${n}.${_}_overlay)`,
                        },
                      }),
                  ),
                  A &&
                    a().createElement(
                      "div",
                      {
                        className: C()(
                          tt.info,
                          tt[`info__${e}`],
                          o === X.MULTI && tt.info__multi,
                          null == c ? void 0 : c.info,
                        ),
                      },
                      A,
                    ),
                ),
              ),
              t &&
                a().createElement(
                  ut,
                  { tooltipArgs: E },
                  a().createElement("div", {
                    className: C()(tt.timer, null == c ? void 0 : c.periodicIcon),
                  }),
                ),
            );
          };
        var at = t(30);
        const rt = "TokenReward_base_db",
          st = "TokenReward_lightContainer_44",
          ot = "TokenReward_light_14",
          it = "TokenReward_button_66",
          lt = (e) => Math.sqrt(1 - Math.pow(e - 1, 2)),
          ct = (0, $.Pi)(({ isReceived: e, value: u, level: t }) => {
            const n = ye().controls,
              r = (0, at.useSpring)({ opacity: e ? 1 : 0, config: { duration: 300, easing: lt } }),
              s = (0, at.useTransition)(e, {
                initial: { opacity: 1, transform: "translateY(12rem)" },
                from: { opacity: 0, transform: "translateY(22rem)" },
                enter: { opacity: 1, transform: "translateY(12rem)" },
                config: { duration: 300, easing: lt },
              }),
              o = `url(R.images.gui.maps.icons.battleMatters.common.tokens.c_48x48.level_${t})`,
              i = { rewardToken: u };
            return a().createElement(
              qu,
              {
                contentId:
                  R.views.lobby.battle_matters.tooltips.BattleMattersTokenTooltipView("resId"),
                args: i,
              },
              a().createElement(
                "div",
                { className: rt, style: { backgroundImage: o } },
                a().createElement(
                  at.animated.div,
                  { style: r, className: st },
                  a().createElement("div", { className: ot }),
                ),
                s(
                  (e, t) =>
                    t &&
                    a().createElement(
                      at.animated.div,
                      { style: e },
                      a().createElement(
                        ze,
                        {
                          mixClass: it,
                          size: We.small,
                          type: $e.main,
                          onClick: () => n.exchangeToken(u),
                        },
                        R.strings.battle_matters.mainScreen.exchangeToken(),
                      ),
                    ),
                ),
              ),
            );
          }),
          dt = "VehicleReward_base_98",
          Et = "VehicleReward_mark_ad",
          mt = ({ icon: e, tooltipArgs: u }) => {
            return a().createElement(
              ut,
              { tooltipArgs: u },
              a().createElement(
                "div",
                {
                  style: {
                    backgroundImage: `url('R.images.gui.maps.icons.vehicle.${((t = e), t.replace(/-/g, "_"))}')`,
                  },
                  className: dt,
                },
                a().createElement("div", { className: Et }),
              ),
            );
            var t;
          },
          _t = (e) => de({ tooltipId: e.tooltipId }, Number(e.tooltipContentId)),
          At = (0, $.Pi)(({ reward: e, isReceived: u }) => {
            switch (e.name) {
              case "token":
                return a().createElement(ct, {
                  isReceived: u,
                  value: e.value,
                  level: Number(e.label),
                });
              case "vehicle":
                return a().createElement(mt, { icon: e.icon, tooltipArgs: _t(e) });
              default:
                return a().createElement(nt, {
                  name: e.name,
                  image: ce(e),
                  size: V.Small,
                  value: e.value,
                  valueType: oe(e.name),
                  tooltipArgs: _t(e),
                });
            }
          }),
          Ft = (0, $.Pi)(
            ({ isReceived: e, state: u, questsCount: t, questNumber: n, rewards: r }) =>
              a().createElement(
                $u,
                {
                  questNumber: n,
                  questsCount: t,
                  state: u,
                  zIndex: ((e) => (-1 !== e.findIndex((e) => "token" === e.name) ? 2 : 1))(r),
                },
                r
                  .filter((e) => e.name)
                  .map((u, t) => a().createElement(At, { key: t, reward: u, isReceived: e })),
              ),
          ),
          gt = (e, u, t) => (u === t ? Gu.AllCompleted : u >= e ? Gu.CurrentCompleted : Gu.Regular),
          Dt = Object.assign({}, Ou, {
            line: { delay: 0, duration: 800 },
            delta: { delay: 0, duration: 800 },
          }),
          Bt = (0, $.Pi)(({ progressToShow: e }) => {
            const u = ye().model,
              t = u.progression.countCompleted.get(),
              r = t - 1,
              s = u.progression.totalQuests.get(),
              o = u.computes.getIntermediateQuests(),
              i = u.computes.getIsQuestSwitchAnimationNeeded(),
              l = u.isRewardsViewOpen.get(),
              c = (0, n.useState)(i ? r : void 0),
              d = c[0],
              E = c[1],
              m = (0, n.useState)(i ? r : t),
              _ = m[0],
              A = m[1];
            ((0, n.useEffect)(() => {
              A(i ? r : t);
            }, [i, r, t]),
              (0, n.useEffect)(() => {
                if (void 0 !== d && d < e)
                  return du(() => He(R.sounds.bp_progress_bar_start()), 500);
              }, [d, e]),
              (0, n.useEffect)(() => {
                E(i && !l && _ < t ? r : void 0);
              }, [l, i, r, _, t]));
            const F = (0, n.useCallback)(() => {
              A(e);
            }, [e]);
            return a().createElement(
              a().Fragment,
              null,
              a().createElement(Hu, {
                value: e,
                deltaFrom: d,
                maxValue: s,
                onEndAnimation: F,
                animationSettings: Dt,
              }),
              o.map((e) =>
                a().createElement(Ft, {
                  key: e.questIdx,
                  questNumber: e.questIdx,
                  questsCount: s,
                  rewards: e.rewards,
                  state: gt(e.questIdx, _, s),
                  isReceived: e.questIdx <= _,
                }),
              ),
              a().createElement($u, { questNumber: s, questsCount: s, state: gt(s, _, s) }),
            );
          }),
          Ct = "Footer_base_2b",
          pt = "Footer_content_75",
          bt = "Footer_progress_84",
          ht = "Footer_title_51",
          ft = "Footer_completedQuests_1f",
          vt = "Footer_completedQuests__allCompleted_b3",
          wt = "Footer_subTitle_e9",
          St = "Footer_progression_00",
          Pt = R.strings.battle_matters.mainScreen,
          yt = (0, $.Pi)(() => {
            const e = ye().model,
              u = e.progression.countCompleted.get(),
              t = u - 1,
              r = e.progression.totalQuests.get(),
              s = e.computes.getIsQuestSwitchAnimationNeeded(),
              o = e.questSwitchAnimationPhase.get(),
              i = (0, n.useState)(s ? t : u),
              l = i[0],
              c = i[1];
            return (
              (0, n.useEffect)(() => {
                o === ve.ToDoneFinished && c(u);
              }, [u, o]),
              (0, n.useEffect)(() => {
                c(s ? t : u);
              }, [t, u, s]),
              a().createElement(
                "div",
                { className: Ct },
                a().createElement(
                  "div",
                  { className: pt },
                  a().createElement(
                    "div",
                    { className: bt },
                    a().createElement(
                      "div",
                      { className: ht },
                      a().createElement(Oe, {
                        text: Pt.progress(),
                        binding: {
                          completed: a().createElement(
                            "span",
                            { className: C()(ft, l === r && vt) },
                            l,
                          ),
                          total: r,
                        },
                      }),
                    ),
                    a().createElement("div", { className: wt }, Pt.target()),
                    a().createElement(
                      "div",
                      { className: St },
                      a().createElement(Bt, { progressToShow: l }),
                    ),
                  ),
                  a().createElement(uu, null),
                ),
              )
            );
          }),
          xt = {
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
          Rt = [
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
        function Tt() {
          return (
            (Tt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            Tt.apply(this, arguments)
          );
        }
        class Mt extends a().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && He(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && He(this.props.soundClick));
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
              s = e.type,
              o = e.classNames,
              i = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              d = e.onMouseUp,
              E =
                (e.soundClick,
                e.soundHover,
                (function (e, u) {
                  if (null == e) return {};
                  var t,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((t = r[n]), u.indexOf(t) >= 0 || (a[t] = e[t]));
                  return a;
                })(e, Rt)),
              m = C()(xt.base, xt[`base__${s}`], xt[`base__${r}`], null == o ? void 0 : o.base),
              _ = C()(xt.icon, xt[`icon__${s}`], xt[`icon__${r}`], null == o ? void 0 : o.icon),
              A = C()(xt.glow, null == o ? void 0 : o.glow),
              F = C()(xt.caption, xt[`caption__${s}`], null == o ? void 0 : o.caption),
              g = C()(xt.goto, null == o ? void 0 : o.goto);
            return a().createElement(
              "div",
              Tt(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                E,
              ),
              "info" !== s && a().createElement("div", { className: xt.shine }),
              a().createElement(
                "div",
                { className: _ },
                a().createElement("div", { className: A }),
              ),
              a().createElement("div", { className: F }, u),
              n && a().createElement("div", { className: g }, n),
            );
          }
        }
        Mt.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const Nt = "BootcampButton_base_9e",
          kt = "BootcampButton_borderGradient_fd",
          It = "BootcampButton_borderGradient__top_40",
          Lt = "BootcampButton_borderGradient__bottom_97",
          Ot = "BootcampButton_splash_88",
          Ht = "BootcampButton_animatedShine_6e",
          Ut = "BootcampButton_clip_ea",
          Gt = "BootcampButton_back_03",
          $t = "BootcampButton_back__hover_44",
          Wt = "BootcampButton_content_ab",
          Qt = "BootcampButton_icon_ad",
          zt = "BootcampButton_text_3a",
          qt = "BootcampButton_buttonGlow_7c",
          jt = "BootcampButton_buttonGlow__hover_e1",
          Yt = R.strings.battle_matters.mainScreen.bootcampButtonTooltip,
          Vt = ({ onClick: e }) =>
            a().createElement(
              Ju,
              { header: Yt.header(), body: Yt.body() },
              a().createElement(
                "div",
                {
                  className: Nt,
                  onClick: () => {
                    (Ue.playClick(), e());
                  },
                  onMouseEnter: () => {
                    Ue.playHighlight();
                  },
                },
                a().createElement("div", { className: Gt }),
                a().createElement("div", { className: C()(Gt, $t) }),
                a().createElement(
                  "div",
                  { className: Ut },
                  a().createElement("div", { className: Ot }),
                  a().createElement("div", { className: Ht }),
                ),
                a().createElement("div", { className: qt }),
                a().createElement("div", { className: C()(qt, jt) }),
                a().createElement(
                  "div",
                  { className: Wt },
                  a().createElement("span", { className: Qt }),
                  a().createElement(
                    "span",
                    { className: zt },
                    R.strings.battle_matters.mainScreen.bootcampButton(),
                  ),
                ),
                a().createElement("div", { className: C()(kt, It) }),
                a().createElement("div", { className: C()(kt, Lt) }),
              ),
            ),
          Xt = "Header_base_5d",
          Kt = "Header_infoBtn_1e",
          Zt = "Header_infoBtnIcon_51",
          Jt = "Header_infoBtnGlow_54",
          en = "Header_bootcampBtn_bb",
          un = "Header_title_d2",
          tn = R.strings.battle_matters.mainScreen,
          nn = (0, $.Pi)(() => {
            const e = ye(),
              u = e.model,
              t = e.controls,
              n = w().mediaSize;
            return a().createElement(
              "div",
              { className: Xt },
              a().createElement(Mt, {
                caption: n === h.ExtraSmall ? tn.infoButtonSmall() : tn.infoButton(),
                type: "info",
                classNames: { base: Kt, icon: Zt, glow: Jt },
                onClick: t.showManual,
              }),
              a().createElement("span", { className: un }, tn.title()),
              u.bootcampInfo.bootcampIsAvailable.get() &&
                !u.bootcampInfo.isBootcampCompleted.get() &&
                a().createElement(
                  "div",
                  { className: en },
                  a().createElement(Vt, { onClick: t.openBootcamp }),
                ),
            );
          }),
          an = (e) => {
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
          rn = [];
        function sn(e) {
          const u = (0, n.useRef)(e);
          return (
            (0, n.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, n.useCallback)((...e) => (0, u.current)(...e), rn)
          );
        }
        function on(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return ln(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return ln(e, u);
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
        function ln(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, n = new Array(u); t < u; t++) n[t] = e[t];
          return n;
        }
        function cn(e, u, t) {
          const a = (0, n.useMemo)(
            () =>
              (function (e, u, t, n) {
                let a,
                  r = !1,
                  s = 0;
                function o() {
                  a && clearTimeout(a);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - s;
                  function d() {
                    ((s = Date.now()), t.apply(l, i));
                  }
                  r ||
                    (n && !a && d(),
                    o(),
                    void 0 === n && c > e
                      ? d()
                      : !0 !== u &&
                        (a = setTimeout(
                          n
                            ? function () {
                                a = void 0;
                              }
                            : d,
                          void 0 === n ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof u && ((n = t), (t = u), (u = void 0)),
                  (i.cancel = function () {
                    (o(), (r = !0));
                  }),
                  i
                );
              })(t, e),
            u,
          );
          return ((0, n.useEffect)(() => a.cancel, [a]), a);
        }
        let dn;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(dn || (dn = {}));
        const En = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          mn = (({
            getContainerSize: e,
            getBounds: u,
            setScrollPosition: t,
            getDirection: a,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: o = !1,
          }) => {
            const i = (e, t) => {
              const n = u(e),
                a = n[0],
                r = n[1];
              return ku(a, r, t);
            };
            return (l = {}) => {
              const c = l.settings,
                d = void 0 === c ? En : c,
                E = (0, n.useRef)(null),
                m = (0, n.useRef)(null),
                _ = (() => {
                  const e = (0, n.useMemo)(() => ({}), []),
                    u = (u) => (e[u] || (e[u] = new Map()), e[u]),
                    t = (e, t) => {
                      u(e).set(t, t);
                    },
                    a = (e, t) => {
                      u(e).delete(t);
                    },
                    r = (e, ...t) => {
                      for (var n, a = on(u(e).values()); !(n = a()).done;) (0, n.value)(...t);
                    };
                  return (0, n.useMemo)(() => ({ on: t, off: a, trigger: r }), []);
                })(),
                A = cn(
                  () => {
                    s.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                F = (0, at.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const u = E.current;
                    u && (t(u, e), _.trigger("change", e), o && A());
                  },
                  onRest: (e) => _.trigger("rest", e),
                  onStart: (e) => _.trigger("start", e),
                  onPause: (e) => _.trigger("pause", e),
                })),
                g = F[0],
                D = F[1],
                B = (0, n.useCallback)(
                  (e, u, t) => {
                    var n;
                    const a = g.scrollPosition.get(),
                      r = (null != (n = g.scrollPosition.goal) ? n : 0) - a;
                    return i(e, u * t + r + a);
                  },
                  [g.scrollPosition],
                ),
                C = (0, n.useCallback)(
                  (e, { immediate: u = !1, reset: t = !0 } = {}) => {
                    const n = E.current;
                    n &&
                      D.start({
                        scrollPosition: i(n, e),
                        immediate: u,
                        reset: t,
                        config: d.animationConfig,
                        from: { scrollPosition: i(n, g.scrollPosition.get()) },
                      });
                  },
                  [D, d.animationConfig, g.scrollPosition],
                ),
                p = (0, n.useCallback)(
                  (e) => {
                    const u = E.current,
                      t = m.current;
                    if (!u || !t) return;
                    const n = ((e, u) => {
                        switch (u.type) {
                          case "proportional":
                            return r(e) / u.factor;
                          case "fixed":
                            return u.value;
                        }
                      })(t, d.step),
                      a = B(u, e, n);
                    C(a);
                  },
                  [C, B, d.step],
                ),
                b = (0, n.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && p(a(e)),
                      E.current && _.trigger("mouseWheel", e, g.scrollPosition, u(E.current)));
                  },
                  [g.scrollPosition, p, _],
                ),
                h = ((e, u = []) => {
                  const t = (0, n.useRef)(),
                    a = (0, n.useCallback)((...u) => {
                      (t.current && t.current(), (t.current = e(...u)));
                    }, u);
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
                    an(() => {
                      const e = E.current;
                      e &&
                        (C(i(e, g.scrollPosition.goal), { immediate: !0 }),
                        _.trigger("resizeHandled"));
                    }),
                  [C, g.scrollPosition.goal],
                ),
                f = sn(() => {
                  const e = E.current;
                  if (!e) return;
                  const u = i(e, g.scrollPosition.goal);
                  (u !== g.scrollPosition.goal && C(u, { immediate: !0 }),
                    _.trigger("recalculateContent"));
                });
              (0, n.useEffect)(
                () => (
                  window.addEventListener("resize", h),
                  () => {
                    window.removeEventListener("resize", h);
                  }
                ),
                [h],
              );
              const v = (0, n.useCallback)((e) => _.trigger("isThumbDraggingChanged", e), [_]);
              return (0, n.useMemo)(
                () => ({
                  getWrapperSize: () => (m.current ? r(m.current) : void 0),
                  getContainerSize: () => (E.current ? e(E.current) : void 0),
                  getBounds: () =>
                    E.current
                      ? u(E.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: d.step.clampedArrowStepTimeout,
                  clampPosition: i,
                  handleMouseWheel: b,
                  applyScroll: C,
                  applyStepTo: p,
                  contentRef: E,
                  wrapperRef: m,
                  scrollPosition: D,
                  animationScroll: g,
                  recalculateContent: f,
                  handleIsThumbDragging: v,
                  events: { on: _.on, off: _.off },
                }),
                [g.scrollPosition, C, p, v, _.off, _.on, f, b, D, d.step.clampedArrowStepTimeout],
              );
            };
          })({
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
            getDirection: (e) => (e.deltaY > 1 ? dn.Next : dn.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          _n = "HorizontalBar_base_49",
          An = "HorizontalBar_base__nonActive_82",
          Fn = "HorizontalBar_leftButton_5f",
          gn = "HorizontalBar_rightButton_03",
          Dn = "HorizontalBar_track_0d",
          Bn = "HorizontalBar_thumb_fd",
          Cn = "HorizontalBar_rail_32",
          pn = "disable",
          bn = { pending: !1, offset: 0 },
          hn = (e) => {
            var u;
            return 0.9 * (null != (u = e.getWrapperSize()) ? u : 0);
          },
          fn = () => {},
          vn = (e, u) => Math.max(20, e.offsetWidth * u),
          wn = (0, n.memo)(
            ({ api: e, classNames: u = {}, getStepByRailClick: t = hn, onDrag: r = fn }) => {
              const s = (0, n.useRef)(null),
                o = (0, n.useRef)(null),
                i = (0, n.useRef)(null),
                l = (0, n.useRef)(null),
                c = (0, n.useRef)(null),
                d = e.stepTimeout || 100,
                E = (0, n.useState)(bn),
                m = E[0],
                _ = E[1],
                A = (0, n.useCallback)(
                  (e) => {
                    (_(e),
                      c.current &&
                        r({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [r],
                ),
                F = () => {
                  const u = l.current,
                    t = c.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && u && t && a)) return;
                  const r = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / a),
                    d = ku(0, 1, r / (a - n)),
                    E = (u.offsetWidth - vn(u, s)) * d;
                  ((t.style.transform = `translateX(${0 | E}px)`),
                    ((e) => {
                      if (o.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (o.current.classList.add(pn), void i.current.classList.remove(pn));
                        if (
                          ((u = l.current),
                          (t = c.current),
                          e - (u.offsetWidth - t.offsetWidth) >= -0.5)
                        )
                          return (o.current.classList.remove(pn), void i.current.classList.add(pn));
                        var u, t;
                        (o.current.classList.remove(pn), i.current.classList.remove(pn));
                      }
                    })(E));
                },
                g = sn(() => {
                  ((() => {
                    const u = c.current,
                      t = l.current,
                      n = e.getWrapperSize(),
                      a = e.getContainerSize();
                    if (!(a && u && n && t)) return;
                    const r = Math.min(1, n / a);
                    ((u.style.width = `${vn(t, r)}px`),
                      (u.style.display = "flex"),
                      s.current &&
                        (1 === r ? s.current.classList.add(An) : s.current.classList.remove(An)));
                  })(),
                    F());
                });
              ((0, n.useEffect)(() => an(g)),
                (0, n.useEffect)(
                  () =>
                    an(() => {
                      const u = () => {
                        F();
                      };
                      let t = fn;
                      const n = () => {
                        (t(), (t = an(g)));
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
                (0, n.useEffect)(() => {
                  if (!m.pending) return;
                  const u = (u) => {
                      var t;
                      const n = e.contentRef.current;
                      if (!n) return;
                      const a = l.current,
                        s = c.current;
                      if (!n || !a || !s) return;
                      const o = u.screenX - m.offset - a.getBoundingClientRect().x,
                        i = (o / a.offsetWidth) * (null != (t = e.getContainerSize()) ? t : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(n, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        r({ type: "dragging", thumb: s, thumbOffset: o, contentOffset: i }));
                    },
                    t = () => {
                      (window.removeEventListener("mousemove", u), A(bn));
                    };
                  return (
                    window.addEventListener("mousemove", u),
                    window.addEventListener("mouseup", t),
                    () => {
                      (window.removeEventListener("mousemove", u),
                        window.removeEventListener("mouseup", t));
                    }
                  );
                }, [e, m.offset, m.pending, r, A]));
              const D = (function (e, u, t = []) {
                  const a = (0, n.useRef)(0),
                    r = (0, n.useCallback)(() => window.clearInterval(a.current), t || []);
                  (0, n.useEffect)(() => r, [r]);
                  const s = (null != t ? t : []).concat([u]);
                  return [
                    (0, n.useCallback)((t) => {
                      ((a.current = window.setInterval(() => e(t, !0), u)), e(t, !1));
                    }, s),
                    r,
                  ];
                })((u) => e.applyStepTo(u), d, [e]),
                B = D[0],
                p = D[1];
              (0, n.useEffect)(
                () => (
                  document.addEventListener("mouseup", p, !0),
                  () => document.removeEventListener("mouseup", p, !0)
                ),
                [p],
              );
              const b = (e) => {
                e.target.classList.contains(pn) || He("highlight");
              };
              return a().createElement(
                "div",
                { className: C()(_n, u.base), ref: s, onWheel: e.handleMouseWheel },
                a().createElement("div", {
                  className: C()(Fn, u.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(pn) || 0 !== e.button || (He("play"), B(dn.Next));
                  },
                  onMouseUp: p,
                  ref: o,
                  onMouseEnter: b,
                }),
                a().createElement(
                  "div",
                  {
                    className: C()(Dn, u.track),
                    onMouseDown: (u) => {
                      const n = c.current;
                      if (n && 0 === u.button)
                        if ((He("play"), u.target === n))
                          A({ pending: !0, offset: u.screenX - n.getBoundingClientRect().x });
                        else {
                          ((u) => {
                            const n = c.current,
                              a = e.contentRef.current;
                            if (!n || !a) return;
                            const r = t(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * u);
                          })(u.screenX > n.getBoundingClientRect().x ? dn.Prev : dn.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: b,
                  },
                  a().createElement("div", { ref: c, className: C()(Bn, u.thumb) }),
                  a().createElement("div", { className: C()(Cn, u.rail) }),
                ),
                a().createElement("div", {
                  className: C()(gn, u.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(pn) || 0 !== e.button || (He("play"), B(dn.Prev));
                  },
                  onMouseUp: p,
                  ref: i,
                  onMouseEnter: b,
                }),
              );
            },
          ),
          Sn = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Pn = ({ api: e, className: u, classNames: t, children: r, style: s }) => (
            (0, n.useEffect)(() => an(e.recalculateContent)),
            a().createElement(
              "div",
              { className: C()(Sn.base, u), style: s },
              a().createElement(
                "div",
                {
                  className: C()(Sn.wrapper, null == t ? void 0 : t.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                a().createElement(
                  "div",
                  { className: C()(Sn.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          );
        ((Pn.Bar = wn),
          (Pn.Default = ({
            children: e,
            api: u,
            className: t,
            barClassNames: r,
            areaClassName: s,
            classNames: o,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const d = (0, n.useMemo)(() => {
                const e = r || {};
                return Object.assign({}, e, { base: C()(Sn.base, e.base) });
              }, [r]),
              E = (0, n.useMemo)(() => Object.assign({}, u, { handleMouseWheel: () => {} }), [u]);
            return a().createElement(
              "div",
              { className: C()(Sn.defaultScroll, t), onWheel: u.handleMouseWheel },
              a().createElement(
                "div",
                { className: C()(Sn.defaultScrollArea, s) },
                a().createElement(Pn, { className: i, api: E, classNames: o }, e),
              ),
              a().createElement(wn, { getStepByRailClick: l, api: u, onDrag: c, classNames: d }),
            );
          }),
          (Pn.SeniorityAwards = ({ api: e, className: u, classNames: t, children: r }) => (
            (0, n.useEffect)(() => an(e.recalculateContent)),
            a().createElement(
              "div",
              { className: C()(Sn.base, u) },
              a().createElement(
                "div",
                { className: C()(Sn.wrapper, null == t ? void 0 : t.wrapper), ref: e.wrapperRef },
                a().createElement(
                  "div",
                  { className: C()(Sn.content, null == t ? void 0 : t.content), ref: e.contentRef },
                  r,
                ),
              ),
            )
          )));
        const yn = { type: "idle" };
        const xn = (e, u, t) => {
          const a = t.contentRef,
            r = t.clampPosition,
            s = t.getWrapperSize,
            o = (0, n.useState)(),
            i = o[0],
            l = o[1],
            c = w(),
            d = c.remScreenWidth,
            E = c.remScreenHeight;
          return (
            (0, n.useEffect)(
              () =>
                an(() => {
                  const t = u.current,
                    n = a.current,
                    o = s();
                  if (void 0 === e || !t || !n || !o) return l(void 0);
                  const i = t[e],
                    c = i.offsetWidth,
                    d = i.offsetLeft,
                    E = r(n, d - o / 2 + c / 2);
                  l(E);
                }),
              [r, a, e, u, d, E, s],
            ),
            (0, n.useEffect)(() => {
              l(null);
            }, [d, E]),
            i
          );
        };
        let Rn;
        !(function (e) {
          ((e[(e.LeftHidden = 0)] = "LeftHidden"),
            (e[(e.Visible = 1)] = "Visible"),
            (e[(e.RightHidden = 2)] = "RightHidden"));
        })(Rn || (Rn = {}));
        let Tn;
        !(function (e) {
          ((e[(e.Start = 0)] = "Start"),
            (e[(e.Between = 1)] = "Between"),
            (e[(e.End = 2)] = "End"));
        })(Tn || (Tn = {}));
        const Mn = {
          base: "Arrow_base_f4",
          bg: "Arrow_bg_b9",
          base__right: "Arrow_base__right_86",
        };
        let Nn;
        !(function (e) {
          ((e.Left = "left"), (e.Right = "right"));
        })(Nn || (Nn = {}));
        const kn = R.strings.battle_matters.mainScreen.list,
          In = ({ isVisible: e, direction: u, onClick: t }) => {
            const n = () => {
                Ue.playHighlight();
              },
              r = () => {
                (Ue.playClick(), t());
              };
            return (0, at.useTransition)(e, {
              from: { opacity: 0 },
              enter: { opacity: 1 },
              leave: { opacity: 0 },
              config: { duration: 300 },
            })(
              (e, t) =>
                t &&
                a().createElement(
                  at.animated.div,
                  { style: e },
                  a().createElement(
                    Ju,
                    { body: kn.arrow() },
                    a().createElement(
                      "div",
                      { className: C()(Mn.base, Mn[`base__${u}`]), onMouseEnter: n, onClick: r },
                      a().createElement("div", { className: Mn.bg }),
                    ),
                  ),
                ),
            );
          },
          Ln = "Action_base_e7",
          On = "Action_glow_d8",
          Hn = "Action_glow__wide_14",
          Un = "Action_glow__normal_a6",
          Gn = "Action_base__withGlow_02",
          $n = "Action_button_1d",
          Wn = "Action_buttonIcon_31",
          Qn = R.strings.battle_matters.mainScreen.quest,
          zn = (0, n.memo)(
            ({
              classNames: e,
              hasGlow: u,
              onClick: t,
              onMouseDown: n,
              onMouseMove: r,
              onMouseUp: s,
              onMouseLeave: o,
            }) => {
              const i = w().mediaSize >= h.Medium ? We.medium : We.small;
              return a().createElement(
                "div",
                { className: C()(Ln, u && Gn, null == e ? void 0 : e.base) },
                a().createElement("div", { className: C()(On, Hn) }),
                a().createElement("div", { className: C()(On, Un) }),
                a().createElement(
                  ze,
                  {
                    type: $e.ghost,
                    mixClass: C()($n, null == e ? void 0 : e.button),
                    size: i,
                    onClick: t,
                    onMouseMove: r,
                    onMouseUp: s,
                    onMouseLeave: o,
                    onMouseDown: n,
                  },
                  a().createElement("div", { className: Wn }),
                  Qn.action(),
                ),
              );
            },
          ),
          qn = {
            base: "Progress_base_2e",
            value: "Progress_value_f1",
            base__inProgress: "Progress_base__inProgress_eb",
            base__done: "Progress_base__done_29",
            current: "Progress_current_ad",
            timingFunction: "Progress_timingFunction_7e",
          },
          jn = R.strings.battle_matters.mainScreen.quest,
          Yn = Object.assign({}, Ou, {
            line: { delay: 0, duration: 2e3 },
            delta: { className: qn.timingFunction, delay: 0, duration: 2e3 },
          }),
          Vn = (0, $.Pi)(({ className: e, state: u, maxProgress: t }) => {
            const r = (0, n.useContext)(Da),
              s = r.progressToShow,
              o = r.lastShowedProgress,
              i = r.setLastShowedProgress,
              l = r.setIsProgressComplete;
            (0, n.useEffect)(() => {
              s > o && He(R.sounds.dq_screen_progress_bar());
            }, [o, s]);
            const c = (0, n.useCallback)(() => {
                i(s);
              }, [s, i]),
              d = (0, n.useCallback)(() => {
                l(!0);
              }, [l]);
            return (
              (0, n.useEffect)(
                () => () => {
                  i(s);
                },
                [s, i],
              ),
              a().createElement(
                "div",
                { className: C()(qn.base, qn[`base__${u}`], e) },
                a().createElement(Oe, {
                  classMix: qn.value,
                  text: jn.progress(),
                  binding: {
                    current: a().createElement(
                      "span",
                      { className: qn.current },
                      a().createElement(q, { value: o }),
                    ),
                    max: a().createElement(q, { value: t }),
                  },
                }),
                a().createElement(Hu, {
                  size: nu.Small,
                  value: s,
                  deltaFrom: o,
                  maxValue: t,
                  onEndAnimation: c,
                  onComplete: d,
                  animationSettings: Yn,
                }),
              )
            );
          }),
          Xn = {
            base: "Content_base_57",
            condition: "Content_condition_c8",
            base__inProgress: "Content_base__inProgress_8c",
            base__done: "Content_base__done_a4",
            conditionText: "Content_conditionText_8d",
            progress: "Content_progress_da",
            spacer: "Content_spacer_02",
            action: "Content_action_da",
            base__dragging: "Content_base__dragging_0c",
            actionButton: "Content_actionButton_89",
            base__buttonClicked: "Content_base__buttonClicked_47",
          },
          Kn = { base: Xn.action, button: Xn.actionButton },
          Zn = (0, $.Pi)(
            ({
              index: e,
              questState: u,
              isDragging: t,
              isButtonClicked: n,
              onMouseDown: r,
              onMouseMove: s,
              onMouseUp: o,
              onMouseLeave: i,
            }) => {
              const l = ye(),
                c = l.model,
                d = l.controls,
                E = sn(() => {
                  d.showAnimForQuest(g);
                }),
                m = c.computes.getQuest(e);
              if (!m) return null;
              const _ = m.condition,
                A = m.maxProgress,
                F = m.hasAnimation,
                g = m.number;
              return a().createElement(
                "div",
                {
                  className: C()(
                    Xn.base,
                    Xn[`base__${u}`],
                    t && Xn.base__dragging,
                    n && Xn.base__buttonClicked,
                  ),
                },
                a().createElement(
                  "div",
                  { className: Xn.condition },
                  a().createElement(Oe, { classMix: Xn.conditionText, text: _ }),
                ),
                A > 0 &&
                  a().createElement(Vn, { className: Xn.progress, state: u, maxProgress: A }),
                a().createElement("div", { className: Xn.spacer }),
                F &&
                  a().createElement(zn, {
                    hasGlow: u === _e.InProgress,
                    classNames: Kn,
                    onClick: E,
                    onMouseDown: r,
                    onMouseMove: s,
                    onMouseUp: o,
                    onMouseLeave: i,
                  }),
              );
            },
          ),
          Jn = {
            base: "Header_base_2d",
            card: "Header_card_8a",
            base__done: "Header_base__done_14",
            base__inProgress: "Header_base__inProgress_fb",
            base__unavailable: "Header_base__unavailable_74",
            glow: "Header_glow_5d",
            glow__visible: "Header_glow__visible_56",
            glow__unavailable: "Header_glow__unavailable_32",
            glow__inProgress: "Header_glow__inProgress_c2",
            glow__done: "Header_glow__done_7f",
            bg: "Header_bg_39",
            header: "Header_header_32",
            body: "Header_body_14",
            content: "Header_content_d3",
            content__toInProgress: "Header_content__toInProgress_03",
            fadeIn: "Header_fadeIn_7b",
            stateIcon: "Header_stateIcon_d1",
            unavailable: "Header_unavailable_d0",
            unavailableTitle: "Header_unavailableTitle_48",
            unavailableDescription: "Header_unavailableDescription_22",
            rewards: "Header_rewards_08",
            base__dragging: "Header_base__dragging_ae",
            arrow: "Header_arrow_98",
            arrowIcon: "Header_arrowIcon_a4",
            arrowIcon__default: "Header_arrowIcon__default_44",
            arrowIcon__done: "Header_arrowIcon__done_48",
            headerNumber: "Header_headerNumber_0e",
            headerNumberGlow: "Header_headerNumberGlow_5d",
            headerNumberText: "Header_headerNumberText_93",
            headerDivider: "Header_headerDivider_b4",
            headerInfo: "Header_headerInfo_d7",
            headerTitle: "Header_headerTitle_c3",
            headerTitleText: "Header_headerTitleText_22",
            headerButton: "Header_headerButton_eb",
            headerButton__hidden: "Header_headerButton__hidden_32",
            base__buttonClicked: "Header_base__buttonClicked_53",
            headerButtonIcon: "Header_headerButtonIcon_52",
            headerDescription: "Header_headerDescription_bf",
            fadeOut: "Header_fadeOut_30",
            fadeInWithScale: "Header_fadeInWithScale_9f",
            slideUp: "Header_slideUp_8c",
            scale: "Header_scale_ad",
            fadeInUp: "Header_fadeInUp_0b",
            rotate: "Header_rotate_00",
            translatedRotating: "Header_translatedRotating_02",
          },
          ea = (0, $.Pi)(
            ({
              index: e,
              questState: u,
              isDragging: t,
              isButtonClicked: n,
              onMouseDown: r,
              onMouseMove: s,
              onMouseUp: o,
              onMouseLeave: i,
            }) => {
              const l = ye(),
                c = l.model,
                d = l.controls,
                E = sn(() => {
                  d.showManualForQuest(_);
                }),
                m = c.computes.getQuest(e);
              if (!m) return null;
              const _ = m.number,
                A = m.description,
                F = m.title,
                g = m.hasManualPage;
              return a().createElement(
                "div",
                {
                  className: C()(
                    Jn.base,
                    Jn[`base__${u}`],
                    t && Jn.base__dragging,
                    n && Jn.base__buttonClicked,
                  ),
                },
                a().createElement(
                  "div",
                  { className: Jn.headerNumber },
                  a().createElement("div", { className: Jn.headerNumberGlow }),
                  a().createElement("div", { className: Jn.headerNumberText }, _),
                ),
                a().createElement("div", { className: Jn.headerDivider }),
                a().createElement(
                  "div",
                  { className: Jn.headerInfo },
                  a().createElement(
                    "div",
                    { className: Jn.headerTitle },
                    a().createElement("div", { className: Jn.headerTitleText }, F),
                    a().createElement(
                      ze,
                      {
                        type: $e.ghost,
                        mixClass: C()(Jn.headerButton, !g && Jn.headerButton__hidden),
                        onClick: E,
                        onMouseMove: s,
                        onMouseUp: o,
                        onMouseLeave: i,
                        onMouseDown: r,
                      },
                      a().createElement("div", { className: Jn.headerButtonIcon }),
                    ),
                  ),
                  a().createElement(
                    "div",
                    { className: Jn.headerDescription },
                    a().createElement(Oe, { text: A }),
                  ),
                ),
              );
            },
          ),
          ua = {
            base: "Quest_base_f9",
            card: "Quest_card_f9",
            base__done: "Quest_base__done_84",
            base__inProgress: "Quest_base__inProgress_ae",
            base__unavailable: "Quest_base__unavailable_26",
            glow: "Quest_glow_2b",
            glow__visible: "Quest_glow__visible_01",
            glow__unavailable: "Quest_glow__unavailable_12",
            glow__inProgress: "Quest_glow__inProgress_29",
            glow__done: "Quest_glow__done_47",
            bg: "Quest_bg_9c",
            header: "Quest_header_75",
            body: "Quest_body_38",
            content: "Quest_content_14",
            content__toInProgress: "Quest_content__toInProgress_08",
            fadeIn: "Quest_fadeIn_78",
            stateIcon: "Quest_stateIcon_68",
            unavailable: "Quest_unavailable_a7",
            unavailableTitle: "Quest_unavailableTitle_4a",
            unavailableDescription: "Quest_unavailableDescription_46",
            rewards: "Quest_rewards_21",
            base__dragging: "Quest_base__dragging_bd",
            arrow: "Quest_arrow_10",
            arrowIcon: "Quest_arrowIcon_57",
            arrowIcon__default: "Quest_arrowIcon__default_8f",
            arrowIcon__done: "Quest_arrowIcon__done_98",
            fadeOut: "Quest_fadeOut_a2",
            fadeInWithScale: "Quest_fadeInWithScale_18",
            slideUp: "Quest_slideUp_59",
            scale: "Quest_scale_1b",
            fadeInUp: "Quest_fadeInUp_93",
            rotate: "Quest_rotate_8e",
            translatedRotating: "Quest_translatedRotating_ea",
          },
          ta = "LootboxTransition_base_9c",
          na = "LootboxTransition_lootbox_62",
          aa = "LootboxTransition_smoke_43",
          ra = (0, n.memo)(({ delay: e, isEnabled: u = !0, children: t }) =>
            u
              ? a().createElement(
                  "div",
                  { className: ta },
                  a().createElement("div", {
                    className: aa,
                    style: { animationDelay: `${e + 500}ms` },
                  }),
                  a().createElement(
                    "div",
                    { className: na, style: { animationDelay: `${e}ms, ${e + 500}ms` } },
                    t,
                  ),
                )
              : t,
          ),
          sa = "Rewards_base_26",
          oa = "Rewards_base__vertical_9f",
          ia = "Rewards_reward_7b",
          la = "Rewards_reward__vertical_c6";
        function ca() {
          return (
            (ca =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            ca.apply(this, arguments)
          );
        }
        const da = [j.BattleToken],
          Ea = a().memo(
            ({
              data: e,
              size: u = V.Big,
              isVertical: t = !1,
              count: r,
              classMix: s,
              rewardItemClassMix: o,
              boxRewardTooltip: i,
              boxRewardValue: l,
              isLootboxAnimationEnabled: c = !1,
              delay: d = 0,
            }) => {
              const E = (0, n.useMemo)(
                  () =>
                    r && r < e.length ? `R.images.gui.maps.icons.quests.bonuses.${u}.default` : "",
                  [r, e.length, u],
                ),
                m =
                  l ||
                  ((_ = R.strings.tooltips.quests.awards.additional.bottom()),
                  (A = { count: e.length - (r || 0) }),
                  _.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
                    const u = 0 === e.indexOf("%") ? 2 : 1;
                    return String(A[e.slice(u, -u)]);
                  }));
              var _, A;
              const F = C()(sa, t && oa, s),
                g = C()(ia, t && la, o);
              return a().createElement(
                "div",
                { className: F },
                E
                  ? a().createElement(
                      a().Fragment,
                      null,
                      e
                        .slice(0, r)
                        .map((e, t) =>
                          a().createElement(
                            "div",
                            { key: t, className: g },
                            a().createElement(nt, ca({ size: u }, e)),
                          ),
                        ),
                      a().createElement(
                        "div",
                        { className: g },
                        a().createElement(nt, {
                          name: "more",
                          image: E,
                          size: u,
                          value: m,
                          tooltipArgs: i,
                        }),
                      ),
                    )
                  : e.map((e, t) => {
                      const r = e.name,
                        s = c && da.includes(r);
                      return a().createElement(
                        n.Fragment,
                        { key: t },
                        a().createElement(
                          ra,
                          { delay: d, isEnabled: s },
                          a().createElement(
                            "div",
                            { key: t, className: g },
                            a().createElement(nt, ca({ size: u }, e)),
                          ),
                        ),
                      );
                    }),
              );
            },
          ),
          ma = "Rewards_reward_9e";
        function _a() {
          return (
            (_a =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            _a.apply(this, arguments)
          );
        }
        const Aa = (0, $.Pi)(({ className: e, index: u }) => {
            const t = ye().model,
              n = w().mediaSize >= h.Medium ? V.Big : V.Small,
              r = t.computes.getQuestRewardsProps(u, n);
            return a().createElement(
              Ea,
              _a({}, r, { classMix: e, rewardItemClassMix: ma, size: n }),
            );
          }),
          Fa = R.strings.battle_matters.mainScreen.quest,
          ga = (e) => {
            switch (e) {
              case _e.Done:
                return _e.InProgress;
              case _e.InProgress:
              default:
                return _e.Unavailable;
            }
          },
          Da = (0, n.createContext)({}),
          Ba = (0, $.Pi)(
            ({
              index: e,
              isDragging: u,
              isVisible: t,
              state: r,
              maxProgress: s,
              lastSeenProgress: o,
              currentProgress: i,
              questsRef: l,
            }) => {
              const c = ye().model,
                d = c.questSwitchAnimationPhase.get(),
                E = c.computes.getLastDoneQuestIndex() === e,
                m = c.computes.getFirstInProgressQuestIndex() === e,
                _ = e === c.computes.getQuestsLength() - 1,
                A = c.computes.getIsQuestSwitchAnimationNeeded() && (E || m),
                F = (0, n.useState)(E || m ? o : i),
                g = F[0],
                D = F[1],
                B = (0, n.useState)(g),
                p = B[0],
                b = B[1],
                h = (0, n.useState)(A ? ga(r) : r),
                f = h[0],
                v = h[1],
                w = (0, n.useState)(f !== _e.Unavailable),
                S = w[0],
                P = w[1],
                y = (0, n.useState)(g === s),
                x = y[0],
                T = y[1],
                M = E && d === ve.ToDone,
                N = m && d === ve.ToInProgress;
              ((0, n.useEffect)(() => {
                A ? (v(ga(r)), P(ga(r) !== _e.Unavailable)) : (v(r), P(r !== _e.Unavailable), b(i));
              }, [A, r, i]),
                (0, n.useEffect)(() => {
                  if (M) {
                    if (!(s > 0) || x)
                      return (v(_e.Done), du(() => He(R.sounds.dq_screen_quest_complete()), 300));
                    b(i);
                  }
                  if (N) return (v(_e.InProgress), b(i), du(() => P(!0), 500));
                }, [M, N, x, s, i]));
              const k = (0, n.useState)(!1),
                I = k[0],
                L = k[1],
                O = sn(() => {
                  L(!0);
                }),
                H = sn(() => {
                  L(!1);
                }),
                U = sn(() => {
                  L(!1);
                }),
                G = sn(() => {
                  L(!1);
                }),
                $ = (0, n.useMemo)(
                  () => ({
                    progressToShow: p,
                    lastShowedProgress: g,
                    setLastShowedProgress: D,
                    setIsProgressComplete: T,
                  }),
                  [g, p],
                );
              return a().createElement(
                Da.Provider,
                { value: $ },
                a().createElement(
                  "div",
                  {
                    className: C()(
                      ua.base,
                      ua[`base__${f}`],
                      u && ua.base__dragging,
                      I && ua.base__buttonClicked,
                    ),
                  },
                  a().createElement(
                    "div",
                    { className: ua.card, ref: (u) => (l.current[e] = u) },
                    t &&
                      a().createElement(
                        a().Fragment,
                        null,
                        Object.values(_e).map((e, u) =>
                          a().createElement("div", {
                            key: u,
                            className: C()(ua.glow, ua[`glow__${e}`], f === e && ua.glow__visible),
                          }),
                        ),
                        a().createElement("div", { className: ua.bg }),
                        a().createElement(
                          "div",
                          { className: ua.header },
                          a().createElement(ea, {
                            index: e,
                            questState: f,
                            isDragging: u,
                            isButtonClicked: I,
                            onMouseDown: O,
                            onMouseMove: H,
                            onMouseUp: U,
                            onMouseLeave: G,
                          }),
                        ),
                        a().createElement(
                          "div",
                          { className: ua.body },
                          S
                            ? a().createElement(
                                "div",
                                {
                                  className: C()(
                                    ua.content,
                                    N && ua[`content__${ve.ToInProgress}`],
                                  ),
                                },
                                a().createElement(Zn, {
                                  index: e,
                                  questState: f,
                                  isDragging: u,
                                  isButtonClicked: I,
                                  onMouseDown: O,
                                  onMouseMove: H,
                                  onMouseUp: U,
                                  onMouseLeave: G,
                                }),
                              )
                            : a().createElement(
                                "div",
                                { className: ua.unavailable },
                                a().createElement(
                                  "div",
                                  { className: ua.unavailableTitle },
                                  Fa.unavailableTitle(),
                                ),
                                a().createElement(
                                  "div",
                                  { className: ua.unavailableDescription },
                                  Fa.unavailableDescription(),
                                ),
                              ),
                          a().createElement(Aa, {
                            className: C()(ua.rewards, u && ua.rewards__dragging),
                            index: e,
                          }),
                        ),
                        a().createElement("div", { className: ua.stateIcon }),
                      ),
                  ),
                  !_ &&
                    a().createElement(
                      "div",
                      { className: ua.arrow },
                      a().createElement("div", {
                        className: C()(ua.arrowIcon, ua.arrowIcon__default),
                      }),
                      a().createElement("div", {
                        className: C()(ua.arrowIcon, ua.arrowIcon__done),
                      }),
                    ),
                ),
              );
            },
          ),
          Ca = "Quests_base_e7",
          pa = "Quests_base__frozen_b7",
          ba = "Quests_wrapper_21",
          ha = "Quests_content_a0",
          fa = "Quests_bar_12",
          va = "Quests_barThumb_37",
          wa = "Quests_barRail_73",
          Sa = "Quests_lip_25",
          Pa = "Quests_lip__left_1e",
          ya = "Quests_lip__right_63",
          xa = "Quests_shadow_1e",
          Ra = "Quests_shadow__visible_b9",
          Ta = "Quests_shadow__left_23",
          Ma = "Quests_shadow__right_a6",
          Na = "Quests_arrow_c8",
          ka = "Quests_arrow__left_f2",
          Ia = "Quests_arrow__right_82";
        function La() {
          return (
            (La =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var n in t) Object.prototype.hasOwnProperty.call(t, n) && (e[n] = t[n]);
                }
                return e;
              }),
            La.apply(this, arguments)
          );
        }
        const Oa = (0, $.Pi)(() => {
            const e = (0, n.useRef)([]),
              u = mn(),
              t = ye(),
              r = t.model,
              o = t.controls,
              i = r.computes.getQuestsLength(),
              l = r.computes.getIsQuestSwitchAnimationNeeded(),
              c = r.computes.getLastDoneQuestIndex(),
              d = void 0 !== c ? r.computes.getIsProgressionQuest(c) : void 0,
              E = r.computes.getCurrentQuestIndex(),
              m = r.questSwitchAnimationPhase.get(),
              _ = r.isRewardsViewOpen.get(),
              A = r.lastPlayedToDoneAnimationQuestIndex.get(),
              F = c === i - 1,
              g = (function (e, u, t) {
                const a = e.contentRef,
                  r = e.wrapperRef,
                  o = e.scrollPosition,
                  i = e.clampPosition,
                  l = e.animationScroll,
                  c = e.events,
                  d = (0, n.useState)(yn),
                  E = d[0],
                  m = d[1];
                return (
                  (0, n.useEffect)(() => {
                    const e = a.current;
                    e && (e.style.cursor = "dragging" === E.type ? "move" : "grab");
                  }, [a, E.type]),
                  (0, n.useEffect)(() => {
                    if ("dragging" !== E.type) return;
                    const e = s.O.client.events.mouse.move(([e, t]) => {
                        const n = a.current,
                          s = r.current;
                        if (!n || !s) return;
                        if ("inside" === t && e.clientX < 0) return;
                        const c = "inside" === t ? e.clientX : e.clientX - s.offsetLeft,
                          d = E.positionFrom - c,
                          m = E.previousScrollPosition + d;
                        o.start(
                          Object.assign(
                            {
                              scrollPosition: i(n, m),
                              from: { scrollPosition: l.scrollPosition.get() },
                            },
                            u && { config: u },
                          ),
                        );
                      }),
                      t = s.O.client.events.mouse.up(function () {
                        m({ type: "scrollingToEnd" });
                      });
                    return () => {
                      (e(), t());
                    };
                  }, [l.scrollPosition, i, a, E, o, r, u]),
                  (0, n.useEffect)(() => {
                    if ("scrollingToEnd" !== E.type) return;
                    const e = () => {
                      m(yn);
                    };
                    return (l.scrollPosition.idle && e(), c.on("rest", e), () => c.off("rest", e));
                  }, [l.scrollPosition, E.type, c]),
                  (0, n.useEffect)(() => {
                    const e = a.current;
                    if (!e) return;
                    const u = (e) => {
                      (t &&
                        t.allowedButtons &&
                        -1 === t.allowedButtons.findIndex((u) => e.button === u)) ||
                        m({
                          type: "dragging",
                          positionFrom: e.screenX,
                          previousScrollPosition: l.scrollPosition.get(),
                        });
                    };
                    return (
                      e.addEventListener("mousedown", u),
                      () => e.removeEventListener("mousedown", u)
                    );
                  }, [l.scrollPosition, a, t]),
                  E
                );
              })(u),
              D = ((e) => {
                const u = (0, n.useState)(Tn.Start),
                  t = u[0],
                  a = u[1],
                  r = e.animationScroll,
                  s = e.getContainerSize,
                  o = e.getWrapperSize,
                  i = e.events;
                return (
                  (0, n.useEffect)(() => {
                    const e = () => {
                      const e = r.scrollPosition.get(),
                        u = s() - o() - 10;
                      a(e <= 10 ? Tn.Start : e >= u ? Tn.End : Tn.Between);
                    };
                    return (i.on("change", e), () => i.off("change", e));
                  }, [r.scrollPosition, i, s, o]),
                  t
                );
              })(u),
              B = xn(c, e, u),
              p = xn(E, e, u),
              b = ((e, u) => {
                const t = w(),
                  a = t.remScreenWidth,
                  r = t.remScreenHeight,
                  s = (0, n.useState)([]),
                  o = s[0],
                  i = s[1],
                  l = (0, n.useRef)({ boxes: [], wrapperWidth: 0, scrollPosition: 0 }),
                  c = u.animationScroll,
                  d = u.events,
                  E = u.getWrapperSize,
                  m = (0, n.useCallback)(() => {
                    const e = l.current,
                      u = e.boxes,
                      t = e.wrapperWidth,
                      n = e.scrollPosition;
                    i(
                      u.map(([e, u]) =>
                        u <= n ? Rn.LeftHidden : n + t <= e ? Rn.RightHidden : Rn.Visible,
                      ),
                    );
                  }, []);
                return (
                  (0, n.useEffect)(
                    () =>
                      an(() => {
                        const u = e.current,
                          t = E();
                        u &&
                          t &&
                          ((l.current.boxes = u.map(({ offsetWidth: e, offsetLeft: u }) => [
                            u,
                            u + e,
                          ])),
                          (l.current.wrapperWidth = t),
                          m());
                      }),
                    [a, r, E, m],
                  ),
                  (0, n.useEffect)(() => {
                    const e = () => {
                      ((l.current.scrollPosition = c.scrollPosition.get()), m());
                    };
                    return (d.on("change", e), () => d.off("change", e));
                  }, [c.scrollPosition, m, d]),
                  o
                );
              })(e, u),
              h = void 0 !== E ? b[E] : void 0,
              f = (0, n.useCallback)(
                (e) => {
                  o.setQuestSwitchAnimationPhase(e);
                },
                [o],
              ),
              v = (0, n.useCallback)(
                (e, u) =>
                  du(() => {
                    o.setQuestSwitchAnimationPhase(e);
                  }, u),
                [o],
              );
            ((0, n.useEffect)(() => {
              if (null !== B && null !== p && !_)
                return an(() => {
                  if (l && c !== A)
                    u.scrollPosition.start({
                      scrollPosition: B,
                      onStart: () => {
                        f(ve.Scrolling);
                      },
                      onResolve: () => {
                        f(ve.ToDone);
                      },
                    });
                  else {
                    if (m !== ve.None) return;
                    u.scrollPosition.start({ scrollPosition: p });
                  }
                });
            }, [f, m, l, _, c, A, u.scrollPosition, p, B]),
              (0, n.useEffect)(() => {
                if (null !== B && null !== p)
                  if (_) f(ve.None);
                  else
                    switch (m) {
                      case ve.ToDone:
                        return (
                          o.setLastPlayedToDoneAnimationQuestIndex(c),
                          v(ve.ToDoneFinished, d ? 4900 : 1e3)
                        );
                      case ve.ToDoneFinished:
                        return F
                          ? void f(ve.None)
                          : void u.scrollPosition.start({
                              scrollPosition: p,
                              onStart: () => {
                                f(ve.Scrolling);
                              },
                              onResolve: () => {
                                f(ve.ToInProgress);
                              },
                            });
                      case ve.ToInProgress:
                        return v(ve.None, 1200);
                    }
              }, [o, F, f, v, p, d, _, B, c, m, u.scrollPosition]));
            const S = () => {
              null !== p && u.scrollPosition.start({ scrollPosition: p });
            };
            return a().createElement(
              "div",
              { className: C()(Ca, m !== ve.None && pa) },
              a().createElement(
                "div",
                { className: ba },
                a().createElement(
                  Pn,
                  { api: u, classNames: { content: ha } },
                  r.computes
                    .getQuests()
                    .map((u, t) =>
                      a().createElement(
                        Ba,
                        La(
                          {
                            key: t,
                            index: t,
                            isVisible: b[t] === Rn.Visible,
                            isDragging: "dragging" === g.type,
                            questsRef: e,
                          },
                          u,
                        ),
                      ),
                    ),
                ),
                a().createElement("div", { className: C()(xa, Ta, D !== Tn.Start && Ra) }),
                a().createElement("div", { className: C()(xa, Ma, D !== Tn.End && Ra) }),
                a().createElement("div", { className: C()(Sa, Pa) }),
                a().createElement("div", { className: C()(Sa, ya) }),
                a().createElement(
                  "div",
                  { className: C()(Na, ka) },
                  a().createElement(In, {
                    direction: Nn.Left,
                    isVisible: h === Rn.LeftHidden,
                    onClick: S,
                  }),
                ),
                a().createElement(
                  "div",
                  { className: C()(Na, Ia) },
                  a().createElement(In, {
                    direction: Nn.Right,
                    isVisible: h === Rn.RightHidden,
                    onClick: S,
                  }),
                ),
              ),
              a().createElement(wn, { api: u, classNames: { base: fa, thumb: va, rail: wa } }),
            );
          }),
          Ha = "App_base_85",
          Ua = "App_base__visible_3c",
          Ga = "App_content_6d",
          $a = (0, $.Pi)(() => {
            const e = ye(),
              u = e.controls,
              t = e.model,
              r = t.isLoaded.get();
            var s;
            return (
              (0, n.useEffect)(() => {
                r && u.showView();
              }, [r, u]),
              (s = u.close),
              G(O.n.ESCAPE, s),
              a().createElement(
                "div",
                { className: C()(Ha, t.isLoaded.get() && Ua) },
                a().createElement(z, { isBlurred: !0, onLoaded: u.loaded }),
                a().createElement(
                  "div",
                  { className: Ga },
                  a().createElement(nn, null),
                  a().createElement(Oa, null),
                  a().createElement(yt, null),
                ),
              )
            );
          });
        engine.whenReady.then(() => {
          L().render(
            a().createElement(k, null, a().createElement(Pe, null, a().createElement($a, null))),
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
    (__webpack_require__.O = (e, u, t, n) => {
      if (!u) {
        var a = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [u, t, n] = deferred[i], r = !0, s = 0; s < u.length; s++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[s]))
              ? u.splice(s--, 1)
              : ((r = !1), n < a && (a = n));
          if (r) {
            deferred.splice(i--, 1);
            var o = t();
            void 0 !== o && (e = o);
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
    (__webpack_require__.j = 678),
    (() => {
      var e = { 678: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var n,
            a,
            [r, s, o] = t,
            i = 0;
          if (r.some((u) => 0 !== e[u])) {
            for (n in s) __webpack_require__.o(s, n) && (__webpack_require__.m[n] = s[n]);
            if (o) var l = o(__webpack_require__);
          }
          for (u && u(t); i < r.length; i++)
            ((a = r[i]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [965], () => __webpack_require__(86));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
