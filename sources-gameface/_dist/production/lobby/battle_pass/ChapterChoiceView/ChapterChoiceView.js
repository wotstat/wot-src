(() => {
  var __webpack_modules__ = {
      2372: (e, u, t) => {
        "use strict";
        t.d(u, { A: () => o });
        var a = t(6179),
          r = t.n(a),
          n = t(4179);
        class o extends r().PureComponent {
          render() {
            let e;
            if ("gold" === this.props.format) e = n.B3.GOLD;
            else e = n.B3.INTEGRAL;
            const u = n.Z5.getNumberFormat(this.props.value, e);
            return void 0 !== this.props.value && void 0 !== u ? u : null;
          }
        }
        o.defaultProps = { format: "integral" };
      },
      280: (e, u, t) => {
        "use strict";
        t.d(u, { z: () => s });
        var a = t(6179),
          r = t.n(a),
          n = t(6483),
          o = t.n(n),
          i = t(3649),
          l = t(5287);
        const s = ({ binding: e, text: u = "", classMix: t, alignment: n = i.v2.left }) =>
          null === u
            ? (console.error("FormatText was supplied with 'null'"), null)
            : r().createElement(
                a.Fragment,
                null,
                u.split("\n").map((u, s) =>
                  r().createElement(
                    "div",
                    { className: o()(l.Z.base, t), key: `${u}-${s}` },
                    (0, i.Uw)(u, n, e).map((e, u) =>
                      r().createElement(a.Fragment, { key: `${u}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, u, t) => {
        "use strict";
        t.d(u, { Y: () => c });
        var a = t(3138),
          r = t(6179),
          n = t(1043),
          o = t(5262);
        const i = a.O.client.getSize("rem"),
          l = i.width,
          s = i.height,
          _ = Object.assign({ width: l, height: s }, (0, o.T)(l, s, n.j)),
          c = (0, r.createContext)(_);
      },
      1039: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => _ });
        var a = t(6179),
          r = t.n(a),
          n = t(6536),
          o = t(3495),
          i = t(1043),
          l = t(5262),
          s = t(3138);
        const _ = (0, a.memo)(({ children: e }) => {
          const u = (0, a.useContext)(o.Y),
            t = (0, a.useState)(u),
            _ = t[0],
            c = t[1],
            m = (0, a.useCallback)((e, u) => {
              const t = s.O.view.pxToRem(e),
                a = s.O.view.pxToRem(u);
              c(Object.assign({ width: t, height: a }, (0, l.T)(t, a, i.j)));
            }, []);
          ((0, n.Z)(() => {
            engine.on("clientResized", m);
          }),
            (0, a.useEffect)(() => () => engine.off("clientResized", m), [m]));
          const d = (0, a.useMemo)(() => Object.assign({}, _), [_]);
          return r().createElement(o.Y.Provider, { value: d }, e);
        });
      },
      6010: (e, u, t) => {
        "use strict";
        var a = t(6179),
          r = t(7382),
          n = t(3495);
        const o = ["children"];
        const i = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, o);
          const i = (0, a.useContext)(n.Y),
            l = i.extraLarge,
            s = i.large,
            _ = i.medium,
            c = i.small,
            m = i.extraSmall,
            d = i.extraLargeWidth,
            E = i.largeWidth,
            A = i.mediumWidth,
            h = i.smallWidth,
            b = i.extraSmallWidth,
            C = i.extraLargeHeight,
            F = i.largeHeight,
            p = i.mediumHeight,
            D = i.smallHeight,
            g = i.extraSmallHeight,
            B = { extraLarge: C, large: F, medium: p, small: D, extraSmall: g };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && l) return u;
            if (t.large && s) return u;
            if (t.medium && _) return u;
            if (t.small && c) return u;
            if (t.extraSmall && m) return u;
          } else {
            if (t.extraLargeWidth && d) return (0, r.H)(u, t, B);
            if (t.largeWidth && E) return (0, r.H)(u, t, B);
            if (t.mediumWidth && A) return (0, r.H)(u, t, B);
            if (t.smallWidth && h) return (0, r.H)(u, t, B);
            if (t.extraSmallWidth && b) return (0, r.H)(u, t, B);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && C) return u;
              if (t.largeHeight && F) return u;
              if (t.mediumHeight && p) return u;
              if (t.smallHeight && D) return u;
              if (t.extraSmallHeight && g) return u;
            }
          }
          return null;
        };
        i.defaultProps = {
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
        (0, a.memo)(i);
      },
      7382: (e, u, t) => {
        "use strict";
        t.d(u, { H: () => a });
        const a = (e, u, t) =>
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
      },
      7739: (e, u, t) => {
        "use strict";
        t.d(u, { YN: () => r.Y, ZN: () => a.Z });
        t(6010);
        var a = t(1039),
          r = t(3495);
      },
      1043: (e, u, t) => {
        "use strict";
        t.d(u, { j: () => a });
        const a = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, u, t) => {
        "use strict";
        var a;
        function r(e, u, t) {
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
        (t.d(u, { T: () => r }),
          (function (e) {
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
          })(a || (a = {})));
      },
      6373: (e, u, t) => {
        "use strict";
        t.d(u, { i: () => s });
        var a = t(2056),
          r = t(6179),
          n = t.n(r);
        const o = ["children", "body", "header", "note", "alert", "args"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = R.views.common.tooltip_window.simple_tooltip_content,
          s = (e) => {
            let u = e.children,
              t = e.body,
              s = e.header,
              _ = e.note,
              c = e.alert,
              m = e.args,
              d = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, o);
            const E = (0, r.useMemo)(() => {
              const e = Object.assign({}, m, { body: t, header: s, note: _, alert: c });
              for (const u in e) void 0 === e[u] && delete e[u];
              return e;
            }, [c, t, s, _, m]);
            return n().createElement(
              a.u,
              i(
                {
                  contentId:
                    ((A = null == m ? void 0 : m.hasHtmlContent),
                    A ? l.SimpleTooltipHtmlContent("resId") : l.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: E,
                },
                d,
              ),
              u,
            );
            var A;
          };
      },
      2056: (e, u, t) => {
        "use strict";
        t.d(u, { u: () => s });
        var a = t(7902),
          r = t(4179),
          n = t(6179);
        const o = [
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
        function i(e) {
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
        const l = (e, u, t = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: r.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: u,
                  targetID: a,
                },
                t,
              ),
            );
          },
          s = (e) => {
            let u = e.children,
              t = e.contentId,
              r = e.args,
              s = e.onMouseEnter,
              _ = e.onMouseLeave,
              c = e.onMouseDown,
              m = e.onClick,
              d = e.ignoreShowDelay,
              E = void 0 !== d && d,
              A = e.ignoreMouseClick,
              h = void 0 !== A && A,
              b = e.decoratorId,
              C = void 0 === b ? 0 : b,
              F = e.isEnabled,
              p = void 0 === F || F,
              D = e.targetId,
              g = void 0 === D ? 0 : D,
              B = e.onShow,
              v = e.onHide,
              w = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, o);
            const f = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              S = (0, n.useMemo)(() => g || (0, a.F)().resId, [g]),
              x = (0, n.useCallback)(() => {
                (f.current.isVisible && f.current.timeoutId) ||
                  (l(t, C, { isMouseEvent: !0, on: !0, arguments: i(r) }, S),
                  B && B(),
                  (f.current.isVisible = !0));
              }, [t, C, r, S, B]),
              L = (0, n.useCallback)(() => {
                if (f.current.isVisible || f.current.timeoutId) {
                  const e = f.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (f.current.timeoutId = 0)),
                    l(t, C, { on: !1 }, S),
                    f.current.isVisible && v && v(),
                    (f.current.isVisible = !1));
                }
              }, [t, C, S, v]),
              y = (0, n.useCallback)((e) => {
                f.current.isVisible &&
                  ((f.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (f.current.hideTimerId = window.setTimeout(() => {
                    const u = document.elementFromPoint(e.clientX, e.clientY);
                    u && !u.isSameNode(f.current.prevTarget) && L();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const e = f.current.hideTimerId;
              return (
                document.addEventListener("wheel", y, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", y, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === p && L();
              }, [p, L]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", L),
                  () => {
                    (window.removeEventListener("mouseleave", L), L());
                  }
                ),
                [L],
              ));
            return p
              ? (0, n.cloneElement)(
                  u,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((P = u.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((f.current.timeoutId = window.setTimeout(x, E ? 100 : 400)),
                            s && s(e),
                            P && P(e));
                        }),
                      onMouseLeave: ((e) => (u) => {
                        (L(), null == _ || _(u), null == e || e(u));
                      })(u.props.onMouseLeave),
                      onClick: ((e) => (u) => {
                        (!1 === h && L(), null == m || m(u), null == e || e(u));
                      })(u.props.onClick),
                      onMouseDown: ((e) => (u) => {
                        (!1 === h && L(), null == c || c(u), null == e || e(u));
                      })(u.props.onMouseDown),
                    },
                    w,
                  ),
                )
              : u;
            var P;
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
      122: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => a });
        const a = (e, u) => {
          let t;
          const a = setTimeout(() => {
            t = e();
          }, u);
          return () => {
            ("function" == typeof t && t(), clearTimeout(a));
          };
        };
      },
      527: (e, u, t) => {
        "use strict";
        (t.r(u), t.d(u, { mouse: () => i, onResize: () => n }));
        var a = t(2472),
          r = t(1176);
        const n = (0, a.E)("clientResized"),
          o = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
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
                    i = o[u]((e) => t([e, "outside"]));
                  function l(e) {
                    t([e, "inside"]);
                  }
                  return (
                    window.addEventListener(n, l),
                    a(),
                    () => {
                      r &&
                        (i(), window.removeEventListener(n, l), (e.listeners -= 1), a(), (r = !1));
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
      5959: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            events: () => a,
            getMouseGlobalPosition: () => n,
            getSize: () => r,
            graphicsQuality: () => o,
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
        const o = {
          isLow: () => 1 === viewEnv.getGraphicsQuality(),
          isHigh: () => 0 === viewEnv.getGraphicsQuality(),
          get: () => viewEnv.getGraphicsQuality(),
        };
      },
      1176: (e, u, t) => {
        "use strict";
        function a(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        t.d(u, { R: () => a });
      },
      2472: (e, u, t) => {
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
      3138: (e, u, t) => {
        "use strict";
        t.d(u, { O: () => r });
        var a = t(5959);
        const r = { view: t(7641), client: a };
      },
      3722: (e, u, t) => {
        "use strict";
        function a(e, u, t = 1) {
          return viewEnv.getChildTexturePath(e, u.width, u.height, t);
        }
        function r(e, u, t) {
          return `url(${a(e, u, t)})`;
        }
        (t.r(u), t.d(u, { getBgUrl: () => r, getTextureUrl: () => a }));
      },
      6112: (e, u, t) => {
        "use strict";
        t.d(u, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, u, t) => {
        "use strict";
        t.d(u, { U: () => r });
        var a = t(2472);
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
      7641: (e, u, t) => {
        "use strict";
        (t.r(u),
          t.d(u, {
            addModelObserver: () => _,
            addPreloadTexture: () => i,
            children: () => a,
            displayStatus: () => r.W,
            displayStatusIs: () => f,
            events: () => n.U,
            extraSize: () => S,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => A,
            getBrowserTexturePath: () => s,
            getDisplayStatus: () => w,
            getScale: () => h,
            getSize: () => m,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => D,
            isEventHandled: () => B,
            isFocused: () => p,
            pxToRem: () => b,
            remToPx: () => C,
            resize: () => d,
            sendEvent: () => o.qP,
            setAnimateWindow: () => F,
            setEventHandled: () => g,
            setInputPaddingsRem: () => l,
            setSidePaddingsRem: () => c,
            whenTutorialReady: () => x,
          }));
        var a = t(3722),
          r = t(6112),
          n = t(6538),
          o = t(8566);
        function i(e) {
          viewEnv.addPreloadTexture(e);
        }
        function l(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function s(e, u, t, a = 1) {
          return viewEnv.getWebBrowserTexturePath(e, u, t, a);
        }
        function _(e, u, t) {
          return viewEnv.addDataChangedCallback(e, u, t);
        }
        function c(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function m(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function d(e, u, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(e, u) : viewEnv.resizeViewPx(e, u);
        }
        function E(e = "rem") {
          const u = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? u : { x: C(u.x), y: C(u.y) };
        }
        function A() {
          viewEnv.freezeTextureBeforeResize();
        }
        function h() {
          return viewEnv.getScale();
        }
        function b(e) {
          return viewEnv.pxToRem(e);
        }
        function C(e) {
          return viewEnv.remToPx(e);
        }
        function F(e, u) {
          viewEnv.setAnimateWindow(e, u);
        }
        function p() {
          return viewEnv.isFocused();
        }
        function D() {
          return viewEnv.isClientAccessible();
        }
        function g() {
          return viewEnv.setEventHandled();
        }
        function B() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function w() {
          return viewEnv.getShowingStatus();
        }
        const f = Object.keys(r.W).reduce(
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
      8566: (e, u, t) => {
        "use strict";
        t.d(u, { qP: () => s });
        const a = ["args"];
        const r = 2,
          n = 16,
          o = 32,
          i = 64,
          l = (e, u) => {
            const t = "GFViewEventProxy";
            if (void 0 !== u) {
              const n = u.args,
                o = (function (e, u) {
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
                    Object.assign({ __Type: t, type: e }, o, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: e }, o));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: e });
            var r;
          },
          s = {
            close(e) {
              l("popover" === e ? r : o);
            },
            minimize() {
              l(i);
            },
            move(e) {
              l(n, { isMouseEvent: !0, on: e });
            },
          };
      },
      7902: (e, u, t) => {
        "use strict";
        t.d(u, { F: () => a });
        const a = (e = 1) => {
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
        };
      },
      6536: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => r });
        var a = t(6179);
        const r = (e) => {
          const u = (0, a.useRef)(!1);
          u.current || (e(), (u.current = !0));
        };
      },
      5415: (e, u, t) => {
        "use strict";
        t.d(u, { Aq: () => l, GS: () => s, cJ: () => o, fd: () => i });
        var a = t(6179),
          r = t(7739),
          n = t(1043);
        let o, i, l;
        (!(function (e) {
          ((e[(e.ExtraSmall = n.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = n.j.small.width)] = "Small"),
            (e[(e.Medium = n.j.medium.width)] = "Medium"),
            (e[(e.Large = n.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = n.j.extraLarge.width)] = "ExtraLarge"));
        })(o || (o = {})),
          (function (e) {
            ((e[(e.ExtraSmall = n.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = n.j.small.width)] = "Small"),
              (e[(e.Medium = n.j.medium.width)] = "Medium"),
              (e[(e.Large = n.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = n.j.extraLarge.width)] = "ExtraLarge"));
          })(i || (i = {})),
          (function (e) {
            ((e[(e.ExtraSmall = n.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = n.j.small.height)] = "Small"),
              (e[(e.Medium = n.j.medium.height)] = "Medium"),
              (e[(e.Large = n.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = n.j.extraLarge.height)] = "ExtraLarge"));
          })(l || (l = {})));
        const s = () => {
          const e = (0, a.useContext)(r.YN),
            u = e.width,
            t = e.height,
            n = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return o.ExtraLarge;
                case e.large:
                  return o.Large;
                case e.medium:
                  return o.Medium;
                case e.small:
                  return o.Small;
                case e.extraSmall:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(e),
            s = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return i.ExtraLarge;
                case e.largeWidth:
                  return i.Large;
                case e.mediumWidth:
                  return i.Medium;
                case e.smallWidth:
                  return i.Small;
                case e.extraSmallWidth:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(e),
            _ = ((e) => {
              switch (!0) {
                case e.extraLargeHeight:
                  return l.ExtraLarge;
                case e.largeHeight:
                  return l.Large;
                case e.mediumHeight:
                  return l.Medium;
                case e.smallHeight:
                  return l.Small;
                case e.extraSmallHeight:
                  return l.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), l.ExtraSmall);
              }
            })(e);
          return {
            mediaSize: n,
            mediaWidth: s,
            mediaHeight: _,
            remScreenWidth: u,
            remScreenHeight: t,
          };
        };
      },
      5521: (e, u, t) => {
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
      7727: (e, u, t) => {
        "use strict";
        function a(e) {
          engine.call("PlaySound", e);
        }
        t.d(u, { $: () => r, G: () => a });
        const r = {
          playHighlight() {
            a("highlight");
          },
          playClick() {
            a("play");
          },
          playYes() {
            a("yes1");
          },
        };
      },
      3649: (e, u, t) => {
        "use strict";
        let a;
        function r(e, u) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const t = 0 === e.indexOf("%") ? 2 : 1;
            return String(u[e.slice(t, -t)]);
          });
        }
        function n(e) {
          return e.replace(/-/g, "_");
        }
        function o(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        (t.d(u, { BN: () => n, Uw: () => d, e: () => o, uF: () => r, v2: () => a }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(a || (a = {})));
        const i = (e, u, t) => {
            if (t % 2) {
              const t = e.pop();
              return [...e, t + u];
            }
            return [...e, u];
          },
          l = (e, u, t) => {
            if (0 === t) return [u];
            if (t % 2) return [...e, " " === u ? " " : u];
            {
              const t = e.pop();
              return [...e, t + u];
            }
          },
          s = (e, u, t = a.left) => e.split(u).reduce(t === a.left ? i : l, []),
          _ = (() => {
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
          c = ["zh_cn", "zh_sg", "zh_tw"],
          m = (e, u = a.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return c.includes(t)
              ? _(e)
              : ((e, u = a.left) => {
                  let t = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    n = e.replace(/&nbsp;/g, " ");
                  return (s(n, /( )/, u).forEach((e) => (t = t.concat(s(e, r, a.left)))), t);
                })(e, u);
          },
          d = (e, u, t) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (t && e in t ? t[e] : m(e, u)));
      },
      1358: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => n });
        var a = t(3138);
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
      4179: (e, u, t) => {
        "use strict";
        t.d(u, { Sw: () => n.Z, B3: () => s, Z5: () => o, B0: () => l, ry: () => C });
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
        var n = t(1358);
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
        let l;
        !(function (e) {
          ((e[(e.UNDEFINED = 0)] = "UNDEFINED"),
            (e[(e.TOOLTIP = 1)] = "TOOLTIP"),
            (e[(e.POP_OVER = 2)] = "POP_OVER"),
            (e[(e.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (e[(e.DROP_DOWN = 8)] = "DROP_DOWN"),
            (e[(e.MOVE = 16)] = "MOVE"),
            (e[(e.CLOSE = 32)] = "CLOSE"),
            (e[(e.MINIMIZE = 64)] = "MINIMIZE"));
        })(l || (l = {}));
        const s = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          _ = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          c = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var d = t(5521),
          E = t(3138);
        const A = ["args"];
        function h(e, u, t, a, r, n, o) {
          try {
            var i = e[n](o),
              l = i.value;
          } catch (e) {
            return void t(e);
          }
          i.done ? u(l) : Promise.resolve(l).then(a, r);
        }
        const b = (e) => ({
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
                  return new Promise(function (a, r) {
                    var n = e.apply(u, t);
                    function o(e) {
                      h(n, a, r, o, i, "next", e);
                    }
                    function i(e) {
                      h(n, a, r, o, i, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return u.apply(this, arguments);
            };
          })(),
          F = (e, u) => {
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
          p = () => F(l.CLOSE),
          D = (e, u) => {
            e.keyCode === d.n.ESCAPE && u();
          };
        var g = t(7572);
        const B = r.instance,
          v = {
            DataTracker: n.Z,
            ViewModel: g.Z,
            ViewEventType: l,
            NumberFormatType: s,
            RealFormatType: _,
            TimeFormatType: c,
            DateFormatType: m,
            makeGlobalBoundingBox: b,
            sendMoveEvent: (e) => F(l.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: p,
            sendClosePopOverEvent: () => F(l.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (e, u, t = 0) => {
              F(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: t,
                args: u,
              });
            },
            sendShowPopOverEvent: (e, u, t, a, r = R.invalid("resId"), n) => {
              const o = E.O.view.getViewGlobalPosition(),
                i = t.getBoundingClientRect(),
                s = i.x,
                _ = i.y,
                c = i.width,
                m = i.height,
                d = {
                  x: E.O.view.pxToRem(s) + o.x,
                  y: E.O.view.pxToRem(_) + o.y,
                  width: E.O.view.pxToRem(c),
                  height: E.O.view.pxToRem(m),
                };
              F(l.POP_OVER, {
                isMouseEvent: !0,
                contentID: e,
                decoratorID: a || R.invalid("resId"),
                targetID: r,
                direction: u,
                bbox: b(d),
                on: !0,
                args: n,
              });
            },
            addEscapeListener: (e) => {
              const u = (u) => D(u, e);
              return (
                window.addEventListener("keydown", u),
                () => window.removeEventListener("keydown", u)
              );
            },
            closeOnEsc: (e) => {
              D(e, p);
            },
            handleViewEvent: F,
            onBindingsReady: C,
            onLayoutReady: () =>
              new Promise((e) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    e();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(l.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(l.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(l.POP_OVER),
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
            ClickOutsideManager: B,
            SystemLocale: o,
            UserLocale: i,
          };
        window.ViewEnvHelper = v;
      },
      908: (e, u, t) => {
        "use strict";
        var a = t(7739),
          r = t(6179),
          n = t.n(r),
          o = t(6483),
          i = t.n(o),
          l = t(926),
          s = t.n(l),
          _ = t(5415);
        const c = ["children", "className"];
        function m() {
          return (
            (m =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            m.apply(this, arguments)
          );
        }
        const d = {
            [_.fd.ExtraSmall]: "",
            [_.fd.Small]: s().SMALL_WIDTH,
            [_.fd.Medium]: `${s().SMALL_WIDTH} ${s().MEDIUM_WIDTH}`,
            [_.fd.Large]: `${s().SMALL_WIDTH} ${s().MEDIUM_WIDTH} ${s().LARGE_WIDTH}`,
            [_.fd.ExtraLarge]:
              `${s().SMALL_WIDTH} ${s().MEDIUM_WIDTH} ${s().LARGE_WIDTH} ${s().EXTRA_LARGE_WIDTH}`,
          },
          E = {
            [_.Aq.ExtraSmall]: "",
            [_.Aq.Small]: s().SMALL_HEIGHT,
            [_.Aq.Medium]: `${s().SMALL_HEIGHT} ${s().MEDIUM_HEIGHT}`,
            [_.Aq.Large]: `${s().SMALL_HEIGHT} ${s().MEDIUM_HEIGHT} ${s().LARGE_HEIGHT}`,
            [_.Aq.ExtraLarge]:
              `${s().SMALL_HEIGHT} ${s().MEDIUM_HEIGHT} ${s().LARGE_HEIGHT} ${s().EXTRA_LARGE_HEIGHT}`,
          },
          A = {
            [_.cJ.ExtraSmall]: "",
            [_.cJ.Small]: s().SMALL,
            [_.cJ.Medium]: `${s().SMALL} ${s().MEDIUM}`,
            [_.cJ.Large]: `${s().SMALL} ${s().MEDIUM} ${s().LARGE}`,
            [_.cJ.ExtraLarge]: `${s().SMALL} ${s().MEDIUM} ${s().LARGE} ${s().EXTRA_LARGE}`,
          },
          h = (e) => {
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
              })(e, c);
            const r = (0, _.GS)(),
              o = r.mediaWidth,
              l = r.mediaHeight,
              s = r.mediaSize;
            return n().createElement("div", m({ className: i()(t, d[o], E[l], A[s]) }, a), u);
          },
          b = ["children"];
        const C = (e) => {
          let u = e.children,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, b);
          return n().createElement(a.ZN, null, n().createElement(h, t, u));
        };
        var F = t(493),
          p = t.n(F),
          D = t(7727);
        const g = {
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
          B = [
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
        function v() {
          return (
            (v =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            v.apply(this, arguments)
          );
        }
        class w extends n().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (u) => {
                (e && e(u),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, D.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (u) => {
                (e && e(u), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (u) => {
                (e && e(u),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, D.G)(this.props.soundClick));
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
              o = e.type,
              l = e.classNames,
              s = e.onMouseEnter,
              _ = e.onMouseLeave,
              c = e.onMouseDown,
              m = e.onMouseUp,
              d =
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
                })(e, B)),
              E = i()(g.base, g[`base__${o}`], g[`base__${r}`], null == l ? void 0 : l.base),
              A = i()(g.icon, g[`icon__${o}`], g[`icon__${r}`], null == l ? void 0 : l.icon),
              h = i()(g.glow, null == l ? void 0 : l.glow),
              b = i()(g.caption, g[`caption__${o}`], null == l ? void 0 : l.caption),
              C = i()(g.goto, null == l ? void 0 : l.goto);
            return n().createElement(
              "div",
              v(
                {
                  className: E,
                  onMouseEnter: this._onMouseEnter(s),
                  onMouseLeave: this._onMouseLeave(_),
                  onMouseDown: this._onMouseDown(c),
                  onMouseUp: this._onMouseUp(m),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                d,
              ),
              "info" !== o && n().createElement("div", { className: g.shine }),
              n().createElement(
                "div",
                { className: A },
                n().createElement("div", { className: h }),
              ),
              n().createElement("div", { className: b }, u),
              a && n().createElement("div", { className: C }, a),
            );
          }
        }
        let f, S;
        ((w.defaultProps = {
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
          })(f || (f = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(S || (S = {})));
        const x = (e) => {
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
        };
        var L = t(3138),
          y = t(5521),
          P = t(4179);
        const M = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function k(e = y.n.NONE, u = M, t = !1) {
          (0, r.useEffect)(() => {
            if (e !== y.n.NONE)
              return (
                window.addEventListener("keydown", a, t),
                () => {
                  window.removeEventListener("keydown", a, t);
                }
              );
            function a(a) {
              if (a.keyCode === e) {
                if (L.O.view.isEventHandled()) return;
                (L.O.view.setEventHandled(), u(a), t && a.stopPropagation());
              }
            }
          }, [u, e, t]);
        }
        function T(e, u) {
          var t;
          if (!(u >= e.length))
            return Array.isArray(e) ? e[u] : null == (t = e[u]) ? void 0 : t.value;
        }
        const N = T;
        function I(e, u) {
          return Array.isArray(e)
            ? e.map(u)
            : e.map((e, t, a) => u(null == e ? void 0 : e.value, t, a));
        }
        function O(e, u) {
          if (Array.isArray(e)) return e.some(u);
          for (let t = 0; t < e.length; t++) {
            if (u(N(e, t), t, e)) return !0;
          }
          return !1;
        }
        var H = t(3403),
          $ = t(903);
        let G, W;
        (!(function (e) {
          ((e.style = "style"),
            (e.tankman = "tankman"),
            (e.vehicle = "vehicle"),
            (e.mixed = "mixed"));
        })(G || (G = {})),
          (function (e) {
            ((e.Default = "default"), (e.Marathon = "marathon"), (e.Resource = "resource"));
          })(W || (W = {})));
        (G.style, G.tankman);
        var U = t(6895);
        const z = (e) => ({
          level: (null == e ? void 0 : e.currentLevel) || 0,
          to: null == e ? void 0 : e.levelProgression,
          from: null == e ? void 0 : e.levelProgression,
        });
        let j;
        !(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Large = "large"));
        })(j || (j = {}));
        function X() {
          return !1;
        }
        console.log;
        var q = t(9174);
        function V(e, u) {
          var t = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (t) return (t = t.call(e)).next.bind(t);
          if (
            Array.isArray(e) ||
            (t = (function (e, u) {
              if (!e) return;
              if ("string" == typeof e) return Y(e, u);
              var t = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === t && e.constructor && (t = e.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(e);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return Y(e, u);
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
        function Y(e, u) {
          (null == u || u > e.length) && (u = e.length);
          for (var t = 0, a = new Array(u); t < u; t++) a[t] = e[t];
          return a;
        }
        const K = (e) => (0 === e ? window : window.subViews.get(e));
        const Z = (e) =>
          null !== e && "object" == typeof e
            ? "CoherentArrayProxy" === e.constructor.name
              ? I(e, (e) => ("object" == typeof e ? Z(e) : e))
              : Array.isArray(e)
                ? e.map((e) => ("object" == typeof e ? Z(e) : e))
                : Object.fromEntries(
                    Object.entries(e).map(([e, u]) => [e, "object" == typeof u ? Z(u) : u]),
                  )
            : e;
        var Q = t(3946);
        const J = ["red", "yellow", "blue", "green"],
          ee = ((e, u) => {
            const t = (0, r.createContext)({});
            return [
              function ({ mode: a = "real", options: o, children: i, mocks: l }) {
                const s = (0, r.useRef)([]),
                  _ = (t, a, r) => {
                    var n;
                    const o = (function ({
                        initializer: e = !0,
                        rootId: u = 0,
                        getRoot: t = K,
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
                        const o = (e) => {
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
                            const i = "string" == typeof n ? `${a}.${n}` : a,
                              l = L.O.view.addModelObserver(i, u, !0);
                            return (r.set(l, t), e && t(o(n)), l);
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
                            for (var e, t = V(r.keys()); !(e = t()).done;) n(e.value, u);
                          },
                          unsubscribe: n,
                        };
                      })(a),
                      i =
                        "real" === t
                          ? o
                          : Object.assign({}, o, {
                              readByPath:
                                null != (n = null == r ? void 0 : r.getter) ? n : () => {},
                            }),
                      l = (e) =>
                        "mocks" === t ? (null == r ? void 0 : r.getter(e)) : i.readByPath(e),
                      _ = (e) => s.current.push(e),
                      c = e({
                        mode: t,
                        readByPath: l,
                        externalModel: i,
                        observableModel: {
                          array: (e, u) => {
                            const a = null != u ? u : l(e),
                              r = q.LO.box(a, { equals: X });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, q.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          object: (e, u) => {
                            const a = null != u ? u : l(e),
                              r = q.LO.box(a, { equals: X });
                            return (
                              "real" === t &&
                                i.subscribe(
                                  (0, q.aD)((e) => r.set(e)),
                                  e,
                                ),
                              r
                            );
                          },
                          primitives: (e, u) => {
                            const a = l(u);
                            if (Array.isArray(e)) {
                              const r = e.reduce((e, u) => ((e[u] = q.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, q.aD)((u) => {
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
                                o = n.reduce((e, [u, t]) => ((e[t] = q.LO.box(a[u], {})), e), {});
                              return (
                                "real" === t &&
                                  i.subscribe(
                                    (0, q.aD)((e) => {
                                      n.forEach(([u, t]) => {
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
                        cleanup: _,
                      }),
                      m = { mode: t, model: c, externalModel: i, cleanup: _ };
                    return {
                      model: c,
                      controls: "mocks" === t && r ? r.controls(m) : u(m),
                      externalModel: i,
                      mode: t,
                    };
                  },
                  c = (0, r.useRef)(!1),
                  m = (0, r.useState)(a),
                  d = m[0],
                  E = m[1],
                  A = (0, r.useState)(() => _(a, o, l)),
                  h = A[0],
                  b = A[1];
                return (
                  (0, r.useEffect)(() => {
                    c.current ? b(_(d, o, l)) : (c.current = !0);
                  }, [l, d, o]),
                  (0, r.useEffect)(() => {
                    E(a);
                  }, [a]),
                  (0, r.useEffect)(
                    () => () => {
                      (h.externalModel.dispose(), s.current.forEach((e) => e()));
                    },
                    [h],
                  ),
                  n().createElement(t.Provider, { value: h }, i)
                );
              },
              () => (0, r.useContext)(t),
            ];
          })(
            ({ observableModel: e }) => {
              const u = {
                  root: e.object(),
                  collectionEntryPoint: e.object("collectionEntryPoint"),
                  chapterTypes: e.array("availableChapterTypes"),
                  chapters: e.array("chapters"),
                },
                t = (0, Q.Om)(() => O(u.chapters.get(), ({ chapterState: e }) => e === f.Active), {
                  equals: X,
                }),
                a = (0, Q.Om)(
                  () =>
                    (function (e, u) {
                      if (Array.isArray(e)) return e.every(u);
                      for (let t = 0; t < e.length; t++) if (!u(N(e, t), t, e)) return !1;
                      return !0;
                    })(u.chapters.get(), ({ chapterState: e }) => e === f.Completed),
                  { equals: X },
                ),
                r = (0, Q.Om)(() => O(u.chapters.get(), ({ chapterType: e }) => e === W.Marathon), {
                  equals: X,
                }),
                n = (0, Q.Om)(
                  () => {
                    return ((e = u.chapters.get()), Z(e));
                    var e;
                  },
                  { equals: X },
                ),
                o = (0, Q.Om)(
                  (e) => {
                    if (e) return n().find((u) => u.chapterID === e);
                  },
                  { equals: X },
                ),
                i = (0, Q.Om)((e) => (e ? J[(e % 10) - 1] : null), { equals: X }),
                l = (0, Q.Om)((e) => O(u.chapters.get(), (u) => u.chapterType === e), {
                  equals: X,
                }),
                s = (0, Q.Om)(
                  () => {
                    var e;
                    return null ==
                      (e = n().find(
                        (e) => e.chapterState === f.NotStarted || e.chapterState === f.Paused,
                      ))
                      ? void 0
                      : e.chapterID;
                  },
                  { equals: X },
                );
              return Object.assign({}, u, {
                computes: {
                  getChapterById: o,
                  hasChapter: l,
                  hasActive: t,
                  isCompleted: a,
                  getChapters: n,
                  getChapterColor: i,
                  hasMarathon: r,
                  getTriggerChapterId: s,
                },
              });
            },
            ({ externalModel: e }) => ({
              selectChapter: e.createCallback((e) => ({ chapterID: e }), "onChapterSelect"),
              buyChapter: e.createCallback((e) => ({ chapterID: e }), "onBuyClick"),
              openPreview: e.createCallback((e) => ({ chapterID: e }), "onPreviewClick"),
              openAbout: e.createCallbackNoArgs("onAboutClick"),
              openPointsInfo: e.createCallbackNoArgs("onPointsInfoClick"),
              takeRewards: e.createCallbackNoArgs("onTakeRewardsClick"),
              openGoodsForBpCoins: e.createCallbackNoArgs("onBpcoinClick"),
              openGoodsForBpPoints: e.createCallbackNoArgs("onBpbitClick"),
              onViewLoaded: e.createCallbackNoArgs("onViewLoaded"),
              close: e.createCallbackNoArgs("onClose"),
              activateChapter: e.createCallback((e) => ({ chapterID: e }), "onActivateChapter"),
              openCollection: e.createCallbackNoArgs("collectionEntryPoint.openCollection"),
            }),
          ),
          ue = ee[0],
          te = ee[1],
          ae = {
            base: "App_base_26",
            backgroundBlur: "App_backgroundBlur_26",
            background: "App_background_6b",
            infoButtons: "App_infoButtons_78",
            header: "App_header_41",
            flags: "App_flags_d9",
            divider: "App_divider_21",
            chapters: "App_chapters_8a",
            chapterLeft: "App_chapterLeft_91",
            chapterRight: "App_chapterRight_5c",
            chapterHolder: "App_chapterHolder_48",
            base__hasMarathon: "App_base__hasMarathon_7f",
          },
          re = {
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
        let ne, oe;
        (!(function (e) {
          ((e.main = "main"),
            (e.primary = "primary"),
            (e.primaryGreen = "primaryGreen"),
            (e.primaryRed = "primaryRed"),
            (e.secondary = "secondary"),
            (e.ghost = "ghost"));
        })(ne || (ne = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(oe || (oe = {})));
        const ie = ({
          children: e,
          size: u,
          isFocused: t,
          type: a,
          disabled: o,
          mixClass: l,
          soundHover: s,
          soundClick: _,
          onMouseEnter: c,
          onMouseMove: m,
          onMouseDown: d,
          onMouseUp: E,
          onMouseLeave: A,
          onClick: h,
        }) => {
          const b = (0, r.useRef)(null),
            C = (0, r.useState)(t),
            F = C[0],
            p = C[1],
            g = (0, r.useState)(!1),
            B = g[0],
            v = g[1],
            w = (0, r.useState)(!1),
            f = w[0],
            S = w[1],
            x = (0, r.useCallback)(() => {
              o || (b.current && (b.current.focus(), p(!0)));
            }, [o]),
            L = (0, r.useCallback)(
              (e) => {
                F && null !== b.current && !b.current.contains(e.target) && p(!1);
              },
              [F],
            ),
            y = (0, r.useCallback)(
              (e) => {
                o || (h && h(e));
              },
              [o, h],
            ),
            P = (0, r.useCallback)(
              (e) => {
                o || (null !== s && (0, D.G)(s), c && c(e), S(!0));
              },
              [o, s, c],
            ),
            M = (0, r.useCallback)(
              (e) => {
                m && m(e);
              },
              [m],
            ),
            k = (0, r.useCallback)(
              (e) => {
                o || (E && E(e), v(!1));
              },
              [o, E],
            ),
            T = (0, r.useCallback)(
              (e) => {
                o || (null !== _ && (0, D.G)(_), d && d(e), t && x(), v(!0));
              },
              [o, _, d, x, t],
            ),
            N = (0, r.useCallback)(
              (e) => {
                o || (A && A(e), v(!1));
              },
              [o, A],
            ),
            I = i()(
              re.base,
              re[`base__${a}`],
              {
                [re.base__disabled]: o,
                [re[`base__${u}`]]: u,
                [re.base__focus]: F,
                [re.base__highlightActive]: B,
                [re.base__firstHover]: f,
              },
              l,
            ),
            O = i()(re.state, re.state__default);
          return (
            (0, r.useEffect)(
              () => (
                document.addEventListener("mousedown", L),
                () => {
                  document.removeEventListener("mousedown", L);
                }
              ),
              [L],
            ),
            (0, r.useEffect)(() => {
              p(t);
            }, [t]),
            n().createElement(
              "div",
              {
                ref: b,
                className: I,
                onMouseEnter: P,
                onMouseMove: M,
                onMouseUp: k,
                onMouseDown: T,
                onMouseLeave: N,
                onClick: y,
              },
              a !== ne.ghost &&
                n().createElement(
                  n().Fragment,
                  null,
                  n().createElement("div", { className: re.back }),
                  n().createElement("span", { className: re.texture }),
                ),
              n().createElement(
                "span",
                { className: O },
                n().createElement("span", { className: re.stateDisabled }),
                n().createElement("span", { className: re.stateHighlightHover }),
                n().createElement("span", { className: re.stateHighlightActive }),
              ),
              n().createElement(
                "span",
                { className: re.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        ie.defaultProps = {
          type: ne.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const le = (0, r.memo)(ie),
          se = {
            base: "Preview_base_1f",
            base__hovered: "Preview_base__hovered_ee",
            icon: "Preview_icon_f3",
            icon__small: "Preview_icon__small_a1",
            icon__normal: "Preview_icon__normal_5c",
            base__mouseDown: "Preview_base__mouseDown_d0",
            label: "Preview_label_2e",
            base__visibleLabel: "Preview_base__visibleLabel_92",
          },
          _e = [
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
        function ce() {
          return (
            (ce =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ce.apply(this, arguments)
          );
        }
        let me;
        !(function (e) {
          ((e.SMALL = "small"), (e.NORMAL = "normal"));
        })(me || (me = {}));
        const de = (0, r.memo)((e) => {
          let u = e.label,
            t = e.isVisibleLabel,
            a = void 0 !== t && t,
            o = e.autofocus,
            l = void 0 !== o && o,
            s = e.soundHover,
            _ = void 0 === s ? "highlight" : s,
            c = e.soundClick,
            m = void 0 === c ? "play" : c,
            d = e.size,
            E = void 0 === d ? me.NORMAL : d,
            A = e.classNames,
            h = e.onClick,
            b = e.onMouseEnter,
            C = e.onMouseLeave,
            F = e.onMouseDown,
            p = e.onMouseUp,
            g = e.onFocus,
            B = e.onBlur,
            v = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, _e);
          const w = (0, r.useState)(!1),
            f = w[0],
            S = w[1],
            x = (0, r.useState)(!1),
            L = x[0],
            y = x[1],
            P = (0, r.useState)(l),
            M = P[0],
            k = P[1],
            T = (0, r.useRef)(null),
            N = (0, r.useCallback)(() => {
              T.current && (T.current.focus(), k(!0));
            }, []),
            R = (0, r.useCallback)(
              (e) => {
                M && null !== T.current && !T.current.contains(e.target) && k(!1);
              },
              [M],
            );
          ((0, r.useEffect)(
            () => (
              document.addEventListener("mousedown", R),
              () => {
                document.removeEventListener("mousedown", R);
              }
            ),
            [R],
          ),
            (0, r.useEffect)(() => {
              k(l);
            }, [l]));
          const I = (0, r.useCallback)(
              (e) => {
                h && h(e);
              },
              [h],
            ),
            O = (0, r.useCallback)(
              (e) => {
                (S(!0), F && F(e), m && (0, D.G)(m), l && N());
              },
              [l, F, N, m],
            ),
            H = (0, r.useCallback)(
              (e) => {
                (S(!1), p && p(e));
              },
              [p],
            ),
            $ = (0, r.useCallback)(
              (e) => {
                (b && b(e), _ && (0, D.G)(_), y(!0));
              },
              [b, _],
            ),
            G = (0, r.useCallback)(
              (e) => {
                (S(!1), y(!1), C && C(e));
              },
              [C],
            ),
            W = (0, r.useCallback)(
              (e) => {
                (k(!0), g && g(e));
              },
              [g],
            ),
            U = (0, r.useCallback)(
              (e) => {
                (k(!1), B && B(e));
              },
              [B],
            ),
            z = i()(
              se.base,
              a && se.base__visibleLabel,
              f && se.base__mouseDown,
              L && se.base__hovered,
              M && se.base__focused,
              null == A ? void 0 : A.base,
            ),
            j = i()(se.icon, se[`icon__${E}`], null == A ? void 0 : A.icon),
            X = i()(se.label, null == A ? void 0 : A.label);
          return n().createElement(
            "div",
            ce(
              {
                ref: T,
                className: z,
                onClick: I,
                onMouseEnter: $,
                onMouseLeave: G,
                onMouseDown: O,
                onMouseUp: H,
                onFocus: W,
                onBlur: U,
              },
              v,
            ),
            n().createElement("div", { className: j }),
            n().createElement("div", { className: X }, u),
          );
        });
        var Ee = t(9887),
          Ae = t.n(Ee);
        const he = ["xl", "lg", "md", "sm", "xs"],
          be = (e) => e.includes("_") && ((e) => he.includes(e))(e.split("_").at(-1)),
          Ce = [_.cJ.ExtraLarge, _.cJ.Large, _.cJ.Medium, _.cJ.Small, _.cJ.ExtraSmall],
          Fe = (e, u) =>
            Object.keys(e).reduce((t, a) => {
              if (a in t) return t;
              if (be(a)) {
                const r = a.split("_").slice(0, -1).join("_");
                if (r in t) return t;
                const n = Ce.indexOf(u),
                  o = (-1 !== n ? he.slice(n) : [])
                    .map((e) => r + "_" + e)
                    .find((u) => void 0 !== e[u]),
                  i = o ? e[o] : void 0;
                return ((t[r] = void 0 !== i ? i : e[r]), t);
              }
              const r = e[a];
              return (
                void 0 === r ||
                  ((e, u) => he.some((t) => void 0 !== u[`${e}_${t}`]))(a, e) ||
                  (t[a] = r),
                t
              );
            }, {}),
          pe = (e, u = Fe) => {
            const t = (
              (e, u = Fe) =>
              (t) => {
                const a = (0, _.GS)().mediaSize,
                  o = (0, r.useMemo)(() => u(t, a), [t, a]);
                return n().createElement(e, o);
              }
            )(e, u);
            return n().memo((u) =>
              Object.keys(u).some((e) => be(e) && void 0 !== u[e])
                ? n().createElement(t, u)
                : n().createElement(e, u),
            );
          },
          De = {
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
        function Be() {
          return (
            (Be =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Be.apply(this, arguments)
          );
        }
        Object.keys(Ae());
        const ve = {
            XL: { mt: De.mt__XL, mr: De.mr__XL, mb: De.mb__XL, ml: De.ml__XL },
            LG: { mt: De.mt__LG, mr: De.mr__LG, mb: De.mb__LG, ml: De.ml__LG },
            MDp: { mt: De.mt__MDp, mr: De.mr__MDp, mb: De.mb__MDp, ml: De.ml__MDp },
            MD: { mt: De.mt__MD, mr: De.mr__MD, mb: De.mb__MD, ml: De.ml__MD },
            SMp: { mt: De.mt__SMp, mr: De.mr__SMp, mb: De.mb__SMp, ml: De.ml__SMp },
            SM: { mt: De.mt__SM, mr: De.mr__SM, mb: De.mb__SM, ml: De.ml__SM },
            XS: { mt: De.mt__XS, mr: De.mr__XS, mb: De.mb__XS, ml: De.ml__XS },
          },
          we = (Object.keys(ve), ["mt", "mr", "mb", "ml"]),
          fe = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Se = pe((e) => {
            let u = e.className,
              t = e.width,
              a = e.height,
              o = e.m,
              l = e.mt,
              s = void 0 === l ? o : l,
              _ = e.mr,
              c = void 0 === _ ? o : _,
              m = e.mb,
              d = void 0 === m ? o : m,
              E = e.ml,
              A = void 0 === E ? o : E,
              h = e.column,
              b = e.row,
              C = e.flexDirection,
              F = void 0 === C ? (h ? "column" : b && "row") || void 0 : C,
              p = e.flexStart,
              D = e.center,
              g = e.flexEnd,
              B = e.spaceBetween,
              v = e.spaceAround,
              w = e.justifyContent,
              f =
                void 0 === w
                  ? (p ? "flex-start" : D && "center") ||
                    (g && "flex-end") ||
                    (B && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : w,
              S = e.alignItems,
              x =
                void 0 === S
                  ? (p ? "flex-start" : D && "center") || (g && "flex-end") || void 0
                  : S,
              L = e.alignSelf,
              y = e.wrap,
              P = e.flexWrap,
              M = void 0 === P ? (y ? "wrap" : void 0) : P,
              k = e.grow,
              T = e.shrink,
              N = e.flex,
              R = void 0 === N ? (k || T ? `${k ? 1 : 0} ${T ? 1 : 0} auto` : void 0) : N,
              I = e.style,
              O = e.children,
              H = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, ge);
            const $ = (0, r.useMemo)(() => {
                const e = { mt: s, mr: c, mb: d, ml: A },
                  u = ((e) =>
                    we.reduce((u, t) => {
                      const a = e[t];
                      return a && "number" != typeof a ? u.concat(ve[!0 === a ? "MD" : a][t]) : u;
                    }, []))(e),
                  r = ((e) =>
                    we.reduce((u, t) => {
                      const a = e[t];
                      return ("number" == typeof a && (u[fe[t]] = a + "rem"), u);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, I, r, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    flex: R,
                    alignSelf: L,
                    display: F || x ? "flex" : void 0,
                    flexDirection: F,
                    flexWrap: M,
                    justifyContent: f,
                    alignItems: x,
                  }),
                  computedClassNames: u,
                };
              }, [t, a, s, c, d, A, I, R, L, F, M, f, x]),
              G = $.computedStyle,
              W = $.computedClassNames;
            return n().createElement(
              "div",
              Be({ className: i()(De.base, ...W, u), style: G }, H),
              O,
            );
          });
        var xe = t(280),
          Le = t(3532),
          ye = t.n(Le);
        const Pe = {
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
          Me = [
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
        function ke() {
          return (
            (ke =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ke.apply(this, arguments)
          );
        }
        Object.keys(Ae());
        const Te = Object.keys(ye()),
          Ne = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Re = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Ie = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Oe = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          He =
            (Object.keys(Oe),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Ne,
              "heading-H36": Ne,
              "heading-H28": Re,
              "heading-H24": Re,
              "heading-H24R": Re,
              "heading-H22": Re,
              "heading-H20R": Re,
              "heading-H18": Re,
              "heading-H15": Ie,
              "heading-H14": Ie,
              "paragraph-P24": Re,
              "paragraph-P18": Re,
              "paragraph-P16": Re,
              "paragraph-P14": Ie,
              "paragraph-P12": Ie,
              "paragraph-P10": Ie,
            }),
          $e =
            (Object.keys(He),
            (e) =>
              e
                ? ((e) => Te.includes(e))(e)
                  ? { colorClassName: Pe[e] }
                  : { colorStyle: { color: e } }
                : {}),
          Ge = pe((e) => {
            let u = e.text,
              t = e.variant,
              a = e.className,
              o = e.color,
              l = e.m,
              s = e.mt,
              _ = void 0 === s ? l : s,
              c = e.mr,
              m = void 0 === c ? l : c,
              d = e.mb,
              E = void 0 === d ? l : d,
              A = e.ml,
              h = void 0 === A ? l : A,
              b = e.style,
              C = e.format,
              F = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, Me);
            const p = (0, r.useMemo)(() => {
                const e = $e(o),
                  u = e.colorClassName,
                  t = e.colorStyle,
                  a = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, b, a), colorClassName: u };
              }, [b, o]),
              D = p.computedStyle,
              g = p.colorClassName;
            return n().createElement(
              Se,
              ke(
                {
                  className: i()(Pe.base, t && Pe[t], g, a),
                  style: D,
                  mt: !0 === _ ? He[t || "paragraph-P16"].mt : _,
                  mr: !0 === m ? He[t || "paragraph-P16"].mr : m,
                  mb: !0 === E ? He[t || "paragraph-P16"].mb : E,
                  ml: !0 === h ? He[t || "paragraph-P16"].ml : h,
                },
                F,
              ),
              void 0 !== C ? n().createElement(xe.z, ke({}, C, { text: u })) : u,
            );
          });
        var We = t(6373);
        const Ue = [];
        function ze(e) {
          const u = (0, r.useRef)(e);
          return (
            (0, r.useLayoutEffect)(() => {
              u.current = e;
            }),
            (0, r.useCallback)((...e) => (0, u.current)(...e), Ue)
          );
        }
        var je = t(7902);
        const Xe = (e, u) => e.split(".").reduce((e, u) => e && e[u], u);
        var qe = t(6536);
        const Ve = (e) => e && "ArrayItem" === e.__proto__.constructor.name,
          Ye = (e, u) => (e.length > 0 ? `${e}.${u}` : u),
          Ke = (e) =>
            ((e, u) =>
              e.split(".").reduce((e, t) => {
                const a = Xe(`${e}.${t}`, window);
                return Ve(a) ? u(e, t, a) : `${e}.${t}`;
              }))(e, (e, u) => `${e}.${u}.value`),
          Ze = (e) => {
            const u = ((e) => {
                const u = (0, je.F)(),
                  t = u.caller,
                  a = u.resId,
                  r = window.__feature && window.__feature !== t && t ? `subViews.${t}` : "";
                return { modelPrefix: r, modelPath: Ye(r, e || ""), resId: a };
              })(),
              t = u.modelPrefix,
              a = e.split(".");
            if (a.length > 0) {
              const e = [a[0]];
              return (
                a.reduce((u, a) => {
                  const r = Xe(Ye(t, `${u}.${a}`), window);
                  return Ve(r) ? (e.push(r.id), `${u}.${a}.value`) : (e.push(a), `${u}.${a}`);
                }),
                e.reduce((e, u) => e + "." + u)
              );
            }
            return "";
          },
          Qe = P.Sw.instance;
        let Je;
        !(function (e) {
          ((e.None = "None"), (e.Shallow = "Shallow"), (e.Deep = "Deep"));
        })(Je || (Je = {}));
        const eu = (e = "model", u = Je.Deep) => {
            const t = (0, r.useState)(0),
              a = (t[0], t[1]),
              n = (0, r.useMemo)(() => (0, je.F)(), []),
              o = n.caller,
              i = n.resId,
              l = (0, r.useMemo)(
                () => (window.__feature && window.__feature !== o ? `subViews.${o}.${e}` : e),
                [o, e],
              ),
              s = (0, r.useState)(() =>
                ((e) => {
                  const u = Xe(e, window);
                  for (const e in u) "function" == typeof u[e] && (u[e] = u[e].bind(u));
                  return Ve(u) ? u.value : u;
                })(Ke(l)),
              ),
              _ = s[0],
              c = s[1],
              m = (0, r.useRef)(-1);
            return (
              (0, qe.Z)(() => {
                if (
                  ("boolean" == typeof u &&
                    ((u = u ? Je.Deep : Je.None),
                    console.warn(
                      'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                    )),
                  u !== Je.None)
                ) {
                  const t = (e) => {
                      ((e) => e && "CoherentArrayProxy" === e.__proto__.constructor.name)(e) &&
                      u === Je.Deep
                        ? (e === _ && a((e) => e + 1), c(e))
                        : c(Object.assign([], e));
                    },
                    r = Ze(e);
                  m.current = Qe.addCallback(r, t, i, u === Je.Deep);
                }
              }),
              (0, r.useEffect)(() => {
                if (u !== Je.None)
                  return () => {
                    Qe.removeCallback(m.current, i);
                  };
              }, [i, u]),
              _
            );
          },
          uu = "display",
          tu = "enabled",
          au = "enabled_change";
        var ru = t(3649);
        const nu = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          ou = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const iu = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          lu = (e) =>
            iu
              ? `${e}`
              : (function (e) {
                  let u = "";
                  for (let t = ou.length - 1; t >= 0; t--)
                    for (; e >= ou[t];) ((u += nu[t]), (e -= ou[t]));
                  return u;
                })(e),
          su = {
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
        let _u, cu;
        (!(function (e) {
          ((e.extraSmall = "extraSmall"), (e.medium = "medium"), (e.big = "big"));
        })(_u || (_u = {})),
          (function (e) {
            ((e.colored = "colored"), (e.white = "white"), (e.whiteSpanish = "whiteSpanish"));
          })(cu || (cu = {})));
        const mu = ({
          isElite: e,
          vehicleName: u,
          vehicleShortName: t,
          vehicleType: a,
          vehicleLvl: r,
          tags: o,
          isPremiumIGR: l,
          size: s = _u.extraSmall,
          type: _ = cu.colored,
          className: c,
          classNames: m,
          isShortName: d = !1,
        }) => {
          const E = `${(0, ru.BN)(a)}${e ? "_elite" : ""}`,
            A = R.images.gui.maps.icons.vehicleTypes.big.$dyn(E);
          return n().createElement(
            "div",
            {
              className: i()(
                su.base,
                su[`base__size${(0, ru.e)(s)}`],
                su[`base__type${(0, ru.e)(_)}`],
                o && I(o, (e) => su[`base__tag${(0, ru.e)(e)}`]),
                c,
              ),
            },
            n().createElement(
              "div",
              { className: i()(su.level, null == m ? void 0 : m.level) },
              lu(r),
            ),
            n().createElement("div", {
              className: i()(su.type, e && su.type__elite, null == m ? void 0 : m.typeIcon),
              style: { backgroundImage: `url(${A})` },
            }),
            l && n().createElement("div", { className: su.premiumIGR }),
            n().createElement(
              "div",
              { className: i()(su.name, null == m ? void 0 : m.name) },
              d ? t : u,
            ),
          );
        };
        let du, Eu, Au, hu, bu, Cu, Fu, pu, Du;
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
        })(du || (du = {})),
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
          })(Eu || (Eu = {})),
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
          })(Au || (Au = {})),
          (function (e) {
            ((e.MULTI = "multi"),
              (e.CURRENCY = "currency"),
              (e.PREMIUM_PLUS = "premium_plus"),
              (e.NUMBER = "number"),
              (e.STRING = "string"));
          })(hu || (hu = {})),
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
          })(bu || (bu = {})),
          (function (e) {
            e.BATTLE_BOOSTER = "battleBooster";
          })(Cu || (Cu = {})),
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
          })(Fu || (Fu = {})),
          (function (e) {
            ((e.Small = "400x300"), (e.Big = "600x450"));
          })(pu || (pu = {})),
          (function (e) {
            e.ProgressionStyle = "progressionStyle";
          })(Du || (Du = {})));
        t(2372);
        (du.Items,
          du.Equipment,
          du.Xp,
          du.XpFactor,
          du.Blueprints,
          du.BlueprintsAny,
          du.Goodies,
          du.Berths,
          du.Slots,
          du.Tokens,
          du.CrewSkins,
          du.CrewBooks,
          du.Customizations,
          du.CreditsFactor,
          du.TankmenXp,
          du.TankmenXpFactor,
          du.FreeXpFactor,
          du.BattleToken,
          du.PremiumUniversal,
          du.NaturalCover,
          du.BpCoin,
          du.BattlePassSelectToken,
          du.BattlaPassFinalAchievement,
          du.BattleBadge,
          du.BonusX5,
          du.CrewBonusX3,
          du.NewYearFillers,
          du.NewYearInvoice,
          du.EpicSelectToken,
          du.Comp7TokenWeeklyReward,
          du.Comp7TokenCouponReward,
          du.BattleBoosterGift,
          du.CosmicLootboxCommon,
          du.CosmicLootboxSilver,
          du.SelectableBonus,
          du.PostStamp,
          du.PremiumPlusUniversal,
          du.GoldenTicket,
          du.RewardsSlots,
          du.WtStamp,
          du.WtTicket,
          du.WtMainPrizeDiscount,
          du.WtHunter,
          du.WtHunterCollection,
          du.Gold,
          du.Credits,
          du.Crystal,
          du.FreeXp,
          du.BattlePassPoints,
          du.PremiumPlus,
          du.Premium);
        let gu;
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
        })(gu || (gu = {}));
        var Bu = t(8546);
        const vu = "bp_highlight",
          wu = (e) => {
            const u = G[e];
            return (u || console.warn("Unknown FinalReward key: ", e), u);
          },
          fu = "Delimiter_base_bd",
          Su = "Delimiter_line_46",
          xu = "Delimiter_base__active_28",
          Lu = "Delimiter_line__left_0a",
          yu = "Delimiter_line__right_6a",
          Pu = ({ isActive: e }) =>
            n().createElement(
              "div",
              { className: i()(fu, e && xu) },
              n().createElement("div", { className: i()(Su, Lu) }),
              n().createElement("div", { className: Su }),
              n().createElement("div", { className: i()(Su, yu) }),
            ),
          Mu = {
            base: "Chapter_base_f0",
            base__small: "Chapter_base__small_32",
            divider: "Chapter_divider_a7",
            bg: "Chapter_bg_2e",
            base__disabled: "Chapter_base__disabled_6d",
            bgInner: "Chapter_bgInner_83",
            disabled: "Chapter_disabled_7a",
            commanderImg: "Chapter_commanderImg_90",
            base__paused: "Chapter_base__paused_ff",
            base__notStarted: "Chapter_base__notStarted_9b",
            base__completed: "Chapter_base__completed_88",
            base__medium: "Chapter_base__medium_e2",
            bgHover: "Chapter_bgHover_ac",
            border: "Chapter_border_5c",
            frame: "Chapter_frame_58",
            frameLeft: "Chapter_frameLeft_e7",
            frameRight: "Chapter_frameRight_fa",
            frameLeft__yellow: "Chapter_frameLeft__yellow_27",
            frameLeft__red: "Chapter_frameLeft__red_08",
            frameLeft__blue: "Chapter_frameLeft__blue_76",
            frameLeft__green: "Chapter_frameLeft__green_52",
            frameRight__yellow: "Chapter_frameRight__yellow_64",
            frameRight__red: "Chapter_frameRight__red_1a",
            frameRight__blue: "Chapter_frameRight__blue_ae",
            frameRight__green: "Chapter_frameRight__green_d0",
            vehicleImg: "Chapter_vehicleImg_b1",
            content: "Chapter_content_61",
            buttonBlockHolder: "Chapter_buttonBlockHolder_db",
            disabledBlock: "Chapter_disabledBlock_9d",
            completedBlock: "Chapter_completedBlock_f9",
            pausedBlock: "Chapter_pausedBlock_a7",
            completedIcon: "Chapter_completedIcon_f2",
            disabledIcon: "Chapter_disabledIcon_f3",
            pausedIcon: "Chapter_pausedIcon_02",
            statusText: "Chapter_statusText_19",
            statusText__completed: "Chapter_statusText__completed_9c",
            statusText__disabled: "Chapter_statusText__disabled_4d",
            statusText__paused: "Chapter_statusText__paused_16",
            statusText__inactive: "Chapter_statusText__inactive_d0",
            hintBody: "Chapter_hintBody_de",
            buttonWrapper: "Chapter_buttonWrapper_de",
            buttonBlockHolder__hidden: "Chapter_buttonBlockHolder__hidden_e5",
            delimiter: "Chapter_delimiter_b4",
            title: "Chapter_title_57",
            base__active: "Chapter_base__active_e5",
            vehicleStyle: "Chapter_vehicleStyle_85",
            preview: "Chapter_preview_1d",
            previewWrapper: "Chapter_previewWrapper_74",
            styleTitle: "Chapter_styleTitle_0d",
            vehicleTitle: "Chapter_vehicleTitle_10",
            vehicleInHangar: "Chapter_vehicleInHangar_61",
            styleHolder: "Chapter_styleHolder_55",
            inactiveText: "Chapter_inactiveText_b6",
            levelBlock: "Chapter_levelBlock_f3",
            level: "Chapter_level_e1",
            levelText: "Chapter_levelText_fc",
            fadeOut: "Chapter_fadeOut_82",
            fadeIn: "Chapter_fadeIn_f7",
            fadeInWithScale: "Chapter_fadeInWithScale_4c",
            slideUp: "Chapter_slideUp_71",
            scale: "Chapter_scale_96",
            rotate: "Chapter_rotate_78",
          };
        var ku = t(122);
        const Tu = "VehicleIcon_base_5e",
          Nu = "VehicleIcon_vehicleIcon_90",
          Ru = "VehicleIcon_vehicleActiveIcon_e0",
          Iu = "VehicleIcon_vehicleActiveIcon__visible_34",
          Ou = "VehicleIcon_vehicleActiveIcon__fadeInAnimated_e9",
          Hu = "VehicleIcon_vehicleActiveIcon__fadeOutAnimated_49",
          $u = (0, r.memo)(({ chapterID: e, isActive: u }) => {
            const t = (0, r.useState)(!1),
              a = t[0],
              o = t[1],
              l = (0, r.useState)(!1),
              s = l[0],
              c = l[1],
              m = (0, r.useState)(!1),
              d = m[0],
              E = m[1],
              A = (0, _.GS)().mediaSize,
              h = (0, $.jz)(A);
            return (
              (0, r.useEffect)(
                () =>
                  u
                    ? (c(!0),
                      (0, ku.F)(() => {
                        (c(!1), o(!0));
                      }, 200))
                    : (E(!0),
                      c(!1),
                      (0, ku.F)(() => {
                        (E(!1), o(!1));
                      }, 200)),
                [u],
              ),
              n().createElement(
                "div",
                { className: Tu },
                n().createElement("div", { className: Nu, style: (0, $.OH)(e, h) }),
                n().createElement("div", {
                  className: i()(Ru, a && Iu, s && Ou, d && Hu),
                  style: (0, $.wq)(e, h),
                }),
              )
            );
          });
        function Gu() {
          return (
            (Gu =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Gu.apply(this, arguments)
          );
        }
        const Wu = R.strings.battle_pass,
          Uu = (0, H.Pi)(
            ({
              chapterID: e,
              hasActive: u,
              progression: t,
              hasTrigger: a = !1,
              chapterSize: o = j.Medium,
            }) => {
              const l = (0, r.useState)(!1),
                s = l[0],
                c = l[1],
                m = te(),
                d = m.model,
                E = m.controls,
                A = (0, _.GS)().mediaSize,
                h = d.computes.hasMarathon(),
                b = d.computes.getChapterById(e),
                C = d.computes.getChapterColor(e);
              if (!b) return null;
              const F = b.chapterState,
                p = b.styleName,
                g = b.tankman,
                B = b.isVehicleInHangar,
                v = b.vehicleInfo,
                w = b.finalReward,
                S = b.chapterType,
                L = t.level,
                y = i()(Mu.base, Mu[`base__${F}`], Mu[`base__${o}`]),
                P = F === f.Completed,
                M = F === f.Disabled,
                k = F === f.Active,
                T = F === f.Paused,
                N = S === W.Marathon,
                R = A <= _.cJ.Small ? oe.small : oe.medium,
                I = A < _.cJ.Medium ? me.SMALL : me.NORMAL,
                O = (0, $.jz)(A),
                H = wu(w) === G.style || wu(w) === G.vehicle,
                U = !P && !M && (L > 1 || (k && L > 0)),
                z = u,
                X = !k && !M && !P,
                q = u && X && !T,
                V = T && u,
                Y = Wu.chapter.fullNameUppercased.$num(e) || `chapter/fullNameUppercased/${e}`,
                K = Wu.chapter.fullName.quoted.$num(e) || `chapter/fullName/quoted/${e}`,
                Z = (0, $.s0)(e, h, k || P, O),
                Q = ((e, u) => {
                  const t = eu("tutorialModel.effects.items").filter((t) => {
                    if (!t) return !1;
                    const a = t.value,
                      r = window.__featureId.toString();
                    return a.componentId === e && a.type === u && a.viewId === r;
                  });
                  if (0 === t.length) return null;
                  const a = Object.assign({}, t[0].value);
                  return {
                    effect: a,
                    completeEffect: () => {
                      (tutorialModel.onEffectCompleted({
                        componentId: e,
                        viewId: window.__featureId.toFixed(0),
                        effectType: u,
                        effectBuilder: a.builder,
                      }),
                        u === uu && window.tutorialApi && window.tutorialApi.updateComponents());
                    },
                  };
                })("BattlePassChapterChoice", tu),
                J = (0, r.useCallback)(
                  (u) => {
                    (E.openPreview(e), u.stopPropagation());
                  },
                  [e, E],
                ),
                ee = (0, r.useCallback)(
                  (u) => {
                    (E.activateChapter(e), u.stopPropagation());
                  },
                  [e, E],
                ),
                ue = (0, r.useCallback)(() => {
                  (D.$.playClick(), E.selectChapter(e));
                }, [e, E]),
                ae = ze(() => {
                  ((0, D.G)(vu), c(!0));
                }),
                re = (0, r.useCallback)(
                  (e) => {
                    switch (e) {
                      case G.style:
                        return n().createElement(
                          "div",
                          { className: Mu.vehicleStyle },
                          n().createElement(
                            "div",
                            { className: Mu.styleTitle },
                            N
                              ? n().createElement(Ge, {
                                  text: Wu.chapterChoice.extraChapter.reward(),
                                })
                              : n().createElement(Ge, {
                                  text: Wu.chapterChoice.stylePreview.name(),
                                  format: { binding: { styleName: p } },
                                }),
                          ),
                          n().createElement(
                            "div",
                            { className: Mu.vehicleTitle },
                            n().createElement(Ge, {
                              text: Wu.chapterChoice.stylePreview.forLabel.$dyn(S),
                              format: {
                                binding: {
                                  vehicleName: n().createElement(mu, Gu({}, v, { type: cu.white })),
                                },
                              },
                            }),
                            B && n().createElement("div", { className: Mu.vehicleInHangar }),
                          ),
                        );
                      case G.tankman:
                        return n().createElement(
                          "div",
                          { className: Mu.vehicleStyle },
                          n().createElement(
                            "div",
                            { className: Mu.styleTitle },
                            n().createElement(Ge, {
                              text: Wu.chapterChoice.tankman.title(),
                              format: { binding: { styleName: p } },
                            }),
                          ),
                          n().createElement(
                            "div",
                            { className: Mu.vehicleTitle },
                            n().createElement(Ge, { text: g }),
                          ),
                        );
                      case G.vehicle:
                        return n().createElement(
                          "div",
                          { className: Mu.vehicleStyle },
                          n().createElement(
                            "div",
                            { className: Mu.styleTitle },
                            n().createElement(Ge, { text: Wu.chapterChoice.extraChapter.reward() }),
                          ),
                          n().createElement(
                            "div",
                            { className: Mu.vehicleTitle },
                            n().createElement(Ge, {
                              text: Wu.chapterChoice.stylePreview.forLabel.$dyn(S),
                              format: {
                                binding: {
                                  vehicleName: n().createElement(mu, Gu({}, v, { type: cu.white })),
                                },
                              },
                            }),
                            B && n().createElement("div", { className: Mu.vehicleInHangar }),
                          ),
                        );
                    }
                  },
                  [S, N, B, p, g, v],
                );
              (0, r.useEffect)(
                () =>
                  x(() => {
                    null !== Q && a && Q.completeEffect();
                  }),
                [Q, a],
              );
              const ie = ((e, u) => {
                const t = eu("tutorialModel.triggers.items").filter((t) => {
                  if (!t) return !1;
                  const a = t.value,
                    r = a.triggers.filter((e) => e.value === u);
                  return a.componentId === e && r.length > 0;
                });
                return 0 === t.length
                  ? null
                  : window.tutorialModel.foundComponents.items.some(
                        (u) => u.value.componentId === e,
                      )
                    ? {
                        trigger: t[0].value,
                        runTrigger: (t) => {
                          window.tutorialModel.onTriggerActivated({
                            componentId: e,
                            triggerType: u,
                            state: t,
                          });
                        },
                      }
                    : null;
              })("BattlePassChapterChoice", au);
              return (
                (0, r.useEffect)(() => {
                  ie && a && ie.runTrigger(!0);
                }, [a, ie]),
                n().createElement(
                  We.i,
                  {
                    header: Wu.chapterChoice.tooltip.disabledChapter.header(),
                    body: (0, ru.uF)(Wu.chapterChoice.tooltip.disabledChapter.body(), {
                      chapterName: K,
                    }),
                    isEnabled: M,
                  },
                  n().createElement(
                    "div",
                    { className: y, onMouseEnter: ae, onClick: ue, onMouseLeave: () => c(!1) },
                    n().createElement(
                      "div",
                      { className: Mu.bg, style: Z },
                      n().createElement("div", {
                        className: Mu.bgInner,
                        style: (0, $.s0)(e, h, !0, O),
                      }),
                    ),
                    n().createElement("div", { className: Mu.divider }),
                    n().createElement(
                      "div",
                      { className: Mu.commanderImg, style: (0, $.TZ)(e, O) },
                      n().createElement(
                        "div",
                        { className: Mu.vehicleImg },
                        n().createElement($u, { chapterID: e, isActive: k || s }),
                      ),
                      H &&
                        n().createElement(
                          "div",
                          { className: Mu.preview },
                          n().createElement(
                            "div",
                            { className: Mu.previewWrapper },
                            n().createElement(de, { onClick: J, size: I }),
                          ),
                        ),
                      n().createElement("div", { className: Mu.bgHover }),
                    ),
                    k &&
                      n().createElement(
                        "div",
                        { className: Mu.frame },
                        n().createElement("div", {
                          className: i()(Mu.frameLeft, C && Mu[`frameLeft__${C}`]),
                        }),
                        n().createElement("div", {
                          className: i()(Mu.frameRight, C && Mu[`frameRight__${C}`]),
                        }),
                      ),
                    n().createElement("div", { className: Mu.disabled }),
                    n().createElement(
                      "div",
                      { className: Mu.content },
                      n().createElement("div", { className: Mu.styleHolder }, re(wu(w))),
                      n().createElement(
                        "div",
                        { className: Mu.delimiter },
                        n().createElement(Pu, { isActive: k }),
                      ),
                      n().createElement(Ge, { text: Y, className: Mu.title }),
                      n().createElement(
                        "div",
                        { className: i()(Mu.buttonBlockHolder, z && Mu.buttonBlockHolder__hidden) },
                        X &&
                          n().createElement(
                            "div",
                            { className: Mu.buttonWrapper },
                            a &&
                              n().createElement("div", {
                                className: Mu.hintBody,
                                id: "bp-chapter-choice",
                              }),
                            n().createElement(
                              We.i,
                              { body: Wu.tooltips.footerBuyBtn.activateChapter.descr() },
                              n().createElement(
                                le,
                                { type: ne.primary, size: R, onClick: ee },
                                n().createElement(Ge, { text: Wu.chapter.activateChapter() }),
                              ),
                            ),
                          ),
                        V &&
                          n().createElement(
                            "div",
                            { className: Mu.pausedBlock },
                            n().createElement("div", { className: Mu.pausedIcon }),
                            n().createElement(Ge, {
                              text: Wu.chapterChoice.chapterPaused(),
                              className: i()(Mu.statusText, Mu.statusText__paused),
                            }),
                          ),
                        q &&
                          n().createElement(
                            "div",
                            { className: Mu.pausedBlock },
                            n().createElement(Ge, {
                              text: Wu.chapterChoice.chapterInactive(),
                              className: i()(Mu.statusText, Mu.statusText__inactive),
                            }),
                          ),
                      ),
                      U &&
                        n().createElement(
                          "div",
                          { className: Mu.levelBlock },
                          n().createElement(Ge, {
                            text: k
                              ? Wu.chapter.currentStep.active()
                              : Wu.chapter.currentStep.colon(),
                            className: Mu.levelText,
                          }),
                          n().createElement(Ge, { text: String(L), className: Mu.level }),
                        ),
                      P &&
                        n().createElement(
                          "div",
                          { className: Mu.completedBlock },
                          n().createElement("div", { className: Mu.completedIcon }),
                          n().createElement(Ge, {
                            text: Wu.chapterChoice.chapterCompleted(),
                            className: i()(Mu.statusText, Mu.statusText__completed),
                          }),
                        ),
                      M &&
                        n().createElement(
                          "div",
                          { className: Mu.disabledBlock },
                          n().createElement("div", { className: Mu.disabledIcon }),
                          n().createElement(Ge, {
                            text: Wu.chapterChoice.chapterDisabled(),
                            className: i()(Mu.statusText, Mu.statusText__disabled),
                          }),
                        ),
                    ),
                  ),
                )
              );
            },
          );
        var zu = t(2269),
          ju = t(7030),
          Xu = t(9830);
        const qu = "Shield_base_ec",
          Vu = "Shield_flag_a2",
          Yu = "Shield_flag__isChapterChosen_81",
          Ku = "Shield_flag__medium_78",
          Zu = "Shield_emblem_59",
          Qu = "Shield_chapterLogoIcon_4b",
          Ju = (0, H.Pi)(({ size: e, chapterID: u = 0, progression: t }) => {
            const a = te().model.computes.getChapterById(u);
            if (!a) return null;
            const r = a.isBought,
              o = a.chapterState,
              l = a.chapterType,
              s = o === f.Completed ? Bu.Bq.Completed : r ? Bu.Bq.Bought : Bu.Bq.Free,
              _ = o === f.Active,
              c = ((e) => void 0 !== e.from && (e.level > 1 || e.from > 0))(t),
              m = c || (o !== f.NotStarted && o !== f.Disabled),
              d = m && s !== Bu.Bq.Completed;
            return n().createElement(
              "div",
              { className: qu },
              n().createElement("div", {
                className: i()(Vu, e === Bu.$u.Medium && Ku, d && Yu),
                style: (0, $.fW)(u, e),
              }),
              n().createElement(
                "div",
                { className: Zu },
                n().createElement(Xu.G, {
                  progression: t,
                  size: e,
                  chapterID: u,
                  battlePassState: s,
                  hasBattlePass: r,
                  hasBeenActive: m,
                  isChapterSelection: !0,
                  isOpen: d,
                  isChapterChosen: _,
                  showProgressBar: _,
                  chapterType: l,
                }),
                d && n().createElement("div", { className: Qu, style: (0, $.cs)(u, r, e) }),
              ),
            );
          }),
          et = "ChapterCompleted_base_55",
          ut = "ChapterCompleted_effect_1e",
          tt = "ChapterCompleted_shine_2f",
          at = "ChapterCompleted_shield_af",
          rt = "ChapterCompleted_title_1a",
          nt = "ChapterCompleted_boughtGlow_56",
          ot = "ChapterCompleted_bought_b1",
          it = "ChapterCompleted_button_33",
          lt = "ChapterCompleted_buttonWrapper_04",
          st = R.strings.battle_pass,
          _t = (0, H.Pi)(({ chapterId: e, progression: u }) => {
            const t = (0, r.useState)(!1),
              a = t[0],
              o = t[1],
              i = te(),
              l = i.model,
              s = i.controls,
              c = (0, ju.useSpring)({
                from: { transform: "rotate(0deg)" },
                to: { transform: "rotate(360deg)" },
                reset: !0,
                pause: !a,
                config: { duration: 6e4 },
              }),
              m = (0, _.GS)().mediaSize,
              d = m <= _.cJ.Small ? Bu.$u.Small : Bu.$u.Medium,
              E = m <= _.cJ.Small ? Bu.$u.Small : Bu.$u.Medium,
              A = ze(() => {
                ((0, D.G)("bp_highlight_02"), o(!0));
              }),
              h = ze(() => {
                o(!1);
              }),
              b = l.computes.getChapterById(e);
            if (!b) return null;
            const C = st.chapter.fullNameUppercased.$num(e);
            return n().createElement(
              "div",
              { className: et },
              n().createElement(
                "div",
                {
                  className: ut,
                  onClick: () => {
                    ((0, D.G)("play"), s.selectChapter(e));
                  },
                  onMouseEnter: A,
                  onMouseOut: h,
                },
                n().createElement(ju.animated.div, { className: tt, style: c }),
                n().createElement(
                  "div",
                  { className: at },
                  n().createElement(Ju, { size: E, chapterID: e, progression: u }),
                ),
              ),
              n().createElement("div", { className: rt }, C),
              b.isBought
                ? n().createElement(
                    We.i,
                    { body: st.chapterChoice.chapterBought.tooltip() },
                    n().createElement(
                      "div",
                      { className: nt },
                      n().createElement("div", { className: ot }),
                    ),
                  )
                : n().createElement(
                    "div",
                    { className: lt },
                    n().createElement(
                      "div",
                      { className: it },
                      n().createElement(
                        le,
                        { onClick: () => s.buyChapter(e), type: ne.main, size: d },
                        st.chapterChoice.buy(),
                      ),
                    ),
                  ),
            );
          }),
          ct = "Header_base_71",
          mt = "Header_title_af",
          dt = "Header_description_cc",
          Et = "Header_freePoints_05",
          At = "Header_freePointsInfo_f3",
          ht = "Header_freePointsCount_a8",
          bt = "Header_freePointsIcon_be",
          Ct = "Header_lightRed_4a",
          Ft = R.strings.battle_pass.chapterChoice.freePoints,
          pt = (0, H.Pi)(({ title: e, description: u, hasActive: t }) => {
            const a = te().model,
              r = a.root.get().freePoints,
              o = a.computes.hasMarathon(),
              i = a.computes.isCompleted(),
              l = !t && !o && !i && r > 0;
            return n().createElement(
              "div",
              { className: ct },
              n().createElement("div", { className: Ct }),
              n().createElement(Ge, { className: mt, text: e }),
              u &&
                n().createElement(
                  "div",
                  { className: dt },
                  l
                    ? n().createElement(
                        "div",
                        { className: Et },
                        Ft.description(),
                        n().createElement(
                          We.i,
                          { header: Ft.tooltip.title(), body: Ft.tooltip.description() },
                          n().createElement(
                            "div",
                            { className: At },
                            n().createElement(Ge, { className: ht, text: String(r) }),
                            n().createElement("span", { className: bt }),
                          ),
                        ),
                      )
                    : n().createElement(Ge, { text: u }),
                ),
            );
          }),
          Dt = "ChaptersCompleted_base_6f",
          gt = "ChaptersCompleted_chapters_8d",
          Bt = "ChaptersCompleted_header_08",
          vt = "ChaptersCompleted_awards_2b";
        function wt() {
          return (
            (wt =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            wt.apply(this, arguments)
          );
        }
        const ft = R.strings.battle_pass,
          St = (0, H.Pi)(() => {
            const e = te(),
              u = e.model,
              t = e.controls,
              a = u.root.get(),
              r = a.notChosenRewardCount,
              o = a.bpbitCount,
              i = a.bpcoinCount,
              l = a.isBattlePassCompleted,
              s = a.isChooseRewardsEnabled,
              _ = a.isBpCoinShopEntryPointActive,
              c = a.isBpPointsShopEntryPointActive,
              m = a.isSingleChapter,
              d = u.collectionEntryPoint.get(),
              E = d.collectionItemCount,
              A = d.newCollectionItemCount,
              h = d.maxCollectionItemCount,
              b = d.isFirstEnter,
              C = d.isCollectionsEnabled,
              F = u.chapters.get(),
              p = t.openGoodsForBpCoins,
              D = t.takeRewards,
              g = t.openGoodsForBpPoints,
              B = t.openCollection;
            return n().createElement(
              "div",
              { className: Dt },
              n().createElement(
                "div",
                { className: Bt },
                n().createElement(pt, {
                  title: m
                    ? ft.chapterChoice.allChaptersCompleted.titleSingle()
                    : ft.chapterChoice.allChaptersCompleted.title(),
                  description: c ? ft.chapterChoice.allChaptersCompleted.description() : void 0,
                }),
              ),
              n().createElement(
                "div",
                { className: gt },
                I(F, (e, t) =>
                  n().createElement(_t, {
                    key: t,
                    chapterId: e.chapterID,
                    progression: z(u.computes.getChapterById(e.chapterID)),
                  }),
                ),
              ),
              n().createElement(
                "div",
                { className: vt },
                n().createElement(
                  U.Z,
                  wt(
                    {},
                    {
                      pointsCount: o,
                      notChosenRewardCount: r,
                      coinCount: i,
                      collectionItemCount: E,
                      maxCollectionItemCount: h,
                      newCollectionItemCount: A,
                      isBPFirstEnter: b,
                      isCollectionsEnabled: C,
                      isAwardDisabled: !s,
                      isPointsLocked: !l,
                      onPointsClick: g,
                      onCoinClick: p,
                      onTakeRewardsClick: D,
                      onCollectionClick: B,
                      hasMarathon: u.computes.hasChapter(W.Marathon),
                      isBpCoinShopEntryPointActive: _,
                      isBpPointsShopEntryPointActive: c,
                    },
                    { size: zu.W.Big },
                  ),
                ),
              ),
            );
          }),
          xt = R.strings.battle_pass,
          Lt = (0, H.Pi)(() => {
            var e;
            const u = te(),
              t = u.model,
              a = u.controls,
              o = t.root.get(),
              l = o.notChosenRewardCount,
              s = o.bpbitCount,
              c = o.bpcoinCount,
              m = o.isBattlePassCompleted,
              d = o.isChooseRewardsEnabled,
              E = o.isBpCoinShopEntryPointActive,
              A = o.isBpPointsShopEntryPointActive,
              h = a.openCollection,
              b = a.openAbout,
              C = a.openPointsInfo,
              F = a.openGoodsForBpPoints,
              p = a.openGoodsForBpCoins,
              D = a.onViewLoaded,
              g = a.takeRewards,
              B = a.close,
              v = t.computes.getChapters(),
              S = t.computes.hasActive(),
              P = t.computes.getTriggerChapterId(),
              M = ((e) => (e < 3 ? j.Large : e > 4 ? j.Small : j.Medium))(v.length),
              T = t.collectionEntryPoint.get(),
              N = T.collectionItemCount,
              R = T.newCollectionItemCount,
              O = T.maxCollectionItemCount,
              H = T.isFirstEnter,
              G = T.isCollectionsEnabled,
              X = (0, r.useState)(!1),
              q = X[0],
              V = X[1],
              Y = (0, _.GS)().mediaSize,
              K = (0, $.jz)(Y);
            (!(function ({
              key: e = y.n.ESCAPE,
              callback: u = () => L.O.view.sendEvent.close(),
              preventPropagation: t = !0,
            } = {}) {
              k(e, u, t);
            })({ callback: B, preventPropagation: !1 }),
              (0, r.useEffect)(
                () =>
                  x(() => {
                    q || (D(), V(!0));
                  }),
                [q, D],
              ));
            const Z = i()(ae.chapters, ae[`chapters__${M}`]),
              Q = S ? xt.chapterChoice.activeTitle() : xt.chapterChoice.title(),
              J = S
                ? xt.chapterChoice.description.hasActive()
                : xt.chapterChoice.description.noActiveHasMarathon(),
              ee = t.computes.isCompleted(),
              ue = null != (e = t.computes.hasChapter(W.Marathon)) && e,
              re = i()(ae.base, ue && ae.base__hasMarathon),
              ne = v[0].chapterState === f.Completed,
              oe = v[v.length - 1].chapterState === f.Completed;
            return n().createElement(
              "div",
              { className: re },
              n().createElement("div", { className: ae.background }),
              ee
                ? n().createElement(
                    n().Fragment,
                    null,
                    n().createElement("div", { className: ae.backgroundBlur }),
                    n().createElement(St, null),
                  )
                : n().createElement(
                    n().Fragment,
                    null,
                    n().createElement(
                      "div",
                      { className: Z },
                      n().createElement(
                        "div",
                        { className: ae.chapterHolder },
                        n().createElement("div", {
                          style: (0, $.NF)(ue, ne, "left", K),
                          className: ae.chapterLeft,
                        }),
                        n().createElement("div", { className: ae.divider }),
                      ),
                      I(v, ({ chapterID: e }, u) =>
                        n().createElement(
                          n().Fragment,
                          { key: u },
                          n().createElement(Uu, {
                            chapterID: e,
                            hasActive: S,
                            chapterSize: M,
                            hasTrigger: P === e,
                            progression: z(t.computes.getChapterById(e)),
                          }),
                        ),
                      ),
                      n().createElement(
                        "div",
                        { className: ae.chapterHolder },
                        n().createElement("div", {
                          style: (0, $.NF)(ue, oe, "right", K),
                          className: ae.chapterRight,
                        }),
                      ),
                    ),
                    n().createElement(
                      "div",
                      { className: ae.infoButtons },
                      n().createElement(w, {
                        caption: xt.intro.aboutButton(),
                        type: "info",
                        onClick: b,
                      }),
                      n().createElement(w, {
                        caption: xt.howToEarnPoints.title(),
                        type: "info",
                        onClick: C,
                      }),
                    ),
                    n().createElement(
                      "div",
                      { className: ae.header },
                      n().createElement(pt, { title: Q, description: J, hasActive: S }),
                    ),
                    n().createElement(
                      "div",
                      { className: ae.flags },
                      n().createElement(U.Z, {
                        pointsCount: s,
                        notChosenRewardCount: l,
                        coinCount: c,
                        collectionItemCount: N,
                        maxCollectionItemCount: O,
                        newCollectionItemCount: R,
                        isBPFirstEnter: H,
                        isCollectionsEnabled: G,
                        isAwardDisabled: !d,
                        isPointsLocked: !m,
                        onPointsClick: F,
                        onCoinClick: p,
                        onTakeRewardsClick: g,
                        onCollectionClick: h,
                        hasMarathon: ue,
                        hasResource: t.computes.hasChapter(W.Resource),
                        isBpCoinShopEntryPointActive: E,
                        isBpPointsShopEntryPointActive: A,
                      }),
                    ),
                  ),
            );
          });
        engine.whenReady.then(() => {
          p().render(
            n().createElement(C, null, n().createElement(ue, null, n().createElement(Lt, null))),
            document.getElementById("root"),
          );
        });
      },
      903: (e, u, t) => {
        "use strict";
        t.d(u, {
          FL: () => l,
          NF: () => d,
          OH: () => E,
          TZ: () => c,
          cs: () => i,
          fW: () => _,
          jz: () => s,
          s0: () => m,
          wD: () => o,
          wq: () => A,
        });
        var a = t(5415),
          r = t(8546);
        const n = (e) => {
            switch (e) {
              case r.$u.Micro:
                return "s";
              case r.$u.Small:
                return "m";
              default:
                return "l";
            }
          },
          o = (e, u, t = "") => {
            const a = t.length > 0 ? `_${t}` : t,
              r = e.$dyn(`c_${u}${a}`),
              n = e.$dyn(`common${a}`);
            return r || n;
          },
          i = (e, u, t) => {
            const a = R.images.gui.maps.icons.battlePass.logo.chapterIcons,
              r = u ? "BP" : "",
              i = `${n(t)}${r}`;
            return { backgroundImage: `url(${o(a, e, i)})` };
          },
          l = (e, u, t, a) => {
            const r = R.images.gui.maps.icons.battlePass.logo,
              n = o(r, e, `emblem${a ? "_BP" : ""}${t ? "_open" : ""}${u}`);
            return n ? { backgroundImage: `url(${n})` } : void 0;
          },
          s = (e) => {
            switch (e) {
              case a.cJ.ExtraSmall:
              case a.cJ.Small:
                return r.$u.Micro;
              case a.cJ.Medium:
                return r.$u.Small;
              default:
                return r.$u.Medium;
            }
          },
          _ = (e, u) => {
            const t = R.images.gui.maps.icons.battlePass.logo.flag,
              a = n(u);
            return { backgroundImage: `url(${o(t, e, a)})` };
          },
          c = (e, u = r.$u.Medium) => {
            const t = R.images.gui.maps.icons.battlePass.chapter_choice.commander,
              a = n(u);
            return { backgroundImage: `url(${o(t, e, a)})` };
          },
          m = (e, u, t = !1, a = r.$u.Medium) => {
            const i = n(a),
              l = u
                ? R.images.gui.maps.icons.battlePass.chapter_choice.marathon
                : R.images.gui.maps.icons.battlePass.chapter_choice.chapter;
            return { backgroundImage: `url(${o(l.$dyn(i), e, t ? "active" : "")})` };
          },
          d = (e, u = !1, t, a = r.$u.Medium) => ({
            backgroundImage: `url(${(e ? R.images.gui.maps.icons.battlePass.chapter_choice.marathon : R.images.gui.maps.icons.battlePass.chapter_choice.chapter).$dyn(n(a)).$dyn(`${t}_edge${u ? "_active" : ""}`)})`,
          }),
          E = (e, u = r.$u.Medium) => {
            const t = R.images.gui.maps.icons.battlePass.chapter_choice.tank.default,
              a = n(u);
            return { backgroundImage: `url(${o(t, e, a)})` };
          },
          A = (e, u) => {
            const t = R.images.gui.maps.icons.battlePass.chapter_choice.tank.active,
              a = n(u);
            return { backgroundImage: `url(${o(t, e, a)})` };
          };
      },
      2269: (e, u, t) => {
        "use strict";
        let a, r;
        (t.d(u, { W: () => r, w: () => a }),
          (function (e) {
            ((e.Award = "Award"),
              (e.Coin = "Coin"),
              (e.Point = "Point"),
              (e.Collection = "Collection"));
          })(a || (a = {})),
          (function (e) {
            ((e.Small = "small"), (e.Big = "big"));
          })(r || (r = {})));
      },
      6895: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => p });
        var a = t(6483),
          r = t.n(a),
          n = t(6179),
          o = t.n(n);
        const i = {
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
          l = ["size", "value", "isEmpty", "fadeInAnimation", "hide", "maximumNumber", "className"];
        function s() {
          return (
            (s =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            s.apply(this, arguments)
          );
        }
        const _ = (e) => {
          let u = e.size,
            t = e.value,
            a = e.isEmpty,
            n = e.fadeInAnimation,
            _ = e.hide,
            c = e.maximumNumber,
            m = e.className,
            d = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, l);
          const E = a ? null : t,
            A = "string" == typeof E;
          if ((E && !A && E < 0) || 0 === E) return null;
          const h = E && !A && E > c,
            b = r()(
              i.base,
              i[`base__${u}`],
              n && i.base__animated,
              _ && i.base__hidden,
              !E && i.base__pattern,
              a && i.base__empty,
              m,
            );
          return o().createElement(
            "div",
            s({ className: b }, d),
            o().createElement("div", { className: i.bg }),
            o().createElement("div", { className: i.pattern }),
            o().createElement(
              "div",
              { className: r()(i.value, A && i.value__text) },
              h ? c : E,
              h && o().createElement("span", { className: i.plus }, "+"),
            ),
          );
        };
        _.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
        var c = t(2372),
          m = t(280),
          d = (t(3649), t(6373)),
          E = t(7727);
        const A = {
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
        var h = t(2269);
        const b = R.strings.battle_pass.awardsWidget,
          C = ({
            type: e,
            count: u,
            disabled: t = !1,
            onClick: a,
            size: i,
            isLocked: l = !1,
            hasTriger: s = !1,
            hasMarathon: C = !1,
            hasResource: F = !1,
            maxCount: p = 0,
            newItemsCount: D = 0,
          }) => {
            let g = "",
              B = "";
            const v = e === h.w.Collection && p === u,
              w = i === h.W.Small && s;
            switch (e) {
              case h.w.Award:
                ((g = 1 === u ? b.title.awardSingle() : b.title.awardMultiple()),
                  (B = t ? b.description.awardDisabled() : b.description.award()));
                break;
              case h.w.Coin:
                ((g = b.title.coin()), (B = b.description.coin()));
                break;
              case h.w.Point:
                ((g = b.title.point()),
                  (B = ((e, u, t) => {
                    switch (!0) {
                      case e && u && t:
                        return b.description.pointLockedExceptExtraAndResource();
                      case e && !u && t:
                        return b.description.pointLockedExceptResource();
                      case e && u:
                        return b.description.pointLockedExceptExtra();
                      case e && !u:
                        return b.description.pointLocked();
                      default:
                        return b.description.point();
                    }
                  })(l, C, F)));
                break;
              case h.w.Collection:
                ((g = b.title.collection()),
                  (B = v ? b.description.collectionCompleted() : b.description.collection()));
            }
            const f = r()(
                A.base,
                A[`base__${i}`],
                t && A.base__disabled,
                l && A.base__locked,
                e === h.w.Award && !t && A.base__hasAppearAnimation,
              ),
              S = r()(A.border, A[`border__${i}${e}`], w && A.border__triggered),
              x = r()(A.borderHover, A[`borderHover__${i}${e}`]),
              L = r()(A.borderDisabled, A[`borderDisabled__${i}`]),
              y = r()(A.shine, A[`shine__${i}Left`]),
              P = r()(A.shine, A[`shine__${i}Right`]),
              M = r()(A.bg, A[`bg__${i}${e}`]),
              k = r()(A.bgHover, A[`bgHover__${i}${e}`]),
              T = r()(A.bgDisabled, A[`bgDisabled__${i}`]),
              N = r()(A.locked, A[`locked__${i}`]),
              R = r()(A.lockedHover, A[`lockedHover__${i}`]),
              I = (0, n.useCallback)(() => {
                t || (E.$.playClick(), a());
              }, [t, a]),
              O = (0, n.useCallback)(() => {
                (0, E.G)("bp_highlight_02");
              }, []);
            return o().createElement(
              d.i,
              { body: B, isEnabled: Boolean(B) },
              o().createElement(
                "div",
                { className: f, onMouseEnter: O, onClick: I },
                D > 0 &&
                  o().createElement(
                    "div",
                    { className: A.bubble },
                    o().createElement(_, { size: "small" }),
                  ),
                t
                  ? o().createElement("div", { className: L })
                  : o().createElement(
                      o().Fragment,
                      null,
                      o().createElement("div", { className: S }),
                      o().createElement("div", { className: x }),
                    ),
                e === h.w.Award &&
                  !t &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement("div", { className: y }),
                    o().createElement("div", { className: P }),
                  ),
                t
                  ? o().createElement("div", { className: T })
                  : o().createElement(
                      o().Fragment,
                      null,
                      o().createElement("div", { className: M }),
                      o().createElement("div", { className: k }),
                    ),
                l &&
                  o().createElement(
                    o().Fragment,
                    null,
                    o().createElement("div", { className: N }),
                    o().createElement("div", { className: R }),
                  ),
                e === h.w.Award && !t && o().createElement("div", { className: A.arrow }),
                o().createElement("div", { className: r()(A.icon, A[`icon__${i}${e}`]) }),
                o().createElement(
                  "div",
                  { className: A.count },
                  e === h.w.Collection
                    ? !v && o().createElement(m.z, { text: `${u || 0} / ${p}` })
                    : o().createElement(c.A, { format: "integral", value: u }),
                  v && o().createElement("div", { className: A.completedCollectionIcon }),
                ),
                o().createElement("div", { className: r()(A.label, A[`label__${i}${e}`]) }, g),
                e === h.w.Award &&
                  !t &&
                  o().createElement(
                    "div",
                    { className: A.blinkShape },
                    o().createElement("div", { className: A.blink }),
                  ),
              ),
            );
          },
          F = {
            base: "AwardsWidget_base_0f",
            base__small: "AwardsWidget_base__small_19",
            award: "AwardsWidget_award_c6",
            base__big: "AwardsWidget_base__big_f7",
          },
          p = ({
            size: e = h.W.Small,
            notChosenRewardCount: u,
            pointsCount: t,
            isPointsLocked: a,
            isAwardDisabled: n,
            coinCount: i,
            collectionItemCount: l,
            maxCollectionItemCount: s,
            newCollectionItemCount: _,
            isBPFirstEnter: c,
            isCollectionsEnabled: m,
            onPointsClick: d,
            onCoinClick: E,
            onTakeRewardsClick: A,
            onCollectionClick: b,
            hasMarathon: p,
            hasResource: D = !1,
            isBpPointsShopEntryPointActive: g = !1,
            isBpCoinShopEntryPointActive: B = !1,
          }) =>
            o().createElement(
              "div",
              { className: r()(F.base, F[`base__${e}`]) },
              u > 0 &&
                o().createElement(
                  "div",
                  { className: F.award },
                  o().createElement(C, {
                    type: h.w.Award,
                    size: e,
                    count: u,
                    disabled: n,
                    onClick: A,
                  }),
                ),
              B &&
                o().createElement(
                  "div",
                  { className: F.award },
                  o().createElement(C, { type: h.w.Coin, count: i, onClick: E, size: e }),
                ),
              g &&
                o().createElement(
                  "div",
                  { className: F.award },
                  o().createElement(C, {
                    type: h.w.Point,
                    count: t,
                    onClick: d,
                    size: e,
                    isLocked: a,
                    hasMarathon: p,
                    hasResource: D,
                  }),
                ),
              m &&
                o().createElement(
                  "div",
                  { className: r()(F.award, F.award__last) },
                  o().createElement(C, {
                    type: h.w.Collection,
                    count: l,
                    maxCount: s,
                    newItemsCount: _,
                    hasTriger: c,
                    onClick: b,
                    size: e,
                  }),
                ),
            );
      },
      9830: (e, u, t) => {
        "use strict";
        t.d(u, { G: () => oe });
        var a = t(6483),
          r = t.n(a),
          n = t(6179),
          o = t.n(n),
          i = t(903);
        const l = {
            base: "Emblem_base_be",
            progress: "Emblem_progress_37",
            progress__small: "Emblem_progress__small_42",
            progress__completed: "Emblem_progress__completed_69",
            hideProgress: "Emblem_hideProgress_b4",
            progress__hidden: "Emblem_progress__hidden_6d",
            image: "Emblem_image_dc",
            image__micro: "Emblem_image__micro_aa",
            image__small: "Emblem_image__small_ce",
            image__open: "Emblem_image__open_43",
            image__openSmall: "Emblem_image__openSmall_5d",
            image__openMicro: "Emblem_image__openMicro_a9",
            image__battlePass: "Emblem_image__battlePass_ba",
            image__battlePassSmall: "Emblem_image__battlePassSmall_d5",
            image__battlePassMicro: "Emblem_image__battlePassMicro_6e",
            image__battlePassOpen: "Emblem_image__battlePassOpen_36",
            image__battlePassSmallOpen: "Emblem_image__battlePassSmallOpen_2f",
            image__battlePassMicroOpen: "Emblem_image__battlePassMicroOpen_e5",
            image__seasonWaiting: "Emblem_image__seasonWaiting_96",
            image__seasonWaitingSmall: "Emblem_image__seasonWaitingSmall_c0",
            image__seasonWaitingMicro: "Emblem_image__seasonWaitingMicro_86",
            image__completedFree: "Emblem_image__completedFree_56",
            image__completedFreeSmall: "Emblem_image__completedFreeSmall_a1",
            image__completedFreeMicro: "Emblem_image__completedFreeMicro_45",
            image__completedFreeOpen: "Emblem_image__completedFreeOpen_08",
            image__completedFreeSmallOpen: "Emblem_image__completedFreeSmallOpen_91",
            image__completedFreeMicroOpen: "Emblem_image__completedFreeMicroOpen_d3",
            image__completedGolden: "Emblem_image__completedGolden_77",
            image__completedGoldenSmall: "Emblem_image__completedGoldenSmall_be",
            image__completedGoldenMicro: "Emblem_image__completedGoldenMicro_2d",
            marathon: "Emblem_marathon_c6",
            resource: "Emblem_resource_97",
            marathon__micro: "Emblem_marathon__micro_61",
            resource__micro: "Emblem_resource__micro_67",
            marathon__small: "Emblem_marathon__small_0b",
            resource__small: "Emblem_resource__small_41",
            hideLevel: "Emblem_hideLevel_f2",
            showLevel: "Emblem_showLevel_c5",
            hideLevelSmall: "Emblem_hideLevelSmall_cc",
            showLevelSmall: "Emblem_showLevelSmall_31",
            hideLevelMicro: "Emblem_hideLevelMicro_15",
            showLevelMicro: "Emblem_showLevelMicro_bc",
            showIcon: "Emblem_showIcon_c2",
            showIconSmall: "Emblem_showIconSmall_1d",
            showIconMicro: "Emblem_showIconMicro_f8",
          },
          s = {
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
          _ = "R.images.gui.maps.icons.battlePass.logo",
          c = R.images.gui.maps.icons.battlePass.logo,
          m = (e, u, t) => {
            if (e && u) {
              const e = `c_${t}_font_texture_gold_contrast`;
              return c.$dyn(e) ? `url(${_}.${e})` : `url(${_}.font_texture_gold_contrast)`;
            }
            if (e) {
              const e = `c_${t}_font_texture_gold`;
              return c.$dyn(e) ? `url(${_}.${e})` : `url(${_}.font_texture_gold)`;
            }
            const a = `c_${t}_font_texture`;
            return c.$dyn(a) ? `url(${_}.${a})` : `url(${_}.font_texture)`;
          },
          d = (0, n.memo)(
            ({
              level: e,
              size: u,
              isGold: t,
              isForRewardScreen: a = !1,
              curState: n,
              isFirstLevel: i,
              showProgressionCompleted: l,
              chapterID: _ = 0,
            }) => {
              const c = r()(s.base, s[`base__${u}`]),
                d = r()(
                  s.text,
                  s.text__filtered,
                  s[`text__${u}`],
                  s[`text__${n}`],
                  l && s.text__hideWithDelay,
                  i && s.text__new,
                  a && s.text__rewardScreen,
                ),
                E = r()(
                  s.textWithBlend,
                  i && s.text__new,
                  l && s.text__hideWithDelay,
                  s[`textWithBlend__${n}`],
                ),
                A = r()(s.text, s.text__blended, s[`text__${u}`], a && s.text__rewardScreen),
                h = r()(s.textMask, a && s.textMask__animated, s[`textMask__${u}`]);
              return o().createElement(
                "div",
                { className: c },
                o().createElement("div", { className: d }, e),
                o().createElement(
                  "div",
                  { className: E },
                  o().createElement("div", { className: A }, e),
                  o().createElement("div", {
                    className: h,
                    style: { backgroundImage: m(t, a, _) },
                  }),
                ),
              );
            },
          );
        var E = t(8546);
        const A = {
            label: "EmblemLabels_label_14",
            label__small: "EmblemLabels_label__small_a3",
            label__micro: "EmblemLabels_label__micro_4b",
            label__hasProgress: "EmblemLabels_label__hasProgress_26",
            label__hasProgressProgression: "EmblemLabels_label__hasProgressProgression_77",
            label__hasProgressSmall: "EmblemLabels_label__hasProgressSmall_c1",
            label__show: "EmblemLabels_label__show_3d",
            showLevel: "EmblemLabels_showLevel_04",
            label__showSmall: "EmblemLabels_label__showSmall_7e",
            showLevelSmall: "EmblemLabels_showLevelSmall_2f",
            label__hide: "EmblemLabels_label__hide_28",
            hideLevel: "EmblemLabels_hideLevel_be",
            label_hideSmall: "EmblemLabels_label_hideSmall_65",
            hideLevelSmall: "EmblemLabels_hideLevelSmall_c1",
            label__hideWithDelay: "EmblemLabels_label__hideWithDelay_68",
            label__hideWithDelaySmall: "EmblemLabels_label__hideWithDelaySmall_36",
            label__new: "EmblemLabels_label__new_d7",
            label__newSmall: "EmblemLabels_label__newSmall_c1",
            label__disabled: "EmblemLabels_label__disabled_b6",
            icon: "EmblemLabels_icon_40",
            icon__small: "EmblemLabels_icon__small_f3",
            icon__micro: "EmblemLabels_icon__micro_cf",
            icon__animated: "EmblemLabels_icon__animated_09",
            showIcon: "EmblemLabels_showIcon_d3",
            icon__animatedSmall: "EmblemLabels_icon__animatedSmall_e4",
            icon__animatedMicro: "EmblemLabels_icon__animatedMicro_10",
            showIconSmall: "EmblemLabels_showIconSmall_cb",
            hideLevelMicro: "EmblemLabels_hideLevelMicro_65",
            showLevelMicro: "EmblemLabels_showLevelMicro_ab",
            hideProgress: "EmblemLabels_hideProgress_7f",
            showIconMicro: "EmblemLabels_showIconMicro_5c",
          },
          h = (e, u) => {
            const t = e ? "BP" : "";
            return `${((e) => {
              switch (e) {
                case E.$u.Small:
                  return "l";
                case E.$u.Micro:
                  return "s";
                default:
                  return "xl";
              }
            })(u)}${t}`;
          },
          b = (0, n.memo)(
            ({
              newLevel: e,
              level: u,
              size: t,
              battlePassState: a,
              hasProgression: n,
              isGolden: l,
              labelAnimation: s,
              newLabelAnimation: _,
              isChapterChosen: c = !1,
              chapterID: m = 0,
              isProgressionCompleted: b = !1,
              hasBeenActive: C = !1,
              isChapterSelection: F = !1,
              isProgression: p = !1,
            }) => {
              let D = "",
                g = "";
              t === E.$u.Small
                ? ((D = "Small"), (g = "__small"))
                : t === E.$u.Micro && ((D = "Micro"), (g = "__micro"));
              const B = a === E.Bq.SwitchedChapterRightNow,
                v = a === E.Bq.CompletedRightNow,
                w = ((e, u, t, a, r) => (e || r ? u || !t : u || !a))(F, b, C, c, p),
                f = !p && !F;
              return o().createElement(
                o().Fragment,
                null,
                w
                  ? o().createElement("div", {
                      className: r()(A.icon, g && A[`icon${g}`], v && A[`icon__animated${D}`]),
                      style: {
                        backgroundImage: `url(${(() => {
                          const e = R.images.gui.maps.icons.battlePass.logo,
                            u = h(l, t);
                          if (f) {
                            if (b) {
                              const t = e.tank.$dyn(`tank_${u}`),
                                a = e.tank.$dyn(`c_${m}_tank_${u}`);
                              return null != a ? a : t;
                            }
                            if (!c) return e.$dyn("not_chosen");
                          }
                          return (0, i.wD)(e.chapterIcons, m, u);
                        })()})`,
                      },
                    })
                  : o().createElement(
                      "div",
                      {
                        className: r()(
                          A.label,
                          A[`label${g}`],
                          B && A.label__new,
                          B && A[`label__new${D}`],
                          !v && b && A.label__disabled,
                          A[`label__${s}${D}`],
                          n && A[`label__hasProgress${D}`],
                          n && A[`label__hasProgress${D}${p ? "Progression" : ""}`],
                        ),
                        lang: R.strings.settings.LANGUAGE_CODE(),
                      },
                      o().createElement(d, {
                        level: u,
                        size: t,
                        isGold: l,
                        isFirstLevel: B,
                        curState: s,
                        showProgressionCompleted: v,
                        key: "label",
                        chapterID: m,
                      }),
                    ),
                e &&
                  o().createElement(
                    "div",
                    {
                      className: r()(
                        A.label,
                        A[`label${g}`],
                        B && A.label__new,
                        B && A[`label__new${D}`],
                        A[`label__${_}${D}`],
                        n && A[`label__hasProgress${D}`],
                      ),
                    },
                    o().createElement(d, {
                      level: e,
                      size: t,
                      isGold: l,
                      isFirstLevel: B,
                      curState: _,
                      key: "newLabel",
                      chapterID: m,
                    }),
                  ),
              );
            },
          ),
          C = {
            base: "ProgressBar_base_45",
            base__medium: "ProgressBar_base__medium_62",
            base__small: "ProgressBar_base__small_df",
            background: "ProgressBar_background_51",
            background__medium: "ProgressBar_background__medium_6e",
            background__small: "ProgressBar_background__small_46",
            lineWrapper: "ProgressBar_lineWrapper_6a",
          };
        let F, p;
        (!(function (e) {
          ((e.Small = "small"), (e.Medium = "medium"), (e.Big = "big"), (e.Default = "big"));
        })(F || (F = {})),
          (function (e) {
            ((e[(e.Simple = 0)] = "Simple"), (e[(e.Growing = 1)] = "Growing"));
          })(p || (p = {})));
        const D = ({ size: e = F.Default, classMix: u }) =>
            o().createElement("div", { className: r()(C.background, C[`background__${e}`], u) }),
          g = {
            base: "ProgressBarBlink_base_24",
            base__medium: "ProgressBarBlink_base__medium_ec",
            base__small: "ProgressBarBlink_base__small_0f",
          },
          B = ({ size: e }) => {
            const u = r()(g.base, g[`base__${e}`]);
            return o().createElement("div", { className: u });
          },
          v = {
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
          w = (0, n.memo)(
            ({
              size: e,
              lineRef: u,
              disabled: t,
              baseStyles: a,
              isComplete: n,
              withoutBounce: i,
            }) => {
              const l = r()(
                  v.base,
                  v[`base__${e}`],
                  t && v.base__disabled,
                  n && v.base__finished,
                  i && v.base__withoutBounce,
                ),
                s = !t && !n;
              return o().createElement(
                "div",
                { className: l, style: a, ref: u },
                o().createElement("div", { className: v.pattern }),
                o().createElement("div", { className: v.gradient }),
                s && o().createElement(B, { size: e }),
              );
            },
          ),
          f = ({ size: e, value: u, lineRef: t, disabled: a, onComplete: r }) => {
            const i = (0, n.useMemo)(() => ({ width: `${u}%`, transitionProperty: "none" }), [u]),
              l = 100 === u;
            return (
              (0, n.useEffect)(() => {
                l && r && r();
              }, [l, r]),
              o().createElement(w, {
                size: e,
                disabled: a,
                baseStyles: i,
                isComplete: l,
                lineRef: t,
              })
            );
          };
        var S = t(122);
        let x, L;
        (!(function (e) {
          ((e.Idle = "Idle"), (e.Grow = "Grow"), (e.Shrink = "Shrink"), (e.End = "End"));
        })(x || (x = {})),
          (function (e) {
            ((e.Idle = "Idle"), (e.In = "In"), (e.End = "End"));
          })(L || (L = {})));
        const y = "ProgressBarDeltaSimple_base_6c",
          P = "ProgressBarDeltaSimple_delta_99",
          M = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: a,
              size: r,
              to: i,
              onEndAnimation: l,
              onChangeAnimationState: s,
            }) => {
              const _ = i < a,
                c = (0, n.useState)(L.Idle),
                m = c[0],
                d = c[1],
                E = m === L.In,
                A = m === L.End,
                h = m === L.Idle,
                b = (0, n.useCallback)(
                  (e) => {
                    (d(e), s && s(e));
                  },
                  [s],
                );
              ((0, n.useEffect)(() => {
                if (h && !t) {
                  const e = u;
                  return (0, S.F)(() => {
                    b(L.In);
                  }, e);
                }
              }, [b, t, h, u]),
                (0, n.useEffect)(() => {
                  if (E) {
                    const t = e + u;
                    return (0, S.F)(() => {
                      (l && l(), b(L.End));
                    }, t);
                  }
                }, [b, E, l, u, e]));
              const C = (0, n.useMemo)(
                  () => ({
                    width: "100%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, u, e],
                ),
                F = (0, n.useMemo)(
                  () => ({
                    width: "0%",
                    transitionDuration: `${e}ms`,
                    transitionDelay: `${u}ms`,
                    [_ ? "left" : "right"]: "0",
                  }),
                  [_, u, e],
                ),
                p = (0, n.useMemo)(
                  () => ({ width: `${Math.abs(a - i)}%`, left: `${_ ? i : a}%` }),
                  [a, _, i],
                );
              return A
                ? null
                : o().createElement(
                    "div",
                    { className: y, style: p },
                    o().createElement(
                      "div",
                      { style: h ? C : F, className: P },
                      o().createElement(B, { size: r }),
                    ),
                  );
            },
          ),
          k = (0, n.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: a,
              disabled: r,
              isComplete: i,
              animationSettings: l,
              onChangeAnimationState: s,
              onEndAnimation: _,
            }) => {
              const c = (0, n.useMemo)(
                () => ({
                  width: `${e}%`,
                  transitionDuration: `${l.line.duration}ms`,
                  transitionDelay: `${l.line.delay}ms`,
                }),
                [l.line.delay, l.line.duration, e],
              );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(w, {
                  size: u,
                  lineRef: a,
                  disabled: r,
                  isComplete: i,
                  baseStyles: c,
                }),
                t >= 0 &&
                  o().createElement(M, {
                    transitionDuration: l.delta.duration,
                    transitionDelay: l.delta.delay,
                    freezed: l.freezed,
                    from: t,
                    size: u,
                    to: e,
                    onChangeAnimationState: s,
                    onEndAnimation: _,
                  }),
              );
            },
          ),
          T = "ProgressBarDeltaGrow_base_7e",
          N = "ProgressBarDeltaGrow_base__withoutBounce_b5",
          I = "ProgressBarDeltaGrow_glow_68",
          O = (e) => (e ? { left: 0 } : { right: 0 }),
          H = (e, u) => (e ? { right: 100 - u + "%" } : { left: `${u}%` }),
          $ = (e) => ({ transitionDuration: `${e}ms` }),
          G = (0, n.memo)(
            ({
              transitionDuration: e,
              transitionDelay: u,
              freezed: t,
              from: a,
              size: i,
              to: l,
              onEndAnimation: s,
              onChangeAnimationState: _,
              className: c,
            }) => {
              const m = l < a,
                d = (0, n.useState)(x.Idle),
                E = d[0],
                A = d[1],
                h = E === x.End,
                b = E === x.Idle,
                C = E === x.Grow,
                F = E === x.Shrink,
                p = (0, n.useCallback)(
                  (e) => {
                    (A(e), _ && _(e));
                  },
                  [_],
                ),
                D = (0, n.useCallback)(
                  (e, u) =>
                    (0, S.F)(() => {
                      p(e);
                    }, u),
                  [p],
                );
              (0, n.useEffect)(() => {
                if (!t)
                  return b
                    ? D(x.Grow, u)
                    : C
                      ? D(x.Shrink, e)
                      : F
                        ? D(x.End, e)
                        : void (h && s && s());
              }, [D, t, h, C, b, F, s, u, e]);
              const g = (0, n.useMemo)(() => Object.assign({ width: "100%" }, $(e), O(m)), [m, e]),
                v = (0, n.useMemo)(() => Object.assign({ width: "0%" }, $(e), O(m)), [m, e]),
                w = (0, n.useMemo)(() => Object.assign({ width: "0%" }, H(m, a), $(e)), [a, m, e]),
                f = (0, n.useMemo)(
                  () => Object.assign({ width: `${Math.abs(l - a)}%` }, H(m, a), $(e)),
                  [a, m, l, e],
                );
              if (h) return null;
              const L = r()(T, c, m && 0 === l && N);
              return o().createElement(
                "div",
                { style: b ? w : f, className: L },
                o().createElement(
                  "div",
                  { style: F ? v : g, className: I },
                  o().createElement(B, { size: i }),
                ),
              );
            },
          ),
          W = (0, n.memo)(
            ({
              to: e,
              size: u,
              from: t,
              lineRef: a,
              disabled: r,
              isComplete: i,
              animationSettings: l,
              onEndAnimation: s,
              onChangeAnimationState: _,
            }) => {
              const c = e < t,
                m = (0, n.useState)(!1),
                d = m[0],
                E = m[1],
                A = (0, n.useCallback)(
                  (e) => {
                    (e === x.Shrink && E(!0), _ && _(e));
                  },
                  [_],
                ),
                h = (0, n.useMemo)(() => ({ width: `${t}%`, transitionProperty: "none" }), [t]),
                b = (0, n.useMemo)(
                  () => ({ width: `${e}%`, transitionDuration: `${l.line.duration}ms` }),
                  [l.line.duration, e],
                );
              return o().createElement(
                o().Fragment,
                null,
                o().createElement(w, {
                  size: u,
                  lineRef: a,
                  disabled: r,
                  isComplete: i,
                  withoutBounce: c && 0 === e,
                  baseStyles: d ? b : h,
                }),
                t >= 0 &&
                  o().createElement(G, {
                    transitionDuration: l.delta.duration,
                    transitionDelay: l.delta.delay,
                    onChangeAnimationState: A,
                    freezed: l.freezed,
                    onEndAnimation: s,
                    from: t,
                    size: u,
                    to: e,
                    className: l.delta.className,
                  }),
              );
            },
          ),
          U = ["onComplete", "onEndAnimation"];
        function z() {
          return (
            (z =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            z.apply(this, arguments)
          );
        }
        const j = (0, n.memo)((e) => {
            let u = e.onComplete,
              t = e.onEndAnimation,
              a = (function (e, u) {
                if (null == e) return {};
                var t,
                  a,
                  r = {},
                  n = Object.keys(e);
                for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
                return r;
              })(e, U);
            const r = (0, n.useState)(!1),
              i = r[0],
              l = r[1],
              s = (0, n.useCallback)(() => {
                const e = 100 === a.to;
                (e !== i && l(e), e && u && u(), t && t());
              }, [i, u, t, a.to]);
            switch (a.animationSettings.type) {
              case p.Simple:
                return o().createElement(k, z({}, a, { onEndAnimation: s, isComplete: i }));
              case p.Growing:
                return o().createElement(W, z({}, a, { onEndAnimation: s, isComplete: i }));
              default:
                return null;
            }
          }),
          X = ["onEndAnimation"];
        function q() {
          return (
            (q =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            q.apply(this, arguments)
          );
        }
        const V = (0, n.memo)((e) => {
          let u = e.onEndAnimation,
            t = (function (e, u) {
              if (null == e) return {};
              var t,
                a,
                r = {},
                n = Object.keys(e);
              for (a = 0; a < n.length; a++) ((t = n[a]), u.indexOf(t) >= 0 || (r[t] = e[t]));
              return r;
            })(e, X);
          const a = (0, n.useRef)({}),
            r = (0, n.useCallback)(() => {
              ((a.current.from = void 0), u && u());
            }, [u]),
            i = "number" == typeof a.current.from ? a.current.from : t.from;
          return (
            (a.current.from = i),
            o().createElement(j, q({}, t, { onEndAnimation: r, key: `${i}-${t.to}`, from: i }))
          );
        });
        function Y() {
          return (
            (Y =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            Y.apply(this, arguments)
          );
        }
        const K = (0, n.memo)(
            ({
              size: e,
              value: u,
              lineRef: t,
              disabled: a,
              deltaFrom: r,
              animationSettings: n,
              onEndAnimation: i,
              onChangeAnimationState: l,
              onComplete: s,
            }) => {
              if (r === u)
                return o().createElement(f, {
                  key: `${r}-${u}`,
                  size: e,
                  value: u,
                  lineRef: t,
                  disabled: a,
                  onComplete: s,
                });
              const _ = {
                from: r,
                to: u,
                size: e,
                lineRef: t,
                disabled: a,
                animationSettings: n,
                onComplete: s,
                onEndAnimation: i,
                onChangeAnimationState: l,
              };
              return n.withStack
                ? o().createElement(V, _)
                : o().createElement(j, Y({ key: `${r}-${u}` }, _));
            },
          ),
          Z = (e) => ({
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
          Q = (e, u, t) => (t < e ? e : t > u ? u : t),
          J = (e, u, t) => {
            if ("number" == typeof t) {
              return (Q(0, u, t) / u) * 100;
            }
            return e;
          },
          ee = {
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
          ue = {
            freezed: !1,
            withStack: !1,
            type: p.Growing,
            delta: { duration: 500, delay: 0 },
            line: { duration: 500, delay: 0 },
          },
          te = (0, n.memo)(
            ({
              maxValue: e = 100,
              theme: u = ee,
              size: t = F.Default,
              animationSettings: a = ue,
              disabled: i = !1,
              withoutBackground: l = !1,
              progressBarBackgroundClassMix: s,
              value: _,
              deltaFrom: c,
              lineRef: m,
              onChangeAnimationState: d,
              onEndAnimation: E,
              onComplete: A,
            }) => {
              const h = ((e, u, t) =>
                (0, n.useMemo)(() => {
                  const a = (Q(0, u, e) / u) * 100;
                  return { value: a, deltaFrom: J(a, u, t) };
                }, [t, u, e]))(_, e, c);
              return o().createElement(
                "div",
                { className: r()(C.base, C[`base__${t}`]), style: Z(u) },
                !l && o().createElement(D, { size: t, classMix: s }),
                o().createElement(K, {
                  size: t,
                  lineRef: m,
                  disabled: i,
                  value: h.value,
                  deltaFrom: h.deltaFrom,
                  animationSettings: a,
                  onEndAnimation: E,
                  onChangeAnimationState: d,
                  onComplete: A,
                }),
              );
            },
          ),
          ae = {
            base: "EmblemProgressBar_base_5c",
            base__small: "EmblemProgressBar_base__small_6c",
            base__completed: "EmblemProgressBar_base__completed_6d",
            hideProgress: "EmblemProgressBar_hideProgress_18",
            base__completePostProgression: "EmblemProgressBar_base__completePostProgression_20",
            base__hidden: "EmblemProgressBar_base__hidden_8b",
            hideLevel: "EmblemProgressBar_hideLevel_1e",
            showLevel: "EmblemProgressBar_showLevel_5d",
            hideLevelSmall: "EmblemProgressBar_hideLevelSmall_ae",
            showLevelSmall: "EmblemProgressBar_showLevelSmall_df",
            hideLevelMicro: "EmblemProgressBar_hideLevelMicro_13",
            showLevelMicro: "EmblemProgressBar_showLevelMicro_ae",
            showIcon: "EmblemProgressBar_showIcon_55",
            showIconSmall: "EmblemProgressBar_showIconSmall_26",
            showIconMicro: "EmblemProgressBar_showIconMicro_78",
          },
          re = (0, n.memo)(
            ({
              progression: e,
              isNoVehicles: u = !1,
              showProgressionCompleted: t,
              isProgressionCompleted: a,
              size: n,
            }) => {
              const i = r()(
                ae.base,
                ae[`base__${n}`],
                t && ae.base__completed,
                !t && a && ae.base__hidden,
              );
              return o().createElement(
                "div",
                { className: i },
                o().createElement(te, {
                  key: e.to,
                  size: F.Small,
                  value: e.to || 0,
                  deltaFrom: e.from || 0,
                  disabled: u,
                }),
              );
            },
          );
        function ne() {
          return (
            (ne =
              Object.assign ||
              function (e) {
                for (var u = 1; u < arguments.length; u++) {
                  var t = arguments[u];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (e[a] = t[a]);
                }
                return e;
              }),
            ne.apply(this, arguments)
          );
        }
        const oe = (0, n.memo)((e) => {
          const u = e.progression,
            t = e.size,
            a = e.battlePassState,
            n = e.hasBattlePass,
            s = e.isChapterChosen,
            _ = e.hasBeenActive,
            c = void 0 !== _ && _,
            m = e.isChapterSelection,
            d = void 0 !== m && m,
            A = e.isOpen,
            h = void 0 !== A && A,
            C = e.isProgression,
            F = void 0 !== C && C,
            p = e.showProgressBar,
            D = void 0 === p || p,
            g = e.chapterType,
            B = e.chapterID;
          let v = "",
            w = "",
            f = "";
          t === E.$u.Small
            ? ((v = "Small"), (w = "__small"), (f = "_small"))
            : t === E.$u.Micro && ((v = "Micro"), (w = "__micro"), (f = "_micro"));
          const S = h ? "Open" : "",
            x = a === E.Bq.CompletedRightNow,
            L = n || a === E.Bq.Bought,
            y = (a === E.Bq.Completed || x) && L,
            P = (a === E.Bq.Completed || x) && !L,
            M = y || P,
            k = r()(
              l.image,
              l[`image${w}`],
              h && l[`image__open${v}`],
              L && l[`image__battlePass${v}${S}`],
              a === E.Bq.AwaitSeason && l[`image__seasonWaiting${v}`],
              P && l[`image__completedFree${v}${S}`],
            ),
            T = r()(l[`${g}`], l[`${g}${w}`]),
            N = void 0 !== u.from,
            R = D && ((N && s) || c);
          return o().createElement(
            "div",
            { className: l.base },
            o().createElement("div", { className: T }),
            o().createElement(
              "div",
              { className: k, style: (0, i.FL)(B, f, h, L) },
              a !== E.Bq.AwaitSeason &&
                o().createElement(
                  o().Fragment,
                  null,
                  o().createElement(
                    b,
                    ne(
                      {
                        hasProgression: N,
                        isGolden: L,
                        isProgressionCompleted: M,
                        isChapterChosen: s,
                        hasBeenActive: c,
                        isChapterSelection: d,
                        isProgression: F,
                      },
                      e,
                      u,
                    ),
                  ),
                  R &&
                    o().createElement(re, {
                      key: u.to,
                      progression: u,
                      showProgressionCompleted: x,
                      isProgressionCompleted: M,
                      size: t,
                    }),
                ),
            ),
          );
        });
      },
      8546: (e, u, t) => {
        "use strict";
        let a, r, n, o;
        (t.d(u, { $u: () => a, Bq: () => n }),
          (function (e) {
            ((e.Micro = "micro"), (e.Small = "small"), (e.Medium = "medium"));
          })(a || (a = {})),
          (function (e) {
            ((e.ACTIVE = "active"), (e.COMPLETED = "completed"), (e.NOT_CHOSEN = "notChosen"));
          })(r || (r = {})),
          (function (e) {
            ((e.AwaitSeason = "awaitSeason"),
              (e.Bought = "bought"),
              (e.Free = "free"),
              (e.Completed = "completed"),
              (e.CompletedRightNow = "completedRightNow"),
              (e.SwitchedChapterRightNow = "switchedChapterRightNow"),
              (e.NoVehiclesBase = "noVehiclesBase"),
              (e.ChapterNotChosen = "chapterNotChosen"));
          })(n || (n = {})),
          (function (e) {
            ((e.None = ""),
              (e.ShowLevel = "show"),
              (e.HideLevel = "hide"),
              (e.HideLevelWithDelay = "hideWithDelay"));
          })(o || (o = {})));
      },
      5287: (e, u, t) => {
        "use strict";
        t.d(u, { Z: () => a });
        const a = { base: "FormatText_base_d0" };
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
        for (l = 0; l < deferred.length; l++) {
          for (var [u, t, a] = deferred[l], n = !0, o = 0; o < u.length; o++)
            (!1 & a || r >= a) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](u[o]))
              ? u.splice(o--, 1)
              : ((n = !1), a < r && (r = a));
          if (n) {
            deferred.splice(l--, 1);
            var i = t();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      a = a || 0;
      for (var l = deferred.length; l > 0 && deferred[l - 1][2] > a; l--)
        deferred[l] = deferred[l - 1];
      deferred[l] = [u, t, a];
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
    (__webpack_require__.j = 1201),
    (() => {
      var e = { 1201: 0, 7737: 0, 1730: 0 };
      __webpack_require__.O.j = (u) => 0 === e[u];
      var u = (u, t) => {
          var a,
            r,
            [n, o, i] = t,
            l = 0;
          if (n.some((u) => 0 !== e[u])) {
            for (a in o) __webpack_require__.o(o, a) && (__webpack_require__.m[a] = o[a]);
            if (i) var s = i(__webpack_require__);
          }
          for (u && u(t); l < n.length; l++)
            ((r = n[l]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(s);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(u.bind(null, 0)), (t.push = u.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [1519], () => __webpack_require__(908));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
