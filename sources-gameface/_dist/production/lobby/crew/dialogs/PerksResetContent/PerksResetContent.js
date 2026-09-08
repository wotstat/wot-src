(() => {
  var __webpack_modules__ = {
      7405: (u, e, t) => {
        "use strict";
        t.d(e, { F: () => E });
        var r = t(6483),
          n = t.n(r),
          a = t(6179),
          i = t.n(a),
          l = t(329),
          s = t(2372),
          o = t(8460);
        const c = ({
          isDiscount: u,
          isInteractiveDiscount: e,
          size: t,
          type: r,
          isEnough: a,
          value: c,
          discountValue: E,
          showPlus: A,
          stockBackgroundName: _ = l.we.Red,
        }) => {
          const d = n()(o.Z.value, o.Z[`value__${r}`], !a && o.Z.value__notEnough),
            F = n()(o.Z.icon, o.Z[`icon__${r}-${t}`]),
            m = n()(o.Z.stock, E && o.Z.stock__indent, e && o.Z.stock__interactive),
            D = A && c > 0 && "+",
            B = n()(o.Z.base, o.Z[`base__${t}`]);
          return i().createElement(
            "span",
            { className: B },
            i().createElement(
              "span",
              { className: d },
              D,
              i().createElement(s.A, { value: c, format: r === l.V2.gold ? "gold" : "integral" }),
            ),
            i().createElement("span", { className: F }),
            u &&
              i().createElement(
                "span",
                { className: m },
                i().createElement("span", {
                  className: o.Z.stockBackground,
                  style: { backgroundImage: `url(R.images.gui.maps.icons.library.${_})` },
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
        const l = r.O.client.getSize("rem"),
          s = l.width,
          o = l.height,
          c = Object.assign({ width: s, height: o }, (0, i.T)(s, o, a.j)),
          E = (0, n.createContext)(c);
      },
      1039: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => c });
        var r = t(6179),
          n = t.n(r),
          a = t(6536),
          i = t(3495),
          l = t(1043),
          s = t(5262),
          o = t(3138);
        const c = (0, r.memo)(({ children: u }) => {
          const e = (0, r.useContext)(i.Y),
            t = (0, r.useState)(e),
            c = t[0],
            E = t[1],
            A = (0, r.useCallback)((u, e) => {
              const t = o.O.view.pxToRem(u),
                r = o.O.view.pxToRem(e);
              E(Object.assign({ width: t, height: r }, (0, s.T)(t, r, l.j)));
            }, []);
          ((0, a.Z)(() => {
            engine.on("clientResized", A);
          }),
            (0, r.useEffect)(() => () => engine.off("clientResized", A), [A]));
          const _ = (0, r.useMemo)(() => Object.assign({}, c), [c]);
          return n().createElement(i.Y.Provider, { value: _ }, u);
        });
      },
      6010: (u, e, t) => {
        "use strict";
        var r = t(6179),
          n = t(7382),
          a = t(3495);
        const i = ["children"];
        const l = (u) => {
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
          const l = (0, r.useContext)(a.Y),
            s = l.extraLarge,
            o = l.large,
            c = l.medium,
            E = l.small,
            A = l.extraSmall,
            _ = l.extraLargeWidth,
            d = l.largeWidth,
            F = l.mediumWidth,
            m = l.smallWidth,
            D = l.extraSmallWidth,
            B = l.extraLargeHeight,
            C = l.largeHeight,
            g = l.mediumHeight,
            h = l.smallHeight,
            p = l.extraSmallHeight,
            b = { extraLarge: B, large: C, medium: g, small: h, extraSmall: p };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && s) return e;
            if (t.large && o) return e;
            if (t.medium && c) return e;
            if (t.small && E) return e;
            if (t.extraSmall && A) return e;
          } else {
            if (t.extraLargeWidth && _) return (0, n.H)(e, t, b);
            if (t.largeWidth && d) return (0, n.H)(e, t, b);
            if (t.mediumWidth && F) return (0, n.H)(e, t, b);
            if (t.smallWidth && m) return (0, n.H)(e, t, b);
            if (t.extraSmallWidth && D) return (0, n.H)(e, t, b);
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
              if (t.extraSmallHeight && p) return e;
            }
          }
          return null;
        };
        l.defaultProps = {
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
        (0, r.memo)(l);
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
        (t.d(e, { T: () => n }),
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
        function l() {
          return (
            (l =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            l.apply(this, arguments)
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
            l(
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
        t.d(e, { l: () => o });
        var r = t(6179),
          n = t.n(r),
          a = t(7078),
          i = t(6373),
          l = t(2056);
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
        const o = ({ children: u, tooltipArgs: e, className: t }) => {
          if (!e) return u;
          const r = n().createElement("div", { className: t }, u);
          if (e.header || e.body) return n().createElement(i.i, e, r);
          const o = e.contentId,
            c = e.args,
            E = null == c ? void 0 : c.contentId;
          return o || E
            ? n().createElement(l.u, s({}, e, { contentId: o || E }), r)
            : n().createElement(a.t, e, r);
        };
      },
      6373: (u, e, t) => {
        "use strict";
        t.d(e, { i: () => o });
        var r = t(2056),
          n = t(6179),
          a = t.n(n);
        const i = ["children", "body", "header", "note", "alert", "args"];
        function l() {
          return (
            (l =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            l.apply(this, arguments)
          );
        }
        const s = R.views.common.tooltip_window.simple_tooltip_content,
          o = (u) => {
            let e = u.children,
              t = u.body,
              o = u.header,
              c = u.note,
              E = u.alert,
              A = u.args,
              _ = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, i);
            const d = (0, n.useMemo)(() => {
              const u = Object.assign({}, A, { body: t, header: o, note: c, alert: E });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [E, t, o, c, A]);
            return a().createElement(
              r.u,
              l(
                {
                  contentId:
                    ((F = null == A ? void 0 : A.hasHtmlContent),
                    F ? s.SimpleTooltipHtmlContent("resId") : s.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: d,
                },
                _,
              ),
              e,
            );
            var F;
          };
      },
      2056: (u, e, t) => {
        "use strict";
        t.d(e, { u: () => o });
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
        function l(u) {
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
          o = (u) => {
            let e = u.children,
              t = u.contentId,
              n = u.args,
              o = u.onMouseEnter,
              c = u.onMouseLeave,
              E = u.onMouseDown,
              A = u.onClick,
              _ = u.ignoreShowDelay,
              d = void 0 !== _ && _,
              F = u.ignoreMouseClick,
              m = void 0 !== F && F,
              D = u.decoratorId,
              B = void 0 === D ? 0 : D,
              C = u.isEnabled,
              g = void 0 === C || C,
              h = u.targetId,
              p = void 0 === h ? 0 : h,
              b = u.onShow,
              v = u.onHide,
              f = (function (u, e) {
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
              y = (0, a.useMemo)(() => p || (0, r.F)().resId, [p]),
              k = (0, a.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (s(t, B, { isMouseEvent: !0, on: !0, arguments: l(n) }, y),
                  b && b(),
                  (w.current.isVisible = !0));
              }, [t, B, n, y, b]),
              S = (0, a.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const u = w.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (w.current.timeoutId = 0)),
                    s(t, B, { on: !1 }, y),
                    w.current.isVisible && v && v(),
                    (w.current.isVisible = !1));
                }
              }, [t, B, y, v]),
              x = (0, a.useCallback)((u) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(w.current.prevTarget) && S();
                  }, 200)));
              }, []);
            ((0, a.useEffect)(() => {
              const u = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", x, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", x, { capture: !0 }),
                    u && window.clearTimeout(u));
                }
              );
            }, []),
              (0, a.useEffect)(() => {
                !1 === g && S();
              }, [g, S]),
              (0, a.useEffect)(
                () => (
                  window.addEventListener("mouseleave", S),
                  () => {
                    (window.removeEventListener("mouseleave", S), S());
                  }
                ),
                [S],
              ));
            return g
              ? (0, a.cloneElement)(
                  e,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((L = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(k, d ? 100 : 400)),
                            o && o(u),
                            L && L(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (S(), null == c || c(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === m && S(), null == A || A(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === m && S(), null == E || E(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    f,
                  ),
                )
              : e;
            var L;
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
        t.d(e, { U: () => l });
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
        function l({
          initializer: u = !0,
          rootId: e = 0,
          getRoot: t = i,
          context: a = "model",
        } = {}) {
          const l = new Map();
          function s(u, e = 0) {
            viewEnv.removeDataChangedCallback(u, e)
              ? l.delete(u)
              : console.error("Can't remove callback by id:", u);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (u, e, t) => {
              t.forEach((e) => {
                const t = l.get(e);
                void 0 !== t && t(u);
              });
            });
          });
          const o = (u) => {
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
              return (l.set(s, t), u && t(o(n)), s);
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
              for (var u, t = n(l.keys()); !(u = t()).done;) {
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
          l = t(8246);
        const s = () => (u, e) => {
          const t = (0, a.createContext)({});
          return [
            function ({ mode: s = "real", options: o, children: c, mocks: E }) {
              const A = (0, a.useRef)([]),
                _ = (t, a, i) => {
                  var s;
                  const o = l.U(a),
                    c =
                      "real" === t
                        ? o
                        : Object.assign({}, o, {
                            readByPath: null != (s = null == i ? void 0 : i.getter) ? s : () => {},
                          }),
                    E = (u) =>
                      "mocks" === t ? (null == i ? void 0 : i.getter(u)) : c.readByPath(u),
                    _ = (u) => A.current.push(u),
                    d = u({
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
                              l = i.reduce((u, [e, t]) => ((u[t] = n.LO.box(r[e], {})), u), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, n.aD)((u) => {
                                    i.forEach(([e, t]) => {
                                      l[t].set(u[e]);
                                    });
                                  }),
                                  e,
                                ),
                              l
                            );
                          }
                        },
                      },
                      cleanup: _,
                    }),
                    F = { mode: t, model: d, externalModel: c, cleanup: _ };
                  return {
                    model: d,
                    controls: "mocks" === t && i ? i.controls(F) : e(F),
                    externalModel: c,
                    mode: t,
                  };
                },
                d = (0, a.useRef)(!1),
                F = (0, a.useState)(s),
                m = F[0],
                D = F[1],
                B = (0, a.useState)(() => _(s, o, E)),
                C = B[0],
                g = B[1];
              return (
                (0, a.useEffect)(() => {
                  d.current ? g(_(m, o, E)) : (d.current = !0);
                }, [E, m, o]),
                (0, a.useEffect)(() => {
                  D(s);
                }, [s]),
                (0, a.useEffect)(
                  () => () => {
                    (C.externalModel.dispose(), A.current.forEach((u) => u()));
                  },
                  [C],
                ),
                i().createElement(t.Provider, { value: C }, c)
              );
            },
            () => (0, a.useContext)(t),
          ];
        };
      },
      527: (u, e, t) => {
        "use strict";
        (t.r(e), t.d(e, { mouse: () => l, onResize: () => a }));
        var r = t(2472),
          n = t(1176);
        const a = (0, r.E)("clientResized"),
          i = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const l = (function () {
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
                    l = i[e]((u) => t([u, "outside"]));
                  function s(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(a, s),
                    r(),
                    () => {
                      n &&
                        (l(), window.removeEventListener(a, s), (u.listeners -= 1), r(), (n = !1));
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
            addPreloadTexture: () => l,
            children: () => r,
            displayStatus: () => n.W,
            displayStatusIs: () => w,
            events: () => a.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => F,
            getBrowserTexturePath: () => o,
            getDisplayStatus: () => f,
            getScale: () => m,
            getSize: () => A,
            getViewGlobalPosition: () => d,
            isClientAccessible: () => h,
            isEventHandled: () => b,
            isFocused: () => g,
            pxToRem: () => D,
            remToPx: () => B,
            resize: () => _,
            sendEvent: () => i.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => p,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => k,
          }));
        var r = t(3722),
          n = t(6112),
          a = t(6538),
          i = t(8566);
        function l(u) {
          viewEnv.addPreloadTexture(u);
        }
        function s(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function o(u, e, t, r = 1) {
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
        function d(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: B(e.x), y: B(e.y) };
        }
        function F() {
          viewEnv.freezeTextureBeforeResize();
        }
        function m() {
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
        const w = Object.keys(n.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === n.W[e]), u),
            {},
          ),
          y = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          k = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : a.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        "use strict";
        t.d(e, { qP: () => o });
        const r = ["args"];
        const n = 2,
          a = 16,
          i = 32,
          l = 64,
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
          o = {
            close(u) {
              s("popover" === u ? n : i);
            },
            minimize() {
              s(l);
            },
            move(u) {
              s(a, { isMouseEvent: !0, on: u });
            },
          };
      },
      4598: (u, e, t) => {
        "use strict";
        function r() {}
        t.d(e, { ZT: () => r, jv: () => a, yR: () => n });
        function n(u) {
          return u;
        }
        function a() {
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
        t.d(e, { Aq: () => s, GS: () => o, cJ: () => i, fd: () => l });
        var r = t(6179),
          n = t(7739),
          a = t(1043);
        let i, l, s;
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
          })(l || (l = {})),
          (function (u) {
            ((u[(u.ExtraSmall = a.j.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = a.j.small.height)] = "Small"),
              (u[(u.Medium = a.j.medium.height)] = "Medium"),
              (u[(u.Large = a.j.large.height)] = "Large"),
              (u[(u.ExtraLarge = a.j.extraLarge.height)] = "ExtraLarge"));
          })(s || (s = {})));
        const o = () => {
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
            o = ((u) => {
              switch (!0) {
                case u.extraLargeWidth:
                  return l.ExtraLarge;
                case u.largeWidth:
                  return l.Large;
                case u.mediumWidth:
                  return l.Medium;
                case u.smallWidth:
                  return l.Small;
                case u.extraSmallWidth:
                  return l.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), l.ExtraSmall);
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
            mediaWidth: o,
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
        function r(u, e) {
          var t;
          if (!(e >= u.length))
            return Array.isArray(u) ? u[e] : null == (t = u[e]) ? void 0 : t.value;
        }
        t.d(e, { U2: () => r, UI: () => n });
        function n(u, e) {
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
        t.d(e, { $: () => n });
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
        (t.d(e, { Eg: () => i, Uw: () => _, uF: () => n, v2: () => r, z4: () => a }),
          (function (u) {
            ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
          })(r || (r = {})));
        const a = (u) => u.replace(/&nbsp;/g, " "),
          i = (u) => u.replace(/&zwnbsp;/g, "\ufeff"),
          l = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          s = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          o = (u, e, t = r.left) => u.split(e).reduce(t === r.left ? l : s, []),
          c = (() => {
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
          E = ["zh_cn", "zh_sg", "zh_tw"],
          A = (u, e = r.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return E.includes(t)
              ? c(u)
              : ((u, e = r.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    i = a(u);
                  return (o(i, /( )/, e).forEach((u) => (t = t.concat(o(u, n, r.left)))), t);
                })(u, e);
          },
          _ = (u, e, t) =>
            u.split(/%\((.*?)\)(?:[sd])?/g).map((u) => (t && u in t ? t[u] : A(u, e)));
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
        t.d(e, { B3: () => o, Z5: () => i, B0: () => s, ry: () => B });
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
          l = {
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
        const o = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          E = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          A = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = t(5521),
          d = t(3138);
        const F = ["args"];
        function m(u, e, t, r, n, a, i) {
          try {
            var l = u[a](i),
              s = l.value;
          } catch (u) {
            return void t(u);
          }
          l.done ? e(s) : Promise.resolve(s).then(r, n);
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
                    function i(u) {
                      m(a, r, n, i, l, "next", u);
                    }
                    function l(u) {
                      m(a, r, n, i, l, "throw", u);
                    }
                    i(void 0);
                  });
                });
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          C = (u, e) => {
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
          g = () => C(s.CLOSE),
          h = (u, e) => {
            u.keyCode === _.n.ESCAPE && e();
          };
        var p = t(7572);
        const b = n.instance,
          v = {
            DataTracker: a.Z,
            ViewModel: p.Z,
            ViewEventType: s,
            NumberFormatType: o,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: A,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (u) => C(s.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: g,
            sendClosePopOverEvent: () => C(s.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (u, e, t = 0) => {
              C(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, r, n = R.invalid("resId"), a) => {
              const i = d.O.view.getViewGlobalPosition(),
                l = t.getBoundingClientRect(),
                o = l.x,
                c = l.y,
                E = l.width,
                A = l.height,
                _ = {
                  x: d.O.view.pxToRem(o) + i.x,
                  y: d.O.view.pxToRem(c) + i.y,
                  width: d.O.view.pxToRem(E),
                  height: d.O.view.pxToRem(A),
                };
              C(s.POP_OVER, {
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
            addEscapeListener: (u) => {
              const e = (e) => h(e, u);
              return (
                window.addEventListener("keydown", e),
                () => window.removeEventListener("keydown", e)
              );
            },
            closeOnEsc: (u) => {
              h(u, g);
            },
            handleViewEvent: C,
            onBindingsReady: B,
            onLayoutReady: () =>
              new Promise((u) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    u();
                  });
                });
              }),
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
            ClickOutsideManager: b,
            SystemLocale: i,
            UserLocale: l,
          };
        window.ViewEnvHelper = v;
      },
      3618: (u, e, t) => {
        "use strict";
        t.d(e, { w: () => _ });
        var r = t(6483),
          n = t.n(r),
          a = t(3415),
          i = t(4419),
          l = t(6179),
          s = t.n(l),
          o = t(6143),
          c = t(3310),
          E = t(131),
          A = t(9053);
        const _ = s().memo(
          ({
            text: u,
            classMix: e,
            onSizeChanged: t,
            binding: r,
            isTooltipEnable: _ = !1,
            isTruncationAvailable: d = !1,
            targetId: F,
            justifyContent: m = A.v2.FlexStart,
            alignContent: D = A.v2.FlexStart,
            truncateIdentify: B = A.YA,
          }) => {
            const C = (0, l.useRef)(null),
              g = (0, l.useRef)({ height: 0, width: 0 }),
              h = (0, l.useState)({ elementList: [], isTruncated: !1, isTruncateFinished: !1 }),
              p = h[0],
              b = h[1],
              v = (0, l.useMemo)(() => (0, c.s)(u, r), [r, u]),
              f = (0, l.useMemo)(() => {
                if (_ && p.isTruncated)
                  return {
                    args: { text: u, stringifyKwargs: r ? JSON.stringify(r) : "" },
                    contentId: R.views.lobby.common.tooltips.ExtendedTextTooltip("resId"),
                    targetId: F,
                  };
              }, [r, _, F, u, p.isTruncated]),
              w = (0, l.useCallback)(
                (u) => {
                  ((g.current.width = u.contentRect.width),
                    (g.current.height = u.contentRect.height));
                  const e = (0, E.T)(C, v, g.current, B),
                    r = e[0],
                    n = e[1];
                  (b({ elementList: r, isTruncated: n, isTruncateFinished: !0 }), t && t(n));
                },
                [t, B, v],
              ),
              y = (0, l.useMemo)(() => ({ justifyContent: m, alignContent: D }), [D, m]);
            return (
              (0, i.y)(C, w, d),
              s().createElement(
                "div",
                {
                  className: n()(
                    o.Z.base,
                    e,
                    o.Z.base__zeroPadding,
                    d && o.Z.base__isTruncationAvailable,
                  ),
                  style: y,
                },
                s().createElement("div", { className: o.Z.unTruncated, ref: C }, v),
                s().createElement(
                  a.l,
                  { tooltipArgs: f },
                  s().createElement(
                    "div",
                    {
                      className: n()(
                        o.Z.truncated,
                        !p.isTruncateFinished && d && o.Z.truncated__hide,
                      ),
                      style: y,
                    },
                    p.isTruncateFinished && d ? p.elementList : v,
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
        const l = (u) => {
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
                  t.push({ blockType: i.kH.Word, colorTag: e, childList: l(u) });
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
          o = (u, e, t = "") => {
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
                      t.push(...o(u, e));
                    },
                    (u) => {
                      t.push(...o(u[2], e, u[1]));
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
              u.childList.forEach((l, s) => {
                const o = `${t}_${s}`;
                if ((0, n.dz)(l)) {
                  const u = l,
                    e = u.blockType,
                    t = r.IY[e],
                    n = a(u, t, o);
                  i.push(...n);
                } else i.push(e({ elementList: [l], textBlock: u, key: o }));
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
                      l = r.IY[i],
                      s = a(u, l, e);
                    return (
                      i === n.kH.NoBreakWrapper
                        ? t.push(l({ elementList: s, textBlock: u, key: `${e}` }))
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
          l = (u, e) => u.offsetLeft + u.offsetWidth - e,
          s = (u, e, t) => {
            if (!u || !u.textContent) return [!1, 0];
            if (u.offsetLeft > e) return [!1, 0];
            const r = l(u, e),
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
          o = (u, e, t, r, i, l) => {
            let c = -1,
              E = null;
            for (let A = t; A >= 0; A--) {
              const t = u[A],
                _ = Number(u[A].getAttribute(a.bF));
              if (_ === a.kH.LineBreak || _ === a.kH.NewLine || _ === a.kH.Binding) continue;
              const d = t.textContent || "";
              if (!(t.childElementCount > 1)) {
                const u = s(t, r, i),
                  a = u[0],
                  o = u[1];
                if (!a) {
                  o > 0 && (i -= o);
                  continue;
                }
                const _ = d.slice(0, d.length - o) + l,
                  F = e[A];
                ((E = n().cloneElement(F, F.props, _)), (c = A));
                break;
              }
              {
                const u = t.children,
                  a = e[A],
                  s = a.props.children,
                  _ = o(u, s, u.length - 1, r, i, l),
                  F = _[0],
                  m = _[1];
                if (!(F < 0)) {
                  const u = s.slice(0, F);
                  ((E = n().cloneElement(a, a.props, u, m)), (c = A));
                  break;
                }
                i -= d.length;
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
              A = s.lastElementChild;
            if (!i(A, c) && l(A, E) <= 0) return [n, !1];
            const _ = s.children,
              d = ((u, e) => {
                let t = 0,
                  r = u.length - 1;
                for (; r - t >= 0;) {
                  const n = t + Math.ceil(0.5 * (r - t));
                  i(u[n], e) ? (r = n - 1) : (t = n + 1);
                }
                return t - 1;
              })(_, c);
            if (d < 0) return [n, !1];
            const F = o(_, n, d, E, r.length, r),
              m = F[0],
              D = F[1];
            return (D && (n.splice(m, 1, D), n.splice(m + 1)), [n, !0]);
          };
      },
      9053: (u, e, t) => {
        "use strict";
        let r, n, a;
        (t.d(e, { YA: () => l, aF: () => o, bF: () => s, dz: () => i, kH: () => r, v2: () => n }),
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
          l = "...",
          s = "data-block-type",
          o = { [a.NBSP]: r.NoBreakSymbol, [a.ZWNBSP]: r.NoBreakSymbol, [a.NEW_LINE]: r.LineBreak };
      },
      597: (u, e, t) => {
        "use strict";
        t.d(e, { IY: () => c });
        var r = t(6179),
          n = t.n(r),
          a = t(9053),
          i = t(9627),
          l = t(7629);
        const s = (u) => ({ color: `#${u}` }),
          o = ({ elementList: u, textBlock: e, key: t }) => {
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
            [a.kH.Word]: o,
            [a.kH.NoBreakSymbol]: o,
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
                className: l.Z.lineBreak,
              }),
            [a.kH.NewLine]: ({ elementList: u, key: e }) =>
              n().createElement(
                "span",
                { key: e, "data-block-type": a.kH.NewLine, className: l.Z.newLine },
                u,
              ),
            [a.kH.NoBreakWrapper]: ({ elementList: u, key: e }) =>
              n().createElement(
                "span",
                { key: e, "data-block-type": a.kH.NoBreakWrapper, className: l.Z.noBreakWrapper },
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
        let l;
        !(function (u) {
          ((u.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (u.SHOP_INFO = "shop_info"),
            (u.RUDY = "rudy"));
        })(l || (l = {}));
      },
      5420: (u, e, t) => {
        "use strict";
        var r = t(7739),
          n = t(6179),
          a = t.n(n),
          i = t(6483),
          l = t.n(i),
          s = t(926),
          o = t.n(s),
          c = t(5415);
        const E = ["children", "className"];
        function A() {
          return (
            (A =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            A.apply(this, arguments)
          );
        }
        const _ = {
            [c.fd.ExtraSmall]: "",
            [c.fd.Small]: o().SMALL_WIDTH,
            [c.fd.Medium]: `${o().SMALL_WIDTH} ${o().MEDIUM_WIDTH}`,
            [c.fd.Large]: `${o().SMALL_WIDTH} ${o().MEDIUM_WIDTH} ${o().LARGE_WIDTH}`,
            [c.fd.ExtraLarge]:
              `${o().SMALL_WIDTH} ${o().MEDIUM_WIDTH} ${o().LARGE_WIDTH} ${o().EXTRA_LARGE_WIDTH}`,
          },
          d = {
            [c.Aq.ExtraSmall]: "",
            [c.Aq.Small]: o().SMALL_HEIGHT,
            [c.Aq.Medium]: `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT}`,
            [c.Aq.Large]: `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT} ${o().LARGE_HEIGHT}`,
            [c.Aq.ExtraLarge]:
              `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT} ${o().LARGE_HEIGHT} ${o().EXTRA_LARGE_HEIGHT}`,
          },
          F = {
            [c.cJ.ExtraSmall]: "",
            [c.cJ.Small]: o().SMALL,
            [c.cJ.Medium]: `${o().SMALL} ${o().MEDIUM}`,
            [c.cJ.Large]: `${o().SMALL} ${o().MEDIUM} ${o().LARGE}`,
            [c.cJ.ExtraLarge]: `${o().SMALL} ${o().MEDIUM} ${o().LARGE} ${o().EXTRA_LARGE}`,
          },
          m = (u) => {
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
              o = n.mediaSize;
            return a().createElement("div", A({ className: l()(t, _[i], d[s], F[o]) }, r), e);
          },
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
          return a().createElement(r.ZN, null, a().createElement(m, t, e));
        };
        var C = t(493),
          g = t.n(C),
          h = t(3403),
          p = t(5501),
          b = t(9887),
          v = t.n(b);
        const f = ["xl", "lg", "md", "sm", "xs"],
          w = (u) => u.includes("_") && ((u) => f.includes(u))(u.split("_").at(-1)),
          y = [c.cJ.ExtraLarge, c.cJ.Large, c.cJ.Medium, c.cJ.Small, c.cJ.ExtraSmall],
          k = (u, e) =>
            Object.keys(u).reduce((t, r) => {
              if (r in t) return t;
              if (w(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const a = y.indexOf(e),
                  i = (-1 !== a ? f.slice(a) : [])
                    .map((u) => n + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  l = i ? u[i] : void 0;
                return ((t[n] = void 0 !== l ? l : u[n]), t);
              }
              const n = u[r];
              return (
                void 0 === n ||
                  ((u, e) => f.some((t) => void 0 !== e[`${u}_${t}`]))(r, u) ||
                  (t[r] = n),
                t
              );
            }, {}),
          S = (u, e = k) => {
            const t = (
              (u, e = k) =>
              (t) => {
                const r = (0, c.GS)().mediaSize,
                  i = (0, n.useMemo)(() => e(t, r), [t, r]);
                return a().createElement(u, i);
              }
            )(u, e);
            return a().memo((e) =>
              Object.keys(e).some((u) => w(u) && void 0 !== e[u])
                ? a().createElement(t, e)
                : a().createElement(u, e),
            );
          },
          x = {
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
          L = [
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
        function T() {
          return (
            (T =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            T.apply(this, arguments)
          );
        }
        Object.keys(v());
        const M = {
            XL: { mt: x.mt__XL, mr: x.mr__XL, mb: x.mb__XL, ml: x.ml__XL },
            LG: { mt: x.mt__LG, mr: x.mr__LG, mb: x.mb__LG, ml: x.ml__LG },
            MDp: { mt: x.mt__MDp, mr: x.mr__MDp, mb: x.mb__MDp, ml: x.ml__MDp },
            MD: { mt: x.mt__MD, mr: x.mr__MD, mb: x.mb__MD, ml: x.ml__MD },
            SMp: { mt: x.mt__SMp, mr: x.mr__SMp, mb: x.mb__SMp, ml: x.ml__SMp },
            SM: { mt: x.mt__SM, mr: x.mr__SM, mb: x.mb__SM, ml: x.ml__SM },
            XS: { mt: x.mt__XS, mr: x.mr__XS, mb: x.mb__XS, ml: x.ml__XS },
          },
          O = (Object.keys(M), ["mt", "mr", "mb", "ml"]),
          I = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          P = S((u) => {
            let e = u.className,
              t = u.width,
              r = u.height,
              i = u.m,
              s = u.mt,
              o = void 0 === s ? i : s,
              c = u.mr,
              E = void 0 === c ? i : c,
              A = u.mb,
              _ = void 0 === A ? i : A,
              d = u.ml,
              F = void 0 === d ? i : d,
              m = u.column,
              D = u.row,
              B = u.flexDirection,
              C = void 0 === B ? (m ? "column" : D && "row") || void 0 : B,
              g = u.flexStart,
              h = u.center,
              p = u.flexEnd,
              b = u.spaceBetween,
              v = u.spaceAround,
              f = u.justifyContent,
              w =
                void 0 === f
                  ? (g ? "flex-start" : h && "center") ||
                    (p && "flex-end") ||
                    (b && "space-between") ||
                    (v && "space-around") ||
                    void 0
                  : f,
              y = u.alignItems,
              k =
                void 0 === y
                  ? (g ? "flex-start" : h && "center") || (p && "flex-end") || void 0
                  : y,
              S = u.alignSelf,
              R = u.wrap,
              P = u.flexWrap,
              N = void 0 === P ? (R ? "wrap" : void 0) : P,
              H = u.grow,
              W = u.shrink,
              j = u.flex,
              G = void 0 === j ? (H || W ? `${H ? 1 : 0} ${W ? 1 : 0} auto` : void 0) : j,
              U = u.style,
              $ = u.children,
              X = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, L);
            const z = (0, n.useMemo)(() => {
                const u = { mt: o, mr: E, mb: _, ml: F },
                  e = ((u) =>
                    O.reduce((e, t) => {
                      const r = u[t];
                      return r && "number" != typeof r ? e.concat(M[!0 === r ? "MD" : r][t]) : e;
                    }, []))(u),
                  n = ((u) =>
                    O.reduce((e, t) => {
                      const r = u[t];
                      return ("number" == typeof r && (e[I[t]] = r + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, U, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: G,
                    alignSelf: S,
                    display: C || k ? "flex" : void 0,
                    flexDirection: C,
                    flexWrap: N,
                    justifyContent: w,
                    alignItems: k,
                  }),
                  computedClassNames: e,
                };
              }, [t, r, o, E, _, F, U, G, S, C, N, w, k]),
              V = z.computedStyle,
              q = z.computedClassNames;
            return a().createElement("div", T({ className: l()(x.base, ...q, e), style: V }, X), $);
          });
        var N = t(3649);
        const H = "FormatText_base_d0",
          W = ({ binding: u, text: e = "", classMix: t, alignment: r = N.v2.left }) =>
            null === e
              ? (console.error("FormatText was supplied with 'null'"), null)
              : a().createElement(
                  n.Fragment,
                  null,
                  e.split("\n").map((e, i) =>
                    a().createElement(
                      "div",
                      { className: l()(H, t), key: `${e}-${i}` },
                      (0, N.Uw)(e, r, u).map((u, e) =>
                        a().createElement(n.Fragment, { key: `${e}-${u}` }, u),
                      ),
                    ),
                  ),
                );
        var j = t(3532),
          G = t.n(j);
        const U = {
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
          $ = [
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
        function X() {
          return (
            (X =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            X.apply(this, arguments)
          );
        }
        Object.keys(v());
        const z = Object.keys(G()),
          V = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          q = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          Z = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          Y = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          K =
            (Object.keys(Y),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": V,
              "heading-H36": V,
              "heading-H28": q,
              "heading-H24": q,
              "heading-H24R": q,
              "heading-H22": q,
              "heading-H20R": q,
              "heading-H18": q,
              "heading-H15": Z,
              "heading-H14": Z,
              "paragraph-P24": q,
              "paragraph-P18": q,
              "paragraph-P16": q,
              "paragraph-P14": Z,
              "paragraph-P12": Z,
              "paragraph-P10": Z,
            }),
          J =
            (Object.keys(K),
            (u) =>
              u
                ? ((u) => z.includes(u))(u)
                  ? { colorClassName: U[u] }
                  : { colorStyle: { color: u } }
                : {}),
          Q = S((u) => {
            let e = u.text,
              t = u.variant,
              r = u.className,
              i = u.color,
              s = u.m,
              o = u.mt,
              c = void 0 === o ? s : o,
              E = u.mr,
              A = void 0 === E ? s : E,
              _ = u.mb,
              d = void 0 === _ ? s : _,
              F = u.ml,
              m = void 0 === F ? s : F,
              D = u.style,
              B = u.format,
              C = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, $);
            const g = (0, n.useMemo)(() => {
                const u = J(i),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, D, r), colorClassName: e };
              }, [D, i]),
              h = g.computedStyle,
              p = g.colorClassName;
            return a().createElement(
              P,
              X(
                {
                  className: l()(U.base, t && U[t], p, r),
                  style: h,
                  mt: !0 === c ? K[t || "paragraph-P16"].mt : c,
                  mr: !0 === A ? K[t || "paragraph-P16"].mr : A,
                  mb: !0 === d ? K[t || "paragraph-P16"].mb : d,
                  ml: !0 === m ? K[t || "paragraph-P16"].ml : m,
                },
                C,
              ),
              void 0 !== B ? a().createElement(W, X({}, B, { text: e })) : e,
            );
          });
        let uu;
        !(function (u) {
          ((u.New = "new"),
            (u.Learned = "learned"),
            (u.Learning = "learning"),
            (u.Irrelevant = "irrelevant"),
            (u.Possible = "possible"),
            (u.ZeroSkill = "zeroSkill"));
        })(uu || (uu = {}));
        const eu = (u, e) => {
          const t = [];
          for (let r = 0; r < u; r++) t.push(e(r));
          return t;
        };
        var tu = t(7030),
          ru = t(6373);
        const nu = {
            base: "RoleLevelIcon_base_e1",
            realLevel: "RoleLevelIcon_realLevel_96",
            base__small: "RoleLevelIcon_base__small_ce",
            icon: "RoleLevelIcon_icon_fa",
          },
          au = (0, n.memo)(({ percentValue: u, skillSize: e, hasSkills: t }) => {
            const r = t ? R.strings.crew_widget.plusValue() : R.strings.crew_widget.plusSpecValue();
            return a().createElement(
              ru.i,
              {
                header: R.strings.crew_widget.tooltip.roleLevelIcon.header(),
                body: R.strings.crew_widget.tooltip.roleLevelIcon.body(),
              },
              a().createElement(
                "div",
                { className: l()(nu.base, nu[`base__${e}`]) },
                a().createElement("div", { className: nu.icon }),
                a().createElement(
                  "div",
                  { className: nu.realLevel },
                  a().createElement(Q, {
                    text: r,
                    format: { binding: { value: a().createElement(Q, { text: u }) } },
                  }),
                ),
              ),
            );
          }),
          iu = (u) => u.skills.length + u.newSkillsAmount + u.possibleSkillsAmount,
          lu = "AcceleratedTrainingIcon_base_4f",
          su = "AcceleratedTrainingIcon_icon_45",
          ou = (0, n.memo)(({ classMix: u }) =>
            a().createElement(
              ru.i,
              {
                header: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.header(),
                body: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.body(),
              },
              a().createElement(
                "div",
                { className: l()(lu, u) },
                a().createElement("div", { className: su }),
              ),
            ),
          ),
          cu = (u) => -(Math.cos(Math.PI * u) - 1) / 2,
          Eu = {
            base: "LastSkillInfo_base_38",
            realLevel: "LastSkillInfo_realLevel_78",
            base__small: "LastSkillInfo_base__small_c5",
            possibleLevel: "LastSkillInfo_possibleLevel_02",
            acceleratedTrainingIcon: "LastSkillInfo_acceleratedTrainingIcon_bf",
            base__big: "LastSkillInfo_base__big_10",
          },
          Au = 0.01,
          _u = (0, n.memo)(
            ({
              lastSkillLevel: u,
              lastPossibleSkillLevel: e,
              showAcceleratedTrainingIcon: t,
              skillSize: r,
              blinkStyle: i,
            }) => {
              const s = (0, n.useRef)(u),
                o = (0, tu.useSpring)(() => ({ from: { scale: 1 } })),
                c = o[0],
                E = o[1];
              (0, n.useEffect)(() => {
                e < 0 &&
                  s.current !== u &&
                  (E.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: cu },
                  }),
                  (s.current = u));
              }, [u, e, E]);
              const A = (0, n.useMemo)(
                  () =>
                    0 === e
                      ? [R.strings.common.percentValue(), e]
                      : e < Au
                        ? [R.strings.crew_widget.plusMinValue(), Au]
                        : [R.strings.crew_widget.plusValue(), e],
                  [e],
                ),
                _ = A[0],
                d = A[1];
              return a().createElement(
                "div",
                { className: l()(Eu.base, Eu[`base__${r}`]) },
                u >= 0 &&
                  u < 100 &&
                  a().createElement(
                    tu.animated.div,
                    { style: c },
                    a().createElement(
                      "div",
                      { className: Eu.realLevel },
                      (0, N.uF)(R.strings.common.percentValue(), {
                        value: u > 0 && u < Au ? Au : u,
                      }),
                    ),
                  ),
                e >= 0 &&
                  e < 100 &&
                  a().createElement(
                    tu.animated.div,
                    { className: Eu.possibleLevel, style: i },
                    (0, N.uF)(_, { value: d }),
                  ),
                t && a().createElement(ou, { classMix: Eu.acceleratedTrainingIcon }),
              );
            },
          );
        var du = t(2056);
        const Fu = {
          base: "TankmanSkill_base_84",
          base__big: "TankmanSkill_base__big_a0",
          bg: "TankmanSkill_bg_f9",
          icon: "TankmanSkill_icon_1b",
          icon__irrelevant: "TankmanSkill_icon__irrelevant_50",
        };
        let mu;
        !(function (u) {
          ((u.Big = "big"), (u.Small = "small"));
        })(mu || (mu = {}));
        const Du = a().memo(function ({ icon: u, type: e, size: t }) {
            const r = (0, n.useMemo)(() => {
                let u;
                return (
                  (u =
                    e === uu.Possible || e === uu.New
                      ? R.images.gui.maps.icons.tankmen.skills.medium.new_skill()
                      : R.images.gui.maps.icons.crew.$dyn(`${e}SkillFrame_${t}`)),
                  { backgroundImage: `url(${u})` }
                );
              }, [e, t]),
              i = (0, n.useMemo)(() => {
                if (!u) return null;
                return {
                  backgroundImage: `url(${R.images.gui.maps.icons.tankmen.skills.$dyn(t === mu.Big ? "c_22x22" : "small").$dyn(u)})`,
                };
              }, [u, t]);
            return a().createElement(
              "div",
              { className: l()(Fu.base, Fu[`base__${t}`]) },
              a().createElement("div", { className: Fu.bg, style: r }),
              i &&
                a().createElement("div", { className: l()(Fu.icon, Fu[`icon__${e}`]), style: i }),
            );
          }),
          Bu = 33,
          Cu = 0,
          gu = !0,
          hu = "play";
        const pu = [
          "width",
          "height",
          "getImageSource",
          "frameCount",
          "onAnimate",
          "frameTime",
          "initialFrameIndex",
          "lastFrameIndex",
          "loop",
          "state",
          "onAnimationDone",
          "onAnimationComplete",
          "poster",
        ];
        function bu() {
          return (
            (bu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            bu.apply(this, arguments)
          );
        }
        const vu = (0, n.memo)(function (u) {
            let e = u.width,
              t = u.height,
              r = u.getImageSource,
              i = u.frameCount,
              l = u.onAnimate,
              s = u.frameTime,
              o = void 0 === s ? Bu : s,
              c = u.initialFrameIndex,
              E = void 0 === c ? Cu : c,
              A = u.lastFrameIndex,
              _ = void 0 === A ? i - 1 : A,
              d = u.loop,
              F = void 0 === d ? gu : d,
              m = u.state,
              D = void 0 === m ? hu : m,
              B = u.onAnimationDone,
              C = u.onAnimationComplete,
              g = u.poster,
              h = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, pu);
            const p = (0, n.useRef)(null);
            return (
              (0, n.useEffect)(() => {
                const u = p.current;
                if (!u) return;
                const e = u.getContext("2d"),
                  t = (t) => {
                    (e.clearRect(0, 0, u.width, u.height), e.drawImage(t.img, -t.x, -t.y));
                  };
                switch (D) {
                  case "play":
                    return (function () {
                      const u = yu(E, _, r),
                        e = fu(E, _),
                        n = window.setInterval(() => {
                          const r = e(),
                            a = u.get(r);
                          a
                            ? (null == l || l(r, a),
                              t(a),
                              r === _ &&
                                (null == C || C(),
                                F || (null == B || B(), window.clearInterval(n))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, o);
                      return () => window.clearInterval(n);
                    })();
                  case "stop":
                    return (function () {
                      const u = 0 === E && g ? { path: g, x: 0, y: 0 } : r(E),
                        e = new Image();
                      e.src = u.path;
                      const n = () => t(wu(u, e));
                      return (
                        e.addEventListener("load", n),
                        () => e.removeEventListener("load", n)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [o, r, E, _, F, l, C, B, g, D]),
              a().createElement("canvas", bu({}, h, { width: e, height: t, ref: p }))
            );
          }),
          fu = (u, e) => {
            let t = u;
            return () => {
              const r = t;
              return ((t += 1), t > e && (t = u), r);
            };
          },
          wu = (u, e) => Object.assign({}, u, { img: e }),
          yu = (u, e, t) => {
            const r = new Map(),
              n = {};
            for (let a = u; a <= e; a++) {
              const u = t(a),
                e = n[u.path];
              if (e) r.set(a, wu(u, e));
              else {
                const e = new Image();
                ((n[u.path] = e),
                  (e.src = u.path),
                  (e.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${a})`,
                      u.path,
                      `(${u.x},${u.y})`,
                    );
                  }),
                  r.set(a, wu(u, e)));
              }
            }
            return r;
          };
        const ku = [
          "width",
          "height",
          "getSrcByFrame",
          "frameCount",
          "onAnimate",
          "frameTime",
          "initialFrameIndex",
          "loop",
          "state",
          "onAnimationComplete",
          "revers",
        ];
        function Su() {
          return (
            (Su =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            Su.apply(this, arguments)
          );
        }
        let xu;
        !(function (u) {
          ((u.Play = "play"), (u.Stop = "stop"));
        })(xu || (xu = {}));
        const Lu = (u, e, t) => {
            const r = new Image();
            ((r.src = t(e)), u.push(r));
          },
          Tu =
            ((0, n.memo)((u) => {
              let e = u.width,
                t = u.height,
                r = u.getSrcByFrame,
                i = u.frameCount,
                l = u.onAnimate,
                s = void 0 === l ? () => {} : l,
                o = u.frameTime,
                c = void 0 === o ? 33 : o,
                E = u.initialFrameIndex,
                A = void 0 === E ? 0 : E,
                _ = u.loop,
                d = void 0 === _ || _,
                F = u.state,
                m = void 0 === F ? xu.Play : F,
                D = u.onAnimationComplete,
                B = void 0 === D ? () => {} : D,
                C = u.revers,
                g = void 0 !== C && C,
                h = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    r,
                    n = {},
                    a = Object.keys(u);
                  for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                  return n;
                })(u, ku);
              const p = (0, n.useRef)(null);
              return (
                (0, n.useEffect)(() => {
                  const u = p.current;
                  if (!u) return;
                  const n = i - 1,
                    a = u.getContext("2d"),
                    l = (r) => {
                      (a.clearRect(0, 0, u.width, u.height), a.drawImage(r, 0, 0, e, t));
                    };
                  if ("stop" === m) {
                    const u = r(0),
                      e = new Image();
                    e.src = u;
                    const t = () => l(e);
                    return (e.addEventListener("load", t), () => e.removeEventListener("load", t));
                  }
                  const o = ((u, e, t) => {
                      const r = [];
                      if (t) for (let t = u; t >= 0; t--) Lu(r, t, e);
                      else for (let t = 0; t < u; t++) Lu(r, t, e);
                      return r;
                    })(i, r, g),
                    E = ((u, e = 0) => {
                      let t = e;
                      return () => {
                        const e = t;
                        return ((t += 1), t > u && (t = 0), e);
                      };
                    })(n, A),
                    _ = setInterval(() => {
                      const u = E(),
                        e = o[u];
                      (l(o[u]), s(u, e), u === n && (B(), d || clearInterval(_)));
                    }, c);
                  return () => clearInterval(_);
                }, [i, c, r, t, A, d, s, B, m, e, g]),
                a().createElement("canvas", Su({}, h, { width: e, height: t, ref: p }))
              );
            }),
            "AnimatedNewSkill_base_6b"),
          Ru = "AnimatedNewSkill_base__big_31";
        function Mu(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return Ou(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return Ou(u, e);
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
        function Ou(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, r = new Array(e); t < e; t++) r[t] = u[t];
          return r;
        }
        class Iu {
          constructor() {
            ((this._intervalID = void 0),
              (this._observers = void 0),
              (this._intervalID = null),
              (this._observers = new Map()));
          }
          static get instance() {
            return (Iu._instance || (Iu._instance = new Iu()), Iu._instance);
          }
          subscribe(u) {
            (this._observers.set(u, u),
              1 === this._observers.size &&
                (this._intervalID = window.setInterval(() => {
                  for (var u, e = Mu(this._observers.values()); !(u = e()).done;) {
                    (0, u.value)();
                  }
                }, 5e3)));
          }
          unsubscribe(u) {
            (this._observers.delete(u),
              0 === this._observers.size &&
                null !== this._intervalID &&
                (clearInterval(this._intervalID), (this._intervalID = null)));
          }
        }
        Iu._instance = void 0;
        const Pu = {
          width: 24,
          height: 24,
          frameCount: 42,
          chunk: { count: 1, columns: 42, rows: 1 },
          getChunkPath:
            ((Nu = "R.images.gui.maps.icons.sequence.new_skill.skill_"), (u) => `${Nu}${u}`),
        };
        var Nu;
        const Hu = ({ size: u }) => {
            const e = (function (u) {
                const e = u.chunk,
                  t = e.rows * e.columns;
                return (r) => {
                  const n = r % t,
                    a = (n % e.columns) * u.width,
                    i = Math.trunc(n / e.columns) * u.height;
                  return { path: u.getChunkPath(Math.trunc(r / t)), x: a, y: i };
                };
              })(Pu),
              t = (0, n.useState)(xu.Stop),
              r = t[0],
              i = t[1],
              s = (0, n.useCallback)(() => {
                i(xu.Play);
              }, [i]),
              o = (0, n.useCallback)(() => {
                i(xu.Stop);
              }, [i]);
            return (
              (0, n.useEffect)(
                () => (Iu.instance.subscribe(s), () => Iu.instance.unsubscribe(s)),
                [s],
              ),
              a().createElement(vu, {
                width: Pu.width,
                height: Pu.height,
                frameCount: Pu.frameCount,
                getImageSource: e,
                loop: !1,
                state: r,
                onAnimationDone: o,
                className: l()(Tu, u === mu.Big && Ru),
              })
            );
          },
          Wu = {
            base: "Skill_base_ba",
            base__big: "Skill_base__big_eb",
            container: "Skill_container_0f",
            divider: "Skill_divider_e8",
            divider__small: "Skill_divider__small_42",
          };
        function ju() {
          return (
            (ju =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            ju.apply(this, arguments)
          );
        }
        let Gu;
        !(function (u) {
          ((u.Big = "big"), (u.Small = "small"));
        })(Gu || (Gu = {}));
        const Uu = (0, n.memo)(
            ({
              name: u,
              icon: e,
              type: t,
              size: r,
              commonMarginValue: i,
              marginValue: s,
              clipWidth: o,
              tankmanID: c,
              blinkStyle: E,
              showNewSkillAnimation: A,
              isTooltipEnabled: _ = !0,
              isLastZeroSkill: d = !1,
            }) => {
              const F = (0, n.useRef)(""),
                m = (0, tu.useSpring)(() => ({ from: { scale: 1 } })),
                D = m[0],
                B = m[1];
              (0, n.useEffect)(() => {
                (t === uu.New &&
                  F.current === uu.Possible &&
                  B.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: cu },
                  }),
                  (F.current = t));
              }, [t, B]);
              return a().createElement(
                du.u,
                ju(
                  {},
                  (() => {
                    switch (t) {
                      case uu.Learned:
                      case uu.ZeroSkill:
                      case uu.Learning:
                      case uu.Irrelevant:
                        return {
                          contentId:
                            R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                              "resId",
                            ),
                          args: { tooltipId: "crewPerkGf", tankmanID: c, skillName: u },
                        };
                      case uu.New:
                      case uu.Possible:
                        return {
                          contentId: R.views.lobby.crew.tooltips.PerkAvailableTooltip("resId"),
                          args: { tankmanID: c },
                        };
                    }
                  })(),
                  {
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                    isEnabled: _,
                    ignoreShowDelay: !0,
                  },
                ),
                a().createElement(
                  tu.animated.div,
                  { className: Wu.container, style: D },
                  a().createElement(
                    tu.animated.div,
                    { style: t === uu.Possible ? E : void 0 },
                    a().createElement(
                      "div",
                      {
                        className: l()(Wu.base, Wu[`base__${r}`]),
                        style: {
                          marginLeft: t !== uu.ZeroSkill ? `${s}rem` : `${s < 0 ? 2 : s}rem`,
                          clipPath: `inset(0 ${o}rem 0 0)`,
                        },
                      },
                      !A || (t !== uu.Possible && t !== uu.New)
                        ? a().createElement(Du, { icon: e, size: r, type: t })
                        : a().createElement(Hu, { size: r }),
                    ),
                  ),
                  d &&
                    a().createElement("div", {
                      className: l()(Wu.divider, r === Gu.Small && Wu.divider__small),
                      style: { marginRight: (r === Gu.Small ? 6 : 8) - (s || i || 0) + "rem" },
                    }),
                ),
              );
            },
          ),
          $u = "SkillsList_base_11",
          Xu = "SkillsList_numOfSkills_64",
          zu = "SkillsList_numOfSkills__twoRows_8d",
          Vu = "SkillsList_numOfSkills__hidden_c5",
          qu = "SkillsList_numOfSkillsContent_a4",
          Zu = "SkillsList_numOfSkillsContent__withNew_b6",
          Yu = "SkillsList_row_03",
          Ku = "SkillsList_skillsWithOutLast_02",
          Ju = "SkillsList_skillsWithOutLast__hidden_8d",
          Qu = "SkillsList_lastSkill_96",
          ue = "SkillsList_lastSkill__wrapped_9d",
          ee = "SkillsList_possibleLevel_97",
          te = "SkillsList_possibleLevel__before_6f",
          re = (0, n.memo)(
            ({
              tankman: u,
              showAcceleratedTrainingIcon: e = !1,
              rowWidth: t = 220,
              maxBigSkillsInRow: r = 10,
              blinkStyle: i,
              isSkillTooltipEnabled: s = !0,
              isCurrentLayoutHangar: o = !1,
              isWidgetHovered: c = !1,
            }) => {
              const E = u.skills,
                A = E.filter((u) => u.type === uu.ZeroSkill).length,
                _ = A > 0 ? E[A - 1].name : null,
                d = E.length,
                F = iu(u),
                m = ((u, e, t) => {
                  let r = u > e ? 10 : u;
                  const n = 0 === u ? u : Math.ceil(u / r),
                    a = n > 1 ? 16 : 24;
                  let i = 2,
                    l = a;
                  for (; (t - (a + i)) / (l + i) < Math.floor((u - 1) / n);) i > 0 ? i-- : l--;
                  return (
                    (r = Math.min(r, 1 + Math.floor((t - a) / (l + i)))),
                    l !== a && (i = l - a),
                    [n, r, i, a, l]
                  );
                })(F, r, t),
                D = m[0],
                B = m[1],
                C = m[2],
                g = m[3],
                h = m[4],
                p = D > 1 ? Gu.Small : Gu.Big,
                b = (0, n.useMemo)(
                  () =>
                    a().createElement(
                      tu.animated.div,
                      { className: l()(ee, 0 === d && te), style: i },
                      a().createElement(au, {
                        percentValue: u.lastPossibleRoleLevel,
                        skillSize: p,
                        hasSkills: u.possibleSkillsAmount > 0 || d > 0,
                      }),
                    ),
                  [i, p, d, u.lastPossibleRoleLevel, u.possibleSkillsAmount],
                ),
                v = u.skills.filter((u) => u.type === uu.New).length > 1,
                f = (0, n.useCallback)(
                  (e, t) => {
                    const r = B * e + t;
                    let n = "",
                      a = "",
                      i = uu.Learned;
                    if (r < d) {
                      const u = E[r];
                      u && ((n = u.name), (a = u.icon), (i = u.type));
                    } else i = r < d + u.newSkillsAmount ? uu.New : uu.Possible;
                    return { skillIndex: r, name: n, icon: a, type: i };
                  },
                  [B, E, d, u.newSkillsAmount],
                ),
                w = Array(D)
                  .fill(null)
                  .reduce((u, e, t) => u + Math.min(B, F - t * B) - 1, 0),
                y = (0, n.useCallback)(
                  (e, t, r) => {
                    const n = t - 1,
                      E = f(e, n),
                      _ = E.skillIndex,
                      d = E.name,
                      F = E.icon,
                      m = E.type,
                      B = 0 === n ? C : 0,
                      h = n * (g + C),
                      b = 2 * (p === Gu.Big ? 8 : 6) + 1 - C;
                    return a().createElement(
                      "div",
                      {
                        className: l()(Qu, o && !c && ue),
                        style: {
                          "--leftPosition": -(h + (!(A > 0) || (D > 1 && r) ? 0 : b)) + "rem",
                        },
                      },
                      a().createElement(Uu, {
                        name: d,
                        icon: F,
                        type: m,
                        size: p,
                        marginValue: 0 === n ? 0 : C,
                        commonMarginValue: B,
                        key: _ + "_" + d,
                        clipWidth: 0,
                        tankmanID: u.tankmanID,
                        blinkStyle: i,
                        isTooltipEnabled: s,
                        showNewSkillAnimation: o,
                      }),
                    );
                  },
                  [f, C, o, c, g, A, D, p, u.tankmanID, i, s],
                );
              return a().createElement(
                "div",
                { className: $u },
                a().createElement(
                  "div",
                  { className: l()(Xu, D > 1 && zu, c && Vu) },
                  o &&
                    w > 0 &&
                    a().createElement(Q, {
                      className: l()(qu, v && Zu),
                      text: R.strings.crew_widget.hiddenSkills(),
                      format: { binding: { num: w } },
                    }),
                ),
                eu(D, (t) => {
                  const r = Math.min(B, F - t * B),
                    n = t === D - 1;
                  return a().createElement(
                    "div",
                    { className: Yu, key: `row_${t}` },
                    u.lastPossibleRoleLevel > 0 && 0 === d && b,
                    a().createElement(
                      "div",
                      { className: l()(Ku, o && !c && Ju) },
                      eu(r - 1, (e) => {
                        const n = f(t, e),
                          l = n.skillIndex,
                          c = n.name,
                          E = n.icon,
                          A = n.type;
                        return a().createElement(Uu, {
                          name: c,
                          icon: E,
                          type: A,
                          size: p,
                          marginValue: 0 === e ? 0 : C,
                          commonMarginValue: 0 === e ? C : 0,
                          key: l + "_" + c + "_" + A,
                          clipWidth: e === r - 1 || A === uu.ZeroSkill ? 0 : g - h,
                          tankmanID: u.tankmanID,
                          blinkStyle: i,
                          isTooltipEnabled: s,
                          showNewSkillAnimation: o,
                          isLastZeroSkill: c === _,
                        });
                      }),
                    ),
                    y(t, r, n),
                    n &&
                      a().createElement(
                        a().Fragment,
                        null,
                        a().createElement(_u, {
                          lastSkillLevel: u.possibleSkillsAmount > 0 ? -1 : u.lastSkillLevel,
                          lastPossibleSkillLevel: u.lastPossibleSkillLevel,
                          showAcceleratedTrainingIcon: e,
                          skillSize: p,
                          blinkStyle: i,
                        }),
                        u.lastPossibleRoleLevel > 0 && d > 0 && b,
                      ),
                  );
                }),
                !D &&
                  a().createElement(
                    "div",
                    { className: Yu },
                    u.lastPossibleRoleLevel > 0 && 0 === d && b,
                    a().createElement(_u, {
                      lastSkillLevel: u.possibleSkillsAmount > 0 ? -1 : u.lastSkillLevel,
                      lastPossibleSkillLevel: u.lastPossibleSkillLevel,
                      showAcceleratedTrainingIcon: e,
                      skillSize: p,
                      blinkStyle: i,
                    }),
                    u.lastPossibleRoleLevel > 0 && d > 0 && b,
                  ),
              );
            },
          );
        var ne = t(3215),
          ae = t(4598),
          ie = t(9480);
        const le = (u) =>
          null !== u && "object" == typeof u
            ? "CoherentArrayProxy" === u.constructor.name
              ? ie.UI(u, (u) => ("object" == typeof u ? le(u) : u))
              : Array.isArray(u)
                ? u.map((u) => ("object" == typeof u ? le(u) : u))
                : Object.fromEntries(
                    Object.entries(u).map(([u, e]) => [u, "object" == typeof e ? le(e) : e]),
                  )
            : u;
        var se = t(3946);
        const oe = (0, ne.q)()(({ observableModel: u }) => {
            const e = Object.assign(
                {},
                u.primitives(["beforeLastSkillLevel", "afterLastSkillLevel"]),
                { tankmen: u.array("tankmen", []) },
              ),
              t = (0, se.Om)(
                () => {
                  return ((u = e.tankmen.get()), le(u));
                  var u;
                },
                { equals: ae.jv },
              ),
              r = (0, se.Om)(() => (0, ie.U2)(t(), 0), { equals: ae.jv }),
              n = (0, se.Om)(() => (0, ie.U2)(t(), 1), { equals: ae.jv });
            return Object.assign({}, e, { computes: { getTankmanBefore: r, getTankmanAfter: n } });
          }, ae.ZT),
          ce = oe[0],
          Ee = oe[1],
          Ae = "ResetResult_base_6d",
          _e = "ResetResult_skillsBefore_8d",
          de = "ResetResult_base__withSkills_2e",
          Fe = "ResetResult_base__withoutSkills_b4",
          me = "ResetResult_labelBefore_57",
          De = "ResetResult_skillsAfter_7b",
          Be = "ResetResult_labelAfter_17",
          Ce = "ResetResult_arrow_e7",
          ge = "ResetResult_noNewSkills_88",
          he = (0, h.Pi)(function () {
            const u = Ee().model.computes,
              e = u.getTankmanBefore,
              t = u.getTankmanAfter,
              r = e(),
              n = t(),
              i = null == n ? void 0 : n.newSkillsAmount,
              s = l()(Ae, n && i && de, n && !i && Fe);
            return a().createElement(
              "div",
              { className: s },
              r &&
                a().createElement(
                  "div",
                  { className: _e },
                  a().createElement("div", { className: me }, R.strings.dialogs.perksRest.before()),
                  a().createElement(re, { tankman: r, isSkillTooltipEnabled: !1 }),
                ),
              n &&
                a().createElement(
                  a().Fragment,
                  null,
                  a().createElement("div", { className: Ce }),
                  a().createElement(
                    "div",
                    { className: De },
                    a().createElement(
                      "div",
                      { className: Be },
                      R.strings.dialogs.perksRest.after(),
                    ),
                    i
                      ? a().createElement(re, { tankman: n, isSkillTooltipEnabled: !1 })
                      : a().createElement(
                          "div",
                          { className: ge },
                          R.strings.dialogs.perksRest.noNewPerks(),
                        ),
                  ),
                ),
            );
          }),
          pe = "PerksResetApp_base_e5",
          be = (0, h.Pi)(function () {
            return a().createElement(
              "div",
              { className: pe },
              a().createElement(p.u, {
                rootId: R.views.lobby.crew.dialogs.PerksResetContent("resId"),
              }),
              a().createElement(he, null),
            );
          });
        engine.whenReady.then(() => {
          g().render(
            a().createElement(
              ce,
              { options: { rootId: R.views.lobby.crew.dialogs.PerksResetContent("resId") } },
              a().createElement(B, null, a().createElement(be, null)),
            ),
            document.getElementById("root"),
          );
        });
      },
      5501: (u, e, t) => {
        "use strict";
        t.d(e, { u: () => z });
        var r = t(6179),
          n = t.n(r),
          a = t(3215),
          i = t(4598),
          l = t(9480),
          s = t(3946);
        const o = (0, a.q)()(
            ({ observableModel: u }) => {
              const e = { cardsList: u.array("cardsList", []) },
                t = (0, s.Om)(() => (0, l.UI)(e.cardsList.get(), i.yR), { equals: i.jv });
              return Object.assign({}, e, { computes: { cards: t } });
            },
            ({ externalModel: u }) => ({
              onCardClick: u.createCallback((u) => ({ index: u }), "onCardClick"),
            }),
          ),
          c = o[0],
          E = o[1];
        var A = t(6483),
          _ = t.n(A),
          d = t(5415),
          F = t(3403);
        let m, D;
        (!(function (u) {
          ((u.Default = "default"),
            (u.Reset = "reset"),
            (u.Retrain = "retrain"),
            (u.Recruit = "recruit"));
        })(m || (m = {})),
          (function (u) {
            ((u.Default = ""), (u.Disabled = "disabled"), (u.Selected = "selected"));
          })(D || (D = {})));
        var B = t(7727);
        const C = "CustomComponents_storage_c8",
          g = "CustomComponents_storageIcon_2c",
          h = "CustomComponents_storageCount_9b",
          p = (0, r.memo)(({ kwargs: u, cardType: e }) => {
            if (e === m.Reset) {
              const e = null == u ? void 0 : u.storageCount;
              return void 0 === e
                ? null
                : n().createElement(
                    "div",
                    { className: C },
                    n().createElement("div", { className: g }),
                    n().createElement("div", { className: h }, e),
                  );
            }
            return null;
          });
        var b = t(3618),
          v = t(9053),
          f = t(8018);
        const w = {
            base: "Description_base_bf",
            binding: "Description_binding_da",
            binding__highLight: "Description_binding__highLight_95",
            newSkillIcon: "Description_newSkillIcon_1b",
          },
          y = n().memo(function ({ description: u, cardType: e, kwargs: t, className: r }) {
            switch (e) {
              case m.Reset:
              case m.Retrain:
              case m.Recruit:
                return n().createElement(
                  "div",
                  { className: _()(w.base, r) },
                  n().createElement(b.w, {
                    text: u,
                    justifyContent: v.v2.Center,
                    binding: {
                      value: n().createElement(
                        "div",
                        {
                          className: _()(
                            w.binding,
                            (null == t ? void 0 : t.isHighlight) && w.binding__highlight,
                          ),
                        },
                        (0, f.T3)(null == t ? void 0 : t.value),
                      ),
                    },
                  }),
                );
              default:
                return n().createElement(
                  "div",
                  { className: _()(w.base, r) },
                  n().createElement(b.w, { text: u, justifyContent: v.v2.Center, binding: t }),
                );
            }
          });
        var k = t(7405),
          S = t(2056),
          x = t(5298);
        const L = "Price_base_3c",
          T = "Price_base__withPrice_ef";
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
            const a = (0, x.l)(e.type, { index: t });
            return u.value === u.discountValue && 0 === u.value
              ? n().createElement("div", { className: L }, R.strings.dialogs.priceCard.price.free())
              : n().createElement(
                  "div",
                  { className: _()(L, T) },
                  n().createElement(
                    S.u,
                    M({}, a, { targetId: r }),
                    n().createElement("div", null, n().createElement(k.F, u)),
                  ),
                );
          },
          I = "Title_base_5e",
          P = "Title_base__highLight_1c",
          N = n().memo(function ({ title: u, cardType: e, kwargs: t, className: r }) {
            switch (e) {
              case m.Reset:
              case m.Retrain:
              case m.Recruit:
                return n().createElement(
                  "div",
                  { className: _()(I, (null == t ? void 0 : t.isHighlight) && P, r) },
                  u,
                );
              default:
                return n().createElement("div", { className: _()(I, r) }, u);
            }
          }),
          H = {
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
            size: l = W.Big,
            title: s,
            description: o,
            cardType: c,
            kwargs: E,
            price: A,
            cardState: d,
            className: F,
          }) => {
            const m = d === D.Default,
              C = (0, r.useState)(!1),
              g = C[0],
              h = C[1],
              b = _()(H.base, H[`base__${l}`], H[`base__${d}`], g && H.base__hover, F),
              v = (0, r.useMemo)(() => (E ? JSON.parse(E) : {}), [E]),
              f = (0, r.useCallback)(() => {
                m && (B.$.playClick(), u(a));
              }, [a, m, u]),
              w = (0, r.useCallback)(() => {
                m && (B.$.playHighlight(), h(!0));
              }, [m]),
              k = (0, r.useCallback)(() => m && h(!1), [m]);
            return n().createElement(
              "div",
              { className: b, onClick: f, onMouseEnter: w, onMouseLeave: k },
              d === D.Disabled && n().createElement("div", { className: H.disabled }),
              d === D.Selected && n().createElement("div", { className: H.selected }),
              g && n().createElement("div", { className: H.hover }),
              n().createElement("div", {
                className: H.icon,
                style: { backgroundImage: `url(${i})` },
              }),
              n().createElement(N, { title: s, cardType: c, kwargs: v, className: H.title }),
              n().createElement(y, {
                description: o,
                cardType: c,
                kwargs: v,
                className: H.description,
              }),
              n().createElement(
                "div",
                { className: H.price },
                n().createElement(O, { cost: A, tooltip: t, index: a, tooltipRootId: e }),
              ),
              n().createElement(p, { cardType: c, kwargs: v }),
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
        const X = (0, F.Pi)(function ({ rootId: u, className: e }) {
            const t = E(),
              r = t.model,
              a = t.controls,
              i = (0, d.GS)().mediaWidth;
            return n().createElement(
              "div",
              { className: _()(G, e) },
              (0, l.UI)(r.computes.cards(), (e, t) =>
                n().createElement(
                  j,
                  $({}, e, {
                    key: `${t}-${e.cardState}`,
                    onClick: a.onCardClick,
                    index: t,
                    tooltipRootId: u,
                    size: i > d.cJ.ExtraSmall ? W.Big : W.Small,
                    className: U,
                  }),
                ),
              ),
            );
          }),
          z = n().memo(function ({
            rootId: u = R.views.lobby.crew.widgets.PriceList("resId"),
            className: e,
          }) {
            return n().createElement(
              c,
              { options: { rootId: u } },
              n().createElement(X, { rootId: u, className: e }),
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
            var l = t();
            void 0 !== l && (u = l);
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
    (__webpack_require__.j = 410),
    (() => {
      var u = { 410: 0, 897: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var r,
            n,
            [a, i, l] = t,
            s = 0;
          if (a.some((e) => 0 !== u[e])) {
            for (r in i) __webpack_require__.o(i, r) && (__webpack_require__.m[r] = i[r]);
            if (l) var o = l(__webpack_require__);
          }
          for (e && e(t); s < a.length; s++)
            ((n = a[s]), __webpack_require__.o(u, n) && u[n] && u[n][0](), (u[n] = 0));
          return __webpack_require__.O(o);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(5420));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
