(() => {
  var __webpack_modules__ = {
      3779: (e, t, a) => {
        "use strict";
        a.d(t, { ZP: () => b });
        var n = a(6483),
          r = a.n(n),
          u = a(9887),
          s = a.n(u),
          i = a(3377),
          l = a(6179),
          o = a.n(l),
          c = a(5026);
        const m = [
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
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        Object.keys(s());
        const _ = {
            XL: { mt: c.Z.mt__XL, mr: c.Z.mr__XL, mb: c.Z.mb__XL, ml: c.Z.ml__XL },
            LG: { mt: c.Z.mt__LG, mr: c.Z.mr__LG, mb: c.Z.mb__LG, ml: c.Z.ml__LG },
            MDp: { mt: c.Z.mt__MDp, mr: c.Z.mr__MDp, mb: c.Z.mb__MDp, ml: c.Z.ml__MDp },
            MD: { mt: c.Z.mt__MD, mr: c.Z.mr__MD, mb: c.Z.mb__MD, ml: c.Z.ml__MD },
            SMp: { mt: c.Z.mt__SMp, mr: c.Z.mr__SMp, mb: c.Z.mb__SMp, ml: c.Z.ml__SMp },
            SM: { mt: c.Z.mt__SM, mr: c.Z.mr__SM, mb: c.Z.mb__SM, ml: c.Z.ml__SM },
            XS: { mt: c.Z.mt__XS, mr: c.Z.mr__XS, mb: c.Z.mb__XS, ml: c.Z.ml__XS },
          },
          E = (Object.keys(_), ["mt", "mr", "mb", "ml"]),
          g = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          b = (0, i.ZP)((e) => {
            let t = e.className,
              a = e.width,
              n = e.height,
              u = e.m,
              s = e.mt,
              i = void 0 === s ? u : s,
              b = e.mr,
              p = void 0 === b ? u : b,
              v = e.mb,
              h = void 0 === v ? u : v,
              A = e.ml,
              C = void 0 === A ? u : A,
              f = e.column,
              D = e.row,
              F = e.flexDirection,
              B = void 0 === F ? (f ? "column" : D && "row") || void 0 : F,
              k = e.flexStart,
              w = e.center,
              y = e.flexEnd,
              S = e.spaceBetween,
              N = e.spaceAround,
              I = e.justifyContent,
              T =
                void 0 === I
                  ? (k ? "flex-start" : w && "center") ||
                    (y && "flex-end") ||
                    (S && "space-between") ||
                    (N && "space-around") ||
                    void 0
                  : I,
              L = e.alignItems,
              x =
                void 0 === L
                  ? (k ? "flex-start" : w && "center") || (y && "flex-end") || void 0
                  : L,
              R = e.alignSelf,
              M = e.wrap,
              P = e.flexWrap,
              O = void 0 === P ? (M ? "wrap" : void 0) : P,
              H = e.grow,
              W = e.shrink,
              G = e.flex,
              V = void 0 === G ? (H || W ? `${H ? 1 : 0} ${W ? 1 : 0} auto` : void 0) : G,
              z = e.style,
              Z = e.children,
              j = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, m);
            const $ = (0, l.useMemo)(() => {
                const e = { mt: i, mr: p, mb: h, ml: C },
                  t = ((e) =>
                    E.reduce((t, a) => {
                      const n = e[a];
                      return n && "number" != typeof n ? t.concat(_[!0 === n ? "MD" : n][a]) : t;
                    }, []))(e),
                  r = ((e) =>
                    E.reduce((t, a) => {
                      const n = e[a];
                      return ("number" == typeof n && (t[g[a]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, z, r, {
                    width: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: V,
                    alignSelf: R,
                    display: B || x ? "flex" : void 0,
                    flexDirection: B,
                    flexWrap: O,
                    justifyContent: T,
                    alignItems: x,
                  }),
                  computedClassNames: t,
                };
              }, [a, n, i, p, h, C, z, V, R, B, O, T, x]),
              U = $.computedStyle,
              X = $.computedClassNames;
            return o().createElement(
              "div",
              d({ className: r()(c.Z.base, ...X, t), style: U }, j),
              Z,
            );
          });
      },
      3457: (e, t, a) => {
        "use strict";
        a.d(t, { L$: () => o.L, qE: () => o.q, u5: () => m });
        var n = a(6483),
          r = a.n(n),
          u = a(7727),
          s = a(6179),
          i = a.n(s),
          l = a(6880),
          o = a(2106);
        const c = ({
          children: e,
          size: t,
          isFocused: a,
          type: n,
          disabled: c,
          mixClass: m,
          soundHover: d,
          soundClick: _,
          onMouseEnter: E,
          onMouseMove: g,
          onMouseDown: b,
          onMouseUp: p,
          onMouseLeave: v,
          onClick: h,
        }) => {
          const A = (0, s.useRef)(null),
            C = (0, s.useState)(a),
            f = C[0],
            D = C[1],
            F = (0, s.useState)(!1),
            B = F[0],
            k = F[1],
            w = (0, s.useState)(!1),
            y = w[0],
            S = w[1],
            N = (0, s.useCallback)(() => {
              c || (A.current && (A.current.focus(), D(!0)));
            }, [c]),
            I = (0, s.useCallback)(
              (e) => {
                f && null !== A.current && !A.current.contains(e.target) && D(!1);
              },
              [f],
            ),
            T = (0, s.useCallback)(
              (e) => {
                c || (h && h(e));
              },
              [c, h],
            ),
            L = (0, s.useCallback)(
              (e) => {
                c || (null !== d && (0, u.G)(d), E && E(e), S(!0));
              },
              [c, d, E],
            ),
            x = (0, s.useCallback)(
              (e) => {
                g && g(e);
              },
              [g],
            ),
            M = (0, s.useCallback)(
              (e) => {
                c || (p && p(e), k(!1));
              },
              [c, p],
            ),
            P = (0, s.useCallback)(
              (e) => {
                c || (null !== _ && (0, u.G)(_), b && b(e), a && N(), k(!0));
              },
              [c, _, b, N, a],
            ),
            O = (0, s.useCallback)(
              (e) => {
                c || (v && v(e), k(!1));
              },
              [c, v],
            ),
            H = r()(
              l.Z.base,
              l.Z[`base__${n}`],
              {
                [l.Z.base__disabled]: c,
                [l.Z[`base__${t}`]]: t,
                [l.Z.base__focus]: f,
                [l.Z.base__highlightActive]: B,
                [l.Z.base__firstHover]: y,
              },
              m,
            ),
            W = r()(l.Z.state, l.Z.state__default);
          return (
            (0, s.useEffect)(
              () => (
                document.addEventListener("mousedown", I),
                () => {
                  document.removeEventListener("mousedown", I);
                }
              ),
              [I],
            ),
            (0, s.useEffect)(() => {
              D(a);
            }, [a]),
            i().createElement(
              "div",
              {
                ref: A,
                className: H,
                onMouseEnter: L,
                onMouseMove: x,
                onMouseUp: M,
                onMouseDown: P,
                onMouseLeave: O,
                onClick: T,
              },
              n !== o.L.ghost &&
                i().createElement(
                  i().Fragment,
                  null,
                  i().createElement("div", { className: l.Z.back }),
                  i().createElement("span", { className: l.Z.texture }),
                ),
              i().createElement(
                "span",
                { className: W },
                i().createElement("span", { className: l.Z.stateDisabled }),
                i().createElement("span", { className: l.Z.stateHighlightHover }),
                i().createElement("span", { className: l.Z.stateHighlightActive }),
              ),
              i().createElement(
                "span",
                { className: l.Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
              ),
            )
          );
        };
        c.defaultProps = {
          type: o.L.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const m = (0, s.memo)(c);
      },
      2106: (e, t, a) => {
        "use strict";
        let n, r;
        (a.d(t, { L: () => n, q: () => r }),
          (function (e) {
            ((e.main = "main"),
              (e.primary = "primary"),
              (e.primaryGreen = "primaryGreen"),
              (e.primaryRed = "primaryRed"),
              (e.secondary = "secondary"),
              (e.ghost = "ghost"));
          })(n || (n = {})),
          (function (e) {
            ((e.extraSmall = "extraSmall"), (e.small = "small"), (e.medium = "medium"));
          })(r || (r = {})));
      },
      9987: (e, t, a) => {
        "use strict";
        a.d(t, { A: () => c });
        var n = a(6483),
          r = a.n(n),
          u = a(6179),
          s = a.n(u),
          i = a(8055);
        const l = [
          "size",
          "value",
          "isEmpty",
          "fadeInAnimation",
          "hide",
          "maximumNumber",
          "className",
        ];
        function o() {
          return (
            (o =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            o.apply(this, arguments)
          );
        }
        const c = (e) => {
          let t = e.size,
            a = e.value,
            n = e.isEmpty,
            u = e.fadeInAnimation,
            c = e.hide,
            m = e.maximumNumber,
            d = e.className,
            _ = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, l);
          const E = n ? null : a,
            g = "string" == typeof E;
          if ((E && !g && E < 0) || 0 === E) return null;
          const b = E && !g && E > m,
            p = r()(
              i.Z.base,
              i.Z[`base__${t}`],
              u && i.Z.base__animated,
              c && i.Z.base__hidden,
              !E && i.Z.base__pattern,
              n && i.Z.base__empty,
              d,
            );
          return s().createElement(
            "div",
            o({ className: p }, _),
            s().createElement("div", { className: i.Z.bg }),
            s().createElement("div", { className: i.Z.pattern }),
            s().createElement(
              "div",
              { className: r()(i.Z.value, g && i.Z.value__text) },
              b ? m : E,
              b && s().createElement("span", { className: i.Z.plus }, "+"),
            ),
          );
        };
        c.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
      },
      280: (e, t, a) => {
        "use strict";
        a.d(t, { z: () => o });
        var n = a(6179),
          r = a.n(n),
          u = a(6483),
          s = a.n(u),
          i = a(3649),
          l = a(5287);
        const o = ({ binding: e, text: t = "", classMix: a, alignment: u = i.v2.left }) =>
          null === t
            ? (console.error("FormatText was supplied with 'null'"), null)
            : r().createElement(
                n.Fragment,
                null,
                t.split("\n").map((t, o) =>
                  r().createElement(
                    "div",
                    { className: s()(l.Z.base, a), key: `${t}-${o}` },
                    (0, i.Uw)(t, u, e).map((e, t) =>
                      r().createElement(n.Fragment, { key: `${t}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, t, a) => {
        "use strict";
        a.d(t, { Y: () => m });
        var n = a(3138),
          r = a(6179),
          u = a(1043),
          s = a(5262);
        const i = n.O.client.getSize("rem"),
          l = i.width,
          o = i.height,
          c = Object.assign({ width: l, height: o }, (0, s.T)(l, o, u.j)),
          m = (0, r.createContext)(c);
      },
      1039: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => c });
        var n = a(6179),
          r = a.n(n),
          u = a(6536),
          s = a(3495),
          i = a(1043),
          l = a(5262),
          o = a(3138);
        const c = (0, n.memo)(({ children: e }) => {
          const t = (0, n.useContext)(s.Y),
            a = (0, n.useState)(t),
            c = a[0],
            m = a[1],
            d = (0, n.useCallback)((e, t) => {
              const a = o.O.view.pxToRem(e),
                n = o.O.view.pxToRem(t);
              m(Object.assign({ width: a, height: n }, (0, l.T)(a, n, i.j)));
            }, []);
          ((0, u.Z)(() => {
            engine.on("clientResized", d);
          }),
            (0, n.useEffect)(() => () => engine.off("clientResized", d), [d]));
          const _ = (0, n.useMemo)(() => Object.assign({}, c), [c]);
          return r().createElement(s.Y.Provider, { value: _ }, e);
        });
      },
      6010: (e, t, a) => {
        "use strict";
        var n = a(6179),
          r = a(7382),
          u = a(3495);
        const s = ["children"];
        const i = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, s);
          const i = (0, n.useContext)(u.Y),
            l = i.extraLarge,
            o = i.large,
            c = i.medium,
            m = i.small,
            d = i.extraSmall,
            _ = i.extraLargeWidth,
            E = i.largeWidth,
            g = i.mediumWidth,
            b = i.smallWidth,
            p = i.extraSmallWidth,
            v = i.extraLargeHeight,
            h = i.largeHeight,
            A = i.mediumHeight,
            C = i.smallHeight,
            f = i.extraSmallHeight,
            D = { extraLarge: v, large: h, medium: A, small: C, extraSmall: f };
          if (a.extraLarge || a.large || a.medium || a.small || a.extraSmall) {
            if (a.extraLarge && l) return t;
            if (a.large && o) return t;
            if (a.medium && c) return t;
            if (a.small && m) return t;
            if (a.extraSmall && d) return t;
          } else {
            if (a.extraLargeWidth && _) return (0, r.H)(t, a, D);
            if (a.largeWidth && E) return (0, r.H)(t, a, D);
            if (a.mediumWidth && g) return (0, r.H)(t, a, D);
            if (a.smallWidth && b) return (0, r.H)(t, a, D);
            if (a.extraSmallWidth && p) return (0, r.H)(t, a, D);
            if (!(
              a.extraLargeWidth ||
              a.largeWidth ||
              a.mediumWidth ||
              a.smallWidth ||
              a.extraSmallWidth
            )) {
              if (a.extraLargeHeight && v) return t;
              if (a.largeHeight && h) return t;
              if (a.mediumHeight && A) return t;
              if (a.smallHeight && C) return t;
              if (a.extraSmallHeight && f) return t;
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
        (0, n.memo)(i);
      },
      7382: (e, t, a) => {
        "use strict";
        a.d(t, { H: () => n });
        const n = (e, t, a) =>
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
      },
      7739: (e, t, a) => {
        "use strict";
        a.d(t, { YN: () => r.Y, ZN: () => n.Z });
        a(6010);
        var n = a(1039),
          r = a(3495);
      },
      1043: (e, t, a) => {
        "use strict";
        a.d(t, { j: () => n });
        const n = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, t, a) => {
        "use strict";
        var n;
        function r(e, t, a) {
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
        (a.d(t, { T: () => r }),
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
          })(n || (n = {})));
      },
      1037: (e, t, a) => {
        "use strict";
        a.d(t, { IC: () => n });
        var n,
          r = a(6483),
          u = a.n(r),
          s = a(6373),
          i = a(1856),
          l = a(3138),
          o = a(2039),
          c = a(5099),
          m = a(7727),
          d = a(4179),
          _ = a(6179),
          E = a.n(_),
          g = a(4769);
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(n || (n = {}));
        const b = ["__left", "__right", "__top", "__bottom"];
        (0, _.forwardRef)(
          (
            { children: e, disableAutoSizeUpdate: t, onOutsideClick: a, customStyles: n = {} },
            r,
          ) => {
            const p = (0, _.useRef)(null),
              v = (0, _.useRef)(null),
              h = (0, _.useRef)(null),
              A = (0, _.useState)(window.decorator && window.decorator.directionType),
              C = A[0],
              f = A[1],
              D = (0, _.useCallback)(() => {
                (m.$.playClick(), l.O.view.sendEvent.close());
              }, []),
              F = (0, _.useCallback)(() => {
                m.$.playHighlight();
              }, []),
              B = u()(g.Z.arrow, g.Z[`arrow${b[C]}`]);
            (0, o.b)(
              () => (
                l.O.client.events.mouse.enableOutside(),
                l.O.client.events.mouse.down(([, e]) => {
                  "outside" === e && (a ? a() : l.O.view.sendEvent.close("popover"));
                })
              ),
            );
            const k = (0, _.useCallback)(
                (e) => {
                  let t = e.target;
                  do {
                    if (t === p.current || t === h.current) return;
                    t = t.parentNode;
                  } while (t);
                  const n = window.decorator;
                  if (void 0 !== window.decorator) {
                    const e = l.O.client.getMouseGlobalPosition(),
                      t = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                      a =
                        e.x < n.boundX ||
                        e.x > n.boundX + n.boundWidth ||
                        e.y > n.boundY + n.boundHeight ||
                        e.y < n.boundY;
                    if (t && !a) return;
                  }
                  a ? a() : l.O.view.sendEvent.close("popover");
                },
                [p, h, a],
              ),
              w = (0, _.useCallback)(
                () => (
                  l.O.view.freezeTextureBeforeResize(),
                  (0, i.v)(() => {
                    if (v.current) {
                      const e = v.current.scrollWidth,
                        t = v.current.scrollHeight;
                      (l.O.view.resize(e, t), f(window.decorator.directionType));
                    }
                  })
                ),
                [],
              );
            return (
              (0, _.useImperativeHandle)(r, () => ({ updateSize: w })),
              (0, o.b)(() => {
                l.O.view.setInputPaddingsRem(58);
              }),
              (0, _.useEffect)(() => {
                document.addEventListener("mousedown", k, { capture: !0 });
                const e = (0, c.B)((0, d.Eu)());
                return (
                  !t && e.promise.then(() => w()),
                  () => {
                    (e.cancel(), document.removeEventListener("mousedown", k));
                  }
                );
              }, [w, k, t]),
              E().createElement(
                "div",
                { className: g.Z.base, ref: v },
                E().createElement(
                  "div",
                  { className: g.Z.decorator },
                  E().createElement(
                    "div",
                    { className: g.Z.content, ref: p },
                    e,
                    window.decorator &&
                      window.decorator.isCloseBtnVisible &&
                      E().createElement(
                        s.i,
                        { body: R.strings.dialogs.common.error.cancel() },
                        E().createElement("div", {
                          className: g.Z.closeBtn,
                          onClick: D,
                          onMouseEnter: F,
                          ref: h,
                        }),
                      ),
                  ),
                  E().createElement("div", { className: B, style: n.arrow }),
                ),
              )
            );
          },
        );
      },
      3616: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => o });
        var n = a(1037),
          r = a(4179),
          u = a(6179),
          s = a.n(u);
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
        function l() {
          return (
            (l =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            l.apply(this, arguments)
          );
        }
        const o = (e) => {
          let t = e.contentId,
            a = e.decoratorId,
            o = e.direction,
            c = void 0 === o ? n.IC.Top : o,
            m = e.targetId,
            d = e.args,
            _ = e.onClick,
            E = e.children,
            g = e.isEnabled,
            b = void 0 === g || g,
            p = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, i);
          const v = (0, u.useRef)(null),
            h = (0, u.useCallback)(() => {
              if ((0, r.wU)()) return (0, r.SW)();
              v.current && (0, r.P3)(t, c, v.current, a, m, d);
            }, [t, c, d, a, m]);
          return s().createElement(
            "div",
            l(
              {
                ref: v,
                onClick:
                  ((A = E.props.onClick),
                  (e) => {
                    b && (h(), _ && _(e), A && A(e));
                  }),
              },
              p,
            ),
            E,
          );
          var A;
        };
      },
      2773: (e, t, a) => {
        "use strict";
        a.d(t, { $Q: () => h });
        var n = a(6483),
          r = a.n(n),
          u = a(7515),
          s = a(1856),
          i = a(3815),
          l = a(560),
          o = a(7727),
          c = a(6179),
          m = a.n(c),
          d = a(6358),
          _ = a(372);
        const E = "disable",
          g = { pending: !1, offset: 0 },
          b = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          p = () => {},
          v = (e, t) => Math.max(20, e.offsetWidth * t),
          h = (0, c.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = b, onDrag: n = p }) => {
              const h = (0, c.useRef)(null),
                A = (0, c.useRef)(null),
                C = (0, c.useRef)(null),
                f = (0, c.useRef)(null),
                D = (0, c.useRef)(null),
                F = e.stepTimeout || 100,
                B = (0, c.useState)(g),
                k = B[0],
                w = B[1],
                y = (0, c.useCallback)(
                  (e) => {
                    (w(e),
                      D.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: D.current }));
                  },
                  [n],
                ),
                S = () => {
                  const t = f.current,
                    a = D.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && a && r)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    i = Math.min(1, n / r),
                    l = (0, u.u)(0, 1, s / (r - n)),
                    o = (t.offsetWidth - v(t, i)) * l;
                  ((a.style.transform = `translateX(${0 | o}px)`),
                    ((e) => {
                      if (A.current && C.current && f.current && D.current) {
                        if (0 === e)
                          return (A.current.classList.add(E), void C.current.classList.remove(E));
                        if (
                          ((t = f.current),
                          (a = D.current),
                          e - (t.offsetWidth - a.offsetWidth) >= -0.5)
                        )
                          return (A.current.classList.remove(E), void C.current.classList.add(E));
                        var t, a;
                        (A.current.classList.remove(E), C.current.classList.remove(E));
                      }
                    })(o));
                },
                N = (0, i.z)(() => {
                  ((() => {
                    const t = D.current,
                      a = f.current,
                      n = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && n && a)) return;
                    const u = Math.min(1, n / r);
                    ((t.style.width = `${v(a, u)}px`),
                      (t.style.display = "flex"),
                      h.current &&
                        (1 === u
                          ? h.current.classList.add(_.Z.base__nonActive)
                          : h.current.classList.remove(_.Z.base__nonActive)));
                  })(),
                    S());
                });
              ((0, c.useEffect)(() => (0, s.v)(N)),
                (0, c.useEffect)(
                  () =>
                    (0, s.v)(() => {
                      const t = () => {
                        S();
                      };
                      let a = p;
                      const n = () => {
                        (a(), (a = (0, s.v)(N)));
                      };
                      return (
                        e.events.on("recalculateContent", N),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", n),
                        () => {
                          (a(),
                            e.events.off("recalculateContent", N),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, c.useEffect)(() => {
                  if (!k.pending) return;
                  const t = (t) => {
                      var a;
                      const r = e.contentRef.current;
                      if (!r) return;
                      const u = f.current,
                        s = D.current;
                      if (!r || !u || !s) return;
                      const i = t.screenX - k.offset - u.getBoundingClientRect().x,
                        l = (i / u.offsetWidth) * (null != (a = e.getContainerSize()) ? a : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(r, l),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: s, thumbOffset: i, contentOffset: l }));
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t), y(g));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, k.offset, k.pending, n, y]));
              const I = (0, l.B)((t) => e.applyStepTo(t), F, [e]),
                T = I[0],
                L = I[1];
              (0, c.useEffect)(
                () => (
                  document.addEventListener("mouseup", L, !0),
                  () => document.removeEventListener("mouseup", L, !0)
                ),
                [L],
              );
              const x = (e) => {
                e.target.classList.contains(E) || (0, o.G)("highlight");
              };
              return m().createElement(
                "div",
                { className: r()(_.Z.base, t.base), ref: h, onWheel: e.handleMouseWheel },
                m().createElement("div", {
                  className: r()(_.Z.leftButton, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(E) ||
                      0 !== e.button ||
                      ((0, o.G)("play"), T(d.Nm.Next));
                  },
                  onMouseUp: L,
                  ref: A,
                  onMouseEnter: x,
                }),
                m().createElement(
                  "div",
                  {
                    className: r()(_.Z.track, t.track),
                    onMouseDown: (t) => {
                      const n = D.current;
                      if (n && 0 === t.button)
                        if (((0, o.G)("play"), t.target === n))
                          y({ pending: !0, offset: t.screenX - n.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const n = D.current,
                              r = e.contentRef.current;
                            if (!n || !r) return;
                            const u = a(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + u * t);
                          })(t.screenX > n.getBoundingClientRect().x ? d.Nm.Prev : d.Nm.Next);
                        }
                    },
                    ref: f,
                    onMouseEnter: x,
                  },
                  m().createElement("div", { ref: D, className: r()(_.Z.thumb, t.thumb) }),
                  m().createElement("div", { className: r()(_.Z.rail, t.rail) }),
                ),
                m().createElement("div", {
                  className: r()(_.Z.rightButton, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(E) ||
                      0 !== e.button ||
                      ((0, o.G)("play"), T(d.Nm.Prev));
                  },
                  onMouseUp: L,
                  ref: C,
                  onMouseEnter: x,
                }),
              );
            },
          );
      },
      2840: (e, t, a) => {
        "use strict";
        a.d(t, { K: () => c });
        var n = a(6483),
          r = a.n(n),
          u = a(6179),
          s = a.n(u),
          i = a(2773),
          l = a(7950),
          o = a(4682);
        const c = ({
          children: e,
          api: t,
          className: a,
          barClassNames: n,
          areaClassName: c,
          classNames: m,
          scrollClassName: d,
          getStepByRailClick: _,
          onDrag: E,
        }) => {
          const g = (0, u.useMemo)(() => {
              const e = n || {};
              return Object.assign({}, e, { base: r()(o.Z.base, e.base) });
            }, [n]),
            b = (0, u.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
          return s().createElement(
            "div",
            { className: r()(o.Z.defaultScroll, a), onWheel: t.handleMouseWheel },
            s().createElement(
              "div",
              { className: r()(o.Z.defaultScrollArea, c) },
              s().createElement(l.Area, { className: d, api: b, classNames: m }, e),
            ),
            s().createElement(i.$Q, { getStepByRailClick: _, api: t, onDrag: E, classNames: g }),
          );
        };
      },
      7950: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            Area: () => _,
            Bar: () => l.$Q,
            DefaultScroll: () => o.K,
            Direction: () => d.Nm,
            defaultSettings: () => d.he,
            useHorizontalScrollApi: () => d.T5,
          }));
        var n = a(6483),
          r = a.n(n),
          u = a(1856),
          s = a(6179),
          i = a.n(s),
          l = a(2773),
          o = a(2840),
          c = a(4682),
          m = a(8579),
          d = a(6358);
        const _ = ({ api: e, className: t, classNames: a, children: n, style: l }) => (
          (0, s.useEffect)(() => (0, u.v)(e.recalculateContent)),
          i().createElement(
            "div",
            { className: r()(c.Z.base, t), style: l },
            i().createElement(
              "div",
              {
                className: r()(c.Z.wrapper, null == a ? void 0 : a.wrapper),
                onWheel: e.handleMouseWheel,
                ref: e.wrapperRef,
              },
              i().createElement(
                "div",
                { className: r()(c.Z.content, null == a ? void 0 : a.content), ref: e.contentRef },
                n,
              ),
            ),
          )
        );
        ((_.Bar = l.$Q), (_.Default = o.K), (_.SeniorityAwards = m.Tm));
      },
      8579: (e, t, a) => {
        "use strict";
        a.d(t, { Tm: () => o });
        var n = a(6483),
          r = a.n(n),
          u = a(1856),
          s = a(6179),
          i = a.n(s),
          l = (a(2773), a(2840), a(4682));
        a(6358);
        const o = ({ api: e, className: t, classNames: a, children: n }) => (
          (0, s.useEffect)(() => (0, u.v)(e.recalculateContent)),
          i().createElement(
            "div",
            { className: r()(l.Z.base, t) },
            i().createElement(
              "div",
              { className: r()(l.Z.wrapper, null == a ? void 0 : a.wrapper), ref: e.wrapperRef },
              i().createElement(
                "div",
                { className: r()(l.Z.content, null == a ? void 0 : a.content), ref: e.contentRef },
                n,
              ),
            ),
          )
        );
      },
      6358: (e, t, a) => {
        "use strict";
        a.d(t, { Nm: () => n.Nm, T5: () => r, he: () => n.he });
        var n = a(7308);
        const r = (0, n.EO)({
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
          getDirection: (e) => (e.deltaY > 1 ? n.Nm.Next : n.Nm.Prev),
          triggerMouseMoveOnUpdate: !0,
        });
      },
      6225: (e, t, a) => {
        "use strict";
        a.d(t, { $Q: () => A });
        var n = a(6483),
          r = a.n(n),
          u = a(7515),
          s = a(1856),
          i = a(3815),
          l = a(560),
          o = a(7727),
          c = a(6179),
          m = a.n(c),
          d = a(7701),
          _ = a(9168);
        const E = "disable",
          g = () => {},
          b = { pending: !1, offset: 0 },
          p = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          v = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          h = (e, t) => Math.max(20, e.offsetHeight * t),
          A = (0, c.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: a = p, onDrag: n = g }) => {
              const A = (0, c.useRef)(null),
                C = (0, c.useRef)(null),
                f = (0, c.useRef)(null),
                D = (0, c.useRef)(null),
                F = (0, c.useRef)(null),
                B = e.stepTimeout || 100,
                k = (0, c.useState)(b),
                w = k[0],
                y = k[1],
                S = (0, c.useCallback)(
                  (e) => {
                    (y(e),
                      F.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: F.current }));
                  },
                  [n],
                ),
                N = (0, i.z)(() => {
                  const t = F.current,
                    a = D.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && r && t && a)) return;
                  const u = Math.min(1, n / r);
                  return (
                    (t.style.height = `${h(a, u)}px`),
                    t.classList.add(_.Z.thumb),
                    A.current &&
                      (1 === u
                        ? A.current.classList.add(_.Z.base__nonActive)
                        : A.current.classList.remove(_.Z.base__nonActive)),
                    u
                  );
                }),
                I = (0, i.z)(() => {
                  const t = D.current,
                    a = F.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && t && a && r)) return;
                  const s = e.animationScroll.scrollPosition.get(),
                    i = Math.min(1, n / r),
                    l = (0, u.u)(0, 1, s / (r - n)),
                    o = (t.offsetHeight - h(t, i)) * l;
                  ((a.style.transform = `translateY(${0 | o}px)`),
                    ((e) => {
                      if (C.current && f.current && D.current && F.current) {
                        if (0 === e)
                          return (C.current.classList.add(E), void f.current.classList.remove(E));
                        if (
                          ((t = D.current),
                          (a = F.current),
                          e - (t.offsetHeight - a.offsetHeight) >= -0.5)
                        )
                          return (C.current.classList.remove(E), void f.current.classList.add(E));
                        var t, a;
                        (C.current.classList.remove(E), f.current.classList.remove(E));
                      }
                    })(o));
                }),
                T = (0, i.z)(() => {
                  v(e, () => {
                    (N(), I());
                  });
                });
              ((0, c.useEffect)(() => (0, s.v)(T)),
                (0, c.useEffect)(() => {
                  const t = () => {
                    v(e, () => {
                      I();
                    });
                  };
                  let a = g;
                  const n = () => {
                    (a(), (a = (0, s.v)(T)));
                  };
                  return (
                    e.events.on("recalculateContent", T),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", n),
                    () => {
                      (a(),
                        e.events.off("recalculateContent", T),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, c.useEffect)(() => {
                  if (!w.pending) return;
                  const t = (t) => {
                      v(e, (a) => {
                        const r = D.current,
                          u = F.current,
                          s = e.getContainerSize();
                        if (!r || !u || !s) return;
                        const i = t.screenY - w.offset - r.getBoundingClientRect().y,
                          l = (i / r.offsetHeight) * s;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(a, l),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: a.scrollTop },
                        }),
                          n({ type: "dragging", thumb: u, thumbOffset: i, contentOffset: l }));
                      });
                    },
                    a = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        S(b));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", a),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", a));
                    }
                  );
                }, [e, w.offset, w.pending, n, S]));
              const L = (0, l.B)((t) => e.applyStepTo(t), B, [e]),
                x = L[0],
                R = L[1];
              (0, c.useEffect)(
                () => (
                  document.addEventListener("mouseup", R, !0),
                  () => document.removeEventListener("mouseup", R, !0)
                ),
                [R],
              );
              const M = (e) => {
                e.target.classList.contains(E) || (0, o.G)("highlight");
              };
              return m().createElement(
                "div",
                { className: r()(_.Z.base, t.base), ref: A, onWheel: e.handleMouseWheel },
                m().createElement("div", {
                  className: r()(_.Z.topButton, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(E) ||
                      0 !== e.button ||
                      ((0, o.G)("play"), x(d.Nm.Next));
                  },
                  ref: C,
                  onMouseEnter: M,
                }),
                m().createElement(
                  "div",
                  {
                    className: r()(_.Z.track, t.track),
                    onMouseDown: (t) => {
                      const n = F.current;
                      if (n && 0 === t.button)
                        if (((0, o.G)("play"), t.target === n))
                          (e.handleIsThumbDragging(!0),
                            S({ pending: !0, offset: t.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            F.current &&
                              v(e, (n) => {
                                if (!n) return;
                                const r = a(e),
                                  u = e.clampPosition(n, n.scrollTop + r * t);
                                e.applyScroll(u);
                              });
                          })(t.screenY > n.getBoundingClientRect().y ? d.Nm.Prev : d.Nm.Next);
                        }
                    },
                    ref: D,
                    onMouseEnter: M,
                  },
                  m().createElement("div", { ref: F, className: t.thumb }),
                  m().createElement("div", { className: r()(_.Z.rail, t.rail) }),
                ),
                m().createElement("div", {
                  className: r()(_.Z.bottomButton, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(E) ||
                      0 !== e.button ||
                      ((0, o.G)("play"), x(d.Nm.Prev));
                  },
                  onMouseUp: R,
                  ref: f,
                  onMouseEnter: M,
                }),
              );
            },
          );
      },
      1158: (e, t, a) => {
        "use strict";
        a.d(t, { K: () => c });
        var n = a(6483),
          r = a.n(n),
          u = a(6179),
          s = a.n(u),
          i = a(6225),
          l = a(9605),
          o = a(5636);
        const c = ({
          children: e,
          api: t,
          className: a,
          barClassNames: n,
          areaClassName: c,
          scrollClassName: m,
          scrollClassNames: d,
          getStepByRailClick: _,
          onDrag: E,
        }) => {
          const g = (0, u.useMemo)(() => {
              const e = n || {};
              return Object.assign({}, e, { base: r()(o.Z.base, e.base) });
            }, [n]),
            b = (0, u.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
          return s().createElement(
            "div",
            { className: r()(o.Z.defaultScroll, a), onWheel: t.handleMouseWheel },
            s().createElement(
              "div",
              { className: r()(o.Z.area, c) },
              s().createElement(l.Area, { className: m, classNames: d, api: b }, e),
            ),
            s().createElement(i.$Q, { getStepByRailClick: _, api: t, onDrag: E, classNames: g }),
          );
        };
      },
      9605: (e, t, a) => {
        "use strict";
        (a.r(t),
          a.d(t, {
            Area: () => d,
            Bar: () => l.$Q,
            Default: () => o.K,
            useVerticalScrollApi: () => c.c4,
          }));
        var n = a(6483),
          r = a.n(n),
          u = a(1856),
          s = a(6179),
          i = a.n(s),
          l = a(6225),
          o = a(1158),
          c = a(7701),
          m = a(5636);
        const d = ({ className: e, classNames: t, children: a, api: n }) => (
          (0, s.useEffect)(() => (0, u.v)(n.recalculateContent)),
          i().createElement(
            "div",
            { className: r()(m.Z.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
            i().createElement(
              "div",
              { className: r()(m.Z.content, null == t ? void 0 : t.content), ref: n.contentRef },
              a,
            ),
          )
        );
        d.Default = o.K;
      },
      7701: (e, t, a) => {
        "use strict";
        a.d(t, { Nm: () => n.Nm, c4: () => r });
        var n = a(7308);
        const r = (0, n.EO)({
          getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
          getContainerSize: (e) => e.scrollHeight,
          getWrapperSize: (e) => e.offsetHeight,
          setScrollPosition: (e, t) => {
            e.scrollTop = t.value.scrollPosition;
          },
          getDirection: (e) => (e.deltaY > 1 ? n.Nm.Next : n.Nm.Prev),
        });
      },
      7308: (e, t, a) => {
        "use strict";
        a.d(t, { EO: () => E, Nm: () => d, he: () => _ });
        var n = a(7515),
          r = a(1856),
          u = a(3138),
          s = a(4532),
          i = a(9653),
          l = a(3815),
          o = a(4489),
          c = a(6179),
          m = a(7030);
        let d;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(d || (d = {}));
        const _ = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          E = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: a,
            getDirection: d,
            getWrapperSize: E,
            triggerMouseMoveOnUpdate: g = !1,
          }) => {
            const b = (e, a) => {
              const r = t(e),
                u = r[0],
                s = r[1];
              return (0, n.u)(u, s, a);
            };
            return (n = {}) => {
              const p = n.settings,
                v = void 0 === p ? _ : p,
                h = (0, c.useRef)(null),
                A = (0, c.useRef)(null),
                C = (0, i.q)(),
                f = (0, o.f)(
                  () => {
                    u.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                D = (0, m.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = h.current;
                    t && (a(t, e), C.trigger("change", e), g && f());
                  },
                  onRest: (e) => C.trigger("rest", e),
                  onStart: (e) => C.trigger("start", e),
                  onPause: (e) => C.trigger("pause", e),
                })),
                F = D[0],
                B = D[1],
                k = (0, c.useCallback)(
                  (e, t, a) => {
                    var n;
                    const r = F.scrollPosition.get(),
                      u = (null != (n = F.scrollPosition.goal) ? n : 0) - r;
                    return b(e, t * a + u + r);
                  },
                  [F.scrollPosition],
                ),
                w = (0, c.useCallback)(
                  (e, { immediate: t = !1, reset: a = !0 } = {}) => {
                    const n = h.current;
                    n &&
                      B.start({
                        scrollPosition: b(n, e),
                        immediate: t,
                        reset: a,
                        config: v.animationConfig,
                        from: { scrollPosition: b(n, F.scrollPosition.get()) },
                      });
                  },
                  [B, v.animationConfig, F.scrollPosition],
                ),
                y = (0, c.useCallback)(
                  (e) => {
                    const t = h.current,
                      a = A.current;
                    if (!t || !a) return;
                    const n = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return E(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(a, v.step),
                      r = k(t, e, n);
                    w(r);
                  },
                  [w, k, v.step],
                ),
                S = (0, c.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && y(d(e)),
                      h.current && C.trigger("mouseWheel", e, F.scrollPosition, t(h.current)));
                  },
                  [F.scrollPosition, y, C],
                ),
                N = (0, s.M)(
                  () =>
                    (0, r.v)(() => {
                      const e = h.current;
                      e &&
                        (w(b(e, F.scrollPosition.goal), { immediate: !0 }),
                        C.trigger("resizeHandled"));
                    }),
                  [w, F.scrollPosition.goal],
                ),
                I = (0, l.z)(() => {
                  const e = h.current;
                  if (!e) return;
                  const t = b(e, F.scrollPosition.goal);
                  (t !== F.scrollPosition.goal && w(t, { immediate: !0 }),
                    C.trigger("recalculateContent"));
                });
              (0, c.useEffect)(
                () => (
                  window.addEventListener("resize", N),
                  () => {
                    window.removeEventListener("resize", N);
                  }
                ),
                [N],
              );
              const T = (0, c.useCallback)((e) => C.trigger("isThumbDraggingChanged", e), [C]);
              return (0, c.useMemo)(
                () => ({
                  getWrapperSize: () => (A.current ? E(A.current) : void 0),
                  getContainerSize: () => (h.current ? e(h.current) : void 0),
                  getBounds: () =>
                    h.current
                      ? t(h.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: v.step.clampedArrowStepTimeout,
                  clampPosition: b,
                  handleMouseWheel: S,
                  applyScroll: w,
                  applyStepTo: y,
                  contentRef: h,
                  wrapperRef: A,
                  scrollPosition: B,
                  animationScroll: F,
                  recalculateContent: I,
                  handleIsThumbDragging: T,
                  events: { on: C.on, off: C.off },
                }),
                [F.scrollPosition, w, y, T, C.off, C.on, I, S, B, v.step.clampedArrowStepTimeout],
              );
            };
          };
      },
      794: (e, t, a) => {
        "use strict";
        a.d(t, { X: () => r });
        var n = a(7950);
        const r = { Vertical: a(9605), Horizontal: n };
      },
      7613: (e, t, a) => {
        "use strict";
        a.d(t, { ZP: () => F });
        var n = a(6483),
          r = a.n(n),
          u = a(3779),
          s = a(280),
          i = a(3532),
          l = a.n(i),
          o = a(9887),
          c = a.n(o),
          m = a(3377),
          d = a(6179),
          _ = a.n(d),
          E = a(3393);
        const g = [
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
        function b() {
          return (
            (b =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            b.apply(this, arguments)
          );
        }
        Object.keys(c());
        const p = Object.keys(l()),
          v = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          h = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          A = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          C = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          f =
            (Object.keys(C),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": v,
              "heading-H36": v,
              "heading-H28": h,
              "heading-H24": h,
              "heading-H24R": h,
              "heading-H22": h,
              "heading-H20R": h,
              "heading-H18": h,
              "heading-H15": A,
              "heading-H14": A,
              "paragraph-P24": h,
              "paragraph-P18": h,
              "paragraph-P16": h,
              "paragraph-P14": A,
              "paragraph-P12": A,
              "paragraph-P10": A,
            }),
          D =
            (Object.keys(f),
            (e) =>
              e
                ? ((e) => p.includes(e))(e)
                  ? { colorClassName: E.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          F = (0, m.ZP)((e) => {
            let t = e.text,
              a = e.variant,
              n = e.className,
              i = e.color,
              l = e.m,
              o = e.mt,
              c = void 0 === o ? l : o,
              m = e.mr,
              p = void 0 === m ? l : m,
              v = e.mb,
              h = void 0 === v ? l : v,
              A = e.ml,
              C = void 0 === A ? l : A,
              F = e.style,
              B = e.format,
              k = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, g);
            const w = (0, d.useMemo)(() => {
                const e = D(i),
                  t = e.colorClassName,
                  a = e.colorStyle,
                  n = void 0 === a ? {} : a;
                return { computedStyle: Object.assign({}, F, n), colorClassName: t };
              }, [F, i]),
              y = w.computedStyle,
              S = w.colorClassName;
            return _().createElement(
              u.ZP,
              b(
                {
                  className: r()(E.Z.base, a && E.Z[a], S, n),
                  style: y,
                  mt: !0 === c ? f[a || "paragraph-P16"].mt : c,
                  mr: !0 === p ? f[a || "paragraph-P16"].mr : p,
                  mb: !0 === h ? f[a || "paragraph-P16"].mb : h,
                  ml: !0 === C ? f[a || "paragraph-P16"].ml : C,
                },
                k,
              ),
              void 0 !== B ? _().createElement(s.z, b({}, B, { text: t })) : t,
            );
          });
      },
      7078: (e, t, a) => {
        "use strict";
        a.d(t, { t: () => l });
        var n = a(6179),
          r = a.n(n),
          u = a(2056);
        const s = ["children"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, s);
          return r().createElement(
            u.u,
            i(
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
      },
      3415: (e, t, a) => {
        "use strict";
        a.d(t, { l: () => o });
        var n = a(6179),
          r = a.n(n),
          u = a(7078),
          s = a(6373),
          i = a(2056);
        function l() {
          return (
            (l =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            l.apply(this, arguments)
          );
        }
        const o = ({ children: e, tooltipArgs: t, className: a }) => {
          if (!t) return e;
          const n = r().createElement("div", { className: a }, e);
          if (t.header || t.body) return r().createElement(s.i, t, n);
          const o = t.contentId,
            c = t.args,
            m = null == c ? void 0 : c.contentId;
          return o || m
            ? r().createElement(i.u, l({}, t, { contentId: o || m }), n)
            : r().createElement(u.t, t, n);
        };
      },
      6373: (e, t, a) => {
        "use strict";
        a.d(t, { i: () => o });
        var n = a(2056),
          r = a(6179),
          u = a.n(r);
        const s = ["children", "body", "header", "note", "alert", "args"];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = R.views.common.tooltip_window.simple_tooltip_content,
          o = (e) => {
            let t = e.children,
              a = e.body,
              o = e.header,
              c = e.note,
              m = e.alert,
              d = e.args,
              _ = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, s);
            const E = (0, r.useMemo)(() => {
              const e = Object.assign({}, d, { body: a, header: o, note: c, alert: m });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [m, a, o, c, d]);
            return u().createElement(
              n.u,
              i(
                {
                  contentId:
                    ((g = null == d ? void 0 : d.hasHtmlContent),
                    g ? l.SimpleTooltipHtmlContent("resId") : l.SimpleTooltipContent("resId")),
                  decoratorId: R.views.common.tooltip_window.tooltip_window.TooltipWindow("resId"),
                  args: E,
                },
                _,
              ),
              t,
            );
            var g;
          };
      },
      2056: (e, t, a) => {
        "use strict";
        a.d(t, { u: () => o });
        var n = a(7902),
          r = a(4179),
          u = a(6179);
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
        function i(e) {
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
        const l = (e, t, a = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: r.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                a,
              ),
            );
          },
          o = (e) => {
            let t = e.children,
              a = e.contentId,
              r = e.args,
              o = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onClick,
              _ = e.ignoreShowDelay,
              E = void 0 !== _ && _,
              g = e.ignoreMouseClick,
              b = void 0 !== g && g,
              p = e.decoratorId,
              v = void 0 === p ? 0 : p,
              h = e.isEnabled,
              A = void 0 === h || h,
              C = e.targetId,
              f = void 0 === C ? 0 : C,
              D = e.onShow,
              F = e.onHide,
              B = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, s);
            const k = (0, u.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              w = (0, u.useMemo)(() => f || (0, n.F)().resId, [f]),
              y = (0, u.useCallback)(() => {
                (k.current.isVisible && k.current.timeoutId) ||
                  (l(a, v, { isMouseEvent: !0, on: !0, arguments: i(r) }, w),
                  D && D(),
                  (k.current.isVisible = !0));
              }, [a, v, r, w, D]),
              S = (0, u.useCallback)(() => {
                if (k.current.isVisible || k.current.timeoutId) {
                  const e = k.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (k.current.timeoutId = 0)),
                    l(a, v, { on: !1 }, w),
                    k.current.isVisible && F && F(),
                    (k.current.isVisible = !1));
                }
              }, [a, v, w, F]),
              N = (0, u.useCallback)((e) => {
                k.current.isVisible &&
                  ((k.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (k.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(k.current.prevTarget) && S();
                  }, 200)));
              }, []);
            ((0, u.useEffect)(() => {
              const e = k.current.hideTimerId;
              return (
                document.addEventListener("wheel", N, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", N, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, u.useEffect)(() => {
                !1 === A && S();
              }, [A, S]),
              (0, u.useEffect)(
                () => (
                  window.addEventListener("mouseleave", S),
                  () => {
                    (window.removeEventListener("mouseleave", S), S());
                  }
                ),
                [S],
              ));
            return A
              ? (0, u.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((I = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((k.current.timeoutId = window.setTimeout(y, E ? 100 : 400)),
                            o && o(e),
                            I && I(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (S(), null == c || c(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === b && S(), null == d || d(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === b && S(), null == m || m(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    B,
                  ),
                )
              : t;
            var I;
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
      7515: (e, t, a) => {
        "use strict";
        a.d(t, { u: () => n });
        const n = (e, t, a) => (a < e ? e : a > t ? t : a);
      },
      1856: (e, t, a) => {
        "use strict";
        a.d(t, { v: () => n });
        const n = (e) => {
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
      },
      8246: (e, t, a) => {
        "use strict";
        a.d(t, { U: () => i });
        var n = a(3138);
        function r(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return u(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return u(e, t);
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
        function u(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, n = new Array(t); a < t; a++) n[a] = e[a];
          return n;
        }
        const s = (e) => (0 === e ? window : window.subViews.get(e));
        function i({
          initializer: e = !0,
          rootId: t = 0,
          getRoot: a = s,
          context: u = "model",
        } = {}) {
          const i = new Map();
          function l(e, t = 0) {
            viewEnv.removeDataChangedCallback(e, t)
              ? i.delete(e)
              : console.error("Can't remove callback by id:", e);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (e, t, a) => {
              a.forEach((t) => {
                const a = i.get(t);
                void 0 !== a && a(e);
              });
            });
          });
          const o = (e) => {
            const n = a(t),
              r = u.split(".").reduce((e, t) => e[t], n);
            return "string" != typeof e || 0 === e.length
              ? r
              : e.split(".").reduce((e, t) => {
                  const a = e[t];
                  return "function" == typeof a ? a.bind(e) : a;
                }, r);
          };
          return {
            subscribe: (a, r) => {
              const s = "string" == typeof r ? `${u}.${r}` : u,
                l = n.O.view.addModelObserver(s, t, !0);
              return (i.set(l, a), e && a(o(r)), l);
            },
            readByPath: o,
            createCallback: (e, t) => {
              const a = o(t);
              return (...t) => {
                a(e(...t));
              };
            },
            createCallbackNoArgs: (e) => {
              const t = o(e);
              return () => {
                t();
              };
            },
            dispose: function () {
              for (var e, a = r(i.keys()); !(e = a()).done;) {
                l(e.value, t);
              }
            },
            unsubscribe: l,
          };
        }
      },
      3215: (e, t, a) => {
        "use strict";
        a.d(t, { q: () => l });
        var n = a(4598),
          r = a(9174),
          u = a(6179),
          s = a.n(u),
          i = a(8246);
        const l = () => (e, t) => {
          const a = (0, u.createContext)({});
          return [
            function ({ mode: l = "real", options: o, children: c, mocks: m }) {
              const d = (0, u.useRef)([]),
                _ = (a, u, s) => {
                  var l;
                  const o = i.U(u),
                    c =
                      "real" === a
                        ? o
                        : Object.assign({}, o, {
                            readByPath: null != (l = null == s ? void 0 : s.getter) ? l : () => {},
                          }),
                    m = (e) =>
                      "mocks" === a ? (null == s ? void 0 : s.getter(e)) : c.readByPath(e),
                    _ = (e) => d.current.push(e),
                    E = e({
                      mode: a,
                      readByPath: m,
                      externalModel: c,
                      observableModel: {
                        array: (e, t) => {
                          const u = null != t ? t : m(e),
                            s = r.LO.box(u, { equals: n.jv });
                          return (
                            "real" === a &&
                              c.subscribe(
                                (0, r.aD)((e) => s.set(e)),
                                e,
                              ),
                            s
                          );
                        },
                        object: (e, t) => {
                          const u = null != t ? t : m(e),
                            s = r.LO.box(u, { equals: n.jv });
                          return (
                            "real" === a &&
                              c.subscribe(
                                (0, r.aD)((e) => s.set(e)),
                                e,
                              ),
                            s
                          );
                        },
                        primitives: (e, t) => {
                          const n = m(t);
                          if (Array.isArray(e)) {
                            const u = e.reduce((e, t) => ((e[t] = r.LO.box(n[t], {})), e), {});
                            return (
                              "real" === a &&
                                c.subscribe(
                                  (0, r.aD)((t) => {
                                    e.forEach((e) => {
                                      u[e].set(t[e]);
                                    });
                                  }),
                                  t,
                                ),
                              u
                            );
                          }
                          {
                            const u = e,
                              s = Object.entries(u),
                              i = s.reduce((e, [t, a]) => ((e[a] = r.LO.box(n[t], {})), e), {});
                            return (
                              "real" === a &&
                                c.subscribe(
                                  (0, r.aD)((e) => {
                                    s.forEach(([t, a]) => {
                                      i[a].set(e[t]);
                                    });
                                  }),
                                  t,
                                ),
                              i
                            );
                          }
                        },
                      },
                      cleanup: _,
                    }),
                    g = { mode: a, model: E, externalModel: c, cleanup: _ };
                  return {
                    model: E,
                    controls: "mocks" === a && s ? s.controls(g) : t(g),
                    externalModel: c,
                    mode: a,
                  };
                },
                E = (0, u.useRef)(!1),
                g = (0, u.useState)(l),
                b = g[0],
                p = g[1],
                v = (0, u.useState)(() => _(l, o, m)),
                h = v[0],
                A = v[1];
              return (
                (0, u.useEffect)(() => {
                  E.current ? A(_(b, o, m)) : (E.current = !0);
                }, [m, b, o]),
                (0, u.useEffect)(() => {
                  p(l);
                }, [l]),
                (0, u.useEffect)(
                  () => () => {
                    (h.externalModel.dispose(), d.current.forEach((e) => e()));
                  },
                  [h],
                ),
                s().createElement(a.Provider, { value: h }, c)
              );
            },
            () => (0, u.useContext)(a),
          ];
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
                  function l(e) {
                    a([e, "inside"]);
                  }
                  return (
                    window.addEventListener(u, l),
                    n(),
                    () => {
                      r &&
                        (i(), window.removeEventListener(u, l), (e.listeners -= 1), n(), (r = !1));
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
            displayStatusIs: () => k,
            events: () => u.U,
            extraSize: () => w,
            forceTriggerMouseMove: () => F,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => o,
            getDisplayStatus: () => B,
            getScale: () => b,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => C,
            isEventHandled: () => D,
            isFocused: () => A,
            pxToRem: () => p,
            remToPx: () => v,
            resize: () => _,
            sendEvent: () => s.qP,
            setAnimateWindow: () => h,
            setEventHandled: () => f,
            setInputPaddingsRem: () => l,
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
        function l(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function o(e, t, a, n = 1) {
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
          return "rem" === e ? t : { x: v(t.x), y: v(t.y) };
        }
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function b() {
          return viewEnv.getScale();
        }
        function p(e) {
          return viewEnv.pxToRem(e);
        }
        function v(e) {
          return viewEnv.remToPx(e);
        }
        function h(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function A() {
          return viewEnv.isFocused();
        }
        function C() {
          return viewEnv.isClientAccessible();
        }
        function f() {
          return viewEnv.setEventHandled();
        }
        function D() {
          return viewEnv.isEventHandled();
        }
        function F() {
          viewEnv.forceTriggerMouseMove();
        }
        function B() {
          return viewEnv.getShowingStatus();
        }
        const k = Object.keys(r.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === r.W[t]), e),
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
              window.isDomBuilt ? e() : u.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, a) => {
        "use strict";
        a.d(t, { qP: () => o });
        const n = ["args"];
        const r = 2,
          u = 16,
          s = 32,
          i = 64,
          l = (e, t) => {
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
          o = {
            close(e) {
              l("popover" === e ? r : s);
            },
            minimize() {
              l(i);
            },
            move(e) {
              l(u, { isMouseEvent: !0, on: e });
            },
          };
      },
      4598: (e, t, a) => {
        "use strict";
        function n() {}
        a.d(t, { ZT: () => n, jv: () => u, yR: () => r });
        function r(e) {
          return e;
        }
        function u() {
          return !1;
        }
        console.log;
      },
      7902: (e, t, a) => {
        "use strict";
        a.d(t, { F: () => n });
        const n = (e = 1) => {
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
        };
      },
      3377: (e, t, a) => {
        "use strict";
        a.d(t, { ZP: () => c });
        var n = a(5415),
          r = a(6179),
          u = a.n(r);
        const s = ["xl", "lg", "md", "sm", "xs"],
          i = (e) => e.includes("_") && ((e) => s.includes(e))(e.split("_").at(-1)),
          l = [n.cJ.ExtraLarge, n.cJ.Large, n.cJ.Medium, n.cJ.Small, n.cJ.ExtraSmall],
          o = (e, t) =>
            Object.keys(e).reduce((a, n) => {
              if (n in a) return a;
              if (i(n)) {
                const r = n.split("_").slice(0, -1).join("_");
                if (r in a) return a;
                const u = l.indexOf(t),
                  i = (-1 !== u ? s.slice(u) : [])
                    .map((e) => r + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  o = i ? e[i] : void 0;
                return ((a[r] = void 0 !== o ? o : e[r]), a);
              }
              const r = e[n];
              return (
                void 0 === r ||
                  ((e, t) => s.some((a) => void 0 !== t[`${e}_${a}`]))(n, e) ||
                  (a[n] = r),
                a
              );
            }, {}),
          c = (e, t = o) => {
            const a = (
              (e, t = o) =>
              (a) => {
                const s = (0, n.GS)().mediaSize,
                  i = (0, r.useMemo)(() => t(a, s), [a, s]);
                return u().createElement(e, i);
              }
            )(e, t);
            return u().memo((t) =>
              Object.keys(t).some((e) => i(e) && void 0 !== t[e])
                ? u().createElement(a, t)
                : u().createElement(e, t),
            );
          };
      },
      6536: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => r });
        var n = a(6179);
        const r = (e) => {
          const t = (0, n.useRef)(!1);
          t.current || (e(), (t.current = !0));
        };
      },
      4532: (e, t, a) => {
        "use strict";
        a.d(t, { M: () => r });
        var n = a(6179);
        const r = (e, t = []) => {
          const a = (0, n.useRef)(),
            r = (0, n.useCallback)((...t) => {
              (a.current && a.current(), (a.current = e(...t)));
            }, t);
          return (
            (0, n.useEffect)(
              () => () => {
                a.current && a.current();
              },
              [r],
            ),
            r
          );
        };
      },
      9653: (e, t, a) => {
        "use strict";
        a.d(t, { q: () => s });
        var n = a(6179);
        function r(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return u(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return u(e, t);
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
        function u(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, n = new Array(t); a < t; a++) n[a] = e[a];
          return n;
        }
        const s = () => {
          const e = (0, n.useMemo)(() => ({}), []),
            t = (t) => (e[t] || (e[t] = new Map()), e[t]),
            a = (e, a) => {
              t(e).set(a, a);
            },
            u = (e, a) => {
              t(e).delete(a);
            },
            s = (e, ...a) => {
              for (var n, u = r(t(e).values()); !(n = u()).done;) {
                (0, n.value)(...a);
              }
            };
          return (0, n.useMemo)(() => ({ on: a, off: u, trigger: s }), []);
        };
      },
      3815: (e, t, a) => {
        "use strict";
        a.d(t, { z: () => u });
        var n = a(6179);
        const r = [];
        function u(e) {
          const t = (0, n.useRef)(e);
          return (
            (0, n.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, n.useCallback)((...e) => (0, t.current)(...e), r)
          );
        }
      },
      5415: (e, t, a) => {
        "use strict";
        a.d(t, { Aq: () => l, GS: () => o, cJ: () => s, fd: () => i });
        var n = a(6179),
          r = a(7739),
          u = a(1043);
        let s, i, l;
        (!(function (e) {
          ((e[(e.ExtraSmall = u.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = u.j.small.width)] = "Small"),
            (e[(e.Medium = u.j.medium.width)] = "Medium"),
            (e[(e.Large = u.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = u.j.extraLarge.width)] = "ExtraLarge"));
        })(s || (s = {})),
          (function (e) {
            ((e[(e.ExtraSmall = u.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = u.j.small.width)] = "Small"),
              (e[(e.Medium = u.j.medium.width)] = "Medium"),
              (e[(e.Large = u.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = u.j.extraLarge.width)] = "ExtraLarge"));
          })(i || (i = {})),
          (function (e) {
            ((e[(e.ExtraSmall = u.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = u.j.small.height)] = "Small"),
              (e[(e.Medium = u.j.medium.height)] = "Medium"),
              (e[(e.Large = u.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = u.j.extraLarge.height)] = "ExtraLarge"));
          })(l || (l = {})));
        const o = () => {
          const e = (0, n.useContext)(r.YN),
            t = e.width,
            a = e.height,
            u = ((e) => {
              switch (!0) {
                case e.extraLarge:
                  return s.ExtraLarge;
                case e.large:
                  return s.Large;
                case e.medium:
                  return s.Medium;
                case e.small:
                  return s.Small;
                case e.extraSmall:
                  return s.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), s.ExtraSmall);
              }
            })(e),
            o = ((e) => {
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
            c = ((e) => {
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
            mediaSize: u,
            mediaWidth: o,
            mediaHeight: c,
            remScreenWidth: t,
            remScreenHeight: a,
          };
        };
      },
      2039: (e, t, a) => {
        "use strict";
        a.d(t, { b: () => r });
        var n = a(6179);
        const r = (e) => {
          (0, n.useEffect)(e, []);
        };
      },
      560: (e, t, a) => {
        "use strict";
        a.d(t, { B: () => r });
        var n = a(6179);
        function r(e, t, a = []) {
          const r = (0, n.useRef)(0),
            u = (0, n.useCallback)(() => window.clearInterval(r.current), a || []);
          (0, n.useEffect)(() => u, [u]);
          const s = (null != a ? a : []).concat([t]);
          return [
            (0, n.useCallback)((a) => {
              ((r.current = window.setInterval(() => e(a, !0), t)), e(a, !1));
            }, s),
            u,
          ];
        }
      },
      4419: (e, t, a) => {
        "use strict";
        a.d(t, { y: () => u });
        var n = a(8045),
          r = a(6179);
        const u = (e, t, a = !0) => {
          const u = (0, r.useCallback)(
            (e) => {
              const a = e[0];
              t && t(a);
            },
            [t],
          );
          (0, r.useEffect)(() => {
            if (!e.current || !a) return;
            const t = new n.Z((e) => u(e));
            return (
              t.observe(e.current),
              () => {
                t.disconnect();
              }
            );
          }, [u, a, e]);
        };
      },
      3112: (e, t, a) => {
        "use strict";
        a.d(t, { V: () => u });
        var n = a(6179),
          r = a(3138);
        const u = () => {
          const e = (0, n.useState)(r.O.view.getScale()),
            t = e[0],
            a = e[1];
          return (
            (0, n.useEffect)(() => {
              const e = () => {
                a(r.O.view.getScale());
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
        };
      },
      4489: (e, t, a) => {
        "use strict";
        a.d(t, { f: () => u });
        var n = a(5139),
          r = a(6179);
        function u(e, t, a) {
          const u = (0, r.useMemo)(() => (0, n.Z)(a, e), t);
          return ((0, r.useEffect)(() => u.cancel, [u]), u);
        }
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
      5175: (e, t, a) => {
        "use strict";
        a.d(t, { c: () => u });
        var n = a(9480);
        const r = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? n.UI(e, (e) => ("object" == typeof e ? r(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? r(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? r(t) : t]),
                    )
              : e,
          u = (e) => r(e);
      },
      9480: (e, t, a) => {
        "use strict";
        function n(e, t) {
          var a;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (a = e[t]) ? void 0 : a.value;
        }
        a.d(t, { U2: () => n, UI: () => s, sE: () => l, tP: () => i, v_: () => o });
        const r = n;
        function u(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function s(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, a, n) => t(null == e ? void 0 : e.value, a, n));
        }
        function i(e, t = 0, a = e.length - 1) {
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
                  return t ? { value: u(t), done: !1 } : { done: !0, value: null };
                },
              };
            },
          };
        }
        function l(e, t) {
          for (let a = 0; a < e.length; a++) {
            const n = u(e[a]);
            if (t(n, a, e)) return n;
          }
        }
        function o(e, t = ",") {
          let a = "";
          for (let n = 0; n < e.length; n++) {
            n > 0 && (a += t);
            const u = r(e, n);
            a += null == u ? "" : String(u);
          }
          return a;
        }
      },
      5099: (e, t, a) => {
        "use strict";
        a.d(t, { B: () => n });
        const n = (e) => {
          let t = !1;
          return {
            promise: new Promise((a, n) => {
              e.then((e) => !t && a(e)).catch((e) => !t && n(e));
            }),
            cancel() {
              t = !0;
            },
          };
        };
      },
      4385: (e, t, a) => {
        "use strict";
        a.d(t, { K: () => n });
        const n = (e, t) => {
          const a = [];
          for (let n = 0; n < e; n++) a.push(t(n));
          return a;
        };
      },
      1612: (e, t, a) => {
        "use strict";
        a.d(t, { h: () => r });
        var n = a(9174);
        function r(e) {
          const t = {};
          for (const a in e)
            if (Object.prototype.hasOwnProperty.call(e, a)) {
              const r = e[a];
              t[a] = (0, n.aD)(r);
            }
          return t;
        }
      },
      9690: (e, t, a) => {
        "use strict";
        a.d(t, { HG: () => s });
        const n = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          r = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const u = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          s = (e) =>
            u
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let a = r.length - 1; a >= 0; a--)
                    for (; e >= r[a];) ((t += n[a]), (e -= r[a]));
                  return t;
                })(e);
      },
      7727: (e, t, a) => {
        "use strict";
        function n(e) {
          engine.call("PlaySound", e);
        }
        a.d(t, { $: () => r, G: () => n });
        const r = {
          playHighlight() {
            n("highlight");
          },
          playClick() {
            n("play");
          },
          playYes() {
            n("yes1");
          },
        };
      },
      3649: (e, t, a) => {
        "use strict";
        let n;
        function r(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const a = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(a, -a)]);
          });
        }
        function u(e) {
          return e.replace(/-/g, "_");
        }
        function s(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        (a.d(t, {
          BN: () => u,
          Eg: () => l,
          Uw: () => g,
          e: () => s,
          uF: () => r,
          v2: () => n,
          z4: () => i,
        }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(n || (n = {})));
        const i = (e) => e.replace(/&nbsp;/g, " "),
          l = (e) => e.replace(/&zwnbsp;/g, "\ufeff"),
          o = (e, t, a) => {
            if (a % 2) {
              const a = e.pop();
              return [...e, a + t];
            }
            return [...e, t];
          },
          c = (e, t, a) => {
            if (0 === a) return [t];
            if (a % 2) return [...e, " " === t ? " " : t];
            {
              const a = e.pop();
              return [...e, a + t];
            }
          },
          m = (e, t, a = n.left) => e.split(t).reduce(a === n.left ? o : c, []),
          d = (() => {
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
          E = (e, t = n.left) => {
            const a = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return _.includes(a)
              ? d(e)
              : ((e, t = n.left) => {
                  let a = [];
                  const r =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    u = i(e);
                  return (m(u, /( )/, t).forEach((e) => (a = a.concat(m(e, r, n.left)))), a);
                })(e, t);
          },
          g = (e, t, a) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (a && e in a ? a[e] : E(e, t)));
      },
      5139: (e, t, a) => {
        "use strict";
        function n(e, t, a, n) {
          let r,
            u = !1,
            s = 0;
          function i() {
            r && clearTimeout(r);
          }
          function l(...l) {
            const o = this,
              c = Date.now() - s;
            function m() {
              ((s = Date.now()), a.apply(o, l));
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
            (l.cancel = function () {
              (i(), (u = !0));
            }),
            l
          );
        }
        a.d(t, { Z: () => n });
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
          B0: () => l,
          c9: () => A,
          wU: () => F,
          ry: () => v,
          Eu: () => h,
          SW: () => f,
          P3: () => D,
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
        const o = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          c = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = a(5521),
          E = a(3138);
        const g = ["args"];
        function b(e, t, a, n, r, u, s) {
          try {
            var i = e[u](s),
              l = i.value;
          } catch (e) {
            return void a(e);
          }
          i.done ? t(l) : Promise.resolve(l).then(n, r);
        }
        const p = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          v = (function () {
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
                      b(u, n, r, s, i, "next", e);
                    }
                    function i(e) {
                      b(u, n, r, s, i, "throw", e);
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
          A = (e, t) => {
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
          C = () => A(l.CLOSE),
          f = () => A(l.POP_OVER, { on: !1 }),
          D = (e, t, a, n, r = R.invalid("resId"), u) => {
            const s = E.O.view.getViewGlobalPosition(),
              i = a.getBoundingClientRect(),
              o = i.x,
              c = i.y,
              m = i.width,
              d = i.height,
              _ = {
                x: E.O.view.pxToRem(o) + s.x,
                y: E.O.view.pxToRem(c) + s.y,
                width: E.O.view.pxToRem(m),
                height: E.O.view.pxToRem(d),
              };
            A(l.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: n || R.invalid("resId"),
              targetID: r,
              direction: t,
              bbox: p(_),
              on: !0,
              args: u,
            });
          },
          F = () => viewEnv.isWindowShownByViewEvent(l.POP_OVER),
          B = (e, t) => {
            e.keyCode === _.n.ESCAPE && t();
          };
        var k = a(7572);
        const w = r.instance,
          y = {
            DataTracker: u.Z,
            ViewModel: k.Z,
            ViewEventType: l,
            NumberFormatType: o,
            RealFormatType: c,
            TimeFormatType: m,
            DateFormatType: d,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => A(l.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: C,
            sendClosePopOverEvent: f,
            sendShowContextMenuEvent: (e, t, a = 0) => {
              A(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: a,
                args: t,
              });
            },
            sendShowPopOverEvent: D,
            addEscapeListener: (e) => {
              const t = (t) => B(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              B(e, C);
            },
            handleViewEvent: A,
            onBindingsReady: v,
            onLayoutReady: h,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(l.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(l.CONTEXT_MENU),
            isPopOverShown: F,
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
            ClickOutsideManager: w,
            SystemLocale: s,
            UserLocale: i,
          };
        window.ViewEnvHelper = y;
      },
      3618: (e, t, a) => {
        "use strict";
        a.d(t, { w: () => _ });
        var n = a(6483),
          r = a.n(n),
          u = a(3415),
          s = a(4419),
          i = a(6179),
          l = a.n(i),
          o = a(6143),
          c = a(3310),
          m = a(131),
          d = a(9053);
        const _ = l().memo(
          ({
            text: e,
            classMix: t,
            onSizeChanged: a,
            binding: n,
            isTooltipEnable: _ = !1,
            isTruncationAvailable: E = !1,
            targetId: g,
            justifyContent: b = d.v2.FlexStart,
            alignContent: p = d.v2.FlexStart,
            truncateIdentify: v = d.YA,
          }) => {
            const h = (0, i.useRef)(null),
              A = (0, i.useRef)({ height: 0, width: 0 }),
              C = (0, i.useState)({ elementList: [], isTruncated: !1, isTruncateFinished: !1 }),
              f = C[0],
              D = C[1],
              F = (0, i.useMemo)(() => (0, c.s)(e, n), [n, e]),
              B = (0, i.useMemo)(() => {
                if (_ && f.isTruncated)
                  return {
                    args: { text: e, stringifyKwargs: n ? JSON.stringify(n) : "" },
                    contentId: R.views.lobby.common.tooltips.ExtendedTextTooltip("resId"),
                    targetId: g,
                  };
              }, [n, _, g, e, f.isTruncated]),
              k = (0, i.useCallback)(
                (e) => {
                  ((A.current.width = e.contentRect.width),
                    (A.current.height = e.contentRect.height));
                  const t = (0, m.T)(h, F, A.current, v),
                    n = t[0],
                    r = t[1];
                  (D({ elementList: n, isTruncated: r, isTruncateFinished: !0 }), a && a(r));
                },
                [a, v, F],
              ),
              w = (0, i.useMemo)(() => ({ justifyContent: b, alignContent: p }), [p, b]);
            return (
              (0, s.y)(h, k, E),
              l().createElement(
                "div",
                {
                  className: r()(
                    o.Z.base,
                    t,
                    o.Z.base__zeroPadding,
                    E && o.Z.base__isTruncationAvailable,
                  ),
                  style: w,
                },
                l().createElement("div", { className: o.Z.unTruncated, ref: h }, F),
                l().createElement(
                  u.l,
                  { tooltipArgs: B },
                  l().createElement(
                    "div",
                    {
                      className: r()(
                        o.Z.truncated,
                        !f.isTruncateFinished && E && o.Z.truncated__hide,
                      ),
                      style: w,
                    },
                    f.isTruncateFinished && E ? f.elementList : F,
                  ),
                ),
              )
            );
          },
        );
      },
      3310: (e, t, a) => {
        "use strict";
        a.d(t, { s: () => m });
        var n = a(3649),
          r = a(6799),
          u = a(6960),
          s = a(9053);
        const i = (e) => {
            const t = /[\s\u002d]/g;
            let a = t.exec(e);
            if (!a) return [e];
            const n = [];
            let r = 0;
            for (; a;) (n.push(e.slice(r, t.lastIndex)), (r = t.lastIndex), (a = t.exec(e)));
            return (r !== e.length && n.push(e.slice(r)), n);
          },
          l = (e, t = "") => {
            const a = [];
            return (
              (0, u.Z)(
                e,
                /(\n+|[\xa0\ufeff]+)/g,
                (e) => {
                  a.push({ blockType: s.kH.Word, colorTag: t, childList: i(e) });
                },
                (e) => {
                  const n = e[0],
                    r = s.aF[n.charAt(0)];
                  r === s.kH.LineBreak
                    ? a.push(
                        ...((e) => {
                          const t = [
                            { blockType: s.kH.LineBreak, colorTag: "", childList: [e.charAt(0)] },
                          ];
                          for (let a = 0; a < e.length - 1; a++)
                            t.push({
                              blockType: s.kH.NewLine,
                              colorTag: "",
                              childList: [e.charAt(0)],
                            });
                          return t;
                        })(n),
                      )
                    : a.push({ blockType: r, colorTag: t, childList: [n] });
                },
              ),
              a
            );
          },
          o = (e, t, a = "") => {
            const n = [];
            return (
              (0, u.Z)(
                e,
                /(?:%\(|{)(.*?)[)}][sd]?/g,
                (e) => {
                  n.push(...l(e, a));
                },
                (e) => {
                  const r = e[1],
                    u = void 0 === t[r] ? e[0] : t[r];
                  "string" == typeof u || "number" == typeof u
                    ? n.push(...l(String(u), a))
                    : n.push({ blockType: s.kH.Binding, colorTag: a, childList: [u] });
                },
              ),
              n
            );
          },
          c = (e, t) => {
            if (!e) return [t];
            const a = [],
              n = Object.assign({}, t, { childList: t.childList.splice(0, 1) });
            if (e.blockType === s.kH.NoBreakWrapper) (e.childList.push(n), a.push(e));
            else {
              const t = Object.assign({}, e, { childList: e.childList.splice(-1) });
              (e.childList.length > 0 && a.push(e),
                a.push({ blockType: s.kH.NoBreakWrapper, colorTag: "", childList: [t, n] }));
            }
            return (t.childList.length > 0 && a.push(t), a);
          },
          m = (e, t = {}) => {
            if (!e) return [];
            const a = ((e) => {
              const t = [];
              let a = !1;
              return (
                e.forEach((e) => {
                  e.blockType === s.kH.NoBreakSymbol
                    ? ((a = !0), t.push(...c(t.pop(), e)))
                    : (a ? t.push(...c(t.pop(), e)) : t.push(e), (a = !1));
                }),
                t
              );
            })(
              ((e, t) => {
                const a = [];
                return (
                  (0, u.Z)(
                    e,
                    /(?:%\(|{)(\w*)(?:_[Oo]pen|_Start)(?:\)s|})([\s\S]*?)(?:%\(|{)\w*(?:_[Cc]lose|_End)(?:\)s|})/g,
                    (e) => {
                      a.push(...o(e, t));
                    },
                    (e) => {
                      a.push(...o(e[2], t, e[1]));
                    },
                  ),
                  a
                );
              })((0, n.Eg)((0, n.z4)(e)), t),
            );
            return (0, r.w)(a);
          };
      },
      6799: (e, t, a) => {
        "use strict";
        a.d(t, { w: () => s });
        var n = a(597),
          r = a(9053);
        const u = (e, t, a) => {
            const s = [];
            return (
              e.childList.forEach((i, l) => {
                const o = `${a}_${l}`;
                if ((0, r.dz)(i)) {
                  const e = i,
                    t = e.blockType,
                    a = n.IY[t],
                    r = u(e, a, o);
                  s.push(...r);
                } else s.push(t({ elementList: [i], textBlock: e, key: o }));
              }),
              s
            );
          },
          s = (e) => {
            const t = [];
            return (
              e.forEach((e, a) => {
                t.push(
                  ...((e, t) => {
                    const a = [],
                      s = e.blockType,
                      i = n.IY[s],
                      l = u(e, i, t);
                    return (
                      s === r.kH.NoBreakWrapper
                        ? a.push(i({ elementList: l, textBlock: e, key: `${t}` }))
                        : a.push(...l),
                      a
                    );
                  })(e, a),
                );
              }),
              t
            );
          };
      },
      6960: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = (e, t, a, n) => {
          let r = t.exec(e),
            u = 0;
          for (; r;)
            (u !== r.index && a(e.slice(u, r.index)), n(r), (u = t.lastIndex), (r = t.exec(e)));
          u !== e.length && a(e.slice(u));
        };
      },
      131: (e, t, a) => {
        "use strict";
        a.d(t, { T: () => c });
        var n = a(6179),
          r = a.n(n),
          u = a(9053);
        const s = (e, t) => !e || e.offsetTop + e.offsetHeight > t,
          i = (e, t) => e.offsetLeft + e.offsetWidth - t,
          l = (e, t, a) => {
            if (!e || !e.textContent) return [!1, 0];
            if (e.offsetLeft > t) return [!1, 0];
            const n = i(e, t),
              r = e.textContent.length,
              u = e.offsetWidth / r,
              s = Math.ceil(n / u);
            if (n > 0) {
              const n = Math.floor((t - e.offsetLeft) / u);
              return n >= a ? [!0, a + s] : [!1, n];
            }
            const l = Math.max(a + s, 0);
            return r < l ? [!1, 0] : [!0, l];
          },
          o = (e, t, a, n, s, i) => {
            let c = -1,
              m = null;
            for (let d = a; d >= 0; d--) {
              const a = e[d],
                _ = Number(e[d].getAttribute(u.bF));
              if (_ === u.kH.LineBreak || _ === u.kH.NewLine || _ === u.kH.Binding) continue;
              const E = a.textContent || "";
              if (!(a.childElementCount > 1)) {
                const e = l(a, n, s),
                  u = e[0],
                  o = e[1];
                if (!u) {
                  o > 0 && (s -= o);
                  continue;
                }
                const _ = E.slice(0, E.length - o) + i,
                  g = t[d];
                ((m = r().cloneElement(g, g.props, _)), (c = d));
                break;
              }
              {
                const e = a.children,
                  u = t[d],
                  l = u.props.children,
                  _ = o(e, l, e.length - 1, n, s, i),
                  g = _[0],
                  b = _[1];
                if (!(g < 0)) {
                  const e = l.slice(0, g);
                  ((m = r().cloneElement(u, u.props, e, b)), (c = d));
                  break;
                }
                s -= E.length;
              }
            }
            return [c, m];
          },
          c = (e, t, a, n = u.YA) => {
            const r = [...t],
              l = e.current;
            if (!l) return [r, !1];
            const c = a.height,
              m = a.width,
              d = l.lastElementChild;
            if (!s(d, c) && i(d, m) <= 0) return [r, !1];
            const _ = l.children,
              E = ((e, t) => {
                let a = 0,
                  n = e.length - 1;
                for (; n - a >= 0;) {
                  const r = a + Math.ceil(0.5 * (n - a));
                  s(e[r], t) ? (n = r - 1) : (a = r + 1);
                }
                return a - 1;
              })(_, c);
            if (E < 0) return [r, !1];
            const g = o(_, r, E, m, n.length, n),
              b = g[0],
              p = g[1];
            return (p && (r.splice(b, 1, p), r.splice(b + 1)), [r, !0]);
          };
      },
      9053: (e, t, a) => {
        "use strict";
        let n, r, u;
        (a.d(t, { YA: () => i, aF: () => o, bF: () => l, dz: () => s, kH: () => n, v2: () => r }),
          (function (e) {
            ((e[(e.Word = 0)] = "Word"),
              (e[(e.LineBreak = 1)] = "LineBreak"),
              (e[(e.NewLine = 2)] = "NewLine"),
              (e[(e.NoBreakSymbol = 3)] = "NoBreakSymbol"),
              (e[(e.NoBreakWrapper = 4)] = "NoBreakWrapper"),
              (e[(e.Binding = 5)] = "Binding"));
          })(n || (n = {})),
          (function (e) {
            ((e.FlexStart = "flex-start"), (e.Center = "center"), (e.FlexEnd = "flex-end"));
          })(r || (r = {})),
          (function (e) {
            ((e.NBSP = " "), (e.ZWNBSP = "\ufeff"), (e.NEW_LINE = "\n"));
          })(u || (u = {})));
        const s = (e) => void 0 !== e.childList,
          i = "...",
          l = "data-block-type",
          o = { [u.NBSP]: n.NoBreakSymbol, [u.ZWNBSP]: n.NoBreakSymbol, [u.NEW_LINE]: n.LineBreak };
      },
      597: (e, t, a) => {
        "use strict";
        a.d(t, { IY: () => c });
        var n = a(6179),
          r = a.n(n),
          u = a(9053),
          s = a(9627),
          i = a(7629);
        const l = (e) => ({ color: `#${e}` }),
          o = ({ elementList: e, textBlock: t, key: a }) => {
            const n = t.colorTag;
            return n
              ? s.Z[n]
                ? r().createElement(
                    "span",
                    { key: a, "data-block-type": t.blockType, className: s.Z[n] },
                    e,
                  )
                : r().createElement(
                    "span",
                    { key: a, "data-block-type": t.blockType, style: l(n) },
                    e,
                  )
              : r().createElement("span", { key: a, "data-block-type": t.blockType }, e);
          },
          c = {
            [u.kH.Word]: o,
            [u.kH.NoBreakSymbol]: o,
            [u.kH.Binding]: ({ elementList: e, textBlock: t, key: a }) =>
              r().createElement(
                "span",
                { key: a, "data-block-type": t.blockType },
                e.map((e) => r().createElement(r().Fragment, { key: a }, e)),
              ),
            [u.kH.LineBreak]: ({ key: e }) =>
              r().createElement("span", {
                key: e,
                "data-block-type": u.kH.LineBreak,
                className: i.Z.lineBreak,
              }),
            [u.kH.NewLine]: ({ elementList: e, key: t }) =>
              r().createElement(
                "span",
                { key: t, "data-block-type": u.kH.NewLine, className: i.Z.newLine },
                e,
              ),
            [u.kH.NoBreakWrapper]: ({ elementList: e, key: t }) =>
              r().createElement(
                "span",
                { key: t, "data-block-type": u.kH.NoBreakWrapper, className: i.Z.noBreakWrapper },
                e,
              ),
          };
      },
      3458: (e, t, a) => {
        "use strict";
        let n;
        (a.d(t, { Z0: () => r, in: () => n, sx: () => u }),
          (function (e) {
            ((e[(e.NonSet = 0)] = "NonSet"),
              (e[(e.Debug = 10)] = "Debug"),
              (e[(e.Info = 20)] = "Info"),
              (e[(e.Warning = 30)] = "Warning"));
          })(n || (n = {})));
        const r = "tooltip_watched",
          u = 2;
        let s;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(s || (s = {}));
      },
      4828: (e, t, a) => {
        "use strict";
        a.d(t, {
          AB: () => d,
          D9: () => n,
          eX: () => u,
          sC: () => s,
          sk: () => l,
          tL: () => r,
          x3: () => o,
        });
        const n = "crew",
          r = 2e3;
        let u, s, i, l, o, c, m;
        (!(function (e) {
          ((e.Viewed = "viewed"), (e.Click = "click"));
        })(u || (u = {})),
          (function (e) {
            ((e.Hangar = "hangar"),
              (e.PersonalFile = "personal_file_view"),
              (e.PersonalData = "personal_data_view"),
              (e.ServiceRecord = "service_record_view"),
              (e.Barracks = "barracks_view"),
              (e.MemberChange = "member_change_view"),
              (e.QuickTraining = "quick_training_view"),
              (e.TankChange = "tank_change_view"));
          })(s || (s = {})),
          (function (e) {
            e.DocumentChange = "document_change_dialog";
          })(i || (i = {})),
          (function (e) {
            ((e.PremiumTooltip = "personal_file_view_premium_tooltip"),
              (e.MstlTooltip = "personal_file_view_mstl_tooltip"));
          })(l || (l = {})),
          (function (e) {
            ((e.ChangeButtonTooltip = "crew_widget_change_button_tooltip"),
              (e.MstlTooltip = "crew_widget_mstl_tooltip"),
              (e.SlotContextMenu = "crew_widget_slot_context_menu"),
              (e.CrewOperationsButton = "crew_widget_crew_operations_button"));
          })(o || (o = {})),
          (function (e) {
            ((e.FirstnameSelect = "document_change_dialog_firstname_select"),
              (e.Firstname = "document_change_dialog_firstname"),
              (e.LastnameSelect = "document_change_dialog_lastname_select"),
              (e.Lastname = "document_change_dialog_lastname"));
          })(c || (c = {})),
          (function (e) {
            e.CardContextMenu = "barracks_view_card_context_menu";
          })(m || (m = {})));
        const d = {
          [R.views.lobby.crew.personal_case.PersonalFileView("resId")]: s.PersonalFile,
          [R.views.lobby.crew.personal_case.PersonalDataView("resId")]: s.PersonalData,
          [R.views.lobby.crew.personal_case.ServiceRecordView("resId")]: s.ServiceRecord,
          [R.views.lobby.crew.BarracksView("resId")]: s.Barracks,
          [R.views.lobby.crew.HangarCrewWidget("resId")]: s.Hangar,
          [R.views.lobby.crew.MemberChangeView("resId")]: s.MemberChange,
          [R.views.lobby.crew.TankChangeView("resId")]: s.TankChange,
          [R.views.lobby.crew.QuickTrainingView("resId")]: s.QuickTraining,
        };
      },
      1943: (e, t, a) => {
        "use strict";
        a.d(t, { Jp: () => m, Sr: () => _ });
        var n = a(6179),
          r = a(3458);
        const u = ["action", "timeLimit"];
        const s = "metrics",
          i = () => Date.now(),
          l = ({ partnerID: e, item: t, parentScreen: a, itemState: n, info: r }) => ({
            item: t,
            partnerID: e || null,
            parent_screen: a || null,
            item_state: n || null,
            additional_info: r || null,
          }),
          o = (e, t) => {
            const a = (0, n.useCallback)(
              (a, n = r.in.Info, u) => {
                (u || (u = {}),
                  Object.keys(u).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: t,
                      action: a,
                      logLevel: n,
                      params: JSON.stringify(u),
                    }));
              },
              [e, t],
            );
            return (e, t, n) => a(e, t, n);
          },
          c = (e, t) => {
            const a = o(e, t),
              r = (0, n.useRef)(new Map()),
              u = (0, n.useRef)(new Map()),
              s = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = r.current.get(e);
                  (void 0 !== t && t > 0) || r.current.set(e, i());
                },
                [r],
              ),
              l = (0, n.useCallback)(() => {
                (r.current.clear(), u.current.clear());
              }, [r, u]),
              c = (0, n.useCallback)(
                (e) => {
                  e &&
                    void 0 !== r.current.get(e) &&
                    void 0 === u.current.get(e) &&
                    u.current.set(e, i());
                },
                [r, u],
              ),
              m = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = r.current.get(e);
                  if (void 0 === t) return;
                  const a = u.current.get(e);
                  if (void 0 === a) return;
                  u.current.delete(e);
                  const n = i() - a;
                  r.current.set(e, t + n);
                },
                [r, u],
              ),
              d = (0, n.useCallback)(
                (e, t = 0, n, s) => {
                  const l = r.current.get(e);
                  if (void 0 === l) return;
                  (void 0 !== u.current.get(e) && m(e), r.current.delete(e));
                  const o = (i() - l) / 1e3;
                  o <= t ||
                    ((s = ((e, t) => (void 0 === e && (e = {}), (e.timeSpent = t), e))(s, o)),
                    a(e, n, s));
                },
                [r, u, a, m],
              );
            return [
              (e) => s(e),
              (e, t, a, n) => d(e, t, a, n),
              () => l(),
              (e) => c(e),
              (e) => m(e),
            ];
          },
          m = (e) => {
            const t = o(e, s),
              a = (0, n.useCallback)(
                (e) => {
                  t(e.action, e.logLevel, l(e));
                },
                [t],
              );
            return (e) => a(e);
          },
          d = (e) => {
            const t = c(e, s),
              a = t[0],
              r = t[1],
              u = t[2],
              i = t[3],
              o = t[4],
              m = (0, n.useCallback)(
                (e) => {
                  const t = e.action,
                    a = e.timeLimit,
                    n = e.logLevel;
                  r(t, a, n, l(e));
                },
                [r],
              );
            return [(e) => a(e), (e) => m(e), () => u(), (e) => i(e), (e) => o(e)];
          },
          _ = (e, t) => {
            const a = d(e),
              s = a[0],
              i = a[1],
              l = t.action,
              o = t.timeLimit,
              c = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(t, u);
            return (0, n.useMemo)(
              () => ({
                onShow: () => s(l || r.Z0),
                onHide: () => i(Object.assign({ action: l || r.Z0, timeLimit: o || r.sx }, c)),
              }),
              [l, o, c, s, i],
            );
          };
      },
      7362: (e, t, a) => {
        "use strict";
        var n = a(7739),
          r = a(6179),
          u = a.n(r),
          s = a(6483),
          i = a.n(s),
          l = a(926),
          o = a.n(l),
          c = a(5415);
        const m = ["children", "className"];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            d.apply(this, arguments)
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
          E = {
            [c.Aq.ExtraSmall]: "",
            [c.Aq.Small]: o().SMALL_HEIGHT,
            [c.Aq.Medium]: `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT}`,
            [c.Aq.Large]: `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT} ${o().LARGE_HEIGHT}`,
            [c.Aq.ExtraLarge]:
              `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT} ${o().LARGE_HEIGHT} ${o().EXTRA_LARGE_HEIGHT}`,
          },
          g = {
            [c.cJ.ExtraSmall]: "",
            [c.cJ.Small]: o().SMALL,
            [c.cJ.Medium]: `${o().SMALL} ${o().MEDIUM}`,
            [c.cJ.Large]: `${o().SMALL} ${o().MEDIUM} ${o().LARGE}`,
            [c.cJ.ExtraLarge]: `${o().SMALL} ${o().MEDIUM} ${o().LARGE} ${o().EXTRA_LARGE}`,
          },
          b = (e) => {
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
              })(e, m);
            const r = (0, c.GS)(),
              s = r.mediaWidth,
              l = r.mediaHeight,
              o = r.mediaSize;
            return u().createElement("div", d({ className: i()(a, _[s], E[l], g[o]) }, n), t);
          },
          p = ["children"];
        const v = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, p);
          return u().createElement(n.ZN, null, u().createElement(b, a, t));
        };
        var h = a(493),
          A = a.n(h),
          C = a(7727);
        const f = u().memo;
        const D = {
            base: "HorizontalTabs_base_92",
            tab: "HorizontalTabs_tab_ca",
            tab__medium: "HorizontalTabs_tab__medium_88",
            tab__active: "HorizontalTabs_tab__active_3e",
            tab__nonInteractive: "HorizontalTabs_tab__nonInteractive_ce",
            state: "HorizontalTabs_state_3d",
            highlight: "HorizontalTabs_highlight_9e",
            border: "HorizontalTabs_border_08",
            border__left: "HorizontalTabs_border__left_64",
            border__right: "HorizontalTabs_border__right_45",
            divider: "HorizontalTabs_divider_6f",
            title: "HorizontalTabs_title_10",
            notification: "HorizontalTabs_notification_89",
            notification__symbol: "HorizontalTabs_notification__symbol_8b",
            notification__small: "HorizontalTabs_notification__small_7c",
            notification__large: "HorizontalTabs_notification__large_a2",
            notification__dot: "HorizontalTabs_notification__dot_d7",
            notification__medium: "HorizontalTabs_notification__medium_19",
          },
          F = { mouseEnter: "highlight", click: "play" },
          B = (e, { active: t, enableInteractiveActiveTab: a = !1 }) => !!a || e !== t,
          k = f(function (e) {
            const t = e.active,
              a = e.tabs,
              n = e.onClick,
              r = e.onMouseEnter,
              s = e.onMouseLeave,
              l = e.className,
              o = e.classNames,
              c = e.sounds,
              m = void 0 === c ? F : c,
              d = (t) => () => {
                B(t, e) && (m.click && (0, C.G)(m.click), null == n || n(t));
              },
              _ = (t) => () => {
                B(t, e) && (m.mouseEnter && (0, C.G)(m.mouseEnter), null == r || r(t));
              },
              E = (t) => () => {
                B(t, e) && (m.mouseLeave && (0, C.G)(m.mouseLeave), null == s || s(t));
              };
            return u().createElement(
              "div",
              { className: i()(D.base, l) },
              a.map(({ id: n, title: r, notification: s }, l) => {
                var c;
                return u().createElement(
                  "div",
                  {
                    className: i()(
                      D.tab,
                      n === t && i()(D.tab__active, null == o ? void 0 : o.activeTab),
                      !B(n, e) && D.tab__nonInteractive,
                      null == o ? void 0 : o.tab,
                    ),
                    key: n,
                    onClick: d(n),
                    onMouseEnter: _(n),
                    onMouseLeave: E(n),
                  },
                  ((e, t) => !((e, t) => e.length - 1 === t)(e, t))(a, l) &&
                    u().createElement("div", {
                      className: i()(D.divider, null == o ? void 0 : o.divider),
                    }),
                  u().createElement(
                    "div",
                    { className: i()(D.state, null == o ? void 0 : o.state) },
                    u().createElement("div", {
                      className: i()(D.highlight, null == o ? void 0 : o.highlight),
                    }),
                    u().createElement("div", {
                      className: i()(
                        D.border,
                        D.border__left,
                        null == o ? void 0 : o.border,
                        null == o ? void 0 : o.borderLeft,
                      ),
                    }),
                    u().createElement("div", {
                      className: i()(
                        D.border,
                        D.border__right,
                        null == o ? void 0 : o.border,
                        null == o ? void 0 : o.borderRight,
                      ),
                    }),
                  ),
                  u().createElement(
                    "div",
                    { className: i()(D.title, null == o ? void 0 : o.title) },
                    r,
                  ),
                  void 0 !== s &&
                    u().createElement(
                      "div",
                      {
                        className: i()(
                          D.notification,
                          D[`notification__${s.type}`],
                          D[`notification__${null != (c = s.size) ? c : "medium"}`],
                          null == o ? void 0 : o.notification,
                        ),
                      },
                      "dot" !== s.type && s.value,
                    ),
                );
              }),
            );
          });
        var w = a(3138),
          y = a(5521);
        a(4179);
        const S = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function N(e = y.n.NONE, t = S, a = !1) {
          (0, r.useEffect)(() => {
            if (e !== y.n.NONE)
              return (
                window.addEventListener("keydown", n, a),
                () => {
                  window.removeEventListener("keydown", n, a);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (w.O.view.isEventHandled()) return;
                (w.O.view.setEventHandled(), t(n), a && n.stopPropagation());
              }
            }
          }, [t, e, a]);
        }
        var I = a(3403),
          T = a(3215);
        let L, x, M, P;
        (!(function (e) {
          ((e.Initialization = "initialization"),
            (e.Loading = "loading"),
            (e.ForceLoading = "forceLoading"),
            (e.Loaded = "loaded"));
        })(L || (L = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.Loading = "loading"),
              (e.Loaded = "loaded"),
              (e.Failed = "failed"));
          })(x || (x = {})),
          (function (e) {
            ((e.Initialization = "initialization"), (e.Loaded = "loaded"), (e.Failed = "failed"));
          })(M || (M = {})),
          (function (e) {
            ((e.Initialization = "initialization"),
              (e.BrowserLoading = "browserLoading"),
              (e.PageLoading = "pageLoading"),
              (e.ForceLoading = "forceLoading"),
              (e.PageFailed = "pageFailed"),
              (e.TextureFailed = "textureFailed"),
              (e.Loaded = "loaded"));
          })(P || (P = {})));
        (L.Initialization, x.Initialization);
        const O = (0, T.q)()(
            ({ observableModel: e }) => {
              const t = { groups: e.array("groups", []) };
              return Object.assign({}, t);
            },
            ({ externalModel: e }) => ({
              onGroupClick: e.createCallback((e) => ({ groupName: e }), "onGroupClick"),
            }),
          ),
          H = O[0],
          W = O[1];
        var G = a(794),
          V = a(7701),
          z = a(9480),
          Z = a(7078),
          j = a(3618);
        let $;
        !(function (e) {
          ((e[(e.none = 0)] = "none"),
            (e[(e.increase = 1)] = "increase"),
            (e[(e.decrease = 2)] = "decrease"),
            (e[(e.mixed = 3)] = "mixed"));
        })($ || ($ = {}));
        const U = {
            base: "BuffIcon_base_c8",
            base__increase: "BuffIcon_base__increase_60",
            base__decrease: "BuffIcon_base__decrease_31",
            base__mixed: "BuffIcon_base__mixed_23",
          },
          X = u().memo(function ({ buffIconType: e, className: t }) {
            return e === $.none
              ? null
              : u().createElement("div", { className: i()(U.base, U[`base__${$[e]}`], t) });
          });
        var q = a(7030);
        const K = "Delta_base_3e",
          Y = "Delta_base__positive_82",
          Q = "Delta_base__negative_86",
          J = u().memo(function ({ isPositive: e, width: t, isUseAnim: a }) {
            const n = (0, q.useSpring)({
                from: { left: 0, width: 0 },
                left: e ? 0 : t,
                width: e ? 0 : Math.abs(t),
                config: { duration: le },
                delay: e ? 0 : le,
                immediate: !a,
              }),
              r = (0, q.useSpring)({
                from: { left: 2, width: 0 },
                left: 2,
                width: e ? t : 0,
                config: { duration: le },
                delay: e || 0 === t ? le : 0,
                immediate: !a,
              });
            return u().createElement(
              u().Fragment,
              null,
              u().createElement(q.animated.div, { className: i()(K, Q), style: n }),
              u().createElement(q.animated.div, { className: i()(K, Y), style: r }),
            );
          }),
          ee = "Indicator_base_b9",
          te = "Indicator_progress_ce",
          ae = "Indicator_progressMarker_b4",
          ne = "Indicator_indicator_bc",
          re = "Indicator_indicator__start_80",
          ue = "Indicator_indicator__end_3b",
          se = "Indicator_marker_f7",
          ie = "Indicator_valueLine_1d",
          le = 300,
          oe = u().memo(function ({
            minValue: e,
            maxValue: t,
            value: a,
            markerValue: n,
            delta: r,
            isUseAnim: s,
          }) {
            const l = n === e ? 2 : (n / t) * 254,
              o = (a / t) * 254,
              c = (r / t) * 254,
              m = r > 0,
              d = { config: { duration: le }, immediate: !s },
              _ = (0, q.useSpring)(
                Object.assign({ from: { left: 2 }, to: { left: l }, delay: le }, d),
              ),
              E = (0, q.useSpring)(
                Object.assign({ from: { width: e }, to: { width: o }, delay: le }, d),
              );
            return u().createElement(
              "div",
              { className: ee },
              u().createElement(
                "div",
                { className: te },
                u().createElement("div", { className: i()(ne, re) }),
                u().createElement(q.animated.div, { className: ie, style: E }),
                u().createElement(
                  "div",
                  { className: ae },
                  u().createElement(
                    q.animated.div,
                    { className: se, style: _ },
                    u().createElement(J, { isPositive: m, width: c, isUseAnim: s }),
                  ),
                ),
                u().createElement("div", { className: i()(ne, ue) }),
              ),
            );
          });
        let ce;
        !(function (e) {
          ((e.None = "none"), (e.Increase = "increase"), (e.Decrease = "decrease"));
        })(ce || (ce = {}));
        var me = a(9053);
        const de = {
            base: "Param_base_51",
            value: "Param_value_51",
            icon: "Param_icon_37",
            name: "Param_name_82",
            highlight: "Param_highlight_81",
            highlight__increase: "Param_highlight__increase_35",
            highlight__decrease: "Param_highlight__decrease_ec",
          },
          _e = u().memo(function ({
            id: e,
            value: t,
            tooltipID: a,
            isEnabled: n,
            highlightType: r,
            localizedName: s,
          }) {
            return u().createElement(
              Z.t,
              {
                args: { tooltipId: a, paramId: e },
                targetId: R.views.lobby.hangar.subViews.VehicleParams("resId"),
                isEnabled: n,
              },
              u().createElement(
                "div",
                { className: de.base },
                u().createElement(j.w, {
                  justifyContent: me.v2.FlexEnd,
                  classMix: de.value,
                  text: t,
                }),
                u().createElement("div", {
                  className: de.icon,
                  style: { backgroundImage: `url('R.images.gui.maps.icons.vehParams.small.${e}')` },
                }),
                u().createElement(
                  "div",
                  { className: de.name },
                  s || R.strings.menu.tank_params.$dyn(e),
                ),
                r !== ce.None &&
                  u().createElement("div", { className: i()(de.highlight, de[`highlight__${r}`]) }),
              ),
            );
          }),
          Ee = "Group_base_66",
          ge = "Group_group_07",
          be = "Group_hoverBg_97",
          pe = "Group_hoverBg__scrollable_2a",
          ve = "Group_groupHeader_f5",
          he = "Group_name_21",
          Ae = "Group_arrow_96",
          Ce = "Group_arrow__opened_47",
          fe = "Group_params_88",
          De = "Group_params__opened_9a",
          Fe = "Group_separator_b5",
          Be = "Group_right_13",
          ke = "Group_buff_fa",
          we = "Group_value_00",
          ye = "Group_value__additional_81";
        function Se() {
          return (
            (Se =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Se.apply(this, arguments)
          );
        }
        const Ne = (0, I.Pi)(
            ({
              id: e,
              isOpen: t,
              params: a,
              extraParams: n,
              tooltipID: r,
              indicator: s,
              value: l,
              additionalValue: o,
              buffIconType: c,
              isEnabled: m,
              isScrollable: d,
            }) => {
              const _ = W().controls,
                E = n && n.length > 0;
              return u().createElement(
                "div",
                { className: Ee },
                u().createElement(
                  Z.t,
                  {
                    args: { tooltipId: r, paramId: e },
                    targetId: R.views.lobby.hangar.subViews.VehicleParams("resId"),
                    isEnabled: m,
                  },
                  u().createElement(
                    "div",
                    {
                      className: ge,
                      onClick: () => _.onGroupClick(e),
                      onMouseEnter: C.$.playHighlight,
                    },
                    u().createElement("div", { className: i()(be, d && pe) }),
                    u().createElement(
                      "div",
                      { className: ve },
                      u().createElement("div", { className: i()(Ae, t && Ce) }),
                      u().createElement(
                        "div",
                        { className: he },
                        R.strings.menu.tank_params.$dyn(e),
                      ),
                      u().createElement(
                        "div",
                        { className: Be },
                        u().createElement(X, { buffIconType: c, className: ke }),
                        o && u().createElement(j.w, { classMix: i()(we, ye), text: o }),
                        u().createElement(j.w, { classMix: we, text: l }),
                      ),
                    ),
                    u().createElement(oe, s),
                  ),
                ),
                u().createElement(
                  "div",
                  { className: i()(fe, t && De) },
                  z.UI(a, (e) => u().createElement(_e, Se({ key: e.id }, e))),
                  E && u().createElement("div", { className: Fe }),
                  z.UI(n, (e) => u().createElement(_e, Se({ key: e.id }, e))),
                ),
              );
            },
          ),
          Ie = {
            base: "VehicleParams_base_3b",
            base__bg: "VehicleParams_base__bg_c4",
            scroll: "VehicleParams_scroll_59",
            content: "VehicleParams_content_09",
            barBase: "VehicleParams_barBase_6f",
          };
        function Te() {
          return (
            (Te =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Te.apply(this, arguments)
          );
        }
        const Le = {
            settings: {
              step: { type: "fixed", value: 48, clampedArrowStepTimeout: 0 },
              animationConfig: { tension: 0, friction: 0 },
            },
          },
          xe = (0, I.Pi)(({ showBackground: e = !0, className: t }) => {
            const a = W().model,
              n = (0, r.useState)(!1),
              s = n[0],
              l = n[1],
              o = a.groups.get(),
              c = (0, V.c4)(Le);
            return (
              (0, r.useEffect)(() => {
                const e = () => {
                  const e = c.getContainerSize(),
                    t = c.getWrapperSize();
                  e && t && l(e > t);
                };
                return (
                  c.events.on("recalculateContent", e),
                  () => {
                    c.events.off("recalculateContent", e);
                  }
                );
              }, [c]),
              u().createElement(
                "div",
                { className: i()(Ie.base, e && Ie.base__bg, t) },
                u().createElement(
                  G.X.Vertical.Area.Default,
                  {
                    api: c,
                    barClassNames: { base: Ie.barBase },
                    scrollClassName: Ie.scroll,
                    scrollClassNames: { content: Ie.content },
                  },
                  u().createElement(
                    "div",
                    { className: Ie.groups },
                    z.UI(o, (e) =>
                      u().createElement(Ne, Te({ key: e.id }, e, { isScrollable: s })),
                    ),
                  ),
                ),
              )
            );
          }),
          Re = (0, r.memo)(function (e) {
            const t = (0, r.useMemo)(() => ({ rootId: e.resId }), [e.resId]);
            return u().createElement(H, { options: t }, u().createElement(xe, e));
          }),
          Me = {
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
          Pe = [
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
        function Oe() {
          return (
            (Oe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Oe.apply(this, arguments)
          );
        }
        class He extends u().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, C.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, C.G)(this.props.soundClick));
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
              s = e.type,
              l = e.classNames,
              o = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onMouseUp,
              _ =
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
                })(e, Pe)),
              E = i()(Me.base, Me[`base__${s}`], Me[`base__${r}`], null == l ? void 0 : l.base),
              g = i()(Me.icon, Me[`icon__${s}`], Me[`icon__${r}`], null == l ? void 0 : l.icon),
              b = i()(Me.glow, null == l ? void 0 : l.glow),
              p = i()(Me.caption, Me[`caption__${s}`], null == l ? void 0 : l.caption),
              v = i()(Me.goto, null == l ? void 0 : l.goto);
            return u().createElement(
              "div",
              Oe(
                {
                  className: E,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(m),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: a,
                },
                _,
              ),
              "info" !== s && u().createElement("div", { className: Me.shine }),
              u().createElement(
                "div",
                { className: g },
                u().createElement("div", { className: b }),
              ),
              u().createElement("div", { className: p }, t),
              n && u().createElement("div", { className: v }, n),
            );
          }
        }
        He.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const We = ({ onClick: e }) =>
            u().createElement(He, {
              onClick: e,
              caption: R.strings.crew.common.navigation.aboutCrew(),
              type: "info",
            }),
          Ge = "common_close_0e",
          Ve = ({ onClick: e, label: t = R.strings.menu.viewHeader.closeBtn.label() }) =>
            u().createElement(He, {
              onClick: e,
              classNames: { base: Ge },
              caption: t,
              type: "close",
              side: "right",
            }),
          ze = "TopButtons_base_ef",
          Ze = "TopButtons_leftButtons_9e",
          je = "TopButtons_rightButtons_33",
          $e = u().memo(function ({
            backButtonLabel: e,
            closeButtonLabel: t = R.strings.menu.viewHeader.closeBtn.label(),
            onBackClick: a,
            onAboutClick: n,
            onCloseClick: r,
            className: s,
            classNames: l,
          }) {
            return u().createElement(
              "div",
              { className: i()(ze, s) },
              u().createElement(
                "div",
                { className: i()(Ze, null == l ? void 0 : l.leftButtons) },
                e && a && u().createElement(He, { onClick: a, caption: e, type: "back" }),
              ),
              u().createElement(
                "div",
                { className: i()(je, null == l ? void 0 : l.rightButtons) },
                n && u().createElement(We, { onClick: n }),
                r && u().createElement(Ve, { onClick: r, label: t }),
              ),
            );
          });
        var Ue = a(9690),
          Xe = a(3649);
        const qe = {
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
        let Ke, Ye;
        (!(function (e) {
          ((e.extraSmall = "extraSmall"), (e.medium = "medium"), (e.big = "big"));
        })(Ke || (Ke = {})),
          (function (e) {
            ((e.colored = "colored"), (e.white = "white"), (e.whiteSpanish = "whiteSpanish"));
          })(Ye || (Ye = {})));
        const Qe = ({
            isElite: e,
            vehicleName: t,
            vehicleShortName: a,
            vehicleType: n,
            vehicleLvl: r,
            tags: s,
            isPremiumIGR: l,
            size: o = Ke.extraSmall,
            type: c = Ye.colored,
            className: m,
            classNames: d,
            isShortName: _ = !1,
          }) => {
            const E = `${(0, Xe.BN)(n)}${e ? "_elite" : ""}`,
              g = R.images.gui.maps.icons.vehicleTypes.big.$dyn(E);
            return u().createElement(
              "div",
              {
                className: i()(
                  qe.base,
                  qe[`base__size${(0, Xe.e)(o)}`],
                  qe[`base__type${(0, Xe.e)(c)}`],
                  s && z.UI(s, (e) => qe[`base__tag${(0, Xe.e)(e)}`]),
                  m,
                ),
              },
              u().createElement(
                "div",
                { className: i()(qe.level, null == d ? void 0 : d.level) },
                (0, Ue.HG)(r),
              ),
              u().createElement("div", {
                className: i()(qe.type, e && qe.type__elite, null == d ? void 0 : d.typeIcon),
                style: { backgroundImage: `url(${g})` },
              }),
              l && u().createElement("div", { className: qe.premiumIGR }),
              u().createElement(
                "div",
                { className: i()(qe.name, null == d ? void 0 : d.name) },
                _ ? a : t,
              ),
            );
          },
          Je = "VehicleParamsDecorator_base_32",
          et = "VehicleParamsDecorator_vehicleInfo_02",
          tt = "VehicleParamsDecorator_tankName_ac",
          at = "VehicleParamsDecorator_tankLvl_26",
          nt = "VehicleParamsDecorator_type_e7",
          rt = "VehicleParamsDecorator_tip_6c",
          ut = ["children", "isPerkTipShown"];
        function st() {
          return (
            (st =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            st.apply(this, arguments)
          );
        }
        const it = (e) => {
          let t = e.children,
            a = e.isPerkTipShown,
            n = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, ut);
          return u().createElement(
            "div",
            { className: Je },
            u().createElement(
              Qe,
              st({ className: et, classNames: { name: tt, level: at, typeIcon: nt } }, n, {
                isShortName: !0,
              }),
            ),
            t,
            a &&
              u().createElement(
                "div",
                { className: rt },
                R.strings.crew.vehicleParamsDecorator.perkTip(),
              ),
          );
        };
        var lt = a(8727),
          ot = a(4598),
          ct = a(1612),
          mt = a(9174),
          dt = a(3946);
        const _t = (0, T.q)()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  {},
                  e.primitives(["currentTabId", "background", "nation", "backButtonLabel"]),
                  {
                    tabs: e.array("tabs"),
                    vehicleInfo: e.object("vehicleInfo"),
                    isTankmanContainerTTCVisible: mt.LO.box(!1),
                  },
                ),
                a = (0, dt.Om)(() => z.UI(t.tabs.get(), ot.yR)),
                n = (0, dt.Om)(() => {
                  const e = a();
                  return Boolean(e.length) && t.currentTabId.get() === e[0].id;
                });
              return Object.assign({}, t, { computes: { getTabs: a, isTTCPerkTipShown: n } });
            },
            ({ externalModel: e, model: t }) =>
              Object.assign(
                {
                  close: e.createCallbackNoArgs("onClose"),
                  closeWithEsc: e.createCallback(() => ({ isFromEscape: !0 }), "onClose"),
                  back: e.createCallbackNoArgs("onBack"),
                  hangar: e.createCallbackNoArgs("onHangar"),
                  tabChange: e.createCallback((e) => ({ tabId: e }), "onTabChange"),
                  aboutCrew: e.createCallbackNoArgs("onAbout"),
                },
                (0, ct.h)({
                  setTankmanContainerTTCVisible: (e) => t.isTankmanContainerTTCVisible.set(e),
                }),
              ),
          ),
          Et = _t[0],
          gt = _t[1],
          bt = "Spinner_base_87",
          pt = "Spinner_caption_cf",
          vt = "Spinner_gear_c4",
          ht = "Spinner_logo_bf",
          At = ({ message: e, className: t, classNames: a }) =>
            u().createElement(
              "div",
              { className: i()(bt, t) },
              e &&
                u().createElement("div", { className: i()(pt, null == a ? void 0 : a.caption) }, e),
              u().createElement("div", { className: i()(vt, null == a ? void 0 : a.gear) }),
              u().createElement("div", { className: i()(ht, null == a ? void 0 : a.logo) }),
            );
        var Ct = a(3457);
        const ft = "Error_base_46",
          Dt = "Error_alertIcon_04",
          Ft = "Error_errorCaption_f2",
          Bt = "Error_button_cd",
          kt = ({ errorBtnLabel: e, errorBtnClickHandler: t, errorMessage: a }) =>
            u().createElement(
              "div",
              { className: ft },
              u().createElement("div", { className: Dt }),
              u().createElement("div", { className: Ft }, a),
              u().createElement(Ct.u5, { size: Ct.qE.medium, mixClass: Bt, onClick: t }, e),
            );
        kt.defaultProps = { errorBtnLabel: "", errorMessage: "" };
        const wt = "Waiting_base_c5",
          yt = "Waiting_blackOverlay_55",
          St = ({
            message: e,
            isError: t,
            errorMessage: a,
            errorBtnLabel: n,
            errorBtnClickHandler: s,
            overlayAlpha: i,
          }) => {
            const l = u().createRef();
            return (
              (0, r.useEffect)(() => {
                const e = l.current;
                e && i && (e.style.opacity = i);
              }, [l, i]),
              u().createElement(
                "div",
                { className: wt },
                u().createElement("div", { className: yt, ref: l }),
                t
                  ? u().createElement(kt, {
                      errorBtnLabel: n,
                      errorMessage: a,
                      errorBtnClickHandler: s,
                    })
                  : u().createElement(At, { message: e }),
              )
            );
          };
        St.defaultProps = {
          isError: !1,
          message: "",
          overlayAlpha: "0.8",
          errorBtnLabel: R.strings.dialogs.disconnected.cancel(),
          errorMessage: "",
        };
        var Nt = a(362),
          It = a(3293),
          Tt = a(894);
        const Lt = "ViewMapper_base_42",
          xt = u().lazy(() => Promise.resolve().then(a.bind(a, 3293))),
          Rt = u().lazy(() => Promise.resolve().then(a.bind(a, 362))),
          Mt = u().lazy(() => Promise.resolve().then(a.bind(a, 894))),
          Pt = {
            [It.PERSONAL_FILE_VIEW_RES_ID]: xt,
            [Nt.PERSONAL_DATA_RES_ID]: Rt,
            [Tt.SERVICE_RECORD_RES_ID]: Mt,
          },
          Ot = ({ id: e, setTTCVisibility: t, className: a }) => {
            const n = Pt[e];
            return u().createElement(
              "div",
              { className: i()(Lt, a) },
              u().createElement(
                r.Suspense,
                {
                  fallback: u().createElement(St, {
                    errorBtnClickHandler: ot.ZT,
                    message: R.strings.waiting.loading(),
                    overlayAlpha: "0.5",
                  }),
                },
                u().createElement(n, { setTTCVisibility: t }),
              ),
            );
          },
          Ht = "TankmanContainerApp_base_42",
          Wt = "TankmanContainerApp_tabs_59",
          Gt = "TankmanContainerApp_widget_f9",
          Vt = "TankmanContainerApp_ttc_a4",
          zt = "TankmanContainerApp_ttc__withPerk_39",
          Zt = "TankmanContainerApp_flag_88";
        function jt() {
          return (
            (jt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            jt.apply(this, arguments)
          );
        }
        const $t = (0, I.Pi)(() => {
          const e = gt(),
            t = e.model,
            a = e.controls,
            n = t.currentTabId.get(),
            s = t.background.get(),
            l = t.computes.getTabs(),
            o = t.computes.isTTCPerkTipShown();
          var c;
          ((c = a.closeWithEsc), N(y.n.ESCAPE, c));
          const m = (0, r.useMemo)(
            () =>
              l.map(({ counter: e, title: t, id: a }) =>
                Object.assign(
                  { id: a, title: t },
                  e > 0 ? { notification: { type: "value", value: e > 99 ? "99+" : e } } : {},
                ),
              ),
            [l],
          );
          return u().createElement(
            "div",
            { style: { backgroundImage: s && `url('${s}')` }, className: Ht },
            u().createElement("div", {
              style: {
                backgroundImage: `url(${R.images.gui.maps.icons.crew.flags.$dyn(t.nation.get())})`,
              },
              className: Zt,
            }),
            u().createElement(Ot, { id: n, setTTCVisibility: a.setTankmanContainerTTCVisible }),
            u().createElement("div", { className: Gt }, u().createElement(lt.O, null)),
            t.isTankmanContainerTTCVisible.get() &&
              u().createElement(
                "div",
                { className: i()(Vt, o && zt) },
                u().createElement(
                  it,
                  jt({}, t.vehicleInfo.get(), { isPerkTipShown: o }),
                  u().createElement(Re, {
                    showBackground: !1,
                    resId: R.views.lobby.hangar.subViews.VehicleParams("resId"),
                  }),
                ),
              ),
            u().createElement(k, { onClick: a.tabChange, tabs: m, active: n, className: Wt }),
            u().createElement($e, {
              onBackClick: a.back,
              backButtonLabel: t.backButtonLabel.get(),
              onAboutClick: a.aboutCrew,
              onCloseClick: a.hangar,
              closeButtonLabel: R.strings.crew.common.navigation.toGarage(),
            }),
          );
        });
        engine.whenReady.then(() => {
          A().render(
            u().createElement(v, null, u().createElement(Et, null, u().createElement($t, null))),
            document.getElementById("root"),
          );
        });
      },
      9367: (e, t, a) => {
        "use strict";
        a.d(t, { Q: () => m });
        var n = a(6483),
          r = a.n(n),
          u = a(9987),
          s = a(6179),
          i = a.n(s);
        const l = "AlertCounter_base_f3",
          o = "AlertCounter_counter_da",
          c = "AlertCounter_label_18",
          m = ({ value: e, className: t }) =>
            i().createElement(
              "div",
              { className: r()(l, t) },
              i().createElement(u.A, { value: e, className: o }),
              !e &&
                i().createElement("div", { className: c }, R.strings.crew.common.exclamationMark()),
            );
      },
      9197: (e, t, a) => {
        "use strict";
        a.d(t, { C: () => D });
        var n = a(6483),
          r = a.n(n),
          u = a(3112),
          s = a(6179),
          i = a.n(s),
          l = a(7613),
          o = a(6373);
        const c = "NumberRange_base_5e",
          m = "NumberRange_base__animation_79",
          d = "NumberRange_from_70",
          _ = "NumberRange_from__red_f8",
          E = "NumberRange_separator_c0",
          g = R.strings.crew.barracks.berthsAmountDivider(),
          b = R.strings.crew.filterPanel.counter.selectLimit,
          p = (0, s.memo)(function ({
            isFilterRange: e,
            from: t,
            to: a,
            className: n,
            isSelectMode: u = !1,
            isSelectedLimitReached: s = !1,
          }) {
            return u
              ? i().createElement(
                  o.i,
                  { header: b.header(), body: b.body(), ignoreShowDelay: !0 },
                  i().createElement(
                    "div",
                    { className: r()(c, n) },
                    i().createElement(l.ZP, { className: d, text: String(t) }),
                    (t !== a || s) &&
                      i().createElement(
                        i().Fragment,
                        null,
                        i().createElement(l.ZP, { className: E, text: g }),
                        i().createElement(l.ZP, { text: String(a) }),
                      ),
                  ),
                )
              : e
                ? i().createElement(
                    "div",
                    { className: r()(c, 0 === t && m, n) },
                    i().createElement(l.ZP, {
                      className: r()(d, 0 === t && a > 0 && _),
                      text: String(t),
                    }),
                    t !== a &&
                      i().createElement(
                        i().Fragment,
                        null,
                        i().createElement(l.ZP, { className: E, text: g }),
                        i().createElement(l.ZP, { text: String(a) }),
                      ),
                  )
                : i().createElement(
                    "div",
                    { className: r()(c, t > a && m, n) },
                    i().createElement(l.ZP, { className: r()(d, t > a && _), text: String(t) }),
                    i().createElement(l.ZP, { className: E, text: g }),
                    i().createElement(l.ZP, { text: String(a) }),
                  );
          }),
          v = "NumberRangeWithLabel_base_2b",
          h = "NumberRangeWithLabel_title_94",
          A = "NumberRangeWithLabel_counter_00",
          C = "NumberRangeWithLabel_counterGlow_1f",
          f = "NumberRangeWithLabel_blink_89",
          D = (0, s.memo)(
            ({
              title: e,
              isGlowVisible: t = !1,
              isSelectedLimitReached: a = !1,
              isFilterRange: n = !1,
              isSelectMode: s = !1,
              className: o,
              classNames: c,
              from: m,
              to: d,
            }) => {
              const _ = (0, u.V)(),
                E = {
                  left:
                    m !== d || a
                      ? 7 * String(m).length * _ + 4 * _
                      : Math.round((7 * String(m).length * _) / 2),
                };
              return i().createElement(
                "div",
                { className: r()(v, o) },
                i().createElement(l.ZP, { className: h, text: e }),
                i().createElement(
                  "div",
                  { className: A },
                  i().createElement(p, {
                    isFilterRange: n,
                    isSelectedLimitReached: a,
                    isSelectMode: s,
                    from: m,
                    to: d,
                  }),
                  t &&
                    n &&
                    i().createElement("div", {
                      style: E,
                      className: r()(C, a && f, null == c ? void 0 : c.counterGlow),
                    }),
                ),
              );
            },
          );
      },
      7077: (e, t, a) => {
        "use strict";
        a.d(t, { G: () => m, U: () => o });
        var n = a(6483),
          r = a.n(n),
          u = a(3649),
          s = a(6179),
          i = a.n(s),
          l = a(3938);
        let o;
        !(function (e) {
          ((e.c158x118 = "big"),
            (e.c100x60 = "small"),
            (e.c100x60Barracks = "barracks"),
            (e.c444x300 = "special"),
            (e.c204x256 = "c_204x256"));
        })(o || (o = {}));
        const c = R.images.gui.maps.icons.tankmen.icons,
          m = (0, s.memo)(({ name: e, size: t = o.c100x60, className: a, isSkin: n = !1 }) => {
            const s = (n ? c.$dyn(t).$dyn("crewSkins") : c.$dyn(t)).$dyn((0, u.BN)(e)),
              m = t === o.c204x256;
            return i().createElement(
              "div",
              {
                style: { backgroundImage: `url(${s})` },
                className: r()(l.Z.base, l.Z[`base__${t}`], a),
              },
              m && i().createElement("div", { className: l.Z.innerShadow }),
            );
          });
      },
      8485: (e, t, a) => {
        "use strict";
        a.d(t, { O: () => o, d: () => c });
        var n = a(6483),
          r = a.n(n),
          u = a(8271),
          s = a(6179),
          i = a.n(s),
          l = a(9426);
        let o;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(o || (o = {}));
        const c = i().memo(function ({ icon: e, type: t, size: a }) {
          const n = (0, s.useMemo)(() => {
              let e;
              return (
                (e =
                  t === u.W.Possible || t === u.W.New
                    ? R.images.gui.maps.icons.tankmen.skills.medium.new_skill()
                    : R.images.gui.maps.icons.crew.$dyn(`${t}SkillFrame_${a}`)),
                { backgroundImage: `url(${e})` }
              );
            }, [t, a]),
            c = (0, s.useMemo)(() => {
              if (!e) return null;
              return {
                backgroundImage: `url(${R.images.gui.maps.icons.tankmen.skills.$dyn(a === o.Big ? "c_22x22" : "small").$dyn(e)})`,
              };
            }, [e, a]);
          return i().createElement(
            "div",
            { className: r()(l.Z.base, l.Z[`base__${a}`]) },
            i().createElement("div", { className: l.Z.bg, style: n }),
            c &&
              i().createElement("div", { className: r()(l.Z.icon, l.Z[`icon__${t}`]), style: c }),
          );
        });
      },
      9631: (e, t, a) => {
        "use strict";
        a.d(t, { C: () => _ });
        var n = a(6483),
          r = a.n(n),
          u = a(3457),
          s = a(2106),
          i = a(9987),
          l = a(6179),
          o = a.n(l),
          c = a(4723);
        const m = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        const _ = o().memo(function (e) {
          let t = e.isActive,
            a = e.counter,
            n = e.className,
            l = e.children,
            _ = e.type,
            E = void 0 === _ ? s.L.secondary : _,
            g = e.size,
            b = void 0 === g ? s.q.small : g,
            p = e.hasIndicator,
            v = void 0 === p || p,
            h = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, m);
          return o().createElement(
            "div",
            { className: r()(c.Z.base, n, t && c.Z.base__active) },
            o().createElement(u.u5, d({ type: E, size: b, mixClass: c.Z.button }, h), l),
            o().createElement("div", { className: c.Z.overlay }),
            v && o().createElement("div", { className: c.Z.indicator }),
            Boolean(a) &&
              o().createElement(
                "div",
                { className: c.Z.counter },
                o().createElement(i.A, { value: a, size: "small" }),
              ),
          );
        });
      },
      7160: (e, t, a) => {
        "use strict";
        a.d(t, { BH: () => u, Fs: () => s, ei: () => n, qb: () => r });
        const n = (e) => Math.sqrt(1 - Math.pow(--e, 2)),
          r = (e) => (e < 0.5 ? 4 * e * e * e : 1 - Math.pow(-2 * e + 2, 3) / 2),
          u = (e) => {
            const t = 1.70158;
            return 1 + 2.70158 * Math.pow(e - 1, 3) + t * Math.pow(e - 1, 2);
          },
          s = (e) => -(Math.cos(Math.PI * e) - 1) / 2;
      },
      8018: (e, t, a) => {
        "use strict";
        a.d(t, { Er: () => l, Gc: () => c, T3: () => u, Xd: () => i, gO: () => o, wP: () => s });
        var n = a(3649);
        const r = R.strings.common.percentValue(),
          u = (e) => (0, n.uF)(r, { value: e });
        let s;
        !(function (e) {
          ((e.Objective = "objective"), (e.Possessive = "possessive"));
        })(s || (s = {}));
        const i = {
            header: R.strings.crew.filterPanel.counter.reset.header(),
            body: R.strings.crew.filterPanel.counter.reset.body(),
          },
          l = {
            header: R.strings.crew.filterPanel.counterMultySelect.reset.header(),
            body: R.strings.crew.filterPanel.counterMultySelect.reset.body(),
          };
        let o;
        !(function (e) {
          ((e.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (e.SHOP_INFO = "shop_info"),
            (e.RUDY = "rudy"));
        })(o || (o = {}));
        const c = (e, t = !1, a = null) => {
          const n = t
            ? R.strings.item_types.tankman.roles.female
            : R.strings.item_types.tankman.roles;
          return (a ? n.$dyn(`${a}Case`) : n).$dyn(e);
        };
      },
      362: (e, t, a) => {
        "use strict";
        (a.r(t), a.d(t, { PERSONAL_DATA_RES_ID: () => $e, default: () => Ue }));
        var n = a(6179),
          r = a.n(n),
          u = a(6483),
          s = a.n(u),
          i = a(1037),
          l = a(5415);
        const o = {
          base: "ListHeader_base_ad",
          title: "ListHeader_title_a8",
          base__memberChange: "ListHeader_base__memberChange_c2",
          base__tankChange: "ListHeader_base__tankChange_fb",
          base__personalData: "ListHeader_base__personalData_aa",
        };
        let c;
        !(function (e) {
          ((e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(c || (c = {}));
        const m = ({ title: e, theme: t = c.Barracks, className: a, children: n }) =>
          r().createElement(
            "div",
            { className: s()(o.base, o[`base__${t}`]) },
            r().createElement("div", { className: s()(o.title, a) }, e),
            n,
          );
        var d = a(5801),
          _ = a(2106),
          E = a(3403),
          g = a(3457),
          b = a(6373),
          p = a(8018);
        const v = "WarningText_base_13",
          h = "WarningText_icon_5d",
          A = "WarningText_label_c6",
          C = r().memo(function ({ label: e }) {
            return r().createElement(
              "div",
              { className: v },
              r().createElement("div", { className: h }),
              r().createElement("div", { className: A }, e),
            );
          }),
          f = "ListEmptyState_base_ae",
          D = "ListEmptyState_content_1e",
          F = "ListEmptyState_shadow_ae",
          B = "ListEmptyState_buttonWrapper_78",
          k = "ListEmptyState_button_f1",
          w = r().memo(function ({
            warningText: e,
            buttonType: t = g.L$.secondary,
            tooltipArgs: a = p.Xd,
            className: n,
            onClick: u,
            children: i,
          }) {
            return r().createElement(
              "div",
              { className: s()(f, n) },
              r().createElement(
                "div",
                { className: D },
                r().createElement("div", { className: F }),
                r().createElement(C, { label: e }),
                i &&
                  r().createElement(
                    "div",
                    { className: B },
                    r().createElement(
                      b.i,
                      a,
                      r().createElement(
                        g.u5,
                        { size: g.qE.small, type: t, onClick: u, mixClass: k },
                        i,
                      ),
                    ),
                  ),
              ),
            );
          });
        var y = a(794),
          S = a(9653);
        var N = a(3138);
        var I = a(4385);
        const T = ({
            startRowIndex: e,
            cellHeight: t,
            paddingTop: a,
            paddingBottom: n,
            amount: r,
            itemsAmountPerRow: u,
            visibleRowsAmount: s,
            numOdfHeadingsBefore: i,
            numOfEmptySlotsInside: l,
          }) => {
            const o = Math.ceil(r / u) * t,
              c = s * t + 40 * l,
              m = e * t + 40 * i;
            return { paddingTop: `${m + a}rem`, paddingBottom: `${Math.max(o - m - c, 0) + n}rem` };
          },
          L = (0, n.memo)((e) => {
            const t = e.className,
              a = e.children,
              n = e.itemsAmountPerRow,
              u = e.visibleRowsAmount,
              s = e.realFirstInRowIndex,
              i = e.amount,
              l = e.numOdfHeadingsBefore,
              o = e.numOfEmptySlotsInside,
              c = Math.min(u * n + o, i - s);
            return r().createElement(
              "div",
              { className: t, style: T(Object.assign({}, e, { numOdfHeadingsBefore: l })) },
              (0, I.K)(c, (e) => a(s + e)),
            );
          }),
          x = "VirtualGrid_base_52",
          M = ({
            amount: e,
            headingsIndexes: t,
            cellWidth: a,
            cellHeight: u,
            children: i,
            api: l,
            classNames: o,
            preloadedRows: c = 1,
            paddingTop: m = 0,
            paddingBottom: d = 0,
          }) => {
            const _ = l.scrollApi,
              E = (0, n.useRef)(0),
              g = (0, n.useState)(0),
              b = g[0],
              p = g[1],
              v = (0, n.useState)(null),
              h = v[0],
              A = v[1],
              C = (0, n.useState)(null),
              f = C[0],
              D = C[1];
            ((0, n.useEffect)(() => {
              const t = (t) => {
                if (!h) return;
                const a = Math.floor((N.O.view.pxToRem(t.value.scrollPosition) - m) / u),
                  n = Math.ceil(e / h),
                  r = Math.max(0, Math.min(a - c, n));
                (p(r), l.startRowIndexChanged(r));
              };
              return (_.events.on("change", t), () => _.events.off("change", t));
            }, [l, _, u, m, h, e, c]),
              (0, n.useEffect)(() => {
                const e = () => {
                    if (_.contentRef.current) {
                      const e = getComputedStyle(_.contentRef.current),
                        t = _.contentRef.current.getBoundingClientRect(),
                        n =
                          N.O.view.pxToRem(t.width) -
                          (parseFloat(e.paddingLeft) + parseFloat(e.paddingRight)),
                        r = Math.floor(n / a),
                        s = Math.ceil(N.O.view.pxToRem(t.height) / u) + 2 * c;
                      ((E.current = r), h !== r && A(r), D(s), l.layoutCalculated(r, s));
                    }
                  },
                  t = () => {
                    const t = E.current;
                    (e(), l.scrollToIndex(b * t));
                  };
                return (
                  _.events.on("recalculateContent", e),
                  _.events.on("resizeHandled", t),
                  () => {
                    (_.events.off("recalculateContent", e), _.events.off("resizeHandled", t));
                  }
                );
              }, [l, _, u, a, h, c, b]),
              (0, n.useEffect)(() => {
                const e = (e, t = !0) => {
                  h && _.applyScroll(Math.floor((e + 1) / h) * u + m, { immediate: t });
                };
                return (l.events.on("scrollToIndex", e), () => l.events.off("scrollToIndex", e));
              }, [l, u, h, m, _]));
            const F = (({ api: e, startRowIndex: t, itemsAmountPerRow: a, headingsIndexes: n }) => {
                const r = t * a;
                if (!n) return r;
                const u = n.reduce((e, t, n, u) => {
                  if (t < r) {
                    if (0 === n) return e + 1;
                    const r = (t - 1 - u[n - 1]) % a;
                    e += 1 - (r ? a - r : 0);
                  }
                  return e;
                }, r);
                return (e.firstCardIndexChanged(u), u);
              })({ api: l, headingsIndexes: t, startRowIndex: b, itemsAmountPerRow: h || 4 }),
              B = (({ offset: e, headingsIndexes: t }) => (t ? t.filter((t) => t < e).length : 0))({
                offset: F,
                headingsIndexes: t,
              }),
              k = (({ amount: e, offset: t, headingsIndexes: a }) =>
                a ? a.filter((a) => a >= t && a <= t + e).length : 0)({
                offset: F,
                amount: (f || 1) * (h || 4),
                headingsIndexes: t,
              }),
              w = (({ offset: e, amount: t, itemsAmountPerRow: a, headingsIndexes: n }) =>
                n
                  ? n.reduce((n, r, u, s) => {
                      if (r >= e && r <= e + t) {
                        if (0 === u) return n + 1;
                        const e = (r - 1 - s[u - 1]) % a;
                        n += 1 + (e ? a - e : 0);
                      }
                      return n;
                    }, 0)
                  : 0)({
                headingsIndexes: t,
                offset: F,
                amount: (f || 1) * (h || 4),
                itemsAmountPerRow: h || 4,
              });
            return r().createElement(
              y.X.Vertical.Default,
              {
                api: _,
                className: null == o ? void 0 : o.scroll,
                areaClassName: null == o ? void 0 : o.areaClassName,
                scrollClassName: null == o ? void 0 : o.scrollClassName,
                scrollClassNames: {
                  content: null == o ? void 0 : o.content,
                  wrapper: null == o ? void 0 : o.wrapper,
                },
              },
              null !== h &&
                null !== f &&
                r().createElement(
                  L,
                  {
                    className: s()(x, null == o ? void 0 : o.inner),
                    paddingBottom: d,
                    realFirstInRowIndex: F,
                    numOdfHeadingsBefore: B,
                    numOdfHeadingsInside: k,
                    paddingTop: m,
                    amount: e,
                    itemsAmountPerRow: h,
                    visibleRowsAmount: f,
                    numOfEmptySlotsInside: w,
                    startRowIndex: b,
                    cellHeight: u,
                  },
                  i,
                ),
            );
          },
          P = "VirtualGridWithFade_scrollAreaFade_94",
          O = ["api", "children", "classNames"];
        function H() {
          return (
            (H =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            H.apply(this, arguments)
          );
        }
        const W = (e) => {
          let t = e.api,
            a = e.children,
            u = e.classNames,
            i = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, O);
          const l = (0, n.useState)(!0),
            o = l[0],
            c = l[1],
            m = t.scrollApi;
          return (
            (0, n.useEffect)(() => {
              const e = () => {
                const e = m.getBounds()[1];
                c(Math.abs(e - m.animationScroll.scrollPosition.goal) > 0.1);
              };
              return (
                m.events.on("change", e),
                m.events.on("recalculateContent", e),
                () => {
                  (m.events.off("change", e), m.events.off("recalculateContent", e));
                }
              );
            }, [m]),
            r().createElement(
              M,
              H(
                {
                  api: t,
                  classNames: Object.assign({}, u, {
                    scrollClassName: s()(null == u ? void 0 : u.scrollClassName, o && P),
                  }),
                },
                i,
              ),
              a,
            )
          );
        };
        var G = a(3215),
          V = a(9480),
          z = a(3946);
        const Z = (0, G.q)()(
            ({ observableModel: e }) => {
              const t = e.array("cardList"),
                a = (0, z.Om)((e) => {
                  const a = V.U2(t.get(), e);
                  if (a) return Object.assign({}, a, { restrictions: [...V.tP(a.restrictions)] });
                });
              return Object.assign({ cardList: t }, e.primitives(["isCardsLocked"]), {
                computes: { getCard: a },
              });
            },
            ({ externalModel: e }) => ({
              resetFilters: e.createCallbackNoArgs("onResetFilters"),
              selectCard: e.createCallback((e, t) => ({ cardID: e, isSkin: t }), "onCardSelected"),
              markAsViewed: e.createCallback((e) => ({ cardID: e }), "onNewCardViewed"),
            }),
          ),
          j = Z[0],
          $ = Z[1];
        let U, X, q;
        (!(function (e) {
          ((e.Default = "default"), (e.Selected = "selected"), (e.Disabled = "disabled"));
        })(U || (U = {})),
          (function (e) {
            ((e.Document = "document"), (e.Skin = "skin"));
          })(X || (X = {})),
          (function (e) {
            ((e.Document = "document"), (e.SuitableSkin = "suitableSkin"));
          })(q || (q = {})));
        var K = a(7727),
          Y = a(3649);
        const Q = {
          base: "FlagIcon_base_25",
          base__c_1080x454: "FlagIcon_base__c_1080x454_6c",
          base__c_240x118: "FlagIcon_base__c_240x118_92",
        };
        let J;
        !(function (e) {
          ((e.c1080x454 = "c_1080x454"), (e.c240x118 = "c_240x118"));
        })(J || (J = {}));
        const ee = (e, t) => {
            switch (t) {
              case J.c1080x454:
                return R.images.gui.maps.icons.crew.flags.$dyn(e);
              case J.c240x118:
                return R.images.gui.maps.icons.tankmen.card.nations.$dyn(e);
            }
          },
          te = r().memo(function ({ nation: e, size: t, className: a }) {
            return r().createElement("div", {
              className: s()(Q.base, Q[`base__${t}`], a),
              style: { backgroundImage: `url('${ee(e, t)}')` },
            });
          }),
          ae = "ListCardAlert_base_52",
          ne = "ListCardAlert_glow_1c",
          re = "ListCardAlert_icon_d2",
          ue = ({ className: e, tooltipArgs: t }) =>
            r().createElement(
              "div",
              { className: s()(ae, e) },
              r().createElement("div", { className: ne }),
              r().createElement(b.i, t, r().createElement("div", { className: re })),
            ),
          se = {
            base: "BaseCard_base_b0",
            base__default: "BaseCard_base__default_2d",
            base__selected: "BaseCard_base__selected_45",
            base__disabled: "BaseCard_base__disabled_47",
            base__alertCardLocked: "BaseCard_base__alertCardLocked_df",
            selectedFrame: "BaseCard_selectedFrame_0a",
            flag: "BaseCard_flag_b5",
            icon: "BaseCard_icon_f4",
            separator: "BaseCard_separator_02",
            cardInfo: "BaseCard_cardInfo_a6",
            cardInfo__withAdditionalInfo: "BaseCard_cardInfo__withAdditionalInfo_cf",
            name: "BaseCard_name_17",
            typeIcon: "BaseCard_typeIcon_71",
            alertIcon: "BaseCard_alertIcon_67",
          };
        let ie;
        !(function (e) {
          ((e.None = "none"), (e.Default = "default"), (e.CardLocked = "cardLocked"));
        })(ie || (ie = {}));
        const le = ({
            icon: e,
            typeIcon: t,
            name: a,
            nation: n,
            cardState: u,
            children: i,
            alertType: l,
          }) =>
            r().createElement(
              "div",
              {
                onMouseEnter: K.$.playHighlight,
                className: s()(se.base, se[`base__${u}`], se[`base__alert${(0, Y.e)(l)}`]),
              },
              u === U.Selected && r().createElement("div", { className: se.selectedFrame }),
              n && r().createElement(te, { nation: n, size: J.c240x118, className: se.flag }),
              r().createElement("div", {
                className: se.icon,
                style: { backgroundImage: `url(${e})` },
              }),
              r().createElement("div", { className: se.separator }),
              r().createElement(
                "div",
                { className: s()(se.cardInfo, Boolean(i) && se.cardInfo__withAdditionalInfo) },
                r().createElement("div", { className: se.name }, a),
                i,
              ),
              r().createElement("div", {
                className: se.typeIcon,
                style: { backgroundImage: `url(${t})` },
              }),
              l !== ie.None &&
                r().createElement(ue, {
                  className: se.alertIcon,
                  tooltipArgs: {
                    header: R.strings.crew.personalData.card.tooltip.locked.title(),
                    body: R.strings.crew.personalData.card.tooltip.locked.body(),
                    isEnabled: l === ie.CardLocked,
                  },
                }),
            ),
          oe = (0, E.Pi)(({ icon: e, name: t, cardState: a, className: n, onClick: u }) => {
            const s = $().model.isCardsLocked.get();
            return r().createElement(
              b.i,
              {
                header: R.strings.crew.personalData.card.tooltip.document.title(),
                body: R.strings.crew.personalData.card.tooltip.document.body(),
                isEnabled: !s,
              },
              r().createElement(
                "div",
                { className: n, onClick: u },
                r().createElement(le, {
                  icon: e,
                  typeIcon: R.images.gui.maps.icons.crew.personalData.c_24x24.document(),
                  name: t,
                  cardState: a,
                  alertType: s ? ie.CardLocked : ie.None,
                }),
              ),
            );
          });
        var ce = a(7078),
          me = a(2603),
          de = a(9367);
        const _e = "InventoryInfo_base_c4",
          Ee = "InventoryInfo_icon_f6",
          ge = "InventoryInfo_amount_59",
          be = r().memo(function ({ amount: e, className: t }) {
            return r().createElement(
              "div",
              { className: s()(_e, t) },
              r().createElement("div", { className: Ee }),
              r().createElement("div", { className: ge }, e),
            );
          }),
          pe = "ResetButton_base_f1",
          ve = "ResetButton_iconWrapper_20",
          he = "ResetButton_icon_a2",
          Ae = "ResetButton_label_f8",
          Ce = ({ className: e }) =>
            r().createElement(
              "div",
              { className: s()(pe, e) },
              r().createElement(
                "div",
                { className: ve },
                r().createElement("div", { className: he }),
              ),
              r().createElement(
                "div",
                { className: Ae },
                R.strings.crew.personalData.card.remove(),
              ),
            ),
          fe = ({ restrictions: e, className: t }) =>
            r().createElement(
              "div",
              { className: t },
              (0, Y.uF)(R.strings.crew.personalData.card.restrictions(), {
                restrictions: V.v_(e, ", "),
              }),
            ),
          De = "SkinCard_base_bb",
          Fe = "SkinCard_resetButton_ff",
          Be = "SkinCard_restrictions_e8",
          ke = "SkinCard_inventoryInfo_62",
          we = "SkinCard_newSkinMark_16",
          ye = (e, t) => (e ? ie.CardLocked : t ? ie.Default : ie.None),
          Se = (0, E.Pi)(
            ({
              id: e,
              nation: t,
              icon: a,
              name: n,
              restrictions: u,
              inventoryCount: i,
              cardState: l,
              newAmount: o,
              className: c,
              onClick: m,
            }) => {
              const d = $(),
                _ = d.model,
                E = d.controls,
                g = u.length > 0,
                b = o > 0;
              return r().createElement(
                ce.t,
                {
                  targetId: R.views.lobby.crew.personal_case.PersonalDataView("resId"),
                  args: { tooltipId: me.lu, skinId: e },
                },
                r().createElement(
                  "div",
                  { className: s()(De, c), onClick: m, onMouseEnter: () => b && E.markAsViewed(e) },
                  r().createElement(
                    le,
                    {
                      icon: a,
                      typeIcon: R.images.gui.maps.icons.crew.personalData.c_24x24.skin(),
                      name: n,
                      nation: t,
                      cardState: l,
                      alertType: ye(_.isCardsLocked.get(), g),
                    },
                    l === U.Selected && r().createElement(Ce, { className: Fe }),
                    g && r().createElement(fe, { restrictions: u, className: Be }),
                  ),
                  r().createElement(be, { amount: i, className: ke }),
                  b && r().createElement(de.Q, { value: o > 1 ? o : void 0, className: we }),
                ),
              );
            },
          );
        function Ne() {
          return (
            (Ne =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ne.apply(this, arguments)
          );
        }
        const Ie = { [X.Skin]: Se, [X.Document]: oe },
          Te = (0, E.Pi)(({ index: e, className: t }) => {
            const a = $(),
              n = a.model,
              u = a.controls,
              s = n.computes.getCard(e);
            if (!s) throw Error(`Index ${e} is out of data card list range`);
            const i = s.cardState !== U.Disabled && !n.isCardsLocked.get(),
              l = Ie[s.cardType];
            return r().createElement(
              l,
              Ne({}, s, {
                className: t,
                onClick: () => i && u.selectCard(s.id, s.cardType === X.Skin),
              }),
            );
          }),
          Le = "DataCardList_base_0a",
          xe = "DataCardList_grid_63",
          Re = "DataCardList_gridWrapper_44",
          Me = "DataCardList_gridWrapper__scaled_8a",
          Pe = "DataCardList_emptyState_f2",
          Oe = "DataCardList_item_b1";
        var He = a(3112);
        const We = (0, E.Pi)(() => {
            const e = (() => {
                const e = y.X.Vertical.useVerticalScrollApi(),
                  t = (0, S.q)(),
                  a = (0, n.useCallback)((e, a = !0) => t.trigger("scrollToIndex", e, a), [t]),
                  r = (0, n.useCallback)((e, a) => t.trigger("layoutCalculated", e, a), [t]),
                  u = (0, n.useCallback)((e) => t.trigger("startRowIndexChanged", e), [t]),
                  s = (0, n.useCallback)((e) => t.trigger("firstCardIndexChanged", e), [t]);
                return (0, n.useMemo)(
                  () => ({
                    scrollToIndex: a,
                    layoutCalculated: r,
                    startRowIndexChanged: u,
                    firstCardIndexChanged: s,
                    scrollApi: e,
                    events: { off: t.off, on: t.on },
                  }),
                  [a, r, u, s, e, t.off, t.on],
                );
              })(),
              t = $(),
              a = t.model,
              u = t.controls,
              i = a.cardList.get().length,
              l = 2 === (0, He.V)();
            return r().createElement(
              "div",
              { className: s()(Le) },
              r().createElement(
                "div",
                { className: s()(Re, l && Me) },
                i > 0
                  ? r().createElement(
                      W,
                      {
                        amount: i,
                        cellWidth: 318,
                        cellHeight: 208,
                        paddingTop: 11,
                        paddingBottom: 11,
                        classNames: { content: xe },
                        api: e,
                      },
                      (e) => r().createElement(Te, { key: e, index: e, className: Oe }),
                    )
                  : r().createElement(
                      w,
                      {
                        warningText: R.strings.crew.personalData.emptyState.noFilteredItems(),
                        buttonType: _.L.primary,
                        onClick: u.resetFilters,
                        className: Pe,
                      },
                      R.strings.crew.filter.reset(),
                    ),
              ),
            );
          }),
          Ge = "PersonalDataApp_base_61",
          Ve = "PersonalDataApp_base__centered_a6",
          ze = "PersonalDataApp_content_36",
          Ze = "PersonalDataApp_content__scaled_66",
          je = () => {
            const e = (0, l.GS)().mediaHeight,
              t = (0, l.GS)().remScreenWidth >= 2560,
              a = 2 === (0, He.V)();
            return r().createElement(
              "div",
              { className: s()(Ge, t && !a && Ve) },
              r().createElement(
                "div",
                { className: s()(ze, a && Ze) },
                r().createElement(m, {
                  title: R.strings.crew.personalData.title(),
                  theme: c.PersonalData,
                }),
                r().createElement(d.p, {
                  popoverDirection: e < l.Aq.Medium ? i.IC.Left : i.IC.Bottom,
                }),
                r().createElement(We, null),
              ),
            );
          },
          $e = R.views.lobby.crew.personal_case.PersonalDataView("resId"),
          Ue = r().memo(
            ({ setTTCVisibility: e }) => (
              e(!1),
              r().createElement(j, { options: { rootId: $e } }, r().createElement(je, null))
            ),
          );
      },
      3293: (e, t, a) => {
        "use strict";
        (a.r(t), a.d(t, { PERSONAL_FILE_VIEW_RES_ID: () => Pe, default: () => Oe }));
        var n = a(6179),
          r = a.n(n),
          u = a(5415),
          s = a(3403),
          i = a(3215),
          l = a(4598),
          o = a(9480),
          c = a(1612),
          m = a(9174),
          d = a(3946);
        const _ = (0, i.q)()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  {},
                  e.primitives([
                    "skillsState",
                    "selectAvailableSkillsCount",
                    "isResetDisable",
                    "isFemale",
                    "hasIncreaseDiscount",
                    "hasDropSkillDiscount",
                    "isTankmanWithDescription",
                    "isTankmanInVehicle",
                  ]),
                  {
                    relevantGroupedSkills: e.array("relevantGroupedSkills"),
                    irrelevantGroupedSkills: e.array("irrelevantGroupedSkills"),
                    commonSkills: e.array("commonSkills"),
                    isTTCVisible: m.LO.box(!1),
                  },
                ),
                a = (e) => o.UI(e, (e) => Object.assign({}, e)),
                n = (e) => o.UI(e, (e) => Object.assign({}, e, { skills: a(e.skills) })),
                r = (0, d.Om)(() => n(t.relevantGroupedSkills.get()), { equals: l.jv }),
                u = (0, d.Om)(() => n(t.irrelevantGroupedSkills.get()), { equals: l.jv }),
                s = (0, d.Om)(() => a(t.commonSkills.get()), { equals: l.jv }),
                i = (0, d.Om)(() => t.isTankmanInVehicle.get() && t.isTTCVisible.get(), !0);
              return Object.assign({}, t, {
                computes: {
                  relevantSkillsGroups: r,
                  irrelevantSkillsGroups: u,
                  commonSkills: s,
                  isTTCVisible: i,
                },
              });
            },
            ({ externalModel: e, model: t }) =>
              Object.assign(
                {
                  increase: e.createCallbackNoArgs("onIncrease"),
                  reset: e.createCallbackNoArgs("onReset"),
                  hoverSkill: e.createCallback((e) => ({ skillId: e }), "onHoverSkill"),
                  leaveSkill: e.createCallback((e) => ({ skillId: e }), "onLeaveSkill"),
                  clickSkill: e.createCallback((e) => ({ skillId: e }), "onClickSkill"),
                },
                (0, c.h)({ setTTCVisible: (e) => t.isTTCVisible.set(e) }),
              ),
          ),
          E = _[0],
          g = _[1];
        var b = a(4022),
          p = a(6483),
          v = a.n(p),
          h = a(2106),
          A = a(6373),
          C = a(3457);
        const f = "ButtonWithDiscountIndicator_base_6c",
          D = "ButtonWithDiscountIndicator_discountIndicator_a5",
          F = "ButtonWithDiscountIndicator_discountIndicator__small_d6",
          B = ["hasDiscount", "className", "children", "wrapperId", "isSmall"];
        const k = r().memo(function (e) {
            let t = e.hasDiscount,
              a = e.className,
              n = e.children,
              u = e.wrapperId,
              s = e.isSmall,
              i = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, B);
            return r().createElement(
              "div",
              { id: u, className: v()(f, a) },
              r().createElement(C.u5, i, n),
              t && r().createElement("div", { className: v()(D, s && F) }),
            );
          }),
          w = "Buttons_base_ec",
          y = "Buttons_increaseBtnContainer_e9",
          S = "Buttons_increaseButton_75",
          N = "Buttons_resetButton_0a",
          I = "Buttons_resetButton__disabled_b9",
          T = "Buttons_resetButton__small_fb",
          L = "Buttons_resetIcon_fa",
          x = "Buttons_buttonWrapper_de",
          M = (0, s.Pi)(function ({ className: e, style: t }) {
            const a = g(),
              n = a.controls,
              s = a.model,
              i = (0, u.GS)().mediaSize,
              l = s.isResetDisable.get(),
              o = i === u.cJ.ExtraSmall || i === u.cJ.Small,
              c = l
                ? R.strings.crew.matrix.resetTooltip.disable
                : R.strings.crew.matrix.resetTooltip.enable;
            return r().createElement(
              "div",
              { className: v()(w, e), style: t },
              r().createElement(
                "div",
                { className: x },
                r().createElement(
                  A.i,
                  {
                    header: R.strings.crew.matrix.increaseTooltip.enable.header(),
                    body: R.strings.crew.matrix.increaseTooltip.enable.body(),
                  },
                  r().createElement(
                    k,
                    {
                      onClick: () => n.increase(),
                      type: h.L.ghost,
                      mixClass: S,
                      hasDiscount: s.hasIncreaseDiscount.get(),
                      className: y,
                    },
                    R.strings.crew.matrix.increaseButton(),
                  ),
                ),
              ),
              r().createElement(
                A.i,
                { header: c.header(), body: c.body(), ignoreMouseClick: l },
                r().createElement(
                  "div",
                  { className: x, id: "matrix_drop_skills_btn" },
                  r().createElement(
                    k,
                    {
                      hasDiscount: s.hasDropSkillDiscount.get(),
                      soundHover: l ? null : "highlight",
                      soundClick: l ? null : "play",
                      onClick: () => !l && n.reset(),
                      type: h.L.ghost,
                      mixClass: v()(N, l && I, o && T),
                      disabled: l,
                      isSmall: o,
                    },
                    o
                      ? r().createElement("div", { className: L })
                      : R.strings.crew.matrix.resetButton(),
                  ),
                ),
              ),
            );
          });
        var P = a(7701);
        let O;
        !(function (e) {
          ((e.LearnAvailable = "available"),
            (e.Training = "training"),
            (e.Achieve = "achieve"),
            (e.ZeroSkills = "zeroSkills"),
            (e.AllSkills = "allSkills"));
        })(O || (O = {}));
        var H = a(3961);
        const W = "SkillRoleIcon_base_6b",
          G = "SkillRoleIcon_base__irrelevant_22",
          V = (0, s.Pi)(function ({ role: e, isIrrelevant: t, className: a }) {
            const n = ((e, t, a) =>
              e
                ? R.strings.crew.matrix.irrelevantQualification.header()
                : t
                  ? R.strings.crew.matrix.skills.roles.female.$dyn(a)
                  : R.strings.crew.matrix.skills.roles.$dyn(a))(t, g().model.isFemale.get(), e);
            return r().createElement(
              A.i,
              { body: n },
              r().createElement("div", {
                style: {
                  backgroundImage: `url(${t ? R.images.gui.maps.icons.tankmen.roles.c_30x30_red.$dyn(e) : R.images.gui.maps.icons.tankmen.roles.c_30x30.$dyn(e)})`,
                },
                className: v()(W, t && G, a),
              }),
            );
          });
        var z = a(4385),
          Z = a(5139);
        function j(e, t, a) {
          const r = (0, n.useMemo)(
            () =>
              (function (e, t, a) {
                return void 0 === a ? (0, Z.Z)(e, t, !1) : (0, Z.Z)(e, a, !1 !== t);
              })(a, e),
            t,
          );
          return ((0, n.useEffect)(() => r.cancel, [r]), r);
        }
        var $ = a(7613),
          U = a(7078),
          X = a(2603),
          q = a(7727);
        const K = {
          base: "SkillIcon_base_43",
          base__small: "SkillIcon_base__small_d0",
          base__c22x22: "SkillIcon_base__c22x22_e5",
          base__medium: "SkillIcon_base__medium_d0",
          base__c36x36_flat: "SkillIcon_base__c36x36_flat_88",
          base__big: "SkillIcon_base__big_ae",
          base__dialogs: "SkillIcon_base__dialogs_e5",
        };
        let Y;
        !(function (e) {
          ((e.c14x14 = "small"),
            (e.c22x22 = "c_22x22"),
            (e.c24x24 = "medium"),
            (e.c36x36_flat = "c_36x36_flat"),
            (e.c52x52 = "big"),
            (e.c180x135 = "dialogs"));
        })(Y || (Y = {}));
        const Q = r().memo(function ({ iconName: e, size: t = Y.c24x24, className: a }) {
          var n;
          return r().createElement("div", {
            style: {
              backgroundImage: `url(${null == (n = R.images.gui.maps.icons.tankmen.skills.$dyn(t)) ? void 0 : n.$dyn(e)})`,
            },
            className: v()(K.base, K[`base__${t}`], a),
          });
        });
        var J = a(8018);
        const ee = {
          base: "Skill_base_8e",
          base__hover: "Skill_base__hover_14",
          base__inProgress: "Skill_base__inProgress_d4",
          base__clickable: "Skill_base__clickable_6c",
          progressBar: "Skill_progressBar_2e",
          stateBg: "Skill_stateBg_7d",
          base__learned: "Skill_base__learned_34",
          disabledPattern: "Skill_disabledPattern_68",
          doublePerkDisabledPattern: "Skill_doublePerkDisabledPattern_95",
          progressText: "Skill_progressText_df",
          base__disabled: "Skill_base__disabled_9d",
          base__doublePerkDisabled: "Skill_base__doublePerkDisabled_00",
          skillIcon: "Skill_skillIcon_26",
          skillName: "Skill_skillName_dd",
          zeroSkill: "Skill_zeroSkill_b3",
        };
        let te, ae;
        (!(function (e) {
          ((e.UnLearned = ""), (e.InProgress = "inProgress"), (e.Learned = "learned"));
        })(te || (te = {})),
          (function (e) {
            ((e.Default = ""),
              (e.Selectable = "selectable"),
              (e.Disable = "disable"),
              (e.DoublePerkDisabled = "doublePerkDisabled"));
          })(ae || (ae = {})));
        const ne = r().memo(function ({
            skillId: e,
            skillIcon: t,
            skillUserName: a,
            isZero: u,
            skillProgress: s,
            progressState: i,
            onClick: l,
            onHover: o,
            onLeave: c,
            skillState: m,
            className: d,
            canBeRelearnedAsZeroSkill: _,
          }) {
            const E = (0, n.useState)(!1),
              g = E[0],
              b = E[1],
              p = i === te.InProgress,
              h = m === ae.Disable,
              A = m === ae.DoublePerkDisabled,
              C = ((e, t, a) => {
                switch (e) {
                  case te.UnLearned:
                    return [t === ae.Selectable || t === ae.DoublePerkDisabled, t !== ae.Disable];
                  case te.InProgress:
                    return [a, t !== ae.Disable];
                  case te.Learned:
                    return [a, a];
                  default:
                    return [!1, !1];
                }
              })(i, m, _),
              f = C[0],
              D = C[1],
              F = v()(
                ee.base,
                ee[`base__${i}`],
                g && ee.base__hover,
                !h && f && ee.base__clickable,
                h && ee.base__disabled,
                A && v()(ee.base__disabled, ee.base__doublePerkDisabled),
                d,
              ),
              B = (0, n.useMemo)(() => ({ height: `${s}%` }), [s]),
              k = (0, n.useMemo)(() => ({ skillName: e, tooltipId: X.HZ }), [e]);
            return r().createElement(
              U.t,
              { targetId: Pe, args: k },
              r().createElement(
                "div",
                {
                  onMouseEnter: D
                    ? () => {
                        (q.$.playHighlight(), b(!0), null == o || o());
                      }
                    : void 0,
                  onMouseLeave: D
                    ? () => {
                        (b(!1), null == c || c());
                      }
                    : void 0,
                  onClick: f
                    ? () => {
                        (q.$.playClick(), l(e));
                      }
                    : void 0,
                  className: F,
                },
                p && r().createElement("div", { style: B, className: ee.progressBar }),
                r().createElement("div", { className: ee.stateBg }),
                h && r().createElement("div", { className: ee.disabledPattern }),
                A && r().createElement("div", { className: ee.doublePerkDisabledPattern }),
                p && r().createElement("div", { className: ee.progressText }, (0, J.T3)(s)),
                r().createElement(Q, { iconName: t, size: Y.c52x52, className: ee.skillIcon }),
                a &&
                  r().createElement(
                    "div",
                    { className: ee.skillName },
                    r().createElement($.ZP, { text: a }),
                  ),
                u && r().createElement("div", { className: ee.zeroSkill }),
              ),
            );
          }),
          re = [
            "isIrrelevant",
            "className",
            "skillId",
            "skillProgress",
            "isInProgress",
            "isLockedByZeroPerks",
            "isSingleHasLearnt",
          ];
        function ue() {
          return (
            (ue =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            ue.apply(this, arguments)
          );
        }
        const se = (0, s.Pi)(function (e) {
            let t = e.isIrrelevant,
              a = e.className,
              u = e.skillId,
              s = e.skillProgress,
              i = e.isInProgress,
              l = e.isLockedByZeroPerks,
              o = e.isSingleHasLearnt,
              c = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, re);
            const m = (0, n.useRef)(!1),
              d = (0, n.useRef)(!1),
              _ = g(),
              E = _.model,
              b = _.controls,
              p = E.isTTCVisible.get(),
              v = ((e, t, a, n, r) => {
                switch (!0) {
                  case t:
                  case n:
                    return ae.Disable;
                  case r:
                    return ae.DoublePerkDisabled;
                  case a:
                    return ae.Default;
                  case e > 0:
                    return ae.Selectable;
                  default:
                    return ae.Default;
                }
              })(E.selectAvailableSkillsCount.get(), t, i, l, o),
              h = ((e, t) => {
                switch (!0) {
                  case 100 === e:
                    return te.Learned;
                  case t:
                    return te.InProgress;
                  default:
                    return te.UnLearned;
                }
              })(s, i),
              A = j(
                () => {
                  m.current && ((d.current = !0), b.hoverSkill(u));
                },
                [u],
                250,
              ),
              C = !t && !l && !c.isZero && E.skillsState.get() === O.ZeroSkills,
              f = (0, n.useCallback)(() => {
                ((m.current = !0), A());
              }, [A]),
              D = (0, n.useCallback)(() => {
                ((m.current = !1), d.current && ((d.current = !1), b.leaveSkill(u)));
              }, [b, u]);
            return r().createElement(
              ne,
              ue({}, c, {
                skillId: u,
                isSingleHasLearnt: o,
                onClick: b.clickSkill,
                onHover: p ? f : void 0,
                onLeave: p ? D : void 0,
                skillState: v,
                progressState: h,
                skillProgress: s,
                className: a,
                canBeRelearnedAsZeroSkill: C,
              }),
            );
          }),
          ie = "SkillsRow_base_1e",
          le = "SkillsRow_skill_df",
          oe = "SkillsRow_emptySkill_b5";
        function ce() {
          return (
            (ce =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            ce.apply(this, arguments)
          );
        }
        const me = ({ skills: e, isIrrelevant: t, className: a, isLockedByZeroPerks: n }) =>
            r().createElement(
              "div",
              { className: v()(ie, a) },
              o.UI(e, (e) =>
                r().createElement(
                  se,
                  ce({ key: e.skillId }, e, {
                    isIrrelevant: t,
                    className: le,
                    isLockedByZeroPerks: n,
                  }),
                ),
              ),
              (0, z.K)(6 - e.length, (e) => r().createElement("div", { className: oe, key: e })),
            ),
          de = "SkillsGroup_base_1e",
          _e = "SkillsGroup_title_5c",
          Ee = "SkillsGroup_qualificationContainer_18",
          ge = "SkillsGroup_alertIcon_77",
          be = "SkillsGroup_qualification_90",
          pe = "SkillsGroup_qualification__locked_57",
          ve = "SkillsGroup_container_04",
          he = "SkillsGroup_rowsContainer_a3",
          Ae = "SkillsGroup_row_ad",
          Ce = "SkillsGroup_roleIcon_b0";
        function fe() {
          return (
            (fe =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            fe.apply(this, arguments)
          );
        }
        const De = ({
            group: e,
            qualificationNumber: t,
            isIrrelevant: a,
            additionalSkills: n,
            className: u,
            isLockedByZeroPerks: s = !1,
          }) =>
            r().createElement(
              "div",
              { className: v()(de, u) },
              r().createElement(
                "div",
                { className: _e },
                s
                  ? r().createElement(
                      "div",
                      { className: Ee },
                      r().createElement("div", { className: ge }),
                      r().createElement(
                        "div",
                        { className: v()(be, pe) },
                        R.strings.crew.matrix.qualification.lockByZeroPerks.$num(t),
                      ),
                    )
                  : r().createElement(
                      "div",
                      { className: be },
                      R.strings.crew.matrix.qualification.$num(t),
                    ),
              ),
              r().createElement(
                "div",
                { className: ve },
                r().createElement(V, fe({}, e, { isIrrelevant: a, className: Ce })),
                r().createElement(
                  "div",
                  { className: he },
                  n &&
                    r().createElement(me, {
                      skills: n,
                      isIrrelevant: a,
                      className: Ae,
                      isLockedByZeroPerks: s,
                    }),
                  r().createElement(
                    me,
                    fe({}, e, { isIrrelevant: a, className: Ae, isLockedByZeroPerks: s }),
                  ),
                ),
              ),
            ),
          Fe = "SkillsGroupsList_base_1d",
          Be = "SkillsGroupsList_base__manyRoles_ba",
          ke = "SkillsGroupsList_scroll_e3",
          we = "SkillsGroupsList_group_ed",
          ye = (0, s.Pi)(() => {
            const e = g().model,
              t = e.computes.relevantSkillsGroups(),
              a = e.computes.irrelevantSkillsGroups(),
              u = (0, P.c4)();
            (0, n.useEffect)(() => {
              u.recalculateContent();
            }, [t, a, u]);
            const s = t.length + a.length >= 2;
            return r().createElement(
              "div",
              { className: v()(Fe, s && Be) },
              r().createElement(
                H.z,
                { className: ke },
                r().createElement(
                  "div",
                  { id: "matrix_skills_list" },
                  o.UI(t, (t, a) =>
                    r().createElement(De, {
                      key: `relevantGroup_${a}`,
                      group: t,
                      qualificationNumber: a + 1,
                      isIrrelevant: !1,
                      className: we,
                      additionalSkills: 0 === a ? e.commonSkills.get() : void 0,
                      isLockedByZeroPerks: e.skillsState.get() === O.ZeroSkills && a > 0,
                    }),
                  ),
                  o.UI(a, (e, a) =>
                    r().createElement(De, {
                      key: `irrelevantGroup_${a}`,
                      group: e,
                      qualificationNumber: t.length + a + 1,
                      isIrrelevant: !0,
                      className: we,
                    }),
                  ),
                ),
              ),
            );
          });
        var Se = a(2056);
        const Ne = {
            base: "SkillsStateInfo_base_de",
            state: "SkillsStateInfo_state_56",
            state__achieve: "SkillsStateInfo_state__achieve_e8",
            state__allSkills: "SkillsStateInfo_state__allSkills_a6",
            state__training: "SkillsStateInfo_state__training_60",
            countContainer: "SkillsStateInfo_countContainer_da",
            count: "SkillsStateInfo_count_87",
            skillIcon: "SkillsStateInfo_skillIcon_e2",
            spinGlow: "SkillsStateInfo_spinGlow_23",
            rotation: "SkillsStateInfo_rotation_58",
          },
          Ie = (0, s.Pi)(({ className: e }) => {
            const t = g().model,
              a = t.selectAvailableSkillsCount.get(),
              n = t.skillsState.get();
            return r().createElement(
              "div",
              { className: v()(Ne.base, e) },
              r().createElement(
                "div",
                { className: v()(Ne.state, Ne[`state__${n}`]) },
                R.strings.crew.matrix.skills.$dyn(n),
              ),
              a > 0 &&
                r().createElement(
                  "div",
                  { className: Ne.countContainer },
                  r().createElement("div", { className: Ne.count }, a),
                  r().createElement(
                    Se.u,
                    {
                      targetId: Pe,
                      contentId: R.views.lobby.crew.tooltips.PerkAvailableTooltip("resId"),
                    },
                    r().createElement(
                      "div",
                      { className: Ne.skillIcon },
                      r().createElement("div", { className: Ne.spinGlow }),
                    ),
                  ),
                ),
            );
          }),
          Te = "SkillsMatrix_base_2a",
          Le = "SkillsMatrix_topContainer_09",
          xe = "SkillsMatrix_skillsStateInfo_2e",
          Re = () =>
            r().createElement(
              "div",
              { className: Te },
              r().createElement(
                "div",
                { className: Le },
                r().createElement(Ie, { className: xe }),
                r().createElement(M, null),
              ),
              r().createElement(ye, null),
            ),
          Me = (0, s.Pi)(({ setTTCVisibility: e }) => {
            const t = (0, u.GS)().mediaSize,
              a = g(),
              s = a.model,
              i = a.controls,
              l = s.computes.isTTCVisible();
            return (
              (0, n.useEffect)(() => {
                (i.setTTCVisible(t >= u.cJ.Small), e && e(l));
              }, [i, l, t, e]),
              r().createElement(b.d, { isLoggingEnabled: !0 }, r().createElement(Re, null))
            );
          }),
          Pe = R.views.lobby.crew.personal_case.PersonalFileView("resId"),
          Oe = r().memo(({ setTTCVisibility: e }) =>
            r().createElement(
              E,
              { options: { rootId: Pe } },
              r().createElement(Me, { setTTCVisibility: e }),
            ),
          );
      },
      894: (e, t, a) => {
        "use strict";
        (a.r(t), a.d(t, { SERVICE_RECORD_RES_ID: () => ee, default: () => te }));
        var n = a(6179),
          r = a.n(n),
          u = a(3403),
          s = a(4022),
          i = a(3215),
          l = a(4598),
          o = a(9480),
          c = a(1612),
          m = a(9174),
          d = a(3946);
        const _ = (0, i.q)()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  {},
                  e.primitives([
                    "rankName",
                    "rankIcon",
                    "battlesCount",
                    "averageXP",
                    "isTankmanInVehicle",
                  ]),
                  { achievementsList: e.array("achievementsList"), isTTCVisible: m.LO.box(!1) },
                ),
                a = (0, d.Om)(() => o.UI(t.achievementsList.get(), l.yR)),
                n = (0, d.Om)(() => t.isTankmanInVehicle.get() && t.isTTCVisible.get(), !0),
                r = (0, d.Om)(() => t.achievementsList.get().length > 0);
              return Object.assign({}, t, {
                computes: { getAchievementsList: a, isTTCVisible: n, hasAchievements: r },
              });
            },
            ({ model: e }) =>
              Object.assign({}, (0, c.h)({ setTTCVisible: (t) => e.isTTCVisible.set(t) })),
          ),
          E = _[0],
          g = _[1];
        var b = a(6483),
          p = a.n(b),
          v = a(5415),
          h = a(3961);
        const A = "AchievementsList_base_90",
          C = "AchievementsList_title_f4",
          f = "AchievementsList_container_a7",
          D = "AchievementsList_item_10",
          F = "AchievementsList_bar_4a";
        var B = a(7078),
          k = a(2603);
        const w = {
          base: "AchievementItem_base_45",
          base__small: "AchievementItem_base__small_b4",
          icon: "AchievementItem_icon_91",
          amountBG: "AchievementItem_amountBG_46",
          amount: "AchievementItem_amount_65",
        };
        let y;
        !(function (e) {
          ((e.Small = "small"), (e.Big = "big"));
        })(y || (y = {}));
        const S = ({ name: e, amount: t, block: a, isRare: n, size: u, className: s }) => {
          const i =
            u === y.Small
              ? R.images.gui.maps.icons.achievement
              : R.images.gui.maps.icons.achievement.big;
          return r().createElement(
            B.t,
            {
              args: { tooltipId: k.Th, name: e, block: a, isRare: n },
              targetId: R.views.lobby.crew.personal_case.ServiceRecordView("resId"),
            },
            r().createElement(
              "div",
              { className: p()(w.base, w[`base__${u}`], s) },
              r().createElement("div", {
                className: w.icon,
                style: { backgroundImage: `url(${i.$dyn(e)})` },
              }),
              t > 1 &&
                r().createElement(
                  "div",
                  { className: w.amountBG },
                  r().createElement("div", { className: w.amount }, t),
                ),
            ),
          );
        };
        function N() {
          return (
            (N =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            N.apply(this, arguments)
          );
        }
        const I = (0, u.Pi)(({ className: e }) => {
          const t = g().model,
            a = (0, v.GS)().mediaSize,
            n = a === v.cJ.Small || a === v.cJ.ExtraSmall ? y.Small : y.Big;
          return r().createElement(
            "div",
            { className: p()(A, e) },
            r().createElement(
              h.z,
              { classNames: { bar: F } },
              r().createElement(
                "div",
                { className: C },
                R.strings.crew.serviceRecord.achievementsList.title(),
              ),
              r().createElement(
                "div",
                { className: f },
                (0, o.UI)(t.computes.getAchievementsList(), (e, t) =>
                  r().createElement(
                    S,
                    N({}, e, { size: n, key: `achievement_${t}`, className: D }),
                  ),
                ),
              ),
            ),
          );
        });
        var T = a(6373);
        const L = "BattlesInfo_base_25",
          x = "BattlesInfo_container_da",
          M = "Item_base_e0",
          P = "Item_icon_81",
          O = "Item_value_28",
          H = "Item_name_35",
          W = ({ name: e, icon: t, value: a }) =>
            r().createElement(
              "div",
              { className: M },
              r().createElement("div", { className: P, style: { backgroundImage: `url(${t})` } }),
              r().createElement("div", { className: O }, a),
              r().createElement("div", { className: H }, e),
            );
        var G = a(3649);
        const V = "RankItem_base_19",
          z = "RankItem_icon_10",
          Z = "RankItem_name_9d",
          j = ({ name: e, icon: t }) =>
            r().createElement(
              T.i,
              {
                header: R.strings.crew.serviceRecord.tooltip.rank.header(),
                body: R.strings.crew.serviceRecord.tooltip.rank.body(),
              },
              r().createElement(
                "div",
                { className: V },
                r().createElement("div", {
                  className: z,
                  style: {
                    backgroundImage: `url(${R.images.gui.maps.icons.tankmen.ranks.big.$dyn((0, G.BN)(t))})`,
                  },
                }),
                r().createElement("div", { className: Z }, e),
              ),
            ),
          $ = (0, u.Pi)(() => {
            const e = g().model;
            return r().createElement(
              "div",
              { className: L },
              r().createElement(
                "div",
                { className: x },
                r().createElement(j, { name: e.rankName.get(), icon: e.rankIcon.get() }),
                r().createElement(
                  T.i,
                  {
                    header: R.strings.tooltips.battlesDetails.header(),
                    body: R.strings.tooltips.battlesDetails.body(),
                  },
                  r().createElement(
                    "div",
                    null,
                    r().createElement(W, {
                      name: R.strings.crew.serviceRecord.battlesCounter(),
                      icon: R.images.gui.maps.icons.crew.serviceRecord.battlesCountIcon(),
                      value: e.battlesCount.get(),
                    }),
                  ),
                ),
                r().createElement(
                  T.i,
                  {
                    header: R.strings.crew.serviceRecord.tooltip.averageXP.header(),
                    body: R.strings.crew.serviceRecord.tooltip.averageXP.body(),
                  },
                  r().createElement(
                    "div",
                    null,
                    r().createElement(W, {
                      name: R.strings.crew.serviceRecord.averageXP(),
                      icon: R.images.gui.maps.icons.crew.serviceRecord.averageXPIcon(),
                      value: e.averageXP.get(),
                    }),
                  ),
                ),
              ),
            );
          }),
          U = "NoAchievements_base_a5",
          X = "NoAchievements_icon_c7",
          q = "NoAchievements_text_34",
          K = ({ className: e }) =>
            r().createElement(
              "div",
              { className: p()(U, e) },
              r().createElement("div", { className: X }),
              r().createElement(
                "div",
                { className: q },
                R.strings.crew.serviceRecord.noAchievements(),
              ),
            ),
          Y = "ServiceRecordApp_achievementsList_fd",
          Q = "ServiceRecordApp_noAchievements_07",
          J = (0, u.Pi)(({ setTTCVisibility: e }) => {
            e(!1);
            const t = g().model.computes.hasAchievements();
            return r().createElement(
              s.d,
              null,
              r().createElement($, null),
              t ? r().createElement(I, { className: Y }) : r().createElement(K, { className: Q }),
            );
          }),
          ee = R.views.lobby.crew.personal_case.ServiceRecordView("resId"),
          te = r().memo(({ setTTCVisibility: e }) =>
            r().createElement(
              E,
              { options: { rootId: ee } },
              r().createElement(J, { setTTCVisibility: e }),
            ),
          );
      },
      3961: (e, t, a) => {
        "use strict";
        a.d(t, { z: () => g });
        var n = a(6483),
          r = a.n(n),
          u = a(794),
          s = a(7701),
          i = a(6179),
          l = a.n(i);
        const o = "ScrollWithLips_base_81",
          c = "ScrollWithLips_fadeTop_3d",
          m = "ScrollWithLips_fadeBottom_44",
          d = "ScrollWithLips_bar_52",
          _ = "ScrollWithLips_content_fb";
        let E;
        !(function (e) {
          ((e.None = "none"), (e.Top = "top"), (e.Both = "both"), (e.Bottom = "bottom"));
        })(E || (E = {}));
        const g = ({ children: e, className: t, classNames: a }) => {
          const n = (0, i.useState)(E.None),
            g = n[0],
            b = n[1],
            p = g === E.Both,
            v = (0, s.c4)();
          return (
            (0, i.useEffect)(() => {
              const e = () => {
                const e = v.getBounds()[1],
                  t = v.animationScroll.scrollPosition.get();
                0 === e
                  ? b(E.None)
                  : t > 1 && t < e - 21
                    ? b(E.Both)
                    : t <= 1
                      ? b(E.Bottom)
                      : t >= e - 21 && b(E.Top);
              };
              return (
                v.events.on("change", e),
                v.events.on("resizeHandled", e),
                v.events.on("recalculateContent", e),
                () => {
                  (v.events.off("change", e),
                    v.events.off("resizeHandled", e),
                    v.events.off("recalculateContent", e));
                }
              );
            }, [v]),
            l().createElement(
              "div",
              { className: r()(o, t) },
              l().createElement(
                u.X.Vertical.Default,
                {
                  api: v,
                  barClassNames: { base: r()(d, null == a ? void 0 : a.bar) },
                  scrollClassNames: { content: _ },
                },
                e,
              ),
              (g === E.Top || p) && l().createElement("div", { className: c }),
              (g === E.Bottom || p) && l().createElement("div", { className: m }),
            )
          );
        };
      },
      4022: (e, t, a) => {
        "use strict";
        a.d(t, { d: () => c });
        var n = a(6179),
          r = a.n(n),
          u = a(3055);
        const s = "TankmanInfoWrapper_base_5a",
          i = "TankmanInfoWrapper_content_b4",
          l = "TankmanInfoWrapper_tankmanInfo_80",
          o = "TankmanInfoWrapper_children_66",
          c = ({ children: e, isLoggingEnabled: t = !1 }) =>
            r().createElement(
              "div",
              { className: s },
              r().createElement(
                "div",
                { className: i },
                r().createElement(u.JW, { className: l, isLoggingEnabled: t }),
                r().createElement("div", { className: o }, e),
              ),
            );
      },
      8727: (e, t, a) => {
        "use strict";
        a.d(t, { O: () => an });
        var n = a(6179),
          r = a.n(n),
          u = a(7727),
          s = a(3403),
          i = a(3215),
          l = a(4598),
          o = a(5175),
          c = a(9480),
          m = a(9174),
          d = a(3946),
          _ = a(4828);
        const E = [
            R.views.lobby.crew.TankmanContainerView("resId"),
            R.views.lobby.crew.personal_case.PersonalFileView("resId"),
            R.views.lobby.crew.personal_case.PersonalDataView("resId"),
            R.views.lobby.crew.personal_case.ServiceRecordView("resId"),
          ],
          g = (0, i.q)()(
            ({ observableModel: e }) => {
              const t = Object.assign(
                  {},
                  e.primitives([
                    "selectedSlotIdx",
                    "isDisabled",
                    "hasDog",
                    "vehicleName",
                    "vehicleType",
                    "currentLayoutID",
                    "previousLayoutID",
                    "isCrewLocked",
                    "nation",
                    "isAcceleratedTraining",
                    "isExtended",
                  ]),
                  {
                    slots: e.array("slots", []),
                    buttonsBar: e.object("buttonsBar"),
                    crewOperations: e.object("buttonsBar.crewOperations"),
                    crewBooks: e.object("buttonsBar.crewBooks"),
                    wotPlus: e.object("buttonsBar.wotPlus"),
                    isWidgetHover: m.LO.box(!1),
                  },
                ),
                a = (0, d.Om)(() => (0, o.c)(t.slots.get()), { equals: l.jv }),
                n = (0, d.Om)(() => Boolean(c.sE(a(), (e) => -1 === e.tankman.tankmanID))),
                r = (0, d.Om)(() => 1 === t.slots.get().length),
                u = (0, d.Om)((e) => t.selectedSlotIdx.get() === e),
                s = (0, d.Om)(() => -1 !== t.selectedSlotIdx.get()),
                i = (0, d.Om)((e) => {
                  var t;
                  return null == (t = c.U2(a(), e)) ? void 0 : t.tankman;
                }),
                g = (0, d.Om)((e) => {
                  var t;
                  const n = null == (t = c.U2(a(), e)) ? void 0 : t.tankman;
                  return n ? n.skills.length + n.newSkillsAmount + n.possibleSkillsAmount : 0;
                }),
                b = (0, d.Om)(() => {
                  return (
                    (e = t.currentLayoutID.get()),
                    (a = t.previousLayoutID.get()),
                    {
                      isCurrentLayoutHangar: e === R.views.lobby.crew.HangarCrewWidget("resId"),
                      isCurrentLayoutTankmanContainer: E.includes(e),
                      isCurrentLayoutQuickTraining:
                        e === R.views.lobby.crew.QuickTrainingView("resId"),
                      isCurrentLayoutMemberChange:
                        e === R.views.lobby.crew.MemberChangeView("resId"),
                      isPreviousLayoutHangar: a === R.views.lobby.crew.HangarCrewWidget("resId"),
                      isPreviousLayoutTankmanContainer: E.includes(a),
                      isPreviousLayoutQuickTraining:
                        a === R.views.lobby.crew.QuickTrainingView("resId"),
                      isPreviousLayoutMemberChange:
                        a === R.views.lobby.crew.MemberChangeView("resId"),
                      isPreviousLayoutBarrack: a === R.views.lobby.crew.BarracksView("resId"),
                    }
                  );
                  var e, a;
                }),
                p = (0, d.Om)(() => {
                  const e = b(),
                    t = e.isCurrentLayoutHangar,
                    a = e.isCurrentLayoutQuickTraining;
                  return !r() && !t && !a;
                }),
                v = (0, d.Om)(() => !r() && t.buttonsBar.get().isVisible),
                h = (0, d.Om)(() => {
                  return ((e = t.currentLayoutID.get()), _.AB[e] || _.sC.Hangar);
                  var e;
                });
              return Object.assign({}, t, {
                computes: {
                  getSlots: a,
                  isSlotSelected: u,
                  isAnySlotSelected: s,
                  getSlotTankman: i,
                  getAllSkillsAmount: g,
                  isAnyEmptySlots: n,
                  isTankmanMode: r,
                  isChangeCrewButtonVisible: p,
                  isButtonBarVisible: v,
                  getLayoutInfo: b,
                  getUiLoggingParentScreen: h,
                },
              });
            },
            ({ externalModel: e, model: t }) => ({
              onSlotClick: e.createCallback(
                (e, t) => ({ slotIdx: e, tankmanID: t }),
                "onSlotClick",
              ),
              onChangeCrewClick: e.createCallback(
                (e, t) => ({ slotIdx: e, tankmanID: t }),
                "onChangeCrewClick",
              ),
              onCrewBooksClick: e.createCallbackNoArgs("buttonsBar.onCrewBooksClick"),
              onWotPlusClick: e.createCallbackNoArgs("buttonsBar.onWotPlusClick"),
              onDogClick: e.createCallbackNoArgs("onDogClick"),
              onDogMoreInfoClick: e.createCallbackNoArgs("onDogMoreInfoClick"),
              setIsWidgetHover: (0, m.aD)((e) => t.isWidgetHover.set(e)),
            }),
          ),
          b = g[0],
          p = g[1];
        var v = a(6483),
          h = a.n(v),
          A = a(7613),
          C = a(6373),
          f = a(2056);
        let D;
        !(function (e) {
          ((e.On = "on"), (e.Off = "off"), (e.Disabled = "disabled"), (e.Hidden = "hidden"));
        })(D || (D = {}));
        const F = "ButtonsBar_base_9c",
          B = "ButtonsBar_button_d1",
          k = "ButtonsBar_button__crewOperaions_70",
          w = "ButtonsBar_button__crewBooks_b4",
          y = "ButtonsBar_button__toggle_64",
          S = "ButtonsBar_acceleratedTrainingContainer_ee",
          N = "ButtonsBar_acceleratedTrainingContainer__visible_79",
          I = "ButtonsBar_acceleratedTraining_94",
          T = "ButtonsBar_acceleratedTraining__icon_9b",
          L = "ButtonsBar_acceleratedTraining__label_ad";
        var x = a(3457),
          M = a(9987),
          P = a(3649);
        const O = "CrewBookButton_base_da",
          H = "CrewBookButton_button_ee",
          W = "CrewBookButton_icon_11",
          G = "CrewBookButton_discount_6b",
          V = "CrewBookButton_counter_5d",
          z = (0, s.Pi)(({ classMix: e, isWidgetDisabled: t }) => {
            const a = p(),
              n = a.model,
              u = a.controls,
              s = n.crewBooks.get(),
              i = u.onCrewBooksClick;
            return r().createElement(
              C.i,
              {
                header: R.strings.crew_widget.tooltip.buttonsBar.crewBooks.header(),
                body: (0, P.uF)(R.strings.crew_widget.tooltip.buttonsBar.crewBooks.body(), {
                  count: s.totalAmount,
                }),
              },
              r().createElement(
                "div",
                { id: "crew_book_button", className: h()(O, e) },
                r().createElement(
                  x.u5,
                  { type: x.L$.primary, mixClass: H, disabled: s.isDisabled || t, onClick: i },
                  r().createElement("div", { className: W }),
                ),
                s.newAmount > 0 &&
                  r().createElement(
                    "div",
                    { className: V },
                    r().createElement(M.A, { value: s.newAmount }),
                  ),
                s.hasDiscount && r().createElement("div", { className: G }),
              ),
            );
          });
        var Z = a(3616);
        const j = ["children"];
        function $() {
          return (
            ($ =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            $.apply(this, arguments)
          );
        }
        const U = (e) => {
          let t = e.children,
            a = (function (e, t) {
              if (null == e) return {};
              var a,
                n,
                r = {},
                u = Object.keys(e);
              for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
              return r;
            })(e, j);
          return r().createElement(
            Z.Z,
            $(
              {
                decoratorId:
                  R.views.common.pop_over_window.backport_pop_over.BackportPopOverWindow("resId"),
                contentId:
                  R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent("resId"),
              },
              a,
            ),
            t,
          );
        };
        var X = a(4489);
        let q;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(q || (q = {}));
        var K = a(1943);
        const Y = "CrewOperationsButton_base_e3",
          Q = "CrewOperationsButton_button_8e",
          J = "CrewOperationsButton_icon_0c",
          ee = "CrewOperationsButton_autoReturnIcon_f0",
          te = (0, s.Pi)(({ classMix: e, isWidgetDisabled: t }) => {
            const a = p().model,
              n = ((e) => {
                const t = (0, K.Jp)(_.D9);
                return (a) => t({ action: _.eX.Click, parentScreen: e, item: a });
              })(a.computes.getUiLoggingParentScreen()),
              u = a.crewOperations.get();
            return r().createElement(
              "div",
              { id: "crew_operations_button", className: h()(Y, e) },
              r().createElement(
                U,
                {
                  targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  isEnabled: !t,
                  onClick: () => n(_.x3.CrewOperationsButton),
                },
                r().createElement(
                  C.i,
                  {
                    header: R.strings.crew_widget.tooltip.buttonsBar.crewOperations.header(),
                    body: R.strings.crew_widget.tooltip.buttonsBar.crewOperations.body(),
                  },
                  r().createElement(
                    "div",
                    null,
                    r().createElement(
                      x.u5,
                      { type: x.L$.primary, mixClass: Q, disabled: t },
                      r().createElement("div", { className: J }),
                    ),
                    u.isAutoReturnOn && r().createElement("div", { className: ee }),
                  ),
                ),
              ),
            );
          });
        var ae = a(9631);
        const ne = "CrewToggleButton_base_03",
          re = "CrewToggleButton_button_89",
          ue = "CrewToggleButton_iconContainer_f9",
          se = "CrewToggleButton_icon_a7";
        let ie;
        !(function (e) {
          e.WotPlus = "wotPlus";
        })(ie || (ie = {}));
        const le = (0, n.memo)(({ type: e, state: t, isDisabled: a, onClick: u, classMix: s }) => {
            const i = (0, n.useMemo)(() => {
              const a = t === D.Disabled ? D.Off : t;
              return {
                backgroundImage: `url(R.images.gui.maps.icons.crewWidget.buttonsBar.icons.${e}_${a})`,
              };
            }, [e, t]);
            return r().createElement(
              "div",
              { className: h()(ne, s) },
              r().createElement(
                ae.C,
                {
                  type: x.L$.primary,
                  isActive: t === D.On,
                  disabled: a || t === D.Disabled,
                  className: re,
                  onClick: u,
                },
                r().createElement(
                  "div",
                  { className: ue },
                  r().createElement("div", { className: se, style: i }),
                ),
              ),
            );
          }),
          oe = R.strings.crew.acceleratedTraining,
          ce = (0, s.Pi)(({ isWidgetDisabled: e, isCurrentLayoutHangar: t }) => {
            const a = p(),
              n = a.model,
              u = a.controls,
              s = n.isWidgetHover.get(),
              i = n.isAcceleratedTraining.get(),
              l = n.wotPlus.get(),
              o = u.onWotPlusClick;
            return r().createElement(
              "div",
              { className: F },
              r().createElement(te, { classMix: h()(B, k), isWidgetDisabled: e }),
              r().createElement(z, { classMix: h()(B, w), isWidgetDisabled: e }),
              l.state !== D.Hidden &&
                r().createElement(
                  f.u,
                  {
                    contentId: R.views.lobby.crew.CrewHeaderTooltipView("resId"),
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  },
                  r().createElement(
                    "div",
                    null,
                    r().createElement(le, {
                      type: ie.WotPlus,
                      state: l.state,
                      isDisabled: e || l.isDisabled,
                      onClick: o,
                      classMix: h()(B, y),
                    }),
                  ),
                ),
              r().createElement(
                "div",
                { className: h()(S, (!t || s) && N) },
                i &&
                  r().createElement(
                    C.i,
                    { header: oe.tooltip.header(), body: oe.tooltip.body() },
                    r().createElement(
                      "div",
                      { className: I },
                      r().createElement("div", { className: T }),
                      r().createElement(A.ZP, { className: L, text: oe.label() }),
                    ),
                  ),
              ),
            );
          }),
          me = "CrewWidgetApp_base_cc",
          de = "CrewWidgetApp_buttonsBar_e5",
          _e = "CrewWidgetApp_slotsList_ee";
        var Ee = a(7030),
          ge = a(8018),
          be = a(7160);
        const pe = {
            base: "BaseSlot_base_97",
            base__inactive: "BaseSlot_base__inactive_7e",
            background: "BaseSlot_background_ef",
            background__hovered: "BaseSlot_background__hovered_ee",
            background__inactive: "BaseSlot_background__inactive_6b",
            base__widgetHovered: "BaseSlot_base__widgetHovered_48",
            hoverGlow: "BaseSlot_hoverGlow_de",
            hoverGlow__visible: "BaseSlot_hoverGlow__visible_f4",
            selectedGlow: "BaseSlot_selectedGlow_25",
            selectedGlow__visible: "BaseSlot_selectedGlow__visible_2f",
            hover: "BaseSlot_hover_e9",
            hover__visible: "BaseSlot_hover__visible_1f",
            disabled: "BaseSlot_disabled_67",
          },
          ve = (0, n.memo)(
            ({
              onClick: e,
              children: t,
              isSelected: a = !1,
              isDisabled: s,
              isEnabledForMouse: i,
              isEmpty: l = !1,
              isWidgetHovered: o = !0,
              layoutInfo: c,
            }) => {
              const m = (0, n.useState)(!1),
                d = m[0],
                _ = m[1],
                E = d && (!a || (!l && c.isCurrentLayoutMemberChange)),
                g = E && !l && !c.isCurrentLayoutHangar;
              return r().createElement(
                "div",
                {
                  className: h()(
                    pe.base,
                    (d || a) && !c.isCurrentLayoutHangar && pe.base__hovered,
                    (a || !i) && pe.base__inactive,
                    c.isCurrentLayoutHangar && o && pe.base__widgetHovered,
                  ),
                  onClick: e,
                  onMouseEnter: () => {
                    i && !a && (u.$.playHighlight(), _(!0));
                  },
                  onMouseLeave: () => {
                    _(!1);
                  },
                },
                r().createElement("div", { className: pe.background }),
                !c.isCurrentLayoutMemberChange &&
                  r().createElement("div", {
                    className: h()(pe.selectedGlow, a && pe.selectedGlow__visible),
                  }),
                r().createElement("div", {
                  className: h()(pe.hoverGlow, g && pe.hoverGlow__visible),
                }),
                r().createElement("div", { className: h()(pe.hover, E && pe.hover__visible) }),
                s && r().createElement("div", { className: pe.disabled }),
                t,
              );
            },
          ),
          he = ({
            startState: e,
            endState: t,
            layoutInfo: a,
            isPaused: u,
            children: s,
            className: i,
            isTankmanMode: l,
          }) => {
            const o = (0, Ee.useSpring)(
                () => ({ from: e, to: t, config: { duration: 300, easing: be.qb }, pause: u }),
                [u],
              )[0],
              c = (0, n.useMemo)(
                () =>
                  a.isCurrentLayoutHangar || a.isCurrentLayoutQuickTraining || l
                    ? e
                    : (!a.isPreviousLayoutHangar && !a.isPreviousLayoutBarrack) || u
                      ? t
                      : o,
                [a, u, o, e, t, l],
              );
            return r().createElement(Ee.animated.div, { className: i, style: c }, s);
          },
          Ae = "DogSlot_base_8f",
          Ce = "DogSlot_icon_ba",
          fe = "DogSlot_container_63",
          De = "DogSlot_roleAndName_c9",
          Fe = "DogSlot_role_5c",
          Be = "DogSlot_name_9c",
          ke = "DogSlot_name__hidden_56",
          we = "DogSlot_btnDetails_b7",
          ye = "DogSlot_btnDetails__hidden_44",
          Se = "DogSlot_infoIcon_09",
          Ne = "DogSlot_infoIcon__hidden_8e",
          Ie = { transform: "translateX(0rem)" },
          Te = (0, s.Pi)(({ isDisabled: e, layoutInfo: t }) => {
            const a = p(),
              s = a.model,
              i = a.controls,
              l = s.nation.get(),
              o = s.isWidgetHover.get(),
              c = i.onDogMoreInfoClick,
              m = (0, n.useCallback)(() => {
                !e && (0, u.G)(ge.gO.RUDY);
              }, [e]),
              d = (0, n.useCallback)(
                (t) => {
                  (t.stopPropagation(), !e && c());
                },
                [c, e],
              ),
              _ = (0, Ee.useSpring)(
                () => ({
                  from: Ie,
                  to: { transform: "translateX(16rem)" },
                  config: { duration: 300, easing: be.qb },
                  pause: !t.isCurrentLayoutQuickTraining,
                }),
                [t],
              )[0],
              E = R.strings.tooltips.hangar.crew.rudy.dog.$dyn(l);
            return r().createElement(
              C.i,
              { header: E.header(), body: E.body() },
              r().createElement(
                "div",
                null,
                r().createElement(
                  ve,
                  {
                    onClick: m,
                    isDisabled: e,
                    isEnabledForMouse: !1,
                    layoutInfo: t,
                    isWidgetHovered: o,
                  },
                  r().createElement(
                    he,
                    {
                      startState: Ie,
                      endState: { transform: "translateX(42rem)" },
                      layoutInfo: t,
                      isPaused: !1,
                      className: Ae,
                      isTankmanMode: !1,
                    },
                    r().createElement(Ee.animated.div, { className: Ce, style: _ }),
                    r().createElement(
                      "div",
                      { className: fe },
                      r().createElement(
                        "div",
                        { className: De },
                        r().createElement("div", { className: Fe }),
                        r().createElement(A.ZP, {
                          className: h()(Be, t.isCurrentLayoutHangar && !o && ke),
                          text: R.strings.menu.hangar.crew.rody.dog.$dyn(l).name(),
                        }),
                      ),
                      r().createElement(
                        "div",
                        { className: h()(we, t.isCurrentLayoutHangar && !o && ye) },
                        r().createElement(
                          x.u5,
                          { onClick: d },
                          r().createElement(A.ZP, { text: R.strings.crew_widget.btnDetails() }),
                        ),
                      ),
                      r().createElement("div", {
                        className: h()(Se, (!t.isCurrentLayoutHangar || o) && Ne),
                      }),
                    ),
                  ),
                ),
              ),
            );
          });
        var Le = a(4179);
        const xe = ({
            children: e,
            contentID: t,
            decoratorID: a = 0,
            targetId: r = 0,
            args: s,
            isEnabled: i = !0,
            onMouseDown: l,
          }) => {
            const o = (0, n.useCallback)(() => {
                ((0, Le.c9)(Le.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: a,
                  targetID: r,
                  isMouseEvent: !0,
                  on: !0,
                  args: s,
                }),
                  u.$.playYes());
              }, [s, t, a, r]),
              c = (0, n.useCallback)(() => {
                (0, Le.c9)(Le.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: a,
                  targetID: r,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, a, r]),
              m = (0, n.useCallback)(
                (e) => {
                  (l && l(e), ((e) => e.button === q.RIGHT)(e) && o());
                },
                [l, o],
              );
            return (
              (0, n.useEffect)(() => {
                !1 === i && c();
              }, [i, c]),
              i ? (0, n.cloneElement)(e, { onMouseDown: m }) : e
            );
          },
          Re = ["children"];
        function Me() {
          return (
            (Me =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Me.apply(this, arguments)
          );
        }
        const Pe = (e) => {
            let t = e.children,
              a = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Re);
            return r().createElement(
              xe,
              Me({}, a, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          Oe = "ChangeCrewButton_base_0f",
          He = "ChangeCrewButton_base__inactive_77",
          We = "ChangeCrewButton_normalState_07",
          Ge = "ChangeCrewButton_normalState__hide_db",
          Ve = "ChangeCrewButton_hoverState_68",
          ze = "ChangeCrewButton_hoverState__show_89",
          Ze = (0, s.Pi)(({ isSelected: e, isLocked: t, mainRole: a, isFemale: s }) => {
            const i = p().model,
              l = (0, n.useState)(!1),
              o = l[0],
              c = l[1],
              m = (0, K.Sr)(_.D9, {
                item: _.x3.ChangeButtonTooltip,
                action: _.eX.Viewed,
                parentScreen: i.computes.getUiLoggingParentScreen(),
              }),
              d = (0, n.useMemo)(
                () =>
                  t
                    ? [
                        R.strings.crew_widget.tooltip.changeCrewButton.unavailable.header(),
                        R.strings.crew_widget.tooltip.changeCrewButton.unavailable.body(),
                      ]
                    : [
                        "",
                        (0, P.uF)(R.strings.crew_widget.changeTankman(), {
                          role: (0, ge.Gc)(a, s, ge.wP.Objective),
                        }),
                      ],
                [t, s, a],
              ),
              E = d[0],
              g = d[1];
            return r().createElement(
              C.i,
              {
                header: E,
                body: g,
                targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                ignoreMouseClick: !0,
              },
              r().createElement(
                "div",
                {
                  className: h()(Oe, (t || e) && He),
                  onMouseEnter: () => {
                    (m.onShow(), t || e || (u.$.playHighlight(), c(!0)));
                  },
                  onMouseLeave: () => {
                    (m.onHide(), c(!1));
                  },
                },
                r().createElement("div", { className: h()(We, o && Ge) }),
                r().createElement("div", { className: h()(Ve, (e || o) && ze) }),
              ),
            );
          }),
          je = "CrewSlot_base_ac",
          $e = "CrewSlot_changeCrew_02",
          Ue = "CrewSlot_content_5b",
          Xe = "CrewSlot_content__withChangeCrewButton_4e",
          qe = "CrewSlot_warningHighlight_ff",
          Ke = "CrewSlot_selectHighlight_50",
          Ye = "CrewSlot_selectHighlightInTankmanMode_37";
        var Qe = a(7077);
        const Je = "AcceleratedTrainingIcon_base_4f",
          et = "AcceleratedTrainingIcon_icon_45",
          tt = (0, n.memo)(({ classMix: e }) =>
            r().createElement(
              C.i,
              {
                header: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.header(),
                body: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.body(),
              },
              r().createElement(
                "div",
                { className: h()(Je, e) },
                r().createElement("div", { className: et }),
              ),
            ),
          ),
          at = "SpecializationAndName_base_ef",
          nt = "SpecializationAndName_roleWrapper_87",
          rt = "SpecializationAndName_secondaryRolesWrapper_d0",
          ut = "SpecializationAndName_secondaryRolesWrapper__hidden_ac",
          st = "SpecializationAndName_role_55",
          it = "SpecializationAndName_role__withGap_35",
          lt = "SpecializationAndName_percent_e6",
          ot = "SpecializationAndName_percent__untrained_1b",
          ct = "SpecializationAndName_percent__wrapped_9b",
          mt = "SpecializationAndName_acceleratedTrainingIcon_35",
          dt = "SpecializationAndName_name_aa",
          _t = "SpecializationAndName_name__hidden_20";
        function Et() {
          return (
            (Et =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Et.apply(this, arguments)
          );
        }
        const gt = (0, s.Pi)(
            ({
              roles: e,
              specializationLevel: t = 0,
              tankmanID: a,
              isUntrained: n,
              name: u,
              isCurrentLayoutHangar: s,
              isAcceleratedTrainingAvailable: i,
            }) => {
              const l = p().model,
                o = (0, K.Sr)(_.D9, {
                  item: _.x3.MstlTooltip,
                  action: _.eX.Viewed,
                  parentScreen: l.computes.getUiLoggingParentScreen(),
                }),
                c = e[0],
                m = e.slice(1),
                d = l.isWidgetHover.get();
              return r().createElement(
                "div",
                { className: at },
                r().createElement(
                  f.u,
                  Et(
                    {
                      targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                      contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                      args: { tankmanID: a },
                      isEnabled: Boolean(a),
                      ignoreMouseClick: !0,
                    },
                    o,
                  ),
                  r().createElement(
                    "div",
                    { className: nt },
                    r().createElement("div", {
                      key: `role__${c}`,
                      className: st,
                      style: {
                        backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(c)})`,
                      },
                    }),
                    r().createElement(
                      "div",
                      { className: h()(rt, s && !d && ut) },
                      m.map((e) =>
                        r().createElement("div", {
                          key: `role__${e}`,
                          className: h()(st, it),
                          style: {
                            backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(e)})`,
                          },
                        }),
                      ),
                    ),
                    t > 0 &&
                      r().createElement(A.ZP, {
                        className: h()(lt, n && ot, s && !d && ct),
                        style: { "--marginLeft": -23 * (e.length - 1) + 4 + "rem" },
                        text: (0, P.uF)(R.strings.common.percentValue(), { value: t }),
                      }),
                  ),
                ),
                i && r().createElement(tt, { classMix: mt }),
                r().createElement(A.ZP, { className: h()(dt, s && !d && _t), text: u || "" }),
              );
            },
          ),
          bt = "EmptySlotContent_base_77",
          pt = "EmptySlotContent_tankmanIcon_07",
          vt = "EmptySlotContent_icon_a8",
          ht = "EmptySlotContent_specialization_1f",
          At = "EmptySlotContent_specialization__disabled_3d",
          Ct = "EmptySlotContent_vehicle_55",
          ft = { transform: "translateX(0rem)", opacity: 1 },
          Dt = { transform: "translateX(-70rem)", opacity: 0 },
          Ft = (0, n.memo)(
            ({
              roles: e,
              layoutInfo: t,
              vehicleName: a,
              vehicleType: n,
              isDisabled: u,
              isSelected: s,
              blinkStyle: i,
              qtTankmanIconStyle: l,
            }) => {
              const o = (0, Ee.useSpring)(
                  () => ({
                    from: ft,
                    to: Dt,
                    config: { duration: 200, easing: be.ei },
                    immediate: !0,
                    pause: s,
                  }),
                  [s],
                ),
                m = o[0],
                d = o[1],
                _ = () => {
                  t.isCurrentLayoutQuickTraining || d.start({ reset: !0, reverse: !0 });
                },
                E = c.U2(e, 0) || "",
                g = R.strings.crew_widget.vehicleWithName.$dyn((0, P.BN)(n)),
                b = (0, P.uF)(R.strings.crew_widget.emptySlot.chooseTankman(), {
                  role: R.strings.item_types.tankman.roles.objectiveCase.$dyn(E),
                });
              return r().createElement(
                "div",
                { className: bt, onMouseEnter: _, onMouseLeave: _ },
                r().createElement(
                  "div",
                  { className: pt },
                  r().createElement(
                    Ee.animated.div,
                    { style: l },
                    r().createElement(Qe.G, {
                      name: "empty",
                      size: Qe.U.c100x60Barracks,
                      className: vt,
                    }),
                    r().createElement(
                      Ee.animated.div,
                      { style: u ? void 0 : i },
                      r().createElement(Qe.G, {
                        name: "emptyRed",
                        size: Qe.U.c100x60Barracks,
                        className: vt,
                      }),
                    ),
                  ),
                ),
                r().createElement(
                  "div",
                  { className: h()(ht, u && At) },
                  r().createElement(gt, {
                    tankmanID: 0,
                    roles: e,
                    name: b,
                    isUntrained: !0,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                  }),
                ),
                r().createElement(
                  Ee.animated.div,
                  { className: Ct, style: s ? void 0 : m },
                  (0, P.uF)(g, { name: a }),
                ),
              );
            },
          );
        var Bt = a(7078),
          kt = a(2603),
          wt = a(5415);
        const yt = (e) => e.skills.length + e.newSkillsAmount + e.possibleSkillsAmount;
        var St = a(8271),
          Nt = a(4385);
        const It = {
            base: "RoleLevelIcon_base_e1",
            realLevel: "RoleLevelIcon_realLevel_96",
            base__small: "RoleLevelIcon_base__small_ce",
            icon: "RoleLevelIcon_icon_fa",
          },
          Tt = (0, n.memo)(({ percentValue: e, skillSize: t, hasSkills: a }) => {
            const n = a ? R.strings.crew_widget.plusValue() : R.strings.crew_widget.plusSpecValue();
            return r().createElement(
              C.i,
              {
                header: R.strings.crew_widget.tooltip.roleLevelIcon.header(),
                body: R.strings.crew_widget.tooltip.roleLevelIcon.body(),
              },
              r().createElement(
                "div",
                { className: h()(It.base, It[`base__${t}`]) },
                r().createElement("div", { className: It.icon }),
                r().createElement(
                  "div",
                  { className: It.realLevel },
                  r().createElement(A.ZP, {
                    text: n,
                    format: { binding: { value: r().createElement(A.ZP, { text: e }) } },
                  }),
                ),
              ),
            );
          }),
          Lt = {
            base: "LastSkillInfo_base_38",
            realLevel: "LastSkillInfo_realLevel_78",
            base__small: "LastSkillInfo_base__small_c5",
            possibleLevel: "LastSkillInfo_possibleLevel_02",
            acceleratedTrainingIcon: "LastSkillInfo_acceleratedTrainingIcon_bf",
            base__big: "LastSkillInfo_base__big_10",
          },
          xt = 0.01,
          Rt = (0, n.memo)(
            ({
              lastSkillLevel: e,
              lastPossibleSkillLevel: t,
              showAcceleratedTrainingIcon: a,
              skillSize: u,
              blinkStyle: s,
            }) => {
              const i = (0, n.useRef)(e),
                l = (0, Ee.useSpring)(() => ({ from: { scale: 1 } })),
                o = l[0],
                c = l[1];
              (0, n.useEffect)(() => {
                t < 0 &&
                  i.current !== e &&
                  (c.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: be.Fs },
                  }),
                  (i.current = e));
              }, [e, t, c]);
              const m = (0, n.useMemo)(
                  () =>
                    0 === t
                      ? [R.strings.common.percentValue(), t]
                      : t < xt
                        ? [R.strings.crew_widget.plusMinValue(), xt]
                        : [R.strings.crew_widget.plusValue(), t],
                  [t],
                ),
                d = m[0],
                _ = m[1];
              return r().createElement(
                "div",
                { className: h()(Lt.base, Lt[`base__${u}`]) },
                e >= 0 &&
                  e < 100 &&
                  r().createElement(
                    Ee.animated.div,
                    { style: o },
                    r().createElement(
                      "div",
                      { className: Lt.realLevel },
                      (0, P.uF)(R.strings.common.percentValue(), {
                        value: e > 0 && e < xt ? xt : e,
                      }),
                    ),
                  ),
                t >= 0 &&
                  t < 100 &&
                  r().createElement(
                    Ee.animated.div,
                    { className: Lt.possibleLevel, style: s },
                    (0, P.uF)(d, { value: _ }),
                  ),
                a && r().createElement(tt, { classMix: Lt.acceleratedTrainingIcon }),
              );
            },
          );
        var Mt = a(8485);
        const Pt = 33,
          Ot = 0,
          Ht = !0,
          Wt = "play";
        const Gt = [
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
        function Vt() {
          return (
            (Vt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Vt.apply(this, arguments)
          );
        }
        const zt = (0, n.memo)(function (e) {
            let t = e.width,
              a = e.height,
              u = e.getImageSource,
              s = e.frameCount,
              i = e.onAnimate,
              l = e.frameTime,
              o = void 0 === l ? Pt : l,
              c = e.initialFrameIndex,
              m = void 0 === c ? Ot : c,
              d = e.lastFrameIndex,
              _ = void 0 === d ? s - 1 : d,
              E = e.loop,
              g = void 0 === E ? Ht : E,
              b = e.state,
              p = void 0 === b ? Wt : b,
              v = e.onAnimationDone,
              h = e.onAnimationComplete,
              A = e.poster,
              C = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, Gt);
            const f = (0, n.useRef)(null);
            return (
              (0, n.useEffect)(() => {
                const e = f.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  a = (a) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(a.img, -a.x, -a.y));
                  };
                switch (p) {
                  case "play":
                    return (function () {
                      const e = $t(m, _, u),
                        t = Zt(m, _),
                        n = window.setInterval(() => {
                          const r = t(),
                            u = e.get(r);
                          u
                            ? (null == i || i(r, u),
                              a(u),
                              r === _ &&
                                (null == h || h(),
                                g || (null == v || v(), window.clearInterval(n))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, o);
                      return () => window.clearInterval(n);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === m && A ? { path: A, x: 0, y: 0 } : u(m),
                        t = new Image();
                      t.src = e.path;
                      const n = () => a(jt(e, t));
                      return (
                        t.addEventListener("load", n),
                        () => t.removeEventListener("load", n)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [o, u, m, _, g, i, h, v, A, p]),
              r().createElement("canvas", Vt({}, C, { width: t, height: a, ref: f }))
            );
          }),
          Zt = (e, t) => {
            let a = e;
            return () => {
              const n = a;
              return ((a += 1), a > t && (a = e), n);
            };
          },
          jt = (e, t) => Object.assign({}, e, { img: t }),
          $t = (e, t, a) => {
            const n = new Map(),
              r = {};
            for (let u = e; u <= t; u++) {
              const e = a(u),
                t = r[e.path];
              if (t) n.set(u, jt(e, t));
              else {
                const t = new Image();
                ((r[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${u})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  n.set(u, jt(e, t)));
              }
            }
            return n;
          };
        const Ut = [
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
        let qt;
        !(function (e) {
          ((e.Play = "play"), (e.Stop = "stop"));
        })(qt || (qt = {}));
        const Kt = (e, t, a) => {
            const n = new Image();
            ((n.src = a(t)), e.push(n));
          },
          Yt =
            ((0, n.memo)((e) => {
              let t = e.width,
                a = e.height,
                u = e.getSrcByFrame,
                s = e.frameCount,
                i = e.onAnimate,
                l = void 0 === i ? () => {} : i,
                o = e.frameTime,
                c = void 0 === o ? 33 : o,
                m = e.initialFrameIndex,
                d = void 0 === m ? 0 : m,
                _ = e.loop,
                E = void 0 === _ || _,
                g = e.state,
                b = void 0 === g ? qt.Play : g,
                p = e.onAnimationComplete,
                v = void 0 === p ? () => {} : p,
                h = e.revers,
                A = void 0 !== h && h,
                C = (function (e, t) {
                  if (null == e) return {};
                  var a,
                    n,
                    r = {},
                    u = Object.keys(e);
                  for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                  return r;
                })(e, Ut);
              const f = (0, n.useRef)(null);
              return (
                (0, n.useEffect)(() => {
                  const e = f.current;
                  if (!e) return;
                  const n = s - 1,
                    r = e.getContext("2d"),
                    i = (n) => {
                      (r.clearRect(0, 0, e.width, e.height), r.drawImage(n, 0, 0, t, a));
                    };
                  if ("stop" === b) {
                    const e = u(0),
                      t = new Image();
                    t.src = e;
                    const a = () => i(t);
                    return (t.addEventListener("load", a), () => t.removeEventListener("load", a));
                  }
                  const o = ((e, t, a) => {
                      const n = [];
                      if (a) for (let a = e; a >= 0; a--) Kt(n, a, t);
                      else for (let a = 0; a < e; a++) Kt(n, a, t);
                      return n;
                    })(s, u, A),
                    m = ((e, t = 0) => {
                      let a = t;
                      return () => {
                        const t = a;
                        return ((a += 1), a > e && (a = 0), t);
                      };
                    })(n, d),
                    _ = setInterval(() => {
                      const e = m(),
                        t = o[e];
                      (i(o[e]), l(e, t), e === n && (v(), E || clearInterval(_)));
                    }, c);
                  return () => clearInterval(_);
                }, [s, c, u, a, d, E, l, v, b, t, A]),
                r().createElement("canvas", Xt({}, C, { width: t, height: a, ref: f }))
              );
            }),
            "AnimatedNewSkill_base_6b"),
          Qt = "AnimatedNewSkill_base__big_31";
        function Jt(e, t) {
          var a = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (a) return (a = a.call(e)).next.bind(a);
          if (
            Array.isArray(e) ||
            (a = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return ea(e, t);
              var a = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === a && e.constructor && (a = e.constructor.name);
              if ("Map" === a || "Set" === a) return Array.from(e);
              if ("Arguments" === a || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))
                return ea(e, t);
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
        function ea(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var a = 0, n = new Array(t); a < t; a++) n[a] = e[a];
          return n;
        }
        class ta {
          constructor() {
            ((this._intervalID = void 0),
              (this._observers = void 0),
              (this._intervalID = null),
              (this._observers = new Map()));
          }
          static get instance() {
            return (ta._instance || (ta._instance = new ta()), ta._instance);
          }
          subscribe(e) {
            (this._observers.set(e, e),
              1 === this._observers.size &&
                (this._intervalID = window.setInterval(() => {
                  for (var e, t = Jt(this._observers.values()); !(e = t()).done;) {
                    (0, e.value)();
                  }
                }, 5e3)));
          }
          unsubscribe(e) {
            (this._observers.delete(e),
              0 === this._observers.size &&
                null !== this._intervalID &&
                (clearInterval(this._intervalID), (this._intervalID = null)));
          }
        }
        ta._instance = void 0;
        const aa = {
          width: 24,
          height: 24,
          frameCount: 42,
          chunk: { count: 1, columns: 42, rows: 1 },
          getChunkPath:
            ((na = "R.images.gui.maps.icons.sequence.new_skill.skill_"), (e) => `${na}${e}`),
        };
        var na;
        const ra = ({ size: e }) => {
            const t = (function (e) {
                const t = e.chunk,
                  a = t.rows * t.columns;
                return (n) => {
                  const r = n % a,
                    u = (r % t.columns) * e.width,
                    s = Math.trunc(r / t.columns) * e.height;
                  return { path: e.getChunkPath(Math.trunc(n / a)), x: u, y: s };
                };
              })(aa),
              a = (0, n.useState)(qt.Stop),
              u = a[0],
              s = a[1],
              i = (0, n.useCallback)(() => {
                s(qt.Play);
              }, [s]),
              l = (0, n.useCallback)(() => {
                s(qt.Stop);
              }, [s]);
            return (
              (0, n.useEffect)(
                () => (ta.instance.subscribe(i), () => ta.instance.unsubscribe(i)),
                [i],
              ),
              r().createElement(zt, {
                width: aa.width,
                height: aa.height,
                frameCount: aa.frameCount,
                getImageSource: t,
                loop: !1,
                state: u,
                onAnimationDone: l,
                className: h()(Yt, e === Mt.O.Big && Qt),
              })
            );
          },
          ua = {
            base: "Skill_base_ba",
            base__big: "Skill_base__big_eb",
            container: "Skill_container_0f",
            divider: "Skill_divider_e8",
            divider__small: "Skill_divider__small_42",
          };
        function sa() {
          return (
            (sa =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            sa.apply(this, arguments)
          );
        }
        let ia;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(ia || (ia = {}));
        const la = (0, n.memo)(
            ({
              name: e,
              icon: t,
              type: a,
              size: u,
              commonMarginValue: s,
              marginValue: i,
              clipWidth: l,
              tankmanID: o,
              blinkStyle: c,
              showNewSkillAnimation: m,
              isTooltipEnabled: d = !0,
              isLastZeroSkill: _ = !1,
            }) => {
              const E = (0, n.useRef)(""),
                g = (0, Ee.useSpring)(() => ({ from: { scale: 1 } })),
                b = g[0],
                p = g[1];
              (0, n.useEffect)(() => {
                (a === St.W.New &&
                  E.current === St.W.Possible &&
                  p.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: be.Fs },
                  }),
                  (E.current = a));
              }, [a, p]);
              return r().createElement(
                f.u,
                sa(
                  {},
                  (() => {
                    switch (a) {
                      case St.W.Learned:
                      case St.W.ZeroSkill:
                      case St.W.Learning:
                      case St.W.Irrelevant:
                        return {
                          contentId:
                            R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                              "resId",
                            ),
                          args: { tooltipId: kt.HZ, tankmanID: o, skillName: e },
                        };
                      case St.W.New:
                      case St.W.Possible:
                        return {
                          contentId: R.views.lobby.crew.tooltips.PerkAvailableTooltip("resId"),
                          args: { tankmanID: o },
                        };
                    }
                  })(),
                  {
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                    isEnabled: d,
                    ignoreShowDelay: !0,
                  },
                ),
                r().createElement(
                  Ee.animated.div,
                  { className: ua.container, style: b },
                  r().createElement(
                    Ee.animated.div,
                    { style: a === St.W.Possible ? c : void 0 },
                    r().createElement(
                      "div",
                      {
                        className: h()(ua.base, ua[`base__${u}`]),
                        style: {
                          marginLeft: a !== St.W.ZeroSkill ? `${i}rem` : `${i < 0 ? 2 : i}rem`,
                          clipPath: `inset(0 ${l}rem 0 0)`,
                        },
                      },
                      !m || (a !== St.W.Possible && a !== St.W.New)
                        ? r().createElement(Mt.d, { icon: t, size: u, type: a })
                        : r().createElement(ra, { size: u }),
                    ),
                  ),
                  _ &&
                    r().createElement("div", {
                      className: h()(ua.divider, u === ia.Small && ua.divider__small),
                      style: { marginRight: (u === ia.Small ? 6 : 8) - (i || s || 0) + "rem" },
                    }),
                ),
              );
            },
          ),
          oa = "SkillsList_base_11",
          ca = "SkillsList_numOfSkills_64",
          ma = "SkillsList_numOfSkills__twoRows_8d",
          da = "SkillsList_numOfSkills__hidden_c5",
          _a = "SkillsList_numOfSkillsContent_a4",
          Ea = "SkillsList_numOfSkillsContent__withNew_b6",
          ga = "SkillsList_row_03",
          ba = "SkillsList_skillsWithOutLast_02",
          pa = "SkillsList_skillsWithOutLast__hidden_8d",
          va = "SkillsList_lastSkill_96",
          ha = "SkillsList_lastSkill__wrapped_9d",
          Aa = "SkillsList_possibleLevel_97",
          Ca = "SkillsList_possibleLevel__before_6f",
          fa = (0, n.memo)(
            ({
              tankman: e,
              showAcceleratedTrainingIcon: t = !1,
              rowWidth: a = 220,
              maxBigSkillsInRow: u = 10,
              blinkStyle: s,
              isSkillTooltipEnabled: i = !0,
              isCurrentLayoutHangar: l = !1,
              isWidgetHovered: o = !1,
            }) => {
              const c = e.skills,
                m = c.filter((e) => e.type === St.W.ZeroSkill).length,
                d = m > 0 ? c[m - 1].name : null,
                _ = c.length,
                E = yt(e),
                g = ((e, t, a) => {
                  let n = e > t ? 10 : e;
                  const r = 0 === e ? e : Math.ceil(e / n),
                    u = r > 1 ? 16 : 24;
                  let s = 2,
                    i = u;
                  for (; (a - (u + s)) / (i + s) < Math.floor((e - 1) / r);) s > 0 ? s-- : i--;
                  return (
                    (n = Math.min(n, 1 + Math.floor((a - u) / (i + s)))),
                    i !== u && (s = i - u),
                    [r, n, s, u, i]
                  );
                })(E, u, a),
                b = g[0],
                p = g[1],
                v = g[2],
                C = g[3],
                f = g[4],
                D = b > 1 ? ia.Small : ia.Big,
                F = (0, n.useMemo)(
                  () =>
                    r().createElement(
                      Ee.animated.div,
                      { className: h()(Aa, 0 === _ && Ca), style: s },
                      r().createElement(Tt, {
                        percentValue: e.lastPossibleRoleLevel,
                        skillSize: D,
                        hasSkills: e.possibleSkillsAmount > 0 || _ > 0,
                      }),
                    ),
                  [s, D, _, e.lastPossibleRoleLevel, e.possibleSkillsAmount],
                ),
                B = e.skills.filter((e) => e.type === St.W.New).length > 1,
                k = (0, n.useCallback)(
                  (t, a) => {
                    const n = p * t + a;
                    let r = "",
                      u = "",
                      s = St.W.Learned;
                    if (n < _) {
                      const e = c[n];
                      e && ((r = e.name), (u = e.icon), (s = e.type));
                    } else s = n < _ + e.newSkillsAmount ? St.W.New : St.W.Possible;
                    return { skillIndex: n, name: r, icon: u, type: s };
                  },
                  [p, c, _, e.newSkillsAmount],
                ),
                w = Array(b)
                  .fill(null)
                  .reduce((e, t, a) => e + Math.min(p, E - a * p) - 1, 0),
                y = (0, n.useCallback)(
                  (t, a, n) => {
                    const u = a - 1,
                      c = k(t, u),
                      d = c.skillIndex,
                      _ = c.name,
                      E = c.icon,
                      g = c.type,
                      p = 0 === u ? v : 0,
                      A = u * (C + v),
                      f = 2 * (D === ia.Big ? 8 : 6) + 1 - v;
                    return r().createElement(
                      "div",
                      {
                        className: h()(va, l && !o && ha),
                        style: {
                          "--leftPosition": -(A + (!(m > 0) || (b > 1 && n) ? 0 : f)) + "rem",
                        },
                      },
                      r().createElement(la, {
                        name: _,
                        icon: E,
                        type: g,
                        size: D,
                        marginValue: 0 === u ? 0 : v,
                        commonMarginValue: p,
                        key: d + "_" + _,
                        clipWidth: 0,
                        tankmanID: e.tankmanID,
                        blinkStyle: s,
                        isTooltipEnabled: i,
                        showNewSkillAnimation: l,
                      }),
                    );
                  },
                  [k, v, l, o, C, m, b, D, e.tankmanID, s, i],
                );
              return r().createElement(
                "div",
                { className: oa },
                r().createElement(
                  "div",
                  { className: h()(ca, b > 1 && ma, o && da) },
                  l &&
                    w > 0 &&
                    r().createElement(A.ZP, {
                      className: h()(_a, B && Ea),
                      text: R.strings.crew_widget.hiddenSkills(),
                      format: { binding: { num: w } },
                    }),
                ),
                (0, Nt.K)(b, (a) => {
                  const n = Math.min(p, E - a * p),
                    u = a === b - 1;
                  return r().createElement(
                    "div",
                    { className: ga, key: `row_${a}` },
                    e.lastPossibleRoleLevel > 0 && 0 === _ && F,
                    r().createElement(
                      "div",
                      { className: h()(ba, l && !o && pa) },
                      (0, Nt.K)(n - 1, (t) => {
                        const u = k(a, t),
                          o = u.skillIndex,
                          c = u.name,
                          m = u.icon,
                          _ = u.type;
                        return r().createElement(la, {
                          name: c,
                          icon: m,
                          type: _,
                          size: D,
                          marginValue: 0 === t ? 0 : v,
                          commonMarginValue: 0 === t ? v : 0,
                          key: o + "_" + c + "_" + _,
                          clipWidth: t === n - 1 || _ === St.W.ZeroSkill ? 0 : C - f,
                          tankmanID: e.tankmanID,
                          blinkStyle: s,
                          isTooltipEnabled: i,
                          showNewSkillAnimation: l,
                          isLastZeroSkill: c === d,
                        });
                      }),
                    ),
                    y(a, n, u),
                    u &&
                      r().createElement(
                        r().Fragment,
                        null,
                        r().createElement(Rt, {
                          lastSkillLevel: e.possibleSkillsAmount > 0 ? -1 : e.lastSkillLevel,
                          lastPossibleSkillLevel: e.lastPossibleSkillLevel,
                          showAcceleratedTrainingIcon: t,
                          skillSize: D,
                          blinkStyle: s,
                        }),
                        e.lastPossibleRoleLevel > 0 && _ > 0 && F,
                      ),
                  );
                }),
                !b &&
                  r().createElement(
                    "div",
                    { className: ga },
                    e.lastPossibleRoleLevel > 0 && 0 === _ && F,
                    r().createElement(Rt, {
                      lastSkillLevel: e.possibleSkillsAmount > 0 ? -1 : e.lastSkillLevel,
                      lastPossibleSkillLevel: e.lastPossibleSkillLevel,
                      showAcceleratedTrainingIcon: t,
                      skillSize: D,
                      blinkStyle: s,
                    }),
                    e.lastPossibleRoleLevel > 0 && _ > 0 && F,
                  ),
              );
            },
          ),
          Da = "TankmanInfo_base_69",
          Fa = "TankmanInfo_base__disabled_36",
          Ba = "TankmanInfo_tankmanTooltipHoverArea_9b",
          ka = "TankmanInfo_specialization_77",
          wa = "TankmanInfo_specialization__withManySkills_9a",
          ya = "TankmanInfo_skillsContainer_17",
          Sa = "TankmanInfo_skillsContainer__withManySkills_00",
          Na = (0, s.Pi)(
            ({ tankman: e, layoutInfo: t, isUntrained: a, blinkStyle: u, isDisabled: s }) => {
              const i = p().model,
                l = (0, wt.GS)().mediaSize,
                o = i.isWidgetHover.get(),
                c = t.isCurrentLayoutQuickTraining || i.computes.isChangeCrewButtonVisible(),
                m = (0, n.useMemo)(() => (c ? (l >= wt.cJ.Small ? 190 : 146) : 220), [c, l]),
                d = ((e, t) => yt(e) > t)(e, 10),
                _ = !t.isCurrentLayoutQuickTraining && -1 !== e.tankmanID && e.isLessMastered,
                E = e.baseSpecializationLevel >= 100;
              return r().createElement(
                "div",
                { className: h()(Da, s && Fa) },
                r().createElement(
                  Bt.t,
                  {
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                    args: { tooltipId: kt.v$, tankmanID: e.tankmanID },
                    ignoreShowDelay: !1,
                  },
                  r().createElement("div", { className: Ba }),
                ),
                r().createElement(
                  "div",
                  { className: h()(ka, d && wa) },
                  r().createElement(gt, {
                    roles: e.roles,
                    tankmanID: e.tankmanID,
                    specializationLevel: e.specializationLevel,
                    isUntrained: a,
                    name: e.fullName,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                    isAcceleratedTrainingAvailable: _ && !E,
                  }),
                ),
                r().createElement(
                  "div",
                  { className: h()(ya, d && Sa) },
                  r().createElement(fa, {
                    tankman: e,
                    showAcceleratedTrainingIcon: _ && E,
                    rowWidth: m,
                    maxBigSkillsInRow: 10,
                    blinkStyle: u,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                    isWidgetHovered: o,
                  }),
                ),
              );
            },
          ),
          Ia = "QuickTrainingTankmanSlotContent_base_8d",
          Ta = "QuickTrainingTankmanSlotContent_arrow_5a",
          La = "QuickTrainingTankmanSlotContent_highlight_72",
          xa = "QuickTrainingTankmanSlotContent_icon_7c",
          Ra = { transform: "translateY(50rem)", opacity: 0, scale: 1 },
          Ma = { transform: "translateY(0rem)", opacity: 1, scale: 1 },
          Pa = [
            { transform: "translateY(-10rem)", scale: 1.3 },
            { opacity: 0, scale: 1 },
          ],
          Oa = { opacity: 0 },
          Ha = [{ opacity: 1 }, { opacity: 0 }],
          Wa = (0, n.memo)(
            ({
              tankman: e,
              isUntrained: t,
              blinkStyle: a,
              qtTankmanIconStyle: u,
              layoutInfo: s,
              isDisabled: i,
            }) => {
              const l = (0, n.useRef)(e.lastSkillLevelFull),
                o = (0, n.useRef)(e.skills.length),
                c = (0, Ee.useSpring)(() => ({ from: Ra })),
                m = c[0],
                d = c[1],
                _ = (0, Ee.useSpring)(() => ({ from: Oa })),
                E = _[0],
                g = _[1],
                b = (0, n.useRef)(!1);
              return (
                (0, n.useEffect)(() => {
                  e.hasPossibleProgress
                    ? b.current ||
                      (d.start({
                        from: Ra,
                        to: Ma,
                        reverse: false,
                        config: { duration: 300, easing: be.BH },
                      }),
                      (b.current = !0))
                    : b.current
                      ? (l.current !== e.lastSkillLevelFull || o.current !== e.skills.length
                          ? (d.start({
                              from: Ma,
                              to: Pa,
                              delay: 200,
                              config: { duration: 500, easing: be.BH },
                            }),
                            (l.current = e.lastSkillLevelFull),
                            (o.current = e.skills.length),
                            g.start({
                              from: Oa,
                              to: Ha,
                              delay: 200,
                              config: { duration: 500, easing: be.BH },
                            }))
                          : d.start({ reset: !0, reverse: !0 }),
                        (b.current = !1))
                      : ((l.current = e.lastSkillLevelFull), (o.current = e.skills.length));
                }, [d, g, e.lastSkillLevelFull, e.hasPossibleProgress, e.skills.length]),
                r().createElement(
                  "div",
                  { className: Ia },
                  r().createElement(Ee.animated.div, { className: La, style: E }),
                  r().createElement(
                    Ee.animated.div,
                    { style: u },
                    r().createElement(Qe.G, {
                      name: e.icon,
                      size: Qe.U.c100x60Barracks,
                      className: xa,
                      isSkin: e.isInSkin,
                    }),
                  ),
                  r().createElement(Ee.animated.div, { className: Ta, style: m }),
                  r().createElement(Na, {
                    tankman: e,
                    layoutInfo: s,
                    isUntrained: t,
                    blinkStyle: a,
                    isDisabled: i,
                  }),
                )
              );
            },
            (e, t) => {
              const a = e.tankman,
                n = t.tankman;
              return (
                a.hasPossibleProgress === n.hasPossibleProgress &&
                ((e, t) => {
                  if (e.length !== t.length) return !1;
                  const a = e.length;
                  for (let u = 0; u < a; u++) {
                    var n, r;
                    if (
                      (null == (n = c.U2(e, u)) ? void 0 : n.name) !==
                      (null == (r = c.U2(t, u)) ? void 0 : r.name)
                    )
                      return !1;
                  }
                  return !0;
                })(a.skills, n.skills) &&
                a.lastSkillLevelFull === n.lastSkillLevelFull &&
                a.possibleSkillsAmount === n.possibleSkillsAmount &&
                a.lastPossibleSkillLevel === n.lastPossibleSkillLevel &&
                a.specializationLevel === n.specializationLevel &&
                a.lastPossibleRoleLevel === n.lastPossibleRoleLevel
              );
            },
          ),
          Ga = "TankmanSlotContent_base_00",
          Va = "TankmanSlotContent_icon_ef",
          za = (0, n.memo)(({ tankman: e, layoutInfo: t, isUntrained: a, isDisabled: n }) =>
            r().createElement(
              "div",
              { className: Ga },
              r().createElement(Qe.G, {
                name: e.icon,
                size: Qe.U.c100x60Barracks,
                className: Va,
                isSkin: e.isInSkin,
              }),
              r().createElement(Na, { tankman: e, layoutInfo: t, isUntrained: a, isDisabled: n }),
            ),
          ),
          Za = (0, n.memo)(
            ({
              roles: e,
              tankman: t,
              layoutInfo: a,
              vehicleName: n,
              vehicleType: u,
              isUntrained: s,
              isDisabled: i,
              isSelected: l,
              blinkSlotStyle: o,
              blinkTankmanStyle: c,
              qtTankmanIconStyle: m,
            }) =>
              -1 === t.tankmanID
                ? r().createElement(Ft, {
                    roles: e,
                    layoutInfo: a,
                    vehicleName: n,
                    vehicleType: u,
                    isDisabled: i,
                    isSelected: l,
                    blinkStyle: c,
                    qtTankmanIconStyle: m,
                  })
                : a.isCurrentLayoutQuickTraining
                  ? r().createElement(Wa, {
                      tankman: t,
                      isUntrained: s,
                      blinkStyle: o,
                      qtTankmanIconStyle: m,
                      layoutInfo: a,
                      isDisabled: i,
                    })
                  : r().createElement(za, {
                      tankman: t,
                      layoutInfo: a,
                      isUntrained: s,
                      isDisabled: i,
                    }),
          ),
          ja = { transform: "translateX(0rem)" },
          $a = { transform: "translateX(41rem)" },
          Ua = { opacity: 0 },
          Xa = { opacity: 1 },
          qa = (0, s.Pi)(
            ({
              slotIdx: e,
              roles: t,
              tankman: a,
              layoutInfo: s,
              isSelected: i,
              isAnySlotSelected: l,
              isDisabled: o,
              blinkSlotStyle: c,
              blinkTankmanStyle: m,
              qtTankmanIconStyle: d,
            }) => {
              const E = p(),
                g = E.model,
                b = E.controls,
                v = ((e, t) => {
                  const a = (0, K.Jp)(_.D9),
                    n = (0, X.f)(
                      () => a({ action: _.eX.Click, parentScreen: e, item: t }),
                      [e, t],
                      _.tL,
                    );
                  return (e) => {
                    e.button === q.RIGHT && n();
                  };
                })(g.computes.getUiLoggingParentScreen(), _.x3.SlotContextMenu),
                A = b.onSlotClick,
                C = b.onChangeCrewClick,
                f = g.isWidgetHover.get(),
                D = g.computes.isChangeCrewButtonVisible(),
                F = g.computes.isTankmanMode(),
                B = g.isCrewLocked.get(),
                k = g.vehicleName.get(),
                w = g.vehicleType.get(),
                y = !o && a.isInteractive && (!s.isCurrentLayoutQuickTraining || l),
                S = (0, n.useCallback)(() => {
                  y && !F && ((0, u.G)(R.sounds.yes1()), A(e, a.tankmanID));
                }, [e, a, A, F, y]),
                N = (0, n.useCallback)(
                  (t) => {
                    (t.stopPropagation(), B || ((0, u.G)(R.sounds.yes1()), C(e, a.tankmanID)));
                  },
                  [e, a, C, B],
                ),
                I = (0, n.useMemo)(() => ({ tankmanID: a.tankmanID, slotIdx: e }), [a, e]);
              return r().createElement(
                Pe,
                {
                  args: I,
                  isEnabled: !o,
                  targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  onMouseDown: v,
                },
                r().createElement(
                  "div",
                  null,
                  r().createElement(
                    ve,
                    {
                      onClick: S,
                      isSelected: i,
                      isDisabled: o,
                      isEmpty: -1 === a.tankmanID,
                      layoutInfo: s,
                      isEnabledForMouse: y,
                      isWidgetHovered: f,
                    },
                    r().createElement(
                      "div",
                      { className: je },
                      a.hasWarning && r().createElement("div", { className: qe }),
                      i && r().createElement("div", { className: F ? Ye : Ke }),
                      r().createElement(
                        he,
                        {
                          startState: ja,
                          endState: $a,
                          layoutInfo: s,
                          isPaused: !D,
                          className: h()(Ue, D && Xe),
                          isTankmanMode: F,
                        },
                        r().createElement(Za, {
                          roles: t,
                          tankman: a,
                          layoutInfo: s,
                          isUntrained: a.isUntrained,
                          isDisabled: o,
                          vehicleName: k,
                          vehicleType: w,
                          blinkSlotStyle: c,
                          blinkTankmanStyle: m,
                          qtTankmanIconStyle: d,
                          isSelected: i,
                        }),
                      ),
                      D &&
                        r().createElement(
                          "div",
                          { onClick: N },
                          r().createElement(
                            he,
                            {
                              startState: Ua,
                              endState: Xa,
                              layoutInfo: s,
                              isPaused: !D,
                              className: $e,
                              isTankmanMode: F,
                            },
                            r().createElement(Ze, {
                              isSelected: s.isCurrentLayoutMemberChange && i,
                              isLocked: B,
                              mainRole: t[0] || "",
                              isFemale: -1 !== a.tankmanID && a.isFemale,
                            }),
                          ),
                        ),
                    ),
                  ),
                ),
              );
            },
          ),
          Ka = "SlotsList_base_5f";
        function Ya() {
          return (
            (Ya =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Ya.apply(this, arguments)
          );
        }
        const Qa = { transform: "translateX(0rem)" },
          Ja = { transform: "translateX(15rem)" },
          en = (0, s.Pi)(({ layoutInfo: e, isWidgetDisabled: t, className: a }) => {
            const u = p().model,
              s = u.computes.isAnyEmptySlots(),
              i = (0, Ee.useSpring)(
                () => ({
                  from: { opacity: 1 },
                  to: [{ opacity: 0 }, { opacity: 1 }],
                  config: { duration: 750, easing: be.Fs },
                  loop: !0,
                }),
                [],
              ),
              l = i[0],
              o = i[1];
            (0, n.useEffect)(() => {
              s ? o.resume() : o.pause();
            }, [o, s]);
            const c = (0, Ee.useSpring)(
                () => ({
                  from: { opacity: 1 },
                  to: [{ opacity: 0.3 }, { opacity: 1 }],
                  config: { duration: 400, easing: be.Fs },
                  loop: !0,
                }),
                [],
              ),
              m = c[0],
              d = c[1];
            (0, n.useEffect)(() => {
              e.isCurrentLayoutQuickTraining ? d.resume() : d.pause();
            }, [d, e.isCurrentLayoutQuickTraining]);
            const _ = (0, Ee.useSpring)(() => ({
                from: Qa,
                to: Ja,
                delay: 200,
                config: { duration: 300, easing: be.ei },
                pause: !e.isCurrentLayoutQuickTraining,
              }))[0],
              E = (0, n.useCallback)(
                (a) => t || (e.isCurrentLayoutQuickTraining && -1 === a),
                [t, e.isCurrentLayoutQuickTraining],
              );
            return r().createElement(
              "div",
              { id: "crew_widget_slots_list", className: h()(Ka, a) },
              u.computes
                .getSlots()
                .map((t, a) =>
                  r().createElement(
                    qa,
                    Ya({}, t, {
                      layoutInfo: e,
                      key: `slot_${a}_${t.tankman.tankmanID}`,
                      isSelected:
                        !e.isCurrentLayoutHangar &&
                        (u.computes.isSlotSelected(t.slotIdx) || u.computes.isTankmanMode()),
                      isAnySlotSelected: u.computes.isAnySlotSelected(),
                      isDisabled: E(t.tankman.tankmanID),
                      blinkSlotStyle: m,
                      blinkTankmanStyle: l,
                      qtTankmanIconStyle: _,
                    }),
                  ),
                ),
            );
          }),
          tn = (0, s.Pi)(() => {
            const e = p(),
              t = e.model,
              a = e.controls,
              s = t.isDisabled.get(),
              i = t.hasDog.get(),
              l = t.computes.getLayoutInfo(),
              o = t.isExtended.get();
            return (
              (0, n.useEffect)(() => {
                a.setIsWidgetHover(o);
              }, [o, a]),
              r().createElement(
                "div",
                {
                  className: me,
                  onMouseEnter: () => {
                    o ||
                      (a.setIsWidgetHover(!0),
                      l.isCurrentLayoutHangar && !s && (0, u.G)(R.sounds.crew_hover()));
                  },
                  onMouseLeave: () => {
                    o ||
                      (a.setIsWidgetHover(!1),
                      l.isCurrentLayoutHangar && !s && (0, u.G)(R.sounds.crew_unhover()));
                  },
                },
                t.computes.isButtonBarVisible() &&
                  r().createElement(
                    "div",
                    { className: de },
                    r().createElement(ce, {
                      isWidgetDisabled: s,
                      isCurrentLayoutHangar: l.isCurrentLayoutHangar,
                    }),
                  ),
                r().createElement(en, { layoutInfo: l, isWidgetDisabled: s, className: _e }),
                i && r().createElement(Te, { layoutInfo: l, isDisabled: s }),
              )
            );
          }),
          an = (0, n.memo)(() =>
            r().createElement(
              b,
              { options: { rootId: R.views.lobby.crew.widgets.CrewWidget("resId") } },
              r().createElement(tn, null),
            ),
          );
      },
      5801: (e, t, a) => {
        "use strict";
        a.d(t, { p: () => Pe });
        var n = a(6179),
          r = a.n(n),
          u = a(6483),
          s = a.n(u),
          i = a(3457),
          l = a(2106),
          o = a(7613),
          c = a(6373);
        let m;
        !(function (e) {
          ((e.Default = "default"),
            (e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(m || (m = {}));
        var d = a(3403),
          _ = a(3415),
          E = a(9480),
          g = a(9631);
        const b = "FilterTitle_base_a7",
          p = "FilterTitle_label_05",
          v = "FilterTitle_discount_42",
          h = "FilterTitle_discountIcon_30",
          A = ({ label: e, hasDiscount: t, className: a }) =>
            r().createElement(
              "div",
              { className: s()(b, a) },
              r().createElement("div", { className: p }, e),
              t &&
                r().createElement(
                  "div",
                  { className: v },
                  r().createElement("div", { className: h }),
                ),
            );
        let C;
        !(function (e) {
          ((e.Default = "default"),
            (e.Nation = "nation"),
            (e.Location = "location"),
            (e.TankmanRole = "tankmanRole"),
            (e.TankmanKind = "tankmanKind"),
            (e.VehicleGrade = "vehicleGrade"),
            (e.VehicleTier = "vehicleTier"),
            (e.VehicleType = "vehicleType"),
            (e.PersonalDataType = "personalDataType"),
            (e.VehicleCD = "vehicle"));
        })(C || (C = {}));
        var f = a(3649);
        const D = "ToggleIcon_base_59",
          F = "ToggleIcon_base__small_3e",
          B = "ToggleIcon_icon_e7",
          k = r().memo(function ({ icon: e, isSmall: t = !1, classNames: a }) {
            return r().createElement(
              "div",
              { className: s()(D, t && F) },
              r().createElement("div", {
                className: s()(B, null == a ? void 0 : a.icon),
                style: { backgroundImage: `url(${e})` },
              }),
            );
          });
        var w = a(9690);
        const y = "VehicleTier_base_9c",
          S = "VehicleTier_base__small_fc",
          N = ({ level: e, isSmall: t = !1 }) =>
            r().createElement("div", { className: s()(y, t && S) }, (0, w.HG)(e)),
          I = {
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
          T = ({ id: e, icon: t, type: a, isSmall: n = !0, isSelected: u = !1 }) =>
            a === C.VehicleTier
              ? r().createElement(N, { isSmall: n, level: Number(e) })
              : r().createElement(k, {
                  icon: t,
                  isSmall: n,
                  classNames: {
                    icon: s()(
                      I[`icon__${a}`],
                      I[`icon__${a}${(0, f.e)(e)}`],
                      u && I.icon__selected,
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
        function x() {
          return (
            (x =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            x.apply(this, arguments)
          );
        }
        let M;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(M || (M = {}));
        const P = ({ header: e, body: t, contentId: a, targetId: n }) =>
            a
              ? { contentId: a, targetId: n }
              : t || e
                ? { header: null != e ? e : void 0, body: null != t ? t : void 0 }
                : void 0,
          O = ({
            id: e,
            type: t,
            label: a,
            hasDiscount: n,
            filters: u,
            onClick: i,
            className: l,
            toggleProps: o,
            theme: c = M.Default,
          }) => {
            const m = c === M.InPopup;
            return r().createElement(
              "div",
              { className: s()(L.base, L[`base__${c}`], l) },
              m && r().createElement(A, { className: L.title, label: a, hasDiscount: n }),
              r().createElement(
                "div",
                { className: L.content },
                E.UI(u, ({ id: a, isSelected: n, tooltip: u, icon: l, counter: c }) =>
                  r().createElement(
                    _.l,
                    { key: a, tooltipArgs: P(u), className: L.toggle },
                    r().createElement(
                      g.C,
                      x({}, o, {
                        className: s()(L.toggle, null == o ? void 0 : o.className),
                        isActive: n,
                        onClick: () => (null == i ? void 0 : i(e, a)),
                        counter: c,
                      }),
                      r().createElement(T, { id: a, icon: l, type: t, isSmall: m, isSelected: n }),
                    ),
                  ),
                ),
              ),
            );
          };
        var H = a(9197),
          W = a(3215),
          G = a(4598),
          V = a(5175),
          z = a(3946);
        const Z = (0, W.q)()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  amountInfo: e.object("amountInfo"),
                  filter: e.array("filter"),
                  filters: e.array("filter.filters"),
                },
                a = (0, z.Om)(() => (0, V.c)(t.filter.get()), { equals: G.jv }),
                n = (0, z.Om)(() => (0, V.c)(t.filters.get()), { equals: G.jv }),
                r = (0, z.Om)(
                  () =>
                    (0, V.c)(t.filters.get()).filter((e) => "dismissed" === e.id && e.isSelected)
                      .length > 0,
                  { equals: G.jv },
                );
              return Object.assign({}, t, {
                computes: { getFilterGroup: a, getFilters: n, getIsRestoreFilter: r },
              });
            },
            ({ externalModel: e }) => ({
              search: e.createCallback((e) => ({ value: e }), "onSearch"),
              updateFilter: e.createCallback(
                (e, t) => ({ groupID: e, toggleID: t }),
                "onUpdateFilter",
              ),
              resetFilter: e.createCallbackNoArgs("onResetFilter"),
              updateSelectMode: e.createCallbackNoArgs("onSelectedModeChange"),
              onCancelSelection: e.createCallbackNoArgs("onCancelSelection"),
              onDismissOrRestore: e.createCallbackNoArgs("onDismissOrRestore"),
            }),
          ),
          j = Z[0],
          $ = Z[1];
        var U = a(3616),
          X = a(1037),
          q = a(9367);
        const K = "PopupButton_base_7c",
          Y = "PopupButton_popupButtonLabel_ed",
          Q = "PopupButton_buttonIconWrapper_d7",
          J = "PopupButton_buttonIcon_e0",
          ee = "PopupButton_buttonIcon__isHighlighted_84",
          te = "PopupButton_discountAlert_c8",
          ae = ({ isHighlighted: e, hasDiscountAlert: t, popoverDirection: a = X.IC.Bottom }) =>
            r().createElement(
              "div",
              { className: K },
              r().createElement(
                "div",
                { className: Y },
                R.strings.crew.filter.popup.button.title(),
              ),
              r().createElement(
                U.Z,
                {
                  contentId: R.views.lobby.crew.popovers.FilterPopoverView("resId"),
                  targetId: R.views.lobby.crew.widgets.FilterPanelWidget("resId"),
                  direction: a,
                },
                r().createElement(
                  "div",
                  { id: "popup_btn", className: Q },
                  r().createElement(
                    g.C,
                    { type: i.L$.ghost, size: i.qE.small, isActive: e, hasIndicator: !1 },
                    r().createElement("div", { className: s()(J, e && ee) }),
                  ),
                  t && r().createElement(q.Q, { className: te }),
                ),
              ),
            );
        var ne = a(8018);
        const re = "ResetButton_base_58",
          ue = "ResetButton_button_a5",
          se = "ResetButton_icon_4a",
          ie = ({ isSelectMode: e, onClick: t }) =>
            r().createElement(
              "div",
              { className: re },
              r().createElement(
                c.i,
                e ? ne.Er : ne.Xd,
                r().createElement(
                  i.u5,
                  { mixClass: ue, onClick: t, type: i.L$.ghost, size: i.qE.small },
                  r().createElement("div", { className: se }),
                ),
              ),
            ),
          le = "default",
          oe = "search",
          ce = "email",
          me = "password",
          de = "normal",
          _e = "disabled",
          Ee = "alert",
          ge = "error",
          be = "medium",
          pe = {
            [le]: "",
            [ce]: R.strings.common.input.placeholder.email(),
            [oe]: R.strings.common.input.placeholder.search(),
            [me]: R.strings.common.input.placeholder.password(),
          },
          ve = { [le]: "text", [ce]: "text", [oe]: "text", [me]: "password" },
          he = { [le]: "", [ce]: "Invalid email", [oe]: "", [me]: "" },
          Ae = R.images.gui.maps.icons.components.input;
        function Ce(e, t) {
          return (
            t !== ce ||
            (function (e) {
              const t = e.match(
                /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
              );
              return Boolean(t);
            })(e)
          );
        }
        var fe = a(7727);
        const De = {
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
          Fe = r().memo(
            ({
              componentId: e,
              value: t = "",
              type: a = le,
              size: u = be,
              variant: i = de,
              placeholder: l = "",
              highlighted: o,
              withClear: c,
              selectOnFocus: m = !0,
              maxLength: d,
              iconSource: _,
              classMix: E,
              onMouseEnter: g,
              onMouseLeave: b,
              onMouseDown: p,
              onMouseUp: v,
              onClick: h,
              onChange: A,
              onClear: C,
              onFocus: f,
              onBlur: D,
            }) => {
              const F = (0, n.useState)(!1),
                B = F[0],
                k = F[1],
                w = (0, n.useRef)(null),
                y = (0, n.useRef)({ mouseOver: !1, mouseDown: !1 }),
                S = i !== _e,
                N = (0, n.useCallback)(
                  (e) => {
                    S && (k(!0), f && f(e));
                  },
                  [S, f],
                ),
                I = (0, n.useCallback)(
                  (e) => {
                    S && !y.current.mouseOver && (k(!1), D && D(e));
                  },
                  [S, D],
                );
              (0, n.useEffect)(() => {
                S && B && m && w.current && w.current.select();
              }, [m, B, S]);
              const T = (0, n.useCallback)(
                  (e) => {
                    S && A && A(e.target.value);
                  },
                  [S, A],
                ),
                L = (0, n.useCallback)(
                  (e) => {
                    S && ((y.current.mouseOver = !0), g && g(e));
                  },
                  [S, g],
                ),
                x = (0, n.useCallback)(
                  (e) => {
                    S &&
                      w.current &&
                      (y.current.mouseDown && w.current.focus(),
                      (y.current.mouseOver = !1),
                      b && b(e));
                  },
                  [S, b],
                ),
                R = (0, n.useCallback)(
                  (e) => {
                    S && ((y.current.mouseDown = !0), p && p(e));
                  },
                  [S, p],
                ),
                M = (0, n.useCallback)(
                  (e) => {
                    S && ((y.current.mouseDown = !1), v && v(e));
                  },
                  [S, v],
                ),
                P = (0, n.useCallback)(
                  (e) => {
                    if (S && w.current) {
                      ((!B || (B && e.target !== w.current)) && w.current.focus(), h && h(e));
                    }
                  },
                  [B, S, h],
                ),
                O = l || pe[a],
                H = Boolean(_),
                W = s()(
                  De.base,
                  De[`base__${u}`],
                  o && De[`base__${i}`],
                  B && De.base__focused,
                  H && De.base__withIcon,
                  E,
                ),
                G = (0, n.useMemo)(() => (_ ? { backgroundImage: `url(${_})` } : null), [_]),
                V = s()(De.input, De[`input__${a}`]),
                z = s()(De.icon, De[`icon__${a}`]),
                Z = s()(De.placeholder, De[`placeholder__${a}`]);
              return r().createElement(
                "div",
                {
                  id: e,
                  className: W,
                  onMouseEnter: L,
                  onMouseDown: R,
                  onMouseUp: M,
                  onMouseLeave: x,
                  onClick: P,
                },
                !S && r().createElement("div", { className: De.disabled }),
                G && r().createElement("div", { style: G, className: z }),
                r().createElement("input", {
                  ref: w,
                  className: V,
                  type: ve[a],
                  value: t,
                  onChange: T,
                  disabled: !S,
                  onFocus: N,
                  onBlur: I,
                  maxLength: d,
                }),
                O && !t && !B && r().createElement("div", { className: Z }, O),
                c &&
                  r().createElement("div", {
                    className: De.clear,
                    onClick: (e) => {
                      (fe.$.playClick(), C && C(e));
                    },
                    onMouseEnter: fe.$.playHighlight,
                  }),
              );
            },
          ),
          Be = {
            base: "HelperMessage_base_1e",
            base__shown: "HelperMessage_base__shown_ab",
            icon: "HelperMessage_icon_10",
            message: "HelperMessage_message_f4",
            message__alert: "HelperMessage_message__alert_b5",
            message__error: "HelperMessage_message__error_45",
            message__done: "HelperMessage_message__done_2b",
          },
          ke = ({ variant: e, show: t = !0, helperText: a, helperIcon: u, classMix: i }) => {
            const l = (0, n.useMemo)(() => {
                const t =
                  u ||
                  (function (e) {
                    return e === Ee ? R.images.gui.maps.icons.library.alertIcon() : "";
                  })(e);
                return t && { backgroundImage: `url(${t})` };
              }, [u, e]),
              o = s()(Be.base, t && Be.base__shown),
              c = s()(Be.message, Be[`message__${e}`], i);
            return r().createElement(
              "div",
              { className: o },
              l && r().createElement("div", { className: Be.icon, style: l }),
              r().createElement("div", { className: c }, a),
            );
          },
          we = {
            base: "Input_base_cd",
            base__small: "Input_base__small_c7",
            base__medium: "Input_base__medium_1f",
            base__large: "Input_base__large_11",
            helper: "Input_helper_ea",
          },
          ye = [
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
        function Se() {
          return (
            (Se =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            Se.apply(this, arguments)
          );
        }
        const Ne = {
            debounceTime: 200,
            performChangeValidation: !0,
            selectOnFocus: !0,
            withTypeIcon: !0,
            disableHighlightOnFocus: !0,
          },
          Ie = (e) => {
            let t = e.componentId,
              a = e.type,
              u = void 0 === a ? le : a,
              i = e.variant,
              l = void 0 === i ? de : i,
              o = e.size,
              c = void 0 === o ? be : o,
              m = e.value,
              d = e.tooltipArgs,
              E = e.helperText,
              g = void 0 === E ? "" : E,
              b = e.isValidated,
              p = void 0 === b || b,
              v = e.showHelper,
              h = void 0 === v || v,
              A = e.error,
              C = e.options,
              f = e.onFocus,
              D = e.onMouseEnter,
              F = e.onMouseLeave,
              B = e.onMouseUp,
              k = e.onMouseDown,
              w = e.onChange,
              y = e.classMix,
              S = e.controlClassMix,
              N = e.helperClassMix,
              I = (function (e, t) {
                if (null == e) return {};
                var a,
                  n,
                  r = {},
                  u = Object.keys(e);
                for (n = 0; n < u.length; n++) ((a = u[n]), t.indexOf(a) >= 0 || (r[a] = e[a]));
                return r;
              })(e, ye);
            const T = (0, n.useState)(m),
              L = T[0],
              x = T[1],
              R = (0, n.useState)(p),
              M = R[0],
              P = R[1],
              O = (0, n.useMemo)(() => Object.assign({}, Ne, C), [C]),
              H = (0, n.useRef)({ debounceTimeout: 0, isChangeHandled: !0, value: m, type: u }),
              W = (0, n.useCallback)((e) => {
                e !== H.current.value &&
                  ((H.current.value = e), (H.current.isChangeHandled = !1), x(e));
              }, []),
              G = (0, n.useCallback)(
                (e) => {
                  let t = !0;
                  (O.performChangeValidation &&
                    (t = O.changesValidator ? O.changesValidator(e) : Ce(e, H.current.type)),
                    w && w(e, t));
                },
                [w, O],
              ),
              V = (0, n.useCallback)(() => {
                H.current.debounceTimeout &&
                  (window.clearTimeout(H.current.debounceTimeout), (H.current.debounceTimeout = 0));
              }, []),
              z = (0, n.useCallback)(() => W(""), [W]);
            (0, n.useEffect)(() => () => V(), [V]);
            const Z = (0, n.useCallback)(
              (e) => {
                (V(),
                  O.debounceTime
                    ? (H.current.debounceTimeout = window.setTimeout(() => {
                        G(e);
                      }, O.debounceTime))
                    : G(e));
              },
              [G, V, O.debounceTime],
            );
            ((0, n.useEffect)(() => {
              H.current.isChangeHandled ||
                H.current.value !== L ||
                (Z(H.current.value), (H.current.isChangeHandled = !0));
            }, [L, Z]),
              (0, n.useEffect)(() => {
                (H.current.isChangeHandled &&
                  m !== H.current.value &&
                  ((H.current.value = m), x(m)),
                  (H.current.type = u));
              }, [m, u]),
              (0, n.useEffect)(() => {
                P(p);
              }, [p, l]));
            const j = (0, n.useCallback)((e) => D && D(e), [D]),
              $ = (0, n.useCallback)(
                (e) => {
                  (O.disableHighlightOnFocus && M && P(!1), f && f(e));
                },
                [M, f, O.disableHighlightOnFocus],
              ),
              U = (0, n.useCallback)((e) => B && B(e), [B]),
              X = (0, n.useCallback)((e) => k && k(e), [k]),
              q = (0, n.useCallback)((e) => F && F(e), [F]),
              K = (0, n.useMemo)(
                () =>
                  O.withTypeIcon
                    ? (function (e, t) {
                        return e === oe ? Ae.$dyn(`search_${t}`) : "";
                      })(u, c)
                    : "",
                [u, c, O.withTypeIcon],
              ),
              Y = g || he[u],
              Q = Boolean(L),
              J = A ? ge : l,
              ee = Boolean(A) || M,
              te = (0, n.useMemo)(
                () => ("boolean" == typeof O.withClear ? Q && O.withClear : Q && u === oe),
                [u, Q, O],
              ),
              ae = s()(we.base, we[`base__${c}`], we[`base__${l}`], y);
            return r().createElement(
              "div",
              {
                id: t,
                className: ae,
                onMouseEnter: j,
                onMouseDown: X,
                onMouseUp: U,
                onMouseLeave: q,
              },
              r().createElement(
                _.l,
                { tooltipArgs: d },
                r().createElement(
                  Fe,
                  Se(
                    {
                      componentId: t ? `${t}-inputControl` : void 0,
                      iconSource: K,
                      size: c,
                      type: u,
                      variant: J,
                      value: L,
                      withClear: te,
                      highlighted: ee,
                      selectOnFocus: O.selectOnFocus,
                      maxLength: O.maxLength,
                      classMix: S,
                      onFocus: $,
                      onChange: W,
                      onClear: z,
                    },
                    I,
                  ),
                ),
              ),
              Y &&
                r().createElement(
                  "div",
                  { className: we.helper },
                  r().createElement(ke, {
                    variant: J,
                    show: h && (O.isPermanentHelper || ee),
                    helperText: A || Y,
                    helperIcon: O.helperIconSource,
                    classMix: N,
                  }),
                ),
            );
          },
          Te = ({
            value: e,
            placeholder: t,
            tooltipHeader: a,
            onChange: n,
            className: u,
            tooltipBody: s,
          }) =>
            r().createElement(
              c.i,
              { header: null != a ? a : void 0, body: s, isEnabled: Boolean(a || s) },
              r().createElement(Ie, {
                type: oe,
                placeholder: null != t ? t : void 0,
                value: e,
                classMix: u,
                onChange: n,
              }),
            ),
          Le = {
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
        var xe = a(5415);
        const Re = R.strings.crew.filterPanel,
          Me = (0, d.Pi)(({ popoverDirection: e }) => {
            const t = $(),
              a = t.model,
              n = t.controls,
              u = a.root.get(),
              d = u.hasDiscountAlert,
              _ = u.isPopoverHighlighted,
              E = u.isPopoverEnabled,
              g = u.searchTooltipBody,
              b = u.searchTooltipHeader,
              p = u.searchPlaceholder,
              v = u.searchString,
              h = u.isSearchEnabled,
              A = u.title,
              C = u.panelType,
              f = u.hasAppliedFilters,
              D = u.popoverTooltipHeader,
              F = u.popoverTooltipBody,
              B = u.isSelectedMode,
              k = u.isSelectButtonVisible,
              w = u.isSelectButtonActive,
              y = u.isSelectedLimitReached,
              S = a.amountInfo.get(),
              N = S.from,
              I = S.to,
              T = a.computes.getFilterGroup(),
              L = a.computes.getFilters(),
              x = a.computes.getIsRestoreFilter(),
              M = f || (0 === N && 0 === I) || B,
              P =
                (0, xe.GS)().mediaSize === xe.cJ.ExtraSmall && B
                  ? R.strings.crew.tankmanList.selected.titleSmall()
                  : A;
            return r().createElement(
              "div",
              { className: s()(Le.base, Le[`base__${C}`]) },
              r().createElement(
                "div",
                { className: Le.titleWrapper },
                r().createElement(H.C, {
                  title: P || "",
                  isGlowVisible: M,
                  isSelectedLimitReached: y,
                  isFilterRange: !0,
                  isSelectMode: B,
                  from: N,
                  to: I,
                  className: Le.title,
                  classNames: { counterGlow: Le.counterGlow },
                }),
                f && r().createElement(ie, { isSelectMode: B, onClick: n.resetFilter }),
              ),
              r().createElement(
                "div",
                { className: Le.filters },
                h &&
                  r().createElement(
                    r().Fragment,
                    null,
                    r().createElement(Te, {
                      value: v,
                      onChange: n.search,
                      className: Le.search,
                      placeholder: p,
                      tooltipHeader: b,
                      tooltipBody: g,
                    }),
                    C === m.Barracks && k && r().createElement("div", { className: Le.separator }),
                  ),
                T.label && r().createElement(o.ZP, { className: Le.filterLabel, text: T.label }),
                k &&
                  (B
                    ? r().createElement(
                        r().Fragment,
                        null,
                        r().createElement(
                          i.u5,
                          { mixClass: Le.button, type: l.L.primary, onClick: n.onCancelSelection },
                          r().createElement(o.ZP, { text: Re.demobilize.cancel() }),
                        ),
                        r().createElement(
                          i.u5,
                          {
                            mixClass: s()(Le.button, Le.button__demobilize),
                            type: l.L.main,
                            onClick: n.onDismissOrRestore,
                            disabled: !w,
                          },
                          r().createElement(o.ZP, {
                            text: x ? Re.restore.confirm() : Re.demobilize.confirm(),
                          }),
                        ),
                      )
                    : r().createElement(
                        i.u5,
                        { mixClass: Le.button, type: l.L.secondary, onClick: n.updateSelectMode },
                        r().createElement(o.ZP, { text: Re.selectMode.title() }),
                      )),
                (k || h) && r().createElement("div", { className: Le.separator }),
                r().createElement(O, {
                  id: T.id,
                  label: T.label,
                  type: T.type,
                  hasDiscount: T.hasDiscount,
                  filters: L,
                  toggleProps: { type: l.L.ghost },
                  onClick: n.updateFilter,
                }),
                E &&
                  r().createElement(
                    c.i,
                    { header: D || void 0, body: F || void 0, isEnabled: Boolean(D || F) },
                    r().createElement(
                      "div",
                      { className: Le.popupButtonWrapper },
                      r().createElement(ae, {
                        isHighlighted: _,
                        hasDiscountAlert: d,
                        popoverDirection: e,
                      }),
                    ),
                  ),
              ),
            );
          }),
          Pe = ({ popoverDirection: e }) =>
            r().createElement(
              j,
              { options: { rootId: R.views.lobby.crew.widgets.FilterPanelWidget("resId") } },
              r().createElement(Me, { popoverDirection: e }),
            );
      },
      3055: (e, t, a) => {
        "use strict";
        a.d(t, { Zk: () => Ge, zn: () => We, JW: () => Ve });
        var n = a(6179),
          r = a.n(n),
          u = a(6483),
          s = a.n(u),
          i = a(7613),
          l = a(7727),
          o = a(3403),
          c = a(3618),
          m = a(3649),
          d = a(7077);
        const _ = "TankmanFolder_base_00",
          E = "TankmanFolder_activeZone_c3",
          g = "TankmanFolder_folderLight_eb",
          b = "TankmanFolder_base__withLight_93",
          p = "TankmanFolder_base__hovered_f8",
          v = "TankmanFolder_folder_f5",
          h = "TankmanFolder_photoFrame_ae",
          A = "TankmanFolder_base__big_60",
          C = "TankmanFolder_icon_74",
          f = "TankmanFolder_editTextWrapper_07",
          D = "TankmanFolder_editText_4c",
          F = R.images.gui.maps.icons.tankmen.icons.c_204x256,
          B = r().memo(function ({
            name: e,
            className: t,
            isSkin: a = !1,
            isFolderLight: u,
            onClick: o,
          }) {
            const c = (0, n.useState)(!1),
              B = c[0],
              k = c[1],
              w = (0, n.useMemo)(() => {
                const t = (0, m.BN)(String(e));
                return null !== (a ? F.$dyn("crewSkins") : F).$dyn(t) ? d.U.c204x256 : d.U.c158x118;
              }, [e, a]),
              y = s()(_, w === d.U.c204x256 && A, u && b, B && p, t);
            return r().createElement(
              "div",
              { className: y },
              r().createElement("div", {
                className: E,
                onMouseEnter: () => {
                  ((0, l.G)(R.sounds.gui_hangar_hover()), k(!0));
                },
                onMouseLeave: () => {
                  k(!1);
                },
                onClick: o,
              }),
              r().createElement("div", { className: g }),
              r().createElement("div", { className: v }),
              r().createElement(
                "div",
                { className: h },
                r().createElement(d.G, { name: e, size: w, isSkin: a, className: C }),
              ),
              r().createElement(
                "div",
                { className: f },
                r().createElement(i.ZP, {
                  className: D,
                  text: R.strings.crew.personalFile.profileEdit(),
                }),
              ),
            );
          });
        var k = a(3215),
          w = a(3946);
        const y = (0, k.q)()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  currentVehicle: e.object("currentVehicle"),
                  nativeVehicle: e.object("nativeVehicle"),
                  currentVehicleTags: e.array("currentVehicle.tags"),
                },
                a = (0, w.Om)(() => {
                  const e = t.currentVehicle.get(),
                    a = t.nativeVehicle.get(),
                    n = Boolean(e.name);
                  return {
                    isWrongVehicleType: n && !(e.type === a.type && e.isPremium),
                    isWrongVehicle: n && e.name !== a.name,
                  };
                }),
                n = (0, w.Om)(() => {
                  const e = a(),
                    t = e.isWrongVehicle,
                    n = e.isWrongVehicleType;
                  return t && n;
                }),
                r = (0, w.Om)(() =>
                  t.root.get().hasRetrainDiscount
                    ? { args: { tooltipId: "actionPrice" }, targetId: We }
                    : {
                        contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                        targetId: We,
                      },
                );
              return Object.assign({}, t, {
                computes: {
                  vehicleValidator: a,
                  isRoleLevelPenaltyActive: n,
                  discountTooltipArgs: r,
                },
              });
            },
            ({ externalModel: e }) => ({
              playUniqueVoice: e.createCallbackNoArgs("onPlayUniqueVoice"),
              changeVehicle: e.createCallbackNoArgs("onChangeVehicle"),
              onEditProfileClick: e.createCallbackNoArgs("onEditProfileClick"),
              retrain: e.createCallbackNoArgs("onRetrain"),
            }),
          ),
          S = y[0],
          N = y[1];
        var I = a(3457),
          T = a(3415),
          L = a(2056),
          x = a(5415),
          M = a(4828),
          P = a(1943),
          O = a(8018);
        const H = "CurrentVehicleTrain_base_22",
          W = "CurrentVehicleTrain_container_ae",
          G = "CurrentVehicleTrain_currentVehicle_9d",
          V = "CurrentVehicleTrain_currentVehicleName_19",
          z = "CurrentVehicleTrain_currentVehicleName__isPremium_86",
          Z = "CurrentVehicleTrain_retrainContainer_6a",
          j = "CurrentVehicleTrain_leftContainer_f4",
          $ = "CurrentVehicleTrain_rightContainer_60",
          U = "CurrentVehicleTrain_roleLevelContainer_95",
          X = "CurrentVehicleTrain_roleLevelLabel_31",
          q = "CurrentVehicleTrain_roleLevelLabel__red_0e",
          K = "CurrentVehicleTrain_retrainBtnContainer_00",
          Y = "CurrentVehicleTrain_discountIcon_04",
          Q = "CurrentVehicleTrain_discountIcon__forText_d9",
          J = "CurrentVehicleTrain_retrainBtn_3e",
          ee = "CurrentVehicleTrain_frameGlow_80",
          te = "CurrentVehicleTrain_trainLevelRateContainer_5c",
          ae = "CurrentVehicleTrain_trainLevelNumber_b0",
          ne = "CurrentVehicleTrain_trainLevelNumber__red_07",
          re = "CurrentVehicleTrain_trainLevelInfoIcon_27",
          ue = "CurrentVehicleTrain_discountContainer_24",
          se = "CurrentVehicleTrain_discountText_45";
        function ie() {
          return (
            (ie =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            ie.apply(this, arguments)
          );
        }
        const le = (0, o.Pi)(function ({ className: e }) {
          const t = N(),
            a = t.model,
            u = t.controls,
            i = (0, x.GS)().mediaSize,
            l = a.currentVehicle.get(),
            o = l.name,
            m = Boolean(o),
            d = a.computes.vehicleValidator().isWrongVehicle,
            _ = a.computes.discountTooltipArgs(),
            E = a.root.get(),
            g = E.hasRetrainDiscount,
            b = E.realRoleLevel,
            p = a.computes.isRoleLevelPenaltyActive(),
            v = (0, n.useContext)(Ge),
            h = (0, P.Sr)(M.D9, {
              item: M.sk.MstlTooltip,
              action: M.eX.Viewed,
              parentScreen: M.sC.PersonalFile,
            });
          return r().createElement(
            "div",
            { className: s()(H, e) },
            r().createElement(
              "div",
              { className: W },
              r().createElement(
                "div",
                { className: j },
                r().createElement(
                  L.u,
                  ie(
                    {
                      targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                      contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                      ignoreShowDelay: !0,
                      ignoreMouseClick: !0,
                    },
                    v ? h : void 0,
                  ),
                  r().createElement(
                    "div",
                    null,
                    r().createElement(c.w, {
                      classMix: G,
                      text: m
                        ? R.strings.crew.personalFile.inVehicle()
                        : R.strings.crew.common.inBarracks(),
                      binding: {
                        vehicle: r().createElement(
                          "div",
                          { className: s()(V, l.isPremium && z) },
                          o,
                        ),
                      },
                    }),
                  ),
                ),
              ),
              r().createElement(
                "div",
                { className: $ },
                r().createElement(
                  L.u,
                  ie(
                    {
                      targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                      contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                      ignoreShowDelay: !0,
                      ignoreMouseClick: !0,
                    },
                    v ? h : void 0,
                  ),
                  r().createElement(
                    "div",
                    { className: U },
                    r().createElement(
                      "div",
                      { className: s()(X, p && q) },
                      R.strings.crew.personalFile.retrainLevel(),
                    ),
                    r().createElement(
                      "div",
                      { className: te },
                      r().createElement("div", { className: s()(ae, p && ne) }, (0, O.T3)(b)),
                      !p && r().createElement("div", { className: re }),
                    ),
                  ),
                ),
                p &&
                  r().createElement(
                    T.l,
                    { tooltipArgs: _ },
                    r().createElement(
                      "div",
                      { className: Z },
                      r().createElement(
                        "div",
                        { className: K },
                        g && r().createElement("div", { className: Y }),
                        r().createElement(
                          I.u5,
                          { onClick: u.retrain, type: I.L$.secondary, mixClass: J },
                          d && r().createElement("div", { className: ee }),
                          R.strings.crew.personalFile.retrain(),
                        ),
                      ),
                    ),
                  ),
                g &&
                  !p &&
                  r().createElement(
                    T.l,
                    { tooltipArgs: _ },
                    r().createElement(
                      "div",
                      { className: ue },
                      r().createElement("div", { className: s()(Y, Q) }),
                      r().createElement(
                        "div",
                        { className: se },
                        i === x.cJ.ExtraSmall || i === x.cJ.Small
                          ? R.strings.crew.personalFile.discount.short()
                          : R.strings.crew.personalFile.discount.full(),
                      ),
                    ),
                  ),
              ),
            ),
          );
        });
        var oe = a(6373);
        const ce = "Name_base_2d",
          me = "Name_label_31",
          de = "Name_voiceButton_00",
          _e = "Name_soundIcon_2a",
          Ee = (0, o.Pi)(function ({ className: e }) {
            const t = N(),
              a = t.model,
              u = t.controls,
              l = a.root.get(),
              o = l.fullName,
              c = l.hasUniqueSound,
              m = (0, n.useCallback)(() => {
                u.playUniqueVoice();
              }, [u]);
            return r().createElement(
              "div",
              { className: s()(ce, e) },
              r().createElement(
                "div",
                null,
                r().createElement("div", { className: me }, r().createElement(i.ZP, { text: o })),
                c &&
                  r().createElement(
                    oe.i,
                    {
                      header: R.strings.crew.personalFile.voiceTooltip.header(),
                      body: R.strings.crew.personalFile.voiceTooltip.body(),
                    },
                    r().createElement(
                      I.u5,
                      { size: I.qE.extraSmall, type: I.L$.ghost, mixClass: de, onClick: m },
                      r().createElement("div", { className: _e }),
                    ),
                  ),
              ),
            );
          });
        var ge = a(7078),
          be = a(2603);
        const pe = "Role_base_e0",
          ve = "Role_role_2a",
          he = "Role_roleIcon_e6",
          Ae = "Role_roleName_79",
          Ce = "Role_commanderFeature_e2",
          fe = "Role_sense_21",
          De = "Role_commanderBonus_99",
          Fe = (0, n.memo)(({ role: e, isFemale: t, className: a, setIsFolderLight: n }) =>
            r().createElement(
              "div",
              { className: s()(pe, a) },
              r().createElement(
                ge.t,
                { args: { tooltipId: be.v$ }, targetId: We, ignoreShowDelay: !1 },
                r().createElement(
                  "div",
                  {
                    className: ve,
                    onMouseEnter: () => {
                      n && n(!0);
                    },
                    onMouseLeave: () => {
                      n && n(!1);
                    },
                  },
                  r().createElement("div", {
                    style: {
                      backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(e)})`,
                    },
                    className: he,
                  }),
                  r().createElement(
                    "div",
                    { className: Ae },
                    r().createElement(i.ZP, { text: (0, O.Gc)(e, t) }),
                  ),
                ),
              ),
              "commander" === e &&
                r().createElement(
                  "div",
                  { className: Ce },
                  r().createElement(
                    ge.t,
                    {
                      args: { skillName: "commander_sixthSense", tooltipId: be.HZ, level: 100 },
                      targetId: We,
                    },
                    r().createElement("div", { className: fe }),
                  ),
                  r().createElement(
                    ge.t,
                    { args: { tooltipId: be.uN }, targetId: We },
                    r().createElement("div", { className: De }),
                  ),
                ),
            ),
          );
        var Be = a(9690);
        const ke = {
          base: "SpecializationSlots_base_1a",
          frame: "SpecializationSlots_frame_85",
          frame__first: "SpecializationSlots_frame__first_23",
          arrowsIcon: "SpecializationSlots_arrowsIcon_fc",
          changeVehicle: "SpecializationSlots_changeVehicle_58",
          tier: "SpecializationSlots_tier_68",
          vehicle: "SpecializationSlots_vehicle_b6",
          vehicleTypeIcon: "SpecializationSlots_vehicleTypeIcon_77",
          info: "SpecializationSlots_info_7c",
          flag: "SpecializationSlots_flag_84",
          vehicleIcon: "SpecializationSlots_vehicleIcon_ec",
          premVehicle: "SpecializationSlots_premVehicle_c3",
        };
        function we() {
          return (
            (we =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var a = arguments[t];
                  for (var n in a) Object.prototype.hasOwnProperty.call(a, n) && (e[n] = a[n]);
                }
                return e;
              }),
            we.apply(this, arguments)
          );
        }
        const ye = ({ isCrewLocked: e, nativeVehicle: t, className: a, setIsFolderLight: u }) => {
            const i = (0, n.useContext)(Ge),
              l = (0, P.Sr)(M.D9, {
                item: M.sk.PremiumTooltip,
                action: M.eX.Viewed,
                parentScreen: M.sC.PersonalFile,
              }),
              o = (0, n.useCallback)(() => {
                u(!0);
              }, [u]),
              c = (0, n.useCallback)(() => u(!1), [u]),
              d = (0, n.useCallback)(
                (e) => ({
                  backgroundImage: `url(${R.images.gui.maps.icons.vehicleTypes.$dyn(e ? "c_48x48_elite" : "c_48x48_specSlot").$dyn((0, m.BN)(t.type))})`,
                }),
                [t.type],
              ),
              _ = {
                backgroundImage: `url(${R.images.gui.maps.icons.nations.c_155x31.$dyn(t.nation)})`,
              };
            return r().createElement(
              "div",
              { className: s()(ke.base, a) },
              r().createElement(
                oe.i,
                {
                  header: e
                    ? R.strings.crew.personalFile.crewLockedTooltip.header()
                    : R.strings.crew.personalFile.vehicleTooltip.header(),
                  body: e ? R.strings.crew.personalFile.crewLockedTooltip.body() : t.name,
                  ignoreMouseClick: e,
                },
                r().createElement(
                  "div",
                  {
                    id: "retraining_btn",
                    onMouseEnter: e ? void 0 : o,
                    onMouseLeave: e ? void 0 : c,
                    className: s()(ke.frame, ke.frame__first, e && ke.frame__crewLocked),
                  },
                  r().createElement("div", { style: _, className: ke.flag }),
                  r().createElement("div", {
                    style: {
                      backgroundImage: `url(${R.images.gui.maps.icons.vehicle.small.$dyn((0, m.BN)(`${t.nation}-${t.techName}`))})`,
                    },
                    className: ke.vehicleIcon,
                  }),
                  r().createElement(
                    "div",
                    { className: ke.info },
                    r().createElement("div", { className: ke.tier }, (0, Be.HG)(t.tier)),
                    r().createElement("div", {
                      style: d(t.isPremium),
                      className: ke.vehicleTypeIcon,
                    }),
                    r().createElement("div", { className: ke.vehicle }, t.name),
                  ),
                ),
              ),
              r().createElement(
                L.u,
                we(
                  {
                    targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                    contentId: R.views.lobby.crew.tooltips.PremiumVehicleTooltip("resId"),
                  },
                  i ? l : void 0,
                ),
                r().createElement(
                  "div",
                  { className: ke.frame },
                  r().createElement("div", { style: _, className: ke.flag }),
                  r().createElement(
                    "div",
                    { className: ke.info },
                    r().createElement("div", { style: d(!0), className: ke.vehicleTypeIcon }),
                    r().createElement(
                      "div",
                      { className: ke.premVehicle },
                      R.strings.crew.personalFile.premiumVehicle(),
                    ),
                  ),
                ),
              ),
            );
          },
          Se = "TankmanInfoApp_base_8a",
          Ne = "TankmanInfoApp_tankmanFolder_2d",
          Ie = "TankmanInfoApp_descriptionBlock_f2",
          Te = "TankmanInfoApp_role_71",
          Le = "TankmanInfoApp_name_68",
          xe = "TankmanInfoApp_description_a6",
          Re = "TankmanInfoApp_currentVehicle_06",
          Me = "TankmanInfoApp_nativeVehicle_5c",
          Pe = "TankmanInfoApp_nativeVehicle__withDescription_03",
          Oe = "TankmanInfoApp_slots_a1",
          He = (0, o.Pi)(({ className: e }) => {
            const t = N(),
              a = t.model,
              u = t.controls,
              o = a.root.get(),
              m = o.description,
              d = o.iconName,
              _ = o.isFemale,
              E = o.isCrewLocked,
              g = o.role,
              b = o.isInSkin,
              p = a.nativeVehicle.get(),
              v = Boolean(m),
              h = (0, n.useState)(!1),
              A = h[0],
              C = h[1],
              f = (0, n.useCallback)(() => {
                ((0, l.G)(R.sounds.yes1()), u.onEditProfileClick());
              }, [u]);
            return r().createElement(
              "div",
              { className: s()(Se, e) },
              r().createElement(B, {
                isFolderLight: A,
                name: d,
                isSkin: b,
                className: Ne,
                onClick: f,
              }),
              r().createElement(
                "div",
                { className: Ie },
                r().createElement(Fe, { className: Te, isFemale: _, role: g, setIsFolderLight: C }),
                r().createElement(Ee, { className: Le }),
                v &&
                  r().createElement(c.w, {
                    classMix: xe,
                    isTruncationAvailable: !0,
                    isTooltipEnable: !0,
                    targetId: R.views.lobby.crew.widgets.TankmanInfo("resId"),
                    text: m,
                  }),
                r().createElement(
                  "div",
                  { className: s()(Me, v && Pe) },
                  r().createElement(i.ZP, { text: R.strings.crew.personalFile.specialization() }),
                ),
                r().createElement(ye, {
                  nativeVehicle: p,
                  isCrewLocked: E,
                  className: Oe,
                  setIsFolderLight: C,
                }),
                r().createElement(le, { className: Re }),
              ),
            );
          }),
          We = R.views.lobby.crew.widgets.TankmanInfo("resId"),
          Ge = (0, n.createContext)(!1),
          Ve = r().memo(function ({ rootId: e = We, className: t, isLoggingEnabled: a = !1 }) {
            return r().createElement(
              S,
              { options: { rootId: e } },
              r().createElement(Ge.Provider, { value: a }, r().createElement(He, { className: t })),
            );
          });
      },
      8271: (e, t, a) => {
        "use strict";
        let n;
        (a.d(t, { W: () => n }),
          (function (e) {
            ((e.New = "new"),
              (e.Learned = "learned"),
              (e.Learning = "learning"),
              (e.Irrelevant = "irrelevant"),
              (e.Possible = "possible"),
              (e.ZeroSkill = "zeroSkill"));
          })(n || (n = {})));
      },
      2603: (e, t, a) => {
        "use strict";
        a.d(t, { HZ: () => n, Th: () => u, lu: () => s, uN: () => r, v$: () => i });
        const n = "crewPerkGf",
          r = "commanderBonus",
          u = "achievement",
          s = "crewSkin",
          i = "tankman";
      },
      5026: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
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
      6880: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
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
      8055: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
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
      5287: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = { base: "FormatText_base_d0" };
      },
      4769: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
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
      372: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          base: "HorizontalBar_base_49",
          base__nonActive: "HorizontalBar_base__nonActive_82",
          leftButton: "HorizontalBar_leftButton_5f",
          rightButton: "HorizontalBar_rightButton_03",
          track: "HorizontalBar_track_0d",
          thumb: "HorizontalBar_thumb_fd",
          rail: "HorizontalBar_rail_32",
        };
      },
      4682: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          base: "HorizontalScroll_base_29",
          wrapper: "HorizontalScroll_wrapper_1e",
          defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
        };
      },
      9168: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          base: "VerticalBar_base_f3",
          base__nonActive: "VerticalBar_base__nonActive_42",
          topButton: "VerticalBar_topButton_d7",
          bottomButton: "VerticalBar_bottomButton_06",
          track: "VerticalBar_track_df",
          thumb: "VerticalBar_thumb_32",
          rail: "VerticalBar_rail_43",
        };
      },
      5636: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          content: "VerticalScroll_content_cb",
          defaultScroll: "VerticalScroll_defaultScroll_f8",
          bar: "VerticalScroll_bar_1e",
          area: "VerticalScroll_area_af",
        };
      },
      3393: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
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
      6143: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          base: "ExtendedText_base_71",
          base__zeroPadding: "ExtendedText_base__zeroPadding_25",
          base__isTruncationAvailable: "ExtendedText_base__isTruncationAvailable_5b",
          truncated: "ExtendedText_truncated_97",
          truncated__hide: "ExtendedText_truncated__hide_31",
          unTruncated: "ExtendedText_unTruncated_b8",
        };
      },
      9627: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
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
      7629: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          noBreakWrapper: "renderers_noBreakWrapper_10",
          lineBreak: "renderers_lineBreak_b5",
          newLine: "renderers_newLine_bd",
        };
      },
      3938: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          base: "TankmanIcon_base_f9",
          base__big: "TankmanIcon_base__big_98",
          base__small: "TankmanIcon_base__small_b2",
          base__barracks: "TankmanIcon_base__barracks_62",
          base__special: "TankmanIcon_base__special_3f",
          base__c_204x256: "TankmanIcon_base__c_204x256_97",
          innerShadow: "TankmanIcon_innerShadow_c6",
        };
      },
      9426: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
          base: "TankmanSkill_base_84",
          base__big: "TankmanSkill_base__big_a0",
          bg: "TankmanSkill_bg_f9",
          icon: "TankmanSkill_icon_1b",
          icon__irrelevant: "TankmanSkill_icon__irrelevant_50",
        };
      },
      4723: (e, t, a) => {
        "use strict";
        a.d(t, { Z: () => n });
        const n = {
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
        for (l = 0; l < deferred.length; l++) {
          for (var [t, a, n] = deferred[l], u = !0, s = 0; s < t.length; s++)
            (!1 & n || r >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[s]))
              ? t.splice(s--, 1)
              : ((u = !1), n < r && (r = n));
          if (u) {
            deferred.splice(l--, 1);
            var i = a();
            void 0 !== i && (e = i);
          }
        }
        return e;
      }
      n = n || 0;
      for (var l = deferred.length; l > 0 && deferred[l - 1][2] > n; l--)
        deferred[l] = deferred[l - 1];
      deferred[l] = [t, a, n];
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
    (__webpack_require__.j = 904),
    (() => {
      var e = { 904: 0, 987: 0, 42: 0, 105: 0, 640: 0, 2: 0, 3: 0, 595: 0, 695: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, a) => {
          var n,
            r,
            [u, s, i] = a,
            l = 0;
          if (u.some((t) => 0 !== e[t])) {
            for (n in s) __webpack_require__.o(s, n) && (__webpack_require__.m[n] = s[n]);
            if (i) var o = i(__webpack_require__);
          }
          for (t && t(a); l < u.length; l++)
            ((r = u[l]), __webpack_require__.o(e, r) && e[r] && e[r][0](), (e[r] = 0));
          return __webpack_require__.O(o);
        },
        a = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (a.forEach(t.bind(null, 0)), (a.push = t.bind(null, a.push.bind(a))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(7362));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
