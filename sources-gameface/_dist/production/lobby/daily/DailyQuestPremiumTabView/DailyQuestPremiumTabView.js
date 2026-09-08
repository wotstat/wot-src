(() => {
  var __webpack_modules__ = {
      3779: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => _ });
        var r = t(6483),
          E = t.n(r),
          a = t(9887),
          A = t.n(a),
          n = t(3377),
          i = t(6179),
          F = t.n(i),
          D = t(5026);
        const s = [
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
        Object.keys(A());
        const l = {
            XL: { mt: D.Z.mt__XL, mr: D.Z.mr__XL, mb: D.Z.mb__XL, ml: D.Z.ml__XL },
            LG: { mt: D.Z.mt__LG, mr: D.Z.mr__LG, mb: D.Z.mb__LG, ml: D.Z.ml__LG },
            MDp: { mt: D.Z.mt__MDp, mr: D.Z.mr__MDp, mb: D.Z.mb__MDp, ml: D.Z.ml__MDp },
            MD: { mt: D.Z.mt__MD, mr: D.Z.mr__MD, mb: D.Z.mb__MD, ml: D.Z.ml__MD },
            SMp: { mt: D.Z.mt__SMp, mr: D.Z.mr__SMp, mb: D.Z.mb__SMp, ml: D.Z.ml__SMp },
            SM: { mt: D.Z.mt__SM, mr: D.Z.mr__SM, mb: D.Z.mb__SM, ml: D.Z.ml__SM },
            XS: { mt: D.Z.mt__XS, mr: D.Z.mr__XS, mb: D.Z.mb__XS, ml: D.Z.ml__XS },
          },
          B = (Object.keys(l), ["mt", "mr", "mb", "ml"]),
          C = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          _ = (0, n.ZP)((u) => {
            let e = u.className,
              t = u.width,
              r = u.height,
              a = u.m,
              A = u.mt,
              n = void 0 === A ? a : A,
              _ = u.mr,
              c = void 0 === _ ? a : _,
              m = u.mb,
              d = void 0 === m ? a : m,
              h = u.ml,
              g = void 0 === h ? a : h,
              b = u.column,
              p = u.row,
              v = u.flexDirection,
              x = void 0 === v ? (b ? "column" : p && "row") || void 0 : v,
              f = u.flexStart,
              w = u.center,
              S = u.flexEnd,
              T = u.spaceBetween,
              L = u.spaceAround,
              M = u.justifyContent,
              y =
                void 0 === M
                  ? (f ? "flex-start" : w && "center") ||
                    (S && "flex-end") ||
                    (T && "space-between") ||
                    (L && "space-around") ||
                    void 0
                  : M,
              O = u.alignItems,
              R =
                void 0 === O
                  ? (f ? "flex-start" : w && "center") || (S && "flex-end") || void 0
                  : O,
              P = u.alignSelf,
              N = u.wrap,
              k = u.flexWrap,
              H = void 0 === k ? (N ? "wrap" : void 0) : k,
              W = u.grow,
              j = u.shrink,
              I = u.flex,
              U = void 0 === I ? (W || j ? `${W ? 1 : 0} ${j ? 1 : 0} auto` : void 0) : I,
              G = u.style,
              Z = u.children,
              X = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  E = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (E[t] = u[t]));
                return E;
              })(u, s);
            const K = (0, i.useMemo)(() => {
                const u = { mt: n, mr: c, mb: d, ml: g },
                  e = ((u) =>
                    B.reduce((e, t) => {
                      const r = u[t];
                      return r && "number" != typeof r ? e.concat(l[!0 === r ? "MD" : r][t]) : e;
                    }, []))(u),
                  E = ((u) =>
                    B.reduce((e, t) => {
                      const r = u[t];
                      return ("number" == typeof r && (e[C[t]] = r + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, G, E, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== r && "number" == typeof r ? r + "rem" : r,
                    flex: U,
                    alignSelf: P,
                    display: x || R ? "flex" : void 0,
                    flexDirection: x,
                    flexWrap: H,
                    justifyContent: y,
                    alignItems: R,
                  }),
                  computedClassNames: e,
                };
              }, [t, r, n, c, d, g, G, U, P, x, H, y, R]),
              Q = K.computedStyle,
              q = K.computedClassNames;
            return F().createElement(
              "div",
              o({ className: E()(D.Z.base, ...q, e), style: Q }, X),
              Z,
            );
          });
      },
      280: (u, e, t) => {
        "use strict";
        t.d(e, { z: () => F });
        var r = t(6179),
          E = t.n(r),
          a = t(6483),
          A = t.n(a),
          n = t(3649),
          i = t(5287);
        const F = ({ binding: u, text: e = "", classMix: t, alignment: a = n.v2.left }) =>
          null === e
            ? (console.error("FormatText was supplied with 'null'"), null)
            : E().createElement(
                r.Fragment,
                null,
                e.split("\n").map((e, F) =>
                  E().createElement(
                    "div",
                    { className: A()(i.Z.base, t), key: `${e}-${F}` },
                    (0, n.Uw)(e, a, u).map((u, e) =>
                      E().createElement(r.Fragment, { key: `${e}-${u}` }, u),
                    ),
                  ),
                ),
              );
      },
      3495: (u, e, t) => {
        "use strict";
        t.d(e, { Y: () => s });
        var r = t(3138),
          E = t(6179),
          a = t(1043),
          A = t(5262);
        const n = r.O.client.getSize("rem"),
          i = n.width,
          F = n.height,
          D = Object.assign({ width: i, height: F }, (0, A.T)(i, F, a.j)),
          s = (0, E.createContext)(D);
      },
      1039: (u, e, t) => {
        "use strict";
        var r = t(6179),
          E = t.n(r),
          a = t(6536),
          A = t(3495),
          n = t(1043),
          i = t(5262),
          F = t(3138);
        (0, r.memo)(({ children: u }) => {
          const e = (0, r.useContext)(A.Y),
            t = (0, r.useState)(e),
            D = t[0],
            s = t[1],
            o = (0, r.useCallback)((u, e) => {
              const t = F.O.view.pxToRem(u),
                r = F.O.view.pxToRem(e);
              s(Object.assign({ width: t, height: r }, (0, i.T)(t, r, n.j)));
            }, []);
          ((0, a.Z)(() => {
            engine.on("clientResized", o);
          }),
            (0, r.useEffect)(() => () => engine.off("clientResized", o), [o]));
          const l = (0, r.useMemo)(() => Object.assign({}, D), [D]);
          return E().createElement(A.Y.Provider, { value: l }, u);
        });
      },
      6010: (u, e, t) => {
        "use strict";
        var r = t(6179),
          E = t(7382),
          a = t(3495);
        const A = ["children"];
        const n = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                r,
                E = {},
                a = Object.keys(u);
              for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (E[t] = u[t]));
              return E;
            })(u, A);
          const n = (0, r.useContext)(a.Y),
            i = n.extraLarge,
            F = n.large,
            D = n.medium,
            s = n.small,
            o = n.extraSmall,
            l = n.extraLargeWidth,
            B = n.largeWidth,
            C = n.mediumWidth,
            _ = n.smallWidth,
            c = n.extraSmallWidth,
            m = n.extraLargeHeight,
            d = n.largeHeight,
            h = n.mediumHeight,
            g = n.smallHeight,
            b = n.extraSmallHeight,
            p = { extraLarge: m, large: d, medium: h, small: g, extraSmall: b };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && i) return e;
            if (t.large && F) return e;
            if (t.medium && D) return e;
            if (t.small && s) return e;
            if (t.extraSmall && o) return e;
          } else {
            if (t.extraLargeWidth && l) return (0, E.H)(e, t, p);
            if (t.largeWidth && B) return (0, E.H)(e, t, p);
            if (t.mediumWidth && C) return (0, E.H)(e, t, p);
            if (t.smallWidth && _) return (0, E.H)(e, t, p);
            if (t.extraSmallWidth && c) return (0, E.H)(e, t, p);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && m) return e;
              if (t.largeHeight && d) return e;
              if (t.mediumHeight && h) return e;
              if (t.smallHeight && g) return e;
              if (t.extraSmallHeight && b) return e;
            }
          }
          return null;
        };
        n.defaultProps = {
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
        (0, r.memo)(n);
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
        function E(u, e, t) {
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
            E = (function (u, e) {
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
            a = Math.min(r, E);
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
            extraLargeHeight: E === t.extraLarge.weight,
            largeHeight: E === t.large.weight,
            mediumHeight: E === t.medium.weight,
            smallHeight: E === t.small.weight,
            extraSmallHeight: E === t.extraSmall.weight,
          };
        }
        (t.d(e, { T: () => E }),
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
      7613: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => v });
        var r = t(6483),
          E = t.n(r),
          a = t(3779),
          A = t(280),
          n = t(3532),
          i = t.n(n),
          F = t(9887),
          D = t.n(F),
          s = t(3377),
          o = t(6179),
          l = t.n(o),
          B = t(3393);
        const C = [
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
        Object.keys(D());
        const c = Object.keys(i()),
          m = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          d = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
          h = { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          g = {
            XL: { mt: "XL", mr: "XL", mb: "XL", ml: "XL" },
            LG: { mt: "LG", mr: "LG", mb: "LG", ml: "LG" },
            MDp: { mt: "MDp", mr: "MDp", mb: "MDp", ml: "MDp" },
            MD: { mt: "MD", mr: "MD", mb: "MD", ml: "MD" },
            SMp: { mt: "SMp", mr: "SMp", mb: "SMp", ml: "SMp" },
            SM: { mt: "SM", mr: "SM", mb: "SM", ml: "SM" },
            XS: { mt: "XS", mr: "XS", mb: "XS", ml: "XS" },
          },
          b =
            (Object.keys(g),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": m,
              "heading-H36": m,
              "heading-H28": d,
              "heading-H24": d,
              "heading-H24R": d,
              "heading-H22": d,
              "heading-H20R": d,
              "heading-H18": d,
              "heading-H15": h,
              "heading-H14": h,
              "paragraph-P24": d,
              "paragraph-P18": d,
              "paragraph-P16": d,
              "paragraph-P14": h,
              "paragraph-P12": h,
              "paragraph-P10": h,
            }),
          p =
            (Object.keys(b),
            (u) =>
              u
                ? ((u) => c.includes(u))(u)
                  ? { colorClassName: B.Z[u] }
                  : { colorStyle: { color: u } }
                : {}),
          v = (0, s.ZP)((u) => {
            let e = u.text,
              t = u.variant,
              r = u.className,
              n = u.color,
              i = u.m,
              F = u.mt,
              D = void 0 === F ? i : F,
              s = u.mr,
              c = void 0 === s ? i : s,
              m = u.mb,
              d = void 0 === m ? i : m,
              h = u.ml,
              g = void 0 === h ? i : h,
              v = u.style,
              x = u.format,
              f = (function (u, e) {
                if (null == u) return {};
                var t,
                  r,
                  E = {},
                  a = Object.keys(u);
                for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (E[t] = u[t]));
                return E;
              })(u, C);
            const w = (0, o.useMemo)(() => {
                const u = p(n),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  r = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, v, r), colorClassName: e };
              }, [v, n]),
              S = w.computedStyle,
              T = w.colorClassName;
            return l().createElement(
              a.ZP,
              _(
                {
                  className: E()(B.Z.base, t && B.Z[t], T, r),
                  style: S,
                  mt: !0 === D ? b[t || "paragraph-P16"].mt : D,
                  mr: !0 === c ? b[t || "paragraph-P16"].mr : c,
                  mb: !0 === d ? b[t || "paragraph-P16"].mb : d,
                  ml: !0 === g ? b[t || "paragraph-P16"].ml : g,
                },
                f,
              ),
              void 0 !== x ? l().createElement(A.z, _({}, x, { text: e })) : e,
            );
          });
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
      122: (u, e, t) => {
        "use strict";
        t.d(e, { F: () => r });
        const r = (u, e) => {
          let t;
          const r = setTimeout(() => {
            t = u();
          }, e);
          return () => {
            ("function" == typeof t && t(), clearTimeout(r));
          };
        };
      },
      8246: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => n });
        var r = t(3138);
        function E(u, e) {
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
        const A = (u) => (0 === u ? window : window.subViews.get(u));
        function n({
          initializer: u = !0,
          rootId: e = 0,
          getRoot: t = A,
          context: a = "model",
        } = {}) {
          const n = new Map();
          function i(u, e = 0) {
            viewEnv.removeDataChangedCallback(u, e)
              ? n.delete(u)
              : console.error("Can't remove callback by id:", u);
          }
          engine.whenReady.then(() => {
            engine.on("viewEnv.onDataChanged", (u, e, t) => {
              t.forEach((e) => {
                const t = n.get(e);
                void 0 !== t && t(u);
              });
            });
          });
          const F = (u) => {
            const r = t(e),
              E = a.split(".").reduce((u, e) => u[e], r);
            return "string" != typeof u || 0 === u.length
              ? E
              : u.split(".").reduce((u, e) => {
                  const t = u[e];
                  return "function" == typeof t ? t.bind(u) : t;
                }, E);
          };
          return {
            subscribe: (t, E) => {
              const A = "string" == typeof E ? `${a}.${E}` : a,
                i = r.O.view.addModelObserver(A, e, !0);
              return (n.set(i, t), u && t(F(E)), i);
            },
            readByPath: F,
            createCallback: (u, e) => {
              const t = F(e);
              return (...e) => {
                t(u(...e));
              };
            },
            createCallbackNoArgs: (u) => {
              const e = F(u);
              return () => {
                e();
              };
            },
            dispose: function () {
              for (var u, t = E(n.keys()); !(u = t()).done;) {
                i(u.value, e);
              }
            },
            unsubscribe: i,
          };
        }
      },
      3215: (u, e, t) => {
        "use strict";
        t.d(e, { q: () => i });
        var r = t(4598),
          E = t(9174),
          a = t(6179),
          A = t.n(a),
          n = t(8246);
        const i = () => (u, e) => {
          const t = (0, a.createContext)({});
          return [
            function ({ mode: i = "real", options: F, children: D, mocks: s }) {
              const o = (0, a.useRef)([]),
                l = (t, a, A) => {
                  var i;
                  const F = n.U(a),
                    D =
                      "real" === t
                        ? F
                        : Object.assign({}, F, {
                            readByPath: null != (i = null == A ? void 0 : A.getter) ? i : () => {},
                          }),
                    s = (u) =>
                      "mocks" === t ? (null == A ? void 0 : A.getter(u)) : D.readByPath(u),
                    l = (u) => o.current.push(u),
                    B = u({
                      mode: t,
                      readByPath: s,
                      externalModel: D,
                      observableModel: {
                        array: (u, e) => {
                          const a = null != e ? e : s(u),
                            A = E.LO.box(a, { equals: r.jv });
                          return (
                            "real" === t &&
                              D.subscribe(
                                (0, E.aD)((u) => A.set(u)),
                                u,
                              ),
                            A
                          );
                        },
                        object: (u, e) => {
                          const a = null != e ? e : s(u),
                            A = E.LO.box(a, { equals: r.jv });
                          return (
                            "real" === t &&
                              D.subscribe(
                                (0, E.aD)((u) => A.set(u)),
                                u,
                              ),
                            A
                          );
                        },
                        primitives: (u, e) => {
                          const r = s(e);
                          if (Array.isArray(u)) {
                            const a = u.reduce((u, e) => ((u[e] = E.LO.box(r[e], {})), u), {});
                            return (
                              "real" === t &&
                                D.subscribe(
                                  (0, E.aD)((e) => {
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
                              A = Object.entries(a),
                              n = A.reduce((u, [e, t]) => ((u[t] = E.LO.box(r[e], {})), u), {});
                            return (
                              "real" === t &&
                                D.subscribe(
                                  (0, E.aD)((u) => {
                                    A.forEach(([e, t]) => {
                                      n[t].set(u[e]);
                                    });
                                  }),
                                  e,
                                ),
                              n
                            );
                          }
                        },
                      },
                      cleanup: l,
                    }),
                    C = { mode: t, model: B, externalModel: D, cleanup: l };
                  return {
                    model: B,
                    controls: "mocks" === t && A ? A.controls(C) : e(C),
                    externalModel: D,
                    mode: t,
                  };
                },
                B = (0, a.useRef)(!1),
                C = (0, a.useState)(i),
                _ = C[0],
                c = C[1],
                m = (0, a.useState)(() => l(i, F, s)),
                d = m[0],
                h = m[1];
              return (
                (0, a.useEffect)(() => {
                  B.current ? h(l(_, F, s)) : (B.current = !0);
                }, [s, _, F]),
                (0, a.useEffect)(() => {
                  c(i);
                }, [i]),
                (0, a.useEffect)(
                  () => () => {
                    (d.externalModel.dispose(), o.current.forEach((u) => u()));
                  },
                  [d],
                ),
                A().createElement(t.Provider, { value: d }, D)
              );
            },
            () => (0, a.useContext)(t),
          ];
        };
      },
      7044: (u, e, t) => {
        "use strict";
        (t(3649), t(728), t(4179));
        Date.now();
      },
      527: (u, e, t) => {
        "use strict";
        (t.r(e), t.d(e, { mouse: () => n, onResize: () => a }));
        var r = t(2472),
          E = t(1176);
        const a = (0, r.E)("clientResized"),
          A = { down: (0, r.E)("mousedown"), up: (0, r.E)("mouseup"), move: (0, r.E)("mousemove") };
        const n = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && (0, E.R)(!1);
          }
          function t() {
            u.enabled && (0, E.R)(!0);
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
              : (0, E.R)(!1);
          }
          const a = ["down", "up", "move"].reduce(
            (e, t) => (
              (e[t] = (function (e) {
                return (t) => {
                  u.listeners += 1;
                  let E = !0;
                  const a = `mouse${e}`,
                    n = A[e]((u) => t([u, "outside"]));
                  function i(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(a, i),
                    r(),
                    () => {
                      E &&
                        (n(), window.removeEventListener(a, i), (u.listeners -= 1), r(), (E = !1));
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
              u.enabled && (0, E.R)(!0);
            },
            disableOutside() {
              u.enabled && (0, E.R)(!1);
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
            getSize: () => E,
            graphicsQuality: () => A,
          }));
        var r = t(527);
        function E(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function a(u = "px") {
          return "rem" === u
            ? viewEnv.getMouseGlobalPositionRem()
            : viewEnv.getMouseGlobalPositionPx();
        }
        const A = {
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
        t.d(e, { O: () => E });
        var r = t(5959);
        const E = { view: t(7641), client: r };
      },
      3722: (u, e, t) => {
        "use strict";
        function r(u, e, t = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, t);
        }
        function E(u, e, t) {
          return `url(${r(u, e, t)})`;
        }
        (t.r(e), t.d(e, { getBgUrl: () => E, getTextureUrl: () => r }));
      },
      6112: (u, e, t) => {
        "use strict";
        t.d(e, { W: () => r });
        const r = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => E });
        var r = t(2472);
        const E = {
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
            addModelObserver: () => D,
            addPreloadTexture: () => n,
            children: () => r,
            displayStatus: () => E.W,
            displayStatusIs: () => f,
            events: () => a.U,
            extraSize: () => w,
            forceTriggerMouseMove: () => v,
            freezeTextureBeforeResize: () => C,
            getBrowserTexturePath: () => F,
            getDisplayStatus: () => x,
            getScale: () => _,
            getSize: () => o,
            getViewGlobalPosition: () => B,
            isClientAccessible: () => g,
            isEventHandled: () => p,
            isFocused: () => h,
            pxToRem: () => c,
            remToPx: () => m,
            resize: () => l,
            sendEvent: () => A.qP,
            setAnimateWindow: () => d,
            setEventHandled: () => b,
            setInputPaddingsRem: () => i,
            setSidePaddingsRem: () => s,
            whenTutorialReady: () => S,
          }));
        var r = t(3722),
          E = t(6112),
          a = t(6538),
          A = t(8566);
        function n(u) {
          viewEnv.addPreloadTexture(u);
        }
        function i(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function F(u, e, t, r = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, r);
        }
        function D(u, e, t) {
          return viewEnv.addDataChangedCallback(u, e, t);
        }
        function s(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function o(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function l(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function B(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: m(e.x), y: m(e.y) };
        }
        function C() {
          viewEnv.freezeTextureBeforeResize();
        }
        function _() {
          return viewEnv.getScale();
        }
        function c(u) {
          return viewEnv.pxToRem(u);
        }
        function m(u) {
          return viewEnv.remToPx(u);
        }
        function d(u, e) {
          viewEnv.setAnimateWindow(u, e);
        }
        function h() {
          return viewEnv.isFocused();
        }
        function g() {
          return viewEnv.isClientAccessible();
        }
        function b() {
          return viewEnv.setEventHandled();
        }
        function p() {
          return viewEnv.isEventHandled();
        }
        function v() {
          viewEnv.forceTriggerMouseMove();
        }
        function x() {
          return viewEnv.getShowingStatus();
        }
        const f = Object.keys(E.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === E.W[e]), u),
            {},
          ),
          w = {
            set: (u, e) => {
              viewEnv.setExtraSizeRem(u, e);
            },
            get: (u, e) => {
              viewEnv.getExtraSizeRem(u, e);
            },
          },
          S = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : a.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        "use strict";
        t.d(e, { qP: () => F });
        const r = ["args"];
        const E = 2,
          a = 16,
          A = 32,
          n = 64,
          i = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const a = e.args,
                A = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    r,
                    E = {},
                    a = Object.keys(u);
                  for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (E[t] = u[t]));
                  return E;
                })(e, r);
              return void 0 !== a
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, A, {
                      arguments:
                        ((E = a),
                        Object.entries(E).map(([u, e]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, A));
            }
            return viewEnv.handleViewEvent({ __Type: t, type: u });
            var E;
          },
          F = {
            close(u) {
              i("popover" === u ? E : A);
            },
            minimize() {
              i(n);
            },
            move(u) {
              i(a, { isMouseEvent: !0, on: u });
            },
          };
      },
      4598: (u, e, t) => {
        "use strict";
        function r() {}
        t.d(e, { ZT: () => r, jv: () => a, yR: () => E });
        function E(u) {
          return u;
        }
        function a() {
          return !1;
        }
        console.log;
      },
      3377: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => D });
        var r = t(5415),
          E = t(6179),
          a = t.n(E);
        const A = ["xl", "lg", "md", "sm", "xs"],
          n = (u) => u.includes("_") && ((u) => A.includes(u))(u.split("_").at(-1)),
          i = [r.cJ.ExtraLarge, r.cJ.Large, r.cJ.Medium, r.cJ.Small, r.cJ.ExtraSmall],
          F = (u, e) =>
            Object.keys(u).reduce((t, r) => {
              if (r in t) return t;
              if (n(r)) {
                const E = r.split("_").slice(0, -1).join("_");
                if (E in t) return t;
                const a = i.indexOf(e),
                  n = (-1 !== a ? A.slice(a) : [])
                    .map((u) => E + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  F = n ? u[n] : void 0;
                return ((t[E] = void 0 !== F ? F : u[E]), t);
              }
              const E = u[r];
              return (
                void 0 === E ||
                  ((u, e) => A.some((t) => void 0 !== e[`${u}_${t}`]))(r, u) ||
                  (t[r] = E),
                t
              );
            }, {}),
          D = (u, e = F) => {
            const t = (
              (u, e = F) =>
              (t) => {
                const A = (0, r.GS)().mediaSize,
                  n = (0, E.useMemo)(() => e(t, A), [t, A]);
                return a().createElement(u, n);
              }
            )(u, e);
            return a().memo((e) =>
              Object.keys(e).some((u) => n(u) && void 0 !== e[u])
                ? a().createElement(t, e)
                : a().createElement(u, e),
            );
          };
      },
      2344: (u, e, t) => {
        "use strict";
        t.d(e, { D9: () => E });
        var r = t(2790);
        (t(3469), t(2133), t(579), t(5360), t(9056));
        const E = r.Z;
      },
      6536: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => E });
        var r = t(6179);
        const E = (u) => {
          const e = (0, r.useRef)(!1);
          e.current || (u(), (e.current = !0));
        };
      },
      3469: (u, e, t) => {
        "use strict";
        (t(7044), t(6179));
      },
      2133: (u, e, t) => {
        "use strict";
        t(6179);
      },
      5415: (u, e, t) => {
        "use strict";
        t.d(e, { GS: () => F, cJ: () => A });
        var r = t(6179),
          E = t(7739),
          a = t(1043);
        let A, n, i;
        (!(function (u) {
          ((u[(u.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = a.j.small.width)] = "Small"),
            (u[(u.Medium = a.j.medium.width)] = "Medium"),
            (u[(u.Large = a.j.large.width)] = "Large"),
            (u[(u.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
        })(A || (A = {})),
          (function (u) {
            ((u[(u.ExtraSmall = a.j.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = a.j.small.width)] = "Small"),
              (u[(u.Medium = a.j.medium.width)] = "Medium"),
              (u[(u.Large = a.j.large.width)] = "Large"),
              (u[(u.ExtraLarge = a.j.extraLarge.width)] = "ExtraLarge"));
          })(n || (n = {})),
          (function (u) {
            ((u[(u.ExtraSmall = a.j.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = a.j.small.height)] = "Small"),
              (u[(u.Medium = a.j.medium.height)] = "Medium"),
              (u[(u.Large = a.j.large.height)] = "Large"),
              (u[(u.ExtraLarge = a.j.extraLarge.height)] = "ExtraLarge"));
          })(i || (i = {})));
        const F = () => {
          const u = (0, r.useContext)(E.YN),
            e = u.width,
            t = u.height,
            a = ((u) => {
              switch (!0) {
                case u.extraLarge:
                  return A.ExtraLarge;
                case u.large:
                  return A.Large;
                case u.medium:
                  return A.Medium;
                case u.small:
                  return A.Small;
                case u.extraSmall:
                  return A.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), A.ExtraSmall);
              }
            })(u),
            F = ((u) => {
              switch (!0) {
                case u.extraLargeWidth:
                  return n.ExtraLarge;
                case u.largeWidth:
                  return n.Large;
                case u.mediumWidth:
                  return n.Medium;
                case u.smallWidth:
                  return n.Small;
                case u.extraSmallWidth:
                  return n.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), n.ExtraSmall);
              }
            })(u),
            D = ((u) => {
              switch (!0) {
                case u.extraLargeHeight:
                  return i.ExtraLarge;
                case u.largeHeight:
                  return i.Large;
                case u.mediumHeight:
                  return i.Medium;
                case u.smallHeight:
                  return i.Small;
                case u.extraSmallHeight:
                  return i.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), i.ExtraSmall);
              }
            })(u);
          return {
            mediaSize: a,
            mediaWidth: F,
            mediaHeight: D,
            remScreenWidth: e,
            remScreenHeight: t,
          };
        };
      },
      5360: (u, e, t) => {
        "use strict";
        t(6536);
        var r = t(4179);
        t(6179);
        r.Sw.instance;
        let E;
        !(function (u) {
          ((u.None = "None"), (u.Shallow = "Shallow"), (u.Deep = "Deep"));
        })(E || (E = {}));
      },
      9056: (u, e, t) => {
        "use strict";
        var r = t(4179);
        t(6179);
        r.Sw.instance;
      },
      2790: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => E });
        var r = t(6179);
        const E = (u) => {
          const e = (0, r.useRef)();
          return (
            (0, r.useEffect)(() => {
              e.current = u;
            }, [u]),
            e.current
          );
        };
      },
      579: (u, e, t) => {
        "use strict";
        (t(3138), t(6179));
      },
      5521: (u, e, t) => {
        "use strict";
        let r, E;
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
          })(E || (E = {})));
      },
      5175: (u, e, t) => {
        "use strict";
        t.d(e, { c: () => a });
        var r = t(9480);
        const E = (u) =>
            null !== u && "object" == typeof u
              ? "CoherentArrayProxy" === u.constructor.name
                ? r.map(u, (u) => ("object" == typeof u ? E(u) : u))
                : Array.isArray(u)
                  ? u.map((u) => ("object" == typeof u ? E(u) : u))
                  : Object.fromEntries(
                      Object.entries(u).map(([u, e]) => [u, "object" == typeof e ? E(e) : e]),
                    )
              : u,
          a = (u) => E(u);
      },
      9480: (u, e, t) => {
        "use strict";
        t.d(e, { find: () => a, map: () => E });
        function r(u) {
          var e;
          return u && "value" in u && null != (e = u.constructor) && e.name.includes("ArrayItem")
            ? null == u
              ? void 0
              : u.value
            : u;
        }
        function E(u, e) {
          return Array.isArray(u)
            ? u.map(e)
            : u.map((u, t, r) => e(null == u ? void 0 : u.value, t, r));
        }
        function a(u, e) {
          for (let t = 0; t < u.length; t++) {
            const E = r(u[t]);
            if (e(E, t, u)) return E;
          }
        }
      },
      7727: (u, e, t) => {
        "use strict";
        function r(u) {
          engine.call("PlaySound", u);
        }
        t.d(e, { $: () => E });
        const E = {
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
        (t.d(e, { Uw: () => D, v2: () => r }),
          (function (u) {
            ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
          })(r || (r = {})));
        const E = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          a = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          A = (u, e, t = r.left) => u.split(e).reduce(t === r.left ? E : a, []),
          n = (() => {
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
          i = ["zh_cn", "zh_sg", "zh_tw"],
          F = (u, e = r.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return i.includes(t)
              ? n(u)
              : ((u, e = r.left) => {
                  let t = [];
                  const E =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    a = u.replace(/&nbsp;/g, " ");
                  return (A(a, /( )/, e).forEach((u) => (t = t.concat(A(u, E, r.left)))), t);
                })(u, e);
          },
          D = (u, e, t) =>
            u.split(/%\((.*?)\)(?:[sd])?/g).map((u) => (t && u in t ? t[u] : F(u, e)));
      },
      728: (u, e, t) => {
        "use strict";
        let r;
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
        })(r || (r = {}));
      },
      1358: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => a });
        var r = t(3138);
        class E {
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
            return (window.__dataTracker || (window.__dataTracker = new E()), window.__dataTracker);
          }
          clear() {
            (void 0 !== this._updateHandler &&
              (this._updateHandler.clear(), (this._updateHandler = void 0)),
              (this._callbacks = {}));
          }
          addCallback(u, e, t = 0, E = !0) {
            void 0 === this._updateHandler &&
              (this._updateHandler = engine.on(
                "viewEnv.onDataChanged",
                this._emmitDataChanged,
                this,
              ));
            const a = r.O.view.addModelObserver(u, t, E);
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
        E.__instance = void 0;
        const a = E;
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
        t.d(e, { Sw: () => a.Z, ry: () => m });
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
        const E = r;
        var a = t(1358);
        const A = {
            getNumberFormat: (u, e) => systemLocale.getNumberFormat(u, e),
            getRealFormat: (u, e) => systemLocale.getRealFormat(u, e),
            getTimeFormat: (u, e) => systemLocale.getTimeFormat(u, e),
            getDateFormat: (u, e) => systemLocale.getDateFormat(u, e),
            toUpperCase: (u) => systemLocale.toUpperCase(u),
            toLowerCase: (u) => systemLocale.toUpperCase(u),
          },
          n = {
            getNumberFormat: (u) => userLocale.getNumberFormat(u),
            getTimeFormat: (u, e, t) => userLocale.getTimeFormat(u, e, void 0 === t || t),
            getTimeString: (u, e, t) => userLocale.getTimeString(u, e, void 0 === t || t),
          };
        let i;
        !(function (u) {
          ((u[(u.UNDEFINED = 0)] = "UNDEFINED"),
            (u[(u.TOOLTIP = 1)] = "TOOLTIP"),
            (u[(u.POP_OVER = 2)] = "POP_OVER"),
            (u[(u.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (u[(u.DROP_DOWN = 8)] = "DROP_DOWN"),
            (u[(u.MOVE = 16)] = "MOVE"),
            (u[(u.CLOSE = 32)] = "CLOSE"),
            (u[(u.MINIMIZE = 64)] = "MINIMIZE"));
        })(i || (i = {}));
        const F = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          D = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          s = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          o = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var l = t(5521),
          B = t(3138);
        const C = ["args"];
        function _(u, e, t, r, E, a, A) {
          try {
            var n = u[a](A),
              i = n.value;
          } catch (u) {
            return void t(u);
          }
          n.done ? e(i) : Promise.resolve(i).then(r, E);
        }
        const c = (u) => ({
            __Type: "GFBoundingBox",
            x: u.x,
            y: u.y,
            width: u.width,
            height: u.height,
          }),
          m = (function () {
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
                  return new Promise(function (r, E) {
                    var a = u.apply(e, t);
                    function A(u) {
                      _(a, r, E, A, n, "next", u);
                    }
                    function n(u) {
                      _(a, r, E, A, n, "throw", u);
                    }
                    A(void 0);
                  });
                });
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          d = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const E = e.args,
                a = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    r,
                    E = {},
                    a = Object.keys(u);
                  for (r = 0; r < a.length; r++) ((t = a[r]), e.indexOf(t) >= 0 || (E[t] = u[t]));
                  return E;
                })(e, C);
              void 0 !== E
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, a, {
                      arguments:
                        ((r = E),
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
          h = () => d(i.CLOSE),
          g = (u, e) => {
            u.keyCode === l.n.ESCAPE && e();
          };
        var b = t(7572);
        const p = E.instance,
          v = {
            DataTracker: a.Z,
            ViewModel: b.Z,
            ViewEventType: i,
            NumberFormatType: F,
            RealFormatType: D,
            TimeFormatType: s,
            DateFormatType: o,
            makeGlobalBoundingBox: c,
            sendMoveEvent: (u) => d(i.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: h,
            sendClosePopOverEvent: () => d(i.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (u, e, t = 0) => {
              d(i.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, r, E = R.invalid("resId"), a) => {
              const A = B.O.view.getViewGlobalPosition(),
                n = t.getBoundingClientRect(),
                F = n.x,
                D = n.y,
                s = n.width,
                o = n.height,
                l = {
                  x: B.O.view.pxToRem(F) + A.x,
                  y: B.O.view.pxToRem(D) + A.y,
                  width: B.O.view.pxToRem(s),
                  height: B.O.view.pxToRem(o),
                };
              d(i.POP_OVER, {
                isMouseEvent: !0,
                contentID: u,
                decoratorID: r || R.invalid("resId"),
                targetID: E,
                direction: e,
                bbox: c(l),
                on: !0,
                args: a,
              });
            },
            addEscapeListener: (u) => {
              const e = (e) => g(e, u);
              return (
                window.addEventListener("keydown", e),
                () => window.removeEventListener("keydown", e)
              );
            },
            closeOnEsc: (u) => {
              g(u, h);
            },
            handleViewEvent: d,
            onBindingsReady: m,
            onLayoutReady: () =>
              new Promise((u) => {
                requestAnimationFrame(() => {
                  requestAnimationFrame(() => {
                    u();
                  });
                });
              }),
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(i.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(i.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(i.POP_OVER),
            dumpViewModel: function u(e) {
              const t = {};
              if ("object" != typeof e) return e;
              for (const r in e)
                if (Object.prototype.hasOwnProperty.call(e, r)) {
                  const E = Object.prototype.toString.call(e[r]);
                  if (E.startsWith("[object CoherentArrayProxy]")) {
                    const E = e[r];
                    t[r] = [];
                    for (let e = 0; e < E.length; e++) t[r].push({ value: u(E[e].value) });
                  } else
                    E.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[r] = u(e[r]))
                      : (t[r] = e[r]);
                }
              return t;
            },
            ClickOutsideManager: p,
            SystemLocale: A,
            UserLocale: n,
          };
        window.ViewEnvHelper = v;
      },
      2603: (u, e, t) => {
        "use strict";
        var r = t(6179),
          E = t.n(r),
          a = t(3099),
          A = t(3215),
          n = t(4598),
          i = t(9480),
          F = t(5175),
          D = t(3946);
        const s = (0, A.q)()(({ observableModel: u }) => {
            const e = { root: u.object(), quests: u.array("quests", []) },
              t = (0, D.Om)(() => Boolean(s() && s() === o())),
              r = (0, D.Om)(() => i.find(A(), (u) => u.status !== a.N.Done)),
              E = (0, D.Om)((u) =>
                u && u.postBattleCondition.items.length >= 1
                  ? i.map(u.postBattleCondition.items, n.yR)
                  : u && u.bonusCondition.items.length >= 1
                    ? i.map(u.bonusCondition.items, n.yR)
                    : void 0,
              ),
              A = (0, D.Om)(() => (0, F.c)(e.quests.get()), { equals: n.jv }),
              s = (0, D.Om)(() => A().length),
              o = (0, D.Om)(() => A().filter((u) => u.status === a.N.Done).length),
              l = (0, D.Om)(() => {
                const u = r(),
                  e = E(u);
                return (e && e.length) > 0 ? e[0].descrData : void 0;
              });
            return Object.assign({}, e, {
              computes: {
                getCurrentQuest: r,
                getQuests: A,
                getQuestsLength: s,
                getCompletedlQuestLength: o,
                getAllQuestsCompleted: t,
                getConditionDescr: l,
              },
            });
          }, n.ZT),
          o = s[0],
          l = s[1];
        var B = t(8515),
          C = t(9153),
          _ = t(8975),
          c = t(122),
          m = t(3509);
        const d = R.strings.quests.premiumQuests.tab,
          h = R.strings.quests.dailyQuests.tab,
          g = (0, B.Pi)(({ isSelected: u, onClick: e }) => {
            const t = l().model,
              a = t.root.get(),
              A = a.isEnabled,
              n = a.hasPremiumAccount,
              i = a.unseenCount,
              F = t.computes.getAllQuestsCompleted(),
              D = t.computes.getCurrentQuest(),
              s = A ? d.label() : d.disabled.title(),
              o = ((u, e, t, r) =>
                u ? (e ? h.completed() : t ? r : d.disabled.noPrem()) : h.disabled.reason())(
                A,
                F,
                n,
                t.computes.getConditionDescr(),
              ),
              B = (0, r.useState)(o),
              g = B[0],
              b = B[1],
              p = (0, r.useState)(D && D.icon),
              v = p[0],
              x = p[1];
            return (
              (0, r.useEffect)(() => {
                if (n)
                  return (0, c.F)(() => {
                    (b(o), x(D && D.icon));
                  }, m.ji.unlockTabPremiumDuration);
                (b(o), x(D && D.icon));
              }, [n, o, D]),
              E().createElement(_.q, {
                tabIdx: C.g.PremiumQuests,
                isEnabled: A,
                isCompleted: F,
                isSelected: u,
                isPremium: !0,
                hasPremium: n,
                title: s,
                description: g,
                total: t.computes.getQuestsLength(),
                current: t.computes.getCompletedlQuestLength(),
                icon: v,
                bubbleCounter: i,
                onClick: e,
              })
            );
          });
        (0, r.memo)(function (u) {
          const e = (0, r.useMemo)(() => ({ rootId: u.resId }), [u.resId]);
          return E().createElement(o, { options: e }, E().createElement(g, u));
        });
      },
      8975: (u, e, t) => {
        "use strict";
        t.d(e, { q: () => W });
        var r = t(6483),
          E = t.n(r),
          a = t(6179),
          A = t.n(a);
        const n = "DailyQuestsTab_base_fd",
          i = "DailyQuestsTab_base__selected_83",
          F = "DailyQuestsTab_bg_ed",
          D = "DailyQuestsTab_hoverBg_a8",
          s = "DailyQuestsTab_selectedBg_25",
          o = "DailyQuestsTab_disabledBg_6c",
          l = "DailyQuestsTab_premBg_16",
          B = "DailyQuestsTab_base__hover_d3",
          C = "DailyQuestsTab_base__completed_3f",
          _ = "DailyQuestsTab_base__notEnabled_eb",
          c = "DailyQuestsTab_contentWrapper_5b",
          m = "DailyQuestsTab_base__unlock_34",
          d = "DailyQuestsTab_iconWrapper_da",
          h = "DailyQuestsTab_icon_40",
          g = "DailyQuestsTab_status_fe",
          b = "DailyQuestsTab_status__lock_ae",
          p = "DailyQuestsTab_status__alert_43",
          v = "DailyQuestsTab_status__check_15",
          x = "DailyQuestsTab_progress_2c",
          f = "DailyQuestsTab_current_8e",
          w = "DailyQuestsTab_separator_79",
          S = "DailyQuestsTab_rightBlockWrapper_22",
          T = "DailyQuestsTab_bubble_5f",
          L = "DailyQuestsTab_title_3d",
          M = "DailyQuestsTab_description_78",
          y = "DailyQuestsTab_bull_be";
        var O = t(7727),
          P = t(7613),
          N = t(122),
          k = t(2344),
          H = t(3509);
        const W = ({
          tabIdx: u,
          isEnabled: e,
          isSelected: t,
          isCompleted: r,
          isPremium: W,
          hasPremium: j,
          icon: I = "win",
          current: U,
          total: G,
          bubbleCounter: Z,
          title: X,
          description: K,
          onClick: Q,
        }) => {
          var q;
          const Y = null != (q = (0, k.D9)(j)) ? q : j,
            z = (0, a.useState)(!1),
            V = z[0],
            $ = z[1],
            J = (0, a.useState)(!1),
            uu = J[0],
            eu = J[1],
            tu = (0, a.useState)(j),
            ru = tu[0],
            Eu = tu[1],
            au = W && !ru,
            Au = !e || au,
            nu = !e || au || r;
          ((0, a.useEffect)(() => {
            !Y && j && eu(!0);
          }, [Y, j]),
            (0, a.useEffect)(() => {
              if (uu)
                return (
                  Eu(!1),
                  (0, N.F)(() => {
                    (eu(!1), Eu(!0));
                  }, H.ji.unlockTabPremiumDuration)
                );
              Eu(j);
            }, [uu, j]));
          const iu = (0, a.useCallback)(() => {
              t || (O.$.playHighlight(), $(!0));
            }, [t]),
            Fu = (0, a.useCallback)(() => {
              t || $(!1);
            }, [t]),
            Du = (0, a.useCallback)(() => {
              (O.$.playClick(), Q(u), $(!1));
            }, [Q, u]);
          return A().createElement(
            "div",
            {
              className: E()(n, V && B, t && i, e && r && C, !e && _, uu && m),
              onMouseEnter: iu,
              onMouseLeave: Fu,
              onClick: Du,
            },
            A().createElement("div", { className: F }),
            A().createElement("div", { className: D }),
            A().createElement("div", { className: s }),
            W && A().createElement("div", { className: l }),
            Au && A().createElement("div", { className: o }),
            A().createElement(
              "div",
              { className: c },
              Boolean(Z) && A().createElement(P.ZP, { className: T, text: Z.toString() }),
              A().createElement(
                "div",
                { className: d },
                nu
                  ? A().createElement("div", { className: E()(g, au && b, !e && p, r && v) })
                  : A().createElement("div", {
                      className: h,
                      style: {
                        backgroundImage: `url(R.images.gui.maps.icons.missions.icons.c_48_${I}_silver)`,
                      },
                    }),
              ),
              A().createElement("div", { className: w }),
              A().createElement(
                "div",
                { className: S },
                A().createElement(
                  "div",
                  { className: L },
                  A().createElement(P.ZP, { text: X }),
                  e &&
                    A().createElement(P.ZP, {
                      text: R.strings.quests.dailyQuests.tab.progress(),
                      format: {
                        binding: {
                          current: A().createElement(P.ZP, {
                            text: U.toString(),
                            className: E()(U > 0 && f),
                          }),
                          total: A().createElement(P.ZP, { text: G.toString() }),
                        },
                      },
                      className: x,
                    }),
                ),
                A().createElement(
                  "div",
                  { className: M },
                  !nu &&
                    A().createElement(P.ZP, {
                      text: R.strings.quests.dailyQuests.tab.bull(),
                      className: y,
                    }),
                  A().createElement(P.ZP, { text: K }),
                ),
              ),
            ),
          );
        };
      },
      3509: (u, e, t) => {
        "use strict";
        t.d(e, { ji: () => r });
        const r = {
          unlockSubscriptionBonusDuration: 2e3,
          unlockBonusQuestDelay: 3e3,
          unlockBonusQuestDuration: 500,
          unlockTabPremiumDuration: 700,
        };
      },
      9153: (u, e, t) => {
        "use strict";
        let r;
        (t.d(e, { g: () => r }),
          (function (u) {
            ((u[(u.DailyQuests = 0)] = "DailyQuests"),
              (u[(u.PremiumQuests = 1)] = "PremiumQuests"));
          })(r || (r = {})));
      },
      3099: (u, e, t) => {
        "use strict";
        let r;
        (t.d(e, { N: () => r }),
          (function (u) {
            ((u.Done = "done"),
              (u.UndoneSubscription = "undoneSubscription"),
              (u.Locked = "notAvailable"),
              (u.Active = ""));
          })(r || (r = {})));
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
      5287: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        const r = { base: "FormatText_base_d0" };
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
        var E = 1 / 0;
        for (i = 0; i < deferred.length; i++) {
          for (var [e, t, r] = deferred[i], a = !0, A = 0; A < e.length; A++)
            (!1 & r || E >= r) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[A]))
              ? e.splice(A--, 1)
              : ((a = !1), r < E && (E = r));
          if (a) {
            deferred.splice(i--, 1);
            var n = t();
            void 0 !== n && (u = n);
          }
        }
        return u;
      }
      r = r || 0;
      for (var i = deferred.length; i > 0 && deferred[i - 1][2] > r; i--)
        deferred[i] = deferred[i - 1];
      deferred[i] = [e, t, r];
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
    (__webpack_require__.j = 83),
    (() => {
      var u = { 83: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var r,
            E,
            [a, A, n] = t,
            i = 0;
          if (a.some((e) => 0 !== u[e])) {
            for (r in A) __webpack_require__.o(A, r) && (__webpack_require__.m[r] = A[r]);
            if (n) var F = n(__webpack_require__);
          }
          for (e && e(t); i < a.length; i++)
            ((E = a[i]), __webpack_require__.o(u, E) && u[E] && u[E][0](), (u[E] = 0));
          return __webpack_require__.O(F);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [272], () => __webpack_require__(2603));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
