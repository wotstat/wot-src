(() => {
  var __webpack_modules__ = {
      2372: (e, t, a) => {
        "use strict";
        a.d(t, { A: () => s });
        var u = a(6179),
          r = a.n(u),
          n = a(4179);
        class s extends r().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = n.B3.GOLD;
            else e = n.B3.INTEGRAL;
            const t = n.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== t ? t : null;
          }
        }
        s.defaultProps = { format: "integral" };
      },
      280: (e, t, a) => {
        "use strict";
        a.d(t, { z: () => l });
        var u = a(6179),
          r = a.n(u),
          n = a(6483),
          s = a.n(n),
          o = a(3649),
          i = a(5287);
        const l = ({ binding: e, text: t = "", classMix: a, alignment: n = o.v2.left }) =>
          null === t
            ? (console.error("FormatText was supplied with 'null'"), null)
            : r().createElement(
                u.Fragment,
                null,
                t.split("\n").map((t, l) =>
                  r().createElement(
                    "div",
                    { className: s()(i.Z.base, a), key: `${t}-${l}` },
                    (0, o.Uw)(t, n, e).map((e, t) =>
                      r().createElement(u.Fragment, { key: `${t}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      6373: (e, t, a) => {
        "use strict";
        a.d(t, { i: () => l });
        var u = a(2056),
          r = a(6179),
          n = a.n(r);
        const s = ["children", "body", "header", "note", "alert", "args"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const i = R.views.common.tooltip_window.simple_tooltip_content,
          l = (e) => {
            let t = e.children,
              a = e.body,
              l = e.header,
              c = e.note,
              _ = e.alert,
              d = e.args,
              m = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, s);
            const E = (0, r.useMemo)(() => {
              const e = Object.assign({}, d, { body: a, header: l, note: c, alert: _ });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [_, a, l, c, d]);
            return n().createElement(
              u.u,
              o(
                {
                  contentId:
                    ((g = null == d ? void 0 : d.hasHtmlContent),
                    g ? i.SimpleTooltipHtmlContent("resId") : i.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: E,
                },
                m,
              ),
              t,
            );
            var g;
          };
      },
      2056: (e, t, a) => {
        "use strict";
        a.d(t, { u: () => l });
        var u = a(7902),
          r = a(4179),
          n = a(6179);
        const s = [
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
        function o(e) {
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
        const i = (e, t, a = {}, u = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: r.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: u,
                },
                a,
              ),
            );
          },
          l = (e) => {
            let t = e.children,
              a = e.contentId,
              r = e.args,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              _ = e.onMouseDown,
              d = e.onClick,
              m = e.ignoreShowDelay,
              E = void 0 !== m && m,
              g = e.ignoreMouseClick,
              p = void 0 !== g && g,
              A = e.decoratorId,
              b = void 0 === A ? 0 : A,
              h = e.isEnabled,
              C = void 0 === h || h,
              v = e.targetId,
              f = void 0 === v ? 0 : v,
              D = e.onShow,
              B = e.onHide,
              F = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, s);
            const w = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, n.useMemo)(() => f || (0, u.F)().resId, [f]),
              P = (0, n.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (i(a, b, { isMouseEvent: !0, on: !0, arguments: o(r) }, S),
                  D && D(),
                  (w.current.isVisible = !0));
              }, [a, b, r, S, D]),
              y = (0, n.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    i(a, b, { on: !1 }, S),
                    w.current.isVisible && B && B(),
                    (w.current.isVisible = !1));
                }
              }, [a, b, S, B]),
              k = (0, n.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(w.current.prevTarget) && y();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", k, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", k, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === C && y();
              }, [C, y]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", y),
                  () => {
                    (window.removeEventListener("mouseleave", y), y());
                  }
                ),
                [y],
              ));
            return C
              ? (0, n.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(P, E ? 100 : 400)),
                            l && l(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (y(), null == c || c(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === p && y(), null == d || d(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === p && y(), null == _ || _(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    F,
                  ),
                )
              : t;
            var x;
          };
      },
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
        (a.r(t), a.d(t, { mouse: () => o, onResize: () => n }));
        var u = a(2472),
          r = a(1176);
        const n = (0, u.E)("clientResized"),
          s = { down: (0, u.E)("mousedown"), up: (0, u.E)("mouseup"), move: (0, u.E)("mousemove") };
        const o = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, r.R)(!1);
          }
          function a() {
            e.enabled && (0, r.R)(!0);
          }
          function u() {
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
          const n = ["down", "up", "move"].reduce(
            (t, a) => (
              (t[a] = (function (t) {
                return (a) => {
                  e.listeners += 1;
                  let r = !0;
                  const n = `mouse${t}`,
                    o = s[t]((e) => a([e, "outside"]));
                  function i(e) {
                    a([e, "inside"]);
                  }
                  return (
                    window.addEventListener(n, i),
                    u(),
                    () => {
                      r &&
                        (o(), window.removeEventListener(n, i), (e.listeners -= 1), u(), (r = !1));
                    }
                  );
                };
              })(a)),
              t
            ),
            {},
          );
          return Object.assign({}, n, {
            disable() {
              ((e.enabled = !1), u());
            },
            enable() {
              ((e.enabled = !0), u());
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
            events: () => u,
            getMouseGlobalPosition: () => n,
            getSize: () => r,
            graphicsQuality: () => s,
          }));
        var u = a(527);
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
      1176: (e, t, a) => {
        "use strict";
        function u(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        a.d(t, { R: () => u });
      },
      2472: (e, t, a) => {
        "use strict";
        function u(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        a.d(t, { E: () => u });
      },
      3138: (e, t, a) => {
        "use strict";
        a.d(t, { O: () => r });
        var u = a(5959);
        const r = { view: a(7641), client: u };
      },
      3722: (e, t, a) => {
        "use strict";
        function u(e, t, a = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, a);
        }
        function r(e, t, a) {
          return `url(${u(e, t, a)})`;
        }
        (a.r(t), a.d(t, { getBgUrl: () => r, getTextureUrl: () => u }));
      },
      6112: (e, t, a) => {
        "use strict";
        a.d(t, { W: () => u });
        const u = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, a) => {
        "use strict";
        a.d(t, { U: () => r });
        var u = a(2472);
        const r = {
          onTextureFrozen: (0, u.E)("self.onTextureFrozen"),
          onTextureReady: (0, u.E)("self.onTextureReady"),
          onDomBuilt: (0, u.E)("self.onDomBuilt"),
          onLoaded: (0, u.E)("self.onLoaded"),
          onDisplayChanged: (0, u.E)("self.onShowingStatusChanged"),
          onFocusUpdated: (0, u.E)("self.onFocusChanged"),
          children: {
            onAdded: (0, u.E)("children.onAdded"),
            onLoaded: (0, u.E)("children.onLoaded"),
            onRemoved: (0, u.E)("children.onRemoved"),
            onAttached: (0, u.E)("children.onAttached"),
            onTextureReady: (0, u.E)("children.onTextureReady"),
            onRequestPosition: (0, u.E)("children.requestPosition"),
          },
        };
      },
      7641: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => o,
            children: () => u,
            displayStatus: () => r.W,
            displayStatusIs: () => w,
            events: () => n.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => B,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => F,
            getScale: () => p,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => v,
            isEventHandled: () => D,
            isFocused: () => C,
            pxToRem: () => A,
            remToPx: () => b,
            resize: () => m,
            sendEvent: () => s.qP,
            setAnimateWindow: () => h,
            setEventHandled: () => f,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => _,
            whenTutorialReady: () => P,
          }));
        var u = a(3722),
          r = a(6112),
          n = a(6538),
          s = a(8566);
        function o(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, a, u = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, a, u);
        }
        function c(e, t, a) {
          return viewEnv.addDataChangedCallback(e, t, a);
        }
        function _(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function m(e, t, a = "px") {
          return "rem" === a ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: b(t.x), y: b(t.y) };
        }
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function p() {
          return viewEnv.getScale();
        }
        function A(e) {
          return viewEnv.pxToRem(e);
        }
        function b(e) {
          return viewEnv.remToPx(e);
        }
        function h(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function C() {
          return viewEnv.isFocused();
        }
        function v() {
          return viewEnv.isClientAccessible();
        }
        function f() {
          return viewEnv.setEventHandled();
        }
        function D() {
          return viewEnv.isEventHandled();
        }
        function B() {
          viewEnv.forceTriggerMouseMove();
        }
        function F() {
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
          P = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : n.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, a) => {
        "use strict";
        a.d(t, { qP: () => l });
        const u = ["args"];
        const r = 2,
          n = 16,
          s = 32,
          o = 64,
          i = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const n = t.args,
                s = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    u,
                    r = {},
                    n = Object.keys(e);
                  for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                  return r;
                })(t, u);
              return void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, s, {
                      arguments:
                        ((r = n),
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
              i("popover" === e ? r : s);
            },
            minimize() {
              i(o);
            },
            move(e) {
              i(n, { isMouseEvent: !0, on: e });
            },
          };
      },
      7902: (e, t, a) => {
        "use strict";
        a.d(t, { F: () => u });
        const u = (e = 1) => {
          const t = new Error().stack;
          let a,
            u = R.invalid("resId");
          return (
            t &&
              ((a = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
              window.__feature &&
                window.__feature !== a &&
                window.subViews[a] &&
                (u = window.subViews[a].id)),
            { caller: a, stack: t, resId: u }
          );
        };
      },
      5521: (e, t, a) => {
        "use strict";
        let u, r;
        (a.d(t, { n: () => u }),
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
          })(u || (u = {})),
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
      7727: (e, t, a) => {
        "use strict";
        function u(e) {
          engine.call("PlaySound", e);
        }
        a.d(t, { $: () => r, G: () => u });
        const r = {
          playHighlight() {
            u("highlight");
          },
          playClick() {
            u("play");
          },
          playYes() {
            u("yes1");
          },
        };
      },
      3649: (e, t, a) => {
        "use strict";
        let u;
        function r(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const a = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(a, -a)]);
          });
        }
        function n(e) {
          return e.replace(/-/g, "_");
        }
        function s(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        (a.d(t, { BN: () => n, Uw: () => m, e: () => s, uF: () => r, v2: () => u }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(u || (u = {})));
        const o = (e, t, a) => {
            if (a % 2) {
              const a = e.pop();
              return [...e, a + t];
            }
            return [...e, t];
          },
          i = (e, t, a) => {
            if (0 === a) return [t];
            if (a % 2) return [...e, " " === t ? " " : t];
            {
              const a = e.pop();
              return [...e, a + t];
            }
          },
          l = (e, t, a = u.left) => e.split(t).reduce(a === u.left ? o : i, []),
          c = (() => {
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
          _ = ["zh_cn", "zh_sg", "zh_tw"],
          d = (e, t = u.left) => {
            const a = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return _.includes(a)
              ? c(e)
              : ((e, t = u.left) => {
                  let a = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (l(n, /( )/, t).forEach((e) => (a = a.concat(l(e, r, u.left)))), a);
                })(e, t);
          },
          m = (e, t, a) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (a && e in a ? a[e] : d(e, t)));
      },
      1358: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        var u = a(3138);
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
            const n = u.O.view.addModelObserver(e, a, r);
            return (
              n > 0
                ? ((this._callbacks[n] = t),
                  a > 0 && (this._views[a] ? this._views[a].push(n) : (this._views[a] = [n])))
                : console.error("Can't add callback for model:", e),
              n
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
              const u = this._callbacks[a];
              void 0 !== u && u(e, t);
            });
          }
        }
        r.__instance = void 0;
        const n = r;
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
        a.d(t, { Sw: () => n.Z, B3: () => l, Z5: () => s, B0: () => i, ry: () => b, Eu: () => h });
        class u {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: a }) => {
                  let u = e.target;
                  do {
                    if (u === t) return;
                    u = u.parentNode;
                  } while (u);
                  a();
                });
              }));
          }
          static get instance() {
            return (u.__instance || (u.__instance = new u()), u.__instance);
          }
          register(e, t) {
            (this.addMouseListener(), this.entries.push({ container: e, callback: t }));
          }
          unregister(e, t) {
            const a = e,
              u = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== a || t !== u,
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
        u.__instance = void 0;
        const r = u;
        var n = a(1358);
        const s = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          o = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, a) => userLocale.getTimeFormat(e, t, void 0 === a || a),
            getTimeString: (e, t, a) => userLocale.getTimeString(e, t, void 0 === a || a),
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
        var m = a(5521),
          E = a(3138);
        const g = ["args"];
        function p(e, t, a, u, r, n, s) {
          try {
            var o = e[n](s),
              i = o.value;
          } catch (e) {
            return void a(e);
          }
          o.done ? t(i) : Promise.resolve(i).then(u, r);
        }
        const A = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          b = (function () {
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
                  return new Promise(function (u, r) {
                    var n = e.apply(t, a);
                    function s(e) {
                      p(n, u, r, s, o, "next", e);
                    }
                    function o(e) {
                      p(n, u, r, s, o, "throw", e);
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
          C = (e, t) => {
            const a = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                n = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    u,
                    r = {},
                    n = Object.keys(e);
                  for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                  return r;
                })(t, g);
              void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: a, type: e }, n, {
                      arguments:
                        ((u = r),
                        Object.entries(u).map(([e, t]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: a, type: e }, n));
            } else viewEnv.handleViewEvent({ __Type: a, type: e });
            var u;
          },
          v = () => C(i.CLOSE),
          f = (e, t) => {
            e.keyCode === m.n.ESCAPE && t();
          };
        var D = a(7572);
        const B = r.instance,
          F = {
            DataTracker: n.Z,
            ViewModel: D.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: _,
            DateFormatType: d,
            makeGlobalBoundingBox: A,
            sendMoveEvent: (e) => C(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: v,
            sendClosePopOverEvent: () => C(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, t, a = 0) => {
              C(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: a,
                args: t,
              });
            },
            sendShowPopOverEvent: (e, t, a, u, r = R.invalid("resId"), n) => {
              const s = E.O.view.getViewGlobalPosition(),
                o = a.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                _ = o.width,
                d = o.height,
                m = {
                  x: E.O.view.pxToRem(l) + s.x,
                  y: E.O.view.pxToRem(c) + s.y,
                  width: E.O.view.pxToRem(_),
                  height: E.O.view.pxToRem(d),
                };
              C(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: u || R.invalid("resId"),
                targetID: r,
                direction: t,
                bbox: A(m),
                on: !0,
                args: n,
              });
            },
            addEscapeListener: (e) => {
              const t = (t) => f(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              f(e, v);
            },
            handleViewEvent: C,
            onBindingsReady: b,
            onLayoutReady: h,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
            dumpViewModel: function e(t) {
              const a = {};
              if ("object" != typeof t) return t;
              for (const u in t)
                if (Object.prototype.hasOwnProperty.call(t, u)) {
                  const r = Object.prototype.toString.call(t[u]);
                  if (r.startsWith("[object CoherentArrayProxy]")) {
                    const r = t[u];
                    a[u] = [];
                    for (let t = 0; t < r.length; t++) a[u].push({ value: e(r[t].value) });
                  } else
                    r.startsWith("[object class BW::WULF::ViewModel")
                      ? (a[u] = e(t[u]))
                      : (a[u] = t[u]);
                }
              return a;
            },
            ClickOutsideManager: B,
            SystemLocale: s,
            UserLocale: o,
          };
        window.ViewEnvHelper = F;
      },
      9481: (e, t, a) => {
        "use strict";
        var u = {};
        (a.r(u),
          a.d(u, {
            Area: () => Mr,
            Bar: () => Nr,
            DefaultScroll: () => Tr,
            Direction: () => Ar,
            defaultSettings: () => br,
            useHorizontalScrollApi: () => Cr,
          }));
        var r = {};
        (a.r(r),
          a.d(r, {
            Area: () => en,
            Bar: () => Qr,
            Default: () => Jr,
            useVerticalScrollApi: () => Ir,
          }));
        var n = a(6179),
          s = a.n(n);
        const o = (e, t, a) =>
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
        var i = a(3138);
        const l = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
        var c;
        function _(e, t, a) {
          const u = (function (e, t) {
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
            n = Math.min(u, r);
          return {
            extraLarge: n === a.extraLarge.weight,
            large: n === a.large.weight,
            medium: n === a.medium.weight,
            small: n === a.small.weight,
            extraSmall: n === a.extraSmall.weight,
            extraLargeWidth: u === a.extraLarge.weight,
            largeWidth: u === a.large.weight,
            mediumWidth: u === a.medium.weight,
            smallWidth: u === a.small.weight,
            extraSmallWidth: u === a.extraSmall.weight,
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
        const d = i.O.client.getSize("rem"),
          m = d.width,
          E = d.height,
          g = Object.assign({ width: m, height: E }, _(m, E, l)),
          p = (0, n.createContext)(g),
          A = ["children"];
        const b = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                u,
                r = {},
                n = Object.keys(e);
              for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, A);
          const u = (0, n.useContext)(p),
            r = u.extraLarge,
            s = u.large,
            i = u.medium,
            l = u.small,
            c = u.extraSmall,
            _ = u.extraLargeWidth,
            d = u.largeWidth,
            m = u.mediumWidth,
            E = u.smallWidth,
            g = u.extraSmallWidth,
            b = u.extraLargeHeight,
            h = u.largeHeight,
            C = u.mediumHeight,
            v = u.smallHeight,
            f = u.extraSmallHeight,
            D = { extraLarge: b, large: h, medium: C, small: v, extraSmall: f };
          if (a.extraLarge || a.large || a.medium || a.small || a.extraSmall) {
            if (a.extraLarge && r) return t;
            if (a.large && s) return t;
            if (a.medium && i) return t;
            if (a.small && l) return t;
            if (a.extraSmall && c) return t;
          } else {
            if (a.extraLargeWidth && _) return o(t, a, D);
            if (a.largeWidth && d) return o(t, a, D);
            if (a.mediumWidth && m) return o(t, a, D);
            if (a.smallWidth && E) return o(t, a, D);
            if (a.extraSmallWidth && g) return o(t, a, D);
            if (!(
              a.extraLargeWidth ||
              a.largeWidth ||
              a.mediumWidth ||
              a.smallWidth ||
              a.extraSmallWidth
            )) {
              if (a.extraLargeHeight && b) return t;
              if (a.largeHeight && h) return t;
              if (a.mediumHeight && C) return t;
              if (a.smallHeight && v) return t;
              if (a.extraSmallHeight && f) return t;
            }
          }
          return null;
        };
        b.defaultProps = {
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
        (0, n.memo)(b);
        const h = (e) => {
            const t = (0, n.useRef)(!1);
            t.current || (e(), (t.current = !0));
          },
          C = (0, n.memo)(({ children: e }) => {
            const t = (0, n.useContext)(p),
              a = (0, n.useState)(t),
              u = a[0],
              r = a[1],
              o = (0, n.useCallback)((e, t) => {
                const a = i.O.view.pxToRem(e),
                  u = i.O.view.pxToRem(t);
                r(Object.assign({ width: a, height: u }, _(a, u, l)));
              }, []);
            (h(() => {
              engine.on("clientResized", o);
            }),
              (0, n.useEffect)(() => () => engine.off("clientResized", o), [o]));
            const c = (0, n.useMemo)(() => Object.assign({}, u), [u]);
            return s().createElement(p.Provider, { value: c }, e);
          });
        var v = a(6483),
          f = a.n(v),
          D = a(926),
          B = a.n(D);
        let F, w, S;
        (!(function (e) {
          ((e[(e.ExtraSmall = l.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = l.small.width)] = "Small"),
            (e[(e.Medium = l.medium.width)] = "Medium"),
            (e[(e.Large = l.large.width)] = "Large"),
            (e[(e.ExtraLarge = l.extraLarge.width)] = "ExtraLarge"));
        })(F || (F = {})),
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
        const P = () => {
            const e = (0, n.useContext)(p),
              t = e.width,
              a = e.height,
              u = ((e) => {
                switch (!0) {
                  case e.extraLarge:
                    return F.ExtraLarge;
                  case e.large:
                    return F.Large;
                  case e.medium:
                    return F.Medium;
                  case e.small:
                    return F.Small;
                  case e.extraSmall:
                    return F.ExtraSmall;
                  default:
                    return (console.error("Unreachable media context resolution"), F.ExtraSmall);
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
              mediaSize: u,
              mediaWidth: r,
              mediaHeight: s,
              remScreenWidth: t,
              remScreenHeight: a,
            };
          },
          y = ["children", "className"];
        function k() {
          return (
            (k =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            k.apply(this, arguments)
          );
        }
        const x = {
            [w.ExtraSmall]: "",
            [w.Small]: B().SMALL_WIDTH,
            [w.Medium]: `${B().SMALL_WIDTH} ${B().MEDIUM_WIDTH}`,
            [w.Large]: `${B().SMALL_WIDTH} ${B().MEDIUM_WIDTH} ${B().LARGE_WIDTH}`,
            [w.ExtraLarge]: `${B().SMALL_WIDTH} ${B().MEDIUM_WIDTH} ${B().LARGE_WIDTH} ${B().EXTRA_LARGE_WIDTH}`,
          },
          N = {
            [S.ExtraSmall]: "",
            [S.Small]: B().SMALL_HEIGHT,
            [S.Medium]: `${B().SMALL_HEIGHT} ${B().MEDIUM_HEIGHT}`,
            [S.Large]: `${B().SMALL_HEIGHT} ${B().MEDIUM_HEIGHT} ${B().LARGE_HEIGHT}`,
            [S.ExtraLarge]: `${B().SMALL_HEIGHT} ${B().MEDIUM_HEIGHT} ${B().LARGE_HEIGHT} ${B().EXTRA_LARGE_HEIGHT}`,
          },
          L = {
            [F.ExtraSmall]: "",
            [F.Small]: B().SMALL,
            [F.Medium]: `${B().SMALL} ${B().MEDIUM}`,
            [F.Large]: `${B().SMALL} ${B().MEDIUM} ${B().LARGE}`,
            [F.ExtraLarge]: `${B().SMALL} ${B().MEDIUM} ${B().LARGE} ${B().EXTRA_LARGE}`,
          },
          T = (e) => {
            let t = e.children,
              a = e.className,
              u = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, y);
            const r = P(),
              n = r.mediaWidth,
              o = r.mediaHeight,
              i = r.mediaSize;
            return s().createElement("div", k({ className: f()(a, x[n], N[o], L[i]) }, u), t);
          },
          M = ["children"];
        const I = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                u,
                r = {},
                n = Object.keys(e);
              for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, M);
          return s().createElement(C, null, s().createElement(T, a, t));
        };
        var O = a(493),
          H = a.n(O);
        const W = (e) => {
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
        var G = a(5521),
          $ = a(4179);
        const U = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function z(e = G.n.NONE, t = U, a = !1) {
          (0, n.useEffect)(() => {
            if (e !== G.n.NONE)
              return (
                window.addEventListener("keydown", u, a),
                () => {
                  window.removeEventListener("keydown", u, a);
                }
              );
            function u(u) {
              if (u.keyCode === e) {
                if (i.O.view.isEventHandled()) return;
                (i.O.view.setEventHandled(), t(u), a && u.stopPropagation());
              }
            }
          }, [t, e, a]);
        }
        var V = a(7902);
        const j = (e, t) => e.split(".").reduce((e, t) => e && e[t], t),
          X = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          Y = (e, t) => (e.length > 0 ? `${e}.${t}` : t),
          q = (e) =>
            ((e, t) =>
              e.split(".").reduce((e, a) => {
                const u = j(`${e}.${a}`, window);
                return X(u) ? t(e, a, u) : `${e}.${a}`;
              }))(e, (e, t) => `${e}.${t}.value`),
          K = (e) => {
            const t = ((e) => {
                const t = (0, V.F)(),
                  a = t.caller,
                  u = t.resId,
                  r = window.__feature && window.__feature !== a && a ? `subViews.${a}` : "";
                return { modelPrefix: r, modelPath: Y(r, e || ""), resId: u };
              })(),
              a = t.modelPrefix,
              u = e.split(".");
            if (u.length > 0) {
              const e = [u[0]];
              return (
                u.reduce((t, u) => {
                  const r = j(Y(a, `${t}.${u}`), window);
                  return X(r) ? (e.push(r.id), `${t}.${u}.value`) : (e.push(u), `${t}.${u}`);
                }),
                e.reduce((e, t) => e + "." + t)
              );
            }
            return "";
          },
          Q = $.Sw.instance;
        let Z;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(Z || (Z = {}));
        const J = (e = "model", t = Z.Deep) => {
          const a = (0, n.useState)(0),
            u = (a[0], a[1]),
            r = (0, n.useMemo)(() => (0, V.F)(), []),
            s = r.caller,
            o = r.resId,
            i = (0, n.useMemo)(
              () => (window.__feature && window.__feature !== s ? `subViews.${s}.${e}` : e),
              [s, e],
            ),
            l = (0, n.useState)(() =>
              ((e) => {
                const t = j(e, window);
                for (const e in t) "function" == typeof t[e] && (t[e] = t[e].bind(t));
                return X(t) ? t.value : t;
              })(q(i)),
            ),
            c = l[0],
            _ = l[1],
            d = (0, n.useRef)(-1);
          return (
            h(() => {
              if (
                ("boolean" == typeof t &&
                  ((t = t ? Z.Deep : Z.None),
                  console.warn(
                    'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                  )),
                t !== Z.None)
              ) {
                const a = (e) => {
                    ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                    t === Z.Deep
                      ? (e === c && u((e) => e + 1), _(e))
                      : _(Object.assign([], e));
                  },
                  r = K(e);
                d.current = Q.addCallback(r, a, o, t === Z.Deep);
              }
            }),
            (0, n.useEffect)(() => {
              if (t !== Z.None)
                return () => {
                  Q.removeCallback(d.current, o);
                };
            }, [o, t]),
            c
          );
        };
        var ee = a(7727),
          te = a(3403);
        var ae = a(3649);
        const ue = "BattlePassOffSeasonViewContent_base_a5",
          re = "BattlePassOffSeasonViewContent_content_17",
          ne = "BattlePassOffSeasonViewContent_background_5f",
          se = "BattlePassOffSeasonViewContent_backgroundFade_3d",
          oe = "BattlePassOffSeasonViewContent_header_66",
          ie = "BattlePassOffSeasonViewContent_title_e9",
          le = "BattlePassOffSeasonViewContent_date_7c",
          ce = "BattlePassOffSeasonViewContent_stats_c1",
          _e = "BattlePassOffSeasonViewContent_subTitle_19",
          de = "BattlePassOffSeasonViewContent_levelLabel_0a",
          me = "BattlePassOffSeasonViewContent_levelLabel__disabled_8f",
          Ee = "BattlePassOffSeasonViewContent_footerLabel_e8";
        var ge = a(6373);
        function pe() {
          return !1;
        }
        console.log;
        var Ae = a(9174);
        function be(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return he(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return he(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var u = 0;
            return function () {
              return u >= e.length ? { done: !0 } : { done: !1, value: e[u++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function he(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, u = new Array(t); a < t; a++) u[a] = e[a];
          return u;
        }
        const Ce = (e) => (0 === e ? window : window.subViews.get(e));
        function ve(e, t) {
          var a;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (a = e[t]) ? void 0 : a.value;
        }
        function fe(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, a, u) => t(null == e ? void 0 : e.value, a, u));
        }
        const De = (e) =>
          null !== e && "object" == typeof e
            ? "CoherentArrayProxy" === e.constructor.name
              ? fe(e, (e) => ("object" == typeof e ? De(e) : e))
              : Array.isArray(e)
                ? e.map((e) => ("object" == typeof e ? De(e) : e))
                : Object.fromEntries(
                    Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? De(t) : t]),
                  )
            : e;
        var Be = a(3946);
        const Fe = ((e, t) => {
            const a = (0, n.createContext)({});
            return [
              function ({ mode: u = "real", options: r, children: o, mocks: l }) {
                const c = (0, n.useRef)([]),
                  _ = (a, u, r) => {
                    var n;
                    const s = (function ({
                        initializer: e = !0,
                        rootId: t = 0,
                        getRoot: a = Ce,
                        context: u = "model",
                      } = {}) {
                        const r = new Map();
                        function n(e, t = 0) {
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
                            n = u.split(".").reduce((e, t) => e[t], r);
                          return "string" != typeof e || 0 === e.length
                            ? n
                            : e.split(".").reduce((e, t) => {
                                const a = e[t];
                                return "function" == typeof a ? a.bind(e) : a;
                              }, n);
                        };
                        return {
                          subscribe: (a, n) => {
                            const o = "string" == typeof n ? `${u}.${n}` : u,
                              l = i.O.view.addModelObserver(o, t, !0);
                            return (r.set(l, a), e && a(s(n)), l);
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
                            for (var e, a = be(r.keys()); !(e = a()).done;) n(e.value, t);
                          },
                          unsubscribe: n,
                        };
                      })(u),
                      o =
                        "real" === a
                          ? s
                          : Object.assign({}, s, {
                              readByPath:
                                null != (n = null == r ? void 0 : r.getter) ? n : () => {},
                            }),
                      l = (e) =>
                        "mocks" === a ? (null == r ? void 0 : r.getter(e)) : o.readByPath(e),
                      _ = (e) => c.current.push(e),
                      d = e({
                        mode: a,
                        readByPath: l,
                        externalModel: o,
                        observableModel: {
                          array: (e, t) => {
                            const u = null != t ? t : l(e),
                              r = Ae.LO.box(u, { equals: pe });
                            return (
                              "real" === a &&
                                o.subscribe(
                                  (0, Ae.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, t) => {
                            const u = null != t ? t : l(e),
                              r = Ae.LO.box(u, { equals: pe });
                            return (
                              "real" === a &&
                                o.subscribe(
                                  (0, Ae.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, t) => {
                            const u = l(t);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, t) => ((e[t] = Ae.LO.box(u[t], {})), e), {});
                              return (
                                "real" === a &&
                                  o.subscribe(
                                    (0, Ae.aD)((t) => {
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
                                n = Object.entries(r),
                                s = n.reduce((e, [t, a]) => ((e[a] = Ae.LO.box(u[t], {})), e), {});
                              return (
                                "real" === a &&
                                  o.subscribe(
                                    (0, Ae.aD)((e) => {
                                      n.forEach(([t, a]) => {
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
                        cleanup: _,
                      }),
                      m = { mode: a, model: d, externalModel: o, cleanup: _ };
                    return {
                      model: d,
                      controls: "mocks" === a && r ? r.controls(m) : t(m),
                      externalModel: o,
                      mode: a,
                    };
                  },
                  d = (0, n.useRef)(!1),
                  m = (0, n.useState)(u),
                  E = m[0],
                  g = m[1],
                  p = (0, n.useState)(() => _(u, r, l)),
                  A = p[0],
                  b = p[1];
                return (
                  (0, n.useEffect)(() => {
                    d.current ? b(_(E, r, l)) : (d.current = !0);
                  }, [l, E, r]),
                  (0, n.useEffect)(() => {
                    g(u);
                  }, [u]),
                  (0, n.useEffect)(
                    () => () => {
                      (A.externalModel.dispose(), c.current.forEach((e) => e()));
                    },
                    [A],
                  ),
                  s().createElement(a.Provider, { value: A }, o)
                );
              },
              () => (0, n.useContext)(a),
            ];
          })(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  extraChapterWidget: e.object("widget3dStyle"),
                  extraChapterVehicleRewardInfo: e.object("widget3dStyle.vehicle"),
                  availableChapterTypes: e.array("availableChapterTypes"),
                  levels: e.array("levels.items"),
                  freeRewardItems: e.array("levels.items.freeRewardItems"),
                  paidRewardItems: e.array("levels.items.paidRewardItems"),
                  collectionEntryPoint: e.object("collectionEntryPoint"),
                  chapterCharacter: e.object("chapterCharacter"),
                  chapterCharacterSkills: e.array("chapterCharacter.skills"),
                  widget3dStyle: e.object("widget3dStyle"),
                  vehicleInfo: e.object("widget3dStyle.vehicle.vehicleInfo"),
                  availableBattleTypes: e.array("availableBattleTypes"),
                  offSeason: e.object("offSeason"),
                },
                a = (0, Be.Om)(() => fe(t.levels.get(), (e) => e), { equals: pe }),
                u = (0, Be.Om)(
                  (e) => {
                    const t = ve(a(), e);
                    if (t) return fe(t.freeRewardItems.items, (e) => Object.assign({}, e));
                  },
                  { equals: pe },
                ),
                r = (0, Be.Om)(
                  (e) => {
                    const t = ve(a(), e);
                    if (t) return fe(t.paidRewardItems.items, (e) => Object.assign({}, e));
                  },
                  { equals: pe },
                ),
                n = (0, Be.Om)(
                  (e) =>
                    (function (e, t) {
                      if (Array.isArray(e)) return e.filter(t);
                      const a = [];
                      for (let r = 0; r < e.length; r++) {
                        var u;
                        const n = null == (u = e[r]) ? void 0 : u.value;
                        t(n, r, e) && a.push(n);
                      }
                      return a;
                    })(t.availableChapterTypes.get(), (t) => t === e).length > 0,
                  { equals: pe },
                ),
                s = (0, Be.Om)(() => fe(t.levels.get(), (e) => e), { equals: pe }),
                o = (0, Be.Om)(() => fe(t.chapterCharacterSkills.get(), (e) => e), { equals: pe }),
                i = (0, Be.Om)(() => t.levels.get().length),
                l = (0, Be.Om)(() => fe(t.availableBattleTypes.get(), (e) => e), { equals: pe }),
                c = (0, Be.Om)(
                  () => {
                    const e = t.extraChapterWidget.get();
                    return {
                      styleName: e.styleName,
                      styleId: e.styleId,
                      isPaidReward: e.isPaidReward,
                    };
                  },
                  { equals: pe },
                ),
                _ = (0, Be.Om)(
                  () => {
                    return ((e = t.extraChapterVehicleRewardInfo.get()), De(e));
                    var e;
                  },
                  { equals: pe },
                );
              return Object.assign({}, t, {
                computes: {
                  hasChapter: n,
                  getLevels: s,
                  getLevelsLength: i,
                  getCharacterSkills: o,
                  getAvailableBattleTypes: l,
                  getLevelsItems: a,
                  getFreeRewardItems: u,
                  getPaidRewardItems: r,
                  getStyleInfoExtraChapterWidget: c,
                  getExtraChapterRewardInfo: _,
                },
              });
            },
            ({ externalModel: e }) => ({
              onClose: e.createCallbackNoArgs("onClose"),
              onViewLoaded: e.createCallbackNoArgs("onViewLoaded"),
              onChapterChoice: e.createCallbackNoArgs("onChapterChoice"),
              openPreview: e.createCallbackNoArgs("widget3dStyle.onMarathonPreviewClick"),
              onSound: e.createCallbackNoArgs("widget3dStyle.onSoundClick"),
              onAbout: e.createCallbackNoArgs("onAboutClick"),
              onPointsInfo: e.createCallbackNoArgs("onPointsInfoClick"),
              onBpcoin: e.createCallbackNoArgs("onBpcoinClick"),
              onBpbit: e.createCallbackNoArgs("onBpbitClick"),
              onTakeRewards: e.createCallbackNoArgs("onTakeRewardsClick"),
              openCollection: e.createCallbackNoArgs("collectionEntryPoint.openCollection"),
              onAction: e.createCallbackNoArgs("onActionClick"),
              onBuyBP: e.createCallbackNoArgs("onBuyBP"),
              onBuyStages: e.createCallbackNoArgs("onBuyStages"),
              on3dStylePreview: e.createCallback((e) => e, "widget3dStyle.onPreviewClick"),
              onFinishedAnimation: e.createCallbackNoArgs("onFinishedAnimation"),
              onTake: e.createCallback((e) => e, "onTakeClick"),
              onLevelsAnimationFinished: e.createCallbackNoArgs("onLevelsAnimationFinished"),
              onTasks: e.createCallbackNoArgs("onTasksClick"),
            }),
          ),
          we = Fe[0],
          Se = Fe[1],
          Pe = {
            base: "Label_base_85",
            textWithBlend: "Label_textWithBlend_07",
            textWithBlend__show: "Label_textWithBlend__show_fa",
            show: "Label_show_69",
            textWithBlend__new: "Label_textWithBlend__new_4a",
            textWithBlend__hide: "Label_textWithBlend__hide_f1",
            hide: "Label_hide_33",
            textMask: "Label_textMask_7f",
            textMask__animated: "Label_textMask__animated_38",
            maskAppearance: "Label_maskAppearance_26",
            textMask__micro: "Label_textMask__micro_37",
            textMask__small: "Label_textMask__small_54",
            textMask__medium: "Label_textMask__medium_eb",
            textMask__large: "Label_textMask__large_0a",
            textMask__extraLarge: "Label_textMask__extraLarge_4c",
            text: "Label_text_67",
            text__micro: "Label_text__micro_a4",
            text__small: "Label_text__small_e0",
            text__large: "Label_text__large_65",
            text__extraLarge: "Label_text__extraLarge_22",
            text__blended: "Label_text__blended_67",
            text__filtered: "Label_text__filtered_86",
            text__rewardScreen: "Label_text__rewardScreen_68",
            textAppearance: "Label_textAppearance_31",
            text__show: "Label_text__show_95",
            text__hide: "Label_text__hide_37",
            text__hideWithDelay: "Label_text__hideWithDelay_53",
            text__new: "Label_text__new_a0",
            hideLevel: "Label_hideLevel_61",
            showLevel: "Label_showLevel_55",
            hideLevelSmall: "Label_hideLevelSmall_9d",
            showLevelSmall: "Label_showLevelSmall_96",
            hideLevelMicro: "Label_hideLevelMicro_9e",
            showLevelMicro: "Label_showLevelMicro_50",
            showIcon: "Label_showIcon_0f",
            showIconSmall: "Label_showIconSmall_96",
            hideProgress: "Label_hideProgress_0c",
            showIconMicro: "Label_showIconMicro_1e",
          },
          ye = "R.images.gui.maps.icons.battlePass.logo",
          ke = R.images.gui.maps.icons.battlePass.logo,
          xe = (e, t, a) => {
            if (e && t) {
              const e = `c_${a}_font_texture_gold_contrast`;
              return ke.$dyn(e) ? `url(${ye}.${e})` : `url(${ye}.font_texture_gold_contrast)`;
            }
            if (e) {
              const e = `c_${a}_font_texture_gold`;
              return ke.$dyn(e) ? `url(${ye}.${e})` : `url(${ye}.font_texture_gold)`;
            }
            const u = `c_${a}_font_texture`;
            return ke.$dyn(u) ? `url(${ye}.${u})` : `url(${ye}.font_texture)`;
          },
          Re = (0, n.memo)(
            ({
              level: e,
              size: t,
              isGold: a,
              isForRewardScreen: u = !1,
              curState: r,
              isFirstLevel: n,
              showProgressionCompleted: o,
              chapterID: i = 0,
            }) => {
              const l = f()(Pe.base, Pe[`base__${t}`]),
                c = f()(
                  Pe.text,
                  Pe.text__filtered,
                  Pe[`text__${t}`],
                  Pe[`text__${r}`],
                  o && Pe.text__hideWithDelay,
                  n && Pe.text__new,
                  u && Pe.text__rewardScreen,
                ),
                _ = f()(
                  Pe.textWithBlend,
                  n && Pe.text__new,
                  o && Pe.text__hideWithDelay,
                  Pe[`textWithBlend__${r}`],
                ),
                d = f()(Pe.text, Pe.text__blended, Pe[`text__${t}`], u && Pe.text__rewardScreen),
                m = f()(Pe.textMask, u && Pe.textMask__animated, Pe[`textMask__${t}`]);
              return s().createElement(
                "div",
                { className: l },
                s().createElement("div", { className: c }, e),
                s().createElement(
                  "div",
                  { className: _ },
                  s().createElement("div", { className: d }, e),
                  s().createElement("div", {
                    className: m,
                    style: { backgroundImage: xe(a, u, i) },
                  }),
                ),
              );
            },
          ),
          Ne = "SeasonEmblem_base_de",
          Le = "SeasonEmblem_emblem_82",
          Te = "SeasonEmblem_emblem__hasBP_55",
          Me = (0, n.memo)(({ level: e, hasBattlePass: t, isEnabled: a }) => {
            const u = f()(Le, t && Te);
            return s().createElement(
              "div",
              { className: Ne },
              s().createElement(
                "div",
                { className: u },
                s().createElement(Re, { level: a ? e : 1, size: "extraLarge", isGold: t }),
              ),
            );
          }),
          Ie = "SeasonStatistics_base_e1",
          Oe = "SeasonStatistics_shineWrapper_36",
          He = "SeasonStatistics_imgShine_22",
          We = "SeasonStatistics_imgLines_8d",
          Ge = "SeasonStatistics_emblem_53",
          $e = "SeasonStatistics_emblem__disabled_12",
          Ue = "SeasonStatistics_stats_11",
          ze = "SeasonStatistics_stats__left_0c",
          Ve = "SeasonStatistics_stats__right_06",
          je = "SeasonStatistics_statsBg_aa",
          Xe = "SeasonStatistics_statsBg__right_00",
          Ye = "SeasonStatistics_statsLabel_2d",
          qe = "SeasonStatistics_statsContainer_d0",
          Ke = "SeasonStatistics_statsValue_07",
          Qe = "SeasonStatistics_alertIcon_15",
          Ze = "---",
          Je = R.strings.battle_pass.offSeason,
          et = (e) => (0 === e ? Ze : $.Z5.getNumberFormat(e, $.B3.INTEGRAL)),
          tt = (0, te.Pi)(() => {
            const e = Se().model.offSeason.get(),
              t = e.isEnabled,
              a = e.leftVehicle,
              u = e.leftPoints,
              r = e.rightVehicle,
              n = e.rightPoints,
              o = e.isFailedService,
              i = e.level,
              l = e.hasBattlePass,
              c = f()([Ge, { [$e]: !t }]),
              _ = (0, ae.uF)(Je.sideChosen(), { vehicle: a }),
              d = (0, ae.uF)(Je.sideChosen(), { vehicle: r }),
              m = ((e, t) =>
                e ? { left: Ze, right: Ze } : { left: et(t.left), right: et(t.right) })(o, {
                left: u,
                right: n,
              }),
              E = f()(Ue, ze),
              g = f()(Ue, Ve),
              p = f()(je, Xe),
              A = Je.alertTooltip();
            return s().createElement(
              "div",
              { className: Ie },
              t &&
                s().createElement(
                  "div",
                  { className: Oe },
                  s().createElement("div", { className: He }),
                ),
              s().createElement("div", { className: We }),
              s().createElement(
                "div",
                { className: E },
                s().createElement("div", { className: je }),
                s().createElement("div", { className: Ye }, _),
                s().createElement(
                  "div",
                  { className: qe },
                  o &&
                    s().createElement(
                      ge.i,
                      { body: A },
                      s().createElement("div", { className: Qe }),
                    ),
                  s().createElement("div", { className: Ke }, m.left),
                ),
              ),
              s().createElement(
                "div",
                { className: g },
                s().createElement("div", { className: p }),
                s().createElement("div", { className: Ye }, d),
                s().createElement(
                  "div",
                  { className: qe },
                  s().createElement("div", { className: Ke }, m.right),
                  o &&
                    s().createElement(
                      ge.i,
                      { body: A },
                      s().createElement("div", { className: Qe }),
                    ),
                ),
              ),
              s().createElement(
                "div",
                { className: c },
                s().createElement(Me, { level: i, hasBattlePass: l, isEnabled: t }),
              ),
            );
          }),
          at = R.strings.battle_pass.offSeason,
          ut = { loseVote: at.footerLose(), winVote: at.footerWin(), notVote: "" },
          rt = () => {
            const e = J("model.offSeason"),
              t = e.level,
              a = e.isEnabled,
              u = e.seasonName,
              r = e.voteStatus,
              n = f()(de, !a && me),
              o = a ? (0, ae.uF)(at.levelReached(), { level: t }) : at.noProgress(),
              i = ut[r];
            return s().createElement(
              "div",
              { className: ue },
              s().createElement("div", { className: ne }),
              s().createElement("div", { className: se }),
              s().createElement(
                "div",
                { className: oe },
                s().createElement("div", { className: ie }, u),
                s().createElement("div", { className: le }, at.finished()),
              ),
              s().createElement(
                "div",
                { className: re },
                s().createElement("div", { className: ce }, s().createElement(tt, null)),
                s().createElement("div", { className: n }, o),
              ),
              s().createElement("div", { className: _e }, at.startsSoon()),
              s().createElement("div", { className: Ee }, i),
            );
          },
          nt = {
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
          st = [
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
        function ot() {
          return (
            (ot =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            ot.apply(this, arguments)
          );
        }
        class it extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, ee.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, ee.G)(this.props.soundClick));
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
              u = e.goto,
              r = e.side,
              n = e.type,
              o = e.classNames,
              i = e.onMouseEnter,
              l = e.onMouseLeave,
              c = e.onMouseDown,
              _ = e.onMouseUp,
              d =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var a,
                    u,
                    r = {},
                    n = Object.keys(e);
                  for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                  return r;
                })(e, st)),
              m = f()(nt.base, nt[`base__${n}`], nt[`base__${r}`], null == o ? void 0 : o.base),
              E = f()(nt.icon, nt[`icon__${n}`], nt[`icon__${r}`], null == o ? void 0 : o.icon),
              g = f()(nt.glow, null == o ? void 0 : o.glow),
              p = f()(nt.caption, nt[`caption__${n}`], null == o ? void 0 : o.caption),
              A = f()(nt.goto, null == o ? void 0 : o.goto);
            return s().createElement(
              "div",
              ot(
                {
                  className: m,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(l),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: a,
                },
                d,
              ),
              "info" !== n && s().createElement("div", { className: nt.shine }),
              s().createElement(
                "div",
                { className: E },
                s().createElement("div", { className: g }),
              ),
              s().createElement("div", { className: p }, t),
              u && s().createElement("div", { className: A }, u),
            );
          }
        }
        let lt, ct, _t, dt, mt, Et, gt;
        ((it.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        }),
          (function (e) {
            ((e.Active = "active"),
              (e.Paused = "paused"),
              (e.Completed = "completed"),
              (e.NotStarted = "notStarted"),
              (e.Disabled = "disabled"));
          })(lt || (lt = {})),
          (function (e) {
            ((e.Hide = "hide"), (e.Buy = "buy"), (e.Level = "level"), (e.Activate = "activate"));
          })(ct || (ct = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(_t || (_t = {})),
          (function (e) {
            ((e.Micro = "micro"), (e.Small = "small"), (e.Medium = "medium"));
          })(dt || (dt = {})),
          (function (e) {
            ((e.ACTIVE = "active"), (e.COMPLETED = "completed"), (e.NOT_CHOSEN = "notChosen"));
          })(mt || (mt = {})),
          (function (e) {
            ((e.AwaitSeason = "awaitSeason"),
              (e.Bought = "bought"),
              (e.Free = "free"),
              (e.Completed = "completed"),
              (e.CompletedRightNow = "completedRightNow"),
              (e.SwitchedChapterRightNow = "switchedChapterRightNow"),
              (e.NoVehiclesBase = "noVehiclesBase"),
              (e.ChapterNotChosen = "chapterNotChosen"));
          })(Et || (Et = {})),
          (function (e) {
            ((e.None = ""),
              (e.ShowLevel = "show"),
              (e.HideLevel = "hide"),
              (e.HideLevelWithDelay = "hideWithDelay"));
          })(gt || (gt = {})));
        const pt = (e) => {
            switch (e) {
              case dt.Micro:
                return "s";
              case dt.Small:
                return "m";
              default:
                return "l";
            }
          },
          At = (e, t, a = "") => {
            const u = a.length > 0 ? `_${a}` : a,
              r = e.$dyn(`c_${t}${u}`),
              n = e.$dyn(`common${u}`);
            return r || n;
          },
          bt = (e, t = dt.Medium) => {
            const a = R.images.gui.maps.icons.battlePass.backgrounds,
              u = pt(t);
            return { backgroundImage: `url(${At(a.chapter, e, u)})` };
          };
        let ht, Ct;
        (!(function (e) {
          ((e.style = "style"),
            (e.tankman = "tankman"),
            (e.vehicle = "vehicle"),
            (e.mixed = "mixed"));
        })(ht || (ht = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(Ct || (Ct = {})));
        (ht.style, ht.tankman);
        const vt = {
          base: "BattlePassProgressionsViewContent_base_67",
          background: "BattlePassProgressionsViewContent_background_f0",
          header: "BattlePassProgressionsViewContent_header_76",
          headerGlow: "BattlePassProgressionsViewContent_headerGlow_c0",
          progression: "BattlePassProgressionsViewContent_progression_7c",
          progression__marathon: "BattlePassProgressionsViewContent_progression__marathon_3e",
          base__buttonVisible: "BattlePassProgressionsViewContent_base__buttonVisible_67",
          extraChapterWidget: "BattlePassProgressionsViewContent_extraChapterWidget_e2",
          footer: "BattlePassProgressionsViewContent_footer_13",
          close: "BattlePassProgressionsViewContent_close_69",
        };
        var ft = a(9887),
          Dt = a.n(ft);
        const Bt = ["xl", "lg", "md", "sm", "xs"],
          Ft = (e) => e.includes("_") && ((e) => Bt.includes(e))(e.split("_").at(-1)),
          wt = [F.ExtraLarge, F.Large, F.Medium, F.Small, F.ExtraSmall],
          St = (e, t) =>
            Object.keys(e).reduce((a, u) => {
              if (u in a) return a;
              if (Ft(u)) {
                const r = u.split("_").slice(0, -1).join("_");
                if (r in a) return a;
                const n = wt.indexOf(t),
                  s = (-1 !== n ? Bt.slice(n) : [])
                    .map((e) => r + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  o = s ? e[s] : void 0;
                return ((a[r] = void 0 !== o ? o : e[r]), a);
              }
              const r = e[u];
              return (
                void 0 === r ||
                  ((e, t) => Bt.some((a) => void 0 !== t[`${e}_${a}`]))(u, e) ||
                  (a[u] = r),
                a
              );
            }, {}),
          Pt = (e, t = St) => {
            const a = (
              (e, t = St) =>
              (a) => {
                const u = P().mediaSize,
                  r = (0, n.useMemo)(() => t(a, u), [a, u]);
                return s().createElement(e, r);
              }
            )(e, t);
            return s().memo((t) =>
              Object.keys(t).some((e) => Ft(e) && void 0 !== t[e])
                ? s().createElement(a, t)
                : s().createElement(e, t),
            );
          },
          yt = {
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
          kt = [
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
        function xt() {
          return (
            (xt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            xt.apply(this, arguments)
          );
        }
        Object.keys(Dt());
        const Rt = {
            XL: { mt: yt.mt__XL, mr: yt.mr__XL, mb: yt.mb__XL, ml: yt.ml__XL },
            LG: { mt: yt.mt__LG, mr: yt.mr__LG, mb: yt.mb__LG, ml: yt.ml__LG },
            MDp: { mt: yt.mt__MDp, mr: yt.mr__MDp, mb: yt.mb__MDp, ml: yt.ml__MDp },
            MD: { mt: yt.mt__MD, mr: yt.mr__MD, mb: yt.mb__MD, ml: yt.ml__MD },
            SMp: { mt: yt.mt__SMp, mr: yt.mr__SMp, mb: yt.mb__SMp, ml: yt.ml__SMp },
            SM: { mt: yt.mt__SM, mr: yt.mr__SM, mb: yt.mb__SM, ml: yt.ml__SM },
            XS: { mt: yt.mt__XS, mr: yt.mr__XS, mb: yt.mb__XS, ml: yt.ml__XS },
          },
          Nt = (Object.keys(Rt), ["mt", "mr", "mb", "ml"]),
          Lt = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Tt = Pt((e) => {
            let t = e.className,
              a = e.width,
              u = e.height,
              r = e.m,
              o = e.mt,
              i = void 0 === o ? r : o,
              l = e.mr,
              c = void 0 === l ? r : l,
              _ = e.mb,
              d = void 0 === _ ? r : _,
              m = e.ml,
              E = void 0 === m ? r : m,
              g = e.column,
              p = e.row,
              A = e.flexDirection,
              b = void 0 === A ? (g ? "column" : p && "row") || void 0 : A,
              h = e.flexStart,
              C = e.center,
              v = e.flexEnd,
              D = e.spaceBetween,
              B = e.spaceAround,
              F = e.justifyContent,
              w =
                void 0 === F
                  ? (h ? "flex-start" : C && "center") ||
                    (v && "flex-end") ||
                    (D && "space-between") ||
                    (B && "space-around") ||
                    void 0
                  : F,
              S = e.alignItems,
              P =
                void 0 === S
                  ? (h ? "flex-start" : C && "center") || (v && "flex-end") || void 0
                  : S,
              y = e.alignSelf,
              k = e.wrap,
              x = e.flexWrap,
              R = void 0 === x ? (k ? "wrap" : void 0) : x,
              N = e.grow,
              L = e.shrink,
              T = e.flex,
              M = void 0 === T ? (N || L ? `${N ? 1 : 0} ${L ? 1 : 0} auto` : void 0) : T,
              I = e.style,
              O = e.children,
              H = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, kt);
            const W = (0, n.useMemo)(() => {
                const e = { mt: i, mr: c, mb: d, ml: E },
                  t = ((e) =>
                    Nt.reduce((t, a) => {
                      const u = e[a];
                      return u && "number" != typeof u ? t.concat(Rt[!0 === u ? "MD" : u][a]) : t;
                    }, []))(e),
                  r = ((e) =>
                    Nt.reduce((t, a) => {
                      const u = e[a];
                      return ("number" == typeof u && (t[Lt[a]] = u + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, I, r, {
                    width: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    height: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    flex: M,
                    alignSelf: y,
                    display: b || P ? "flex" : void 0,
                    flexDirection: b,
                    flexWrap: R,
                    justifyContent: w,
                    alignItems: P,
                  }),
                  computedClassNames: t,
                };
              }, [a, u, i, c, d, E, I, M, y, b, R, w, P]),
              G = W.computedStyle,
              $ = W.computedClassNames;
            return s().createElement(
              "div",
              xt({ className: f()(yt.base, ...$, t), style: G }, H),
              O,
            );
          });
        var Mt = a(280),
          It = a(3532),
          Ot = a.n(It);
        const Ht = {
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
          Wt = [
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
        function Gt() {
          return (
            (Gt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            Gt.apply(this, arguments)
          );
        }
        Object.keys(Dt());
        const $t = Object.keys(Ot()),
          Ut = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          zt = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Vt = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          jt = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Xt =
            (Object.keys(jt),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ut,
              "heading-H36": Ut,
              "heading-H28": zt,
              "heading-H24": zt,
              "heading-H24R": zt,
              "heading-H22": zt,
              "heading-H20R": zt,
              "heading-H18": zt,
              "heading-H15": Vt,
              "heading-H14": Vt,
              "paragraph-P24": zt,
              "paragraph-P18": zt,
              "paragraph-P16": zt,
              "paragraph-P14": Vt,
              "paragraph-P12": Vt,
              "paragraph-P10": Vt,
            }),
          Yt =
            (Object.keys(Xt),
            (e) =>
              e
                ? ((e) => $t.includes(e))(e)
                  ? { colorClassName: Ht[e] }
                  : { colorStyle: { color: e } }
                : {}),
          qt = Pt((e) => {
            let t = e.text,
              a = e.variant,
              u = e.className,
              r = e.color,
              o = e.m,
              i = e.mt,
              l = void 0 === i ? o : i,
              c = e.mr,
              _ = void 0 === c ? o : c,
              d = e.mb,
              m = void 0 === d ? o : d,
              E = e.ml,
              g = void 0 === E ? o : E,
              p = e.style,
              A = e.format,
              b = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Wt);
            const h = (0, n.useMemo)(() => {
                const e = Yt(r),
                  t = e.colorClassName,
                  a = e.colorStyle,
                  u = void 0 === a ? {} : a;
                return { computedStyle: Object.assign({}, p, u), colorClassName: t };
              }, [p, r]),
              C = h.computedStyle,
              v = h.colorClassName;
            return s().createElement(
              Tt,
              Gt(
                {
                  className: f()(Ht.base, a && Ht[a], v, u),
                  style: C,
                  mt: !0 === l ? Xt[a || "paragraph-P16"].mt : l,
                  mr: !0 === _ ? Xt[a || "paragraph-P16"].mr : _,
                  mb: !0 === m ? Xt[a || "paragraph-P16"].mb : m,
                  ml: !0 === g ? Xt[a || "paragraph-P16"].ml : g,
                },
                b,
              ),
              void 0 !== A ? s().createElement(Mt.z, Gt({}, A, { text: t })) : t,
            );
          });
        var Kt = a(2056);
        const Qt = "BonusQuest_base_98",
          Zt = "BonusQuest_subTitle_b1",
          Jt = "BonusQuest_subTitleTextWrapper_57",
          ea = "BonusQuest_subTitleText_b6",
          ta = "BonusQuest_infoIcon_d7";
        function aa(e, t, a, u, r, n, s) {
          try {
            var o = e[n](s),
              i = o.value;
          } catch (e) {
            return void a(e);
          }
          o.done ? t(i) : Promise.resolve(i).then(u, r);
        }
        function ua(e) {
          return function () {
            var t = this,
              a = arguments;
            return new Promise(function (u, r) {
              var n = e.apply(t, a);
              function s(e) {
                aa(n, u, r, s, o, "next", e);
              }
              function o(e) {
                aa(n, u, r, s, o, "throw", e);
              }
              s(void 0);
            });
          };
        }
        const ra = R.strings.battle_pass.progression.extraChapterWidget,
          na = (0, n.memo)(({ vehicleName: e, marathonRewardId: t }) => {
            const a = (0, n.useRef)(null),
              u = (0, n.useCallback)(
                ua(function* () {
                  yield (0, $.Eu)();
                  a.current;
                }),
                [],
              );
            var r;
            return (
              (r = () => (
                u(),
                engine.on("clientResized", u),
                () => {
                  engine.off("clientResized", u);
                }
              )),
              (0, n.useEffect)(r, []),
              s().createElement(
                "div",
                { className: Qt },
                t &&
                  s().createElement(
                    Kt.u,
                    {
                      contentId: R.views.lobby.battle_pass.tooltips.RandomQuestTooltip("resId"),
                      args: { tokenID: t },
                    },
                    s().createElement(
                      "div",
                      { className: Zt },
                      s().createElement(
                        "div",
                        { className: Jt },
                        s().createElement(
                          "div",
                          { className: ea, ref: a },
                          s().createElement(qt, {
                            text: ra.styleSubTitle(),
                            format: { binding: { vehicleName: e } },
                          }),
                        ),
                      ),
                      s().createElement("div", { className: ta }),
                    ),
                  ),
              )
            );
          }),
          sa = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          oa = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        function ia(e) {
          let t = "";
          for (let a = oa.length - 1; a >= 0; a--) for (; e >= oa[a];) ((t += sa[a]), (e -= oa[a]));
          return t;
        }
        ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE());
        const la = "VehicleInfo_base_45",
          ca = "VehicleInfo_type_2e",
          _a = ({ vehicleLvl: e, vehicleName: t, vehicleType: a, isElite: u, classNames: r }) =>
            s().createElement(
              "div",
              { className: f()(la, null == r ? void 0 : r.base) },
              ia(e),
              s().createElement("div", {
                className: f()(ca, null == r ? void 0 : r.type),
                style: {
                  backgroundImage: `url(${R.images.gui.maps.icons.vehicleTypes.big.$dyn(`${(0, ae.BN)(a)}${u ? "_elite" : ""}`)})`,
                },
              }),
              t,
            ),
          da = "RewardsList_base_6f",
          ma = "RewardsList_base__free_f9",
          Ea = "RewardsList_title_1e",
          ga = "RewardsList_tankman_fe",
          pa = "RewardsList_vehicle_b5",
          Aa = "RewardsList_caption_f5",
          ba = "RewardsList_caption__vehicle_6f",
          ha = "RewardsList_caption__style_f5",
          Ca = "RewardsList_bonusQuest_ee",
          va = "RewardsList_vehicleBg_6c",
          fa = "RewardsList_remark_2e",
          Da = "RewardsList_remark__hide_de",
          Ba = "RewardsList_lockIcon_36",
          Fa = R.strings.battle_pass.progression.extraChapterWidget,
          wa = (0, n.memo)(
            ({
              styleReward: e,
              vehicleReward: t,
              characterReward: a,
              isBattlePassPurchased: u,
              marathonRewardId: r,
              progressionQuestVehicleName: n,
              isPaidRewards: o = !1,
            }) => {
              const i = t.isPaidReward,
                l = t.vehicleInfo,
                c = l.vehicleType,
                _ = l.isElite,
                d = l.vehicleName,
                m = l.vehicleShortName,
                E = l.vehicleLvl,
                g = l.vehicleNation,
                p = e.styleName,
                A = e.isPaidReward,
                b = a.tankman,
                h = a.isPaidReward,
                C = P().mediaSize > F.Medium ? 14 : 12,
                v = d.length > C ? m : d,
                D = o === i && v,
                B = o === h && b,
                w = n && o,
                S = o === A && p,
                y = !u && o,
                k = { backgroundImage: `url(R.images.gui.maps.icons.flags.c_600x450.${g})` };
              return s().createElement(
                "div",
                { className: f()(da, !o && ma) },
                D &&
                  s().createElement(
                    s().Fragment,
                    null,
                    s().createElement("div", { className: va, style: k }),
                    s().createElement(
                      "div",
                      { className: pa },
                      s().createElement(qt, { text: Fa.vehicleCaption(), className: f()(Aa, ba) }),
                      s().createElement(_a, {
                        vehicleLvl: E,
                        vehicleName: v,
                        vehicleType: c,
                        isElite: _,
                      }),
                    ),
                  ),
                S &&
                  s().createElement(qt, {
                    className: f()(Aa, ha),
                    text: Fa.styleTitle(),
                    format: { binding: { styleName: p } },
                  }),
                B &&
                  s().createElement(
                    s().Fragment,
                    null,
                    s().createElement(qt, { text: Fa.characterVoice(), className: Ea }),
                    s().createElement(qt, { text: b, className: ga }),
                  ),
                w &&
                  s().createElement(
                    "div",
                    { className: Ca },
                    s().createElement(na, { vehicleName: v, marathonRewardId: r }),
                  ),
                o &&
                  s().createElement(
                    "div",
                    { className: f()(fa, !y && Da) },
                    s().createElement("div", { className: Ba }),
                    s().createElement("div", null, Fa.styleRemark()),
                  ),
              );
            },
          ),
          Sa = "ExtraChapterWidget_base_61",
          Pa = "ExtraChapterWidget_glow_e7",
          ya = "ExtraChapterWidget_separatorBg_ab",
          ka = {
            base: "Preview_base_1f",
            base__hovered: "Preview_base__hovered_ee",
            icon: "Preview_icon_f3",
            icon__small: "Preview_icon__small_a1",
            icon__normal: "Preview_icon__normal_5c",
            base__mouseDown: "Preview_base__mouseDown_d0",
            label: "Preview_label_2e",
            base__visibleLabel: "Preview_base__visibleLabel_92",
          },
          xa = [
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
        function Ra() {
          return (
            (Ra =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            Ra.apply(this, arguments)
          );
        }
        let Na;
        !(function (e) {
          ((e.SMALL = "small"), (e.NORMAL = "normal"));
        })(Na || (Na = {}));
        const La = (0, n.memo)((e) => {
            let t = e.label,
              a = e.isVisibleLabel,
              u = void 0 !== a && a,
              r = e.autofocus,
              o = void 0 !== r && r,
              i = e.soundHover,
              l = void 0 === i ? "highlight" : i,
              c = e.soundClick,
              _ = void 0 === c ? "play" : c,
              d = e.size,
              m = void 0 === d ? Na.NORMAL : d,
              E = e.classNames,
              g = e.onClick,
              p = e.onMouseEnter,
              A = e.onMouseLeave,
              b = e.onMouseDown,
              h = e.onMouseUp,
              C = e.onFocus,
              v = e.onBlur,
              D = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, xa);
            const B = (0, n.useState)(!1),
              F = B[0],
              w = B[1],
              S = (0, n.useState)(!1),
              P = S[0],
              y = S[1],
              k = (0, n.useState)(o),
              x = k[0],
              R = k[1],
              N = (0, n.useRef)(null),
              L = (0, n.useCallback)(() => {
                N.current && (N.current.focus(), R(!0));
              }, []),
              T = (0, n.useCallback)(
                (e) => {
                  x && null !== N.current && !N.current.contains(e.target) && R(!1);
                },
                [x],
              );
            ((0, n.useEffect)(
              () => (
                document.addEventListener("mousedown", T),
                () => {
                  document.removeEventListener("mousedown", T);
                }
              ),
              [T],
            ),
              (0, n.useEffect)(() => {
                R(o);
              }, [o]));
            const M = (0, n.useCallback)(
                (e) => {
                  g && g(e);
                },
                [g],
              ),
              I = (0, n.useCallback)(
                (e) => {
                  (w(!0), b && b(e), _ && (0, ee.G)(_), o && L());
                },
                [o, b, L, _],
              ),
              O = (0, n.useCallback)(
                (e) => {
                  (w(!1), h && h(e));
                },
                [h],
              ),
              H = (0, n.useCallback)(
                (e) => {
                  (p && p(e), l && (0, ee.G)(l), y(!0));
                },
                [p, l],
              ),
              W = (0, n.useCallback)(
                (e) => {
                  (w(!1), y(!1), A && A(e));
                },
                [A],
              ),
              G = (0, n.useCallback)(
                (e) => {
                  (R(!0), C && C(e));
                },
                [C],
              ),
              $ = (0, n.useCallback)(
                (e) => {
                  (R(!1), v && v(e));
                },
                [v],
              ),
              U = f()(
                ka.base,
                u && ka.base__visibleLabel,
                F && ka.base__mouseDown,
                P && ka.base__hovered,
                x && ka.base__focused,
                null == E ? void 0 : E.base,
              ),
              z = f()(ka.icon, ka[`icon__${m}`], null == E ? void 0 : E.icon),
              V = f()(ka.label, null == E ? void 0 : E.label);
            return s().createElement(
              "div",
              Ra(
                {
                  ref: N,
                  className: U,
                  onClick: M,
                  onMouseEnter: H,
                  onMouseLeave: W,
                  onMouseDown: I,
                  onMouseUp: O,
                  onFocus: G,
                  onBlur: $,
                },
                D,
              ),
              s().createElement("div", { className: z }),
              s().createElement("div", { className: V }, t),
            );
          }),
          Ta = (e, t) => {
            let a;
            const u = setTimeout(() => {
              a = e();
            }, t);
            return () => {
              ("function" == typeof a && a(), clearTimeout(u));
            };
          },
          Ma = {
            base: "Sonar_base_8f",
            back: "Sonar_back_6b",
            fadeIn: "Sonar_fadeIn_d6",
            emitter: "Sonar_emitter_50",
            wave: "Sonar_wave_1e",
            wave__0: "Sonar_wave__0_7a",
            sonarWave: "Sonar_sonarWave_6b",
            wave__1: "Sonar_wave__1_aa",
            wave__2: "Sonar_wave__2_5d",
            wave__3: "Sonar_wave__3_67",
            wave__4: "Sonar_wave__4_cd",
            wave__5: "Sonar_wave__5_08",
            wave__6: "Sonar_wave__6_0b",
            wave__7: "Sonar_wave__7_b6",
            wave__8: "Sonar_wave__8_3b",
            wave__9: "Sonar_wave__9_16",
            wave__10: "Sonar_wave__10_09",
          },
          Ia = ({ className: e }) =>
            s().createElement(
              "div",
              { className: f()(Ma.base, e) },
              s().createElement(
                "div",
                { className: Ma.emitter },
                Array.from({ length: 10 }, (e, t) =>
                  s().createElement("div", {
                    key: `wave-${t}`,
                    className: f()(Ma.wave, Ma[`wave__${t}`]),
                  }),
                ),
              ),
              s().createElement("div", { className: Ma.back }),
            ),
          Oa = "Sound_base_9f",
          Ha = "Sound_content_7a",
          Wa = "Sound_icoContainer_b7",
          Ga = "Sound_base__active_d7",
          $a = "Sound_ico_d2",
          Ua = "Sound_sonar_ef",
          za = "Sound_sonar__show_f5",
          Va = R.strings.battle_pass.progression.extraChapterWidget,
          ja = ({ active: e, soundOn: t }) =>
            s().createElement(
              ge.i,
              { body: Va.voiceOverTooltip() },
              s().createElement(
                "div",
                { className: f()(Oa, (e || t) && Ga) },
                s().createElement(
                  "div",
                  { className: Ha },
                  s().createElement(
                    "div",
                    { className: Wa },
                    s().createElement("div", { className: $a }),
                  ),
                ),
                s().createElement(Ia, { className: f()(Ua, t && za) }),
              ),
            ),
          Xa = {
            base: "Separator_base_c5",
            separatorBg: "Separator_separatorBg_28",
            item: "Separator_item_fc",
            previewLabel: "Separator_previewLabel_7b",
          },
          Ya = (0, n.memo)(({ classNames: e, soundTag: t, onSound: a, onPreviewIconClick: u }) => {
            const r = (0, n.useState)(!1),
              o = r[0],
              i = r[1],
              l = (0, n.useState)(!1),
              c = l[0],
              _ = l[1],
              d = Boolean(t);
            return s().createElement(
              "div",
              { className: f()(Xa.base, d && Xa.base__hasSound) },
              s().createElement("div", {
                className: f()(Xa.separatorBg, null == e ? void 0 : e.separatorBg),
              }),
              d &&
                s().createElement(
                  "div",
                  {
                    className: Xa.item,
                    onClick: () => {
                      if (!c)
                        return (
                          _(!0),
                          a && a(),
                          Ta(() => {
                            _(!1);
                          }, 3e3)
                        );
                    },
                    onMouseEnter: () => {
                      ((0, ee.G)("highlight"), i(!0));
                    },
                    onMouseLeave: () => {
                      i(!1);
                    },
                  },
                  s().createElement(ja, { active: o, soundOn: c }),
                ),
              u &&
                s().createElement(
                  "div",
                  { className: Xa.item },
                  s().createElement(La, {
                    size: Na.NORMAL,
                    onClick: u,
                    classNames: { label: Xa.previewLabel },
                  }),
                ),
            );
          }),
          qa = (0, te.Pi)(() => {
            const e = Se(),
              t = e.model,
              a = e.controls,
              u = t.root.get(),
              r = u.isBattlePassPurchased,
              n = u.progressionQuestVehicleName,
              o = t.computes.getStyleInfoExtraChapterWidget(),
              i = t.extraChapterWidget.get().marathonRewardId,
              l = t.computes.getExtraChapterRewardInfo(),
              c = t.chapterCharacter.get();
            return s().createElement(
              "div",
              { className: Sa },
              s().createElement("div", { className: Pa }),
              s().createElement(wa, {
                styleReward: o,
                vehicleReward: l,
                characterReward: c,
                isBattlePassPurchased: r,
                marathonRewardId: i,
                progressionQuestVehicleName: n,
              }),
              s().createElement(Ya, {
                classNames: { separatorBg: ya },
                onPreviewIconClick: a.openPreview,
                onSound: a.onSound,
                soundTag: c.voiceTag,
              }),
              s().createElement(wa, {
                styleReward: o,
                vehicleReward: l,
                characterReward: c,
                isBattlePassPurchased: r,
                marathonRewardId: i,
                progressionQuestVehicleName: n,
                isPaidRewards: !0,
              }),
            );
          }),
          Ka = {
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
        let Qa, Za;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(Qa || (Qa = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(Za || (Za = {})));
        const Ja = ({
          children: e,
          size: t,
          isFocused: a,
          type: u,
          disabled: r,
          mixClass: o,
          soundHover: i,
          soundClick: l,
          onMouseEnter: c,
          onMouseMove: _,
          onMouseDown: d,
          onMouseUp: m,
          onMouseLeave: E,
          onClick: g,
        }) => {
          const p = (0, n.useRef)(null),
            A = (0, n.useState)(a),
            b = A[0],
            h = A[1],
            C = (0, n.useState)(!1),
            v = C[0],
            D = C[1],
            B = (0, n.useState)(!1),
            F = B[0],
            w = B[1],
            S = (0, n.useCallback)(() => {
              r || (p.current && (p.current.focus(), h(!0)));
            }, [r]),
            P = (0, n.useCallback)(
              (e) => {
                b && null !== p.current && !p.current.contains(e.target) && h(!1);
              },
              [b],
            ),
            y = (0, n.useCallback)(
              (e) => {
                r || (g && g(e));
              },
              [r, g],
            ),
            k = (0, n.useCallback)(
              (e) => {
                r || (null !== i && (0, ee.G)(i), c && c(e), w(!0));
              },
              [r, i, c],
            ),
            x = (0, n.useCallback)(
              (e) => {
                _ && _(e);
              },
              [_],
            ),
            N = (0, n.useCallback)(
              (e) => {
                r || (m && m(e), D(!1));
              },
              [r, m],
            ),
            L = (0, n.useCallback)(
              (e) => {
                r || (null !== l && (0, ee.G)(l), d && d(e), a && S(), D(!0));
              },
              [r, l, d, S, a],
            ),
            T = (0, n.useCallback)(
              (e) => {
                r || (E && E(e), D(!1));
              },
              [r, E],
            ),
            M = f()(
              Ka.base,
              Ka[`base__${u}`],
              {
                [Ka.base__disabled]: r,
                [Ka[`base__${t}`]]: t,
                [Ka.base__focus]: b,
                [Ka.base__highlightActive]: v,
                [Ka.base__firstHover]: F,
              },
              o,
            ),
            I = f()(Ka.state, Ka.state__default);
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
              h(a);
            }, [a]),
            s().createElement(
              "div",
              {
                ref: p,
                className: M,
                onMouseEnter: k,
                onMouseMove: x,
                onMouseUp: N,
                onMouseDown: L,
                onMouseLeave: T,
                onClick: y,
              },
              u !== Qa.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: Ka.back }),
                  s().createElement("span", { className: Ka.texture }),
                ),
              s().createElement(
                "span",
                { className: I },
                s().createElement("span", { className: Ka.stateDisabled }),
                s().createElement("span", { className: Ka.stateHighlightHover }),
                s().createElement("span", { className: Ka.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: Ka.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        Ja.defaultProps = {
          type: Qa.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const eu = (0, n.memo)(Ja),
          tu = ["children"];
        function au() {
          return (
            (au =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            au.apply(this, arguments)
          );
        }
        const uu = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                u,
                r = {},
                n = Object.keys(e);
              for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, tu);
          return s().createElement(
            Kt.u,
            au(
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
        };
        function ru() {
          return (
            (ru =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            ru.apply(this, arguments)
          );
        }
        const nu = ({ children: e, tooltipArgs: t, className: a }) => {
            if (!t) return e;
            const u = s().createElement("div", { className: a }, e);
            if (t.header || t.body) return s().createElement(ge.i, t, u);
            const r = t.contentId,
              n = t.args,
              o = null == n ? void 0 : n.contentId;
            return r || o
              ? s().createElement(Kt.u, ru({}, t, { contentId: r || o }), u)
              : s().createElement(uu, t, u);
          },
          su = "Footer_base_96",
          ou = "Footer_light_53",
          iu = "Footer_light__opacityMode1_53",
          lu = "Footer_light__opacityMode2_14",
          cu = "Footer_light__opacityMode3_5c",
          _u = "Footer_button_2a",
          du = "Footer_button__buyBp_c9",
          mu = "Footer_button__medium_23",
          Eu = "Footer_button__large_3f",
          gu = "Footer_labelContainer_bf",
          pu = "Footer_labelHeader_ad",
          Au = "Footer_label_61",
          bu = "Footer_days_3d",
          hu = "Footer_blink_5d",
          Cu = R.strings.battle_pass.progression,
          vu = R.strings.battle_pass.tooltips.footerBuyBtn;
        let fu, Du;
        (!(function (e) {
          ((e.Red = "red"), (e.Green = "green"), (e.None = ""));
        })(fu || (fu = {})),
          (function (e) {
            ((e.Inactive = "Inactive"), (e.Paused = "Paused"));
          })(Du || (Du = {})));
        const Bu = (0, te.Pi)(() => {
            const e = Se(),
              t = e.model,
              a = e.controls,
              u = P().mediaSize,
              r = t.root.get(),
              n = r.isSeasonEndingSoon,
              o = r.expireTimeStr,
              i = r.chapterState,
              l = r.isBattlePassPurchased,
              c = r.isWalletAvailable,
              _ = i === lt.Completed,
              d = i === lt.Active || _,
              m = i !== lt.Active,
              E = u <= F.Small ? Za.small : Za.medium,
              g = l ? Cu.episodeBuyDescr() : Cu.battlePassBuyDescr(),
              p = n ? Cu.seasonEndingDescr() : g;
            return s().createElement(
              "div",
              { className: su },
              l
                ? s().createElement(
                    s().Fragment,
                    null,
                    s().createElement("div", { className: f()(ou, lu) }),
                    s().createElement(
                      "div",
                      { className: gu },
                      s().createElement(
                        "div",
                        { className: Au },
                        s().createElement(qt, { text: p }),
                        n && s().createElement(qt, { text: o, className: bu }),
                      ),
                      s().createElement(
                        ge.i,
                        {
                          body: R.strings.battle_pass.progression.episodeBuyBtnTooltipDisabled(),
                          isEnabled: m,
                        },
                        s().createElement(
                          "div",
                          { className: pu },
                          s().createElement(
                            nu,
                            {
                              tooltipArgs: {
                                contentId:
                                  R.views.lobby.battle_pass.tooltips.BuyStagesFooterTooltipView(
                                    "resId",
                                  ),
                                args: { isActive: !0 },
                                isEnabled: !m,
                              },
                            },
                            s().createElement(
                              eu,
                              {
                                type: Qa.main,
                                size: E,
                                mixClass: f()(_u, mu),
                                onClick: a.onBuyStages,
                                disabled: m || !c,
                              },
                              n && !m && s().createElement("div", { className: hu }),
                              s().createElement(qt, { text: Cu.episodeBuyBtn() }),
                            ),
                          ),
                        ),
                      ),
                    ),
                  )
                : s().createElement(
                    s().Fragment,
                    null,
                    s().createElement("div", { className: f()(ou, d ? cu : iu) }),
                    s().createElement(
                      "div",
                      { className: gu },
                      s().createElement(
                        "div",
                        { className: Au },
                        s().createElement(qt, { text: p }),
                        n && s().createElement(qt, { text: o, className: bu }),
                      ),
                      s().createElement(
                        "div",
                        { className: pu },
                        s().createElement(
                          ge.i,
                          { body: vu.battlePass.descr() },
                          s().createElement(
                            eu,
                            {
                              type: Qa.main,
                              size: E,
                              mixClass: f()(_u, Eu, d && du),
                              onClick: a.onBuyBP,
                              disabled: !c,
                            },
                            n && s().createElement("div", { className: hu }),
                            s().createElement(qt, { text: Cu.battlePassBuyBtn() }),
                          ),
                        ),
                        d &&
                          !_ &&
                          s().createElement(
                            nu,
                            {
                              tooltipArgs: {
                                contentId:
                                  R.views.lobby.battle_pass.tooltips.BuyStagesFooterTooltipView(
                                    "resId",
                                  ),
                                args: { isActive: !1 },
                              },
                            },
                            s().createElement(
                              eu,
                              {
                                type: Qa.primary,
                                size: E,
                                mixClass: f()(_u, Eu),
                                onClick: a.onBuyStages,
                                disabled: !0,
                              },
                              s().createElement(qt, { text: Cu.episodeBuyBtn() }),
                            ),
                          ),
                      ),
                    ),
                  ),
            );
          }),
          Fu = "display",
          wu = "enabled",
          Su = "enabled_change";
        function Pu(e, t, a) {
          const u = (0, n.useContext)(p);
          let r = Object.entries(u).filter(([e, t]) => !0 === t && e in c);
          return (
            a && (r = r.filter((e) => a.includes(e[0]))),
            e.reduce((e, a) => {
              const u = r.map((e) =>
                f()(t[((e, t) => e + "__" + t)(a, e[0])], t[((e, t) => e + (0, ae.e)(t))(a, e[0])]),
              );
              return ((e[a] = f()(t[a], ...u)), e);
            }, {})
          );
        }
        const yu = {
          base: "ViewDecorator_base_aa",
          container: "ViewDecorator_container_98",
          container__shown: "ViewDecorator_container__shown_da",
          leftBlock: "ViewDecorator_leftBlock_63",
          leftBlock__small: "ViewDecorator_leftBlock__small_6a",
          rightBlock: "ViewDecorator_rightBlock_71",
          rightBlock__small: "ViewDecorator_rightBlock__small_ef",
          view: "ViewDecorator_view_9e",
        };
        let ku;
        !(function (e) {
          ((e.Back = "back"), (e.Forward = "forward"), (e.Close = "close"), (e.Info = "info"));
        })(ku || (ku = {}));
        (0, n.memo)(
          ({
            background: e,
            rightText: t,
            leftText: a,
            children: u,
            leftSubText: r,
            leftButtonType: o,
            onClose: i,
            onLeftButtonClick: l,
            isHideButtons: c = !1,
          }) => {
            const _ = Pu(["leftBlock", "rightBlock"], yu),
              d = (0, n.useState)(c),
              m = d[0],
              E = d[1];
            (0, n.useEffect)(() => E(!c), [c]);
            const g = (0, n.useMemo)(() => (e ? { backgroundImage: `url('${e}')` } : void 0), [e]),
              p = f()(yu.container, m && yu.container__shown);
            return s().createElement(
              "div",
              { className: yu.base, style: g },
              s().createElement(
                "div",
                { className: p },
                Boolean(a) &&
                  s().createElement(
                    "div",
                    { className: _.leftBlock },
                    s().createElement(it, {
                      caption: a || "",
                      goto: r,
                      type: o,
                      side: "left",
                      onClick: l,
                    }),
                  ),
                Boolean(t) &&
                  s().createElement(
                    "div",
                    { className: _.rightBlock },
                    s().createElement(it, {
                      caption: t || "",
                      type: "close",
                      side: "right",
                      onClick: i,
                    }),
                  ),
              ),
              s().createElement("div", { className: yu.view }, u),
            );
          },
        );
        var xu = a(6895);
        const Ru = "Header_base_be",
          Nu = "Header_content_4d",
          Lu = "Header_hintBody_84",
          Tu = "Header_infoContainer_8f",
          Mu = "Header_titleContainer_9a",
          Iu = "Header_topTitleContainer_28",
          Ou = "Header_chapterName_c7",
          Hu = "Header_expireTime_55",
          Wu = "Header_expireCount_19",
          Gu = "Header_horizontalSeparator_4d",
          $u = "Header_verticalSeparator_c3",
          Uu = "Header_verticalTitleSeparator_21",
          zu = "Header_mainTitle_05",
          Vu = "Header_actionContainer_91",
          ju = "Header_disabledText_b2",
          Xu = "Header_expireCount__active_4e",
          Yu = "Header_gameModes_b5",
          qu = "Header_gameModeIcon_e4",
          Ku = "Header_tasksIcon_21",
          Qu = "Header_gameModesContainer_70",
          Zu = "Header_tasksButtonContainer_36",
          Ju = "Header_hiddenBattleTypes_5e",
          er = "Header_titleButtons_80",
          tr = "Header_titleButtons__small_17",
          ar = "Header_titleButton_1d",
          ur = "Header_button_e2",
          rr = "Header_tasksButton_4c",
          nr = "Header_awards_7b",
          sr = R.strings.battle_pass,
          or = (0, te.Pi)(() => {
            const e = P().mediaSize,
              t = Se(),
              a = t.model,
              u = t.controls,
              r = a.root.get(),
              o = r.chapterID,
              i = r.chapterState,
              l = r.expireTimeStr,
              c = r.bpcoinCount,
              _ = r.bpbitCount,
              d = r.notChosenRewardCount,
              m = r.isChooseRewardsEnabled,
              E = r.isBattlePassCompleted,
              g = r.chapterType,
              p = r.isSeasonEndingSoon,
              A = r.isBpCoinShopEntryPointActive,
              b = r.isBpPointsShopEntryPointActive,
              h = a.collectionEntryPoint.get(),
              C = h.collectionItemCount,
              v = h.newCollectionItemCount,
              D = h.maxCollectionItemCount,
              B = h.isFirstEnter,
              w = h.isCollectionsEnabled,
              S = a.computes.hasChapter(Ct.Marathon),
              y = a.computes.hasChapter(Ct.Resource),
              k = a.computes.getAvailableBattleTypes(),
              x = sr.chapter.fullName.quoted.$num(o),
              N = e < F.Medium ? Za.small : Za.medium,
              L = e > F.ExtraSmall,
              T = i === lt.NotStarted || i === lt.Paused,
              M = (0, ae.uF)(sr.progression.header.chapter.status(), { chapterName: x }),
              I = ((e, t, a) => {
                switch (e) {
                  case lt.Paused:
                  case lt.NotStarted:
                    return s().createElement(
                      ge.i,
                      { body: sr.tooltips.footerBuyBtn.activateChapter.descr() },
                      s().createElement(
                        "div",
                        null,
                        s().createElement("div", { className: Lu, id: "chapter-header-trigger" }),
                        s().createElement(
                          eu,
                          { type: Qa.primary, size: t, mixClass: ur, onClick: a },
                          s().createElement(qt, { text: sr.chapter.activateChapter() }),
                        ),
                      ),
                    );
                  case lt.Disabled:
                    return s().createElement(qt, {
                      text: sr.progression.battlePassDisabled(),
                      className: ju,
                    });
                  default:
                    return;
                }
              })(i, N, u.onAction),
              O = ((e, t) => {
                const a = J("tutorialModel.effects.items").filter((a) => {
                  if (!a) return !1;
                  const u = a.value,
                    r = window.__featureId.toString();
                  return u.componentId === e && u.type === t && u.viewId === r;
                });
                if (0 === a.length) return null;
                const u = Object.assign({}, a[0].value);
                return {
                  effect: u,
                  completeEffect: () => {
                    (tutorialModel.onEffectCompleted({
                      componentId: e,
                      viewId: window.__featureId.toFixed(0),
                      effectType: t,
                      effectBuilder: u.builder,
                    }),
                      t === Fu && window.tutorialApi && window.tutorialApi.updateComponents());
                  },
                };
              })("ChapterHeaderTrigger", wu);
            (0, n.useEffect)(
              () =>
                W(() => {
                  null !== O && T && O.completeEffect();
                }),
              [O, T],
            );
            const H = ((e, t) => {
              const a = J("tutorialModel.triggers.items").filter((a) => {
                if (!a) return !1;
                const u = a.value,
                  r = u.triggers.filter((e) => e.value === t);
                return u.componentId === e && r.length > 0;
              });
              return 0 === a.length
                ? null
                : window.tutorialModel.foundComponents.items.some((t) => t.value.componentId === e)
                  ? {
                      trigger: a[0].value,
                      runTrigger: (a) => {
                        window.tutorialModel.onTriggerActivated({
                          componentId: e,
                          triggerType: t,
                          state: a,
                        });
                      },
                    }
                  : null;
            })("ChapterHeaderTrigger", Su);
            return (
              (0, n.useEffect)(() => {
                H && T && H.runTrigger(!0);
              }, [T, H]),
              s().createElement(
                "div",
                { className: Ru },
                s().createElement(
                  "div",
                  { className: Mu },
                  s().createElement(
                    "div",
                    { className: Iu },
                    s().createElement(qt, { text: M, className: Ou }),
                    s().createElement("div", { className: Uu }),
                    s().createElement(qt, { text: sr.progression.header.endDays(), className: Hu }),
                    s().createElement(qt, { text: l, className: f()(Wu, p && Xu) }),
                  ),
                  s().createElement(qt, {
                    text: sr.progression.header.title.$dyn(i),
                    className: zu,
                  }),
                  I && s().createElement("div", { className: Vu }, I),
                ),
                s().createElement(
                  "div",
                  { className: Nu },
                  s().createElement(
                    "div",
                    { className: Tu },
                    s().createElement(
                      "div",
                      { className: f()(er, !L && tr) },
                      s().createElement(
                        "div",
                        { className: ar },
                        s().createElement(it, {
                          caption: sr.progression.about.$dyn(g),
                          type: ku.Info,
                          onClick: u.onAbout,
                        }),
                      ),
                      s().createElement(
                        "div",
                        { className: ar },
                        s().createElement(it, {
                          caption: sr.howToEarnPoints.title(),
                          type: ku.Info,
                          onClick: u.onPointsInfo,
                        }),
                      ),
                    ),
                    L &&
                      s().createElement(
                        s().Fragment,
                        null,
                        s().createElement("div", { className: Gu }),
                        s().createElement(
                          "div",
                          { className: Qu },
                          s().createElement(
                            nu,
                            {
                              tooltipArgs: {
                                contentId:
                                  R.views.lobby.battle_pass.tooltips.BattleTypesTooltipView(
                                    "resId",
                                  ),
                              },
                            },
                            s().createElement(
                              "div",
                              { className: Yu },
                              k
                                .slice(0, 5)
                                .map((e) =>
                                  s().createElement("div", {
                                    className: qu,
                                    key: `game_mode_${e}`,
                                    style: {
                                      backgroundImage: `url(R.images.gui.maps.icons.battleTypeIcons.c_40x40.c_${e})`,
                                    },
                                  }),
                                ),
                              k.length > 5 &&
                                s().createElement(qt, {
                                  text: sr.progression.header.hiddenBattleTypes(),
                                  className: Ju,
                                }),
                            ),
                          ),
                          s().createElement("div", { className: $u }),
                          s().createElement("div", { className: Ku }),
                          s().createElement(
                            "div",
                            { className: Zu },
                            s().createElement(
                              ge.i,
                              {
                                header: sr.progression.btnTasksTooltip.header(),
                                body: sr.progression.btnTasksTooltip.body(),
                              },
                              s().createElement(
                                eu,
                                {
                                  type: Qa.ghost,
                                  size: Za.medium,
                                  mixClass: rr,
                                  onClick: u.onTasks,
                                },
                                s().createElement(qt, { text: sr.progression.btnTasks() }),
                              ),
                            ),
                          ),
                        ),
                      ),
                  ),
                  s().createElement(
                    "div",
                    { className: nr },
                    s().createElement(xu.Z, {
                      notChosenRewardCount: d,
                      pointsCount: _,
                      coinCount: c,
                      collectionItemCount: C,
                      maxCollectionItemCount: D,
                      newCollectionItemCount: v,
                      isBPFirstEnter: B,
                      isCollectionsEnabled: w,
                      isAwardDisabled: !m,
                      isPointsLocked: !E,
                      onPointsClick: u.onBpbit,
                      onCoinClick: u.onBpcoin,
                      onTakeRewardsClick: u.onTakeRewards,
                      onCollectionClick: u.openCollection,
                      hasMarathon: S,
                      hasResource: y,
                      isBpCoinShopEntryPointActive: A,
                      isBpPointsShopEntryPointActive: b,
                    }),
                  ),
                ),
              )
            );
          }),
          ir = {
            base: "Progression_base_52",
            base__marathon: "Progression_base__marathon_dd",
            scroll: "Progression_scroll_25",
            scroll__hidden: "Progression_scroll__hidden_62",
            scrollWrapper: "Progression_scrollWrapper_3a",
            wrapper: "Progression_wrapper_0f",
            section__last: "Progression_section__last_4d",
            divider: "Progression_divider_4e",
            dividerContent: "Progression_dividerContent_82",
            dividerText: "Progression_dividerText_8c",
            progressContainer: "Progression_progressContainer_7f",
            progress: "Progression_progress_c8",
            progress__inactive: "Progression_progress__inactive_b8",
            progressBackground: "Progression_progressBackground_8c",
            progressBackground__disabled: "Progression_progressBackground__disabled_0b",
            progressBackground__finished: "Progression_progressBackground__finished_0e",
            decor: "Progression_decor_7f",
            decorBackground: "Progression_decorBackground_4c",
            decor__left: "Progression_decor__left_4e",
            row: "Progression_row_2c",
            row__basic: "Progression_row__basic_05",
            bookmark: "Progression_bookmark_78",
            bookmark__start: "Progression_bookmark__start_e7",
            bookmarkLeftFixed: "Progression_bookmarkLeftFixed_6c",
            bookmarkLeftFixed__active: "Progression_bookmarkLeftFixed__active_3b",
            bookmarkLeftResponsive: "Progression_bookmarkLeftResponsive_c3",
            bookmarkBackground: "Progression_bookmarkBackground_d6",
            scrollToButton: "Progression_scrollToButton_38",
            scrollToButton__visible: "Progression_scrollToButton__visible_47",
            scrollToButton__forward: "Progression_scrollToButton__forward_18",
            scrollToButton__backward: "Progression_scrollToButton__backward_1f",
            arrowButton: "Progression_arrowButton_ad",
            progressionToButton: "Progression_progressionToButton_3b",
            progressionToButton__hidden: "Progression_progressionToButton__hidden_29",
            progressionToButton__back: "Progression_progressionToButton__back_a8",
            progressionToButton__forward: "Progression_progressionToButton__forward_ce",
            shadow: "Progression_shadow_4a",
            shadow__left: "Progression_shadow__left_e1",
            shadow__right: "Progression_shadow__right_f8",
            additionalShadow: "Progression_additionalShadow_69",
            additionalShadow__active: "Progression_additionalShadow__active_80",
            scrollBarPosition: "Progression_scrollBarPosition_40",
            fadeOut: "Progression_fadeOut_7c",
            fadeIn: "Progression_fadeIn_1d",
            fadeInWithScale: "Progression_fadeInWithScale_74",
            slideUp: "Progression_slideUp_a2",
            scale: "Progression_scale_a8",
            rotate: "Progression_rotate_1c",
          },
          lr = (e, t, a) => (a < e ? e : a > t ? t : a),
          cr = [];
        function _r(e) {
          const t = (0, n.useRef)(e);
          return (
            (0, n.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, n.useCallback)((...e) => (0, t.current)(...e), cr)
          );
        }
        function dr(e, t, a = []) {
          const u = (0, n.useRef)(0),
            r = (0, n.useCallback)(() => window.clearInterval(u.current), a || []);
          (0, n.useEffect)(() => r, [r]);
          const s = (null != a ? a : []).concat([t]);
          return [
            (0, n.useCallback)((a) => {
              ((u.current = window.setInterval(() => e(a, !0), t)), e(a, !1));
            }, s),
            r,
          ];
        }
        function mr(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return Er(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return Er(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            a && (e = a);
            var u = 0;
            return function () {
              return u >= e.length ? { done: !0 } : { done: !1, value: e[u++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function Er(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, u = new Array(t); a < t; a++) u[a] = e[a];
          return u;
        }
        function gr(e, t, a) {
          const u = (0, n.useMemo)(
            () =>
              (function (e, t, a, u) {
                let r,
                  n = !1,
                  s = 0;
                function o() {
                  r && clearTimeout(r);
                }
                function i(...i) {
                  const l = this,
                    c = Date.now() - s;
                  function _() {
                    ((s = Date.now()), a.apply(l, i));
                  }
                  n ||
                    (u && !r && _(),
                    o(),
                    void 0 === u && c > e
                      ? _()
                      : !0 !== t &&
                        (r = setTimeout(
                          u
                            ? function () {
                                r = void 0;
                              }
                            : _,
                          void 0 === u ? e - c : e,
                        )));
                }
                return (
                  "boolean" != typeof t && ((u = a), (a = t), (t = void 0)),
                  (i.cancel = function () {
                    (o(), (n = !0));
                  }),
                  i
                );
              })(a, e),
            t,
          );
          return ((0, n.useEffect)(() => u.cancel, [u]), u);
        }
        var pr = a(7030);
        let Ar;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Ar || (Ar = {}));
        const br = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          hr = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: a,
            getDirection: u,
            getWrapperSize: r,
            triggerMouseMoveOnUpdate: s = !1,
          }) => {
            const o = (e, a) => {
              const u = t(e),
                r = u[0],
                n = u[1];
              return lr(r, n, a);
            };
            return (l = {}) => {
              const c = l.settings,
                _ = void 0 === c ? br : c,
                d = (0, n.useRef)(null),
                m = (0, n.useRef)(null),
                E = (() => {
                  const e = (0, n.useMemo)(() => ({}), []),
                    t = (t) => (e[t] || (e[t] = new Map()), e[t]),
                    a = (e, a) => {
                      t(e).set(a, a);
                    },
                    u = (e, a) => {
                      t(e).delete(a);
                    },
                    r = (e, ...a) => {
                      for (var u, r = mr(t(e).values()); !(u = r()).done;) (0, u.value)(...a);
                    };
                  return (0, n.useMemo)(() => ({ on: a, off: u, trigger: r }), []);
                })(),
                g = gr(
                  () => {
                    i.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                p = (0, pr.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = d.current;
                    t && (a(t, e), E.trigger("change", e), s && g());
                  },
                  onRest: (e) => E.trigger("rest", e),
                  onStart: (e) => E.trigger("start", e),
                  onPause: (e) => E.trigger("pause", e),
                })),
                A = p[0],
                b = p[1],
                h = (0, n.useCallback)(
                  (e, t, a) => {
                    var u;
                    const r = A.scrollPosition.get(),
                      n = (null != (u = A.scrollPosition.goal) ? u : 0) - r;
                    return o(e, t * a + n + r);
                  },
                  [A.scrollPosition],
                ),
                C = (0, n.useCallback)(
                  (e, { immediate: t = !1, reset: a = !0 } = {}) => {
                    const u = d.current;
                    u &&
                      b.start({
                        scrollPosition: o(u, e),
                        immediate: t,
                        reset: a,
                        config: _.animationConfig,
                        from: { scrollPosition: o(u, A.scrollPosition.get()) },
                      });
                  },
                  [b, _.animationConfig, A.scrollPosition],
                ),
                v = (0, n.useCallback)(
                  (e) => {
                    const t = d.current,
                      a = m.current;
                    if (!t || !a) return;
                    const u = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return r(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(a, _.step),
                      n = h(t, e, u);
                    C(n);
                  },
                  [C, h, _.step],
                ),
                f = (0, n.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && v(u(e)),
                      d.current && E.trigger("mouseWheel", e, A.scrollPosition, t(d.current)));
                  },
                  [A.scrollPosition, v, E],
                ),
                D = ((e, t = []) => {
                  const a = (0, n.useRef)(),
                    u = (0, n.useCallback)((...t) => {
                      (a.current && a.current(), (a.current = e(...t)));
                    }, t);
                  return (
                    (0, n.useEffect)(
                      () => () => {
                        a.current && a.current();
                      },
                      [u],
                    ),
                    u
                  );
                })(
                  () =>
                    W(() => {
                      const e = d.current;
                      e &&
                        (C(o(e, A.scrollPosition.goal), { immediate: !0 }),
                        E.trigger("resizeHandled"));
                    }),
                  [C, A.scrollPosition.goal],
                ),
                B = _r(() => {
                  const e = d.current;
                  if (!e) return;
                  const t = o(e, A.scrollPosition.goal);
                  (t !== A.scrollPosition.goal && C(t, { immediate: !0 }),
                    E.trigger("recalculateContent"));
                });
              (0, n.useEffect)(
                () => (
                  window.addEventListener("resize", D),
                  () => {
                    window.removeEventListener("resize", D);
                  }
                ),
                [D],
              );
              const F = (0, n.useCallback)((e) => E.trigger("isThumbDraggingChanged", e), [E]);
              return (0, n.useMemo)(
                () => ({
                  getWrapperSize: () => (m.current ? r(m.current) : void 0),
                  getContainerSize: () => (d.current ? e(d.current) : void 0),
                  getBounds: () =>
                    d.current
                      ? t(d.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: _.step.clampedArrowStepTimeout,
                  clampPosition: o,
                  handleMouseWheel: f,
                  applyScroll: C,
                  applyStepTo: v,
                  contentRef: d,
                  wrapperRef: m,
                  scrollPosition: b,
                  animationScroll: A,
                  recalculateContent: B,
                  handleIsThumbDragging: F,
                  events: { on: E.on, off: E.off },
                }),
                [A.scrollPosition, C, v, F, E.off, E.on, B, f, b, _.step.clampedArrowStepTimeout],
              );
            };
          },
          Cr = hr({
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
            getDirection: (e) => (e.deltaY > 1 ? Ar.Next : Ar.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          vr = "HorizontalBar_base_49",
          fr = "HorizontalBar_base__nonActive_82",
          Dr = "HorizontalBar_leftButton_5f",
          Br = "HorizontalBar_rightButton_03",
          Fr = "HorizontalBar_track_0d",
          wr = "HorizontalBar_thumb_fd",
          Sr = "HorizontalBar_rail_32",
          Pr = "disable",
          yr = { pending: !1, offset: 0 },
          kr = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          xr = () => {},
          Rr = (e, t) => Math.max(20, e.offsetWidth * t),
          Nr = (0, n.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = kr, onDrag: u = xr }) => {
              const r = (0, n.useRef)(null),
                o = (0, n.useRef)(null),
                i = (0, n.useRef)(null),
                l = (0, n.useRef)(null),
                c = (0, n.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, n.useState)(yr),
                m = d[0],
                E = d[1],
                g = (0, n.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        u({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [u],
                ),
                p = () => {
                  const t = l.current,
                    a = c.current,
                    u = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(u && t && a && r)) return;
                  const n = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, u / r),
                    _ = lr(0, 1, n / (r - u)),
                    d = (t.offsetWidth - Rr(t, s)) * _;
                  ((a.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (o.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (o.current.classList.add(Pr), void i.current.classList.remove(Pr));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetWidth - a.offsetWidth) >= -0.5)
                        )
                          return (o.current.classList.remove(Pr), void i.current.classList.add(Pr));
                        var t, a;
                        (o.current.classList.remove(Pr), i.current.classList.remove(Pr));
                      }
                    })(d));
                },
                A = _r(() => {
                  ((() => {
                    const t = c.current,
                      a = l.current,
                      u = e.getWrapperSize(),
                      n = e.getContainerSize();
                    if (!(n && t && u && a)) return;
                    const s = Math.min(1, u / n);
                    ((t.style.width = `${Rr(a, s)}px`),
                      (t.style.display = "flex"),
                      r.current &&
                        (1 === s ? r.current.classList.add(fr) : r.current.classList.remove(fr)));
                  })(),
                    p());
                });
              ((0, n.useEffect)(() => W(A)),
                (0, n.useEffect)(
                  () =>
                    W(() => {
                      const t = () => {
                        p();
                      };
                      let a = xr;
                      const u = () => {
                        (a(), (a = W(A)));
                      };
                      return (
                        e.events.on("recalculateContent", A),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", u),
                        () => {
                          (a(),
                            e.events.off("recalculateContent", A),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", u));
                        }
                      );
                    }),
                  [e],
                ),
                (0, n.useEffect)(() => {
                  if (!m.pending) return;
                  const t = (t) => {
                      var a;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const n = l.current,
                        s = c.current;
                      if (!r || !n || !s) return;
                      const o = t.screenX - m.offset - n.getBoundingClientRect().x,
                        i = (o / n.offsetWidth) * (null != (a = e.getContainerSize()) ? a : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        u({ type: "dragging", thumb: s, thumbOffset: o, contentOffset: i }));
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t), g(yr));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, m.offset, m.pending, u, g]));
              const b = dr((t) => e.applyStepTo(t), _, [e]),
                h = b[0],
                C = b[1];
              (0, n.useEffect)(
                () => (
                  document.addEventListener("mouseup", C, !0),
                  () => document.removeEventListener("mouseup", C, !0)
                ),
                [C],
              );
              const v = (e) => {
                e.target.classList.contains(Pr) || (0, ee.G)("highlight");
              };
              return s().createElement(
                "div",
                { className: f()(vr, t.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: f()(Dr, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Pr) ||
                      0 !== e.button ||
                      ((0, ee.G)("play"), h(Ar.Next));
                  },
                  onMouseUp: C,
                  ref: o,
                  onMouseEnter: v,
                }),
                s().createElement(
                  "div",
                  {
                    className: f()(Fr, t.track),
                    onMouseDown: (t) => {
                      const u = c.current;
                      if (u && 0 === t.button)
                        if (((0, ee.G)("play"), t.target === u))
                          g({ pending: !0, offset: t.screenX - u.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const u = c.current,
                              r = e.contentRef.current;
                            if (!u || !r) return;
                            const n = a(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + n * t);
                          })(t.screenX > u.getBoundingClientRect().x ? Ar.Prev : Ar.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: v,
                  },
                  s().createElement("div", { ref: c, className: f()(wr, t.thumb) }),
                  s().createElement("div", { className: f()(Sr, t.rail) }),
                ),
                s().createElement("div", {
                  className: f()(Br, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Pr) ||
                      0 !== e.button ||
                      ((0, ee.G)("play"), h(Ar.Prev));
                  },
                  onMouseUp: C,
                  ref: i,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          Lr = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          Tr = ({
            children: e,
            api: t,
            className: a,
            barClassNames: u,
            areaClassName: r,
            classNames: o,
            scrollClassName: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, n.useMemo)(() => {
                const e = u || {};
                return Object.assign({}, e, { base: f()(Lr.base, e.base) });
              }, [u]),
              d = (0, n.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return s().createElement(
              "div",
              { className: f()(Lr.defaultScroll, a), onWheel: t.handleMouseWheel },
              s().createElement(
                "div",
                { className: f()(Lr.defaultScrollArea, r) },
                s().createElement(Mr, { className: i, api: d, classNames: o }, e),
              ),
              s().createElement(Nr, { getStepByRailClick: l, api: t, onDrag: c, classNames: _ }),
            );
          },
          Mr = ({ api: e, className: t, classNames: a, children: u, style: r }) => (
            (0, n.useEffect)(() => W(e.recalculateContent)),
            s().createElement(
              "div",
              { className: f()(Lr.base, t), style: r },
              s().createElement(
                "div",
                {
                  className: f()(Lr.wrapper, null == a ? void 0 : a.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                s().createElement(
                  "div",
                  { className: f()(Lr.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  u,
                ),
              ),
            )
          );
        ((Mr.Bar = Nr),
          (Mr.Default = Tr),
          (Mr.SeniorityAwards = ({ api: e, className: t, classNames: a, children: u }) => (
            (0, n.useEffect)(() => W(e.recalculateContent)),
            s().createElement(
              "div",
              { className: f()(Lr.base, t) },
              s().createElement(
                "div",
                { className: f()(Lr.wrapper, null == a ? void 0 : a.wrapper), ref: e.wrapperRef },
                s().createElement(
                  "div",
                  { className: f()(Lr.content, null == a ? void 0 : a.content), ref: e.contentRef },
                  u,
                ),
              ),
            )
          )));
        const Ir = hr({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Ar.Next : Ar.Prev),
          }),
          Or = "VerticalBar_base_f3",
          Hr = "VerticalBar_base__nonActive_42",
          Wr = "VerticalBar_topButton_d7",
          Gr = "VerticalBar_bottomButton_06",
          $r = "VerticalBar_track_df",
          Ur = "VerticalBar_thumb_32",
          zr = "VerticalBar_rail_43",
          Vr = "disable",
          jr = () => {},
          Xr = { pending: !1, offset: 0 },
          Yr = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          qr = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          Kr = (e, t) => Math.max(20, e.offsetHeight * t),
          Qr = (0, n.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = Yr, onDrag: u = jr }) => {
              const r = (0, n.useRef)(null),
                o = (0, n.useRef)(null),
                i = (0, n.useRef)(null),
                l = (0, n.useRef)(null),
                c = (0, n.useRef)(null),
                _ = e.stepTimeout || 100,
                d = (0, n.useState)(Xr),
                m = d[0],
                E = d[1],
                g = (0, n.useCallback)(
                  (e) => {
                    (E(e),
                      c.current &&
                        u({ type: e.pending ? "dragStart" : "dragEnd", thumb: c.current }));
                  },
                  [u],
                ),
                p = _r(() => {
                  const t = c.current,
                    a = l.current,
                    u = e.getWrapperSize(),
                    n = e.getContainerSize();
                  if (!(u && n && t && a)) return;
                  const s = Math.min(1, u / n);
                  return (
                    (t.style.height = `${Kr(a, s)}px`),
                    t.classList.add(Ur),
                    r.current &&
                      (1 === s ? r.current.classList.add(Hr) : r.current.classList.remove(Hr)),
                    s
                  );
                }),
                A = _r(() => {
                  const t = l.current,
                    a = c.current,
                    u = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(u && t && a && r)) return;
                  const n = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, u / r),
                    _ = lr(0, 1, n / (r - u)),
                    d = (t.offsetHeight - Kr(t, s)) * _;
                  ((a.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (o.current && i.current && l.current && c.current) {
                        if (0 === e)
                          return (o.current.classList.add(Vr), void i.current.classList.remove(Vr));
                        if (
                          ((t = l.current),
                          (a = c.current),
                          e - (t.offsetHeight - a.offsetHeight) >= -0.5)
                        )
                          return (o.current.classList.remove(Vr), void i.current.classList.add(Vr));
                        var t, a;
                        (o.current.classList.remove(Vr), i.current.classList.remove(Vr));
                      }
                    })(d));
                }),
                b = _r(() => {
                  qr(e, () => {
                    (p(), A());
                  });
                });
              ((0, n.useEffect)(() => W(b)),
                (0, n.useEffect)(() => {
                  const t = () => {
                    qr(e, () => {
                      A();
                    });
                  };
                  let a = jr;
                  const u = () => {
                    (a(), (a = W(b)));
                  };
                  return (
                    e.events.on("recalculateContent", b),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", u),
                    () => {
                      (a(),
                        e.events.off("recalculateContent", b),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", u));
                    }
                  );
                }, [e]),
                (0, n.useEffect)(() => {
                  if (!m.pending) return;
                  const t = (t) => {
                      qr(e, (a) => {
                        const r = l.current,
                          n = c.current,
                          s = e.getContainerSize();
                        if (!r || !n || !s) return;
                        const o = t.screenY - m.offset - r.getBoundingClientRect().y,
                          i = (o / r.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(a, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: a.scrollTop },
                        }),
                          u({ type: "dragging", thumb: n, thumbOffset: o, contentOffset: i }));
                      });
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        g(Xr));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, m.offset, m.pending, u, g]));
              const h = dr((t) => e.applyStepTo(t), _, [e]),
                C = h[0],
                v = h[1];
              (0, n.useEffect)(
                () => (
                  document.addEventListener("mouseup", v, !0),
                  () => document.removeEventListener("mouseup", v, !0)
                ),
                [v],
              );
              const D = (e) => {
                e.target.classList.contains(Vr) || (0, ee.G)("highlight");
              };
              return s().createElement(
                "div",
                { className: f()(Or, t.base), ref: r, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: f()(Wr, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Vr) ||
                      0 !== e.button ||
                      ((0, ee.G)("play"), C(Ar.Next));
                  },
                  ref: o,
                  onMouseEnter: D,
                }),
                s().createElement(
                  "div",
                  {
                    className: f()($r, t.track),
                    onMouseDown: (t) => {
                      const u = c.current;
                      if (u && 0 === t.button)
                        if (((0, ee.G)("play"), t.target === u))
                          (e.handleIsThumbDragging(!0),
                            g({ pending: !0, offset: t.screenY - u.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            c.current &&
                              qr(e, (u) => {
                                if (!u) return;
                                const r = a(e),
                                  n = e.clampPosition(u, u.scrollTop + r * t);
                                e.applyScroll(n);
                              });
                          })(t.screenY > u.getBoundingClientRect().y ? Ar.Prev : Ar.Next);
                        }
                    },
                    ref: l,
                    onMouseEnter: D,
                  },
                  s().createElement("div", { ref: c, className: t.thumb }),
                  s().createElement("div", { className: f()(zr, t.rail) }),
                ),
                s().createElement("div", {
                  className: f()(Gr, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Vr) ||
                      0 !== e.button ||
                      ((0, ee.G)("play"), C(Ar.Prev));
                  },
                  onMouseUp: v,
                  ref: i,
                  onMouseEnter: D,
                }),
              );
            },
          ),
          Zr = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          Jr = ({
            children: e,
            api: t,
            className: a,
            barClassNames: u,
            areaClassName: r,
            scrollClassName: o,
            scrollClassNames: i,
            getStepByRailClick: l,
            onDrag: c,
          }) => {
            const _ = (0, n.useMemo)(() => {
                const e = u || {};
                return Object.assign({}, e, { base: f()(Zr.base, e.base) });
              }, [u]),
              d = (0, n.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return s().createElement(
              "div",
              { className: f()(Zr.defaultScroll, a), onWheel: t.handleMouseWheel },
              s().createElement(
                "div",
                { className: f()(Zr.area, r) },
                s().createElement(en, { className: o, classNames: i, api: d }, e),
              ),
              s().createElement(Qr, { getStepByRailClick: l, api: t, onDrag: c, classNames: _ }),
            );
          },
          en = ({ className: e, classNames: t, children: a, api: u }) => (
            (0, n.useEffect)(() => W(u.recalculateContent)),
            s().createElement(
              "div",
              { className: f()(Zr.base, e), ref: u.wrapperRef, onWheel: u.handleMouseWheel },
              s().createElement(
                "div",
                { className: f()(Zr.content, null == t ? void 0 : t.content), ref: u.contentRef },
                a,
              ),
            )
          );
        en.Default = Jr;
        const tn = { Vertical: r, Horizontal: u };
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
        let an, un, rn, nn, sn, on, ln, cn, _n;
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
        })(an || (an = {})),
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
          })(un || (un = {})),
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
          })(rn || (rn = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(nn || (nn = {})),
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
          })(sn || (sn = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(on || (on = {})),
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
          })(ln || (ln = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(cn || (cn = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(_n || (_n = {})));
        var dn = a(2372);
        const mn = [
            an.Items,
            an.Equipment,
            an.Xp,
            an.XpFactor,
            an.Blueprints,
            an.BlueprintsAny,
            an.Goodies,
            an.Berths,
            an.Slots,
            an.Tokens,
            an.CrewSkins,
            an.CrewBooks,
            an.Customizations,
            an.CreditsFactor,
            an.TankmenXp,
            an.TankmenXpFactor,
            an.FreeXpFactor,
            an.BattleToken,
            an.PremiumUniversal,
            an.NaturalCover,
            an.BpCoin,
            an.BattlePassSelectToken,
            an.BattlaPassFinalAchievement,
            an.BattleBadge,
            an.BonusX5,
            an.CrewBonusX3,
            an.NewYearFillers,
            an.NewYearInvoice,
            an.EpicSelectToken,
            an.Comp7TokenWeeklyReward,
            an.Comp7TokenCouponReward,
            an.BattleBoosterGift,
            an.CosmicLootboxCommon,
            an.CosmicLootboxSilver,
            an.SelectableBonus,
            an.PostStamp,
            an.PremiumPlusUniversal,
            an.GoldenTicket,
            an.RewardsSlots,
            an.WtStamp,
            an.WtTicket,
            an.WtMainPrizeDiscount,
            an.WtHunter,
            an.WtHunterCollection,
          ],
          En = [an.Gold, an.Credits, an.Crystal, an.FreeXp],
          gn = [an.BattlePassPoints],
          pn = [an.PremiumPlus, an.Premium];
        let An;
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
        })(An || (An = {}));
        const bn = ["engravings", "backgrounds"],
          hn = ["engraving", "background"],
          Cn = (e, t = rn.Small) => {
            const a = e.name,
              u = e.type,
              r = e.value,
              n = e.icon,
              s = e.item,
              o = e.dogTagType,
              i = ((e) => {
                switch (e) {
                  case rn.S600x450:
                    return "c_600x450";
                  case rn.S400x300:
                    return "c_400x300";
                  case rn.S296x222:
                    return "c_296x222";
                  case rn.S232x174:
                    return "c_232x174";
                  case rn.Big:
                    return "c_80x80";
                  case rn.Small:
                    return "c_48x48";
                  default:
                    return e;
                }
              })(t);
            switch (a) {
              case "basic":
              case "plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${u}_${r}`;
              case "premium":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}_plus_${r}`;
              case "premium_plus":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}_${r}`;
              case "items":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${s}`;
              case "blueprints":
              case "blueprintsAny":
              case "finalBlueprints":
                return `R.images.gui.maps.icons.blueprints.fragment.${t}.${n}`;
              case "tokens":
              case "battleToken":
                return ((e, t) => {
                  switch (t) {
                    case rn.Big:
                      return e.iconBig.replace("..", "img://gui");
                    case rn.Small:
                      return e.iconSmall.replace("..", "img://gui");
                    default:
                      return `R.images.gui.maps.icons.quests.bonuses.${t}.${e.icon}`;
                  }
                })(e, t);
              case "crewBooks":
                return `R.images.gui.maps.icons.crewBooks.books.${t}.${n}`;
              case "dogTagComponents":
                return ((e, t, a) => {
                  const u = bn[e];
                  if (u) {
                    const r = R.images.gui.maps.icons.dogtags.$dyn(t).$dyn(u),
                      n = r.$dyn(a);
                    return n ? `${n}` : `${r.$dyn(hn[e])}`;
                  }
                  return (
                    console.error(
                      "Unreachable branch: add dogTagType and icon folder for corresponding icon matching",
                    ),
                    ""
                  );
                })(o, t, n);
              case "dossier_badge":
                return `R.images.gui.maps.icons.quests.bonuses.badges.${i}.${n}`;
              case "dossier_achievement":
                return `R.images.gui.maps.icons.achievement.${((e) => {
                  switch (e) {
                    case rn.S600x450:
                      return "c_600x450";
                    case rn.S400x300:
                      return "c_400x300";
                    case rn.S296x222:
                      return "c_296x222";
                    case rn.S232x174:
                      return "c_232x174";
                    case rn.S180x135:
                      return "big";
                    case rn.Big:
                    case rn.S80x80:
                      return "c_80x80";
                    case rn.Small:
                    case rn.S48x48:
                      return "c_48x48";
                    default:
                      return e;
                  }
                })(t)}.${n}`;
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
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${n}`;
              case "premiumTank":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.vehicles`;
              case "styleProgressToken":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.style_3d`;
              case "collectionItem":
                return `R.images.gui.maps.icons.collectionItems.${i}.${n}`;
              case "premium_universal":
                return `R.images.gui.maps.icons.quests.bonuses.${t}.premium_plus_universal`;
              case "armory_coin":
                return `R.images.armory_yard.gui.maps.icons.token.sf${((e) => {
                  switch (e) {
                    case rn.Mini:
                      return An.s32;
                    case rn.Small:
                    case rn.S48x48:
                      return An.s48;
                    case rn.S80x80:
                    case rn.Big:
                      return An.s80;
                    case rn.S128x100:
                      return An.s116;
                    case rn.S180x135:
                    case rn.S232x174:
                    case rn.S296x222:
                      return An.s296;
                    case rn.S400x300:
                      return An.s400;
                    case rn.S600x450:
                      return An.s600;
                  }
                })(t)}`;
              case an.StyleProgress:
              case an.LbStyleProgress:
                return fn(n, t, _n.ProgressionStyle);
              default:
                return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}`;
            }
          },
          vn = (e, t, a) => {
            const u = t && { contentId: t };
            return Object.assign(
              {
                args: e,
                isEnabled: Boolean((e && e.tooltipId) || t),
                ignoreMouseClick: !0,
                ignoreShowDelay: !t,
              },
              u,
              a,
            );
          },
          fn = (e, t, a) => {
            const u = R.images.gui.maps.icons.quests.bonuses.$dyn(t),
              r = u.$dyn(e);
            return String(null != r ? r : u.$dyn(a));
          };
        let Dn, Bn;
        (!(function (e) {
          ((e.Active = "active"),
            (e.Paused = "paused"),
            (e.Completed = "completed"),
            (e.NotStarted = "notStarted"),
            (e.Disabled = "disabled"));
        })(Dn || (Dn = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(Bn || (Bn = {})));
        const Fn = (e) => {
          const t = ht[e];
          return (t || console.warn("Unknown FinalReward key: ", e), t);
        };
        let wn;
        !(function (e) {
          ((e.Dragging = "dragging"), (e.End = "scrollingToEnd"), (e.Idle = "idle"));
        })(wn || (wn = {}));
        const Sn = { type: wn.Idle };
        let Pn;
        !(function (e) {
          ((e[(e.MainButton = 0)] = "MainButton"),
            (e[(e.AuxiliaryButton = 1)] = "AuxiliaryButton"),
            (e[(e.SecondaryButton = 2)] = "SecondaryButton"),
            (e[(e.FourthButton = 3)] = "FourthButton"),
            (e[(e.FifthButton = 4)] = "FifthButton"));
        })(Pn || (Pn = {}));
        const yn = () => {
            const e = (0, n.useState)(i.O.view.getScale()),
              t = e[0],
              a = e[1];
            return (
              (0, n.useEffect)(() => {
                const e = () => {
                  a(i.O.view.getScale());
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
          kn = {
            base: "ArrowButton_base_8c",
            base__gray: "ArrowButton_base__gray_bd",
            icon: "ArrowButton_icon_af",
            icon__scale: "ArrowButton_icon__scale_e4",
            icon__back: "ArrowButton_icon__back_28",
            icon__forward: "ArrowButton_icon__forward_ff",
          };
        let xn;
        !(function (e) {
          ((e.Default = "default"), (e.Gray = "gray"));
        })(xn || (xn = {}));
        const Rn = ({
            onClick: e,
            direction: t,
            type: a = xn.Default,
            className: u,
            tooltipBody: r,
          }) => {
            const o = yn(),
              i = f()(kn.icon, kn[`icon__${t}`], o > 1 && kn.icon__scale),
              l = (0, n.useCallback)(() => {
                (0, ee.G)("highlight");
              }, []),
              c = (0, n.useCallback)(() => {
                ((0, ee.G)("bp_slide"), e());
              }, [e]);
            return s().createElement(
              ge.i,
              { body: r },
              s().createElement(
                "div",
                { className: f()(kn.base, kn[`base__${a}`], u), onClick: c, onMouseEnter: l },
                s().createElement("div", { className: i }),
              ),
            );
          },
          Nn = "Bookmark_base_cc",
          Ln = "Bookmark_container_72",
          Tn = "Bookmark_container__start_b1",
          Mn = "Bookmark_container__wide_14",
          In = "Bookmark_textWrapper_46",
          On = "Bookmark_withTooltip_58",
          Hn = "Bookmark_text_6f",
          Wn = "Bookmark_text__basic_01",
          Gn = "Bookmark_text__premium_b8",
          $n = "Bookmark_text__single_a0",
          Un = "Bookmark_text__wide_4c",
          zn = "Bookmark_text__disappeared_f2",
          Vn = "Bookmark_textInner_b4",
          jn = "Bookmark_leftTextLine_0a",
          Xn = "Bookmark_rightTextLine_37",
          Yn = ({ isWide: e, isDecorated: t }) => {
            const a = f()(Hn, $n, e && Un);
            return s().createElement(
              "div",
              { className: a },
              t && s().createElement("div", { className: jn }),
              s().createElement(
                "div",
                { className: Vn },
                R.strings.battle_pass.progression.postProgressionDescr(),
              ),
              t && s().createElement("div", { className: Xn }),
            );
          };
        class qn extends n.PureComponent {
          render() {
            const e = this.props,
              t = e.tooltipBody,
              a = e.tooltipTitle,
              u = e.children;
            return "string" == typeof t
              ? s().createElement(
                  ge.i,
                  { body: t, header: a },
                  s().createElement("div", { className: On }, u),
                )
              : { children: u };
          }
        }
        const Kn = (0, n.memo)(qn),
          Qn = (0, n.forwardRef)(
            (
              {
                isWide: e = !1,
                isDisappeared: t = !1,
                tooltipBody: a,
                tooltipTitle: u,
                chapterStep: r,
                mixClass: o,
              },
              i,
            ) => {
              const l = (0, n.useRef)(null);
              (0, n.useImperativeHandle)(i, () => ({
                width: () => {
                  const e = l.current;
                  if (e) {
                    const t = window.getComputedStyle(e, null).getPropertyValue("width");
                    return Number(t.split("rem")[0]);
                  }
                  return 0;
                },
              }));
              const c = (0, ae.uF)(R.strings.battle_pass.tooltips.postProgress.body(), {
                  chapterStep: r,
                }),
                _ = f()(Nn, o),
                d = f()(Ln, e && Mn, !e && Tn),
                m = f()(Hn, Wn, t && zn),
                E = f()(Hn, Gn);
              return s().createElement(
                "div",
                { className: _, ref: l },
                s().createElement(
                  "div",
                  { className: d },
                  e
                    ? s().createElement(
                        Kn,
                        { tooltipBody: a, tooltipTitle: u },
                        s().createElement(Yn, { isWide: e, isDecorated: !0 }),
                      )
                    : s().createElement(
                        s().Fragment,
                        null,
                        s().createElement(
                          "div",
                          { className: In },
                          s().createElement(
                            ge.i,
                            {
                              header: R.strings.battle_pass.tooltips.postProgress.header(),
                              body: c,
                            },
                            s().createElement(Yn, { isWide: e }),
                          ),
                        ),
                        s().createElement(
                          Kt.u,
                          {
                            contentId:
                              R.views.lobby.battle_pass.tooltips.BattlePassLockIconTooltipView(
                                "resId",
                              ),
                          },
                          s().createElement(
                            "div",
                            { className: E },
                            R.strings.battle_pass.progression.premiumProgressionDescr(),
                          ),
                        ),
                        s().createElement(
                          "div",
                          { className: m },
                          R.strings.battle_pass.progression.baseProgressionDescr(),
                        ),
                      ),
                ),
              );
            },
          ),
          Zn = "CrewReward_base_60",
          Jn = "CrewReward_baseWrapper_38",
          es = "CrewReward_infoWrapper_6c",
          ts = "CrewReward_crewDescription_93",
          as = "CrewReward_name_9b",
          us = "CrewReward_skillWrapper_cd",
          rs = "CrewReward_skillBackground_3f",
          ns = "CrewReward_skill_91",
          ss =
            R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent("resId"),
          os = R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
          is = (0, te.Pi)(() => {
            const e = Se().model,
              t = e.chapterCharacter.get(),
              a = t.tankman,
              u = t.tooltipId,
              r = e.computes.getCharacterSkills(),
              o = ss,
              i = o === ss ? os : void 0,
              l = (0, n.useMemo)(() => ({ tooltipId: u }), [u]);
            return s().createElement(
              Kt.u,
              {
                ignoreShowDelay: !0,
                ignoreMouseClick: !0,
                contentId: o,
                decoratorId: i,
                isEnabled: !0,
                args: l,
              },
              s().createElement(
                "div",
                { className: Zn },
                s().createElement(
                  "div",
                  { className: Jn },
                  s().createElement(
                    "div",
                    { className: es },
                    s().createElement(
                      "div",
                      { className: ts },
                      s().createElement("div", { className: as }, a),
                    ),
                    s().createElement(
                      "div",
                      { className: us },
                      s().createElement("div", { className: rs }),
                      r.map((e, t) =>
                        s().createElement("div", {
                          className: ns,
                          key: t,
                          style: {
                            backgroundImage: `url('img://gui/maps/icons/battlePass/tooltips/icons/icon_perk_${e}.png')`,
                          },
                        }),
                      ),
                    ),
                  ),
                ),
              ),
            );
          });
        let ls, cs, _s, ds, ms;
        (!(function (e) {
          ((e.left = "left"), (e.right = "right"));
        })(ls || (ls = {})),
          (function (e) {
            ((e.COMPLETED = "completed"),
              (e.IN_PROGRESS = "inProgress"),
              (e.NOT_STARTED = "notStarted"),
              (e.DISABLED = "disabled"),
              (e.COMPLETED_TROPHY_NOT_SELECTED = "completedTrophyNotSelected"));
          })(cs || (cs = {})),
          (function (e) {
            ((e.UNLOCK_BIG = "bp_unlock_big"),
              (e.UNLOCK_SMALL = "bp_unlock_small"),
              (e.IMPROVED_REWARD = "bp_improved_reward"));
          })(_s || (_s = {})),
          (function (e) {
            ((e.back = "back"), (e.forward = "forward"));
          })(ds || (ds = {})),
          (function (e) {
            ((e.Default = "default"), (e.Gray = "gray"));
          })(ms || (ms = {})));
        var Es = a(1481);
        const gs = "VehicleInfo_base_b3",
          ps = "VehicleInfo_prefix_f6",
          As = "VehicleInfo_type_1b",
          bs = R.strings.battle_pass.progression.widget3dStyle,
          hs = (0, n.memo)(({ vehicleLvl: e, vehicleName: t, vehicleType: a, isElite: u }) => {
            const r = (0, n.useMemo)(() => {
              const e = (0, ae.BN)(a);
              return {
                backgroundImage: `url(${R.images.gui.maps.icons.vehicleTypes.big.$dyn(`${e}${u ? "_elite" : ""}`)})`,
              };
            }, [a, u]);
            return s().createElement(
              "div",
              { className: gs },
              s().createElement("div", { className: ps }, bs.forVehicle()),
              ia(e),
              s().createElement("div", { className: As, style: r }),
              t,
            );
          }),
          Cs = "Widget3dStyle_base_ae",
          vs = "Widget3dStyle_title_20",
          fs = "Widget3dStyle_base__closedChapter_d4",
          Ds = "Widget3dStyle_box_f8",
          Bs = "Widget3dStyle_light_82",
          Fs = "Widget3dStyle_previewButton_03",
          ws = "Widget3dStyle_box__hover_39",
          Ss = "Widget3dStyle_footer_b9",
          Ps = "Widget3dStyle_caption_2b",
          ys = R.strings.battle_pass.progression.widget3dStyle,
          ks = (0, te.Pi)(
            ({ widget3dStyleRef: e, overScrollWidth: t, level: a, isShowTitle: u }) => {
              const r = (0, n.useState)(!1),
                o = r[0],
                i = r[1],
                l = Se(),
                c = l.model,
                _ = l.controls,
                d = c.root.get(),
                m = d.chapterState,
                E = d.isStyleTaken,
                g = c.widget3dStyle.get().styleName,
                p = _.on3dStylePreview,
                A = c.vehicleInfo.get(),
                b = { marginRight: `-${t}`, marginLeft: t },
                h = (0, ae.uF)(ys.currentStyle(), { name: g }),
                C = (0, n.useCallback)(() => {
                  p({ level: a });
                }, [p, a]),
                v = m === lt.Completed,
                D = f()(Cs, v && fs),
                B = f()(Ds, o && ws);
              return s().createElement(
                "div",
                { className: D, ref: e, style: b },
                !E && u && s().createElement("div", { className: vs }, ys.titleNoChapterSelected()),
                s().createElement(
                  "div",
                  {
                    className: B,
                    onMouseEnter: () => {
                      i(!0);
                    },
                    onMouseLeave: () => {
                      i(!1);
                    },
                  },
                  !E && 1 === a && s().createElement("div", { className: Bs }),
                  s().createElement(
                    "div",
                    { className: Fs },
                    s().createElement(Es.k, { onClick: C }),
                  ),
                ),
                s().createElement(
                  "div",
                  { className: Ss },
                  s().createElement("div", { className: Ps }, h),
                  s().createElement(hs, A),
                ),
              );
            },
          ),
          xs = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let Rs, Ns;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(Rs || (Rs = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(Ns || (Ns = {})));
        const Ls = ({ size: e = Rs.Default, classMix: t }) =>
            s().createElement("div", { className: f()(xs.background, xs[`background__${e}`], t) }),
          Ts = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          Ms = ({ size: e }) => {
            const t = f()(Ts.base, Ts[`base__${e}`]);
            return s().createElement("div", { className: t });
          },
          Is = {
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
          Os = (0, n.memo)(
            ({
              size: e,
              lineRef: t,
              disabled: a,
              baseStyles: u,
              isComplete: r,
              withoutBounce: n,
            }) => {
              const o = f()(
                  Is.base,
                  Is[`base__${e}`],
                  a && Is.base__disabled,
                  r && Is.base__finished,
                  n && Is.base__withoutBounce,
                ),
                i = !a && !r;
              return s().createElement(
                "div",
                { className: o, style: u, ref: t },
                s().createElement("div", { className: Is.pattern }),
                s().createElement("div", { className: Is.gradient }),
                i && s().createElement(Ms, { size: e }),
              );
            },
          ),
          Hs = ({ size: e, value: t, lineRef: a, disabled: u, onComplete: r }) => {
            const o = (0, n.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
              i = 100 === t;
            return (
              (0, n.useEffect)(() => {
                i && r && r();
              }, [i, r]),
              s().createElement(Os, {
                size: e,
                disabled: u,
                baseStyles: o,
                isComplete: i,
                lineRef: a,
              })
            );
          };
        let Ws, Gs;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(Ws || (Ws = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(Gs || (Gs = {})));
        const $s = "ProgressBarDeltaSimple_base_6c",
          Us = "ProgressBarDeltaSimple_delta_99",
          zs = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: u,
              size: r,
              to: o,
              onEndAnimation: i,
              onChangeAnimationState: l,
            }) => {
              const c = o < u,
                _ = (0, n.useState)(Gs.Idle),
                d = _[0],
                m = _[1],
                E = d === Gs.In,
                g = d === Gs.End,
                p = d === Gs.Idle,
                A = (0, n.useCallback)(
                  (e) => {
                    (m(e), l && l(e));
                  },
                  [l],
                );
              ((0, n.useEffect)(() => {
                if (p && !a) {
                  return Ta(() => {
                    A(Gs.In);
                  }, t);
                }
              }, [A, a, p, t]),
                (0, n.useEffect)(() => {
                  if (E) {
                    return Ta(() => {
                      (i && i(), A(Gs.End));
                    }, e + t);
                  }
                }, [A, E, i, t, e]));
              const b = (0, n.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                h = (0, n.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${t}ms`,
                    [c ? "left" : "right"]: "0",
                  }),
                  [c, t, e],
                ),
                C = (0, n.useMemo)(
                  () => ({ width: `${Math.abs(u - o)}%`, left: `${c ? o : u}%` }),
                  [u, c, o],
                );
              return g
                ? null
                : s().createElement(
                    "div",
                    { className: $s, style: C },
                    s().createElement(
                      "div",
                      { style: p ? b : h, className: Us },
                      s().createElement(Ms, { size: r }),
                    ),
                  );
            },
          ),
          Vs = (0, n.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: u,
              disabled: r,
              isComplete: o,
              animationSettings: i,
              onChangeAnimationState: l,
              onEndAnimation: c,
            }) => {
              const _ = (0, n.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${i.line.duration}ms`,
                  transitionDelay: `${i.line.delay}ms`,
                }),
                [i.line.delay, i.line.duration, e],
              );
              return s().createElement(
                s().Fragment,
                null,
                s().createElement(Os, {
                  size: t,
                  lineRef: u,
                  disabled: r,
                  isComplete: o,
                  baseStyles: _,
                }),
                a >= 0 &&
                  s().createElement(zs, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    freezed: i.freezed,
                    from: a,
                    size: t,
                    to: e,
                    onChangeAnimationState: l,
                    onEndAnimation: c,
                  }),
              );
            },
          ),
          js = "ProgressBarDeltaGrow_base_7e",
          Xs = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          Ys = "ProgressBarDeltaGrow_glow_68",
          qs = (e) => (e ? { left: 0 } : { right: 0 }),
          Ks = (e, t) => (e ? { right: 100 - t + "%" } : { left: `${t}%` }),
          Qs = (e) => ({ transitionDuration: `${e}ms` }),
          Zs = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: t,
              freezed: a,
              from: u,
              size: r,
              to: o,
              onEndAnimation: i,
              onChangeAnimationState: l,
              className: c,
            }) => {
              const _ = o < u,
                d = (0, n.useState)(Ws.Idle),
                m = d[0],
                E = d[1],
                g = m === Ws.End,
                p = m === Ws.Idle,
                A = m === Ws.Grow,
                b = m === Ws.Shrink,
                h = (0, n.useCallback)(
                  (e) => {
                    (E(e), l && l(e));
                  },
                  [l],
                ),
                C = (0, n.useCallback)(
                  (e, t) =>
                    Ta(() => {
                      h(e);
                    }, t),
                  [h],
                );
              (0, n.useEffect)(() => {
                if (!a)
                  return p
                    ? C(Ws.Grow, t)
                    : A
                      ? C(Ws.Shrink, e)
                      : b
                        ? C(Ws.End, e)
                        : void (g && i && i());
              }, [C, a, g, A, p, b, i, t, e]);
              const v = (0, n.useMemo)(
                  () => Object.assign({ width: "100%" }, Qs(e), qs(_)),
                  [_, e],
                ),
                D = (0, n.useMemo)(() => Object.assign({ width: "0%" }, Qs(e), qs(_)), [_, e]),
                B = (0, n.useMemo)(
                  () => Object.assign({ width: "0%" }, Ks(_, u), Qs(e)),
                  [u, _, e],
                ),
                F = (0, n.useMemo)(
                  () => Object.assign({ width: `${Math.abs(o - u)}%` }, Ks(_, u), Qs(e)),
                  [u, _, o, e],
                );
              if (g) return null;
              const w = f()(js, c, _ && 0 === o && Xs);
              return s().createElement(
                "div",
                { style: p ? B : F, className: w },
                s().createElement(
                  "div",
                  { style: b ? D : v, className: Ys },
                  s().createElement(Ms, { size: r }),
                ),
              );
            },
          ),
          Js = (0, n.memo)(
            ({
              to: e,
              size: t,
              from: a,
              lineRef: u,
              disabled: r,
              isComplete: o,
              animationSettings: i,
              onEndAnimation: l,
              onChangeAnimationState: c,
            }) => {
              const _ = e < a,
                d = (0, n.useState)(!1),
                m = d[0],
                E = d[1],
                g = (0, n.useCallback)(
                  (e) => {
                    (e === Ws.Shrink && E(!0), c && c(e));
                  },
                  [c],
                ),
                p = (0, n.useMemo)(() => ({ width: `${a}%`, transitionProperty: "none" }), [a]),
                A = (0, n.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${i.line.duration}ms` }),
                  [i.line.duration, e],
                );
              return s().createElement(
                s().Fragment,
                null,
                s().createElement(Os, {
                  size: t,
                  lineRef: u,
                  disabled: r,
                  isComplete: o,
                  withoutBounce: _ && 0 === e,
                  baseStyles: m ? A : p,
                }),
                a >= 0 &&
                  s().createElement(Zs, {
                    transitionDuration: i.delta.duration,
                    transitionDelay: i.delta.delay,
                    onChangeAnimationState: g,
                    freezed: i.freezed,
                    onEndAnimation: l,
                    from: a,
                    size: t,
                    to: e,
                    className: i.delta.className,
                  }),
              );
            },
          ),
          eo = ["onComplete", "onEndAnimation"];
        function to() {
          return (
            (to =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            to.apply(this, arguments)
          );
        }
        const ao = (0, n.memo)((e) => {
            let t = e.onComplete,
              a = e.onEndAnimation,
              u = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, eo);
            const r = (0, n.useState)(!1),
              o = r[0],
              i = r[1],
              l = (0, n.useCallback)(() => {
                const e = 100 === u.to;
                (e !== o && i(e), e && t && t(), a && a());
              }, [o, t, a, u.to]);
            switch (u.animationSettings.type) {
              case Ns.Simple:
                return s().createElement(Vs, to({}, u, { onEndAnimation: l, isComplete: o }));
              case Ns.Growing:
                return s().createElement(Js, to({}, u, { onEndAnimation: l, isComplete: o }));
              default:
                return null;
            }
          }),
          uo = ["onEndAnimation"];
        function ro() {
          return (
            (ro =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            ro.apply(this, arguments)
          );
        }
        const no = (0, n.memo)((e) => {
          let t = e.onEndAnimation,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                u,
                r = {},
                n = Object.keys(e);
              for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, uo);
          const u = (0, n.useRef)({}),
            r = (0, n.useCallback)(() => {
              ((u.current.from = void 0), t && t());
            }, [t]),
            o = "number" == typeof u.current.from ? u.current.from : a.from;
          return (
            (u.current.from = o),
            s().createElement(ao, ro({}, a, { onEndAnimation: r, key: `${o}-${a.to}`, from: o }))
          );
        });
        function so() {
          return (
            (so =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            so.apply(this, arguments)
          );
        }
        const oo = (0, n.memo)(
            ({
              size: e,
              value: t,
              lineRef: a,
              disabled: u,
              deltaFrom: r,
              animationSettings: n,
              onEndAnimation: o,
              onChangeAnimationState: i,
              onComplete: l,
            }) => {
              if (r === t)
                return s().createElement(Hs, {
                  key: `${r}-${t}`,
                  size: e,
                  value: t,
                  lineRef: a,
                  disabled: u,
                  onComplete: l,
                });
              const c = {
                from: r,
                to: t,
                size: e,
                lineRef: a,
                disabled: u,
                animationSettings: n,
                onComplete: l,
                onEndAnimation: o,
                onChangeAnimationState: i,
              };
              return n.withStack
                ? s().createElement(no, c)
                : s().createElement(ao, so({ key: `${r}-${t}` }, c));
            },
          ),
          io = (e) => ({
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
          lo = {
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
          co = {
            bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_grey",
            line: { bgColorBase: "#ссс", bgColorDisabled: "transparent", bgColorFinished: "#ссс" },
            pattern: {
              bgImageBase: "R.images.gui.maps.icons.components.progress_bar.pattern_light_grey",
              bgImageDisabled: "R.images.gui.maps.icons.components.progress_bar.pattern_disabled",
              bgImageFinished: "R.images.gui.maps.icons.components.progress_bar.pattern_light_grey",
            },
            glow: "R.images.gui.maps.icons.battlePass.progression.progress_glow_white",
            glowSmall: "R.images.gui.maps.icons.components.progress_bar.glow_small",
            delta: {
              color: "#fff",
              shadow:
                "0 0 4px 1px #ffaa0066, 0 0 9px 1px #ffaa0066, 0 0 12px 2px #ff550066, 0 0 12px 4px #ff000066",
            },
          },
          _o = (e, t, a) => {
            if ("number" == typeof a) {
              return (lr(0, t, a) / t) * 100;
            }
            return e;
          },
          mo = lo,
          Eo = {
            freezed: !1,
            withStack: !1,
            type: Ns.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          go = (0, n.memo)(
            ({
              maxValue: e = 100,
              theme: t = mo,
              size: a = Rs.Default,
              animationSettings: u = Eo,
              disabled: r = !1,
              withoutBackground: o = !1,
              progressBarBackgroundClassMix: i,
              value: l,
              deltaFrom: c,
              lineRef: _,
              onChangeAnimationState: d,
              onEndAnimation: m,
              onComplete: E,
            }) => {
              const g = ((e, t, a) =>
                (0, n.useMemo)(() => {
                  const u = (lr(0, t, e) / t) * 100;
                  return { value: u, deltaFrom: _o(u, t, a) };
                }, [a, t, e]))(l, e, c);
              return s().createElement(
                "div",
                { className: f()(xs.base, xs[`base__${a}`]), style: io(t) },
                !o && s().createElement(Ls, { size: a, classMix: i }),
                s().createElement(oo, {
                  size: a,
                  lineRef: _,
                  disabled: r,
                  value: g.value,
                  deltaFrom: g.deltaFrom,
                  animationSettings: u,
                  onEndAnimation: m,
                  onChangeAnimationState: d,
                  onComplete: E,
                }),
              );
            },
          ),
          po = "OptimizedProgressBar_base_1f",
          Ao = "OptimizedProgressBar_wrapper_ab",
          bo = "OptimizedProgressBar_background_ce",
          ho = ["api", "value", "maxValue", "theme"];
        function Co() {
          return (
            (Co =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            Co.apply(this, arguments)
          );
        }
        const vo = (e, t) => ("number" == typeof t ? t : e.offsetLeft),
          fo = (e) => {
            let t = e.api,
              a = e.value,
              u = e.maxValue,
              r = void 0 === u ? 100 : u,
              o = e.theme,
              i = void 0 === o ? mo : o,
              l = (function (e, t) {
                if (null == e) return {};
                var a,
                  u,
                  r = {},
                  n = Object.keys(e);
                for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, ho);
            const c = (0, n.useRef)(null),
              _ = (0, n.useRef)(null),
              d = (0, n.useRef)(null),
              m = lr(0, a, r) / r,
              E = (0, n.useCallback)(
                (e) => {
                  (d.current &&
                    c.current &&
                    (({ horizontalScrollPosition: e, leftOffset: t }, a, u) => {
                      const r = a.offsetWidth - u.offsetWidth,
                        n = e - vo(a, t),
                        s = lr(0, r, n);
                      u.style.left = `${s}px`;
                    })(e, c.current, d.current),
                    _.current &&
                      c.current &&
                      ((
                        { horizontalScrollPosition: e, leftOffset: t },
                        a,
                        { container: u, line: r },
                      ) => {
                        const n = Math.max(0, Math.floor(u.offsetWidth * a) - 8e3),
                          s = e - vo(u, t),
                          o = lr(0, n, s);
                        r.style.left = `${o}px`;
                      })(e, m, { line: _.current, container: c.current }));
                },
                [m],
              ),
              g = (0, n.useMemo)(() => io(i), [i]);
            return (
              (t.current.update = E),
              s().createElement(
                "div",
                { className: po, ref: c },
                s().createElement(
                  "div",
                  { className: Ao },
                  s().createElement(
                    "div",
                    { style: g, className: f()(bo, l.progressBarBackgroundClassMix), ref: d },
                    s().createElement(Ls, {
                      size: l.size,
                      classMix: l.progressBarBackgroundClassMix,
                    }),
                  ),
                  s().createElement(
                    go,
                    Co({}, l, {
                      lineRef: _,
                      value: a,
                      theme: i,
                      maxValue: r,
                      withoutBackground: !0,
                    }),
                  ),
                ),
              )
            );
          },
          Do = ({
            level: e,
            levelWidth: t,
            currentLevelWidth: a,
            pointsInLevel: u,
            totalPointsInLevel: r,
            currentLevel: n,
          }) => (e > n ? a + t * (e - 2) + t * (u / r) : (e - 1) * t + a * (u / r)),
          Bo = (e) => e + 1,
          Fo = (0, te.Pi)(
            ({
              api: e,
              progressChange: t,
              levelWidth: a,
              currentLevelWidth: u,
              level: r,
              previousLevel: o,
              currentPointsInLevel: i,
              previousPointsInLevel: l,
              currentPointsInChapter: c,
              previousPointsInChapter: _,
              theme: d,
            }) => {
              const m = (0, n.useContext)(wi).levels,
                E = Se().model.root.get(),
                g = E.isPaused,
                p = E.showLevelsAnimations,
                A = E.currentLevel,
                b = (0, n.useState)(0),
                h = b[0],
                C = b[1],
                v = (0, n.useRef)(-1),
                f = (0, n.useState)({
                  previousBaseEarnedPoints: 0,
                  maxBasePoints: 0,
                  baseProgressionSize: 0,
                }),
                D = f[0],
                B = D.previousBaseEarnedPoints,
                F = D.maxBasePoints,
                w = D.baseProgressionSize,
                S = f[1];
              (0, n.useEffect)(() => {
                if (g) return;
                const e = v.current !== _,
                  t = e ? o : r,
                  n = u + (m.items.length - 1) * a,
                  s = m.items[t - 1],
                  d = r <= m.items.length ? r - 1 : m.items.length - 1,
                  E = m.items[d].value.levelPoints,
                  p = Do({
                    level: r,
                    levelWidth: a,
                    currentLevelWidth: u,
                    pointsInLevel: i,
                    totalPointsInLevel: E,
                    currentLevel: A,
                  }),
                  b = s ? s.value.levelPoints : 0,
                  h = Do({
                    level: t > r ? r : t,
                    levelWidth: a,
                    currentLevelWidth: t < A ? a : u,
                    pointsInLevel: l,
                    totalPointsInLevel: b,
                    currentLevel: A,
                  }),
                  C = e && t <= r ? h : p;
                (_ !== c && a && (v.current = _),
                  S({ maxBasePoints: n, previousBaseEarnedPoints: C, baseProgressionSize: p }));
              }, [g, a, u, r, o, c, l, i, _, A, m.items]);
              const P = (0, n.useMemo)(
                () =>
                  Object.assign({}, Eo, {
                    withStack: !0,
                    type: Ns.Simple,
                    delta: { duration: 400, delay: 300 },
                    line: { duration: 400, delay: 300 },
                  }),
                [],
              );
              return (
                (0, n.useEffect)(() => {
                  const e = A !== o || i !== l;
                  if (p) C(Bo);
                  else if (e && -1 === v.current)
                    return Ta(() => {
                      C(Bo);
                    }, 700);
                }, [A, i, o, l, p]),
                (0, n.useEffect)(() => {
                  if (p)
                    return W(() => {
                      t && t();
                    });
                }, [t, p]),
                s().createElement(fo, {
                  key: h,
                  animationSettings: P,
                  deltaFrom: B,
                  value: w,
                  maxValue: F,
                  api: e,
                  theme: d,
                })
              );
            },
          ),
          wo = R.strings.battle_pass.tooltips.progression.freePoints,
          So = (0, te.Pi)(
            ({
              progressApi: e,
              freePointsApi: t,
              levelWidth: a,
              currentLevelWidth: u,
              progressChange: r,
            }) => {
              const o = (0, n.useContext)(wi),
                i = o.levels,
                l = o.chapterState,
                c = o.currentPointsInLevel,
                _ = Se().model.root.get(),
                d = _.previousPointsInLevel,
                m = _.currentPointsInChapter,
                E = _.previousPointsInChapter,
                g = _.freePointsInLevel,
                p = _.freePointsInChapter,
                A = _.previousFreePointsInChapter,
                b = _.previousFreePointsInLevel,
                h = _.potentialLevel,
                C = _.previousPotentialLevel,
                v = _.chapterType,
                D = _.currentLevel,
                B = _.previousLevel,
                F = yn(),
                w = (l === lt.NotStarted || l === lt.Paused) && p - m > 0,
                S = i.items[i.items.length - 1].value.levelPoints,
                P = ((D - 1) * a + (c / S) * u) / F,
                y = m >= i.items.length * S,
                k = (0, n.useMemo)(
                  () => ({
                    "--progress-line-base": lo.line.bgColorBase,
                    "--progress-line-disabled": lo.line.bgColorDisabled,
                    "--progress-line-finished": lo.line.bgColorFinished,
                  }),
                  [],
                );
              return s().createElement(
                "div",
                { className: ir.progressContainer },
                w &&
                  s().createElement(
                    ge.i,
                    { header: wo.header(), body: wo.body.$dyn(v) },
                    s().createElement(
                      "div",
                      { className: ir.progress },
                      s().createElement(Fo, {
                        api: t,
                        progressChange: r,
                        levelWidth: a,
                        currentLevelWidth: u,
                        level: h,
                        previousLevel: C,
                        currentPointsInLevel: g,
                        previousPointsInLevel: b,
                        currentPointsInChapter: p,
                        previousPointsInChapter: A,
                        theme: co,
                      }),
                    ),
                  ),
                s().createElement("div", {
                  className: f()(ir.progressBackground, y && ir.progressBackground__finished),
                  style: Object.assign({ width: `${P}rem` }, k),
                }),
                s().createElement(
                  Kt.u,
                  { contentId: R.views.lobby.battle_pass.tooltips.BattlePassPointsView("resId") },
                  s().createElement(
                    "div",
                    { className: f()(ir.progress, w && ir.progress__inactive) },
                    s().createElement(Fo, {
                      api: e,
                      levelWidth: a,
                      currentLevelWidth: u,
                      level: D,
                      previousLevel: B,
                      currentPointsInLevel: c,
                      previousPointsInLevel: d,
                      currentPointsInChapter: m,
                      previousPointsInChapter: E,
                      progressChange: r,
                    }),
                  ),
                ),
              );
            },
          );
        let Po;
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
        })(Po || (Po = {}));
        Date.now();
        $.Sw.instance;
        const yo = {
            base: "Background_base_f7",
            default: "Background_default_c1",
            default__premium: "Background_default__premium_d5",
            default__normal: "Background_default__normal_15",
            default__rare: "Background_default__rare_4a",
            normalCompleted: "Background_normalCompleted_e0",
            normalCompleted__premium: "Background_normalCompleted__premium_a4",
            normalCompleted__disabled: "Background_normalCompleted__disabled_52",
            rare: "Background_rare_b6",
            rare__premium: "Background_rare__premium_2e",
            rareBg: "Background_rareBg_ee",
            rare__completed: "Background_rare__completed_85",
            rare__notStarted: "Background_rare__notStarted_3f",
            rarePattern: "Background_rarePattern_03",
            rarePattern__left: "Background_rarePattern__left_8b",
            rarePattern__leftCompleted: "Background_rarePattern__leftCompleted_3f",
            rarePattern__leftIndent: "Background_rarePattern__leftIndent_e2",
            rarePattern__leftNoIndent: "Background_rarePattern__leftNoIndent_ac",
            rarePattern__right: "Background_rarePattern__right_c2",
            rarePattern__rightCompleted: "Background_rarePattern__rightCompleted_eb",
            rarePattern__rightNoIndent: "Background_rarePattern__rightNoIndent_f1",
            rarePattern__rightIndent: "Background_rarePattern__rightIndent_f7",
            rare__completedEnabled: "Background_rare__completedEnabled_b0",
            rare__completedDisabled: "Background_rare__completedDisabled_a6",
            rare__notStartedEnabled: "Background_rare__notStartedEnabled_62",
            rare__notStartedDisabled: "Background_rare__notStartedDisabled_7f",
            disabled: "Background_disabled_ba",
            disabled__premium: "Background_disabled__premium_6d",
            inProgress: "Background_inProgress_68",
            inProgress__premium: "Background_inProgress__premium_8e",
            inProgressInner: "Background_inProgressInner_0d",
            inProgressPart: "Background_inProgressPart_68",
            inProgressPart__left: "Background_inProgressPart__left_76",
            inProgressPart__right: "Background_inProgressPart__right_5b",
          },
          ko = ({ status: e, chapterState: t, isPremium: a, isPremiumActivated: u, isRare: r }) => {
            const n = a && !u,
              o = e === cs.IN_PROGRESS,
              i = e === cs.COMPLETED || e === cs.COMPLETED_TROPHY_NOT_SELECTED,
              l = e === cs.NOT_STARTED,
              c = e === cs.DISABLED || t === lt.Disabled,
              _ = f()(
                yo.default,
                !n && !r && yo.default__normal,
                !n && r && yo.default__rare,
                a ? yo.default__premium : yo.default__basic,
              ),
              d = f()(
                yo.normalCompleted,
                a && yo.normalCompleted__premium,
                n ? yo.normalCompleted__disabled : yo.normalCompleted__enabled,
              ),
              m = f()(
                yo.rare,
                a && yo.rare__premium,
                i && yo.rare__completed,
                i && !a && yo.rare__completedEnabled,
                a && i && (n ? yo.rare__completedDisabled : yo.rare__completedEnabled),
                l && yo.rare__notStarted,
                a && l && (n ? yo.rare__notStartedDisabled : yo.rare__notStartedEnabled),
              ),
              E = f()(
                yo.rarePattern,
                i ? yo.rarePattern__leftCompleted : yo.rarePattern__left,
                ((i && !a) || (l && a)) && yo.rarePattern__leftIndent,
                ((l && !a) || (i && a)) && yo.rarePattern__leftNoIndent,
              ),
              g = f()(
                yo.rarePattern,
                i ? yo.rarePattern__rightCompleted : yo.rarePattern__right,
                ((i && !a) || (l && a)) && yo.rarePattern__rightNoIndent,
                ((l && !a) || (i && a)) && yo.rarePattern__rightIndent,
              ),
              p = f()(yo.inProgress, a && yo.inProgress__premium),
              A = f()(yo.inProgressInner, a && yo.inProgressInner__premium),
              b = f()(yo.inProgressPart, yo.inProgressPart__left),
              h = f()(yo.inProgressPart, yo.inProgressPart__right),
              C = f()(yo.disabled, a && yo.disabled__premium);
            return s().createElement(
              "div",
              { className: yo.base },
              (c || n) && s().createElement("div", { className: C }),
              s().createElement("div", { className: _ }),
              i && !r && s().createElement("div", { className: d }),
              o &&
                s().createElement(
                  "div",
                  { className: p },
                  s().createElement("div", { className: b }),
                  !a && s().createElement("div", { className: A }),
                  s().createElement("div", { className: h }),
                ),
              r &&
                !o &&
                s().createElement(
                  "div",
                  { className: m },
                  s().createElement("div", { className: E }),
                  s().createElement("div", { className: g }),
                  s().createElement("div", { className: yo.rareBg }),
                ),
            );
          };
        var xo = a(8664);
        const Ro = {
            base: "Stage_base_46",
            base__notStarted: "Stage_base__notStarted_86",
            number: "Stage_number_1f",
            numberAnimated: "Stage_numberAnimated_c6",
            numberAnimated__enter: "Stage_numberAnimated__enter_98",
            numberAnimated__enterActive: "Stage_numberAnimated__enterActive_1a",
            highlightScale: "Stage_highlightScale_6b",
            numberAnimated__enterDone: "Stage_numberAnimated__enterDone_68",
            numberGlow: "Stage_numberGlow_b7",
            numberGlow__active: "Stage_numberGlow__active_3c",
            circleOut: "Stage_circleOut_87",
            numberGlow__exit: "Stage_numberGlow__exit_d9",
            numberInProgress: "Stage_numberInProgress_69",
            title: "Stage_title_ee",
            glow: "Stage_glow_9e",
            glow__inProgress: "Stage_glow__inProgress_6a",
            iconFinal: "Stage_iconFinal_70",
            iconFinal__inProgress: "Stage_iconFinal__inProgress_c1",
          },
          No = R.strings.battle_pass.progression,
          Lo = (0, te.Pi)(
            ({
              status: e,
              stepNumber: t,
              isFinal: a,
              showLevelsAnimations: u,
              stageAnimationDelay: r,
            }) => {
              const o = Se(),
                i = o.model,
                l = o.controls,
                c = i.root.get().chapterState,
                _ = l.onLevelsAnimationFinished,
                d = (0, n.useState)(!1),
                m = d[0],
                E = d[1],
                g = e === cs.IN_PROGRESS,
                p = e === cs.COMPLETED,
                A = c === lt.NotStarted || c === lt.Paused,
                b = g ? Ro.numberInProgress : Ro.number,
                h = {
                  enter: Ro.numberAnimated__enter,
                  enterActive: Ro.numberAnimated__enterActive,
                  enterDone: Ro.numberAnimated__enterDone,
                },
                C = { enterActive: Ro.numberGlow__active, enterDone: Ro.numberGlow__exit },
                v = (0, n.useCallback)(() => {
                  (0, ee.G)("bp_current_phase");
                }, []);
              return (
                (0, n.useEffect)(() => {
                  if (u && g)
                    return Ta(() => {
                      (E(!0), _());
                    }, r);
                }, [u, g, r, _]),
                s().createElement(
                  "div",
                  { className: f()(Ro.base, Ro[`base__${e}`]) },
                  ((a && p) || (g && !A)) &&
                    s().createElement(
                      s().Fragment,
                      null,
                      s().createElement("div", {
                        className: f()(Ro.glow, g && Ro.glow__inProgress),
                      }),
                      s().createElement(
                        xo.Z,
                        { in: m, timeout: r + 4e3, className: Ro.numberGlow, classNames: C },
                        s().createElement("div", null),
                      ),
                    ),
                  a &&
                    s().createElement("div", {
                      className: f()(Ro.iconFinal, g && Ro.iconFinal__inProgress),
                    }),
                  g
                    ? s().createElement(
                        "div",
                        { className: b },
                        t,
                        s().createElement(
                          xo.Z,
                          {
                            in: m,
                            timeout: r + 4e3,
                            className: f()(Ro.numberInProgress, Ro.numberAnimated),
                            classNames: h,
                            onEnter: v,
                          },
                          s().createElement("div", null, t),
                        ),
                      )
                    : s().createElement("div", { className: b }, t),
                  g &&
                    s().createElement(
                      "div",
                      { className: Ro.title },
                      A ? No.pausedStep() : No.currentStep(),
                    ),
                )
              );
            },
          ),
          To = {
            base: "ClosedStatus_base_8a",
            icon: "ClosedStatus_icon_18",
            icon__current: "ClosedStatus_icon__current_44",
            icon__exit: "ClosedStatus_icon__exit_fd",
            icon__exitActive: "ClosedStatus_icon__exitActive_65",
            icon__exitCurrentActive: "ClosedStatus_icon__exitCurrentActive_4d",
            fadeDown: "ClosedStatus_fadeDown_d3",
            zoomOut: "ClosedStatus_zoomOut_0f",
            icon__exitDone: "ClosedStatus_icon__exitDone_b2",
            title: "ClosedStatus_title_a3",
            title__premium: "ClosedStatus_title__premium_e2",
            title__exit: "ClosedStatus_title__exit_16",
            title__exitActive: "ClosedStatus_title__exitActive_44",
            title__exitDone: "ClosedStatus_title__exitDone_51",
          };
        function Mo() {
          return (
            (Mo =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            Mo.apply(this, arguments)
          );
        }
        const Io = ({
            isPremium: e = !1,
            isLockedState: t = !1,
            isInProgress: a = !1,
            isPremiumActivated: u = !1,
            playUnlockAnimation: r = !1,
            handleUnlockAnimationExited: n,
            baseUnlockProps: o,
          }) => {
            const i = a && e && (!u || r),
              l = {
                exit: To.icon__exit,
                exitActive: a ? To.icon__exitCurrentActive : To.icon__exitActive,
                exitDone: To.icon__exitDone,
              },
              c = t || r,
              _ =
                c && e
                  ? {
                      exit: To.title__exit,
                      exitActive: To.title__exitActive,
                      exitDone: To.title__exitDone,
                    }
                  : {};
            return s().createElement(
              "div",
              { className: To.base },
              c &&
                s().createElement(
                  xo.Z,
                  Mo({}, o, { classNames: l, onExited: n }),
                  s().createElement("div", {
                    className: f()(To.icon, a ? To.icon__current : To.icon__locked),
                  }),
                ),
              i &&
                s().createElement(
                  xo.Z,
                  Mo({}, o, { classNames: _ }),
                  s().createElement(
                    "div",
                    { className: f()(To.title, e && To.title__premium) },
                    Vo.progression.currentStepLocked(),
                  ),
                ),
            );
          },
          Oo = {
            base__showAnimation: "CompletedStatus_base__showAnimation_3f",
            slideUp: "CompletedStatus_slideUp_d2",
            iconGlow__completedEnter: "CompletedStatus_iconGlow__completedEnter_03",
            iconGlow__completedEnterActive: "CompletedStatus_iconGlow__completedEnterActive_19",
            showUp: "CompletedStatus_showUp_a2",
            iconGlow__completedEnterDone: "CompletedStatus_iconGlow__completedEnterDone_d8",
            icon: "CompletedStatus_icon_b1",
            icon__potentiallyCompleted: "CompletedStatus_icon__potentiallyCompleted_a4",
            icon__currentPotentiallyCompleted:
              "CompletedStatus_icon__currentPotentiallyCompleted_60",
          },
          Ho = ({
            hasTrophySelectionToken: e,
            isPotentiallyCompleted: t,
            isCurrentPotentiallyCompleted: a,
            completedIn: u,
            handleCompleteGlowAnimationExited: r,
            children: n,
            isRewardAnimationEnd: o,
          }) => {
            const i = {
                exit: Oo.iconGlow__completedEnter,
                exitActive: Oo.iconGlow__completedEnterActive,
                exitDone: Oo.iconGlow__completedEnterDone,
              },
              l = f()(
                Oo.icon,
                t && Oo.icon__potentiallyCompleted,
                a && Oo.icon__currentPotentiallyCompleted,
              );
            return s().createElement(
              "div",
              { className: f()(Oo.base, o && Oo.base__showAnimation) },
              s().createElement(xo.Z, { in: !u, timeout: zo, classNames: i, onExited: r }, n),
              e
                ? s().createElement(
                    "div",
                    { className: Oo.trophyTokenLabel },
                    Vo.progression.trophySelectAwaiting(),
                  )
                : s().createElement(
                    ge.i,
                    { body: Vo.tooltips.completed.got() },
                    s().createElement("div", { className: l }),
                  ),
            );
          },
          Wo = {
            base: "CurrentPoints_base_98",
            value__current: "CurrentPoints_value__current_73",
            value__total: "CurrentPoints_value__total_b4",
            divider: "CurrentPoints_divider_dc",
            icon: "CurrentPoints_icon_08",
          },
          Go = ({ totalPoints: e, currentPoints: t }) => {
            const a = f()(Wo.value, Wo.value__current),
              u = f()(Wo.value, Wo.value__total);
            return s().createElement(
              Kt.u,
              {
                ignoreShowDelay: !0,
                contentId: R.views.lobby.battle_pass.tooltips.BattlePassPointsView("resId"),
              },
              s().createElement(
                "div",
                { className: Wo.base },
                s().createElement("div", { className: a }, t),
                s().createElement("div", { className: Wo.divider }, "/"),
                s().createElement("div", { className: u }, e),
                s().createElement("div", { className: Wo.icon }),
              ),
            );
          },
          $o = {
            base: "Status_base_1f",
            base__default: "Status_base__default_a1",
            base__inProgress: "Status_base__inProgress_b8",
            base__premiumInProgress: "Status_base__premiumInProgress_5e",
            iconContainer: "Status_iconContainer_2f",
            iconInner: "Status_iconInner_30",
            iconGlow: "Status_iconGlow_c5",
            iconGlow__completed: "Status_iconGlow__completed_b9",
            iconGlow__completedRare: "Status_iconGlow__completedRare_be",
            iconGlow__hidden: "Status_iconGlow__hidden_24",
            icon: "Status_icon_8b",
            icon__completedEnter: "Status_icon__completedEnter_e2",
            icon__completedEnterActive: "Status_icon__completedEnterActive_d1",
            fadeUp: "Status_fadeUp_a4",
            icon__completedEnterDone: "Status_icon__completedEnterDone_9e",
            glowWrapper: "Status_glowWrapper_67",
            glow: "Status_glow_89",
            glow__active: "Status_glow__active_7f",
            highlightScale: "Status_highlightScale_62",
            dust: "Status_dust_b2",
            dust__active: "Status_dust__active_14",
            trophyTokenLabel: "Status_trophyTokenLabel_b9",
            pointsWrapper: "Status_pointsWrapper_e8",
          };
        function Uo() {
          return (
            (Uo =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            Uo.apply(this, arguments)
          );
        }
        const zo = 1500,
          Vo = R.strings.battle_pass,
          jo = R.views.lobby.battle_pass,
          Xo = ({
            status: e,
            potentialStatus: t,
            isPremium: a,
            isRare: u,
            isPremiumActivated: r,
            totalPoints: o,
            currentPoints: i,
            playCompleteAnimation: l,
            playUnlockAnimation: c,
            completeAnimationDelay: _ = 0,
            unlockAnimationDelay: d = 0,
            baseTimeout: m = 0,
            playUnlockAnimationSound: E = !0,
            playCompleteAnimationSound: g = !0,
            onAnimationDone: p,
            onCompleteAnimationStart: A,
            initialAnimationDelay: b,
            hasTrophySelectionToken: h,
            isTaken: C,
            completedDuration: v,
            playCompleteSelectRewardAnimation: D,
            isRewardAnimationEnd: B,
          }) => {
            const F = (0, n.useState)(!1),
              w = F[0],
              S = F[1],
              P = (0, n.useState)(!1),
              y = P[0],
              k = P[1],
              x = (0, n.useState)(!0),
              R = x[0],
              N = x[1],
              L = (0, n.useState)(!1),
              T = L[0],
              M = L[1],
              I = { "--animation-duration": `${v}ms` },
              O = e === cs.IN_PROGRESS,
              H = e === cs.COMPLETED,
              W = t === cs.IN_PROGRESS,
              G = !H && t === cs.COMPLETED,
              $ = (0, n.useCallback)(() => {
                (N(!1), E && !T && (O ? (0, ee.G)(_s.UNLOCK_BIG) : (0, ee.G)(_s.UNLOCK_SMALL)));
              }, [T, O, E]),
              U = (0, n.useCallback)(() => {
                (g && (0, ee.G)(_s.IMPROVED_REWARD), S(!0), A && A());
              }, [A, g]);
            (0, n.useEffect)(
              () =>
                c
                  ? Ta(() => {
                      $();
                    }, b + d)
                  : l
                    ? (k(!0),
                      Ta(() => {
                        (k(!1), U());
                      }, b + _))
                    : void (y && k(!1)),
              [c, l, U, b, _, $, d, y],
            );
            const z =
                O && a
                  ? f()($o.base, $o.base__premiumInProgress)
                  : f()($o.base, $o.base__default, O && $o.base__inProgress),
              V = {
                exit: $o.icon__completedEnter,
                exitActive: $o.icon__completedEnterActive,
                exitDone: $o.icon__completedEnterDone,
              },
              j = { exit: $o.glow, exitActive: $o.glow__active, exitDone: $o.glow },
              X = { exit: $o.dust, exitActive: $o.dust__active, exitDone: $o.dust },
              Y = H && (!a || (a && r)) && !C,
              q = a && !r,
              K = !a && !Y && G,
              Q = !a && O && G,
              Z = f()(
                $o.iconGlow,
                Y && (u ? $o.iconGlow__completedRare : $o.iconGlow__completed),
                y && $o.iconGlow__hidden,
              ),
              J = (0, n.useCallback)(() => {
                p && p();
              }, [p]),
              te = (0, n.useCallback)(() => {
                (!l && p && p(), M(!0));
              }, [p, l]),
              ae = (0, n.useCallback)(() => {
                y && k(!1);
              }, [y]);
            (0, n.useEffect)(() => {
              if (l && T)
                return Ta(() => {
                  U();
                }, _);
            }, [l, T, U, _]);
            const ue = { in: R, timeout: zo + m },
              re = w ? f()($o.icon, Y && $o.icon__completed) : void 0,
              ne = a || Y || G,
              se = !a && ((O && !G) || W);
            return s().createElement(
              "div",
              { className: z, style: I },
              ne &&
                s().createElement(
                  "div",
                  { className: $o.iconContainer },
                  !l &&
                    !c &&
                    (Y
                      ? s().createElement(
                          Ho,
                          {
                            hasTrophySelectionToken: h,
                            isPotentiallyCompleted: K,
                            isCurrentPotentiallyCompleted: Q,
                            completedIn: w,
                            handleCompleteGlowAnimationExited: ae,
                            isRewardAnimationEnd: B,
                          },
                          s().createElement("div", { className: Z }),
                        )
                      : s().createElement(
                          Kt.u,
                          {
                            isEnabled: a,
                            contentId: jo.tooltips.BattlePassLockIconTooltipView("resId"),
                          },
                          s().createElement(
                            "div",
                            null,
                            s().createElement(Io, {
                              isPremium: a,
                              isLockedState: q,
                              isInProgress: O,
                              isPremiumActivated: r,
                              playUnlockAnimation: c,
                              baseUnlockProps: ue,
                              handleUnlockAnimationExited: te,
                            }),
                          ),
                        )),
                  (l || D) &&
                    s().createElement(
                      xo.Z,
                      { in: !w, timeout: zo, classNames: V, onExited: J },
                      h && w
                        ? s().createElement(
                            "div",
                            { className: $o.trophyTokenLabel },
                            Vo.progression.trophySelectAwaiting(),
                          )
                        : s().createElement("div", { className: re }),
                    ),
                  c &&
                    !T &&
                    s().createElement(
                      Kt.u,
                      { contentId: jo.tooltips.BattlePassLockIconTooltipView("resId") },
                      s().createElement(
                        "div",
                        { className: $o.iconInner },
                        s().createElement(Io, {
                          baseUnlockProps: ue,
                          isPremium: a,
                          isLockedState: q,
                          isInProgress: O,
                          isPremiumActivated: r,
                          playUnlockAnimation: c,
                          handleUnlockAnimationExited: te,
                        }),
                        O &&
                          s().createElement(
                            "div",
                            null,
                            s().createElement(
                              xo.Z,
                              Uo({}, ue, { classNames: j }),
                              s().createElement(
                                "div",
                                { className: $o.glowWrapper },
                                s().createElement("div", { className: $o.glow }),
                              ),
                            ),
                            s().createElement(
                              xo.Z,
                              Uo({}, ue, { classNames: X }),
                              s().createElement(
                                "div",
                                { className: $o.glowWrapper },
                                s().createElement("div", { className: $o.dust }),
                              ),
                            ),
                          ),
                      ),
                    ),
                ),
              se &&
                s().createElement(
                  "div",
                  { className: $o.pointsWrapper },
                  s().createElement(Go, { totalPoints: o, currentPoints: i }),
                ),
            );
          },
          Yo = {
            base: "CardContent_base_aa",
            content: "CardContent_content_ed",
            content__notStarted: "CardContent_content__notStarted_30",
            content__premiumWithoutBP: "CardContent_content__premiumWithoutBP_2f",
            content__enter: "CardContent_content__enter_10",
            content__enterActive: "CardContent_content__enterActive_80",
            content__enterDone: "CardContent_content__enterDone_1b",
            status: "CardContent_status_6f",
            buttonHolder: "CardContent_buttonHolder_a0",
            buttonLight: "CardContent_buttonLight_95",
            buttonInner: "CardContent_buttonInner_27",
            buttonInner__disabled: "CardContent_buttonInner__disabled_b1",
            button: "CardContent_button_3a",
            button__disabled: "CardContent_button__disabled_a8",
            buttonBlink: "CardContent_buttonBlink_db",
            move: "CardContent_move_18",
            buttonText: "CardContent_buttonText_fc",
          },
          qo = {
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
          Ko = ({
            name: e,
            image: t,
            isPeriodic: a = !1,
            size: u = rn.Big,
            special: r,
            value: n,
            valueType: o,
            style: i,
            className: l,
            classNames: c,
            tooltipArgs: _,
            periodicIconTooltipArgs: d,
          }) => {
            const m = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case sn.BATTLE_BOOSTER:
                  case sn.BATTLE_BOOSTER_REPLACE:
                    return on.BATTLE_BOOSTER;
                }
              })(r),
              E = ((e) => {
                if (void 0 === e) return null;
                switch (e) {
                  case sn.BATTLE_BOOSTER:
                    return ln.BATTLE_BOOSTER;
                  case sn.BATTLE_BOOSTER_REPLACE:
                    return ln.BATTLE_BOOSTER_REPLACE;
                  case sn.BUILT_IN_EQUIPMENT:
                    return ln.BUILT_IN_EQUIPMENT;
                  case sn.EQUIPMENT_PLUS:
                    return ln.EQUIPMENT_PLUS;
                  case sn.EQUIPMENT_TROPHY_BASIC:
                    return ln.EQUIPMENT_TROPHY_BASIC;
                  case sn.EQUIPMENT_TROPHY_UPGRADED:
                    return ln.EQUIPMENT_TROPHY_UPGRADED;
                  case sn.EQUIPMENT_MODERNIZED_UPGRADED_1:
                    return ln.EQUIPMENT_MODERNIZED_UPGRADED_1;
                  case sn.EQUIPMENT_MODERNIZED_UPGRADED_2:
                    return ln.EQUIPMENT_MODERNIZED_UPGRADED_2;
                  case sn.EQUIPMENT_MODERNIZED_UPGRADED_3:
                    return ln.EQUIPMENT_MODERNIZED_UPGRADED_3;
                  case sn.PROGRESSION_STYLE_UPGRADED_1:
                    return ln.PROGRESSION_STYLE_UPGRADED_1;
                  case sn.PROGRESSION_STYLE_UPGRADED_2:
                    return ln.PROGRESSION_STYLE_UPGRADED_2;
                  case sn.PROGRESSION_STYLE_UPGRADED_3:
                    return ln.PROGRESSION_STYLE_UPGRADED_3;
                  case sn.PROGRESSION_STYLE_UPGRADED_4:
                    return ln.PROGRESSION_STYLE_UPGRADED_4;
                }
              })(r),
              g = ((e, t) => {
                if (void 0 === e) return null;
                switch (t) {
                  case nn.MULTI: {
                    const t = Number(e);
                    return isFinite(t) && t > 1 ? `x${Math.floor(t)}` : null;
                  }
                  case nn.CURRENCY:
                  case nn.NUMBER:
                    return s().createElement(dn.A, { format: "integral", value: Number(e) });
                  case nn.PREMIUM_PLUS: {
                    const t = Number(e);
                    return isNaN(t) ? e : null;
                  }
                  default:
                    return e;
                }
              })(n, o);
            return s().createElement(
              "div",
              { className: f()(qo.base, qo[`base__${u}`], l), style: i },
              s().createElement(
                nu,
                { tooltipArgs: _, className: qo.tooltipWrapper },
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement(
                    "div",
                    { className: f()(qo.image, null == c ? void 0 : c.image) },
                    m &&
                      s().createElement("div", {
                        className: f()(qo.highlight, null == c ? void 0 : c.highlight),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${u}.${m}_highlight)`,
                        },
                      }),
                    t &&
                      s().createElement("div", {
                        className: f()(qo.icon, null == c ? void 0 : c.rewardIcon),
                        style: { backgroundImage: `url(${t})` },
                      }),
                    E &&
                      s().createElement("div", {
                        className: f()(qo.overlay, null == c ? void 0 : c.overlay),
                        style: {
                          backgroundImage: `url(R.images.gui.maps.icons.quests.bonuses.${u}.${E}_overlay)`,
                        },
                      }),
                  ),
                  g &&
                    s().createElement(
                      "div",
                      {
                        className: f()(
                          qo.info,
                          qo[`info__${e}`],
                          o === nn.MULTI && qo.info__multi,
                          null == c ? void 0 : c.info,
                        ),
                      },
                      g,
                    ),
                ),
              ),
              a &&
                s().createElement(
                  nu,
                  { tooltipArgs: d },
                  s().createElement("div", {
                    className: f()(qo.timer, null == c ? void 0 : c.periodicIcon),
                  }),
                ),
            );
          },
          Qo = {
            base: "Rewards_base_46",
            base__column: "Rewards_base__column_5d",
            base__inProgress: "Rewards_base__inProgress_a5",
            reward: "Rewards_reward_1f",
            base__tripleDefault: "Rewards_base__tripleDefault_fd",
            reward__0: "Rewards_reward__0_7c",
            reward__2: "Rewards_reward__2_e3",
            base__reverse: "Rewards_base__reverse_14",
            base__tripleInProgress: "Rewards_base__tripleInProgress_85",
            reward__1: "Rewards_reward__1_11",
            shine: "Rewards_shine_3f",
            shine__animated: "Rewards_shine__animated_08",
            fade: "Rewards_fade_96",
            rewardInner__animated: "Rewards_rewardInner__animated_7a",
            changeReward: "Rewards_changeReward_ee",
            staticShine: "Rewards_staticShine_e4",
            explosion: "Rewards_explosion_f6",
            customOverlay: "Rewards_customOverlay_2b",
            customOverlay__small: "Rewards_customOverlay__small_e8",
            customOverlay__big: "Rewards_customOverlay__big_35",
          };
        function Zo() {
          return (
            (Zo =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            Zo.apply(this, arguments)
          );
        }
        const Jo = (0, n.memo)(
            ({
              data: e,
              isTaken: t,
              isVertical: a,
              isTriple: u,
              isReverse: r,
              isInProgress: n,
              hasAnimation: o,
            }) => {
              const i = P().mediaSize <= F.Small,
                l = f()(
                  Qo.base,
                  a && Qo.base__column,
                  n && Qo.base__inProgress,
                  r && Qo.base__reverse,
                  n && u && Qo.base__tripleInProgress,
                  !n && u && Qo.base__tripleDefault,
                );
              return s().createElement(
                "div",
                { className: l },
                e.map((e, a) => {
                  const u =
                      e.name.includes("styleProgressToken") ||
                      e.name.includes("battlePassSelectToken"),
                    r = (t && u) || (o && u),
                    n = f()(Qo.rewardInner, o && u && Qo.rewardInner__animated),
                    l = f()(Qo.shine, o && u && Qo.shine__animated);
                  return s().createElement(
                    "div",
                    { key: a, className: f()(Qo.reward, Qo[`reward__${a}`]) },
                    r && s().createElement("div", { className: l }),
                    s().createElement(
                      "div",
                      { className: n },
                      o &&
                        u &&
                        s().createElement(
                          s().Fragment,
                          null,
                          s().createElement("div", { className: Qo.staticShine }),
                          s().createElement("div", { className: Qo.explosion }),
                        ),
                      s().createElement(
                        Ko,
                        Zo(
                          { size: i ? rn.Small : rn.Big, image: i ? e.smallImage : e.bigImage },
                          e,
                        ),
                      ),
                      e.withUniqueVoice &&
                        s().createElement("div", {
                          className: f()(
                            Qo.customOverlay,
                            i ? Qo.customOverlay__small : Qo.customOverlay__big,
                          ),
                        }),
                    ),
                  );
                }),
              );
            },
          ),
          ei = {
            content: "CardRewards_content_0a",
            content__inProgress: "CardRewards_content__inProgress_18",
            content__enterDone: "CardRewards_content__enterDone_26",
            content__isActive: "CardRewards_content__isActive_f0",
            content__premiumWithoutBP: "CardRewards_content__premiumWithoutBP_05",
            content__isCompleted: "CardRewards_content__isCompleted_aa",
            content__enterActive: "CardRewards_content__enterActive_07",
            content__isTaken: "CardRewards_content__isTaken_e7",
          },
          ti = (0, n.memo)(
            ({
              rewards: e,
              showHighlight: t,
              completedIn: a,
              isTaken: u,
              isPremium: r,
              isInProgress: o,
              isCompleted: i,
              isNotStarted: l,
              isPremiumActivated: c,
              baseTimeout: _,
              isRewardAnimationActive: d,
              isActive: m,
            }) => {
              const E = e.map((e) => {
                  const t = e.item,
                    a = e.name,
                    u = e.value,
                    r = e.overlayType,
                    n = e.tooltipId,
                    s = e.tooltipContentId,
                    o = e.withUniqueVoice,
                    i = e.name === an.TmanToken,
                    l = (e, t) => {
                      switch (e.name) {
                        case an.TmanToken:
                          return `R.images.gui.maps.icons.tankmen.icons.${t}.${((u = e.bigIcon), u.replace("tankman_", "").replace("tankwoman_", ""))}`;
                        case an.DogTagType:
                          return `R.images.gui.maps.icons.quests.bonuses.${t}.${a}_${e.icon}`;
                        default:
                          return Cn(e, t);
                      }
                      var u;
                    };
                  return {
                    name: t || a,
                    smallImage: l(e, i ? rn.S48x48 : rn.Small),
                    bigImage: l(e, i ? rn.S80x80 : rn.Big),
                    special: r,
                    value: u,
                    valueType:
                      ((c = a),
                      mn.includes(c)
                        ? nn.MULTI
                        : En.includes(c)
                          ? nn.CURRENCY
                          : gn.includes(c)
                            ? nn.NUMBER
                            : pn.includes(c)
                              ? nn.PREMIUM_PLUS
                              : nn.STRING),
                    tooltipArgs: vn({ tooltipId: n }, Number(s), { ignoreShowDelay: !0 }),
                    withUniqueVoice: o,
                  };
                  var c;
                }),
                g = (0, n.useState)(E),
                p = g[0],
                A = g[1],
                b = (0, n.useRef)(E),
                h = b.current;
              (0, n.useEffect)(() => {
                if (h.some((e, t) => e !== E[t])) return ((b.current = E), Ta(() => A(E), 1e3));
              }, [E, h]);
              const C = (0, n.useMemo)(
                  () => ({
                    enter: ei.content__enter,
                    enterActive: ei.content__enterActive,
                    enterDone: ei.content__enterDone,
                  }),
                  [],
                ),
                v = f()(
                  ei.content,
                  t && !a && ei.content__enter,
                  l && ei.content__notStarted,
                  i && ei.content__isCompleted,
                  u && ei.content__isTaken,
                  m && ei.content__isActive,
                  o && ei.content__inProgress,
                  r && !c && ei.content__premiumWithoutBP,
                ),
                D = (0, n.useMemo)(
                  () => ({
                    data: p,
                    isVertical: 2 === p.length,
                    isTaken: u,
                    isTriple: 3 === p.length,
                    isReverse: r,
                    isInProgress: o,
                    hasAnimation: d,
                  }),
                  [p, u, r, o, d],
                );
              return t
                ? s().createElement(
                    xo.Z,
                    { in: a, timeout: _, className: v, classNames: C },
                    s().createElement("div", null, s().createElement(Jo, D)),
                  )
                : s().createElement("div", { className: v }, s().createElement(Jo, D));
            },
          );
        function ai() {
          return (
            (ai =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            ai.apply(this, arguments)
          );
        }
        const ui = 100,
          ri = 1800,
          ni = (0, te.Pi)(
            ({
              status: e,
              potentialStatus: t,
              isPremium: a,
              isRare: u,
              isPremiumActivated: r,
              rewards: o,
              stepNumber: i,
              totalPoints: l,
              currentPoints: c,
              currentLevel: _,
              previousLevel: d,
              isFinal: m,
              showBuyAnimations: E,
              showLevelsAnimations: g,
              onFinalAnimationDone: p,
              maxVisibleCards: A,
              isTaken: b,
              isButtonVisible: h,
              isButtonDisabled: C,
              chapterState: v,
            }) => {
              (0, n.useContext)(Si);
              const D = Se().controls,
                B = D.onTake,
                w = D.onFinishedAnimation,
                S = e === cs.IN_PROGRESS,
                y = e === cs.COMPLETED,
                k = e === cs.COMPLETED_TROPHY_NOT_SELECTED,
                x = e === cs.NOT_STARTED,
                N = v === lt.Active,
                L = (0, n.useState)(!1),
                T = L[0],
                M = L[1],
                I = (0, n.useState)(!1),
                O = I[0],
                H = I[1],
                W = (0, n.useState)(!1),
                G = W[0],
                $ = W[1],
                U = (0, n.useState)(!1),
                z = U[0],
                V = U[1],
                j = (0, n.useCallback)(() => M(!0), []),
                X = P().mediaSize <= F.Small ? Za.extraSmall : Za.small,
                Y = (0, n.useRef)(b),
                q = (0, n.useRef)([]),
                K = Y.current;
              ((0, n.useEffect)(() => {
                Y.current = b;
              }),
                (0, n.useEffect)(() => {
                  if (K && !b) {
                    const e = window.setTimeout(() => {
                        (H(!1), $(!0), w());
                      }, ri),
                      t = window.setTimeout(() => {
                        V(!1);
                      }, 2300);
                    (H(!0), V(!0), q.current.push(e, t));
                  }
                }, [b, w, K, o]),
                (0, n.useEffect)(
                  () => () => {
                    q.current.forEach(clearTimeout);
                  },
                  [],
                ));
              const Q = (0, n.useMemo)(() => {
                  let e,
                    t = 0,
                    u = 0,
                    n = 0,
                    s = 0,
                    o = !1,
                    l = !1,
                    c = !1,
                    m = !1,
                    b = 500 * Math.ceil(_ / 25);
                  if (A && E && r) {
                    const e = Math.floor(0.5 * A);
                    let a = _ - e,
                      r = _ + e,
                      n = 0;
                    a <= 0 && ((n = 1 - a), (r += n), (a = 1));
                    const d = i < _ && i >= a,
                      E = i > _ && i <= r,
                      g = i === a;
                    (d ? (t = (i - a + 1) * ui) : E && (t = (i - a) * ui),
                      (o = Boolean(S || d || E || g)),
                      (l = Boolean(S || g)),
                      (c = Boolean(y && o)),
                      (m = Boolean(k && o)),
                      (u = (A - n - 1) * ui),
                      S && (s = (i - a + 1) * ui * 2.5));
                  }
                  if (A && g) {
                    const t = Math.min(_ - d, Math.floor(0.5 * A));
                    let r = _ - t;
                    r <= 0 && (r = 1);
                    const s = i < _ && i >= r;
                    (s && ((u = (i - r + 1) * ui), a && (u += ui)),
                      (c = Boolean(y && s)),
                      (n = t * ui + ui * Math.trunc(t / 2) + b),
                      g ? (e = p) : i === _ - 1 && (e = j));
                  }
                  return (
                    z && ((b = 0), (u = ri), (c = Boolean(y)), (m = Boolean(k))),
                    S ? (e = j) : i === _ - 1 && (e = p),
                    {
                      baseTimeout: s,
                      playCompleteAnimation: c,
                      playCompleteSelectRewardAnimation: m,
                      playCompleteAnimationSound: c,
                      playUnlockAnimation: o,
                      playUnlockAnimationSound: l,
                      unlockAnimationDelay: t,
                      onAnimationDone: e,
                      onCompleteAnimationStart: j,
                      completeAnimationDelay: u,
                      stageAnimationDelay: n,
                      initialAnimationDelay: b,
                    }
                  );
                }, [_, y, S, a, r, A, j, p, d, E, g, i, z, k]),
                Z = (0, n.useCallback)(() => {
                  B({ level: i });
                }, [B, i]),
                J = f()(Yo.base, S && !a ? Yo.base__inProgress : Yo.base__default),
                ee = f()(Yo.buttonInner, C && Yo.buttonInner__disabled),
                te = f()(Yo.button, C && Yo.button__disabled),
                ae = (y || S) && (Q.playUnlockAnimation || Q.playCompleteAnimation),
                ue = e === cs.COMPLETED_TROPHY_NOT_SELECTED;
              return s().createElement(
                "div",
                { className: J },
                !a &&
                  s().createElement(
                    Lo,
                    ai({ status: e, stepNumber: i, isFinal: m, showLevelsAnimations: g }, Q),
                  ),
                h &&
                  !a &&
                  s().createElement(
                    ge.i,
                    {
                      isEnabled: C,
                      body: R.strings.battle_pass.progression.btnRewardsUnavailable(),
                    },
                    s().createElement(
                      "div",
                      { className: Yo.buttonHolder },
                      !C && s().createElement("div", { className: Yo.buttonLight }),
                      s().createElement(
                        "div",
                        { className: ee },
                        s().createElement(
                          eu,
                          { type: Qa.ghost, size: X, disabled: C, onClick: Z, mixClass: te },
                          !C && s().createElement("div", { className: Yo.buttonBlink }),
                          s().createElement(
                            "div",
                            { className: Yo.buttonText },
                            R.strings.battle_pass.progression.takeReward(),
                          ),
                        ),
                      ),
                    ),
                  ),
                s().createElement(ti, {
                  showHighlight: ae,
                  rewards: o,
                  completedIn: T,
                  isTaken: b,
                  isPremium: a,
                  isInProgress: S,
                  baseTimeout: Q.baseTimeout,
                  isNotStarted: x,
                  isCompleted: y,
                  isActive: N,
                  isPremiumActivated: r,
                  isRewardAnimationActive: O,
                }),
                s().createElement(
                  "div",
                  { className: Yo.status },
                  s().createElement(
                    Xo,
                    ai(
                      {
                        status: e,
                        potentialStatus: t,
                        isPremium: Boolean(a),
                        isRare: u,
                        isPremiumActivated: r,
                        totalPoints: l,
                        currentPoints: c,
                        isTaken: b,
                        hasTrophySelectionToken: ue,
                        completedDuration: 500,
                        isRewardAnimationEnd: G,
                      },
                      Q,
                    ),
                  ),
                ),
              );
            },
          ),
          si = {
            base: "Divider_base_8f",
            base__left: "Divider_base__left_bd",
            base__right: "Divider_base__right_1e",
            base__fullBasic: "Divider_base__fullBasic_b1",
            base__fullPremium: "Divider_base__fullPremium_0a",
            inner: "Divider_inner_40",
            inner__basic: "Divider_inner__basic_17",
            inner__premium: "Divider_inner__premium_28",
          },
          oi = ({ position: e, isFull: t = !0, isPremium: a = !1 }) => {
            const u = f()(
                si.base,
                si[`base__${e}`],
                t && (a ? si.base__fullPremium : si.base__fullBasic),
              ),
              r = f()(si.inner, a ? si.inner__premium : si.inner__basic);
            return s().createElement(
              "div",
              { className: u },
              s().createElement("div", { className: r }),
            );
          },
          ii = {
            base: "Card_base_5f",
            base__inProgress: "Card_base__inProgress_ad",
            base__inProgressNonPremium: "Card_base__inProgressNonPremium_0c",
            totalPoints: "Card_totalPoints_51",
            totalPoints__default: "Card_totalPoints__default_db",
            totalPoints__final: "Card_totalPoints__final_ee",
            progressShadow: "Card_progressShadow_ca",
          },
          li = (0, n.memo)(
            (0, n.forwardRef)(
              (
                {
                  status: e,
                  potentialStatus: t,
                  isPremium: a,
                  isPremiumActivated: u,
                  isRare: r,
                  rewards: o,
                  stepNumber: i,
                  totalPoints: l,
                  totalPointsFinal: c,
                  currentPoints: _,
                  currentLevel: d,
                  previousLevel: m,
                  isFinal: E,
                  maxVisibleCards: g,
                  showBuyAnimations: p,
                  showLevelsAnimations: A,
                  onAnimationDone: b,
                  isTaken: h,
                  isButtonVisible: C,
                  isButtonDisabled: v,
                  isShadowVisible: D,
                },
                B,
              ) => {
                const F = J("model"),
                  w = F.currentPointsInLevel,
                  S = F.chapterState,
                  P = (0, n.useRef)(null);
                (0, n.useImperativeHandle)(B, () => ({
                  width: () => {
                    const e = P.current;
                    return e ? e.offsetWidth : void 0;
                  },
                  offsetLeft: () => {
                    const e = P.current;
                    return e ? e.offsetLeft : void 0;
                  },
                }));
                const y = e === cs.NOT_STARTED,
                  k = e === cs.IN_PROGRESS,
                  x = e === cs.COMPLETED,
                  R = e === cs.COMPLETED_TROPHY_NOT_SELECTED,
                  N = x || k || R || (y && 1 === i),
                  L = y || k || R || (x && E),
                  T = f()(ii.base, ii[`base__${e}`], !a && ii[`base__${e}NonPremium`]),
                  M = f()(ii.totalPoints, ii.totalPoints__default),
                  I = f()(ii.totalPoints, ii.totalPoints__final),
                  O = ((e, t, a, u) =>
                    e === cs.COMPLETED
                      ? 100
                      : e !== cs.IN_PROGRESS || (t !== lt.NotStarted && t !== lt.Paused)
                        ? 0
                        : (100 * a) / u)(e, S, w, l),
                  H = { width: `${O}%` },
                  W = {
                    "--small-card-width": "140rem",
                    "--small-current-card-width": "224rem",
                    "--big-card-width": "220rem",
                    "--big-current-card-width": "340rem",
                  };
                return s().createElement(
                  "div",
                  { className: T, ref: P, style: W },
                  s().createElement(ko, {
                    status: e,
                    chapterState: S,
                    isPremium: a,
                    isPremiumActivated: u,
                    isRare: r,
                  }),
                  s().createElement(ni, {
                    status: e,
                    potentialStatus: t,
                    isPremium: a,
                    isRare: r,
                    isPremiumActivated: u,
                    rewards: o,
                    stepNumber: i,
                    totalPoints: l,
                    currentPoints: _,
                    currentLevel: d,
                    previousLevel: m,
                    isFinal: E,
                    maxVisibleCards: g,
                    showBuyAnimations: p,
                    showLevelsAnimations: A,
                    onFinalAnimationDone: b,
                    isTaken: h,
                    isButtonVisible: C,
                    isButtonDisabled: v,
                    chapterState: S,
                  }),
                  a && s().createElement("div", { className: M }, l),
                  a && E && s().createElement("div", { className: I }, c),
                  D && s().createElement("div", { className: ii.progressShadow, style: H }),
                  N && s().createElement(oi, { position: ls.left, isFull: !0, isPremium: a }),
                  L && s().createElement(oi, { position: ls.right, isFull: !0, isPremium: a }),
                );
              },
            ),
          );
        function ci() {
          return (
            (ci =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            ci.apply(this, arguments)
          );
        }
        const _i = (e, t, a, u, r, n, s) =>
            r === n && u === t
              ? cs.COMPLETED
              : e === r && ((s !== lt.NotStarted && s !== lt.Disabled) || u > 0)
                ? cs.IN_PROGRESS
                : e < r
                  ? 3 !== a || (s !== lt.Active && s !== lt.Completed)
                    ? cs.COMPLETED
                    : cs.COMPLETED_TROPHY_NOT_SELECTED
                  : cs.NOT_STARTED,
          di = (0, te.Pi)(
            ({
              currentCardRef: e,
              freeProgressionCutCardRef: t,
              potentialLevelCardRef: a,
              levels: u,
              isPremium: r,
              sectionKey: o,
              maxVisibleCards: i,
              isMarathon: l = !1,
            }) => {
              const c = Se().model,
                _ = c.root.get(),
                d = _.chapterID,
                m = _.chapterState,
                E = _.currentPointsInLevel,
                g = _.currentPointsInChapter,
                p = _.freePointsInChapter,
                A = _.freePointsInLevel,
                b = _.currentLevel,
                h = _.previousLevel,
                C = _.potentialLevel,
                v = _.isBattlePassPurchased,
                D = _.showBuyAnimations,
                B = _.showLevelsAnimations,
                F = (0, n.useState)(!1),
                w = F[0],
                S = F[1],
                P = (0, n.useCallback)(() => {
                  S(!0);
                }, [S]),
                y = Boolean(i && r && D),
                k = Boolean(i && B);
              let x = 0;
              const R = u.items,
                N = R.length,
                L = m === lt.NotStarted || m === lt.Paused,
                T = R.map(({ value: u }, n) => {
                  const _ = u.level,
                    f = u.levelPoints,
                    D = u.state,
                    B = u.isButtonDisabled;
                  x += f;
                  const F = r ? c.computes.getPaidRewardItems(n) : c.computes.getFreeRewardItems(n),
                    S = _ === N,
                    R = _i(_, x, D, g, b, N, m),
                    T = L ? _i(_, x, D, p, C, N, m) : cs.NOT_STARTED,
                    M = ((u, r, n) => (u === r ? e : u === n ? a : t))(_, b, C),
                    I = F || [],
                    O = !r && (R === cs.COMPLETED || R === cs.IN_PROGRESS);
                  return s().createElement(
                    li,
                    ci(
                      {
                        key: `${d}_${o}_${n}`,
                        showBuyAnimations: y && !w,
                        showLevelsAnimations: k,
                      },
                      u,
                      {
                        ref: M,
                        rewards: I,
                        currentPoints: L && !l ? A : E,
                        currentLevel: b,
                        previousLevel: h,
                        stepNumber: _,
                        status: R,
                        potentialStatus: T,
                        totalPoints: r ? x - f : f,
                        totalPointsFinal: x,
                        isPremium: r,
                        isPremiumActivated: v,
                        isFinal: S,
                        isShadowVisible: O,
                        maxVisibleCards: i,
                        onAnimationDone: P,
                        isTaken: r ? u.needTakePaid : u.needTakeFree,
                        isButtonDisabled: B,
                      },
                    ),
                  );
                });
              return s().createElement("div", { className: f()(ir.row, !r && ir.row__basic) }, T);
            },
          );
        function mi() {
          return (
            (mi =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            mi.apply(this, arguments)
          );
        }
        const Ei = (0, te.Pi)(
          ({
            currentCardRef: e,
            freeProgressionCutCardRef: t,
            potentialLevelCardRef: a,
            onProgressChanged: u,
            overScrollWidth: r,
            widget3dStyleLeftRef: o,
            shadowLipRef: l,
            api: c,
          }) => {
            const _ = (0, n.useContext)(wi).levels,
              d = Se().model.root.get(),
              m = d.showLevelsAnimations,
              E = d.finalReward,
              g = d.isStyleProgressive,
              p = d.currentLevel,
              A = d.currentPointsInLevel,
              b = d.chapterType,
              h = (0, n.useRef)({ update: () => {} }),
              C = (0, n.useRef)({ update: () => {} }),
              v = b === Ct.Marathon;
            c.current.moveProgressBars = (0, n.useCallback)((e) => {
              (h.current.update(e), C.current.update(e));
            }, []);
            const D = (0, n.useState)({ levelWidth: 0, currentLevelWidth: 0, maxCardsShown: 0 }),
              B = D[0],
              F = D[1],
              w = (0, n.useCallback)(() => {
                if (e.current) {
                  const a = e.current,
                    u = t.current,
                    r = a ? a.width() : 0,
                    n = u ? u.width() : 0;
                  return !n && r
                    ? { currentLevelWidth: r, levelWidth: 224 === r ? 140 : 220 }
                    : { currentLevelWidth: r, levelWidth: n };
                }
              }, [e, t]),
              S = P().mediaSize;
            ((0, n.useEffect)(() => {
              (0, $.Eu)().then(() => {
                const e = w();
                if (e) {
                  const t = i.O.client.getSize(),
                    a = Math.floor((t.width - e.currentLevelWidth) / e.levelWidth) + 1;
                  F({
                    levelWidth: e.levelWidth,
                    currentLevelWidth: e.currentLevelWidth,
                    maxCardsShown: a,
                  });
                }
              });
            }, [S, w, _.items.length, p, A]),
              (0, n.useEffect)(() => {
                m && (0, ee.G)(R.sounds.bp_progress_bar_start());
              }, [m]),
              (0, n.useEffect)(() => {
                u && u();
              }, [p, A, u]));
            const y = _.items.map((e) => {
                const t = e.value.isFreeRewardChoiceEnabled || e.value.isPaidRewardChoiceEnabled,
                  a = e.value.needTakeFree || e.value.needTakePaid,
                  u = a && !t;
                return {
                  id: e.id,
                  value: Object.assign({}, e.value, { isButtonDisabled: u, isButtonVisible: a }),
                };
              }),
              k = !v && Fn(E) === ht.style && g;
            return s().createElement(
              "div",
              { className: ir.wrapper },
              k &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement(ks, {
                    widget3dStyleRef: o,
                    overScrollWidth: r,
                    level: 1,
                    isShowTitle: !0,
                  }),
                  s().createElement(
                    "div",
                    { className: f()(ir.decor, ir.decor__left) },
                    s().createElement("div", { className: ir.decorBackground }),
                  ),
                  s().createElement(
                    "div",
                    { className: ir.bookmarkBackground, ref: l },
                    s().createElement(Qn, {
                      isDisappeared: !0,
                      mixClass: ir.bookmarkLeftResponsive,
                    }),
                  ),
                ),
              s().createElement(
                "div",
                { className: ir.section },
                s().createElement(di, {
                  sectionKey: "baseCard",
                  currentCardRef: e,
                  freeProgressionCutCardRef: t,
                  potentialLevelCardRef: a,
                  levels: Object.assign({}, _, { items: y }),
                  maxVisibleCards: m ? B.maxCardsShown : 0,
                  currentLevel: p,
                  isMarathon: v,
                }),
                s().createElement(
                  So,
                  mi({ progressApi: h, freePointsApi: C, progressChange: u }, B),
                ),
                s().createElement(di, {
                  sectionKey: "basePremiumCard",
                  isPremium: !0,
                  currentCardRef: e,
                  freeProgressionCutCardRef: t,
                  levels: _,
                  maxVisibleCards: B.maxCardsShown,
                  currentLevel: p,
                  isMarathon: v,
                }),
              ),
            );
          },
        );
        function gi() {
          return (
            (gi =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            gi.apply(this, arguments)
          );
        }
        function pi(e, t, a, u, r, n, s) {
          try {
            var o = e[n](s),
              i = o.value;
          } catch (e) {
            return void a(e);
          }
          o.done ? t(i) : Promise.resolve(i).then(u, r);
        }
        const Ai = { allowedButtons: [Pn.MainButton] },
          bi = 0,
          hi = R.strings.battle_pass.progression;
        let Ci;
        !(function (e) {
          ((e.Hidden = "hidden"),
            (e.NavToCurrentLevel = "navToCurrentLevel"),
            (e.NavToPotentialLevel = "navToPotentialLevel"));
        })(Ci || (Ci = {}));
        const vi = (0, te.Pi)(() => {
            const e = (0, n.useContext)(wi).levels,
              t = Se().model.root.get(),
              a = t.currentLevel,
              u = t.isBattlePassPurchased,
              r = t.showBuyAnimations,
              o = t.isStyleProgressive,
              i = t.chapterType,
              l = t.finalReward,
              c = i === Ct.Marathon,
              _ = (0, n.useRef)({ moveProgressBars: () => {} }),
              d = (0, n.useRef)(null),
              m = (0, n.useRef)(null),
              E = (0, n.useRef)(null),
              g = (0, n.useRef)(null),
              p = (0, n.useRef)(null),
              A = (0, n.useRef)(null),
              b = (0, n.useRef)(null),
              h = (0, n.useRef)(0),
              C = o ? 4 : 0,
              v = Fn(l) === ht.tankman,
              D = !c && Fn(l) === ht.style,
              B = (0, n.useState)(Ci.Hidden),
              F = B[0],
              w = B[1],
              S = (0, n.useState)(Ci.Hidden),
              P = S[0],
              y = S[1],
              k = (0, n.useState)(!1),
              x = k[0],
              R = k[1],
              N = o,
              L = (0, n.useState)(!1),
              T = L[0],
              M = L[1],
              I = Cr(),
              O = I.animationScroll.scrollPosition,
              H = I.applyScroll,
              G = I.events,
              U = I.handleMouseWheel,
              z = I.getContainerSize,
              V = I.getWrapperSize,
              j = (function (e, t, a) {
                const u = e.contentRef,
                  r = e.wrapperRef,
                  s = e.scrollPosition,
                  o = e.clampPosition,
                  i = e.animationScroll,
                  l = e.events,
                  c = (0, n.useState)(Sn),
                  _ = c[0],
                  d = c[1];
                return (
                  (0, n.useEffect)(() => {
                    const e = u.current;
                    e && (e.style.cursor = _.type === wn.Dragging ? "move" : "grab");
                  }, [u, _.type]),
                  (0, n.useEffect)(() => {
                    if (_.type !== wn.Dragging) return;
                    const e = (e) => {
                      const a = u.current,
                        n = r.current;
                      if (!a || !n) return;
                      const l = _.positionFrom - e.screenX,
                        c = _.previousScrollPosition + l;
                      s.start(
                        Object.assign(
                          {
                            scrollPosition: o(a, c),
                            from: { scrollPosition: i.scrollPosition.get() },
                          },
                          t && { config: t },
                        ),
                      );
                    };
                    function a() {
                      (window.removeEventListener("mousemove", e),
                        document.body.removeEventListener("mouseleave", a),
                        d({ type: "scrollingToEnd" }));
                    }
                    return (
                      window.addEventListener("mousemove", e),
                      window.addEventListener("mouseup", a),
                      document.body.addEventListener("mouseleave", a),
                      () => {
                        (window.removeEventListener("mousemove", e),
                          window.removeEventListener("mouseup", a),
                          document.body.removeEventListener("mouseleave", a));
                      }
                    );
                  }, [i.scrollPosition, o, u, _, s, r, t, a]),
                  (0, n.useEffect)(() => {
                    if (_.type !== wn.End) return;
                    const e = () => {
                      d(Sn);
                    };
                    return (i.scrollPosition.idle && e(), l.on("rest", e), () => l.off("rest", e));
                  }, [i.scrollPosition, _.type, l]),
                  (0, n.useEffect)(() => {
                    const e = u.current;
                    if (!e) return;
                    const t = (e) => {
                      (a &&
                        a.allowedButtons &&
                        -1 === a.allowedButtons.findIndex((t) => e.button === t)) ||
                        d({
                          type: wn.Dragging,
                          positionFrom: e.screenX,
                          previousScrollPosition: i.scrollPosition.get(),
                        });
                    };
                    return (
                      e.addEventListener("mousedown", t),
                      () => e.removeEventListener("mousedown", t)
                    );
                  }, [i.scrollPosition, u, a]),
                  [_, d]
                );
              })(I, void 0, Ai),
              X = j[0],
              Y = j[1],
              q = (e) => {
                (X.type === wn.Dragging && Y({ type: wn.End }), U(e));
              },
              K = (0, n.useMemo)(() => Object.assign({}, I, { handleMouseWheel: q }), []),
              Q = (0, n.useCallback)(
                (e) => {
                  const t = g.current ? g.current.offsetWidth : 0,
                    a = p.current ? p.current.offsetWidth : 0;
                  if (d.current) {
                    const u = V();
                    (_.current.moveProgressBars({
                      viewPort: d.current,
                      horizontalScrollPosition: u ? e - u : e,
                      leftOffset: t + bi + a,
                    }),
                      R(!N || e > t + bi + 0.5 * a));
                  }
                },
                [V, N],
              ),
              Z = (0, n.useCallback)(
                (e) => {
                  Q(e);
                },
                [Q],
              ),
              J = (0, n.useCallback)((e = !1) => {
                const t = m.current;
                let a = 0,
                  u = 0;
                const r = g.current ? g.current.offsetWidth : 0,
                  n = p.current ? p.current.offsetWidth : 0;
                t && ((a = t.width()), (u = t.offsetLeft() + r + n));
                const s = d.current;
                let o = 0;
                if (a && s) {
                  const t = 0.5 * s.offsetWidth;
                  e && h.current
                    ? (o = u + a - 0.5 * h.current - t)
                    : ((o = u + 0.5 * a - t), (h.current = a));
                }
                return ((o = Math.round(o < 0 ? 0 : o)), o);
              }, []),
              ee = (0, n.useCallback)((e) => {
                let t = 0;
                if (e && e.current && d && d.current) {
                  const a = e.current,
                    u = g.current ? g.current.offsetWidth : 0,
                    r = p.current ? p.current.offsetWidth : 0;
                  let n = 0,
                    s = 0;
                  a && ((n = a.width()), (s = a.offsetLeft() + u + r));
                  const o = d.current;
                  if (n && o) {
                    t = s + 0.5 * n - 0.5 * o.offsetWidth;
                  }
                  t = Math.round(t < 0 ? 0 : t);
                }
                return t;
              }, []),
              te = (0, n.useCallback)(() => {
                const e = d.current,
                  t = m.current,
                  a = E.current,
                  u = g.current ? g.current.offsetWidth : 0,
                  r = p.current ? p.current.offsetWidth : 0,
                  n = t.offsetLeft() + u + r,
                  s = (null == a ? void 0 : a.offsetLeft()) + u + r,
                  o =
                    O.goal < n - e.offsetWidth
                      ? Ci.NavToCurrentLevel
                      : a && O.goal < s - e.offsetWidth
                        ? Ci.NavToPotentialLevel
                        : Ci.Hidden,
                  i = (() => {
                    switch (!0) {
                      case a && O.goal > s + a.width():
                        return Ci.NavToPotentialLevel;
                      case O.goal > n + t.width():
                        return Ci.NavToCurrentLevel;
                      default:
                        return Ci.Hidden;
                    }
                  })();
                (w(o), y(i));
              }, [O.goal]),
              ae = (0, n.useCallback)(
                (e) => {
                  const t = ee(e);
                  (Z(O.goal), H(t), te());
                },
                [H, ee, Z, O.goal, te],
              ),
              ue = (0, n.useCallback)(
                (e) => {
                  switch (e) {
                    case Ci.NavToCurrentLevel:
                      return ae(m);
                    case Ci.NavToPotentialLevel:
                      return ae(E);
                  }
                },
                [ae],
              ),
              re = (e) => {
                switch (e) {
                  case Ci.NavToCurrentLevel:
                    return { type: xn.Default, tooltipBody: hi.backToCurrentStageArrow.descr() };
                  case Ci.NavToPotentialLevel:
                    return { type: xn.Gray, tooltipBody: hi.backToPotentialStageArrow.descr() };
                }
              },
              ne = (0, n.useCallback)(() => {
                const e = I.getBounds()[1];
                (Z(O.goal), te(), M(O.goal === e));
              }, [I, Z, O.goal, te]);
            ((0, n.useEffect)(
              () =>
                W(() => {
                  u && r && H(J());
                }),
              [H, J, u, r],
            ),
              (0, n.useEffect)(() => {
                const e = (function () {
                  var e,
                    t =
                      ((e = function* () {
                        const e = z(),
                          t = O.goal;
                        (yield (0, $.Eu)(),
                          yield new Promise((e) => {
                            requestAnimationFrame(() => {
                              requestAnimationFrame(() => {
                                e();
                              });
                            });
                          }));
                        const a = z(),
                          u = d.current,
                          r = I.getBounds()[1],
                          n = 0.25 * u.offsetWidth,
                          s = a && e && a !== e ? (t * a) / e : t;
                        (Q(s), H(s > r - n ? r : s));
                      }),
                      function () {
                        var t = this,
                          a = arguments;
                        return new Promise(function (u, r) {
                          var n = e.apply(t, a);
                          function s(e) {
                            pi(n, u, r, s, o, "next", e);
                          }
                          function o(e) {
                            pi(n, u, r, s, o, "throw", e);
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
              (0, n.useEffect)(() => Ta(() => ae(m), 700), [a]),
              (0, n.useEffect)(() => {
                const e = () => {
                    Z(O.goal);
                  },
                  t = () => {
                    Z(O.goal);
                  };
                return (
                  G.on("rest", e),
                  G.on("start", t),
                  () => {
                    (G.off("rest", e), G.off("start", t));
                  }
                );
              }, [X.type, G, Z, O.goal]));
            const se = f()(
                ir.scrollToButton,
                ir.scrollToButton__backward,
                P !== Ci.Hidden && ir.scrollToButton__visible,
              ),
              oe = f()(
                ir.scrollToButton,
                ir.scrollToButton__forward,
                F !== Ci.Hidden && ir.scrollToButton__visible,
              ),
              ie = f()(ir.shadow, ir.shadow__left),
              le = f()(ir.shadow, ir.shadow__right),
              ce = f()(ir.additionalShadow, ir.additionalShadow__active),
              _e = f()(ir.additionalShadow, !T && ir.additionalShadow__active);
            return s().createElement(
              s().Fragment,
              null,
              s().createElement(
                "div",
                { className: f()(ir.bookmark, ir.bookmark__start) },
                s().createElement(Qn, {
                  chapterStep: e.items.length,
                  mixClass: f()(ir.bookmarkLeftFixed, x && ir.bookmarkLeftFixed__active),
                }),
              ),
              s().createElement(
                "div",
                { className: ir.scrollWrapper, ref: d, onClick: ne, onMouseLeave: te, onWheel: ne },
                s().createElement(
                  "div",
                  { className: ie },
                  s().createElement("div", { className: ce }),
                ),
                s().createElement(
                  "div",
                  { className: le },
                  s().createElement("div", { className: _e }),
                ),
                s().createElement(
                  tn.Horizontal.Area.Default,
                  {
                    api: K,
                    barClassNames: { base: ir.scrollBarPosition },
                    onDrag: ne,
                    areaClassName: f()(ir.scroll, T && ir.scroll__hidden),
                  },
                  s().createElement(Ei, {
                    api: _,
                    currentCardRef: m,
                    freeProgressionCutCardRef: A,
                    potentialLevelCardRef: E,
                    separatorRef: b,
                    overScrollWidth: bi,
                    widget3dStyleLeftRef: g,
                    shadowLipRef: p,
                    onProgressChanged: () => {
                      ne();
                    },
                  }),
                ),
                s().createElement(
                  "div",
                  { className: se },
                  s().createElement(
                    Rn,
                    gi(
                      { onClick: () => ue(P), direction: ds.back, className: ir.arrowButton },
                      re(P),
                    ),
                  ),
                ),
                s().createElement(
                  "div",
                  { className: oe },
                  s().createElement(
                    Rn,
                    gi(
                      { onClick: () => ue(F), direction: ds.forward, className: ir.arrowButton },
                      re(F),
                    ),
                  ),
                ),
              ),
              D && s().createElement(ks, { overScrollWidth: bi, level: C }),
              v && s().createElement(is, null),
            );
          }),
          fi = (0, te.Pi)(() => {
            const e = Se().model.root.get(),
              t = e.isPaused,
              a = e.chapterType,
              u = f()(ir.base, ir[`base__${a}`]);
            return t
              ? null
              : s().createElement("div", { className: u }, s().createElement(vi, null));
          }),
          Di = (0, n.memo)(fi),
          Bi = (0, n.memo)(({ chapterID: e, buttonState: t, handleChapterChoiceClick: a }) => {
            const u = Se().model.root.get(),
              r = u.chapterState,
              n = u.chapterType,
              o = u.hasActiveChapter,
              i = u.isSingleChapter,
              l = t !== ct.Hide,
              c = n === Ct.Marathon,
              _ = (r === lt.NotStarted || r === lt.Disabled) && !o,
              d = i
                ? R.strings.battle_pass.progression.btnBack()
                : R.strings.battle_pass.progression.btnAllChapters(),
              m = f()(vt.progression, vt[`progression__${n}`]),
              E = ((e) => {
                switch (e) {
                  case F.ExtraSmall:
                  case F.Small:
                    return dt.Micro;
                  case F.Medium:
                    return dt.Small;
                  default:
                    return dt.Medium;
                }
              })(P().mediaSize);
            return s().createElement(
              "div",
              { className: f()(vt.base, vt[`base__${n}`], l && vt.base__buttonVisible) },
              s().createElement("div", { className: vt.background, style: bt(e, E) }),
              _ && s().createElement("div", { className: vt.headerGlow }),
              s().createElement(
                "div",
                { className: vt.close },
                s().createElement(it, { caption: d, side: "left", type: "back", onClick: a }),
              ),
              s().createElement("div", { className: vt.header }, s().createElement(or, null)),
              s().createElement("div", { className: m }, s().createElement(Di, null)),
              l && s().createElement("div", { className: vt.footer }, s().createElement(Bu, null)),
              c &&
                s().createElement(
                  we,
                  null,
                  s().createElement(
                    "div",
                    { className: vt.extraChapterWidget },
                    s().createElement(qa, null),
                  ),
                ),
            );
          }),
          Fi = "BattlePassProgressionsViewApp_base_40",
          wi = (0, n.createContext)({}),
          Si = s().createContext(!1),
          Pi = (0, te.Pi)(() => {
            const e = Se(),
              t = e.model,
              a = e.controls,
              u = t.root.get(),
              r = u.showOffSeason,
              o = u.showReplaceRewardsAnimations,
              l = u.buttonState,
              c = u.chapterID,
              _ = u.chapterState,
              d = u.currentPointsInLevel,
              m = a.onChapterChoice,
              E = a.onViewLoaded,
              g = J("model.levels"),
              p = (0, n.useState)(r),
              A = p[0],
              b = p[1],
              h = (0, n.useState)(!1),
              C = h[0],
              v = h[1];
            (0, n.useEffect)(() => {
              const e = () => {
                document.body.style.height = window.innerHeight - (innerHeight % 2) + "px";
              };
              return (
                window.addEventListener("resize", e),
                e(),
                () => {
                  (window.removeEventListener("resize", e), (document.body.style.height = "auto"));
                }
              );
            }, []);
            const f = (0, n.useCallback)(() => {
                m();
              }, [m]),
              D = (0, n.useCallback)(() => {
                C || (E(), v(!0));
              }, [C, E]);
            (!(function ({
              key: e = G.n.ESCAPE,
              callback: t = () => i.O.view.sendEvent.close(),
              preventPropagation: a = !0,
            } = {}) {
              z(e, t, a);
            })({ callback: f, preventPropagation: !1 }),
              (0, n.useEffect)(
                () =>
                  W(() => {
                    D();
                  }),
                [D],
              ),
              (0, n.useEffect)(() => {
                b(r);
              }, [r]),
              (0, n.useEffect)(() => {
                o && (0, ee.G)("bp_pick_up_award");
              }, [o]));
            const B = { chapterState: _, levels: g, currentPointsInLevel: d };
            return s().createElement(
              Si.Provider,
              { value: o },
              s().createElement(
                "div",
                { className: Fi },
                !A &&
                  s().createElement(
                    wi.Provider,
                    { value: B },
                    s().createElement(Bi, {
                      chapterID: c,
                      buttonState: l,
                      handleChapterChoiceClick: f,
                    }),
                  ),
                A && s().createElement(rt, null),
              ),
            );
          });
        engine.whenReady.then(() => {
          H().render(
            s().createElement(I, null, s().createElement(we, null, s().createElement(Pi, null))),
            document.getElementById("root"),
          );
        });
      },
      2269: (e, t, a) => {
        "use strict";
        let u, r;
        (a.d(t, { W: () => r, w: () => u }),
          (function (e) {
            ((e.Award = "Award"),
              (e.Coin = "Coin"),
              (e.Point = "Point"),
              (e.Collection = "Collection"));
          })(u || (u = {})),
          (function (e) {
            ((e.Small = "small"), (e.Big = "big"));
          })(r || (r = {})));
      },
      6895: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => C });
        var u = a(6483),
          r = a.n(u),
          n = a(6179),
          s = a.n(n);
        const o = {
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
          i = ["size", "value", "isEmpty", "fadeInAnimation", "hide", "maximumNumber", "className"];
        function l() {
          return (
            (l =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var u in a) Object.prototype.hasOwnProperty.call(a, u) && (e[u] = a[u]);
                }
                return e;
              }),
            l.apply(this, arguments)
          );
        }
        const c = (e) => {
          let t = e.size,
            a = e.value,
            u = e.isEmpty,
            n = e.fadeInAnimation,
            c = e.hide,
            _ = e.maximumNumber,
            d = e.className,
            m = (function (e, t) {
              if (null == e) return {};
              var a,
                u,
                r = {},
                n = Object.keys(e);
              for (u = 0; u < n.length; u++) ((a = n[u]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, i);
          const E = u ? null : a,
            g = "string" == typeof E;
          if ((E && !g && E < 0) || 0 === E) return null;
          const p = E && !g && E > _,
            A = r()(
              o.base,
              o[`base__${t}`],
              n && o.base__animated,
              c && o.base__hidden,
              !E && o.base__pattern,
              u && o.base__empty,
              d,
            );
          return s().createElement(
            "div",
            l({ className: A }, m),
            s().createElement("div", { className: o.bg }),
            s().createElement("div", { className: o.pattern }),
            s().createElement(
              "div",
              { className: r()(o.value, g && o.value__text) },
              p ? _ : E,
              p && s().createElement("span", { className: o.plus }, "+"),
            ),
          );
        };
        c.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        var _ = a(2372),
          d = a(280),
          m = (a(3649), a(6373)),
          E = a(7727);
        const g = {
          base: "Award_base_1b",
          base__disabled: "Award_base__disabled_f6",
          base__small: "Award_base__small_88",
          base__big: "Award_base__big_70",
          base__hasAppearAnimation: "Award_base__hasAppearAnimation_90",
          baseAppear: "Award_baseAppear_1e",
          border: "Award_border_20",
          border__smallAward: "Award_border__smallAward_71",
          border__smallCoin: "Award_border__smallCoin_a9",
          border__smallPoint: "Award_border__smallPoint_a1",
          border__smallCollection: "Award_border__smallCollection_f7",
          border__bigAward: "Award_border__bigAward_d1",
          border__bigCoin: "Award_border__bigCoin_0e",
          border__bigPoint: "Award_border__bigPoint_9a",
          border__bigCollection: "Award_border__bigCollection_40",
          border__disabled: "Award_border__disabled_cc",
          border__triggered: "Award_border__triggered_89",
          borderDisabled: "Award_borderDisabled_0b",
          borderDisabled__small: "Award_borderDisabled__small_d3",
          borderDisabled__big: "Award_borderDisabled__big_67",
          borderHover: "Award_borderHover_9b",
          borderHover__smallAward: "Award_borderHover__smallAward_cc",
          borderHover__smallCoin: "Award_borderHover__smallCoin_34",
          borderHover__smallPoint: "Award_borderHover__smallPoint_26",
          borderHover__smallCollection: "Award_borderHover__smallCollection_75",
          borderHover__bigAward: "Award_borderHover__bigAward_cf",
          borderHover__bigCoin: "Award_borderHover__bigCoin_2d",
          borderHover__bigPoint: "Award_borderHover__bigPoint_db",
          borderHover__bigCollection: "Award_borderHover__bigCollection_6d",
          shine: "Award_shine_64",
          shine__smallLeft: "Award_shine__smallLeft_bd",
          shine__smallRight: "Award_shine__smallRight_a4",
          shine_small_s: "Award_shine_small_s_8e",
          shine_small_m: "Award_shine_small_m_ad",
          shine__bigLeft: "Award_shine__bigLeft_54",
          shine__bigRight: "Award_shine__bigRight_41",
          shine_big_s: "Award_shine_big_s_5f",
          shine_big_m: "Award_shine_big_m_4d",
          bg: "Award_bg_cb",
          bgDisabled: "Award_bgDisabled_5c",
          bgHover: "Award_bgHover_a6",
          bg__smallAward: "Award_bg__smallAward_a0",
          bg__smallCoin: "Award_bg__smallCoin_03",
          bg__smallPoint: "Award_bg__smallPoint_0e",
          bg__smallCollection: "Award_bg__smallCollection_c2",
          bg__bigAward: "Award_bg__bigAward_48",
          bg__bigCoin: "Award_bg__bigCoin_66",
          bg__bigPoint: "Award_bg__bigPoint_83",
          bg__bigCollection: "Award_bg__bigCollection_10",
          bg__disabled: "Award_bg__disabled_94",
          bgDisabled__small: "Award_bgDisabled__small_23",
          bgDisabled__big: "Award_bgDisabled__big_2a",
          bgHover__smallAward: "Award_bgHover__smallAward_e1",
          bgHover__smallCoin: "Award_bgHover__smallCoin_3e",
          bgHover__smallPoint: "Award_bgHover__smallPoint_99",
          bgHover__smallCollection: "Award_bgHover__smallCollection_44",
          bgHover__bigAward: "Award_bgHover__bigAward_25",
          bgHover__bigCoin: "Award_bgHover__bigCoin_5e",
          bgHover__bigPoint: "Award_bgHover__bigPoint_4b",
          bgHover__bigCollection: "Award_bgHover__bigCollection_9d",
          locked: "Award_locked_9e",
          lockedHover: "Award_lockedHover_e1",
          locked__small: "Award_locked__small_3d",
          lockedHover__small: "Award_lockedHover__small_0c",
          locked__big: "Award_locked__big_71",
          lockedHover__big: "Award_lockedHover__big_00",
          arrow: "Award_arrow_5e",
          icon: "Award_icon_b6",
          icon__smallAward: "Award_icon__smallAward_c3",
          icon__smallCoin: "Award_icon__smallCoin_23",
          icon__smallPoint: "Award_icon__smallPoint_72",
          icon__smallCollection: "Award_icon__smallCollection_c1",
          icon__bigAward: "Award_icon__bigAward_3e",
          icon__bigCoin: "Award_icon__bigCoin_c0",
          icon__bigPoint: "Award_icon__bigPoint_91",
          icon__bigCollection: "Award_icon__bigCollection_de",
          count: "Award_count_e4",
          base__locked: "Award_base__locked_9b",
          completedCollectionIcon: "Award_completedCollectionIcon_c4",
          bubble: "Award_bubble_eb",
          label: "Award_label_e8",
          label__smallAward: "Award_label__smallAward_7c",
          label__bigAward: "Award_label__bigAward_fe",
          label__smallCoin: "Award_label__smallCoin_45",
          label__smallPoint: "Award_label__smallPoint_b8",
          label__smallCollection: "Award_label__smallCollection_2b",
          label__bigCoin: "Award_label__bigCoin_b9",
          label__bigPoint: "Award_label__bigPoint_33",
          label__bigCollection: "Award_label__bigCollection_2e",
          blinkShape: "Award_blinkShape_77",
          blink: "Award_blink_c9",
          blinker: "Award_blinker_c1",
        };
        var p = a(2269);
        const A = R.strings.battle_pass.awardsWidget,
          b = ({
            type: e,
            count: t,
            disabled: a = !1,
            onClick: u,
            size: o,
            isLocked: i = !1,
            hasTriger: l = !1,
            hasMarathon: b = !1,
            hasResource: h = !1,
            maxCount: C = 0,
            newItemsCount: v = 0,
          }) => {
            let f = "",
              D = "";
            const B = e === p.w.Collection && C === t,
              F = o === p.W.Small && l;
            switch (e) {
              case p.w.Award:
                ((f = 1 === t ? A.title.awardSingle() : A.title.awardMultiple()),
                  (D = a ? A.description.awardDisabled() : A.description.award()));
                break;
              case p.w.Coin:
                ((f = A.title.coin()), (D = A.description.coin()));
                break;
              case p.w.Point:
                ((f = A.title.point()),
                  (D = ((e, t, a) => {
                    switch (!0) {
                      case e && t && a:
                        return A.description.pointLockedExceptExtraAndResource();
                      case e && !t && a:
                        return A.description.pointLockedExceptResource();
                      case e && t:
                        return A.description.pointLockedExceptExtra();
                      case e && !t:
                        return A.description.pointLocked();
                      default:
                        return A.description.point();
                    }
                  })(i, b, h)));
                break;
              case p.w.Collection:
                ((f = A.title.collection()),
                  (D = B ? A.description.collectionCompleted() : A.description.collection()));
            }
            const w = r()(
                g.base,
                g[`base__${o}`],
                a && g.base__disabled,
                i && g.base__locked,
                e === p.w.Award && !a && g.base__hasAppearAnimation,
              ),
              S = r()(g.border, g[`border__${o}${e}`], F && g.border__triggered),
              P = r()(g.borderHover, g[`borderHover__${o}${e}`]),
              y = r()(g.borderDisabled, g[`borderDisabled__${o}`]),
              k = r()(g.shine, g[`shine__${o}Left`]),
              x = r()(g.shine, g[`shine__${o}Right`]),
              R = r()(g.bg, g[`bg__${o}${e}`]),
              N = r()(g.bgHover, g[`bgHover__${o}${e}`]),
              L = r()(g.bgDisabled, g[`bgDisabled__${o}`]),
              T = r()(g.locked, g[`locked__${o}`]),
              M = r()(g.lockedHover, g[`lockedHover__${o}`]),
              I = (0, n.useCallback)(() => {
                a || (E.$.playClick(), u());
              }, [a, u]),
              O = (0, n.useCallback)(() => {
                (0, E.G)("bp_highlight_02");
              }, []);
            return s().createElement(
              m.i,
              { body: D, isEnabled: Boolean(D) },
              s().createElement(
                "div",
                { className: w, onMouseEnter: O, onClick: I },
                v > 0 &&
                  s().createElement(
                    "div",
                    { className: g.bubble },
                    s().createElement(c, { size: "small" }),
                  ),
                a
                  ? s().createElement("div", { className: y })
                  : s().createElement(
                      s().Fragment,
                      null,
                      s().createElement("div", { className: S }),
                      s().createElement("div", { className: P }),
                    ),
                e === p.w.Award &&
                  !a &&
                  s().createElement(
                    s().Fragment,
                    null,
                    s().createElement("div", { className: k }),
                    s().createElement("div", { className: x }),
                  ),
                a
                  ? s().createElement("div", { className: L })
                  : s().createElement(
                      s().Fragment,
                      null,
                      s().createElement("div", { className: R }),
                      s().createElement("div", { className: N }),
                    ),
                i &&
                  s().createElement(
                    s().Fragment,
                    null,
                    s().createElement("div", { className: T }),
                    s().createElement("div", { className: M }),
                  ),
                e === p.w.Award && !a && s().createElement("div", { className: g.arrow }),
                s().createElement("div", { className: r()(g.icon, g[`icon__${o}${e}`]) }),
                s().createElement(
                  "div",
                  { className: g.count },
                  e === p.w.Collection
                    ? !B && s().createElement(d.z, { text: `${t || 0} / ${C}` })
                    : s().createElement(_.A, { format: "integral", value: t }),
                  B && s().createElement("div", { className: g.completedCollectionIcon }),
                ),
                s().createElement("div", { className: r()(g.label, g[`label__${o}${e}`]) }, f),
                e === p.w.Award &&
                  !a &&
                  s().createElement(
                    "div",
                    { className: g.blinkShape },
                    s().createElement("div", { className: g.blink }),
                  ),
              ),
            );
          },
          h = {
            base: "AwardsWidget_base_0f",
            base__small: "AwardsWidget_base__small_19",
            award: "AwardsWidget_award_c6",
            base__big: "AwardsWidget_base__big_f7",
          },
          C = ({
            size: e = p.W.Small,
            notChosenRewardCount: t,
            pointsCount: a,
            isPointsLocked: u,
            isAwardDisabled: n,
            coinCount: o,
            collectionItemCount: i,
            maxCollectionItemCount: l,
            newCollectionItemCount: c,
            isBPFirstEnter: _,
            isCollectionsEnabled: d,
            onPointsClick: m,
            onCoinClick: E,
            onTakeRewardsClick: g,
            onCollectionClick: A,
            hasMarathon: C,
            hasResource: v = !1,
            isBpPointsShopEntryPointActive: f = !1,
            isBpCoinShopEntryPointActive: D = !1,
          }) =>
            s().createElement(
              "div",
              { className: r()(h.base, h[`base__${e}`]) },
              t > 0 &&
                s().createElement(
                  "div",
                  { className: h.award },
                  s().createElement(b, {
                    type: p.w.Award,
                    size: e,
                    count: t,
                    disabled: n,
                    onClick: g,
                  }),
                ),
              D &&
                s().createElement(
                  "div",
                  { className: h.award },
                  s().createElement(b, { type: p.w.Coin, count: o, onClick: E, size: e }),
                ),
              f &&
                s().createElement(
                  "div",
                  { className: h.award },
                  s().createElement(b, {
                    type: p.w.Point,
                    count: a,
                    onClick: m,
                    size: e,
                    isLocked: u,
                    hasMarathon: C,
                    hasResource: v,
                  }),
                ),
              d &&
                s().createElement(
                  "div",
                  { className: r()(h.award, h.award__last) },
                  s().createElement(b, {
                    type: p.w.Collection,
                    count: i,
                    maxCount: l,
                    newItemsCount: c,
                    hasTriger: _,
                    onClick: A,
                    size: e,
                  }),
                ),
            );
      },
      1481: (e, t, a) => {
        "use strict";
        a.d(t, { k: () => d });
        var u = a(6179),
          r = a.n(u),
          n = a(6483),
          s = a.n(n),
          o = a(7727);
        const i = "LoupeButton_base_ba",
          l = "LoupeButton_icon_44",
          c = "LoupeButton_iconHover_91",
          _ = "LoupeButton_hoverArea_d0",
          d = ({ onClick: e, hoverAreaClasses: t }) => {
            const a = (0, u.useCallback)(() => (0, o.G)("highlight"), []),
              n = (0, u.useCallback)(() => {
                ((0, o.G)("play"), e());
              }, [e]),
              d = s()(_, t);
            return r().createElement(
              "div",
              { className: i, onClick: n, onMouseEnter: a },
              r().createElement("div", { className: l }),
              r().createElement("div", { className: c }),
              t && r().createElement("div", { className: d }),
            );
          };
      },
      5287: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => u });
        const u = { base: "FormatText_base_d0" };
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
    (__webpack_require__.O = (e, t, a, u) => {
      if (!t) {
        var r = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, a, u] = deferred[i], n = !0, s = 0; s < t.length; s++)
            (!1 & u || r >= u) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[s]))
              ? t.splice(s--, 1)
              : ((n = !1), u < r && (r = u));
          if (n) {
            deferred.splice(i--, 1);
            var o = a();
            void 0 !== o && (e = o);
          }
        }
        return e;
      }
      u = u || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > u; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, a, u];
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
    (__webpack_require__.j = 1488),
    (() => {
      var e = { 1488: 0, 7737: 0, 8363: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, a) => {
          var u,
            r,
            [n, s, o] = a,
            i = 0;
          if (n.some((t) => 0 !== e[t])) {
            for (u in s) __webpack_require__.o(s, u) && (__webpack_require__.m[u] = s[u]);
            if (o) var l = o(__webpack_require__);
          }
          for (t && t(a); i < n.length; i++)
            ((r = n[i]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(l);
        },
        a = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (a.forEach(t.bind(null, 0)), (a.push = t.bind(null, a.push.bind(a))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [1519], () => __webpack_require__(9481));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
