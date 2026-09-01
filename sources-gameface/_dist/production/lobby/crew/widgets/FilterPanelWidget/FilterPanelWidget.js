(() => {
  var __webpack_modules__ = {
      3779: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => m });
        var r = t(6483),
          n = t.n(r),
          a = t(9887),
          o = t.n(a),
          i = t(3377),
          s = t(6179),
          l = t.n(s),
          c = t(5026);
        const E = [
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
        Object.keys(o());
        const A = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          F = (Object.keys(A), ["mt", "mr", "mb", "ml"]),
          d = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          m = (0, i.ZP)((u) => {
            let e = u.className,
              t = u.width,
              r = u.height,
              a = u.m,
              o = u.mt,
              i = void 0 === o ? a : o,
              m = u.mr,
              D = void 0 === m ? a : m,
              C = u.mb,
              B = void 0 === C ? a : C,
              g = u.ml,
              h = void 0 === g ? a : g,
              p = u.column,
              b = u.row,
              v = u.flexDirection,
              f = void 0 === v ? (p ? "column" : b && "row") || void 0 : v,
              w = u.flexStart,
              x = u.center,
              y = u.flexEnd,
              S = u.spaceBetween,
              M = u.spaceAround,
              O = u.justifyContent,
              T =
                void 0 === O
                  ? (w ? "flex-start" : x && "center") ||
                    (y && "flex-end") ||
                    (S && "space-between") ||
                    (M && "space-around") ||
                    void 0
                  : O,
              L = u.alignItems,
              R =
                void 0 === L
                  ? (w ? "flex-start" : x && "center") || (y && "flex-end") || void 0
                  : L,
              P = u.alignSelf,
              N = u.wrap,
              k = u.flexWrap,
              I = void 0 === k ? (N ? "wrap" : void 0) : k,
              H = u.grow,
              W = u.shrink,
              j = u.flex,
              Z = void 0 === j ? (H || W ? `${H ? 1 : 0} ${W ? 1 : 0} auto` : void 0) : j,
              G = u.style,
              U = u.children,
              z = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, E);
            const V = (0, s.useMemo)(() => {
                const u = { mt: i, mr: D, mb: B, ml: h },
                  e = ((u) =>
                    F.reduce((e, t) => {
                      const r = u[t];
                      return r && "number" != typeof r ? e.concat(A[!0 === r ? "MD" : r][t]) : e;
                    }, []))(u),
                  n = ((u) =>
                    F.reduce((e, t) => {
                      const r = u[t];
                      return ("number" == typeof r && (e[d[t]] = r + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, G, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: Z,
                    alignSelf: P,
                    display: f || R ? "flex" : void 0,
                    flexDirection: f,
                    flexWrap: I,
                    justifyContent: T,
                    alignItems: R,
                  }),
                  computedClassNames: e,
                };
              }, [t, r, i, D, B, h, G, Z, P, f, I, T, R]),
              X = V.computedStyle,
              K = V.computedClassNames;
            return l().createElement(
              "div",
              _({ className: n()(c.Z.base, ...K, e), style: X }, z),
              U,
            );
          });
      },
      3457: (u, e, t) => {
        "use strict";
        t.d(e, { L$: () => l.L, qE: () => l.q, u5: () => E });
        var r = t(6483),
          n = t.n(r),
          a = t(7727),
          o = t(6179),
          i = t.n(o),
          s = t(6880),
          l = t(2106);
        const c = ({
          children: u,
          size: e,
          isFocused: t,
          type: r,
          disabled: c,
          mixClass: E,
          soundHover: _,
          soundClick: A,
          onMouseEnter: F,
          onMouseMove: d,
          onMouseDown: m,
          onMouseUp: D,
          onMouseLeave: C,
          onClick: B,
        }) => {
          const g = (0, o.useRef)(null),
            h = (0, o.useState)(t),
            p = h[0],
            b = h[1],
            v = (0, o.useState)(!1),
            f = v[0],
            w = v[1],
            x = (0, o.useState)(!1),
            y = x[0],
            S = x[1],
            M = (0, o.useCallback)(() => {
              c || (g.current && (g.current.focus(), b(!0)));
            }, [c]),
            O = (0, o.useCallback)(
              (u) => {
                p && null !== g.current && !g.current.contains(u.target) && b(!1);
              },
              [p],
            ),
            T = (0, o.useCallback)(
              (u) => {
                c || (B && B(u));
              },
              [c, B],
            ),
            L = (0, o.useCallback)(
              (u) => {
                c || (null !== _ && (0, a.G)(_), F && F(u), S(!0));
              },
              [c, _, F],
            ),
            P = (0, o.useCallback)(
              (u) => {
                d && d(u);
              },
              [d],
            ),
            N = (0, o.useCallback)(
              (u) => {
                c || (D && D(u), w(!1));
              },
              [c, D],
            ),
            k = (0, o.useCallback)(
              (u) => {
                c || (null !== A && (0, a.G)(A), m && m(u), t && M(), w(!0));
              },
              [c, A, m, M, t],
            ),
            I = (0, o.useCallback)(
              (u) => {
                c || (C && C(u), w(!1));
              },
              [c, C],
            ),
            H = n()(
              s.Z.base,
              s.Z[`base__${r}`],
              {
                [s.Z.base__disabled]: c,
                [s.Z[`base__${e}`]]: e,
                [s.Z.base__focus]: p,
                [s.Z.base__highlightActive]: f,
                [s.Z.base__firstHover]: y,
              },
              E,
            ),
            W = n()(s.Z.state, s.Z.state__default);
          return (
            (0, o.useEffect)(
              () => (
                document.addEventListener("mousedown", O),
                () => {
                  document.removeEventListener("mousedown", O);
                }
              ),
              [O],
            ),
            (0, o.useEffect)(() => {
              b(t);
            }, [t]),
            i().createElement(
              "div",
              {
                ref: g,
                className: H,
                onMouseEnter: L,
                onMouseMove: P,
                onMouseUp: N,
                onMouseDown: k,
                onMouseLeave: I,
                onClick: T,
              },
              r !== l.L.ghost &&
                i().createElement(
                  i().Fragment,
                  null,
                  i().createElement("div", { className: s.Z.back }),
                  i().createElement("span", { className: s.Z.texture }),
                ),
              i().createElement(
                "span",
                { className: W },
                i().createElement("span", { className: s.Z.stateDisabled }),
                i().createElement("span", { className: s.Z.stateHighlightHover }),
                i().createElement("span", { className: s.Z.stateHighlightActive }),
              ),
              i().createElement(
                "span",
                { className: s.Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
                u,
              ),
            )
          );
        };
        c.defaultProps = {
          type: l.L.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const E = (0, o.memo)(c);
      },
      2106: (u, e, t) => {
        "use strict";
        let r, n;
        (t.d(e, { L: () => r, q: () => n }),
          (function (u) {
            ((u.main = "main"),
              (u.primary = "primary"),
              (u.primaryGreen = "primaryGreen"),
              (u.primaryRed = "primaryRed"),
              (u.secondary = "secondary"),
              (u.ghost = "ghost"));
          })(r || (r = {})),
          (function (u) {
            ((u.extraSmall = "extraSmall"), (u.small = "small"), (u.medium = "medium"));
          })(n || (n = {})));
      },
      9987: (u, e, t) => {
        "use strict";
        t.d(e, { A: () => c });
        var r = t(6483),
          n = t.n(r),
          a = t(6179),
          o = t.n(a),
          i = t(8055);
        const s = [
          "size",
          "value",
          "isEmpty",
          "fadeInAnimation",
          "hide",
          "maximumNumber",
          "className",
        ];
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
        const c = (u) => {
          let e = u.size,
            t = u.value,
            r = u.isEmpty,
            a = u.fadeInAnimation,
            c = u.hide,
            E = u.maximumNumber,
            _ = u.className,
            A = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, s);
          const F = r ? null : t,
            d = "string" == typeof F;
          if ((F && !d && F < 0) || 0 === F) return null;
          const m = F && !d && F > E,
            D = n()(
              i.Z.base,
              i.Z[`base__${e}`],
              a && i.Z.base__animated,
              c && i.Z.base__hidden,
              !F && i.Z.base__pattern,
              r && i.Z.base__empty,
              _,
            );
          return o().createElement(
            "div",
            l({ className: D }, A),
            o().createElement("div", { className: i.Z.bg }),
            o().createElement("div", { className: i.Z.pattern }),
            o().createElement(
              "div",
              { className: n()(i.Z.value, d && i.Z.value__text) },
              m ? E : F,
              m && o().createElement("span", { className: i.Z.plus }, "+"),
            ),
          );
        };
        c.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
      },
      280: (u, e, t) => {
        "use strict";
        t.d(e, { z: () => l });
        var r = t(6179),
          n = t.n(r),
          a = t(6483),
          o = t.n(a),
          i = t(3649),
          s = t(5287);
        const l = ({ binding: u, text: e = "", classMix: t, alignment: a = i.v2.left }) =>
          null === e
            ? (console.error("FormatText was supplied with 'null'"), null)
            : n().createElement(
                r.Fragment,
                null,
                e.split("\n").map((e, l) =>
                  n().createElement(
                    "div",
                    { className: o()(s.Z.base, t), key: `${e}-${l}` },
                    (0, i.Uw)(e, a, u).map((u, e) =>
                      n().createElement(r.Fragment, { key: `${e}-${u}` }, u),
                    ),
                  ),
                ),
              );
      },
      3495: (u, e, t) => {
        "use strict";
        t.d(e, { Y: () => E });
        var r = t(3138),
          n = t(6179),
          a = t(1043),
          o = t(5262);
        const i = r.O.client.getSize("rem"),
          s = i.width,
          l = i.height,
          c = Object.assign({ width: s, height: l }, (0, o.T)(s, l, a.j)),
          E = (0, n.createContext)(c);
      },
      1039: (u, e, t) => {
        "use strict";
        var r = t(6179),
          n = t.n(r),
          a = t(6536),
          o = t(3495),
          i = t(1043),
          s = t(5262),
          l = t(3138);
        (0, r.memo)(({ children: u }) => {
          const e = (0, r.useContext)(o.Y),
            t = (0, r.useState)(e),
            c = t[0],
            E = t[1],
            _ = (0, r.useCallback)((u, e) => {
              const t = l.O.view.pxToRem(u),
                r = l.O.view.pxToRem(e);
              E(Object.assign({ width: t, height: r }, (0, s.T)(t, r, i.j)));
            }, []);
          ((0, a.Z)(() => {
            engine.on("clientResized", _);
          }),
            (0, r.useEffect)(() => () => engine.off("clientResized", _), [_]));
          const A = (0, r.useMemo)(() => Object.assign({}, c), [c]);
          return n().createElement(o.Y.Provider, { value: A }, u);
        });
      },
      6010: (u, e, t) => {
        "use strict";
        var r = t(6179),
          n = t(7382),
          a = t(3495);
        const o = ["children"];
        const i = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, o);
          const i = (0, r.useContext)(a.Y),
            s = i.extraLarge,
            l = i.large,
            c = i.medium,
            E = i.small,
            _ = i.extraSmall,
            A = i.extraLargeWidth,
            F = i.largeWidth,
            d = i.mediumWidth,
            m = i.smallWidth,
            D = i.extraSmallWidth,
            C = i.extraLargeHeight,
            B = i.largeHeight,
            g = i.mediumHeight,
            h = i.smallHeight,
            p = i.extraSmallHeight,
            b = { extraLarge: C, large: B, medium: g, small: h, extraSmall: p };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && s) return e;
            if (t.large && l) return e;
            if (t.medium && c) return e;
            if (t.small && E) return e;
            if (t.extraSmall && _) return e;
          } else {
            if (t.extraLargeWidth && A) return (0, n.H)(e, t, b);
            if (t.largeWidth && F) return (0, n.H)(e, t, b);
            if (t.mediumWidth && d) return (0, n.H)(e, t, b);
            if (t.smallWidth && m) return (0, n.H)(e, t, b);
            if (t.extraSmallWidth && D) return (0, n.H)(e, t, b);
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
        (0, r.memo)(i);
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
        t.d(e, { YN: () => r.Y });
        (t(6010), t(1039));
        var r = t(3495);
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
      1037: (u, e, t) => {
        "use strict";
        t.d(e, { IC: () => r });
        var r,
          n = t(6483),
          a = t.n(n),
          o = t(6373),
          i = t(1856),
          s = t(3138),
          l = t(2039),
          c = t(5099),
          E = t(7727),
          _ = t(4179),
          A = t(6179),
          F = t.n(A),
          d = t(4769);
        !(function (u) {
          ((u[(u.Left = 0)] = "Left"),
            (u[(u.Right = 1)] = "Right"),
            (u[(u.Top = 2)] = "Top"),
            (u[(u.Bottom = 3)] = "Bottom"));
        })(r || (r = {}));
        const m = ["__left", "__right", "__top", "__bottom"];
        (0, A.forwardRef)(
          (
            { children: u, disableAutoSizeUpdate: e, onOutsideClick: t, customStyles: r = {} },
            n,
          ) => {
            const D = (0, A.useRef)(null),
              C = (0, A.useRef)(null),
              B = (0, A.useRef)(null),
              g = (0, A.useState)(window.decorator && window.decorator.directionType),
              h = g[0],
              p = g[1],
              b = (0, A.useCallback)(() => {
                (E.$.playClick(), s.O.view.sendEvent.close());
              }, []),
              v = (0, A.useCallback)(() => {
                E.$.playHighlight();
              }, []),
              f = a()(d.Z.arrow, d.Z[`arrow${m[h]}`]);
            (0, l.b)(
              () => (
                s.O.client.events.mouse.enableOutside(),
                s.O.client.events.mouse.down(([, u]) => {
                  "outside" === u && (t ? t() : s.O.view.sendEvent.close("popover"));
                })
              ),
            );
            const w = (0, A.useCallback)(
                (u) => {
                  let e = u.target;
                  do {
                    if (e === D.current || e === B.current) return;
                    e = e.parentNode;
                  } while (e);
                  const r = window.decorator;
                  if (void 0 !== window.decorator) {
                    const u = s.O.client.getMouseGlobalPosition(),
                      e = ![r.boundX, r.boundY, r.boundWidth, r.boundHeight].includes(void 0),
                      t =
                        u.x < r.boundX ||
                        u.x > r.boundX + r.boundWidth ||
                        u.y > r.boundY + r.boundHeight ||
                        u.y < r.boundY;
                    if (e && !t) return;
                  }
                  t ? t() : s.O.view.sendEvent.close("popover");
                },
                [D, B, t],
              ),
              x = (0, A.useCallback)(
                () => (
                  s.O.view.freezeTextureBeforeResize(),
                  (0, i.v)(() => {
                    if (C.current) {
                      const u = C.current.scrollWidth,
                        e = C.current.scrollHeight;
                      (s.O.view.resize(u, e), p(window.decorator.directionType));
                    }
                  })
                ),
                [],
              );
            return (
              (0, A.useImperativeHandle)(n, () => ({ updateSize: x })),
              (0, l.b)(() => {
                s.O.view.setInputPaddingsRem(58);
              }),
              (0, A.useEffect)(() => {
                document.addEventListener("mousedown", w, { capture: !0 });
                const u = (0, c.B)((0, _.Eu)());
                return (
                  !e && u.promise.then(() => x()),
                  () => {
                    (u.cancel(), document.removeEventListener("mousedown", w));
                  }
                );
              }, [x, w, e]),
              F().createElement(
                "div",
                { className: d.Z.base, ref: C },
                F().createElement(
                  "div",
                  { className: d.Z.decorator },
                  F().createElement(
                    "div",
                    { className: d.Z.content, ref: D },
                    u,
                    window.decorator &&
                      window.decorator.isCloseBtnVisible &&
                      F().createElement(
                        o.i,
                        { body: R.strings.dialogs.common.error.cancel() },
                        F().createElement("div", {
                          className: d.Z.closeBtn,
                          onClick: b,
                          onMouseEnter: v,
                          ref: B,
                        }),
                      ),
                  ),
                  F().createElement("div", { className: f, style: r.arrow }),
                ),
              )
            );
          },
        );
      },
      3616: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => l });
        var r = t(1037),
          n = t(4179),
          a = t(6179),
          o = t.n(a);
        const i = [
          "contentId",
          "decoratorId",
          "direction",
          "targetId",
          "args",
          "onClick",
          "children",
          "isEnabled",
        ];
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
        const l = (u) => {
          let e = u.contentId,
            t = u.decoratorId,
            l = u.direction,
            c = void 0 === l ? r.IC.Top : l,
            E = u.targetId,
            _ = u.args,
            A = u.onClick,
            F = u.children,
            d = u.isEnabled,
            m = void 0 === d || d,
            D = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, i);
          const C = (0, a.useRef)(null),
            B = (0, a.useCallback)(() => {
              if ((0, n.wU)()) return (0, n.SW)();
              C.current && (0, n.P3)(e, c, C.current, t, E, _);
            }, [e, c, _, t, E]);
          return o().createElement(
            "div",
            s(
              {
                ref: C,
                onClick:
                  ((g = F.props.onClick),
                  (u) => {
                    m && (B(), A && A(u), g && g(u));
                  }),
              },
              D,
            ),
            F,
          );
          var g;
        };
      },
      7613: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => v });
        var r = t(6483),
          n = t.n(r),
          a = t(3779),
          o = t(280),
          i = t(3532),
          s = t.n(i),
          l = t(9887),
          c = t.n(l),
          E = t(3377),
          _ = t(6179),
          A = t.n(_),
          F = t(3393);
        const d = [
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
        function m() {
          return (
            (m =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            m.apply(this, arguments)
          );
        }
        Object.keys(c());
        const D = Object.keys(s()),
          C = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          B = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          g = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          h = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          p =
            (Object.keys(h),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": C,
              "heading-H36": C,
              "heading-H28": B,
              "heading-H24": B,
              "heading-H24R": B,
              "heading-H22": B,
              "heading-H20R": B,
              "heading-H18": B,
              "heading-H15": g,
              "heading-H14": g,
              "paragraph-P24": B,
              "paragraph-P18": B,
              "paragraph-P16": B,
              "paragraph-P14": g,
              "paragraph-P12": g,
              "paragraph-P10": g,
            }),
          b =
            (Object.keys(p),
            (u) =>
              u
                ? ((u) => D.includes(u))(u)
                  ? { colorClassName: F.Z[u] }
                  : { colorStyle: { color: u } }
                : {}),
          v = (0, E.ZP)((u) => {
            let e = u.text,
              t = u.variant,
              r = u.className,
              i = u.color,
              s = u.m,
              l = u.mt,
              c = void 0 === l ? s : l,
              E = u.mr,
              D = void 0 === E ? s : E,
              C = u.mb,
              B = void 0 === C ? s : C,
              g = u.ml,
              h = void 0 === g ? s : g,
              v = u.style,
              f = u.format,
              w = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, d);
            const x = (0, _.useMemo)(() => {
                const u = b(i),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, v, r), colorClassName: e };
              }, [v, i]),
              y = x.computedStyle,
              S = x.colorClassName;
            return A().createElement(
              a.ZP,
              m(
                {
                  className: n()(F.Z.base, t && F.Z[t], S, r),
                  style: y,
                  mt: !0 === c ? p[t || "paragraph-P16"].mt : c,
                  mr: !0 === D ? p[t || "paragraph-P16"].mr : D,
                  mb: !0 === B ? p[t || "paragraph-P16"].mb : B,
                  ml: !0 === h ? p[t || "paragraph-P16"].ml : h,
                },
                w,
              ),
              void 0 !== f ? A().createElement(o.z, m({}, f, { text: e })) : e,
            );
          });
      },
      7078: (u, e, t) => {
        "use strict";
        t.d(e, { t: () => s });
        var r = t(6179),
          n = t.n(r),
          a = t(2056);
        const o = ["children"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            i.apply(this, arguments)
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
            })(u, o);
          return n().createElement(
            a.u,
            i(
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
          o = t(6373),
          i = t(2056);
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
          if (e.header || e.body) return n().createElement(o.i, e, r);
          const l = e.contentId,
            c = e.args,
            E = null == c ? void 0 : c.contentId;
          return l || E
            ? n().createElement(i.u, s({}, e, { contentId: l || E }), r)
            : n().createElement(a.t, e, r);
        };
      },
      6373: (u, e, t) => {
        "use strict";
        t.d(e, { i: () => l });
        var r = t(2056),
          n = t(6179),
          a = t.n(n);
        const o = ["children", "body", "header", "note", "alert", "args"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            i.apply(this, arguments)
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
              A = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, o);
            const F = (0, n.useMemo)(() => {
              const u = Object.assign({}, _, { body: t, header: l, note: c, alert: E });
              for (const e in u) void 0 === u[e] && delete u[e];
              return u;
            }, [E, t, l, c, _]);
            return a().createElement(
              r.u,
              i(
                {
                  contentId:
                    ((d = null == _ ? void 0 : _.hasHtmlContent),
                    d ? s.SimpleTooltipHtmlContent("resId") : s.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: F,
                },
                A,
              ),
              e,
            );
            var d;
          };
      },
      2056: (u, e, t) => {
        "use strict";
        t.d(e, { u: () => l });
        var r = t(7902),
          n = t(4179),
          a = t(6179);
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
        function i(u) {
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
              A = u.ignoreShowDelay,
              F = void 0 !== A && A,
              d = u.ignoreMouseClick,
              m = void 0 !== d && d,
              D = u.decoratorId,
              C = void 0 === D ? 0 : D,
              B = u.isEnabled,
              g = void 0 === B || B,
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
              })(u, o);
            const w = (0, a.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              x = (0, a.useMemo)(() => p || (0, r.F)().resId, [p]),
              y = (0, a.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (s(t, C, { isMouseEvent: !0, on: !0, arguments: i(n) }, x),
                  b && b(),
                  (w.current.isVisible = !0));
              }, [t, C, n, x, b]),
              S = (0, a.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const u = w.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (w.current.timeoutId = 0)),
                    s(t, C, { on: !1 }, x),
                    w.current.isVisible && v && v(),
                    (w.current.isVisible = !1));
                }
              }, [t, C, x, v]),
              M = (0, a.useCallback)((u) => {
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
                document.addEventListener("wheel", M, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", M, { capture: !0 }),
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
                        ((O = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(y, F ? 100 : 400)),
                            l && l(u),
                            O && O(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (S(), null == c || c(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === m && S(), null == _ || _(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === m && S(), null == E || E(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    f,
                  ),
                )
              : e;
            var O;
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
      1856: (u, e, t) => {
        "use strict";
        t.d(e, { v: () => r });
        const r = (u) => {
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
        };
      },
      8246: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => i });
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
        const o = (u) => (0 === u ? window : window.subViews.get(u));
        function i({
          initializer: u = !0,
          rootId: e = 0,
          getRoot: t = o,
          context: a = "model",
        } = {}) {
          const i = new Map();
          function s(u, e = 0) {
            viewEnv.removeDataChangedCallback(u, e)
              ? i.delete(u)
              : console.error("Can't remove callback by id:", u);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (u, e, t) => {
              t.forEach((e) => {
                const t = i.get(e);
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
              const o = "string" == typeof n ? `${a}.${n}` : a,
                s = r.O.view.addModelObserver(o, e, !0);
              return (i.set(s, t), u && t(l(n)), s);
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
              for (var u, t = n(i.keys()); !(u = t()).done;) {
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
          o = t.n(a),
          i = t(8246);
        const s = () => (u, e) => {
          const t = (0, a.createContext)({});
          return [
            function ({ mode: s = "real", options: l, children: c, mocks: E }) {
              const _ = (0, a.useRef)([]),
                A = (t, a, o) => {
                  var s;
                  const l = i.U(a),
                    c =
                      "real" === t
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (s = null == o ? void 0 : o.getter) ? s : () => {},
                          }),
                    E = (u) =>
                      "mocks" === t ? (null == o ? void 0 : o.getter(u)) : c.readByPath(u),
                    A = (u) => _.current.push(u),
                    F = u({
                      mode: t,
                      readByPath: E,
                      externalModel: c,
                      observableModel: {
                        array: (u, e) => {
                          const a = null != e ? e : E(u),
                            o = n.LO.box(a, { equals: r.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, n.aD)((u) => o.set(u)),
                                u,
                              ),
                            o
                          );
                        },
                        object: (u, e) => {
                          const a = null != e ? e : E(u),
                            o = n.LO.box(a, { equals: r.jv });
                          return (
                            "real" === t &&
                              c.subscribe(
                                (0, n.aD)((u) => o.set(u)),
                                u,
                              ),
                            o
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
                              o = Object.entries(a),
                              i = o.reduce((u, [e, t]) => ((u[t] = n.LO.box(r[e], {})), u), {});
                            return (
                              "real" === t &&
                                c.subscribe(
                                  (0, n.aD)((u) => {
                                    o.forEach(([e, t]) => {
                                      i[t].set(u[e]);
                                    });
                                  }),
                                  e,
                                ),
                              i
                            );
                          }
                        },
                      },
                      cleanup: A,
                    }),
                    d = { mode: t, model: F, externalModel: c, cleanup: A };
                  return {
                    model: F,
                    controls: "mocks" === t && o ? o.controls(d) : e(d),
                    externalModel: c,
                    mode: t,
                  };
                },
                F = (0, a.useRef)(!1),
                d = (0, a.useState)(s),
                m = d[0],
                D = d[1],
                C = (0, a.useState)(() => A(s, l, E)),
                B = C[0],
                g = C[1];
              return (
                (0, a.useEffect)(() => {
                  F.current ? g(A(m, l, E)) : (F.current = !0);
                }, [E, m, l]),
                (0, a.useEffect)(() => {
                  D(s);
                }, [s]),
                (0, a.useEffect)(
                  () => () => {
                    (B.externalModel.dispose(), _.current.forEach((u) => u()));
                  },
                  [B],
                ),
                o().createElement(t.Provider, { value: B }, c)
              );
            },
            () => (0, a.useContext)(t),
          ];
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
                  function s(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(a, s),
                    r(),
                    () => {
                      n &&
                        (i(), window.removeEventListener(a, s), (u.listeners -= 1), r(), (n = !1));
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
            extraSize: () => x,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => d,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => m,
            getSize: () => _,
            getViewGlobalPosition: () => F,
            isClientAccessible: () => h,
            isEventHandled: () => b,
            isFocused: () => g,
            pxToRem: () => D,
            remToPx: () => C,
            resize: () => A,
            sendEvent: () => o.qP,
            setAnimateWindow: () => B,
            setEventHandled: () => p,
            setInputPaddingsRem: () => s,
            setSidePaddingsRem: () => E,
            whenTutorialReady: () => y,
          }));
        var r = t(3722),
          n = t(6112),
          a = t(6538),
          o = t(8566);
        function i(u) {
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
        function A(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function F(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: C(e.x), y: C(e.y) };
        }
        function d() {
          viewEnv.freezeTextureBeforeResize();
        }
        function m() {
          return viewEnv.getScale();
        }
        function D(u) {
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
          o = 32,
          i = 64,
          s = (u, e) => {
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
          l = {
            close(u) {
              s("popover" === u ? n : o);
            },
            minimize() {
              s(i);
            },
            move(u) {
              s(a, { isMouseEvent: !0, on: u });
            },
          };
      },
      4598: (u, e, t) => {
        "use strict";
        t.d(e, { jv: () => r });
        function r() {
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
      3377: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => c });
        var r = t(5415),
          n = t(6179),
          a = t.n(n);
        const o = ["xl", "lg", "md", "sm", "xs"],
          i = (u) => u.includes("_") && ((u) => o.includes(u))(u.split("_").at(-1)),
          s = [r.cJ.ExtraLarge, r.cJ.Large, r.cJ.Medium, r.cJ.Small, r.cJ.ExtraSmall],
          l = (u, e) =>
            Object.keys(u).reduce((t, r) => {
              if (r in t) return t;
              if (i(r)) {
                const n = r.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const a = s.indexOf(e),
                  i = (-1 !== a ? o.slice(a) : [])
                    .map((u) => n + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  l = i ? u[i] : void 0;
                return ((t[n] = void 0 !== l ? l : u[n]), t);
              }
              const n = u[r];
              return (
                void 0 === n ||
                  ((u, e) => o.some((t) => void 0 !== e[`${u}_${t}`]))(r, u) ||
                  (t[r] = n),
                t
              );
            }, {}),
          c = (u, e = l) => {
            const t = (
              (u, e = l) =>
              (t) => {
                const o = (0, r.GS)().mediaSize,
                  i = (0, n.useMemo)(() => e(t, o), [t, o]);
                return a().createElement(u, i);
              }
            )(u, e);
            return a().memo((e) =>
              Object.keys(e).some((u) => i(u) && void 0 !== e[u])
                ? a().createElement(t, e)
                : a().createElement(u, e),
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
        t.d(e, { GS: () => l, cJ: () => o });
        var r = t(6179),
          n = t(7739),
          a = t(1043);
        let o, i, s;
        (!(function (u) {
          ((u[(u.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = a.j.small.width)] = "Small"),
            (u[(u.Medium = a.j.medium.width)] = "Medium"),
            (u[(u.Large = a.j.large.width)] = "Large"),
            (u[(u.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
        })(o || (o = {})),
          (function (u) {
            ((u[(u.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = a.j.small.width)] = "Small"),
              (u[(u.Medium = a.j.medium.width)] = "Medium"),
              (u[(u.Large = a.j.large.width)] = "Large"),
              (u[(u.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
          })(i || (i = {})),
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
                  return o.ExtraLarge;
                case u.large:
                  return o.Large;
                case u.medium:
                  return o.Medium;
                case u.small:
                  return o.Small;
                case u.extraSmall:
                  return o.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), o.ExtraSmall);
              }
            })(u),
            l = ((u) => {
              switch (!0) {
                case u.extraLargeWidth:
                  return i.ExtraLarge;
                case u.largeWidth:
                  return i.Large;
                case u.mediumWidth:
                  return i.Medium;
                case u.smallWidth:
                  return i.Small;
                case u.extraSmallWidth:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
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
      2039: (u, e, t) => {
        "use strict";
        t.d(e, { b: () => n });
        var r = t(6179);
        const n = (u) => {
          (0, r.useEffect)(u, []);
        };
      },
      3112: (u, e, t) => {
        "use strict";
        t.d(e, { V: () => a });
        var r = t(6179),
          n = t(3138);
        const a = () => {
          const u = (0, r.useState)(n.O.view.getScale()),
            e = u[0],
            t = u[1];
          return (
            (0, r.useEffect)(() => {
              const u = () => {
                t(n.O.view.getScale());
              };
              return (
                window.addEventListener("resize", u),
                () => {
                  window.removeEventListener("resize", u);
                }
              );
            }, []),
            e
          );
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
      5175: (u, e, t) => {
        "use strict";
        t.d(e, { c: () => a });
        var r = t(9480);
        const n = (u) =>
            null !== u && "object" == typeof u
              ? "CoherentArrayProxy" === u.constructor.name
                ? r.UI(u, (u) => ("object" == typeof u ? n(u) : u))
                : Array.isArray(u)
                  ? u.map((u) => ("object" == typeof u ? n(u) : u))
                  : Object.fromEntries(
                      Object.entries(u).map(([u, e]) => [u, "object" == typeof e ? n(e) : e]),
                    )
              : u,
          a = (u) => n(u);
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
      5099: (u, e, t) => {
        "use strict";
        t.d(e, { B: () => r });
        const r = (u) => {
          let e = !1;
          return {
            promise: new Promise((t, r) => {
              u.then((u) => !e && t(u)).catch((u) => !e && r(u));
            }),
            cancel() {
              e = !0;
            },
          };
        };
      },
      9690: (u, e, t) => {
        "use strict";
        t.d(e, { HG: () => o });
        const r = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          n = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const a = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          o = (u) =>
            a
              ? `${u}`
              : (function (u) {
                  let e = "";
                  for (let t = n.length - 1; t >= 0; t--)
                    for (; u >= n[t];) ((e += r[t]), (u -= n[t]));
                  return e;
                })(u);
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
        function n(u) {
          return u[0].toUpperCase() + u.slice(1);
        }
        (t.d(e, { Uw: () => E, e: () => n, v2: () => r }),
          (function (u) {
            ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
          })(r || (r = {})));
        const a = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          o = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          i = (u, e, t = r.left) => u.split(e).reduce(t === r.left ? a : o, []),
          s = (() => {
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
          l = ["zh_cn", "zh_sg", "zh_tw"],
          c = (u, e = r.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return l.includes(t)
              ? s(u)
              : ((u, e = r.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = u.replace(/&nbsp;/g, " ");
                  return (i(a, /( )/, e).forEach((u) => (t = t.concat(i(u, n, r.left)))), t);
                })(u, e);
          },
          E = (u, e, t) =>
            u.split(/%\((.*?)\)(?:[sd])?/g).map((u) => (t && u in t ? t[u] : c(u, e)));
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
        t.d(e, { B0: () => s, wU: () => v, ry: () => C, Eu: () => B, SW: () => p, P3: () => b });
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
        var A = t(5521),
          F = t(3138);
        const d = ["args"];
        function m(u, e, t, r, n, a, o) {
          try {
            var i = u[a](o),
              s = i.value;
          } catch (u) {
            return void t(u);
          }
          i.done ? e(s) : Promise.resolve(s).then(r, n);
        }
        const D = (u) => ({
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
                    function o(u) {
                      m(a, r, n, o, i, "next", u);
                    }
                    function i(u) {
                      m(a, r, n, o, i, "throw", u);
                    }
                    o(void 0);
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
                })(e, d);
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
          p = () => g(s.POP_OVER, { on: !1 }),
          b = (u, e, t, r, n = R.invalid("resId"), a) => {
            const o = F.O.view.getViewGlobalPosition(),
              i = t.getBoundingClientRect(),
              l = i.x,
              c = i.y,
              E = i.width,
              _ = i.height,
              A = {
                x: F.O.view.pxToRem(l) + o.x,
                y: F.O.view.pxToRem(c) + o.y,
                width: F.O.view.pxToRem(E),
                height: F.O.view.pxToRem(_),
              };
            g(s.POP_OVER, {
              isMouseEvent: !0,
              contentID: u,
              decoratorID: r || R.invalid("resId"),
              targetID: n,
              direction: e,
              bbox: D(A),
              on: !0,
              args: a,
            });
          },
          v = () => viewEnv.isWindowShownByViewEvent(s.POP_OVER),
          f = (u, e) => {
            u.keyCode === A.n.ESCAPE && e();
          };
        var w = t(7572);
        const x = n.instance,
          y = {
            DataTracker: a.Z,
            ViewModel: w.Z,
            ViewEventType: s,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: E,
            DateFormatType: _,
            makeGlobalBoundingBox: D,
            sendMoveEvent: (u) => g(s.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: h,
            sendClosePopOverEvent: p,
            sendShowContextMenuEvent: (u, e, t = 0) => {
              g(s.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: b,
            addEscapeListener: (u) => {
              const e = (e) => f(e, u);
              return (
                window.addEventListener("keydown", e),
                () => window.removeEventListener("keydown", e)
              );
            },
            closeOnEsc: (u) => {
              f(u, h);
            },
            handleViewEvent: g,
            onBindingsReady: C,
            onLayoutReady: B,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(s.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(s.CONTEXT_MENU),
            isPopOverShown: v,
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
            ClickOutsideManager: x,
            SystemLocale: o,
            UserLocale: i,
          };
        window.ViewEnvHelper = y;
      },
      9367: (u, e, t) => {
        "use strict";
        t.d(e, { Q: () => E });
        var r = t(6483),
          n = t.n(r),
          a = t(9987),
          o = t(6179),
          i = t.n(o);
        const s = "AlertCounter_base_f3",
          l = "AlertCounter_counter_da",
          c = "AlertCounter_label_18",
          E = ({ value: u, className: e }) =>
            i().createElement(
              "div",
              { className: n()(s, e) },
              i().createElement(a.A, { value: u, className: l }),
              !u &&
                i().createElement("div", { className: c }, R.strings.crew.common.exclamationMark()),
            );
      },
      9197: (u, e, t) => {
        "use strict";
        t.d(e, { C: () => b });
        var r = t(6483),
          n = t.n(r),
          a = t(3112),
          o = t(6179),
          i = t.n(o),
          s = t(7613),
          l = t(6373);
        const c = "NumberRange_base_5e",
          E = "NumberRange_base__animation_79",
          _ = "NumberRange_from_70",
          A = "NumberRange_from__red_f8",
          F = "NumberRange_separator_c0",
          d = R.strings.crew.barracks.berthsAmountDivider(),
          m = R.strings.crew.filterPanel.counter.selectLimit,
          D = (0, o.memo)(function ({
            isFilterRange: u,
            from: e,
            to: t,
            className: r,
            isSelectMode: a = !1,
            isSelectedLimitReached: o = !1,
          }) {
            return a
              ? i().createElement(
                  l.i,
                  { header: m.header(), body: m.body(), ignoreShowDelay: !0 },
                  i().createElement(
                    "div",
                    { className: n()(c, r) },
                    i().createElement(s.ZP, { className: _, text: String(e) }),
                    (e !== t || o) &&
                      i().createElement(
                        i().Fragment,
                        null,
                        i().createElement(s.ZP, { className: F, text: d }),
                        i().createElement(s.ZP, { text: String(t) }),
                      ),
                  ),
                )
              : u
                ? i().createElement(
                    "div",
                    { className: n()(c, 0 === e && E, r) },
                    i().createElement(s.ZP, {
                      className: n()(_, 0 === e && t > 0 && A),
                      text: String(e),
                    }),
                    e !== t &&
                      i().createElement(
                        i().Fragment,
                        null,
                        i().createElement(s.ZP, { className: F, text: d }),
                        i().createElement(s.ZP, { text: String(t) }),
                      ),
                  )
                : i().createElement(
                    "div",
                    { className: n()(c, e > t && E, r) },
                    i().createElement(s.ZP, { className: n()(_, e > t && A), text: String(e) }),
                    i().createElement(s.ZP, { className: F, text: d }),
                    i().createElement(s.ZP, { text: String(t) }),
                  );
          }),
          C = "NumberRangeWithLabel_base_2b",
          B = "NumberRangeWithLabel_title_94",
          g = "NumberRangeWithLabel_counter_00",
          h = "NumberRangeWithLabel_counterGlow_1f",
          p = "NumberRangeWithLabel_blink_89",
          b = (0, o.memo)(
            ({
              title: u,
              isGlowVisible: e = !1,
              isSelectedLimitReached: t = !1,
              isFilterRange: r = !1,
              isSelectMode: o = !1,
              className: l,
              classNames: c,
              from: E,
              to: _,
            }) => {
              const A = (0, a.V)(),
                F = {
                  left:
                    E !== _ || t
                      ? 7 * String(E).length * A + 4 * A
                      : Math.round((7 * String(E).length * A) / 2),
                };
              return i().createElement(
                "div",
                { className: n()(C, l) },
                i().createElement(s.ZP, { className: B, text: u }),
                i().createElement(
                  "div",
                  { className: g },
                  i().createElement(D, {
                    isFilterRange: r,
                    isSelectedLimitReached: t,
                    isSelectMode: o,
                    from: E,
                    to: _,
                  }),
                  e &&
                    r &&
                    i().createElement("div", {
                      style: F,
                      className: n()(h, t && p, null == c ? void 0 : c.counterGlow),
                    }),
                ),
              );
            },
          );
      },
      9631: (u, e, t) => {
        "use strict";
        t.d(e, { C: () => A });
        var r = t(6483),
          n = t.n(r),
          a = t(3457),
          o = t(2106),
          i = t(9987),
          s = t(6179),
          l = t.n(s),
          c = t(4723);
        const E = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
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
        const A = l().memo(function (u) {
          let e = u.isActive,
            t = u.counter,
            r = u.className,
            s = u.children,
            A = u.type,
            F = void 0 === A ? o.L.secondary : A,
            d = u.size,
            m = void 0 === d ? o.q.small : d,
            D = u.hasIndicator,
            C = void 0 === D || D,
            B = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                n = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, E);
          return l().createElement(
            "div",
            { className: n()(c.Z.base, r, e && c.Z.base__active) },
            l().createElement(a.u5, _({ type: F, size: m, mixClass: c.Z.button }, B), s),
            l().createElement("div", { className: c.Z.overlay }),
            C && l().createElement("div", { className: c.Z.indicator }),
            Boolean(t) &&
              l().createElement(
                "div",
                { className: c.Z.counter },
                l().createElement(i.A, { value: t, size: "small" }),
              ),
          );
        });
      },
      8018: (u, e, t) => {
        "use strict";
        t.d(e, { Er: () => a, Xd: () => n });
        t(3649);
        R.strings.common.percentValue();
        let r;
        !(function (u) {
          ((u.Objective = "objective"), (u.Possessive = "possessive"));
        })(r || (r = {}));
        const n = {
            header: R.strings.crew.filterPanel.counter.reset.header(),
            body: R.strings.crew.filterPanel.counter.reset.body(),
          },
          a = {
            header: R.strings.crew.filterPanel.counterMultySelect.reset.header(),
            body: R.strings.crew.filterPanel.counterMultySelect.reset.body(),
          };
        let o;
        !(function (u) {
          ((u.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (u.SHOP_INFO = "shop_info"),
            (u.RUDY = "rudy"));
        })(o || (o = {}));
      },
      5801: (u, e, t) => {
        "use strict";
        var r = t(6179),
          n = t.n(r),
          a = t(6483),
          o = t.n(a),
          i = t(3457),
          s = t(2106),
          l = t(7613),
          c = t(6373);
        let E;
        !(function (u) {
          ((u.Default = "default"),
            (u.Barracks = "barracks"),
            (u.MemberChange = "memberChange"),
            (u.TankChange = "tankChange"),
            (u.PersonalData = "personalData"));
        })(E || (E = {}));
        var _ = t(3403),
          A = t(3415),
          F = t(9480),
          d = t(9631);
        const m = "FilterTitle_base_a7",
          D = "FilterTitle_label_05",
          C = "FilterTitle_discount_42",
          B = "FilterTitle_discountIcon_30",
          g = ({ label: u, hasDiscount: e, className: t }) =>
            n().createElement(
              "div",
              { className: o()(m, t) },
              n().createElement("div", { className: D }, u),
              e &&
                n().createElement(
                  "div",
                  { className: C },
                  n().createElement("div", { className: B }),
                ),
            );
        let h;
        !(function (u) {
          ((u.Default = "default"),
            (u.Nation = "nation"),
            (u.Location = "location"),
            (u.TankmanRole = "tankmanRole"),
            (u.TankmanKind = "tankmanKind"),
            (u.VehicleGrade = "vehicleGrade"),
            (u.VehicleTier = "vehicleTier"),
            (u.VehicleType = "vehicleType"),
            (u.PersonalDataType = "personalDataType"),
            (u.VehicleCD = "vehicle"));
        })(h || (h = {}));
        var p = t(3649);
        const b = "ToggleIcon_base_59",
          v = "ToggleIcon_base__small_3e",
          f = "ToggleIcon_icon_e7",
          w = n().memo(function ({ icon: u, isSmall: e = !1, classNames: t }) {
            return n().createElement(
              "div",
              { className: o()(b, e && v) },
              n().createElement("div", {
                className: o()(f, null == t ? void 0 : t.icon),
                style: { backgroundImage: `url(${u})` },
              }),
            );
          });
        var x = t(9690);
        const y = "VehicleTier_base_9c",
          S = "VehicleTier_base__small_fc",
          M = ({ level: u, isSmall: e = !1 }) =>
            n().createElement("div", { className: o()(y, e && S) }, (0, x.HG)(u)),
          O = {
            icon__vehicleType: "ToggleButtonIcon_icon__vehicleType_83",
            icon__nation: "ToggleButtonIcon_icon__nation_c1",
            icon__vehicleGradePrimary: "ToggleButtonIcon_icon__vehicleGradePrimary_d6",
            icon__tankmanRole: "ToggleButtonIcon_icon__tankmanRole_4b",
            icon__selected: "ToggleButtonIcon_icon__selected_ca",
            icon__tankmanKind: "ToggleButtonIcon_icon__tankmanKind_5e",
            icon__vehicleGradeElite: "ToggleButtonIcon_icon__vehicleGradeElite_26",
            icon__locationRecruit: "ToggleButtonIcon_icon__locationRecruit_3b",
            icon__locationTankman: "ToggleButtonIcon_icon__locationTankman_f6",
            icon__locationUnique: "ToggleButtonIcon_icon__locationUnique_cb",
            icon__personalDataType: "ToggleButtonIcon_icon__personalDataType_a8",
            icon__tankmanKindDismissed: "ToggleButtonIcon_icon__tankmanKindDismissed_86",
            icon__vehicleGradePremium: "ToggleButtonIcon_icon__vehicleGradePremium_11",
          },
          T = ({ id: u, icon: e, type: t, isSmall: r = !0, isSelected: a = !1 }) =>
            t === h.VehicleTier
              ? n().createElement(M, { isSmall: r, level: Number(u) })
              : n().createElement(w, {
                  icon: e,
                  isSmall: r,
                  classNames: {
                    icon: o()(
                      O[`icon__${t}`],
                      O[`icon__${t}${(0, p.e)(u)}`],
                      a && O.icon__selected,
                    ),
                  },
                }),
          L = {
            base: "FilterToggleGroup_base_69",
            title: "FilterToggleGroup_title_65",
            content: "FilterToggleGroup_content_80",
            toggle: "FilterToggleGroup_toggle_d4",
            base__inPopup: "FilterToggleGroup_base__inPopup_11",
          };
        function P() {
          return (
            (P =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            P.apply(this, arguments)
          );
        }
        let N;
        !(function (u) {
          ((u.Default = "default"), (u.InPopup = "inPopup"));
        })(N || (N = {}));
        const k = ({ header: u, body: e, contentId: t, targetId: r }) =>
            t
              ? { contentId: t, targetId: r }
              : e || u
                ? { header: null != u ? u : void 0, body: null != e ? e : void 0 }
                : void 0,
          I = ({
            id: u,
            type: e,
            label: t,
            hasDiscount: r,
            filters: a,
            onClick: i,
            className: s,
            toggleProps: l,
            theme: c = N.Default,
          }) => {
            const E = c === N.InPopup;
            return n().createElement(
              "div",
              { className: o()(L.base, L[`base__${c}`], s) },
              E && n().createElement(g, { className: L.title, label: t, hasDiscount: r }),
              n().createElement(
                "div",
                { className: L.content },
                F.UI(a, ({ id: t, isSelected: r, tooltip: a, icon: s, counter: c }) =>
                  n().createElement(
                    A.l,
                    { key: t, tooltipArgs: k(a), className: L.toggle },
                    n().createElement(
                      d.C,
                      P({}, l, {
                        className: o()(L.toggle, null == l ? void 0 : l.className),
                        isActive: r,
                        onClick: () => (null == i ? void 0 : i(u, t)),
                        counter: c,
                      }),
                      n().createElement(T, { id: t, icon: s, type: e, isSmall: E, isSelected: r }),
                    ),
                  ),
                ),
              ),
            );
          };
        var H = t(9197),
          W = t(3215),
          j = t(4598),
          Z = t(5175),
          G = t(3946);
        const U = (0, W.q)()(
            ({ observableModel: u }) => {
              const e = {
                  root: u.object(),
                  amountInfo: u.object("amountInfo"),
                  filter: u.array("filter"),
                  filters: u.array("filter.filters"),
                },
                t = (0, G.Om)(() => (0, Z.c)(e.filter.get()), { equals: j.jv }),
                r = (0, G.Om)(() => (0, Z.c)(e.filters.get()), { equals: j.jv }),
                n = (0, G.Om)(
                  () =>
                    (0, Z.c)(e.filters.get()).filter((u) => "dismissed" === u.id && u.isSelected)
                      .length > 0,
                  { equals: j.jv },
                );
              return Object.assign({}, e, {
                computes: { getFilterGroup: t, getFilters: r, getIsRestoreFilter: n },
              });
            },
            ({ externalModel: u }) => ({
              search: u.createCallback((u) => ({ value: u }), "onSearch"),
              updateFilter: u.createCallback(
                (u, e) => ({ groupID: u, toggleID: e }),
                "onUpdateFilter",
              ),
              resetFilter: u.createCallbackNoArgs("onResetFilter"),
              updateSelectMode: u.createCallbackNoArgs("onSelectedModeChange"),
              onCancelSelection: u.createCallbackNoArgs("onCancelSelection"),
              onDismissOrRestore: u.createCallbackNoArgs("onDismissOrRestore"),
            }),
          ),
          z = (U[0], U[1]);
        var V = t(3616),
          X = t(1037),
          K = t(9367);
        const q = "PopupButton_base_7c",
          Y = "PopupButton_popupButtonLabel_ed",
          $ = "PopupButton_buttonIconWrapper_d7",
          J = "PopupButton_buttonIcon_e0",
          Q = "PopupButton_buttonIcon__isHighlighted_84",
          uu = "PopupButton_discountAlert_c8",
          eu = ({ isHighlighted: u, hasDiscountAlert: e, popoverDirection: t = X.IC.Bottom }) =>
            n().createElement(
              "div",
              { className: q },
              n().createElement(
                "div",
                { className: Y },
                R.strings.crew.filter.popup.button.title(),
              ),
              n().createElement(
                V.Z,
                {
                  contentId: R.views.lobby.crew.popovers.FilterPopoverView("resId"),
                  targetId: R.views.lobby.crew.widgets.FilterPanelWidget("resId"),
                  direction: t,
                },
                n().createElement(
                  "div",
                  { id: "popup_btn", className: $ },
                  n().createElement(
                    d.C,
                    { type: i.L$.ghost, size: i.qE.small, isActive: u, hasIndicator: !1 },
                    n().createElement("div", { className: o()(J, u && Q) }),
                  ),
                  e && n().createElement(K.Q, { className: uu }),
                ),
              ),
            );
        var tu = t(8018);
        const ru = "ResetButton_base_58",
          nu = "ResetButton_button_a5",
          au = "ResetButton_icon_4a",
          ou = ({ isSelectMode: u, onClick: e }) =>
            n().createElement(
              "div",
              { className: ru },
              n().createElement(
                c.i,
                u ? tu.Er : tu.Xd,
                n().createElement(
                  i.u5,
                  { mixClass: nu, onClick: e, type: i.L$.ghost, size: i.qE.small },
                  n().createElement("div", { className: au }),
                ),
              ),
            ),
          iu = "default",
          su = "search",
          lu = "email",
          cu = "password",
          Eu = "normal",
          _u = "disabled",
          Au = "alert",
          Fu = "error",
          du = "medium",
          mu = {
            [iu]: "",
            [lu]: R.strings.common.input.placeholder.email(),
            [su]: R.strings.common.input.placeholder.search(),
            [cu]: R.strings.common.input.placeholder.password(),
          },
          Du = { [iu]: "text", [lu]: "text", [su]: "text", [cu]: "password" },
          Cu = { [iu]: "", [lu]: "Invalid email", [su]: "", [cu]: "" },
          Bu = R.images.gui.maps.icons.components.input;
        function gu(u, e) {
          return (
            e !== lu ||
            (function (u) {
              const e = u.match(
                /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
              );
              return Boolean(e);
            })(u)
          );
        }
        var hu = t(7727);
        const pu = {
            base: "InputControl_base_68",
            base__focused: "InputControl_base__focused_aa",
            base__alert: "InputControl_base__alert_22",
            base__error: "InputControl_base__error_ff",
            base__done: "InputControl_base__done_a7",
            base__disabled: "InputControl_base__disabled_f8",
            input: "InputControl_input_93",
            base__small: "InputControl_base__small_85",
            base__medium: "InputControl_base__medium_a2",
            base__large: "InputControl_base__large_32",
            base__withIcon: "InputControl_base__withIcon_9e",
            input__search: "InputControl_input__search_85",
            disabled: "InputControl_disabled_78",
            placeholder: "InputControl_placeholder_e3",
            placeholder__search: "InputControl_placeholder__search_d5",
            icon: "InputControl_icon_13",
            icon__search: "InputControl_icon__search_57",
            clear: "InputControl_clear_bb",
          },
          bu = n().memo(
            ({
              componentId: u,
              value: e = "",
              type: t = iu,
              size: a = du,
              variant: i = Eu,
              placeholder: s = "",
              highlighted: l,
              withClear: c,
              selectOnFocus: E = !0,
              maxLength: _,
              iconSource: A,
              classMix: F,
              onMouseEnter: d,
              onMouseLeave: m,
              onMouseDown: D,
              onMouseUp: C,
              onClick: B,
              onChange: g,
              onClear: h,
              onFocus: p,
              onBlur: b,
            }) => {
              const v = (0, r.useState)(!1),
                f = v[0],
                w = v[1],
                x = (0, r.useRef)(null),
                y = (0, r.useRef)({ mouseOver: !1, mouseDown: !1 }),
                S = i !== _u,
                M = (0, r.useCallback)(
                  (u) => {
                    S && (w(!0), p && p(u));
                  },
                  [S, p],
                ),
                O = (0, r.useCallback)(
                  (u) => {
                    S && !y.current.mouseOver && (w(!1), b && b(u));
                  },
                  [S, b],
                );
              (0, r.useEffect)(() => {
                S && f && E && x.current && x.current.select();
              }, [E, f, S]);
              const T = (0, r.useCallback)(
                  (u) => {
                    S && g && g(u.target.value);
                  },
                  [S, g],
                ),
                L = (0, r.useCallback)(
                  (u) => {
                    S && ((y.current.mouseOver = !0), d && d(u));
                  },
                  [S, d],
                ),
                R = (0, r.useCallback)(
                  (u) => {
                    S &&
                      x.current &&
                      (y.current.mouseDown && x.current.focus(),
                      (y.current.mouseOver = !1),
                      m && m(u));
                  },
                  [S, m],
                ),
                P = (0, r.useCallback)(
                  (u) => {
                    S && ((y.current.mouseDown = !0), D && D(u));
                  },
                  [S, D],
                ),
                N = (0, r.useCallback)(
                  (u) => {
                    S && ((y.current.mouseDown = !1), C && C(u));
                  },
                  [S, C],
                ),
                k = (0, r.useCallback)(
                  (u) => {
                    if (S && x.current) {
                      ((!f || (f && u.target !== x.current)) && x.current.focus(), B && B(u));
                    }
                  },
                  [f, S, B],
                ),
                I = s || mu[t],
                H = Boolean(A),
                W = o()(
                  pu.base,
                  pu[`base__${a}`],
                  l && pu[`base__${i}`],
                  f && pu.base__focused,
                  H && pu.base__withIcon,
                  F,
                ),
                j = (0, r.useMemo)(() => (A ? { backgroundImage: `url(${A})` } : null), [A]),
                Z = o()(pu.input, pu[`input__${t}`]),
                G = o()(pu.icon, pu[`icon__${t}`]),
                U = o()(pu.placeholder, pu[`placeholder__${t}`]);
              return n().createElement(
                "div",
                {
                  id: u,
                  className: W,
                  onMouseEnter: L,
                  onMouseDown: P,
                  onMouseUp: N,
                  onMouseLeave: R,
                  onClick: k,
                },
                !S && n().createElement("div", { className: pu.disabled }),
                j && n().createElement("div", { style: j, className: G }),
                n().createElement("input", {
                  ref: x,
                  className: Z,
                  type: Du[t],
                  value: e,
                  onChange: T,
                  disabled: !S,
                  onFocus: M,
                  onBlur: O,
                  maxLength: _,
                }),
                I && !e && !f && n().createElement("div", { className: U }, I),
                c &&
                  n().createElement("div", {
                    className: pu.clear,
                    onClick: (u) => {
                      (hu.$.playClick(), h && h(u));
                    },
                    onMouseEnter: hu.$.playHighlight,
                  }),
              );
            },
          ),
          vu = {
            base: "HelperMessage_base_1e",
            base__shown: "HelperMessage_base__shown_ab",
            icon: "HelperMessage_icon_10",
            message: "HelperMessage_message_f4",
            message__alert: "HelperMessage_message__alert_b5",
            message__error: "HelperMessage_message__error_45",
            message__done: "HelperMessage_message__done_2b",
          },
          fu = ({ variant: u, show: e = !0, helperText: t, helperIcon: a, classMix: i }) => {
            const s = (0, r.useMemo)(() => {
                const e =
                  a ||
                  (function (u) {
                    return u === Au ? R.images.gui.maps.icons.library.alertIcon() : "";
                  })(u);
                return e && { backgroundImage: `url(${e})` };
              }, [a, u]),
              l = o()(vu.base, e && vu.base__shown),
              c = o()(vu.message, vu[`message__${u}`], i);
            return n().createElement(
              "div",
              { className: l },
              s && n().createElement("div", { className: vu.icon, style: s }),
              n().createElement("div", { className: c }, t),
            );
          },
          wu = {
            base: "Input_base_cd",
            base__small: "Input_base__small_c7",
            base__medium: "Input_base__medium_1f",
            base__large: "Input_base__large_11",
            helper: "Input_helper_ea",
          },
          xu = [
            "componentId",
            "type",
            "variant",
            "size",
            "value",
            "tooltipArgs",
            "helperText",
            "isValidated",
            "showHelper",
            "error",
            "options",
            "onFocus",
            "onMouseEnter",
            "onMouseLeave",
            "onMouseUp",
            "onMouseDown",
            "onChange",
            "classMix",
            "controlClassMix",
            "helperClassMix",
          ];
        function yu() {
          return (
            (yu =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var r in t) Object.prototype.hasOwnProperty.call(t, r) && (u[r] = t[r]);
                }
                return u;
              }),
            yu.apply(this, arguments)
          );
        }
        const Su = {
            debounceTime: 200,
            performChangeValidation: !0,
            selectOnFocus: !0,
            withTypeIcon: !0,
            disableHighlightOnFocus: !0,
          },
          Mu = (u) => {
            let e = u.componentId,
              t = u.type,
              a = void 0 === t ? iu : t,
              i = u.variant,
              s = void 0 === i ? Eu : i,
              l = u.size,
              c = void 0 === l ? du : l,
              E = u.value,
              _ = u.tooltipArgs,
              F = u.helperText,
              d = void 0 === F ? "" : F,
              m = u.isValidated,
              D = void 0 === m || m,
              C = u.showHelper,
              B = void 0 === C || C,
              g = u.error,
              h = u.options,
              p = u.onFocus,
              b = u.onMouseEnter,
              v = u.onMouseLeave,
              f = u.onMouseUp,
              w = u.onMouseDown,
              x = u.onChange,
              y = u.classMix,
              S = u.controlClassMix,
              M = u.helperClassMix,
              O = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  n = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, xu);
            const T = (0, r.useState)(E),
              L = T[0],
              R = T[1],
              P = (0, r.useState)(D),
              N = P[0],
              k = P[1],
              I = (0, r.useMemo)(() => Object.assign({}, Su, h), [h]),
              H = (0, r.useRef)({ debounceTimeout: 0, isChangeHandled: !0, value: E, type: a }),
              W = (0, r.useCallback)((u) => {
                u !== H.current.value &&
                  ((H.current.value = u), (H.current.isChangeHandled = !1), R(u));
              }, []),
              j = (0, r.useCallback)(
                (u) => {
                  let e = !0;
                  (I.performChangeValidation &&
                    (e = I.changesValidator ? I.changesValidator(u) : gu(u, H.current.type)),
                    x && x(u, e));
                },
                [x, I],
              ),
              Z = (0, r.useCallback)(() => {
                H.current.debounceTimeout &&
                  (window.clearTimeout(H.current.debounceTimeout), (H.current.debounceTimeout = 0));
              }, []),
              G = (0, r.useCallback)(() => W(""), [W]);
            (0, r.useEffect)(() => () => Z(), [Z]);
            const U = (0, r.useCallback)(
              (u) => {
                (Z(),
                  I.debounceTime
                    ? (H.current.debounceTimeout = window.setTimeout(() => {
                        j(u);
                      }, I.debounceTime))
                    : j(u));
              },
              [j, Z, I.debounceTime],
            );
            ((0, r.useEffect)(() => {
              H.current.isChangeHandled ||
                H.current.value !== L ||
                (U(H.current.value), (H.current.isChangeHandled = !0));
            }, [L, U]),
              (0, r.useEffect)(() => {
                (H.current.isChangeHandled &&
                  E !== H.current.value &&
                  ((H.current.value = E), R(E)),
                  (H.current.type = a));
              }, [E, a]),
              (0, r.useEffect)(() => {
                k(D);
              }, [D, s]));
            const z = (0, r.useCallback)((u) => b && b(u), [b]),
              V = (0, r.useCallback)(
                (u) => {
                  (I.disableHighlightOnFocus && N && k(!1), p && p(u));
                },
                [N, p, I.disableHighlightOnFocus],
              ),
              X = (0, r.useCallback)((u) => f && f(u), [f]),
              K = (0, r.useCallback)((u) => w && w(u), [w]),
              q = (0, r.useCallback)((u) => v && v(u), [v]),
              Y = (0, r.useMemo)(
                () =>
                  I.withTypeIcon
                    ? (function (u, e) {
                        return u === su ? Bu.$dyn(`search_${e}`) : "";
                      })(a, c)
                    : "",
                [a, c, I.withTypeIcon],
              ),
              $ = d || Cu[a],
              J = Boolean(L),
              Q = g ? Fu : s,
              uu = Boolean(g) || N,
              eu = (0, r.useMemo)(
                () => ("boolean" == typeof I.withClear ? J && I.withClear : J && a === su),
                [a, J, I],
              ),
              tu = o()(wu.base, wu[`base__${c}`], wu[`base__${s}`], y);
            return n().createElement(
              "div",
              {
                id: e,
                className: tu,
                onMouseEnter: z,
                onMouseDown: K,
                onMouseUp: X,
                onMouseLeave: q,
              },
              n().createElement(
                A.l,
                { tooltipArgs: _ },
                n().createElement(
                  bu,
                  yu(
                    {
                      componentId: e ? `${e}-inputControl` : void 0,
                      iconSource: Y,
                      size: c,
                      type: a,
                      variant: Q,
                      value: L,
                      withClear: eu,
                      highlighted: uu,
                      selectOnFocus: I.selectOnFocus,
                      maxLength: I.maxLength,
                      classMix: S,
                      onFocus: V,
                      onChange: W,
                      onClear: G,
                    },
                    O,
                  ),
                ),
              ),
              $ &&
                n().createElement(
                  "div",
                  { className: wu.helper },
                  n().createElement(fu, {
                    variant: Q,
                    show: B && (I.isPermanentHelper || uu),
                    helperText: g || $,
                    helperIcon: I.helperIconSource,
                    classMix: M,
                  }),
                ),
            );
          },
          Ou = ({
            value: u,
            placeholder: e,
            tooltipHeader: t,
            onChange: r,
            className: a,
            tooltipBody: o,
          }) =>
            n().createElement(
              c.i,
              { header: null != t ? t : void 0, body: o, isEnabled: Boolean(t || o) },
              n().createElement(Mu, {
                type: su,
                placeholder: null != e ? e : void 0,
                value: u,
                classMix: a,
                onChange: r,
              }),
            ),
          Tu = {
            base: "FilterPanelWidgetApp_base_1c",
            titleWrapper: "FilterPanelWidgetApp_titleWrapper_1b",
            title: "FilterPanelWidgetApp_title_ad",
            filters: "FilterPanelWidgetApp_filters_0d",
            counterGlow: "FilterPanelWidgetApp_counterGlow_df",
            separator: "FilterPanelWidgetApp_separator_9e",
            filterLabel: "FilterPanelWidgetApp_filterLabel_5b",
            base__tankChange: "FilterPanelWidgetApp_base__tankChange_ff",
            base__memberChange: "FilterPanelWidgetApp_base__memberChange_18",
            popupButtonWrapper: "FilterPanelWidgetApp_popupButtonWrapper_4c",
            base__personalData: "FilterPanelWidgetApp_base__personalData_1d",
            search: "FilterPanelWidgetApp_search_0e",
            chooseButton: "FilterPanelWidgetApp_chooseButton_2b",
            button: "FilterPanelWidgetApp_button_8e",
            button__demobilize: "FilterPanelWidgetApp_button__demobilize_d8",
          };
        var Lu = t(5415);
        const Ru = R.strings.crew.filterPanel;
        (0, _.Pi)(({ popoverDirection: u }) => {
          const e = z(),
            t = e.model,
            r = e.controls,
            a = t.root.get(),
            _ = a.hasDiscountAlert,
            A = a.isPopoverHighlighted,
            F = a.isPopoverEnabled,
            d = a.searchTooltipBody,
            m = a.searchTooltipHeader,
            D = a.searchPlaceholder,
            C = a.searchString,
            B = a.isSearchEnabled,
            g = a.title,
            h = a.panelType,
            p = a.hasAppliedFilters,
            b = a.popoverTooltipHeader,
            v = a.popoverTooltipBody,
            f = a.isSelectedMode,
            w = a.isSelectButtonVisible,
            x = a.isSelectButtonActive,
            y = a.isSelectedLimitReached,
            S = t.amountInfo.get(),
            M = S.from,
            O = S.to,
            T = t.computes.getFilterGroup(),
            L = t.computes.getFilters(),
            P = t.computes.getIsRestoreFilter(),
            N = p || (0 === M && 0 === O) || f,
            k =
              (0, Lu.GS)().mediaSize === Lu.cJ.ExtraSmall && f
                ? R.strings.crew.tankmanList.selected.titleSmall()
                : g;
          return n().createElement(
            "div",
            { className: o()(Tu.base, Tu[`base__${h}`]) },
            n().createElement(
              "div",
              { className: Tu.titleWrapper },
              n().createElement(H.C, {
                title: k || "",
                isGlowVisible: N,
                isSelectedLimitReached: y,
                isFilterRange: !0,
                isSelectMode: f,
                from: M,
                to: O,
                className: Tu.title,
                classNames: { counterGlow: Tu.counterGlow },
              }),
              p && n().createElement(ou, { isSelectMode: f, onClick: r.resetFilter }),
            ),
            n().createElement(
              "div",
              { className: Tu.filters },
              B &&
                n().createElement(
                  n().Fragment,
                  null,
                  n().createElement(Ou, {
                    value: C,
                    onChange: r.search,
                    className: Tu.search,
                    placeholder: D,
                    tooltipHeader: m,
                    tooltipBody: d,
                  }),
                  h === E.Barracks && w && n().createElement("div", { className: Tu.separator }),
                ),
              T.label && n().createElement(l.ZP, { className: Tu.filterLabel, text: T.label }),
              w &&
                (f
                  ? n().createElement(
                      n().Fragment,
                      null,
                      n().createElement(
                        i.u5,
                        { mixClass: Tu.button, type: s.L.primary, onClick: r.onCancelSelection },
                        n().createElement(l.ZP, { text: Ru.demobilize.cancel() }),
                      ),
                      n().createElement(
                        i.u5,
                        {
                          mixClass: o()(Tu.button, Tu.button__demobilize),
                          type: s.L.main,
                          onClick: r.onDismissOrRestore,
                          disabled: !x,
                        },
                        n().createElement(l.ZP, {
                          text: P ? Ru.restore.confirm() : Ru.demobilize.confirm(),
                        }),
                      ),
                    )
                  : n().createElement(
                      i.u5,
                      { mixClass: Tu.button, type: s.L.secondary, onClick: r.updateSelectMode },
                      n().createElement(l.ZP, { text: Ru.selectMode.title() }),
                    )),
              (w || B) && n().createElement("div", { className: Tu.separator }),
              n().createElement(I, {
                id: T.id,
                label: T.label,
                type: T.type,
                hasDiscount: T.hasDiscount,
                filters: L,
                toggleProps: { type: s.L.ghost },
                onClick: r.updateFilter,
              }),
              F &&
                n().createElement(
                  c.i,
                  { header: b || void 0, body: v || void 0, isEnabled: Boolean(b || v) },
                  n().createElement(
                    "div",
                    { className: Tu.popupButtonWrapper },
                    n().createElement(eu, {
                      isHighlighted: A,
                      hasDiscountAlert: _,
                      popoverDirection: u,
                    }),
                  ),
                ),
            ),
          );
        });
      },
      5026: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
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
        };
      },
      6880: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
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
      },
      8055: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
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
        };
      },
      5287: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = { base: "FormatText_base_d0" };
      },
      4769: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
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
      },
      3393: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
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
        };
      },
      4723: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = {
          base: "ToggleButton_base_09",
          overlay: "ToggleButton_overlay_76",
          base__active: "ToggleButton_base__active_05",
          button: "ToggleButton_button_14",
          indicator: "ToggleButton_indicator_c2",
          counter: "ToggleButton_counter_86",
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
          for (var [e, t, r] = deferred[s], a = !0, o = 0; o < e.length; o++)
            (!1 & r || n >= r) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[o]))
              ? e.splice(o--, 1)
              : ((a = !1), r < n && (n = r));
          if (a) {
            deferred.splice(s--, 1);
            var i = t();
            void 0 !== i && (u = i);
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
    (__webpack_require__.j = 595),
    (() => {
      var u = { 595: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var r,
            n,
            [a, o, i] = t,
            s = 0;
          if (a.some((e) => 0 !== u[e])) {
            for (r in o) __webpack_require__.o(o, r) && (__webpack_require__.m[r] = o[r]);
            if (i) var l = i(__webpack_require__);
          }
          for (e && e(t); s < a.length; s++)
            ((n = a[s]), __webpack_require__.o(u, n) && u[n] && u[n][0](), (u[n] = 0));
          return __webpack_require__.O(l);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(5801));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
