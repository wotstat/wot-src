(() => {
  var __webpack_modules__ = {
      3779: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => d });
        var a = t(6483),
          n = t.n(a),
          r = t(9887),
          i = t.n(r),
          s = t(3377),
          l = t(6179),
          o = t.n(l),
          E = t(5026);
        const A = [
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
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (u[a] = t[a]);
                }
                return u;
              }),
            _.apply(this, arguments)
          );
        }
        Object.keys(i());
        const F = {
            XL: { mt: E.Z.mt__XL, mr: E.Z.mr__XL, mb: E.Z.mb__XL, ml: E.Z.ml__XL },
            LG: { mt: E.Z.mt__LG, mr: E.Z.mr__LG, mb: E.Z.mb__LG, ml: E.Z.ml__LG },
            MDp: { mt: E.Z.mt__MDp, mr: E.Z.mr__MDp, mb: E.Z.mb__MDp, ml: E.Z.ml__MDp },
            MD: { mt: E.Z.mt__MD, mr: E.Z.mr__MD, mb: E.Z.mb__MD, ml: E.Z.ml__MD },
            SMp: { mt: E.Z.mt__SMp, mr: E.Z.mr__SMp, mb: E.Z.mb__SMp, ml: E.Z.ml__SMp },
            SM: { mt: E.Z.mt__SM, mr: E.Z.mr__SM, mb: E.Z.mb__SM, ml: E.Z.ml__SM },
            XS: { mt: E.Z.mt__XS, mr: E.Z.mr__XS, mb: E.Z.mb__XS, ml: E.Z.ml__XS },
          },
          c = (Object.keys(F), ["mt", "mr", "mb", "ml"]),
          D = { mt: "marginTop", mr: "marginRight", mb: "marginBottom", ml: "marginLeft" },
          d = (0, s.ZP)((u) => {
            let e = u.className,
              t = u.width,
              a = u.height,
              r = u.m,
              i = u.mt,
              s = void 0 === i ? r : i,
              d = u.mr,
              m = void 0 === d ? r : d,
              B = u.mb,
              C = void 0 === B ? r : B,
              h = u.ml,
              g = void 0 === h ? r : h,
              v = u.column,
              p = u.row,
              b = u.flexDirection,
              f = void 0 === b ? (v ? "column" : p && "row") || void 0 : b,
              x = u.flexStart,
              w = u.center,
              L = u.flexEnd,
              T = u.spaceBetween,
              M = u.spaceAround,
              S = u.justifyContent,
              y =
                void 0 === S
                  ? (x ? "flex-start" : w && "center") ||
                    (L && "flex-end") ||
                    (T && "space-between") ||
                    (M && "space-around") ||
                    void 0
                  : S,
              O = u.alignItems,
              R =
                void 0 === O
                  ? (x ? "flex-start" : w && "center") || (L && "flex-end") || void 0
                  : O,
              P = u.alignSelf,
              k = u.wrap,
              N = u.flexWrap,
              I = void 0 === N ? (k ? "wrap" : void 0) : N,
              H = u.grow,
              G = u.shrink,
              W = u.flex,
              U = void 0 === W ? (H || G ? `${H ? 1 : 0} ${G ? 1 : 0} auto` : void 0) : W,
              j = u.style,
              V = u.children,
              X = (function (u, e) {
                if (null == u) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(u);
                for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, A);
            const Z = (0, l.useMemo)(() => {
                const u = { mt: s, mr: m, mb: C, ml: g },
                  e = ((u) =>
                    c.reduce((e, t) => {
                      const a = u[t];
                      return a && "number" != typeof a ? e.concat(F[!0 === a ? "MD" : a][t]) : e;
                    }, []))(u),
                  n = ((u) =>
                    c.reduce((e, t) => {
                      const a = u[t];
                      return ("number" == typeof a && (e[D[t]] = a + "rem"), e);
                    }, {}))(u);
                return {
                  computedStyle: Object.assign({}, j, n, {
                    width: void 0 !== t && "number" == typeof t ? t + "rem" : t,
                    height: void 0 !== a && "number" == typeof a ? a + "rem" : a,
                    flex: U,
                    alignSelf: P,
                    display: f || R ? "flex" : void 0,
                    flexDirection: f,
                    flexWrap: I,
                    justifyContent: y,
                    alignItems: R,
                  }),
                  computedClassNames: e,
                };
              }, [t, a, s, m, C, g, j, U, P, f, I, y, R]),
              $ = Z.computedStyle,
              Y = Z.computedClassNames;
            return o().createElement(
              "div",
              _({ className: n()(E.Z.base, ...Y, e), style: $ }, X),
              V,
            );
          });
      },
      280: (u, e, t) => {
        "use strict";
        t.d(e, { z: () => o });
        var a = t(6179),
          n = t.n(a),
          r = t(6483),
          i = t.n(r),
          s = t(3649),
          l = t(5287);
        const o = ({ binding: u, text: e = "", classMix: t, alignment: r = s.v2.left }) =>
          null === e
            ? (console.error("FormatText was supplied with 'null'"), null)
            : n().createElement(
                a.Fragment,
                null,
                e.split("\n").map((e, o) =>
                  n().createElement(
                    "div",
                    { className: i()(l.Z.base, t), key: `${e}-${o}` },
                    (0, s.Uw)(e, r, u).map((u, e) =>
                      n().createElement(a.Fragment, { key: `${e}-${u}` }, u),
                    ),
                  ),
                ),
              );
      },
      3495: (u, e, t) => {
        "use strict";
        t.d(e, { Y: () => A });
        var a = t(3138),
          n = t(6179),
          r = t(1043),
          i = t(5262);
        const s = a.O.client.getSize("rem"),
          l = s.width,
          o = s.height,
          E = Object.assign({ width: l, height: o }, (0, i.T)(l, o, r.j)),
          A = (0, n.createContext)(E);
      },
      1039: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => E });
        var a = t(6179),
          n = t.n(a),
          r = t(6536),
          i = t(3495),
          s = t(1043),
          l = t(5262),
          o = t(3138);
        const E = (0, a.memo)(({ children: u }) => {
          const e = (0, a.useContext)(i.Y),
            t = (0, a.useState)(e),
            E = t[0],
            A = t[1],
            _ = (0, a.useCallback)((u, e) => {
              const t = o.O.view.pxToRem(u),
                a = o.O.view.pxToRem(e);
              A(Object.assign({ width: t, height: a }, (0, l.T)(t, a, s.j)));
            }, []);
          ((0, r.Z)(() => {
            engine.on("clientResized", _);
          }),
            (0, a.useEffect)(() => () => engine.off("clientResized", _), [_]));
          const F = (0, a.useMemo)(() => Object.assign({}, E), [E]);
          return n().createElement(i.Y.Provider, { value: F }, u);
        });
      },
      6010: (u, e, t) => {
        "use strict";
        var a = t(6179),
          n = t(7382),
          r = t(3495);
        const i = ["children"];
        const s = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                a,
                n = {},
                r = Object.keys(u);
              for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, i);
          const s = (0, a.useContext)(r.Y),
            l = s.extraLarge,
            o = s.large,
            E = s.medium,
            A = s.small,
            _ = s.extraSmall,
            F = s.extraLargeWidth,
            c = s.largeWidth,
            D = s.mediumWidth,
            d = s.smallWidth,
            m = s.extraSmallWidth,
            B = s.extraLargeHeight,
            C = s.largeHeight,
            h = s.mediumHeight,
            g = s.smallHeight,
            v = s.extraSmallHeight,
            p = { extraLarge: B, large: C, medium: h, small: g, extraSmall: v };
          if (t.extraLarge || t.large || t.medium || t.small || t.extraSmall) {
            if (t.extraLarge && l) return e;
            if (t.large && o) return e;
            if (t.medium && E) return e;
            if (t.small && A) return e;
            if (t.extraSmall && _) return e;
          } else {
            if (t.extraLargeWidth && F) return (0, n.H)(e, t, p);
            if (t.largeWidth && c) return (0, n.H)(e, t, p);
            if (t.mediumWidth && D) return (0, n.H)(e, t, p);
            if (t.smallWidth && d) return (0, n.H)(e, t, p);
            if (t.extraSmallWidth && m) return (0, n.H)(e, t, p);
            if (!(
              t.extraLargeWidth ||
              t.largeWidth ||
              t.mediumWidth ||
              t.smallWidth ||
              t.extraSmallWidth
            )) {
              if (t.extraLargeHeight && B) return e;
              if (t.largeHeight && C) return e;
              if (t.mediumHeight && h) return e;
              if (t.smallHeight && g) return e;
              if (t.extraSmallHeight && v) return e;
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
        (0, a.memo)(s);
      },
      7382: (u, e, t) => {
        "use strict";
        t.d(e, { H: () => a });
        const a = (u, e, t) =>
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
        t.d(e, { YN: () => n.Y, ZN: () => a.Z });
        t(6010);
        var a = t(1039),
          n = t(3495);
      },
      1043: (u, e, t) => {
        "use strict";
        t.d(e, { j: () => a });
        const a = {
          extraLarge: { weight: 4, width: 2560, height: 1440 },
          large: { weight: 3, width: 1920, height: 1080 },
          medium: { weight: 2, width: 1600, height: 900 },
          small: { weight: 1, width: 1366, height: 768 },
          extraSmall: { weight: 0, width: 1024, height: 768 },
        };
      },
      5262: (u, e, t) => {
        "use strict";
        var a;
        function n(u, e, t) {
          const a = (function (u, e) {
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
            r = Math.min(a, n);
          return {
            extraLarge: r === t.extraLarge.weight,
            large: r === t.large.weight,
            medium: r === t.medium.weight,
            small: r === t.small.weight,
            extraSmall: r === t.extraSmall.weight,
            extraLargeWidth: a === t.extraLarge.weight,
            largeWidth: a === t.large.weight,
            mediumWidth: a === t.medium.weight,
            smallWidth: a === t.small.weight,
            extraSmallWidth: a === t.extraSmall.weight,
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
          })(a || (a = {})));
      },
      7613: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => b });
        var a = t(6483),
          n = t.n(a),
          r = t(3779),
          i = t(280),
          s = t(3532),
          l = t.n(s),
          o = t(9887),
          E = t.n(o),
          A = t(3377),
          _ = t(6179),
          F = t.n(_),
          c = t(3393);
        const D = [
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
        function d() {
          return (
            (d =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (u[a] = t[a]);
                }
                return u;
              }),
            d.apply(this, arguments)
          );
        }
        Object.keys(E());
        const m = Object.keys(l()),
          B = { mt: "MD", mr: "SM", mb: "SM", ml: "SM" },
          C = { mt: "SM", mr: "XS", mb: "XS", ml: "XS" },
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
          v =
            (Object.keys(g),
            {
              "heading-H144": { mt: "XL", mr: "LG", mb: "LG", ml: "LG" },
              "heading-H73": { mt: "LG", mr: "MD", mb: "MD", ml: "MD" },
              "heading-H56": B,
              "heading-H36": B,
              "heading-H28": C,
              "heading-H24": C,
              "heading-H24R": C,
              "heading-H22": C,
              "heading-H20R": C,
              "heading-H18": C,
              "heading-H15": h,
              "heading-H14": h,
              "paragraph-P24": C,
              "paragraph-P18": C,
              "paragraph-P16": C,
              "paragraph-P14": h,
              "paragraph-P12": h,
              "paragraph-P10": h,
            }),
          p =
            (Object.keys(v),
            (u) =>
              u
                ? ((u) => m.includes(u))(u)
                  ? { colorClassName: c.Z[u] }
                  : { colorStyle: { color: u } }
                : {}),
          b = (0, A.ZP)((u) => {
            let e = u.text,
              t = u.variant,
              a = u.className,
              s = u.color,
              l = u.m,
              o = u.mt,
              E = void 0 === o ? l : o,
              A = u.mr,
              m = void 0 === A ? l : A,
              B = u.mb,
              C = void 0 === B ? l : B,
              h = u.ml,
              g = void 0 === h ? l : h,
              b = u.style,
              f = u.format,
              x = (function (u, e) {
                if (null == u) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(u);
                for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, D);
            const w = (0, _.useMemo)(() => {
                const u = p(s),
                  e = u.colorClassName,
                  t = u.colorStyle,
                  a = void 0 === t ? {} : t;
                return { computedStyle: Object.assign({}, b, a), colorClassName: e };
              }, [b, s]),
              L = w.computedStyle,
              T = w.colorClassName;
            return F().createElement(
              r.ZP,
              d(
                {
                  className: n()(c.Z.base, t && c.Z[t], T, a),
                  style: L,
                  mt: !0 === E ? v[t || "paragraph-P16"].mt : E,
                  mr: !0 === m ? v[t || "paragraph-P16"].mr : m,
                  mb: !0 === C ? v[t || "paragraph-P16"].mb : C,
                  ml: !0 === g ? v[t || "paragraph-P16"].ml : g,
                },
                x,
              ),
              void 0 !== f ? F().createElement(i.z, d({}, f, { text: e })) : e,
            );
          });
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
      527: (u, e, t) => {
        "use strict";
        (t.r(e), t.d(e, { mouse: () => s, onResize: () => r }));
        var a = t(2472),
          n = t(1176);
        const r = (0, a.E)("clientResized"),
          i = { down: (0, a.E)("mousedown"), up: (0, a.E)("mouseup"), move: (0, a.E)("mousemove") };
        const s = (function () {
          const u = { listeners: 0, enabled: !0, initialized: !1 };
          function e() {
            u.enabled && (0, n.R)(!1);
          }
          function t() {
            u.enabled && (0, n.R)(!0);
          }
          function a() {
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
          const r = ["down", "up", "move"].reduce(
            (e, t) => (
              (e[t] = (function (e) {
                return (t) => {
                  u.listeners += 1;
                  let n = !0;
                  const r = `mouse${e}`,
                    s = i[e]((u) => t([u, "outside"]));
                  function l(u) {
                    t([u, "inside"]);
                  }
                  return (
                    window.addEventListener(r, l),
                    a(),
                    () => {
                      n &&
                        (s(), window.removeEventListener(r, l), (u.listeners -= 1), a(), (n = !1));
                    }
                  );
                };
              })(t)),
              e
            ),
            {},
          );
          return Object.assign({}, r, {
            disable() {
              ((u.enabled = !1), a());
            },
            enable() {
              ((u.enabled = !0), a());
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
            events: () => a,
            getMouseGlobalPosition: () => r,
            getSize: () => n,
            graphicsQuality: () => i,
          }));
        var a = t(527);
        function n(u = "px") {
          return "rem" === u ? viewEnv.getClientSizeRem() : viewEnv.getClientSizePx();
        }
        function r(u = "px") {
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
        function a(u) {
          viewEnv.setTrackMouseOnStage(u);
        }
        t.d(e, { R: () => a });
      },
      2472: (u, e, t) => {
        "use strict";
        function a(u) {
          return (e) => (
            engine.on(u, e),
            () => {
              engine.off(u, e);
            }
          );
        }
        t.d(e, { E: () => a });
      },
      3138: (u, e, t) => {
        "use strict";
        t.d(e, { O: () => n });
        var a = t(5959);
        const n = { view: t(7641), client: a };
      },
      3722: (u, e, t) => {
        "use strict";
        function a(u, e, t = 1) {
          return viewEnv.getChildTexturePath(u, e.width, e.height, t);
        }
        function n(u, e, t) {
          return `url(${a(u, e, t)})`;
        }
        (t.r(e), t.d(e, { getBgUrl: () => n, getTextureUrl: () => a }));
      },
      6112: (u, e, t) => {
        "use strict";
        t.d(e, { W: () => a });
        const a = { showing: 0, shown: 1, hiding: 2, hidden: 3 };
      },
      6538: (u, e, t) => {
        "use strict";
        t.d(e, { U: () => n });
        var a = t(2472);
        const n = {
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
      7641: (u, e, t) => {
        "use strict";
        (t.r(e),
          t.d(e, {
            addModelObserver: () => E,
            addPreloadTexture: () => s,
            children: () => a,
            displayStatus: () => n.W,
            displayStatusIs: () => x,
            events: () => r.U,
            extraSize: () => w,
            forceTriggerMouseMove: () => b,
            freezeTextureBeforeResize: () => D,
            getBrowserTexturePath: () => o,
            getDisplayStatus: () => f,
            getScale: () => d,
            getSize: () => _,
            getViewGlobalPosition: () => c,
            isClientAccessible: () => g,
            isEventHandled: () => p,
            isFocused: () => h,
            pxToRem: () => m,
            remToPx: () => B,
            resize: () => F,
            sendEvent: () => i.qP,
            setAnimateWindow: () => C,
            setEventHandled: () => v,
            setInputPaddingsRem: () => l,
            setSidePaddingsRem: () => A,
            whenTutorialReady: () => L,
          }));
        var a = t(3722),
          n = t(6112),
          r = t(6538),
          i = t(8566);
        function s(u) {
          viewEnv.addPreloadTexture(u);
        }
        function l(u) {
          viewEnv.setHitAreaPaddingsRem(u, u, u, u, 15);
        }
        function o(u, e, t, a = 1) {
          return viewEnv.getWebBrowserTexturePath(u, e, t, a);
        }
        function E(u, e, t) {
          return viewEnv.addDataChangedCallback(u, e, t);
        }
        function A(u) {
          viewEnv.setHitAreaPaddingsRem(u.top, u.right, u.bottom, u.left, 15);
        }
        function _(u = "px") {
          return "rem" === u ? viewEnv.getViewSizeRem() : viewEnv.getViewSizePx();
        }
        function F(u, e, t = "px") {
          return "rem" === t ? viewEnv.resizeViewRem(u, e) : viewEnv.resizeViewPx(u, e);
        }
        function c(u = "rem") {
          const e = viewEnv.getViewGlobalPositionRem();
          return "rem" === u ? e : { x: B(e.x), y: B(e.y) };
        }
        function D() {
          viewEnv.freezeTextureBeforeResize();
        }
        function d() {
          return viewEnv.getScale();
        }
        function m(u) {
          return viewEnv.pxToRem(u);
        }
        function B(u) {
          return viewEnv.remToPx(u);
        }
        function C(u, e) {
          viewEnv.setAnimateWindow(u, e);
        }
        function h() {
          return viewEnv.isFocused();
        }
        function g() {
          return viewEnv.isClientAccessible();
        }
        function v() {
          return viewEnv.setEventHandled();
        }
        function p() {
          return viewEnv.isEventHandled();
        }
        function b() {
          viewEnv.forceTriggerMouseMove();
        }
        function f() {
          return viewEnv.getShowingStatus();
        }
        const x = Object.keys(n.W).reduce(
            (u, e) => ((u[e] = () => viewEnv.getShowingStatus() === n.W[e]), u),
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
          L = Promise.all([
            new Promise((u) => {
              window.isDomBuilt ? u() : r.U.onDomBuilt(u);
            }),
            engine.whenReady,
          ]);
      },
      8566: (u, e, t) => {
        "use strict";
        t.d(e, { qP: () => o });
        const a = ["args"];
        const n = 2,
          r = 16,
          i = 32,
          s = 64,
          l = (u, e) => {
            const t = "GFViewEventProxy";
            if (void 0 !== e) {
              const r = e.args,
                i = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    a,
                    n = {},
                    r = Object.keys(u);
                  for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                  return n;
                })(e, a);
              return void 0 !== r
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, i, {
                      arguments:
                        ((n = r),
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
              l("popover" === u ? n : i);
            },
            minimize() {
              l(s);
            },
            move(u) {
              l(r, { isMouseEvent: !0, on: u });
            },
          };
      },
      3377: (u, e, t) => {
        "use strict";
        t.d(e, { ZP: () => E });
        var a = t(5415),
          n = t(6179),
          r = t.n(n);
        const i = ["xl", "lg", "md", "sm", "xs"],
          s = (u) => u.includes("_") && ((u) => i.includes(u))(u.split("_").at(-1)),
          l = [a.cJ.ExtraLarge, a.cJ.Large, a.cJ.Medium, a.cJ.Small, a.cJ.ExtraSmall],
          o = (u, e) =>
            Object.keys(u).reduce((t, a) => {
              if (a in t) return t;
              if (s(a)) {
                const n = a.split("_").slice(0, -1).join("_");
                if (n in t) return t;
                const r = l.indexOf(e),
                  s = (-1 !== r ? i.slice(r) : [])
                    .map((u) => n + "_" + u)
                    .find((e) => void 0 !== u[e]),
                  o = s ? u[s] : void 0;
                return ((t[n] = void 0 !== o ? o : u[n]), t);
              }
              const n = u[a];
              return (
                void 0 === n ||
                  ((u, e) => i.some((t) => void 0 !== e[`${u}_${t}`]))(a, u) ||
                  (t[a] = n),
                t
              );
            }, {}),
          E = (u, e = o) => {
            const t = (
              (u, e = o) =>
              (t) => {
                const i = (0, a.GS)().mediaSize,
                  s = (0, n.useMemo)(() => e(t, i), [t, i]);
                return r().createElement(u, s);
              }
            )(u, e);
            return r().memo((e) =>
              Object.keys(e).some((u) => s(u) && void 0 !== e[u])
                ? r().createElement(t, e)
                : r().createElement(u, e),
            );
          };
      },
      6536: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => n });
        var a = t(6179);
        const n = (u) => {
          const e = (0, a.useRef)(!1);
          e.current || (u(), (e.current = !0));
        };
      },
      5415: (u, e, t) => {
        "use strict";
        t.d(e, { Aq: () => l, GS: () => o, cJ: () => i, fd: () => s });
        var a = t(6179),
          n = t(7739),
          r = t(1043);
        let i, s, l;
        (!(function (u) {
          ((u[(u.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
            (u[(u.Small = r.j.small.width)] = "Small"),
            (u[(u.Medium = r.j.medium.width)] = "Medium"),
            (u[(u.Large = r.j.large.width)] = "Large"),
            (u[(u.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
        })(i || (i = {})),
          (function (u) {
            ((u[(u.ExtraSmall = r.j.extraSmall.width)] = "ExtraSmall"),
              (u[(u.Small = r.j.small.width)] = "Small"),
              (u[(u.Medium = r.j.medium.width)] = "Medium"),
              (u[(u.Large = r.j.large.width)] = "Large"),
              (u[(u.ExtraLarge = r.j.extraLarge.width)] = "ExtraLarge"));
          })(s || (s = {})),
          (function (u) {
            ((u[(u.ExtraSmall = r.j.extraSmall.height)] = "ExtraSmall"),
              (u[(u.Small = r.j.small.height)] = "Small"),
              (u[(u.Medium = r.j.medium.height)] = "Medium"),
              (u[(u.Large = r.j.large.height)] = "Large"),
              (u[(u.ExtraLarge = r.j.extraLarge.height)] = "ExtraLarge"));
          })(l || (l = {})));
        const o = () => {
          const u = (0, a.useContext)(n.YN),
            e = u.width,
            t = u.height,
            r = ((u) => {
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
                  return s.ExtraLarge;
                case u.largeWidth:
                  return s.Large;
                case u.mediumWidth:
                  return s.Medium;
                case u.smallWidth:
                  return s.Small;
                case u.extraSmallWidth:
                  return s.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), s.ExtraSmall);
              }
            })(u),
            E = ((u) => {
              switch (!0) {
                case u.extraLargeHeight:
                  return l.ExtraLarge;
                case u.largeHeight:
                  return l.Large;
                case u.mediumHeight:
                  return l.Medium;
                case u.smallHeight:
                  return l.Small;
                case u.extraSmallHeight:
                  return l.ExtraSmall;
                default:
                  return (console.error("Unreachable media context resolution"), l.ExtraSmall);
              }
            })(u);
          return {
            mediaSize: r,
            mediaWidth: o,
            mediaHeight: E,
            remScreenWidth: e,
            remScreenHeight: t,
          };
        };
      },
      5521: (u, e, t) => {
        "use strict";
        let a, n;
        (t.d(e, { n: () => a }),
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
          })(a || (a = {})),
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
        function a(u, e) {
          var t;
          if (!(e >= u.length))
            return Array.isArray(u) ? u[e] : null == (t = u[e]) ? void 0 : t.value;
        }
        t.d(e, { U2: () => a, UI: () => n });
        function n(u, e) {
          return Array.isArray(u)
            ? u.map(e)
            : u.map((u, t, a) => e(null == u ? void 0 : u.value, t, a));
        }
      },
      3649: (u, e, t) => {
        "use strict";
        let a;
        function n(u, e) {
          return u.replace(/(\{|%\()\w+(\}|\)s)/g, (u) => {
            const t = 0 === u.indexOf("%") ? 2 : 1;
            return String(e[u.slice(t, -t)]);
          });
        }
        (t.d(e, { Uw: () => A, uF: () => n, v2: () => a }),
          (function (u) {
            ((u[(u.left = 0)] = "left"), (u[(u.right = 1)] = "right"));
          })(a || (a = {})));
        const r = (u, e, t) => {
            if (t % 2) {
              const t = u.pop();
              return [...u, t + e];
            }
            return [...u, e];
          },
          i = (u, e, t) => {
            if (0 === t) return [e];
            if (t % 2) return [...u, " " === e ? " " : e];
            {
              const t = u.pop();
              return [...u, t + e];
            }
          },
          s = (u, e, t = a.left) => u.split(e).reduce(t === a.left ? r : i, []),
          l = (() => {
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
          o = ["zh_cn", "zh_sg", "zh_tw"],
          E = (u, e = a.left) => {
            const t = R.strings.settings.LANGUAGE_CODE().toLowerCase();
            return o.includes(t)
              ? l(u)
              : ((u, e = a.left) => {
                  let t = [];
                  const n =
                      /(?<=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])(\x2D)(?=[a-z\xB5\xDF-\xF6\xF8-\xFF\u0101\u0103\u0105\u0107\u0109\u010B\u010D\u010F\u0111\u0113\u0115\u0117\u0119\u011B\u011D\u011F\u0121\u0123\u0125\u0127\u0129\u012B\u012D\u012F\u0131\u0133\u0135\u0137\u0138\u013A\u013C\u013E\u0140\u0142\u0144\u0146\u0148\u0149\u014B\u014D\u014F\u0151\u0153\u0155\u0157\u0159\u015B\u015D\u015F\u0161\u0163\u0165\u0167\u0169\u016B\u016D\u016F\u0171\u0173\u0175\u0177\u017A\u017C\u017E-\u0180\u0183\u0185\u0188\u018C\u018D\u0192\u0195\u0199-\u019B\u019E\u01A1\u01A3\u01A5\u01A8\u01AA\u01AB\u01AD\u01B0\u01B4\u01B6\u01B9\u01BA\u01BD-\u01BF\u01C6\u01C9\u01CC\u01CE\u01D0\u01D2\u01D4\u01D6\u01D8\u01DA\u01DC\u01DD\u01DF\u01E1\u01E3\u01E5\u01E7\u01E9\u01EB\u01ED\u01EF\u01F0\u01F3\u01F5\u01F9\u01FB\u01FD\u01FF\u0201\u0203\u0205\u0207\u0209\u020B\u020D\u020F\u0211\u0213\u0215\u0217\u0219\u021B\u021D\u021F\u0221\u0223\u0225\u0227\u0229\u022B\u022D\u022F\u0231\u0233-\u0239\u023C\u023F\u0240\u0242\u0247\u0249\u024B\u024D\u024F-\u0293\u0295-\u02AF\u0371\u0373\u0377\u037B-\u037D\u0390\u03AC-\u03CE\u03D0\u03D1\u03D5-\u03D7\u03D9\u03DB\u03DD\u03DF\u03E1\u03E3\u03E5\u03E7\u03E9\u03EB\u03ED\u03EF-\u03F3\u03F5\u03F8\u03FB\u03FC\u0430-\u045F\u0461\u0463\u0465\u0467\u0469\u046B\u046D\u046F\u0471\u0473\u0475\u0477\u0479\u047B\u047D\u047F\u0481\u048B\u048D\u048F\u0491\u0493\u0495\u0497\u0499\u049B\u049D\u049F\u04A1\u04A3\u04A5\u04A7\u04A9\u04AB\u04AD\u04AF\u04B1\u04B3\u04B5\u04B7\u04B9\u04BB\u04BD\u04BF\u04C2\u04C4\u04C6\u04C8\u04CA\u04CC\u04CE\u04CF\u04D1\u04D3\u04D5\u04D7\u04D9\u04DB\u04DD\u04DF\u04E1\u04E3\u04E5\u04E7\u04E9\u04EB\u04ED\u04EF\u04F1\u04F3\u04F5\u04F7\u04F9\u04FB\u04FD\u04FF\u0501\u0503\u0505\u0507\u0509\u050B\u050D\u050F\u0511\u0513\u0515\u0517\u0519\u051B\u051D\u051F\u0521\u0523\u0525\u0527\u0529\u052B\u052D\u052F\u0560-\u0588\u10D0-\u10FA\u10FD-\u10FF\u13F8-\u13FD\u1C80-\u1C88\u1D00-\u1D2B\u1D6B-\u1D77\u1D79-\u1D9A\u1E01\u1E03\u1E05\u1E07\u1E09\u1E0B\u1E0D\u1E0F\u1E11\u1E13\u1E15\u1E17\u1E19\u1E1B\u1E1D\u1E1F\u1E21\u1E23\u1E25\u1E27\u1E29\u1E2B\u1E2D\u1E2F\u1E31\u1E33\u1E35\u1E37\u1E39\u1E3B\u1E3D\u1E3F\u1E41\u1E43\u1E45\u1E47\u1E49\u1E4B\u1E4D\u1E4F\u1E51\u1E53\u1E55\u1E57\u1E59\u1E5B\u1E5D\u1E5F\u1E61\u1E63\u1E65\u1E67\u1E69\u1E6B\u1E6D\u1E6F\u1E71\u1E73\u1E75\u1E77\u1E79\u1E7B\u1E7D\u1E7F\u1E81\u1E83\u1E85\u1E87\u1E89\u1E8B\u1E8D\u1E8F\u1E91\u1E93\u1E95-\u1E9D\u1E9F\u1EA1\u1EA3\u1EA5\u1EA7\u1EA9\u1EAB\u1EAD\u1EAF\u1EB1\u1EB3\u1EB5\u1EB7\u1EB9\u1EBB\u1EBD\u1EBF\u1EC1\u1EC3\u1EC5\u1EC7\u1EC9\u1ECB\u1ECD\u1ECF\u1ED1\u1ED3\u1ED5\u1ED7\u1ED9\u1EDB\u1EDD\u1EDF\u1EE1\u1EE3\u1EE5\u1EE7\u1EE9\u1EEB\u1EED\u1EEF\u1EF1\u1EF3\u1EF5\u1EF7\u1EF9\u1EFB\u1EFD\u1EFF-\u1F07\u1F10-\u1F15\u1F20-\u1F27\u1F30-\u1F37\u1F40-\u1F45\u1F50-\u1F57\u1F60-\u1F67\u1F70-\u1F7D\u1F80-\u1F87\u1F90-\u1F97\u1FA0-\u1FA7\u1FB0-\u1FB4\u1FB6\u1FB7\u1FBE\u1FC2-\u1FC4\u1FC6\u1FC7\u1FD0-\u1FD3\u1FD6\u1FD7\u1FE0-\u1FE7\u1FF2-\u1FF4\u1FF6\u1FF7\u210A\u210E\u210F\u2113\u212F\u2134\u2139\u213C\u213D\u2146-\u2149\u214E\u2184\u2C30-\u2C5F\u2C61\u2C65\u2C66\u2C68\u2C6A\u2C6C\u2C71\u2C73\u2C74\u2C76-\u2C7B\u2C81\u2C83\u2C85\u2C87\u2C89\u2C8B\u2C8D\u2C8F\u2C91\u2C93\u2C95\u2C97\u2C99\u2C9B\u2C9D\u2C9F\u2CA1\u2CA3\u2CA5\u2CA7\u2CA9\u2CAB\u2CAD\u2CAF\u2CB1\u2CB3\u2CB5\u2CB7\u2CB9\u2CBB\u2CBD\u2CBF\u2CC1\u2CC3\u2CC5\u2CC7\u2CC9\u2CCB\u2CCD\u2CCF\u2CD1\u2CD3\u2CD5\u2CD7\u2CD9\u2CDB\u2CDD\u2CDF\u2CE1\u2CE3\u2CE4\u2CEC\u2CEE\u2CF3\u2D00-\u2D25\u2D27\u2D2D\uA641\uA643\uA645\uA647\uA649\uA64B\uA64D\uA64F\uA651\uA653\uA655\uA657\uA659\uA65B\uA65D\uA65F\uA661\uA663\uA665\uA667\uA669\uA66B\uA66D\uA681\uA683\uA685\uA687\uA689\uA68B\uA68D\uA68F\uA691\uA693\uA695\uA697\uA699\uA69B\uA723\uA725\uA727\uA729\uA72B\uA72D\uA72F-\uA731\uA733\uA735\uA737\uA739\uA73B\uA73D\uA73F\uA741\uA743\uA745\uA747\uA749\uA74B\uA74D\uA74F\uA751\uA753\uA755\uA757\uA759\uA75B\uA75D\uA75F\uA761\uA763\uA765\uA767\uA769\uA76B\uA76D\uA76F\uA771-\uA778\uA77A\uA77C\uA77F\uA781\uA783\uA785\uA787\uA78C\uA78E\uA791\uA793-\uA795\uA797\uA799\uA79B\uA79D\uA79F\uA7A1\uA7A3\uA7A5\uA7A7\uA7A9\uA7AF\uA7B5\uA7B7\uA7B9\uA7BB\uA7BD\uA7BF\uA7C1\uA7C3\uA7C8\uA7CA\uA7D1\uA7D3\uA7D5\uA7D7\uA7D9\uA7F6\uA7FA\uAB30-\uAB5A\uAB60-\uAB68\uAB70-\uABBF\uFB00-\uFB06\uFB13-\uFB17\uFF41-\uFF5A\u{10428}-\u{1044F}\u{104D8}-\u{104FB}\u{10597}-\u{105A1}\u{105A3}-\u{105B1}\u{105B3}-\u{105B9}\u{105BB}\u{105BC}\u{10CC0}-\u{10CF2}\u{118C0}-\u{118DF}\u{16E60}-\u{16E7F}\u{1D41A}-\u{1D433}\u{1D44E}-\u{1D454}\u{1D456}-\u{1D467}\u{1D482}-\u{1D49B}\u{1D4B6}-\u{1D4B9}\u{1D4BB}\u{1D4BD}-\u{1D4C3}\u{1D4C5}-\u{1D4CF}\u{1D4EA}-\u{1D503}\u{1D51E}-\u{1D537}\u{1D552}-\u{1D56B}\u{1D586}-\u{1D59F}\u{1D5BA}-\u{1D5D3}\u{1D5EE}-\u{1D607}\u{1D622}-\u{1D63B}\u{1D656}-\u{1D66F}\u{1D68A}-\u{1D6A5}\u{1D6C2}-\u{1D6DA}\u{1D6DC}-\u{1D6E1}\u{1D6FC}-\u{1D714}\u{1D716}-\u{1D71B}\u{1D736}-\u{1D74E}\u{1D750}-\u{1D755}\u{1D770}-\u{1D788}\u{1D78A}-\u{1D78F}\u{1D7AA}-\u{1D7C2}\u{1D7C4}-\u{1D7C9}\u{1D7CB}\u{1DF00}-\u{1DF09}\u{1DF0B}-\u{1DF1E}\u{1E922}-\u{1E943}])/gu,
                    r = u.replace(/&nbsp;/g, " ");
                  return (s(r, /( )/, e).forEach((u) => (t = t.concat(s(u, n, a.left)))), t);
                })(u, e);
          },
          A = (u, e, t) =>
            u.split(/%\((.*?)\)(?:[sd])?/g).map((u) => (t && u in t ? t[u] : E(u, e)));
      },
      1358: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => r });
        var a = t(3138);
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
            const r = a.O.view.addModelObserver(u, t, n);
            return (
              r > 0
                ? ((this._callbacks[r] = e),
                  t > 0 && (this._views[t] ? this._views[t].push(r) : (this._views[t] = [r])))
                : console.error("Can't add callback for model:", u),
              r
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
              const a = this._callbacks[t];
              void 0 !== a && a(u, e);
            });
          }
        }
        n.__instance = void 0;
        const r = n;
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
        t.d(e, { B0: () => l, ry: () => B, Sy: () => h });
        class a {
          constructor() {
            ((this.entries = []),
              (this._listenMouse = !1),
              (this.onMouseDown = (u) => {
                this.entries.forEach(({ container: e, callback: t }) => {
                  let a = u.target;
                  do {
                    if (a === e) return;
                    a = a.parentNode;
                  } while (a);
                  t();
                });
              }));
          }
          static get instance() {
            return (a.__instance || (a.__instance = new a()), a.__instance);
          }
          register(u, e) {
            (this.addMouseListener(), this.entries.push({ container: u, callback: e }));
          }
          unregister(u, e) {
            const t = u,
              a = e;
            ((this.entries = this.entries.filter(
              ({ container: u, callback: e }) => u !== t || e !== a,
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
        const n = a;
        var r = t(1358);
        const i = {
            getNumberFormat: (u, e) => systemLocale.getNumberFormat(u, e),
            getRealFormat: (u, e) => systemLocale.getRealFormat(u, e),
            getTimeFormat: (u, e) => systemLocale.getTimeFormat(u, e),
            getDateFormat: (u, e) => systemLocale.getDateFormat(u, e),
            toUpperCase: (u) => systemLocale.toUpperCase(u),
            toLowerCase: (u) => systemLocale.toUpperCase(u),
          },
          s = {
            getNumberFormat: (u) => userLocale.getNumberFormat(u),
            getTimeFormat: (u, e, t) => userLocale.getTimeFormat(u, e, void 0 === t || t),
            getTimeString: (u, e, t) => userLocale.getTimeString(u, e, void 0 === t || t),
          };
        let l;
        !(function (u) {
          ((u[(u.UNDEFINED = 0)] = "UNDEFINED"),
            (u[(u.TOOLTIP = 1)] = "TOOLTIP"),
            (u[(u.POP_OVER = 2)] = "POP_OVER"),
            (u[(u.CONTEXT_MENU = 4)] = "CONTEXT_MENU"),
            (u[(u.DROP_DOWN = 8)] = "DROP_DOWN"),
            (u[(u.MOVE = 16)] = "MOVE"),
            (u[(u.CLOSE = 32)] = "CLOSE"),
            (u[(u.MINIMIZE = 64)] = "MINIMIZE"));
        })(l || (l = {}));
        const o = Object.freeze({ INTEGRAL: 0, GOLD: 1 }),
          E = Object.freeze({ FRACTIONAL: 0, WO_ZERO_DIGITS: 1 }),
          A = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1 }),
          _ = Object.freeze({ SHORT_FORMAT: 0, LONG_FORMAT: 1, YEAR_MONTH: 2 });
        var F = t(5521),
          c = t(3138);
        const D = ["args"];
        function d(u, e, t, a, n, r, i) {
          try {
            var s = u[r](i),
              l = s.value;
          } catch (u) {
            return void t(u);
          }
          s.done ? e(l) : Promise.resolve(l).then(a, n);
        }
        const m = (u) => ({
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
                  return new Promise(function (a, n) {
                    var r = u.apply(e, t);
                    function i(u) {
                      d(r, a, n, i, s, "next", u);
                    }
                    function s(u) {
                      d(r, a, n, i, s, "throw", u);
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
                r = (function (u, e) {
                  if (null == u) return {};
                  var t,
                    a,
                    n = {},
                    r = Object.keys(u);
                  for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                  return n;
                })(e, D);
              void 0 !== n
                ? viewEnv.handleViewEvent(
                    Object.assign({ __Type: t, type: u }, r, {
                      arguments:
                        ((a = n),
                        Object.entries(a).map(([u, e]) => {
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
                : viewEnv.handleViewEvent(Object.assign({ __Type: t, type: u }, r));
            } else viewEnv.handleViewEvent({ __Type: t, type: u });
            var a;
          },
          h = () => C(l.CLOSE),
          g = (u, e) => {
            u.keyCode === F.n.ESCAPE && e();
          };
        var v = t(7572);
        const p = n.instance,
          b = {
            DataTracker: r.Z,
            ViewModel: v.Z,
            ViewEventType: l,
            NumberFormatType: o,
            RealFormatType: E,
            TimeFormatType: A,
            DateFormatType: _,
            makeGlobalBoundingBox: m,
            sendMoveEvent: (u) => C(l.MOVE, { isMouseEvent: !0, on: u }),
            sendCloseEvent: h,
            sendClosePopOverEvent: () => C(l.POP_OVER, { on: !1 }),
            sendShowContextMenuEvent: (u, e, t = 0) => {
              C(l.CONTEXT_MENU, {
                isMouseEvent: !0,
                contentID: u,
                on: !0,
                decoratorID: t,
                args: e,
              });
            },
            sendShowPopOverEvent: (u, e, t, a, n = R.invalid("resId"), r) => {
              const i = c.O.view.getViewGlobalPosition(),
                s = t.getBoundingClientRect(),
                o = s.x,
                E = s.y,
                A = s.width,
                _ = s.height,
                F = {
                  x: c.O.view.pxToRem(o) + i.x,
                  y: c.O.view.pxToRem(E) + i.y,
                  width: c.O.view.pxToRem(A),
                  height: c.O.view.pxToRem(_),
                };
              C(l.POP_OVER, {
                isMouseEvent: !0,
                contentID: u,
                decoratorID: a || R.invalid("resId"),
                targetID: n,
                direction: e,
                bbox: m(F),
                on: !0,
                args: r,
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
            isTooltipShown: () => viewEnv.isWindowShownByViewEvent(l.TOOLTIP),
            isContextMenuShown: () => viewEnv.isWindowShownByViewEvent(l.CONTEXT_MENU),
            isPopOverShown: () => viewEnv.isWindowShownByViewEvent(l.POP_OVER),
            dumpViewModel: function u(e) {
              const t = {};
              if ("object" != typeof e) return e;
              for (const a in e)
                if (Object.prototype.hasOwnProperty.call(e, a)) {
                  const n = Object.prototype.toString.call(e[a]);
                  if (n.startsWith("[object CoherentArrayProxy]")) {
                    const n = e[a];
                    t[a] = [];
                    for (let e = 0; e < n.length; e++) t[a].push({ value: u(n[e].value) });
                  } else
                    n.startsWith("[object class BW::WULF::ViewModel")
                      ? (t[a] = u(e[a]))
                      : (t[a] = e[a]);
                }
              return t;
            },
            ClickOutsideManager: p,
            SystemLocale: i,
            UserLocale: s,
          };
        window.ViewEnvHelper = b;
      },
      3418: (u, e, t) => {
        "use strict";
        var a = t(7739),
          n = t(6179),
          r = t.n(n),
          i = t(6483),
          s = t.n(i),
          l = t(926),
          o = t.n(l),
          E = t(5415);
        const A = ["children", "className"];
        function _() {
          return (
            (_ =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (u[a] = t[a]);
                }
                return u;
              }),
            _.apply(this, arguments)
          );
        }
        const F = {
            [E.fd.ExtraSmall]: "",
            [E.fd.Small]: o().SMALL_WIDTH,
            [E.fd.Medium]: `${o().SMALL_WIDTH} ${o().MEDIUM_WIDTH}`,
            [E.fd.Large]: `${o().SMALL_WIDTH} ${o().MEDIUM_WIDTH} ${o().LARGE_WIDTH}`,
            [E.fd.ExtraLarge]:
              `${o().SMALL_WIDTH} ${o().MEDIUM_WIDTH} ${o().LARGE_WIDTH} ${o().EXTRA_LARGE_WIDTH}`,
          },
          c = {
            [E.Aq.ExtraSmall]: "",
            [E.Aq.Small]: o().SMALL_HEIGHT,
            [E.Aq.Medium]: `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT}`,
            [E.Aq.Large]: `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT} ${o().LARGE_HEIGHT}`,
            [E.Aq.ExtraLarge]:
              `${o().SMALL_HEIGHT} ${o().MEDIUM_HEIGHT} ${o().LARGE_HEIGHT} ${o().EXTRA_LARGE_HEIGHT}`,
          },
          D = {
            [E.cJ.ExtraSmall]: "",
            [E.cJ.Small]: o().SMALL,
            [E.cJ.Medium]: `${o().SMALL} ${o().MEDIUM}`,
            [E.cJ.Large]: `${o().SMALL} ${o().MEDIUM} ${o().LARGE}`,
            [E.cJ.ExtraLarge]: `${o().SMALL} ${o().MEDIUM} ${o().LARGE} ${o().EXTRA_LARGE}`,
          },
          d = (u) => {
            let e = u.children,
              t = u.className,
              a = (function (u, e) {
                if (null == u) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(u);
                for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, A);
            const n = (0, E.GS)(),
              i = n.mediaWidth,
              l = n.mediaHeight,
              o = n.mediaSize;
            return r().createElement("div", _({ className: s()(t, F[i], c[l], D[o]) }, a), e);
          },
          m = ["children"];
        const B = (u) => {
          let e = u.children,
            t = (function (u, e) {
              if (null == u) return {};
              var t,
                a,
                n = {},
                r = Object.keys(u);
              for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
              return n;
            })(u, m);
          return r().createElement(a.ZN, null, r().createElement(d, t, e));
        };
        var C = t(493),
          h = t.n(C);
        function g(u) {
          engine.call("PlaySound", u);
        }
        var v = t(4179);
        const p = [
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
        function b(u) {
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
        const f = (u, e, t = {}, a = 0) => {
            viewEnv.handleViewEvent(
              Object.assign(
                {
                  __Type: "GFViewEventProxy",
                  type: v.B0.TOOLTIP,
                  contentID: u,
                  decoratorID: e,
                  targetID: a,
                },
                t,
              ),
            );
          },
          x = (u) => {
            let e = u.children,
              t = u.contentId,
              a = u.args,
              r = u.onMouseEnter,
              i = u.onMouseLeave,
              s = u.onMouseDown,
              l = u.onClick,
              o = u.ignoreShowDelay,
              E = void 0 !== o && o,
              A = u.ignoreMouseClick,
              _ = void 0 !== A && A,
              F = u.decoratorId,
              c = void 0 === F ? 0 : F,
              D = u.isEnabled,
              d = void 0 === D || D,
              m = u.targetId,
              B = void 0 === m ? 0 : m,
              C = u.onShow,
              h = u.onHide,
              g = (function (u, e) {
                if (null == u) return {};
                var t,
                  a,
                  n = {},
                  r = Object.keys(u);
                for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                return n;
              })(u, p);
            const v = (0, n.useRef)({
                timeoutId: 0,
                isVisible: !1,
                prevTarget: null,
                hideTimerId: null,
              }),
              x = (0, n.useMemo)(
                () =>
                  B ||
                  ((u = 1) => {
                    const e = new Error().stack;
                    let t,
                      a = R.invalid("resId");
                    return (
                      e &&
                        ((t = e.split("\n")[u].split(".js")[0].split("/").pop() || ""),
                        window.__feature &&
                          window.__feature !== t &&
                          window.subViews[t] &&
                          (a = window.subViews[t].id)),
                      { caller: t, stack: e, resId: a }
                    );
                  })().resId,
                [B],
              ),
              w = (0, n.useCallback)(() => {
                (v.current.isVisible && v.current.timeoutId) ||
                  (f(t, c, { isMouseEvent: !0, on: !0, arguments: b(a) }, x),
                  C && C(),
                  (v.current.isVisible = !0));
              }, [t, c, a, x, C]),
              L = (0, n.useCallback)(() => {
                if (v.current.isVisible || v.current.timeoutId) {
                  const u = v.current.timeoutId;
                  (u > 0 && (clearTimeout(u), (v.current.timeoutId = 0)),
                    f(t, c, { on: !1 }, x),
                    v.current.isVisible && h && h(),
                    (v.current.isVisible = !1));
                }
              }, [t, c, x, h]),
              T = (0, n.useCallback)((u) => {
                v.current.isVisible &&
                  ((v.current.prevTarget = document.elementFromPoint(u.clientX, u.clientY)),
                  (v.current.hideTimerId = window.setTimeout(() => {
                    const e = document.elementFromPoint(u.clientX, u.clientY);
                    e && !e.isSameNode(v.current.prevTarget) && L();
                  }, 200)));
              }, []);
            ((0, n.useEffect)(() => {
              const u = v.current.hideTimerId;
              return (
                document.addEventListener("wheel", T, { capture: !0 }),
                () => {
                  (document.removeEventListener("wheel", T, { capture: !0 }),
                    u && window.clearTimeout(u));
                }
              );
            }, []),
              (0, n.useEffect)(() => {
                !1 === d && L();
              }, [d, L]),
              (0, n.useEffect)(
                () => (
                  window.addEventListener("mouseleave", L),
                  () => {
                    (window.removeEventListener("mouseleave", L), L());
                  }
                ),
                [L],
              ));
            return d
              ? (0, n.cloneElement)(
                  e,
                  Object.assign(
                    {
                      onMouseEnter:
                        ((M = e.props.onMouseEnter),
                        (u) => {
                          (u.clientX === window.innerWidth && u.clientY === window.innerHeight) ||
                            ((v.current.timeoutId = window.setTimeout(w, E ? 100 : 400)),
                            r && r(u),
                            M && M(u));
                        }),
                      onMouseLeave: ((u) => (e) => {
                        (L(), null == i || i(e), null == u || u(e));
                      })(e.props.onMouseLeave),
                      onClick: ((u) => (e) => {
                        (!1 === _ && L(), null == l || l(e), null == u || u(e));
                      })(e.props.onClick),
                      onMouseDown: ((u) => (e) => {
                        (!1 === _ && L(), null == s || s(e), null == u || u(e));
                      })(e.props.onMouseDown),
                    },
                    g,
                  ),
                )
              : e;
            var M;
          },
          w = ({ tooltipArgs: u, children: e }) => (u ? r().createElement(x, u, e) : e),
          L = "PaginationRender_base_75",
          T = "PaginationRender_base__completed_69",
          M = "PaginationRender_base__inaccessible_55",
          S = "PaginationRender_base__selected_e1",
          y = "PaginationRender_selectedImage_58",
          O = ({
            className: u,
            index: e,
            onClick: t,
            isSelected: a,
            isCompleted: i,
            isInaccessible: l,
            tooltipArgs: o,
          }) => {
            const E = s()(L, a && S, i && T, l && M, u),
              A = (0, n.useCallback)(() => {
                (t(e), g("yes1"));
              }, [e, t]),
              _ = (0, n.useCallback)(() => {
                g("highlight");
              }, []);
            return r().createElement(
              w,
              { tooltipArgs: o },
              r().createElement(
                "div",
                { className: E, onClick: A, onMouseEnter: _ },
                a && r().createElement("span", { className: y }),
                e + 1,
              ),
            );
          },
          P = "PaginationList_base_94",
          k = "PaginationList_item_58",
          N = "PaginationList_item__last_ec";
        function I() {
          return (
            (I =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (u[a] = t[a]);
                }
                return u;
              }),
            I.apply(this, arguments)
          );
        }
        const H = ({ className: u, selectedStep: e, data: t, onChange: a }) => {
            const i = t.length - 1,
              l = s()(P, u),
              o = (0, n.useCallback)(
                (u) => {
                  a(u);
                },
                [a],
              );
            return r().createElement(
              "div",
              { className: l },
              t.map((u, t) =>
                r().createElement(
                  O,
                  I(
                    {
                      onClick: o,
                      index: t,
                      className: s()(k, t === i && N),
                      isSelected: e === t,
                      key: t,
                    },
                    u,
                  ),
                ),
              ),
            );
          },
          G = {
            base: "PaginationArrowButton_base_32",
            icon: "PaginationArrowButton_icon_15",
            icon__back: "PaginationArrowButton_icon__back_d0",
            icon__forward: "PaginationArrowButton_icon__forward_f6",
            base__locked: "PaginationArrowButton_base__locked_a9",
          };
        let W;
        !(function (u) {
          ((u.Back = "back"), (u.Forward = "forward"));
        })(W || (W = {}));
        const U = ({ onClick: u, direction: e, isLocked: t, tooltipArgs: a, className: i }) => {
            const l = s()(G.icon, G[`icon__${e}`]),
              o = (0, n.useCallback)(() => {
                t || (u(), g("play"));
              }, [u, t]),
              E = (0, n.useCallback)(() => {
                t || g("highlight");
              }, [t]),
              A = s()(G.base, t && G.base__locked, i);
            return r().createElement(
              w,
              { tooltipArgs: a },
              r().createElement(
                "div",
                { className: A },
                r().createElement("div", { className: l, onClick: o, onMouseEnter: E }),
              ),
            );
          },
          j = "Pagination_base_50",
          V = "Pagination_content_0e",
          X = "Pagination_list_9e",
          Z = ({ className: u, hasArrow: e, arrowOffset: t, selectedIndex: a, children: i }) => {
            t = t || 0;
            const l = (0, n.useMemo)(
                () =>
                  i.map((u) => ({
                    isInaccessible: u.isInaccessible,
                    isCompleted: u.isCompleted,
                    tooltipArgs: u.tooltipArgs,
                  })),
                [i],
              ),
              o = i.length - 1,
              E = (0, n.useMemo)(() => {
                const u = l.findIndex(
                  (u) => void 0 === u.isInaccessible && void 0 === u.isCompleted,
                );
                return -1 === u ? 0 : u;
              }, [l]),
              A = (0, n.useState)(a || E),
              _ = A[0],
              F = A[1],
              c = (0, n.useCallback)(
                (u) => {
                  F(u);
                },
                [F],
              ),
              D = (0, n.useCallback)(() => {
                F(_ - 1);
              }, [F, _]),
              d = (0, n.useCallback)(() => {
                F(_ + 1);
              }, [F, _]),
              m = s()(j, u),
              B = (0, n.useMemo)(() => ({ marginLeft: t, marginRight: t }), [t]),
              C = 0 === _,
              h = _ === o,
              g = (0, n.useMemo)(() => (C ? void 0 : i[_ - 1].tooltipArgs), [i, C, _]),
              v = (0, n.useMemo)(() => (h ? void 0 : i[_ + 1].tooltipArgs), [i, h, _]);
            return r().createElement(
              "div",
              { className: m },
              r().createElement(
                "div",
                { className: V },
                e &&
                  r().createElement(U, {
                    onClick: D,
                    direction: W.Back,
                    isLocked: C,
                    tooltipArgs: g,
                  }),
                r().createElement("div", { style: B }, i[_].render()),
                e &&
                  r().createElement(U, {
                    onClick: d,
                    direction: W.Forward,
                    isLocked: h,
                    tooltipArgs: v,
                  }),
              ),
              r().createElement(H, { className: X, selectedStep: _, data: l, onChange: c }),
            );
          },
          $ = {
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
          Y = [
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
        function K() {
          return (
            (K =
              Object.assign ||
              function (u) {
                for (var e = 1; e < arguments.length; e++) {
                  var t = arguments[e];
                  for (var a in t) Object.prototype.hasOwnProperty.call(t, a) && (u[a] = t[a]);
                }
                return u;
              }),
            K.apply(this, arguments)
          );
        }
        class q extends r().PureComponent {
          constructor(...u) {
            (super(...u),
              (this.state = { hover: !1, click: !1 }),
              (this._onMouseEnter = (u) => (e) => {
                (u && u(e),
                  this.setState({ hover: !0 }),
                  this.props.soundHover && g(this.props.soundHover));
              }),
              (this._onMouseLeave = (u) => (e) => {
                (u && u(e), this.setState({ hover: !1, click: !1 }));
              }),
              (this._onMouseDown = (u) => (e) => {
                (u && u(e),
                  this.setState({ click: !0 }),
                  this.props.soundClick && g(this.props.soundClick));
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
              a = u.goto,
              n = u.side,
              i = u.type,
              l = u.classNames,
              o = u.onMouseEnter,
              E = u.onMouseLeave,
              A = u.onMouseDown,
              _ = u.onMouseUp,
              F =
                (u.soundClick,
                u.soundHover,
                (function (u, e) {
                  if (null == u) return {};
                  var t,
                    a,
                    n = {},
                    r = Object.keys(u);
                  for (a = 0; a < r.length; a++) ((t = r[a]), e.indexOf(t) >= 0 || (n[t] = u[t]));
                  return n;
                })(u, Y)),
              c = s()($.base, $[`base__${i}`], $[`base__${n}`], null == l ? void 0 : l.base),
              D = s()($.icon, $[`icon__${i}`], $[`icon__${n}`], null == l ? void 0 : l.icon),
              d = s()($.glow, null == l ? void 0 : l.glow),
              m = s()($.caption, $[`caption__${i}`], null == l ? void 0 : l.caption),
              B = s()($.goto, null == l ? void 0 : l.goto);
            return r().createElement(
              "div",
              K(
                {
                  className: c,
                  onMouseEnter: this._onMouseEnter(o),
                  onMouseLeave: this._onMouseLeave(E),
                  onMouseDown: this._onMouseDown(A),
                  onMouseUp: this._onMouseUp(_),
                  onFocus: this.handleFocus,
                  onBlur: this.handleBlur,
                  onClick: t,
                },
                F,
              ),
              "info" !== i && r().createElement("div", { className: $.shine }),
              r().createElement(
                "div",
                { className: D },
                r().createElement("div", { className: d }),
              ),
              r().createElement("div", { className: m }, e),
              a && r().createElement("div", { className: B }, a),
            );
          }
        }
        q.defaultProps = {
          side: "left",
          type: "back",
          soundHover: "highlight",
          soundClick: "play",
        };
        var z = t(3138),
          J = t(5521);
        const Q = (u) => {
          console.error(u.type + ": useKeydownListener hook :: Callback is not defined");
        };
        function uu(u = J.n.NONE, e = Q, t = !1) {
          (0, n.useEffect)(() => {
            if (u !== J.n.NONE)
              return (
                window.addEventListener("keydown", a, t),
                () => {
                  window.removeEventListener("keydown", a, t);
                }
              );
            function a(a) {
              if (a.keyCode === u) {
                if (z.O.view.isEventHandled()) return;
                (z.O.view.setEventHandled(), e(a), t && a.stopPropagation());
              }
            }
          }, [e, u, t]);
        }
        function eu() {
          !(function (u = J.n.ESCAPE) {
            uu(u, v.Sy, !0);
          })(J.n.ESCAPE);
        }
        var tu = t(9480),
          au = t(3403);
        let nu;
        !(function (u) {
          ((u[(u.TECH = 0)] = "TECH"),
            (u[(u.LIMIT = 1)] = "LIMIT"),
            (u[(u.DAILY = 2)] = "DAILY"),
            (u[(u.BATTLE = 3)] = "BATTLE"),
            (u[(u.EPIC_BATTLE_POINTS = 4)] = "EPIC_BATTLE_POINTS"),
            (u[(u.COMP7 = 5)] = "COMP7"));
        })(nu || (nu = {}));
        function ru() {
          return !1;
        }
        console.log;
        var iu = t(9174);
        function su(u, e) {
          var t = ("undefined" != typeof Symbol && u[Symbol.iterator]) || u["@@iterator"];
          if (t) return (t = t.call(u)).next.bind(t);
          if (
            Array.isArray(u) ||
            (t = (function (u, e) {
              if (!u) return;
              if ("string" == typeof u) return lu(u, e);
              var t = Object.prototype.toString.call(u).slice(8, -1);
              "Object" === t && u.constructor && (t = u.constructor.name);
              if ("Map" === t || "Set" === t) return Array.from(u);
              if ("Arguments" === t || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(t))
                return lu(u, e);
            })(u)) ||
            (e && u && "number" == typeof u.length)
          ) {
            t && (u = t);
            var a = 0;
            return function () {
              return a >= u.length ? { done: !0 } : { done: !1, value: u[a++] };
            };
          }
          throw new TypeError(
            "Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.",
          );
        }
        function lu(u, e) {
          (null == e || e > u.length) && (e = u.length);
          for (var t = 0, a = new Array(e); t < e; t++) a[t] = u[t];
          return a;
        }
        const ou = (u) => (0 === u ? window : window.subViews.get(u));
        var Eu = t(3946);
        const Au = { cardType: nu.BATTLE, viewId: "", vehiclesList: [] },
          _u = ((u, e) => {
            const t = (0, n.createContext)({});
            return [
              function ({ mode: a = "real", options: i, children: s, mocks: l }) {
                const o = (0, n.useRef)([]),
                  E = (t, a, n) => {
                    var r;
                    const i = (function ({
                        initializer: u = !0,
                        rootId: e = 0,
                        getRoot: t = ou,
                        context: a = "model",
                      } = {}) {
                        const n = new Map();
                        function r(u, e = 0) {
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
                        const i = (u) => {
                          const n = t(e),
                            r = a.split(".").reduce((u, e) => u[e], n);
                          return "string" != typeof u || 0 === u.length
                            ? r
                            : u.split(".").reduce((u, e) => {
                                const t = u[e];
                                return "function" == typeof t ? t.bind(u) : t;
                              }, r);
                        };
                        return {
                          subscribe: (t, r) => {
                            const s = "string" == typeof r ? `${a}.${r}` : a,
                              l = z.O.view.addModelObserver(s, e, !0);
                            return (n.set(l, t), u && t(i(r)), l);
                          },
                          readByPath: i,
                          createCallback: (u, e) => {
                            const t = i(e);
                            return (...e) => {
                              t(u(...e));
                            };
                          },
                          createCallbackNoArgs: (u) => {
                            const e = i(u);
                            return () => {
                              e();
                            };
                          },
                          dispose: function () {
                            for (var u, t = su(n.keys()); !(u = t()).done;) r(u.value, e);
                          },
                          unsubscribe: r,
                        };
                      })(a),
                      s =
                        "real" === t
                          ? i
                          : Object.assign({}, i, {
                              readByPath:
                                null != (r = null == n ? void 0 : n.getter) ? r : () => {},
                            }),
                      l = (u) =>
                        "mocks" === t ? (null == n ? void 0 : n.getter(u)) : s.readByPath(u),
                      E = (u) => o.current.push(u),
                      A = u({
                        mode: t,
                        readByPath: l,
                        externalModel: s,
                        observableModel: {
                          array: (u, e) => {
                            const a = null != e ? e : l(u),
                              n = iu.LO.box(a, { equals: ru });
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, iu.aD)((u) => n.set(u)),
                                  u,
                                ),
                              n
                            );
                          },
                          object: (u, e) => {
                            const a = null != e ? e : l(u),
                              n = iu.LO.box(a, { equals: ru });
                            return (
                              "real" === t &&
                                s.subscribe(
                                  (0, iu.aD)((u) => n.set(u)),
                                  u,
                                ),
                              n
                            );
                          },
                          primitives: (u, e) => {
                            const a = l(e);
                            if (Array.isArray(u)) {
                              const n = u.reduce((u, e) => ((u[e] = iu.LO.box(a[e], {})), u), {});
                              return (
                                "real" === t &&
                                  s.subscribe(
                                    (0, iu.aD)((e) => {
                                      u.forEach((u) => {
                                        n[u].set(e[u]);
                                      });
                                    }),
                                    e,
                                  ),
                                n
                              );
                            }
                            {
                              const n = u,
                                r = Object.entries(n),
                                i = r.reduce((u, [e, t]) => ((u[t] = iu.LO.box(a[e], {})), u), {});
                              return (
                                "real" === t &&
                                  s.subscribe(
                                    (0, iu.aD)((u) => {
                                      r.forEach(([e, t]) => {
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
                        cleanup: E,
                      }),
                      _ = { mode: t, model: A, externalModel: s, cleanup: E };
                    return {
                      model: A,
                      controls: "mocks" === t && n ? n.controls(_) : e(_),
                      externalModel: s,
                      mode: t,
                    };
                  },
                  A = (0, n.useRef)(!1),
                  _ = (0, n.useState)(a),
                  F = _[0],
                  c = _[1],
                  D = (0, n.useState)(() => E(a, i, l)),
                  d = D[0],
                  m = D[1];
                return (
                  (0, n.useEffect)(() => {
                    A.current ? m(E(F, i, l)) : (A.current = !0);
                  }, [l, F, i]),
                  (0, n.useEffect)(() => {
                    c(a);
                  }, [a]),
                  (0, n.useEffect)(
                    () => () => {
                      (d.externalModel.dispose(), o.current.forEach((u) => u()));
                    },
                    [d],
                  ),
                  r().createElement(t.Provider, { value: d }, s)
                );
              },
              () => (0, n.useContext)(t),
            ];
          })(
            ({ observableModel: u }) => {
              const e = { root: u.object(), gameModes: u.array("gameModes") },
                t = (0, Eu.Om)(() => tu.UI(e.gameModes.get(), (u) => u)),
                a = (0, Eu.Om)((u) => tu.U2(t(), u), { equals: ru }),
                n = (0, Eu.Om)(
                  (u, e) => {
                    var t;
                    return tu.U2((null == (t = a(e)) ? void 0 : t.cards) || [], u) || Au;
                  },
                  { equals: ru },
                );
              return Object.assign({}, e, { computes: { getItems: t, getSlide: a, getCard: n } });
            },
            ({ externalModel: u }) => ({
              openLink: u.createCallback((u) => ({ viewId: u }), "onLinkClick"),
            }),
          ),
          Fu = _u[0],
          cu = _u[1],
          Du = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"],
          du = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1e3];
        const mu = ["ko", "no"].includes(R.strings.settings.LANGUAGE_CODE()),
          Bu = (u) =>
            mu
              ? `${u}`
              : (function (u) {
                  let e = "";
                  for (let t = du.length - 1; t >= 0; t--)
                    for (; u >= du[t];) ((e += Du[t]), (u -= du[t]));
                  return e;
                })(u);
        var Cu = t(3649);
        let hu;
        !(function (u) {
          ((u[(u.REGULAR = 1)] = "REGULAR"),
            (u[(u.SORTIE_2 = 20)] = "SORTIE_2"),
            (u[(u.FORT_BATTLE_2 = 21)] = "FORT_BATTLE_2"),
            (u[(u.RANKED = 22)] = "RANKED"),
            (u[(u.EPIC_BATTLE = 27)] = "EPIC_BATTLE"),
            (u[(u.BATTLE_ROYALE_SOLO = 29)] = "BATTLE_ROYALE_SOLO"),
            (u[(u.BATTLE_ROYALE_SQUAD = 30)] = "BATTLE_ROYALE_SQUAD"),
            (u[(u.COMP7 = 43)] = "COMP7"),
            (u[(u.VERSUS_AI = 50)] = "VERSUS_AI"));
        })(hu || (hu = {}));
        const gu = "Table_base_61",
          vu = "Table_row_d4",
          pu = "Table_row__head_19",
          bu = "Table_row__content_6b",
          fu = "Table_cell_8e",
          xu = "Table_cell__text_8c",
          wu = "Table_cell__wide_52",
          Lu = "Table_cell__wideHead_0b",
          Tu = "Table_cell__inFirstRow_49",
          Mu = "Table_points_dc",
          Su = ({ tableRows: u, arenaBonusType: e }) => {
            const t = tu.U2(u, 1),
              a = u.length > 1 ? (null == t ? void 0 : t.cell) : null;
            return r().createElement(
              "div",
              { className: gu },
              tu.UI(u, (u, t) => {
                const n = s()(vu, 0 === t && pu, 0 !== t && bu),
                  i = a && 0 !== t && e === hu.COMP7;
                return r().createElement(
                  "div",
                  { key: t, className: n },
                  tu.UI(u.cell, ({ text: u, points: n }, l) => {
                    const o = s()(
                      fu,
                      a && a[l].value.text && xu,
                      i && a && a[l].value.text && wu,
                      0 === t && Tu,
                      0 === t && 0 === l && e === hu.COMP7 && Lu,
                    );
                    return r().createElement(
                      "div",
                      { className: o, lang: R.strings.settings.LANGUAGE_CODE(), key: l },
                      n ? r().createElement("div", { className: Mu }, n) : u,
                    );
                  }),
                );
              }),
            );
          },
          yu = {
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
        let Ou, Ru;
        (!(function (u) {
          ((u.main = "main"),
            (u.primary = "primary"),
            (u.primaryGreen = "primaryGreen"),
            (u.primaryRed = "primaryRed"),
            (u.secondary = "secondary"),
            (u.ghost = "ghost"));
        })(Ou || (Ou = {})),
          (function (u) {
            ((u.extraSmall = "extraSmall"), (u.small = "small"), (u.medium = "medium"));
          })(Ru || (Ru = {})));
        const Pu = ({
          children: u,
          size: e,
          isFocused: t,
          type: a,
          disabled: i,
          mixClass: l,
          soundHover: o,
          soundClick: E,
          onMouseEnter: A,
          onMouseMove: _,
          onMouseDown: F,
          onMouseUp: c,
          onMouseLeave: D,
          onClick: d,
        }) => {
          const m = (0, n.useRef)(null),
            B = (0, n.useState)(t),
            C = B[0],
            h = B[1],
            v = (0, n.useState)(!1),
            p = v[0],
            b = v[1],
            f = (0, n.useState)(!1),
            x = f[0],
            w = f[1],
            L = (0, n.useCallback)(() => {
              i || (m.current && (m.current.focus(), h(!0)));
            }, [i]),
            T = (0, n.useCallback)(
              (u) => {
                C && null !== m.current && !m.current.contains(u.target) && h(!1);
              },
              [C],
            ),
            M = (0, n.useCallback)(
              (u) => {
                i || (d && d(u));
              },
              [i, d],
            ),
            S = (0, n.useCallback)(
              (u) => {
                i || (null !== o && g(o), A && A(u), w(!0));
              },
              [i, o, A],
            ),
            y = (0, n.useCallback)(
              (u) => {
                _ && _(u);
              },
              [_],
            ),
            O = (0, n.useCallback)(
              (u) => {
                i || (c && c(u), b(!1));
              },
              [i, c],
            ),
            P = (0, n.useCallback)(
              (u) => {
                i || (null !== E && g(E), F && F(u), t && L(), b(!0));
              },
              [i, E, F, L, t],
            ),
            k = (0, n.useCallback)(
              (u) => {
                i || (D && D(u), b(!1));
              },
              [i, D],
            ),
            N = s()(
              yu.base,
              yu[`base__${a}`],
              {
                [yu.base__disabled]: i,
                [yu[`base__${e}`]]: e,
                [yu.base__focus]: C,
                [yu.base__highlightActive]: p,
                [yu.base__firstHover]: x,
              },
              l,
            ),
            I = s()(yu.state, yu.state__default);
          return (
            (0, n.useEffect)(
              () => (
                document.addEventListener("mousedown", T),
                () => {
                  document.removeEventListener("mousedown", T);
                }
              ),
              [T],
            ),
            (0, n.useEffect)(() => {
              h(t);
            }, [t]),
            r().createElement(
              "div",
              {
                ref: m,
                className: N,
                onMouseEnter: S,
                onMouseMove: y,
                onMouseUp: O,
                onMouseDown: P,
                onMouseLeave: k,
                onClick: M,
              },
              a !== Ou.ghost &&
                r().createElement(
                  r().Fragment,
                  null,
                  r().createElement("div", { className: yu.back }),
                  r().createElement("span", { className: yu.texture }),
                ),
              r().createElement(
                "span",
                { className: I },
                r().createElement("span", { className: yu.stateDisabled }),
                r().createElement("span", { className: yu.stateHighlightHover }),
                r().createElement("span", { className: yu.stateHighlightActive }),
              ),
              r().createElement(
                "span",
                { className: yu.content, lang: R.strings.settings.LANGUAGE_CODE() },
                u,
              ),
            )
          );
        };
        Pu.defaultProps = {
          type: Ou.primary,
          isFocused: !1,
          soundHover: "highlight",
          soundClick: "play",
        };
        const ku = (0, n.memo)(Pu);
        var Nu = t(7613),
          Iu = t(9243);
        const Hu = "Card_base_cd",
          Gu = "Card_base__small_ec",
          Wu = "Card_text_d5",
          Uu = "Card_image_1e",
          ju = "Card_pointsIcon_11",
          Vu = "Card_vehicleBonusListContainer_71",
          Xu = "Card_backgroundImage_43",
          Zu = "Card_cardTitle_e7",
          $u = R.strings.battle_pass.howToEarnPoints.card,
          Yu = R.images.gui.maps.icons.battlePass,
          Ku = {
            [nu.TECH]: {
              title: $u.specialVehicle.title(),
              text: $u.specialVehicle.text(),
              vehicleBonusPoints: 80,
            },
            [nu.LIMIT]: {
              title: $u.limitPoints.title(),
              text: $u.limitPoints.text(),
              image: { small: Yu.tooltips.points_reward(), large: Yu.tooltips.points_136() },
              backgroundImage: {
                small: Yu.how_to_earn_points.godrays_157x157(),
                large: Yu.how_to_earn_points.godrays_210x210(),
              },
            },
            [nu.DAILY]: {
              title: $u.daily.title(),
              text: $u.daily.text(),
              linkText: $u.daily.linkText(),
              image: {
                small: Yu.how_to_earn_points.quest_80x80(),
                large: Yu.how_to_earn_points.quest_136x136(),
              },
            },
            [nu.BATTLE]: {
              title: $u.battle.title(),
              text: $u.battle.text(),
              linkText: $u.battle.linkText(),
              image: {
                small: Yu.how_to_earn_points.quest_80x80(),
                large: Yu.how_to_earn_points.quest_136x136(),
              },
            },
            [nu.EPIC_BATTLE_POINTS]: {
              title: $u.epicBattlePoints.title(),
              text: $u.epicBattlePoints.text(),
              image: { small: Yu.tooltips.points_reward(), large: Yu.tooltips.points_136() },
              backgroundImage: {
                small: Yu.how_to_earn_points.godrays_157x157(),
                large: Yu.how_to_earn_points.godrays_210x210(),
              },
            },
            [nu.COMP7]: {
              title: $u.comp7.title(),
              text: $u.comp7.text(),
              image: {
                small: Yu.how_to_earn_points.quest_80x80(),
                large: Yu.how_to_earn_points.quest_136x136(),
              },
            },
          },
          qu = (0, au.Pi)(({ cardIndex: u, slideIndex: e, isSmall: t = !1 }) => {
            const a = cu(),
              n = a.model,
              i = a.controls,
              l = (0, E.GS)().mediaSize,
              o = n.computes.getCard(u, e),
              A = o.cardType,
              _ = o.viewId,
              F = o.vehiclesList,
              c = l >= E.cJ.Medium,
              D = Ku[A],
              d = D.text,
              m = D.image,
              B = D.backgroundImage,
              C = D.linkText,
              h = D.vehicleBonusPoints,
              g = {
                backgroundImage: `url(${c ? (null == m ? void 0 : m.large) : null == m ? void 0 : m.small})`,
              },
              v = {
                backgroundImage: `url(${c ? (null == B ? void 0 : B.large) : null == B ? void 0 : B.small})`,
              };
            return r().createElement(
              "div",
              { className: s()(Hu, t && Gu) },
              r().createElement(Nu.ZP, { text: Ku[A].title, className: Zu }),
              m &&
                r().createElement(
                  "div",
                  { className: Uu, style: g },
                  B && r().createElement("div", { className: Xu, style: v }),
                ),
              F.length > 0 &&
                r().createElement(
                  "div",
                  { className: Vu },
                  r().createElement(Iu.Y, { vehiclesList: F }),
                ),
              r().createElement(Nu.ZP, {
                text: d,
                className: Wu,
                format: {
                  binding: h
                    ? {
                        textBind: r().createElement(
                          "div",
                          { className: ju },
                          r().createElement(Nu.ZP, { text: String(h) }),
                        ),
                      }
                    : void 0,
                  classMix: Wu,
                },
              }),
              C &&
                _ &&
                r().createElement(
                  ku,
                  { onClick: () => _ && i.openLink(_), size: "small", type: "ghost" },
                  C,
                ),
            );
          }),
          zu = R.images.gui.maps.icons,
          Ju = zu.battleTypes.c_64x64,
          Qu = zu.battleTypes.c_136x136,
          ue = {
            [hu.REGULAR]: { small: Ju.random(), large: Qu.random() },
            [hu.RANKED]: { small: Ju.ranked(), large: Qu.ranked() },
            [hu.BATTLE_ROYALE_SOLO]: { small: Ju.steelhunt(), large: Qu.battle_royale() },
            [hu.EPIC_BATTLE]: { small: Ju.frontline(), large: Qu.epicbattle() },
            [hu.COMP7]: { small: Ju.comp7(), large: Qu.comp7() },
            [hu.SORTIE_2]: { small: Ju.fortifications(), large: Qu.fortifications() },
            [hu.FORT_BATTLE_2]: { small: Ju.fortifications(), large: Qu.fortifications() },
            [hu.VERSUS_AI]: { small: Ju.versusAI(), large: Qu.versusAI() },
          },
          ee = {
            [hu.REGULAR]: { levelRange: [6, 11] },
            [hu.RANKED]: { levelRange: [0] },
            [hu.BATTLE_ROYALE_SOLO]: { levelRange: [0] },
            [hu.EPIC_BATTLE]: { levelRange: [0] },
            [hu.COMP7]: { levelRange: [0] },
          },
          te = "Slide_base_b8",
          ae = "Slide_container_2d",
          ne = "Slide_tableBackground_24",
          re = "Slide_tableContainer_90",
          ie = "Slide_titleContainer_8a",
          se = "Slide_titleImage_f0",
          le = "Slide_title_31",
          oe = "Slide_description_42",
          Ee = "Slide_cards_36",
          Ae = "Slide_cardsWrapper_5d",
          _e = (u, e) => {
            const t = ue[e],
              a = t.small,
              n = t.large;
            return { backgroundImage: `url(${u ? n : a})` };
          },
          Fe = (0, au.Pi)(({ index: u }) => {
            var e;
            const t = cu().model.computes.getSlide(u),
              a = t.title,
              n = t.text,
              i = t.tableRows,
              s = t.cards,
              l = t.arenaBonusType,
              o = (0, E.GS)().mediaSize >= E.cJ.Medium,
              A = (null == (e = ee[l]) ? void 0 : e.levelRange) || [],
              _ = (0, Cu.uF)(
                n,
                2 === A.length ? { startLevel: Bu(A[0]), endLevel: Bu(A[1]) } : { level: Bu(A[0]) },
              );
            return r().createElement(
              "div",
              { className: te },
              r().createElement(
                "div",
                { className: ae },
                r().createElement("div", { className: ne }),
                r().createElement(
                  "div",
                  { className: re },
                  r().createElement("div", { className: se, style: _e(o, l) }),
                  r().createElement(
                    "div",
                    { className: ie },
                    r().createElement("div", { className: le }, a),
                    r().createElement("div", { className: oe }, _),
                  ),
                  r().createElement(Su, { tableRows: i, arenaBonusType: l }),
                ),
                r().createElement(
                  "div",
                  { className: Ee },
                  r().createElement(
                    "div",
                    { className: Ae },
                    tu.UI(s, (e, t) =>
                      r().createElement(qu, {
                        cardIndex: t,
                        slideIndex: u,
                        key: `card-${t}`,
                        isSmall: s.length >= 3,
                      }),
                    ),
                  ),
                ),
              ),
            );
          }),
          ce = "App_base_1c",
          De = "App_animationMain_2b",
          de = "App_mainBg_a3",
          me = "App_dimBg_f6",
          Be = "App_close_6f",
          Ce = "App_titleContainer_46",
          he = "App_title_d4",
          ge = "App_description_af",
          ve = "App_pagination_1a",
          pe = "App_animationBg_04",
          be = R.strings.battle_pass.howToEarnPoints,
          fe = (0, au.Pi)(() => {
            const u = cu().model;
            return (
              eu(),
              r().createElement(
                "div",
                { className: ce },
                r().createElement("div", { className: pe }),
                r().createElement(
                  "div",
                  { className: De },
                  r().createElement(
                    "div",
                    { className: de },
                    r().createElement("div", { className: me }),
                  ),
                  r().createElement(
                    "div",
                    { className: Ce },
                    r().createElement("div", { className: he }, be.title()),
                    r().createElement("div", { className: ge }, be.description()),
                  ),
                  u.computes.getItems().length > 0 &&
                    r().createElement(
                      Z,
                      { hasArrow: !0, selectedIndex: 0, className: ve },
                      tu.UI(u.gameModes.get(), (u, e) => ({
                        render: () => r().createElement(Fe, { key: e, index: e }),
                      })),
                    ),
                  r().createElement(
                    "div",
                    { className: Be },
                    r().createElement(q, {
                      caption: R.strings.menu.viewHeader.closeBtn.label(),
                      type: "close",
                      side: "right",
                      onClick: v.Sy,
                    }),
                  ),
                ),
              )
            );
          });
        engine.whenReady.then(() => {
          h().render(
            r().createElement(Fu, null, r().createElement(B, null, r().createElement(fe, null))),
            document.getElementById("root"),
          );
        });
      },
      6583: (u, e, t) => {
        "use strict";
        t.d(e, { e: () => E });
        var a = t(6483),
          n = t.n(a),
          r = t(7613),
          i = t(6179),
          s = t.n(i);
        const l = {
            base: "VehicleInfo_base_4f",
            base__level1: "VehicleInfo_base__level1_15",
            base__level2: "VehicleInfo_base__level2_28",
            base__level3: "VehicleInfo_base__level3_17",
            base__level4: "VehicleInfo_base__level4_02",
            base__level5: "VehicleInfo_base__level5_bd",
            base__level6: "VehicleInfo_base__level6_ea",
            base__level7: "VehicleInfo_base__level7_0a",
            base__level8: "VehicleInfo_base__level8_27",
            base__level9: "VehicleInfo_base__level9_95",
            base__level10: "VehicleInfo_base__level10_dc",
            base__level11: "VehicleInfo_base__level11_96",
            vehicleType: "VehicleInfo_vehicleType_e2",
            vehicleType__elite: "VehicleInfo_vehicleType__elite_95",
            vehicleName: "VehicleInfo_vehicleName_9e",
            vehicleName__special: "VehicleInfo_vehicleName__special_03",
          },
          o = R.images.gui.maps.icons.vehicleTypes,
          E = ({
            isSpecial: u = !1,
            vehicleLevel: e,
            vehicleName: t,
            vehicleType: a,
            isElite: i,
          }) => {
            const E = ((u, e) => {
                const t = e.replace("-", "_"),
                  a = u ? o.elite : o;
                if ((n = t) in a && "$num" !== n && "$dyn" !== n && "function" == typeof a[t]) {
                  return { backgroundImage: `url(${a.$dyn(t)})` };
                }
                var n;
              })(i, a),
              A = n()(l.base, l[`base__level${e}`]),
              _ = n()(l.vehicleType, i && l.vehicleType__elite);
            return s().createElement(
              "div",
              { className: A },
              s().createElement("div", { className: _, style: E }),
              s().createElement(r.ZP, {
                text: t,
                className: n()(l.vehicleName, u && l.vehicleName__special),
              }),
            );
          };
      },
      9243: (u, e, t) => {
        "use strict";
        t.d(e, { Y: () => F });
        var a = t(280),
          n = t(9480),
          r = t(3649),
          i = t(6179),
          s = t.n(i),
          l = t(6583);
        const o = "VehicleList_base_b7",
          E = "VehicleList_info_5a",
          A = "VehicleList_points_59",
          _ = "VehicleList_top_09",
          F = ({ vehiclesList: u }) => {
            const e = ({
              vehicleLevel: u,
              vehicleName: e,
              vehicleType: t,
              vehicleBonus: a,
              vehicleTop: n,
              isElite: i,
            }) => ({
              vehicle: s().createElement(l.e, {
                isElite: i,
                vehicleLevel: u,
                vehicleName: e,
                vehicleType: t,
                key: "vehicle",
              }),
              bonus: s().createElement(
                "div",
                { className: A, key: "bonus" },
                (0, r.uF)(R.strings.battle_pass.howToEarnPoints.bonus(), { bonus: a }),
              ),
              top: s().createElement(
                "div",
                { className: _, key: "top" },
                (0, r.uF)(R.strings.battle_pass.points.topCount(), { top: n }),
              ),
            });
            return s().createElement(
              "div",
              { className: o },
              n.UI(u, (u, t) =>
                s().createElement(a.z, {
                  classMix: E,
                  text: u.textResource,
                  key: t,
                  binding: e(u),
                }),
              ),
            );
          };
      },
      5026: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => a });
        const a = {
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
        t.d(e, { Z: () => a });
        const a = { base: "FormatText_base_d0" };
      },
      3393: (u, e, t) => {
        "use strict";
        t.d(e, { Z: () => a });
        const a = {
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
    (__webpack_require__.O = (u, e, t, a) => {
      if (!e) {
        var n = 1 / 0;
        for (l = 0; l < deferred.length; l++) {
          for (var [e, t, a] = deferred[l], r = !0, i = 0; i < e.length; i++)
            (!1 & a || n >= a) &&
            Object.keys(__webpack_require__.O).every((u) => __webpack_require__.O[u](e[i]))
              ? e.splice(i--, 1)
              : ((r = !1), a < n && (n = a));
          if (r) {
            deferred.splice(l--, 1);
            var s = t();
            void 0 !== s && (u = s);
          }
        }
        return u;
      }
      a = a || 0;
      for (var l = deferred.length; l > 0 && deferred[l - 1][2] > a; l--)
        deferred[l] = deferred[l - 1];
      deferred[l] = [e, t, a];
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
    (__webpack_require__.j = 3853),
    (() => {
      var u = { 3853: 0, 1243: 0, 2914: 0 };
      __webpack_require__.O.j = (e) => 0 === u[e];
      var e = (e, t) => {
          var a,
            n,
            [r, i, s] = t,
            l = 0;
          if (r.some((e) => 0 !== u[e])) {
            for (a in i) __webpack_require__.o(i, a) && (__webpack_require__.m[a] = i[a]);
            if (s) var o = s(__webpack_require__);
          }
          for (e && e(t); l < r.length; l++)
            ((n = r[l]), __webpack_require__.o(u, n) && u[n] && u[n][0](), (u[n] = 0));
          return __webpack_require__.O(o);
        },
        t = (self.webpackChunkgameface = self.webpackChunkgameface || []);
      (t.forEach(e.bind(null, 0)), (t.push = e.bind(null, t.push.bind(t))));
    })());
  var __webpack_exports__ = __webpack_require__.O(void 0, [1519], () => __webpack_require__(3418));
  __webpack_exports__ = __webpack_require__.O(__webpack_exports__);
})();
