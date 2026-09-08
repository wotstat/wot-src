(() => {
  var __webpack_modules__ = {
      3779: (e, t, u) => {
        "use strict";
        u.d(t, { ZP: () => A });
        var n = u(6483),
          a = u.n(n),
          r = u(9887),
          o = u.n(r),
          s = u(3377),
          i = u(6179),
          l = u.n(i),
          c = u(5026);
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
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        Object.keys(o());
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
          A = (0, s.ZP)((e) => {
            let t = e.className,
              u = e.width,
              n = e.height,
              r = e.m,
              o = e.mt,
              s = void 0 === o ? r : o,
              A = e.mr,
              p = void 0 === A ? r : A,
              C = e.mb,
              F = void 0 === C ? r : C,
              h = e.ml,
              b = void 0 === h ? r : h,
              v = e.column,
              D = e.row,
              B = e.flexDirection,
              f = void 0 === B ? (v ? "column" : D && "row") || void 0 : B,
              w = e.flexStart,
              y = e.center,
              k = e.flexEnd,
              S = e.spaceBetween,
              L = e.spaceAround,
              x = e.justifyContent,
              I =
                void 0 === x
                  ? (w ? "flex-start" : y && "center") ||
                    (k && "flex-end") ||
                    (S && "space-between") ||
                    (L && "space-around") ||
                    void 0
                  : x,
              N = e.alignItems,
              T =
                void 0 === N
                  ? (w ? "flex-start" : y && "center") || (k && "flex-end") || void 0
                  : N,
              M = e.alignSelf,
              R = e.wrap,
              P = e.flexWrap,
              O = void 0 === P ? (R ? "wrap" : void 0) : P,
              H = e.grow,
              W = e.shrink,
              G = e.flex,
              j = void 0 === G ? (H || W ? `${H ? 1 : 0} ${W ? 1 : 0} auto` : void 0) : G,
              z = e.style,
              U = e.children,
              $ = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, m);
            const Z = (0, i.useMemo)(() => {
                const e = { mt: s, mr: p, mb: F, ml: b },
                  t = ((e) =>
                    E.reduce((t, u) => {
                      const n = e[u];
                      return n && "number" != typeof n ? t.concat(_[!0 === n ? "MD" : n][u]) : t;
                    }, []))(e),
                  a = ((e) =>
                    E.reduce((t, u) => {
                      const n = e[u];
                      return ("number" == typeof n && (t[g[u]] = n + "rem"), t);
                    }, {}))(e);
                return {
                  computedStyle: Object.assign({}, z, a, {
                    width: void 0 !== u && "number" == typeof u ? u + "rem" : u,
                    height: void 0 !== n && "number" == typeof n ? n + "rem" : n,
                    flex: j,
                    alignSelf: M,
                    display: f || T ? "flex" : void 0,
                    flexDirection: f,
                    flexWrap: O,
                    justifyContent: I,
                    alignItems: T,
                  }),
                  computedClassNames: t,
                };
              }, [u, n, s, p, F, b, z, j, M, f, O, I, T]),
              V = Z.computedStyle,
              X = Z.computedClassNames;
            return l().createElement(
              "div",
              d({ className: a()(c.Z.base, ...X, t), style: V }, $),
              U,
            );
          });
      },
      3457: (e, t, u) => {
        "use strict";
        u.d(t, { L$: () => l.L, qE: () => l.q, u5: () => m });
        var n = u(6483),
          a = u.n(n),
          r = u(7727),
          o = u(6179),
          s = u.n(o),
          i = u(6880),
          l = u(2106);
        const c = ({
          children: e,
          size: t,
          isFocused: u,
          type: n,
          disabled: c,
          mixClass: m,
          soundHover: d,
          soundClick: _,
          onMouseEnter: E,
          onMouseMove: g,
          onMouseDown: A,
          onMouseUp: p,
          onMouseLeave: C,
          onClick: F,
        }) => {
          const h = (0, o.useRef)(null),
            b = (0, o.useState)(u),
            v = b[0],
            D = b[1],
            B = (0, o.useState)(!1),
            f = B[0],
            w = B[1],
            y = (0, o.useState)(!1),
            k = y[0],
            S = y[1],
            L = (0, o.useCallback)(() => {
              c || (h.current && (h.current.focus(), D(!0)));
            }, [c]),
            x = (0, o.useCallback)(
              (e) => {
                v && null !== h.current && !h.current.contains(e.target) && D(!1);
              },
              [v],
            ),
            I = (0, o.useCallback)(
              (e) => {
                c || (F && F(e));
              },
              [c, F],
            ),
            N = (0, o.useCallback)(
              (e) => {
                c || (null !== d && (0, r.G)(d), E && E(e), S(!0));
              },
              [c, d, E],
            ),
            T = (0, o.useCallback)(
              (e) => {
                g && g(e);
              },
              [g],
            ),
            M = (0, o.useCallback)(
              (e) => {
                c || (p && p(e), w(!1));
              },
              [c, p],
            ),
            P = (0, o.useCallback)(
              (e) => {
                c || (null !== _ && (0, r.G)(_), A && A(e), u && L(), w(!0));
              },
              [c, _, A, L, u],
            ),
            O = (0, o.useCallback)(
              (e) => {
                c || (C && C(e), w(!1));
              },
              [c, C],
            ),
            H = a()(
              i.Z.base,
              i.Z[`base__${n}`],
              {
                [i.Z.base__disabled]: c,
                [i.Z[`base__${t}`]]: t,
                [i.Z.base__focus]: v,
                [i.Z.base__highlightActive]: f,
                [i.Z.base__firstHover]: k,
              },
              m,
            ),
            W = a()(i.Z.state, i.Z.state__default);
          return (
            (0, o.useEffect)(
              () => (
                document.addEventListener("mousedown", x),
                () => {
                  document.removeEventListener("mousedown", x);
                }
              ),
              [x],
            ),
            (0, o.useEffect)(() => {
              D(u);
            }, [u]),
            s().createElement(
              "div",
              {
                ref: h,
                className: H,
                onMouseEnter: N,
                onMouseMove: T,
                onMouseUp: M,
                onMouseDown: P,
                onMouseLeave: O,
                onClick: I,
              },
              n !== l.L.ghost &&
                s().createElement(
                  s().Fragment,
                  null,
                  s().createElement("div", { className: i.Z.back }),
                  s().createElement("span", { className: i.Z.texture }),
                ),
              s().createElement(
                "span",
                { className: W },
                s().createElement("span", { className: i.Z.stateDisabled }),
                s().createElement("span", { className: i.Z.stateHighlightHover }),
                s().createElement("span", { className: i.Z.stateHighlightActive }),
              ),
              s().createElement(
                "span",
                { className: i.Z.content, lang: R.strings.settings.LANGUAGE_CODE() },
                e,
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
        const m = (0, o.memo)(c);
      },
      2106: (e, t, u) => {
        "use strict";
        let n, a;
        (u.d(t, { L: () => n, q: () => a }),
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
          })(a || (a = {})));
      },
      9987: (e, t, u) => {
        "use strict";
        u.d(t, { A: () => c });
        var n = u(6483),
          a = u.n(n),
          r = u(6179),
          o = u.n(r),
          s = u(8055);
        const i = [
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
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            l.apply(this, arguments)
          );
        }
        const c = (e) => {
          let t = e.size,
            u = e.value,
            n = e.isEmpty,
            r = e.fadeInAnimation,
            c = e.hide,
            m = e.maximumNumber,
            d = e.className,
            _ = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, i);
          const E = n ? null : u,
            g = "string" == typeof E;
          if ((E && !g && E < 0) || 0 === E) return null;
          const A = E && !g && E > m,
            p = a()(
              s.Z.base,
              s.Z[`base__${t}`],
              r && s.Z.base__animated,
              c && s.Z.base__hidden,
              !E && s.Z.base__pattern,
              n && s.Z.base__empty,
              d,
            );
          return o().createElement(
            "div",
            l({ className: p }, _),
            o().createElement("div", { className: s.Z.bg }),
            o().createElement("div", { className: s.Z.pattern }),
            o().createElement(
              "div",
              { className: a()(s.Z.value, g && s.Z.value__text) },
              A ? m : E,
              A && o().createElement("span", { className: s.Z.plus }, "+"),
            ),
          );
        };
        c.defaultProps = { size: "normal", fadeInAnimation: !1, hide: !1, maximumNumber: 99 };
      },
      280: (e, t, u) => {
        "use strict";
        u.d(t, { z: () => l });
        var n = u(6179),
          a = u.n(n),
          r = u(6483),
          o = u.n(r),
          s = u(3649),
          i = u(5287);
        const l = ({ binding: e, text: t = "", classMix: u, alignment: r = s.v2.left }) =>
          null === t
            ? (console.error("FormatText was supplied with 'null'"), null)
            : a().createElement(
                n.Fragment,
                null,
                t.split("\n").map((t, l) =>
                  a().createElement(
                    "div",
                    { className: o()(i.Z.base, u), key: `${t}-${l}` },
                    (0, s.Uw)(t, r, e).map((e, t) =>
                      a().createElement(n.Fragment, { key: `${t}-${e}` }, e),
                    ),
                  ),
                ),
              );
      },
      3495: (e, t, u) => {
        "use strict";
        u.d(t, { Y: () => m });
        var n = u(3138),
          a = u(6179),
          r = u(1043),
          o = u(5262);
        const s = n.O.client.getSize("rem"),
          i = s.width,
          l = s.height,
          c = Object.assign({ width: i, height: l }, (0, o.T)(i, l, r.j)),
          m = (0, a.createContext)(c);
      },
      1039: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => c });
        var n = u(6179),
          a = u.n(n),
          r = u(6536),
          o = u(3495),
          s = u(1043),
          i = u(5262),
          l = u(3138);
        const c = (0, n.memo)(({ children: e }) => {
          const t = (0, n.useContext)(o.Y),
            u = (0, n.useState)(t),
            c = u[0],
            m = u[1],
            d = (0, n.useCallback)((e, t) => {
              const u = l.O.view.pxToRem(e),
                n = l.O.view.pxToRem(t);
              m(Object.assign({ width: u, height: n }, (0, i.T)(u, n, s.j)));
            }, []);
          ((0, r.Z)(() => {
            engine.on("clientResized", d);
          }),
            (0, n.useEffect)(() => () => engine.off("clientResized", d), [d]));
          const _ = (0, n.useMemo)(() => Object.assign({}, c), [c]);
          return a().createElement(o.Y.Provider, { value: _ }, e);
        });
      },
      6010: (e, t, u) => {
        "use strict";
        var n = u(6179),
          a = u(7382),
          r = u(3495);
        const o = ["children"];
        const s = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, o);
          const s = (0, n.useContext)(r.Y),
            i = s.extraLarge,
            l = s.large,
            c = s.medium,
            m = s.small,
            d = s.extraSmall,
            _ = s.extraLargeWidth,
            E = s.largeWidth,
            g = s.mediumWidth,
            A = s.smallWidth,
            p = s.extraSmallWidth,
            C = s.extraLargeHeight,
            F = s.largeHeight,
            h = s.mediumHeight,
            b = s.smallHeight,
            v = s.extraSmallHeight,
            D = { extraLarge: C, large: F, medium: h, small: b, extraSmall: v };
          if (u.extraLarge || u.large || u.medium || u.small || u.extraSmall) {
            if (u.extraLarge && i) return t;
            if (u.large && l) return t;
            if (u.medium && c) return t;
            if (u.small && m) return t;
            if (u.extraSmall && d) return t;
          } else {
            if (u.extraLargeWidth && _) return (0, a.H)(t, u, D);
            if (u.largeWidth && E) return (0, a.H)(t, u, D);
            if (u.mediumWidth && g) return (0, a.H)(t, u, D);
            if (u.smallWidth && A) return (0, a.H)(t, u, D);
            if (u.extraSmallWidth && p) return (0, a.H)(t, u, D);
            if (!(
              u.extraLargeWidth ||
              u.largeWidth ||
              u.mediumWidth ||
              u.smallWidth ||
              u.extraSmallWidth
            )) {
              if (u.extraLargeHeight && C) return t;
              if (u.largeHeight && F) return t;
              if (u.mediumHeight && h) return t;
              if (u.smallHeight && b) return t;
              if (u.extraSmallHeight && v) return t;
            }
          }
          return null;
        };
        s.defaultProps = {
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
        (0, n.memo)(s);
      },
      7382: (e, t, u) => {
        "use strict";
        u.d(t, { H: () => n });
        const n = (e, t, u) =>
          t.extraLargeHeight ||
          t.largeHeight ||
          t.mediumHeight ||
          t.smallHeight ||
          t.extraSmallHeight
            ? (t.extraLargeHeight && u.extraLarge) ||
              (t.largeHeight && u.large) ||
              (t.mediumHeight && u.medium) ||
              (t.smallHeight && u.small) ||
              (t.extraSmallHeight && u.extraSmall)
              ? e
              : null
            : e;
      },
      7739: (e, t, u) => {
        "use strict";
        u.d(t, { YN: () => a.Y, ZN: () => n.Z });
        u(6010);
        var n = u(1039),
          a = u(3495);
      },
      1043: (e, t, u) => {
        "use strict";
        u.d(t, { j: () => n });
        const n = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (e, t, u) => {
        "use strict";
        var n;
        function a(e, t, u) {
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
            })(e, u),
            a = (function (e, t) {
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
            })(t, u),
            r = Math.min(n, a);
          return {
            extraLarge: r === u.extraLarge.weight,
            large: r === u.large.weight,
            medium: r === u.medium.weight,
            small: r === u.small.weight,
            extraSmall: r === u.extraSmall.weight,
            extraLargeWidth: n === u.extraLarge.weight,
            largeWidth: n === u.large.weight,
            mediumWidth: n === u.medium.weight,
            smallWidth: n === u.small.weight,
            extraSmallWidth: n === u.extraSmall.weight,
            extraLargeHeight: a === u.extraLarge.weight,
            largeHeight: a === u.large.weight,
            mediumHeight: a === u.medium.weight,
            smallHeight: a === u.small.weight,
            extraSmallHeight: a === u.extraSmall.weight,
          };
        }
        (u.d(t, { T: () => a }),
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
      1037: (e, t, u) => {
        "use strict";
        u.d(t, { IC: () => n });
        var n,
          a = u(6483),
          r = u.n(a),
          o = u(6373),
          s = u(1856),
          i = u(3138),
          l = u(2039),
          c = u(5099),
          m = u(7727),
          d = u(4179),
          _ = u(6179),
          E = u.n(_),
          g = u(4769);
        !(function (e) {
          ((e[(e.Left = 0)] = "Left"),
            (e[(e.Right = 1)] = "Right"),
            (e[(e.Top = 2)] = "Top"),
            (e[(e.Bottom = 3)] = "Bottom"));
        })(n || (n = {}));
        const A = ["__left", "__right", "__top", "__bottom"];
        (0, _.forwardRef)(
          (
            { children: e, disableAutoSizeUpdate: t, onOutsideClick: u, customStyles: n = {} },
            a,
          ) => {
            const p = (0, _.useRef)(null),
              C = (0, _.useRef)(null),
              F = (0, _.useRef)(null),
              h = (0, _.useState)(window.decorator && window.decorator.directionType),
              b = h[0],
              v = h[1],
              D = (0, _.useCallback)(() => {
                (m.$.playClick(), i.O.view.sendEvent.close());
              }, []),
              B = (0, _.useCallback)(() => {
                m.$.playHighlight();
              }, []),
              f = r()(g.Z.arrow, g.Z[`arrow${A[b]}`]);
            (0, l.b)(
              () => (
                i.O.client.events.mouse.enableOutside(),
                i.O.client.events.mouse.down(([, e]) => {
                  "outside" === e && (u ? u() : i.O.view.sendEvent.close("popover"));
                })
              ),
            );
            const w = (0, _.useCallback)(
                (e) => {
                  let t = e.target;
                  do {
                    if (t === p.current || t === F.current) return;
                    t = t.parentNode;
                  } while (t);
                  const n = window.decorator;
                  if (void 0 !== window.decorator) {
                    const e = i.O.client.getMouseGlobalPosition(),
                      t = ![n.boundX, n.boundY, n.boundWidth, n.boundHeight].includes(void 0),
                      u =
                        e.x < n.boundX ||
                        e.x > n.boundX + n.boundWidth ||
                        e.y > n.boundY + n.boundHeight ||
                        e.y < n.boundY;
                    if (t && !u) return;
                  }
                  u ? u() : i.O.view.sendEvent.close("popover");
                },
                [p, F, u],
              ),
              y = (0, _.useCallback)(
                () => (
                  i.O.view.freezeTextureBeforeResize(),
                  (0, s.v)(() => {
                    if (C.current) {
                      const e = C.current.scrollWidth,
                        t = C.current.scrollHeight;
                      (i.O.view.resize(e, t), v(window.decorator.directionType));
                    }
                  })
                ),
                [],
              );
            return (
              (0, _.useImperativeHandle)(a, () => ({ updateSize: y })),
              (0, l.b)(() => {
                i.O.view.setInputPaddingsRem(58);
              }),
              (0, _.useEffect)(() => {
                document.addEventListener("mousedown", w, { capture: !0 });
                const e = (0, c.B)((0, d.Eu)());
                return (
                  !t && e.promise.then(() => y()),
                  () => {
                    (e.cancel(), document.removeEventListener("mousedown", w));
                  }
                );
              }, [y, w, t]),
              E().createElement(
                "div",
                { className: g.Z.base, ref: C },
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
                        o.i,
                        { body: R.strings.dialogs.common.error.cancel() },
                        E().createElement("div", {
                          className: g.Z.closeBtn,
                          onClick: D,
                          onMouseEnter: B,
                          ref: F,
                        }),
                      ),
                  ),
                  E().createElement("div", { className: f, style: n.arrow }),
                ),
              )
            );
          },
        );
      },
      3616: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => l });
        var n = u(1037),
          a = u(4179),
          r = u(6179),
          o = u.n(r);
        const s = [
          "contentId",
          "decoratorId",
          "direction",
          "targetId",
          "args",
          "onClick",
          "children",
          "isEnabled",
        ];
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = (e) => {
          let t = e.contentId,
            u = e.decoratorId,
            l = e.direction,
            c = void 0 === l ? n.IC.Top : l,
            m = e.targetId,
            d = e.args,
            _ = e.onClick,
            E = e.children,
            g = e.isEnabled,
            A = void 0 === g || g,
            p = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, s);
          const C = (0, r.useRef)(null),
            F = (0, r.useCallback)(() => {
              if ((0, a.wU)()) return (0, a.SW)();
              C.current && (0, a.P3)(t, c, C.current, u, m, d);
            }, [t, c, d, u, m]);
          return o().createElement(
            "div",
            i(
              {
                ref: C,
                onClick:
                  ((h = E.props.onClick),
                  (e) => {
                    A && (F(), _ && _(e), h && h(e));
                  }),
              },
              p,
            ),
            E,
          );
          var h;
        };
      },
      7613: (e, t, u) => {
        "use strict";
        u.d(t, { ZP: () => B });
        var n = u(6483),
          a = u.n(n),
          r = u(3779),
          o = u(280),
          s = u(3532),
          i = u.n(s),
          l = u(9887),
          c = u.n(l),
          m = u(3377),
          d = u(6179),
          _ = u.n(d),
          E = u(3393);
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
        function A() {
          return (
            (A =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            A.apply(this, arguments)
          );
        }
        Object.keys(c());
        const p = Object.keys(i()),
          C = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          F = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          h = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          b = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          v =
            (Object.keys(b),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": C,
              "heading-H36": C,
              "heading-H28": F,
              "heading-H24": F,
              "heading-H24R": F,
              "heading-H22": F,
              "heading-H20R": F,
              "heading-H18": F,
              "heading-H15": h,
              "heading-H14": h,
              "paragraph-P24": F,
              "paragraph-P18": F,
              "paragraph-P16": F,
              "paragraph-P14": h,
              "paragraph-P12": h,
              "paragraph-P10": h,
            }),
          D =
            (Object.keys(v),
            (e) =>
              e
                ? ((e) => p.includes(e))(e)
                  ? { colorClassName: E.Z[e] }
                  : { colorStyle: { color: e } }
                : {}),
          B = (0, m.ZP)((e) => {
            let t = e.text,
              u = e.variant,
              n = e.className,
              s = e.color,
              i = e.m,
              l = e.mt,
              c = void 0 === l ? i : l,
              m = e.mr,
              p = void 0 === m ? i : m,
              C = e.mb,
              F = void 0 === C ? i : C,
              h = e.ml,
              b = void 0 === h ? i : h,
              B = e.style,
              f = e.format,
              w = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, g);
            const y = (0, d.useMemo)(() => {
                const e = D(s),
                  t = e.colorClassName,
                  u = e.colorStyle,
                  n = void 0 === u ? {} : u;
                return { computedStyle: Object.assign({}, B, n), colorClassName: t };
              }, [B, s]),
              k = y.computedStyle,
              S = y.colorClassName;
            return _().createElement(
              r.ZP,
              A(
                {
                  className: a()(E.Z.base, u && E.Z[u], S, n),
                  style: k,
                  mt: !0 === c ? v[u || "paragraph-P16"].mt : c,
                  mr: !0 === p ? v[u || "paragraph-P16"].mr : p,
                  mb: !0 === F ? v[u || "paragraph-P16"].mb : F,
                  ml: !0 === b ? v[u || "paragraph-P16"].ml : b,
                },
                w,
              ),
              void 0 !== f ? _().createElement(o.z, A({}, f, { text: t })) : t,
            );
          });
      },
      7078: (e, t, u) => {
        "use strict";
        u.d(t, { t: () => i });
        var n = u(6179),
          a = u.n(n),
          r = u(2056);
        const o = ["children"];
        function s() {
          return (
            (s =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            s.apply(this, arguments)
          );
        }
        const i = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, o);
          return a().createElement(
            r.u,
            s(
              {
                contentId:
                  R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                    "resId",
                  ),
                ignoreShowDelay: !0,
              },
              u,
            ),
            t,
          );
        };
      },
      3415: (e, t, u) => {
        "use strict";
        u.d(t, { l: () => l });
        var n = u(6179),
          a = u.n(n),
          r = u(7078),
          o = u(6373),
          s = u(2056);
        function i() {
          return (
            (i =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            i.apply(this, arguments)
          );
        }
        const l = ({ children: e, tooltipArgs: t, className: u }) => {
          if (!t) return e;
          const n = a().createElement("div", { className: u }, e);
          if (t.header || t.body) return a().createElement(o.i, t, n);
          const l = t.contentId,
            c = t.args,
            m = null == c ? void 0 : c.contentId;
          return l || m
            ? a().createElement(s.u, i({}, t, { contentId: l || m }), n)
            : a().createElement(r.t, t, n);
        };
      },
      6373: (e, t, u) => {
        "use strict";
        u.d(t, { i: () => l });
        var n = u(2056),
          a = u(6179),
          r = u.n(a);
        const o = ["children", "body", "header", "note", "alert", "args"];
        function s() {
          return (
            (s =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            s.apply(this, arguments)
          );
        }
        const i = R.views.common.tooltip_window.simple_tooltip_content,
          l = (e) => {
            let t = e.children,
              u = e.body,
              l = e.header,
              c = e.note,
              m = e.alert,
              d = e.args,
              _ = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, o);
            const E = (0, a.useMemo)(() => {
              const e = Object.assign({}, d, { body: u, header: l, note: c, alert: m });
              for (const t in e) void 0 === e[t] && delete e[t];
              return e;
            }, [m, u, l, c, d]);
            return r().createElement(
              n.u,
              s(
                {
                  contentId:
                    ((g = null == d ? void 0 : d.hasHtmlContent),
                    g ? i.SimpleTooltipHtmlContent("resId") : i.SimpleTooltipContent("resId")),
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
      2056: (e, t, u) => {
        "use strict";
        u.d(t, { u: () => l });
        var n = u(7902),
          a = u(4179),
          r = u(6179);
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
        function s(e) {
          return Object.entries(e || {}).map(([e, t]) => {
            const u = { __Type: "GFValueProxy", name: e };
            switch (typeof t) {
              case "number":
                u.number = t;
                break;
              case "boolean":
                u.bool = t;
                break;
              case "undefined":
                break;
              default:
                u.string = t.toString();
            }
            return u;
          });
        }
        const i = (e, t, u = {}, n = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: a.B0.TOOLTIP,
                  contentID: e,
                  decoratorID: t,
                  targetID: n,
                },
                u,
              ),
            );
          },
          l = (e) => {
            let t = e.children,
              u = e.contentId,
              a = e.args,
              l = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onClick,
              _ = e.ignoreShowDelay,
              E = void 0 !== _ && _,
              g = e.ignoreMouseClick,
              A = void 0 !== g && g,
              p = e.decoratorId,
              C = void 0 === p ? 0 : p,
              F = e.isEnabled,
              h = void 0 === F || F,
              b = e.targetId,
              v = void 0 === b ? 0 : b,
              D = e.onShow,
              B = e.onHide,
              f = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, o);
            const w = (0, r.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              y = (0, r.useMemo)(() => v || (0, n.F)().resId, [v]),
              k = (0, r.useCallback)(() => {
                (w.current.isVisible && w.current.timeoutId) ||
                  (i(u, C, { isMouseEvent: !0, on: !0, arguments: s(a) }, y),
                  D && D(),
                  (w.current.isVisible = !0));
              }, [u, C, a, y, D]),
              S = (0, r.useCallback)(() => {
                if (w.current.isVisible || w.current.timeoutId) {
                  const e = w.current.timeoutId;
                  (e > 0 && (clearTimeout(e), (w.current.timeoutId = 0)),
                    i(u, C, { on: !1 }, y),
                    w.current.isVisible && B && B(),
                    (w.current.isVisible = !1));
                }
              }, [u, C, y, B]),
              L = (0, r.useCallback)((e) => {
                w.current.isVisible &&
                  ((w.current.prevTarget = document.elementFromPoint(e.clientX, e.clientY)),
                  (w.current.hideTimerId = window.setTimeout(() => {
                    const t = document.elementFromPoint(e.clientX, e.clientY);
                    t && !t.isSameNode(w.current.prevTarget) && S();
                  }, 200)));
              }, []);
            ((0, r.useEffect)(() => {
              const e = w.current.hideTimerId;
              return (
                document.addEventListener("wheel", L, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", L, { capture: !0 }),
                    e && window.clearTimeout(e));
                }
              );
            }, []),
              (0, r.useEffect)(() => {
                !1 === h && S();
              }, [h, S]),
              (0, r.useEffect)(
                () => (
                  window.addEventListener("mouseleave", S),
                  () => {
                    (window.removeEventListener("mouseleave", S), S());
                  }
                ),
                [S],
              ));
            return h
              ? (0, r.cloneElement)(
                  t,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((x = t.props.onMouseEnter),
                        (e) => {
                          (e.clientX === window.innerWidth && e.clientY === window.innerHeight) ||
                            ((w.current.timeoutId = window.setTimeout(k, E ? 100 : 400)),
                            l && l(e),
                            x && x(e));
                        }),
                      onMouseLeave: ((e) => (t) => {
                        (S(), null == c || c(t), null == e || e(t));
                      })(t.props.onMouseLeave),
                      onClick: ((e) => (t) => {
                        (!1 === A && S(), null == d || d(t), null == e || e(t));
                      })(t.props.onClick),
                      onMouseDown: ((e) => (t) => {
                        (!1 === A && S(), null == m || m(t), null == e || e(t));
                      })(t.props.onMouseDown),
                    },
                    f,
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
      1856: (e, t, u) => {
        "use strict";
        u.d(t, { v: () => n });
        const n = (e) => {
          let t,
            u = null;
          return (
            (u = requestAnimationFrame(() => {
              u = requestAnimationFrame(() => {
                ((u = null), (t = e()));
              });
            })),
            () => {
              ("function" == typeof t && t(), null !== u && cancelAnimationFrame(u));
            }
          );
        };
      },
      8246: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => s });
        var n = u(3138);
        function a(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return r(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return r(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function r(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        const o = (e) => (0 === e ? window : window.subViews.get(e));
        function s({
          initializer: e = !0,
          rootId: t = 0,
          getRoot: u = o,
          context: r = "model",
        } = {}) {
          const s = new Map();
          function i(e, t = 0) {
            viewEnv.removeDataChangedCallback(e, t)
              ? s.delete(e)
              : console.error("Can't remove callback by id:", e);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (e, t, u) => {
              u.forEach((t) => {
                const u = s.get(t);
                void 0 !== u && u(e);
              });
            });
          });
          const l = (e) => {
            const n = u(t),
              a = r.split(".").reduce((e, t) => e[t], n);
            return "string" != typeof e || 0 === e.length
              ? a
              : e.split(".").reduce((e, t) => {
                  const u = e[t];
                  return "function" == typeof u ? u.bind(e) : u;
                }, a);
          };
          return {
            subscribe: (u, a) => {
              const o = "string" == typeof a ? `${r}.${a}` : r,
                i = n.O.view.addModelObserver(o, t, !0);
              return (s.set(i, u), e && u(l(a)), i);
            },
            readByPath: l,
            createCallback: (e, t) => {
              const u = l(t);
              return (...t) => {
                u(e(...t));
              };
            },
            createCallbackNoArgs: (e) => {
              const t = l(e);
              return () => {
                t();
              };
            },
            dispose: function () {
              for (var e, u = a(s.keys()); !(e = u()).done;) {
                i(e.value, t);
              }
            },
            unsubscribe: i,
          };
        }
      },
      3215: (e, t, u) => {
        "use strict";
        u.d(t, { q: () => i });
        var n = u(4598),
          a = u(9174),
          r = u(6179),
          o = u.n(r),
          s = u(8246);
        const i = () => (e, t) => {
          const u = (0, r.createContext)({});
          return [
            function ({ mode: i = "real", options: l, children: c, mocks: m }) {
              const d = (0, r.useRef)([]),
                _ = (u, r, o) => {
                  var i;
                  const l = s.U(r),
                    c =
                      "real" === u
                        ? l
                        : Object.assign({}, l, {
                            readByPath: null != (i = null == o ? void 0 : o.getter) ? i : () => {},
                          }),
                    m = (e) =>
                      "mocks" === u ? (null == o ? void 0 : o.getter(e)) : c.readByPath(e),
                    _ = (e) => d.current.push(e),
                    E = e({
                      mode: u,
                      readByPath: m,
                      externalModel: c,
                      observableModel: {
                        array: (e, t) => {
                          const r = null != t ? t : m(e),
                            o = a.LO.box(r, { equals: n.jv });
                          return (
                            "real" === u &&
                              c.subscribe(
                                (0, a.aD)((e) => o.set(e)),
                                e,
                              ),
                            o
                          );
                        },
                        object: (e, t) => {
                          const r = null != t ? t : m(e),
                            o = a.LO.box(r, { equals: n.jv });
                          return (
                            "real" === u &&
                              c.subscribe(
                                (0, a.aD)((e) => o.set(e)),
                                e,
                              ),
                            o
                          );
                        },
                        primitives: (e, t) => {
                          const n = m(t);
                          if (Array.isArray(e)) {
                            const r = e.reduce((e, t) => ((e[t] = a.LO.box(n[t], {})), e), {});
                            return (
                              "real" === u &&
                                c.subscribe(
                                  (0, a.aD)((t) => {
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
                              o = Object.entries(r),
                              s = o.reduce((e, [t, u]) => ((e[u] = a.LO.box(n[t], {})), e), {});
                            return (
                              "real" === u &&
                                c.subscribe(
                                  (0, a.aD)((e) => {
                                    o.forEach(([t, u]) => {
                                      s[u].set(e[t]);
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
                    g = { mode: u, model: E, externalModel: c, cleanup: _ };
                  return {
                    model: E,
                    controls: "mocks" === u && o ? o.controls(g) : t(g),
                    externalModel: c,
                    mode: u,
                  };
                },
                E = (0, r.useRef)(!1),
                g = (0, r.useState)(i),
                A = g[0],
                p = g[1],
                C = (0, r.useState)(() => _(i, l, m)),
                F = C[0],
                h = C[1];
              return (
                (0, r.useEffect)(() => {
                  E.current ? h(_(A, l, m)) : (E.current = !0);
                }, [m, A, l]),
                (0, r.useEffect)(() => {
                  p(i);
                }, [i]),
                (0, r.useEffect)(
                  () => () => {
                    (F.externalModel.dispose(), d.current.forEach((e) => e()));
                  },
                  [F],
                ),
                o().createElement(u.Provider, { value: F }, c)
              );
            },
            () => (0, r.useContext)(u),
          ];
        };
      },
      527: (e, t, u) => {
        "use strict";
        (u.r(t), u.d(t, { mouse: () => s, onResize: () => r }));
        var n = u(2472),
          a = u(1176);
        const r = (0, n.E)("clientResized"),
          o = { down: (0, n.E)("mousedown"), up: (0, n.E)("mouseup"), move: (0, n.E)("mousemove") };
        const s = (function () {
          const e = { listeners: 0, enabled: !0, initialized: !1 };
          function t() {
            e.enabled && (0, a.R)(!1);
          }
          function u() {
            e.enabled && (0, a.R)(!0);
          }
          function n() {
            e.enabled
              ? e.listeners < 1
                ? ((e.initialized = !1),
                  document.body.removeEventListener("mouseenter", t),
                  document.body.removeEventListener("mouseleave", u))
                : e.initialized ||
                  ((e.initialized = !0),
                  document.body.addEventListener("mouseenter", t),
                  document.body.addEventListener("mouseleave", u))
              : (0, a.R)(!1);
          }
          const r = ["down", "up", "move"].reduce(
            (t, u) => (
              (t[u] = (function (t) {
                return (u) => {
                  e.listeners += 1;
                  let a = !0;
                  const r = `mouse${t}`,
                    s = o[t]((e) => u([e, "outside"]));
                  function i(e) {
                    u([e, "inside"]);
                  }
                  return (
                    window.addEventListener(r, i),
                    n(),
                    () => {
                      a &&
                        (s(), window.removeEventListener(r, i), (e.listeners -= 1), n(), (a = !1));
                    }
                  );
                };
              })(u)),
              t
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((e.enabled = !1), n());
            },
            enable() {
              ((e.enabled = !0), n());
            },
            enableOutside() {
              e.enabled && (0, a.R)(!0);
            },
            disableOutside() {
              e.enabled && (0, a.R)(!1);
            },
          });
        })();
      },
      5959: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            events: () => n,
            getMouseGlobalPosition: () => r,
            getSize: () => a,
            graphicsQuality: () => o,
          }));
        var n = u(527);
        function a(e = "px") {
          return "rem" === e ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(e = "px") {
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
      1176: (e, t, u) => {
        "use strict";
        function n(e) {
          viewEnv.setTrackMouseOnStage(e);
        }
        u.d(t, { R: () => n });
      },
      2472: (e, t, u) => {
        "use strict";
        function n(e) {
          return (t) => (
            engine.on(e, t),
            () => {
              engine.off(e, t);
            }
          );
        }
        u.d(t, { E: () => n });
      },
      3138: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => a });
        var n = u(5959);
        const a = { view: u(7641), client: n };
      },
      3722: (e, t, u) => {
        "use strict";
        function n(e, t, u = 1) {
          return viewEnv.getChildTexturePath(e, t.width, t.height, u);
        }
        function a(e, t, u) {
          return `url(${n(e, t, u)})`;
        }
        (u.r(t), u.d(t, { getBgUrl: () => a, getTextureUrl: () => n }));
      },
      6112: (e, t, u) => {
        "use strict";
        u.d(t, { W: () => n });
        const n = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (e, t, u) => {
        "use strict";
        u.d(t, { U: () => a });
        var n = u(2472);
        const a = {
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
      7641: (e, t, u) => {
        "use strict";
        (u.r(t),
          u.d(t, {
            addModelObserver: () => c,
            addPreloadTexture: () => s,
            children: () => n,
            displayStatus: () => a.W,
            displayStatusIs: () => w,
            events: () => r.U,
            extraSize: () => y,
            forceTriggerMouseMove: () => B,
            freezeTextureBeforeResize: () => g,
            getBrowserTexturePath: () => l,
            getDisplayStatus: () => f,
            getScale: () => A,
            getSize: () => d,
            getViewGlobalPosition: () => E,
            isClientAccessible: () => b,
            isEventHandled: () => D,
            isFocused: () => h,
            pxToRem: () => p,
            remToPx: () => C,
            resize: () => _,
            sendEvent: () => o.qP,
            setAnimateWindow: () => F,
            setEventHandled: () => v,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => m,
            whenTutorialReady: () => k,
          }));
        var n = u(3722),
          a = u(6112),
          r = u(6538),
          o = u(8566);
        function s(e) {
          viewEnv.addPreloadTexture(e);
        }
        function i(e) {
          viewEnv.setHitAreaPaddingsRem(e, e, e, e, 15);
        }
        function l(e, t, u, n = 1) {
          return viewEnv.getWebBrowserTexturePath(e, t, u, n);
        }
        function c(e, t, u) {
          return viewEnv.addDataChangedCallback(e, t, u);
        }
        function m(e) {
          viewEnv.setHitAreaPaddingsRem(e.top, e.right, e.bottom, e.left, 15);
        }
        function d(e = "px") {
          return "rem" === e ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function _(e, t, u = "px") {
          return "rem" === u ? viewEnv.resizeViewRem(e, t) : viewEnv.resizeViewPx(e, t);
        }
        function E(e = "rem") {
          const t = viewEnv.getViewGlobalPositionRem();
          return "rem" === e ? t : { x: C(t.x), y: C(t.y) };
        }
        function g() {
          viewEnv.freezeTextureBeforeResize();
        }
        function A() {
          return viewEnv.getScale();
        }
        function p(e) {
          return viewEnv.pxToRem(e);
        }
        function C(e) {
          return viewEnv.remToPx(e);
        }
        function F(e, t) {
          viewEnv.setAnimateWindow(e, t);
        }
        function h() {
          return viewEnv.isFocused();
        }
        function b() {
          return viewEnv.isClientAccessible();
        }
        function v() {
          return viewEnv.setEventHandled();
        }
        function D() {
          return viewEnv.isEventHandled();
        }
        function B() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const w = Object.keys(a.W).reduce(
            (e, t) => ((e[t] = () => viewEnv.getShowingStatus() === a.W[t]), e),
            {},
          ),
          y = {
            set: (e, t) => {
              viewEnv.setExtraSizeRem(e, t);
            },
            get: (e, t) => {
              viewEnv.getExtraSizeRem(e, t);
            },
          },
          k = Promise.all([
            new Promise((e) => {
              window.isDomBuilt ? e() : r.U.onDomBuilt(e);
            }),
            engine.whenReady,
          ]);
      },
      8566: (e, t, u) => {
        "use strict";
        u.d(t, { qP: () => l });
        const n = ["args"];
        const a = 2,
          r = 16,
          o = 32,
          s = 64,
          i = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const r = t.args,
                o = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(t, n);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, o, {
                      arguments:
                        ((a = r),
                        Object.entries(a).map(([e, t]) => {
                          const u = "GFValueProxy";
                          switch (typeof t) {
                            case "number":
                              return { __Type: u, name: e, number: t };
                            case "boolean":
                              return { __Type: u, name: e, bool: t };
                            default:
                              return { __Type: u, name: e, string: t.toString() };
                          }
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, o));
            }
            return viewEnv.handleViewEvent({ __Type: u, type: e });
            var a;
          },
          l = {
            close(e) {
              i("popover" === e ? a : o);
            },
            minimize() {
              i(s);
            },
            move(e) {
              i(r, { isMouseEvent: !0, on: e });
            },
          };
      },
      4598: (e, t, u) => {
        "use strict";
        u.d(t, { jv: () => n });
        function n() {
          return !1;
        }
        console.log;
      },
      7902: (e, t, u) => {
        "use strict";
        u.d(t, { F: () => n });
        const n = (e = 1) => {
          const t = new Error().stack;
          let u,
            n = R.invalid("resId");
          return (
            t &&
              ((u = t.split("\n")[e].split(".js")[0].split("/").pop() || ""),
              window.__feature &&
                window.__feature !== u &&
                window.subViews[u] &&
                (n = window.subViews[u].id)),
            { caller: u, stack: t, resId: n }
          );
        };
      },
      3377: (e, t, u) => {
        "use strict";
        u.d(t, { ZP: () => c });
        var n = u(5415),
          a = u(6179),
          r = u.n(a);
        const o = ["xl", "lg", "md", "sm", "xs"],
          s = (e) => e.includes("_") && ((e) => o.includes(e))(e.split("_").at(-1)),
          i = [n.cJ.ExtraLarge, n.cJ.Large, n.cJ.Medium, n.cJ.Small, n.cJ.ExtraSmall],
          l = (e, t) =>
            Object.keys(e).reduce((u, n) => {
              if (n in u) return u;
              if (s(n)) {
                const a = n.split("_").slice(0, -1).join("_");
                if (a in u) return u;
                const r = i.indexOf(t),
                  s = (-1 !== r ? o.slice(r) : [])
                    .map((e) => a + "_" + e)
                    .find((t) => void 0 !== e[t]),
                  l = s ? e[s] : void 0;
                return ((u[a] = void 0 !== l ? l : e[a]), u);
              }
              const a = e[n];
              return (
                void 0 === a ||
                  ((e, t) => o.some((u) => void 0 !== t[`${e}_${u}`]))(n, e) ||
                  (u[n] = a),
                u
              );
            }, {}),
          c = (e, t = l) => {
            const u = (
              (e, t = l) =>
              (u) => {
                const o = (0, n.GS)().mediaSize,
                  s = (0, a.useMemo)(() => t(u, o), [u, o]);
                return r().createElement(e, s);
              }
            )(e, t);
            return r().memo((t) =>
              Object.keys(t).some((e) => s(e) && void 0 !== t[e])
                ? r().createElement(u, t)
                : r().createElement(e, t),
            );
          };
      },
      6536: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => a });
        var n = u(6179);
        const a = (e) => {
          const t = (0, n.useRef)(!1);
          t.current || (e(), (t.current = !0));
        };
      },
      5415: (e, t, u) => {
        "use strict";
        u.d(t, { Aq: () => i, GS: () => l, cJ: () => o, fd: () => s });
        var n = u(6179),
          a = u(7739),
          r = u(1043);
        let o, s, i;
        (!(function (e) {
          ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
            (e[(e.Small = r.j.small.width)] = "Small"),
            (e[(e.Medium = r.j.medium.width)] = "Medium"),
            (e[(e.Large = r.j.large.width)] = "Large"),
            (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
        })(o || (o = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.width)] = "Small"),
              (e[(e.Medium = r.j.medium.width)] = "Medium"),
              (e[(e.Large = r.j.large.width)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
          })(s || (s = {})),
          (function (e) {
            ((e[(e.ExtraSmall = r.j.extraSmall.height)] = "ExtraSmall"),
              (e[(e.Small = r.j.small.height)] = "Small"),
              (e[(e.Medium = r.j.medium.height)] = "Medium"),
              (e[(e.Large = r.j.large.height)] = "Large"),
              (e[(e.ExtraLarge = r.j.extraLarge.height)] = "ExtraLarge"));
          })(i || (i = {})));
        const l = () => {
          const e = (0, n.useContext)(a.YN),
            t = e.width,
            u = e.height,
            r = ((e) => {
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
            l = ((e) => {
              switch (!0) {
                case e.extraLargeWidth:
                  return s.ExtraLarge;
                case e.largeWidth:
                  return s.Large;
                case e.mediumWidth:
                  return s.Medium;
                case e.smallWidth:
                  return s.Small;
                case e.extraSmallWidth:
                  return s.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), s.ExtraSmall);
              }
            })(e),
            c = ((e) => {
              switch (!0) {
                case e.extraLargeHeight:
                  return i.ExtraLarge;
                case e.largeHeight:
                  return i.Large;
                case e.mediumHeight:
                  return i.Medium;
                case e.smallHeight:
                  return i.Small;
                case e.extraSmallHeight:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(e);
          return {
            mediaSize: r,
            mediaWidth: l,
            mediaHeight: c,
            remScreenWidth: t,
            remScreenHeight: u,
          };
        };
      },
      2039: (e, t, u) => {
        "use strict";
        u.d(t, { b: () => a });
        var n = u(6179);
        const a = (e) => {
          (0, n.useEffect)(e, []);
        };
      },
      3112: (e, t, u) => {
        "use strict";
        u.d(t, { V: () => r });
        var n = u(6179),
          a = u(3138);
        const r = () => {
          const e = (0, n.useState)(a.O.view.getScale()),
            t = e[0],
            u = e[1];
          return (
            (0, n.useEffect)(() => {
              const e = () => {
                u(a.O.view.getScale());
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
      4489: (e, t, u) => {
        "use strict";
        u.d(t, { f: () => r });
        var n = u(5139),
          a = u(6179);
        function r(e, t, u) {
          const r = (0, a.useMemo)(() => (0, n.Z)(u, e), t);
          return ((0, a.useEffect)(() => r.cancel, [r]), r);
        }
      },
      5521: (e, t, u) => {
        "use strict";
        let n, a;
        (u.d(t, { n: () => n }),
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
      5175: (e, t, u) => {
        "use strict";
        u.d(t, { c: () => r });
        var n = u(9480);
        const a = (e) =>
            null !== e && "object" == typeof e
              ? "CoherentArrayProxy" === e.constructor.name
                ? n.UI(e, (e) => ("object" == typeof e ? a(e) : e))
                : Array.isArray(e)
                  ? e.map((e) => ("object" == typeof e ? a(e) : e))
                  : Object.fromEntries(
                      Object.entries(e).map(([e, t]) => [e, "object" == typeof t ? a(t) : t]),
                    )
              : e,
          r = (e) => a(e);
      },
      9480: (e, t, u) => {
        "use strict";
        function n(e, t) {
          var u;
          if (!(t >= e.length))
            return Array.isArray(e) ? e[t] : null == (u = e[t]) ? void 0 : u.value;
        }
        u.d(t, { U2: () => n, UI: () => r, sE: () => o });
        function a(e) {
          var t;
          return e && "value" in e && null != (t = e.constructor) && t.name.includes("ArrayItem")
            ? null == e
              ? void 0
              : e.value
            : e;
        }
        function r(e, t) {
          return Array.isArray(e)
            ? e.map(t)
            : e.map((e, u, n) => t(null == e ? void 0 : e.value, u, n));
        }
        function o(e, t) {
          for (let u = 0; u < e.length; u++) {
            const n = a(e[u]);
            if (t(n, u, e)) return n;
          }
        }
      },
      5099: (e, t, u) => {
        "use strict";
        u.d(t, { B: () => n });
        const n = (e) => {
          let t = !1;
          return {
            promise: new Promise((u, n) => {
              e.then((e) => !t && u(e)).catch((e) => !t && n(e));
            }),
            cancel() {
              t = !0;
            },
          };
        };
      },
      4385: (e, t, u) => {
        "use strict";
        u.d(t, { K: () => n });
        const n = (e, t) => {
          const u = [];
          for (let n = 0; n < e; n++) u.push(t(n));
          return u;
        };
      },
      9690: (e, t, u) => {
        "use strict";
        u.d(t, { HG: () => o });
        const n = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          a = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const r = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          o = (e) =>
            r
              ? `${e}`
              : (function (e) {
                  let t = "";
                  for (let u = a.length - 1; u >= 0; u--)
                    for (; e >= a[u];) ((t += n[u]), (e -= a[u]));
                  return t;
                })(e);
      },
      7727: (e, t, u) => {
        "use strict";
        function n(e) {
          engine.call("PlaySound", e);
        }
        u.d(t, { $: () => a, G: () => n });
        const a = {
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
      3649: (e, t, u) => {
        "use strict";
        let n;
        function a(e, t) {
          return e.replace(/(\{|%\()\w+(\}|\)s)/g, (e) => {
            const u = 0 === e.indexOf("%") ? 2 : 1;
            return String(t[e.slice(u, -u)]);
          });
        }
        function r(e) {
          return e.replace(/-/g, "_");
        }
        function o(e) {
          return e[0].toUpperCase() + e.slice(1);
        }
        (u.d(t, { BN: () => r, Uw: () => _, e: () => o, uF: () => a, v2: () => n }),
          (function (e) {
            ((e[(e.left = 0)] = "left"), (e[(e.right = 1)] = "right"));
          })(n || (n = {})));
        const s = (e, t, u) => {
            if (u % 2) {
              const u = e.pop();
              return [...e, u + t];
            }
            return [...e, t];
          },
          i = (e, t, u) => {
            if (0 === u) return [t];
            if (u % 2) return [...e, " " === t ? " " : t];
            {
              const u = e.pop();
              return [...e, u + t];
            }
          },
          l = (e, t, u = n.left) => e.split(t).reduce(u === n.left ? s : i, []),
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
          m = ["zh_cn", "zh_sg", "zh_tw"],
          d = (e, t = n.left) => {
            const u = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return m.includes(u)
              ? c(e)
              : ((e, t = n.left) => {
                  let u = [];
                  const a =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = e.replace(/&nbsp;/g, " ");
                  return (l(r, /( )/, t).forEach((e) => (u = u.concat(l(e, a, n.left)))), u);
                })(e, t);
          },
          _ = (e, t, u) =>
            e.split(/%\((.*?)\)(?:[sd])?/g).map((e) => (u && e in u ? u[e] : d(e, t)));
      },
      5139: (e, t, u) => {
        "use strict";
        function n(e, t, u, n) {
          let a,
            r = !1,
            o = 0;
          function s() {
            a && clearTimeout(a);
          }
          function i(...i) {
            const l = this,
              c = Date.now() - o;
            function m() {
              ((o = Date.now()), u.apply(l, i));
            }
            r ||
              (n && !a && m(),
              s(),
              void 0 === n && c > e
                ? m()
                : !0 !== t &&
                  (a = setTimeout(
                    n
                      ? function () {
                          a = void 0;
                        }
                      : m,
                    void 0 === n ? e - c : e,
                  )));
          }
          return (
            "boolean" != typeof t && ((n = u), (u = t), (t = void 0)),
            (i.cancel = function () {
              (s(), (r = !0));
            }),
            i
          );
        }
        u.d(t, { Z: () => n });
      },
      1358: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => r });
        var n = u(3138);
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
          addCallback(e, t, u = 0, a = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const r = n.O.view.addModelObserver(e, u, a);
            return (
              r > 0
                ? ((this._callbacks[r] = t),
                  u > 0 && (this._views[u] ? this._views[u].push(r) : (this._views[u] = [r])))
                : console.error("Can't add callback for model:", e),
              r
            );
          }
          removeCallback(e, t = 0) {
            let u = !1;
            return (
              void 0 !== e &&
                void 0 !== this._callbacks[e] &&
                ((u = viewEnv.removeDataChangedCallback(e, t)), delete this._callbacks[e]),
              u || console.error("Can't remove callback by id:", e),
              u
            );
          }
          _emmitDataChanged(e, t, u) {
            u.forEach((u) => {
              const n = this._callbacks[u];
              void 0 !== n && n(e, t);
            });
          }
        }
        a.__instance = void 0;
        const r = a;
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
      4179: (e, t, u) => {
        "use strict";
        u.d(t, {
          B0: () => i,
          c9: () => h,
          wU: () => B,
          ry: () => C,
          Eu: () => F,
          SW: () => v,
          P3: () => D,
        });
        class n {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (e) => {
                this.entries.forEach(({ container: t, callback: u }) => {
                  let n = e.target;
                  do {
                    if (n === t) return;
                    n = n.parentNode;
                  } while (n);
                  u();
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
            const u = e,
              n = t;
            ((this.entries = this.entries.filter(
              ({ container: e, callback: t }) => e !== u || t !== n,
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
        var r = u(1358);
        const o = {
            getNumberFormat: (e, t) => systemLocale.getNumberFormat(e, t),
            getRealFormat: (e, t) => systemLocale.getRealFormat(e, t),
            getTimeFormat: (e, t) => systemLocale.getTimeFormat(e, t),
            getDateFormat: (e, t) => systemLocale.getDateFormat(e, t),
            toUpperCase: (e) => systemLocale.toUpperCase(e),
            toLowerCase: (e) => systemLocale.toUpperCase(e),
          },
          s = {
            getNumberFormat: (e) => userLocale.getNumberFormat(e),
            getTimeFormat: (e, t, u) => userLocale.getTimeFormat(e, t, void 0 === u || u),
            getTimeString: (e, t, u) => userLocale.getTimeString(e, t, void 0 === u || u),
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
          m = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          d = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var _ = u(5521),
          E = u(3138);
        const g = ["args"];
        function A(e, t, u, n, a, r, o) {
          try {
            var s = e[r](o),
              i = s.value;
          } catch (e) {
            return void u(e);
          }
          s.done ? t(i) : Promise.resolve(i).then(n, a);
        }
        const p = (e) => ({
            __Type: "GFBoundingBox",
            x: e.x,
            y: e.y,
            width: e.width,
            height: e.height,
          }),
          C = (function () {
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
                    u = arguments;
                  return new Promise(function (n, a) {
                    var r = e.apply(t, u);
                    function o(e) {
                      A(r, n, a, o, s, "next", e);
                    }
                    function s(e) {
                      A(r, n, a, o, s, "throw", e);
                    }
                    o(void 0);
                  });
                });
            return function () {
              return t.apply(this, arguments);
            };
          })(),
          F = () =>
            new Promise((e) => {
              requestAnimationFrame(() => {
                requestAnimationFrame(() => {
                  e();
                });
              });
            }),
          h = (e, t) => {
            const u = "GFViewEventProxy";
            if (void 0 !== t) {
              const a = t.args,
                r = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(t, g);
              void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: u, type: e }, r, {
                      arguments:
                        ((n = a),
                        Object.entries(n).map(([e, t]) => {
                          const u = { __Type: "GFValueProxy", name: e };
                          switch (typeof t) {
                            case "number":
                              u.number = t;
                              break;
                            case "boolean":
                              u.bool = t;
                              break;
                            default:
                              u.string = t.toString();
                          }
                          return u;
                        })),
                    }),
                  )
                : viewEnv.handleViewEvent(Object.assign({ __Type: u, type: e }, r));
            } else viewEnv.handleViewEvent({ __Type: u, type: e });
            var n;
          },
          b = () => h(i.CLOSE),
          v = () => h(i.POP_OVER, { on: !1 }),
          D = (e, t, u, n, a = R.invalid("resId"), r) => {
            const o = E.O.view.getViewGlobalPosition(),
              s = u.getBoundingClientRect(),
              l = s.x,
              c = s.y,
              m = s.width,
              d = s.height,
              _ = {
                x: E.O.view.pxToRem(l) + o.x,
                y: E.O.view.pxToRem(c) + o.y,
                width: E.O.view.pxToRem(m),
                height: E.O.view.pxToRem(d),
              };
            h(i.POP_OVER, {
              isMouseEvent: !0,
              contentID: e,
              decoratorID: n || R.invalid("resId"),
              targetID: a,
              direction: t,
              bbox: p(_),
              on: !0,
              args: r,
            });
          },
          B = () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
          f = (e, t) => {
            e.keyCode === _.n.ESCAPE && t();
          };
        var w = u(7572);
        const y = a.instance,
          k = {
            DataTracker: r.Z,
            ViewModel: w.Z,
            ViewEventType: i,
            NumberFormatType: l,
            RealFormatType: c,
            TimeFormatType: m,
            DateFormatType: d,
            makeGlobalBoundingBox: p,
            sendMoveEvent: (e) => h(i.MOVE, { isMouseEvent: !0, on: e }),
            sendCloseEvent: b,
            sendClosePopOverEvent: v,
            sendShowContextMenuEvent: (e, t, u = 0) => {
              h(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: e,
                on: !0,
                decoratorID: u,
                args: t,
              });
            },
            sendShowPopOverEvent: D,
            addEscapeListener: (e) => {
              const t = (t) => f(t, e);
              return (
                window.addEventListener("keydown", t),
                () => window.removeEventListener("keydown", t)
              );
            },
            closeOnEsc: (e) => {
              f(e, b);
            },
            handleViewEvent: h,
            onBindingsReady: C,
            onLayoutReady: F,
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: B,
            dumpViewModel: function e(t) {
              const u = {};
              if ("object" != typeof t) return t;
              for (const n in t)
                if (Object.prototype.hasOwnProperty.call(t, n)) {
                  const a = Object.prototype.toString.call(t[n]);
                  if (a.startsWith("[object CoherentArrayProxy]")) {
                    const a = t[n];
                    u[n] = [];
                    for (let t = 0; t < a.length; t++) u[n].push({ value: e(a[t].value) });
                  } else
                    a.startsWith("[object class BW::WULF::ViewModel")
                      ? (u[n] = e(t[n]))
                      : (u[n] = t[n]);
                }
              return u;
            },
            ClickOutsideManager: y,
            SystemLocale: o,
            UserLocale: s,
          };
        window.ViewEnvHelper = k;
      },
      3458: (e, t, u) => {
        "use strict";
        let n;
        (u.d(t, { Z0: () => a, in: () => n, sx: () => r }),
          (function (e) {
            ((e[(e.NonSet = 0)] = "NonSet"),
              (e[(e.Debug = 10)] = "Debug"),
              (e[(e.Info = 20)] = "Info"),
              (e[(e.Warning = 30)] = "Warning"));
          })(n || (n = {})));
        const a = "tooltip_watched",
          r = 2;
        let o;
        !(function (e) {
          ((e.Click = "click"), (e.KeyDown = "keydown"));
        })(o || (o = {}));
      },
      4828: (e, t, u) => {
        "use strict";
        u.d(t, { AB: () => d, D9: () => n, eX: () => r, sC: () => o, tL: () => a, x3: () => l });
        const n = "crew",
          a = 2e3;
        let r, o, s, i, l, c, m;
        (!(function (e) {
          ((e.Viewed = "viewed"), (e.Click = "click"));
        })(r || (r = {})),
          (function (e) {
            ((e.Hangar = "hangar"),
              (e.PersonalFile = "personal_file_view"),
              (e.PersonalData = "personal_data_view"),
              (e.ServiceRecord = "service_record_view"),
              (e.Barracks = "barracks_view"),
              (e.MemberChange = "member_change_view"),
              (e.QuickTraining = "quick_training_view"),
              (e.TankChange = "tank_change_view"));
          })(o || (o = {})),
          (function (e) {
            e.DocumentChange = "document_change_dialog";
          })(s || (s = {})),
          (function (e) {
            ((e.PremiumTooltip = "personal_file_view_premium_tooltip"),
              (e.MstlTooltip = "personal_file_view_mstl_tooltip"));
          })(i || (i = {})),
          (function (e) {
            ((e.ChangeButtonTooltip = "crew_widget_change_button_tooltip"),
              (e.MstlTooltip = "crew_widget_mstl_tooltip"),
              (e.SlotContextMenu = "crew_widget_slot_context_menu"),
              (e.CrewOperationsButton = "crew_widget_crew_operations_button"));
          })(l || (l = {})),
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
          [R.views.lobby.crew.personal_case.PersonalFileView("resId")]: o.PersonalFile,
          [R.views.lobby.crew.personal_case.PersonalDataView("resId")]: o.PersonalData,
          [R.views.lobby.crew.personal_case.ServiceRecordView("resId")]: o.ServiceRecord,
          [R.views.lobby.crew.BarracksView("resId")]: o.Barracks,
          [R.views.lobby.crew.HangarCrewWidget("resId")]: o.Hangar,
          [R.views.lobby.crew.MemberChangeView("resId")]: o.MemberChange,
          [R.views.lobby.crew.TankChangeView("resId")]: o.TankChange,
          [R.views.lobby.crew.QuickTrainingView("resId")]: o.QuickTraining,
        };
      },
      1943: (e, t, u) => {
        "use strict";
        u.d(t, { Jp: () => m, Sr: () => _ });
        var n = u(6179),
          a = u(3458);
        const r = ["action", "timeLimit"];
        const o = "metrics",
          s = () => Date.now(),
          i = ({ partnerID: e, item: t, parentScreen: u, itemState: n, info: a }) => ({
            item: t,
            partnerID: e || null,
            parent_screen: u || null,
            item_state: n || null,
            additional_info: a || null,
          }),
          l = (e, t) => {
            const u = (0, n.useCallback)(
              (u, n = a.in.Info, r) => {
                (r || (r = {}),
                  Object.keys(r).length >= 200 ||
                    window.uiLoggerModel.log({
                      feature: e,
                      group: t,
                      action: u,
                      logLevel: n,
                      params: JSON.stringify(r),
                    }));
              },
              [e, t],
            );
            return (e, t, n) => u(e, t, n);
          },
          c = (e, t) => {
            const u = l(e, t),
              a = (0, n.useRef)(new Map()),
              r = (0, n.useRef)(new Map()),
              o = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  (void 0 !== t && t > 0) || a.current.set(e, s());
                },
                [a],
              ),
              i = (0, n.useCallback)(() => {
                (a.current.clear(), r.current.clear());
              }, [a, r]),
              c = (0, n.useCallback)(
                (e) => {
                  e &&
                    void 0 !== a.current.get(e) &&
                    void 0 === r.current.get(e) &&
                    r.current.set(e, s());
                },
                [a, r],
              ),
              m = (0, n.useCallback)(
                (e) => {
                  if (!e) return;
                  const t = a.current.get(e);
                  if (void 0 === t) return;
                  const u = r.current.get(e);
                  if (void 0 === u) return;
                  r.current.delete(e);
                  const n = s() - u;
                  a.current.set(e, t + n);
                },
                [a, r],
              ),
              d = (0, n.useCallback)(
                (e, t = 0, n, o) => {
                  const i = a.current.get(e);
                  if (void 0 === i) return;
                  (void 0 !== r.current.get(e) && m(e), a.current.delete(e));
                  const l = (s() - i) / 1e3;
                  l <= t ||
                    ((o = ((e, t) => (void 0 === e && (e = {}), (e.timeSpent = t), e))(o, l)),
                    u(e, n, o));
                },
                [a, r, u, m],
              );
            return [
              (e) => o(e),
              (e, t, u, n) => d(e, t, u, n),
              () => i(),
              (e) => c(e),
              (e) => m(e),
            ];
          },
          m = (e) => {
            const t = l(e, o),
              u = (0, n.useCallback)(
                (e) => {
                  t(e.action, e.logLevel, i(e));
                },
                [t],
              );
            return (e) => u(e);
          },
          d = (e) => {
            const t = c(e, o),
              u = t[0],
              a = t[1],
              r = t[2],
              s = t[3],
              l = t[4],
              m = (0, n.useCallback)(
                (e) => {
                  const t = e.action,
                    u = e.timeLimit,
                    n = e.logLevel;
                  a(t, u, n, i(e));
                },
                [a],
              );
            return [(e) => u(e), (e) => m(e), () => r(), (e) => s(e), (e) => l(e)];
          },
          _ = (e, t) => {
            const u = d(e),
              o = u[0],
              s = u[1],
              i = t.action,
              l = t.timeLimit,
              c = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(t, r);
            return (0, n.useMemo)(
              () => ({
                onShow: () => o(i || a.Z0),
                onHide: () => s(Object.assign({ action: i || a.Z0, timeLimit: l || a.sx }, c)),
              }),
              [i, l, c, o, s],
            );
          };
      },
      2316: (e, t, u) => {
        "use strict";
        var n = {};
        (u.r(n),
          u.d(n, {
            Area: () => ze,
            Bar: () => We,
            DefaultScroll: () => je,
            Direction: () => Be,
            defaultSettings: () => fe,
            useHorizontalScrollApi: () => ye,
          }));
        var a = {};
        (u.r(a),
          u.d(a, {
            Area: () => st,
            Bar: () => at,
            Default: () => ot,
            useVerticalScrollApi: () => Ue,
          }));
        var r = u(7739),
          o = u(6179),
          s = u.n(o),
          i = u(6483),
          l = u.n(i),
          c = u(926),
          m = u.n(c),
          d = u(5415);
        const _ = ["children", "className"];
        function E() {
          return (
            (E =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            E.apply(this, arguments)
          );
        }
        const g = {
            [d.fd.ExtraSmall]: "",
            [d.fd.Small]: m().SMALL_WIDTH,
            [d.fd.Medium]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH}`,
            [d.fd.Large]: `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH}`,
            [d.fd.ExtraLarge]:
              `${m().SMALL_WIDTH} ${m().MEDIUM_WIDTH} ${m().LARGE_WIDTH} ${m().EXTRA_LARGE_WIDTH}`,
          },
          A = {
            [d.Aq.ExtraSmall]: "",
            [d.Aq.Small]: m().SMALL_HEIGHT,
            [d.Aq.Medium]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT}`,
            [d.Aq.Large]: `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT}`,
            [d.Aq.ExtraLarge]:
              `${m().SMALL_HEIGHT} ${m().MEDIUM_HEIGHT} ${m().LARGE_HEIGHT} ${m().EXTRA_LARGE_HEIGHT}`,
          },
          p = {
            [d.cJ.ExtraSmall]: "",
            [d.cJ.Small]: m().SMALL,
            [d.cJ.Medium]: `${m().SMALL} ${m().MEDIUM}`,
            [d.cJ.Large]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE}`,
            [d.cJ.ExtraLarge]: `${m().SMALL} ${m().MEDIUM} ${m().LARGE} ${m().EXTRA_LARGE}`,
          },
          C = (e) => {
            let t = e.children,
              u = e.className,
              n = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, _);
            const a = (0, d.GS)(),
              r = a.mediaWidth,
              o = a.mediaHeight,
              i = a.mediaSize;
            return s().createElement("div", E({ className: l()(u, g[r], A[o], p[i]) }, n), t);
          },
          F = ["children"];
        const h = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, F);
          return s().createElement(r.ZN, null, s().createElement(C, u, t));
        };
        var b = u(493),
          v = u.n(b),
          D = u(1037),
          B = u(3138),
          f = u(5521);
        u(4179);
        const w = (e) => {
          console.error(e.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function y(e = f.n.NONE, t = w, u = !1) {
          (0, o.useEffect)(() => {
            if (e !== f.n.NONE)
              return (
                window.addEventListener("keydown", n, u),
                () => {
                  window.removeEventListener("keydown", n, u);
                }
              );
            function n(n) {
              if (n.keyCode === e) {
                if (B.O.view.isEventHandled()) return;
                (B.O.view.setEventHandled(), t(n), u && n.stopPropagation());
              }
            }
          }, [t, e, u]);
        }
        const k = {
          base: "FlagIcon_base_25",
          base__c_1080x454: "FlagIcon_base__c_1080x454_6c",
          base__c_240x118: "FlagIcon_base__c_240x118_92",
        };
        let S;
        !(function (e) {
          ((e.c1080x454 = "c_1080x454"), (e.c240x118 = "c_240x118"));
        })(S || (S = {}));
        const L = (e, t) => {
            switch (t) {
              case S.c1080x454:
                return R.images.gui.maps.icons.crew.flags.$dyn(e);
              case S.c240x118:
                return R.images.gui.maps.icons.tankmen.card.nations.$dyn(e);
            }
          },
          x = s().memo(function ({ nation: e, size: t, className: u }) {
            return s().createElement("div", {
              className: l()(k.base, k[`base__${t}`], u),
              style: { backgroundImage: `url('${L(e, t)}')` },
            });
          }),
          I = {
            base: "ListHeader_base_ad",
            title: "ListHeader_title_a8",
            base__memberChange: "ListHeader_base__memberChange_c2",
            base__tankChange: "ListHeader_base__tankChange_fb",
            base__personalData: "ListHeader_base__personalData_aa",
          };
        let N;
        !(function (e) {
          ((e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(N || (N = {}));
        const T = ({ title: e, theme: t = N.Barracks, className: u, children: n }) =>
          s().createElement(
            "div",
            { className: l()(I.base, I[`base__${t}`]) },
            s().createElement("div", { className: l()(I.title, u) }, e),
            n,
          );
        var M = u(7727);
        const P = {
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
          O = [
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
        function H() {
          return (
            (H =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            H.apply(this, arguments)
          );
        }
        class W extends s().PureComponent {
          constructor(...e) {
            (super(...e),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (e) => (t) => {
                (e && e(t),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && (0, M.G)(this.props.soundHover));
              }),
              (this._onMouseLeave = (e) => (t) => {
                (e && e(t), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (e) => (t) => {
                (e && e(t),
                  this.setState({ click: !0 }),
                  this.props.soundClick && (0, M.G)(this.props.soundClick));
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
              u = e.onClick,
              n = e.goto,
              a = e.side,
              r = e.type,
              o = e.classNames,
              i = e.onMouseEnter,
              c = e.onMouseLeave,
              m = e.onMouseDown,
              d = e.onMouseUp,
              _ =
                (e.soundClick,
                e.soundHover,
                (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(e, O)),
              E = l()(P.base, P[`base__${r}`], P[`base__${a}`], null == o ? void 0 : o.base),
              g = l()(P.icon, P[`icon__${r}`], P[`icon__${a}`], null == o ? void 0 : o.icon),
              A = l()(P.glow, null == o ? void 0 : o.glow),
              p = l()(P.caption, P[`caption__${r}`], null == o ? void 0 : o.caption),
              C = l()(P.goto, null == o ? void 0 : o.goto);
            return s().createElement(
              "div",
              H(
                {
                  className: E,
                  onMouseEnter: this._onMouseEnter(i),
                  onMouseLeave: this._onMouseLeave(c),
                  onMouseDown: this._onMouseDown(m),
                  onMouseUp: this._onMouseUp(d),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: u,
                },
                _,
              ),
              "info" !== r && s().createElement("div", { className: P.shine }),
              s().createElement(
                "div",
                { className: g },
                s().createElement("div", { className: A }),
              ),
              s().createElement("div", { className: p }, t),
              n && s().createElement("div", { className: C }, n),
            );
          }
        }
        W.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        const G = ({ onClick: e }) =>
            s().createElement(W, {
              onClick: e,
              caption: R.strings.crew.common.navigation.aboutCrew(),
              type: "info",
            }),
          j = "common_close_0e",
          z = ({ onClick: e, label: t = R.strings.menu.viewHeader.closeBtn.label() }) =>
            s().createElement(W, {
              onClick: e,
              classNames: { base: j },
              caption: t,
              type: "close",
              side: "right",
            }),
          U = "TopButtons_base_ef",
          $ = "TopButtons_leftButtons_9e",
          Z = "TopButtons_rightButtons_33",
          V = s().memo(function ({
            backButtonLabel: e,
            closeButtonLabel: t = R.strings.menu.viewHeader.closeBtn.label(),
            onBackClick: u,
            onAboutClick: n,
            onCloseClick: a,
            className: r,
            classNames: o,
          }) {
            return s().createElement(
              "div",
              { className: l()(U, r) },
              s().createElement(
                "div",
                { className: l()($, null == o ? void 0 : o.leftButtons) },
                e && u && s().createElement(W, { onClick: u, caption: e, type: "back" }),
              ),
              s().createElement(
                "div",
                { className: l()(Z, null == o ? void 0 : o.rightButtons) },
                n && s().createElement(G, { onClick: n }),
                a && s().createElement(z, { onClick: a, label: t }),
              ),
            );
          });
        var X = u(8727),
          q = u(5801);
        const K = (0, u(3215).q)()(
            ({ observableModel: e }) =>
              Object.assign(
                { vehicleList: e.array("vehicleList") },
                e.primitives(["nation", "backButtonLabel", "isButtonBarVisible"]),
              ),
            ({ externalModel: e }) => ({
              back: e.createCallbackNoArgs("onBack"),
              hangar: e.createCallbackNoArgs("onHangar"),
              close: e.createCallbackNoArgs("onClose"),
              closeWithEsc: e.createCallback(() => ({ isFromEscape: !0 }), "onClose"),
              selectVehicle: e.createCallback((e) => ({ vehicleID: e }), "onVehicleSelected"),
              resetFilters: e.createCallbackNoArgs("onResetFilters"),
            }),
          ),
          Y = K[0],
          Q = K[1];
        var J = u(2106),
          ee = u(3403),
          te = u(3457),
          ue = u(6373),
          ne = u(8018);
        const ae = "WarningText_base_13",
          re = "WarningText_icon_5d",
          oe = "WarningText_label_c6",
          se = s().memo(function ({ label: e }) {
            return s().createElement(
              "div",
              { className: ae },
              s().createElement("div", { className: re }),
              s().createElement("div", { className: oe }, e),
            );
          }),
          ie = "ListEmptyState_base_ae",
          le = "ListEmptyState_content_1e",
          ce = "ListEmptyState_shadow_ae",
          me = "ListEmptyState_buttonWrapper_78",
          de = "ListEmptyState_button_f1",
          _e = s().memo(function ({
            warningText: e,
            buttonType: t = te.L$.secondary,
            tooltipArgs: u = ne.Xd,
            className: n,
            onClick: a,
            children: r,
          }) {
            return s().createElement(
              "div",
              { className: l()(ie, n) },
              s().createElement(
                "div",
                { className: le },
                s().createElement("div", { className: ce }),
                s().createElement(se, { label: e }),
                r &&
                  s().createElement(
                    "div",
                    { className: me },
                    s().createElement(
                      ue.i,
                      u,
                      s().createElement(
                        te.u5,
                        { size: te.qE.small, type: t, onClick: a, mixClass: de },
                        r,
                      ),
                    ),
                  ),
              ),
            );
          });
        var Ee = u(1856);
        const ge = (e, t, u) => (u < e ? e : u > t ? t : u),
          Ae = [];
        function pe(e) {
          const t = (0, o.useRef)(e);
          return (
            (0, o.useLayoutEffect)(() => {
              t.current = e;
            }),
            (0, o.useCallback)((...e) => (0, t.current)(...e), Ae)
          );
        }
        function Ce(e, t, u = []) {
          const n = (0, o.useRef)(0),
            a = (0, o.useCallback)(() => window.clearInterval(n.current), u || []);
          (0, o.useEffect)(() => a, [a]);
          const r = (null != u ? u : []).concat([t]);
          return [
            (0, o.useCallback)((u) => {
              ((n.current = window.setInterval(() => e(u, !0), t)), e(u, !1));
            }, r),
            a,
          ];
        }
        function Fe(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return he(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return he(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function he(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        const be = () => {
          const e = (0, o.useMemo)(() => ({}), []),
            t = (t) => (e[t] || (e[t] = new Map()), e[t]),
            u = (e, u) => {
              t(e).set(u, u);
            },
            n = (e, u) => {
              t(e).delete(u);
            },
            a = (e, ...u) => {
              for (var n, a = Fe(t(e).values()); !(n = a()).done;) {
                (0, n.value)(...u);
              }
            };
          return (0, o.useMemo)(() => ({ on: u, off: n, trigger: a }), []);
        };
        var ve = u(4489),
          De = u(7030);
        let Be;
        !(function (e) {
          ((e[(e.Next = -1)] = "Next"), (e[(e.Prev = 1)] = "Prev"));
        })(Be || (Be = {}));
        const fe = {
            step: { type: "proportional", factor: 4, clampedArrowStepTimeout: 100 },
            animationConfig: { tension: 170, friction: 26 },
          },
          we = ({
            getContainerSize: e,
            getBounds: t,
            setScrollPosition: u,
            getDirection: n,
            getWrapperSize: a,
            triggerMouseMoveOnUpdate: r = !1,
          }) => {
            const s = (e, u) => {
              const n = t(e),
                a = n[0],
                r = n[1];
              return ge(a, r, u);
            };
            return (i = {}) => {
              const l = i.settings,
                c = void 0 === l ? fe : l,
                m = (0, o.useRef)(null),
                d = (0, o.useRef)(null),
                _ = be(),
                E = (0, ve.f)(
                  () => {
                    B.O.view.forceTriggerMouseMove();
                  },
                  [],
                  150,
                ),
                g = (0, De.useSpring)(() => ({
                  scrollPosition: 0,
                  onChange: (e) => {
                    const t = m.current;
                    t && (u(t, e), _.trigger("change", e), r && E());
                  },
                  onRest: (e) => _.trigger("rest", e),
                  onStart: (e) => _.trigger("start", e),
                  onPause: (e) => _.trigger("pause", e),
                })),
                A = g[0],
                p = g[1],
                C = (0, o.useCallback)(
                  (e, t, u) => {
                    var n;
                    const a = A.scrollPosition.get(),
                      r = (null != (n = A.scrollPosition.goal) ? n : 0) - a;
                    return s(e, t * u + r + a);
                  },
                  [A.scrollPosition],
                ),
                F = (0, o.useCallback)(
                  (e, { immediate: t = !1, reset: u = !0 } = {}) => {
                    const n = m.current;
                    n &&
                      p.start({
                        scrollPosition: s(n, e),
                        immediate: t,
                        reset: u,
                        config: c.animationConfig,
                        from: { scrollPosition: s(n, A.scrollPosition.get()) },
                      });
                  },
                  [p, c.animationConfig, A.scrollPosition],
                ),
                h = (0, o.useCallback)(
                  (e) => {
                    const t = m.current,
                      u = d.current;
                    if (!t || !u) return;
                    const n = ((e, t) => {
                        switch (t.type) {
                          case "proportional":
                            return a(e) / t.factor;
                          case "fixed":
                            return t.value;
                        }
                      })(u, c.step),
                      r = C(t, e, n);
                    F(r);
                  },
                  [F, C, c.step],
                ),
                b = (0, o.useCallback)(
                  (e) => {
                    (0 !== e.deltaY && h(n(e)),
                      m.current && _.trigger("mouseWheel", e, A.scrollPosition, t(m.current)));
                  },
                  [A.scrollPosition, h, _],
                ),
                v = ((e, t = []) => {
                  const u = (0, o.useRef)(),
                    n = (0, o.useCallback)((...t) => {
                      (u.current && u.current(), (u.current = e(...t)));
                    }, t);
                  return (
                    (0, o.useEffect)(
                      () => () => {
                        u.current && u.current();
                      },
                      [n],
                    ),
                    n
                  );
                })(
                  () =>
                    (0, Ee.v)(() => {
                      const e = m.current;
                      e &&
                        (F(s(e, A.scrollPosition.goal), { immediate: !0 }),
                        _.trigger("resizeHandled"));
                    }),
                  [F, A.scrollPosition.goal],
                ),
                D = pe(() => {
                  const e = m.current;
                  if (!e) return;
                  const t = s(e, A.scrollPosition.goal);
                  (t !== A.scrollPosition.goal && F(t, { immediate: !0 }),
                    _.trigger("recalculateContent"));
                });
              (0, o.useEffect)(
                () => (
                  window.addEventListener("resize", v),
                  () => {
                    window.removeEventListener("resize", v);
                  }
                ),
                [v],
              );
              const f = (0, o.useCallback)((e) => _.trigger("isThumbDraggingChanged", e), [_]);
              return (0, o.useMemo)(
                () => ({
                  getWrapperSize: () => (d.current ? a(d.current) : void 0),
                  getContainerSize: () => (m.current ? e(m.current) : void 0),
                  getBounds: () =>
                    m.current
                      ? t(m.current)
                      : (console.warn("getBounds: contentRef.current is null"), [0, 0]),
                  stepTimeout: c.step.clampedArrowStepTimeout,
                  clampPosition: s,
                  handleMouseWheel: b,
                  applyScroll: F,
                  applyStepTo: h,
                  contentRef: m,
                  wrapperRef: d,
                  scrollPosition: p,
                  animationScroll: A,
                  recalculateContent: D,
                  handleIsThumbDragging: f,
                  events: { on: _.on, off: _.off },
                }),
                [A.scrollPosition, F, h, f, _.off, _.on, D, b, p, c.step.clampedArrowStepTimeout],
              );
            };
          },
          ye = we({
            getBounds: (e) => {
              var t, u;
              return [
                0,
                e.offsetWidth -
                  (null != (t = null == (u = e.parentElement) ? void 0 : u.offsetWidth) ? t : 0),
              ];
            },
            getContainerSize: (e) => e.offsetWidth,
            getWrapperSize: (e) => e.offsetWidth,
            setScrollPosition: (e, t) => {
              e.style.transform = `translateX(-${t.value.scrollPosition}px)`;
            },
            getDirection: (e) => (e.deltaY > 1 ? Be.Next : Be.Prev),
            triggerMouseMoveOnUpdate: !0,
          }),
          ke = "HorizontalBar_base_49",
          Se = "HorizontalBar_base__nonActive_82",
          Le = "HorizontalBar_leftButton_5f",
          xe = "HorizontalBar_rightButton_03",
          Ie = "HorizontalBar_track_0d",
          Ne = "HorizontalBar_thumb_fd",
          Te = "HorizontalBar_rail_32",
          Me = "disable",
          Re = { pending: !1, offset: 0 },
          Pe = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          Oe = () => {},
          He = (e, t) => Math.max(20, e.offsetWidth * t),
          We = (0, o.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = Pe, onDrag: n = Oe }) => {
              const a = (0, o.useRef)(null),
                r = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                m = (0, o.useRef)(null),
                d = e.stepTimeout || 100,
                _ = (0, o.useState)(Re),
                E = _[0],
                g = _[1],
                A = (0, o.useCallback)(
                  (e) => {
                    (g(e),
                      m.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [n],
                ),
                p = () => {
                  const t = c.current,
                    u = m.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && t && u && a)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / a),
                    l = ge(0, 1, o / (a - n)),
                    d = (t.offsetWidth - He(t, s)) * l;
                  ((u.style.transform = `translateX(${0 | d}px)`),
                    ((e) => {
                      if (r.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (r.current.classList.add(Me), void i.current.classList.remove(Me));
                        if (
                          ((t = c.current),
                          (u = m.current),
                          e - (t.offsetWidth - u.offsetWidth) >= -0.5)
                        )
                          return (r.current.classList.remove(Me), void i.current.classList.add(Me));
                        var t, u;
                        (r.current.classList.remove(Me), i.current.classList.remove(Me));
                      }
                    })(d));
                },
                C = pe(() => {
                  ((() => {
                    const t = m.current,
                      u = c.current,
                      n = e.getWrapperSize(),
                      r = e.getContainerSize();
                    if (!(r && t && n && u)) return;
                    const o = Math.min(1, n / r);
                    ((t.style.width = `${He(u, o)}px`),
                      (t.style.display = "flex"),
                      a.current &&
                        (1 === o ? a.current.classList.add(Se) : a.current.classList.remove(Se)));
                  })(),
                    p());
                });
              ((0, o.useEffect)(() => (0, Ee.v)(C)),
                (0, o.useEffect)(
                  () =>
                    (0, Ee.v)(() => {
                      const t = () => {
                        p();
                      };
                      let u = Oe;
                      const n = () => {
                        (u(), (u = (0, Ee.v)(C)));
                      };
                      return (
                        e.events.on("recalculateContent", C),
                        e.events.on("rest", t),
                        e.events.on("change", t),
                        e.events.on("resizeHandled", n),
                        () => {
                          (u(),
                            e.events.off("recalculateContent", C),
                            e.events.off("rest", t),
                            e.events.off("change", t),
                            e.events.off("resizeHandled", n));
                        }
                      );
                    }),
                  [e],
                ),
                (0, o.useEffect)(() => {
                  if (!E.pending) return;
                  const t = (t) => {
                      var u;
                      const a = e.contentRef.current;
                      if (!a) return;
                      const r = c.current,
                        o = m.current;
                      if (!a || !r || !o) return;
                      const s = t.screenX - E.offset - r.getBoundingClientRect().x,
                        i = (s / r.offsetWidth) * (null != (u = e.getContainerSize()) ? u : 0);
                      (e.scrollPosition.start({
                        scrollPosition: e.clampPosition(a, i),
                        reset: !0,
                        immediate: !0,
                        from: { scrollPosition: e.animationScroll.scrollPosition.get() },
                      }),
                        n({ type: "dragging", thumb: o, thumbOffset: s, contentOffset: i }));
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t), A(Re));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, E.offset, E.pending, n, A]));
              const F = Ce((t) => e.applyStepTo(t), d, [e]),
                h = F[0],
                b = F[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", b, !0),
                  () => document.removeEventListener("mouseup", b, !0)
                ),
                [b],
              );
              const v = (e) => {
                e.target.classList.contains(Me) || (0, M.G)("highlight");
              };
              return s().createElement(
                "div",
                { className: l()(ke, t.base), ref: a, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: l()(Le, t.leftButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Me) ||
                      0 !== e.button ||
                      ((0, M.G)("play"), h(Be.Next));
                  },
                  onMouseUp: b,
                  ref: r,
                  onMouseEnter: v,
                }),
                s().createElement(
                  "div",
                  {
                    className: l()(Ie, t.track),
                    onMouseDown: (t) => {
                      const n = m.current;
                      if (n && 0 === t.button)
                        if (((0, M.G)("play"), t.target === n))
                          A({ pending: !0, offset: t.screenX - n.getBoundingClientRect().x });
                        else {
                          ((t) => {
                            const n = m.current,
                              a = e.contentRef.current;
                            if (!n || !a) return;
                            const r = u(e);
                            e.applyScroll(e.animationScroll.scrollPosition.get() + r * t);
                          })(t.screenX > n.getBoundingClientRect().x ? Be.Prev : Be.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: v,
                  },
                  s().createElement("div", { ref: m, className: l()(Ne, t.thumb) }),
                  s().createElement("div", { className: l()(Te, t.rail) }),
                ),
                s().createElement("div", {
                  className: l()(xe, t.rightButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Me) ||
                      0 !== e.button ||
                      ((0, M.G)("play"), h(Be.Prev));
                  },
                  onMouseUp: b,
                  ref: i,
                  onMouseEnter: v,
                }),
              );
            },
          ),
          Ge = {
            base: "HorizontalScroll_base_29",
            wrapper: "HorizontalScroll_wrapper_1e",
            defaultScrollArea: "HorizontalScroll_defaultScrollArea_8d",
          },
          je = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: a,
            classNames: r,
            scrollClassName: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: l()(Ge.base, e.base) });
              }, [n]),
              _ = (0, o.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return s().createElement(
              "div",
              { className: l()(Ge.defaultScroll, u), onWheel: t.handleMouseWheel },
              s().createElement(
                "div",
                { className: l()(Ge.defaultScrollArea, a) },
                s().createElement(ze, { className: i, api: _, classNames: r }, e),
              ),
              s().createElement(We, { getStepByRailClick: c, api: t, onDrag: m, classNames: d }),
            );
          },
          ze = ({ api: e, className: t, classNames: u, children: n, style: a }) => (
            (0, o.useEffect)(() => (0, Ee.v)(e.recalculateContent)),
            s().createElement(
              "div",
              { className: l()(Ge.base, t), style: a },
              s().createElement(
                "div",
                {
                  className: l()(Ge.wrapper, null == u ? void 0 : u.wrapper),
                  onWheel: e.handleMouseWheel,
                  ref: e.wrapperRef,
                },
                s().createElement(
                  "div",
                  { className: l()(Ge.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          );
        ((ze.Bar = We),
          (ze.Default = je),
          (ze.SeniorityAwards = ({ api: e, className: t, classNames: u, children: n }) => (
            (0, o.useEffect)(() => (0, Ee.v)(e.recalculateContent)),
            s().createElement(
              "div",
              { className: l()(Ge.base, t) },
              s().createElement(
                "div",
                { className: l()(Ge.wrapper, null == u ? void 0 : u.wrapper), ref: e.wrapperRef },
                s().createElement(
                  "div",
                  { className: l()(Ge.content, null == u ? void 0 : u.content), ref: e.contentRef },
                  n,
                ),
              ),
            )
          )));
        const Ue = we({
            getBounds: (e) => [0, e.scrollHeight - e.offsetHeight],
            getContainerSize: (e) => e.scrollHeight,
            getWrapperSize: (e) => e.offsetHeight,
            setScrollPosition: (e, t) => {
              e.scrollTop = t.value.scrollPosition;
            },
            getDirection: (e) => (e.deltaY > 1 ? Be.Next : Be.Prev),
          }),
          $e = "VerticalBar_base_f3",
          Ze = "VerticalBar_base__nonActive_42",
          Ve = "VerticalBar_topButton_d7",
          Xe = "VerticalBar_bottomButton_06",
          qe = "VerticalBar_track_df",
          Ke = "VerticalBar_thumb_32",
          Ye = "VerticalBar_rail_43",
          Qe = "disable",
          Je = () => {},
          et = { pending: !1, offset: 0 },
          tt = (e) => {
            var t;
            return 0.9 * (null != (t = e.getWrapperSize()) ? t : 0);
          },
          ut = (e, t) => {
            e.contentRef.current && t(e.contentRef.current);
          },
          nt = (e, t) => Math.max(20, e.offsetHeight * t),
          at = (0, o.memo)(
            ({ api: e, classNames: t = {}, getStepByRailClick: u = tt, onDrag: n = Je }) => {
              const a = (0, o.useRef)(null),
                r = (0, o.useRef)(null),
                i = (0, o.useRef)(null),
                c = (0, o.useRef)(null),
                m = (0, o.useRef)(null),
                d = e.stepTimeout || 100,
                _ = (0, o.useState)(et),
                E = _[0],
                g = _[1],
                A = (0, o.useCallback)(
                  (e) => {
                    (g(e),
                      m.current &&
                        n({ type: e.pending ? "dragStart" : "dragEnd", thumb: m.current }));
                  },
                  [n],
                ),
                p = pe(() => {
                  const t = m.current,
                    u = c.current,
                    n = e.getWrapperSize(),
                    r = e.getContainerSize();
                  if (!(n && r && t && u)) return;
                  const o = Math.min(1, n / r);
                  return (
                    (t.style.height = `${nt(u, o)}px`),
                    t.classList.add(Ke),
                    a.current &&
                      (1 === o ? a.current.classList.add(Ze) : a.current.classList.remove(Ze)),
                    o
                  );
                }),
                C = pe(() => {
                  const t = c.current,
                    u = m.current,
                    n = e.getWrapperSize(),
                    a = e.getContainerSize();
                  if (!(n && t && u && a)) return;
                  const o = e.animationScroll.scrollPosition.get(),
                    s = Math.min(1, n / a),
                    l = ge(0, 1, o / (a - n)),
                    d = (t.offsetHeight - nt(t, s)) * l;
                  ((u.style.transform = `translateY(${0 | d}px)`),
                    ((e) => {
                      if (r.current && i.current && c.current && m.current) {
                        if (0 === e)
                          return (r.current.classList.add(Qe), void i.current.classList.remove(Qe));
                        if (
                          ((t = c.current),
                          (u = m.current),
                          e - (t.offsetHeight - u.offsetHeight) >= -0.5)
                        )
                          return (r.current.classList.remove(Qe), void i.current.classList.add(Qe));
                        var t, u;
                        (r.current.classList.remove(Qe), i.current.classList.remove(Qe));
                      }
                    })(d));
                }),
                F = pe(() => {
                  ut(e, () => {
                    (p(), C());
                  });
                });
              ((0, o.useEffect)(() => (0, Ee.v)(F)),
                (0, o.useEffect)(() => {
                  const t = () => {
                    ut(e, () => {
                      C();
                    });
                  };
                  let u = Je;
                  const n = () => {
                    (u(), (u = (0, Ee.v)(F)));
                  };
                  return (
                    e.events.on("recalculateContent", F),
                    e.events.on("rest", t),
                    e.events.on("change", t),
                    e.events.on("resizeHandled", n),
                    () => {
                      (u(),
                        e.events.off("recalculateContent", F),
                        e.events.off("rest", t),
                        e.events.off("change", t),
                        e.events.off("resizeHandled", n));
                    }
                  );
                }, [e]),
                (0, o.useEffect)(() => {
                  if (!E.pending) return;
                  const t = (t) => {
                      ut(e, (u) => {
                        const a = c.current,
                          r = m.current,
                          o = e.getContainerSize();
                        if (!a || !r || !o) return;
                        const s = t.screenY - E.offset - a.getBoundingClientRect().y,
                          i = (s / a.offsetHeight) * o;
                        (e.scrollPosition.start({
                          scrollPosition: e.clampPosition(u, i),
                          reset: !0,
                          immediate: !0,
                          from: { scrollPosition: u.scrollTop },
                        }),
                          n({ type: "dragging", thumb: r, thumbOffset: s, contentOffset: i }));
                      });
                    },
                    u = () => {
                      (window.removeEventListener("mousemove", t),
                        e.handleIsThumbDragging(!1),
                        A(et));
                    };
                  return (
                    window.addEventListener("mousemove", t),
                    window.addEventListener("mouseup", u),
                    () => {
                      (window.removeEventListener("mousemove", t),
                        window.removeEventListener("mouseup", u));
                    }
                  );
                }, [e, E.offset, E.pending, n, A]));
              const h = Ce((t) => e.applyStepTo(t), d, [e]),
                b = h[0],
                v = h[1];
              (0, o.useEffect)(
                () => (
                  document.addEventListener("mouseup", v, !0),
                  () => document.removeEventListener("mouseup", v, !0)
                ),
                [v],
              );
              const D = (e) => {
                e.target.classList.contains(Qe) || (0, M.G)("highlight");
              };
              return s().createElement(
                "div",
                { className: l()($e, t.base), ref: a, onWheel: e.handleMouseWheel },
                s().createElement("div", {
                  className: l()(Ve, t.topButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Qe) ||
                      0 !== e.button ||
                      ((0, M.G)("play"), b(Be.Next));
                  },
                  ref: r,
                  onMouseEnter: D,
                }),
                s().createElement(
                  "div",
                  {
                    className: l()(qe, t.track),
                    onMouseDown: (t) => {
                      const n = m.current;
                      if (n && 0 === t.button)
                        if (((0, M.G)("play"), t.target === n))
                          (e.handleIsThumbDragging(!0),
                            A({ pending: !0, offset: t.screenY - n.getBoundingClientRect().y }));
                        else {
                          ((t) => {
                            m.current &&
                              ut(e, (n) => {
                                if (!n) return;
                                const a = u(e),
                                  r = e.clampPosition(n, n.scrollTop + a * t);
                                e.applyScroll(r);
                              });
                          })(t.screenY > n.getBoundingClientRect().y ? Be.Prev : Be.Next);
                        }
                    },
                    ref: c,
                    onMouseEnter: D,
                  },
                  s().createElement("div", { ref: m, className: t.thumb }),
                  s().createElement("div", { className: l()(Ye, t.rail) }),
                ),
                s().createElement("div", {
                  className: l()(Xe, t.bottomButton),
                  onMouseDown: (e) => {
                    e.target.classList.contains(Qe) ||
                      0 !== e.button ||
                      ((0, M.G)("play"), b(Be.Prev));
                  },
                  onMouseUp: v,
                  ref: i,
                  onMouseEnter: D,
                }),
              );
            },
          ),
          rt = {
            content: "VerticalScroll_content_cb",
            defaultScroll: "VerticalScroll_defaultScroll_f8",
            bar: "VerticalScroll_bar_1e",
            area: "VerticalScroll_area_af",
          },
          ot = ({
            children: e,
            api: t,
            className: u,
            barClassNames: n,
            areaClassName: a,
            scrollClassName: r,
            scrollClassNames: i,
            getStepByRailClick: c,
            onDrag: m,
          }) => {
            const d = (0, o.useMemo)(() => {
                const e = n || {};
                return Object.assign({}, e, { base: l()(rt.base, e.base) });
              }, [n]),
              _ = (0, o.useMemo)(() => Object.assign({}, t, { handleMouseWheel: () => {} }), [t]);
            return s().createElement(
              "div",
              { className: l()(rt.defaultScroll, u), onWheel: t.handleMouseWheel },
              s().createElement(
                "div",
                { className: l()(rt.area, a) },
                s().createElement(st, { className: r, classNames: i, api: _ }, e),
              ),
              s().createElement(at, { getStepByRailClick: c, api: t, onDrag: m, classNames: d }),
            );
          },
          st = ({ className: e, classNames: t, children: u, api: n }) => (
            (0, o.useEffect)(() => (0, Ee.v)(n.recalculateContent)),
            s().createElement(
              "div",
              { className: l()(rt.base, e), ref: n.wrapperRef, onWheel: n.handleMouseWheel },
              s().createElement(
                "div",
                { className: l()(rt.content, null == t ? void 0 : t.content), ref: n.contentRef },
                u,
              ),
            )
          );
        st.Default = ot;
        const it = { Vertical: a, Horizontal: n };
        var lt = u(4385);
        const ct = ({
            startRowIndex: e,
            cellHeight: t,
            paddingTop: u,
            paddingBottom: n,
            amount: a,
            itemsAmountPerRow: r,
            visibleRowsAmount: o,
            numOdfHeadingsBefore: s,
            numOfEmptySlotsInside: i,
          }) => {
            const l = Math.ceil(a / r) * t,
              c = o * t + 40 * i,
              m = e * t + 40 * s;
            return { paddingTop: `${m + u}rem`, paddingBottom: `${Math.max(l - m - c, 0) + n}rem` };
          },
          mt = (0, o.memo)((e) => {
            const t = e.className,
              u = e.children,
              n = e.itemsAmountPerRow,
              a = e.visibleRowsAmount,
              r = e.realFirstInRowIndex,
              o = e.amount,
              i = e.numOdfHeadingsBefore,
              l = e.numOfEmptySlotsInside,
              c = Math.min(a * n + l, o - r);
            return s().createElement(
              "div",
              { className: t, style: ct(Object.assign({}, e, { numOdfHeadingsBefore: i })) },
              (0, lt.K)(c, (e) => u(r + e)),
            );
          }),
          dt = "VirtualGrid_base_52",
          _t = ({
            amount: e,
            headingsIndexes: t,
            cellWidth: u,
            cellHeight: n,
            children: a,
            api: r,
            classNames: i,
            preloadedRows: c = 1,
            paddingTop: m = 0,
            paddingBottom: d = 0,
          }) => {
            const _ = r.scrollApi,
              E = (0, o.useRef)(0),
              g = (0, o.useState)(0),
              A = g[0],
              p = g[1],
              C = (0, o.useState)(null),
              F = C[0],
              h = C[1],
              b = (0, o.useState)(null),
              v = b[0],
              D = b[1];
            ((0, o.useEffect)(() => {
              const t = (t) => {
                if (!F) return;
                const u = Math.floor((B.O.view.pxToRem(t.value.scrollPosition) - m) / n),
                  a = Math.ceil(e / F),
                  o = Math.max(0, Math.min(u - c, a));
                (p(o), r.startRowIndexChanged(o));
              };
              return (_.events.on("change", t), () => _.events.off("change", t));
            }, [r, _, n, m, F, e, c]),
              (0, o.useEffect)(() => {
                const e = () => {
                    if (_.contentRef.current) {
                      const e = getComputedStyle(_.contentRef.current),
                        t = _.contentRef.current.getBoundingClientRect(),
                        a =
                          B.O.view.pxToRem(t.width) -
                          (parseFloat(e.paddingLeft) + parseFloat(e.paddingRight)),
                        o = Math.floor(a / u),
                        s = Math.ceil(B.O.view.pxToRem(t.height) / n) + 2 * c;
                      ((E.current = o), F !== o && h(o), D(s), r.layoutCalculated(o, s));
                    }
                  },
                  t = () => {
                    const t = E.current;
                    (e(), r.scrollToIndex(A * t));
                  };
                return (
                  _.events.on("recalculateContent", e),
                  _.events.on("resizeHandled", t),
                  () => {
                    (_.events.off("recalculateContent", e), _.events.off("resizeHandled", t));
                  }
                );
              }, [r, _, n, u, F, c, A]),
              (0, o.useEffect)(() => {
                const e = (e, t = !0) => {
                  F && _.applyScroll(Math.floor((e + 1) / F) * n + m, { immediate: t });
                };
                return (r.events.on("scrollToIndex", e), () => r.events.off("scrollToIndex", e));
              }, [r, n, F, m, _]));
            const f = (({ api: e, startRowIndex: t, itemsAmountPerRow: u, headingsIndexes: n }) => {
                const a = t * u;
                if (!n) return a;
                const r = n.reduce((e, t, n, r) => {
                  if (t < a) {
                    if (0 === n) return e + 1;
                    const a = (t - 1 - r[n - 1]) % u;
                    e += 1 - (a ? u - a : 0);
                  }
                  return e;
                }, a);
                return (e.firstCardIndexChanged(r), r);
              })({ api: r, headingsIndexes: t, startRowIndex: A, itemsAmountPerRow: F || 4 }),
              w = (({ offset: e, headingsIndexes: t }) => (t ? t.filter((t) => t < e).length : 0))({
                offset: f,
                headingsIndexes: t,
              }),
              y = (({ amount: e, offset: t, headingsIndexes: u }) =>
                u ? u.filter((u) => u >= t && u <= t + e).length : 0)({
                offset: f,
                amount: (v || 1) * (F || 4),
                headingsIndexes: t,
              }),
              k = (({ offset: e, amount: t, itemsAmountPerRow: u, headingsIndexes: n }) =>
                n
                  ? n.reduce((n, a, r, o) => {
                      if (a >= e && a <= e + t) {
                        if (0 === r) return n + 1;
                        const e = (a - 1 - o[r - 1]) % u;
                        n += 1 + (e ? u - e : 0);
                      }
                      return n;
                    }, 0)
                  : 0)({
                headingsIndexes: t,
                offset: f,
                amount: (v || 1) * (F || 4),
                itemsAmountPerRow: F || 4,
              });
            return s().createElement(
              it.Vertical.Default,
              {
                api: _,
                className: null == i ? void 0 : i.scroll,
                areaClassName: null == i ? void 0 : i.areaClassName,
                scrollClassName: null == i ? void 0 : i.scrollClassName,
                scrollClassNames: {
                  content: null == i ? void 0 : i.content,
                  wrapper: null == i ? void 0 : i.wrapper,
                },
              },
              null !== F &&
                null !== v &&
                s().createElement(
                  mt,
                  {
                    className: l()(dt, null == i ? void 0 : i.inner),
                    paddingBottom: d,
                    realFirstInRowIndex: f,
                    numOdfHeadingsBefore: w,
                    numOdfHeadingsInside: y,
                    paddingTop: m,
                    amount: e,
                    itemsAmountPerRow: F,
                    visibleRowsAmount: v,
                    numOfEmptySlotsInside: k,
                    startRowIndex: A,
                    cellHeight: n,
                  },
                  a,
                ),
            );
          },
          Et = "VirtualGridWithFade_scrollAreaFade_94",
          gt = ["api", "children", "classNames"];
        function At() {
          return (
            (At =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            At.apply(this, arguments)
          );
        }
        const pt = (e) => {
          let t = e.api,
            u = e.children,
            n = e.classNames,
            a = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, gt);
          const r = (0, o.useState)(!0),
            i = r[0],
            c = r[1],
            m = t.scrollApi;
          return (
            (0, o.useEffect)(() => {
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
            s().createElement(
              _t,
              At(
                {
                  api: t,
                  classNames: Object.assign({}, n, {
                    scrollClassName: l()(null == n ? void 0 : n.scrollClassName, i && Et),
                  }),
                },
                a,
              ),
              u,
            )
          );
        };
        var Ct = u(9480),
          Ft = u(7078),
          ht = u(9690),
          bt = u(3649);
        const vt = {
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
        let Dt, Bt;
        (!(function (e) {
          ((e.extraSmall = "extraSmall"), (e.medium = "medium"), (e.big = "big"));
        })(Dt || (Dt = {})),
          (function (e) {
            ((e.colored = "colored"), (e.white = "white"), (e.whiteSpanish = "whiteSpanish"));
          })(Bt || (Bt = {})));
        const ft = ({
            isElite: e,
            vehicleName: t,
            vehicleShortName: u,
            vehicleType: n,
            vehicleLvl: a,
            tags: r,
            isPremiumIGR: o,
            size: i = Dt.extraSmall,
            type: c = Bt.colored,
            className: m,
            classNames: d,
            isShortName: _ = !1,
          }) => {
            const E = `${(0, bt.BN)(n)}${e ? "_elite" : ""}`,
              g = R.images.gui.maps.icons.vehicleTypes.big.$dyn(E);
            return s().createElement(
              "div",
              {
                className: l()(
                  vt.base,
                  vt[`base__size${(0, bt.e)(i)}`],
                  vt[`base__type${(0, bt.e)(c)}`],
                  r && Ct.UI(r, (e) => vt[`base__tag${(0, bt.e)(e)}`]),
                  m,
                ),
              },
              s().createElement(
                "div",
                { className: l()(vt.level, null == d ? void 0 : d.level) },
                (0, ht.HG)(a),
              ),
              s().createElement("div", {
                className: l()(vt.type, e && vt.type__elite, null == d ? void 0 : d.typeIcon),
                style: { backgroundImage: `url(${g})` },
              }),
              o && s().createElement("div", { className: vt.premiumIGR }),
              s().createElement(
                "div",
                { className: l()(vt.name, null == d ? void 0 : d.name) },
                _ ? u : t,
              ),
            );
          },
          wt = "ListCardAlert_base_52",
          yt = "ListCardAlert_glow_1c",
          kt = "ListCardAlert_icon_d2",
          St = ({ className: e, tooltipArgs: t }) =>
            s().createElement(
              "div",
              { className: l()(wt, e) },
              s().createElement("div", { className: yt }),
              s().createElement(ue.i, t, s().createElement("div", { className: kt })),
            ),
          Lt = "VehicleIcon_base_80",
          xt = "VehicleIcon_icon_cc",
          It = "VehicleIcon_noImageLabel_dc",
          Nt = s().memo(function ({ techName: e, className: t }) {
            const u = R.images.gui.maps.shop.vehicles.c_180x135.$dyn(e);
            return s().createElement(
              "div",
              { className: l()(Lt, t) },
              s().createElement("div", {
                className: xt,
                style: {
                  backgroundImage: `url(${null != u ? u : R.images.gui.maps.shop.vehicles.c_180x135.empty_tank()})`,
                },
              }),
              !u &&
                s().createElement(
                  "div",
                  { className: It },
                  R.strings.crew.common.imageNotAvailable(),
                ),
            );
          }),
          Tt = "Content_base_23",
          Mt = "Content_base__default_f7",
          Rt = "Content_base__selected_0c",
          Pt = "Content_base__unclickable_b6",
          Ot = "Content_vehicleIcon_bd",
          Ht = "Content_tooltipLayer_e4",
          Wt = "Content_selectedBackground_53",
          Gt = "Content_isInInventory_7d",
          jt = "Content_premiumIcon_43",
          zt = "Content_vehicle_dd",
          Ut = "Content_vehicleType_a4",
          $t = "Content_premiumVehicleName_d3",
          Zt = ({
            isSelected: e,
            isPremium: t,
            isElite: u,
            techName: n,
            isInInventory: a,
            isTrainingAvailable: r,
            name: o,
            type: i,
            tier: c,
            tags: m,
            vehicleCD: d,
            onClick: _,
            className: E,
          }) =>
            s().createElement(
              "div",
              {
                className: l()(Tt, e ? Rt : Mt, !r && Pt, E),
                onMouseEnter: () => {
                  r && M.$.playHighlight();
                },
                onClick: () => {
                  r && _ && (_(), M.$.playClick());
                },
              },
              e && s().createElement("div", { className: Wt }),
              s().createElement(Nt, { techName: n, className: Ot }),
              a && s().createElement("div", { className: Gt }),
              s().createElement(ft, {
                isElite: u,
                vehicleName: o,
                vehicleShortName: o,
                vehicleType: i,
                vehicleLvl: c,
                tags: m,
                className: zt,
                classNames: { typeIcon: Ut, name: t ? $t : void 0 },
                type: Bt.whiteSpanish,
              }),
              s().createElement(
                Ft.t,
                { args: { tooltipId: "inventoryVehicle", vehicleCD: d } },
                s().createElement("div", { className: Ht }),
              ),
              t &&
                s().createElement(St, {
                  tooltipArgs: {
                    header: R.strings.crew.tankChange.tooltip.premium.header(),
                    body: R.strings.crew.tankChange.tooltip.premium.body(),
                  },
                  className: jt,
                }),
            );
        function Vt() {
          return (
            (Vt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Vt.apply(this, arguments)
          );
        }
        const Xt = (0, ee.Pi)(({ index: e, className: t }) => {
            const u = Q(),
              n = u.model,
              a = u.controls,
              r = Ct.U2(n.vehicleList.get(), e);
            if (!r) throw Error(`Index ${e} is out of vehicle list range`);
            return s().createElement(
              Zt,
              Vt({}, r, { className: t, onClick: () => a.selectVehicle(r.vehicleCD) }),
            );
          }),
          qt = "VehicleList_base_20",
          Kt = "VehicleList_grid_f5",
          Yt = "VehicleList_gridWrapper_a7",
          Qt = "VehicleList_emptyState_33",
          Jt = "VehicleList_item_c8",
          eu = [],
          tu = (0, ee.Pi)(() => {
            const e = (() => {
                const e = it.Vertical.useVerticalScrollApi(),
                  t = be(),
                  u = (0, o.useCallback)((e, u = !0) => t.trigger("scrollToIndex", e, u), [t]),
                  n = (0, o.useCallback)((e, u) => t.trigger("layoutCalculated", e, u), [t]),
                  a = (0, o.useCallback)((e) => t.trigger("startRowIndexChanged", e), [t]),
                  r = (0, o.useCallback)((e) => t.trigger("firstCardIndexChanged", e), [t]);
                return (0, o.useMemo)(
                  () => ({
                    scrollToIndex: u,
                    layoutCalculated: n,
                    startRowIndexChanged: a,
                    firstCardIndexChanged: r,
                    scrollApi: e,
                    events: { off: t.off, on: t.on },
                  }),
                  [u, n, a, r, e, t.off, t.on],
                );
              })(),
              t = Q(),
              u = t.model,
              n = t.controls,
              a = u.vehicleList.get().length;
            return s().createElement(
              "div",
              { id: "vehicles_list", className: qt },
              s().createElement(
                "div",
                { className: Yt },
                a > 0
                  ? s().createElement(
                      pt,
                      {
                        amount: a,
                        cellWidth: 318,
                        cellHeight: 208,
                        paddingTop: 11,
                        paddingBottom: 11,
                        headingsIndexes: eu,
                        classNames: { content: Kt },
                        api: e,
                      },
                      (e) => s().createElement(Xt, { key: e, index: e, className: Jt }),
                    )
                  : s().createElement(
                      _e,
                      {
                        warningText: R.strings.crew.tankmanList.emptyState.noFilteredItems(),
                        buttonType: J.L.primary,
                        onClick: n.resetFilters,
                        className: Qt,
                      },
                      R.strings.crew.tankmanList.emptyState.button.resetFilers(),
                    ),
              ),
            );
          }),
          uu = "TankChangeApp_base_2b",
          nu = "TankChangeApp_widget_22",
          au = "TankChangeApp_flagIcon_6c",
          ru = "TankChangeApp_topButtons_98",
          ou = "TankChangeApp_content_4f",
          su = s().memo(function () {
            const e = Q(),
              t = e.model,
              u = e.controls,
              n = (0, d.GS)().mediaHeight;
            var a;
            return (
              (a = u.closeWithEsc),
              y(f.n.ESCAPE, a),
              s().createElement(
                "div",
                { className: uu },
                s().createElement(x, { className: au, nation: t.nation.get(), size: S.c1080x454 }),
                s().createElement(
                  "div",
                  { className: ou },
                  s().createElement(T, {
                    title: R.strings.crew.tankChange.title(),
                    theme: N.TankChange,
                  }),
                  s().createElement(q.p, {
                    popoverDirection: n < d.Aq.Medium ? D.IC.Left : D.IC.Bottom,
                  }),
                  s().createElement(tu, null),
                ),
                s().createElement("div", { className: nu }, s().createElement(X.O, null)),
                s().createElement(V, {
                  onBackClick: u.back,
                  backButtonLabel: t.backButtonLabel.get(),
                  onCloseClick: u.hangar,
                  closeButtonLabel: R.strings.crew.common.navigation.toGarage(),
                  className: t.isButtonBarVisible.get() && ru,
                }),
              )
            );
          });
        engine.whenReady.then(() => {
          v().render(
            s().createElement(Y, null, s().createElement(h, null, s().createElement(su, null))),
            document.getElementById("root"),
          );
        });
      },
      9367: (e, t, u) => {
        "use strict";
        u.d(t, { Q: () => m });
        var n = u(6483),
          a = u.n(n),
          r = u(9987),
          o = u(6179),
          s = u.n(o);
        const i = "AlertCounter_base_f3",
          l = "AlertCounter_counter_da",
          c = "AlertCounter_label_18",
          m = ({ value: e, className: t }) =>
            s().createElement(
              "div",
              { className: a()(i, t) },
              s().createElement(r.A, { value: e, className: l }),
              !e &&
                s().createElement("div", { className: c }, R.strings.crew.common.exclamationMark()),
            );
      },
      9197: (e, t, u) => {
        "use strict";
        u.d(t, { C: () => D });
        var n = u(6483),
          a = u.n(n),
          r = u(3112),
          o = u(6179),
          s = u.n(o),
          i = u(7613),
          l = u(6373);
        const c = "NumberRange_base_5e",
          m = "NumberRange_base__animation_79",
          d = "NumberRange_from_70",
          _ = "NumberRange_from__red_f8",
          E = "NumberRange_separator_c0",
          g = R.strings.crew.barracks.berthsAmountDivider(),
          A = R.strings.crew.filterPanel.counter.selectLimit,
          p = (0, o.memo)(function ({
            isFilterRange: e,
            from: t,
            to: u,
            className: n,
            isSelectMode: r = !1,
            isSelectedLimitReached: o = !1,
          }) {
            return r
              ? s().createElement(
                  l.i,
                  { header: A.header(), body: A.body(), ignoreShowDelay: !0 },
                  s().createElement(
                    "div",
                    { className: a()(c, n) },
                    s().createElement(i.ZP, { className: d, text: String(t) }),
                    (t !== u || o) &&
                      s().createElement(
                        s().Fragment,
                        null,
                        s().createElement(i.ZP, { className: E, text: g }),
                        s().createElement(i.ZP, { text: String(u) }),
                      ),
                  ),
                )
              : e
                ? s().createElement(
                    "div",
                    { className: a()(c, 0 === t && m, n) },
                    s().createElement(i.ZP, {
                      className: a()(d, 0 === t && u > 0 && _),
                      text: String(t),
                    }),
                    t !== u &&
                      s().createElement(
                        s().Fragment,
                        null,
                        s().createElement(i.ZP, { className: E, text: g }),
                        s().createElement(i.ZP, { text: String(u) }),
                      ),
                  )
                : s().createElement(
                    "div",
                    { className: a()(c, t > u && m, n) },
                    s().createElement(i.ZP, { className: a()(d, t > u && _), text: String(t) }),
                    s().createElement(i.ZP, { className: E, text: g }),
                    s().createElement(i.ZP, { text: String(u) }),
                  );
          }),
          C = "NumberRangeWithLabel_base_2b",
          F = "NumberRangeWithLabel_title_94",
          h = "NumberRangeWithLabel_counter_00",
          b = "NumberRangeWithLabel_counterGlow_1f",
          v = "NumberRangeWithLabel_blink_89",
          D = (0, o.memo)(
            ({
              title: e,
              isGlowVisible: t = !1,
              isSelectedLimitReached: u = !1,
              isFilterRange: n = !1,
              isSelectMode: o = !1,
              className: l,
              classNames: c,
              from: m,
              to: d,
            }) => {
              const _ = (0, r.V)(),
                E = {
                  left:
                    m !== d || u
                      ? 7 * String(m).length * _ + 4 * _
                      : Math.round((7 * String(m).length * _) / 2),
                };
              return s().createElement(
                "div",
                { className: a()(C, l) },
                s().createElement(i.ZP, { className: F, text: e }),
                s().createElement(
                  "div",
                  { className: h },
                  s().createElement(p, {
                    isFilterRange: n,
                    isSelectedLimitReached: u,
                    isSelectMode: o,
                    from: m,
                    to: d,
                  }),
                  t &&
                    n &&
                    s().createElement("div", {
                      style: E,
                      className: a()(b, u && v, null == c ? void 0 : c.counterGlow),
                    }),
                ),
              );
            },
          );
      },
      7077: (e, t, u) => {
        "use strict";
        u.d(t, { G: () => m, U: () => l });
        var n = u(6483),
          a = u.n(n),
          r = u(3649),
          o = u(6179),
          s = u.n(o),
          i = u(3938);
        let l;
        !(function (e) {
          ((e.c158x118 = "big"),
            (e.c100x60 = "small"),
            (e.c100x60Barracks = "barracks"),
            (e.c444x300 = "special"),
            (e.c204x256 = "c_204x256"));
        })(l || (l = {}));
        const c = R.images.gui.maps.icons.tankmen.icons,
          m = (0, o.memo)(({ name: e, size: t = l.c100x60, className: u, isSkin: n = !1 }) => {
            const o = (n ? c.$dyn(t).$dyn("crewSkins") : c.$dyn(t)).$dyn((0, r.BN)(e)),
              m = t === l.c204x256;
            return s().createElement(
              "div",
              {
                style: { backgroundImage: `url(${o})` },
                className: a()(i.Z.base, i.Z[`base__${t}`], u),
              },
              m && s().createElement("div", { className: i.Z.innerShadow }),
            );
          });
      },
      8485: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => l, d: () => c });
        var n = u(6483),
          a = u.n(n),
          r = u(8271),
          o = u(6179),
          s = u.n(o),
          i = u(9426);
        let l;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(l || (l = {}));
        const c = s().memo(function ({ icon: e, type: t, size: u }) {
          const n = (0, o.useMemo)(() => {
              let e;
              return (
                (e =
                  t === r.W.Possible || t === r.W.New
                    ? R.images.gui.maps.icons.tankmen.skills.medium.new_skill()
                    : R.images.gui.maps.icons.crew.$dyn(`${t}SkillFrame_${u}`)),
                { backgroundImage: `url(${e})` }
              );
            }, [t, u]),
            c = (0, o.useMemo)(() => {
              if (!e) return null;
              return {
                backgroundImage: `url(${R.images.gui.maps.icons.tankmen.skills.$dyn(u === l.Big ? "c_22x22" : "small").$dyn(e)})`,
              };
            }, [e, u]);
          return s().createElement(
            "div",
            { className: a()(i.Z.base, i.Z[`base__${u}`]) },
            s().createElement("div", { className: i.Z.bg, style: n }),
            c &&
              s().createElement("div", { className: a()(i.Z.icon, i.Z[`icon__${t}`]), style: c }),
          );
        });
      },
      9631: (e, t, u) => {
        "use strict";
        u.d(t, { C: () => _ });
        var n = u(6483),
          a = u.n(n),
          r = u(3457),
          o = u(2106),
          s = u(9987),
          i = u(6179),
          l = u.n(i),
          c = u(4723);
        const m = ["isActive", "counter", "className", "children", "type", "size", "hasIndicator"];
        function d() {
          return (
            (d =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            d.apply(this, arguments)
          );
        }
        const _ = l().memo(function (e) {
          let t = e.isActive,
            u = e.counter,
            n = e.className,
            i = e.children,
            _ = e.type,
            E = void 0 === _ ? o.L.secondary : _,
            g = e.size,
            A = void 0 === g ? o.q.small : g,
            p = e.hasIndicator,
            C = void 0 === p || p,
            F = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, m);
          return l().createElement(
            "div",
            { className: a()(c.Z.base, n, t && c.Z.base__active) },
            l().createElement(r.u5, d({ type: E, size: A, mixClass: c.Z.button }, F), i),
            l().createElement("div", { className: c.Z.overlay }),
            C && l().createElement("div", { className: c.Z.indicator }),
            Boolean(u) &&
              l().createElement(
                "div",
                { className: c.Z.counter },
                l().createElement(s.A, { value: u, size: "small" }),
              ),
          );
        });
      },
      7160: (e, t, u) => {
        "use strict";
        u.d(t, { BH: () => r, Fs: () => o, ei: () => n, qb: () => a });
        const n = (e) => Math.sqrt(1 - Math.pow(--e, 2)),
          a = (e) => (e < 0.5 ? 4 * e * e * e : 1 - Math.pow(-2 * e + 2, 3) / 2),
          r = (e) => {
            const t = 1.70158;
            return 1 + 2.70158 * Math.pow(e - 1, 3) + t * Math.pow(e - 1, 2);
          },
          o = (e) => -(Math.cos(Math.PI * e) - 1) / 2;
      },
      8018: (e, t, u) => {
        "use strict";
        u.d(t, { Er: () => r, Gc: () => s, Xd: () => a, gO: () => o, wP: () => n });
        u(3649);
        R.strings.common.percentValue();
        let n;
        !(function (e) {
          ((e.Objective = "objective"), (e.Possessive = "possessive"));
        })(n || (n = {}));
        const a = {
            header: R.strings.crew.filterPanel.counter.reset.header(),
            body: R.strings.crew.filterPanel.counter.reset.body(),
          },
          r = {
            header: R.strings.crew.filterPanel.counterMultySelect.reset.header(),
            body: R.strings.crew.filterPanel.counterMultySelect.reset.body(),
          };
        let o;
        !(function (e) {
          ((e.CREW_FREEXP_HIGHLIGHT = "crew_crewbook_freeexp_highlight"),
            (e.SHOP_INFO = "shop_info"),
            (e.RUDY = "rudy"));
        })(o || (o = {}));
        const s = (e, t = !1, u = null) => {
          const n = t
            ? R.strings.item_types.tankman.roles.female
            : R.strings.item_types.tankman.roles;
          return (u ? n.$dyn(`${u}Case`) : n).$dyn(e);
        };
      },
      8727: (e, t, u) => {
        "use strict";
        u.d(t, { O: () => un });
        var n = u(6179),
          a = u.n(n),
          r = u(7727),
          o = u(3403),
          s = u(3215),
          i = u(4598),
          l = u(5175),
          c = u(9480),
          m = u(9174),
          d = u(3946),
          _ = u(4828);
        const E = [
            R.views.lobby.crew.TankmanContainerView("resId"),
            R.views.lobby.crew.personal_case.PersonalFileView("resId"),
            R.views.lobby.crew.personal_case.PersonalDataView("resId"),
            R.views.lobby.crew.personal_case.ServiceRecordView("resId"),
          ],
          g = (0, s.q)()(
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
                u = (0, d.Om)(() => (0, l.c)(t.slots.get()), { equals: i.jv }),
                n = (0, d.Om)(() => Boolean(c.sE(u(), (e) => -1 === e.tankman.tankmanID))),
                a = (0, d.Om)(() => 1 === t.slots.get().length),
                r = (0, d.Om)((e) => t.selectedSlotIdx.get() === e),
                o = (0, d.Om)(() => -1 !== t.selectedSlotIdx.get()),
                s = (0, d.Om)((e) => {
                  var t;
                  return null == (t = c.U2(u(), e)) ? void 0 : t.tankman;
                }),
                g = (0, d.Om)((e) => {
                  var t;
                  const n = null == (t = c.U2(u(), e)) ? void 0 : t.tankman;
                  return n ? n.skills.length + n.newSkillsAmount + n.possibleSkillsAmount : 0;
                }),
                A = (0, d.Om)(() => {
                  return (
                    (e = t.currentLayoutID.get()),
                    (u = t.previousLayoutID.get()),
                    {
                      isCurrentLayoutHangar: e === R.views.lobby.crew.HangarCrewWidget("resId"),
                      isCurrentLayoutTankmanContainer: E.includes(e),
                      isCurrentLayoutQuickTraining:
                        e === R.views.lobby.crew.QuickTrainingView("resId"),
                      isCurrentLayoutMemberChange:
                        e === R.views.lobby.crew.MemberChangeView("resId"),
                      isPreviousLayoutHangar: u === R.views.lobby.crew.HangarCrewWidget("resId"),
                      isPreviousLayoutTankmanContainer: E.includes(u),
                      isPreviousLayoutQuickTraining:
                        u === R.views.lobby.crew.QuickTrainingView("resId"),
                      isPreviousLayoutMemberChange:
                        u === R.views.lobby.crew.MemberChangeView("resId"),
                      isPreviousLayoutBarrack: u === R.views.lobby.crew.BarracksView("resId"),
                    }
                  );
                  var e, u;
                }),
                p = (0, d.Om)(() => {
                  const e = A(),
                    t = e.isCurrentLayoutHangar,
                    u = e.isCurrentLayoutQuickTraining;
                  return !a() && !t && !u;
                }),
                C = (0, d.Om)(() => !a() && t.buttonsBar.get().isVisible),
                F = (0, d.Om)(() => {
                  return ((e = t.currentLayoutID.get()), _.AB[e] || _.sC.Hangar);
                  var e;
                });
              return Object.assign({}, t, {
                computes: {
                  getSlots: u,
                  isSlotSelected: r,
                  isAnySlotSelected: o,
                  getSlotTankman: s,
                  getAllSkillsAmount: g,
                  isAnyEmptySlots: n,
                  isTankmanMode: a,
                  isChangeCrewButtonVisible: p,
                  isButtonBarVisible: C,
                  getLayoutInfo: A,
                  getUiLoggingParentScreen: F,
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
          A = g[0],
          p = g[1];
        var C = u(6483),
          F = u.n(C),
          h = u(7613),
          b = u(6373),
          v = u(2056);
        let D;
        !(function (e) {
          ((e.On = "on"), (e.Off = "off"), (e.Disabled = "disabled"), (e.Hidden = "hidden"));
        })(D || (D = {}));
        const B = "ButtonsBar_base_9c",
          f = "ButtonsBar_button_d1",
          w = "ButtonsBar_button__crewOperaions_70",
          y = "ButtonsBar_button__crewBooks_b4",
          k = "ButtonsBar_button__toggle_64",
          S = "ButtonsBar_acceleratedTrainingContainer_ee",
          L = "ButtonsBar_acceleratedTrainingContainer__visible_79",
          x = "ButtonsBar_acceleratedTraining_94",
          I = "ButtonsBar_acceleratedTraining__icon_9b",
          N = "ButtonsBar_acceleratedTraining__label_ad";
        var T = u(3457),
          M = u(9987),
          P = u(3649);
        const O = "CrewBookButton_base_da",
          H = "CrewBookButton_button_ee",
          W = "CrewBookButton_icon_11",
          G = "CrewBookButton_discount_6b",
          j = "CrewBookButton_counter_5d",
          z = (0, o.Pi)(({ classMix: e, isWidgetDisabled: t }) => {
            const u = p(),
              n = u.model,
              r = u.controls,
              o = n.crewBooks.get(),
              s = r.onCrewBooksClick;
            return a().createElement(
              b.i,
              {
                header: R.strings.crew_widget.tooltip.buttonsBar.crewBooks.header(),
                body: (0, P.uF)(R.strings.crew_widget.tooltip.buttonsBar.crewBooks.body(), {
                  count: o.totalAmount,
                }),
              },
              a().createElement(
                "div",
                { id: "crew_book_button", className: F()(O, e) },
                a().createElement(
                  T.u5,
                  { type: T.L$.primary, mixClass: H, disabled: o.isDisabled || t, onClick: s },
                  a().createElement("div", { className: W }),
                ),
                o.newAmount > 0 &&
                  a().createElement(
                    "div",
                    { className: j },
                    a().createElement(M.A, { value: o.newAmount }),
                  ),
                o.hasDiscount && a().createElement("div", { className: G }),
              ),
            );
          });
        var U = u(3616);
        const $ = ["children"];
        function Z() {
          return (
            (Z =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Z.apply(this, arguments)
          );
        }
        const V = (e) => {
          let t = e.children,
            u = (function (e, t) {
              if (null == e) return {};
              var u,
                n,
                a = {},
                r = Object.keys(e);
              for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
              return a;
            })(e, $);
          return a().createElement(
            U.Z,
            Z(
              {
                decoratorId:
                  R.views.common.pop_over_window.backport_pop_over.BackportPopOverWindow("resId"),
                contentId:
                  R.views.common.pop_over_window.backport_pop_over.BackportPopOverContent("resId"),
              },
              u,
            ),
            t,
          );
        };
        var X = u(4489);
        let q;
        !(function (e) {
          ((e[(e.LEFT = 0)] = "LEFT"),
            (e[(e.WHEEL = 1)] = "WHEEL"),
            (e[(e.RIGHT = 2)] = "RIGHT"),
            (e[(e.FOURTH = 3)] = "FOURTH"),
            (e[(e.FIFTH = 4)] = "FIFTH"));
        })(q || (q = {}));
        var K = u(1943);
        const Y = "CrewOperationsButton_base_e3",
          Q = "CrewOperationsButton_button_8e",
          J = "CrewOperationsButton_icon_0c",
          ee = "CrewOperationsButton_autoReturnIcon_f0",
          te = (0, o.Pi)(({ classMix: e, isWidgetDisabled: t }) => {
            const u = p().model,
              n = ((e) => {
                const t = (0, K.Jp)(_.D9);
                return (u) => t({ action: _.eX.Click, parentScreen: e, item: u });
              })(u.computes.getUiLoggingParentScreen()),
              r = u.crewOperations.get();
            return a().createElement(
              "div",
              { id: "crew_operations_button", className: F()(Y, e) },
              a().createElement(
                V,
                {
                  targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  isEnabled: !t,
                  onClick: () => n(_.x3.CrewOperationsButton),
                },
                a().createElement(
                  b.i,
                  {
                    header: R.strings.crew_widget.tooltip.buttonsBar.crewOperations.header(),
                    body: R.strings.crew_widget.tooltip.buttonsBar.crewOperations.body(),
                  },
                  a().createElement(
                    "div",
                    null,
                    a().createElement(
                      T.u5,
                      { type: T.L$.primary, mixClass: Q, disabled: t },
                      a().createElement("div", { className: J }),
                    ),
                    r.isAutoReturnOn && a().createElement("div", { className: ee }),
                  ),
                ),
              ),
            );
          });
        var ue = u(9631);
        const ne = "CrewToggleButton_base_03",
          ae = "CrewToggleButton_button_89",
          re = "CrewToggleButton_iconContainer_f9",
          oe = "CrewToggleButton_icon_a7";
        let se;
        !(function (e) {
          e.WotPlus = "wotPlus";
        })(se || (se = {}));
        const ie = (0, n.memo)(({ type: e, state: t, isDisabled: u, onClick: r, classMix: o }) => {
            const s = (0, n.useMemo)(() => {
              const u = t === D.Disabled ? D.Off : t;
              return {
                backgroundImage: `url(R.images.gui.maps.icons.crewWidget.buttonsBar.icons.${e}_${u})`,
              };
            }, [e, t]);
            return a().createElement(
              "div",
              { className: F()(ne, o) },
              a().createElement(
                ue.C,
                {
                  type: T.L$.primary,
                  isActive: t === D.On,
                  disabled: u || t === D.Disabled,
                  className: ae,
                  onClick: r,
                },
                a().createElement(
                  "div",
                  { className: re },
                  a().createElement("div", { className: oe, style: s }),
                ),
              ),
            );
          }),
          le = R.strings.crew.acceleratedTraining,
          ce = (0, o.Pi)(({ isWidgetDisabled: e, isCurrentLayoutHangar: t }) => {
            const u = p(),
              n = u.model,
              r = u.controls,
              o = n.isWidgetHover.get(),
              s = n.isAcceleratedTraining.get(),
              i = n.wotPlus.get(),
              l = r.onWotPlusClick;
            return a().createElement(
              "div",
              { className: B },
              a().createElement(te, { classMix: F()(f, w), isWidgetDisabled: e }),
              a().createElement(z, { classMix: F()(f, y), isWidgetDisabled: e }),
              i.state !== D.Hidden &&
                a().createElement(
                  v.u,
                  {
                    contentId: R.views.lobby.crew.CrewHeaderTooltipView("resId"),
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  },
                  a().createElement(
                    "div",
                    null,
                    a().createElement(ie, {
                      type: se.WotPlus,
                      state: i.state,
                      isDisabled: e || i.isDisabled,
                      onClick: l,
                      classMix: F()(f, k),
                    }),
                  ),
                ),
              a().createElement(
                "div",
                { className: F()(S, (!t || o) && L) },
                s &&
                  a().createElement(
                    b.i,
                    { header: le.tooltip.header(), body: le.tooltip.body() },
                    a().createElement(
                      "div",
                      { className: x },
                      a().createElement("div", { className: I }),
                      a().createElement(h.ZP, { className: N, text: le.label() }),
                    ),
                  ),
              ),
            );
          }),
          me = "CrewWidgetApp_base_cc",
          de = "CrewWidgetApp_buttonsBar_e5",
          _e = "CrewWidgetApp_slotsList_ee";
        var Ee = u(7030),
          ge = u(8018),
          Ae = u(7160);
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
          Ce = (0, n.memo)(
            ({
              onClick: e,
              children: t,
              isSelected: u = !1,
              isDisabled: o,
              isEnabledForMouse: s,
              isEmpty: i = !1,
              isWidgetHovered: l = !0,
              layoutInfo: c,
            }) => {
              const m = (0, n.useState)(!1),
                d = m[0],
                _ = m[1],
                E = d && (!u || (!i && c.isCurrentLayoutMemberChange)),
                g = E && !i && !c.isCurrentLayoutHangar;
              return a().createElement(
                "div",
                {
                  className: F()(
                    pe.base,
                    (d || u) && !c.isCurrentLayoutHangar && pe.base__hovered,
                    (u || !s) && pe.base__inactive,
                    c.isCurrentLayoutHangar && l && pe.base__widgetHovered,
                  ),
                  onClick: e,
                  onMouseEnter: () => {
                    s && !u && (r.$.playHighlight(), _(!0));
                  },
                  onMouseLeave: () => {
                    _(!1);
                  },
                },
                a().createElement("div", { className: pe.background }),
                !c.isCurrentLayoutMemberChange &&
                  a().createElement("div", {
                    className: F()(pe.selectedGlow, u && pe.selectedGlow__visible),
                  }),
                a().createElement("div", {
                  className: F()(pe.hoverGlow, g && pe.hoverGlow__visible),
                }),
                a().createElement("div", { className: F()(pe.hover, E && pe.hover__visible) }),
                o && a().createElement("div", { className: pe.disabled }),
                t,
              );
            },
          ),
          Fe = ({
            startState: e,
            endState: t,
            layoutInfo: u,
            isPaused: r,
            children: o,
            className: s,
            isTankmanMode: i,
          }) => {
            const l = (0, Ee.useSpring)(
                () => ({ from: e, to: t, config: { duration: 300, easing: Ae.qb }, pause: r }),
                [r],
              )[0],
              c = (0, n.useMemo)(
                () =>
                  u.isCurrentLayoutHangar || u.isCurrentLayoutQuickTraining || i
                    ? e
                    : (!u.isPreviousLayoutHangar && !u.isPreviousLayoutBarrack) || r
                      ? t
                      : l,
                [u, r, l, e, t, i],
              );
            return a().createElement(Ee.animated.div, { className: s, style: c }, o);
          },
          he = "DogSlot_base_8f",
          be = "DogSlot_icon_ba",
          ve = "DogSlot_container_63",
          De = "DogSlot_roleAndName_c9",
          Be = "DogSlot_role_5c",
          fe = "DogSlot_name_9c",
          we = "DogSlot_name__hidden_56",
          ye = "DogSlot_btnDetails_b7",
          ke = "DogSlot_btnDetails__hidden_44",
          Se = "DogSlot_infoIcon_09",
          Le = "DogSlot_infoIcon__hidden_8e",
          xe = { transform: "translateX(0rem)" },
          Ie = (0, o.Pi)(({ isDisabled: e, layoutInfo: t }) => {
            const u = p(),
              o = u.model,
              s = u.controls,
              i = o.nation.get(),
              l = o.isWidgetHover.get(),
              c = s.onDogMoreInfoClick,
              m = (0, n.useCallback)(() => {
                !e && (0, r.G)(ge.gO.RUDY);
              }, [e]),
              d = (0, n.useCallback)(
                (t) => {
                  (t.stopPropagation(), !e && c());
                },
                [c, e],
              ),
              _ = (0, Ee.useSpring)(
                () => ({
                  from: xe,
                  to: { transform: "translateX(16rem)" },
                  config: { duration: 300, easing: Ae.qb },
                  pause: !t.isCurrentLayoutQuickTraining,
                }),
                [t],
              )[0],
              E = R.strings.tooltips.hangar.crew.rudy.dog.$dyn(i);
            return a().createElement(
              b.i,
              { header: E.header(), body: E.body() },
              a().createElement(
                "div",
                null,
                a().createElement(
                  Ce,
                  {
                    onClick: m,
                    isDisabled: e,
                    isEnabledForMouse: !1,
                    layoutInfo: t,
                    isWidgetHovered: l,
                  },
                  a().createElement(
                    Fe,
                    {
                      startState: xe,
                      endState: { transform: "translateX(42rem)" },
                      layoutInfo: t,
                      isPaused: !1,
                      className: he,
                      isTankmanMode: !1,
                    },
                    a().createElement(Ee.animated.div, { className: be, style: _ }),
                    a().createElement(
                      "div",
                      { className: ve },
                      a().createElement(
                        "div",
                        { className: De },
                        a().createElement("div", { className: Be }),
                        a().createElement(h.ZP, {
                          className: F()(fe, t.isCurrentLayoutHangar && !l && we),
                          text: R.strings.menu.hangar.crew.rody.dog.$dyn(i).name(),
                        }),
                      ),
                      a().createElement(
                        "div",
                        { className: F()(ye, t.isCurrentLayoutHangar && !l && ke) },
                        a().createElement(
                          T.u5,
                          { onClick: d },
                          a().createElement(h.ZP, { text: R.strings.crew_widget.btnDetails() }),
                        ),
                      ),
                      a().createElement("div", {
                        className: F()(Se, (!t.isCurrentLayoutHangar || l) && Le),
                      }),
                    ),
                  ),
                ),
              ),
            );
          });
        var Ne = u(4179);
        const Te = ({
            children: e,
            contentID: t,
            decoratorID: u = 0,
            targetId: a = 0,
            args: o,
            isEnabled: s = !0,
            onMouseDown: i,
          }) => {
            const l = (0, n.useCallback)(() => {
                ((0, Ne.c9)(Ne.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: a,
                  isMouseEvent: !0,
                  on: !0,
                  args: o,
                }),
                  r.$.playYes());
              }, [o, t, u, a]),
              c = (0, n.useCallback)(() => {
                (0, Ne.c9)(Ne.B0.CONTEXT_MENU, {
                  contentID: t,
                  decoratorID: u,
                  targetID: a,
                  isMouseEvent: !1,
                  on: !1,
                });
              }, [t, u, a]),
              m = (0, n.useCallback)(
                (e) => {
                  (i && i(e), ((e) => e.button === q.RIGHT)(e) && l());
                },
                [i, l],
              );
            return (
              (0, n.useEffect)(() => {
                !1 === s && c();
              }, [s, c]),
              s ? (0, n.cloneElement)(e, { onMouseDown: m }) : e
            );
          },
          Me = ["children"];
        function Re() {
          return (
            (Re =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Re.apply(this, arguments)
          );
        }
        const Pe = (e) => {
            let t = e.children,
              u = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Me);
            return a().createElement(
              Te,
              Re({}, u, { contentID: R.views.common.BackportContextMenu("resId") }),
              t,
            );
          },
          Oe = "ChangeCrewButton_base_0f",
          He = "ChangeCrewButton_base__inactive_77",
          We = "ChangeCrewButton_normalState_07",
          Ge = "ChangeCrewButton_normalState__hide_db",
          je = "ChangeCrewButton_hoverState_68",
          ze = "ChangeCrewButton_hoverState__show_89",
          Ue = (0, o.Pi)(({ isSelected: e, isLocked: t, mainRole: u, isFemale: o }) => {
            const s = p().model,
              i = (0, n.useState)(!1),
              l = i[0],
              c = i[1],
              m = (0, K.Sr)(_.D9, {
                item: _.x3.ChangeButtonTooltip,
                action: _.eX.Viewed,
                parentScreen: s.computes.getUiLoggingParentScreen(),
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
                          role: (0, ge.Gc)(u, o, ge.wP.Objective),
                        }),
                      ],
                [t, o, u],
              ),
              E = d[0],
              g = d[1];
            return a().createElement(
              b.i,
              {
                header: E,
                body: g,
                targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                ignoreMouseClick: !0,
              },
              a().createElement(
                "div",
                {
                  className: F()(Oe, (t || e) && He),
                  onMouseEnter: () => {
                    (m.onShow(), t || e || (r.$.playHighlight(), c(!0)));
                  },
                  onMouseLeave: () => {
                    (m.onHide(), c(!1));
                  },
                },
                a().createElement("div", { className: F()(We, l && Ge) }),
                a().createElement("div", { className: F()(je, (e || l) && ze) }),
              ),
            );
          }),
          $e = "CrewSlot_base_ac",
          Ze = "CrewSlot_changeCrew_02",
          Ve = "CrewSlot_content_5b",
          Xe = "CrewSlot_content__withChangeCrewButton_4e",
          qe = "CrewSlot_warningHighlight_ff",
          Ke = "CrewSlot_selectHighlight_50",
          Ye = "CrewSlot_selectHighlightInTankmanMode_37";
        var Qe = u(7077);
        const Je = "AcceleratedTrainingIcon_base_4f",
          et = "AcceleratedTrainingIcon_icon_45",
          tt = (0, n.memo)(({ classMix: e }) =>
            a().createElement(
              b.i,
              {
                header: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.header(),
                body: R.strings.crew_widget.tooltip.buttonsBar.acceleratedTraining_on.body(),
              },
              a().createElement(
                "div",
                { className: F()(Je, e) },
                a().createElement("div", { className: et }),
              ),
            ),
          ),
          ut = "SpecializationAndName_base_ef",
          nt = "SpecializationAndName_roleWrapper_87",
          at = "SpecializationAndName_secondaryRolesWrapper_d0",
          rt = "SpecializationAndName_secondaryRolesWrapper__hidden_ac",
          ot = "SpecializationAndName_role_55",
          st = "SpecializationAndName_role__withGap_35",
          it = "SpecializationAndName_percent_e6",
          lt = "SpecializationAndName_percent__untrained_1b",
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
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Et.apply(this, arguments)
          );
        }
        const gt = (0, o.Pi)(
            ({
              roles: e,
              specializationLevel: t = 0,
              tankmanID: u,
              isUntrained: n,
              name: r,
              isCurrentLayoutHangar: o,
              isAcceleratedTrainingAvailable: s,
            }) => {
              const i = p().model,
                l = (0, K.Sr)(_.D9, {
                  item: _.x3.MstlTooltip,
                  action: _.eX.Viewed,
                  parentScreen: i.computes.getUiLoggingParentScreen(),
                }),
                c = e[0],
                m = e.slice(1),
                d = i.isWidgetHover.get();
              return a().createElement(
                "div",
                { className: ut },
                a().createElement(
                  v.u,
                  Et(
                    {
                      targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                      contentId: R.views.lobby.crew.tooltips.TrainingLevelTooltip("resId"),
                      args: { tankmanID: u },
                      isEnabled: Boolean(u),
                      ignoreMouseClick: !0,
                    },
                    l,
                  ),
                  a().createElement(
                    "div",
                    { className: nt },
                    a().createElement("div", {
                      key: `role__${c}`,
                      className: ot,
                      style: {
                        backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(c)})`,
                      },
                    }),
                    a().createElement(
                      "div",
                      { className: F()(at, o && !d && rt) },
                      m.map((e) =>
                        a().createElement("div", {
                          key: `role__${e}`,
                          className: F()(ot, st),
                          style: {
                            backgroundImage: `url(${R.images.gui.maps.icons.tankmen.roles.c_18x18.$dyn(e)})`,
                          },
                        }),
                      ),
                    ),
                    t > 0 &&
                      a().createElement(h.ZP, {
                        className: F()(it, n && lt, o && !d && ct),
                        style: { "--marginLeft": -23 * (e.length - 1) + 4 + "rem" },
                        text: (0, P.uF)(R.strings.common.percentValue(), { value: t }),
                      }),
                  ),
                ),
                s && a().createElement(tt, { classMix: mt }),
                a().createElement(h.ZP, { className: F()(dt, o && !d && _t), text: r || "" }),
              );
            },
          ),
          At = "EmptySlotContent_base_77",
          pt = "EmptySlotContent_tankmanIcon_07",
          Ct = "EmptySlotContent_icon_a8",
          Ft = "EmptySlotContent_specialization_1f",
          ht = "EmptySlotContent_specialization__disabled_3d",
          bt = "EmptySlotContent_vehicle_55",
          vt = { transform: "translateX(0rem)", opacity: 1 },
          Dt = { transform: "translateX(-70rem)", opacity: 0 },
          Bt = (0, n.memo)(
            ({
              roles: e,
              layoutInfo: t,
              vehicleName: u,
              vehicleType: n,
              isDisabled: r,
              isSelected: o,
              blinkStyle: s,
              qtTankmanIconStyle: i,
            }) => {
              const l = (0, Ee.useSpring)(
                  () => ({
                    from: vt,
                    to: Dt,
                    config: { duration: 200, easing: Ae.ei },
                    immediate: !0,
                    pause: o,
                  }),
                  [o],
                ),
                m = l[0],
                d = l[1],
                _ = () => {
                  t.isCurrentLayoutQuickTraining || d.start({ reset: !0, reverse: !0 });
                },
                E = c.U2(e, 0) || "",
                g = R.strings.crew_widget.vehicleWithName.$dyn((0, P.BN)(n)),
                A = (0, P.uF)(R.strings.crew_widget.emptySlot.chooseTankman(), {
                  role: R.strings.item_types.tankman.roles.objectiveCase.$dyn(E),
                });
              return a().createElement(
                "div",
                { className: At, onMouseEnter: _, onMouseLeave: _ },
                a().createElement(
                  "div",
                  { className: pt },
                  a().createElement(
                    Ee.animated.div,
                    { style: i },
                    a().createElement(Qe.G, {
                      name: "empty",
                      size: Qe.U.c100x60Barracks,
                      className: Ct,
                    }),
                    a().createElement(
                      Ee.animated.div,
                      { style: r ? void 0 : s },
                      a().createElement(Qe.G, {
                        name: "emptyRed",
                        size: Qe.U.c100x60Barracks,
                        className: Ct,
                      }),
                    ),
                  ),
                ),
                a().createElement(
                  "div",
                  { className: F()(Ft, r && ht) },
                  a().createElement(gt, {
                    tankmanID: 0,
                    roles: e,
                    name: A,
                    isUntrained: !0,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                  }),
                ),
                a().createElement(
                  Ee.animated.div,
                  { className: bt, style: o ? void 0 : m },
                  (0, P.uF)(g, { name: u }),
                ),
              );
            },
          );
        var ft = u(7078),
          wt = u(2603),
          yt = u(5415);
        const kt = (e) => e.skills.length + e.newSkillsAmount + e.possibleSkillsAmount;
        var St = u(8271),
          Lt = u(4385);
        const xt = {
            base: "RoleLevelIcon_base_e1",
            realLevel: "RoleLevelIcon_realLevel_96",
            base__small: "RoleLevelIcon_base__small_ce",
            icon: "RoleLevelIcon_icon_fa",
          },
          It = (0, n.memo)(({ percentValue: e, skillSize: t, hasSkills: u }) => {
            const n = u ? R.strings.crew_widget.plusValue() : R.strings.crew_widget.plusSpecValue();
            return a().createElement(
              b.i,
              {
                header: R.strings.crew_widget.tooltip.roleLevelIcon.header(),
                body: R.strings.crew_widget.tooltip.roleLevelIcon.body(),
              },
              a().createElement(
                "div",
                { className: F()(xt.base, xt[`base__${t}`]) },
                a().createElement("div", { className: xt.icon }),
                a().createElement(
                  "div",
                  { className: xt.realLevel },
                  a().createElement(h.ZP, {
                    text: n,
                    format: { binding: { value: a().createElement(h.ZP, { text: e }) } },
                  }),
                ),
              ),
            );
          }),
          Nt = {
            base: "LastSkillInfo_base_38",
            realLevel: "LastSkillInfo_realLevel_78",
            base__small: "LastSkillInfo_base__small_c5",
            possibleLevel: "LastSkillInfo_possibleLevel_02",
            acceleratedTrainingIcon: "LastSkillInfo_acceleratedTrainingIcon_bf",
            base__big: "LastSkillInfo_base__big_10",
          },
          Tt = 0.01,
          Mt = (0, n.memo)(
            ({
              lastSkillLevel: e,
              lastPossibleSkillLevel: t,
              showAcceleratedTrainingIcon: u,
              skillSize: r,
              blinkStyle: o,
            }) => {
              const s = (0, n.useRef)(e),
                i = (0, Ee.useSpring)(() => ({ from: { scale: 1 } })),
                l = i[0],
                c = i[1];
              (0, n.useEffect)(() => {
                t < 0 &&
                  s.current !== e &&
                  (c.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: Ae.Fs },
                  }),
                  (s.current = e));
              }, [e, t, c]);
              const m = (0, n.useMemo)(
                  () =>
                    0 === t
                      ? [R.strings.common.percentValue(), t]
                      : t < Tt
                        ? [R.strings.crew_widget.plusMinValue(), Tt]
                        : [R.strings.crew_widget.plusValue(), t],
                  [t],
                ),
                d = m[0],
                _ = m[1];
              return a().createElement(
                "div",
                { className: F()(Nt.base, Nt[`base__${r}`]) },
                e >= 0 &&
                  e < 100 &&
                  a().createElement(
                    Ee.animated.div,
                    { style: l },
                    a().createElement(
                      "div",
                      { className: Nt.realLevel },
                      (0, P.uF)(R.strings.common.percentValue(), {
                        value: e > 0 && e < Tt ? Tt : e,
                      }),
                    ),
                  ),
                t >= 0 &&
                  t < 100 &&
                  a().createElement(
                    Ee.animated.div,
                    { className: Nt.possibleLevel, style: o },
                    (0, P.uF)(d, { value: _ }),
                  ),
                u && a().createElement(tt, { classMix: Nt.acceleratedTrainingIcon }),
              );
            },
          );
        var Rt = u(8485);
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
        function jt() {
          return (
            (jt =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            jt.apply(this, arguments)
          );
        }
        const zt = (0, n.memo)(function (e) {
            let t = e.width,
              u = e.height,
              r = e.getImageSource,
              o = e.frameCount,
              s = e.onAnimate,
              i = e.frameTime,
              l = void 0 === i ? Pt : i,
              c = e.initialFrameIndex,
              m = void 0 === c ? Ot : c,
              d = e.lastFrameIndex,
              _ = void 0 === d ? o - 1 : d,
              E = e.loop,
              g = void 0 === E ? Ht : E,
              A = e.state,
              p = void 0 === A ? Wt : A,
              C = e.onAnimationDone,
              F = e.onAnimationComplete,
              h = e.poster,
              b = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, Gt);
            const v = (0, n.useRef)(null);
            return (
              (0, n.useEffect)(() => {
                const e = v.current;
                if (!e) return;
                const t = e.getContext("2d"),
                  u = (u) => {
                    (t.clearRect(0, 0, e.width, e.height), t.drawImage(u.img, -u.x, -u.y));
                  };
                switch (p) {
                  case "play":
                    return (function () {
                      const e = Zt(m, _, r),
                        t = Ut(m, _),
                        n = window.setInterval(() => {
                          const a = t(),
                            r = e.get(a);
                          r
                            ? (null == s || s(a, r),
                              u(r),
                              a === _ &&
                                (null == F || F(),
                                g || (null == C || C(), window.clearInterval(n))))
                            : console.error("frameImage was not provided in frameImages Map");
                        }, l);
                      return () => window.clearInterval(n);
                    })();
                  case "stop":
                    return (function () {
                      const e = 0 === m && h ? { path: h, x: 0, y: 0 } : r(m),
                        t = new Image();
                      t.src = e.path;
                      const n = () => u($t(e, t));
                      return (
                        t.addEventListener("load", n),
                        () => t.removeEventListener("load", n)
                      );
                    })();
                  default:
                    return console.error("[CanvasSequence] Unreachable state!");
                }
              }, [l, r, m, _, g, s, F, C, h, p]),
              a().createElement("canvas", jt({}, b, { width: t, height: u, ref: v }))
            );
          }),
          Ut = (e, t) => {
            let u = e;
            return () => {
              const n = u;
              return ((u += 1), u > t && (u = e), n);
            };
          },
          $t = (e, t) => Object.assign({}, e, { img: t }),
          Zt = (e, t, u) => {
            const n = new Map(),
              a = {};
            for (let r = e; r <= t; r++) {
              const e = u(r),
                t = a[e.path];
              if (t) n.set(r, $t(e, t));
              else {
                const t = new Image();
                ((a[e.path] = t),
                  (t.src = e.path),
                  (t.onerror = () => {
                    console.error(
                      `[CanvasSequence] Error loading image(${r})`,
                      e.path,
                      `(${e.x},${e.y})`,
                    );
                  }),
                  n.set(r, $t(e, t)));
              }
            }
            return n;
          };
        const Vt = [
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
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
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
        const Kt = (e, t, u) => {
            const n = new Image();
            ((n.src = u(t)), e.push(n));
          },
          Yt =
            ((0, n.memo)((e) => {
              let t = e.width,
                u = e.height,
                r = e.getSrcByFrame,
                o = e.frameCount,
                s = e.onAnimate,
                i = void 0 === s ? () => {} : s,
                l = e.frameTime,
                c = void 0 === l ? 33 : l,
                m = e.initialFrameIndex,
                d = void 0 === m ? 0 : m,
                _ = e.loop,
                E = void 0 === _ || _,
                g = e.state,
                A = void 0 === g ? qt.Play : g,
                p = e.onAnimationComplete,
                C = void 0 === p ? () => {} : p,
                F = e.revers,
                h = void 0 !== F && F,
                b = (function (e, t) {
                  if (null == e) return {};
                  var u,
                    n,
                    a = {},
                    r = Object.keys(e);
                  for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                  return a;
                })(e, Vt);
              const v = (0, n.useRef)(null);
              return (
                (0, n.useEffect)(() => {
                  const e = v.current;
                  if (!e) return;
                  const n = o - 1,
                    a = e.getContext("2d"),
                    s = (n) => {
                      (a.clearRect(0, 0, e.width, e.height), a.drawImage(n, 0, 0, t, u));
                    };
                  if ("stop" === A) {
                    const e = r(0),
                      t = new Image();
                    t.src = e;
                    const u = () => s(t);
                    return (t.addEventListener("load", u), () => t.removeEventListener("load", u));
                  }
                  const l = ((e, t, u) => {
                      const n = [];
                      if (u) for (let u = e; u >= 0; u--) Kt(n, u, t);
                      else for (let u = 0; u < e; u++) Kt(n, u, t);
                      return n;
                    })(o, r, h),
                    m = ((e, t = 0) => {
                      let u = t;
                      return () => {
                        const t = u;
                        return ((u += 1), u > e && (u = 0), t);
                      };
                    })(n, d),
                    _ = setInterval(() => {
                      const e = m(),
                        t = l[e];
                      (s(l[e]), i(e, t), e === n && (C(), E || clearInterval(_)));
                    }, c);
                  return () => clearInterval(_);
                }, [o, c, r, u, d, E, i, C, A, t, h]),
                a().createElement("canvas", Xt({}, b, { width: t, height: u, ref: v }))
              );
            }),
            "AnimatedNewSkill_base_6b"),
          Qt = "AnimatedNewSkill_base__big_31";
        function Jt(e, t) {
          var u = ("undefined" != typeof Symbol && e[Symbol.iterator]) || e["@@iterator"];
          if (u) return (u = u.call(e)).next.bind(u);
          if (
            Array.isArray(e) ||
            (u = (function (e, t) {
              if (!e) return;
              if ("string" == typeof e) return eu(e, t);
              var u = Object.prototype.toString.call(e).slice(8, -1);
              "Object" === u && e.constructor && (u = e.constructor.name);
              if ("Map" === u || "Set" === u) return Array.from(e);
              if ("Arguments" === u || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(u))
                return eu(e, t);
            })(e)) ||
            (t && e && "number" == typeof e.length)
          ) {
            u && (e = u);
            var n = 0;
            return function () {
              return n >= e.length ? { done: !0 } : { done: !1, value: e[n++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function eu(e, t) {
          (null == t || t > e.length) && (t = e.length);
          for (var u = 0, n = new Array(t); u < t; u++) n[u] = e[u];
          return n;
        }
        class tu {
          constructor() {
            ((this._intervalID = void 0),
              (this._observers = void 0),
              (this._intervalID = null),
              (this._observers = new Map()));
          }
          static get instance() {
            return (tu._instance || (tu._instance = new tu()), tu._instance);
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
        tu._instance = void 0;
        const uu = {
          width: 24,
          height: 24,
          frameCount: 42,
          chunk: { count: 1, columns: 42, rows: 1 },
          getChunkPath:
            ((nu = "R.images.gui.maps.icons.sequence.new_skill.skill_"), (e) => `${nu}${e}`),
        };
        var nu;
        const au = ({ size: e }) => {
            const t = (function (e) {
                const t = e.chunk,
                  u = t.rows * t.columns;
                return (n) => {
                  const a = n % u,
                    r = (a % t.columns) * e.width,
                    o = Math.trunc(a / t.columns) * e.height;
                  return { path: e.getChunkPath(Math.trunc(n / u)), x: r, y: o };
                };
              })(uu),
              u = (0, n.useState)(qt.Stop),
              r = u[0],
              o = u[1],
              s = (0, n.useCallback)(() => {
                o(qt.Play);
              }, [o]),
              i = (0, n.useCallback)(() => {
                o(qt.Stop);
              }, [o]);
            return (
              (0, n.useEffect)(
                () => (tu.instance.subscribe(s), () => tu.instance.unsubscribe(s)),
                [s],
              ),
              a().createElement(zt, {
                width: uu.width,
                height: uu.height,
                frameCount: uu.frameCount,
                getImageSource: t,
                loop: !1,
                state: r,
                onAnimationDone: i,
                className: F()(Yt, e === Rt.O.Big && Qt),
              })
            );
          },
          ru = {
            base: "Skill_base_ba",
            base__big: "Skill_base__big_eb",
            container: "Skill_container_0f",
            divider: "Skill_divider_e8",
            divider__small: "Skill_divider__small_42",
          };
        function ou() {
          return (
            (ou =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            ou.apply(this, arguments)
          );
        }
        let su;
        !(function (e) {
          ((e.Big = "big"), (e.Small = "small"));
        })(su || (su = {}));
        const iu = (0, n.memo)(
            ({
              name: e,
              icon: t,
              type: u,
              size: r,
              commonMarginValue: o,
              marginValue: s,
              clipWidth: i,
              tankmanID: l,
              blinkStyle: c,
              showNewSkillAnimation: m,
              isTooltipEnabled: d = !0,
              isLastZeroSkill: _ = !1,
            }) => {
              const E = (0, n.useRef)(""),
                g = (0, Ee.useSpring)(() => ({ from: { scale: 1 } })),
                A = g[0],
                p = g[1];
              (0, n.useEffect)(() => {
                (u === St.W.New &&
                  E.current === St.W.Possible &&
                  p.start({
                    from: { scale: 1 },
                    to: [{ scale: 1.2 }, { scale: 1 }],
                    delay: 200,
                    config: { duration: 400, easing: Ae.Fs },
                  }),
                  (E.current = u));
              }, [u, p]);
              return a().createElement(
                v.u,
                ou(
                  {},
                  (() => {
                    switch (u) {
                      case St.W.Learned:
                      case St.W.ZeroSkill:
                      case St.W.Learning:
                      case St.W.Irrelevant:
                        return {
                          contentId:
                            R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(
                              "resId",
                            ),
                          args: { tooltipId: wt.HZ, tankmanID: l, skillName: e },
                        };
                      case St.W.New:
                      case St.W.Possible:
                        return {
                          contentId: R.views.lobby.crew.tooltips.PerkAvailableTooltip("resId"),
                          args: { tankmanID: l },
                        };
                    }
                  })(),
                  {
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                    isEnabled: d,
                    ignoreShowDelay: !0,
                  },
                ),
                a().createElement(
                  Ee.animated.div,
                  { className: ru.container, style: A },
                  a().createElement(
                    Ee.animated.div,
                    { style: u === St.W.Possible ? c : void 0 },
                    a().createElement(
                      "div",
                      {
                        className: F()(ru.base, ru[`base__${r}`]),
                        style: {
                          marginLeft: u !== St.W.ZeroSkill ? `${s}rem` : `${s < 0 ? 2 : s}rem`,
                          clipPath: `inset(0 ${i}rem 0 0)`,
                        },
                      },
                      !m || (u !== St.W.Possible && u !== St.W.New)
                        ? a().createElement(Rt.d, { icon: t, size: r, type: u })
                        : a().createElement(au, { size: r }),
                    ),
                  ),
                  _ &&
                    a().createElement("div", {
                      className: F()(ru.divider, r === su.Small && ru.divider__small),
                      style: { marginRight: (r === su.Small ? 6 : 8) - (s || o || 0) + "rem" },
                    }),
                ),
              );
            },
          ),
          lu = "SkillsList_base_11",
          cu = "SkillsList_numOfSkills_64",
          mu = "SkillsList_numOfSkills__twoRows_8d",
          du = "SkillsList_numOfSkills__hidden_c5",
          _u = "SkillsList_numOfSkillsContent_a4",
          Eu = "SkillsList_numOfSkillsContent__withNew_b6",
          gu = "SkillsList_row_03",
          Au = "SkillsList_skillsWithOutLast_02",
          pu = "SkillsList_skillsWithOutLast__hidden_8d",
          Cu = "SkillsList_lastSkill_96",
          Fu = "SkillsList_lastSkill__wrapped_9d",
          hu = "SkillsList_possibleLevel_97",
          bu = "SkillsList_possibleLevel__before_6f",
          vu = (0, n.memo)(
            ({
              tankman: e,
              showAcceleratedTrainingIcon: t = !1,
              rowWidth: u = 220,
              maxBigSkillsInRow: r = 10,
              blinkStyle: o,
              isSkillTooltipEnabled: s = !0,
              isCurrentLayoutHangar: i = !1,
              isWidgetHovered: l = !1,
            }) => {
              const c = e.skills,
                m = c.filter((e) => e.type === St.W.ZeroSkill).length,
                d = m > 0 ? c[m - 1].name : null,
                _ = c.length,
                E = kt(e),
                g = ((e, t, u) => {
                  let n = e > t ? 10 : e;
                  const a = 0 === e ? e : Math.ceil(e / n),
                    r = a > 1 ? 16 : 24;
                  let o = 2,
                    s = r;
                  for (; (u - (r + o)) / (s + o) < Math.floor((e - 1) / a);) o > 0 ? o-- : s--;
                  return (
                    (n = Math.min(n, 1 + Math.floor((u - r) / (s + o)))),
                    s !== r && (o = s - r),
                    [a, n, o, r, s]
                  );
                })(E, r, u),
                A = g[0],
                p = g[1],
                C = g[2],
                b = g[3],
                v = g[4],
                D = A > 1 ? su.Small : su.Big,
                B = (0, n.useMemo)(
                  () =>
                    a().createElement(
                      Ee.animated.div,
                      { className: F()(hu, 0 === _ && bu), style: o },
                      a().createElement(It, {
                        percentValue: e.lastPossibleRoleLevel,
                        skillSize: D,
                        hasSkills: e.possibleSkillsAmount > 0 || _ > 0,
                      }),
                    ),
                  [o, D, _, e.lastPossibleRoleLevel, e.possibleSkillsAmount],
                ),
                f = e.skills.filter((e) => e.type === St.W.New).length > 1,
                w = (0, n.useCallback)(
                  (t, u) => {
                    const n = p * t + u;
                    let a = "",
                      r = "",
                      o = St.W.Learned;
                    if (n < _) {
                      const e = c[n];
                      e && ((a = e.name), (r = e.icon), (o = e.type));
                    } else o = n < _ + e.newSkillsAmount ? St.W.New : St.W.Possible;
                    return { skillIndex: n, name: a, icon: r, type: o };
                  },
                  [p, c, _, e.newSkillsAmount],
                ),
                y = Array(A)
                  .fill(null)
                  .reduce((e, t, u) => e + Math.min(p, E - u * p) - 1, 0),
                k = (0, n.useCallback)(
                  (t, u, n) => {
                    const r = u - 1,
                      c = w(t, r),
                      d = c.skillIndex,
                      _ = c.name,
                      E = c.icon,
                      g = c.type,
                      p = 0 === r ? C : 0,
                      h = r * (b + C),
                      v = 2 * (D === su.Big ? 8 : 6) + 1 - C;
                    return a().createElement(
                      "div",
                      {
                        className: F()(Cu, i && !l && Fu),
                        style: {
                          "--leftPosition": -(h + (!(m > 0) || (A > 1 && n) ? 0 : v)) + "rem",
                        },
                      },
                      a().createElement(iu, {
                        name: _,
                        icon: E,
                        type: g,
                        size: D,
                        marginValue: 0 === r ? 0 : C,
                        commonMarginValue: p,
                        key: d + "_" + _,
                        clipWidth: 0,
                        tankmanID: e.tankmanID,
                        blinkStyle: o,
                        isTooltipEnabled: s,
                        showNewSkillAnimation: i,
                      }),
                    );
                  },
                  [w, C, i, l, b, m, A, D, e.tankmanID, o, s],
                );
              return a().createElement(
                "div",
                { className: lu },
                a().createElement(
                  "div",
                  { className: F()(cu, A > 1 && mu, l && du) },
                  i &&
                    y > 0 &&
                    a().createElement(h.ZP, {
                      className: F()(_u, f && Eu),
                      text: R.strings.crew_widget.hiddenSkills(),
                      format: { binding: { num: y } },
                    }),
                ),
                (0, Lt.K)(A, (u) => {
                  const n = Math.min(p, E - u * p),
                    r = u === A - 1;
                  return a().createElement(
                    "div",
                    { className: gu, key: `row_${u}` },
                    e.lastPossibleRoleLevel > 0 && 0 === _ && B,
                    a().createElement(
                      "div",
                      { className: F()(Au, i && !l && pu) },
                      (0, Lt.K)(n - 1, (t) => {
                        const r = w(u, t),
                          l = r.skillIndex,
                          c = r.name,
                          m = r.icon,
                          _ = r.type;
                        return a().createElement(iu, {
                          name: c,
                          icon: m,
                          type: _,
                          size: D,
                          marginValue: 0 === t ? 0 : C,
                          commonMarginValue: 0 === t ? C : 0,
                          key: l + "_" + c + "_" + _,
                          clipWidth: t === n - 1 || _ === St.W.ZeroSkill ? 0 : b - v,
                          tankmanID: e.tankmanID,
                          blinkStyle: o,
                          isTooltipEnabled: s,
                          showNewSkillAnimation: i,
                          isLastZeroSkill: c === d,
                        });
                      }),
                    ),
                    k(u, n, r),
                    r &&
                      a().createElement(
                        a().Fragment,
                        null,
                        a().createElement(Mt, {
                          lastSkillLevel: e.possibleSkillsAmount > 0 ? -1 : e.lastSkillLevel,
                          lastPossibleSkillLevel: e.lastPossibleSkillLevel,
                          showAcceleratedTrainingIcon: t,
                          skillSize: D,
                          blinkStyle: o,
                        }),
                        e.lastPossibleRoleLevel > 0 && _ > 0 && B,
                      ),
                  );
                }),
                !A &&
                  a().createElement(
                    "div",
                    { className: gu },
                    e.lastPossibleRoleLevel > 0 && 0 === _ && B,
                    a().createElement(Mt, {
                      lastSkillLevel: e.possibleSkillsAmount > 0 ? -1 : e.lastSkillLevel,
                      lastPossibleSkillLevel: e.lastPossibleSkillLevel,
                      showAcceleratedTrainingIcon: t,
                      skillSize: D,
                      blinkStyle: o,
                    }),
                    e.lastPossibleRoleLevel > 0 && _ > 0 && B,
                  ),
              );
            },
          ),
          Du = "TankmanInfo_base_69",
          Bu = "TankmanInfo_base__disabled_36",
          fu = "TankmanInfo_tankmanTooltipHoverArea_9b",
          wu = "TankmanInfo_specialization_77",
          yu = "TankmanInfo_specialization__withManySkills_9a",
          ku = "TankmanInfo_skillsContainer_17",
          Su = "TankmanInfo_skillsContainer__withManySkills_00",
          Lu = (0, o.Pi)(
            ({ tankman: e, layoutInfo: t, isUntrained: u, blinkStyle: r, isDisabled: o }) => {
              const s = p().model,
                i = (0, yt.GS)().mediaSize,
                l = s.isWidgetHover.get(),
                c = t.isCurrentLayoutQuickTraining || s.computes.isChangeCrewButtonVisible(),
                m = (0, n.useMemo)(() => (c ? (i >= yt.cJ.Small ? 190 : 146) : 220), [c, i]),
                d = ((e, t) => kt(e) > t)(e, 10),
                _ = !t.isCurrentLayoutQuickTraining && -1 !== e.tankmanID && e.isLessMastered,
                E = e.baseSpecializationLevel >= 100;
              return a().createElement(
                "div",
                { className: F()(Du, o && Bu) },
                a().createElement(
                  ft.t,
                  {
                    targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                    args: { tooltipId: wt.v$, tankmanID: e.tankmanID },
                    ignoreShowDelay: !1,
                  },
                  a().createElement("div", { className: fu }),
                ),
                a().createElement(
                  "div",
                  { className: F()(wu, d && yu) },
                  a().createElement(gt, {
                    roles: e.roles,
                    tankmanID: e.tankmanID,
                    specializationLevel: e.specializationLevel,
                    isUntrained: u,
                    name: e.fullName,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                    isAcceleratedTrainingAvailable: _ && !E,
                  }),
                ),
                a().createElement(
                  "div",
                  { className: F()(ku, d && Su) },
                  a().createElement(vu, {
                    tankman: e,
                    showAcceleratedTrainingIcon: _ && E,
                    rowWidth: m,
                    maxBigSkillsInRow: 10,
                    blinkStyle: r,
                    isCurrentLayoutHangar: t.isCurrentLayoutHangar,
                    isWidgetHovered: l,
                  }),
                ),
              );
            },
          ),
          xu = "QuickTrainingTankmanSlotContent_base_8d",
          Iu = "QuickTrainingTankmanSlotContent_arrow_5a",
          Nu = "QuickTrainingTankmanSlotContent_highlight_72",
          Tu = "QuickTrainingTankmanSlotContent_icon_7c",
          Mu = { transform: "translateY(50rem)", opacity: 0, scale: 1 },
          Ru = { transform: "translateY(0rem)", opacity: 1, scale: 1 },
          Pu = [
            { transform: "translateY(-10rem)", scale: 1.3 },
            { opacity: 0, scale: 1 },
          ],
          Ou = { opacity: 0 },
          Hu = [{ opacity: 1 }, { opacity: 0 }],
          Wu = (0, n.memo)(
            ({
              tankman: e,
              isUntrained: t,
              blinkStyle: u,
              qtTankmanIconStyle: r,
              layoutInfo: o,
              isDisabled: s,
            }) => {
              const i = (0, n.useRef)(e.lastSkillLevelFull),
                l = (0, n.useRef)(e.skills.length),
                c = (0, Ee.useSpring)(() => ({ from: Mu })),
                m = c[0],
                d = c[1],
                _ = (0, Ee.useSpring)(() => ({ from: Ou })),
                E = _[0],
                g = _[1],
                A = (0, n.useRef)(!1);
              return (
                (0, n.useEffect)(() => {
                  e.hasPossibleProgress
                    ? A.current ||
                      (d.start({
                        from: Mu,
                        to: Ru,
                        reverse: false,
                        config: { duration: 300, easing: Ae.BH },
                      }),
                      (A.current = !0))
                    : A.current
                      ? (i.current !== e.lastSkillLevelFull || l.current !== e.skills.length
                          ? (d.start({
                              from: Ru,
                              to: Pu,
                              delay: 200,
                              config: { duration: 500, easing: Ae.BH },
                            }),
                            (i.current = e.lastSkillLevelFull),
                            (l.current = e.skills.length),
                            g.start({
                              from: Ou,
                              to: Hu,
                              delay: 200,
                              config: { duration: 500, easing: Ae.BH },
                            }))
                          : d.start({ reset: !0, reverse: !0 }),
                        (A.current = !1))
                      : ((i.current = e.lastSkillLevelFull), (l.current = e.skills.length));
                }, [d, g, e.lastSkillLevelFull, e.hasPossibleProgress, e.skills.length]),
                a().createElement(
                  "div",
                  { className: xu },
                  a().createElement(Ee.animated.div, { className: Nu, style: E }),
                  a().createElement(
                    Ee.animated.div,
                    { style: r },
                    a().createElement(Qe.G, {
                      name: e.icon,
                      size: Qe.U.c100x60Barracks,
                      className: Tu,
                      isSkin: e.isInSkin,
                    }),
                  ),
                  a().createElement(Ee.animated.div, { className: Iu, style: m }),
                  a().createElement(Lu, {
                    tankman: e,
                    layoutInfo: o,
                    isUntrained: t,
                    blinkStyle: u,
                    isDisabled: s,
                  }),
                )
              );
            },
            (e, t) => {
              const u = e.tankman,
                n = t.tankman;
              return (
                u.hasPossibleProgress === n.hasPossibleProgress &&
                ((e, t) => {
                  if (e.length !== t.length) return !1;
                  const u = e.length;
                  for (let r = 0; r < u; r++) {
                    var n, a;
                    if (
                      (null == (n = c.U2(e, r)) ? void 0 : n.name) !==
                      (null == (a = c.U2(t, r)) ? void 0 : a.name)
                    )
                      return !1;
                  }
                  return !0;
                })(u.skills, n.skills) &&
                u.lastSkillLevelFull === n.lastSkillLevelFull &&
                u.possibleSkillsAmount === n.possibleSkillsAmount &&
                u.lastPossibleSkillLevel === n.lastPossibleSkillLevel &&
                u.specializationLevel === n.specializationLevel &&
                u.lastPossibleRoleLevel === n.lastPossibleRoleLevel
              );
            },
          ),
          Gu = "TankmanSlotContent_base_00",
          ju = "TankmanSlotContent_icon_ef",
          zu = (0, n.memo)(({ tankman: e, layoutInfo: t, isUntrained: u, isDisabled: n }) =>
            a().createElement(
              "div",
              { className: Gu },
              a().createElement(Qe.G, {
                name: e.icon,
                size: Qe.U.c100x60Barracks,
                className: ju,
                isSkin: e.isInSkin,
              }),
              a().createElement(Lu, { tankman: e, layoutInfo: t, isUntrained: u, isDisabled: n }),
            ),
          ),
          Uu = (0, n.memo)(
            ({
              roles: e,
              tankman: t,
              layoutInfo: u,
              vehicleName: n,
              vehicleType: r,
              isUntrained: o,
              isDisabled: s,
              isSelected: i,
              blinkSlotStyle: l,
              blinkTankmanStyle: c,
              qtTankmanIconStyle: m,
            }) =>
              -1 === t.tankmanID
                ? a().createElement(Bt, {
                    roles: e,
                    layoutInfo: u,
                    vehicleName: n,
                    vehicleType: r,
                    isDisabled: s,
                    isSelected: i,
                    blinkStyle: c,
                    qtTankmanIconStyle: m,
                  })
                : u.isCurrentLayoutQuickTraining
                  ? a().createElement(Wu, {
                      tankman: t,
                      isUntrained: o,
                      blinkStyle: l,
                      qtTankmanIconStyle: m,
                      layoutInfo: u,
                      isDisabled: s,
                    })
                  : a().createElement(zu, {
                      tankman: t,
                      layoutInfo: u,
                      isUntrained: o,
                      isDisabled: s,
                    }),
          ),
          $u = { transform: "translateX(0rem)" },
          Zu = { transform: "translateX(41rem)" },
          Vu = { opacity: 0 },
          Xu = { opacity: 1 },
          qu = (0, o.Pi)(
            ({
              slotIdx: e,
              roles: t,
              tankman: u,
              layoutInfo: o,
              isSelected: s,
              isAnySlotSelected: i,
              isDisabled: l,
              blinkSlotStyle: c,
              blinkTankmanStyle: m,
              qtTankmanIconStyle: d,
            }) => {
              const E = p(),
                g = E.model,
                A = E.controls,
                C = ((e, t) => {
                  const u = (0, K.Jp)(_.D9),
                    n = (0, X.f)(
                      () => u({ action: _.eX.Click, parentScreen: e, item: t }),
                      [e, t],
                      _.tL,
                    );
                  return (e) => {
                    e.button === q.RIGHT && n();
                  };
                })(g.computes.getUiLoggingParentScreen(), _.x3.SlotContextMenu),
                h = A.onSlotClick,
                b = A.onChangeCrewClick,
                v = g.isWidgetHover.get(),
                D = g.computes.isChangeCrewButtonVisible(),
                B = g.computes.isTankmanMode(),
                f = g.isCrewLocked.get(),
                w = g.vehicleName.get(),
                y = g.vehicleType.get(),
                k = !l && u.isInteractive && (!o.isCurrentLayoutQuickTraining || i),
                S = (0, n.useCallback)(() => {
                  k && !B && ((0, r.G)(R.sounds.yes1()), h(e, u.tankmanID));
                }, [e, u, h, B, k]),
                L = (0, n.useCallback)(
                  (t) => {
                    (t.stopPropagation(), f || ((0, r.G)(R.sounds.yes1()), b(e, u.tankmanID)));
                  },
                  [e, u, b, f],
                ),
                x = (0, n.useMemo)(() => ({ tankmanID: u.tankmanID, slotIdx: e }), [u, e]);
              return a().createElement(
                Pe,
                {
                  args: x,
                  isEnabled: !l,
                  targetId: R.views.lobby.crew.widgets.CrewWidget("resId"),
                  onMouseDown: C,
                },
                a().createElement(
                  "div",
                  null,
                  a().createElement(
                    Ce,
                    {
                      onClick: S,
                      isSelected: s,
                      isDisabled: l,
                      isEmpty: -1 === u.tankmanID,
                      layoutInfo: o,
                      isEnabledForMouse: k,
                      isWidgetHovered: v,
                    },
                    a().createElement(
                      "div",
                      { className: $e },
                      u.hasWarning && a().createElement("div", { className: qe }),
                      s && a().createElement("div", { className: B ? Ye : Ke }),
                      a().createElement(
                        Fe,
                        {
                          startState: $u,
                          endState: Zu,
                          layoutInfo: o,
                          isPaused: !D,
                          className: F()(Ve, D && Xe),
                          isTankmanMode: B,
                        },
                        a().createElement(Uu, {
                          roles: t,
                          tankman: u,
                          layoutInfo: o,
                          isUntrained: u.isUntrained,
                          isDisabled: l,
                          vehicleName: w,
                          vehicleType: y,
                          blinkSlotStyle: c,
                          blinkTankmanStyle: m,
                          qtTankmanIconStyle: d,
                          isSelected: s,
                        }),
                      ),
                      D &&
                        a().createElement(
                          "div",
                          { onClick: L },
                          a().createElement(
                            Fe,
                            {
                              startState: Vu,
                              endState: Xu,
                              layoutInfo: o,
                              isPaused: !D,
                              className: Ze,
                              isTankmanMode: B,
                            },
                            a().createElement(Ue, {
                              isSelected: o.isCurrentLayoutMemberChange && s,
                              isLocked: f,
                              mainRole: t[0] || "",
                              isFemale: -1 !== u.tankmanID && u.isFemale,
                            }),
                          ),
                        ),
                    ),
                  ),
                ),
              );
            },
          ),
          Ku = "SlotsList_base_5f";
        function Yu() {
          return (
            (Yu =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Yu.apply(this, arguments)
          );
        }
        const Qu = { transform: "translateX(0rem)" },
          Ju = { transform: "translateX(15rem)" },
          en = (0, o.Pi)(({ layoutInfo: e, isWidgetDisabled: t, className: u }) => {
            const r = p().model,
              o = r.computes.isAnyEmptySlots(),
              s = (0, Ee.useSpring)(
                () => ({
                  from: { opacity: 1 },
                  to: [{ opacity: 0 }, { opacity: 1 }],
                  config: { duration: 750, easing: Ae.Fs },
                  loop: !0,
                }),
                [],
              ),
              i = s[0],
              l = s[1];
            (0, n.useEffect)(() => {
              o ? l.resume() : l.pause();
            }, [l, o]);
            const c = (0, Ee.useSpring)(
                () => ({
                  from: { opacity: 1 },
                  to: [{ opacity: 0.3 }, { opacity: 1 }],
                  config: { duration: 400, easing: Ae.Fs },
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
                from: Qu,
                to: Ju,
                delay: 200,
                config: { duration: 300, easing: Ae.ei },
                pause: !e.isCurrentLayoutQuickTraining,
              }))[0],
              E = (0, n.useCallback)(
                (u) => t || (e.isCurrentLayoutQuickTraining && -1 === u),
                [t, e.isCurrentLayoutQuickTraining],
              );
            return a().createElement(
              "div",
              { id: "crew_widget_slots_list", className: F()(Ku, u) },
              r.computes
                .getSlots()
                .map((t, u) =>
                  a().createElement(
                    qu,
                    Yu({}, t, {
                      layoutInfo: e,
                      key: `slot_${u}_${t.tankman.tankmanID}`,
                      isSelected:
                        !e.isCurrentLayoutHangar &&
                        (r.computes.isSlotSelected(t.slotIdx) || r.computes.isTankmanMode()),
                      isAnySlotSelected: r.computes.isAnySlotSelected(),
                      isDisabled: E(t.tankman.tankmanID),
                      blinkSlotStyle: m,
                      blinkTankmanStyle: i,
                      qtTankmanIconStyle: _,
                    }),
                  ),
                ),
            );
          }),
          tn = (0, o.Pi)(() => {
            const e = p(),
              t = e.model,
              u = e.controls,
              o = t.isDisabled.get(),
              s = t.hasDog.get(),
              i = t.computes.getLayoutInfo(),
              l = t.isExtended.get();
            return (
              (0, n.useEffect)(() => {
                u.setIsWidgetHover(l);
              }, [l, u]),
              a().createElement(
                "div",
                {
                  className: me,
                  onMouseEnter: () => {
                    l ||
                      (u.setIsWidgetHover(!0),
                      i.isCurrentLayoutHangar && !o && (0, r.G)(R.sounds.crew_hover()));
                  },
                  onMouseLeave: () => {
                    l ||
                      (u.setIsWidgetHover(!1),
                      i.isCurrentLayoutHangar && !o && (0, r.G)(R.sounds.crew_unhover()));
                  },
                },
                t.computes.isButtonBarVisible() &&
                  a().createElement(
                    "div",
                    { className: de },
                    a().createElement(ce, {
                      isWidgetDisabled: o,
                      isCurrentLayoutHangar: i.isCurrentLayoutHangar,
                    }),
                  ),
                a().createElement(en, { layoutInfo: i, isWidgetDisabled: o, className: _e }),
                s && a().createElement(Ie, { layoutInfo: i, isDisabled: o }),
              )
            );
          }),
          un = (0, n.memo)(() =>
            a().createElement(
              A,
              { options: { rootId: R.views.lobby.crew.widgets.CrewWidget("resId") } },
              a().createElement(tn, null),
            ),
          );
      },
      5801: (e, t, u) => {
        "use strict";
        u.d(t, { p: () => Pe });
        var n = u(6179),
          a = u.n(n),
          r = u(6483),
          o = u.n(r),
          s = u(3457),
          i = u(2106),
          l = u(7613),
          c = u(6373);
        let m;
        !(function (e) {
          ((e.Default = "default"),
            (e.Barracks = "barracks"),
            (e.MemberChange = "memberChange"),
            (e.TankChange = "tankChange"),
            (e.PersonalData = "personalData"));
        })(m || (m = {}));
        var d = u(3403),
          _ = u(3415),
          E = u(9480),
          g = u(9631);
        const A = "FilterTitle_base_a7",
          p = "FilterTitle_label_05",
          C = "FilterTitle_discount_42",
          F = "FilterTitle_discountIcon_30",
          h = ({ label: e, hasDiscount: t, className: u }) =>
            a().createElement(
              "div",
              { className: o()(A, u) },
              a().createElement("div", { className: p }, e),
              t &&
                a().createElement(
                  "div",
                  { className: C },
                  a().createElement("div", { className: F }),
                ),
            );
        let b;
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
        })(b || (b = {}));
        var v = u(3649);
        const D = "ToggleIcon_base_59",
          B = "ToggleIcon_base__small_3e",
          f = "ToggleIcon_icon_e7",
          w = a().memo(function ({ icon: e, isSmall: t = !1, classNames: u }) {
            return a().createElement(
              "div",
              { className: o()(D, t && B) },
              a().createElement("div", {
                className: o()(f, null == u ? void 0 : u.icon),
                style: { backgroundImage: `url(${e})` },
              }),
            );
          });
        var y = u(9690);
        const k = "VehicleTier_base_9c",
          S = "VehicleTier_base__small_fc",
          L = ({ level: e, isSmall: t = !1 }) =>
            a().createElement("div", { className: o()(k, t && S) }, (0, y.HG)(e)),
          x = {
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
          I = ({ id: e, icon: t, type: u, isSmall: n = !0, isSelected: r = !1 }) =>
            u === b.VehicleTier
              ? a().createElement(L, { isSmall: n, level: Number(e) })
              : a().createElement(w, {
                  icon: t,
                  isSmall: n,
                  classNames: {
                    icon: o()(
                      x[`icon__${u}`],
                      x[`icon__${u}${(0, v.e)(e)}`],
                      r && x.icon__selected,
                    ),
                  },
                }),
          N = {
            base: "FilterToggleGroup_base_69",
            title: "FilterToggleGroup_title_65",
            content: "FilterToggleGroup_content_80",
            toggle: "FilterToggleGroup_toggle_d4",
            base__inPopup: "FilterToggleGroup_base__inPopup_11",
          };
        function T() {
          return (
            (T =
              Object.assign ||
              function (e) {
                for (var t = 1; t < arguments.length; t++) {
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            T.apply(this, arguments)
          );
        }
        let M;
        !(function (e) {
          ((e.Default = "default"), (e.InPopup = "inPopup"));
        })(M || (M = {}));
        const P = ({ header: e, body: t, contentId: u, targetId: n }) =>
            u
              ? { contentId: u, targetId: n }
              : t || e
                ? { header: null != e ? e : void 0, body: null != t ? t : void 0 }
                : void 0,
          O = ({
            id: e,
            type: t,
            label: u,
            hasDiscount: n,
            filters: r,
            onClick: s,
            className: i,
            toggleProps: l,
            theme: c = M.Default,
          }) => {
            const m = c === M.InPopup;
            return a().createElement(
              "div",
              { className: o()(N.base, N[`base__${c}`], i) },
              m && a().createElement(h, { className: N.title, label: u, hasDiscount: n }),
              a().createElement(
                "div",
                { className: N.content },
                E.UI(r, ({ id: u, isSelected: n, tooltip: r, icon: i, counter: c }) =>
                  a().createElement(
                    _.l,
                    { key: u, tooltipArgs: P(r), className: N.toggle },
                    a().createElement(
                      g.C,
                      T({}, l, {
                        className: o()(N.toggle, null == l ? void 0 : l.className),
                        isActive: n,
                        onClick: () => (null == s ? void 0 : s(e, u)),
                        counter: c,
                      }),
                      a().createElement(I, { id: u, icon: i, type: t, isSmall: m, isSelected: n }),
                    ),
                  ),
                ),
              ),
            );
          };
        var H = u(9197),
          W = u(3215),
          G = u(4598),
          j = u(5175),
          z = u(3946);
        const U = (0, W.q)()(
            ({ observableModel: e }) => {
              const t = {
                  root: e.object(),
                  amountInfo: e.object("amountInfo"),
                  filter: e.array("filter"),
                  filters: e.array("filter.filters"),
                },
                u = (0, z.Om)(() => (0, j.c)(t.filter.get()), { equals: G.jv }),
                n = (0, z.Om)(() => (0, j.c)(t.filters.get()), { equals: G.jv }),
                a = (0, z.Om)(
                  () =>
                    (0, j.c)(t.filters.get()).filter((e) => "dismissed" === e.id && e.isSelected)
                      .length > 0,
                  { equals: G.jv },
                );
              return Object.assign({}, t, {
                computes: { getFilterGroup: u, getFilters: n, getIsRestoreFilter: a },
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
          $ = U[0],
          Z = U[1];
        var V = u(3616),
          X = u(1037),
          q = u(9367);
        const K = "PopupButton_base_7c",
          Y = "PopupButton_popupButtonLabel_ed",
          Q = "PopupButton_buttonIconWrapper_d7",
          J = "PopupButton_buttonIcon_e0",
          ee = "PopupButton_buttonIcon__isHighlighted_84",
          te = "PopupButton_discountAlert_c8",
          ue = ({ isHighlighted: e, hasDiscountAlert: t, popoverDirection: u = X.IC.Bottom }) =>
            a().createElement(
              "div",
              { className: K },
              a().createElement(
                "div",
                { className: Y },
                R.strings.crew.filter.popup.button.title(),
              ),
              a().createElement(
                V.Z,
                {
                  contentId: R.views.lobby.crew.popovers.FilterPopoverView("resId"),
                  targetId: R.views.lobby.crew.widgets.FilterPanelWidget("resId"),
                  direction: u,
                },
                a().createElement(
                  "div",
                  { id: "popup_btn", className: Q },
                  a().createElement(
                    g.C,
                    { type: s.L$.ghost, size: s.qE.small, isActive: e, hasIndicator: !1 },
                    a().createElement("div", { className: o()(J, e && ee) }),
                  ),
                  t && a().createElement(q.Q, { className: te }),
                ),
              ),
            );
        var ne = u(8018);
        const ae = "ResetButton_base_58",
          re = "ResetButton_button_a5",
          oe = "ResetButton_icon_4a",
          se = ({ isSelectMode: e, onClick: t }) =>
            a().createElement(
              "div",
              { className: ae },
              a().createElement(
                c.i,
                e ? ne.Er : ne.Xd,
                a().createElement(
                  s.u5,
                  { mixClass: re, onClick: t, type: s.L$.ghost, size: s.qE.small },
                  a().createElement("div", { className: oe }),
                ),
              ),
            ),
          ie = "default",
          le = "search",
          ce = "email",
          me = "password",
          de = "normal",
          _e = "disabled",
          Ee = "alert",
          ge = "error",
          Ae = "medium",
          pe = {
            [ie]: "",
            [ce]: R.strings.common.input.placeholder.email(),
            [le]: R.strings.common.input.placeholder.search(),
            [me]: R.strings.common.input.placeholder.password(),
          },
          Ce = { [ie]: "text", [ce]: "text", [le]: "text", [me]: "password" },
          Fe = { [ie]: "", [ce]: "Invalid email", [le]: "", [me]: "" },
          he = R.images.gui.maps.icons.components.input;
        function be(e, t) {
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
        var ve = u(7727);
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
          Be = a().memo(
            ({
              componentId: e,
              value: t = "",
              type: u = ie,
              size: r = Ae,
              variant: s = de,
              placeholder: i = "",
              highlighted: l,
              withClear: c,
              selectOnFocus: m = !0,
              maxLength: d,
              iconSource: _,
              classMix: E,
              onMouseEnter: g,
              onMouseLeave: A,
              onMouseDown: p,
              onMouseUp: C,
              onClick: F,
              onChange: h,
              onClear: b,
              onFocus: v,
              onBlur: D,
            }) => {
              const B = (0, n.useState)(!1),
                f = B[0],
                w = B[1],
                y = (0, n.useRef)(null),
                k = (0, n.useRef)({ mouseOver: !1, mouseDown: !1 }),
                S = s !== _e,
                L = (0, n.useCallback)(
                  (e) => {
                    S && (w(!0), v && v(e));
                  },
                  [S, v],
                ),
                x = (0, n.useCallback)(
                  (e) => {
                    S && !k.current.mouseOver && (w(!1), D && D(e));
                  },
                  [S, D],
                );
              (0, n.useEffect)(() => {
                S && f && m && y.current && y.current.select();
              }, [m, f, S]);
              const I = (0, n.useCallback)(
                  (e) => {
                    S && h && h(e.target.value);
                  },
                  [S, h],
                ),
                N = (0, n.useCallback)(
                  (e) => {
                    S && ((k.current.mouseOver = !0), g && g(e));
                  },
                  [S, g],
                ),
                T = (0, n.useCallback)(
                  (e) => {
                    S &&
                      y.current &&
                      (k.current.mouseDown && y.current.focus(),
                      (k.current.mouseOver = !1),
                      A && A(e));
                  },
                  [S, A],
                ),
                M = (0, n.useCallback)(
                  (e) => {
                    S && ((k.current.mouseDown = !0), p && p(e));
                  },
                  [S, p],
                ),
                R = (0, n.useCallback)(
                  (e) => {
                    S && ((k.current.mouseDown = !1), C && C(e));
                  },
                  [S, C],
                ),
                P = (0, n.useCallback)(
                  (e) => {
                    if (S && y.current) {
                      ((!f || (f && e.target !== y.current)) && y.current.focus(), F && F(e));
                    }
                  },
                  [f, S, F],
                ),
                O = i || pe[u],
                H = Boolean(_),
                W = o()(
                  De.base,
                  De[`base__${r}`],
                  l && De[`base__${s}`],
                  f && De.base__focused,
                  H && De.base__withIcon,
                  E,
                ),
                G = (0, n.useMemo)(() => (_ ? { backgroundImage: `url(${_})` } : null), [_]),
                j = o()(De.input, De[`input__${u}`]),
                z = o()(De.icon, De[`icon__${u}`]),
                U = o()(De.placeholder, De[`placeholder__${u}`]);
              return a().createElement(
                "div",
                {
                  id: e,
                  className: W,
                  onMouseEnter: N,
                  onMouseDown: M,
                  onMouseUp: R,
                  onMouseLeave: T,
                  onClick: P,
                },
                !S && a().createElement("div", { className: De.disabled }),
                G && a().createElement("div", { style: G, className: z }),
                a().createElement("input", {
                  ref: y,
                  className: j,
                  type: Ce[u],
                  value: t,
                  onChange: I,
                  disabled: !S,
                  onFocus: L,
                  onBlur: x,
                  maxLength: d,
                }),
                O && !t && !f && a().createElement("div", { className: U }, O),
                c &&
                  a().createElement("div", {
                    className: De.clear,
                    onClick: (e) => {
                      (ve.$.playClick(), b && b(e));
                    },
                    onMouseEnter: ve.$.playHighlight,
                  }),
              );
            },
          ),
          fe = {
            base: "HelperMessage_base_1e",
            base__shown: "HelperMessage_base__shown_ab",
            icon: "HelperMessage_icon_10",
            message: "HelperMessage_message_f4",
            message__alert: "HelperMessage_message__alert_b5",
            message__error: "HelperMessage_message__error_45",
            message__done: "HelperMessage_message__done_2b",
          },
          we = ({ variant: e, show: t = !0, helperText: u, helperIcon: r, classMix: s }) => {
            const i = (0, n.useMemo)(() => {
                const t =
                  r ||
                  (function (e) {
                    return e === Ee ? R.images.gui.maps.icons.library.alertIcon() : "";
                  })(e);
                return t && { backgroundImage: `url(${t})` };
              }, [r, e]),
              l = o()(fe.base, t && fe.base__shown),
              c = o()(fe.message, fe[`message__${e}`], s);
            return a().createElement(
              "div",
              { className: l },
              i && a().createElement("div", { className: fe.icon, style: i }),
              a().createElement("div", { className: c }, u),
            );
          },
          ye = {
            base: "Input_base_cd",
            base__small: "Input_base__small_c7",
            base__medium: "Input_base__medium_1f",
            base__large: "Input_base__large_11",
            helper: "Input_helper_ea",
          },
          ke = [
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
                  var u = arguments[t];
                  for (var n in u) Object.prototype.hasOwnProperty.call(u, n) && (e[n] = u[n]);
                }
                return e;
              }),
            Se.apply(this, arguments)
          );
        }
        const Le = {
            debounceTime: 200,
            performChangeValidation: !0,
            selectOnFocus: !0,
            withTypeIcon: !0,
            disableHighlightOnFocus: !0,
          },
          xe = (e) => {
            let t = e.componentId,
              u = e.type,
              r = void 0 === u ? ie : u,
              s = e.variant,
              i = void 0 === s ? de : s,
              l = e.size,
              c = void 0 === l ? Ae : l,
              m = e.value,
              d = e.tooltipArgs,
              E = e.helperText,
              g = void 0 === E ? "" : E,
              A = e.isValidated,
              p = void 0 === A || A,
              C = e.showHelper,
              F = void 0 === C || C,
              h = e.error,
              b = e.options,
              v = e.onFocus,
              D = e.onMouseEnter,
              B = e.onMouseLeave,
              f = e.onMouseUp,
              w = e.onMouseDown,
              y = e.onChange,
              k = e.classMix,
              S = e.controlClassMix,
              L = e.helperClassMix,
              x = (function (e, t) {
                if (null == e) return {};
                var u,
                  n,
                  a = {},
                  r = Object.keys(e);
                for (n = 0; n < r.length; n++) ((u = r[n]), t.indexOf(u) >= 0 || (a[u] = e[u]));
                return a;
              })(e, ke);
            const I = (0, n.useState)(m),
              N = I[0],
              T = I[1],
              M = (0, n.useState)(p),
              R = M[0],
              P = M[1],
              O = (0, n.useMemo)(() => Object.assign({}, Le, b), [b]),
              H = (0, n.useRef)({ debounceTimeout: 0, isChangeHandled: !0, value: m, type: r }),
              W = (0, n.useCallback)((e) => {
                e !== H.current.value &&
                  ((H.current.value = e), (H.current.isChangeHandled = !1), T(e));
              }, []),
              G = (0, n.useCallback)(
                (e) => {
                  let t = !0;
                  (O.performChangeValidation &&
                    (t = O.changesValidator ? O.changesValidator(e) : be(e, H.current.type)),
                    y && y(e, t));
                },
                [y, O],
              ),
              j = (0, n.useCallback)(() => {
                H.current.debounceTimeout &&
                  (window.clearTimeout(H.current.debounceTimeout), (H.current.debounceTimeout = 0));
              }, []),
              z = (0, n.useCallback)(() => W(""), [W]);
            (0, n.useEffect)(() => () => j(), [j]);
            const U = (0, n.useCallback)(
              (e) => {
                (j(),
                  O.debounceTime
                    ? (H.current.debounceTimeout = window.setTimeout(() => {
                        G(e);
                      }, O.debounceTime))
                    : G(e));
              },
              [G, j, O.debounceTime],
            );
            ((0, n.useEffect)(() => {
              H.current.isChangeHandled ||
                H.current.value !== N ||
                (U(H.current.value), (H.current.isChangeHandled = !0));
            }, [N, U]),
              (0, n.useEffect)(() => {
                (H.current.isChangeHandled &&
                  m !== H.current.value &&
                  ((H.current.value = m), T(m)),
                  (H.current.type = r));
              }, [m, r]),
              (0, n.useEffect)(() => {
                P(p);
              }, [p, i]));
            const $ = (0, n.useCallback)((e) => D && D(e), [D]),
              Z = (0, n.useCallback)(
                (e) => {
                  (O.disableHighlightOnFocus && R && P(!1), v && v(e));
                },
                [R, v, O.disableHighlightOnFocus],
              ),
              V = (0, n.useCallback)((e) => f && f(e), [f]),
              X = (0, n.useCallback)((e) => w && w(e), [w]),
              q = (0, n.useCallback)((e) => B && B(e), [B]),
              K = (0, n.useMemo)(
                () =>
                  O.withTypeIcon
                    ? (function (e, t) {
                        return e === le ? he.$dyn(`search_${t}`) : "";
                      })(r, c)
                    : "",
                [r, c, O.withTypeIcon],
              ),
              Y = g || Fe[r],
              Q = Boolean(N),
              J = h ? ge : i,
              ee = Boolean(h) || R,
              te = (0, n.useMemo)(
                () => ("boolean" == typeof O.withClear ? Q && O.withClear : Q && r === le),
                [r, Q, O],
              ),
              ue = o()(ye.base, ye[`base__${c}`], ye[`base__${i}`], k);
            return a().createElement(
              "div",
              {
                id: t,
                className: ue,
                onMouseEnter: $,
                onMouseDown: X,
                onMouseUp: V,
                onMouseLeave: q,
              },
              a().createElement(
                _.l,
                { tooltipArgs: d },
                a().createElement(
                  Be,
                  Se(
                    {
                      componentId: t ? `${t}-inputControl` : void 0,
                      iconSource: K,
                      size: c,
                      type: r,
                      variant: J,
                      value: N,
                      withClear: te,
                      highlighted: ee,
                      selectOnFocus: O.selectOnFocus,
                      maxLength: O.maxLength,
                      classMix: S,
                      onFocus: Z,
                      onChange: W,
                      onClear: z,
                    },
                    x,
                  ),
                ),
              ),
              Y &&
                a().createElement(
                  "div",
                  { className: ye.helper },
                  a().createElement(we, {
                    variant: J,
                    show: F && (O.isPermanentHelper || ee),
                    helperText: h || Y,
                    helperIcon: O.helperIconSource,
                    classMix: L,
                  }),
                ),
            );
          },
          Ie = ({
            value: e,
            placeholder: t,
            tooltipHeader: u,
            onChange: n,
            className: r,
            tooltipBody: o,
          }) =>
            a().createElement(
              c.i,
              { header: null != u ? u : void 0, body: o, isEnabled: Boolean(u || o) },
              a().createElement(xe, {
                type: le,
                placeholder: null != t ? t : void 0,
                value: e,
                classMix: r,
                onChange: n,
              }),
            ),
          Ne = {
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
        var Te = u(5415);
        const Me = R.strings.crew.filterPanel,
          Re = (0, d.Pi)(({ popoverDirection: e }) => {
            const t = Z(),
              u = t.model,
              n = t.controls,
              r = u.root.get(),
              d = r.hasDiscountAlert,
              _ = r.isPopoverHighlighted,
              E = r.isPopoverEnabled,
              g = r.searchTooltipBody,
              A = r.searchTooltipHeader,
              p = r.searchPlaceholder,
              C = r.searchString,
              F = r.isSearchEnabled,
              h = r.title,
              b = r.panelType,
              v = r.hasAppliedFilters,
              D = r.popoverTooltipHeader,
              B = r.popoverTooltipBody,
              f = r.isSelectedMode,
              w = r.isSelectButtonVisible,
              y = r.isSelectButtonActive,
              k = r.isSelectedLimitReached,
              S = u.amountInfo.get(),
              L = S.from,
              x = S.to,
              I = u.computes.getFilterGroup(),
              N = u.computes.getFilters(),
              T = u.computes.getIsRestoreFilter(),
              M = v || (0 === L && 0 === x) || f,
              P =
                (0, Te.GS)().mediaSize === Te.cJ.ExtraSmall && f
                  ? R.strings.crew.tankmanList.selected.titleSmall()
                  : h;
            return a().createElement(
              "div",
              { className: o()(Ne.base, Ne[`base__${b}`]) },
              a().createElement(
                "div",
                { className: Ne.titleWrapper },
                a().createElement(H.C, {
                  title: P || "",
                  isGlowVisible: M,
                  isSelectedLimitReached: k,
                  isFilterRange: !0,
                  isSelectMode: f,
                  from: L,
                  to: x,
                  className: Ne.title,
                  classNames: { counterGlow: Ne.counterGlow },
                }),
                v && a().createElement(se, { isSelectMode: f, onClick: n.resetFilter }),
              ),
              a().createElement(
                "div",
                { className: Ne.filters },
                F &&
                  a().createElement(
                    a().Fragment,
                    null,
                    a().createElement(Ie, {
                      value: C,
                      onChange: n.search,
                      className: Ne.search,
                      placeholder: p,
                      tooltipHeader: A,
                      tooltipBody: g,
                    }),
                    b === m.Barracks && w && a().createElement("div", { className: Ne.separator }),
                  ),
                I.label && a().createElement(l.ZP, { className: Ne.filterLabel, text: I.label }),
                w &&
                  (f
                    ? a().createElement(
                        a().Fragment,
                        null,
                        a().createElement(
                          s.u5,
                          { mixClass: Ne.button, type: i.L.primary, onClick: n.onCancelSelection },
                          a().createElement(l.ZP, { text: Me.demobilize.cancel() }),
                        ),
                        a().createElement(
                          s.u5,
                          {
                            mixClass: o()(Ne.button, Ne.button__demobilize),
                            type: i.L.main,
                            onClick: n.onDismissOrRestore,
                            disabled: !y,
                          },
                          a().createElement(l.ZP, {
                            text: T ? Me.restore.confirm() : Me.demobilize.confirm(),
                          }),
                        ),
                      )
                    : a().createElement(
                        s.u5,
                        { mixClass: Ne.button, type: i.L.secondary, onClick: n.updateSelectMode },
                        a().createElement(l.ZP, { text: Me.selectMode.title() }),
                      )),
                (w || F) && a().createElement("div", { className: Ne.separator }),
                a().createElement(O, {
                  id: I.id,
                  label: I.label,
                  type: I.type,
                  hasDiscount: I.hasDiscount,
                  filters: N,
                  toggleProps: { type: i.L.ghost },
                  onClick: n.updateFilter,
                }),
                E &&
                  a().createElement(
                    c.i,
                    { header: D || void 0, body: B || void 0, isEnabled: Boolean(D || B) },
                    a().createElement(
                      "div",
                      { className: Ne.popupButtonWrapper },
                      a().createElement(ue, {
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
            a().createElement(
              $,
              { options: { rootId: R.views.lobby.crew.widgets.FilterPanelWidget("resId") } },
              a().createElement(Re, { popoverDirection: e }),
            );
      },
      8271: (e, t, u) => {
        "use strict";
        let n;
        (u.d(t, { W: () => n }),
          (function (e) {
            ((e.New = "new"),
              (e.Learned = "learned"),
              (e.Learning = "learning"),
              (e.Irrelevant = "irrelevant"),
              (e.Possible = "possible"),
              (e.ZeroSkill = "zeroSkill"));
          })(n || (n = {})));
      },
      2603: (e, t, u) => {
        "use strict";
        u.d(t, { HZ: () => n, v$: () => a });
        const n = "crewPerkGf",
          a = "tankman";
      },
      5026: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
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
      6880: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
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
      8055: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
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
      5287: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
        const n = { base: "FormatText_base_d0" };
      },
      4769: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
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
      3393: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
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
      3938: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
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
      9426: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
        const n = {
          base: "TankmanSkill_base_84",
          base__big: "TankmanSkill_base__big_a0",
          bg: "TankmanSkill_bg_f9",
          icon: "TankmanSkill_icon_1b",
          icon__irrelevant: "TankmanSkill_icon__irrelevant_50",
        };
      },
      4723: (e, t, u) => {
        "use strict";
        u.d(t, { Z: () => n });
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
    var u = (__webpack_module_cache__[e] = { exports: {} });
    return (__webpack_modules__[e](u, u.exports, __webpack_require__), u.exports);
  }
  ((__webpack_require__.m = __webpack_modules__),
    (deferred = []),
    (__webpack_require__.O = (e, t, u, n) => {
      if (!t) {
        var a = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [t, u, n] = deferred[i], r = !0, o = 0; o < t.length; o++)
            (!1 & n || a >= n) &&
            Object.keys(__webpack_require__.O).every((e) => __webpack_require__.O[e](t[o]))
              ? t.splice(o--, 1)
              : ((r = !1), n < a && (a = n));
          if (r) {
            deferred.splice(i--, 1);
            var s = u();
            void 0 !== s && (e = s);
          }
        }
        return e;
      }
      n = n || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > n; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [t, u, n];
    }),
    (__webpack_require__.n = (e) => {
      var t = e && e.__esModule ? () => e.default : () => e;
      return (__webpack_require__.d(t, { a: t }), t);
    }),
    (__webpack_require__.d = (e, t) => {
      for (var u in t)
        __webpack_require__.o(t, u) &&
          !__webpack_require__.o(e, u) &&
          Object.defineProperty(e, u, { enumerable: !0, get: t[u] });
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
    (__webpack_require__.j = 587),
    (() => {
      var e = { 587: 0, 3: 0, 595: 0 };
      __webpack_require__.O.j = (t) => 0 === e[t];
      var t = (t, u) => {
          var n,
            a,
            [r, o, s] = u,
            i = 0;
          if (r.some((t) => 0 !== e[t])) {
            for (n in o) __webpack_require__.o(o, n) && (__webpack_require__.m[n] = o[n]);
            if (s) var l = s(__webpack_require__);
          }
          for (t && t(u); i < r.length; i++)
            ((a = r[i]), __webpack_require__.o(e, a) && e[a] && e[a][0](), (e[a] = 0));
          return __webpack_require__.O(l);
        },
        u = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (u.forEach(t.bind(null, 0)), (u.push = t.bind(null, u.push.bind(u))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [56], () => __webpack_require__(2316));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
