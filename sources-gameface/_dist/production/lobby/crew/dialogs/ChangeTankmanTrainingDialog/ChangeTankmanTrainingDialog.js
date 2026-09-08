(() => {
  var __webpack_modules__ = {
      7405: (u, e, t) => {
        "use strict";
        t.d(e, { F: () => E });
        var r = t(6483),
          n = t.n(r),
          a = t(6179),
          i = t.n(a),
          o = t(329),
          s = t(2372),
          l = t(8460);
        const c = ({
          isDiscount: u,
          isInteractiveDiscount: e,
          size: t,
          type: r,
          isEnough: a,
          value: c,
          discountValue: E,
          showPlus: _,
          stockBackgroundName: d = o.we.Red,
        }) => {
          const A = n()(l.Z.value, l.Z[`value__${r}`], !a && l.Z.value__notEnough),
            F = n()(l.Z.icon, l.Z[`icon__${r}-${t}`]),
            D = n()(l.Z.stock, E && l.Z.stock__indent, e && l.Z.stock__interactive),
            m = _ && c > 0 && "+",
            C = n()(l.Z.base, l.Z[`base__${t}`]);
          return i().createElement(
            "span",
            { className: C },
            i().createElement(
              "span",
              { className: A },
              m,
              i().createElement(s.A, { value: c, format: r === o.V2.gold ? "gold" : "integral" }),
            ),
            i().createElement("span", { className: F }),
            u &&
              i().createElement(
                "span",
                { className: D },
                i().createElement("span", {
                  className: l.Z.stockBackground,
                  style: { backgroundImage: `url(R.images.gui.maps.icons.library.${d})` },
                }),
                Boolean(E) && E,
              ),
          );
        };
        c.defaultProps = { isEnough: !0 };
        const E = i().memo(c);
      },
      329: (u, e, t) => {
        "use strict";
        let r, n, a;
        (t.d(e, { V2: () => n, we: () => a }),
          (function (u) {
            ((u.small = "small"),
              (u.big = "big"),
              (u.large = "large"),
              (u.extraLarge = "extraLarge"));
          })(r || (r = {})),
          (function (u) {
            ((u.credits = "credits"),
              (u.gold = "gold"),
              (u.crystal = "crystal"),
              (u.xp = "xp"),
              (u.freeXP = "freeXP"),
              (u.equipCoin = "equipCoin"));
          })(n || (n = {})),
          (function (u) {
            ((u.Red = "RedActionBG"), (u.Blue = "BlueActionBG"));
          })(a || (a = {})));
      },
      2372: (u, e, t) => {
        "use strict";
        t.d(e, { A: () => i });
        var r = t(6179),
          n = t.n(r),
          a = t(4179);
        class i extends n().PureComponent {
          render() {
            let u;
            if ("gold" === this.props.format) u = a.B3.GOLD;
            else u = a.B3.INTEGRAL;
            const e = a.Z5.getNumberFormat(this.props.value, u);
            return void 0 !== this.props.value && void 0 !== e ? e : null;
          }
        }
        i.defaultProps = { format: "integral" };
      },
      3495: (u, e, t) => {
        "use strict";
        t.d(e, { Y: () => E });
        var r = t(3138),
          n = t(6179),
          a = t(1043),
          i = t(5262);
        const o = r.O.client.getSize("rem"),
          s = o.width,
          l = o.height,
          c = Object.assign({ width: s, height: l }, (0, i.T)(s, l, a.j)),
          E = (0, n.createContext)(c);
      },
      1039: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => c });
        var r = t(6179),
          n = t.n(r),
          a = t(6536),
          i = t(3495),
          o = t(1043),
          s = t(5262),
          l = t(3138);
        const c = (0, r.memo)(({ children: u }) => {
          const e = (0, r.useContext)(i.Y),
            t = (0, r.useState)(e),
            c = t[0],
            E = t[1],
            _ = (0, r.useCallback)((u, e) => {
              const t = l.O.view.pxToRem(u),
                r = l.O.view.pxToRem(e);
              E(Object.assign({ width: t, height: r }, (0, s.T)(t, r, o.j)));
            }, []);
          ((0, a.Z)(() => {
            engine.on("clientResized", _);
          }),
            (0, r.useEffect)(() => () => engine.off("clientResized", _), [_]));
          const d = (0, r.useMemo)(() => Object.assign({}, c), [c]);
          return n().createElement(i.Y.Provider, { value: d }, u);
        });
      },
      6010: (u, e, t) => {
        "use strict";
        var r = t(6179),
          n = t(7382),
          a = t(3495);
        const i = ["children"];
        const o = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, i);
          const o = (0, r.useContext)(a.Y),
            s = o.extraLarge,
            l = o.large,
            c = o.medium,
            E = o.small,
            _ = o.extraSmall,
            d = o.extraLargeWidth,
            A = o.largeWidth,
            F = o.mediumWidth,
            D = o.smallWidth,
            m = o.extraSmallWidth,
            C = o.extraLargeHeight,
            B = o.largeHeight,
            g = o.mediumHeight,
            h = o.smallHeight,
            p = o.extraSmallHeight,
            b = { extraLarge: C, large: B, medium: g, small: h, extraSmall: p };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && s) return e;
            if (t.large && l) return e;
            if (t.medium && c) return e;
            if (t.small && E) return e;
            if (t.extraSmall && _) return e;
          } else {
            if (t.extraLargeWidth && d) return (0, n.H)(e, t, b);
            if (t.largeWidth && A) return (0, n.H)(e, t, b);
            if (t.mediumWidth && F) return (0, n.H)(e, t, b);
            if (t.smallWidth && D) return (0, n.H)(e, t, b);
            if (t.extraSmallWidth && m) return (0, n.H)(e, t, b);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && C) return e;
              if (t.largeHeight && B) return e;
              if (t.mediumHeight && g) return e;
              if (t.smallHeight && h) return e;
              if (t.extraSmallHeight && p) return e;
            }
          }
          return null;
        };
        o.defaultProps = {
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
        (0, r.memo)(o);
      },
      7382: (u, e, t) => {
        "use strict";
        t.d(e, { H: () => r });
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
      },
      7739: (u, e, t) => {
        "use strict";
        t.d(e, { YN: () => n.Y, ZN: () => r.Z });
        t(6010);
        var r = t(1039),
          n = t(3495);
      },
      1043: (u, e, t) => {
        "use strict";
        t.d(e, { j: () => r });
        const r = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (u, e, t) => {
        "use strict";
        var r;
        function n(u, e, t) {
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
        (t.d(e, { T: () => n, u: () => r }),
          (function (u) {
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
          })(r || (r = {})));
      },
      7078: (u, e, t) => {
        "use strict";
        t.d(e, { t: () => s });
        var r = t(6179),
          n = t.n(r),
          a = t(2056);
        const i = ["children"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            o.apply(this, arguments)
          );
        }
        const s = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, i);
          return n().createElement(
            a.u,
            o(
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
      },
      3415: (u, e, t) => {
        "use strict";
        t.d(e, { l: () => l });
        var r = t(6179),
          n = t.n(r),
          a = t(7078),
          i = t(6373),
          o = t(2056);
        function s() {
          return (
            (s =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            s.apply(this, arguments)
          );
        }
        const l = ({ children: u, tooltipArgs: e, className: t }) => {
          if (!e) return u;
          const r = n().createElement("div", { className: t }, u);
          if (e.header || e.body) return n().createElement(i.i, e, r);
          const l = e.contentId,
            c = e.args,
            E = null == c ? void 0 : c.contentId;
          return l || E
            ? n().createElement(o.u, s({}, e, { contentId: l || E }), r)
            : n().createElement(a.t, e, r);
        };
      },
      6373: (u, e, t) => {
        "use strict";
        t.d(e, { i: () => l });
        var r = t(2056),
          n = t(6179),
          a = t.n(n);
        const i = ["children", "body", "header", "note", "alert", "args"];
        function o() {
          return (
            (o =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            o.apply(this, arguments)
          );
        }
        const s = R.views.common.tooltip_window.simple_tooltip_content,
          l = (u) => {
            let e = u.children,
              t = u.body,
              l = u.header,
              c = u.note,
              E = u.alert,
              _ = u.args,
              d = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, i);
            const A = (0, n.useMemo)(() => {
              const u = Object.assign({}, _, { body: t, header: l, note: c, alert: E });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [E, t, l, c, _]);
            return a().createElement(
              r.u,
              o(
                {
                  contentId:
                    ((F = null == _ ? void 0 : _.hasHtmlContent),
                    F ? s.SimpleTooltipHtmlContent("resId") : s.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: A,
                },
                d,
              ),
              e,
            );
            var F;
          };
      },
      2056: (u, e, t) => {
        "use strict";
        t.d(e, { u: () => l });
        var r = t(7902),
          n = t(4179),
          a = t(6179);
        const i = [
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
        function o(u) {
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
        const s = (u, e, t = {}, r = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: n.B0.TOOLTIP,
                  contentID: u,
                  decoratorID: e,
                  targetID: r,
                },
                t,
              ),
            );
          },
          l = (u) => {
            let e = u.children,
              t = u.contentId,
              n = u.args,
              l = u.onMouseEnter,
              c = u.onMouseLeave,
              E = u.onMouseDown,
              _ = u.onClick,
              d = u.ignoreShowDelay,
              A = void 0 !== d && d,
              F = u.ignoreMouseClick,
              D = void 0 !== F && F,
              m = u.decoratorId,
              C = void 0 === m ? 0 : m,
              B = u.isEnabled,
              g = void 0 === B || B,
              h = u.targetId,
              p = void 0 === h ? 0 : h,
              b = u.onShow,
              f = u.onHide,
              v = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, i);
            const w = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              x = (0, a.useMemo)(() => p || (0, r.F)().resId, [p]),
              y = (0, a.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (s(t, C, { isMouseEvent: !0, on: !0, arguments: o(n) }, x),
                  b && b(),
                  (w.current.isVisible = !0));
              }, [t, C, n, x, b]),
              T = (0, a.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const u = w.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (w.current.timeoutId = 0)),
                    s(t, C, { on: !1 }, x),
                    w.current.isVisible && f && f(),
                    (w.current.isVisible = !1));
                }
              }, [t, C, x, f]),
              L = (0, a.useCallback)((u) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(w.current.prevTarget) && T();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const u = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", L, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", L, { capture: !0 }),
                    u && window.clearTimeout(u));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === g && T();
              }, [g, T]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", T),
                  () => {
                    (window.removeEventListener("mouseleave", T), T());
                  }
                ),
                [T],
              ));
            return g
              ? (0, a.cloneElement)(
                  e,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((S = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(y, A ? 100 : 400)),
                            l && l(u),
                            S && S(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (T(), null == c || c(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === D && T(), null == _ || _(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === D && T(), null == E || E(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    v,
                  ),
                )
              : e;
            var S;
          };
      },
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
      8246: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => o });
        var r = t(3138);
        function n(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return a(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return a(u, e);
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
        function a(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, r = new Array(e); t < e; t++) r[t] = u[t];
          return r;
        }
        const i = (u) => (0 === u ? window : window.subViews.get(u));
        function o({
          initializer: u = !0,
          rootId: e = 0,
          getRoot: t = i,
          context: a = "model",
        } = {}) {
          const o = new Map();
          function s(u, e = 0) {
            viewEnv.removeDataChangedCallback(u, e)
              ? o.delete(u)
              : console.error("Can't remove callback by id:", u);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (u, e, t) => {
              t.forEach((e) => {
                const t = o.get(e);
                void 0 !== t && t(u);
              });
            });
          });
          const l = (u) => {
            const r = t(e),
              n = a.split(".").reduce((u, e) => u[e], r);
            return "string" != typeof u || 0 === u.length
              ? n
              : u.split(".").reduce((u, e) => {
                  const t = u[e];
                  return "function" == typeof t ? t.bind(u) : t;
                }, n);
          };
          return {
            subscribe: (t, n) => {
              const i = "string" == typeof n ? `${a}.${n}` : a,
                s = r.O.view.addModelObserver(i, e, !0);
              return (o.set(s, t), u && t(l(n)), s);
            },
            readByPath: l,
            createCallback: (u, e) => {
              const t = l(e);
              return (...e) => {
                t(u(...e));
              };
            },
            createCallbackNoArgs: (u) => {
              const e = l(u);
              return () => {
                e();
              };
            },
            dispose: function () {
              for (var u, t = n(o.keys()); !(u = t()).done;) {
                s(u.value, e);
              }
            },
            unsubscribe: s,
          };
        }
      },
      3215: (u, e, t) => {
        "use strict";
        t.d(e, { q: () => s });
        var r = t(4598),
          n = t(9174),
          a = t(6179),
          i = t.n(a),
          o = t(8246);
        const s = () => (u, e) => {
          const t = (0, a.createContext)({});
          return [
            function ({ mode: s = "real", options: l, children: c, mocks: E }) {
              const _ = (0, a.useRef)([]),
                d = (t, a, i) => {
                  var s;
                  const l = o.U(a),
                    c =
                      "real" === t
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (s = null == i ? void 0 : i.getter) ? s : () => {},
                          }),
                    E = (u) =>
                      "mocks" === t ? (null == i ? void 0 : i.getter(u)) : c.readByPath(u),
                    d = (u) => _.current.push(u),
                    A = u({
                      mode: t,
                      readByPath: E,
                      externalModel: c,
                      observableModel: {
                        array: (u, e) => {
                          const a = null != e ? e : E(u),
                            i = n.LO.box(a, { equals: r.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, n.aD)((u) => i.set(u)),
                                u,
                              ),
                            i
                          );
                        },
                        object: (u, e) => {
                          const a = null != e ? e : E(u),
                            i = n.LO.box(a, { equals: r.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, n.aD)((u) => i.set(u)),
                                u,
                              ),
                            i
                          );
                        },
                        primitives: (u, e) => {
                          const r = E(e);
                          if (Array.isArray(u)) {
                            const a = u.reduce((u, e) => ((u[e] = n.LO.box(r[e], {})), u), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, n.aD)((e) => {
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
                              i = Object.entries(a),
                              o = i.reduce((u, [e, t]) => ((u[t] = n.LO.box(r[e], {})), u), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, n.aD)((u) => {
                                    i.forEach(([e, t]) => {
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
                      cleanup: d,
                    }),
                    F = { mode: t, model: A, externalModel: c, cleanup: d };
                  return {
                    model: A,
                    controls: "mocks" === t && i ? i.controls(F) : e(F),
                    externalModel: c,
                    mode: t,
                  };
                },
                A = (0, a.useRef)(!1),
                F = (0, a.useState)(s),
                D = F[0],
                m = F[1],
                C = (0, a.useState)(() => d(s, l, E)),
                B = C[0],
                g = C[1];
              return (
                (0, a.useEffect)(() => {
                  A.current ? g(d(D, l, E)) : (A.current = !0);
                }, [E, D, l]),
                (0, a.useEffect)(() => {
                  m(s);
                }, [s]),
                (0, a.useEffect)(
                  () => () => {
                    (B.externalModel.dispose(), _.current.forEach((u) => u()));
                  },
                  [B],
                ),
                i().createElement(t.Provider, { value: B }, c)
              );
            },
            () => (0, a.useContext)(t),
          ];
        };
      },
      527: (u, e, t) => {
        "use strict";
        (t.r(e), t.d(e, { mouse: () => o, onResize: () => a }));
        var r = t(2472),
          n = t(1176);
        const a = (0, r.E)("clientResized"),
          i = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const o = (function () {
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
                    o = i[e]((u) => t([u, "outside"]));
                  function s(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(a, s),
                    r(),
                    () => {
                      n &&
                        (o(), window.removeEventListener(a, s), (u.listeners -= 1), r(), (n = !1));
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
            graphicsQuality: () => i,
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
        const i = {
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
            addPreloadTexture: () => o,
            children: () => r,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => a.U,
            extraSize: () => x,
            forceTriggerMouseMove: () => f,
            freezeTextureBeforeResize: () => F,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => v,
            getScale: () => D,
            getSize: () => _,
            getViewGlobalPosition: () => A,
            isClientAccessible: () => h,
            isEventHandled: () => b,
            isFocused: () => g,
            pxToRem: () => m,
            remToPx: () => C,
            resize: () => d,
            sendEvent: () => i.qP,
            setAnimateWindow: () => B,
            setEventHandled: () => p,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => y,
          }));
        var r = t(3722),
          n = t(6112),
          a = t(6538),
          i = t(8566);
        function o(u) {
          viewEnv.addPreloadTexture(u);
        }
        function s(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function l(u, e, t, r = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, r);
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
        function d(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function A(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: C(e.x), y: C(e.y) };
        }
        function F() {
          viewEnv.freezeTextureBeforeResize();
        }
        function D() {
          return viewEnv.getScale();
        }
        function m(u) {
          return viewEnv.pxToRem(u);
        }
        function C(u) {
          return viewEnv.remToPx(u);
        }
        function B(u, e) {
          viewEnv.setAnimateWindow(u, e);
        }
        function g() {
          return viewEnv.isFocused();
        }
        function h() {
          return viewEnv.isClientAccessible();
        }
        function p() {
          return viewEnv.setEventHandled();
        }
        function b() {
          return viewEnv.isEventHandled();
        }
        function f() {
          viewEnv.forceTriggerMouseMove();
        }
        function v() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(n.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === n.W[e]), u),
            {},
          ),
          x = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          y = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : a.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        "use strict";
        t.d(e, { qP: () => l });
        const r = ["args"];
        const n = 2,
          a = 16,
          i = 32,
          o = 64,
          s = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const a = e.args,
                i = (function (u, e) {
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
                    Object.assign({ __Type: t, type: u }, i, {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, i));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: u });
            var n;
          },
          l = {
            close(u) {
              s("popover" === u ? n : i);
            },
            minimize() {
              s(o);
            },
            move(u) {
              s(a, { isMouseEvent: !0, on: u });
            },
          };
      },
      4598: (u, e, t) => {
        "use strict";
        t.d(e, { jv: () => n, yR: () => r });
        function r(u) {
          return u;
        }
        function n() {
          return !1;
        }
        console.log;
      },
      7902: (u, e, t) => {
        "use strict";
        t.d(e, { F: () => r });
        const r = (u = 1) => {
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
        };
      },
      6536: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => n });
        var r = t(6179);
        const n = (u) => {
          const e = (0, r.useRef)(!1);
          e.current || (u(), (e.current = !0));
        };
      },
      5415: (u, e, t) => {
        "use strict";
        t.d(e, { Aq: () => s, GS: () => l, cJ: () => i, fd: () => o });
        var r = t(6179),
          n = t(7739),
          a = t(1043);
        let i, o, s;
        (!(function (u) {
          ((u[(u.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = a.j.small.width)] = "Small"),
            (u[(u.Medium = a.j.medium.width)] = "Medium"),
            (u[(u.Large = a.j.large.width)] = "Large"),
            (u[(u.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
        })(i || (i = {})),
          (function (u) {
            ((u[(u.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = a.j.small.width)] = "Small"),
              (u[(u.Medium = a.j.medium.width)] = "Medium"),
              (u[(u.Large = a.j.large.width)] = "Large"),
              (u[(u.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
          })(o || (o = {})),
          (function (u) {
            ((u[(u.ExtraSmall = a.j.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = a.j.small.height)] = "Small"),
              (u[(u.Medium = a.j.medium.height)] = "Medium"),
              (u[(u.Large = a.j.large.height)] = "Large"),
              (u[(u.ExtraLarge = a.j.extraLarge.height)] = "ExtraLarge"));
          })(s || (s = {})));
        const l = () => {
          const u = (0, r.useContext)(n.YN),
            e = u.width,
            t = u.height,
            a = ((u) => {
              switch (!0) {
                case u.extraLarge:
                  return i.ExtraLarge;
                case u.large:
                  return i.Large;
                case u.medium:
                  return i.Medium;
                case u.small:
                  return i.Small;
                case u.extraSmall:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(u),
            l = ((u) => {
              switch (!0) {
                case u.extraLargeWidth:
                  return o.ExtraLarge;
                case u.largeWidth:
                  return o.Large;
                case u.mediumWidth:
                  return o.Medium;
                case u.smallWidth:
                  return o.Small;
                case u.extraSmallWidth:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(u),
            c = ((u) => {
              switch (!0) {
                case u.extraLargeHeight:
                  return s.ExtraLarge;
                case u.largeHeight:
                  return s.Large;
                case u.mediumHeight:
                  return s.Medium;
                case u.smallHeight:
                  return s.Small;
                case u.extraSmallHeight:
                  return s.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), s.ExtraSmall);
              }
            })(u);
          return {
            mediaSize: a,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: e,
            remScreenHeight: t,
          };
        };
      },
      4419: (u, e, t) => {
        "use strict";
        t.d(e, { y: () => a });
        var r = t(8045),
          n = t(6179);
        const a = (u, e, t = !0) => {
          const a = (0, n.useCallback)(
            (u) => {
              const t = u[0];
              e && e(t);
            },
            [e],
          );
          (0, n.useEffect)(() => {
            if (!u.current || !t) return;
            const e = new r.Z((u) => a(u));
            return (
              e.observe(u.current),
              () => {
                e.disconnect();
              }
            );
          }, [a, t, u]);
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
      9480: (u, e, t) => {
        "use strict";
        t.d(e, { UI: () => r });
        function r(u, e) {
          return Array.isArray(u)
            ? u.map(e)
            : u.map((u, t, r) => e(null == u ? void 0 : u.value, t, r));
        }
      },
      7727: (u, e, t) => {
        "use strict";
        function r(u) {
          engine.call("PlaySound", u);
        }
        t.d(e, { $: () => n, G: () => r });
        const n = {
          playHighlight() {
            r("highlight");
          },
          playClick() {
            r("play");
          },
          playYes() {
            r("yes1");
          },
        };
      },
      3649: (u, e, t) => {
        "use strict";
        let r;
        function n(u, e) {
          return u.replace(/(\{|%\()\w+(\}|\)s)/g, (u) => {
            const t = 0 === u.indexOf("%") ? 2 : 1;
            return String(e[u.slice(t, -t)]);
          });
        }
        function a(u) {
          return u[0].toUpperCase() + u.slice(1);
        }
        (t.d(e, { Eg: () => o, Uw: () => A, e: () => a, uF: () => n, v2: () => r, z4: () => i }),
          (function (u) {
            ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
          })(r || (r = {})));
        const i = (u) => u.replace(/&nbsp;/g, " "),
          o = (u) => u.replace(/&zwnbsp;/g, "\ufeff"),
          s = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          l = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          c = (u, e, t = r.left) => u.split(e).reduce(t === r.left ? s : l, []),
          E = (() => {
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
          _ = ["zh_cn", "zh_sg", "zh_tw"],
          d = (u, e = r.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return _.includes(t)
              ? E(u)
              : ((u, e = r.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = i(u);
                  return (c(a, /( )/, e).forEach((u) => (t = t.concat(c(u, n, r.left)))), t);
                })(u, e);
          },
          A = (u, e, t) =>
            u.split(/%\((.*?)\)(?:[sd])?/g).map((u) => (t && u in t ? t[u] : d(u, e)));
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
        t.d(e, { Sw: () => a.Z, B3: () => l, Z5: () => i, B0: () => s, ry: () => C, Eu: () => B });
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
        var d = t(5521),
          A = t(3138);
        const F = ["args"];
        function D(u, e, t, r, n, a, i) {
          try {
            var o = u[a](i),
              s = o.value;
          } catch (u) {
            return void t(u);
          }
          o.done ? e(s) : Promise.resolve(s).then(r, n);
        }
        const m = (u) => ({
            __Type: "GFBoundingBox",
            x: u.x,
            y: u.y,
            width: u.width,
            height: u.height,
          }),
          C = (function () {
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
                    function i(u) {
                      D(a, r, n, i, o, "next", u);
                    }
                    function o(u) {
                      D(a, r, n, i, o, "throw", u);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          B = () =>
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
                })(e, F);
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
          h = () => g(s.CLOSE),
          p = (u, e) => {
            u.keyCode === d.n.ESCAPE && e();
          };
        var b = t(7572);
        const f = n.instance,
          v = {
            DataTracker: a.Z,
            ViewModel: b.Z,
            ViewEventType: s,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: _,
            makeGlobalBoundingBox: m,
            sendMoveEvent: (u) => g(s.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: h,
            sendClosePopOverEvent: () => g(s.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (u, e, t = 0) => {
              g(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, r, n = R.invalid("resId"), a) => {
              const i = A.O.view.getViewGlobalPosition(),
                o = t.getBoundingClientRect(),
                l = o.x,
                c = o.y,
                E = o.width,
                _ = o.height,
                d = {
                  x: A.O.view.pxToRem(l) + i.x,
                  y: A.O.view.pxToRem(c) + i.y,
                  width: A.O.view.pxToRem(E),
                  height: A.O.view.pxToRem(_),
                };
              g(s.POP_OVER, {
                isMouseEvent: !0,
                contentID: u,
                decoratorID: r || R.invalid("resId"),
                targetID: n,
                direction: e,
                bbox: m(d),
                on: !0,
                args: a,
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
              p(u, h);
            },
            handleViewEvent: g,
            onBindingsReady: C,
            onLayoutReady: B,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
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
            ClickOutsideManager: f,
            SystemLocale: i,
            UserLocale: o,
          };
        window.ViewEnvHelper = v;
      },
      3618: (u, e, t) => {
        "use strict";
        t.d(e, { w: () => d });
        var r = t(6483),
          n = t.n(r),
          a = t(3415),
          i = t(4419),
          o = t(6179),
          s = t.n(o),
          l = t(6143),
          c = t(3310),
          E = t(131),
          _ = t(9053);
        const d = s().memo(
          ({
            text: u,
            classMix: e,
            onSizeChanged: t,
            binding: r,
            isTooltipEnable: d = !1,
            isTruncationAvailable: A = !1,
            targetId: F,
            justifyContent: D = _.v2.FlexStart,
            alignContent: m = _.v2.FlexStart,
            truncateIdentify: C = _.YA,
          }) => {
            const B = (0, o.useRef)(null),
              g = (0, o.useRef)({ height: 0, width: 0 }),
              h = (0, o.useState)({ elementList: [], isTruncated: !1, isTruncateFinished: !1 }),
              p = h[0],
              b = h[1],
              f = (0, o.useMemo)(() => (0, c.s)(u, r), [r, u]),
              v = (0, o.useMemo)(() => {
                if (d && p.isTruncated)
                  return {
                    args: { text: u, stringifyKwargs: r ? JSON.stringify(r) : "" },
                    contentId: R.views.lobby.common.tooltips.ExtendedTextTooltip("resId"),
                    targetId: F,
                  };
              }, [r, d, F, u, p.isTruncated]),
              w = (0, o.useCallback)(
                (u) => {
                  ((g.current.width = u.contentRect.width),
                    (g.current.height = u.contentRect.height));
                  const e = (0, E.T)(B, f, g.current, C),
                    r = e[0],
                    n = e[1];
                  (b({ elementList: r, isTruncated: n, isTruncateFinished: !0 }), t && t(n));
                },
                [t, C, f],
              ),
              x = (0, o.useMemo)(() => ({ justifyContent: D, alignContent: m }), [m, D]);
            return (
              (0, i.y)(B, w, A),
              s().createElement(
                "div",
                {
                  className: n()(
                    l.Z.base,
                    e,
                    l.Z.base__zeroPadding,
                    A && l.Z.base__isTruncationAvailable,
                  ),
                  style: x,
                },
                s().createElement("div", { className: l.Z.unTruncated, ref: B }, f),
                s().createElement(
                  a.l,
                  { tooltipArgs: v },
                  s().createElement(
                    "div",
                    {
                      className: n()(
                        l.Z.truncated,
                        !p.isTruncateFinished && A && l.Z.truncated__hide,
                      ),
                      style: x,
                    },
                    p.isTruncateFinished && A ? p.elementList : f,
                  ),
                ),
              )
            );
          },
        );
      },
      3310: (u, e, t) => {
        "use strict";
        t.d(e, { s: () => E });
        var r = t(3649),
          n = t(6799),
          a = t(6960),
          i = t(9053);
        const o = (u) => {
            const e = /[\s\u002d]/g;
            let t = e.exec(u);
            if (!t) return [u];
            const r = [];
            let n = 0;
            for (; t;) (r.push(u.slice(n, e.lastIndex)), (n = e.lastIndex), (t = e.exec(u)));
            return (n !== u.length && r.push(u.slice(n)), r);
          },
          s = (u, e = "") => {
            const t = [];
            return (
              (0, a.Z)(
                u,
                /(\n+|[\xa0\ufeff]+)/g,
                (u) => {
                  t.push({ blockType: i.kH.Word, colorTag: e, childList: o(u) });
                },
                (u) => {
                  const r = u[0],
                    n = i.aF[r.charAt(0)];
                  n === i.kH.LineBreak
                    ? t.push(
                        ...((u) => {
                          const e = [
                            { blockType: i.kH.LineBreak, colorTag: "", childList: [u.charAt(0)] },
                          ];
                          for (let t = 0; t < u.length - 1; t++)
                            e.push({
                              blockType: i.kH.NewLine,
                              colorTag: "",
                              childList: [u.charAt(0)],
                            });
                          return e;
                        })(r),
                      )
                    : t.push({ blockType: n, colorTag: e, childList: [r] });
                },
              ),
              t
            );
          },
          l = (u, e, t = "") => {
            const r = [];
            return (
              (0, a.Z)(
                u,
                /(?:%\(|{)(.*?)[)}][sd]?/g,
                (u) => {
                  r.push(...s(u, t));
                },
                (u) => {
                  const n = u[1],
                    a = void 0 === e[n] ? u[0] : e[n];
                  "string" == typeof a || "number" == typeof a
                    ? r.push(...s(String(a), t))
                    : r.push({ blockType: i.kH.Binding, colorTag: t, childList: [a] });
                },
              ),
              r
            );
          },
          c = (u, e) => {
            if (!u) return [e];
            const t = [],
              r = Object.assign({}, e, { childList: e.childList.splice(0, 1) });
            if (u.blockType === i.kH.NoBreakWrapper) (u.childList.push(r), t.push(u));
            else {
              const e = Object.assign({}, u, { childList: u.childList.splice(-1) });
              (u.childList.length > 0 && t.push(u),
                t.push({ blockType: i.kH.NoBreakWrapper, colorTag: "", childList: [e, r] }));
            }
            return (e.childList.length > 0 && t.push(e), t);
          },
          E = (u, e = {}) => {
            if (!u) return [];
            const t = ((u) => {
              const e = [];
              let t = !1;
              return (
                u.forEach((u) => {
                  u.blockType === i.kH.NoBreakSymbol
                    ? ((t = !0), e.push(...c(e.pop(), u)))
                    : (t ? e.push(...c(e.pop(), u)) : e.push(u), (t = !1));
                }),
                e
              );
            })(
              ((u, e) => {
                const t = [];
                return (
                  (0, a.Z)(
                    u,
                    /(?:%\(|{)(\w*)(?:_[Oo]pen|_Start)(?:\)s|})([\s\S]*?)(?:%\(|{)\w*(?:_[Cc]lose|_End)(?:\)s|})/g,
                    (u) => {
                      t.push(...l(u, e));
                    },
                    (u) => {
                      t.push(...l(u[2], e, u[1]));
                    },
                  ),
                  t
                );
              })((0, r.Eg)((0, r.z4)(u)), e),
            );
            return (0, n.w)(t);
          };
      },
      6799: (u, e, t) => {
        "use strict";
        t.d(e, { w: () => i });
        var r = t(597),
          n = t(9053);
        const a = (u, e, t) => {
            const i = [];
            return (
              u.childList.forEach((o, s) => {
                const l = `${t}_${s}`;
                if ((0, n.dz)(o)) {
                  const u = o,
                    e = u.blockType,
                    t = r.IY[e],
                    n = a(u, t, l);
                  i.push(...n);
                } else i.push(e({ elementList: [o], textBlock: u, key: l }));
              }),
              i
            );
          },
          i = (u) => {
            const e = [];
            return (
              u.forEach((u, t) => {
                e.push(
                  ...((u, e) => {
                    const t = [],
                      i = u.blockType,
                      o = r.IY[i],
                      s = a(u, o, e);
                    return (
                      i === n.kH.NoBreakWrapper
                        ? t.push(o({ elementList: s, textBlock: u, key: `${e}` }))
                        : t.push(...s),
                      t
                    );
                  })(u, t),
                );
              }),
              e
            );
          };
      },
      6960: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = (u, e, t, r) => {
          let n = e.exec(u),
            a = 0;
          for (; n;)
            (a !== n.index && t(u.slice(a, n.index)), r(n), (a = e.lastIndex), (n = e.exec(u)));
          a !== u.length && t(u.slice(a));
        };
      },
      131: (u, e, t) => {
        "use strict";
        t.d(e, { T: () => c });
        var r = t(6179),
          n = t.n(r),
          a = t(9053);
        const i = (u, e) => !u || u.offsetTop + u.offsetHeight > e,
          o = (u, e) => u.offsetLeft + u.offsetWidth - e,
          s = (u, e, t) => {
            if (!u || !u.textContent) return [!1, 0];
            if (u.offsetLeft > e) return [!1, 0];
            const r = o(u, e),
              n = u.textContent.length,
              a = u.offsetWidth / n,
              i = Math.ceil(r / a);
            if (r > 0) {
              const r = Math.floor((e - u.offsetLeft) / a);
              return r >= t ? [!0, t + i] : [!1, r];
            }
            const s = Math.max(t + i, 0);
            return n < s ? [!1, 0] : [!0, s];
          },
          l = (u, e, t, r, i, o) => {
            let c = -1,
              E = null;
            for (let _ = t; _ >= 0; _--) {
              const t = u[_],
                d = Number(u[_].getAttribute(a.bF));
              if (d === a.kH.LineBreak || d === a.kH.NewLine || d === a.kH.Binding) continue;
              const A = t.textContent || "";
              if (!(t.childElementCount > 1)) {
                const u = s(t, r, i),
                  a = u[0],
                  l = u[1];
                if (!a) {
                  l > 0 && (i -= l);
                  continue;
                }
                const d = A.slice(0, A.length - l) + o,
                  F = e[_];
                ((E = n().cloneElement(F, F.props, d)), (c = _));
                break;
              }
              {
                const u = t.children,
                  a = e[_],
                  s = a.props.children,
                  d = l(u, s, u.length - 1, r, i, o),
                  F = d[0],
                  D = d[1];
                if (!(F < 0)) {
                  const u = s.slice(0, F);
                  ((E = n().cloneElement(a, a.props, u, D)), (c = _));
                  break;
                }
                i -= A.length;
              }
            }
            return [c, E];
          },
          c = (u, e, t, r = a.YA) => {
            const n = [...e],
              s = u.current;
            if (!s) return [n, !1];
            const c = t.height,
              E = t.width,
              _ = s.lastElementChild;
            if (!i(_, c) && o(_, E) <= 0) return [n, !1];
            const d = s.children,
              A = ((u, e) => {
                let t = 0,
                  r = u.length - 1;
                for (; r - t >= 0;) {
                  const n = t + Math.ceil(0.5 * (r - t));
                  i(u[n], e) ? (r = n - 1) : (t = n + 1);
                }
                return t - 1;
              })(d, c);
            if (A < 0) return [n, !1];
            const F = l(d, n, A, E, r.length, r),
              D = F[0],
              m = F[1];
            return (m && (n.splice(D, 1, m), n.splice(D + 1)), [n, !0]);
          };
      },
      9053: (u, e, t) => {
        "use strict";
        let r, n, a;
        (t.d(e, { YA: () => o, aF: () => l, bF: () => s, dz: () => i, kH: () => r, v2: () => n }),
          (function (u) {
            ((u[(u.Word = 0)] = "Word"),
              (u[(u.LineBreak = 1)] = "LineBreak"),
              (u[(u.NewLine = 2)] = "NewLine"),
              (u[(u.NoBreakSymbol = 3)] = "NoBreakSymbol"),
              (u[(u.NoBreakWrapper = 4)] = "NoBreakWrapper"),
              (u[(u.Binding = 5)] = "Binding"));
          })(r || (r = {})),
          (function (u) {
            ((u.FlexStart = "flex-start"), (u.Center = "center"), (u.FlexEnd = "flex-end"));
          })(n || (n = {})),
          (function (u) {
            ((u.NBSP = " "), (u.ZWNBSP = "\ufeff"), (u.NEW_LINE = "\n"));
          })(a || (a = {})));
        const i = (u) => void 0 !== u.childList,
          o = "...",
          s = "data-block-type",
          l = { [a.NBSP]: r.NoBreakSymbol, [a.ZWNBSP]: r.NoBreakSymbol, [a.NEW_LINE]: r.LineBreak };
      },
      597: (u, e, t) => {
        "use strict";
        t.d(e, { IY: () => c });
        var r = t(6179),
          n = t.n(r),
          a = t(9053),
          i = t(9627),
          o = t(7629);
        const s = (u) => ({ color: `#${u}` }),
          l = ({ elementList: u, textBlock: e, key: t }) => {
            const r = e.colorTag;
            return r
              ? i.Z[r]
                ? n().createElement(
                    "span",
                    { key: t, "data-block-type": e.blockType, className: i.Z[r] },
                    u,
                  )
                : n().createElement(
                    "span",
                    { key: t, "data-block-type": e.blockType, style: s(r) },
                    u,
                  )
              : n().createElement("span", { key: t, "data-block-type": e.blockType }, u);
          },
          c = {
            [a.kH.Word]: l,
            [a.kH.NoBreakSymbol]: l,
            [a.kH.Binding]: ({ elementList: u, textBlock: e, key: t }) =>
              n().createElement(
                "span",
                { key: t, "data-block-type": e.blockType },
                u.map((u) => n().createElement(n().Fragment, { key: t }, u)),
              ),
            [a.kH.LineBreak]: ({ key: u }) =>
              n().createElement("span", {
                key: u,
                "data-block-type": a.kH.LineBreak,
                className: o.Z.lineBreak,
              }),
            [a.kH.NewLine]: ({ elementList: u, key: e }) =>
              n().createElement(
                "span",
                { key: e, "data-block-type": a.kH.NewLine, className: o.Z.newLine },
                u,
              ),
            [a.kH.NoBreakWrapper]: ({ elementList: u, key: e }) =>
              n().createElement(
                "span",
                { key: e, "data-block-type": a.kH.NoBreakWrapper, className: o.Z.noBreakWrapper },
                u,
              ),
          };
      },
      5298: (u, e, t) => {
        "use strict";
        t.d(e, { l: () => n });
        var r = t(776);
        const n = (u, e) => ({
          isEnabled: u !== r.f.absent,
          args: e,
          contentId: R.views.dialogs.common.DialogTemplateGenericTooltip("resId"),
          decoratorId:
            u === r.f.normal
              ? R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId")
              : void 0,
          ignoreShowDelay: u === r.f.backport,
          ignoreMouseClick: !0,
        });
      },
      8018: (u, e, t) => {
        "use strict";
        t.d(e, { T3: () => a });
        var r = t(3649);
        const n = R.strings.common.percentValue(),
          a = (u) => (0, r.uF)(n, { value: u });
        let i;
        !(function (u) {
          ((u.Objective = "objective"), (u.Possessive = "possessive"));
        })(i || (i = {}));
        (R.strings.crew.filterPanel.counter.reset.header(),
          R.strings.crew.filterPanel.counter.reset.body(),
          R.strings.crew.filterPanel.counterMultySelect.reset.header(),
          R.strings.crew.filterPanel.counterMultySelect.reset.body());
        let o;
        !(function (u) {
          ((u.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (u.SHOP_INFO = "shop_info"),
            (u.RUDY = "rudy"));
        })(o || (o = {}));
      },
      7442: (u, e, t) => {
        "use strict";
        var r = t(7739),
          n = t(6179),
          a = t.n(n),
          i = t(6483),
          o = t.n(i),
          s = t(926),
          l = t.n(s),
          c = t(5415);
        const E = ["children", "className"];
        function _() {
          return (
            (_ =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            _.apply(this, arguments)
          );
        }
        const d = {
            [c.fd.ExtraSmall]: "",
            [c.fd.Small]: l().SMALL_WIDTH,
            [c.fd.Medium]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH}`,
            [c.fd.Large]: `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH}`,
            [c.fd.ExtraLarge]:
              `${l().SMALL_WIDTH} ${l().MEDIUM_WIDTH} ${l().LARGE_WIDTH} ${l().EXTRA_LARGE_WIDTH}`,
          },
          A = {
            [c.Aq.ExtraSmall]: "",
            [c.Aq.Small]: l().SMALL_HEIGHT,
            [c.Aq.Medium]: `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT}`,
            [c.Aq.Large]: `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT} ${l().LARGE_HEIGHT}`,
            [c.Aq.ExtraLarge]:
              `${l().SMALL_HEIGHT} ${l().MEDIUM_HEIGHT} ${l().LARGE_HEIGHT} ${l().EXTRA_LARGE_HEIGHT}`,
          },
          F = {
            [c.cJ.ExtraSmall]: "",
            [c.cJ.Small]: l().SMALL,
            [c.cJ.Medium]: `${l().SMALL} ${l().MEDIUM}`,
            [c.cJ.Large]: `${l().SMALL} ${l().MEDIUM} ${l().LARGE}`,
            [c.cJ.ExtraLarge]: `${l().SMALL} ${l().MEDIUM} ${l().LARGE} ${l().EXTRA_LARGE}`,
          },
          D = (u) => {
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
              })(u, E);
            const n = (0, c.GS)(),
              i = n.mediaWidth,
              s = n.mediaHeight,
              l = n.mediaSize;
            return a().createElement("div", _({ className: o()(t, d[i], A[s], F[l]) }, r), e);
          },
          m = ["children"];
        const C = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, m);
          return a().createElement(r.ZN, null, a().createElement(D, t, e));
        };
        var B = t(493),
          g = t.n(B);
        var h = t(3649);
        let p;
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
        })(p || (p = {}));
        var b = t(4179);
        Date.now();
        var f = t(3138);
        var v = t(7902);
        const w = (u, e) => u.split(".").reduce((u, e) => u && u[e], e);
        var x = t(6536);
        const y = (u) => u && "ArrayItem" === u.__proto__.constructor.name,
          T = (u, e) => (u.length > 0 ? `${u}.${e}` : e),
          L = (u) =>
            ((u, e) =>
              u.split(".").reduce((u, t) => {
                const r = w(`${u}.${t}`, window);
                return y(r) ? e(u, t, r) : `${u}.${t}`;
              }))(u, (u, e) => `${u}.${e}.value`),
          S = (u) => {
            const e = ((u) => {
                const e = (0, v.F)(),
                  t = e.caller,
                  r = e.resId,
                  n = window.__feature && window.__feature !== t && t ? `subViews.${t}` : "";
                return { modelPrefix: n, modelPath: T(n, u || ""), resId: r };
              })(),
              t = e.modelPrefix,
              r = u.split(".");
            if (r.length > 0) {
              const u = [r[0]];
              return (
                r.reduce((e, r) => {
                  const n = w(T(t, `${e}.${r}`), window);
                  return y(n) ? (u.push(n.id), `${e}.${r}.value`) : (u.push(r), `${e}.${r}`);
                }),
                u.reduce((u, e) => u + "." + e)
              );
            }
            return "";
          },
          k = b.Sw.instance;
        let M;
        !(function (u) {
          ((u.None = "None"), (u.Shallow = "Shallow"), (u.Deep = "Deep"));
        })(M || (M = {}));
        const O = (u = "model", e = M.Deep) => {
          const t = (0, n.useState)(0),
            r = (t[0], t[1]),
            a = (0, n.useMemo)(() => (0, v.F)(), []),
            i = a.caller,
            o = a.resId,
            s = (0, n.useMemo)(
              () => (window.__feature && window.__feature !== i ? `subViews.${i}.${u}` : u),
              [i, u],
            ),
            l = (0, n.useState)(() =>
              ((u) => {
                const e = w(u, window);
                for (const u in e) "function" == typeof e[u] && (e[u] = e[u].bind(e));
                return y(e) ? e.value : e;
              })(L(s)),
            ),
            c = l[0],
            E = l[1],
            _ = (0, n.useRef)(-1);
          return (
            (0, x.Z)(() => {
              if (
                ("boolean" == typeof e &&
                  ((e = e ? M.Deep : M.None),
                  console.warn(
                    'Boolean key for useModel "tracking" param is deprecated. Use ModelTracking enum values instead!',
                  )),
                e !== M.None)
              ) {
                const t = (u) => {
                    ((u) => u && "CoherentArrayProxy" === u.__proto__.constructor.name)(u) &&
                    e === M.Deep
                      ? (u === c && r((u) => u + 1), E(u))
                      : E(Object.assign([], u));
                  },
                  n = S(u);
                _.current = k.addCallback(n, t, o, e === M.Deep);
              }
            }),
            (0, n.useEffect)(() => {
              if (e !== M.None)
                return () => {
                  k.removeCallback(_.current, o);
                };
            }, [o, e]),
            c
          );
        };
        b.Sw.instance;
        var N = t(5521);
        const H = (u) => {
          console.error(u.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function P(u = N.n.NONE, e = H, t = !1) {
          (0, n.useEffect)(() => {
            if (u !== N.n.NONE)
              return (
                window.addEventListener("keydown", r, t),
                () => {
                  window.removeEventListener("keydown", r, t);
                }
              );
            function r(r) {
              if (r.keyCode === u) {
                if (f.O.view.isEventHandled()) return;
                (f.O.view.setEventHandled(), e(r), t && r.stopPropagation());
              }
            }
          }, [e, u, t]);
        }
        const I = /<link.*?>/g,
          W = /\.\.\//g,
          j = /<script.*?>/g,
          G = "default.css",
          U = (u) => {
            const e = u.match(W);
            return e && e.join("");
          },
          $ = () => {
            for (
              var u = 0, e = Array.from(document.head.querySelectorAll('link[rel="stylesheet"]'));
              u < e.length;
              u++
            ) {
              const t = e[u];
              if (!t.href.includes(G)) return t.href;
            }
            return "";
          },
          V = (u, e) => {
            const t = $(),
              r = U(t);
            let n,
              a = u;
            for (; null !== (n = j.exec(u));) {
              const u = n[0].match(/<script (defer|defer="defer") src="(.*?)">/);
              if (u) {
                const t = r + u[2].replace(W, "");
                ((a = a.replace(u[2], t)),
                  (a = a.replace('<div id="root"', `<div data-root-id=${e} id="root"`)));
              }
            }
            return a;
          },
          X = "SubView_base_df",
          q = "subViews.onChanged",
          Y = (() => {
            const u = [];
            let e = !1;
            const t = () => {
              if (!u.length) return void (e = !1);
              const r = u.shift();
              r && ((e = !0), r().then(() => t()));
            };
            return {
              add: (r) => {
                (u.push(r), e || t());
              },
            };
          })(),
          z = (0, n.memo)(({ id: u, fallback: e, onLoadCallback: t, mixClass: r }) => {
            const i = (0, n.useState)(""),
              s = i[0],
              l = i[1],
              c = (0, n.useMemo)(() => ({ __html: V(s, u) }), [s, u]),
              E = (0, n.useMemo)(() => window.subViews.addChildChangedCallback(u), [u]),
              _ = (0, n.useState)(!1),
              d = _[0],
              A = _[1],
              F = (0, n.useCallback)(
                (u) => {
                  u.includes(E) &&
                    (A(!0), engine.off(q, F), window.subViews.removeChildChangedCallback(E));
                },
                [E],
              ),
              D = (0, n.useCallback)((u) => {
                Y.add(
                  () =>
                    new Promise((e) => {
                      l(u);
                      const t = new MutationObserver(() => {
                          (t.disconnect(), e());
                        }),
                        r = document.getElementById("root");
                      r && t.observe(r, { childList: !0 });
                    }),
                );
              }, []);
            ((0, n.useEffect)(() => {
              if (window.subViews.ids().includes(u)) {
                const e = window.subViews.get(u),
                  t = e.path;
                let r;
                if ((r = t.split("/").pop()))
                  return (
                    (r = r.split(".")[0]),
                    (window.subViews[r] = Object.assign({ id: u }, e)),
                    engine.on(`subView:inject->${r}`, D),
                    (({ path: u, name: e }) => {
                      const t = new XMLHttpRequest();
                      ((t.onreadystatechange = () => {
                        4 === t.readyState &&
                          (200 === t.status
                            ? (0, b.Eu)().then(() => {
                                (console.info(`Sub view ${e} loaded: ${u}`),
                                  engine.TriggerEvent(`subView:inject->${e}`, t.responseText));
                              })
                            : console.error(`subView: status: ${t.status} - can't get bundle`));
                      }),
                        t.open("GET", u),
                        t.send());
                    })({ name: r, path: t }),
                    () => {
                      (r && window.subViews[r] && delete window.subViews[r],
                        engine.trigger("subView:destroy", { viewName: r, viewId: u }),
                        window.__dataTracker &&
                          window.__dataTracker.clearViewCallbacks &&
                          window.__dataTracker.clearViewCallbacks(u),
                        engine.off(`subView:inject->${r}`, D),
                        console.info(`Sub view ${r} is destroyed: ${t}`));
                    }
                  );
                console.error("subView: can't get View component name");
              } else engine.on(q, F);
            }, [F, D, u, d]),
              (0, n.useEffect)(
                () => () => {
                  s &&
                    ((u) => {
                      const e = U($());
                      let t;
                      for (; null !== (t = I.exec(u));) {
                        const u = t[0].match(/href="(.*?)"/);
                        if (u) {
                          const t = e + u[1].replace(W, ""),
                            r = document.head.querySelector(`[href="${t}"]`);
                          r && document.head.removeChild(r);
                        }
                      }
                    })(s);
                },
                [s],
              ));
            const m = o()(X, r);
            if (s) {
              let e;
              return (
                (e = document.getElementById("root")) && e.setAttribute("id", "bugSubView"),
                ((u) => {
                  let e;
                  const t = $(),
                    r = U(t);
                  for (; null !== (e = I.exec(u));) {
                    const u = e[0].match(/href="(.*?)"/);
                    if (u && !u[1].includes(G) && r) {
                      const e = r + u[1].replace(W, ""),
                        t = document.createElement("link");
                      ((t.href = e), (t.rel = "stylesheet"), document.head.appendChild(t));
                    }
                  }
                })(s),
                t && t(u),
                a().createElement("div", { className: m, dangerouslySetInnerHTML: c })
              );
            }
            return e
              ? a().createElement("div", { className: m }, a().createElement(e, null))
              : null;
          });
        var K = t(7727);
        const Z = {
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
        let J, Q;
        (!(function (u) {
          ((u.main = "main"),
            (u.primary = "primary"),
            (u.primaryGreen = "primaryGreen"),
            (u.primaryRed = "primaryRed"),
            (u.secondary = "secondary"),
            (u.ghost = "ghost"));
        })(J || (J = {})),
          (function (u) {
            ((u.extraSmall = "extraSmall"), (u.small = "small"), (u.medium = "medium"));
          })(Q || (Q = {})));
        const uu = ({
          children: u,
          size: e,
          isFocused: t,
          type: r,
          disabled: i,
          mixClass: s,
          soundHover: l,
          soundClick: c,
          onMouseEnter: E,
          onMouseMove: _,
          onMouseDown: d,
          onMouseUp: A,
          onMouseLeave: F,
          onClick: D,
        }) => {
          const m = (0, n.useRef)(null),
            C = (0, n.useState)(t),
            B = C[0],
            g = C[1],
            h = (0, n.useState)(!1),
            p = h[0],
            b = h[1],
            f = (0, n.useState)(!1),
            v = f[0],
            w = f[1],
            x = (0, n.useCallback)(() => {
              i || (m.current && (m.current.focus(), g(!0)));
            }, [i]),
            y = (0, n.useCallback)(
              (u) => {
                B && null !== m.current && !m.current.contains(u.target) && g(!1);
              },
              [B],
            ),
            T = (0, n.useCallback)(
              (u) => {
                i || (D && D(u));
              },
              [i, D],
            ),
            L = (0, n.useCallback)(
              (u) => {
                i || (null !== l && (0, K.G)(l), E && E(u), w(!0));
              },
              [i, l, E],
            ),
            S = (0, n.useCallback)(
              (u) => {
                _ && _(u);
              },
              [_],
            ),
            k = (0, n.useCallback)(
              (u) => {
                i || (A && A(u), b(!1));
              },
              [i, A],
            ),
            M = (0, n.useCallback)(
              (u) => {
                i || (null !== c && (0, K.G)(c), d && d(u), t && x(), b(!0));
              },
              [i, c, d, x, t],
            ),
            O = (0, n.useCallback)(
              (u) => {
                i || (F && F(u), b(!1));
              },
              [i, F],
            ),
            N = o()(
              Z.base,
              Z[`base__${r}`],
              {
                [Z.base__disabled]: i,
                [Z[`base__${e}`]]: e,
                [Z.base__focus]: B,
                [Z.base__highlightActive]: p,
                [Z.base__firstHover]: v,
              },
              s,
            ),
            H = o()(Z.state, Z.state__default);
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
              g(t);
            }, [t]),
            a().createElement(
              "div",
              {
                ref: m,
                className: N,
                onMouseEnter: L,
                onMouseMove: S,
                onMouseUp: k,
                onMouseDown: M,
                onMouseLeave: O,
                onClick: T,
              },
              r !== J.ghost &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: Z.back }),
                  a().createElement("span", { className: Z.texture }),
                ),
              a().createElement(
                "span",
                { className: H },
                a().createElement("span", { className: Z.stateDisabled }),
                a().createElement("span", { className: Z.stateHighlightHover }),
                a().createElement("span", { className: Z.stateHighlightActive }),
              ),
              a().createElement(
                "span",
                { className: Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
                u,
              ),
            )
          );
        };
        uu.defaultProps = {
          type: J.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const eu = (0, n.memo)(uu);
        var tu = t(6373);
        const ru = "TextOverflow_base_3b",
          nu = ({ content: u, classMix: e }) => {
            const t = (0, n.useRef)(null),
              r = (0, n.useState)(!0),
              i = r[0],
              s = r[1];
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
                  u && u.offsetWidth >= u.scrollWidth && s(!1);
                }),
              ),
              a().createElement(
                tu.i,
                { isEnabled: i, body: u },
                a().createElement("div", { ref: t, className: o()(ru, e) }, u),
              )
            );
          };
        var au = t(2056),
          iu = t(776),
          ou = t(5298);
        const su = "DialogTemplateButton_base_0b",
          lu = "DialogTemplateButton_label_83",
          cu = "DialogTemplateButton_label__noTooltip_14",
          Eu = (0, n.memo)(
            ({
              onClick: u,
              isFocused: e,
              buttonID: t,
              isDisabled: r,
              label: i,
              tooltip: s,
              type: l,
            }) => {
              const c = (0, n.useCallback)(() => {
                  u({ buttonID: t });
                }, [u, t]),
                E = (0, n.useCallback)(
                  (u) => {
                    u.altKey || !e || r || c();
                  },
                  [e, r, c],
                );
              P(N.n.ENTER, E);
              const _ = (0, n.useMemo)(() => (0, ou.l)(s.type, { buttonID: t }), [s.type, t]),
                d = o()(lu, s.type !== iu.f.absent && cu);
              return a().createElement(
                au.u,
                _,
                a().createElement(
                  "div",
                  { className: su },
                  a().createElement(
                    eu,
                    { size: Q.medium, type: l, disabled: r, onClick: c, isFocused: e },
                    a().createElement(nu, { classMix: d, content: i || "" }),
                  ),
                ),
              );
            },
          ),
          _u = "DialogTemplateButtonList_base_8e";
        function du() {
          return (
            (du =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            du.apply(this, arguments)
          );
        }
        const Au = (0, n.memo)(() => {
            const u = O("model").onButtonClicked,
              e = O("model.focus"),
              t = e.focusedIndex,
              r = e.onTabPressed,
              i = O("model.buttons"),
              o = (0, n.useCallback)(
                (u) => {
                  r({ shift: u.shiftKey });
                },
                [r],
              );
            return (
              P(N.n.TAB, o),
              a().createElement(
                "div",
                { className: _u },
                i.map(({ value: e }, r) =>
                  a().createElement(Eu, du({ key: e.buttonID, isFocused: r === t, onClick: u }, e)),
                ),
              )
            );
          }),
          Fu = "DialogTemplateWrapper_base_f7",
          Du = "DialogTemplateWrapper_base__hidden_5f",
          mu = "DialogTemplateWrapper_subView_30";
        function Cu() {
          return (
            (Cu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Cu.apply(this, arguments)
          );
        }
        const Bu = (0, n.memo)(({ Template: u }) => {
          const e = O("model", M.None),
            t = e.onCloseClicked,
            i = e.placeHolders,
            s = e.background,
            l = e.dimmerAlpha,
            c = e.displayFlags;
          (0, n.useEffect)(() => {
            const u = document.getElementById("root");
            u && u.setAttribute("id", "stubDialogTemplate");
          }, []);
          const E = c.map(({ value: u }) => u),
            _ = (0, n.useRef)(i.map(({ value: u }) => u.resourceID)),
            d = (0, n.useState)(0 !== _.current.length),
            A = d[0],
            F = d[1],
            D = (0, n.useCallback)(
              (u = "default") => {
                t({ reason: u });
              },
              [t],
            ),
            m = (0, n.useCallback)(() => {
              D("escape");
            }, [D]);
          var C;
          ((C = m), P(N.n.ESCAPE, C));
          const B = (0, n.useCallback)((u) => {
              const e = _.current,
                t = e.indexOf(u);
              t > -1 && (e.splice(t, 1), 0 === e.length && F(!1));
            }, []),
            g = (0, n.useMemo)(() => {
              const u = { backgroundColor: `rgba(19, 18, 16, ${l})` };
              return (s && (u.backgroundImage = `url(${s})`), u);
            }, [s, l]),
            h = (0, n.useMemo)(
              () =>
                i.reduce(
                  (u, { value: e }) => (
                    (u[e.placeHolder] = a().createElement(z, {
                      key: e.placeHolder,
                      id: e.resourceID,
                      mixClass: mu,
                      onLoadCallback: B,
                    })),
                    u
                  ),
                  {},
                ),
              [B, i],
            ),
            p = o()(Fu, A && Du);
          return a().createElement(
            r.ZN,
            null,
            a().createElement(
              "div",
              { className: p, style: g },
              a().createElement(
                u,
                Cu(
                  {
                    onClose: D,
                    buttons: a().createElement(Au, null),
                    displayFlags: E,
                    isShown: !A,
                  },
                  h,
                ),
              ),
            ),
          );
        });
        var gu = t(9887),
          hu = t.n(gu);
        const pu = ["xl", "lg", "md", "sm", "xs"],
          bu = (u) => u.includes("_") && ((u) => pu.includes(u))(u.split("_").at(-1)),
          fu = [c.cJ.ExtraLarge, c.cJ.Large, c.cJ.Medium, c.cJ.Small, c.cJ.ExtraSmall],
          vu = (u, e) =>
            Object.keys(u).reduce((t, r) => {
              if (r in t) return t;
              if (bu(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const a = fu.indexOf(e),
                  i = (-1 !== a ? pu.slice(a) : [])
                    .map((u) => n + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  o = i ? u[i] : void 0;
                return ((t[n] = void 0 !== o ? o : u[n]), t);
              }
              const n = u[r];
              return (
                void 0 === n ||
                  ((u, e) => pu.some((t) => void 0 !== e[`${u}_${t}`]))(r, u) ||
                  (t[r] = n),
                t
              );
            }, {}),
          wu = (u, e = vu) => {
            const t = (
              (u, e = vu) =>
              (t) => {
                const r = (0, c.GS)().mediaSize,
                  i = (0, n.useMemo)(() => e(t, r), [t, r]);
                return a().createElement(u, i);
              }
            )(u, e);
            return a().memo((e) =>
              Object.keys(e).some((u) => bu(u) && void 0 !== e[u])
                ? a().createElement(t, e)
                : a().createElement(u, e),
            );
          },
          xu = {
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
          yu = [
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
        Object.keys(hu());
        const Lu = {
            XL: { mt: xu.mt__XL, mr: xu.mr__XL, mb: xu.mb__XL, ml: xu.ml__XL },
            LG: { mt: xu.mt__LG, mr: xu.mr__LG, mb: xu.mb__LG, ml: xu.ml__LG },
            MDp: { mt: xu.mt__MDp, mr: xu.mr__MDp, mb: xu.mb__MDp, ml: xu.ml__MDp },
            MD: { mt: xu.mt__MD, mr: xu.mr__MD, mb: xu.mb__MD, ml: xu.ml__MD },
            SMp: { mt: xu.mt__SMp, mr: xu.mr__SMp, mb: xu.mb__SMp, ml: xu.ml__SMp },
            SM: { mt: xu.mt__SM, mr: xu.mr__SM, mb: xu.mb__SM, ml: xu.ml__SM },
            XS: { mt: xu.mt__XS, mr: xu.mr__XS, mb: xu.mb__XS, ml: xu.ml__XS },
          },
          Su = (Object.keys(Lu), ["mt", "mr", "mb", "ml"]),
          ku = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          Mu = wu((u) => {
            let e = u.className,
              t = u.width,
              r = u.height,
              i = u.m,
              s = u.mt,
              l = void 0 === s ? i : s,
              c = u.mr,
              E = void 0 === c ? i : c,
              _ = u.mb,
              d = void 0 === _ ? i : _,
              A = u.ml,
              F = void 0 === A ? i : A,
              D = u.column,
              m = u.row,
              C = u.flexDirection,
              B = void 0 === C ? (D ? "column" : m && "row") || void 0 : C,
              g = u.flexStart,
              h = u.center,
              p = u.flexEnd,
              b = u.spaceBetween,
              f = u.spaceAround,
              v = u.justifyContent,
              w =
                void 0 === v
                  ? (g ? "flex-start" : h && "center") ||
                    (p && "flex-end") ||
                    (b && "space-between") ||
                    (f && "space-around") ||
                    void 0
                  : v,
              x = u.alignItems,
              y =
                void 0 === x
                  ? (g ? "flex-start" : h && "center") || (p && "flex-end") || void 0
                  : x,
              T = u.alignSelf,
              L = u.wrap,
              S = u.flexWrap,
              k = void 0 === S ? (L ? "wrap" : void 0) : S,
              M = u.grow,
              O = u.shrink,
              R = u.flex,
              N = void 0 === R ? (M || O ? `${M ? 1 : 0} ${O ? 1 : 0} auto` : void 0) : R,
              H = u.style,
              P = u.children,
              I = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, yu);
            const W = (0, n.useMemo)(() => {
                const u = { mt: l, mr: E, mb: d, ml: F },
                  e = ((u) =>
                    Su.reduce((e, t) => {
                      const r = u[t];
                      return r && "number" != typeof r ? e.concat(Lu[!0 === r ? "MD" : r][t]) : e;
                    }, []))(u),
                  n = ((u) =>
                    Su.reduce((e, t) => {
                      const r = u[t];
                      return ("number" == typeof r && (e[ku[t]] = r + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, H, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: N,
                    alignSelf: T,
                    display: B || y ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: k,
                    justifyContent: w,
                    alignItems: y,
                  }),
                  computedClassNames: e,
                };
              }, [t, r, l, E, d, F, H, N, T, B, k, w, y]),
              j = W.computedStyle,
              G = W.computedClassNames;
            return a().createElement(
              "div",
              Tu({ className: o()(xu.base, ...G, e), style: j }, I),
              P,
            );
          }),
          Ou = "FormatText_base_d0",
          Ru = ({ binding: u, text: e = "", classMix: t, alignment: r = h.v2.left }) =>
            null === e
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  n.Fragment,
                  null,
                  e.split("\n").map((e, i) =>
                    a().createElement(
                      "div",
                      { className: o()(Ou, t), key: `${e}-${i}` },
                      (0, h.Uw)(e, r, u).map((u, e) =>
                        a().createElement(n.Fragment, { key: `${e}-${u}` }, u),
                      ),
                    ),
                  ),
                );
        var Nu = t(3532),
          Hu = t.n(Nu);
        const Pu = {
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
          Iu = [
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
        function Wu() {
          return (
            (Wu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Wu.apply(this, arguments)
          );
        }
        Object.keys(hu());
        const ju = Object.keys(Hu()),
          Gu = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          Uu = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          $u = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Vu = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          Xu =
            (Object.keys(Vu),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": Gu,
              "heading-H36": Gu,
              "heading-H28": Uu,
              "heading-H24": Uu,
              "heading-H24R": Uu,
              "heading-H22": Uu,
              "heading-H20R": Uu,
              "heading-H18": Uu,
              "heading-H15": $u,
              "heading-H14": $u,
              "paragraph-P24": Uu,
              "paragraph-P18": Uu,
              "paragraph-P16": Uu,
              "paragraph-P14": $u,
              "paragraph-P12": $u,
              "paragraph-P10": $u,
            }),
          qu =
            (Object.keys(Xu),
            (u) =>
              u
                ? ((u) => ju.includes(u))(u)
                  ? { colorClassName: Pu[u] }
                  : { colorStyle: { color: u } }
                : {}),
          Yu = wu((u) => {
            let e = u.text,
              t = u.variant,
              r = u.className,
              i = u.color,
              s = u.m,
              l = u.mt,
              c = void 0 === l ? s : l,
              E = u.mr,
              _ = void 0 === E ? s : E,
              d = u.mb,
              A = void 0 === d ? s : d,
              F = u.ml,
              D = void 0 === F ? s : F,
              m = u.style,
              C = u.format,
              B = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, Iu);
            const g = (0, n.useMemo)(() => {
                const u = qu(i),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, m, r), colorClassName: e };
              }, [m, i]),
              h = g.computedStyle,
              p = g.colorClassName;
            return a().createElement(
              Mu,
              Wu(
                {
                  className: o()(Pu.base, t && Pu[t], p, r),
                  style: h,
                  mt: !0 === c ? Xu[t || "paragraph-P16"].mt : c,
                  mr: !0 === _ ? Xu[t || "paragraph-P16"].mr : _,
                  mb: !0 === A ? Xu[t || "paragraph-P16"].mb : A,
                  ml: !0 === D ? Xu[t || "paragraph-P16"].ml : D,
                },
                B,
              ),
              void 0 !== C ? a().createElement(Ru, Wu({}, C, { text: e })) : e,
            );
          }),
          zu = {
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
          Ku = [
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
        function Zu() {
          return (
            (Zu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Zu.apply(this, arguments)
          );
        }
        class Ju extends a().PureComponent {
          constructor(...u) {
            (super(...u),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (u) => (e) => {
                (u && u(e),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, K.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (u) => (e) => {
                (u && u(e), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (u) => (e) => {
                (u && u(e),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, K.G)(this.props.soundClick));
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
              r = u.goto,
              n = u.side,
              i = u.type,
              s = u.classNames,
              l = u.onMouseEnter,
              c = u.onMouseLeave,
              E = u.onMouseDown,
              _ = u.onMouseUp,
              d =
                (u.soundClick,
                u.soundHover,
                (function (u, e) {
                  if (null == u) return {};
                  var t,
                    r,
                    n = {},
                    a = Object.keys(u);
                  for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                  return n;
                })(u, Ku)),
              A = o()(zu.base, zu[`base__${i}`], zu[`base__${n}`], null == s ? void 0 : s.base),
              F = o()(zu.icon, zu[`icon__${i}`], zu[`icon__${n}`], null == s ? void 0 : s.icon),
              D = o()(zu.glow, null == s ? void 0 : s.glow),
              m = o()(zu.caption, zu[`caption__${i}`], null == s ? void 0 : s.caption),
              C = o()(zu.goto, null == s ? void 0 : s.goto);
            return a().createElement(
              "div",
              Zu(
                {
                  className: A,
                  onMouseEnter: this._onMouseEnter(l),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(E),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                d,
              ),
              "info" !== i && a().createElement("div", { className: zu.shine }),
              a().createElement(
                "div",
                { className: F },
                a().createElement("div", { className: D }),
              ),
              a().createElement("div", { className: m }, e),
              r && a().createElement("div", { className: C }, r),
            );
          }
        }
        let Qu;
        ((Ju.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        }),
          (function (u) {
            ((u.responsiveHeader = "responsiveHeader"),
              (u.responsiveClosePosition = "responsiveClosePosition"),
              (u.disableResponsiveContentPosition = "disableResponsiveContentPosition"));
          })(Qu || (Qu = {})));
        var ue = t(5262);
        function ee(u, e, t) {
          const a = (0, n.useContext)(r.YN);
          let i = Object.entries(a).filter(([u, e]) => !0 === e && u in ue.u);
          return (
            t && (i = i.filter((u) => t.includes(u[0]))),
            u.reduce((u, t) => {
              const r = i.map((u) =>
                o()(e[((u, e) => u + "__" + e)(t, u[0])], e[((u, e) => u + (0, h.e)(e))(t, u[0])]),
              );
              return ((u[t] = o()(e[t], ...r)), u);
            }, {})
          );
        }
        const te = {
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
          re = (0, n.memo)(
            ({
              isShown: u = !0,
              classMix: e,
              onClose: t,
              icon: r,
              topRight: i,
              title: s,
              content: l,
              buttons: c,
              footer: E,
              displayFlags: _,
              classNames: d,
            }) => {
              const A = ((u, e) =>
                  Object.keys(e).reduce((e, t) => ((e[t] = u.includes(t)), e), {}))(_, Qu),
                F = A.responsiveHeader,
                D = A.responsiveClosePosition,
                m = A.disableResponsiveContentPosition,
                C = ee(["base"], te),
                B = (0, n.useCallback)(() => {
                  t && t();
                }, [t]),
                g = o()(C.base, e),
                h = o()(
                  te.center,
                  r && te.center__withIcon,
                  u && te.center__shown,
                  !m && te.center__responsive,
                  null == d ? void 0 : d.center,
                ),
                p = o()(te.icon, F && te.icon__responsive),
                b = o()(te.title, F && te.title__responsive),
                f = o()(te.closeBtn, D && te.closeBtn__responsive),
                v = o()(
                  te.divider,
                  !l && te.divider__noContent,
                  !E && te.divider__noFooter,
                  null == d ? void 0 : d.divider,
                );
              return a().createElement(
                "div",
                { className: g },
                a().createElement(
                  "div",
                  { className: te.topRight },
                  i,
                  a().createElement(
                    "div",
                    { className: f },
                    a().createElement(Ju, {
                      caption: R.strings.menu.viewHeader.closeBtn.label(),
                      type: "close",
                      side: "right",
                      onClick: B,
                    }),
                  ),
                ),
                a().createElement(
                  "div",
                  { className: h },
                  r && a().createElement("div", { className: p }, r),
                  s && a().createElement("div", { className: b }, s),
                  l && a().createElement("div", { className: te.content }, l),
                  a().createElement("div", { className: v }),
                  E && a().createElement("div", { className: te.footer }, E),
                  c && a().createElement("div", { className: te.buttons }, c),
                ),
              );
            },
          );
        var ne = t(5501);
        const ae = "App_center_34",
          ie = "App_list_80",
          oe = "App_content_c3",
          se = ["onClose", "buttons", "isShown", "displayFlags"];
        function le() {
          return (
            (le =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            le.apply(this, arguments)
          );
        }
        const ce = R.strings.dialogs.retrain,
          Ee = a().memo(function (u) {
            let e = u.onClose,
              t = u.buttons,
              r = u.isShown,
              n = u.displayFlags,
              i = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, se);
            return a().createElement(
              re,
              le({ onClose: e, buttons: t, displayFlags: n, isShown: r }, i, {
                title: a().createElement(Yu, { text: ce.header() }),
                content: a().createElement(
                  "div",
                  { className: oe },
                  a().createElement(ne.u, { className: ie }),
                ),
                classNames: { center: ae },
              }),
            );
          });
        engine.whenReady.then(() => {
          g().render(
            a().createElement(C, null, a().createElement(Bu, { Template: Ee })),
            document.getElementById("root"),
          );
        });
      },
      5501: (u, e, t) => {
        "use strict";
        t.d(e, { u: () => X });
        var r = t(6179),
          n = t.n(r),
          a = t(3215),
          i = t(4598),
          o = t(9480),
          s = t(3946);
        const l = (0, a.q)()(
            ({ observableModel: u }) => {
              const e = { cardsList: u.array("cardsList", []) },
                t = (0, s.Om)(() => (0, o.UI)(e.cardsList.get(), i.yR), { equals: i.jv });
              return Object.assign({}, e, { computes: { cards: t } });
            },
            ({ externalModel: u }) => ({
              onCardClick: u.createCallback((u) => ({ index: u }), "onCardClick"),
            }),
          ),
          c = l[0],
          E = l[1];
        var _ = t(6483),
          d = t.n(_),
          A = t(5415),
          F = t(3403);
        let D, m;
        (!(function (u) {
          ((u.Default = "default"),
            (u.Reset = "reset"),
            (u.Retrain = "retrain"),
            (u.Recruit = "recruit"));
        })(D || (D = {})),
          (function (u) {
            ((u.Default = ""), (u.Disabled = "disabled"), (u.Selected = "selected"));
          })(m || (m = {})));
        var C = t(7727);
        const B = "CustomComponents_storage_c8",
          g = "CustomComponents_storageIcon_2c",
          h = "CustomComponents_storageCount_9b",
          p = (0, r.memo)(({ kwargs: u, cardType: e }) => {
            if (e === D.Reset) {
              const e = null == u ? void 0 : u.storageCount;
              return void 0 === e
                ? null
                : n().createElement(
                    "div",
                    { className: B },
                    n().createElement("div", { className: g }),
                    n().createElement("div", { className: h }, e),
                  );
            }
            return null;
          });
        var b = t(3618),
          f = t(9053),
          v = t(8018);
        const w = {
            base: "Description_base_bf",
            binding: "Description_binding_da",
            binding__highLight: "Description_binding__highLight_95",
            newSkillIcon: "Description_newSkillIcon_1b",
          },
          x = n().memo(function ({ description: u, cardType: e, kwargs: t, className: r }) {
            switch (e) {
              case D.Reset:
              case D.Retrain:
              case D.Recruit:
                return n().createElement(
                  "div",
                  { className: d()(w.base, r) },
                  n().createElement(b.w, {
                    text: u,
                    justifyContent: f.v2.Center,
                    binding: {
                      value: n().createElement(
                        "div",
                        {
                          className: d()(
                            w.binding,
                            (null == t ? void 0 : t.isHighlight) && w.binding__highlight,
                          ),
                        },
                        (0, v.T3)(null == t ? void 0 : t.value),
                      ),
                    },
                  }),
                );
              default:
                return n().createElement(
                  "div",
                  { className: d()(w.base, r) },
                  n().createElement(b.w, { text: u, justifyContent: f.v2.Center, binding: t }),
                );
            }
          });
        var y = t(7405),
          T = t(2056),
          L = t(5298);
        const S = "Price_base_3c",
          k = "Price_base__withPrice_ef";
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
        const O = ({ cost: u, tooltip: e, index: t, tooltipRootId: r }) => {
            const a = (0, L.l)(e.type, { index: t });
            return u.value === u.discountValue && 0 === u.value
              ? n().createElement("div", { className: S }, R.strings.dialogs.priceCard.price.free())
              : n().createElement(
                  "div",
                  { className: d()(S, k) },
                  n().createElement(
                    T.u,
                    M({}, a, { targetId: r }),
                    n().createElement("div", null, n().createElement(y.F, u)),
                  ),
                );
          },
          N = "Title_base_5e",
          H = "Title_base__highLight_1c",
          P = n().memo(function ({ title: u, cardType: e, kwargs: t, className: r }) {
            switch (e) {
              case D.Reset:
              case D.Retrain:
              case D.Recruit:
                return n().createElement(
                  "div",
                  { className: d()(N, (null == t ? void 0 : t.isHighlight) && H, r) },
                  u,
                );
              default:
                return n().createElement("div", { className: d()(N, r) }, u);
            }
          }),
          I = {
            base: "PriceCard_base_1c",
            base__small: "PriceCard_base__small_b0",
            base__selected: "PriceCard_base__selected_e3",
            base__disabled: "PriceCard_base__disabled_9c",
            hover: "PriceCard_hover_a1",
            disabled: "PriceCard_disabled_79",
            selected: "PriceCard_selected_df",
            icon: "PriceCard_icon_43",
            title: "PriceCard_title_98",
            description: "PriceCard_description_97",
            price: "PriceCard_price_13",
          };
        let W;
        !(function (u) {
          ((u.Big = "big"), (u.Small = "small"));
        })(W || (W = {}));
        const j = ({
            onClick: u,
            tooltipRootId: e,
            tooltip: t,
            index: a,
            icon: i,
            size: o = W.Big,
            title: s,
            description: l,
            cardType: c,
            kwargs: E,
            price: _,
            cardState: A,
            className: F,
          }) => {
            const D = A === m.Default,
              B = (0, r.useState)(!1),
              g = B[0],
              h = B[1],
              b = d()(I.base, I[`base__${o}`], I[`base__${A}`], g && I.base__hover, F),
              f = (0, r.useMemo)(() => (E ? JSON.parse(E) : {}), [E]),
              v = (0, r.useCallback)(() => {
                D && (C.$.playClick(), u(a));
              }, [a, D, u]),
              w = (0, r.useCallback)(() => {
                D && (C.$.playHighlight(), h(!0));
              }, [D]),
              y = (0, r.useCallback)(() => D && h(!1), [D]);
            return n().createElement(
              "div",
              { className: b, onClick: v, onMouseEnter: w, onMouseLeave: y },
              A === m.Disabled && n().createElement("div", { className: I.disabled }),
              A === m.Selected && n().createElement("div", { className: I.selected }),
              g && n().createElement("div", { className: I.hover }),
              n().createElement("div", {
                className: I.icon,
                style: { backgroundImage: `url(${i})` },
              }),
              n().createElement(P, { title: s, cardType: c, kwargs: f, className: I.title }),
              n().createElement(x, {
                description: l,
                cardType: c,
                kwargs: f,
                className: I.description,
              }),
              n().createElement(
                "div",
                { className: I.price },
                n().createElement(O, { cost: _, tooltip: t, index: a, tooltipRootId: e }),
              ),
              n().createElement(p, { cardType: c, kwargs: f }),
            );
          },
          G = "PriceListApp_base_7d",
          U = "PriceListApp_card_6a";
        function $() {
          return (
            ($ =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            $.apply(this, arguments)
          );
        }
        const V = (0, F.Pi)(function ({ rootId: u, className: e }) {
            const t = E(),
              r = t.model,
              a = t.controls,
              i = (0, A.GS)().mediaWidth;
            return n().createElement(
              "div",
              { className: d()(G, e) },
              (0, o.UI)(r.computes.cards(), (e, t) =>
                n().createElement(
                  j,
                  $({}, e, {
                    key: `${t}-${e.cardState}`,
                    onClick: a.onCardClick,
                    index: t,
                    tooltipRootId: u,
                    size: i > A.cJ.ExtraSmall ? W.Big : W.Small,
                    className: U,
                  }),
                ),
              ),
            );
          }),
          X = n().memo(function ({
            rootId: u = R.views.lobby.crew.widgets.PriceList("resId"),
            className: e,
          }) {
            return n().createElement(
              c,
              { options: { rootId: u } },
              n().createElement(V, { rootId: u, className: e }),
            );
          });
      },
      776: (u, e, t) => {
        "use strict";
        let r;
        (t.d(e, { f: () => r }),
          (function (u) {
            ((u.backport = "backport"), (u.normal = "normal"), (u.absent = "absent"));
          })(r || (r = {})));
      },
      8460: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
          base: "Currency_base_57",
          icon: "Currency_icon_c5",
          base__small: "Currency_base__small_af",
          base__big: "Currency_base__big_bc",
          base__large: "Currency_base__large_65",
          base__extraLarge: "Currency_base__extraLarge_4d",
          "icon__credits-small": "Currency_icon__credits-small_9b",
          "icon__credits-big": "Currency_icon__credits-big_96",
          "icon__credits-large": "Currency_icon__credits-large_ac",
          "icon__credits-extraLarge": "Currency_icon__credits-extraLarge_16",
          "icon__gold-small": "Currency_icon__gold-small_86",
          "icon__gold-big": "Currency_icon__gold-big_15",
          "icon__gold-large": "Currency_icon__gold-large_36",
          "icon__gold-extraLarge": "Currency_icon__gold-extraLarge_a0",
          "icon__crystal-small": "Currency_icon__crystal-small_27",
          "icon__crystal-big": "Currency_icon__crystal-big_cd",
          "icon__crystal-large": "Currency_icon__crystal-large_d3",
          "icon__crystal-extraLarge": "Currency_icon__crystal-extraLarge_09",
          "icon__xp-small": "Currency_icon__xp-small_a7",
          "icon__xp-big": "Currency_icon__xp-big_97",
          "icon__xp-large": "Currency_icon__xp-large_6b",
          "icon__xp-extraLarge": "Currency_icon__xp-extraLarge_67",
          "icon__freeXP-small": "Currency_icon__freeXP-small_ca",
          "icon__freeXP-big": "Currency_icon__freeXP-big_21",
          "icon__freeXP-large": "Currency_icon__freeXP-large_c8",
          "icon__freeXP-extraLarge": "Currency_icon__freeXP-extraLarge_58",
          "icon__equipCoin-small": "Currency_icon__equipCoin-small_32",
          "icon__equipCoin-big": "Currency_icon__equipCoin-big_79",
          "icon__equipCoin-large": "Currency_icon__equipCoin-large_2c",
          "icon__equipCoin-extraLarge": "Currency_icon__equipCoin-extraLarge_8a",
          value: "Currency_value_e1",
          value__freeXP: "Currency_value__freeXP_cb",
          value__credits: "Currency_value__credits_76",
          value__gold: "Currency_value__gold_dd",
          value__xp: "Currency_value__xp_b0",
          value__crystal: "Currency_value__crystal_19",
          value__equipCoin: "Currency_value__equipCoin_d0",
          value__notEnough: "Currency_value__notEnough_56",
          stock: "Currency_stock_87",
          stock__indent: "Currency_stock__indent_a1",
          stock__interactive: "Currency_stock__interactive_93",
          stockBackground: "Currency_stockBackground_82",
        };
      },
      6143: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
          base: "ExtendedText_base_71",
          base__zeroPadding: "ExtendedText_base__zeroPadding_25",
          base__isTruncationAvailable: "ExtendedText_base__isTruncationAvailable_5b",
          truncated: "ExtendedText_truncated_97",
          truncated__hide: "ExtendedText_truncated__hide_31",
          unTruncated: "ExtendedText_unTruncated_b8",
        };
      },
      9627: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
          blackReal: "colors_blackReal_fc",
          whiteReal: "colors_whiteReal_31",
          white: "colors_white_45",
          whiteOrange: "colors_whiteOrange_81",
          whiteSpanish: "colors_whiteSpanish_c3",
          par: "colors_par_5b",
          parSecondary: "colors_parSecondary_fd",
          parTertiary: "colors_parTertiary_97",
          red: "colors_red_79",
          redDark: "colors_redDark_73",
          yellow: "colors_yellow_76",
          orange: "colors_orange_cd",
          cream: "colors_cream_0f",
          brown: "colors_brown_82",
          greenBright: "colors_greenBright_68",
          green: "colors_green_fa",
          greenDark: "colors_greenDark_a9",
          blueBooster: "colors_blueBooster_26",
          blueTeamkiller: "colors_blueTeamkiller_86",
          cred: "colors_cred_35",
          gold: "colors_gold_c3",
          bond: "colors_bond_ce",
          prom: "colors_prom_83",
        };
      },
      7629: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
          noBreakWrapper: "renderers_noBreakWrapper_10",
          lineBreak: "renderers_lineBreak_b5",
          newLine: "renderers_newLine_bd",
        };
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
        for (s = 0; s < deferred.length; s++) {
          for (var [e, t, r] = deferred[s], a = !0, i = 0; i < e.length; i++)
            (!1 & r || n >= r) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[i]))
              ? e.splice(i--, 1)
              : ((a = !1), r < n && (n = r));
          if (a) {
            deferred.splice(s--, 1);
            var o = t();
            void 0 !== o && (u = o);
          }
        }
        return u;
      }
      r = r || 0;
      for (var s = deferred.length; s > 0 && deferred[s - 1][2] > r; s--)
        deferred[s] = deferred[s - 1];
      deferred[s] = [e, t, r];
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
    (__webpack_require__.j = 180),
    (() => {
      var u = { 180: 0, 897: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var r,
            n,
            [a, i, o] = t,
            s = 0;
          if (a.some((e) => 0 !== u[e])) {
            for (r in i) __webpack_require__.o(i, r) && (__webpack_require__.m[r] = i[r]);
            if (o) var l = o(__webpack_require__);
          }
          for (e && e(t); s < a.length; s++)
            ((n = a[s]), __webpack_require__.o(u, n) && u[n] && u[n][0](), (u[n] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(7442));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
